from __future__ import annotations
from typing import Dict, Any, List, Optional


class Linker:
    """Map extracted entities to KFM IDs (stub with simple rule-based mapping).

    In practice this can call a local registry or a lightweight embedding index.
    """

    def __init__(self, registry: Optional[Dict[str, str]] = None) -> None:
        # simple text→id map; replace with real registry later
        self.registry = registry or {
            "Santa Fe Trail": "kfm:trail:santafe",
            "Fort Larned": "kfm:fort:larned",
            "Kaw": "kfm:nation:kaw",
            "Kansas River": "kfm:river:kansas",
        }

    def run(self, entities: List[Dict[str, Any]]) -> Dict[str, Any]:
        links: List[Dict[str, Any]] = []
        for e in entities:
            key = e["text"]
            if key in self.registry:
                links.append({"text": key, "id": self.registry[key], "label": e.get("label")})
        return {"links": links}
