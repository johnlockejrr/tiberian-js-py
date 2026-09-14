"""Transcription profiles (Standard Tiberian streams; do not blend BA/BN)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

Tradition = Literal["ben_asher", "ben_naftali"]
Stream = Literal["forte_lene", "extended_forte"]
VavMode = Literal["default_v", "w_glide"]


@dataclass(frozen=True)
class Profile:
    name: str
    tradition: Tradition = "ben_asher"
    stream: Stream = "forte_lene"
    vav: VavMode = "default_v"
    # When True, emit half-long / stress marks following I.5 sample conventions where rules support them.
    emit_prosody: bool = True


DEFAULT_PROFILE = Profile(
    name="standard-ben-asher-forte-lene",
    stream="forte_lene",
)
# Opt-in only: second I.5.4 reading with prolonged BGDKPT (extended dagesh forte).
EXTENDED_FORTE = Profile(
    name="standard-ben-asher-extended-forte",
    stream="extended_forte",
)
BEN_NAFTALI = Profile(
    name="standard-ben-naftali-forte-lene",
    tradition="ben_naftali",
)

PROFILES = {
    DEFAULT_PROFILE.name: DEFAULT_PROFILE,
    EXTENDED_FORTE.name: EXTENDED_FORTE,
    BEN_NAFTALI.name: BEN_NAFTALI,
    "forte_lene": DEFAULT_PROFILE,
    "extended_forte": EXTENDED_FORTE,
    "ben_asher": DEFAULT_PROFILE,
    "ben_naftali": BEN_NAFTALI,
}


def resolve_profile(name: str | Profile | None) -> Profile:
    if name is None:
        return DEFAULT_PROFILE
    if isinstance(name, Profile):
        return name
    key = name.strip().lower().replace("-", "_")
    if name in PROFILES:
        return PROFILES[name]
    if key in PROFILES:
        return PROFILES[key]
    raise ValueError(
        f"Unknown profile {name!r}. Known: {sorted(set(PROFILES))}"
    )
