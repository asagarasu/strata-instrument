#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
§8 DEMONSTRATION SCORING — the LATENT rows (written + referent-thin).
Translation-studies instrument. Sibling of
deterministic-descriptive-fields/. BUILD + SMOKE + DRY here; the real
scoring run (--run) is fired by the orchestrator AFTER her review.

═══ THE LAW (reports/methodology_amendment_0721_53.md §2/§4; #53) ═══
deterministic-F = descriptive-F + latent-F. The descriptive row is the
sibling folder. THIS folder scores the LATENT rows:

  LATENT-WRITTEN — the field rides the visible written form (the char 赤
    inside 赤字; the etymon sidus inside "consider"). CLAIM = a conjunction
    of THREE severally-warranted checks, NO separate degree credential
    (her ruling 07-21, §2):
      (1) SCALAR-SAYS-FIELD  — the battery-credentialed descriptive axis,
          read at the line (the descriptive scorer's law). Needs the
          encoder → applied at --run only. In --dry/--smoke this leg is
          PENDING (reported, not evaluated) — the descriptive --dry has the
          same shape (fires without the scalar).
      (2) BOOLEAN-SILENT     — the descriptive word-level field boolean does
          NOT fire on the line (reused verbatim from the descriptive scorer:
          trait_labelers / illumination_labeler_53). Citation.
      (3) CARRIER-PRESENT    — a character in the line is field-charged per
          the CITABLE single-char inventories, AND the carrier's own word is
          field-silent in its own dictionary entry (the written sensor's
          (a)∧(b); §2 "the carrier is there and its dictionary entry carries
          the field"). Citation-by-inspection.
    A --dry/--smoke "written-row fire" = (2)∧(3) [boolean side]; (1) pending.

  LATENT-REFERENT (COLOUR only — the one credentialed meter) — the field
    rides world-knowledge of the referent. TRIGGER = a citable referent
    account (the committed definition-witness json, where covered); CCFD-
    covered words are TRUTH-side context only, NEVER triggers (§4, her
    07-21 evening ruling: a norm set credentials OR triggers, never both).
    DEGREE = the credentialed in-context meter
    (engine/word_latent_v5_referent_color_54.py: color_salience_
    axis_48.npz key "axis", LaBSE, attempt-6 F1 .800 precision 1.000 floor
    .70 THIN n=6, 2026-07-22) — its word-grain substitution protocol does
    NOT re-run here; per-line degree RIDES the line colour scalar (same
    axis/encoder law, read at line grain). Kept honest and thin.
    CITATION NOTE (accuracy pass #71): word_latent_v5_referent_color_54.py is
    NOT SHIPPED in this repo. The published record of that meter is its
    OUTPUT — engine/results/word_latent_v5_referent_color_54.json (plus the
    wide-pool rerun word_latent_v7_wide_referent_color_54.json, and the
    word_grain_referent_pass_* files that name it as "machinery … imported
    verbatim"). The citation stands as the credential's address; only the
    source file is absent.

═══ CARRIERS (the CITABLE single-char inventories) ═══
  colour       HowNet ∪ MOE-53  (latent_written_labeler_53 v2 — the written
               sensor of record; carriers + provenance + liveness emitted)
  illumination HowNet-only      (her ruling; latent_written_labeler_53 illum
               side, no MOE union)
  sound        HowNet ∪ her-sanctioned 声-amendment
               (engine/results/hownet_sound_chars_54_amended.json — A2)
  plant        any-position 259 (her 連理枝 ruling;
               engine/results/hownet_plant_chars_54.json)
  temporal     head-sememe 123  (engine/results/hownet_temporal_chars_54.json — A1)
  en           Skeat etymon chains (engine/etym_chains_v1_52.py) —
               FIELD_TERMS_EN covers colour + dark(→illumination) + star;
               sound/plant/temporal have NO en-etymon list → UNAVAILABLE.
  de / jp      NO citable char/etymon inventory → UNAVAILABLE (declared,
               never fabricated).

═══ SURVIVAL / COMPENSATION (the written→descriptive detector, §1) ═══
  Written meaning dies at a script boundary unless the translator
  COMPENSATES, so a written-latent survival score is a compensation-event
  detector. The written-row poem states feed rubric_compare's LATENT SLOTS
  for the 4 en↔zh pairs (poem grain, F1):
      src written-latent → tr DESCRIPTIVE active  = COMPENSATION-candidate
                                                    (latent→active = REVIVAL)
      src written-latent → tr written-latent       = survival (LATENT-CARRY)
      src written-latent → tr nothing              = loss (LATENT-UNREALIZED)
  Supplying both latent slots UNLOCKS the REVIVAL / PARTIAL-LOSS / LATENT-*
  cells the descriptive row folds away (its F4). In --dry the latent states
  are the boolean side (checks 2∧3), so previews are boolean-side only.

═══ FLAGGED OPEN DETAILS (minimal readings) ═══
  L-F1  FOLDER NAME. The descriptive README (its F4, §7) reserves the
        sibling name `deterministic-latent-written-fields/`; the build task
        names `deterministic-latent-written-fields/`. Built under the TASK name
        (this folder also carries the referent-thin row, so "-latent-" is
        the wider-correct name). Flagged for her rename if wanted.
  L-F2  CHECK-1 DEFERRAL. --dry/--smoke have no encoder → the scalar gate
        (check 1) is PENDING; written-row fires reported are the boolean
        side (checks 2∧3). --run applies check 1 (the descriptive axis at
        the line) and only then is the three-check conjunction complete.
        Same discipline as the descriptive --dry.
  L-F3  REALIZED-GATE LAYERING. Check 2 (descriptive boolean silent, line
        grain) uses trait_labelers/illumination (the descriptive lexicons).
        The written sensor's own (b) uses the WORD's HowNet DEF. They are
        different lexicons; a word could be HowNet-realized yet trait-silent
        or vice versa. MINIMAL READING: require BOTH — line-level trait
        silence AND per-carrier-word HowNet-DEF silence (the conservative
        union; fewer false latent fires). Emitted per fire.
  L-F4  en ILLUMINATION check-2. illumination has NO en descriptive boolean
        (zh-only, descriptive F2). So en illumination-written cannot
        complete the conjunction; en 'dark' Skeat chains are reported
        INFORMATIONAL, not counted as completed en written-latent fires.
        en written-latent survival-eligible field = COLOUR.
  L-F5  CONSIDER/STAR EXHIBIT. Skeat FIELD_TERMS_EN has color/dark/STAR;
        'star' is the founding example (sidus inside consider) but is NOT
        one of the five scored fields → surfaced as a fixed EXHIBIT,
        informational, outside the survival table.
  L-F6  REFERENT TRIGGER EXTRACTION. The committed witness json is a
        diagnostic dump, not a word→fires table. Trigger words are extracted
        best-effort (recursive walk: a word-record with a truthy colour
        signal). Thin by mandate; where a word is uncovered by the witness
        there is NO referent trigger (declared, never fabricated). CCFD
        (lexical_resources/impression_norms/ccfd_2021) is TRUTH-side context
        only and is CITED, not enumerated (openpyxl absent in venv).

Reuses VERBATIM from ../deterministic-descriptive-fields/
score_descriptive_fields.py: corpus loading (BOARD + local tier),
verse_lines, F9 redaction, boolean_states (the descriptive booleans =
check 2), maskable_units, load_axes/project/embed_inventory/scalar_readings
(the scalar leg = check 1), poem_inventory, sha256, SEED, determinism
discipline. Redaction law F9 applies verbatim.
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------- paths
HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent                       # repo root (instrument/)
DESC = REPO / "publishable" / "deterministic-descriptive-fields"
PROTO = REPO / "engine"
RESULTS = PROTO / "results"
MARK_TOOLS = REPO / "marking" / "tools"
LEX = REPO / "lexical_resources"

# import the descriptive scorer as the canonical source of corpus loading,
# F9 redaction, booleans (check 2), and the scalar leg (check 1). Its own
# module-level path setup (MARK_TOOLS, PROTO) is REPO-relative, so it resolves
# correctly from here.
sys.path.insert(0, str(DESC))
sys.path.insert(0, str(MARK_TOOLS))
sys.path.insert(0, str(PROTO))
import score_descriptive_fields as D            # noqa: E402

SEED = D.SEED
FIELDS5 = ["color", "illumination", "sound", "plant", "temporal"]


# ============================================================ carriers
def _load_json(path):
    return json.load(open(path, encoding="utf-8"))


# -- zh single-char carrier inventories (the CITABLE lists) --
def load_zh_carriers():
    """field -> set of charged single chars, from the citable inventories."""
    inv = {}
    # sound: HowNet ∪ her-sanctioned 声-amendment (A2)
    sd = _load_json(RESULTS / "hownet_sound_chars_54_amended.json")
    inv["sound"] = set(sd["chars"].keys())
    inv["_sound_amended_token_set"] = set(sd["amended_token_set"])
    # plant: any-position 259 (her 連理枝 ruling)
    pl = _load_json(RESULTS / "hownet_plant_chars_54.json")
    inv["plant"] = set(pl["charged_chars_any_position"])
    # temporal: head-sememe (A1)
    tp = _load_json(RESULTS / "hownet_temporal_chars_54.json")
    inv["temporal"] = set(tp["charged_chars"])
    return inv


# word-realized (b) sememe rules for sound/plant/temporal (colour/illum use
# the labeler's own (b)). PAIR / head-sememe matching mirrors the char rules.
PLANT_SEMEMES = {"FlowerGrass|花草", "plant|植物", "tree|树"}         # any-position (her plant ruling)
TEMPORAL_TOKENS = {"time|时间", "TimeLong|长时间", "TimeShort|短时间"}  # head-sememe
import re as _re
_RE_SEM = _re.compile(r"[A-Za-z~][A-Za-z0-9 ]*\|[^\s{}:=,]+")


def _head(def_line):
    toks = [t for t in _RE_SEM.findall(def_line) if not t.startswith("~")]
    return toks[0] if toks else None


class ZhWritten:
    """The zh written-latent sensor: colour/illumination via the sensor of
    record (latent_written_labeler_53 v2), sound/plant/temporal via the
    citable single-char inventories + a HowNet-word-DEF realized (b) guard."""

    def __init__(self):
        import latent_written_labeler_53 as LW
        self.LW = LW
        self.labeler = LW.Labeler()               # HowNet defs + MOE-53 colour union
        self.defs = self.labeler.defs             # char/word -> [DEF...]
        self.single = self.labeler.single_chars
        self.carriers = load_zh_carriers()
        self.sound_pairs = self.carriers["_sound_amended_token_set"]

    def _word_realized(self, word, field):
        """word's OWN HowNet DEF carries the field (the (b) guard)."""
        for d in self.defs.get(word, []):
            if field == "plant":
                if any(p in d for p in PLANT_SEMEMES):
                    return True
            elif field == "temporal":
                if _head(d) in TEMPORAL_TOKENS:
                    return True
            elif field == "sound":
                if any(p in d for p in self.sound_pairs):
                    return True
        return False

    def word_fire(self, word, field):
        """Fire-record for one zh word × field, or None. colour/illum defer to
        the sensor of record; sound/plant/temporal use inventory + (b)."""
        if field in ("color", "illumination"):
            r = self.labeler.label_field(word, field)
            if r and r.get("fired"):
                return {"carriers": [c["char"] for c in r["carriers"]],
                        "receipts": r["carriers"], "sensor": "latent_written_labeler_53_v2",
                        "word_hownet_realized": False}
            return None
        # sound / plant / temporal
        if len(word) < 2 or not any(D.CJK.match(c) for c in word):
            return None
        cars = [c for c in dict.fromkeys(word)
                if D.CJK.match(c) and c in self.carriers[field]]
        if not cars:
            return None                            # (a) carrier-present fails
        if self._word_realized(word, field):
            return None                            # (b) word openly carries field -> OPEN, not latent
        return {"carriers": cars, "receipts": [{"char": c} for c in cars],
                "sensor": f"hownet_single_char_inventory[{field}]",
                "word_hownet_realized": False}


class EnWritten:
    """The en written-latent sensor: Skeat etymon chains. FIELD_TERMS_EN
    covers colour + dark(→illumination) + star. sound/plant/temporal have no
    en-etymon list → UNAVAILABLE."""

    FIELD_MAP = {"color": "color", "illumination": "dark"}   # star handled as exhibit
    EN_AVAILABLE = {"color", "illumination"}

    def __init__(self):
        import etym_chains_v1_52 as EC
        self.EC = EC
        self.entries = EC.skeat_entries()

    def word_fire(self, word, field):
        term = self.FIELD_MAP.get(field)
        if term is None:
            return None                            # sound/plant/temporal: no en-etymon list
        w = _re.sub(r"[^A-Za-z]", "", word)
        if len(w) < 3:
            return None
        r = self.EC.en_chain(self.entries, w, term)
        if r.get("found"):
            return {"carriers": [w], "etymon_terms": r["terms"],
                    "citation": r["citation"], "sensor": "skeat_etym_chain",
                    "entry_head": r.get("entry_head", "")[:80]}
        return None

    def consider_exhibit(self):
        r = self.EC.en_chain(self.entries, "consider", "star")
        return {"word": "consider", "field_outside_shelf": "star",
                "found": r.get("found"), "terms": r.get("terms"),
                "citation": r.get("citation"),
                "note": ("L-F5: the founding example (sidus/star inside consider); "
                         "'star' is OUTSIDE the five-field shelf — informational exhibit.")}


# ============================================================ written row
def _line_words(line, lang):
    """word units for the written sensor. zh -> jieba; en/latin -> whitespace
    alpha tokens. (Same tokenisation family as the descriptive maskable_units.)"""
    if D.CJK.search(line) and not _re.search(r"[A-Za-z]", line):
        import jieba
        return [t for t in jieba.cut(line) if t.strip()]
    if D.CJK.search(line):                         # mixed — take both
        import jieba
        zh = [t for t in jieba.cut(line) if t.strip()]
        return zh
    return [t for t in _re.findall(r"[A-Za-z][A-Za-z'’-]*", line)]


def written_row_line(line, lang, zh_sensor, en_sensor):
    """Per field: the boolean-side written-latent state at one line.
    checks: (2) boolean-silent [descriptive boolean], (3) carrier-present
    [∧ word (b) silent]. (1) scalar PENDING (--run).
    Returns {field: {available, boolean_silent, carrier_present, fires_bool,
    carriers, receipts, checks_note}}."""
    out = {}
    bstate = D.boolean_states(line, lang)          # check 2 source (verbatim)
    if lang == "zh":
        words = _line_words(line, "zh")
        for f in FIELDS5:
            bsil = (bstate[f]["fires"] is False)   # descriptive boolean silent on the line
            fires = []
            for w in words:
                fr = zh_sensor.word_fire(w, f)
                if fr:
                    fires.append({"word": w, **fr})
            carrier = bool(fires)
            out[f] = {
                "available": True,
                "boolean_silent": bsil,            # check 2
                "carrier_present": carrier,        # check 3 (a∧b)
                "fires_bool": bool(bsil and carrier),
                "scalar_check1": "PENDING (--run: descriptive axis at line)",
                "carriers": sorted({c for fr in fires for c in fr["carriers"]}),
                "fires": fires,
            }
    elif lang == "en":
        words = _line_words(line, "en")
        for f in FIELDS5:
            if f not in en_sensor.EN_AVAILABLE:
                out[f] = {"available": False,
                          "reason": "no en-etymon inventory (Skeat FIELD_TERMS covers colour/dark only)"}
                continue
            # L-F4: illumination has no en descriptive boolean -> can't complete check 2
            if f == "illumination":
                fires = [{"word": w, **fr} for w in words
                         if (fr := en_sensor.word_fire(w, f))]
                out[f] = {"available": True, "boolean_silent": None,
                          "informational_only": True,
                          "reason": "L-F4: no en illumination descriptive boolean (zh-only) -> not survival-counted",
                          "carriers": sorted({c for fr in fires for c in fr["carriers"]}),
                          "fires": fires}
                continue
            bsil = (bstate[f]["fires"] is False)
            fires = [{"word": w, **fr} for w in words if (fr := en_sensor.word_fire(w, f))]
            carrier = bool(fires)
            out[f] = {"available": True, "boolean_silent": bsil,
                      "carrier_present": carrier,
                      "fires_bool": bool(bsil and carrier),
                      "scalar_check1": "PENDING (--run: descriptive axis at line)",
                      "carriers": sorted({c for fr in fires for c in fr["carriers"]}),
                      "fires": fires}
    else:  # de / jp
        for f in FIELDS5:
            out[f] = {"available": False,
                      "reason": "UNAVAILABLE — no citable char/etymon inventory for this language (declared)"}
    return out


# ============================================================ referent row (colour only, thin)
_WITNESS_WORDS = None


def _witness_color_words():
    """Colour-witness word set (L-F6 lineage). zh = the MOE witness of record
    (definition_witness_zh_PROPOSED_53, recursive walk unchanged). en = the
    UNIFIED PROSE witness of record since 07-26 (definition_witness_v2_PROPOSED_53
    run_b_*/run_a sections, explicit `colorful` flags — amendment §2's
    GCIDE+Wiktextract witness; was: the superseded WordNet-gloss en v1 file,
    manual §7.22). v1-en fallback is DECLARED, never silent."""
    global _WITNESS_WORDS
    if _WITNESS_WORDS is not None:
        return _WITNESS_WORDS
    words = set()

    def walk(node):
        if isinstance(node, dict):
            sig = (node.get("colorful_gloss") is True
                   or node.get("colorful_full") is True
                   or node.get("color_families_gloss")
                   or node.get("color_families_full")
                   or node.get("color_hits_gloss"))
            if sig:
                for k in ("query", "word", "headword", "resolved_form", "zh", "en"):
                    v = node.get(k)
                    if isinstance(v, str) and v:
                        words.add(v)
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    p_zh = RESULTS / "definition_witness_zh_PROPOSED_53.json"
    if p_zh.exists():
        walk(_load_json(p_zh))

    p_v2 = RESULTS / "definition_witness_v2_PROPOSED_53.json"
    if p_v2.exists():
        v2 = _load_json(p_v2)
        for sec in ("run_b_pool_en_color", "run_b_illum_en", "run_a_coco"):
            for w, rec in (v2.get(sec) or {}).items():
                if isinstance(rec, dict) and rec.get("colorful"):
                    words.add(w)
    else:
        p_en1 = RESULTS / "definition_witness_en_PROPOSED_53.json"
        if p_en1.exists():
            print("[latent] WARN: v2 prose witness absent — DECLARED fallback to "
                  "the superseded WordNet-gloss en v1 witness (manual §7.22)")
            walk(_load_json(p_en1))
    _WITNESS_WORDS = words
    return words


def referent_row_line(line, lang):
    """COLOUR-only referent flags (thin). Trigger = a word in the line whose
    definition-witness fires colour (where covered). Degree rides the line
    scalar (the .800 THIN meter's axis/encoder law at line grain)."""
    if lang not in ("zh", "en"):
        return {"available": False,
                "reason": "referent colour row: witness covers zh/en only here"}
    wit = _witness_color_words()
    words = _line_words(line, lang)
    hits = sorted({w for w in words if w in wit})
    return {
        "available": True,
        "field": "color",
        "referent_trigger_words": hits,
        "trigger_source": "committed definition-witness json (where covered)",
        "ccfd_context_only": ("lexical_resources/impression_norms/ccfd_2021 — TRUTH-side "
                              "context, NEVER a trigger; cited not enumerated (openpyxl absent)"),
        "degree": ("credentialed meter EXISTS — word_latent_v5_referent_color_54.py "
                   "(color_salience_axis_48.npz key 'axis', LaBSE; attempt-6 F1 .800 "
                   "precision 1.000 floor .70 THIN n=6, 2026-07-22). Per-line degree "
                   "RIDES the line colour scalar (same axis/encoder law, read at line "
                   "grain); the meter's word-grain protocol does NOT re-run here."),
    }


# ============================================================ poem fold + transitions
def written_poem_inventory(states_per_line):
    """Fold per-line boolean-side written states -> poem-level {field:{""}}
    for a side. A field is written-latent active for the side iff any line
    fires_bool. Fields UNAVAILABLE on all lines are omitted (not fabricated)."""
    active, seen = {}, set()
    for st in states_per_line:
        for f, v in st.items():
            if not v.get("available"):
                continue
            if v.get("informational_only"):
                continue
            seen.add(f)
            if v.get("fires_bool"):
                active.setdefault(f, set()).add("")
    return active, seen


def survival_transitions(src_desc_states, src_writ_states, tr_desc_states, tr_writ_states):
    """Feed written-row states into rubric_compare's LATENT slots. Poem grain.
    Returns (rows, ladder, counts) with the compensation reading.

    Restricts to fields COVERED ON BOTH SIDES (descriptive-seen ∪ written-
    latent-available), mirroring the descriptive scorer's transition_table
    `both = src_seen & tr_seen` — so e.g. illumination (no en boolean, en-
    written informational per L-F4) never emits a cross-lingual verdict; it
    participates via the scalar only (descriptive F2 corollary)."""
    import rubric_compare as RC
    src_active, src_dseen = D.poem_inventory(src_desc_states)  # descriptive active (verbatim)
    tr_active, tr_dseen = D.poem_inventory(tr_desc_states)
    src_latent, src_lseen = written_poem_inventory(src_writ_states)   # written-latent (boolean side)
    tr_latent, tr_lseen = written_poem_inventory(tr_writ_states)
    both = (src_dseen | src_lseen) & (tr_dseen | tr_lseen)
    src_active = {f: v for f, v in src_active.items() if f in both}
    tr_active = {f: v for f, v in tr_active.items() if f in both}
    src_latent = {f: v for f, v in src_latent.items() if f in both}
    tr_latent = {f: v for f, v in tr_latent.items() if f in both}
    rows, ladder = RC.compare(src_active, tr_active,
                              src_latent=src_latent, tr_latent=tr_latent)
    cat = {f: c for f, c in rows if not f.startswith("_")}
    counts = {
        "COMPENSATION_candidate(latent->active=REVIVAL)":
            [f for f, c in cat.items() if c == "REVIVAL"],
        "survival(latent->latent=LATENT-CARRY)":
            [f for f, c in cat.items() if c == "LATENT-CARRY"],
        "loss(latent->absent=LATENT-UNREALIZED)":
            [f for f, c in cat.items() if c == "LATENT-UNREALIZED"],
        "SURVIVAL(active->active)": [f for f, c in cat.items() if c == "SURVIVAL"],
        "PARTIAL-LOSS(active->latent)": [f for f, c in cat.items() if c == "PARTIAL-LOSS"],
        "DEFORMATION(active->absent)": [f for f, c in cat.items() if c == "DEFORMATION"],
        "INVENTION(absent->active)": [f for f, c in cat.items() if c == "INVENTION"],
    }
    return rows, ladder, counts, {"src_latent": sorted(src_latent),
                                  "tr_latent": sorted(tr_latent),
                                  "src_active": sorted(src_active),
                                  "tr_active": sorted(tr_active)}


# ==================================================== input-resource guard
# Both written sensors read ACQUISITIONS that this repo does not ship (they are
# gitignored payloads, rebuilt from rebuild_manifest.tsv). Without the guard the
# first mode call dies three frames down with a bare FileNotFoundError from
# inside a labeler; say what is missing, and where it comes from, up front.
REQUIRED_INPUTS = [
    ("HowNet.txt — zh written sensor (single-char sememe DEFs, via "
     "latent_written_labeler_53)",
     LEX / "sewrl" / "datasets" / "HowNet.txt", "sewrl"),
    ("Skeat etymological dictionary text — en written sensor (etymon chains, "
     "via etym_chains_v1_52)",
     LEX / "etym" / "skeat_etymological_raw.txt", "etym"),
]


def check_inputs():
    """True iff every sensor input is on disk. Otherwise print WHAT is missing
    and WHICH rebuild_manifest.tsv row restores it, and return False (callers
    exit 1 before touching the corpus or writing anything)."""
    missing = [(label, p, row) for label, p, row in REQUIRED_INPUTS
               if not p.exists()]
    if not missing:
        return True
    print("!! MISSING INPUT RESOURCES — the latent written sensors cannot be "
          "built:", file=sys.stderr)
    for label, p, row in missing:
        print(f"   · {label}", file=sys.stderr)
        print(f"     expected at : {p}", file=sys.stderr)
        print(f"     restore from: rebuild_manifest.tsv row `{row}` "
              f"(payload gitignored — not shipped here)", file=sys.stderr)
    print("   nothing was read and nothing was written.", file=sys.stderr)
    return False


# ================================================================ MODES
def _sensors():
    return ZhWritten(), EnWritten()


def mode_dry():
    """Real corpus, NO encoder. Written-row fire counts per rendering × field
    (carriers named), en Skeat fires, 4-pair transition previews (boolean
    side), referent triggers, embed estimate for the scalar leg (check 1)."""
    if not check_inputs():
        return 1
    present, missing = D.load_corpus()
    zh_sensor, en_sensor = _sensors()

    print("=" * 74)
    print("DRY / COUNT MODE — LATENT rows, real corpus, no encoder")
    print("  (check-1 scalar is PENDING here, L-F2; fires shown = checks 2∧3)")
    print("=" * 74)

    # written-row states per rendering
    writ = {rid: [written_row_line(l, present[rid]["lang"], zh_sensor, en_sensor)
                  for l in present[rid]["lines"]] for rid in present}
    desc = {rid: [D.boolean_states(l, present[rid]["lang"]) for l in present[rid]["lines"]]
            for rid in present}

    print("\n[WRITTEN-LATENT fire counts per rendering × field  (fires = checks 2∧3; carriers named)]")
    print("  tier repo=PD-in-repo · LOCAL=in-copyright (carriers/counts only, F9)")
    print(f"    {'rendering':26} {'lang':4} " + " ".join(f"{f[:5]:>7}" for f in FIELDS5))
    for rid in sorted(present):
        lang = present[rid]["lang"]
        cnt = {f: 0 for f in FIELDS5}
        cars = {f: set() for f in FIELDS5}
        avail = {f: False for f in FIELDS5}
        for st in writ[rid]:
            for f in FIELDS5:
                v = st[f]
                if v.get("available") and not v.get("informational_only"):
                    avail[f] = True
                    if v.get("fires_bool"):
                        cnt[f] += 1
                        cars[f].update(v["carriers"])
        cells = []
        for f in FIELDS5:
            cells.append((f"{cnt[f]}" if avail[f] else "n/a").rjust(7))
        print(f"    {rid:26} {lang:4} " + " ".join(cells))
        for f in FIELDS5:
            if cars[f]:
                print(f"        {f}: carriers {' '.join(sorted(cars[f]))}")

    print("\n[en SKEAT written-latent fires (colour survival-eligible; dark informational, L-F4)]")
    en_ids = [rid for rid in present if present[rid]["lang"] == "en"]
    for rid in en_ids:
        for li, st in enumerate(writ[rid], 1):
            for f in ("color", "illumination"):
                v = st.get(f, {})
                if v.get("available") and v.get("fires", []):
                    for fr in v["fires"]:
                        tag = "COLOUR(counts)" if f == "color" and v.get("fires_bool") else \
                              ("colour(bool-not-silent)" if f == "color" else "dark(informational)")
                        print(f"    {rid} L{li} [{tag}] {fr['word']} -> {fr.get('etymon_terms')} "
                              f"({fr.get('citation')})")
    ce = en_sensor.consider_exhibit()
    print(f"    EXHIBIT (L-F5): consider -> {ce['terms']} [{ce['citation']}]  "
          f"(field 'star' outside shelf, informational)")

    print("\n[4-PAIR en↔zh transition previews — boolean side, poem grain (F1), latent slots fed]")
    src_ids = [rid for rid in present if present[rid]["lang"] == D.SOURCE_LANG]
    zh_ids = sorted(rid for rid in present
                    if present[rid]["lang"] == "zh")
    if src_ids:
        src = src_ids[0]
        for rid in zh_ids:
            rows, ladder, counts, slots = survival_transitions(
                desc[src], writ[src], desc[rid], writ[rid])
            comp = counts["COMPENSATION_candidate(latent->active=REVIVAL)"]
            surv = counts["survival(latent->latent=LATENT-CARRY)"]
            loss = counts["loss(latent->absent=LATENT-UNREALIZED)"]
            print(f"    {src} ↔ {rid}")
            print(f"        src written-latent: {slots['src_latent'] or '—'} | "
                  f"tr written-latent: {slots['tr_latent'] or '—'}")
            print(f"        COMPENSATION-cand: {comp or '—'} | survival(carry): {surv or '—'} | "
                  f"loss(unrealized): {loss or '—'}")
            other = {k: v for k, v in counts.items()
                     if v and not k.startswith(("COMPENSATION", "survival", "loss"))}
            if other:
                print(f"        (descriptive-side cells: "
                      + " ".join(f"{k.split('(')[0]}={v}" for k, v in other.items()) + ")")

    print("\n[REFERENT-COLOUR triggers (thin) — definition-witness word hits per rendering]")
    wit_n = len(_witness_color_words())
    print(f"    witness colour-fire word set extracted (L-F6): {wit_n} words")
    for rid in sorted(present):
        lang = present[rid]["lang"]
        if lang not in ("zh", "en"):
            continue
        hits = set()
        for l in present[rid]["lines"]:
            hits.update(referent_row_line(l, lang)["referent_trigger_words"])
        if hits:
            tag = "LOCAL/F9" if present[rid]["redact"] else "repo"
            print(f"    {rid} [{tag}]: referent-colour trigger words {' '.join(sorted(hits))}")
    print("    degree: .800 THIN meter exists (word_latent_v5); per-line rides the line colour scalar")
    print("    CCFD: lexical_resources/impression_norms/ccfd_2021 — truth-side context only (cited)")

    # embed estimate for the scalar leg (check 1) — identical inventory to descriptive
    n_uniq = set()
    for rid in sorted(present):
        for l in present[rid]["lines"]:
            n_uniq.add(l)
            for u in D.maskable_units(l):
                n_uniq.add(D.delete_unit(l, u))
    print("\n[embed estimate — the CHECK-1 scalar leg at --run (LaBSE, batch_size=1)]")
    print(f"    unique texts (line + one-deletion masks): {len(n_uniq)}")
    print(f"    with re-order certificate replay: ~{2*len(n_uniq)} encodes")
    print("    (identical inventory to the descriptive scalar leg — the written row's "
          "check 1 IS the descriptive axis at the line; no new encoder pass)")

    print("\n[input shas]")
    for name, p in [("temporal_inv", RESULTS / "hownet_temporal_chars_54.json"),
                    ("sound_amended_inv", RESULTS / "hownet_sound_chars_54_amended.json"),
                    ("plant_inv", RESULTS / "hownet_plant_chars_54.json"),
                    ("written_labeler", MARK_TOOLS / "latent_written_labeler_53.py"),
                    ("etym_chains", PROTO / "etym_chains_v1_52.py"),
                    ("rubric_compare", MARK_TOOLS / "rubric_compare.py"),
                    ("referent_meter_v5", PROTO / "word_latent_v5_referent_color_54.py"),
                    ("witness_zh", RESULTS / "definition_witness_zh_PROPOSED_53.json")]:
        if p.exists():
            print(f"    {name:20} {D.sha256(p)[:16]}…  {p.name}")
    return 0


def mode_smoke():
    """Toy lines through the FULL path incl. ONE axis read for check 1
    (colour), so the three-check conjunction is exercised end to end.
    Writes ONLY to /tmp."""
    if not check_inputs():
        return 1
    out = Path("/tmp/latent_smoke")
    out.mkdir(exist_ok=True)
    print("SMOKE — LATENT rows, toy lines, full path (incl. check-1 axis), writes only", out)
    zh_sensor, en_sensor = _sensors()

    # toy zh: 赤字 (赤=red, word fiscal -> colour written-latent), 深夜 (夜 temporal),
    #         波黑 (黑 colour), 明天 (明 illum) ; toy en: consider-class + a colour etymon
    zh_lines = ["赤字连年", "深夜的钟声", "波黑边境", "明天启程"]
    en_lines = ["When yellow leaves do consider the boughs",
                "In twilight's ashes cold"]

    print("\n[zh written-latent (checks 2∧3; scalar pending until axis read below)]")
    zh_writ = [written_row_line(l, "zh", zh_sensor, en_sensor) for l in zh_lines]
    for l, st in zip(zh_lines, zh_writ):
        fired = {f: st[f]["carriers"] for f in FIELDS5
                 if st[f].get("fires_bool")}
        print(f"  {l}\n     written-latent fires (bool side): {fired}")

    print("\n[en written-latent — Skeat]")
    en_writ = [written_row_line(l, "en", zh_sensor, en_sensor) for l in en_lines]
    for l, st in zip(en_lines, en_writ):
        for f in ("color", "illumination"):
            v = st.get(f, {})
            for fr in v.get("fires", []):
                print(f"  {l}\n     {f}: {fr['word']} -> {fr.get('etymon_terms')} ({fr.get('citation')})")

    # CHECK 1 — one axis read (colour), the descriptive scorer's law verbatim
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(str(PROTO / "models" / "LaBSE"), device="cpu")
    axes_all = D.load_axes()
    axes = {"color": axes_all["color"]}
    rend = {"zh:toy": {"lang": "zh", "lines": zh_lines},
            "en:toy": {"lang": "en", "lines": en_lines}}
    readings, drift, ninv = D.scalar_readings(model, axes, rend)
    print(f"\n[check-1 colour axis — certificate drift={drift:.2e} over {ninv} texts]")
    assert drift < 1e-6, f"certificate FAILED: {drift}"
    for rid, rows in sorted(readings.items()):
        for row in rows:
            print(f"  {rid} L{row['line_no']} colour_scalar={row['reading']['color']:+.3f}  "
                  f"(check1 = this reading vs the field-present threshold at --run)")

    # transition preview (poem grain, latent slots fed)
    zh_desc = [D.boolean_states(l, "zh") for l in zh_lines]
    en_desc = [D.boolean_states(l, "en") for l in en_lines]
    rows, ladder, counts, slots = survival_transitions(en_desc, en_writ, zh_desc, zh_writ)
    print(f"\n[transition — 8-cell, poem grain, latent slots fed]  slots={slots}")
    print(f"  rows: {rows}")
    print(f"  COMPENSATION-cand: {counts['COMPENSATION_candidate(latent->active=REVIVAL)']} | "
          f"survival: {counts['survival(latent->latent=LATENT-CARRY)']} | "
          f"loss: {counts['loss(latent->absent=LATENT-UNREALIZED)']}")

    # referent thin
    print("\n[referent-colour (thin)]")
    for l in zh_lines:
        rr = referent_row_line(l, "zh")
        if rr["referent_trigger_words"]:
            print(f"  {l}: triggers {rr['referent_trigger_words']}")

    (out / "smoke_result.json").write_text(json.dumps({
        "certificate": drift, "n_inventory": ninv,
        "zh_written": zh_writ, "en_written": en_writ,
        "transition_rows": rows, "transition_counts": counts, "slots": slots,
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    print("\n→ /tmp/latent_smoke/smoke_result.json  (nothing written under the repo)")
    print("SMOKE OK")
    return 0


def mode_run(align_file=None):
    """REAL run (orchestrator, post-review). Writes latent_scores.json (NO .md
    — corrected 07-26, manual §7; the .md was promised here but never written)
    into THIS folder, F9-redacted for local-tier line text. Applies check 1
    (the descriptive colour/field axes at the line) to complete the
    three-check conjunction."""
    if not check_inputs():
        return 1
    present, missing = D.load_corpus()
    zh_sensor, en_sensor = _sensors()
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(str(PROTO / "models" / "LaBSE"), device="cpu")
    axes = D.load_axes()
    rend = {rid: {"lang": present[rid]["lang"], "lines": present[rid]["lines"]} for rid in present}
    readings, drift, ninv = D.scalar_readings(model, axes, rend)
    if drift >= 1e-6:
        print(f"CERTIFICATE FAILED {drift:.2e} — aborting (house law).", file=sys.stderr)
        return 1

    writ = {rid: [written_row_line(l, present[rid]["lang"], zh_sensor, en_sensor)
                  for l in present[rid]["lines"]] for rid in present}
    desc = {rid: [D.boolean_states(l, present[rid]["lang"]) for l in present[rid]["lines"]]
            for rid in present}
    ref = {rid: [referent_row_line(l, present[rid]["lang"]) for l in present[rid]["lines"]]
           for rid in present}

    # CHECK 1 applied: a written-latent fire is COMPLETE iff checks 2∧3 (already
    # in writ) ∧ the line's descriptive-axis reading says the field. The
    # field-present threshold is the descriptive scorer's law (line scalar sign,
    # ensemble-relative). We attach the line scalar per fire; the conjunction's
    # sign gate is the descriptive axis reading (>0 for the field's positive pole).
    for rid in present:
        for li, st in enumerate(writ[rid]):
            for f in FIELDS5:
                v = st.get(f, {})
                if v.get("available") and not v.get("informational_only"):
                    v["scalar_check1"] = float(readings[rid][li]["reading"][f])
                    v["fires_three_check"] = bool(v.get("fires_bool") and v["scalar_check1"] > 0)

    # transitions (complete written-latent uses fires_three_check at run)
    def writ_poem_complete(states):
        active, seen = {}, set()
        for st in states:
            for f, vv in st.items():
                if not vv.get("available") or vv.get("informational_only"):
                    continue
                seen.add(f)
                if vv.get("fires_three_check"):
                    active.setdefault(f, set()).add("")
        return active, seen

    import rubric_compare as RC
    src_ids = [rid for rid in present if present[rid]["lang"] == D.SOURCE_LANG]
    transitions = {}
    if src_ids:
        src = src_ids[0]
        src_active, src_dseen = D.poem_inventory(desc[src])
        src_lat, src_lseen = writ_poem_complete(writ[src])
        for rid in sorted(present):
            if present[rid]["lang"] != "zh":
                continue
            tr_active, tr_dseen = D.poem_inventory(desc[rid])
            tr_lat, tr_lseen = writ_poem_complete(writ[rid])
            both = (src_dseen | src_lseen) & (tr_dseen | tr_lseen)   # both-covered only
            sa = {f: v for f, v in src_active.items() if f in both}
            ta = {f: v for f, v in tr_active.items() if f in both}
            sl = {f: v for f, v in src_lat.items() if f in both}
            tl = {f: v for f, v in tr_lat.items() if f in both}
            rows, ladder = RC.compare(sa, ta, src_latent=sl, tr_latent=tl)
            transitions[rid] = {"grain": "poem", "rows": rows,
                                "both_covered_fields": sorted(both),
                                "src_latent": sorted(sl), "tr_latent": sorted(tl)}

    # F9 redaction: strip local-tier line text everywhere it lands
    for rid in present:
        if present[rid]["redact"]:
            # The written row holds WORD-grain receipts only (carriers, fired
            # words, counts) — never a full line — so F9 has nothing to strip
            # there. It used to sweep st[f].pop("_line", None); verified #71
            # that written_row_line emits no "_line" key in ANY branch (zh:
            # available/boolean_silent/carrier_present/fires_bool/
            # scalar_check1/carriers/fires · en: same, or the informational
            # illumination form · de/jp: available/reason) and that mode_run
            # adds only scalar_check1 + fires_three_check. The sweep was a
            # no-op and is gone.
            for rr in ref[rid]:
                rr["_line_redacted"] = True

    manifest = {"seed": SEED, "certificate_drift": drift, "n_inventory": ninv,
                "corpus_present": {rid: {"sha256": present[rid]["sha256"], "tier": present[rid]["tier"],
                                         "redacted": present[rid]["redact"]} for rid in sorted(present)},
                "corpus_missing": missing,
                "carrier_inventories": {
                    "temporal": D.sha256(RESULTS / "hownet_temporal_chars_54.json"),
                    "sound_amended": D.sha256(RESULTS / "hownet_sound_chars_54_amended.json"),
                    "plant": D.sha256(RESULTS / "hownet_plant_chars_54.json"),
                    "written_labeler": D.sha256(MARK_TOOLS / "latent_written_labeler_53.py"),
                    "etym_chains": D.sha256(PROTO / "etym_chains_v1_52.py"),
                    "rubric_compare": D.sha256(MARK_TOOLS / "rubric_compare.py"),
                    # her pin ruling 08-12 (#71): this scorer runs THROUGH
                    # score_descriptive_fields (imported as D) — its bytes join
                    # the manifest so D-drift can no longer reach latent
                    # outputs without a hash witness
                    "score_descriptive_fields": D.sha256(Path(D.__file__))}}

    result = {"what": "deterministic LATENT rows — §8 demonstration, sonnet 73",
              "law": "methodology_amendment_0721_53.md §2/§4; rubric_compare 8-cell",
              "flags": ["L-F1 folder name", "L-F2 check1=scalar (applied here at run)",
                        "L-F3 realized-gate layering", "L-F4 en illumination no boolean",
                        "L-F5 consider/star exhibit", "L-F6 referent trigger thin",
                        "F9 local-tier line text redacted"],
              "manifest": manifest,
              "written_row": writ, "referent_row": ref, "transitions": transitions,
              "consider_exhibit": en_sensor.consider_exhibit()}
    (HERE / "latent_scores.json").write_text(json.dumps(result, ensure_ascii=False, indent=1),
                                             encoding="utf-8")
    print(f"→ latent_scores.json  (certificate {drift:.2e})")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="§8 latent-field scoring (written + referent-thin)")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry", action="store_true", help="real corpus, no encoder: written fires/carriers, en Skeat, 4-pair previews, embed estimate")
    g.add_argument("--smoke", action="store_true", help="toy lines, full path incl. check-1 axis, writes only /tmp")
    g.add_argument("--run", action="store_true", help="REAL run (orchestrator, post-review): writes json here, F9-redacted")
    ap.add_argument("--align", default=None, help="chair-drafted alignment file (F1; unfrozen)")
    a = ap.parse_args()
    if a.dry:
        sys.exit(mode_dry())
    if a.smoke:
        sys.exit(mode_smoke())
    if a.run:
        sys.exit(mode_run(a.align))
