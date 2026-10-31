#!/usr/bin/env python3
"""THE LAW, single-sourced (#60, 2026-07-27, her order: rewrite, not patch).

Every function here is the ruling implementation of one law-piece; exhibits,
harnesses, and the census (since v4.2) import from HERE and nowhere else.
Extracted verbatim from the post-amendment gen_sample_exhibits_59 (whose
exhibit half is deprecated). Semantics of record as of 07-28 —
per-word trigger SPLIT BY AXIS KIND (her re-census ruling, 07-28 late night,
#62 — supersedes the prior all-fields two-sided law): SALIENCE axes
{color, plant, sound} are POSITIVE-ONLY (dd >= cut — a negative Δ there is
dilution, not an event), VALUE rulers {illumination dark+, temporal long+}
stay TWO-SIDED (|dd| >= cut — "greatly negative means saliently short/bright",
her original 07-28 duration reasoning, still correct for signed value axes).
The full ruling + its superseded history live on triggered_tokens (house law:
corrections carried on their face). Census of record: findings_v50 (v4.9 and
before were the two-sided era). GHOST PINNED AT THE WORD (her ruling 07-28) —
the line-gate
makes no states; a line over the verse null with no token account is a
LINE-RESIDUAL annotation (line_residual(): zh sides, illumination excluded),
never a state, never a crossing; precedence stated > latent > ghost >
silent; device = parallel organ.
No project-module imports; no encoder; pure functions over committed JSON.

── LOADER FAILURE MODES, declared (they are NOT uniform, and the divergence is
deliberate — each loader fails the way its law-status demands; #71 refactor
documented them, changed none):
  load_board(board)   descriptive + latent: RAW EXCEPTION (FileNotFoundError) —
                      a board without its two committed score files is a broken
                      call, not a state. Its THIRD leg, the unattributed signal
                      file, is caught and degrades to an empty set() SILENTLY
                      (the exploratory tier is optional by construction). One
                      function, two modes, on purpose.
  cuts()              RAW EXCEPTION — the promotion thresholds are the trigger's
                      arithmetic; there is no exhibit without them.
  linecut2()          SILENT {} on FileNotFoundError — the v2 line-cut feeds
                      line_residual(), an ANNOTATION tier; its absence must not
                      stop a run (it just annotates nothing).
  news_norms()        loud SystemExit — the language-relative z IS law
                      (her ruling, twice); no silent fallback.
  line_exam_grades()  loud SystemExit — the z-dot saturation IS the field's
                      battery grade; it may never be defaulted.
  z_line_data()       loud SystemExit — the z-line is an ADOPTED display
                      element (her ruling, 07-28 night).
  alignments()        SILENT {} — an unaligned seat then reads its honest
                      declared 'awaits alignment file' status.
  _fold_map()         SILENT {} if Unihan_Variants.txt is absent (fold becomes
                      identity: the zh simplified/traditional twins stop
                      folding, matching degrades, nothing crashes).
  _variant_map()      SILENT {} per missing artifact (claim-match degrades to
                      exact/zh-fold only).
The rule the pattern encodes: a loader whose datum MAKES OR GATES A STATE fails
loud; a loader feeding a DISPLAY/ANNOTATION tier degrades quiet."""
import glob
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
DESC = HERE / "deterministic-descriptive-fields"
LAT = HERE / "deterministic-latent-written-fields"
UNATTR = HERE / "exploratory-unattributed-signal-fields"
CUTS_J = HERE.parent / "engine" / "results" / "promotion_threshold_59.json"
LC2_J = HERE.parent / "engine" / "results" / "linecut_v2_60.json"
ZLINE_J = HERE.parent / "engine" / "results" / "colour_zline_62.json"
NEWS_NORMS_J = HERE.parent / "engine" / "results" / "news_norms_z_62.json"
NEWS_NORMS_SRC = "news_norms_z_62"     # provenance id carried into the sidecar
LINE_EXAM_J = HERE.parent / "engine" / "results" / "line_scalar_exam_60.json"

HUE = {"color": "#b22222", "sound": "#0f766e", "plant": "#758b23",
       "illumination": "#4338ca", "temporal": "#92400e"}
TOK_HUE = "#d97706"
AMBER, PURPLE, PALE = "#c9a227", "#7c3aed", "#94a3b8"
DEV_BG = "#e0f2fe"
CELL15 = {("active", "active"): "SURVIVAL", ("active", "latent"): "PARTIAL-LOSS",
          ("active", "ghost"): "ECHO", ("active", "absent"): "DEFORMATION",
          ("latent", "active"): "REVIVAL", ("latent", "latent"): "LATENT-CARRY",
          ("latent", "ghost"): "LATENT-ECHO", ("latent", "absent"): "LATENT-UNREALIZED",
          ("ghost", "active"): "RENDERED", ("ghost", "latent"): "GHOST-GROUNDED",
          ("ghost", "ghost"): "GHOST-CARRY", ("ghost", "absent"): "UNHEARD",
          ("absent", "active"): "INVENTION", ("absent", "latent"): "LATENT-INVENTION",
          ("absent", "ghost"): "STIRRED"}

