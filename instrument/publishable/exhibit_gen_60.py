#!/usr/bin/env python3
"""Exhibit generator, rewritten from scratch (#60, 2026-07-28 — her orders:
删了重写 [deleted and rewritten], harness-gated, single-sourced; and, said by her 很多很多遍 [many, many times] and finally
implemented in full: THE DETERMINISTIC COLUMNS ARE THE INVESTIGATION OF THE
TOP-TOK).

Semantics of the row, of record:
  - top-tok — PER-AXIS since F8 (her ruling 07-29, #63; registration
    display_law_F8_toptok_registration_0729_63.md): SALIENCE axes = the max
    POSITIVE contentful token (the strongest admissible mover under the
    v5.0 positive-only trigger); if none exists, the least-negative
    contentful token draws FADED with its signed value (third grammar —
    nearness, never a fire's ink). VALUE axes = the |Δ|-max contentful
    token, sign kept (two-sided by law) — the meter's gaze.
  - the LINE HIGHLIGHT is the top-tok, always; its colour = which channel
    claims that very token (her 07-28 ruling).
  - the three deterministic cascade cells answer, FOR THE TOP-TOK ONLY:
    does the dictionary claim it? does the written channel claim it? does the
    referent channel claim it? Channel fires on OTHER words of the line are
    context, rendered as a pale "(line: …)" footnote inside the cell — they
    never impersonate the top-tok's investigation (attribution never migrates
    in ink — her walk).
  - device stays a PARALLEL LINE ORGAN by law (叠字/alliteration are line
    phenomena; never trigger-gated) — it is not part of the per-word probe.
  - line STATE remains the whole-line law (a stated word anywhere states the
    line); the state pair column carries it, with via in the sidecar.

Three stages, strictly separated: build_model (ALL semantics, single-sourced
from committed JSON via linegrain_law_60) → render (pure layout) → gate
(BEFORE anything lands). Sidecar .model.json = the provenance of every cell.

Gate = her caught bug classes as standing assertions:
  A. cascade cells equal the top-tok's freshly-recomputed claim status
  B. count-mismatched seats are STATUS rows with zero data cells
  C. top-tok is the true |Δ|-max contentful token
  D. displayed units clean; line-context receipts equal committed data
  E. the line highlight IS the top-tok whenever locatable
Guarded main."""
import html
import json
import subprocess
import sys
from pathlib import Path

import linegrain_law_60 as LAW

HERE = Path(__file__).resolve().parent
FIG = HERE.parent / "reports" / "figures" / "samples_59"

# THE READING-KEY figure stem (her "explain those stars and lines and whatever in
# graphs", #62). key_gen_62.py draws reports/figures/{KEY_FIGURE_STEM}.svg; every
# exhibit footer carries one pointer line "key: {KEY_FIGURE_STEM}". One source for
# the name, so a footer pointer can never drift from the figure it names.
KEY_FIGURE_STEM = "KEY_exhibit_reading_guide_0728_62"

POLE = {"temporal": "− = brief-pole / + = long-pole (A7 value axis)",
        "illumination": "− = bright-pole / + = dark-pole (polarity axis)"}

# RANK and alignments() moved to their canonical home in the LAW module (#71
# refactor, 2026-08-12) and are RE-EXPORTED here under exactly their old names,
# so every consumer reading GEN.RANK / GEN.alignments() keeps working unchanged
# (verify_exhibits_60 reads GEN.RANK; the miners reach alignments through the
# census). Values are the same objects the law now single-sources: RANK was
# byte-identical to the census copy, and the law's alignments() IS the memoized
# form this file already used — same glob root, same keys, same records.
RANK = LAW.RANK
alignments = LAW.alignments
_CORPUS = {}
_CORPUS_WARNED = set()


def corpus_line(board, rid, idx):
    """The seat's corpus text for one line, via corpus_breadth_runner_56, cached
    per (board, rid). On ANY failure the seat degrades to "(line unavailable)".

    #71: the fallback behaviour is UNCHANGED, but it is no longer SILENT — the
    exception is now reported on stderr (once per distinct cause) before the
    degrade. The silence was hiding a live one: corpus_breadth_runner_56 imports
    numpy at module scope, so under a numpy-less interpreter EVERY seat lost its
    corpus text and the regenerated exhibits differed from the committed ones in
    exactly those lines, with no signal whatsoever. The except stays BROAD on
    purpose — any breakage in the corpus runner must degrade a text cell, never
    abort a render — it just says so now."""
    key = (board, rid)
    if key not in _CORPUS:
        try:
            import corpus_breadth_runner_56 as R
            seat = next((s for s in R.BOARDS[board]["seats"]
                         if s["rid"] == rid), None)
            _CORPUS[key] = R.parse_seat(seat) if seat else []
        except Exception as e:
            msg = (f"corpus_line: {type(e).__name__}: {e} — corpus text "
                   f"unavailable; seats degrade to '(line unavailable)'")
            if msg not in _CORPUS_WARNED:
                _CORPUS_WARNED.add(msg)
                print(f"WARNING {msg}", file=sys.stderr)
            _CORPUS[key] = []
    lines = _CORPUS[key]
    return lines[idx] if idx < len(lines) else "(line unavailable)"


def _matches(top_tok, w):
    # #61 Stage 2c: shared variant-map claim-match (exact · zh char-fold · map
    # lemma hit) — replaces substring containment, which silently failed fr
    # irregulars (rousse vs roux) and en derivations (rosy vs rose).
    return LAW.variant_match(top_tok, w)


def _claimed_surface(txt, claim_word):
    """The SURFACE token in `txt` that carries `claim_word` — the word-tier
    claim that MADE the seat's state (state_word: a receipt lemma like 'clack',
    a carrier, or a call word). Used by the LINE-WINDOW law (#61, her live
    catch): the claimed word's surface must never be amputated out of the
    rendered seat text. claim_word may be a lemma ('clack') while the surface is
    an inflection ('Clacking'), so we variant-match each raw token against it,
    mirroring the labeler's own fold. Returns the first surface token, or None
    (nothing to protect — the highlight already carries the display)."""
    if not claim_word:
        return None
    for raw in str(txt).split():
        tok = raw.strip(",.;:!?，。；：？！()（）「」『』“”'’…—-")
        if tok and _matches(tok, claim_word):
            return tok
    return None


# ---------------------------------------------------------------- 1. MODEL --

