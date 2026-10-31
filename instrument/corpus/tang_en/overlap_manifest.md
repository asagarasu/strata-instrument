# Overlap manifest: Pound's *Cathay* (1915) vs. Waley's *A Hundred and Seventy Chinese Poems* (1918) and *More Translations from the Chinese* (1919)

Compiled 2026-07-05. Raw gathering and cross-checking only — no passage
selection performed. All claims below were established by reading the
full fetched texts (not by relying on secondary-source lists of "known
overlaps"), per the task brief.

## Files in raw/

| File | Source | URL | Fetch date |
|---|---|---|---|
| `raw/pound_cathay_1915.txt` (+ `_raw.html`) | Ezra Pound, *Cathay* (London: Elkin Mathews, 1915) | https://www.gutenberg.org/files/50155/50155-h/50155-h.htm (PG #50155) | 2026-07-05 |
| `raw/waley_170chinese_1918.txt` (+ `_raw.html`) | Arthur Waley, *A Hundred and Seventy Chinese Poems* (London: Constable, 1918) | https://www.gutenberg.org/files/42290/42290-h/42290-h.htm (PG #42290) | 2026-07-05 |
| `raw/waley_moretranslations_1919.txt` (+ `_raw.html`) | Arthur Waley, *More Translations from the Chinese* (New York: Knopf, 1919) | https://www.gutenberg.org/files/16500/16500-h/16500-h.htm (PG #16500) | 2026-07-05 |
| `zh_source/gushi19shou_02_qingqing_hepan_cao.txt` | 古詩十九首 (Nineteen Old Poems), poem #2, anonymous, Han dynasty | https://zh.wikisource.org/wiki/古詩十九首 | 2026-07-05 |

All three English-language `.txt` files are plain-text conversions
(via `pandoc -f html -t plain`) of the Project Gutenberg HTML editions,
which are themselves saved unmodified as the companion `_raw.html`
files for provenance. No wording was altered in conversion, only HTML
markup stripped.

## IMPORTANT — result differs from the task brief's working assumption

The brief's example list of "known overlaps" (长干行/"The River-Merchant's
Wife", 玉阶怨/"The Jewel Stairs' Grievance", 送友人/"Taking Leave of a
Friend") does **not hold** for these two specific Waley volumes. I
checked every Li Bai (Rihaku) poem in *Cathay* against the full text of
both Waley books — by title and, more importantly, by content/proper
nouns/imagery, since Pound and Waley use different Romanizations and
sometimes different English titles for the same Chinese poem — and
found only **one** genuine shared source poem. Waley states explicitly
in his preliminary note to *170 Chinese Poems*: "In making this book I
have tried to avoid poems which have been translated before" — and his
Appendix note in *More Translations* ("Of the eight poems by Li Po, all
but Number 6 have been translated before") confirms he was consciously
steering around already-translated Li Bai material, which as of
1918–19 effectively meant Cathay's most famous pieces. Neither Waley
volume ever names Pound, Fenollosa, or Cathay directly (checked by
full-text search).

## Established overlap (1)

| Chinese source | Pound (*Cathay*) | Waley | Caveats |
|---|---|---|---|
| 古詩十九首 其二「青青河畔草」("Nineteen Old Poems," #2, anonymous Han-dynasty; sometimes attributed to Mei Sheng 枚乘, d. 140 BC) | **"The Beautiful Toilet"** — `raw/pound_cathay_1915.txt`, line 79 (poem body lines 80–89). Pound's byline reads "By Mei Sheng. B.C. 140." | Untitled poem **(2)** of the "Seventeen Old Poems" section — `raw/waley_170chinese_1918.txt`, line 1309 (section head "SEVENTEEN OLD POEMS") / line 1348 (poem 2 itself, "Green, green, / The grass by the river-bank..."). Waley's headnote says "Some have been attributed to Mei Shēng (first century B.C.)" — note the different attributed century vs. Pound's caption. | (a) Pound's version derives from Ernest Fenollosa's notebooks, filtered through the (partly erroneous) glosses of Japanese scholars Mori and Ariga — Pound did not read Chinese and worked from Fenollosa's transliterations/cribs of a Japanese kanbun reading tradition, not directly from the Chinese. Waley worked directly from the Chinese. (b) Attribution discrepancy: Pound's caption dates the poem "B.C. 140" (i.e., to Mei Sheng definitively); Waley is more guarded, calling the attribution traditional/uncertain and noting the 19 poems are "manifestly not all by the same hand." (c) Waley does not title the poem; Pound's title "The Beautiful Toilet" is his own invention, not a rendering of a Chinese title (the source has no title beyond its incipit). (d) This overlap is independently noted in secondary scholarship comparing the two translators' handling of 盈盈 ("ying ying") — Waley renders it "sad, sad," which commentators flag as a mistranslation (the term describes graceful bearing, not sadness). |

Chinese source text saved at
`zh_source/gushi19shou_02_qingqing_hepan_cao.txt`.

## Cathay poems checked against both Waley volumes and found to have NO Waley counterpart

For completeness (and to support future researchers who might otherwise
assume the popularly-cited overlaps exist), here is the full poem list
of *Cathay*'s Chinese-derived poems (i.e., excluding "The Seafarer,"
which is an Anglo-Saxon poem included as a pendant, not a Chinese
translation), with the line where each starts in
`raw/pound_cathay_1915.txt`, and confirmation that no matching content
appears in either Waley volume:

| Cathay poem | Line in raw file | Underlying Chinese poem (as identifiable) | Found in Waley (170 / More Translations)? |
|---|---|---|---|
| Song of the Bowmen of Shu | 45 | 詩經·小雅·采薇 (Shijing/Book of Songs — pre-Han, not Li Bai) | No — neither Waley volume includes any Book of Songs material. |
| The Beautiful Toilet | 79 | 古詩十九首 其二 | **Yes — see overlap table above.** |
| The River Song | 92 | 李白, 江上吟 (attrib.) | No — searched for proper nouns unique to this poem (Kutsu/Qu Yuan, King So/King of Chu, shato-wood boat) in both Waley volumes; no match. |
| The River-Merchant's Wife: a Letter | 149 | 李白, 長干行 (Chang Gan xing) | No — searched "merchant," "Chokan," "Ku-to-Yen," "Cho-fu-Sa" in both Waley volumes; no match. Waley never translates 長干行 in either book. |
| The Jewel Stairs' Grievance | 183 | 李白, 玉階怨 (Yu jie yuan) | No — searched "jewel," "stairs," "steps," "dew," "gauze," "crystal curtain" throughout both Waley volumes; several unrelated hits, none matching this poem's content. Waley never translates 玉階怨 in either book. |
| Lament of the Frontier Guard | 237 | Likely 李白, 古風 (Ancient Airs) no. 14, "胡關饒風沙" (tentative identification — mentions general Li Mu 李牧/"Rihoku") | No — Waley's *170 Chinese Poems* does contain a differently-authored poem with a similar title, "Fighting South of the Castle" (an anonymous Han-dynasty yuefu, circa 124 BC, at line ~1117 of `raw/waley_170chinese_1918.txt`), but its content (crows eating corpses, unburied dead) is entirely different from Pound's poem (Rihoku, the North Gate, barbarian kings) — **title resemblance only, not a real overlap; flagged so it isn't mistaken for one.** |
| Exile's Letter | 265 | 李白, 憶舊遊寄譙郡元參軍 (tentative) | No match found for "So-Kin," "Rakuyo," or other proper nouns. |
| Separation on the River Kiang | 479 | 李白, 黃鶴樓送孟浩然之廣陵 (tentative) | No. |
| Taking Leave of a Friend | 485 | 李白, 送友人 (Song you ren) | No — searched "neigh," "floating cloud," "sunset," "clasped hands" in both Waley volumes; no match. Waley never translates 送友人 in either book. |
| [untitled, "Sanso, King of Shoku, built roads..."] | ~492 | 李白, 蜀道難 (tentative, partial) or a related road-to-Shu poem | No. |
| The City of Choan | 508 | 李白, 登金陵鳳凰臺 (Deng Jinling Fenghuang Tai) | No — searched "phoenix" throughout both Waley volumes; no hits at all. |
| South-Folk in Cold Country | 522 | 李白, 古風 or border-themed yuefu (tentative) | No — searched "Dai horse," "Etsu," "En," "Wild-Goose gate," "Rishogu" — no hits. |

Tentative Chinese-source identifications above (marked "tentative") are
my own working attributions based on content/proper-noun matching
against standard knowledge of the Li Bai corpus — they have **not**
been independently verified against a critical edition and should be
re-checked before being relied on for anything beyond locating Chinese
source text for the one confirmed overlap. Because these poems have no
Waley counterpart in the two specified volumes, I did not fetch
Chinese-source originals for them (task scope: "For each overlap poem,
fetch the Chinese source text" — only one overlap poem was established).

## Gaps / caveats for the record

1. **Only one overlap established**, not the three-plus implied by the
   task brief's example list. This is a real finding, not a shortfall
   in search effort — see full-text search methodology above (title
   search + proper-noun/content search across both complete Waley
   volumes for every Cathay poem).
2. If the research goal specifically wants Waley vs. Pound on 長干行,
   玉階怨, or 送友人, that requires a **different, later Waley source**
   (e.g., material in *The Poetry and Career of Li Po* or later
   anthologies), which is outside the two volumes named in the brief
   and whose public-domain status would need separate verification
   (Waley died 1966; anything past the 1918/1919 volumes may still be
   under copyright in some jurisdictions depending on publication
   date). Not fetched — flagging rather than substituting a dubious
   source, per instructions.
3. The Pound/Fenollosa provenance caveat applies to *every* Cathay
   poem, not just the overlap poem: Pound worked from Ernest
   Fenollosa's notebooks (themselves based on lectures by Japanese
   scholars Mori Kainan and Ariga Nagao reading the Chinese in kanbun
   /Japanese-inflected fashion), not from the Chinese text directly.
   This is stated in Cathay's own subtitle/headnote ("FOR THE MOST PART
   FROM THE CHINESE OF RIHAKU, FROM THE NOTES OF THE LATE ERNEST
   FENOLLOSA, AND THE DECIPHERINGS OF THE PROFESSORS MORI AND ARIGA" —
   `raw/pound_cathay_1915.txt` lines 9–13).
4. "Rihaku" (Pound/Fenollosa's Japanese on-reading of 李白's name) =
   Li Bai = Li Po (Waley's Wade-Giles rendering). Same poet, three
   names across the corpus — noted here to avoid confusion when
   searching raw files.
5. The Chinese source text fetched (`zh_source/gushi19shou_02_qingqing_hepan_cao.txt`)
   was cross-checked against a second independent web source (a
   general search aggregating ctext.org-adjacent results) and found to
   match exactly; only the Wikisource copy was saved as the citable
   file since it's the more stable/citable public-domain repository
   page for this text.
6. Did not attempt to fetch a Chinese source for "The Seafarer" since
   it is an Old English poem (not Chinese) included in Cathay as an
   acknowledged pendant piece, not a translation.

---

## ADDENDUM — 2026-07-05 (later same day): Obata (1922) and Lowell/Ayscough
## (1921) added; the brief's expected overlaps DO exist after all, just not
## in the two Waley volumes

This addendum extends the search beyond the two Waley volumes above to two
additional public-domain Li Bai/Li Po translators, per a follow-on task.
It resolves Gap #2 noted above: the task brief's example overlaps (長干行,
玉階怨, 送友人) turn out to be real — they just needed a different
translator than the two specific Waley volumes on hand.

### New files in raw/

| File | Source | URL | Fetch date |
|---|---|---|---|
| `raw/obata_worksoflipo_1922_raw.txt` | Unmodified OCR download (no header) | https://archive.org/download/workslipochines00conggoog/workslipochines00conggoog_djvu.txt | 2026-07-05 |
| `raw/obata_worksoflipo_1922.txt` | Shigeyoshi Obata, *The Works of Li Po, the Chinese Poet* (New York: E. P. Dutton & Company, 1922) — same OCR text as above with a prepended provenance header (see header text in the file itself for full detail, including a documented OCR-garble/cross-check note on poem No. 18) | https://archive.org/details/workslipochines00conggoog (Google Books scan of the University of Virginia Library's copy of the original edition) | 2026-07-05 |
| `raw/firflower_ayscough_lowell_1921_raw.html` | Unmodified HTML download | https://www.gutenberg.org/files/48222/48222-h/48222-h.htm (PG #48222) | 2026-07-05 |
| `raw/firflower_ayscough_lowell_1921.txt` | Florence Ayscough & Amy Lowell, *Fir-Flower Tablets: Poems Translated from the Chinese* (Boston/New York: Houghton Mifflin, 1921) — `pandoc -f html -t plain` conversion of the above, with a prepended provenance header; no wording altered | https://www.gutenberg.org/files/48222/48222-h/48222-h.htm | 2026-07-05 |

**Public domain status, both confirmed:**
- Obata: copyright page reads "Copyright, 1922, BY E. P. DUTTON & COMPANY" —
  first published in the US in 1922, pre-1929, public domain in the US.
  (Cross-checked against a second scan — the London & Toronto: J. M. Dent
  & Sons, "MCMXXIII" [1923] reprint edition, Internet Archive item
  `worksoflipochine00libauoft` — same text, same 1922 preface date; used
  only to correct one OCR-garbled line in the primary copy, per the note
  in `raw/obata_worksoflipo_1922.txt`'s header.)
- Ayscough/Lowell: copyright page reads "COPYRIGHT, 1921, BY FLORENCE
  AYSCOUGH AND AMY LOWELL" — pre-1929 US publication, public domain in
  the US, and already hosted as a completed Project Gutenberg edition
  (PG #48222), which independently confirms PG's own clearance process
  found it public domain.

### Method: how the overlaps below were found

Obata's book itself contains an extensive bibliographic concordance (an
appendix, roughly `raw/obata_worksoflipo_1922.txt` lines 9950–10500)
in which Obata cross-references each of his 124 numbered poems against
prior translations by Pound, Waley, Lowell, Giles, Cranmer-Byng, and
several French/German translators (St. Denys, Toussaint, Florenz,
Bernhardi, Gautier, Forke, Bethge, Edkins). This concordance was used as
the primary index to identify overlaps, then every claimed overlap was
independently verified by reading the actual poem text in both books (not
just trusting Obata's title-matching) — same discipline as the original
manifest above. Fir-Flower Tablets does not contain an equivalent index,
so its coverage was checked both via Obata's concordance entries (which
cite Lowell by title) and via direct full-text search of
`raw/firflower_ayscough_lowell_1921.txt` for proper nouns/imagery, exactly
as was done for the two Waley volumes above.

### Established overlaps: Cathay × Obata × Lowell/Ayscough

**Triple overlaps (all three of Pound, Obata, and Lowell/Ayscough):**

| Chinese source (zh_source file) | Pound (*Cathay*) | Obata (*Works of Li Po*, 1922) | Lowell/Ayscough (*Fir-Flower Tablets*, 1921) |
|---|---|---|---|
| 江上吟 — `li_bai_jiangshang_yin.txt` | "The River Song" — `raw/pound_cathay_1915.txt` line 92 | "On the Ship of Spice-wood," poem No. 1 — `raw/obata_worksoflipo_1922.txt` line 2278 | "River Chant" — `raw/firflower_ayscough_lowell_1921.txt` line 3663 |
| 長干行 其一 — `li_bai_changgan_xing.txt` | "The River-Merchant's Wife: A Letter" — line 149 | "Two Letters from Chang-kan — I" (and Obata also did 其二 as "— II"), poems No. 105/106 — lines 7036 / 7150 | "Ch'ang Kan" — line 3150 |
| 玉階怨 — `li_bai_yujie_yuan.txt` | "The Jewel Stair's Grievance" — line 183 | "The Sorrow of the Jewel Staircase," poem No. 18 — line 3062 | **Not present** — see "double overlaps" below; listed here only because Obata's concordance entry for this poem cites no Lowell title, which I independently confirmed by full-text search |
| 送友人 — `li_bai_song_you_ren.txt` | "Taking Leave of a Friend" — line 485 | "Taking Leave of a Friend," poem No. 60 — line 4776 | "Saying Good-Bye to a Friend" — line 3891 |
| 登金陵鳳凰臺 — `li_bai_deng_jinling_fenghuang_tai.txt` | "The City of Choan" (Cho-An) — line 508 | "The Phoenix Bird Tower," poem No. 76 — line 5584 | "Fêng Huang T'ai" (subtitled "Ascending the Terrace of the Silver-Crested Love-Pheasants...") — line 2922 |
| 黃鶴樓送孟浩然之廣陵 — `li_bai_huanghelou_song_menghaoran.txt` | "Separation on the River Kiang" — line 479 | "On Seeing off Meng Hao-jan," poem No. 40 — line 3707 | "At the Yellow Crane Tower, Taking Leave of Mêng Hao Jan on His Departure to Kuang Ling" — line 5065 |

Correction to the original manifest above: 玉階怨 is **not** a triple
overlap — I've left it in this table with a note rather than a separate
one because Obata's own concordance is what first suggested checking it,
and it's important precisely because it's the poem the task brief named
by title. Full-text search of `firflower_ayscough_lowell_1921.txt` for
"jewel," "staircase," "steps," "dew," "crystal curtain" (all
image-vocabulary from this poem) returned no matching content — Lowell
and Ayscough did not translate this poem. It is a genuine **double**
overlap (Pound + Obata only) — see next table.

**Double overlaps (Pound + Obata only; Lowell/Ayscough checked and absent):**

| Chinese source (zh_source file) | Pound (*Cathay*) | Obata (*Works of Li Po*, 1922) |
|---|---|---|
| 玉階怨 — `li_bai_yujie_yuan.txt` | "The Jewel Stair's Grievance" — line 183 | "The Sorrow of the Jewel Staircase," poem No. 18 — line 3062 |
| 送友人入蜀 — `li_bai_song_youren_ru_shu.txt` | "Leave-taking near Shoku" — line 495 | "To His Friend Departing for Shuh," poem No. 10 — line 2678 |
| 憶舊遊寄譙郡元參軍 — `li_bai_yijiuyou_ji_qiaojun_yuan_canjun.txt` | "Exile's Letter" — line 265 | "To Tung Tsao-chiu," poem No. 59 — line 4528 |

For "Leave-taking near Shoku": the original manifest above (see table in
the first section) had listed this Cathay poem only tentatively as
"[untitled, 'Sanso, King of Shoku, built roads...']" without confirming
its actual title. Re-checking `raw/pound_cathay_1915.txt` line 495
confirms the real title is "Leave-taking near Shoku"; Obata's concordance
(which explicitly cross-references "Pound, Cathay. Leave-taking near
Shuh") independently corroborates the Chinese-source identification as
送友人入蜀.

**Cathay poems checked again and still confirmed to have NO counterpart
in Obata or Lowell/Ayscough** (in addition to Waley, per the original
table above): "Song of the Bowmen of Shu" (not Li Bai — Book of Songs;
neither Obata nor Lowell/Ayscough translate Book of Songs material in
these volumes), "Lament of the Frontier Guard," and "South-Folk in Cold
Country" — checked via Obata's full concordance (no "Pound, Cathay" entry
for either) and via direct full-text search of both new raw files for
proper nouns/imagery ("Li Mu," "Rihoku," "North Gate," "wild-goose gate,"
"Dai horse," "Etsu," "En," "Rishogu") with no matches beyond generic
wild-goose-letter imagery unrelated to the specific frontier place-names
sought.

### New files in zh_source/

Per instructions, Chinese source text was fetched for every poem now
covered by 2+ translators — this is all eight poems in both tables above
(the five triple overlaps, plus the three double overlaps, since "2+"
includes Pound+Obata pairs even without Lowell). All eight were fetched
from Chinese Wikisource using the MediaWiki raw wikitext endpoint
(`?action=raw`) rather than rendered HTML, specifically to get exact
characters without an intermediate summarization/OCR step:

| File | Chinese title | Fetch date |
|---|---|---|
| `li_bai_song_you_ren.txt` | 送友人 | 2026-07-05 |
| `li_bai_changgan_xing.txt` | 長干行二首 (both 其一 and 其二) | 2026-07-05 |
| `li_bai_yujie_yuan.txt` | 玉階怨 | 2026-07-05 |
| `li_bai_jiangshang_yin.txt` | 江上吟 | 2026-07-05 |
| `li_bai_deng_jinling_fenghuang_tai.txt` | 登金陵鳳凰臺 | 2026-07-05 |
| `li_bai_huanghelou_song_menghaoran.txt` | 黃鶴樓送孟浩然之廣陵 | 2026-07-05 |
| `li_bai_song_youren_ru_shu.txt` | 送友人入蜀 | 2026-07-05 |
| `li_bai_yijiuyou_ji_qiaojun_yuan_canjun.txt` | 憶舊遊寄譙郡元參軍 | 2026-07-05 |

Each file documents its own provenance, PD status, and — where relevant —
in-text variant-reading annotations found in the Wikisource source markup
(e.g., 長干行 其二's disputed authorship note; 黃鶴樓送孟浩然之廣陵's
recorded manuscript variants in line 3) and cross-references to which
English translations it underlies, with exact line numbers in the raw/
files. `li_bai_changgan_xing.txt` also records that Chinese Wikisource's
own page for 長干行 其一 links directly to English Wikisource's "The
River Merchant's Wife: A Letter," an independent corroboration of that
identification from a third source.

### Reputation verification

Reputation findings for Obata and for Ayscough/Lowell (documented
citations, not a HIGH/LOW classification) are written up separately in
`<LAB>/obata_lowell_reputation_report.md`,
per the task's instruction to keep that as its own file. Short version:
evidence is genuinely thin on both — a real contemporaneous peer review
(Giles & Blackman, *JRAS* 1924) and at least two modern academic articles
(Yan Liu 2010; Eugene Chen Eoyang 2014/2019) exist and are cited there,
but several were paywalled and I could not verify their actual verdicts,
which the report states plainly rather than guessing at. See that file
for full citations and the honesty caveats.

### Gaps / caveats for this addendum

1. I could not access the actual text of the 1924 JRAS review or the 2010
   Comparative Literature: East & West article — cited in the reputation
   report as leads, not as verified content.
2. Obata also translated 其二 of 長干行 (which Pound did not touch at
   all — Pound's "River-Merchant's Wife" only covers 其一); this is noted
   in `zh_source/li_bai_changgan_xing.txt` for completeness but doesn't
   change the overlap count since Pound has no counterpart to 其二.
3. Did not attempt a systematic re-check of the *entire* Fir-Flower
   Tablets table of contents against Obata's non-Cathay poems (over 100
   further Li Bai poems in each book) — scope was Cathay-poem overlaps
   specifically, per the task brief. A fuller Obata-vs-Lowell overlap
   study (independent of Cathay) would be a separate undertaking.
4. As with the Waley section above, "Rihaku"/"Li Bai"/"Li Po"/"Li
   T'ai-po" are all the same poet under different translators'
   Romanization conventions — noted again here since this section adds
   yet another spelling ("Li T'ai-po," Lowell/Ayscough's preferred form).
