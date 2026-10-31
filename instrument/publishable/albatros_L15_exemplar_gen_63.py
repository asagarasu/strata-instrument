#!/usr/bin/env python3
"""Current-law exemplar regeneration, parameterized (#63, 2026-07-29).

PANELS (each replaces a stale pre-two-strip exhibit; records NEVER touched):
  albatros — albatros L15 COLOUR (idx 14). Record kept:
      reports/figures/albatros_L15_color_h1_exemplar_61.svg
      Output: reports/figures/albatros_L15_color_h1_exemplar_63.svg
  loom     — tiaotiao L4 SOUND (idx 3, 札札弄机杼). Records kept:
      reports/figures/samples_59/sample_sound_tiaotiao_L4_59.svg
      reports/figures/sound_exhibit_tiaotiao_L4_UNREDACTED.svg
      Output: reports/figures/loom_exhibit_tiaotiao_L4_sound_63.svg

Route (both panels): regenerate THROUGH exhibit_gen_60 (the current display
law) — build_model -> render -> gate, the very path interesting_gen_61 uses.
exhibit_gen_60 and linegrain_law_60 are import-safe (guarded main / no
import-time work). Nothing about the law is duplicated or hardcoded; the only
literals are exhibit_gen_60.render's fixed panel coordinates (mirrored solely
to seat an ADDITIVE annotation) and the chair-given numbers being TESTED, plus
the v6 graded RELABEL LOGIC (not numbers) lifted verbatim from
engine/census_coverage_ledger_63.py.

v6 GRADED LABELS (her #63 coverage ruling): a side's ghost/latent is only as
strong as the channels its language ran —
  zh (full stack)      : ghost stays ghost
  en (referent-open)   : ghost -> could-be-ghost ; latent stands
  de/fr/jp (stated only): ghost|latent -> not-stated (unresolvable disjunction)
Drawn as a small extra 'coverage-graded' column, class="v6-graded" — ADDITIVE
only; raw state and transmission cells UNTOUCHED (the gate re-derives them);
the augmented SVG is re-gated to prove the annotation inert to gates A-F5.
*-states (present*/silent*: the WORD channel itself uncovered — chan_word
wstate None) carry the note "(lang: word channel uncovered)". The albatros
emission is byte-identical to the shipped _63 SVG (left-anchored at GX); loom
uses right-anchored labels (text-anchor=end at GXR — the longer *-note would
overflow the 1980px canvas left-anchored at the same column).

LOOM FORKE HISTORY, of record (#63, corrections superseded never erased): the
coordinator's FIRST brief gave forke_1899 as silent* / Weberin -0.0466 / zero
fires — an identity-index error (those numbers are forke's PHYSICAL line 4,
"Sitzt die Weberin fern.", which renders a DIFFERENT source line; navigation
pairing, which the law rejects). Chair-side correction, same sitting: forke is
aligned VIA FILE (corpus/alignments/tiaotiao__de_forke_1899.json; 20 seat
lines vs 10 source), src L4 -> seat [7,8] ("札札 onomatopoeic -> 'Webstuhl
klappert laut', sound-preserved" per the map's own note); under the law the
fold reads carrier L7: PRESENT* via scalar, starred (two-flag), fires klappert
+0.1509 / laut +0.1396 (louder than xu's tune), L8 fires fliegt's +0.0639,
wording None on both mapped lines; highlight = klappert (|Δ|-max, positive).
The stale samples_59 sidecar had already recorded present*/klappert. This
script asserts the CORRECTED facts as blocking checks; if build_model ever
rendered forke as a gate-B status row (unaligned) the roster check exits loud
— aligned-via-file seats must fold, never sit out.

Writes ONLY the requested panel's SVG. No sidecar rewrites, no law/census/
registration edits. Any blocking check or gate failure exits loud, writing
nothing. Guarded main; run with engine/venv/bin/python (display-only
over committed data — no encoder work). Usage:
    python albatros_L15_exemplar_gen_63.py [albatros|loom]   (default albatros)
"""
import html
import subprocess
import sys
from pathlib import Path

import linegrain_law_60 as LAW          # import-safe (constants + defs only)
import exhibit_gen_60 as GEN            # import-safe (guarded main)

