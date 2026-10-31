#!/usr/bin/env python3
"""Arm-1 boolean trait labelers: color, sound (2 tiers), plant, temporal.

WHAT THIS IS — a lookup/regex sensor shelf. For one unit of text it answers, per
field, "does this line SAY this field": BOOLEANS plus a citable receipt, never
scalars (the intensity program is a separate build).

INTERFACE
  label_unit(text, lang=None) -> {field: (hit, evidence, flags)}
    fields  color · plant · temporal · sound (WORD tier: the line describes a
            sound) · sound_device (DEVICE tier: the line enacts euphony —
            叠字/雙聲/叠韵/alliteration/repetition). A field absent from the
            returned dict did not fire.
    lang    gates the fr and de colour legs ('fr' / 'de'); every other
            language path is byte-identical whether those legs exist or not.
  Per-field helpers: _label_color / _plant / _temporal / _sound / _sound_device,
  fed by _mask_compounds (runs FIRST) and _fold_en_words.
  Lexicon getters, all lazy + cached: en_color · en_plant · en_sound_word ·
  en_temporal · zh_plant · zh_temporal · zh_sound (+ ZH_COLOR, ZH_COMPOUNDS).
ENTRY POINTS
  python3 trait_labelers.py             selftest: the always-current probe table
  python3 trait_labelers.py --calibrate P/R/F1 against human marks — needs the
                                        PRIVATE marking tree; refuses loudly
                                        when absent (never a vacuous 0-table)
THE RULE in one line: every lexicon here is a CITABLE DERIVATION from a named
source, or is flagged AUTHORED-INTERIM with its named replacement — no
dev-fitted lists, ever. Full ruling, per-lexicon provenance table and dated
build record below.

════════════════════════ PROVENANCE & CHANGELOG ═════════════════════════
House law: the docstring IS the receipt. Below, in order — the dated build
blocks (newest first) · THE RULE verbatim (07-15/16) · the current calibration
state · the per-lexicon provenance table · the standing operational
declarations. Every citation, ruling, date and derivation rule below backs a
number that appears in the paper; none of it is decoration.

═══ 2026-08-12 (#71): REFACTOR ONLY — no lexicon, no derivation, no number ═══
Structural pass over this file. `python3 trait_labelers.py` stdout verified
BYTE-IDENTICAL to the pre-refactor baseline (227 lines, 37/37 probes, same leg
counts, same colour tiers). No lexicon gained or lost a member.
  · label_unit (156 ll.) split into per-field helpers. Evaluation ORDER is
    unchanged and load-bearing: compound masking FIRST, then the naive en fold,
    then sound_device · colour (fr/de/en branches as-is) · the de language gate
    · plant · temporal · sound.
  · Mechanical de-duplication, behaviour preserved: ONE 廣韻 gloss-head sweep
    (_gy_gloss_chars) under the temporal and sound legs · ONE WordNet ~-closure
    (_wn_noun_index + _wn_hyponym_closure) under en_plant and en_sound_word ·
    ONE variant-map loader under the colour and sound folds · ONE sibling-build
    importer under _fr/_de · ONE _lazy singleton helper replacing 16 hand-written
    `_X = None` caches. gy() was CHECKED and deliberately NOT folded into the
    gloss sweep: it reads different columns (音韻地位/字頭) into a different
    shape (phonology dict, not a char set).
  · EN_TEMPORAL was this file's one EAGER import-time load; it is now the lazy
    getter en_temporal(), like every sibling lexicon. Same contents.
  · INTENDED BEHAVIOUR CHANGE, exactly one: --calibrate now FAILS LOUD when the
    private marking inputs are absent. It previously printed a silent
    P=0/R=0/F1=0 table computed over zero units — a vacuous result dressed as a
    score. The selftest path is untouched.
  · KEPT deliberately, not "cleaned": load_map/sheet_units own implementations
    (cross-referenced to normalize.py at their definition) · the USE_SUPERSENSE
    dead-by-flag block (frozen decision 07-15) · ZH_COMPOUNDS inline (its
    externalisation to a data file remains future work, not done here).

═══ 2026-07-28 night (#61): DE COLOUR + EN-TEMPORAL — the fr blueprint · HeidelTime ═══
Two additions this build (branch de-temporal-support-61; colour-only for de,
temporal for en; en/zh/fr outputs BYTE-IDENTICAL — proven by regression):
  · DE COLOUR LEG — a language-gated `lang=='de'` colour leg in label_unit (the
    fr precedent 50cb569/2ebf673), consulting the German colour sets via a
    FORWARD PARADIGM MAP (grüner→grün, weissen→weiß). Sets = B&K12-German ∪
    kaikki.org German Wiktextract adj colour-sense; built by engine/
    de_build/ (extract_kaikki_de_color.py → build_de_color_inventory.py →
    de_labelers.py). On a German unit the en xkcd base is NOT consulted (the
    lang!='de' guard) so German non-colour words that collide with en colour
    names (fern='far', Rosen→rose) do not false-fire. Colour-only, citation-tier;
    de written/referent stay UNCOVERED (starred PARTIAL-INVESTIGATION, the fr law).
  · EN TEMPORAL — the AUTHORED-INTERIM ⚠ EN_TEMPORAL hardcode is RETIRED and
    replaced by a cited word-list-of-facts DERIVED from HeidelTime's published
    English resource files (Strötgen & Gertz 2013, LRE, README item [4]; GPLv3,
    no code/patterns copied), LOADED AS DATA from lexical_resources/temporal_
    lexicon/en_temporal_inventory_61.json (built by en_temporal_derive_61.py),
    UNIONed with EN_TEMPORAL_RULED_EXCLUSIVE {twilight,dusk} (ruling (c) below —
    an independent standing ruling with its own receipt). INTERACTION AUDIT:
    en_temporal() is subtracted from en_color(); the swap changes en_color() by
    exactly one member — 'midnight' now yields to temporal (a HeidelTime part-of-
    day term also in the xkcd base; a true cross-field exclusive, correctly
    yielded). BK11 is UNTOUCHED (ruling (a) safe). twilight/dusk preserved.
STATUS: BUILT + SELFTESTED (de-seat colour lines fire; temporal months/seasons/
units fire; en/zh/fr byte-identical). PROPOSED; adopt-by-numbers in the morning.

═══ 2026-07-27/28 night (#61): EN-COLOUR YIELD LAW — ruled by An, of record ═══
en_color()'s old blanket "names yield to the other field" (en_plant subtraction,
commit c65c3b4) over-yielded: it ate BK11 basics orange+pink AND 72 xkcd colour
names (rose/violet/olive/lavender/lilac/peach/plum/cherry/mint/sage/mustard/
fern…) — the second cause of the #61 rosy pseudo-ghost (commit 6bf9088). Her
four rulings, now ONE coherent law (see the block above en_color()):
  (a) BK11 basics NEVER yield (Berlin & Kay 1969); orange/pink restored.
  (b) xkcd∩en_plant names are NOT deleted — FLAG-class, fire colour + declared
      polysemy (byte-mirror of the fr nuit ruling, commit 50cb569: priced, not
      hidden — the live exemplar now that EN_COLOR_FLAG is empty, gold+fair both
      removed at the #61 no-vibes audit). See en_color_plant_flag().
  (c) en_temporal() subtraction KEPT (true cross-field exclusivity — twilight/dusk
      ARE the other field; arm-1 receipt v11 L134). Yielded, not flagged.
  (d) EN_COLOR_YIELD_RULED — per-word ruled yields; dark→illumination (her ruling
      after the correspondances en:dillon "darkness" finding), so a future
      darkness→dark fold cannot state colour. Named/citable/appendable.
STATUS: BUILT + SELFTESTED (`python3 trait_labelers.py` — pink/orange fire clean,
rose fires flagged, dark does not fire colour). The morphological fold that folds
rosy→rose (the pseudo-ghost's FIRST cause) is the #61 Stage-2 build (en_morph_
fold; the variant of a flag-class base inherits flag-class).

═══ 2026-07-26 (#58): word-tier SOUND built — PROPOSED ═══
The delivered "sound" boolean was DEVICE-tier only (叠字/雙聲/聯綿/allit/
word-rep — euphony ENACTED). A word-tier "does this word DIRECTLY DESCRIBE
sound" labeler (歌聲/噪/鳴/noise/song — sound MENTIONED) never existed; every
"descriptive ×5 fields" summary rounded that substitution into a tick
(reports/sound_descriptive_gap_0726_58.md). Correction, device≠descriptive:
  · the device block's output key RENAMES "sound" -> "sound_device"
    (receipts byte-identical);
  · a new field "sound" = the word-tier labeler (zh three citable legs
    釋樂∪音部∪廣韻 ∩ line chars, leg-tagged · en WordNet auditory closure
    ∩ folded words). See _zh_sound_legs()/en_sound_word() below.
STATUS: BUILT + SELFTESTED (founding line 上有弦歌聲, en line, device
regression — `python3 trait_labelers.py`). PROPOSED, pending field-owner
adoption and the descriptive-pass rerun cascade. Board scoring NOT run here;
the one-line scorer field-list change is in the build note, not applied.
Derivation receipts / rejected seeds / collisions / rerun cascade:
reports/sound_word_labeler_build_58.md.

═══ 2026-07-26 (#58): descriptive COLOUR ZH re-derived — Option A, ADOPTED ═══
The zh colour side was the last AUTHORED-INTERIM ⚠ lexicon (ZH_COLOR, flagged
since the 07-15 provenance ruling); the en side (B&K ∪ XKCD) already stood.
Fixed as a citable derivation with two zh legs (proposal
reports/colour_descriptive_proposal_58.md, field-owner-adopted Option A):
  · CHAR tier  — ZH_COLOR re-derived from 禮記·玉藻 五色 (正色/間色, wikisource
                 PD) ∪ 蓝(藍) as the one occurring clean gap-fill. ⚠ RETIRED.
                 廣韻 色-gloss sweep documented as GAP-CHECK ONLY (not wired).
  · COMPOUND tier — ZH_COMPOUNDS gains the 144 中国传统色 compound names
                 (zerosoul MIT, simp-only), colour-typed, maximal-match. Compound
                 grain is collision-safe → net-new 琥珀/金色 fire, 青翠/雪白
                 precision, and the latent/stated distinction is PRESERVED (a
                 tight char set keeps 碧/皎/縞… latent). EN unchanged (poop stays,
                 field-owner-validated).
STATUS: BUILT + SELFTESTED (compound-colour fires, qingqing chars unchanged,
masking-interaction probes, sound/device regression — `python3 trait_labelers.py`).
The full colour-cascade rerun is registered in
publishable/rerun_registration_0727_colour_58.md.

═══ THE RULE (the PI, provenance ruling 07-15; restated verbatim 07-16:
"NO any dev-fitted lexicon") ═══
Every lexicon in this file is either a CITABLE DERIVATION from a
named source, or is flagged AUTHORED-INTERIM with a named citable
replacement. A lexicon whose CONTENTS were selected by dev
performance is dev-fitted regardless of when editing stopped — the
old "freeze" framing (no further dev edits) is the weaker corollary,
not the rule. Consequence: no FN/FP-driven lexicon edits, ever;
citable-derivation improvements are legal at any time (with
recalibration reported, drops included — the honest drop IS the
finding).

═══ CURRENT STATE (2026-07-16 audit, #48) ═══
Output type: BOOLEANS per field per unit. Scalars do not exist here;
the intensity program is a separate build (design/
trait_intensity_program_48.md). Calibration (dev, zh/en in-scope,
POST-v3.1-provenance state — reproduced from this code 07-16; the
delta §10 / calibration-report tables are PRE-provenance and stale):
  color P.91 R.83 F1.87 · sound P1.00 R.50 F1.67 ·
  plant P.70 R.88 F1.78 · temporal P.94 R.73 F1.82
The provenance replacement moved these honestly (authored lists →
derivations; the drop IS the finding). Rerun `python3
trait_labelers.py` for the always-current table; trust the print
over any document, including this one.

Lexicon provenance table:
  zh plant      DERIVED   爾雅 釋草/釋木 (wikisource PD) ∧ Kangxi
                          radical (Unihan kRSUnicode)
  zh temporal   DERIVED   爾雅 釋天 calendrical ∪ 廣韻 gloss-head
                          seeds (tshet-uinh CC0) ∪ 日/夕 radical rule
  en plant      DERIVED   WordNet 3.0 flora + plant_part closures
  zh sound      DERIVED   爾雅 釋樂 definienda (wikisource PD) ∪ 音-radical
                (word-tier) 180 (Unihan) ∪ 廣韻 gloss-head seeds (CC0)   [#58]
  en sound      DERIVED   WordNet 3.0 auditory closure (~ of sound/noise/
                (word-tier) music senses)                                [#58]
  {zh,en} sound_device — the DEVICE tier (叠字/雙聲/聯綿/allit/rep); derived
                in-line in label_unit (pypinyin/廣韻/CMU); no lexicon.
  en color      DERIVED   Berlin&Kay 11 ∪ XKCD survey (CC0), under THE EN-
                          COLOUR YIELD LAW (#61): BK11 basics never yield;
                          xkcd∩en_plant names fire FLAGGED (polysemy priced);
                          en_temporal() + EN_COLOR_YIELD_RULED (dark→illum) yield.
                          See en_color()/en_color_plant_flag()/the law block.
  zh color      DERIVED   禮記·玉藻 五色 (正色 青赤黃白黑 + 間色, wikisource
                (char)    PD) ∪ 蓝(藍) gap-fill  [#58: AUTHORED-INTERIM ⚠
                          RETIRED; 廣韻 sweep = gap-check only, not wired]
  en temporal   DERIVED   HeidelTime English resource files → cited word-list-
                          of-facts (Strötgen & Gertz 2013, LRE, item [4]; GPLv3
                          — no code/patterns redistributed, a derived vocabulary
                          inventory) ∪ EN_TEMPORAL_RULED_EXCLUSIVE {twilight,dusk}
                          (ruling (c), arm-1 L134). Loaded AS DATA from
                          lexical_resources/temporal_lexicon/en_temporal_
                          inventory_61.json (built by en_temporal_derive_61.py).
                          [#61 Stage 2: AUTHORED-INTERIM ⚠ RETIRED]
  de color      DERIVED   Berlin&Kay 1969 German basic set ∪ kaikki.org German
                (colour)  Wiktextract adj colour-sense (CC BY-SA 4.0/GFDL); built
                          by engine/de_build/, loaded via the language-
                          gated de leg in label_unit (lang=='de'). Forward
                          paradigm generation (German declension + ß/ss). [#61
                          night build — colour-only, citation-tier, PROPOSED]
  ZH_COMPOUNDS  MIXED     (1) 7 legacy DISAMBIGUATION entries: AUTHORED-
                          INTERIM ⚠ (dev FPs 07-15, pre-rule; replacement:
                          HowNet multi-char DEF lookup). (2) COLOUR compound
                          tier [#58]: DERIVED — 中国传统色 144 names (zerosoul
                          MIT, simp-only; upstream Sina blog DISCLOSED)
  ZH_BINOMES    AUTHORED-INTERIM ⚠  replacement: a citable 聯綿詞
                          dictionary
  EN_ALLIT_STOP AUTHORED-INTERIM ⚠  standard function-word class;
                          replacement: any citable EN stopword list
  ZH_PARTICLES  declared  the standard 文言虛詞 class (documented
                          exception, pre-rule)
NOTE: the v1.1 narrative's "lexicon adds: bough(s), 甞嘗曾茲" do NOT
exist in this code — bough falls out of the plant_part closure; the
four zh chars are in no current set. Saga ≠ state; trust this table.

Operational declarations still in force: supersense module EXCLUDED
from calibrated fields (dev net-negative; USE_SUPERSENSE=False) ·
phoneme tier = declared approximations (pypinyin for Middle Chinese
until 廣韻 covers; orthographic alliteration until CMU covers) ·
sound-as-REFERENT is a separate organ (sound_referent.py) ·
validation-grade numbers only from the pre-registered post-rule poem
path (江上吟 class), never dev.

History/changelog: lives in the dated calibration report and
appendices (ruling_arm1_taggers_20260715), not here.
"""
import csv
import functools
import glob
import importlib
import json
import re
import sys
from pathlib import Path
try:
    from pypinyin import pinyin, Style   # pure lookup table (ruled admissible 07-15)
    HAVE_PINYIN = True
