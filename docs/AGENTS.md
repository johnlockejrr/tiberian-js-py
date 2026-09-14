You are working inside a project directory containing a book about Tiberian Hebrew

vocalization. Your task has three phases. Do not skip ahead between phases.



SOURCE FILES (read every one, in full, start to finish — no sampling, no skimming):

\- T1\_0\_Intro.md

\- T1\_1.md

\- T1\_2B\_corrected\_p352.md

\- T1\_3B.md

\- T1\_4B\_5\_Ref.md



These five files are the ONLY source of truth. Do not consult external sources, prior

training knowledge of Tiberian Hebrew, or general Hebrew grammar references to fill

gaps, resolve ambiguity, or "complete" a rule. If something in the text is unclear,

incomplete, or contradictory, report it as such rather than resolving it yourself.



PHASE 1 — Full read

Read all five files completely before extracting anything. If any file is long,

read it in sequential chunks until you reach the end — confirm to yourself you have

seen the last line of each file before moving to Phase 2. Keep track of which file

and section each piece of information comes from.



PHASE 2 — Extraction

Extract every rule governing Tiberian pronunciation (vocalization, vowel realization,

consonant realization, gemination, shewa behavior, dagesh/rafe, accents/te'amim as

they affect pronunciation, syllabification, stress, and any conditioning environment

or exception mentioned), together with every example the source gives for that rule.



Rules for the extraction itself:

\- Do not invent examples. Only use examples that appear in the source files.

\- Do not invent rules, generalize beyond what is stated, or merge two source

&#x20; statements into a rule the text does not itself state.

\- Do not silently resolve conflicting statements between files — flag the conflict.

\- Preserve the source's own terminology and transcription conventions; note them if

&#x20; the source defines them.

\- For every rule, cite which file (and page/section if given) it came from.

\- If a rule is stated but no example is given in the source, mark it explicitly as

&#x20; "no example in source" rather than fabricating one.



PHASE 3 — Deliverables

Produce exactly two files:



1\. `tiberian\_rules.md`

&#x20;  A human-readable markdown document listing every extracted rule, grouped by

&#x20;  category, each with:

&#x20;  - The rule as stated in the source (paraphrased for clarity if needed, but not

&#x20;    altered in meaning)

&#x20;  - Its source citation (file + location)

&#x20;  - Its example(s) from the source, or "no example in source"

&#x20;  - Any noted ambiguity, exception, or conflict



2\. `tiberian\_rules.json`

&#x20;  A machine-readable JSON file with the same rules, hierarchically categorized

&#x20;  (e.g. by domain: vowels / consonants / shewa / dagesh-rafe / gemination /

&#x20;  syllabification / stress / accents, then sub-rules within each), structured so

&#x20;  it can drive a future Python IPA-transcription pipeline. Each rule object should

&#x20;  include at minimum: id, category, subcategory, statement, conditions/environment,

&#x20;  examples (array, each with source Hebrew form and its IPA/phonetic realization

&#x20;  exactly as given or derivable directly from the source), and source\_citation.

&#x20;  Do not add rules or examples to the JSON that are not in the markdown file.



Before finalizing, do a self-check pass: re-scan the source files once more to

confirm no rule was missed and that nothing in tiberian\_rules.md or

tiberian\_rules.json goes beyond what the sources state. Report any part of the

source material you were unable to turn into a clean rule (e.g. narrative

discussion without a codifiable rule) rather than forcing it into the schema.

