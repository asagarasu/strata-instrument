*[07-23 (updated same night): EXPIRED — the PI's word ("licensing of LLM is expired"); the whole branch incl. the Step-7/CONTAINMENT portability design is dead. Originally noted: the licensing line was ruled DEAD wholesale (her ruling 07-20) and the operative methodology forbids LLM marking entirely. Kept as record; the collaborator's eyes-slot question is presumed obsolete pending the PI's confirmation. (Codex comprehensibility audit 07-23 evening)]*

# Ruling: licensing criterion AMENDED — subcommittee-symmetric (2026-07-16)
*An, in session, on seeing the leave-one-out control (every human
fails the original criterion: A 10/14 · C 10/14 · K 6/6 · S 12/14).
Verbatim: "Then we use this as the license granter: (Anneliese
10/14, the collaborator 10/14, Marker K 6/6, Marker S 12/14)." Amends
ruling_licensing_criterion_20260716 (same night); the original
per-poem two-sided BANDS survive as the check unit — what changes
is the pass rule.*

## Formalization (chair's, declared under her rule — one choice was
## load-bearing and is flagged for her nod)
Naive reading (machine's fail-rate vs full-pool bands ≤ humans'
LOO rates) was not adopted (asymmetric): machines faced wider 4-human
bands than the humans' 3-human LOO bands. Adopted form is fully
symmetric:

For each subcommittee P = pool minus one human h:
  bands B_P from P's pairs; machine M and excluded human h face the
  SAME B_P and the same checks (vs each member of P, per poem,
  per language). M passes P iff rate(M|P) ≤ rate(h|P).
M is licensed per language iff it passes EVERY subcommittee with
checks in that language. Each check remains two-sided (over-
agreement still violates — contamination detection retained); the
meta-comparison is one-sided (violating LESS than the excluded
human is virtue, not anomaly).

## Verdicts under the amended criterion (license_check.py --amended)
| model | zh | en |
|---|---|---|
| Codex GPT-5.6 | **LICENSED** | (vacuous — see below) |
| Gemini 3.1 Pro Ext | not licensed (fails −A 7/10>6/10, −S 9/10>8/10) | (vacuous) |
| Claude Opus 4.8 | not licensed (fails −A 8/10>6/10) | (vacuous) |

**zh is a real, discriminating verdict** — Marker K's marks give
3-human subcommittees with genuine bands (12-check cells exist).
**en is VACUOUS at current n**: only three humans mark en, so every
subcommittee leaves a single pair → point bands → human and machine
both fail 4/4 → "≤" holds trivially. En licenses are NOT granted;
recorded as CRITERION INAPPLICABLE at n=3 en markers (a 4th
en-marking human would activate it). This limit ships with the
table (A8 register).

## Net licensing state for the the collaborator package
- **Codex GPT-5.6: licensed for zh** — the pool's first licensed
  machine. (Its full-pool failure mode was honest under-agreement.)
- Gemini 3.1 Pro Extended, Claude Opus 4.8: not licensed (zh);
  en inapplicable for all.
- DeepSeek: did not enter (task comprehension).
- Standing rules unchanged: Claude never sole marker (moot — not
  licensed); licensed machines extend the instrument to texts
  outside the committee's reach, per statement §5.
