# Жанры и дисциплины: что специфично для каждой области

Что в каждом жанре и каждой дисциплине работает иначе, чем в общей теории: свои принципы, типовые ошибки и метрики здоровья. Справочник открывают на этапе 10 [пайплайна](pipeline.md#этап-10-поиск-в-библиотеке-знаний), когда проблема типична для жанра, и на этапе 2, когда для жанра нужны целевые метрики. Карточные игры разобраны подробнее остальных: для них автоматический замер даёт больше всего, и это основной жанр проектов, для которых писался скилл.

- [1. Как пользоваться](#1-как-пользоваться)
- [2. Карточные игры](#2-карточные-игры)
- [3. Рогалики и roguelite](#3-рогалики-и-roguelite)
- [4. Левел-дизайн](#4-левел-дизайн)
- [5. Нарративный дизайн](#5-нарративный-дизайн)
- [6. Стратегии и тактика](#6-стратегии-и-тактика)
- [7. Экшен, платформеры, game feel](#7-экшен-платформеры-game-feel)
- [8. Головоломки](#8-головоломки)
- [9. Мультиплеер и соревновательные игры](#9-мультиплеер-и-соревновательные-игры)
- [10. Live service, F2P и этичная монетизация](#10-live-service-f2p-и-этичная-монетизация)
- [11. Мобильные и казуальные](#11-мобильные-и-казуальные)
- [12. Кооперативные](#12-кооперативные)
- [13. Настольные](#13-настольные)
- [14. Файтинги](#14-файтинги)
- [15. MMO и онлайн-миры](#15-mmo-и-онлайн-миры)
- [16. Симуляторы и системные песочницы](#16-симуляторы-и-системные-песочницы)
- [17. Хоррор](#17-хоррор)
- [18. VR](#18-vr)
- [19. Расхождения и пробелы](#19-расхождения-и-пробелы)

## 1. Как пользоваться

1. Найдите раздел жанра. Если игра на стыке (roguelike-deckbuilder, мобильная ККИ), читайте оба раздела: карточный и жанровый.
2. «Ключевые принципы» — это проверочный список для ревью дизайна ([design-review.md](design-review.md)) и источник гипотез. «Типичные ошибки» — симптомы, которые стоит искать в замере и на плейтесте.
3. «Что мерить» дан в схеме записи стенда из [pipeline.md](pipeline.md#этап-7-измерительный-стенд): одна строка JSONL на игрока в партии, на забег или на сессию. Ключи вида `rate:win@deck=X` и `num:turns` — это выход [design_metrics.py](../scripts/design_metrics.py): `--rate ПОЛЕ` для булевых полей, `--num ПОЛЕ` для чисел, `--by ПОЛЕ` или `--by ПОЛЕ1,ПОЛЕ2` для разрезов. Поля в примерах — предложение, проект выбирает свои.
4. Метрики, которые скрипт не считает (энтропия, тепловые карты, концентрация выручки), помечены «считается отдельно». Числовые пороги — рабочие ориентиры, а не цитаты источников; свои коридоры задаются на этапе 2 пайплайна по [systems-balance.md](systems-balance.md) и [playtesting-metrics.md](playtesting-metrics.md). Книги по жанрам — в [books.md](books.md).
5. Пометки: `[не проверено]` — ссылку, дату или факт не удалось сверить с первоисточником; `[устарело]` — ссылка мертва, рядом дана замена.

## 2. Карточные игры

ККИ (CCG/TCG), LCG, колодостроители (deckbuilder) и roguelike-deckbuilder. Это самая «инженерная» дисциплина геймдизайна: у Magic: The Gathering около 30 лет публичных материалов о дизайне, а цифровые ККИ добавили к ним балансировку по телеметрии. Ключевые принципы разбиты по темам в 2.1–2.7, ошибки, метрики и источники идут после них.

### 2.1 Дизайн сета: скелет, бюджет сложности, идентичность фракций

**Скелет до карт.** Сет планируют как чертёж дома (Rosewater, Nuts & Bolts 2010). Порядок: число слотов по редкости → распределение по цвету или фракции и по типу → кривая стоимости внутри цвета → функции слотов («removal на коммоне в каждом цвете», «дешёвый блокер») → только потом конкретные карты. Слот описывает функцию, а не карту (Filling the Design Skeleton, 2011). Каждому слоту дают код (цвет, редкость, номер), чтобы обсуждать дыры и перекосы до того, как появятся тексты. По MTG Wiki, скелет пересматривали в 2021 году, а правки 2024 года связаны с переходом на Play Boosters. Пример скелета для франшизной ККИ с ресурсом DON!!: оси «цвет → кривая стоимости в DON!! → роль» (блокер, раш, каунтер, триггер).

**Сложность — ограниченный бюджет.** New World Order (Rosewater 2011) переносит сложность с коммонов на анкоммоны и выше. Мерой сложности служит, среди прочего, число карт на коммоне, которые «смотрят» на другие карты на поле. Принцип NWO: «если темы нет на коммоне, это не твоя тема». MTG Wiki датирует начало инициативы 2008 годом; NWO вырос из падения продаж после блока Time Spiral. Бюджет ключевых слов устроен так же: новых ключевых слов на сет немного, «вечнозелёные» переиспользуются. Точных чисел в проверенных источниках нет.

**Lenticular design** (Rosewater, 2014; на сайте статья датирована 16.12.2014) — карта, которую новичок читает просто, а опытный игрок видит в ней глубину. Это главный приём против роста сложности: глубина без новых слов.

**Идентичность фракций (color pie).** Mechanical Color Pie 2021 расписывает для каждого цвета основные, вторичные и третичные возможности, а также то, чего цвет не умеет вовсе. Слабости важнее сильных сторон: они создают взаимодействие и причину играть в два цвета. Шаблон подходит для фракций, команд или домов любой ККИ.

**Адресат у каждой механики.** Психографии Timmy (опыт, большие эффекты), Johnny (самовыражение, комбо) и Spike (победа) из «Timmy, Johnny, and Spike Revisited» (2006; оригинальная статья о психографиях — 2002). У каждой редкости и механики должен быть адресат.

**Лимитед и конструктед — разные игры.** Лимитед балансируют по силе коммонов и по as-fan. As-fan — термин R&D: сколько карт определённого вида в среднем попадает в один бустер; считается из редкости, числа карт этой редкости в сете и числа слотов этой редкости в бустере ([MTG Wiki](https://mtg.wiki/page/As-fan) со ссылкой на Rosewater, A Few More Words from R&D, 2016). Конструктед балансируют по лучшим картам формата. Power creep сдерживают ротация (Standard) или «пенсия» героев (Living Legend во Flesh and Blood). Внутри сета WotC применяет «лестницу Эшера» (Escher Stairwell): одно ослабляют, другое усиливают, и кажется, что сила растёт, хотя общий уровень держится ровным (Rosewater, [Blogatog, 15.11.2019](https://markrosewater.tumblr.com/post/189093325363/what-strategies-if-any-does-wizards-take-to)). Комментаторы с этой оценкой спорят.

### 2.2 Ресурсные системы франшизных ККИ

Ресурсная система определяет дисперсию партии: сколько будет «не-игр», когда игрок не может действовать из-за случайного расклада. Классика — mana screw и mana flood в MTG. Современные франшизные ККИ почти все строят ресурс так, чтобы его нельзя было не получить.

| Игра | Ресурс | Центр колоды | Дисперсия ресурса | Статус данных |
| --- | --- | --- | --- | --- |
| One Piece Card Game | DON!!: отдельная колода DON!! из 10 карт. В фазу DON!! каждый ход в зону стоимости выкладываются 2 DON!!, у первого игрока на первом ходу 1 (6-4-1). Отданная лидеру или персонажу DON!! даёт +1000 силы только в ваш ход (6-5-5-2); в фазу обновления отданные DON!! возвращаются в зону стоимости повёрнутыми (6-2-3) | Лидер с жизнями (Life), задаёт цвета; колода 50 карт, не больше 4 копий (5-1-2) | Нет screw/flood по ресурсу | Сверено с Comprehensive Rules v1.2.1 от 28.08.2026 |
| Disney Lorcana | Inkwell («чернильница»): раз в ход можно показать карту с символом чернил и положить её в inkwell рубашкой вверх (4.2.3); эффекты могут добавлять дополнительные карты | Персонажи «квестуют» за лор вместо атаки в лицо; победа на 20 лора (1.8.1.1) | Игрок сам выбирает, чем жертвовать; карты без символа чернил ресурсом стать не могут | Comprehensive Rules 2.2.0 (с 09.07.2026); дизайн-интервью Ravensburger об inkwell не найдено |
| Star Wars: Unlimited | При подготовке каждый кладёт ровно 2 карты из руки ресурсами; затем в фазе перегруппировки можно положить 1 любую карту из руки (5.5) | Лидер + база; initiative: кто взял жетон, ходит первым в следующем раунде | Низкая | Comprehensive Rules v8.0 от 08.07.2026 |
| Flesh and Blood | Pitch: любая карта — ресурс, ресурсы есть с первого хода; базовая защита карт 3 | Герой | Низкая; таблица «cost–pitch–power» для циклов | Revealing Cycles, 2019 |
| Pokémon TCG Pocket | Energy Zone вместо энергокарт: одна Energy каждый ход | Колода 20 карт, не больше 2 копий; 3 очка за нокауты вместо призов; скамейка 3 и отсутствие муллигана — по Bulbapedia | Низкая | Колода, Energy Zone и 3 очка — pokemon.com, 30.01.2025; дизайн-интервью Creatures не найдено |

Выводы для своей игры:

- Чем проще ресурс, тем шире аудитория. Снижение «не-игр» — явная цель у Flesh and Blood и Pokémon Pocket.
- Ресурс без случайности переносит дисперсию в другое место: в добор карт, триггеры, порядок колоды. Мерить надо «не-игры» в целом, а не только нехватку ресурса.
- Компенсация первого хода в One Piece по CR v1.2.1: первый игрок не берёт карту на первом ходу (6-3-1) и получает 1 DON!! вместо 2 (6-4-1). Запрет боя на первом ходу действует для **обоих** игроков на их собственный первый ход (6-5-6-1), так что это не компенсация второму игроку, а общее замедление старта. Первая атака в партии всё равно у первого игрока — на его втором ходу, с 3 DON!!; второй игрок отвечает на своём втором ходу с 4 DON!! (без учёта эффектов карт). Для симулятора это значит: преимущество хода мерить отдельно (`rate:win@went_first=true`), а не считать его снятым правилами. Общие приёмы компенсации — в [mechanics-patterns.md](mechanics-patterns.md#4-баланс-и-честность), строки Б1–Б4.

**Правила One Piece Card Game.** Актуальная официальная версия — Comprehensive Rules **v1.2.1 от 28.08.2026** ([страница правил Bandai](https://en.onepiece-cardgame.com/rules/)). Версия v1.2.0 существовала: это официальный PDF от **16.01.2026** (в архиве Wayback Machine), а не от 09.01.2026, как писали фанатские гайды. До неё были v1.1.9 (17.10.2025) и v1.1.3 (2024). Ключевые числа (колода 50 карт и 10 DON!!, +2 DON!! за ход и 1 у первого игрока на первом ходу, +1000 за DON!! только в свой ход, запрет боя на первом ходу) не менялись между v1.1.9, v1.2.0 и v1.2.1. В v1.2.1 уточнены, в частности, Counter (2-10-3, 2-10-4: значение может меняться эффектами; при нескольких Counter применяется наибольший) и формулировки «если у вас есть» (3-1-2-1: по умолчанию имеется в виду поле). Bandai обновляет правила несколько раз в год: перед работой с правилами берите PDF со страницы правил, номер версии стоит на первой странице.

### 2.3 Как передавать IP через механику

- **Feelings-first** (Danny Schaefer, Star Wars: Unlimited). Карту персонажа проектируют от ощущения: «каким должен ощущаться Дарт Вейдер». Сначала эмоция и образ персонажа, потом механика. Вейдер подавляет, Луффи растягивается и бьёт дважды.
- **Резонанс** (Rosewater, Twenty Years, Twenty Lessons, GDC 2016): механика должна рассказывать то же, что арт и имя. Карта — микрорассказ из имени, арта, механики и flavor text.
- **Каналы передачи IP**: (а) лидер или герой, который задаёт цвета и стиль колоды (лидер One Piece, лидер + база в SWU, герой FaB); (б) ресурс с флейвором: DON!! как сила команды, которую раздают персонажам на ход, чернила в Lorcana, которыми «рисуют» героев; (в) условие победы, отражающее тон IP: в Lorcana — лор через квесты, а не прямая агрессия.
- **Сет как кусочек вселенной.** В SWU сеты первого года планировали как фрагменты мира: контрабандисты, Внешнее кольцо (Shadowy Insights, 2024).
- **Top-down по умолчанию.** Для франшизной ККИ дизайн идёт от сцен и персонажей IP к механикам. Пример — Innistrad: по словам Rosewater, «с первого дня» сет проектировался как top-down, и механики встраивались в креатив с самого начала ([C'mon Innistrad, Part 1](https://magic.wizards.com/en/news/making-magic/cmon-innistrad-part-1-2011-09-02), 2011). Формулировку «золотой стандарт» в первоисточнике найти не удалось.
- **Аудитория IP шире аудитории ККИ.** Цели Lorcana: стратегично, весело, инклюзивно, для аудитории шире традиционной (Ryan Miller). Ориентир иммерсии — «как в Диснейленде».

### 2.4 Баланс цифровых ККИ

**Win rate — сигнал, а не цель.** У каждой карты своя роль, а не равная сила. 50% у каждой карты не нужны: «у каждой карты есть дом в мете» (Riot, Legends of Runeterra). Метрики обманчивы без интерпретации (Giovannetti, Slay the Spire, GDC 2019).

**Pick rate против win rate.** Две оси дают четыре случая:

| Pick rate | Win rate | Что значит | Что делать |
| --- | --- | --- | --- |
| Высокий | Высокий | Кандидат в доминирующие карты | Проверить матрицу матчапов и фрустрацию, затем решать |
| Высокий | Низкий | Ловушка: карта выглядит сильной, но проигрывает | Обучение, текст, ясность эффекта; иногда это карта новичков (см. разрез по уровню) |
| Низкий | Высокий | Нишевая или недооценённая карта | Часто ничего: сообщество само найдёт. Проверить, не мала ли выборка |
| Около 0 | — | «Мёртвая» карта, которую никто не берёт | Кандидат на ап или переделку (дашборды Monster Train) |

WR всегда смотрят в контексте: колода, мастерство пилота, первый или второй ход. Разрез по уровню мастерства или по боту — строка Б8 в [mechanics-patterns.md](mechanics-patterns.md#4-баланс-и-честность).

**Нерф за фрустрацию, а не только за силу.** Критерии нерфа Hearthstone (Eric Dodds, 2014): карта неинтерактивна, против неё «бесит играть», она непредсказуема или превосходит всё в своей стоимости. Сильные архетипы там не нерфят, а контрят новыми картами; слабые карты почти не апают. В Legends of Runeterra Lee Sin с WR около 53% ослабили не за WR, а за то, что против него неприятно играть (Steve Rubin, 2020). Фрустрацию меряют опросом после матча.

**Частота правок — компромисс между свежестью и доверием к коллекции.** Здесь три разные философии:

| Игра | Подход | Источник |
| --- | --- | --- |
| Hearthstone (2014) | После релиза менять карты минимально; сильное контрят новыми картами | Dodds, Card Balance Philosophy |
| Legends of Runeterra (2020) | Ежемесячный баланс (каждый второй патч) по WR карт, WR колод и play rate чемпионов; цикл из трёх патчей на сет `[не проверено]` | Riot, по пересказам Inven Global и outof.games; страницы playruneterra.com не читаются без JS и не архивированы |
| Marvel Snap (2023) | OTA-правки без обновления клиента каждые две недели по четвергам, патчи примерно раз в 4 недели по вторникам. OTA меняет только числа: стоимость, силу, масштаб эффекта; переделка способности требует патча | Заметки разработчиков, цитата в [Marvel Snap Zone, 09.11.2023](https://marvelsnapzone.com/marvel-snap-november-9-2023-ota-card-balance-updates/); график мог измениться |

Частые правки снижают доверие к коллекции и делают политику возврата ресурсов болезненной. Выбирайте подход осознанно и записывайте его в опоры.

**Короткая партия и ставки.** Marvel Snap: партия около 3 минут, 6 ходов, удвоение ставки как кубик удвоения в нардах. Отступление даёт выход из проигранной партии без полной потери. Это снимает «мёртвое время» (Brode, GDC 2023). Онбординг: ранние игроки просили муллиган, его сознательно не добавили; сложность вводят картами по мере роста коллекции.

**Полная переделка живой ККИ возможна, но дорога.** Gwent Homecoming (2018): в анонсе CD Projekt Red закладывал на переделку около шести месяцев и рассматривал удаление одного из рядов ([Engadget, 14.04.2018](https://engadget.com/2018/04/14/gwent-card-game-overhaul)). В нынешнем Gwent два ряда, Melee и Ranged: по Wikipedia, ряда Siege из The Witcher 3 нет. Что ряд убрали именно в Homecoming и какую долю карт переработали (в заметках «80–90%»), по первоисточнику не сверено `[не проверено]`.

### 2.5 Физическая ККИ без патчей

- Напечатанную карту исправить нельзя. Остаются бан-листы, ограничения и эррата, а эррата в физической игре дорога: у игроков на руках старый текст. Ошибки в физической ККИ стоят дороже, чем в цифровой.
- Отсюда два обязательных инструмента до печати: внутренний симулятор партий (этапы 7–8 [пайплайна](pipeline.md#этап-7-измерительный-стенд)) и долгий плейтест с людьми.
- Ротация (Standard) или «пенсия» героев (Living Legend во FaB) — способы управлять силой пула без изменения карт.
- Зависимость от генератора — отдельный риск. KeyForge генерировал уникальные колоды алгоритмом без деклбилдинга; по Wikipedia, в 2021 году производство встало, потому что сломался алгоритм.

### 2.6 Roguelike-deckbuilder и колодостроители

- **Колода — это прогрессия забега.** Ключевые решения: взять карту, пропустить или убрать. Удаление карт ценно так же, как добавление (Slay the Spire).
- **Метрики с первого дня.** Slay the Spire поднял сервер метрик ещё до раннего доступа и балансировал по данным Early Access и отзывам сообщества (Giovannetti, GDC 2019).
- **Механика → плейтест → арт.** Monster Train делал арт только после плейтестов; внутренние дашборды показывали pick rate и WR по связкам кланов и карты, которые никто не берёт (Mark Cooke, 2020).
- **Скейлинг одного числа.** Balatro сводит прогрессию к счёту против blind и множителям. Главный источник вдохновения — слот-roguelike Luck Be a Landlord, а не деклбилдеры; истоки — Big Two и покер. Системы, которые не добавляют удовольствия, вырезаются (LocalThunk, 2024).
- **Читаемость важнее текста.** Inscryption заменил текст иконками сигилов из-за низкого разрешения (Mullins, GDC 2022).
- **Модульность рынка карт.** Dominion: набор из 10 карт королевства на партию даёт реиграбельность без новых правил (Vaccarino).

### 2.7 Правила — тоже продукт

Образец — Magic Comprehensive Rules (действующая редакция от 25.09.2026, сверено по [странице правил](https://magic.wizards.com/en/rules)): пронумерованные пункты (100.1a), глоссарий, слои эффектов (613), приоритет (117), стек и разрешение (405, 608), state-based actions (704). Те же приёмы у One Piece CG (пункты вида 6-5-6-1), Lorcana (4.2.3) и Star Wars: Unlimited (5.5). Для движка это прямой мост «правило → тест»: на каждый пункт правил — свой тест (этап 6 пайплайна). Как писать такие правила — [documentation.md](documentation.md#7-правила-карточной-игры-в-стиле-comprehensive-rules).

### Типичные ошибки

- Тема механики есть только на редких картах (нарушение NWO).
- Взрыв ключевых слов и перегруженный текст на коммонах: новички уходят.
- Неинтерактивные комбо и OTK; карты, против которых «бесит играть», хотя WR в норме.
- Баланс только по WR, без разрезов по колоде, мастерству и очерёдности хода.
- Power creep ради продаж без ротации или «пенсии»: старые карты обесцениваются.
- Слишком частые правки в цифровой ККИ: падает доверие к коллекции.
- Ресурсная система с «не-играми» без компенсации.
- Нечитаемые карты: мелкий текст при низком разрешении.
- Зависимость от процедурного генератора колод без запасного плана.
- Частые эррата в физической ККИ.

### Что мерить

Основной файл стенда — одна строка на игрока в партии:

```json
{"match": 77, "seed": 77, "deck": "Red-Rush", "opp_deck": "Blue-Control", "bot": "mcts", "went_first": true, "win": false, "turns": 9, "comeback": false, "no_game": false, "curve_hit_t3": true, "mulligan": false}
```

| Метрика | Ключ или способ | Что показывает |
| --- | --- | --- |
| Преимущество хода | `rate:win@went_first=true` | Нужна ли компенсация второму игроку |
| Сила колоды и матрица матчапов | `rate:win@deck=*`, `rate:win@deck=*,opp_deck=*`, `spread:win@deck` | Доминирующие колоды (ориентир: строка с WR выше 55% против всех) и «камень-ножницы-бумага». Зеркала исключать |
| Длина партии | `num:turns@went_first=true`, `num:turns@deck=*` | Темп, доля партий, решённых к ходу N |
| «Не-игры» | `rate:no_game` (нет ходов или ресурсов к ходу 3–4) | Дисперсия ресурса и добора |
| Попадание в кривую | `rate:curve_hit_t3` (сыграна карта стоимостью k на ходу k); теоретически — гипергеометрика | Состав колоды и кривая стоимости |
| Камбэк | `rate:comeback` (победил отстававший по жизням или доске на ходу N) | Снежный ком, опоры вида «камбэк возможен» |
| Муллиган | `rate:win@mulligan=true` | Цена плохой стартовой руки |
| Разнообразие меты | Эффективное число архетипов 1/Σp² и энтропия Шеннона по доле `deck`; считается отдельно | Застой меты |

Покарточные метрики удобнее писать отдельным файлом, одна строка на карту в колоде игрока в партии:

```json
{"match": 77, "card": "OP-R-014", "deck": "Red-Rush", "drawn": true, "played": true, "opening_hand": false, "win": false}
```

`rate:win@card=*,drawn=true` — аналог GIH WR (win rate, когда карта была в руке; термин популяризировал 17lands `[не проверено]`). `rate:played@card=*` показывает, мёртвая ли карта в руке, `rate:win@card=*,opening_hand=true` — силу в стартовой руке.

Для roguelike-deckbuilder — файл предложений карт, одна строка на карту в предложении, и файл забегов:

```json
{"run": 5120, "act": 2, "card": "Bash+", "picked": true, "skipped_all": false, "run_win": false}
```

`rate:picked@card=*` против `rate:run_win@card=*,picked=true` даёт разрыв «берут, но проигрывают» и обратный; карты с `rate:picked` около 0 — «мёртвые». WR забега по уровням сложности (Ascension) и смерти по актам — как в [разделе 3](#3-рогалики-и-roguelite).

Телеметрия и плейтест: удержание новичков после N партий, ход или карта, на которых сдаются (`num:conceded_turn`), время хода, конверсия обучения (`rate:finished_tutorial`). Опрос после матча «бесило ли играть против» (`rate:annoying@opp_deck=*`) — отдельная ось рядом с WR.

### Источники: Magic: The Gathering

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Nuts & Bolts: Design Skeleton](https://magic.wizards.com/en/news/making-magic/nuts-bolts-design-skeleton-2010-02-15) | Mark Rosewater, 2010 | Канонический метод скелета сета: слоты по редкости, цвету, типу, коды карт |
| [Nuts & Bolts: Filling the Design Skeleton](https://magic.wizards.com/en/news/making-magic/nuts-bolts-filling-design-skeleton-2011-02-28) | Rosewater, 2011 | Наполнение скелета функциями, а не картами |
| [Nuts & Bolts — индекс серии](https://mtg.wiki/page/Nuts_&_Bolts) | MTG Wiki, с 2009 | Все выпуски, включая Troubleshooting (2016) и Initial Ideation (2022) |
| [New World Order](https://magic.wizards.com/en/news/making-magic/new-world-order-2011-12-05) | Rosewater, 2011 | Сложность как бюджет по редкостям |
| [Lenticular Design](https://magic.wizards.com/en/news/making-magic/lenticular-design-2014-12-15) | Rosewater, 16.12.2014 | Глубина для опытных без сложности для новичков |
| [C'mon Innistrad, Part 1](https://magic.wizards.com/en/news/making-magic/cmon-innistrad-part-1-2011-09-02) | Rosewater, 2011 | Top-down сет от первого дня: механики из жанра ужасов |
| [Mechanical Color Pie 2021](https://magic.wizards.com/en/news/making-magic/mechanical-color-pie-2021), [Changes](https://magic.wizards.com/en/news/making-magic/mechanical-color-pie-2021-changes) | Rosewater, 2021 | Шаблон механической идентичности фракций |
| [Ten Things Every Game Needs, Part 1](https://magic.wizards.com/en/news/making-magic/ten-things-every-game-needs-part-1-2011-10-24) | Rosewater, 2011 | Базовый чек-лист: цель, правила, взаимодействие, катч-ап |
| [Timmy, Johnny, and Spike Revisited](https://magic.wizards.com/en/articles/archive/making-magic/timmy-johnny-and-spike-revisited-2006-03-20-0) | Rosewater, 2006 | Психографии игроков ККИ |
| [Twenty Years, Twenty Lessons](https://www.gdcvault.com/play/1023186/) | Rosewater, GDC 2016, бесплатно | Уроки 20 лет: ограничения, резонанс, «любят, но не обожают — провал» |
| [Magic Comprehensive Rules](https://magic.wizards.com/en/rules) | Wizards; на 20.10.2026 действует редакция от 25.09.2026 ([PDF](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.pdf)) | Эталон формулировки правил для движка и rules-документа |
| [Power creep](https://mtg.wiki/page/Power_creep), [Escher Stairwell на Blogatog](https://markrosewater.tumblr.com/post/189093325363/what-strategies-if-any-does-wizards-take-to) | MTG Wiki; Rosewater, 15.11.2019 | Позиция WotC: «лестница Эшера» держит общий уровень силы ровным |
| [As-fan](https://mtg.wiki/page/As-fan) | MTG Wiki со ссылками на Rosewater (2011, 2016, 2025) | Определение и расчёт as-fan для лимитеда |
| Characteristics of Games | George Skaff Elias, Richard Garfield, Gutschera; MIT Press, 2012 (Open Library) | Удача и навык, длина партии, катч-ап; один из авторов — создатель Magic |

### Источники: цифровые ККИ и roguelike-deckbuilder

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Hearthstone's Card Balance Philosophy](https://hearthstone.blizzard.com/en-gb/blog/12383909) | Eric Dodds, 2014 | Явные критерии нерфа; «контрить новыми картами, а не нерфить» |
| [10 Bits of Hearthstone Design Wisdom](https://gamedeveloper.com/design/video-10-pieces-of-i-hearthstone-i-design-wisdom) | Eric Dodds, GDC 2014 | Читаемость, меньше пустых решений, ход соперника не скучен |
| [Designing MARVEL SNAP](https://gdcvault.com/play/1029024/Designing-MARVEL-SNAP) | Ben Brode, GDC 2023 | Короткая партия, удвоение ставки, бумажный прототип за 2 дня |
| [Second Dinner: onboarding и дизайн карт](https://mobilegamer.biz/second-dinner-reveals-the-secrets-of-marvel-snaps-onboarding-and-card-design/) | mobilegamer.biz, 2023 | Онбординг без муллигана, сложность по мере роста коллекции |
| Doing It Live: Prototyping in MARVEL SNAP | Kent-Erik Hagman, GDC 2025 | Прототипирование в живой игре; доклад подтверждён отчётом 4Gamer, страница в GDC Vault и запись не найдены |
| [OTA Card Balance Updates, 09.11.2023](https://marvelsnapzone.com/marvel-snap-november-9-2023-ota-card-balance-updates/) | Marvel Snap Zone с цитатой заметок Second Dinner | Ритм OTA и патчей; что можно менять без обновления клиента |
| [Slay the Spire: Metrics Driven Design and Balance](https://www.gdcvault.com/browse/gdc-19/play/1025731) | Anthony Giovannetti, GDC 2019 | Метрики с ранней стадии; где метрики обманывают |
| [Анонс доклада Slay the Spire](https://gdconf.com/news/learn-slay-spires-successful-metrics-driven-approach-game-balancing-gdc-2019) | GDC, 2019 | Краткие тезисы, бесплатно |
| [Balatro interview](https://toucharcade.com/2024/03/18/balatro-interview-mobile-port-localthunk-dlc-plans-updates-new-jokers-demo-feedback/) | LocalThunk, TouchArcade 2024 | Итерации демо с сообществом |
| [Balatro inspired by Luck Be a Landlord](https://shacknews.com/article/139116/balatro-inspiration-luck-be-a-landlord-reddit-ama) | LocalThunk, Shacknews 2024 | Прогрессия одним числом; вдохновение из слот-roguelike |
| [Game Maker's Notebook: LocalThunk](https://gamemakersnotebook.libsyn.com/balatro-creator-localthunk-talks-inspirations-and-jokers) | AIAS, 2024 | Вырезать системы без удовольствия (прочитано только описание) |
| [Sacrifices Were Made: The Inscryption Post-Mortem](https://gdcvault.com/play/1027609/Independent-Games-Summit-Sacrifices-Were) | Daniel Mullins, GDC 2022 | От джема к игре, иконки вместо текста, мета-нарратив |
| [How a game jam on "sacrifices" became Inscryption](https://www.gamedeveloper.com/design/how-game-jam-sacrifices-became-inscryption) | Game Developer, 2022 | Конспект доклада |
| [Monster Train developer Q&A](https://www.digitallydownloaded.net/2020/02/developer-q-a-monster-train-a-deckbuilding-roguelike-with-a-hellish-theme.html) | Mark Cooke, 2020 | Pick rate и WR по связкам кланов, «карты, которые никто не берёт» |
| [LoR: подход к балансу и патч 1.2](https://www.invenglobal.com/articles/11264/legends-of-runeterra-patch-12-balances-new-mechanics-from-rising-tides) | Inven Global со ссылкой на Riot, 2020 | Входы баланса и цель «у каждой карты есть дом» |
| LoR Dev Notes: approach to balance in Set 1 | Riot, 2020 `[не проверено]` | Цикл трёх балансных патчей на сет; playruneterra.com рендерится только через JS, копии в Wayback Machine нет |
| [RubinZoo о балансе LoR](https://outof.games/news/2215-riots-rubinzoo-discusses-recent-runeterra-card-changes-card-balance-design-process-and-more/) | Steve Rubin, 2020 | Нерф Lee Sin за фрустрацию при WR около 53% |

### Источники: настольные ККИ, LCG, колодостроители, франшизные ККИ

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [The Secret History of Dominion](https://dominionstrategy.com/2013/06/24/the-secret-history-of-dominion/) | Donald X. Vaccarino, 2013; серия статей, начиналась на BGG и BoardGameNews | История каждой карты, происхождение жанра deckbuilding |
| [Dominion Outtakes](https://dominionstrategy.com/2013/06/24/dominion-outtakes/) | Vaccarino, 2013 | Отброшенные дизайны с причинами отказа |
| [Interview with Donald X. Vaccarino, Part II: Dominion](https://dominionstrategy.com/2012/12/21/interview-with-donald-x-vaccarino-part-ii-dominion/) | dominionstrategy.com, 2012 | Процесс плейтестов, модульное королевство |
| Заметки о переосмыслении Android: Netrunner как LCG | Lukas Litzsinger, FFG, около 2012 `[не проверено]`, ссылка мертва | «Не поменять ничего — устареть; поменять слишком много — потерять суть» |
| [The Enigmatic Architect](https://www.fantasyflightgames.com/en/news/2018/8/22/the-enigmatic-architect/) | FFG, Richard Garfield, 2018 | KeyForge: колоды из алгоритма |
| [Luck vs Skill with Richard Garfield](https://boardgamedesignlab.com/luck-vs-skill-with-richard-garfield/) | Board Game Design Lab | Удача расширяет аудиторию |
| [Game Designers in Detail: Richard Garfield](https://gamecenter.nyu.edu/game-designers-in-detail-richard-garfield/) | NYU Game Center, 2012 | Удача и внешняя мета-игра ККИ |
| [Flesh and Blood creator — интервью](https://articles.starcitygames.com/flesh-and-blood/flesh-and-blood-creator-talks-living-legend-format-rosetta-design-uzuri-winning-the-pro-tour/) | James White, около 2024 | Living Legend: «пенсия» героев вместо ротации |
| [Revealing Cycles](https://legacy.fabtcg.com/en/articles/revealing-cycles/) | Legend Story Studios, 2019 | Pitch-система, таблица cost–pitch–power |
| [Gwent overhaul](https://engadget.com/2018/04/14/gwent-card-game-overhaul) | Jon Fingas, Engadget, 14.04.2018 | Кейс полной переделки живой ККИ: план на полгода, сокращение рядов |
| [ONE PIECE CARD GAME Comprehensive Rules (PDF)](https://en.onepiece-cardgame.com/pdf/rule_comprehensive.pdf), [страница правил](https://en.onepiece-cardgame.com/rules/) | Bandai; v1.2.1 от 28.08.2026 (до неё v1.2.0 от 16.01.2026, v1.1.9 от 17.10.2025) | Первоисточник по DON!!, лидеру, Life, Counter, Trigger; там же Tournament Rules Manual (16.01.2026) |
| [Disney Lorcana Comprehensive Rules 2.2.0 (PDF)](https://files.disneylorcana.com/Comprehensive-Rules_2.2.0-EN.pdf) | Ravensburger, действует с 09.07.2026 | Inkwell как ход раз в ход (4.2), победа на 20 лора; живой документ, свежая версия — на странице Resources |
| [Star Wars: Unlimited Comprehensive Rules v8.0 (PDF)](https://cdn.starwarsunlimited.com//SWH_Comp_Rules_v8_0_e26603c6e1.pdf) | FFG, 08.07.2026 | Подготовка с двумя ресурсами, фаза перегруппировки, initiative |
| [Learn How to Build a Deck in Pokémon TCG Pocket](https://www.pokemon.com/us/strategy/learn-how-to-build-a-deck-in-pokemon-tcg-pocket) | pokemon.com, 30.01.2025 | Официально: колода 20 карт, не больше 2 копий, Energy Zone, 3 очка |
| [Exclusive Interview with Disney Lorcana TCG Designer](https://disneyparksblog.com/products/exclusive-interview-with-disney-lorcana-trading-card-game-designer/) | Ryan Miller, Disney Parks Blog, около 2023–2024 | Цели дизайна и аудитория |
| [Talking the magic of Disney Lorcana with co-designer Ryan Miller](https://checkpointgaming.net/features/2024/08/talking-the-magic-of-disney-lorcana-with-co-designer-ryan-miller) | Checkpoint Gaming, 2024 | Иммерсия как ориентир дизайна |
| [Shadowy Insights with Danny Schaefer](https://starwarsunlimited.com/articles/shadowy-insights-danny-schaefer) | FFG, 2024 | Сет как кусочек вселенной |
| [Danny Schaefer on a "feelings-first" approach](https://brandsuntapped.com/?p=11576) | Brands Untapped, около 2024 | Главный текст о передаче IP через механику |
| [Pokémon Trading Card Game Pocket](https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Trading_Card_Game_Pocket) | Bulbapedia, 2024– | Как франшиза упрощает ККИ под телефон (вторичный источник) |

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
{"run": 9001, "seed": 9001, "char": "Ironclad", "ascension": 5, "bot": "heuristic", "meta_level": "none", "win": false, "floor_died": 23, "killer": "Act2Boss", "duration_s": 2410}
```

| Метрика | Ключ или способ | Что показывает |
| --- | --- | --- |
| Кривая сложности | `rate:win@ascension=*` | Путь «новичок → эксперт» по ступеням |
| Стены сложности | `num:floor_died`, `rate:win@killer=*` или доля смертей по `killer` | Пики смертей на этажах и боссах |
| Честность RNG | `spread:win@seed_bucket` при одной стратегии бота | Дисперсия исхода по сидам |
| Проходимость генератора | `rate:solvable` по прогону валидатора; должна быть ровно 1.0 | Невыигрываемые уровни |
| Вклад мета-прогрессии | `rate:win@meta_level=*` (none против full) | Подменяет ли мета навык |
| Разнообразие билдов среди побед | Энтропия по архетипу билда; считается отдельно | Одна выигрышная стратегия |
| Длина и ритм | `num:duration_s`, время до первой смерти, забегов до первой победы | Соответствие длины забега частоте смертей |

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
{"player": "p07", "level": "1-3", "section": "B", "time_s": 74, "deaths": 2, "lost": false, "main_path_unaided": true, "secret_found": false, "quit": false}
```

- `num:time_s@section=*` против плана из beat chart.
- `rate:main_path_unaided` — нашли главный путь без подсказки; `rate:secret_found` — секреты.
- `rate:quit@section=*` — где бросают уровень; `rate:lost@section=*` — долгая стоянка или бэктрекинг.
- Тепловые карты смертей и застреваний по координатам — считается отдельно.

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
| Half-Life 2 Developer Commentary | Valve, 2006–2007, в игре `[не проверено]` | Сигналы, направление взгляда, обучение без текста |

## 5. Нарративный дизайн

### Ключевые принципы

- **Структура под реиграбельность.** Quality-based и salience-based структуры, storylets и waypoint-нарратив масштабируются лучше дерева ветвлений (Emily Short, 2016).
- **Окружение и системы рассказывают сами.** Environmental storytelling: следы событий, выводы игрока (Smith & Worch, 2010). Системный нарратив из модульных «кирпичиков» (Ken Levine, Narrative Legos, 2014).
- **Без лудонарративного диссонанса.** Механики и сюжет говорят одно (Clint Hocking, 2007).
- **Инструменты для писателя.** ink и Yarn Spinner позволяют итерировать без программиста; Yarn Spinner поддерживает Godot.
- **В карточных играх** карта — микрорассказ: имя, арт, механика и flavor text вместе. Мета-нарратив (Inscryption) и нарратив через смерть (Hades) встраивают сюжет в реиграбельный жанр. Навыки как голоса-персонажи и провал как контент — Disco Elysium `[не проверено]`.

### Типичные ошибки

- Экспоненциальное ветвление: контент, который видит 5% игроков.
- Сюжет в катсценах, оторванный от механик.
- Flavor text, противоречащий механике карты.

### Что мерить

Строка на игрока в узле выбора и строка на сцену:

```json
{"player": "p07", "node": "ch2_dock", "option": "B", "scene_skipped": false, "read_time_s": 41}
```

- Распределение `option` по узлу: выбор, который делают 95% игроков, ложный (считается отдельно по долям).
- `rate:scene_skipped@scene=*`, `num:read_time_s` — пропуск и чтение.
- Доля увиденного контента на игрока — `num:content_seen_share` в строке сессии.
- Опрос: могут ли игроки пересказать мотивы персонажей.

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
| Disco Elysium: доклады и разборы | ZA/UM, 2019–2020 `[не проверено]` | Навыки как голоса, провал как контент |

## 6. Стратегии и тактика

### Ключевые принципы

- **Интересные решения** (Sid Meier, GDC 2012). У каждого варианта есть цена. Плохие решения — очевидные, случайные и принимаемые без информации.
- **Вода находит трещину** (Soren Johnson, 2011). Игроки оптимизируют и эксплуатируют любую дыру и не ценят своё время: отсюда микроменеджмент и гринд. Доминирующие стратегии ищут до релиза.
- **Тема поддерживает, смысл в механике** (Johnson, Theme is Not Meaning).
- **Детерминизм и полная информация** (Into the Breach: намерения врагов видны, поле 8×8, защита зданий вместо килл-рейса) против случайности с воспринимаемой справедливостью (XCOM `[не проверено]`; Johnson, Playing the Odds).
- **Борьба со снежным комом**: догоняющие механики, издержки расширения. Паттерны — [mechanics-patterns.md](mechanics-patterns.md#6-темп-и-длительность).

### Типичные ошибки

- Доминирующая стратегия, «единственный путь».
- Обязательный микроменеджмент; скучная оптимальная игра.
- Снежный ком: исход ясен за час до конца.
- ИИ, который легко эксплуатировать или который заметно читерит.

### Что мерить

Одна строка на игрока в партии:

```json
{"match": 310, "seed": 310, "faction": "Rome", "strategy": "wide", "bot": "mcts", "win": true, "turns": 142, "leader_at_mid": true, "empty_turns": 6, "decisions_per_turn": 4.2}
```

- `rate:win@faction=*`, `rate:win@strategy=*` — перекосы; энтропия выборов — считается отдельно.
- `rate:win@leader_at_mid=true` — предсказуемость исхода. Если лидер на середине выигрывает больше чем в 90% партий, это снежный ком (ориентир из заметок).
- `num:empty_turns`, `num:decisions_per_turn`, время хода — пустые ходы и перегрузка.
- Эксплойты: ограниченные и поисковые боты из [стенда](pipeline.md#этап-7-измерительный-стенд), фаззинг симуляции.

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Water Finds a Crack](https://www.designer-notes.com/game-developer-column-17-water-finds-a-crack/) | Soren Johnson; Game Developer, 2011 | Игроки эксплуатируют любые дыры |
| [Theme is Not Meaning, Part I](http://www.designer-notes.com/?p=237), [Part II](http://www.designer-notes.com/?p=240) | Soren Johnson, около 2010 | Смысл игры в механиках, а не в теме |
| [Seven Deadly Sins for Strategy Games](http://www.designer-notes.com/?p=106), [Sid's Rules](http://www.designer-notes.com/?p=119), [Playing the Odds](http://www.designer-notes.com/?p=171), [When Choice is Bad](http://www.designer-notes.com/?p=609) | Soren Johnson, Design of the Times | Грехи стратегий, восприятие вероятностей, вредный выбор |
| [Designer Notes](https://www.designer-notes.com/) | Soren Johnson, подкаст, 2014– | Интервью с дизайнерами о решениях |
| [Interesting Decisions](https://www.gdcvault.com/play/1015756/) | Sid Meier, GDC 2012 | Игра как серия интересных решений |
| [Sid Meier's Memoir!](https://wwnorton.com/books/9781324005872) | Sid Meier; W. W. Norton, 2020 (соавтор `[не проверено]`) | Уроки Civilization и Pirates! |
| ['Into the Breach' Design Postmortem](https://www.gdcvault.com/play/1025772/) | Matthew Davis, GDC 2019 | Полная информация, решения вместо догадок |
| Доклады о XCOM: Enemy Unknown | Jake Solomon, Firaxis, около 2013 `[не проверено]` | Переосмысление классики, восприятие процентов попадания |

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
- Задержка ввода и окна прощения в кадрах — замеряются в движке отдельно и фиксируются в спецификации.

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Game Feel: A Game Designer's Guide to Virtual Sensation](https://www.routledge.com/Game-Feel-A-Game-Designers-Guide-to-Virtual-Sensation/Swink/p/book/9780123743282) | Steve Swink; CRC, ©2009 | Определение game feel и метрики отзывчивости |
| [Celeste & Forgiveness](https://maddymakesgames.com/articles/celeste_and_forgiveness/index.html) | Maddy Thorson (оригинал на Medium, год `[не проверено]`) | Десять механик прощения — чек-лист платформера |
| [Juice It or Lose It](https://www.gdcvault.com/play/1016487/) | Martin Jonasson, Petri Purho; GDC Europe 2012 | Эффекты превращают прототип в «сочный» |
| [The art of screenshake](https://www.youtube.com/watch?v=AJdEqssNZ-U) | Jan Willem Nijman, 2013 | Пошаговое усочнение шутера |
| [Embracing Push Forward Combat in DOOM](https://gdcvault.com/play/1024940/Embracing-Push-Forward-Combat-in) | Kurt Loudy, Jake Campbell; GDC 2018, запись есть на канале GDC | Роли врагов и ресурсы, которые толкают вперёд |
| Доклады и разборы God of War (2018) и Hollow Knight | `[не проверено]` | Камера и комбо; читаемость атак и честность урона |

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
{"player": "p11", "level": 14, "solved": true, "time_s": 380, "hints": 1, "quit": false, "intended": false}
```

- `num:time_s@level=*` — скачки сложности по порядку уровней.
- `rate:quit@level=*`, `num:hints@level=*`.
- `rate:intended@level=*` — решено задуманным способом. Непредусмотренные решения («дыры») ищет автоматический солвер.

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

- **Много жизнеспособных стратегий важнее идеального равенства** (Sirlin, Balancing Multiplayer Competitive Games, 2009). Это обязательное чтение для ККИ с соревновательным режимом.
- **Рейтинг с неопределённостью.** Для дуэлей 1×1, в том числе ККИ, подходят Glicko-2 (рейтинг, отклонение RD и волатильность; public domain) или OpenSkill (открытая альтернатива TrueSkill, быстрее, поддерживает несколько команд). Для команд — TrueSkill-класс; TrueSkill 2 учитывает индивидуальные показатели и быстрее калибрует новичков.
- **Поведение формируется дизайном**: обратная связь о наказании, прайминг, прозрачность (Jeffrey Lin, Riot, 2013).
- **Ranked anxiety** снижают видимым прогрессом, защитой от потери ранга и сменой режима. Это общая практика; первоисточник не найден `[не проверено]`.

### Типичные ошибки

- Elo без неопределённости: долгая калибровка, смурфы.
- Матчмейкинг, оптимизирующий только время очереди.
- Наказания без объяснения причины, отсюда рецидивы.

### Что мерить

Одна строка на игрока в рейтинговом матче:

```json
{"match": 55012, "rating_bucket": "gold", "predicted_win": 0.53, "rating_gap": 41, "queue_s": 38, "went_first": false, "win": true, "loss_streak_before": 3, "churned_7d": false, "reported": false}
```

| Метрика | Ключ или способ | Что показывает |
| --- | --- | --- |
| Качество матча | `num:predicted_win` (медиана около 0.5), `num:rating_gap` | Честность подбора |
| Очередь | `num:queue_s@rating_bucket=*` (p90 для краёв распределения) | Цена качества подбора |
| Отток после поражений | `rate:churned_7d@loss_streak_before=*` | Ranked anxiety и фрустрация |
| Токсичность | `rate:reported`, доля рецидивов; доля матчей с токсичным чатом | Работает ли система наказаний |
| Для ККИ | `rate:win@went_first=true` в ранкеде, разнообразие меты `deck` по `rating_bucket` | Баланс на высоком уровне игры |

Распределение игроков по рангам — считается отдельно.

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
- **ESRB с 13.04.2020 ставит пометку «In-Game Purchases (Includes Random Items)»** на рандомизированные покупки: лутбоксы, гачу и **бустеры карт**. Цифровая ККИ с платными паками получит эту пометку.

### Ключевые принципы

- **Прозрачность.** Шансы выпадения и цена в реальных деньгах видны. Минимум промежуточных валют.
- **Монетизировать удобство и самовыражение** (косметика, battle pass с честной ценой), а не снятие созданной боли.
- **Предсказуемый сезонный ритм.** Battle pass достижим за разумное время игры.
- **Для ККИ**: детерминированный путь к любой карте (крафт, обмен), защита от дубликатов, гарантия редкой карты после N паков (pity), бесплатные колоды для новичков, учёт пометки ESRB.
- **Защита уязвимых**: лимиты трат, никаких ante-механик на реальные деньги.
- **Список того, чего не делать** — каталог Shokrizade (2013): промежуточные валюты, «fun pain», мягкие и жёсткие гейты, отъём награды, ante-игры. Модели источников и стоков — в [systems-balance.md](systems-balance.md), паттерны — в [mechanics-patterns.md](mechanics-patterns.md#13-экономика-и-монетизация).

### Типичные ошибки

- «Fun pain»: создать фрустрацию и продавать её снятие.
- Скрытые шансы и непрозрачная цена через гемы.
- Гача-бустеры без гарантии (pity).
- Сила за деньги в соревновательной ККИ: pay-to-win разрушает ранкед.

### Что мерить

Одна строка на игрока в когорте:

```json
{"player": "u4411", "cohort": "2026-10-w2", "d1": true, "d7": true, "d30": false, "payer": false, "spend_usd": 0, "days_to_competitive_deck": 19, "rank_bucket": "diamond", "refund": false}
```

| Метрика | Ключ или способ | Что показывает |
| --- | --- | --- |
| Удержание | `rate:d1@cohort=*`, `rate:d7@cohort=*`, `rate:d30@cohort=*` | Здоровье живой игры |
| Конверсия | `rate:payer`; ARPDAU — считается отдельно | Доля платящих |
| Концентрация выручки | Доля выручки от верхнего процента плательщиков — считается отдельно | Зависимость от «китов»: красный флаг этики |
| Путь бесплатного игрока | `num:days_to_competitive_deck@payer=false` | Сколько дней игры до конкурентной колоды бесплатно |
| Pay-to-win | `rate:payer@rank_bucket=*` | Есть ли бесплатные игроки в топ-рангах |
| Сожаление | `rate:refund`, жалобы, время до первой покупки | Покупки, о которых жалеют |

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
| Отчёт Бельгийской комиссии по азартным играм о лутбоксах | регулятор, 2018 `[не проверено]` | Основание бельгийского запрета |
| [Loot boxes in FIFA toch géén verboden kansspel](https://www.dirkzwager.nl/kennis/artikelen/loot-boxes-in-fifa-toch-geen-verboden-kansspel-dwangsom-onterecht-opgelegd) | Dirkzwager, 01.04.2022 (на нидерландском) | Разбор решения Государственного совета Нидерландов ECLI:NL:RVS:2022:690 по делу EA |

## 11. Мобильные и казуальные

- **Принципы**: сессия 2–5 минут, игра одной рукой в вертикальной ориентации, прерываемость, онбординг без текста. Мобильная ККИ строится вокруг гарантированно короткой партии (Marvel Snap) и упрощённых систем (Pokémon Pocket: колода 20, Energy Zone, без муллиганов).
- **Ошибки**: перенос длинных партий и сложного ресурса с ПК, обучение текстом.
- **Что мерить**: строка на сессию `{"player", "session_s", "sessions_today", "ftue_step"}` → `num:session_s`, `num:sessions_today`; воронка обучения по `ftue_step` (считается отдельно) и `rate:finished_tutorial`.

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Deconstructor of Fun](https://www.deconstructoroffun.com/) | 2012–2026 | Разборы мобильных хитов |
| [Designing MARVEL SNAP](https://gdcvault.com/play/1029024/Designing-MARVEL-SNAP) | Ben Brode, GDC 2023 | Мобильная ККИ с короткими сессиями |
| [Pokémon Trading Card Game Pocket](https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Trading_Card_Game_Pocket) | Bulbapedia, 2024– | Упрощение ККИ под телефон |
| Free-to-Play: Making Money From Games You Give Away | Will Luton; New Riders, 2013 | Базовая экономика F2P |

## 12. Кооперативные

- **Принципы**: главная проблема — «альфа-игрок», который играет за всех. Лекарства — скрытая информация, ограничение коммуникации (Hanabi), одновременные решения, личные цели. Игра выступает общим противником с нарастающей угрозой (Pandemic).
- **Ошибки**: полная открытая информация без ограничений общения — один игрок решает за всех; угроза без нарастания.
- **Что мерить**: строка на команду в партии `{"difficulty", "players", "win", "alpha_share"}` → `rate:win@difficulty=*`, `rate:win@players=*`; `num:alpha_share` — доля решений, принятых одним игроком, по наблюдению на плейтесте.

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| Доклады и интервью о Pandemic и Forbidden Island | Matt Leacock, 2008– `[не проверено]` | Проблема альфа-игрока и лекарства |
| Building Blocks of Tabletop Game Design | Geoffrey Engelstein, Isaac Shalev; CRC, 1-е изд. 2019, 2-е 2022, актуальное 3-е — июль 2026 ([books.md](books.md)) | Энциклопедия механизмов, включая кооперативные структуры |
| [Hanabi](https://en.wikipedia.org/wiki/Hanabi_(card_game)) | Antoine Bauza, 2010; Spiel des Jahres 2013 | Кооператив с ограниченной коммуникацией: свои карты не видны, подсказки стоят жетонов |

## 13. Настольные

- **Принципы**: правила — интерфейс, и ясность важнее полноты. Мало downtime между ходами, короткий сетап, масштабируемость по числу игроков. Удача расширяет аудиторию: слабый иногда выигрывает, а серия партий или турнир компенсирует случайность (Garfield). Модульность даёт реиграбельность без новых правил (Dominion).
- **Ошибки**: правила, которые нельзя понять без автора за столом; долгий простой в ожидании хода; игра, которая работает только на одном числе игроков.
- **Что мерить**: строка на партию плейтеста `{"players", "blind", "duration_min", "setup_min", "downtime_min", "rules_questions"}` → `num:duration_min@players=*`, `num:setup_min`, `num:downtime_min@players=*`, `num:rules_questions@blind=true`. Слепой плейтест (без автора) — главный тест правил. Методы — в [playtesting-metrics.md](playtesting-metrics.md).

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
{"match": 812, "char": "Ryu", "opp_char": "Guile", "rating_bucket": "diamond", "win": true, "max_combo_dmg_share": 0.42, "comeback": false, "rollback_frames_p95": 3, "input_delay_frames": 1, "rage_quit": false}
```

| Метрика | Ключ или способ | Что показывает |
| --- | --- | --- |
| Матчап-чарт | `rate:win@char=*,opp_char=*`, `spread:win@char` | Перекошенные матчапы; зеркала исключать |
| Баланс по уровню | `rate:win@char=*,rating_bucket=*` | Персонаж силён только у новичков или только у топов |
| Урон одной связки | `num:max_combo_dmg_share@char=*` | Доля здоровья за одну ошибку: «касание = смерть» |
| Камбэк | `rate:comeback` | Снежный ком или избыточный перпетуальный камбэк |
| Качество сети | `num:rollback_frames_p95`, `num:input_delay_frames` | Насколько онлайн отличается от офлайна |
| Фрустрация | `rate:rage_quit@opp_char=*` | Персонажи, против которых «бесит играть» |

Пороги — рабочие ориентиры проекта, а не цитаты источников.

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
{"player": "u77", "day": "2026-10-19", "gold_in": 5400, "gold_out": 3100, "guild_size": 41, "griefed": false, "owns_house": true, "churned_30d": false}
```

- Баланс источников и стоков: сумма `gold_in` против `gold_out` по дням и медианный запас валюты — считается отдельно. Устойчивый рост запаса — сигнал инфляции.
- `rate:churned_30d@owns_house=*`, `rate:churned_30d@guild_size_bucket=*` — удерживают ли владение и сообщество.
- `rate:griefed` и доля жалоб — работает ли защита от гриферства.
- Смесь типов игроков — опросом по Bartle, отдельно.

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
- `rate:noticed@event=*` — какие системы работают «впустую».

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
- Физиология (пульс, кожная проводимость) — считается отдельно; поля и пороги здесь — предложение, а не цитаты источников.

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
- Время кадра и доля пропущенных кадров — замеряются в движке отдельно.

### Источники

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Locomotion best practices](https://developers.meta.com/horizon/design/locomotion-best-practices/) | Meta, обновлено 17.12.2025 | Повороты, ускорения, частота кадров, пресеты комфорта |
| [Locomotion comfort and usability](https://developers.meta.com/horizon/design/locomotion-comfort-usability/) | Meta, обновлено 17.12.2025 | Векция, скорости аватара, виньетки |
| [Valve deep dive: Half-Life: Alyx locomotion](https://uploadvr.com/valve-deep-dive-locomotion/) | Ian Hamilton, UploadVR, 06.04.2020, о видео Valve | Blink, Shift, Continuous; проверка точки прибытия; звук шагов |
| [Owlchemy Labs Case Study: Lessons Learned from JOB to VACATION](https://developers.meta.com/horizon/blog/owlchemy-labs-case-study-lessons-learned-from-job-to-vacation/) | Devin Reimer, Andrew Eiche; 23.04.2019 | Руки, зоны телепорта, комфорт, доступность |
| [Simulator Sickness Questionnaire](https://doi.org/10.1207/s15327108ijap0303_3) | Kennedy, Lane, Berbaum, Lilienthal; International Journal of Aviation Psychology, 1993 | Стандартный опросник укачивания для плейтестов |

## 19. Расхождения и пробелы

1. **Философии баланса цифровых ККИ расходятся.** Hearthstone (2014): минимум правок после релиза. Legends of Runeterra (2020): ежемесячные правки, у каждой карты есть дом. Marvel Snap (2023): OTA-правки чисел каждые две недели, переделки способностей — патчами раз в четыре недели. Это разные модели доверия к коллекции; для своей игры выбор записывается в опоры.
2. **Power creep.** «Лестница Эшера» подтверждена Rosewater (Blogatog, 15.11.2019), но то, что общий уровень силы действительно не растёт, — позиция WotC, и комментаторы с ней спорят.
3. **Числовых ориентиров в первоисточниках почти нет.** Пороги вроде «WR выше 55% в матрице матчапов», «лидер на середине выигрывает больше 90%» или «нет ходов к ходу 3–4» — рабочие эвристики, а не цитаты. Коридоры ставятся на этапе 2 [пайплайна](pipeline.md#этап-2-опоры-и-целевые-метрики) и помечаются как предположение, если нет референса. Исключения с числами из источников: скорости аватара в VR (Meta) и 8 кадров отката за 16 мс (NetherRealm).
4. **One Piece Card Game — сверено с официальными правилами.** Актуальна Comprehensive Rules v1.2.1 от 28.08.2026; v1.2.0 вышла 16.01.2026 (фанатская дата 09.01.2026 неверна). Детали DON!! в разделе 2.2 сверены с текстом правил. Уточнение к заметкам: запрет боя на первом ходу действует для обоих игроков, а компенсация первого хода — это отсутствие добора и 1 DON!! вместо 2.
5. **Дизайн-интервью о ресурсах франшизных ККИ не найдены.** Правила Lorcana (2.2.0), Star Wars: Unlimited (v8.0) и базовые правила Pokémon Pocket (pokemon.com) сверены с официальными источниками, но объяснений дизайнеров, почему ресурс устроен именно так, нет. Скамейка 3 и отсутствие муллигана в Pocket — только по Bulbapedia.
6. **Уточнения названий и дат.** У Soren Johnson статья называется «Theme is Not Meaning» (Design of the Times #11–12). «The Secret History of Dominion» — серия статей, а не книга. «Timmy, Johnny, and Spike Revisited» вышла в 2006 году. Блог Hocking переехал с Typepad на clicknothing.com. GDC-доклада Ben Brode о Hearthstone 2014 года не найдено: на GDC 2014 о Hearthstone выступали Eric Dodds (дизайн) и Ben Thompson (арт). Доклад Hagman на GDC 2025 подтверждён только 4Gamer. Gwent: Engadget (2018) сообщал о плане на полгода и о том, что удаление ряда только рассматривается. Доклад Dan Taylor — GDC 2013 по Game Developer, а не GDC Europe. Доклад DOOM делали Kurt Loudy и Jake Campbell. Magic CR обновлены 25.09.2026; приоритет в них — пункт 117, а не 405.
7. **Осталось непроверенным** (помечено `[не проверено]`): цикл трёх патчей на сет и Dev Notes LoR, доля переработанных карт в Gwent и время удаления ряда, термин GIH WR у 17lands, статья FFG о Netrunner, Half-Life 2 Developer Commentary, Disco Elysium, XCOM (Solomon), доклады о God of War и Hollow Knight, год Celeste & Forgiveness, соавтор мемуаров Sid Meier, материалы Riot о ranked anxiety, отчёт Бельгийской комиссии по азартным играм, доклады Matt Leacock.
8. **Мёртвые и ограниченные ссылки.** Статья FFG о Netrunner — 404. Оригинал Celeste & Forgiveness на Medium недоступен, используется копия на maddymakesgames.com; даты на ней нет. playruneterra.com отдаёт пустую страницу без JS, а в Wayback Machine копии патч-нотов 1.2 нет. Страница доклада Marvel Snap на GDC 2024 в расписании GDC отдаёт 403. Сайт Frictional Games не показывает старые посты Thomas Grip, используются перепечатки на Game Developer.
9. **Пробелы по жанрам.** Разделы 14–18 дают по 4–7 проверенных источников на жанр, но это вводный уровень: нет собственных метрик-ориентиров для файтингов, MMO-экономик и хоррора, нет первоисточников Mike Zaimont (только пресса и Wikipedia) и Valve о Half-Life: Alyx (только пересказ UploadVR видео Valve). По кооперативным, мобильным и настольным играм материал по-прежнему короткий. Если проблема выходит за рамки этих разделов, в карточке гипотезы пишите, что решения в библиотеке нет, а общие паттерны берите из [mechanics-patterns.md](mechanics-patterns.md) и [systems-balance.md](systems-balance.md).