except ImportError:
    HAVE_PINYIN = False

# ---------- path anchors (one definition each; every loader below reads
# through these instead of recomputing Path(__file__) inline) ----------
HERE = Path(__file__).resolve().parent          # marking/tools
ROOT = HERE.parents[1]                          # repo root (== Path(__file__).parents[2])
V = HERE / "vectors"                            # vendored lookup tables, see LEXICONS below
GY_CSV = V / "guangyun/韻書/廣韻.csv"            # 廣韻 — nk2028/tshet-uinh-data, CC0


def _lazy(build):
    """Module-local lazy singleton: run `build` once on first call, then return
    the SAME object forever. Mechanical replacement for the `_X = None; global
    _X; if _X is None:` idiom this file used at ~16 sites — identical semantics
    (one build per process, callers share the cached object), no output change."""
    cache = []

    @functools.wraps(build)
    def get():
        if not cache:
            cache.append(build())
        return cache[0]
    return get


# --- Middle Chinese (廣韻) lookup — nk2028/tshet-uinh-data, CC0.
# 音韻地位 strings like 端一東平: initial = s[0], rhyme = s[-2], tone = s[-1].
# NOT foldable into the two 廣韻 GLOSS legs below (_gy_gloss_chars): this reads
# 音韻地位/字頭 into a phonology dict, they read 釋義 heads into char sets —
# different columns, different shape. Only the CSV path is shared (GY_CSV).
@_lazy
def gy():
    out = {}
    if GY_CSV.exists():
        for row in csv.DictReader(open(GY_CSV, encoding="utf-8")):
            s, ch = row["音韻地位"], row["字頭"]
            if len(s) >= 3 and ch:
                out.setdefault(ch, []).append((s[0], s[-2], s[-1]))
    return out


@_lazy
def cmu():
    """CMU dict: word -> first-pronunciation phoneme list (ARPAbet)."""
    out = {}
    p = V / "cmudict.dict"
    if p.exists():
        for ln in open(p, encoding="utf-8", errors="ignore"):
            parts = ln.strip().split()
            if parts and "(" not in parts[0]:
                out[parts[0].lower()] = parts[1:]
    return out

def rhyme_part(word):
    """Phonemes from last stressed vowel onward (the rhyming tail)."""
    ph = cmu().get(word.lower())
    if not ph:
        return None
    idx = [i for i, p in enumerate(ph) if p[-1] in "12"] or \
          [i for i, p in enumerate(ph) if p[-1] == "0"]
    return tuple(ph[idx[-1]:]) if idx else None

# WordNet supersenses (local wordnet30) — FIRST-SENSE ONLY (declared:
# WordNet orders senses by frequency; first-sense gating avoids the
# abstract-field noise that got WordNet dropped from schema work).
# DEAD BY FLAG, DELIBERATELY KEPT: USE_SUPERSENSE = False (frozen decision
# 07-15, dev-net-negative — see the flag below). Nothing in this module calls
# supersense(); the module is retained un-deleted as the record of that decision
# and for the declared "full-corpus assist only" use. Not dead code to prune.
_LEX_TO_FIELD = {"20": "plant", "28": "temporal"}   # noun.plant, noun.time


@_lazy
def supersense():
    out = {}
    d = V / "wordnet30"
    idx, dat = d / "index.noun", d / "data.noun"
    if idx.exists() and dat.exists():
        off_lex = {}
        for ln in open(dat, encoding="utf-8", errors="ignore"):
            if ln[:1].isdigit():
                p = ln.split()
                off_lex[p[0]] = p[1]
        for ln in open(idx, encoding="utf-8", errors="ignore"):
            if ln[:1] == " " or not ln.strip():
                continue
            p = ln.split()
            word = p[0]
            first = p[len(p) - int(p[2])]      # first (most frequent) synset
            f = _LEX_TO_FIELD.get(off_lex.get(first, ""))
            if f and "_" not in word:
                out.setdefault(f, set()).add(word)
    return out

def mc_pair_device(a, b):
    """雙聲/叠韵 classification by Middle Chinese readings (any-reading match)."""
    ra, rb = gy().get(a, []), gy().get(b, [])
    if any(x[0] == y[0] for x in ra for y in rb):
        return "雙聲"
    if any(x[1] == y[1] for x in ra for y in rb):
        return "叠韵"
    return None

CJK = r"㐀-鿿"
# FROZEN DECISION 07-15: the supersense module is dev-net-negative, so it is
# switched OFF here and no caller consults it (see supersense() above). The flag
# and its module stay in place as the record of that decision — declared
# "full-corpus assist only". Do not repurpose without a new ruling.
USE_SUPERSENSE = False

# ---------- LEXICONS, v3-PROVENANCE (07-15 night, her ruling: no
# authored lists — every set below is a CITABLE derivation or is
# explicitly flagged AUTHORED-INTERIM pending its named replacement) --
# (path anchors HERE / ROOT / V / GY_CSV are defined at the top of the file)


@_lazy
def radicals():
    """char -> Kangxi radical number. Source: Unicode Unihan
    kRSUnicode (Unicode data-files license)."""
    rad = {}
    f = V / "Unihan_IRGSources.txt"
    if f.exists():
        for ln in open(f, encoding="utf-8"):
            if "\tkRSUnicode\t" in ln:
                cp, _, val = ln.rstrip("\n").split("\t")
                try:
                    rad[chr(int(cp[2:], 16))] = int(val.split()[0].split(".")[0].rstrip("'"))
                except ValueError:
                    pass
    return rad

# Classical particles/connectives stoplist — the ONLY authored element
# in the zh derivations; citable as the standard 文言虛詞 class.
# 徒 added #58: standard 文言虛詞, adverbial "merely" (徒歌/徒鼓 in 釋樂);
# a definiendum modifier, never a sound-description itself.
ZH_PARTICLES = set("之乎者也而已矣焉哉其于於以爲為曰謂所似有無不大小上中下在一二三四五六七八九十百正月的徒")

PLANT_RADICALS = {140, 75, 118, 115, 119, 97, 179, 200, 202}  # 艸木竹禾米瓜韭麻黍
TIME_RADICALS = {72, 36}                                       # 日 夕

def _erya_chars(*files):
    s = set()
    for f in files:
        p = V / f
        if p.exists():
            s |= set(re.findall(r"[㐀-鿿𠀀-𪛟]", open(p, encoding="utf-8").read()))
    return s - ZH_PARTICLES

def _gy_gloss_chars(seeds):
    """DERIVED, shared 廣韻-gloss mechanism (declared; gloss-based semantic-field
    extraction, standard DH method): the 字頭 whose 釋義 HEAD contains any of
    `seeds`. HEAD = the text before the first 又/亦 tail, first 12 chars — the
    definiens proper, never the cross-reference tail. One implementation for the
    TEMPORAL and SOUND legs (GY_TEMPORAL_SEEDS / GY_SOUND_SEEDS); the seed lists
    are declared per field at their own definitions, each leg applies its own
    stoplist subtraction at its call site. Source: 廣韻, tshet-uinh CC0."""
    out = set()
    if GY_CSV.exists():
        for r in csv.DictReader(open(GY_CSV, encoding="utf-8")):
            head = r["釋義"].split("又")[0].split("亦")[0][:12]
            if any(s in head for s in seeds):
                out.add(r["字頭"])
    return out


