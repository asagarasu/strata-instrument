# REGISTRATION — THE T'AO MINI-BOARD (#61 sitting build, 2026-07-28)
*陶淵明 飲酒 其五 × Arthur Waley 1918, built as an EXHIBITION-TIER board and MEASURED.
Her GO given, verbatim: "yes go for the 夕→dusk mini-board and we help figure_2."
Registered-before-delivery per house law. Alignments are law and hers — the map
ships as a DRAFT with the banner PENDING-PI-SIGNOFF. The census / heat-map
standing of this board is FLAGGED FOR HER REVIEW, NOT decided by the board agent.*

## EXHIBITION-TIER DECLARATION (of record)
This board is NOT part of the 8-board paper census. It is scored by its OWN
standalone scorer (`publishable/tao_yinjiu_exhibition_board_61.py`) into its OWN
namespace (`reports/figures/tao_yinjiu_exhibition/`). The census
(`linegrain_census_v47_61` → v43), the miner (`interesting_gen_61`) and the heat
map (`stack_heatmap_61`) each carry a hard-coded 8-board list
(`["sonnet18","qingqing","tiaotiao","xibei","albatros","correspondances",
"invitation","elevation"]`) and never see `tao_yinjiu`. The scorer REUSES the
committed scoring functions verbatim — `score_descriptive_fields`
(load_axes/scalar_readings/boolean_states, the REAL word boolean + scalar/top-tok),
`latent_score_54` (written_row_line/referent_row_line/_sensors, the REAL written +
referent channels), `linegrain_law_60` (CELL15/to3/line_state/chan_*, the census
law) — it invents no instrument. LaBSE certificate 0.00e+00.

## THE CRITICAL DIFFERENCE FROM ANTIGONÄ (task-named): BOTH SIDES FULLY COVERED
Antigonä's grc source had NO standing shelf (2-state starred, plus a bespoke grc
colour written STRETCH). Here BOTH languages are fully channel-covered, so we run
the REAL channels, not bespoke ones:
- **zh** (陶淵明): word boolean = `trait_labelers` (color/temporal/plant/sound) ∪
  `illumination_labeler_53` (illumination, zh-only) · written = `latent_score_54`
  ZhWritten · referent = `latent_score_54` referent (colour/sound).
- **en** (Waley): word boolean = `trait_labelers` · written = `latent_score_54`
  EnWritten (Skeat etym chains) · referent = `latent_score_54` referent.

## THE FINDING (measured) — the L7 crossing under full law
**zh L7 «山氣日夕佳» × Waley L7 «The mountain air is fresh at the dusk of day», on
the ILLUMINATION field, lands `LATENT-CARRY` — the EXPECTED verdict, MATCHED.**
Receipts (all live, all cited):
- **zh side = LATENT (written).** The word 日夕 fires the TEMPORAL boolean (`夕 日`,
  the 日/夕 radical rule) — the word reads TIME. The zh illumination WORD boolean
  (HowNet, `illumination_labeler_53`) does NOT fire. The illumination is carried by
  the CHARACTER 夕: MOE 《重編國語辭典修訂本》 s.v. 夕 = 傍晚、日落時分 (dusk / the hour
  the sun sets) · 泛指夜晚, the DARK pole. `hownet_had_it=false` (HowNet misses it).
  → latent-WRITTEN(illumination).
- **en side = LATENT (written).** en has no illumination WORD boolean (F2, zh-only).
  The illumination is carried by the etymon of *dusk*: **Skeat s.v. DUSK "dull,
  dark, dim. (E.)"** (`etymon_terms=[dark,dim]`, OE *dox*) — the live
  `latent_score_54` EnWritten fires it (`sensor=skeat_etym_chain`). The word states
  the hour, not the light. → latent-WRITTEN(illumination).
