# Methodology statement — 2026-07-16 (kill-pass amendments applied)

> ⚠ **HISTORICAL DOCUMENT — banner added 2026-07-28 (#60, at the order of the PI — Anneliese; see §8).**
> This text is the audit trail of its era. The 07-27/28 sittings changed the
> construct beneath it: the POEM FOLD is retired (verdicts are line-grain
> crossings); GHOST is pinned at the WORD (a triggered token no channel
> claims); triggers are TWO-SIDED (|Δ| ≥ cut); the TIER MAP governs claim
> strength; alignment files are law; a French colour boolean exists.
> **Current state lives in `methodology_sheet_CURRENT_0726_58.md` (v2) and
> `SCORING_MANUAL_0726_59.md` (v3).** Read this file for provenance, never
> for state.

**STATUS: KEEP — the PI's kill-pass 07-16. (The DRAFT banner was stale —
KEEP had been given but the banner never removed; corrected 07-17 on
her word, in session with #49.) Supersedes methodology_statement_0713
+ the 0715 delta as START-HERE; the file-by-file audit runs against
this document.**

## 1. What this project is
One instrument: the **translation rubric** — it scores any
translation's conformance to its source's **trait interface**.
Sentence = object · trait set = interface · translation =
reimplementation · quality = conformance test. This repository is the
rubric's technical and empirical artifact. THE SCALAR IS THE PAPER: graded
trait-intensity scoring is the thesis; ceilings, schema, and
licensing are its harness.

## 2. Schema (discovery COMPLETE — this is the field inventory)
Schema discovery is finished. Its product: the inventory of trait
fields the machines mark for, expressed as flat `field, value`
pairs pointed at words, with an ACTIVE (surface) and LATENT
(decomposition-recoverable) layer, identical on both sides of a
translation pair. Consolidation settled at v3.4 (applied 07-15,
two-judge blind-validated). The discovery phase's working
heuristics (the field/axis and referent/device distinctions,
attention-vs-structure) did their work and are retired with it;
where one still earns its keep it appears below as instrument
design, not doctrine.

## 3. Scoring doctrine (the rubric's actual rules)
- Asymmetric survival scoring: active→active = conformance ·
  latent→active = revival, never penalized · active→latent =
  partial loss · active→∅ = deformation. Weak-tier survival is a
  finding, not noise.
- Rubric comparisons are machine-tags vs machine-tags. ~~The same
  instrument on both sides of a pair, so coverage bias cancels.~~
  *(REWORDED at her KEEP 07-19 ("perfect"), external review F1 +
  her two-assessor equating argument:)* Cross-side comparison
  happens in ensemble-relative (rank) space: each side scored among
  its own peers (the ~10-rendering ensemble = the shared world), and
  "high among peers" transfers where each side's assessor is
  certified against its own external truth and the peer set shows
  real variance. Raw cross-side scalar deltas are never compared —
  sensitivity differences (measured: 5.6× compression) do not
  cancel.
- Latent traits count only if LIVE — readers can still feel them.
  竹马 carries bamboo and horse only if this pool's readers actually
  notice them there; 法 shows nobody its water anymore. Liveness is
  decided by evidence: a latent field is live when this pool's
  markers actually marked it on units containing the word; where no
  marks exist yet, an estimate from three observable word-facts
  fills the gap (is the old root visible in the written form? does
  a living relative-word still carry the field — 燃 keeps 然's
  fire? is the host word too common to be looked AT rather than
  through?). Live-for-Tang-readers ≠ live-for-us: every liveness
  claim names its reader pool.
- Four markers and nine poems make every current
  number a dev-scale floor or pilot estimate. Claims are calibrated
  to instrument-plus-pilot; nothing here supports population-level
  generalization yet.

## 4. Corpus & the human committee
Four markers; collection CLOSED; 9 dev poems (zh/en/fr/jp). The
committee's job was **field discovery** — the schema in §2 is its
product, and that job is complete. The agreement band was a side
job: a test of whether LLMs could extend marking to languages
beyond the committee's reach. Regrettably they cannot (§5); what
survives of that arm is scale-marking in zh. The corpus manifest
is binding, which here means one thing: dev and validation sets
share no translation pairs, and validation pairs stay untouched
until the demonstration run. 江上吟 is the held-out post-freeze
exhibit, marked, ~~unspent~~ *(exhibit purpose retired by her
ruling 07-16 (ledger item 6); SPENT for the smoke tier 07-18 at her
offer — her word-pointed marks, scored in the line-grain smoke
tables. Validation translation pairs remain untouched. CHRONOLOGY
CORRECTED same day, review F10: 江上吟 was first spent 2026-07-15
(marks+validator+result committed together; a sound organ tuned on
its named miss minutes later) — it has been development data since
07-15, and cannot independently validate that organ. Full rewrite +
manifest correction = remediation R3, her KEEP.)*

## 5. Machine marking (side-experiment, complete)
Machines can exceed human agreement on a well-trained language —
but "well-trained" is only certifiable by a human reader of that
language; without one, excellent and confidently-wrong are
indistinguishable from outside. So machines cannot take part in
new-language schema discovery, and no license extends the
instrument's reach. NO LLM MARKS ANYTHING in this project (her
ruling 07-19 #52, in session: "we are not letting any LLM doing
marking" — any past license was schema-discovery-scoped, and schema
discovery is permanently closed). The demonstration pipeline is
instruments-only: rulers, organs, labelers produce every field
state, source-side and translation-side alike.
Criterion, controls, verdicts, numbers: marking/
machine_round_20260716.md · reports/ceilings_v34_20260716.md ·
appendices/ruling_licensing_*_20260716.md.