# Temporal-definiens seed patterns for 廣韻-gloss derivation (declared;
# matched against the gloss HEAD only — see _gy_gloss_chars).
GY_TEMPORAL_SEEDS = ("時也","早也","晚也","日晚","旦也","夕也","暮也",
                     "朝也","古也","久也","是時")


@_lazy
def gy_gloss_temporal():
    """DERIVED: chars whose 廣韻 釋義 head matches a temporal
    definiens seed. Closes the deictic gap (今昔朝暮晚初…) citably."""
    return _gy_gloss_chars(GY_TEMPORAL_SEEDS) - (ZH_PARTICLES | ZH_COLOR)


@_lazy
def zh_plant():
    """DERIVED: chars attested in 爾雅 釋草+釋木 (zh.wikisource, PD)
    ∧ Kangxi radical ∈ plant radicals (Unihan). Zero authored words."""
    cao = _erya_chars("erya_shicao.txt")
    mu = _erya_chars("erya_shimu.txt")
    # 木-radical chars mean "wooden thing" as often as "tree" —
    # so radical 75 requires attestation in the TREE chapter 釋木
    # itself; the herb radicals may come from either chapter.
    out = {c for c in (cao | mu)
           if radicals().get(c) in PLANT_RADICALS - {75}} \
        | {c for c in mu if radicals().get(c) == 75}
    return out - zh_temporal()   # calendrical canon outranks radical attestation (秋)


@_lazy
def zh_temporal():
    """DERIVED: 爾雅 釋天 calendrical sections (attested chars minus
    particles) ∪ chars with Kangxi radical 日/夕 (the lexicographic
    semantic classifiers for day/evening). Both sources citable."""
    # 釋天's season EPITHETS (青陽/白藏/玄英…) leak color chars —
    # cross-domain collisions resolve to the color canon (declared).
    return (_erya_chars("erya_shitian_calendrical.txt") | gy_gloss_temporal()) \
        - ZH_COLOR - set("英藏")

def zh_time_rad(c):
    return radicals().get(c) in TIME_RADICALS

# color zh: DERIVED — canonical 五色 (#58, 2026-07-26: the AUTHORED-INTERIM ⚠
# is RETIRED by this cited derivation). Anchor = 禮記·玉藻 五色 (正色/間色),
# zh.wikisource PD (the erya precedent): "衣正色，裳間色" —
#   正色 (五方正色): 青 赤 黃 白 黑    (五間色, 禮記正義 皇侃疏 / 白虎通·衣裳):
#   綠 紅 碧 紫 駵黃.
# The set OPERATIONALIZES that canon over the corpus's actual colour tokens
# (Option A, reports/colour_descriptive_proposal_58.md, field-owner-adopted):
#   · 正色-red is carried by the occurring red-shade graphs 朱/紅, not the
#     archaic 赤 graph (赤 non-occurring here; membership-only, omitted);
#   · 翠 (kingfisher-green) · 黛 (blue-black brow pigment) · 素 (undyed/white)
#     are canon-adjacent traditional colour vocabulary, KEPT for continuity;
#   · 蓝(藍) ADDED — the one occurring clean gap-fill (青 conflates blue/green;
#     the 正/間 canon and the prior set had no standalone blue);
#   · 碧 (a 間色) is DELIBERATELY held latent (Option A: a tight char set keeps
#     latent-only colour graphs latent — the latent/stated distinction the
#     paper turns on); it fires only inside compounds (碧色/碧綠…, ZH_COMPOUNDS).
# 廣韻 色-gloss sweep = GAP-CHECK ONLY, NOT wired (it surfaced 碧; 124 chars,
# ~all horse-coat/dyed-silk dead weight on this corpus — proposal Leg C).
# The zh COMPOUND colour tier (中国传统色, 144 names) lives in ZH_COMPOUNDS.
ZH_COLOR = set("青朱紅紫綠翠黛素白黑黃蓝藍")
ZH_COLOR_FLAG = set("金")

# color en: DERIVED — Berlin & Kay (1969) 11 basic terms ∪ XKCD color
# survey single-token names (xkcd.com/color/rgb.txt, CC0).
BK11 = {"black","white","red","green","yellow","blue","brown","purple",
        "pink","orange","grey"}
# ═══ THE EN-COLOUR YIELD LAW (rulings #61, ruled by Anneliese, of record,
# 2026-07-27/28 night; build agent) — ONE coherent law so we don't confuse
# ourself down the road. What the base yields, and what it does NOT, when a
# name is claimed by another field. Provenance receipts, all four rulings:
#   · flag-not-delete doctrine: commit 50cb569 (nuit FLAGGED not gated —
#     "priced not hidden"); the fr precedent this en side now mirrors.
#   · the OLD "names yield to the other field" (plant subtraction): commit
#     c65c3b4 + reports/arm1_calibration_v11_20260715.md L134 ("en plant =
#     WordNet closure … + naive plural folding"). That blanket subtraction
#     ate BK11 basics orange+pink AND colour names rose/violet/olive/lavender/
#     lilac/peach/plum/cherry/mint/sage/mustard/fern (72 xkcd∩en_plant names) —
#     the #61 rosy pseudo-ghost's second cause (commit 6bf9088).
#   · cross-field EXCLUSIVITY that DOES hold (twilight/dusk yield to temporal):
#     arm-1 receipt L134 ("cross-domain exclusivity (twilight yields to
#     temporal)"). KEPT — a true different-quantity fact.
# (a) BK11 BASICS NEVER YIELD to anything (Berlin & Kay 1969: the 11 basic
#     colour terms are the field's own foundation; a basic term outranks any
#     other field's claim on the same string). orange/pink restored.
# (b) xkcd names colliding with en_plant() are NOT deleted — they become
#     FLAG-CLASS (fire + declared polysemy), exactly mirroring the fr nuit ruling
#     (50cb569 — the live exemplar; EN_COLOR_FLAG itself is empty after the #61
#     no-vibes audit removed gold+fair): the type-prior fires, wears the price tag,
#     zero occurrence intervention. See en_color_plant_flag().
# (c) en_temporal() subtraction KEPT (true cross-field exclusivity, not polysemy:
#     twilight/dusk ARE the other field; arm-1 receipt L134). Not flagged —
#     yielded, because the colour reading is not co-present, it is the wrong
#     field. This is the ONE blanket subtraction that survives.
# (d) EN_COLOR_YIELD_RULED — per-word ruled yields (named, citable, appendable).
#     "dark" (xkcd name) yields to ILLUMINATION — her ruling tonight after the
#     correspondances en:dillon L7 "darkness" finding: were an EN morphological
#     fold to fold darkness→dark, xkcd's "dark" would wrongly state the line
#     COLOUR; dark is the illumination field's, not colour's. Yielded (removed),
#     not flagged: like temporal, it is the wrong field, not co-present polysemy.
EN_COLOR_YIELD_RULED = {
    "dark": "illumination",   # #61, dillon "darkness" finding — dark is illum's
}
@_lazy
def en_color_plant_flag():
    """DERIVED flag-class (ruling b, #61): the xkcd colour names that COLLIDE
    with en_plant() — NOT the BK11 basics (they never yield, ruling a), NOT the
    temporal-exclusive names (ruling c), NOT the ruled-yield names (ruling d).
    These fire COLOUR carrying a declared-polysemy flag (the plant sense is the
    other reading), byte-mirroring the fr nuit ruling (50cb569) — the live
    flag-class exemplar now that EN_COLOR_FLAG is empty (gold+fair both removed at
    the #61 no-vibes audit). The receipt says COLOUR fired; the flag prices the
    plant polysemy, not hidden."""
    return (_en_xkcd_base() & en_plant()) - set(BK11) \
        - en_temporal() - set(EN_COLOR_YIELD_RULED)


@_lazy
def _en_xkcd_base():
    """BK11 ∪ {gray} ∪ xkcd single-token colour names (xkcd_rgb.txt, CC0) —
    the raw en colour base BEFORE any yield. Shared by en_color() and the
    flag-class derivation so the two partition the same source exactly."""
    out = set(BK11) | {"gray"}
    f = V / "xkcd_rgb.txt"
    if f.exists():
        for ln in open(f, encoding="utf-8"):
            name = ln.split("\t")[0].strip()
            if name and " " not in name and "/" not in name and name.isalpha():
                out.add(name.lower())
    return out


@_lazy
def en_color():
    """DERIVED — Berlin & Kay (1969) 11 basic ∪ XKCD single-token (CC0), under
    THE EN-COLOUR YIELD LAW above. The CLEAN-fire colour set: what fires colour
    with no flag. Its complement inside the base is the flag-class
    (en_color_plant_flag) + the yielded names (temporal / ruled)."""
    out = set(_en_xkcd_base())
    out -= EN_COLOR_FLAG                 # EMPTY set now (gold + fair both REMOVED,
                                         # #61 no-vibes audit) → subtracts nothing;
                                         # kept live so a future CITED flag drops in
    out -= en_temporal()                 # (c) true cross-field exclusivity (twilight/dusk)
    out -= set(EN_COLOR_YIELD_RULED)     # (d) per-word ruled yields (dark→illumination)
    out -= en_color_plant_flag()         # (b) plant-collision names move to flag-class…
    out |= set(BK11)                     # (a) …but BK11 basics NEVER yield (orange/pink restored)
    return out
# EN_COLOR_FLAG — the NO-VIBES-FLAG audit (#61, 2026-07-28, her law: "we should
# not manually flag anything because we think so… if {gold, fair} is without
# support we should remove them"). The provenance hunt (git -S EN_COLOR_FLAG +
# arm-1 era docs) found BOTH gold and fair were HAND-DECLARED from chair memory
# (b8feacd) and grandfathered UNCITED through the c65c3b4 cited-derivation cleanup
# (arm1_calibration_v11_20260715.md: the authored lexicons were declared
# "PROVENANCE-INVALID for the paper"). Neither carries a polysemy citation. BOTH
# are now GONE — the set is EMPTY:
#   · gold — REMOVED at the audit (4629cdf, receipts-only, census byte-identical BY
#     CONSTRUCTION): gold is a BK/xkcd basic colour (xkcd 'gold #dbb40c'), so with
#     the flag gone it fires CLEAN colour via en_color() (state stays 'stated'; the
#     census reads fires==True unchanged — PROVEN at that build's end).
#   · fair — REMOVED now (v4.9, this sitting). She RULED at the #61 fork where the
#     audit HELD it: "remove fair. (though it is a color for makeup foundation,
#     lol)". fair is NOT a colour word in ANY lexicon (not xkcd, not BK11); it only
#     ever fired colour BECAUSE of this hand-declared flag — so post-removal it
#     fires NOTHING (no set, no flag channel). This is NOT receipts-only: it flips
#     the colour fire-state on the 5 census lines where 'fair' is the SOLE colour
#     trigger (qingqing xu_yuanchong L3 · qingqing waley_1918 L9 · correspondances
#     scott_1909 L10 · invitation millay L5 · elevation dillon L16: stated→silent,
#     or →ghost if another token line-scalars colour-hot). Those 5 flips + one
#     receipt-only drop (qingqing en:birrell L5, where 'rouge' — a clean xkcd
#     colour — co-fires, so the cell STAYS stated and only the 'fair' receipt
#     leaves) are the entire ruled colour-only delta; the census re-baselines
#     v4.8→v4.9 under her ruling (the byte-identity the audit protected is
#     deliberately spent here, per her word). See the #61 flag audit (4629cdf) +
#     its receipts + linegrain_census_v49_61.py.
# The EMPTY-SET MECHANISM IS KEPT, deliberately (NOT collapsed to a bare no-op):
# EN_COLOR_FLAG stays a live set that en_color() subtracts and label_unit unions
# into en_flags, so any FUTURE en colour flag must arrive WITH A CITATION (her
# no-vibes-flag law, 950d10b: flags require citable support) and drops in here —
# the channel exists, it is simply empty of uncited memory. (A citable colour
# inventory — e.g. a documented fashion/commerce swatch source — could one day
# repopulate this and the base honestly; until such a source lands, the set is
# empty and flags return ONLY with citations.)
EN_COLOR_FLAG = set()      # EMPTY — gold + fair both REMOVED (uncited, #61 no-vibes
                            # audit; fair per her v4.9 ruling "remove fair"). Kept as
                            # a live (empty) set: a future flag needs a CITATION to
                            # enter here. Post-removal 'fair' fires nothing (not in
                            # any lexicon) → 5 census cells flip + birrell L5 receipt
                            # drop; census re-baselined v4.9. See linegrain_census_v49.

