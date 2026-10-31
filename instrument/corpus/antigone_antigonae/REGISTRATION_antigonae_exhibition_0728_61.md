# REGISTRATION — THE ANTIGONÄ EXHIBITION BOARD (#61 vigil, 2026-07-28)
*The founding illustration of the paper — the καλχαίνω/rothes-Wort crossing —
built as an EXHIBITION-TIER board and MEASURED for the first time. Her GO given
(gated on de-ok, which Phase 1 established: de_color ADOPTED). Registered-before-
delivery per house law; the board was built + scored during the #61 vigil under
Anneliese's standing order. Alignments are law and hers — the map ships as a
DRAFT with the banner PENDING-PI-SIGNOFF.*

## EXHIBITION-TIER DECLARATION (of record)
This board is NOT part of the 8-board paper census. It is scored by its OWN
standalone scorer (`publishable/antigonae_exhibition_board_61.py`) into its OWN
namespace (`reports/figures/antigonae_exhibition/`). The census
(`linegrain_census_v47_61`), the miner (`interesting_gen_61`) and the heat map
(`stack_heatmap_61`) each carry a hard-coded 8-board list and never see
`antigonae`; the paper runner's `BOARDS`/`BOARD_ORDER` are untouched. The scorer
REUSES the committed scoring functions verbatim (`score_descriptive_fields`
load_axes/scalar_readings/boolean_states; `linegrain_law_60` CELL15/to3/
precedence) — it invents no instrument. LaBSE certificate 0.00e+00.

## THE FINDING (measured)
grc source verse 20 «τί δ᾽ ἔστι; δηλοῖς γάρ τι καλχαίνουσ᾽ ἔπος.» carries an
**LSJ-cited latent-WRITTEN colour etymon** — καλχαίνω, "properly to make purple"
(LSJ s.v.), from κάλχη "the murex, purple limpet = πορφύρα" (LSJ s.v.). The
crossing against each de seat's rendering of that verse:
- **Hölderlin 1804: REVIVAL ★** — «Was ist's, du scheinst ein rothes Wort zu
  färben?» → `de_color` fires **rot** (the roth→rot pre-reform fold). The dormant
  purple colour of the Greek verb is REVIVED on the German surface. Cell =
  (latent-written, active) = **REVIVAL**, starred (grc source is suggestive-tier).
- **Donner 1868: LATENT-UNREALIZED ★** — «Was hast du? Düster wogt in dir ein
  schweres Wort» → `de_color` SILENT. Donner takes the figurative "darkly
  troubled" sense; the colour stays latent. Cell = (latent-written, absent) =
  **LATENT-UNREALIZED**, starred.
The same Greek verb; one translator colours it, the other darkens it. **This is
the paper's founding claim measured for the first time** (c7a7fb2: "the Antigone
20 is the showcase cell's ONLY possible occupant" — now occupied, REVIVAL).

## BOARD PROVENANCE
### Source (grc)
- **Sophocles, ΑΝΤΙΓΟΝΗ vv. 1–20** (the opening Antigone/Ismene stichomythia,
  Πρόλογος). Digital edition: **Perseus Digital Library, ed. Francis Storr (Loeb
  1912)**, CTS urn:cts:greekLit:tlg0011.tlg002; text retrieved from Perseus
  dltext (doc=Perseus:text:1999.01.0185) 2026-07-28, cross-checked (vv. 1, 11,
  20) against an independent polytonic rendering of the same standard edition.
- **PD:** ancient Greek wording + the Storr 1912 edition both public domain.
- **Encoding:** Perseus served beta-code; converted to Unicode polytonic by a
  deterministic beta-code→Unicode map (breathings/accents/iota-subscript/final-
  sigma/capitals), NFC-normalized. The Greek was NEVER reconstructed from memory
  (house STOP rule) — it is Perseus's own text, mechanically re-encoded, then
  verified. File: `sophocles_grc_source.txt` (its header carries the full note).

### Seats
| seat | edition | date | PD/F9 | lines | v.20 colour |
|---|---|---|---|---|---|
| grc:sophocles_storr | Perseus/Storr Loeb | 1912 | PD (quoted) | 20 | latent-written καλχαίνω (LSJ) |
| de:hoelderlin_1804 | Trauerspiele des Sophokles, Wilmans (Indiana scan) | 1804 | PD (quoted in full) | 21 | **stated rot** |
| de:donner_1868 | Antigone, dt. Donner, Winter | 1868 | PD (quoted in full) | 22 | silent |

