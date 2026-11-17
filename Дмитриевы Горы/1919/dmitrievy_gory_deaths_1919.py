from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import DIARRHEA, OLD_AGE, WEAKNESS
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1919 г.,
# часть третья «Объ умершихъ». ГАВО ф.590 оп.12 д.200.
#
# TARGETED extract: only the КЕКЕВЪ / КИКЕВЪ family. The 1919 death section
# runs л. 43об–52об and holds 70 deaths (38 муж. + 32 жен.); all of it was read
# and these three are every entry naming the family. Часть вторая
# «О бракосочетавшихся» (л. 34об–40об, 30 браков) names none of them at all.
#
# ⚠ The book does NOT stop at 1919: from л. 53об the same volume carries 1934
# death entries, and the priest drafted a rough birth register over the blank
# and printed pages (л. 33об, 34, 40об). Neither is transcribed here — see
# ../CLAUDE.md.
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE)

dmitrievy_gory_deaths_1919 = death_records(
    "ГАВО", "590", "12", "200", "Дмитриевы Горы", "Покровская",
    1919,
    *page("44об", reviewed=False,
          *death_month(Month.FEBRUARY,
                       death(4, Gender.FEMALE, 10, 12,
                             deceased=person("Иулиания", "Андреева", last_name_orig="Кекева", status="крестьянская вдова"),
                             age=70, cause_of_death=OLD_AGE),
                       ),
          ),
    *page("45об", reviewed=False,
          *death_month(Month.APRIL,
                       death(14, Gender.MALE, 10, 12,
                             deceased=person("Иоанн"), age="10 мес",
                             relatives=[relative(person("Евфимий", "Иванов", last_name_orig="Кекев"), Relationship.FATHER)],
                             cause_of_death=WEAKNESS),
                       ),
          ),
    *page("48об", reviewed=False,
          *death_month(Month.JULY,
                       death(23, Gender.MALE, 6, 8,
                             deceased=person("Василий"), age="6 мес",
                             relatives=[relative(person("Павел", "Федоров", last_name_orig="Кекев"), Relationship.FATHER)],
                             cause_of_death=DIARRHEA,
                             comment="это младенец, рождённый 21 января 1919 — запись о рождении № 8, л. 3об, где отец записан «Кикевъ». Одно и то же лицо в двух написаниях"),
                       ),
          ),
    # Вторая волна (09.11.2026): дети замужних дочерей Кекевых. reviewed=False.
    *page("48об", reviewed=False,
          *death_month(Month.JULY,
                       # Григорий — сын Иоанна Тимофеевича Савина и Марии Кекевой, род. 17.01.1919 (ч. 1, № м5)
                       death(25, Gender.MALE, 8, 10,
                             deceased=person("Григорій"), age="7 мес",
                             relatives=[relative(person("Іоаннъ", "Тимоѳеевъ", last_name_orig="Савинъ"), Relationship.FATHER)]),
                       ),
          ),
    defaults=DEFAULTS,
)
