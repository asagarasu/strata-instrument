# Library acquisitions — harvest manifest (#51, 2026-07-19)
*Her acquisition, her sanction ("Ok for the OCRs"); acquisition-tier
guardrails apply (8e88f70): scans + transcriptions are LOCAL-ONLY,
untracked, outside this repo at
`<HOME>/garden/books/dnd2027/corpus/` (scans in
`pages/<book>/pNNN.pdf`, transcriptions in `transcriptions/`).
This manifest carries provenance + shas only — the repo never
distributes the texts. Pipeline: pdfseparate → Sonnet index-hunt
agents (6, parallel) → chair page-reads of located targets only.*

## Books received (6)
1. Watson, *Chinese Lyricism* (252pp scan)
2. Birrell, *New Songs from a Jade Terrace* (436pp)
3. Mathews (eds.), *The Flowers of Evil: A Selection*, New
   Directions 1958 pbk of 1955 translations — **the starred green
   book**, 19 translators, French facing (196pp)
4. 戴望舒译诗集, 湖南人民 1983 (诗苑译林; 恶之花掇英 = 1947 单行本
   as 卷二) (359pp)
5. 莎士比亚十四行诗, 梁宗岱 译, 四川文艺 1983 (162pp)
6. 莎士比亚十四行诗集, 屠岸 译, 上海文艺联合 **1955** 新一版
   (印数3000, 繁體直排, 每首附譯解) (370pp)