- **Cell = (latent, latent) = LATENT-CARRY.** Both words state TIME (日夕 / "dusk of
  day"); both bury the failing light of day in the written form. This is the first
  bilateral LATENT-CARRY suspect to survive BOTH channels (the c818d8a reading
  pass named it; here it is measured under full law).
Corroboration in the same line: the L7 TEMPORAL crossing is SURVIVAL (zh stated 日夕
× en stated "dusk of day") — both sides DO state time at the word tier, which is
exactly why the illumination is *latent*, not *stated*. The measurement is
internally consistent.

**HONESTY NOTE (task 1.3, "REPORT what IS"):** the verdict was NOT assumed. The zh
illumination word boolean was checked and returns False (did not fire on 日); the
line does not state illumination elsewhere (of the poem's 49 unique chars, only 夕
carries a MOE illumination sense — 日 is NOT in the MOE illumination charged set).
Had the zh illumination boolean fired on 日, or had illumination been stated
elsewhere, the crossing would have landed elsewhere; it did not. LATENT-CARRY is
what IS.

## THE ONE BOARD-LOCAL ADDITION (declared, the grc-LSJ precedent)
`corpus/tao_yinjiu/zh_illum_sense_chars_moe.json` — a poem-scoped zh WRITTEN
illumination inventory, **cited to the MOE dictionary** via the committed proposal
artifact `caesitas_proto/results/moe_illum_sense_chars_PROPOSED_54.json`. ONE row:
夕 (dark pole, 傍晚/日落). Wired as the zh WRITTEN illumination channel ON THIS BOARD
ONLY (never into `trait_labelers` / `illumination_labeler_53` /
`latent_written_labeler_53` / the census), exactly as the grc colour etymon channel
was board-local for `antigonae`.
- **WHY board-local:** the LIVE zh written labeler (`latent_written_labeler_53.py`)
  gates its MOE union to the COLOUR field only (line 283:
  `moe_snip = self.moe_color.get(c) if field=='color' else None`); illumination is
  HowNet-only by her standing ruling (README §illumination: "HowNet-only; no MOE
  union"). HowNet has no illumination sememe for 夕. So the print-charged
  illumination of 夕 is invisible to the live written channel — this board supplies
  it, cited, board-local.
- **⚠ MOE ARTIFACT STATUS = PROPOSED (DECLARED).** The upstream
  `moe_illum_sense_chars_PROPOSED_54.json` is STATUS "PROPOSED — concludes nothing;
  field owner adopts/amends/rejects" (session 54). It is NOT adopted into the live
  instrument (contrast the colour side, whose `moe_color_sense_chars_PROPOSED_53`
  IS adopted). This board-local illumination-written channel therefore rests on a
  PROPOSED (not-yet-ratified) MOE artifact. Declared here, in the board-local JSON,
  and on the exhibit face ("MOE artifact status: PROPOSED").

The **en side needs no patch**: `latent_score_54` EnWritten ALREADY fires
dusk→[dark,dim] (Skeat), it is merely tagged `informational_only` in the 8-board
census (L-F4: "no en illumination descriptive boolean (zh-only) → not
survival-counted"). On THIS board, where BOTH sides carry illumination, that en
written illumination becomes survival-eligible — declared. (This is a reading of
the REAL channel's own output, not a new instrument.)

## BOARD PROVENANCE
### Source (zh)
- **陶淵明《飲酒二十首》其五** (結廬在人境 … 欲辨已忘言, 10 five-character lines).
- **Text of record:** 逯欽立 校注《陶淵明集》(北京: 中華書局, 1979), 卷三 — the standard
  critical edition. The poem is one of the most textually stable in the classical
  canon.
- **Retrieval (house STOP rule — NEVER reconstructed from memory):** retrieved and
  cross-checked from two citable digital editions 2026-07-28 — 维基文库 (Wikisource)
  《飲酒 (陶淵明)》 and Chinese Text Project (ctext.org) 陶淵明集 / 箋註陶淵明集
  (欽定四庫全書本, ctext:184305, TOC-verified). The two agree character-for-character
  on all 10 lines except the declared final-line variant.
- **⚠ TEXTUAL VARIANT (final line), DECLARED:** the standard 中華書局/逯欽立 text (and
  the task) print 欲**辨**已忘言 (辨 'discern'); 維基文庫 prints 欲**辯**已忘言 (辯
  'argue'). 辨/辯 are a well-attested interchange in this line (both from the
  《莊子》「得意忘言」 allusion). The board adopts the standard-edition **辨** as text of
  record and declares the 辯 variant (in the source file + here). The variant is
  illumination-inert and does not touch the L7 crossing.
- **PD:** T'ao Ch'ien (365–427 CE) — the wording is public domain by any measure.
- File: `tao_yinjiu5_zh_source.txt` (its header carries the full provenance note).

### Seat (en)
- **Arthur Waley, *A Hundred and Seventy Chinese Poems*** (Constable 1918 / Knopf
  1919), CHAPTER III · POEMS BY T'AO CH'IEN, poem **(7)** ("I built my hut in a
  zone of human habitation").
- **Transcription source (F9):** Project Gutenberg **eBook #42290**, HTML edition,
  fetched by the chair by hand into `books/dnd2027/corpus_20260727/` on 2026-07-27.
  The 10 verse lines were extracted mechanically from the `<div class="poem">`
  verse spans, HTML stripped, Waley's lineation kept verbatim, grep-cross-checked.
- **PD (F9):** Waley's 1918/1919 translation is public domain (first published
  1918; the Gutenberg text is a PD edition). Quoted freely, in full, PD stated.
- File: `waley_en_1918.md`.

| seat | edition | date | PD | lines | L7 illumination |
|---|---|---|---|---|---|
| zh:tao_yinjiu5 | 逯欽立/中華書局 (retrieved Wikisource+ctext) | 1979 crit./ancient text | PD | 10 | **latent-written 夕 (MOE dark, board-local)** |
| en:waley_1918 | Waley, 170 Chinese Poems (Gutenberg #42290) | 1918 | PD (F9) | 10 | **latent-written dusk (Skeat [dark,dim], REAL)** |

### Dropped seats (declared)
None dropped. The mini-board is exactly the zh source + the one Waley seat, as she
scoped it ("the 夕→dusk mini-board"). No MT seat (declared: no MT for this board).
Other Waley-era renderings (e.g. the Gutenberg *More Translations from the Chinese*
volume also on the shelf) were NOT seated — this is a 1:1 demonstrative mini-board,
not a full ensemble; further seats are a corpus-scope call (below).

## ALIGNMENT — **DRAFT, PENDING-PI-SIGNOFF** (her standing order: its OWN table)
`corpus/tao_yinjiu/tao_yinjiu5__en_waley_1918.json` — the zh L1–10 ↔ Waley L1–10
map, extracted as its OWN table of record per her standing order ("yes to table but
its own table", the Antigonä precedent). The two texts are **strictly 1:1** (ten
lines each, same order, no fusion/split/drop/addition), so the map is a clean
identity; the only rendering liberties (南山 'southern hills' → 'summer hills'; 佳
'good' → 'fresh') are within-line word choices, not line-boundary events. Confidence
very high. **VERIFICATION PENDING — chair-drafted, NOT PI-approved;** banner
DRAFT-PENDING-PI-SIGNOFF stands until she blesses it (then the banner retires and
provenance updates to VERIFIED, per the `corpus/alignments/` convention).

## THE QUESTION FLAGGED FOR HER REVIEW (task 1.4 — NOT decided by the agent)
**Does this board enter the paper census, or annotate Figure 2 / the heat map?**
This zh→en pair is **fully channel-covered on both sides** (word boolean + written +
referent, both languages) — which makes it a **demonstrative-grade candidate**: it
could stand as a census board in its own right (unlike the de/fr seats, which are
colour-only word-tier). But whether it ENTERS the paper census, or instead
ANNOTATES Figure 2 / the heat map as an exhibition exemplar, is **the PI + the collaborator's
corpus-scope call, NOT the board agent's**. It is registered here as a flagged
question, scored and ready either way. (Caveats she will weigh: the zh
illumination-written leg rests on a PROPOSED MOE artifact; the alignment is a draft;
the board is 2-seat / 1:1, demonstrative rather than ensemble-scale.)

## NO-CENSUS-CONTAMINATION PROOF (the proof of isolation) — task 1.4 MANDATORY
The T'ao build adds only NEW files under `corpus/tao_yinjiu/`,
`publishable/tao_yinjiu_exhibition_board_61.py`, and
`reports/figures/tao_yinjiu_exhibition/`; it edits NO shared census instrument —
the board-local MOE illum channel lives in its own JSON, consulted only by the
T'ao scorer. Proof, BOTH census baselines:
- **vs v4.7** (`linegrain_census_v47_61.py`, the baseline at T'ao build time):
  re-run after the T'ao build was **BYTE-IDENTICAL**, sha256
  `900e7297bf58fd71dfa200c11993e861cbd8cf20b8aff0992c41c48f5138184b` before and
  after.
- **vs v4.8** (`linegrain_census_v48_61.py`, the current baseline after the
  EN-SOUND-FOLD + flag-audit rebuild): re-run after re-scoring the T'ao board is
  **BYTE-IDENTICAL**, sha256
  `19d127df6aadc85bba9fd433fb684071c9777043ef49f1fc0a6e044c556e7b54` before and
  after. The T'ao board adds ZERO census delta on top of the sound-fold baseline.
The paper census is untouched by the T'ao exhibition board either way.

## FILES
```
corpus/tao_yinjiu/
  tao_yinjiu5_zh_source.txt                       # zh source (逯欽立/中華書局, retrieved+cross-checked, PD) + 辨/辯 variant note
  waley_en_1918.md                                # Waley seat (Gutenberg #42290, PD, F9) + provenance
  zh_illum_sense_chars_moe.json                   # BOARD-LOCAL zh written illumination channel (MOE 夕, PROPOSED-declared)
  tao_yinjiu5__en_waley_1918.json                 # alignment table (1:1) — DRAFT, PENDING-PI-SIGNOFF
  REGISTRATION_tao_yinjiu_exhibition_0728_61.md   # this
publishable/tao_yinjiu_exhibition_board_61.py     # the exhibition scorer (isolated, REAL channels + board-local illum)
reports/figures/tao_yinjiu_exhibition/
  tao_yinjiu_board_61.json / .md                  # scored board + human table (all 10 lines × fields, crossings)
  exhibit_tao_yinjiu_L7_dusk_illumination.svg / .model.json  # the L7 dusk-illumination panel (gated, xmllint)
```

## RULING-GATED FOR HER
- **Alignment map** — DRAFT, PENDING-PI-SIGNOFF (own table; banner retires on her word).
- **Census / heat-map / Figure-2 standing** — FLAGGED FOR HER REVIEW (above); her call, not the agent's.
- **The board-local zh illumination-written channel rests on a PROPOSED MOE
  artifact** (moe_illum_sense_chars_PROPOSED_54) — hers to adopt/amend/reject; the
  board declares the PROPOSED status everywhere.
- The L7 LATENT-CARRY verdict is staked as measured under full law with live cited
  receipts (MOE 夕 · Skeat DUSK) — hers to adopt into the narrative or hold as
  exhibition-tier.


## HER RULINGS (the PI, 07-28 evening, 10 lines : 10 lines)
- **Alignment APPROVED**: "it is 10:10 then let's just roll with it" — the strict
  1:1 map stands; her note of record: alignment becomes a question only when a
  translator does something wild (omission, combination, inserted lines).
  DRAFT-PENDING banner retired.
- **MOE ADOPTED**: the MOE illumination sense-char inventory
  (moe_illum_sense_chars_PROPOSED_54.json) is adopted at her word — the
  PROPOSED-era filename stays as record; citations may drop the
  declared-proposed hedge from here on (exhibit faces update at next regen).
- **Class-B sound bases: KNOWN, NOT TREATED** (her ruling, same sitting):
  WordNet's marginal sound-senses (place/end/round/air/roll/beat) fire
  word-tier sound on bare forms — "a wordnet problem not our problem";
  let-be for now; also filed on the TODO shelf.
