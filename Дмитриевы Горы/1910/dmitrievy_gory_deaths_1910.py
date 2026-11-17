from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import DIARRHEA, WHOOPING_COUGH
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1910 г.,
# часть третья «Об умерших». ГАВО ф.590 оп.12 д.**198**, лл. 417–426
# (записи — на лл. 417об–426об). Часть лежит В ДРУГОМ КОНЦЕ ДЕЛА, чем части
# первая и вторая того же года: см. заголовок births-файла.
#
# Прочитано на ОБЕ фамилии. Кекевых двое, и оба — младенцы этого же года,
# сыновья двух братьев Иоанновых; Земсковых нет. Год в целом тяжёлый —
# 49 мужского и 49 женского пола, с летней волной поноса и осенней коклюша.
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE)

dmitrievy_gory_deaths_1910 = death_records(
    "ГАВО", "590", "12", "198", "Дмитриевы Горы", "Покровская",
    1910,
    *page("421об", reviewed=False,
          *death_month(Month.JUNE,
                       death(23, Gender.MALE, 27, 29,
                             deceased=person("Алексий"), age="4 мес",
                             relatives=[relative(person("Феодор", "Иоаннов", last_name_orig="Кекев"), Relationship.FATHER)],
                             cause_of_death=DIARRHEA,
                             comment="это младенец, рождённый 6 марта того же года (запись о рождении № м11, "
                                     "л. 162об); в источнике возраст «около 4 месяцев». Оба конца жизни — "
                                     "в одной книге. Мать, не названная здесь, — Пелагия Феодорова, первая "
                                     "жена; в сентябре 1913 г. отец венчается вторым браком"),
                       ),
          ),
    *page("425об", reviewed=False,
          *death_month(Month.OCTOBER,
                       death(44, Gender.MALE, 15, 17,
                             deceased=person("Алексий"), age="8 мес",
                             relatives=[relative(person("Георгий", "Иоаннов", last_name_orig="Кекев"), Relationship.FATHER)],
                             cause_of_death=WHOOPING_COUGH,
                             comment="это младенец, рождённый 9 февраля того же года (запись о рождении № м6, "
                                     "л. 161об). У той же пары через два с половиной месяца родится дочь "
                                     "Евдокия, умершая трёх дней 2 января 1911 г. (л. 28об д.199): двое детей "
                                     "подряд, ни один не пережил года"),
                       ),
          ),
    # Вторая волна (09.11.2026): мужья и дети замужних дочерей Кекевых. reviewed=False.
    *page("423об", reviewed=False,
          *death_month(Month.JULY,
                       # Феодор Филиппович Шимарянов — муж Марии Георгиевны Кекевой (брак 1903 № 7); дети Николай 1904,
                       # Михаил 1907, Василий 1909
                       death(31, Gender.MALE, 30, 1, b_month=Month.AUGUST,
                             deceased=person("Ѳеодоръ", "Филипповъ", last_name_orig="Шимаряновъ"), age=25),
                       ),
          ),
    *page("426об", reviewed=False,
          *death_month(Month.DECEMBER,
                       # Александр — сын Александра Георгиевича Шимарянова и Екатерины Димитриевны Кекевой, род. 17.10.1910
                       # (ч. 1, № м63)
                       death(48, Gender.MALE, 21, 22,
                             deceased=person("Александръ"),
                             relatives=[relative(person("Александръ", "Георгіевъ", last_name_orig="Шимаряновъ"), Relationship.FATHER)],
                             comment="в графе смерти «24» при погребении 22 — так читается; возраст не записан"),
                       ),
          ),
    defaults=DEFAULTS,
)
