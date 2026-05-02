from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

MAGIC = "PMTILESv1"


@dataclass(frozen=True)
class PMTilesArchive:
    header_valid: bool
    directory_valid: bool
    tiles: dict[str, str]


def read_pmtiles_archive(path: str | Path) -> PMTilesArchive:
    payload = Path(path).read_text(encoding="utf-8")
    parts = payload.splitlines()
    if len(parts) < 3 or parts[0].strip() != MAGIC:
        return PMTilesArchive(False, False, {})

    try:
        header = json.loads(parts[1])
        directory = json.loads(parts[2])
    except json.JSONDecodeError:
        return PMTilesArchive(False, False, {})

    if not isinstance(header.get("directory_offset"), int) or not isinstance(header.get("directory_length"), int):
        return PMTilesArchive(True, False, {})

    tiles = directory.get("tiles", {}) if isinstance(directory, dict) else {}
    if not isinstance(tiles, dict):
        return PMTilesArchive(True, False, {})

    return PMTilesArchive(True, True, {str(k): str(v) for k, v in tiles.items()})


def tile_exists(archive: PMTilesArchive, z: int, x: int, y: int) -> bool:
    return f"{z}/{x}/{y}" in archive.tiles


def read_tile_bytes(archive: PMTilesArchive, z: int, x: int, y: int) -> bytes:
    return archive.tiles[f"{z}/{x}/{y}"].encode("utf-8")