# ── THE EIGHT BOARDS — canonical home since the #71 refactor (2026-08-12). The
# board roster, formerly copy-pasted BYTE-IDENTICALLY in linegrain_census_v43_60
# and interesting_gen_61 (verified cmp-clean before the move). Those two now
# re-export this list under their own module names, so `C.BOARDS` and every other
# existing reference keeps working unchanged. A FOURTH copy lives outside this
# package in engine/census_coverage_ledger_63.py; it is deliberately LEFT ALONE —
# that module declares itself a verbatim analysis-only fork of the v43 loop, and
# forking is its stated method.
BOARDS = ["sonnet18", "qingqing", "tiaotiao", "xibei",
          "albatros", "correspondances", "invitation", "elevation"]

# ── THE STATE-PRIORITY RANK — canonical home since the #71 refactor
# (2026-08-12). The precedence weight for every fold over the seat lines that
# render ONE source line: the census's fold_states, exhibit_gen_60's carrier-line
# pick, and the verify harness's independent mirror all weigh states with this.
# Formerly copy-pasted BYTE-IDENTICALLY in exhibit_gen_60 and
# linegrain_census_v43_60 (verified cmp-clean before the move); both now
# re-export it, so GEN.RANK / C.RANK keep working unchanged. The
# engine/census_coverage_ledger_63 copy is left alone for the same reason as
# BOARDS. It is the ORDERING that carries the meaning, not the absolute numbers:
# stated > present* > latent > ghost > silent > silent*.
RANK = {"stated": 5, "present*": 4.5, "latent": 4, "ghost": 3,
        "silent": 1, "silent*": 0.9}

_CUTS, _LC2, _FOLD, _ALIGN = None, None, None, None


def load_board(board):
    """The board's three committed score legs: (descriptive, latent, unattributed
    membership set). Failure mode is MIXED BY DESIGN (see the module docstring):
    the descriptive and latent files raise RAW (a board without them is a broken
    call), while a missing unattributed_signal file degrades to an empty set()
    silently (the exploratory tier is optional by construction)."""
    d = json.loads((DESC / f"descriptive_scores_{board}_59.json").read_text())
    l = json.loads((LAT / f"latent_scores_{board}_59.json").read_text())
    try:
        u = json.loads((UNATTR / f"unattributed_signal_{board}_59.json").read_text())
        umem = {(r["rid"], r["line_no"], r["field"]) for r in u.get("rows", [])}
    except FileNotFoundError:
        umem = set()
    return d, l, umem


def alignments():
    """The PI-approved alignment files (chair-verified), loaded once, as
    {(board, rid): record}. The exhibits, the census and the miners use them
    identically; 'awaits alignment file' stays reserved for seats that truly have
    none.

    Canonical home since the #71 refactor (2026-08-12). Formerly TWO
    near-duplicates: exhibit_gen_60's (memoized, Path.read_text) and
    linegrain_census_v43_60's (fresh dict per call, json.load(open(p))). They were
    DIFFED before the move — same glob root, same key, same value, therefore the
    same mapping on the present data; the ONLY semantic delta was the memo. The
    memoized form is the one canonicalized, on two checked grounds: it is the
    strictly cheaper one (exhibit calls this per seat inside build_model), and NO
    caller anywhere in the repo mutates the result — every call site only ever
    does `.get((board, rid))`, so a shared cached dict is indistinguishable from a
    fresh one. Consumers re-export the name, so `C.alignments()` keeps working.

    Failure mode: SILENT {} — an absent or empty corpus/alignments/ directory
    globs to nothing, and an unaligned seat then reads its honest declared
    'awaits alignment file' status rather than crashing a render."""
    global _ALIGN
    if _ALIGN is None:
        _ALIGN = {}
        for p in glob.glob(str(HERE.parent / "corpus" / "alignments" / "*.json")):
            d = json.loads(Path(p).read_text())
            _ALIGN[(d["board"], d["rid"])] = d
    return _ALIGN


def cuts():
    """The per-field promotion thresholds as
    {field: (cut, tier_label, line_cut_or_None)}, loaded once. Failure mode: RAW
    EXCEPTION (no guard, by design) — these cuts ARE the trigger's arithmetic, so
    a missing promotion_threshold_59.json is a broken call, never a fallback."""
    global _CUTS
    if _CUTS is None:
        d = json.loads(CUTS_J.read_text())
        _CUTS = {}
        for f, ff in d["fields"].items():
            adopted = ff.get("adopted_threshold")
            _CUTS[f] = (float(adopted) if adopted is not None
                        else float(ff["quantile_cut"]["0.95"]),
                        "ADOPTED · flagship" if adopted is not None else "SUGGESTED",
                        float(ff["line_cut"]) if ff.get("line_cut") is not None else None)
    return _CUTS


