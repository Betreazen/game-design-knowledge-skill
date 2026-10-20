# Документация, прототипирование и продакшн

Какие документы нужны игре, как их писать, чтобы их читали люди и исполняли ИИ-агенты, как прототипировать и как вести проект до релиза. Готовые шаблоны лежат в [assets/](../assets/); здесь — правила, структуры и источники.

- [1. Главный принцип: короткие документы, подробные спецификации](#1-главный-принцип-короткие-документы-подробные-спецификации)
- [2. Карта документов](#2-карта-документов)
- [3. Концепт, one-sheet и питч](#3-концепт-one-sheet-и-питч)
- [4. Опоры дизайна](#4-опоры-дизайна)
- [5. Живой GDD](#5-живой-gdd)
- [6. Спецификация фичи для программиста и ИИ-агента](#6-спецификация-фичи-для-программиста-и-ии-агента)
- [7. Правила карточной игры в стиле comprehensive rules](#7-правила-карточной-игры-в-стиле-comprehensive-rules)
- [8. Core loop, карта систем и данные баланса](#8-core-loop-карта-систем-и-данные-баланса)
- [9. Техническая документация: TDD, ADR, RFC](#9-техническая-документация-tdd-adr-rfc)
- [10. Прототипирование](#10-прототипирование)
- [11. Этапы продакшна и критерии выхода](#11-этапы-продакшна-и-критерии-выхода)
- [12. Продакшн для соло и малой команды](#12-продакшн-для-соло-и-малой-команды)
- [13. Источники](#13-источники)
- [14. Расхождения в источниках](#14-расхождения-в-источниках)

## 1. Главный принцип: короткие документы, подробные спецификации

Толстый GDD-«библия», который пишут до игры и никто не читает, устарел. Против него выступают Librande (One-Page Designs, GDC 2010), Sweatman (Jagex, 2014) и Derek Yu («Finishing a Game», 2010: «дизайн-доки не считаются за начало игры»). За подробные документы — Tim Ryan (1999) и Spolsky (2000): «проектировать прозой — минуты, кодом — недели».

Противоречие снимает оговорка самого Sweatman: центральный подробный документ нужен, когда исполнитель внешний — аутсорс, другая студия. **ИИ-агент — именно такой исполнитель.** Поэтому:

- верхний уровень короткий: one-sheet, опоры, one-page designs, карта систем;
- на каждую фичу — подробная самодостаточная спецификация с правилами, примерами и критериями приёмки;
- решения записываются отдельно от описаний, в журнал решений;
- каждый документ отвечает на один вопрос для одного читателя (Librande, Cain, Ubl). Документ, который не читают, хуже, чем никакой.

Spec-driven development (GitHub Spec Kit 2025, Kiro, Claude Code best practices) формулирует то же для агентов: «намерение — источник правды». Если оно не записано, агент пишет правдоподобный, но не тот код.

## 2. Карта документов

| Документ | Объём | Когда | Шаблон |
| --- | --- | --- | --- |
| One-sheet (концепт) | 1–2 стр. | До прототипа: делаем или нет | [assets/one-pager.md](../assets/one-pager.md) |
| Опоры дизайна | полстраницы | Вместе с концептом; пересматриваются редко | там же |
| Целевые метрики | полстраницы + `targets.json` | После опор, до стенда | [assets/targets.example.json](../assets/targets.example.json) |
| Prototype brief | полстраницы | Перед каждым прототипом | [assets/prototype-brief.md](../assets/prototype-brief.md) |
| Core loop / карта систем | 1 лист | Препродакшн | раздел 8 |
| Спецификация фичи | 1–3 стр. | Перед реализацией каждой фичи | [assets/feature-spec.md](../assets/feature-spec.md) |
| Правила игры (comprehensive rules) | растёт с игрой | Карточные, настольные, пошаговые игры | раздел 7 |
| Таблицы данных + схема | — | Всегда, когда есть контент | раздел 8 |
| План плейтеста | 1 стр. | Перед каждым плейтестом | [assets/playtest-plan.md](../assets/playtest-plan.md) |
| Журнал решений (ADR/DDR) | 1 стр. на решение | При каждом неочевидном решении | раздел 9 |
| Журнал дизайна (баланс) | строка на гипотезу | Цикл улучшения в пайплайне | [assets/design-log.md](../assets/design-log.md) |
| TDD | 1–20 стр. | Крупная техническая система с альтернативами | раздел 9 |
| Питч издателю | 15–20 слайдов | Поиск финансирования | раздел 3 |
| Premortem / postmortem | 1–2 стр. | Начало и конец проекта или майлстоуна | раздел 12 |
| CLAUDE.md / AGENTS.md | коротко | Как только в проекте работает агент | раздел 6 |

## 3. Концепт, one-sheet и питч

**One-sheet** (Ryan 1999, Ismail/Vlambeer 2014, Tim Cain 2023):

1. Одно предложение: «Это игра, в которой…» — название, жанр, сеттинг, изюминка, платформа. Правило Ismail: если не получается сказать одним предложением, идея ещё не готова.
2. Сеттинг в 1–2 предложениях, с твистом (Cain: порядок сеттинг → история → системы, механики подчинены сеттингу).
3. Опыт игрока во втором лице, без меню и кнопок: несколько абзацев о том, что игрок делает и чувствует.
4. Ключевые особенности: список не длиннее страницы.
5. Жанр, платформы, аудитория, длина сессии.
6. Опоры дизайна (раздел 4).
7. Референсы: что берём из каждой игры и чем отличаемся.

**Питч издателю** — 15–20 слайдов на 10–15 минут ([Ismail, Pitch Template, 2023](https://ltpf.ramiismail.com/pitch-template/); [Sazhin, 2020](https://www.gamedeveloper.com/business/pitching-your-game-to-a-publisher-tips-and-advice); [Ahearn, 2006](https://www.gamedeveloper.com/business/the-game-proposal-part-two-the-contents)):

1. Хук: одно предложение и сильнейший визуал или геймплейное видео первым.
2. Команда: что выпускали и почему доделаете.
3. Почему эта игра и почему сейчас.
4. Игра: USP, core loop, текущее состояние, стек.
5. Билд или видео. Демо — самое важное (Ahearn).
6. Бизнес-кейс: сравнение минимум с пятью конкурентами, аудитория, маркетинг.
7. Скоуп, бюджет, сроки, майлстоуны.
8. Риски и план их снятия (Sazhin).
9. Что нужно от издателя.

Конкретика вместо баззвордов, не обещать лишнего. Показывать рано, но выбирать, что показать: без недоделанных ассетов.

## 4. Опоры дизайна

Опоры (pillars) — фильтр решений: «служит ли фича опоре? Нет — режем».

- 3–5 коротких фраз о **переживании игрока**, а не о фичах. Destiny: «A world players want to be in» ([Game Informer, 2013](https://gameinformer.com/b/features/archive/2013/12/11/jason-jones-the-destiny-interview)).
- Под каждой опорой 2–3 тест-вопроса, которые можно задать к любой фиче. У Destiny: «Is this world cool? Do I want to stay here?».
- **Анти-опоры**: чем игра не является. Это аналог non-goals у Ubl и No Gos в Shape Up.
- Каждая измеримая опора получает метрику и целевой коридор, см. [pipeline.md](pipeline.md#этап-2-опоры-и-целевые-метрики).
- Пример вырезанной из-за опоры фичи показывает команде и агенту, что опоры работают.

Ловушка: опоры вида «бой / исследование / сюжет» (по пересказам, у God of War 2018) делят игру на части и не говорят, что их связывает. Лучше формулировать связь: «каждый бой продвигает отношения отца и сына». Hearthstone в первоисточнике (Dodds, GDC 2014, доклад «10 Bits of Design Wisdom») использовал не опоры, а 10 принципов дизайна: «Iterate Fast», «Simplify», «Keep It Deep», «Immediate Fun» и другие ([пересказ 80.lv](https://80.lv/articles/hearthstone-10-rules-of-great-design)).

## 5. Живой GDD

Не книга, а справочник: папка Markdown в репозитории или вики. Адаптация функциональной спецификации Ryan (1999) под модульность:

```text
design/
├── 00-vision.md          one-sheet + опоры + анти-опоры
├── 01-targets.md         целевые метрики и почему такие (+ targets.json)
├── 10-core-loop.md       петли и карта систем
├── 20-systems/<name>.md  по файлу на систему, по шаблону спецификации фичи
├── 30-content/           таблицы данных и их схемы
├── 40-ui/                поток экранов, требования, макеты
├── 50-art-audio/         цели и списки ассетов
├── 60-narrative/         сеттинг, история, персонажи
├── 70-levels/            уровни: эскиз → бумага → ядро → детали → плейтест
├── rules/                comprehensive rules (для карточных и настольных)
└── decisions/            журнал решений (ADR/DDR)
```

Правила: у каждого файла дата и статус; ссылки вместо копирования; устаревшее помечается, а не удаляется молча; документ обновляется до фактического поведения игры.

**Story bible для `60-narrative/`** (Anna Megill, Ubisoft Massive, Sweden Game Conference, [пересказ Game Developer, 2019](https://www.gamedeveloper.com/design/building-a-basic-story-bible-for-your-game)) — тоже живой документ: сводка на 2–3 абзаца → опоры и темы → ключевые объекты, события, локации предыстории → бой, экономика, маркетинг → референсы → тон, язык, персонажи → способы подачи истории игроку. Для `40-ui/` отдельного проверенного шаблона UI flow не найдено; ближайший ориентир — глава «Sign Language: UI, HUD, and Icon Design» в Level Up! 3rd ed.

## 6. Спецификация фичи для программиста и ИИ-агента

Шаблон: [assets/feature-spec.md](../assets/feature-spec.md). Сюда сходятся Spolsky, [Claude Code best practices](https://code.claude.com/docs/en/best-practices), [GitHub Spec Kit](https://github.com/github/spec-kit), [Kiro Specs](https://kiro.dev/docs/specs/), EARS, Gherkin и Shape Up.

1. **Зачем**: какой опоре служит. User story по Sweatman: «Как игрок, я могу X с помощью Y, чтобы почувствовать Z».
2. **Appetite**: сколько времени готовы потратить (Shape Up), а не оценка сроков.
3. **Правила**: нумерованные и атомарные (`R1`, `R1.a`), в шаблонах [EARS](https://alistairmavin.com/ears/):
   - `When <событие>, игра <реакция>` — событие;
   - `While <состояние>, …` — состояние;
   - `If <нежелательная ситуация>, then …` — ошибка или крайний случай;
   - `Where <опция включена>, …` — вариант правил.
4. **Примеры** в форме [Given / When / Then](https://martinfowler.com/bliki/GivenWhenThen.html) с конкретными картами и числами, включая крайние случаи: пустая колода, одновременные триггеры, нули, ничья. Для таблицы кейсов — Scenario Outline + Examples из [Gherkin](https://cucumber.io/docs/gherkin/reference/). Эти примеры становятся тестами на этапе 6 пайплайна.
5. **Данные**: какие таблицы и поля затронуты, где их схема.
6. **Интерфейс и обратная связь**: что игрок видит и слышит.
7. **Вне скоупа / No Gos / Rabbit holes** — что не делать, даже если хочется.
8. **Затрагиваемые файлы и интерфейсы** — для агента.
9. **Критерии приёмки**: проверяемые пункты pass/fail; последний — сквозная проверка (тест, безголовый прогон, скриншот).
10. **Открытые вопросы**: нерешённое не оставляется «на усмотрение» агента.

Практика с агентом: «опроси меня → SPEC.md», затем реализация в новой сессии с чистым контекстом, затем ревью диффа против спецификации отдельным агентом.

**«Проблема двери»** ([Liz England, 2014](https://lizengland.com/blog/2014/04/the-door-problem/)): одна дверь в игре порождает десятки решений — открывается ли, кем, видно ли, что заперта, что с ИИ врагов. Если спецификация их не перечисляет, их примет программист или агент.

**CLAUDE.md / AGENTS.md игрового проекта** ([agents.md](https://agents.md/)): ссылки на `00-vision.md` и правила, команды сборки, тестов и симуляций, где лежат спецификации, данные и ADR, запреты («не менять схему данных без ADR», «не трогать стенд замеров»). Для каждой строки спрашивайте: станет ли агент ошибаться без неё?

## 7. Правила карточной игры в стиле comprehensive rules

Образец — [MTG Comprehensive Rules](https://magic.wizards.com/en/rules): иерархическая нумерация (`601.2a`), глоссарий, разбор крайних случаев. Это справочник, а не учебник, и единый источник правды для движка правил и тестов.

- Разделы по образцу CR: 1xx — концепции (победа, игроки, зоны), 2xx — части карты, 3xx — типы карт, 4xx — зоны, 5xx — структура хода, 6xx — розыгрыш, способности, стек или очередь, 7xx — дополнительные правила (замещение, длительности), 8xx — варианты и мультиплеер, глоссарий.
- Каждое правило атомарно и адресуемо. Текст карт использует только термины глоссария (templating): одно понятие — одна формулировка.
- К правилу привязаны тест-кейсы с его номером: правило ↔ тест прослеживаются в обе стороны.
- Изменения правил проходят через ADR или RFC, а не правку на месте.
- Для франшизной ККИ, если у оригинала есть официальные правила (например, One Piece Card Game), сначала сверяйтесь с ними и фиксируйте отличия своей версии.

## 8. Core loop, карта систем и данные баланса

**Петли и дуги** ([Daniel Cook, Loops and Arcs, 2012](https://lostgarden.com/2012/04/30/loops-and-arcs/)): петля — модель игрока → действие → обратная связь → обновлённая модель, повторяется. Дуга — разорванная петля, потребляемый контент: сюжет, уровни. Диагностический вопрос: что повторяется, а что расходуется? Карта систем показывает петли разных масштабов (секунды, партия, мета-прогрессия), ресурсы с источниками, стоками и конвертерами, и skill atoms — чему учится игрок ([Cook, The Chemistry of Game Design, 2007](https://www.gamedeveloper.com/pc/feature-the-chemistry-of-game-design-)). Формат — один лист (Librande) или исполняемая модель в [Machinations](https://machinations.io/).

**Данные баланса — источник правды, а не иллюстрация:**

- карты и юниты — данные (JSON, RON, CSV, ресурсы движка), а не подклассы: паттерн [Type Object](https://gameprogrammingpatterns.com/type-object.html) у Nystrom;
- рядом с данными — схема: поле, тип, диапазон, единицы, значение по умолчанию, кто правит;
- кривые стоимости и формулы — в отдельной таблице-модели ([Schreiber, Game Balance Concepts](https://gamebalanceconcepts.wordpress.com/)), см. [systems-balance.md](systems-balance.md);
- валидация данных в CI даёт агенту проверку pass/fail;
- «ручки» для баланса закладываются в системы заранее ([Cook, 2023](https://lostgarden.com/2023/07/08/what-is-a-daniel-cook-game/)).

## 9. Техническая документация: TDD, ADR, RFC

**TDD** ([Malte Ubl, Design Docs at Google, 2020](https://www.industrialempathy.com/posts/design-docs-at-google/); Ryan 1999, часть 2):

1. Контекст и скоуп.
2. Цели и **не-цели**.
3. Дизайн: обзор, детали, поток данных и игровой цикл, хранение, эскизы API.
4. **Рассмотренные альтернативы** — по Ubl, самый важный раздел.
5. Сквозные вопросы: производительность, сохранения, сеть, детерминизм, платформы.
6. План тестирования и метрики.

Объём 10–20 страниц для крупной системы или мини-документ на 1–3 страницы. Не пишите TDD, если решение однозначно или документ превращается в инструкцию по реализации без компромиссов.

**ADR и журнал дизайн-решений** ([Nygard, 2011](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions)): файл `NNNN-название.md`, разделы Status (proposed, accepted, deprecated, superseded by NNNN), Context, Decision («Мы будем…»), Consequences. [MADR 4.0](https://adr.github.io/madr/) добавляет варианты с плюсами и минусами и способ подтверждения. Короткая форма — [Y-statement](https://www.infoq.com/articles/sustainable-architectural-design-decisions/): «В контексте X, столкнувшись с Y, мы выбрали Z, чтобы получить Q, приняв цену D». Тот же формат годится для решений по правилам и балансу: «почему у карты стоимость 3, а не 2». Записи не переписываются, а заменяются новыми.

**RFC** для крупного изменения правил или архитектуры — по образцу [Rust RFC](https://github.com/rust-lang/rfcs): черновик → обсуждение → период финальных комментариев (соло-разработчику достаточно дать идее «отлежаться» сутки) → принять, отклонить или отложить.

## 10. Прототипирование

Правила из [Gabler et al., How to Prototype a Game in Under 7 Days (2005)](https://www.gamedeveloper.com/game-platforms/how-to-prototype-a-game-in-under-7-days), [Hecker & Gingold, Advanced Prototyping (GDC 2006)](http://www.chrishecker.com/Advanced_Prototyping), [Juul (2005)](https://www.jesperjuul.net/ludologist/2005/10/29/how-to-prototype-a-game-in-under-7-days/), [Derek Yu (2010)](https://makegames.tumblr.com/post/1136623767/finishing-a-game), Librande:

1. **Один прототип — один вопрос**, timebox и критерий «убить или продолжать». Шаблон: [assets/prototype-brief.md](../assets/prototype-brief.md).
2. **Сначала игрушка, потом игра**: ядро должно быть приятным само по себе, затем добавляется цель.
3. **Подделывайте всё, что можно**: код прототипа никто не увидит.
4. **Тема и графика не спасают плохую механику**, но хорошую делают лучше.
5. **Бумага — самый дешёвый движок** для карточных игр и систем. Слайды Librande «Paper Prototypes of Spore», «Play it on Paper», «Paper Simulations of Digital Games» на [stonetronix.com](https://www.stonetronix.com/); Hearthstone тоже начинался на бумаге (Dodds, «Iterate Fast»).
6. **Самый нижний уровень «башни настройки»** (Hecker & Gingold): скрипт → горячая перезагрузка → данные → редактор → перекомпиляция. Каждый уровень выше дороже.
7. **Критика конкретного прототипа полезнее брейншторма** (Gabler et al.).
8. **Убивайте рано**, а новые большие идеи откладывайте на следующую игру (Yu).
9. **Длина**: Gabler et al. — до 7 дней в одиночку. Juul возражает: за 7 дней получается механика, но редко игра. Его формат — 2 недели вдвоём: неделя на механику и управление, неделя на тюнинг и прогрессию.

Метрика удачного прототипа по Hecker & Gingold: к нему возвращаются, его хочется запускать снова.

Jonathan Blow ([GDC 2007, Independent Games Summit, пересказ Game Developer](https://www.gamedeveloper.com/pc/gdc-prototyping-for-indie-developers)): прототип, который проверяет только технологию, а не геймплей, — плохой прототип. «Невесёлый» прототип тоже полезен: Oracle Billiards не стал игрой, но привёл к механике времени Braid.

## 11. Этапы продакшна и критерии выхода

| Этап | Цель | Критерий выхода |
| --- | --- | --- |
| Концепт / исследование | Выбрать идею | One-sheet, опоры, ответы прототипов на ключевые вопросы; решение go / kill |
| Препродакшн | Снять риски | First playable или vertical slice; ключевые ADR и TDD; план майлстоунов; premortem |
| Производство | Фичи и контент | Feature Complete (зафиксированы основные глаголы), затем Content Complete |
| Альфа | Фичи готовы | Дальше только доработка по тестам |
| Бета | Фичи и ассеты готовы | Нет блокирующих багов, меняются только исправления |
| Release Candidate → Gold | Готово к выпуску | Пройден тест-план QA |
| Live / пост-продакшн | Поддержка | Постмортем, план обновлений |

Источники: [Cerny Method (2002)](https://en.wikipedia.org/wiki/Mark_Cerny) — препродакшн снимает риски и заканчивается «publishable first playable», который не зацепил — проект отменяют; [Rami Ismail, Milestones (2022)](https://ltpf.ramiismail.com/milestones/) — Research → Pre-Production (vertical slice) → Production → Wrap-Up, шаблон майлстоуна «цель / стратегия / ресурсы / сроки», буфер вычитается из дедлайна; [Wikipedia: Video game development](https://en.wikipedia.org/wiki/Video_game_development) — определения альфы, беты, gold.

**Definition of Done для фичи** (по [Scrum Guide 2020](https://scrumguides.org/scrum-guide.html) и практике работы с агентами):

- все критерии приёмки спецификации выполнены, сквозная проверка пройдена, доказательство приложено;
- тесты правил добавлены и зелёные, данные прошли валидацию;
- новые решения записаны в ADR, спецификация обновлена до фактического поведения;
- дифф проверен против спецификации отдельным ревьюером: агентом или человеком;
- не прошло — возвращается в бэклог и не называется «готово».

## 12. Продакшн для соло и малой команды

- **Фиксированное время, гибкий скоуп** ([Shape Up](https://basecamp.com/shapeup)): у фичи есть appetite; не успеваем — режем скоуп, а не двигаем срок. Список того, что вырезаем, составляется заранее.
- **Режьте безжалостно** (Yu). Рутина вроде меню и сохранений неизбежна, её надо планировать. Последний отрезок — самый тяжёлый.
- **Без кранча.** При 60 часах в неделю выигрыш в производительности исчезает примерно за два месяца, 40 часов — долгосрочный максимум ([Robinson, IGDA, 2005](https://www.igda.org/resources-archive/why-crunch-mode-doesnt-work-six-lessons-2005/)).
- **Premortem** в начале ([Klein, HBR, 2007](https://hbr.org/2007/09/performing-a-project-premortem)): «проект провалился — почему?». У каждого риска есть вероятность, влияние, способ снятия (обычно прототип) и триггер.
- **Postmortem** после каждого майлстоуна, а не только после релиза: что пошло хорошо, что плохо, корневая причина и её тип. По анализу 200 постмортемов ([Politowski et al., 2020](https://arxiv.org/abs/2009.02440)) корневые причины чаще в людях и процессах, чем в технологиях. Предшественник — [Washburn et al., ICSE 2016](https://doi.org/10.1145/2889160.2889253): 155 постмортемов с Gamasutra, лучшие практики и ловушки. Архив классических постмортемов Game Developer Magazine 1994–2013 бесплатно лежит на [GDC Vault](https://www.gdcvault.com/gdmag).
- **ИИ-агент как исполнитель**: спецификация → план → задачи → реализация → проверка. Одна фича — один агент в чистом контексте; ревью отдельным агентом; тесты и хуки вместо «выглядит готовым».

**ИИ в геймдеве: что известно на 2026 год.** По [GDC 2026 State of the Game Industry](https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/) (больше 2300 респондентов) генеративный ИИ на работе используют 36% (в студиях — 30%). Среди применений: исследования и брейншторм — 81%, помощь с кодом — 47%, прототипирование — 35%. 52% считают влияние ИИ на индустрию негативным. Доклад GDC 2026 [AI-Driven 3D Game Prototyping with Engine Integration](https://gdcvault.com/play/1036034/AI-Driven-3D-Game-Prototyping) (Yang Hao, Tencent) показывает путь от простых требований к прототипу: код логики, UI, сцены. Проверенных докладов именно о спецификациях для агентов (Claude Code, Codex, Cursor) в разработке игр не найдено, поэтому практика в разделе 6 опирается на общие источники SDD.

## 13. Источники

**Дизайн-документы**

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [The Anatomy of a Design Document, Part 1](https://www.gamedeveloper.com/design/the-anatomy-of-a-design-document-part-1-documentation-guidelines-for-the-game-concept-and-proposal) и [Part 2](https://www.gamedeveloper.com/design/the-anatomy-of-a-design-document-part-2-documentation-guidelines-for-the-functional-and-technical-specifications) | Tim Ryan, 1999 | Классика: concept, proposal, функциональная и техническая спецификации. Формат монолита устарел, перечень разделов — нет |
| [One Page (GDC Vault)](https://gdcvault.com/play/1012356/One-Page), [слайды на stonetronix.com](https://www.stonetronix.com/) | Stone Librande, GDC 2010 | Один лист — одна система: примеры из Diablo III, Spore, The Simpsons. Плюс бумажные прототипы цифровых игр |
| [Death of the game design document](https://www.mcvuk.com/development-news/death-of-the-game-design-document/) | James Sweatman, 2014 | Пять аргументов против центрального GDD и когда он всё же нужен |
| [Painless Functional Specifications](https://www.joelonsoftware.com/2000/10/02/painless-functional-specifications-part-1-why-bother/) | Joel Spolsky, 2000 | Лучший аргумент за спецификации |
| [The Door Problem](https://lizengland.com/blog/2014/04/the-door-problem/) | Liz England, 2014 | Сколько решений скрыто в простой фиче |
| [Loops and Arcs](https://lostgarden.com/2012/04/30/loops-and-arcs/) | Daniel Cook, 2012 | Язык для диаграмм core loop |
| [MTG Comprehensive Rules](https://magic.wizards.com/en/rules) | Wizards of the Coast, живой | Эталон формулировки правил карточной игры |
| [Video: 10 pieces of Hearthstone design wisdom](https://gamedeveloper.com/design/video-10-pieces-of-i-hearthstone-i-design-wisdom) | Eric Dodds, GDC 2014 | Принципы дизайна ККИ от команды Hearthstone |
| Level Up! The Guide to Great Video Game Design, 3rd ed. ([books.md](books.md), [оглавление](https://shop.heise.de/9781394298785-level-up-the-guide-to-great-video-game-design-pdf)) | Scott Rogers, Wiley, 19.11.2024 | Глава 4: one-sheet → ten-pager → beat chart → GDD. В приложениях образцы one-sheet и ten-pager, шаблон GDD, high-concept pitch, анкета плейтеста |
| [Building a basic story bible for your game](https://www.gamedeveloper.com/design/building-a-basic-story-bible-for-your-game) | Anna Megill (пересказ Bryant Francis), 2019 | Структура story bible как живого документа |

**Спецификации, решения, агенты**

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [Documenting Architecture Decisions](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) | Michael Nygard, 2011 | Канонический ADR |
| [MADR](https://adr.github.io/madr/) | MADR 4.0, 2024 | ADR с вариантами и подтверждением |
| [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/) | Malte Ubl, 2020 | Разделы TDD и когда его не писать |
| [EARS](https://alistairmavin.com/ears/) | Alistair Mavin et al., 2009 | Пять шаблонов однозначных требований |
| [Gherkin Reference](https://cucumber.io/docs/gherkin/reference/) | Cucumber | Feature / Rule / Example / Scenario Outline |
| [Spec-driven development with AI](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/) | Den Delimarsky, GitHub, 2025 | Почему агенту нужна записанная цель; Specify → Plan → Tasks → Implement |
| [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices) | Anthropic, живой | Самодостаточная спека, проверка, которую агент запускает сам, «опроси меня → SPEC.md» |
| [AGENTS.md](https://agents.md/) | Agentic AI Foundation | Формат инструкций для агентов в репозитории |
| [Type Object](https://gameprogrammingpatterns.com/type-object.html) | Robert Nystrom | Почему карты и юниты — данные |

**Прототипирование и продакшн**

| Источник | Автор, год | Зачем читать |
| --- | --- | --- |
| [How to Prototype a Game in Under 7 Days](https://www.gamedeveloper.com/game-platforms/how-to-prototype-a-game-in-under-7-days) | Gabler, Gray, Kucic, Shodhan, 2005 | 19 правил быстрого прототипа |
| [Advanced Prototyping](http://www.chrishecker.com/Advanced_Prototyping) | Hecker, Gingold, GDC 2006 | Прототип как ответ на вопрос, «башня настройки» |
| [GDC: Prototyping for Indie Developers](https://www.gamedeveloper.com/pc/gdc-prototyping-for-indie-developers) | Jonathan Blow, GDC 2007 (пересказ Simon Carless) | Прототипы Braid: проверять геймплей, а не технологию |
| Game Production: Prototyping and Producing Your Board Game | Geoffrey Engelstein, CRC, 18.12.2020 | Физический прототип настольной и карточной игры: от бумаги до производства |
| [Finishing a Game](https://makegames.tumblr.com/post/1136623767/finishing-a-game) | Derek Yu, 2010 | 15 правил, как довести игру до конца |
| [The Indie Soapbox](https://gdcvault.com/play/1015763/The-Indie-Soapbox) | GDC Independent Games Summit, ежегодно; запись 2012 бесплатна | 10 инди по несколько минут: позиции о ремесле и индустрии |
| [Spelunky](https://bossfightbooks.com/products/spelunky-by-derek-yu) | Derek Yu, 2016 | Путь от прототипа до релиза |
| [Milestones](https://ltpf.ramiismail.com/milestones/), [Pitch Template](https://ltpf.ramiismail.com/pitch-template/) | Rami Ismail, 2022, 2023 | Фазы и майлстоуны инди-проекта, шаблон питча |
| [Agile Game Development, 2nd ed.](https://www.pearson.com/store/en-us/p/agile-game-development-build-play-repeat/P200000000362/9780136527817) | Clinton Keith, 2020 | Scrum и Kanban для игр |
| [The Game Production Toolbox](https://www.routledge.com/The-Game-Production-Toolbox/Chandler/p/book/9781138341708) | Heather Chandler, 2020 | Фазы, расписание, бюджет, QA, локализация |
| A Playful Production Process | Richard Lemarchand, MIT Press 2021 | Четыре фазы для малых команд и студентов |
| [Shape Up](https://basecamp.com/shapeup) | Ryan Singer, 2019 | Appetite, фиксированное время, гибкий скоуп |
| [Why Crunch Mode Doesn't Work](https://www.igda.org/resources-archive/why-crunch-mode-doesnt-work-six-lessons-2005/) | Evan Robinson, IGDA 2005 | Данные против кранча |
| [Game Industry Problems](https://arxiv.org/abs/2009.02440) | Politowski et al., 2020 | Анализ 200 постмортемов |
| [What went right and what went wrong](https://doi.org/10.1145/2889160.2889253) | Washburn, Sathiyanarayanan, Nagappan, Zimmermann, Bird, ICSE 2016, с. 280–289 | 155 постмортемов: лучшие практики и ловушки |
| [2026 State of the Game Industry](https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/) | GDC, 2026 | Как разработчики реально используют генеративный ИИ |
| Blood, Sweat, and Pixels; [Press Reset](https://books.apple.com/si/book/press-reset/id1530789188) | Jason Schreier, 2017, 2021 | Как реально идёт разработка и почему закрываются студии |

## 14. Расхождения в источниках

- **Длина прототипа**: 7 дней в одиночку (Gabler et al.) или 2 недели вдвоём (Juul).
- **Препродакшн**: у Cerny он свободный, без майлстоунов до одобрения; у Ismail и Keith итерации и майлстоуны идут с самого начала.
- **Опоры**: неизменный фильтр (Bungie, по пересказам) или пересматриваемый документ (вторичные гайды).
- **Показ рано или с полировкой**: Ismail советует показывать рано, издательские гайды — не показывать недоделанные ассеты. Компромисс: показывать рано, но выбирать, что показать.
- **Фиксированное время** (Shape Up, Ismail) или фиксированный контент майлстоуна (AAA). Для соло и агентов удобнее первое.

- **Дата Level Up! 3rd ed.**: 19.11.2024 у Wiley-VCH и heise; раньше в справочнике стоял декабрь 2024.

Пробелы: первоисточник Damion Schubert о живом документе и вики-GDD не найден. Нет проверенного шаблона UI flow и wireframes для игр. Шаблон GDD Benjamin Stanley известен только по вторичным копиям `[не проверено]`; gamedev.world (Rami Ismail) не открывается из-за ошибки сертификата. Докладов 2025–2026 годов именно о спецификациях для ИИ-агентов в геймдеве не найдено, есть только общая статистика и доклад Tencent (раздел 12).
