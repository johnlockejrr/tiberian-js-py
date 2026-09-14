# Tiberian Hebrew Pronunciation Rules Corpus — Design Specification

## 1. Purpose

This project will create a source-faithful corpus of the pronunciation rules documented in the supplied Markdown files. The corpus will be the authoritative basis for a later Python transcription engine that accepts Masoretic Hebrew text and returns Tiberian Hebrew IPA without inventing unsupported phonetic values.

The first implementation cycle is limited to the rules corpus and its machine-readable companion. The Python transcription engine is a separate later cycle.

## 2. Source boundary

The corpus will use only these supplied Markdown files:

- `T1_0_Intro.md`
- `T1_1.md`
- `T1_2B_corrected_p352.md`
- `T1_3B.md`
- `T1_4B_5_Ref.md`

No external scholarship or pronunciation values will be added in the first cycle.

The primary target is the Standard Tiberian reading tradition. Non-Standard Tiberian vocalization, manuscript-specific observations, and comparative traditions will be retained as labeled evidence or variants rather than silently merged into the target rules.

## 3. Meaning of “exact IPA”

“Exact IPA” means deterministic segmental IPA supported by the selected source layer and its documented conditions.

The initial transcription target is segmental IPA only. Stress, duration, timing, and intonation will not be invented. When stress or duration conditions a segmental rule, that information may be retained as metadata or used internally, but it will not be emitted as an unsupported prosodic claim.

If the sources permit multiple realizations or do not determine a value, the result will be marked unresolved or source-dependent. The system will not choose a Modern Hebrew, Babylonian, Palestinian, Samaritan, or editorially guessed value by default.

## 4. Corpus deliverables

The first cycle will produce:

1. A comprehensive Markdown rules document.
2. A YAML companion containing the same rule records.
3. A source-to-rule coverage matrix.
4. An index of pronunciation-bearing examples.
5. A register of unresolved gaps and source-dependent cases.
6. A full-coverage audit.

Proposed filenames:

- `tiberian-hebrew-pronunciation-rules.md`
- `tiberian-hebrew-pronunciation-rules.yaml`

The Markdown document is the canonical human-readable record. YAML is the machine-readable companion and must not introduce rules that are absent from the Markdown evidence.

## 5. Corpus organization

The Markdown corpus will be organized by linguistic domain:

1. Source conventions and authority levels.
2. Orthographic input and textual resolution.
3. Consonant inventory.
4. Consonant allophony.
5. Begadkephat stop/fricative behavior.
6. Gutturals, laryngeals, pharyngeals, alef, and resh.
7. Dagesh and rafe.
8. Gemination and loss of gemination.
9. Vowel qualities.
10. Vowel length and duration.
11. Shewa and ḥaṭef vowels.
12. Syllable structure.
13. Stress and secondary stress.
14. Maqqef and phrase-boundary effects.
15. Qere and ketiv.
16. Non-Standard Tiberian and manuscript variation.
17. IPA emission rules.
18. Unresolved cases and evidence gaps.
19. Complete example index.
20. Coverage audit.

The source files map to these domains as follows:

| Source | Main contribution |
| --- | --- |
| `T1_0_Intro.md` | Oral and written transmission, source authority, Qere/Ketiv, accents, manuscript layers |
| `T1_1.md` | Consonants, individual letter behavior, phoneme inventory, begadkephat distribution |
| `T1_2B_corrected_p352.md` | Vowels, syllables, shewa, ḥaṭef signs, stress, duration, maqqef |
| `T1_3B.md` | Dagesh, rafe, gemination, orthoepy, loss of gemination, manuscript exceptions |
| `T1_4B_5_Ref.md` | Imperfect/non-standard learning, substrate effects, summaries, sample transcriptions |

## 6. Rule identity and metadata

Each rule receives a stable semantic identifier independent of source line numbers. Suggested ID families are:

