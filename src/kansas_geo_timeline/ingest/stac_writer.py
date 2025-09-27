from __future__ import annotations
from pathlib import Path
from typing import Dict, Optional
from .provenance import Provenance


class StacWriter:
    """Tiny STAC item emitter (JSON dict). Expand as needed."""

    @staticmethod
    def mk_item(
        id_: str,
        source_path: Path,
        out_path: Path,
        bbox: Optional[list[float]],
        geometry: Optional[dict],
        properties: dict,
        asset_media_type: str,
        collection: Optional[str] = None,
    ) -> Dict:
        props = {
            "datetime": properties.get("datetime") or Provenance.now_iso(),
            **{k: v for k, v in properties.items() if k != "datetime"},
        }
        item = {
            "type": "Feature",
            "stac_version": "1.0.0",
            "id": id_,
            "bbox": bbox,
            "geometry": geometry,
            "properties": props,
            "assets": {
                "data": Provenance.basic_asset(out_path, asset_media_type),
                "source": Provenance.basic_asset(source_path, "application/octet-stream"),
            },
        }
        if collection:
            item["collection"] = collection
        return item

    @staticmethod
    def write_item(item: Dict, out_dir: Path, filename: Optional[str] = None) -> Path:
        out_dir.mkdir(parents=True, exist_ok=True)
        name = filename or f"{item['id']}.json"
        path = out_dir / name
        import json
        path.write_text(json.dumps(item, ensure_ascii=False, indent=2), encoding="utf-8")
        return path
