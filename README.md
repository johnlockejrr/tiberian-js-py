# tiberian-js-py

Python CLI/API that wraps [hebrew-transliteration](https://github.com/charlesLoder/hebrew-transliteration)’s **Tiberian** schema (via Node) to produce **Tiberian IPA** from pointed Biblical Hebrew.

This repository is the **JS-backed** stack (`src/tiberian` + `js/`). A separate pure-Python port lives elsewhere and is not part of this package.

## Credits

- **Linguistic authority:** Geoffrey Khan’s description of the Tiberian reading tradition (*The Tiberian Pronunciation Tradition of Biblical Hebrew* / TPT). Private source extracts used during development are **not** included in this repository.
- **Engine:** Charles Loder — [hebrew-transliteration](https://github.com/charlesLoder/hebrew-transliteration) + [havarotjs](https://github.com/charlesLoder/havarotjs) (MIT). Schema: [`js/schemas/tiberian.ts`](js/schemas/tiberian.ts).

## Requirements

- Python **3.11+**
- Node.js **≥18** (runtime for the Tiberian schema)

## Install

```bash
git clone https://github.com/johnlockejrr/tiberian-js-py.git
cd tiberian-js-py

python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

cd js && npm install && cd ..
```

## Quickstart

### CLI

```bash
tiberian "מִֽי־פָקַ֣ד עָלָ֣יו אָ֑רְצָה וּמִ֥י שָׂ֝֗ם תֵּבֵ֥ל כֻּלָּֽהּ׃"
# ˌmiˑ-ppʰɔːˈq̟aːað ʕɔːˈlɔːɔw ˈʔɔːɔʀ̟sˁɔː wuˈmiː ˈsɔːɔm tʰeːˈveːel kʰulˈlɔːɔh

tiberian --json "בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים"
tiberian --engine js "…"      # default
tiberian -p extended_forte "…"  # opt-in stream label (partial)
```

### Python

```python
from tiberian import transcribe

r = transcribe("בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָֽרֶץ׃")
print(r.ipa)
# baʀ̟eːˈʃiːiθ bɔːˈʀ̟ɔː ʔɛloːˈhiːim ˈʔeːeθ haʃʃɔːˈmaːjim veˈʔeːeθ hɔːˈʔɔːʀ̟ɛsˁ
print(r.mode)  # js-tiberian
```

### Batch (chapter files)

Verse-numbered input (e.g. `Genesis_1.txt` → `1 HEBREW…׃ 2 …`):

```bash
python scripts/batch_transcribe_js.py -i Genesis_1.txt -o Genesis_1.ipa.txt
# lines: 1\t<ipa>
```

JSONL: `-o out.jsonl` or `--format jsonl`.

## How it works

```text
pointed Hebrew
  → normalize (NFD) + qere
  → js/runner.ts  (hebrew-transliteration + js/schemas/tiberian.ts + havarotjs)
  → bare IPA
```

| Path | Role |
|------|------|
| `src/tiberian/` | Python API + CLI (`engine_js` bridge) |
| `js/` | Node runner + vendored schema |
| `js/schemas/tiberian.ts` | Tiberian Schema (IPA inventory + ADDITIONAL_FEATURES) |
| `corpus/` | Extracted pronunciation-rule corpus (derived; not the book text) |

Default stream: **forte–lene**. Output is **bare IPA** (no `[…]`). Non-Hebrew input fails closed.

## Test

```bash
pytest -q
tiberian --help
```

## License

MIT — see `pyproject.toml`. Upstream hebrew-transliteration / havarotjs are MIT.