# EN morphological fold (#61 Stage 2): variant→lemma map, LOADED AS DATA from
# the committed en_color_variants_61.json (built by engine/
# en_morph_fold_61.py from WordNet-'+' ∪ Wiktextract — no hand-authored rows).
# The en sibling of the zh Unihan fold and the fr paradigm map: a colour variant
# (rosy, reddish, roses) fires AS its lemma; a variant of a flag-class base
# inherits flag-class (rosy → rose → fires-with-flag). Consulted BEFORE the
# set/flag intersection in label_unit (mirrors the fr _var2lemma wiring, 2ebf673:
# the CONSUMING path must consult the map, or the numbers don't move).
def _load_variant_map(path, key):
    """variant(lower) -> lemma(lower) from a committed *_variants_61.json under
    `key`. Shared loader for the colour and sound folds (identical artifact
    shape). DATA-ONLY load: EMPTY when the artifact is absent — drop-and-declare,
    an unmapped variant stays unfired, never hand-authored around."""
    out = {}
    if path.exists():
        d = json.loads(path.read_text(encoding="utf-8"))
        for var, rec in (d.get(key) or {}).items():
            out[var] = rec["lemma"]
    return out


# committed artifact home: lexical_resources/color_lexicon/ (vectors/ is
# gitignored). ROOT = the repo root anchor defined at the top of this file.
@_lazy
def en_var2lemma():
    """variant(lower) -> lemma(lower), the en colour fold. Data-only load of
    the committed artifact; empty if absent (drop-and-declare: unmapped variants
    stay unfired, never hand-authored around)."""
    return _load_variant_map(
        ROOT / "lexical_resources" / "color_lexicon" / "en_color_variants_61.json",
        "en")

# EN SOUND morphological fold (#61 Task 4): the SOUND sibling of the colour fold,
# LOADED AS DATA from the committed en_sound_variants_61.json (built by
# engine/en_sound_morph_fold_61.py — verbal+plural inflection rule-
# generated ∪ WordNet-'+'/Wiktextract-cited derivation, collision-vetoed, no hand-
# authored rows). A sound variant (clacking, ringing, hums) fires AS its lemma
# (clack, ring, hum). No sound flag-class exists → every variant is clean sound.
# Consulted BEFORE the sound set intersection in label_unit (the 2ebf673 lesson).
@_lazy
def en_sound_var2lemma():
    """variant(lower) -> lemma(lower), the en SOUND fold. Data-only load of the
    committed artifact; empty if absent (drop-and-declare: unmapped variants stay
    unfired, never hand-authored around). The 'clacking' specimen's fix."""
    return _load_variant_map(
        ROOT / "lexical_resources" / "audio_witness" / "en_sound_variants_61.json",
        "en_sound")

# ---------- WordNet 3.0 noun closures (shared by en_plant + en_sound_word) ----
def _wn_noun_index():
    """Parse vectors/wordnet30/data.noun into (words, kids): synset offset ->
    raw lemma list, offset -> hyponym (~) child offsets. Empty when the file is
    absent. NOT memoised on purpose: each closure below builds its set once, and
    caching this index would retain the whole parsed noun database for the life
    of the process (the per-function parses it replaces did not)."""
    words, kids = {}, {}
    dat = V / "wordnet30/data.noun"
    if dat.exists():
        for ln in open(dat, encoding="utf-8", errors="ignore"):
            if not ln[:1].isdigit():
                continue
            p = ln.split()
            off, w_cnt = p[0], int(p[3], 16)
            words[off] = [p[4 + 2*i] for i in range(w_cnt)]
            ptrs = ln.split("|")[0].split()
            for i, t in enumerate(ptrs):
                if t == "~":
                    kids.setdefault(off, []).append(ptrs[i+1])
    return words, kids


def _wn_hyponym_closure(roots, words, kids):
    """Walk ~ downward from `roots`; harvest single-word alphabetic lemmas,
    lowercased. One implementation for the flora closure (en_plant) and the
    auditory closure (en_sound_word) — same walk, different roots."""
    out, seen, stack = set(), set(), list(roots)
    while stack:
        o = stack.pop()
        if o in seen or o not in words:
            continue
        seen.add(o)
        out |= {w.lower() for w in words[o] if "_" not in w and w.isalpha()}
        stack.extend(kids.get(o, []))
    return out


# plant en: DERIVED — WordNet 3.0 hyponym closure of plant.n.02
# (flora sense; lex_filenum 20 root), single-word lemmas.
@_lazy
def en_plant():
    words, kids = _wn_noun_index()
    # plant.n.02 lives in noun.Tops (lex 03), not noun.plant — located by its own
    # lemma set, first match in file order (as before).
    root = next((off for off, ws in words.items()
                 if "plant" in ws and "flora" in ws), None)
    roots = ([root] if root else []) \
        + [off for off, ws in words.items() if "plant_part" in ws]   # plant parts join the closure
    return _wn_hyponym_closure(roots, words, kids)

# ---------- SOUND, WORD-TIER (#58, 2026-07-26) ----------------------
# "does this word DIRECTLY DESCRIBE sound" (歌聲/噪/鳴/noise/song). This
# is the DESCRIPTIVE tier — distinct from the DEVICE tier (叠字/雙聲/
# 聯綿/allit/word-rep) which now emits under key "sound_device".
# Design-fixed: strings are referent-tier THINGS, not sound-descriptions
# (弦 must NOT fire on 上有弦歌聲; 歌聲 must). Three citable legs,
# mirroring zh_temporal()'s recipe (爾雅 attestation ∪ 廣韻 gloss-head,
# with a radical leg), all sources PD/CC0.
#   釋樂  definiendum chars of 爾雅釋樂第七 (zh.wikisource, PD): the terms
#         BEING DEFINED (text before each 謂之), i.e. the canonical
#         sound/instrument vocabulary — NOT the definientia.
#   音部  Kangxi radical 180 音 (Unihan kRSUnicode): the lexicographic
#         semantic classifier for sound (音韻響韶…), free-standing leg.
#   廣韻  chars whose 廣韻 釋義 head matches a sound-definiens seed
#         (tshet-uinh CC0), GY_SOUND_SEEDS declared below.
# Derivation receipts / rejected seeds / collision rule: build note
# reports/sound_word_labeler_build_58.md.
def _erya_shiyue_definienda():
    """DERIVED: definiendum-position chars of 爾雅釋樂 — per [，。；]-clause,
    the CJK before each 謂之, minus particles. The DEFINED terms only
    (灑/離/鼖… definientia deliberately excluded)."""
    s = set()
    p = V / "erya_shiyue.txt"
    if p.exists():
        for clause in re.split(r"[，。；]", p.read_text(encoding="utf-8")):
            if "謂之" in clause:
                s |= set(re.findall(r"[㐀-鿿𠀀-𪛟]", clause.split("謂之")[0]))
    return s - ZH_PARTICLES

# 廣韻 sound-definiens seeds — DECLARED before any scoring run (mirror of
# GY_TEMPORAL_SEEDS); matched against the gloss HEAD only (before 又/亦).
# 樂也 REJECTED (pulls 31 joy chars 康悅愉愷娛僖…); bare 鳴/聲 REJECTED
# (49/446 pulls); coverage gaps 噪(gloss='上同' cross-ref)·啼(empty head)
# and the correct 笑=joy non-fire are recorded in the build note.
GY_SOUND_SEEDS = ("聲也","音也","鳴也","響也","歌也","吟也","啼也","叫也",
                  "呼也","喚也","哀聲","呻吟","嘶",
                  "聲音","鼓聲","鐘聲","雷聲","鳥聲","犬聲","樂器")
def gy_gloss_sound():
    """DERIVED: chars whose 廣韻 釋義 head matches a sound-definiens seed."""
    return _gy_gloss_chars(GY_SOUND_SEEDS) - ZH_PARTICLES


@_lazy
def _zh_sound_legs():
    """(union, 釋樂-set, 音部-set, 廣韻-set) with collisions resolved."""
    leg_erya = _erya_shiyue_definienda()
    leg_rad  = {c for c, n in radicals().items() if n == 180}
    leg_gy   = gy_gloss_sound()
    # Cross-domain collisions with the temporal field (商·章) resolve
    # by a DECLARED rule: temporal collision yields to temporal EXCEPT
    # where sound membership is by 釋樂 definiendum CANON (a named
    # source), which outranks a temporal gloss/radical pull. Keeps 商
    # (note-name in 釋樂 ∧ temporal — kept per design) and drops 章
    # (calendrical 章; in sound only via radical 音). This is the
    # house rule "calendrical canon outranks radical attestation (秋)".
    # (∩ ZH_COLOR and ∩ zh_plant are empty; verified in build note.)
    drop = ZH_PARTICLES | ZH_COLOR | (zh_temporal() - leg_erya)
    union = (leg_erya | leg_rad | leg_gy) - drop
    return (union, leg_erya - drop, leg_rad - drop, leg_gy - drop)
def zh_sound():
    return _zh_sound_legs()[0]
def zh_sound_tag(c):
    """Leg tag for a fired char; priority 釋樂 > 音部 > 廣韻 (named
    definiendum canon first, then radical, then gloss-head)."""
    _, erya, rad, _gy = _zh_sound_legs()
    return "釋樂" if c in erya else "音部" if c in rad else "廣韻"

# en sound: DERIVED — WordNet 3.0 hyponym (~) closure of the auditory-
# domain synsets of sound/noise/music, single-word lemmas. Same kids-walk
# as en_plant (the flora closure). ~ is taxonomic hyponymy and EXCLUDES
# @i named-instances — which is why wordnet_lite's native closure (it
# conflates @/@i in .hyper) is NOT used here: inverting @i vacuums 77
# scripture/anthem instances (genesis, isaiah, star-spangled_banner…)
# into the set. Roots are the AUDITORY senses only — the ocean-inlet /
# statistical-noise / electrical-noise / "face the music" idiom senses
# are excluded; each offset is justified by its gloss in the build note.
EN_SOUND_ROOTS = {
    "04981139", "05718254", "06278136", "07371293", "11480930",  # sound.*: percept · sensation · audio-signal · audible-event · vibration
    "05720248", "07387509",                                       # noise.*: dissonance-percept · sound-of-any-kind
    "05718556", "05718935", "07020895",                           # music.*: euphony · produced-sounds · auditory-art
}
@_lazy
def en_sound_word():
    """DERIVED: WordNet flora-style ~ closure over EN_SOUND_ROOTS."""
    words, kids = _wn_noun_index()
    return _wn_hyponym_closure(EN_SOUND_ROOTS, words, kids)