def linecut2():
    """The v2 per-field line-cut as {field: line_cut_v2}, loaded once. Failure
    mode: SILENT {} on a missing file — deliberately UNLIKE news_norms()'s loud
    SystemExit, because this datum feeds line_residual() alone, which is an
    ANNOTATION tier (never a state): absent, it annotates nothing and the run is
    still correct. news_norms() shares this load idiom and differs precisely in
    the loud-fail, because the z IS law."""
    global _LC2
    if _LC2 is None:
        try:
            _LC2 = {f: v["line_cut_v2"]
                    for f, v in json.loads(LC2_J.read_text())["fields"].items()}
        except FileNotFoundError:
            _LC2 = {}
    return _LC2


# ── NEWS-NORMED LINE-SCALAR z (her ruling, twice; #62 build, norms 9bc5709),
# LOADED AS DATA (the no-project-import law — precedent: cuts()/linecut2()).
# z(line) = (reading − μ(ℓ,f)) / σ(ℓ,f) over ≈10k Leipzig NEWS sentences per
# (language, field). DISPLAY/ANNOTATION TIER ONLY — makes NO states (her pin;
# two-norms doctrine: the CUT's verse null is untouched, this is the CURRENCY
# norm on the register uniform across the five languages). The z is now LAW:
# a MISSING norms file is a loud SystemExit, never a silent fallback.
_NN = None


def news_norms():
    """The per-(field, language) news μ/σ, loaded once as data. Returns
    {field: {lang: (mu, sigma)}}. Missing file = SystemExit (the z is law; no
    silent fallback — her ruling that the line-scalar IS a language-relative
    value). Mirrors linecut2()'s load idiom; the loud-fail is the difference."""
    global _NN
    if _NN is None:
        if not NEWS_NORMS_J.exists():
            raise SystemExit(
                f"news norms MISSING: {NEWS_NORMS_J} not found. The "
                f"language-relative z is law (her ruling, twice); the display "
                f"tier cannot render without it. Produce news_norms_z_62.json "
                f"(commit 9bc5709) before generating exhibits.")
        d = json.loads(NEWS_NORMS_J.read_text(encoding="utf-8"))
        _NN = {}
        for f, langs in (d.get("fields") or {}).items():
            _NN[f] = {lang: (float(c["mu"]), float(c["sigma"]))
                      for lang, c in langs.items()}
    return _NN


def z_of(lang, field, v):
    """News-normed relative z for a committed line-scalar reading v in
    (language, field). Returns None if v is None or the language has no news
    norm (jp; any lang outside {en,zh,de,fr}) — the seat then draws the empty
    'untested (no news norm)' z strip (her jp ruling). No state consequence."""
    if v is None:
        return None
    cell = news_norms().get(field, {}).get(lang)
    if cell is None:
        return None
    mu, sigma = cell
    return (float(v) - mu) / sigma


# ── z-STRIP DISPLAY LAW (her rulings, 07-28 evening, #62): the z strip's scale
# is FIXED symmetric ±3 z-units (clamp beyond); the dot's SATURATION follows
# the field's battery grade (the muted dot's true reason, finally displayed as
# itself). Grade → fill-opacity mapping, per the registration's PROPOSED table
# now WIRED at her word:
#   DISCRIMINATION at line grain            → 0.95   (credentialed colour)
#   WEAK — exploratory                      → 0.55
#   NO demonstrated discrimination          → 0.22   (ghost)
#   temporal (NOT in the line-grain AUC exam; credentialed via Spearman ρ .860
#     [.843–.875], RULERS A7 — a DISTINCT metric, DECLARED) → 0.85
# The grades load AS DATA from line_scalar_exam_60.json (the four AUC fields);
# temporal is the declared exception (it faces a different credential, so it
# carries no exam row and takes its own saturation by declaration).
Z_CLAMP = 3.0                       # the z strip scale: symmetric ±3σ, clamp
GRADE_SATURATION = {
    "DISCRIMINATION at line grain": 0.95,
    "WEAK — exploratory": 0.55,
    "NO demonstrated discrimination": 0.22,
}
TEMPORAL_SATURATION = 0.85          # ρ .860 duration credential (A7), declared
# ── CHANCE-LIKE Z SUPPRESSED FROM THE DIAGRAM (her ruling, 07-28 night, #62).
# A field whose LINE-TIER grade is "NO demonstrated discrimination" (measured,
# found nothing at line grain) DOES NOT RENDER a z strip at all — no dot, no
# label, no baseline, no tick. Her words: "I think we remove them from graph,
# but left sentences in the paper if we mention" — a globally chance-like z
# "does not mean anything", so it belongs in prose, not the diagram. (Sequence
# of record: the chair first picked GREY within her delegation; she superseded
# it the same sitting — removal from diagrams, honesty carried by the paper's
# instruments prose. Hers governs.) In place of the strip the panel carries ONE
# suppression sentence (Z_SUPPRESS_NOTE). temporal is NOT suppressed: its
# credential is Spearman ρ .860 (a value ruler, a DISTINCT metric); fired-line
# separation was never its claim, so it keeps its field-hued z at 0.85
# (declared exception, above). NOTE the jp/unnormed untested-bar is a DIFFERENT
# absence (no news norm ≠ no discrimination) and is UNCHANGED by this ruling.
GRADE_NONE = "NO demonstrated discrimination"
Z_SUPPRESS_NOTE = ("line-scalar suppressed: no line-tier discrimination at "
                   "grade (exam .427) — see instruments prose")
