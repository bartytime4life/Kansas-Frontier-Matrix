from __future__ import annotations
import abc
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional


class NLPError(RuntimeError):
    """Raised for NLP failures."""


@dataclass
class TextRecord:
    """Minimal input/output record."""
    id: str
    text: str
    meta: Dict[str, Any]


class PipelineStage(abc.ABC):
    """Abstract stage in the NLP pipeline."""

    @abc.abstractmethod
    def run(self, rec: TextRecord) -> TextRecord:
        """Transform the record in-place or return a new one."""
        raise NotImplementedError
