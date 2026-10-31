#!/usr/bin/env python3
"""Findings v4.3 (#60, 2026-07-28) — the census under
(i) GHOST PINNED AT THE WORD (her ruling — token-ghost only; the line-gate
makes no states; LINE-RESIDUAL is annotation, counted separately here) and
(ii) HER-BLESSED ALIGNMENT FILES (corpus/alignments/, chair-verified):
the five formerly-unaligned seats now enter crossings, each source line
crossing the precedence-fold of its MAPPED seat lines; dropped source lines
(seat []) read as absent (the deformation story the mapping itself tells);
translator-added lines with no source anchor are declared, never crossed.
Law: linegrain_law_60 (single source). v4/.1/.2 stay as records. Guarded.

── THIS MODULE HAS TWO ROLES, and only one of them is the v4.3 census.
  1. AS A SCRIPT (main()) it emits findings_v43_linegrain_0728_60.json — a
     SUPERSEDED census. v4.3 was the token-ghost-pinned + blessed-alignments
     era; the census OF RECORD has moved on (v5.0 under the salience
     positive-only trigger, then v5.1 with the fr token-ghost star retired —
     see linegrain_census_v51_62, which drives this same main() and re-labels
     the output). Its findings JSON is deliberately NOT COMMITTED: the file is
     untracked, regenerated on demand, and must not be read as current.
  2. AS A LIBRARY it is LIVE, current, load-bearing code. seat_state_at(),
     fold_states(), row_at(), wording_state(), is_mt() and the re-exported
     BOARDS/alignments() are imported by interesting_gen_61 (the miner's
     fold-aware seat walk), stack_heatmap_61 (which mirrors this walk rather
     than re-deriving semantics) and linegrain_census_v51_62 (which reuses
     main() wholesale). Those functions are NOT superseded by anything; edit
     them as live law-adjacent code, not as an archived census.
The era stamp inside the emitted JSON describes role 1 only."""
import json
import collections
from pathlib import Path

import linegrain_law_60 as LAW

HERE = Path(__file__).resolve().parent
OUT_J = HERE.parent / "reports" / "findings_v43_linegrain_0728_60.json"

# BOARDS, RANK and alignments() moved to their canonical home in the LAW module
# (#71 refactor, 2026-08-12) and are RE-EXPORTED here under exactly their old
# names, so `C.BOARDS` / `C.alignments()` and this file's own fold_states() keep
# working unchanged. The two moved constants were verified byte-identical to the
# law's before the move; the law's alignments() was diffed against the local one
# (same glob root, same keys, same records — it only adds a memo, and no caller
# mutates the result).
BOARDS = LAW.BOARDS
RANK = LAW.RANK
alignments = LAW.alignments


def is_mt(rid):
    return "google" in rid or ":mt_" in rid


def row_at(perseat, rid, li):
    rows = perseat.get(rid)
    if rows and li < len(rows):
        return rows[li]
    return {}


def seat_state_at(field, d, l, rid, li, cut, lc):
    row = d["scalar_readings"][rid][li]
    nb = len(d["scalar_readings"][rid])
    boolrow = (d["booleans"].get(rid) or [{}] * nb)[li] \
        if d["booleans"].get(rid) else {}
    writrow = (l["written_row"].get(rid) or [{}] * nb)[li] \
        if l["written_row"].get(rid) else {}
    return LAW.line_state(field, boolrow, writrow, l, rid, li, cut, row, lc)


def fold_states(states):
    """Precedence fold across the seat lines rendering ONE source line."""
    if not states:
        return "silent", True   # dropped line: nothing rendered -> absent
    best = max(states, key=lambda s: RANK[s[0]])
    starred = any(s[1] for s in states)
    return best[0], starred


def wording_state(field, boolrow, row, cut):
    receipts, wstate = LAW.chan_word(field, boolrow)
    if wstate == "stated":
        return "stated"
    if wstate == "silent":
        return "silent"
    if LAW.triggered_tokens(row, field, cut):
        return "present*"
    return "silent*"


class _Tally:
    """The census's running counters in one bag, so the per-crossing work can be
    lifted out of main() without a twelve-argument signature. Attribute names
    mirror the original local variable names one-for-one, and nothing about the
    emitted structure changes — this is a container, not a semantic."""

    def __init__(self):
        self.census = collections.Counter()
        self.census_starred = collections.Counter()
        self.per_board = collections.defaultdict(collections.Counter)
        self.per_field = collections.defaultdict(collections.Counter)
        self.seatclass = {"human": collections.Counter(),
                          "MT": collections.Counter()}
        self.unheard_by_seat = collections.Counter()
        self.wonly = collections.Counter()
        self.changes = collections.Counter()
        self.residuals = []
        self.additions = []
        self.declared = []
        self.aligned_via_file = []
        self.n = 0


