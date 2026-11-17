from verso.ru.dsl import EventDate, Month, criminal_record, external_source_records, person
from verso.ru.dsl.statuses import PEASANT_MALE

# Судимость («Ведомости справок о судимости 1870–1927», familio.org /catalogs/vss/).
# Внесены только люди, найденные в корпусе (реестр всех записей села —
# EXTERNAL_SOURCES.md и external_sources/sudimost_vss.tsv).
# Кикѣевъ Семенъ Ивановъ, 27 л. (~1881 г. р.) — Симеон Иоаннов Кекев корпуса,
# восприемник в МК 1894 № 40 и 1899 № 12; сведён с записью 1899 г. (решение владельца
# 25.09.2026, кластер semen_ivanovich_kekev_1899).
dmitrievy_gory_external_sources_1908 = external_source_records(
    "Дмитриевы Горы",
    criminal_record(
        person("Семенъ", "Ивановъ", "Кикѣевъ", status=PEASANT_MALE, residence="Дмитриевы Горы"),
        age=27,  # → birth year derived: 1908 − 27 = 1881
        record_number=9281,
        date=EventDate(1908, Month.OCTOBER, 24),
        page="331",
        source_url="https://viewer.rsl.ru/ru/rsl01005455266?page=166",
        scan_file="scans/sudimost_kikeev_semen_1908.jpg",
        original_text=(
            "9281. КИКЕЕВ, СЕМЕН ИВАНОВЪ. К. Меленков. у., в. и с. Дмитриево-Горска, "
            "27 л.; — Г. С. 1 уч. г. Самары, 169 и 3 п. 171 М., тюр. 1½ м. "
            "Исп. 24 Окт. 908."
        ),
        bibliography=(
            "Ведомость справок о судимости / М-во юстиции. — СПб.: Тип. "
            "Правительствующего Сената, 1870–1929. 1909, кн. 1: Списки лиц, "
            "приговоренных к наказаниям… — 1909. С. 331. (РСЛ: rsl01005455266, скан с. 166.)"
        ),
        comment=(
            "Преступление: кража (ст. 169 Устава о наказаниях, налагаемых мировыми "
            "судьями, — кража на сумму не свыше 300 руб.; п. 3 ст. 171 — при "
            "отягчающих обстоятельствах). "
            "Суд: городской судья 1-го участка г. Самары. "
            "Наказание: тюрьма 1½ месяца. Исполнено 24 октября 1908 г. "
            "В печатной ведомости фамилия набрана «Кикѣевъ»."
        ),
    ),
)
