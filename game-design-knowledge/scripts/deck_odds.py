#!/usr/bin/env python3
"""Вероятности по гипергеометрическому распределению: увидеть нужное вовремя в колоде, мешке или пуле.

Подходит для любой выборки без возвращения: колода карт, мешок фишек, перемешанный пул наград
или противников. Термины ниже карточные, но «копии» — это любые нужные объекты в пуле.

Запуск:
  python3 deck_odds.py at-least --deck 40 --copies 17 --need 3 --turn 3            # на play
  python3 deck_odds.py at-least --deck 40 --copies 17 --need 3 --turn 3 --draw     # на draw
  python3 deck_odds.py at-least --deck 30 --copies 2 --need 1 --seen 7             # явно: 7 вытянутых
  python3 deck_odds.py by-turn --deck 40 --copies 2                                # таблица по ходам 1..10
  python3 deck_odds.py min-copies --deck 40 --need 1 --turn 3 --target 0.90        # сколько копий нужно
  python3 deck_odds.py hand --deck 40 --copies 17 --from 2 --to 5                  # стартовая рука с 2..5

Сколько увидено к ходу T: --hand (по умолчанию 7) + (T - 1) на play, ещё +1 на draw;
--draws-per-turn меняет добор. Муллиганы и поиск по колоде не учитываются.
Правило Karsten «89 + M %» — условное (считает только партии, где ресурсов хватило) и с муллиганом,
поэтому безусловные числа отсюда ниже его порогов. Таблица Karsten — в references/systems-balance.md.

Код выхода: 0 — успех; 1 — в min-copies цель недостижима даже со всей колодой; 2 — ошибка ввода.
"""

import argparse
from math import comb

MAX_DECK = 100_000
MAX_TURNS = 1_000


def p_at_least(deck, copies, seen, need):
    """P(X >= need), X ~ Hypergeometric(deck, copies, seen)."""
    seen = min(seen, deck)
    hits = sum(comb(copies, i) * comb(deck - copies, seen - i) for i in range(need, min(copies, seen) + 1))
    return hits / comb(deck, seen)


def cards_seen(turn, hand, on_draw, draws_per_turn):
    return hand + (turn - 1) * draws_per_turn + (draws_per_turn if on_draw else 0)


def int_in(low, high):
    def parse(text):
        value = int(text)
        if not low <= value <= high:
            raise argparse.ArgumentTypeError(f"expected an integer in {low}..{high}, got {text}")
        return value
    return parse


def add_draw_options(parser, with_turn):
    if with_turn:
        parser.add_argument("--turn", type=int_in(1, MAX_TURNS), help="turn number (cards seen derived from hand and draws)")
        parser.add_argument("--seen", type=int_in(0, MAX_DECK), help="cards seen, overrides --turn")
        parser.add_argument("--draw", action="store_true", help="on the draw: one extra card")
    parser.add_argument("--hand", type=int_in(0, MAX_DECK), default=7, help="opening hand size (default 7)")
    parser.add_argument("--draws-per-turn", type=int_in(0, MAX_DECK), default=1)


def resolve_seen(parser, args):
    if args.seen is not None:
        return args.seen
    if args.turn is None:
        parser.error("pass --turn or --seen")
    return cards_seen(args.turn, args.hand, args.draw, args.draws_per_turn)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Hypergeometric odds for decks, bags and shuffled pools.")
    sub = parser.add_subparsers(dest="mode", required=True)
    at_least = sub.add_parser("at-least", help="P(at least NEED copies among the cards seen)")
    by_turn = sub.add_parser("by-turn", help="P(at least NEED copies) for turns 1..N, on play and draw")
    min_copies = sub.add_parser("min-copies", help="smallest number of copies reaching TARGET probability")
    hand = sub.add_parser("hand", help="P(opening hand has FROM..TO copies)")
    for mode in (at_least, by_turn, min_copies, hand):
        mode.add_argument("--deck", type=int_in(1, MAX_DECK), required=True, help="deck or pool size")
    for mode in (at_least, by_turn, hand):
        mode.add_argument("--copies", type=int_in(0, MAX_DECK), required=True, help="copies of what you need")
    for mode in (at_least, by_turn, min_copies):
        mode.add_argument("--need", type=int_in(1, MAX_DECK), default=1, help="how many copies are needed (default 1)")
    add_draw_options(at_least, with_turn=True)
    add_draw_options(min_copies, with_turn=True)
    add_draw_options(by_turn, with_turn=False)
    add_draw_options(hand, with_turn=False)
    min_copies.add_argument("--target", type=float, default=0.9, help="probability to reach (default 0.9)")
    by_turn.add_argument("--turns", type=int_in(1, MAX_TURNS), default=10)
    hand.add_argument("--from", dest="low", type=int_in(0, MAX_DECK), required=True)
    hand.add_argument("--to", dest="high", type=int_in(0, MAX_DECK), required=True)
    args = parser.parse_args(argv)

    if getattr(args, "copies", 0) > args.deck:
        parser.error("--copies cannot exceed --deck")
    if getattr(args, "need", 0) > args.deck:
        parser.error("--need cannot exceed --deck")

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
                print(f"{copies} copies: P(>= {args.need} in {seen} cards seen) = {p:.1%} >= {args.target:.1%}")
                break
        else:
            print(f"unreachable: with {seen} cards seen even {args.deck} copies stay below {args.target:.1%}")
            return 1
    else:
        if args.low > args.high:
            parser.error("--from must not exceed --to")
        p = (p_at_least(args.deck, args.copies, args.hand, args.low)
             - p_at_least(args.deck, args.copies, args.hand, args.high + 1))
        print(f"P({args.low}..{args.high} of {args.copies} in a {args.hand}-card hand, deck {args.deck}) = {p:.1%}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
