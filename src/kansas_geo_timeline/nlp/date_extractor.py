from __future__ import annotations
import re
from typing import Any, Dict, List, Optional, Tuple

try:
    import dateparser  # optional
except Exception:
    dateparser = None

# Simple patterns: YYYY, Month YYYY, M/D/YYYY, YYYY–YYYY ranges
_YEAR = r"(?P<year>\d{4})"
_MONTHS = ("january|february|march|april|may|june|july|august|"
           "september|october|november|december")
_PATTERNS = [
    re.compile(rf"\b(?P<y1>\d{{4}})\s*[–-]\s*(?P<y2>\d{{4}})\b", re.I),
    re.compile(rf"\b({_MONTHS})\s+(?P<year>\d{{4}})\b", re.I),
    re.compile(r"\b(?P<m>\d{1,2})/(?P<d>\d{1,2})/(?P<y>\d{4})\b"),
    re.compile(rf"\b{_YEAR}\b"),
]


class DateExtractor:
    """Extract explicit/implicit dates; returns normalized ISO candidates with confidence."""

    def __init__(self, prefer_day_first: bool = False) -> None:
        self.prefer_day_first = prefer_day_first

    def _norm(self, s: str) -> Optional[str]:
        if dateparser:
            dt = dateparser.parse(s, settings={"PREFER_DAY_OF_MONTH": "first", "DATE_ORDER": "DMY" if self.prefer_day_first else "MDY"})
            if dt:
                return dt.date().isoformat()
        # Heuristic: year only
        m = re.fullmatch(r"\d{4}", s)
        if m:
            return f"{s}-01-01"
        return None

    def run(self, text: str) -> Dict[str, Any]:
        findings: List[Dict[str, Any]] = []
        for rx in _PATTERNS:
            for m in rx.finditer(text):
                raw = m.group(0)
                iso = self._norm(raw)
                if not iso and (m.lastgroup in ("y1", "y2", "year")):
                    # Range or year patterns
                    y1 = m.groupdict().get("y1") or m.groupdict().get("year")
                    y2 = m.groupdict().get("y2")
                    if y1 and not y2:
                        iso = f"{y1}-01-01"
                    elif y1 and y2:
                        iso = f"{y1}-01-01/{y2}-12-31"
                if iso:
                    findings.append({"text": raw, "value": iso, "confidence": 0.8})
        # De-duplicate by value
        uniq = {}
        for f in findings:
            uniq[f["value"]] = f
        return {"dates": list(uniq.values())}
