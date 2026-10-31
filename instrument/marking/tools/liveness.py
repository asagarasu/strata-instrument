#!/usr/bin/env python3
"""Liveness index for latent decomposition candidates (tagset_v2 machine layer
item 2 + rubric_pipeline_plan §3; audit contract in protocol_DRAFT §5).

A latent candidate is an etymon field buried in a word (法's water, 然's fire,
consider's star). By construction every latent candidate is sense-drifted —
if the field were in the active sense it would be an active-layer mark — so
the index scores *recoverability* for a reader population from three word-facts
named in the pipeline plan:

  surface_trace      is the etymon material visible in the modern written form?
                     whole (root is the word's visible body) / component
                     (a visible part, e.g. 氵 in 法) / absent (consider)
  root_productivity  strongest living cognate that carries the field
                     transparently, by frequency class: common (燃) /
                     uncommon / rare (sidereal) / archaic (灋) / none
  frequency          entrenchment of the host word in its drifted sense:
                     rare (reader stalls and examines: καλχαίνω) / common /
                     grammaticalized (glass — looked through, never at: 然)

  prior = 0.35*T + 0.45*P + 0.20*R

Bands (reporting sugar; the ORDERING is the §5 contract):
  recoverable >= 0.70 > marginal >= 0.35 > dead;
  "excavatable" = dead with a visible surface trace (法, not consider).
Weights and thresholds are CALIBRATION on the n=4 audit set and will be
re-stressed as cases are added before freeze; nothing here may special-case
a word.

Empirical override (tagset_v2, verbatim rule): a candidate is live for a
population iff native active marks cover its field on units containing the
word. When marks exist, coverage outranks the lexical prior; the prior only
fills the gap where no native has marked yet. Both are always reported.

Case file: blocks of `key: value` lines separated by blank lines, `#` comments.
Keys: case, word, field, surface_trace, root_productivity, frequency,
      units (optional, comma-separated unit ids for coverage vs a marks file).

Usage:
  liveness.py <cases.txt> [--marks <compact_marks.txt> --map <synonyms.txt>]
Marks files use the compact format (normalize.py output / agreement.py input);
the synonym map is applied to fields before coverage, same as everywhere else.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import normalize

W_TRACE, W_PROD, W_FREQ = 0.35, 0.45, 0.20
TRACE = {"whole": 1.0, "component": 0.5, "absent": 0.0}
PROD = {"common": 1.0, "uncommon": 0.6, "rare": 0.3, "archaic": 0.1, "none": 0.0}
FREQ = {"rare": 1.0, "common": 0.3, "grammaticalized": 0.0}
RECOVERABLE, MARGINAL = 0.70, 0.35


def parse_cases(path):
    cases, block = [], {}
    for ln in Path(path).read_text(encoding="utf-8").splitlines() + [""]:
        ln = ln.split("#")[0].strip()
        if not ln:
            if block:
                cases.append(block)
                block = {}
            continue
        if ":" in ln:
            k, v = ln.split(":", 1)
            block[k.strip().lower()] = v.strip()
    return cases


def prior_score(case):
    t = TRACE[case["surface_trace"]]
    p = PROD[case["root_productivity"]]
    r = FREQ[case["frequency"]]
    return round(W_TRACE * t + W_PROD * p + W_FREQ * r, 4)


def band(score, case):
    if score >= RECOVERABLE:
        return "recoverable"
    if score >= MARGINAL:
        return "marginal"
    return "dead/excavatable" if TRACE[case["surface_trace"]] > 0 else "dead"


def coverage(case, marks_units):
    """tagset_v2 rule: live iff native active marks cover the candidate's
    field on the units containing the word. Returns fraction of the given
    units on which the field appears, or None if the case names no units."""
    units = [u.strip().upper() for u in case.get("units", "").split(",") if u.strip()]
    if not units:
        return None
    hit = sum(
        1 for u in units
        if case["field"].lower() in {f for f, _ in marks_units.get(u, [])}
    )
    return hit / len(units)


def verdict(prior_band, cov):
    if cov is None:
        return prior_band + " (prior)"
    return ("live" if cov > 0 else "not-live") + " (coverage)"


def load_marks(path, synmap):
    units, warns = normalize.parse_file(Path(path))
    merges = {"field": {}, "value": {}}
    return normalize.normalize_units(units, synmap, {}, merges), warns


def main(argv):
    cases_path, marks_path, map_path = None, None, None
    i = 0
    while i < len(argv):
        if argv[i] == "--marks":
            i += 1; marks_path = argv[i]
        elif argv[i] == "--map":
            i += 1; map_path = argv[i]
        else:
            cases_path = argv[i]
        i += 1
    if not cases_path:
        print(__doc__); sys.exit(2)
    synmap = normalize.load_map(map_path) if map_path else {}
    marks = {}
    if marks_path:
        marks, warns = load_marks(marks_path, synmap)
        for w in warns:
            print("WARN:", w, file=sys.stderr)
    print(f"{'case':24} {'prior':>6}  {'band':18} {'coverage':>8}  verdict")
    for case in sorted(parse_cases(cases_path), key=prior_score, reverse=True):
        s = prior_score(case)
        b = band(s, case)
        cov = coverage(case, marks) if marks else None
        cs = f"{cov:.2f}" if cov is not None else "-"
        print(f"{case['case']:24} {s:6.3f}  {b:18} {cs:>8}  {verdict(b, cov)}")


if __name__ == "__main__":
    main(sys.argv[1:])
