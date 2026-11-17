from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          page, person)
from verso.ru.dsl.statuses import PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1915 г.,
# часть вторая «О бракосочетавшихся». ГАВО ф.590 оп.12 д.199, лл. 182об–183об.
#
# TARGETED extract: only the КЕКЕВЪ family. Военный год — всего 5 браков за 1915,
# все прочитаны; Кекевы участвуют только в первом.
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE)

dmitrievy_gory_marriages_1915 = marriage_records(
    "ГАВО", "590", "12", "199", "Дмитриевы Горы", "Покровская",
    1915,
    *page("182об", reviewed=False,
          *marriage_month(Month.JANUARY,
                          marriage(1, 9,
                                   groom=person("Иван", "Максимов", last_name_orig="Липатов", status=PEASANT_SON),
                                   groom_marriage_num=1, groom_age="17 лет 6 мес",
                                   bride=person("Евдокия", "Георгиева", last_name_orig="Кекева", status=PEASANT_DAUGHTER),
                                   bride_marriage_num=1, bride_age=18,
                                   witness1=person("Стефан", "Георгиев", last_name_orig="Домов", side=Side.GROOM),
                                   witness2=person("Стефан", "Михайлов", last_name_orig="Абашин", side=Side.GROOM),
                                   witness3=person("Димитрий", "Максимов", last_name_orig="Кекев", side=Side.BRIDE),
                                   witness4=person("Михаил", "Феодоров", last_name_orig="Костин", side=Side.BRIDE),
                                   comment="в источнике возраст жениха — «17½». Поручители 1 и 2 — по женихе, "
                                           "3 и 4 — по невесте, так что Димитрий Максимов Кекев поручается за "
                                           "невесту. Невеста тремя днями раньше, ещё девицей, была восприемницей "
                                           "при рождении № м2 (л. 158об)"),
                          ),
          ),
    defaults=DEFAULTS,
)
