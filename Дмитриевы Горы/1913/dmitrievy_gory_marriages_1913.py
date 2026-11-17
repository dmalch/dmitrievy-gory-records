from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          page, person)
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON,
                                   PEASANT_WIDOW)

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1913 г.,
# часть вторая «О бракосочетавшихся». ГАВО ф.590 оп.12 д.199, лл. 106об–110об.
#
# Прочитаны все 27 браков года на ОБЕ фамилии. Кекевы в трёх — невеста, жених и
# поручитель, — и здесь же **ПЕРВЫЙ ЗЕМСКИЙ, найденный в метрических книгах**.
#
# Ещё раз Кекев поручителем: Иаков Сильвестров Кекев по невесте в браке № 5
# (21 апреля, л. 107об) — записано в ../../regional-rules/dmitrievy-gory/README.md.
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE)

dmitrievy_gory_marriages_1913 = marriage_records(
    "ГАВО", "590", "12", "199", "Дмитриевы Горы", "Покровская",
    1913,
    *page("107об", reviewed=False,
          *marriage_month(Month.JUNE,
                          marriage(8, 3,
                                   groom=person("Павел", "Тимофеев", last_name_orig="Полтонин", status=PEASANT_SON),
                                   groom_marriage_num=1, groom_age="17 лет 6 мес",
                                   bride=person("Анастасия", "Феодорова", last_name_orig="Кекева", status=PEASANT_DAUGHTER),
                                   bride_marriage_num=1, bride_age=19,
                                   witness1=person("Максим", "Тимофеев", last_name_orig="Полтонин", side=Side.GROOM),
                                   witness2=person("Николай", "Евсигниев", last_name_orig="Полтонин", side=Side.GROOM),
                                   witness3=person("Иоанн", last_name_orig="Кекев", side=Side.BRIDE),
                                   witness4=person("Димитрий", "Максимов", last_name_orig="Кекев", side=Side.BRIDE),
                                   comment="в источнике возраст жениха — «17½». Оба поручителя по невесте — Кекевы; "
                                           "у первого отчество не записано. Фамилия жениха и первых двух поручителей "
                                           "читается неуверенно, принята по «Аннѣ Абрамовой Полтониной» записи о "
                                           "смерти № ж9 (л. 115об)"),
                          ),
          *marriage_month(Month.SEPTEMBER,
                          # ВТОРОЙ БРАК ОБОИХ. Это венчание той пары, что в 1914 г. крестит сына Иоанна (л.
                          # 138об) и в 1919 г. значится «Ѳедоръ Іоанновъ + Ѳеодосія Иванова» (д.200 л. 13об).
                          # За четыре месяца до свадьбы у жениха умер сын Василий, 2 лет (запись о смерти №
                          # м18, л. 117об) — от первого брака. Фамилия невесты — по первому мужу
                          marriage(10, 25,
                                   groom=person("Феодор", "Иоаннов", last_name_orig="Кекев"),
                                   groom_marriage_num=2, groom_age=41,
                                   bride=person("Феодосия", "Иоаннова", last_name_orig="Пуркова", status=PEASANT_WIDOW),
                                   bride_marriage_num=2, bride_age=27,
                                   witness1=person("Алексий", "Никифоров", last_name_orig="Романов"),
                                   witness2=person("Прокопий", "Тимофеев", last_name_orig="Гуленкин"),
                                   witness3=person("Стефан", "Георгиев", last_name_orig="Домов"),
                                   witness4=person("Иаков", "Петров", last_name_orig="Кочетков")),
                          ),
          ),
    *page("109об", reviewed=False,
          *marriage_month(Month.OCTOBER,
                          # ПЕРВЫЙ ЗЕМСКОВ, найденный в метрических книгах. Фамилия в МК стоит в
                          # прилагательной форме «Земскій» (перепись 1897 г. пишет «Земсковъ»); по отчеству
                          # жених — сын Игната Феодорова Земскова, главы двора 4 той переписи. Четыре
                          # поручителя в октябре 1913 г. одни и те же во всех браках месяца — это дежурные
                          # свидетели, не родня
                          marriage(15, 2,
                                   groom=person("Андрей", "Игнатиев", last_name_orig="Земский", status=PEASANT_SON),
                                   groom_marriage_num=1, groom_age=21,
                                   bride=person("Татиана", "Иоаннова", last_name_orig="Маслихина", status=PEASANT_DAUGHTER),
                                   bride_marriage_num=1, bride_age=20,
                                   witness1=person("Алексий", "Никифоров", last_name_orig="Романов"),
                                   witness2=person("Прокопий", "Тимофеев", last_name_orig="Гуленкин"),
                                   witness3=person("Стефан", "Георгиев", last_name_orig="Домов"),
                                   witness4=person("Иаков", "Петров", last_name_orig="Кочетков")),
                          ),
          ),
    defaults=DEFAULTS,
)
