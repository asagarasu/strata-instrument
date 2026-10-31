# REGISTRATION — THE LI BAI MINI-BOARD (#64 sitting build, 2026-07-30)
*李白《送友人》 × Ezra Pound 1915 (Cathay), built as an EXHIBITION-TIER board and
MEASURED. Sibling of the T'ao 夕→dusk board (REGISTRATION_tao_yinjiu_exhibition_0728_61.md).
Registered-before-delivery per house law. Alignments are law and hers — the map ships
as a DRAFT with the banner PENDING-PI-SIGNOFF (and this map is NOT a clean identity:
Pound splits the poem's final line, an 8→9 line-boundary event). The census / heat-map
standing of this board is FLAGGED FOR HER REVIEW, NOT decided by the board agent.*

## EXHIBITION-TIER DECLARATION (of record)
This board is NOT part of the 8-board paper census. It is scored by its OWN standalone
scorer (`publishable/song_youren_exhibition_board_64.py`) into its OWN namespace
(`reports/figures/song_youren_exhibition/`). The census / miner / heat map each carry a
hard-coded 8-board list and never see `song_youren`. The scorer REUSES the committed
scoring functions verbatim — `score_descriptive_fields` (load_axes/scalar_readings/
boolean_states, the REAL word boolean + scalar), `latent_score_54` (written_row_line/
referent_row_line/_sensors, the REAL written + referent channels), `linegrain_law_60`
(CELL15/to3/line_state/chan_*, the census law) — it invents no instrument. **LaBSE
certificate 0.00e+00.**

## THE FINDING (measured) — the L8 crossing under full law
**zh L8 «蕭蕭班馬鳴» (the poem's final line) × Pound «Our horses neigh to each other / as
we are departing.», on the PLANT field, lands `DEFORMATION` — NOT the task's EXPECTED
`LATENT-UNREALIZED`. `verdict_matches_expected = FALSE`, reported honestly (task rule:
"REPORT what IS"; the verdict is NOT faked to match the expectation).**

### What was verified (the crossing, at board grade)
- **zh side = STATED (word).** The character 蕭 fires the zh WORD-tier plant boolean of
  the live descriptive labeler (`trait_labelers`), receipt `["蕭"]`. Per
  `linegrain_law_60.line_state` precedence (**word STATED > written latent > referent**),
  the zh plant state is `stated` → `active`.
- **en side = ABSENT (silent).** Pound's rendering of the line carries no plant word
  (word boolean silent), and the en WRITTEN plant channel is UNAVAILABLE in
  `latent_score_54` (no en plant etymon inventory — Skeat's `FIELD_TERMS` cover
  colour/dark only). So en plant is `silent` → `absent`. (The joined seat line for the
  crossing is "Our horses neigh to each other as we are departing.")
- **Cell = (active, absent) = `DEFORMATION`** (`linegrain_law_60.CELL15[("active","absent")]`).

### WHY the expected LATENT-UNREALIZED did NOT obtain — the honest mechanism
The task's expectation rested on the premise that 蕭's plant is carried **only latently,
via the WRITTEN channel** (the 艸 radical), so that the zh side would be `latent` and the
crossing `(latent, absent) = LATENT-UNREALIZED`. That premise is **falsified by the live
instrument**:
- The live DESCRIPTIVE plant labeler `trait_labelers.zh_plant()` is **itself
  radical-attestation-based**: a char charges as plant iff it is attested in **《爾雅》
  釋草/釋木** (Erya, the ancient Chinese thesaurus, Wikisource PD) **AND** carries a
  **Kangxi plant radical** (Unihan `kRSUnicode`; `PLANT_RADICALS` includes **140 = 艸**).
- 蕭 satisfies **both**: it is a 釋草 (herb-chapter) headword — the artemisia (艾蒿 / 香草)
  sense — and it carries radical **140** (`kRSUnicode 140.12`). So `zh_plant()` charges it
  and the zh **WORD** plant boolean fires. (Note the simplified 萧 is NOT in the traditional
  Erya text and does NOT fire — it is the traditional 蕭 of the source that charges.)
- The **same radical evidence** the board-local WRITTEN file cites is therefore **already
  promoted to the WORD tier** by the radical-aware descriptive labeler. There is no gap for
  the written-latent channel to fill: the plant is *realized*, not *latent*.

Corroboration in the same board (internal consistency):
- The **L4 plant crossing is SURVIVAL** — zh 蓬 (孤蓬 "lone tumbleweed", the drifting
  Artemisia/fleabane) stated × Pound "dead grass" stated. Pound **does** render plant
  elsewhere; the machinery detects plant on both sides when it is present. This isolates
  the L8 result: Pound's *horse* line simply carries no plant, and 蕭's plant is
  word-realized — so the loss is a DEFORMATION (source states, seat drops), not a latent
  carry.
- The word 蕭蕭 (reduplicated) reads as ONOMATOPOEIA — the rustling / the horses'
  whinnying (the MOE 釋義 [形] 寂寥冷清 "蕭瑟"/"蕭條" sound-adjective sense; it modifies
  班馬鳴). Accordingly the zh L8 **sound** boolean also fires (`鳴[廣韻]`). The reduplicative
  realizes SOUND; its 艸-radical botanical sense is the *graph's* plant charge — which the
  radical-aware word labeler already counts.

**HONESTY NOTE (task rule "REPORT what IS"):** the verdict was NOT assumed. The zh word
plant boolean was checked and returns **True** on 蕭; the REAL HowNet written-plant channel
was checked and returns **False** (HowNet misses 蕭, below); the en word/written plant were
checked and are **absent/unavailable**. The crossing lands DEFORMATION and is reported as
such. Had the word labeler NOT charged 蕭 (e.g. had 蕭 not been an Erya 釋草 headword, or had
the labeler been sememe-based like HowNet), the zh side would have fallen through to the
board-local WRITTEN carrier and the crossing would have been the expected LATENT-UNREALIZED
— but it did not, because the live word tier is radical-aware.

## THE ONE BOARD-LOCAL ADDITION (declared, the tao-illum / grc-LSJ precedent)
`corpus/song_youren/zh_plant_sense_chars_written.json` — a poem-scoped zh WRITTEN plant
single-graph inventory. ONE row: 蕭, cited to **(1) Unicode Unihan `kRSUnicode` = 140.12**
(Kangxi radical 140 = 艸/grass-plant — the SAME Unihan data-file family the law's variant
fold reads, `linegrain_law_60._fold_map`, and the SAME radical field `trait_labelers`
reads), and **(2) MOE 《重編國語辭典修訂本》** s.v. 蕭 (部首字=艸; 釋義 [名]1 一種香草，即艾蒿),
which itself cites **《說文解字．艸部》「蕭，艾蒿也」** (Shuowen Jiezi, c. 100 CE). Wired as the
zh WRITTEN plant channel ON THIS BOARD ONLY (never into `trait_labelers` /
`latent_written_labeler_53` / the live `hownet_plant_chars_54.json` inventory / the census),
exactly as the tao illumination channel and the grc colour etymon channel were board-local.
- **WHY board-local:** the LIVE zh written-plant inventory
  (`caesitas_proto/results/hownet_plant_chars_54.json`, read by
  `latent_score_54.load_zh_carriers → ZhWritten`) is **HowNet-sememe-based and
  SIMPLIFIED-DOMINANT**, and **misses 蕭**: HowNet records 蕭 (traditional) as the bare
  placeholder `{character|文字:belong={China|中国}}` (exactly the 蘭/楓 simplified-dominance
  case the plant inventory itself documents) and 萧 (simplified) as `{desolate|荒}` /
  `{surname|姓}` — **no plant sememe on either**. Checked: 蕭 and 萧 are both absent from the
  259 `charged_chars_any_position`. So 蕭's print-charged plant (radical 艸, sense 艾蒿) is
  invisible to the live written channel; the board supplies it, cited, board-local.
- **STATUS = SETTLED CITATION (declared), NOT PROPOSED.** Unlike the tao illumination board
  (which rested on a PROPOSED MOE illum artifact), this board's written-plant evidence rests
  on the Unihan `kRSUnicode` radical field (a stable, adopted data source already used by the
  live instruments) and on MOE headword facts. The board-local status is about **SCOPE** (not
  wired into the shared instrument), not about the reliability of the citation.
- **The en side needs no patch and gets none:** en PLANT is UNAVAILABLE in `latent_score_54`
  (no en plant etymon inventory — Skeat covers colour/dark only). The en written-plant leg is
  the honest n/a; Pound's plant is absent on both the word and written tiers on the target line.

## BOARD PROVENANCE
### Source (zh)
- **李白《送友人》** (青山橫北郭 … 蕭蕭班馬鳴, 8 five-character verse-lines, a 五言律詩 in four
  couplets).
- **Text of record:** 维基文库 (Wikisource) 《送友人_(李白)》, retrieved 2026-07-05, recorded in
  the committed corpus survey `corpus/tang_en/overlap_manifest.md` (SOURCE block) and
  `corpus/tang_en/zh_source/li_bai_song_you_ren.txt`. The 8 lines were copied verbatim from
  that committed repo file — **not re-typed from memory** (house STOP rule).
- **LINE NUMBERING — RESOLVED (task rule).** The corpus file prints the poem as FOUR physical
  rows (couplet layout, two verse-lines per row). The board's source file
  `song_youren_zh_source.txt` writes ONE verse-line per physical line so the parser reads
  **eight** lines. The TARGET 蕭蕭班馬鳴 is the **final (eighth) verse-line** — the second half
  of the fourth couplet's row. Confirmed from the actual source text; recorded in the source
  file header and here.
- **PD:** Li Bai (701–762 CE) — public domain in all jurisdictions; the Wikisource
  transcription is a community-maintained PD text.
- File: `song_youren_zh_source.txt`.

### Seat (en)
- **Ezra Pound, *Cathay*** (Elkin Mathews, 1915), "Taking Leave of a Friend" (Pound's
  rendering of 送友人; poet given as "Rihaku", the Japanese reading of 李白, per the Fenollosa
  notebooks).
- **Transcription source (F9):** Project Gutenberg **eBook #50155**, fetched 2026-07-05 into
  `corpus/tang_en/raw/pound_cathay_1915.txt` (from `pound_cathay_1915_raw.html` via
  `pandoc -f html -t plain`). "Taking Leave of a Friend" begins at **line 485** (title);
  the nine body lines are lines 486–494. Copied verbatim; grep-cross-checked.
- **PD (F9):** Pound's *Cathay* (1915) is public domain (published 1915; PG #50155 PD edition).
  Quoted freely, in full, PD stated.
- File: `pound_en_1915.md`.
- **LINE-BOUNDARY EVENT (declared).** Pound's rendering has **nine** body lines against the
  poem's **eight** verse-lines: he **splits** the final zh line 蕭蕭班馬鳴 across his lines 8
  and 9 ("Our horses neigh to each other" / "as we are departing."). The first seven zh lines
  map 1:1 to Pound's first seven; zh L8 → Pound [8, 9]. For the L8 crossing the two Pound lines
  are **joined** into one target rendering so the seat-state reflects Pound's full rendering.

| seat | edition | date | PD | lines | L8 plant |
|---|---|---|---|---|---|
| zh:song_youren | Li Bai 送友人 (Wikisource text of record) | Tang, 8th c. | PD | 8 | **STATED (word) — 蕭 charges 爾雅釋草 ∧ 艸 radical; also latent-written 蕭 (board-local)** |
| en:pound_1915 | Pound, Cathay (Gutenberg #50155) | 1915 | PD (F9) | 9 (→8, split) | **ABSENT — no plant word; en written plant UNAVAILABLE** |

### Dropped seats (declared)
None seated beyond the one Pound seat. The corpus also holds two other PD renderings of
送友人 (Shigeyoshi Obata, *The Works of Li Po* 1922, "Taking Leave of a Friend", poem No. 60;
Amy Lowell & Florence Ayscough, *Fir-Flower Tablets* 1921, "Saying Good-Bye to a Friend" —
both catalogued in `corpus/tang_en/overlap_manifest.md`). They were NOT seated: the task's
deliverable is ONE verified seat (Pound 1915), and a second seat is not trivial here because
each would need its own alignment resolution against the 8-line source. Registered as
available for a follow-up ensemble build if she wants it; NOT built here.

## ALIGNMENT — **DRAFT, PENDING-PI-SIGNOFF** (her standing order: its OWN table)
`corpus/song_youren/song_youren__en_pound_1915.json` — the zh L1–8 ↔ Pound L1–9 map, its OWN
table of record per her standing order. **This is NOT a clean identity:** zh L1–7 map 1:1 to
Pound L1–7, but **zh L8 → Pound [8, 9]** (a split). This is exactly the case her standing note
names ("alignment becomes a question when a translator does something wild — omission,
combination, inserted lines"), so the PENDING-PI-SIGNOFF banner is not a formality here. The
alignment JSON records `target_seat_line_joined` (the joined L8 rendering used for the crossing)
and flags the split for her review. **VERIFICATION PENDING — chair-drafted, NOT PI-approved.**

## THE QUESTION FLAGGED FOR HER REVIEW — NOT decided by the agent
**Does this board enter the paper census, annotate a figure, or stay a filed exhibition
exemplar?** This is the PI + the collaborator's corpus-scope call, NOT the board agent's. Caveats she will
weigh: (a) the target crossing came out **DEFORMATION, not the expected LATENT-UNREALIZED** —
useful as a *methodology* exemplar (it shows the descriptive plant labeler is radical-aware and
thus promotes graph-latent plant to the word tier), but it is NOT a clean latent-carry showpiece;
(b) the alignment carries a genuine 8→9 split; (c) the board is 2-seat / non-identity,
demonstrative rather than ensemble-scale.

## NO-CENSUS-CONTAMINATION PROOF (the proof of isolation)
The Li Bai build adds only NEW files under `corpus/song_youren/`,
`publishable/song_youren_exhibition_board_64.py`, and
`reports/figures/song_youren_exhibition/`; it edits NO shared census instrument — the
board-local written-plant channel lives in its own JSON, consulted only by the Li Bai scorer.
No existing script, census file, findings JSON, or the frozen poem 江上吟 was touched.
(A byte-identical census re-run proof of the tao form was not executed by the board agent this
sitting — the census baseline hashes are the chair's to record; the isolation is structural: no
shared file is written or imported-for-mutation by this board.)

## FILES
```
corpus/song_youren/
  song_youren_zh_source.txt                          # zh source (Wikisource text of record, PD) + line-numbering resolution
  pound_en_1915.md                                   # Pound seat (Gutenberg #50155, PD, F9) + provenance + 8→9 split note
  zh_plant_sense_chars_written.json                  # BOARD-LOCAL zh written-plant channel (蕭: Unihan radical 140 艸 + MOE/Shuowen 艾蒿)
  song_youren__en_pound_1915.json                    # alignment table — DRAFT, PENDING-PI-SIGNOFF; zh L8 → Pound [8,9] split
  REGISTRATION_song_youren_exhibition_0730_64.md     # this
publishable/song_youren_exhibition_board_64.py       # the exhibition scorer (isolated, REAL channels + board-local plant augment)
reports/figures/song_youren_exhibition/
  song_youren_board_64.json / .md                    # scored board + human table (all 8 lines × fields, crossings)
  exhibit_song_youren_L8_xiao_plant.svg / .model.json  # the L8 plant panel (gated, xmllint)
```

## LAW CITATIONS (the instruments this board rests on, imported not reimplemented)
- `linegrain_law_60.CELL15[("active","absent")] = "DEFORMATION"` — the verdict cell.
- `linegrain_law_60.line_state` — precedence word STATED > written latent > referent > silent
  (the reason the word-tier plant fire wins over the board-local written latent).
- `linegrain_law_60.to3` — {stated→active, latent→latent, silent→absent}.
- `linegrain_law_60.chan_word / chan_written / triggered_tokens` — the channel readers; plant is
  a SALIENCE axis (positive-only trigger, `SALIENCE_TRIGGER_FIELDS`).
- `score_descriptive_fields.scalar_readings` — the LaBSE line-scalar + the replay/certificate
  (drift 0.00e+00, < 1e-6 house law).
- `score_descriptive_fields.boolean_states → trait_labelers.zh_plant()` — the radical-aware word
  plant labeler (《爾雅》釋草/釋木 ∧ Kangxi `PLANT_RADICALS` incl. 140 艸) that charges 蕭.
- `latent_score_54.written_row_line → ZhWritten` over `hownet_plant_chars_54.json` — the REAL
  written-plant channel (HowNet-sememe-based; misses 蕭).
- `latent_score_54` EnWritten — en plant UNAVAILABLE (no en plant etymon; Skeat colour/dark only).

## RULING-GATED FOR HER
- **Alignment map** — DRAFT, PENDING-PI-SIGNOFF (own table; the zh L8 → Pound [8,9] split in
  particular; banner retires on her word).
- **Census / figure / exhibition standing** — FLAGGED FOR HER REVIEW; her call, not the agent's.
- **The DEFORMATION verdict** (not the expected LATENT-UNREALIZED) is staked as measured under
  full law with live cited receipts (蕭 word-plant via 爾雅∧radical; board-local written 蕭 via
  Unihan 140 + Shuowen 艾蒿; Pound plant absent). Hers to read as a methodology exemplar or hold.
- **The board-local written-plant channel** (蕭 via Unihan radical + MOE/Shuowen) — hers to
  adopt into the shared plant instrument or leave board-local. NB it would only change the
  WRITTEN tier; the WORD tier already charges 蕭 via the radical-aware descriptive labeler.

---

## SOUND-AXIS ADDENDUM (2026-07-30) — the first author's follow-up: *at word grain, is 蕭蕭 SOUND-latent?*
*Extends the SAME L8 crossing (蕭蕭班馬鳴 × Pound "Our horses neigh to each other / as we are
departing.") to the SOUND axis and reports per-WORD channel status. Same discipline: REAL
instruments only, EXHIBITION-tier isolation, LaBSE certificate with a replay-verify leg,
outputs in the same namespace with `_sound` suffixes. Nothing else touched. Scored honestly;
what the instruments say is reported, not what any expectation wants.*

### THE ANSWER (measured) — **NO: 蕭蕭 is NOT word-grain sound-latent.**
At word grain **no LATENT channel (written / referent) claims 蕭 for sound while the word tier
stays silent** — the pre-condition for "sound-latent" is not met. Precisely:
- **蕭's word-tier sound = SILENT.** 蕭 falls in NONE of the three zh sound legs
  (`trait_labelers._zh_sound_legs`: 爾雅釋樂 definienda ∪ 音-radical 180 ∪ 廣韻 gloss-head).
  Checked all three — 蕭 ∈ 釋樂? False; ∈ 音部(180)? False; ∈ 廣韻? False.
- **蕭's WRITTEN-sound (latent) = SILENT.** The REAL zh written-sound channel
  (`latent_score_54.ZhWritten.word_fire(·, "sound")` over
  `hownet_sound_chars_54_amended.json`, 171 charged chars) does NOT fire on 蕭: **蕭 is absent
  from the hownet_sound carrier inventory**, so check (3) carrier-present fails. `written_row_line`
  reports L8 sound `carrier_present=false, fires_bool=false, carriers=[]`.
- **蕭's sound REFERENT = n/a (not a claim).** The referent miner
  (`latent_score_54.referent_row_line`) is **colour-only** (`field=='color'`); it emits no
  per-word sound referent row for any word. So there is no referent channel to claim 蕭 either.
  (This is the honest null the plant board also declared for the sound referent leg.)
- Therefore **蕭 is claimed by NO descriptive/latent sound channel at word grain.** It is not
  sound-latent (no latent claim with the word tier silent) and it is **not a sound-GHOST at its
  own grain**: zh L8 tokenises as ONE jieba unit `蕭蕭班馬鳴` (`maskable_units`), so 蕭/蕭蕭 are
  **not separately maskable** — there is no per-char sound Δ to be a ghost from; and even the
  whole-line LaBSE sound salience is moot because the WORD tier already STATES sound, which
  outranks any ghost.

### WHAT DOES fire — sound is word-STATED, but via **鳴**, and 蕭蕭 fires the DEVICE tier
- **zh L8 sound state = `stated` (via word), receipt `鳴[廣韻]`.** The state is made by **鳴**
  (the 廣韻 gloss-head leg), NOT by 蕭. (`chan_word("sound", L8)` → `["鳴[廣韻]"]`, `stated`.)
- The reduplicative **蕭蕭 fires ONLY the DEVICE tier** — `sound_device = 叠字:蕭蕭` (reduplication
  onomatopoeia). This is **sound as EUPHONY-ENACTED**, a DISTINCT organ from the descriptive /
  latent SOUND field the question asks about (the #58 device≠descriptive split, `label_unit`
  emits it under the separate key `sound_device`). So the intuition "蕭蕭 is a sound word" is
  correct at the DEVICE tier and correct as onomatopoeia — but it is NOT a *latent* charge on
  the descriptive SOUND field, and the descriptive SOUND on the line is carried by 鳴.

### THE CROSSING (under full law, `CELL15`)
- **Source (zh L8):** sound `stated` (word, via 鳴) → `active`.
- **Seat (Pound L8+L9 joined):** "**neigh**" fires the en WORD-tier sound via **WordNet
  auditory closure** (`trait_labelers.en_sound_word`, receipt `neigh[wn]`) → sound `stated` →
  `active`. (Nothing else on the seat claims sound at the word tier; the seat's LaBSE sound
  salience is below-cut for `neigh` and the one above-cut token is the function-word artifact
  `as` — moot, since the word tier already STATES.)
- **CELL = (active, active) = `SURVIVAL`** (`linegrain_law_60.CELL15[("active","active")]`).
  This matches the plant board's own all-fields table (its L8 sound crossing row = SURVIVAL) —
  cross-validated, the addendum reuses the identical instruments.

### word × channel → fires / receipt (the deliverable table)
| word | word-tier sound | written-sound (latent) | sound referent | device tier | LaBSE own-token |
|---|---|---|---|---|---|
| **蕭** | silent (no 釋樂/音部/廣韻 leg) | silent (∉ hownet_sound 171-char inventory) | n/a (miner colour-only) | **FIRES** `叠字:蕭蕭` (euphony ENACTED) | not separately maskable (one jieba unit) |
| **鳴** | **FIRES** `鳴[廣韻]` | silent | n/a (miner colour-only) | silent | not separately maskable (one jieba unit) |
| **neigh** (Pound seat) | **FIRES** `neigh[wn]` (WordNet auditory closure) | — (en written-sound UNAVAILABLE) | — | — | — |

*(en written-sound is UNAVAILABLE by construction: `latent_score_54.EnWritten` — Skeat
`FIELD_TERMS` cover colour/dark/star only; sound/plant/temporal have no en-etymon list. The
honest n/a, unchanged from the plant board.)*

### LaBSE SOUND-detector trigger status (rule 1, the scalar tail)
- **sound cut = 0.0242** (SUGGESTED tier; **SOUND is a SALIENCE axis** →
  `SALIENCE_TRIGGER_FIELDS` → **positive-only** trigger, `dd >= cut`).
- **zh L8** sound line-scalar **+0.2024**. Its only content jieba unit is the whole line
  `蕭蕭班馬鳴` (dd **+0.2311**, fires the cut). 蕭蕭 is not separable from this unit, so the
  salience cannot be attributed to 蕭蕭 alone — and it is moot for the state (word STATED wins).
- **Pound seat (joined)** sound line-scalar **−0.0367**. Per-token: `neigh` dd **+0.0213**
  (BELOW cut), `as` dd **+0.0297** (above cut — a function-word artifact), `departing.` −0.0200,
  `horses` −0.0140. `triggered_tokens(sound)` on the seat = `[('as', 0.0297)]` — moot (word
  tier STATES via neigh). On Pound's physical L8 alone ("Our horses neigh to each other"),
  `neigh` dd +0.0202 (below cut) and NO token fires.

### CERTIFICATE (addendum discipline) — replay-VERIFIED
The encoder leg ran. **LaBSE re-order certificate drift = 0.00e+00** (< 1e-6 house law). The
addendum additionally **REPLAY-VERIFIED** it: the inventory was encoded a **second, independent
time** — second-run drift **0.00e+00**, and the **max per-field reading disagreement between the
two runs = 0.00e+00** (identical readings; e.g. zh L8 sound = +0.202436 both runs). **No drift.**

### ISOLATION (no-census-contamination, sound addendum)
Adds only NEW files: `publishable/song_youren_exhibition_board_64_sound.py` and, in the same
namespace, `reports/figures/song_youren_exhibition/song_youren_board_64_sound.{json,md}`
(the `_sound` suffixes). It **imports** the committed instruments (score_descriptive_fields,
latent_score_54, linegrain_law_60, trait_labelers) but writes/mutates **none** of them; it does
not touch any census file, and it does not touch the plant board's outputs. Structural isolation,
same as the plant board.

### FILES (sound addendum)
```
publishable/song_youren_exhibition_board_64_sound.py     # the SOUND-axis addendum scorer (REAL instruments, isolated)
reports/figures/song_youren_exhibition/
  song_youren_board_64_sound.json / .md                  # per-word sound channels + crossing + the direct answer
```

### RULING-GATED FOR HER (sound addendum)
- **The SURVIVAL verdict** (L8 sound, via 鳴 × neigh) is staked as measured under full law with
  live receipts. Hers to read alongside the plant DEFORMATION as a fuller L8 picture.
- **The finding "蕭蕭 is device-tier sound, not descriptive/latent sound"** is a clean methodology
  point: it shows the pipeline separates ENACTED euphony (叠字) from MENTIONED/charged sound, and
  that the descriptive sound on this line is 鳴's, not 蕭蕭's. Not the agent's call whether to
  surface it in the paper.

---

## TEMPORAL-AXIS ADDENDUM (2026-07-30) — the corpus reading pass's L5 claim: *temporal by referent (浮雲 = ephemeral)*
*Takes the SAME 送友人 board to the TEMPORAL axis at L5: 浮雲遊子意 ("floating cloud — the
wanderer's mind") × Pound "Mind like a floating wide cloud." Same discipline: REAL instruments
only, EXHIBITION-tier isolation, LaBSE certificate with a replay-verify leg, outputs in the same
namespace with `_temporal` suffixes. Nothing else touched. The POINT of this crossing (per the
task) is to DOCUMENT AN INSTRUMENT LIMIT honestly: the reading pass claims L5 carries temporal
meaning by REFERENT (clouds are ephemeral), but the house referent miner is COLOUR-ONLY, so the
pipeline cannot see it. Scored honestly; what the instruments produce is reported, the limit is
reported as a limit, and no temporal signal is manufactured to match the reading.*

### THE ANSWER (measured) — **the referent-carried temporal is INVISIBLE to the instruments.**
The L5 temporal crossing is the **`(absent, absent)` NULL — NO CELL**. Both sides are temporal
ABSENT at every channel the pipeline computes, and the referent channel that would carry the
"clouds = ephemeral" reading **does not exist**:
- **zh L5 temporal WORD boolean = SILENT.** None of 浮/雲/遊/子/意 is a 爾雅釋天 calendrical char or
  carries a 日/夕 time radical (Kangxi 72/36), so `trait_labelers` zh temporal does not fire
  (`fires=False`, receipts `[]`). **雲 "cloud" is NOT a temporal word** — the ephemerality is a
  referent inference, not a lexical temporal charge.
- **zh L5 temporal WRITTEN = SILENT.** `written_row_line(...)["temporal"]` reports
  `carrier_present=False, fires_bool=False` — no HowNet head-sememe-123 temporal char on the line.
- **zh/en L5 temporal REFERENT = STRUCTURAL n/a (THE INSTRUMENT LIMIT).** `latent_score_54.referent_
  row_line` emits `field=='color'` ONLY (checked: L5 referent `field='color'`, trigger words `[]`).
  **There is NO temporal referent miner in the pipeline.** So the reading-pass's temporal reading
  has no channel to land in — this is the honest limit the board documents.
- **en L5 temporal WORD boolean = SILENT** ("cloud"/"floating"/"wide"/"Mind" are not HeidelTime
  temporal words). **en temporal WRITTEN = UNAVAILABLE** (no en temporal etymon; Skeat covers
  colour/dark only — `available=False`).
- **LaBSE temporal DETECTOR = no trigger.** temporal is a VALUE axis (two-sided) BUT its per-TOKEN
  cut is **None** (no adopted temporal token cut), so `triggered_tokens` is **EMPTY** on both sides
  (`[]`, `[]`) — not even a temporal token-ghost is possible. (temporal keeps a LINE scalar — zh L5
  reading −0.0482, en L5 −0.0395 — and a duration credential ρ.860, but neither makes a state.)
- Therefore **both sides resolve temporal SILENT → ABSENT**, and `CELL15` has no entry for
  (absent, absent) — the crossing is the null, not a state.

### THE DIRECT ANSWER (the task's point, verbatim intent)
The reading pass is right *as literary reading* — 浮雲/"floating cloud" does read as transience —
but that reading is **carried by the referent** (what clouds ARE), and **the house referent miner
is colour-only**, so the machine computes no temporal referent for any word. Combined with a silent
word tier, a silent/unavailable written tier, and a token-cut-None detector, the instruments
produce temporal ABSENT on both sides. The board reports the LIMIT as a limit — it does not invent a
temporal signal to match the reading pass. (This is the temporal analogue of the SOUND addendum's
honest null for the sound referent leg: the referent miner covers colour only.)

### word × channel → fires (the deliverable table; clouds carry NO word-tier temporal)
| word | word-tier temporal | temporal referent |
|---|---|---|
| **雲** (cloud, zh) | **False** (no 釋天 / 日夕-radical leg) | **n/a — miner colour-only** (the ephemerality is a referent inference, uncomputed) |
| 浮 遊 子 意 (zh) | False (no leg) | n/a — miner colour-only |
| **cloud** (Pound seat) | **False** (no HeidelTime hit) | n/a — miner colour-only |
| floating · wide · Mind · like (en) | False (no HeidelTime hit) | n/a — miner colour-only |

### THE CROSSING (under full law, `CELL15`)
- **Source (zh L5):** temporal `silent` (word/written/referent all silent; detector no-trigger) →
  `absent`.
- **Seat (Pound L5, a clean 1:1):** temporal `silent` (word silent; written unavailable; referent
  colour-only; detector no-trigger) → `absent`.
- **CELL = (absent, absent) = NO CELL** (the null; `linegrain_law_60.CELL15` has no
  (absent, absent) entry — not a state, not a crossing).

### CERTIFICATE (addendum discipline) — replay-VERIFIED
The encoder leg ran. **LaBSE re-order certificate drift = 0.00e+00** (< 1e-6 house law). The
addendum additionally **REPLAY-VERIFIED** it: the inventory was encoded a **second, independent
time** — second-run drift **0.00e+00**, max per-field reading disagreement between the two runs =
**0.00e+00**. **No drift.**

### ISOLATION (no-census-contamination, temporal addendum)
Adds only NEW files: `publishable/song_youren_exhibition_board_64_temporal.py` and, in the same
namespace, `reports/figures/song_youren_exhibition/song_youren_board_64_temporal.{json,md}` (the
`_temporal` suffixes). It **imports** the committed instruments read-only and writes/mutates none of
them; it does not touch any census file, the plant/sound boards' outputs, or the frozen 江上吟.
Structural isolation, same as the plant/sound boards.

### FILES (temporal addendum)
```
publishable/song_youren_exhibition_board_64_temporal.py    # the TEMPORAL-axis addendum scorer (REAL instruments, isolated)
reports/figures/song_youren_exhibition/
  song_youren_board_64_temporal.json / .md                 # per-word temporal channels + crossing + the instrument-limit finding
```

### RULING-GATED FOR HER (temporal addendum)
- **The (absent, absent) NULL verdict** (L5 temporal) is staked as measured under full law with live
  receipts. It is NOT a claim that the poem lacks temporal meaning — it is a claim that the CURRENT
  MACHINE cannot compute the referent-carried temporal reading, because the referent miner is
  colour-only. Hers to read.
- **The finding "the referent miner is colour-only, so referent-carried temporal is invisible"** is a
  clean methodology / limitations point (it names a concrete missing channel: a temporal referent
  miner). Whether to surface it in the paper's limitations, and whether to build a temporal referent
  miner, is the PI + the collaborator's call, NOT the board agent's.