_EXAM = None


def line_exam_grades():
    """Per-field battery grade string, loaded once as data from
    line_scalar_exam_60.json (the four line-grain AUC fields: color, plant,
    sound, illumination). Missing file = SystemExit (the saturation is now the
    dot's declared meaning; no silent default). temporal is NOT here — it is
    credentialed by a distinct metric (ρ .860) and takes TEMPORAL_SATURATION."""
    global _EXAM
    if _EXAM is None:
        if not LINE_EXAM_J.exists():
            raise SystemExit(
                f"line-scalar exam grades MISSING: {LINE_EXAM_J} not found. "
                f"The z-dot saturation IS the field's battery grade (her "
                f"ruling); it cannot render without the grades.")
        d = json.loads(LINE_EXAM_J.read_text(encoding="utf-8"))
        _EXAM = {f: v.get("grade") for f, v in (d.get("fields") or {}).items()}
    return _EXAM


def z_saturation(field):
    """The z-dot fill-opacity for a field = its battery grade mapped to
    saturation. temporal → TEMPORAL_SATURATION (declared distinct credential);
    the four AUC fields → GRADE_SATURATION[grade]. An unknown grade string is a
    loud SystemExit (a new grade must be mapped deliberately, never defaulted)."""
    if field == "temporal":
        return TEMPORAL_SATURATION
    grade = line_exam_grades().get(field)
    if grade not in GRADE_SATURATION:
        raise SystemExit(
            f"z-dot saturation: field {field!r} grade {grade!r} has no "
            f"saturation mapping (GRADE_SATURATION). Map it deliberately.")
    return GRADE_SATURATION[grade]


def z_suppressed(field):
    """CHANCE-LIKE-Z-SUPPRESSED predicate (her ruling, 07-28 night, #62): True
    iff the field's LINE-TIER exam grade is GRADE_NONE ("NO demonstrated
    discrimination") — its z separated nothing at line grain, so the whole z
    strip is REMOVED FROM THE DIAGRAM (no dot/label/baseline/tick); the panel
    carries the Z_SUPPRESS_NOTE sentence instead (honesty in prose, not the
    graph). temporal is NEVER suppressed here: it is credentialed by a distinct
    metric (ρ .860) and carries no line-grain AUC exam row, so fired-line
    separation was never its claim (declared exception). Currently True for
    illumination alone. (The jp/unnormed untested-bar is unrelated — a different
    absence: no news norm, not no discrimination.)"""
    if field == "temporal":
        return False
    return line_exam_grades().get(field) == GRADE_NONE


# ── THE COLOUR z-LINE (her ruling, 07-28 night, #62: "now we can draw a little
# line on the line-scalar z for color" → "we are going to adopt it"). A single
# vertical z-threshold on the z strip = the p95 of the UNFIRED colour z over
# covered census cells (pooled across en/zh/de/fr, POSITIVE side — the promotion-
# threshold quantile idiom, the same 0.95 the cuts use). LOADED AS DATA
# (colour_zline_62.json; the no-project-import law, precedent cuts()/linecut2()/
# news_norms()). DISPLAY/ANNOTATION TIER — makes NO states (her standing pin;
# boolean layer, LAW-INDEPENDENT: unaffected by the salience trigger flip).
# CREDENTIAL GATE: drawn ONLY on fields graded "DISCRIMINATION at line grain" in
# the census z line-exam (today colour alone; auto-extends on future
# graduation). ADOPTED tier (her word; chair non-objecting) — the strip label
# reads "z-cut ·ADOPTED". Licensed reading, verbatim: a dot RIGHT of the line
# reads "relatively colourful against the census unfired baseline (above 95% of
# boolean-unfired lines)", NEVER "proof" of colour. Convention caveat (her
# words): "which is a p95, not wonderfully great" — a quantile convention, not an
# optimized/validated boundary. Missing file = SystemExit (the loud-fail law,
# mirroring news_norms()/line_exam_grades(): the element is registered law).
GRADE_DISCRIM = "DISCRIMINATION at line grain"
ZLINE_TIER = "ADOPTED"                 # her adoption word, 07-28 night, #62
_ZLINE = None


