#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
§8 DEMONSTRATION SCORING — the DETERMINISTIC DESCRIPTIVE FIELDS row.
Translation-studies instrument. Convened by the field owner
07-22 ("since these rows are pretty stable themselves, I think we can
start scoring"). BUILD + SMOKE + DRY here; the real scoring run
(--run) is fired by the orchestrator AFTER her review.

═══ THE LAW (reports/methodology_statement_0716.md, KEEP) ═══
  • THE SCALAR IS THE PAPER — graded trait-intensity scoring (§1, §7).
  • INSTRUMENTS ONLY. NO LLM MARKS ANYTHING — rulers/labelers produce
    every field state, source-side and translation-side alike (§5, §8).
    Nothing in this file asks a generative model for a judgment.
  • The 8-cell transition comparator is FIXED + tested:
    marking/tools/rubric_compare.py (RULERS.md l.12; spec prose in
    design/r2_scalar_shift_spec_52.md "Anchor"). We call it; we do not
    reimplement it.
  • Encoder = LaBSE; PCA-whitening (generic sample) then unit-norm;
    axis = mean(pole+)-mean(pole-) unit norm; score = projection; word
    contribution = score(line) - score(line with word deleted)
    (RULERS.md "Shared mechanics"). Each axis npz carries its OWN
    mu + W + axis key — verified. Same form as smoke_score_sheets_50.py
    (the reference; her sanity-check 07-18 "look sane and can be used").

═══ SCOPE: five credentialed DESCRIPTIVE fields, boolean + scalar ═══
  field         boolean state (which words fire, receipts)         scalar reading (line-grain, R1 credential)
  color         trait_labelers.label_unit["color"]  (en+zh)        color_salience_axis_48.npz["axis"]      AUC .879 [.830-.926]  (RULERS A3)
  illumination  illumination_labeler_53.label       (zh)           illum_polarity_axis_v3_48.npz["dark"]        .825 [.740-.906]  (RULERS A1, physical VALUE dark+)
  sound         trait_labelers.label_unit["sound"]  (en+zh)        sound_salience_axis_v3_49.npz["axis"]        .815 [.786-.843]  (RULERS A5, realized)
  plant         trait_labelers.label_unit["plant"]  (en+zh)        plant_salience_axis_48.npz["axis"]           .801 [.756-.841]  (RULERS A4)
  temporal      trait_labelers.label_unit["temporal"] (en+zh)      duration_value_axis_48.npz["axis"]      rho .860 [.843-.875]  (RULERS A7, VALUE long+)
  NOTE temporal scalar = the DURATION ruler (A7); temporal-SALIENCE
  (A9) is a documented negative and is NOT used (RULERS A9; task spec).

═══ FLAGGED OPEN DETAILS (minimal readings; see README §"Open details") ═══
  F1 GRAIN. rubric_compare.py is tested at POEM level; its own boundary:
     "Line-level comparison awaits an alignment file — never guessed."
     R2 (b) requires a CHAIR-DRAFTED s<i>->t<j> alignment file (unfrozen,
     absent on disk for sonnet 73). MINIMAL READING: default to the
     law-stated fallback (poem grain); line-pair mode runs only if an
     alignment file is supplied (--align), flagged unfrozen.
  F2 BOOLEAN LANGUAGE COVERAGE. The boolean shelf is EN + ZH only
     (illumination is ZH-only: its runtime lexicon is HowNet W_C =
     Chinese words). German has no boolean lexicon; Japanese-in-kanji
     hits the ZH lexicons only INCIDENTALLY via shared Han characters —
     which is NOT a validated JP labeler. MINIMAL READING: a field's
     boolean STATE is emitted only for covered languages; for de/jp
     targets the state is UNAVAILABLE (never fabricated, never "absent").
     Consequence: the transition table classifies only pairs where BOTH
     sides are boolean-covered.
     AMENDED — accuracy pass #71, read off boolean_states() below: COLOUR
     alone is now boolean-covered for fr (07-28 convening) and de (#61 night
     build) too, via the citation-tier B&K12∪GLAWI / B&K12-de∪kaikki
     inventories. "EN + ZH only" still holds for the other four fields.
     Two consequences the prose above predates:
       · coverage is per-FIELD, not per-language: transition_table() keeps
         any field whose state is not None on BOTH sides, so an fr/de target
         IS classified — on colour alone — rather than returning NO_COVERAGE.
       · BOOL_COVERED_LANGS is still {en, zh} and --dry's "runnable
         transition pairs" line counts with it, so that DRY line UNDERCOUNTS
         what a --run would actually classify for fr/de seats. Recorded, not
         changed here (the --run path is not exercisable in this tree).
  F3 SCALAR CROSS-SIDE. §3: raw cross-side scalar deltas are NEVER
     compared (measured 5.6x compression); comparison is
     ensemble-relative (rank). Per-field equating (R2 (c)) is UNFROZEN
     and awaits her convening. MINIMAL READING: emit per-side line
     scalar + per-side ensemble RANK; emit the raw delta flagged
     NON-TRANSFERABLE; apply no equating.
  F4 LATENT FOLD. This is the DESCRIPTIVE row only. No latent files are
     supplied, so rubric_compare.py runs FOLD-DECLARED (active/absent
     states; reachable cells SURVIVAL / DEFORMATION / INVENTION). The
     latent tier is the sibling folder deterministic-latent-written-fields/.
  F5 MASKING GRAIN (per-word Delta receipt only). R1 credentials are
     token-true. The primary scalar (the LINE projection) is
     masking-independent. The secondary per-word Delta receipt uses
     jieba word-units for zh, whitespace for latin, per-char for jp
     (no jp tokenizer in venv) — jp Delta is char-grain (smears 叠字/
     compounds), flagged; it does not affect the line reading.
  F6 pypinyin absent in venv → sound-device 雙聲/叠韵 pinyin-fallback is
     skipped (中古/叠字/rep/alliteration paths intact); color/plant/
     temporal are pypinyin-independent.
  F9 LOCAL_TIER (in-copyright acquisitions). By house law in-copyright
     transcriptions live OUTSIDE the repo, under an acquisitions root
     (see LOCAL below and $STRATA_LOCAL_CORPUS); the repo carries
     provenance + shas only. This
     scorer reads them as declared inputs (paths + shas recorded in the
     run manifest) but the OUTPUTS REDACT their line text: word-grain
     receipts (firing tokens) + numbers only, never full-line quotes of
     an in-copyright translation inside publishable/. Kraus is held to
     the same rule (his own header: "US PD not asserted").

Determinism discipline (house scorers): sorted iteration · encode
seed = RandomState(48) for the re-order certificate (batch_size=1,
drift < 1e-6, matching smoke_score_sheets_50.py) · every input
sha256-pinned into the output manifest.
"""
import argparse
import glob
import hashlib
import json
import os
import re
import sys
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------- paths
HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent                       # repo root (instrument/)
PROTO = REPO / "engine"
RESULTS = PROTO / "results"
MODELS = PROTO / "models"
MARK_TOOLS = REPO / "marking" / "tools"
CORPUS = REPO / "corpus"

sys.path.insert(0, str(MARK_TOOLS))
sys.path.insert(0, str(PROTO))

SEED = 48
CJK = re.compile(r"[㐀-鿿豈-﫿\U00020000-\U0002ffff]")
KANA = re.compile(r"[぀-ヿ]")

# ---------------------------------------------------------- ruler wiring
# (field, npz filename, key-inside-npz, credential-string). LaBSE space.
# npz keys verified: color/plant/sound/duration -> "axis";
# illum -> "dark" (A1 physical VALUE, valence-orthogonalized).
SCALAR = [
    ("color",        "color_salience_axis_48.npz",     "axis", "AUC .879 [.830-.926] (R1-gamma, RULERS A3)"),
    ("illumination", "illum_polarity_axis_v3_48.npz",  "dark", ".825 [.740-.906] (R1-beta, RULERS A1, physical VALUE dark+)"),
    ("sound",        "sound_salience_axis_v3_49.npz",  "axis", ".815 [.786-.843] (R1-gamma, RULERS A5, realized)"),
    ("plant",        "plant_salience_axis_48.npz",     "axis", ".801 [.756-.841] (R1-gamma, RULERS A4)"),
    ("temporal",     "duration_value_axis_48.npz",     "axis", "rho .860 [.843-.875] (RULERS A7, VALUE long+ = DURATION ruler; A9 salience is a documented negative, excluded)"),
]

# ------------------------------------------------- declared pilot board
# Sonnet 73, An 07-19 (r2_scalar_shift_spec_52.md §1;
# ensemble_scout_survey_51.md L317/334-336). Entries are
# (rid, path-or-None, tier): tier "repo" = PD, transcribed in-repo;
# tier "local" = in-copyright acquisition, LOCAL-ONLY by house law
# (outside the repo; outputs REDACT its line text — F9);
# path None = declared-but-missing (LIST, don't substitute).
# LOCAL_TIER root (F9): in-copyright transcriptions kept OUTSIDE this repo by
# licensing policy. This public artifact ships only the public-domain corpus
# texts (and redacted placeholders for the in-copyright seats). Set
# STRATA_LOCAL_CORPUS=<your acquisitions root> (sub-layout <translator>/sonnet_NN.md)
# to resolve the in-copyright seats locally; unset, they list as MISSING.
LOCAL = Path(os.environ.get(
    "STRATA_LOCAL_CORPUS",
    str(REPO / "acquisitions" / "transcriptions")))
BOARD = {
    "en": [  # the 1609 Quarto source
        ("shakespeare_1609", CORPUS / "sonnets/en_source/shakespeare_sonnet73_1609.txt", "repo"),
    ],
    "zh": [  # all four IN COPYRIGHT -> LOCAL_TIER transcriptions (page-read #51, 07-19)
        ("liang_zongdai", LOCAL / "liang_zongdai_sonnets/sonnet_73.md", "local"),
        ("tu_an_1955",    LOCAL / "tu_an_sonnets/sonnet_73.md",         "local"),
        ("liang_shiqiu",  LOCAL / "liang_shiqiu/sonnet_73.md",          "local"),
        ("gu_zhengkun",   LOCAL / "gu_zhengkun/sonnet_73.md",           "local"),
    ],
    "de": [  # 5 PD in corpus/ensemble/sonnet_73/*.md + Kraus LOCAL ("US PD not asserted", his header)
        ("bodenstedt_1862",  CORPUS / "ensemble/sonnet_73/bodenstedt_de_1862.md",   "repo"),
        ("george_1909",      CORPUS / "ensemble/sonnet_73/george_de_1909.md",       "repo"),
        ("gildemeister_1871",CORPUS / "ensemble/sonnet_73/gildemeister_de_1871.md", "repo"),
        ("regis_1836",       CORPUS / "ensemble/sonnet_73/regis_de_1836.md",        "repo"),
        ("wolff_1903",       CORPUS / "ensemble/sonnet_73/wolff_de_1903.md",        "repo"),
        ("kraus_1933",       LOCAL / "kraus/sonnet_73.md",                          "local"),
    ],
    "jp": [  # only Tsubouchi is PD+transcribed; board says ~7 "held" (soft count);
             # NO jp renderings exist in the local tier either (inventoried 07-22)
        ("tsubouchi_1928", CORPUS / "sonnets/jp_target/tsubouchi_sonnet73.txt", "repo"),
        ("takamatsu",      None, None),  # in-copyright, located-only, NOT transcribed anywhere
        # the remaining ~5 of the soft "~7 (held)" are neither enumerated
        # nor transcribed on disk (ensemble_scout_survey_51.md L336 "jp ~7 held").
    ],
}
SOURCE_LANG = "en"          # the source side of every pair
# languages whose boolean shelf is validated (F2). illumination is zh-only,
# handled per-field in boolean_states().
BOOL_COVERED_LANGS = {"en", "zh"}

# ------------------------------------------------------------ utilities
def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def verse_lines(path):
    """Extract the 14 verse lines. Declared rule (see README): the verse
    is the FINAL contiguous run of non-empty lines, after stripping each
    line, excluding a trailing/leading run that is a bare poem-number
    (^\\d+$ or CJK numerals) and dropping any leading markdown # / ** line.
    Works for the fenced .txt (en/jp: ==== header, bare number, verse) and
    the .md (de: # title, **provenance**, blank, verse)."""
    raw = Path(path).read_text(encoding="utf-8").splitlines()
    # split into blank-separated blocks of stripped non-empty lines
    blocks, cur = [], []
    for ln in raw:
        s = ln.strip()
        if s:
            cur.append(s)
        elif cur:
            blocks.append(cur); cur = []
    if cur:
        blocks.append(cur)
    if not blocks:
        return []
    verse = blocks[-1]
    # drop leading markdown header lines defensively
    while verse and (verse[0].startswith("#") or verse[0].startswith("**")):
        verse = verse[1:]
    # a lone poem-number line can trail into the last block only if no
    # blank separated it; guard both ends
    numre = re.compile(r"^[0-9〇一-九十百]+$")
    verse = [v for v in verse if not numre.match(v)]
    return verse


# ------------------------------------------------ boolean field states
_T = None
_ILLUM = None
def _labelers():
    global _T, _ILLUM
    if _T is None:
        import trait_labelers as T
        import illumination_labeler_53 as I
        _T, _ILLUM = T, I
    return _T, _ILLUM


def boolean_states(text, lang):
    """Per-line field STATE from the boolean shelf. Returns
    {field: {"fires": bool|None, "receipts": [...], "coverage": str}}.
    'None' fires = UNAVAILABLE (language not covered, F2) — never
    fabricated. Incidental shared-kanji hits on jp are tagged so.
    """
    T, I = _labelers()
    out = {}
    # fr: colour-only boolean coverage (her convening 07-28; citation-tier
    # B&K12∪GLAWI inventory, registration_descriptive_fr — other fields stay
    # uncovered for fr).
    # de: colour-only boolean coverage (#61 night build; citation-tier
    # B&K12-de ∪ kaikki inventory, de_build/registration_descriptive_de). Other
    # fields UNCOVERED for de, so de written/referent stay starred PARTIAL-
    # INVESTIGATION exactly like fr; the language-gated de leg in label_unit
    # supplies out['color'] on lang=='de' units. This is the CONSUMING-path half
    # of the wiring (the 2ebf673 lesson: the fix lands only when the consumer
    # consults it) — with lang=='de' now colour-covered, the bethge/forke/
    # heilmann colour crossings UNSTAR (2-state present*/silent* → the 4-state
    # scalar+boolean census cell).
    covered_fields = (set(("color", "sound", "sound_device", "plant",
                           "temporal")) if lang in BOOL_COVERED_LANGS
                      else ({"color"} if lang in ("fr", "de") else set()))
    lab = T.label_unit(text, lang)                       # color/sound/plant/temporal (en+zh)
    # #58 (2026-07-26): "sound" is now the WORD-TIER descriptive field
    # (label_unit renamed the DEVICE tier to "sound_device"). Carry
    # sound_device as its own field so the device data is PRESERVED in every
    # output; the transition table consumes the word-tier "sound"
    # (poem_inventory excludes sound_device — see below).
    for f in ("color", "sound", "sound_device", "plant", "temporal"):
        covered = f in covered_fields
        if covered:
            hit = f in lab and bool(lab[f][0])
            rec = lab[f][1].split() if hit else []
            cov = lang
        else:
            # de: no lexicon. jp: shared-kanji hits are INCIDENTAL, not a
            # validated jp labeler — report them but tag UNAVAILABLE.
            inc = (f in lab and bool(lab[f][0]))
            hit, rec, cov = None, (lab[f][1].split() if inc else []), (
                "incidental_kanji" if (lang == "jp" and inc) else "uncovered")
        out[f] = {"fires": hit, "receipts": rec, "coverage": cov}
    # illumination: whole-field boolean, ZH-only runtime lexicon (F2)
    ib, ihits = I.label(text)
    if lang == "zh":
        out["illumination"] = {"fires": bool(ib), "receipts": list(ihits), "coverage": "zh"}
    else:
        out["illumination"] = {
            "fires": None, "receipts": list(ihits),
            "coverage": ("incidental_kanji" if (lang == "jp" and ib) else "uncovered")}
    return out


# ----------------------------------------------------- scalar (encoder)
def load_axes():
    axes = {}
    for field, fn, key, cred in SCALAR:
        z = np.load(RESULTS / fn)
        axes[field] = {"mu": z["mu"], "W": z["W"], "axis": z[key], "fn": fn, "key": key, "cred": cred}
    return axes


def maskable_units(text):
    """(index, token) units for deletion-masking. zh -> jieba word units;
    latin -> whitespace tokens; jp (kana present) -> per-char (F5)."""
    # NOTE (#71, observation only — left exactly as-is because this feeds the
    # --run masking path): the second disjunct ends in _is_jp(text), which is
    # itself KANA.search(text), so the whole test reduces to "has kana". The
    # CJK/latin clauses cannot change the outcome.
    if KANA.search(text) or (CJK.search(text) and not re.search(r"[A-Za-z]", text) and _is_jp(text)):
        # jp: per-char over CJK+kana (no jp tokenizer in venv) — flagged F5
        return [(i, ch) for i, ch in enumerate(text) if CJK.match(ch) or KANA.match(ch)]
    if CJK.search(text):
        import jieba
        toks, out, pos = list(jieba.cut(text)), [], 0
        for t in toks:
            j = text.find(t, pos)
            if j >= 0 and t.strip():
                out.append((j, t)); pos = j + len(t)
        return out
    return [(m.start(), m.group()) for m in re.finditer(r"\S+", text)]


def _is_jp(text):
    return bool(KANA.search(text))


def delete_unit(text, unit):
    i, t = unit
    return text[:i] + text[i + len(t):]


def embed_inventory(model, inventory):
    """Encode with batch_size=1; re-order certificate at seed 48."""
    def enc(ts):
        return np.asarray(model.encode(ts, normalize_embeddings=True, batch_size=1))
    E1 = enc(inventory)
    order = np.random.RandomState(SEED).permutation(len(inventory))
    E2 = np.empty_like(E1)
    E2[order] = enc([inventory[i] for i in order])
    drift = float(np.max(np.abs(E1 - E2)))
    return E1, drift


def project(E, axes):
    """field -> per-inventory projection. (E - mu) @ W, unit-norm, @ axis."""
    proj = {}
    for field, a in axes.items():
        Ew = (E - a["mu"]) @ a["W"]
        Ew = Ew / (np.linalg.norm(Ew, axis=1, keepdims=True) + 1e-12)
        proj[field] = Ew @ a["axis"]
    return proj


def scalar_readings(model, axes, renderings):
    """renderings: {rid: {"lang":..., "lines":[...]}} -> per-line line
    scalar + FULL per-token |Delta| per field, sorted by |Delta| (key name
    top_delta kept for consumer compatibility; content complete since 07-26,
    manual §1.3 — top-k is presentation only, never the record). Single
    shared inventory (one encode)."""
    inv, idx = [], {}
    def add(s):
        if s not in idx:
            idx[s] = len(inv); inv.append(s)
    for rid, r in sorted(renderings.items()):
        for line in r["lines"]:
            add(line)
            for u in maskable_units(line):
                add(delete_unit(line, u))
    E, drift = embed_inventory(model, inv)
    proj = project(E, axes)
    out = {}
    for rid, r in sorted(renderings.items()):
        rows = []
        for li, line in enumerate(r["lines"]):
            reading = {f: float(proj[f][idx[line]]) for f in axes}
            contrib = {}
            for f in axes:
                base = proj[f][idx[line]]
                ds = [(t, float(base - proj[f][idx[delete_unit(line, u)]]))
                      for u in maskable_units(line) for t in (u[1],)]
                contrib[f] = sorted(ds, key=lambda x: -abs(x[1]))
            rows.append({"line_no": li + 1, "text": line, "reading": reading, "top_delta": contrib})
        out[rid] = rows
    return out, drift, len(inv)


# ----------------------------------------- comparator (the fixed 8-cell)
def poem_inventory(states_per_line):
    """Fold per-line boolean states -> a poem-level {field: {""}} active
    inventory for rubric_compare.compare(). A field is ACTIVE for the side
    if its boolean fires on ANY line (fires is True). Fields whose state is
    UNAVAILABLE (fires is None) on ALL lines are OMITTED (not 'absent') so
    the comparator never sees a fabricated de/jp state (F2)."""
    active, seen_any = {}, set()
    for st in states_per_line:
        for f, v in st.items():
            # sound_device = its own FIELD ROW since 07-26 (C1 field-split:
            # rhythm and chirp can take different verdicts in one translation;
            # manual §0/§7.7 — was: skipped from verdicts, carried for data only).
            if v["fires"] is True:
                active.setdefault(f, set()).add("")   # value-less: descriptive membership
            if v["fires"] is not None:
                seen_any.add(f)
    return active, seen_any


def transition_table(src_states, tr_states):
    """Run the FIXED comparator over poem-level boolean inventories.
    Returns (rows, coverage) or ("NO_COVERAGE", reason). No latent files
    (F4) -> FOLD-DECLARED; reachable cells SURVIVAL/DEFORMATION/INVENTION."""
    import rubric_compare as RC
    src_inv, src_seen = poem_inventory(src_states)
    tr_inv,  tr_seen  = poem_inventory(tr_states)
    if not tr_seen:
        return "NO_COVERAGE", ("target side has NO boolean-covered field states "
                               "(F2: booleans are en+zh only; this target's language "
                               "is uncovered) — transition classification not runnable")
    # restrict comparison to fields covered on BOTH sides
    both = src_seen & tr_seen
    src_c = {f: v for f, v in src_inv.items() if f in both}
    tr_c  = {f: v for f, v in tr_inv.items()  if f in both}
    rows, ladder = RC.compare(src_c, tr_c)        # src_latent=None,tr_latent=None -> fold declared
    # Ladder recorded as a "_"-meta row (manual §4.3; was discarded) — cell
    # consumers already skip "_"-prefixed rows by the existing convention.
    rows.append(("_ladder", ladder))
    return rows, sorted(both)


def survival_rates(rows):
    """Aggregate the fixed categories into per-field survival/loss/gain."""
    from collections import Counter
    cats = {f: c for f, c in rows if not f.startswith("_")}
    counts = Counter(cats.values())
    return {
        "SURVIVAL": [f for f, c in cats.items() if c == "SURVIVAL"],
        "DEFORMATION(loss)": [f for f, c in cats.items() if c == "DEFORMATION"],
        "INVENTION(gain)": [f for f, c in cats.items() if c == "INVENTION"],
        "counts": dict(counts),
        "fold_declared": any(f == "_meta" for f, _ in rows),
    }


# --------------------------------------------------------- corpus load
def load_corpus():
    """Resolve the declared board against disk (repo + local tier). Returns
    (present {rid:{lang,file,lines,sha,tier,redact}}, missing [{rid,lang,reason}]).
    tier="local" renderings are in-copyright acquisitions: their line text
    is REDACTED in every output under publishable/ (F9)."""
    present, missing = {}, []
    for lang, items in BOARD.items():
        for rid, path, tier in items:
            full = f"{lang}:{rid}"
            if path is None or not Path(path).exists():
                reason = ("declared on the board, not transcribed in repo OR local tier "
                          "(locate-only / in-copyright / held; see corpus/sonnets/*/locate_only*.md)")
                missing.append({"rid": full, "lang": lang, "reason": reason})
                continue
            lines = verse_lines(path)
            present[full] = {"lang": lang, "file": str(path),
                             "lines": lines, "n_lines": len(lines),
                             "sha256": sha256(path),
                             "tier": tier, "redact": (tier == "local")}
    return present, missing


# ---------------------------------------------------------- input shas
def input_manifest():
    m = {"axes": {}, "boolean_lexicons": {}, "comparator": {}, "model": {}}
    for field, fn, key, cred in SCALAR:
        p = RESULTS / fn
        m["axes"][fn] = {"sha256": sha256(p), "key": key, "field": field, "credential": cred}
    for p in [MARK_TOOLS / "illumination_lexicon_hownet_53.json",
              MARK_TOOLS / "trait_labelers.py",
              MARK_TOOLS / "illumination_labeler_53.py"]:
        if p.exists():
            m["boolean_lexicons"][p.name] = sha256(p)
    rc = MARK_TOOLS / "rubric_compare.py"
    m["comparator"][rc.name] = sha256(rc)
    ml = MODELS / "LaBSE" / "model.safetensors"
    if ml.exists():
        m["model"]["LaBSE/model.safetensors"] = {"sha256": sha256(ml)}
    return m


# ================================================================ MODES
def mode_dry():
    """Real corpus, NO encoder. Inventory + alignment + boolean fires +
    embed estimate + shas.

    DEPENDENCY NOTE (#71): "no encoder" does not mean "stdlib only". This mode
    still needs numpy (module import) and jieba — the zh illumination labeler
    tokenises EVERY line whatever its language, so a tree without jieba dies at
    the boolean-fire tally with ModuleNotFoundError, after printing the
    inventory/alignment blocks."""
    present, missing = load_corpus()
    print("=" * 70)
    print("DRY / COUNT MODE — real corpus, no encoder")
    print("=" * 70)

    by_lang = {}
    for rid, r in sorted(present.items()):
        by_lang.setdefault(r["lang"], []).append(r)
    print("\n[renderings on disk, scoring-clean — tier repo=PD-in-repo, LOCAL=in-copyright")
    print(" acquisition tier (outputs redact its line text, F9)]")
    for lang in ("en", "zh", "de", "jp"):
        rs = by_lang.get(lang, [])
        print(f"  {lang}: {len(rs)} present")
        for r in rs:
            tag = "LOCAL" if r["redact"] else "repo "
            print(f"      [{tag}] {Path(r['file']).parent.name + '/' + Path(r['file']).name:44} "
                  f"lines={r['n_lines']}  sha={r['sha256'][:12]}")
    print("\n[declared but MISSING on disk — listed, not substituted]")
    for m in missing:
        print(f"  {m['rid']:22} ({m['lang']})  {m['reason'].splitlines()[0]}")

    print("\n[alignment convention]")
    align = list(glob.glob(str(CORPUS / "**/*sonnet*align*"), recursive=True)) + \
            list(glob.glob(str(CORPUS / "**/*73*align*"), recursive=True))
    print(f"  alignment files found for sonnet 73: {len(align)}  {align}")
    print("  → NONE. Fixed comparator grain = POEM-level (rubric_compare.py header;")
    print("    line-grain needs a chair-drafted s<i>->t<j> file, R2 (b), UNFROZEN). ")
    print("  → per-rendering line structure = the file's own printed lines "
          "(final-block parse); sonnet 73 = 14 lines. Monotone line-i<->line-i")
    print("    line-pairing is available only behind --align and is FLAGGED unfrozen (F1).")

    print("\n[boolean fire counts per field per language — the shelf is en+zh only, F2]")
    fields = ["color", "illumination", "sound", "plant", "temporal"]
    tally = {}
    for rid, r in sorted(present.items()):
        lang = r["lang"]
        for line in r["lines"]:
            st = boolean_states(line, lang)
            for f in fields:
                key = (lang, f)
                d = tally.setdefault(key, {"fires": 0, "unavailable": 0, "incidental": 0, "lines": 0})
                d["lines"] += 1
                v = st[f]["fires"]
                if v is True:
                    d["fires"] += 1
                elif v is None:
                    d["unavailable"] += 1
                    if st[f]["coverage"] == "incidental_kanji" and st[f]["receipts"]:
                        d["incidental"] += 1
    print(f"    {'lang':4} {'field':13} {'fires':>6} {'unavail':>8} {'incid.kanji':>12} {'lines':>6}")
    for lang in ("en", "zh", "de", "jp"):
        for f in fields:
            d = tally.get((lang, f))
            if not d:
                continue
            print(f"    {lang:4} {f:13} {d['fires']:6d} {d['unavailable']:8d} {d['incidental']:12d} {d['lines']:6d}")

    # embed estimate for the real run
    n_texts = 0
    for rid, r in sorted(present.items()):
        for line in r["lines"]:
            n_texts += 1 + len(maskable_units(line))
    uniq = set()
    for rid, r in sorted(present.items()):
        for line in r["lines"]:
            uniq.add(line)
            for u in maskable_units(line):
                uniq.add(delete_unit(line, u))
    print("\n[embed estimate for the real run (LaBSE, batch_size=1)]")
    print(f"  base inventory (line + one-deletion masks): {len(uniq)} unique texts")
    print(f"  raw (pre-dedup) encode units: {n_texts}")
    print(f"  certificate re-order replay doubles it: ~{2*len(uniq)} encodes total")

    print("\n[transition table runnability]")
    tgt_covered = sorted(rid for rid, r in present.items()
                         if r["lang"] != SOURCE_LANG and r["lang"] in BOOL_COVERED_LANGS)
    tgt_uncov = sorted(rid for rid, r in present.items()
                       if r["lang"] != SOURCE_LANG and r["lang"] not in BOOL_COVERED_LANGS)
    print(f"  boolean-coverable TARGET renderings (lang in {sorted(BOOL_COVERED_LANGS - {SOURCE_LANG})}): "
          f"{len(tgt_covered)}  {tgt_covered}")
    print(f"  → RUNNABLE en-source ↔ target transition pairs: {len(tgt_covered)}")
    print(f"  scalar-only targets (boolean-uncovered langs, F2): {len(tgt_uncov)}  {tgt_uncov}")
    print("  (Scalar readings run for ALL present renderings; cross-side comparison")
    print("   is rank-space only, §3, equating unfrozen — F3.)")

    print("\n[input shas]")
    man = input_manifest()
    for grp, d in man.items():
        for k, v in d.items():
            s = v["sha256"] if isinstance(v, dict) else v
            print(f"  {grp:18} {k:34} {s[:16]}…")
    return 0


def mode_smoke():
    """2-3 toy lines through the FULL path (booleans + one axis read +
    transition classify). Writes ONLY to /tmp."""
    out = Path("/tmp/descriptive_smoke")
    out.mkdir(exist_ok=True)
    print("SMOKE — toy lines, full path, writes only to", out)

    # toy source (en) vs a synthetic en "translation" + a zh toy line
    src_lines = ["When yellow leaues, or none, or few doe hange",
                 "In me thou seest the glowing of such fire,"]
    tr_lines = ["Where golden leaves upon the boughs still cling",   # color+plant kept, temporal dropped
                "In me you see the embers of a flame,"]              # sound/illum shift
    zh_line = ["黄葉飄零"]

    src_states = [boolean_states(t, "en") for t in src_lines]
    tr_states = [boolean_states(t, "en") for t in tr_lines]
    zh_states = [boolean_states(t, "zh") for t in zh_line]
    print("\n[booleans — source]")
    for t, s in zip(src_lines, src_states):
        fired = {f: v["receipts"] for f, v in s.items() if v["fires"]}
        print(f"  {t}\n     fires: {fired}")
    print("[booleans — zh toy (illumination zh-only labeler active)]")
    for t, s in zip(zh_line, zh_states):
        fired = {f: v["receipts"] for f, v in s.items() if v["fires"]}
        print(f"  {t}\n     fires: {fired}")

    # ONE axis read + encoder on the toy inventory
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(str(MODELS / "LaBSE"), device="cpu")
    axes_all = load_axes()
    axes = {"color": axes_all["color"]}          # one axis, per the smoke charter
    rend = {"en:src": {"lang": "en", "lines": src_lines},
            "en:tr": {"lang": "en", "lines": tr_lines}}
    readings, drift, ninv = scalar_readings(model, axes, rend)
    print(f"\n[scalar — one axis (color), certificate drift={drift:.2e} over {ninv} texts]")
    assert drift < 1e-6, f"certificate FAILED: {drift}"
    for rid, rows in sorted(readings.items()):
        for row in rows:
            td = row["top_delta"]["color"]
            print(f"  {rid} L{row['line_no']} color={row['reading']['color']:+.3f}  "
                  f"topΔ={[(t, round(d,3)) for t,d in td]}")

    # transition classify (poem grain, fold declared)
    rows, cov = transition_table(src_states, tr_states)
    rates = survival_rates(rows) if rows != "NO_COVERAGE" else None
    print(f"\n[transition — 8-cell comparator, poem grain, fold-declared]  coverage={cov}")
    print(f"  rows: {rows}")
    print(f"  survival/loss/gain: {rates}")

    (out / "smoke_result.json").write_text(json.dumps({
        "certificate": drift, "n_inventory": ninv,
        "source_booleans": [{f: v for f, v in s.items()} for s in src_states],
        "scalar_color": {rid: [r["reading"]["color"] for r in rows_] for rid, rows_ in readings.items()},
        "transition_rows": rows, "survival_rates": rates,
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    print("\n→ /tmp/descriptive_smoke/smoke_result.json  (nothing written under the repo)")
    print("SMOKE OK")
    return 0


def mode_run(align_file=None):
    """The REAL scoring run. Writes descriptive_scores.json + .md INTO this
    folder. Fired by the orchestrator AFTER her review — not by build/smoke."""
    present, missing = load_corpus()
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(str(MODELS / "LaBSE"), device="cpu")
    axes = load_axes()

    rend = {rid: {"lang": r["lang"], "lines": r["lines"]} for rid, r in present.items()}
    readings, drift, ninv = scalar_readings(model, axes, rend)
    if drift >= 1e-6:
        print(f"CERTIFICATE FAILED {drift:.2e} — aborting (house law).", file=sys.stderr)
        return 1

    # per-line boolean states
    booleans = {rid: [boolean_states(line, present[rid]["lang"]) for line in present[rid]["lines"]]
                for rid in present}

    # ensemble ranks (per field, per line-position pooled per side language) — rank space (§3)
    fields = [f for f, *_ in SCALAR]
    # cross-side transitions where runnable (F1 poem grain default; F2 coverage)
    src_ids = [rid for rid in present if present[rid]["lang"] == SOURCE_LANG]
    transitions = {}
    if src_ids:
        src = src_ids[0]
        for rid in sorted(present):
            if rid == src:
                continue
            rows, cov = transition_table(booleans[src], booleans[rid])
            transitions[rid] = {
                "grain": "poem",
                "coverage": cov,
                "rows": rows if rows != "NO_COVERAGE" else None,
                "note": (cov[1] if rows == "NO_COVERAGE" else None),
                "survival_rates": survival_rates(rows) if rows != "NO_COVERAGE" else None,
            }

    # F9 REDACTION: strip line text of local-tier (in-copyright) renderings
    # from everything that lands under publishable/. Word-grain receipts
    # (firing tokens, top-Delta tokens) + numbers stay.
    for rid, r in present.items():
        if r["redact"]:
            for row in readings[rid]:
                row["text"] = None
                row["text_redacted"] = ("in-copyright LOCAL_TIER transcription — full-line "
                                        "text never enters publishable/ (F9); source file + "
                                        "sha in manifest")

    manifest = input_manifest()
    manifest["seed"] = SEED
    manifest["certificate_drift"] = drift
    manifest["n_inventory"] = ninv
    manifest["corpus_present"] = {rid: {"sha256": present[rid]["sha256"],
                                        "tier": present[rid]["tier"],
                                        "file": present[rid]["file"],
                                        "text_redacted_in_outputs": present[rid]["redact"]}
                                  for rid in sorted(present)}
    manifest["corpus_missing"] = missing

    result = {
        "what": "deterministic descriptive fields — §8 demonstration scoring, sonnet 73",
        "law": "methodology_statement_0716.md §3/§5/§6/§7/§8/§9; RULERS.md A1/A3/A4/A5/A7",
        "flags": ["F1 grain=poem (line needs chair alignment, unfrozen)",
                  "F2 booleans en+zh only; de/jp target states UNAVAILABLE",
                  "F3 raw scalar deltas NON-TRANSFERABLE (§3); equating unfrozen",
                  "F4 fold-declared (no latent files; descriptive row only)",
                  "F5 jp per-word Δ char-grain", "F6 pypinyin absent"],
        "manifest": manifest,
        "scalar_readings": readings,
        "booleans": {rid: [{f: {"fires": v["fires"], "receipts": v["receipts"],
                                 "coverage": v["coverage"]} for f, v in st.items()}
                           for st in booleans[rid]] for rid in booleans},
        "transitions": transitions,
    }
    (HERE / "descriptive_scores.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    _write_human_table(present, readings, booleans, transitions, manifest)
    print(f"→ descriptive_scores.json + descriptive_scores.md  (certificate {drift:.2e})")
    return 0


def _write_human_table(present, readings, booleans, transitions, manifest):
    md = ["# Descriptive-field scores — Sonnet 73 (§8 demonstration run)",
          "",
          "*Instruments only (no LLM marks anything). THE SCALAR IS THE PAPER.*",
          f"*Certificate (re-order, batch_size=1): {manifest['certificate_drift']:.2e} — "
          f"seed {manifest['seed']}. Scalar space = LaBSE + each axis npz's own mu/W.*",
          "",
          "Flags: F1 grain=poem · F2 booleans en+zh only (de/jp field states UNAVAILABLE) · "
          "F3 raw scalar deltas NON-TRANSFERABLE, comparison is rank-space (§3), equating unfrozen · "
          "F4 fold-declared.", ""]
    for rid in sorted(present):
        r = present[rid]
        md.append(f"## {rid}  ({r['lang']}, {r['n_lines']} lines)")
        md.append("")
        md.append("| line | text | color | illum | sound | plant | temporal | booleans fired |")
        md.append("|---|---|---|---|---|---|---|---|")
        if r["redact"]:
            md.append(f"*(line text REDACTED — in-copyright LOCAL_TIER, F9; "
                      f"file + sha in `descriptive_scores.json` manifest)*")
        for row, st in zip(readings[rid], booleans[rid]):
            rd = row["reading"]
            fired = " ".join(f"{f}[{' '.join(v['receipts'])}]"
                             for f, v in st.items() if v["fires"] is True) or "—"
            txt = "*(redacted)*" if row.get("text") is None else row["text"].replace("|", "/")
            md.append(f"| {row['line_no']} | {txt} | {rd['color']:+.2f} | {rd['illumination']:+.2f} | "
                      f"{rd['sound']:+.2f} | {rd['plant']:+.2f} | {rd['temporal']:+.2f} | {fired} |")
        md.append("")
    md.append("## Cross-side transitions (8-cell comparator, poem grain, fold-declared)")
    md.append("")
    for rid, t in sorted(transitions.items()):
        if t["rows"] is None:
            md.append(f"- **{rid}**: NOT RUNNABLE — {t['note']}")
        else:
            md.append(f"- **{rid}** (fields {t['coverage']}): {t['survival_rates']}")
    (HERE / "descriptive_scores.md").write_text("\n".join(md), encoding="utf-8")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="§8 descriptive-field scoring")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry", action="store_true", help="real corpus, no encoder: inventory/alignment/fires/estimate/shas")
    g.add_argument("--smoke", action="store_true", help="2-3 toy lines, full path, writes only /tmp")
    g.add_argument("--run", action="store_true", help="REAL run (orchestrator, post-review): writes json+md here")
    ap.add_argument("--align", default=None, help="chair-drafted s<i>->t<j> alignment file (F1; unfrozen)")
    a = ap.parse_args()
    if a.dry:
        sys.exit(mode_dry())
    if a.smoke:
        sys.exit(mode_smoke())
    if a.run:
        sys.exit(mode_run(a.align))
