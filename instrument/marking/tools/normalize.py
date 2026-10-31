#!/usr/bin/env python3
"""Normalization step for field,value marks (marking_pack_v2 §normalization).

Absorbs marker-side format variation and applies the synonym maps, producing
canonical compact mark files (agreement.py's input format) plus a published
normalization log. Original strings are never discarded: every applied merge
is logged, and the log carries a per-field value inventory to support building
the value map from human marks only, before machine marks are unblinded.

Accepted input formats (mixed freely, per pack: "format police do not exist"):
  compact   L1: field, value; field, value; bare_field
  sheet     POEM:/MARKER: headers, then
                L1 <line text>            (or U1 for whole-poem units)
                marks: field, value; ...  (may continue on following lines)
Full-width punctuation (：；，) is folded to ASCII before parsing.

Map files, one entry per line, `#` comments:
  fields    alias -> canonical                     (synonyms_pilot.txt format)
  values    value -> canonical                      global value merge
            field.value -> canonical                scoped to a canonical field
Scalar bucketing lives in the value map too (e.g. `water.riverbank -> medium`);
buckets are small/medium/large by convention (pack rule 3) but the tool does
not invent entries — when in doubt, don't merge, so unmapped values pass
through lower-cased and unchanged.

Usage:
  normalize.py <marks_or_sheet>... --fields <map> [--values <map>] -o <outdir>
Writes <stem>_norm.txt per input and normalization_log.md in <outdir>.

Raw-vs-normalized agreement (spec step 3) is two runs of the untouched
instrument: `agreement.py rawA rawB` vs `agreement.py A_norm B_norm`.
"""
import re
import sys
from pathlib import Path

FULLWIDTH = str.maketrans({"：": ":", "；": ";", "，": ",", "·": ";", "•": ";"})
UNIT_PREFIXES = ("L", "U")


def load_map(path):
    m = {}
    for ln in Path(path).read_text(encoding="utf-8").splitlines():
        ln = ln.split("#")[0].strip()
        if "->" in ln:
            a, c = [s.strip().lower() for s in ln.split("->")]
            m[a] = c
    return m


def is_unit_header(tok):
    return (
        len(tok) > 1 and tok[0] in UNIT_PREFIXES and tok[1:].isdigit()
    )


def parse_pairs(text):
    """`field, value; field` → [(field, value_or_None), ...], raw strings.
    Machine-format absorption (round 2026-07-16, format police still do
    not exist): backticks stripped (`color, green`); a TRAILING
    parenthesized group is dropped only when purely CJK — that's the
    character-attribution idiom (`material, jade` (玉)); human values
    legitimately contain ASCII parens and are untouched."""
    pairs = []
    for chunk in text.split(";"):
        chunk = chunk.replace("`", "").strip()
        chunk = re.sub(r"\s*[(（][㐀-鿿𠀀-𪛟]+[)）]$", "", chunk)
        if not chunk:
            continue
        parts = [p.strip().rstrip(".").strip() for p in chunk.split(",", 1)]
        pairs.append((parts[0], parts[1] if len(parts) > 1 and parts[1] else None))
    return pairs


def parse_file(path):
    """→ (ordered {unit: [(field, value), ...]}, [warnings]). Absorbs both formats."""
    units, warnings = {}, []
    current = None          # unit whose `marks:` continuation lines we're in
    collecting = False
    for raw in Path(path).read_text(encoding="utf-8").splitlines():
        ln = raw.translate(FULLWIDTH).strip()
        if not ln or ln.startswith("#"):
            continue
        head = ln.split(":", 1)[0].strip()
        first_tok = ln.split(None, 1)[0].rstrip(":")
        if ln.upper().startswith(("POEM:", "MARKER:")):
            current, collecting = None, False
            continue
        if is_unit_header(head) and ":" in ln:      # compact: L1: pairs
            unit = head.upper()
            units.setdefault(unit, []).extend(parse_pairs(ln.split(":", 1)[1]))
            current, collecting = unit, False
            continue
        if is_unit_header(first_tok):               # sheet: L1 <line text>
            current, collecting = first_tok.upper(), False
            units.setdefault(current, [])
            continue
        if ln.lower().startswith("marks:"):
            if current is None:
                warnings.append(f"{path.name}: 'marks:' outside any unit: {raw!r}")
                continue
            units[current].extend(parse_pairs(ln.split(":", 1)[1]))
            collecting = True
            continue
        if collecting and current is not None:      # marks continuation line
            units[current].extend(parse_pairs(ln))
            continue
        warnings.append(f"{path.name}: unparsed line: {raw!r}")
    return units, warnings