HERE = Path(__file__).resolve().parent
FIGDIR = HERE.parent / "reports" / "figures"

# exhibit_gen_60.render's row geometry (mirrored ONLY to seat an additive
# annotation on the correct row; the render owns these):
Y0, YSTEP = 148, 58

PANELS = {
    "albatros": dict(
        board="albatros", line_idx=14, field="color",
        out="albatros_L15_color_h1_exemplar_63.svg",
        records=["albatros_L15_color_h1_exemplar_61.svg"],
        inject_style="left",           # byte-identical to the shipped _63
    ),
    "loom": dict(
        board="tiaotiao", line_idx=3, field="sound",
        out="loom_exhibit_tiaotiao_L4_sound_63.svg",
        records=["samples_59/sample_sound_tiaotiao_L4_59.svg",
                 "sound_exhibit_tiaotiao_L4_UNREDACTED.svg"],
        inject_style="right",          # anchor-end (long *-note fits canvas)
    ),
}

# v6 graded relabel — LOGIC lifted verbatim from census_coverage_ledger_63.py
# (her #63 coverage scheme). Law-shape, no numbers.
CLASS = {"zh": "full-stack", "en": "referent-open"}


def lang_class(lang):
    return CLASS.get(lang, "stated-only")            # de / fr / jp


def relabel(state, lang):
    c = lang_class(lang)
    if state == "ghost":
        return {"full-stack": "ghost", "referent-open": "could-be-ghost",
                "stated-only": "not-stated"}[c]
    if state == "latent":
        return "latent" if c in ("full-stack", "referent-open") else "not-stated"
    return state          # stated / present* / silent / silent* untouched


# graded-label ink: colour by class so the reader can see coverage at a glance
GRADE_COL = {"ghost": "#7c3aed",          # full-stack ghost — resolved (purple)
             "could-be-ghost": "#b45309",  # en referent-open — amber-brown
             "not-stated": "#94a3b8",      # stated-only — pale slate (weakest)
             "stated": "#166534", "silent": "#64748b",
             "present*": "#166534", "silent*": "#64748b", "latent": "#0f766e"}
GX = 1905          # left-anchored annotation column x (albatros, as shipped)
GXR = 1972         # right-anchored annotation edge x (loom; W=1980)

LEGEND_SENTENCE = (
    'coverage-graded seat label (#63): a '
    'side’s ghost/latent is only as strong as its language’s '
    'channels — zh full-stack (ghost stays ghost) · en '
    'referent-open (ghost→could-be-ghost) · de/fr/jp '
    'stated-only (ghost→not-stated). Raw state &amp; '
    'transmission unchanged; this column is the graded reading.')


def _graded_note(graded, state, lang, style):
    """The parenthetical after a graded token. Moved labels name the coverage
    gap; RIGHT style additionally notes *-states (word channel uncovered —
    exactly the chan_word wstate-None case). LEFT keeps the albatros emission
    of record byte-identical (no *-states occur on that panel)."""
    if graded != state:
        return {"not-stated": " (de: word-only)",
                "could-be-ghost": " (en: no referent)"}.get(graded, "")
    if style == "right" and state.endswith("*"):
        return f" ({lang}: word channel uncovered)"
    return ""


def inject_graded(svg, m, style):
    """Additive v6 graded-label column + one legend line. Touches nothing the
    gate counts (fresh class 'v6-graded'; no field-hue circle; no gated class
    string; no fill-opacity=0.35). Inserted just before </svg>."""
    add = []
    if style == "left":
        # header legend line for the graded column (sits in the free band under
        # the existing badge legend at y=67) — the albatros emission of record
        add.append(f'<text x="{GX-2}" y="128" font-size="9" font-weight="bold" '
                   f'fill="#334155" class="v6-graded-head">coverage-graded '
                   f'(#63)</text>')
    else:
        add.append(f'<text x="{GXR}" y="128" font-size="9" font-weight="bold" '
                   f'fill="#334155" text-anchor="end" class="v6-graded-head">'
                   f'coverage-graded (#63)</text>')
    add.append(f'<text x="20" y="82" font-size="9.5" fill="#555" '
               f'class="v6-graded-legend">{LEGEND_SENTENCE}</text>')
    for i, r in enumerate(m["seats"]):
        y = Y0 + i * YSTEP
        if r.get("unaligned"):
            continue
        graded = relabel(r["state"], r["lang"])
        col = GRADE_COL.get(graded, "#334155")
        label = html.escape(graded + _graded_note(graded, r["state"],
                                                  r["lang"], style))
        weight = 'font-weight="bold"' if graded == "ghost" else ""
        if style == "left":
            add.append(f'<text x="{GX}" y="{y+20}" font-size="9.5" fill="{col}" '
                       f'{weight} class="v6-graded">{label}</text>')
        else:
            add.append(f'<text x="{GXR}" y="{y+20}" font-size="9.5" '
                       f'fill="{col}" {weight} text-anchor="end" '
                       f'class="v6-graded">{label}</text>')
    return svg.replace("</svg>", "\n".join(add) + "\n</svg>")


