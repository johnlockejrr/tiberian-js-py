# Tiberian Hebrew Pronunciation Rules

Source-faithful extraction from Khan T1 sources. Machine companion: `tiberian_rules.json`.

Total rules: **462**

## orthography

### TH-ORTH-T0-001: Pointing partially encodes speech

- **Status:** evidence
- **Authority:** editorial
- **Category:** orthography / notation limits
- **Statement:** Vocalization marks vowels and some consonant details, but only partially represents the oral reading.
- **Conditions:** When reconstructing pronunciation from pointing.
- **Operation:** Supplement signs with medieval pronunciation sources.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.4 (lines 78–86)
- **Certainty:** high
- **Examples:** no example in source

### TH-ORTH-T0-002: Sin dot

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** orthography / consonant diacritics
- **Statement:** The sin point identifies the [s] reading of ש.
- **Conditions:** When ש bears the sin dot.
- **Operation:** Realize it as [s].
- **Result IPA:** s
- **Source:** T1_0_Intro.md §I.0.8 (lines 326–326)
- **Certainty:** high
- **Examples:** no example in source

### TH-RAF-T3-002: Rafe marking is non-obligatory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** orthography / rafe
- **Statement:** Absence of a written rafe does not imply a stop; rafe marking varies by manuscript and is often omitted in print.
- **Conditions:** Interpreting a Tiberian manuscript or edition.
- **Operation:** Determine frication from phonological context, not solely the visible rafe.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.2 (lines 765–775)
- **Certainty:** high
- **Notes:** C and S mark rafe more often than L and A; B rarely; BHS/BHQ generally omit it.
- **Examples:** no example in source

### TH-RAF-T3-003: Rafe marks non-consonantal matres

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** orthography / rafe-matres
- **Statement:** Rafe may mark he or alef as non-consonantal.
- **Conditions:** He or alef functions non-consonantally and the manuscript marks rafe.
- **Operation:** Suppress consonantal realization.
- **Result IPA:** ∅
- **Source:** T1_3B.md §I.3.2 (lines 779–779)
- **Certainty:** high
- **Examples:**
  - `מַלְכָּהֿ` → `—`
  - `בָּאֿ` → `—`

### TH-VAR-T0-029: NST sign development

- **Status:** variant
- **Authority:** non-standard-tiberian
- **Category:** orthography / diacritic systems
- **Statement:** NST shows less advanced or extended uses of dagesh, rafe, shewa, and ḥaṭef.
- **Conditions:** In NST manuscripts.
- **Operation:** Interpret each manuscript’s sign system separately.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.13.6 (lines 697–701)
- **Certainty:** high
- **Examples:** no example in source

## qere-ketiv

### TH-QK-T0-001: Qere overrides ketiv

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** qere-ketiv / mechanism
- **Statement:** At a qere/ketiv conflict, the oral qere supplies the reading; its vowels are normally placed on ketiv letters.
- **Conditions:** At a marked conflict.
- **Operation:** Read the qere rather than pronounce the ketiv spelling.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.5 (lines 146–154)
- **Certainty:** high
- **Examples:**
  - `הָעֵי֖ר / חָצֵ֖ר` → `—` (I.0.5 lines 150–154)

### TH-QK-T0-002: Perpetual qere

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** qere-ketiv / qere perpetuum
- **Statement:** Frequent conventional qere forms have qere vocalization but no marginal note.
- **Conditions:** For the Tetragrammaton, Jerusalem, and conventional suffixes.
- **Operation:** Recover the conventional qere without a margin note.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.5 (lines 160–160)
- **Certainty:** high
- **Examples:** no example in source

### TH-QK-T0-003: Tetragrammaton as Adonai

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** qere-ketiv / Tetragrammaton
- **Statement:** יהוה is read אֲדֹנָי where that qere is signaled.
- **Conditions:** For the corresponding Tetragrammaton vocalization.
- **Operation:** Substitute אֲדֹנָי.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.5 (lines 160–160)
- **Certainty:** high
- **Examples:**
  - `יהוה / אֲדֹנָי` → `—` (I.0.5 line 160)

### TH-QK-T0-004: Tetragrammaton as Elohim

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** qere-ketiv / Tetragrammaton
- **Statement:** יהוה is read אֱלֹהִים where that qere is signaled.
- **Conditions:** For the corresponding Tetragrammaton vocalization.
- **Operation:** Substitute אֱלֹהִים.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.5 (lines 160–160)
- **Certainty:** high
- **Examples:**
  - `יהוה / אֱלֹהִים` → `—` (I.0.5 line 160)

### TH-QK-T0-005: Jerusalem qere

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** qere-ketiv / place name
- **Statement:** ירושלם is read יְרוּשָׁלַיִם with a glide breaking the final syllable.
- **Conditions:** For the regular ketiv ירושלם.
- **Operation:** Insert the qere glide.
- **Result IPA:** jaʀ̟uːʃɔːˈlaːjim
- **Source:** T1_0_Intro.md §I.0.5 (lines 160–320)
- **Certainty:** high
- **Examples:**
  - `יְרוּשָׁלַיִם` → `jaʀ̟uːʃɔːˈlaːjim` (I.0.8 line 320)

### TH-QK-T0-006: Second-person kaf suffix qere

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** qere-ketiv / suffixes
- **Statement:** The qere suffix ךָ- is [-χɔː], differing morphologically from ketiv.
- **Conditions:** For Tiberian qere ךָ-.
- **Operation:** Realize the suffix as [-χɔː].
- **Result IPA:** -χɔː
- **Source:** T1_0_Intro.md §I.0.5 (lines 178–180)
- **Certainty:** high
- **Examples:**
  - `ךָ-` → `-χɔː` (I.0.5 lines 178–180)

### TH-QK-T0-007: Second-person tav suffix qere

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** qere-ketiv / suffixes
- **Statement:** The qere suffix תָּ- is [‑tʰɔː], differing morphologically from ketiv.
- **Conditions:** For Tiberian qere תָּ-.
- **Operation:** Realize the suffix as [‑tʰɔː].
- **Result IPA:** ‑tʰɔː
- **Source:** T1_0_Intro.md §I.0.5 (lines 178–180)
- **Certainty:** high
- **Examples:**
  - `תָּ-` → `‑tʰɔː` (I.0.5 lines 178–180)

### TH-QK-T0-008: Third-person plural-noun suffix qere

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** qere-ketiv / suffixes
- **Statement:** The qere suffix ָיו- is [-ɔːɔv], differing morphologically from ketiv.
- **Conditions:** For Tiberian qere ָיו-.
- **Operation:** Realize the suffix as [-ɔːɔv].
- **Result IPA:** -ɔːɔv
- **Source:** T1_0_Intro.md §I.0.5 (lines 178–180)
- **Certainty:** high
- **Examples:**
  - `ָיו-` → `-ɔːɔv` (I.0.5 lines 178–180)

### TH-QK-T0-009: Same-sound semantic qere

- **Status:** evidence
- **Authority:** standard-tiberian
- **Category:** qere-ketiv / semantic reading
- **Statement:** Some qere/ketiv pairs differ only in meaning or parsing, not phonetic form.
- **Conditions:** For pairs such as לו and לֹא.
- **Operation:** Preserve pronunciation but apply qere semantics.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.5 (lines 210–226)
- **Certainty:** high
- **Examples:**
  - `לוֹ / לֹא` → `—` (I.0.5 lines 210–224)

### TH-QK-T0-010: Consonantal final vav pointer

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** qere-ketiv / final diphthong
- **Statement:** Final יו in a qere note can signal consonantal vav and [ɔːɔv], where vav would normally be read as a vowel.
- **Conditions:** At exceptional final -או/-מו sequences.
- **Operation:** Read vav consonantally and preserve the diphthong.
- **Result IPA:** ɔːɔv
- **Source:** T1_0_Intro.md §I.0.5 (lines 228–232)
- **Certainty:** high
- **Examples:**
  - `וַיִּתְאָ֥יו` → `ɔːɔv` (I.0.5 lines 228–232)
  - `יָמָיו֙` → `ɔːɔv` (I.0.5 line 232)

### TH-QK-T0-011: Qere protects short qameṣ

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** qere-ketiv / vowel length
- **Statement:** A qere may remove ketiv vav to prevent a short qameṣ-type vowel from being read long.
- **Conditions:** When qameṣ ḥaṭuf or ḥaṭef qameṣ conflicts with a ketiv vowel letter.
- **Operation:** Read the short vowel and ignore misleading vav.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.5 (lines 234–238)
- **Certainty:** high
- **Examples:**
  - `וַנָּ֤שָׁוב / וַנָּ֤שָׁב` → `—` (I.0.5 lines 234–238)

### TH-QK-T0-012: Erroneous historical qere

- **Status:** exception
- **Authority:** standard-tiberian
- **Category:** qere-ketiv / misreading
- **Statement:** A canonical qere can preserve an old oral misreading of visually similar letters.
- **Conditions:** For isolated difficult qere forms identified by the source.
- **Operation:** Apply canonical qere but flag its likely origin.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.5 (lines 274–284)
- **Certainty:** medium
- **Examples:**
  - `הַוְצֵ֣א / הַיְצֵ֣א` → `—` (I.0.5 lines 280–284)

## consonants

### TH-CON-ALEF-T1-001: Consonantal alef

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonant / letter realization
- **Statement:** Consonantal א is a glottal plosive [ʔ].
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Apply the stated realization.
- **Result IPA:** ʔ
- **Source:** T1_1.md §I.1.1 (lines 3–5)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-ALEF-T1-002: Initial-onset alef

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonant / letter realization
- **Statement:** Consonantal alef is retained as [ʔ] in this context.
- **Conditions:** Word-initial syllable onset.
- **Operation:** Preserve a consonantal glottal closure.
- **Result IPA:** ʔ
- **Source:** T1_1.md §I.1.1 (lines 7–9)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-CON-ALEF-001']
- **Examples:**
  - `אָמַ֗ר` → `ʔɔːˈmaːaʀ̟` (Gen. 3.16)
  - `אֱלֹהִ֑ים` → `ʔɛloːˈhiːim` (Gen. 1.1)

### TH-CON-ALEF-T1-003: Alef after silent shewa

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonant / letter realization
- **Statement:** Consonantal alef is retained as [ʔ] in this context.
- **Conditions:** Medial syllable onset after silent shewa.
- **Operation:** Preserve a consonantal glottal closure.
- **Result IPA:** ʔ
- **Source:** T1_1.md §I.1.1 (lines 11–11)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-CON-ALEF-001']
- **Examples:**
  - `וַיִּבְאַ֣שׁ` → `vaɟɟivˈʔaːaʃ` (Exod. 7.21)

### TH-CON-ALEF-T1-004: Alef after a vocalic segment

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonant / letter realization
- **Statement:** Consonantal alef is retained as [ʔ] in this context.
- **Conditions:** Medial onset after a vowel, ḥaṭef vowel, or vocalic shewa.
- **Operation:** Preserve a consonantal glottal closure.
- **Result IPA:** ʔ
- **Source:** T1_1.md §I.1.1 (lines 13–13)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-CON-ALEF-001']
- **Examples:**
  - `יָבִ֑יאוּ` → `jɔːˈviːʔuː` (Exod. 16.5)
  - `אֲאַזֶּרְךָ֖` → `ʔaʔazzɛrˁˈχɔː` (Isa. 45.5)
  - `מְאֹ֑ד` → `moˈʔoːoð` (Gen. 1.31)

### TH-CON-ALEF-T1-005: Medial-coda alef

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonant / letter realization
- **Statement:** Consonantal alef is retained as [ʔ] in this context.
- **Conditions:** Word-medial syllable coda.
- **Operation:** Preserve a consonantal glottal closure.
- **Result IPA:** ʔ
- **Source:** T1_1.md §I.1.1 (lines 15–15)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-CON-ALEF-001']
- **Examples:**
  - `וַיֶּאְסֹ֤ר` → `vaɟɟɛʔˈsoːorˁ` (Gen. 46.29)

### TH-CON-AYIN-T1-001: ʿAyin

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonant / letter realization
- **Statement:** ע is a voiced pharyngeal fricative [ʕ].
- **Conditions:** Written ע has consonantal realization.
- **Operation:** Realize ע as [ʕ].
- **Result IPA:** ʕ
- **Source:** T1_1.md §I.1.16 (lines 1143–1145)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-HE-T1-001: Consonantal he

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonant / letter realization
- **Statement:** Consonantal ה is a glottal fricative [h].
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Apply the stated realization.
- **Result IPA:** h
- **Source:** T1_1.md §I.1.5 (lines 365–367)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-HET-T1-001: Ḥet

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonant / letter realization
- **Statement:** ח is a unvoiced pharyngeal fricative [ħ].
- **Conditions:** Written ח has consonantal realization.
- **Operation:** Realize ח as [ħ].
- **Result IPA:** ħ
- **Source:** T1_1.md §I.1.8 (lines 867–869)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-LAMED-T1-001: Lamed

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonant / letter realization
- **Statement:** ל is a voiced alveolar lateral continuant [l].
- **Conditions:** Written ל has consonantal realization.
- **Operation:** Realize ל as [l].
- **Result IPA:** l
- **Source:** T1_1.md §I.1.12 (lines 1109–1111)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-MEM-T1-001: Mem

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonant / letter realization
- **Statement:** מ, ם is a voiced bilabial nasal [m].
- **Conditions:** Written מ, ם has consonantal realization.
- **Operation:** Realize מ, ם as [m].
- **Result IPA:** m
- **Source:** T1_1.md §I.1.13 (lines 1117–1119)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-NUN-T1-001: Nun

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonant / letter realization
- **Statement:** נ, ן is a voiced alveolar nasal [n].
- **Conditions:** Written נ, ן has consonantal realization.
- **Operation:** Realize נ, ן as [n].
- **Result IPA:** n
- **Source:** T1_1.md §I.1.14 (lines 1123–1125)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-QOF-T1-001: Qof

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonant / letter realization
- **Statement:** ק is a unvoiced advanced uvular unaspirated plosive [q̟].
- **Conditions:** Written ק has consonantal realization.
- **Operation:** Realize ק as [q̟].
- **Result IPA:** q̟
- **Source:** T1_1.md §I.1.19 (lines 1329–1331)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-RESH-T1-001: Default resh

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonant / letter realization
- **Statement:** Default resh is transcribed as advanced uvular trill [ʀ̟]; [ʁ̖̟] is a possible articulatory interpretation.
- **Conditions:** No [rˁ]-conditioning environment applies.
- **Operation:** Use advanced uvular [ʀ̟].
- **Result IPA:** ʀ̟
- **Source:** T1_1.md §I.1.20 (lines 1363–1411)
- **Certainty:** high
- **Examples:**
  - `רֶ֣כֶב` → `ˈʀ̟ɛːxɛv` (Exod. 14.9)
  - `מַרְאֶ֖ה` → `maʀ̟ˈʔɛː` (Gen. 12.11)
  - `שָׁמַ֥ר` → `ʃɔːˈmaːaʀ̟` (Gen. 37.11)
  - `אֶרְדּ֣וֹף` → `ʔɛʀ̟ˈdoːof` (Psa. 18.38)

### TH-CON-SADE-T1-001: Ṣade

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonant / letter realization
- **Statement:** צ, ץ is a unvoiced emphatic alveolar sibilant [sˁ].
- **Conditions:** Written צ, ץ has consonantal realization.
- **Operation:** Realize צ, ץ as [sˁ].
- **Result IPA:** sˁ
- **Source:** T1_1.md §I.1.18 (lines 1311–1313)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-SAMEKH-T1-001: Samekh

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonant / letter realization
- **Statement:** ס is a unvoiced alveolar sibilant [s].
- **Conditions:** Written ס has consonantal realization.
- **Operation:** Realize ס as [s].
- **Result IPA:** s
- **Source:** T1_1.md §I.1.15 (lines 1129–1131)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-SHIN-T1-001: Shin

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonant / letter realization
- **Statement:** שׁ is a unvoiced palato-alveolar fricative [ʃ].
- **Conditions:** Written שׁ has consonantal realization.
- **Operation:** Realize שׁ as [ʃ].
- **Result IPA:** ʃ
- **Source:** T1_1.md §I.1.22 (lines 1481–1483)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-SIN-T1-001: Sin

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonant / letter realization
- **Statement:** שׂ is a unvoiced alveolar sibilant [s].
- **Conditions:** Written שׂ has consonantal realization.
- **Operation:** Realize שׂ as [s].
- **Result IPA:** s
- **Source:** T1_1.md §I.1.21 (lines 1437–1439)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-T0-001: Qumran guttural weakening

- **Status:** variant
- **Authority:** comparative
- **Category:** consonants / gutturals
- **Statement:** Some Second Temple traditions weakened gutturals, reflected by omission or interchange in spelling.
- **Conditions:** In affected Qumran and Judaean sources.
- **Operation:** Weaken, merge, or omit a guttural.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.1 (lines 14–16)
- **Certainty:** medium
- **Examples:** no example in source

### TH-CON-T0-002: Bar Kochba guttural preservation

- **Status:** evidence
- **Authority:** comparative
- **Category:** consonants / gutturals
- **Statement:** The Bar Kochba documents reflect a dialect that largely preserved gutturals.
- **Conditions:** In the dialect represented by those documents.
- **Operation:** Retain guttural contrasts.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.1 (lines 14–14)
- **Certainty:** medium
- **Examples:** no example in source

### TH-CON-T0-003: Historical velar fricatives

- **Status:** evidence
- **Authority:** comparative
- **Category:** consonants / historical velars
- **Statement:** Greek transcriptions attest preservation of Proto-Semitic *ḵ and *ġ in some Hebrew dialects.
- **Conditions:** In relevant Septuagint transcriptions.
- **Operation:** Preserve the velar fricative distinction.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.1 (lines 16–16)
- **Certainty:** medium
- **Examples:**
  - `אָחָז` → `—` (I.0.1 line 16)
  - `עַזָּה` → `—` (I.0.1 line 16)

### TH-CON-T0-004: Unaspirated pe in appadno

- **Status:** exception
- **Authority:** standard-tiberian
- **Category:** consonants / pe
- **Statement:** Pe in אַפַּדְנ֔וֹ is emphatic unaspirated [p], unlike other dageshed pe, described as aspirated.
- **Conditions:** Only in Dan. 11.45.
- **Operation:** Suppress aspiration.
- **Result IPA:** p
- **Source:** T1_0_Intro.md §I.0.8 (lines 324–324)
- **Certainty:** high
- **Examples:**
  - `אַפַּּדְנ֔וֹ` → `p` (I.0.8 line 324)

### TH-CON-T0-005: Shin-sin distinction

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / sibilants
- **Statement:** Pointed shin is [ʃ]; pointed sin is [s], equivalent to samekh.
- **Conditions:** When interpreting the dot on ש.
- **Operation:** Select [ʃ] or [s] from the pointing.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.8 (lines 326–336)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-T0-006: Default consonantal vav

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / vav
- **Statement:** Default consonantal vav is labiodental [v].
- **Conditions:** When vav is consonantal and no exception is specified.
- **Operation:** Realize vav as [v].
- **Result IPA:** v
- **Source:** T1_0_Intro.md §I.0.8 (lines 362–368)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-T4-101: Interdental-to-stop substrate replacement

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** consonants / substrate-interference
- **Statement:** Some later Sefardi traditions replace Tiberian fricative tav [θ] and dalet [ð] with stops under Arabic substrate influence.
- **Conditions:** The reader's substrate lacks interdental phonemes.
- **Operation:** Variant replacement [θ] → stop and [ð] → stop.
- **Result IPA:** θ > t/tʰ; ð > d
- **Source:** T1_4B_5_Ref.md §I.4.2 (lines 18–40)
- **Certainty:** high
- **Examples:**
  - `תְהֹמֹ֖ת` → `tihuˈmut` (Exod. 15.8)

### TH-CON-T4-102: Partial tav stop substitution

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** consonants / imperfect-learning
- **Statement:** BL Or 2551 variably substitutes stop tav for target fricative tav while retaining evidence of the Tiberian target.
- **Conditions:** Reading BL Or 2551.; Target consonant is fricative tav.
- **Operation:** Record sporadic [θ] → [t] mismatch.
- **Result IPA:** None
- **Source:** T1_4B_5_Ref.md §I.4.2 (lines 42–70)
- **Certainty:** high
- **Examples:**
  - `הִתְעַבָּֽר` → `—` (Psa. 78.62)

### TH-CON-T4-103: Embedded Hebrew has weaker target control

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** consonants / register
- **Statement:** Hebrew embedded in Arabic commentary exhibits more stop substitutions than the manuscript's biblical reading.
- **Conditions:** Hebrew occurs within the Arabic commentary of BL Or 2551.
- **Operation:** Interpret increased substitutions as reduced effort toward the Tiberian target.
- **Result IPA:** None
- **Source:** T1_4B_5_Ref.md §I.4.2 (lines 72–80)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-T4-104: Advanced interdental leveling

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** consonants / imperfect-learning
- **Statement:** BL Or 2552 mostly replaces target fricative tav with stop tav, preserving only occasional interdentals.
- **Conditions:** Reading BL Or 2552.
- **Operation:** Record near-general [θ] → [t] leveling.
- **Result IPA:** None
- **Source:** T1_4B_5_Ref.md §I.4.2 (lines 86–102)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-T4-105: Hypercorrect interdental tav

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** consonants / hypercorrection
- **Statement:** A learner may insert fricative [θ] where Standard Tiberian requires stop [tʰ].
- **Conditions:** A reader imperfectly generalizes prestigious interdental tav.
- **Operation:** Hypercorrect target stop to interdental.
- **Result IPA:** tʰ > θ
- **Source:** T1_4B_5_Ref.md §I.4.2 (lines 102–106)
- **Certainty:** high
- **Examples:**
  - `אַל־תִּרְשַׁ֥ע` → `—` (Ecc. 7.17)

### TH-CON-T4-106: Analogical fricativization of anomalous tav

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** consonants / analogical-leveling
- **Statement:** Some manuscripts fricativize singleton post-vocalic tav in אַתְּ and בָּתִּים, regularizing an anomalous Standard Tiberian stop.
- **Conditions:** Lexeme is אַתְּ or בָּתִּים.; The evidence is from the cited variant manuscripts.
- **Operation:** Variant [tʰ] → [θ] after a vowel.
- **Result IPA:** tʰ > θ
- **Source:** T1_4B_5_Ref.md §I.4.2 (lines 108–114)
- **Certainty:** high
- **Examples:**
  - `בָּתֵּיהֶ֖ם` → `—` (Jer. 5.25)

### TH-CON-T4-201: ʾalef inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** א (ʾalef) has canonical realization [ʔ] and phonemic analysis /ʔ/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** ʔ
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 284–284)
- **Certainty:** high
- **Notes:** §I.1.1.
- **Examples:** no example in source

### TH-CON-T4-202: bet (dagesh) inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** בּ (bet (dagesh)) has canonical realization [b], [bb] and phonemic analysis /b/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** b, bb
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 285–285)
- **Certainty:** high
- **Notes:** §I.1.2., §I.1.25., §I.3.1.11.3.
- **Examples:** no example in source

### TH-CON-T4-203: bet (rafe) inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** ב (bet (rafe)) has canonical realization [v] and phonemic analysis /v/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** v
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 286–286)
- **Certainty:** high
- **Notes:** §I.1.2., §I.1.25.
- **Examples:** no example in source

### TH-CON-T4-204: gimel (dagesh) inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** גּ (gimel (dagesh)) has canonical realization [g], [gg] and phonemic analysis /g/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** g, gg
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 287–287)
- **Certainty:** high
- **Notes:** §I.1.3., §I.1.25., §I.3.1.11.3.
- **Examples:** no example in source

### TH-CON-T4-205: gimel (rafe) inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** ג (gimel (rafe)) has canonical realization [ʁ] and phonemic analysis /ʁ/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** ʁ
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 288–288)
- **Certainty:** high
- **Notes:** §I.1.3., §I.1.25.
- **Examples:** no example in source

### TH-CON-T4-206: dalet (dagesh) inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** דּ (dalet (dagesh)) has canonical realization [d], [dd] and phonemic analysis /d/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** d, dd
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 289–289)
- **Certainty:** high
- **Notes:** §I.1.4., §I.1.25., §I.3.1.11.3.
- **Examples:** no example in source

### TH-CON-T4-207: dalet (rafe) inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** ד (dalet (rafe)) has canonical realization [ð] and phonemic analysis /ð/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** ð
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 290–290)
- **Certainty:** high
- **Notes:** §I.1.4., §I.1.25.
- **Examples:** no example in source

### TH-CON-T4-208: he inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** ה (he) has canonical realization [h] and phonemic analysis /h/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** h
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 291–291)
- **Certainty:** high
- **Notes:** §I.1.5.
- **Examples:** no example in source

### TH-CON-T4-209: vav inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** ו (vav) has canonical realization [v], [w] and phonemic analysis /v/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** v, w
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 292–292)
- **Certainty:** high
- **Notes:** §I.1.6.
- **Examples:** no example in source

### TH-CON-T4-210: zayin inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** ז (zayin) has canonical realization [z] and phonemic analysis /z/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** z
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 293–293)
- **Certainty:** high
- **Notes:** §I.1.7.
- **Examples:** no example in source

### TH-CON-T4-211: ḥet inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** ח (ḥet) has canonical realization [ħ] and phonemic analysis /ħ/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** ħ
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 294–294)
- **Certainty:** high
- **Notes:** §I.1.8.
- **Examples:** no example in source

### TH-CON-T4-212: ṭet inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** ט (ṭet) has canonical realization [tˁ] and phonemic analysis /tˁ/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** tˁ
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 295–295)
- **Certainty:** high
- **Notes:** §I.1.9.
- **Examples:** no example in source

### TH-CON-T4-213: yod inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** י (yod) has canonical realization [j], [ɟ] and phonemic analysis /j/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** j, ɟ
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 296–296)
- **Certainty:** high
- **Notes:** §I.1.10. The stop allophone [ɟ] occurs only when geminated.
- **Examples:** no example in source

### TH-CON-T4-214: kaf (dagesh) inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** כּ, ךּ (kaf (dagesh)) has canonical realization [kʰ], [kkʰ] and phonemic analysis /kʰ/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** kʰ, kkʰ
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 297–297)
- **Certainty:** high
- **Notes:** §I.1.11., §I.1.25., §I.3.1.11.3.
- **Examples:** no example in source

### TH-CON-T4-215: kaf (rafe) inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** כ, ך (kaf (rafe)) has canonical realization [χ] and phonemic analysis /χ/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** χ
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 298–298)
- **Certainty:** high
- **Notes:** §I.1.11., §I.1.25.
- **Examples:** no example in source

### TH-CON-T4-216: lamed inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** ל (lamed) has canonical realization [l] and phonemic analysis /l/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** l
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 299–299)
- **Certainty:** high
- **Notes:** §I.1.12.
- **Examples:** no example in source

### TH-CON-T4-217: mem inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** מ, ם (mem) has canonical realization [m] and phonemic analysis /m/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** m
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 300–300)
- **Certainty:** high
- **Notes:** §I.1.13.
- **Examples:** no example in source

### TH-CON-T4-218: nun inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** נ, ן (nun) has canonical realization [n] and phonemic analysis /n/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** n
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 301–301)
- **Certainty:** high
- **Notes:** §I.1.14.
- **Examples:** no example in source

### TH-CON-T4-219: samekh inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** ס (samekh) has canonical realization [s] and phonemic analysis /s/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** s
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 302–302)
- **Certainty:** high
- **Notes:** §I.1.15. Equivalent orally to sin.
- **Examples:** no example in source

### TH-CON-T4-220: ʿayin inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** ע (ʿayin) has canonical realization [ʕ] and phonemic analysis /ʕ/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** ʕ
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 303–303)
- **Certainty:** high
- **Notes:** §I.1.16.
- **Examples:** no example in source

### TH-CON-T4-221: pe (dagesh) inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** פּ (pe (dagesh)) has canonical realization [pʰ], [ppʰ] and phonemic analysis /pʰ/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** pʰ, ppʰ
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 304–304)
- **Certainty:** high
- **Notes:** §I.1.17., §I.1.25., §I.3.1.11.3.
- **Examples:** no example in source

### TH-CON-T4-222: emphatic pe (dagesh) inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** פּ (emphatic pe (dagesh)) has canonical realization [pˁ], [ppˁ] and phonemic analysis /pˁ/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** pˁ, ppˁ
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 305–305)
- **Certainty:** high
- **Notes:** §I.1.17. Only in אַפַּדְנ֔וֹ (Dan. 11.45).
- **Examples:** no example in source

### TH-CON-T4-223: pe (rafe) inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** פ (pe (rafe)) has canonical realization [f] and phonemic analysis /f/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** f
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 306–306)
- **Certainty:** high
- **Notes:** §I.1.17., §I.1.25.
- **Examples:** no example in source

### TH-CON-T4-224: ṣade inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** צ (ṣade) has canonical realization [sˁ], [zˁ] and phonemic analysis /sˁ/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** sˁ, zˁ
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 307–307)
- **Certainty:** high
- **Notes:** §I.1.18. Voiced variant is conditioned.
- **Examples:** no example in source

### TH-CON-T4-225: qof inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** ק (qof) has canonical realization [q̟] and phonemic analysis /q̟/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** q̟
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 308–308)
- **Certainty:** high
- **Notes:** §I.1.19.
- **Examples:** no example in source

### TH-CON-T4-226: resh inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** ר (resh) has canonical realization [ʀ̟], [rˁ] and phonemic analysis /r/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** ʀ̟, rˁ
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 309–309)
- **Certainty:** high
- **Notes:** §I.1.20. Conditioned allophones.
- **Examples:** no example in source

### TH-CON-T4-227: sin inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** שׂ (sin) has canonical realization [s] and phonemic analysis /s/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** s
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 310–310)
- **Certainty:** high
- **Notes:** §I.1.21. Equivalent orally to samekh.
- **Examples:** no example in source

### TH-CON-T4-228: shin inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** שׁ (shin) has canonical realization [ʃ] and phonemic analysis /ʃ/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** ʃ
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 311–311)
- **Certainty:** high
- **Notes:** §I.1.22.
- **Examples:** no example in source

### TH-CON-T4-229: tav (dagesh) inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** תּ (tav (dagesh)) has canonical realization [tʰ], [ttʰ] and phonemic analysis /tʰ/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** tʰ, ttʰ
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 312–312)
- **Certainty:** high
- **Notes:** §I.1.23., §I.1.25., §I.3.1.11.3.
- **Examples:** no example in source

### TH-CON-T4-230: tav (rafe) inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / inventory
- **Statement:** ת (tav (rafe)) has canonical realization [θ] and phonemic analysis /θ/.
- **Conditions:** Apply the contextual allophony and stream distinctions cited in the table.
- **Operation:** Map the grapheme to its canonical phonetic realization(s).
- **Result IPA:** θ
- **Source:** T1_4B_5_Ref.md §I.5.1 (lines 313–313)
- **Certainty:** high
- **Notes:** §I.1.23., §I.1.25.
- **Examples:** no example in source

### TH-CON-TET-T1-001: Ṭet

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonant / letter realization
- **Statement:** ט is a emphatic unvoiced alveolar plosive [tˁ].
- **Conditions:** Written ט has consonantal realization.
- **Operation:** Realize ט as [tˁ].
- **Result IPA:** tˁ
- **Source:** T1_1.md §I.1.9 (lines 953–955)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-VAV-T1-001: Default consonantal vav

- **Status:** rule
- **Authority:** comparative
- **Category:** consonant / letter realization
- **Statement:** Palestinian consonantal ו is normally labio-dental [v], identical to bet rafe.
- **Conditions:** Consonantal ו is outside a specifically attested [w] context.
- **Operation:** Realize ו as [v].
- **Result IPA:** v
- **Source:** T1_1.md §I.1.6 (lines 569–579)
- **Certainty:** high
- **Examples:**
  - `וְאָמַר` → `vɔʔɔːˈmaːaʀ̟` (uncited)

### TH-CON-VAV-T1-002: Vav glide before furtive pataḥ

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonant / letter realization
- **Statement:** Vav after [uː]/[oː] and before a guttural with furtive pataḥ is [w].
- **Conditions:** ו follows [uː] or [oː] and precedes a guttural bearing furtive pataḥ.
- **Operation:** Insert a bilabial glide.
- **Result IPA:** w
- **Source:** T1_1.md §I.1.6 (lines 571–573)
- **Certainty:** high
- **Examples:**
  - `רוּחַ` → `ˈʀ̟uːwaħ` (uncited)
  - `נִיחוֹחַ` → `niːˈħoːwaħ` (uncited)

### TH-CON-YOD-T1-001: Yod

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonant / letter realization
- **Statement:** י is a palatal unrounded semi-vowel [j].
- **Conditions:** Written י has consonantal realization.
- **Operation:** Realize י as [j].
- **Result IPA:** j
- **Source:** T1_1.md §I.1.10 (lines 995–997)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-ZAYIN-T1-001: Zayin

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonant / letter realization
- **Statement:** ז is a voiced alveolar sibilant [z].
- **Conditions:** Written ז has consonantal realization.
- **Operation:** Realize ז as [z].
- **Result IPA:** z
- **Source:** T1_1.md §I.1.7 (lines 837–839)
- **Certainty:** high
- **Examples:** no example in source

### TH-DAG-T3-001: Dagesh forte marks gemination

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / dagesh-forte
- **Statement:** A dagesh on a geminated consonant marks dagesh forte.
- **Conditions:** A consonantal letter bears dagesh and the consonant is geminated.
- **Operation:** Realize the consonant with increased pressure and duration.
- **Result IPA:** CC
- **Source:** T1_3B.md §I.3.1.1 (lines 45–49)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-DAG-002', 'TH-VAR-001', 'TH-VAR-002']
- **Examples:** no example in source

### TH-DAG-T3-002: Dagesh lene marks BGDKPT stops

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / dagesh-lene
- **Statement:** In the forte-lene stream, dagesh lene marks a plosive realization of בגדכפת without itself requiring gemination.
- **Conditions:** The letter is one of בגדכפת.; The dagesh is conventionally dagesh lene.
- **Operation:** Select the stop allophone.
- **Result IPA:** b g d kʰ pʰ tʰ
- **Source:** T1_3B.md §I.3.1.1 (lines 45–49)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-DAG-001', 'TH-BGDKPT-001', 'TH-VAR-001']
- **Examples:** no example in source

### TH-DAG-T3-003: Dagesh increases articulatory pressure

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / dagesh
- **Statement:** Letters with dagesh are pronounced with greater muscular pressure than counterparts without dagesh.
- **Conditions:** A letter bears dagesh.
- **Operation:** Increase articulatory pressure.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.1 (lines 45–49)
- **Certainty:** high
- **Examples:** no example in source

### TH-DAG-T3-004: Gutturals normally reject dagesh

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / gemination-restrictions
- **Statement:** Standard Tiberian normally does not mark dagesh on אהעח; in principle these consonants are not geminated.
- **Conditions:** Target consonant is א, ה, ע, or ח.
- **Operation:** Block dagesh and gemination.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.1 (lines 49–52)
- **Certainty:** high
- **Examples:** no example in source

### TH-DAG-T3-005: Resh normally rejects dagesh

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / gemination-restrictions
- **Statement:** Resh is generally not geminated, but an attested dagesh on resh is dagesh forte and marks gemination.
- **Conditions:** Target consonant is resh.
- **Operation:** Normally block gemination; geminate when dagesh is explicitly attested.
- **Result IPA:** ʀ̟ʀ̟
- **Source:** T1_3B.md §I.3.1.1 (lines 53–65)
- **Certainty:** high
- **Examples:**
  - `שֶׁרֹּאשִׁי֙` → `—` (Cant. 5.2)

### TH-GAP-T0-002: Extended dagesh forte stream

