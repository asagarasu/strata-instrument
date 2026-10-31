#!/usr/bin/env python3
"""Rubric comparator — §6 scoring doctrine as code (#47, 07-15).

Implements the frozen asymmetric categories — ALL FIFTEEN of record, the
code's own TRANSITIONS table below (four source states × four translation
states, less absent→absent, which is not a transition):
  active→active   SURVIVAL
  active→latent   PARTIAL-LOSS (requires translation latent file; else
                   folded into loss with the fold DECLARED in output)
  active→ghost    ECHO       (seat doesn't say it; its line still sounds)
  active→nothing  DEFORMATION
  latent→active   REVIVAL   (never penalized; requires source latent file)
  latent→latent   LATENT-CARRY (informational; latent-stays-latent = survived)
  latent→ghost    LATENT-ECHO (mech; informational)
  latent→nothing  LATENT-UNREALIZED (informational, no penalty)
  ghost→active    RENDERED   (her verb: a rendering renders the ghost)
  ghost→latent    GHOST-GROUNDED (mech; seat found a citable carrier)
  ghost→ghost     GHOST-CARRY (both lines hum, neither can cite)
  ghost→nothing   UNHEARD    (that reader didn't render it)
  nothing→active  INVENTION (a finding about the translator, not a fault)
  nothing→latent  LATENT-INVENTION (informational)
  nothing→ghost   STIRRED    (mech; nothing in source, seat's line hums)
DOCTRINE-DRIFT RECORD, closed twice. (1) This prose once named FIVE while the
code carried EIGHT — closed 2026-07-26 (#59) at her ruling, by aligning the
docstring to the code's table. (2) The SAME NIGHT the GHOST row/column was
adopted (#59 — her wording and the citation live on TRANSITIONS below), taking
the table from 8 cells to 15, and this header was not re-aligned: it drifted
again, to "ALL EIGHT". Re-aligned 2026-08-12 (#71) to the 15 the code carries.
The rule this keeps proving: TRANSITIONS is the record, and a prose count that
disagrees with it is the bug, not the other way round.
plus the grain hypothesis's value comparison: a SPECIFICITY LADDER
(same / more-specific / less-specific / unclassified) via WordNet
hypernym ancestry (en values only in v1; zh ladder = future, needs
the taxonomy acquisitions).

v1 GRAIN OF COMPARISON: poem-level trait inventories (alignment-free,
conservative). Line-level comparison awaits an alignment file — never
guessed.

⚠ VALIDATION-ONCE LAW: this tool must NOT be pointed at frozen
validation pairs (Waley/Pound/Obata rows of the corpus manifest)
until the demonstration run is deliberately convened. Fixture use
and dev-side use only until then. (--selftest runs synthetic pairs.)

Inputs: marks files in the house compact format (L1: field, value; …)
— human marks (normalize.py output) or machine labels: any file in the
same format, e.g. trait_labelers.label_unit receipts written out per
unit. (#71: this line previously named `trait_labelers.label_marks_file`,
an entry point that does not exist in that module — corrected, not added.)
"""
import sys, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

def load_marks(path_or_lines):
    """poem-level: field -> set(values); unit info kept for counts."""
    inv = {}
    lines = path_or_lines if isinstance(path_or_lines, list) \
        else open(path_or_lines, encoding="utf-8").read().splitlines()
    for ln in lines:
        g = re.match(r"^([LU]\d+)\s*:\s*(.*)$", ln.strip())
        if not g:
            continue
        for pair in g.group(2).split(";"):
            pair = pair.strip()
            if not pair:
                continue
            parts = [p.strip() for p in pair.split(",", 1)]
            f = parts[0].lower()
            v = parts[1].lower() if len(parts) > 1 and parts[1] else None
            if f:
                inv.setdefault(f, set())
                if v:
                    inv[f].add(v)
    return inv

# --- WordNet hypernym ancestry for the specificity ladder (en) ---
_HYPER = None
def hypernyms():
    global _HYPER
    if _HYPER is None:
        _HYPER = {"parents": {}, "words": {}}
        dat = HERE / "vectors/wordnet30/data.noun"
        if dat.exists():
            for ln in open(dat, encoding="utf-8", errors="ignore"):
                if not ln[:1].isdigit():
                    continue
                p = ln.split()
                off, w_cnt = p[0], int(p[3], 16)
                ws = [p[4 + 2*i].lower() for i in range(w_cnt)]
                for w in ws:
                    _HYPER["words"].setdefault(w, []).append(off)
                ptrs = ln.split("|")[0].split()
                for i, t in enumerate(ptrs):
                    if t == "@":
                        _HYPER["parents"].setdefault(off, []).append(ptrs[i+1])
    return _HYPER

def ancestors(off, seen=None):
    seen = seen or set()
    for p in hypernyms()["parents"].get(off, []):
        if p not in seen:
            seen.add(p)
            ancestors(p, seen)
    return seen

def specificity(src_val, tr_val):
    """same / more-specific (tr below src) / less-specific / unclassified."""
    if src_val == tr_val:
        return "same"
    H = hypernyms()["words"]
    so, to = H.get(src_val, []), H.get(tr_val, [])
    if not so or not to:
        return "unclassified"
    s_anc = set().union(*(ancestors(o) for o in so)) | set(so)
    t_anc = set().union(*(ancestors(o) for o in to)) | set(to)
    if set(so) & t_anc:
        return "more-specific"     # source concept is ancestor of translation's
    if set(to) & s_anc:
        return "less-specific"
    return "unclassified"

