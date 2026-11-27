from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import SCARLATINA
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, SOLDIER

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1906 г.,
# часть третья «О умерших». ГАВО ф.590 оп.12 д.**198**, лл. 320–333об
# (титул — л. 320, записи — на лл. 320об–333об). Итог года: м69 + ж55.
#
# Прочитано на ОБЕ фамилии. Кекевых трое, и все три — девочки, унесённые одной
# и той же **осенне-зимней волной скарлатины**; Земсковых нет.
#
# ⚠ **Скарлатина 1906/07 гг. — самое смертоносное, что видели прочитанные годы
# этого прихода.** Она берёт октябрь, ноябрь и декабрь почти без остатка (на
# л. 328 подряд восемь «отъ Скарлатины» из десяти, на л. 332 — семь из
# одиннадцати) и не кончается с годом: январь 1907 г. даёт десять погребений из
# одиннадцати той же причины (ч. 3 1907 г., л. 370). За три месяца она уносит
# у Кекевых троих: двух дочерей Михаила Феодорова (записи ниже) и дочь Евфимия
# Иоаннова, а в январе — сына Феодора Иоаннова.
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE)

dmitrievy_gory_deaths_1906 = death_records(
    "ГАВО", "590", "12", "198", "Дмитриевы Горы", "Покровская",
    1906,
    *page("327об", reviewed=False,
          *death_month(Month.OCTOBER,
                       death(28, Gender.FEMALE, 18, 20,
                             deceased=person("Матрона"), age="8 мес",
                             relatives=[relative(person("Михаил", "Феодоров", last_name_orig="Кекев", status=SOLDIER, comment="запасный солдат"), Relationship.FATHER)],
                             cause_of_death=SCARLATINA,
                             comment="это девочка, рождённая 20 февраля того же года (запись о рождении № ж11, "
                                     "л. 293об): оба конца жизни в одной книге, и возраст сходится день в день. "
                                     "Через четыре дня отец хоронит и вторую дочь (запись № ж30 ниже)"),
                       # старшая дочь той же пары, рождённая **8 февраля 1904 г.** (запись о рождении № ж13,
                       # л. 215об 1904 г.); «2¾» источника точны почти до месяца. Двух дочерей Михаил Феодоров
                       # потерял за четыре дня; больше о его семье корпус пока не знает ничего, кроме имени
                       # жены (Мария Саввина) ⚠ **Первенство снято 05.09.2026**: Михаил Федорович Кекев назван
                       # раньше — рождение 1893 № 10, 1893-04-08.
                       death(30, Gender.FEMALE, 22, 25,
                             deceased=person("Евдокия"), age="2 г 9 мес",
                             relatives=[relative(person("Михаил", "Феодоров", last_name_orig="Кекев", status=SOLDIER, comment="запасный солдат"), Relationship.FATHER)],
                             cause_of_death=SCARLATINA),
                       ),
          ),
    *page("331об", reviewed=False,
          *death_month(Month.DECEMBER,
                       # ЭТО девочка, рождённая **21 марта 1905 г.** (запись о рождении № ж26, л. 254об 1905
                       # г.); «два года» источника округлены — ей был год и восемь месяцев. Имя пары
                       # освободилось и было дано снова — вторая Мария родилась у Евфимия Иоаннова и Марии
                       # Васильевой 21 марта 1908 г. (л. 388об); между ними, 16 января 1907 г., родилась Анна,
                       # умершая полутора лет (л. 334об 1907 г., л. 414об 1908 г.). Трое подряд, и только
                       # третья выжила
                       death(49, Gender.FEMALE, 5, 7,
                             deceased=person("Мария"), age=2,
                             relatives=[relative(person("Евфимий", "Иоаннов", last_name_orig="Кекев", status=SOLDIER, comment="запасный солдат"), Relationship.FATHER)],
                             cause_of_death=SCARLATINA),
                       ),
          ),
    # Вторая волна (09.11.2026): дети замужних дочерей Кекевых и Кузиных, найденные по имени мужа. reviewed=False.
    *page("324об", reviewed=False,
          *death_month(Month.JULY,
                       # Мария — дочь Григория Петровича Рыбкина и Дарьи Романовны Кекевой, род. 7.07.1906 (ч. 1, № ж31)
                       death(13, Gender.FEMALE, 26, 28,
                             deceased=person("Марія"), age="3 нед",
                             relatives=[relative(person("Григорій", "Петровъ", last_name_orig="Рыбкинъ"), Relationship.FATHER)]),
                       ),
          ),
    *page("326об", reviewed=False,
          *death_month(Month.SEPTEMBER,
                       # Андрей — сын Максима Архипповича Ипаткина и Феодосии Павловны Кузиной, род. 10.08.1902 (1902 ч. 1, № м45)
                       death(36, Gender.MALE, 26, 28,
                             deceased=person("Андрей"), age=4,
                             relatives=[relative(person("Максимъ", "Архипповъ", last_name_orig="Ипаткинъ"), Relationship.FATHER)]),
                       ),
          ),
    defaults=DEFAULTS,
)
