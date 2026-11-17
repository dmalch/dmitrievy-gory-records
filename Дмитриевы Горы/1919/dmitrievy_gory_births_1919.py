from verso.ru.dsl import (Gender, Month, RecordDefaults, birth, birth_month, birth_records, page,
                          person)
from verso.ru.dsl.statuses import (PEASANT_FEMALE, PEASANT_MAIDEN, PEASANT_MALE, PEASANT_SON,
                                   PEASANT_SPOUSE, PEASANT_ZHONKA)

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1919 г.,
# часть первая «О родившихся». ГАВО ф.590 оп.12 д.200.
#
# TARGETED extract: only the КИКЕВЪ / КЕКЕВЪ family. The 1919 birth section
# runs л. 1об–26об and holds 151 births (№ 77 муж. + № 74 жен.); all of it was
# read, and these three are every entry naming the family. Everyone else is
# deliberately absent — this is not a digitisation of the year.
#
# SPELLING. The same priest (І. Вертоградовъ) writes the surname two ways in
# one book, and the source itself proves they are one family: Павелъ Ѳеодоровъ
# is «Кикевъ» at the birth of his son Василій (л. 3об, № 8) and «Кекевъ» at
# that same son's death six months later (л. 48об, № 23 — see the deaths file).
# Each record therefore carries the form its own page uses; unifying them onto
# one canonical profile is a `preference` pin in generate_config_names.py, per
# ../CLAUDE.md — never a DSL name edit.
#
# ⚠ A THIRD form, «Кексевъ» (л. 5об), was withdrawn on re-reading — see the
# comment on that record. It was the only occurrence in 92 years of read books,
# and the same couple is «Ѳеодоръ ИГНАТІЕВЪ КЕКЕВЪ» in 1914. Withdrawing it is
# a correction of OUR reading, not a normalisation of the scribe's spelling.
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE, status_mother=PEASANT_FEMALE)

