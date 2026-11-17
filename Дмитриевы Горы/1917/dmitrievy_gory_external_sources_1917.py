from verso.ru.dsl import (EventDate, Month, WwiDocumentType, external_source_records, person,
                          wwi_record)
from verso.ru.dsl.marital_status import SINGLE

# ПМВ — gwar.mil.ru («Памяти героев Великой войны»), событие 1917 г..
# Внесены только люди, найденные в корпусе (реестр всех карточек села —
# EXTERNAL_SOURCES.md и external_sources/pmv_gwar.tsv). Сканы сверены с указателем;
# расхождения — в comment.
dmitrievy_gory_external_sources_1917 = external_source_records(
    "Дмитриевы Горы",
    wwi_record(
        person("Павелъ", "Михайловъ", "Мирошкинъ", residence="Дмитриевы Горы"),
        source_url="https://gwar.mil.ru/heroes/chelovek_gospital22351473/",
        rank="мл. унтер-офицер",
        military_unit="88-й пехотный Петровский полк",
        casualty_reason="сквозная рана бедра",
        date=EventDate(1917, Month.MARCH, 16),
        document_type=WwiDocumentType.ARRIVAL_CARD_LOWER,
        casualty_date=EventDate(1917, Month.FEBRUARY, 20),
        archive="РГВИА",
        fund="Картотека бюро учёта потерь в Первой мировой войне (офицеров и солдат)",
        archive_location="Шкаф без номера, ящик 2358-М",
        scan_file="scans/gwar_gospital22351473.jpg",
        comment=(
            "Карточка на прибывших № 11586: «вол. Дмитріевской, с. Дмитріевгорское»; ранен 20 февраля 1917 г.; "
            "Хирургический госпиталь № 87 ВЗС, Одесса, поступил 16/III 1917. "
            "Корпус: Павел Михайлов Мирошкин — жених 1912, брак № 33."
        ),
    ),
    wwi_record(
        person("Александръ", "Дмитріевъ", "Кикеевъ", residence="Дмитриевы Горы"),
        source_url="https://gwar.mil.ru/heroes/chelovek_gospital1373652/",
        rank="рядовой",
        military_unit="46-я пехотная дивизия",
        casualty_reason="плевритъ",
        date=EventDate(1917, Month.JUNE, 22),
        document_type=WwiDocumentType.ARRIVAL_CARD_HIGHER,
        archive="РГВИА",
        fund="Картотека бюро учёта потерь в Первой мировой войне (офицеров и солдат)",
        archive_location="Шкаф без номера, ящик 437-Б",
        scan_file="scans/gwar_gospital1373652.jpg",
        comment=(
            "Карточка на прибывших № 73053, штамп «№ 78 С.Э.Г. Курскъ» (сводный эвакуационный госпиталь № 78, г. Курск); "
            "болен плевритом, поступил 29/VI 1917 (в указателе — 22.06.1917). В указателе место рождения искажено "
            "(«Беляковский уезд, Дмитриевская вол.»); на карточке уезд читается как Меленковский, волость залита чернилами, "
            "графа селения пуста. Та же болезнь, что на карточке chelovek_gospital22952713."
        ),
    ),
    wwi_record(
        person("Александръ", "Дмитріевъ", "Кикеевъ", residence="Дмитриевы Горы"),
        source_url="https://gwar.mil.ru/heroes/chelovek_gospital22952713/",
        rank="рядовой",
        military_unit="46-я пехотная дивизия",
        casualty_reason="плевритъ",
        date=EventDate(1917, Month.JUNE, 27),
        document_type=WwiDocumentType.REPORTING_CARD,
        archive="РГВИА",
        fund="Картотека бюро учёта потерь в Первой мировой войне (офицеров и солдат)",
        archive_location="Шкаф без номера, ящик 1768-К",
        scan_file="scans/gwar_gospital22952713.jpg",
        comment=(
            "Отчетно-осведомительная карточка Всероссийского земского союза от госпиталя № 2 Дамского комитета, г. Воронеж: "
            "уроженец «вол. и с. Дмитріевы Горы» Меленковского у.; плеврит; поступил 27 июня 1917 г., 8 июля 1917 г. "
            "эвакуирован — «отпускъ [неразб.]». В указателе причина выбытия — «болен». "
            "Корпус: Александр Димитриев Кекев — перепись 1897 (1887 г. р.), жених 1912 № 24, отец в 1914 и 1918."
        ),
    ),
    wwi_record(
        person("Петръ", "Николаевъ", "Захаровъ", residence="Дмитриевы Горы"),
        source_url="https://gwar.mil.ru/heroes/chelovek_donesenie13484876/",
        rank="рядовой",
        military_unit="205-й пехотный Шемахинский полк",
        marital_status=SINGLE,
        casualty_reason="ранен/контужен",
        date=EventDate(1917, Month.JULY, 17),
        document_type=WwiDocumentType.CASUALTY_LISTS,
        archive="РГВИА",
        fund="Ф. 16196 — Особое делопроизводство по сбору и регистрации сведений о выбывших за смертью или за ранами, а также пропавших без вести воинских чинах (1914–1918)",
        inventory="Оп. 1, Именные списки потерь солдат и офицеров 1914–1918 (по полкам и бригадам)",
        case="Д. 387, Списки потерь солдат 205 пехотного Шемахинского полка",
        scan_file="scans/gwar_donesenie13484876.jpg",
        comment=(
            "В списке (графы знаками повтора): холост; волость — «Дмитр.», селение не названо; ранен 17 июля 1917 г. "
            "Корпус: Петр Николаев Захаров — восприемник 1910 № 11."
        ),
    ),
)