# ---------------------------------------------------------------- FACTS ----
# Each panel's chair-given facts, RE-DERIVED through the law before drawing.
# All checks are BLOCKING: any failure prints and exits, writing nothing.

def _carrier_row(d, rid, s, line_idx):
    ci = s.get("carrier_line", line_idx + 1) - 1
    return d["scalar_readings"][rid][ci], ci


def _boolrow(d, rid, ci):
    rr = d["scalar_readings"][rid]
    return (d["booleans"].get(rid) or [{}] * len(rr))[ci] \
        if d["booleans"].get(rid) else {}


def facts_albatros(m, d):
    LI, FIELD = 14, "color"
    byrid = {s["rid"]: s for s in m["seats"] if not s.get("unaligned")}
    checks = []

    def want(cond, why):
        checks.append((bool(cond), why))

    # fr source: wording silent, NO colour token fires (positive-only salience
    # -> negative top-tok Exilé is dilution), line colour negative, state silent
    src = byrid["fr:baudelaire_1861"]
    srow, ci = _carrier_row(d, "fr:baudelaire_1861", src, LI)
    _rcpt, wst = LAW.chan_word(FIELD, _boolrow(d, "fr:baudelaire_1861", ci))
    want(wst == "silent", "fr source wording SILENT")
    want(len(LAW.triggered_tokens(srow, FIELD, m["cut"])) == 0
         and src["state"] == "silent",
         "fr source NO colour token fires (positive-only) -> state silent")
    want(src["v"] is not None and src["v"] < 0,
         "fr source line colour NEGATIVE")
    for rid in ["en:aggeler", "en:campbell", "en:dillon", "en:leclercq",
                "en:wilbur"]:
        s = byrid[rid]
        want(s["state"] == "stated"
             and any(LAW._word0(x) == "earth"
                     for x in s["investigation"]["word"]["line_receipts"]),
             f"{rid} STATED word 'earth'")
    for rid in ["de:george_1901", "de:kalckreuth_1907"]:
        s = byrid[rid]
        want(s["state"] == "ghost" and relabel(s["state"], s["lang"])
             == "not-stated", f"{rid} raw GHOST -> graded NOT-STATED")
    for rid in ["zh:dai_wangshu", "zh:guo_hongan"]:
        s = byrid[rid]
        want(s["state"] == "ghost" and relabel(s["state"], s["lang"])
             == "ghost" and s.get("full_stack"),
             f"{rid} raw GHOST -> graded GHOST (full stack)")
    s = byrid["zh:qian_chunqi"]
    want(s["state"] == "silent" and not s["top_tok"]["triggered"],
         "zh:qian_chunqi SILENT, no fires")
    want(abs(m["cut"] - 0.014944) < 1e-5, "adopted colour cut 0.014944")
    return checks


