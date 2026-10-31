# Dated appendix — arm-1 admissibility: statistical NLP admitted (07-15)
*An ruling, in session; chair #47 scribing. Resolves the ⚠ line left
open in `design/arm1_mechanical_labeling_design.md` since 07-13.*

**Ruled:** pretrained STATISTICAL taggers — segmenters, POS models —
are admissible in arm 1 ("an obvious yes," her words). Furthermore,
her direction: segmentation alone is insufficient — arm 1 needs
**per-field classifiers** ("if a word is X ∈ {color, sound, …}"),
consistent with the 07-08 frozen law's own "small closed-set
classifiers" clause. Generative/instructed models remain ❌ in arm 1;
their only door is still arm 2 (licensing band, fail-closed).

**Her calibration reframe, same sitting:** labeler-vs-human dev
calibration stands as the design's step, but with n=4 markers it is
sanity-scale, "loose and toy-ish" — not a gold standard. The full
version of this architecture is arm-2's: LLM schema discovery for
new/understaffed languages, licensed against human pools. The dev
table rehearses the shape at toy scale; report it as such.

**Register note (chair, engineering):** the ruling is adopted; where
it pays first is en (POS) and any modern-zh text. For the classical
TRADITIONAL verse in dev, mainstream segmenters (jieba-class,
modern-simplified-news priors) are the wrong register — v2 therefore
implements compound-aware maximal-match segmentation (deterministic,
lexicon-driven, register-true), and the pretrained per-field
classifier increment (WordNet supersenses en / HowNet-CiLin-class
taxonomies zh, static-embedding centroid backstop per the 07-10
embeddings ruling) is the named v3 build.