def build_model(board, line_idx, field):
    d, l, umem = LAW.load_board(board)
    readings = d["scalar_readings"]
    src = next(r for r in readings if r.startswith(d["source_lang"] + ":"))
    src_len = len(readings[src])
    cut, tier, line_cut = LAW.cuts().get(
        field, (None, "VALUE axis (duration ρ.860) — no promotion cut", None))
    order = [src] + sorted(r for r in readings if r != src)
    seats = []
    for rid in order:
        rr = readings[rid]
        folded_from = None
        row_idx = line_idx
        if rid != src and len(rr) != src_len:
            amap = alignments().get((board, rid))
            if amap is None:
                seats.append(dict(rid=rid,
                                  mt="google" in rid or ":mt_" in rid,
                                  unaligned=True,
                                  status="unaligned — awaits alignment file; "
                                         "line-number pairing is navigation, "
                                         "not an alignment claim"))
                continue
            entry = amap["map"][line_idx]
            seat_lis = [j - 1 for j in entry["seat"]]
            if not seat_lis:
                seats.append(dict(rid=rid,
                                  mt="google" in rid or ":mt_" in rid,
                                  unaligned=True, dropped=True,
                                  status="(dropped — the translator renders "
                                         "nothing for this source line; "
                                         "PI-approved alignment)"))
                continue
            # carrier line = the state-fold winner across the mapped lines
            cut0, _t0, lc0 = LAW.cuts().get(field, (None, "", None))
            best, best_rank = seat_lis[0], -1
            for j in seat_lis:
                r_j = rr[j]
                b_j = (d["booleans"].get(rid) or [{}] * len(rr))[j] \
                    if d["booleans"].get(rid) else {}
                w_j = (l["written_row"].get(rid) or [{}] * len(rr))[j] \
                    if l["written_row"].get(rid) else {}
                st_j, _v, _tw = LAW.line_state(field, b_j, w_j, l, rid, j,
                                               cut0, r_j, lc0)
                if RANK[st_j] > best_rank:
                    best, best_rank = j, RANK[st_j]
            row_idx = best
            folded_from = [j + 1 for j in seat_lis]
        row = rr[row_idx]
        nrr = len(rr)
        boolrow = (d["booleans"].get(rid) or [{}] * nrr)[row_idx] \
            if d["booleans"].get(rid) else {}
        writrow = (l["written_row"].get(rid) or [{}] * nrr)[row_idx] \
            if l["written_row"].get(rid) else {}
        st, via, two = LAW.line_state(field, boolrow, writrow, l, rid,
                                      row_idx, cut, row, line_cut)
        receipts, wstate = LAW.chan_word(field, boolrow)
        receipts = LAW.mass_rank(receipts, row, field) if receipts else receipts
        carriers, wfired, carrier_words = LAW.chan_written(field, writrow)
        refdisp, rcall, call_words = LAW.chan_referent(field, l, rid, row_idx)
        devrec, dfired = LAW.chan_device(boolrow)
        trigs = LAW.triggered_tokens(row, field, cut)
        tm, tmd = LAW.top_mover(row, field)
        # F8 (her ruling 07-29, #63; registration display_law_F8_...): on
        # SALIENCE axes the top-tok is the max POSITIVE contentful token;
        # if none, the least-negative contentful draws FADED (nearness).
        tt_faded = False
        if field in LAW.SALIENCE_TRIGGER_FIELDS:
            pos, near = None, None
            for t, dd in (row.get("top_delta", {}).get(field) or []):
                ts = LAW._clean(t)
                if dd is None or not ts or not LAW._contentful(ts):
                    continue
                if dd > 0:
                    if pos is None or dd > pos[1]:
                        pos = (ts, dd)
                elif near is None or dd > near[1]:
                    near = (ts, dd)
            if pos is not None:
                tm, tmd = pos
            elif near is not None:
                tm, tmd = near
                tt_faded = True
            else:
                tm, tmd = None, None
        txt = str(row.get("text") or corpus_line(board, rid, row_idx))
        if folded_from and len(folded_from) > 1:
            txt = txt + f" ⟨carrier of {len(folded_from)} folded: " \
                        f"L{'+L'.join(str(j) for j in folded_from)}⟩"
        hw, hcol, hpale = LAW.pick_highlight(txt, field, receipts,
                                             carrier_words, call_words,
                                             trigs, row)
        # F8: on salience axes the highlight follows the per-axis top-tok
        # (pick_highlight's internal top_mover stays law-frozen |Δ|-max)
        if field in LAW.SALIENCE_TRIGGER_FIELDS:
            if tm:
                span = LAW.find_span(txt, tm)
                _trg = any(LAW.fold(ts) == LAW.fold(tm) for ts, _ in trigs)
                hw, hcol, hpale = (span, LAW.TOK_HUE, not _trg) \
                    if span else (None, None, False)
            else:
                hw, hcol, hpale = None, None, False
        # THE INVESTIGATION OF THE TOP-TOK (her design, of record):
        word_claim = next((w for w in receipts if tm and _matches(tm, w)),
                          None)
        written_claims = bool(tm and wfired
                              and any(_matches(tm, w) for w in carrier_words))
        ref_claim = next((disp for disp, w in
                          zip(refdisp or [], (refdisp and call_words) or [])
                          if tm and _matches(tm, w)), None) \
            if refdisp is not None else None
        if refdisp is not None and ref_claim is None and tm:
            ref_claim = next((disp for disp in (refdisp or [])
                              if _matches(tm, disp.split()[0])), None)
        v = row["reading"].get(field)
        col = sorted((x["reading"].get(field) or 0.0) for x in rr)
        rank = sum(1 for x in col if x > (v or 0.0)) + 1
        # NEWS-NORMED z (her ruling, twice; #62, norms 9bc5709) — DISPLAY TIER:
        # lang = rid prefix; z = (v − μ)/σ over Leipzig news (None when v is None
        # or the lang is unnormed: jp / any lang outside {en,zh,de,fr}). μ, σ and
        # the norms source id are carried into the sidecar (readable-facts law).
        lang = rid.split(":", 1)[0]
        z = LAW.z_of(lang, field, v)
        _nn = LAW.news_norms().get(field, {}).get(lang)
        z_mu, z_sigma = (_nn if _nn is not None else (None, None))
        # (B), her ruling: the state carries its DERIVING WORD — the word-level
        # event that made the line state, visible in the state pair display
        if st == "stated" and receipts:
            state_word = LAW._word0(receipts[0])
        elif via == "written" and carrier_words:
            state_word = LAW._word0(carrier_words[0])
        elif via == "referent" and call_words:
            state_word = LAW._word0(call_words[0])
        elif st == "ghost" and trigs:
            state_word = max(trigs, key=lambda t: abs(t[1]))[0]
        elif st == "present*" and tm:
            state_word = tm
        else:
            state_word = None
        seats.append(dict(
            rid=rid, mt="google" in rid or ":mt_" in rid, unaligned=False,
            is_src=(rid == src), text=txt, v=v, rank=rank, n_rank=len(col),
            # FULL-STACK BADGE (her REVERSAL ruling, 07-28 late night, #62): the
            # seat's language has word + written + referent channels ALL running.
            # Single-sourced from LAW.FULL_STACK_LANGS (the badge's ONE fact, also
            # the future full-stack gate); the positive mark that replaces the
            # retired fr deficiency star. lang = rid prefix (e.g. "zh").
            full_stack=(lang in LAW.FULL_STACK_LANGS),
            # NEWS-NORMED z line-scalar (display tier; sidecar = readable facts):
            # z None ⟺ lang unnormed (jp / non-{en,zh,de,fr}) → untested z strip.
            lang=lang, z=z, z_mu=z_mu, z_sigma=z_sigma,
            z_norms_src=LAW.NEWS_NORMS_SRC,
            state=st, via=via, two=two, state_word=state_word,
            folded_from=folded_from, carrier_line=row_idx + 1,
            star=(rid, row_idx + 1, field) in umem,
            top_tok=dict(token=tm, delta=tmd, faded=tt_faded,
                         triggered=bool(
                             cut is not None and tmd is not None
                             and ((tmd >= cut)
                                  if field in LAW.SALIENCE_TRIGGER_FIELDS
                                  else (abs(tmd) >= cut)))),
            investigation=dict(
                word=dict(claims_top=bool(word_claim), receipt=word_claim,
                          line_receipts=receipts,
                          covered=wstate is not None),
                written=dict(claims_top=written_claims,
                             carriers=carriers if carriers is not None else None,
                             line_words=carrier_words,
                             covered=carriers is not None, fired=wfired),
                referent=dict(claims_top=bool(ref_claim), display=ref_claim,
                              line_display=refdisp or [],
                              covered=refdisp is not None, call=rcall),
                device=dict(covered=devrec is not None, fired=dfired,
                            receipts=devrec or [])),
            line_triggered=bool(trigs),
            highlight=dict(word=hw, colour=hcol, pale=hpale),
            # LINE-WINDOW law (#61, her live catch — 'Clacking' clipped off
            # tiaotiao L4 owen): the surface form of the CLAIMED word — the
            # word-tier receipt that MADE this seat's state (state_word, e.g. the
            # fold-lemma 'clack' whose surface is 'Clacking'), located back in the
            # line. The rendered text must always include it, never amputate it.
            # Note this is the DERIVING word, not necessarily the top-tok: on
            # owen L4 the top-tok is 'shuttle' but the claim is 'Clacking', and
            # THAT is the word that must not vanish. Empty when the state has no
            # single deriving word (e.g. pure line-scalar ghost handled by the
            # highlight itself).
            claimed_surface=_claimed_surface(txt, state_word),
        ))
    srcrow = seats[0]
    for s in seats:
        if s["unaligned"] or s["is_src"]:
            continue
        pair = (LAW.to3(srcrow["state"]), LAW.to3(s["state"]))
        s["transmission"] = LAW.CELL15.get(pair, "(no cell)") + \
            (" *" if (s["two"] or srcrow["two"]) else "")
    return dict(board=board, line_idx=line_idx, field=field,
                cut=cut, tier=tier, line_cut=line_cut,
                src_rid=src, seats=seats,
                # z display-tier facts (her rulings, #62): the field's z-dot
                # saturation = its battery grade, and the norms provenance.
                # z_suppressed (her ruling B, 07-28 night): grade-NONE fields
                # draw NO z strip — the chance-like z lives in the paper prose,
                # not the diagram (readable fact of the panel).
                z_norms_src=LAW.NEWS_NORMS_SRC, z_clamp=LAW.Z_CLAMP,
                z_saturation=LAW.z_saturation(field),
                z_suppressed=LAW.z_suppressed(field),
                # THE COLOUR z-LINE (her ruling, 07-28 night, #62 — ADOPTED). A
                # single z-threshold on the z strip = p95 of the unfired colour z
                # (credential-gated: DISCRIMINATION-graded fields only; today
                # colour alone). None ⟺ the field is not credentialed for a line.
                # Display/annotation tier; makes NO states (her pin).
                z_line=LAW.z_line(field), z_line_tier=LAW.ZLINE_TIER,
                z_grade=(LAW.line_exam_grades().get(field)
                         if field != "temporal"
                         else "temporal — ρ .860 (RULERS A7, distinct metric)"),
                # FULL-STACK BADGE count (her REVERSAL ruling, #62): the number of
                # ALIGNED seats whose language ∈ LAW.FULL_STACK_LANGS — gate F5
                # asserts the drawn badge count equals exactly this (zero badges
                # on any other seat). Single-sourced via the seats' full_stack flag.
                n_full_stack=sum(1 for x in seats
                                 if not x["unaligned"] and x.get("full_stack")),
                law="linegrain_law_60 · cascade = the TOP-TOK's investigation "
                    "(her design); (line: …) = context, never attribution")


