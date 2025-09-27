# src/kansas_geo_timeline/ingest/base.py
from __future__ import annotations

import abc
import logging
import os
from pathlib import Path
from typing import Dict, Tuple, Optional


class IngestError(RuntimeError):
    """Raised for ingest failures."""


class BaseIngestor(abc.ABC):
    """Abstract base for all ingestors.

    Contract:
      - `run()` returns (output_path, stac_item_dict)
      - Implementations should be idempotent and write a .sha256 sidecar.
    """

    #: Default CRS used across the project unless overridden.
    DEFAULT_CRS = "EPSG:4326"

    def __init__(
        self,
        src_path: str | Path,
        out_dir: str | Path | None = None,
        dst_crs: str = DEFAULT_CRS,
    ) -> None:
        self.logger = logging.getLogger("kfm.ingest")
        if not self.logger.handlers:
            # Quiet, sensible default logger; projects can reconfigure globally.
            handler = logging.StreamHandler()
            fmt = logging.Formatter("[%(levelname)s] %(name)s: %(message)s")
            handler.setFormatter(fmt)
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.INFO)

        self.src_path = Path(src_path).expanduser().resolve()
        if not self.src_path.exists():
            raise IngestError(f"Source not found: {self.src_path}")

        self.out_dir = Path(out_dir).expanduser().resolve() if out_dir else self._default_out_dir()
        self._ensure_out_dir(self.out_dir)

        self.dst_crs = self._norm_dst_crs(dst_crs)

        self.logger.debug(
            "Initialized %s with src=%s, out_dir=%s, dst_crs=%s",
            self.__class__.__name__, self.src_path, self.out_dir, self.dst_crs
        )

    # --- abstract API -----------------------------------------------------

    @abc.abstractmethod
    def _default_out_dir(self) -> Path:
        """Return the default output directory for this ingestor."""
        ...

    @abc.abstractmethod
    def run(self) -> Tuple[Path, Dict]:
        """Execute the ingest step and return (output_path, stac_item_dict)."""
        ...

    # --- optional hooks / helpers ----------------------------------------

    def extra_properties(self) -> Optional[Dict]:
        """Hook for subclasses to add extra STAC properties."""
        return None

    # --- utilities (kept dependency-light) --------------------------------

    def _ensure_out_dir(self, path: Path) -> None:
        """Create output directory and sanity-check writability."""
        try:
            path.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            raise IngestError(f"Unable to create output directory: {path}") from e

        # Best-effort write check (no file created).
        if not os.access(path, os.W_OK):
            raise IngestError(f"Output directory not writable: {path}")

    def _norm_dst_crs(self, crs: str) -> str:
        """Normalize CRS string (e.g., 'epsg:4326' -> 'EPSG:4326')."""
        if not isinstance(crs, str) or ":" not in crs:
            # Keep lenient to allow subclasses to handle non-OGC strings if needed.
            self.logger.warning("Non-standard CRS string '%s' passed; leaving as-is.", crs)
            return crs
        auth, code = crs.split(":", 1)
        return f"{auth.upper()}:{code}"

    def relpath(self, path: Path, start: Optional[Path] = None) -> str:
        """Project-friendly relative path helper (POSIX style)."""
        base = Path.cwd() if start is None else Path(start)
        try:
            rel = Path(path).resolve().relative_to(base.resolve())
        except Exception:
            rel = Path(path).resolve()
        return rel.as_posix()
