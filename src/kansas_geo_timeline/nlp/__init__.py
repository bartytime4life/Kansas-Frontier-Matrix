# src/kansas_geo_timeline/nlp/__init__.py
"""Kansas Geo Timeline — NLP package.

Public API
----------
- NLPPipeline (end-to-end orchestrator)
- Tokenizer, DateExtractor, EntityExtractor, Glossary, Linker (building blocks)

Convenience
-----------
- analyze_text(text, *, rec_id="doc-1", meta=None) -> dict
- nlp_process_file(input_jsonl, output_jsonl, *, stac_dir="stac/items/text", collection=None) -> (count, [stac_paths])
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# --- version (robust) -----------------------------------------------------
try:
    try:
        from importlib.metadata import version, PackageNotFoundError  # py>=3.8
    except Exception:  # pragma: no cover
        from importlib_metadata import version, PackageNotFoundError  # type: ignore
    try:
        __version__ = version("kansas-geo-timeline")
    except PackageNotFoundError:
        try:
            __version__ = version("kansas_geo_timeline")
        except PackageNotFoundError:
            __version__ = "0.0.0"
except Exception:  # pragma: no cover
    __version__ = "0.0.0"

# --- primary classes (light modules; heavy deps are optional inside) ------
from .pipeline import NLPPipeline
from .tokenizer import Tokenizer
from .date_extractor import DateExtractor
from .entity_extractor import EntityExtractor
from .glossary import Glossary
from .linker import Linker

# --- defaults (single source of truth for callers) ------------------------
DEFAULT_STAC_TEXT_DIR: Path = Path("stac/items/text")

# --- convenience helpers --------------------------------------------------
def analyze_text(text: str, *, rec_id: str = "doc-1", meta: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Run the default NLP pipeline on a single text snippet and return the enriched record (dict)."""
    # Lazy import to avoid import-time cost if only metadata is read
    from .pipeline import NLPPipeline
    from .base import TextRecord

    pipe = NLPPipeline()
    rec = TextRecord(id=rec_id, text=text, meta=meta or {"id": rec_id, "text": text})
    return pipe.process_record(rec)

def nlp_process_file(
    input_jsonl: str | Path,
    output_jsonl: str | Path,
    *,
    stac_dir: str | Path = DEFAULT_STAC_TEXT_DIR,
    collection: Optional[str] = None,
) -> Tuple[int, List[Path]]:
    """Process a JSONL file through the NLP pipeline and write STAC items.

    Returns:
        (count, stac_paths)
    """
    from .pipeline import NLPPipeline

    pipe = NLPPipeline(stac_items_dir=stac_dir)
    return pipe.run_file(Path(input_jsonl), Path(output_jsonl), collection=collection)

__all__ = (
    "NLPPipeline",
    "Tokenizer",
    "DateExtractor",
    "EntityExtractor",
    "Glossary",
    "Linker",
    "DEFAULT_STAC_TEXT_DIR",
    "analyze_text",
    "nlp_process_file",
    "__version__",
)
