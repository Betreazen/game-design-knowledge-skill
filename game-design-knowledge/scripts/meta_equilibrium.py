#!/usr/bin/env python3
"""Равновесие меты по матрице матчапов: какие варианты годятся идеальному игроку, а какие лишние.

Запуск:
  python3 meta_equilibrium.py metrics/before.json                          # из design_metrics.py
  python3 meta_equilibrium.py metrics/before.json --rate win --row character --col opp_character
  python3 meta_equilibrium.py matchups.csv                                 # квадратная матрица долей побед

Вход:
  - JSON design_metrics.py с разрезом `--by pick,opp_pick`: ключи вида rate:win@pick=A,opp_pick=B
    (pick — то, что выбирает игрок: персонаж, колода, фракция, герой, сборка);
  - или CSV (разделитель запятая или точка с запятой): первая строка — имена вариантов-соперников,
    первый столбец — имя варианта, в ячейке доля побед строки против столбца (0..1).
    Пустая ячейка берётся как 1 − обратный матчап.
Подходит для любой игры с матчапами: файтинг, MOBA, RTS, карточная, настольная.
Имена вариантов не должны содержать запятую: она разделяет поля в ключе метрики.

Метод: симметричная антагонистическая игра с выигрышем A[i][j] = (P[i][j] − P[j][i]) / 2,
решается фиктивной игрой (Schreiber, Game Balance Concepts, Level 9; автобаланс меты — Hernandez et al. 2020).
Все отчётные числа считаются по A: результат = 0.5 + A, то есть ничьи делятся пополам.

Что печатает по каждому варианту:
  share     — доля в найденном равновесии;
  vs field  — ожидаемый результат против равномерного поля (все варианты поровну);
  vs eq     — ожидаемый результат против равновесной меты;
  status    — viable, если vs eq не ниже 50% − eps: вариант годится идеальному игроку.
              Равновесие бывает не единственным, поэтому share 0% само по себе ничего не значит;
              beaten — вариант проигрывает равновесной мете.
Плюс нестрого доминируемые варианты (другой не хуже против всех, включая очную встречу,
и лучше хотя бы в одном матчапе) и эксплуатируемость равномерной меты: насколько лучший вариант
обыгрывает поле из всех вариантов поровну. 0 п.п. — «каждый вариант жизнеспособен».
Код выхода: 0 — успех, 2 — ошибка ввода.
"""

import argparse
import csv
import io
import json
import math
import re
import sys

MIN_ITERATIONS = 1000


def read_text(path):
    try:
        with open(path, encoding="utf-8-sig", newline="") as stream:
            return stream.read()
    except (OSError, UnicodeDecodeError) as err:
        raise SystemExit(f"error: {path}: {err}")


def from_metrics(data, rate, row, col):
    metrics = data.get("metrics")
    if not isinstance(metrics, dict):
        raise SystemExit("error: metrics file has no 'metrics' object")
    pattern = re.compile(rf"^rate:{re.escape(rate)}@{re.escape(row)}=([^,]+),{re.escape(col)}=([^,]+)$")
    cells, low = {}, []
    for key, metric in metrics.items():
        match = pattern.match(key)
        if not match or not isinstance(metric, dict) or metric.get("value") is None:
            continue
        value = metric["value"]
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise SystemExit(f"error: {key}: value is not a number")
        cells[match.groups()] = value
        if metric.get("low_n"):
            low.append(f"{match.group(1)} vs {match.group(2)} (n={metric.get('n')})")
    if not cells:
        raise SystemExit(f"error: no keys like rate:{rate}@{row}=X,{col}=Y; run design_metrics.py with --by {row},{col}")
    return cells, low


def from_csv(text):
    first = text.splitlines()[0] if text else ""
    delimiter = ";" if first.count(";") > first.count(",") else ","
    table = [line for line in csv.reader(io.StringIO(text), delimiter=delimiter) if any(c.strip() for c in line)]
    if len(table) < 3:
        raise SystemExit("error: CSV needs a header row and at least two options")
    header = [h.strip() for h in table[0][1:]]
    cells = {}
    for line in table[1:]:
        name = line[0].strip()
        if len(line) - 1 > len(header):
            raise SystemExit(f"error: row {name!r} has more cells than the header")
        for opp, value in zip(header, line[1:]):
            if not value.strip():
                continue
            if (name, opp) in cells:
                raise SystemExit(f"error: duplicate matchup: {name} vs {opp}")
            try:
                cells[(name, opp)] = float(value.replace(",", ".") if delimiter == ";" else value)
            except ValueError:
                raise SystemExit(f"error: not a number: {name} vs {opp}: {value!r}")
    return cells, []