def z_line_data():
    """The colour z-line as data (once). Returns {field: {"z_line": float,
    "quantile": float, ...}} for every field carrying a registered line. Missing
    file = SystemExit (the z-line is an adopted display element; no silent
    fallback — mirrors news_norms()/line_exam_grades())."""
    global _ZLINE
    if _ZLINE is None:
        if not ZLINE_J.exists():
            raise SystemExit(
                f"colour z-line MISSING: {ZLINE_J} not found. The z-line is an "
                f"ADOPTED display element (her ruling, 07-28 night); the z strip "
                f"cannot draw it without the registered value. Produce "
                f"colour_zline_62.json before generating exhibits.")
        d = json.loads(ZLINE_J.read_text(encoding="utf-8"))
        _ZLINE = {f: v for f, v in (d.get("fields") or {}).items()}
    return _ZLINE


def z_line(field):
    """The registered z-line value for a field, or None if the field carries no
    line. Guarded by the CREDENTIAL GATE: a line is returned ONLY when the field
    is graded DISCRIMINATION at line grain in the census exam AND a value is
    registered for it (both hold today for colour alone). This double gate means
    the line auto-appears on any field that graduates to DISCRIMINATION and gets
    a registered value, and never on a field that has not — no per-field special-
    casing in the drawing code."""
    if field == "temporal":                 # value ruler; no line-grain grade
        return None
    if line_exam_grades().get(field) != GRADE_DISCRIM:
        return None                          # not credentialed → no line
    cell = z_line_data().get(field)
    if cell is None or cell.get("z_line") is None:
        return None
    return float(cell["z_line"])


def _contentful(ts):
    return any(("一" <= c <= "鿿") or c.isalpha() for c in ts)


def _clean(t):
    return str(t).strip(",.;:!?，。；：？！()（）「」『』“”'’ ")


def _word0(w):
    return re.split(r"[\[\(（【]", str(w))[0].strip()


def _fold_map():
    global _FOLD
    if _FOLD is None:
        _FOLD = {}
        p = HERE.parent / "marking" / "tools" / "vectors" / "Unihan_Variants.txt"
        if p.exists():
            for ln in p.read_text(encoding="utf-8", errors="ignore").splitlines():
                if "kSimplifiedVariant" in ln and ln.startswith("U+"):
                    parts = ln.split("\t")
                    if len(parts) >= 3:
                        try:
                            _FOLD[chr(int(parts[0][2:], 16))] = \
                                chr(int(parts[2].split()[0][2:], 16))
                        except ValueError:
                            pass
    return _FOLD


def fold(s):
    m = _fold_map()
    return "".join(m.get(c, c) for c in str(s))


# ── shared variant→lemma fold (#61 Stage 2c), LOADED AS DATA (precedent:
# _fold_map loads Unihan_Variants.txt) — NO project-module import. The committed
# en_color_variants_61.json carries BOTH the en fold (rosy→rose, built from
# WordNet-'+' ∪ Wiktextract) AND the fr fold (re-emitted from fr_labelers'
# _var2lemma, incl. the rousse→roux irregular). Replaces the old substring-
# containment claim-match that silently failed fr irregulars (rousse vs roux)
# and en derivations (rosy vs rose).
_VMAP = None


def _variant_map():
    global _VMAP
    if _VMAP is None:
        _VMAP = {}
        # committed artifact home: lexical_resources/color_lexicon/ (vectors/ is
        # gitignored, unlike the Unihan_Variants precedent). HERE = publishable;
        # repo root = HERE.parent.
        p = (HERE.parent / "lexical_resources" / "color_lexicon"
             / "en_color_variants_61.json")
        if p.exists():
            d = json.loads(p.read_text(encoding="utf-8"))
            for lang in ("en", "fr"):
                for var, rec in (d.get(lang) or {}).items():
                    # last write wins is fine — en/fr keyspaces are disjoint in
                    # practice; a variant resolves to its lemma either way
                    _VMAP[var.lower()] = rec["lemma"].lower()
        # #61 Task 4 — the EN SOUND FOLD joins the shared claim-match map, so a
        # sound top-tok 'clacking' claim-matches the receipt 'clack' in exhibits/
        # verify (the same field-agnostic variant→lemma role). Colour keys win on
        # the rare overlap (loaded first); sound adds the verbal-inflection keys.
        ps = (HERE.parent / "lexical_resources" / "audio_witness"
              / "en_sound_variants_61.json")
        if ps.exists():
            ds = json.loads(ps.read_text(encoding="utf-8"))
            for var, rec in (ds.get("en_sound") or {}).items():
                _VMAP.setdefault(var.lower(), rec["lemma"].lower())
    return _VMAP


def _lemma_of(tok):
    """Clean → lower → variant-map lemma (identity if unmapped)."""
    w = _word0(tok).strip().lower()
    return _variant_map().get(w, w)


def variant_match(a, b):
    """Claim-match (#61 Stage 2c): a top-tok and a receipt name the SAME word iff
    — exact (cleaned/lower) equal, OR zh char-fold equal (simplified/traditional
    twins, the 嘆/叹 fold), OR they resolve to the SAME lemma in the shared
    variant map (rosy≡rose, rousse≡roux, golden≡gold). Deterministic; no
    substring containment (which mis-joined un-related tokens and missed
    consonant-mutation irregulars)."""
    if not a or not b:
        return False
    wa, wb = _word0(a).strip().lower(), _word0(b).strip().lower()
    if not wa or not wb:
        return False
    if wa == wb:
        return True
    if fold(wa) == fold(wb):            # zh simplified/traditional fold
        return True
    return _lemma_of(wa) == _lemma_of(wb)   # shared variant-map lemma hit


