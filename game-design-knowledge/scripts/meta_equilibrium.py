#!/usr/bin/env python3
"""Равновесие меты по матрице матчапов: какие варианты выжили бы у идеальных игроков и какие лишние.

Запуск:
  python3 meta_equilibrium.py metrics/before.json                          # из design_metrics.py
  python3 meta_equilibrium.py metrics/before.json --rate win --row character --col opp_character
  python3 meta_equilibrium.py matchups.csv                                 # квадратная матрица долей побед

Вход:
  - JSON design_metrics.py с разрезом `--by pick,opp_pick`: ключи вида rate:win@pick=A,opp_pick=B
    (pick — то, что выбирает игрок: персонаж, колода, фракция, герой, сборка);
  - или CSV: первая строка — имена вариантов-соперников, первый столбец — имя варианта,
    в ячейке доля побед строки против столбца (0..1). Пустая ячейка берётся как 1 − обратный матчап.
Одна строка матрицы — один вариант выбора; подходит для любой игры с матчапами: файтинг, MOBA, RTS, карточная.

Метод: симметричная антагонистическая игра с выигрышем P(i бьёт j) − 0.5, решается фиктивной игрой
(Schreiber, Game Balance Concepts, Level 9; автобаланс меты — Hernandez et al. 2020).
Матрица сначала симметризуется: A[i][j] = (P[i][j] − P[j][i]) / 2, зеркала = 0.

Что печатает по каждому варианту:
  share     — доля в равновесной мете (0% — вариант не нужен идеальному игроку);
  vs field  — доля побед против равномерного поля (все варианты поровну);
  vs eq     — доля побед против равновесной меты (у вариантов в равновесии ≈ 50%).
Плюс строго доминируемые варианты и эксплуатируемость равномерной меты: насколько лучший вариант
обыгрывает поле из всех вариантов поровну. 0 п.п. — идеальный баланс «каждый вариант жизнеспособен».
Код выхода: 0 — успех, 2 — ошибка ввода.
"""

import argparse
import csv
import io
import json
import math
import re
import sys


def read_text(path):
    try:
        with open(path, encoding="utf-8-sig", newline="") as stream:
            return stream.read()
    except (OSError, UnicodeDecodeError) as err:
        raise SystemExit(f"error: {path}: {err}")


def from_metrics(data, rate, row, col):
    pattern = re.compile(rf"^rate:{re.escape(rate)}@{re.escape(row)}=(.+),{re.escape(col)}=(.+)$")
    cells, low = {}, []
    for key, metric in data.get("metrics", {}).items():
        match = pattern.match(key)
        if match and metric.get("value") is not None:
            cells[match.groups()] = metric["value"]
            if metric.get("low_n"):
                low.append(f"{match.group(1)} vs {match.group(2)} (n={metric.get('n')})")
    if not cells:
        raise SystemExit(f"error: no keys like rate:{rate}@{row}=X,{col}=Y; run design_metrics.py with --by {row},{col}")
    return cells, low


def from_csv(text):
    table = list(csv.reader(io.StringIO(text)))
    if len(table) < 3:
        raise SystemExit("error: CSV needs a header row and at least two picks")
    header = [h.strip() for h in table[0][1:]]
    cells = {}
    for line in table[1:]:
        if not line or not line[0].strip():
            continue
        for opp, value in zip(header, line[1:]):
            if value.strip():
                try:
                    cells[(line[0].strip(), opp)] = float(value)
                except ValueError:
                    raise SystemExit(f"error: not a number: {line[0]} vs {opp}: {value!r}")
    return cells, []


def build_matrix(cells):
    picks = sorted({a for a, _ in cells} | {b for _, b in cells})
    index = {d: i for i, d in enumerate(picks)}
    n = len(picks)
    p = [[math.nan] * n for _ in range(n)]
    for (a, b), value in cells.items():
        if not 0 <= value <= 1:
            raise SystemExit(f"error: win rate out of 0..1: {a} vs {b}: {value}")
        p[index[a]][index[b]] = value
    missing = []
    for i in range(n):
        p[i][i] = 0.5
        for j in range(n):
            if math.isnan(p[i][j]):
                if math.isnan(p[j][i]):
                    missing.append(f"{picks[i]} vs {picks[j]}")
                else:
                    p[i][j] = 1 - p[j][i]
    if missing:
        raise SystemExit("error: missing matchups: " + ", ".join(sorted(set(missing))[:10]))
    payoff = [[(p[i][j] - p[j][i]) / 2 for j in range(n)] for i in range(n)]
    return picks, p, payoff


