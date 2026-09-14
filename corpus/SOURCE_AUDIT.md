# Source audit report

## Rule application hierarchy (engine pipeline)

Corpus JSON is sorted by rule **id** for stability. Pronunciation **application** order is the pipeline below (not alphabetical categories).

1. `01_normalize` — Unicode NFD + orthographic fixes
1. `02_qere` — Qere/ketiv resolution
1. `03_orthography` — Letters, matres, shin/sin, dagesh/rafe marks
1. `04_inventory` — Consonant/vowel IPA inventory
1. `05_shewa_hatef` — Shewa / ḥaṭef classification
1. `06_syllables` — Syllabification / metrical structure
1. `07_length` — Vowel length, epenthesis, furtive pataḥ
1. `08_bgdkpt` — Begadkephat stop/fricative + sandhi
1. `09_gemination` — Dagesh forte / extended forte / loss of gemination
1. `10_resh_guttural` — Resh allophony, guttural constraints
1. `11_stress_maq` — Stress, gaʿya, maqqef, deḥiq
1. `12_emit` — IPA emission (bare, forte_lene default)

## Corpus stats

- Rules: **462**
- Sorted by id: **True**
- With ordering_notes: **6**

## Holam-vav encoding in T1 sources

| File | VAV+HOLAM (`וֹ`) | HOLAM+VAV (`ֹו`) | VAV+U+05BA |
|------|-----|-----|-----|
| T1_0_Intro.md | 57 | 0 | 0 |
| T1_1.md | 124 | 6 | 1 |
| T1_2B_corrected_p352.md | 228 | 6 | 0 |
| T1_3B.md | 86 | 7 | 0 |
| T1_4B_5_Ref.md | 52 | 2 | 0 |

Verdict: **VAV then HOLAM (`וֹ`) is the source-majority form**; pipeline rewrites HOLAM+VAV and stranded holam-before-vav to that form.

## I.5.4 fixture vs source (forte_lene = first reading)

### Genesis

- v1: OK
- v2: OK
- v3: OK
- v4: OK
- v5: OK
- v6: OK
- v7: OK
- v8: OK
- v9: OK
- v10: OK
- v11: OK
- v12: OK
- v13: OK

### Psalm

- v1: OK
- v2: OK
- v3: OK
- v4: OK
- v5: OK
- v6: OK

## Corpus TH-ORTH-SAMPLE vs fixtures

Sample rules: **19**
Bare (unbracketed) sample IPAs: **38**

## Candidate source encoding quirks (not silent-fixed in SoT files)

- `T1_1.md`: …(_vav_) are: ‎הֹוָ֤ה עַל־הֹוָה '…
- `T1_1.md`: …Ezek. 7.26), ‎הֹוֶ֤ה לָהֶם֙ לְמֶ…
- `T1_1.md`: …ֹֽא־יֵבֹ֖שׁוּ קֹוָֽי 'those who …
- `T1_1.md`: …וִבכִשרֹֿון (Yevin 1985, …
- `T1_1.md`: …הַגֹוִי (OB, Yeivin …
- `T1_2B_corrected_p352.md`: … L \[BHS\]: יְסֹובְבֻ֥הָ Psa. 55…
- `T1_2B_corrected_p352.md`: …יִסֹוד \[iːsoːð\] (Y…
- `T1_2B_corrected_p352.md`: …: בְּמִרְעֶה־טֹּוב֙ 'in good pas…
- `T1_2B_corrected_p352.md`: …בְמֲרְעֶה טֹוב \[bmarʕa ttˁo…
- `T1_2B_corrected_p352.md`: …: בְּמִרְעֶה־טֹּוב֙).…
- `T1_2B_corrected_p352.md`: …תֽהְיֶה בֹו \[tihya bboː\]…
- `T1_3B.md`: …ישַלֵם לֹּו (OB | L \[BHS\…
- `T1_3B.md`: …לאֹויֵב לֹּו (OB | L \[BHS\…
- `T1_3B.md`: …]: לְאֹויֵ֣ב לֹֽו Job 3…
- `T1_3B.md`: …the _qere_ is לֹו but the _ketiv…
- `T1_3B.md`: …ֵ֖ם, _qere_ וְלֹו־ 1 Chron. 11.2…
- `T1_3B.md`: … \[BHS\]: הָרְחֹוקִ֖ים מִצְּדָקָ…
- `T1_4B_5_Ref.md`: …עֵבְדֹו֙ (LG B1.56, Ar…
- `T1_4B_5_Ref.md`: …\[BHS\]: עַבְדֹּו֙ Gen. 24.2 'hi…

