from verso.ru.dsl import (EventDate, Month, WwiiDocumentType, external_source_records, person,
                          wwii_record)
from verso.ru.dsl.marital_status import MARRIED

# ВОВ — pamyat-naroda.ru, выбытие в 1942 г. Внесены только люди, найденные в корпусе
# (реестр всех карточек села — EXTERNAL_SOURCES.md и external_sources/vov_pamyat.tsv).
dmitrievy_gory_external_sources_1942 = external_source_records(
    "Дмитриевы Горы",
    wwii_record(
        person("Василий", "Андреевич", "Кикеев", residence="Дмитриевы Горы"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_dopolnitelnoe_donesenie57409306/",
        scan_file="scans/pamyat_058-0018004-0208_00000123.jpg",
        birth_date=EventDate(1899),
        rank="красноармеец",
        marital_status=MARRIED,
        casualty_reason="пропал без вести",
        document_type=WwiiDocumentType.CASUALTY_CLARIFICATION,
        draft_board="Выксунский РВК, Горьковская обл., Выксунский р-н",
        draft_date=EventDate(1942, Month.JANUARY, 9),
        casualty_date=EventDate(1942, Month.FEBRUARY, 13),
        date=EventDate(1942, Month.MARCH),
        archive="ЦАМО",
        fund="58",
        inventory="18004",
        case="208",
        comment=(
            "В листе (№ 92): красноармеец, стрелок, беспартийный; уроженец Владимирской обл., "
            "Ляховского р-на, с. Дмитриевы горы; выбыл 13 февраля 1942 г. — «считаю возможным "
            "учесть пропавшим без вести в феврале 1942 года». Жена — Кикеева Мария Егоровна, "
            "с. Сноведь Выксунского р-на Горьковской обл. "
            "Корпус: метрика 01.03.1899 (МК 1899 № 12), отец Андрей Иоаннов Кекев, восприемник "
            "Симеон Иоаннов Кекев. Печатная Книга памяти Нижегородской обл. тоже пишет его "
            "жителем Выксунского р-на, с. Сноведь."
        ),
    ),
    wwii_record(
        person("Василий", "Андреевич", "Кикеев", residence="Дмитриевы Горы"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_dopolnitelnoe_donesenie58508152/",
        scan_file="scans/pamyat_058-0018004-0547_00000279.jpg",
        birth_date=EventDate(1899),
        rank="красноармеец",
        marital_status=MARRIED,
        casualty_reason="пропал без вести",
        document_type=WwiiDocumentType.CASUALTY_CLARIFICATION,
        draft_board="Выксунский РВК, Горьковская обл., Выксунский р-н",
        draft_date=EventDate(1942, Month.JANUARY, 9),
        casualty_date=EventDate(1942, Month.FEBRUARY, 18),
        date=EventDate(1942, Month.MARCH),
        archive="ЦАМО",
        fund="58",
        inventory="18004",
        case="547",
        comment=(
            "Второй документ, уточняющий ту же потерю, в другом деле. В листе (№ 727): "
            "стрелок, беспартийный; «село Дмитрово горы Ляховского р-на Горьковской обл.»; "
            "выбыл 18 февраля 1942 г. — «считаю возможным учесть пропавшим без вести в марте "
            "1942 года» (в первом документе — 13 февраля). Жена — Кикеева Мария Егоровна, "
            "с. Сноведь Выксунского р-на Горьковской обл."
        ),
    ),
)
