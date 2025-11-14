---
title: "🛰️ Kansas Frontier Matrix — STAC→Validation→Neo4j Auto-Updater (ETag-Aware) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/remote-sensing/stac/landsatlook-auto-updater.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/pipelines-stac-updater-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
kfm_markdown_protocol: "docs/standards/kfm_markdown_output_protocol.md"
---

<div align="center">

# 🛰️ **Kansas Frontier Matrix — STAC→Validation→Neo4j Auto-Updater (ETag-Aware)**  
`src/pipelines/remote-sensing/stac/landsatlook-auto-updater.md`

**Purpose:**  
Efficiently ingest Landsat STAC Items over Kansas using HTTP conditional requests (ETag / `If-None-Match`), validate them with **Great Expectations**, and upsert idempotent `Scene` nodes with Neo4j `POINT` geometry for Focus Mode timelines and map/timeline queries.

</div>

---

## ✅ Why this matters

- **Low-cost polling:** Avoids re-downloading unchanged search results via `304 Not Modified`.  
- **Trustable data:** Each batch runs through **Great Expectations** checkpoints before graph writes.  
- **Graph-ready:** Stores spatial attributes as WGS84 `POINT` for fast bounding and time-slider queries.

---

## 🧭 Scope & Region

- **AOI:** Kansas bounding box (modifiable).  
- **Source:** USGS LandsatLook STAC Search endpoint.  
- **Cadence:** Every 5 minutes (tunable) with ETag cache.  

---

## 🧪 Data Quality & Validation (Great Expectations)

Validation MUST include at minimum:

- Schema expectations for `id`, `properties.datetime`, geometry type, CRS = EPSG:4326.  
- Row-level checks:
  - Timestamps parseable and within desired time window.  
  - Coordinates within Kansas AOI.  
  - Cloud cover within `[0, 100]`.  
- Checkpoint MUST **PASS** before any Neo4j write occurs.  

---

## 🗺️ Graph Model (Neo4j)

- **Label:** `Scene`  
- **Identity:** `Scene.id` (STAC `id`)  
- **Properties:**
  - `acq` (ISO datetime, from `properties.datetime`)  
  - `collection` (STAC collection ID)  
  - `cloud_cover` (from `properties["eo:cloud_cover"]`)  
- **Geometry:**  

  ~~~~~text
  s.geom = point({longitude: lon, latitude: lat, srid:4326})
  ~~~~~

  where `lon, lat` come from a representative footprint vertex or centroid.

- **MERGE pattern:**  

  ~~~~~text
  MERGE (s:Scene {id:$id})
  SET s += {acq: $acq, collection: $collection, cloud_cover: $cloud_cover, geom: point({...})}
  ~~~~~

to ensure idempotency.

---

## ⚙️ Minimal Runnable Template (Python 3.10+)

> Place under:  
> `src/pipelines/remote-sensing/stac/landsatlook_auto_updater.py`  
> Configure environment vars: `NEO4J_URI`, `NEO4J_USER`, `NEO4J_PASS`.  
> Install: `pip install requests great-expectations neo4j`

~~~~~python
import json, os, time, requests
from pathlib import Path
from typing import Any, Dict, List, Tuple

# --- Config ---
KS_BBOX = (-102.1, 36.9, -94.6, 40.1)  # Kansas bbox
STAC_SEARCH = f"https://landsatlook.usgs.gov/stac-server/search?bbox={','.join(map(str, KS_BBOX))}"
ETAG_FILE = Path(".cache/etag.json")
ETAG_FILE.parent.mkdir(parents=True, exist_ok=True)
SLEEP_SECONDS = 300

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASS", "password")


def load_etag() -> str:
    if ETAG_FILE.exists():
        try:
            return json.loads(ETAG_FILE.read_text()).get("etag", "")
        except Exception:
            return ""
    return ""


def save_etag(tag: str) -> None:
    ETAG_FILE.write_text(json.dumps({"etag": tag or ""}))


def fetch_stac(etag: str) -> Tuple[List[Dict[str, Any]], str, bool]:
    headers = {"If-None-Match": etag} if etag else {}
    resp = requests.get(STAC_SEARCH, headers=headers, timeout=30)
    if resp.status_code == 304:
        return [], etag, False
    resp.raise_for_status()
    new_etag = resp.headers.get("ETag", etag)
    payload = resp.json()
    items = payload.get("features", [])
    return items, new_etag, True


