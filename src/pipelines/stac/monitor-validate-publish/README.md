---
title: "🛰️ Kansas Frontier Matrix — STAC Monitor → Validate → Publish Orchestrator (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/stac/monitor-validate-publish/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/pipelines-stac-orchestrator-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🛰️ **Kansas Frontier Matrix — STAC Monitor → Validate → Publish Orchestrator**  
`src/pipelines/stac/monitor-validate-publish/README.md`

**Purpose:**  
Turn **STAC API Item Search** results in the Kansas AOI into reliable, validated Items and Collections, then **upsert** them to KFM storage and graph on a schedule.  
Uses **HTTP conditional requests (ETag / If-None-Match)** for efficient polling, **Great Expectations** for schema/range/uniqueness checks, and **GitHub Actions** for cron orchestration and attestable CI.

**Scope:**  
KFM-wide ingestion of remote sensing & environmental feeds (NOAA/USGS/NASA vendors) within Kansas bounding geometries, producing ready-to-serve STAC assets, provenance, and Neo4j graph links.

</div>

---

## 📘 Overview

The **STAC Monitor → Validate → Publish Orchestrator**:

- Polls remote **STAC APIs** for new/updated Items intersecting the **Kansas AOI**  
- Uses **ETag / If-None-Match** for efficient “no-change” detection  
- Runs **Great Expectations** as a **hard validation gate**  
- Normalizes STAC Items/Collections into **KFM STAC layout**  
- Upserts validated STAC assets into `data/stac/published/`  
- Updates **Neo4j graph** links for Scenes, Datasets, and Themes  
- Is driven by **GitHub Actions** on **cron** and manual dispatch  
- Emits **telemetry** and governance metadata for every run  

---

## 📁 Directory Layout

~~~~~text
src/pipelines/stac/monitor-validate-publish/
├── README.md
├── monitor.py                      # STAC polling + ETag handling
├── publish.py                      # Upsert to data/stac + Neo4j graph
├── transform.py                    # Normalize/augment STAC Items
├── etag_cache.json                 # ETag cache for Item Search polling
├── expectations/                   # Great Expectations config
│   ├── great_expectations.yml
│   ├── checkpoints/
│   │   └── stac_items.yml
│   └── expectations/
│       └── stac_item_schema.json
│
data/stac/
├── incoming/                       # Raw polled JSON/JSONL
├── quarantine/                     # Failed validation batches
└── published/                      # Validated STAC Items/Collections
data/geometry/
└── kansas_aoi.geojson              # Authoritative Kansas AOI (EPSG:4326)
.github/workflows/
└── stac-orchestrator.yml           # GitHub Actions workflow
~~~~~

---

## 🧭 Kansas AOI

- Authoritative AOI lives at:

  ~~~~~text
  data/geometry/kansas_aoi.geojson
  ~~~~~

- CRS: **EPSG:4326**  
- Optional tiling (H3 / quadbin) may be generated to shard polling windows.

---

## 🧩 Flow Overview

### Orchestrator Diagram

~~~~~mermaid
flowchart LR
  A["Schedule GitHub Actions"] --> B["Poll STAC API<br/>If-None-Match (ETag)"]
  B -->|304 Not Modified| Z["No-Op · Emit Telemetry"]
  B -->|200 OK (Items)| C["Stage Raw JSONL<br/>data/stac/incoming"]
  C --> D["Great Expectations Checkpoint<br/>stac_items.yml"]
  D -->|PASS| E["Transform & Normalize STAC"]
  D -->|FAIL| F["Quarantine Batch<br/>+ Open GitHub Issue"]
  E --> G["Upsert Items/Collections<br/>data/stac/published/**"]
  G --> H["Update Neo4j Graph Links<br/>Scenes → Datasets → Themes"]
  H --> I["Emit Telemetry + Artifacts"]
~~~~~

---

## 🌐 Polling STAC API Efficiently (ETag / If-None-Match)

**Goal:** Avoid unnecessary data transfers and quota usage when nothing has changed.

- Item Search endpoint (example):

  ~~~~~text
  POST <PROVIDER_STAC_API>/search
  ~~~~~

- Filters:
  - `intersects` = Kansas AOI  
  - `datetime` = `2020-01-01T00:00:00Z/..` (open-ended)  
  - `collections` = e.g. `["landsat-c2-l2", "sentinel-2-l2a"]`  
  - `limit` = 200 (batch size)

### ETag Cache Location

~~~~~text
src/pipelines/stac/monitor-validate-publish/etag_cache.json
~~~~~

### Python Polling Sketch

