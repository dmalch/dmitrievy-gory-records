from verso.ru.dsl import (Gender, Month, RecordDefaults, birth, birth_month, birth_records, page,
                          person)
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MAIDEN, PEASANT_MALE,
                                   PEASANT_SON, PEASANT_SPOUSE)

# «Метрическая опись о родившихся … за 1918 годъ», Покровская церковь
# с. Димитриевы Горы. ГАВО ф.590 оп.12 д.199, лл. 259об–274об.
#
# TARGETED extract: only the КЕКЕВЪ family (= Кикевъ/Кексевъ, see the 1919
# files — the same man is written both ways there). Every birth page of 1918
# was read; these three are the entries where a Кекевъ is a PARENT.
#
# ⚠ This is NOT the printed consistory form but a hand-ruled register, and the
# leaves are torn — dark areas on the scans are missing paper. Some entries are
# certainly lost, so absence here is weaker evidence than in the 1919 book.
#
# The family is much more visible as восприемники than as parents in 1918.
# Recorded in ../CLAUDE.md rather than invented into records: Илья Егоровъ,
# Ѳедоръ Димитріевъ, Марія Иванова, Евфросинія Сергіева, Евдокія Сергіева,
# Димитрій Алексѣевъ and Григорій Андреевъ Кекевы all stand as godparents to
# other families' children.
#
# reviewed=False: read once from the scans, not yet checked back against them.

DEFAULTS = RecordDefaults(residence="Дмитриевы Горы", status_male=PEASANT_MALE,
                          status_female=PEASANT_FEMALE, status_mother=PEASANT_FEMALE)

dmitrievy_gory_births_1918 = birth_records(
    "ГАВО", "590", "12", "199", "Дмитриевы Горы", "Покровская",
    1918,
    *page("260об", reviewed=False,
          *birth_month(Month.APRIL,
                       birth(15, Gender.FEMALE, 20, 21,
                             child=person("Анна"),
                             father=person("Александр", "Димитриев", last_name_orig="Кекев"),
                             mother=person("Екатерина"),
                             god_parent1=person("Петр", "Димитриев", last_name_orig="Кекев", status=PEASANT_SON),
                             god_parent2=person("Елена", "Димитриева", last_name_orig="Кекева", status=PEASANT_DAUGHTER),
                             comment="отчество матери утрачено — разрыв листа. Оба восприемника Кекевы и, судя по отчеству, брат и сестра отца"),
                       ),
          ),
    *page("261об", reviewed=False,
          *birth_month(Month.JUNE,
                       birth(19, Gender.MALE, 2, 3,
                             child=person("Димитрий"),
                             father=person("Косма", "Романов", last_name_orig="Кекев"),
                             mother=person("Параскева", "Антониева"),
                             god_parent1=person("Иаков", "Григорьев", last_name_orig="Рыбкин", status=PEASANT_SON),
                             god_parent2=person("Кристина", "Романова", last_name_orig="Федюнина", status=PEASANT_SPOUSE),
                             comment="восприемница Кристина Романова — по отчеству сестра отца"),
                       ),
          ),
    *page("262об", reviewed=False,
          *birth_month(Month.JULY,
                       birth(23, Gender.MALE, 1, 2,
                             child=person("Иоанн"),
                             father=person("Евфимий", "Иванов", last_name_orig="Кекев"),
                             mother=person("Мария", "Васильева"),
                             god_parent1=person("Феодор", "Максимов", last_name_orig="Игнатов", status=PEASANT_SON),
                             god_parent2=person("Анна", "Васильева", last_name_orig="Гуленкина", status=PEASANT_SPOUSE),
                             comment="этот младенец умер 10 апреля 1919 в возрасте 10 мес — запись о смерти № 14, л. 45об д.200. Евфимий и Федор Ивановы Кекевы — братья"),
                       ),
          ),
    # Вторая волна (09.11.2026): дети замужних дочерей Кекевых, найденные по имени мужа.
    # reviewed=False: прочитано по сканам один раз, не вычитано.
    *page("260об", reviewed=False,
          *birth_month(Month.MARCH,
                       # мать — Матрона Романовна Кекева (брак 1899 № 18 с Иоанном Евфимиевичем Юкачевым); восприемники — дети
                       # её сестры Дарьи Романовны Рыбкиной (Гавриил род. 1899)
                       birth(12, Gender.MALE, 24, 25,
                             child=person("Гавріилъ"),
                             father=person("Иванъ", "Евфиміевъ", last_name_orig="Юкачевъ"),
                             mother=person("Матрона", "Романова", status=PEASANT_SPOUSE),
                             god_parent1=person("Гавріилъ", "Григорьевъ", last_name_orig="Рыбкинъ", status=PEASANT_SON),
                             god_parent2=person("Евдокія", "Григорьева", last_name_orig="Рыбкина", status=PEASANT_MAIDEN)),
                       ),
          ),
    *page("261об", reviewed=False,
          *birth_month(Month.APRIL,
                       # мать — Мария Иоанновна Кекева (брак 1912 № 33 с Павлом Михайловичем Мирошкиным); восприемница — её
                       # сестра Анна Ивановна Кекева
                       birth(15, Gender.MALE, 24, 25,
                             child=person("Николай"),
                             father=person("Павелъ", "Михайловъ", last_name_orig="Мирошкинъ"),
                             mother=person("Марія", "Иванова", status=PEASANT_SPOUSE),
                             god_parent1=person("Василій", "Ивановъ", last_name_orig="Мирошкинъ", status=PEASANT_SON),
                             god_parent2=person("Анна", "Иванова", last_name_orig="Кекева", status=PEASANT_MAIDEN)),
                       ),
          ),
    *page("266об", reviewed=False,
          *birth_month(Month.SEPTEMBER,
                       # мать — Евдокия Георгиевна Кекева (брак 1915 № 1 с Иоанном Максимовичем Липатовым = Ипаткиным; здесь
                       # «Ипатовъ», мать «Егорова»)
                       birth(38, Gender.FEMALE, 13, 14,
                             child=person("Анна"),
                             father=person("Иванъ", "Максимовъ", last_name_orig="Ипатовъ"),
                             mother=person("Евдокія", "Егорова", status=PEASANT_SPOUSE),
                             god_parent1=person("Василій", "Никифоровъ", last_name_orig="Мухинъ", comment="фамилия читается неуверенно"),
                             god_parent2=person("Евдокія", "Сергіева", last_name_orig="Кекева", status=PEASANT_SPOUSE)),
                       ),
          ),
    defaults=DEFAULTS,
)