- **Status:** gap
- **Authority:** standard-tiberian
- **Category:** consonants / extended dagesh forte
- **Statement:** An extended stream pronounces syllable-initial BGDKPT dagesh lene as dagesh forte for maximal plosive/fricative and syllable separation.
- **Conditions:** At syllable-initial BGDKPT with dagesh in that stream.
- **Operation:** Promote lene to forte pronunciation.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.11 (lines 595–595)
- **Certainty:** unresolved
- **Notes:** Deferred to §I.3.1.11.3; keep distinct from the ordinary forte–lene stream.
- **Examples:** no example in source

### TH-RAF-T3-001: Rafe marks BGDKPT fricatives

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / rafe
- **Statement:** Rafe primarily marks a בגדכפת consonant as fricative.
- **Conditions:** A בגדכפת letter bears rafe.
- **Operation:** Select the fricative allophone.
- **Result IPA:** v ʁ ð χ f θ
- **Source:** T1_3B.md §I.3.2 (lines 763–769)
- **Certainty:** high
- **Examples:** no example in source

### TH-RAF-T3-004: Rafe explicitly marks lost gemination

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / rafe-ungeminated
- **Statement:** Rafe may explicitly mark a weak consonant as ungeminated where dagesh would otherwise be expected.
- **Conditions:** Morphology or deḥiq would normally predict dagesh.; The manuscript marks rafe instead.
- **Operation:** Do not geminate the consonant.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.2 (lines 781–795)
- **Certainty:** high
- **Examples:**
  - `וַיְֿבַקְשׁ֔וּ` → `—` (Jud. 6.29)

### TH-RAF-T3-006: Rafe marks consonantal vav

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / rafe-vav
- **Statement:** In some manuscripts, rafe on vav indicates consonantal rather than vocalic value.
- **Conditions:** Vav bears rafe in a manuscript using this convention.
- **Operation:** Realize vav consonantally.
- **Result IPA:** v or w
- **Source:** T1_3B.md §I.3.2 (lines 829–833)
- **Certainty:** high
- **Examples:**
  - `וִֿיהִ֤י` → `—` (Psa. 90.17)

### TH-VAR-T0-009: Sin-samekh equivalence

- **Status:** evidence
- **Authority:** comparative
- **Category:** consonants / sibilants
- **Statement:** Late spelling interchange supports phonetic equivalence of sin and samekh as [s].
- **Conditions:** In cited late-book variants.
- **Operation:** Map both to [s].
- **Result IPA:** s
- **Source:** T1_0_Intro.md §I.0.8 (lines 328–356)
- **Certainty:** high
- **Examples:**
  - `וְסֹכְרִ֧ים / שֹׂכְרִים֙` → `s` (I.0.8 lines 328–336)

### TH-VAR-T0-017: Contrastive dagesh

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** consonants / semantic gemination
- **Statement:** Selected homophones use dagesh/gemination to distinguish meaning, including divine versus human reference.
- **Conditions:** Only in specified lexical pairs.
- **Operation:** Apply transmitted gemination.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.8 (lines 468–468)
- **Certainty:** high
- **Examples:**
  - `אֲבִיר / אַבִּיר` → `—` (I.0.8 line 468)

### TH-VAR-T0-022: Ben Asher Issachar

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** consonants / Ben Asher
- **Statement:** Ben Asher reads Issachar with geminate sin.
- **Conditions:** In Ben Asher’s stream.
- **Operation:** Realize the sibilants as [ss].
- **Result IPA:** jissɔːχɔːɔʀ̟
- **Source:** T1_0_Intro.md §I.0.10 (lines 539–593)
- **Certainty:** high
- **Examples:**
  - `יִשָּׂשכָר` → `jissɔːχɔːɔʀ̟` (I.0.11 line 593)

### TH-VAR-T0-023: Ben Naftali Issachar

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** consonants / Ben Naftali
- **Statement:** Ben Naftali reads Issachar with distinct shin and sin.
- **Conditions:** In Ben Naftali’s stream.
- **Operation:** Realize the sibilants as [ʃs].
- **Result IPA:** jiʃsɔːχɔːɔʀ̟
- **Source:** T1_0_Intro.md §I.0.10 (lines 539–593)
- **Certainty:** high
- **Examples:**
  - `יִשְׁשָׂכָר` → `jiʃsɔːχɔːɔʀ̟` (I.0.11 line 593)

### TH-VAR-T0-024: Moshe Moḥe Issachar

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** consonants / Moshe Moḥe
- **Statement:** Moshe Moḥe points Issachar יִשְׂשָׂכָר.
- **Conditions:** In his stream.
- **Operation:** Preserve this pointing.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.10 (lines 539–539)
- **Certainty:** high
- **Examples:**
  - `יִשְׂשָׂכָר` → `—` (I.0.10 line 539)

## gutturals

### TH-GUTT-AYIN-T1-001: ʿAyin resists dagesh

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** guttural / gemination restriction
- **Statement:** ʿAyin does not take dagesh and cannot be made heavy by it.
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Block dagesh-driven gemination.
- **Result IPA:** ʕ
- **Source:** T1_1.md §I.1.16 (lines 1157–1163)
- **Certainty:** high
- **Examples:** no example in source

### TH-GUTT-HET-T1-001: Ḥet resists dagesh

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** guttural / gemination restriction
- **Statement:** Standard Tiberian ח does not take dagesh or regular gemination.
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Block dagesh-driven gemination.
- **Result IPA:** ħ
- **Source:** T1_1.md §I.1.8 (lines 879–897)
- **Certainty:** high
- **Examples:** no example in source

## dagesh

### TH-CON-HE-T1-005: Mappiq does not geminate he

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** dagesh / mappiq interpretation
- **Statement:** Mappiq marks consonantal realization, not gemination; he is not geminated.
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Supply [h], never [hh].
- **Result IPA:** h
- **Source:** T1_1.md §I.1.5 (lines 425–431)
- **Certainty:** high
- **Examples:** no example in source

### TH-DAG-ALEF-T1-001: Canonical alef dagesh gemination

- **Status:** rule
- **Authority:** comparative
- **Category:** dagesh / alef gemination
- **Statement:** In the four canonical places, dagesh in א marks gemination [ʔʔ], an orthoepic protection against slurring.
- **Conditions:** The token is one of the four Masoretically fixed occurrences.
- **Operation:** Lengthen the consonantal glottal closure.
- **Result IPA:** ʔʔ
- **Source:** T1_1.md §I.1.1 (lines 77–119)
- **Certainty:** high
- **Examples:** no example in source

### TH-DAG-ALEF-T1-002: Canonical geminated alef: Gen. 43.26

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** dagesh / canonical alef dagesh
- **Statement:** The alef in וַיָּבִ֥יאּוּ ל֛וֹ is canonically geminated.
- **Conditions:** This fixed scriptural token is read.
- **Operation:** Realize אּ as [ʔʔ].
- **Result IPA:** ʔʔ
- **Source:** T1_1.md §I.1.1 (lines 17–25)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-DAG-ALEF-001']
- **Examples:**
  - `וַיָּבִ֥יאּוּ ל֛וֹ` → `vaɟɟɔːˈviːiʔʔuː` (Gen. 43.26)

### TH-DAG-ALEF-T1-003: Canonical geminated alef: Ezra 8.18

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** dagesh / canonical alef dagesh
- **Statement:** The alef in וַיָּבִ֨יאּוּ לָ֜נוּ is canonically geminated.
- **Conditions:** This fixed scriptural token is read.
- **Operation:** Realize אּ as [ʔʔ].
- **Result IPA:** ʔʔ
- **Source:** T1_1.md §I.1.1 (lines 17–25)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-DAG-ALEF-001']
- **Examples:**
  - `וַיָּבִ֨יאּוּ לָ֜נוּ` → `vaɟɟɔːˈviːiʔʔuː` (Ezra 8.18)

### TH-DAG-ALEF-T1-004: Canonical geminated alef: Lev. 23.17

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** dagesh / canonical alef dagesh
- **Statement:** The alef in תָּבִ֣יאּוּ ׀ לֶ֣חֶם is canonically geminated.
- **Conditions:** This fixed scriptural token is read.
- **Operation:** Realize אּ as [ʔʔ].
- **Result IPA:** ʔʔ
- **Source:** T1_1.md §I.1.1 (lines 17–25)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-DAG-ALEF-001']
- **Examples:**
  - `תָּבִ֣יאּוּ ׀ לֶ֣חֶם` → `tʰɔːˈviːiʔʔuː` (Lev. 23.17)

### TH-DAG-ALEF-T1-005: Canonical geminated alef: Job 33.21

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** dagesh / canonical alef dagesh
- **Statement:** The alef in לֹ֣א רֻאּֽוּ is canonically geminated.
- **Conditions:** This fixed scriptural token is read.
- **Operation:** Realize אּ as [ʔʔ].
- **Result IPA:** ʔʔ
- **Source:** T1_1.md §I.1.1 (lines 17–25)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-DAG-ALEF-001']
- **Examples:**
  - `לֹ֣א רֻאּֽוּ` → `ʀ̟uʔˈʔuː` (Job 33.21)

## gemination

### TH-CON-RESH-T1-005: Geminated resh

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** gemination / resh
- **Statement:** Dagesh-marked resh is geminate primary uvular [ʀ̟ʀ̟], not alveolar [rˁ].
- **Conditions:** ר bears dagesh and does not occur in the [rˁ] environments.
- **Operation:** Geminate the advanced uvular trill.
- **Result IPA:** ʀ̟ʀ̟
- **Source:** T1_1.md §I.1.20 (lines 1369–1371)
- **Certainty:** high
- **Examples:**
  - `הַרְּעִמָ֑הּ` → `hɑʀ̟ʀ̟iʕiːˈmɔːɔh` (1 Sam. 1.6)

### TH-CON-YOD-T1-002: Geminated yod stop

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** gemination / yod
- **Statement:** Geminated yod strengthens from [j] to a voiced palatal stop [ɉɉ].
- **Conditions:** י is geminated or marked with dagesh.
- **Operation:** Strengthen [j] to a geminate palatal stop.
- **Result IPA:** ɉɉ
- **Source:** T1_1.md §I.1.10 (lines 995–1003)
- **Certainty:** high
- **Examples:**
  - `וַיַּשְׁמֵ֣ד` → `vaɉɉaʃˈmeːeð` (1 Kings 16.12)

## vowels

### TH-DAG-T3-012: Gemination preserves high u

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowels / high-vowel-preservation
- **Statement:** Gemination after lexical /u/ may preserve the high vowel against reduction to epenthetic shewa.
- **Conditions:** A consonant follows lexical /u/ represented by qibbuṣ.; The lexeme belongs to an attested pattern.
- **Operation:** Geminate the following consonant; retain /u/.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.5.1 (lines 179–199)
- **Certainty:** high
- **Examples:**
  - `עֲמֻקָּה` → `—`
  - `לֻקַּ֖ח` → `—` (Gen. 3.23)

### TH-DAG-T3-013: Gemination preserves high i

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowels / high-vowel-preservation
- **Statement:** Gemination after lexical /i/ may preserve the high vowel against reduction.
- **Conditions:** A consonant follows lexical /i/ represented by ḥireq.; The form is lexically attested.
- **Operation:** Geminate the following consonant; retain /i/.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.5.2 (lines 201–203)
- **Certainty:** high
- **Examples:**
  - `אִסָּר` → `—`

### TH-DAG-T3-014: Gemination replaces pretonic lengthening

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowels / quantity
- **Statement:** At certain stem-suffix boundaries, gemination preserves original short *a instead of allowing pretonic lengthening.
- **Conditions:** Original short *a precedes a consonant at a morphological boundary.; The syllable would otherwise be open and pretonic.
- **Operation:** Geminate the consonant and retain the preceding vowel as short.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.6 (lines 205–231)
- **Certainty:** high
- **Examples:**
  - `גְּמַלִּים` → `—`
  - `קְטַנִּים` → `—`

### TH-DAG-T3-020: Interrogative he compensatory vowel

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowels / compensatory-lengthening
- **Statement:** Before a guttural, interrogative he takes long pataḥ, or long segol before qameṣ, as a substitute for gemination.
- **Conditions:** Interrogative ה precedes a guttural.
- **Operation:** Block guttural gemination and lengthen the prefix vowel.
- **Result IPA:** aː or ɛː
- **Source:** T1_3B.md §I.3.1.8 (lines 283–289)
- **Certainty:** high
- **Examples:**
  - `הַע֥וֹד` → `haːˈʕoːoð` (Gen. 31.14)

### TH-LEN-T2-001: Stressed basic-sign vowel lengthening

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / length
- **Statement:** A vowel represented by a basic vowel sign is long in a stressed syllable.
- **Conditions:** basic vowel sign; syllable bears stress
- **Operation:** Lengthen the vowel.
- **Result IPA:** Vː
- **Source:** T1_2B_corrected_p352.md §I.2.2.1. General Principles (lines 278–284)
- **Certainty:** high
- **Examples:**
  - `מֶ֫לֶךְ` → `ˈmɛːlɛχ`
  - `נַ֫עַר` → `ˈnaːʕɑʀ̟`

### TH-LEN-T2-002: Open unstressed vowel lengthening

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / length
- **Statement:** A vowel represented by a basic vowel sign is long in an unstressed open syllable.
- **Conditions:** basic vowel sign; unstressed syllable; open syllable
- **Operation:** Lengthen the vowel.
- **Result IPA:** Vː
- **Source:** T1_2B_corrected_p352.md §I.2.2.1. General Principles (lines 278–284)
- **Certainty:** high
- **Examples:**
  - `הַה֫וּא` → `haːˈhuː`
  - `יַעֲלֶ֫ה` → `yaːʕaˈlɛː`

### TH-LEN-T2-003: Closed unstressed vowel shortening

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / length
- **Statement:** A vowel represented by a basic vowel sign is short in an unstressed closed syllable.
- **Conditions:** basic vowel sign; unstressed syllable; closed syllable
- **Operation:** Realize the vowel short.
- **Result IPA:** V
- **Source:** T1_2B_corrected_p352.md §I.2.2.1. General Principles (lines 278–284)
- **Certainty:** high
- **Examples:**
  - `כָּל־` → `kʰɔl` (Isa. 38.17)
  - `וְנִחַמְתִּ֣י` → `vaniːħamˈtʰiː` (Jer. 26.3)

### TH-LEN-T2-004: Stressed qameṣ

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / length-instance
- **Statement:** In this structural context, stressed qameṣ is realized as [ɔː].
- **Conditions:** stressed qameṣ
- **Operation:** Apply the general stress/open-syllable length rule.
- **Result IPA:** ɔː
- **Source:** T1_2B_corrected_p352.md §I.2.2.2. Stressed Syllables (lines 294–302)
- **Certainty:** high
- **Examples:**
  - `שָׂרָ֑ה` → `sɔːˈʀ̟ɔː` (Gen. 21.7)

### TH-LEN-T2-005: Stressed pataḥ

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / length-instance
- **Statement:** In this structural context, stressed pataḥ is realized as [aː].
- **Conditions:** stressed pataḥ
- **Operation:** Apply the general stress/open-syllable length rule.
- **Result IPA:** aː
- **Source:** T1_2B_corrected_p352.md §I.2.2.2. Stressed Syllables (lines 304–314)
- **Certainty:** high
- **Examples:**
  - `וַיַּ֤עַשׂ` → `vaɟˈɟaːʕas` (Gen. 21.8)

### TH-LEN-T2-006: Stressed segol

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / length-instance
- **Statement:** In this structural context, stressed segol is realized as [ɛː].
- **Conditions:** stressed segol
- **Operation:** Apply the general stress/open-syllable length rule.
- **Result IPA:** ɛː
- **Source:** T1_2B_corrected_p352.md §I.2.2.2. Stressed Syllables (lines 316–326)
- **Certainty:** high
- **Examples:**
  - `הַגֶּ֗בֶר` → `hagˈgɛːvɛʀ̟` (Psa. 52.9)

### TH-LEN-T2-007: Stressed ṣere

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / length-instance
- **Statement:** In this structural context, stressed ṣere is realized as [eː].
- **Conditions:** stressed ṣere
- **Operation:** Apply the general stress/open-syllable length rule.
- **Result IPA:** eː
- **Source:** T1_2B_corrected_p352.md §I.2.2.2. Stressed Syllables (lines 328–334)
- **Certainty:** high
- **Examples:**
  - `וַתֵּ֨שֶׁב` → `vatˈtʰeːʃɛv` (Gen. 21.16)

### TH-LEN-T2-008: Stressed ḥireq

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / length-instance
- **Statement:** In this structural context, stressed ḥireq is realized as [iː].
- **Conditions:** stressed ḥireq
- **Operation:** Apply the general stress/open-syllable length rule.
- **Result IPA:** iː
- **Source:** T1_2B_corrected_p352.md §I.2.2.2. Stressed Syllables (lines 336–344)
- **Certainty:** high
- **Examples:**
  - `וַיִּ֨בֶן` → `vaɟˈɟiːvɛn` (Gen. 22.9)

### TH-LEN-T2-009: Stressed ḥolem

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / length-instance
- **Statement:** In this structural context, stressed ḥolem is realized as [oː].
- **Conditions:** stressed ḥolem
- **Operation:** Apply the general stress/open-syllable length rule.
- **Result IPA:** oː
- **Source:** T1_2B_corrected_p352.md §I.2.2.2. Stressed Syllables (lines 346–352)
- **Certainty:** high
- **Examples:**
  - `הַגָּדֹ֖ל` → `haggɔːˈðoːol` (Exod. 3.3)

### TH-LEN-T2-010: Stressed shureq/qibbuṣ

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / length-instance
- **Statement:** In this structural context, stressed shureq/qibbuṣ is realized as [uː].
- **Conditions:** stressed shureq/qibbuṣ
- **Operation:** Apply the general stress/open-syllable length rule.
- **Result IPA:** uː
- **Source:** T1_2B_corrected_p352.md §I.2.2.2. Stressed Syllables (lines 354–362)
- **Certainty:** high
- **Examples:**
  - `וַיָּקֻ֛מוּ` → `vaɟɟɔːˈq̟uːmuː` (Gen. 22.19)

### TH-LEN-T2-011: Open unstressed pataḥ

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / length-instance
- **Statement:** In this structural context, open unstressed pataḥ is realized as [aː].
- **Conditions:** open unstressed pataḥ
- **Operation:** Apply the general stress/open-syllable length rule.
- **Result IPA:** aː
- **Source:** T1_2B_corrected_p352.md §I.2.2.3. Open Unstressed Syllables (lines 376–382)
- **Certainty:** high
- **Examples:**
  - `הַהִ֔וא` → `haːˈhiː` (Gen. 21.22)

### TH-LEN-T2-012: Open unstressed segol

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / length-instance
- **Statement:** In this structural context, open unstressed segol is realized as [ɛː].
- **Conditions:** open unstressed segol
- **Operation:** Apply the general stress/open-syllable length rule.
- **Result IPA:** ɛː
- **Source:** T1_2B_corrected_p352.md §I.2.2.3. Open Unstressed Syllables (lines 384–390)
- **Certainty:** high
- **Examples:**
  - `בֶּחָ֑רֶב` → `bɛːˈħɔːʀ̟ɛv` (Num. 14.43)

### TH-LEN-T2-013: Open unstressed shureq

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / length-instance
- **Statement:** In this structural context, open unstressed shureq is realized as [uː].
- **Conditions:** open unstressed shureq
- **Operation:** Apply the general stress/open-syllable length rule.
- **Result IPA:** uː
- **Source:** T1_2B_corrected_p352.md §I.2.2.3. Open Unstressed Syllables (lines 410–420)
- **Certainty:** high
- **Examples:**
  - `רְאוּבֵ֣ן` → `ʀ̟uʔuːˈveːen` (Exod. 1.2)

### TH-LEN-T2-014: Ṣere is invariably long

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / inherent-length
- **Statement:** Ṣere has no short surface variant and is invariably long.
- **Conditions:** ṣere
- **Operation:** Preserve long duration.
- **Result IPA:** eː
- **Source:** T1_2B_corrected_p352.md §I.2.2.4. Closed Unstressed Syllables (lines 458–458)
- **Certainty:** high
- **Examples:**
  - `מֵבִ֫יא` → `meːˈviː`

### TH-LEN-T2-015: Ḥolem is invariably long

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / inherent-length
- **Statement:** Ḥolem has no short surface variant and is invariably long.
- **Conditions:** ḥolem
- **Operation:** Preserve long duration.
- **Result IPA:** oː
- **Source:** T1_2B_corrected_p352.md §I.2.2.4. Closed Unstressed Syllables (lines 458–458)
- **Certainty:** high
- **Examples:**
  - `מְקוֹמ֫וֹ` → `maq̟oːˈmoː`

### TH-LEN-T2-027: Lengthening before guttural epenthetic

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / metrical-lengthening
- **Statement:** After guttural epenthesis creates two light syllables, the vowel before the guttural is lengthened.
- **Conditions:** short open syllable before guttural; following weak epenthetic syllable
- **Operation:** Lengthen preceding vowel after epenthesis.
- **Result IPA:** Vː.GV
- **Source:** T1_2B_corrected_p352.md §I.2.5.4. _Ḥaṭef_ Signs on Guttural Consonants (lines 1298–1308)
- **Certainty:** high
- **Examples:**
  - `יַעֲל֫וּ` → `jaː.ʕa.ˈluː`

### TH-LEN-T2-028: Secondary stress lengthens lexical [ɔ]

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / lexical-hatef
- **Statement:** Secondary stress on lexical [ɔ] lengthens it fully to [ɔː] and it is written with simple qameṣ.
- **Conditions:** lexical /o/ in open syllable; secondary stress
- **Operation:** [ɔ] → [ɔː].
- **Result IPA:** ɔː
- **Source:** T1_2B_corrected_p352.md §I.2.7. Lexical _Ḥaṭef_ Vowels (lines 3144–3154)
- **Certainty:** high
- **Examples:**
  - `קָֽדָשִׁ֔ים` → `ˌq̟ɔː.ðɔː.ˈʃiː.im` (Exod. 29.37)

### TH-VAR-T0-020: Ben Asher preposition

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** vowels / Ben Asher
- **Statement:** Ben Asher places shewa on ל/ב before yod with ḥireq.
- **Conditions:** In this environment.
- **Operation:** Use לְיִ-type pointing.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.10 (lines 539–539)
- **Certainty:** high
- **Examples:**
  - `לְיִשְׂרָאֵל` → `—` (I.0.10 line 539)

### TH-VAR-T0-021: Ben Naftali preposition

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** vowels / Ben Naftali
- **Statement:** Ben Naftali places ḥireq on ל/ב and leaves following yod vowelless.
- **Conditions:** In this environment.
- **Operation:** Use לִי-type pointing.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.10 (lines 539–539)
- **Certainty:** high
- **Examples:**
  - `לִישְׂרָאֵל` → `—` (I.0.10 line 539)

### TH-VAR-T0-028: NST vowel interchange

- **Status:** variant
- **Authority:** non-standard-tiberian
- **Category:** vowels / sign-value interchange
- **Statement:** NST manuscripts interchange segol/ṣere and pataḥ/qameṣ, reflecting Palestinian-type vowel mergers.
- **Conditions:** In NST manuscripts.
- **Operation:** Interpret signs manuscript-specifically rather than with Standard values.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.13.6 (lines 694–701)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T0-001: Three pronunciation traditions

- **Status:** evidence
- **Authority:** comparative
- **Category:** vowels / tradition inventory
- **Statement:** Medieval pointing represents Tiberian, Babylonian, and Palestinian pronunciation traditions.
- **Conditions:** When classifying medieval vocalized manuscripts.
- **Operation:** Assign evidence to its pronunciation tradition.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.3 (lines 54–54)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T0-002: Tiberian pataḥ quality

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowels / quality inventory
- **Statement:** Tiberian pataḥ has quality [a].
- **Conditions:** When pataḥ is read in Standard Tiberian.
- **Operation:** Realize pataḥ as [a].
- **Result IPA:** a
- **Source:** T1_0_Intro.md §I.0.3 (lines 56–56)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T0-003: Tiberian qameṣ quality

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowels / quality inventory
- **Statement:** Tiberian qameṣ has quality [ɔ].
- **Conditions:** When qameṣ is read in Standard Tiberian.
- **Operation:** Realize qameṣ as [ɔ].
- **Result IPA:** ɔ
- **Source:** T1_0_Intro.md §I.0.3 (lines 56–56)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T0-004: Tiberian ṣere quality

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowels / quality inventory
- **Statement:** Tiberian ṣere has quality [e].
- **Conditions:** When ṣere is read in Standard Tiberian.
- **Operation:** Realize ṣere as [e].
- **Result IPA:** e
- **Source:** T1_0_Intro.md §I.0.3 (lines 56–56)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T0-005: Tiberian segol quality

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowels / quality inventory
- **Statement:** Tiberian segol has quality [ɛ].
- **Conditions:** When segol is read in Standard Tiberian.
- **Operation:** Realize segol as [ɛ].
- **Result IPA:** ɛ
- **Source:** T1_0_Intro.md §I.0.3 (lines 56–56)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T0-006: Babylonian pataḥ-segol merger

- **Status:** variant
- **Authority:** comparative
- **Category:** vowels / Babylonian inventory
- **Statement:** Babylonian generally does not distinguish Tiberian [a] and [ɛ], using [a].
- **Conditions:** Where Babylonian pataḥ corresponds to Tiberian segol.
- **Operation:** Merge both qualities as [a].
- **Result IPA:** a
- **Source:** T1_0_Intro.md §I.0.3 (lines 56–56)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T0-007: Palestinian low-vowel merger

- **Status:** variant
- **Authority:** comparative
- **Category:** vowels / Palestinian inventory
- **Statement:** Palestinian pronunciation merges pataḥ and qameṣ as one a-vowel.
- **Conditions:** In Palestinian pronunciation.
- **Operation:** Merge pataḥ and qameṣ.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.3 (lines 56–56)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T0-008: Palestinian front-vowel merger

- **Status:** variant
- **Authority:** comparative
- **Category:** vowels / Palestinian inventory
- **Statement:** Palestinian pronunciation merges ṣere and segol as one e-vowel.
- **Conditions:** In Palestinian pronunciation.
- **Operation:** Merge ṣere and segol.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.3 (lines 56–56)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T0-009: Babylonian unstressed a

- **Status:** variant
- **Authority:** comparative
- **Category:** vowels / conservation
- **Statement:** Babylonian preserves unstressed /a/ in closed syllables where Tiberian often has /i/.
- **Conditions:** In cited comparative forms.
- **Operation:** Preserve /a/.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.8 (lines 358–360)
- **Certainty:** high
- **Examples:**
  - `מַבצַר` → `mavˈsˁɑːr` (I.0.8 line 360)

### TH-VOW-T0-010: Babylonian unstressed o

- **Status:** variant
- **Authority:** comparative
- **Category:** vowels / conservation
- **Statement:** Babylonian preserves unstressed /o/ in prefix verbs where Tiberian reduces it to shewa.
- **Conditions:** In cited comparative forms.
- **Operation:** Preserve /o/.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.8 (lines 360–360)
- **Certainty:** high
- **Examples:**
  - `תִטבֹלֵנִי` → `tiṭboˈleːniː` (I.0.8 line 360)

### TH-VOW-T0-011: Babylonian ḥolem-to-ṣere

- **Status:** variant
- **Authority:** comparative
- **Category:** vowels / innovation
- **Statement:** Babylonian shows a characteristic shift of ḥolem to ṣere.
- **Conditions:** In affected Babylonian forms.
- **Operation:** Front ḥolem to ṣere quality.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.8 (lines 370–370)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T0-012: Compound Babylonian length evidence

- **Status:** evidence
- **Authority:** manuscript
- **Category:** vowels / length
- **Statement:** Compound Babylonian signs distinguish short vowels in open and closed syllables from long vowels and thus reveal Tiberian length.
- **Conditions:** When Babylonian signs represent Tiberian reading.
- **Operation:** Infer length from the sign class.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.13.7 (lines 705–708)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T2-001: Pataḥ front quality

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / quality
- **Statement:** Open, unrounded front [a].
- **Conditions:** basic vowel sign is pataḥ
- **Operation:** Assign vowel quality.
- **Result IPA:** a
- **Source:** T1_2B_corrected_p352.md §I.2.1.1. The Qualities of the Vowels (lines 7–9)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T2-002: Pataḥ back quality

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / quality
- **Statement:** Open, unrounded back [ɑ].
- **Conditions:** basic vowel sign is pataḥ
- **Operation:** Assign vowel quality.
- **Result IPA:** ɑ
- **Source:** T1_2B_corrected_p352.md §I.2.1.1. The Qualities of the Vowels (lines 7–9)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T2-003: Qameṣ quality

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / quality
- **Statement:** Back, open-mid rounded [ɔ].
- **Conditions:** basic vowel sign is qameṣ
- **Operation:** Assign vowel quality.
- **Result IPA:** ɔ
- **Source:** T1_2B_corrected_p352.md §I.2.1.1. The Qualities of the Vowels (lines 11–11)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T2-004: Segol quality

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / quality
- **Statement:** Front, open-mid unrounded [ɛ].
- **Conditions:** basic vowel sign is segol
- **Operation:** Assign vowel quality.
- **Result IPA:** ɛ
- **Source:** T1_2B_corrected_p352.md §I.2.1.1. The Qualities of the Vowels (lines 12–12)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T2-005: Ṣere quality

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / quality
- **Statement:** Front, close-mid unrounded [e].
- **Conditions:** basic vowel sign is ṣere
- **Operation:** Assign vowel quality.
- **Result IPA:** e
- **Source:** T1_2B_corrected_p352.md §I.2.1.1. The Qualities of the Vowels (lines 13–13)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T2-006: Ḥireq quality

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / quality
- **Statement:** Front, close, unrounded [i].
- **Conditions:** basic vowel sign is ḥireq
- **Operation:** Assign vowel quality.
- **Result IPA:** i
- **Source:** T1_2B_corrected_p352.md §I.2.1.1. The Qualities of the Vowels (lines 14–14)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T2-007: Ḥolem quality

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / quality
- **Statement:** Back, close-mid rounded [o].
- **Conditions:** basic vowel sign is ḥolem
- **Operation:** Assign vowel quality.
- **Result IPA:** o
- **Source:** T1_2B_corrected_p352.md §I.2.1.1. The Qualities of the Vowels (lines 15–15)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T2-008: Shureq quality

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / quality
- **Statement:** Back, close, rounded [u].
- **Conditions:** basic vowel sign is shureq
- **Operation:** Assign vowel quality.
- **Result IPA:** u
- **Source:** T1_2B_corrected_p352.md §I.2.1.1. The Qualities of the Vowels (lines 16–16)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T2-009: Qibbuṣ quality

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowel / quality
- **Statement:** Back, close, rounded [u].
- **Conditions:** basic vowel sign is qibbuṣ
- **Operation:** Assign vowel quality.
- **Result IPA:** u
- **Source:** T1_2B_corrected_p352.md §I.2.1.1. The Qualities of the Vowels (lines 16–16)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T4-101: Palestinian a/e sign interchanges

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** vowels / Palestinian-substrate
- **Statement:** Non-Standard manuscripts may interchange pataḥ/qameṣ and segol/ṣere under a Palestinian one-a/one-e substrate.
- **Conditions:** The reading has a Palestinian phonological substrate.
- **Operation:** Record sign/quality mergers as imperfect convergence, not Standard Tiberian equivalence.
- **Result IPA:** None
- **Source:** T1_4B_5_Ref.md §I.4.3.1 (lines 116–124)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T4-102: Independent e-sign and e-quality confusion

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** vowels / imperfect-learning
- **Statement:** In BL Or 2555, segol and ṣere signs and [ɛː]/[eː] qualities vary independently because both target vowels map to one substrate prototype.
- **Conditions:** Reading BL Or 2555 long e-vowels.
- **Operation:** Allow evidence-level mismatch between sign and [ɛː]/[eː] token.
- **Result IPA:** ɛː ~ eː
- **Source:** T1_4B_5_Ref.md §I.4.3.2 (lines 126–167)
- **Certainty:** high
- **Examples:**
  - `יָדֶ֑ךָ` → `jɔːˈðɛːχɔː` (Ecc. 7.18)
  - `יָפֶ֣ה` → `jɔːˈfeː` (Ecc. 3.11)

### TH-VOW-T4-103: Arabic-substrate segol–pataḥ interchange

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** vowels / Arabic-substrate
- **Statement:** Arabic substrate matching can cause segol and pataḥ signs/qualities to interchange.
- **Conditions:** The reader maps Tiberian vowel tokens onto Arabic /a/ and /ā/ prototypes.
- **Operation:** Record segol–pataḥ confusion as non-standard interference.
- **Result IPA:** None
- **Source:** T1_4B_5_Ref.md §I.4.3.3 (lines 169–195)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T4-104: Three- and four-way vowel interchange

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** vowels / Arabic-substrate
- **Statement:** Reduced perception of Tiberian contrasts can produce pataḥ–segol–ṣere and pataḥ–segol–qameṣ–ṣere interchanges.
- **Conditions:** The reader maps multiple Tiberian qualities onto broad Arabic /a, ā/ allophony.
- **Operation:** Record the attested multi-way confusion only for the relevant manuscript.
- **Result IPA:** None
- **Source:** T1_4B_5_Ref.md §I.4.3.3 (lines 197–245)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T4-105: Hypercorrect vowel lengthening

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** vowels / hypercorrection
- **Statement:** BL Or 2539 MS B hypercorrectly lengthens historically short qameṣ, segol, and even ḥaṭef qameṣ by analogy with deḥiq.
- **Conditions:** Reading BL Or 2539 MS B.; Historically short qameṣ/segol occurs in an unstressed closed syllable.
- **Operation:** Variant lengthening, represented with mater lectionis.
- **Result IPA:** None
- **Source:** T1_4B_5_Ref.md §I.4.3.4 (lines 247–269)
- **Certainty:** high
- **Examples:**
  - `קָדְשֵׁ֣י` → `—` (Num. 18.8)

### TH-VOW-T4-201: pataḥ inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowels / inventory
- **Statement:** אַ (pataḥ) has canonical realization [a], [ɑ], [aː], [ɑː] and phonemic analysis /a/.
- **Conditions:** Apply quantity and conditioning stated in the table.
- **Operation:** Map the vowel sign to its canonical realization(s).
- **Result IPA:** a, ɑ, aː, ɑː
- **Source:** T1_4B_5_Ref.md §I.5.2 (lines 319–319)
- **Certainty:** high
- **Notes:** Long in stressed or open unstressed syllables.
- **Examples:** no example in source

### TH-VOW-T4-202: qameṣ inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowels / inventory
- **Statement:** אָ (qameṣ) has canonical realization [ɔ], [ɔː] and phonemic analysis /o/ when short; /ɔ̄/ when long.
- **Conditions:** Apply quantity and conditioning stated in the table.
- **Operation:** Map the vowel sign to its canonical realization(s).
- **Result IPA:** ɔ, ɔː
- **Source:** T1_4B_5_Ref.md §I.5.2 (lines 320–320)
- **Certainty:** high
- **Notes:** Long in stressed or open unstressed syllables.
- **Examples:** no example in source

### TH-VOW-T4-203: segol inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowels / inventory
- **Statement:** אֶ (segol) has canonical realization [ɛ], [ɛː] and phonemic analysis /ɛ/; /e/ in specified final forms.
- **Conditions:** Apply quantity and conditioning stated in the table.
- **Operation:** Map the vowel sign to its canonical realization(s).
- **Result IPA:** ɛ, ɛː
- **Source:** T1_4B_5_Ref.md §I.5.2 (lines 321–321)
- **Certainty:** high
- **Notes:** Long in stressed or open unstressed syllables.
- **Examples:** no example in source

