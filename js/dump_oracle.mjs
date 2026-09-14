import { transliterate } from "hebrew-transliteration";
import { tiberian } from "./schemas/tiberian.ts";
import { Text } from "havarotjs";
import fs from "fs";

const cases = {
  user: "מִֽי־פָקַ֣ד עָלָ֣יו אָ֑רְצָה וּמִ֥י שָׂ֝֗ם תֵּבֵ֥ל כֻּלָּֽהּ׃",
  shalom: "שָׁלוֹם",
  elohim: "אֱלֹהִים",
  bereshit: "בְּרֵאשִׁ֖ית",
  gen1: "בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָֽרֶץ׃",
};

// js/schemas/tiberian.ts syl opts
const sylOpts = {
  allowNoNiqqud: false, article: false, holemHaser: "remove",
  longVowels: false, qametsQatan: true, shevaAfterMeteg: false,
  shevaWithMeteg: true, sqnmlvy: false, strict: true, wawShureq: false
};

const out = {};
for (const [k,v] of Object.entries(cases)) {
  out[k] = { hebrew: v, ipa: transliterate(v, tiberian) };
  const t = new Text(v, sylOpts);
  out[k].syllables = t.words.map(w => ({
    text: w.text,
    syls: w.syllables.map(s => ({
      text: s.text,
      isClosed: s.isClosed,
      isAccented: s.isAccented,
      onset: s.onset,
      coda: s.coda,
    }))
  }));
}
fs.writeFileSync('../native/tests/fixtures/js_oracle.json', JSON.stringify(out, null, 2));
console.log('ok', Object.keys(out));
