# Baudelaire cluster manifest: "Correspondances" and "L'Albatros" across fr / zh / en / de

Compiled 2026-07-05. Two target poems throughout: **Correspondances**
(Spleen et Idéal IV, 1861 numbering) and **L'Albatros** (Spleen et
Idéal II, 1861). Raw gathering, provenance, and locate-only research —
no passage selection performed. Every "translator did/didn't include
this poem" claim below was verified against a full table of contents
or full fetched text, not taken from secondary summaries, except where
explicitly flagged otherwise.

## Edition finding (fr) — verified, and it matters for the whole cluster

*Les Fleurs du mal* had two lifetime editions: 1857 (Poulet-Malassis,
100 poems, 6 suppressed by the 20 August 1857 court order) and 1861
(expanded, 35 new poems, new "Tableaux parisiens" section).

- **"Correspondances" is in BOTH editions** — confirmed in the 1857
  table of contents on fr.wikisource (Spleen et Idéal, p. 19) and on
  fleursdumal.org's 1857 TOC (listed as poem 103). It is not one of
  the six condemned poems.
- **"L'Albatros" is in the 1861 edition ONLY** — it appears nowhere in
  either site's 1857 TOC. It entered the collection in 1861 as Spleen
  et Idéal II (between Bénédiction and Élévation); first periodical
  publication was the *Revue française*, 10 April 1859. The task
  brief's recollection is confirmed by direct TOC inspection, not
  assumed. (fleursdumal.org's 1861 TOC marks it with the red guillemet
  it uses for poems new relative to the other edition.)
- Consequence: any translation of L'Albatros necessarily derives from
  the 1861 text (or later); Correspondances translations could derive
  from either. All files in fr_source/ save the 1861 text.
- Line-level 1857-vs-1861 collation of Correspondances was NOT done:
  fr.wikisource has no per-poem 1857 transcription (the page returns
  "aucun texte" — kept as fr_source/correspondances_1857_raw.html to
  document the dead end), and fleursdumal.org shows a single French
  text per poem without variant apparatus. No claim either way about
  1857/1861 variants in this poem.

## Files fetched (all with provenance headers; raws unmodified)

| File | Source | URL | Fetch date |
|---|---|---|---|
| `fr_source/correspondances_fr_1861.txt` (+ `correspondances_1861_raw.html`) | Baudelaire, Les Fleurs du mal, 2nd ed. (Poulet-Malassis et de Broise, 1861), pp. 15-16; Wikisource "Texte validé" | https://fr.wikisource.org/wiki/Les_Fleurs_du_mal_(1861)/Correspondances | 2026-07-05 |
| `fr_source/albatros_fr_1861.txt` (+ `albatros_1861_raw.html`) | same edition, pp. 11-12 | https://fr.wikisource.org/wiki/Les_Fleurs_du_mal_(1861)/L%E2%80%99Albatros | 2026-07-05 |
| `fr_source/correspondances_1857_raw.html` | negative-result documentation only (empty Wikisource page) | https://fr.wikisource.org/wiki/Les_Fleurs_du_mal_(1857)/Correspondances | 2026-07-05 |
| `zh_target/dai_wangshu_xintianweng.txt` | 戴望舒《信天翁》, 《恶之花掇英》(怀正文化社 1947; repr. 《戴望舒译诗集》湖南人民出版社 1983) | https://www.zhonghuadiancang.com/leishuwenji/16752/322808.html (301→ https://www.diancang.xyz/leishuwenji/16752/322808.html) | 2026-07-05 |
| `zh_target/dai_wangshu_yinghe.txt` | 戴望舒《应和》, same volume | same URL | 2026-07-05 |
| `zh_target/dai_wangshu_translations_raw.html` | unmodified raw for both Dai poems (whole translations page) | same URL | 2026-07-05 |
| `zh_target/dai_wangshu_yinghe_douban_crosscheck_raw.html` | independent reproduction of Dai's 应和 used for cross-check (two small reading variances flagged in the .txt header) | https://site.douban.com/217222/widget/notes/14334787/note/292551579/ | 2026-07-05 |
| `en_target/scott_echoes_correspondances_1909.txt` (+ `scott_flowersofevil_1909_raw.html`) | Cyril Scott, "Echoes" [= Correspondances], The Flowers of Evil (Elkin Mathews, 1909) | https://www.gutenberg.org/files/36098/36098-h/36098-h.htm (PG #36098); cross-checked vs archive.org item flowersofevil00bauduoft | 2026-07-05 |
| `en_target/sturm_correspondences_1906.txt` (+ `sturm_correspondences_1906_raw.html`) | F. P. Sturm, "Correspondences", The Poems of Charles Baudelaire (Walter Scott Publishing, 1906) | https://en.wikisource.org/wiki/Poems_of_Charles_Baudelaire/Correspondences; cross-checked vs 1919 Huneker reprint (archive.org poemsprosepoemso00baud) | 2026-07-05 |
| `de_target/george_der_albatros.txt` (+ `george_der_albatros_zeno_raw.html`) | Stefan George, "Der Albatros", Die Blumen des Bösen: Umdichtungen (Bondi, 1901; text per Gesamt-Ausgabe Bd. 13/14, 1930, pp. 13-14) | http://www.zeno.org/nid/20004818741 | 2026-07-05 |
| `de_target/george_einklaenge.txt` (+ `george_einklaenge_zeno_raw.html`) | Stefan George, "Einklänge" [= Correspondances], same volume, pp. 16-17 | http://www.zeno.org/nid/20004818768 | 2026-07-05 |
| `de_target/george_blumendesboesen_1901_archiveorg_ocr_raw.txt` | unmodified OCR of the 1901 Bondi first edition, used to cross-check both George poems and the volume's Inhalt | https://archive.org/download/dieblumendesbs00bauduoft/dieblumendesbs00bauduoft_djvu.txt | 2026-07-05 |