### TH-VOW-T4-204: ṣere inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowels / inventory
- **Statement:** אֵ (ṣere) has canonical realization [eː] and phonemic analysis /e/, /ē/.
- **Conditions:** Apply quantity and conditioning stated in the table.
- **Operation:** Map the vowel sign to its canonical realization(s).
- **Result IPA:** eː
- **Source:** T1_4B_5_Ref.md §I.5.2 (lines 322–322)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T4-205: ḥireq inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowels / inventory
- **Statement:** אִ (ḥireq) has canonical realization [i], [iː] and phonemic analysis /i/, /ī/.
- **Conditions:** Apply quantity and conditioning stated in the table.
- **Operation:** Map the vowel sign to its canonical realization(s).
- **Result IPA:** i, iː
- **Source:** T1_4B_5_Ref.md §I.5.2 (lines 323–323)
- **Certainty:** high
- **Notes:** Long in stressed or open unstressed syllables.
- **Examples:** no example in source

### TH-VOW-T4-206: ḥolem inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowels / inventory
- **Statement:** אֹ (ḥolem) has canonical realization [oː] and phonemic analysis /o/ in specified final forms; /ō/.
- **Conditions:** Apply quantity and conditioning stated in the table.
- **Operation:** Map the vowel sign to its canonical realization(s).
- **Result IPA:** oː
- **Source:** T1_4B_5_Ref.md §I.5.2 (lines 324–324)
- **Certainty:** high
- **Examples:** no example in source

### TH-VOW-T4-207: shureq/qibbuṣ inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** vowels / inventory
- **Statement:** אוּ, אֻ (shureq/qibbuṣ) has canonical realization [u], [uː] and phonemic analysis /u/, /ū/.
- **Conditions:** Apply quantity and conditioning stated in the table.
- **Operation:** Map the vowel sign to its canonical realization(s).
- **Result IPA:** u, uː
- **Source:** T1_4B_5_Ref.md §I.5.2 (lines 325–325)
- **Certainty:** high
- **Notes:** Long in stressed or open unstressed syllables.
- **Examples:** no example in source

## shewa

### TH-SHEWA-T2-001: Vocalic shewa default [a]

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / quality
- **Statement:** Vocalic shewa has the default quality [a].
- **Conditions:** shewa is vocalic; no conditioning guttural or yod
- **Operation:** Insert short [a].
- **Result IPA:** a
- **Source:** T1_2B_corrected_p352.md §I.2.5.1.1. Default Realization of _Shewa_ (lines 907–914)
- **Certainty:** high
- **Examples:**
  - `תְּכַסֶּ֥ה` → `tʰaχasˈsɛː` (Job 21.26)
  - `מְדַבְּרִ֣ים` → `maðabbaˈʀ̟iːim` (Esther 2.14)

### TH-SHEWA-T2-002: Shewa copies following guttural vowel

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / assimilation
- **Statement:** Vocalic shewa before a guttural is a short vowel with the quality of the vowel on the guttural.
- **Conditions:** vocalic shewa; immediately before אהחע
- **Operation:** Copy the following guttural's vowel quality.
- **Result IPA:** V̆
- **Source:** T1_2B_corrected_p352.md §I.2.5.1.2. Contextually-Conditioned Realization of _Shewa_ (lines 1039–1055)
- **Certainty:** high
- **Examples:**
  - `בְּעֶרְכְּךָ֛` → `bɛʕɛʀ̟kʰaˈχɔː` (Lev. 5.15)
  - `מְחִ֫יר` → `miˈħiːiʀ̟`

### TH-SHEWA-T2-003: Shewa before yod is [i]

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / assimilation
- **Statement:** Vocalic shewa before yod is realized as short [i].
- **Conditions:** vocalic shewa; immediately before yod
- **Operation:** Realize shewa as [i].
- **Result IPA:** i
- **Source:** T1_2B_corrected_p352.md §I.2.5.1.2. Contextually-Conditioned Realization of _Shewa_ (lines 1057–1065)
- **Certainty:** high
- **Examples:**
  - `בְּי֛וֹם` → `biˈjoːom` (Gen. 2.17)
  - `לְיִשְׂרָאֵל֙` → `lijisrˁɔːˈʔeːel` (Gen. 46.2)

### TH-SHEWA-T2-004: Initial onset cluster epenthesis

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / epenthesis
- **Statement:** A word-initial /CC/ onset cluster is broken phonetically by vocalic shewa.
- **Conditions:** word-initial /CC/
- **Operation:** Insert [a] by default between the consonants.
- **Result IPA:** Ca.C
- **Source:** T1_2B_corrected_p352.md §I.2.5.3. Phonological Principles (lines 1238–1246)
- **Certainty:** high
- **Examples:**
  - `מְקוֹמ֫וֹ` → `ma.q̟oː.ˈmoː`
  - `סְפָרִ֫ים` → `sa.fɔː.ˈʀ̟iː.im`

### TH-SHEWA-T2-005: Numeral two has silent initial shewa

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / lexical-exception
- **Statement:** The initial shewa in שְׁתַּיִם, שְׁתֵּי and שְׁתֵּים is silent in the described Tiberian analysis.
- **Conditions:** lexeme is feminine numeral 'two' or first component of 'twelve'
- **Operation:** Do not insert a vowel after shin.
- **Result IPA:** ʃt
- **Source:** T1_2B_corrected_p352.md §I.2.5.3. Phonological Principles (lines 1248–1268)
- **Certainty:** high
- **Examples:**
  - `שְׁתַּיִם` → `ˈʃtaːjim`
  - `שְׁתֵּי` → `ʃteː`

### TH-SHEWA-T2-006: Word-internal CCC cluster repair

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / epenthesis
- **Statement:** Word-internal /CCC/ is syllabified /C.CC/, and the onset cluster is split by vocalic shewa.
- **Conditions:** word-internal /CCC/
- **Operation:** /C.CC/ → [C.Ca.C].
- **Result IPA:** C.Ca.C
- **Source:** T1_2B_corrected_p352.md §I.2.5.3. Phonological Principles (lines 1282–1286)
- **Certainty:** high
- **Examples:**
  - `יִכְתְּבוּ` → `yiχ.tʰa.ˈvuː`

### TH-SHEWA-T2-007: Shewa under geminate is vocalic

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / gemination
- **Statement:** A shewa under a word-internal geminated consonant is vocalic.
- **Conditions:** word-internal consonant has dagesh forte and shewa
- **Operation:** Realize vocalic [a] after the first mora of the geminate.
- **Result IPA:** CaC
- **Source:** T1_2B_corrected_p352.md §I.2.5.3. Phonological Principles (lines 1288–1292)
- **Certainty:** high
- **Examples:**
  - `הַמְּלָכִ֖ים` → `ham.ma.lɔː.χiː.im` (Gen. 14.17)

### TH-SHEWA-T2-008: Silent shewa after long vowel

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / post-long-vowel
- **Statement:** Within a word, shewa after a long vowel is silent as the general rule.
- **Conditions:** word-internal shewa; preceding vowel long
- **Operation:** Suppress shewa vowel; insert same-quality epenthetic before its consonant.
- **Result IPA:** Vː.VC
- **Source:** T1_2B_corrected_p352.md §I.2.5.6. Silent _Shewa_ after a Long Vowel (lines 1592–1604)
- **Certainty:** high
- **Examples:**
  - `יֵשְׁבוּ֙` → `jeːeʃˈvuː` (Gen. 47.6)
  - `שָׁמְר֥וּ` → `ʃɔːɔmˈʀ̟uː` (Jud. 2.22)

### TH-SHEWA-T2-009: Post-long shewa vocalic on gutturals

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / post-long-vowel-exception
- **Statement:** After a long vowel, shewa on a guttural is vocalic and is explicitly written with a ḥaṭef sign.
- **Conditions:** long vowel; following consonant is guttural with shewa
- **Operation:** Realize an epenthetic after the guttural.
- **Result IPA:** Vː.Ga
- **Source:** T1_2B_corrected_p352.md §I.2.5.7.1. On Guttural Consonants (lines 1638–1648)
- **Certainty:** high
- **Examples:**
  - `כֹּהֲנִים` → `kʰoːhaˈniːim`
  - `צֹעֲקִ֥ים` → `sˁoːʕaˈq̟iːim` (Gen. 4.10)

### TH-SHEWA-T2-010: Post-long shewa vocalic between identical consonants

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / identical-consonants
- **Statement:** Shewa on the first of two identical consonants is vocalic when the preceding vowel is long.
- **Conditions:** long vowel; CְC with identical consonants
- **Operation:** Insert [a] between the identical consonants.
- **Result IPA:** VːCaC
- **Source:** T1_2B_corrected_p352.md §I.2.5.7.3. Long Vowel before Two Identical Consonants (lines 1660–1678)
- **Certainty:** high
- **Examples:**
  - `לָקְק֤וּ` → `lɔːq̟aˈq̟uː` (1 Kings 21.19)
  - `סָבְב֥וּ` → `sɔːvaˈvuː` (Josh. 6.15)

### TH-SHEWA-T2-011: Post-short shewa silent between identical consonants

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / identical-consonants
- **Statement:** Shewa on the first of two identical consonants is silent when the preceding vowel is short.
- **Conditions:** short vowel; CְC with identical consonants
- **Operation:** Keep CVC bimoraic; do not insert vowel.
- **Result IPA:** VCC
- **Source:** T1_2B_corrected_p352.md §I.2.5.7.3. Long Vowel before Two Identical Consonants (lines 1680–1692)
- **Certainty:** high
- **Examples:**
  - `הִנְנִי֩` → `hinˈniː` (Gen. 6.17)
  - `רִבְב֣וֹת` → `ʀ̟ivˈvoːoθ` (Deut. 33.17)

### TH-SHEWA-T2-012: Prefixed long particle before resh

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / morpheme-boundary
- **Statement:** In nouns, shewa on stem-initial resh after a prefixed particle with long qameṣ or ṣere is vocalic.
- **Conditions:** noun stem begins resh+shewa; prefixed particle has /ɔ̄/ or /ē/
- **Operation:** Realize resh's shewa, normally [a], and align foot boundary with morpheme boundary.
- **Result IPA:** Vː.ʀ̟a
- **Source:** T1_2B_corrected_p352.md §I.2.5.7.4. Long Vowel in a Prefixed Particle before Resh (lines 1724–1748)
- **Certainty:** high
- **Examples:**
  - `הָרְשָׁעִ֑ים` → `hɔːʀ̟ɑʃɔːˈʕiːim` (Psa. 1.4)
  - `מֵרְכ֥וּשׁ` → `meːʀ̟ɑˈχuːuʃ` (2 Chron. 35.7)

### TH-SHEWA-T2-013: Post-short medial shewa default silent

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / post-short-vowel
- **Statement:** A medial shewa on an ungeminated consonant after a short vowel is normally silent.
- **Conditions:** medial shewa; preceding vowel short; consonant lacks dagesh
- **Operation:** Syllabify consonant as coda; realize zero.
- **Result IPA:** CVC
- **Source:** T1_2B_corrected_p352.md §I.2.5.8. Vocalic _Shewa_ after Short Vowel Phonemes (lines 1978–1984)
- **Certainty:** high
- **Examples:**
  - `מַמְרֵ֖א` → `mam.ˈʀ̟eː` (Gen. 13.18)

### TH-SHEWA-T2-014: Article plus mem resyllabification

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / article-mem
- **Statement:** When article /ha-/ precedes mem+shewa and expected mem gemination is lost, mem is often resyllabified as the onset of the following syllable and its shewa is vocalic.
- **Conditions:** definite article; stem begins מְ; mem gemination lost; licensed lexical/prosodic case
- **Operation:** Lengthen article /a/ compensatorily and vocalize mem's shewa.
- **Result IPA:** haːma
- **Source:** T1_2B_corrected_p352.md §I.2.5.8.1. The Definite Article (lines 1986–1996)
- **Certainty:** high
- **Examples:**
  - `הַֽמְדַבֵּ֥ר` → `haːmaðabˈbeːeʀ̟` (Gen. 45.12)

### TH-SHEWA-T2-015: Interrogative he default silent following shewa

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / interrogative-he
- **Statement:** After interrogative he with pataḥ, a following word-initial shewa is often silent.
- **Conditions:** interrogative he; following word begins Cְ
- **Operation:** Realize following shewa as zero.
- **Result IPA:** haC
- **Source:** T1_2B_corrected_p352.md §I.2.5.8.2. Interrogative _He_ (lines 2246–2262)
- **Certainty:** high
- **Examples:**
  - `הַמְעַט֙` → `hamˈʕɑːɑtˁ` (Gen. 30.15)

### TH-SHEWA-T2-016: Interrogative he phonetic-gaʿya resyllabification

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / interrogative-he
- **Statement:** With phonetic gaʿya, interrogative he is lengthened and the following shewa is vocalic to mark the morpheme boundary.
- **Conditions:** interrogative he; phonetic gaʿya; following Cְ
- **Operation:** Lengthen /a/ and vocalize following shewa.
- **Result IPA:** haː.Ca
- **Source:** T1_2B_corrected_p352.md §I.2.5.8.2. Interrogative _He_ (lines 2264–2286)
- **Certainty:** high
- **Examples:**
  - `הַֽמְצָאתַ֖נִי` → `haːmasˁɔːˈθaːniː` (1 Kings 21.20)
  - `הַֽתְמַלֵּ֣א` → `haːθamalˈleː` (Job 40.31)

### TH-SHEWA-T2-017: Phonetic gaʿya separates identical consonants

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / identical-consonants
- **Statement:** Before two identical consonants after an underlying short vowel, phonetic gaʿya can add a mora, resyllabify, and make shewa vocalic.
- **Conditions:** short vowel before CְC identical; phonetic gaʿya
- **Operation:** V → Vː; CְC → C.a.C.
- **Result IPA:** Vː.CaC
- **Source:** T1_2B_corrected_p352.md §I.2.5.8.3. Two Identical Consonants (lines 2324–2340)
- **Certainty:** high
- **Examples:**
  - `צִֽלֲל֑וֹ` → `sˁiːlaˈloː` (Job 40.22)
  - `קִֽלֲלַ֖ת` → `q̟iːlaˈloːoθ` (Jud. 9.57)

### TH-SHEWA-T2-018: Conjunctive vav phonetic-gaʿya vocalization

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / conjunctive-vav
- **Statement:** After initial conjunctive vav, phonetic gaʿya lengthens [u] and can make a following silent shewa vocalic.
- **Conditions:** conjunctive וּ; following consonant has shewa; phonetic gaʿya
- **Operation:** [u] → [uː] and realize shewa vocalically.
- **Result IPA:** wuːCa
- **Source:** T1_2B_corrected_p352.md §I.2.5.8.4. Conjunctive _Vav_ (lines 2466–2480)
- **Certainty:** high
- **Examples:**
  - `וּֽקְרָ֔אוּ` → `wuːq̟aˈʀ̟ɔːʔuː` (Isa. 34.16)

### TH-SHEWA-T2-019: Weak-contact phonetic-gaʿya resyllabification

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / weak-consonants
- **Statement:** A short vowel before silent shewa may be mora-augmented by phonetic gaʿya, making the shewa vocalic to separate weak consonants.
- **Conditions:** suboptimal contact of weak consonants; phonetic gaʿya
- **Operation:** CVC.C → CVː.CV.C.
- **Result IPA:** CVː.Ca.C
- **Source:** T1_2B_corrected_p352.md §I.2.5.8.5. Elsewhere (lines 2568–2582)
- **Certainty:** high
- **Examples:**
  - `יִֽצֲחַק־לִֽי` → `jiːsˁɑħaq̟-ˈliː` (Gen. 21.6)
  - `אַֽרְזֵי־אֵֽל` → `ʔaːʀ̟azeː-ˈʔeːel` (Psa. 80.11)

### TH-SHEWA-T2-020: No shewa on ordinary final consonant

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / word-final-notation
- **Statement:** An ordinary vowelless word-final consonant is generally not marked with shewa.
- **Conditions:** single vowelless final consonant; not final kaf or listed exception
- **Operation:** Realize consonant as coda without written shewa.
- **Result IPA:** C#
- **Source:** T1_2B_corrected_p352.md §I.2.5.9. Marking of _Shewa_ at the End of a Word (lines 2668–2678)
- **Certainty:** high
- **Examples:**
  - `בְּרֵאשִׁ֖ית` → `baʀ̟eːˈʃiːiθ` (Gen. 1.1)

### TH-SHEWA-T2-021: Both shewas silent in final cluster

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / word-final-cluster
- **Statement:** In Standard Tiberian word-final clusters marked with two shewas, both shewas are silent.
- **Conditions:** word-final cluster of two vowelless consonants
- **Operation:** Realize both shewas as zero.
- **Result IPA:** CC#
- **Source:** T1_2B_corrected_p352.md §I.2.5.9.1. In Word-final Consonantal Clusters (lines 2680–2710)
- **Certainty:** high
- **Examples:**
  - `וַיֵּ֣בְךְּ` → `vaɟˈɟeːevk` (Gen. 45.15)
  - `וַיֵּ֥שְׁתְּ` → `vaɟˈɟeːeʃtʰ` (Gen. 9.21)

### TH-SHEWA-T2-022: Shewa before silent final alef

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / orthographic-disambiguation
- **Statement:** When an unpronounced final alef follows the consonant that closes the word, shewa is marked on the pronounced penultimate consonant.
- **Conditions:** orthographic final alef unpronounced; preceding consonant closes syllable
- **Operation:** Mark coda on preceding consonant; do not pronounce alef.
- **Result IPA:** C# (ʾalef ∅)
- **Source:** T1_2B_corrected_p352.md §I.2.5.9.2. Before a Final _ʾAlef_ in the Orthography (lines 2730–2742)
- **Certainty:** high
- **Examples:**
  - `חֵֽטְא` → `ħeːetˁ` (Lev. 19.17)
  - `שָׁ֑וְא` → `ˈʃɔːɔv` (Exod. 23.1)

### TH-SHEWA-T2-023: Final 2fs stop suffix shewa

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / 2fs-suffix
- **Statement:** A plosive tav 2fs suffix after a consonant with silent shewa is itself marked with silent shewa.
- **Conditions:** 2fs suffix tav; preceded by consonant with silent shewa; tav is plosive
- **Operation:** Realize final cluster with no vowel.
- **Result IPA:** Ctʰ#
- **Source:** T1_2B_corrected_p352.md §I.2.5.9.3. Second Person Feminine Singular Pronominal Suffix (lines 2754–2768)
- **Certainty:** high
- **Examples:**
  - `וְיֹלַ֣דְתְּ` → `vijoːˈlaːaðtʰ` (Gen. 16.11)
  - `לִקַּ֤טְתְּ` → `liq̟ˈq̟aːatˁtʰ` (Ruth 2.19)

### TH-SHEWA-T2-024: Final weak-verb 2fs tav unmarked

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / 2fs-suffix
- **Statement:** After a vowel in a final-weak verb, the 2fs tav is fricative and normally has no shewa.
- **Conditions:** 2fs suffix after vowel; final-weak verb
- **Operation:** Realize fricative [θ] without shewa.
- **Result IPA:** θ
- **Source:** T1_2B_corrected_p352.md §I.2.5.9.3. Second Person Feminine Singular Pronominal Suffix (lines 2772–2778)
- **Certainty:** high
- **Examples:**
  - `עָשִׂ֑ית` → `ʕɔːˈsiːiθ` (Gen. 3.13)

### TH-SHEWA-T2-025: Final kaf always marked with shewa

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / final-kaf
- **Statement:** A vowelless word-final kaf is regularly written with shewa.
- **Conditions:** word-final vowelless kaf
- **Operation:** Mark shewa orthographically; realize no vowel.
- **Result IPA:** χ or kʰ as independently conditioned
- **Source:** T1_2B_corrected_p352.md §I.2.5.9.4. Final Kaf (lines 2836–2854)
- **Certainty:** high
- **Examples:**
  - `וְחֹ֖שֶׁךְ` → `—` (Gen. 1.2)

### TH-SHEWA-T4-201: shewa inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / inventory
- **Statement:** Silent shewa is [∅]. Vocalic shewa defaults to [a], copies the following guttural's vowel quality, and is [i] before yod.
- **Conditions:** Apply the conditioning stated in the table.
- **Operation:** Map the sign to its canonical realization.
- **Result IPA:** ∅; a, ɔ, ɛ, e, i, o, u
- **Source:** T1_4B_5_Ref.md §I.5.3 (lines 331–331)
- **Certainty:** high
- **Examples:** no example in source

### TH-SHEWA-T4-202: ḥaṭef pataḥ inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / inventory
- **Statement:** אֲ (ḥaṭef pataḥ) has canonical realization [a] and phonemic analysis /∅/.
- **Conditions:** Apply the conditioning stated in the table.
- **Operation:** Map the sign to its canonical realization.
- **Result IPA:** a
- **Source:** T1_4B_5_Ref.md §I.5.3 (lines 332–332)
- **Certainty:** high
- **Examples:** no example in source

### TH-SHEWA-T4-203: ḥaṭef segol inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / inventory
- **Statement:** אֱ (ḥaṭef segol) has canonical realization [ɛ] and phonemic analysis /∅/.
- **Conditions:** Apply the conditioning stated in the table.
- **Operation:** Map the sign to its canonical realization.
- **Result IPA:** ɛ
- **Source:** T1_4B_5_Ref.md §I.5.3 (lines 333–333)
- **Certainty:** high
- **Examples:** no example in source

### TH-SHEWA-T4-204: ḥaṭef qameṣ inventory

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** shewa / inventory
- **Statement:** אֳ (ḥaṭef qameṣ) has canonical realization [ɔ] and phonemic analysis /∅/; /o/.
- **Conditions:** Apply the conditioning stated in the table.
- **Operation:** Map the sign to its canonical realization.
- **Result IPA:** ɔ
- **Source:** T1_4B_5_Ref.md §I.5.3 (lines 334–334)
- **Certainty:** high
- **Examples:** no example in source

### TH-VAR-T0-025: אכל shewa disagreement

- **Status:** conflict
- **Authority:** standard-tiberian
- **Category:** shewa / Ben Asher versus Ben Naftali
- **Statement:** Before segol in אכל, Ben Asher reads mobile shewa (ḥaṭef pataḥ), while Ben Naftali reads silent shewa.
- **Conditions:** In the specified forms.
- **Operation:** Follow the chosen sub-tradition.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.10 (lines 539–539)
- **Certainty:** unresolved
- **Examples:**
  - `תֹּֽאכֲלֶ֑נָּה` → `—` (I.0.10 line 539)

## hatef

### TH-HATEF-T2-001: ḥaṭef pataḥ quality

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** hatef / quality
- **Statement:** ḥaṭef pataḥ explicitly marks a short vocalic realization [a].
- **Conditions:** ḥaṭef pataḥ
- **Operation:** Realize the compound sign's vowel quality.
- **Result IPA:** a
- **Source:** T1_2B_corrected_p352.md §I.2.5.1.3. _Ḥaṭef_ Signs (lines 1071–1080)
- **Certainty:** high
- **Examples:** no example in source

### TH-HATEF-T2-002: ḥaṭef segol quality

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** hatef / quality
- **Statement:** ḥaṭef segol explicitly marks a short vocalic realization [ɛ].
- **Conditions:** ḥaṭef segol
- **Operation:** Realize the compound sign's vowel quality.
- **Result IPA:** ɛ
- **Source:** T1_2B_corrected_p352.md §I.2.5.1.3. _Ḥaṭef_ Signs (lines 1071–1080)
- **Certainty:** high
- **Examples:** no example in source

### TH-HATEF-T2-003: ḥaṭef qameṣ quality

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** hatef / quality
- **Statement:** ḥaṭef qameṣ explicitly marks a short vocalic realization [ɔ].
- **Conditions:** ḥaṭef qameṣ
- **Operation:** Realize the compound sign's vowel quality.
- **Result IPA:** ɔ
- **Source:** T1_2B_corrected_p352.md §I.2.5.1.3. _Ḥaṭef_ Signs (lines 1071–1080)
- **Certainty:** high
- **Examples:** no example in source

### TH-HATEF-T2-004: Ḥaṭef and vocalic shewa are short

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** hatef / quantity
- **Statement:** Vocalic shewa and ḥaṭef vowels are short, quantitatively equivalent to short vowels in unstressed closed syllables.
- **Conditions:** vocalic shewa or ḥaṭef
- **Operation:** Assign short duration.
- **Result IPA:** V
- **Source:** T1_2B_corrected_p352.md §I.2.5.1.3. _Ḥaṭef_ Signs (lines 1094–1098)
- **Certainty:** high
- **Examples:**
  - `הֲמֶלֶךְ` → `haˈmɛːlɛχ`

### TH-HATEF-T2-005: Guttural epenthesis

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** hatef / guttural
- **Statement:** A guttural that historically closed a medial syllable before another consonant receives a short epenthetic, regularly written with ḥaṭef.
- **Conditions:** medial guttural; historically before a consonant
- **Operation:** Insert a short vowel after the guttural.
- **Result IPA:** ĞV
- **Source:** T1_2B_corrected_p352.md §I.2.5.4. _Ḥaṭef_ Signs on Guttural Consonants (lines 1294–1304)
- **Certainty:** high
- **Examples:** no example in source

### TH-HATEF-T2-006: Guttural epenthetic copies preceding vowel

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** hatef / guttural-assimilation
- **Statement:** The epenthetic after a medial guttural copies the preceding vowel quality.
- **Conditions:** medial guttural epenthesis
- **Operation:** Copy preceding vowel after guttural.
- **Result IPA:** Vː.GV
- **Source:** T1_2B_corrected_p352.md §I.2.5.4. _Ḥaṭef_ Signs on Guttural Consonants (lines 1300–1314)
- **Certainty:** high
- **Examples:**
  - `יַעֲל֫וּ` → `jaː.ʕa.ˈluː`
  - `הֶעֱלָ֫ה` → `hɛː.ʕɛ.ˈlɔː`
  - `טָהֳרָ֫ה` → `tˁɔː.hɔ.ˈʀ̟ɔː`

### TH-HATEF-T2-007: Lexical ḥaṭef qameṣ is /o/

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** hatef / lexical
- **Statement:** Lexical ḥaṭef qameṣ in an open syllable represents /o/ with unspecified length and surfaces unstressed as [ɔ].
- **Conditions:** lexically specified ḥaṭef qameṣ; unstressed open syllable
- **Operation:** /o/ → [ɔ].
- **Result IPA:** ɔ
- **Source:** T1_2B_corrected_p352.md §I.2.7. Lexical _Ḥaṭef_ Vowels (lines 3044–3062)
- **Certainty:** high
- **Examples:**
  - `צֳרִי` → `sˁɔ.ˈʀ̟iː`
  - `דֳּמִי` → `dɔ.ˈmiː`
  - `חֳלִי` → `ħɔ.ˈliː`

### TH-HATEF-T2-008: Stressed lexical /o/ becomes [oː]

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** hatef / lexical
- **Statement:** The lexical /o/ represented unstressed by ḥaṭef qameṣ is realized [oː] under main stress.
- **Conditions:** lexical /o/; main stress
- **Operation:** Lengthen and realize tense [oː].
- **Result IPA:** oː
- **Source:** T1_2B_corrected_p352.md §I.2.7. Lexical _Ḥaṭef_ Vowels (lines 3044–3058)
- **Certainty:** high
- **Examples:**
  - `חֹ֑לִי` → `ˈħoːliː` (Deut. 7.15)
  - `רֹ֑אִי` → `ˈʀ̟oːʔiː` (1 Sam. 16.12)

### TH-HATEF-T2-009: Lexical long rounded vowel shortening

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** hatef / lexical-shortening
- **Statement:** Some lexical ḥaṭef qameṣ vowels result from shortening historical /ō/ or /ɔ̄/ in an unstressed open syllable.
- **Conditions:** historical long rounded vowel; unstressed open syllable; lexically attested shortening
- **Operation:** /ō, ɔ̄/ → /o/ → [ɔ].
- **Result IPA:** ɔ
- **Source:** T1_2B_corrected_p352.md §I.2.7. Lexical _Ḥaṭef_ Vowels (lines 3064–3072)
- **Certainty:** high
- **Examples:**
  - `צִפֳּרִ֑ים` → `sˁip.pʰɔ.ˈʀ̟iː.im` (Lev. 14.49)
  - `בָּ֣מֳתֵי` → `ˈbɔː.mɔ.θeː` (Isa. 14.14)

### TH-HATEF-T2-010: Lexical ḥaṭef resists assimilation

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** hatef / lexical
- **Statement:** Lexical ḥaṭef qameṣ preserves [ɔ] and does not assimilate to a following guttural vowel.
- **Conditions:** lexical ḥaṭef qameṣ; following guttural
- **Operation:** Preserve lexical [ɔ].
- **Result IPA:** ɔ
- **Source:** T1_2B_corrected_p352.md §I.2.7. Lexical _Ḥaṭef_ Vowels (lines 3090–3094)
- **Certainty:** high
- **Examples:**
  - `רֳאִ֑י` → `ʀ̟ɔ.ˈʔiː` (Gen. 16.13)

### TH-HATEF-T2-011: Elision after preceding light syllable

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** hatef / lexical
- **Statement:** A lexical ḥaṭef qameṣ is elided when its degenerate CV foot would follow another monomoraic vocalic-shewa or short conjunctive-vav syllable.
- **Conditions:** preceding monomoraic CV; lexical ḥaṭef qameṣ CV
- **Operation:** Elide the lexical [ɔ].
- **Result IPA:** ∅
- **Source:** T1_2B_corrected_p352.md §I.2.7. Lexical _Ḥaṭef_ Vowels (lines 3122–3127)
- **Certainty:** high
- **Examples:**
  - `בִּדְמִ֥י` → `bið.ˈmiː` (Isa. 38.10)
  - `וּצְרִ֣י` → `wusˁ.ˈrˁiː` (Gen. 37.25)

## syllables

### TH-SYL-T2-001: Split superheavy closed syllable

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** syllable / weight-repair
- **Statement:** A closed syllable containing a long vowel is split phonetically by an epenthetic vowel of the same quality before the final consonant.
- **Conditions:** CV̄C at the phonetic level
- **Operation:** Insert a same-quality epenthetic: CV̄C → CV̄.VC.
- **Result IPA:** CVː.VC
- **Source:** T1_2B_corrected_p352.md §I.2.4. Long Vowels in Closed Syllables (lines 647–665)
- **Certainty:** high
- **Examples:**
  - `ק֫וֹל` → `ˈq̟oː.ol`
  - `יָ֫ד` → `ˈjɔː.ɔð`
  - `בֵּ֫ית` → `ˈbeː.eθ`

### TH-SYL-T2-002: Same-quality epenthesis: לָק֫וּם

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** syllable / weight-repair-instance
- **Statement:** A phonetically long vowel in a closed syllable is followed by a same-quality epenthetic.
- **Conditions:** long vowel; following coda consonant
- **Operation:** Split the vowel-plus-coda into CV̄.VC.
- **Result IPA:** lɔː.ˈq̟uː.um
- **Source:** T1_2B_corrected_p352.md §I.2.4. Long Vowels in Closed Syllables (lines 649–659)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-SYL-001']
- **Examples:**
  - `לָק֫וּם` → `lɔː.ˈq̟uː.um`

### TH-SYL-T2-003: Same-quality epenthesis: הִשְׁמִ֫יד

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** syllable / weight-repair-instance
- **Statement:** A phonetically long vowel in a closed syllable is followed by a same-quality epenthetic.
- **Conditions:** long vowel; following coda consonant
- **Operation:** Split the vowel-plus-coda into CV̄.VC.
- **Result IPA:** hiʃ.ˈmiː.ið
- **Source:** T1_2B_corrected_p352.md §I.2.4. Long Vowels in Closed Syllables (lines 649–659)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-SYL-001']
- **Examples:**
  - `הִשְׁמִ֫יד` → `hiʃ.ˈmiː.ið`

### TH-SYL-T2-004: Same-quality epenthesis: עָמַ֫ד

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** syllable / weight-repair-instance
- **Statement:** A phonetically long vowel in a closed syllable is followed by a same-quality epenthetic.
- **Conditions:** long vowel; following coda consonant
- **Operation:** Split the vowel-plus-coda into CV̄.VC.
- **Result IPA:** ʕɔː.ˈmaː.að
- **Source:** T1_2B_corrected_p352.md §I.2.4. Long Vowels in Closed Syllables (lines 687–695)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-SYL-001']
- **Examples:**
  - `עָמַ֫ד` → `ʕɔː.ˈmaː.að`

### TH-SYL-T2-005: Same-quality epenthesis: לָכֶ֫ם

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** syllable / weight-repair-instance
- **Statement:** A phonetically long vowel in a closed syllable is followed by a same-quality epenthetic.
- **Conditions:** long vowel; following coda consonant
- **Operation:** Split the vowel-plus-coda into CV̄.VC.
- **Result IPA:** lɔː.ˈχɛː.ɛm
- **Source:** T1_2B_corrected_p352.md §I.2.4. Long Vowels in Closed Syllables (lines 687–695)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-SYL-001']
- **Examples:**
  - `לָכֶ֫ם` → `lɔː.ˈχɛː.ɛm`

### TH-SYL-T2-006: Same-quality epenthesis: עֹ֫ז

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** syllable / weight-repair-instance
- **Statement:** A phonetically long vowel in a closed syllable is followed by a same-quality epenthetic.
- **Conditions:** long vowel; following coda consonant
- **Operation:** Split the vowel-plus-coda into CV̄.VC.
- **Result IPA:** ˈʕoː.oz
- **Source:** T1_2B_corrected_p352.md §I.2.4. Long Vowels in Closed Syllables (lines 687–695)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-SYL-001']
- **Examples:**
  - `עֹ֫ז` → `ˈʕoː.oz`

### TH-SYL-T2-007: Same-quality epenthesis: לֵ֫ב

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** syllable / weight-repair-instance
- **Statement:** A phonetically long vowel in a closed syllable is followed by a same-quality epenthetic.
- **Conditions:** long vowel; following coda consonant
- **Operation:** Split the vowel-plus-coda into CV̄.VC.
- **Result IPA:** ˈleː.ev
- **Source:** T1_2B_corrected_p352.md §I.2.4. Long Vowels in Closed Syllables (lines 687–695)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-SYL-001']
- **Examples:**
  - `לֵ֫ב` → `ˈleː.ev`

### TH-SYL-T2-008: Furtive pataḥ as assimilated epenthetic

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** syllable / furtive-pataḥ
- **Statement:** Before a final laryngeal or pharyngeal, the epenthetic after a long vowel shifts to [a] through assimilation.
- **Conditions:** long vowel; word-final guttural
- **Operation:** Insert epenthetic and assimilate its quality to [a].
- **Result IPA:** Vː.aG
- **Source:** T1_2B_corrected_p352.md §I.2.4. Long Vowels in Closed Syllables (lines 661–665)
- **Certainty:** high
- **Examples:**
  - `ר֫וּחַ` → `ˈʀ̟uː.aħ`

### TH-SYL-T2-009: Labial glide before furtive pataḥ

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** syllable / glide
- **Statement:** After [uː] or [oː], the onset before furtive pataḥ is a bilabial glide [w].
- **Conditions:** furtive pataḥ; preceding [uː] or [oː]
- **Operation:** Realize a homorganic [w] glide.
- **Result IPA:** w
- **Source:** T1_2B_corrected_p352.md §I.2.4. Long Vowels in Closed Syllables (lines 775–783)
- **Certainty:** high
- **Examples:**
  - `ר֤וּחַ` → `ˈʀ̟uːwaħ`

### TH-SYL-T2-010: Palatal glide before furtive pataḥ

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** syllable / glide
- **Statement:** After [iː] or [eː], the onset before furtive pataḥ is a palatal glide [j].
- **Conditions:** furtive pataḥ; preceding [iː] or [eː]
- **Operation:** Realize a homorganic [j] glide.
- **Result IPA:** j
- **Source:** T1_2B_corrected_p352.md §I.2.4. Long Vowels in Closed Syllables (lines 779–783)
- **Certainty:** high
- **Examples:**
  - `שִׂיחַ` → `ˈsiːjaħ`

