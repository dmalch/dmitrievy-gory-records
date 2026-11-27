from verso.ru.dsl import (Gender, Month, RecordDefaults, birth, birth_month, birth_records, page,
                          person)
from verso.ru.dsl.statuses import (PEASANT_FEMALE, PEASANT_MAIDEN, PEASANT_MALE, PEASANT_SON,
                                   PEASANT_SPOUSE, PEASANT_WIDOW, PEASANT_ZHONKA, SOLDIER,
                                   SOLDIER_WIFE)

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1916 г.,
# часть первая «О родившихся». ГАВО ф.590 оп.12 д.199, лл. 197об–215об.
#
# TARGETED extract: only the КЕКЕВЪ family (= Кикевъ/Кексевъ). The whole 1916
# birth section was read — 50 мужского и 47 женского пола — and these three are
# the entries where a Кекевъ is a PARENT.
#
# Кекевы стоят и восприемниками, что записано в ../../regional-rules/dmitrievy-gory/README.md,
# а не здесь: Анна Николаева Кекева (№ ж5, л. 199об) и Мария Иоаннова Кекева
# (№ м20, л. 205об; № м38, л. 212об).
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE, status_mother=PEASANT_FEMALE)

dmitrievy_gory_births_1916 = birth_records(
    "ГАВО", "590", "12", "199", "Дмитриевы Горы", "Покровская",
    1916,
    *page("204об", reviewed=False,
          *birth_month(Month.MAY,
                       # в источнике «зап. солдатъ Евѳимій Іоанновъ Кекевъ»; крещён в день рождения. ⚠
                       # Отчество жены здесь читается «Антоніева», но у того же Евфимия она «Марія ВАСИЛЬЕВА»
                       # и в 1913 г. (л. 96об), и в 1918 г. (л. 262об) — то есть выпадает из ряда именно эта
                       # запись. Отчество восприемницы читается неуверенно («Николаева» или «Никонова»)
                       birth(17, Gender.MALE, 1, 1,
                             child=person("Николай"),
                             father=person("Евфимий", "Иоаннов", last_name_orig="Кекев", status=SOLDIER, comment="запасный солдат"),
                             mother=person("Мария", "Антониева"),
                             god_parent1=person("Стефан", "Ермилов", last_name_orig="Майоров", status=PEASANT_SON),
                             god_parent2=person("Евдокия", "Николаева", last_name_orig="Мирошкина", status=PEASANT_MAIDEN)),
                       ),
          ),
    *page("206об", reviewed=False,
          *birth_month(Month.JUNE,
                       birth(25, Gender.MALE, 8, 9,
                             child=person("Иоанн"),
                             father=person("Андрей", "Иоаннов", last_name_orig="Кекев", status=SOLDIER, comment="запасный солдат"),
                             mother=person("Евфросиния", "Алексиева"),
                             god_parent1=person("Димитрий", "Мартынов", last_name_orig="Бондарев", status=PEASANT_SON),
                             god_parent2=person("Параскева", "Николаева", last_name_orig="Мирошкина", status=PEASANT_ZHONKA),
                             comment="этот младенец умер 17 июня 1916 в возрасте 1 недели — запись о смерти № 25, "
                                     "л. 225об. Восприемник Димитрий Мартынов Бондарев — «кр. сынъ Харьковской "
                                     "губ. гор. Старобѣльска»"),
                       ),
          ),
    *page("215об", reviewed=False,
          *birth_month(Month.DECEMBER,
                       birth(47, Gender.FEMALE, 23, 24,
                             child=person("Татиана"),
                             father=person("Григорий", "Васильев", last_name_orig="Кекев", status=SOLDIER),
                             mother=person("Анна", "Романова"),
                             comment="ВОСПРИЕМНИКИ НЕ ЗАПИСАНЫ: л. 215об — последняя левая страница части первой, "
                                     "а обращённый к ней л. 216 занят печатным титулом «Часть вторая, о "
                                     "бракосочетавшихся», так что графы восприемников для декабрьских записей "
                                     "в книге нет"),
                       ),
          ),
    # Вторая волна (09.11.2026): дети замужних дочерей Кекевых и Кузиных, найденные по имени мужа.
    # reviewed=False: прочитано по сканам один раз, не вычитано (кадры ~1500 px на разворот).
    *page("200об", reviewed=False,
          *birth_month(Month.FEBRUARY,
                       # мать — Мария Михайловна Кекева (брак 1914 № 12 с Павлом Ипполитовичем Кузнецовым); восприемник
                       # Иоанн Тимофеевич Савин — сам жених Марии Ипполитовны Кекевой (брак 1916 № 1)
                       birth(9, Gender.FEMALE, 20, 21,
                             child=person("Евдокія"),
                             father=person("Павелъ", "Ипполитовъ", last_name_orig="Кузнецовъ", status=SOLDIER, comment="запасный солдат"),
                             mother=person("Марія", "Михайлова", status=PEASANT_SPOUSE),
                             god_parent1=person("Іоаннъ", "Тимофеевъ", last_name_orig="Савинъ", status=PEASANT_SON),
                             god_parent2=person("Марія", "Іоаннова", last_name_orig="Легкова", status=PEASANT_MAIDEN, comment="отчество читается неуверенно")),
                       ),
          ),
    *page("208об", reviewed=False,
          *birth_month(Month.JULY,
                       # мать — Ксения Иоанновна Кекева (брак 1894 № 26 с Петром Иоанновичем Шиковым), здесь уже «кр. вдова»:
                       # Петр Иоаннович умер 10.04.1916 (ч. 3, № м18), Василий родился после смерти отца.
                       # Восприемник — её сын Иоанн Петрович Шиков (род. 1898). Восприемники на л. 210 (л. 209 — вклеенная
                       # справка общины евангельских христиан)
                       birth(31, Gender.MALE, 24, 25,
                             child=person("Василій"),
                             mother=person("Ксенія", "Іоаннова", last_name_orig="Шикова", status=PEASANT_WIDOW),
                             god_parent1=person("Іоаннъ", "Петровъ", last_name_orig="Шиковъ", status=PEASANT_SON),
                             god_parent2=person("Любовь", "Іоаннова", last_name_orig="Майорова", status=SOLDIER_WIFE)),
                       ),
          ),
    *page("214об", reviewed=False,
          *birth_month(Month.DECEMBER,
                       # мать — Евдокия Георгиевна Кекева (брак 1915 № 1 с Иоанном Максимовичем Липатовым). Иоанн Максимович —
                       # по всему сын Максима Архипповича «Ипаткина» и Феодосии Павловны Кузиной (Иоанн род. 22.06.1897; жених
                       # 1915 г. — «17½»): в этой книге та же семья пишется Липатовыми (№ ж44 ниже), восприемник — брат
                       # Василий Максимович (род. 1899)
                       birth(43, Gender.FEMALE, 8, 9,
                             child=person("Марія"),
                             father=person("Іоаннъ", "Максимовъ", last_name_orig="Липатовъ", status=SOLDIER, comment="«крестьянинъ» исправлено на «солдатъ»"),
                             mother=person("Евдокія", "Георгіева", status=PEASANT_SPOUSE),
                             god_parent1=person("Василій", "Максимовъ", last_name_orig="Липатовъ", status=PEASANT_SON),
                             god_parent2=person("Анна", "Георгіева", last_name_orig="Филатова", status=SOLDIER_WIFE)),
                       # мать — Феодосия Павловна Кузина (брак 1894 № 33 с Максимом Архипповичем, тогда «Ипаткинъ»); здесь
                       # фамилия — «Липатовъ». Восприемник — сын Феодор Максимович (род. 1905)
                       birth(44, Gender.FEMALE, 11, 12,
                             child=person("Татіана"),
                             father=person("Максимъ", "Архиповъ", last_name_orig="Липатовъ"),
                             mother=person("Ѳеодосія", "Павлова", status=PEASANT_SPOUSE),
                             god_parent1=person("Ѳеодоръ", "Максимовъ", last_name_orig="Липатовъ", status=PEASANT_SON),
                             god_parent2=person("Наталія", "Адріанова", last_name_orig="Осипова", status=SOLDIER_WIFE),
                             comment="восприемники вписаны поверх зачёркнутых «солдатъ Іоаннъ Гавриловъ Сотняковъ и кр. дѣвица "
                                     "Марія Николаева …» (фамилия под зачёркиванием не читается)"),
                       ),
          ),
    defaults=DEFAULTS,
)
