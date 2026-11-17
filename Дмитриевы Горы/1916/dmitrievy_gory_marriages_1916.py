from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1916 г.,
# часть вторая «О бракосочетавшихся». ГАВО ф.590 оп.12 д.199, лл. 216об–218об.
#
# TARGETED extract: only the КЕКЕВЪ family. Все 10 браков 1916 г. прочитаны;
# в двух из них НЕВЕСТА — Кекева, жениха Кекева в этом году нет.
# Иоанн Михайлов Кекев стоит поручителем по женихе в браке № 2 (20 января) —
# это записано в ../../regional-rules/dmitrievy-gory/README.md, не здесь.
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE)

dmitrievy_gory_marriages_1916 = marriage_records(
    "ГАВО", "590", "12", "199", "Дмитриевы Горы", "Покровская",
    1916,
    *page("216об", reviewed=False,
          *marriage_month(Month.JANUARY,
                          # ⚠ отчество невесты в роду больше нигде не отзывается: Ипполита Кекева корпус не
                          # знает. Прежде её считали сестрой «Феодора Ипполитова Кексева» (МК 1919, д. 200 л.
                          # 5об), но то чтение отозвано — тот Феодор Игнатіевъ Кекевъ, см. запись 1919 г. Чья
                          # она дочь, открыто. Фамилия первого поручителя читалась неуверенно
                          # («Юдовъ»/«Юровъ») и разрешена по записи о рождении № м28 1913 г. (л. 85об), где
                          # тот же человек — «Косьма Григорьевъ ЮРОВЪ»
                          marriage(1, 8,
                                   groom=person("Иоанн", "Тимофеев", last_name_orig="Савин", status=PEASANT_SON),
                                   groom_marriage_num=1, groom_age=18,
                                   bride=person("Мария", "Ипполитова", last_name_orig="Кекева", status=PEASANT_DAUGHTER),
                                   bride_marriage_num=1, bride_age=19,
                                   witness1=person("Косма", "Григориев", last_name_orig="Юров"),
                                   witness2=person("Петр", "Павлов", last_name_orig="Мирошкин"),
                                   witness3=person("Максим", "Архипов", last_name_orig="Липатов"),
                                   witness4=person("Стефан", "Михайлов", last_name_orig="Абашин")),
                          ),
          ),
    *page("218об", reviewed=False,
          *marriage_month(Month.OCTOBER,
                          # ПОРУЧИТЕЛИ НЕ ЗАПИСАНЫ: л. 218об — последняя левая страница части второй, а
                          # обращённый к ней л. 219 занят печатным титулом «Часть третья, о умершихъ», так что
                          # графы поручителей для записей № 7–10 в книге нет. Невеста, судя по отчеству,
                          # сестра Евфимия и Андрея Иоанновых Кекевых (записи о рождении № 17 и № 25 за тот же
                          # год)
                          marriage(10, 23,
                                   groom=person("Николай", "Евфимов", last_name_orig="Кандрушин", status=PEASANT_SON),
                                   groom_marriage_num=1, groom_age=21,
                                   bride=person("Евфросиния", "Иоаннова", last_name_orig="Кекева", status=PEASANT_DAUGHTER),
                                   bride_marriage_num=1, bride_age=17),
                          ),
          ),
    defaults=DEFAULTS,
)
