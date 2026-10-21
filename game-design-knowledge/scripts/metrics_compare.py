#!/usr/bin/env python3
"""Сравнивает два файла design_metrics.py: базовую линию и повторный замер.

Запуск:
  python3 metrics_compare.py metrics/before.json metrics/after.json --targets design/targets.json
  python3 metrics_compare.py before.json after.json --only "rate:win@pick=*" --holm --json diff.json

Файл целей (targets.json) задаёт для метрик коридор и/или желаемое направление.
Ключ — шаблон имени метрики (fnmatch), побеждает первый подходящий:
  {
    "rate:win@went_first=true": {"min": 0.47, "max": 0.53},
    "rate:win@pick=*":       {"min": 0.45, "max": 0.55},
    "spread:win@pick":       {"max": 0.10},
    "rate:completed@level=*": {"min": 0.60},
    "num:turns":             {"min": 7, "max": 12, "stat": "median"},
    "num:attempts@level=*":  [{"max": 8, "stat": "median"}, {"max": 25, "stat": "p90"}],
    "rate:finished_tutorial": {"better": "higher"}
  }
Список коридоров у одного шаблона проверяет несколько статистик одной числовой метрики:
каждая даёт свою строку с пометкой [stat] (у долей — [#1], [#2]). Поправка Холма считает
такую метрику одним тестом.

Значимость: доли — z-тест двух пропорций, числа — U-тест Манна — Уитни по сохранённым значениям
(для любого "stat": он сравнивает распределения целиком, а коридор проверяется по выбранной статистике).
spread не тестируется: это производная метрика, её вердикт идёт только по коридору.
Вердикты:
  better / worse — изменение значимо и метрика приблизилась к коридору (отдалилась от него)
                   или сдвинулась в сторону "better" (в обратную сторону);
  shifted        — значимое изменение внутри коридора: не хуже, но стоит посмотреть;
  changed        — значимое изменение у метрики без цели;
  untested       — spread без коридора изменился, но значимость не проверяется
                   (для spread "better" не используется: без коридора он только справочный);
  same           — изменение в пределах шума.
Колонка Band показывает положение относительно коридора до и после: in/out.
Код выхода: 0 — ухудшений нет, 1 — есть хотя бы одно worse, 2 — ошибка ввода.
"""

import argparse
import fnmatch
import io
import json
import math
import sys

IGNORED_META = {"label", "commit", "date", "note"}


STATS = {"mean", "median", "q1", "q3", "p10", "p90", "min", "max"}


def read_json(path):
    """UTF-8 с BOM или без; UTF-16 и битый JSON — ошибка ввода (код 2), а не трейсбэк."""
    try:
        with open(path, encoding="utf-8-sig") as stream:
            return json.load(stream)
    except (OSError, ValueError) as err:
        raise SystemExit(f"error: {path}: {err}")


def load(path):
    data = read_json(path)
    if (not isinstance(data, dict) or data.get("tool") != "design_metrics"
            or not isinstance(data.get("metrics"), dict)):
        raise SystemExit(f"error: {path}: not a design_metrics.py output")
    return data


def load_targets(path):
    targets = read_json(path)
    if not isinstance(targets, dict):
        raise SystemExit(f"error: {path}: expected an object of pattern -> target")
    for pattern, value in targets.items():
        items = value if isinstance(value, list) and value else [value]
        for target in items:
            if not isinstance(target, dict) or not ({"min", "max", "better"} & set(target)):
                raise SystemExit(f"error: {path}: {pattern}: expected an object (or a list of objects) "
                                 "with min, max or better")
            if target.get("better") not in (None, "higher", "lower"):
                raise SystemExit(f"error: {path}: {pattern}: better must be 'higher' or 'lower'")
            if target.get("stat", "median") not in STATS:
                raise SystemExit(f"error: {path}: {pattern}: stat must be one of {', '.join(sorted(STATS))}")
            for bound in ("min", "max"):
                value_ = target.get(bound)
                if bound in target and (isinstance(value_, bool) or not isinstance(value_, (int, float))):
                    raise SystemExit(f"error: {path}: {pattern}: {bound} must be a number")
        stats = [t.get("stat", "median") for t in items if isinstance(t, dict)]
        if len(stats) != len(set(stats)):
            raise SystemExit(f"error: {path}: {pattern}: each corridor in a list needs its own stat")
    return targets


def normal_p(z):
    """Двусторонний p-value для стандартного нормального распределения."""
    return math.erfc(abs(z) / math.sqrt(2))


