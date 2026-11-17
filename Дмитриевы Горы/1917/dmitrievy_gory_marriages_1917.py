from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1917 г.,
# часть вторая «О бракосочетавшихся». ГАВО ф.590 оп.12 д.199, лл. 242об–247об.
#
# TARGETED extract: only the КЕКЕВЪ family. All 21 marriages of 1917 were read;
# in two of them the BRIDE is a Кекева. No Кекевъ is a groom. (Several stand as
# поручители — Павелъ Кекевъ at №№ 10, 12, 13 and Михаилъ Кекевъ at № 15 — those
# are recorded in ../../regional-rules/dmitrievy-gory/README.md, not here.)
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE)

dmitrievy_gory_marriages_1917 = marriage_records(
    "ГАВО", "590", "12", "199", "Дмитриевы Горы", "Покровская",
    1917,
    *page("243об", reviewed=False,
          *marriage_month(Month.MAY,
                          marriage(5, 26,
                                   groom=person("Павел", "Феодоров", last_name_orig="Кузин", status=PEASANT_SON), groom_marriage_num=1, groom_age="17 лет 6 мес",
                                   bride=person("Мария", "Николаева", last_name_orig="Кекева", status=PEASANT_DAUGHTER), bride_marriage_num=1,
                                   witness1=person("Максим", "Иосифов", last_name_orig="Филатов"),
                                   witness2=person("Иоанн", "Стефанов", last_name_orig="Есикин"),
                                   witness3=person("Игнатий", "Павлов", last_name_orig="Козлов"),
                                   witness4=person("Антоний", "Иоаннов", last_name_orig="Легков"),
                                   comment="в источнике возраст жениха — «17½»; возраст невесты в графе «Лѣта невѣсты» не заполнен. Жених Павел Феодоров Кузин — восприемник при рождении № 21 (л. 237об)"),
                          ),
          ),
    *page("245об", reviewed=False,
          *marriage_month(Month.OCTOBER,
                          marriage(14, 15,
                                   groom=person("Иоанн", "Стефанов", last_name_orig="Есикин", status=PEASANT_SON), groom_marriage_num=1, groom_age="17 лет 9 мес",
                                   bride=person("Александра", "Алексеева", last_name_orig="Кекева", status=PEASANT_DAUGHTER), bride_marriage_num=1, bride_age=19,
                                   witness1=person("Стефан", "Георгиев", last_name_orig="Домов"),
                                   witness2=person("Василий", "Тарасов", last_name_orig="Есикин"),
                                   witness3=person("Михаил", "Николаев", last_name_orig="Борисов"),
                                   witness4=person("Феодор", "Андреев", last_name_orig="Царев"),
                                   comment="в источнике возраст жениха — «17¾». Месяц перенесён с л. 244об («Октябрь»); на л. 245об заголовка месяца нет — проверить при вычитке"),
                          ),
          ),
    defaults=DEFAULTS,
)
