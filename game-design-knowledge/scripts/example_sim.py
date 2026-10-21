#!/usr/bin/env python3
"""Учебный стенд: игрушечная дуэльная ККИ с ботами, пишет JSONL по схеме pipeline.md (этап 7).

Нужен, чтобы прогнать цикл «базовая линия → гипотеза → повторный замер» целиком за минуту
и как шаблон своего симулятора. Правила намеренно простые, баланс намеренно неидеальный.

Запуск:
  python3 example_sim.py --games 4000 --seed-from 1 > runs/before.jsonl
  python3 example_sim.py --games 4000 --seed-from 1 --coin > runs/after.jsonl     # гипотеза: монета
  python3 design_metrics.py runs/before.jsonl --rate win --rate comeback --num turns \
      --by went_first --by pick --by pick,opp_pick --by bot --meta sim=example --out metrics/before.json

Правила: 20 здоровья, колода 20 карт, стартовая рука 4, добор 1 за ход, мана = номер своего хода (до 8).
Пустая колода — усталость: 1, 2, 3… урона за каждый пропущенный добор. Существо атакует со следующего
своего хода после розыгрыша. Атакующего блокирует самое крупное свободное существо защитника, которое
переживёт удар или убьёт атакующего; иначе удар идёт в лицо. «Молния» бьёт существо или лицо.
Ход 50 — ничья (win=false у обоих).

Базовая линия намеренно кривая: первый игрок выигрывает около 70%. Учебный пример цикла —
references/pipeline.md, раздел «Учебный прогон».
--coin: второй игрок берёт +1 карту и один раз получает +1 ману (как The Coin в Hearthstone).
--decks-file: колоды из JSON (шаблон: --dump-decks > decks.json). Балансная гипотеза — правка этого файла,
как и в настоящем пайплайне: правим данные, а не код.

Строка JSONL на игрока в партии: match, seed, pick и opp_pick (колоды), bot, opp_bot, went_first, win, draw,
turns, comeback (победил, отставая по здоровью после 4-го хода соперника), dead_cards (карт в руке в конце).
"""

import argparse
import json
import random
import sys

# (стоимость, атака, здоровье) для существ; (стоимость, урон, None) для молний
DECKS = {
    "aggro":    [(1, 2, 1)] * 6 + [(2, 2, 3)] * 6 + [(3, 4, 3)] * 4 + [(2, 3, None)] * 4,
    "midrange": [(2, 2, 3)] * 4 + [(3, 3, 3)] * 5 + [(4, 4, 4)] * 5 + [(5, 5, 4)] * 2 + [(2, 3, None)] * 4,
    "control":  [(1, 2, None)] * 4 + [(3, 4, None)] * 4 + [(2, 1, 4)] * 4 + [(5, 4, 5)] * 4 + [(6, 6, 6)] * 4,
}
START_HP, HAND, MAX_MANA, TURN_LIMIT = 20, 4, 8, 50


def load_decks(path):
    """Колоды из JSON: {"aggro": [{"cost": 1, "power": 1, "health": 1, "count": 4}, ...]}; health null — молния."""
    try:
        with open(path, encoding="utf-8-sig") as stream:
            raw = json.load(stream)
        return {name: [(c["cost"], c["power"], c.get("health")) for c in cards for _ in range(c["count"])]
                for name, cards in raw.items()}
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as err:
        raise SystemExit(f"error: {path}: {err!r}")


def dump_decks(decks):
    out = {}
    for name, cards in decks.items():
        counted = {}
        for card in cards:
            counted[card] = counted.get(card, 0) + 1
        out[name] = [{"cost": c, "power": p, "health": h, "count": n} for (c, p, h), n in counted.items()]
    return out


class Player:
    def __init__(self, deck_name, cards, bot, rng):
        self.deck_name, self.bot = deck_name, bot
        self.library = list(cards)
        rng.shuffle(self.library)
        self.hand, self.board, self.hp, self.turns, self.coin, self.fatigue = [], [], START_HP, 0, 0, 0

    def draw(self, count=1):
        for _ in range(count):
            if self.library:
                self.hand.append(self.library.pop())
            else:
                self.fatigue += 1
                self.hp -= self.fatigue


def cast(player, enemy, card, rng, smart):
    _, power, health = card
    player.hand.remove(card)
    if health is not None:
        player.board.append([power, health, False])  # третий элемент — готов ли атаковать
        return
    killable = [u for u in enemy.board if u[1] <= power]
    if smart:
        lethal = enemy.hp <= power
        target = None if lethal or not killable else max(killable, key=lambda u: u[0])
    else:
        target = rng.choice(enemy.board + [None])
    if target is None:
        enemy.hp -= power
    else:
        target[1] -= power
        enemy.board[:] = [u for u in enemy.board if u[1] > 0]