def two_proportion_p(a, b):
    n1, n2 = a["n"], b["n"]
    if n1 == 0 or n2 == 0:
        return None
    pooled = (a["k"] + b["k"]) / (n1 + n2)
    se = math.sqrt(pooled * (1 - pooled) * (1 / n1 + 1 / n2))
    if se == 0:
        return 1.0
    return normal_p((b["k"] / n2 - a["k"] / n1) / se)


def mann_whitney_p(xs, ys):
    """U-тест с поправкой на совпадения и на непрерывность (нормальное приближение)."""
    n1, n2 = len(xs), len(ys)
    if n1 == 0 or n2 == 0:
        return None
    combined = sorted([(v, 0) for v in xs] + [(v, 1) for v in ys])
    rank_sum_x = 0.0
    tie_term = 0.0
    i = 0
    while i < len(combined):
        j = i
        while j + 1 < len(combined) and combined[j + 1][0] == combined[i][0]:
            j += 1
        avg_rank = (i + j) / 2 + 1
        size = j - i + 1
        tie_term += size ** 3 - size
        rank_sum_x += avg_rank * sum(1 for _, side in combined[i:j + 1] if side == 0)
        i = j + 1
    u = rank_sum_x - n1 * (n1 + 1) / 2
    mean_u = n1 * n2 / 2
    n = n1 + n2
    var_u = n1 * n2 / 12 * ((n + 1) - tie_term / (n * (n - 1))) if n > 1 else 0
    if var_u <= 0:
        return 1.0
    z = (abs(u - mean_u) - 0.5) / math.sqrt(var_u)
    return normal_p(max(z, 0.0))


def find_targets(key, targets):
    """Коридоры первого подходящего шаблона: список (один или несколько) или [None]."""
    for pattern, target in targets.items():
        if fnmatch.fnmatchcase(key, pattern):
            return target if isinstance(target, list) else [target]
    return [None]


def stat_value(metric, target):
    if metric["kind"] == "num":
        return metric.get((target or {}).get("stat", "median"))
    return metric.get("value")


def band_distance(value, target):
    if "min" in target and value < target["min"]:
        return target["min"] - value
    if "max" in target and value > target["max"]:
        return value - target["max"]
    return 0.0


def p_value(before, after):
    if before["kind"] == "rate":
        return two_proportion_p(before, after)
    if before["kind"] == "num":
        return mann_whitney_p(before.get("values", []), after.get("values", []))
    return None


def holm_adjust(rows):
    """Поправка Холма — Бонферрони: один тест на метрику, даже если у неё несколько коридоров."""
    tests = sorted({(r["metric"], r["p"]) for r in rows if r["p"] is not None}, key=lambda t: t[1])
    adjusted, running = {}, 0.0
    for i, (metric, p) in enumerate(tests):
        running = max(running, min(1.0, (len(tests) - i) * p))
        adjusted[metric] = running
    for row in rows:
        row["p_adj"] = adjusted.get(row["metric"], row["p"])


def verdict(row, alpha, min_change):
    """Поправленный p нужен, чтобы не объявить ложное улучшение. Ухудшение проверяется
    по исходному p: пропустить регрессию дороже, чем лишний раз её перепроверить."""
    raw = direction(row, min_change)
    # spread — производная метрика без теста значимости: решает только коридор
    if row["kind"] == "spread" or raw in ("same", "untested"):
        return raw
    p = row["p"] if raw == "worse" else row["p_adj"]
    return raw if p is not None and p < alpha else "same"


def direction(row, min_change):
    target = row["target"] or {}
    before, after = row["before"], row["after"]
    if before is None or after is None or before == after or abs(after - before) < min_change:
        return "same"
    has_band = "min" in target or "max" in target
    if has_band:
        d_before, d_after = band_distance(before, target), band_distance(after, target)
        if d_after < d_before:
            return "better"
        if d_after > d_before:
            return "worse"
    if row["kind"] == "spread":
        return "same" if has_band else "untested"
    if target.get("better") in ("higher", "lower"):
        return "better" if (after > before) == (target["better"] == "higher") else "worse"
    return "shifted" if has_band else "changed"


