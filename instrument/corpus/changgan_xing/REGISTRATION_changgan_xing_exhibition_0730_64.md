# REGISTRATION — THE RIVER-MERCHANT MINI-BOARD (#64 sitting build, 2026-07-30)
*李白《長干行》其一 × Ezra Pound 1915 (Cathay), built as an EXHIBITION-TIER board and
MEASURED. Sibling of the Li Bai 送友人 board (REGISTRATION_song_youren_exhibition_0730_64.md)
and the T'ao 夕→dusk board. Registered-before-delivery per house law. Alignments are law and
hers — the map ships as a DRAFT with the banner PENDING-PI-SIGNOFF. The census / heat-map
standing of this board is FLAGGED FOR HER REVIEW, NOT decided by the board agent.*

## EXHIBITION-TIER DECLARATION (of record)
This board is NOT part of the 8-board paper census. It is scored by its OWN standalone scorer
(`publishable/changgan_xing_exhibition_board_64.py`) into its OWN namespace
(`reports/figures/changgan_xing_exhibition/`). The census / miner / heat map each carry a
hard-coded 8-board list and never see `changgan_xing`. The scorer REUSES the committed scoring
functions verbatim — `score_descriptive_fields` (load_axes/scalar_readings/boolean_states, the
REAL word boolean + scalar), `latent_score_54` (written_row_line/referent_row_line/_sensors, the
REAL written + colour-referent channels), `linegrain_law_60` (CELL15/to3/line_state/chan_*, the
census law) — it invents no instrument. **NO board-local channel is added:** COLOUR is a
fully-wired shared field (word boolean + written + colour referent all run through
`LAW.line_state`), so unlike the 送友人 plant board (which supplied a board-local written-plant
graph) this board scores the crossing on the LIVE law with nothing bespoke. **LaBSE certificate
0.00e+00**; replay-VERIFIED (encoded twice, second-run drift 0.00e+00, max reading disagreement
0.00e+00).

## THE FINDING (measured) — the L20 crossing under full law
**zh L20 «一一生綠苔» ("there, one by one, the green moss grows") × Pound «By the gate now, the
moss is grown, the different mosses,», on the COLOUR field, lands `SURVIVAL` — NOT the task's
EXPECTED `DEFORMATION`. `verdict_matches_expected = FALSE`, reported honestly (task rule:
"REPORT what IS"; the verdict is NOT faked to match the expectation).**

### What was verified (the crossing, at board grade)
- **zh side = STATED (word).** The character 綠 (green) fires the zh WORD-tier colour boolean of
  the live descriptive labeler (`trait_labelers.zh_color`, the derived 五色 term set — 青赤黃白黑
  正色 + 綠紅碧紫 間色 anchored to 禮記·玉藻, Wikisource PD), receipt `["綠"]`. Per
  `linegrain_law_60.line_state` precedence (word STATED > written latent > referent), the zh
  colour state is `stated` → `active`.
- **en side = STATED (word).** Pound's line fires the en WORD-tier colour boolean, receipt
  `["moss"]` — **CLEAN, not plant-flagged**. The live en colour labeler `trait_labelers.en_color`
  is xkcd-colour-name-based (Berlin & Kay BK11 ∪ the single-token xkcd names in `xkcd_rgb.txt`),
  and **"moss" is an xkcd colour name (a green)**. So Pound's colour state is `stated` → `active`.
- **Cell = (active, active) = `SURVIVAL`** (`linegrain_law_60.CELL15[("active","active")]`).

### WHY the expected DEFORMATION did NOT obtain — the honest mechanism
The task's expectation rested on the premise that Pound **drops the colour** (renders "the
different mosses" with no hue-word — "green" indeed does not appear), so that the crossing would
be `(active, absent) = DEFORMATION`. That premise is **falsified by the live instrument**: the en
colour labeler is not a hue-word list, it is the **xkcd colour-name inventory**, in which "moss"
is a named green. The colour does not vanish across the crossing — it **re-lands lexically** on
the colour-charged noun "moss". This is the SAME class of finding as the 送友人 plant board: a
lexeme-aware (there, radical-aware) descriptive labeler charges a word the task assumed was
colour-silent, so the crossing is a SURVIVAL, not the loss the reading pass anticipated.