def find_span(txt, word):
    if word and word in txt:
        return word
    fw, ft = fold(word), fold(txt)
    i = ft.find(fw)
    if fw and i >= 0:
        return txt[i:i + len(word)]
    return None


# SALIENCE trigger fields (color/plant/sound) — POSITIVE-ONLY since v5.0
# (her re-census ruling). VALUE rulers (illumination, temporal) and any future
# field stay TWO-SIDED. Named here so the split is one readable fact.
SALIENCE_TRIGGER_FIELDS = frozenset({"color", "plant", "sound"})

# FULL-STACK LANGUAGES — the languages whose word + written + referent channels
# ALL run (the referent miners are Chinese-side only; en/de/fr referent legs are
# partial/absent). SINGLE SOURCE for the exhibit full-stack BADGE (▪ before the
# seat rid, exhibit_gen_60) AND any future full-stack gate — one readable fact,
# never a second copy. Tonight's honest form is LITERAL-WITH-COMMENT: {"zh"} is
# the only language with all three channels wired this era. The FUTURE form is
# DERIVED-FROM-COVERAGE (a language is full-stack iff each channel's coverage
# artifact reports it live) — deferred to a calmer sitting when the coverage
# ledger is a single queryable fact; until then the literal set, declared, is the
# honest statement of what is built. (Her REVERSAL ruling, 07-28 late night, #62,
# verbatim: "I think we should reverse the star situation. We should somehow
# indicate that 'zh is terrific and we have the full support here!' while other
# ones we write in prose about 'ok this is not built and from what we see in zh
# it is really really thin.'") The badge is the POSITIVE mark this set feeds; the
# non-zh referent thinness is carried in PROSE (scope-sentence law), never stars.
FULL_STACK_LANGS = frozenset({"zh"})


def triggered_tokens(row, field, cut):
    """The per-word trigger. TWO KINDS OF AXIS, TWO PREDICATES:

    SALIENCE axes {color, plant, sound} — POSITIVE-ONLY: dd >= cut.
    VALUE rulers {illumination (dark+), temporal (duration long+)} + any other
    field — TWO-SIDED: |dd| >= cut.

    ── HISTORY, carried on its face (house law: corrections superseded, never
    erased). The ORIGINAL two-sided ruling (her ruling, 07-28 night, verbatim):
        "if something is greatly negative that means the temporal-duration is
        saliently short. the same disease plagues the other axis. you are not
        tracking the saliently negative as triggered though they are."
    That reasoning was |Δ| >= cut for EVERY field — coherent with the cut's own
    derivation (|Δ| quantiles of controls). It is CORRECT for the value rulers
    (a large negative excursion on a signed value axis IS a salient reading of
    the opposite pole — "saliently short"). Its analogical extension to the
    SALIENCE axes ("the same disease plagues the other axis") is SUPERSEDED
    below. Census of record under the old two-sided law: findings_v42 … v4.9.

    ── THE RULING OF RECORD (her re-census ruling, 2026-07-28 late night, #62,
    verbatim: "about the incorrect negative triggers: 're-census' please").
    The SALIENCE axes read DOMAIN ENGAGEMENT, not polarity: a NEGATIVE Δ on a
    salience axis is DILUTION (the masked token was making the line MORE
    domain-remote), NEVER a salience event — there is no "saliently anti-sound"
    the way there is a "saliently short". Evidence: the silence probe
    (engine/results/silence_probe_diag_62.txt) — silence/hush/quiet
    wording projects POSITIVE (+0.57 mean z) on the sound axis, reading through
    the word to its non-acoustic sense; and the negative side was minting ghosts
    out of dilution ("Nein"/"und" minting colour ghosts; "kurz" triggering
    colour — the ~750 state-bearing cells on negative-only triggers the chair
    exposure count found). So for the three salience fields the trigger is now
    dd >= cut. The value rulers keep both sides (her original duration reasoning,
    still correct for them). Registration:
    engine/registrations/trigger_law_salience_positive_registration_0728_62.md;
    census of record under this law: findings_v50."""
    out = []
    if cut is None:
        return out
    positive_only = field in SALIENCE_TRIGGER_FIELDS
    for t, dd in (row.get("top_delta", {}).get(field) or []):
        ts = _clean(t)
        if dd is None or not ts or not _contentful(ts):
            continue
        fired = (dd >= cut) if positive_only else (abs(dd) >= cut)
        if fired:
            out.append((ts, dd))
    return out


def top_mover(row, field):
    """TRUE |delta|-max contentful token, sign kept (her sonnet18-L6 catch)."""
    for t, dd in (row.get("top_delta", {}).get(field) or []):
        ts = _clean(t)
        if dd is not None and ts and _contentful(ts):
            return ts, dd
    return None, None


