# Ezra Pound — rendering of Li Bai 黃鶴樓送孟浩然之廣陵 (the Yellow-Crane mini-board, en SEAT)

**Edition.** Ezra Pound, *Cathay* (London: Elkin Mathews, 1915), "Separation on the River Kiang"
(Pound's rendering of Li Bai 黃鶴樓送孟浩然之廣陵; Pound gives the poet as "Rihaku", the Japanese
reading of 李白, following the Fenollosa notebooks). Pound's *Cathay* is "for the most part from
the Chinese of Rihaku, from the notes of the late Ernest Fenollosa, and the decipherings of the
professors Mori and Ariga."

**Source of this transcription (house F9 / provenance).** Project Gutenberg **eBook #50155**,
*Cathay, by Ezra Pound* — fetched from https://www.gutenberg.org/files/50155/50155-h/50155-h.htm
on 2026-07-05 into `corpus/tang_en/raw/pound_cathay_1915.txt` (converted from the fetched HTML
`pound_cathay_1915_raw.html` with `pandoc -f html -t plain`, no wording changed). "Separation on
the River Kiang" begins at **line 479** of that committed file (title line) — the five body lines
are lines 480–484. The lines below are copied verbatim from that committed corpus file; no line was
re-typed from memory. Cross-checked line-for-line against the fetched file.

**PD (stated, F9).** Pound's *Cathay* (1915) is **public domain** — published 1915, U.S. public
domain per the Project Gutenberg license terms (PG #50155). Under house law F9 this PD translation
is quoted freely, in full, with its public-domain status stated.

**The target line.** Pound renders zh L3 孤帆遠影碧山盡 ("the lone sail's far shade into the
jade-green hills fades") as **body line 3**, "His lone sail blots the far sky." This is the crossing
of interest on the **COLOUR** axis: the zh graph 碧 (jade-green / azure) states a colour; Pound's
line names "the far sky" but no explicit hue-word ("blue"/"green" do not appear). The task's
expected family was a colour loss — measured HONESTLY, what the live instruments say is reported
(see the alignment JSON and the registration; the surprises are that 碧 does NOT fire the zh word
colour boolean — it is deliberately held latent in the term set — and that "sky" charges the en
word colour, so the crossing is an INVENTION, not the loss the reading pass anticipated).

**LINE-COUNT NOTE (a line-boundary event, DECLARED — not silently normalised).** Pound's rendering
has **five** body lines against the poem's **four** verse-lines. Pound SPLITS the final zh
verse-line 唯見長江天際流 across TWO of his lines ("And now I see only the river," / "The long Kiang,
reaching heaven."). The first three zh verse-lines map 1:1 to Pound's first three body lines; the
fourth zh line maps to Pound's fourth AND fifth. This is exactly the "translator does something wild
(a split / inserted line)" case that makes alignment a live question (the PI's standing note; the same
4→5-style split the 送友人 board declared for its final line). The alignment file records the split as
`{src: 4, seat: [4, 5]}`. The L3 TARGET is a clean 1:1 (zh L3 ↔ Pound body line 3), unaffected by
the split. Declared here, in the alignment JSON, and in the registration.

## Pound's rendering (title + 5 body lines, verbatim, Pound's lineation)

Separation on the River Kiang

Ko-jin goes west from Ko-kaku-ro,
The smoke-flowers are blurred over the river.
His lone sail blots the far sky.
And now I see only the river,
The long Kiang, reaching heaven.
