from verso.ru.dsl import (CONFESSION_LIST, CensusRole, RecordDefaults, census_records, household,
                          member, page, person)
from verso.ru.dsl.marital_status import WIDOW
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON,
                                   PEASANT_SPOUSE)

# Исповедная роспись 1785 г., с. Дмитриевы Горы, церковь Покрова Пресвятыя Богородицы.
# **ГАВО ф. 556 оп. 109 д. 6, лл. 165–177об** (заказ № 5003, получен 28.10.2026; Photos
# «Дмитриевы Горы 1785 ИР (ГАВО 556-109-6)», pk 3756). Раздел прихода целый — от заголовка на
# л. 165 до итога на л. 177об. Владельца села в шапке я не читал, поэтому статус не задан.
#
# Взят двор 51 (л. 170) — дом, где после смерти Харитона Петрова живут его вдова и сыновья
# (`../families/Кикеевы.md`, линия Анны).
# 🏆🏆 **ХАРИТОНЪ УМЕРЪ МЕЖДУ ИЮНЕМ 1782 И 1785 ГОДОМ.** В сказке 1782 г. он ещё глава ветви
# в дворе Петра Андреева; здесь вместо него «сноха вдова Марѳа Гаврилова, 41» — жена Харитона по
# сказке 1782 г. — и «дѣти ея: Федоръ, Василей, Евдокея». Пропавшего в 30 книгах Харитона
# (умер «до 1803 г.») роспись отодвигает на двадцать лет назад.
# Главой двора записана «вдова Матрена Савинова, 66» с сыном **Григорей Симіоновъ** —
# в сказке 1782 г. это Матрёна Савельева, жена Симиона Петрова, брата Харитона, и их сын
# Григорей 13. Ни Петра Андреева, ни Симиона в росписи нет ⇒ оба тоже умерли к 1785 г.
# Марѳа названа «у нея сноха», хотя для Матрены она невестка (жена деверя); слово оставлено
# как в подлиннике.
#
# ⚠ Цифры в графах стоят на строку НИЖЕ имени (видно по мужской графе: «20» стоит против
# Евдокеи). Разложены по этому правилу, оно сходится с соседними дворами.
# ⚠ «Евдокея 14» не сходится со сказкой 1782 г. (там Евдокея 3, Дарья 10): возможно, это
# Дарья под другим именем или ошибка росписи — не сведено.
# Нумерация граф в ИР — по полу отдельно (мужчины 263–266, женщины 264–270), поэтому номера
# членов двора здесь — сквозной счёт, а не номера граф (`rules/extraction-confessions.md`).
#
# Вычитано в Verso 29.10.2026 (прочитано 28.10.2026 по кадру 330 при ~1.6×).

census = census_records(
    "ГАВО", "556", "109", "6", "Дмитриевы Горы", 1785,
    *page("170",
          household("51",
                    member(1, person("Матрена", "Савинова", status=PEASANT_FEMALE), CensusRole.HEAD, age=66,
                           marital_status=WIDOW),
                    member(2, person("Григорей", "Симіоновъ", status=PEASANT_MALE), CensusRole.SON, ref_member=1, age=20),
                    member(3, person("Прасковія", "Іванова", status=PEASANT_FEMALE), CensusRole.WIFE, ref_member=2, age=19),
                    member(4, person("Евдокея", status=PEASANT_DAUGHTER), CensusRole.DAUGHTER, ref_member=2, age="полгода"),
                    member(5, person("Марфа", "Гаврілова", status=PEASANT_FEMALE), CensusRole.DAUGHTER_IN_LAW, ref_member=1, age=41,
                           marital_status=WIDOW, comment="«у нея сноха вдова»; жена Харитона Петрова по сказке 1782 г."),
                    member(6, person("Федоръ", status=PEASANT_MALE), CensusRole.SON, ref_member=5, age=26),
                    member(7, person("Василей", status=PEASANT_MALE), CensusRole.SON, ref_member=5, age=20),
                    member(8, person("Евдокея", status=PEASANT_DAUGHTER), CensusRole.DAUGHTER, ref_member=5, age=14),
                    member(9, person("Феодора", "Антонова", status=PEASANT_SPOUSE), CensusRole.WIFE, ref_member=6, age=26),
                    member(10, person("Григорей", status=PEASANT_SON), CensusRole.SON, ref_member=6, age=6),
                    member(11, person("Ѯенія", "Никифорова", status=PEASANT_SPOUSE), CensusRole.WIFE, ref_member=7, age=18),
                    # В росписи его нет — умер между июнем 1782 и 1785 г.; восстановлен по «сноха вдова
                    # Марфа Гаврілова» и сказке 1782 г., где она — жена Харитона Петрова
                    member(12, person("Харитонъ", "Петровъ"), None, ref_member=5, spouse_member=5, hidden=True),
                    ),
          ),
    defaults=RecordDefaults(residence="Дмитриевы Горы"),
    **CONFESSION_LIST,
)
