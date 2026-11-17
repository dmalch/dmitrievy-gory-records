from verso.ru.dsl import (EventDate, Month, WwiDocumentType, external_source_records, person,
                          wwi_record)
from verso.ru.dsl.marital_status import MARRIED

# ПМВ — gwar.mil.ru («Памяти героев Великой войны»), событие 1916 г..
# Внесены только люди, найденные в корпусе (реестр всех карточек села —
# EXTERNAL_SOURCES.md и external_sources/pmv_gwar.tsv). Сканы сверены с указателем;
# расхождения — в comment.
dmitrievy_gory_external_sources_1916 = external_source_records(
    "Дмитриевы Горы",
    wwi_record(
        person("Андрей", "Васильевъ", "Кузинъ", residence="Дмитриевы Горы"),
        source_url="https://gwar.mil.ru/heroes/chelovek_donesenie14070613/",
        rank="рядовой",
        military_unit="313-й пехотный Балашовский полк",
        marital_status=MARRIED,
        casualty_reason="пропал без вести",
        date=EventDate(1916, Month.JULY, 26),
        document_type=WwiDocumentType.CASUALTY_LISTS,
        place_of_casualty="Карпатские горы, м. Жабе",
        archive="РГВИА",
        fund="Ф. 16196 — Особое делопроизводство по сбору и регистрации сведений о выбывших за смертью или за ранами, а также пропавших без вести воинских чинах (1914–1918)",
        inventory="Оп. 1, Именные списки потерь солдат и офицеров 1914–1918 (по полкам и бригадам)",
        case="Д. 508, Именные списки потерь солдат 313 пехотного Балашовского полка",
        scan_file="scans/gwar_donesenie14070613.jpg",
        comment=(
            "В списке: «Дмитріевогор. и села». "
            "Корпус: метрика 15.08.1888 (МК 1888 № 53), отец Василий Авксентьев Кузин."
        ),
    ),
    wwi_record(
        person("Василій", "Андреевъ", "Кокеевъ", residence="Дмитриевы Горы"),
        source_url="https://gwar.mil.ru/heroes/chelovek_donesenie13614854/",
        rank="ефрейтор",
        military_unit="310-й пехотный Шацкий полк",
        casualty_reason="ранен/контужен",
        date=EventDate(1916, Month.NOVEMBER, 26),
        document_type=WwiDocumentType.CASUALTY_LISTS,
        place_of_casualty="д. Валепутно, выс. 1243",
        archive="РГВИА",
        fund="Ф. 16196 — Особое делопроизводство по сбору и регистрации сведений о выбывших за смертью или за ранами, а также пропавших без вести воинских чинах (1914–1918)",
        inventory="Оп. 1, Именные списки потерь солдат и офицеров 1914–1918 (по полкам и бригадам)",
        case="Д. 504, Именные списки потерь солдат 310 пехотного Шацкого полка",
        scan_file="scans/gwar_donesenie13614854.jpg",
        comment=(
            "В списке волость — Дмитрогорская, селение не названо. "
            "Корпус: Василий Андреев Кекев — метрика 23.12.1889 (МК 1889 № 102), восприемник 1906, жених 1912 № 4."
        ),
    ),
)
