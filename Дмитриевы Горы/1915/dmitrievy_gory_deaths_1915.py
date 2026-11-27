from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import CONSUMPTION
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, PEASANT_WIDOW, SOLDIER

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1915 г.,
# часть третья «Объ умершихъ». ГАВО ф.590 оп.12 д.199, лл. 219об–229об.
#
# ⚠ ЭТОТ ФАЙЛ — НЕ РЕЗУЛЬТАТ ПРОХОДА ПО ЗЕМСКОВЫМ. Весь раздел о умерших за 1915 г.
# прочитан, но ТАРГЕТИРОВАННО НА КЕКЕВЫХ, и Кекевых в нём нет ни одного. Запись ниже —
# Земсков, замеченный попутно. Земсковы (двор 4 переписи 1897, свойственники Кикевых)
# входят в проход начиная с 1914 г. и глубже; годы 1915–1919 на них НЕ проверялись,
# так что отсутствие других Земсковых здесь НИЧЕГО не доказывает.
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE)

dmitrievy_gory_deaths_1915 = death_records(
    "ГАВО", "590", "12", "199", "Дмитриевы Горы", "Покровская",
    1915,
    *page("187об", reviewed=False,
          *death_month(Month.APRIL,
                       # в источнике фамилия отца стоит в родительном падеже — «Николая Ѳедорова ЗЕМСКАГО», то
                       # есть прилагательная форма «Земскій», тогда как перепись 1897 г. пишет «Земсковъ»;
                       # вариант сводить преференс-пином, не правкой имени. Николай Феодоров по отчеству —
                       # брат Игната Феодорова Земскова (двор 4 № 3 переписи 1897)
                       death(9, Gender.MALE, 26, 28,
                             deceased=person("Петр"), age=21,
                             relatives=[relative(person("Николай", "Феодоров", last_name_orig="Земский"), Relationship.FATHER)],
                             cause_of_death=CONSUMPTION),
                       ),
          ),
    # Вторая волна (09.11.2026): мужья и дети замужних дочерей Кекевых. reviewed=False.
    # Раздел о умерших 1915 г. стоит на лл. 184об–196об (а не 219об–229об, как в шапке выше).
    *page("192об", reviewed=False,
          *death_month(Month.SEPTEMBER,
                       # Алексей Наумович Иванов — муж Елены Игнатиевны Кекевой (брак 1897 № 12); дочь Мария род. 10.03.1915
                       death(27, Gender.MALE, 3, 5,
                             deceased=person("Алексѣй", "Наумовъ", last_name_orig="Ивановъ"), age=36),
                       ),
          *death_month(Month.OCTOBER,
                       # Иоанн — сын Петра Георгиевича Шимарянова и Александры Иоанновны Кекевой, род. 8.08.1915 (ч. 1, № м56)
                       death(30, Gender.MALE, 6, 8,
                             deceased=person("Іоаннъ"), age="2 мес",
                             relatives=[relative(person("Петръ", "Георгіевъ", last_name_orig="Шимаряновъ", status=SOLDIER, comment="запасный солдат"), Relationship.FATHER)]),
                       ),
          ),
    *page("194об", reviewed=False,
          *death_month(Month.NOVEMBER,
                       # Екатерина — дочь Марии Феодоровны Кекевой (брак 1896 № 8 с Феодором Петровичем Ореховым), вдовы с
                       # 1905 г.; Екатерина род. в 1911 г. без отца
                       death(30, Gender.FEMALE, 17, 19,
                             deceased=person("Екатерина"), age=4,
                             relatives=[relative(person("Марія", "Ѳеодорова", last_name_orig="Орѣхова", status=PEASANT_WIDOW), Relationship.MOTHER)]),
                       ),
          ),
    defaults=DEFAULTS,
)
