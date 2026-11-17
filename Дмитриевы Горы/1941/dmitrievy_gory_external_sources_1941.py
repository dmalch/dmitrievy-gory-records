from verso.ru.dsl import (EventDate, Month, WwiiDocumentType, external_source_records, person,
                          wwii_record)
from verso.ru.dsl.marital_status import MARRIED

# ВОВ — pamyat-naroda.ru, пропавшие без вести в 1941 г. Внесены только люди, найденные
# в корпусе (реестр всех карточек села — EXTERNAL_SOURCES.md и external_sources/vov_pamyat.tsv).
# Оба — на одном листе алфавитного списка Ляховского РВК (ЦАМО 58-18004-570, штамп
# «8373/1-о 6.42», т. е. июнь 1942 г.). Даты взяты из текста листа; указатель
# «Памяти народа» даёт другие (см. comment).
dmitrievy_gory_external_sources_1941 = external_source_records(
    "Дмитриевы Горы",
    wwii_record(
        person("Сергей", "Иванович", "Кикеев", residence="Дмитриевы Горы"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_dopolnitelnoe_donesenie58086941/",
        scan_file="scans/pamyat_058-0018004-0570_00000171.jpg",
        birth_date=EventDate(1905),
        rank="красноармеец",
        military_unit="п/п 14?2 (указатель: 146 стрелковая дивизия, п/п 1482)",
        marital_status=MARRIED,
        casualty_reason="пропал без вести",
        place_of_casualty="Ленинградский фронт",
        document_type=WwiiDocumentType.CASUALTY_CLARIFICATION,
        draft_board="Ляховский РВК, Владимирская обл., Ляховский р-н",
        draft_date=EventDate(1941, Month.AUGUST, 13),
        casualty_date=EventDate(1941, Month.NOVEMBER, 18),
        date=EventDate(1941, Month.DECEMBER),
        archive="ЦАМО",
        fund="58",
        inventory="18004",
        case="570",
        comment=(
            "В листе: красноармеец, стрелок, беспартийный; «рм-Горы» (Дмитриевы Горы); призван "
            "Ляховским РВК 13.8.41 (в указателе — 18.08.1941); «с 18.11.41 г.» нет связи, п/п 14?2 "
            "(третья цифра перебита: 1432 или 1482); «полагать пропавшим без вести под "
            "Ленинградским фронтом в дек. 41 г.» (в указателе дата выбытия — 02.1942, по "
            "карандашной помете «2.42»). Жена — Кикеева Анна Петровна. "
            "Корпус: метрика 03.09.1905 (МК 1905 № 51), отец Иоанн Михайлов Кекев."
        ),
    ),
    wwii_record(
        person("Илья", "Егорович", "Кикеев", residence="Дмитриевы Горы"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_dopolnitelnoe_donesenie58086936/",
        scan_file="scans/pamyat_058-0018004-0570_00000171.jpg",
        birth_date=EventDate(1900),
        rank="красноармеец",
        marital_status=MARRIED,
        casualty_reason="пропал без вести",
        document_type=WwiiDocumentType.CASUALTY_CLARIFICATION,
        draft_board="Ляховский РВК, Владимирская обл., Ляховский р-н",
        draft_date=EventDate(1941, Month.AUGUST, 29),
        casualty_date=EventDate(1941, Month.NOVEMBER),
        date=EventDate(1941, Month.DECEMBER),
        archive="ЦАМО",
        fund="58",
        inventory="18004",
        case="570",
        comment=(
            "В листе: красноармеец, стрелок, беспартийный; «рм-Горы» (Дмитриевы Горы); призван "
            "Ляховским РВК 29.?.41 (месяц на машинописи — 3 или 8; в указателе — 29.08.1941); "
            "«с ноября 1941 г. адреса нет»; «полагать пропавшим без вести в дек. 4? г.». "
            "Указатель даёт дату выбытия 02.1945 — невозможно для листа, составленного в июне "
            "1942 г. Жена — Кикеева Евдокия (отчество читается плохо, возможно Сергеевна). "
            "Корпус: метрика 10.07.1900 (МК 1900 № 30), отец Георгий Максимов Кекев."
        ),
    ),
)
