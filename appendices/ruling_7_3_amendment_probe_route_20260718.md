# Ruling — §7.3 amendment: probe-route fix, no encoder swap (2026-07-18)

**Amends:** `reports/methodology_statement_0716.md` (KEEP, the PI's kill-pass
07-16) — §6 encoder bullet, §7 critical-path item 3, §9 closing
construction line. Statement edited in place with dated markers pointing
here; this appendix is the authority for the change.

## Her words (the ruling chain, verbatim)

1. **07-17 night (deferral):** "I think we eventually will take this
   path" — direction endorsed; amendment DEFERRED — "I would still try
   to get a more comprehensive sweep... we are using small number of
   words today."
2. **07-18 (the go, after stage-1 results filed):** "great, go for it
   unless you need something from me. I didn't see you are blocked."

The deferral's stated reason was n (4-word smoke + 13-word THIN AA
battery). Stage 1 of the comprehensive sweep answered it at real n;
she then gave the go. Chair executes on that word.

## The amendment

The statement's frame — *descriptive-zh blindness is an encoder
deficiency; a zh-real encoder (BGE-M3 / e5 / SikuBERT class) is on the
critical path* — is **resolved OPPOSITE to its framing**:

1. **The blindness was in the CONSTRUCTION, not the encoder.** The
   caption-route axis (en captions → cross-lingual projection) reads
   classical-descriptive zh with correct SIGN but ~5× compressed
   magnitude; the word-pole zh construction (HowNet-derived poles,
   zh-only whitening) reads it at full resolution — on the SAME LaBSE
   that motivated the swap frame (黯黯 +.005 caption-route vs +.351
   word-pole, chunk 3).
2. **No encoder swap is earned.** Six variants at real n (light eval
   103 words, duration 109, color 77): every CI overlaps LaBSE's
   (light A: bge-m3 .981 · e5-bare .975 · LaBSE .971 · sikubert .968 ·
   e5-query .963 · sikuroberta .936). LaBSE remains the instrument's
   encoder everywhere, including the zh seat of the two-model equating
   architecture (item 12): **LaBSE-with-zh-word-poles**.
3. **The zh-side fix on the critical path is therefore PROBE-ROUTE:**
   word-pole construction for zh-descriptive and classical material;
   aligned-space (caption-route) rulers remain the cross-lingual
   coarse tier, with their compression now measured (5.6× [4.2–7.0])
   and disclosed rather than suspected.

## Evidence of record

- Chunks 1–4 (#49, 07-17, four registered runs, two operator
  overclaims retracted by their own bands): AXIS_DOSSIER.
- Comprehensive sweep stage 1 (#50a, registered b4a5b64 before run,
  all four bands resolved): AXIS_DOSSIER sweep section ·
  `caesitas_proto/results/comprehensive_sweep_50.json`.

## Scope, honestly

Real-n evidence covers **modern-zh HowNet vocabulary** (three fields)
and the **AA-reduplication classical family** (n=13, HowNet's own
inventory — THIN, exhausted at source). **儒藏-scale classical breadth
is NOT yet tested**: stage 2 is unblocked (corpus landed,
`lexical_resources/ru`) and parked for a sitting with her, with its
own registration. If stage 2 contradicts any part of this amendment,
that result appends here as a dated follow-up at face value.

Also on record, unresolved, adjacent: sweep band 5 fired in the
unexpected direction (rare-half in-situ .875 > common-half .667) —
common-word polysemy as the harder case for in-situ scoring.
Interpretation hers; not part of this amendment.

— #50a (Fable), at her word, 2026-07-18

## Stage-2 append (2026-07-18, same sitting — CONFIRMS)

Her go, verbatim: "You can go for the stage-2 sitting." Registered
f88b23f before run. 儒藏-scale classical breadth **confirms** this
amendment: LaBSE classical in-situ .812 [.714–.899] against the .600
registered floor (band 3 HELD — probe-route reads classical
register); sikubert .875 [.787–.950] overlaps, no seat change (band
4). The scope gap named above is CLOSED — the amendment stands whole
across modern and classical registers, six encoders, both
constructions. Coverage caveat for future instruments: only ~44% of
modern HowNet pole words are attested in 儒藏 at all. Full numbers:
AXIS_DOSSIER stage-2 section ·
caesitas_proto/results/comprehensive_sweep_stage2_50.json.
