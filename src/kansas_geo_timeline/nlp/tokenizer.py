from __future__ import annotations
import re
from typing import List, Dict, Any, Optional

try:
    import spacy
    _NLP: Optional["spacy.language.Language"] = spacy.load("en_core_web_sm")  # optional
except Exception:  # spaCy may be missing
    _NLP = None

_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")
_WORD_SPLIT = re.compile(r"\w+([-']\w+)?", re.UNICODE)


class Tokenizer:
    """Sentence + word tokenizer with optional spaCy acceleration."""

    def __init__(self, use_spacy: bool = True) -> None:
        self.use_spacy = bool(use_spacy and _NLP)

    def run(self, text: str) -> Dict[str, Any]:
        if self.use_spacy and _NLP:
            doc = _NLP(text)
            sents = [s.text for s in doc.sents]
            tokens = [t.text for t in doc if not t.is_space]
        else:
            sents = _SENT_SPLIT.split(text.strip()) if text.strip() else []
            tokens = _WORD_SPLIT.findall(text)
            # regex .findall with group returns tuples; flatten
            tokens = [t[0] if isinstance(t, tuple) else t for t in tokens]
        return {"sentences": sents, "tokens": tokens}
