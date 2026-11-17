from verso.ru.dsl import CensusRole, census_records, household, member, person
from verso.ru.dsl.marital_status import MARRIED_FEMALE, SINGLE_FEMALE, WIDOW
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MAIDEN, PEASANT_SON,
                                   PEASANT_SPOUSE)

# 1-я всеобщая перепись населения Российской империи, 28 января 1897 г.
# Переписные листы по Дмитриево-Горской волости Меленковского уезда,
# счётный участок 8. ГАВО ф.433 оп.1 д.100 (лл. 1–241).
#
# Дело 101 — the other half of the same участок — is a separate file
# (`dmitrievy_gory_census_1897_d101.py`); households are numbered 1–4 here and
# 5–7 there so the 1897 set reads as one series. The household numbers are an
# editorial index: the transcript identifies each двор by лист only.
#
# Source: a transcript supplied by a researcher at ГАВО, covering the surnames
# Ганины / Абашины / Кикеевы (Кековы) / Земсковы / Кирюхины / Осиповы.
# Checked against the scans on 2026-10-05 (ГАВО order № 4594, album
# «Дмитриевы Горы 1897 перепись (ГАВО 433-1-100)»). Двор 4 members 21–22
# (л. 152об–153, переписной лист № 62в) were checked on 2026-10-06: the archive
# first sent л. 100об–101 (Мирошкины) in their place and re-delivered the spread
# on request (frame 0013_152об-153 of the same album). Proofread in Verso on
# 2026-10-27, households 1–4.