# --------------------------------------------------------------- 2. RENDER --

# UNTESTED-CELL DISPLAY LAW (her ruling, #61: an uncovered channel's cell must
# NOT resemble tested-silence — "maybe a cross-out box"). A cell for a channel
# that returns None-carriers / uncovered (fr written/referent, de non-colour, en
# illumination, …) renders as a light diagonal cross-out box (two thin pale
# diagonals) + a tiny "untested" label — visibly DISTINCT from the tested-silent
# "—" (which means: the channel WAS consulted and nothing fired). The two are
# asserted apart by the gate + verify_exhibits.
UNTESTED_STROKE = "#cbd5e1"     # pale slate — the cross-out ink
UNTESTED_LABEL = "untested"
_UNT_W, _UNT_H = 58, 22          # the cross-out box footprint inside the cell

# FULL-STACK BADGE (her REVERSAL ruling, 07-28 late night, #62): a small filled
# square immediately before the seat rid on seats whose language ∈
# LAW.FULL_STACK_LANGS (word · written · referent all run — the zh full support).
# Hue NEUTRAL-DARK (not a field hue — it is a coverage fact, not a channel). The
# positive mark that replaces the retired fr deficiency star; class="full-stack-
# badge" so gate F5 + verify count it. Drawn as a 4px filled rect just left of the
# seat text (which shifts right by _BADGE_DX on badged seats).
BADGE_HUE = "#1e293b"           # neutral-dark slate (a coverage fact, not a field)
_BADGE_SZ = 8                    # ≈ a small filled square / 4px-ish filled rect
_BADGE_DX = 12                   # how far the seat text shifts right to seat it


def _untested_cell(s, x, y):
    """Render the UNTESTED mark for an uncovered channel cell: a pale diagonal
    cross-out box + the 'untested' label. Distinct by construction from '—'."""
    bx, by = x, y + 4
    s.append(f'<rect x="{bx}" y="{by}" width="{_UNT_W}" height="{_UNT_H}" '
             f'fill="none" stroke="{UNTESTED_STROKE}" stroke-width="0.8" '
             f'class="untested-box"/>')
    s.append(f'<line x1="{bx}" y1="{by}" x2="{bx+_UNT_W}" y2="{by+_UNT_H}" '
             f'stroke="{UNTESTED_STROKE}" stroke-width="0.8" '
             f'class="untested-diag"/>')
    s.append(f'<line x1="{bx+_UNT_W}" y1="{by}" x2="{bx}" y2="{by+_UNT_H}" '
             f'stroke="{UNTESTED_STROKE}" stroke-width="0.8" '
             f'class="untested-diag"/>')
    s.append(f'<text x="{bx+2}" y="{by+_UNT_H+7}" font-size="7" '
             f'fill="{UNTESTED_STROKE}">{UNTESTED_LABEL}</text>')


def _inv_cell(s, x, y, claimed, primary, context, colour, pale_probe):
    """One investigation cell: primary = the top-tok's claim status; context =
    other fires on this line, pale parenthetical. pale_probe = top-tok
    untriggered (mechanical view, ° law). This cell is only reached for a
    COVERED channel; tested-null renders as '—' (never the untested mark)."""
    if primary:
        deg = "°" if pale_probe else ""
        op = ' fill-opacity="0.55"' if pale_probe else ""
        s.append(f'<text x="{x}" y="{y+20}" font-size="10" fill="{colour}"'
                 f'{op}>{html.escape(primary[:18])}{deg}</text>')
    else:
        s.append(f'<text x="{x}" y="{y+20}" font-size="10" fill="{LAW.PALE}" '
                 f'fill-opacity="0.8">—</text>')
    if context:
        s.append(f'<text x="{x}" y="{y+31}" font-size="7.5" fill="{LAW.PALE}" '
                 f'fill-opacity="0.85">(line: {html.escape(context[:24])})</text>')