### TH-SYL-T2-011: Vocalic shewa forms iambic foot

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** syllable / metrical-foot
- **Statement:** A vocalic shewa or ḥaṭef syllable is weak and bound to a following strong full-vowel syllable in an iambic foot.
- **Conditions:** vocalic shewa or ḥaṭef; following full-vowel syllable
- **Operation:** Parse as (. *).
- **Result IPA:** (CV.CV̄/CVC)
- **Source:** T1_2B_corrected_p352.md §I.2.5.2. Syllabification and Metrical Structure (lines 1172–1184)
- **Certainty:** high
- **Examples:**
  - `תִּסְפְּר֖וּ` → `(tʰis.) (pʰa.ˈʀ̟uː)` (Lev. 23.16)

### TH-SYL-T2-012: Final cluster extrasyllabicity

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** syllable / word-edge
- **Statement:** The final consonant of a word-final cluster is extrasyllabic; stress lengthens the preceding vowel and same-quality epenthesis splits the closed long syllable.
- **Conditions:** word-final consonant cluster
- **Operation:** Keep final consonant extrasyllabic; derive CVː.VC.C.
- **Result IPA:** CVː.VC.C
- **Source:** T1_2B_corrected_p352.md §I.2.6. Syllabification and Metrical Structure of Word-final Syllables (lines 2934–2942)
- **Certainty:** high
- **Examples:**
  - `וַיֵּ֣בְךְּ` → `vaɟ.ˈɟeː.ev.k` (Gen. 45.15)
  - `לִקַּ֤טְתְּ` → `liq̟.ˈq̟aːatˁ.t` (Ruth 2.19)

### TH-SYL-T2-013: Segolate final epenthesis

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** syllable / segolate
- **Statement:** Segolate nouns have an underlying final extrasyllabic consonant syllabified by a phonetic epenthetic; the first vowel is lengthened.
- **Conditions:** segolate underlying /CVC.C/
- **Operation:** /CVC.C/ → [CVː.CVC].
- **Result IPA:** CVː.CVC
- **Source:** T1_2B_corrected_p352.md §I.2.6. Syllabification and Metrical Structure of Word-final Syllables (lines 2944–2952)
- **Certainty:** high
- **Examples:**
  - `מֶ֫לֶךְ` → `ˈmɛː.lɛχ`
  - `סֵ֫פֶר` → `ˈseː.fɛʀ̟`
  - `קֹ֫דֶשׁ` → `ˈq̟oː.ðɛʃ`

### TH-SYL-T2-014: Medial alef epenthetic reanalysis

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** syllable / lexicalization
- **Statement:** In historical *CVʾC nouns, the cluster-breaking vowel takes stress and is reanalyzed as lexical, while the original first vowel reduces to shewa.
- **Conditions:** historical *CVʾC noun
- **Operation:** Shift stress to epenthetic and lexicalize it; reduce first vowel.
- **Result IPA:** Cə.ˈʔVː.VC
- **Source:** T1_2B_corrected_p352.md §I.2.6. Syllabification and Metrical Structure of Word-final Syllables (lines 2962–2974)
- **Certainty:** high
- **Examples:**
  - `בְּאֵר` → `beˈʔeːeʀ̟`

### TH-SYL-T2-015: Nesiga operates over feet

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** syllable / nesiga
- **Statement:** Nesiga retracts stress no farther than the foot immediately preceding the word-final foot.
- **Conditions:** prosodic phrase licenses nesiga
- **Operation:** Retract stress by foot, not raw phonetic syllable.
- **Result IPA:** ˈFoot ... Foot
- **Source:** T1_2B_corrected_p352.md §I.2.6. Syllabification and Metrical Structure of Word-final Syllables (lines 2990–3016)
- **Certainty:** high
- **Examples:**
  - `נַ֣עַמְדָה יָּ֑חַד` → `ˈnaː.ʕam.ðɔː` (Isa. 50.8)

### TH-SYL-T2-016: Word-internal segolate-pattern extension

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** syllable / proper-name
- **Statement:** Some proper names extend word-final segolate syllabification and a trochaic foot into word-internal position.
- **Conditions:** lexically specified proper-name pattern
- **Operation:** /CVC.C/ → [CVː.CVC] internally.
- **Result IPA:** (CVː.CVC)
- **Source:** T1_2B_corrected_p352.md §I.2.6. Syllabification and Metrical Structure of Word-final Syllables (lines 3024–3034)
- **Certainty:** high
- **Examples:**
  - `בֶּרֶכְיָ֖הוּ` → `bɛː.ʀ̟ɛχˈjɔːhuː` (1 Chron. 2.24)

### TH-SYL-T2-017: Lexical ḥaṭef degenerate foot

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** syllable / metrical-foot
- **Statement:** A lexical lax [ɔ] or [ɛ] in a light open syllable can form a separate degenerate monomoraic foot before a stronger bimoraic syllable.
- **Conditions:** lexical ḥaṭef qameṣ/segol; immediately followed by stronger bimoraic syllable
- **Operation:** Parse CV as its own degenerate foot.
- **Result IPA:** (CV).(CVV/CVC)
- **Source:** T1_2B_corrected_p352.md §I.2.7. Lexical _Ḥaṭef_ Vowels (lines 3094–3120)
- **Certainty:** high
- **Examples:**
  - `צֳרִי֙` → `sˁɔ.ˈʀ̟iː` (Gen. 43.11)

### TH-SYL-T2-018: Metrical zero epenthesis

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** syllable / metrical-epenthesis
- **Statement:** A zero interval functioning as a weak metrical beat separates adjacent secondary and main prominences in weak-consonant contacts.
- **Conditions:** phonetic gaʿya immediately before main-stressed weak onset
- **Operation:** Insert metrical ∅ beat without a segmental vowel.
- **Result IPA:** ˌVˑC∅ˈCV
- **Source:** T1_2B_corrected_p352.md §I.2.10. Metrical Epenthesis (lines 3856–3870)
- **Certainty:** high
- **Examples:**
  - `יְשַֽׁעְיָ֣הוּ` → `ja.ˌʃaˑʕ∅ˈjɔː.huː` (Isa. 1.1)

## stress

### TH-STR-T2-001: Main-stressed long vowels are longest

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** stress / duration
- **Statement:** Long vowels under main stress are longer than long vowels in unstressed open syllables.
- **Conditions:** compare main-stressed and unstressed long vowels
- **Operation:** Assign greater duration under main stress.
- **Result IPA:** V́ː > Vː
- **Source:** T1_2B_corrected_p352.md §I.2.8.1.1. Stressed and Unstressed Vowels (lines 3179–3193)
- **Certainty:** high
- **Examples:** no example in source

### TH-STR-T2-002: Deḥiq compresses final lax long vowel

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** stress / dehiq
- **Statement:** Deḥiq compresses a word-final long lax qameṣ or segol to half-long before an initially stressed following word in a close prosodic bond.
- **Conditions:** first word penultimately stressed with conjunctive or maqqef; final [ɔː] or [ɛː]; following word initial foot stressed
- **Operation:** Compress final vowel.
- **Result IPA:** ɔˑ or ɛˑ
- **Source:** T1_2B_corrected_p352.md §I.2.8.1.2. _Deḥiq_ (lines 3223–3241)
- **Certainty:** high
- **Examples:**
  - `וְאָעִ֣ידָה בָּ֔ם` → `vɔʔɔːˈʕiːðɔˑ ˈbbɔːɔm` (Deut. 31.28)

### TH-STR-T2-003: Deḥiq triggers following gemination

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** stress / dehiq
- **Statement:** The initial consonant of the second word in deḥiq is geminated, compensating for vowel compression and marking the word boundary.
- **Conditions:** deḥiq; following consonant can take dagesh
- **Operation:** Geminate following onset.
- **Result IPA:** Cː
- **Source:** T1_2B_corrected_p352.md §I.2.8.1.2. _Deḥiq_ (lines 3283–3287)
- **Certainty:** high
- **Examples:**
  - `וְאָעִ֣ידָה בָּ֔ם` → `vɔ.ʔɔː.ˈʕiː.ðɔˑ b.ˈbɔː.ɔm` (Deut. 31.28)

### TH-STR-T2-004: Tense vowels resist deḥiq

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** stress / dehiq
- **Statement:** Final unstressed tense shureq and ḥireq generally are not compressed in deḥiq configurations, and the next consonant lacks deḥiq dagesh.
- **Conditions:** deḥiq configuration; final tense [uː] or [iː]
- **Operation:** Preserve full length; do not trigger gemination.
- **Result IPA:** uː or iː
- **Source:** T1_2B_corrected_p352.md §I.2.8.1.2. _Deḥiq_ (lines 3257–3267)
- **Certainty:** high
- **Examples:**
  - `בָחַ֙רְתִּי ב֥וֹ` → `vɔːˈħaːaʀ̟tʰiː ˈvoː` (1 Chron. 28.6)

### TH-STR-T2-005: Gutturals block deḥiq compression

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** stress / dehiq
- **Statement:** Before a following guttural that cannot geminate, deḥiq compression does not occur regardless of vowel quality.
- **Conditions:** deḥiq configuration; following onset guttural
- **Operation:** Preserve final vowel length.
- **Result IPA:** Vː
- **Source:** T1_2B_corrected_p352.md §I.2.8.1.2. _Deḥiq_ (lines 3263–3275)
- **Certainty:** high
- **Examples:** no example in source

### TH-STR-T2-006: Interrogative ma in deḥiq is half-long

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** stress / dehiq
- **Statement:** In the careful Tiberian stream, interrogative מַה before maqqef and geminated onset is compressed but remains half-long.
- **Conditions:** מַה־; deḥiq construction
- **Operation:** Realize pataḥ as [aˑ]; geminate following onset.
- **Result IPA:** maˑ-Cː
- **Source:** T1_2B_corrected_p352.md §I.2.8.1.2. _Deḥiq_ (lines 3331–3347)
- **Certainty:** high
- **Examples:**
  - `מַה־לָּ֣ךְ` → `maˑ ˈllɔːɔχ` (Gen. 21.17)
  - `מַה־זֹּ֑את` → `maˑ ˈzzoːoθ` (Exod. 13.14)

### TH-STR-T2-007: Disjunctive main stress lengthens more

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** stress / accent-duration
- **Statement:** Stressed vowels with disjunctive accents are generally longer than those with conjunctive accents.
- **Conditions:** main-stressed vowel
- **Operation:** Scale duration by accent class.
- **Result IPA:** V́ː(disjunctive) > V́ː(conjunctive)
- **Source:** T1_2B_corrected_p352.md §I.2.8.1.3. The Impact of Musical Accents on Duration (lines 3385–3389)
- **Certainty:** medium
- **Examples:** no example in source

### TH-STR-T2-008: Major gaʿya secondary stress

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** stress / major-gaya
- **Statement:** Major gaʿya marks secondary stress on a long vowel in an open syllable, normally separated from main stress by at least one syllable.
- **Conditions:** open syllable with long vowel; at least one intervening syllable before main stress
- **Operation:** Assign secondary stress and increased duration.
- **Result IPA:** ˌVː
- **Source:** T1_2B_corrected_p352.md §I.2.8.2.1. On Open Syllables with Long Vowels (lines 3409–3421)
- **Certainty:** high
- **Examples:**
  - `הָֽאָדָ֗ם` → `—` (Gen. 2.7)

### TH-STR-T2-009: Secondary stress may be unmarked

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** stress / major-gaya
- **Statement:** A syllable structurally suitable for major gaʿya may bear secondary stress even when gaʿya is not written.
- **Conditions:** structure suitable for major gaʿya
- **Operation:** Infer possible secondary stress independent of notation.
- **Result IPA:** ˌVː
- **Source:** T1_2B_corrected_p352.md §I.2.8.2.1. On Open Syllables with Long Vowels (lines 3481–3497)
- **Certainty:** medium
- **Examples:** no example in source

### TH-STR-T2-010: Minor gaʿya half-lengthens short closed vowel

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** stress / minor-gaya
- **Statement:** Minor gaʿya places secondary stress on a short vowel in a closed syllable and lengthens it only to half-long.
- **Conditions:** closed syllable with vowel unspecified for length; regular minor-gaʿya pattern; usually disjunctive accent
- **Operation:** Assign secondary stress and half-length.
- **Result IPA:** ˌVˑ
- **Source:** T1_2B_corrected_p352.md §I.2.8.2.2. On Closed Syllables with Short Vowels   (lines 3531–3554)
- **Certainty:** high
- **Examples:**
  - `מִֽתְפַּלְפְּלִ֔ים` → `ˌmiˑθpʰalpʰaˈliːim`
  - `וַֽיִּשְׁמְע֡וּ` → `ˌvaˑɟɟiʃmuˈʕuː` (Exod. 4.31)

### TH-STR-T2-011: Regular minor-gaʿya patterns

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** stress / minor-gaya
- **Statement:** Minor gaʿya is most consistent in מִתְפַּלְפְּלִים, מִתְקַטְּלִים, and מִתְפַּעֲלִים type patterns with a minimal light buffer before main stress.
- **Conditions:** one of the three regular structural patterns
- **Operation:** License minor gaʿya on the first closed syllable.
- **Result IPA:** ˌVˑ
- **Source:** T1_2B_corrected_p352.md §I.2.8.2.2. On Closed Syllables with Short Vowels   (lines 3531–3544)
- **Certainty:** high
- **Examples:** no example in source

### TH-STR-T2-012: Minor gaʿya crosses maqqef

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** stress / minor-gaya
- **Statement:** Minor gaʿya may apply across a maqqef boundary when the combined accent group has the required structure.
- **Conditions:** words joined by maqqef; minor-gaʿya structural pattern spans boundary
- **Operation:** Assign half-long secondary stress across the group.
- **Result IPA:** ˌVˑ
- **Source:** T1_2B_corrected_p352.md §I.2.8.2.2. On Closed Syllables with Short Vowels   (lines 3566–3576)
- **Certainty:** high
- **Examples:**
  - `עַֽל־הַחֲמֹ֔ר` → `—` (Exod. 4.20)

### TH-STR-T2-013: Shewa gaʿya lengthens vocalic shewa

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** stress / shewa-gaya
- **Statement:** Gaʿya on vocalic shewa or ḥaṭef phonetically lengthens it while it remains metrically subordinate to the following syllable.
- **Conditions:** vocalic shewa or ḥaṭef bears gaʿya
- **Operation:** Add secondary prominence and phonetic duration without creating an independent foot.
- **Result IPA:** ˌVˑ
- **Source:** T1_2B_corrected_p352.md §I.2.9. _Shewa Gaʿya_ (lines 3638–3648)
- **Certainty:** high
- **Examples:**
  - `תְּֽשַׁלְּח֡וּ` → `—` (Jer. 34.14)
  - `בְּֽמַעֲלֵה֘` → `—` (2 Chron. 32.33)

### TH-STR-T2-014: Shewa gaʿya conditioned quality

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** stress / shewa-gaya
- **Statement:** The quality of shewa gaʿya follows ordinary shewa quality rules: [a] by default, [i] before yod, and the adjacent guttural vowel quality before gutturals.
- **Conditions:** shewa gaʿya
- **Operation:** Assign quality first, then half-lengthen.
- **Result IPA:** aˑ iˑ eˑ oˑ uˑ
- **Source:** T1_2B_corrected_p352.md §I.2.9. _Shewa Gaʿya_ (lines 3684–3712)
- **Certainty:** high
- **Examples:**
  - `וְֽיַ֫עֲבֹ֥דוּ` → `ˌviˑjaːʕaˈvoːðuː` (Job 36.11)
  - `וְֽאוּלָ֗ם` → `ˌwuˑʔuːˈlɔːɔm` (Job 12.7)

### TH-STR-T2-015: Shewa gaʿya remains monomoraic

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** stress / shewa-gaya
- **Statement:** Despite phonetic stretching, shewa gaʿya remains underlyingly monomoraic and does not attain full bimoraic vowel status.
- **Conditions:** shewa gaʿya
- **Operation:** Preserve iambic foot membership and monomoraic status.
- **Result IPA:** ˌVˑ, not /V̄/
- **Source:** T1_2B_corrected_p352.md §I.2.9. _Shewa Gaʿya_ (lines 3720–3750)
- **Certainty:** high
- **Examples:** no example in source

### TH-STR-T2-016: Weak-contact phonetic gaʿya is half-long

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** stress / metrical-epenthesis
- **Statement:** Before a weak coda-plus-weak onset contact immediately preceding main stress, phonetic gaʿya half-lengthens the short vowel.
- **Conditions:** short vowel in closed syllable; weak coda and weak following onset; adjacent main stress
- **Operation:** Half-lengthen vowel and assign secondary prominence.
- **Result IPA:** ˌVˑ
- **Source:** T1_2B_corrected_p352.md §I.2.10. Metrical Epenthesis (lines 3758–3788)
- **Certainty:** high
- **Examples:**
  - `יְשַֽׁעְיָ֣הוּ` → `ja.ˌʃaˑʕ.ˈjɔː.huː` (Isa. 1.1)
  - `שְׁמַֽע־נָ֤א` → `ʃa.ˌmaˑʕ.-ˈnɔː` (1 Sam. 28.22)

### TH-STR-T2-017: Weak-contact gaʿya keeps shewa silent

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** stress / metrical-epenthesis
- **Statement:** In half-long weak-contact phonetic gaʿya, a following written shewa remains silent; this contrasts with mora-augmenting gaʿya that makes shewa vocalic.
- **Conditions:** weak-contact half-long phonetic gaʿya
- **Operation:** Keep shewa zero and use metrical epenthesis.
- **Result IPA:** VˑC∅
- **Source:** T1_2B_corrected_p352.md §I.2.10. Metrical Epenthesis (lines 3844–3856)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-SHEWA-019']
- **Examples:** no example in source

### TH-STR-T2-018: Haya and ḥaya prefix lengthening

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** stress / metrical-epenthesis
- **Statement:** Prefixes of היה and חיה are lengthened before weak guttural-plus-yod contacts as an orthoepic metrical-epenthesis strategy.
- **Conditions:** prefix of היה or חיה; weak guttural followed by yod
- **Operation:** Half-lengthen prefix vowel; retain silent shewa.
- **Result IPA:** iˑh/ħj or aˑjh
- **Source:** T1_2B_corrected_p352.md §I.2.10. Metrical Epenthesis (lines 3892–3920)
- **Certainty:** high
- **Examples:**
  - `יִֽהְיֶ֖ה` → `ˌjiˑhˈjɛː` (Gen. 1.29)
  - `וַֽיְחִ֣י` → `ˌvaˑjˈħiː` (Gen. 5.3)

### TH-STR-T2-019: Metiga does not lengthen

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** stress / metiga
- **Statement:** Metiga on a closed short-vowel syllable before zaqef does not lengthen the vowel and is not a secondary stress beat.
- **Conditions:** metiga before zaqef; closed syllable with short vowel
- **Operation:** Preserve short vowel.
- **Result IPA:** V
- **Source:** T1_2B_corrected_p352.md §I.2.12. Further Cases of Second Accents in a Word on Closed Syllables with Short Vowels (lines 4146–4174)
- **Certainty:** high
- **Examples:**
  - `וּמִ֨קְצָתָ֔ם` → `—` (Dan. 1.5)

### TH-STR-T2-020: First element of composite accent does not lengthen

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** stress / composite-accent
- **Statement:** The first accent of a composite accent in the three books does not lengthen a short vowel and does not represent secondary stress.
- **Conditions:** first element of composite accent; closed syllable with short vowel; three books
- **Operation:** Preserve short vowel.
- **Result IPA:** V
- **Source:** T1_2B_corrected_p352.md §I.2.12. Further Cases of Second Accents in a Word on Closed Syllables with Short Vowels (lines 4170–4174)
- **Certainty:** high
- **Examples:**
  - `מִ֜שְׁלַ֗חַת` → `—` (Psa. 78.49)

## maqqef

### TH-MAQ-T2-001: Maqqef creates one stress group

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** maqqef / prosodic-group
- **Statement:** Maqqef joins two to four words into one group with a single main stress.
- **Conditions:** words joined by maqqef
- **Operation:** Assign one main stress to the group.
- **Result IPA:** ω-ω ... ˈω
- **Source:** T1_2B_corrected_p352.md §I.2.11. _Maqqef_ (lines 3974–3984)
- **Certainty:** high
- **Examples:**
  - `אֶת־הָא֖וֹר` → `—` (Gen. 1.4)

### TH-MAQ-T2-002: Maqqef removes first-word stress

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** maqqef / stress-deletion
- **Statement:** A word before maqqef normally loses its main stress.
- **Conditions:** word followed by maqqef
- **Operation:** Delete its independent main stress.
- **Result IPA:** unstressed
- **Source:** T1_2B_corrected_p352.md §I.2.11. _Maqqef_ (lines 3986–4008)
- **Certainty:** high
- **Examples:** no example in source

### TH-MAQ-T2-003: Maqqef shortens unspecified vowels

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** maqqef / vowel-shortening
- **Statement:** When maqqef removes stress, vowels without inherent length become short.
- **Conditions:** pre-maqqef word; vowel unspecified for length; vowel would otherwise be lengthened by stress
- **Operation:** Remove stress-conditioned length and apply unstressed closed-syllable quality.
- **Result IPA:** V
- **Source:** T1_2B_corrected_p352.md §I.2.11. _Maqqef_ (lines 4008–4018)
- **Certainty:** high
- **Examples:**
  - `כָּל־` → `kʰɔl`
  - `עָז־` → `ʕɔz` (Isa. 26.1)
  - `אֶת־` → `ʔɛθ`

### TH-MAQ-T2-004: Maqqef /e/ surfaces [ɛ]

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** maqqef / quality
- **Statement:** Underlying short /e/ in a monosyllable before maqqef surfaces as [ɛ].
- **Conditions:** underlying /e/; stress removed by maqqef
- **Operation:** /e/ → [ɛ].
- **Result IPA:** ɛ
- **Source:** T1_2B_corrected_p352.md §I.2.11. _Maqqef_ (lines 4014–4018)
- **Certainty:** high
- **Examples:**
  - `אֶת־` → `ʔɛθ`
  - `וַיִּתֶּן־` → `vaɟɟittʰɛn`

### TH-MAQ-T2-005: Maqqef /o/ surfaces [ɔ]

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** maqqef / quality
- **Statement:** Underlying short /o/ in a monosyllable before maqqef surfaces as [ɔ].
- **Conditions:** underlying /o/; stress removed by maqqef
- **Operation:** /o/ → [ɔ].
- **Result IPA:** ɔ
- **Source:** T1_2B_corrected_p352.md §I.2.11. _Maqqef_ (lines 4008–4014)
- **Certainty:** high
- **Examples:**
  - `כָּל־` → `kʰɔl`
  - `תִּמְשָׁל־` → `tʰimʃɔl` (Gen. 4.7)

### TH-MAQ-T2-006: Inherent length resists maqqef

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** maqqef / inherent-length
- **Statement:** Vowels with an inherent length feature do not in principle shorten before maqqef.
- **Conditions:** pre-maqqef vowel has specified length
- **Operation:** Preserve Vː.
- **Result IPA:** Vː
- **Source:** T1_2B_corrected_p352.md §I.2.11. _Maqqef_ (lines 4020–4026)
- **Certainty:** high
- **Examples:**
  - `בֵּית־אָבִ֛יךְ` → `beːeθ` (Gen. 24.23)
  - `אִישׁ־אֶחָ֖ד` → `ʔiːiʃ` (Gen. 42.11)

### TH-MAQ-T2-007: Secondary stress preserves pre-maqqef /o/

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** maqqef / secondary-stress
- **Statement:** A pre-maqqef underlying /o/ may retain long [oː] under secondary stress rather than shorten to [ɔ].
- **Conditions:** underlying /o/; pre-maqqef secondary stress
- **Operation:** /o/ → [oː].
- **Result IPA:** oː
- **Source:** T1_2B_corrected_p352.md §I.2.11. _Maqqef_ (lines 4046–4054)
- **Certainty:** high
- **Examples:**
  - `יִגְנֹֽב־אִישׁ֙` → `—` (Exod. 21.37)
  - `עֹֽז־לָ֑מוֹ` → `—` (Psa. 28.8)

### TH-MAQ-T2-008: Compound numeral secondary stress

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** maqqef / compound-numeral
- **Statement:** Compound numerals joined by maqqef generally preserve secondary stress on the first element.
- **Conditions:** compound numeral; elements joined by maqqef
- **Operation:** Assign secondary stress to first element.
- **Result IPA:** ˌV(ː/ˑ)
- **Source:** T1_2B_corrected_p352.md §I.2.11. _Maqqef_ (lines 4056–4062)
- **Certainty:** high
- **Examples:**
  - `אַרְבַּֽע־עֶשְׂרֵ֤ה` → `—` (Gen. 14.4)

### TH-MAQ-T2-009: Distant main stress preserves /e o/

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** maqqef / secondary-stress
- **Statement:** Monosyllables with /e/ or /o/ before maqqef have long [eː]/[oː] when separated from the group's main stress by at least one intervening syllable.
- **Conditions:** pre-maqqef monosyllable with /e/ or /o/; at least one intervening syllable before main stress
- **Operation:** Assign secondary stress and long tense realization.
- **Result IPA:** eː or oː
- **Source:** T1_2B_corrected_p352.md §I.2.11. _Maqqef_ (lines 4064–4074)
- **Certainty:** high
- **Examples:**
  - `שֵׁשׁ־הַשְּׂעֹרִ֥ים` → `—` (Ruth 3.17)
  - `בֵּן־פָּרִ֖יץ` → `—` (Ezek. 18.10)

### TH-MAQ-T2-010: Metrical epenthesis across maqqef

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** maqqef / metrical-epenthesis
- **Statement:** When a pre-maqqef final open syllable bears secondary stress immediately before initial main stress, a metrical zero interval prevents stress clash.
- **Conditions:** pre-maqqef open syllable with gaʿya; following word initially stressed
- **Operation:** Insert metrical ∅ interval.
- **Result IPA:** ˌCVː∅ˈCV
- **Source:** T1_2B_corrected_p352.md §I.2.11. _Maqqef_ (lines 4110–4120)
- **Certainty:** high
- **Examples:**
  - `כִּֽי־אֵ֛שׁ` → `—` (Jer. 17.4)

## samples

### TH-ORTH-SAMPLE-GEN-01-T4: Genesis 1:1 dual-stream sample

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** samples / dual-stream
- **Statement:** Canonical sample transcription of Genesis 1:1 in both standard streams.
- **Conditions:** Reciting Genesis 1:1.; Choose the configured standard stream.
- **Operation:** Use the corresponding source transcription without phonetic normalization.
- **Result IPA:** {'forte-lene': 'baʀ̟eːˈʃiːiθ bɔːˈʀ̟ɔː ʔɛloːˈhiːim ˈʔeːeθ haʃʃɔːˈmaːjim veˈʔeːeθ hɔːˈʔɔːʀ̟ɛsˁ', 'extended-forte': 'bbaʀ̟eːˈʃiːiθ bbɔːˈʀ̟ɔː ʔɛloːˈhiːim ˈʔeːeθ haʃʃɔːˈmaːjim veˈʔeːeθ hɔːˈʔɔːʀ̟ɛsˁ'}
- **Source:** T1_4B_5_Ref.md §I.5.4.1 (lines 346–350)
- **Certainty:** high
- **Notes:** When the source prints only one reading because both streams coincide, the identical source IPA is assigned to both stream labels. | Dropped unresolved related_ids: ['TH-VAR-001', 'TH-VAR-002']
- **Examples:**
  - `בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָֽרֶץ׃` → `baʀ̟eːˈʃiːiθ bɔːˈʀ̟ɔː ʔɛloːˈhiːim ˈʔeːeθ haʃʃɔːˈmaːjim veˈʔeːeθ hɔːˈʔɔːʀ̟ɛsˁ` (Genesis 1:1) [forte-lene]
  - `בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָֽרֶץ׃` → `bbaʀ̟eːˈʃiːiθ bbɔːˈʀ̟ɔː ʔɛloːˈhiːim ˈʔeːeθ haʃʃɔːˈmaːjim veˈʔeːeθ hɔːˈʔɔːʀ̟ɛsˁ` (Genesis 1:1) [extended-forte]

### TH-ORTH-SAMPLE-GEN-02-T4: Genesis 1:2 dual-stream sample

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** samples / dual-stream
- **Statement:** Canonical sample transcription of Genesis 1:2 in both standard streams.
- **Conditions:** Reciting Genesis 1:2.; Choose the configured standard stream.
- **Operation:** Use the corresponding source transcription without phonetic normalization.
- **Result IPA:** {'forte-lene': 'vɔhɔːˈʔɔːʀ̟ɛsˁ hɔːɔjˈθɔː ˈθoːhuː vɔːˈvoːhuː voˈħoːʃɛχ ʕal-pʰaˈneː θoˈhoːom vaˈʀ̟uːwaħ ʔɛloːˈhiːim maʀ̟aːˈħɛːfɛθ ʕal-pʰaˈneː hamˈmɔːjim', 'extended-forte': 'vɔhɔːˈʔɔːʀ̟ɛsˁ hɔːɔjˈθɔː ˈθoːhuː vɔːˈvoːhuː voˈħoːʃɛχ ʕal-ppʰaˈneː θoˈhoːom vaˈʀ̟uːwaħ ʔɛloːˈhiːim maʀ̟aːˈħɛːfɛθ ʕal-ppʰaˈneː hamˈmɔːjim'}
- **Source:** T1_4B_5_Ref.md §I.5.4.1 (lines 352–356)
- **Certainty:** high
- **Notes:** When the source prints only one reading because both streams coincide, the identical source IPA is assigned to both stream labels. | Dropped unresolved related_ids: ['TH-VAR-001', 'TH-VAR-002']
- **Examples:**
  - `וְהָאָ֗רֶץ הָיְתָ֥ה תֹ֙הוּ֙ וָבֹ֔הוּ וְחֹ֖שֶׁךְ עַל־פְּנֵ֣י תְה֑וֹם וְר֣וּחַ אֱלֹהִ֔ים מְרַחֶ֖פֶת עַל־פְּנֵ֥י הַמָּֽיִם׃` → `vɔhɔːˈʔɔːʀ̟ɛsˁ hɔːɔjˈθɔː ˈθoːhuː vɔːˈvoːhuː voˈħoːʃɛχ ʕal-pʰaˈneː θoˈhoːom vaˈʀ̟uːwaħ ʔɛloːˈhiːim maʀ̟aːˈħɛːfɛθ ʕal-pʰaˈneː hamˈmɔːjim` (Genesis 1:2) [forte-lene]
  - `וְהָאָ֗רֶץ הָיְתָ֥ה תֹ֙הוּ֙ וָבֹ֔הוּ וְחֹ֖שֶׁךְ עַל־פְּנֵ֣י תְה֑וֹם וְר֣וּחַ אֱלֹהִ֔ים מְרַחֶ֖פֶת עַל־פְּנֵ֥י הַמָּֽיִם׃` → `vɔhɔːˈʔɔːʀ̟ɛsˁ hɔːɔjˈθɔː ˈθoːhuː vɔːˈvoːhuː voˈħoːʃɛχ ʕal-ppʰaˈneː θoˈhoːom vaˈʀ̟uːwaħ ʔɛloːˈhiːim maʀ̟aːˈħɛːfɛθ ʕal-ppʰaˈneː hamˈmɔːjim` (Genesis 1:2) [extended-forte]

### TH-ORTH-SAMPLE-GEN-03-T4: Genesis 1:3 dual-stream sample

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** samples / dual-stream
- **Statement:** Canonical sample transcription of Genesis 1:3 in both standard streams.
- **Conditions:** Reciting Genesis 1:3.; Choose the configured standard stream.
- **Operation:** Use the corresponding source transcription without phonetic normalization.
- **Result IPA:** {'forte-lene': 'vaɟˈɟoːmɛʀ̟ ʔɛloːˈhiːim jiˈhiː ˈʔoːoʀ̟ ˌvaˑjhiː-ˈʔoːoʀ̟', 'extended-forte': 'vaɟˈɟoːmɛʀ̟ ʔɛloːˈhiːim jiˈhiː ˈʔoːoʀ̟ ˌvaˑjhiː-ˈʔoːoʀ̟'}
- **Source:** T1_4B_5_Ref.md §I.5.4.1 (lines 358–360)
- **Certainty:** high
- **Notes:** When the source prints only one reading because both streams coincide, the identical source IPA is assigned to both stream labels. | Dropped unresolved related_ids: ['TH-VAR-001', 'TH-VAR-002']
- **Examples:**
  - `וַיֹּ֥אמֶר אֱלֹהִ֖ים יְהִ֣י א֑וֹר וַֽיְהִי־אֽוֹר׃` → `vaɟˈɟoːmɛʀ̟ ʔɛloːˈhiːim jiˈhiː ˈʔoːoʀ̟ ˌvaˑjhiː-ˈʔoːoʀ̟` (Genesis 1:3) [forte-lene]
  - `וַיֹּ֥אמֶר אֱלֹהִ֖ים יְהִ֣י א֑וֹר וַֽיְהִי־אֽוֹר׃` → `vaɟˈɟoːmɛʀ̟ ʔɛloːˈhiːim jiˈhiː ˈʔoːoʀ̟ ˌvaˑjhiː-ˈʔoːoʀ̟` (Genesis 1:3) [extended-forte]

### TH-ORTH-SAMPLE-GEN-04-T4: Genesis 1:4 dual-stream sample

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** samples / dual-stream
- **Statement:** Canonical sample transcription of Genesis 1:4 in both standard streams.
- **Conditions:** Reciting Genesis 1:4.; Choose the configured standard stream.
- **Operation:** Use the corresponding source transcription without phonetic normalization.
- **Result IPA:** {'forte-lene': 'vaɟˈɟaːaʀ̟ ʔɛloːˈhiːim ʔɛθ-hɔːˈʔoːoʀ̟ kʰiː-ˈtˁoːov vaɟɟavˈdeːel ʔɛloːˈhiːim beːen hɔːˈʔoːoʀ̟ wuˈveːen haːˈħoːʃɛχ', 'extended-forte': 'vaɟˈɟaːaʀ̟ ʔɛloːˈhiːim ʔɛθ-hɔːˈʔoːoʀ̟ kkʰiː-ˈtˁoːov vaɟɟavˈddeːel ʔɛloːˈhiːim bbeːen hɔːˈʔoːoʀ̟ wuˈveːen haːˈħoːʃɛχ'}
- **Source:** T1_4B_5_Ref.md §I.5.4.1 (lines 362–366)
- **Certainty:** high
- **Notes:** When the source prints only one reading because both streams coincide, the identical source IPA is assigned to both stream labels. | Dropped unresolved related_ids: ['TH-VAR-001', 'TH-VAR-002']
- **Examples:**
  - `וַיַּ֧רְא אֱלֹהִ֛ים אֶת־הָא֖וֹר כִּי־ט֑וֹב וַיַּבְדֵּ֣ל אֱלֹהִ֔ים בֵּ֥ין הָא֖וֹר וּבֵ֥ין הַחֹֽשֶׁךְ׃` → `vaɟˈɟaːaʀ̟ ʔɛloːˈhiːim ʔɛθ-hɔːˈʔoːoʀ̟ kʰiː-ˈtˁoːov vaɟɟavˈdeːel ʔɛloːˈhiːim beːen hɔːˈʔoːoʀ̟ wuˈveːen haːˈħoːʃɛχ` (Genesis 1:4) [forte-lene]
  - `וַיַּ֧רְא אֱלֹהִ֛ים אֶת־הָא֖וֹר כִּי־ט֑וֹב וַיַּבְדֵּ֣ל אֱלֹהִ֔ים בֵּ֥ין הָא֖וֹר וּבֵ֥ין הַחֹֽשֶׁךְ׃` → `vaɟˈɟaːaʀ̟ ʔɛloːˈhiːim ʔɛθ-hɔːˈʔoːoʀ̟ kkʰiː-ˈtˁoːov vaɟɟavˈddeːel ʔɛloːˈhiːim bbeːen hɔːˈʔoːoʀ̟ wuˈveːen haːˈħoːʃɛχ` (Genesis 1:4) [extended-forte]

