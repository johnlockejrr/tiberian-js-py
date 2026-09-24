/**
 * Patch hebrew-transliteration rules for deḥiq gemination + word-initial stress.
 *
 * Stock isDageshChazaq only treats maqqef-construct; deḥiq needs the same
 * doubling. Word-initial geminates take stress before the whole onset (ˈbb…),
 * not mid-geminate (bˈb…).
 *
 * Applied by rewriting dist/rules.js on postinstall (and at first import if needed).
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { isDehiqPair } from "./dehiq.ts";

const MARKER = "/* khan-dehiq-patch */";

const DEHIQ_BLOCK = `${MARKER}
    {
        const word = cluster.syllable?.word;
        if (prevWord && word && globalThis.__khanIsDehiqPair?.(prevWord, word)) {
            return true;
        }
    }
`;

const STRESS_BLOCK = `${MARKER}
        if (!syl.prev) {
            return \`\${mark}\${text}\`;
        }
`;

export function applyHebTransRulesSourcePatch(): boolean {
  const rulesPath = path.resolve(
    path.dirname(fileURLToPath(import.meta.url)),
    "../node_modules/hebrew-transliteration/dist/rules.js"
  );
  if (!fs.existsSync(rulesPath)) {
    return false;
  }
  let src = fs.readFileSync(rulesPath, "utf8");
  if (src.includes(MARKER)) return true;

  // Insert deḥiq check after construct check in isDageshChazaq
  const constructNeedle =
    "if (prevWord?.isInConstruct && !prevWord.syllables[prevWord.syllables.length - 1].isClosed) {\n        return true;\n    }";
  if (!src.includes(constructNeedle)) {
    throw new Error("hebrew-transliteration rules.js: construct check not found");
  }
  src = src.replace(
    constructNeedle,
    constructNeedle + "\n    " + DEHIQ_BLOCK.trimStart()
  );

  // Word-initial geminate stress before whole onset
  const stressNeedle =
    "if (location === \"before-syllable\") {\n        const isDoubled = syl.clusters.map((c) => isDageshChazaq(c, schema)).includes(true);\n        if (isDoubled) {\n            const firstCluster = syl.clusters[0];";
  if (!src.includes(stressNeedle)) {
    throw new Error("hebrew-transliteration rules.js: stress doubled block not found");
  }
  src = src.replace(
    stressNeedle,
    `if (location === "before-syllable") {\n        const isDoubled = syl.clusters.map((c) => isDageshChazaq(c, schema)).includes(true);\n        if (isDoubled) {\n            ${STRESS_BLOCK.trim()}\n            const firstCluster = syl.clusters[0];`
  );

  fs.writeFileSync(rulesPath, src);
  return true;
}

/** Runtime hook used by the patched isDageshChazaq. */
export function installDehiqRuntimeHook(): void {
  (globalThis as unknown as { __khanIsDehiqPair: typeof isDehiqPair }).__khanIsDehiqPair =
    isDehiqPair;
}

let ready = false;

export function ensureHebTransDehiqPatch(): void {
  if (ready) return;
  installDehiqRuntimeHook();
  try {
    applyHebTransRulesSourcePatch();
  } catch {
    // Source already patched or path missing — runtime hook still helps after patch.
  }
  ready = true;
}

// Apply as early as possible (before hebrew-transliteration is loaded by importers).
ensureHebTransDehiqPatch();