### Dropped seats (declared, effort-capped)
- **en:lloyd_jones_loeb** — Loeb/Lloyd-Jones 1994 IS in copyright. F9 = token-only,
  no full lines committed. SKIP-and-declare for this exhibition (the F9 redaction
  path is not implemented in the exhibition scorer; not worth the effort here).
- **de:solger_1808** — Solger 1808 scan (books/antigone/): heavy long-s (ſ) OCR
  corruption, the Antigone play text not cleanly located near its opening in the
  multi-play volume (pages checked show the Ajax play + commentary cross-refs).
  Drop-and-declare (dirty extraction), within the ~30-min cap.
- **mt (any)** — ancient-Greek MT is noise. Declared skipped (no MT seat), per
  the standing rule.
Minimum viable board (grc source + Hölderlin 1804) is EXCEEDED: grc + Hölderlin +
Donner landed.

## VERSE RANGE (documented)
Sophocles Antigone **verses 1–20** on every seat — the self-contained opening
sisters' exchange, ENDING exactly on the target line (grc v.20 καλχαίνουσ᾽ ἔπος /
Hölderlin "ein rothes Wort zu färben"), so the crossing of interest sits at the
window's close. German expands the Greek (Hölderlin 21 lines, Donner 20 verse
lines over the 20 grc verses); the alignment map records the correspondence.

## OCR CLEANUP LOG (summary; per-seat logs in the seat files)
- **Hölderlin 1804** (Indiana scan pp.123–124): long-s ligature artifacts
  normalized — «weifs»→weiß, «dafs»→daß, «gesezgemäfs»→gesezgemäß (the ſs→fs
  misread). **1804 orthography KEPT** (rothes stays rothes, lezten/gesez/beyden/
  zweyen/Todten). Speaker headers de-spaced (ANTIGONÄ./ISMENE.). Each documented.
- **Donner 1868**: clean OCR, no long-s artifacts; only the inline printed verse
  numbers (5/10/15/20 = apparatus) stripped. 1868 orthography kept (jezt, deßhalb,
  Thor, Todten).
- **The roth→rot orthography fold is a LEXICON rule (kaikki-attested, cited), kept
  STRICTLY SEPARATE from OCR normalization** (the OCR log cleans the scanner; the
  labeler folds attested pre-reform spellings — two different layers).

## THE ORTHOGRAPHY FOLD (roth→rot class) + ACCEPTANCE TEST
`caesitas_proto/de_build/de_labelers.py` extended (v) PRE-REFORM th→t: admitted
ONLY on lemmas whose committed kaikki `forms` attest a t→th twin (the citation
gate). kaikki German attests it: the `rot` adj entry lists `roth` tagged
["alternative","obsolete"], and the standalone `roth` entry is glossed "obsolete
spelling of rot ('red')" with its own pre-reform paradigm (rother, am rothesten).
So the archaic base `roth` declines forward → rothes/rother/rothe/rothem/rothen
fold to rot. Over-generation guarded: no th-twin for lemmas kaikki does not
attest (grün→grühn NOT generated; amethyst/anthrazit's native-th not treated as
pre-reform). Scope: the fold admits th-variants for exactly `rot`, `rötlich`,
`morgenrötlich` (each kaikki-attested); `röthlich`/`morgenröthlich` are genuine
attested pre-reform forms.

**ACCEPTANCE TEST (printed, mandatory):**
`label_color_de("Was ist es, du scheinst ein rothes Wort zu färben?")` → `(True,
'rot', '')` — **fires rot.** (The 1804-exact "Was ist's…" form fires too.)
Selftest probe ADDED to `de_labelers.selftest()` (now 16/16, incl. the pre-reform
fire + the grühn over-generation guard). trait_labelers selftest stays 30/30.

## THE STRETCH — a CITED grc colour WRITTEN channel (LANDED)
`corpus/antigone_antigonae/grc_colour_etymon_lsj.json` — a snippet-scoped grc
colour-etymon inventory, **every row cited to LSJ s.v.** ONE row: καλχαίνω ←
κάλχη (purple murex, = πορφύρα). The other content lemmas of vv.1–20 were checked
against LSJ and carry NO colour sense (declared, not invented). Wired as the
grc WRITTEN channel ON THIS BOARD ONLY (never into trait_labelers / the census),
so καλχαίνω reads latent-written and the Hölderlin crossing lands REVIVAL. **It
landed** — REVIVAL ★, said plainly. LSJ = public domain (Perseus).