### TH-ORTH-SAMPLE-GEN-05-T4: Genesis 1:5 dual-stream sample

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** samples / dual-stream
- **Statement:** Canonical sample transcription of Genesis 1:5 in both standard streams.
- **Conditions:** Reciting Genesis 1:5.; Choose the configured standard stream.
- **Operation:** Use the corresponding source transcription without phonetic normalization.
- **Result IPA:** {'forte-lene': 'vaɟɟiq̟ˈʀ̟ɔː ʔɛloːˈhiːim lɔːˈʔoːoʀ̟ ˈjoːom valaːˈħoːʃɛχ ˈq̟ɔːʀ̟ɔː ˈlɔːɔjlɔː ˌvaˑjhiː-ˈʕɛːʀ̟ɛv ˌvaˑjhiː-ˈvoːq̟ɛʀ̟ ˈjoːom ʔɛːˈħɔːɔð', 'extended-forte': 'vaɟɟiq̟ˈʀ̟ɔː ʔɛloːˈhiːim lɔːˈʔoːoʀ̟ ˈjoːom valaːˈħoːʃɛχ ˈq̟ɔːʀ̟ɔː ˈlɔːɔjlɔː ˌvaˑjhiː-ˈʕɛːʀ̟ɛv ˌvaˑjhiː-ˈvoːq̟ɛʀ̟ ˈjoːom ʔɛːˈħɔːɔð'}
- **Source:** T1_4B_5_Ref.md §I.5.4.1 (lines 368–370)
- **Certainty:** high
- **Notes:** When the source prints only one reading because both streams coincide, the identical source IPA is assigned to both stream labels. | Dropped unresolved related_ids: ['TH-VAR-001', 'TH-VAR-002']
- **Examples:**
  - `וַיִּקְרָ֨א אֱלֹהִ֤ים ׀ לָאוֹר֙ י֔וֹם וְלַחֹ֖שֶׁךְ קָ֣רָא לָ֑יְלָה וַֽיְהִי־עֶ֥רֶב וַֽיְהִי־בֹ֖קֶר י֥וֹם אֶחָֽד׃` → `vaɟɟiq̟ˈʀ̟ɔː ʔɛloːˈhiːim lɔːˈʔoːoʀ̟ ˈjoːom valaːˈħoːʃɛχ ˈq̟ɔːʀ̟ɔː ˈlɔːɔjlɔː ˌvaˑjhiː-ˈʕɛːʀ̟ɛv ˌvaˑjhiː-ˈvoːq̟ɛʀ̟ ˈjoːom ʔɛːˈħɔːɔð` (Genesis 1:5) [forte-lene]
  - `וַיִּקְרָ֨א אֱלֹהִ֤ים ׀ לָאוֹר֙ י֔וֹם וְלַחֹ֖שֶׁךְ קָ֣רָא לָ֑יְלָה וַֽיְהִי־עֶ֥רֶב וַֽיְהִי־בֹ֖קֶר י֥וֹם אֶחָֽד׃` → `vaɟɟiq̟ˈʀ̟ɔː ʔɛloːˈhiːim lɔːˈʔoːoʀ̟ ˈjoːom valaːˈħoːʃɛχ ˈq̟ɔːʀ̟ɔː ˈlɔːɔjlɔː ˌvaˑjhiː-ˈʕɛːʀ̟ɛv ˌvaˑjhiː-ˈvoːq̟ɛʀ̟ ˈjoːom ʔɛːˈħɔːɔð` (Genesis 1:5) [extended-forte]

### TH-ORTH-SAMPLE-GEN-06-T4: Genesis 1:6 dual-stream sample

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** samples / dual-stream
- **Statement:** Canonical sample transcription of Genesis 1:6 in both standard streams.
- **Conditions:** Reciting Genesis 1:6.; Choose the configured standard stream.
- **Operation:** Use the corresponding source transcription without phonetic normalization.
- **Result IPA:** {'forte-lene': 'vaɟˈɟoːmɛʀ̟ ʔɛloːˈhiːim jiˈhiː ʀ̟ɔːˈq̟iːjaʕ baˈθoːoχ hamˈmɔːjim viːˈhiː mavˈdiːil ˈbeːen ˈmaːjim lɔːˈmɔːjim', 'extended-forte': 'vaɟˈɟoːmɛʀ̟ ʔɛloːˈhiːim jiˈhiː ʀ̟ɔːˈq̟iːjaʕ bbaˈθoːoχ hamˈmɔːjim viːˈhiː mavˈddiːil ˈbbeːen ˈmaːjim lɔːˈmɔːjim'}
- **Source:** T1_4B_5_Ref.md §I.5.4.1 (lines 372–376)
- **Certainty:** high
- **Notes:** When the source prints only one reading because both streams coincide, the identical source IPA is assigned to both stream labels. | Dropped unresolved related_ids: ['TH-VAR-001', 'TH-VAR-002']
- **Examples:**
  - `וַיֹּ֣אמֶר אֱלֹהִ֔ים יְהִ֥י רָקִ֖יעַ בְּת֣וֹךְ הַמָּ֑יִם וִיהִ֣י מַבְדִּ֔יל בֵּ֥ין מַ֖יִם לָמָֽיִם׃` → `vaɟˈɟoːmɛʀ̟ ʔɛloːˈhiːim jiˈhiː ʀ̟ɔːˈq̟iːjaʕ baˈθoːoχ hamˈmɔːjim viːˈhiː mavˈdiːil ˈbeːen ˈmaːjim lɔːˈmɔːjim` (Genesis 1:6) [forte-lene]
  - `וַיֹּ֣אמֶר אֱלֹהִ֔ים יְהִ֥י רָקִ֖יעַ בְּת֣וֹךְ הַמָּ֑יִם וִיהִ֣י מַבְדִּ֔יל בֵּ֥ין מַ֖יִם לָמָֽיִם׃` → `vaɟˈɟoːmɛʀ̟ ʔɛloːˈhiːim jiˈhiː ʀ̟ɔːˈq̟iːjaʕ bbaˈθoːoχ hamˈmɔːjim viːˈhiː mavˈddiːil ˈbbeːen ˈmaːjim lɔːˈmɔːjim` (Genesis 1:6) [extended-forte]

### TH-ORTH-SAMPLE-GEN-07-T4: Genesis 1:7 dual-stream sample

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** samples / dual-stream
- **Statement:** Canonical sample transcription of Genesis 1:7 in both standard streams.
- **Conditions:** Reciting Genesis 1:7.; Choose the configured standard stream.
- **Operation:** Use the corresponding source transcription without phonetic normalization.
- **Result IPA:** {'forte-lene': 'vaɟˈɟaːʕas ʔɛloːˈhiːim ʔɛθ-hɔːʀ̟ɔːˈq̟iːjaʕ vaɟɟavˈdeːel beːen hamˈmaːjim ʔaˈʃɛːɛʀ̟ mitˈtʰaːħaθ lɔːʀ̟ɔːˈq̟iːjaʕ wuˈveːen hamˈmaːjim ʔaˈʃɛːɛʀ̟ meːˈʕaːal lɔːʀ̟ɔːˈq̟iːjaʕ ˌvaˑjhiː-ˈχeːen', 'extended-forte': 'vaɟˈɟaːʕas ʔɛloːˈhiːim ʔɛθ-hɔːʀ̟ɔːˈq̟iːjaʕ vaɟɟavˈddeːel bbeːen hamˈmaːjim ʔaˈʃɛːɛʀ̟ mitˈtʰaːħaθ lɔːʀ̟ɔːˈq̟iːjaʕ wuˈveːen hamˈmaːjim ʔaˈʃɛːɛʀ̟ meːˈʕaːal lɔːʀ̟ɔːˈq̟iːjaʕ ˌvaˑjhiː-ˈχeːen'}
- **Source:** T1_4B_5_Ref.md §I.5.4.1 (lines 378–382)
- **Certainty:** high
- **Notes:** When the source prints only one reading because both streams coincide, the identical source IPA is assigned to both stream labels. | Dropped unresolved related_ids: ['TH-VAR-001', 'TH-VAR-002']
- **Examples:**
  - `וַיַּ֣עַשׂ אֱלֹהִים֮ אֶת־הָרָקִיעַ֒ וַיַּבְדֵּ֗ל בֵּ֤ין הַמַּ֙יִם֙ אֲשֶׁר֙ מִתַּ֣חַת לָרָקִ֔יעַ וּבֵ֣ין הַמַּ֔יִם אֲשֶׁ֖ר מֵעַ֣ל לָרָקִ֑יעַ וַֽיְהִי־כֵֽן׃` → `vaɟˈɟaːʕas ʔɛloːˈhiːim ʔɛθ-hɔːʀ̟ɔːˈq̟iːjaʕ vaɟɟavˈdeːel beːen hamˈmaːjim ʔaˈʃɛːɛʀ̟ mitˈtʰaːħaθ lɔːʀ̟ɔːˈq̟iːjaʕ wuˈveːen hamˈmaːjim ʔaˈʃɛːɛʀ̟ meːˈʕaːal lɔːʀ̟ɔːˈq̟iːjaʕ ˌvaˑjhiː-ˈχeːen` (Genesis 1:7) [forte-lene]
  - `וַיַּ֣עַשׂ אֱלֹהִים֮ אֶת־הָרָקִיעַ֒ וַיַּבְדֵּ֗ל בֵּ֤ין הַמַּ֙יִם֙ אֲשֶׁר֙ מִתַּ֣חַת לָרָקִ֔יעַ וּבֵ֣ין הַמַּ֔יִם אֲשֶׁ֖ר מֵעַ֣ל לָרָקִ֑יעַ וַֽיְהִי־כֵֽן׃` → `vaɟˈɟaːʕas ʔɛloːˈhiːim ʔɛθ-hɔːʀ̟ɔːˈq̟iːjaʕ vaɟɟavˈddeːel bbeːen hamˈmaːjim ʔaˈʃɛːɛʀ̟ mitˈtʰaːħaθ lɔːʀ̟ɔːˈq̟iːjaʕ wuˈveːen hamˈmaːjim ʔaˈʃɛːɛʀ̟ meːˈʕaːal lɔːʀ̟ɔːˈq̟iːjaʕ ˌvaˑjhiː-ˈχeːen` (Genesis 1:7) [extended-forte]

### TH-ORTH-SAMPLE-GEN-08-T4: Genesis 1:8 dual-stream sample

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** samples / dual-stream
- **Statement:** Canonical sample transcription of Genesis 1:8 in both standard streams.
- **Conditions:** Reciting Genesis 1:8.; Choose the configured standard stream.
- **Operation:** Use the corresponding source transcription without phonetic normalization.
- **Result IPA:** {'forte-lene': 'vaɟɟiq̟ˈʀ̟ɔː ʔɛloːˈhiːim ˌlɔːʀ̟ɔːˈq̟iːjaʕ ʃɔːˈmɔːjim ˌvaˑjhiː-ˈʕɛːʀ̟ev ˌvaˑjhiː-ˈvoːq̟ɛʀ̟ ˈjoːom ʃeːˈniː', 'extended-forte': 'vaɟɟiq̟ˈʀ̟ɔː ʔɛloːˈhiːim ˌlɔːʀ̟ɔːˈq̟iːjaʕ ʃɔːˈmɔːjim ˌvaˑjhiː-ˈʕɛːʀ̟ev ˌvaˑjhiː-ˈvoːq̟ɛʀ̟ ˈjoːom ʃeːˈniː'}
- **Source:** T1_4B_5_Ref.md §I.5.4.1 (lines 384–386)
- **Certainty:** high
- **Notes:** When the source prints only one reading because both streams coincide, the identical source IPA is assigned to both stream labels. | Dropped unresolved related_ids: ['TH-VAR-001', 'TH-VAR-002']
- **Examples:**
  - `וַיִּקְרָ֧א אֱלֹהִ֛ים לָֽרָקִ֖יעַ שָׁמָ֑יִם וַֽיְהִי־עֶ֥רֶב וַֽיְהִי־בֹ֖קֶר י֥וֹם שֵׁנִֽי` → `vaɟɟiq̟ˈʀ̟ɔː ʔɛloːˈhiːim ˌlɔːʀ̟ɔːˈq̟iːjaʕ ʃɔːˈmɔːjim ˌvaˑjhiː-ˈʕɛːʀ̟ev ˌvaˑjhiː-ˈvoːq̟ɛʀ̟ ˈjoːom ʃeːˈniː` (Genesis 1:8) [forte-lene]
  - `וַיִּקְרָ֧א אֱלֹהִ֛ים לָֽרָקִ֖יעַ שָׁמָ֑יִם וַֽיְהִי־עֶ֥רֶב וַֽיְהִי־בֹ֖קֶר י֥וֹם שֵׁנִֽי` → `vaɟɟiq̟ˈʀ̟ɔː ʔɛloːˈhiːim ˌlɔːʀ̟ɔːˈq̟iːjaʕ ʃɔːˈmɔːjim ˌvaˑjhiː-ˈʕɛːʀ̟ev ˌvaˑjhiː-ˈvoːq̟ɛʀ̟ ˈjoːom ʃeːˈniː` (Genesis 1:8) [extended-forte]

### TH-ORTH-SAMPLE-GEN-09-T4: Genesis 1:9 dual-stream sample

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** samples / dual-stream
- **Statement:** Canonical sample transcription of Genesis 1:9 in both standard streams.
- **Conditions:** Reciting Genesis 1:9.; Choose the configured standard stream.
- **Operation:** Use the corresponding source transcription without phonetic normalization.
- **Result IPA:** {'forte-lene': 'vaɟˈɟoːmɛʀ̟ ʔɛloːˈhiːim jiq̟q̟ɔːˈvuː hamˈmaːjim mitˈtʰaːħaθ haʃʃɔːˈmaːjim ʔɛl-mɔːˈq̟oːom ʔɛːˈħɔːɔð vaθeːʀ̟ɔːˈʔɛː haɟɟab-bɔːˈʃɔː ˌvaˑjhiː-ˈχeːen', 'extended-forte': 'vaɟˈɟoːmɛʀ̟ ʔɛloːˈhiːim jiq̟q̟ɔːˈvuː hamˈmaːjim mitˈtʰaːħaθ haʃʃɔːˈmaːjim ʔɛl-mɔːˈq̟oːom ʔɛːˈħɔːɔð vaθeːʀ̟ɔːˈʔɛː haɟɟab-bɔːˈʃɔː ˌvaˑjhiː-ˈχeːen'}
- **Source:** T1_4B_5_Ref.md §I.5.4.1 (lines 388–390)
- **Certainty:** high
- **Notes:** When the source prints only one reading because both streams coincide, the identical source IPA is assigned to both stream labels. | Dropped unresolved related_ids: ['TH-VAR-001', 'TH-VAR-002']
- **Examples:**
  - `וַיֹּ֣אמֶר אֱלֹהִ֗ים יִקָּו֨וּ הַמַּ֜יִם מִתַּ֤חַת הַשָּׁמַ֙יִם֙ אֶל־מָק֣וֹם אֶחָ֔ד וְתֵרָאֶ֖ה הַיַּבָּשָׁ֑ה וַֽיְהִי־כֵֽן׃` → `vaɟˈɟoːmɛʀ̟ ʔɛloːˈhiːim jiq̟q̟ɔːˈvuː hamˈmaːjim mitˈtʰaːħaθ haʃʃɔːˈmaːjim ʔɛl-mɔːˈq̟oːom ʔɛːˈħɔːɔð vaθeːʀ̟ɔːˈʔɛː haɟɟab-bɔːˈʃɔː ˌvaˑjhiː-ˈχeːen` (Genesis 1:9) [forte-lene]
  - `וַיֹּ֣אמֶר אֱלֹהִ֗ים יִקָּו֨וּ הַמַּ֜יִם מִתַּ֤חַת הַשָּׁמַ֙יִם֙ אֶל־מָק֣וֹם אֶחָ֔ד וְתֵרָאֶ֖ה הַיַּבָּשָׁ֑ה וַֽיְהִי־כֵֽן׃` → `vaɟˈɟoːmɛʀ̟ ʔɛloːˈhiːim jiq̟q̟ɔːˈvuː hamˈmaːjim mitˈtʰaːħaθ haʃʃɔːˈmaːjim ʔɛl-mɔːˈq̟oːom ʔɛːˈħɔːɔð vaθeːʀ̟ɔːˈʔɛː haɟɟab-bɔːˈʃɔː ˌvaˑjhiː-ˈχeːen` (Genesis 1:9) [extended-forte]

### TH-ORTH-SAMPLE-GEN-10-T4: Genesis 1:10 dual-stream sample

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** samples / dual-stream
- **Statement:** Canonical sample transcription of Genesis 1:10 in both standard streams.
- **Conditions:** Reciting Genesis 1:10.; Choose the configured standard stream.
- **Operation:** Use the corresponding source transcription without phonetic normalization.
- **Result IPA:** {'forte-lene': 'vaɟɟiq̟ˈʀ̟ɔː ʔɛloːˈhiːim laɟɟabbɔːˈʃɔː ˈʔɛːʀ̟ɛsˁ wulmiq̟ˈveː hamˈmaːjim q̟ɔːˈʀ̟ɔː jamˈmiːim vaɟˈɟaːaʀ̟ ʔɛloːˈhiːim kʰiː-ˈtˁoːov', 'extended-forte': 'vaɟɟiq̟ˈʀ̟ɔː ʔɛloːˈhiːim laɟɟabbɔːˈʃɔː ˈʔɛːʀ̟ɛsˁ wulmiq̟ˈveː hamˈmaːjim q̟ɔːˈʀ̟ɔː jamˈmiːim vaɟˈɟaːaʀ̟ ʔɛloːˈhiːim kkʰiː-ˈtˁoːov'}
- **Source:** T1_4B_5_Ref.md §I.5.4.1 (lines 392–396)
- **Certainty:** high
- **Notes:** When the source prints only one reading because both streams coincide, the identical source IPA is assigned to both stream labels. | Dropped unresolved related_ids: ['TH-VAR-001', 'TH-VAR-002']
- **Examples:**
  - `וַיִּקְרָ֨א אֱלֹהִ֤ים ׀ לַיַּבָּשָׁה֙ אֶ֔רֶץ וּלְמִקְוֵ֥ה הַמַּ֖יִם קָרָ֣א יַמִּ֑ים וַיַּ֥רְא אֱלֹהִ֖ים כִּי־טֽוֹב׃` → `vaɟɟiq̟ˈʀ̟ɔː ʔɛloːˈhiːim laɟɟabbɔːˈʃɔː ˈʔɛːʀ̟ɛsˁ wulmiq̟ˈveː hamˈmaːjim q̟ɔːˈʀ̟ɔː jamˈmiːim vaɟˈɟaːaʀ̟ ʔɛloːˈhiːim kʰiː-ˈtˁoːov` (Genesis 1:10) [forte-lene]
  - `וַיִּקְרָ֨א אֱלֹהִ֤ים ׀ לַיַּבָּשָׁה֙ אֶ֔רֶץ וּלְמִקְוֵ֥ה הַמַּ֖יִם קָרָ֣א יַמִּ֑ים וַיַּ֥רְא אֱלֹהִ֖ים כִּי־טֽוֹב׃` → `vaɟɟiq̟ˈʀ̟ɔː ʔɛloːˈhiːim laɟɟabbɔːˈʃɔː ˈʔɛːʀ̟ɛsˁ wulmiq̟ˈveː hamˈmaːjim q̟ɔːˈʀ̟ɔː jamˈmiːim vaɟˈɟaːaʀ̟ ʔɛloːˈhiːim kkʰiː-ˈtˁoːov` (Genesis 1:10) [extended-forte]

### TH-ORTH-SAMPLE-GEN-11-T4: Genesis 1:11 dual-stream sample

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** samples / dual-stream
- **Statement:** Canonical sample transcription of Genesis 1:11 in both standard streams.
- **Conditions:** Reciting Genesis 1:11.; Choose the configured standard stream.
- **Operation:** Use the corresponding source transcription without phonetic normalization.
- **Result IPA:** {'forte-lene': 'vaɟˈɟoːmɛʀ̟ ʔɛloːˈhiːim ˌtʰaˑðˈʃeː hɔːˈʔɔːʀ̟ɛsˁ ˈdɛːʃɛː ˈʕeːsɛv mɑzˈrˁiːjaʕ ˈzɛːʀ̟aʕ ˈʕeːesˁ pʰaˈʀ̟iː ˈʕoːsɛˑ ppʰaˈʀ̟iː lamiːˈnoː ʔaˈʃɛːɛʀ̟ zɑrˁʕoː-ˈvoː ʕal-hɔːˈʔɔːʀ̟ɛsˁ ˌvaˑjhiː-ˈχeːen', 'extended-forte': 'vaɟˈɟoːmɛʀ̟ ʔɛloːˈhiːim ˌttʰaˑðˈʃeː hɔːˈʔɔːʀ̟ɛsˁ ˈddɛːʃɛː ˈʕeːsɛv mɑzˈrˁiːjaʕ ˈzɛːʀ̟aʕ ˈʕeːesˁ ppʰaˈʀ̟iː ˈʕoːsɛˑ ppʰaˈʀ̟iː lamiːˈnoː ʔaˈʃɛːɛʀ̟ zɑrˁʕoː-ˈvoː ʕal-hɔːˈʔɔːʀ̟ɛsˁ ˌvaˑjhiː-ˈχeːen'}
- **Source:** T1_4B_5_Ref.md §I.5.4.1 (lines 398–402)
- **Certainty:** high
- **Notes:** When the source prints only one reading because both streams coincide, the identical source IPA is assigned to both stream labels. | Dropped unresolved related_ids: ['TH-VAR-001', 'TH-VAR-002']
- **Examples:**
  - `וַיֹּ֣אמֶר אֱלֹהִ֗ים תַּֽדְשֵׁ֤א הָאָ֙רֶץ֙ דֶּ֔שֶׁא עֵ֚שֶׂב מַזְרִ֣יעַ זֶ֔רַע עֵ֣ץ פְּרִ֞י עֹ֤שֶׂה פְּרִי֙ לְמִינ֔וֹ אֲשֶׁ֥ר זַרְעוֹ־ב֖וֹ עַל־הָאָ֑רֶץ וַֽיְהִי־כֵֽן׃` → `vaɟˈɟoːmɛʀ̟ ʔɛloːˈhiːim ˌtʰaˑðˈʃeː hɔːˈʔɔːʀ̟ɛsˁ ˈdɛːʃɛː ˈʕeːsɛv mɑzˈrˁiːjaʕ ˈzɛːʀ̟aʕ ˈʕeːesˁ pʰaˈʀ̟iː ˈʕoːsɛˑ ppʰaˈʀ̟iː lamiːˈnoː ʔaˈʃɛːɛʀ̟ zɑrˁʕoː-ˈvoː ʕal-hɔːˈʔɔːʀ̟ɛsˁ ˌvaˑjhiː-ˈχeːen` (Genesis 1:11) [forte-lene]
  - `וַיֹּ֣אמֶר אֱלֹהִ֗ים תַּֽדְשֵׁ֤א הָאָ֙רֶץ֙ דֶּ֔שֶׁא עֵ֚שֶׂב מַזְרִ֣יעַ זֶ֔רַע עֵ֣ץ פְּרִ֞י עֹ֤שֶׂה פְּרִי֙ לְמִינ֔וֹ אֲשֶׁ֥ר זַרְעוֹ־ב֖וֹ עַל־הָאָ֑רֶץ וַֽיְהִי־כֵֽן׃` → `vaɟˈɟoːmɛʀ̟ ʔɛloːˈhiːim ˌttʰaˑðˈʃeː hɔːˈʔɔːʀ̟ɛsˁ ˈddɛːʃɛː ˈʕeːsɛv mɑzˈrˁiːjaʕ ˈzɛːʀ̟aʕ ˈʕeːesˁ ppʰaˈʀ̟iː ˈʕoːsɛˑ ppʰaˈʀ̟iː lamiːˈnoː ʔaˈʃɛːɛʀ̟ zɑrˁʕoː-ˈvoː ʕal-hɔːˈʔɔːʀ̟ɛsˁ ˌvaˑjhiː-ˈχeːen` (Genesis 1:11) [extended-forte]

### TH-ORTH-SAMPLE-GEN-12-T4: Genesis 1:12 dual-stream sample

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** samples / dual-stream
- **Statement:** Canonical sample transcription of Genesis 1:12 in both standard streams.
- **Conditions:** Reciting Genesis 1:12.; Choose the configured standard stream.
- **Operation:** Use the corresponding source transcription without phonetic normalization.
- **Result IPA:** {'forte-lene': 'vattʰoːˈsˁeː hɔːˈʔɔːʀ̟ɛsˁ ˈdɛːʃɛː ˈʕeːsɛv mɑzˈrˁiːjaʕ ˈzɛːʀ̟aʕ lamiːˈneːhuː veˈʕeːesˁ ˈʕoːsɛˑ ppʰaˈʀ̟iː ʔaˈʃɛːɛʀ̟ zɑrˁʕoː-ˈvoː lamiːˈneːhuː vaɟˈɟaːaʀ̟ ʔɛloːˈhiːim kʰiː-ˈtˁoːov', 'extended-forte': 'vattʰoːˈsˁeː hɔːˈʔɔːʀ̟ɛsˁ ˈddɛːʃɛː ˈʕeːsɛv mɑzˈrˁiːjaʕ ˈzɛːʀ̟aʕ lamiːˈneːhuː veˈʕeːesˁ ˈʕoːsɛˑ ppʰaˈʀ̟iː ʔaˈʃɛːɛʀ̟ zɑrˁʕoː-ˈvoː lamiːˈneːhuː vaɟˈɟaːaʀ̟ ʔɛloːˈhiːim kkʰiː-ˈtˁoːov'}
- **Source:** T1_4B_5_Ref.md §I.5.4.1 (lines 404–408)
- **Certainty:** high
- **Notes:** When the source prints only one reading because both streams coincide, the identical source IPA is assigned to both stream labels. | Dropped unresolved related_ids: ['TH-VAR-001', 'TH-VAR-002']
- **Examples:**
  - `וַתּוֹצֵ֨א הָאָ֜רֶץ דֶּ֠שֶׁא עֵ֣שֶׂב מַזְרִ֤יעַ זֶ֙רַע֙ לְמִינֵ֔הוּ וְעֵ֧ץ עֹֽשֶׂה־פְּרִ֛י אֲשֶׁ֥ר זַרְעוֹ־ב֖וֹ לְמִינֵ֑הוּ וַיַּ֥רְא אֱלֹהִ֖ים כִּי־טֽוֹב׃` → `vattʰoːˈsˁeː hɔːˈʔɔːʀ̟ɛsˁ ˈdɛːʃɛː ˈʕeːsɛv mɑzˈrˁiːjaʕ ˈzɛːʀ̟aʕ lamiːˈneːhuː veˈʕeːesˁ ˈʕoːsɛˑ ppʰaˈʀ̟iː ʔaˈʃɛːɛʀ̟ zɑrˁʕoː-ˈvoː lamiːˈneːhuː vaɟˈɟaːaʀ̟ ʔɛloːˈhiːim kʰiː-ˈtˁoːov` (Genesis 1:12) [forte-lene]
  - `וַתּוֹצֵ֨א הָאָ֜רֶץ דֶּ֠שֶׁא עֵ֣שֶׂב מַזְרִ֤יעַ זֶ֙רַע֙ לְמִינֵ֔הוּ וְעֵ֧ץ עֹֽשֶׂה־פְּרִ֛י אֲשֶׁ֥ר זַרְעוֹ־ב֖וֹ לְמִינֵ֑הוּ וַיַּ֥רְא אֱלֹהִ֖ים כִּי־טֽוֹב׃` → `vattʰoːˈsˁeː hɔːˈʔɔːʀ̟ɛsˁ ˈddɛːʃɛː ˈʕeːsɛv mɑzˈrˁiːjaʕ ˈzɛːʀ̟aʕ lamiːˈneːhuː veˈʕeːesˁ ˈʕoːsɛˑ ppʰaˈʀ̟iː ʔaˈʃɛːɛʀ̟ zɑrˁʕoː-ˈvoː lamiːˈneːhuː vaɟˈɟaːaʀ̟ ʔɛloːˈhiːim kkʰiː-ˈtˁoːov` (Genesis 1:12) [extended-forte]

### TH-ORTH-SAMPLE-GEN-13-T4: Genesis 1:13 dual-stream sample

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** samples / dual-stream
- **Statement:** Canonical sample transcription of Genesis 1:13 in both standard streams.
- **Conditions:** Reciting Genesis 1:13.; Choose the configured standard stream.
- **Operation:** Use the corresponding source transcription without phonetic normalization.
- **Result IPA:** {'forte-lene': 'ˌvaˑjhiː-ˈʕɛːʀ̟ev ˌvaˑjhiː-ˈvoːq̟ɛʀ̟ ˈjoːom ʃaliːˈʃiː', 'extended-forte': 'ˌvaˑjhiː-ˈʕɛːʀ̟ev ˌvaˑjhiː-ˈvoːq̟ɛʀ̟ ˈjoːom ʃaliːˈʃiː'}
- **Source:** T1_4B_5_Ref.md §I.5.4.1 (lines 410–412)
- **Certainty:** high
- **Notes:** When the source prints only one reading because both streams coincide, the identical source IPA is assigned to both stream labels. | Dropped unresolved related_ids: ['TH-VAR-001', 'TH-VAR-002']
- **Examples:**
  - `וַֽיְהִי־עֶ֥רֶב וַֽיְהִי־בֹ֖קֶר י֥וֹם שְׁלִישִֽׁי׃` → `ˌvaˑjhiː-ˈʕɛːʀ̟ev ˌvaˑjhiː-ˈvoːq̟ɛʀ̟ ˈjoːom ʃaliːˈʃiː` (Genesis 1:13) [forte-lene]
  - `וַֽיְהִי־עֶ֥רֶב וַֽיְהִי־בֹ֖קֶר י֥וֹם שְׁלִישִֽׁי׃` → `ˌvaˑjhiː-ˈʕɛːʀ̟ev ˌvaˑjhiː-ˈvoːq̟ɛʀ̟ ˈjoːom ʃaliːˈʃiː` (Genesis 1:13) [extended-forte]

### TH-ORTH-SAMPLE-PS-01-T4: Psalm 1:1 dual-stream sample

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** samples / dual-stream
- **Statement:** Canonical sample transcription of Psalm 1:1 in both standard streams.
- **Conditions:** Reciting Psalm 1:1.; Choose the configured standard stream.
- **Operation:** Use the corresponding source transcription without phonetic normalization.
- **Result IPA:** {'forte-lene': 'ˌʔaːˌʃaˑʀ̟eː-hɔːˈʔiːiʃ ʔaˈʃɛːɛʀ̟ ˈloː hɔːˈlaːaχ baːʕɑˈsˁɑːɑθ ʀ̟aʃɔːˈʕiːim wuvˈðɛːʀ̟ɛχ ħɑttˁɔːˈʔiːim ˈloː ʕɔːˈmɔːɔð wuvmoːˈʃaːav leːˈsˁiːim ˈloː jɔːˈʃɔːɔv', 'extended-forte': 'ˌʔaːˌʃaˑʀ̟eː-hɔːˈʔiːiʃ ʔaˈʃɛːɛʀ̟ ˈloː hɔːˈlaːaχ bbaːʕɑˈsˁɑːɑθ ʀ̟aʃɔːˈʕiːim wuvˈðɛːʀ̟ɛχ ħɑttˁɔːˈʔiːim ˈloː ʕɔːˈmɔːɔð wuvmoːˈʃaːav leːˈsˁiːim ˈloː jɔːˈʃɔːɔv'}
- **Source:** T1_4B_5_Ref.md §I.5.4.2 (lines 418–422)
- **Certainty:** high
- **Notes:** When the source prints only one reading because both streams coincide, the identical source IPA is assigned to both stream labels. | Dropped unresolved related_ids: ['TH-VAR-001', 'TH-VAR-002']
- **Examples:**
  - `אַ֥שְֽׁרֵי־הָאִ֗ישׁ אֲשֶׁ֤ר ׀ לֹ֥א הָלַךְ֮ בַּעֲצַ֪ת רְשָׁ֫עִ֥ים וּבְדֶ֣רֶךְ חַ֭טָּאִים לֹ֥א עָמָ֑ד וּבְמוֹשַׁ֥ב לֵ֝צִ֗ים לֹ֣א יָשָֽׁב׃` → `ˌʔaːˌʃaˑʀ̟eː-hɔːˈʔiːiʃ ʔaˈʃɛːɛʀ̟ ˈloː hɔːˈlaːaχ baːʕɑˈsˁɑːɑθ ʀ̟aʃɔːˈʕiːim wuvˈðɛːʀ̟ɛχ ħɑttˁɔːˈʔiːim ˈloː ʕɔːˈmɔːɔð wuvmoːˈʃaːav leːˈsˁiːim ˈloː jɔːˈʃɔːɔv` (Psalm 1:1) [forte-lene]
  - `אַ֥שְֽׁרֵי־הָאִ֗ישׁ אֲשֶׁ֤ר ׀ לֹ֥א הָלַךְ֮ בַּעֲצַ֪ת רְשָׁ֫עִ֥ים וּבְדֶ֣רֶךְ חַ֭טָּאִים לֹ֥א עָמָ֑ד וּבְמוֹשַׁ֥ב לֵ֝צִ֗ים לֹ֣א יָשָֽׁב׃` → `ˌʔaːˌʃaˑʀ̟eː-hɔːˈʔiːiʃ ʔaˈʃɛːɛʀ̟ ˈloː hɔːˈlaːaχ bbaːʕɑˈsˁɑːɑθ ʀ̟aʃɔːˈʕiːim wuvˈðɛːʀ̟ɛχ ħɑttˁɔːˈʔiːim ˈloː ʕɔːˈmɔːɔð wuvmoːˈʃaːav leːˈsˁiːim ˈloː jɔːˈʃɔːɔv` (Psalm 1:1) [extended-forte]

### TH-ORTH-SAMPLE-PS-02-T4: Psalm 1:2 dual-stream sample

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** samples / dual-stream
- **Statement:** Canonical sample transcription of Psalm 1:2 in both standard streams.
- **Conditions:** Reciting Psalm 1:2.; Choose the configured standard stream.
- **Operation:** Use the corresponding source transcription without phonetic normalization.
- **Result IPA:** {'forte-lene': 'ˈkʰiː ˈʔiːim baθoːˈʀ̟aːaθ ʔaðoːˈnɔːɔj ħɛfˈsˁoː ˌwuˑvθoːʀ̟ɔːˈθoː jɛhˈgɛː joːˈmɔːɔm vɔːˈlɔːɔjlɔː', 'extended-forte': 'ˈkkʰiː ˈʔiːim bbaθoːˈʀ̟aːaθ ʔaðoːˈnɔːɔj ħɛfˈsˁoː ˌwuˑvθoːʀ̟ɔːˈθoː jɛhˈggɛː joːˈmɔːɔm vɔːˈlɔːɔjlɔː'}
- **Source:** T1_4B_5_Ref.md §I.5.4.2 (lines 424–428)
- **Certainty:** high
- **Notes:** When the source prints only one reading because both streams coincide, the identical source IPA is assigned to both stream labels. | Dropped unresolved related_ids: ['TH-VAR-001', 'TH-VAR-002']
- **Examples:**
  - `כִּ֤י אִ֥ם בְּתוֹרַ֥ת יְהוָ֗ה חֶ֫פְצ֥וֹ וּֽבְתוֹרָת֥וֹ יֶהְגֶּ֗ה יוֹמָ֥ם וָלָֽיְלָה׃` → `ˈkʰiː ˈʔiːim baθoːˈʀ̟aːaθ ʔaðoːˈnɔːɔj ħɛfˈsˁoː ˌwuˑvθoːʀ̟ɔːˈθoː jɛhˈgɛː joːˈmɔːɔm vɔːˈlɔːɔjlɔː` (Psalm 1:2) [forte-lene]
  - `כִּ֤י אִ֥ם בְּתוֹרַ֥ת יְהוָ֗ה חֶ֫פְצ֥וֹ וּֽבְתוֹרָת֥וֹ יֶהְגֶּ֗ה יוֹמָ֥ם וָלָֽיְלָה׃` → `ˈkkʰiː ˈʔiːim bbaθoːˈʀ̟aːaθ ʔaðoːˈnɔːɔj ħɛfˈsˁoː ˌwuˑvθoːʀ̟ɔːˈθoː jɛhˈggɛː joːˈmɔːɔm vɔːˈlɔːɔjlɔː` (Psalm 1:2) [extended-forte]

