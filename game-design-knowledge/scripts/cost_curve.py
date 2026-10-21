#!/usr/bin/env python3
"""Кривая стоимости: линейная регрессия «стоимость ← характеристики» и карты вне кривой.

Запуск:
  python3 cost_curve.py data/cards.csv --cost cost --name name --features attack,health,taunt,charge
  python3 cost_curve.py data/cards.json --cost mana --exclude rarity --threshold 0.75 --json curve.json

Вход: CSV с заголовком или JSON-массив объектов. Одна строка — одна карта, юнит или предмет.
Признаки — числовые столбцы; ключевые слова кодируются 0/1 (true/false тоже понимаются),
пустая ячейка признака считается нулём.
Без --features берутся все числовые столбцы, кроме --cost, --name и --exclude.

Что печатает:
  - цену каждой характеристики в единицах стоимости (коэффициенты регрессии, как «1 атака ≈ 0.5 маны»);
  - R² — насколько кривая объясняет стоимость (низкий R² значит, что в цене есть неучтённые эффекты);
  - карты вне кривой: residual = прогноз − фактическая стоимость.
    > +threshold — карта даёт больше, чем стоит (кандидат на нерф или «надкривая» намеренно);
    < −threshold — карта переплачивает (кандидат на баф или скрытая ценность не в признаках).
Это метод «кривой стоимости» Schreiber (Game Balance Concepts, Level 3) в автоматическом виде:
кривая ищет выбросы, а не назначает цены. Код выхода: 0 — успех, 2 — ошибка ввода.
"""

import argparse
import csv
import io
import json
import math
import sys

TRUE_WORDS = {"true", "yes", "y"}
FALSE_WORDS = {"false", "no", "n", ""}


def to_number(value):
    if isinstance(value, bool):
        return float(value)
    if isinstance(value, (int, float)):
        return float(value) if math.isfinite(value) else None
    text = str(value).strip().lower()
    if text in TRUE_WORDS:
        return 1.0
    if text in FALSE_WORDS:
        return 0.0 if text else None
    try:
        number = float(text.replace(",", "."))
    except ValueError:
        return None
    return number if math.isfinite(number) else None


def read_rows(path):
    try:
        with open(path, encoding="utf-8-sig", newline="") as stream:
            text = stream.read()
    except (OSError, UnicodeDecodeError) as err:
        raise SystemExit(f"error: {path}: {err}")
    if path.lower().endswith(".json"):
        try:
            rows = json.loads(text)
        except ValueError as err:
            raise SystemExit(f"error: {path}: {err}")
        if not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
            raise SystemExit(f"error: {path}: expected a JSON array of objects")
        return rows
    return list(csv.DictReader(io.StringIO(text)))


def solve(matrix, vector):
    """Гаусс с выбором главного элемента; None, если система вырождена."""
    n = len(vector)
    a = [row[:] + [vector[i]] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(a[r][col]))
        if abs(a[pivot][col]) < 1e-12:
            return None
        a[col], a[pivot] = a[pivot], a[col]
        for r in range(n):
            if r != col:
                factor = a[r][col] / a[col][col]
                a[r] = [x - factor * y for x, y in zip(a[r], a[col])]
    return [a[i][n] / a[i][i] for i in range(n)]


def fit(xs, ys):
    """Наименьшие квадраты с интерсептом: нормальные уравнения (XᵀX)b = Xᵀy."""
    design = [[1.0] + row for row in xs]
    k = len(design[0])
    xtx = [[sum(r[i] * r[j] for r in design) for j in range(k)] for i in range(k)]
    xty = [sum(r[i] * y for r, y in zip(design, ys)) for i in range(k)]
    return solve(xtx, xty)


