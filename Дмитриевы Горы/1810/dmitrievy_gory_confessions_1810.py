from corpus.statuses import BATASHEV_PEASANT, BATASHEV_PEASANT_FEMALE
from verso.ru.dsl import (CONFESSION_LIST, CensusRole, RecordDefaults, census_records, household,
                          member, page, person)
from verso.ru.dsl.marital_status import WIDOW

# Исповедная роспись 1810 г., с. Дмитриевы Горы, церковь Покрова Пресвятыя Богородицы.
# **ГАВО ф. 556 оп. 111 д. 232, лл. 473–491об** (заказ № 5003, получен 28.10.2026; Photos
# «Дмитриевы Горы 1810 ИР (ГАВО 556-111-232)», pk 3758). Раздел кончается итогом на л. 491об —
# заказанные лл. 492–492об к нему не относятся.
#
# Взяты (`../families/Кикеевы.md`):
# - двор 51 (л. 478) — Васильевы, вопрос 69. 🏆 **БРАТ, КОТОРОГО РС-7 1816 Г. НЕ НАЗЫВАЕТ:**
#   «Семіонъ 35, Иванъ 26, Петръ 16 — Васильевы; у Семіона жена Оксинья Кондратьева 34, дѣти
#   ихъ Варвара 11, Марья 9; у Ивана жена Овдотья Макарова 26, сынъ ихъ Несторъ 2,5». Отец
#   Нестора, восстановленный в сказке 1816 г. (чл. 9, hidden), — **Иванъ Васильевъ**, жена его
#   **Авдотья Макарова**; Несторъ род. ок. 1807–08 (как по РС-7 1816 г.: 4 в 1811 г.).
#   🆕 У Семёна есть и старшая дочь **Варвара**.
#   Марья 9 ⇒ ок. 1801, как в РС-7 1816 г. (14) и ИР 1815 г. (14).
# - двор 55 (л. 478об) — Василій Харитоновъ с женой Овдотьей Арефьевой и детьми, а с ними
#   «вдова Ѳедора Антонова» с сыновьями (младший — «Ѳокей»): **Ѳедоръ Харитоновъ уже умер**
#   (погр. 10.05.1810).
# - двор 56 — Родіонъ Кондратьевъ; «у Родіона сноха вдова Офимья Харитонова» с детьми.
#
# Вычитано в Verso 03.11.2026 (прочитано 28.10.2026 по кадрам 530 и 540 при ~1.6×).

census = census_records(
    "ГАВО", "556", "111", "232", "Дмитриевы Горы", 1810,
    *page("478",
          household("51",
                    member(1, person("Семіонъ", "Васильевъ"), CensusRole.HEAD, age=35),
                    member(2, person("Иванъ", "Васильевъ"), CensusRole.BROTHER, ref_member=1, age=26),
                    member(3, person("Петръ", "Васильевъ"), CensusRole.BROTHER, ref_member=1, age=16),
                    member(4, person("Оксинья", "Кондратьева"), CensusRole.WIFE, ref_member=1, age=34),
                    member(5, person("Варвара"), CensusRole.DAUGHTER, ref_member=1, age=11),
                    member(6, person("Марья"), CensusRole.DAUGHTER, ref_member=1, age=9),
                    member(7, person("Овдотья", "Макарова"), CensusRole.WIFE, ref_member=2, age=26),
                    member(8, person("Несторъ"), CensusRole.SON, ref_member=2, age="2,5"),
                    ),
          ),
    *page("478об",
          household("55",
                    member(1, person("Василій", "Харитоновъ"), CensusRole.HEAD, age=44),
                    member(2, person("Овдотья", "Арефьева"), CensusRole.WIFE, ref_member=1, age=31),
                    member(3, person("Родіонъ"), CensusRole.SON, ref_member=1, age=2),
                    # Татіана (ок. 1793) родилась до венчания Василия с Овдотьей Арефьевой (17.04.1803) — дочь
                    # первой жены, Аксиньи Никиѳоровой (10), как в ИР 1805 г.; secondary_* закрывает ей союз с
                    # Овдотьей (m2) — иначе у ребёнка две матери
                    member(4, person("Татіана"), CensusRole.DAUGHTER, ref_member=1, parent_member=10, age=17,
                           secondary_role=CensusRole.DAUGHTER, secondary_ref_member=10),
                    member(5, person("Ѳедора", "Антонова"), CensusRole.LODGER, ref_member=1, age=52, marital_status=WIDOW,
                           comment="жена Ѳедора Харитонова, брата главы"),
                    member(6, person("Антонъ"), CensusRole.SON, ref_member=5, age=16),
                    member(7, person("Игнатій"), CensusRole.SON, ref_member=5, age=13),
                    member(8, person("Ѳокей"), CensusRole.SON, ref_member=5, age=9),
                    # В росписи его нет — погребёнъ 10.05.1810; восстановлен по «вдова Ѳедора Антонова»
                    member(9, person("Ѳедоръ", "Харитоновъ"), None, ref_member=5, spouse_member=5, hidden=True),
                    # В росписи её нет — умерла до 1803 г.; восстановлена, как в ИР 1805 г., по ревизии 1782 г.
                    # и по венчанію 1803 г. Василия «вторымъ бракомъ»
                    member(10, person("Аксинья", "Никиѳорова"), None, ref_member=1, spouse_member=1, hidden=True),
                    ),
          household("56",
                    member(1, person("Родіонъ", "Кондратьевъ"), CensusRole.HEAD, age=61),
                    member(2, person("Овдотья", "Петрова"), CensusRole.WIFE, ref_member=1, age=53),
                    member(3, person("Іуда"), CensusRole.SON, ref_member=1, age=31),
                    member(4, person("Осипъ"), CensusRole.SON, ref_member=1, age=19),
                    member(5, person("Петръ"), CensusRole.SON, ref_member=1, age=15),
                    member(6, person("Маланья", "Петрова"), CensusRole.WIFE, ref_member=3, age=31),
                    member(7, person("Афонасій"), CensusRole.SON, ref_member=3, age=5),
                    member(8, person("Анна"), CensusRole.DAUGHTER, ref_member=3, age=2),
                    member(9, person("Анна", "Тимоѳѣева"), CensusRole.WIFE, ref_member=4, age=19),
                    member(10, person("Офимья", "Харитонова"), CensusRole.DAUGHTER_IN_LAW, ref_member=1, age=33,
                           marital_status=WIDOW, comment="«у Родіона сноха вдова»; вдова Трофима Родіонова († 13.03.1806)"),
                    member(11, person("Федоръ"), CensusRole.SON, ref_member=10, age=7),
                    member(12, person("Овдотья"), CensusRole.DAUGHTER, ref_member=10, age=10),
                    # В росписи его нет — умер 13.03.1806; восстановлен по «у Родіона сноха вдова»
                    member(13, person("Трофимъ"), None, ref_member=10, spouse_member=10, parent_member=1, hidden=True),
                    ),
          ),
    defaults=RecordDefaults(residence="Дмитриевы Горы", status_male=BATASHEV_PEASANT,
                            status_female=BATASHEV_PEASANT_FEMALE),
    **CONFESSION_LIST,
)