def render(m):
    field, seats = m["field"], m["seats"]
    hue = LAW.HUE[field]
    # CHANCE-LIKE Z SUPPRESSED (her ruling B, 07-28 night, #62): a field whose
    # line-tier grade is "NO demonstrated discrimination" DOES NOT render a z
    # strip at all — no dot, no label, no baseline, no tick (her: a globally
    # chance-like z "does not mean anything" → prose, not the graph). In its
    # place the panel carries ONE suppression sentence. temporal is NEVER
    # suppressed (ρ .860, a distinct metric — never chance-like here). Currently:
    # illumination. (Sequence of record in the spec: the chair first picked GREY
    # within her delegation; she superseded it the same sitting — removal from
    # the diagram, honesty in the paper prose. Hers governs.)
    z_suppressed = LAW.z_suppressed(field)
    vmax = max(0.06, max((abs(s["v"]) for s in seats
                          if not s["unaligned"] and s["v"] is not None),
                         default=0.06) * 1.15)
    W, ystep, y0 = 1980, 58, 148
    H = y0 + ystep * len(seats) + 66
    cutlab = (f"tok-cut |Δ|≥{m['cut']:.4f} ({m['tier']})"
              if m["cut"] is not None else m["tier"])
    pole = f" · {POLE[field]}" if field in POLE else ""
    # F8 legend wording (axis-truthful; her ruling 07-29, #63)
    tt_leg = ("max positive; faded = nearest, none fired"
              if field in LAW.SALIENCE_TRIGGER_FIELDS else f"sign kept{pole}")
    cut_leg = ("one-sided, positive"
               if field in LAW.SALIENCE_TRIGGER_FIELDS else "two-sided")
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'font-family="Helvetica,Arial,sans-serif">',
         f'<rect width="{W}" height="{H}" fill="white"/>',
         f'<text x="20" y="32" font-size="17" font-weight="bold">'
         f'{m["board"]} · line {m["line_idx"]+1} · {field.upper()} — '
         f'the top-tok and its investigation · {cutlab}</text>',
         f'<text x="20" y="52" font-size="10.5" fill="#555">highlight = the '
         f'top-tok, in top-tok colour (claims live in the cells) · cascade '
         f'cells = the TOP-TOK\'s investigation; (line: …) = context only'
         f' · bar = TWO strips: TOKEN-tier (upper) '
         f'<tspan fill="{LAW.TOK_HUE}">●</tspan> top-tok '
         f'({tt_leg}), dashed = cut ({cut_leg}) — the raw line-scalar leaves '
         f'the face (in the sidecar); '
         + (f'z (lower) SUPPRESSED — chance-like at grade (no line-tier '
            f'discrimination; see instruments prose) '
            if z_suppressed else
            f'z (lower) <tspan fill="{hue}">●</tspan> news-normed z (±3σ, 0 = '
            f'news mean; saturation = field battery grade; unnormed langs → '
            f'untested) ')
         + f'· ghost = TOKEN-tier only (her 07-28 pin; '
         f'line-residual = annotation) · boxed zone = token-grain; state/'
         f'transmission outside = LINE-level verdicts, word-derived: '
         f'state(word) names the deriving word · * = borrowed-cut 2-state · '
         f'★ = escape · ° = untriggered/mechanical · provenance: sidecar</text>',
         # FULL-STACK BADGE legend (her REVERSAL ruling, #62): one line in the
         # header legend area — the drawn square + its plain sentence. The badge
         # marks the full-support side positively (superseding the retired fr
         # deficiency star); non-zh referent thinness is carried in prose.
         f'<rect x="20" y="60" width="{_BADGE_SZ}" height="{_BADGE_SZ}" '
         f'fill="{BADGE_HUE}" class="full-stack-badge-legend"/>',
         f'<text x="{20 + _BADGE_DX}" y="67" font-size="10" fill="#555">'
         f'= full channel stack (word · written · referent all run)</text>',
         f'<rect x="875" y="96" width="460" height="18" fill="#e2e8f0"/>',
         f'<text x="1050" y="109" font-size="10" font-weight="bold" '
         f'fill="#1e293b">the top-tok\'s investigation（对 top-tok 的调查）</text>',
         f'<rect x="1005" y="116" width="330" height="16" fill="#f1f5f9"/>',
         f'<text x="1120" y="128" font-size="9.5" font-weight="bold" '
         f'fill="#334155">latent</text>',
         ]
    if field == "sound":
        # her ruling 07-28: sound_device is a SOUND organ — drawn on sound
        # panels only, never elsewhere
        s.append(f'<rect x="1338" y="96" width="104" height="36" '
                 f'fill="{LAW.DEV_BG}"/>')
        s.append(f'<text x="1345" y="109" font-size="9.5" font-weight="bold" '
                 f'fill="#0369a1">organ · parallel (line)</text>')
    heads = [(20, "seat"), (170, "line"), (562, "scalar bar"),
             (745, "TOP-TOK"), (880, "word claims it?"),
             (1010, "written claims it?"), (1155, "referent claims it?"),
             (1455, "★"), (1497, "state src→seat (word-derived)"),
             (1700, "transmission")]
    if field == "sound":
        heads.insert(7, (1345, "device"))
    for x, t in heads:
        s.append(f'<text x="{x}" y="{y0-6}" font-size="10.5" '
                 f'font-weight="bold" fill="#333">{t}</text>')
    # HER FRAME (07-28): one box around the token-grain zone — the TOP-TOK
    # and its investigation — so state/transmission read as what they are:
    # line-level verdicts (word-derived), a different thing, outside the box
    s.append(f'<rect x="732" y="78" width="716" height="{H-78-44}" '
             f'fill="none" stroke="#94a3b8" stroke-width="1.2" rx="8"/>')
    s.append(f'<text x="740" y="72" font-size="10.5" font-weight="bold" '
             f'fill="#475569">the TOP-TOK &amp; its investigation · '
             f'token-grain</text>')
    srcrow = seats[0]
    for i, r in enumerate(seats):
        y = y0 + i * ystep
        label = html.escape(r["rid"]) + (" ⟨MT⟩" if r["mt"] else "")
        if r["unaligned"]:
            s.append(f'<text x="20" y="{y+20}" font-size="11" '
                     f'font-weight="bold" fill="#94a3b8" font-style="italic">'
                     f'{label}</text>')
            s.append(f'<text x="170" y="{y+20}" font-size="10.5" '
                     f'fill="#94a3b8" font-style="italic">({r["status"]})</text>')
            continue
        lst = 'fill="#64748b" font-style="italic"' if r["mt"] else ""
        # FULL-STACK BADGE (her REVERSAL ruling, #62): a small neutral-dark filled
        # square immediately before the seat rid, on seats whose language ∈
        # LAW.FULL_STACK_LANGS (the zh full support: word · written · referent all
        # run). The positive mark superseding the retired fr deficiency star. The
        # seat text shifts right by _BADGE_DX so the square sits just before it.
        tx0 = 20
        if r.get("full_stack"):
            s.append(f'<rect x="20" y="{y+11}" width="{_BADGE_SZ}" '
                     f'height="{_BADGE_SZ}" fill="{BADGE_HUE}" '
                     f'class="full-stack-badge"/>')
            tx0 = 20 + _BADGE_DX
        s.append(f'<text x="{tx0}" y="{y+20}" font-size="11" font-weight="bold" '
                 f'{lst}>{label}</text>')
        txt, h = r["text"], r["highlight"]
        claim_sfc = r.get("claimed_surface")
        if h["word"] and h["word"] in txt:
            pre, _, post = txt.partition(h["word"])
            pre_vis, post_vis = pre[-34:], post[:34]
            pale = ' fill-opacity="0.65"' if h["pale"] else ''
            s.append(f'<text x="170" y="{y+20}" font-size="11">'
                     f'<tspan>{html.escape(pre_vis)}</tspan>'
                     f'<tspan font-weight="bold" fill="{h["colour"]}"{pale}>'
                     f'{html.escape(h["word"])}</tspan>'
                     f'<tspan>{html.escape(post_vis)}</tspan></text>')
            # LINE-WINDOW law (#61, her live catch — 'Clacking' amputated off
            # tiaotiao L4 owen): NEVER amputate a CLAIMED word's surface. The
            # highlight law is untouched (line above = top-tok always); if the
            # claimed receipt's surface would fall OUTSIDE this window, wrap a
            # SECOND line that carries it (claim underlined), so both the top-tok
            # and the claimed word are always in view. GATE F2 asserts it.
            visible = pre_vis + h["word"] + post_vis
            if claim_sfc and claim_sfc not in visible:
                cpre, _, cpost = txt.partition(claim_sfc)
                s.append(f'<text x="170" y="{y+32}" font-size="9.5" '
                         f'fill="#475569">'
                         f'<tspan>…{html.escape(cpre[-30:])}</tspan>'
                         f'<tspan font-weight="bold" fill="{h["colour"]}" '
                         f'text-decoration="underline">'
                         f'{html.escape(claim_sfc)}</tspan>'
                         f'<tspan>{html.escape(cpost[:30])}…</tspan></text>')
        else:
            # no locatable highlight — window from the front, but if a claimed
            # surface sits past it, anchor the window on the claimed surface so
            # it stays visible (never amputated).
            if claim_sfc and claim_sfc in txt and claim_sfc not in txt[:68]:
                cpre, _, cpost = txt.partition(claim_sfc)
                pale = ' fill-opacity="0.65"' if h.get("pale") else ''
                s.append(f'<text x="170" y="{y+20}" font-size="11">'
                         f'<tspan>…{html.escape(cpre[-30:])}</tspan>'
                         f'<tspan font-weight="bold" fill="{h["colour"]}"{pale} '
                         f'text-decoration="underline">'
                         f'{html.escape(claim_sfc)}</tspan>'
                         f'<tspan>{html.escape(cpost[:30])}…</tspan></text>')
            else:
                s.append(f'<text x="170" y="{y+20}" font-size="11">'
                         f'{html.escape(txt[:68])}</text>')
        # HER LAYOUT RULING (07-28): the dominant cell belongs to the TOP-TOK;
        # the line-scalar's currency on the face is now z ALONE (lower strip).
        tt0 = r["top_tok"]
        if tt0["token"]:
            faded0 = bool(tt0.get("faded"))
            cell_op = 0.18 if tt0["triggered"] else \
                (0.04 if faded0 else 0.07)
            s.append(f'<rect x="740" y="{y}" width="110" height="36" '
                     f'fill="{LAW.TOK_HUE}" fill-opacity="{cell_op}" '
                     f'stroke="#d0d0d0"/>')
            # F8 third grammar: FADED = nearness (no positive mover on a
            # salience axis) — italic, low ink, never bold, never °
            if faded0:
                wt = 'fill-opacity="0.4" font-style="italic"'
            elif tt0["triggered"]:
                wt = 'font-weight="bold"'
            else:
                wt = 'fill-opacity="0.75"'
            deg0 = "" if (tt0["triggered"] or faded0) else "°"
            s.append(f'<text x="746" y="{y+16}" font-size="12" '
                     f'class="{"f8-faded" if faded0 else "toptok"}" '
                     f'fill="{LAW.TOK_HUE}" {wt}>'
                     f'{html.escape(tt0["token"][:9])}</text>')
            s.append(f'<text x="746" y="{y+30}" font-size="9" '
                     f'fill="{LAW.TOK_HUE}" fill-opacity="0.8">'
                     f'Δ{tt0["delta"]:+.3f}{deg0}'
                     f'{" ·nearest" if faded0 else ""}</text>')
        else:
            s.append(f'<text x="746" y="{y+20}" font-size="10" '
                     f'fill="{LAW.PALE}">—</text>')
        # THE TWO-STRIP BAR (her rulings, 07-28 evening, #62: "2 bar will be
        # good"; amended 07-28 NIGHT #62 — RAW DOT RETIRES, her ruling A). Same
        # footprint (bx=560, bw=150), row height unchanged. UPPER = the TOKEN-
        # TIER strip: center tick + cut dashes (SALIENCE = the POSITIVE dash
        # only; VALUE rulers keep BOTH — her dash ruling, below) + the orange
        # top-tok dot ONLY. The muted raw line-scalar dot and its raw value
        # label are
        # GONE from the face (her ruling A: the raw non-z line-scalar leaves the
        # face; the line's currency here is z ALONE, lower strip). The raw
        # reading survives in the sidecar .model.json (readable-facts law).
        # LOWER = the z strip: the line-scalar as a news-normed z, the only face
        # currency for the line.
        bx, bw = 560, 150
        cx = bx + bw / 2
        rawy = y + 11               # token-tier strip baseline (was y+18)
        # --- TOKEN-TIER STRIP (upper): center tick + cut dash(es) ---
        s.append(f'<line x1="{bx}" y1="{rawy}" x2="{bx+bw}" y2="{rawy}" '
                 f'stroke="#ccc"/>')
        s.append(f'<line x1="{cx}" y1="{rawy-9}" x2="{cx}" y2="{rawy+9}" '
                 f'stroke="#999"/>')
        # THE CUT-DASH SIDE LAW (her ruling, 07-28 late night, #62 — verbatim
        # trigger: "i am still seeing the double little lines for at least
        # sound!"). Under the v5.0 positive-only trigger law a NEGATIVE Δ on a
        # SALIENCE axis {color, plant, sound} is dilution, never an event — so
        # the salience strip draws the POSITIVE cut dash ALONE; the two-sided
        # negative dash there was display-legacy (EXHIBIT_SPEC amendment +
        # NEEDS_HER item 2, now RULED). VALUE rulers {illumination, temporal}
        # keep BOTH sides (two-sided remains their trigger law — a large
        # negative excursion IS a salient reading of the opposite pole). The
        # salience/value split is SINGLE-SOURCED from the law module's
        # LAW.SALIENCE_TRIGGER_FIELDS (the same set the trigger uses — no second
        # copy). class="cut-dash" so gate F-style / verify count the sides.
        if m["cut"] is not None:
            signs = (1,) if field in LAW.SALIENCE_TRIGGER_FIELDS else (1, -1)
            for sign in signs:
                cutx = cx + sign * (m["cut"] / vmax) * (bw / 2)
                s.append(f'<line x1="{cutx:.1f}" y1="{rawy-11}" x2="{cutx:.1f}" '
                         f'y2="{rawy+11}" stroke="{LAW.TOK_HUE}" '
                         f'stroke-dasharray="4,3" class="cut-dash"/>')
        # (raw line-scalar dot + its value RETIRED here — her ruling A, 07-28
        # night: the raw non-z reading leaves the face; it lives in the sidecar.)
        tt = r["top_tok"]
        if tt["delta"] is not None:
            tx = cx + (max(-vmax, min(vmax, tt["delta"])) / vmax) * (bw / 2)
            s.append(f'<circle cx="{tx:.1f}" cy="{rawy}" r="3.5" '
                     f'fill="{LAW.TOK_HUE}"/>')
        # --- z STRIP (lower): FIXED symmetric ±3 z-units, center tick = 0 (the
        # language's news mean); the line-scalar dot in field hue at the z
        # position, SATURATION = the field's battery grade (her ruling: the
        # muted dot's true reason, displayed as itself). Small z label z±X.X.
        # jp / unnormed seats (z is None) draw an EMPTY strip + an untested-bar
        # mark (her jp ruling) — a DISTINCT class from the untested-CELL box, so
        # gate F's untested-box count law is untouched. ---
        # HER RULING B (07-28 night): when the field is chance-like (grade NONE),
        # the z strip is SUPPRESSED ENTIRELY — no baseline, no tick, no dot, no
        # label, no untested-bar. Nothing is drawn here; the panel carries ONE
        # suppression sentence in the footer instead (added once, below). The jp
        # untested-bar case is UNTOUCHED — it only applies on non-suppressed
        # fields (a different absence: no news norm, not no discrimination).
        if not z_suppressed:
            zy = y + 40                 # z strip baseline
            s.append(f'<line x1="{bx}" y1="{zy}" x2="{bx+bw}" y2="{zy}" '
                     f'stroke="#e2e8f0" class="z-baseline"/>')
            s.append(f'<line x1="{cx}" y1="{zy-6}" x2="{cx}" y2="{zy+6}" '
                     f'stroke="#cbd5e1"/>')
            # THE COLOUR z-LINE (her ruling, 07-28 night, #62 — ADOPTED). A dashed
            # vertical at the registered z-line on the z strip (credential-gated
            # via LAW.z_line: DISCRIMINATION-graded fields only, today colour), at
            # the SAME ±3σ scale/clamp as the z dots, with a tiny label
            # "z-cut ·ADOPTED". Drawn once per qualifying row so the strip reads
            # its threshold; makes NO states (her pin). Licensed reading: a dot to
            # its right is "relatively colourful against the census unfired
            # baseline (>95% of boolean-unfired lines)", never proof of colour.
            zline = m.get("z_line")
            if zline is not None:
                zlc = max(-LAW.Z_CLAMP, min(LAW.Z_CLAMP, zline))
                zlx = cx + (zlc / LAW.Z_CLAMP) * (bw / 2)
                s.append(f'<line x1="{zlx:.1f}" y1="{zy-9}" x2="{zlx:.1f}" '
                         f'y2="{zy+9}" stroke="{hue}" stroke-width="1" '
                         f'stroke-dasharray="2,2" class="z-line"/>')
                s.append(f'<text x="{zlx:.1f}" y="{zy-11}" font-size="6.5" '
                         f'text-anchor="middle" fill="{hue}" class="z-line-label">'
                         f'z-cut ·{m.get("z_line_tier","ADOPTED")}</text>')
            zval = r.get("z")
            if zval is None:
                # her jp ruling: empty z strip bearing an untested-style mark,
                # own class untested-bar (kin to untested-cell, but DISTINCT).
                uw, uhh = 30, 12
                ux0, uy0 = cx - uw / 2, zy - uhh / 2
                s.append(f'<rect x="{ux0:.1f}" y="{uy0:.1f}" width="{uw}" '
                         f'height="{uhh}" fill="none" stroke="{UNTESTED_STROKE}" '
                         f'stroke-width="0.8" class="untested-bar"/>')
                s.append(f'<line x1="{ux0:.1f}" y1="{uy0:.1f}" '
                         f'x2="{ux0+uw:.1f}" y2="{uy0+uhh:.1f}" '
                         f'stroke="{UNTESTED_STROKE}" stroke-width="0.8" '
                         f'class="untested-bar-diag"/>')
                s.append(f'<line x1="{ux0+uw:.1f}" y1="{uy0:.1f}" '
                         f'x2="{ux0:.1f}" y2="{uy0+uhh:.1f}" '
                         f'stroke="{UNTESTED_STROKE}" stroke-width="0.8" '
                         f'class="untested-bar-diag"/>')
                s.append(f'<text x="{cx:.1f}" y="{zy+18}" font-size="7" '
                         f'text-anchor="middle" fill="{UNTESTED_STROKE}">'
                         f'untested (no news norm)</text>')
            else:
                zc = max(-LAW.Z_CLAMP, min(LAW.Z_CLAMP, zval))   # clamp position
                zpx = cx + (zc / LAW.Z_CLAMP) * (bw / 2)
                s.append(f'<circle cx="{zpx:.1f}" cy="{zy}" r="4" fill="{hue}" '
                         f'fill-opacity="{m["z_saturation"]}" class="z-dot"/>')
                zlx = max(bx + 18, min(bx + bw - 18, zpx))
                s.append(f'<text x="{zlx:.1f}" y="{zy+13}" font-size="8" '
                         f'text-anchor="middle" fill="{hue}" class="z-label">'
                         f'z{zval:+.1f}</text>')
        inv = r["investigation"]
        if field == "sound":
            s.append(f'<rect x="1338" y="{y-4}" width="104" '
                     f'height="{ystep-8}" fill="{LAW.DEV_BG}" '
                     f'fill-opacity="0.55"/>')
        pale_probe = not tt["triggered"]
        w = inv["word"]
        if not w["covered"]:
            _untested_cell(s, 880, y)          # UNCOVERED channel → untested mark
        else:
            ctx = ",".join(x for x in w["line_receipts"]
                           if x != w["receipt"]) if w["line_receipts"] else ""
            _inv_cell(s, 880, y, w["claims_top"], w["receipt"], ctx,
                      LAW.HUE[field], pale_probe)
        wr = inv["written"]
        if not wr["covered"]:
            _untested_cell(s, 1010, y)         # UNCOVERED channel → untested mark
        else:
            prim = ",".join(wr["carriers"]) if wr["claims_top"] else None
            ctx = (",".join(wr["carriers"])
                   if (wr["fired"] and not wr["claims_top"]) else "")
            _inv_cell(s, 1010, y, wr["claims_top"], prim, ctx,
                      LAW.AMBER, pale_probe)
        rf = inv["referent"]
        if not rf["covered"]:
            _untested_cell(s, 1155, y)         # UNCOVERED channel → untested mark
        else:
            ctx = " ".join(x for x in rf["line_display"]
                           if x != rf["display"]) if rf["line_display"] else ""
            _inv_cell(s, 1155, y, rf["claims_top"], rf["display"], ctx,
                      LAW.PURPLE, pale_probe)
        dev = inv["device"]
        if field == "sound":
            if not dev["covered"]:
                _untested_cell(s, 1345, y)     # UNCOVERED device → untested mark
            else:
                dtxt = (",".join(dev["receipts"]) if dev["receipts"] else "—")
                s.append(f'<text x="1345" y="{y+20}" font-size="10" fill="#0369a1"'
                         f'{" font-weight=" + chr(34) + "bold" + chr(34) if dev["fired"] else ""}>'
                         f'{html.escape(dtxt[:12])}</text>')
        if r["star"]:
            s.append(f'<text x="1455" y="{y+20}" font-size="12" '
                     f'fill="{LAW.TOK_HUE}">★</text>')
        sdev = "+dev" if (field == "sound" and dev["fired"]) else ""
        srcdev = "+dev" if (field == "sound"
                            and srcrow["investigation"]["device"]["fired"]) else ""

        def _sw(seat):
            w = seat.get("state_word")
            return f'({html.escape(str(w)[:6])})' if w else ""

        if r["is_src"]:
            pair = f'{srcrow["state"]}{_sw(srcrow)}{srcdev} (source)'
            trans = "— source —"
        else:
            pair = (f'{srcrow["state"]}{_sw(srcrow)}{srcdev} → '
                    f'{r["state"]}{_sw(r)}{sdev}')
            trans = r["transmission"]
        s.append(f'<text x="1497" y="{y+20}" font-size="9.5" '
                 f'font-weight="bold">{pair}</text>')
        s.append(f'<text x="1700" y="{y+20}" font-size="10.5" '
                 f'font-weight="bold" fill="#334155">{trans}</text>')
    # HER RULING B (07-28 night): a chance-like (grade-NONE) field draws NO z
    # strip; in place of it the panel carries EXACTLY ONE suppression sentence —
    # honesty in prose, not the graph. Own class z-suppress-note; gate/verify
    # assert exactly one on suppressed panels, zero elsewhere.
    if z_suppressed:
        s.append(f'<text x="20" y="{H-38}" font-size="10" fill="#666" '
                 f'class="z-suppress-note">{html.escape(LAW.Z_SUPPRESS_NOTE)}'
                 f'</text>')
    s.append(f'<text x="20" y="{H-24}" font-size="10" fill="#666">'
             f'Law: {html.escape(m["law"])} · cuts promotion_threshold_59 + '
             f'linecut_v2_60 · single-sourced; sidecar = provenance'
             f' · z: {LAW.NEWS_NORMS_SRC} (±{LAW.Z_CLAMP:g}σ clamp; '
             f'saturation=line-tier grade{"; suppressed on grade-NONE fields" if z_suppressed else ""}).</text>')
    # THE READING-KEY POINTER (her "explain those stars and lines and whatever in
    # graphs", #62): one line pointing every face at the standalone reading key
    # figure, which draws + names EVERY mark on the faces. class="key-pointer".
    s.append(f'<text x="20" y="{H-10}" font-size="10" fill="#666" '
             f'class="key-pointer">key: {KEY_FIGURE_STEM}</text>')
    s.append('</svg>')
    return "\n".join(s)


