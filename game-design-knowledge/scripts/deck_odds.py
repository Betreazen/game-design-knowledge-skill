#!/usr/bin/env python3
"""Вероятности колоды по гипергеометрическому распределению: увидеть нужную карту или ресурс вовремя.

Запуск:
  python3 deck_odds.py at-least --deck 40 --copies 17 --need 3 --turn 3            # на play
  python3 deck_odds.py at-least --deck 40 --copies 17 --need 3 --turn 3 --draw     # на draw
  python3 deck_odds.py at-least --deck 30 --copies 2 --need 1 --seen 7             # явно: 7 карт
  python3 deck_odds.py by-turn --deck 40 --copies 2                                # таблица по ходам 1..10
  python3 deck_odds.py min-copies --deck 40 --need 1 --turn 3 --target 0.90        # сколько копий нужно
  python3 deck_odds.py hand --deck 40 --copies 17 --from 2 --to 5                  # стартовая рука с 2..5

Сколько карт увидено к ходу T: --hand (по умолчанию 7) + (T - 1) на play, ещё +1 на draw;
--draws-per-turn меняет добор. Муллиганы и поиск по колоде не учитываются.
Правило Karsten «89 + M %» — условное (считает только партии, где ресурсов хватило) и с муллиганом,
поэтому безусловные числа отсюда ниже его порогов. Таблица Karsten — в references/systems-balance.md.
"""

import argparse
from math import comb


def p_at_least(deck, copies, seen, need):
    """P(X >= need), X ~ Hypergeometric(deck, copies, seen)."""
    seen = min(seen, deck)
    total = comb(deck, seen)
    hits = sum(comb(copies, i) * comb(deck - copies, seen - i)
               for i in range(need, min(copies, seen) + 1))
    return hits / total


def p_between(deck, copies, seen, low, high):
    return p_at_least(deck, copies, seen, low) - p_at_least(deck, copies, seen, high + 1)


def cards_seen(turn, hand, on_draw, draws_per_turn):
    return hand + (turn - 1) * draws_per_turn + (draws_per_turn if on_draw else 0)


def positive(text):
    value = int(text)
    if value < 1:
        raise argparse.ArgumentTypeError(f"expected a positive integer, got {text}")
    return value


def non_negative(text):
    value = int(text)
    if value < 0:
        raise argparse.ArgumentTypeError(f"expected a non-negative integer, got {text}")
    return value


def add_seen_options(parser):
    parser.add_argument("--turn", type=positive, help="turn number (cards seen derived from hand and draws)")
    parser.add_argument("--seen", type=non_negative, help="cards seen, overrides --turn")
    parser.add_argument("--draw", action="store_true", help="on the draw: one extra card")
    parser.add_argument("--hand", type=non_negative, default=7, help="opening hand size (default 7)")
    parser.add_argument("--draws-per-turn", type=non_negative, default=1)


def resolve_seen(parser, args):
    if args.seen is not None:
        return args.seen
    if args.turn is None:
        parser.error("pass --turn or --seen")
    return cards_seen(args.turn, args.hand, args.draw, args.draws_per_turn)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Hypergeometric deck odds for card game design.")
    sub = parser.add_subparsers(dest="mode", required=True)

    at_least = sub.add_parser("at-least", help="P(at least NEED copies among the cards seen)")
    by_turn = sub.add_parser("by-turn", help="P(at least NEED copies) for turns 1..N, on play and draw")
    min_copies = sub.add_parser("min-copies", help="smallest number of copies reaching TARGET probability")
    hand = sub.add_parser("hand", help="P(opening hand has FROM..TO copies)")
    for mode in (at_least, by_turn, min_copies, hand):
        mode.add_argument("--deck", type=positive, required=True, help="deck size")
    for mode in (at_least, by_turn, hand):
        mode.add_argument("--copies", type=non_negative, required=True, help="copies or resource cards")
    for mode in (at_least, by_turn, min_copies):
        mode.add_argument("--need", type=positive, default=1, help="how many copies are needed (default 1)")
    add_seen_options(at_least)
    add_seen_options(min_copies)
    min_copies.add_argument("--target", type=float, default=0.9, help="probability to reach (default 0.9)")
    by_turn.add_argument("--turns", type=positive, default=10)
    by_turn.add_argument("--hand", type=non_negative, default=7)
    by_turn.add_argument("--draws-per-turn", type=non_negative, default=1)
    hand.add_argument("--hand", type=non_negative, default=7)
    hand.add_argument("--from", dest="low", type=non_negative, required=True)
    hand.add_argument("--to", dest="high", type=non_negative, required=True)
    args = parser.parse_args(argv)

    if getattr(args, "copies", 0) > args.deck:
        parser.error("--copies cannot exceed --deck")

    if args.mode == "at-least":
        seen = resolve_seen(at_least, args)
        p = p_at_least(args.deck, args.copies, seen, args.need)
        print(f"P(>= {args.need} of {args.copies} in {args.deck}, {seen} cards seen) = {p:.1%}")
    elif args.mode == "by-turn":
        print(f"P(>= {args.need} of {args.copies} in {args.deck})")
        print(f"{'Turn':>4} {'Seen':>5} {'Play':>7} {'Draw':>7}")
        for turn in range(1, args.turns + 1):
            on_play = cards_seen(turn, args.hand, False, args.draws_per_turn)
            on_draw = cards_seen(turn, args.hand, True, args.draws_per_turn)
            print(f"{turn:>4} {on_play:>5} {p_at_least(args.deck, args.copies, on_play, args.need):>7.1%} "
                  f"{p_at_least(args.deck, args.copies, on_draw, args.need):>7.1%}")
    elif args.mode == "min-copies":
        if not 0 < args.target < 1:
            parser.error("--target must be between 0 and 1")
        seen = resolve_seen(min_copies, args)
        for copies in range(args.need, args.deck + 1):
            p = p_at_least(args.deck, copies, seen, args.need)
            if p >= args.target:
                print(f"{copies} copies: P(>= {args.need} in {seen} cards seen) = {p:.1%} >= {args.target:.0%}")
                break
        else:
            print(f"unreachable: even {args.deck} copies stay below {args.target:.0%}")
            return 1
    else:
        if args.low > args.high:
            parser.error("--from must not exceed --to")
        p = p_between(args.deck, args.copies, args.hand, args.low, args.high)
        print(f"P({args.low}..{args.high} of {args.copies} in a {args.hand}-card hand, deck {args.deck}) = {p:.1%}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
