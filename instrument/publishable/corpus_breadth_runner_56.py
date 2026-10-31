#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
e7 CORPUS-BREADTH MASS-SCORING — orchestration runner (#56, 2026-07-23).

Spec of record: `engine/registrations/corpus_breadth_scoring_registration_56.md`
(committed BEFORE any run, house law — the F3 lesson: assertions on
OUTPUTS). Plan: `engine/VIGIL_PLAN_56.md` P1.

═══ WHAT THIS IS (registration §A) ═══
ORCHESTRATION ONLY. This runner creates NO instrument, axis, lexicon,
carrier inventory, threshold, or comparator. It imports the two committed
row scorers VERBATIM and feeds them per-poem boards + per-file verse
parse specs:
  - ../deterministic-descriptive-fields/score_descriptive_fields.py (D):
    load_axes, scalar_readings, boolean_states, poem_inventory,
    transition_table/survival_rates, input_manifest, verse_lines, sha256,
    F9 redaction pattern (mode_run), SEED, CJK, BOOL_COVERED_LANGS.
  - ../deterministic-latent-written-fields/latent_score_54.py (L):
    written_row_line, referent_row_line, _sensors, the check-1 /
    fires_three_check application + poem-fold + RC.compare latent-slot
    generalisation (its mode_run), F9 redaction pattern.
NO LLM MARKS ANYTHING. Determinism law verbatim: batch_size=1, seed 48,
re-order certificate < 1e-6 per board, sha-pinned manifests.

═══ BOARDS (registration §C) ═══
sonnet18 · qingqing · albatros · correspondances. Seats, tiers, parse
specs, expected counts, and source langs are the PARSE_SPECS + BOARDS
tables below — frozen from §C (dry-marked counts filled at chair
sign-off). s18 source=en (transitions en↔zh ×4); qingqing source=zh
(transitions zh↔en ×n_en); albatros/correspondances source=fr (fr has no
boolean shelf, F2 → transitions DECLARED NOT RUNNABLE, never emitted
empty; scalars + per-rendering states + zh written-latent still land).

═══ PARSE LAW (registration §C) ═══
Per-file spec, one of:
  [S] single-block — the pilot's committed `verse_lines` final-block rule
      (imported verbatim from D). Works for the fenced .txt (==== header,
      bare number, verse) and the single-stanza .md.
  [M] all-verse-blocks-after-header — header block = any block whose first
      line starts '#' / '**' / contains a line starting '===='. Exclude
      trailing blocks whose first line starts '*(' / '*' (italic note /
      attribution) / '#' (markdown section). Also drop leading singleton
      blocks that are a bare number line (arabic/CJK/roman) or an all-caps
      Latin title (the fenced-.txt title block, e.g. II / L'ALBATROS).
      Bare number lines dropped inside verse via the committed numre
      regex (replicated). Multi-stanza safe.
  [X] explicit block — select the block whose FIRST line starts with a
      registered first-line prefix (files with prose FINDING sections,
      e.g. giles/heilmann); everything else excluded.

Every parsed seat: assert count == registered count where registered.
At --run a mismatch ABORTS that board (fix parse spec = one retry, else
drop-and-declare — never silently mis-parse). At --dry it is REPORTED.

═══ F9 REDACTION (registration §C/§D, verbatim from D.mode_run/L.mode_run) ═══
For every tier=local seat, the line text is nulled in ALL outputs:
descriptive readings rows' "text" -> None + a note (mirroring D.mode_run);
latent structures carry no line text (mirroring L.mode_run). --verify B
mechanically re-opens the board's outputs and greps them for EVERY raw
line string of every local-tier input file — any hit = FAIL (offending
path printed, nonzero exit).

═══ OUTPUTS (registration §D) ═══
Per board <b> ∈ {sonnet18,qingqing,albatros,correspondances}:
  ../deterministic-descriptive-fields/descriptive_scores_<b>_56.{json,md}
  ../deterministic-latent-written-fields/latent_scores_<b>_56.json
Manifests carry: input shas (D.input_manifest + latent carrier shas the
way L.mode_run pins them) + sha256 of every corpus file + parse spec +
parsed count per seat + seed + certificate drift + inventory size +
seats present/missing. The human .md table mirrors the pilot's
_write_human_table shape (redacted rows marked).

═══ CLI ═══
  --dry [--board B]     real corpus, no encoder: parse counts + first/last
                        parsed line + fires preview + shas (no writes)
  --run [--board B]     REAL run: certificate < 1e-6 or abort the board;
                        skip-if-exists = json present AND --verify passes
                        -> SKIP. Boards run in fixed order when --board
                        absent. (Fired by the orchestrator AFTER review.)
  --verify B            re-open board B's outputs, assert §E.2-5 on them.

Style follows the two committed scorers: module docstring citing the
registration by path + section, __main__ guard, sorted iteration
everywhere, determinism-pinned.
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------- paths
HERE = Path(__file__).resolve().parent            # publishable/
REPO = HERE.parent                                # repo root (instrument/)
DESC = HERE / "deterministic-descriptive-fields"
LAT = HERE / "deterministic-latent-written-fields"
PROTO = REPO / "engine"
RESULTS = PROTO / "results"
MODELS = PROTO / "models"
MARK_TOOLS = REPO / "marking" / "tools"
CORPUS = REPO / "corpus"
# LOCAL_TIER root (F9, in-copyright acquisitions kept OUTSIDE this repo).
# Overridable: export STRATA_LOCAL_CORPUS=<your acquisitions root> (sub-layout
# <translator>/sonnet_NN.md). score_descriptive_fields.py honours the SAME
# variable; unset, the in-copyright seats list as MISSING.
LOCAL = Path(os.environ.get(
    "STRATA_LOCAL_CORPUS",
    str(REPO / "acquisitions" / "transcriptions")))

# import the two committed scorers VERBATIM (sys.path insertion the way
# latent_score_54.py does it — each scorer's own module-level path setup is
# REPO-relative and resolves correctly from here). linegrain_law_60 is the
# census LAW, a sibling in this same folder: imported for its trad→simp Unihan
# fold, which this runner used to carry as a private copy (#71 dedup).
sys.path.insert(0, str(DESC))
sys.path.insert(0, str(LAT))
sys.path.insert(0, str(MARK_TOOLS))
sys.path.insert(0, str(PROTO))
sys.path.insert(0, str(HERE))
import score_descriptive_fields as D            # noqa: E402
import latent_score_54 as L                     # noqa: E402
from linegrain_law_60 import fold               # noqa: E402

SEED = D.SEED
FORCE_RERUN = False   # set by --force (same-session rule-change reruns)
FIELDS5 = ["color", "illumination", "sound", "plant", "temporal"]

# committed numre (replicated per task: "reuse the committed numre logic by
# replicating the regex only"). D.verse_lines uses r"^[0-9〇一-九十百]+$".
NUMRE = re.compile(r"^[0-9〇一-九十百]+$")
# roman-numeral singleton (the fenced-.txt poem-number block, e.g. II / IV)
ROMANRE = re.compile(r"^[IVXLCDM]+$")


# ============================================================ boards (§C)
# Each seat = dict(rid, path, tier, spec, exp). spec ∈ {"S","M","X"}.
# exp = registered expected line count, or None ("dry" — frozen at chair
# sign-off). X seats carry "prefix" (registered first-line prefix string).
# tier "local" -> F9 redaction. Paths resolved against REPO (repo) or LOCAL.

def _repo(p):
    return CORPUS / p


def _loc(p):
    return LOCAL / p


def _de_ensemble(folder, names):
    return [dict(rid=f"de:{n.split('_')[0]}", path=_repo(f"ensemble/{folder}/{n}.md"),
                 tier="repo", spec="S", exp=14) for n in names]


BOARDS = {
    # ---- Board s18 — source en, transitions en↔zh (4) — pilot-mirror ----
    "sonnet18": {
        "source_lang": "en",
        "source_rid": "en:shakespeare_1609",
        "seats": [
            dict(rid="en:shakespeare_1609",
                 path=_repo("sonnets/en_source/shakespeare_sonnet18_1609.txt"),
                 tier="repo", spec="S", exp=14),
            dict(rid="zh:liang_zongdai", path=_loc("liang_zongdai_sonnets/sonnet_18.md"),
                 tier="local", spec="S", exp=14),
            dict(rid="zh:tu_an_1955", path=_loc("tu_an_sonnets/sonnet_18.md"),
                 tier="local", spec="S", exp=14),
            dict(rid="zh:liang_shiqiu", path=_loc("liang_shiqiu/sonnet_18.md"),
                 tier="local", spec="S", exp=14),
            dict(rid="zh:gu_zhengkun", path=_loc("gu_zhengkun/sonnet_18.md"),
                 tier="local", spec="S", exp=14),
            dict(rid="de:bodenstedt_1862", path=_repo("ensemble/sonnet_18/bodenstedt_de_1862.md"),
                 tier="repo", spec="S", exp=14),
            dict(rid="de:george_1909", path=_repo("ensemble/sonnet_18/george_de_1909.md"),
                 tier="repo", spec="S", exp=14),
            dict(rid="de:gildemeister_1871", path=_repo("ensemble/sonnet_18/gildemeister_de_1871.md"),
                 tier="repo", spec="S", exp=14),
            dict(rid="de:regis_1836", path=_repo("ensemble/sonnet_18/regis_de_1836.md"),
                 tier="repo", spec="S", exp=14),
            dict(rid="de:wolff_1903", path=_repo("ensemble/sonnet_18/wolff_de_1903.md"),
                 tier="repo", spec="S", exp=14),
            dict(rid="jp:tsubouchi", path=_repo("sonnets/jp_target/tsubouchi_sonnet18.txt"),
                 tier="repo", spec="S", exp=14),
            dict(rid="zh:google_translate", path=_repo("gt_seats_0727/gt_zh_sonnet18.txt"),
                 tier="repo", spec="S", exp=14),  # her-hand acquisition 07-27, GT appendix
        ],
    },
    # ---- Board qingqing — source zh, transitions zh↔en (≤6) ----
    "qingqing": {
        "source_lang": "zh",
        "source_rid": "zh:gushi19_02",
        "seats": [
            dict(rid="zh:gushi19_02",
                 path=_repo("tang_en/zh_source/gushi19shou_02_qingqing_hepan_cao.txt"),
                 tier="repo", spec="S", exp=10),
            dict(rid="en:giles_1898", path=_repo("ensemble/qingqing_hepancao/giles_en_1898.md"),
                 tier="repo", spec="X", prefix="Green grows", exp=10),
            dict(rid="en:birrell", path=_loc("birrell_jade_terrace/qingqing_hepan_cao.md"),
                 tier="local", spec="M", exp=10),
            dict(rid="en:owen", path=_loc("owen_norton/qingqing_hepan_cao.md"),
                 tier="local", spec="M", exp=None),
            dict(rid="en:watson", path=_loc("watson_chinese_lyricism/qingqing_hepan_cao.md"),
                 tier="local", spec="M", exp=None),
            dict(rid="en:xu_yuanchong", path=_loc("xu_yuanchong/qingqing_hepan_cao.md"),
                 tier="local", spec="M", exp=None),
            dict(rid="en:pound_1915", path=_repo("ensemble/qingqing_hepancao/pound_en_1915.md"),
                 tier="repo", spec="M", exp=9),
            dict(rid="en:waley_1918", path=_repo("ensemble/qingqing_hepancao/waley_en_1918.md"),
                 tier="repo", spec="M", exp=16),   # §B.2 est. ~17-18; poem body is 16 (SPEC-FLAG)
            dict(rid="de:heilmann_1905", path=_repo("ensemble/qingqing_hepancao/heilmann_de_1905.md"),
                 tier="repo", spec="X", prefix="Grüner Rasen", exp=10),
            dict(rid="de:bethge_1907", path=_repo("ensemble/qingqing_hepancao/bethge_de_1907.md"),
                 tier="repo", spec="M", exp=15),
        ],
    },
    # ---- Board albatros — source fr, transitions NOT RUNNABLE (F2) ----
    "albatros": {
        "source_lang": "fr",
        "source_rid": "fr:baudelaire_1861",
        "seats": [
            dict(rid="fr:baudelaire_1861", path=_repo("baudelaire/fr_source/albatros_fr_1861.txt"),
                 tier="repo", spec="M", exp=16),
            dict(rid="zh:dai_wangshu", path=_loc("dai_wangshu/xintianweng_albatros.md"),
                 tier="local", spec="M", exp=16),
            dict(rid="zh:qian_chunqi", path=_loc("qian_chunqi/xintianweng.md"),
                 tier="local", spec="M", exp=16),
            dict(rid="zh:guo_hongan", path=_loc("guo_hongan/xintianweng.md"),
                 tier="local", spec="M", exp=16),
            dict(rid="en:campbell", path=_loc("campbell/albatross.md"),
                 tier="local", spec="M", exp=16),
            dict(rid="en:aggeler", path=_loc("aggeler/albatross.md"),
                 tier="local", spec="M", exp=16),
            # registration glob {mathews_1955_complete}/albatross*.md ->
            # actual file albatross_wilbur.md (SPEC-FLAG: filename resolved)
            dict(rid="en:wilbur", path=_loc("mathews_1955_complete/albatross_wilbur.md"),
                 tier="local", spec="M", exp=16),
            dict(rid="en:dillon", path=_loc("dillon_millay/albatross_dillon.md"),
                 tier="local", spec="M", exp=16),
            dict(rid="en:leclercq", path=_loc("leclercq/albatrosses.md"),
                 tier="local", spec="M", exp=16),
            dict(rid="de:george_1901", path=_repo("ensemble/baudelaire_albatros/george_de_1901.md"),
                 tier="repo", spec="M", exp=16),
            dict(rid="de:kalckreuth_1907", path=_repo("ensemble/baudelaire_albatros/kalckreuth_de_1907.md"),
                 tier="repo", spec="M", exp=16),
        ],
    },
    # ---- Board correspondances — source fr, transitions NOT RUNNABLE ----
    "correspondances": {
        "source_lang": "fr",
        "source_rid": "fr:baudelaire_1861",
        "seats": [
            dict(rid="fr:baudelaire_1861", path=_repo("baudelaire/fr_source/correspondances_fr_1861.txt"),
                 tier="repo", spec="M", exp=14),
            dict(rid="zh:dai_wangshu", path=_loc("dai_wangshu/yinghe_correspondances.md"),
                 tier="local", spec="M", exp=14),
            dict(rid="zh:qian_chunqi", path=_loc("qian_chunqi/ganying_correspondances.md"),
                 tier="local", spec="M", exp=14),
            dict(rid="zh:guo_hongan", path=_loc("guo_hongan/yinghe_correspondances.md"),
                 tier="local", spec="M", exp=14),
            dict(rid="en:sturm_1906", path=_repo("baudelaire/en_target/sturm_correspondences_1906.txt"),
                 tier="repo", spec="M", exp=14),
            dict(rid="en:scott_1909", path=_repo("baudelaire/en_target/scott_echoes_correspondances_1909.txt"),
                 tier="repo", spec="M", exp=14),
            dict(rid="en:campbell", path=_loc("campbell/correspondences.md"),
                 tier="local", spec="M", exp=14),
            dict(rid="en:aggeler", path=_loc("aggeler/correspondences.md"),
                 tier="local", spec="M", exp=14),
            dict(rid="en:wilbur", path=_loc("mathews_1955_complete/correspondences_wilbur.md"),
                 tier="local", spec="M", exp=14),
            dict(rid="en:dillon", path=_loc("dillon_millay/correspondences_dillon.md"),
                 tier="local", spec="M", exp=14),
            dict(rid="en:leclercq", path=_loc("leclercq/correspondences.md"),
                 tier="local", spec="M", exp=14),
            dict(rid="de:george_1901", path=_repo("ensemble/baudelaire_correspondances/george_de_1901.md"),
                 tier="repo", spec="M", exp=14),
        ],
    },
    # ---- DAY-SLATE BOARDS (#56 07-23, registration §H — her approved slate) ----
    # ---- Board tiaotiao — source zh, transitions zh↔en ----
    "tiaotiao": {
        "source_lang": "zh",
        "source_rid": "zh:gushi19_10",
        "seats": [
            dict(rid="zh:gushi19_10",
                 path=_repo("tang_en/zh_source/gushi19shou_10_tiaotiao_qianniuxing.txt"),
                 tier="repo", spec="S", exp=10),
            dict(rid="en:owen", path=_loc("owen_norton/tiaotiao_qianniuxing.md"),
                 tier="local", spec="M", exp=10),
            dict(rid="en:xu_yuanchong", path=_loc("xu_yuanchong/tiaotiao_qianniuxing.md"),
                 tier="local", spec="M", exp=10),
            dict(rid="en:birrell", path=_loc("birrell_jade_terrace/tiaotiao_qianniuxing.md"),
                 tier="local", spec="M", exp=10),
            dict(rid="en:watson", path=_loc("watson_columbia/tiaotiao_qianniuxing.md"),
                 tier="local", spec="M", exp=10, nblocks=1),  # verse=1 block; headnote/flags sections after --- stay unparsed
            dict(rid="en:waley_1918", path=_repo("ensemble/tiaotiao_qianniuxing/waley_en_1918.md"),
                 tier="repo", spec="M", exp=10),
            dict(rid="de:forke_1899", path=_repo("ensemble/tiaotiao_qianniuxing/forke_de_1899.md"),
                 tier="repo", spec="M", exp=20, nblocks=5),  # 5 short-line quatrains; trailing prose cut by nblocks (§H dry fix)
            dict(rid="en:google_translate", path=_repo("gt_seats_0727/gt_en_tiaotiao.txt"),
                 tier="repo", spec="S", exp=10),  # was exp=9 (GT fused L1+L2,
                 # declared); HER HAND split the fusion 07-28 ("I gave GT one
                 # line break") — seat now index-aligned; dated amendment in
                 # corpus_appendix_gt_seats_20260727_59.md
        ],
    },
    # ---- Board xibei — source zh, transitions zh↔en ----
    "xibei": {
        "source_lang": "zh",
        "source_rid": "zh:gushi19_05",
        "seats": [
            dict(rid="zh:gushi19_05",
                 path=_repo("tang_en/zh_source/gushi19shou_05_xibei_you_gaolou.txt"),
                 tier="repo", spec="S", exp=16),
            dict(rid="en:owen", path=_loc("owen_norton/xibei_you_gaolou.md"),
                 tier="local", spec="M", exp=16),
            dict(rid="en:xu_yuanchong", path=_loc("xu_yuanchong/xibei_you_gaolou.md"),
                 tier="local", spec="M", exp=16),
            dict(rid="en:birrell", path=_loc("birrell_jade_terrace/xibei_you_gaolou.md"),
                 tier="local", spec="M", exp=16),
            dict(rid="en:watson", path=_loc("watson_columbia/xibei_you_gaolou.md"),
                 tier="local", spec="M", exp=16, nblocks=1),  # verse=1 block; footnote/flags sections stay unparsed
            dict(rid="en:waley_1918", path=_repo("ensemble/xibei_you_gaolou/waley_en_1918.md"),
                 tier="repo", spec="M", exp=16),
            dict(rid="en:google_translate", path=_repo("gt_seats_0727/gt_en_xibei.txt"),
                 tier="repo", spec="S", exp=16),  # her-hand acquisition 07-27, GT appendix
        ],
    },
    # ---- Board invitation — source fr, transitions NOT RUNNABLE (F2) ----
    "invitation": {
        "source_lang": "fr",
        "source_rid": "fr:baudelaire_1861",
        "seats": [
            dict(rid="fr:baudelaire_1861",
                 path=_repo("baudelaire/fr_source/invitation_au_voyage_fr_1861.txt"),
                 tier="repo", spec="M", exp=42),
            dict(rid="zh:dai_wangshu", path=_loc("dai_wangshu/yaolv_invitation.md"),
                 tier="local", spec="M", exp=42),
            dict(rid="zh:qian_chunqi", path=_loc("qian_chunqi/invitation.md"),
                 tier="local", spec="M", exp=42),
            dict(rid="zh:guo_hongan", path=_loc("guo_hongan/invitation.md"),
                 tier="local", spec="M", exp=41),     # 郭's stanza-3 = 11 lines (restructure, §H)
            dict(rid="en:campbell", path=_loc("campbell/invitation.md"),
                 tier="local", spec="M", exp=42),
            dict(rid="en:aggeler", path=_loc("aggeler/invitation.md"),
                 tier="local", spec="M", exp=42),
            dict(rid="en:wilbur", path=_loc("mathews_1955_complete/invitation_wilbur.md"),
                 tier="local", spec="M", exp=42),
            dict(rid="en:millay", path=_loc("dillon_millay/invitation_millay.md"),
                 tier="local", spec="M", exp=42),     # dry-pinned 42; the report's 46 counted artifacts (§H)
        ],
    },
    # ---- Board elevation — source fr, transitions NOT RUNNABLE (F2) ----
    "elevation": {
        "source_lang": "fr",
        "source_rid": "fr:baudelaire_1861",
        "seats": [
            dict(rid="fr:baudelaire_1861",
                 path=_repo("baudelaire/fr_source/elevation_fr_1861.txt"),
                 tier="repo", spec="M", exp=20),
            dict(rid="zh:dai_wangshu", path=_loc("dai_wangshu/gaoju_elevation.md"),
                 tier="local", spec="M", exp=20),
            dict(rid="zh:qian_chunqi", path=_loc("qian_chunqi/elevation.md"),
                 tier="local", spec="M", exp=20),
            dict(rid="zh:guo_hongan", path=_loc("guo_hongan/elevation.md"),
                 tier="local", spec="M", exp=20),
            dict(rid="en:campbell", path=_loc("campbell/elevation.md"),
                 tier="local", spec="M", exp=20),
            dict(rid="en:aggeler", path=_loc("aggeler/elevation.md"),
                 tier="local", spec="M", exp=20),
            dict(rid="en:dillon", path=_loc("dillon_millay/elevation_dillon.md"),
                 tier="local", spec="M", exp=20),
            # mathews_1955_complete/elevation_campbell.md = cross-witness of the
            # seated Campbell rendering — NOT a second seat (§H: one slot/translator)
        ],
    },
}
BOARD_ORDER = ["sonnet18", "qingqing", "albatros", "correspondances",
               "tiaotiao", "xibei", "invitation", "elevation"]


def seat_lang(seat):
    return seat["rid"].split(":", 1)[0]


# ============================================================ PARSE SPECS
def _blocks(path):
    """Blank-separated blocks of stripped non-empty lines (D.verse_lines'
    own block split, replicated so M/X can slice)."""
    raw = Path(path).read_text(encoding="utf-8").splitlines()
    blocks, cur = [], []
    for ln in raw:
        s = ln.strip()
        if s:
            cur.append(s)
        elif cur:
            blocks.append(cur); cur = []
    if cur:
        blocks.append(cur)
    return blocks


def _is_header_block(b):
    """§C: header block = first line starts '#' or '**', OR any line starts
    '===='."""
    if b[0].startswith("#") or b[0].startswith("**"):
        return True
    return any(ln.startswith("====") for ln in b)


def _is_trailing_note_block(b):
    """§C: trailing blocks whose first line starts '*(' or '*' (italic note /
    attribution) or '#' (markdown section) are EXCLUDED."""
    f = b[0]
    return f.startswith("*(") or f.startswith("*") or f.startswith("#")


def _is_number_title_singleton(b):
    """A leading singleton block that is a bare number (arabic/CJK/roman) or
    an all-caps Latin title — the fenced-.txt poem-number/title block
    (II / IV / L'ALBATROS / CORRESPONDANCES / ECHOES). Dropped in M so the
    title block between the ==== header and the verse never counts as verse."""
    if len(b) != 1:
        return False
    s = b[0]
    if NUMRE.match(s) or ROMANRE.match(s):
        return True
    letters = [c for c in s if c.isalpha()]
    # all-caps Latin title: has letters, all uppercase (unicode-aware — the
    # accented É of ÉLÉVATION defeated the A-Z range check; §H dry fix)
    if letters and all(c.isupper() for c in letters):
        return True
    return False


def parse_S(path):
    """[S] the committed final-block rule — verbatim from D."""
    return D.verse_lines(path)


def parse_M(path, nblocks=None):
    """[M] all verse blocks after header blocks; trailing italic-note /
    markdown-section blocks excluded; leading number/title singletons
    dropped; bare number lines dropped inside verse (committed numre).
    nblocks (per-seat, §H): take only the FIRST nblocks verse blocks —
    for files with trailing prose paragraphs that carry no markdown
    marker (the forke case, §H dry fix)."""
    blocks = _blocks(path)
    verse = []
    taken = 0
    for b in blocks:
        if _is_header_block(b):
            continue
        if _is_trailing_note_block(b):
            continue
        if _is_number_title_singleton(b):
            continue
        if nblocks is not None and taken >= nblocks:
            break
        taken += 1
        for ln in b:
            if NUMRE.match(ln):
                continue
            verse.append(ln)
    return verse


def parse_X(path, prefix):
    """[X] select the block whose FIRST line starts with the registered
    first-line prefix; drop bare number lines inside it (committed numre)."""
    for b in _blocks(path):
        if b[0].startswith(prefix):
            return [ln for ln in b if not NUMRE.match(ln)]
    return []


def parse_seat(seat):
    """Dispatch on the seat's registered spec. Returns the verse line list."""
    spec = seat["spec"]
    p = seat["path"]
    if spec == "S":
        return parse_S(p)
    if spec == "M":
        return parse_M(p, nblocks=seat.get("nblocks"))
    if spec == "X":
        return parse_X(p, seat["prefix"])
    raise ValueError(f"unknown spec {spec!r} for {seat['rid']}")


# ============================================================ corpus load
def load_board(board):
    """Resolve a board's seats against disk. Returns
    (present {rid:{lang,file,lines,n_lines,sha256,tier,redact,spec,exp}},
     missing [{rid,lang,path,reason}]). Aborts nothing here — the caller
     decides (dry reports, run aborts on count mismatch)."""
    b = BOARDS[board]
    present, missing = {}, []
    for seat in b["seats"]:
        rid = seat["rid"]
        lang = seat_lang(seat)
        path = seat["path"]
        if not Path(path).exists():
            missing.append({"rid": rid, "lang": lang, "path": str(path),
                            "reason": "declared on the board, not present on disk"})
            continue
        lines = parse_seat(seat)
        present[rid] = {"lang": lang, "file": str(path), "lines": lines,
                        "n_lines": len(lines), "sha256": D.sha256(path),
                        "tier": seat["tier"], "redact": (seat["tier"] == "local"),
                        "spec": seat["spec"], "exp": seat["exp"]}
    return present, missing


def count_check(present):
    """Per seat: (rid, parsed, exp, ok). ok is None when exp unregistered
    (dry-marked); True/False otherwise."""
    rows = []
    for rid in sorted(present):
        r = present[rid]
        exp = r["exp"]
        ok = None if exp is None else (r["n_lines"] == exp)
        rows.append((rid, r["n_lines"], exp, ok))
    return rows


# ============================================================ manifests
def latent_carrier_shas():
    """Latent carrier shas, pinned the way L.mode_run pins them."""
    m = {}
    for name, p in [("temporal", RESULTS / "hownet_temporal_chars_54.json"),
                    ("sound_amended", RESULTS / "hownet_sound_chars_54_amended.json"),
                    ("plant", RESULTS / "hownet_plant_chars_54.json"),
                    ("written_labeler", MARK_TOOLS / "latent_written_labeler_53.py"),
                    ("etym_chains", PROTO / "etym_chains_v1_52.py"),
                    ("rubric_compare", MARK_TOOLS / "rubric_compare.py")]:
        if p.exists():
            m[name] = D.sha256(p)
        else:
            # Declared, never silently omitted (manual §7.20): a manifest that
            # under-reports its pinned inputs is worse than one that says MISSING.
            m[name] = f"MISSING: {p}"
    return m


def board_manifest(board, present, missing, drift, ninv):
    b = BOARDS[board]
    man = D.input_manifest()                      # axes, booleans, comparator, model shas (verbatim)
    man["latent_carriers"] = latent_carrier_shas()
    man["seed"] = SEED
    man["board"] = board
    man["source_lang"] = b["source_lang"]
    man["source_rid"] = b["source_rid"]
    man["certificate_drift"] = drift
    man["n_inventory"] = ninv
    man["corpus_present"] = {rid: {"sha256": present[rid]["sha256"],
                                   "tier": present[rid]["tier"],
                                   "file": present[rid]["file"],
                                   "spec": present[rid]["spec"],
                                   "parsed_n_lines": present[rid]["n_lines"],
                                   "registered_exp": present[rid]["exp"],
                                   "text_redacted_in_outputs": present[rid]["redact"]}
                             for rid in sorted(present)}
    man["corpus_missing"] = missing
    man["inventory_size"] = ninv
    man["seats_missing"] = sorted(m["rid"] for m in missing)
    return man


# ==================================================== ruled cuts (manual §3/§4.1)
_CUTS_MEMO = None


def ruled_cuts():
    """Per-field promotion/presence cuts of record (her ruling 07-26):
    color ADOPTED (flagship); plant/sound/illumination SUGGESTED boundaries.
    Single source of truth = the registered derivation output; sha pinned."""
    global _CUTS_MEMO
    if _CUTS_MEMO is None:
        p = PROTO / "results" / "promotion_threshold_59.json"
        d = json.loads(p.read_text(encoding="utf-8"))
        cuts, tiers, line_cuts = {}, {}, {}
        for f, ff in d["fields"].items():
            if ff.get("adopted_threshold") is not None:
                cuts[f] = float(ff["adopted_threshold"])
                tiers[f] = "ADOPTED (flagship)"
            else:
                cuts[f] = float(ff["quantile_cut"]["0.95"])
                tiers[f] = "SUGGESTED boundary (her ruling 07-26 — lower confidence, declared)"
            # LINE-BAR (her night ruling): p95 of control host-line projections;
            # absent on pre-extension jsons -> line-ghost clause simply inert.
            if ff.get("line_cut") is not None:
                line_cuts[f] = float(ff["line_cut"])
        _CUTS_MEMO = (cuts, tiers, line_cuts, D.sha256(p))
    return _CUTS_MEMO


# CONTENTFUL — the runner's token filter for scalar movers. DELIBERATELY NOT the
# same predicate as linegrain_law_60._contentful, and NOT to be unified with it
# (#71 finding, load-bearing): this one is an explicit script-range whitelist
# (ASCII + Latin-1/Ext-A + kana + CJK), the LAW's is
# `any(CJK or c.isalpha())`. They disagree in BOTH directions — Greek ἄνθος,
# Cyrillic кровь, Hangul 한글, the ﬁ ligature and IPA ɐ are contentful to the LAW
# and not here; the kana voicing mark ゛ is contentful here and not to the LAW.
# The census and this runner therefore filter movers by different rules ON
# PURPOSE; changing either silently moves published counts.
CONTENTFUL = re.compile(r"[A-Za-zÀ-ɏ぀-ヿ一-鿿]")

# trad→simp fold: `fold` is imported from linegrain_law_60 (see the import
# block). This runner used to carry a private _fold_zh with the same body —
# same Unihan_Variants.txt path, same kSimplifiedVariant parse, same
# char-substitution — so the copy was deleted in #71 rather than kept in sync.
# The ruling it implements is unchanged: her 嘆/叹 catch, 07-27 — simplified
# inventories must match traditional boards.


def scalar_poem_inventory(rows, cuts, line_cuts=None):
    """2-state presence per field from token deltas OR line projections
    (manual §4.1 + her night ruling: token trigger, else line trigger):
    PRESENT iff some line carries a contentful token with Δ >= token-cut,
    OR some line's own reading >= line-cut. Borrowed-cut parity caveat.
    Temporal has no scalar cut (organ field) — absent here by design."""
    line_cuts = line_cuts or {}
    active, seen = {}, set()
    for row in rows:
        for f, movers in (row.get("top_delta") or {}).items():
            if f not in cuts and f not in line_cuts:
                continue
            seen.add(f)
            if f in active:
                continue
            if f in cuts:
                for t, dd in movers:
                    if dd is not None and dd >= cuts[f] and CONTENTFUL.search(str(t)):
                        active[f] = {""}
                        break
            if f not in active and f in line_cuts:
                if float((row.get("reading") or {}).get(f, -9e9)) >= line_cuts[f]:
                    active[f] = {""}
    return active, seen


# ============================================================ scoring
def _new_model():
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer(str(MODELS / "LaBSE"), device="cpu")


def score_board(board):
    """ONE ENCODE PASS per board feeding BOTH rows (registration §C.b).
    Returns (present, missing, readings, drift, ninv, desc, writ, ref,
    desc_transitions, lat_transitions, transitions_runnable) or raises
    RuntimeError on count mismatch / certificate failure (--run abort law)."""
    b = BOARDS[board]
    src_lang = b["source_lang"]
    src_rid = b["source_rid"]
    present, missing = load_board(board)

    # count assertions (§C.a / §E.2): registered mismatch → DROP-AND-DECLARE the seat
    # (the module docstring's own promised posture; was: whole-board abort — manual
    # §7.20). A mismatching SOURCE still aborts: no source, no crossings.
    for rid, parsed, exp, ok in count_check(present):
        if ok is False:
            if rid == src_rid:
                raise RuntimeError(
                    f"PARSE COUNT MISMATCH {board} SOURCE {rid}: parsed {parsed} != "
                    f"registered {exp} — source seat unusable, board aborted")
            missing.append({"rid": rid, "path": present[rid]["file"],
                            "reason": f"COUNT MISMATCH parsed {parsed} != registered "
                                      f"{exp} (spec {present[rid]['spec']}) — "
                                      f"dropped-and-declared"})
            print(f"[{board}] DROP-AND-DECLARE {rid}: parsed {parsed} != registered {exp}",
                  file=sys.stderr)
            del present[rid]

    model = _new_model()
    axes = D.load_axes()

    # ONE encode pass: build the renderings dict, load_axes + scalar_readings ONCE
    rend = {rid: {"lang": present[rid]["lang"], "lines": present[rid]["lines"]}
            for rid in present}
    readings, drift, ninv = D.scalar_readings(model, axes, rend)
    if drift >= 1e-6:
        raise RuntimeError(f"CERTIFICATE FAILED {drift:.2e} — board {board} aborted (house law)")

    # descriptive row = readings (above) + per-line boolean_states + transitions
    desc = {rid: [D.boolean_states(l, present[rid]["lang"]) for l in present[rid]["lines"]]
            for rid in sorted(present)}

    # latent row = written_row_line / referent_row_line per line
    zh_sensor, en_sensor = L._sensors()
    writ = {rid: [L.written_row_line(l, present[rid]["lang"], zh_sensor, en_sensor)
                  for l in present[rid]["lines"]] for rid in sorted(present)}
    ref = {rid: [L.referent_row_line(l, present[rid]["lang"]) for l in present[rid]["lines"]]
           for rid in sorted(present)}

    # ============ PER-WORD TRIGGER LAW + GHOST REGISTRY (her 札札弄机杼 walk,
    # 07-26 night): every unit is scored; only TRIGGERED words (own token-Δ >=
    # the field's ruled cut) are probed; attribution never migrates between
    # words; triggered-and-unaccounted = GHOST ("what the meter attests and no
    # citation grounds — 弦外之音 / the ignition of an aesthetic idea").
    c1_cuts, c1_tiers, c1_line_cuts, _c1_sha = ruled_cuts()
    sound_join = sound_pool_join(present)
    trig = {}   # rid -> [per line: {field: [(token, Δ) triggered contentful]}]
    for rid in sorted(present):
        rows_t = []
        for li in range(len(present[rid]["lines"])):
            row_deltas = readings[rid][li].get("top_delta", {})
            per_f = {}
            for f, cut in c1_cuts.items():
                toks = [(str(t), dd) for t, dd in (row_deltas.get(f) or [])
                        if dd is not None and dd >= cut and CONTENTFUL.search(str(t))]
                if toks:
                    per_f[f] = toks
            rows_t.append(per_f)
        trig[rid] = rows_t

    def _match(tok, words):
        # Fold-aware since 07-27 (her 嘆/叹 catch): simplified inventory words
        # must match traditional board text and vice versa.
        ft = fold(tok)
        for w in words:
            if not w:
                continue
            fw = fold(str(w))
            if ft == fw or fw in ft or ft in fw:
                return True
        return False

    def _attributions(rid, li, f):
        """(stated_words, written_words, referent_words) claimable at this line."""
        b = desc[rid][li].get(f, {})
        stated = set(b.get("receipts") or []) if b.get("fires") else set()
        wv = writ[rid][li].get(f, {})
        written = {fr.get("word") for fr in (wv.get("fires") or [])
                   if isinstance(fr, dict) and fr.get("word")} if wv.get("fires_bool") else set()
        referent = set()
        rr = ref[rid][li] if li < len(ref.get(rid, [])) else {}
        if f == "color" and rr.get("available") and rr.get("field") == "color":
            referent |= set(rr.get("referent_trigger_words") or [])
        if f == "sound":
            # CALL-gated (07-26 night fix: occurrence is not citation — 水 at
            # z −2.77 must not ground a latent-sound state; only meter CALLS
            # (z >= 1.5) constitute a citable sound-referent account here)
            srows = (sound_join.get("renderings") or {}).get(rid) or []
            if li < len(srows):
                referent |= {h.get("word") for h in srows[li]
                             if h.get("word") and h.get("call")}
        # tag-strip receipts so 吹[gy]-style entries match tokens (07-27)
        stated = {re.split(r"[\[\(（【]", str(w))[0].strip() for w in stated if w}
        return stated, written, referent

    # check-1 per fired word: the FIRED word itself must be triggered.
    for rid in sorted(present):
        for li, st in enumerate(writ[rid]):
            for f in FIELDS5:
                v = st.get(f, {})
                v["scalar_check1"] = float(readings[rid][li]["reading"][f])
                if not (v.get("available") and not v.get("informational_only")):
                    continue
                cut = c1_cuts.get(f)
                if not v.get("fires_bool") or cut is None:
                    v["fires_three_check"] = False
                    continue
                fired_words = [fr.get("word") for fr in (v.get("fires") or [])
                               if isinstance(fr, dict) and fr.get("word")]
                hit = None
                for ts, dd in trig[rid][li].get(f, []):
                    if _match(ts, fired_words) and (hit is None or dd > hit[1]):
                        hit = (ts, dd)
                v["check1_rule"] = ("per-word: the fired word itself must trigger "
                                    "(her walk 07-26; attribution never migrates)")
                v["check1_cut"] = cut
                v["check1_tier"] = c1_tiers.get(f)
                if hit:
                    v["check1_trigger_token"], v["check1_trigger_delta"] = hit
                    v["fires_three_check"] = True
                else:
                    v["fires_three_check"] = False
                    others = [t for t, _ in trig[rid][li].get(f, [])]
                    if others:
                        v["check1_line_ghost_candidates"] = others   # declared

    # transitions — EVERY seat classifies (manual §4.1; was: coverage-gated,
    # fr boards produced no verdicts at all). State source is PER-FIELD PER-SEAT:
    # boolean where that field's boolean covers the seat's language (full
    # resolution), else scalar 2-state under the ruled cuts (SUGGESTED tier,
    # zh-derived cuts borrowed cross-language — parity caveat, her ruling 07-26).
    # A field crosses only where BOTH sides have some channel (no fabricated
    # absents — the F2 guard, generalized).
    cuts, cut_tiers, line_cuts, cuts_sha = ruled_cuts()
    transitions_runnable = src_rid in present
    desc_transitions, lat_transitions = {}, {}
    if transitions_runnable:
        import rubric_compare as RC

        def writ_poem_complete(states):
            active, seen = {}, set()
            for st in states:
                for f, vv in st.items():
                    if not vv.get("available") or vv.get("informational_only"):
                        continue
                    seen.add(f)
                    if vv.get("fires_three_check"):
                        active.setdefault(f, set()).add("")
            return active, seen

        def seat_states(rid):
            """(active, resolution_map, latent, latent_seen, ghost) — per-field.
            Covered seats: latent = written fires (per-word gated) ∪ referent-
            attributed triggered words; ghost = triggered words no channel
            claims (her walk). Uncovered seats: 2-state active*/absent only —
            ghost requires citation channels to have EXISTED (parity honesty)."""
            b_act, b_seen = D.poem_inventory(desc[rid])
            s_act, s_seen = scalar_poem_inventory(readings[rid], cuts, line_cuts)
            act, res = {}, {}
            for f in sorted(b_seen | s_seen):
                if f in b_seen:
                    res[f] = "boolean"
                    if f in b_act:
                        act[f] = b_act[f]
                else:
                    res[f] = "scalar-2state (borrowed zh cut, SUGGESTED tier)"
                    if f in s_act:
                        act[f] = s_act[f]
            covered = present[rid]["lang"] in D.BOOL_COVERED_LANGS
            lat, lseen = (writ_poem_complete(writ[rid]) if covered else ({}, set()))
            gho = {}
            if covered:
                for li, per_f in enumerate(trig[rid]):
                    for f, toks in per_f.items():
                        stated_w, written_w, referent_w = _attributions(rid, li, f)
                        for ts, dd in toks:
                            if _match(ts, stated_w):
                                continue                       # active channel owns it
                            if _match(ts, written_w) or _match(ts, referent_w):
                                lat.setdefault(f, set()).add("")   # citable account
                            else:
                                gho.setdefault(f, set()).add("")   # token-GHOST
                    # (line-ghost-as-STATE not adopted — her later ruling: ranks
                    # on exhibits + the consensus-ghost board list carry the
                    # line-level story; line_cuts remain reported reference.)
            return act, res, lat, lseen, gho

        sa_full, s_res, sl_full, s_lseen, sg_full = seat_states(src_rid)
        for rid in sorted(present):
            if rid == src_rid:
                continue
            ta_full, t_res, tl_full, t_lseen, tg_full = seat_states(rid)
            dom = set(s_res) & set(t_res)
            sa = {f: v for f, v in sa_full.items() if f in dom}
            ta = {f: v for f, v in ta_full.items() if f in dom}
            sl = {f: v for f, v in sl_full.items() if f in dom}
            tl = {f: v for f, v in tl_full.items() if f in dom}
            sg = {f: v for f, v in sg_full.items() if f in dom}
            tg = {f: v for f, v in tg_full.items() if f in dom}
            rows, ladder = RC.compare(sa, ta, src_latent=sl, tr_latent=tl,
                                      src_ghost=sg, tr_ghost=tg)
            entry = {
                "grain": "poem",
                "fields_domain": sorted(dom),
                "resolution": {"source": s_res, "target": t_res},
                "cut_provenance": (None if all(r == "boolean" for r in
                                               list(s_res.values()) + list(t_res.values()))
                                   else {"file": "engine/results/promotion_threshold_59.json",
                                         "sha256": cuts_sha, "cuts": cuts,
                                         "tiers": cut_tiers,
                                         "caveat": "zh-derived cuts on non-zh deltas — "
                                                   "parity loan, SUGGESTED tier"}),
                "rows": rows,
                "ladder": ladder,
                "survival_rates": D.survival_rates(rows),
                "src_latent": sorted(sl), "tr_latent": sorted(tl),
                "src_ghost": sorted(sg), "tr_ghost": sorted(tg),
            }
            desc_transitions[rid] = entry
            lat_transitions[rid] = entry  # one unified crossing since 07-26 —
            # descriptive+latent slots cross together; both files carry it.

    return (present, missing, readings, drift, ninv, desc, writ, ref,
            desc_transitions, lat_transitions, transitions_runnable)


# ============================================================ F9 redaction
_F9_NOTE = ("in-copyright LOCAL_TIER transcription — full-line text never enters "
            "publishable/ (F9); source file + sha in manifest")
_FR_NOT_RUNNABLE = ("fr source has NO boolean shelf (F2: booleans are en+zh only) — "
                    "cross-lingual transition classification DECLARED NOT RUNNABLE for "
                    "this board; scalars + per-rendering field states + zh written-latent "
                    "still land (registration §C, board law)")


def apply_f9(present, readings, writ, ref):
    """Null local-tier line text in ALL outputs. Descriptive readings rows'
    "text" -> None + note (mirroring D.mode_run). Latent structures carry no
    line text (mirroring L.mode_run: written states carry no _line; referent
    rows marked)."""
    for rid in sorted(present):
        if not present[rid]["redact"]:
            continue
        for row in readings[rid]:
            row["text"] = None
            row["text_redacted"] = _F9_NOTE
        for st in writ[rid]:
            for f in FIELDS5:
                # Defensive no-op, kept: verified #71 that the written-row
                # builder emits no "_line" key in any branch (word-grain
                # receipts only, which F9 permits), so this sweep never fires.
                # latent_score_54.mode_run carried the identical line and it was
                # dropped there; kept HERE because this runner's --run path is
                # not exercisable in the published tree.
                st[f].pop("_line", None)
        for rr in ref[rid]:
            rr["_line_redacted"] = True


# ============================================================ output writers
def _desc_result(board, present, readings, desc, desc_transitions,
                 transitions_runnable, manifest):
    b = BOARDS[board]
    result = {
        "what": f"deterministic descriptive fields — e7 corpus-breadth, board {board}",
        "registration": "engine/registrations/corpus_breadth_scoring_registration_56.md §C/§D",
        "law": "methodology_statement_0716.md §3/§5/§6/§7/§8/§9; RULERS.md A1/A3/A4/A5/A7",
        "source_lang": b["source_lang"],
        "flags": ["F1 grain=poem (line needs chair alignment, unfrozen)",
                  "F2 booleans en+zh only; de/jp/fr target states UNAVAILABLE",
                  "F3 raw scalar deltas NON-TRANSFERABLE (§3); equating unfrozen",
                  "F9 local-tier line text redacted"],
        "manifest": manifest,
        "supersedes_beside": f"descriptive_scores_{board}_56.json (originals kept; "
                             f"v2 = the corrected pipeline, manual SCORING_MANUAL_0726_59)",
        "ruled_cuts": dict(zip(("cuts", "tiers", "line_cuts", "source_sha256"), ruled_cuts())),
        "scalar_readings": readings,
        "booleans": {rid: [{f: {"fires": v["fires"], "receipts": v["receipts"],
                                "coverage": v["coverage"]} for f, v in st.items()}
                           for st in desc[rid]] for rid in sorted(desc)},
        # transitions ALWAYS present since 07-26 (manual §4.1) — resolution
        # flags inside each entry carry the coverage difference.
        "transitions": desc_transitions,
    }
    return result


def colour_join_for(board):
    """Embed the board's per-line colour referent column (the #59 join —
    committed type-prior charges attached to line occurrences)."""
    p = HERE / "deterministic-latent-referent-fields" / "per_line_referent_colour_59.json"
    if not p.exists():
        return {"status": f"MISSING: {p}"}
    d = json.loads(p.read_text(encoding="utf-8"))
    bb = d.get("boards", {}).get(board)
    if bb is None and board == "sonnet73":
        bb = d.get("boards", {}).get("55")   # pilot's charge table is the 55 file
    return {"tier": d.get("tier"), "label": d.get("label"),
            "join_sha256": D.sha256(p),
            "board_data": bb if bb is not None else {"status": "board absent from join"}}


def sound_pool_join(present):
    """Per-line occurrences of the MEASURED sound latent-referent pool
    (word_latent_sound_referent_54.json items, zh seats) with word-TYPE charges.
    Type-prior label (Q5c); sealed-exam credential +.120; SUGGESTED per-line
    (occurrence lookup, not in-line measurement). Pool words are dictionary
    items, never line text — F9-safe."""
    p = PROTO / "results" / "word_latent_sound_referent_54.json"
    if not p.exists():
        return {"status": f"MISSING: {p}"}
    d = json.loads(p.read_text(encoding="utf-8"))
    items = {w: v for w, v in (d.get("items") or {}).items()
             if isinstance(v, dict) and "charge" in v}
    out = {"tier": "type-prior (her Q5c); sound sealed-exam +.120; SUGGESTED "
                   "per-line (occurrence lookup, not in-line measurement)",
           "source_sha256": D.sha256(p), "n_pool": len(items), "renderings": {}}
    for rid in sorted(present):
        if present[rid]["lang"] != "zh":
            continue
        rows = []
        for line in present[rid]["lines"]:
            fline = fold(line)       # fold-aware occurrence (機杼 vs 机杼, 07-27)
            hits = [{"word": w, "charge": v.get("charge"), "z": v.get("z"),
                     "call": v.get("call"), "role": v.get("role")}
                    for w, v in items.items() if fold(w) in fline]
            rows.append(hits)
        out["renderings"][rid] = rows
    return out


def _lat_result(board, present, writ, ref, lat_transitions, transitions_runnable,
                manifest, en_sensor, sound_pool_join_result):
    b = BOARDS[board]
    result = {
        "what": f"deterministic LATENT rows — e7 corpus-breadth, board {board}",
        "registration": "engine/registrations/corpus_breadth_scoring_registration_56.md §C/§D",
        "law": "methodology_amendment_0721_53.md §2/§4; rubric_compare 8-cell",
        "source_lang": b["source_lang"],
        "flags": ["L-F1 folder name", "L-F2 check1=scalar (applied at run)",
                  "L-F3 realized-gate layering", "L-F4 en illumination no boolean",
                  "L-F5 consider/star exhibit", "L-F6 referent trigger thin",
                  "F9 local-tier line text redacted"],
        "manifest": manifest,
        "supersedes_beside": f"latent_scores_{board}_56.json (originals kept)",
        "written_row": writ,
        "referent_row": ref,
        "referent_per_line_colour": colour_join_for(board),
        "sound_referent_per_line": sound_pool_join_result,
        "consider_exhibit": en_sensor.consider_exhibit(),
        "transitions": lat_transitions,
    }
    return result


def _write_human_table(board, present, readings, desc, desc_transitions,
                       transitions_runnable, manifest, out_md):
    """Human .md table mirroring the pilot's _write_human_table shape;
    redacted rows marked."""
    b = BOARDS[board]
    md = [f"# Descriptive-field scores — board {board} (e7 corpus-breadth, #56)",
          "",
          "*Instruments only (no LLM marks anything). THE SCALAR IS THE PAPER.*",
          f"*Certificate (re-order, batch_size=1): {manifest['certificate_drift']:.2e} — "
          f"seed {manifest['seed']}. Scalar space = LaBSE + each axis npz's own mu/W.*",
          f"*Source lang: {b['source_lang']} · registration "
          f"engine/registrations/corpus_breadth_scoring_registration_56.md §C/§D.*",
          "",
          "Flags: F1 grain=poem · F2 booleans en+zh only (de/jp/fr field states UNAVAILABLE) · "
          "F3 raw scalar deltas NON-TRANSFERABLE, comparison is rank-space (§3) · "
          "F9 local-tier line text redacted.", ""]
    for rid in sorted(present):
        r = present[rid]
        md.append(f"## {rid}  ({r['lang']}, {r['n_lines']} lines, spec {r['spec']})")
        md.append("")
        md.append("| line | text | color | illum | sound | plant | temporal | booleans fired |")
        md.append("|---|---|---|---|---|---|---|---|")
        if r["redact"]:
            md.append("*(line text REDACTED — in-copyright LOCAL_TIER, F9; "
                      "file + sha in the json manifest)*")
        for row, st in zip(readings[rid], desc[rid]):
            rd = row["reading"]
            fired = " ".join(f"{f}[{' '.join(v['receipts'])}]"
                             for f, v in st.items() if v["fires"] is True) or "—"
            txt = "*(redacted)*" if row.get("text") is None else row["text"].replace("|", "/")
            md.append(f"| {row['line_no']} | {txt} | {rd['color']:+.2f} | {rd['illumination']:+.2f} | "
                      f"{rd['sound']:+.2f} | {rd['plant']:+.2f} | {rd['temporal']:+.2f} | {fired} |")
        md.append("")
    md.append("## Cross-side transitions (8-cell comparator, poem grain — every seat "
              "classifies since 07-26; scalar-2state seats flagged)")
    md.append("")
    for rid, t in sorted(desc_transitions.items()):
        scal = sorted(f for f, r in t["resolution"]["target"].items()
                      if r != "boolean")
        flag = f" · target scalar-2state fields: {scal} (borrowed cut, SUGGESTED)" if scal else ""
        md.append(f"- **{rid}** (domain {t['fields_domain']}): {t['survival_rates']}{flag}")
    out_md.write_text("\n".join(md), encoding="utf-8")


def desc_paths(board):
    # _59 = v2-beside (originals never overwritten; supersede pointers inside)
    return (DESC / f"descriptive_scores_{board}_59.json",
            DESC / f"descriptive_scores_{board}_59.md")


def lat_path(board):
    return LAT / f"latent_scores_{board}_59.json"


# ================================================================ MODES
def mode_dry(board):
    print("=" * 74)
    print(f"DRY / COUNT MODE — board {board} — real corpus, no encoder")
    print("  (check-1 scalar PENDING here, L-F2; latent fires = checks 2∧3)")
    print("=" * 74)
    b = BOARDS[board]
    present, missing = load_board(board)
    zh_sensor, en_sensor = L._sensors()

    print(f"\n[board {board}] source_lang={b['source_lang']}  source_rid={b['source_rid']}")
    print(f"  transitions runnable (source boolean-covered): "
          f"{b['source_lang'] in D.BOOL_COVERED_LANGS}")

    print("\n[PARSE — per seat: rid · tier · spec · parsed · registered · first/last parsed line]")
    print("  (tier LOCAL rows: counts + first/last 3 chars only — in-copyright, F9)")
    for rid in sorted(present):
        r = present[rid]
        exp = r["exp"]
        ok = "—" if exp is None else ("OK" if r["n_lines"] == exp else "**MISMATCH**")
        tag = "LOCAL" if r["redact"] else "repo "
        if r["lines"]:
            first, last = r["lines"][0], r["lines"][-1]
            if r["redact"]:
                fl = f"first[{first[:3]}…] last[…{last[-3:]}]"
            else:
                fl = f"first={first!r} last={last!r}"
        else:
            fl = "(no lines parsed)"
        exps = "dry" if exp is None else str(exp)
        print(f"  [{tag}] {rid:22} spec={r['spec']} parsed={r['n_lines']:>3} "
              f"registered={exps:>3} {ok:>11}")
        print(f"          {fl}")
    if missing:
        print("\n[declared but MISSING on disk — listed, not substituted]")
        for m in missing:
            print(f"  {m['rid']:22} ({m['lang']})  {m['path']}")

    # descriptive boolean fire preview
    print("\n[descriptive boolean fire counts per field per language (shelf en+zh only, F2)]")
    tally = {}
    for rid in sorted(present):
        lang = present[rid]["lang"]
        for line in present[rid]["lines"]:
            st = D.boolean_states(line, lang)
            for f in FIELDS5:
                d = tally.setdefault((lang, f), {"fires": 0, "unavail": 0, "lines": 0})
                d["lines"] += 1
                v = st[f]["fires"]
                if v is True:
                    d["fires"] += 1
                elif v is None:
                    d["unavail"] += 1
    print(f"    {'lang':4} {'field':13} {'fires':>6} {'unavail':>8} {'lines':>6}")
    for lang in ("en", "zh", "de", "jp", "fr"):
        for f in FIELDS5:
            d = tally.get((lang, f))
            if not d:
                continue
            print(f"    {lang:4} {f:13} {d['fires']:6d} {d['unavail']:8d} {d['lines']:6d}")

    # latent written-row preview (checks 2∧3)
    print("\n[WRITTEN-LATENT fire preview per rendering × field (checks 2∧3; carriers named)]")
    print("  tier LOCAL: carriers/counts only, F9")
    for rid in sorted(present):
        lang = present[rid]["lang"]
        cnt = {f: 0 for f in FIELDS5}
        cars = {f: set() for f in FIELDS5}
        avail = {f: False for f in FIELDS5}
        for l in present[rid]["lines"]:
            st = L.written_row_line(l, lang, zh_sensor, en_sensor)
            for f in FIELDS5:
                v = st[f]
                if v.get("available") and not v.get("informational_only"):
                    avail[f] = True
                    if v.get("fires_bool"):
                        cnt[f] += 1
                        cars[f].update(v["carriers"])
        cells = " ".join(((f"{cnt[f]}" if avail[f] else "n/a").rjust(7)) for f in FIELDS5)
        print(f"    {rid:22} {lang:4} " + cells)
        for f in FIELDS5:
            if cars[f]:
                print(f"        {f}: carriers {' '.join(sorted(cars[f]))}")

    # transition runnability
    print("\n[transition runnability]")
    if b["source_lang"] not in D.BOOL_COVERED_LANGS:
        print(f"  NOT RUNNABLE — {_FR_NOT_RUNNABLE}")
    else:
        tgt = sorted(rid for rid in present
                     if rid != b["source_rid"] and present[rid]["lang"] in D.BOOL_COVERED_LANGS)
        print(f"  source {b['source_rid']} ({b['source_lang']}) boolean-covered → "
              f"runnable transition pairs: {len(tgt)}")
        print(f"    targets: {tgt}")

    # embed estimate
    uniq = set()
    for rid in sorted(present):
        for l in present[rid]["lines"]:
            uniq.add(l)
            for u in D.maskable_units(l):
                uniq.add(D.delete_unit(l, u))
    print("\n[embed estimate for the real run (LaBSE, batch_size=1)]")
    print(f"  unique texts (line + one-deletion masks): {len(uniq)}")
    print(f"  with certificate re-order replay: ~{2*len(uniq)} encodes")

    # input shas
    print("\n[input shas]")
    man = D.input_manifest()
    for grp, d in sorted(man.items()):
        for k, v in sorted(d.items()):
            s = v["sha256"] if isinstance(v, dict) else v
            print(f"  {grp:18} {k:34} {s[:16]}…")
    for name, sh in sorted(latent_carrier_shas().items()):
        print(f"  {'latent_carrier':18} {name:34} {sh[:16]}…")
    print(f"\n[outputs that --run would write] {[str(p) for p in (*desc_paths(board), lat_path(board))]}")
    return 0


def mode_run(board):
    """REAL run for one board. Certificate < 1e-6 or abort (house law).
    skip-if-exists = json present AND --verify passes -> SKIP."""
    djson, dmd = desc_paths(board)
    ljson = lat_path(board)
    if djson.exists() and ljson.exists() and not FORCE_RERUN:
        rc = _verify(board, quiet=True)
        if rc == 0:
            print(f"SKIP {board} — outputs exist and --verify passes (--force overrides)")
            return 0
        print(f"[{board}] outputs exist but --verify failed — re-running")

    try:
        (present, missing, readings, drift, ninv, desc, writ, ref,
         desc_transitions, lat_transitions, runnable) = score_board(board)
    except RuntimeError as e:
        print(f"ABORT {board}: {e}", file=sys.stderr)
        return 1

    _, en_sensor = L._sensors()
    apply_f9(present, readings, writ, ref)         # F9 before anything lands
    manifest = board_manifest(board, present, missing, drift, ninv)

    sound_join = sound_pool_join(present)   # before F9 (uses input lines; F9-safe output)
    desc_result = _desc_result(board, present, readings, desc, desc_transitions,
                               runnable, manifest)
    lat_result = _lat_result(board, present, writ, ref, lat_transitions, runnable,
                             manifest, en_sensor, sound_join)
    djson.write_text(json.dumps(desc_result, ensure_ascii=False, indent=1), encoding="utf-8")
    _write_human_table(board, present, readings, desc, desc_transitions, runnable,
                       manifest, dmd)
    ljson.write_text(json.dumps(lat_result, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"→ {djson.name} + {dmd.name} + {ljson.name}  (certificate {drift:.2e})")

    rc = _verify(board)
    if rc != 0:
        # Declare-don't-destroy (manual §7.20; was: unlink — a gauge bug could destroy
        # good data). If §E.3 (F9) failed, quarantined files may contain local-tier
        # text: the suffix marks them not-for-delivery; they never leave this disk.
        print(f"[{board}] POST-RUN VERIFY FAILED — quarantining outputs "
              f"(*.QUARANTINE_FAILED_VERIFY)", file=sys.stderr)
        for p in (djson, dmd, ljson):
            if p.exists():
                p.rename(p.with_name(p.name + ".QUARANTINE_FAILED_VERIFY"))
        return 1
    return 0


# ============================================================ verify (§E)
def _local_line_strings(board):
    """Every raw stripped line string of every local-tier input file of the
    board (the F9 redaction scan target — §E.3)."""
    strs = {}
    for seat in BOARDS[board]["seats"]:
        if seat["tier"] != "local" or not Path(seat["path"]).exists():
            continue
        lines = parse_seat(seat)
        # F9 scan floor 2 (was 4 — manual §7.11): 2-3 char CJK verse lines are real
        # local-tier text; 1-char lines stay out (substring noise — every char matches).
        strs[seat["rid"]] = [ln for ln in lines if len(ln.strip()) >= 2]
    return strs


def _verify(board, quiet=False):
    """§E.2-5 assertions on the board's OUTPUTS (the F3 lesson)."""
    def say(*a):
        if not quiet:
            print(*a)

    fails = []
    djson, dmd = desc_paths(board)
    ljson = lat_path(board)
    for p in (djson, dmd, ljson):
        if not p.exists():
            fails.append(f"missing output {p}")
    if fails:
        for f in fails:
            say("FAIL:", f)
        return 1

    dobj = json.loads(djson.read_text(encoding="utf-8"))
    lobj = json.loads(ljson.read_text(encoding="utf-8"))
    b = BOARDS[board]
    runnable = b["source_lang"] in D.BOOL_COVERED_LANGS

    # §E.2 counts match frozen specs (parsed == registered where registered).
    # A mismatching seat passes ONLY if it was dropped-and-declared in the manifest
    # (mirrors score_board's posture; an undeclared mismatch still fails).
    present, missing = load_board(board)
    declared_drops = {m.get("rid") for m in dobj.get("manifest", {}).get("corpus_missing", [])
                      if "COUNT MISMATCH" in str(m.get("reason", ""))}
    for rid, parsed, exp, ok in count_check(present):
        if ok is False and rid not in declared_drops:
            fails.append(f"§E.2 count {rid}: parsed {parsed} != registered {exp} (undeclared)")
    say(f"[{board}] §E.2 parse counts vs frozen specs: "
        f"{'OK' if not any(str(f).startswith('§E.2') for f in fails) else 'FAIL'}")

    # §E.3 F9 redaction scan — grep BOTH json + md for every local raw line
    blob = djson.read_text(encoding="utf-8") + "\n" + dmd.read_text(encoding="utf-8") \
        + "\n" + ljson.read_text(encoding="utf-8")
    hits = []
    for rid, lines in sorted(_local_line_strings(board).items()):
        for ln in lines:
            if ln in blob:
                hits.append((rid, ln))
    if hits:
        for rid, ln in hits[:5]:
            say(f"FAIL §E.3 F9: local line text leaked ({rid}) — offending output under "
                f"publishable/{board}")
        fails.append(f"§E.3 F9 redaction: {len(hits)} local line strings leaked")
    say(f"[{board}] §E.3 F9 redaction scan: {'OK (zero local line text)' if not hits else 'FAIL'}")

    # §E.4 transitions present for EVERY board (manual §4.1, 07-26 — coverage no
    # longer gates verdicts; resolution flags inside entries carry the difference)
    trs = dobj.get("transitions")
    if not isinstance(trs, dict) or not trs:
        fails.append("§E.4 transitions absent/empty (must exist for every board since 07-26)")
    else:
        for rid, t in trs.items():
            if "resolution" not in t or "rows" not in t:
                fails.append(f"§E.4 transition entry {rid} missing resolution/rows")
    say(f"[{board}] §E.4 transitions present w/ resolution flags: "
        f"{'OK' if not any(str(f).startswith('§E.4') for f in fails) else 'FAIL'}")

    # §E.5 latent availability declarations: en fires colour-only counted;
    # de/jp/fr rows carry available:false declarations.
    wl = lobj.get("written_row", {})
    lat_ok = True
    for rid, states in sorted(wl.items()):
        lang = rid.split(":", 1)[0]
        for st in states:
            for f in FIELDS5:
                v = st.get(f, {})
                if lang in ("de", "jp", "fr"):
                    if v.get("available") is not False:
                        lat_ok = False
                if lang == "en" and f in ("sound", "plant", "temporal"):
                    if v.get("available") is not False:
                        lat_ok = False
    if not lat_ok:
        fails.append("§E.5 latent availability declarations wrong (de/jp/fr must be "
                     "available:false; en written-latent limited to colour[/dark informational])")
    say(f"[{board}] §E.5 latent availability declarations: {'OK' if lat_ok else 'FAIL'}")

    if fails:
        for f in fails:
            say("FAIL:", f)
        return 1
    say(f"[{board}] VERIFY OK — §E.2-5 all pass")
    return 0


def mode_verify(board):
    return _verify(board)


# ================================================================ main
if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="e7 corpus-breadth mass-scoring runner (#56)")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry", action="store_true", help="real corpus, no encoder: parse counts + fires + shas")
    g.add_argument("--run", action="store_true", help="REAL run (orchestrator, post-review): writes per-board json+md")
    g.add_argument("--verify", metavar="BOARD", help="assert §E.2-5 on a board's outputs")
    ap.add_argument("--board", choices=BOARD_ORDER, help="restrict to one board (else all, in fixed order)")
    ap.add_argument("--force", action="store_true",
                    help="re-run even where verified outputs exist (same-session rule change)")
    a = ap.parse_args()
    FORCE_RERUN = a.force

    if a.verify:
        if a.verify not in BOARDS:
            print(f"unknown board {a.verify!r}", file=sys.stderr)
            sys.exit(2)
        sys.exit(mode_verify(a.verify))

    boards = [a.board] if a.board else BOARD_ORDER
    _audit_after_run = bool(a.run)
    rc = 0
    for bd in boards:
        if a.dry:
            rc |= mode_dry(bd)
        elif a.run:
            rc |= mode_run(bd)
    if _audit_after_run:
        # DYNAMIC REFLAG LAW (her word 07-26, SCRIPT_MANIFEST §6): report every
        # project file imported by this run — any HISTORICAL-classified file
        # appearing here reflags to LIVE with this run as receipt.
        repo = str(REPO)
        mods = sorted({str(getattr(m, "__file__", ""))
                       for m in list(sys.modules.values())
                       if getattr(m, "__file__", None)
                       and str(getattr(m, "__file__")).startswith(repo)
                       and "venv" not in str(getattr(m, "__file__"))})
        print("[module audit — reflag law] project files imported by this run:")
        for mp in mods:
            print("   ", mp)
    sys.exit(rc)
