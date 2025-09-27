# src/kansas_geo_timeline/nlp/date_extractor.py
from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Tuple

try:
    import dateparser  # optional
except Exception:  # pragma: no cover
    dateparser = None

# ---------------------- month tables & helpers ----------------------

_MONTHS_FULL = (
    "january|february|march|april|may|june|july|august|"
    "september|october|november|december"
)
_MONTHS_ABBR = "jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec"
_MONTH_RX = rf"(?:{_MONTHS_FULL}|{_MONTHS_ABBR})"

# Day with optional ordinal suffix (1st, 2nd, 3rd, 4th...)
_DAY_RX = r"(?P<day>[0-3]?\d)(?:st|nd|rd|th)?"
_YEAR_RX = r"(?P<year>\d{4})"
_YEAR_RX_NAMED = r"(?P<y>\d{4})"
_RANGE_SEP = r"[–—-]"  # en dash, em dash, hyphen

# ---------------------- compiled patterns ----------------------
# Order matters: more specific first.
_PATTERNS: List[Tuple[str, re.Pattern]] = [
    # ISO-like: YYYY-MM-DD or YYYY/MM/DD
    ("ymd_iso", re.compile(rf"\b(?P<y>\d{{4}})[-/](?P<m>\d{{1,2}})[-/](?P<d>\d{{1,2}})\b")),
    # Month D, YYYY  (with optional comma)
    ("mdy_commas", re.compile(rf"\b(?P<mon>{_MONTH_RX})\s+{_DAY_RX}\s*,?\s*(?P<y>\d{{4}})\b", re.I)),
    # D Month YYYY
    ("dmy_words", re.compile(rf"\b{_DAY_RX}\s+(?P<mon>{_MONTH_RX})\s+(?P<y>\d{{4}})\b", re.I)),
    # Month YYYY
    ("my_words", re.compile(rf"\b(?P<mon>{_MONTH_RX})\s+(?P<y>\d{{4}})\b", re.I)),
    # Numeric M/D/YYYY
    ("mdy_num", re.compile(r"\b(?P<m>\d{1,2})/(?P<d>\d{1,2})/(?P<y>\d{4})\b")),
    # Range YYYY–YYYY (or hyphen)
    ("yy_range", re.compile(rf"\b(?P<y1>\d{{4}})\s*{_RANGE_SEP}\s*(?P<y2>\d{{4}})\b")),
    # Bare year
    ("year_only", re.compile(rf"\b{_YEAR_RX_NAMED}\b")),
]

_MONTH_MAP = {
    "jan": 1, "january": 1,
    "feb": 2, "february": 2,
    "mar": 3, "march": 3,
    "apr": 4, "april": 4,
    "may": 5,
    "jun": 6, "june": 6,
    "jul": 7, "july": 7,
    "aug": 8, "august": 8,
    "sep": 9, "sept": 9, "september": 9,
    "oct": 10, "october": 10,
    "nov": 11, "november": 11,
    "dec": 12, "december": 12,
}


def _clamp_md(m: int, d: int) -> Tuple[int, int]:
    """Clamp obviously invalid month/day into valid ranges (defensive for OCR)."""
    m = max(1, min(12, int(m)))
    d = max(1, min(31, int(d)))
    return m, d


def _norm_ymd(y: int, m: Optional[int] = None, d: Optional[int] = None) -> Tuple[str, str]:
    """Return (iso, granularity)."""
    if m is None:
        return (f"{y:04d}-01-01", "year")
    if d is None:
        m, _ = _clamp_md(m, 1)
        return (f"{y:04d}-{m:02d}-01", "month")
    m, d = _clamp_md(m, d)
    return (f"{y:04d}-{m:02d}-{d:02d}", "day")


def _parse_month(mon: str) -> Optional[int]:
    return _MONTH_MAP.get(mon.strip().lower())


def _mk_range(y1: int, y2: int) -> Tuple[str, str]:
    """Normalize a year range into full-ISO bounds with granularity=range."""
    if y2 < y1:
        y1, y2 = y2, y1
    return (f"{y1:04d}-01-01/{y2:04d}-12-31", "range")


