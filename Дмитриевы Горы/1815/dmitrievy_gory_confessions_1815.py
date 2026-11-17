from corpus.statuses import BATASHEV_PEASANT, BATASHEV_PEASANT_FEMALE
from verso.ru.dsl import (CONFESSION_LIST, CensusRole, RecordDefaults, census_records, household,
                          member, page, person)
from verso.ru.dsl.marital_status import WIDOW

# Исповедная роспись 1815 г., с. Дмитриевы Горы, церковь Покрова Пресвятыя Богородицы.
# **ГАВО ф. 556 оп. 107 д. 131, лл. 227–242об** (заказ № 5003, получен 28.10.2026; Photos
# «Дмитриевы Горы 1815 ИР (ГАВО 556-107-131)», pk 3759). Раздел целый, от заголовка до итога.
#
# Взяты три двора с л. 231об (`../families/Кикеевы.md`):
# - двор 50 — Семенъ Васильевъ, вопрос 69: «Семенъ Васильевъ 40, жена его Оксинья Кондратьева 39,
#   дѣти ихъ Силвестръ 6, Марья 14; Петръ Васильевъ 21, жена его Марья Терентьева 22». Тот же
#   двор, что семья 38 РС-7 1816 г.; 🆕 отчество жены Петра — **Терентьева**. Варвары (11 в
#   1810 г.) и Ивана Васильева с семьёй здесь уже нет.
# - двор 52 — «вдова Ѳедора Антонова 57; дѣти ихъ Антонъ 21, Игнатій 18, Ѳотій 14». Над «у Антона
#   жена Татіяна Васильева, 27» писец надписал «сестра» и не зачеркнул «жена»: это **Татьяна
#   Васильевна, дочь Василія Харитонова** (25 в РС-7 1816 г.) — двоюродная Антону. Далее «у Антона
#   жена Елена Васильева 21, дочь ихъ Анна 3». Самого Василія Харитонова в этих дворах нет.
# - двор 53 — Родіонъ Кондратьевъ с сыновьями и «вдова Офимья Харитонова» с детьми.
#
# Вычитано в Verso 03.11.2026 (прочитано 28.10.2026 по кадру 1050 при ~1.8×).

census = census_records(
    "ГАВО", "556", "107", "131", "Дмитриевы Горы", 1815,
    *page("231об",
          household("50",
                    member(1, person("Семенъ", "Васильевъ"), CensusRole.HEAD, age=40),
                    member(2, person("Оксинья", "Кондратьева"), CensusRole.WIFE, ref_member=1, age=39),
                    member(3, person("Силвестръ"), CensusRole.SON, ref_member=1, age=6),
                    member(4, person("Марья"), CensusRole.DAUGHTER, ref_member=1, age=14),
                    member(5, person("Петръ", "Васильевъ"), CensusRole.BROTHER, ref_member=1, age=21),
                    member(6, person("Марья", "Терентьева"), CensusRole.WIFE, ref_member=5, age=22),
                    ),
          household("52",
                    member(1, person("Ѳедора", "Антонова"), CensusRole.HEAD, age=57, marital_status=WIDOW),
                    member(2, person("Антонъ"), CensusRole.SON, ref_member=1, age=21),
                    member(3, person("Игнатій"), CensusRole.SON, ref_member=1, age=18),
                    member(4, person("Ѳотій"), CensusRole.SON, ref_member=1, age=14,
                           comment="в метриках — Ѳока Ѳедоровъ"),
                    member(5, person("Татіяна", "Васильева"), CensusRole.LODGER, ref_member=2, age=27,
                           comment="«у Антона жена», над строкой надписано «сестра»"),
                    member(6, person("Елена", "Васильева"), CensusRole.WIFE, ref_member=2, age=21),
                    member(7, person("Анна"), CensusRole.DAUGHTER, ref_member=2, age=3),
                    # В росписи его нет — погребёнъ 10.05.1810; восстановлен по «вдова Ѳедора Антонова»,
                    # как в ИР 1810 г.
                    member(8, person("Ѳедоръ", "Харитоновъ"), None, ref_member=1, spouse_member=1, hidden=True),
                    ),
          household("53",
                    member(1, person("Родіонъ", "Кондратьевъ"), CensusRole.HEAD, age=66),
                    member(2, person("Овдотья", "Петрова"), CensusRole.WIFE, ref_member=1, age=65),
                    member(3, person("Іуда"), CensusRole.SON, ref_member=1, age=36),
                    member(4, person("Осипъ"), CensusRole.SON, ref_member=1, age=24),
                    member(5, person("Петръ"), CensusRole.SON, ref_member=1, age=21),
                    member(6, person("Меланья", "Петрова"), CensusRole.WIFE, ref_member=3, age=34),
                    member(7, person("Анна", "Тимоѳева"), CensusRole.WIFE, ref_member=4, age=22),
                    member(8, person("Офимья", "Петрова"), CensusRole.WIFE, ref_member=5, age=20),
                    member(9, person("Афонасій"), CensusRole.SON, ref_member=3, age=10),
                    member(10, person("Анна"), CensusRole.DAUGHTER, ref_member=3, age=9),
                    member(11, person("Офимья", "Харитонова"), CensusRole.DAUGHTER_IN_LAW, ref_member=1, age=41,
                           marital_status=WIDOW, comment="«вдова»; вдова Трофима Родіонова"),
                    member(12, person("Ѳедоръ"), CensusRole.SON, ref_member=11, age=11),
                    member(13, person("Овдотья"), CensusRole.DAUGHTER, ref_member=11, age=14),
                    # В росписи его нет — умер 13.03.1806; восстановлен по «вдова Офимья Харитонова»
                    member(14, person("Трофимъ"), None, ref_member=11, spouse_member=11, parent_member=1, hidden=True),
                    ),
          ),
    defaults=RecordDefaults(residence="Дмитриевы Горы", status_male=BATASHEV_PEASANT,
                            status_female=BATASHEV_PEASANT_FEMALE),
    **CONFESSION_LIST,
)
