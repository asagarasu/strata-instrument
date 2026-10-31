# Tag scheme v2 — post-pilot redesign

*Chair, 2026-07-05, after pilots #1 (玉阶怨) and #2 (青青河畔草). v1 is dead; long live the marker who killed it. Core change: the human layer adopts Anneliese's native ontology — concrete `field, value` pairs — and everything abstract moves to the machine layer or the grave.*

## Human layer (what markers do)

**Format: `field, value` pairs per unit** (unit = poem line / whole haiku). Values may be:
- categorical (`color, green` · `person, female` · `temporal, past`)
- **scalar** (`wetness, small|medium|…` · `volume, dense|thin` · `space, small|medium|empty`) — pilot evidence: scalar use is internally coherent across poems (dew-small < river-medium)
- bare when value is hard (`action` · `furniture` · `alone`) — a bare field is a valid mark; forced values breed noise (pilot #1's "hostile or straight?" lesson)

**Field vocabulary: semi-open.** Core lexicon (color, light, wetness/water, plant, space, volume/density, temporal, person, body, action, material, furniture, sound…) offered as examples, not a menu; markers may coin fields. Cross-marker normalization (synonym-mapping of coined fields) happens downstream, never during marking.

**Sound devices marked as fields too:** `word, repetitive` (叠字), rhyme, onomatopoeia. Pilot evidence: per-line repetition marks compose into belt-and-cutoff structure automatically — no lattice instruction needed, no extra burden.

**Rules (unchanged in spirit):** point or don't tag · wording not situation · sparse honest marks · full poem visible, tag only the unit.

**Killed from the human layer, with cause:**
- `figure-*` — replaced by machine field-clash detection (a word's home field vs its scene)
- `figure-symbol_conventional` — requires cultural interpretation; both pilots' marker practice refused it; Rule 4 agrees
- `register-*` — abstract; the concrete fields carry it (玉阶's courtliness lives in `stone, precious`)
- agency + Vendler aspect — linguist categories; markers produce flat `action`; moved to machine layer
- evaluative fields (beauty) — RESOLVED (Anneliese, 07-05): no beauty *field*; beauty is a **value on an existing field** — `person, beautiful` (娥娥), legal because the word itself is the evaluation (pointable wording, not situation-inference). Waley's "Fair, fair" confirms the trait transits.

## Machine layer (computed, never asked of humans)

1. **Field-clash detection**: home-field lexicons per content word; clash = home field ∉ scene fields. **Calibrated per reader population** — audit cases: 侵-hostile LIVE (marker's own translation restored it), 盈-fullness LIVE (`volumn, dense`), 玲珑-sound LIVE, 守-military **NOT live** (marker: `action, still`; Waley: "keep"), 素-silk not live, 秋-fire dead, 望-月 dead-orthographic.
2. **Latent liveness by coverage, not questionnaire**: generate decomposition candidates; a candidate is live-for-population iff native active marks cover its field. (Pilot #2: marker ignored all accept/reject checkboxes and simply marked what was alive. The interface should stop asking.)
3. **Lattices via aggregation**: repetition belts + cutoffs (L1–6 → L7), field through-lines (jade lattice: 玉阶→水晶→玲珑), scalar gradients (the zoom: space marks narrowing), chain repetition (荡子…荡子).
4. **Structural deltas**: pro-drop vs forced subject (Pound's inserted "I"), classifier/number, tense-marking asymmetries — scored as language-pair constants, charged to no translator.
5. Vendler aspect & agency distribution — parses, machine-only, validated on a linguist-marked gold subset if the companion paper wants them; out of sprint scope.

## Conformance checks this scheme feeds (per unit and per lattice)

field survives / field transplanted (盈盈→"midmost of her youth") / field deleted (空床 → ∅ in Pound) / field invented ("sot": drunkenness ∉ source) / scalar shifted / belt kept-with-cutoff (Waley 6/6 ✓) / clash preserved (侵: soaks=gradual-only, ruined=adversative-only).

## Standing audit table (updated known answers)

| case | verdict | source |
|---|---|---|
| καλχαίνω purple | live-latent | philology (seed case) |
| 玲珑 jingle | live-active for native | pilot #1 |
| 盈盈 fullness | live-active for native; "Sad, sad" = situation-tag violation | pilot #2 + Waley diff |
| 侵 hostile | live (restored in marker's own translation) | pilot #1 discussion |
| 守 military | not live for native pop — clash-detector calibration case | pilot #2 |
| 素 silk ghost | not live (unmarked) | pilot #2 |
| 秋 fire, 望-月, consider-sidus, 法-water | dead | pilots + tagset v1 |

*For kill-pass: the semi-open vocabulary trades some agreement-computability for marker honesty — the normalization step must be specified before the human round (chair task, with the marking interface).*