def build_matrix(cells):
    picks = sorted({a for a, _ in cells} | {b for _, b in cells})
    if len(picks) < 2:
        raise SystemExit("error: need at least two options in the matrix")
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
    return picks, [[(p[i][j] - p[j][i]) / 2 for j in range(n)] for i in range(n)]


def fictitious_play(payoff, iterations):
    """Средняя стратегия фиктивной игры; для антагонистических игр сходится к равновесию."""
    n = len(payoff)
    counts = [0] * n
    totals = [0.0] * n  # суммарный выигрыш каждой чистой стратегии против истории соперника
    choice = 0
    for _ in range(iterations):
        counts[choice] += 1
        for i in range(n):
            totals[i] += payoff[i][choice]
        choice = max(range(n), key=totals.__getitem__)
    return [c / iterations for c in counts]


def expected(payoff, row, mix):
    """Ожидаемый результат (победы + половина ничьих) варианта row против смеси mix."""
    return 0.5 + sum(a * m for a, m in zip(payoff[row], mix))


def dominated(payoff, eps):
    """Пары (i, k): k не хуже i против каждого соперника, включая очную встречу, и лучше хотя бы в одном."""
    n = len(payoff)
    result = []
    for i in range(n):
        for k in range(n):
            if k == i:
                continue
            gaps = [payoff[k][j] - payoff[i][j] for j in range(n) if j not in (i, k)] + [payoff[k][i]]
            if all(g >= -eps for g in gaps) and any(g > eps for g in gaps):
                result.append((i, k))
                break
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description="Nash equilibrium of a metagame from a matchup matrix.")
    parser.add_argument("data", help="design_metrics.py JSON or a square CSV matrix of win rates")
    parser.add_argument("--rate", default="win", help="rate field in the metrics file (default: win)")
    parser.add_argument("--row", default="pick", help="row grouping field (default: pick)")
    parser.add_argument("--col", default="opp_pick", help="column grouping field (default: opp_pick)")
    parser.add_argument("--iterations", type=int, default=200000,
                        help=f"fictitious play iterations (at least {MIN_ITERATIONS})")
    parser.add_argument("--eps", type=float, default=0.005,
                        help="tolerance in win-rate units: viable if vs eq >= 0.5 - eps (default 0.005)")
    parser.add_argument("--json", help="also write the result as JSON")
    args = parser.parse_args(argv)
    if args.iterations < MIN_ITERATIONS:
        parser.error(f"--iterations must be at least {MIN_ITERATIONS}")

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
    picks, payoff = build_matrix(cells)
    n = len(picks)
    mix = fictitious_play(payoff, args.iterations)
    vs_field = [expected(payoff, i, [1 / n] * n) for i in range(n)]
    vs_eq = [expected(payoff, i, mix) for i in range(n)]
    viable = [v >= 0.5 - args.eps for v in vs_eq]
    accuracy = max(vs_eq) - 0.5
    exploit_uniform = max(vs_field) - 0.5
    pairs = dominated(payoff, args.eps)

    width = max(len(d) for d in picks + ["Pick"])
    print(f"{'Pick':<{width}} {'share':>7} {'vs field':>9} {'vs eq':>7}  status")
    for i in sorted(range(n), key=lambda i: (-mix[i], -vs_eq[i])):
        print(f"{picks[i]:<{width}} {mix[i]:>7.1%} {vs_field[i]:>9.1%} {vs_eq[i]:>7.1%}  "
              f"{'viable' if viable[i] else 'beaten'}")
    print(f"\nViable picks: {sum(viable)} of {n}")
    if sum(viable) > sum(1 for s in mix if s > 0.01):
        print("Equilibrium is not unique: viable picks with ~0% share are equally good against this meta.")
    print(f"Uniform meta exploitability: {exploit_uniform * 100:+.1f} p.p. "
          f"(best pick vs an even field: {picks[vs_field.index(max(vs_field))]})")
    print(f"Equilibrium accuracy: best response gains {accuracy * 100:.2f} p.p. (0 = exact)")
    if pairs:
        print("Weakly dominated (another pick is no worse against every opponent and better against one):")
        for i, k in pairs:
            print(f"  {picks[i]} <= {picks[k]}")
    if low:
        print("Low-n matchups (treat with care): " + ", ".join(low[:10]))
    if args.json:
        result = {"picks": picks, "share": dict(zip(picks, mix)), "vs_field": dict(zip(picks, vs_field)),
                  "vs_equilibrium": dict(zip(picks, vs_eq)), "viable": dict(zip(picks, viable)),
                  "uniform_exploitability": exploit_uniform, "equilibrium_accuracy": accuracy,
                  "weakly_dominated": [[picks[i], picks[k]] for i, k in pairs]}
        try:
            with open(args.json, "w", encoding="utf-8") as stream:
                json.dump(result, stream, ensure_ascii=False, indent=1)
        except OSError as err:
            raise SystemExit(f"error: {args.json}: {err}")
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
