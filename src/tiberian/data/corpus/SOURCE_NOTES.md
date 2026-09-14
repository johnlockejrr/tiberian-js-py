# Source notes (terminology and conventions)

## Source of truth

Only these files define pronunciation rules:

- `T1_0_Intro.md` — §I.0 Introduction (main prose ≈ lines 1–713)
- `T1_1.md` — §I.1 Consonants (main prose ≈ lines 1–1577)
- `T1_2B_corrected_p352.md` — §I.2 Vowels and syllable structure (main prose ≈ lines 1–4174)
- `T1_3B.md` — §I.3 Dagesh and rafe (main prose ≈ lines 39–943)
- `T1_4B_5_Ref.md` — §I.4 imperfect learning; §I.5 summary and samples (main prose ≈ lines 1–452)

Indexes and bibliographies after main prose are not primary rule sources.

Helpers (`docs/AGENTS.md`, `docs/superpowers.md`, `docs/tiberian.ts`) are non-authoritative.

## Authority layers

| Layer | Meaning |
|-------|---------|
| `standard-tiberian` | Reconstructed Standard Tiberian oral reading (Ben Asher / Ben Naftali streams) |
| `non-standard-tiberian` | Tiberian signs with non-standard system (often Palestinian-like) |
| `manuscript` | Codex-specific observation (A, L, C, B, S, etc.) |
| `comparative` | Babylonian, Palestinian, Karaite, modern community evidence |
| `editorial` | Explicit editorial note in corpus (never presented as source quotation) |

## Dual Standard reading streams

Standard Tiberian has two orthoepic streams for בגדכפת with *dagesh*:

1. **forte–lene** — conventional *dagesh forte* vs *dagesh lene*
2. **extended forte** — *dagesh lene* also realized as geminate

These are not merged; samples in §I.5.4 give both when they differ.

## IPA conventions in the sources

- Length: `ː` long; `ˑ` half-long
- Stress: `ˈ` primary; `ˌ` secondary
- Aspiration: `ʰ` on כּ פּ תּ stops
- Emphatics: `ˁ` (pharyngealization)
- Advanced uvular: `̟` on `q̟`, `ʀ̟`
- Silent shewa / zero: `∅` in summaries
- Geminate yod: source conflict `[ɉ]` (§I.1.10) vs `[ɟ]` (§I.1.24 / §I.5) — see gaps register
- **Project transcriptions omit the book's editorial `[...]` wrappers** — store and emit bare IPA only (e.g. `baʀ̟eːˈʃiːiθ`, not `[baʀ̟eːˈʃiːiθ]`).

## Profiles (for future engine; not invented here)

- `ben_asher` / `ben_naftali` — do not blend
- `forte_lene` / `extended_forte`
- `vav_w_glide` — where sources disagree on [v] vs [w]