## Transcribed (9 poems; sha256 of transcription files)
| rendering | source pages | sha256[:16] |
|---|---|---|
| 梁宗岱 Sonnet 18 | 梁 p026 | 7fc055d2ef696439 |
| 梁宗岱 Sonnet 73 | 梁 p081 | 927c0d556da833ad |
| 屠岸 1955 Sonnet 18 | 屠 p044–p045 | 0171c0bb5d209810 |
| 屠岸 1955 Sonnet 73 | 屠 p154–p155 | 37e496febc2a6fe2 |
| 戴望舒 信天翁 (Albatros) | 戴 p138 | 456fbbe860ae9aea |
| 戴望舒 应和 (Correspondances) | 戴 p141 | 954ef701cf3f44f0 |
| Watson 青青河畔草 | Watson p037 | a3936729126add90 |
| Birrell 青青河畔草 | Birrell p067 | 24d282043d5dd968 |
| Birrell 飲馬長城窟行 (?Ts'ai Yung) | Birrell p075–p076 | 0a169946bd3516a7 |

## Second delivery, same day: the COMPLETE Mathews (her hunt, ~2h after the errand was named)
7. Mathews (eds.), *The Flowers of Evil*, New Directions **1955
   first printing** (LCCN 54-9871, no revision notice — not the
   1962), 488pp scan with binding blanks. Design fact: French is an
   APPENDIX, not facing ("It is not comparison that is to be
   avoided, but competition for the reader's attention" — p.viii).
   Both targets are **Richard Wilbur's**:
   | rendering | source pages | sha256[:16] |
   |---|---|---|
   | Wilbur, The Albatross | p042 (EN); French appendix p272 | ff44c97f3bd43307 |
   | Wilbur, Correspondences | p044 (EN); French appendix p273–274 | 6c02c818398ac246 |
   **Albatros-EN: 0 → 1 — the board's last zero falls.**
   Correspondances-EN: 2 PD → 3 in-hand. Field note filed in the
   transcription: Baudelaire's four-incense inventory survives 4/4
   in Dai, 3/4 in Wilbur (benjoin dropped, myrrh imported); 洞箫 vs
   "oboe" for hautbois. The night/light line: NOT an equivalence
   row — her correction 07-19. Baudelaire's one "vaste" → Wilbur
   compresses (one "Huge", order kept) vs Dai differentiates (广大
   /光明 · 浩漫/黑夜, two pole-tuned magnitudes, order swapped) —
   same salience, divergent VALUE structure; scalar-tier specimen,
   filed as contrast.

## Honest negatives (2)
- **Mathews *Selection* does NOT contain L'Albatros or
  Correspondances** — the 53-poem NDP-71 selection skips Spleen et
  Idéal II–V entirely (verified: contents + translator index +
  page-by-page pp.5–11). The targets live in the COMPLETE 163-poem
  New Directions 1955 bilingual edition — a different, larger book:
  sourcing errand for her list.
- **Watson does NOT translate our yinma** — only Ch'en Lin's
  same-title poem (飲馬長城窟,水寒傷馬骨), with an explicit note that
  the anonymous/蔡邕 青青河邊草 variant exists untranslated. The
  survey's recorded title-collision trap, demonstrated in print;
  Birrell's p076 carries BOTH poems on one page, same title.

## Findings that feed instruments/doctrine
- **屠岸 1955 Sonnet 18 REORDERS lines 9–10** vs the English
  (confirmed by the 也 in the printed line 10) — live specimen for
  the R2 alignment spec (translator reordering within a quatrain).
- **Birrell reads 宿昔 as "In bed at night"** (night reading) where
  Marker K's relayed text carries 夙昔 (long-ago) — the variant
  diverges exactly at the poem's hinge; flag for the marking sheets.
- 屠岸 73 glyph RESOLVED: 灰燼 both occurrences (lines 10–11),
  verified by the PI's direct page read 2026-07-19; transcription clean
  for scoring use.
- Birrell renders 皎皎 as "White, white" (illumination→color);
  Watson as "bright bright" — a ready-made illumination-row
  contrast between the two EN renderings of the same line.

## Ensemble depth movement (vs survey baseline 035a312/2f82856)
- Sonnet 18 zh: 1 → **3** (wiki-CC · 梁 · 屠1955)
- Sonnet 73 zh: **0 → 2** (梁 · 屠1955) — the honest wall now has
  research-tier renderings (PD status unchanged: none are PD; her
  three-gate ruling governs use-tier)
- yinma EN: **0 → 1** (Birrell) — wall broken, research-tier
- qingqing EN: 2 → 4 (＋Watson, Birrell)
- Albatros zh / Correspondances zh: +1 each (戴 1947-via-1983)
- Albatros EN: still 0 PD, 0 in-hand (Mathews negative above)
All still below the ~10/source the equating architecture wants;
her three-gate sourcing ruling remains the R2 gate.

## Deliveries 2–3 transcribed (sha256 manifest completion, #51 audit at her ask)
| rendering | sha256[:16] |
|---|---|
| owen_norton/qingqing_hepan_cao.md | b05e425572a63eea |
| owen_norton/song_youren.md | 5211291a20c8afee |
| owen_norton/yinma_changcheng.md | 5bf60a0446c4b02a |
| watson_columbia/song_youren.md | bf1dc96bcb9d1613 |
| campbell/albatross.md | 6dac4ae7a5fa4d6c |
| campbell/correspondences.md | 8b9844a90eea72e3 |
| aggeler/albatross.md | 7be667beb966c056 |
| aggeler/correspondences.md | 73dbebf76f9f3330 |
| dillon_millay/albatross_dillon.md | b6aeeb43614e5222 |
| dillon_millay/correspondences_dillon.md | 64d164fe0b137dce |
| liang_shiqiu/sonnet_18.md | 6b8d30875671a441 |
| liang_shiqiu/sonnet_73.md | 12608db75a02be2d |
| gu_zhengkun/sonnet_18.md | 7f22876343497a7e |
| gu_zhengkun/sonnet_73.md | f1a5d7b1178ce743 |
| qian_chunqi/ganying_correspondances.md | 9395e0db4cb699a4 |
| qian_chunqi/xintianweng.md | e2a9225c7d0493fd |
| guo_hongan/xintianweng.md | 6a66b39655f20d3f |
| guo_hongan/yinghe_correspondances.md | 5b5387695480a74a |
| xu_yuanchong/qingqing_hepan_cao.md | fbac94e3551f2ea3 |
| debon/song_youren.md | 25794b35e5dab03b |
| kraus/sonnet_18.md | 169fa434ee915609 |
| kraus/sonnet_73.md | 69fd9e3045f894bf |
