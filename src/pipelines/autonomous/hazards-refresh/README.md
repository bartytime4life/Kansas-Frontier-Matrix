---
title: "⚡ KFM v11 — Autonomous Hazards Refresh Pipeline (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/autonomous/hazards-refresh/README.md"
version: "v11.0.0"
last_updated: "2025-11-22"
review_cycle: "Daily · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/telemetry/autonomous-hazards-refresh.json"
telemetry_schema: "../../../../schemas/telemetry/autonomous-hazards-refresh-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Pipeline"
semantic_document_id: "kfm-autonomous-hazards-refresh-v11"
doc_uuid: "urn:kfm:pipelines:autonomous:hazards-refresh:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# ⚡ **Autonomous Hazards Refresh Pipeline (v11)**  
`src/pipelines/autonomous/hazards-refresh/README.md`

**Purpose:**  
Provide the complete, autonomous, zero-touch ingestion and refresh pipeline for **hazards data**  
(NOAA Storm Events, NWS severe weather, FEMA disaster declarations, USGS seismicity, wildfire datasets,  
and related hazard chronologies) using LangGraph YAML DAGs, STAC v11 datasets, and Neo4j sync.

</div>

---

# 📘 Overview

The **Hazards Refresh** pipeline maintains continuously updated hazard datasets for Kansas, including:

- **NOAA Storm Events** (tornado, hail, wind, flood, extreme temp)  
- **NWS hazards** (live warnings; polygon feeds)  
- **FEMA disaster declarations** (federal-level)  
- **USGS earthquake/seismic activity**  
- **Wildfire detection** (MODIS/VIIRS, where available)  
- **Seasonal hazard composites**, **impact summaries**, **event clustering**  

Pipeline characteristics:

- Fully autonomous  
- STAC-first architecture  
- Daily + on-demand backfill  
- OpenLineage provenance  
- Neo4j graph write patterns (CIDOC-CRM + GeoSPARQL + OWL-Time)  
- Compliance with KFM v11 Hydrology, CRS, STAC, Vertical Axis, and Tiling Standards  

---

# 🗂 Directory Layout (v11)

```text
src/pipelines/autonomous/hazards-refresh/
│
├── README.md                        # This file (v11 MDP)
├── dag.yaml                          # LangGraph DAG
│
├── nodes/
│   ├── detect_stale.py               # Detect datasets needing refresh
│   ├── fetch_sources.py              # Download hazard data
│   ├── normalize_events.py           # Normalize tabular/polygon feeds
│   ├── build_stac_items.py           # Construct STAC Items w/ hazard extensions
│   ├── validate_checksums.py
│   ├── stac_validate.py
│   ├── neo4j_sync.py                 # Update graph (events, locations, timelines)
│   └── post_hooks.py
│
├── resources/
│   ├── providers.yaml                # All hazard data providers
│   ├── schema/
│   │   └── hazards_v1.schema.json
│   └── checksums/
│       └── manifest.json
│
└── tests/
    └── test_dag_smoke.py
```

---

# ⚙️ LangGraph DAG (v11 Example)

`src/pipelines/autonomous/hazards-refresh/dag.yaml`

```yaml
schedule: "0 2 * * *"
retries:
  max_attempts: 3
  backoff_seconds: 600

lineage:
  openlineage: true
  namespace: "kfm.autonomous.hazards"

context:
  workdir: "data/work/staging/tabular/normalized/hazards/"
  stac_out: "data/stac/hazards/statewide/items/"
  checksum_manifest: "src/pipelines/autonomous/hazards-refresh/resources/checksums/manifest.json"
  schema: "src/pipelines/autonomous/hazards-refresh/resources/schema/hazards_v1.schema.json"
  providers_cfg: "src/pipelines/autonomous/hazards-refresh/resources/providers.yaml"

nodes:
  - id: detect_stale
    kind: python
    entry: "src/pipelines/autonomous/hazards-refresh/nodes/detect_stale.py:run"
    outputs: ["stale_targets"]

  - id: fetch_sources
    kind: python
    entry: "src/pipelines/autonomous/hazards-refresh/nodes/fetch_sources.py:run"
    inputs: ["stale_targets"]
    outputs: ["raw_files"]

  - id: normalize_events
    kind: python
    entry: "src/pipelines/autonomous/hazards-refresh/nodes/normalize_events.py:run"
    inputs: ["raw_files"]
    outputs: ["norm_files"]

  - id: build_stac_items
    kind: python
    entry: "src/pipelines/autonomous/hazards-refresh/nodes/build_stac_items.py:run"
    inputs: ["norm_files"]
    outputs: ["stac_items"]

  - id: validate_checksums
    kind: python
    entry: "src/pipelines/autonomous/hazards-refresh/nodes/validate_checksums.py:run"
    inputs: ["stac_items"]
    outputs: ["validated_items"]

  - id: stac_validate
    kind: python
    entry: "src/pipelines/autonomous/hazards-refresh/nodes/stac_validate.py:run"
    inputs: ["validated_items"]
    outputs: ["ready_items"]

  - id: neo4j_sync
    kind: python
    entry: "src/pipelines/autonomous/hazards-refresh/nodes/neo4j_sync.py:run"
    inputs: ["ready_items"]
    outputs: ["graph_report"]

  - id: post_hooks
    kind: python
    entry: "src/pipelines/autonomous/hazards-refresh/nodes/post_hooks.py:run"
    inputs: ["graph_report"]
    outputs: ["run_summary"]
```

