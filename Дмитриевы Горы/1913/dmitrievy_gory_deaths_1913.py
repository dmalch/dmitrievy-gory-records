from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import CHILDBIRTH, CONSUMPTION, SCARLATINA
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, PEASANT_ZHONKA

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1913 г.,
# часть третья «Объ умершихъ». ГАВО ф.590 оп.12 д.199, лл. 113об–123об.
#
# Прочитано на ОБЕ фамилии. Скарлатинный и дифтеритный год — детских записей
# больше половины. Кекевых шесть, Земсковых нет.
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE)

dmitrievy_gory_deaths_1913 = death_records(
    "ГАВО", "590", "12", "199", "Дмитриевы Горы", "Покровская",
    1913,
    *page("114об", reviewed=False,
          *death_month(Month.JANUARY,
                       # ✅ **17.09.2026 НОМЕР, ДАТЫ И ВОЗРАСТ СВЕРЕНЫ ПО СКАНУ.** Счёт «м9», смерть 26,
                       # погребение 28 — сходится с DSL; возраст писан «**1 г**» при 7×. Родился 14 мая 1912
                       # г. (ч. 1 № м26) ⇒ прожил 8 месяцев 12 дней, и «1 г» — **округление причта вверх**, а
                       # не другой ребёнок: тождество уже утверждено комментарием при метрике 1912 года.
                       # `death-age-check` держал это HIGH «расхождение 3.6 мес»
                       death(9, Gender.MALE, 26, 28,
                             deceased=person("Феодор"), age=1,
                             relatives=[relative(person("Косма", "Романов", last_name_orig="Кекев"), Relationship.FATHER)],
                             cause_of_death=SCARLATINA,
                             source_age_error="в книге «1 г» (сверено при 7×), прожито 8 мес 12 дн от "
                                              "рождения 14.05.1912 ч.1 № м26 — округление причта вверх; "
                                              "тождество ребёнка не под вопросом",
                             comment="в декабре того же года у этой пары родилась дочь Мария (запись о рождении "
                                     "№ ж67, л. 104об)"),
                       ),
          ),
    *page("117об", reviewed=False,
          *death_month(Month.MAY,
                       death(18, Gender.MALE, 14, 16,
                             deceased=person("Василий"), age=2,
                             relatives=[relative(person("Феодор", "Иоаннов", last_name_orig="Кекев"), Relationship.FATHER)],
                             cause_of_death=SCARLATINA,
                             comment="сын от первого брака: 25 сентября того же года отец женится вторым браком "
                                     "на вдове Феодосии Иоанновой (запись о браке № 10, л. 108об)"),
                       ),
          ),
    *page("118об", reviewed=False,
          *death_month(Month.JULY,
                       death(24, Gender.MALE, 1, 3,
                             deceased=person("Александр"), age=6,
                             relatives=[relative(person("Григорий", "Андреев", last_name_orig="Кекев"), Relationship.FATHER)],
                             cause_of_death=SCARLATINA,
                             comment="в графе «Лѣта» стоит «6» без единицы; в мужской колонке это годы. "
                                     "Второй ребёнок этой семьи умер через два месяца — Екатерина, № ж36, л. 121об"),
                       ),
          ),
    *page("120об", reviewed=False,
          *death_month(Month.AUGUST,
                       death(40, Gender.MALE, 29, 31,
                             deceased=person("Роман", "Андреев", last_name_orig="Кекев"), age=61,
                             cause_of_death=CONSUMPTION,
                             comment="ГЛАВА СТАРШЕГО ПОКОЛЕНИЯ, единственный взрослый Кекев-мужчина, чью смерть "
                                     "мы застали. По отчествам детей — отец Космы Романова, Матроны Романовой "
                                     "(жены Иоанна Евфимиева Кекева) и Кристины Романовой (в замужестве "
                                     "Федюниной, 1918); по своему отчеству — брат Григория Андреева Кекева"),
                       ),
          ),
    *page("121об", reviewed=False,
          *death_month(Month.AUGUST,
                       death(36, Gender.FEMALE, 29, 31,
                             deceased=person("Екатерина"), age=2,
                             relatives=[relative(person("Григорий", "Андреев", last_name_orig="Кекев"), Relationship.FATHER)],
                             cause_of_death="дифтерит",
                             comment="вторая потеря этой семьи за лето — ср. № м24, л. 118об"),
                       ),
          *death_month(Month.SEPTEMBER,
                       death(37, Gender.FEMALE, 7, 9,
                             deceased=person("Анисия", "Феодорова", last_name_orig="Кекева", status=PEASANT_ZHONKA),
                             age=41,
                             cause_of_death=CHILDBIRTH,
                             comment="умерла родами; ребёнок в метрической книге не назван — ни записи о "
                                     "рождении, ни второй записи о смерти в этом году нет. Мужа запись не "
                                     "называет"),
                       ),
          ),
    # Вторая волна (09.11.2026): дети замужних дочерей Кекевых, найденные по имени мужа. reviewed=False.
    *page("118об", reviewed=False,
          *death_month(Month.JULY,
                       # Мария — дочь Алексия Николаевича Прошина и Наталии Евфимиевны Кекевой, род. 2.07.1913 (ч. 1, № ж33).
                       # ⚠ 13 марта того же года погребён «Алексія Васильева Прошина сынъ Михаилъ» — другой Прошин
                       death(None, Gender.FEMALE, 8, 10,
                             deceased=person("Марія"), age="1 нед", comment="номер записи не виден",
                             relatives=[relative(person("Алексій", "Николаевъ", last_name_orig="Прошинъ"), Relationship.FATHER)]),
                       ),
          ),
    defaults=DEFAULTS,
)
