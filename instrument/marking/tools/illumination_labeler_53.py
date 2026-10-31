#!/usr/bin/env python3
"""Illumination boolean labeler — whole-field REPLACEMENT for
dark_labeler_52.py (field owner's ruling, 07-20, in session):
dark_labeler_52.py was built dark-side-only; every other boolean
labeler in this family is whole-field (citable dictionary-derived
word-list checker, one per field), so the field owner ruled this
field must be whole-field too: "is this word openly about
illumination — darkness or brightness alike." This file is that
labeler. dark_labeler_52.py is NOT edited by this change — it stays
in place as the record of the dark-only build and its selftest
history (the 波黑 substring bug, the 黑夜 boundary finding). Read it
first for that history; this docstring assumes it.

SAME-DAY DERIVATION-SET FIX (07-20, in session; house precedent:
dark_labeler_52.py's same-sitting jieba/substring fix, 波黑 fired via
黑, caught by selftest and fixed same sitting). The first cut of this
file matched only the pair bright|明 on the bright side, which left
光明 silent (its own HowNet DEF records are {honest|诚实},
{lights|光}, {promissing|前景佳} — none is bright|明). The field owner
ruled this too narrow, verbatim: "we cannot have a checker saying
光明 is not light. 明天 can be not light and that is sane." Fix: widen
the bright pole from the single pair bright|明 to the full set of
HowNet sememe pairs a fresh inventory scan over HowNet.txt verifies
as illumination-denoting (bright|明, lights|光, Brightness|明暗,
illuminate|照射 — see BRIGHT_PAIRS below and
illumination_labeler_53_selftest.md for the complete candidate table,
occurrence counts, and an include/exclude call with reason for every
pair touching 光/明/亮/耀/照/辉 or an English light-root found in the
scan). 光明 now fires via lights|光 (its own DEF contains {lights|光}
verbatim). 明天 is untouched by this fix either way: all its DEF
records are time|时间 with modifier={future|将来} — purely temporal,
no bright-class pair in any candidate considered, so it stays silent
as required. Same law as always, still: citable derivation, no
dev-fitted lexicon, no FN/FP-driven edits ever — wider gloss set, not
a looser rule.

THE RULE (the PI, 07-15/16) still applies verbatim, unchanged: citable
derivation, no dev-fitted lexicon, no FN/FP-driven edits ever. Same
law, wider gloss set.

Derivation (mechanical, one pass, lexicon emitted beside this file):
  zh illumination = every HowNet W_C such that ANY of its DEF records
  (one word may span several NO. blocks / senses in HowNet, each with
  its own DEF line) carries a dark-class sememe OR a bright-class
  sememe:

    DARK pole   — a bare-English sememe token in {black, dark, dim,
                  gloomy} appears anywhere in the DEF line. UNCHANGED
                  from dark_labeler_52.py's GLOSS rule and from the
                  first cut of this file, carried over verbatim: bare
                  matching is safe on this side because none of these
                  four English glosses collide with an unrelated
                  HowNet sememe. NOT touched by today's fix.

    BRIGHT pole — the FULL PAIR appears in the DEF line, matched as a
                  pair (the English sememe token together with its
                  own paired Chinese gloss), for ANY pair in
                  BRIGHT_PAIRS:
                    bright|明        — first cut; 167 words alone.
                    lights|光        — NEW today; this is what fixes
                                       光明 (its own DEF is
                                       {lights|光}).
                    Brightness|明暗  — NEW today; 明暗's own DEF is
                                       exactly {Brightness|明暗:
                                       host={physical|物质}}.
                    illuminate|照射  — NEW today; the general HowNet
                                       sememe for light fixtures/
                                       lamps, light emission/
                                       reflection/refraction,
                                       radiation-as-light, sun- and
                                       moonlight exposure (灯, 台灯,
                                       反光, 光照, 闪光, 蜡烛, ...) —
                                       verified over its full 264-word
                                       membership, see selftest md.
                  Full-pair matching is LOAD-BEARING on every one of
                  these, not just bright|明: HowNet reuses the same
                  Chinese gloss character across unrelated English
                  primitives. 光 glosses BOTH lights|光 (illumination)
                  AND polished|光 (smooth/glazed — 光滑, 光洁, 刨子/
                  刨床, a woodworking sense with nothing to do with
                  light). 明 glosses bright|明 but ALSO explain|说明,
                  prove|证明, naif|不精明, Obviousness|明显性 (all
                  abstract/mental, not visual). 照 glosses
                  illuminate|照射 but ALSO TakeCare|照料 (caregiving).
                  耀 glosses ShowOff|炫耀 (boastfulness) with no
                  bare-耀 sememe of its own. Bare-English or
                  bare-Chinese-character matching on any of these
                  would silently pull in unrelated words (光滑, 光荣,
                  说明, 照料, 炫耀, ...) — wrong per the field owner's
                  ruling. Matching full pairs avoids this; see the
                  selftest md's inventory-scan table and the 光荣/光滑
                  polysemy trip-check probes (direct DEF inspection
                  confirms 光荣's only DEF is glorious|荣 and 光滑's
                  only DEF is polished|光 — neither is an adopted
                  pair, so neither fires).

                  Color-value and fire/heat pairs are excluded on the
                  same principle as the first cut's light|淡
                  exclusion, extended to what this scan turned up:
                  light|淡 (color-value/pale, e.g. red|红:degree=
                  {light|淡}); lighting|点燃 (combustion/ignition —
                  点燃 is "kindle/ignite"; its 94-word membership is
                  overwhelmingly matches/explosives/arson, e.g. 打火机,
                  火柴, 炸药, TNT — the English gloss "lighting" reads
                  like a light word but the HowNet primitive is
                  fire-family, not illumination); fire|火, hot|热,
                  Heat|热量 (heat is not illumination, per the task's
                  own exclusion rule).

  Source: lexical_resources/sewrl/datasets/HowNet.txt — same file,
  same substrate as dark_labeler_52.py. sha256 of that file is
  recorded in the emitted lexicon json for provenance.

Interface UNCHANGED from dark_labeler_52.py: label(unit_text) -> bool
+ carriers; jieba token matching; 叠字 rule (an XX token fires if X is
in the lexicon). The token-matching loop in label() below is copied
from dark_labeler_52.py near-verbatim (attribution: dark_labeler_52.py,
#52 night) — only the lexicon underneath it is wider (union of the two
poles instead of the dark list alone). derive()/build_lexicon() are
new: two poles instead of one, plus hownet_sha256 provenance.

KNOWN BOUNDARIES (found by selftest, declared, NOT "fixed" — same law
as dark_labeler_52.py's 黑夜 finding):
  - 黑夜 stays silent, unchanged: it tokenizes whole and its own
    HowNet DEF is temporal (night-as-time), not dark-class. Carried
    over as-is; this is the labeler's established empirical behavior.
  - 皎皎 is IN the derived bright lexicon (its own DEF is bright|明,
    ×3 records) but the LABELER stays silent on bare input "皎皎":
    jieba tokenizes it as two singleton chars ['皎','皎'], not one
    2-char token, so the 叠字 rule (which only inspects a single
    length-2 token) never gets a chance to look at it, and bare 皎
    alone is not in the lexicon (its own DEF is clear|清). This is a
    tokenizer-boundary gap between "word is in the list" and "labeler
    fires," not a derivation error — reported, not patched. UNCHANGED
    by today's fix.
  - 灿烂 stays silent: own DEF is the atomic sememe magnificent|灿烂
    (×13 records, all identical). Today's scan considered
    magnificent|灿烂 as a candidate and EXCLUDED it: the English gloss
    "magnificent" denotes grandeur/impressiveness, not literal shine
    — nothing in its dictionary sense requires light (contrast
    Resplendence|辉煌 below). Same call as the first cut, now made on
    purpose after inventory review rather than left untested.
  - 辉煌 stays silent: own DEF is 7 records of magnificent|灿烂 plus 1
    of the atomic sememe Resplendence|辉煌. Today's scan considered
    Resplendence|辉煌 too and excluded it: 辉煌 is HowNet-tagged
    predominantly (7/8 of its own DEF records) as the same
    splendor-class primitive as 灿烂, not as a light-quality primitive
    — the one Resplendence record doesn't outweigh that, and 灿烂's
    exclusion reasoning applies to its majority sense.
  - lights|光 (and, compositionally, illuminate|照射) also pull a
    small number of words that denote the ABSENCE of, or shelter
    FROM, light — not brightness — into bright_words: 阴, 树荫, 浓荫,
    绿荫, 阴凉, 树阴 each carry a DEF record shaped
    {place|地方:{exempt|免除:ResultEvent={illuminate|照射:agent=
    {lights|光:...}},location={~}}} — "a place EXEMPT FROM
    illuminate|照射," i.e. shade — and 遮阳板 (sun visor) carries
    {...{obstruct|阻止:instrument={~},patient={illuminate|照射}}} —
    "obstructs illuminate|照射." The pair-presence rule has no
    negation handling (the first cut never handled negation for
    bright|明 either — same mechanical limitation, just newly visible
    because lights|光/illuminate|照射 happen to appear inside
    HowNet's own exempt/obstruct relational structures). Reported,
    not patched — same law.
  - n_both (words carrying both poles): see the emitted lexicon json
    for the current count; report in illumination_labeler_53_selftest.md,
    not hand-verified here in the docstring since it can shift with
    the HowNet snapshot.
See illumination_labeler_53_selftest.md for the full probe table and
the inventory-scan candidate table (every pair considered, counts,
include/exclude call and reason).

═══ 2026-08-12 (#71): RUNNABILITY ONLY — the derivation is untouched ═══
No change to THE RULE, the two poles, BRIGHT_PAIRS, the derived lexicon or any
probe expectation. The committed illumination_lexicon_hownet_53.json is BYTE-
UNCHANGED (verified before and after). Three fail-loud fixes:
  · __main__ DEFAULT now LOADS the committed lexicon and runs the probe list
    against it; re-deriving moved behind an explicit --rebuild flag. The old
    default was the rebuild — which needs the HowNet substrate that does not
    ship with this release (so __main__ could only crash here), and which
    REWRITES the committed json as a side effect of merely running the file.
  · jieba is now a guarded top-level import with a clear RuntimeError raised at
    label() time (the family's optional-import pattern, cf. trait_labelers /
    pypinyin). Token matching remains LOAD-BEARING: no substring fallback was
    added, and none may be — see the 波黑 finding above.
  · load()'s cache-missing + substrate-missing case raises ONE error naming BOTH
    hops, instead of falling through to a bare FileNotFoundError two calls deep;
    derive()/_hownet_sha256() name rebuild_manifest.tsv row `sewrl`.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

try:                     # OPTIONAL at import, REQUIRED at label() — the family's
    import jieba         # optional-import pattern (cf. trait_labelers/pypinyin).
except ImportError:      # Deriving/loading the lexicon needs no tokenizer; only
    jieba = None         # label() does, and it says so loudly at the call.

HERE = Path(__file__).resolve().parent
LEX = HERE.parent.parent / "lexical_resources/sewrl/datasets/HowNet.txt"
DARK_GLOSS = {"black", "dark", "dim", "gloomy"}  # unchanged from dark_labeler_52.py; bare-English, safe
# FULL PAIRS only, English side lowercased for matching — bare "light" would wrongly grab light|淡
# (pale, a color-value sememe, not illumination); bare "光"/"明"/"照" would wrongly grab
# polished|光, explain|说明/prove|证明/naif|不精明/Obviousness|明显性, TakeCare|照料; see module
# docstring and illumination_labeler_53_selftest.md's inventory-scan table for the full candidate
# set considered and why each of these four (and only these four) was adopted, 07-20 widening.
BRIGHT_PAIRS = {
    ("bright", "明"),        # first cut.
    ("lights", "光"),        # NEW 07-20 — fixes 光明 (own DEF is {lights|光}).
    ("brightness", "明暗"),  # NEW 07-20 — 明暗's own DEF is exactly {Brightness|明暗:host={physical|物质}}.
    ("illuminate", "照射"),  # NEW 07-20 — lamps/light fixtures/reflection/refraction/radiation-as-light.
}
PAIR_RE = re.compile(r"([A-Za-z]+)\|([^\s,:{}]+)")
LIST_FILE = HERE / "illumination_lexicon_hownet_53.json"


def _require_hownet():
    """Fail loud when the DERIVATION substrate is absent, naming the manifest row
    that fetches it (#71). HowNet.txt is the substrate for this whole labeler
    family and is not committed to the public release; deriving needs it, LOADING
    the committed lexicon beside this file does not."""
    if not LEX.exists():
        raise RuntimeError(
            f"HowNet substrate missing: {LEX}\n"
            "  Fetch it via rebuild_manifest.tsv row `sewrl` (method=manual: "
            "git github.com/thunlp/SE-WRL, which ships HowNet.txt) and unpack to "
            "lexical_resources/sewrl/.\n"
            f"  Only derive()/build_lexicon() need it — load() reads the "
            f"committed {LIST_FILE.name} and needs no substrate.")


def _hownet_sha256():
    _require_hownet()
    h = hashlib.sha256()
    with open(LEX, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def derive():
    """One pass over HowNet.txt. Returns (dark_words, bright_words) sets.
    W_C=/DEF= tracking loop shape copied from dark_labeler_52.py's derive();
    extended to test two poles per DEF line instead of one dark-only GLOSS.
    Bright pole now tests membership against the whole BRIGHT_PAIRS set
    (07-20 widening) instead of a single pair — still full-pair matching,
    still one mechanical pass, no per-word overrides."""
    _require_hownet()
    dark_words, bright_words = set(), set()
    w = None
    for ln in open(LEX, encoding="utf-8"):
        ln = ln.strip()
        if ln.startswith("W_C="):
            w = ln[4:].strip() or None
        elif ln.startswith("DEF=") and w:
            eng_toks = re.findall(r"([A-Za-z]+)\|", ln)
            if any(t.lower() in DARK_GLOSS for t in eng_toks):
                dark_words.add(w)
            pairs = PAIR_RE.findall(ln)
            if any((e.lower(), h) in BRIGHT_PAIRS for e, h in pairs):
                bright_words.add(w)
    return dark_words, bright_words


def build_lexicon():
    dark_words, bright_words = derive()
    both = dark_words & bright_words
    out = {
        "rule": {
            "dark_pole": "HowNet DEF contains a bare English sememe token in "
                         + str(sorted(DARK_GLOSS))
                         + " (unchanged from dark_labeler_52.py's GLOSS rule)",
            "bright_pole": "HowNet DEF contains one of the FULL PAIRS "
                            + str(sorted(BRIGHT_PAIRS))
                            + " (pair match throughout, never bare-English or "
                            "bare-Chinese-character; widened 07-20 from "
                            "bright|明 alone -- field owner's ruling: 'we "
                            "cannot have a checker saying 光明 is not light. "
                            "明天 can be not light and that is sane.' "
                            "light|淡 [color-value/pale] and lighting|点燃 "
                            "[combustion/ignition] were considered and "
                            "excluded; see illumination_labeler_53_selftest.md "
                            "for the full inventory-scan candidate table)",
            "membership": "a word enters the lexicon (dark list, bright list, "
                           "or both) iff ANY of its HowNet DEF records (one "
                           "word may span several NO. blocks/senses) fires "
                           "that pole",
        },
        "hownet_sha256": _hownet_sha256(),
        "n_dark": len(dark_words),
        "n_bright": len(bright_words),
        "n_both": len(both),
        "words": sorted(dark_words),
        "bright_words": sorted(bright_words),
        "both_pole_words": sorted(both),
    }
    json.dump(out, open(LIST_FILE, "w"), ensure_ascii=False, indent=1)
    return out


def load():
    """The labeler's lexicon: dark ∪ bright, read from the COMMITTED cache beside
    this file. Derives from HowNet only when that cache is absent.
    #71: when BOTH hops are missing this now raises ONE error naming both. It
    used to fall through to build_lexicon() and surface a bare FileNotFoundError
    two calls deep, which reads like a code fault rather than a missing input."""
    if LIST_FILE.exists():
        data = json.load(open(LIST_FILE, encoding="utf-8"))
    else:
        if not LEX.exists():
            raise RuntimeError(
                "illumination lexicon unavailable — BOTH hops are missing:\n"
                f"  1. committed lexicon: {LIST_FILE}\n"
                "     ABSENT. This file SHIPS with the repo — restore it from git "
                "rather than rebuilding it.\n"
                f"  2. HowNet substrate : {LEX}\n"
                "     ABSENT. Needed only to REBUILD hop 1; fetch via "
                "rebuild_manifest.tsv row `sewrl` (git github.com/thunlp/SE-WRL).\n"
                "Nothing to load, and nothing to derive from.")
        data = build_lexicon()      # NB: rebuild-on-demand REWRITES the committed file
    return set(data["words"]) | set(data["bright_words"])


_LEX = None


def label(text):
    """boolean + carriers, TOKEN-matched (jieba, her segmentation sanction):
    a lexicon word fires only as its own token — substring containment
    inverted the discrimination in the dark-only build (波黑 fired via 黑;
    caught by selftest there, fixed same sitting; that fix is preserved
    here unchanged). 叠字 rule: an XX token fires if X is in the lexicon
    (黯黯-class), mechanical. Copied near-verbatim from dark_labeler_52.py's
    label(); only the lexicon underneath (_LEX = dark ∪ bright) is wider."""
    global _LEX
    if _LEX is None:
        _LEX = load()
    if jieba is None:
        raise RuntimeError(
            "illumination_labeler_53.label() requires jieba, which is not "
            "installed here. Token matching is LOAD-BEARING, not a convenience: "
            "substring containment inverted the discrimination in the dark-only "
            "build (波黑 fired via 黑, caught by selftest and fixed the same "
            "sitting), so there is deliberately NO substring fallback. The "
            "lexicon itself needs no tokenizer — use load() for a set check.")
    hits = []
    for tok in jieba.cut(text):
        if tok in _LEX:
            hits.append(tok)
        elif len(tok) == 2 and tok[0] == tok[1] and tok[0] in _LEX:
            hits.append(tok)
    return bool(hits), hits[:5]


if __name__ == "__main__":
    # #71: the DEFAULT run READS the committed lexicon and runs the probe list
    # against it. Re-deriving is behind an explicit --rebuild flag, because that
    # path (a) requires the HowNet substrate, which does NOT ship with this repo,
    # and (b) REWRITES the committed lexicon json. The old default WAS the
    # rebuild, so on any checkout without HowNet this __main__ could only crash —
    # and on a checkout with it, merely running the file rewrote a committed
    # artifact. Probes are unchanged (same known-answer list, same expectations).
    rebuild = "--rebuild" in sys.argv
    if rebuild:
        data = build_lexicon()                  # derives AND rewrites LIST_FILE
        source = f"re-derived from HowNet, rewrote {LIST_FILE.name}"
    else:
        if not LIST_FILE.exists():
            raise SystemExit(
                f"{LIST_FILE.name} is absent. It SHIPS with this repo — restore it "
                "from git, or pass --rebuild to re-derive it from HowNet "
                "(rebuild_manifest.tsv row `sewrl`).")
        data = json.load(open(LIST_FILE, encoding="utf-8"))
        source = f"loaded committed {LIST_FILE.name} (--rebuild to re-derive)"
    total = len(set(data["words"]) | set(data["bright_words"]))
    print(f"illumination lexicon: dark={data['n_dark']} "
          f"bright={data['n_bright']} both={data['n_both']} "
          f"total={total} — {source}")
    print(f"hownet_sha256={data['hownet_sha256']}")
    print("\n-- dark side (must be unchanged) --")
    for t in ["黑", "黯黯當窗牖", "灰暗的天空", "波黑", "黑夜", "默"]:
        b, hits = label(t)
        print(f"  {t:<10} → {b}  {hits}")
    print("\n-- bright side (光明 REQUIRED True, 明天 REQUIRED False) --")
    for t in ["光明", "明天", "明亮", "明月", "明媚", "灿烂", "明暗", "皎", "皎皎",
              "光", "阳光", "月光", "灯光", "光荣", "光滑"]:
        b, hits = label(t)
        print(f"  {t:<10} → {b}  {hits}")
