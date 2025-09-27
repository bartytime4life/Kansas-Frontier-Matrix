from __future__ import annotations
import re
from typing import Any, Dict, List, Optional

try:
    import spacy
    _NLP: Optional["spacy.language.Language"] = spacy.load("en_core_web_sm")  # optional
except Exception:
    _NLP = None

# Lightweight rule-based backup (proper nouns / capitalized multi-words)
_CAP_SEQ = re.compile(r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,3})\b")


class EntityExtractor:
    """Named entities with optional spaCy; fallback picks up capitalized spans."""

    def __init__(self, use_spacy: bool = True) -> None:
        self.use_spacy = bool(use_spacy and _NLP)

    def run(self, text: str) -> Dict[str, Any]:
        ents: List[Dict[str, Any]] = []
        if self.use_spacy and _NLP:
            doc = _NLP(text)
            for e in doc.ents:
                ents.append({"text": e.text, "label": e.label_})
        else:
            for m in _CAP_SEQ.finditer(text):
                ents.append({"text": m.group(1), "label": "PROPN"})
        # de-dupe
        seen = set()
        uniq = []
        for e in ents:
            key = (e["text"], e.get("label"))
            if key in seen:
                continue
            seen.add(key)
            uniq.append(e)
        return {"entities": uniq}