# temporal en: DERIVED (#61 Stage 2, ruled — the AUTHORED-INTERIM ⚠ is RETIRED).
# HeidelTime English resource files → a cited word-list-of-facts (month/season/
# weekday/part-of-day/part-of-year/unit/date-word basic temporal terms), built by
# engine/en_temporal_derive_61.py and LOADED AS DATA from the committed
# lexical_resources/temporal_lexicon/en_temporal_inventory_61.json. HeidelTime is
# GPLv3; we redistribute NO HeidelTime code/patterns — a derived list of factual
# vocabulary, each term cited to its source file (the en analogue of the fr GLAWI
# gloss sweep and the zh 廣韻/爾雅 legs). CITATION OF RECORD (repo README item [4]):
#   Strötgen & Gertz (2013), Multilingual and Cross-domain Temporal Tagging,
#   Language Resources and Evaluation 47(2):269-298.
# RULED CROSS-FIELD EXCLUSIVES (EN_TEMPORAL_RULED_EXCLUSIVE) — kept SEPARATELY,
# their own citation: {twilight, dusk} yield from en_color() to temporal by the
# EN-COLOUR YIELD LAW ruling (c) (arm-1 receipt v11 L134; commit d26fa95 — "true
# cross-field exclusivity … twilight/dusk ARE the other field"). HeidelTime's
# part-of-day inventory does NOT list twilight/dusk (it uses morning/afternoon/
# evening/night/noon/midnight), so the source swap would otherwise DROP them from
# the subtraction set and wrongly re-admit them to colour. Ruling (c) is an
# independent standing ruling with its OWN receipt, not a HeidelTime fact — so it
# is unioned in explicitly, named and citable (mirroring how en_color() is BK11 ∪
# xkcd with the per-word EN_COLOR_YIELD_RULED table). This is NOT a hand-authored
# temporal lexicon: it is (cited HeidelTime inventory) ∪ (named standing ruling).
EN_TEMPORAL_RULED_EXCLUSIVE = {"twilight", "dusk"}   # ruling (c), arm-1 L134 / d26fa95
@_lazy
def en_temporal():
    """The en temporal set: HeidelTime-derived inventory ∪ the ruled cross-field
    exclusives. Data-only load of the committed artifact; on absence, DROP-AND-
    DECLARE — falls back to the ruled-exclusive set alone (never re-hand-authored;
    the absence is visible as a near-empty temporal field, honest).
    #71: this was the file's one EAGER import-time load (module-level
    `EN_TEMPORAL = _load_en_temporal()`); it is now the same lazy getter every
    sibling lexicon uses. Identical contents and call-time values — the set is
    built from a committed artifact that nothing mutates."""
    out = set(EN_TEMPORAL_RULED_EXCLUSIVE)
    f = ROOT / "lexical_resources" / "temporal_lexicon" / "en_temporal_inventory_61.json"
    if f.exists():
        d = json.loads(f.read_text(encoding="utf-8"))
        out |= set((d.get("en") or {}).keys())
    return out
ZH_TEMPORAL_FLAG = set("月")   # moon-vs-month; 日 now via radical rule

# 聯綿詞 (lexicalized binomes) — the canonical 雙聲/叠韵 device class.
# v2.2: phoneme pairs count ONLY here (free adjacent-pair detection
# over-fired on chance homophony across word boundaries; gated until
# segmentation-aware detection lands).
ZH_BINOMES = set("""玲瓏 徘徊 窈窕 參差 参差 蕭瑟 萧瑟 逍遙 逍遥 蜿蜒
彷彿 仿佛 憔悴 躊躇 踌躇 慷慨 淋漓 爛漫 烂漫 朦朧 朦胧 磅礴 繽紛 缤纷
惆悵 惆怅 逶迤 婀娜 芳菲 玲琅 琳瑯 琳琅 蹉跎 崔嵬 嶙峋 潺湲 潺潺
輾轉 辗转 依稀 汪洋 蒼茫 苍茫 渺茫 縹緲 缥缈 崢嶸 峥嵘 荒唐 匍匐
瀟灑 潇洒 婆娑 齟齬 齷齪 猶豫 犹豫 玲玎 叮嚀 叮咛""".split())

EN_ALLIT_STOP = {"that","this","thou","thee","then","than","they","them",
    "there","these","those","thine","with","what","when","where","which","will"}

# zh compounds: matched first (maximal-match, longest key first), consume
# chars, carry own category (None = no trait category; suppresses
# component-char hits). Two tiers:
#
#   (1) the 7 legacy DISAMBIGUATION entries below — AUTHORED-INTERIM ⚠
#       (contents picked from dev FPs 07-15, pre-rule; replacement path =
#       HowNet multi-char DEF lookup). KEPT for continuity (#58).
#
#   (2) the COLOUR compound tier (#58, 2026-07-26) — DERIVED, citable:
#       中国传统色 (traditional Chinese colour names), 144 compound names from
#       lexical_resources/color_lexicon/chinese_colors_zerosoul_20260720.json
#       (github.com/zerosoul/chinese-colors, MIT © 2019 Tristan Yang; upstream
#       a Sina 中国传统颜色 blog post, opaque beyond that — DISCLOSE in
#       publication; PROVENANCE.md / ACQUISITION_STATUS.md). 144 = the 161 leaf
#       names − 16 single-char names (char tier / ZH_COLOR) − 1 four-char data
#       anomaly 绀青绀紫 (dropped). Compound grain is COLLISION-SAFE (月白≠月,
#       水色≠水, 竹青≠竹): the maximal-match masks the whole span before the
#       char-harvest, so a colour name built on a plant/temporal char (松柏绿/
#       柳绿/竹青/秋色/玄色…) fires COLOUR and does NOT leak that char to plant/
#       temporal — the hound-tension vanishes at compound grain. Only 4 of the
#       144 occur in the corpus (琥珀 金色 青翠 雪白; none carries a cross-field
#       char — verified, so the shared masking machinery leaves plant/temporal/
#       sound byte-identical). Simplified forms ONLY: no in-house opencc-style
#       simp→trad resource exists (checked), so the traditional twins are NOT
#       hand-authored (provenance rule) — a documented simp-only LIMITATION.
#       The 4 corpus-occurring names are script-invariant (simp==trad), so this
#       limitation costs no verdict on this corpus. Rationale/sizing:
#       reports/colour_descriptive_proposal_58.md (Option A, field-owner-adopted).
ZH_COMPOUNDS = {
    # -- (1) legacy disambiguation (AUTHORED-INTERIM ⚠) --
    "竹馬": None, "竹马": None,          # hobby-horse: toy, not plant
    "楊柳": "plant", "杨柳": "plant", "芙蓉": "plant", "青草": "plant",
    "白露": ("temporal", "color"),
    "落日": "temporal",        # solar term AND white dew — dual-typed
    "水晶": None,                         # crystal: not water-the-field
    # -- (2) 中国传统色 colour compound tier (144, zerosoul MIT; simp-only) --
    "粉红": "color", "妃色": "color", "品红": "color", "桃红": "color", "海棠红": "color", "石榴红": "color",
    "樱桃色": "color", "银红": "color", "大红": "color", "绛紫": "color", "绯红": "color", "胭脂": "color",
    "朱红": "color", "茜色": "color", "火红": "color", "赫赤": "color", "嫣红": "color", "洋红": "color",
    "枣红": "color", "殷红": "color", "酡红": "color", "酡颜": "color", "鹅黄": "color", "鸭黄": "color",
    "樱草色": "color", "杏黄": "color", "杏红": "color", "橘黄": "color", "橙黄": "color", "橘红": "color",
    "姜黄": "color", "缃色": "color", "橙色": "color", "茶色": "color", "驼色": "color", "昏黄": "color",
    "栗色": "color", "棕色": "color", "棕绿": "color", "棕黑": "color", "棕红": "color", "棕黄": "color",
    "赭色": "color", "琥珀": "color", "褐色": "color", "枯黄": "color", "黄栌": "color", "秋色": "color",
    "秋香色": "color", "嫩绿": "color", "柳黄": "color", "柳绿": "color", "竹青": "color", "葱黄": "color",
    "葱绿": "color", "葱青": "color", "葱倩": "color", "青葱": "color", "油绿": "color", "绿沈": "color",
    "碧色": "color", "碧绿": "color", "青碧": "color", "翡翠色": "color", "草绿": "color", "青色": "color",
    "青翠": "color", "青白": "color", "鸭卵青": "color", "蟹壳青": "color", "鸦青": "color", "绿色": "color",
    "豆绿": "color", "豆青": "color", "石青": "color", "玉色": "color", "艾绿": "color", "松柏绿": "color",
    "松花绿": "color", "松花色": "color", "靛青": "color", "靛蓝": "color", "碧蓝": "color", "蔚蓝": "color",
    "宝蓝": "color", "蓝灰色": "color", "藏青": "color", "藏蓝": "color", "黛绿": "color", "黛蓝": "color",
    "黛紫": "color", "紫色": "color", "紫酱": "color", "酱紫": "color", "紫檀": "color", "紫棠": "color",
    "青莲": "color", "群青": "color", "雪青": "color", "丁香色": "color", "藕色": "color", "藕荷色": "color",
    "苍色": "color", "苍翠": "color", "苍黄": "color", "苍青": "color", "苍黑": "color", "苍白": "color",
    "水色": "color", "水红": "color", "水绿": "color", "水蓝": "color", "淡青": "color", "湖蓝": "color",
    "湖绿": "color", "精白": "color", "象牙白": "color", "雪白": "color", "月白": "color", "荼白": "color",
    "霜色": "color", "花白": "color", "鱼肚白": "color", "莹白": "color", "灰色": "color", "牙色": "color",
    "铅白": "color", "玄色": "color", "玄青": "color", "乌色": "color", "乌黑": "color", "漆黑": "color",
    "墨色": "color", "墨灰": "color", "黑色": "color", "缁色": "color", "煤黑": "color", "黝黑": "color",
    "赤金": "color", "金色": "color", "银白": "color", "老银": "color", "乌金": "color", "铜绿": "color",
}

RE_AA = re.compile(rf"([{CJK}])\1")                    # 叠字 AA
RE_AABB = re.compile(rf"([{CJK}])\1([{CJK}])\2")       # AABB
RE_EN_WORD = re.compile(r"[A-Za-z']+")
RE_WORD_REP = re.compile(r"\b([A-Za-zÀ-ÿ]{3,})\b(?:\W+\w+){0,3}?\W+\b\1\b", re.I)

_SIBLING_WARNED = set()


def _sibling_build(subdir, module):
    """Lazy import of a sibling language build (engine/<subdir>/<module>.py).
    One importer for the fr and de colour legs. Both are LANGUAGE-GATED at the
    CALL SITE (consulted only when lang matches), so every other language's
    output is byte-identical whether or not these trees are present.

    Returns None (once-warned) when the build tree is absent. This public
    artifact ships the committed per-board score legs, not the fr/de build
    sources, so a fresh fr/de labelling run degrades the colour leg to empty
    rather than aborting; the committed score legs already carry these results.
    Fetch the build trees per fetch_verify.sh for a full fr/de labelling run."""
    sys.path.insert(0, str(ROOT / "engine" / subdir))
    try:
        return importlib.import_module(module)
    except ImportError:
        if subdir not in _SIBLING_WARNED:
            _SIBLING_WARNED.add(subdir)
            sys.stderr.write(
                f"[trait_labelers] optional sibling build engine/{subdir} absent — "
                f"{module} colour leg skipped (see fetch_verify.sh)\n")
        return None


def _fr():
    """fr colour leg (her convening 07-28: 'Plug the fr branch in') — lazy
    import from the fr build; language-gated at the call (only consulted when
    lang == 'fr', per the integration proposal's recommended gating: en/zh
    outputs stay byte-identical)."""
    return _sibling_build("fr_build", "fr_labelers")


