# REGISTRATION — THE YELLOW-CRANE MINI-BOARD (#64 sitting build, 2026-07-30)
*李白《黃鶴樓送孟浩然之廣陵》 × Ezra Pound 1915 (Cathay), built as an EXHIBITION-TIER board and
MEASURED. Sibling of the Li Bai 送友人 board (REGISTRATION_song_youren_exhibition_0730_64.md) and
the River-Merchant board (REGISTRATION_changgan_xing_exhibition_0730_64.md). Registered-before-
delivery per house law. Alignments are law and hers — the map ships as a DRAFT with the banner
PENDING-PI-SIGNOFF (and this map is NOT a clean identity: Pound splits the poem's final line, a
4→5 line-boundary event; the L3 target is a clean 1:1). The census / heat-map standing is FLAGGED
FOR HER REVIEW, NOT decided by the board agent.*

## EXHIBITION-TIER DECLARATION (of record)
This board is NOT part of the 8-board paper census. It is scored by its OWN standalone scorer
(`publishable/huanghelou_exhibition_board_64.py`) into its OWN namespace
(`reports/figures/huanghelou_exhibition/`). The census / miner / heat map each carry a hard-coded
8-board list and never see `huanghelou`. The scorer REUSES the committed scoring functions verbatim
— `score_descriptive_fields`, `latent_score_54`, `linegrain_law_60` — it invents no instrument.
**NO board-local channel is added** (COLOUR is a fully-wired shared field). **LaBSE certificate
0.00e+00**; replay-VERIFIED (encoded twice, second-run drift 0.00e+00, max reading disagreement
0.00e+00).

## THE FINDING (measured) — the L3 crossing under full law
**zh L3 «孤帆遠影碧山盡» ("the lone sail's far shade into the jade-green hills fades") × Pound «His
lone sail blots the far sky.», on the COLOUR field, lands `RENDERED`** (`linegrain_law_60.CELL15
[("ghost","active")]`). The task named the COLOUR axis and the reading pass anticipated a colour
LOSS; the measured cell is NOT a simple loss. The board scored HONESTLY whatever fell out (task
rule: "REPORT what IS"); the verdict is the full-law computation, never assumed. *No specific cell
was stated as "expected" for this crossing, so `verdict_matches_expected` is null (n/a) — the task
stated only the axis.*

### What was verified (the crossing, at board grade)
- **zh side = GHOST (meter/token).** THREE facts combine:
  1. The character 碧 (jade-green / azure, a 間色) does **NOT** fire the zh WORD-tier colour
     boolean. The live labeler `trait_labelers.zh_color` **deliberately holds 碧 latent** — it fires
     only inside listed compounds (`ZH_COMPOUNDS`: 碧色/碧綠/青碧…); in 碧山 it stands alone. Checked:
     `boolean_states("孤帆遠影碧山盡，","zh")["color"].fires = False`.
  2. The zh WRITTEN-colour cell **does carry a carrier** — `written_row_line(...)["color"]` reports
     `carrier_present=True, fires_bool=True, carriers=["碧"]` (碧, HowNet pair blue/蓝) — **BUT** the
     census law reader `linegrain_law_60.chan_written("color", …)` reads the key `fires_three_check`,
     which the colour written cell **does not set** (`fires_three_check=None`; its `scalar_check1` is
     `"PENDING"`). So the written channel does **not** promote 碧 to a latent STATE. And the colour
     REFERENT miner found no trigger word (`referent_trigger_words=[]`).
  3. BUT the **LaBSE colour DETECTOR fires a token-GHOST** on L3: read with its native punctuation
     (孤帆遠影碧山盡，), the maskable token **影碧山** — which **contains 碧** — has a positive colour
     Δ of **+0.0184 ≥ the cut 0.0149**, so `linegrain_law_60.triggered_tokens("color", …)` fires.
     With the word tier silent and no written/referent state, `linegrain_law_60.line_state` returns
     the zh colour state = **`ghost`** (via "meter (token)"). `to3(ghost) = "ghost"`.
