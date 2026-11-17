from verso.ru.dsl import (EventDate, Month, WwiiDocumentType, external_source_records, person,
                          wwii_record)

# ВОВ — pamyat-naroda.ru, послевоенное награждение (1967 г.). Внесены только люди,
# найденные в корпусе (реестр — EXTERNAL_SOURCES.md и external_sources/vov_pamyat.tsv).
dmitrievy_gory_external_sources_1967 = external_source_records(
    "Дмитриевы Горы",
    wwii_record(
        person("Федор", "Николаевич", "Кикеев", residence="Дмитриевы Горы"),
        source_url="https://pamyat-naroda.ru/heroes/podvig-chelovek_kartoteka1503974444/",
        birth_date=EventDate(1903),
        rank="рядовой",
        document_type=WwiiDocumentType.AWARD_CARD,
        award="Орден Славы III степени",
        draft_date=EventDate(1941),
        date=EventDate(1967, Month.JUNE, 8),
        archive="ЦАМО",
        archive_location="шкаф 39, ящик 1",
        comment=(
            "Картотека награждений. Место рождения на карточке: Владимирская обл., "
            "Меленковский р-н, с. Дм. Горы. Запись военкомата: дата выбытия — 1981 г. "
            "Корпус: метрика 04.06.1903 (МК 1903 № 20), отец Николай Флоров Кекев."
        ),
    ),
)