### TH-ORTH-SAMPLE-PS-03-T4: Psalm 1:3 dual-stream sample

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** samples / dual-stream
- **Statement:** Canonical sample transcription of Psalm 1:3 in both standard streams.
- **Conditions:** Reciting Psalm 1:3.; Choose the configured standard stream.
- **Operation:** Use the corresponding source transcription without phonetic normalization.
- **Result IPA:** {'forte-lene': 'ˌvɔˑhɔːˈjɔː kʰeˈʕeːesˁ ʃɔːˈθuːul ˌʕaˑl-pʰalˈʁeː ˈmɔːjim ʔaˈʃɛːɛʀ̟ pʰiʀ̟ˈjoː jitˈtʰeːen biʕitˈtʰoː vɔʕɔːˈleːhuː ˌloː-jibˈboːol vaˈχoːol ʔaʃɛʀ̟-jaːʕaˈsɛː jɑsˁˈliːjaħ', 'extended-forte': 'ˌvɔˑhɔːˈjɔː kkʰeˈʕeːesˁ ʃɔːˈθuːul ˌʕaˑl-ppʰalˈʁeː ˈmɔːjim ʔaˈʃɛːɛʀ̟ ppʰiʀ̟ˈjoː jitˈtʰeːen bbiʕitˈtʰoː vɔʕɔːˈleːhuː ˌloː-jibˈboːol vaˈχoːol ʔaʃɛʀ̟-jaːʕaˈsɛː jɑsˁˈliːjaħ'}
- **Source:** T1_4B_5_Ref.md §I.5.4.2 (lines 430–434)
- **Certainty:** high
- **Notes:** When the source prints only one reading because both streams coincide, the identical source IPA is assigned to both stream labels. | Dropped unresolved related_ids: ['TH-VAR-001', 'TH-VAR-002']
- **Examples:**
  - `וְֽהָיָ֗ה כְּעֵץ֮ שָׁת֪וּל עַֽל־פַּלְגֵ֫י מָ֥יִם אֲשֶׁ֤ר פִּרְי֨וֹ ׀ יִתֵּ֬ן בְּעִתּ֗וֹ וְעָלֵ֥הוּ לֹֽא־יִבּ֑וֹל וְכֹ֖ל אֲשֶׁר־יַעֲשֶׂ֣ה יַצְלִֽיחַ׃` → `ˌvɔˑhɔːˈjɔː kʰeˈʕeːesˁ ʃɔːˈθuːul ˌʕaˑl-pʰalˈʁeː ˈmɔːjim ʔaˈʃɛːɛʀ̟ pʰiʀ̟ˈjoː jitˈtʰeːen biʕitˈtʰoː vɔʕɔːˈleːhuː ˌloː-jibˈboːol vaˈχoːol ʔaʃɛʀ̟-jaːʕaˈsɛː jɑsˁˈliːjaħ` (Psalm 1:3) [forte-lene]
  - `וְֽהָיָ֗ה כְּעֵץ֮ שָׁת֪וּל עַֽל־פַּלְגֵ֫י מָ֥יִם אֲשֶׁ֤ר פִּרְי֨וֹ ׀ יִתֵּ֬ן בְּעִתּ֗וֹ וְעָלֵ֥הוּ לֹֽא־יִבּ֑וֹל וְכֹ֖ל אֲשֶׁר־יַעֲשֶׂ֣ה יַצְלִֽיחַ׃` → `ˌvɔˑhɔːˈjɔː kkʰeˈʕeːesˁ ʃɔːˈθuːul ˌʕaˑl-ppʰalˈʁeː ˈmɔːjim ʔaˈʃɛːɛʀ̟ ppʰiʀ̟ˈjoː jitˈtʰeːen bbiʕitˈtʰoː vɔʕɔːˈleːhuː ˌloː-jibˈboːol vaˈχoːol ʔaʃɛʀ̟-jaːʕaˈsɛː jɑsˁˈliːjaħ` (Psalm 1:3) [extended-forte]

### TH-ORTH-SAMPLE-PS-04-T4: Psalm 1:4 dual-stream sample

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** samples / dual-stream
- **Statement:** Canonical sample transcription of Psalm 1:4 in both standard streams.
- **Conditions:** Reciting Psalm 1:4.; Choose the configured standard stream.
- **Operation:** Use the corresponding source transcription without phonetic normalization.
- **Result IPA:** {'forte-lene': 'loː-ˈχeːen hɔːʀ̟aʃɔːˈʕiːim ˈkʰiː ʔim-kʰamˈmoːosˁ ˌʔaˑʃɛʀ̟-tʰiddaˈfɛːɛnnuː ˈʀ̟uːwaħ', 'extended-forte': 'loː-ˈχeːen hɔːʀ̟aʃɔːˈʕiːim ˈkkʰiː ʔim-kkʰamˈmoːosˁ ˌʔaˑʃɛʀ̟-ttʰiddaˈfɛːɛnnuː ˈʀ̟uːwaħ'}
- **Source:** T1_4B_5_Ref.md §I.5.4.2 (lines 436–440)
- **Certainty:** high
- **Notes:** When the source prints only one reading because both streams coincide, the identical source IPA is assigned to both stream labels. | Dropped unresolved related_ids: ['TH-VAR-001', 'TH-VAR-002']
- **Examples:**
  - `לֹא־כֵ֥ן הָרְשָׁעִ֑ים כִּ֥י אִם־כַּ֝מֹּ֗ץ אֲ‍ֽשֶׁר־תִּדְּפֶ֥נּוּ רֽוּחַ׃` → `loː-ˈχeːen hɔːʀ̟aʃɔːˈʕiːim ˈkʰiː ʔim-kʰamˈmoːosˁ ˌʔaˑʃɛʀ̟-tʰiddaˈfɛːɛnnuː ˈʀ̟uːwaħ` (Psalm 1:4) [forte-lene]
  - `לֹא־כֵ֥ן הָרְשָׁעִ֑ים כִּ֥י אִם־כַּ֝מֹּ֗ץ אֲ‍ֽשֶׁר־תִּדְּפֶ֥נּוּ רֽוּחַ׃` → `loː-ˈχeːen hɔːʀ̟aʃɔːˈʕiːim ˈkkʰiː ʔim-kkʰamˈmoːosˁ ˌʔaˑʃɛʀ̟-ttʰiddaˈfɛːɛnnuː ˈʀ̟uːwaħ` (Psalm 1:4) [extended-forte]

### TH-ORTH-SAMPLE-PS-05-T4: Psalm 1:5 dual-stream sample

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** samples / dual-stream
- **Statement:** Canonical sample transcription of Psalm 1:5 in both standard streams.
- **Conditions:** Reciting Psalm 1:5.; Choose the configured standard stream.
- **Operation:** Use the corresponding source transcription without phonetic normalization.
- **Result IPA:** {'forte-lene': 'ʕal-ˈkʰeːen loː-jɔːˈq̟uːmuː ʀ̟aʃɔːˈʕiːim bammiʃˈpʰɔːɔtˁ vaħɑttˁɔːˈʔiːim baːʕaˈðaːaθ sˁɑddiːˈq̟iːim', 'extended-forte': 'ʕal-ˈkkʰeːen loː-jɔːˈq̟uːmuː ʀ̟aʃɔːˈʕiːim bbammiʃˈppʰɔːɔtˁ vaħɑttˁɔːˈʔiːim bbaːʕaˈðaːaθ sˁɑddiːˈq̟iːim'}
- **Source:** T1_4B_5_Ref.md §I.5.4.2 (lines 442–446)
- **Certainty:** high
- **Notes:** When the source prints only one reading because both streams coincide, the identical source IPA is assigned to both stream labels. | Dropped unresolved related_ids: ['TH-VAR-001', 'TH-VAR-002']
- **Examples:**
  - `עַל־כֵּ֤ן ׀ לֹא־יָקֻ֣מוּ רְ֭שָׁעִים בַּמִּשְׁפָּ֑ט וְ֝חַטָּאִ֗ים בַּעֲדַ֥ת צַדִּיקִֽים׃` → `ʕal-ˈkʰeːen loː-jɔːˈq̟uːmuː ʀ̟aʃɔːˈʕiːim bammiʃˈpʰɔːɔtˁ vaħɑttˁɔːˈʔiːim baːʕaˈðaːaθ sˁɑddiːˈq̟iːim` (Psalm 1:5) [forte-lene]
  - `עַל־כֵּ֤ן ׀ לֹא־יָקֻ֣מוּ רְ֭שָׁעִים בַּמִּשְׁפָּ֑ט וְ֝חַטָּאִ֗ים בַּעֲדַ֥ת צַדִּיקִֽים׃` → `ʕal-ˈkkʰeːen loː-jɔːˈq̟uːmuː ʀ̟aʃɔːˈʕiːim bbammiʃˈppʰɔːɔtˁ vaħɑttˁɔːˈʔiːim bbaːʕaˈðaːaθ sˁɑddiːˈq̟iːim` (Psalm 1:5) [extended-forte]

### TH-ORTH-SAMPLE-PS-06-T4: Psalm 1:6 dual-stream sample

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** samples / dual-stream
- **Statement:** Canonical sample transcription of Psalm 1:6 in both standard streams.
- **Conditions:** Reciting Psalm 1:6.; Choose the configured standard stream.
- **Operation:** Use the corresponding source transcription without phonetic normalization.
- **Result IPA:** {'forte-lene': 'ˌkʰiː-joːˈðeːjaʕ ʔaðoːˈnɔːɔj ˈdɛːʀ̟ɛχ sˁɑddiːˈq̟iːim vaˈðɛːʀ̟ɛχ ʀ̟aʃɔːˈʕiːim tʰoːˈveːeð', 'extended-forte': 'ˌkkʰiː-joːˈðeːjaʕ ʔaðoːˈnɔːɔj ˈddɛːʀ̟ɛχ sˁɑddiːˈq̟iːim vaˈðɛːʀ̟ɛχ ʀ̟aʃɔːˈʕiːim ttʰoːˈveːeð'}
- **Source:** T1_4B_5_Ref.md §I.5.4.2 (lines 448–452)
- **Certainty:** high
- **Notes:** When the source prints only one reading because both streams coincide, the identical source IPA is assigned to both stream labels. | Dropped unresolved related_ids: ['TH-VAR-001', 'TH-VAR-002']
- **Examples:**
  - `כִּֽי־יוֹדֵ֣עַ יְ֭הוָה דֶּ֣רֶךְ צַדִּיקִ֑ים וְדֶ֖רֶךְ רְשָׁעִ֣ים תֹּאבֵֽד` → `ˌkʰiː-joːˈðeːjaʕ ʔaðoːˈnɔːɔj ˈdɛːʀ̟ɛχ sˁɑddiːˈq̟iːim vaˈðɛːʀ̟ɛχ ʀ̟aʃɔːˈʕiːim tʰoːˈveːeð` (Psalm 1:6) [forte-lene]
  - `כִּֽי־יוֹדֵ֣עַ יְ֭הוָה דֶּ֣רֶךְ צַדִּיקִ֑ים וְדֶ֖רֶךְ רְשָׁעִ֣ים תֹּאבֵֽד` → `ˌkkʰiː-joːˈðeːjaʕ ʔaðoːˈnɔːɔj ˈddɛːʀ̟ɛχ sˁɑddiːˈq̟iːim vaˈðɛːʀ̟ɛχ ʀ̟aʃɔːˈʕiːim ttʰoːˈveːeð` (Psalm 1:6) [extended-forte]

## variation

### TH-VAR-ALEF-T1-001: Noncanonical alef dagesh

- **Status:** variant
- **Authority:** manuscript
- **Category:** manuscript variation / alef dagesh
- **Statement:** Some early model codices mark dagesh in additional consonantal alefs, but these are not canonical.
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Record a manuscript-specific protective marking; do not infer canonical status.
- **Result IPA:** None
- **Source:** T1_1.md §I.1.1 (lines 41–55)
- **Certainty:** high
- **Examples:**
  - `וְאָּנֹכִ֖י` → `—` (Ruth 2.10)
  - `וַתַּֽעַזְבִ֞י אָּבִ֣יךְ` → `—` (Ruth 2.11)

### TH-VAR-T3-007: Non-Standard Tiberian generalized dagesh

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** variation / NST
- **Statement:** Some Non-Standard Tiberian manuscripts extend dagesh/rafe distribution from BGDKPT to most geminable consonants at word onset and after silent shewa.
- **Conditions:** The source is a manuscript with Non-Standard Tiberian vocalization.
- **Operation:** Treat the marking as evidence of a generalized onset-strengthening system, not as the Standard Tiberian distribution.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.3 (lines 835–873)
- **Certainty:** high
- **Examples:** no example in source

### TH-VAR-T3-008: NST extended-forte analogy

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** variation / NST
- **Statement:** The extended NST marking may represent phonetic gemination created by analogical extension of the extended-forte stream to non-BGDKPT onsets.
- **Conditions:** Interpreting the described NST system.
- **Operation:** Model marked eligible onsets as geminated only within this non-standard system.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.3 (lines 869–879)
- **Certainty:** medium
- **Examples:**
  - `נִּשְׁמֹּר` → `nniʃ.ˈmmoːoʀ̟`

### TH-VAR-T4-101: I.4 evidence is non-target variation

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** variation / imperfect-learning
- **Statement:** Treat I.4 phenomena as evidence of imperfect acquisition, substrate interference, or hypercorrection, not as Standard Tiberian rules.
- **Conditions:** A datum is presented in I.4.
- **Operation:** Tag as evidence/variant and keep it outside the standard target grammar.
- **Result IPA:** None
- **Source:** T1_4B_5_Ref.md §I.4.1 (lines 1–14)
- **Certainty:** high
- **Examples:** no example in source

### TH-VAR-T4-102: Later written signs decoupled from pronunciation

- **Status:** evidence
- **Authority:** standard-tiberian
- **Category:** variation / later-middle-ages
- **Statement:** After the oral Tiberian tradition disappeared, Tiberian signs could be read through local traditions and no longer directly evidence Tiberian pronunciation.
- **Conditions:** Interpreting later medieval vocalized Bibles.
- **Operation:** Do not infer oral Tiberian realization from signs alone without independent evidence.
- **Result IPA:** None
- **Source:** T1_4B_5_Ref.md §I.4.4 (lines 271–273)
- **Certainty:** high
- **Examples:** no example in source

## gaps

### TH-GAP-BGDKPT-T1-001: No certain Hebrew minimal pair

- **Status:** gap
- **Authority:** standard-tiberian
- **Category:** BGDKPT / minimal-pair evidence
- **Statement:** The Hebrew Bible has no certain minimal pair created by BGDKPT phonemicization.
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Do not claim an attested Hebrew minimal pair from this source.
- **Result IPA:** None
- **Source:** T1_1.md §I.1.25 (lines 1577–1577)
- **Certainty:** unresolved
- **Notes:** Dropped unresolved related_ids: ['TH-BGDKPT-DIST-003']
- **Examples:** no example in source

### TH-GAP-DUAL-V-T1-001: Dual /v/ inventory entries

- **Status:** gap
- **Authority:** standard-tiberian
- **Category:** phoneme inventory / dual /v/
- **Statement:** The table lists /v/ for both bet rafe and vav, whose [v] realizations overlap; no distinct minimal-pair evidence is supplied here.
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Keep both inventory entries while recording the overlap.
- **Result IPA:** None
- **Source:** T1_1.md §I.1.24 (lines 1531–1537)
- **Certainty:** unresolved
- **Notes:** Dropped unresolved related_ids: ['TH-CON-INV-003', 'TH-CON-INV-009', 'TH-CON-VAV-001', 'TH-BGDKPT-BET-002']
- **Examples:** no example in source

### TH-GAP-T0-001: Unwritten oral detail

- **Status:** gap
- **Authority:** editorial
- **Category:** reconstruction / oral tradition
- **Statement:** Pronunciation cannot be recovered reliably from signs alone where oral details were unmarked.
- **Conditions:** When a phonetic feature is not graphically represented.
- **Operation:** Consult sources with access to the living oral tradition.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.4 (lines 84–86)
- **Certainty:** unresolved
- **Notes:** Do not infer absence from non-marking.
- **Examples:** no example in source

### TH-GAP-T0-003: Lost unmarked orthoepy

- **Status:** gap
- **Authority:** editorial
- **Category:** reconstruction / oral loss
- **Statement:** Unmarked orthoepic features, including extended dagesh forte, were forgotten after the oral tradition disappeared.
- **Conditions:** When using later signs alone.
- **Operation:** Do not treat non-marking as proof of non-pronunciation.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.12 (lines 627–627)
- **Certainty:** unresolved
- **Examples:** no example in source

### TH-GAP-T0-004: NST not simply Ben Naftali

- **Status:** conflict
- **Authority:** editorial
- **Category:** tradition / classification
- **Statement:** NST cannot be equated with Ben Naftali solely from לִישְׂרָאֵל-type pointing because it contains many unattested additional features.
- **Conditions:** When classifying NST witnesses.
- **Operation:** Do not infer Ben Naftali affiliation from one feature.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.13.6 (lines 701–701)
- **Certainty:** unresolved
- **Examples:** no example in source

### TH-GAP-T2-001: Conditioning of pataḥ [a] versus [ɑ]

- **Status:** gap
- **Authority:** standard-tiberian
- **Category:** gap / allophony
- **Statement:** Pataḥ likely had [a] and [ɑ] allophones, with [ɑ] especially near tongue-root-retracting consonants, but the source does not provide a deterministic Tiberian distribution.
- **Conditions:** pataḥ
- **Operation:** Do not choose [a] versus [ɑ] deterministically from this source alone.
- **Result IPA:** a ~ ɑ
- **Source:** T1_2B_corrected_p352.md §I.2.1.3. More on the Quality of _Pataḥ_ and _Qameṣ_ (lines 32–34)
- **Certainty:** medium
- **Notes:** Modern Middle Eastern traditions are indirect evidence, not a complete Tiberian rule.
- **Examples:** no example in source

### TH-GAP-T2-002: Distribution of guttural ḥaṭef

- **Status:** gap
- **Authority:** standard-tiberian
- **Category:** gap / guttural-epenthesis
- **Statement:** Ḥaṭef on gutturals is not universal; following-consonant sonority and metrical rhythm condition tendencies, but variation remains.
- **Conditions:** guttural before consonant
- **Operation:** Do not infer ḥaṭef solely from segment sequence.
- **Result IPA:** None
- **Source:** T1_2B_corrected_p352.md §I.2.5.4. _Ḥaṭef_ Signs on Guttural Consonants (lines 1354–1360)
- **Certainty:** unresolved
- **Examples:**
  - `יַחֲר֣וֹשׁ` → `—` (Hos. 10.11)
  - `יֶחְדַּ֥ל` → `—` (1 Sam. 9.5)

### TH-GAP-T2-003: Article plus mem distribution

- **Status:** gap
- **Authority:** standard-tiberian
- **Category:** gap / article-mem
- **Statement:** The vocalic-versus-silent realization of shewa in article+מְ forms has no absolute deterministic rule; word length, accent distance, minor gaʿya, and fixed stream-specific distributions interact.
- **Conditions:** definite article + מְ
- **Operation:** Require lexical/manuscript evidence.
- **Result IPA:** haːma ~ haˑm ~ ham
- **Source:** T1_2B_corrected_p352.md §I.2.5.8.1. The Definite Article (lines 1998–2024)
- **Certainty:** unresolved
- **Examples:** no example in source

### TH-GAP-T2-004: Marginal minor-gaʿya distribution

- **Status:** gap
- **Authority:** standard-tiberian
- **Category:** gap / minor-gaya
- **Statement:** Outside regular patterns, minor gaʿya is inconsistent and may be absent; the source does not define a fully deterministic placement rule.
- **Conditions:** closed short vowel before main stress; noncanonical buffer or conjunctive accent
- **Operation:** Require lexical/manuscript evidence.
- **Result IPA:** ˌVˑ ~ V
- **Source:** T1_2B_corrected_p352.md §I.2.8.2.2. On Closed Syllables with Short Vowels   (lines 3566–3604)
- **Certainty:** unresolved
- **Examples:** no example in source

### TH-GAP-T3-001: BHS phantom dagesh is editorial error

- **Status:** gap
- **Authority:** standard-tiberian
- **Category:** editorial / BHS-error
- **Statement:** Do not infer gemination from BHS dagesh signs shown to be parchment specks or other transcription errors in L.
- **Conditions:** The BHS locus is one of the demonstrated erroneous dagesh readings.
- **Operation:** Discard the phantom dagesh; follow the manuscript reading.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.14 (lines 741–761)
- **Certainty:** unresolved
- **Notes:** This is a gap/editorial safeguard, not a Standard Tiberian pronunciation rule.
- **Examples:**
  - `אֲבִימֶ֥לֶךְ` → `—` (Gen. 26.1)
  - `אֲבִימֶּ֥לֶךְ` → `—` (Gen. 26.1)

### TH-GAP-YOD-T1-001: Yod stop-symbol discrepancy

- **Status:** gap
- **Authority:** comparative
- **Category:** transcription gap / yod
- **Statement:** The prose gives [ɉ], while the phoneme table gives [ɟ], for geminated yod.
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Preserve both source forms; do not silently normalize them.
- **Result IPA:** None
- **Source:** T1_1.md §I.1.10; I.1.24 (lines 997–1541)
- **Certainty:** unresolved
- **Notes:** Dropped unresolved related_ids: ['TH-CON-YOD-002', 'TH-CON-INV-013']
- **Examples:** no example in source

### TH-VAR-VAV-T1-001: Vav after pretonic u

- **Status:** conflict
- **Authority:** comparative
- **Category:** sub-tradition / vav after u
- **Statement:** After pretonic [uː], Mishaʾel reports [w], while al-Fāsī and transcriptions support [v].
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Choose the realization belonging to the selected source stream.
- **Result IPA:** None
- **Source:** T1_1.md §I.1.6 (lines 581–609)
- **Certainty:** unresolved
- **Examples:**
  - `וּפֻוָ֖ה` → `fuːwɔː` (Gen. 46.13)
  - `וּפֻוָ֖ה` → `fuːˈvɔː` (Gen. 46.13)

### TH-VAR-ZAYIN-T1-001: Zāy makrūkh

- **Status:** gap
- **Authority:** standard-tiberian
- **Category:** variant / zayin
- **Statement:** A reported zāy makrūkh may be [zˁ], but its identity and distribution are unknown.
- **Conditions:** Unknown.
- **Operation:** Do not apply automatically.
- **Result IPA:** zˁ
- **Source:** T1_1.md §I.1.7 (lines 845–865)
- **Certainty:** low
- **Notes:** It may refer to voiced ṣade rather than written zayin.
- **Examples:** no example in source

## other

### TH-ACC-T0-001: Accents mark main stress

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** prosody / stress
- **Statement:** Accent signs indicate main word stress as well as cantillation.
- **Conditions:** For accented Tiberian words.
- **Operation:** Locate main stress at the accent.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.4 (lines 76–76)
- **Certainty:** high
- **Examples:** no example in source

### TH-ACC-T0-002: Cantillation follows qere

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** prosody / qere interaction
- **Statement:** Accents relate more closely to qere: read additions have accents and unread ketiv words do not.
- **Conditions:** At qere additions or ketiv omissions.
- **Operation:** Assign accents to the qere stream.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.6 (lines 288–304)
- **Certainty:** high
- **Examples:**
  - `הִנֵּ֛ה יָמִ֥ים בָּאִ֖ים` → `—` (I.0.6 line 302)

### TH-ACC-T0-003: Conjunctive accents prevent slurring

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** prosody / orthoepy
- **Statement:** Conjunctive accents reduce accentless orthographic words at risk of slurring.
- **Conditions:** Between disjunctive accents.
- **Operation:** Give intervening words conjunctive accents.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.11 (lines 573–573)
- **Certainty:** high
- **Examples:** no example in source

### TH-BGDKPT-BET-T1-001: Bet with dagesh

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** BGDKPT / letter realization
- **Statement:** בּ is a voiced bilabial stop [b].
- **Conditions:** The letter bears dagesh.
- **Operation:** Realize בּ as [b].
- **Result IPA:** b
- **Source:** T1_1.md §I.1.2 (lines 265–269)
- **Certainty:** high
- **Examples:** no example in source

### TH-BGDKPT-BET-T1-002: Bet without dagesh

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** BGDKPT / letter realization
- **Statement:** בֿ is a voiced labio-dental fricative [v].
- **Conditions:** The letter lacks dagesh and is not geminated.
- **Operation:** Realize בֿ as [v].
- **Result IPA:** v
- **Source:** T1_1.md §I.1.2 (lines 265–271)
- **Certainty:** high
- **Examples:** no example in source

### TH-BGDKPT-BET-T1-003: Rafe on fricative bet

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** orthographic cue / rafe
- **Statement:** Fricative bet is frequently, but not regularly, marked with rafe.
- **Conditions:** The BGDKPT letter has its fricative realization.
- **Operation:** Treat rafe as an explicit fricative cue.
- **Result IPA:** None
- **Source:** T1_1.md §I.1.2 (lines 269–271)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-BGDKPT-BET-002']
- **Examples:** no example in source

### TH-BGDKPT-DALET-T1-001: Dalet with dagesh

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** BGDKPT / letter realization
- **Statement:** דּ is a voiced post-dental stop [d].
- **Conditions:** The letter bears dagesh.
- **Operation:** Realize דּ as [d].
- **Result IPA:** d
- **Source:** T1_1.md §I.1.4 (lines 337–343)
- **Certainty:** high
- **Examples:** no example in source

### TH-BGDKPT-DALET-T1-002: Dalet without dagesh

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** BGDKPT / letter realization
- **Statement:** דֿ is a voiced post-dental fricative [ð].
- **Conditions:** The letter lacks dagesh and is not geminated.
- **Operation:** Realize דֿ as [ð].
- **Result IPA:** ð
- **Source:** T1_1.md §I.1.4 (lines 337–343)
- **Certainty:** high
- **Examples:** no example in source

### TH-BGDKPT-DALET-T1-003: Rafe on fricative dalet

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** orthographic cue / rafe
- **Statement:** Fricative dalet is frequently, but not regularly, marked with rafe.
- **Conditions:** The BGDKPT letter has its fricative realization.
- **Operation:** Treat rafe as an explicit fricative cue.
- **Result IPA:** None
- **Source:** T1_1.md §I.1.4 (lines 341–343)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-BGDKPT-DALET-002']
- **Examples:** no example in source

### TH-BGDKPT-DIST-T1-001: Postvocalic fricative distribution

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** BGDKPT / distribution
- **Statement:** Ungeminated BGDKPT letters generally become [v ʁ ð χ f θ] after a vowel.
- **Conditions:** A BGDKPT consonant follows a vowel and is not geminated.
- **Operation:** Select its fricative realization.
- **Result IPA:** None
- **Source:** T1_1.md §I.1.25 (lines 1561–1561)
- **Certainty:** high
- **Examples:**
  - `רַ֣ב` → `ˈʀ̟aːav` (Gen. 24.25)
  - `יִשְׁכְּבוּ֙` → `jiʃkʰaˈvuː` (Isa. 43.17)

### TH-BGDKPT-DIST-T1-002: Fricative after historical vowel loss

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** BGDKPT / lexicalization
- **Statement:** A fricative may survive after its historically preceding vowel has been elided.
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Retain the lexically specified fricative.
- **Result IPA:** None
- **Source:** T1_1.md §I.1.25 (lines 1561–1565)
- **Certainty:** high
- **Examples:**
  - `בְּכָתְבוֹ֩` → `baχɔθˈvoː` (Jer. 45.1)
  - `מַלְכֵ֥י` → `malˈχeː` (Gen. 17.16)

### TH-BGDKPT-DIST-T1-003: Synchronic BGDKPT phonemicization

- **Status:** rule
- **Authority:** editorial
- **Category:** BGDKPT / phonemicization
- **Statement:** Because stop/fricative distribution is not fully predictable, synchronic representations distinguish the variants.
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Encode stop and fricative as distinct synchronic segments.
- **Result IPA:** None
- **Source:** T1_1.md §I.1.25 (lines 1571–1575)
- **Certainty:** high
- **Examples:**
  - `מַלְכֵ֥י` → `malˈχeː` (Gen. 17.16)
  - `בִּנְפֹ֖ל` → `binˈfoːol` (Isa. 30.25)

### TH-BGDKPT-GIMEL-T1-001: Gimel with dagesh

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** BGDKPT / letter realization
- **Statement:** גּ is a voiced velar stop [g].
- **Conditions:** The letter bears dagesh.
- **Operation:** Realize גּ as [g].
- **Result IPA:** g
- **Source:** T1_1.md §I.1.3 (lines 315–321)
- **Certainty:** high
- **Examples:** no example in source

### TH-BGDKPT-GIMEL-T1-002: Gimel without dagesh

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** BGDKPT / letter realization
- **Statement:** גֿ is a voiced uvular fricative [ʁ].
- **Conditions:** The letter lacks dagesh and is not geminated.
- **Operation:** Realize גֿ as [ʁ].
- **Result IPA:** ʁ
- **Source:** T1_1.md §I.1.3 (lines 315–321)
- **Certainty:** high
- **Examples:** no example in source

### TH-BGDKPT-GIMEL-T1-003: Rafe on fricative gimel

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** orthographic cue / rafe
- **Statement:** Fricative gimel is frequently, but not regularly, marked with rafe.
- **Conditions:** The BGDKPT letter has its fricative realization.
- **Operation:** Treat rafe as an explicit fricative cue.
- **Result IPA:** None
- **Source:** T1_1.md §I.1.3 (lines 319–321)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-BGDKPT-GIMEL-002']
- **Examples:** no example in source

### TH-BGDKPT-KAF-T1-001: Kaf with dagesh

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** BGDKPT / letter realization
- **Statement:** כּ is a unvoiced aspirated velar stop [kʰ].
- **Conditions:** The letter bears dagesh.
- **Operation:** Realize כּ as [kʰ].
- **Result IPA:** kʰ
- **Source:** T1_1.md §I.1.11 (lines 1067–1073)
- **Certainty:** high
- **Examples:** no example in source

### TH-BGDKPT-KAF-T1-002: Kaf without dagesh

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** BGDKPT / letter realization
- **Statement:** כ, ך is a unvoiced uvular fricative [χ].
- **Conditions:** The letter lacks dagesh and is not geminated.
- **Operation:** Realize כ, ך as [χ].
- **Result IPA:** χ
- **Source:** T1_1.md §I.1.11 (lines 1067–1073)
- **Certainty:** high
- **Examples:** no example in source

### TH-BGDKPT-KAF-T1-003: Rafe on fricative kaf

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** orthographic cue / rafe
- **Statement:** Fricative kaf is frequently, but not regularly, marked with rafe.
- **Conditions:** The BGDKPT letter has its fricative realization.
- **Operation:** Treat rafe as an explicit fricative cue.
- **Result IPA:** None
- **Source:** T1_1.md §I.1.11 (lines 1071–1073)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-BGDKPT-KAF-002']
- **Examples:** no example in source

### TH-BGDKPT-PE-T1-001: Pe with dagesh

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** BGDKPT / letter realization
- **Statement:** פּ is a unvoiced aspirated bilabial stop [pʰ].
- **Conditions:** The letter bears dagesh.
- **Operation:** Realize פּ as [pʰ].
- **Result IPA:** pʰ
- **Source:** T1_1.md §I.1.17 (lines 1225–1231)
- **Certainty:** high
- **Examples:** no example in source

### TH-BGDKPT-PE-T1-002: Pe without dagesh

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** BGDKPT / letter realization
- **Statement:** פ, ף is a unvoiced labio-dental fricative [f].
- **Conditions:** The letter lacks dagesh and is not geminated.
- **Operation:** Realize פ, ף as [f].
- **Result IPA:** f
- **Source:** T1_1.md §I.1.17 (lines 1225–1231)
- **Certainty:** high
- **Examples:** no example in source

### TH-BGDKPT-PE-T1-003: Rafe on fricative pe

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** orthographic cue / rafe
- **Statement:** Fricative pe is frequently, but not regularly, marked with rafe.
- **Conditions:** The BGDKPT letter has its fricative realization.
- **Operation:** Treat rafe as an explicit fricative cue.
- **Result IPA:** None
- **Source:** T1_1.md §I.1.17 (lines 1229–1231)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-BGDKPT-PE-002']
- **Examples:** no example in source

### TH-BGDKPT-T3-001: BGDKPT cross-word sandhi

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** sandhi / bgdkpt
- **Statement:** A word-initial בגדכפת after a vowel is fricative after a conjunctive accent or maqqef, but plosive after a disjunctive accent.
- **Conditions:** A word-initial בגדכפת follows a vowel-final word.
- **Operation:** Select fricative after conjunctive/maqqef; select stop after disjunctive.
- **Result IPA:** v ʁ ð χ f θ / b g d kʰ pʰ tʰ
- **Source:** T1_3B.md §I.3.1.10 (lines 305–317)
- **Certainty:** high
- **Examples:**
  - `שְׁלֹשָׁ֣ה בָנִ֑ים` → `ʃaloːˈʃɔː vɔːˈniːim` (Gen. 6.10)

### TH-BGDKPT-T3-002: Paseq blocks fricative sandhi

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** sandhi / bgdkpt-exception
- **Statement:** Paseq after a conjunctive accent causes the following word-initial בגדכפת to be plosive.
- **Conditions:** A conjunctively accented vowel-final word is followed by paseq.
- **Operation:** Select the stop allophone.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.10 (lines 317–323)
- **Certainty:** high
- **Examples:**
  - `עָשׂ֣וּ׀ כָּלָ֑ה` → `—` (Gen. 18.21)

### TH-BGDKPT-T3-003: Consonantal vav blocks fricative sandhi

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** sandhi / bgdkpt-exception
- **Statement:** After consonantal vav, following word-initial בגדכפת is normally plosive.
- **Conditions:** The preceding word ends in consonantal vav.
- **Operation:** Select the stop allophone.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.10 (lines 325–335)
- **Certainty:** high
- **Examples:** no example in source

### TH-BGDKPT-T3-004: Consonantal yod blocks fricative sandhi

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** sandhi / bgdkpt-exception
- **Statement:** After consonantal yod, following word-initial בגדכפת is normally plosive.
- **Conditions:** The preceding word ends in consonantal yod.
- **Operation:** Select the stop allophone.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.10 (lines 337–347)
- **Certainty:** high
- **Examples:** no example in source