- `TH-CON-*` — consonants
- `TH-BGDKPT-*` — begadkephat behavior
- `TH-GUTT-*` — gutturals and related consonants
- `TH-DAG-*` — dagesh and gemination
- `TH-RAF-*` — rafe
- `TH-VOW-*` — vowel quality
- `TH-LEN-*` — vowel length and duration
- `TH-SHEWA-*` — shewa
- `TH-HATEF-*` — ḥaṭef vowels
- `TH-SYL-*` — syllabification
- `TH-STR-*` — stress
- `TH-MAQ-*` — maqqef
- `TH-QK-*` — qere/ketiv
- `TH-VAR-*` — non-standard or manuscript variation
- `TH-GAP-*` — unresolved cases

Every rule record contains:

- Stable rule ID.
- Concise title.
- Status: `rule`, `exception`, `variant`, `evidence`, or `gap`.
- Authority layer: `standard-tiberian`, `non-standard-tiberian`, `manuscript`, `comparative`, or `editorial`.
- Trigger conditions.
- Phonological or orthographic operation.
- Resulting IPA or phonological representation.
- Preconditions and ordering constraints.
- Exceptions and overriding rules.
- Relevant Hebrew examples.
- Source IPA preserved exactly as printed.
- Source file.
- Source section.
- Source line range.
- Short source quotation or excerpt hash.
- Biblical citation where available.
- Certainty label.
- Related rule IDs.
- Notes on unresolved interpretation.

Source line ranges are useful for the initial extraction but are not the sole identity mechanism, because line numbers can change during editing.

## 7. Extraction method

### 7.1 Source inventory

Every heading and relevant subsection will be entered into a coverage matrix. The matrix records the source file, section, linguistic topic, extracted rules, examples, variants, gaps, and review status.

### 7.2 Atomic extraction

Pronunciation-bearing prose will be decomposed into atomic records. One paragraph may yield multiple records when it contains a general rule, a conditioning environment, an exception, a manuscript variant, comparative evidence, or an unresolved interpretation.

A record will not combine unrelated conditions merely to reduce the number of entries.

### 7.3 Evidence classification

Each claim will be classified as one of:

- Directly stated Standard Tiberian rule.
- Rule inferred through explicit source reasoning.
- Manuscript-specific observation.
- Non-Standard Tiberian variant.
- Comparative evidence.
- Historical explanation.
- Editorial normalization.
- Unresolved.

Editorial normalization will be visibly labeled and will never be presented as a source quotation.

### 7.4 IPA preservation

The source IPA will be preserved in a dedicated field without silently changing vowel symbols, length marks, stress marks, aspiration markers, emphatic markings, gemination notation, syllable boundaries, or secondary-stress notation.

A normalized IPA field may be added only when a documented normalization is required for the future engine. The relationship between source IPA and normalized IPA will be explicit.

### 7.5 Example handling

Every example that instantiates a pronunciation rule, exception, variant, or ambiguity will be included. Each example retains the Hebrew form, supplied transliteration, source IPA, gloss, biblical citation, manuscript siglum where supplied, and the rule or gap IDs it demonstrates.

Background examples with no pronunciation-bearing function may be summarized or cited rather than duplicated.

## 8. Future transcription-engine architecture

The later Python engine will consume the stabilized corpus rather than independently encoding pronunciation rules.

The planned data flow is:

1. **Input normalization**
   - Accept Unicode Masoretic Hebrew text.
   - Preserve consonants, vowel signs, dagesh, rafe, cantillation, maqqef, and other relevant marks.
   - Retain the original input separately from any normalized form.

2. **Textual resolution**
   - Resolve supported qere/ketiv cases.
   - Distinguish written form from read form.
   - Preserve unresolved textual conflicts.

3. **Orthographic analysis**
   - Identify consonantal and vocalic mater lectionis behavior.
   - Identify shin/sin marking.
   - Interpret dagesh and rafe.
   - Detect documented special orthographic cases.

4. **Syllabification**
   - Apply documented shewa and ḥaṭef behavior.
   - Build syllable nuclei, onsets, and codas.
   - Represent uncertainty rather than guessing.

5. **Phonological rule application**
   - Apply vowel-quality rules.
   - Apply consonant allophony.
   - Apply begadkephat rules.
   - Apply gemination and loss-of-gemination rules.
   - Apply guttural, alef, and resh constraints.
   - Use stress and secondary stress only where they condition segmental output.

6. **IPA emission**
   - Produce segmental IPA only in the initial engine.
   - Retain source-supported length or stress as metadata when needed for rule selection.
   - Do not emit unsupported timing or intonation.

