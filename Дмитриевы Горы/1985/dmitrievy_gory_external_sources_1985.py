from verso.ru.dsl import (EventDate, Month, WwiiDocumentType, external_source_records, person,
                          wwii_record)

# ВОВ — pamyat-naroda.ru, юбилейная картотека награждений 1985 г. (40-летие Победы).
# Внесены только люди, найденные в корпусе (реестр — EXTERNAL_SOURCES.md и
# external_sources/vov_pamyat.tsv). Вторая юбилейная карточка «Кикеев Александр
# Иванович, 1912, Орден Отечественной войны I степени» не внесена: год рождения
# расходится с метрикой, и это может быть другой человек.
dmitrievy_gory_external_sources_1985 = external_source_records(
    "Дмитриевы Горы",
    wwii_record(
        person("Александр", "Иванович", "Кикеев", residence="Дмитриевы Горы"),
        source_url="https://pamyat-naroda.ru/heroes/podvig-chelovek_yubileinaya_kartoteka1523023848/",
        birth_date=EventDate(1911),
        document_type=WwiiDocumentType.ANNIVERSARY_AWARD,
        award="Орден Отечественной войны II степени",
        award_number="74",
        date=EventDate(1985, Month.APRIL, 6),
        archive="ЦАМО",
        archive_location="шкаф 25, ящик 3",
        comment=(
            "Место рождения на карточке: Владимирская обл., с. Дм. Горы. "
            "Корпус: метрика 11.03.1911 (МК 1911 № 16), отец Иоанн Димитриев Кекев."
        ),
    ),
    wwii_record(
        person("Иван", "Иванович", "Кикеев", residence="Дмитриевы Горы"),
        source_url="https://pamyat-naroda.ru/heroes/podvig-chelovek_yubileinaya_kartoteka1523023858/",
        birth_date=EventDate(1917),
        document_type=WwiiDocumentType.ANNIVERSARY_AWARD,
        award="Орден Отечественной войны II степени",
        award_number="74",
        date=EventDate(1985, Month.APRIL, 6),
        archive="ЦАМО",
        archive_location="шкаф 25, ящик 3",
        comment=(
            "Место рождения на карточке: Владимирская обл., Меленковский р-н, д. Дмитриевы Горы. "
            "Записи военкомата: призван 10.06.1942 ВК Небыловского р-на Владимирской обл., "
            "ст. сержант; дата выбытия — 1993 г. "
            "Корпус: метрика 05.08.1917 (МК 1917 № 18), отец Иоанн Кекев."
        ),
    ),
    wwii_record(
        person("Николай", "Ефимович", "Кикеев", residence="Дмитриевы Горы"),
        source_url="https://pamyat-naroda.ru/heroes/podvig-chelovek_yubileinaya_kartoteka1523023872/",
        birth_date=EventDate(1916),
        document_type=WwiiDocumentType.ANNIVERSARY_AWARD,
        award="Орден Отечественной войны II степени",
        award_number="85",
        date=EventDate(1985, Month.APRIL, 6),
        archive="ЦАМО",
        archive_location="шкаф 25, ящик 3",
        comment=(
            "Место рождения на карточке: Владимирская обл., Ляховский р-н, с. Дм.-горы. "
            "Записи военкомата: Ляховский РВК, сержант; дата выбытия — 1983 г. "
            "Представлен к медали «За победу над Германией» как старшина 53 зенад. "
            "Корпус: метрика 01.05.1916 (МК 1916 № 17), отец Евфимий Иоаннов Кекев."
        ),
    ),
)
