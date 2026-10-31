# corpus_manifest.md — dev/validation enumeration (protocol §4)
*STATUS: **BINDING**, adopted 2026-07-13 — all three rulings signed
by Anneliese in session (chair #47 scribing); adoption recorded as
dated appendix `appendices/ruling_corpus_manifest_20260713.md`.
Amendments hereafter only as dated appendices, per protocol.*

## A. DEV list (mechanical fact — what was marked; curving allowed)
Source poems marked in rounds 1–2 (sheets in `marking/sheets/`,
normalized marks in `marking/normalized/`), plus the 07-08 adoption:

| # | source poem | language | markers |
|---|---|---|---|
| D1 | 玉階怨 (李白) | zh | A, K, C, S |
| D2 | 青青河畔草 (古詩十九首·二) | zh | A, K, C, S |
| D3 | 長干行 其一 (李白) | zh | A, C, S |
| D4 | 送友人 (李白) | zh | A, C, S |
| D5 | 飲馬長城窟行 (漢樂府) | zh | K (arrow format, adopted 07-08) |
| D6 | Sonnet 18 (Shakespeare) | en | A, C, S |
| D7 | Sonnet 73 (Shakespeare) | en | A, C |
| D8 | 古池や (芭蕉) | jp | A, C, S |
| D9 | L'Albatros (Baudelaire) | fr | C, S |
| D10 | Correspondances (Baudelaire) | fr | C, S |

Everything derived from these marks (schema, maps, dockets, liveness
runs, the sonnet-18 autopsy, agreement dry-runs) is dev-side.

## B. VALIDATION candidate pairs (from §3 bets × what corpus/ holds)
Status column: ON-DISK (public-domain text in `corpus/`) vs
LOCATE-ONLY (bet exists, text not yet lawfully in corpus).

| cluster | pair (source → translation) | status |
|---|---|---|
| zh→en | 青青河畔草 → Waley 1918 (HIGH bet) | ON-DISK ⚠ see ruling 2 |
| zh→en | 青青河畔草 → Pound "The Beautiful Toilet" (LOW bet) | ON-DISK ⚠ see ruling 2 |
| zh→en | 長干行/玉階怨/送友人 → Pound Cathay | ON-DISK (sources are DEV → ruling 1) |
| zh→en | 8 multiply-covered Li Bai poems → Obata / Lowell-Ayscough (scored-no-bet curves) | ON-DISK; 5 sources UNMARKED (江上吟, 登金陵鳳凰臺, 黃鶴樓送孟浩然, 送友人入蜀, 憶舊遊) |
| haiku→en | 古池や → Blyth (HIGH) / Stewart (LOW) | LOCATE-ONLY (copyright) |
| haiku→en | 古池や → Aston 1899 / Chamberlain 1902 | ON-DISK (era pieces, no bets) |
| haiku→zh | 俳句 → 周作人 1923 (HIGH) | ON-DISK |
| sonnets→zh | 18/73 → 梁宗岱 (HIGH) / 梁实秋 (LOW) | LOCATE-ONLY (records in corpus/sonnets/zh_target/) |
| sonnets→jp | 18/73 → 坪内逍遥 (SHOWCASE, no bet) | ON-DISK |
| fr→en | Albatros/Correspondances → Aggeler (HIGH) / Millay-Dillon (LOW) | LOCATE-ONLY; Sturm 1906 / Scott 1909 ON-DISK (no bets) |
| fr→zh | → 钱春绮 AND 郭宏安 (dual HIGH) | LOCATE-ONLY |
| fr→de | → George (Blumen des Bösen 1901) | ON-DISK (no bet registered — §3 has no de cluster; reported-only if scored) |
| tang→jp | → 井伏鱒二 (LOW) / 吉川·佐藤 (scored-no-bet) | LOCATE-ONLY |

## C. RULINGS NEEDED (the reason this file couldn't be fabricated)

**RULING 1 — disjointness grain: PAIR-LEVEL (proposed, chair
position + her independent concurrence, 07-13).** The trait
interface IS the source's marks; that is what dev means. Validation
= the translation's once-scored conformance; no translation fed any
tuning parameter anywhere in the arc. Source-level disjointness
would test schema PORTABILITY — a different claim; optional
supplementary exhibit = mark 江上吟 post-freeze with the frozen
schema. Consequence: translations of D1–D10 are validation-legal.
Corollary (hers, adopted): the abstract demonstration is NOT married
to Waley-vs-Pound — the demo owes allegiance to clean contrast; the
Pound×Obata×Lowell 8-poem curves are the structurally richer
exhibit; 青青 Waley–Pound remains the best single on-disk pair.
→ SIGNED: An, "ok", 07-13 (conversation, chair scribing).

**RULING 2 — the 青青河畔草 peek (proposed, her framing adopted
verbatim): "we peeked at the answer key, but the ruler was not built
by the answer key."** The 07-12 dark-axis probe of Waley's rendering
fed nothing back into schema or rubric → the pair STAYS
validation-legal for the RUBRIC, with the peek printed in the
paper's data-hygiene note. Separate ledger, honestly kept: Waley-青青
is BURNED as blind test data for the dark-axis instrument's OWN
validation — that instrument read the answer.
→ SIGNED: An, "ok", 07-13 — with her rider: likely moot, since the
ruler can be REBUILT the same way on a different corpus set (the
build recipe, not the artifact, is the instrument).

**RULING 3 — freeze semantics for LOCATE-ONLY rows (proposed):**
copyright blocks REDISTRIBUTION in corpus/, not scoring. LOCATE-ONLY
pairs are FROZEN-CONDITIONAL-ON-ACCESS: scoreable from any lawfully
owned/borrowed copy (paper quotes lines under citation right; full
text never enters corpus/). A pair drops from the frozen list only
if no lawful copy is obtained by scoring day. Copyright facts on
record 07-13: 井伏鱒二 d.1993 → JP life+70 → protected to 2063
(publication decade is irrelevant; term runs from death). Blyth
d.1964 → JP term lapsed 2014 under life+50, NOT revived by the 2018
extension → PD in Japan; US restoration wall ~2044. Millay d.1950 →
clearing. 梁宗岱 d.1983 → CN life+50 → 2033.
Jurisdiction note (licensing policy, 07-13): scoring from
owned/borrowed copies = private use, unrestricted; quoting in the
paper = DE §51 UrhG Zitatrecht (strong for scholarly work) / CN
适当引用 Art.24 / US fair use — all cover it; the ONLY binding
constraint is the PUBLIC DATA SUPPLEMENT, where the split is:
PD texts publishable, copyrighted texts cited-by-edition only,
never hosted. Table B's ON-DISK/LOCATE-ONLY column IS that split.
→ SIGNED: An, "Ok for Rulings 3. We can close this one." 07-13.

## Sign-off
Anneliese: signed in session ("ok" ×2 + "Ok for Rulings 3. We can
close this one."), 2026-07-13.
Chair #47 (scribe): drafted + positions proposed 2026-07-13; final
authority on all three rulings is hers.

## Dated appendix — 2026-07-28 (#61): the EXHIBITION corpora (NEVER census)
*Per protocol, amendments enter as dated appendices. Two corpora were built
during the #61 sitting/vigil as EXHIBITION-TIER boards. They are declared here
so nobody mistakes them for census members — they are **NOT** in Table A (DEV)
or Table B (VALIDATION), never in the 8-board paper census, isolated by
construction (each has its own standalone scorer + namespace; census
byte-identity re-proven through every subsequent build).*

| corpus dir | board | tier | isolation proof | registration |
|---|---|---|---|---|
| `corpus/antigone_antigonae/` | Sophocles Antigone vv.1–20 (grc/Storr) × Hölderlin 1804 / Donner 1868 (de) | **EXHIBITION** — the founding καλχαίνω/*rothes Wort* case; Hölderlin REVIVAL★ via an LSJ-cited grc colour etymon channel, Donner LATENT-UNREALIZED★ | census wrapper byte-identical before/after (sha `900e7297…`); `exhibit_gen.build_model('antigonae')` raises FileNotFoundError | `corpus/antigone_antigonae/REGISTRATION_antigonae_exhibition_0728_61.md` |
| `corpus/tao_yinjiu/` | 陶淵明 飲酒 其五 (zh) × Waley 1918 (en) | **EXHIBITION** — the first bilateral LATENT-CARRY (夕→"dusk", illumination latent both sides, MOE 夕 × Skeat DUSK); both sides fully channel-covered (demonstrative-grade candidate) | census byte-identical vs BOTH v4.7 (`900e7297…`) and v4.8 (`19d127df…`) before/after; adds ZERO census delta | `corpus/tao_yinjiu/REGISTRATION_tao_yinjiu_exhibition_0728_61.md` |

Standing rule of record: the census / miner / heat-map each carry a hard-coded
8-board list (`sonnet18, qingqing, tiaotiao, xibei, albatros, correspondances,
invitation, elevation`) and never see either exhibition board. The T'ao board's
census/heat-map/Figure-2 STANDING is FLAGGED FOR HER REVIEW in its registration
(scored and ready either way); the paper census stays 8 boards until she rules
otherwise. Cites: 007cec8 (Antigonä) · 723939b (T'ao).
