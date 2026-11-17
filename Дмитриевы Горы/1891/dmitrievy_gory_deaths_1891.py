from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import DEBILITY
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1891 г., часть третья «О умерших».
# ГАВО ф.590 оп.12 д.197, лл. 27–36об и 59–60об (состав — в `../ARCHIVES.md`).
#
# Вторая волна (09.11.2026): дети замужних дочерей Кекевых, найденные по имени мужа.
# Вычитано владельцем 11.11.2026: № ж21 (причина смерти — слабость, прежде не заведена).

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE)

dmitrievy_gory_deaths_1891 = death_records(
    "ГАВО", "590", "12", "197", "Дмитриевы Горы", "Покровская",
    1891,
    *page("28об",
          *death_month(Month.MAY,
                       # Александра — дочь Николая Васильевича Горбачева и Марфы Максимовны Кекевой, род. 17.04.1891
                       # (ч. 1, л. 6об, № ж17)
                       death(21, Gender.FEMALE, 9, 10,
                             deceased=person("Александра"), age="3 нед",
                             relatives=[relative(person("Николай", "Васильевъ", last_name_orig="Горбачевъ"), Relationship.FATHER)],
                             cause_of_death=DEBILITY),
                       ),
          ),
    defaults=DEFAULTS,
)