dmitrievy_gory_births_1919 = birth_records(
    "ГАВО", "590", "12", "200", "Дмитриевы Горы", "Покровская",
    1919,
    *page("3об", reviewed=False,
          *birth_month(Month.JANUARY,
                       birth(8, Gender.MALE, 21, 22,
                             child=person("Василий"),
                             father=person("Павел", "Феодоров", last_name_orig="Кикев"),
                             mother=person("Татиана", "Никитина"),
                             god_parent1=person("Иоанн", "Никитин", last_name_orig="Ганин", status=PEASANT_SON),
                             god_parent2=person("Александра", "Феодорова", last_name_orig="Анискина", status=PEASANT_SPOUSE),
                             comment="сын умер 6 июля 1919 в возрасте 6 мес — запись о смерти № 23, л. 48об, где отец записан «Кекевъ»"),
                       ),
          ),
    *page("5об", reviewed=False,
          *birth_month(Month.MARCH,
                       # ⚠ ОБА ИМЕНИ ОТЦА ИСПРАВЛЕНЫ ПО ЗАПИСИ 1914 г. Прежнее чтение — «Ѳеодоръ ИППОЛИТОВЪ
                       # КЕКСЕВЪ»; лист поднят и пересмотрен при 9–24×, и скан этого не решает: при ~900 px с
                       # листа спорная буква занимает около четырёх пикселей, входного штриха «е» (против «с»)
                       # там физически нет, а ширина слова (78 px) равно ложится и на шесть букв, и на семь —
                       # у этой руки разброс 11–17 px на букву в соседних словах той же строки. Решает второй
                       # признак: та же пара — «Ѳеодоръ + Параскева Никитина» — в МК 1914 г. (д. 199 л. 136об,
                       # № 39) записана «Ѳеодоръ ИГНАТІЕВЪ КЕКЕВЪ», а Параскева Никитина Филаткина — жена
                       # Феодора Игнатьевича по венчанию 02.10.1902 г. ✅ И ЭТО ПОТЯНУЛО ЗА СОБОЙ 1887 г.:
                       # вторая и единственная другая «Кексевъ» корпуса — брак № 27 (д.196 л. 373об) —
                       # разрешалась в эту форму ссылкой на ЭТУ запись. Опора снята, лист 373об перечитан, и
                       # жених оказался **Канышевымъ**: формы «Кексевъ» в корпусе больше нет вовсе, а
                       # «Полянковъ» перестал быть третьей уличной фамилией рода. ⚠ У восприемника «того же
                       # села» зачёркнуто и надписано «села Санчура»
                       birth(10, Gender.MALE, 28, 29,
                             child=person("Андрей"),
                             father=person("Феодор", "Игнатиев", last_name_orig="Кекев"),
                             mother=person("Параскева", "Никитина"),
                             god_parent1=person("Сергий", "Григорьев", last_name_orig="Ермаков", status=PEASANT_SON, residence="с. Санчур"),
                             god_parent2=person("Евдокия", "Маркелова", last_name_orig="Занетина", status=PEASANT_SPOUSE)),
                       ),
          ),
    *page("13об", reviewed=False,
          *birth_month(Month.AUGUST,
                       birth(34, Gender.MALE, 12, 13,
                             child=person("Алексий"),
                             father=person("Федор", "Иоаннов", last_name_orig="Кекев"),
                             mother=person("Феодосия", "Иванова"),
                             god_parent1=person("Димитрий", "Алексеев", last_name_orig="Кекев", status=PEASANT_SON),
                             god_parent2=person("Татиана", "Никитова", last_name_orig="Кекева", status=PEASANT_SPOUSE),
                             comment="оба восприемника — Кекевы. Татиана Никитова Кекева, вероятно, та же Татиана Никитина, жена Павла Феодорова (№ 8, л. 3об)"),
                       ),
          ),
    # Вторая волна (09.11.2026): дети замужних дочерей Кекевых, найденные по имени мужа (д. 200; восприемники — на
    # правой странице разворота).
    # reviewed=False: прочитано по сканам один раз, не вычитано.
    *page("2об", reviewed=False,
          *birth_month(Month.JANUARY,
                       # мать — Мария Кекева (брак 1916 № 1 с Иоанном Тимофеевичем Савиным: там «Ипполитова», здесь, как и в
                       # 1917 г., «Игнатіева»); восприемница — сестра отца Мария Тимофеевна Савина. Григорий умер 8.07.1919
                       # (ч. 3, № м25)
                       birth(5, Gender.MALE, 17, 18,
                             child=person("Григорій"),
                             father=person("Іоаннъ", "Тимоѳеевъ", last_name_orig="Савинъ"),
                             mother=person("Марія", "Игнатіева", status=PEASANT_SPOUSE),
                             god_parent1=person("Матвей", "Ѳеодоровъ", last_name_orig="Крайновъ", status=PEASANT_SON),
                             god_parent2=person("Марія", "Тимоѳеева", last_name_orig="Савина", status=PEASANT_MAIDEN)),
                       ),
          ),
    *page("20об", reviewed=False,
          *birth_month(Month.NOVEMBER,
                       # мать — Надежда Евфимиевна Кекева (брак 1914 № 13); отец и здесь «Михаилъ ЛАЗАРЕВЪ Орѣховъ», как в 1917 г.
                       # и на скане брака 1914 г. Восприемница — его сестра Наталия Лазаревна, уже в замужестве Крайнова
                       birth(64, Gender.MALE, 1, 1,
                             child=person("Василій"),
                             father=person("Михаилъ", "Лазаревъ", last_name_orig="Орѣховъ"),
                             mother=person("Надежда", "Евфиміева", status=PEASANT_SPOUSE),
                             god_parent1=person("Павелъ", "Ермиловъ", last_name_orig="Майоровъ", status=PEASANT_SON),
                             god_parent2=person("Наталія", "Лазарева", last_name_orig="Крайнова", status=PEASANT_ZHONKA)),
                       ),
          ),
    *page("24об", reviewed=False,
          *birth_month(Month.DECEMBER,
                       # мать — Матрона Романовна Кекева (брак 1899 № 18 с Иоанном Евфимиевичем Юкачевым); восприемники — брат
                       # отца Никифор Евфимиевич и дочь Наталия Иоанновна (род. 1904)
                       birth(71, Gender.MALE, 16, 17,
                             child=person("Василій"),
                             father=person("Іоаннъ", "Евфиміевъ", last_name_orig="Юкачевъ"),
                             mother=person("Матрона", "Романова", status=PEASANT_SPOUSE),
                             god_parent1=person("Никифоръ", "Евфиміевъ", last_name_orig="Юкачевъ", status=PEASANT_SON),
                             god_parent2=person("Наталія", "Іоаннова", last_name_orig="Юкачева", status=PEASANT_MAIDEN)),
                       ),
          ),
    *page("25об", reviewed=False,
          *birth_month(Month.DECEMBER,
                       # мать — Александра Иоанновна Кекева (брак 1905 № 8 с Петром Георгиевичем Шимаряновым)
                       birth(71, Gender.FEMALE, 23, 24,
                             child=person("Татіана"),
                             father=person("Петръ", "Георгіевъ", last_name_orig="Шимаряновъ"),
                             mother=person("Александра", "Іоаннова", status=PEASANT_SPOUSE),
                             god_parent1=person("Алексѣй", "Петровъ", last_name_orig="Шиковъ", status=PEASANT_SON),
                             god_parent2=person("Наталія", "Ѳеодорова", last_name_orig="Масликина", status=PEASANT_MAIDEN, comment="фамилия читается неуверенно")),
                       # мать — по всему Ирина Михайловна Кекева (брак 1911 № 15 с Феодором Иосифовичем, там «Абашовъ»). Здесь
                       # отец — «Ѳеодоръ Іосиф. Филатовъ», восприемники тоже Филатовы. Какая фамилия верна, не решено — сверить
                       # скан брака 1911 г.
                       birth(74, Gender.MALE, 28, 29,
                             child=person("Іоаннъ"),
                             father=person("Ѳеодоръ", "Іосифовъ", last_name_orig="Филатовъ"),
                             mother=person("Ирина", "Михайлова", status=PEASANT_SPOUSE),
                             god_parent1=person("Николай", "Іоанновъ", last_name_orig="Филатовъ", status=PEASANT_SON),
                             god_parent2=person("Анна", "Прокопіева", last_name_orig="Филатова", status=PEASANT_MAIDEN)),
                       ),
          ),
    defaults=DEFAULTS,
)
