from verso.ru.dsl import (Gender, Month, RecordDefaults, birth, birth_month, birth_records, page,
                          person)
from verso.ru.dsl.statuses import (PEASANT_FEMALE, PEASANT_MALE, PEASANT_MAIDEN, PEASANT_SON,
                                   PEASANT_SPOUSE, PEASANT_ZHONKA, SOLDIER)

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1915 г.,
# часть первая «О родившихся». ГАВО ф.590 оп.12 д.199, лл. 158об–179об.
#
# TARGETED extract: only the КЕКЕВЪ family (= Кикевъ/Кексевъ). Весь раздел о
# родившихся прочитан — 77 мужского и 74 женского пола — и это три записи, где
# Кекевъ РОДИТЕЛЬ.
#
# Кекевы гораздо чаще стоят восприемниками; они перечислены в
# ../../regional-rules/dmitrievy-gory/README.md, а не здесь.
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE, status_mother=PEASANT_FEMALE)

dmitrievy_gory_births_1915 = birth_records(
    "ГАВО", "590", "12", "199", "Дмитриевы Горы", "Покровская",
    1915,
    *page("163об", reviewed=False,
          *birth_month(Month.MARCH,
                       birth(22, Gender.FEMALE, 14, 15,
                             child=person("Александра"),
                             father=person("Сергий", "Алексиев", last_name_orig="Кекев", status=SOLDIER, comment="запасный солдат"),
                             mother=person("Екатерина", "Алексиева"),
                             god_parent1=person("Иоанн", "Феодоров", last_name_orig="Маслихин", status=PEASANT_SON),
                             god_parent2=person("Евдокия", "Петрова", last_name_orig="Кондрушина", status=PEASANT_SPOUSE),
                             comment="отец, судя по отчествам детей, — тот Сергий, чьими дочерьми названы "
                                     "Евфросиния и Евдокия Сергиевы Кекевы (восприемницы 1915–1918 гг.)"),
                       ),
          ),
    *page("172об", reviewed=False,
          *birth_month(Month.AUGUST,
                       # тот же Косма Романов Кекев с женой Параскевой записан в 1918 г. (л. 261об, сын
                       # Димитрий). Отчество жены здесь переносится через строку («Ан-/типова») и само по себе
                       # неразборчиво; принято по записи о рождении № ж67 1913 г. (л. 104об), где оно написано
                       # отчётливо — «Антипова». В 1918 г. прочитано «Антониева» — тот лист стоит перечитать.
                       # Восприемник Григорий Петров записан без фамилии
                       birth(47, Gender.FEMALE, 1, 2,
                             child=person("Наталия"),
                             father=person("Косма", "Романов", last_name_orig="Кекев"),
                             mother=person("Параскева", "Антипова"),
                             god_parent1=person("Григорий", "Петров"),
                             god_parent2=person("Елена", "Васильева", last_name_orig="Рыбкина", status=PEASANT_ZHONKA)),
                       ),
          ),
    *page("176об", reviewed=False,
          *birth_month(Month.OCTOBER,
                       birth(69, Gender.MALE, 6, 7,
                             child=person("Иоанн"),
                             father=person("Андрей", "Игнатиев", last_name_orig="Кекев", status=SOLDIER, comment="запасный солдат"),
                             mother=person("Татиана", "Иоаннова"),
                             god_parent1=person("Василий", "Алексиев", last_name_orig="Иванов", status=PEASANT_SON),
                             god_parent2=person("Параскева", "Петрова", last_name_orig="Маслихина", status=PEASANT_ZHONKA),
                             comment="НЕ путать с Андреем Иоанновым Кекевым, у которого сын родился в 1916 г. "
                                     "(л. 206об): здесь отчество отца — «Игнатіевъ», и жена другая"),
                       ),
          ),
    # Вторая волна (09.11.2026): дети замужних дочерей Кекевых, найденные по имени мужа.
    # reviewed=False: прочитано по сканам один раз, не вычитано (кадры ~1500 px на разворот).
    *page("159об", reviewed=False,
          *birth_month(Month.JANUARY,
                       # мать — Екатерина Димитриевна Кекева (брак 1909 № 12 с Александром Георгиевичем Шимаряновым,
                       # там «Шамарын»); восприемник — её брат Петр Димитриевич Кекев
                       birth(5, Gender.FEMALE, 21, 22,
                             child=person("Анна"),
                             father=person("Александръ", "Георгіевъ", last_name_orig="Шимаряновъ"),
                             mother=person("Екатерина", "Димитріева", status=PEASANT_SPOUSE),
                             god_parent1=person("Петръ", "Димитріевъ", last_name_orig="Кекевъ", status=PEASANT_SON),
                             god_parent2=person("Марія", "Косьмина", last_name_orig="Хохлова", status=PEASANT_MAIDEN)),
                       ),
          ),
    *page("163об", reviewed=False,
          *birth_month(Month.MARCH,
                       # мать — Елена Игнатиевна Кекева (брак 1897 № 12 с Алексеем Наумовичем Ивановым); отец умер 3.09.1915
                       # (ч. 3, № м27)
                       birth(21, Gender.FEMALE, 10, 11,
                             child=person("Марія"),
                             father=person("Алексѣй", "Наумовъ", last_name_orig="Ивановъ"),
                             mother=person("Елена", "Игнатіева", status=PEASANT_SPOUSE),
                             god_parent1=person("Ѳеодоръ", "Алексѣевъ", last_name_orig="Ивановъ", status=PEASANT_SON),
                             god_parent2=person("Елена", "Наумова", last_name_orig="Пысина", status=PEASANT_SPOUSE)),
                       ),
          ),
    *page("173об", reviewed=False,
          *birth_month(Month.AUGUST,
                       # мать — Александра Иоанновна Кекева (брак 1905 № 8 с Петром Георгиевичем Шимаряновым); Иоанн умер
                       # 6.10.1915 двух месяцев (ч. 3, № м30)
                       birth(56, Gender.MALE, 8, 9,
                             child=person("Іоаннъ"),
                             father=person("Петръ", "Георгіевъ", last_name_orig="Шимаряновъ", status=SOLDIER, comment="запасный солдат"),
                             mother=person("Александра", "Іоаннова", status=PEASANT_SPOUSE),
                             god_parent1=person("Іоаннъ", "Филипповъ", last_name_orig="Шимаряновъ", status=PEASANT_SON),
                             god_parent2=person("Марія", "Косьмина", last_name_orig="Хохлова", status=PEASANT_MAIDEN)),
                       ),
          ),
    defaults=DEFAULTS,
)