# ----------------------------------------------------------------- 3. GATE --

def gate(m, svg):
    F = []
    field = m["field"]
    d, _, _ = LAW.load_board(m["board"])
    F += _gate_per_seat(m, d, field)
    F += _gate_status_rows(m, svg)
    F += _gate_untested_cells(m, svg, field)
    F += _gate_line_window(m, svg)
    z_suppressed = LAW.z_suppressed(field)
    F += _gate_z_strip(m, svg, d, field, z_suppressed)
    F += _gate_raw_dot(svg, field)
    F += _gate_z_line(m, svg, field, z_suppressed)
    F += _gate_cut_dash(m, svg, field)
    F += _gate_full_stack_badge(m, svg)
    F += _gate_key_pointer(svg)
    return F


# ── gate() helpers (#71 refactor, 2026-08-12). ONE LAW PER FUNCTION, called by
# gate() in exactly the order the single 300-line body ran them, each returning
# its failure list; the assertion messages are carried over verbatim, so a gate
# report reads identically to before. Splitting is presentational only — no law
# was added, dropped, reordered or reworded. (The deliberate physical duplication
# against verify_exhibits_60's mirrored second lock is UNTOUCHED: two locks, one
# law, by standing in-code ruling.)

def _gate_per_seat(m, d, field):
    """Laws C · E · A · D + the state-pair re-derivation, per aligned seat.

    Kept as ONE pass because that is how it ran: the four checks share the
    carrier-line row, the freshly re-derived top-tok and the committed boolean
    row, and their failure messages interleave per seat in that order."""
    F = []
    for r in m["seats"]:
        rid = r["rid"]
        if r["unaligned"]:
            continue
        # folded seats: verify against the model's DECLARED carrier line
        ci = r.get("carrier_line", m["line_idx"] + 1) - 1
        row = d["scalar_readings"][rid][ci]
        # C: top-tok per axis (F8, her ruling 07-29): SALIENCE = max
        # POSITIVE contentful (least-negative FADED fallback); VALUE =
        # |Δ|-max contentful
        best = None
        want_faded = False
        if field in LAW.SALIENCE_TRIGGER_FIELDS:
            pos_g, near_g = None, None
            for t, dd in (row.get("top_delta", {}).get(field) or []):
                ts = LAW._clean(t)
                if dd is None or not ts or not LAW._contentful(ts):
                    continue
                if dd > 0:
                    if pos_g is None or dd > pos_g[1]:
                        pos_g = (ts, dd)
                elif near_g is None or dd > near_g[1]:
                    near_g = (ts, dd)
            best = pos_g or near_g
            want_faded = pos_g is None and near_g is not None
        else:
            for t, dd in (row.get("top_delta", {}).get(field) or []):
                ts = LAW._clean(t)
                if dd is not None and ts and LAW._contentful(ts):
                    best = (ts, dd)
                    break
        if best and r["top_tok"]["token"] != best[0]:
            F.append(f"{rid}: top-tok {r['top_tok']['token']!r} != "
                     f"per-axis F8 pick {best[0]!r}")
        if best and bool(r["top_tok"].get("faded")) != want_faded:
            F.append(f"{rid}: faded flag {r['top_tok'].get('faded')!r} != "
                     f"F8 expectation {want_faded!r}")
        # E: highlight IS the top-tok whenever locatable
        hw = r["highlight"]["word"]
        if best and hw is not None and not _matches(best[0], hw):
            F.append(f"{rid}: highlight {hw!r} != top-tok {best[0]!r}")
        if best and hw is None and LAW.find_span(r["text"], best[0]):
            F.append(f"{rid}: top-tok {best[0]!r} locatable but unhighlighted")
        # A: investigation cells equal the top-tok's fresh claim status
        inv = r["investigation"]
        boolrow = (d["booleans"].get(rid) or [{}] * 99)[ci] \
            if d["booleans"].get(rid) else {}
        # committed receipts pass the SAME law gate the model uses: receipts
        # exist as claims only when fires is True (a json may carry noted
        # receipts on an unfired/uncovered boolean — those are not claims;
        # the tsubouchi 風[廣韻] lesson, 07-28)
        _b = boolrow.get(field, {})
        committed = (_b.get("receipts") or []) if _b.get("fires") is True else []
        tm = r["top_tok"]["token"]
        want_claim = next((w for w in committed if tm and _matches(tm, w)),
                          None)
        if bool(want_claim) != inv["word"]["claims_top"] or \
                (want_claim or None) != inv["word"]["receipt"]:
            F.append(f"{rid}: word-claim cell {inv['word']['receipt']!r} != "
                     f"fresh {want_claim!r}")
        # D: line-context receipts equal committed data (nothing invented)
        if sorted(LAW._word0(x) for x in inv["word"]["line_receipts"]) != \
                sorted(LAW._word0(x) for x in committed):
            F.append(f"{rid}: line receipts {inv['word']['line_receipts']} != "
                     f"committed {committed}")
        for x in inv["word"]["line_receipts"]:
            if LAW._word0(x) and not LAW._contentful(LAW._word0(x)):
                F.append(f"{rid}: non-contentful display unit {x!r}")
        # state pair re-derivation
        if r["is_src"]:
            continue
        pair = (LAW.to3(m["seats"][0]["state"]), LAW.to3(r["state"]))
        want = LAW.CELL15.get(pair, "(no cell)")
        if not r["transmission"].startswith(want):
            F.append(f"{rid}: transmission {r['transmission']!r} != {want!r}")
    return F