def pick_features(rows, cost, name, exclude):
    columns = [c for c in rows[0] if c not in {cost, name} | exclude]
    return [c for c in columns if any(to_number(r.get(c)) is not None for r in rows)
            and all(to_number(r.get(c)) is not None or r.get(c) in (None, "") for r in rows)]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Fit a cost curve and list cards off the curve.")
    parser.add_argument("data", help="CSV with a header row or a JSON array of objects")
    parser.add_argument("--cost", default="cost", help="cost column (default: cost)")
    parser.add_argument("--name", default="name", help="name column (default: name)")
    parser.add_argument("--features", help="comma-separated feature columns (default: all numeric)")
    parser.add_argument("--exclude", default="", help="comma-separated columns to ignore")
    parser.add_argument("--threshold", type=float, default=0.75,
                        help="report cards whose |residual| exceeds this many cost units (default 0.75)")
    parser.add_argument("--json", help="also write coefficients and residuals as JSON")
    args = parser.parse_args(argv)

    rows = read_rows(args.data)
    if not rows:
        raise SystemExit(f"error: {args.data}: no rows")
    exclude = {c.strip() for c in args.exclude.split(",") if c.strip()}
    if args.features:
        features = [c.strip() for c in args.features.split(",") if c.strip()]
        missing = [c for c in features if c not in rows[0]]
        if missing:
            raise SystemExit(f"error: unknown feature columns: {', '.join(missing)}")
    else:
        features = pick_features(rows, args.cost, args.name, exclude)
    if not features:
        raise SystemExit("error: no numeric feature columns found; pass --features")

    names, xs, ys, skipped = [], [], [], 0
    for i, row in enumerate(rows, 1):
        y = to_number(row.get(args.cost))
        # пустая ячейка признака = «нет ключевого слова» (0); пустая стоимость — строка пропускается
        x = [0.0 if row.get(c) in (None, "") else to_number(row.get(c)) for c in features]
        if y is None or any(v is None for v in x):
            skipped += 1
            continue
        names.append(str(row.get(args.name, f"row {i}")))
        xs.append(x)
        ys.append(y)
    if len(ys) <= len(features) + 1:
        raise SystemExit(f"error: need more than {len(features) + 1} complete rows, got {len(ys)}")

    coef = fit(xs, ys)
    if coef is None:
        raise SystemExit("error: features are collinear (one is a combination of others); drop one with --exclude")
    # второй проход: выбросы искажают кривую, поэтому она пересчитывается без них,
    # а затем по ней заново оцениваются все карты
    first = [coef[0] + sum(b * v for b, v in zip(coef[1:], x)) - y for x, y in zip(xs, ys)]
    inliers = [i for i, r in enumerate(first) if abs(r) <= args.threshold]
    refit = None
    if len(inliers) < len(ys) and len(inliers) > len(features) + 1:
        refit = fit([xs[i] for i in inliers], [ys[i] for i in inliers])
    if refit is not None:
        coef = refit
    predicted = [coef[0] + sum(b * v for b, v in zip(coef[1:], x)) for x in xs]
    residuals = [p - y for p, y in zip(predicted, ys)]
    fit_rows = inliers if refit is not None else range(len(ys))
    fit_y = [ys[i] for i in fit_rows]
    mean_y = sum(fit_y) / len(fit_y)
    ss_tot = sum((y - mean_y) ** 2 for y in fit_y)
    ss_res = sum(residuals[i] ** 2 for i in fit_rows)
    r2 = 1 - ss_res / ss_tot if ss_tot else 1.0
    rmse = math.sqrt(ss_res / len(fit_y))

    print(f"Cost curve: {args.cost} ~ {' + '.join(features)}  (n={len(ys)}, skipped {skipped})")
    if refit is not None:
        print(f"Refit without {len(ys) - len(inliers)} first-pass outliers")
    print(f"R^2 = {r2:.3f}, RMSE = {rmse:.2f} cost units (on the rows the curve was fitted to)")
    print(f"{'intercept':<24} {coef[0]:+.3f}")
    for feature, value in zip(features, coef[1:]):
        print(f"{feature:<24} {value:+.3f} per unit")
    off = sorted(((r, n, y, p) for r, n, y, p in zip(residuals, names, ys, predicted)
                  if abs(r) > args.threshold), reverse=True)
    print(f"\nOff the curve (|predicted - actual| > {args.threshold}):")
    if not off:
        print("  none")
    for r, name, y, p in off:
        verdict = "gives more than it costs" if r > 0 else "overpays"
        print(f"  {name:<28} actual {y:g}, curve {p:.2f}, {r:+.2f}  {verdict}")
    if args.json:
        with open(args.json, "w", encoding="utf-8") as stream:
            json.dump({"features": features, "intercept": coef[0], "coefficients": dict(zip(features, coef[1:])),
                       "r2": r2, "rmse": rmse,
                       "cards": [{"name": n, "actual": y, "predicted": p, "residual": r}
                                 for n, y, p, r in zip(names, ys, predicted, residuals)]},
                      stream, ensure_ascii=False, indent=1)
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
