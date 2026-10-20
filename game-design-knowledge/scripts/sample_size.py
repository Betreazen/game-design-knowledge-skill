#!/usr/bin/env python3
"""Сколько партий симуляции или сессий плейтеста нужно для нужной точности доли.

Запуск:
  python3 sample_size.py margin 0.02            # n, чтобы 95% интервал доли был ±2 п.п. (худший случай p=0.5)
  python3 sample_size.py margin 0.02 --p 0.3    # то же при ожидаемой доле 30%
  python3 sample_size.py vs 0.50 0.53           # n, чтобы отличить долю 53% от фиксированных 50%
  python3 sample_size.py diff 0.50 0.53         # n в КАЖДОЙ из двух групп (до/после правки, колода A/B)

Опции: --conf (доверие для margin, 0.95), --alpha (0.05), --power (0.8).
Формулы — нормальное приближение для долей; для долей ближе 5% к 0 или 1 и малых n оно занижает n.
"""

import argparse
import math
from statistics import NormalDist

STD = NormalDist()


def n_margin(margin, p, conf):
    z = STD.inv_cdf(1 - (1 - conf) / 2)
    return math.ceil(z * z * p * (1 - p) / (margin * margin))


def n_vs(p0, p1, alpha, power):
    z_a, z_b = STD.inv_cdf(1 - alpha / 2), STD.inv_cdf(power)
    top = z_a * math.sqrt(p0 * (1 - p0)) + z_b * math.sqrt(p1 * (1 - p1))
    return math.ceil((top / (p1 - p0)) ** 2)


def n_diff(p1, p2, alpha, power):
    z_a, z_b = STD.inv_cdf(1 - alpha / 2), STD.inv_cdf(power)
    p_bar = (p1 + p2) / 2
    top = z_a * math.sqrt(2 * p_bar * (1 - p_bar)) + z_b * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return math.ceil((top / (p2 - p1)) ** 2)


def proportion(text):
    value = float(text)
    if not 0 < value < 1:
        raise argparse.ArgumentTypeError(f"expected a proportion between 0 and 1, got {text}")
    return value


def main(argv=None):
    parser = argparse.ArgumentParser(description="Sample size for rates in simulations and playtests.")
    sub = parser.add_subparsers(dest="mode", required=True)
    margin = sub.add_parser("margin", help="n for a confidence interval of +/- MARGIN")
    margin.add_argument("margin", type=proportion)
    margin.add_argument("--p", type=proportion, default=0.5, help="expected rate (0.5 = worst case)")
    margin.add_argument("--conf", type=proportion, default=0.95)
    for name, text in (("vs", "n to tell rate P1 from a fixed P0"), ("diff", "n per group to tell P1 from P2")):
        mode = sub.add_parser(name, help=text)
        mode.add_argument("p_a", type=proportion)
        mode.add_argument("p_b", type=proportion)
        mode.add_argument("--alpha", type=proportion, default=0.05)
        mode.add_argument("--power", type=proportion, default=0.8)
    args = parser.parse_args(argv)

    if args.mode == "margin":
        n = n_margin(args.margin, args.p, args.conf)
        print(f"n = {n}  (rate {args.p:.0%} +/- {args.margin * 100:g} p.p. at {args.conf:.0%} confidence)")
        return 0
    if args.p_a == args.p_b:
        parser.error("the two rates must differ")
    if args.mode == "vs":
        n = n_vs(args.p_a, args.p_b, args.alpha, args.power)
        print(f"n = {n}  (detect {args.p_b:.1%} vs fixed {args.p_a:.1%}, alpha {args.alpha}, power {args.power:.0%})")
    else:
        n = n_diff(args.p_a, args.p_b, args.alpha, args.power)
        print(f"n = {n} per group, {2 * n} total  "
              f"(detect {args.p_a:.1%} vs {args.p_b:.1%}, alpha {args.alpha}, power {args.power:.0%})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
