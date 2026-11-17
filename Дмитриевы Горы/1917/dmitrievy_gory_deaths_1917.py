from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import WEAKNESS
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, SOLDIER

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1917 г.,
# часть третья «Объ умершихъ». ГАВО ф.590 оп.12 д.199, and NOT in one run:
# январь — л. 284об (bound among the 1919 leaves, the year left blank on the
# form), февраль и начало марта — л. 255об, the rest — лл. 248об–254об. See
# ARCHIVES.md § «Оговорки по д. 199» → «1918 и 1919 гг.».
#
# TARGETED extract: only the КЕКЕВЪ family. Лл. 248об–254об were read first —
# a bad dysentery year, most entries are infants «отъ дизентеріи» — and gave
# the August entry. January and 255об were found on 30.09.2026: January adds
# Николай, 255об names no Кекевъ.
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE)

dmitrievy_gory_deaths_1917 = death_records(
    "ГАВО", "590", "12", "199", "Дмитриевы Горы", "Покровская",
    1917,
    *page("284об", reviewed=False,
          *death_month(Month.JANUARY,
                       death(6, Gender.MALE, 23, 25,
                             deceased=person("Николай"), age=2,
                             relatives=[relative(person("Георгій", "Іоанновъ", last_name_orig="Кекевъ"), Relationship.FATHER)],
                             comment="лист подшит в деле среди листов 1919 г., год на бланке не проставлен; 1917-й "
                                     "доказан счётом (январь — м1–8, ж1; л. 255об продолжает с ж2 и м9) и Иоанном "
                                     "Андреевым Залетиным того же листа: † 20 января «3 нед.», рождён 28 декабря 1916 "
                                     "(л. 215об, № м50). Это близнец Николай, рождённый 1 мая 1914 (запись о рождении "
                                     "№ м24, л. 130об): ему 2 г. 8 мес.; старший Николай этого отца (рождён 1901) "
                                     "погребён в 1905 г. Причина смерти стоит на правой половине разворота, а её в деле нет"),
                       ),
          ),
    *page("253об", reviewed=False,
          *death_month(Month.AUGUST,
                       death(24, Gender.FEMALE, 17, 19,
                             deceased=person("Наталия"), age="3 нед",
                             relatives=[relative(person("Алексий", "Николаев", last_name_orig="Кекев", status=SOLDIER), Relationship.FATHER)],
                             cause_of_death=WEAKNESS,
                             comment="это младенец, рождённый 29 июля 1917 — запись о рождении № 21, л. 237об"),
                       ),
          ),
    # Вторая волна (09.11.2026): мужья и дети замужних дочерей Кекевых. reviewed=False.
    *page("255об", reviewed=False,
          *death_month(Month.MARCH,
                       # Павел Ипполитович Кузнецов — муж Марии Михайловны Кекевой (брак 1914 № 12); дочь Евдокия род. 20.02.1916,
                       # †23.06.1916
                       death(10, Gender.MALE, 4, 6,
                             deceased=person("Павелъ", "Ипполитовъ", last_name_orig="Кузнецовъ"), age=22),
                       ),
          ),
    defaults=DEFAULTS,
)