def _crossing_cells(field, d, l, src, li, srow, sbool, rid, seat_lis,
                    readings, bools, cut, lc):
    """ONE source-line × seat crossing, as (cell, wcell, starred).

    cell = the full-stack verdict (every channel), wcell = the WORDING-ONLY
    verdict, starred = either side carried a borrowed-cut two-state. Returns
    None when both verdicts read absent→absent (nothing to score). Pure: it
    reads the committed rows and touches no counter."""
    swrit = row_at(l.get("written_row") or {}, src, li)
    sst, _v, stwo = LAW.line_state(field, sbool, swrit, l,
                                   src, li, cut, srow, lc)
    parts = [seat_state_at(field, d, l, rid, j, cut, lc)[:3:2]
             for j in seat_lis]
    parts = [(p[0], p[1]) for p in parts]
    tst, ttwo = fold_states(parts)
    a, b = LAW.to3(sst), LAW.to3(tst)
    wa = LAW.to3(wording_state(field, sbool, srow, cut))
    wparts = []
    for j in seat_lis:
        trow = readings[rid][j]
        tbool = row_at(bools, rid, j)
        wparts.append((wording_state(field, tbool, trow, cut),
                       False))
    wt, _ws = fold_states(wparts)
    wb = LAW.to3(wt)
    cell = None if (a, b) == ("absent", "absent") \
        else LAW.CELL15[(a, b)]
    wcell = None if (wa, wb) == ("absent", "absent") \
        else LAW.CELL15[(wa, wb)]
    if cell is None and wcell is None:
        return None
    return cell, wcell, (stwo or ttwo)


def _record_crossing(t, board, rid, field, cell, wcell, starred):
    """Post one scored crossing into the tallies."""
    t.n += 1
    if cell:
        (t.census_starred if starred else t.census)[cell] += 1
        t.per_board[board][cell] += 1
        t.per_field[field][cell] += 1
        t.seatclass["MT" if is_mt(rid) else "human"][cell] += 1
        if cell == "UNHEARD":
            t.unheard_by_seat[f"{board}/{rid}"] += 1
    if wcell:
        t.wonly[wcell] += 1
    if wcell != cell:
        t.changes[(wcell or "(silent)", cell or "(silent)")] += 1


def _record_device(t, board, rid, sbool, bools, seat_lis):
    """The sound_device crossing — a PARALLEL LINE ORGAN by law, so it is
    counted per source line beside the field crossings, never inside them.
    Scored only when BOTH sides are covered and at least one fires."""
    sdev_r, sdev = LAW.chan_device(sbool)
    tdev = False
    covered = sdev_r is not None
    for j in seat_lis:
        tb = row_at(bools, rid, j)
        r_, f_ = LAW.chan_device(tb)
        covered = covered and (r_ is not None)
        tdev = tdev or f_
    if covered and (sdev or tdev):
        a, b = ("active" if sdev else "absent",
                "active" if tdev else "absent")
        cell = LAW.CELL15[(a, b)]
        t.n += 1
        t.census[cell] += 1
        t.per_board[board][cell] += 1
        t.per_field["sound_device"][cell] += 1
        t.seatclass["MT" if is_mt(rid) else "human"][cell] += 1
        t.wonly[cell] += 1


def _record_translator_additions(t, board, rid, amap, bools, fd):
    """Translator-added lines (unmapped seat lines): DECLARED, never crossed —
    they have no source anchor to cross against."""
    for u in amap.get("seat_lines_unmapped", []):
        j = u["seat"] - 1
        fires = []
        tb = row_at(bools, rid, j)
        for field in fd:
            rec, ws = LAW.chan_word(field, tb)
            if ws == "stated":
                fires.append(f"{field}:{','.join(rec)}")
        t.additions.append(dict(board=board, seat=rid,
                                seat_line=u["seat"],
                                note=u.get("note", "")[:80],
                                field_fires=fires))


def _record_line_residuals(t, board, readings, cuts):
    """LINE-RESIDUAL annotations — ALL zh-side rows, sources and seats (the
    three 07-28 specimens were zh SEATS humming, not sources). Annotation only:
    never a state, never a crossing, counted separately."""
    for rid, rr in readings.items():
        for li, row in enumerate(rr):
            for field in ("color", "sound", "plant"):
                cut, _t, lc = cuts.get(field, (None, "", None))
                v = LAW.line_residual(field, rid, row, cut)
                if v is not None:
                    t.residuals.append(dict(board=board, rid=rid,
                                            line=li + 1, field=field,
                                            reading=v))


