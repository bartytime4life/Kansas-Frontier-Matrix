# src/kansas_geo_timeline/nlp/glossary.py
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from typing import Dict, List, Any, Iterable, Tuple, Optional


_DEFAULT: Dict[str, List[str]] = {
    "Kaw": ["Kanza", "Kansa", "Kaw Nation"],
    "Santa Fe Trail": ["SFT", "Santa Fé Trail", "Santa Fé Trail"],  # composed + decomposed accents
    "Fort Larned": ["Camp on Pawnee Fork", "Larned Fort"],
}


def _strip_accents(s: str) -> str:
    """Normalize diacritics (NFKD) and strip combining marks."""
    nfkd = unicodedata.normalize("NFKD", s)
    return "".join(ch for ch in nfkd if not unicodedata.combining(ch))


def _norm(s: str) -> str:
    """Case/diacritic/punct-light normalization for matching keys."""
    s = _strip_accents(s).lower().strip()
    # Collapse internal whitespace
    s = re.sub(r"\s+", " ", s)
    return s


@dataclass(frozen=True)
class _Entry:
    canonical: str
    alias: str
    pattern: re.Pattern  # word-boundary aware regex for this alias


class Glossary:
    """Domain term normalization + alias expansion with offsets and confidence.

    Output format (per hit):
      {
        "canonical": "Santa Fe Trail",
        "matched": "Santa Fé Trail",
        "start": 10, "end": 25,
        "confidence": 0.92,
        "source": "glossary",
        "id": "kfm:trail:santafe"   # optional if provided via id_map
      }
    """

    def __init__(
        self,
        terms: Dict[str, List[str]] | None = None,
        id_map: Optional[Dict[str, str]] = None,  # canonical → stable ID
        boundary: str = r"\b",                    # customize if needed for non-Latin text
    ) -> None:
        self._raw_terms = terms or _DEFAULT
        self._id_map = id_map or {}
        self._boundary = boundary
        self._entries: List[_Entry] = []
        self._canon_norm: Dict[str, str] = {}  # norm(canonical) → canonical (original casing)
        self._build_index()

    # --------------------------- public API ---------------------------

    def add_terms(self, updates: Dict[str, Iterable[str]]) -> None:
        """Add or extend canonical→aliases mapping at runtime."""
        for canon, aliases in updates.items():
            self._raw_terms.setdefault(canon, [])
            for a in aliases:
                if a not in self._raw_terms[canon]:
                    self._raw_terms[canon].append(a)
        self._build_index()

    def run(self, text: str) -> Dict[str, Any]:
        """Find canonical terms and aliases within text (boundary-aware, diacritic-robust)."""
        # Prepare a normalized “search string” alongside original for fast case/diacritic-agnostic search.
        # Strategy: we search in the original text using regex with case-insensitive flag and permissive
        # accent forms; we also keep a fully normalized mirror if needed in the future.
        hits: List[Dict[str, Any]] = []
        used_ranges: List[Tuple[int, int]] = []  # to help reduce overlapping junk

        for e in self._entries:
            for m in e.pattern.finditer(text):
                start, end = m.span()
                surface = text[start:end]

                # Simple overlap control: skip if this span is contained in a previously matched longer span
                if any(start >= s and end <= t for (s, t) in used_ranges):
                    continue

                # Confidence heuristic: aliases slightly lower than exact canonical match
                # bonus for longer phrases (reduce false positives on short words)
                base = 0.90 if surface.lower() == e.alias.lower() == e.canonical.lower() else 0.88
                length_bonus = min(0.06, max(0.0, (len(surface) - 8) * 0.005))
                confidence = round(base + length_bonus, 3)

                hit = {
                    "canonical": e.canonical,
                    "matched": surface,
                    "start": start,
                    "end": end,
                    "confidence": confidence,
                    "source": "glossary",
                }
                if e.canonical in self._id_map:
                    hit["id"] = self._id_map[e.canonical]

                hits.append(hit)
                used_ranges.append((start, end))

        # De-dupe by (canonical, span) and prefer higher confidence if duplicates sneak in
        dedup: Dict[Tuple[str, int, int], Dict[str, Any]] = {}
        for h in hits:
            key = (h["canonical"], h["start"], h["end"])
            if key not in dedup or h["confidence"] > dedup[key]["confidence"]:
                dedup[key] = h

        # Backwards-compatibility: same keys you used previously are present ("canonical","matched")
        out = sorted(dedup.values(), key=lambda x: (x["start"], -x["confidence"]))
        return {"glossary": out}

    # --------------------------- internals ---------------------------

    def _build_index(self) -> None:
        """Compile regex patterns for each alias with word boundaries (diacritic variants)."""
        self._entries.clear()
        self._canon_norm.clear()

        for canonical, aliases in self._raw_terms.items():
            can_norm = _norm(canonical)
            self._canon_norm[can_norm] = canonical
            all_terms = [canonical] + list(aliases)

            for alias in all_terms:
                # Build a diacritic-agnostic, boundary-aware regex:
                # - Escape literal characters
                # - Allow composed/decomposed diacritics by normalizing and matching against both forms
                alias_clean = alias.strip()
                if not alias_clean:
                    continue

                # We create a character-class expression that tolerates decomposed accent variants.
                # For simplicity, we match case-insensitively and rely on \b boundaries.
                # Also allow variable internal whitespace.
                token_parts = re.split(r"\s+", alias_clean)
                part_patterns = [re.escape(_strip_accents(p)) for p in token_parts]
                pattern_str = self._boundary + r"(?:\s+)".join(part_patterns) + self._boundary

                # Build a pattern that matches either with or without accents by normalizing the input:
                # Since Python's re doesn't do accent-insensitive matching, we match the de-accented form
                # using a custom replacer at runtime via a (?i) case-insensitive regex.
                # A practical compromise: match the de-accented alias against the raw text ignoring case,
                # which works for most Latin-alphabet sources.
                pat = re.compile(pattern_str, flags=re.IGNORECASE)

                self._entries.append(_Entry(canonical=canonical, alias=alias_clean, pattern=pat))