def _gate_status_rows(m, svg):
    """B: count-mismatched (unaligned/dropped) seats render as STATUS rows."""
    F = []
    # B: unaligned seats render as status rows
    lines = svg.splitlines()
    for r in m["seats"]:
        if not r["unaligned"]:
            continue
        band = [i for i, ln in enumerate(lines)
                if html.escape(r["rid"]) in ln]
        # dropped rows are status rows too (#60's law: "dropped source lines
        # = honest '(dropped)' rows"); this check predated that render path
        # and false-failed the first dropped-row pick (#61, qingqing L5 —
        # verify_exhibits already checked both terms)
        blob = "\n".join(lines[band[0]:band[0] + 3]) if band else ""
        if band and "unaligned" not in blob and "dropped" not in blob:
            F.append(f"{r['rid']}: unaligned seat lacks status text")
    return F


def _gate_untested_cells(m, svg, field):
    """F: THE UNTESTED-CELL DISPLAY LAW (her ruling #61)."""
    F = []
    # F: THE UNTESTED-CELL DISPLAY LAW (her ruling #61). An uncovered channel's
    # cell MUST carry the untested cross-out mark; a tested-null covered cell MUST
    # NOT (it renders '—'). Assert by construction: the count of untested boxes in
    # the SVG equals the count of UNCOVERED channel-cells across aligned seats in
    # the model (word · written · referent · device-on-sound). This makes
    # untested and tested-silent provably distinct — the two can never collapse.
    want_untested = 0
    for r in m["seats"]:
        if r["unaligned"]:
            continue
        invg = r["investigation"]
        if not invg["word"]["covered"]:
            want_untested += 1
        if not invg["written"]["covered"]:
            want_untested += 1
        if not invg["referent"]["covered"]:
            want_untested += 1
        if field == "sound" and not invg["device"]["covered"]:
            want_untested += 1
    got_untested = svg.count('class="untested-box"')
    if got_untested != want_untested:
        F.append(f"untested-cell law: {got_untested} untested marks drawn != "
                 f"{want_untested} uncovered channel-cells in the model")
    # tested-null must NOT wear the mark: an untested box must never share a cell
    # column-row with a '—' from a COVERED channel. Structural guarantee: the
    # render draws EITHER _untested_cell OR _inv_cell per cell, never both — so a
    # mark count that matches the uncovered count (above) already proves no
    # covered '—' cell was marked. (Belt-and-braces: the mark carries its own
    # 'untested' label token, '—' never does.)
    if got_untested and "untested" not in svg:
        F.append("untested-cell law: mark drawn but 'untested' label absent")
    return F