TRANSITIONS = {
    # (src_state, tr_state) -> category. Full table (#50a, 07-19,
    # review F5 fix; GHOST state adopted 07-26 #59 at her word:
    # "we mark as ghost what the meter attests and no citation grounds —
    # 弦外之音 in the classical vocabulary, the ignition of an aesthetic
    # idea in the Kantian one." Precedence active > latent > ghost > absent.
    # Cells marked (mech) carry mechanical names until data surfaces them
    # and she renames).
    ("active", "active"): "SURVIVAL",
    ("active", "latent"): "PARTIAL-LOSS",
    ("active", "ghost"): "ECHO",                  # seat doesn't say it; its line still sounds
    ("active", "absent"): "DEFORMATION",
    ("latent", "active"): "REVIVAL",
    ("latent", "latent"): "LATENT-CARRY",        # informational
    ("latent", "ghost"): "LATENT-ECHO",          # (mech) informational
    ("latent", "absent"): "LATENT-UNREALIZED",   # informational, no penalty
    ("ghost", "active"): "RENDERED",             # her verb: a rendering renders the ghost
    ("ghost", "latent"): "GHOST-GROUNDED",       # (mech) seat found a citable carrier
    ("ghost", "ghost"): "GHOST-CARRY",           # both lines hum, neither can cite
    ("ghost", "absent"): "UNHEARD",              # that reader didn't render it
    ("absent", "active"): "INVENTION",
    ("absent", "latent"): "LATENT-INVENTION",    # informational
    ("absent", "ghost"): "STIRRED",              # (mech) nothing in source; seat's line hums
}

def compare(src, tr, src_latent=None, tr_latent=None, src_ghost=None, tr_ghost=None):
    fold_declared = (src_latent is None) or (tr_latent is None)
    src_latent = src_latent or {}
    tr_latent = tr_latent or {}
    src_ghost = src_ghost or {}
    tr_ghost = tr_ghost or {}
    rows, ladder = [], []
    def state(f, active, latent, ghost):
        if f in active:
            return "active"
        if f in latent:
            return "latent"
        return "ghost" if f in ghost else "absent"
    for f in sorted(set(src) | set(tr) | set(src_latent) | set(tr_latent)
                    | set(src_ghost) | set(tr_ghost)):
        s_state = state(f, src, src_latent, src_ghost)
        t_state = state(f, tr, tr_latent, tr_ghost)
        if (s_state, t_state) == ("absent", "absent"):
            continue
        cat = TRANSITIONS[(s_state, t_state)]
        if cat == "SURVIVAL":
            for sv in sorted(src[f]):
                best = None
                for tv in sorted(tr[f]):
                    r = specificity(sv, tv)
                    if best is None or (r != "unclassified" and best[1] == "unclassified"):
                        best = (tv, r)
                if best and src[f] and tr[f]:
                    ladder.append((f, sv, best[0], best[1]))
        rows.append((f, cat))
    if fold_declared:
        rows.append(("_meta", "FOLD-DECLARED: latent file(s) absent — "
                     "latent-involving categories folded conservatively"))
    return rows, ladder

def report(rows, ladder, note=""):
    from collections import Counter
    c = Counter(cat for _, cat in rows)
    print(f"| category | n | fields |")
    print(f"|---|---|---|")
    # ALL cells print (her rulings 07-26: the 8-cell mystery closed, then the
    # GHOST row/column adopted the same night)
    for cat in ["SURVIVAL", "PARTIAL-LOSS", "ECHO", "DEFORMATION",
                "REVIVAL", "LATENT-CARRY", "LATENT-ECHO", "LATENT-UNREALIZED",
                "RENDERED", "GHOST-GROUNDED", "GHOST-CARRY", "UNHEARD",
                "INVENTION", "LATENT-INVENTION", "STIRRED"]:
        fs = [f for f, k in rows if k == cat]
        print(f"| {cat} | {len(fs)} | {' '.join(fs) or '-'} |")
    if ladder:
        print("\nvalue ladder (grain hypothesis):")
        for f, sv, tv, r in ladder:
            print(f"  {f}: {sv} → {tv}  [{r}]")
    if note:
        print(f"\nNOTE: {note}")

def selftest():
    """Synthetic pair with KNOWN deformations — the comparator must
    report exactly these, nothing else."""
    src = load_marks(["L1: color, gold; plant, willow",
                      "L2: temporal, autumn; sound, repetition",
                      "L3: animal, bird"])
    # synthetic translation: color survives w/ value generalized
    # (gold→yellow is NOT ancestor-related; willow→tree IS less-specific);
    # temporal DEFORMED away; sound survives; animal survives;
    # weather INVENTED; 'water' revived from source latent.
    tr = load_marks(["L1: color, yellow; plant, tree",
                     "L2: sound, repetition",
                     "L3: animal, bird; weather, storm; water, river"])
    src_latent = {"water": {"river"}}
    rows, ladder = compare(src, tr, src_latent=src_latent)
    d = dict(rows)
    assert d["temporal"] == "DEFORMATION", d
    assert d["weather"] == "INVENTION", d
    assert d["water"] == "REVIVAL", d
    assert d["color"] == "SURVIVAL" and d["plant"] == "SURVIVAL", d
    lad = {(f, sv, tv): r for f, sv, tv, r in ladder}
    assert lad[("plant", "willow", "tree")] == "less-specific", lad
    assert lad[("animal", "bird", "bird")] == "same", lad
    report(rows, ladder, note="selftest synthetic pair — all assertions passed")
    print("\nSELFTEST OK")

if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    else:
        a = [x for x in sys.argv[1:] if not x.startswith("--")]
        rows, ladder = compare(load_marks(a[0]), load_marks(a[1]))
        report(rows, ladder, note="poem-level inventories; latent layers not supplied "
               "— REVIVAL/PARTIAL-LOSS unavailable, folded per header")