Corroboration in the same board (internal consistency — the machinery detects colour on both
sides where present, and detects genuine losses where they occur):
- **L4 青梅 → "blue plums" = SURVIVAL** (青 blue STATED × Pound "blue" STATED) — colour survives
  when Pound keeps a hue-word.
- **L26 紅顏老 → "I grow older" = ECHO** (紅 red STATED × Pound colour ghost/absent of a hue) —
  a genuine colour LOSS, where Pound's compression drops the 紅顏 "rosy face". The instrument
  DOES register loss when it happens; the L20 result is not an artefact of a colour-blind seat.
- **L22 落葉秋風早 → "The leaves fall early…" = INVENTION** and **L23/L24 → "yellow with August"
  / West-garden grass = RENDERED** — Pound adds colour where the zh line has none.
So the L20 SURVIVAL is a real measured outcome: both 綠 and "moss" charge colour at the word tier.

**HONESTY NOTE (task rule "REPORT what IS"):** the verdict was NOT assumed. The zh word colour
boolean was checked and returns **True** on 綠 (receipt `["綠"]`); the en word colour boolean was
checked and returns **True** on **"moss"** (receipt `["moss"]`, clean). The crossing lands
SURVIVAL and is reported as such. Had Pound's line carried no colour-name noun (e.g. had he
written "the growth by the gate"), the en side would have fallen silent and the crossing would
have been the expected DEFORMATION — but it did not, because "moss" is itself a colour term in
the live inventory.

## NO BOARD-LOCAL ADDITION (declared)
Unlike the 送友人 plant board (which supplied a board-local written-plant single-graph inventory
because the live HowNet plant inventory missed 蕭), this board adds NOTHING board-local. COLOUR is
the most fully-wired field in the pipeline: the zh word colour (`trait_labelers.zh_color`), the zh
written colour (`latent_written_labeler_53` via `latent_score_54.ZhWritten`), the en word colour
(`trait_labelers.en_color`), the en written colour (Skeat etymon via `EnWritten`), and the colour
referent (`latent_score_54.referent_row_line`, the one referent miner that is wired) all run on the
live instruments. The crossing is scored on the LIVE law, no patch.

### A note on the WRITTEN colour channel (for the record — it did not change the verdict)
The zh WRITTEN colour cell of `written_row_line("一一生綠苔","zh")` reports `carrier_present=true,
carriers=["綠"]` (綠 is a written-colour carrier), but its `scalar_check1` is `"PENDING"` and it
carries **no `fires_three_check`** key — so `linegrain_law_60.chan_written("color", …)` reads it as
**not firing** a latent state (the census law does not promote the colour-written carrier to a
STATE while the written-colour scalar leg is unrun). This is moot on L20 because the WORD tier
already STATES colour via 綠; it is recorded here as the honest behaviour of the colour-written
channel under the law of record (the same is true on L4/L26 etc.).

## BOARD PROVENANCE
### Source (zh)
- **李白《長干行》其一** (妾髮初覆額 … 直至長風沙, 30 five-character verse-lines, a 樂府 narrative;
  其一 is the poem Pound rendered).