### TH-BGDKPT-T3-005: Avoid adjacent fricative bet/kaf onsets

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** sandhi / bgdkpt-exception
- **Statement:** When two bet or kaf consonants occur in successive onsets in one foot and the first is a shewa-bearing prepositional affix, make the first plosive.
- **Conditions:** Two bet/kaf consonants occur successively.; The first is a prepositional affix with vocalic shewa.
- **Operation:** Select stop for the first bet/kaf.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.10 (lines 349–377)
- **Certainty:** high
- **Examples:**
  - `בְּבִגְד֛וֹ` → `(ba.viʁ.)(ˈdoː)` (Gen. 39.12)

### TH-BGDKPT-T3-006: Bet before pe onset dissimilation

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** sandhi / bgdkpt-exception
- **Statement:** A shewa-bearing prepositional bet before fricative pe is plosive in the specified sandhi context.
- **Conditions:** Prepositional bet has shewa.; It is followed by pe.; A vowel-final conjunctively accented word precedes.
- **Operation:** Select stop [b] for the preposition.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.10 (lines 379–393)
- **Certainty:** high
- **Examples:** no example in source

### TH-BGDKPT-T3-007: Seven lexical BGDKPT sandhi exceptions

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** sandhi / bgdkpt-lexical-exceptions
- **Statement:** Seven transmitted phrases have plosive word-initial BGDKPT despite not fitting the productive exceptions.
- **Conditions:** The phrase is one of the seven Masoretically listed cases.
- **Operation:** Preserve the listed stop pronunciation.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.10 (lines 395–409)
- **Certainty:** high
- **Examples:**
  - `גָאֹ֣ה גָּאָ֔ה` → `—` (Exod. 15.1, 21)
  - `מִ֥י כָּמֹ֖כָה` → `—` (Exod. 15.11)

### TH-BGDKPT-T3-008: Ben Asher–Ben Naftali BGDKPT variants

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** sandhi / masoretic-variation
- **Statement:** Preserve source-specific Ben Asher and Ben Naftali stop/fricative readings rather than generalizing them into the base sandhi rule.
- **Conditions:** The locus is listed as a Ben Asher–Ben Naftali disagreement.
- **Operation:** Choose the reading associated with the selected Masoretic authority.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.10 (lines 411–453)
- **Certainty:** high
- **Notes:** Ben Naftali generally prefers clearer separation by dagesh in these cases.
- **Examples:** no example in source

### TH-BGDKPT-TAV-T1-001: Tav with dagesh

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** BGDKPT / letter realization
- **Statement:** תּ is a unvoiced aspirated alveolar stop [tʰ].
- **Conditions:** The letter bears dagesh.
- **Operation:** Realize תּ as [tʰ].
- **Result IPA:** tʰ
- **Source:** T1_1.md §I.1.23 (lines 1487–1493)
- **Certainty:** high
- **Examples:** no example in source

### TH-BGDKPT-TAV-T1-002: Tav without dagesh

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** BGDKPT / letter realization
- **Statement:** ת is a unvoiced alveolar fricative [θ].
- **Conditions:** The letter lacks dagesh and is not geminated.
- **Operation:** Realize ת as [θ].
- **Result IPA:** θ
- **Source:** T1_1.md §I.1.23 (lines 1487–1493)
- **Certainty:** high
- **Examples:** no example in source

### TH-BGDKPT-TAV-T1-003: Rafe on fricative tav

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** orthographic cue / rafe
- **Statement:** Fricative tav is frequently, but not regularly, marked with rafe.
- **Conditions:** The BGDKPT letter has its fricative realization.
- **Operation:** Treat rafe as an explicit fricative cue.
- **Result IPA:** None
- **Source:** T1_1.md §I.1.23 (lines 1491–1493)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-BGDKPT-TAV-002']
- **Examples:** no example in source

### TH-CON-ALEF-T1-006: Rafe on silent alef

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** orthographic cue / alef rafe
- **Statement:** Rafe may mark א with no consonantal realization and is regular in L on silent א between vowels.
- **Conditions:** א is written but not read.
- **Operation:** Suppress [ʔ].
- **Result IPA:** None
- **Source:** T1_1.md §I.1.1 (lines 179–193)
- **Certainty:** high
- **Examples:**
  - `פּתָֿאֿיִ֣ם` → `—` (Psa. 116.6)
  - `עֳ֜פָֿאֿיִ֗ם` → `—` (Psa. 104.12)

### TH-CON-HE-T1-002: Final mappiq he

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** orthographic cue / mappiq
- **Statement:** Mappiq on final ה marks consonantal [h], distinguishing it from a vowel letter.
- **Conditions:** Word-final ה bears mappiq.
- **Operation:** Pronounce final ה as [h].
- **Result IPA:** h
- **Source:** T1_1.md §I.1.5 (lines 371–373)
- **Certainty:** high
- **Examples:**
  - `לָהּ` → `lɔːɔh` (uncited)
  - `מַלְכָּה` → `malkʰɔː` (uncited)

### TH-CON-HE-T1-003: Nonfinal consonantal he cues

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** orthographic cue / he distribution
- **Statement:** A vowel sign, following vowel letter, or coda shewa identifies nonfinal consonantal ה.
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Retain [h].
- **Result IPA:** h
- **Source:** T1_1.md §I.1.5 (lines 373–373)
- **Certainty:** high
- **Examples:**
  - `פְּדַהְאֵ֖ל` → `pʰaðahˈʔeːel` (Num. 34.28)

### TH-CON-HE-T1-004: Unvocalized medial he as mater

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** orthographic cue / mater lectionis
- **Statement:** Medial ה without a vocalization sign or following vowel letter is a vowel letter, not [h].
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Suppress consonantal [h].
- **Result IPA:** None
- **Source:** T1_1.md §I.1.5 (lines 373–373)
- **Certainty:** high
- **Examples:**
  - `פְּדָהצֽוּר` → `pʰaðɔːˈsˁuːurˁ` (Num. 1.10)

### TH-CON-INV-T1-001: Inventory phoneme /ʔ/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /ʔ/ has allophone(s) [ʔ] and orthography א.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** ʔ
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-002: Inventory phoneme /b/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /b/ has allophone(s) [b] and orthography בּ.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** b
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-003: Inventory phoneme /v/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /v/ has allophone(s) [v] and orthography ב. See I.1.25.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** v
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-004: Inventory phoneme /g/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /g/ has allophone(s) [g] and orthography גּ.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** g
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-005: Inventory phoneme /ʁ/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /ʁ/ has allophone(s) [ʁ] and orthography ג. See I.1.25.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** ʁ
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-006: Inventory phoneme /d/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /d/ has allophone(s) [d] and orthography דּ.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** d
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-007: Inventory phoneme /ð/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /ð/ has allophone(s) [ð] and orthography ד. See I.1.25.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** ð
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-008: Inventory phoneme /h/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /h/ has allophone(s) [h] and orthography ה.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** h
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-009: Inventory phoneme /v/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /v/ has allophone(s) [v], [w] and orthography ו. Allophones vary across sub-traditions.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** v, w
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-010: Inventory phoneme /z/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /z/ has allophone(s) [z] and orthography ז.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** z
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-011: Inventory phoneme /ħ/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /ħ/ has allophone(s) [ħ] and orthography ח.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** ħ
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-012: Inventory phoneme /tˁ/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /tˁ/ has allophone(s) [tˁ] and orthography ט.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** tˁ
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-013: Inventory phoneme /j/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /j/ has allophone(s) [j], [ɟ] and orthography י. [ɟ] occurs only when geminated.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** j, ɟ
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-014: Inventory phoneme /kʰ/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /kʰ/ has allophone(s) [kʰ] and orthography כּ, ךּ.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** kʰ
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-015: Inventory phoneme /χ/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /χ/ has allophone(s) [χ] and orthography כ, ך. See I.1.25.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** χ
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-016: Inventory phoneme /l/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /l/ has allophone(s) [l] and orthography ל.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** l
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-017: Inventory phoneme /m/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /m/ has allophone(s) [m] and orthography מ, ם.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** m
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-018: Inventory phoneme /n/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /n/ has allophone(s) [n] and orthography נ, ן.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** n
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-019: Inventory phoneme /s/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /s/ has allophone(s) [s] and orthography ס, שׂ. Equivalent orally; spelling distinction is archaic.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** s
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-020: Inventory phoneme /ʕ/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /ʕ/ has allophone(s) [ʕ] and orthography ע.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** ʕ
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-021: Inventory phoneme /pʰ/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /pʰ/ has allophone(s) [pʰ] and orthography פּ.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** pʰ
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-022: Inventory phoneme /pˁ/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /pˁ/ has allophone(s) [pˁ] and orthography פּ. Only in אַפַּדְנ֔וֹ; not environmentally conditioned.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** pˁ
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-023: Inventory phoneme /f/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /f/ has allophone(s) [f] and orthography פ. See I.1.25.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** f
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-024: Inventory phoneme /sˁ/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /sˁ/ has allophone(s) [sˁ], [zˁ] and orthography צ. Voiced variant in I.1.7.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** sˁ, zˁ
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-025: Inventory phoneme /q̟/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /q̟/ has allophone(s) [q̟] and orthography ק.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** q̟
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-026: Inventory phoneme /r/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /r/ has allophone(s) [ʀ̟], [rˁ] and orthography ר. Environmentally conditioned.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** ʀ̟, rˁ
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-027: Inventory phoneme /ʃ/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /ʃ/ has allophone(s) [ʃ] and orthography שׁ.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** ʃ
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-028: Inventory phoneme /tʰ/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /tʰ/ has allophone(s) [tʰ] and orthography תּ.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** tʰ
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-INV-T1-029: Inventory phoneme /θ/

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** phoneme inventory / consonant phoneme
- **Statement:** /θ/ has allophone(s) [θ] and orthography ת. See I.1.25.
- **Conditions:** Inventory-level representation.
- **Operation:** Register the listed phoneme, allophones, and orthography.
- **Result IPA:** θ
- **Source:** T1_1.md §I.1.24 (lines 1525–1557)
- **Certainty:** high
- **Examples:** no example in source

### TH-CON-PE-T1-003: Exceptional emphatic pe in appadno

- **Status:** rule
- **Authority:** non-standard-tiberian
- **Category:** lexical exception / pe
- **Statement:** The geminated pe of אַפַּדְנ֔וֹ is unaspirated pharyngealized /pˁ/, not ordinary [pʰ].
- **Conditions:** The fixed word אַפַּדְנ֔וֹ (Dan. 11.45) is read.
- **Operation:** Use geminated emphatic unaspirated pe.
- **Result IPA:** pˁ
- **Source:** T1_1.md §I.1.17 (lines 1269–1297)
- **Certainty:** high
- **Examples:**
  - `אַפַּדְנ֔וֹ` → `—` (Dan. 11.45)

### TH-CON-RESH-T1-002: Resh after an adjacent alveolar

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** allophony / resh
- **Statement:** Resh is pharyngealized apico-alveolar [rˁ] immediately after an alveolar.
- **Conditions:** Preceding ד ז צ ת ט ס ל נ, or equivalent שׂ, immediately contacts ר.
- **Operation:** Replace default [ʀ̟] with [rˁ].
- **Result IPA:** rˁ
- **Source:** T1_1.md §I.1.20 (lines 1403–1405)
- **Certainty:** high
- **Examples:**
  - `בְּמִזְרֶ֖ה` → `bamizˈrˁɛː` (Jer. 15.7)
  - `מַצְרֵ֣ף` → `mɑsˁˈrˁeːef` (Prov. 17.3)

### TH-CON-RESH-T1-003: Resh in a foot with preceding alveolar

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** allophony / resh
- **Statement:** Resh is [rˁ] in the same prosodic foot as a preceding alveolar.
- **Conditions:** Preceding ד ז צ ת ט ס ל נ or שׂ shares the prosodic foot with ר.
- **Operation:** Replace [ʀ̟] with [rˁ].
- **Result IPA:** rˁ
- **Source:** T1_1.md §I.1.20 (lines 1407–1407)
- **Certainty:** high
- **Examples:**
  - `דַּרְכּ֖וֹ` → `dɑrˁˈkʰoː` (Gen. 24.21)
  - `טַרְפֵּ֤י` → `tˁɑrˁˈpʰeː` (Ezek. 17.9)
  - `שַׂר` → `sɑrˁ` (1 Sam. 18.13)
  - `לִמְטַ֥ר` → `limˈtˁɑːɑrˁ` (Deut. 11.11)
  - `צְרוּפָ֔ה` → `sˁɑ.rˁuː.ˈfɔː` (2 Sam. 22.31)

### TH-CON-RESH-T1-004: Resh before lamed or nun

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** allophony / resh
- **Statement:** Resh is [rˁ] in immediate contact with, or in the same syllable/foot as, following ל or נ.
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Replace [ʀ̟] with [rˁ].
- **Result IPA:** rˁ
- **Source:** T1_1.md §I.1.20 (lines 1409–1409)
- **Certainty:** high
- **Examples:**
  - `עַרְלֵי־לֵֽב` → `ʕɑrˁleː-leːev` (Jer. 9.25)
  - `גָּרְנִ֑י` → `gɔrˁniː` (Isa. 21.10)
  - `רַנְּנ֣וּ` → `rˁɑnnaˈnuː` (Psa. 33.1)
  - `רְנָנָ֣ה` → `rˁɑnɔːˈnɔː` (Job 3.7)

### TH-CON-RESH-T1-006: Sin triggers emphatic resh

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** allophony / resh trigger
- **Statement:** Sin [s] conditions [rˁ] exactly like samekh in the applicable environments.
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Add שׂ to the alveolar trigger set.
- **Result IPA:** rˁ
- **Source:** T1_1.md §I.1.20 (lines 1413–1413)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-CON-RESH-002', 'TH-CON-RESH-003', 'TH-CON-SIN-002']
- **Examples:**
  - `שַׂר` → `sɑrˁ` (1 Sam. 18.13)

### TH-CON-SIN-T1-002: Sin equals samekh

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** phoneme identity / sin-samekh
- **Statement:** Sin and samekh are both [s]; written sin was treated as having samekh as qere.
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Map both spellings to [s].
- **Result IPA:** s
- **Source:** T1_1.md §I.1.21 (lines 1439–1441)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-CON-SIN-001', 'TH-CON-SAMEKH-001']
- **Examples:** no example in source

### TH-CON-VAV-T1-003: Conjunctive vav with shewa

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** morphophonology / conjunction
- **Statement:** Initial conjunctive וְ is labio-dental like bet rafe.
- **Conditions:** Word-initial conjunctive ו bears shewa.
- **Operation:** Use [v] as the onset.
- **Result IPA:** v
- **Source:** T1_1.md §I.1.6 (lines 627–627)
- **Certainty:** high
- **Examples:**
  - `וְאָמַר` → `vɔʔɔːˈmaːaʀ̟` (uncited)

### TH-CON-VAV-T1-004: Conjunctive shureq

- **Status:** rule
- **Authority:** comparative
- **Category:** morphophonology / conjunction
- **Statement:** Conjunctive וּ is [wu], not [ʔuː], before ב מ פ or a consonant with silent shewa.
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Use [w] onset plus short [u].
- **Result IPA:** wu
- **Source:** T1_1.md §I.1.6 (lines 629–655)
- **Certainty:** high
- **Examples:**
  - `וּלְנֶכְדִּ֑י` → `—` (Gen. 21.23)

### TH-CON-VAV-T1-005: Gaʿya-lengthened conjunctive wu

- **Status:** rule
- **Authority:** comparative
- **Category:** prosody / conjunction
- **Statement:** Gaʿya lengthens conjunctive [wu] to [wuˑ].
- **Conditions:** Initial conjunctive וּ bears minor or phonetic gaʿya.
- **Operation:** Lengthen [u] to [uˑ], retaining [w].
- **Result IPA:** wuˑ
- **Source:** T1_1.md §I.1.6 (lines 697–707)
- **Certainty:** high
- **Examples:**
  - `וּֽלְהַעֲלֹתוֹ֮` → `wuˑ` (Exod. 3.8)

### TH-DAG-T3-006: Morphological-pattern gemination

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** morphology / gemination
- **Statement:** Geminate a consonant when gemination belongs to the word's morphological pattern, typically the second root radical.
- **Conditions:** The morphological pattern specifies a doubled radical.
- **Operation:** Geminate the specified radical.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.2 (lines 71–79)
- **Certainty:** high
- **Examples:**
  - `בִּקֵּשׁ` → `—`
  - `גַּנָּב` → `—`

### TH-DAG-T3-007: Inherent final-radical gemination

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** morphology / geminate-roots
- **Statement:** Identical final radicals surface as one geminated consonant when adjacent before an affix.
- **Conditions:** The final two root radicals are identical.; An affix makes them adjacent in non-final position.
- **Operation:** Coalesce the radicals and geminate the resulting consonant.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.2 (lines 73–79)
- **Certainty:** high
- **Examples:**
  - `עַמִּים` → `—`
  - `עַם` → `—`

### TH-DAG-T3-008: Contextual gemination distinguishes homophones

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** morphology / semantic-gemination
- **Statement:** Gemination may distinguish otherwise homophonous forms, contextually or as a permanent morphological feature.
- **Conditions:** Two forms would otherwise be homophonous.; The transmitted form bears dagesh.
- **Operation:** Geminate the marked consonant.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.3 (lines 81–91)
- **Certainty:** high
- **Examples:**
  - `לֹּ֥א ל֖וֹ` → `ˈlloː ˈloː` (Gen. 38.9)

### TH-DAG-T3-009: Lexical semantic gemination

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** morphology / semantic-gemination
- **Statement:** In specified lexical pairs, gemination is a permanent morphological distinction of meaning.
- **Conditions:** The word belongs to an attested contrastive lexical pair.
- **Operation:** Preserve the lexically specified gemination.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.3 (lines 89–93)
- **Certainty:** high
- **Examples:**
  - `יָנִיחַ / יַנִּיחַ` → `—`
  - `עֲצָבִים / עֲצַבִּים` → `—`

### TH-DAG-T3-010: אָנָּה contrastive gemination

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** lexicon / semantic-gemination
- **Statement:** The interjection אָנָּה has geminate nun, distinguishing it from אָנָה 'to where?'.
- **Conditions:** Lexeme is the interjection אָנָּה/אָנָּא.
- **Operation:** Geminate nun.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.3 (lines 91–131)
- **Certainty:** medium
- **Examples:**
  - `אָֽנָּ֤א` → `—` (Neh. 1.5)

### TH-DAG-T3-011: Assimilatory gemination

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** phonology / assimilation
- **Statement:** At consonant contact, one consonant may assimilate to the other and surface as gemination, often at a stem-affix boundary.
- **Conditions:** Two consonants come into contact.; The transmitted form reflects assimilation.
- **Operation:** Assimilate one consonant to its neighbor and geminate.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.4 (lines 165–177)
- **Certainty:** high
- **Examples:**
  - `יִפֹּ֫ל` → `jip-ˈpʰoːol`
  - `מִשָּׁ֫ם` → `miʃ-ˈʃɔːɔm`

### TH-DAG-T3-015: Stress-associated final gemination

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** prosody / stress-gemination
- **Statement:** In a few verbal forms, geminate a final sonorant radical between preceding main stress and a following inflectional suffix.
- **Conditions:** The radical is a final sonorant.; Main stress immediately precedes it.; An inflectional suffix follows.
- **Operation:** Geminate the final radical.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.7 (lines 245–255)
- **Certainty:** high
- **Examples:**
  - `חָדֵ֑לּוּ` → `—` (Jud. 5.7)

### TH-DAG-T3-016: Prefix-boundary gemination

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** morphology / prefix-gemination
- **Statement:** Certain prefixed particles trigger gemination of the stem-initial consonant.
- **Conditions:** An attested prefix and stem meet at a morphological boundary.
- **Operation:** Geminate the stem-initial consonant.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.8 (lines 257–269)
- **Certainty:** high
- **Examples:**
  - `בַּמָּ֫ה` → `—`
  - `כַּמָּ֫ה` → `—`

### TH-DAG-T3-017: לָמָּה stress-sensitive gemination

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** prosody / lexical-gemination
- **Statement:** לָמָּה normally has geminate mem when stress is on the preceding syllable; final-stress variants can lack gemination.
- **Conditions:** Lexeme is לָמָּה.; Stress is non-final or the word is joined by maqqef.
- **Operation:** Geminate mem.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.8 (lines 267–271)
- **Certainty:** high
- **Examples:**
  - `לָמָּה־` → `—` (Prov. 17.16)

### TH-DAG-T3-018: Wayyiqṭol prefix gemination

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** morphology / prefix-gemination
- **Statement:** The prefix consonant in wayyiqṭol is geminated; the gemination may also distinguish the form semantically from weyiqṭol.
- **Conditions:** The form is וַיִּקְטֹל.
- **Operation:** Geminate the prefixed imperfect consonant.
- **Result IPA:** vaɟɟiq̟ˈtˁoːol
- **Source:** T1_3B.md §I.3.1.8 (lines 269–271)
- **Certainty:** medium
- **Examples:**
  - `וַיִּקְטֹ֫ל` → `vaɟɟiq̟ˈtˁoːol`

### TH-DAG-T3-019: Interrogative he marks boundary by gemination

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** morphology / interrogative-prefix
- **Statement:** Interrogative he may trigger gemination of a following consonant when the following word begins with shewa.
- **Conditions:** Interrogative ה precedes a word beginning with shewa.; The transmitted form marks dagesh.
- **Operation:** Geminate the following consonant.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.8 (lines 273–281)
- **Certainty:** high
- **Examples:**
  - `הַכְּצַעֲקָתָ֛הּ` → `hakkʰɑsˁɑːʕɑq̟ɔːˈθɔːh` (Gen. 18.21)

### TH-DAG-T3-021: Deḥiq word-boundary gemination

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** sandhi / dehiq
- **Statement:** Deḥiq geminates a word-initial consonant after an unstressed final vowel in a closely connected preceding word.
- **Conditions:** The preceding word ends in an unstressed vowel.; The words form a close prosodic unit.
- **Operation:** Geminate the following word-initial consonant.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.9 (lines 291–303)
- **Certainty:** high
- **Examples:**
  - `תַּעֲשֶׂה־לְּךָ֣` → `—` (Prov. 24.6)

### TH-DAG-T3-022: Deḥiq preserves reduced long vowel

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** sandhi / dehiq
- **Statement:** The vowel before deḥiq gemination remains long but has compressed duration.
- **Conditions:** Deḥiq applies.
- **Operation:** Retain vowel length while reducing its duration.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.9 (lines 299–303)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-DAG-021']
- **Examples:** no example in source

### TH-DAG-T3-023: Orthoepic gemination prevents slurring

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** orthoepy / dagesh
- **Statement:** Dagesh may introduce gemination to preserve clear articulation and syllable division.
- **Conditions:** A transmitted orthoepic dagesh occurs in a vulnerable consonant sequence.
- **Operation:** Geminate the marked consonant.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.11 (lines 455–461)
- **Certainty:** high
- **Examples:** no example in source

### TH-DAG-T3-024: Gemination vocalizes shewa between weak consonants

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** orthoepy / weak-consonant-separation
- **Statement:** When weak consonants contact across a syllable boundary, geminating the first can make its shewa vocalic and separate the consonants.
- **Conditions:** Two vulnerable consonants contact across a syllable boundary.; The first bears orthoepic dagesh.
- **Operation:** Geminate the first consonant and realize its shewa vocally.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.11.1 (lines 459–487)
- **Certainty:** high
- **Examples:**
  - `מִקְּרֵה־לָ֑יְלָה` → `miq̟q̟aʀ̟eː-ˈlɔːɔjlɔː` (Deut. 23.11)

### TH-DAG-T3-025: Orthoepic CVCC restructuring

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** orthoepy / epenthesis
- **Statement:** A rare orthoepic strategy restructures CC as CVCC by inserting a vowel and geminating the second consonant.
- **Conditions:** The transmitted exceptional form יִֽרַדֹּף is read.
- **Operation:** Apply CC > CVCC.
- **Result IPA:** jiːṛaddoːof
- **Source:** T1_3B.md §I.3.1.11.1 (lines 489–495)
- **Certainty:** high
- **Examples:**
  - `יִֽרַדֹּ֥ף` → `jiːṛaddoːof` (Psa. 7.6)

### TH-DAG-T3-026: Dagesh strengthens syllable onset

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** orthoepy / onset-strengthening
- **Statement:** Orthoepic dagesh on the second of contacting consonants strengthens the onset and marks a clear syllable boundary.
- **Conditions:** Two consonants contact across a syllable or word boundary.; The second bears orthoepic dagesh.
- **Operation:** Geminate/fortify the onset consonant.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.11.2 (lines 497–507)
- **Certainty:** high
- **Examples:**
  - `וַיִּתֶּן־לּ֖וֹ` → `—` (Gen. 24.36)

### TH-DAG-T3-027: Dagesh disambiguates syllabification

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** orthoepy / syllabification
- **Statement:** In the Ben Naftali reading of יַעְקֹב 'he supplants', dagesh in qof marks gemination, clear syllable division, and silent shewa under ayin.
- **Conditions:** Following the attributed Ben Naftali reading of Jer. 9.3.
- **Operation:** Geminate qof and interpret preceding shewa as silent.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.11.2 (lines 505–511)
- **Certainty:** high
- **Examples:**
  - `יַעְקֹּ֔ב` → `—` (Jer. 9.3)

### TH-DAG-T3-028: Compensatory lengthening after guttural degemination

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** phonology / loss-of-gemination
- **Statement:** Historical gemination of gutturals, and often resh, is lost with compensatory lengthening of the preceding vowel.
- **Conditions:** A weak guttural or resh historically bore gemination.
- **Operation:** Degeminate the consonant and lengthen the preceding vowel.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.13.1 (lines 685–701)
- **Certainty:** high
- **Examples:**
  - `הָאָדָ֫ם` → `hɔːʔɔːˈðɔːɔm`

### TH-DAG-T3-029: Degemination of weak consonants with shewa

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** phonology / loss-of-gemination
- **Statement:** Weak consonants with shewa may lose gemination because both the consonant and shewa syllable are weak.
- **Conditions:** The consonant is especially a sibilant, yod, lamed, mem, nun, or qof.; It bears shewa.
- **Operation:** Remove gemination.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.13.2 (lines 703–717)
- **Certainty:** high
- **Examples:** no example in source

### TH-DAG-T3-030: No-compensation weak degemination

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** phonology / loss-of-gemination
- **Statement:** After weak-consonant degemination without compensation, the consonant closes the preceding syllable.
- **Conditions:** Weak shewa-bearing consonant loses gemination.; No gaʿya/lengthening is transmitted.
- **Operation:** Keep the preceding vowel short and resyllabify the consonant as coda.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.13.2 (lines 705–711)
- **Certainty:** high
- **Examples:**
  - `הַלְוִיִּ֖ם` → `—` (Exod. 6.25)

### TH-DAG-T3-031: Compensated weak degemination

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** phonology / loss-of-gemination
- **Statement:** When weak-consonant degemination is compensated, lengthen the preceding vowel and retain vocalic shewa.
- **Conditions:** Weak shewa-bearing consonant loses gemination.; Lengthening is indicated, generally by gaʿya.
- **Operation:** Lengthen the preceding vowel and realize shewa vocally.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.13.2 (lines 713–717)
- **Certainty:** high
- **Examples:**
  - `הַֽמְדַבֵּ֥ר` → `—` (Gen. 45.12)

### TH-DAG-T3-032: Avoid adjacent geminates

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** phonology / loss-of-gemination
- **Statement:** A prosodically weak consonant may lose gemination immediately before another geminate, avoiding a clash of strengthened consonants.
- **Conditions:** A geminated consonant would immediately precede another geminate.; The first is in an unstressed onset, often a weak consonant.
- **Operation:** Degeminate the first consonant.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.13.3 (lines 719–739)
- **Certainty:** high
- **Examples:**
  - `מַה־מַשָּׂ֖א` → `—` (Jer. 23.33)

### TH-GUTT-AYIN-T1-002: Lengthening protects ʿayin

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** orthoepy / guttural protection
- **Statement:** A preceding vowel may be lengthened to preserve vulnerable [ʕ].
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Lengthen the preceding vowel and retain [ʕ].
- **Result IPA:** None
- **Source:** T1_1.md §I.1.16 (lines 1191–1193)
- **Certainty:** high
- **Examples:**
  - `שְׁמַֽעְיָ֥הוּ` → `ʃaˌmaˑʕˈjɔːhuː` (2 Chron. 11.2)
  - `שְׁמַֽע־נָ֤א` → `ʃaˌmaˑʕ-ˈnɔː` (1 Sam. 28.22)

### TH-GUTT-HET-T1-002: Lengthening protects ḥet

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** orthoepy / guttural protection
- **Statement:** A preceding vowel may be lengthened to protect vulnerable [ħ].
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Lengthen the preceding vowel and retain [ħ].
- **Result IPA:** None
- **Source:** T1_1.md §I.1.8 (lines 925–927)
- **Certainty:** high
- **Examples:**
  - `וּפְתַֽחְיָ֨ה` → `wufˌθaˑḥˈjɔː` (Neh. 11.24)
  - `מִֽחְיָ֥ה` → `ˌmiˑḥˈjɔː` (Ezra 9.8)

### TH-LEN-T2-016: Specified length: qameṣ /ɔ̄/

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** phonology / specified-length
- **Statement:** qameṣ /ɔ̄/ includes a length feature in its underlying representation.
- **Conditions:** qameṣ /ɔ̄/
- **Operation:** Represent underlying vowel with specified length.
- **Result IPA:** /ɔ̄/
- **Source:** T1_2B_corrected_p352.md §I.2.3.1. Vowel Phonemes with a Specified Length Feature (lines 464–476)
- **Certainty:** high
- **Examples:**
  - `שָׁתָ֫ה` → `ʃɔːˈθɔː`

### TH-LEN-T2-017: Specified length: ḥolem /ō/

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** phonology / specified-length
- **Statement:** ḥolem /ō/ includes a length feature in its underlying representation.
- **Conditions:** ḥolem /ō/
- **Operation:** Represent underlying vowel with specified length.
- **Result IPA:** /ō/
- **Source:** T1_2B_corrected_p352.md §I.2.3.1. Vowel Phonemes with a Specified Length Feature (lines 464–476)
- **Certainty:** high
- **Examples:**
  - `בֵּית֫וֹ` → `beːˈθoː`

### TH-LEN-T2-018: Specified length: ṣere /ē/

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** phonology / specified-length
- **Statement:** ṣere /ē/ includes a length feature in its underlying representation.
- **Conditions:** ṣere /ē/
- **Operation:** Represent underlying vowel with specified length.
- **Result IPA:** /ē/
- **Source:** T1_2B_corrected_p352.md §I.2.3.1. Vowel Phonemes with a Specified Length Feature (lines 464–476)
- **Certainty:** high
- **Examples:**
  - `עֵדָ֫ה` → `ʕeːˈðɔː`

### TH-LEN-T2-019: Specified length: long shureq /ū/

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** phonology / specified-length
- **Statement:** long shureq /ū/ includes a length feature in its underlying representation.
- **Conditions:** long shureq /ū/
- **Operation:** Represent underlying vowel with specified length.
- **Result IPA:** /ū/
- **Source:** T1_2B_corrected_p352.md §I.2.3.1. Vowel Phonemes with a Specified Length Feature (lines 464–476)
- **Certainty:** high
- **Examples:**
  - `ק֫וּמוּ` → `ˈq̟uːmuː`

### TH-LEN-T2-020: Specified length: long ḥireq /ī/

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** phonology / specified-length
- **Statement:** long ḥireq /ī/ includes a length feature in its underlying representation.
- **Conditions:** long ḥireq /ī/
- **Operation:** Represent underlying vowel with specified length.
- **Result IPA:** /ī/
- **Source:** T1_2B_corrected_p352.md §I.2.3.1. Vowel Phonemes with a Specified Length Feature (lines 464–476)
- **Certainty:** high
- **Examples:**
  - `יִירָ֫א` → `jiːˈʀ̟ɔː`

### TH-LEN-T2-021: Unspecified length: pataḥ /a/

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** phonology / unspecified-length
- **Statement:** pataḥ /a/ lacks a specified underlying length feature; surface duration is assigned by stress and syllable structure.
- **Conditions:** pataḥ /a/
- **Operation:** Leave length unspecified, then apply surface length rules.
- **Result IPA:** /a/
- **Source:** T1_2B_corrected_p352.md §I.2.3.2. Vowel Phonemes without a Specified Length   (lines 478–491)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-LEN-001', 'TH-LEN-002', 'TH-LEN-003']
- **Examples:**
  - `עָמַ֫ד` → `ʕɔːˈmaːað`

### TH-LEN-T2-022: Unspecified length: segol /ɛ/

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** phonology / unspecified-length
- **Statement:** segol /ɛ/ lacks a specified underlying length feature; surface duration is assigned by stress and syllable structure.
- **Conditions:** segol /ɛ/
- **Operation:** Leave length unspecified, then apply surface length rules.
- **Result IPA:** /ɛ/
- **Source:** T1_2B_corrected_p352.md §I.2.3.2. Vowel Phonemes without a Specified Length   (lines 478–491)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-LEN-001', 'TH-LEN-002', 'TH-LEN-003']
- **Examples:**
  - `לָהֶ֫ם` → `lɔːˈhɛːɛm`

### TH-LEN-T2-023: Unspecified length: ḥireq /i/

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** phonology / unspecified-length
- **Statement:** ḥireq /i/ lacks a specified underlying length feature; surface duration is assigned by stress and syllable structure.
- **Conditions:** ḥireq /i/
- **Operation:** Leave length unspecified, then apply surface length rules.
- **Result IPA:** /i/
- **Source:** T1_2B_corrected_p352.md §I.2.3.2. Vowel Phonemes without a Specified Length   (lines 478–491)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-LEN-001', 'TH-LEN-002', 'TH-LEN-003']
- **Examples:**
  - `מִ֫ן` → `ˈmiːin`

### TH-LEN-T2-024: Unspecified length: qibbuṣ/shureq /u/

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** phonology / unspecified-length
- **Statement:** qibbuṣ/shureq /u/ lacks a specified underlying length feature; surface duration is assigned by stress and syllable structure.
- **Conditions:** qibbuṣ/shureq /u/
- **Operation:** Leave length unspecified, then apply surface length rules.
- **Result IPA:** /u/
- **Source:** T1_2B_corrected_p352.md §I.2.3.2. Vowel Phonemes without a Specified Length   (lines 478–491)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-LEN-001', 'TH-LEN-002', 'TH-LEN-003']
- **Examples:** no example in source

### TH-LEN-T2-025: Unspecified length: stressed ṣere-sign /e/

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** phonology / unspecified-length
- **Statement:** stressed ṣere-sign /e/ lacks a specified underlying length feature; surface duration is assigned by stress and syllable structure.
- **Conditions:** stressed ṣere-sign /e/
- **Operation:** Leave length unspecified, then apply surface length rules.
- **Result IPA:** /e/
- **Source:** T1_2B_corrected_p352.md §I.2.3.2. Vowel Phonemes without a Specified Length   (lines 507–527)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-LEN-001', 'TH-LEN-002', 'TH-LEN-003']
- **Examples:**
  - `לֵ֫ב` → `ˈleːev`

### TH-LEN-T2-026: Unspecified length: stressed ḥolem-sign /o/

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** phonology / unspecified-length
- **Statement:** stressed ḥolem-sign /o/ lacks a specified underlying length feature; surface duration is assigned by stress and syllable structure.
- **Conditions:** stressed ḥolem-sign /o/
- **Operation:** Leave length unspecified, then apply surface length rules.
- **Result IPA:** /o/
- **Source:** T1_2B_corrected_p352.md §I.2.3.2. Vowel Phonemes without a Specified Length   (lines 507–527)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-LEN-001', 'TH-LEN-002', 'TH-LEN-003']
- **Examples:**
  - `עֹ֫ז` → `ˈʕoːoz`

