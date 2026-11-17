"""The landlords' statuses of Дмитриевы Горы's books: Баташев, then the Шепелевы.

One of the villages' modules of the corpus's statuses (2026-11-16): `corpus.statuses` gathers them under the
name the DSL imports and the library reads; a village's public repository (tools/publish_village) carries its
own module alone. Their names are in every record's ratchet print: renaming one is DSL v2, never a cleanup.
"""
from verso.ru.dsl import Gender, Status

# In definition order, not sorted: the order is the catalog's (corpus/statuses.py gathers
# the villages' modules in it).
__all__ = [  # noqa: RUF022
    "BATASHEV_PEASANT",
    "BATASHEV_PEASANT_FEMALE",
    "BATASHEV_PEASANT_WIFE",
    "BATASHEV_PEASANT_SPOUSE",
    "BATASHEV_PEASANT_GIRL",
    "BATASHEV_PEASANT_SON",
    "BATASHEV_PEASANT_DAUGHTER",
    "SHEPELEV_PEASANT",
    "SHEPELEV_PEASANT_FEMALE",
    "SHEPELEV_PEASANT_WIFE",
    "SHEPELEV_PEASANT_LEGAL_WIFE",
    "SHEPELEV_PEASANT_WIDOWER",
    "SHEPELEV_PEASANT_SON",
    "SHEPELEV_PEASANT_DAUGHTER",
    "SHEPELEV_PEASANT_SPOUSE",
    "SHEPELEV_PEASANT_GIRL",
    "SHEPELEV_PEASANT_DAUGHTER_GIRL",
    "SHEPELEV_ZEMSKOY",
    "SHEPELEV_ZEMSKOY_WIFE",
    "SHEPELEV_CHILDREN_ZEMSKOY",
    "SHEPELEV_CHILDREN_ZEMSKOY_WIFE",
    "SHEPELEV_STEWARD",
    "SHEPELEV_FACTORY_STEWARD",
    "SHEPELEV_FACTORY_SERVANT",
]

# Landlord peasants — Баташев (Дмитриевы Горы, 1788–1821; the estate passes to the
# Шепелевы in 1822). The books name the owner after «вотчины», never «помещика» — he
# is «Г-на Коллежскаго Ассессора Ивана Родіоновича Баташева» in full. A birth record
# names the mother only «отъ жены его», so a wife is written as her husband's
# (regional-rules/dmitrievy-gory/README.md, Social Estates).
# The honorific is written as modern orthography writes it — «г-на», «гг.» — where
# the books capitalise it, «Г-на», «Г.Г.», «Гг.» (rules/extraction-rules.md §1a).
BATASHEV_PEASANT = Status("крестьянин вотчины г-на Баташева", Gender.MALE)
# The book's DEFAULTS for a woman it does not style — a newborn girl, a girl it buries:
# the estate kept, as the 1780 and 1787 books keep Глѣбовъ's and Баташевъ's.
BATASHEV_PEASANT_FEMALE = Status("крестьянка вотчины г-на Баташева", Gender.FEMALE)
BATASHEV_PEASANT_WIFE = Status("жена крестьянина вотчины г-на Баташева", Gender.FEMALE)
# The short forms, as PEASANT_SPOUSE is to PEASANT_WIFE: how the books of 1807–1818
# style a godmother, a wife or a girl, who stands at the font on her own.
BATASHEV_PEASANT_SPOUSE = Status("крестьянская жена вотчины г-на Баташева", Gender.FEMALE)
BATASHEV_PEASANT_GIRL = Status("крестьянская девка вотчины г-на Баташева", Gender.FEMALE)
# A child, as a peasant's child of an owner is styled throughout the catalog
# («крестьянский сын помещика …») and as the Дмитриевы Горы files already wrote the
# son by hand. `child_status_for` derives them from the parent; until 2026-10-03
# there were none, and a newborn or a buried child of a styled father fell to the
# book's bare «крестьянин»/«крестьянка» — 77 of them, every one a Шепелев serf's.
BATASHEV_PEASANT_SON = Status("крестьянский сын вотчины г-на Баташева", Gender.MALE)
BATASHEV_PEASANT_DAUGHTER = Status("крестьянская дочь вотчины г-на Баташева", Gender.FEMALE)

