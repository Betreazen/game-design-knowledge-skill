#!/usr/bin/env python3
"""Сводит логи симуляций или плейтестов (JSONL) в метрики дизайна.

Запуск:
  python3 design_metrics.py runs.jsonl --rate win --num turns --by deck --by deck,opp_deck \
      --meta sim=v3 --meta seeds=1-5000 --out metrics/before.json

Вход: одна строка JSONL = одна партия, забег или сессия. Поля проект выбирает сам.
  --rate ПОЛЕ  доля: значения true/false или 1/0 (например, win, first_player_won, finished_tutorial)
  --num ПОЛЕ   число: медиана, квартили, p10/p90 (например, turns, duration_s, gold_at_day_7)
  --by ПОЛЯ    разрез по одному полю или паре через запятую (deck; deck,opp_deck — матрица матчапов)
  --meta K=V   условия прогона: версия симулятора, боты, seed-диапазон. metrics_compare.py
               предупредит, если они различаются между базовой линией и повторным замером.
  --min-n N    группы меньше N помечаются low_n (по умолчанию 30)

Выход — JSON для metrics_compare.py. Ключи метрик:
  rate:win, rate:win@deck=Aggro, num:turns@deck=Aggro,opp_deck=Control,
  spread:win@deck — разница между лучшей и худшей группой по доле.
Доли идут с 95% доверительным интервалом Уилсона. Код выхода: 0 — успех, 2 — ошибка ввода.
"""

import argparse
import io
import json
import math
import sys

Z95 = 1.959964


def wilson(k, n, z=Z95):
    if n == 0:
        return [0.0, 1.0]
    p = k / n
    denom = 1 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return [max(0.0, center - half), min(1.0, center + half)]


def percentile(sorted_values, q):
    """Линейная интерполяция, как numpy.percentile по умолчанию."""
    if not sorted_values:
        return None
    pos = (len(sorted_values) - 1) * q
    lo = math.floor(pos)
    hi = math.ceil(pos)
    return sorted_values[lo] + (sorted_values[hi] - sorted_values[lo]) * (pos - lo)


def as_rate(value):
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, (int, float)) and value in (0, 1):
        return int(value)
    return None


