#!/usr/bin/env node
/**
 * postinstall: patch hebrew-transliteration dist/rules.js for deḥiq.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const MARKER = "/* khan-dehiq-patch */";
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rulesPath = path.resolve(
  __dirname,
  "../node_modules/hebrew-transliteration/dist/rules.js"
);

if (!fs.existsSync(rulesPath)) {
  console.warn("patch-hebtrans: hebrew-transliteration not installed; skip");
  process.exit(0);
}

let src = fs.readFileSync(rulesPath, "utf8");
if (src.includes(MARKER)) {
  console.log("patch-hebtrans: already applied");
  process.exit(0);
}

const constructNeedle =
  "if (prevWord?.isInConstruct && !prevWord.syllables[prevWord.syllables.length - 1].isClosed) {\n        return true;\n    }";
if (!src.includes(constructNeedle)) {
  console.error("patch-hebtrans: construct needle missing");
  process.exit(1);
}
src = src.replace(
  constructNeedle,
  constructNeedle +
    `\n    ${MARKER}\n    {\n        const word = cluster.syllable?.word;\n        if (prevWord && word && globalThis.__khanIsDehiqPair?.(prevWord, word)) {\n            return true;\n        }\n    }`
);

const stressNeedle =
  'if (location === "before-syllable") {\n        const isDoubled = syl.clusters.map((c) => isDageshChazaq(c, schema)).includes(true);\n        if (isDoubled) {\n            const firstCluster = syl.clusters[0];';
if (!src.includes(stressNeedle)) {
  console.error("patch-hebtrans: stress needle missing");
  process.exit(1);
}
src = src.replace(
  stressNeedle,
  `if (location === "before-syllable") {\n        const isDoubled = syl.clusters.map((c) => isDageshChazaq(c, schema)).includes(true);\n        if (isDoubled) {\n            ${MARKER}\n            if (!syl.prev) {\n                return \`\${mark}\${text}\`;\n            }\n            const firstCluster = syl.clusters[0];`
);

fs.writeFileSync(rulesPath, src);
console.log("patch-hebtrans: applied", rulesPath);