# Landlord peasants — Шепелевы (Дмитриевы Горы, from 1822). One family, owning
# through a minority and an inheritance, which the books write as it stood: «вотчины
# малолетных детей Г.Г. Шепелевых» 1822–1827, «детей Г.Г. Шепелевых» 1828–1830,
# «Г.Г. наследников Шепелевых» in 1825, «Г.Г. Шепелевых» from 1833, and «отчины Гг.
# Шепелевых» in the 1850s rolls. The wordings are kept apart because a record is
# transcribed as written; PSA reads them as one estate (parent_status.ESTATE_ALIASES).
# Except the peasants' owner as minors, children or heirs: «малолетных детей» is not
# written since 2026-10-02, «детей» and «наследников» since 2026-10-03, and the
# 1822–1830 books take the plain SHEPELEV_PEASANT(_WIFE). Nor is «отчины» (since
# 2026-10-03, the owner's ruling): the same owners as «вотчины», so the 1850, 1855
# and 1858 rolls and the 1859 book take the plain constants too; the DSL comments
# keep quoting the source as it is written.
SHEPELEV_PEASANT = Status("крестьянин вотчины гг. Шепелевых", Gender.MALE)
SHEPELEV_PEASANT_FEMALE = Status("крестьянка вотчины гг. Шепелевых", Gender.FEMALE)
SHEPELEV_PEASANT_WIFE = Status("жена крестьянина вотчины гг. Шепелевых", Gender.FEMALE)
# The mother as the books of 1833–1837 and 1859 write her, «у крестьянина … и законной
# жены его»: PEASANT_WIFE's words with the estate.
SHEPELEV_PEASANT_LEGAL_WIFE = Status("законная жена крестьянина вотчины гг. Шепелевых", Gender.FEMALE)
SHEPELEV_PEASANT_WIDOWER = Status("крестьянин вотчины гг. Шепелевых, вдовец", Gender.MALE)
SHEPELEV_PEASANT_SON = Status("крестьянский сын вотчины гг. Шепелевых", Gender.MALE)
SHEPELEV_PEASANT_DAUGHTER = Status("крестьянская дочь вотчины гг. Шепелевых", Gender.FEMALE)
# A wife and a girl standing at the font on their own, as BATASHEV_PEASANT_SPOUSE and
# _GIRL are for the estate before them: «крестьянская жена» (МК 1822, 1836, 1837,
# рождения), «крестьянская девка» (МК 1822-1829, 1859, рождения).
SHEPELEV_PEASANT_SPOUSE = Status("крестьянская жена вотчины гг. Шепелевых", Gender.FEMALE)
SHEPELEV_PEASANT_GIRL = Status("крестьянская девка вотчины гг. Шепелевых", Gender.FEMALE)
# An unmarried daughter as the books of the 1820s style a bride: «крестьянская дочь
# девка» (МК 1825 and 1828, венчания) — the role DAUGHTER_GIRL, as DAUGHTER_MAIDEN is
# «дочь девица», so the estate stays SHEPELEV_PEASANT.
SHEPELEV_PEASANT_DAUGHTER_GIRL = Status("крестьянская дочь девка вотчины гг. Шепелевых", Gender.FEMALE)
# The estate's own people: its земской (the peasants' elected head), its приказчики.
SHEPELEV_ZEMSKOY = Status("земской вотчины гг. Шепелевых", Gender.MALE)
SHEPELEV_ZEMSKOY_WIFE = Status("жена земского вотчины гг. Шепелевых", Gender.FEMALE)
SHEPELEV_CHILDREN_ZEMSKOY = Status("земской вотчины детей гг. Шепелевых", Gender.MALE)
SHEPELEV_CHILDREN_ZEMSKOY_WIFE = Status("жена земского вотчины детей гг. Шепелевых", Gender.FEMALE)
SHEPELEV_STEWARD = Status("приказчик вотчины гг. Шепелевых", Gender.MALE)
SHEPELEV_FACTORY_STEWARD = Status("приказчик Сноведского завода вотчины гг. Шепелевых", Gender.MALE)
SHEPELEV_FACTORY_SERVANT = Status("служитель Сноведского завода вотчины гг. Шепелевых", Gender.MALE)


# Estates the catalog spells under several bases, for `child_status_for` — the corpus's part
# of `verso.ru.domain.statuses._ESTATE_ALIASES`: a земской of the Шепелевы's estate (or of their
# children's) is its peasant.
CHILD_ESTATE_ALIASES: dict[str, str] = {
    "SHEPELEV_ZEMSKOY": "SHEPELEV_PEASANT",
    "SHEPELEV_CHILDREN_ZEMSKOY": "SHEPELEV_PEASANT",
}

# The corpus's part of `parent_status.ESTATE_ALIASES` (PSA): one Шепелевы estate under each
# wording the books give its own people — земской of the estate or of the owners' children,
# приказчики; as free text they agreed by the surname, as constants they must agree too.
ESTATE_ALIASES: dict[str, str] = {
    **{base: "SHEPELEV_PEASANT" for base in (
        "SHEPELEV_ZEMSKOY", "SHEPELEV_CHILDREN_ZEMSKOY",
        "SHEPELEV_STEWARD", "SHEPELEV_FACTORY_STEWARD", "SHEPELEV_FACTORY_SERVANT")},
}
