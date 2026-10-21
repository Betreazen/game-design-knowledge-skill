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
Бой длиннее 1000 раундов считается поражением героя (защита от зацикленных конфигураций).

Строка JSONL на забег: run, seed, character, bot, win, floor_reached, died_on_floor_1,
run_minutes (условные минуты: раунды боя / 6), build (улучшение, взятое чаще всего).
Код выхода: 0 — успех, 2 — ошибка ввода.
"""

import argparse
import io
import json
import math
import random
import sys
from collections import Counter

MAX_ROUNDS = 1000
STATS = ("damage", "hp", "armor", "crit")

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
    for rounds in range(1, MAX_ROUNDS + 1):
        hit = hero["damage"] * (2 if rng.random() < hero["crit"] else 1)
        enemy_hp -= hit
        if enemy_hp <= 0:
            return True, rounds
        hero["cur"] -= max(1, round(enemy_damage) - hero["armor"])
        if hero["cur"] <= 0:
            return False, rounds
    return False, MAX_ROUNDS


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
    picks[choice] += 1


def play_run(run, seed, cfg, characters, bots):
    rng = random.Random(seed)
    name, bot = rng.choice(characters), rng.choice(bots)
    hero = dict(cfg["characters"][name])
    hero["cur"] = hero["hp"]
    picks, rounds, floor_reached, alive = Counter(), 0, 0, True
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
    build = max(sorted(picks), key=picks.__getitem__) if picks else "none"
    return {"run": run, "seed": seed, "character": name, "bot": bot, "win": alive,
            "floor_reached": floor_reached, "died_on_floor_1": not alive and floor_reached == 1,
            "run_minutes": round(rounds / 6, 1), "build": build}


def number(value, low, high=math.inf, integer=False):
    kinds = (int,) if integer else (int, float)
    return (isinstance(value, kinds) and not isinstance(value, bool)
            and math.isfinite(value) and low <= value <= high)


def config_errors(cfg):
    """Список проблем конфигурации; пустой список — конфигурация годна."""
    if not isinstance(cfg, dict):
        return ["config must be a JSON object"]
    errors = []
    checks = [("floors", 1, 1000, True), ("fights_per_floor", 1, 1000, True),
              ("enemy_scale", 0.01, 100, False), ("rest_heal", 0, 1, False)]
    errors += [f"{key}: expected a number in {lo}..{hi}" for key, lo, hi, whole in checks
               if not number(cfg.get(key), lo, hi, whole)]
    if not (isinstance(cfg.get("boss_floors"), list) and all(number(b, 1, 1000, True) for b in cfg["boss_floors"])):
        errors.append("boss_floors: expected a list of floor numbers")
    enemy = cfg.get("enemy")
    if not isinstance(enemy, dict) or not all(number(enemy.get(k), lo) for k, lo in
                                              (("hp", 1e-9), ("damage", 1e-9), ("boss_hp_mult", 1e-9),
                                               ("boss_damage_mult", 1e-9), ("variance", 0))):
        errors.append("enemy: needs positive hp, damage, boss_hp_mult, boss_damage_mult and variance >= 0")
    elif enemy["variance"] >= 1:
        errors.append("enemy.variance: must be below 1")
    upgrades = cfg.get("upgrades")
    if not isinstance(upgrades, dict) or len(upgrades) < 3:
        errors.append("upgrades: expected an object with at least 3 upgrades")
    else:
        errors += [f"upgrades.{k}: unknown upgrade or bad value" for k, v in upgrades.items()
                   if k not in STATS + ("heal",) or not number(v, 0)]
    characters = cfg.get("characters")
    if not isinstance(characters, dict) or not characters:
        return errors + ["characters: expected a non-empty object"]
    for name, hero in characters.items():
        ok = (isinstance(hero, dict) and number(hero.get("hp"), 1) and number(hero.get("damage"), 1e-9)
              and number(hero.get("armor"), 0) and number(hero.get("crit"), 0, 1)
              and isinstance(hero.get("priorities"), list) and all(p in STATS + ("heal",) for p in hero["priorities"]))
        if not ok:
            errors.append(f"characters.{name}: needs hp >= 1, damage > 0, armor >= 0, crit 0..1 "
                          "and priorities from damage, hp, armor, crit, heal")
    return errors


def load_config(path):
    try:
        with open(path, encoding="utf-8-sig") as stream:
            cfg = json.load(stream)
    except (OSError, ValueError) as err:
        raise SystemExit(f"error: {path}: {err}")
    errors = config_errors(cfg)
    if errors:
        raise SystemExit(f"error: {path}: " + "; ".join(errors))
    return cfg


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
    for stream in (sys.stdout, sys.stderr):
        if isinstance(stream, io.TextIOWrapper):
            stream.reconfigure(errors="backslashreplace")
    try:
        raise SystemExit(main())
    except SystemExit as exit_:
        if isinstance(exit_.code, str):
            print(exit_.code, file=sys.stderr)
            sys.exit(2)
        raise