## 6. The instrument shelf
**Boolean labelers** (color, sound-device, plant, temporal) —
sanity tier; no further lexicon development. Provenance law: no
dev-fitted lexicon — citable derivations or flagged
AUTHORED-INTERIM with a named replacement. Current table
(post-provenance, reproduced from code): color .87 · sound .67 ·
plant .78 · temporal .82 (F1). Structural end-rhyme and the HowNet
sound-referent query are separate organs. *(07-20 addition at her
word: a DARK boolean joined the tier — HowNet dark-gloss derivation,
162 words, token-matched — built, selftested, UNCALIBRATED until its
dev run; marking/tools/dark_labeler_52.py. The boolean tier gained a
second job the same night: HOME-ANCHOR for the descriptive/latent
discrimination — boolean fires → a scalar score is descriptive;
boolean silent while the scalar runs high → latent candidate.)*
**L1 ordinal profiles** (word grain): HowNet DEF head→STRONG /
in-DEF→MEDIUM; en via WordNet first-sense closure. *(07-20, her
rulings: L2 cultural-associative = OUT of measurement — reflective-
infused; L3 constituent = LIVE as a PROCEDURE, not a new ruler —
in-situ buried Δ over exposure denominator = per-field TRANSMISSION
RATIO, liveness-gated, on the existing axes; three registered
validation aborts recorded, redo registered awaiting her word;
design/word_latent_instrument_v1_52.md.)* Raw sememes out;
sememe→field mapping is a maths decision — a derivable criterion
(assignment optimized against machine marks, validated held-out,
certificate-gated), not a judgment call by anyone. Human decisions
ended with field discovery; from here the machinery decides by
measurement or it does not decide.
**Scalar rulers — the thesis.** A scalar ruler takes a sentence
and returns a number: either how strongly a trait field is present
at all (a SALIENCE ruler) or where the sentence sits between a
field's poles (a VALUE ruler — darker/brighter, saturated/faded).
Mechanically: probe sentences define a direction in a multilingual
embedding space; a sentence's score is its projection onto that
direction; mask one word, re-score, and the difference is that
word's contribution in its context. The rubric needs these numbers
because survival categories like "scalar shifted" compare
intensities, not memberships — booleans cannot score them.
- Form proven: word-masked in-situ scoring (deletion mask;
  word-unit masking for 叠字/compounds — char-level smears);
  batch-invariance certificate gates every run; the form beat the
  bag-level baseline across three different axes.