---

# 🌩 Hazard Providers (Example)

`resources/providers.yaml`

```yaml
providers:
  - id: "noaa.storm_events"
    kind: "csv_http"
    url: "https://example.noaa.gov/stormevents/ks/latest.csv"
    etag_header: "ETag"
    time_header: "Last-Modified"
    stac:
      collection: "kfm-hazards-statewide"
      license: "CC0-1.0"
      providers:
        - name: "NOAA"
          roles: ["producer"]

  - id: "fema.disasters"
    kind: "json_http"
    url: "https://example.fema.gov/api/disasters?state=KS"
    etag_header: "ETag"
    time_header: "Last-Modified"
    stac:
      collection: "kfm-hazards-statewide"
      license: "CC0-1.0"
      providers:
        - name: "FEMA"
          roles: ["producer"]

  - id: "usgs.earthquakes"
    kind: "geojson_http"
    url: "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minlatitude=36&maxlatitude=41&minlongitude=-103&maxlongitude=-94"
    stac:
      collection: "kfm-hazards-statewide"
      license: "U.S. Government Works"
      providers:
        - name: "USGS"
          roles: ["producer"]
```

---

# 🧪 Node Stubs (Minimal v11)

`nodes/normalize_events.py`

```python
def run(raw_files, context):
    # Normalize columns: EVENT_ID, TYPE, START_TIME, END_TIME, LAT, LON, etc.
    # Harmonize hazard_type taxonomy: tornado, hail, wind, flood, wildfire, seismic.
    # Output CSV or Parquet; ensure schema matches hazards_v1.schema.json.
    return {"norm_files": [".../norm/noaa_storms.parquet"]}
```

`nodes/build_stac_items.py`

```python
def run(norm_files, context):
    # Build STAC Items with hazard metadata:
    # hazard:type, hazard:severity, hazard:geometry, datetime, bbox, CRS, lineage.
    return {"stac_items": [".../items/storm_2025-11-22.json"]}
```

`nodes/neo4j_sync.py`

```python
def run(ready_items, context):
    # Upsert HazardEvent nodes and connect to Place, TimeSpan, and HazardType.
    return {"graph_report": {"items": len(ready_items), "status": "ok"}}
```

---

# 🚨 Hazard STAC Metadata (v11 Required)

Hazard STAC Items MUST include:

```json
"hazard:type": "tornado|hail|wind|flood|wildfire|earthquake|storm",
"hazard:severity": "minor|severe|extreme",
"hazard:taxonomy": "noaa|nws|fema|usgs",
"hazard:people_affected": <int>,
"hazard:property_damage_usd": <float>,
"hazard:injuries": <int>,
"hazard:fatalities": <int>
```

Plus all **STAC GEO**, **CRS**, **Vertical-Axis**, **Tiling**, **Lineage**, and **DCAT3** fields required by v11.

---

# 🧭 Integration in the Autonomous Data Plane

Hazards Refresh is one of three major autonomous ingestion systems:

- **Hydrology Refresh**  
- **Climate Refresh** (planned)  
- **Hazards Refresh** (this pipeline)  

Its STAC outputs feed:

- Focus Mode  
- Timeline hazard overlays  
- MapLibre hazard layers  
- Graph event networks  
- Story Node generation where culturally appropriate  

---

# 🔍 CI/CD Requirements

CI must enforce:

- STAC 1.0 validation  
- hazards_v1.schema.json validation  
- Checksum manifest matching  
- Neo4j dry-run sync  
- Lineage + OpenLineage event validation  
- CRS + vertical metadata compliance  
- No missing hazard:event required fields  

Failure → PR blocked.

---

# 🕰 Version History

- **v11.0.0 (2025-11-22):** Initial autonomous hazards ingest pipeline (v11 MDP).

---

<div align="center">

**Kansas Frontier Matrix — Autonomous Hazards Pipeline (v11)**  
*Real-Time Insight · Deterministic ETL · Provenance-Driven*

</div>

---

### 🔗 Footer  
[⬅ Back to Autonomous Pipelines](../README.md) · [🧰 Utilities](../utils/README.md) · [🏛 Governance](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