- **Text of record:** 维基文库 (Wikisource) 《長干行二首》, retrieved 2026-07-05, recorded in the
  committed corpus file `corpus/tang_en/zh_source/li_bai_changgan_xing.txt` (【其一】 block).
  The 30 lines of 其一 were copied verbatim from that committed repo file — **not re-typed from
  memory** (house STOP rule). (其二 is a separate, authorship-disputed poem — "此篇一作張潮,
  黃庭堅作李益" — and is NOT part of this board; the dispute does not touch 其一.)
- **LINE NUMBERING — RESOLVED (task rule).** The corpus file prints 其一 as FIFTEEN physical rows
  (couplet layout, two verse-lines per row). The board's source file `changgan_xing_zh_source.txt`
  writes ONE verse-line per physical line so the parser reads **thirty** lines. The TARGET
  一一生綠苔 is **verse-line 20** — the second half of the tenth couplet's row 「門前遲行跡，
  一一生綠苔。」. Confirmed from the actual source text; recorded in the source file header and here.
- **PD:** Li Bai (701–762 CE) — public domain in all jurisdictions; the Wikisource transcription is
  a community-maintained PD text.
- File: `changgan_xing_zh_source.txt`.

### Seat (en)
- **Ezra Pound, *Cathay*** (Elkin Mathews, 1915), "The River-Merchant's Wife: a Letter" (Pound's
  rendering of 長干行 其一; poet given as "Rihaku", per the Fenollosa notebooks).
- **Transcription source (F9):** Project Gutenberg **eBook #50155**, fetched 2026-07-05 into
  `corpus/tang_en/raw/pound_cathay_1915.txt` (from `pound_cathay_1915_raw.html` via
  `pandoc -f html -t plain`). "The River-Merchant's Wife: a Letter" begins at **line 149** (title);
  the thirty body lines are lines 150–179. Copied verbatim; line-for-line cross-checked.
- **PD (F9):** Pound's *Cathay* (1915) is public domain (published 1915; PG #50155 PD edition).
  Quoted freely, in full, PD stated.
- File: `pound_en_1915.md`.
- **LINE-COUNT NOTE (declared).** Pound's rendering has **thirty** body lines against the poem's
  **thirty** verse-lines — the counts MATCH at 30 = 30, but Pound is famously NOT character-faithful
  (he compresses couplets, e.g. 常存抱柱信/豈上望夫臺 → "Forever and forever, and forever." / "Why
  should I climb the look out?", and expands elsewhere). So the 30↔30 map is a chair-drafted
  POSITIONAL correspondence, NOT a mechanical identity, and it is a live alignment question per the PI's
  standing note. For the **L20 TARGET** the correspondence is a clean positional 1:1
  (zh L20 ↔ Pound body line 20).

| seat | edition | date | PD | lines | L20 colour |
|---|---|---|---|---|---|
| zh:changgan_xing | Li Bai 長干行 其一 (Wikisource text of record) | Tang, 8th c. | PD | 30 | **STATED (word) — 綠 charges the 五色 term set (receipt 綠)** |
| en:pound_1915 | Pound, Cathay (Gutenberg #50155) | 1915 | PD (F9) | 30 | **STATED (word) — "moss" is an xkcd colour name (receipt moss, clean)** |

### Dropped seats (declared)
None seated beyond the one Pound seat. The corpus also holds two other PD renderings of 長干行 其一
(Shigeyoshi Obata, *The Works of Li Po* 1922, poem No. 105, `firflower`/`obata` raws catalogued in
`corpus/tang_en/zh_source/li_bai_changgan_xing.txt`; Amy Lowell & Florence Ayscough, *Fir-Flower
Tablets* 1921, "Ch'ang Kan"). They were NOT seated: the task's deliverable is ONE verified seat
(Pound 1915), and a second seat is not trivial here (each needs its own alignment resolution against
the 30-line source). Registered as available for a follow-up ensemble build; NOT built here.

## ALIGNMENT — **DRAFT, PENDING-PI-SIGNOFF** (her standing order: its OWN table)
`corpus/changgan_xing/changgan_xing__en_pound_1915.json` — the zh L1–30 ↔ Pound L1–30 map, its OWN
table of record per her standing order. The counts match at 30, but the interior map is chair-drafted
POSITIONAL (several rows are Pound's free rendering of a compressed couplet, not line-faithful), so
the PENDING-PI-SIGNOFF banner is not a formality. The TARGET row (L20 colour) is the only crossing
this board scores; it is a clean positional 1:1. **VERIFICATION PENDING — chair-drafted, NOT
PI-approved.**

## THE QUESTION FLAGGED FOR HER REVIEW — NOT decided by the agent
**Does this board enter the paper census, annotate a figure, or stay a filed exhibition exemplar?**
the PI + the collaborator's corpus-scope call, NOT the board agent's. Caveats she will weigh: (a) the target
crossing came out **SURVIVAL, not the expected DEFORMATION** — a clean *methodology* exemplar (it
shows the descriptive en colour labeler is xkcd-name-based and so charges "moss" as a colour), but
it is NOT a colour-loss showpiece; (b) the alignment is a 30↔30 positional draft with genuine
compression rows; (c) the board is 2-seat / demonstrative rather than ensemble-scale.

## NO-CENSUS-CONTAMINATION PROOF (the proof of isolation)
The River-Merchant build adds only NEW files under `corpus/changgan_xing/`,
`publishable/changgan_xing_exhibition_board_64.py`, and `reports/figures/changgan_xing_exhibition/`;
it edits NO shared census instrument. No existing script, census file, findings JSON, or the frozen
poem 江上吟 was touched. The isolation is structural: no shared file is written or imported-for-
mutation by this board (it imports the committed instruments read-only).

## FILES
```
corpus/changgan_xing/
  changgan_xing_zh_source.txt                       # zh source (Wikisource text of record, PD) + line-numbering resolution
  pound_en_1915.md                                  # Pound seat (Gutenberg #50155, PD, F9) + provenance + 30↔30 count note
  changgan_xing__en_pound_1915.json                 # alignment table — DRAFT, PENDING-PI-SIGNOFF; 30↔30 positional
  REGISTRATION_changgan_xing_exhibition_0730_64.md  # this
publishable/changgan_xing_exhibition_board_64.py    # the exhibition scorer (isolated, REAL channels, no board-local augment)
reports/figures/changgan_xing_exhibition/
  changgan_xing_board_64.json / .md                 # scored board + human table (all 30 lines × fields, colour crossings)
  exhibit_changgan_xing_L20_lu_color.svg / .model.json  # the L20 colour panel (gated, xmllint)
```

## LAW CITATIONS (the instruments this board rests on, imported not reimplemented)
- `linegrain_law_60.CELL15[("active","active")] = "SURVIVAL"` — the verdict cell.
- `linegrain_law_60.line_state` — precedence word STATED > written latent > referent > silent.
- `linegrain_law_60.to3` — {stated→active, latent→latent, silent→absent}.
- `linegrain_law_60.chan_word / chan_written / chan_referent / triggered_tokens` — the channel
  readers; colour is a SALIENCE axis (positive-only trigger, `SALIENCE_TRIGGER_FIELDS`).
- `score_descriptive_fields.scalar_readings` — the LaBSE line-scalar + the replay/certificate
  (drift 0.00e+00, < 1e-6 house law; replay-verified).
- `score_descriptive_fields.boolean_states → trait_labelers.zh_color / en_color` — the word colour
  labelers (zh 五色 term set incl. 綠; en xkcd colour names ∪ BK11 incl. "moss").
- `latent_score_54.written_row_line → ZhWritten/EnWritten` — the written colour channels;
  `referent_row_line` — the colour referent miner.

## RULING-GATED FOR HER
- **Alignment map** — DRAFT, PENDING-PI-SIGNOFF (own table; the 30↔30 positional interior in
  particular; banner retires on her word).
- **Census / figure / exhibition standing** — FLAGGED FOR HER REVIEW; her call, not the agent's.
- **The SURVIVAL verdict** (not the expected DEFORMATION) is staked as measured under full law with
  live cited receipts (綠 word-colour; "moss" en word-colour, clean). Hers to read as a methodology
  exemplar (the en colour inventory is xkcd-name-based, so colour-charged nouns like "moss" carry
  the field) or to hold.