def play_cards(player, enemy, rng):
    mana = min(player.turns, MAX_MANA) + player.coin
    smart = player.bot == "greedy"
    while True:
        affordable = [c for c in player.hand if c[0] <= mana]
        if not affordable:
            break
        card = max(affordable, key=lambda c: c[0]) if smart else rng.choice(affordable)
        if not smart and rng.random() < 0.2:
            break  # случайный бот иногда просто не тратит ману
        if player.coin and card[0] > mana - player.coin:
            player.coin = 0  # монета тратится, только если без неё карта не по карману
        mana -= card[0]
        cast(player, enemy, card, rng, smart)
        if enemy.hp <= 0:
            return


def attack(player, enemy):
    blockers = sorted(enemy.board, key=lambda u: -u[0])
    for unit in player.board:
        if not unit[2]:
            continue
        useful = [b for b in blockers if b[1] > unit[0] or b[0] >= unit[1]]
        if useful:
            blocker = useful[0]
            blockers.remove(blocker)
            blocker[1] -= unit[0]
            unit[1] -= blocker[0]
        else:
            enemy.hp -= unit[0]
    player.board[:] = [u for u in player.board if u[1] > 0]
    enemy.board[:] = [u for u in enemy.board if u[1] > 0]


def play_match(match, seed, decks, bots, coin):
    rng = random.Random(seed)
    names = sorted(decks)
    first_deck, first_bot = rng.choice(names), rng.choice(bots)
    second_deck, second_bot = rng.choice(names), rng.choice(bots)
    first = Player(first_deck, decks[first_deck], first_bot, rng)
    second = Player(second_deck, decks[second_deck], second_bot, rng)
    first.draw(HAND)
    second.draw(HAND + (1 if coin else 0))
    second.coin = 1 if coin else 0
    hp_after_4, turn = None, 0
    order = [first, second]
    for turn in range(1, TURN_LIMIT + 1):
        active, other = order[(turn - 1) % 2], order[turn % 2]
        active.turns += 1
        active.draw()
        for unit in active.board:
            unit[2] = True  # существа, пережившие ход соперника, готовы атаковать
        play_cards(active, other, rng)
        if other.hp > 0:
            attack(active, other)
        if turn == 8:
            hp_after_4 = (first.hp, second.hp)
        if other.hp <= 0:
            winner = active
            break
    else:
        winner = None
    rows = []
    for me, opp, went_first in ((first, second, True), (second, first, False)):
        won = winner is me
        behind = hp_after_4 is not None and (hp_after_4[0] < hp_after_4[1]) == went_first \
            and hp_after_4[0] != hp_after_4[1]
        rows.append({"match": match, "seed": seed, "pick": me.deck_name, "opp_pick": opp.deck_name,
                     "bot": me.bot, "opp_bot": opp.bot, "went_first": went_first, "win": won,
                     "draw": winner is None, "turns": turn, "comeback": won and behind,
                     "dead_cards": len(me.hand)})
    return rows


def main(argv=None):
    parser = argparse.ArgumentParser(description="Toy card game simulator that writes JSONL for design_metrics.py.")
    parser.add_argument("--games", type=int, default=2000)
    parser.add_argument("--seed-from", type=int, default=1, help="match i uses seed seed_from + i")
    parser.add_argument("--decks", help="comma-separated deck pool (default: all decks)")
    parser.add_argument("--decks-file", help="JSON with deck lists; a hypothesis is an edit of this file")
    parser.add_argument("--dump-decks", action="store_true", help="print the built-in decks as JSON and exit")
    parser.add_argument("--bots", default="greedy", help="comma-separated bots per side: greedy, random")
    parser.add_argument("--coin", action="store_true", help="hypothesis: second player gets +1 card and a one-time +1 mana")
    args = parser.parse_args(argv)
    if args.dump_decks:
        print(json.dumps(dump_decks(DECKS), indent=1))
        return 0
    library = load_decks(args.decks_file) if args.decks_file else DECKS
    names = [d.strip() for d in args.decks.split(",") if d.strip()] if args.decks else list(library)
    bots = [b.strip() for b in args.bots.split(",") if b.strip()]
    unknown = [d for d in names if d not in library] + [b for b in bots if b not in ("greedy", "random")]
    if unknown or not names or not bots or args.games < 1:
        parser.error(f"bad --decks/--bots/--games: {', '.join(unknown) or 'empty'}")
    pool = {name: library[name] for name in names}
    out = sys.stdout
    for i in range(args.games):
        for row in play_match(i, args.seed_from + i, pool, bots, args.coin):
            out.write(json.dumps(row) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