**Fetched poem texts: 7** (2 fr, 2 zh, 2 en, 2 de — of which one en is
"Correspondances only"; there is NO fetched English or additional
fetched Chinese "L'Albatros" beyond Dai — see Gaps).

## PD determinations (translation copyright is separate from the original's)

The French originals are trivially PD everywhere (Baudelaire d. 1867).
Every *translation* carries its own copyright clock, independent of
the original's status. Per item:

| Translator | Died | Determination |
|---|---|---|
| 戴望舒 Dai Wangshu | 1950 | **PD in China since 1 Jan 2001** (life+50). Fetched. |
| Cyril Scott | 1970 | **US-PD only** (1909 publication, pre-1929). Still in copyright in life+70 jurisdictions until 1 Jan 2041. Fetched on the US basis; flagged in file header. |
| F. P. Sturm | 1942 | **PD everywhere relevant**: US via 1906 publication; UK/EU since 1 Jan 2013 (life+70). Fetched. |
| Stefan George | 1933 | **PD everywhere relevant**: Germany/EU since 1 Jan 2004 (life+70); US via 1901 publication. Verified independently of Zeno.org's "Gemeinfrei" label (and NOT sourced from Projekt Gutenberg-DE, whose inclusion would not prove PD). Fetched. |
| 钱春绮 Qian Chunqi | 2010 | **In copyright** (China life+50 → 2061). Locate only. |
| 郭宏安 Guo Hong'an | **16 Jan 2023** (confirmed — 界面新闻 obit, https://www.jiemian.com/article/8760485.html; he was NOT still living, contra the task brief's uncertainty) | **In copyright** (→ 2074 in China). Locate only. |
| William Aggeler | **death date NOT FOUND** (searched; he taught French at UC Santa Barbara for 30 years per UGA Press author page — no obituary/dates located) | **Treated as in copyright**: 1954 US publication is inside the 95-year window regardless of death date (→ 1 Jan 2050 at the earliest if renewed). Locate only. |
| Roy Campbell | 1957 | **In copyright**: UK/EU life+70 runs to 1 Jan 2028 (close, but not yet). US: 1952 publication → 95-year term to 2048 IF renewed; **renewal status not verified** (Stanford renewal DB not consulted — flagged as unverified rather than assumed either way). Locate only. |
| Edna St. Vincent Millay (d. 1950) / George Dillon (d. 1968) | — | **In copyright in the US** (1936 publication, renewal near-certain for a Harper title → to 1 Jan 2032). Locate only. |
| Arthur Symons | 1945 | **PD everywhere relevant** (UK/EU since 1 Jan 2016; US via 1925 publication) — but see Gaps: no fetchable digitization found. |

### fleursdumal.org's permission framing — reasoned through, as instructed

Site's own words (home page, https://fleursdumal.org/, fetched
2026-07-05): "Most of the translations that appear on fleursdumal.org
have appeared previously in book form... they are ones that the site
felt comfortable reproducing in terms of rights. If you are a rights
holder and object to your translations being included here, please
contact fleursdumal.org to discuss the issue." Footer: "© 2026 • All
rights reserved." No terms/FAQ page granting reuse was found.