~~~~~python
import json
import requests
from pathlib import Path

from typing import Dict, Any

API = "https://example-stac.com"  # STAC_API
cache_path = Path("src/pipelines/stac/monitor-validate-publish/etag_cache.json")
etag_cache: Dict[str, Any] = json.loads(cache_path.read_text()) if cache_path.exists() else {}

headers = {"Content-Type": "application/json"}
if etag_cache.get("search_etag"):
    headers["If-None-Match"] = etag_cache["search_etag"]

aoi = json.loads(Path("data/geometry/kansas_aoi.geojson").read_text())

payload = {
    "collections": ["landsat-c2-l2", "sentinel-2-l2a"],
    "intersects": aoi,
    "datetime": "2020-01-01T00:00:00Z/..",
    "limit": 200
}

resp = requests.post(f"{API}/search", json=payload, headers=headers)

if resp.status_code == 304:
    print("No changes (304).")
else:
    resp.raise_for_status()
    features = resp.json().get("features", [])
    incoming = Path("data/stac/incoming/items.jsonl")
    incoming.parent.mkdir(parents=True, exist_ok=True)
    incoming.write_text("\n".join(json.dumps(f) for f in features))

    if "ETag" in resp.headers:
        etag_cache["search_etag"] = resp.headers["ETag"]
        cache_path.write_text(json.dumps(etag_cache, indent=2))
~~~~~

---

## 🔎 Validation Gate (Great Expectations)

**Checkpoint:**  
- `expectations/checkpoints/stac_items.yml`

Covers, at minimum:

- JSON schema conformity (using `stac_item_schema.json`)  
- Ranges (e.g. `properties["eo:cloud_cover"]` ∈ [0,100])  
- Required field presence (id, geometry, datetime, assets, links)  
- ID uniqueness per collection  
- Link integrity (`rel == "self"`, `"collection"`, `"root"`)

### CLI Pattern

~~~~~bash
cd src/pipelines/stac/monitor-validate-publish/expectations

great_expectations checkpoint run stac_items \
  --config great_expectations.yml \
  --suite stac_item_suite
~~~~~

**Outcome:**

- ✅ PASS → proceed to transform/publish  
- ❌ FAIL → move batch to `data/stac/quarantine/` and open a GitHub Issue

---

## 🧪 Transform & Normalize (transform.py)

Responsibilities:

- Normalize Item `properties` (datetime, gsd, cloud_cover)  
- Ensure **proj:\*** and **eo:\*** fields are present when applicable  
- Fix relative `href`s → absolute or KFM-standard paths  
- Ensure correct `assets[*].type` (MIME) and `roles`  
- Add KFM provenance & ingest metadata, e.g.:

~~~~~python
def normalize_item(item: dict) -> dict:
    props = item.setdefault("properties", {})
    props.setdefault("kfm:ingest_version", "v10.3.1")
    # Normalize datetime, cloud cover, etc.
    # e.g., props["datetime"] = normalize_datetime(props.get("datetime"))
    return item
~~~~~

---

## ⬆️ Publish (Upsert Items & Collections)

**Targets:**

- Filesystem:

  ~~~~~text
  data/stac/published/collections/<collection_id>.json
  data/stac/published/items/<collection_id>/<item_id>.json
  ~~~~~

- Graph (Neo4j):

  - Scenes (`:Scene {stac_id}`)  
  - Datasets (`:Dataset {id}`)  
  - Themes (`:Theme {name}`)

### Neo4j Upsert Sketch (publish.py excerpt)

~~~~~python
from neo4j import GraphDatabase

def upsert_graph(item: dict, driver: GraphDatabase.driver) -> None:
    with driver.session() as session:
        session.run(
            """
            MERGE (s:Scene {stac_id: $id})
            SET s.updated = timestamp(), s.datetime = $dt
            MERGE (dset:Dataset {id: $collection})
            MERGE (s)-[:BELONGS_TO]->(dset)
            """,
            id=item["id"],
            dt=item["properties"]["datetime"],
            collection=item["collection"],
        )
~~~~~

---

## ⏱️ GitHub Actions Orchestration

**Workflow:** `.github/workflows/stac-orchestrator.yml`

~~~~~yaml
name: STAC Orchestrator

on:
  schedule:
    - cron: "5 * * * *"   # every hour at :05
  workflow_dispatch: {}