def _gate_line_window(m, svg):
    """F2: THE LINE-WINDOW LAW (her live catch, #61)."""
    F = []
    # F2: THE LINE-WINDOW LAW (her live catch, #61 — 'Clacking' amputated off
    # the front of tiaotiao L4 owen). A CLAIMED word's surface form must NEVER be
    # amputated out of the rendered seat text: whenever the model located a
    # claimed_surface, that surface must appear in the SVG (first-line window OR
    # the wrapped claim line). The highlight law is unaffected (checked at E).
    for r in m["seats"]:
        if r["unaligned"]:
            continue
        cs = r.get("claimed_surface")
        if cs and html.escape(cs) not in svg:
            F.append(f"{r['rid']}: line-window law — claimed surface {cs!r} "
                     f"amputated from rendered text (not in SVG)")
    return F


def _gate_z_strip(m, svg, d, field, z_suppressed):
    """F3: THE z-STRIP LAW (her rulings, #62) — two regimes by line-tier grade."""
    F = []
    # F3: THE z-STRIP LAW (her rulings, #62 — the two-strip bar + jp untested +
    # chance-like SUPPRESSION). Two regimes, decided by the field's line-tier
    # grade (re-derived from the exam json via LAW.z_suppressed):
    #   • SUPPRESSED (grade NONE, currently illumination): her ruling B, 07-28
    #     night — the z strip is REMOVED from the diagram. ZERO z dots, ZERO z
    #     labels, ZERO untested-bars anywhere on the panel; EXACTLY ONE
    #     suppression sentence (class z-suppress-note). Honesty in prose.
    #   • NORMAL (all other fields, incl. temporal): for every ALIGNED seat, a
    #     NORMED language ⟹ exactly one z dot + one z label, the label's rounded
    #     value == round(z,1) recomputed FRESH from news_norms() + the committed
    #     reading (never trusting the model's carried z); an UNNORMED language
    #     (jp / non-{en,zh,de,fr}) ⟹ exactly one untested-bar and ZERO z dots.
    # Count-based, like F — two locks with verify_exhibits_60.
    got_zdots = svg.count('class="z-dot"')
    got_zlabels = svg.count('class="z-label"')
    got_ubars = svg.count('class="untested-bar"')
    got_supp = svg.count('class="z-suppress-note"')
    if z_suppressed:
        # her ruling B: NOTHING of the z strip may render; the panel says so once
        if got_zdots or got_zlabels or got_ubars:
            F.append(f"z-suppress law (B): field {field!r} is grade-NONE — the "
                     f"z strip must not render; got {got_zdots} z dots / "
                     f"{got_zlabels} labels / {got_ubars} untested-bars (all 0)")
        if got_supp != 1:
            F.append(f"z-suppress law (B): field {field!r} is grade-NONE — "
                     f"expected EXACTLY ONE suppression sentence, got {got_supp}")
        if got_supp and html.escape(LAW.Z_SUPPRESS_NOTE) not in svg:
            F.append("z-suppress law (B): suppression sentence text mismatch")
    else:
        if got_supp != 0:
            F.append(f"z-suppress law (B): field {field!r} is NOT grade-NONE — "
                     f"no suppression sentence expected, got {got_supp}")
        want_zdots = want_untested_bars = 0
        for r in m["seats"]:
            if r["unaligned"]:
                continue
            # re-derive z FRESH from the norms json + the committed reading (the
            # same reading build_model read: the carrier row's field value),
            # never the model's carried z — a stale z can never hide here.
            ci = r.get("carrier_line", m["line_idx"] + 1) - 1
            vfresh = d["scalar_readings"][r["rid"]][ci]["reading"].get(field)
            zfresh = LAW.z_of(r["rid"].split(":", 1)[0], field, vfresh)
            if zfresh is None:
                want_untested_bars += 1
            else:
                want_zdots += 1
                lbl = f"z{zfresh:+.1f}"   # the rounded label the render must draw
                if f'>{lbl}</text>' not in svg:
                    F.append(f"{r['rid']}: z-strip law — expected z label "
                             f"{lbl!r} (from fresh z={zfresh:+.4f}) absent in SVG")
        if got_zdots != want_zdots:
            F.append(f"z-strip law: {got_zdots} z dots drawn != {want_zdots} "
                     f"normed aligned seats")
        if got_zlabels != want_zdots:
            F.append(f"z-strip law: {got_zlabels} z labels drawn != {want_zdots} "
                     f"normed aligned seats (one label per z dot)")
        if got_ubars != want_untested_bars:
            F.append(f"z-strip law: {got_ubars} untested-bar marks drawn != "
                     f"{want_untested_bars} unnormed aligned seats")
    return F


def _gate_raw_dot(svg, field):
    """F3b: RAW DOT RETIRES (her ruling A, 07-28 night) — global, every panel."""
    F = []
    # F3b: RAW DOT RETIRES (her ruling A, 07-28 night — global, every panel). The
    # raw non-z line-scalar dot must NOT appear on the face: the muted field-hue
    # dot was the ONLY circle bearing fill="{hue}" that is not a z-dot, so the
    # count of field-hue circles that are NOT z-dots must be 0, and its unique
    # signature fill-opacity="0.35" must be wholly absent. (On suppressed panels
    # there are no z-dots at all, so ANY field-hue circle would be a raw dot.)
    hue = LAW.HUE[field]
    hue_dots = sum(1 for ln in svg.splitlines()
                   if 'class="z-dot"' in ln and f'fill="{hue}"' in ln)
    hue_circles = sum(1 for ln in svg.splitlines()
                      if ln.lstrip().startswith('<circle')
                      and f'fill="{hue}"' in ln)
    if hue_circles - hue_dots != 0:
        F.append(f"raw-dot-retires (A): {hue_circles - hue_dots} field-hue "
                 f"circle(s) on the upper strip — the raw line dot must not "
                 f"appear")
    if 'fill-opacity="0.35"' in svg:
        F.append("raw-dot-retires (A): raw-dot signature fill-opacity=\"0.35\" "
                 "still present in SVG")
    return F