**Determination:** this is a risk-tolerance posture plus a
notice-and-takedown offer, NOT a statement that the texts are freely
reproducible, and the site's own footer asserts all-rights-reserved.
The task's conditional ("follow the site's own claim if it says the
text is freely reproducible") is therefore NOT triggered. Aggeler and
Campbell remain locate-only. This is a determination from the site's
actual language, not a default to caution.

## Located only (in copyright, or not fetchable) — what and where

**钱春绮 (Qian Chunqi), 《恶之花》:**
- Editions: 人民文学出版社 1986; 1991 (ISBN 9787020011292); 《恶之花
  巴黎的忧郁》人民文学出版社 2011 (ISBN 9787020082018).
- His rendering of Correspondances is titled **《感应》**; quoted in
  full with "钱春绮译" credit at
  https://www.shigeku.com/shiku/ws/wg/baudelaire/004.htm and
  https://www.shigeku.com/shiku/ws/wg/baudelaire.htm (with his
  edition-note on the poem's 1845/1855 dating and the Hoffmann
  passage). His 《信天翁》 opens "常常，为了消遣，航船上的海员…" —
  quoted at https://zhuanlan.zhihu.com/p/31364707 (attribution per
  search-level verification only; the page itself was not fully
  fetched — weaker evidence than the shigeku pages).
- Note: shigeku.com pages are GB2312-encoded; fetch as gb18030.

**郭宏安 (Guo Hong'an), 《恶之花》:**
- Editions: 漓江出版社 1992 插图本 (ISBN 9787540708641); 广西师范大学
  出版社 2002 (ISBN 9787563337019); 上海译文出版社 2011 (ISBN
  9787532753932) and 2013 (ISBN 9787532763757); also 《恶之花：
  波德莱尔诗歌集注》(商务印书馆, bbtpress listing).
- His 《信天翁》 quoted in full with "郭宏安译" credit at
  https://www.shigeku.com/shiku/ws/wg/baudelaire/002.htm; his 《应和》
  ("自然是座庙宇，那里活的柱子…") quoted with credit at
  https://www.shigeku.com/shiku/ws/wg/baudelaire.htm and
  https://www.pinshiwen.com/gsdq/zwms/20190624124822.html.
- Title-collision warning recorded in the Dai file headers: 应和 is
  BOTH Dai's 1947 title and Guo's later title for Correspondances;
  钱春绮 uses 感应, 文爱艺 契合. Title alone does not identify the
  translator.

**William Aggeler, The Flowers of Evil (Fresno, CA: Academy Library
Guild, 1954):**
- Both target poems reproduced in full (English + French) on
  fleursdumal.org: Correspondances at https://fleursdumal.org/poem/103,
  L'Albatros at https://fleursdumal.org/poem/200, each with the
  citation line "— William Aggeler, The Flowers of Evil (Fresno, CA:
  Academy Library Guild, 1954)".
- Modern reprints: Digireads/Neeland Media ISBN 9781420951189 (with
  the F. P. Sturm introductory study); bilingual reprint ISBN
  9781684227471.

**Roy Campbell, Poems of Baudelaire: A Translation of Les Fleurs du
Mal (New York: Pantheon Books, 1952; London: Harvill, 1952):**
- Both target poems on the same two fleursdumal.org pages
  (poem/103, poem/200), citation line "— Roy Campbell, Poems of
  Baudelaire (New York: Pantheon Books, 1952)".