jobs:
  run:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      issues: write

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install deps
        run: |
          pip install -r requirements.txt
          pip install great_expectations neo4j

      - name: Poll STAC with ETag
        env:
          STAC_API: ${{ secrets.STAC_API }}
        run: |
          python src/pipelines/stac/monitor-validate-publish/monitor.py

      - name: Validate (Great Expectations)
        run: |
          great_expectations checkpoint run stac_items \
            --config src/pipelines/stac/monitor-validate-publish/expectations/great_expectations.yml \
            --suite stac_item_suite

      - name: Publish + Graph
        env:
          NEO4J_URI: ${{ secrets.NEO4J_URI }}
          NEO4J_USER: ${{ secrets.NEO4J_USER }}
          NEO4J_PASS: ${{ secrets.NEO4J_PASS }}
        run: |
          python src/pipelines/stac/monitor-validate-publish/publish.py

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: stac-run-${{ github.run_id }}
          path: |
            data/stac/incoming/**/*.jsonl
            data/stac/published/**/*.json
            src/pipelines/stac/monitor-validate-publish/expectations/uncommitted/data_docs

      - name: Open issue on validation failure
        if: failure()
        uses: peter-evans/create-issue-from-file@v5
        with:
          title: "STAC validation failure in run ${{ github.run_id }}"
          content-file: data/stac/quarantine/last_failure_summary.md
          labels: pipeline, stac, validation
~~~~~

---

## 🔐 Secrets & Configuration

Required secrets:

- `STAC_API` — Base URL of provider STAC API  
- `NEO4J_URI`, `NEO4J_USER`, `NEO4J_PASS` — Graph credentials  

Optional env:

- `HTTP_TIMEOUT`  
- `RETRY_COUNT`  
- `BATCH_LIMIT`

---

## 📈 Telemetry & Provenance

The orchestrator MUST emit telemetry fields such as:

- `polled_count`  
- `new_items`  
- `updated_items`  
- `quarantined_items`  
- `publish_latency_ms`  

Telemetry is linked via:

~~~~~text
../../../releases/v10.3.0/focus-telemetry.json
~~~~~

Additional telemetry JSONL may be written to:

~~~~~text
data/stac/telemetry/*.jsonl
~~~~~

Include an **ingest hash** over normalized Items for immutability audits.

---

## 🧰 Requirements (Python Dependencies)

Add to `requirements.txt`:

~~~~~text
requests>=2.32
great-expectations>=1.0
neo4j>=5.25
jsonschema
shapely
h3
~~~~~

---

## 🧪 Great Expectations — Minimal Check Examples

Validation suite `stac_item_suite` SHOULD include checks for:

- **Schema presence**: `id`, `geometry`, `properties.datetime`, `assets`  
- **Ranges**: `properties["eo:cloud_cover"]` in `[0, 100]`  
- **Uniqueness**: `id` unique per collection  
- **Links**: `links[?rel == "self"]`, `links[?rel == "collection"]` present  

---

## 🧯 Failure Handling

- On **GE failure**:
  - Move batch to `data/stac/quarantine/<timestamp>/`  
  - Write `last_failure_summary.md` with validation findings  
  - Auto-open GitHub Issue linking to quarantined batch  

- On **publish failure**:
  - Retry with backoff (pipeline retry rules)  
  - On repeated failure → open GitHub Issue and mark dataset as blocked  

---

## 🧪 Local Dry-Run

~~~~~bash
export STAC_API="https://example-stac.com"

python src/pipelines/stac/monitor-validate-publish/monitor.py

great_expectations checkpoint run stac_items \
  --config src/pipelines/stac/monitor-validate-publish/expectations/great_expectations.yml \
  --suite stac_item_suite

python src/pipelines/stac/monitor-validate-publish/publish.py
~~~~~

---

## 🧭 Governance & Compliance

- **FAIR+CARE**:
  - Ensure STAC metadata completeness (license, providers, contacts)  
  - Log community/tribal impact when relevant in provenance and governance ledgers  

- **Security**:
  - Use least-privilege secrets  
  - Generate SBOM & manifest per release  
  - Attest CI runs via appropriate workflows  

- **Accessibility**:
  - GE data docs exported with alt-text and WCAG-aware HTML  
  - Telemetry dashboards designed with accessibility tokens  

---

## 🕰️ Version History

| Version  | Date       | Author                  | Summary                                                                 |
|----------|------------|-------------------------|-------------------------------------------------------------------------|
| v10.3.1 | 2025-11-14 | STAC Pipelines Team     | Updated orchestrator spec to KFM Markdown rules; converted examples to tilde-fences; aligned with telemetry v1 & FAIR+CARE governance. |
| v10.3.0 | 2025-11-14 | STAC Pipelines Team     | Initial orchestrator spec (ETag polling, GE gate, upsert, GitHub Actions cron). |