- **en side = STATED (word).** Pound's line fires the en WORD-tier colour boolean, receipt
  `["sky"]` — **CLEAN, not plant-flagged**. `trait_labelers.en_color` is xkcd-colour-name-based and
  **"sky" is an xkcd colour name (a blue)**. So Pound's colour state is `stated` → `active`.
- **Cell = (ghost, active) = `RENDERED`** (`linegrain_law_60.CELL15[("ghost","active")]`).

### WHY the anticipated colour LOSS did NOT obtain — the honest mechanism
The reading-pass anticipation was that 碧 states a jade-green and Pound's "the far sky" drops the
hue → a colour loss (DEFORMATION-family). The measured chain is richer and honest in three ways:
1. 碧's colour is **REAL but held latent** at the word tier by construction (the 間色 tight-set
   policy, `trait_labelers` docstring: "碧 is DELIBERATELY held latent … it fires only inside
   compounds"), so it never reaches STATED.
2. The census law does **not** promote the colour WRITTEN carrier to a latent state (the
   colour-written scalar leg is unrun → `fires_three_check` absent → `chan_written` reads no fire).
   So 碧 is not `latent` either.
3. Yet the LaBSE colour **detector does see 碧's colour salience** (the token 影碧山 crosses the cut),
   so the state is `ghost` — the detector's account with no channel to claim it. Meanwhile Pound's
   "sky" is itself a colour term in the live inventory, so the seat is STATED. (ghost source × stated
   seat) = RENDERED: "the source's colour is only a meter-ghost; the seat realizes it as stated
   colour." The colour did not simply vanish; it re-surfaces as a detector-ghost on the source and a
   stated word on the seat.

Corroboration in the same board (internal consistency):
- **L1 故人西辭黃鶴樓 → "Ko-jin goes west from Ko-kaku-ro," = DEFORMATION** (zh 黃 "yellow" in 黃鶴樓
  STATES colour × Pound transliterates the tower name and drops "yellow"). Here the zh colour IS
  word-stated (黃 is a 正色, not held latent) and Pound genuinely drops it — a real colour loss. This
  isolates the L3 result: the machinery registers a stated-colour loss when it happens (L1), so L3's
  RENDERED is not an artefact — it is specifically because 碧 is held latent while "sky" mints colour.
- **L2 → "smoke-flowers blurred over the river" = GHOST-CARRY** (both sides colour-ghost).

**HONESTY NOTE (task rule "REPORT what IS"):** the verdict was NOT assumed. The zh word colour was
checked (False), the written cell was checked (carrier present, but `fires_three_check` absent so no
state), the referent was checked (no trigger), the LaBSE colour trigger was checked (影碧山 +0.0184 ≥
0.0149 → token-ghost), and the en word colour was checked (True, receipt "sky"). The crossing lands
RENDERED and is reported as such. NB the trailing punctuation is load-bearing: without the native
comma the 影碧山 token sits just below the cut (would give `silent`→absent, a different cell); the
board reads lines with their native punctuation, exactly as the 送友人/長干行 boards do.

## THE TEXTUAL VARIANT ON L3 (declared)
Wikisource records for L3 the standard manuscript-tradition variants: the fifth character has an
alternate 一作「緑」 (green) and an alternate 一作「空」 (empty/sky → 碧空盡). The board scores the
**MAIN reading 碧山盡** (碧, jade-green) per the text of record. Had the 一作「緑」 green-variant been
adopted, 緑 (green) IS in the 五色 term set and would fire the zh WORD colour → a DIFFERENT crossing
(zh stated × en stated = SURVIVAL). This is declared so the choice of reading is on the face; the
board does not adopt the variant.

## NO BOARD-LOCAL ADDITION (declared)
Nothing board-local is added. COLOUR is fully wired (zh/en word, zh/en written, colour referent all
run on the live instruments). The crossing is scored on the LIVE law, no patch. (Contrast the 送友人
plant board, which needed a board-local written-plant graph because the live HowNet plant inventory
missed 蕭.)

## BOARD PROVENANCE
### Source (zh)
- **李白《黃鶴樓送孟浩然之廣陵》** (故人西辭黃鶴樓 … 唯見長江天際流, 4 seven-character verse-lines,
  a 七言絕句).
