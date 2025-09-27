# src/kansas_geo_timeline/nlp/base.py
from __future__ import annotations

import abc
import logging
from dataclasses import dataclass, field, asdict
from typing import Any, Dict, Optional, Tuple


class NLPError(RuntimeError):
    """Raised for NLP failures."""


# ---------- Logging (lightweight, project-friendly) ----------
_logger = logging.getLogger("kfm.nlp")
if not _logger.handlers:
    _h = logging.StreamHandler()
    _h.setFormatter(logging.Formatter("[%(levelname)s] %(name)s: %(message)s"))
    _logger.addHandler(_h)
    _logger.setLevel(logging.INFO)


# ---------- Core record model ----------
@dataclass
class TextRecord:
    """Minimal input/output record flowing through NLP stages.

    Attributes
    ----------
    id   : stable identifier for the record (e.g., 'doc-1')
    text : raw/plaintext content (UTF-8)
    meta : mutable dict that stages enrich (tokens, dates, entities, links, etc.)
    """
    id: str
    text: str
    meta: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        # Ensure meta always contains core reflections
        self.meta.setdefault("id", self.id)
        self.meta.setdefault("text", self.text)

    @classmethod
    def from_obj(cls, obj: Dict[str, Any]) -> "TextRecord":
        """Construct from a dict with at least {'text', ...}. Falls back to synthetic id."""
        rid = str(obj.get("id") or "rec-1")
        txt = obj.get("text", "")
        meta = dict(obj)
        return cls(id=rid, text=txt, meta=meta)

    def to_jsonable(self) -> Dict[str, Any]:
        """Return a JSON-serializable dict (shallow)."""
        # Prefer meta as the canonical container, but ensure id/text present
        d = dict(self.meta)
        d["id"] = self.id
        d["text"] = self.text
        return d


# ---------- Stage base class ----------
class PipelineStage(abc.ABC):
    """Abstract stage in the NLP pipeline.

    Subclasses implement `run()` to transform/enrich the `TextRecord`.
    Use `safe_run()` in orchestration to convert unexpected errors into NLPError.
    """

    name: str = "stage"

    # Optional lifecycle hooks
    def setup(self) -> None:  # pragma: no cover (usually trivial)
        """Prepare resources (models, indexes). Called once by orchestrator."""
        return None

    def teardown(self) -> None:  # pragma: no cover (usually trivial)
        """Release resources. Called once by orchestrator shutdown."""
        return None

    @abc.abstractmethod
    def run(self, rec: TextRecord) -> TextRecord:
        """Transform the record (in-place or return a new one)."""
        raise NotImplementedError

    # Helper for orchestrators: wraps exceptions with context
    def safe_run(self, rec: TextRecord) -> TextRecord:
        try:
            return self.run(rec)
        except NLPError:
            # Bubble up domain errors as-is
            raise
        except Exception as e:
            _logger.debug("Stage '%s' failed with %r on record id=%s", self.name, e, rec.id)
            raise NLPError(f"NLP stage '{self.name}' failed for record '{rec.id}': {e}") from e
