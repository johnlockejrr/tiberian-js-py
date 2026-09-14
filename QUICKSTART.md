# Quick start (JS-backed Tiberian IPA)

## 1. Setup

```bash
cd /path/to/tiberian-js-py
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cd js && npm install && cd ..
```

## 2. Transcribe

```bash
tiberian "מִֽי־פָקַ֣ד עָלָ֣יו אָ֑רְצָה וּמִ֥י שָׂ֝֗ם תֵּבֵ֥ל כֻּלָּֽהּ׃"
# ˌmiˑ-ppʰɔːˈq̟aːað ʕɔːˈlɔːɔw ˈʔɔːɔʀ̟sˁɔː wuˈmiː ˈsɔːɔm tʰeːˈveːel kʰulˈlɔːɔh
```

```python
from tiberian import transcribe
print(transcribe("בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים").ipa)
```

Batch:

```bash
python scripts/batch_transcribe_js.py -i Genesis_1.txt -o Genesis_1.ipa.txt
```

## 3. Check

```bash
pytest -q
tiberian --help
```

More: [README.md](README.md).
