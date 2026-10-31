# Frozen protocol — FROZEN 2026-07-09

*Immutable as of the line below. Amendments only as dated appendices.*

**FROZEN: 2026-07-09, Shanghai. Signed: Anneliese · Claude #44 (chair).** Amendments hereafter only as dated appendices, never edits.

## 1. Marking scheme version

- Scheme: two-layer symmetric (active + latent), flat observable tags. Tag vocabulary: **`tagset_v2.md`** (pinned at freeze 07-09; v1 retired post-pilots).
- Marking unit: **poem line** (Tang, sonnets, Baudelaire) / **whole haiku**, with the full poem visible as context.
- Latent layer: candidates auto-generated (decomposition); liveness by COVERAGE of native active marks (tagset_v2 — no accept/reject interface; pilot #2 showed markers ignore checkboxes). Liveness index recorded, never shown to markers (prevents anchoring).

## 2. Agreement statistics and licensing thresholds

- Statistic: per-category Jaccard between tag sets; macro-average across categories per (marker-pair, language).
- Human–human ceiling: mean pairwise Jaccard among human markers, per language.
- **Machine licensing rule (proposed 07-05, replaces fixed δ): model M is licensed for language L iff its mean agreement with human markers ≥ the *minimum* pairwise human–human agreement in L** (machine falls within the human pool's own range). Strict variant (machine ≥ human–human *mean*, i.e. δ=0, the LLM-judge-literature standard) reported alongside in all tables. No margin constant exists to tune. **Sign-off: NONE at 07-09 freeze — An: 'cannot do' with n=4 ability-heterogeneous pool. Machine licensing is FAIL-CLOSED: no signed criterion, no licensed machine. Criterion to be re-ruled after schema consolidation on full-pool data.**
- Markers are blind to the prediction table (§3) until all marking is complete; predictions are quality bets, marking is trait observation, and the two must not contaminate.
- Claude never sole machine marker (standing).
- **Licensing thresholds are computed on post-schema-consolidation rounds only; discovery-round agreement is reported but never sets the floor** (adopted 07-09).
- **Round 1 = schema-discovery round**: open vocabulary, synonym map built after, consolidation deferred until all markers submit (adopted 07-09; matches actual conduct).
- **Machine marking architecture**: mechanical pipeline from the human-derived schema (lexicon lookup + small closed-set classifiers); no free-generation LLM marking (the PI's ruling 07-08). **LLM marks MAY be collected during discovery, SEALED, excluded from schema consolidation per pack §normalization step 4; unsealed only post-map** (adopted 07-09).

## 3. Predicted contrast orderings — TO BE FILLED JOINTLY BEFORE ANY VALIDATION SCORING

Format: within each cluster, name ≥1 predicted-HIGH-conformance translation and ≥1 predicted-LOW (beautiful-but-free / heavily domesticating), with one sentence of published-reputation justification each. Predictions are falsifiable commitments: if the rubric inverts them, the rubric (or the prediction's justification) is wrong, and the paper reports it either way.

| cluster | predicted HIGH | predicted LOW | justification source |
|---|---|---|---|
| Classical zh → en | Arthur Waley (alt: Stephen Owen) | Ezra Pound *Cathay* (alt: 许渊冲 rhymed en versions) | verification report 07-05 |
| Tang → jp | — no HIGH bet: **吉川幸次郎 ruled evaluation-target-not-benchmark 07-09** (nobody in pool can provide a fidelity verdict; scored, unbetted, Howard-treatment) | 井伏鱒二 (cited: 芥川敏子 1994, 「サヨナラ」ダケガ人生ダ "beyond free translation"; alt: 佐藤春夫 — 薔薇-for-香花 invention verified against primary text + Kawakami 閑人詩話 criticism) | zhjp_reputation_report.md |
| Haiku → en | R. H. Blyth | Harold Stewart *A Net of Fireflies* | verification report 07-05 |
| Haiku → zh | 周作人 (cited: self-stated fidelity-first principle 1918/1925; Takuboku/Issa still benchmark) | 陳黎/張芬齡 — informal criticism only (Douban); **recommend scored-no-bet** | zhjp_reputation_report.md |
| Sonnets → zh | 梁宗岱 | 梁实秋 (documented meter abandonment, 意译; alt: 辜正坤) | verification report 07-05 |
| Sonnets → jp | — no bets: Takamatsu unsupported by sources | — | **坪内逍遥 designated per-category SHOWCASE, not a bet**: sources say syntax tracks the English closely while diction domesticates into Kabuki-register — i.e., a translator the rubric should *decompose*, not rank; the per-category conformance report is the demonstration |
| Baudelaire → zh | 钱春绮 AND 郭宏安 (dual-listed; reputation genuinely split) | — none: no documented domesticating complete edition found; cluster carries HIGH-side bets only (retraction 07-05) | verification report 07-05 |
| Baudelaire → en | William Aggeler | Millay/Dillon *Flowers of Evil* (alt: Roy Campbell) | verification report 07-05 |

Special case: **Richard Howard (Baudelaire→en)** is scored but carries **no bet** — his fidelity reputation is documented-contested (prestige vs literalist criticism); his rubric position is reported as a finding, not a prediction.
Nuance on file: 戴望舒's fidelity reputation is functional/emotional rather than literal (see report) — he is scored, unbetted, same treatment as Howard.
Added 07-05: **Obata** and **Lowell/Ayscough** (Tang/classical→en) join the scored-no-bet list — reputation evidence came back thin/paywalled (see `obata_lowell_reputation_report.md`); they provide same-source comparison curves on 8 multiply-covered poems, not predictions. Cluster label corrected 07-09 ✓ (青青河畔草 is Han; 饮马长城窟行 adopted 07-08 into dev/schema-discovery, also Han).

Candidate LOW archetypes to consider while filling (not commitments): Fitzgerald-type free renderings, rhymed-at-all-costs Victorian versions, 郭沫若-style 再創作. HIGH archetypes: poet-philologist collaborations, foreignizing translations with documented markedness (Venuti's catalogue is a source of nominations).

**Secondary hypothesis (registered 07-05, Anneliese's objection → reformulation): translator profession predicts the GRAIN of deviation, not its amount.** Field grain = invent/delete whole categories (Pound: "sot" invented, 空床 deleted). Value grain = fields preserved, values shifted directionally generic→specific (佐藤: 香花→薔薇 — scores *conformant* at field level; visible only on a typed value comparison: same / more-specific / less-specific, i.e. a concretization check). Predictions: scholar-translators conform at both grains; 井伏-type free poets deviate at field grain; 佐藤-type poets show elevated concretization rate at value grain with near-scholar field conformance. 吉川 tests the scholar profile. Consequence for tooling: value-level agreement is not equality-Jaccard (pilot showed 0.161 = noise) but a specificity-ladder classification — machine-assisted, human-audited. 佐藤 = designated fine-grain test case, removed from simple LOW candidacy.

## 4. Data hygiene

- Dev passages (curving allowed) and validation pairs (frozen, scored once) are disjoint lists, enumerated in `corpus_manifest.md` at freeze. **Scope: the ENTIRE paper** — dev serves schema discovery + rubric tuning; validation = the once-scored conformance runs (clarified 07-09). All round-1 poems are dev.
- The validation run happens once per rubric version; reruns require a dated protocol appendix stating why.
- The honest number ships.

## 5. Liveness-index audit set (fixed at freeze)

Known-answer cases the index must order correctly before it is used: καλχαίνω→purple (recoverable), 然→fire (marginal, alive via 燃), 法→water (dead/excavatable), consider→sidus (dead). Additions welcome before freeze. **07-09: empirical candidates (盈盈, 素) considered and NOT added — with n=2 high-literacy markers, marker-confirmed liveness is unstable; population-liveness stays unclaimed until the pool is characterized (An: normal readers let 叠字 glide). Per-marker coverage is recorded; §5 keeps philology seeds only.**
