from verso.ru.dsl import (Gender, Month, RecordDefaults, birth, birth_month, birth_records, page,
                          person)
from verso.ru.dsl.statuses import (PEASANT_FEMALE, PEASANT_MAIDEN, PEASANT_MALE, PEASANT_SON,
                                   PEASANT_SPOUSE, PEASANT_ZHONKA, SOLDIER, UNTER_OFFICER)

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1912 г.,
# часть первая «О родившихся». ГАВО ф.590 оп.12 д.199, лл. 36об–60об.
#
# Прочитано на ОБЕ фамилии — Кикев/Кекев и Земсков. Семь записей, где Кекев
# родитель — больше, чем в любом другом прочитанном году; Земсковых нет.
#
# Фолиация альбома 1912 г. проверена по самим страницам и совпадает с именами
# файлов (в отличие от 1913 г., см. ARCHIVES.md). Вложенные посторонние листы:
# лл. 37, 38, 44, 49, 51 — советские справки 1920-х–30-х гг.; из-за л. 37 разворот
# л. 36об смотрит на л. 39, а из-за л. 44 разворот л. 43об — на л. 45.
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE, status_mother=PEASANT_FEMALE)

dmitrievy_gory_births_1912 = birth_records(
    "ГАВО", "590", "12", "199", "Дмитриевы Горы", "Покровская",
    1912,
    *page("40об", reviewed=False,
          *birth_month(Month.FEBRUARY,
                       birth(11, Gender.FEMALE, 19, 20,
                             child=person("Клавдия"),
                             father=person("Евфимий", "Иванов", last_name_orig="Кекев", status=SOLDIER, comment="запасный солдат"),
                             mother=person("Мария", "Васильева"),
                             god_parent1=person("Косма", "Петров", last_name_orig="Кохлов", status=UNTER_OFFICER, comment="старший унтер-офицер"),
                             god_parent2=person("Мария", "Евфимиева", last_name_orig="Макарова", status="жена волостного писаря"),
                             comment="третье независимое подтверждение пары: «Марія Васильева» стоит женой Евфимия "
                                     "и здесь, и в 1913 г. (л. 96об), и в 1918 г. (л. 262об) — «Марія Антоніева» "
                                     "записи 1916 г. остаётся единственным выпадающим чтением"),
                       ),
          ),
    *page("43об", reviewed=False,
          *birth_month(Month.APRIL,
                       birth(20, Gender.MALE, 22, 23,
                             child=person("Николай"),
                             father=person("Иоанн", "Михайлов", last_name_orig="Кекев"),
                             mother=person("Наталия", "Георгиева"),
                             god_parent1=person("Николай", "Димитриев", last_name_orig="Кекев", status=PEASANT_SON),
                             god_parent2=person("Евфросиния", "Иоаннова", last_name_orig="Кекева", status=PEASANT_MAIDEN),
                             comment="отец — тот Иоанн Михайлов, что пять раз поручитель в 1914 г. и ещё раз в "
                                     "1916 г.; здесь он впервые в своей записи. Восприемник Николай Димитриев — "
                                     "четвёртый брат к Александру, Петру и Феодору Димитриевым. Восприемники на "
                                     "л. 45 (из-за вложенного л. 44 разворот смещён)"),
                       ),
          ),
    *page("45об", reviewed=False,
          *birth_month(Month.MAY,
                       birth(26, Gender.MALE, 14, 15,
                             child=person("Феодор"),
                             father=person("Косма", "Романов", last_name_orig="Кекев"),
                             mother=person("Параскева", "Антипина"),
                             god_parent1=person("Василий", "Иаковлев", last_name_orig="Залетин", status=SOLDIER, comment="запасный солдат"),
                             god_parent2=person("Анисия", "Павлова", last_name_orig="Кобзина", status=PEASANT_ZHONKA),
                             comment="этот мальчик умер 26 января 1913 в возрасте 1 года — запись о смерти № м9, "
                                     "л. 114об. Отчество матери здесь «Антипина», в 1913 г. «Антипова» — один "
                                     "корень; «Антоніева» записей 1915 и 1918 гг. из ряда выпадает. Восприемница — "
                                     "крестьянка Рязанской губ., с. Истопника"),
                       # ЭТА Елена умерла 22 декабря того же года (запись о смерти № ж33, л. 78об), и в 1914
                       # г. у той же пары родилась ВТОРАЯ Елена (л. 130об) — имя дано повторно. Восприемник
                       # Игнатий Феодоров по отчеству — брат отца, и его детьми по отчеству оказываются Андрей
                       # Игнатиев (1915, л. 176об) и Феодор Игнатиев (1914, л. 136об)
                       birth(26, Gender.FEMALE, 21, 22,
                             child=person("Елена"),
                             father=person("Андрей", "Феодоров", last_name_orig="Кекев"),
                             mother=person("Иулиания", "Иоаннова"),
                             god_parent1=person("Игнатий", "Феодоров", last_name_orig="Кекев"),
                             god_parent2=person("Варвара", "Андреева", last_name_orig="Кекева", status=PEASANT_MAIDEN)),
                       ),
          ),
    *page("52об", reviewed=False,
          *birth_month(Month.AUGUST,
                       birth(49, Gender.FEMALE, 19, 20,
                             child=person("Анна"),
                             father=person("Сергий", "Алексиев", last_name_orig="Кекев", status=SOLDIER, comment="запасный солдат"),
                             mother=person("Екатерина", "Алексиева"),
                             god_parent1=person("Стефан", "Григорьев", last_name_orig="Скурлетов"),
                             god_parent2=person("Татиана", "Филиппова", last_name_orig="Кандрушина", status=PEASANT_MAIDEN),
                             comment="через две недели после этих родов у пары умер двухлетний сын Павел — "
                                     "запись о смерти № м27, л. 74об. Та же пара крестит Александру в 1915 г. "
                                     "(л. 163об)"),
                       birth(50, Gender.FEMALE, 24, 25,
                             child=person("Любовь"),
                             father=person("Евфимий", "Георгиев", last_name_orig="Кекев"),
                             mother=person("Анна", "Климентиева"),
                             god_parent1=person("Симеон", "Климентов", last_name_orig="Шишков"),
                             god_parent2=person("Евдокия", "Георгиева", last_name_orig="Кекева", status=PEASANT_MAIDEN),
                             comment="восприемница Евдокия Георгиева по отчеству — сестра отца; она же невеста "
                                     "брака № 1 1915 г. (л. 182об). Восприемник Симеон Климентов по отчеству — "
                                     "брат матери"),
                       ),
          ),
    *page("53об", reviewed=False,
          *birth_month(Month.SEPTEMBER,
                       # ⚠ ЭТА ЗАПИСЬ ЗАКРЫВАЕТ ЗАГАДКУ 1917 ГОДА. В записи о рождении № м5 1917 г. (л. 238об)
                       # писец правил всё подряд, а отчество отца «Андреевъ» густо зачеркнул, не вписав
                       # замены, и пара осталась как «Іоаннъ … Кекевъ + Татіана Онисимова». Вот она же за пять
                       # лет до того, целиком. Младенец умер 29 сентября двух недель от роду — запись о смерти
                       # № м30, л. 75об
                       birth(52, Gender.MALE, 19, 20,
                             child=person("Михаил"),
                             father=person("Иоанн", "Андреев", last_name_orig="Кекев"),
                             mother=person("Татиана", "Онисимова"),
                             god_parent1=person("Иоанн", "Иаковлев", last_name_orig="Царев"),
                             god_parent2=person("Варвара", "Андреева", last_name_orig="Кекева", status=PEASANT_MAIDEN)),
                       ),
          ),
    # Вторая волна (09.11.2026): дети замужних дочерей Кекевых, найденные по имени мужа.
    # reviewed=False: прочитано по сканам один раз, не вычитано (кадры ~1500 px на разворот).
    *page("59об", reviewed=False,
          *birth_month(Month.DECEMBER,
                       # мать — Дарья Романовна Кекева (брак 1894 № 34 с Григорием Петровичем Рыбкиным); восприемник — их сын
                       # Иаков
                       birth(69, Gender.MALE, 16, 17,
                             child=person("Василій"),
                             father=person("Григорій", "Петровъ", last_name_orig="Рыбкинъ"),
                             mother=person("Дарія", "Романова", status=PEASANT_SPOUSE),
                             god_parent1=person("Іаковъ", "Григорьевъ", last_name_orig="Рыбкинъ", status=PEASANT_SON),
                             god_parent2=person("Елена", "Васильева", last_name_orig="Рыбкина", status=PEASANT_ZHONKA),
                             comment="день крещения закрыт пометой о выданном свидетельстве — «17» читается неуверенно"),
                       # мать — Елена Игнатьевна Кекева (брак 1897 № 12 с Алексеем Наумовичем Ивановым); восприемник — их сын
                       # Василий
                       birth(71, Gender.MALE, 25, 26,
                             child=person("Іоаннъ"),
                             father=person("Алексій", "Наумовъ", last_name_orig="Ивановъ"),
                             mother=person("Елена", "Игнатіева", status=PEASANT_SPOUSE),
                             god_parent1=person("Василій", "Алексѣевъ", last_name_orig="Ивановъ", status=PEASANT_SON),
                             god_parent2=person("Елена", "Наумова", last_name_orig="Пысина", status=PEASANT_ZHONKA, comment="фамилия читается неуверенно")),
                       ),
          ),
    defaults=DEFAULTS,
)