def _de():
    """de colour leg (#61 night build, the fr blueprint — de first, unlocks the
    bethge/forke crossings). Lazy import from engine/de_build; language-
    gated at the call (consulted only when lang == 'de'), so en/zh/fr outputs stay
    BYTE-IDENTICAL. Colour-only, citation-tier (B&K12-de ∪ kaikki-adj-colour-
    sense; forward paradigm generation for German declension + ß/ss orthography)."""
    return _sibling_build("de_build", "de_labelers")


# ---------- label_unit, one helper per emitted field -------------------------
# EVALUATION ORDER IS LOAD-BEARING and is unchanged by the #71 split: compound
# masking runs FIRST (it consumes whole spans before any per-char harvest, which
# is what keeps a colour compound built on a plant/temporal char — 松柏绿/竹青 —
# from leaking that char to plant/temporal; see ZH_COMPOUNDS), then the naive en
# fold, then sound_device, then colour with its language branches AS-IS, then the
# de language gate, then plant/temporal/sound off the gated word set. Each helper
# returns the field's (hit, evidence, flags) 3-tuple, or None for "does not fire".

def _mask_compounds(text):
    """Maximal-match (longest key first) over ZH_COMPOUNDS → (compound_hits:
    field -> [compound], masked text). Each matched span becomes ◌ fillers so its
    component chars are consumed before any char-harvest. Runs first, for ALL
    fields — the shared masking machinery, the declared risk channel."""
    compound_hits = {}   # field -> [compound]
    masked = text
    for w in sorted(ZH_COMPOUNDS, key=len, reverse=True):
        if w in masked:
            cat = ZH_COMPOUNDS[w]
            for c in ((cat,) if isinstance(cat, str) else (cat or ())):
                compound_hits.setdefault(c, []).append(w)
            masked = masked.replace(w, "◌" * len(w))
    return compound_hits, masked


def _fold_en_words(text):
    """Lowercased en tokens ∪ their NAIVE plural/-ves folds (arm-1 receipt v11
    L134: 'en plant = WordNet closure … + naive plural folding'). This is the
    crude fold that runs for every field; the cited morphological folds
    (en_var2lemma / en_sound_var2lemma) are consulted per field on top of it."""
    en_words = {w.lower() for w in RE_EN_WORD.findall(text)}
    folded = set(en_words)
    for w in list(en_words):
        if w.endswith("ves"): folded.add(w[:-3] + "f")
        if w.endswith("es"):  folded.add(w[:-2])
        if w.endswith("s"):   folded.add(w[:-1])
    return folded


def _label_sound_device(text):
    """DEVICE tier (euphony ENACTED), #58: 叠字 · word-repetition · 雙聲/叠韵 ·
    en alliteration. Phoneme tier = declared approximations (pypinyin for Middle
    Chinese where 廣韻 does not cover; orthographic alliteration where CMU does
    not). #58: the output key was RENAMED "sound" -> "sound_device" — this is the
    device tier, distinct from the word-tier "sound"; receipt format unchanged."""
    # sound-as-device: 叠字 · word-repetition · 雙聲/叠韵 · en alliteration
    aa = RE_AA.findall(text)
    rep = RE_WORD_REP.search(text)
    dev = []
    if aa: dev.append("叠字:" + "".join(f"{c}{c}" for c in aa))
    if rep: dev.append(f"rep:{rep.group(1)}")
    zh_seq = re.findall(rf"[{CJK}]", text)
    if HAVE_PINYIN and len(zh_seq) >= 2:
        inits = [p[0] for p in pinyin(zh_seq, style=Style.INITIALS, strict=False)]
        fins  = [p[0] for p in pinyin(zh_seq, style=Style.FINALS, strict=False)]
        for i in range(len(zh_seq) - 1):
            pair = zh_seq[i] + zh_seq[i+1]
            if pair not in ZH_BINOMES or zh_seq[i] == zh_seq[i+1]:
                continue
            mc = mc_pair_device(zh_seq[i], zh_seq[i+1]) if gy() else None
            if mc:
                dev.append(f"{mc}(中古):{pair}")
            elif inits[i] and inits[i] not in "yw" and inits[i] == inits[i+1]:
                dev.append(f"雙聲:{pair}")
            elif fins[i] and fins[i] == fins[i+1]:
                dev.append(f"叠韵:{pair}")
            else:
                dev.append(f"聯綿:{pair}")
    words = RE_EN_WORD.findall(text)
    content = [w for w in words if len(w) > 3 and w.lower() not in EN_ALLIT_STOP]
    for i in range(len(content) - 1):
        a, b = content[i].lower(), content[i+1].lower()
        if a == b:
            continue
        pa, pb = cmu().get(a), cmu().get(b)
        if pa and pb:
            same = pa[0] == pb[0] and pa[0][-1] not in "012"   # initial CONSONANT phoneme
        else:
            same = content[i][0].lower() == content[i+1][0].lower()  # fallback: letters
        if same:
            dev.append(f"allit:{content[i]}-{content[i+1]}")
    if not dev:
        return None
    return (True, " ".join(dev), "AABB" if RE_AABB.search(text) else "")


def _label_color(text, lang, zh_chars, en_words, compound_hits):
    """COLOUR — zh char tier (ZH_COLOR) ∪ zh compound tier (中国传统色, consumed
    by the mask upstream) ∪ the en base under THE EN-COLOUR YIELD LAW, plus the
    language-gated fr and de legs. The language branching is exactly as built:
    fr/de consult their OWN sets through their own paradigm maps, and the en
    xkcd base is NOT consulted on a de unit."""
    fr_ev, fr_fl = [], []
    if lang == "fr":
        F = _fr()
        if F is not None:
            fw = F._fold_fr({w.lower() for w in F._fr_tokens(text)})
            # via the PARADIGM MAP (her blanches catch): variants fire AS their
            # lemma — the raw-set intersection bypassed the gender fold
            v2l = F._var2lemma()
            lemmas = {v2l[w] for w in fw if w in v2l}
            fr_ev = sorted(lemmas & F.fr_color())
            fr_fl = sorted(lemmas & F.FR_COLOR_FLAG)
    de_ev, de_fl = [], []
    if lang == "de":
        # #61 night build: German colour leg (the fr blueprint). Consult the de
        # sets via the FORWARD PARADIGM MAP (grüner→grün, weissen→weiß). de is a
        # distinct word-language leg: on a German unit the colour evidence is
        # German-derived ONLY — the en xkcd base is NOT consulted (see the
        # lang!='de' guard below), so German words that COLLIDE with an en colour
        # name (e.g. 'fern' = German 'far' = en xkcd fern; 'Rosen' → en 'rose')
        # do NOT false-fire as colour. This gating is exactly the fr-integration
        # 'or'-collision containment (PROPOSED_INTEGRATION_trait_labelers.md),
        # sharpened for de where the collisions are genuine German non-colour
        # words. en/zh/fr/None paths are UNCHANGED (byte-identical).
        D = _de()
        if D is not None:
            dw = D._fold_de({w for w in D._de_tokens(text)})
            dv2l = D._var2lemma()
            dlemmas = {dv2l[w] for w in dw if w in dv2l}
            de_ev = sorted(dlemmas & D.de_color())
            de_fl = sorted(dlemmas & D.DE_COLOR_FLAG())
    # en flag-class (#61 ruling b): EN_COLOR_FLAG (now EMPTY — gold+fair removed at
    # the no-vibes audit; kept live so a future CITED flag drops in) ∪ the plant-
    # collision names (en_color_plant_flag), which fire COLOUR carrying a
    # declared-polysemy flag, byte-mirroring the fr nuit ruling (50cb569).
    en_flags = EN_COLOR_FLAG | en_color_plant_flag()
    # via the EN FOLD (#61 Stage 2, mirroring the fr paradigm-map wiring): a
    # colour variant fires AS its lemma (rosy→rose, reddish→red, roses→rose) —
    # consult en_var2lemma BEFORE the intersection, receipts stay LEMMA-keyed
    # (fr law). Identity rows keep base matches; unmapped words fall through
    # unchanged (they simply won't hit a colour set). The naive-folded en_words
    # feed the map too, so a fold the map lacks still reaches its base.
    # LANGUAGE GATE: the en colour base is NOT consulted on German units (lang ==
    # 'de'), so genuine German non-colour words that collide with en xkcd names
    # (fern/Rosen…) do not leak — de fires ONLY the de sets. en/zh/fr/None are
    # byte-identical (the gate is a no-op for every non-'de' lang).
    if lang == "de":
        en_col_ev, en_col_fl = [], []
    else:
        _v2l = en_var2lemma()
        en_color_lemmas = en_words | {_v2l[w] for w in en_words if w in _v2l}
        en_col_ev = sorted(en_color_lemmas & en_color())
        en_col_fl = sorted(en_color_lemmas & en_flags)
    ev = sorted(zh_chars & ZH_COLOR) + compound_hits.get("color", []) + en_col_ev + fr_ev + de_ev
    fl = sorted(zh_chars & ZH_COLOR_FLAG) + en_col_fl + fr_fl + de_fl
    if not (ev or fl):
        return None
    return (True, " ".join(ev + fl), "flagged:" + " ".join(fl) if fl else "")


def _label_plant(zh_chars, en_words_other, compound_hits):
    """PLANT (zh: 爾雅 釋草/釋木 ∧ Kangxi radical · en: WordNet flora closure)."""
    ev = sorted(zh_chars & zh_plant()) + compound_hits.get("plant", []) \
         + sorted(en_words_other & en_plant())
    if not ev:
        return None
    return (True, " ".join(ev), "")


def _label_temporal(zh_chars, en_words_other, compound_hits):
    """TEMPORAL (zh: 爾雅釋天-calendrical ∪ 廣韻 gloss-head ∪ the 日/夕-radical
    rule · en: the HeidelTime-derived inventory ∪ the ruled exclusives)."""
    ev = sorted(zh_chars & zh_temporal()) \
         + sorted(c for c in zh_chars if zh_time_rad(c) and c not in zh_temporal()) \
         + compound_hits.get("temporal", []) + sorted(en_words_other & en_temporal())
    fl = sorted(zh_chars & ZH_TEMPORAL_FLAG)
    if not (ev or fl):
        return None
    return (True, " ".join(ev + fl), "flagged:" + " ".join(fl) if fl else "")


def _label_sound(zh_chars, en_words_other):
    """SOUND, WORD TIER (#58): DIRECT sound-description — zh three-leg set
    ∩ line chars (each leg-tagged) · en auditory closure ∩ folded words.
    Distinct field from "sound_device".
    #61 Task 4 — the EN SOUND FOLD (the 'clacking' specimen): consult
    en_sound_var2lemma BEFORE the intersection so an inflected sound surface
    fires AS its lemma (clacking→clack, ringing→ring); receipts stay LEMMA-keyed
    (the colour/rosy law). LANGUAGE GATE preserved: en_words_other arrives already
    emptied on de units (label_unit's gate), so the fold never leaks onto German.
    zh/fr/None unaffected (the fold is an en-only expansion of the en set match)."""
    zsnd = sorted(zh_chars & zh_sound())
    _sv2l = en_sound_var2lemma()
    en_sound_lemmas = en_words_other | {_sv2l[w] for w in en_words_other
                                        if w in _sv2l}
    esnd = sorted(en_sound_lemmas & en_sound_word())
    if not (zsnd or esnd):
        return None
    ev = [f"{c}[{zh_sound_tag(c)}]" for c in zsnd] + [f"{w}[wn]" for w in esnd]
    return (True, " ".join(ev), "")


