# STRATA — an instrument for the typed axes along which a translation keeps or loses its source

A fidelity metric built on a multilingual encoder scores a translation with one
number: the cosine between source and translation embeddings. That number says
how far two texts sit apart, not *what moved*. STRATA fixes a few interpretable
directions ("axes") in the embedding space in advance — among them colour and
sound — and measures, line by line, whether a translation keeps or loses the
reading on each axis. On axes a reader plainly registers, translators behave in
a way one cosine cannot see.

## Scope of this repository

This repository is the **technical and empirical artifact** behind the
accompanying two-page research note. It is *not* the full project. It contains:

- **the STRATA instrument** — the encoder wiring, the per-axis whitening and
  projection, the line-state law, the field labelers, and the comparator;
- **the census data and corpus** reported in the note — the per-board,
  per-line score legs and the result file the census counts are read from, plus
  the poems and translations the census ran on;
- **a 2×2 colour demonstration** (`twobytwo.py`) — a constructed, reverse-decoded
  four-cell example on one line, showing a colour axis moving far while the
  cosine barely moves.

Every census number in the note is reproducible from the files here:
`reports/findings_v51_linegrain_0728_62.json` (the census of record) together
with the state/comparator law in `instrument/publishable/linegrain_law_60.py`,
over the corpus under `instrument/corpus/`. The 2×2 numbers are in
`instrument/` → produced by `twobytwo.py` and recorded in
`results/twobytwo_results.json` once you run it.

## Layout

```
twobytwo.py                     the 2x2 colour demonstration (run this)
requirements.txt
fetch_verify.sh                 fetch + hash-verify the external third-party resources
reports/findings_v51_...json    the census of record (counts)
reports/figures/                a few committed exhibit SVGs
docs/                           methodology statement, scoring manual, manifests
design/marking_pack_v2.md       the reader study
appendices/                     the standing method rulings
instrument/                     the importable instrument (mirrors the engine layout)
  mdtest.py                       instrument library used by twobytwo.py
  publishable/                    scorers, the line-state law, exemplar/census code
  marking/tools/                  the field labelers + the illumination lexicon
  engine/results/                 the five trained axes (.npz) + cuts / news-z norms
  corpus/                         the poems, translations, alignments, TOC index
  lexical_resources/              small first-party colour / sound / temporal inventories
```

Imports resolve inside the repository: `twobytwo.py` puts `instrument/` on
`sys.path`; the modules under `instrument/` resolve all their data paths
relative to `instrument/`.

## Reproduce

1. Install the Python dependencies:

   ```
   pip install -r requirements.txt
   ```

2. The encoder is **`sentence-transformers/LaBSE`**, downloaded from the
   HuggingFace Hub on first run (no model weights are vendored here).

3. Some labeler legs consult large **third-party lexical resources** that are
   *not* vendored (for size and licensing): WordNet 3.0, the Guangyun (廣韻)
   rime dictionary, the Unicode Unihan database, and the CMU Pronouncing
   Dictionary. Fetch and hash-verify them with:

   ```
   ./fetch_verify.sh
   ```

   The 2×2 colour demonstration does **not** require these: when a resource is
   absent the corresponding inventory leg degrades to empty (it warns once on
   stderr), which does not affect the demonstration's reported colour verdicts.
   They are needed for a full re-labeling run across all boards and languages.

4. Run the demonstration:

   ```
   python twobytwo.py --explore     # stage 1: print the geometry that fixes the cell targets
   python twobytwo.py --run         # stage 2: construct + decode the four cells, write results/
   ```

   `--run` writes `results/twobytwo_results.json` (every number, per cell) and
   `results/dictionary_coords.tsv`.

## Corpus and provenance

The corpus under `instrument/corpus/` carries the public-domain source poems and
translations. In-copyright translations are **not** redistributed: the score
legs record their provenance and hashes, and their line text is redacted. Set
`STRATA_LOCAL_CORPUS=<your acquisitions root>` to resolve in-copyright seats
from your own licensed copies; unset, they list as missing.

## The accompanying note

A two-page research note is provided alongside this repository; it motivates the
instrument and reports the census and the demonstration.

## License

See `LICENSE`.