def token_delta_of(word, row, field):
    """The biggest token-delta among the row's top_delta entries matching `word`.

    MODERNIZED at her ruling 08-12 (#71): "you need to modernize it because it
    is a bug, though not affecting result now." History, kept as receipt: this
    function carried substring containment (`fw in ts or ts in fw`) — the very
    pattern variant_match()'s docstring records as RETIRED for claim-matching
    (#61 Stage 2c: containment mis-joined unrelated tokens, rousse/roux,
    rosy/rose) — and was case-sensitive besides (fold() is the zh char-fold,
    not a case-normalizer). It survived because it makes no state: its four
    call sites (mass_rank's sort key, the verify harness mirror, two pinned
    `want()` assertions in albatros_L15_exemplar_gen_63) cost an ordering or a
    pinned number, never a crossing. Matching now routes through
    variant_match(): exact-or-fold-or-shared-lemma, case-normalized, no
    containment."""
    best = None
    for t, dd in (row.get("top_delta", {}).get(field) or []):
        if dd is not None and variant_match(word, _clean(t)):
            if best is None or dd > best:
                best = dd
    return best


def mass_rank(words, row, field):
    """Her walk applied to ink: the word carrying the biggest token-delta
    leads; attribution never migrates in display."""
    return sorted(words, key=lambda w: -(
        token_delta_of(_word0(w), row, field) or -1.0))


def chan_word(field, boolrow):
    b = (boolrow or {}).get(field, {})
    if b.get("fires") is True:
        return b.get("receipts") or ["✓"], "stated"
    if b.get("fires") is False:
        return [], "silent"
    return [], None


def chan_device(boolrow):
    dv = (boolrow or {}).get("sound_device", {})
    if dv.get("fires") is True:
        return dv.get("receipts") or ["✓"], True
    if dv.get("fires") is False:
        return [], False
    return None, False       # None receipts = uncovered


def chan_written(field, writrow):
    w = (writrow or {}).get(field, {})
    if w.get("fires_three_check"):
        cars = [c.get("char", "?") if isinstance(c, dict) else str(c)
                for c in (w.get("carriers") or [])] or ["✓"]
        words = [fr.get("word") for fr in (w.get("fires") or [])
                 if isinstance(fr, dict) and fr.get("word")]
        return cars, True, words
    if w.get("available"):
        return [], False, []
    return None, False, []   # None carriers = n/a


def chan_referent(field, lat, rid, idx):
    # A rid ABSENT from the artifact means the referent leg NEVER RAN for that
    # seat (the miners are zh-substrate — CCFD/HowNet/leipzig_zh; en/de/fr legs
    # cannot run by construction). That is UNCOVERED (None), not tested-empty:
    # `or []` used to collapse the two, so en/de referent cells wore
    # tested-silence "—" — the misread the untested-cell law (07-28, #61)
    # forbids, its own example being "de referent". A rid PRESENT with an
    # empty line keeps meaning ran-and-nothing (tested-empty). Chair-proposed
    # #66, 07-31, awaiting her ruling; fig3/scope-sentence doctrine unchanged.
    if field == "color":
        jb = (lat.get("referent_per_line_colour") or {}).get("board_data") or {}
        rows = (jb.get("renderings") or {}).get(rid)
        if rows is None:
            return None, False, []   # leg never ran for this seat → uncovered
        hits = {r["word"]: r for r in rows if r.get("line") == idx + 1}
        if hits:
            disp = [(f"{w} z{r['z']:+.1f}" if r.get("z") is not None
                     else f"{w} ({r.get('status') or 'sit-out'})") +
                    ("✓" if r.get("call") else "") for w, r in hits.items()]
            return disp, bool([w for w, r in hits.items() if r.get("call")]), \
                [w for w, r in hits.items() if r.get("call")]
        return [], False, []
    if field == "sound":
        sj = (lat.get("sound_referent_per_line") or {}).get("renderings") or {}
        rows = sj.get(rid)
        if rows is None:
            return None, False, []   # leg never ran for this seat → uncovered
        hits = {h["word"]: h for h in (rows[idx] if idx < len(rows) else [])}
        if hits:
            disp = [(f"{w} z{h['z']:+.1f}" if h.get("z") is not None
                     else f"{w} (?)") + ("✓" if h.get("call") else "")
                    for w, h in hits.items()]
            return disp, bool([w for w, h in hits.items() if h.get("call")]), \
                [w for w, h in hits.items() if h.get("call")]
        return [], False, []
    return None, False, []   # None = n/a for this field