def label_unit(text, lang=None):
    """Return dict field -> (hit, evidence, flags). Lookup/regex +
    compound-aware maximal-match (v2). A field absent from the dict did not
    fire. Emission order: sound_device · color · plant · temporal · sound."""
    compound_hits, masked = _mask_compounds(text)   # FIRST — consumes the spans
    zh_chars = set(re.findall(rf"[{CJK}]", masked))
    en_words = _fold_en_words(text)
    out = {}

    def emit(field, rec):
        if rec is not None:
            out[field] = rec

    emit("sound_device", _label_sound_device(text))
    emit("color", _label_color(text, lang, zh_chars, en_words, compound_hits))
    # LANGUAGE GATE for the en-word cross-fields on de units (#61 night build):
    # the de leg is COLOUR-ONLY (citation-tier); de plant/temporal/sound are
    # UNCOVERED (starred). The en word sets (en_plant/en_temporal/en_sound_word)
    # would otherwise FALSE-FIRE on German tokens that collide with an English
    # word — e.g. German 'aug' (Auge/eye) ∈ HeidelTime month-abbrev en_temporal(),
    # or an ASCII fragment of an umlaut-split German word. These never become a
    # covered census STATE (de non-colour is uncovered), but suppressing them
    # keeps the raw labeler output honest (no spurious German receipts) and makes
    # de a cleanly-gated colour-only leg, symmetric with the colour gate above.
    # en/zh/fr/None are UNCHANGED (the gate is a no-op for every non-'de' lang).
    en_words_other = set() if lang == "de" else en_words
    emit("plant", _label_plant(zh_chars, en_words_other, compound_hits))
    emit("temporal", _label_temporal(zh_chars, en_words_other, compound_hits))
    emit("sound", _label_sound(zh_chars, en_words_other))
    return out

# ---------- calibration ----------
# CALIBRATION INPUTS — all three live in the PRIVATE marking tree and are NOT
# shipped with the public release (see marking/tools/README.md). Named here so
# the guard below can report exactly which one is missing.
CALIBRATION_MAP = HERE.parent / "map_session_20260711" / "map_v34_PREPARED.txt"
CALIBRATION_SHEETS = HERE.parent / "sheets"
CALIBRATION_MARKS = HERE.parent / "normalized"


def _require_calibration_inputs():
    """FAIL LOUD before scoring (#71 — notify_sound doctrine: fail loud, never
    silently). --calibrate reads three private-tree inputs. When they are absent
    every counter stays 0, and the table prints P=0.00 R=0.00 F1=0.00 for every
    field — a VACUOUS table indistinguishable from a genuine zero score, over an
    empty error listing. Refuse instead of printing it."""
    missing = [str(p) for p in (CALIBRATION_MAP, CALIBRATION_SHEETS, CALIBRATION_MARKS)
               if not p.exists()]
    if not missing and not glob.glob(str(CALIBRATION_SHEETS / "sheet_*.md")):
        missing.append(f"{CALIBRATION_SHEETS}/sheet_*.md (directory present, no sheets in it)")
    if missing:
        raise SystemExit(
            "trait_labelers --calibrate: required calibration input(s) MISSING:\n  "
            + "\n  ".join(missing)
            + "\n\nThese are private-tree marking artifacts (the prepared field map, the\n"
              "marking sheets, the normalized human marks) and are deliberately not part\n"
              "of the public reproducibility release — see marking/tools/README.md.\n"
              "Without them the P/R/F1 table would be computed over ZERO units and print\n"
              "an all-zero row per field, which is not a score. Refusing to print it.\n"
              "Run `python3 trait_labelers.py` with no flag for the selftest, which needs\n"
              "only the committed lexicons.")


# load_map / sheet_units: KEPT as this module's own implementations, deliberately.
#   · load_map is functionally equivalent to normalize.load_map (same `#`-comment
#     strip, same `->` split, same lower()/strip() on both sides; only the read
#     idiom differs — file iteration here vs Path.read_text().splitlines() there,
#     which diverge only on exotic line separators no map file contains). Not
#     imported: keeping the calibration path free of a cross-tool dependency, and
#     the two have no verified shared-change history to justify collapsing them.
#   · sheet_units has NO counterpart in normalize.py. normalize.parse_file() reads
#     the same sheet format but keeps the MARKS and discards the line text; this
#     one keeps the LINE TEXT and ignores the marks. Different extractions from
#     one format — not a duplicate.
def load_map(p):
    m = {}
    for ln in open(p, encoding="utf-8"):
        ln = ln.split("#")[0].strip()
        if "->" in ln:
            a, c = [s.strip().lower() for s in ln.split("->")]
            m[a] = c
    return m

def sheet_units(path):
    units = {}
    for ln in open(path, encoding="utf-8"):
        g = re.match(r"^([LU]\d+)\s+(.+)$", ln.strip())
        if g and g.group(1) != "marks":
            units[g.group(1)] = g.group(2)
    return units

def human_fields(poem, mapping):
    """unit -> set(fields), union over markers, map applied."""
    agg = {}
    for f in glob.glob(str(CALIBRATION_MARKS / f"*_{poem}.txt")):
        for ln in open(f, encoding="utf-8"):
            g = re.match(r"^([LU]\d+)\s*:\s*(.*)$", ln.strip())
            if not g:
                continue
            for pair in g.group(2).split(";"):
                fld = pair.strip().split(",")[0].strip().lower()
                if fld:
                    agg.setdefault(g.group(1), set()).add(mapping.get(fld, fld))
    return agg

def poem_rhyme_units(units):
    """Structural END-RHYME channel. zh: MC 韻+調 shared with >=2 other
    units. en: CMU rhyme-part shared with >=1 other line-final word
    (sonnet schemes pair lines). Measured, not assumed."""
    finals, zh_mode = {}, False
    for u, text in units.items():
        chars = re.findall(rf"[{CJK}]", text)
        if chars and gy():
            finals[u] = {(r[1], r[2]) for r in gy().get(chars[-1], [])}
            zh_mode = True
        else:
            ws = RE_EN_WORD.findall(text)
            if ws:
                rp = rhyme_part(ws[-1])
                if rp:
                    finals[u] = {rp}
    hit = set()
    need = 2 if zh_mode else 1   # zh schemes chain >=3 lines; en sonnets pair
    for u, fs in finals.items():
        n = sum(1 for v, gs in finals.items() if v != u and fs & gs)
        if fs and n >= need:
            hit.add(u)
    return hit

