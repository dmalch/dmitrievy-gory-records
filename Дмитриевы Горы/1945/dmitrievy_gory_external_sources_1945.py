from verso.ru.dsl import (EventDate, Month, WwiiDocumentType, external_source_records, person,
                          wwii_record)

# ВОВ — pamyat-naroda.ru, награждение 1945 г. (приказ + наградной лист, ЦАМО ф. 33).
# Внесены только люди, найденные в корпусе (реестр — EXTERNAL_SOURCES.md и
# external_sources/vov_pamyat.tsv).
dmitrievy_gory_external_sources_1945 = external_source_records(
    "Дмитриевы Горы",
    wwii_record(
        person("Александр", "Иванович", "Кикеев", residence="Дмитриевы Горы"),
        source_url="https://pamyat-naroda.ru/heroes/podvig-chelovek_nagrazhdenie25861775/",
        scan_file=[
            "scans/pamyat_033-0686196-4491_00000545.jpg",
            "scans/pamyat_033-0686196-4491_00000688.jpg",
        ],
        birth_date=EventDate(1911),
        rank="гв. сержант",
        military_unit="артдивизион 28 гвардейской мотострелковой бригады 8 гвардейского танкового корпуса",
        document_type=WwiiDocumentType.AWARD_ORDER,
        award="Орден Красной Звезды",
        award_number="15/н",
        draft_board="Выксунский ГВК, Горьковская обл., г. Выкса",
        draft_date=EventDate(1941, Month.JUNE),
        date=EventDate(1945, Month.MARCH, 8),
        archive="ЦАМО",
        fund="33",
        inventory="686196",
        case="4491",
        comment=(
            "Приказ 28 гв. мсбр 8 гв. тк № 15/н от 08.03.1945 (строка 68) и наградной лист от 24.02.1945. По листу: гвардии сержант, оружейно-пулемётный "
            "мастер артдивизиона; 1911 г. р., русский, член ВКП(б) с ноября 1944 г.; на фронте с сентября 1942 г.; ранений нет; в армии с июня "
            "1941 г.; призван Выксунским РВК Горьковской обл.; ранее награждён орденом «Красная Звезда» 5.8.44 и медалью «За боевые заслуги» "
            "14.8.43. Подвиг: особенно отличился в районе Лебштадта и Лихтенталя, где под сильным артогнём вместе с орудийными мастерами "
            "устранил повреждения 2 орудий. Домашний адрес закрыт архивом. Корпус: метрика 11.03.1911 (МК 1911 № 16), отец Иоанн Димитриев Кекев."
        ),
    ),
)