def normalize_units(units, fmap, vmap, merges):
    """Apply maps; record every changed string in `merges` (original kept)."""
    out = {}
    for unit, pairs in units.items():
        norm_pairs = []
        for f_raw, v_raw in pairs:
            f = f_raw.strip().lower()
            fc = fmap.get(f, f)
            if fc != f_raw.strip():
                merges["field"][(f_raw.strip(), fc)] = merges["field"].get((f_raw.strip(), fc), 0) + 1
            v = None
            if v_raw is not None:
                v = v_raw.strip().lower()
                vc = vmap.get(f"{fc}.{v}", vmap.get(v, v))
                if vc != v_raw.strip():
                    merges["value"][(f_raw.strip(), v_raw.strip(), vc)] = (
                        merges["value"].get((f_raw.strip(), v_raw.strip(), vc), 0) + 1
                    )
                v = vc
            norm_pairs.append((fc, v))
        out[unit] = norm_pairs
    return out


def dump_compact(units, path):
    def key(u):
        return (u[0], int(u[1:]))
    with path.open("w", encoding="utf-8") as fh:
        for unit in sorted(units, key=key):
            body = "; ".join(f"{f}, {v}" if v else f for f, v in units[unit])
            fh.write(f"{unit}: {body}\n")


def write_log(path, sources, merges, inventory, warnings):
    L = ["# Normalization log (auto-generated by normalize.py)", ""]
    L.append("Inputs: " + ", ".join(s.name for s in sources))
    L.append("")
    L.append("## Field merges applied (original -> canonical, count)")
    rows = sorted(merges["field"].items())
    L += [f"- `{a}` -> `{c}` ×{n}" for (a, c), n in rows] or ["- none"]
    L.append("")
    L.append("## Value merges applied (field: original -> canonical, count)")
    rows = sorted(merges["value"].items())
    L += [f"- {f}: `{a}` -> `{c}` ×{n}" for (f, a, c), n in rows] or ["- none"]
    L.append("")
    L.append("## Value inventory per canonical field (for map-building; humans only)")
    for f in sorted(inventory):
        vals = sorted(v for v in inventory[f] if v)
        L.append(f"- **{f}**: {', '.join(vals) if vals else '(bare field only)'}")
    L.append("")
    L.append("## Warnings")
    L += [f"- {w}" for w in warnings] or ["- none"]
    path.write_text("\n".join(L) + "\n", encoding="utf-8")


def main(argv):
    inputs, fpath, vpath, outdir = [], None, None, None
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--fields":
            i += 1; fpath = argv[i]
        elif a == "--values":
            i += 1; vpath = argv[i]
        elif a in ("-o", "--out"):
            i += 1; outdir = argv[i]
        else:
            inputs.append(Path(a))
        i += 1
    if not inputs or not fpath or not outdir:
        print(__doc__); sys.exit(2)
    fmap = load_map(fpath)
    vmap = load_map(vpath) if vpath else {}
    outdir = Path(outdir); outdir.mkdir(parents=True, exist_ok=True)
    merges = {"field": {}, "value": {}}
    inventory, warnings = {}, []
    for src in inputs:
        units, warns = parse_file(src)
        warnings += warns
        norm = normalize_units(units, fmap, vmap, merges)
        for pairs in norm.values():
            for f, v in pairs:
                inventory.setdefault(f, set()).add(v)
        dump_compact(norm, outdir / f"{src.stem}_norm.txt")
    write_log(outdir / "normalization_log.md", inputs, merges, inventory, warnings)
    print(f"wrote {len(inputs)} normalized file(s) + normalization_log.md to {outdir}")
    for w in warnings:
        print("WARN:", w, file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1:])