def facts_loom(m, d):
    """Coordinator brief #63 AS CORRECTED same sitting (forke identity-index
    error superseded — see module docstring), re-derived through the law."""
    LI, FIELD = 3, "sound"
    byrid = {s["rid"]: s for s in m["seats"] if not s.get("unaligned")}
    checks = []

    def want(cond, why):
        checks.append((bool(cond), why))

    want(abs(m["cut"] - 0.024173) < 1e-5, "sound cut 0.024173")
    want(m["src_rid"] == "zh:gushi19_10", "src rid zh:gushi19_10")
    # roster first: aligned-via-file seats must FOLD, never sit out as gate-B
    # status rows (the coordinator's loud-report condition — forke must be here)
    want(set(byrid) == {"zh:gushi19_10", "en:birrell", "en:owen",
                        "en:waley_1918", "en:watson", "en:xu_yuanchong",
                        "en:google_translate", "de:forke_1899"},
         "aligned roster == the brief's 8 seats (forke folded via file, "
         "NOT a status row)")
    src = byrid[m["src_rid"]]
    srow, sci = _carrier_row(d, m["src_rid"], src, LI)
    _r, wst = LAW.chan_word(FIELD, _boolrow(d, m["src_rid"], sci))
    want(wst == "silent" and not LAW.triggered_tokens(srow, FIELD, m["cut"])
         and src["state"] == "silent",
         "src zh:gushi19_10 wording silent, no fires, state silent")
    STATED = {"en:birrell": ({"clack", "click"}, ("clack", 0.0454)),
              "en:owen": ({"clack"}, ("clack", 0.0249)),
              "en:waley_1918": ({"click"}, None),
              "en:watson": ({"clack"}, None),
              "en:xu_yuanchong": ({"clack", "tune"}, ("tune", 0.1348)),
              "en:google_translate": ({"clatter"}, None)}
    for rid, (words, fired) in STATED.items():
        s = byrid[rid]
        rec = {LAW._word0(x)
               for x in s["investigation"]["word"]["line_receipts"]}
        want(s["state"] == "stated" and rec == words,
             f"{rid} STATED {sorted(words)}")
        if fired:
            w, dexp = fired
            row, _ = _carrier_row(d, rid, s, LI)
            dgot = LAW.token_delta_of(w, row, FIELD)
            want(dgot is not None and abs(dgot - dexp) < 5e-4,
                 f"{rid} fired {w} ~{dexp:+.4f} (law: {dgot})")
    want(byrid["en:google_translate"]["mt"] is True, "google_translate is MT")
    # owen under F8 (her ruling 07-29; registration display_law_F8_...):
    # salience top-tok = max POSITIVE contentful -> clacking +0.0249 FIRED;
    # shuttle (−0.0308) no longer highlighted; highlight == claimed surface
    owen = byrid["en:owen"]
    want(owen["top_tok"]["token"] is not None
         and LAW.fold(owen["top_tok"]["token"]).startswith("clack")
         and abs(owen["top_tok"]["delta"] - 0.0249) < 5e-4
         and owen["top_tok"]["triggered"]
         and not owen["top_tok"].get("faded"),
         "en:owen F8 top-tok clacking ~+0.0249 FIRED (not shuttle)")
    want(owen["highlight"]["word"] is not None
         and "clack" in owen["highlight"]["word"].lower(),
         "en:owen highlight = clacking under F8")
    # ---- forke, CORRECTED brief: aligned VIA FILE, src L4 -> seat [7,8] ----
    fk = byrid["de:forke_1899"]
    want(fk.get("folded_from") == [7, 8] and fk.get("carrier_line") == 7,
         "forke fold src L4 -> seat [7,8], carrier L7 (PI-approved map)")
    # wording None (de sound word channel uncovered) on BOTH mapped lines
    for j in (6, 7):
        _rj, wj = LAW.chan_word(FIELD, _boolrow(d, "de:forke_1899", j))
        want(wj is None, f"forke wording None on mapped L{j+1} "
                         f"(word channel uncovered)")
    want(fk["state"] == "present*" and fk["two"] is True,
         "forke folded state present*, starred True (borrowed-cut two-flag)")
    l7 = d["scalar_readings"]["de:forke_1899"][6]
    l8 = d["scalar_readings"]["de:forke_1899"][7]
    f7 = {LAW.fold(t): dd for t, dd in LAW.triggered_tokens(l7, FIELD, m["cut"])}
    f8 = {LAW.fold(t): dd for t, dd in LAW.triggered_tokens(l8, FIELD, m["cut"])}
    want("klappert" in f7 and abs(f7["klappert"] - 0.1509) < 5e-4
         and "laut" in f7 and abs(f7["laut"] - 0.1396) < 5e-4,
         f"forke L7 fires klappert +0.1509, laut +0.1396 (law: {f7})")
    want(any(k.startswith("fliegt") for k in f8)
         and abs(next(v for k, v in f8.items()
                      if k.startswith("fliegt")) - 0.0639) < 5e-4,
         f"forke L8 fires fliegt's +0.0639 (law: {f8})")
    # klappert is the strongest sound fire at this source line (louder than
    # xu's tune) and the |Δ|-max top-tok -> gate C highlights klappert
    xu_row, _ = _carrier_row(d, "en:xu_yuanchong", byrid["en:xu_yuanchong"], LI)
    want(f7.get("klappert", 0) > (LAW.token_delta_of("tune", xu_row, FIELD)
                                  or 0),
         "forke klappert louder than xu's tune")
    want(fk["top_tok"]["token"] is not None
         and LAW.fold(fk["top_tok"]["token"]) == "klappert"
         and fk["top_tok"]["delta"] > 0
         and fk["highlight"]["word"] is not None
         and LAW.fold(fk["highlight"]["word"]) == "klappert",
         "forke gate-C highlight = klappert (positive |Δ|-max)")
    ghosts = [r["rid"] for r in m["seats"]
              if not r.get("unaligned") and r["state"] == "ghost"]
    want(not ghosts, f"no ghosts on panel (got {ghosts})")
    return checks