- **Text of record:** 维基文库 (Wikisource) 《黃鶴樓送孟浩然之廣陵》, retrieved 2026-07-05, recorded
  in the committed corpus file `corpus/tang_en/zh_source/li_bai_huanghelou_song_menghaoran.txt`. The
  4 lines were copied verbatim from that committed repo file — **not re-typed from memory** (house
  STOP rule).
- **LINE NUMBERING — RESOLVED (task rule).** The poem is FOUR seven-character verse-lines, one per
  physical line. The board's source file `huanghelou_zh_source.txt` writes one verse-line per line so
  the parser reads **four** lines. The TARGET 孤帆遠影碧山盡 is **verse-line 3**. Confirmed from the
  actual source text; recorded in the source file header and here.
- **TEXTUAL VARIANT (L3):** declared above and in the source header (碧 main; 緑/空 variants).
- **PD:** Li Bai (701–762 CE) — public domain in all jurisdictions; the Wikisource transcription is a
  community-maintained PD text.
- File: `huanghelou_zh_source.txt`.

### Seat (en)
- **Ezra Pound, *Cathay*** (Elkin Mathews, 1915), "Separation on the River Kiang" (Pound's rendering
  of 黃鶴樓送孟浩然之廣陵; poet given as "Rihaku").
- **Transcription source (F9):** Project Gutenberg **eBook #50155**, fetched 2026-07-05 into
  `corpus/tang_en/raw/pound_cathay_1915.txt`. "Separation on the River Kiang" begins at **line 479**
  (title); the five body lines are lines 480–484. Copied verbatim; line-for-line cross-checked.