## NO-CENSUS-CONTAMINATION PROOF (the proof of isolation)
1. The v4.7 census wrapper (`linegrain_census_v47_61.py`) re-run AFTER the whole
   Antigonä build (incl. the de_labelers th→t edit) is **BYTE-IDENTICAL** to the
   Phase-1 output: sha256 `900e7297bf58fd71dfa200c11993e861cbd8cf20b8aff0992c41c48f5138184b`
   (unchanged). The paper census is untouched.
2. Re-scoring qingqing's de seats (bethge/heilmann) with the LIVE post-edit
   `de_labelers` gives **0 mismatches** vs the committed board — the th→t fold is
   provably INERT on the paper corpus (no pre-reform colour word occurs in any
   8-board de seat line; verified by scan).
3. `exhibit_gen.build_model('antigonae', …)` raises FileNotFoundError — the board
   is not in the paper JSON namespace at all.

## ALIGNMENT — **APPROVED** (the PI, 2026-07-28 afternoon: "yes to table but its own table")
The grc v.1–20 ↔ German-line map now lives as its OWN tables of record —
`antigonae__de_hoelderlin_1804.json` (20→21; v.3 expands to lines 3–4) and
`antigonae__de_donner_1868.json` (1:1) in this directory — extracted verbatim
from the scorer's inline draft (verified identical) and blessed at her word.
The scorer's inline copy stands as the executable mirror; any future edit
happens in the FILES first. PENDING banner retired.

## FILES
```
corpus/antigone_antigonae/
  sophocles_grc_source.txt                     # grc source vv.1-20 (Perseus/Storr, PD)
  hoelderlin_de_1804.md                        # Hölderlin seat (Indiana scan, PD) + OCR log
  donner_de_1868.md                            # Donner seat (PD) + OCR log
  grc_colour_etymon_lsj.json                   # the STRETCH: grc colour written channel (LSJ-cited)
  REGISTRATION_antigonae_exhibition_0728_61.md # this
publishable/antigonae_exhibition_board_61.py   # the exhibition scorer (isolated)
reports/figures/antigonae_exhibition/
  antigonae_board_61.json / .md                # scored board + human table
  exhibit_antigonae_rothes_wort_color.svg / .model.json  # the rothes-Wort colour panel (gated, xmllint)
```

## RULING-GATED FOR THE MORNING
- **Alignment map** — APPROVED 07-28 afternoon, own tables (see ALIGNMENT above); banner retired.
- The exhibition-tier claims (REVIVAL, the LSJ etymon channel) are staked as
  measured; the grc colour written channel is the paper's founding claim now
  quantified — hers to adopt into the narrative or hold as suggestive-tier.

## APPENDIX — the v.20 LATENT-CARRY hunt across the full shelf (#61 vigil, filed at her ask)
*Question: could any German rendering of v.20 occupy LATENT-CARRY (colour
latent both sides)? Answer: NO, by construction and by corpus. Receipts:*

| seat | translator | v.20 rendering | de_color verdict | status |
|---|---|---|---|---|
| grc source | Sophocles (Perseus/Storr) | καλχαίνουσ᾽ ἔπος | latent (LSJ etymon channel) | seated |
| Hölderlin 1804 | Wilmans | «Was ist's, du scheinst ein rothes Wort zu färben?» | **stated: rot** (roth→rot fold) → REVIVAL★ | seated |
| Donner 1868 | | «Was hast du? Düster wogt in dir ein schweres Wort» | silent → LATENT-UNREALIZED★ | seated |
| Böckh 1843/1912 Insel | | «Was ist es? Sicher wogt in dir ein schweres Wort.» | silent (file-verified, PD) | spare witness, not seated |
| Solger 1808 | | web-attested only («…tief aufwogend Wort…») — zip OCR unusable | silent (unverifiable in-file) | declared drop |
| Weinstock 1957 Kröner | | [F9 — tokens only: *sinnst* · *finsteres Wort*] | silent (dark-adjective, not colour) | read-only, no F9 candidate |
| Steinmann 2015 Reclam | | [F9 — tokens only: *wühlt* · *Kunde* (ἔπος→news)] | silent | read-only, no F9 candidate |

**Why the cell is unoccupiable here, three levels:** (1) no de latent-written
instrument exists (declared UNAVAILABLE, deterministic-latent-written-fields
README L71); (2) the board's de path emits stated|silent only; (3) empirically
no German v.20 rendering carries ANY colour word — of seven translators across
two centuries, one colours the verb (Hölderlin), six take the dark/wave sense.
One verb, seven fates: the split the fields predict, enacted by the shelf.
Census contamination re-proof at hunt's end: findings_v47 sha byte-identical.