def _score(granularity: str) -> float:
    # Favor more specific dates
    return {"day": 0.95, "month": 0.9, "year": 0.8, "range": 0.85}.get(granularity, 0.8)


def _maybe_dateparser(raw: str, prefer_day_first: bool) -> Optional[Tuple[str, str]]:
    if not dateparser:
        return None
    dt = dateparser.parse(
        raw,
        settings={
            "PREFER_DAY_OF_MONTH": "first",
            "DATE_ORDER": "DMY" if prefer_day_first else "MDY",
            "RELATIVE_BASE": None,
            "RETURN_AS_TIMEZONE_AWARE": False,
        },
    )
    if not dt:
        return None
    return (dt.date().isoformat(), "day")


class DateExtractor:
    """Extract explicit/implicit dates and ranges, normalized to ISO.

    Output schema:
        {
          "dates": [
            {"text": "May 4, 1865", "value": "1865-05-04", "granularity": "day", "confidence": 0.95, "source": "mdy_commas"},
            {"text": "1860–1865", "value": "1860-01-01/1865-12-31", "granularity": "range", "confidence": 0.85, "source": "yy_range"}
          ]
        }
    """

    def __init__(self, prefer_day_first: bool = False) -> None:
        self.prefer_day_first = prefer_day_first

    def _norm(self, tag: str, m: re.Match) -> Optional[Tuple[str, str]]:
        """Pattern-specific normalization → (value, granularity)."""
        gd = m.groupdict()
        if tag == "ymd_iso":
            y, mm, dd = int(gd["y"]), int(gd["m"]), int(gd["d"])
            return _norm_ymd(y, mm, dd)
        if tag == "mdy_commas":
            mon = _parse_month(gd["mon"])
            if mon:
                return _norm_ymd(int(gd["y"]), mon, int(gd["day"]))
        if tag == "dmy_words":
            mon = _parse_month(gd["mon"])
            if mon:
                return _norm_ymd(int(gd["y"]), mon, int(gd["day"]))
        if tag == "my_words":
            mon = _parse_month(gd["mon"])
            if mon:
                return _norm_ymd(int(gd["y"]), mon, None)
        if tag == "mdy_num":
            return _norm_ymd(int(gd["y"]), int(gd["m"]), int(gd["d"]))
        if tag == "yy_range":
            return _mk_range(int(gd["y1"]), int(gd["y2"]))
        if tag == "year_only":
            return _norm_ymd(int(gd["y"]), None, None)
        return None

    def run(self, text: str) -> Dict[str, Any]:
        findings: List[Dict[str, Any]] = []

        # Pass 1: regex patterns (precise → broad)
        for tag, rx in _PATTERNS:
            for m in rx.finditer(text):
                raw = m.group(0)
                ng = self._norm(tag, m)
                if not ng and tag not in ("yy_range", "year_only"):
                    # If not normalized by hand, try dateparser as a last resort
                    dp = _maybe_dateparser(raw, self.prefer_day_first)
                    if dp:
                        iso, gran = dp
                        findings.append({
                            "text": raw,
                            "value": iso,
                            "granularity": gran,
                            "confidence": _score(gran) - 0.05,
                            "source": f"{tag}+dateparser",
                        })
                        continue
                if ng:
                    iso, gran = ng
                    findings.append({
                        "text": raw,
                        "value": iso,
                        "granularity": gran,
                        "confidence": _score(gran),
                        "source": tag,
                    })

        # Pass 2: de-duplicate by normalized value, keep highest confidence / most specific
        best: Dict[str, Dict[str, Any]] = {}
        for f in findings:
            v = f["value"]
            if v not in best or f["confidence"] > best[v]["confidence"]:
                best[v] = f

        # Stable order: by start date ascending when comparable
        def _start_key(val: str) -> str:
            return val.split("/")[0] if "/" in val else val

        out = sorted(best.values(), key=lambda x: _start_key(x["value"]))
        return {"dates": out}
