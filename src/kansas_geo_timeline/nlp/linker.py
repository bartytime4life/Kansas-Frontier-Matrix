# src/kansas_geo_timeline/nlp/linker.py
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from typing import Dict, Any, List, Optional, Iterable, Tuple


def _strip_accents(s: str) -> str:
    nfkd = unicodedata.normalize("NFKD", s)
    return "".join(ch for ch in nfkd if not unicodedata.combining(ch))


def _norm(s: str) -> str:
    """Lowercase, strip accents, collapse whitespace."""
    s = _strip_accents(s).lower().strip()
    s = re.sub(r"\s+", " ", s)
    return s


def _tokset(s: str) -> set[str]:
    return set(t for t in re.findall(r"[a-z0-9]+", _norm(s)) if t)


def _jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    inter = len(a & b)
    if inter == 0:
        return 0.0
    return inter / float(len(a | b))


@dataclass(frozen=True)
class _Entry:
    canonical: str
    id: str
    aliases: Tuple[str, ...]
    norm_aliases: Tuple[str, ...]
    token_sets: Tuple[set, ...]


def _coerce_registry(registry: Dict[str, Any] | None) -> Dict[str, _Entry]:
    """Normalize various registry shapes into canonical → _Entry."""
    if not registry:
        registry = {
            "Santa Fe Trail": "kfm:trail:santafe",
            "Fort Larned": "kfm:fort:larned",
            "Kaw": "kfm:nation:kaw",
            "Kansas River": "kfm:river:kansas",
        }
    out: Dict[str, _Entry] = {}
    for canon, v in registry.items():
        if isinstance(v, str):
            rid = v
            aliases: List[str] = []
        elif isinstance(v, dict):
            rid = str(v.get("id") or v.get("ID") or v.get("Id") or "")
            if not rid:
                # tolerate dicts that are just {"aliases":[...]} with missing id
                rid = f"kfm:unknown:{_norm(canon).replace(' ', '_')}"
            aliases = list(v.get("aliases") or v.get("alias") or [])
        else:
            continue
        all_aliases = [canon] + aliases
        norm_aliases = tuple(_norm(a) for a in all_aliases)
        token_sets = tuple(_tokset(a) for a in all_aliases)
        out[canon] = _Entry(
            canonical=canon,
            id=rid,
            aliases=tuple(all_aliases),
            norm_aliases=norm_aliases,
            token_sets=token_sets,
        )
    return out


class Linker:
    """Map extracted entities (and optional glossary hits) to stable KFM IDs.

    Registry formats accepted:
      {
        "Canonical Name": "kfm:id",
        "Another Canonical": {"id": "kfm:other", "aliases": ["Alias A", "Alias B"]}
      }

    run(entities, glossary=None)  # glossary is optional list of hits like {"canonical","matched",...}
    """

    def __init__(self, registry: Optional[Dict[str, Any]] = None) -> None:
        self.entries = _coerce_registry(registry)
        # Inverted index: normalized token -> set of canonical names
        self.token_index: Dict[str, set[str]] = {}
        for canon, ent in self.entries.items():
            for ts in ent.token_sets:
                for tok in ts:
                    self.token_index.setdefault(tok, set()).add(canon)

    # ----------------------- public API -----------------------

    def run(self, entities: List[Dict[str, Any]], glossary: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
        links: List[Dict[str, Any]] = []

        # 1) Prime matches from glossary (canonical is explicit)
        if glossary:
            for g in glossary:
                canon = g.get("canonical")
                if canon in self.entries:
                    ent = self.entries[canon]
                    links.append(self._mk_link(
                        text=g.get("matched", canon),
                        canonical=ent.canonical,
                        rid=ent.id,
                        label="GAZ",
                        confidence=min(0.98, float(g.get("confidence", 0.9)) + 0.04),
                        match_type="glossary",
                        start=g.get("start"),
                        end=g.get("end"),
                    ))

        # 2) Entity list (spaCy/regex) → resolve via exact, normalized, and token-Jaccard
        for e in entities:
            surface = str(e.get("text", "")).strip()
            if not surface:
                continue
            label = e.get("label")
            start = e.get("start")
            end = e.get("end")

            cand = self._best_candidate(surface)
            if not cand:
                continue

            canon, rid, conf, mtype = cand
            # small bonus if labels hint at a place/facility matching known suffixes
            if label in {"GPE", "LOC", "FAC"} and mtype != "exact":
                conf = min(0.99, conf + 0.02)

            links.append(self._mk_link(
                text=surface,
                canonical=canon,
                rid=rid,
                label=label,
                confidence=conf,
                match_type=mtype,
                start=start,
                end=end,
            ))

        # De-duplicate: keep highest confidence per (text, id)
        best: Dict[Tuple[str, str], Dict[str, Any]] = {}
        for L in links:
            key = (L["text"].lower(), L["id"])
            if key not in best or L["confidence"] > best[key]["confidence"]:
                best[key] = L

        # Stable order: confidence desc, then text asc
        final = sorted(best.values(), key=lambda x: (-x["confidence"], x["text"].lower()))
        return {"links": final}

    # ----------------------- internals -----------------------

    def _mk_link(
        self,
        *,
        text: str,
        canonical: str,
        rid: str,
        label: Optional[str],
        confidence: float,
        match_type: str,
        start: Optional[int] = None,
        end: Optional[int] = None,
    ) -> Dict[str, Any]:
        out = {
            "text": text,
            "canonical": canonical,
            "id": rid,
            "confidence": round(float(confidence), 3),
            "match_type": match_type,
        }
        if label is not None:
            out["label"] = label
        if start is not None:
            out["start"] = int(start)
        if end is not None:
            out["end"] = int(end)
        return out

    def _best_candidate(self, surface: str) -> Optional[Tuple[str, str, float, str]]:
        """Return (canonical, id, confidence, match_type) or None."""
        n = _norm(surface)
        toks = _tokset(surface)

        # Exact (case-sensitive) across aliases
        for canon, ent in self.entries.items():
            if surface in ent.aliases:
                return (canon, ent.id, 0.99, "exact")

        # Normalized exact (case/diacritic insensitive)
        for canon, ent in self.entries.items():
            if n in ent.norm_aliases:
                return (canon, ent.id, 0.97, "norm-exact")

        # Token-index shortlist (fast)
        shortlist: set[str] = set()
        for t in toks:
            shortlist |= self.token_index.get(t, set())

        best: Optional[Tuple[str, str, float, str]] = None
        for canon in shortlist or self.entries.keys():
            ent = self.entries[canon]
            # Compare against all alias token sets and pick the best score
            scores = [_jaccard(toks, ts) for ts in ent.token_sets]
            score = max(scores) if scores else 0.0
            if score >= 0.5:  # reasonable threshold to prevent noise
                conf = 0.88 + 0.08 * (score - 0.5) / 0.5  # map [0.5..1.0] → [0.88..0.96]
                cand = (canon, ent.id, conf, "token-jaccard")
                if (best is None) or cand[2] > best[2]:
                    best = cand

        return best
