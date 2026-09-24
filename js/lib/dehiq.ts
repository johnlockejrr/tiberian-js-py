/**
 * Deḥiq detection — Khan T1 §I.2.8.1.2 (port of native hebtrans/dehiq.py).
 */
import type { Word } from "havarotjs";

const CONJUNCTIVE = /[\u05A3-\u05AA\u05AC]/u;
const GUTTURAL_ONSET = /[אהחע]/u;

function sylHasMeteg(syl: { clusters: { hasMeteg: boolean }[] }): boolean {
  return syl.clusters.some((c) => c.hasMeteg);
}

function penultimatelyStressed(word: Word): boolean {
  const syls = word.syllables;
  if (syls.length < 2 || syls[syls.length - 1].isAccented) return false;
  return syls.slice(0, -1).some((s) => s.isAccented || sylHasMeteg(s));
}

function finalIsLaxOpen(word: Word): boolean {
  const syls = word.syllables;
  if (!syls.length) return false;
  const final = syls[syls.length - 1];
  if (final.isClosed) return false;
  if (sylHasMeteg(final)) return false;
  const names = final.vowelNames;
  return Boolean(names.length && (names[0] === "QAMATS" || names[0] === "SEGOL"));
}

function initialFootStressed(word: Word): boolean {
  const syls = word.syllables;
  if (!syls.length) return false;
  if (syls[0].isAccented) return true;
  if (
    syls.length > 1 &&
    syls[0].vowelNames.length === 1 &&
    syls[0].vowelNames[0] === "SHEVA" &&
    syls[1].isAccented
  ) {
    return true;
  }
  return false;
}

function followingHasDagesh(word: Word): boolean {
  const syls = word.syllables;
  if (!syls.length || !syls[0].clusters.length) return false;
  return /\u05BC/u.test(syls[0].clusters[0].text);
}

export function isDehiqPair(first: Word | null | undefined, second: Word | null | undefined): boolean {
  if (!first || !second) return false;
  if (!penultimatelyStressed(first)) return false;
  if (!finalIsLaxOpen(first)) return false;
  const bound = first.isInConstruct || CONJUNCTIVE.test(first.text);
  if (!bound) return false;
  if (!initialFootStressed(second)) return false;
  const onset = sylsOnset(second);
  if (GUTTURAL_ONSET.test(onset || "")) return false;
  if (!followingHasDagesh(second)) return false;
  return true;
}

function sylsOnset(word: Word): string {
  const syls = word.syllables;
  return syls.length ? syls[0].onset : "";
}

export function wordIsDehiqHost(word: Word): boolean {
  const nxt = word.next?.value ?? null;
  return isDehiqPair(word, nxt);
}
