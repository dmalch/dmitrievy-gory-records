from verso.ru.dsl import (Gender, Month, RecordDefaults, birth, birth_month, birth_records, page,
                          person)
from verso.ru.dsl.statuses import (PEASANT_FEMALE, PEASANT_MAIDEN, PEASANT_MALE, PEASANT_SON,
                                   PEASANT_SPOUSE, PEASANT_WIDOW, PEASANT_ZHONKA, SOLDIER,
                                   SOLDIER_WIFE)

# Метрическая книга Покровской церкви с. Димитриевы Горы за 1917 г.,
# часть первая «О родившихся». ГАВО ф.590 оп.12 д.199, лл. 230об–241об.
#
# TARGETED extract: only the КЕКЕВЪ family (= Кикевъ/Кексевъ; the 1919 book
# writes one man both ways). The whole 1917 birth section was read; these two
# are the entries where a Кекевъ is a parent.
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE, status_mother=PEASANT_FEMALE)

dmitrievy_gory_births_1917 = birth_records(
    "ГАВО", "590", "12", "199", "Дмитриевы Горы", "Покровская",
    1917,
    *page("237об", reviewed=False,
          *birth_month(Month.JULY,
                       birth(21, Gender.FEMALE, 29, 30,
                             child=person("Наталия"),
                             father=person("Алексий", "Николаев", last_name_orig="Кекев", status=SOLDIER),
                             mother=person("Любовь", "Емельянова"),
                             god_parent1=person("Павел", "Феодоров", last_name_orig="Кузин"),
                             god_parent2=person("Александра", "Феодорова", last_name_orig="Кекева", status=PEASANT_MAIDEN),
                             comment="дочь умерла 17 августа 1917 в возрасте 3 недель — запись о смерти № 24, л. 253об"),
                       ),
          ),
    *page("238об", reviewed=False,
          *birth_month(Month.AUGUST,
                       birth(18, Gender.MALE, 5, 6,
                             child=person("Иоанн"),
                             father=person("Иоанн", last_name_orig="Кекев", status=SOLDIER),
                             mother=person("Татиана", "Онисимова"),
                             god_parent1=person("Илия", "Иоаннов", last_name_orig="Моисеев", status=PEASANT_SON),
                             god_parent2=person("Наталия", "Петрова", last_name_orig="Щецина", status=PEASANT_MAIDEN),
                             comment="ЗАПИСЬ ИСПРАВЛЕНА ПИСЦОМ: «Ѳеодоръ»→«Іоаннъ», «Горячевъ»→«Кекевъ», "
                                     "«Васильева»→«Онисимова» — надстрочно; отчество отца «Андреевъ» густо "
                                     "зачёркнуто, замена НЕ вписана, поэтому здесь его нет"),
                       ),
          ),
    # Вторая волна (09.11.2026): дети замужних дочерей Кекевых, найденные по имени мужа.
    # reviewed=False: прочитано по сканам один раз, не вычитано. Л. 231 в нумерации пропущен: за 230об сразу 232.
    *page("230об", reviewed=False,
          *birth_month(Month.JANUARY,
                       # мать — Дарья Романовна Кекева (брак 1894 № 34 с Григорием Петровичем Рыбкиным)
                       birth(4, Gender.MALE, 19, 20,
                             child=person("Алексѣй"),
                             father=person("Григорій", "Петровъ", last_name_orig="Рыбкинъ", status=SOLDIER),
                             mother=person("Дарія", "Романова", status=PEASANT_SPOUSE),
                             god_parent1=person("Николай", "Михайловъ", last_name_orig="Журавлевъ", status=SOLDIER),
                             god_parent2=person("Елена", "Васильева", last_name_orig="Рыбкина", status=SOLDIER_WIFE)),
                       # мать — по всему Мария Кекева (брак 1916 № 1 с Иоанном Тимофеевичем Савиным, невеста там «Ипполитова»);
                       # здесь отчество матери ясно «Игнатіева» — расхождение не разрешено. Восприемница — Мария Михайловна
                       # Кузнецова (Кекева), восприемник — Феодор Максимович Ипаткин (в 1916 г. «Липатовъ»)
                       birth(2, Gender.FEMALE, 28, 29,
                             child=person("Евдокія"),
                             father=person("Іоаннъ", "Тимофеевъ", last_name_orig="Савинъ", status=SOLDIER),
                             mother=person("Марія", "Игнатіева", status=PEASANT_SPOUSE),
                             god_parent1=person("Ѳеодоръ", "Максимовъ", last_name_orig="Ипаткинъ", status=PEASANT_SON),
                             god_parent2=person("Марія", "Михайлова", last_name_orig="Кузнецова", status=PEASANT_ZHONKA)),
                       ),
          ),
    *page("239об", reviewed=False,
          *birth_month(Month.AUGUST,
                       # мать — Надежда Евфимиевна Кекева (брак 1914 № 13). Отец здесь «Михаилъ Лазаревъ Орѣховъ», восприемница —
                       # его сестра Наталия Лазаревна; в записи о браке 1914 г. (л. 146об) на скане тоже «Лазаревъ», в DSL того
                       # года — «Феодоров»: чтение первой волны, ждёт вычитки владельцем
                       birth(24, Gender.FEMALE, 24, 25,
                             child=person("Анна"),
                             father=person("Михаилъ", "Лазаревъ", last_name_orig="Орѣховъ"),
                             mother=person("Надежда", "Евфиміева", status=PEASANT_SPOUSE),
                             god_parent1=person("Павелъ", "Ермиловъ", last_name_orig="Майоровъ", status=PEASANT_SON),
                             god_parent2=person("Наталія", "Лазарева", last_name_orig="Орѣхова", status=PEASANT_MAIDEN)),
                       ),
          ),
    # Л. 273об: обрывок печатного бланка 1917 г. (октябрь — ноябрь, № ж29–32; подпись свящ. Фортунатова),
    # наклеенный поверх рукописной описи 1918 г. Счёт продолжает л. 240об (сентябрь, № ж28). Восприемники к нему не
    # сохранились: на л. 274 — графа восприемников рукописной описи 1918 г.
    *page("273об", reviewed=False,
          *birth_month(Month.OCTOBER,
                       # мать — Мария Михайловна Кекева (брак 1914 № 12), вдова Павла Ипполитовича Кузнецова (†4.03.1917):
                       # «вдова Марія Михайлова Кузнецова отъ умершаго мужа Павла Ипполитова»
                       birth(30, Gender.FEMALE, 15, 16,
                             child=person("Марія"),
                             father=person("Павелъ", "Ипполитовъ", last_name_orig="Кузнецовъ", comment="умерший муж матери"),
                             mother=person("Марія", "Михайлова", last_name_orig="Кузнецова", status=PEASANT_WIDOW),
                             comment="восприемники на листе не сохранились"),
                       ),
          ),
    defaults=DEFAULTS,
)
