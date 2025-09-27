from __future__ import annotations
import abc
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

    def __init__(
        self,
        src_path: str | Path,
        out_dir: str | Path | None = None,
        dst_crs: str = "EPSG:4326",
    ) -> None:
        self.src_path = Path(src_path)
        if not self.src_path.exists():
            raise IngestError(f"Source not found: {self.src_path}")
        self.out_dir = Path(out_dir) if out_dir else self._default_out_dir()
        self.out_dir.mkdir(parents=True, exist_ok=True)
        self.dst_crs = dst_crs

    @abc.abstractmethod
    def _default_out_dir(self) -> Path:
        ...

    @abc.abstractmethod
    def run(self) -> Tuple[Path, Dict]:
        ...

    # Optional hook
    def extra_properties(self) -> Optional[Dict]:
        return None
