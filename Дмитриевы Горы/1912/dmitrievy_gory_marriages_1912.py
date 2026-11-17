from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          page, person)
from verso.ru.dsl.statuses import (MESHCHANIN, PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE,
                                   PEASANT_SON)

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1912 г.,
# часть вторая «О бракосочетавшихся». ГАВО ф.590 оп.12 д.199, лл. 61об–68об.
#
# Прочитаны все 33 брака года на ОБЕ фамилии. Кекевы в пяти — два жениха, три
# невесты; Земсковых нет. Три из пяти венчаны в один день, 3 октября: на селе
# это единый осенний свадебный день, и поручители у всех октябрьских браков одни
# и те же четверо (Николай Максимов Мирошкин, мещанин Александр Иванов Евдокимов,
# Стефан Георгиев Домов, Даниил Петров Афонин) — дежурные свидетели, не родня.
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE)

dmitrievy_gory_marriages_1912 = marriage_records(
    "ГАВО", "590", "12", "199", "Дмитриевы Горы", "Покровская",
    1912,
    *page("61об", reviewed=False,
          *marriage_month(Month.JANUARY,
                          marriage(4, 27,
                                   groom=person("Василий", "Андреев", last_name_orig="Кекев", status=PEASANT_SON),
                                   groom_marriage_num=1, groom_age=18,
                                   bride=person("Анастасия", "Артемиева", last_name_orig="Шерстнева", status=PEASANT_DAUGHTER),
                                   bride_marriage_num=1, bride_age=19,
                                   witness1=person("Михаил", "Николаев", last_name_orig="Филатов", side=Side.GROOM),
                                   witness2=person("Евфимий", "Стефанов", last_name_orig="Мишков", side=Side.GROOM),
                                   witness3=person("Андрей", "Игнатиев", last_name_orig="Кекев", side=Side.BRIDE),
                                   witness4=person("Иоанн", "Андреев", last_name_orig="Кекев", side=Side.BRIDE),
                                   comment="поручители 1–2 по женихе, 3–4 по невесте. Иоанн Андреев по отчеству — "
                                           "брат жениха, и он же отец записи о рождении № м52 этого года "
                                           "(л. 53об); Андрей Игнатиев — отец записи 1915 г. (л. 176об)"),
                          ),
          *marriage_month(Month.APRIL,
                          marriage(6, 4,
                                   groom=person("Феодор", "Свиридов", last_name_orig="Савлинский", status=PEASANT_SON),
                                   groom_marriage_num=1, groom_age=19,
                                   bride=person("Екатерина", "Андреева", last_name_orig="Кекева", status=PEASANT_DAUGHTER),
                                   bride_marriage_num=1, bride_age=20,
                                   witness1=person("Косма", last_name_orig="Шуянов"),
                                   witness2=person("Николай", "Максимов", last_name_orig="Мирошкин"),
                                   witness3=person("Евфимий", "Иоаннов", last_name_orig="Кекев", status="запасный солдат"),
                                   witness4=person("Стефан", "Георгиев", last_name_orig="Козлов"),
                                   comment="невеста по отчеству — сестра Василия, Иоанна и Варвары Андреевых "
                                           "Кекевых. Фамилия жениха читается неуверенно («Савлинскій»/«Савлиневъ»); "
                                           "у первого поручителя отчество не записано"),
                          ),
          ),
    *page("65об", reviewed=False,
          *marriage_month(Month.OCTOBER,
                          marriage(20, 3,
                                   groom=person("Иаков", "Сильвестров", last_name_orig="Кекев", status=PEASANT_SON),
                                   groom_marriage_num=1, groom_age=20,
                                   bride=person("Мария", "Иоаннова", last_name_orig="Орехова", status=PEASANT_DAUGHTER),
                                   bride_marriage_num=1, bride_age="17 лет 6 мес",
                                   witness1=person("Николай", "Максимов", last_name_orig="Мирошкин"),
                                   witness2=person("Александр", "Иванов", last_name_orig="Евдокимов", status=MESHCHANIN),
                                   witness3=person("Стефан", "Георгиев", last_name_orig="Домов"),
                                   witness4=person("Даниил", "Петров", last_name_orig="Афонин"),
                                   comment="в источнике возраст невесты — «17½». ЭТО ВЕНЧАНИЕ ИМЕНУЕТ ЖЕНУ: далее "
                                           "она «Марія Іоаннова» и в 1914 г. (л. 134об), а «Наталія Іоаннова» "
                                           "записи 1913 г. (л. 87об) — описка писца. На поле поздняя приписка "
                                           "синим: «бракъ расторгнутъ, Пенза 1927 годъ»"),
                          marriage(24, 3,
                                   groom=person("Александр", "Димитриев", last_name_orig="Кекев", status="запасный солдат"),
                                   groom_marriage_num=1, groom_age="25 лет 6 мес",
                                   bride=person("Екатерина", "Андреева", last_name_orig="Романшина", status=PEASANT_DAUGHTER),
                                   bride_marriage_num=1, bride_age=19,
                                   witness1=person("Николай", "Максимов", last_name_orig="Мирошкин"),
                                   witness2=person("Александр", "Иванов", last_name_orig="Евдокимов", status=MESHCHANIN),
                                   witness3=person("Стефан", "Георгиев", last_name_orig="Домов"),
                                   witness4=person("Даниил", "Петров", last_name_orig="Афонин"),
                                   comment="в источнике возраст жениха — «25½»; в графе звания «крестьянскій сынъ» "
                                           "зачёркнуто и надписано «зап. солдатъ». Это венчание той пары, что "
                                           "крестит Алексия в 1914 г. (л. 128об, там фамилия писана «Кикевъ») и "
                                           "стоит в книге 1918 г. (л. 260об); девичья фамилия жены — Романшина"),
                          ),
          ),
    *page("68об", reviewed=False,
          *marriage_month(Month.OCTOBER,
                          marriage(33, 3,
                                   groom=person("Павел", "Михайлов", last_name_orig="Мирошкин", status=PEASANT_SON),
                                   groom_marriage_num=1, groom_age="18 лет 6 мес",
                                   bride=person("Мария", "Иоаннова", last_name_orig="Кекева", status=PEASANT_DAUGHTER),
                                   bride_marriage_num=1, bride_age=17,
                                   witness1=person("Николай", "Максимов", last_name_orig="Мирошкин"),
                                   witness2=person("Александр", "Иванов", last_name_orig="Евдокимов", status=MESHCHANIN),
                                   witness3=person("Стефан", "Георгиев", last_name_orig="Домов"),
                                   witness4=person("Даниил", "Петров", last_name_orig="Афонин"),
                                   comment="в источнике возраст жениха — «18½». После этого венчания невеста и "
                                           "становится той «кр. жёнкой Маріей Іоанновой Кекевой», что "
                                           "восприемница в 1913 г. (л. 87об) и дважды в 1915 г. (лл. 205об, "
                                           "212об) — фамилию она сохраняет девичью, как это принято в здешних "
                                           "записях"),
                          ),
          ),
    defaults=DEFAULTS,
)
