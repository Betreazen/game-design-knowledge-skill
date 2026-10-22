# Жанры и дисциплины: что специфично для каждой области

Что в каждом жанре и каждой дисциплине работает иначе, чем в общей теории: свои принципы, типовые ошибки и метрики здоровья. Справочник открывают на этапе 2 [пайплайна](pipeline.md#этап-2-опоры-и-целевые-метрики), когда для жанра нужны целевые коридоры, и на этапе 10, когда проблема типична для жанра. Жанры разобраны с одинаковой глубиной: ключевые принципы, ошибки, схема замера и 4–8 проверенных источников на раздел. Игра на стыке жанров читает все свои разделы.

**Навигатор.** Найдите жанр, откройте раздел и возьмите стартовый файл коридоров из [assets/targets/](../assets/targets/README.md). Файл — отправная точка: числа в нём предположения, их заменяют своими.

| Жанр или дисциплина | Раздел | Файл коридоров |
| --- | --- | --- |
| Карточные: ККИ, LCG, колодостроители | [2](#2-карточные-игры) | [card-duel.json](../assets/targets/card-duel.json), [pvp-duel.json](../assets/targets/pvp-duel.json) |
| Рогалики, roguelite, roguelike-deckbuilder | [3](#3-рогалики-и-roguelite) | [roguelike-runs.json](../assets/targets/roguelike-runs.json) |
| Левел-дизайн | [4](#4-левел-дизайн) | [levels.json](../assets/targets/levels.json) |
| Нарративный дизайн | [5](#5-нарративный-дизайн) | нет готового; поля — в разделе |
| Стратегии: 4X, RTS, тактика | [6](#6-стратегии-и-тактика) | [pvp-duel.json](../assets/targets/pvp-duel.json), [economy-progression.json](../assets/targets/economy-progression.json) |
| Экшен, платформеры, game feel | [7](#7-экшен-платформеры-game-feel) | [levels.json](../assets/targets/levels.json) |
| Головоломки | [8](#8-головоломки) | [levels.json](../assets/targets/levels.json) |
| Соревновательный мультиплеер, рейтинг | [9](#9-мультиплеер-и-соревновательные-игры) | [pvp-duel.json](../assets/targets/pvp-duel.json), [team-pvp.json](../assets/targets/team-pvp.json) |
| Live service, F2P, монетизация | [10](#10-live-service-f2p-и-этичная-монетизация) | [economy-progression.json](../assets/targets/economy-progression.json) |
| Мобильные и казуальные | [11](#11-мобильные-и-казуальные) | [levels.json](../assets/targets/levels.json), [economy-progression.json](../assets/targets/economy-progression.json) |
| Кооперативные | [12](#12-кооперативные) | [levels.json](../assets/targets/levels.json) |
| Настольные | [13](#13-настольные) | [pvp-duel.json](../assets/targets/pvp-duel.json) |
| Файтинги | [14](#14-файтинги) | [pvp-duel.json](../assets/targets/pvp-duel.json) |
| MMO и онлайн-миры | [15](#15-mmo-и-онлайн-миры) | [economy-progression.json](../assets/targets/economy-progression.json) |
| Симуляторы и системные песочницы | [16](#16-симуляторы-и-системные-песочницы) | [economy-progression.json](../assets/targets/economy-progression.json) |
| Хоррор | [17](#17-хоррор) | [levels.json](../assets/targets/levels.json) |
| VR | [18](#18-vr) | нет готового; поля — в разделе |
| Шутеры: FPS/TPS, hero shooter, battle royale, extraction | [19](#19-шутеры) | [team-pvp.json](../assets/targets/team-pvp.json) |
| RPG: CRPG, JRPG, action RPG, прокачка и сборки | [20](#20-rpg) | [economy-progression.json](../assets/targets/economy-progression.json), [roguelike-runs.json](../assets/targets/roguelike-runs.json) |
| MOBA | [21](#21-moba) | [team-pvp.json](../assets/targets/team-pvp.json) |
| Метроидвании | [22](#22-метроидвании) | [levels.json](../assets/targets/levels.json) |
| Стелс | [23](#23-стелс) | [levels.json](../assets/targets/levels.json) |
| Ритм-игры | [24](#24-ритм-игры) | [levels.json](../assets/targets/levels.json) |
| Приключения, point-and-click, визуальные новеллы | [25](#25-приключения-point-and-click-и-визуальные-новеллы) | [levels.json](../assets/targets/levels.json) |
| Гонки | [26](#26-гонки) | [levels.json](../assets/targets/levels.json), [pvp-duel.json](../assets/targets/pvp-duel.json) |
| Спортивные | [27](#27-спортивные) | [team-pvp.json](../assets/targets/team-pvp.json) |
| Выживание, крафт, песочницы | [28](#28-выживание-крафт-и-песочницы) | [economy-progression.json](../assets/targets/economy-progression.json) |
| Градостроители, менеджмент, тайкуны | [29](#29-градостроители-менеджмент-и-тайкуны) | [economy-progression.json](../assets/targets/economy-progression.json) |
| Открытые миры | [30](#30-открытые-миры) | [economy-progression.json](../assets/targets/economy-progression.json), [levels.json](../assets/targets/levels.json) |
| Idle и incremental | [31](#31-idle-и-incremental) | [economy-progression.json](../assets/targets/economy-progression.json) |
| Party и социальные | [32](#32-party-и-социальные-игры) | [team-pvp.json](../assets/targets/team-pvp.json) (поле `side` — роль) |

## 1. Как пользоваться

1. Найдите раздел жанра в навигаторе. Если игра на стыке (roguelike-deckbuilder, action RPG с открытым миром, градостроитель-рогалик), читайте все её разделы. Номера разделов 1–18 сохранены с прошлых версий, чтобы не ломать ссылки из соседних справочников; новые жанры идут с 19-го.
2. «Ключевые принципы» — проверочный список для ревью дизайна ([design-review.md](design-review.md)) и источник гипотез. «Типичные ошибки» — симптомы, которые стоит искать в замере и на плейтесте. Решения по симптомам — в [mechanics-patterns.md](mechanics-patterns.md).
3. «Что мерить» дан в схеме записи стенда из [pipeline.md](pipeline.md#этап-7-измерительный-стенд): одна строка JSONL на игрока в партии, на забег, на попытку уровня или на игровой день. Ключи вида `rate:win@pick=X` и `num:turns` — выход [design_metrics.py](../scripts/design_metrics.py): `--rate ПОЛЕ` для булевых полей, `--num ПОЛЕ` для чисел, `--by ПОЛЕ` или `--by ПОЛЕ1,ПОЛЕ2` для разрезов, `spread:` — разница лучшей и худшей группы.
4. Поля во всех разделах одни и те же: `pick` и `opp_pick` — выбор игрока и соперника (колода, персонаж, герой, фракция, машина, сборка); `side` — асимметричная сторона (атака и защита, синие и красные, роль в социальной дедукции); `character` — персонаж забега; `level` — уровень, глава, трек или чарт; `day` — игровой день или сессия. Шаблоны коридоров используют те же имена; если ваш стенд пишет другие, поправьте ключи в шаблоне.
5. Метрики, которые скрипт не считает (энтропия, доля выбора, тепловые карты, концентрация выручки), помечены «считается отдельно». Числовые пороги — рабочие ориентиры, а не цитаты источников, если источник не указан рядом. Свои коридоры задаются на этапе 2 пайплайна по [systems-balance.md](systems-balance.md) и [playtesting-metrics.md](playtesting-metrics.md). Книги по жанрам — в [books.md](books.md); генерация контента — в procedural-generation.md, интерфейс и онбординг — в ux-ui.md.
6. Пометки: `[не проверено]` — ссылку, дату или факт не удалось сверить с первоисточником; `[устарело]` — ссылка мертва, рядом дана замена.

## 2. Карточные игры

ККИ (CCG/TCG), LCG, колодостроители и roguelike-deckbuilder. У Magic: The Gathering около 30 лет публичных материалов о дизайне, цифровые ККИ добавили к ним балансировку по телеметрии. Математика колоды и кривая стоимости — в [systems-balance.md](systems-balance.md#410-карточные-и-настольные-игры), покарточные метрики — в [playtesting-metrics.md](playtesting-metrics.md#541-дуэли-и-pvp-11), движок правил — в [architecture-code.md](architecture-code.md#5-движок-правил-пошаговых-игр-карточные-настольные-тактические-roguelike). Чеклист ревью — [design-review.md](design-review.md#99-карточные-и-настольные).

### 2.1 Дизайн сета: скелет, бюджет сложности, идентичность фракций

- **Скелет до карт.** Сет планируют как чертёж дома (Rosewater, Nuts & Bolts 2010). Порядок: число слотов по редкости → распределение по цвету или фракции и по типу → кривая стоимости внутри цвета → функции слотов («removal на коммоне в каждом цвете», «дешёвый блокер») → только потом конкретные карты. Слот описывает функцию, а не карту (Filling the Design Skeleton, 2011). Каждому слоту дают код, чтобы обсуждать дыры до появления текстов.
- **Сложность — ограниченный бюджет.** New World Order (Rosewater 2011) переносит сложность с коммонов на анкоммоны и выше. Одна из мер — сколько карт на коммоне «смотрят» на другие карты на поле. Принцип: «если темы нет на коммоне, это не твоя тема». Новых ключевых слов на сет немного, «вечнозелёные» переиспользуются.
- **Lenticular design** (Rosewater, 16.12.2014) — карта, которую новичок читает просто, а опытный игрок видит в ней глубину. Глубина без новых слов.
- **Идентичность фракций.** Mechanical Color Pie 2021 расписывает для каждого цвета основные, вторичные и третичные возможности и то, чего цвет не умеет. Слабости важнее сильных сторон: они создают взаимодействие и причину играть в два цвета. Шаблон подходит для фракций, команд и домов любой игры.
- **Адресат у каждой механики.** Психографии Timmy (опыт, большие эффекты), Johnny (самовыражение, комбо) и Spike (победа) — «Timmy, Johnny, and Spike Revisited» (2006).
- **Лимитед и конструктед — разные игры.** Лимитед балансируют по силе коммонов и по as-fan — сколько карт определённого вида в среднем попадает в бустер ([MTG Wiki](https://mtg.wiki/page/As-fan)). Конструктед — по лучшим картам формата. Power creep сдерживают ротация (Standard) или «пенсия» героев (Living Legend во Flesh and Blood). WotC называет свой подход «лестницей Эшера»: одно ослабляют, другое усиливают, общий уровень держится ровным (Rosewater, Blogatog, 15.11.2019); комментаторы с этой оценкой спорят.

### 2.2 Ресурсные системы

Ресурсная система определяет долю «не-игр»: партий, где игрок не может действовать из-за расклада. Классика — mana screw и mana flood в MTG. Большинство современных ККИ строят ресурс так, чтобы его нельзя было не получить.

| Игра | Ресурс | Дисперсия ресурса | Правила |
| --- | --- | --- | --- |
| Magic: The Gathering | Карты земель в колоде, одна земля за ход | Высокая: screw и flood | [Comprehensive Rules](https://magic.wizards.com/en/rules) |
| Flesh and Blood | Pitch: любая карта — ресурс; таблица «cost–pitch–power» для циклов | Низкая | [Revealing Cycles](https://legacy.fabtcg.com/en/articles/revealing-cycles/), 2019 |
| One Piece Card Game | Отдельная колода ресурса DON!!, ресурс приходит каждый ход | Нет по ресурсу | [Страница правил Bandai](https://en.onepiece-cardgame.com/rules/) |
| Disney Lorcana | Inkwell: раз в ход карту с символом чернил можно положить ресурсом | Игрок сам выбирает, чем жертвовать | [Comprehensive Rules 2.2.0](https://files.disneylorcana.com/Comprehensive-Rules_2.2.0-EN.pdf) |
| Star Wars: Unlimited | При подготовке 2 карты из руки в ресурсы, затем по желанию 1 любая карта за раунд | Низкая | [Comprehensive Rules v8.0](https://cdn.starwarsunlimited.com//SWH_Comp_Rules_v8_0_e26603c6e1.pdf) |
| Pokémon TCG Pocket | Energy Zone: одна Energy за ход без энергокарт; колода 20 карт | Низкая | [pokemon.com](https://www.pokemon.com/us/strategy/learn-how-to-build-a-deck-in-pokemon-tcg-pocket), 30.01.2025 |

- Чем проще ресурс, тем шире аудитория. Снижение «не-игр» — явная цель у Flesh and Blood и Pokémon Pocket.
- Ресурс без случайности переносит дисперсию в добор, триггеры и порядок колоды. Мерить надо «не-игры» в целом, а не только нехватку ресурса.
- Правила задают компенсацию первого хода, но не снимают вопрос: преимущество хода меряют всегда (`rate:win@went_first=true`). Приёмы компенсации — строки Б1–Б4 в [mechanics-patterns.md](mechanics-patterns.md#4-баланс-и-честность).
- Правила франшизных ККИ обновляются несколько раз в год. Перед работой берите текущую версию со страницы правил: номер стоит на первой странице PDF.

### 2.3 Как передавать IP через механику

- **Feelings-first** (Danny Schaefer, Star Wars: Unlimited): карту героя проектируют от ощущения «каким он должен ощущаться», потом подбирают механику. **Резонанс** (Rosewater, GDC 2016): механика рассказывает то же, что арт, имя и flavor text.
- **Каналы передачи IP**: лидер или герой, который задаёт цвета и стиль колоды; ресурс с флейвором; условие победы в тоне IP (в Lorcana — лор через квесты, а не прямая агрессия). Сет можно планировать как кусочек вселенной (SWU, Shadowy Insights, 2024).
- **Top-down.** Innistrad «с первого дня» проектировался от жанра ужасов к механикам ([C'mon Innistrad, Part 1](https://magic.wizards.com/en/news/making-magic/cmon-innistrad-part-1-2011-09-02), 2011).

### 2.4 Баланс цифровых ККИ

**Win rate — сигнал, а не цель.** У каждой карты своя роль: «у каждой карты есть дом в мете» (Riot, Legends of Runeterra). Метрики обманчивы без интерпретации (Giovannetti, Slay the Spire, GDC 2019). Две оси дают четыре случая:

| Доля выбора | Win rate | Что значит | Что делать |
| --- | --- | --- | --- |
| Высокая | Высокий | Кандидат в доминирующие карты | Проверить матрицу матчапов и фрустрацию, затем решать |
| Высокая | Низкий | Ловушка: выглядит сильной, но проигрывает | Обучение, ясность текста; разрез по уровню игрока |
| Низкая | Высокий | Нишевая или недооценённая | Часто ничего; проверить размер выборки |
| Около 0 | — | «Мёртвая» карта | Кандидат на ап или переделку (дашборды Monster Train) |

- **Нерф за фрустрацию, а не только за силу.** Критерии Hearthstone (Eric Dodds, 2014): карта неинтерактивна, против неё «бесит играть», она непредсказуема или превосходит всё в своей стоимости. В Legends of Runeterra Lee Sin с WR около 53% ослабили за фрустрацию (Steve Rubin, 2020). Фрустрацию меряют опросом после матча.
- **Частота правок — компромисс между свежестью и доверием к коллекции.** Hearthstone после релиза меняет карты минимально, Legends of Runeterra правит регулярно, Marvel Snap меняет числа без обновления клиента раз в две недели (заметки разработчиков в [Marvel Snap Zone, 09.11.2023](https://marvelsnapzone.com/marvel-snap-november-9-2023-ota-card-balance-updates/)). Подход записывают в опоры ([раздел 33](#33-расхождения-и-пробелы), пункт 1).
- **Короткая партия и ставки.** Marvel Snap: партия около 3 минут и 6 ходов, удвоение ставки, отступление без полной потери; сложность вводят картами по мере роста коллекции (Brode, GDC 2023).

### 2.5 Физическая ККИ и правила как продукт

- Напечатанную карту не исправить: остаются бан-листы, ограничения и эррата, а эррата дорога. Поэтому до печати нужны симулятор партий (этапы 7–8 [пайплайна](pipeline.md#этап-7-измерительный-стенд)) и долгий плейтест с людьми. Ротация и «пенсия» героев управляют силой пула без изменения карт.
- Образец правил — Magic Comprehensive Rules: пронумерованные пункты, глоссарий, слои эффектов (613), приоритет (117), стек (405, 608), state-based actions (704). Так же устроены правила Lorcana, Star Wars: Unlimited и One Piece Card Game. Для движка это мост «правило → тест» (этап 6 пайплайна); как писать — [documentation.md](documentation.md#7-правила-и-параметры-систем-единый-источник-правды).

### 2.6 Roguelike-deckbuilder и колодостроители

- **Колода — это прогрессия забега.** Ключевые решения: взять карту, пропустить или убрать. Удаление ценно так же, как добавление (Slay the Spire). Slay the Spire поднял сервер метрик до раннего доступа (Giovannetti, GDC 2019).
- **Механика → плейтест → арт.** Monster Train делал арт после плейтестов; дашборды показывали pick rate и WR по связкам кланов и карты, которые никто не берёт (Mark Cooke, 2020).
- **Скейлинг одного числа.** Balatro сводит прогрессию к счёту против blind и множителям; главный источник — слот-roguelike Luck Be a Landlord. Системы без удовольствия вырезаются (LocalThunk, 2024).
- **Читаемость и модульность.** Inscryption заменил текст иконками сигилов (Mullins, GDC 2022). Dominion: набор из 10 карт королевства на партию даёт реиграбельность без новых правил (Vaccarino).

### Типичные ошибки

- Тема механики есть только на редких картах (нарушение NWO); взрыв ключевых слов на коммонах.
- Неинтерактивные комбо; карты, против которых «бесит играть», хотя WR в норме.
- Баланс только по WR, без разрезов по колоде, мастерству и очерёдности хода.
- Power creep без ротации или «пенсии»; слишком частые правки в цифровой ККИ.
- Ресурсная система с «не-играми» без компенсации; нечитаемые карты при низком разрешении.

### Что мерить

Одна строка на игрока в партии; `pick` — колода или архетип:

```json
{"match": 77, "seed": 77, "pick": "Red-Rush", "opp_pick": "Blue-Control", "bot": "mcts", "went_first": true, "win": false, "turns": 9, "comeback": false, "no_game": false, "curve_hit_t3": true, "mulligan": false}
```

| Метрика | Ключ или способ | Что показывает |
| --- | --- | --- |
| Преимущество хода | `rate:win@went_first=true` | Нужна ли компенсация второму игроку |
| Сила колоды и матчапы | `rate:win@pick=*`, `rate:win@pick=*,opp_pick=*`, `spread:win@pick` | Доминирующие колоды и «камень-ножницы-бумага»; зеркала исключать |
| Длина партии | `num:turns@went_first=true` | Темп; одна строка на партию |
| «Не-игры» | `rate:no_game` (нет ходов или ресурса к ходу 3–4) | Дисперсия ресурса и добора |
| Попадание в кривую | `rate:curve_hit_t3`; теоретически — гипергеометрика | Состав колоды и кривая стоимости |
| Камбэк и муллиган | `rate:comeback`, `rate:win@mulligan=true` | Снежный ком; цена плохой стартовой руки |
| Разнообразие меты | 1/Σp² и энтропия по доле `pick`; считается отдельно | Застой меты |

Покарточный файл — строка на карту в колоде игрока в партии: `{"match", "card", "pick", "drawn", "played", "opening_hand", "win"}`. `rate:win@card=*,drawn=true` — аналог GIH WR, если `drawn` включает и стартовую руку (у 17lands это доля побед в партиях, где карта пришла в руку в стартовой руке или добором; [Metrics Definitions](https://www.17lands.com/metrics_definitions)), `rate:played@card=*` — мёртвая ли карта в руке. Для roguelike-deckbuilder — строка на карту в предложении `{"run", "act", "card", "picked", "run_win"}`: `rate:picked@card=*` против `rate:run_win@card=*,picked=true` даёт разрыв «берут, но проигрывают». Опрос «бесило ли играть против» — `rate:annoying@opp_pick=*`.

Шаблоны коридоров: [card-duel.json](../assets/targets/card-duel.json) и [pvp-duel.json](../assets/targets/pvp-duel.json).

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Nuts & Bolts: Design Skeleton](https://magic.wizards.com/en/news/making-magic/nuts-bolts-design-skeleton-2010-02-15), [Filling the Design Skeleton](https://magic.wizards.com/en/news/making-magic/nuts-bolts-filling-design-skeleton-2011-02-28) | Mark Rosewater, 2010–2011 | Скелет сета: слоты по редкости, цвету, функции |
| [New World Order](https://magic.wizards.com/en/news/making-magic/new-world-order-2011-12-05) | Rosewater, 2011 | Сложность как бюджет по редкостям |
| [Lenticular Design](https://magic.wizards.com/en/news/making-magic/lenticular-design-2014-12-15) | Rosewater, 16.12.2014 | Глубина без сложности для новичков |
| [Mechanical Color Pie 2021](https://magic.wizards.com/en/news/making-magic/mechanical-color-pie-2021) | Rosewater, 2021 | Шаблон механической идентичности фракций |
| [Twenty Years, Twenty Lessons](https://www.gdcvault.com/play/1023186/) | Rosewater, GDC 2016 | Ограничения, резонанс, «любят, но не обожают — провал» |
| [Hearthstone's Card Balance Philosophy](https://hearthstone.blizzard.com/en-gb/blog/12383909) | Eric Dodds, 2014 | Критерии нерфа; «контрить новыми картами» |
| [Designing MARVEL SNAP](https://gdcvault.com/play/1029024/Designing-MARVEL-SNAP) | Ben Brode, GDC 2023 | Короткая партия, удвоение ставки, бумажный прототип |
| [RubinZoo о балансе LoR](https://outof.games/news/2215-riots-rubinzoo-discusses-recent-runeterra-card-changes-card-balance-design-process-and-more/) | Steve Rubin, 2020 | Нерф за фрустрацию при WR около 53% |
| [Slay the Spire: Metrics Driven Design and Balance](https://www.gdcvault.com/browse/gdc-19/play/1025731) | Anthony Giovannetti, GDC 2019 | Метрики с ранней стадии; где они обманывают |
| [Balatro inspired by Luck Be a Landlord](https://shacknews.com/article/139116/balatro-inspiration-luck-be-a-landlord-reddit-ama) | LocalThunk, Shacknews 2024 | Прогрессия одним числом |
| [Sacrifices Were Made: The Inscryption Post-Mortem](https://gdcvault.com/play/1027609/Independent-Games-Summit-Sacrifices-Were) | Daniel Mullins, GDC 2022 | Иконки вместо текста, мета-нарратив |
| [The Secret History of Dominion](https://dominionstrategy.com/2013/06/24/the-secret-history-of-dominion/) | Donald X. Vaccarino, 2013 | Происхождение deckbuilding, история карт |
| [Danny Schaefer on a "feelings-first" approach](https://brandsuntapped.com/?p=11576), [Shadowy Insights](https://starwarsunlimited.com/articles/shadowy-insights-danny-schaefer) | Brands Untapped, около 2024; FFG, 2024 | Передача IP через механику, сет как кусочек мира |
| Официальные правила франшизных ККИ: [One Piece Card Game](https://en.onepiece-cardgame.com/rules/), [Disney Lorcana](https://files.disneylorcana.com/Comprehensive-Rules_2.2.0-EN.pdf), [Star Wars: Unlimited](https://cdn.starwarsunlimited.com//SWH_Comp_Rules_v8_0_e26603c6e1.pdf), [Pokémon TCG Pocket](https://www.pokemon.com/us/strategy/learn-how-to-build-a-deck-in-pokemon-tcg-pocket) | Bandai, Ravensburger, FFG, The Pokémon Company | Первоисточник ресурсных систем; версии меняются, проверяйте номер |

## 3. Рогалики и roguelite

### Ключевые принципы

- **Roguelike — спектр, а не чек-лист.** Berlin Interpretation (2008) перечисляет 9 «высоких» факторов (случайная генерация, permadeath, пошаговость, сетка, немодальность, сложность взаимодействий, управление ресурсами, hack'n'slash, исследование) и 6 «низких». Позже её критиковали как узкий канон. Roguelite — permadeath плюс сохраняемая мета-прогрессия.
- **Случайно, но всегда проходимо.** Генератор Spelunky: сетка комнат 4×4, сначала гарантированный путь решения, потом побочные комнаты из шаблонов. Валидатор проходимости обязателен.
- **Мастерство важнее мета-прогрессии** (Josh Ge, 2025). Мета-прогрессия не подменяет навык. Hades даёт нарратив и косметику, а добровольное усложнение — Pact of Punishment.
- **Часы давления.** Food clock и аналоги не дают безопасно фармить (Ge, 2014).
- **Смерть — контент.** Каждый забег продвигает историю; смерть — нарративное событие, а не сброс (Kasavin, Hades).
- **Статика и процедура вместе.** Ручные вставки в процедурную карту (Ge, 2019).
- **Малые рогалики с плотными решениями** вместо «рандома ради рандома». Michael Brough (868-HACK, Imbroglio) работает с маленьким полем и «случайностью, о которой можно принять осознанное решение» (Leigh Alexander, Game Developer, 2013).

### Типичные ошибки

- Неравные забеги: невыигрываемые сиды или «мёртвый старт».
- Мета-прогрессия как обязательный гринд: навык обесценивается.
- Генерация разнообразная, но ощущается одинаково (проблема «10 000 тарелок овсянки»: каждая математически уникальна, а игрок видит просто овсянку; Kate Compton, «So you want to build a generator…», 2016).
- Бэктрекинг и пустые комнаты (Ge, 2022).
- Забег слишком длинный для заданной частоты смертей.

### Что мерить

Одна строка на забег:

```json
{"run": 9001, "seed": 9001, "character": "Ironclad", "ascension": 5, "bot": "heuristic", "meta_level": "none", "win": false, "floor_reached": 23, "died_on_floor_1": false, "killer": "Act2Boss", "run_minutes": 40}
```

| Метрика | Ключ или способ | Что показывает |
| --- | --- | --- |
| Баланс персонажей | `rate:win@character=*`, `spread:win@character` | Персонаж, который выигрывает заметно чаще других |
| Кривая сложности | `rate:win@ascension=*` | Путь «новичок → эксперт» по ступеням |
| Стены сложности | `num:floor_reached`, `rate:died_on_floor_1`, доля смертей по `killer` | Мёртвый старт, пики смертей на этажах и боссах |
| Честность RNG | `spread:win@seed_bucket` при одной стратегии бота | Дисперсия исхода по сидам |
| Проходимость генератора | `rate:solvable` по прогону валидатора; должна быть ровно 1.0 | Невыигрываемые уровни |
| Вклад мета-прогрессии | `rate:win@meta_level=*` (none против full) | Подменяет ли мета навык |
| Разнообразие билдов среди побед | Энтропия по архетипу билда; считается отдельно | Одна выигрышная стратегия |
| Длина и ритм | `num:run_minutes`, время до первой смерти, забегов до первой победы | Соответствие длины забега частоте смертей |

Шаблон коридоров: [roguelike-runs.json](../assets/targets/roguelike-runs.json). Метрики — [playtesting-metrics.md](playtesting-metrics.md#543-рогалики), чеклист ревью — [design-review.md](design-review.md#98-рогалики).

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Berlin Interpretation](https://www.roguebasin.com/index.php/Berlin_Interpretation) | IRDC 2008, опубликовал Jeff Lait | Факторы жанра как спектр |
| [Grid Sage Games blog](https://www.gridsagegames.com/blog/) | Josh Ge, 2013–2026 | Designing for Mastery (2025), Food Clocks (2014), Static vs. Procedural (2019), Backtracking (2022) |
| [Procedural Generation in Game Design](https://emshort.blog/2017/06/08/procedural-generation-in-game-design/) | ред. Tanya X. Short, Tarn Adams; CRC, 2017 | Главы практиков о генерации карт, предметов и историй |
| [Spelunky](https://bossfightbooks.com/products/spelunky-by-derek-yu) | Derek Yu, Boss Fight Books, 2016 | Рандомизация, сложность, доведение до релиза |
| [Spelunky Generator Lessons](http://tinysubversions.com/spelunkyGen/) | Darius Kazemi | Интерактивный разбор генератора с гарантированным путём |
| [Dive into the dialogue of Hades](https://gdconf.com/news/dive-dialogue-hades-gdc-2021) | Greg Kasavin, Darren Korb; GDC 2021 | Нарратив, растущий с каждой смертью |
| [GDC Podcast ep. 16: Roguelikes and narrative design](https://gdconf.com/news/roguelikes-and-narrative-design-hades-creative-director-greg-kasavin-gdc-podcast-ep-16) | GDC, 2021 | Смерть как нарративное событие |
| [Beyond Procedural Horizons](https://www.gdcvault.com/play/1025069/) | Emily Short и др., GDC 2018 | Генерация нарратива, музыки и персонажей |
| [Roguelike Celebration](https://www.roguelike.club/) | ежегодно, последняя — 17–18.10.2026 | Архив докладов на YouTube |
| [Subverting historical cause & effect: generation of mythic biographies in Caves of Qud](https://doi.org/10.1145/3102071.3110574) | Jason Grinblat, Brian Bucklew; FDG 2017 | Процедурная история: сначала событие, потом подобранная причина |
| [The gorgeous math of Michael Brough's 868-HACK](https://gamedeveloper.com/design/the-gorgeous-math-of-michael-brough-s-i-868-hack-i-) | Leigh Alexander, Game Developer, 2013 | Малые рогалики, управляемая случайность, долгосрочные решения |
| [So you want to build a generator…](https://galaxykate0.tumblr.com/post/139774965871/so-you-want-to-build-a-generator) | Kate Compton, 22.02.2016 | Проблема «овсянки»: уникальность без воспринимаемой разницы |
| [3 lessons in storytelling from Inscryption](https://blog.unity.com/en/games/3-lessons-in-storytelling-from-inscryption) | Unity, около 2022 | Мета-структура в три акта со сменой жанра |

## 4. Левел-дизайн

### Ключевые принципы

- **Одна идея — одна арка.** Kishōtenketsu: ввести механику → развить → неожиданный поворот → показать мастерство (Koichi Hayashida, Super Mario 3D Land, 2012). Обучение через вариации ситуации, а не через текст.
- **Signposting.** Свет, контраст, «хлебные крошки», ориентиры. Игрок знает, что делать, но не знает как. Навигация должна быть интересной, а не только понятной (Dan Taylor, Ten Principles for Good Level Design, GDC 2013).
- **Gating и pacing.** Чередование напряжения и разрядки. Beat chart — таблица «бит → механика → эмоция → длительность».
- **Blockout рано, арт поздно.** Процесс The Level Design Book: pre-production → combat design → layout → blockout с плейтестом → scripting → lighting → env art → release. Плейтест блокаута — главный этап.
- **Модульность** экономит производство: семь модульных наборов дали больше 400 уникальных интерьеров Skyrim; наборы делали два художника, подземелья — восемь левел-дизайнеров около двух с половиной лет (Joel Burgess, Nate Purkeypile, GDC 2013).
- **Целостность.** Геймплей, нарратив и арт поддерживают друг друга (Steve Lee, Arkane, 2017).
- **Архитектура** даёт язык пространства: ритм, prospect–refuge, вход и выход (Totten).

### Типичные ошибки

- Арт до проверки блокаута.
- Нет ориентиров, однообразные модули: игрок теряется.
- Механика вводится текстом, а не ситуацией.
- Плоский pacing: всё на одной интенсивности.
- Одноразовые идеи без развития и поворота.

### Что мерить

Одна строка на игрока в секции уровня (телеметрия плейтеста):

```json
{"player": "p07", "level": "1-3", "section": "B", "time_s": 74, "deaths": 2, "lost": false, "main_path_unaided": true, "secret_found": false, "quit_on_level": false}
```

- `num:time_s@section=*` против плана из beat chart.
- `rate:main_path_unaided` — нашли главный путь без подсказки; `rate:secret_found` — секреты.
- `rate:quit_on_level@section=*` — где бросают уровень; `rate:lost@section=*` — долгая стоянка или бэктрекинг.
- Тепловые карты смертей и застреваний по координатам — считается отдельно. Шаблон коридоров: [levels.json](../assets/targets/levels.json).

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [An Architectural Approach to Level Design, 2nd ed.](https://www.routledge.com/An-Architectural-Approach-to-Level-Design-Second-edition/Totten/p/book/9780815361367) | Christopher W. Totten; CRC, 2019 | Архитектурная теория уровней |
| Level Design: Processes and Experiences | ред. C. W. Totten; CRC, 2016 | Эссе практиков о процессе |
| [The Level Design Book](https://book.leveldesignbook.com/), [Process overview](https://book.leveldesignbook.com/process/overview) | открытая книга, CC BY-NC-SA 4.0; основатель проекта Robert Yang, авторство коллективное | Процесс от pre-production до релиза, разборы уровней |
| [Level Design Workshop: An Approach to Holistic Level Design](https://www.gdcvault.com/play/1024301/) | Steve Lee, GDC 2017 | Уровень как единство геймплея, нарратива и арта |
| [The Structure of Fun: Learning from Super Mario 3D Land's Director](https://www.gamedeveloper.com/design/the-structure-of-fun-learning-from-i-super-mario-3d-land-i-s-director) | Christian Nutt, интервью с Koichi Hayashida, 2012 | Kishōtenketsu, одна идея на уровень |
| [Super Mario 3D World's 4 Step Level Design](https://www.youtube.com/watch?v=dBmIkEvEBtA) | Mark Brown, GMTK, 16.03.2015 | Видеоразбор того же принципа |
| [Ten Principles for Good Level Design](https://www.youtube.com/watch?v=iNEe3KhMvXM) | Dan Taylor (Square Enix Montreal), GDC 2013; запись на канале GDC с 2018 | Десять принципов: интересная навигация, повествование без слов, ясные цели, риск и награда (перечень по конспектам слушателей) |
| [Skyrim's Modular Approach to Level Design](https://www.gamedeveloper.com/design/skyrim-s-modular-approach-to-level-design) | Joel Burgess, Nate Purkeypile; GDC 2013, Level Design in a Day; текст 2013 | Семь наборов, больше 400 интерьеров, состав команды и сроки |
| Комментарии разработчиков Half-Life 2 | Valve, в игре: Lost Coast (2005), Episode One (2006), Episode Two (2007); для самой Half-Life 2 — 3,5 ч в [обновлении к 20-летию](https://www.half-life.com/halflife2/20th) (2024) | Сигналы, направление взгляда, обучение без текста |

## 5. Нарративный дизайн

### Ключевые принципы

- **Структура под реиграбельность.** Quality-based и salience-based структуры, storylets и waypoint-нарратив масштабируются лучше дерева ветвлений (Emily Short, 2016).
- **Окружение и системы рассказывают сами.** Environmental storytelling: следы событий, выводы игрока (Smith & Worch, 2010). Системный нарратив из модульных «кирпичиков» (Ken Levine, Narrative Legos, 2014).
- **Без лудонарративного диссонанса.** Механики и сюжет говорят одно (Clint Hocking, 2007).
- **Инструменты для писателя.** ink и Yarn Spinner позволяют итерировать без программиста; Yarn Spinner поддерживает Godot.
- **Сюжет в реиграбельном жанре.** Мета-нарратив (Inscryption) и нарратив через смерть (Hades) встраивают историю в повторяемые забеги; квесты открытого мира — в [разделе 30](#30-открытые-миры), выборы в приключениях — в [разделе 25](#25-приключения-point-and-click-и-визуальные-новеллы). Навыки как голоса-персонажи и провал как контент — Disco Elysium: пассивные проверки звучат репликами навыков, а провал «красной» проверки разыгрывается как сцена (ZA/UM, devblog, 2016).

### Типичные ошибки

- Экспоненциальное ветвление: контент, который видит 5% игроков.
- Сюжет в катсценах, оторванный от механик.
- Описания и тексты предметов, противоречащие их механике.

### Что мерить

Строка на игрока в узле выбора и строка на сцену:

```json
{"player": "p07", "node": "ch2_dock", "option": "B", "scene_skipped": false, "read_time_s": 41}
```

- Распределение `option` по узлу: выбор, который делают 95% игроков, ложный (считается отдельно по долям).
- `rate:scene_skipped@scene=*`, `num:read_time_s` — пропуск и чтение.
- Доля увиденного контента на игрока — `num:content_seen_share` в строке сессии.
- Опрос: могут ли игроки пересказать мотивы персонажей. Готового шаблона коридоров нет; для глав подойдёт [levels.json](../assets/targets/levels.json), где `level` — глава.

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| The Game Narrative Toolbox | Tobias Heussner, Toiya Kristen Finley, Jennifer Brandes Hepler, Ann Lemay; CRC Press / Routledge, 2015 | Практический учебник: от питча до диалогов |
| [Beyond Branching: Quality-Based, Salience-Based, and Waypoint Narrative Structures](https://emshort.blog/2016/04/12/beyond-branching-quality-based-and-salience-based-narrative-structures/) | Emily Short, 2016 | Альтернативы дереву ветвлений |
| [ink](https://www.inklestudios.com/ink/) | inkle; MIT | Язык нарративных скриптов, встраивается в движок |
| [Yarn Spinner](https://www.yarnspinner.dev/) | Yarn Spinner | Диалоги для Unity, Godot, Unreal |
| [Twine](https://twinery.org/) | open source; v2.12.1 от 06.10.2026 | Прототип ветвящегося нарратива без кода |
| [Ludonarrative dissonance](https://en.wikipedia.org/wiki/Ludonarrative_dissonance) | Clint Hocking, блог Click Nothing, 2007 | Конфликт механики и сюжета. Старый адрес на Typepad `[устарело]`; новый: clicknothing.com/2007/10/07/ludonarrative-d/ |
| [Narrative Legos](https://www.gdcvault.com/play/1020434/) | Ken Levine, GDC 2014 | Системный нарратив |
| [What Happened Here? Environmental Storytelling](https://www.gdcvault.com/play/1012647/) | Harvey Smith, Matthias Worch; GDC 2010 | Пространство как рассказчик |
| [Hamlet on the Holodeck](https://en.wikipedia.org/wiki/Hamlet_on_the_Holodeck) | Janet H. Murray, 1997; 2-е изд. 2017 | Агентность, иммерсия, трансформация |
| [On skill checks](https://discoelysium.com/devblog/2016/09/19/on-skill-checks), [On active skill checks](https://discoelysium.com/devblog/2016/10/06/active-skill-checks) | ZA/UM, devblog Disco Elysium, 19.09 и 06.10.2016 | Навыки как голоса, белые и красные проверки, провал как контент |

## 6. Стратегии и тактика

### Ключевые принципы

- **Интересные решения** (Sid Meier, GDC 2012). У каждого варианта есть цена. Плохие решения — очевидные, случайные и принимаемые без информации.
- **Вода находит трещину** (Soren Johnson, 2011). Игроки оптимизируют и эксплуатируют любую дыру и не ценят своё время: отсюда микроменеджмент и гринд. Доминирующие стратегии ищут до релиза.
- **Тема поддерживает, смысл в механике** (Johnson, Theme is Not Meaning).
- **Детерминизм и полная информация** (Into the Breach: намерения врагов видны, поле 8×8, защита зданий вместо килл-рейса) против случайности с воспринимаемой справедливостью (XCOM: Enemy Within на Easy и Normal скрыто прерывает серии промахов — Ananda Gupta, PCGamesN, 2013; Johnson, Playing the Odds).
- **Борьба со снежным комом**: догоняющие механики, издержки расширения. Паттерны — [mechanics-patterns.md](mechanics-patterns.md#6-темп-и-длительность).

### Типичные ошибки

- Доминирующая стратегия, «единственный путь».
- Обязательный микроменеджмент; скучная оптимальная игра.
- Снежный ком: исход ясен за час до конца.
- ИИ, который легко эксплуатировать или который заметно читерит.

### Что мерить

Одна строка на игрока в партии:

```json
{"match": 310, "seed": 310, "pick": "Rome", "opp_pick": "Carthage", "strategy": "wide", "bot": "mcts", "went_first": true, "win": true, "turns": 142, "leader_at_mid": true, "empty_turns": 6, "decisions_per_turn": 4.2}
```

- `rate:win@pick=*`, `rate:win@pick=*,opp_pick=*`, `rate:win@strategy=*` — перекосы фракций и стратегий; энтропия выборов — считается отдельно.
- `rate:win@leader_at_mid=true` — предсказуемость исхода. Если лидер на середине выигрывает больше чем в 90% партий, это снежный ком (ориентир из заметок).
- `num:empty_turns`, `num:decisions_per_turn`, время хода — пустые ходы и перегрузка.
- Эксплойты: ограниченные и поисковые боты из [стенда](pipeline.md#этап-7-измерительный-стенд), фаззинг симуляции. Шаблоны коридоров: [pvp-duel.json](../assets/targets/pvp-duel.json) для дуэлей, [economy-progression.json](../assets/targets/economy-progression.json) для экономики 4X. Стоимость юнитов и законы Ланчестера — [systems-balance.md](systems-balance.md#44-rts-стоимость-юнитов-контр-треугольники-ланчестер), чеклист ревью — [design-review.md](design-review.md#96-стратегии).

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Water Finds a Crack](https://www.designer-notes.com/game-developer-column-17-water-finds-a-crack/) | Soren Johnson; Game Developer, 2011 | Игроки эксплуатируют любые дыры |
| [Theme is Not Meaning, Part I](http://www.designer-notes.com/?p=237), [Part II](http://www.designer-notes.com/?p=240) | Soren Johnson, около 2010 | Смысл игры в механиках, а не в теме |
| [Seven Deadly Sins for Strategy Games](http://www.designer-notes.com/?p=106), [Sid's Rules](http://www.designer-notes.com/?p=119), [Playing the Odds](http://www.designer-notes.com/?p=171), [When Choice is Bad](http://www.designer-notes.com/?p=609) | Soren Johnson, Design of the Times | Грехи стратегий, восприятие вероятностей, вредный выбор |
| [Designer Notes](https://www.designer-notes.com/) | Soren Johnson, подкаст, 2014– | Интервью с дизайнерами о решениях |
| [Interesting Decisions](https://www.gdcvault.com/play/1015756/) | Sid Meier, GDC 2012 | Игра как серия интересных решений |
| [Sid Meier's Memoir!](https://wwnorton.com/books/9781324005872) | Sid Meier при участии Jennifer Lee Noonan; W. W. Norton, ©2020 | Уроки Civilization и Pirates! |
| ['Into the Breach' Design Postmortem](https://www.gdcvault.com/play/1025772/) | Matthew Davis, GDC 2019 | Полная информация, решения вместо догадок |
| [The secret dice rolls of XCOM: Enemy Within](https://www.pcgamesn.com/secret-dice-rolls-xcom-enemy-within) | Steve Hogarty, интервью с Ananda Gupta (Firaxis); PCGamesN, 15.10.2013 | Скрытый прерыватель серий промахов, зерно ГСЧ против перезагрузок |

## 7. Экшен, платформеры, game feel

### Ключевые принципы

- **Отзывчивость прежде всего.** Минимальная задержка от нажатия до реакции, ясная обратная связь (Swink, Game Feel).
- **Прощение невидимо.** Coyote time, буфер прыжка, ослабленная гравитация на пике, коррекция углов, широкое окно wall-jump. Игрок думает «я сделал», хотя игра незаметно помогла (Thorson, Celeste & Forgiveness).
- **Juice подчёркивает, но не заменяет механику** (Jonasson & Purho, 2012; Nijman, 2013).
- **Ресурсы толкают в бой**: в DOOM (2016) отказались от регенерации здоровья, перезарядки и укрытий; игрок забирает нужное у врагов (Kurt Loudy, Jake Campbell, id Software, GDC 2018).
- **Читаемость атак**: телеграфирование пропорционально урону. Общая теория ощущения управления — в [foundations.md](foundations.md), паттерны — в [mechanics-patterns.md](mechanics-patterns.md#11-управление-и-ощущение).

### Типичные ошибки

- Пиксельно-точные требования без coyote time и буфера ввода.
- Перегруз эффектами, который мешает читать ситуацию.
- Долгий респаун: падает число попыток в минуту.

### Что мерить

Одна строка на попытку участка:

```json
{"player": "p03", "segment": "7B", "died": true, "cause": "spike", "retry_s": 1.1, "felt_unfair": false}
```

- `rate:died@segment=*`, распределение `cause` — где и от чего умирают.
- `num:retry_s` — время до повторной попытки.
- `rate:felt_unfair@segment=*` — жалобы «нажал, а игра не сработала».
- Задержка ввода и окна прощения в кадрах — замеряются в движке отдельно и фиксируются в спецификации. Шаблон коридоров: [levels.json](../assets/targets/levels.json), где `level` — участок.

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Game Feel: A Game Designer's Guide to Virtual Sensation](https://www.routledge.com/Game-Feel-A-Game-Designers-Guide-to-Virtual-Sensation/Swink/p/book/9780123743282) | Steve Swink; CRC, ©2009 | Определение game feel и метрики отзывчивости |
| [Celeste & Forgiveness](https://maddymakesgames.com/articles/celeste_and_forgiveness/index.html) | Maddy Thorson; тред в Twitter 12.03.2020, на Medium 25.04.2022 | Десять механик прощения — чек-лист платформера |
| [Juice It or Lose It](https://www.gdcvault.com/play/1016487/) | Martin Jonasson, Petri Purho; GDC Europe 2012 | Эффекты превращают прототип в «сочный» |
| [The art of screenshake](https://www.youtube.com/watch?v=AJdEqssNZ-U) | Jan Willem Nijman, 2013 | Пошаговое усочнение шутера |
| [Embracing Push Forward Combat in DOOM](https://gdcvault.com/play/1024940/Embracing-Push-Forward-Combat-in) | Kurt Loudy, Jake Campbell; GDC 2018, запись есть на канале GDC | Роли врагов и ресурсы, которые толкают вперёд |
| [Доклады о God of War (2018) на GDC 2019](https://www.gamedeveloper.com/audio/-boy-does-gdc-2019-offer-more-great-i-god-of-war-i-talks-than-you-can-shake-an-axe-at-) | Mihir Sheth (Evolving Combat in 'God of War' for a New Perspective), Jason McDonald (Taking an Axe to 'God of War' Gameplay); список — Game Developer, 28.01.2019 | Бой под близкую камеру от третьего лица |

## 8. Головоломки

### Ключевые принципы

- **Одно озарение на уровень.** Всё, что не ведёт к нему, убирается; ложные пути допустимы, шум — нет (Mark Brown, GMTK).
- **Механика порождает неочевидные следствия.** Дизайнер не изобретает, а открывает свойства системы и показывает их в простейшей форме (Blow & ten Bosch, IndieCade 2011); правила как объекты в Baba Is You (Arvi Teikari, GDC 2020).
- **Последовательность уровней — обучение**: ввести → комбинировать → перевернуть, как в kishōtenketsu. В каждом пазле выбирают одно взаимодействие или цепочку, которую игрок обязан сделать в решении; один пазл итерируют от минут до многих часов (Alan Hazelden о A Monster's Expedition, 2021).
- **Быстрый прототип** сеточных пазлов — PuzzleScript.

### Типичные ошибки

- Перебор вместо озарения; решение через «угадай мысль автора».
- Шум: элементы, которые не участвуют в решении.

### Что мерить

Строка на игрока в уровне:

```json
{"player": "p11", "level": 14, "completed": true, "time_s": 380, "hints": 1, "quit_on_level": false, "intended": false}
```

- `num:time_s@level=*` — скачки сложности по порядку уровней.
- `rate:quit_on_level@level=*`, `num:hints@level=*`.
- `rate:intended@level=*` — решено задуманным способом. Непредусмотренные решения («дыры») ищет автоматический солвер. Шаблон коридоров: [levels.json](../assets/targets/levels.json).

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [What Makes a Good Puzzle?](https://www.youtube.com/watch?v=zsjC6fa_YBg) | Mark Brown, GMTK, 14.03.2018 | Пазл вокруг одного озарения |
| [PuzzleScript](https://www.puzzlescript.net/) | Stephen Lavelle, open source | Прототипы сеточных пазлов, галерея примеров |
| [Designing to Reveal the Nature of the Universe](https://marctenbosch.com/news/?p=181) | Jonathan Blow, Marc ten Bosch; IndieCade, октябрь 2011 | Пазл раскрывает свойства системы; против комбинаторного дизайна |
| [Understanding the rules of Baba Is You](https://gamedeveloper.com/design/video-understanding-the-rules-of-i-baba-is-you-i-) | Arvi Teikari, GDC 2020 (онлайн) | Правила-предложения как данные игры; бесплатная запись на канале GDC |
| [The relaxing, open-world puzzle design of A Monster's Expedition](https://www.gamedeveloper.com/game-platforms/the-relaxing-open-world-puzzle-design-of-i-a-monster-s-expedition-i-) | Joel Couture, интервью с Alan Hazelden, Game Developer, 2021 | Одно обязательное взаимодействие на пазл, итерации, размещение пазлов в открытом мире |

## 9. Мультиплеер и соревновательные игры

### Ключевые принципы

- **Много жизнеспособных стратегий важнее идеального равенства** (Sirlin, Balancing Multiplayer Competitive Games, 2009). Это обязательное чтение для любой игры с соревновательным режимом.
- **Рейтинг с неопределённостью.** Для дуэлей 1×1 подходят Glicko-2 (рейтинг, отклонение RD и волатильность; public domain) или OpenSkill (открытая альтернатива TrueSkill, быстрее, поддерживает несколько команд). Для команд — TrueSkill-класс; TrueSkill 2 учитывает индивидуальные показатели и быстрее калибрует новичков.
- **Поведение формируется дизайном**: обратная связь о наказании, прайминг, прозрачность (Jeffrey Lin, Riot, 2013).
- **Страх рейтинговой игры** (ranked anxiety) снижают защитой от понижения и запасом после повышения ранга: так VALORANT ответил на жалобы, что один плохой день стоит большой потери ранга ([Ask VALORANT](https://playvalorant.com/en-us/news/dev/ask-valorant-dec-24/), Riot, 24.12.2020, патч 2.0).

### Типичные ошибки

- Elo без неопределённости: долгая калибровка, смурфы.
- Матчмейкинг, оптимизирующий только время очереди.
- Наказания без объяснения причины, отсюда рецидивы.

### Что мерить

Одна строка на игрока в рейтинговом матче:

```json
{"match": 55012, "pick": "Zangief", "rating_bucket": "gold", "predicted_win": 0.53, "rating_gap": 41, "queue_s": 38, "went_first": false, "win": true, "loss_streak_before": 3, "churned_7d": false, "reported": false}
```

| Метрика | Ключ или способ | Что показывает |
| --- | --- | --- |
| Качество матча | `num:predicted_win` (медиана около 0.5), `num:rating_gap` | Честность подбора |
| Очередь | `num:queue_s@rating_bucket=*` (p90 для краёв распределения) | Цена качества подбора |
| Отток после поражений | `rate:churned_7d@loss_streak_before=*` | Ranked anxiety и фрустрация |
| Токсичность | `rate:reported`, доля рецидивов; доля матчей с токсичным чатом | Работает ли система наказаний |
| Баланс на верхних рангах | `rate:win@pick=*,rating_bucket=*`; для дуэлей с очерёдностью — `rate:win@went_first=true` в ранкеде; разнообразие `pick` по рангам | Что сильно у новичков и что у топов |

Распределение игроков по рангам — считается отдельно. Шаблоны коридоров: [pvp-duel.json](../assets/targets/pvp-duel.json), [team-pvp.json](../assets/targets/team-pvp.json).

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Playing to Win](https://www.sirlin.net/ptw) | David Sirlin, бесплатно онлайн | Психология соревнования, yomi, что банить |
| [Balancing Multiplayer Competitive Games](https://www.gdcvault.com/play/1570/) | David Sirlin, GDC 2009 | Разнообразие вариантов, справедливость, глубина |
| [The Science Behind Shaping Player Behavior in Online Games](https://www.gdcvault.com/play/1017940/) | Jeffrey Lin, GDC 2013 | Исследования токсичности в League of Legends |
| [TrueSkill](https://www.microsoft.com/en-us/research/project/trueskill-ranking-system/) | Microsoft Research, с 2005 | Байесовский рейтинг для команд, TrueSkill 2 |
| [Glicko / Glicko-2](http://www.glicko.net/glicko.html) | Mark Glickman; документы обновлены в 2016 и 2022 | Рейтинг с RD и волатильностью для 1×1 |
| [OpenSkill](https://arxiv.org/abs/2401.05451) | Vivek Joshy, 2024 | Открытая быстрая альтернатива TrueSkill |
| [League of Legends dev news](https://www.leagueoflegends.com/en-us/news/dev/) | Riot, 2026 | Как объяснять игрокам изменения ранкеда |

## 10. Live service, F2P и этичная монетизация

### Что известно о лутбоксах

- **Связь с проблемным гэмблингом есть, причинность не установлена.** Zendle & Cairns (PLOS ONE, 2018, n=7422): траты на лутбоксы связаны с тяжестью проблемного гэмблинга сильнее, чем прочие микротранзакции. Drummond & Sauer (Nature Human Behaviour, 2018): лутбоксы структурно похожи на азартные игры.
- **Регулирование отстаёт.** Бельгия запретила платные лутбоксы с 2018 года, но запрет плохо соблюдается (Xiao, Collabra: Psychology, 2023). В Нидерландах Kansspelautoriteit оштрафовал EA за паки FIFA Ultimate Team, суд первой инстанции штраф поддержал, но в марте 2022 года Государственный совет его отменил (ECLI:NL:RVS:2022:690). Довод: паки — не самостоятельная азартная игра, около 92% игроков получают их обычной игрой, и регулятор не доказал массовую продажу паков отдельно (разбор Dirkzwager, 01.04.2022). Вывод: этика остаётся на совести дизайнера.
- **ESRB с 13.04.2020 ставит пометку «In-Game Purchases (Includes Random Items)»** на рандомизированные покупки: лутбоксы, гачу и бустеры карт. Любая игра с платными случайными наборами получит эту пометку.

### Ключевые принципы

- **Прозрачность.** Шансы выпадения и цена в реальных деньгах видны. Минимум промежуточных валют.
- **Монетизировать удобство и самовыражение** (косметика, battle pass с честной ценой), а не снятие созданной боли.
- **Предсказуемый сезонный ритм.** Battle pass достижим за разумное время игры.
- **Для игр с коллекцией** (ККИ, гача, герои): детерминированный путь к любому предмету (крафт, обмен), защита от дубликатов, гарантия редкого после N попыток (pity), бесплатный стартовый набор, учёт пометки ESRB.
- **Защита уязвимых**: лимиты трат, никаких ante-механик на реальные деньги.
- **Список того, чего не делать** — каталог Shokrizade (2013): промежуточные валюты, «fun pain», мягкие и жёсткие гейты, отъём награды, ante-игры. Модели источников и стоков — в [systems-balance.md](systems-balance.md), паттерны — в [mechanics-patterns.md](mechanics-patterns.md#13-экономика-и-монетизация).

### Типичные ошибки

- «Fun pain»: создать фрустрацию и продавать её снятие.
- Скрытые шансы и непрозрачная цена через гемы.
- Гача и наборы без гарантии (pity).
- Сила за деньги в соревновательной игре: pay-to-win разрушает ранкед.

### Что мерить

Одна строка на игрока в когорте:

```json
{"player": "u4411", "cohort": "2026-10-w2", "d1": true, "d7": true, "d30": false, "payer": false, "spend_usd": 0, "days_to_competitive": 19, "rank_bucket": "diamond", "refund": false}
```

| Метрика | Ключ или способ | Что показывает |
| --- | --- | --- |
| Удержание | `rate:d1@cohort=*`, `rate:d7@cohort=*`, `rate:d30@cohort=*` | Здоровье живой игры |
| Конверсия | `rate:payer`; ARPDAU — считается отдельно | Доля платящих |
| Концентрация выручки | Доля выручки от верхнего процента плательщиков — считается отдельно | Зависимость от «китов»: красный флаг этики |
| Путь бесплатного игрока | `num:days_to_competitive@payer=false` | Сколько дней игры до конкурентного набора (колоды, героя, снаряжения) бесплатно |
| Pay-to-win | `rate:payer@rank_bucket=*` | Есть ли бесплатные игроки в топ-рангах |
| Сожаление | `rate:refund`, жалобы, время до первой покупки | Покупки, о которых жалеют |

Шаблон коридоров для экономики: [economy-progression.json](../assets/targets/economy-progression.json); удержание и конверсию задают своими коридорами.

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Video game loot boxes are linked to problem gambling](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0206767) | David Zendle, Paul Cairns; PLOS ONE, 2018 | Корреляция трат на лутбоксы и проблемного гэмблинга, n=7422 |
| [Video game loot boxes are psychologically akin to gambling](https://www.nature.com/articles/s41562-018-0360-1) | Aaron Drummond, James D. Sauer; Nature Human Behaviour, 2018 | Структурное сходство с азартными играми (за пейволлом) |
| [Breaking Ban: Belgium's Ineffective Gambling Law Regulation of Video Game Loot Boxes](https://doi.org/10.1525/collabra.57641) | Leon Y. Xiao; Collabra: Psychology, 2023 | Почему запрет не работает |
| [In-Game Purchases (Includes Random Items)](https://www.esrb.org/blog/in-game-purchases-includes-random-items/) | ESRB, 2020 | Маркировка, которая касается бустеров карт |
| [The Top F2P Monetization Tricks](https://www.gamedeveloper.com/business/the-top-f2p-monetization-tricks) | Ramin Shokrizade, 2013 (правки 2017) | Каталог тёмных паттернов |
| [Deconstructor of Fun](https://www.deconstructoroffun.com/) | 2012–2026 | Разборы мобильных F2P и live ops |
| [Designing for Free](http://www.designer-notes.com/?p=115), [The End of Games?](http://www.designer-notes.com/?p=372) | Soren Johnson | Взгляд дизайнера стратегий на F2P |
| Getting Gamers: The Psychology of Video Games and Their Impact | Jamie Madigan; Rowman & Littlefield, 2015 | Мотивация, расписания подкреплений, когнитивные искажения |
| [Research Report on Loot Boxes](https://www.gamingcommission.be/sites/default/files/2021-08/onderzoeksrapport-loot-boxen-Engels-publicatie.pdf) | Peter Naessens, секретариат Gaming Commission (Бельгия), апрель 2018; англ. перевод | Основание бельгийского запрета: Overwatch, Battlefront II, FIFA 18, CS:GO |
| [Loot boxes in FIFA toch géén verboden kansspel](https://www.dirkzwager.nl/kennis/artikelen/loot-boxes-in-fifa-toch-geen-verboden-kansspel-dwangsom-onterecht-opgelegd) | Dirkzwager, 01.04.2022 (на нидерландском) | Разбор решения Государственного совета Нидерландов ECLI:NL:RVS:2022:690 по делу EA |

## 11. Мобильные и казуальные

- **Принципы**: сессия 2–5 минут, игра одной рукой в вертикальной ориентации, прерываемость, онбординг без текста. Жанры при переносе на телефон упрощают ядро и укорачивают партию: короткая гарантированная партия (Marvel Snap), упрощённые системы (Pokémon Pocket), городской F2P-строитель (SimCity BuildIt, [раздел 29](#29-градостроители-менеджмент-и-тайкуны)), idle-петли ([раздел 31](#31-idle-и-incremental)).
- **Ошибки**: перенос длинных партий и сложных систем с ПК, обучение текстом, сессия, которую нельзя прервать.
- **Что мерить**: строка на сессию `{"player", "day", "session_s", "sessions_today", "ftue_step", "finished_tutorial"}` → `num:session_s`, `num:sessions_today`; воронка обучения по `ftue_step` (считается отдельно) и `rate:finished_tutorial`. Шаблоны коридоров: [levels.json](../assets/targets/levels.json) для уровней, [economy-progression.json](../assets/targets/economy-progression.json) для мета-прогрессии.

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Deconstructor of Fun](https://www.deconstructoroffun.com/) | 2012–2026 | Разборы мобильных хитов |
| [Designing MARVEL SNAP](https://gdcvault.com/play/1029024/Designing-MARVEL-SNAP) | Ben Brode, GDC 2023 | Короткая партия под мобильную сессию |
| ['SimCity BuildIt' - What Did I Learn as a Game Designer?](https://gdcvault.com/play/1023103/-SimCity-BuildIt-What-Did) | Petri Ikonen, EA; GDC 2016 | Перенос градостроителя в мобильный F2P |
| Free-to-Play: Making Money From Games You Give Away | Will Luton; New Riders, 2013 | Базовая экономика F2P |

## 12. Кооперативные

- **Принципы**: главная проблема — «альфа-игрок», который играет за всех. Лекарства — скрытая информация, ограничение коммуникации (Hanabi), одновременные решения, личные цели. Игра выступает общим противником с нарастающей угрозой (Pandemic).
- **Ошибки**: полная открытая информация без ограничений общения — один игрок решает за всех; угроза без нарастания.
- **Что мерить**: строка на команду в партии `{"difficulty", "players", "win", "alpha_share"}` → `rate:win@difficulty=*`, `rate:win@players=*`; `num:alpha_share` — доля решений, принятых одним игроком, по наблюдению на плейтесте. Шаблон коридоров: [levels.json](../assets/targets/levels.json), где `level` — уровень сложности или сценарий. Видеоигровой кооператив и party — в [разделе 32](#32-party-и-социальные-игры).

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Cooperation and Engagement: What can board games teach us?](https://www.youtube.com/watch?v=cdTVcFo2EQw) | Matt Leacock, Google Tech Talk, 25.04.2008 | Кооперативные игры и вовлечённость |
| Интервью Matt Leacock в Senet, Issue 10, 2023 | по пересказу с цитатами: [Derek Bruff, 14.04.2023](https://derekbruff.org/2023/04/14/alpha-players-and-in-class-group-work) | Три лекарства от альфа-игрока: скрытая информация, «злые» задачи, задачи с нюансами |
| Building Blocks of Tabletop Game Design | Geoffrey Engelstein, Isaac Shalev; CRC, 1-е изд. 2019, 2-е 2022, актуальное 3-е — июль 2026 ([books.md](books.md)) | Энциклопедия механизмов, включая кооперативные структуры |
| [Hanabi](https://en.wikipedia.org/wiki/Hanabi_(card_game)) | Antoine Bauza, 2010; Spiel des Jahres 2013 | Кооператив с ограниченной коммуникацией: свои карты не видны, подсказки стоят жетонов |

## 13. Настольные

- **Принципы**: правила — интерфейс, и ясность важнее полноты. Мало downtime между ходами, короткий сетап, масштабируемость по числу игроков. Удача расширяет аудиторию: слабый иногда выигрывает, а серия партий или турнир компенсирует случайность (Garfield). Модульность даёт реиграбельность без новых правил (Dominion).
- **Ошибки**: правила, которые нельзя понять без автора за столом; долгий простой в ожидании хода; игра, которая работает только на одном числе игроков.
- **Что мерить**: строка на партию плейтеста `{"players", "blind", "duration_min", "setup_min", "downtime_min", "rules_questions"}` → `num:duration_min@players=*`, `num:setup_min`, `num:downtime_min@players=*`, `num:rules_questions@blind=true`. Слепой плейтест (без автора) — главный тест правил. Методы — в [playtesting-metrics.md](playtesting-metrics.md). Для баланса сторон и фракций — `pick` и шаблон [pvp-duel.json](../assets/targets/pvp-duel.json).

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| Characteristics of Games | Elias, Garfield, Gutschera; MIT Press, 2012 | Теория настольных и карточных игр |
| [The Secret History of Dominion](https://dominionstrategy.com/2013/06/24/the-secret-history-of-dominion/) | Donald X. Vaccarino, 2013; серия статей | Дизайн-дневник настольного хита |
| [Luck vs Skill with Richard Garfield](https://boardgamedesignlab.com/luck-vs-skill-with-richard-garfield/) | Board Game Design Lab | Удача и навык |
| The Kobold Guide to Board Game Design | ред. Mike Selinker; Open Design / Kobold Press, 2011 | Эссе Garfield, Knizia, Kevin Wilson и других |

## 14. Файтинги

### Ключевые принципы

- **Баланс — честные матчапы при асимметрии.** «Слишком сбалансировано — значит скучно» — миф: баланс означает только, что матчапы честные, а персонажи могут и должны различаться. Баланс не ставят выше ощущения, динамики и элегантности: иначе игра «ощущается ужасно» (Sirlin, Game Balance and Yomi, 2014).
- **Эксперты видят дисбаланс раньше статистики.** Sirlin опирается на тир-листы и матчап-чарты от сильных игроков: они находят проблемные матчапы быстрее, чем данные о победах. Статистику побед используют как подтверждение. Правка контр-механики одного персонажа может сломать сразу несколько матчапов (там же).
- **Снежный ком дозируют.** Постоянный slippery slope, когда отставший отстаёт всё сильнее, обычно вреден: исход решается рано. Ограниченный и временный допустим. Perpetual comeback (отставание даёт преимущество) работает в меру, но легко ломается при плохой настройке (Sirlin, Slippery Slope and Perpetual Comeback, 2014).
- **Эксплойты закрывают системой, а не только правкой персонажей.** Skullgirls детектирует бесконечные комбо, и жертва вырывается из петли любой кнопкой; после блока даётся короткое окно защиты от «неблокируемых» связок верх-низ (Mike Zaimont; по Wikipedia со ссылкой на PlayStation Blog, 2011). Игра проектировалась «с расчётом на эксплойтеров» (Destructoid, GDC 2011).
- **Онлайн — через rollback.** Симуляция идёт, не дожидаясь ввода соперника; когда ввод приходит и расходится с предсказанием, игра откатывается и пересчитывает кадры. NetherRealm откатывает и пересчитывает до 8 кадров за 16 мс (Stallone, GDC 2018). Rollback прячет плохое соединение, и онлайн ощущается почти как офлайн (Infil, 2019).

### Типичные ошибки

- Бесконечные комбо и неблокируемые связки без системной защиты.
- Баланс только по статистике побед без матчап-чарта и мнения сильных игроков.
- Delay-based сеткод: задержка ввода растёт с пингом, и тайминги из офлайна не работают онлайн.
- Механики камбэка, которые решают исход сильнее, чем игра до них.

### Что мерить

Одна строка на игрока в раунде или матче:

```json
{"match": 812, "pick": "Ryu", "opp_pick": "Guile", "rating_bucket": "diamond", "win": true, "max_combo_dmg_share": 0.42, "comeback": false, "rollback_frames_p95": 3, "input_delay_frames": 1, "rage_quit": false}
```

| Метрика | Ключ или способ | Что показывает |
| --- | --- | --- |
| Матчап-чарт | `rate:win@pick=*,opp_pick=*`, `spread:win@pick` | Перекошенные матчапы; зеркала исключать |
| Баланс по уровню | `rate:win@pick=*,rating_bucket=*` | Персонаж силён только у новичков или только у топов |
| Урон одной связки | `num:max_combo_dmg_share@pick=*` | Доля здоровья за одну ошибку: «касание = смерть» |
| Камбэк | `rate:comeback` | Снежный ком или избыточный перпетуальный камбэк |
| Качество сети | `num:rollback_frames_p95`, `num:input_delay_frames` | Насколько онлайн отличается от офлайна |
| Фрустрация | `rate:rage_quit@opp_pick=*` | Персонажи, против которых «бесит играть» |

Пороги — рабочие ориентиры проекта, а не цитаты источников. Шаблон коридоров: [pvp-duel.json](../assets/targets/pvp-duel.json). Фреймдата и масштабирование урона — [systems-balance.md](systems-balance.md#45-файтинги-фреймдата-и-масштабирование-урона).

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Playing to Win](https://www.sirlin.net/ptw) | David Sirlin, бесплатно онлайн (книга с 2005) | Психология соревнования, yomi, что банить |
| [Game Balance and Yomi](https://www.sirlin.net/articles/game-balance-and-yomi) | David Sirlin, 20.08.2014 | Баланс при асимметрии, тир-листы и матчап-чарты, каскад правок |
| [Slippery Slope and Perpetual Comeback](https://www.sirlin.net/articles/slippery-slope-and-perpetual-comeback) | David Sirlin, 11.08.2014 | Как дозировать снежный ком и камбэк |
| [Street Fighter HD Remix — статьи](https://www.sirlin.net/articles/sf) | David Sirlin | Дизайн-заметки ребаланса живого файтинга |
| [8 Frames in 16ms: Rollback Networking in Mortal Kombat and Injustice 2](https://gdcvault.com/play/1025021/8-Frames-in-16ms-Rollback) | Michael Stallone, NetherRealm; GDC 2018 | Rollback в коммерческом файтинге: движок, оптимизации, инструменты |
| [Fightin' Words: netcode](https://words.infil.net/w02-netcode-p5.html) | Infil, 16.10.2019 | Понятное объяснение delay-based и rollback сеткода |
| [GDC 11: You need to pay attention to Skullgirls](https://destructoid.com/gdc-11-you-need-to-pay-attention-to-skullgirls) | Hamza Aziz, Destructoid, 03.03.2011 | Дизайн «с расчётом на эксплойтеров», Mike Zaimont |

## 15. MMO и онлайн-миры

### Ключевые принципы

- **Типы игроков в равновесии.** Bartle выделил Achievers, Explorers, Socialisers и Killers. Устойчивый мир — тот, где четыре стиля в равновесии; сильный перекос превращает его во что-то другое: одиночную игру, чат или аркадный шутер (Bartle, Hearts, Clubs, Diamonds, Spades, 1996).
- **Экономике нужны стоки.** Без обязательных регулярных трат богатство копится, начинается «Monty Haul»: баланс ломается, а жизнь игры сокращается (Koster, Laws of Online World Design).
- **Клиент — в руках врага.** Логика и данные на клиенте будут взломаны; авторитет — на сервере (Koster).
- **Насилие неизбежно.** Харассмент и гриферство появятся при любых правилах боя; их проектируют заранее (Koster).
- **Владение и сообщество.** Дома, вещи и роли дают причину остаться; идеальное сообщество — не больше 250 человек, дальше оно делится на подсообщества (Koster).
- **Задуманная экосистема может не пережить игроков.** Ultima Online потеряла задуманную экологию (пример у Sylvester, The Simulation Dream, 2013); история UO — в постмортеме к 20-летию (GDC 2018) и книге Koster «Postmortems» (2018).

### Типичные ошибки

- Источники валюты без стоков: инфляция и обесценивание наград.
- Доверие клиенту: читы и дюп.
- Мир только для одного типа игроков; гриферство не учтено в дизайне.
- Нет владения и мест для сообществ: игроки уходят вместе со своей гильдией.

### Что мерить

Одна строка на игрока за игровой день:

```json
{"player": "u77", "day": 19, "gold_in": 5400, "gold_out": 3100, "guild_size": 41, "griefed": false, "owns_house": true, "churned_30d": false}
```

- Баланс источников и стоков: сумма `gold_in` против `gold_out` по дням и медианный запас валюты — считается отдельно. Устойчивый рост запаса — сигнал инфляции.
- `rate:churned_30d@owns_house=*`, `rate:churned_30d@guild_size_bucket=*` — удерживают ли владение и сообщество.
- `rate:griefed` и доля жалоб — работает ли защита от гриферства.
- Смесь типов игроков — опросом по Bartle, отдельно. Шаблон коридоров: [economy-progression.json](../assets/targets/economy-progression.json).

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Hearts, Clubs, Diamonds, Spades: Players Who Suit MUDs](https://mud.co.uk/richard/hcds.htm) | Richard A. Bartle, 1996 | Четыре типа игроков и равновесие мира |
| Designing Virtual Worlds | Richard Bartle; New Riders, 2003 (переиздание CRC, 2025) | Учебник по дизайну онлайн-миров |
| [The Laws of Online World Design](https://www.raphkoster.com/games/laws-of-online-world-design/the-laws-of-online-world-design/) | Raph Koster, обновлено 31.05.2023 | Экономика, клиент, насилие, владение, размер сообщества |
| [Ultima Online at 20: Classic Game Postmortem](https://www.raphkoster.com/?p=32248) | Raph Koster о докладе GDC 2018 | Уроки первой массовой MMO |
| Postmortems | Raph Koster; Altered Tuning Press, 2018 | Сборник постмортемов и эссе Koster об онлайн-мирах |

## 16. Симуляторы и системные песочницы

### Ключевые принципы

- **Динамика как материал дизайна.** Динамика — правила, по которым структуры меняются во времени. Простые эмерджентные системы дают широкий простор; чувство динамики развивают прототипами (Will Wright, Dynamics for Designers, GDC 2003).
- **Ценно только то, что попало в голову игрока.** «Всё в модели игры, что не копируется в модель игрока, ничего не стоит» (Sylvester, The Simulation Dream, 2013). Сложную симуляцию делают читаемой.
- **Апофения работает на дизайнера.** Игроки видят смысл и намерение в простых событиях; эмоцию можно подразумевать, а не симулировать. Симуляция — соавтор историй вместе с игроком (там же).
- **Story-richness.** Доля взаимодействий, которые игроку интересны, важнее полноты модели (там же).
- **Подделка дешевле полной симуляции.** Caves of Qud генерирует исторические события и подбирает им причины задним числом вместо симуляции истории (Grinblat, Bucklew, FDG 2017; см. [раздел 3](#3-рогалики-и-roguelite)).

### Типичные ошибки

- Глубина, которую игрок не видит и не может объяснить.
- Полная симуляция там, где хватило бы правдоподобной подделки.
- Задуманная экосистема, которую игроки ломают за первые часы (UO и BioShock у Sylvester).

### Что мерить

Строка на событие симуляции, которое игрок заметил, и опрос после сессии:

```json
{"player": "p05", "event": "raid_on_farm", "noticed": true, "explained_cause": true, "found_interesting": true}
```

- `rate:explained_cause@event=*` — может ли игрок объяснить, почему это случилось: проверка модели в голове игрока.
- `rate:found_interesting@event=*` — оценка story-richness по событиям.
- `rate:noticed@event=*` — какие системы работают «впустую». Шаблон коридоров для экономики симуляции: [economy-progression.json](../assets/targets/economy-progression.json); понятность событий задаётся своими коридорами.

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Dynamics for Designers](https://gdcvault.com/play/1019938/Dynamics-for) | Will Wright, GDC 2003; бесплатно в GDC Vault с 2014 | Эмерджентные системы и прототипы динамики |
| [The Simulation Dream](https://www.gamedeveloper.com/design/the-simulation-dream) | Tynan Sylvester, 02.06.2013 | Модель игрока, апофения, story-richness |
| Designing Games: A Guide to Engineering Experiences | Tynan Sylvester; O'Reilly, 2013 | Книга автора RimWorld об инженерии опыта |
| [Procedural Generation in Game Design](https://emshort.blog/2017/06/08/procedural-generation-in-game-design/) | ред. Tanya X. Short, Tarn Adams; CRC, 2017 | Генерация историй и миров, Dwarf Fortress |

## 17. Хоррор

### Ключевые принципы

- **Напряжение важнее испытания.** В Amnesia: The Dark Descent убрали fail-состояния и большую часть сложности, хотя это традиционные инструменты хоррора, и получили более напряжённый и иммерсивный опыт (Thomas Grip, GDC Europe 2011).
- **Четыре слоя.** Геймплей → нарративная цель → нарративный фон → ментальное моделирование. Обычно дизайн застревает на механике и тактике, а нарратив получается побочным продуктом; слою нарратива дают не меньше внимания (Grip, 4-Layers, 2014).
- **Темп через директора.** В Alien: Isolation директор следит за «шкалой угрозы» (menace gauge); если угроза держится на пике слишком долго, чужой уходит в вентиляцию. Директор всегда знает, где игрок, но сам чужой не жульничает и ищет игрока своими сенсорами; по словам разработчиков, он телепортируется только дважды за кампанию, в катсценах (Tommy Thompson, 2017).

### Типичные ошибки

- Постоянная угроза без разрядки: игрок привыкает, и страх уходит.
- Смерть и перезагрузка как основной инструмент: повтор снимает напряжение.
- Монстр, который заметно жульничает: страх сменяется ощущением нечестности.

### Что мерить

Строка на игрока в сегменте уровня:

```json
{"player": "p09", "segment": "medbay", "menace_peak_s": 48, "deaths": 1, "reloads": 1, "fear_1to7": 6, "felt_unfair": false, "quit": false}
```

- `num:fear_1to7@segment=*` — самоотчёт о страхе по сегментам против плана напряжения и разрядки.
- `num:menace_peak_s` — сколько угроза держится на пике; `num:deaths@segment=*`, `num:reloads`.
- `rate:felt_unfair@segment=*`, `rate:quit@segment=*`.
- Физиология (пульс, кожная проводимость) — считается отдельно; поля и пороги здесь — предложение, а не цитаты источников. Шаблон коридоров: [levels.json](../assets/targets/levels.json), где `level` — сегмент.

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Evoking Emotions and Achieving Success by Breaking All the Rules](https://gdcvault.com/play/1014890/Evoking-Emotions-and-Achieving-Success) | Thomas Grip, Frictional Games; GDC Europe 2011, Independent Games Summit | Отказ от fail-состояний ради напряжения |
| [4-Layers, A Narrative Design Approach](https://gamedeveloper.com/design/4-layers-a-narrative-design-approach) | Thomas Grip, 29.04.2014 (из блога Frictional, по докладу GDC 2014) | Связь геймплея и нарратива |
| [The Perfect Organism: The AI of Alien: Isolation](https://www.gamedeveloper.com/design/the-perfect-organism-the-ai-of-alien-isolation) | Tommy Thompson, 31.10.2017 | Директор, шкала угрозы, честный монстр |
| The World of Scary Video Games | Bernard Perron; Bloomsbury Academic, 2018 | Академическая история и теория хоррор-игр |

## 18. VR

### Ключевые принципы

- **Комфорт прежде всего.** Главное правило Owlchemy Labs: «Don't make people sick!» — им подчинены телепорт и камера (Owlchemy, 2019).
- **Меньше векции.** Векция — визуально вызванное ощущение движения, когда тело неподвижно. Скорость аватара близка к реальной: около 1,4 м/с шагом и 2,8 м/с бегом; виньетки затемняют края экрана при движении; ускорения короткие и редкие (Meta, Locomotion comfort and usability, обновлено 17.12.2025).
- **Повороты и перемещения на выбор.** Snap-повороты, телепорт и blink снижают векцию; плавный поворот — только по желанию игрока. Стабильная частота кадров против рывков. Тестировать на разных людях и давать пресеты Recommended, Comfortable и Advanced (Meta, Locomotion best practices).
- **Несколько способов передвижения и проверка точки прибытия.** В Half-Life: Alyx есть Blink, Shift и Continuous. Valve проверяет, что точка прибытия годится для тела игрока и путь к ней проходим; громкость шагов зависит от дистанции перемещения (Greg Coomer, Valve, 2020).
- **Руки и тело как интерфейс.** Взаимодействие руками и движение в комнате интуитивны; зоны телепорта видны заранее; пространство подстраивается под размер комнаты и физические ограничения; персонажи стоят на границе личного пространства, а ближе — по выбору игрока (Owlchemy, Job Simulator → Vacation Simulator).

### Типичные ошибки

- Принудительное плавное перемещение и плавный поворот без альтернатив.
- Камера движется без действия игрока; провалы частоты кадров.
- Один способ передвижения на всех; телепорт в точку, где тело не помещается.
- Интерфейс и персонажи вплотную к лицу игрока.

### Что мерить

Строка на игрока в сессии:

```json
{"player": "p02", "locomotion": "continuous", "turn": "snap", "comfort_preset": "comfortable", "session_min": 22, "ssq_total": 18.7, "quit_early": false}
```

- `num:ssq_total@locomotion=*`, `num:ssq_total@turn=*` — укачивание по Simulator Sickness Questionnaire (Kennedy и др., 1993) до и после сессии.
- `rate:quit_early@locomotion=*`, `num:session_min@comfort_preset=*` — сколько выдерживают в каждом режиме.
- Время кадра и доля пропущенных кадров — замеряются в движке отдельно. Готового шаблона коридоров нет: начните с [levels.json](../assets/targets/levels.json), где `level` — сцена или режим передвижения, и добавьте коридор на `num:ssq_total`.

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Locomotion best practices](https://developers.meta.com/horizon/design/locomotion-best-practices/) | Meta, обновлено 17.12.2025 | Повороты, ускорения, частота кадров, пресеты комфорта |
| [Locomotion comfort and usability](https://developers.meta.com/horizon/design/locomotion-comfort-usability/) | Meta, обновлено 17.12.2025 | Векция, скорости аватара, виньетки |
| [Valve deep dive: Half-Life: Alyx locomotion](https://uploadvr.com/valve-deep-dive-locomotion/) | Ian Hamilton, UploadVR, 06.04.2020, о видео Valve | Blink, Shift, Continuous; проверка точки прибытия; звук шагов |
| [Owlchemy Labs Case Study: Lessons Learned from JOB to VACATION](https://developers.meta.com/horizon/blog/owlchemy-labs-case-study-lessons-learned-from-job-to-vacation/) | Devin Reimer, Andrew Eiche; 23.04.2019 | Руки, зоны телепорта, комфорт, доступность |
| [Simulator Sickness Questionnaire](https://doi.org/10.1207/s15327108ijap0303_3) | Kennedy, Lane, Berbaum, Lilienthal; International Journal of Aviation Psychology, 1993 | Стандартный опросник укачивания для плейтестов |

## 19. Шутеры

FPS и TPS, hero shooter, battle royale, extraction shooter. Ощущение стрельбы и отзывчивость — в [разделе 7](#7-экшен-платформеры-game-feel), рейтинг и матчмейкинг — в [разделе 9](#9-мультиплеер-и-соревновательные-игры). Математика оружия и TTK — [systems-balance.md](systems-balance.md#42-шутеры-оружие-ttk-разброс-и-дальность), герои — [systems-balance.md](systems-balance.md#43-moba-и-hero-shooters-герои-роли-драфт), хитбоксы — [architecture-code.md](architecture-code.md#45-хитбоксы-хёртбоксы-и-обнаружение-попаданий), чеклист ревью — [design-review.md](design-review.md#93-экшен-и-шутеры), метрики — [playtesting-metrics.md](playtesting-metrics.md#542-командный-pvp).

### Ключевые принципы

- **Баланс оружия живёт в мелких числах.** В Halo 3 минимальное время между выстрелами снайперской винтовки поменяли с 0,5 до 0,7 с. Это меньше стотысячной доли данных игры, но заметный сдвиг баланса. Мультиплеер Halo балансирует больше 1000 объектов, у одной винтовки больше 200 полей (Jaime Griesemer, GDC 2010). Правку оформляют гипотезой и проверяют, как любую другую.
- **Сетевой код — часть дизайна.** Peeker's advantage: тот, кто выглядывает из-за угла, видит соперника раньше, потому что держащий позицию ещё не получил его движение. Вклад дают задержка, частота тиков сервера, буферизация и задержка вывода кадра. VALORANT целился в серверы 128 тиков для всех и пинг около 35 мс для 70% игроков (deWet, Straily, Riot, 28.07.2020). Компенсация задержки на сервере «отматывает» мир к моменту выстрела; цена — игрока иногда убивают уже за укрытием (Yahn W. Bernier, Valve, 2001: пример, где игрока с малым пингом поражают уже за ящиком). Архитектура и сетевой код Overwatch — доклад Tim Ford (GDC 2017).
- **Hero shooter: баланс по данным и восприятию.** VALORANT не добивается 50% у каждого агента: равные исходы делают решения шаблонными. Входы баланса — WR матчей, WR раундов атаки и защиты, доля выбора агентов, покупки оружия и регулярные опросы. «Ваше восприятие — ваша правда»: опросы объясняют данные, но не заменяют их. Для агента, карты и стороны есть внутренние границы. Raze с WR около 51% (53,5% без зеркал) не выходила за них, и команда поняла, что сила видна в десятых долях процента, а не в целых (David Cole, 26.06.2020). Каждая правка сохраняет тактический цикл «разведка, план, исполнение».
- **Battle royale: зона и неравная добыча задают темп.** PUBG: до 100 игроков прыгают с самолёта, «синяя стена» сужает зону и сталкивает игроков. Города богаче добычей, но опаснее в начале; глушь беднее, но спокойнее. Значения спавна предметов настраивали всю разработку (Game Developer, 27.04.2017). Fortnite Battle Royale вырос из разворота после успеха PUBG (Paul Gadi, 2017).
- **Extraction: ставка — снаряжение.** Потеря снаряжения при провале создаёт напряжение, но игрок должен хотеть вернуться в рейд даже после потери (разработчики Escape from Duckov, 2025). Читы бьют по такому жанру сильнее всего: The Cycle: Frontier закрыли после всплеска читерства, которое увело игроков (2023). Авторитет — на сервере ([architecture-code.md](architecture-code.md#35-детерминизм-реплеи-сеть-сохранения)).
- **Толкать в бой ресурсами** (DOOM, [раздел 7](#7-экшен-платформеры-game-feel)) и **проблемы free-for-all** ([раздел 32](#32-party-и-социальные-игры): политика и kingmaking) действуют и здесь.

### Типичные ошибки

- Баланс героев по общему WR без учёта зеркал и уровня игроков.
- Доверие клиенту в попаданиях: читы и спор «я же попал».
- Горячие точки высадки, где большинство умирает в первые минуты без шанса на игру.
- Потеря снаряжения без пути восстановиться: отток после серии провалов.

### Что мерить

Одна строка на игрока в матче; `pick` — герой, агент или основной класс:

```json
{"match": 4410, "mode": "br", "side": "attack", "pick": "Raze", "rating_bucket": "gold", "win": false, "placement": 14, "died_first_120s": true, "extracted": false, "gear_value_lost": 3200, "abandon": false, "duration_min": 18}
```

| Метрика | Ключ или способ | Что показывает |
| --- | --- | --- |
| Баланс сторон | `rate:win@side=*` (раунды атаки и защиты — отдельным файлом) | Карта или режим перекошены |
| Баланс героев | `rate:win@pick=*`, `spread:win@pick`, `rate:win@pick=*,rating_bucket=*` | Сила с поправкой на зеркала и уровень |
| Ранние смерти | `rate:died_first_120s`, `num:placement@pick=*` | Горячие точки, лотерея высадки |
| Extraction | `rate:extracted@pick=*`, `num:gear_value_lost` | Цена провала и шанс вынести добычу |
| Длительность и уходы | `num:duration_min@side=attack`, `rate:abandon` | Темп и фрустрация |
| Оружие | Файл «строка на оружие в матче»: `num:ttk_ms@weapon=*`, `rate:win@weapon=*` | Время до убийства, доминирующее оружие |

Доля выбора героев и оружия считается отдельно. Шаблон коридоров: [team-pvp.json](../assets/targets/team-pvp.json).

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Design in Detail: Changing the Time Between Shots for the Sniper Rifle from 0.5 to 0.7 Seconds for Halo 3](https://www.gdcvault.com/play/1012211/) | Jaime Griesemer, GDC 2010 | Как одна микроправка меняет баланс и как её доказывают |
| ['Overwatch' Gameplay Architecture and Netcode](https://www.gdcvault.com/play/1024001/) | Timothy Ford, GDC 2017 | ECS и сетевой код hero shooter |
| [Peeking into VALORANT's Netcode](https://www.riotgames.com/en/news/peeking-valorants-netcode) | Matt deWet, David Straily; Riot, 28.07.2020 | Peeker's advantage и из чего он складывается |
| [How we balance VALORANT](https://playvalorant.com/en-gb/news/dev/how-we-balance-valorant/) | David Cole, Riot, 26.06.2020 | Данные, опросы, границы, урок Raze |
| [Designing the giant battle royale maps of Playerunknown's Battlegrounds](https://www.gamedeveloper.com/design/designing-the-giant-battle-royale-maps-of-i-playerunknown-s-battlegrounds-i-) | Game Developer, 27.04.2017 | Карта, спавн добычи, сужение зоны |
| [Game Design Inspirations: Fortnite's Battle Royale Pivot](https://www.gamedeveloper.com/design/game-design-inspirations-fortnite-s-battle-royale-pivot) | Paul Gadi, 2017 | Разворот жанра внутри живой игры |
| [How Escape from Duckov topped the Steam charts](https://www.gamedeveloper.com/business/behind-escape-from-duckov-s-unlikely-rise-to-the-top-of-the-steam-charts) | Nicole Carpenter, 30.10.2025 | Одиночный extraction: мотивация после потери снаряжения |
| [Yager sunsetting The Cycle: Frontier](https://www.gamedeveloper.com/business/yager-sunsetting-the-cycle-frontier-after-cheaters-cause-irreparable-damage) | Chris Kerr, 28.06.2023 | Как читы убивают extraction-игру |
| [Latency Compensating Methods in Client/Server In-game Protocol Design and Optimization](https://developer.valvesoftware.com/wiki/Latency_Compensating_Methods_in_Client/Server_In-game_Protocol_Design_and_Optimization) | Yahn W. Bernier, Valve, 2001; сайт закрыт проверкой от ботов, сверено по копии web.archive.org от 10.01.2024 | Классика компенсации задержки |

## 20. RPG

CRPG, JRPG, action RPG, системы прокачки и сборок. Кривые опыта и экономика — в [systems-balance.md](systems-balance.md#73-xp-кривые), нарратив и квесты — в [разделе 5](#5-нарративный-дизайн) и [разделе 30](#30-открытые-миры). Статы и разрыв уровней — [systems-balance.md](systems-balance.md#41-rpg-статы-уровни-и-разрыв-уровней), чеклист ревью — [design-review.md](design-review.md#95-rpg).

### Ключевые принципы

- **Несколько путей решения.** Fallout дал открытый мир, моральные дилеммы и квесты, которые решаются разными, часто нестандартными способами (Timothy Cain, GDC 2012). Реактивность дорога: каждую ветку надо написать и протестировать.
- **Разговор — тоже система.** Josh Sawyer на GDC 2012 разобрал, как устроены разговоры в RPG от Fallout до New Vegas, и показал, что подход к их структуре почти не менялся больше десяти лет (запись бесплатна на канале GDC; Game Developer, 2017).
- **Итерация на каждом уровне.** Divinity: Original Sin 2 итерировали от системы боя до организации команды, с разным успехом (Swen Vincke, GDC 2019). Масштабирование команды и ожидания фанатов — в докладе о Baldur's Gate 3 (Vincke, GDC 2022).
- **JRPG: бой как цепочка решений, а не спам атаки.** Persona 5: очередь ходов по ловкости; попадание в слабость даёт ещё ход и сбивает врага; когда сбиты все, доступна общая атака; засада даёт полный ход; у боссов мало слабостей, поэтому их бои долгие (Papucci, 2017). Такие правила наказывают «спам базовой атаки».
- **Action RPG: добыча и сборки как долгая игра.** Path of Exile строит релизы сезонами с предсказуемыми датами и объёмом, переиспользует контент, генерирует уровни против приедания и накладывает несколько осей случайности (Chris Wilson, GDC 2019). История жанра от первой идеи до релиза Diablo — постмортем David Brevik (GDC 2016).
- **Сборка — набор решений, а не одна правильная схема.** Разнообразие сборок среди сильных игроков меряют так же, как разнообразие меты; мёртвые ветки навыков — как «мёртвые» карты ([раздел 2.4](#24-баланс-цифровых-кки)). Положительная обратная связь прокачки — в [mechanics-patterns.md](mechanics-patterns.md#9-мотивация-и-прогрессия).

### Типичные ошибки

- Одна доминирующая сборка; ветки навыков, которые никто не берёт.
- Квест обещает выбор, но решается одним способом.
- Масштабирование уровня врагов съедает ощущение роста.
- Пошаговый бой, где оптимальна одна кнопка.

### Что мерить

Строка на игрока за игровой день или сессию; для боёв — строка на столкновение:

```json
{"player": "p12", "day": 5, "level": 14, "pick": "rogue_poison", "quest": "q_bridge", "solution": "stealth", "deaths": 1, "stuck": false, "minutes_to_next_unlock": 22}
```

- `num:level@day=*` против плановой кривой опыта; `rate:stuck@day=*`; `num:minutes_to_next_unlock` (p90) — паузы без новых возможностей.
- Распределение `solution` по квесту — считается отдельно. Если 95% решают одним способом, другие пути не видны или не нужны.
- `num:deaths@pick=*`, `rate:win@pick=*` по боссам — сила сборок; энтропия сборок у сильных игроков — отдельно.
- JRPG: строка на бой `{"encounter", "turns", "basic_attack_share", "win"}` → `num:turns@encounter=*`, `num:basic_attack_share` — доля боёв, решённых одной кнопкой. Шаблоны коридоров: [economy-progression.json](../assets/targets/economy-progression.json) для прокачки, [roguelike-runs.json](../assets/targets/roguelike-runs.json) для забегов и сезонов action RPG.

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Classic Game Postmortem: Fallout](https://www.gdcvault.com/play/1015843/) | Timothy Cain, GDC 2012 | Открытый мир и квесты с несколькими решениями |
| [Video: New Vegas and the art of designing better conversations in games](https://www.gamedeveloper.com/design/video-i-new-vegas-i-and-the-art-of-designing-better-conversations-in-games) | Josh Sawyer, GDC 2012; Game Developer, 2017 | Структура разговоров в RPG |
| [The Making of 'Divinity: Original Sin 2'](https://www.gdcvault.com/play/1025734/) | Swen Vincke, GDC 2019 | Итерация на всех уровнях: что сработало, что нет |
| [The Many Challenges of Making 'Baldur's Gate 3'](https://gdcvault.com/play/1028044/The-Many-Challenges-of-Making) | Swen Vincke, GDC 2022 | Ожидания фанатов, собственное видение, рост команды |
| [Learn how to make turn-based battles from Persona 5](https://www.gamedeveloper.com/design/learn-how-to-make-turn-based-battles-from-persona-5) | Michele Papucci, 2017 | Слабости, дополнительный ход, общая атака |
| [Classic Game Postmortem: Diablo](https://gdcvault.com/play/1023469/Classic-Game-Postmortem) | David Brevik, GDC 2016 | Как родился action RPG |
| [Designing 'Path of Exile' to Be Played Forever](https://www.gdcvault.com/play/1025784/Designing-Path-of-Exile-to) | Chris Wilson, GDC 2019; запись бесплатна на канале GDC | Сезоны, оси случайности, глубокие системы |
| [The CRPG Book Project](https://crpgbook.wordpress.com/) | ред. Felipe Pepe, бесплатный PDF | История и разборы сотен CRPG |

## 21. MOBA

Командные арены 5×5 с героями, линиями и объектами. Рейтинг, токсичность и уходы — в [разделе 9](#9-мультиплеер-и-соревновательные-игры). Герои, роли и драфт — [systems-balance.md](systems-balance.md#43-moba-и-hero-shooters-герои-роли-драфт), чеклист ревью — [design-review.md](design-review.md#92-командный-pvp), метрики — [playtesting-metrics.md](playtesting-metrics.md#542-командный-pvp).

### Ключевые принципы

- **Ясность прежде глубины.** Силуэт — главное для узнавания героя: у каждого есть уникальная черта, которую не меняют скины; размер и форма подсказывают роль и источник силы. Хитбокс совпадает с видимым эффектом. Жёсткий контроль заметен и слышен, у него ясный замах. Внимание к эффекту пропорционально важности: урон, сила контроля, уворачиваемость, влияние на игру. Скины не дают преимущества и не мешают (Riot, Clarity in League, 12.03.2021).
- **Камбэк заслуженный.** Проигрывающая команда — та, чей шанс на победу 40% и ниже. Камбэк должен следовать из ошибок лидера и не ощущаться подарком; лидерство — преимущество, а не победа. Слишком сильные механики обесценивают ранний перевес, слишком слабые не дают камбэков. Пример — награды за голову: забрать награду с героя 8/0 значит убить намного более сильного соперника (Riot Phroxzon, 25.02.2022).
- **Баланс по уровням мастерства.** Champion Balance Framework (Riot, 2019) задаёт прозрачные критерии нерфа и бафа по уровням мастерства игроков ([mechanics-patterns.md](mechanics-patterns.md#2-каталоги-паттернов)). Решения опираются на телеметрию и массовый опрос о чемпионах (Nathan Blau, GDC 2019).
- **Производство героя — процесс.** Как Riot создаёт новых чемпионов от идеи до релиза — доклад Jeremy Lee (GDC 2017, пересказ Game Developer 2019).
- **Длительность и снежный ком** — общие паттерны в [mechanics-patterns.md](mechanics-patterns.md#6-темп-и-длительность).

### Типичные ошибки

- Герой, чьи умения нельзя прочитать в массовой драке.
- Механики камбэка, после которых ранняя игра ничего не значит.
- Герой силён только у профессионалов или только у новичков, а баланс смотрят по общему WR.
- Уходы и AFK без защиты оставшихся четверых.

### Что мерить

Строка на игрока в матче:

```json
{"match": 9120, "side": "blue", "pick": "Ahri", "opp_pick": "Zed", "rating_bucket": "plat", "win": true, "gold_diff_15": -2300, "comeback": true, "abandon": false, "duration_min": 31}
```

- `rate:win@side=*` — синяя и красная стороны; `num:duration_min@side=blue` — одна строка на матч.
- `rate:win@pick=*,rating_bucket=*` — сила героя по уровням; `rate:win@pick=*,opp_pick=*` для соперников по линии; `spread:win@pick`.
- `rate:comeback` (победа при `gold_diff_15` ниже порога); `rate:win@gold_diff_15_bucket=*` — насколько ранний перевес решает исход.
- `rate:abandon`; доля выбора и банов — отдельно. Шаблон коридоров: [team-pvp.json](../assets/targets/team-pvp.json).

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Clarity in League](https://www.leagueoflegends.com/en-gb/news/dev/clarity-in-league/) | Riot, 12.03.2021 | Силуэт, хитбоксы, иерархия эффектов |
| [Quick Gameplay Thoughts 2/25: Comeback Mechanics](https://www.leagueoflegends.com/en-us/news/dev/quick-gameplay-thoughts-2-25-comeback-mechanics/) | Riot Phroxzon, 25.02.2022 | Заслуженный камбэк, награды за голову |
| [Champion Balance Framework](https://nexus.leagueoflegends.com/en-au/2019/05/dev-champion-balance-framework/) | Riot, 2019 | Критерии нерфа и бафа по уровням мастерства |
| [Data Informed Decisions with the Champions of 'League of Legends'](https://www.gdcvault.com/play/1026252/Data-Informed-Decisions-with-the/) | Nathan Blau, GDC 2019 | Телеметрия и опрос о 140+ чемпионах |
| [Video: How Riot creates new League of Legends champions](https://www.gamedeveloper.com/design/video-how-riot-creates-new-i-league-of-legends-i-champions) | Jeremy Lee, GDC 2017; Game Developer, 2019 | Производственный процесс героя |
| [The Science Behind Shaping Player Behavior in Online Games](https://www.gdcvault.com/play/1017940/) | Jeffrey Lin, GDC 2013 | Токсичность в командной игре |

## 22. Метроидвании

Связанный мир, который открывается по мере получения способностей. Платформенная механика — в [разделе 7](#7-экшен-платформеры-game-feel), процедурные варианты — в procedural-generation.md. Кривые сложности — [systems-balance.md](systems-balance.md#48-экшен-и-платформеры-кривые-сложности-и-окна-реакции), чеклист ревью — [design-review.md](design-review.md#94-платформеры), метрики — [playtesting-metrics.md](playtesting-metrics.md#544-уровни-и-кампании).

### Ключевые принципы

- **Способность — новый глагол, а не ключ.** Улучшение меняет то, как герой движется и сражается, а не открывает одну дверь. Игра хороша «с первой минуты», хотя герой слаб (Josh Bycer, 2017).
- **Связанный мир и меньше пустого бэктрекинга.** Несколько путей, препятствия, которые меняются с новыми способностями, секреты за возвратом и быстрые перемещения в большом мире (Bycer). Blasphemous не хотел заставлять возвращаться тех, кто пропускает исследование, и добавил шорткаты, открываемые рычагами (Yarwood, 2019).
- **Снизить когнитивную нагрузку карты.** Prince of Persia: The Lost Crown дал «осколки памяти» — снимки экрана, прикреплённые к карте как заметки. Доступность планировали за три года до релиза; среди прошедших игру 44% играли на стандартной сложности, по 19% — на лёгкой и настраиваемой, 15% — на трудной, 3% — на очень трудной (Rémi Boutin, GDC 2025, слайды).
- **Ручное и процедурное вместе.** Dead Cells держит фиксированную карту острова и связи между уровнями, а комнаты собирает из ручных шаблонов по графу биома: длина, число особых комнат, запутанность. Темп — по образцу AI Director из Left 4 Dead (Sébastien Benard, 2017).
- **Метод жанра от его автора** — Koji Igarashi о Castlevania: Symphony of the Night и последующих играх (GDC 2014).

### Типичные ошибки

- Способность используется в одном месте и больше нигде.
- Обязательный бэктрекинг через пустые зачищенные зоны.
- Нет карты или пометок: игрок забывает, где видел препятствие.
- Обход последовательности ломает прогрессию или сюжет.

### Что мерить

Строка на игрока в зоне за посещение:

```json
{"player": "p05", "level": "sewers", "abilities": "dash+walljump", "time_s": 410, "lost": true, "backtrack_s": 140, "map_opened": 12, "deaths": 2, "quit_on_level": false}
```

- `rate:lost@level=*`, `num:backtrack_s@level=*`, `num:map_opened@level=*` — ориентация и пустые возвраты.
- `num:time_s@level=*` против плана; `rate:quit_on_level@level=*`.
- Порядок получения способностей по игрокам — считается отдельно: показывает обходы последовательности. Тепловые карты — отдельно. Шаблон коридоров: [levels.json](../assets/targets/levels.json), где `level` — зона.

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [There and Back Again: Koji Igarashi's Metroidvania Tale](https://www.gdcvault.com/play/1020822/There-and-Back-Again-Koji) | Koji Igarashi, GDC 2014 | Метод жанра от Symphony of the Night |
| [The Foundation of Metroidvania Design](https://www.gamedeveloper.com/design/the-foundation-of-metroidvania-design) | Josh Bycer, 2017 | Основа, дизайн улучшений, окружение |
| [How Blasphemous' level design iterates on classic Metroidvanias](https://www.gamedeveloper.com/design/how-i-blasphemous-i-level-design-iterates-on-classic-metroidvanias) | Jack Yarwood, 2019 | Шорткаты вместо принудительного бэктрекинга |
| [Building the Level Design of a procedurally generated Metroidvania](https://www.gamedeveloper.com/design/building-the-level-design-of-a-procedurally-generated-metroidvania-a-hybrid-approach-) | Sébastien Benard, 2017 | Гибрид ручных комнат и процедурной сборки |
| [Making a Modern Metroidvania Both Accessible and Challenging (слайды)](https://media.gdcvault.com/gdc2025/Slides/BOUTIN_Remi_Prince+of+Persia.pdf) | Rémi Boutin, Ubisoft; GDC 2025 | Доступность без потери вызова, заметки на карте |

## 23. Стелс

Игры, где главное — не быть замеченным: от Thief до 2D-стелса. Директор угрозы и монстр-преследователь — в [разделе 17](#17-хоррор), ИИ в коде — в [architecture-code.md](architecture-code.md#37-игровой-ии). Метрики уровней — [playtesting-metrics.md](playtesting-metrics.md#544-уровни-и-кампании).

### Ключевые принципы

- **Серая зона между «заметили» и «нет».** Thief хранил осведомлённость ИИ дискретными состояниями. Видимость объекта — число от 0 до 1 из освещения, движения и открытости. Звуки идут по геометрии уровня. Рост тревоги проходит через фильтр времени (реакция и прощение), спад — постепенный. Простые дискретные входы и выходы позволяют игроку предсказывать ИИ (Tom Leonard, 2003).
- **Прозрачность системы.** Mark of the Ninja: свет и тьма бинарны и видны по герою; у охранника три уровня тревоги и ясная причина перехода; управление не спорит с намерением игрока; чекпоинт между значимыми столкновениями; зона столкновения — около экрана плюс 0,5–0,75 экрана в каждую сторону, потому что большое 2D-пространство трудно держать в голове (Nels Anderson, 2012). Исходная идея — привлекательность стелса в выборе игрока, а не в тропах жанра (Anderson, GDC 2013).
- **Восприятие правдоподобное, а не умное.** Splinter Cell: Blacklist: зона обзора похожа на гроб, а не на конус; обнаружение накапливается; видимость считают лучами к восьми костям героя; звук идёт по пути через проходы; недавно изменённые двери и свет подозрительны; поднятая тревога не падает сама в покой; на низкой сложности больше слепых зон (Tommy Thompson о докладе Martin Walsh, GDC 2014).
- **Обучать стелсу ситуациями.** Как Splinter Cell: Blacklist учил новичков шпионским механикам — доклад Laurent Malville (GDC 2014).

### Типичные ошибки

- Мгновенное обнаружение без шкалы и предупреждения.
- Непрозрачный ИИ: игрок не понимает, почему его заметили.
- Наказание за провал — долгая перезагрузка; игрок сохраняется каждые десять секунд.
- Один стиль прохождения явно выгоднее остальных.

### Что мерить

Строка на игрока в столкновении:

```json
{"player": "p03", "level": "e3_courtyard", "detected": true, "detect_cause": "sound", "alerts": 2, "reloads": 1, "time_s": 95, "approach": "ghost", "felt_unfair": false}
```

- `rate:detected@level=*` и распределение `detect_cause` — где и от чего замечают.
- `num:reloads@level=*` — перезагрузки вместо игры; `rate:felt_unfair@level=*`.
- Распределение `approach` (незаметно, без убийств, бой) — считается отдельно; показывает, есть ли выбор. Шаблон коридоров: [levels.json](../assets/targets/levels.json), где `level` — столкновение или уровень.

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Building an AI Sensory System: Examining The Design of Thief: The Dark Project](https://www.gamedeveloper.com/programming/building-an-ai-sensory-system-examining-the-design-of-i-thief-the-dark-project-i-) | Tom Leonard, 2003 | Состояния осведомлённости, видимость, звук |
| [Mark of the Ninja's five stealth design rules](https://www.gamedeveloper.com/design/-i-mark-of-the-ninja-i-s-five-stealth-design-rules) | Mathew Kumar о докладе Nels Anderson, 2012 | Пять «ересей» прозрачного стелса |
| [Of Choice and Breaking New Ground: Designing Mark of the Ninja](https://www.gdcvault.com/play/1018948/Of-Choice-and-Breaking-New) | Nels Anderson, GDC 2013 | Стелс от выбора игрока, а не от тропов |
| [Bringing Balance to Stealth AI in Splinter Cell: Blacklist](https://www.gamedeveloper.com/design/bringing-balance-to-stealth-ai-in-splinter-cell-blacklist) | Tommy Thompson, 2020, о докладе Martin Walsh GDC 2014 | Модель восприятия и баланс по сложности |
| [Super Spy Crash Course: Teaching Players in Splinter Cell: Blacklist](https://gdcvault.com/play/1020450/Super-Spy-Crash-Course-Teaching) | Laurent Malville, GDC 2014 | Обучение стелс-механикам |

## 24. Ритм-игры

Игры, где ввод оценивается по попаданию в такт. Задержка ввода и ощущение — в [разделе 7](#7-экшен-платформеры-game-feel), доступность — в [design-review.md](design-review.md#6-доступность). Окна реакции — [systems-balance.md](systems-balance.md#48-экшен-и-платформеры-кривые-сложности-и-окна-реакции).

### Ключевые принципы

- **Часы — по звуку, а не по кадрам.** Позицию в песне считают от аудиочасов, а не от времени кадра: кадровое время обновляется раз в кадр и уходит от звука. Ноты двигают интерполяцией по позиции в долях такта, а не накоплением шагов кадра, потому что доля может попасть между кадрами (Yu Chao, 2017).
- **Окно попадания — параметр сложности в данных.** В osu! полуширина окна на «300» равна 80 − 6×OD мс, на «100» — 140 − 8×OD, на «50» — 200 − 10×OD, где OD — сложность карты (osu! wiki). Окна задают числами и меряют на плейтесте, а не подбирают «на ощупь».
- **Калибровка задержки обязательна.** Задержка вывода звука и картинки у устройств разная; без калибровки точный игрок получает «мимо». Это общая практика жанра; первоисточник с числами не найден.
- **Простота и сильная арт-дирекция.** Thumper сделали два человека за семь лет, опираясь на арт-дирекцию, постоянные эксперименты и простоту; отдельный рассказ — перенос в VR (Marc Flury, GDC 2017). Beat Saber создала команда из трёх человек (Jaroslav Beck, XRDC 2018).

### Типичные ошибки

- Тайминг от кадровых часов: рассинхрон растёт к концу трека.
- Нет калибровки или она спрятана в меню.
- Окна попадания уже, чем позволяет аудитория и устройство.
- Скачки плотности нот внутри одного уровня сложности.

### Что мерить

Строка на игрока в попытке чарта:

```json
{"player": "p08", "level": "song07_hard", "calibrated": true, "offset_ms": -18, "hit_err_ms_p90": 41, "accuracy": 0.91, "completed": true, "attempts": 3, "quit_on_level": false}
```

- `rate:completed@level=*`, `num:attempts@level=*`, `num:accuracy@level=*` — кривая сложности чартов.
- `num:hit_err_ms_p90@calibrated=*` — помогает ли калибровка; распределение `offset_ms` — разброс задержки устройств.
- `rate:quit_on_level@level=*` — где бросают. Шаблон коридоров: [levels.json](../assets/targets/levels.json), где `level` — чарт.

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Music Syncing in Rhythm Games](https://www.gamedeveloper.com/programming/music-syncing-in-rhythm-games) | Yu Chao, 2017 | Аудиочасы и интерполяция по долям |
| [Coding to the Beat - Under the Hood of a Rhythm Game in Unity](https://www.gamedeveloper.com/audio/coding-to-the-beat---under-the-hood-of-a-rhythm-game-in-unity) | Graham Tattersall, 2019 | Устройство ритм-игры в коде |
| [Beatmap / Overall difficulty](https://osu.ppy.sh/wiki/en/Beatmap/Overall_difficulty) | osu! wiki, живая | Формулы окон попадания |
| [Seven Years in Alpha: 'Thumper' Postmortem](https://gdcvault.com/play/1024291/Seven-Years-in-Alpha-Thumper) | Marc Flury, GDC 2017 | Простота, эксперименты, перенос в VR |
| [The Story of 'Beat Saber'](https://gdcvault.com/play/1025605/The-Story-of-39-Beat) | Jaroslav Beck, XRDC 2018 | Ритм-игра в VR от команды из трёх |
| [Rhythm Games: Simplicity and Mass Appeal](https://www.gamedeveloper.com/game-platforms/gcg-feature-rhythm-games-simplicity-and-mass-appeal-) | Jason Dobson, 2007 | Почему простой ввод даёт массовую аудиторию |

## 25. Приключения, point-and-click и визуальные новеллы

Квесты с предметами и головоломками, интерактивная литература и визуальные новеллы. Структуры ветвления, ink и Yarn Spinner — в [разделе 5](#5-нарративный-дизайн), устройство головоломок — в [разделе 8](#8-головоломки). Оценка сложности головоломок — [systems-balance.md](systems-balance.md#49-головоломки-оценка-сложности), квесты и диалоги в коде — [architecture-code.md](architecture-code.md#410-квесты-и-диалоги).

### Ключевые принципы

- **Правила Gilbert (1989).** Конечная цель ясна; первые подцели очевидны; игру можно пройти без смертей и сохранений, если быть внимательным; нет «обратных» головоломок, где решение встречается раньше задачи; нельзя навсегда упустить нужный предмет; каждая головоломка двигает историю; драматический тайминг вместо часов реального времени; решения логичны; намерение игрока вознаграждается; игроку дают выбор, а не одну цепочку (Ron Gilbert, Why Adventure Games Suck).
- **Граф зависимостей головоломок.** Это не блок-схема, а граф «что от чего зависит». Решённая головоломка открывает две-три новых, потом они сходятся к одному решению: расширение и сжатие. Акт кончается «бутылочным горлом», которое даёт чувство завершения. Gilbert строит граф от конца назад (Puzzle Dependency Charts, 10.08.2014).
- **Выбор без «хорошего» ответа.** The Walking Dead: сюжетный «хребет» написан вручную, внутри него игрок решает ключевые моменты; это сильнее шкалы добра и зла; мелкие выборы бывают интереснее больших предательств; варианты, которые не дают сильной сцены, вырезают (Kevin Bruner, постмортем 2013).
- **Игра сама рассказывает историю.** 80 Days выросла из истории с выборами на карте мира в настольную игру, которая сама себя рассказывает: экономика, арт и мультиплеер двигают сюжет, а текст гибок, но последователен (Jon Ingold, GDC China 2014). Как делать выборы, которые важны, и как держать темп текста — Ingold, GDC 2015.
- **Детектив как система дедукции.** Return of the Obra Dinn: история как набор отдельных катастроф, в каждой гибнет несколько героев; книгу-журнал добавили поздно, чтобы удержать сложность (Bryant Francis, 2018).

### Типичные ошибки

- «Лунная логика»: решение понятно только автору; перебор «всё на всё».
- Тупики, из которых нельзя выйти без перезагрузки.
- Поиск пикселя вместо поиска идеи.
- Выборы без видимых последствий.
- Экспоненциальное ветвление ([раздел 5](#5-нарративный-дизайн)).

### Что мерить

Строка на игрока в головоломке или сцене:

```json
{"player": "p14", "level": "ch2_lighthouse_key", "completed": true, "time_s": 540, "hints": 2, "wrong_combos": 17, "attempts": 1, "quit_on_level": false}
```

- `num:time_s@level=*`, `num:hints@level=*` — скачки сложности.
- `num:wrong_combos@level=*` — много неверных сочетаний предметов значит перебор вместо озарения.
- `rate:quit_on_level@level=*` — где бросают; выборы — как в [разделе 5](#5-нарративный-дизайн). Шаблон коридоров: [levels.json](../assets/targets/levels.json), где `level` — головоломка или сцена.

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Why Adventure Games Suck](https://grumpygamer.com/why_adventure_games_suck/) | Ron Gilbert, 1989 | Двенадцать правил честного квеста |
| [Puzzle Dependency Charts](https://grumpygamer.com/puzzle_dependency_charts/) | Ron Gilbert, 10.08.2014 | Граф головоломок, ширина и «горлышки» |
| [80 DAYS Post-mortem: Letting the Game Tell the Story](https://gdcvault.com/play/1021666/80-DAYS-Post-mortem-Letting) | Jon Ingold, GDC China 2014 | Системы, которые двигают сюжет |
| [Adventures in Text: Innovating in Interactive Fiction](https://gdcvault.com/play/1021774/Adventures-in-Text-Innovating-in) | Jon Ingold, GDC 2015 | Выборы, которые важны; темп текста |
| [The Walking Dead and the art of providing no 'good' choice](https://www.gamedeveloper.com/design/-i-the-walking-dead-i-and-the-art-of-providing-no-good-choice) | Game Developer, 08.03.2013, о постмортеме Kevin Bruner | Выбор без шкалы морали |
| [For Lucas Pope, Return of the Obra Dinn was a bunch of appealing design problems](https://www.gamedeveloper.com/design/for-lucas-pope-i-return-of-the-obra-dinn-i-was-a-bunch-of-appealing-design-problems) | Bryant Francis, 2018 | Дедукция как механика |

## 26. Гонки

Аркадные и симуляционные гонки, карт-рейсинг. Догоняющие механики — в [mechanics-patterns.md](mechanics-patterns.md#3-мини-каталог-паттернов), петли обратной связи — в [systems-balance.md](systems-balance.md#61-положительные-и-отрицательные-петли). Rubber banding в числах — [systems-balance.md](systems-balance.md#46-гонки-rubber-banding-и-catch-up), чеклист ревью — [design-review.md](design-review.md#910-гонки-и-спорт), метрики — [playtesting-metrics.md](playtesting-metrics.md#547-гонки-и-спорт).

### Ключевые принципы

- **Сценарий гонки вместо голой «резинки».** В Pure группы ИИ держат целевые точки относительно игрока, и цели сдвигаются по ходу гонки: задняя группа — от «вровень» до 500 м позади, средняя — от 250 м впереди до 250 м позади, передняя — от 500 м впереди до «вровень», ближняя всё время рядом. Сценарий действует первые 80% гонки, потом бонусы ИИ уходят в ноль, чтобы игрок мог отыграть ошибку. Классическая «резинка» через скорость заметна и кажется нечестной (Eduardo Jimenez, 2009).
- **Подстройка машин, а не водителей.** Drivatar в Forza учится на скорости, угле поворота и стабильности игрока по участкам; старые данные весят меньше; перемотка отменяет обучение на участке. Если игрок далеко впереди, машины соперников чуть тяжелее и слабее; если позади — чуть лучше реальных, в пределах, которые не ломают физику (Tommy Thompson, 2021).
- **Догоняющие предметы — сознательная цена.** Сильные предметы для отстающих (Mario Kart) держат гонку плотной, но эксперт иногда проигрывает новичку. Решение записывают в опоры.
- **Одиночество убивает гонку.** Вся логика Pure построена против гонки, где игрок едет один (Jimenez).

### Типичные ошибки

- Видимая «резинка»: соперник едет сверхчеловечески быстро или стоит на месте.
- Одна ошибка на последнем круге стоит всей гонки.
- Игрок большую часть гонки едет без соперников рядом.
- Одна машина или настройка лучше остальных на всех трассах.

### Что мерить

Строка на игрока в гонке; `pick` — машина или карт:

```json
{"player": "p02", "level": "t04_canyon", "pick": "gt3_a", "assist": "on", "position": 3, "win": false, "completed": true, "lead_changes": 4, "alone_share": 0.12, "gap_s_at_80pct": 1.8, "felt_unfair": false, "attempts": 2}
```

- `num:alone_share@level=*` — доля времени без соперников рядом; `num:lead_changes` — драма гонки.
- `num:gap_s_at_80pct` — разрыв до лидера на 80% дистанции; `rate:felt_unfair@level=*` — заметна ли подстройка.
- `num:position@assist=*` — помогают ли ассисты; `rate:win@pick=*`, `spread:win@pick` — баланс машин в онлайне. Шаблоны коридоров: [levels.json](../assets/targets/levels.json) (`level` — трасса), [pvp-duel.json](../assets/targets/pvp-duel.json) для баланса машин.

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [The Pure Advantage: Advanced Racing Game AI](https://www.gamedeveloper.com/design/the-pure-advantage-advanced-racing-game-ai) | Eduardo Jimenez, 2009 | Сценарий гонки и динамическая подстройка |
| [How Forza's Drivatar Actually Works](https://www.gamedeveloper.com/design/how-forza-s-drivatar-actually-works) | Tommy Thompson, 2021 | Обучение на игроке и подстройка машин |
| [The value of 'Rubber Banding' (An engagement driver)](https://www.gamedeveloper.com/design/the-value-of-rubber-banding-an-engagement-driver-) | Nikhil Birla, 2015 | Аргументы за «резинку» как удержание |
| [Blue shell](https://en.wikipedia.org/wiki/Blue_shell) | Wikipedia | Догоняющий предмет и спор вокруг него |

## 27. Спортивные

Симуляторы командных видов спорта, аркадный спорт, спортивные менеджеры. Командный матчмейкинг — в [разделе 9](#9-мультиплеер-и-соревновательные-игры). Рейтинги игроков и команд — [systems-balance.md](systems-balance.md#47-спорт-симы-рейтинги-игроков-и-команд), чеклист ревью — [design-review.md](design-review.md#910-гонки-и-спорт), метрики — [playtesting-metrics.md](playtesting-metrics.md#547-гонки-и-спорт).

### Ключевые принципы

- **Сделать результат важным.** Главная задача — чтобы игроку был не безразличен исход в мире без настоящих ставок. Bennett Foddy разбирает пять способов, которыми реальный спорт решает ту же задачу (GDC 2013).
- **Физика — источник удовольствия.** Почему Rocket League приятно играть людям любого возраста: устройство физики машин и мяча (Jared Cone, GDC 2018).
- **Видеоигра не обязана копировать спорт.** Компьютерная точность правил даёт то, чего нет в аналоговом спорте (Tim Rogers о Videoball, GDC 2016).
- **Менеджер: воображение вместо картинки.** Football Manager долго показывал матч текстовым комментарием в духе радиорепортажа, чтобы игрок сам представлял игру (Bryant Francis, 2016). Исход матч-движка должен отражать решения игрока, иначе менеджер превращается в лотерею.
- **Реализм против игры.** Лицензия обещает узнаваемость, игра — ясные решения. Где они расходятся, решение фиксируют в опорах ([documentation.md](documentation.md#4-опоры-дизайна)).

### Типичные ошибки

- Одна тактика или тип гола работает всегда.
- Реализм, который делает матч скучным или нечитаемым.
- Исход симуляции менеджера слабо зависит от решений игрока.
- Преимущество домашней стороны или старта, не заданное дизайном.

### Что мерить

Строка на игрока или команду в матче; `pick` — команда, `side` — дома или в гостях:

```json
{"match": 300, "side": "home", "pick": "team_a", "opp_pick": "team_b", "rating_bucket": "silver", "win": true, "draw": false, "goal_type": "cross_header", "comeback": false, "abandon": false, "duration_min": 12}
```

- `rate:win@side=*` — преимущество стороны; `rate:win@pick=*,opp_pick=*` — сила команд против рейтинга.
- `rate:draw`, `rate:comeback`, `rate:abandon`.
- Распределение `goal_type` — считается отдельно: доминирующая тактика. Для менеджера — прогон матч-движка ботами: `rate:win@tactic=*` при равных составах. Шаблон коридоров: [team-pvp.json](../assets/targets/team-pvp.json); для дуэлей 1×1 — [pvp-duel.json](../assets/targets/pvp-duel.json).

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Making it Matter: Lessons from Real Sports](https://www.gdcvault.com/play/1017925/Making-it-Matter-Lessons-from) | Bennett Foddy, GDC 2013 | Как сделать исход важным для игрока |
| [It IS Rocket Science! The Physics of 'Rocket League' Detailed](https://www.gdcvault.com/play/1024972/) | Jared Cone, GDC 2018 | Физика как основа ощущения |
| [Video: Videoball and video games' superiority over sports](https://www.gamedeveloper.com/design/video-i-videoball-i-and-video-games-superiority-over-sports) | Tim Rogers, GDC 2016; Game Developer, 2016 | Спортивная игра без копирования спорта |
| [The ingredient that turned Football Manager into a massive hit](https://www.gamedeveloper.com/design/the-ingredient-that-turned-i-football-manager-i-into-a-massive-hit) | Bryant Francis, 2016 | Текстовый матч и воображение игрока |

## 28. Выживание, крафт и песочницы

Survival, крафт, строительство, песочницы без жёсткой цели. Часы давления — в [разделе 3](#3-рогалики-и-roguelite), экономика — в [systems-balance.md](systems-balance.md#71-источники-стоки-конвертеры). Метрики прогрессии — [playtesting-metrics.md](playtesting-metrics.md#545-экономика-и-прогрессия).

### Ключевые принципы

- **Выживание — управление временем.** Seth Rosen (Ironwood Studios, раньше Klei) на GDC 2026: время — единственный настоящий ресурс; сбор, крафт и шкалы — «тарелки», которые игрок крутит; эмоция жанра — решение задач под давлением. Каждая система должна работать на петлю давления, иначе она превращается в рутину; главная цель должна быть ясна (Carli Velocci, 2026).
- **Опоры и эмоция с прототипа.** Subnautica держалась опор дизайна, ловила эмоцию в ранних прототипах, использовала страхи игроков (глубина, темнота), загадочные подсказки и радиосигналы, которые дают песочнице структуру без поводка (Charlie Cleveland, GDC 2019). Открытая разработка в раннем доступе — отдельный доклад (Jonas Boetel, GDC 2019).
- **Часы давления.** Голод и аналоги не дают безопасно фармить (Josh Ge, Food Clocks, 2014; [раздел 3](#3-рогалики-и-roguelite)).
- **Песочница без давления — другой жанр.** Rosen отделяет классическое выживание от песочниц вроде Minecraft, где давление и опасность сняты. Решите, какой из двух опыт вы делаете.

### Типичные ошибки

- Шкалы, которые тикают, но не дают решений.
- Системы ради рутины, не связанные с давлением времени.
- Ранний сбор ресурсов скучен и долог.
- Нет цели после постройки базы.

### Что мерить

Строка на игрока за игровой день:

```json
{"player": "p21", "day": 3, "deaths": 1, "death_cause": "starvation", "idle_share": 0.18, "crafted_new": 4, "stuck": false, "minutes_to_next_unlock": 14}
```

- `rate:stuck@day=*`, `num:minutes_to_next_unlock` (p90) — паузы без прогресса.
- `num:idle_share@day=*` — доля времени без давления и решений; растёт к поздней игре — значит, жанр «кончился».
- Распределение `death_cause` — считается отдельно: какие «тарелки» роняют чаще; `num:deaths@day=*`. Шаблон коридоров: [economy-progression.json](../assets/targets/economy-progression.json).

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| ['Pacific Drive' Under the Hood: Survival Fundamentals, Systems Design, and Speeding Past Tropes](https://gdcvault.com/play/1035732/-Pacific-Drive-Under-the) | Seth Rosen, GDC 2026 | Основы выживания и таксономия опыта |
| [Resource management? Survival games are about time management.](https://www.gamedeveloper.com/design/resource-management-survival-games-are-about-time-management-) | Carli Velocci, 17.06.2026 | Конспект доклада Rosen |
| [The Design of 'Subnautica'](https://gdcvault.com/play/1025745/The-Design-of-Subnautica) | Charlie Cleveland, GDC 2019 | Опоры, крафт, страхи, структура песочницы |
| ['Subnautica' Postmortem](https://www.gdcvault.com/play/1025691/-Subnautica) | Jonas Boetel, GDC 2019 | Открытая разработка и ранний доступ |
| [Grid Sage Games blog: Food Clocks](https://www.gridsagegames.com/blog/) | Josh Ge, 2014 | Часы давления против безопасного фарма |

## 29. Градостроители, менеджмент и тайкуны

City builder, менеджмент колонии, фабрики, тайкуны. Динамика систем — в [разделе 16](#16-симуляторы-и-системные-песочницы), источники и стоки — в [systems-balance.md](systems-balance.md#71-источники-стоки-конвертеры). Метрики экономики — [playtesting-metrics.md](playtesting-metrics.md#545-экономика-и-прогрессия).

### Ключевые принципы

- **Четыре техники городской симуляции.** Карты, сети и глобальные значения, агенты, связи «здание — здание». На них строятся красота, водоснабжение, преступность, пожары, рабочие смены и парковки (Guillaume Pierre, SimCity и Cityscapes: Sim Builder; GDC 2024).
- **Документы на одну страницу.** Для SimCity сделали больше 100 одностраничных документов от концепта до продакшна (Stone Librande, GDC 2013); шаблон — в [documentation.md](documentation.md#3-концепт-one-sheet-и-питч).
- **Малая команда может сделать жанр.** Cities: Skylines сделали 13 человек; доклад о том, какие функции и решения это позволили (Karoliina Korppoo, GDC Europe 2015).
- **Стабильность скучна.** Градостроитель стремится к устойчивому городу, и устойчивость надоедает. Against the Storm режет игру на забеги: новые сочетания народов, карт и нужд, сезоны и события, награда до того, как придёт скука; поселение служит «аватаром» с квестами и здоровьем; несколько путей к победе (Joel Couture, 2023).
- **Фабрика — это узкие места.** Еженедельный дневник Factorio с 2013 года показывает решения по дизайну, интерфейсу и производительности большой симуляции (Wube Software, Friday Facts).

### Типичные ошибки

- Поздняя игра без решений: город работает сам.
- Нечитаемая симуляция: игрок не понимает, почему жители недовольны.
- Одна оптимальная планировка.
- Экономика без стоков: деньги копятся и теряют смысл.

### Что мерить

Строка на симулированного игрока за игровой день:

```json
{"player": "bot_planner", "day": 12, "population": 4200, "gold": 8100, "sink_ratio": 0.92, "stuck": false, "unhappy_share": 0.07, "idle_share": 0.4, "explained_cause": true}
```

- `num:population@day=*`, `num:gold@day=*`, `num:sink_ratio@day=*` — кривая роста и баланс источников и стоков.
- `rate:stuck@day=*`; `num:idle_share@day=*` — растущая доля ожидания без решений означает позднюю скуку.
- `rate:explained_cause` — опросом: может ли игрок объяснить, почему город страдает. Шаблон коридоров: [economy-progression.json](../assets/targets/economy-progression.json).

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [We Built This City on Bits 'n Maps](https://gdcvault.com/play/1034401/We-Built-This-City-on) | Guillaume Pierre, GDC 2024 | Четыре техники городской симуляции |
| [Simulating a City, One Page at a Time](https://gdcvault.com/play/1017708/Simulating-a-City-One-Page) | Stone Librande, GDC 2013 | Одностраничные документы большой симуляции |
| [Cities: Skylines, A Case Study](https://www.gdcvault.com/play/1022809/Cities-Skylines-a-Case) | Karoliina Korppoo, GDC Europe 2015 | Градостроитель силами 13 человек |
| [How Against the Storm managed to mix city-building and roguelite play](https://www.gamedeveloper.com/business/how-against-the-storm-managed-to-mix-city-building-and-roguelite-play) | Joel Couture, 2023 | Забеги против поздней скуки |
| [Factorio Friday Facts](https://www.factorio.com/blog/) | Wube Software, с 27.09.2013 | Решения большой производственной симуляции |

## 30. Открытые миры

Открытые миры в экшене и RPG. Квесты и нарратив — в [разделе 5](#5-нарративный-дизайн), модульное производство уровней — в [разделе 4](#4-левел-дизайн). Чеклист ревью — [design-review.md](design-review.md#911-открытые-миры), метрики — [playtesting-metrics.md](playtesting-metrics.md#548-открытые-миры), стриминг мира в коде — [architecture-code.md](architecture-code.md#411-открытый-мир-стриминг-и-lod-симуляции).

### Ключевые принципы

- **Свобода маршрута.** Breath of the Wild убрала прогрессионные ворота: на любую поверхность можно залезть, параплан смягчает падения (Takuhiro Dohta, GDC 2017; пересказ Game Developer, 2023). «Химический» движок даёт огню, воде и другим стихиям действовать на любой объект, отсюда сотни взаимодействий (Game Developer, 2017). Сам Fujibayashi формулирует принцип как «делать игры умножением»: способности героя, умноженные на насыщенный мир (Ask the Developer: Tears of the Kingdom, часть 4, Nintendo, 2023); термин «мультипликативный геймплей» — из пересказа доклада GDC 2017 (Thumbsticks, 02.03.2017).
- **Рельеф управляет взглядом.** Треугольные формы рельефа дают выбор пути и прячут то, что за ними; разные формы служат ориентиром, ширмой или задают темп (Fujibayashi, Yonezu; CEDEC 2017, по пересказу Game Developer, 2023).
- **Мир вне главного квеста.** The Witcher 3: экономика, добыча и прогрессия должны награждать игру вне основной линии (Matthew Steinke, GDC Europe 2016).
- **Квесты.** Игрок должен хотеть историю; эмоция важнее зрелищности; не повторять одну информацию; последствия видимы и иногда отложены; не переусложнять второстепенное; новое строить на знакомом (Paweł Sasko, GDC 2023).
- **Производство мира без армии.** inFamous построил плотный город силами примерно дюжины художников: гексагональные основы, стандартные фундаменты зданий, приёмы раскладки (Nate Fox, GDC 2010). Путь от бумажной концепции до открытого action RPG — постмортем Horizon Zero Dawn (Eric Boltjes, GDC 2018).

### Типичные ошибки

- Контент-чеклист: иконки на карте вместо любопытства.
- Пустые пространства между интересными точками.
- Масштабирование врагов, которое отменяет рост героя.
- Быстрое перемещение, которое убирает исследование целиком.

### Что мерить

Строка на игрока за сессию:

```json
{"player": "p09", "day": 7, "level": "region_marsh", "poi_found": 5, "poi_from_marker": 2, "travel_share": 0.35, "main_quest_share": 0.4, "fast_travel_uses": 6, "stuck": false}
```

- `num:poi_found@level=*` и доля `poi_from_marker` — что находят сами, а что по указке.
- `num:travel_share` — доля времени в пути без событий; `num:main_quest_share` — сколько игры вне главной линии.
- `rate:stuck@day=*`; тепловые карты маршрутов — отдельно. Шаблоны коридоров: [economy-progression.json](../assets/targets/economy-progression.json) (`day` — сессия), [levels.json](../assets/targets/levels.json) (`level` — регион).

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Change and Constant: Breaking Conventions with 'The Legend of Zelda: Breath of the Wild'](https://www.gdcvault.com/play/1024562/) | Dohta, Fujibayashi, Takizawa; GDC 2017 | Как ломали условности серии |
| [5 design lessons learned from Breath of the Wild](https://www.gamedeveloper.com/design/5-design-lessons-learned-from-i-the-legend-of-zelda-breath-of-the-wild-i-) | Game Developer, 11.05.2023 | Свобода маршрута, треугольники CEDEC 2017, взаимодействия |
| [The Living World of 'The Witcher'](https://gdcvault.com/play/1023867/The-Living-World-of-The) | Matthew Steinke, GDC Europe 2016 | Экономика и добыча вне главного квеста |
| [10 Key Quest Design Lessons from 'The Witcher 3' and 'Cyberpunk 2077'](https://gdcvault.com/play/1028897/10-Key-Quest-Design-Lessons), [конспект](https://www.gamedeveloper.com/marketing/10-key-takeaways-from-the-quest-design-of-cyberpunk-2077-and-the-witcher-3) | Paweł Sasko, GDC 2023; Game Developer, 2023 | Уроки квест-дизайна |
| [Building an Open-World Game Without Hiring an Army](https://www.gdcvault.com/play/1012233/Building-an-Open-World-Game) | Nate Fox, GDC 2010 | Производство плотного города малой командой |
| ['Horizon Zero Dawn': A Game Design Postmortem](https://www.gdcvault.com/play/1024963/-Horizon-Zero-Dawn-A) | Eric Boltjes, GDC 2018 | От концепции к открытому action RPG |

## 31. Idle и incremental

Игры, где прогресс идёт сам, а игрок решает, куда вложить. Математика — в [systems-balance.md](systems-balance.md#75-idle-математика), этика монетизации — в [разделе 10](#10-live-service-f2p-и-этичная-монетизация). Метрики — [playtesting-metrics.md](playtesting-metrics.md#545-экономика-и-прогрессия).

### Ключевые принципы

- **Экспоненциальная цена против линейного дохода.** Цена следующего генератора = базовая × рост^число_купленных; в примере AdVenture Capitalist рост 1,07. Доход = базовый × число × множители. Цена обгоняет доход, и прогресс упирается в стену (Anthony Pecorella, 2016).
- **Престиж переносит стену дальше.** Сброс почти всего в обмен на валюту престижа или постоянные множители: каждый следующий забег уходит дальше по кривой. Формулы престижа разных игр (Realm Grinder, AdVenture Capitalist, Cookie Clicker, Egg, Inc., Clicker Heroes) и совет моделировать параметры в таблице — Part III (Pecorella).
- **Петли ядра и мета держат удержание.** Почему у idle-игр высокое удержание и почему они жизнеспособны в F2P — доклад с метриками платформы Kongregate (Pecorella, GDC 2015).
- **Ожидание — не наказание.** Стену, которую можно пройти только деньгами, игрок читает как «fun pain» ([раздел 10](#10-live-service-f2p-и-этичная-монетизация)).

### Типичные ошибки

- Стены, где единственное действие — ждать.
- Престиж слишком рано (сброс без смысла) или слишком поздно (застой).
- Переполнение чисел и нечитаемые большие значения.
- Монетизация ожидания вместо удобства.

### Что мерить

Бот-оптимизатор играет N дней и пишет строку на игровой день:

```json
{"player": "bot_greedy", "day": 4, "prestige_count": 2, "gold": 3.2e9, "stuck": false, "minutes_to_next_unlock": 9, "sessions": 11}
```

- `num:minutes_to_next_unlock` (p90) — длина стен; `rate:stuck@day=*`.
- `num:prestige_count@day=*` — темп престижа; время до первого престижа — отдельно.
- `num:sessions@day=*` — ритм возвращений. Шаблон коридоров: [economy-progression.json](../assets/targets/economy-progression.json).

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [The Math of Idle Games, Part I](https://www.gamedeveloper.com/design/the-math-of-idle-games-part-i) | Anthony Pecorella, 2016 | Формулы цены, дохода, массовой покупки |
| [The Math of Idle Games, Part II](https://www.gamedeveloper.com/game-platforms/the-math-of-idle-games-part-ii) | Anthony Pecorella, 14.12.2016 | Альтернативные модели роста, актуальность старых генераторов |
| [The Math of Idle Games, Part III](https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii) | Anthony Pecorella, 01.02.2017 | Престиж в разных играх |
| [Idle Games: The Mechanics and Monetization of Self-Playing Games](https://www.gdcvault.com/play/1022065/) | Anthony Pecorella, GDC 2015 | Петли, удержание, F2P, метрики Kongregate |

## 32. Party и социальные игры

Игры для компании: party-игры, локальный кооператив хаоса, социальная дедукция. Кооператив и «альфа-игрок» — в [разделе 12](#12-кооперативные), токсичность — в [разделе 9](#9-мультиплеер-и-соревновательные-игры).

### Ключевые принципы

- **Простое управление, равные герои, задач больше, чем игроков.** Overcooked: одна кнопка взять, одна — действие, стик — движение; у поваров одинаковые параметры. Игроки застревали в одной роли, поэтому задач сделали больше, чем людей, добавили задержки и помехи посреди уровня. Систему трёх жизней заменили лимитом времени с малым штрафом за проваленный заказ (Phil Duncan, 2016).
- **Социальная дедукция живёт в обсуждении.** Among Us держит карту и действия простыми, поэтому их легко обсуждать и смотреть; короткая фаза обсуждения даёт меньше места токсичным игрокам (Game Developer, 2021). Напряжение в скрытых ролях — Secret Hitler (Mike Boxleiter, GDC 2017).
- **Проклятые проблемы.** Free-for-all с упором на мастерство неизбежно превращается в политику: союзы, игра «вполсилы», чтобы не стать целью, kingmaking. Это конфликт обещаний игроку, а не баг; его не решают, а смягчают четырьмя приёмами: убрать возможности, ломающие обещание; спрятать плохие состояния за испытанием; поощрять их избегать; сделать их весёлыми (Alex Jaffe, Cursed Problems in Game Design, GDC 2019).
- **Просоциальный дизайн.** Токсичность бьёт по удержанию и доходу; «добрые игры» строят взаимозависимость и безопасность в основу, а не латают модерацией потом (Daniel Cook, Kind Games, GDC 2024).

### Типичные ошибки

- Выбывшие игроки долго ждут без дела.
- Один игрок решает за всех.
- Правила надо читать до начала, а компания уже собралась.
- Kingmaking: исход решает проигрывающий.

### Что мерить

Строка на игрока в раунде; `side` — роль:

```json
{"session": 41, "round": 3, "players": 6, "side": "impostor", "win": true, "idle_s": 40, "talk_share": 0.22, "rules_questions": 1, "wants_rematch": true}
```

- `rate:win@side=*`, `rate:win@side=*,players=*` — баланс ролей при разном числе игроков.
- `num:idle_s` — время выбывших без дела; распределение `talk_share` по игрокам — доминирование, считается отдельно.
- `num:rules_questions`, `rate:wants_rematch` — порог входа и желание сыграть ещё. Шаблон коридоров: [team-pvp.json](../assets/targets/team-pvp.json) с `side` — ролью; коридор 48–52% подходит только симметричным ролям, для неравных по числу ролей задайте свой.

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Game Design Deep Dive: Building truly cooperative play in Overcooked](https://www.gamedeveloper.com/design/game-design-deep-dive-building-truly-cooperative-play-in-i-overcooked-i-) | Phil Duncan, 2016 | Роли, помехи, мягкий провал |
| [From Mafia to Among Us: Can social deduction evolve as online multiplayer?](https://www.gamedeveloper.com/design/from-mafia-to-among-us-can-social-deduction-evolve-as-online-multiplayer-) | Game Developer, 2021 | Обсуждение как ядро дедукции |
| [Board Game Design Day: 'Secret Hitler'](https://gdcvault.com/browse/gdc-17/play/1024248) | Mike Boxleiter, GDC 2017 | Конфликт и пики напряжения в скрытых ролях |
| [Cursed Problems in Game Design (слайды)](https://media.gdcvault.com/gdc2019/presentations/Jaffe_Alex_Cursed_Problems_In.pdf) | Alex Jaffe, GDC 2019 | Политика в free-for-all и четыре приёма |
| [Kind Games: designing for prosocial multiplayer (слайды)](https://media.gdcvault.com/gdc2024/Slides/GDC+slide+presentations/Kind+Games+-+GDC+2024+-+Daniel+Cook.pdf) | Daniel Cook, GDC 2024 | Взаимозависимость и безопасность в основе |
| [The challenges and rewards of designing local multiplayer games](https://www.gamedeveloper.com/design/the-challenges-and-rewards-of-designing-local-multiplayer-games) | Phill Cameron, 2016 | Локальный мультиплеер на одном экране |

## 33. Расхождения и пробелы

1. **Философии баланса живых игр расходятся.** Hearthstone (2014): минимум правок после релиза. Legends of Runeterra (2020): регулярные правки, у каждой карты есть дом. Marvel Snap (2023): правки чисел каждые две недели без обновления клиента. VALORANT (2020): правки по выходу за внутренние границы, без расписания. Это разные модели доверия игроков; выбор записывается в опоры.
2. **Win rate против восприятия.** Riot (Lee Sin в LoR, Raze в VALORANT) и Blizzard (Dodds) нерфят за фрустрацию при нормальном WR; Sirlin и VALORANT подчёркивают, что эксперты и мелкие доли процента видят дисбаланс раньше общей статистики. Числа и опросы смотрят вместе.
3. **«Резинка» спорна.** Pure отказалась от классической «резинки» ради сценария гонки, Forza подстраивает машины, а не водителей, Birla защищает «резинку» как удержание, а Mario Kart сознательно платит ею за плотную гонку. Единого ответа нет.
4. **Power creep.** «Лестница Эшера» подтверждена Rosewater (Blogatog, 15.11.2019), но то, что общий уровень силы не растёт, — позиция WotC, с которой спорят.
5. **Числовых ориентиров в первоисточниках мало.** Пороги вроде «WR выше 55%», «лидер на середине выигрывает больше 90%», «нет ходов к ходу 3–4» — рабочие эвристики. Числа из источников: окна попадания osu!, 128 тиков и 35 мс у VALORANT, 80% дистанции в Pure, 40% шанса у проигрывающей команды в LoR, скорости аватара в VR (Meta), 8 кадров отката за 16 мс (NetherRealm), рост цены 1,07 в примере Pecorella. Коридоры ставятся на этапе 2 [пайплайна](pipeline.md#этап-2-опоры-и-целевые-метрики) и помечаются как предположение, если нет референса.
6. **Пересказ вместо первоисточника.** Часть докладов GDC доступна только по подписке; тогда в таблицах стоит конспект Game Developer или Tommy Thompson (Splinter Cell: Blacklist, Drivatar), слайды (Jaffe, Cook, Boutin) или описание сессии в GDC Vault (Cain, Brevik, Igarashi, Korppoo, Steinke). Детали докладов сверх описания и конспекта не проверялись.
7. **Непроверенных утверждений не осталось** (сверка 22.10.2026). Не найдены и убраны: доклады Jake Solomon о XCOM (вместо них интервью Ananda Gupta), доклады Team Cherry о бое Hollow Knight, первоисточник про видимый прогресс и смену режима против ranked anxiety. По пересказу: интервью Leacock в платном журнале Senet (цитаты у Derek Bruff), термин «мультипликативный геймплей» (Thumbsticks). Документ Valve и определения 17lands сверены по копиям web.archive.org.
8. **Мёртвые и ограниченные ссылки.** Оригинал Celeste & Forgiveness на Medium недоступен, используется копия на maddymakesgames.com. playruneterra.com отдаёт пустую страницу без JS. Статья Riot о сетевом коде VALORANT переехала с technology.riotgames.com на riotgames.com. Сайт Frictional Games не показывает старые посты Thomas Grip, используются перепечатки на Game Developer.
9. **Пробелы по жанрам.** Нет первоисточников по extraction-шутерам (Escape from Tarkov, Hunt: Showdown) — только пресса; нет докладов о дизайне FIFA, Madden и NBA 2K; по JRPG есть разбор Persona 5, но нет докладов Atlus, Square Enix и Game Freak; по party-играм нет материалов Jackbox; по ритм-играм не найдено исследование калибровки задержки. Дизайн-интервью о ресурсах франшизных ККИ (Lorcana, SWU, One Piece, Pokémon Pocket) не найдены — есть только правила. Кооперативные, мобильные и настольные разделы короче остальных. Если проблема выходит за рамки разделов, в карточке гипотезы пишите, что решения в библиотеке нет, а общие паттерны берите из [mechanics-patterns.md](mechanics-patterns.md) и [systems-balance.md](systems-balance.md).
