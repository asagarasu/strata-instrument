#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
STRATA 2x2 demonstration (gc#110, 2026-10-31): construct-then-reverse-decode.
Builds on the gc#107 instrument as a LIBRARY (mdtest as M): same LaBSE snapshot,
same axis projection (score_descriptive_fields.project via M.D), same cosine
(dot of normalize_embeddings=True vectors), same cuts / z-norms / law states,
same re-order certificate (D.embed_inventory, seed 48) and zh sound anchor.

Stage 1 (--explore): embed the decode dictionary + source carrier word (+ anchor),
                     print the geometry needed to fix the cell targets.
Stage 2 (--run):     construct the four cell points, reverse-decode, fill the blank,
                     embed the filled lines (second certificate), write results.
"""
import json, re, sys, math
from pathlib import Path
import numpy as np

WORK = Path(__file__).resolve().parent
sys.path.insert(0, str(WORK / "instrument"))   # the instrument library lives in instrument/
import mdtest as M                      # the instrument library (reuses repo code verbatim)
D, LAW, FIELDS = M.D, M.LAW, M.FIELDS
OUT = WORK / "results"; OUT.mkdir(exist_ok=True)

SRC_LINE = "Dans une chaude lumière."       # Baudelaire, L'Invitation au voyage, L40 (board 'invitation')
SRC_WORD = "chaude"                         # the implicit-colour carrier (fires the colour meter, no fr inventory claims it)
BLANK = "In a {} light."                    # the scaffolded-translation blank (article follows the filler, see fill())
AN_EXCEPT_A = ("uni", "use", "usu", "eu", "one", "ubi", "ura", "uti")     # vowel letter, consonant sound → "a"
AN_EXCEPT_AN = ("hour", "honest", "honor", "heir")                         # silent h → "an"


def fill(w):
    """Fill the blank with the English article the filler takes (a / an)."""
    an = w[0] in "aeiou"
    if w.startswith(AN_EXCEPT_A): an = False
    if w.startswith(AN_EXCEPT_AN): an = True
    return ("In an {} light." if an else "In a {} light.").format(w)
VOCAB_MIN_COUNT = 50                        # Leipzig en news (1M sentences) frequency floor

# dictionary hygiene (stated before any decoding): standard English stopwords + ordinals/sequence words
STOP = set("""a about above after again against all am an and any are as at be because been before being below between both
but by can did do does doing down during each few for from further had has have having he her here hers herself him himself his
how i if in into is it its itself just me more most my myself no nor not now of off on once only or other our ours ourselves
out over own same she should so some such than that the their theirs them themselves then there these they this those through to
too under until up very was we were what when where which while who whom why will with you your yours yourself yourselves
many much several own same few certain enough another either neither every own whole""".split())
ORDINAL = set("first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth twentieth hundredth last next former latter".split())


def load_vocab():
    cnt = json.loads((WORK / "scratch" / "vocab_counts.json").read_text())
    words = sorted(w for w, c in cnt.items() if c >= VOCAB_MIN_COUNT and w not in STOP and w not in ORDINAL)
    return words


def embed(inv, cache_name, model):
    """D.embed_inventory (batch_size=1 + seed-48 re-order certificate), cached on identical inventory."""
    cache = OUT / cache_name
    if cache.exists():
        z = np.load(cache, allow_pickle=True)
        if list(z["inv"]) == inv:
            return z["E"], float(z["drift"]), True
    E, drift = D.embed_inventory(model, inv)
    np.savez(cache, E=E, inv=np.array(inv, dtype=object), drift=drift)
    return E, drift, False


def colour_dirs(axes):
    """Raw-space colour direction d (d @ W = axis exactly; W is symmetric ZCA whitening, so d = W^-1 axis)
    and the whitened-axis gradient direction g = W @ axis (directions orthogonal to g leave the
    pre-normalisation axis coordinate unchanged)."""
    a = axes["color"]
    d = np.linalg.solve(a["W"].T, a["axis"])
    g = a["W"] @ a["axis"]
    return d, g


def reading(e, axes, field="color"):
    """Colour-axis reading of raw (unit) embedding(s) e: exactly D.project on a 1- or 2-D array."""
    e2 = np.atleast_2d(e)
    return D.project(e2, {field: axes[field]})[field]


def main_explore():
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(str(M.LABSE), device="cpu")
    axes = D.load_axes()
    vocab = load_vocab()
    inv = [SRC_WORD] + vocab + [M.ANCHOR_TXT]
    E, drift, cached = embed(inv, "emb_words.npz", model)
    idx = {s: i for i, s in enumerate(inv)}
    proj = D.project(E, axes)
    print(f"dictionary: {len(vocab)} words; inventory {len(inv)}; certificate drift {drift:.2e} (cached={cached})")
    print(f"anchor |Δ| = {abs(float(proj['sound'][idx[M.ANCHOR_TXT]]) - M.ANCHOR_VAL):.2e}")
    s = E[idx[SRC_WORD]]
    rs = float(proj["color"][idx[SRC_WORD]])
    V = E[1:1 + len(vocab)]
    rv = proj["color"][1:1 + len(vocab)]
    cv = V @ s
    print(f"source word «{SRC_WORD}»: colour reading {rs:+.4f}; dictionary readings: mean {rv.mean():+.4f} sd {rv.std():.4f} "
          f"pcts 1/5/25/50/75/95/99 = {np.percentile(rv,[1,5,25,50,75,95,99]).round(4)}; source percentile rank {100*np.mean(rv<rs):.1f}")
    print(f"cos(word, {SRC_WORD}): max {cv.max():.3f} pcts 50/75/90/95/99 = {np.percentile(cv,[50,75,90,95,99]).round(3)}")
    order = np.argsort(-cv)
    print("nearest 30 words:", [(vocab[i], round(float(cv[i]),3), round(float(rv[i]),4)) for i in order[:30]])
    print("highest colour reading 20:", [(vocab[i], round(float(rv[i]),4), round(float(cv[i]),3)) for i in np.argsort(-rv)[:20]])
    print("lowest colour reading 20:", [(vocab[i], round(float(rv[i]),4), round(float(cv[i]),3)) for i in np.argsort(rv)[:20]])
    # joint geometry: among words with cos >= 95th pct, the reading range
    hi = cv >= np.percentile(cv, 95)
    print(f"words in top-5% cosine: n={hi.sum()}, reading range {rv[hi].min():+.4f}..{rv[hi].max():+.4f}, sd {rv[hi].std():.4f}")
    print("  those with lowest reading:", [(vocab[i], round(float(cv[i]),3), round(float(rv[i]),4)) for i in np.where(hi)[0][np.argsort(rv[hi])[:10]]])
    print("  those with highest reading:", [(vocab[i], round(float(cv[i]),3), round(float(rv[i]),4)) for i in np.where(hi)[0][np.argsort(-rv[hi])[:10]]])
    # how much cosine does the colour move cost? walk along d from s
    d, g = colour_dirs(axes)
    print(f"||d|| {np.linalg.norm(d):.4f}  ||g|| {np.linalg.norm(g):.2f}  cos(d,g) {d@g/np.linalg.norm(d)/np.linalg.norm(g):.3f}  cos(d,s) {d@s/np.linalg.norm(d):+.3f}")
    for alpha in (-6, -4, -2, -1, 0, 1, 2, 4, 6):
        p = s + alpha * d; p = p / np.linalg.norm(p)
        print(f"  alpha {alpha:+d}: reading {float(reading(p, axes)[0]):+.4f}  cos to source {float(p@s):.4f}")
    # and along the centroid direction (orthogonalised against s and g)
    c = V.mean(0); u = c - s; u -= (u @ s) * s; u -= (u @ g) * g / (g @ g); u /= np.linalg.norm(u)
    for beta in (0.25, 0.5, 1.0, 2.0):
        p = s + beta * u; p = p / np.linalg.norm(p)
        print(f"  beta {beta}: reading {float(reading(p, axes)[0]):+.4f}  cos to source {float(p@s):.4f}")
    # rank-1 dependence: Spearman of cosine vs reading over the dictionary
    rk = lambda x: np.argsort(np.argsort(x))
    print(f"Spearman(cos, reading) over dictionary: {np.corrcoef(rk(cv), rk(rv))[0,1]:+.3f}")




# ───────────────────────────── stage 2: the 2x2 (targets fixed by the rule below BEFORE any decoding)
# Target rule (stated, mechanical; percentiles are of the decode dictionary's own distributions):
#   axis NEAR  = the source carrier's own colour reading r_s
#   axis FAR   = the dictionary's P_FAR percentile of colour readings on the side of r_s with more room
#                (more room = larger gap between r_s and that side's extreme percentile)
#   cosine NEAR = the largest cosine any dictionary word has to the source (as close as a real word gets)
#   cosine FAR  = the dictionary's P_COS_FAR percentile of cosine-to-source (the ordinary dictionary word)
# Landing bands (fixed before decoding; a decoded word "lands" in its cell if its MEASURED coordinates satisfy both):
#   axis-near: |r_w - r_s| <= 1 dictionary SD of readings      axis-far: r_w beyond 2 dictionary SDs from r_s on the far side
#   cos-near:  cos_w >= dictionary 99th percentile (top 1 %)    cos-far:  cos_w <= dictionary 75th percentile
#   and the four decoded words must be distinct.
P_FAR = 95          # → 95th (gain side) or 5th (loss side)
P_COS_FAR = 50
BAND_NEAR_SD, BAND_FAR_SD, BAND_COS_NEAR_PCT, BAND_COS_FAR_PCT = 1.0, 2.0, 99, 75
CELLS = [("axis-near", "cos-near"), ("axis-far", "cos-near"), ("axis-near", "cos-far"), ("axis-far", "cos-far")]
REFERENCE = ["warm", "hot"]   # reference renderings reported beside the cells (not cells): the gc107 'faithful' line and the nearest word


def construct(s, d, u, axes, r_t, c_t):
    """p(α,β) = unit(s + α d + β u); solve reading(p)=r_t, cos(p,s)=c_t by least squares (β ≥ 0), several starts.
    Returns p, (α,β), achieved (reading, cos), residual norm."""
    from scipy.optimize import least_squares
    def pt(x):
        p = s + x[0] * d + x[1] * u
        return p / np.linalg.norm(p)
    def res(x):
        p = pt(x)
        return [float(reading(p, axes)[0]) - r_t, float(p @ s) - c_t]
    best = None
    for a0 in (-8, -4, -2, 0, 2, 4, 8):
        for b0 in (0.0, 0.3, 1.0, 3.0):
            try:
                sol = least_squares(res, x0=[a0, b0], bounds=([-np.inf, 0.0], [np.inf, np.inf]), xtol=1e-12, ftol=1e-12, gtol=1e-12)
            except Exception:
                continue
            if best is None or sol.cost < best.cost:
                best = sol
    p = pt(best.x)
    return p, (float(best.x[0]), float(best.x[1])), (float(reading(p, axes)[0]), float(p @ s)), float(np.linalg.norm(best.fun))


def decode_both(p, V, rv, r_p):
    """Two nearest-neighbour decodes of a constructed point p over the dictionary V (readings rv).
    raw : highest raw LaBSE cosine to p (the plain-cosine decode).
    axis: smallest standardised two-channel distance ((max_w cos(w,p) - cos(w,p)) / sd_w(cos(w,p)))^2 + ((r_w - r_p) / sd_w(r_w))^2,
          i.e. embedding similarity to p AND the colour-axis coordinate of p, each in dictionary-SD units. PRIMARY.
    Returns (raw_order, axis_order, sims, score)."""
    sims = V @ p
    # both terms = distance from the best value any dictionary word attains, in dictionary-SD units
    # (v1 used (1 - cos) for the first term; its large common offset inflated that term against the reading term,
    #  so cosine-far cells decoded to centroid hub words regardless of reading; superseded, recorded in METHOD_AND_RESULT.md)
    t1 = (sims.max() - sims) / sims.std()
    t2 = (rv - r_p) / rv.std()
    score = t1 ** 2 + t2 ** 2
    return np.argsort(-sims), np.argsort(score), sims, score


def main_run():
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(str(M.LABSE), device="cpu")
    axes = D.load_axes(); cuts = LAW.cuts(); nn = LAW.news_norms()
    vocab = load_vocab()
    inv1 = [SRC_WORD] + vocab + [M.ANCHOR_TXT]
    E1, drift1, _ = embed(inv1, "emb_words.npz", model)
    idx1 = {t: i for i, t in enumerate(inv1)}
    proj1 = D.project(E1, axes)
    anchor1 = float(proj1["sound"][idx1[M.ANCHOR_TXT]])
    s = E1[idx1[SRC_WORD]]; r_s = float(proj1["color"][idx1[SRC_WORD]])
    V = E1[1:1 + len(vocab)]; rv = proj1["color"][1:1 + len(vocab)]; cv = V @ s

    # ── targets by the rule
    lo, hi = np.percentile(rv, 100 - P_FAR), np.percentile(rv, P_FAR)
    far_side = "gain" if (hi - r_s) >= (r_s - lo) else "loss"
    r_far = float(hi if far_side == "gain" else lo)
    c_near, c_far = float(cv.max()), float(np.percentile(cv, P_COS_FAR))
    targets = {"axis-near": r_s, "axis-far": r_far, "cos-near": c_near, "cos-far": c_far}
    sd = float(rv.std()); cos99, cos75 = float(np.percentile(cv, BAND_COS_NEAR_PCT)), float(np.percentile(cv, BAND_COS_FAR_PCT))
    sign = 1.0 if far_side == "gain" else -1.0
    def lands(ax, co, r_w, c_w):
        ok_ax = (abs(r_w - r_s) <= BAND_NEAR_SD * sd) if ax == "axis-near" else (sign * (r_w - r_s) >= BAND_FAR_SD * sd)
        ok_co = (c_w >= cos99) if co == "cos-near" else (c_w <= cos75)
        return bool(ok_ax), bool(ok_co)
    print(f"source «{SRC_WORD}» reading {r_s:+.4f} (dictionary pct rank {100*np.mean(rv < r_s):.1f}); far side = {far_side}, r_far {r_far:+.4f}; "
          f"c_near {c_near:.4f} (nearest word «{vocab[int(np.argmax(cv))]}»), c_far {c_far:.4f}; bands: SD {sd:.4f}, cos99 {cos99:.4f}, cos75 {cos75:.4f}")
    print("news norms colour (mu, sigma): fr", nn["color"]["fr"], " en", nn["color"]["en"])

    # ── directions
    d, g = colour_dirs(axes)
    c = V.mean(0); u = c - s; u -= (u @ s) * s; u -= (u @ g) * g / (g @ g); u /= np.linalg.norm(u)

    # ── construct + decode
    cells = []
    for ax, co in CELLS:
        r_t, c_t = targets[ax], targets[co]
        p, (alpha, beta), (r_p, c_p), resid = construct(s, d, u, axes, r_t, c_t)
        raw_order, ax_order, sims, score = decode_both(p, V, rv, r_p)
        k = int(ax_order[0]); w = vocab[k]; kr = int(raw_order[0])
        def wm(i):
            return dict(word=vocab[int(i)], reading=float(rv[i]), cos_to_source=float(cv[i]), cos_to_point=float(sims[i]),
                        reading_pct=float(100 * np.mean(rv < rv[i])), cos_pct=float(100 * np.mean(cv < cv[i])),
                        reading_sd_from_source=float((rv[i] - r_s) / sd))
        cells.append(dict(cell=f"({ax}, {co})", axis_level=ax, cos_level=co,
                          target=dict(reading=r_t, cos=c_t),
                          construction=dict(alpha=alpha, beta=beta, achieved_reading=r_p, achieved_cos=c_p, residual=resid),
                          decoded=w, decode_metric="axis-aware (primary)", decode_score=float(score[k]), decode_cos_to_point=float(sims[k]),
                          runners_up_axis=[(vocab[int(i)], round(float(score[i]), 3), round(float(rv[i]), 4), round(float(cv[i]), 4)) for i in ax_order[1:6]],
                          raw_decode=wm(kr), raw_runners_up=[(vocab[int(i)], round(float(sims[i]), 4), round(float(rv[i]), 4)) for i in raw_order[1:6]],
                          word_measured=wm(k),
                          lands=dict(zip(("axis", "cos"), lands(ax, co, float(rv[k]), float(cv[k])))),
                          raw_lands=dict(zip(("axis", "cos"), lands(ax, co, float(rv[kr]), float(cv[kr]))))))
        print(f"{cells[-1]['cell']}: target (r {r_t:+.4f}, c {c_t:.4f}) → constructed (r {r_p:+.4f}, c {c_p:.4f}; α {alpha:+.2f} β {beta:.3f}, resid {resid:.1e})")
        print(f"    raw-cosine decode «{vocab[kr]}» (cos to p {sims[kr]:.3f}; measured r {rv[kr]:+.4f}, c {cv[kr]:.4f}; lands {cells[-1]['raw_lands']}); runners-up {cells[-1]['raw_runners_up'][:3]}")
        print(f"    axis-aware decode «{w}» (score {score[k]:.3f}, cos to p {sims[k]:.3f}; measured r {rv[k]:+.4f} = {(rv[k]-r_s)/sd:+.2f} SD, c {cv[k]:.4f} pct {100*np.mean(cv < cv[k]):.1f}; lands {cells[-1]['lands']}); runners-up {cells[-1]['runners_up_axis'][:3]}")

    distinct = len({ce["decoded"] for ce in cells}) == 4
    print("four decoded words distinct:", distinct, " landed:", [(ce["cell"], ce["lands"]) for ce in cells])
    refs = []
    for w in REFERENCE:
        i = vocab.index(w)
        refs.append(dict(word=w, word_measured=dict(reading=float(rv[i]), cos_to_source=float(cv[i]), reading_pct=float(100 * np.mean(rv < rv[i])),
                                                   cos_pct=float(100 * np.mean(cv < cv[i])), reading_sd_from_source=float((rv[i] - r_s) / sd))))
    # ── stage-2 inventory: the filled lines (+ deletion masks), the source line (+ masks), every dictionary line, anchor
    inv2, idx2 = [], {}
    def add(t):
        if t not in idx2:
            idx2[t] = len(inv2); inv2.append(t)
    def add_line(t):
        add(t)
        for un in D.maskable_units(t):
            add(D.delete_unit(t, un))
    add_line(SRC_LINE); add(SRC_WORD)
    for w in REFERENCE:
        add_line(fill(w))
    for w in vocab:
        add(fill(w))
    add(M.ANCHOR_TXT)
    E2, drift2, _ = embed(inv2, "emb_lines.npz", model)          # decode-independent inventory (cacheable)
    # stage 3: the four decoded lines with their deletion masks (+ anchor), own certificate
    inv3, idx3 = [], {}
    for ce in cells:
        t = fill(ce["decoded"])
        for x in [t] + [D.delete_unit(t, un) for un in D.maskable_units(t)]:
            if x not in idx3:
                idx3[x] = len(inv3); inv3.append(x)
    if M.ANCHOR_TXT not in idx3:
        idx3[M.ANCHOR_TXT] = len(inv3); inv3.append(M.ANCHOR_TXT)
    E3, drift3, _ = embed(inv3, "emb_decoded_lines.npz", model)
    anchor3 = float(D.project(E3, axes)["sound"][idx3[M.ANCHOR_TXT]])
    # merge stage 2 + 3 into one lookup (texts present in both must agree: deterministic encoder)
    for t, i in idx3.items():
        if t in idx2:
            assert float(np.abs(E2[idx2[t]] - E3[i]).max()) < 1e-6, t
        else:
            idx2[t] = len(inv2); inv2.append(t); E2 = np.vstack([E2, E3[i][None, :]])
    proj2 = D.project(E2, axes)
    anchor2 = float(proj2["sound"][idx2[M.ANCHOR_TXT]])
    print(f"certificates: stage-1 words drift {drift1:.2e} anchor|Δ| {abs(anchor1 - M.ANCHOR_VAL):.2e}; stage-2 lines drift {drift2:.2e} anchor|Δ| {abs(anchor2 - M.ANCHOR_VAL):.2e}; "
          f"stage-3 decoded lines drift {drift3:.2e} anchor|Δ| {abs(anchor3 - M.ANCHOR_VAL):.2e}")

    # replay check of the committed source row (board invitation, fr:baudelaire_1861, L40)
    cm = M.committed_row("invitation", "fr:baudelaire_1861", 40); assert cm["text"] == SRC_LINE
    src_row = M.row_from(E2, idx2, proj2, SRC_LINE)
    replay = dict(max_dreading=max(abs(src_row["reading"][f] - cm["reading"][f]) for f in FIELDS),
                  carrier_delta_committed=dict(cm["top_delta"]["color"]).get(SRC_WORD), carrier_delta_mine=dict(src_row["top_delta"]["color"]).get(SRC_WORD))
    src_st = M.states_for(src_row, "fr", cuts)
    s_line = E2[idx2[SRC_LINE]]
    print(f"replay vs committed row: max|Δreading| {replay['max_dreading']:.2e}; carrier colour Δ committed {replay['carrier_delta_committed']:+.5f} mine {replay['carrier_delta_mine']:+.5f}; source colour state {src_st['color']['state']}")

    # line-level geometry over the whole dictionary (what a sentence-level metric sees)
    L = np.array([E2[idx2[fill(w)]] for w in vocab])
    rl = D.project(L, {"color": axes["color"]})["color"]; cl = L @ s_line
    zl = (rl - nn["color"]["en"][0]) / nn["color"]["en"][1]
    src_z_fr = (src_row["reading"]["color"] - nn["color"]["fr"][0]) / nn["color"]["fr"][1]
    def line_measure(w):
        line = fill(w); row = M.row_from(E2, idx2, proj2, line); st = M.states_for(row, "en", cuts); i = vocab.index(w)
        return line, dict(cos_line=float(cl[i]), reading=float(rl[i]), z_en=float(zl[i]),
                          reading_pct=float(100 * np.mean(rl < rl[i])), cos_pct=float(100 * np.mean(cl < cl[i])),
                          colour_state=st["color"]["state"], colour_receipts=st["color"]["word_receipts"],
                          colour_triggered=[t for t, _ in st["color"]["triggered"]],
                          cell_vs_source=M.cell(src_st["color"]["state"], st["color"]["state"]),
                          filler_colour_delta=dict(row["top_delta"]["color"]).get(w),
                          illum_state=st["illumination"]["state"], dz_vs_source_colour=M.zshift(src_row, row, "en", nn)["color"])
    for ce in cells:
        ce["translation"], ce["line_measured"] = line_measure(ce["decoded"]); lm = ce["line_measured"]
        print(f"{ce['cell']} «{ce['translation']}»: cos_line {lm['cos_line']:.4f} (pct {lm['cos_pct']:.0f}), reading {lm['reading']:+.4f} z_en {lm['z_en']:+.2f} (pct {lm['reading_pct']:.0f}), "
              f"state {lm['colour_state']} cell {lm['cell_vs_source']}, filler Δ {lm['filler_colour_delta']}, triggered {lm['colour_triggered']}")
    for rf in refs:
        rf["translation"], rf["line_measured"] = line_measure(rf["word"]); lm = rf["line_measured"]
        print(f"reference «{rf['translation']}»: word (r {rf['word_measured']['reading']:+.4f}, c {rf['word_measured']['cos_to_source']:.4f}); cos_line {lm['cos_line']:.4f}, z_en {lm['z_en']:+.2f}, state {lm['colour_state']} cell {lm['cell_vs_source']}, filler Δ {lm['filler_colour_delta']}")

    out = dict(meta=dict(instrument="gc107 mdtest (import mdtest as M): LaBSE from M.LABSE, D.project, D.embed_inventory certificate, LAW cuts/news_norms/line_state/CELL15",
                         encoder="sentence-transformers/LaBSE (gc107 snapshot, weights sha = committed pin)", device="cpu", batch_size=1,
                         dictionary=dict(rule=f"WordNet 3.0 adjective lemmas (single lowercase alphabetic token, len>=3) with >= {VOCAB_MIN_COUNT} occurrences in the 1M-sentence Leipzig English news file; minus a stated stopword list and ordinal/sequence words",
                                         n=len(vocab), stop_removed=sorted(STOP), ordinal_removed=sorted(ORDINAL)),
                         source=dict(line=SRC_LINE, word=SRC_WORD, blank=BLANK, article_rule="a/an by first letter with exceptions " + str(AN_EXCEPT_A) + " / " + str(AN_EXCEPT_AN), word_reading=r_s, word_reading_pct=float(100 * np.mean(rv < r_s)),
                                     line_reading=src_row["reading"]["color"], line_z_fr=float(src_z_fr), line_colour_state=src_st["color"]["state"],
                                     line_colour_triggered=[t for t, _ in src_st["color"]["triggered"]]),
                         targets=dict(rule=dict(P_FAR=P_FAR, cos_near="max dictionary cosine", P_COS_FAR=P_COS_FAR, far_side=far_side), values=targets,
                                      dictionary_reading_pcts={str(p): float(np.percentile(rv, p)) for p in (1, 5, 25, 50, 75, 95, 99)},
                                      dictionary_cos_pcts={str(p): float(np.percentile(cv, p)) for p in (1, 5, 25, 50, 75, 95, 99)}),
                         construction=dict(d="raw-space colour direction, d = W^-1 axis (so d@W = axis exactly; W is the symmetric ZCA whitening of the colour axis npz)",
                                           u="unit(centroid(dictionary) - s) orthogonalised against s and against g = W@axis (so moving along u leaves the pre-normalisation axis coordinate unchanged)",
                                           point="p(α,β) = unit(s + α d + β u), (α,β) solved by least squares for reading(p)=r_target and cos(p,s)=c_target, β ≥ 0",
                                           decode="dictionary word with the highest cosine to p (top-1; runners-up listed for information only)",
                                           norm_d=float(np.linalg.norm(d)), norm_g=float(np.linalg.norm(g)), cos_d_g=float(d @ g / np.linalg.norm(d) / np.linalg.norm(g))),
                         certificate=dict(stage1_words=dict(n_inventory=len(inv1), drift=drift1, anchor_abs_delta=abs(anchor1 - M.ANCHOR_VAL)),
                                          stage2_lines=dict(n_inventory=len(inv2), drift=drift2, anchor_abs_delta=abs(anchor2 - M.ANCHOR_VAL)),
                                          stage3_decoded_lines=dict(n_inventory=len(inv3), drift=drift3, anchor_abs_delta=abs(anchor3 - M.ANCHOR_VAL))),
                         decode=dict(primary="axis-aware v2: argmin ((max cos(.,p) - cos(w,p))/sd(cos(.,p)))^2 + ((r_w - r_p)/sd(r))^2 over the dictionary",
                                     baseline="raw: argmax cos(w,p); recorded per cell as raw_decode (degenerate: the colour displacement is invisible to it)"),
                         replay_committed_source_row=replay, cuts={f: v[0] for f, v in cuts.items()},
                         line_level_dictionary=dict(n=len(vocab), cos_line_pcts={str(p): float(np.percentile(cl, p)) for p in (1, 5, 25, 50, 75, 95, 99)},
                                                    z_en_pcts={str(p): float(np.percentile(zl, p)) for p in (1, 5, 25, 50, 75, 95, 99)})),
               cells=cells, references=refs, distinct_decodes=distinct,
               landing_bands=dict(axis_near_within_sd=BAND_NEAR_SD, axis_far_beyond_sd=BAND_FAR_SD, cos_near_pct=BAND_COS_NEAR_PCT, cos_far_pct=BAND_COS_FAR_PCT,
                                  dictionary_sd=sd, cos99=cos99, cos75=cos75))
    (OUT / "twobytwo_results.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    # dictionary scatter for the record (word level and line level)
    rows = ["word\tcos_word\treading_word\tcos_line\treading_line\tz_en_line"]
    for i, w in enumerate(vocab):
        rows.append(f"{w}\t{cv[i]:.4f}\t{rv[i]:+.4f}\t{cl[i]:.4f}\t{rl[i]:+.4f}\t{zl[i]:+.3f}")
    (OUT / "dictionary_coords.tsv").write_text("\n".join(rows))
    print("wrote", OUT / "twobytwo_results.json", "and", OUT / "dictionary_coords.tsv")


if __name__ == "__main__":
    if "--explore" in sys.argv:
        main_explore()
    elif "--run" in sys.argv:
        main_run()
    else:
        print("use --explore (stage 1) or --run (stage 2)")
