# src/kansas_geo_timeline/ingest/provenance.py
from __future__ import annotations

import hashlib
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, Optional, Tuple


GNU_SHA256_LINE = "{digest}  {name}\n"  # two spaces (GNU coreutils format)


class Provenance:
    """Utilities for hashing, sidecars, timestamps, and basic media typing."""

    # --------------------------- time utilities ---------------------------

    @staticmethod
    def now_iso() -> str:
        """UTC now in RFC3339/ISO-8601 with 'Z'."""
        return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    @staticmethod
    def iso_from_ts(ts: float) -> str:
        """POSIX timestamp → ISO-8601 UTC string."""
        return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat().replace("+00:00", "Z")

    # --------------------------- hashing (files) --------------------------

    @staticmethod
    def sha256_file(path: Path, chunk: int = 1024 * 1024) -> str:
        """Stream SHA256 for a file (chunked, memory-safe)."""
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for b in iter(lambda: f.read(chunk), b""):
                h.update(b)
        return h.hexdigest()

    @staticmethod
    def sha256_bytes(data: bytes) -> str:
        """SHA256 for bytes."""
        return hashlib.sha256(data).hexdigest()

    @staticmethod
    def sha256_text(text: str, encoding: str = "utf-8") -> str:
        """SHA256 for text."""
        return hashlib.sha256(text.encode(encoding)).hexdigest()

    @staticmethod
    def tree_sha256(paths: Iterable[Path]) -> str:
        """Deterministic SHA256 across many files (path+size+hash), order-insensitive.

        Useful for quick content signatures of a collection without producing a tarball.
        """
        digests: list[Tuple[str, int, str]] = []
        for p in paths:
            p = Path(p)
            if not p.is_file():
                continue
            stat = p.stat()
            digests.append((p.as_posix(), stat.st_size, Provenance.sha256_file(p)))

        # Sort to ensure determinism across invocations
        digests.sort(key=lambda t: t[0])
        h = hashlib.sha256()
        for rel, size, d in digests:
            h.update(rel.encode("utf-8"))
            h.update(b"\0")
            h.update(str(size).encode("ascii"))
            h.update(b"\0")
            h.update(d.encode("ascii"))
            h.update(b"\n")
        return h.hexdigest()

    # --------------------------- sidecar I/O ------------------------------

    @staticmethod
    def write_sha256_sidecar(path: Path, digest: str) -> Path:
        """Atomically write a .sha256 sidecar (GNU format)."""
        side = path.with_suffix(path.suffix + ".sha256")
        side.parent.mkdir(parents=True, exist_ok=True)
        content = GNU_SHA256_LINE.format(digest=digest, name=path.name)

        # Atomic write: temp file in same dir then replace
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, dir=side.parent) as tmp:
            tmp.write(content)
            tmp_path = Path(tmp.name)
        os.replace(tmp_path, side)
        return side

    @staticmethod
    def read_sha256_sidecar(sidecar: Path) -> Optional[Tuple[str, str]]:
        """Read a .sha256 sidecar. Returns (digest, filename) or None if not parseable."""
        try:
            line = sidecar.read_text(encoding="utf-8").strip()
        except Exception:
            return None

        # Accept both '  ' (GNU) and ' *' forms defensively
        parts = line.split()
        if len(parts) >= 2:
            digest = parts[0]
            name = parts[-1]
            return digest, name
        return None

    @staticmethod
    def verify_sha256_sidecar(path: Path, sidecar: Optional[Path] = None) -> bool:
        """Verify file content matches sidecar digest."""
        side = sidecar or path.with_suffix(path.suffix + ".sha256")
        meta = Provenance.read_sha256_sidecar(side)
        if not meta:
            return False
        digest_expected, name_in_sidecar = meta
        # Do not enforce name equality strictly; content integrity is the goal.
        digest_actual = Provenance.sha256_file(path)
        return digest_actual == digest_expected

    # --------------------------- file metadata ----------------------------

    @staticmethod
    def file_stats(path: Path) -> Dict:
        """Small, JSON-serializable subset of file stats."""
        st = path.stat()
        return {
            "size": st.st_size,
            "mtime": st.st_mtime,
            "mtime_iso": Provenance.iso_from_ts(st.st_mtime),
            "ctime": st.st_ctime,
            "ctime_iso": Provenance.iso_from_ts(st.st_ctime),
        }

    # --------------------------- STAC helpers -----------------------------

    @staticmethod
    def basic_asset(path: Path, media_type: str) -> Dict:
        """Minimal STAC Asset dict."""
        return {
            "href": path.as_posix(),
            "type": media_type,
            "title": path.name,
        }

    @staticmethod
    def inferred_media_type(path: Path) -> str:
        """Guess a media type from suffix; conservative defaults."""
        suf = path.suffix.lower()
        if suf in {".tif", ".tiff"}:
            return "image/tiff; application=geotiff"
        if suf in {".cog.tif", ".cog.tiff"} or "cog" in path.name.lower():
            return "image/tiff; application=geotiff; profile=cloud-optimized"
        if suf in {".json", ".geojson"}:
            return "application/geo+json"
        if suf in {".gpkg"}:
            return "application/geopackage+sqlite3"
        if suf in {".shp"}:
            return "application/x-esri-shapefile"
        if suf in {".png"}:
            return "image/png"
        if suf in {".jpg", ".jpeg"}:
            return "image/jpeg"
        return "application/octet-stream"

    # --------------------------- convenience ------------------------------

    @staticmethod
    def digest_and_sidecar(path: Path) -> str:
        """Compute SHA256 and write sidecar; returns digest."""
        digest = Provenance.sha256_file(path)
        Provenance.write_sha256_sidecar(path, digest)
        return digest
