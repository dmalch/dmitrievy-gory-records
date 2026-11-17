from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import WEAKNESS
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, PEASANT_WIDOW

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1916 г.,
# часть третья «Объ умершихъ». ГАВО ф.590 оп.12 д.199, лл. 219об–229об.
#
# TARGETED extract: only the КЕКЕВЪ family. Вся часть третья прочитана —
# корьевый год, большинство записей детские «отъ кори» — и это единственная
# запись, называющая семью.
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE)

dmitrievy_gory_deaths_1916 = death_records(
    "ГАВО", "590", "12", "199", "Дмитриевы Горы", "Покровская",
    1916,
    *page("225об", reviewed=False,
          *death_month(Month.JUNE,
                       death(25, Gender.MALE, 17, 19,
                             deceased=person("Иоанн"), age="1 нед",
                             relatives=[relative(person("Андрей", "Иоаннов", last_name_orig="Кекев", status="запасный солдат"), Relationship.FATHER)],
                             cause_of_death=WEAKNESS,
                             comment="это младенец, рождённый 8 июня 1916 — запись о рождении № 25, л. 206об"),
                       ),
          ),
    # Вторая волна (09.11.2026): мужья и дети замужних дочерей Кекевых. reviewed=False.
    *page("222об", reviewed=False,
          *death_month(Month.APRIL,
                       # Мария — дочь Алексея Наумовича Иванова (†3.09.1915) и Елены Игнатиевны Кекевой, род. 10.03.1915
                       # (1915 ч. 1, № ж21)
                       death(9, Gender.FEMALE, 5, 7,
                             deceased=person("Марія"), age=1,
                             relatives=[relative(person("Елена", "Игнатіева", last_name_orig="Иванова", status=PEASANT_WIDOW), Relationship.MOTHER)]),
                       ),
          ),
    *page("223об", reviewed=False,
          *death_month(Month.APRIL,
                       # Петр Иоаннович Шиков — муж Ксении Иоанновны Кекевой (брак 1894 № 26); сын Василий родился уже после
                       # его смерти, 24.07.1916 (ч. 1, № м31)
                       death(18, Gender.MALE, 10, 12,
                             deceased=person("Петръ", "Іоанновъ", last_name_orig="Шиковъ"), age=40),
                       ),
          ),
    *page("225об", reviewed=False,
          *death_month(Month.JUNE,
                       # Евдокия — дочь Павла Ипполитовича Кузнецова и Марии Михайловны Кекевой, род. 20.02.1916 (ч. 1, № ж9)
                       death(16, Gender.FEMALE, 23, 25,
                             deceased=person("Евдокія"), age="3 мес",
                             relatives=[relative(person("Павелъ", "Ипполитовъ", last_name_orig="Кузнецовъ", status="запасный солдат"), Relationship.FATHER)]),
                       ),
          ),
    *page("229об", reviewed=False,
          *death_month(Month.NOVEMBER,
                       # Наталия — дочь Петра Иоанновича Шикова (†10.04.1916) и Ксении Иоанновны Кекевой, род. 19.08.1913
                       death(34, Gender.FEMALE, 25, 27,
                             deceased=person("Наталія"), age=3,
                             relatives=[relative(person("Ксенія", "Іоаннова", last_name_orig="Шикова", status=PEASANT_WIDOW), Relationship.MOTHER)]),
                       ),
          *death_month(Month.DECEMBER,
                       # Мария — дочь Иоанна Евфимиевича Юкачева и Матроны Романовны Кекевой (брак 1899 № 18); её рождения
                       # (~1911) во второй волне не найдено
                       death(35, Gender.FEMALE, 27, 29,
                             deceased=person("Марія"), age=5,
                             relatives=[relative(person("Іоаннъ", "Евфиміевъ", last_name_orig="Юкачевъ"), Relationship.FATHER)]),
                       ),
          ),
    defaults=DEFAULTS,
)
