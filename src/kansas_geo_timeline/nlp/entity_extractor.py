# src/kansas_geo_timeline/nlp/entity_extractor.py
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional, Tuple

# -------- optional spaCy --------
try:
    import spacy  # type: ignore
    _NLP: Optional["spacy.language.Language"] = spacy.load("en_core_web_sm")
except Exception:
    _NLP = None

# -------- fallback patterns --------
# Capture up to 4 capitalized tokens (proper-noun-ish), allowing hyphens/apostrophes.
# We don't anchor word boundaries too aggressively to keep offsets sane around punctuation.
_CAP_TOKEN = r"[A-Z][a-z]+(?:[-'][A-Za-z]+)?"
_CAP_SEQ = re.compile(rf"({ _CAP_TOKEN }(?:\s+{ _CAP_TOKEN }){{0,3}})")

# Trailing punctuation/quotes to trim from surface forms
_TRIM = re.compile(r"^[\"'“”‘’\(\[]+|[\"'“”‘’\)\],.:;!?]+$")

# Common capitalized words that are rarely entities (reduce false positives)
_STOP = {
    "The", "A", "An", "And", "On", "In", "Of", "For", "To", "From",
    # Months/Weekdays to avoid flooding
    "January","February","March","April","May","June","July","August","September","October","November","December",
    "Mon","Tue","Tues","Wednesday","Thu","Thur","Friday","Saturday","Sunday",
}

# Map regex-fallback guess to a coarse label
def _fallback_label(text: str) -> str:
    # Heuristics: ends with "Trail", "River", "Fort", etc.
    t = text.strip()
    if any(t.endswith(suf) for suf in (" Trail", " River", " Creek", " Fork", " Ridge", " Lake", " Prairie", " Canyon")):
        return "LOC"
    if any(t.startswith(pre) for pre in ("Fort ", "Camp ", "Station ")):
        return "FAC"
    if any(t.endswith(suf) for suf in (" Company", " Co.", " Railroad", " RR", " University", " Church")):
        return "ORG"
    # Names with space likely PERSON or ORG; default to MISC
    return "MISC"

@dataclass(frozen=True)
class _Span:
    start: int
    end: int
    text: str
    label: str
    confidence: float
    source: str

    def key_ci(self) -> Tuple[str, str]:
        return (self.text.lower(), self.label)

    def overlaps(self, other: "_Span") -> bool:
        return not (self.end <= other.start or other.end <= self.start)

def _trim(text: str) -> str:
    # Remove leading/trailing quotes/punct while preserving core text
    return _TRIM.sub("", text)

def _merge_overlaps(spans: List[_Span]) -> List[_Span]:
    """Prefer longer, higher-confidence spans when they overlap."""
    if not spans:
        return spans
    # Sort by (start asc, -length desc, confidence desc)
    spans.sort(key=lambda s: (s.start, -(s.end - s.start), -s.confidence))
    kept: List[_Span] = []
    for s in spans:
        if any(s.overlaps(k) and ( (k.end - k.start) >= (s.end - s.start) and k.confidence >= s.confidence ) for k in kept):
            continue
        # Remove any existing kept that s dominates
        kept = [k for k in kept if not (s.overlaps(k) and ( (s.end - s.start) > (k.end - k.start) or s.confidence > k.confidence ))]
        kept.append(s)
    return kept

def _dedupe_case_insensitive(spans: Iterable[_Span]) -> List[_Span]:
    seen: set[Tuple[str, str]] = set()
    out: List[_Span] = []
    for s in spans:
        key = s.key_ci()
        if key in seen:
            continue
        seen.add(key)
        out.append(s)
    return out

class EntityExtractor:
    """Named entities with optional spaCy; robust regex fallback; optional gazetteer.

    Returns:
      {"entities": [{"text","label","start","end","confidence","source"}, ...]}
    """

    def __init__(
        self,
        use_spacy: bool = True,
        gazetteer: Optional[Dict[str, str] | Iterable[str]] = None,
        min_len: int = 2,
    ) -> None:
        self.use_spacy = bool(use_spacy and _NLP)
        self.min_len = max(1, int(min_len))

        # Normalize gazetteer to a dict[str, label] (case-sensitive keys)
        if gazetteer is None:
            self.gazetteer: Dict[str, str] = {}
        elif isinstance(gazetteer, dict):
            self.gazetteer = {str(k): str(v) for k, v in gazetteer.items()}
        else:
            self.gazetteer = {str(k): "GAZ" for k in gazetteer}

    # --------------- main API ---------------

    def run(self, text: str) -> Dict[str, Any]:
        spans: List[_Span] = []

        # 1) Gazetteer exact matches first (highest confidence)
        if self.gazetteer:
            spans.extend(self._run_gazetteer(text))

        # 2) spaCy (if available)
        if self.use_spacy and _NLP:
            spans.extend(self._run_spacy(text))

        # 3) Regex fallback
        spans.extend(self._run_regex(text))

        # Merge overlaps and de-dupe
        spans = _merge_overlaps(spans)
        spans = _dedupe_case_insensitive(spans)

        ents = [
            {"text": s.text, "label": s.label, "start": s.start, "end": s.end,
             "confidence": round(float(s.confidence), 3), "source": s.source}
            for s in spans
        ]
        return {"entities": ents}

    # --------------- strategies ---------------

    def _run_gazetteer(self, text: str) -> List[_Span]:
        spans: List[_Span] = []
        # Search each gazetteer entry literally; prefer longest-first to avoid nested duplicates
        for key, lbl in sorted(self.gazetteer.items(), key=lambda kv: len(kv[0]), reverse=True):
            start = 0
            while True:
                idx = text.find(key, start)
                if idx == -1:
                    break
                end = idx + len(key)
                # Boundaries: avoid partial word matches (letters on either side)
                if (idx == 0 or not text[idx-1].isalnum()) and (end == len(text) or not text[end:end+1].isalnum()):
                    spans.append(_Span(idx, end, key, lbl, 0.96, "gazetteer"))
                start = end
        return spans

    def _run_spacy(self, text: str) -> List[_Span]:
        spans: List[_Span] = []
        try:
            doc = _NLP(text)  # type: ignore
            for e in doc.ents:
                raw = _trim(e.text)
                if not raw or raw in _STOP or len(raw) < self.min_len:
                    continue
                start = e.start_char + (0 if raw == e.text else text[e.start_char:e.end_char].find(raw))
                end = start + len(raw)
                # spaCy doesn't provide scores in small model; set strong baseline
                spans.append(_Span(start, end, raw, e.label_, 0.90, "spacy"))
        except Exception:
            # If spaCy fails, skip silently (regex fallback will still run)
            pass
        return spans

    def _run_regex(self, text: str) -> List[_Span]:
        spans: List[_Span] = []
        for m in _CAP_SEQ.finditer(text):
            raw = _trim(m.group(1))
            if not raw or raw in _STOP or len(raw) < self.min_len:
                continue
            # Heuristic filters: drop sentence-initial single words like "The"
            if m.start() == 0 and " " not in raw and raw in _STOP:
                continue
            label = _fallback_label(raw)
            spans.append(_Span(m.start(), m.end(), raw, label, 0.62, "regex"))
        return spans