def fictitious_play(payoff, iterations):
    """Средняя стратегия фиктивной игры; для антагонистических игр сходится к равновесию."""
    n = len(payoff)
    counts = [0] * n
    totals = [0.0] * n  # суммарный выигрыш каждой чистой стратегии против истории соперника
    choice = 0
    for _ in range(iterations):
        counts[choice] += 1
        column = choice
        for i in range(n):
            totals[i] += payoff[i][column]
        choice = max(range(n), key=totals.__getitem__)
    return [c / iterations for c in counts]


def expected(p, row, mix):
    return sum(p[row][j] * mix[j] for j in range(len(mix)))


def dominated(p):
    n = len(p)
    result = []
    for i in range(n):
        for k in range(n):
            if k != i and all(p[k][j] >= p[i][j] for j in range(n) if j not in (i, k)) \
                    and any(p[k][j] > p[i][j] for j in range(n) if j not in (i, k)) and p[k][i] >= 0.5:
                result.append((i, k))
                break
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description="Nash equilibrium of a metagame from a matchup matrix.")
    parser.add_argument("data", help="design_metrics.py JSON or a square CSV matrix of win rates")
    parser.add_argument("--rate", default="win", help="rate field in the metrics file (default: win)")
    parser.add_argument("--row", default="pick", help="row grouping field (default: pick)")
    parser.add_argument("--col", default="opp_pick", help="column grouping field (default: opp_pick)")
    parser.add_argument("--iterations", type=int, default=200000, help="fictitious play iterations")
    parser.add_argument("--min-share", type=float, default=0.01, help="share below this counts as absent")
    parser.add_argument("--json", help="also write the result as JSON")
    args = parser.parse_args(argv)

    text = read_text(args.data)
    if args.data.lower().endswith(".json"):
        try:
            data = json.loads(text)
        except ValueError as err:
            raise SystemExit(f"error: {args.data}: {err}")
        if not isinstance(data, dict) or data.get("tool") != "design_metrics":
            raise SystemExit(f"error: {args.data}: not a design_metrics.py output")
        cells, low = from_metrics(data, args.rate, args.row, args.col)
    else:
        cells, low = from_csv(text)
    picks, p, payoff = build_matrix(cells)
    n = len(picks)
    mix = fictitious_play(payoff, max(args.iterations, 1000))
    uniform = [1 / n] * n
    vs_field = [expected(p, i, uniform) for i in range(n)]
    vs_eq = [expected(p, i, mix) for i in range(n)]
    exploit_eq = max(vs_eq) - 0.5
    exploit_uniform = max(vs_field) - 0.5

    width = max(len(d) for d in picks + ["Pick"])
    print(f"{'Pick':<{width}} {'share':>7} {'vs field':>9} {'vs eq':>7}")
    for i in sorted(range(n), key=lambda i: -mix[i]):
        absent = "  absent" if mix[i] < args.min_share else ""
        print(f"{picks[i]:<{width}} {mix[i]:>7.1%} {vs_field[i]:>9.1%} {vs_eq[i]:>7.1%}{absent}")
    in_eq = sum(1 for s in mix if s >= args.min_share)
    print(f"\nPicks in equilibrium: {in_eq} of {n}")
    print(f"Uniform meta exploitability: {exploit_uniform * 100:+.1f} p.p. "
          f"(best pick vs an even field: {picks[vs_field.index(max(vs_field))]})")
    print(f"Equilibrium accuracy: best response gains {exploit_eq * 100:.2f} p.p. (0 = exact)")
    pairs = dominated(p)
    if pairs:
        print("Strictly dominated (another pick is at least as good against every opponent and beats it):")
        for i, k in pairs:
            print(f"  {picks[i]} <= {picks[k]}")
    if low:
        print("Low-n matchups (treat with care): " + ", ".join(low[:10]))
    if args.json:
        with open(args.json, "w", encoding="utf-8") as stream:
            json.dump({"picks": picks, "share": dict(zip(picks, mix)), "vs_field": dict(zip(picks, vs_field)),
                       "vs_equilibrium": dict(zip(picks, vs_eq)), "uniform_exploitability": exploit_uniform,
                       "dominated": [[picks[i], picks[k]] for i, k in pairs]}, stream, ensure_ascii=False, indent=1)
    return 0


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if isinstance(stream, io.TextIOWrapper):
            stream.reconfigure(errors="backslashreplace")
    try:
        sys.exit(main())
    except SystemExit as exit_:
        if isinstance(exit_.code, str):
            print(exit_.code, file=sys.stderr)
            sys.exit(2)
        raise