### TH-ORTH-T0-003: Maximal distinctness

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** orthoepy / principle
- **Statement:** Careful reading maximally distinguishes letters, vowels, syllables, and words and avoids slurring.
- **Conditions:** In orthoepic recitation.
- **Operation:** Enhance segmental and prosodic distinctness.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.11 (lines 569–571)
- **Certainty:** high
- **Examples:** no example in source

### TH-ORTH-T0-004: Mah lengthening

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** orthoepy / mah construction
- **Statement:** The common strategy lengthens pataḥ in מַה־ before a dageshed consonant to preserve word distinctness.
- **Conditions:** For this maqqef construction.
- **Operation:** Lengthen pataḥ.
- **Result IPA:** maˑ-ttʰisˁˈʕaːaq̟
- **Source:** T1_0_Intro.md §I.0.11 (lines 591–591)
- **Certainty:** high
- **Examples:**
  - `מַה־תִּצְעַ֖ק` → `maˑ-ttʰisˁˈʕaːaq̟` (I.0.11 line 591)

### TH-ORTH-T0-005: Mah h insertion

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** orthoepy / mah construction
- **Statement:** An alternative pronounces [h] after pataḥ in מַה־, separating it from the following word.
- **Conditions:** For this maqqef construction.
- **Operation:** Insert [h].
- **Result IPA:** mah-ʃʃaˈmoː
- **Source:** T1_0_Intro.md §I.0.11 (lines 591–591)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-ORTH-004']
- **Examples:**
  - `מַה־שְּׁמ֔וֹ` → `mah-ʃʃaˈmoː` (I.0.11 line 591)

### TH-ORTH-T0-006: Bin-Nun strengthening

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** orthoepy / adjacent consonants
- **Statement:** Ben Naftali strengthens the second nun in בִּן־נּוּן to prevent coalescence across the word boundary.
- **Conditions:** In this name sequence.
- **Operation:** Geminate/strengthen the onset nun.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.11 (lines 593–593)
- **Certainty:** high
- **Examples:**
  - `בִּן־נּוּן` → `—` (I.0.11 line 593)

### TH-ORTH-T0-007: Yaʿqov dagesh

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** orthoepy / shewa disambiguation
- **Statement:** Ben Naftali puts dagesh in qof of יַעְקֹב to ensure preceding shewa is silent and distinguish the verb from the name.
- **Conditions:** For this verb in his stream.
- **Operation:** Strengthen qof and suppress the shewa vowel.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.11 (lines 595–595)
- **Certainty:** high
- **Examples:**
  - `יַעְקֹּ֔ב / יַעֲקֹב` → `—` (I.0.11 line 595)

### TH-ORTH-T0-008: Hayah prefix lengthening

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** orthoepy / guttural preservation
- **Statement:** Lengthen the prefix vowel of הָיָה to prevent weakening of its guttural and preserve lexical contrast.
- **Conditions:** In cited prefix forms.
- **Operation:** Lengthen the prefix vowel.
- **Result IPA:** tʰiˑhjɛː
- **Source:** T1_0_Intro.md §I.0.11 (lines 597–597)
- **Certainty:** high
- **Examples:**
  - `תִּהְיֶ֥ה` → `tʰiˑhjɛː` (I.0.11 line 597)

### TH-ORTH-T0-009: Ḥayah prefix lengthening

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** orthoepy / guttural preservation
- **Statement:** Lengthen the prefix vowel of חָיָה to prevent weakening of its guttural and preserve lexical contrast.
- **Conditions:** In cited prefix forms.
- **Operation:** Lengthen the prefix vowel.
- **Result IPA:** jiˑħjɛː
- **Source:** T1_0_Intro.md §I.0.11 (lines 597–597)
- **Certainty:** high
- **Examples:**
  - `יִחְיֶ֑ה` → `jiˑħjɛː` (I.0.11 line 597)

### TH-RAF-T3-005: Rafe distinguishes non-wayyiqṭol prefixes

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** morphology / rafe-contrast
- **Statement:** Rafe on an imperfect prefix after vav with shewa marks the prefix as ungeminated, distinguishing it from wayyiqṭol.
- **Conditions:** Vav with shewa precedes an imperfect prefix.; The manuscript marks rafe on the prefix.
- **Operation:** Keep the prefix singleton.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.2 (lines 797–801)
- **Certainty:** high
- **Examples:**
  - `וְיִֿשְׁמַ֖ע` → `—` (Isa. 42.23)

### TH-VAR-BGDKPT-T1-001: BGDKPT free variation

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** BGDKPT / free variation
- **Statement:** A few forms have free variation between plosive and fricative realizations.
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Permit either attested realization.
- **Result IPA:** None
- **Source:** T1_1.md §I.1.25 (lines 1567–1569)
- **Certainty:** high
- **Examples:**
  - `רִשְׁפֵי` → `ʀ̟iʃˈfeː` (Psa. 76.4)
  - `רִשְׁפֵּ֕י` → `ʀ̟iʃˈpʰeː` (Cant. 8.6)

### TH-VAR-DALET-T1-001: Emphatic dalet by spreading

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** assimilation / dalet
- **Statement:** Emphasis from adjacent emphatic pe or resh can produce fricative [ðˁ].
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Spread pharyngealization to [ð].
- **Result IPA:** ðˁ
- **Source:** T1_1.md §I.1.4 (lines 351–355)
- **Certainty:** medium
- **Examples:**
  - `אַפַּדְנ֔וֹ` → `—` (Dan. 11.45)
  - `וַֽיַּדְרְכ֤וּ` → `—` (Jer. 9.2)

### TH-VAR-HE-T1-001: Fixed silent final-he cases

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** lexical exception / final he
- **Statement:** The Masora identifies eighteen fixed cases where expected final consonantal ה is not pronounced.
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Suppress final [h] in listed tokens.
- **Result IPA:** None
- **Source:** T1_1.md §I.1.5 (lines 483–497)
- **Certainty:** high
- **Examples:**
  - `וַתַּחְמְרָ֥ה` → `—` (Exod. 2.3)
  - `עֲוֺנָ֥הֿ` → `—` (Num. 15.31)

### TH-VAR-PE-T1-001: Aspirated appadno variant

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** sub-tradition / pe
- **Statement:** Some Greek transcription streams give aspirated, ungeminated pe in אַפַּדְנ֔וֹ.
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Use ordinary aspirated pe and omit gemination.
- **Result IPA:** pʰ
- **Source:** T1_1.md §I.1.17 (lines 1285–1293)
- **Certainty:** high
- **Examples:**
  - `אַפַּדְנ֔וֹ` → `—` (Dan. 11.45)

### TH-VAR-SADE-T1-001: Voiced ṣade variant

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** assimilation / ṣade
- **Statement:** Ṣade has a voiced emphatic variant [zˁ], associated with adjacent voicing.
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Voice [sˁ] while retaining emphasis.
- **Result IPA:** zˁ
- **Source:** T1_1.md §I.1.7; I.1.18 (lines 853–1323)
- **Certainty:** medium
- **Examples:**
  - `אֲמַצְיָהוּ` → `ʔamazˁˈjɔːhuː` (uncited)

### TH-VAR-SADE-T1-002: Weakened ṣade

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** sub-tradition / ṣade
- **Statement:** A Karaite transcription records non-emphatic [s] for ṣade.
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Remove pharyngealization.
- **Result IPA:** s
- **Source:** T1_1.md §I.1.18 (lines 1323–1327)
- **Certainty:** high
- **Examples:**
  - `וּפֹרֵ֥ץ` → `—` (Ecc. 10.8)

### TH-VAR-SAMEKH-T1-001: Pharyngealized samekh

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** assimilation / samekh
- **Statement:** Samekh may become [sˁ] near a pharyngeal.
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Spread pharyngealization.
- **Result IPA:** sˁ
- **Source:** T1_1.md §I.1.15 (lines 1137–1141)
- **Certainty:** medium
- **Examples:**
  - `פִּנְחָס` → `—` (uncited)

### TH-VAR-SIN-T1-001: Pharyngealized sin

- **Status:** variant
- **Authority:** comparative
- **Category:** assimilation / sin
- **Statement:** Sin can become [sˁ] near pharyngeal or emphatic consonants.
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Spread pharyngealization.
- **Result IPA:** sˁ
- **Source:** T1_1.md §I.1.21 (lines 1471–1479)
- **Certainty:** high
- **Examples:**
  - `וַיִּשְׂטֹ֤ם` → `wajjɪsˁtˁɞːm` (Gen. 27.41)

### TH-VAR-T0-001: Northern diphthong contraction

- **Status:** variant
- **Authority:** comparative
- **Category:** historical phonology / dialect variation
- **Statement:** Northern Hebrew tended to contract diphthongs; southern Judahite Hebrew tended to preserve them.
- **Conditions:** In the northern Israelian dialects.
- **Operation:** Contract a diphthong to a monophthong.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.1 (lines 14–14)
- **Certainty:** high
- **Examples:**
  - `ין` → `—` (I.0.1 line 14)

### TH-VAR-T0-002: Consonant-final suffix variants

- **Status:** evidence
- **Authority:** comparative
- **Category:** morphophonology / suffixes
- **Statement:** Second Temple sources attest vocalic and consonant-final variants of second-person suffixes.
- **Conditions:** For forms written -ך/-כה and -ת/-תה.
- **Operation:** Select the transmitted dialectal suffix form.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.1 (lines 18–24)
- **Certainty:** high
- **Examples:**
  - `-ך/-כה` → `—` (I.0.1 line 20)
  - `-ת/-תה` → `—` (I.0.1 line 20)

### TH-VAR-T0-003: Non-Standard Tiberian definition

- **Status:** variant
- **Authority:** non-standard-tiberian
- **Category:** vocalization / classification
- **Statement:** Non-Standard Tiberian uses Tiberian signs but reflects a non-standard, often Palestinian, pronunciation.
- **Conditions:** For Tiberian-sign manuscripts not following Standard Tiberian values.
- **Operation:** Classify as Non-Standard Tiberian.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.3 (lines 54–56)
- **Certainty:** high
- **Examples:** no example in source

### TH-VAR-T0-004: Aleppo Codex A

- **Status:** evidence
- **Authority:** manuscript
- **Category:** manuscripts / A
- **Statement:** A is a direct Ben Asher witness and agrees with Ben Asher in 94% of recorded disagreements.
- **Conditions:** When weighting model codices.
- **Operation:** Use A as the primary Ben Asher manuscript witness.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.4 (lines 106–108)
- **Certainty:** high
- **Examples:** no example in source

### TH-VAR-T0-005: Leningrad Codex L

- **Status:** variant
- **Authority:** manuscript
- **Category:** manuscripts / L
- **Statement:** L marks fewer non-guttural ḥaṭef signs and slightly more open-syllable gaʿya than A; corrections tend toward A.
- **Conditions:** When comparing L and A.
- **Operation:** Retain L-specific pointing as manuscript variation.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.4 (lines 110–112)
- **Certainty:** high
- **Examples:** no example in source

### TH-VAR-T0-006: British Library Codex B

- **Status:** variant
- **Authority:** manuscript
- **Category:** manuscripts / B
- **Statement:** B marks non-guttural ḥaṭef more than L, open-syllable gaʿya less than A, and non-BGDKPT rafe less than A.
- **Conditions:** When comparing B, L, and A.
- **Operation:** Treat frequencies as manuscript variation.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.4 (lines 114–116)
- **Certainty:** high
- **Examples:** no example in source

### TH-VAR-T0-007: Cairo Codex C

- **Status:** variant
- **Authority:** manuscript
- **Category:** manuscripts / C
- **Statement:** C is Ben Naftali-leaning and more frequently marks open-syllable gaʿya and consonantal-ʾalef dagesh than A and L.
- **Conditions:** When interpreting C.
- **Operation:** Associate these features with C.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.4 (lines 118–120)
- **Certainty:** high
- **Examples:**
  - `לִישְׂרָאֵל` → `—` (I.0.4 line 120)

### TH-VAR-T0-008: Sassoon Codex S

- **Status:** variant
- **Authority:** manuscript
- **Category:** manuscripts / S
- **Statement:** S is mixed between Ben Asher and Ben Naftali, marks more rafe and open-syllable gaʿya, and no non-guttural ḥaṭef.
- **Conditions:** When interpreting S.
- **Operation:** Treat its practices as manuscript-specific.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.4 (lines 122–124)
- **Certainty:** high
- **Examples:**
  - `בִּישְׂרָאֵל` → `—` (I.0.4 line 124)

### TH-VAR-T0-010: Dagesh variation

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** morphophonology / dagesh
- **Statement:** Tiberian preserves the cited internal morphophonemic alternation, generally without semantic significance.
- **Conditions:** In lexically transmitted forms.
- **Operation:** Select the transmitted variant.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.8 (lines 380–380)
- **Certainty:** high
- **Examples:**
  - `יִסֹּ֔ב / יָסֹ֖ב` → `—` (I.0.8 line 380)

### TH-VAR-T0-011: Ḥaṭef variation

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** morphophonology / ḥaṭef
- **Statement:** Tiberian preserves the cited internal morphophonemic alternation, generally without semantic significance.
- **Conditions:** In lexically transmitted forms.
- **Operation:** Select the transmitted variant.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.8 (lines 382–382)
- **Certainty:** high
- **Examples:**
  - `יַחְשֹׁ֔בוּ / יַחֲשֹׁבֽוּן` → `—` (I.0.8 line 382)

### TH-VAR-T0-012: Ḥireq-segol variation

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** morphophonology / vowels
- **Statement:** Tiberian preserves the cited internal morphophonemic alternation, generally without semantic significance.
- **Conditions:** In lexically transmitted forms.
- **Operation:** Select the transmitted variant.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.8 (lines 384–384)
- **Certainty:** high
- **Examples:**
  - `וְהִגְלָ֣ה / הֶגְלָ֖ה` → `—` (I.0.8 line 384)

### TH-VAR-T0-013: Qibbuṣ-qameṣ variation

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** morphophonology / vowels
- **Statement:** Tiberian preserves the cited internal morphophonemic alternation, generally without semantic significance.
- **Conditions:** In lexically transmitted forms.
- **Operation:** Select the transmitted variant.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.8 (lines 386–386)
- **Certainty:** high
- **Examples:**
  - `גֻּדְלֽוֹ / גָּדְל֕וֹ` → `—` (I.0.8 line 386)

### TH-VAR-T0-014: Suffix-context ḥaṭef qameṣ

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** morphophonology / vowel reduction
- **Statement:** Tiberian preserves the cited internal morphophonemic alternation, generally without semantic significance.
- **Conditions:** In lexically transmitted forms.
- **Operation:** Select the transmitted variant.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.8 (lines 388–388)
- **Certainty:** high
- **Examples:**
  - `אֶשְׁתֳּלֶ֔נּוּ` → `—` (I.0.8 line 388)

### TH-VAR-T0-015: Piʿel ṣere-pataḥ variation

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** morphophonology / vowels
- **Statement:** Tiberian preserves the cited internal morphophonemic alternation, generally without semantic significance.
- **Conditions:** In lexically transmitted forms.
- **Operation:** Select the transmitted variant.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.8 (lines 390–390)
- **Certainty:** high
- **Examples:**
  - `גִדֵּ֔ל / גִּדַּ֤ל` → `—` (I.0.8 line 390)

### TH-VAR-T0-016: Pre-guttural piʿel variation

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** morphophonology / vowels
- **Statement:** Tiberian preserves the cited internal morphophonemic alternation, generally without semantic significance.
- **Conditions:** In lexically transmitted forms.
- **Operation:** Select the transmitted variant.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.8 (lines 392–392)
- **Certainty:** high
- **Examples:**
  - `נִאֵ֣ר / מֵאֵ֣ן` → `—` (I.0.8 line 392)

### TH-VAR-T0-018: Verb-name shewa contrast

- **Status:** exception
- **Authority:** standard-tiberian
- **Category:** morphophonology / semantic ḥaṭef
- **Statement:** Silent shewa versus ḥaṭef distinguishes יַעְקֹב from the name יַעֲקֹב.
- **Conditions:** For this isolated pair.
- **Operation:** Suppress or realize the vowel as lexically specified.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.8 (lines 470–470)
- **Certainty:** high
- **Examples:**
  - `יַעְקֹ֔ב / יַעֲקֹב` → `—` (I.0.8 line 470)

### TH-VAR-T0-019: Internal Tiberian streams

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** tradition / sub-schools
- **Statement:** Standard Tiberian contains minor word-specific differences among sub-schools and manuscripts.
- **Conditions:** Where authorities disagree.
- **Operation:** Preserve the selected stream.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.10 (lines 536–539)
- **Certainty:** high
- **Examples:** no example in source

### TH-VAR-T0-026: Major gaʿya optionality

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** prosody / gaʿya
- **Statement:** Major gaʿya may be omitted by one reader and sustained by another.
- **Conditions:** For major gaʿya.
- **Operation:** Optionally sustain the vowel.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.10 (lines 555–561)
- **Certainty:** high
- **Examples:** no example in source

### TH-VAR-T0-027: Ben Naftali conjunctive accents

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** prosody / Ben Naftali
- **Statement:** Ben Naftali sometimes uses a conjunctive accent where Ben Asher uses maqqef.
- **Conditions:** At transmitted loci.
- **Operation:** Prosodically separate the words.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.11 (lines 575–589)
- **Certainty:** high
- **Examples:**
  - `בְּנָקְב֥וֹ שֵׁ֖ם` → `—` (I.0.11 lines 577–579)

### TH-VAR-T0-030: NST lower authority

- **Status:** variant
- **Authority:** non-standard-tiberian
- **Category:** tradition / authority
- **Statement:** NST never had the same status as Standard Tiberian and eventually fell out of use.
- **Conditions:** When weighting conflicting systems.
- **Operation:** Treat NST as non-standard evidence.
- **Result IPA:** None
- **Source:** T1_0_Intro.md §I.0.13.6 (lines 703–703)
- **Certainty:** high
- **Examples:** no example in source

### TH-VAR-T2-001: Unstressed /e/ lowering

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** variant / quality-allophony
- **Statement:** Unstressed /e/ is generally realized [ɛ].
- **Conditions:** underlying /e/; not main-stressed
- **Operation:** Lower /e/ to [ɛ].
- **Result IPA:** ɛ
- **Source:** T1_2B_corrected_p352.md §I.2.3.2. Vowel Phonemes without a Specified Length   (lines 529–535)
- **Certainty:** high
- **Examples:**
  - `וַיֵּ֫רֶד` → `vaɟˈɟeːʀ̟ɛð`

### TH-VAR-T2-002: Unstressed /o/ lowering

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** variant / quality-allophony
- **Statement:** Unstressed /o/ is generally realized [ɔ].
- **Conditions:** underlying /o/; not main-stressed
- **Operation:** Lower /o/ to [ɔ].
- **Result IPA:** ɔ
- **Source:** T1_2B_corrected_p352.md §I.2.3.2. Vowel Phonemes without a Specified Length   (lines 529–539)
- **Certainty:** high
- **Examples:**
  - `קָדְשׁ֫וֹ` → `qɔðˈʃoː`

### TH-VAR-T2-003: Geminated glide before furtive pataḥ

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** variant / glide-fortition
- **Statement:** Some medieval Tiberian streams geminated the glide before furtive pataḥ.
- **Conditions:** furtive pataḥ; stream with glide fortition
- **Operation:** Geminate [w] or fortify geminated [j] to [ɟɟ].
- **Result IPA:** ww ~ ɟɟ
- **Source:** T1_2B_corrected_p352.md §I.2.4. Long Vowels in Closed Syllables (lines 811–827)
- **Certainty:** high
- **Examples:**
  - `רֽוּחַ` → `—` (Ecc. 4.4)

### TH-VAR-T2-004: Omission of furtive pataḥ

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** variant / furtive-pataḥ
- **Statement:** Some Non-Standard Tiberian manuscripts omit furtive pataḥ.
- **Conditions:** Non-Standard Tiberian stream; final guttural
- **Operation:** Do not insert or mark furtive pataḥ.
- **Result IPA:** None
- **Source:** T1_2B_corrected_p352.md §I.2.4. Long Vowels in Closed Syllables (lines 863–883)
- **Certainty:** high
- **Examples:**
  - `פִתֵּֽח` → `—` (Job 39.5)

### TH-VAR-T2-005: Ben Naftali contraction before yod

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** variant / Ben-Asher-Ben-Naftali
- **Statement:** Ben Naftali contracts the [iji] sequence found in Ben Asher's preposition-plus-yod reading to a long [iː] sequence.
- **Conditions:** prefixed ל or ב before yod; Ben Naftali stream
- **Operation:** Contract [iji] to long [iː] with epenthetic split.
- **Result IPA:** iːi
- **Source:** T1_2B_corrected_p352.md §I.2.5.1.2. Contextually-Conditioned Realization of _Shewa_ (lines 1067–1069)
- **Certainty:** high
- **Examples:**
  - `לִישְׂרָאֵל` → `liːisrˁɔːˈʔeːel`

### TH-VAR-T2-006: Prosthesis before numeral two

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** variant / lexical-exception
- **Statement:** Some Tiberian sources report a prosthetic [ʔɛ] before the silent initial cluster of שְׁתַּיִם.
- **Conditions:** שְׁתַּיִם; prosthetic stream
- **Operation:** Prefix [ʔɛ] while retaining silent shewa.
- **Result IPA:** ʔɛʃˈtʰaːjim
- **Source:** T1_2B_corrected_p352.md §I.2.5.3. Phonological Principles (lines 1248–1262)
- **Certainty:** high
- **Examples:**
  - `שְׁתַּיִם` → `ʔɛʃˈtʰaːjim`

### TH-VAR-T2-007: Prefixed-particle resh variation

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** variant / stream-variation
- **Statement:** Some Tiberian streams pronounce the shewa after a long prefixed particle as silent where the Treatise predicts vocalic shewa.
- **Conditions:** long prefixed particle before resh+shewa
- **Operation:** Allow silent realization by stream.
- **Result IPA:** VːVʀ̟C
- **Source:** T1_2B_corrected_p352.md §I.2.5.7.4. Long Vowel in a Prefixed Particle before Resh (lines 1802–1814)
- **Certainty:** high
- **Examples:**
  - `וּבָ֣רְחֹב֔וֹת` → `wuvɔːɔʀ̟ħoːˈvoːoθ` (Cant. 3.2)

### TH-VAR-T2-008: Ben Asher lexical-root shewa rules

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** variant / Ben-Asher
- **Statement:** Ben Asher has lexical and morphological exceptions with vocalic shewa after long vowels in specified roots, including ברך, גרש, אכל, ירד and הלך.
- **Conditions:** one of the listed verbal roots; listed inflectional/prosodic context
- **Operation:** Realize shewa vocalically where listed.
- **Result IPA:** a
- **Source:** T1_2B_corrected_p352.md §I.2.5.7.5. _Shewa_ in Inflections of Specific Verbal Roots (lines 1816–1908)
- **Certainty:** high
- **Examples:**
  - `בָּרֲכֵ֥נִי` → `bɔːʀ̟aˈχeːniː` (Gen. 27.34)
  - `תֹּֽאכֲלֶ֔נָּה` → `tʰoːχaːˈlɛːɛnnɔː` (Gen. 3.17)

### TH-VAR-T2-009: Ben Naftali silent lexical-root shewa

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** variant / Ben-Naftali
- **Statement:** Ben Naftali reads shewa silent throughout the roots גרש and אכל where Ben Asher has listed vocalic exceptions.
- **Conditions:** root גרש or אכל; Ben Naftali stream
- **Operation:** Realize shewa as zero.
- **Result IPA:** ∅
- **Source:** T1_2B_corrected_p352.md §I.2.5.7.5. _Shewa_ in Inflections of Specific Verbal Roots (lines 1848–1900)
- **Certainty:** high
- **Examples:** no example in source

### TH-VAR-T2-010: Article plus mem minor-gaʿya stream variation

- **Status:** variant
- **Authority:** manuscript
- **Category:** variant / Ben-Asher-Ben-Naftali
- **Statement:** Ben Asher and Ben Naftali differ in minor gaʿya and shewa realization in article+מְ forms.
- **Conditions:** article+מְ form
- **Operation:** Apply manuscript/authority-specific reading.
- **Result IPA:** haːma ~ haˑm ~ ham
- **Source:** T1_2B_corrected_p352.md §I.2.5.8.1. The Definite Article (lines 2128–2160)
- **Certainty:** high
- **Examples:**
  - `הַֽמְזִמָּ֙תָה֙` → `haːmazimmɔːˈθɔː` (Jer. 11.15)
  - `הַֽמְיַלְּדֹת֙` → `ˌhaˑmjallaˈðoːoθ` (Exod. 1.17)

### TH-VAR-T2-011: Identical-consonant lengthening variation

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** variant / Ben-Asher-Ben-Naftali
- **Statement:** Authorities and manuscripts vary in lengthening and shewa vocalization before two identical consonants.
- **Conditions:** short vowel before identical consonants
- **Operation:** Apply authority-specific gaʿya/length.
- **Result IPA:** VːCaC ~ VCC
- **Source:** T1_2B_corrected_p352.md §I.2.5.8.3. Two Identical Consonants (lines 2442–2464)
- **Certainty:** high
- **Examples:**
  - `לְשִֽׁמְמָ֖ה` → `laʃiːmaˈmoː` (Ezek. 35.7)
  - `לְשְֽמְמָה` → `laʃimˈmɔː` (Ezek. 35.7)

### TH-VAR-T2-012: Conjunctive vav minor-gaʿya silent shewa

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** variant / minor-gaʿya
- **Statement:** When gaʿya on conjunctive vav is musical minor gaʿya, the vowel is half-long and the following shewa remains silent.
- **Conditions:** conjunctive וּ; minor gaʿya
- **Operation:** Half-lengthen [u]; keep shewa silent.
- **Result IPA:** uˑC
- **Source:** T1_2B_corrected_p352.md §I.2.5.8.4. Conjunctive _Vav_ (lines 2518–2544)
- **Certainty:** high
- **Examples:**
  - `וּֽדְמֵה־לְךָ֤` → `ˌwuˑðmeː-laˈχɔː` (Cant. 8.14)

### TH-VAR-T2-013: Western vocalic final shewa

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** variant / word-final-cluster
- **Statement:** Some western medieval sources pronounce the final shewa vocalically outside major pause.
- **Conditions:** western medieval stream; word-final cluster; not major pause
- **Operation:** Vocalize final shewa.
- **Result IPA:** CCV#
- **Source:** T1_2B_corrected_p352.md §I.2.5.9.1. In Word-final Consonantal Clusters (lines 2710–2710)
- **Certainty:** high
- **Examples:** no example in source

### TH-VAR-T2-014: Lexical ḥaṭef qameṣ reduction variants

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** variant / lexical-vowel
- **Statement:** Some words vary between lexical ḥaṭef qameṣ and reduced shewa/ḥaṭef pataḥ readings.
- **Conditions:** listed lexical item or authority
- **Operation:** Select lexical [ɔ] or reduced epenthetic quality by source.
- **Result IPA:** ɔ ~ a
- **Source:** T1_2B_corrected_p352.md §I.2.7. Lexical _Ḥaṭef_ Vowels (lines 3074–3082)
- **Certainty:** high
- **Examples:**
  - `אֶצֳּרֶֽנָּה` → `ʔɛsˁ.sˁɔ.ˈʀ̟ɛː.ɛn.nɔː` (Isa. 27.3)
  - `וְאֶצְּרֶ֥נָּה` → `—` (Psa. 119.33)

### TH-VAR-T2-015: Careless shortening of unstressed long vowels

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** variant / reading-tempo
- **Statement:** Less careful streams reduce the duration of long vowels in unstressed open syllables.
- **Conditions:** less careful reading; unstressed long vowel
- **Operation:** Shorten relative to careful Tiberian length.
- **Result IPA:** Vː → V(ˑ/V)
- **Source:** T1_2B_corrected_p352.md §I.2.8.1.1. Stressed and Unstressed Vowels (lines 3195–3215)
- **Certainty:** high
- **Examples:** no example in source

### TH-VAR-T2-016: Full shortening in non-core deḥiq streams

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** variant / dehiq
- **Statement:** Babylonian, Greek, modern, and less careful evidence can reflect full shortening where the careful Tiberian stream preserves half-length.
- **Conditions:** non-core or less careful stream; deḥiq
- **Operation:** Shorten final vowel fully.
- **Result IPA:** V
- **Source:** T1_2B_corrected_p352.md §I.2.8.1.2. _Deḥiq_ (lines 3307–3367)
- **Certainty:** high
- **Examples:**
  - `מֶה זֹאת` → `ma ˈzzoːθ` (Exod. 13.14)

### TH-VAR-T2-017: Major gaʿya manuscript frequency

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** variant / notation
- **Statement:** Early manuscripts differ substantially in how often they write major gaʿya; notation is not a deterministic record of its pronunciation.
- **Conditions:** major-gaʿya-eligible syllable
- **Operation:** Treat written presence/absence as manuscript-specific.
- **Result IPA:** None
- **Source:** T1_2B_corrected_p352.md §I.2.8.2.1. On Open Syllables with Long Vowels (lines 3475–3485)
- **Certainty:** high
- **Examples:** no example in source

### TH-VAR-T2-018: Haya and ḥaya length notation variation

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** variant / metrical-epenthesis
- **Statement:** Model codices vary in writing gaʿya on היה/חיה prefixes, while Karaite transcriptions often indicate length even when gaʿya is absent.
- **Conditions:** prefix of היה or חיה
- **Operation:** Do not equate absence of gaʿya with absence of lengthening.
- **Result IPA:** iˑ ~ aˑ
- **Source:** T1_2B_corrected_p352.md §I.2.10. Metrical Epenthesis (lines 3904–3942)
- **Certainty:** high
- **Examples:** no example in source

### TH-VAR-T2-019: Inherent long vowel maqqef shortening

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** variant / maqqef
- **Statement:** Some Masoretic and Karaite evidence shortens inherently long vowels in closed pre-maqqef words.
- **Conditions:** closed syllable; pre-maqqef word; stream allowing prosodic reduction
- **Operation:** Shorten inherently long vowel.
- **Result IPA:** Vː → V
- **Source:** T1_2B_corrected_p352.md §I.2.11. _Maqqef_ (lines 4028–4044)
- **Certainty:** high
- **Examples:**
  - `הוֹד־` → `—` (Psa. 111.3)
  - `לֵב־פַּרְעֹה֙` → `—` (Exod. 7.22)

### TH-VAR-T2-020: Ben Naftali favors conjunctive independence

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** variant / Ben-Asher-Ben-Naftali
- **Statement:** In several cases Ben Naftali uses a conjunctive accent where Ben Asher uses maqqef, giving the first word greater prosodic independence.
- **Conditions:** listed phrase; Ben Naftali stream
- **Operation:** Replace maqqef grouping with conjunctive-accent grouping.
- **Result IPA:** greater first-word prominence
- **Source:** T1_2B_corrected_p352.md §I.2.11. _Maqqef_ (lines 4084–4100)
- **Certainty:** high
- **Examples:** no example in source

### TH-VAR-T2-021: Glottalized maqqef boundary

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** variant / boundary-marking
- **Statement:** Some Karaite transcriptions glottalize or devoice the offset of a pre-maqqef final vowel to preserve the word boundary.
- **Conditions:** word-final vowel before maqqef; glottalizing stream
- **Operation:** Add [h]-like/glottalized offset.
- **Result IPA:** Vh-
- **Source:** T1_2B_corrected_p352.md §I.2.11. _Maqqef_ (lines 4122–4144)
- **Certainty:** high
- **Examples:**
  - `מַה־שְּׁמֶ֑ךָ` → `mah-ʃʃaˈmɛːχɔː` (Gen. 32.28)

### TH-VAR-T3-001: Forte–lene standard stream

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** streams / forte-lene
- **Statement:** In the dagesh forte–dagesh lene stream, dagesh forte consonants are geminated, while dagesh lene BGDKPT stops are singleton.
- **Conditions:** The selected standard stream is forte-lene.
- **Operation:** Geminate forte; realize lene as an ungeminated stop.
- **Result IPA:** forte: CC; lene: b g d kʰ pʰ tʰ
- **Source:** T1_3B.md §I.3.1.11.3 (lines 519–593)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-VAR-002']
- **Examples:** no example in source

### TH-VAR-T3-002: Extended-forte standard stream

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** streams / extended-forte
- **Statement:** In the extended dagesh forte stream, every dagesh—including conventional dagesh lene on BGDKPT—is realized as gemination.
- **Conditions:** The selected standard stream is extended-forte.; A consonant bears dagesh.
- **Operation:** Give dagesh its full geminating value in all contexts.
- **Result IPA:** bb gg dd kkʰ ppʰ ttʰ
- **Source:** T1_3B.md §I.3.1.11.3 (lines 555–635)
- **Certainty:** high
- **Notes:** Dropped unresolved related_ids: ['TH-VAR-001']
- **Examples:** no example in source

### TH-VAR-T3-003: Major dagesh in three tavs

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** prosody / extra-long-gemination
- **Statement:** In the extended-forte evidence, three specified tavs have 'major dagesh', stronger and longer than normal gemination.
- **Conditions:** The tav is one of the three specified forms.
- **Operation:** Realize tav with exceptionally high pressure and duration.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.11.3 (lines 595–609)
- **Certainty:** high
- **Examples:**
  - `תֵּל־עוֹלָם֙` → `—` (Josh. 8.28) [extended-forte]

### TH-VAR-T3-004: בָּתִּים in extended-forte

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** lexicon / battim
- **Statement:** In the extended-forte stream, tav in בָּתִּים and its forms is normally geminated.
- **Conditions:** The lexeme is בָּתִּים or an inflected/construct form.; The selected stream is extended-forte.
- **Operation:** Geminate tav.
- **Result IPA:** ttʰ
- **Source:** T1_3B.md §I.3.1.12 (lines 641–649)
- **Certainty:** high
- **Examples:**
  - `בְּבָתֵּ֣י` → `—` (Zeph. 2.7) [extended-forte]

### TH-VAR-T3-005: בָּתִּים in forte–lene

- **Status:** rule
- **Authority:** standard-tiberian
- **Category:** lexicon / battim
- **Statement:** In the forte–lene stream, tav in בָּתִּים and its forms is an ungeminated stop.
- **Conditions:** The lexeme is בָּתִּים or an inflected/construct form.; The selected stream is forte-lene.
- **Operation:** Realize singleton stop tav.
- **Result IPA:** tʰ
- **Source:** T1_3B.md §I.3.1.12 (lines 651–681)
- **Certainty:** high
- **Examples:**
  - `הַבָּתִּֽים` → `—` (Exod. 9.20) [forte-lene]

### TH-VAR-T3-006: בָּתִּים extra-long accented variant

- **Status:** variant
- **Authority:** standard-tiberian
- **Category:** prosody / battim
- **Statement:** In specified extended-forte readings, accented בָּתִּים has tav stronger than normal gemination; Ben Naftali generalizes this to cases with secondary accent, while Ben Asher restricts it.
- **Conditions:** Selected stream is extended-forte.; The word has the specified secondary and main accent pattern.; The selected Masoretic authority licenses the locus.
- **Operation:** Lengthen geminate tav beyond normal gemination.
- **Result IPA:** None
- **Source:** T1_3B.md §I.3.1.12 (lines 641–645)
- **Certainty:** high
- **Notes:** Ben Asher and Ben Naftali differ in lexical extent.
- **Examples:** no example in source

### TH-VAR-VAV-T1-002: Conjunctive va variant

- **Status:** variant
- **Authority:** comparative
- **Category:** sub-tradition / conjunction
- **Statement:** A variant stream reads conjunctive וּ as [va], even before a labial.
- **Conditions:** The stated orthographic or phonological context applies.
- **Operation:** Realize the conjunction as [va].
- **Result IPA:** va
- **Source:** T1_1.md §I.1.6 (lines 667–683)
- **Certainty:** high
- **Examples:**
  - `וּמִ֣י` → `va` (Ecc. 2.19)

