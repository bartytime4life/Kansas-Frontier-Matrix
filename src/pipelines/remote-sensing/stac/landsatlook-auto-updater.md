Here’s a GitHub‑ready, single‑box Markdown you can drop into your repo: a standards‑compliant guide + runnable Python template for a STAC → Validate → Neo4j auto‑updater that uses HTTP ETags to poll USGS LandsatLook efficiently and write idempotent scene nodes with POINT geometry.

---
title: "🛰️ Kansas Frontier Matrix — STAC→Validation→Neo4j Auto‑Updater (ETag‑Aware) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/remote-sensing/stac/landsatlook-auto-updater.md"
version: "v10.3.0"
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

# 🛰️ **Kansas Frontier Matrix — STAC→Validation→Neo4j Auto‑Updater (ETag‑Aware)**
`src/pipelines/remote-sensing/stac/landsatlook-auto-updater.md`

**Purpose:** Efficiently ingest Landsat STAC items over Kansas using HTTP conditional requests (ETag / `If-None-Match`), validate with Great Expectations, and upsert idempotent nodes with Neo4j `POINT` geometry for Focus Mode timelines.

</div>

---

## ✅ Why this matters
- **Low‑cost polling:** Avoids re-downloading unchanged search results via `304 Not Modified`.
- **Trustable data:** Each batch can run through **Great Expectations** checkpoints before graph writes.
- **Graph‑ready:** Stores spatial attributes as WGS84 `POINT` for fast bounding and time‑slider queries.

---

## 🧭 Scope & Region
- **AOI:** Kansas bounding box (modifiable).  
- **Source:** USGS LandsatLook STAC Search endpoint.  
- **Cadence:** Every 5 minutes (tunable) with ETag cache.

---

## 🧪 Data Quality & Validation (Great Expectations)
- Schema expectations for `id`, `properties.datetime`, geometry type, CRS = 4326.  
- Row‑level checks: timestamps parseable; coordinates within Kansas AOI; cloud cover within [0,100].  
- Checkpoint must **pass** before any Neo4j write occurs.

---

## 🗺️ Graph Model (Neo4j)
- **Label:** `Scene`  
- **Identity:** `Scene.id` (STAC `id`)  
- **Props:** `acq` (ISO datetime), `collection`, `cloud_cover`  
- **Geom:** `geom = point({longitude: lon, latitude: lat, srid:4326})` (representative footprint vertex or centroid)  
- **MERGE pattern:** `MERGE (s:Scene {id:$id}) SET s += {...}` to ensure idempotency.

---

## ⚙️ Minimal Runnable Template (Python 3.10+)

> Place under `src/pipelines/remote-sensing/stac/landsatlook_auto_updater.py`.  
> Configure environment vars: `NEO4J_URI`, `NEO4J_USER`, `NEO4J_PASS`.  
> Install: `pip install requests great-expectations neo4j`

```python
import json, os, time, requests
from pathlib import Path
from typing import Any, Dict, List, Tuple

# --- Config ---
KS_BBOX = (-102.1, 36.9, -94.6, 40.1)  # Kansas bbox
STAC_SEARCH = f"https://landsatlook.usgs.gov/stac-server/search?bbox={','.join(map(str, KS_BBOX))}"
ETAG_FILE = Path(".cache/etag.json"); ETAG_FILE.parent.mkdir(parents=True, exist_ok=True)
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
    r = requests.get(STAC_SEARCH, headers=headers, timeout=30)
    if r.status_code == 304:
        return [], etag, False
    r.raise_for_status()
    new_etag = r.headers.get("ETag", etag)
    payload = r.json()
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
    q = """
    MERGE (s:Scene {id:$id})
    SET s.acq = $acq,
        s.collection = $collection,
        s.cloud_cover = $cloud_cover,
        s.geom = point({longitude:$lon, latitude:$lat, srid:4326})
    """
    with drv.session() as s:
        for it in items:
            lon, lat = representative_lonlat(it)
            p = it.get("properties", {})
            s.run(q, id=it["id"],
                     acq=p.get("datetime"),
                     collection=p.get("collection"),
                     cloud_cover=p.get("eo:cloud_cover"),
                     lon=lon, lat=lat)
    drv.close()

def main() -> None:
    while True:
        etag = load_etag()
        items, new_etag, changed = fetch_stac(etag)
        if not changed:
            time.sleep(SLEEP_SECONDS); continue
        if items:
            validate_items(items)
            upsert_neo4j(items)
        save_etag(new_etag)
        time.sleep(SLEEP_SECONDS)

if __name__ == "__main__":
    main()


⸻

🧵 CI Integration (excerpt)
	•	Workflow: .github/workflows/stac-validate.yml
	•	Step 1: Run Python validator (fast).
	•	Step 2: Run GE checkpoint (strict).
	•	Step 3: On success, run Neo4j upserts against staging.
	•	Step 4: Promote to prod graph via approval.

⸻

📦 Directory Layout (excerpt)

src/
  pipelines/
    remote-sensing/
      stac/
        landsatlook_auto_updater.py
        landsatlook-auto-updater.md
.cache/
  etag.json


⸻

🧩 Focus Mode Hooks
	•	Scene cards show acq, collection, cloud_cover, and a zoom‑to geometry button.
	•	Time slider queries MATCH (s:Scene) WHERE s.acq >= $t0 AND s.acq < $t1 RETURN s ORDER BY s.acq.

⸻

🔒 Governance & Ethics
	•	FAIR+CARE tags preserved; provenance recorded in the Governance Ledger.
	•	Telemetry logs energy & carbon for polling + validation.
	•	Incident path: if validator fails, halt writes, open auto‑issue, attach artifacts.

⸻

🧰 Local Testing Snippets

python -m venv .venv && source .venv/bin/activate
pip install requests great-expectations neo4j
export NEO4J_URI="bolt://localhost:7687" NEO4J_USER="neo4j" NEO4J_PASS="test"
python src/pipelines/remote-sensing/stac/landsatlook_auto_updater.py


⸻

🧭 Version History
	•	v10.3.0 (2025‑11‑14): Initial ETag‑aware STAC poller with GE hook + Neo4j POINT upserts; KFM‑protocol compliant doc.

⸻


