from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLD, MEASLES, WEAKNESS
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, PEASANT_ZHONKA

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1914 г.,
# часть третья «Объ умершихъ». ГАВО ф.590 оп.12 д.199, лл. 148об–157об.
#
# Прочитан весь раздел на ОБЕ фамилии — Кикев/Кекев и Земсков. Корьевый год:
# больше половины детских записей «отъ кори». Кекевых три, Земсковых нет.
#
# ⚠ Одна запись прошла мимо: 7 февраля умерла «кр. Ефиміи Іоаннова дочь Марія»,
# 2 лет, отъ скарлатины (л. 148об) — БЕЗ ФАМИЛИИ. Евфимий Иоаннов Кекев в селе
# есть, но есть и Евфимий Иоаннов Романов, и Евфимий Иоаннов Ткачев, так что
# приписать её некому.
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE)

dmitrievy_gory_deaths_1914 = death_records(
    "ГАВО", "590", "12", "199", "Дмитриевы Горы", "Покровская",
    1914,
    *page("153об", reviewed=False,
          *death_month(Month.SEPTEMBER,
                       # ⛔ **ВОЗРАСТ ИСПРАВЛЕН 16.09.2026: 9 мѣс., а не 2.** Графа перечитана при 12×: цифра
                       # несёт замкнутую петлю сверху и хвост вниз — это девятка; у двойки этой руки петли нет
                       # вовсе. Прежнее чтение «2 мѣс» и породило помету «записи о рождении не найдено»: оно
                       # требовало рождения в конце июля 1914 г., которого в части первой нет. ✅ **С девяткой
                       # всё сходится день в день**: Марія родилась **10 декабря 1913 г.** (д.199 л. 104об, ч.
                       # 1 № ж67, та же пара — Косма Романовъ Кекевъ и Параскева), и на 24 сентября 1914 г. ей
                       # девять месяцев и две недели. Ни один из двух документов не ошибался — ошибалась
                       # расшифровка. Та же пара записана при рождении дочери Наталии в 1915 г. (л. 172об) и
                       # сына Димитрия в 1918 г. (л. 261об)
                       death(18, Gender.FEMALE, 24, 26,
                             deceased=person("Мария"), age="9 мес",
                             relatives=[relative(person("Косма", "Романов", last_name_orig="Кекев"), Relationship.FATHER)],
                             cause_of_death=MEASLES),
                       ),
          ),
    *page("154об", reviewed=False,
          *death_month(Month.OCTOBER,
                       death(20, Gender.MALE, 11, 13,
                             deceased=person("Николай"), age="2 мес 2 нед",
                             relatives=[relative(person("Иаков", "Сильвестров", last_name_orig="Кекев"), Relationship.FATHER)],
                             cause_of_death=WEAKNESS,
                             comment="это младенец, рождённый 22 июля 1914 — запись о рождении № м38, л. 134об. "
                                     "В источнике возраст — «2½ мес», причина — «отъ слабосилія»"),
                       death(20, Gender.FEMALE, 22, 24,
                             deceased=person("Мария", "Савельева", last_name_orig="Кекева", status=PEASANT_ZHONKA),
                             age=53,
                             cause_of_death=COLD,
                             comment="взрослая Кекева, ни с одной из семей года по записи не связанная: "
                                     "ни мужа, ни детей запись не называет"),
                       ),
          ),
    defaults=DEFAULTS,
)
