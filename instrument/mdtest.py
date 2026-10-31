#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
STRATA matched-distance pilot (gc#107, 2026-10-30).

Reuses the repo's committed machinery VERBATIM:
  score_descriptive_fields (D): load_axes, maskable_units, delete_unit,
                                embed_inventory (batch_size=1 + seed-48 re-order
                                certificate), project, boolean_states
  linegrain_law_60 (LAW):       cuts, triggered_tokens, line_state, CELL15, to3,
                                news_norms (z currency)
Encoder: LaBSE snapshot fetched 2026-10-30 (sentence-transformers/LaBSE, main),
device=cpu, batch_size=1 (house law).

DESIGN
  For each BASE line (a committed corpus line whose colour word fires the colour
  meter under the registered cut), build one-word SUBSTITUTIONS of the colour
  carrier from three pools:
    target    = another colour word (shifts the colour value)
    related   = an illumination word (shifts brightness instead)
    unrelated = a non-element adjective (shifts nothing typed)
  Measure, for every substituted line:
    cos_line  = LaBSE cosine(base line, substituted line)   [the single number]
    cos_word  = LaBSE cosine(original word, substitute word)
    typed readings on the 5 axes (per-axis whitening + unit norm + projection,
      exactly D.project), their news-normed z shift vs the base, the per-token
      deletion-Δ, the per-field line STATE under the law (word channel + meter;
      latent channels declared not run), and the colour comparator cell with
      the base as source and the substituted line as rendering.
  Cosine matching: per base line, the triple (one per pool) with the smallest
  max pairwise |cos_line| gap; plus pooled analysis in a common cosine band and
  an OLS with cosine as covariate.
"""
import json, re, sys, os, math, itertools
from pathlib import Path
import numpy as np

WORK = Path(__file__).resolve().parent
REPO = WORK                       # instrument/ mirrors the repo layout (publishable/, marking/, engine/, corpus/)
PUB = REPO / "publishable"
DESC = PUB / "deterministic-descriptive-fields"
LAT = PUB / "deterministic-latent-written-fields"
MARK_TOOLS = REPO / "marking" / "tools"
PROTO = REPO / "engine"
LABSE = "sentence-transformers/LaBSE"   # HuggingFace model id (first run downloads it)
OUT = WORK / "results"; OUT.mkdir(exist_ok=True)

for p in (DESC, LAT, MARK_TOOLS, PROTO, PUB):
    sys.path.insert(0, str(p))
import score_descriptive_fields as D          # noqa: E402
import linegrain_law_60 as LAW                # noqa: E402

FIELDS = ["color", "illumination", "sound", "plant", "temporal"]
ANCHOR_TXT = "札札弄机杼。"
ANCHOR_VAL = 0.04199111035800016   # zh sound-axis sentinel (news_norms_z_registration_0728_62.md)

# ───────────────────────────── base lines (committed, non-redacted, colour fires)
# (id, board, rid, line_no, lang, text, carrier token as it appears in maskable_units)
BASES = [
    ("EN1", "sonnet18",        "en:shakespeare_1609", 6,  "en", "And often is his gold complexion dimm'd,", "gold"),
    ("EN2", "tiaotiao",        "en:waley_1918",       3,  "en", "Slender, slender she plies her white fingers.", "white"),
    ("EN3", "qingqing",        "en:giles_1898",       6,  "en", "Her rounded arm is dazzling white;", "white;"),
    ("FR1", "invitation",      "fr:baudelaire_1861",  40, "fr", "Dans une chaude lumière.", "chaude"),
    ("FR2", "albatros",        "fr:baudelaire_1861",  7,  "fr", "Laissent piteusement leurs grandes ailes blanches", "blanches"),
    ("FR3", "correspondances", "fr:baudelaire_1861",  10, "fr", "Doux comme les hautbois, verts comme les prairies,", "verts"),
    ("DE1", "albatros",        "de:george_1901",      7,  "de", "Die grossen weissen flügel traurig hängen", "weissen"),
    ("DE2", "qingqing",        "de:heilmann_1905",    1,  "de", "Grüner Rasen wächst am Ufer.", "Grüner"),
]

# ───────────────────────────── substitution pools (inflected per slot)
POOLS = {
  # English attributive adjectives (no agreement)
  "en": {
    # dropped after the hygiene dry-run: pink/orange/violet (also fire the en PLANT
    # inventory — the house FLAG-class polysemes), pale (xkcd colour term)
    "target":    ["red", "blue", "green", "yellow", "white", "black", "brown", "purple",
                  "grey", "golden", "crimson", "scarlet", "azure", "silver"],
    "related":   ["bright", "dim", "dark", "glowing", "radiant", "shadowy", "gleaming",
                  "luminous", "dusky", "faint", "blazing", "shining", "murky", "brilliant",
                  "gloomy", "sunlit", "dazzling", "shaded", "lit"],
    # dropped: rounded (fires the en sound inventory via WordNet 'round')
    "unrelated": ["gentle", "strange", "distant", "heavy", "soft", "sweet", "lonely", "sacred",
                  "foreign", "humble", "bitter", "wild", "vast", "narrow", "plain", "solemn",
                  "tender", "cruel", "holy", "secret", "proud", "calm", "noble", "weary",
                  "idle", "brave", "slender"],
  },
  # French feminine singular (lumière), feminine plural (ailes), masculine plural (verts comme…)
  "fr_fs": {
    # dropped: argentée (not claimed by the fr inventory), ardente (claimed, but a heat word)
    "target":    ["rouge", "bleue", "verte", "blanche", "noire", "jaune", "grise", "rose", "brune",
                  "pourpre", "dorée", "écarlate", "violette", "blonde"],
    "related":   ["vive", "claire", "pâle", "sombre", "brillante", "éclatante", "obscure", "faible",
                  "radieuse", "luisante", "blafarde", "terne", "éblouissante", "lumineuse",
                  "étincelante", "ténébreuse", "crue", "tamisée"],
    "unrelated": ["douce", "étrange", "lointaine", "lourde", "tendre", "sacrée", "secrète", "pure",
                  "calme", "profonde", "tranquille", "amère", "fière", "vaste", "humble", "sainte",
                  "cruelle", "folle", "légère", "étroite", "simple", "noble", "triste", "grande"],
  },
  "fr_fp": {
    "target":    ["rouges", "bleues", "vertes", "noires", "jaunes", "grises", "roses", "brunes",
                  "pourpres", "dorées", "écarlates", "violettes", "blondes"],
    "related":   ["vives", "claires", "pâles", "sombres", "brillantes", "éclatantes", "obscures",
                  "faibles", "radieuses", "luisantes", "blafardes", "ternes", "éblouissantes",
                  "lumineuses", "étincelantes", "ténébreuses", "crues", "tamisées"],
    "unrelated": ["douces", "étranges", "lointaines", "lourdes", "tendres", "sacrées", "secrètes",
                  "pures", "calmes", "profondes", "tranquilles", "amères", "fières", "vastes",
                  "humbles", "saintes", "cruelles", "folles", "légères", "étroites", "simples",
                  "nobles", "tristes", "grandes"],
  },
  "fr_mp": {
    "target":    ["rouges", "bleus", "blancs", "noirs", "jaunes", "gris", "roses", "bruns",
                  "pourpres", "dorés", "écarlates", "violets", "blonds"],
    "related":   ["vifs", "clairs", "pâles", "sombres", "brillants", "éclatants", "obscurs",
                  "faibles", "radieux", "luisants", "blafards", "ternes", "éblouissants",
                  "lumineux", "étincelants", "ténébreux", "crus", "tamisés"],
    "unrelated": ["doux", "étranges", "lointains", "lourds", "tendres", "sacrés", "secrets", "purs",
                  "calmes", "profonds", "tranquilles", "amers", "fiers", "vastes", "humbles",
                  "saints", "cruels", "fous", "légers", "étroits", "simples", "nobles", "tristes",
                  "grands"],
  },
  # German weak plural after definite article (die grossen …en flügel)
  "de_weak_pl": {
    # dropped: goldenen / rosigen / blonden (not claimed by the de colour inventory)
    "target":    ["roten", "blauen", "grünen", "gelben", "schwarzen", "braunen", "grauen",
                  "violetten", "purpurnen", "silbernen", "scharlachroten"],
    "related":   ["hellen", "dunklen", "blassen", "fahlen", "leuchtenden", "strahlenden",
                  "schimmernden", "glänzenden", "düsteren", "finsteren", "matten", "schattigen",
                  "grellen", "lichten", "glühenden", "funkelnden"],
    "unrelated": ["schweren", "sanften", "fremden", "fernen", "weichen", "süßen", "einsamen",
                  "heiligen", "bitteren", "wilden", "weiten", "engen", "schlichten", "zarten",
                  "grausamen", "geheimen", "stolzen", "ruhigen", "edlen", "müden", "grossen"],
  },
  # German strong masculine nominative, sentence-initial (Grüner Rasen …)
  "de_strong_m": {
    "target":    ["Roter", "Blauer", "Gelber", "Weißer", "Schwarzer", "Brauner", "Grauer",
                  "Purpurner", "Violetter", "Silberner"],
    "related":   ["Heller", "Dunkler", "Blasser", "Fahler", "Leuchtender", "Strahlender",
                  "Schimmernder", "Glänzender", "Düsterer", "Finsterer", "Matter", "Schattiger",
                  "Greller", "Lichter", "Glühender", "Funkelnder"],
    "unrelated": ["Schwerer", "Sanfter", "Fremder", "Ferner", "Weicher", "Süßer", "Einsamer",
                  "Heiliger", "Bitterer", "Wilder", "Weiter", "Enger", "Schlichter", "Zarter",
                  "Grausamer", "Geheimer", "Stolzer", "Ruhiger", "Edler", "Müder"],
  },
}
POOL_OF = {"EN1": "en", "EN2": "en", "EN3": "en", "FR1": "fr_fs", "FR2": "fr_fp", "FR3": "fr_mp",
           "DE1": "de_weak_pl", "DE2": "de_strong_m"}

# cross-lingual demo: fr source vs English candidate renderings (two-pager's own example)
XLING_SRC = ("FR1x", "fr", "Dans une chaude lumière.")
XLING_CANDS = [
    ("faithful",  "In a warm light."),
    ("target",    "In a red light."),
    ("target",    "In a golden light."),
    ("target",    "In a blue light."),
    ("related",   "In a bright light."),
    ("related",   "In a dim light."),
    ("related",   "In a glowing light."),
    ("unrelated", "In a gentle light."),
    ("unrelated", "In a strange light."),
    ("unrelated", "In a distant light."),
    ("insert-colour-noun",  "In a warm hue of light."),
    ("insert-illum-noun",   "In a warm glow of light."),
    ("insert-neutral-noun", "In a warm kind of light."),
]


# ───────────────────────────── helpers
def substitute(text, carrier, sub):
    """Replace the carrier token's alphabetic core, keep attached punctuation and
    initial capital. Exactly one whitespace token must match."""
    units = D.maskable_units(text)
    hits = [u for u in units if u[1] == carrier]
    assert len(hits) == 1, (text, carrier, hits)
    i, tok = hits[0]
    m = re.match(r"^(\W*)(.*?)(\W*)$", tok, flags=re.U)
    pre, core, post = m.group(1), m.group(2), m.group(3)
    if core[:1].isupper() and not sub[:1].isupper():
        sub = sub[:1].upper() + sub[1:]
    new_tok = pre + sub + post
    return text[:i] + new_tok + text[i + len(tok):], new_tok


def committed_row(board, rid, line_no):
    p = DESC / f"descriptive_scores_{board}_59.json"
    d = json.loads(p.read_text())
    for r in d["scalar_readings"][rid]:
        if r["line_no"] == line_no:
            return r
    raise KeyError((board, rid, line_no))


def row_from(E, idx, proj, line):
    """Build a scorer row (reading + full per-token Δ) exactly as D.scalar_readings."""
    reading = {f: float(proj[f][idx[line]]) for f in FIELDS}
    contrib = {}
    for f in FIELDS:
        base = proj[f][idx[line]]
        ds = [(u[1], float(base - proj[f][idx[D.delete_unit(line, u)]])) for u in D.maskable_units(line)]
        contrib[f] = sorted(ds, key=lambda x: -abs(x[1]))
    return {"text": line, "reading": reading, "top_delta": contrib}


def states_for(row, lang, cuts):
    """Per-field line STATE under the law with the latent channels declared NOT
    RUN (writrow=None, lat={}): word channel + meter only."""
    boolrow = D.boolean_states(row["text"], lang)
    out = {}
    for f in FIELDS:
        cut = cuts.get(f, (None,))[0]
        st, via, star = LAW.line_state(f, boolrow, None, {}, f"{lang}:x", 0, cut, row)
        trig = LAW.triggered_tokens(row, f, cut) if cut is not None else []
        out[f] = {"state": st, "via": via, "starred": star,
                  "word_receipts": boolrow[f]["receipts"], "word_fires": boolrow[f]["fires"],
                  "coverage": boolrow[f]["coverage"], "triggered": trig}
    return out


def zshift(row_b, row_c, lang, nn):
    # LAW.news_norms() -> {field: {lang: (mu, sigma)}}
    return {f: (row_c["reading"][f] - row_b["reading"][f]) / nn[f][lang][1] for f in FIELDS}


def cell(src_state, tr_state):
    """The law's 15-cell comparator; absent×absent is not a crossing (the census
    skips it) — reported here as 'none' so the row is still countable."""
    key = (LAW.to3(src_state), LAW.to3(tr_state))
    return LAW.CELL15.get(key, "none(absent×absent)")


def main():
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(str(LABSE), device="cpu")
    axes = D.load_axes()
    cuts = LAW.cuts()
    nn = LAW.news_norms()          # {field: {lang: (mu, sigma)}}
    print("cuts:", {f: round(v[0], 5) for f, v in cuts.items()})

    # ── build the inventory (bases, substitutions, their deletion masks, bare words)
    inv, idx = [], {}
    def add(s):
        if s not in idx:
            idx[s] = len(inv); inv.append(s)
    def add_line(s):
        add(s)
        for u in D.maskable_units(s):
            add(D.delete_unit(s, u))

    cands = []   # (base_id, pool, sub_word, new_tok, line)
    for bid, board, rid, ln, lang, text, carrier in BASES:
        add_line(text)
        core = re.match(r"^\W*(.*?)\W*$", carrier).group(1)
        add(core)
        for pool, words in POOLS[POOL_OF[bid]].items():
            for w in words:
                if w.lower() == core.lower():
                    continue
                line, new_tok = substitute(text, carrier, w)
                add_line(line); add(w)
                cands.append((bid, pool, w, new_tok, line))
    add_line(XLING_SRC[2])
    for pool, line in XLING_CANDS:
        add_line(line)
    add(ANCHOR_TXT)
    print(f"inventory: {len(inv)} unique texts (encoded twice for the certificate)")

    cache = OUT / "emb_cache.npz"
    if cache.exists():
        z = np.load(cache, allow_pickle=True)
        if list(z["inv"]) == inv:
            E, drift = z["E"], float(z["drift"])
            print("embeddings loaded from cache (same inventory)")
        else:
            E, drift = D.embed_inventory(model, inv)
            np.savez(cache, E=E, inv=np.array(inv, dtype=object), drift=drift)
    else:
        E, drift = D.embed_inventory(model, inv)
        np.savez(cache, E=E, inv=np.array(inv, dtype=object), drift=drift)
    print(f"certificate drift (re-order, batch_size=1): {drift:.2e}")
    proj = D.project(E, axes)
    anchor = float(proj["sound"][idx[ANCHOR_TXT]])
    print(f"anchor 札札弄机杼。 sound-axis: {anchor:.17g}  (registered {ANCHOR_VAL:.17g})  |Δ|={abs(anchor-ANCHOR_VAL):.2e}")

    def cos(a, b):
        return float(np.dot(E[idx[a]], E[idx[b]]))

    # ── pipeline check against the committed rows
    check = []
    for bid, board, rid, ln, lang, text, carrier in BASES:
        cm = committed_row(board, rid, ln)
        assert cm["text"] == text, (cm["text"], text)
        mine = row_from(E, idx, proj, text)
        dread = max(abs(mine["reading"][f] - cm["reading"][f]) for f in FIELDS)
        cm_d = {f: dict(cm["top_delta"][f]) for f in FIELDS}
        my_d = {f: dict(mine["top_delta"][f]) for f in FIELDS}
        ddelta = max(abs(my_d[f][t] - cm_d[f][t]) for f in FIELDS for t in my_d[f] if t in cm_d[f])
        check.append({"id": bid, "line": text, "max|Δreading|": dread, "max|ΔtokenΔ|": ddelta,
                      "colour_Δ_carrier_committed": cm_d["color"].get(carrier),
                      "colour_Δ_carrier_mine": my_d["color"].get(carrier)})
    print("\npipeline check vs committed rows (max abs differences):")
    for c in check:
        print(f"  {c['id']}: reading {c['max|Δreading|']:.2e}  tokenΔ {c['max|ΔtokenΔ|']:.2e}  "
              f"carrier colourΔ committed {c['colour_Δ_carrier_committed']:+.5f} mine {c['colour_Δ_carrier_mine']:+.5f}")

    # ── score every base + candidate
    base_rows, base_states = {}, {}
    for bid, board, rid, ln, lang, text, carrier in BASES:
        base_rows[bid] = row_from(E, idx, proj, text)
        base_states[bid] = states_for(base_rows[bid], lang, cuts)

    results = []
    for bid, pool, w, new_tok, line in cands:
        _, board, rid, ln, lang, text, carrier = next(b for b in BASES if b[0] == bid)
        core = re.match(r"^\W*(.*?)\W*$", carrier).group(1)
        row = row_from(E, idx, proj, line)
        st = states_for(row, lang, cuts)
        bst = base_states[bid]
        # pool hygiene: word channel verdict on the substitute
        colour_claims_sub = any(re.sub(r"\W", "", r).lower() in (w.lower(), new_tok.lower())
                                or w.lower().startswith(re.sub(r"\W", "", r).lower()[:4])
                                for r in st["color"]["word_receipts"]) if st["color"]["word_fires"] else False
        res = {
            "base": bid, "lang": lang, "pool": pool, "sub": w, "line": line,
            "cos_line": cos(text, line), "cos_word": cos(core, w),
            "reading": row["reading"], "dz": zshift(base_rows[bid], row, lang, nn),
            "sub_delta": {f: dict(row["top_delta"][f]).get(new_tok) for f in FIELDS},
            "states": {f: st[f]["state"] for f in FIELDS},
            "base_states": {f: bst[f]["state"] for f in FIELDS},
            "cells": {f: cell(bst[f]["state"], st[f]["state"]) for f in FIELDS},
            "colour_word_receipts": st["color"]["word_receipts"],
            "colour_word_fires": st["color"]["word_fires"],
            "colour_triggered": [t for t, _ in st["color"]["triggered"]],
            "illum_triggered": [t for t, _ in st["illumination"]["triggered"]],
            "sub_claimed_as_colour": colour_claims_sub,
            "colour_value_changed": None,
        }
        # value-grain note: both stated → did the claiming colour lemma set change?
        if res["base_states"]["color"] == "stated" and res["states"]["color"] == "stated":
            res["colour_value_changed"] = (set(bst["color"]["word_receipts"]) != set(st["color"]["word_receipts"]))
        results.append(res)

    # ── cross-lingual demo
    xl = []
    src_row = row_from(E, idx, proj, XLING_SRC[2]); src_st = states_for(src_row, "fr", cuts)
    for pool, line in XLING_CANDS:
        row = row_from(E, idx, proj, line); st = states_for(row, "en", cuts)
        xl.append({"pool": pool, "line": line, "cos_to_src": cos(XLING_SRC[2], line),
                   "reading": row["reading"],
                   "z": {f: (row["reading"][f] - nn[f]["en"][0]) / nn[f]["en"][1] for f in FIELDS},
                   "states": {f: st[f]["state"] for f in FIELDS},
                   "cells_vs_src": {f: cell(src_st[f]["state"], st[f]["state"]) for f in FIELDS},
                   "colour_receipts": st["color"]["word_receipts"],
                   "colour_triggered": [t for t, _ in st["color"]["triggered"]],
                   "illum_triggered": [t for t, _ in st["illumination"]["triggered"]]})

    out = {
        "meta": {"encoder": "sentence-transformers/LaBSE (fetched 2026-10-30, main)", "device": "cpu",
                 "batch_size": 1, "certificate_drift": drift, "anchor_sound_axis": anchor,
                 "anchor_registered": ANCHOR_VAL, "n_inventory": len(inv),
                 "cuts": {f: v[0] for f, v in cuts.items()},
                 "latent_channels": "NOT RUN (writrow=None, lat={}) — states come from the word channel (boolean inventories) + the meter (trigger) only",
                 "env": "python3.12 venv: torch 2.8.0+cpu, transformers 4.57.6, sentence-transformers 5.1.2, numpy 2.0.2 (frozen env is py3.9.6 — same package pins)"},
        "pipeline_check": check,
        "bases": [{"id": b[0], "board": b[1], "rid": b[2], "line_no": b[3], "lang": b[4], "text": b[5],
                   "carrier": b[6], "reading": base_rows[b[0]]["reading"],
                   "states": {f: base_states[b[0]][f]["state"] for f in FIELDS},
                   "colour_receipts": base_states[b[0]]["color"]["word_receipts"],
                   "colour_triggered": [t for t, _ in base_states[b[0]]["color"]["triggered"]],
                   "carrier_colour_delta": dict(base_rows[b[0]]["top_delta"]["color"]).get(b[6])} for b in BASES],
        "candidates": results,
        "xling": {"source": XLING_SRC, "source_states": {f: src_st[f]["state"] for f in FIELDS},
                  "source_colour_triggered": [t for t, _ in src_st["color"]["triggered"]], "cands": xl},
    }
    (OUT / "mdtest_results.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    print(f"\nwrote {OUT/'mdtest_results.json'}")
    analyse(out)


# ───────────────────────────── analysis
def analyse(out):
    R = out["candidates"]
    lines = []
    P = lines.append
    P("# Matched-distance pilot — tables\n")
    P(f"certificate drift {out['meta']['certificate_drift']:.2e}; anchor |Δ| {abs(out['meta']['anchor_sound_axis']-out['meta']['anchor_registered']):.2e}; inventory {out['meta']['n_inventory']}\n")

    # pool hygiene
    P("## Pool hygiene (word-channel verdict on each substitute)\n")
    bad = [r for r in R if (r["pool"] != "target" and r["sub_claimed_as_colour"]) or
           (r["pool"] == "target" and not r["sub_claimed_as_colour"])]
    for r in bad:
        P(f"- {r['base']} {r['pool']} «{r['sub']}»: colour word channel {'claims' if r['sub_claimed_as_colour'] else 'does NOT claim'} it (receipts {r['colour_word_receipts']})")
    P(f"\n{len(bad)} pool anomalies of {len(R)} candidates. Analysis below keeps pools AS DESIGNED (type decided by the word list), with these flagged.\n")

    # per-base matched triples
    P("## A. Per base line: the tightest cosine-matched triple\n")
    P("| base | pool | substitute | cos_line | cos_word | colour state base→cand | colour cell | value changed | illum state base→cand | Δz colour | Δz illum | Δz other3 (sum abs) |")
    P("|---|---|---|---|---|---|---|---|---|---|---|---|")
    triples = []
    for b in out["bases"]:
        bid = b["id"]
        byp = {p: [r for r in R if r["base"] == bid and r["pool"] == p] for p in ("target", "related", "unrelated")}
        best = None
        for t in byp["target"]:
            for rl in byp["related"]:
                for u in byp["unrelated"]:
                    cs = [t["cos_line"], rl["cos_line"], u["cos_line"]]
                    gap = max(cs) - min(cs)
                    if best is None or gap < best[0]:
                        best = (gap, t, rl, u)
        gap, t, rl, u = best
        triples.append((bid, gap, t, rl, u))
        for r in (t, rl, u):
            o3 = sum(abs(r["dz"][f]) for f in ("sound", "plant", "temporal"))
            P(f"| {bid} «{b['carrier']}» | {r['pool']} | {r['sub']} | {r['cos_line']:.4f} | {r['cos_word']:.3f} | "
              f"{r['base_states']['color']}→{r['states']['color']} | {r['cells']['color']} | {r['colour_value_changed']} | "
              f"{r['base_states']['illumination']}→{r['states']['illumination']} | {r['dz']['color']:+.2f} | {r['dz']['illumination']:+.2f} | {o3:.2f} |")
        P(f"| | | *max cos gap* | *{gap:.4f}* | | | | | | | | |")
    P("")

    # pooled by pool
    P("## B. Pooled over all candidates, by pool\n")
    P("| pool | n | cos_line mean±sd | cos_word mean±sd | Δz colour median [IQR] | Δz illum median [IQR] | colour slot stays stated | colour cell counts | illum present* gained | sub fires colour meter | sub fires illum meter |")
    P("|---|---|---|---|---|---|---|---|---|---|---|")
    def q(xs, p): return float(np.percentile(xs, p)) if xs else float("nan")
    for pool in ("target", "related", "unrelated"):
        rs = [r for r in R if r["pool"] == pool]
        cl = [r["cos_line"] for r in rs]; cw = [r["cos_word"] for r in rs]
        dzc = [r["dz"]["color"] for r in rs]; dzi = [r["dz"]["illumination"] for r in rs]
        stays = sum(1 for r in rs if r["base_states"]["color"] == "stated" and r["states"]["color"] == "stated")
        nst = sum(1 for r in rs if r["base_states"]["color"] == "stated")
        from collections import Counter
        cc = Counter(r["cells"]["color"] for r in rs)
        ill_gain = sum(1 for r in rs if r["base_states"]["illumination"] != "present*" and r["states"]["illumination"] == "present*")
        ill_base_not = sum(1 for r in rs if r["base_states"]["illumination"] != "present*")
        sub_col = sum(1 for r in rs if r["sub_delta"]["color"] is not None and r["sub_delta"]["color"] >= out["meta"]["cuts"]["color"])
        sub_ill = sum(1 for r in rs if r["sub_delta"]["illumination"] is not None and abs(r["sub_delta"]["illumination"]) >= out["meta"]["cuts"]["illumination"])
        P(f"| {pool} | {len(rs)} | {np.mean(cl):.4f}±{np.std(cl):.4f} | {np.mean(cw):.3f}±{np.std(cw):.3f} | "
          f"{q(dzc,50):+.2f} [{q(dzc,25):+.2f},{q(dzc,75):+.2f}] | {q(dzi,50):+.2f} [{q(dzi,25):+.2f},{q(dzi,75):+.2f}] | "
          f"{stays}/{nst} | {dict(cc)} | {ill_gain}/{ill_base_not} | {sub_col}/{len(rs)} | {sub_ill}/{len(rs)} |")
    P("")

    # common cosine band
    P("## C. Within a common cosine band (matched by construction)\n")
    lo = max(min(r["cos_line"] for r in R if r["pool"] == p) for p in ("target", "related", "unrelated"))
    hi = min(max(r["cos_line"] for r in R if r["pool"] == p) for p in ("target", "related", "unrelated"))
    P(f"band = [{lo:.4f}, {hi:.4f}] (intersection of the three pools' cos_line ranges)\n")
    P("| pool | n in band | cos_line mean | Δz colour median | Δz illum median | colour stays stated | illum present* gained |")
    P("|---|---|---|---|---|---|---|")
    for pool in ("target", "related", "unrelated"):
        rs = [r for r in R if r["pool"] == pool and lo <= r["cos_line"] <= hi]
        if not rs:
            P(f"| {pool} | 0 | | | | | |"); continue
        stays = sum(1 for r in rs if r["base_states"]["color"] == "stated" and r["states"]["color"] == "stated")
        nst = sum(1 for r in rs if r["base_states"]["color"] == "stated")
        ill_gain = sum(1 for r in rs if r["base_states"]["illumination"] != "present*" and r["states"]["illumination"] == "present*")
        ill_base_not = sum(1 for r in rs if r["base_states"]["illumination"] != "present*")
        P(f"| {pool} | {len(rs)} | {np.mean([r['cos_line'] for r in rs]):.4f} | {q([r['dz']['color'] for r in rs],50):+.2f} | "
          f"{q([r['dz']['illumination'] for r in rs],50):+.2f} | {stays}/{nst} | {ill_gain}/{ill_base_not} |")
    P("")

    # OLS: dz_colour ~ cos_line + pool dummies (+ base fixed effects)
    P("## D. OLS with cosine as covariate (base-line fixed effects)\n")
    bases = sorted(set(r["base"] for r in R))
    def design(rs):
        X = []
        for r in rs:
            row = [r["cos_line"], 1.0 if r["pool"] == "related" else 0.0, 1.0 if r["pool"] == "unrelated" else 0.0]
            row += [1.0 if r["base"] == b else 0.0 for b in bases]
            X.append(row)
        return np.array(X)
    X = design(R)
    for dep, lab in (("color", "Δz colour"), ("illumination", "Δz illumination")):
        y = np.array([r["dz"][dep] for r in R])
        beta, *_ = np.linalg.lstsq(X, y, rcond=None)
        resid = y - X @ beta
        n, k = X.shape
        s2 = float(resid @ resid) / (n - k)
        cov = s2 * np.linalg.pinv(X.T @ X)
        se = np.sqrt(np.diag(cov))
        P(f"**{lab}** ~ cos_line + related + unrelated + base FE   (n={n}; reference pool = target)")
        for name, b_, s_ in zip(["cos_line", "related (vs target)", "unrelated (vs target)"], beta[:3], se[:3]):
            P(f"- {name}: β = {b_:+.3f} (se {s_:.3f}, t = {b_/s_:+.1f})")
        P("")
    # Spearman within pool: cos vs |dz colour|
    def spearman(a, b):
        ra = np.argsort(np.argsort(a)); rb = np.argsort(np.argsort(b))
        return float(np.corrcoef(ra, rb)[0, 1])
    P("Spearman ρ(cos_line, Δz colour) within pool (pooled across bases):")
    for pool in ("target", "related", "unrelated"):
        rs = [r for r in R if r["pool"] == pool]
        P(f"- {pool}: ρ = {spearman([r['cos_line'] for r in rs], [r['dz']['color'] for r in rs]):+.2f}")
    P("")

    # Per base summary
    P("## E. Per base line, per pool medians\n")
    P("| base | carrier (colour Δ) | base colour state | pool | n | cos_line median | Δz colour median | Δz illum median | colour stays stated | colour cells |")
    P("|---|---|---|---|---|---|---|---|---|---|")
    from collections import Counter
    for b in out["bases"]:
        for pool in ("target", "related", "unrelated"):
            rs = [r for r in R if r["base"] == b["id"] and r["pool"] == pool]
            stays = sum(1 for r in rs if r["states"]["color"] == "stated")
            cc = Counter(r["cells"]["color"] for r in rs)
            P(f"| {b['id']} | {b['carrier']} ({b['carrier_colour_delta']:+.4f}) | {b['states']['color']} | {pool} | {len(rs)} | "
              f"{q([r['cos_line'] for r in rs],50):.4f} | {q([r['dz']['color'] for r in rs],50):+.2f} | {q([r['dz']['illumination'] for r in rs],50):+.2f} | {stays}/{len(rs)} | {dict(cc)} |")
    P("")

    # cross-lingual
    X = out["xling"]
    P("## F. Cross-lingual demo: fr source «Dans une chaude lumière.» vs English renderings\n")
    P(f"source colour state: {X['source_states']['color']} (meter-triggered: {X['source_colour_triggered']}); source illumination: {X['source_states']['illumination']}\n")
    P("| pool | rendering | cos(fr src, en) | colour state | colour receipts | colour meter tokens | colour cell vs src | illum state | illum meter tokens | z colour | z illum |")
    P("|---|---|---|---|---|---|---|---|---|---|---|")
    for c in X["cands"]:
        P(f"| {c['pool']} | {c['line']} | {c['cos_to_src']:.4f} | {c['states']['color']} | {c['colour_receipts']} | {c['colour_triggered']} | "
          f"{c['cells_vs_src']['color']} | {c['states']['illumination']} | {c['illum_triggered']} | {c['z']['color']:+.2f} | {c['z']['illumination']:+.2f} |")
    P("")
    (OUT / "mdtest_tables.md").write_text("\n".join(lines))
    print("\n".join(lines))

    # stimuli for a human damage rating (the half this pilot cannot supply)
    rows = ["base_id\tbase_line\tpool\tsubstituted_line\tcos_line\tcos_word"]
    for bid, gap, t, rl, u in triples:
        b = next(x for x in out["bases"] if x["id"] == bid)
        for r in (t, rl, u):
            rows.append(f"{bid}\t{b['text']}\t{r['pool']}\t{r['line']}\t{r['cos_line']:.4f}\t{r['cos_word']:.3f}")
    (OUT / "matched_triples_for_rating.tsv").write_text("\n".join(rows))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--analyse":
        analyse(json.loads((OUT / "mdtest_results.json").read_text()))
    else:
        main()
