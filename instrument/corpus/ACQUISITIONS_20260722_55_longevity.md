# Acquisition ledger — AnAge Build 15 (2026-07-22, #55)

Acquired at her word ("go for it", the lifespan magnitude eval,
evening_addons_registration_55.md §2). Build-agent ledger entry,
written with the acquisition (mirror of the #52 manifest format);
chair review gates the commit. Full provenance:
`lexical_resources/lifespan/PROVENANCE.md`.  *(dir corrected #56b — see dedup note below)*

## Database received
**AnAge: the Animal Ageing and Longevity Database** (Human Ageing
Genomic Resources / HAGR), Build 15, release 2023-07-03. Tab-delimited
export, 1 header + 4646 species rows; the eval reads the measured
**"Maximum longevity (yrs)"** column, bridged to organ members via
Genus / Species / Common-name. Stored under `lexical_resources/lifespan/`.

| item | value |
|---|---|
| source (data) | https://genomics.senescence.info/species/dataset.zip |
| source (license) | https://genomics.senescence.info/legal.html |
| fetch date | 2026-07-22 |
| sha256 anage_dataset.zip | `e3ddb66e32e973a79932859ba53013e8f60d957c6ec01c6eb573e3ea3018d630` |
| sha256 anage_data.txt | `98867969fbd4d0bed6bab415c2715bb19079dbd7f92bdc26e5961856aa1c1519` |
| sha256 anage_release.html | `9187bfbb34abbc659a394a11d69d12ccdd6f7aff95620a1b1ac47374c7964b7b` |

## License (verified AT FETCH) — verdict: PERMITS research use + attribution
CC BY 3.0 Unported. Verbatim (legal.html): *"This work is licensed
under a Creative Commons Attribution 3.0 Unported License. In brief,
HAGR is free for all purposes, including commercial, educational, and
research purposes, provided you mention the use of HAGR in subsequent
presentations, publications, etc."* AnAge: *"made freely available to
everyone under the terms and conditions described in HAGR's license."*
Cite: de Magalhaes et al. (2024) *Nucleic Acids Research* 52(D1):D900-D908.

## What it feeds
`organ_lifespan_eval_55.py` → `results/organ_lifespan_eval_55.{json,md}`
(REPORT-ONLY). Class-separation test of the two temporal-referent
organs' ephemeral / enduring classes against measured maximum lifespan
(EN via WordNet taxonomic lemmas; ZH via HowNet W_E glosses, one
receipt per mapping, Unihan T→S fold, HowNet-DEF organism gate).

## Honest negative (coverage)
AnAge is vertebrate-centric. The **enduring** members that map land at
10^1.6–10^3.7 yr (tortoise 177, crane 45, bristlecone pine 5062). The
**ephemeral** referents (mayfly, epiphyllum, morning-mushroom) and the
EN members (ferns, wallflowers, magnolia, yew) are almost entirely
absent from AnAge → those classes yield 0 measurable species, so the
per-language AUC is **not computable** this build (a class is empty).
A full AUC would need a longevity DB covering short-lived
invertebrates / plants — a SEPARATE ledgered acquisition, not opened here.

## Acquisitions list after this delivery
One DB added (AnAge Build 15). No further longevity source acquired;
the short-lived-taxa gap is noted, not filled.

## Dedup note — #56b, 2026-07-23
This DB was vendored TWICE by parallel #55 agents (`longevity/` + `lifespan/`,
byte-identical). Consolidated to the canonical **`lexical_resources/lifespan/`**;
the `longevity/` twin was removed. The sha256 table above is unchanged (same
bytes); the canonical dir's filenames carry the `_build15` suffix
(`anage_dataset_build15.zip`, `anage_release_build15.html`) with identical
sha256. The "short-lived-taxa gap" upgrade was DEFERRED to post-08-01 at #56b's
adoption call — spec in `caesitas_proto/lifespan_upgrade_path_PROPOSED_56b.md`.
