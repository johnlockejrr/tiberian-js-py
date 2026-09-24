#!/usr/bin/env node
/**
 * Tiberian IPA runner — applies js/schemas/tiberian.ts via hebrew-transliteration
 * + havarotjs syllabification.
 *
 * stdin JSON: { "text": "<hebrew>" }
 * stdout JSON: { "ipa": "...", "engine": "...", "schema": "js/schemas/tiberian.ts" }
 */
import "./lib/khanHavarotPatch.ts";
import "./lib/patchHebTrans.ts";
import { transliterate } from "hebrew-transliteration";
import { tiberian } from "./schemas/tiberian.ts";

async function readStdin(): Promise<string> {
  const chunks: Buffer[] = [];
  for await (const chunk of process.stdin) chunks.push(chunk as Buffer);
  return Buffer.concat(chunks).toString("utf8");
}

function bareIpa(s: string): string {
  return String(s)
    .replace(/^\[|\]$/g, "")
    .replace(/\s+/g, " ")
    .trim();
}

const raw = (await readStdin()).trim();
if (!raw) {
  console.error("runner: empty stdin");
  process.exit(2);
}

let payload: { text?: string; hebrew?: string };
try {
  payload = JSON.parse(raw);
} catch {
  payload = { text: raw };
}

const text = payload.text ?? payload.hebrew ?? "";
if (!String(text).trim()) {
  console.error("runner: missing text");
  process.exit(2);
}

try {
  const ipa = bareIpa(transliterate(text, tiberian));
  process.stdout.write(
    JSON.stringify({
      ipa,
      engine: "hebrew-transliteration",
      schema: "js/schemas/tiberian.ts",
    })
  );
} catch (err) {
  const e = err as Error;
  process.stderr.write(String(e?.stack || e));
  process.exit(1);
}