- Three instrument species, set by probe algebra: polarity
  contrast (F⁺−F⁻) → signed VALUE ruler · presence contrast
  (F−neutral) → unsigned FIELD-SALIENCE ruler ("plant-ness" is a
  salience question; the dye axis is a salience ruler and was
  correct for its original purpose) · latent-charge vs
  realized-reading rulers form a layer pair, and their per-word
  divergence measures latency (紅 stays hot; 窗 keeps daylight in a
  dark line).
- Valence: the darkness axis's valence entanglement is measured —
  orthogonalization collapses the AUC gap entirely; at n=7 dev
  positives darkness and grief are statistically inseparable. Two
  rulers therefore: a physical (valence-orthogonal) dark ruler and
  a declared-mixed register ruler (name pending).
- Probe provenance: the chair is a co-author, so chair-authored
  probes are team-authored; ratification does not change that. The
  paper's rulers use ground truth external to the team — current
  best: dual-witness COCO selection (a stranger's caption
  verbalizes the light state ∧ measured pixel luminance agrees;
  word-lists select, never label).
- Register asymmetry (packageable finding): natural description
  verbalizes darkness adverbially (explicit light-words) and
  brightness denotatively (luminous referents) — the marked pole
  is said, the default pole is carried in nouns.
- Encoder: LaBSE is the instrument. *(AMENDED 2026-07-18 at her go —
  appendices/ruling_7_3_amendment_probe_route_20260718.md. The
  original line read LaBSE's zh as thin in the descriptive subspace
  and put a zh-real encoder on the critical path; the blindness
  proved to be in the caption-route CONSTRUCTION, not the encoder —
  word-pole zh probes read 皎皎/黯黯 at full resolution on LaBSE
  itself, and no encoder beat LaBSE at real n across six variants.
  The zh-side fix is probe-route, not encoder swap; caption-route
  compression is measured (5.6×) and disclosed. 儒藏-scale classical
  breadth pending, stage 2.)*
- Evaluation discipline: no AUC without a bootstrap CI; at n=7
  positives all current AUC differences are inside the noise band —
  point-racing stopped. Evaluation truth by species, no new marks:
  SALIENCE rulers evaluate against the EXISTING dev field marks
  (plant/color/temporal carry dozens of positives across 46 units;
  only light/brightness is n=7). VALUE rulers evaluate against
  DERIVED truth: contrast batteries generated from citable sources
  (e.g. HowNet brightness-sememe classes → polarity pairs, the
  皎皎/黯黯 pattern generalized by math) and physical calibrations
  of the dual-witness class. Machine marks are never evaluation
  truth (marker ≠ judge, §5); machine scalar marking is not a path
  at all — scalar marks would be intensity-schema discovery.

## 7. Critical path (07-16 → 07-23)
**Get good scalar rulers for the four chosen fields: color, sound,
plant, temporal.** That is the path; everything else is done or
waits. *(07-19 R1: all four re-credentialed clean-room, + illumination
pair. 07-20: the path gained the LATENT tier — the word-latent
procedure on the same axes (no new ruler; one meter, registered
procedures point it at different measurands) — and the row-service
law is now explicitly MANY-TO-MANY: one ruler can serve several rows,
one row can be served by a composition; see the field-rows
inventory.)*
1. ✅ A SALIENCE ruler per field — presence-contrast probes from
   external/citable material, masked in-situ form,
   certificate-gated, evaluated with CIs against the existing dev
   field marks. *(R1 clean-room credentials, 07-19, her KEEP —
   token-true, development tier: color .879 · plant .801 ·
   sound-v3 .815 · temporal = documented negative, its instruments
   are organs. Latent tier measured real-and-weaker in 4/4 fields.
   Pre-R1 numbers: archived/statement_shelf_numbers_pre_R1_20260719
   .md; full program: RULERS.md + codex_triage.md.)*
2. ✅ VALUE rulers where a field has poles — the darkness pilot is
   the template; saturation is next. Truth = derived contrast
   batteries + physical calibration where the field admits one.
   *(DONE, her mark 07-18: illumination physical + register(unnamed)
   · duration ρ .860 · 浓淡 = observed negative, shown labeled.)*
3. ~~Swap in a zh-capable encoder where descriptive-zh blindness
   blocks a ruler; re-run the panels under the same gauges.~~
   *(RESOLVED OPPOSITE, 2026-07-18 amendment: no swap — word-pole
   probe construction for zh-descriptive/classical; panels re-run
   under the same gauges across six encoder variants at real n,
   LaBSE holds every seat. Appendix
   ruling_7_3_amendment_probe_route_20260718.md.)*
