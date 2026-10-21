#!/usr/bin/env python3
"""Учебный стенд №2: забеги в игрушечном рогалике, пишет JSONL «строка на забег» (assets/targets/roguelike-runs.json).

Второй пример к example_sim.py (дуэль): здесь меряется кривая сложности и баланс персонажей в PvE.
Конфигурация — данные: --dump-config выгружает её в JSON, --config загружает правленую версию.

Запуск:
  python3 example_runs_sim.py --runs 3000 > runs/before.jsonl
  python3 example_runs_sim.py --dump-config > config.json        # гипотеза — правка config.json
  python3 example_runs_sim.py --runs 3000 --config config.json > runs/after.jsonl
  python3 design_metrics.py runs/before.jsonl --rate win --rate died_on_floor_1 --num floor_reached \
      --num run_minutes --by character --by bot --meta sim=runs --out metrics/before.json

Правила: 8 этажей, на каждом 3 боя и босс на 4-м и 8-м. Бой — обмен ударами до смерти одного:
урон героя (с шансом крита ×2) против здоровья врага, урон врага минус броня героя (не меньше 1).
Здоровье и урон врагов растут на enemy_scale за этаж, у каждого врага разброс ±variance. После боя — выбор одного из трёх улучшений,
после этажа — отдых: лечение rest_heal от максимума. Победа — пройден 8-й этаж.
Боты: greedy выбирает улучшение по приоритетам персонажа и лечится, когда здоровья мало; random — случайно.

Строка JSONL на забег: run, seed, character, bot, win, floor_reached, died_on_floor_1,
run_minutes (условные минуты: раунды боя / 6), build (улучшение, взятое чаще всего).
"""

import argparse
import json
import random
import sys

CONFIG = {
    "floors": 8,
    "fights_per_floor": 3,
    "boss_floors": [4, 8],
    "enemy": {"hp": 20, "damage": 4, "boss_hp_mult": 2.2, "boss_damage_mult": 1.3, "variance": 0.25},
    "enemy_scale": 1.24,
    "rest_heal": 0.3,
    "characters": {
        "warrior": {"hp": 70, "damage": 6, "armor": 2, "crit": 0.05, "priorities": ["armor", "hp", "damage"]},
        "rogue":   {"hp": 45, "damage": 8, "armor": 0, "crit": 0.25, "priorities": ["crit", "damage", "hp"]},
        "mage":    {"hp": 38, "damage": 11, "armor": 0, "crit": 0.10, "priorities": ["damage", "hp", "crit"]},
    },
    "upgrades": {"damage": 2, "hp": 12, "armor": 1, "crit": 0.06, "heal": 0.5},
}


def fight(hero, enemy_hp, enemy_damage, rng):
    rounds = 0
    while True:
        rounds += 1
        hit = hero["damage"] * (2 if rng.random() < hero["crit"] else 1)
        enemy_hp -= hit
        if enemy_hp <= 0:
            return True, rounds
        hero["cur"] -= max(1, round(enemy_damage) - hero["armor"])
        if hero["cur"] <= 0:
            return False, rounds


def upgrade(hero, cfg, rng, bot, picks):
    options = rng.sample(sorted(cfg["upgrades"]), 3)
    if bot == "random":
        choice = rng.choice(options)
    elif "heal" in options and hero["cur"] < 0.4 * hero["hp"]:
        choice = "heal"
    else:
        # крит выше 75% почти ничего не даёт, поэтому жадный бот его пропускает
        ranked = [o for o in hero["priorities"] if o in options and not (o == "crit" and hero["crit"] >= 0.75)]
        choice = ranked[0] if ranked else rng.choice(options)
    value = cfg["upgrades"][choice]
    if choice == "heal":
        hero["cur"] = min(hero["hp"], hero["cur"] + value * hero["hp"])
    elif choice == "hp":
        hero["hp"] += value
        hero["cur"] += value
    else:
        hero[choice] += value
    picks[choice] = picks.get(choice, 0) + 1


def play_run(run, seed, cfg, characters, bots):
    rng = random.Random(seed)
    name, bot = rng.choice(characters), rng.choice(bots)
    hero = dict(cfg["characters"][name])
    hero["cur"] = hero["hp"]
    picks, rounds, floor_reached, alive = {}, 0, 0, True
    enemy = cfg["enemy"]
    for floor in range(1, cfg["floors"] + 1):
        floor_reached = floor
        scale = cfg["enemy_scale"] ** (floor - 1)
        boss = floor in cfg["boss_floors"]
        for i in range(cfg["fights_per_floor"] + (1 if boss else 0)):
            is_boss = boss and i == cfg["fights_per_floor"]
            roll = 1 + rng.uniform(-enemy["variance"], enemy["variance"])
            hp = enemy["hp"] * scale * roll * (enemy["boss_hp_mult"] if is_boss else 1)
            damage = enemy["damage"] * scale * roll * (enemy["boss_damage_mult"] if is_boss else 1)
            won, spent = fight(hero, hp, damage, rng)
            rounds += spent
            if not won:
                alive = False
                break
            upgrade(hero, cfg, rng, bot, picks)
        if not alive:
            break
        hero["cur"] = min(hero["hp"], hero["cur"] + cfg["rest_heal"] * hero["hp"])
    build = max(sorted(picks), key=lambda k: picks[k]) if picks else "none"
    return {"run": run, "seed": seed, "character": name, "bot": bot, "win": alive,
            "floor_reached": floor_reached, "died_on_floor_1": not alive and floor_reached == 1,
            "run_minutes": round(rounds / 6, 1), "build": build}


def load_config(path):
    try:
        with open(path, encoding="utf-8-sig") as stream:
            cfg = json.load(stream)
        for key in ("floors", "fights_per_floor", "boss_floors", "enemy", "enemy_scale", "rest_heal",
                    "characters", "upgrades"):
            cfg[key]
        return cfg
    except (OSError, ValueError, KeyError, TypeError) as err:
        raise SystemExit(f"error: {path}: {err!r}")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Toy roguelike run simulator that writes JSONL for design_metrics.py.")
    parser.add_argument("--runs", type=int, default=2000)
    parser.add_argument("--seed-from", type=int, default=1, help="run i uses seed seed_from + i")
    parser.add_argument("--characters", help="comma-separated characters (default: all)")
    parser.add_argument("--bots", default="greedy", help="comma-separated bots: greedy, random")
    parser.add_argument("--config", help="JSON config; a hypothesis is an edit of this file")
    parser.add_argument("--dump-config", action="store_true", help="print the built-in config as JSON and exit")
    args = parser.parse_args(argv)
    if args.dump_config:
        print(json.dumps(CONFIG, indent=1))
        return 0
    cfg = load_config(args.config) if args.config else CONFIG
    names = [c.strip() for c in args.characters.split(",") if c.strip()] if args.characters else sorted(cfg["characters"])
    bots = [b.strip() for b in args.bots.split(",") if b.strip()]
    unknown = [c for c in names if c not in cfg["characters"]] + [b for b in bots if b not in ("greedy", "random")]
    if unknown or not names or not bots or args.runs < 1:
        parser.error(f"bad --characters/--bots/--runs: {', '.join(unknown) or 'empty'}")
    for i in range(args.runs):
        sys.stdout.write(json.dumps(play_run(i, args.seed_from + i, cfg, names, bots)) + "\n")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit as exit_:
        if isinstance(exit_.code, str):
            print(exit_.code, file=sys.stderr)
            sys.exit(2)
        raise
