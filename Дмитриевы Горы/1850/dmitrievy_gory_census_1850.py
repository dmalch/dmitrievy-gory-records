from corpus.statuses import SHEPELEV_PEASANT, SHEPELEV_PEASANT_FEMALE
from verso.ru.dsl import (CensusRole, Month, RecordDefaults, census_records, household, member,
                          page, person)

# Ревизская сказка 9-й ревизии, 1850 г., с. Дмитриевы Горы.
# **ГАВО ф. 301 оп. 5 д. 629, лл. 1021об–1022об** (сканы ЭЧЗ 1074–1075).
# Дело — «Ревизские сказки 9-й ревизии помещичьих крестьян Меленковского уезда
# с литера «Р» по «Я»»; село лежит на сканах 1055–1120, сказка от 7 сентября 1850 г.
#
# ⚠ Помещичьи сказки подшиты ПО ФАМИЛИИ ВЛАДЕЛЬЦА, не по селению. Дмитриевы Горы —
# за Шепелевыми (литера «Ш»), что подтверждает и МК 1859 г.: «крестьянинъ отчины
# Гг. Шепелевыхъ».
#
# ⚠ В этом деле каждый двор — отдельная сказка, мужская и женская страницы стоят
# рядом на одном скане, поэтому жёны и дочери названы сразу.
#
# Двор прочитан один раз, при зуме 2.6–5.5×, обратной сверки не было.
# Вычитано в Verso 10.10.2026.