- **PD (F9):** Pound's *Cathay* (1915) is public domain. Quoted freely, in full, PD stated.
- File: `pound_en_1915.md`.
- **LINE-BOUNDARY EVENT (declared).** Pound's rendering has **five** body lines against the poem's
  **four** verse-lines: he **splits** the final zh line 唯見長江天際流 across his lines 4 and 5 ("And
  now I see only the river," / "The long Kiang, reaching heaven."). The first three zh lines map 1:1
  to Pound's first three; zh L4 → Pound [4, 5]. The **L3 TARGET is a clean 1:1**, unaffected by the
  split.

| seat | edition | date | PD | lines | L3 colour |
|---|---|---|---|---|---|
| zh:huanghelou | Li Bai 黃鶴樓送孟浩然之廣陵 (Wikisource text of record) | Tang, 8th c. | PD | 4 | **GHOST (meter/token) — 碧 held latent at word tier; written carrier present but not state-promoted; LaBSE colour token-ghost on 影碧山 (contains 碧)** |
| en:pound_1915 | Pound, Cathay (Gutenberg #50155) | 1915 | PD (F9) | 5 (→4, split) | **STATED (word) — "sky" is an xkcd colour name (receipt sky, clean)** |

### Dropped seats (declared)
None seated beyond the one Pound seat. The corpus also holds two other PD renderings (Shigeyoshi
Obata, *The Works of Li Po* 1922, poem No. 40, "On Seeing off Meng Hao-jan"; Amy Lowell & Florence
Ayscough, *Fir-Flower Tablets* 1921, "At the Yellow Crane Tower…"), catalogued in
`corpus/tang_en/zh_source/li_bai_huanghelou_song_menghaoran.txt`. They were NOT seated (the task's
deliverable is ONE verified seat). Registered as available for a follow-up ensemble build; NOT built.

## ALIGNMENT — **DRAFT, PENDING-PI-SIGNOFF** (her standing order: its OWN table)
`corpus/huanghelou/huanghelou__en_pound_1915.json` — the zh L1–4 ↔ Pound L1–5 map, its OWN table of
record. **This is NOT a clean identity:** zh L1–3 map 1:1 to Pound L1–3, but **zh L4 → Pound [4, 5]**
(a split). This is exactly the case her standing note names ("alignment becomes a question when a
translator does something wild"), so the PENDING-PI-SIGNOFF banner is not a formality. The alignment
JSON records the split and `target_seat_line_joined`. The **L3 target is a clean 1:1**.
**VERIFICATION PENDING — chair-drafted, NOT PI-approved.**

## THE QUESTION FLAGGED FOR HER REVIEW — NOT decided by the agent
**Does this board enter the paper census, annotate a figure, or stay a filed exhibition exemplar?**
the PI + the collaborator's corpus-scope call. Caveats she will weigh: (a) the target crossing came out
**RENDERED via a colour token-ghost** — a rich *methodology* exemplar (it shows 碧's held-latent
word status, the un-promoted written carrier, AND the LaBSE detector picking up 碧's colour salience
as a ghost, all at once), but not a clean loss showpiece; (b) the alignment carries a genuine 4→5
split; (c) the board is 2-seat / demonstrative; (d) the L3 verdict is punctuation-sensitive (declared).

## NO-CENSUS-CONTAMINATION PROOF (the proof of isolation)
The Yellow-Crane build adds only NEW files under `corpus/huanghelou/`,
`publishable/huanghelou_exhibition_board_64.py`, and `reports/figures/huanghelou_exhibition/`; it
edits NO shared census instrument. No existing script, census file, findings JSON, or the frozen poem
江上吟 was touched. The isolation is structural: no shared file is written or imported-for-mutation.

## FILES
```
corpus/huanghelou/
  huanghelou_zh_source.txt                          # zh source (Wikisource text of record, PD) + L3 variant + line-numbering resolution
  pound_en_1915.md                                  # Pound seat (Gutenberg #50155, PD, F9) + provenance + 4→5 split note
  huanghelou__en_pound_1915.json                    # alignment table — DRAFT, PENDING-PI-SIGNOFF; zh L4 → Pound [4,5] split
  REGISTRATION_huanghelou_exhibition_0730_64.md     # this
publishable/huanghelou_exhibition_board_64.py       # the exhibition scorer (isolated, REAL channels, no board-local augment)
reports/figures/huanghelou_exhibition/
  huanghelou_board_64.json / .md                    # scored board + human table (all 4 lines × fields, colour crossings)
  exhibit_huanghelou_L3_bi_color.svg / .model.json  # the L3 colour panel (gated, xmllint)
```

## LAW CITATIONS (the instruments this board rests on, imported not reimplemented)
- `linegrain_law_60.CELL15[("ghost","active")] = "RENDERED"` — the verdict cell.
- `linegrain_law_60.line_state` — precedence word STATED > written latent > referent > GHOST (token)
  > silent; the zh side falls through to the token-ghost branch.
- `linegrain_law_60.triggered_tokens` — the colour token-ghost (影碧山 +0.0184 ≥ cut 0.0149); colour
  is a SALIENCE axis (positive-only trigger, `SALIENCE_TRIGGER_FIELDS`).
- `linegrain_law_60.chan_written` — reads `fires_three_check` (absent for colour) → no written state.
- `linegrain_law_60.to3` — {stated→active, ghost→ghost, latent→latent, silent→absent}.
- `score_descriptive_fields.scalar_readings` — the LaBSE line-scalar + certificate (0.00e+00,
  replay-verified).
- `score_descriptive_fields.boolean_states → trait_labelers.zh_color / en_color` — zh_color holds 碧
  latent; en_color charges "sky" (xkcd colour name).
- `latent_score_54.written_row_line` — the zh written-colour cell (碧 carrier present, three-check
  unrun); `referent_row_line` — the colour referent miner (no trigger on L3).

## RULING-GATED FOR HER
- **Alignment map** — DRAFT, PENDING-PI-SIGNOFF (own table; the zh L4 → Pound [4,5] split; banner
  retires on her word).
- **Census / figure / exhibition standing** — FLAGGED FOR HER REVIEW; her call, not the agent's.
- **The RENDERED verdict** (source colour a meter-ghost via 碧; seat colour stated via "sky") is
  staked as measured under full law with live cited receipts. Hers to read as a methodology exemplar
  (碧's triple status: word-latent, written-carrier-not-promoted, detector-ghost) or to hold. NB the
  L3 verdict is punctuation-sensitive (影碧山 sits just above the cut with the native comma) —
  declared, hers to weigh.
