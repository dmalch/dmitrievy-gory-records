from verso.ru.dsl import (Gender, Month, RecordDefaults, birth, birth_month, birth_records, page,
                          person)
from verso.ru.dsl.statuses import (PEASANT_FEMALE, PEASANT_MAIDEN, PEASANT_MALE, PEASANT_SON,
                                   PEASANT_SPOUSE, SOLDIER)

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1914 г.,
# часть первая «О родившихся». ГАВО ф.590 оп.12 д.199, лл. 124об–141об.
#
# Первый год, прочитанный НА ДВЕ ФАМИЛИИ — Кикев/Кекев и Земсков. Весь раздел
# о родившихся прочитан (77 мужского и 44+ женского пола); Кекевых-родителей
# семь записей (одна двойня), ЗЕМСКОВЫХ среди родителей и восприемников НЕТ.
#
# ⚠ Написание фамилии в 1914 г. ПЛАВАЕТ ВНУТРИ ОДНОЙ КНИГИ: «Кикевъ» (л. 128об
# № м14), «Кикеевъ» (л. 128об № м15 — форма, совпадающая с современной фамилией
# Анны) и «Кекевъ» (все остальные). Каждая запись держит написание своей страницы.
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE, status_mother=PEASANT_FEMALE)

dmitrievy_gory_births_1914 = birth_records(
    "ГАВО", "590", "12", "199", "Дмитриевы Горы", "Покровская",
    1914,
    *page("128об", reviewed=False,
          *birth_month(Month.MARCH,
                       birth(14, Gender.MALE, 7, 8,
                             child=person("Алексий"),
                             father=person("Александр", "Димитриев", last_name_orig="Кикев", status=SOLDIER, comment="запасный солдат"),
                             mother=person("Екатерина", "Андреева"),
                             god_parent1=person("Алексий", "Андреев", last_name_orig="Ремшин", status=PEASANT_SON),
                             god_parent2=person("Евдокия", "Васильева", last_name_orig="Шимаринова", status=PEASANT_MAIDEN),
                             comment="фамилия на этой строке написана «Кикевъ». Тот же Александр Димитриев с женой "
                                     "Екатериной записан в 1918 г. (л. 260об) уже как «Кекевъ». Фамилия восприемницы "
                                     "читается неуверенно — «Шимарянцова» либо «Шимаринова»"),
                       # ✅ 06.10.2026: отец — «Алексѣй ФЛОРОВЪ», не Ѳедоровъ: сверено по скану, см. regional-rules § «Алексѣй Ѳлоровъ»; строкой ниже
                       # для сравнения «Николай Феодоровъ Никитаевъ» — у этого писца слово заметно длиннее
                       birth(15, Gender.MALE, 8, 9,
                             child=person("Иоанн"),
                             father=person("Алексий", "Флоров", last_name_orig="Кикеев", status=SOLDIER, comment="запасный солдат"),
                             mother=person("Евдокия", "Миронова"),
                             god_parent1=person("Евфимий", "Васильев", last_name_orig="Горячев"),
                             god_parent2=person("Александра", "Алексиева", last_name_orig="Кикеева", status=PEASANT_MAIDEN),
                             comment="ЕДИНСТВЕННАЯ строка книги, где фамилия написана «Кикеевъ» — как у Анны. "
                                     "Восприемница Александра Алексиева по отчеству — сестра новорождённого; "
                                     "по возрасту она же «Александра Алексеева Кекева», 19 лет, невеста в браке "
                                     "№ 14 1917 г. (л. 245об). Не утверждается, только отмечено"),
                       ),
          ),
    *page("130об", reviewed=False,
          *birth_month(Month.MAY,
                       birth(24, Gender.MALE, 1, 1,
                             child=person("Николай"),
                             father=person("Георгий", "Иоаннов", last_name_orig="Кекев"),
                             mother=person("Анна", "Иоаннова"),
                             god_parent1=person("Максим", "Алексиев", last_name_orig="Залетин", status=SOLDIER, comment="запасный солдат"),
                             god_parent2=person("Мария", "Георгиева", last_name_orig="Кекева", status=PEASANT_MAIDEN),
                             god_parent3=person("Мария", "Иоаннова", last_name_orig="Романова"),
                             comment="ДВОЙНЯ: Николай (№ м24) и Пелагия (№ ж15) записаны писцом ОДНОЙ строкой — "
                                     "одни родители, одна пара дат, три восприемника на двоих. Здесь разнесены "
                                     "по двум записям, восприемники продублированы, потому что источник не "
                                     "говорит, кто чей"),
                       birth(15, Gender.FEMALE, 1, 1,
                             child=person("Пелагия"),
                             father=person("Георгий", "Иоаннов", last_name_orig="Кекев"),
                             mother=person("Анна", "Иоаннова"),
                             god_parent1=person("Максим", "Алексиев", last_name_orig="Залетин", status=SOLDIER, comment="запасный солдат"),
                             god_parent2=person("Мария", "Георгиева", last_name_orig="Кекева", status=PEASANT_MAIDEN),
                             god_parent3=person("Мария", "Иоаннова", last_name_orig="Романова"),
                             comment="вторая половина двойни — см. запись № м24 той же строки"),
                       birth(17, Gender.FEMALE, 5, 6,
                             child=person("Елена"),
                             father=person("Андрей", "Феодоров", last_name_orig="Кекев", status=SOLDIER, comment="запасный солдат"),
                             mother=person("Иулиания", "Иоаннова"),
                             god_parent1=person("Феодор", "Андреев", last_name_orig="Царев", status=SOLDIER, comment="запасный солдат"),
                             god_parent2=person("Варвара", "Андреева", last_name_orig="Кекева", status=PEASANT_MAIDEN),
                             comment="восприемница Варвара Андреева по отчеству — сестра новорождённой"),
                       ),
          ),
    *page("134об", reviewed=False,
          *birth_month(Month.JULY,
                       birth(38, Gender.MALE, 22, 23,
                             child=person("Николай"),
                             father=person("Иаков", "Сильвестров", last_name_orig="Кекев"),
                             mother=person("Мария", "Иоаннова"),
                             god_parent1=person("Иоанн", "Васильев", last_name_orig="Маслихин"),
                             god_parent2=person("Любовь", "Сильвестрова", last_name_orig="Кекева", status=PEASANT_MAIDEN),
                             comment="этот младенец умер 11 октября 1914 в возрасте 2½ месяцев — запись о смерти "
                                     "№ м20, л. 154об. Восприемница Любовь Сильвестрова по отчеству — сестра отца"),
                       ),
          ),
    *page("135об", reviewed=False,
          *birth_month(Month.JULY,
                       birth(36, Gender.FEMALE, 27, 28,
                             child=person("Мария"),
                             father=person("Алексий", "Николаев", last_name_orig="Кекев"),
                             mother=person("Любовь", "Емельянова"),
                             god_parent1=person("Григорий", "Петров", last_name_orig="Шувалов", status="исполняющий должность псаломщика"),
                             god_parent2=person("Мария", "Николаева", last_name_orig="Кекева", status=PEASANT_MAIDEN),
                             comment="отчество матери в источнике сокращено — «Емелiева»; принято по записи 1917 г. "
                                     "(л. 237об), где та же пара записана как «солдатъ Алексій Николаевъ Кекевъ и "
                                     "Любовь Емельянова». Восприемница Мария Николаева по отчеству — сестра отца; "
                                     "она же невеста в браке № 5 1917 г. (л. 243об)"),
                       ),
          ),
    *page("136об", reviewed=False,
          *birth_month(Month.AUGUST,
                       # отчество отца читается «Игнатіевъ» (ср. Андрея Игнатіева Кекева, 1915, л. 176об — по
                       # отчеству брат), а жена — Параскева Никитина Филаткина, за которой он венчан
                       # 02.10.1902 г. ✅ Лист 1919 г. (д.200 л. 5об), где ту же пару прочитали «Ѳеодоръ
                       # ИППОЛИТОВЪ Кексевъ», ПЕРЕСМОТРЕН по скану: буквы он не решает, и запись исправлена по
                       # настоящей — см. комментарий там
                       birth(39, Gender.FEMALE, 19, 20,
                             child=person("Анна"),
                             father=person("Феодор", "Игнатиев", last_name_orig="Кекев"),
                             mother=person("Параскева", "Никитина"),
                             god_parent1=person("Иоанн", "Григорьев", last_name_orig="Ермилов", status=PEASANT_SON),
                             god_parent2=person("Татиана", "Иоаннова", last_name_orig="Кекева", status=PEASANT_SPOUSE)),
                       ),
          ),
    *page("138об", reviewed=False,
          *birth_month(Month.OCTOBER,
                       birth(54, Gender.MALE, 10, 11,
                             child=person("Иоанн"),
                             father=person("Феодор", "Иоаннов", last_name_orig="Кекев"),
                             mother=person("Феодосия", "Иоаннова"),
                             god_parent1=person("Георгий", "Иоаннов", last_name_orig="Кекев"),
                             god_parent2=person("Александра", "Феодорова", last_name_orig="Кекева", status=PEASANT_MAIDEN),
                             comment="та же пара — «Ѳедоръ Іоанновъ + Ѳеодосія Иванова» — в МК 1919 г. (д.200 "
                                     "л. 13об). Восприемник Георгий Иоаннов по отчеству брат отца (его двойня "
                                     "родилась 1 мая того же года, л. 130об), восприемница Александра Феодорова "
                                     "по отчеству — дочь отца; она же восприемница в 1917 г. (л. 237об)"),
                       ),
          ),
    # Вторая волна (09.11.2026): дети замужних дочерей Кекевых, найденные по имени мужа.
    # reviewed=False: прочитано по сканам один раз, не вычитано (кадры ~1500 px на разворот).
    *page("136об", reviewed=False,
          *birth_month(Month.AUGUST,
                       # мать — Мария Иоанновна Кекева (брак 1912 № 33 с Павлом Михайловичем Мирошкиным); восприемница — её
                       # сестра Евфросиния Иоанновна Кекева
                       birth(40, Gender.FEMALE, 23, 24,
                             child=person("Надежда"),
                             father=person("Павелъ", "Михайловъ", last_name_orig="Мирошкинъ"),
                             mother=person("Марія", "Іоаннова", status=PEASANT_SPOUSE),
                             god_parent1=person("Іоаннъ", "Михайловъ", last_name_orig="Мирошкинъ", status=PEASANT_SON),
                             god_parent2=person("Евфросинія", "Іоаннова", last_name_orig="Кекева", status=PEASANT_MAIDEN)),
                       ),
          ),
    defaults=DEFAULTS,
)
