# corpus/alignments — Line Alignment Files

## Purpose

These JSON files provide line-level alignment maps for seats whose parsed
line count differs from the source poem count. A seat with a line-count
mismatch cannot be used for line-grain crossing analyses without an explicit
map of which seat line(s) render each source line.

Status of all files in this directory: **VERIFICATION PENDING — not law
until chair-verified and PI-approved.**

---

## Format Specification

Each file is a JSON object with the following keys:

```json
{
  "board":         "<board name>",
  "rid":           "<seat rid, e.g. de:bethge_1907>",
  "source_lines":  <integer — number of parsed source lines>,
  "seat_lines":    <integer — number of parsed seat lines>,
  "map": [
    {
      "src":  <integer — source line number, 1-indexed>,
      "seat": [<integer, ...>],
      "note": "<justification quoting 3-6 words from each side>"
    }
  ],
  "seat_lines_unmapped": [
    {
      "seat": <integer — seat line number, 1-indexed>,
      "note": "<reason — e.g. translator's added title, refrain, moral>"
    }
  ],
  "confidence": "<one-line summary of overall certainty and soft spots>",
  "provenance":  "<authorship + commission + verification status>"
}
```

**Invariants (checked at verification):**

1. `map` has exactly `source_lines` entries, one per source line in order.
2. Every source line gets exactly one `map` entry; `seat` may be `[]`
   (untranslated) but must be present.
3. Coverage: every integer in `1 .. seat_lines` appears exactly once
   across all `map[*].seat` lists and `seat_lines_unmapped[*].seat`.
4. Monotonicity: the seat-line numbers across `map` entries should be
   non-decreasing. Any non-monotonic entry requires an explicit note
   explaining the inversion (rare in poetry translation).
5. Notes quote sparingly (a few words per side) — some renderings are
   in-copyright; do not reproduce full lines.

---

## Files in this directory

| File | Board | Seat rid | src lines | seat lines | Shape |
|------|-------|----------|-----------|------------|-------|
| `qingqing__de_bethge_1907.json` | qingqing | de:bethge_1907 | 10 | 15 | expansion + 3 unmapped appended lines |
| `qingqing__en_pound_1915.json`  | qingqing | en:pound_1915  | 10 |  9 | src L5+L6 fused into seat L5; src L10 untranslated |
| `qingqing__en_waley_1918.json`  | qingqing | en:waley_1918  | 10 | 16 | 2:1 split throughout src L1–L6; 1:1 for src L7–L10 |
| `tiaotiao__de_forke_1899.json`  | tiaotiao | de:forke_1899  | 10 | 20 | strict 2:1 throughout — 5 short-line quatrains |
| `invitation__zh_guo_hongan.json`| invitation | zh:guo_hongan | 42 | 41 | src L29+L30 fused into seat L29; all else 1:1 |

---

## How the chair verifies

1. **Coverage check.** For each file: collect all integers in
   `map[*].seat` and `seat_lines_unmapped[*].seat`. Assert the union
   equals `{1, 2, ..., seat_lines}` with no duplicates.

2. **Source coverage.** Assert `len(map) == source_lines` and that
   `map[i]["src"] == i+1` for all i (each source line addressed once,
   in order).

3. **Monotonicity check.** Walk `map` entries; verify that the maximum
   seat number in entry i is <= minimum seat number in entry i+1
   (or that the entry is flagged with a non-monotonic justification note).

4. **Semantic spot-checks.** For each file, read the seat text at the
   mapped lines and confirm the `note` quote matches. Priority spot-checks:
   - `qingqing__en_pound_1915.json` src L5+L6 fusion: verify seat L5
     renders 纤纤/手 content, not 娥娥/红粉 content.
   - `qingqing__en_waley_1918.json`: verify the 2-line split pattern
     applies to all six reduplicated-pair source lines (L1–L6).
   - `tiaotiao__de_forke_1899.json`: verify each quatrain maps to exactly
     one source couplet pair.
   - `invitation__zh_guo_hongan.json` src L29+L30 fusion: confirm
     seat L29 is '看那运河上，船儿入梦乡，' (one printed line).
   - `invitation__zh_guo_hongan.json` stanza-3 redistribution: spot-check
     seat L35–L37 vs src L36–L38 (color/landscape reordering noted as
     soft spot).

5. **Sign-off.** After passing all checks, update `provenance` field in
   each file to remove "VERIFICATION PENDING" and add "VERIFIED [date]
   [her initials/blessing]".

## Chair verification (2026-07-28, #60)
- MECHANICAL: all five files PASS (src coverage exact · every seat line
  accounted exactly once · monotonic).
- CORRECTION applied: pound src5/src6 — agent used seat-first bookkeeping for
  the fusion (seat L5 filed under src L5); corrected to CONTENT-faithful
  (seat L5 renders 纖纖出素手 → filed under src L6; src L5's rouge content =
  dropped, seat []) — crossings compare content, not bookkeeping.
- guo stanza-3 (src L35-38): agent kept monotonic positional mapping with the
  colour-redistribution documented in notes. Chair-reviewed and ACCEPTED —
  the redistribution is intra-stanza paraphrase where line-precision is not
  in the text; flagged for her eye at blessing.
- STATUS: chair-verified; **PENDING HER BLESSING** — on her word these become
  the alignment files of law ("line-grain awaits the PI's alignment files") and
  unlock line-grain verdicts for the five seats (census v4.3, convened).
