from verso.ru.dsl import CensusRole, census_records, household, member, person
from verso.ru.dsl.marital_status import WIDOW, WIDOWER
from verso.ru.dsl.statuses import PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_SON

# 1-я всеобщая перепись населения Российской империи, 28 января 1897 г.
# Переписные листы по Дмитриево-Горской волости Меленковского уезда,
# счётный участок 8. ГАВО ф.433 оп.1 д.101 (лл. 1–260).
#
# The other half of the same участок is `dmitrievy_gory_census_1897_d100.py`;
# household numbering continues from it (1–4 there, 5–7 here) so the 1897 set
# reads as one series. See that file's header for the source and its limits.
# Checked against the scans on 2026-10-05 (ГАВО order № 4594, album
# «Дмитриевы Горы 1897 перепись (ГАВО 433-1-101)») — every member of дворы 5–7.
# Proofread in Verso on 2026-10-28, households 5–7.

census = census_records(
    "ГАВО", "433", "1", "101", "Дмитриевы Горы", 1897,

    # Л. 33, 33 об. – 34, 35 об. – 36 (переписные листы № 111а, 111б) — Кикев Максим Антонов
    household("5",
              member(1, person("Максимъ", "Антоновъ", "Кикевъ", status="крестьянин из владельческих"), CensusRole.HEAD, age=70),
              member(2, person("Федора", "Петрова", status="крестьянка из владельческих"), CensusRole.WIFE, age=70),
              member(3, person("Дмитрій", status="крестьянин из владельческих"), CensusRole.SON, age=40,
                     destination="Ардатовский уезд", occupation="сторож частного леса",
                     comment="живёт в Нижегородской губернии Ардатовском уезде; грамотный (дома)"),
              member(4, person("Егоръ", status="крестьянин из владельческих"), CensusRole.SON, age=35,
                     occupation="выработка угля на заводе", comment="временно отсутствует"),
              member(5, person("Аграфена", "Иванова", status="крестьянка из владельческих"), CensusRole.WIFE, ref_member=3, age=40,
                     destination="Ардатовский уезд",
                     comment="роль в оригинале: сноха и жена №3; живёт при муже"),
              member(6, person("Андрей", "Дмитріевъ", status=PEASANT_SON), CensusRole.GRANDSON, ref_member=1, age=15,
                     parent_member=3, destination="Ардатовский уезд",
                     comment="роль в оригинале: внук и сын №3; живёт с отцом; грамотный "
                             "(в церковно-приходской школе)"),
              member(7, person("Иванъ", "Дмитревъ", status=PEASANT_SON), CensusRole.GRANDSON, ref_member=1, age=11,
                     parent_member=3, destination="Ардатовский уезд",
                     comment="роль в оригинале: внук и сын №3; живёт с отцом; грамотный "
                             "(в земской школе)"),
              member(8, person("Александръ", "Дмитревъ", status=PEASANT_SON), CensusRole.GRANDSON, ref_member=1, age=10,
                     parent_member=3, destination="Ардатовский уезд",
                     comment="роль в оригинале: внук и сын №3; живёт с отцом; грамотный "
                             "(в земской школе)"),
              member(9, person("Василій", "Дмитревъ", status=PEASANT_SON), CensusRole.GRANDSON, ref_member=1, age=8,
                     parent_member=3, destination="Ардатовский уезд",
                     comment="роль в оригинале: внук и сын №3; живёт с отцом"),
              # Возраст по скану — **2** (расшифровка давала 1; сверено 05.10.2026, цифра чёткая).
              member(10, person("Николай", "Дмитревъ", status=PEASANT_SON), CensusRole.GRANDSON, ref_member=1, age=2,
                     parent_member=3, destination="Ардатовский уезд",
                     comment="роль в оригинале: внук и сын №3; живёт с отцом"),
              member(11, person("Катерина", "Дмитрева", status=PEASANT_DAUGHTER), CensusRole.GRANDDAUGHTER, ref_member=1, age=6,
                     parent_member=3, destination="Ардатовский уезд",
                     comment="роль в оригинале: внука и дочь №3; живёт с отцом"),
              member(12, person("Елена", "Дмитріева", status=PEASANT_DAUGHTER), CensusRole.GRANDDAUGHTER, ref_member=1, age=3,
                     parent_member=3, destination="Ардатовский уезд",
                     comment="роль в оригинале: внука и дочь №3; живёт с отцом"),
              member(13, person("Надежда", "Дмитрева", status="крестьянка из владельческих"), CensusRole.WIFE, ref_member=4, age=37,
                     comment="роль в оригинале: сноха и жена №4"),
              member(14, person("Ефимъ", "Егоровъ", status=PEASANT_SON), CensusRole.GRANDSON, ref_member=1, age=13,
                     parent_member=4, comment="роль в оригинале: внук и сын №4"),
              member(15, person("Марья", "Егорова", status=PEASANT_DAUGHTER), CensusRole.GRANDDAUGHTER, ref_member=1, age=10,
                     parent_member=4, comment="роль в оригинале: внука и дочь №4"),
              member(16, person("Матрона", "Егорова", status=PEASANT_DAUGHTER), CensusRole.GRANDDAUGHTER, ref_member=1, age=7,
                     parent_member=4, comment="роль в оригинале: внука и дочь №4"),
              member(17, person("Анна", "Егорова", status=PEASANT_DAUGHTER), CensusRole.GRANDDAUGHTER, ref_member=1, age=4,
                     parent_member=4, comment="роль в оригинале: внука и дочь №4"),
              member(18, person("Анастасія", "Егорова", status=PEASANT_DAUGHTER), CensusRole.GRANDDAUGHTER, ref_member=1, age=3,
                     parent_member=4, comment="роль в оригинале: внука и дочь №4"),
              member(19, person("Евдокия", "Егорова", status=PEASANT_DAUGHTER), CensusRole.GRANDDAUGHTER, ref_member=1, age="6 мес",
                     parent_member=4, comment="роль в оригинале: внука и дочь №4"),
              page="33"),

    # Л. 53, 53 об. – 54 (переписной лист № 118) — Кикев Павел Фокеев
    household("6",
              member(1, person("Павелъ", "Фокѣевъ", "Кикевъ", status="крестьянин из владельческих"), CensusRole.HEAD, age=61,
                     marital_status=WIDOWER,
                     comment="грамотный (дома); брат Алексея Фокина (двор 3, д. 100) — оба по отчеству сыновья Фоки"),
              member(2, person("Григорій", status="крестьянин из владельческих"), CensusRole.SON, age=20,
                     occupation="выработка угля на заводе",
                     comment="временно отсутствует; грамотный (в церковно-приходской школе)"),
              member(3, person("Степанъ", status="крестьянин из владельческих"), CensusRole.SON, age=17,
                     comment="грамотный (в церковно-приходской школе)"),
              member(4, person("Матвѣй", status=PEASANT_SON), CensusRole.SON, age=14),
              member(5, person("Улита", "Максимова", status="крестьянка из владельческих"), CensusRole.WIFE, ref_member=2, age=21,
                     comment="роль в оригинале: сноха и жена №2"),
              page="53, 53об–54"),

    # Л. 233, 233 об. – 234, 235 об. – 236 (переписные листы № 191а, 191б) — Кикев Андрей Иванов
    household("7",
              member(1, person("Андрей", "Ивановъ", "Кикевъ", status="крестьянин из владельческих"), CensusRole.HEAD, age=35,
                     occupation="выработка угля на заводе", comment="временно отсутствует"),
              # 25 лет при детях 13 и 12 лет (№4, №3) — по возрасту она им не мать, т.е. ВТОРАЯ жена Андрея.
              # Первая названа не переписью, а метрикой: **Стефанида Егорова** (МК 1884, д.196 № м76; пара
              # отодвинута на МК 1882, № ж54) — заведена ниже под № 14 как `hidden`. Григорий, Марфа и —
              # с 21.09.2026 — Катерина уходят к Стефаниде. ⚠ Размечены ВСЕ ТРОЕ детей Андрея, а не
              # только переносимые: фильтр двух жён односторонний, и неразмеченный ребёнок попадает в
              # союз КАЖДОЙ жены.
              member(2, person("Наталья", "Ефимова", status="крестьянка из владельческих"), CensusRole.WIFE, age=25),
              member(3, person("Григорій", status=PEASANT_SON), CensusRole.SON, age=12,
                     secondary_role=CensusRole.SON, secondary_ref_member=14,
                     comment="грамотный (в церковно-приходской школе). "
                             "Сын ПЕРВОЙ жены: его метрика найдена — род. 23 сентября 1884 г. от "
                             "«Андрея Иванова Кекева и жены его Стефаниды Егоровой» "
                             "(МК 1884, д.196 № м76). Возраст переписи (12 лет на январь 1897 г.) "
                             "сходится."),
              # 🔴 **МЕТРИКА НАЙДЕНА — МК 1882 г., ч. 1 № ж54, л. 107об**: род. **28 августа**, крещена 29
              # августа 1882 г. от «Андрея Иванова Кекева и жены его Стефаниды Егоровой». Прежде она была
              # отнесена к первой жене ПО ВОЗРАСТУ, а не по метрике, и корпус искал её рождение в 1883 г.; там
              # его нет, а ранний 1884-й исключён братом Григоріемъ (род. 23 сентября 1884 г.). ⚠ **Возраст
              # переписи занижен на год**: на 28 января 1897 г. ей 14 л. 5 мѣс., а записано 13. Возраст
              # Григория (№3) перепись при этом держит верно — ошибка в одной строке. Наталье Ефимовой в 1882
              # г. было 10–11, так что мать — Стефанида, и это теперь сказано источником, а не выведено из
              # арифметики.
              member(4, person("Марфа", status=PEASANT_DAUGHTER), CensusRole.DAUGHTER, age=13,
                     secondary_role=CensusRole.DAUGHTER, secondary_ref_member=14),
              # 🔴 **21.09.2026: КАТЕРИНА ПЕРЕВЕДЕНА К СТЕФАНИДЕ.** Мать названа метрикой — МК 1891 ч. 1
              # № ж15, л. 5: род. 16 февраля, крещена 17-го, от «Андрея Иванова Кекева и жены его
              # **Стефаниды Егоровой**». Прежде она стояла за Натальей по доводу «25 лет при детях 13 и
              # 12 — она им не мать», который о ПЯТИЛЕТНЕЙ не говорил ничего. Решают даты: Стефанида
              # погребена 27 июня 1895 г. «31 года» (ч. 3 № ж8), а Наталія Евфиміева Пѣтухова венчается
              # с Андреем вдовцом только 12 ноября 1895 г. (ч. 2 № 20, ему 33 вторымъ бракомъ, ей 26
              # первымъ) ⇒ девочке, рождённой в феврале 1891 г., она матерью быть не может.
              member(5, person("Катерина", status=PEASANT_DAUGHTER), CensusRole.DAUGHTER, age=5,
                     secondary_role=CensusRole.DAUGHTER, secondary_ref_member=14),
              # 🏆 **МУЖ НАЗВАН 16.09.2026: ИВАНЪ ѲОКИНЪ** (ок. 1839 – 24.01.1881), сын Ѳоки и брат Алексія
              # (двор 3) и Павла (двор 6). МК 1871 (март) и 1878 (№ м70) дают эту пару вместе, 1878-й — с
              # сыном Матвѣемъ; вдовеет она с января 1881 г., что и объясняет её здесь. Сама она погребена 3
              # февраля 1909 г. «крестьянской вдовой Евфросиніей Прокопіевой Кекевой», 67 л. ⇒ **двор 7 —
              # кровная ветвь рода**, а не безотцовщина. Разбор — `families/Кикеевы.md`, вопросы 63, 43, 60
              member(6, person("Евфросинья", "Прокопьева", "Кикева", status="крестьянка из владельческих"), CensusRole.MOTHER, age=58,
                     marital_status=WIDOW),
              member(7, person("Степанъ", "Ивановъ", "Кикевъ", status="крестьянин из владельческих"), CensusRole.BROTHER, age=27,
                     occupation="рабочий на чугунолитейном заводе",
                     comment="живёт в Екатеринославской губернии, в г. Александровске "
                             "(чтение места в источнике под вопросом)"),
              member(8, person("Ефимъ", "Ивановъ", "Кикевъ", status="крестьянин из владельческих"), CensusRole.BROTHER, age=23,
                     comment="в военной службе"),
              member(9, person("Семенъ", "Ивановъ", "Кикевъ", status=PEASANT_SON), CensusRole.BROTHER, age=15,
                     destination="Меленки", occupation="рабочий в типографии",
                     comment="живёт в Меленках; грамотный (в церковно-приходской школе)"),
              member(10, person("Еѳимья", "Игнатьева", status="крестьянка из владельческих"), CensusRole.WIFE, ref_member=7, age=27,
                     comment="роль в оригинале: сноха и жена №7; живёт с мужем"),
              member(11, person("Марья", "Васильева", status="крестьянка из владельческих"), CensusRole.WIFE, ref_member=8, age=20,
                     comment="роль в оригинале: сноха и жена №8"),
              member(12, person("Надежда", "Ефимова", "Кикева", status=PEASANT_DAUGHTER), CensusRole.NIECE, ref_member=1, age=1,
                     parent_member=8, comment="роль в оригинале: племянница и дочь №8"),
              member(13, person("Прасковья", "Ефимова", "Кикева", status=PEASANT_DAUGHTER), CensusRole.NIECE, ref_member=1, age="2 мес",
                     parent_member=8, comment="роль в оригинале: племянница и дочь №8"),
              # В переписи 1897 г. ОТСУТСТВУЕТ; первая жена Андрея Ивановича и мать Григория (№3) и, по
              # возрасту, Марфы (№4). Названа метрической книгой: «Андрей Ивановъ Кекевъ и жена его
              # **Стефанида Егорова**» (МК 1884, д.196 № м76, л. 197об, рождение Григория 23.09.1884; **и МК
              # 1882, № ж54, л. 107об — рождение Марфы**, чем пара отодвинута на 1882 г., а материнство
              # Стефаниды для №4 стало названным, а не вычисленным). Наталья Ефимова (№2) — 25 лет в 1897 г.,
              # т.е. не мать тринадцати- и двенадцатилетнего; заведена вручную для генеалогической цепочки. ⚠
              # Год её смерти неизвестен: 1909–1911 гг. прочитаны целиком и погребения не дали ⇒ умерла до
              # 1909 г., искать между 1885 и 1897 гг. и в д.198 (1900–1908).
              member(14, person("Стефанида", "Егорова", "Кикева", status=PEASANT_FEMALE), CensusRole.WIFE, ref_member=1,
                     hidden=True, departure_reason="умерла"),
              page="233, 233об–234, 235об–236"),

    document_type="1-я всеобщая перепись",
    document_type_genitive="1-й всеобщей переписи",
    district="8",
    volost="Дмитриево-Горская",
    archive_suffix="433-1-101",
    suffix_in_res_names=True,
)
