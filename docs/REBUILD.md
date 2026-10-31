# REBUILD — regenerable bulk, pinned and refetchable

The paper claims (§3, §4): *"Each run is registered before it begins, and
every input is hash-pinned … every number replays from hash-pinned
inputs."* This kit makes that claim executable after the bulk
(`engine/models/`, `lexical_resources/`, `engine/nltk_data/`,
`engine/data/` payloads, `marking/tools/vectors/`) leaves any
working copy.

## The kit
- **`rebuild_manifest.tsv`** — 62 rows (fr_color_inventory added 08-12), one per fetchable artifact:
  `artifact_id · method · source · version · sha256 · local_path · notes`.
  File artifacts pin the fetched unit's sha256; directory artifacts pin
  `DIR:<filecount>@<treehash>` (deterministic tree hash, recipe in the
  verifier); git-clone artifacts additionally record the checked-out
  commit — reproduce those by clone + checkout, verify the commit.
- **`fetch_verify.sh`** — `--list` · `--verify-local` (hash what's on
  disk against every pin; no network) · `--fetch DIR` (stranger mode:
  download and verify). Fails loud, exits nonzero on any mismatch.
  Run from a FULL tree. In a bulk-less checkout expect a TRI-STATE
  report, not uniform ABSENT (measured 08-12: 15 PASS / 7 FAIL / 40
  ABSENT): small PROVENANCE/CHECKSUMS/norm files stay tracked, so
  partially-tracked dirs report FAIL — that usually means "bulk
  correctly excluded", not corruption. See the .gitignore comments for
  the fine-grained exclusion design.
- **`MANIFEST_GAPS_AND_FINDINGS.md`** — provenance of this kit
  (2026-08-06/07 night audit): 13 previously unpinned live inputs
  closed (incl. the LaBSE encoder, previously path-pinned only), 41/41
  recorded-pin cross-checks MATCH + 2 git-HEAD MATCH (zero drift), and
  the honest unresolvables (cmudict is headerless → version
  unconfirmed, hash-pinned instead; Miceli per-word source down;
  ctext origins inferred; nltk snapshot identity-pinned by zip hash).
- **`engine/docs/requirements_frozen.txt`** — the encoder env:
  python 3.9.6 + 45 pinned packages (captured from the canonical venv;
  see `REGEN_RUNBOOK_0729_62.md` §6 for the anchor-value check after
  any env rebuild).

## Pin policy (her ruling, 2026-08-07)
Pins record **what we pulled when we pulled it**. Upstream drift is
upstream's business; a changed upstream never invalidates the record,
it only means a stranger must fetch the pinned version/commit, not HEAD.

Verified state at kit creation: `--verify-local` 55/55 PASS, exit=0
(2026-08-07, full tree). Post extract-prune same day (DIR pins split to
file units, her prune agreement): **61/61 PASS, exit=0**.

## Interpreters (pinned 2026-08-12, #71, her word: "agree pin + note")

- **Encoder env (canonical):** python 3.9.6 + `engine/docs/requirements_frozen.txt`
  — every `--run`/encoder pass replays in that venv.
- **System dependency:** `xmllint` (libxml2 CLI) — every figure/exhibit
  generator shells out to it as a post-write XML self-check. Present by
  default on macOS; install libxml2 elsewhere.
- **Exhibit / presentation regeneration:** requires an interpreter WITH numpy
  — the route is indirect (the generators are stdlib, but exhibit_gen's
  corpus_line lazily imports corpus_breadth_runner_56, which imports numpy
  at module scope; without it, seat text silently degraded pre-0812, now
  warns loudly)
  (committed exhibits reproduce byte-perfect under python 3.13 + numpy 2.1.3).
  A numpy-less interpreter used to degrade every seat text SILENTLY via a
  swallowed import error — that except now warns loudly, but pin your
  interpreter anyway.
- **Scorer `--dry`:** needs numpy AND jieba in ONE interpreter. A machine with
  the split (3.9+jieba / 3.13+numpy) cannot complete it — use the frozen venv.