census = census_records(
    "ГАВО",
    "301",
    "5",
    "629",
    "Дмитриевы Горы",
    1850,
    *page("1021об-1022об",
          household("45",
                    # Родоначальникъ двора — Ѳедоръ; у него трое сыновей: Антонъ, Игнатъ и Ѳока. В ревизии
                    # 1858 г. этот же двор идёт под № 42 (по 9-й ревизии — 45), и там на строке Антона
                    # стоит фамилия «Кикеевъ»
                    member(1, person("Антонъ", "Федоровъ"), CensusRole.HEAD, age=54, previous_age=38),
                    member(2, person("Елена", "Васильева"), CensusRole.WIFE, ref_member=1, age=54),
                    member(3, person("Осипъ"), CensusRole.SON, ref_member=1, previous_age=15,
                           departure_year=1840, departure_reason="отдан в рекруты"),
                    # в графе прошлой ревизии — «новорожденный»
                    member(4, person("Макаръ"), CensusRole.SON, ref_member=3, age=10,
                           comment="«Осиповъ сынъ»"),
                    member(5, person("Петръ"), CensusRole.SON, ref_member=1, age=28, previous_age=12),
                    member(6, person("Ольга", "Никифорова"), CensusRole.WIFE, ref_member=5, age=27),
                    member(7, person("Авдотья"), CensusRole.DAUGHTER, ref_member=5, age=6),
                    # «Настасья» — несомненно: перечитано 12.10.2026 при 9× (л. 1074), круглое «с» после «На» и
                    # перед «ья», «л» нет (ср. «Елена», «Васильева» той же руки). ИР 1855 г. и РС 1858 г. зовут
                    # её «Наталья» (10 и 12 лет) — одна девочка, имя расходится в источниках; свод —
                    # natalja_petrovna_1845
                    member(8, person("Настасья"), CensusRole.DAUGHTER, ref_member=5, age=5),
                    member(9, person("Андрей"), CensusRole.SON, ref_member=1, age=24, previous_age=8),
                    member(10, person("Василиса", "Никитина"), CensusRole.WIFE, ref_member=9, age=27),
                    # первое чтение при 4.2× — «Сосипатра»; вычитка дала «Секлетея»
                    member(11, person("Секлетея"), CensusRole.DAUGHTER, ref_member=9, age=3),
                    # в графе прошлой ревизии — «новорожденный»
                    member(12, person("Иванъ"), CensusRole.SON, ref_member=9, age=4),
                    # в графе прошлой ревизии — «новорожденный». С Романомъ Андреевичемъ, погребённымъ в
                    # 1913 г. «61» (⇒ ок. 1852), не сведён: возрасты расходятся
                    member(13, person("Раманъ"), CensusRole.SON, ref_member=9, age=1),
                    member(14, person("Максимъ"), CensusRole.SON, ref_member=1, age=20, previous_age=4),
                    # 🔴 та самая пара из МК 1859 и 1869 гг. Ревизия решает спор корпуса «Максимъ vs Мемнонъ» в
                    # пользу Максима
                    member(15, person("Федора", "Петрова"), CensusRole.WIFE, ref_member=14, age=20),
                    member(16, person("Игнатъ", "Федоровъ"), CensusRole.BROTHER, ref_member=1,
                           age=52, previous_age=36, comment="«Антона Федорова братъ»"),
                    member(17, person("Авдотья", "Иванова"), CensusRole.WIFE, ref_member=16,
                           age=49),
                    # 🔴 «Игнатовъ сынъ Фролъ». Ревизия 1858 г. пишет так же, и на женской странице — «Фрола
                    # Игнатова жена». ⇒ Фролъ ИГНАТОВИЧЪ. Чтение метрики 1883 г. «Флор назван сам =
                    # Иоанновичъ» надо перепроверить по скану
                    member(18, person("Фролъ"), CensusRole.SON, ref_member=16, age=20, previous_age=4),
                    # В корпусе «Екатерина Ивановна» погребена в 1911 г. 79 лет ⇒ род. ок. 1832, что к
                    # Фролу подходит; не сведена
                    member(19, person("Екатерина", "Иванова"), CensusRole.WIFE, ref_member=18,
                           age=20),
                    # в графе прошлой ревизии — «новорожденный»
                    member(20, person("Василій"), CensusRole.SON, ref_member=18, age=1),
                    # 🔴 «Ѳедоръ Игнатьевъ» корпуса: погребён 1909 в 76 л. ⇒ ок. 1833
                    member(21, person("Федоръ"), CensusRole.SON, ref_member=16, age="16.5",
                           previous_age="0.5"),
                    # в графе прошлой ревизии — «новорожденный»; тёзка племянника (чл. 20)
                    member(22, person("Василій"), CensusRole.SON, ref_member=16, age=11),
                    # 🔴🔴🔴 СЕЛЬСКІЙ ѲОКА НАЗВАН. Проход по метрикам знал его только по отчествам детей. Не
                    # путать с Ѳокой Митрофановымъ казённой деревни Кононовой (†1872)
                    member(23, person("Фока", "Федоровъ"), CensusRole.BROTHER, ref_member=1,
                           previous_age=32, departure_year=1847, departure_reason="умер"),
                    member(24, person("Марья", "Семенова"), CensusRole.WIFE, ref_member=23,
                           age=47),
                    # 🔴 «Ѳедосья Ѳокина» МК 1859 г., жена Селиверста Алексѣева (двор 145/135 ревизии 1858 г.).
                    # Возраст не читается
                    member(25, person("Федосья"), CensusRole.DAUGHTER, ref_member=23, age=18),
                    # 🔴 «Павелъ Ѳокинъ Кекевъ» МК 1880 г.; погребён 1901 в 61 г.
                    member(26, person("Павелъ"), CensusRole.SON, ref_member=23, age=14),
                    # 🔴 погребён 1881 в 42 г. ⇒ род. 1839 — сходится день в день
                    member(27, person("Иванъ"), CensusRole.SON, ref_member=23, age=11),
                    # 🔴 «Алексій Ѳокинъ» МК 1872 г. (сын Сильвестръ), хозяин двора 3 переписи 1897 г. (53 г.),
                    # **погребён 20 мая 1897 г. пятидесяти четырёх лет** (д.197 л. 253об). ✅ **ТРОЕ СЫНОВЕЙ —
                    # И ЭТО ВЕРНО** (проверено 16.09.2026). Прежде здесь стояла тревога: «Аникиты Ѳокина,
                    # погребённого в 1897 г. 54 лет, в дворе НЕТ, а Ѳока умер в 1847 и позже зачать его не
                    # мог». Тревога снята — **никакого Аникиты не было**: имя в записи 1897 г. перечитано как
                    # **«Аликсѣй»**, то есть это сам Алексѣй, третий из троих. Ревизия и метрика согласны, и
                    # лишний сын из рода уходит
                    member(28, person("Алексей"), CensusRole.SON, ref_member=23, age=5)),
          ),
    record_day=7,
    record_month=Month.SEPTEMBER,
    prev_revision_year=1834,
    defaults=RecordDefaults(residence="Дмитриевы Горы", status_male=SHEPELEV_PEASANT,
                            status_female=SHEPELEV_PEASANT_FEMALE),
)
