from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import CONSUMPTION, NATURAL, SCARLATINA
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, PEASANT_WIDOW, PEASANT_ZHONKA

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1911 г.,
# часть третья «Об умерших». ГАВО ф.590 оп.12 д.199, лл. 28об–34об
# (титул части — л. 28; л. 35об чист).
#
# Прочитано на ОБЕ фамилии. Шесть кекевских записей — больше, чем в любом из
# прочитанных 1912–1919 гг.; Земсковых нет. ЧЕТЫРЕ из шести — в январе, и это
# один и тот же зимний мор: инфлюэнца, скарлатина, скоропостижная смерть.
# Четверо взрослых из шести — три женщины 52, 60 и 79 лет и двое младенцев.
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE)

dmitrievy_gory_deaths_1911 = death_records(
    "ГАВО", "590", "12", "199", "Дмитриевы Горы", "Покровская",
    1911,
    *page("28об", reviewed=False,
          *death_month(Month.JANUARY,
                       death(1, Gender.FEMALE, 2, 4,
                             deceased=person("Евдокия"), age="3 дн",
                             relatives=[relative(person("Георгий", "Иоаннов", last_name_orig="Кекев"), Relationship.FATHER)],
                             cause_of_death="инфлюэнца",
                             comment="трёх дней от роду, то есть родилась около 30 декабря 1910 г.: записи о её "
                                     "рождении в этом деле нет и быть не может — д.199 открывается 1911 годом, "
                                     "искать в д.198 (1900–1910). В августе того же года у той же пары "
                                     "родилась дочь Наталия (запись о рождении № ж51, л. 14об)"),
                       death(3, Gender.FEMALE, 3, 5,
                             deceased=person("Екатерина", "Иоаннова", last_name_orig="Кекева", status=PEASANT_WIDOW),
                             age=79,
                             cause_of_death=NATURAL,
                             comment="старейшая Кекева из всех прочитанных лет: по возрасту род. ок. 1832 г. "
                                     "Вдова; чья — в записи не сказано, и по имеющимся годам не выводится"),
                       ),
          ),
    *page("29об", reviewed=False,
          *death_month(Month.JANUARY,
                       # ✅ **СЛОВО ПРОЧИТАНО 16.09.2026 (владельцем корпуса): «ТОЖЕ».** В подлиннике
                       # «крестьянская женка Агрипина Авраамиева **ОСИПОВА ТОЖЕ КЕКЕВА**». Прежняя помета —
                       # «слово прочесть не удалось даже при 10×, по смыслу вероятно „по мужу“» — снята. 🔴
                       # **Это та же алиасная связка, которой писцы этого прихода соединяют уличную фамилию с
                       # родовой** — «Кекевъ тожъ Земсковъ» (1896–1902), «Кекевъ или Кузинъ» (1901). Значит
                       # «Осиповы» стоит в одном ряду с Земсковыми, Кузиными и Акиллинами, а не читается как
                       # девичья фамилия автоматически. ⚠ Но и утверждать четвёртую уличную фамилию рано:
                       # связка «X тоже Y» у ЖЁНКИ может нести и девичью фамилию, тогда как все прежние «тожъ»
                       # корпуса стоят при МУЖЧИНАХ. Осиповичей-Кекевых корпус не знает, Авраамиевичей тоже.
                       # Записана под той фамилией, что стоит последней
                       death(7, Gender.FEMALE, 24, 27,
                             deceased=person("Агриппина", "Авраамиева", last_name_orig="Кекева", status=PEASANT_ZHONKA),
                             age=52,
                             cause_of_death="скоропостижно"),
                       death(8, Gender.FEMALE, 26, 28,
                             deceased=person("Евдокия"), age=0.5,
                             relatives=[relative(person("Григорий", "Андреев", last_name_orig="Кекев"), Relationship.FATHER)],
                             cause_of_death=SCARLATINA,
                             comment="полугода: родилась около июля 1910 г., записи о рождении в этом деле нет "
                                     "(искать в д.198). В ноябре того же года у той же пары родилась дочь "
                                     "Екатерина (запись о рождении № ж63, л. 18об)"),
                       ),
          ),
    *page("30об", reviewed=False,
          *death_month(Month.MARCH,
                       death(11, Gender.FEMALE, 5, 7,
                             deceased=person("Мария", "Прокопиева", last_name_orig="Кекева", status=PEASANT_ZHONKA),
                             age=60,
                             cause_of_death=CONSUMPTION,
                             comment="по возрасту род. ок. 1851 г. Отчество Прокопиева среди Кекевых больше "
                                     "нигде не встречается; чья жена — в записи не сказано"),
                       ),
          *death_month(Month.MAY,
                       death(14, Gender.FEMALE, 13, 15,
                             deceased=person("Мария"), age="10 мес",
                             relatives=[relative(person("Косма", "Романов", last_name_orig="Кекев"), Relationship.FATHER)],
                             cause_of_death=SCARLATINA,
                             comment="отец — тот Косма Романов, у которого в мае 1912 г. родился сын Феодор "
                                     "(л. 45об), умерший годовалым в январе 1913 г.: двое детей подряд. Жена "
                                     "здесь не названа; в 1912 г. она «Параскева Антипина»"),
                       ),
          ),
    # Вторая волна (09.11.2026): дети замужних дочерей Кекевых, найденные по имени мужа. reviewed=False.
    *page("31об", reviewed=False,
          *death_month(Month.JULY,
                       # Василий — сын Максима Михайловича Мирошкина и Наталии Симеоновны Кикевой, род. 17.03.1911 (двойня;
                       # ч. 1, № м21)
                       death(None, Gender.MALE, 29, 31,
                             deceased=person("Василій"), age="4 мес 15 дн", comment="в подлиннике «4½ мѣсяца»; номер записи не виден",
                             relatives=[relative(person("Максимъ", "Михайловъ", last_name_orig="Мирошкинъ"), Relationship.FATHER)]),
                       ),
          ),
    defaults=DEFAULTS,
)
