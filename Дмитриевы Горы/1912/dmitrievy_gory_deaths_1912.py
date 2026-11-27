from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import SCARLATINA, WEAKNESS
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, SOLDIER

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1912 г.,
# часть третья «Объ умершихъ». ГАВО ф.590 оп.12 д.199, лл. 69об–78об.
#
# Прочитано на ОБЕ фамилии. Скарлатинный год, как и следующий. Кекевых три,
# Земсковых нет. Все три записи смыкаются с записями о рождении: два младенца
# этого же года и один двухлетний.
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE)

dmitrievy_gory_deaths_1912 = death_records(
    "ГАВО", "590", "12", "199", "Дмитриевы Горы", "Покровская",
    1912,
    *page("74об", reviewed=False,
          *death_month(Month.SEPTEMBER,
                       death(27, Gender.MALE, 5, 7,
                             deceased=person("Павел"), age=2,
                             relatives=[relative(person("Сергий", "Алексиев", last_name_orig="Кекев", status=SOLDIER, comment="запасный солдат"), Relationship.FATHER)],
                             cause_of_death=SCARLATINA,
                             comment="умер через две недели после рождения сестры Анны (запись о рождении № ж49, "
                                     "л. 52об). Родился 9 января 1910 г. — метрика ч. 1 № м1 того года, те же "
                                     "родители; прожил 2 года 8 месяцев, что сходится с записанными «2»"),
                       ),
          ),
    *page("75об", reviewed=False,
          *death_month(Month.SEPTEMBER,
                       death(30, Gender.MALE, 29, 1, b_month=Month.OCTOBER,
                             deceased=person("Михаил"), age="2 нед",
                             relatives=[relative(person("Иоанн", "Андреев", last_name_orig="Кекев"), Relationship.FATHER)],
                             cause_of_death=WEAKNESS,
                             comment="это младенец, рождённый 19 сентября 1912 — запись о рождении № м52, "
                                     "л. 53об. Погребён 1 октября, то есть уже следующим месяцем"),
                       ),
          ),
    *page("78об", reviewed=False,
          *death_month(Month.DECEMBER,
                       death(33, Gender.FEMALE, 22, 24,
                             deceased=person("Елена"),
                             relatives=[relative(person("Андрей", "Феодоров", last_name_orig="Кекев", status=SOLDIER, comment="запасный солдат"), Relationship.FATHER)],
                             comment="это девочка, рождённая 21 мая 1912 — запись о рождении № ж26, л. 45об; на "
                                     "момент смерти ей семь месяцев, но графа «Лѣта» на этой последней странице "
                                     "не заполнена, и причина смерти не записана. В 1914 г. у той же пары "
                                     "родилась вторая Елена (л. 130об) — имя дано повторно"),
                       ),
          ),
    # Вторая волна (09.11.2026): дети замужних дочерей Кекевых, найденные по имени мужа. reviewed=False.
    *page("69об", reviewed=False,
          *death_month(Month.JANUARY,
                       # Василий — сын Петра Георгиевича Шимарянова и Александры Иоанновны Кекевой, род. 29.12.1911 (1911 ч. 1, № м67)
                       death(None, Gender.MALE, 11, 13,
                             deceased=person("Василій"), age="2 нед", comment="номер записи не виден",
                             relatives=[relative(person("Петръ", "Георгіевъ", last_name_orig="Шимаряновъ"), Relationship.FATHER)]),
                       ),
          ),
    defaults=DEFAULTS,
)
