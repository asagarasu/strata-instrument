#!/usr/bin/env python3
"""Findings v5.1 (#62, 2026-07-28 late night) — THE STAR REVERSAL: the v5.0
census re-run under ONE law change this sitting — the fr TOKEN-GHOST STAR RETIRES.

  • THE STAR REVERSAL (her ruling, #62, verbatim: "I think we should reverse the
    star situation. We should somehow indicate that 'zh is terrific and we have
    the full support here!' while other ones we write in prose about 'ok this is
    not built and from what we see in zh it is really really thin.'"). In the law
    module `linegrain_law_60.line_state` the fr token-ghost branch no longer
    stars (its fourth return goes False-for-all; was `rid.startswith("fr:")`).
    The full-support side is now marked POSITIVELY on the exhibit face (the zh
    FULL-STACK BADGE, driven by `LAW.FULL_STACK_LANGS`); the non-zh referent
    thinness is carried in PROSE (the scope-sentence, RULERS referent-coverage
    doctrine), never a star. The present*/silent* uncovered-WORD-channel stars —
    a DEEPER deficiency — are UNTOUCHED and stay starred.

    THE MEASURED EFFECT vs v5.0 (ALL in fr:baudelaire COLOUR crossings — 33
    distinct fr colour source token-ghosts × their seats; every other cell,
    field, board, seat-class, and the wording/residual/change registries
    BYTE-IDENTICAL to v5.0):
      · comparisons UNCHANGED (4143 → 4143 — a star is a tier tag, not a cell);
      · conservation EXACT per cell (full + starred conserved);
      · crossings move STARRED → FULL-STACK (demonstrative), colour only:
          GHOST-CARRY  +133 (271 → 404; starred 133 → 0)
          UNHEARD       +90 (208 → 298; starred 166 → 76)
          RENDERED      +20 ( 40 →  60; starred 303 → 283)
          GHOST-GROUNDED +3 (  5 →   8; starred   3 → 0)
        246 crossing-rows total; the 247th fr-colour token-ghost crossing keeps a
        star from an INDEPENDENT seat-side present*/silent* star (ttwo), so it
        stays starred by design.

    Behind the reversal (chair count 07-28): the zh referent leg alters 2 of 669
    word-tier-silent verdicts (colour 0/352, sound 2/317 — 0.30%, smoke tier;
    the two: elevation zh:guo_hongan L19 sound, zh:qian_chunqi L19 sound). The
    referent blindness on non-zh seats is real but thin.

Cites: her reversal ruling (#62) + the referent-coverage doctrine (RULERS) + the
star-reversal registration/EXHIBIT_SPEC amendment. Pure wrapper over the v4.3
census law — only OUT_J changes; the star retirement lives in
linegrain_law_60.line_state (single source). v4/.1/.2/.3/.4/.5/.6/.7/.8/.9 and
v5.0 stay as records (v5.0 = the fr-star era). Guarded main."""
from pathlib import Path

import linegrain_census_v43_60 as C

HERE = Path(__file__).resolve().parent
C.OUT_J = HERE.parent / "reports" / "findings_v51_linegrain_0728_62.json"

def _relabel_header():
    """#69 (2026-08-07): emit the header #63 hand-relabelled into the committed
    record ('header only, data untouched'), so a replay reproduces the file of
    record byte-for-byte. v4.3/v5.0 wrappers keep their own eras' headers."""
    import json
    d = json.loads(C.OUT_J.read_text(encoding="utf-8"))
    d["what"] = ("findings v5.1 — the star-reversal era, census of record for "
                 "COUNTS (salience-positive trigger + fr star retirement; "
                 "token-ghost law and PI-approved alignments carried from v4.3)")
    d["supersedes"] = "findings_v50 (salience-positive era), v49, v4x line"
    d["header_relabelled"] = ("#63, 2026-07-29 — header only, data untouched "
                              "(the v4.3/#60 label was wrapper heritage); "
                              "reporting labels live in findings_v6 per "
                              "census_coverage_relabel_registration_0729_63.md")
    C.OUT_J.write_text(json.dumps(d, ensure_ascii=False, indent=1),
                       encoding="utf-8")


if __name__ == "__main__":
    C.main()
    _relabel_header()