- Complete translation (so both poems are certainly his), pre-ISBN
  edition; JSTOR-reviewed on publication
  (https://www.jstor.org/stable/27538396).

**Edna St. Vincent Millay & George Dillon, Flowers of Evil (New York:
Harper & Brothers, 1936):**
- First edition: bilingual (French/English facing), 282 pp., with
  Millay's preface; pre-ISBN.
- In-print reprint: *Flowers of Evil* (NYRB Poets), ISBN
  9781681378282 — https://www.nyrb.com/products/flowers-of-evil.
- Dillon's Correspondances rendering is quoted on
  https://fleursdumal.org/poem/103 and his Albatross on
  https://fleursdumal.org/poem/200 ("— George Dillon, Flowers of
  Evil (NY: Harper and Brothers, 1936)"). NOTE: the 1936 volume was a
  co-translation with poems individually credited; the fleursdumal
  citations for these two specific poems name Dillon, not Millay.
  Whether Millay herself also rendered either target poem was not
  determined.

**Arthur Symons, Les Fleurs du Mal / Petits Poèmes en Prose / Les
Paradis Artificiels (London: The Casanova Society, 1925):**
- The only pre-1929 (hence US-PD) *complete* English Fleurs du mal
  found — it would contain L'Albatros. Symons d. 1945 → also PD in
  UK/EU since 2016. **But no fetchable digitization was located**:
  HathiTrust has a catalog record (
  https://catalog.hathitrust.org/Record/008414438 ) whose item pages
  returned 403 to automated access; archive.org has no scan (searched
  creator:baudelaire + symons — only his 1913 Poems in Prose and the
  1927 Letters). Located-PD-but-not-fetched.

## Gaps — with "not found by me" vs "translator didn't do it" separated

**Translator-confirmed negatives (not search gaps):**
1. **Cyril Scott (1909) did NOT translate L'Albatros.** Verified two
   ways: full TOC of the 1909 edition (PG #36098 and the archive.org
   scan) contains no Albatross title; case-insensitive full-text
   search for "albatross" in both complete copies: zero hits. His
   selection (~54 poems) includes Correspondances (as "Echoes") but
   skips L'Albatros entirely.
2. **F. P. Sturm (1906) did NOT translate L'Albatros** — same
   double-check (Wikisource TOC + full-text search of the 1919
   Huneker reprint of Sturm's renderings: zero "albatross" hits).
3. **J. C. Squire, Poems and Baudelaire Flowers (New Age Press, 1909)
   contains NEITHER target poem** — full TOC read in the archive.org
   scan (poemsbaudelairef00squi); it has Elevation, The Enemy, etc.,
   but no Correspondances and no Albatross.
4. **戴望舒 DID translate both target poems** — the expected negative
   did not materialize. Despite selecting only 24 of the poems for
   《恶之花掇英》 (16 from Spleen et Idéal per 中国作家网's account,
   https://www.chinawriter.com.cn/n1/2021/0611/c404092-32128340.html),
   both 《信天翁》 and 《应和》 made his cut. Verified from the
   reproduced text itself, not a secondary TOC.
5. **Stefan George DID translate both** ("Der Albatros" II,
   "Einklänge" IV) — verified in the 1901 first-edition Inhalt and
   Zeno.org's section list. His versions are self-described
   *Umdichtungen* (free re-poetizations), a caveat recorded in the
   file headers.

**Not-found-by-me / unresolved (search gaps, honestly labeled):**
6. **No PD English "L'Albatros" was fetched.** Every pre-1929 English
   version checked (Scott 1909, Sturm 1906, Squire 1909, the 1919
   Huneker anthology) simply lacks the poem — items 1-3 above. The
   one pre-1929 complete translation (Symons 1925) is PD but has no
   accessible digitization (see Located section). So the corpus's
   English side currently has PD Correspondances (×2) and NO PD
   Albatross text: a real structural asymmetry in the corpus, caused
   by translator selectivity, not by search failure — but the
   *absence of a Symons fetch* specifically is an access gap, not a
   selectivity fact.
7. **William Aggeler's death date could not be established** (multiple
   searches; Goodreads/publisher pages carry no dates). His US
   copyright status doesn't hinge on it (95-year publication term),
   but life+70 status elsewhere is undetermined.
8. **Roy Campbell's US renewal status not verified** — flagged above.
9. **1857-vs-1861 line-level collation of Correspondances not done**
   (no per-poem 1857 transcription found on fr.wikisource;
   fleursdumal.org shows no variant apparatus).
10. **Dai Wangshu text reproduction variants**: the two independent
    web reproductions of his 《应和》 differ in two readings (凝视/凝望,
    和谐/和协 — detailed in dai_wangshu_yinghe.txt's header); the 1947
    or 1983 printed edition was not available to adjudicate. The
    fetched text is a web reproduction of the printed book, not a
    scan-verified transcription — one provenance rung below the
    Wikisource-validated French and the PG/archive.org English.
11. **钱春绮's 《信天翁》**: located only at search-snippet level
    (opening line + zhihu URL); no fully-fetched page with an explicit
    钱春绮译 credit for that specific poem (his 《感应》 IS solidly
    located, with credit, on shigeku). Minor evidentiary gap within a
    locate-only item.