def as_num(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return value if math.isfinite(value) else None


def read_records(path):
    """Читает UTF-8 (с BOM или без). UTF-16 от `>` в Windows PowerShell 5 — ошибка ввода."""
    records = []
    if path == "-":
        stream = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8-sig")
    else:
        stream = open(path, encoding="utf-8-sig")
    with stream:
        try:
            lines = list(stream)
        except UnicodeDecodeError as err:
            raise SystemExit(f"error: {path}: not UTF-8 ({err.reason}); re-save the file as UTF-8")
    for line_no, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as err:
            raise SystemExit(f"error: {path}:{line_no}: invalid JSON: {err}")
        if not isinstance(record, dict):
            raise SystemExit(f"error: {path}:{line_no}: expected a JSON object")
        records.append(record)
    return records


def group_key(record, fields):
    parts = []
    for field in fields:
        if field not in record:
            return None
        value = record[field]
        parts.append(f"{field}={value if isinstance(value, str) else json.dumps(value)}")
    return ",".join(parts)


def rate_metric(values, min_n):
    n = len(values)
    k = sum(values)
    return {
        "kind": "rate",
        "n": n,
        "k": k,
        "value": k / n if n else None,
        "ci95": wilson(k, n),
        "low_n": n < min_n,
    }


def num_metric(values, min_n):
    values = sorted(values)
    n = len(values)
    return {
        "kind": "num",
        "n": n,
        "mean": sum(values) / n if n else None,
        "median": percentile(values, 0.5),
        "q1": percentile(values, 0.25),
        "q3": percentile(values, 0.75),
        "p10": percentile(values, 0.10),
        "p90": percentile(values, 0.90),
        "min": values[0] if values else None,
        "max": values[-1] if values else None,
        "low_n": n < min_n,
        "values": values,
    }


def collect(records, field, convert, groupings):
    """Возвращает все значения поля и {индекс разреза: {ключ группы: [значения]}}."""
    overall = []
    grouped = {i: {} for i in range(len(groupings))}
    for record in records:
        value = convert(record.get(field))
        if value is None:
            continue
        overall.append(value)
        for i, fields in enumerate(groupings):
            key = group_key(record, fields)
            if key is not None:
                grouped[i].setdefault(key, []).append(value)
    return overall, grouped


def spread_metric(groups, min_n):
    """Разница долей между лучшей и худшей группой; группы с low_n не учитываются."""
    rates = {key: rate_metric(values, min_n) for key, values in groups.items()}
    rates = {key: m for key, m in rates.items() if not m["low_n"]}
    if len(rates) < 2:
        return None
    best = max(rates, key=lambda key: rates[key]["value"])
    worst = min(rates, key=lambda key: rates[key]["value"])
    return {
        "kind": "spread",
        "value": rates[best]["value"] - rates[worst]["value"],
        "max_group": best,
        "min_group": worst,
        "groups": len(rates),
    }


def build_metrics(records, rates, nums, groupings, min_n):
    metrics = {}
    for field in rates:
        overall, grouped = collect(records, field, as_rate, groupings)
        metrics[f"rate:{field}"] = rate_metric(overall, min_n)
        for i, fields in enumerate(groupings):
            for key, values in sorted(grouped[i].items()):
                metrics[f"rate:{field}@{key}"] = rate_metric(values, min_n)
            spread = spread_metric(grouped[i], min_n)
            if spread:
                metrics[f"spread:{field}@{','.join(fields)}"] = spread
    for field in nums:
        overall, grouped = collect(records, field, as_num, groupings)
        metrics[f"num:{field}"] = num_metric(overall, min_n)
        for i in range(len(groupings)):
            for key, values in sorted(grouped[i].items()):
                metrics[f"num:{field}@{key}"] = num_metric(values, min_n)
    return metrics


def parse_meta(items):
    meta = {}
    for item in items:
        key, sep, value = item.partition("=")
        if not sep or not key:
            raise SystemExit(f"error: --meta expects KEY=VALUE, got {item!r}")
        meta[key] = value
    return meta


def main(argv=None):
    parser = argparse.ArgumentParser(description="Aggregate JSONL game runs into design metrics.")
    parser.add_argument("runs", help="JSONL file, one match/run/session per line; '-' for stdin")
    parser.add_argument("--rate", action="append", default=[], help="boolean field to report as a rate")
    parser.add_argument("--num", action="append", default=[], help="numeric field to summarize")
    parser.add_argument("--by", action="append", default=[], help="group by FIELD or FIELD,FIELD")
    parser.add_argument("--meta", action="append", default=[], help="run conditions as KEY=VALUE")
    parser.add_argument("--min-n", type=int, default=30, help="flag groups smaller than this")
    parser.add_argument("--out", help="write JSON here instead of stdout")
    args = parser.parse_args(argv)
    if not args.rate and not args.num:
        parser.error("pass at least one --rate or --num field")

    groupings = [[f.strip() for f in spec.split(",") if f.strip()] for spec in args.by]
    if not all(groupings):
        parser.error("--by expects FIELD or FIELD,FIELD")
    records = read_records(args.runs)
    if not records:
        raise SystemExit(f"error: {args.runs}: no records")
    result = {
        "tool": "design_metrics",
        "format": 1,
        "source": args.runs,
        "records": len(records),
        "meta": parse_meta(args.meta),
        "metrics": build_metrics(records, args.rate, args.num, groupings, args.min_n),
    }
    if args.out:
        with open(args.out, "w", encoding="utf-8") as out:
            out.write(json.dumps(result, ensure_ascii=False, indent=1) + "\n")
    else:
        # ASCII-экранирование: вывод в консоль Windows (cp1251) не падает на любых именах групп
        print(json.dumps(result, indent=1))
    for key, metric in result["metrics"].items():
        if metric["kind"] in ("rate", "num") and metric["n"] == 0:
            print(f"warning: {key}: no values (field missing or wrong type)", file=sys.stderr)


if __name__ == "__main__":
    if isinstance(sys.stderr, io.TextIOWrapper):
        sys.stderr.reconfigure(errors="backslashreplace")
    try:
        main()
    except OSError as err:
        print(f"error: {err}", file=sys.stderr)
        sys.exit(2)
    except SystemExit as exit_:
        if isinstance(exit_.code, str):
            print(exit_.code, file=sys.stderr)
            sys.exit(2)
        raise