def selftest():
    """#58 word-tier sound probes + device regression. Unit probes on
    hand-specified lines with declared expectations — NOT dev scoring."""
    def fired(o, f): return f in o and o[f][0]
    def rc(o, f):    return o[f][1] if f in o else ""
    cases = []   # (label, text, predicate(out)->bool, note)
    # -- founding line: 歌聲 must fire word-tier sound; 弦 must NOT --
    cases.append(("founding 上有弦歌聲: sound fires, 歌+聲 in receipt, 弦 not",
        "上有弦歌聲",
        lambda o: fired(o, "sound") and "歌" in rc(o, "sound")
                  and "聲" in rc(o, "sound") and "弦" not in rc(o, "sound")))
    cases.append(("negative 弦 (string=referent, not sound-desc): no sound",
        "弦", lambda o: not fired(o, "sound")))
    cases.append(("negative 山樹静 (mountain/tree/quiet): no sound",
        "山樹静", lambda o: not fired(o, "sound")))
    # -- en auditory closure; singing-noun gap documented --
    cases.append(('en "a noise of playing and singing": noise fires, '
                  "singing does NOT (verb/act gap)",
        "a noise of playing and singing",
        lambda o: fired(o, "sound") and "noise[wn]" in rc(o, "sound")
                  and "singing" not in rc(o, "sound")))
    # -- DEVICE regression: sound_device unchanged; word-tier stays clear --
    cases.append(("device 叠字 青青子衿: sound_device fires 叠字, sound(word) clear",
        "青青子衿",
        lambda o: fired(o, "sound_device") and "叠字:青青" in rc(o, "sound_device")
                  and not fired(o, "sound")))
    cases.append(("device allit 'the wild wind': sound_device fires allit",
        "the wild wind",
        lambda o: fired(o, "sound_device") and "allit:wild-wind" in rc(o, "sound_device")))
    # -- #58 COLOUR: compound-colour tier fires; char tier unchanged --
    cases.append(("colour compound 琥珀: color fires 琥珀 (neither char in ZH_COLOR)",
        "琥珀",
        lambda o: fired(o, "color") and "琥珀" in rc(o, "color")))
    cases.append(("colour compound 金色: color fires 金色 [compound], NOT flagged:金 (金 masked)",
        "金色",
        lambda o: fired(o, "color") and "金色" in rc(o, "color")
                  and "flagged" not in (o["color"][2] if "color" in o else "")))
    cases.append(("founding chars 青青河畔草: 青 color + 草 plant fire as before (no compound masks)",
        "青青河畔草",
        lambda o: fired(o, "color") and "青" in rc(o, "color")
                  and fired(o, "plant") and "草" in rc(o, "plant")))
    # -- #58 masking-interaction: a compound consumes its span; a field char
    #    OUTSIDE the span still fires (shared masking machinery is upstream of
    #    the char-harvest for ALL fields — the declared risk channel) --
    cases.append(("masking 青翠松柏: 青翠→color (span masked), 松/柏 OUTSIDE still fire plant",
        "青翠松柏",
        lambda o: fired(o, "color") and "青翠" in rc(o, "color")
                  and fired(o, "plant") and "松" in rc(o, "plant") and "柏" in rc(o, "plant")))
    cases.append(("cross-field-char compound 竹青松: 竹青→color, 竹 consumed (no plant leak), 松 OUTSIDE fires plant",
        "竹青松",
        lambda o: fired(o, "color") and "竹青" in rc(o, "color")
                  and fired(o, "plant") and "松" in rc(o, "plant")
                  and "竹" not in rc(o, "plant")))
    # -- #61 EN-COLOUR YIELD LAW (rulings by An, 07-27/28 night) --
    def fl2(o, f): return o[f][2] if f in o else ""   # the flags element
    # (a) BK11 basics NEVER yield to plant — orange/pink restored, fire CLEAN
    cases.append(("#61(a) BK11 'an orange sky': orange fires colour CLEAN (not flagged; B&K basic never yields)",
        "an orange sky",
        lambda o: fired(o, "color") and "orange" in rc(o, "color")
                  and "orange" not in fl2(o, "color")))
    cases.append(("#61(a) BK11 'the pink dawn': pink fires colour CLEAN (B&K basic; dawn is temporal not xkcd)",
        "the pink flowers",
        lambda o: fired(o, "color") and "pink" in rc(o, "color")
                  and "pink" not in fl2(o, "color")))
    # (b) plant-collision names fire colour WITH a declared-polysemy flag (nuit mirror)
    cases.append(("#61(b) 'a rose bloom': rose fires colour FLAGGED (plant polysemy priced, not hidden); plant co-fires",
        "a rose bloom",
        lambda o: fired(o, "color") and "rose" in rc(o, "color")
                  and "flagged:" in fl2(o, "color") and "rose" in fl2(o, "color")
                  and fired(o, "plant") and "rose" in rc(o, "plant")))
    cases.append(("#61(b) 'olive leaves': olive fires colour FLAGGED (plant polysemy, kaikki-cited)",
        "olive leaves",
        lambda o: fired(o, "color") and "olive" in rc(o, "color")
                  and "olive" in fl2(o, "color")))
    # -- #61 NO-VIBES-FLAG AUDIT (her law: uncited flags removed) --
    # gold REMOVED from EN_COLOR_FLAG (hand-declared, never cited): it now fires
    # CLEAN colour (BK/xkcd basic 'gold'), NOT flagged. Census byte-identical
    # (state stays 'stated'; the census reads fires==True). Regression guard:
    cases.append(("#61-audit 'a gold ring': gold fires colour CLEAN (flag REMOVED, uncited; was flagged:gold)",
        "a gold ring",
        lambda o: fired(o, "color") and "gold" in rc(o, "color")
                  and "gold" not in fl2(o, "color")))
    # fair REMOVED from EN_COLOR_FLAG (#61 v4.9, her ruling "remove fair"): fair is
    # in NO colour lexicon (not xkcd, not BK11) and fired colour ONLY via the
    # hand-declared flag — so post-removal it fires NOTHING for colour. This is the
    # source of the 5 ruled census flips (xu_yuanchong L3 / waley_1918 L9 /
    # scott_1909 L10 / millay L5 / dillon L16). Regression guard:
    cases.append(("#61-audit 'her fair skin': fair fires NO colour (flag REMOVED per her v4.9 ruling; not in any lexicon)",
        "her fair skin",
        lambda o: not (fired(o, "color") and "fair" in rc(o, "color"))))
    # birrell L5 shape: 'rouge' (a clean xkcd colour) co-fires, so removing 'fair'
    # is receipt-only there — the cell STAYS stated, only the 'fair' receipt leaves.
    cases.append(("#61-audit 'rouge and fair' (birrell L5 shape): rouge fires colour CLEAN, fair contributes NOTHING (receipt-only drop, cell stays stated)",
        "rouge and fair",
        lambda o: fired(o, "color") and "rouge" in rc(o, "color")
                  and "fair" not in rc(o, "color")))
    # (d) 'dark' RULED-YIELD to illumination — must NOT fire colour (dillon finding)
    cases.append(("#61(d) 'a dark wood': dark does NOT fire colour (ruled-yield → illumination; the dillon finding)",
        "a dark wood",
        lambda o: not (fired(o, "color") and "dark" in rc(o, "color"))))
    # (c) temporal exclusivity KEPT — 'twilight' yields to temporal, no colour
    cases.append(("#61(c) 'the twilight hour': twilight does NOT fire colour (temporal exclusivity, arm-1 L134)",
        "the twilight hour",
        lambda o: not (fired(o, "color") and "twilight" in rc(o, "color"))))
    # -- #61 Stage 2: EN MORPHOLOGICAL FOLD (rosy→rose; the flagship pseudo-ghost) --
    cases.append(("#61-fold 'rosy cheeks': rosy→rose fires colour FLAGGED (the xu L5 ghost dissolved)",
        "rosy cheeks",
        lambda o: fired(o, "color") and "rose" in rc(o, "color")
                  and "rose" in fl2(o, "color")))
    cases.append(("#61-fold 'roses and violets': plural roses→rose fires (inflection)",
        "roses and violets",
        lambda o: fired(o, "color") and "rose" in rc(o, "color")))
    cases.append(("#61-fold 'darkness fell': darkness NOT folded to colour (dark is ruled-yield; dillon guard)",
        "darkness fell",
        lambda o: not fired(o, "color")))
    # -- #61 TASK 4: EN SOUND FOLD (the 'clacking' specimen — rosy's disease in sound) --
    # clacking→clack (inflect -ing) so the sound boolean fires; the tiaotiao L4
    # en:owen ghost dissolves (ghost→stated). Receipts are LEMMA-keyed.
    cases.append(("#61-sound-fold 'clacking, she whiles': clacking→clack fires sound STATED (owen L4 ghost dissolved)",
        "clacking, she whiles away time with the shuttle.",
        lambda o: fired(o, "sound") and "clack" in rc(o, "sound")))
    cases.append(("#61-sound-fold 'the bells were ringing': ringing→ring fires sound (inflection -ing)",
        "the bells were ringing",
        lambda o: fired(o, "sound") and "ring" in rc(o, "sound")))
    cases.append(("#61-sound-fold 'it hums and buzzes': hums→hum, buzzes→buzz fire sound (inflection)",
        "it hums and buzzes",
        lambda o: fired(o, "sound") and "hum" in rc(o, "sound") and "buzz" in rc(o, "sound")))
    cases.append(("#61-sound-fold 'a reddening sky': reddening NOT folded to sound (no sound base — honest drop)",
        "a reddening sky",
        lambda o: not (fired(o, "sound") and "red" in rc(o, "sound"))))
    # -- #61 NIGHT BUILD: DE COLOUR LEG (lang='de'; the fr blueprint) --------
    # de-seat colour lines are PD (bethge 1907 / heilmann 1905 / forke 1899).
    def firedL(t, lang):
        o = label_unit(t, lang); return "color" in o and o["color"][0]
    def rcL(t, lang):
        o = label_unit(t, lang); return o["color"][1] if "color" in o else ""
    cases.append(("#61-de 'heller grüner Rasen' (bethge/heilmann): grün fires under lang=de (grüner→grün)",
        "heller grüner Rasen",
        lambda o: firedL("heller grüner Rasen", "de") and "grün" in rcL("heller grüner Rasen", "de")))
    cases.append(("#61-de 'Und am weissen Strom' (forke): weiss→weiß fires (ß/ss orthography)",
        "Und am weissen Strom",
        lambda o: firedL("Und am weissen Strom", "de") and "weiß" in rcL("Und am weissen Strom", "de")))
    cases.append(("#61-de GATE 'Sitzt die Weberin fern' (forke): 'fern'(German 'far') does NOT fire de colour (en-xkcd collision gated)",
        "Sitzt die Weberin fern",
        lambda o: not firedL("Sitzt die Weberin fern", "de")))
    cases.append(("#61-de 'In der stillen Nacht' (forke): no de colour (Nacht=temporal not a hue)",
        "In der stillen Nacht",
        lambda o: not firedL("In der stillen Nacht", "de")))
    # -- #61 NIGHT BUILD: EN TEMPORAL (HeidelTime-derived inventory) ---------
    cases.append(("#61-temporal 'in the month of April': month/april fire temporal (HeidelTime month facts)",
        "in the month of April",
        lambda o: fired(o, "temporal") and "april" in rc(o, "temporal")))
    cases.append(("#61-temporal 'a summer evening': summer(season)+evening(part-of-day) fire temporal",
        "a summer evening",
        lambda o: fired(o, "temporal") and "summer" in rc(o, "temporal") and "evening" in rc(o, "temporal")))
    cases.append(("#61-temporal 'many weeks and years': week+year(units) fire temporal",
        "many weeks and years",
        lambda o: fired(o, "temporal") and "week" in rc(o, "temporal") and "year" in rc(o, "temporal")))
    cases.append(("#61-temporal near-miss 'Death's second self': ordinal 'second' does NOT fire temporal (composition-glue dropped)",
        "Death's second self",
        lambda o: not fired(o, "temporal")))
    cases.append(("#61-temporal ruling(c) 'the twilight hour at dusk': twilight/dusk fire temporal, NOT colour (ruled-exclusive preserved)",
        "the twilight hour at dusk",
        lambda o: fired(o, "temporal") and "twilight" in rc(o, "temporal") and "dusk" in rc(o, "temporal")
                  and not fired(o, "color")))
    cases.append(("#61-temporal DROP 'the pink dawn' (declared): pink fires COLOUR (BK basic), dawn does NOT fire temporal (HeidelTime lacks 'dawn' — honest drop)",
        "the pink dawn",
        lambda o: fired(o, "color") and "pink" in rc(o, "color")
                  and not (fired(o, "temporal") and "dawn" in rc(o, "temporal"))))
    print("=== #58 sound + colour · #61 en-colour yield law + en fold · #61 de+temporal — SELFTEST ===")
    ok = 0
    for label, text, pred in cases:
        o = label_unit(text)
        p = bool(pred(o))
        ok += p
        print(f"[{'PASS' if p else 'FAIL'}] {label}")
        print(f"        text={text!r}")
        print(f"        color        = {o.get('color', '—')}")
        print(f"        plant        = {o.get('plant', '—')}")
        print(f"        sound        = {o.get('sound', '—')}")
        print(f"        sound_device = {o.get('sound_device', '—')}")
    print(f"\n{ok}/{len(cases)} probes passed")
    print(f"leg counts: 釋樂={len(_zh_sound_legs()[1])} 音部={len(_zh_sound_legs()[2])} "
          f"廣韻={len(_zh_sound_legs()[3])} | zh_sound(union)={len(zh_sound())} | "
          f"en_sound_word()={len(en_sound_word())}")
    n_compound_colour = sum(1 for v in ZH_COMPOUNDS.values() if v == "color")
    print(f"colour tiers: ZH_COLOR(char)={len(ZH_COLOR)} chars ({''.join(sorted(ZH_COLOR))}) | "
          f"ZH_COMPOUNDS colour tier={n_compound_colour} names | "
          f"ZH_COLOR_FLAG={''.join(sorted(ZH_COLOR_FLAG))} | en_color()={len(en_color())}")
    return 0 if ok == len(cases) else 1

def main():
    if "--calibrate" not in sys.argv:
        return selftest()
    # #58 NOTE: under the word-tier rename, calibrating "sound" against the
    # dev sheets (which carry DEVICE marks) is INVALID until sound is re-
    # marked descriptive-vs-device. Board scoring is convened by Anneliese,
    # not run here; this path is kept behind --calibrate for that rerun.
    _require_calibration_inputs()          # #71: refuse a vacuous all-zero table
    mapping = load_map(CALIBRATION_MAP)
    fields = ["color", "sound", "plant", "temporal"]
    tp = {f: 0 for f in fields}; fp = {f: 0 for f in fields}; fn = {f: 0 for f in fields}
    misses = []; rhyme_stats = [0, 0]  # [structural rhyme units, of which human-tagged]
    for sheet in sorted(glob.glob(str(CALIBRATION_SHEETS / "sheet_*.md"))):
        poem = Path(sheet).stem.replace("sheet_", "")
        if poem in ("albatros", "correspondances", "haiku_basho"):
            continue  # out-of-scope v1.1 (fr/jp), by declaration
        units = sheet_units(sheet)
        truth = human_fields(poem, mapping)
        if not truth:
            continue
        rhymes = poem_rhyme_units(units)
        for u, text in units.items():
            pred = label_unit(text)
            # end-rhyme = SEPARATE structural channel (07-15 finding:
            # detector tracks poem structure; human sound-marks track
            # ATTENTION — different quantities; not merged into the
            # calibrated field, reported apart for the rubric's use)
            if u in rhymes:
                rhyme_stats[0] += 1
                if "sound" in truth.get(u, set()):
                    rhyme_stats[1] += 1
            for f in fields:
                p = f in pred and pred[f][0]
                t = f in truth.get(u, set())
                if p and t: tp[f] += 1
                elif p and not t:
                    fp[f] += 1; misses.append(f"FP {f:8} {poem} {u}: {text[:30]} [{pred[f][1]}]")
                elif t and not p:
                    fn[f] += 1; misses.append(f"FN {f:8} {poem} {u}: {text[:30]}")
    print(f"{'field':10}{'P':>7}{'R':>7}{'F1':>7}   (tp/fp/fn)")
    for f in fields:
        P = tp[f] / (tp[f] + fp[f]) if tp[f] + fp[f] else 0.0
        R = tp[f] / (tp[f] + fn[f]) if tp[f] + fn[f] else 0.0
        F1 = 2 * P * R / (P + R) if P + R else 0.0
        print(f"{f:10}{P:7.2f}{R:7.2f}{F1:7.2f}   ({tp[f]}/{fp[f]}/{fn[f]})")
    print(f"\nstructural end-rhyme channel (中古韻, apart from table): "
          f"{rhyme_stats[0]} units detected, {rhyme_stats[1]} human-tagged "
          f"— the attention-vs-structure gap, measured")
    print(f"\n--- error listing ({len(misses)}) ---")
    for m in misses:
        print(m)

if __name__ == "__main__":
    sys.exit(main())
