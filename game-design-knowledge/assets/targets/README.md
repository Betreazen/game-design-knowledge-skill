# Примеры целевых коридоров

Стартовые `targets.json` для разных типов игр в формате [metrics_compare.py](../../scripts/metrics_compare.py). Это отправная точка этапа 2 [пайплайна](../../references/pipeline.md#этап-2-опоры-и-целевые-метрики), а не отраслевой стандарт. Почти все числа — предположения, их нужно заменить своими: из опор дизайна, референсных игр и ориентиров в [systems-balance.md](../../references/systems-balance.md) и [genres.md](../../references/genres.md).

Ключ — шаблон имени метрики, побеждает первый подходящий. Для числовой метрики можно задать несколько коридоров списком: `[{"max": 8, "stat": "median"}, {"max": 25, "stat": "p90"}]`. Поля в ключах — пример: называйте их как удобно, но так же, как пишет ваш симулятор или телеметрия.

| Файл | Тип игры | Одна строка JSONL | Ключевые поля |
| --- | --- | --- | --- |
| [pvp-duel.json](pvp-duel.json) | Дуэль 1×1: файтинг, карточная, RTS, настольная, шахматоподобная | игрок в матче | `pick`, `opp_pick` (персонаж, колода, фракция, сборка), `went_first`, `bot`, `win`, `comeback`, `turns` |
| [team-pvp.json](team-pvp.json) | Командный PvP: MOBA, шутер, спорт | игрок в матче | `side`, `pick` (герой), `mmr_gap`, `win`, `comeback`, `abandon`, `duration_min` |
| [roguelike-runs.json](roguelike-runs.json) | Рогалик, roguelite, забег в экшен-RPG | забег | `character`, `win`, `floor_reached`, `died_on_floor_1`, `run_minutes`, `distinct_builds` |
| [levels.json](levels.json) | Уровни: платформер, головоломка, экшен, кампания | игрок на уровне | `level`, `completed`, `attempts`, `quit_on_level`, `time_s` |
| [economy-progression.json](economy-progression.json) | Экономика и прогрессия: RPG, F2P, idle, градостроитель | симулированный игрок на день или сессию | `day`, `gold`, `level`, `sink_ratio`, `stuck`, `minutes_to_next_unlock` |
| [card-duel.json](card-duel.json) | Частный случай дуэли: карточная с ресурсом в колоде | игрок в матче | `pick`, `opp_pick` (колоды), `went_first`, `mana_screw` |

Поля уровня матча (длительность, число смен лидера) повторяются в строке каждого игрока. Читайте их через разрез с одной строкой на матч, например `@went_first=true` или `@side=blue`, иначе n удвоится ([pipeline.md](../../references/pipeline.md#этап-7-измерительный-стенд)).

Метрики, которые `design_metrics.py` не считает напрямую — доля выбора (pick rate), энтропия меты, кривые по времени — считайте отдельно и пишите в JSONL готовым числом или полем.
