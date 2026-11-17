from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          page, person)
from verso.ru.dsl.statuses import PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1914 г.,
# часть вторая «О бракосочетавшихся». ГАВО ф.590 оп.12 д.199, лл. 143об–147об.
#
# Прочитаны все 19 браков 1914 г. на ОБЕ фамилии — Кикев/Кекев и Земсков.
# В двух браках НЕВЕСТА — Кекева; жениха Кекева в году нет; Земсковых нет вовсе.
# Кекевы-поручители, не имеющие своей записи, перечислены в
# ../../regional-rules/dmitrievy-gory/README.md.
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE)

dmitrievy_gory_marriages_1914 = marriage_records(
    "ГАВО", "590", "12", "199", "Дмитриевы Горы", "Покровская",
    1914,
    *page("146об", reviewed=False,
          *marriage_month(Month.NOVEMBER,
                          marriage(12, 1,
                                   groom=person("Павел", "Ипполитов", last_name_orig="Кузнецов", status=PEASANT_SON),
                                   groom_marriage_num=1, groom_age=20,
                                   bride=person("Мария", "Михайлова", last_name_orig="Кекева", status=PEASANT_DAUGHTER),
                                   bride_marriage_num=1, bride_age=18,
                                   witness1=person("Димитрий", "Спиридонов", last_name_orig="Махнев", side=Side.GROOM),
                                   witness2=person("Иоанн", "Михайлов", last_name_orig="Кекев", side=Side.GROOM),
                                   witness3=person("Николай", "Максимов", last_name_orig="Мирошкин", side=Side.BRIDE),
                                   witness4=person("Стефан", "Иоаннов", last_name_orig="Никитаев", side=Side.BRIDE),
                                   comment="поручители 1 и 2 — по женихе, 3 и 4 — по невесте. Иоанн Михайлов Кекев "
                                           "по отчеству — брат невесты; он же поручитель в браках № 8, 9, 10 и 13 "
                                           "этого года и в браке № 2 1916 г."),
                          marriage(13, 5,
                                   groom=person("Михаил", "Феодоров", last_name_orig="Орехов", status=PEASANT_SON),
                                   groom_marriage_num=1, groom_age="17 лет 6 мес",
                                   bride=person("Надежда", "Евфимиева", last_name_orig="Кекева", status=PEASANT_DAUGHTER),
                                   bride_marriage_num=1, bride_age=19,
                                   witness1=person("Димитрий", "Спиридонов", last_name_orig="Махнев"),
                                   witness2=person("Иоанн", "Михайлов", last_name_orig="Кекев"),
                                   witness3=person("Михаил", "Васильев", last_name_orig="Кондрушин"),
                                   witness4=person("Стефан", "Иоаннов", last_name_orig="Никитаев"),
                                   comment="в источнике возраст жениха — «17½». Невеста семью неделями раньше была "
                                           "восприемницей при рождении № м53 (л. 137об), где её имя написано "
                                           "неразборчиво и читается по этой записи"),
                          ),
          ),
    defaults=DEFAULTS,
)