FACTS = {"albatros": facts_albatros, "loom": facts_loom}


# ----------------------------------------------------------------- MAIN ----

def main(panel_key):
    p = PANELS[panel_key]
    out = FIGDIR / p["out"]
    records = [FIGDIR / r for r in p["records"]]
    for k in records:
        if not k.exists():
            sys.exit(f"REFUSE: record {k.name} missing — will not proceed")
        if out.resolve() == k.resolve():
            sys.exit("REFUSE: output path equals a record — abort")

    m = GEN.build_model(p["board"], p["line_idx"], p["field"])
    d, _l, _u = LAW.load_board(p["board"])
    checks = FACTS[panel_key](m, d)
    bad = [w for ok, w in checks if not ok]
    for w in bad:
        print("FACT MISMATCH:", w)
    if bad:
        sys.exit(f"{len(bad)} chair-fact mismatch(es) — NOTHING WRITTEN")
    print(f"[{panel_key}] chair facts re-derived through the law: "
          f"{len(checks)}/{len(checks)} match")

    # --- render + GATE (before anything lands) ---
    svg = GEN.render(m)
    fails = GEN.gate(m, svg)
    if fails:
        for f in fails:
            print("GATE FAIL:", f)
        sys.exit(f"{len(fails)} gate failure(s) on base render — NOTHING WRITTEN")

    # --- inject additive v6 graded labels, then RE-GATE (prove inert) ---
    svg2 = inject_graded(svg, m, p["inject_style"])
    fails2 = GEN.gate(m, svg2)
    if fails2:
        for f in fails2:
            print("GATE FAIL (post-annotation):", f)
        sys.exit(f"{len(fails2)} gate failure(s) after graded annotation — "
                 f"NOTHING WRITTEN")
    # belt-and-braces: every gate-counted class count is preserved by the inject
    for cls in ('z-dot', 'z-label', 'z-line"', 'z-line-label', 'cut-dash',
                'full-stack-badge"', 'full-stack-badge-legend', 'untested-box',
                'untested-bar"', 'key-pointer'):
        if svg.count(f'class="{cls}') != svg2.count(f'class="{cls}'):
            sys.exit(f"annotation altered gated class count for {cls!r} — abort")
    if 'fill-opacity="0.35"' in svg2:
        sys.exit("annotation introduced a raw-dot signature — abort")

    out.write_text(svg2, encoding="utf-8")
    r = subprocess.run(["xmllint", "--noout", str(out)], capture_output=True)
    if r.returncode != 0:
        sys.exit(f"xmllint FAIL: {r.stderr.decode()}")
    print("GATE CLEAN (A-F5) before and after annotation; xmllint OK")
    print("wrote", out)
    print("records preserved:", ", ".join(k.name for k in records),
          "untouched")


if __name__ == "__main__":
    key = sys.argv[1] if len(sys.argv) > 1 else "albatros"
    if key not in PANELS:
        sys.exit(f"unknown panel {key!r}; choose from {sorted(PANELS)}")
    main(key)