def _summary(t):
    """The findings record. Key order here IS the emitted JSON's key order."""
    human_u = sum(v for k, v in t.unheard_by_seat.items()
                  if not is_mt(k.split("/", 1)[1]))
    mt_u = sum(v for k, v in t.unheard_by_seat.items()
               if is_mt(k.split("/", 1)[1]))
    return {
        "what": "findings v4.3 — token-ghost only (her pin) + PI-approved alignments",
        "date": "2026-07-28", "chair": "#60",
        "law": "linegrain_law_60 @ ghost-pinned-at-word; alignment files "
               "corpus/alignments/ (chair-verified, PI-approved)",
        "supersedes": "findings_v42 (line-gate era), v41, v4",
        "totals_full_stack": dict(t.census.most_common()),
        "totals_suggestive_starred": dict(t.census_starred.most_common()),
        "comparisons_scored": t.n,
        "wording_only_census": dict(t.wonly.most_common()),
        "changed_verdicts_total": sum(t.changes.values()),
        "change_matrix": {f"{w} → {c}": x for (w, c), x
                          in sorted(t.changes.items(), key=lambda kv: -kv[1])},
        "per_board": {b: dict(c.most_common()) for b, c in t.per_board.items()},
        "per_field": {f: dict(c.most_common()) for f, c in t.per_field.items()},
        "seat_class": {k: dict(v.most_common()) for k, v in t.seatclass.items()},
        "unheard": {"human_total": human_u, "mt_total": mt_u,
                    "by_seat_top": dict(t.unheard_by_seat.most_common(12))},
        "aligned_via_file": t.aligned_via_file,
        "line_residual_registry": t.residuals,
        "translator_additions_declared": t.additions,
        "declared": t.declared,
    }


def _print_report(t, out):
    print("=== FINDINGS v4.3 — token-ghost only + alignments ===")
    print("comparisons:", t.n, "| aligned via file:", t.aligned_via_file)
    print("full-stack:", dict(t.census.most_common()))
    print("starred:", dict(t.census_starred.most_common()))
    print("UNHEARD human", out["unheard"]["human_total"],
          "MT", out["unheard"]["mt_total"])
    print("line-residual registry:", t.residuals)
    print("translator additions:", len(t.additions),
          [f"{a['board']}/{a['seat']} L{a['seat_line']}" for a in t.additions])
    print("wrote", OUT_J)


def main():
    cuts = LAW.cuts()
    align = alignments()
    t = _Tally()
    for board in BOARDS:
        d, l, _ = LAW.load_board(board)
        readings = d["scalar_readings"]
        src = next(r for r in readings if r.startswith(d["source_lang"] + ":"))
        nsrc = len(readings[src])
        trans = d.get("transitions") or {}
        bools = d.get("booleans") or {}
        for rid in sorted(readings):
            if rid == src:
                continue
            amap = align.get((board, rid))
            if len(readings[rid]) != nsrc and amap is None:
                t.declared.append(f"{board}/{rid}: unaligned, no file — status")
                continue
            if amap is not None:
                t.aligned_via_file.append(f"{board}/{rid}")
            fd = (trans.get(rid) or {}).get("fields_domain")
            if fd is None:
                fd = [f for f in LAW.HUE]
            cross_device = "sound_device" not in fd
            # per source line: seat side = identity (equal counts) or the map
            for li in range(nsrc):
                srow = readings[src][li]
                sbool = row_at(bools, src, li)
                if amap is None:
                    seat_lis = [li]
                else:
                    entry = amap["map"][li]
                    assert entry["src"] == li + 1
                    seat_lis = [j - 1 for j in entry["seat"]]
                for field in fd:
                    cut, _t, lc = cuts.get(field, (None, "", None))
                    scored = _crossing_cells(field, d, l, src, li, srow, sbool,
                                             rid, seat_lis, readings, bools,
                                             cut, lc)
                    if scored is None:
                        continue
                    _record_crossing(t, board, rid, field, *scored)
                if cross_device:
                    _record_device(t, board, rid, sbool, bools, seat_lis)
            # translator additions (unmapped seat lines): declared, not crossed
            if amap is not None:
                _record_translator_additions(t, board, rid, amap, bools, fd)
        _record_line_residuals(t, board, readings, cuts)

    out = _summary(t)
    OUT_J.write_text(json.dumps(out, ensure_ascii=False, indent=1),
                     encoding="utf-8")
    _print_report(t, out)


if __name__ == "__main__":
    main()