census = census_records(
    "ГАВО", "433", "1", "100", "Дмитриевы Горы", 1897,

    # Л. 66, 66 об. – 67 (переписной лист № 2б) — Кикева Евдокия Петрова
    household("1",
              # Сверено со сканом 05.10.2026: «Родился» — «Здѣсь», а «Тамб. г. къ г. Елатьмѣ»
              # стоит в графе 8 «Приписанъ ли здѣсь». Расшифровка сделала из приписки место
              # рождения (`origin="Елатьма"`), и профиль получал рождение в Елатьме.
              member(1, person("Евдокія", "Петрова", "Кикева", status=PEASANT_FEMALE), CensusRole.HEAD, age=45,
                     marital_status=MARRIED_FEMALE,
                     occupation="живёт на милостыню",
                     comment="временно отсутствует; родилась здесь, приписана к г. Елатьме "
                             "Тамбовской губернии; записана замужней, а не вдовой — муж "
                             "(Константин, по отчеству дочери) в переписи не значится"),
              member(2, person("Меланія", "Константинова", status=PEASANT_MAIDEN), CensusRole.DAUGHTER, age=18,
                     marital_status=SINGLE_FEMALE),
              page="66"),

    # Л. 92, 92 об. – 93 (переписной лист № 37) — Кикев Иван Михайлов
    household("2",
              member(1, person("Иванъ", "Михайловъ", "Кикевъ", status="крестьянин из владельческих"), CensusRole.HEAD, age=24,
                     occupation="земледелец; выработка угля на заводе",
                     comment="грамотный (в церковно-приходской школе)"),
              member(2, person("Настасья", "Егорова", status="крестьянка из владельческих"), CensusRole.WIFE, age=24),
              member(3, person("Марья", status=PEASANT_DAUGHTER), CensusRole.DAUGHTER, age=2),
              member(4, person("Нерапія", "Васильева", status="крестьянка из владельческих"), CensusRole.MOTHER, age=50,
                     marital_status=WIDOW),
              page="92"),

    # Л. 118, 118 об. – 119 (переписной лист № 50) — Кикев Алексей Фокин
    household("3",
              member(1, person("Алексѣй", "Фокинъ", "Кикевъ", status="крестьянин из владельческих"), CensusRole.HEAD, age=53),
              member(2, person("Аксинья", "Емельянова", status="крестьянка из владельческих"), CensusRole.WIFE, age=51),
              member(3, person("Сильверстъ", status="крестьянин из владельческих"), CensusRole.SON, age=25,
                     occupation="земледелец; выработка угля на заводе", comment="временно отсутствует"),
              member(4, person("Сергѣй", status="крестьянин из владельческих"), CensusRole.SON, age=18,
                     occupation="возчик", comment="временно отсутствует"),
              member(5, person("Петръ", status=PEASANT_SON), CensusRole.SON, age=11,
                     comment="грамотный (в церковно-приходской школе)"),
              member(6, person("Григорій", status=PEASANT_SON), CensusRole.SON, age=9,
                     comment="грамотный (в церковно-приходской школе)"),
              member(7, person("Евдокія", "Игнатьева", status="крестьянка из владельческих"), CensusRole.WIFE, ref_member=3, age=24,
                     comment="роль в оригинале: сноха и жена №3"),
              member(8, person("Яковъ", "Сильверстовъ", status=PEASANT_SON), CensusRole.GRANDSON, ref_member=1, age=4,
                     parent_member=3, comment="роль в оригинале: внук и сын №3"),
              member(9, person("Степанъ", "Сильверстовъ", status=PEASANT_SON), CensusRole.GRANDSON, ref_member=1, age="1 мес",
                     parent_member=3, comment="роль в оригинале: внук и сын №3"),
              page="118"),

    # Л. 148, 148 об. – 149, 150 об. – 151, 152 об. – 153 (переписные листы № 62а, 62б, 62в) —
    # Земсков Федор Игнатьев. №№ 21–22 стоят на л. 152об–153 — архив дослал его 06.10.2026
    # (в заказе № 4594 вместо него лежал л. 100об–101). Сверено: 62а держит «М 10 / Ж 12»,
    # на 62а–62б женщин 10, на 62в ещё 2 — сводка сходится.
    household("4",
              member(1, person("Федоръ", "Игнатьевъ", "Земсковъ", status="крестьянин из владельческих"), CensusRole.HEAD, age=60,
                     occupation="земледелец; выработка угля на заводе", comment="грамотный (дома)"),
              member(2, person("Федора", "Данилова", status="крестьянка из владельческих"), CensusRole.WIFE, age=60),
              member(3, person("Игнатъ", status="крестьянин из владельческих"), CensusRole.SON, age=40,
                     occupation="земледелец; выработка угля на заводе", comment="временно отсутствует"),
              member(4, person("Михаилъ", status="крестьянин из владельческих"), CensusRole.SON, age=35,
                     occupation="земледелец; выработка угля на заводе",
                     comment="временно отсутствует; грамотный (в военной службе)"),
              member(5, person("Николай", status="крестьянин из владельческих"), CensusRole.SON, age=32,
                     occupation="земледелец; выработка угля на заводе", comment="временно отсутствует"),
              member(6, person("Андрей", status="крестьянин из владельческих"), CensusRole.SON, age=30,
                     occupation="сторож при лесной даче",
                     comment="временно отсутствует; грамотный (в военной службе)"),
              member(7, person("Евдокія", "Тимофіева", status="крестьянка из владельческих"), CensusRole.WIFE, ref_member=3, age=40,
                     comment="роль в оригинале: сноха и жена №3"),
              member(8, person("Федоръ", "Игнатьевъ", status=PEASANT_SON), CensusRole.GRANDSON, ref_member=1, age=12,
                     parent_member=3,
                     comment="роль в оригинале: внук и сын №3; тёзка деда (№1); грамотный (в церковно-приходской школе)"),
              member(9, person("Андрей", "Игнатьев", status=PEASANT_SON), CensusRole.GRANDSON, ref_member=1, age=2,
                     parent_member=3, comment="роль в оригинале: внук и сын №3"),
              member(10, person("Елена", "Игнатьева", status=PEASANT_DAUGHTER), CensusRole.GRANDDAUGHTER, ref_member=1, age=16,
                     parent_member=3, comment="роль в оригинале: внука и дочь №3"),
              member(11, person("Анна", "Игнатьева", status=PEASANT_DAUGHTER), CensusRole.GRANDDAUGHTER, ref_member=1, age=10,
                     parent_member=3, comment="роль в оригинале: внука и дочь №3"),
              member(12, person("Марья", "Игнатьева", status=PEASANT_DAUGHTER), CensusRole.GRANDDAUGHTER, ref_member=1, age="1 мес",
                     parent_member=3, comment="роль в оригинале: внука и дочь №3"),
              member(13, person("Марья", "Савельева", status="крестьянка из владельческих"), CensusRole.WIFE, ref_member=4, age=35,
                     comment="роль в оригинале: сноха и жена №4"),
              member(14, person("Орина", "Михайлова", status=PEASANT_DAUGHTER), CensusRole.GRANDDAUGHTER, ref_member=1, age=3,
                     parent_member=4, comment="роль в оригинале: внука и дочь №4"),
              member(15, person("Татьяна", "Михайлова", status=PEASANT_DAUGHTER), CensusRole.GRANDDAUGHTER, ref_member=1, age=1,
                     parent_member=4, comment="роль в оригинале: внука и дочь №4"),
              member(16, person("Прасковья", "Павлова", status="крестьянка из владельческих"), CensusRole.WIFE, ref_member=5, age=31,
                     comment="роль в оригинале: сноха и жена №5"),
              member(17, person("Ульяна", "Иванова", status=PEASANT_SPOUSE), CensusRole.WIFE, ref_member=6, age=25,
                     comment="роль в оригинале: сноха и жена №6; временно отсутствует"),
              member(18, person("Иванъ", "Андреевъ", status=PEASANT_SON), CensusRole.GRANDSON, ref_member=1, age=6,
                     parent_member=6,
                     comment="роль в оригинале: внук и сын №6; временно отсутствует"),
              member(19, person("Василій", "Андреевъ", status=PEASANT_SON), CensusRole.GRANDSON, ref_member=1, age=3,
                     parent_member=6,
                     comment="роль в оригинале: внук и сын №6; временно отсутствует"),
              member(20, person("Николай", "Андреевъ", status=PEASANT_SON), CensusRole.GRANDSON, ref_member=1, age=1,
                     parent_member=6,
                     comment="роль в оригинале: внук и сын №6; временно отсутствует"),
              member(21, person("Евдокія", "Андреева", status=PEASANT_DAUGHTER), CensusRole.GRANDDAUGHTER, ref_member=1, age=5,
                     parent_member=6,
                     comment="роль в оригинале: внука и дочь №6; временно отсутствует"),
              # Скан 06.10.2026: «Филатова / Евдокія Ѳедорова», дочь, 41; графа 5 — «З»
              # (замужняя, как у Федоры Даниловой, № 2), живёт здесь, не отсутствует;
              # занятие «Земледѣлица при Отцѣ». Отчество генератор и так выводит от № 1.
              # Вычитка 27.10.2026 внесла «З» (`marital_status=MARRIED_FEMALE`); занятие не
              # внесено.
              member(22, person("Евдокія", last_name_orig="Филатова", status="крестьянка из владельческих"), CensusRole.DAUGHTER, ref_member=1, age=41,
                     marital_status=MARRIED_FEMALE,
                     comment="записана под фамилией Филатова — замужняя фамилия; муж в переписи "
                             "не значится"),
              page="148"),

    document_type="1-я всеобщая перепись",
    document_type_genitive="1-й всеобщей переписи",
    district="8",
    volost="Дмитриево-Горская",
    archive_suffix="433-1-100",
    suffix_in_res_names=True,
)