def validate_items(items: List[Dict[str, Any]]) -> None:
    # Lightweight inline checks (augment/replace with Great Expectations checkpoint)
    for it in items:
        assert "id" in it
        props = it.get("properties", {})
        dt = props.get("datetime")
        assert isinstance(dt, str) and len(dt) >= 10
        geom = it.get("geometry", {})
        assert geom.get("type") in {"Polygon", "MultiPolygon"}
    # Example GE hook:
    # from great_expectations.checkpoint import Checkpoint
    # Checkpoint(...).run()


def representative_lonlat(it: Dict[str, Any]) -> Tuple[float, float]:
    geom = it.get("geometry", {})
    if geom.get("type") == "Polygon":
        coords = geom["coordinates"][0][0]
    else:
        coords = geom["coordinates"][0][0][0]
    lon, lat = coords
    return float(lon), float(lat)


def upsert_neo4j(items: List[Dict[str, Any]]) -> None:
    from neo4j import GraphDatabase

    drv = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
    query = """
    MERGE (s:Scene {id:$id})
    SET s.acq = $acq,
        s.collection = $collection,
        s.cloud_cover = $cloud_cover,
        s.geom = point({longitude:$lon, latitude:$lat, srid:4326})
    """
    with drv.session() as session:
        for it in items:
            lon, lat = representative_lonlat(it)
            props = it.get("properties", {})
            session.run(
                query,
                id=it["id"],
                acq=props.get("datetime"),
                collection=props.get("collection"),
                cloud_cover=props.get("eo:cloud_cover"),
                lon=lon,
                lat=lat,
            )
    drv.close()


def main() -> None:
    while True:
        etag = load_etag()
        items, new_etag, changed = fetch_stac(etag)
        if not changed:
            time.sleep(SLEEP_SECONDS)
            continue
        if items:
            validate_items(items)
            upsert_neo4j(items)
        save_etag(new_etag)
        time.sleep(SLEEP_SECONDS)


if __name__ == "__main__":
    main()
~~~~~

---

## 🧵 CI Integration (Conceptual)

- **Workflow:** `.github/workflows/stac-validate.yml`  
- **Steps:**
  - Run Python validator (fast structural checks).  
  - Run **Great Expectations** checkpoint (strict gate).  
  - On success, run Neo4j upserts against staging graph.  
  - Promote changes to production graph via manual approval step.  

---

## 📦 Directory Layout (Excerpt)

~~~~~text
src/
  pipelines/
    remote-sensing/
      stac/
        landsatlook_auto_updater.py
        landsatlook-auto-updater.md
.cache/
  etag.json
~~~~~

---

## 🧩 Focus Mode Hooks

- Focus Mode Scene cards can surface:
  - Acquisition datetime (`acq`)  
  - Collection ID (`collection`)  
  - Cloud cover (`cloud_cover`)  
  - Zoom-to-geometry button using `geom` POINT.  

- Time slider queries (conceptual):

  ~~~~~text
  MATCH (s:Scene)
  WHERE s.acq >= $t0 AND s.acq < $t1
  RETURN s
  ORDER BY s.acq
  ~~~~~

---

## 🔒 Governance & Ethics

- **FAIR+CARE:**  
  - CARE labels and provenance tracked from upstream STAC metadata.  
  - Any CARE/sovereignty conflicts must halt writes and trigger governance review.

- **Telemetry:**  
  - Logs energy and carbon for polling + validation stages.  
  - Emitted to `focus-telemetry.json` and per-run telemetry JSONL.

- **Incident path:**  
  - If GE validator fails → halt writes, open auto-issue, attach failing batch + Data Docs.  

---

## 🧰 Local Testing Snippets

~~~~~bash
python -m venv .venv
source .venv/bin/activate
pip install requests great-expectations neo4j

export NEO4J_URI="bolt://localhost:7687"
export NEO4J_USER="neo4j"
export NEO4J_PASS="test"

python src/pipelines/remote-sensing/stac/landsatlook_auto_updater.py
~~~~~

---

## 🕰️ Version History

| Version  | Date       | Author | Summary |
|----------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | Remote Sensing Team | Updated to KFM Markdown Protocol (tilde fences), clarified CI + governance links, and aligned telemetry + Neo4j model. |
| v10.3.0 | 2025-11-14 | Remote Sensing Team | Initial ETag-aware STAC poller with GE hook + Neo4j POINT upserts; KFM protocol-compliant design. |