def _gate_z_line(m, svg, field, z_suppressed):
    """F3c: THE COLOUR z-LINE (her ruling, 07-28 night, #62 — ADOPTED)."""
    F = []
    # F3c: THE COLOUR z-LINE (her ruling, 07-28 night, #62 — ADOPTED). The z-line
    # is present IFF the field is CREDENTIALED (LAW.z_line(field) is not None:
    # DISCRIMINATION-graded, with a registered value — today colour alone) AND the
    # panel is not suppressed. Re-derive fresh from the LAW module (never the
    # model's carried value). On a credentialed non-suppressed panel one z-line +
    # one label is drawn per z-strip (one per aligned seat); on any other panel
    # ZERO. The line's x-position must sit at the registered value (checked via the
    # clamp arithmetic below) — the line can never drift off its registered z.
    got_zlines = svg.count('class="z-line"')
    got_zline_labels = svg.count('class="z-line-label"')
    zline_fresh = LAW.z_line(field)
    if zline_fresh is not None and not z_suppressed:
        want_zlines = sum(1 for r in m["seats"] if not r["unaligned"])
        if got_zlines != want_zlines:
            F.append(f"z-line law (F3c): {got_zlines} z-lines drawn != "
                     f"{want_zlines} z strips (credentialed field {field!r}; one "
                     f"per aligned seat)")
        if got_zline_labels != want_zlines:
            F.append(f"z-line law (F3c): {got_zline_labels} z-line labels != "
                     f"{want_zlines} (one 'z-cut ·{LAW.ZLINE_TIER}' per line)")
        # position: the registered value, clamped to ±Z_CLAMP, at the strip scale
        bx, bw = 560, 150
        cx = bx + bw / 2
        zlc = max(-LAW.Z_CLAMP, min(LAW.Z_CLAMP, zline_fresh))
        want_x = f'x1="{cx + (zlc / LAW.Z_CLAMP) * (bw / 2):.1f}"'
        if got_zlines and want_x not in svg:
            F.append(f"z-line law (F3c): z-line not at the registered value "
                     f"(expected {want_x} for z={zline_fresh:+.4f})")
        if got_zlines and f'·{LAW.ZLINE_TIER}' not in svg:
            F.append(f"z-line law (F3c): tier label '·{LAW.ZLINE_TIER}' absent")
    else:
        if got_zlines or got_zline_labels:
            F.append(f"z-line law (F3c): field {field!r} is NOT credentialed for a "
                     f"z-line (or suppressed) — expected ZERO, got {got_zlines} "
                     f"lines / {got_zline_labels} labels")
    return F


def _gate_cut_dash(m, svg, field):
    """F4: THE CUT-DASH SIDE LAW (her ruling, 07-28 late night, #62)."""
    F = []
    # F4: THE CUT-DASH SIDE LAW (her ruling, 07-28 late night, #62 — "i am still
    # seeing the double little lines for at least sound!"). The token-tier cut
    # dash is ONE-SIDED on SALIENCE panels (color/plant/sound: the positive dash
    # alone, v5.0 positive-only law) and TWO-SIDED on VALUE panels (illumination,
    # temporal: both sides remain their law). Count-based, like F: the split is
    # re-derived FRESH from LAW.SALIENCE_TRIGGER_FIELDS (single source), so every
    # aligned seat draws exactly (1 if salience else 2) cut dashes — UNLESS the
    # field carries no cut (temporal: value-axis, no cut), where zero dashes draw
    # on either regime. Mirrored in verify_exhibits_60.
    got_dashes = svg.count('class="cut-dash"')
    if m["cut"] is None:
        want_dashes = 0                      # no cut → no cut dash, either side
        per = 0
    else:
        per = 1 if field in LAW.SALIENCE_TRIGGER_FIELDS else 2
        want_dashes = per * sum(1 for r in m["seats"] if not r["unaligned"])
    if got_dashes != want_dashes:
        F.append(f"cut-dash side law (F4): {got_dashes} cut dashes drawn != "
                 f"{want_dashes} ({per}/aligned-seat; field {field!r} is "
                 f"{'SALIENCE one-sided' if field in LAW.SALIENCE_TRIGGER_FIELDS else 'VALUE two-sided'}"
                 f"{', but no cut' if m['cut'] is None else ''})")
    return F


def _gate_full_stack_badge(m, svg):
    """F5: THE FULL-STACK BADGE LAW."""
    F = []
    # F5: THE FULL-STACK BADGE LAW (her REVERSAL ruling, 07-28 late night, #62 —
    # "zh is terrific and we have the full support here!"). The badge is a small
    # neutral-dark filled square before the seat rid on EXACTLY the aligned seats
    # whose language ∈ LAW.FULL_STACK_LANGS (word · written · referent all run).
    # Count-based, like F: the badge count in the SVG
    # == the count of aligned seats with a full-stack language (re-derived FRESH
    # from LAW.FULL_STACK_LANGS + the seat rids' language prefix, never trusting
    # the model's carried flag); zero badges on any other seat. Mirrored in
    # verify_exhibits_60 — two locks, one law. (The legend badge carries its own
    # class full-stack-badge-legend, so it is NOT counted here.)
    want_badges = sum(1 for r in m["seats"] if not r["unaligned"]
                      and r["rid"].split(":", 1)[0] in LAW.FULL_STACK_LANGS)
    got_badges = svg.count('class="full-stack-badge"')
    if got_badges != want_badges:
        F.append(f"full-stack badge law (F5): {got_badges} badges drawn != "
                 f"{want_badges} aligned full-stack-language seats "
                 f"(LAW.FULL_STACK_LANGS={sorted(LAW.FULL_STACK_LANGS)})")
    # exactly one legend badge per panel (the header key line)
    if svg.count('class="full-stack-badge-legend"') != 1:
        F.append(f"full-stack badge law (F5): expected exactly ONE legend badge, "
                 f"got {svg.count('class=' + chr(34) + 'full-stack-badge-legend' + chr(34))}")
    return F


def _gate_key_pointer(svg):
    """THE READING-KEY POINTER: exactly one per face, naming the key figure."""
    F = []
    # the reading-key pointer line: exactly one per face, naming the key figure
    if svg.count('class="key-pointer"') != 1:
        F.append(f"key-pointer law: expected exactly ONE key pointer line, got "
                 f"{svg.count('class=' + chr(34) + 'key-pointer' + chr(34))}")
    if KEY_FIGURE_STEM not in svg:
        F.append(f"key-pointer law: the key figure stem {KEY_FIGURE_STEM!r} "
                 f"is absent from the face")
    return F


def find_line(board, needle):
    d, _, _ = LAW.load_board(board)
    for rid, rr in d["scalar_readings"].items():
        if rid.startswith(d["source_lang"] + ":"):
            for row in rr:
                if row.get("text") and needle in row["text"]:
                    return row["line_no"] - 1
    raise SystemExit(f"line with {needle!r} not found in {board} source")


def samples():
    d18, _, _ = LAW.load_board("sonnet18")
    src18 = next(r for r in d18["scalar_readings"] if r.startswith("en:"))
    tl = max(d18["scalar_readings"][src18],
             key=lambda r: abs(r["reading"]["temporal"]))
    dx, _, _ = LAW.load_board("xibei")
    srcx = next(r for r in dx["scalar_readings"] if r.startswith("zh:"))
    il = max(dx["scalar_readings"][srcx],
             key=lambda r: abs(r["reading"]["illumination"]))
    return [
        ("sample_colour_correspondances_nuit_59.svg", "correspondances",
         find_line("correspondances", "comme la nuit"), "color"),
        ("sample_sound_tiaotiao_L4_59.svg", "tiaotiao", 3, "sound"),
        ("sample_plant_qingqing_L1_59.svg", "qingqing", 0, "plant"),
        (f"sample_illum_xibei_L{il['line_no']}_59.svg", "xibei",
         il["line_no"] - 1, "illumination"),
        (f"sample_temporal_sonnet18_L{tl['line_no']}_59.svg", "sonnet18",
         tl["line_no"] - 1, "temporal"),
    ]


def main():
    FIG.mkdir(parents=True, exist_ok=True)
    staged, fails = [], []
    for name, board, li, field in samples():
        m = build_model(board, li, field)
        svg = render(m)
        f = gate(m, svg)
        if f:
            fails += [f"{name}: {x}" for x in f]
            print(f"GATE FAIL {name}")
            for x in f:
                print("   -", x)
        else:
            staged.append((name, svg, m))
            print(f"GATE PASS {name}")
    if fails:
        sys.exit(f"{len(fails)} gate failure(s) — NOTHING WRITTEN")
    for name, svg, m in staged:
        p = FIG / name
        p.write_text(svg, encoding="utf-8")
        (FIG / (name.replace(".svg", "") + ".model.json")).write_text(
            json.dumps(m, ensure_ascii=False, indent=1, default=str),
            encoding="utf-8")
        if subprocess.run(["xmllint", "--noout", str(p)],
                          capture_output=True).returncode != 0:
            sys.exit(f"xmllint FAIL {name}")
        print("wrote", p.name, "+ sidecar")
    print("ALL GATES PASSED; five exhibits + provenance sidecars on disk")


if __name__ == "__main__":
    main()