def compare(before, after, targets, alpha, min_change, only, holm):
    rows = []
    b_metrics, a_metrics = before["metrics"], after["metrics"]
    for key in sorted(set(b_metrics) | set(a_metrics)):
        if only and not any(fnmatch.fnmatchcase(key, pattern) for pattern in only):
            continue
        if key not in b_metrics or key not in a_metrics:
            rows.append({"key": key, "missing": "before" if key not in b_metrics else "after"})
            continue
        b, a = b_metrics[key], a_metrics[key]
        found = find_targets(key, targets)
        p = p_value(b, a)
        for number, target in enumerate(found, 1):
            label = key
            if len(found) > 1:
                label += f" [{(target or {}).get('stat', 'median')}]" if b["kind"] == "num" else f" [#{number}]"
            rows.append({
                "key": label,
                "metric": key,
                "kind": b["kind"],
                "target": target,
                "before": stat_value(b, target),
                "after": stat_value(a, target),
                "p": p,
                "low_n": b.get("low_n", False) or a.get("low_n", False),
            })
    present = [r for r in rows if "missing" not in r]
    for row in present:
        row["p_adj"] = row["p"]
    if holm:
        holm_adjust(present)
    for row in present:
        row["band"] = band_label(row)
        row["verdict"] = verdict(row, alpha, min_change)
    return rows


def band_label(row):
    target = row["target"]
    if not target or ("min" not in target and "max" not in target):
        return ""
    labels = []
    for value in (row["before"], row["after"]):
        labels.append("?" if value is None else "in" if band_distance(value, target) == 0 else "out")
    return "->".join(labels)


def fmt(value, kind):
    if value is None:
        return "-"
    if kind in ("rate", "spread"):
        return f"{value * 100:.1f}%"
    return f"{value:.4g}"


def print_table(rows, holm):
    width = max([len(r["key"]) for r in rows] + [6])
    p_columns = ["p", "p_adj"] if holm else ["p"]
    header = " ".join(f"{name:>7}" for name in p_columns)
    print(f"{'Metric':<{width}} {'Before':>9} {'After':>9} {header} {'Band':>7}  Verdict")
    for row in rows:
        if "missing" in row:
            blank = " ".join(f"{'':>7}" for _ in p_columns)
            print(f"{row['key']:<{width}} {'':>9} {'':>9} {blank} {'':>7}  missing in {row['missing']}")
            continue
        ps = " ".join(f"{'-' if row[c] is None else format(row[c], '.3f'):>7}" for c in p_columns)
        note = " (low n)" if row["low_n"] else ""
        print(f"{row['key']:<{width}} {fmt(row['before'], row['kind']):>9} "
              f"{fmt(row['after'], row['kind']):>9} {ps} {row['band']:>7}  {row['verdict']}{note}")


def warn_meta(before, after):
    b_meta, a_meta = before.get("meta", {}), after.get("meta", {})
    for key in sorted((set(b_meta) | set(a_meta)) - IGNORED_META):
        b, a = b_meta.get(key), a_meta.get(key)
        if b != a:
            print(f"WARNING: run conditions differ: {key}: {b!r} -> {a!r}")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Compare two design_metrics.py outputs.")
    parser.add_argument("before")
    parser.add_argument("after")
    parser.add_argument("--targets", help="JSON with target bands and directions per metric pattern")
    parser.add_argument("--alpha", type=float, default=0.05, help="significance level (default 0.05)")
    parser.add_argument("--min-change", type=float, default=0.0,
                        help="ignore changes smaller than this in absolute units (0.02 = 2 p.p. for rates)")
    parser.add_argument("--only", action="append", default=[], help="compare only metrics matching PATTERN")
    parser.add_argument("--holm", action="store_true",
                        help="Holm-Bonferroni correction for 'better' verdicts; 'worse' keeps the raw p")
    parser.add_argument("--json", help="also write the comparison as JSON")
    args = parser.parse_args(argv)

    before, after = load(args.before), load(args.after)
    targets = load_targets(args.targets) if args.targets else {}

    warn_meta(before, after)
    rows = compare(before, after, targets, args.alpha, args.min_change, args.only, args.holm)
    if not rows:
        raise SystemExit("error: no metrics to compare")
    print_table(rows, args.holm)
    counts = {}
    for row in rows:
        counts[row.get("verdict", "missing")] = counts.get(row.get("verdict", "missing"), 0) + 1
    print("\nSummary: " + ", ".join(f"{name} {count}" for name, count in sorted(counts.items())))
    out_of_band = [r["key"] for r in rows if r.get("band", "").endswith("out")]
    if out_of_band:
        print("Still out of band: " + ", ".join(out_of_band))
    if args.json:
        try:
            with open(args.json, "w", encoding="utf-8") as stream:
                json.dump(rows, stream, ensure_ascii=False, indent=1)
        except OSError as err:
            raise SystemExit(f"error: {args.json}: {err}")
    return 1 if counts.get("worse") else 0


if __name__ == "__main__":
    # Имена групп могут быть любыми: в консоли cp1251 непечатное экранируется, а не роняет скрипт
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
