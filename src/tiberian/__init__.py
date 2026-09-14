"""Tiberian Hebrew IPA transcription — corpus-driven, fail-closed."""

from tiberian.api import Result, TranscribeProfile, transcribe
from tiberian.profiles import DEFAULT_PROFILE, Profile

__all__ = [
    "Result",
    "TranscribeProfile",
    "transcribe",
    "Profile",
    "DEFAULT_PROFILE",
    "__version__",
]

__version__ = "0.1.0"