7. **Unresolved reporting**
   - Return partial IPA for supported spans.
   - Return structured unresolved items for unsupported or ambiguous spans.
   - Include relevant rule IDs and evidence references.

A future result object will conceptually contain:

- Input text.
- Resolved reading text.
- Segmental IPA.
- Per-segment rule provenance.
- Unresolved spans.
- Warnings about manuscript or source variation.

## 9. Rule ordering and conflict handling

The engine will use explicit precedence rather than implicit ordering.

The corpus will define ordering for interacting rules, especially:

- Qere/ketiv resolution before phonological analysis.
- Orthographic resolution before syllabification.
- Shewa classification before syllable construction.
- Syllable structure before context-sensitive consonant allophony.
- Gemination before begadkephat realization where the source requires that interaction.
- Stress-sensitive rules after syllabification.
- Manuscript-specific overrides only within an explicitly selected source profile.

If two rules conflict and the sources do not state precedence, the case becomes a `TH-GAP-*` record rather than being resolved by editorial preference.

## 10. Error and uncertainty behavior

The system fails closed.

It explicitly reports:

- Unsupported Hebrew characters.
- Unsupported or ambiguous sign combinations.
- Missing qere information needed to determine the reading.
- Conflicting qere and ketiv evidence.
- Undocumented consonant-vowel combinations.
- Ambiguous syllabification.
- Conflicting manuscript traditions.
- Rules with insufficient evidence.
- IPA values that cannot be selected without invention.

The output will never silently substitute:

- Modern Hebrew pronunciation.
- A generalized Semitic reconstruction.
- Babylonian or Palestinian values.
- A guessed stress pattern.
- A guessed vowel length.
- A guessed consonant realization.

## 11. Validation and testing

### 11.1 Source-coverage tests

The completion audit verifies that:

- Every source heading is accounted for.
- Every pronunciation-bearing passage is mapped to a rule, variant, evidence record, or gap.
- Every extracted example is linked to at least one rule or gap.
- Every rule has source evidence.
- Every unresolved claim has a gap ID.
- Standard and non-standard material is not conflated.

### 11.2 Linguistic regression tests

The future engine will be tested against:

- All source examples with supplied IPA.
- The sample transcriptions in `T1_4B_5_Ref.md`.
- Genesis 1.1–13 examples.
- Psalm 1 examples.
- Begadkephat stop/fricative environments.
- Dagesh forte and dagesh lene.
- Guttural and resh exceptions.
- Vocalic and silent shewa.
- Ḥaṭef vowels.
- Long vowels in closed syllables.
- Stress-sensitive duration cases.
- Maqqef boundaries.
- Qere/ketiv readings.
- Non-Standard Tiberian examples.

### 11.3 Negative and uncertainty tests

Tests confirm that unsupported or ambiguous input produces partial IPA where possible, explicit unresolved spans, source references, and no fabricated fallback pronunciation.

### 11.4 Schema and consistency tests

The YAML companion is checked for:

- Unique rule IDs.
- Valid status values.
- Valid authority layers.
- Required evidence fields.
- Referential integrity between examples and rules.
- Duplicate or contradictory rules.
- Missing exception links.
- Missing gap records.

## 12. Repository and versioning

This design and the future rules corpus are maintained in a local Git repository. The design specification is committed before implementation planning begins.

The initial repository contains the supplied source files as untracked working-tree material. The first design commit contains only this specification unless the user explicitly requests that source files be added.

## 13. Completion criteria

The rules-corpus cycle is complete only when:

1. The Markdown corpus covers every pronunciation-bearing rule, condition, exception, variant, and example in the five source files.
2. Every record has stable identification and traceable evidence.
3. The YAML companion is structurally valid and consistent with Markdown.
4. All unresolved cases are explicitly recorded rather than silently filled.
5. The coverage audit reports no unclassified source sections or pronunciation-bearing passages.
6. The future engine remains separate until this corpus is approved and stabilized.

## 14. Approval gate

No Python project files, transcription code, generated corpus files, or implementation scaffolding are created by this design specification. Implementation planning begins only after this specification is reviewed and approved.
