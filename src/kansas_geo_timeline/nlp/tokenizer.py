# src/kansas_geo_timeline/nlp/tokenizer.py
from __future__ import annotations

import re
from typing import List, Dict, Any, Optional, Tuple

# ---------- optional spaCy ----------
try:
    import spacy  # type: ignore
    _NLP: Optional["spacy.language.Language"] = spacy.load("en_core_web_sm")
except Exception:  # spaCy may be missing
    _NLP = None

# ---------- regex fallback rules ----------
# Common abbreviations that should not trigger sentence breaks.
_ABBR = {
    "mr.", "mrs.", "ms.", "dr.", "prof.", "sr.", "jr.",
    "u.s.", "u.k.", "e.g.", "i.e.", "etc.", "vs.", "st.", "mt.", "no.", "fig.", "al.",
}

# Sentence boundary: ., !, ?, possibly followed by closing quotes/brackets, then whitespace/newline.
# We'll post-filter with abbreviation checks.
_SENT_BOUNDARY = re.compile(r"""
    (?P<end>[.!?])                 # terminal punctuation
    (?P<closers>["'”’\)\]]*)       # optional closing quotes/brackets
    (?=\s+|$)                      # followed by whitespace or end of text
""", re.VERBOSE)

# Token pattern:
# - Words with unicode letters, digits
# - Allow internal hyphens/apostrophes (e.g., "Santa-Fe", "o'clock")
# - Capture numbers and simple punctuation as separate tokens when needed
_WORD = r"[0-9\p{L}]+(?:[-'][0-9\p{L}]+)*"
# Python's 're' doesn't support \p{L}; approximate with \w plus added letters via Unicode flag.
# We'll use a more permissive class and filter later.
_TOKEN_RX = re.compile(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*|[^\sA-Za-z0-9]", re.UNICODE)


def _is_abbrev(segment: str) -> bool:
    """Return True if a tail segment like 'Dr.' or 'U.S.' is a known abbreviation."""
    s = segment.strip().lower()
    # Quick path: direct membership
    if s in _ABBR:
        return True
    # U.S.A.-style acronyms with dots: X.X. or X.X.X.
    if re.fullmatch(r"(?:[a-z]\.){2,}", s):
        return True
    return False


def _sentence_split_regex(text: str) -> List[Tuple[int, int]]:
    """Return list of (start, end) spans for sentences using regex fallback."""
    spans: List[Tuple[int, int]] = []
    n = len(text)
    if n == 0:
        return spans

    start = 0
    for m in _SENT_BOUNDARY.finditer(text):
        end_idx = m.end()
        # Look back to a reasonable context slice to test for abbreviations
        lookback_start = max(start, m.start() - 10)
        tail = text[lookback_start:m.start() + 1]  # include the punctuation
        if _is_abbrev(tail.strip()):
            continue  # don't split here

        # Commit a sentence from 'start' to this boundary+closers
        spans.append((start, end_idx))
        start = end_idx

    # Trailing remainder
    if start < n:
        # Skip pure whitespace tails
        tail = text[start:].strip()
        if tail:
            # Trim leading whitespace in the span but keep absolute offsets
            # (UI can further pretty-print)
            while start < n and text[start].isspace():
                start += 1
            spans.append((start, n))
    return spans


def _tokenize_regex(text: str, span: Tuple[int, int]) -> List[Tuple[str, int, int]]:
    """Tokenize a sentence span; return list of (token, start, end)."""
    s, e = span
    sent = text[s:e]
    toks: List[Tuple[str, int, int]] = []
    for m in _TOKEN_RX.finditer(sent):
        tok = m.group(0)
        # Filter out lone whitespace (shouldn't occur) and control chars
        if not tok.strip():
            continue
        # Map to absolute offsets
        a = s + m.start()
        b = s + m.end()
        toks.append((tok, a, b))
    return toks


class Tokenizer:
    """Sentence + word tokenizer with optional spaCy acceleration.

    Returns dict with:
      - sentences: List[str]
      - tokens:    List[str]
      - sentence_spans: List[{"text","start","end"}]
      - token_spans:    List[{"text","start","end"}]
    """

    def __init__(self, use_spacy: bool = True, return_offsets: bool = True) -> None:
        self.use_spacy = bool(use_spacy and _NLP)
        self.return_offsets = bool(return_offsets)

    def run(self, text: str) -> Dict[str, Any]:
        text = text or ""
        sentences: List[str] = []
        tokens: List[str] = []
        sentence_spans: List[Dict[str, int | str]] = []
        token_spans: List[Dict[str, int | str]] = []

        if self.use_spacy and _NLP:
            doc = _NLP(text)  # type: ignore
            # Sentences
            for s in doc.sents:
                s_text = s.text
                sentences.append(s_text)
                if self.return_offsets:
                    sentence_spans.append({"text": s_text, "start": s.start_char, "end": s.end_char})
                # Tokens
                for t in s:
                    if t.is_space:
                        continue
                    tok = t.text
                    tokens.append(tok)
                    if self.return_offsets:
                        token_spans.append({"text": tok, "start": t.idx, "end": t.idx + len(tok)})

        else:
            # Regex fallback path
            spans = _sentence_split_regex(text)
            for s, e in spans:
                s_text = text[s:e]
                sentences.append(s_text)
                if self.return_offsets:
                    sentence_spans.append({"text": s_text, "start": s, "end": e})
                for tok, a, b in _tokenize_regex(text, (s, e)):
                    tokens.append(tok)
                    if self.return_offsets:
                        token_spans.append({"text": tok, "start": a, "end": b})

        out: Dict[str, Any] = {"sentences": sentences, "tokens": tokens}
        if self.return_offsets:
            out["sentence_spans"] = sentence_spans
            out["token_spans"] = token_spans
        return out
