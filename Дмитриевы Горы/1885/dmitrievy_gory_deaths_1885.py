from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import PLEURISY
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1885 г., часть третья «О умерших».
# ГАВО ф.590 оп.12 д.196, лл. 263об–276об (титул — л. 263; состав — в `../ARCHIVES.md`).
#
# Вторая волна (09.11.2026): дети замужних дочерей Кекевых, найденные по имени мужа.
# Вычитано владельцем 11.11.2026.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE)

dmitrievy_gory_deaths_1885 = death_records(
    "ГАВО", "590", "12", "196", "Дмитриевы Горы", "Покровская",
    1885,
    *page("275об",
          *death_month(Month.NOVEMBER,
                       # Макарий — сын Николая Васильевича Горбачева и Марфы Максимовны Кекевой, род. 20.07.1885 (ч. 1,
                       # л. 239об, № м34, где отец записан «Горячевъ»). Здесь отец назван без фамилии
                       death(55, Gender.MALE, 5, 6,
                             deceased=person("Макарій"), age="3 мес 2 нед",
                             relatives=[relative(person("Николай", "Васильевъ"), Relationship.FATHER)],
                             cause_of_death=PLEURISY),
                       ),
          ),
    defaults=DEFAULTS,
)