4. Assemble 07-23: scalar results as core, harness as supporting
   apparatus. *(REWORDED at her ruling 07-18: the numbers packed
   for 07-23 are the SCORING RUN's — rulers applied to the
   translation corpus, survival profiles under §3. The run is
   convened by her (§8); until it runs there is nothing to pack.
   Shelf and harness are ready; smoke tables sanity-checked by her
   07-18.)*

## 8. Standing laws
Batch-invariance before any number ships · certificate on every
encode run · no dev-fitted lexicon · probe ground truth external
to the team · no AUC without CI ·
revival never penalized · no LLM marking, ever (schema discovery
permanently closed; the marking era's human-scale and sole-marker
laws retired with it — her rulings 07-19 #52) · (the old
"machine-tags compare to machine-tags" law: retired as stale, her
word 07-19; for the record its "machine" was the MECHANICAL tag
tier — organs/labelers — never LLMs) ·
demonstration runs are convened by Anneliese ·
**NO GENERATIVE MODELS INSIDE INSTRUMENTS** *(her method law,
ruled 07-17, entered here at her KEEP 07-18: nothing in this paper
is "let's batch-ask an LLM" — the measurand is novel and
credibility is the scarcest reagent; instruments fail loudly or
not at all)* · THE SCALAR IS THE
PAPER.

## 9. Addendum — 07-16 afternoon (post-kill-pass results; prose above unchanged)
- **Graded capacity DEMONSTRATED** (supersedes the frontier line
  "nothing binary establishes graded intensity"): a blind-built
  duration-value axis (TimeLong/TimeShort head-sememes, committed
  before the dataset existed locally) tracks 2,101 numeric duration
  magnitudes at Spearman .860 [.843–.875]; verbal subset .811 —
  pure lexical gradedness. Value axes are calibratable continuous
  instruments where numeric truth exists; fields without numeric
  ledgers inherit the capacity, not the calibration.
  caesitas_proto/DURATION_DOSSIER.md.
- **Valence yardstick DERIVED** (知网 lists, 8,936 words): the
  authored quad axis barely resembles it (cos .209); the
  illumination axis is cleaner against the honest ruler (residual
  .075). Chain now derived at every layer.
- **Field shelf**: color salience (locked .790) and plant (.712)
  shipped; temporal = documented negative (time is ground in
  language); color value layer = observed negative (chroma doesn't
  reach wording). SOUND salience ruler BUILT (#49, 07-17, registered
  da58740 before the run): battery holds (locked .689 [.644–.735],
  halves agree) · holdout d′ 1.35 missed its registered ≥2.0 · dev
  null at pilot scale (.542, 22/46) — mixed at face value,
  caesitas_proto/SOUND_DOSSIER.md; follow-up calls NEEDS_HER item 9.
  *(SUPERSEDED 07-17, her ruling in session, verbatim "I agree to
  promote v3 with the new names": v3 register-orthogonalized ruler
  PROMOTED as the REALIZED-LAYER sound salience ruler — battery
  LOCKED .783 · dev .706 [.534–.848], first sound dev CIs clear of
  .5. Shelf (R1 clean-room, 07-19): color .879 · sound(realized)
  .815 · plant .801 · illumination .825 · duration ρ .860. Recorded
  here per the #49 precedent of updating §9 on her in-session
  word; pre-R1 numbers archived.)*
  ~~The encoder swap remains the one open construction item.~~
  *(CLOSED 2026-07-18: resolved as probe-route fix, no swap — see
  §6 encoder bullet and the 07-18 amendment appendix. Remaining
  open construction: 儒藏 classical breadth = sweep stage 2, at a
  sitting.)*
- **Repo unified**: caesitas_proto merged into this repo (full
  history); the collaborator invited; CAESITAS_START_HERE.md at root is
  her onboarding. Survey of temporal/sentiment witnesses saved at
  caesitas_proto/temporal_witness_survey.md; durations + sentiment
  lists vendored under lexical_resources/.
