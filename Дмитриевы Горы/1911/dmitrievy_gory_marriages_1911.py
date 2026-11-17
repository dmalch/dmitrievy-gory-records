from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON,
                                   PEASANT_WIDOW, RETIRED_SOLDIER)

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1911 г.,
# часть вторая «О бракосочетавшихся». ГАВО ф.590 оп.12 д.199, лл. 23об–27об
# (титул части — л. 23, титул части третьей — л. 28).
#
# Прочитаны все 22 брака года на ОБЕ фамилии. Кекевы в двух — жених и невеста;
# Земсковых нет. Четырнадцать из двадцати двух венчаны в один день, 2 октября.
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE)

dmitrievy_gory_marriages_1911 = marriage_records(
    "ГАВО", "590", "12", "199", "Дмитриевы Горы", "Покровская",
    1911,
    *page("24об", reviewed=False,
          *marriage_month(Month.APRIL,
                          # ВТОРОЙ брак жениха, ТРЕТИЙ невесты; ему 52, ей 47. Невеста — «Нижегородской
                          # губернии Ардатовского уезда прихода села Селикова(?) деревни Ситановки(?)
                          # крестьянская вдова» (оба топонима читаются неуверенно). И поручитель по невесте —
                          # отставной солдат Димитрий Максимов Кекев, тот самый, что в 1897 г. со всей семьёй
                          # жил сторожем частного леса в АРДАТОВСКОМ УЕЗДЕ Нижегородской губ. (двор 5
                          # переписи): первое документальное касание двух концов той связи. Второй поручитель
                          # по жениху — из Судогодского уезда, прихода села Ивинского; у третьего фамилия не
                          # записана. 7 ноября того же года умерла «Ардатовского уезда … крестьянская девица
                          # Пелагия Никифорова Козакова», 16 лет (запись о смерти № ж23, л. 33об) —
                          # однофамилица невесты
                          marriage(6, 17,
                                   groom=person("Василий", "Ермолаев", last_name_orig="Кекев", status="вдовый крестьянин"),
                                   groom_marriage_num=2, groom_age=52,
                                   bride=person("Елизавета", "Петрова", last_name_orig="Казакова", status=PEASANT_WIDOW),
                                   bride_marriage_num=3, bride_age=47,
                                   witness1=person("Стефан", "Павлов", last_name_orig="Кузин"),
                                   witness2=person("Стефан", "Егоров", last_name_orig="Фомин"),
                                   witness3=person("Феодор", "Михайлов"),
                                   witness4=person("Димитрий", "Максимов", last_name_orig="Кекев", status=RETIRED_SOLDIER)),
                          ),
          ),
    *page("26об", reviewed=False,
          *marriage_month(Month.OCTOBER,
                          # невеста по отчеству — сестра Иоанна Михайлова Кекева, отца записи о рождении 1912
                          # г. № м20 (л. 43об). За шесть недель до свадьбы, 21 августа, она была восприемницей
                          # у Феодора Игнатиева Кекева (запись о рождении № м54, л. 14об) — там ещё
                          # «крестьянская девица». Ни у одного из четырёх поручителей отчество не записано.
                          # Фамилия жениха на этой странице выведена «Абашовъ», хотя в прочих записях года род
                          # пишется «Абашинъ» — так же записан и четвёртый поручитель
                          marriage(15, 2,
                                   groom=person("Феодор", "Иосифов", last_name_orig="Абашов", status=PEASANT_SON),
                                   groom_marriage_num=1, groom_age=19,
                                   bride=person("Ирина", "Михайлова", last_name_orig="Кекева", status=PEASANT_DAUGHTER),
                                   bride_marriage_num=1, bride_age=19,
                                   witness1=person("Василий", last_name_orig="Шуянов"),
                                   witness2=person("Павел", last_name_orig="Захаров"),
                                   witness3=person("Косма", last_name_orig="Хохлов", status="запасный унтер-офицер"),
                                   witness4=person("Петр", last_name_orig="Абашин")),
                          ),
          ),
    defaults=DEFAULTS,
)