def line_state(field, boolrow, writrow, lat, rid, idx, cut, row, line_cut=None):
    """Per-word law; GHOST PINNED AT THE WORD (her ruling 07-28).

    line_cut is a DEAD parameter (line-ghost era): accepted for
    caller-signature stability (census v4.3+, exhibit_gen, verify harness all
    pass it), never read. The line-scalar's one epistemic lane is
    line_residual() — annotation, never a state. Removing the limb is a
    4-file signature change (all sha-pinned); deferred to a calmer sitting.
    Docstring refreshed #61 at her word, 07-27 night; code unchanged.

    ── THE fr TOKEN-GHOST STAR: RETIRED (history on its face — house law:
    corrections superseded, never erased). ORIGINAL (her convening, 2026-07-28):
    a fr token-ghost, being a PARTIAL investigation (fr written/referent
    uncovered), was STARRED SUGGESTIVE — the fourth return True when
    rid.startswith("fr:") — splitting ~247 crossing-rows (33 distinct
    fr:baudelaire colour source token-ghosts × their seats) into the suggestive
    tier. SUPERSEDED SAME NIGHT by her REVERSAL RULING (2026-07-28 late night,
    #62, verbatim): "I think we should reverse the star situation. We should
    somehow indicate that 'zh is terrific and we have the full support here!'
    while other ones we write in prose about 'ok this is not built and from what
    we see in zh it is really really thin.'" So the DEFICIENCY star retires: the
    full-support side is marked POSITIVELY (the zh full-stack BADGE, driven by
    FULL_STACK_LANGS, in exhibit_gen_60), non-zh thinness lives in PROSE (the
    scope-sentence) and never in stars, and the fr branch returns FALSE-FOR-ALL.
    Measured bound (chair count 07-28): the zh referent leg alters 2 of 669
    word-tier-silent verdicts (colour 0/352, sound 2/317 — 0.30%) — real but
    thin. Census of record under the star: v5.0 (findings_v50); under the
    retired star: v5.1 (findings_v51). The present*/silent* stars (uncovered
    WORD channel — a DEEPER deficiency) are UNTOUCHED and STAY STARRED; this
    reversal retired ONLY the fr partial-investigation star."""
    _r, wstate = chan_word(field, boolrow)
    if wstate == "stated":
        return "stated", "word", False
    _c, wfired, _w = chan_written(field, writrow)
    if wfired:
        return "latent", "written", False
    _d, rcall, _cw = chan_referent(field, lat, rid, idx)
    if rcall:
        return "latent", "referent", False
    if wstate == "silent":
        if triggered_tokens(row, field, cut):
            # fr TOKEN-GHOST STAR RETIRED (her REVERSAL ruling, 07-28 late night,
            # #62 — full history + her verbatim words in this function's
            # docstring). No fourth-return star here; was: rid.startswith("fr:").
            # The present*/silent* uncovered-WORD-channel stars below are a
            # DEEPER deficiency and are UNTOUCHED.
            return "ghost", "meter (token)", False
        # GHOST PINNED AT THE WORD (her ruling 07-28): the line-gate no longer
        # makes states — a line over the verse null with no token account is a
        # LINE-RESIDUAL annotation (see line_residual()), never a crossing.
        return "silent", None, False
    if triggered_tokens(row, field, cut):
        return "present*", "scalar", True
    return "silent*", None, True


def line_residual(field, rid, row, cut):
    """Exploratory LINE-RESIDUAL annotation (her 07-28 ruling): the line reads
    ≥ the verse null yet no token accounts for it. Annotation only — never a
    state, never a crossing. zh sides; illumination excluded (exam: no
    discrimination); colour alone carries a line-tier credential (.855)."""
    if not rid.startswith("zh:") or field == "illumination":
        return None
    lc2 = linecut2().get(field)
    if lc2 is None:
        return None
    v = float(row["reading"].get(field) or 0.0)
    if v >= lc2 and not triggered_tokens(row, field, cut):
        return round(v, 4)
    return None


def to3(state):
    return {"stated": "active", "present*": "active", "latent": "latent",
            "ghost": "ghost", "silent": "absent", "silent*": "absent"}[state]


def pick_highlight(txt, field, receipts, carrier_words, call_words, trigs, row):
    """TOP-TOK FIRST (her ruling, 07-28 night: "在line上高光的基本都不是
    top-tok，这个有那么难吗？" — the exhibit displays the top-tok's
    investigation, so the line highlight IS the top-tok, always).
    The highlight = the |Δ|-max contentful token; its COLOUR = which channel
    claims that very token: field hue if it is a boolean receipt · amber if a
    written carrier · purple if a referent call-word · orange if triggered but
    unclaimed (token-ghost) · pale ° if untriggered (mechanical view). Channel
    fires on OTHER words stay in the cascade cells — they never steal the
    line's light (#59's channel-first rule retired at her word)."""
    tm, tmd = top_mover(row, field)
    if not tm:
        return None, None, False
    span = find_span(txt, tm)
    if not span:
        return None, None, False
    # Colour ruling (her word, 07-28: "keep highlight the color of top-tok")
    # — the highlight IS the top-tok, so it wears the top-tok colour, always;
    # channel claims live in the investigation cells, never in the highlight.
    # Pale when untriggered (° law).
    triggered = any(fold(ts) == fold(tm) for ts, _ in trigs)
    return span, TOK_HUE, not triggered
