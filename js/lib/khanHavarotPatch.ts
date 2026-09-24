/**
 * Patch havarotjs Word.syllables so furtive pataḥ never bears stress
 * (native syllabifier `_shift_accent_off_furtive`).
 *
 * Must be imported before any transliterate() call.
 */
import { Word } from "havarotjs";
import type { Syllable } from "havarotjs";

const TAAMIM_METEG_SOF = /[\u0591-\u05AF\u05BD\u05C3]/gu;
const FURTIVE_END = /(?:\u05D7|\u05E2|\u05D4\u05BC)\u05B7$/u;

function plainForFurtive(text: string): string {
  return text.replace(TAAMIM_METEG_SOF, "");
}

function isFurtiveSyllable(syl: Syllable): boolean {
  if (!syl.isFinal || syl.isClosed) return false;
  return FURTIVE_END.test(plainForFurtive(syl.text));
}

function shiftAccentOffFurtive(syllables: Syllable[]): void {
  for (let i = 0; i < syllables.length; i++) {
    const syl = syllables[i];
    if (!syl.isAccented || !isFurtiveSyllable(syl)) continue;
    syl.isAccented = false;
    if (i > 0) syllables[i - 1].isAccented = true;
    return;
  }
}

let patched = false;

export function applyKhanHavarotPatch(): void {
  if (patched) return;
  patched = true;

  const desc = Object.getOwnPropertyDescriptor(Word.prototype, "syllables");
  if (!desc?.get) {
    throw new Error("havarotjs Word.syllables getter not found — cannot patch furtive accent");
  }
  const originalGet = desc.get;

  Object.defineProperty(Word.prototype, "syllables", {
    configurable: true,
    enumerable: desc.enumerable,
    get(this: Word) {
      const syllables = originalGet.call(this) as Syllable[];
      shiftAccentOffFurtive(syllables);
      return syllables;
    },
  });
}

// Apply on import so runner / schemas always see the fix.
applyKhanHavarotPatch();
