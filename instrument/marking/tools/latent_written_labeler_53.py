#!/usr/bin/env python3
"""Latent-WRITTEN labeler — the 釋字-level, rule-based sensor for the
WRITTEN half of the latent-color split (field owner's ruling, 07-20, in
session). That ruling divided latent color into TWO rows:

  latent-WRITTEN   — the color lives in the VISIBLE CHARACTER. A citeable
                     list of color-charged characters exists (HowNet's
                     single-char DEF inventory); if a color character is
                     printed in the word, it is there. Pure rule, no
                     encoder, no axis. Field owner's frame, verbatim: "we
                     have a citeable list of color words, and if it is
                     there, it is there." THIS FILE.
  latent-REFERENT  — the color lives in the WORLD REFERENT (scallions are
                     green, tomatoes red). Measured by the existing
                     in-context embedding instrument (word_latent_v2_*),
                     NOT by this file. Referent is where 波兰 lands: the
                     axis fires it at z=2.60 (folk etymology 蘭色=blue),
                     but no HowNet single-char DEF for 兰 or 蘭 carries a
                     color sememe (兰={FlowerGrass|花草}, 蘭={character|
                     文字}), so the WRITTEN rule is correctly SILENT on it.
                     That silence is the split's own prediction, not a
                     miss — a word can be referent-latent without being
                     written-latent.

DERIVATION LAW (same law as the boolean-labeler family — see
illumination_labeler_53.py and dark_labeler_52.py for the lineage):
citable HowNet derivation, no dev-fitted lexicon, no FN/FP-driven edits
ever. A character is color-/illumination-charged iff its OWN single-char
HowNet DEF carries the field sememe — membership by ANY DEF record (one
char spans several senses), exactly the pole-membership rule of
illumination_labeler_53.derive(). Nothing here special-cases a word.

THE RULE (field owner's design, verbatim frame carried above). Word W
(len >= 2, CJK) FIRES latent-written for field F iff:

  (a) some character c visible in W is PRINT-CHARGED for F — c has a
      single-char HowNet DEF (c is in the single-char inventory) and that
      DEF carries an F-class sememe. A char absent from the single-char
      HowNet inventory is NOT print-charged (no fire via that char) — an
      emitted edge, never silently passed (flag carried on the word).
  (b) W's OWN word-level HowNet DEF does NOT carry F. If the word itself
      says F, that is OPEN F — the word-boolean's territory (REALIZED),
      not latent. The (a) and (b) checks use the SAME field set F: one
      rule, two uses.
  (c) with every fire, emit: the carrier char(s), the matched sememe
      pair(s), and the liveness prior + band for c-in-W, mechanized per
      word_latent_v1_52.gate_prior verbatim — trace=whole (c is visible
      in W by construction); productivity=common if c has a standalone
      HowNet entry else rare (a print-charged carrier ALWAYS has a
      standalone single-char entry by (a), so productivity is common and
      the band is recoverable for every fired carrier — mechanical
      consequence of the rule, not a tuned value); host-frequency default
      common. Weights/bands from liveness.py (LV.W_*, LV.TRACE/PROD/FREQ,
      LV.RECOVERABLE/MARGINAL), unmodified.

  EDGE, always EMITTED never silently passed: W absent from HowNet makes
  the (b) check UNKNOWN — cannot confirm the word is F-silent. If (a)
  holds, the word still fires, carrying the flag
  "word_not_in_hownet_realized_unknown".

FIELDS (both run):
  color        — FIELD_SEMEME_GLOSS["color"] from word_latent_v1_52,
                 bare-English matching (as v1_52.print_has_field): a bare
                 English sememe token in {colour, color, red, white,
                 black, green, blue, yellow, purple, brown, grey, gray}
                 appears in the DEF line. Reused verbatim.
  illumination — the WIDENED whole-field set from illumination_labeler_53,
                 REUSED verbatim: DARK pole = bare-English in {black,
                 dark, dim, gloomy}; BRIGHT pole = FULL PAIRS {bright|明,
                 lights|光, Brightness|明暗, illuminate|照射} matched as
                 pairs (bare 光/明/照 would wrongly grab polished|光,
                 explain|说明, TakeCare|照料 — full-pair matching is
                 load-bearing; see illumination_labeler_53.py docstring).
                 Both the char check (a) and the word check (b) use this
                 same two-pole set.

Source: lexical_resources/sewrl/datasets/HowNet.txt — the same substrate
as the whole family. DARK_GLOSS / BRIGHT_PAIRS are IMPORTED from
illumination_labeler_53 (stdlib-only module). load_hownet /
FIELD_SEMEME_GLOSS / gate_prior are copied VERBATIM from word_latent_v1_52
(attribution below) rather than imported: v1_52 imports the frozen-encoder
stack (numpy, sentence_transformers) at module top, and a pure-rule,
citable written-layer sensor must not depend on the encoder — reusing the
functions verbatim keeps the derivation identical while keeping this sensor
encoder-free. This file adds no lexicon of its own — it composes the
family's citable pieces into the written-layer rule.

Interface: label(word) -> {field: fire-record | None}. See
latent_written_labeler_53_selftest.md for the committed known-answer
probe table (color: 赤字/抹黑/波黑/黑夜 fire, 波兰/每天/同一 silent,
西红柿 checked; illumination: 明天/黑夜 fire, 每天 silent, 光明 realized
not latent) and the HowNet surprises (波兰's axis/written split; 赤's
minority red sense; 发扬光大 firing illumination via 光).

================================ v2 AMENDMENT (2026-07-21, dated) ================
WHY. The COLOR char-charge inventory was HowNet-single-char-only, PROVEN
INCOMPLETE: 橙 has a genuine MOE colour SENSE (「一種黃中帶著微紅的顏色」) that
HowNet lacks (HowNet 橙 = {fruit|水果}), so v1 was SILENT on 橙子 though its colour
lives in the printed 橙. Fix (field owner's frame, in session): the COLOR
char-charge becomes the UNION

    HowNet single-char colour sememe  ∪  the PROPOSED MOE colour-sense list

derived and hardened in engine/moe_color_sense_chars_53.py, loaded here
from results/moe_color_sense_chars_PROPOSED_53.json (53 chars, e.g. 橙 綠 紫 靛 …).

STATUS AS WRITTEN AT THE AMENDMENT (2026-07-21): MOE adoption PENDING. The
sensor RUNS with the union, but every fire whose ONLY source is the MOE list is
flagged: each COLOR carrier carries `provenance` in {"hownet",
"moe_color_sense_PROPOSED"}, and the fire carries `moe_provenance_only` = True
iff EVERY carrier is MOE-exclusive. The field owner adopts / amends / rejects the
MOE list; until then MOE-only fires are PROPOSED.
  ↳ SUPERSEDED THE SAME DAY (2026-07-21, her ruling: "Keep the MOE-list as the
    color lexical list then"): the list is ADOPTED. The provenance marking
    described above is UNCHANGED and still emitted on every fire — `provenance`
    and `moe_provenance_only` are now an AUDIT TRAIL rather than a gate, and the
    artifact keeps its PROPOSED-era filename and provenance string. Full ruling
    and her 黎 aliveness note: the MOE status block below load_moe_color().

SCOPE (narrow; everything else stays v1-verbatim):
  - COLOR carrier test only. A char is a colour carrier iff it has a HowNet
    single-char colour sememe (as v1) OR it is in MOE_COLOR_SET. The MOE branch is
    INDEPENDENT of the HowNet single-char inventory gate, so an archaic MOE-only
    char (盭 袾 赮 韎 騂 髹 …) with no HowNet entry still fires.
  - ILLUMINATION: unchanged (no MOE union).
  - Realized check (b): unchanged — the word's own HowNet DEF only. The MOE list
    charges CHARS, not word-openness, so it does not enter the realized test.
  - 皓 ruling honoured: 皓 is NOT in the MOE list (its 潔白/雪白/純白 are
    quality-of-white). REPORTED, not patched: HowNet's single-char 皓 carries
    DEF={white|白} (NO.=208886), so 皓月 STILL fires colour via the HowNet branch
    (provenance "hownet") exactly as v1 — the union CANNOT subtract a HowNet
    sememe. The ruling scoped the MOE DERIVATION (which excluded 皓); it does not,
    and the union cannot, remove 皓's pre-existing HowNet-white firing. The v2
    selftest asserts only that 皓 does not fire via the MOE addition.
  - Script: MOE is traditional, HowNet / eval inputs are simplified; MOE_COLOR_SET
    is normalised to include simplified forms (紅→红 綠→绿 …) so the union is
    script-robust. 橙 is script-invariant.

═══ 2026-08-12 (#71): HYGIENE ONLY — no rule, no lexicon, no expectation moved ═══
  · PAIR_RE is now IMPORTED from illumination_labeler_53 instead of copy-pasted.
    The two pattern strings were verified byte-identical BEFORE the copy was
    dropped, so the bright-pole matching here and there is provably one regex.
  · load_hownet() gains a one-line existence guard naming rebuild_manifest.tsv
    row `sewrl`; the v1_52 verbatim copy is otherwise byte-unchanged.
  · MOE_ADOPTION — a module-level string that nothing in the repo read — became
    the status comment it always was. The v2-amendment STATUS paragraph above is
    annotated as superseded by her same-day adoption ruling; neither text is
    deleted, both dated decisions stand on the record.
NOT VERIFIED BY RUN: this sensor cannot execute in the public checkout (HowNet
absent by design), so the selftests below are UNRUN here. Verified instead: AST
parse + `import latent_written_labeler_53` — import is side-effect-free, Labeler
is constructed only on the first label() call, never at import time.
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))                       # illumination_labeler_53, liveness

from illumination_labeler_53 import DARK_GLOSS, BRIGHT_PAIRS, PAIR_RE
import liveness as LV

# ---- copied VERBATIM from engine/word_latent_v1_52.py (see docstring for why
#      copied and not imported: v1_52's encoder-stack top-level imports). This
#      copy is DELIBERATE and stays. #71 touched it in exactly one way: a
#      one-line existence guard at the top of load_hownet() (below), so a missing
#      substrate reports itself instead of raising a bare FileNotFoundError. The
#      parse loop, FIELD_SEMEME_GLOSS and gate_prior are byte-unchanged. ----
LEX = HERE.parent.parent / "lexical_resources"
HOWNET = LEX / "sewrl/datasets/HowNet.txt"

# FIELD_SEMEME_GLOSS (v1_52 lines 40-44), verbatim:
FIELD_SEMEME_GLOSS = {
    "color": {"colour", "color", "red", "white", "black", "green", "blue",
              "yellow", "purple", "brown", "grey", "gray"},
    "dark":  {"black", "dark", "dim", "gloomy"},
}

def load_hownet():
    """char/word → list of DEF strings; from the vendored HowNet.txt.
    Copied verbatim from word_latent_v1_52.load_hownet() (plus the #71 guard)."""
    if not HOWNET.exists():                                   # #71 fail-loud guard
        raise RuntimeError(
            f"HowNet substrate missing: {HOWNET}\n"
            "  This sensor IS the HowNet single-char DEF inventory — with no "
            "substrate there is nothing to derive from and no fallback exists "
            "(a hand-authored char list would violate the derivation law above).\n"
            "  Fetch it via rebuild_manifest.tsv row `sewrl` (method=manual: "
            "git github.com/thunlp/SE-WRL, which ships HowNet.txt) and unpack to "
            "lexical_resources/sewrl/.")
    defs = defaultdict(list)
    w = None
    for ln in open(HOWNET, encoding="utf-8"):
        ln = ln.strip()
        if ln.startswith("W_C="):
            w = ln[4:].strip() or None
        elif ln.startswith("DEF=") and w:
            defs[w].append(ln[4:].strip())
    return defs

def gate_prior(defs, char):
    """trace=whole (character visible in host by construction);
    productivity: standalone HowNet entry exists → common, else rare;
    host frequency: default 'common' (conservative).
    Copied verbatim from word_latent_v1_52.gate_prior()."""
    trace = LV.TRACE["whole"]
    prod = LV.PROD["common"] if defs.get(char) else LV.PROD["rare"]
    freq = LV.FREQ["common"]
    return LV.W_TRACE * trace + LV.W_PROD * prod + LV.W_FREQ * freq
# ---- end verbatim copy ----

CJK = re.compile(r"[㐀-鿿]")
COLOR_GLOSS = FIELD_SEMEME_GLOSS["color"]           # reused verbatim
# PAIR_RE is IMPORTED from illumination_labeler_53 (top of file), not re-declared.
# #71: this file carried its own copy annotated "same shape as
# illumination_labeler_53.PAIR_RE"; the two pattern strings were confirmed
# byte-identical before the copy was dropped, so the bright-pole pair matching
# here and there is now provably ONE regex rather than two that agree today.

FIELDS = ("color", "illumination")

# ---- v2 AMENDMENT: PROPOSED MOE colour-sense list (union with HowNet) ----
import json as _json

# ---- MOE COLOUR-LIST STATUS: ADOPTED ----------------------------------------
# Her word, 2026-07-21: "Keep the MOE-list as the color lexical list then." The
# 53-char list stands as print. Her aliveness note filed with the ruling: 黎 is
# fading as a COMMON color name (her Taobao test — absent from live commercial
# color vocabulary) — a LIVENESS datum, not an exclusion: 黎 stays citable print;
# its sedimentation-slope position is the liveness index's business. Provenance
# marking retained as audit trail, no longer gating.
# #71: this was a bare module-level string `MOE_ADOPTION = "ADOPTED"` that
# NOTHING read — not this file, not any other file in the repo (verified by
# grep). It was a status note wearing the costume of a flag; it is recorded here
# as a comment so no reader mistakes it for a switch. The union it describes is
# unconditional in load_moe_color() and always was.
MOE_JSON = HERE.parent.parent / "engine" / "results" / "moe_color_sense_chars_PROPOSED_53.json"
# MOE is traditional; HowNet/eval are simplified. Normalise the differing chars
# among the 53 so the union catches simplified eval forms.
_TRAD2SIMP = {"紅": "红", "綠": "绿", "藍": "蓝", "黃": "黄", "蒼": "苍", "絳": "绛",
              "緋": "绯", "縞": "缟", "緇": "缁", "緗": "缃", "緹": "缇", "黲": "黪",
              "蠟": "蜡", "騂": "骍", "盧": "卢"}


def load_moe_color():
    """char -> matched MOE colour-sense snippet (verbatim, citation-stripped),
    normalised to include simplified forms. Empty dict if the PROPOSED list is
    absent (sensor degrades to v1 colour — flagged by empty MOE_COLOR_SET)."""
    out = {}
    if MOE_JSON.exists():
        data = _json.load(open(MOE_JSON, encoding="utf-8"))
        for c, rec in data.get("chars", {}).items():
            snip = rec.get("matched_snippet") or rec.get("matched_sense") or ""
            out[c] = snip
            if c in _TRAD2SIMP:
                out[_TRAD2SIMP[c]] = snip
    return out


def _def_field_pairs(def_line, field):
    """Return the list of matched (english, chinese) sememe pairs in one
    DEF line for `field`, using that field's citable rule:
      color        — bare-English token in COLOR_GLOSS (chinese side kept
                     for the emit, but matching is bare-English as v1_52).
      illumination — bare-English in DARK_GLOSS (dark pole) OR full pair
                     in BRIGHT_PAIRS (bright pole).
    Empty list = this DEF line does not carry the field."""
    pairs = PAIR_RE.findall(def_line)
    out = []
    if field == "color":
        for e, h in pairs:
            if e.lower() in COLOR_GLOSS:
                out.append((e, h))
    elif field == "illumination":
        for e, h in pairs:
            if e.lower() in DARK_GLOSS:                       # dark pole, bare-English
                out.append((e, h))
            elif (e.lower(), h) in BRIGHT_PAIRS:              # bright pole, FULL PAIR
                out.append((e, h))
    return out


def _has_field(defs, unit, field):
    """True iff ANY DEF record of `unit` (char or word) carries `field`."""
    return any(_def_field_pairs(d, field) for d in defs.get(unit, []))


def _field_pairs_for_unit(defs, unit, field):
    """Deduped list of matched sememe pairs across all DEF records of `unit`."""
    seen, out = set(), []
    for d in defs.get(unit, []):
        for pr in _def_field_pairs(d, field):
            if pr not in seen:
                seen.add(pr)
                out.append(list(pr))
    return out


class Labeler:
    def __init__(self, defs=None, single_chars=None, moe_color=None):
        self.defs = defs if defs is not None else load_hownet()
        # single-char HowNet inventory: chars that have their own W_C entry
        self.single_chars = single_chars if single_chars is not None else {
            w for w in self.defs if len(w) == 1 and CJK.match(w)
        }
        # v2: PROPOSED MOE colour-sense list (char -> matched snippet), unioned
        # with HowNet for the COLOR field only.
        self.moe_color = moe_color if moe_color is not None else load_moe_color()

    def label_field(self, word, field):
        """One field's fire-record, or None if the word does not fire.
        Emits carriers, matched pairs, liveness band, realized flag, and
        edge flags per the rule. v2: COLOR carriers additionally fire from the
        MOE list (provenance moe_color_sense_PROPOSED when that is the ONLY
        source); illumination and the realized check are v1-verbatim."""
        if len(word) < 2 or not any(CJK.match(c) for c in word):
            return None
        carriers = []
        for c in dict.fromkeys(word):                 # preserve order, dedupe
            if not CJK.match(c):
                continue
            # HowNet single-char branch (v1): print-charged iff in the single-char
            # inventory AND its DEF carries the field.
            pairs = _field_pairs_for_unit(self.defs, c, field) if c in self.single_chars else []
            # MOE branch (v2, COLOR only): independent of the HowNet inventory gate.
            moe_snip = self.moe_color.get(c) if field == "color" else None
            if not pairs and moe_snip is None:        # not charged via either source
                continue
            prior = gate_prior(self.defs, c)          # trace=whole; prod=common iff any HowNet entry
            band = "recoverable" if prior >= LV.RECOVERABLE else (
                "marginal" if prior >= LV.MARGINAL else "dead")
            provenance = "hownet" if pairs else "moe_color_sense_PROPOSED"
            car = {
                "char": c,
                "pairs": pairs,
                "provenance": provenance,
                "liveness_prior": round(prior, 4),
                "liveness_band": band,
            }
            if provenance == "moe_color_sense_PROPOSED":
                car["moe_sense"] = moe_snip           # verbatim, citation-stripped
            carriers.append(car)
        if not carriers:                              # (a) fails
            return None
        moe_only = all(c["provenance"] == "moe_color_sense_PROPOSED" for c in carriers)
        # (b): word-level realized check
        in_hownet = word in self.defs
        realized = _has_field(self.defs, word, field)
        edge_flags = []
        if not in_hownet:
            edge_flags.append("word_not_in_hownet_realized_unknown")
        elif realized:
            # word itself carries F -> OPEN F, not latent-written
            return {
                "field": field,
                "fired": False,
                "realized": True,
                "carriers": carriers,
                "moe_provenance_only": moe_only,
                "edge_flags": edge_flags,
                "note": "realized (word DEF carries field) -> OPEN, not latent-written",
            }
        return {
            "field": field,
            "fired": True,
            "realized": False,
            "carriers": carriers,
            "moe_provenance_only": moe_only,
            "edge_flags": edge_flags,
        }

    def label(self, word):
        return {f: self.label_field(word, f) for f in FIELDS}


_L = None


def label(word):
    global _L
    if _L is None:
        _L = Labeler()
    return _L.label(word)


# ---- committed selftests (known answers; fail = report, do not patch) ----
def _selftests():
    L = Labeler()
    ok = True
    results = []

    def chk(name, cond, detail=""):
        nonlocal ok
        ok = ok and cond
        results.append((("PASS" if cond else "FAIL"), name, detail))

    def carrier_chars(rec):
        return [c["char"] for c in rec["carriers"]] if rec else []

    # -- color --
    for w, car in [("赤字", "赤"), ("抹黑", "黑"), ("波黑", "黑"), ("黑夜", "黑")]:
        r = L.label_field(w, "color")
        chk(f"color {w} FIRES carrier {car}",
            bool(r) and r["fired"] and car in carrier_chars(r),
            detail=f"got {carrier_chars(r)} fired={r['fired'] if r else None}")
    for w in ["波兰", "每天", "同一"]:
        r = L.label_field(w, "color")
        chk(f"color {w} SILENT", r is None, detail=f"got {r}")
    # 西红柿: expected FIRES 红 IFF word-DEF color-silent — check and report
    xr = L.label_field("西红柿", "color")
    xdefs = L.defs.get("西红柿", [])
    xfires = bool(xr) and xr["fired"] and "红" in carrier_chars(xr)
    chk("color 西红柿 FIRES carrier 红 (word-DEF color-silent)",
        xfires, detail=f"word DEFs={xdefs} -> carrier {carrier_chars(xr)}")

    # -- illumination --
    r = L.label_field("明天", "illumination")
    chk("illum 明天 FIRES carrier 明 (bright)",
        bool(r) and r["fired"] and "明" in carrier_chars(r),
        detail=f"got {carrier_chars(r)}")
    r = L.label_field("每天", "illumination")
    chk("illum 每天 SILENT", r is None, detail=f"got {r}")
    r = L.label_field("光明", "illumination")
    chk("illum 光明 does NOT fire latent (word-DEF lights|光 -> REALIZED, open)",
        bool(r) and r["fired"] is False and r["realized"] is True,
        detail=f"got fired={r['fired'] if r else None} realized={r['realized'] if r else None}")
    r = L.label_field("黑夜", "illumination")
    chk("illum 黑夜 FIRES carrier 黑 (dark)",
        bool(r) and r["fired"] and "黑" in carrier_chars(r),
        detail=f"got {carrier_chars(r)}")

    # -- v2 AMENDMENT selftests (MOE colour-sense union) --
    def prov(rec, ch):
        for c in (rec["carriers"] if rec else []):
            if c["char"] == ch:
                return c.get("provenance")
        return None

    # 橙子 must now FIRE colour via the MOE list (v1 was SILENT: HowNet 橙={fruit}).
    o = L.label_field("橙子", "color")
    chk("v2 color 橙子 FIRES carrier 橙 via MOE (provenance moe_color_sense_PROPOSED)",
        bool(o) and o["fired"] and "橙" in carrier_chars(o)
        and prov(o, "橙") == "moe_color_sense_PROPOSED" and o.get("moe_provenance_only") is True,
        detail=f"got {carrier_chars(o)} prov(橙)={prov(o,'橙')} moe_only={o.get('moe_provenance_only') if o else None}")

    # 红绿灯 unchanged: FIRES via HowNet 红/绿 (both hownet-provenance, not MOE).
    rg = L.label_field("红绿灯", "color")
    chk("v2 color 红绿灯 FIRES carriers 红+绿 (hownet, unchanged)",
        bool(rg) and rg["fired"] and "红" in carrier_chars(rg) and "绿" in carrier_chars(rg)
        and prov(rg, "红") == "hownet" and prov(rg, "绿") == "hownet"
        and rg.get("moe_provenance_only") is False,
        detail=f"got {carrier_chars(rg)} prov={[(c['char'],c['provenance']) for c in rg['carriers']] if rg else None}")

    # 皓 ruling: 皓 must NOT be a MOE-added carrier. (It is absent from the MOE
    # list; the derivation excluded its 潔白/雪白/純白 quality-white senses.)
    chk("v2 皓 NOT in MOE colour list (derivation excluded 潔白/雪白/純白)",
        "皓" not in L.moe_color, detail=f"皓 in moe_color = {'皓' in L.moe_color}")
    # And any 皓 colour fire must be HowNet-white, NOT via the MOE addition.
    hm = L.label_field("皓月", "color")
    chk("v2 皓月 does NOT fire colour via MOE (皓 carrier is hownet-white if present, never moe)",
        (hm is None) or (prov(hm, "皓") in (None, "hownet")),
        detail=(f"REPORTED: 皓月 fires={hm['fired'] if hm else None} via 皓 prov={prov(hm,'皓')} "
                f"(HowNet 皓 DEF={{white|白}} — pre-existing v1 firing, union cannot subtract it)"))

    return ok, results


if __name__ == "__main__":
    ok, results = _selftests()
    print("== latent-written selftests ==")
    for status, name, detail in results:
        print(f"  [{status}] {name}")
        if status == "FAIL" or "西红柿" in name:
            print(f"          {detail}")
    print(f"\n{'ALL PASS' if ok else 'FAILURES PRESENT'}")
