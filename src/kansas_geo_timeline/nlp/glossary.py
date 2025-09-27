from __future__ import annotations
from typing import Dict, List, Any


_DEFAULT = {
    "Kaw": ["Kanza", "Kansa", "Kaw Nation"],
    "Santa Fe Trail": ["SFT", "Santa Fé Trail"],
    "Fort Larned": ["Camp on Pawnee Fork", "Larned Fort"],
}


class Glossary:
    """Domain term normalization + alias expansion."""

    def __init__(self, terms: Dict[str, List[str]] | None = None) -> None:
        self.terms = terms or _DEFAULT

    def run(self, text: str) -> Dict[str, Any]:
        hits: List[Dict[str, str]] = []
        low = text.lower()
        for canon, aliases in self.terms.items():
            all_terms = [canon] + list(aliases)
            for t in all_terms:
                if t.lower() in low:
                    hits.append({"canonical": canon, "matched": t})
        # de-dupe by canonical
        uniq = {}
        for h in hits:
            uniq[h["canonical"]] = h
        return {"glossary": list(uniq.values())}
