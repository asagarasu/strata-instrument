# Marking pack v2 — instructions, template, normalization

*Chair, 2026-07-05. The single file relayed to markers (zh version via codex). Scheme: tagset v2. Markers: Anneliese, Marker K, Sylvaine, the collaborator + licensed machines later.*

## What you are doing

You'll read short classical poems and, for each line, write down what the wording puts in front of you — as `field, value` pairs. You are describing the words, not interpreting the poem. There are no wrong fields; invent whatever categories feel natural. Ten minutes per poem is plenty.

## The five rules

1. **Point or don't tag.** Every mark must attach to a specific word or phrase in the line. If you can't point at it, don't write it.
2. **Wording, not situation.** Mark what the words carry, not what you infer. A poem about an abandoned wife is *sad as a situation* — but you only mark sadness if a sadness-word is on the page.
3. **`field, value` — loosely.** `color, white` · `plant, dense` · `temporal, long` · `person, beautiful`. Values may be sizes/intensities (`wetness, small` for dew; `wetness, medium` for a river). A bare field is fine when the value is hard (`action` alone is a good mark; don't force "hostile vs. neutral" if the word won't say).
4. **Sound counts.** Repeated words/syllables (`word, repetitive`), rhyme, jingling — if the line makes noise, mark the noise.
5. **Sparse and honest.** Three marks you can point at beat eight you guessed. Skipping a line entirely is a legal answer.

## Worked examples (deliberately not from the poems you'll mark)

- Hölderlin renders a Greek line as *"ein rotes Wort zu färben"* (to dye a word red) → `color, red` · `action` (dyeing) · the color is *in the wording*, so it's marked — even though the conventional translation ("brooding") has no color at all.
- English *"consider the options"* → no marks. (The word "consider" secretly contains Latin for "star." You can't see the star from the sentence, so it isn't there. If you need a dictionary to find it, don't mark it.)
- 「法律面前人人平等」 → `person` · no water mark for 法 — the water in 灋 is invisible in modern wording. Same principle as "consider."

## Blindness rules (matter for the statistics)

- Don't look at any *translation* of a poem before or while marking its original.
- Don't discuss your marks with other markers until the collection is closed.
- If you've read a poem's famous translations before in life, that's fine — just mark the original as it sits on the page today.

## Per-poem sheet template

```
POEM: <title> — <source, provenance line copied from corpus file>
MARKER: <name>   DATE: <date>   LANGUAGE(S) YOU READ THIS IN: <zh/jp/en/...>

L1 <line text>
marks:

L2 <line text>
marks:

...
```

Return in any medium — filled file, chat message, paper photo. Format police do not exist; the normalization step (below) absorbs variation.

## Dev-set poems (proposed, vetoable)

1. 玉阶怨 (李白) — pilot poem; fresh for Marker K/Sylvaine/the collaborator; Anneliese+chair marks join with contamination asterisk
2. 古诗十九首·青青河畔草 — same status
3. 长干行 (李白) — triple-covered (Pound/Obata/Lowell), long: mark first 8 lines only
4. 送友人 (李白) — triple-covered, short
Haiku + sonnet + Baudelaire dev units to be appended when those clusters' sheets are cut (same pack, same rules).

## Normalization spec (chair-side; markers can ignore)

After collection, before any statistic:
1. Build a **field-synonym map** across markers (e.g. wetness/water/moisture → one field). Merge only clear synonyms; when in doubt, don't merge. Every merge is logged in a published mapping table; original strings preserved.
2. Scalar values normalized to a 3-point scale (small/medium/large); categorical values lower-cased, synonym-mapped the same way.
3. Agreement (per-category Jaccard, per protocol) computed on normalized marks; raw-string agreement reported alongside so the normalization's contribution is visible.
4. Machine marks pass through the identical map — built once, from human marks only, *before* machine marks are unblinded. (Prevents tuning the map to help a model pass licensing.)
