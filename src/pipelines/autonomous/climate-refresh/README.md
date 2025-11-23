---
title: "🌡️ KFM v11 — Autonomous Climate Refresh Pipeline (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/autonomous/climate-refresh/README.md"
version: "v11.0.0"
last_updated: "2025-11-22"
review_cycle: "Daily · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/telemetry/autonomous-climate-refresh.json"
telemetry_schema: "../../../../schemas/telemetry/autonomous-climate-refresh-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Pipeline"
semantic_document_id: "kfm-autonomous-climate-refresh-v11"
doc_uuid: "urn:kfm:pipelines:autonomous:climate-refresh:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🌡️ **Autonomous Climate Refresh Pipeline (v11)**  
`src/pipelines/autonomous/climate-refresh/README.md`

**Purpose:**  
Define the **autonomous, deterministic, daily climate ingestion pipeline** for NOAA, Daymet, PRISM, and  
other climate sources—producing normalized time-series, STAC Items, multi-resolution rasters, and  
Neo4j climate entities automatically under KFM v11.

</div>

---

# 📘 Overview

The **Climate Refresh Pipeline**:

- Detects stale climate datasets (NOAA NCEI, NWS, PRISM, Daymet, Mesonet)  
- Downloads + normalizes raw station, gridded, or multi-band climate data  
- Generates v11-compliant **STAC Climate Items** (gridded + tabular)  
- Ensures CRS/vertical metadata (EPSG:4326, EPSG:26914, NAVD88, GEOID18)  
- Produces cloud-optimized rasters (COG) with pyramids  
- Emits OpenLineage provenance and telemetry bundles  
- Syncs results to Neo4j using CIDOC-CRM / GeoSPARQL / OWL-Time semantics  
- Runs fully autonomously, with retries/backoff, no manual intervention  

This pipeline is part of the **KFM Autonomous Data Plane**.

---

# 🗂 Directory Layout (v11)

```text
src/pipelines/autonomous/climate-refresh/
│
├── README.md                      # This file (v11 MDP)
├── dag.yaml                        # LangGraph DAG definition
│
├── nodes/
│   ├── detect_stale.py
│   ├── fetch_sources.py
│   ├── normalize_station.py
│   ├── normalize_gridded.py
│   ├── build_stac_items.py
│   ├── validate_checksums.py
│   ├── stac_validate.py
│   ├── neo4j_sync.py
│   └── post_hooks.py
│
├── resources/
│   ├── providers.yaml
│   ├── schema/
│   │   └── climate_v1.schema.json
│   └── checksums/
│       └── manifest.json
│
└── tests/
    └── test_dag_smoke.py
```

---

# ⚙️ Climate Refresh DAG (v11)

Example `dag.yaml`:

```yaml
schedule: "0 1 * * *"
retries:
  max_attempts: 3
  backoff_seconds: 600

lineage:
  openlineage: true
  namespace: "kfm.autonomous.climate"

context:
  workdir: "data/work/staging/climate/"
  stac_out: "data/stac/climate/statewide/items/"
  checksum_manifest: "src/pipelines/autonomous/climate-refresh/resources/checksums/manifest.json"
  schema: "src/pipelines/autonomous/climate-refresh/resources/schema/climate_v1.schema.json"
  providers_cfg: "src/pipelines/autonomous/climate-refresh/resources/providers.yaml"

nodes:
  - id: detect_stale
    kind: python
    entry: "src/pipelines/autonomous/climate-refresh/nodes/detect_stale.py:run"
    outputs: ["stale_targets"]

  - id: fetch_sources
    kind: python
    entry: "src/pipelines/autonomous/climate-refresh/nodes/fetch_sources.py:run"
    inputs: ["stale_targets"]
    outputs: ["raw_files"]

  - id: normalize_station
    kind: python
    entry: "src/pipelines/autonomous/climate-refresh/nodes/normalize_station.py:run"
    inputs: ["raw_files"]
    outputs: ["station_norm"]

  - id: normalize_gridded
    kind: python
    entry: "src/pipelines/autonomous/climate-refresh/nodes/normalize_gridded.py:run"
    inputs: ["station_norm"]
    outputs: ["grid_norm"]

  - id: build_stac_items
    kind: python
    entry: "src/pipelines/autonomous/climate-refresh/nodes/build_stac_items.py:run"
    inputs: ["grid_norm"]
    outputs: ["stac_items"]

  - id: validate_checksums
    kind: python
    entry: "src/pipelines/autonomous/climate-refresh/nodes/validate_checksums.py:run"
    inputs: ["stac_items"]
    outputs: ["validated_items"]

  - id: stac_validate
    kind: python
    entry: "src/pipelines/autonomous/climate-refresh/nodes/stac_validate.py:run"
    inputs: ["validated_items"]
    outputs: ["ready_items"]

  - id: neo4j_sync
    kind: python
    entry: "src/pipelines/autonomous/climate-refresh/nodes/neo4j_sync.py:run"
    inputs: ["ready_items"]
    outputs: ["graph_report"]

  - id: post_hooks
    kind: python
    entry: "src/pipelines/autonomous/climate-refresh/nodes/post_hooks.py:run"
    inputs: ["graph_report"]
    outputs: ["run_summary"]
```

---

# 🌡 Climate Data Sources (Examples)

From `providers.yaml`:

- **NOAA NCEI** — daily/hourly climate variables  
- **NOAA NWS** — 24h summaries, station conditions  
- **PRISM** — long-term normals, monthly/annual grids  
- **Daymet** — daily 1 km grid climatology  
- **Kansas Mesonet** — high-resolution soil moisture, temp, wind  
- **CPC drought indices**, **Palmer**, **SPEI**, **SPI**  

Provider blocks include:

- `id`, `kind`, `url`  
- `etag_header`, `time_header`  
- STAC metadata  
- Provider roles (`["producer", "licensor"]`)  
- Licensing  

---

# 🧬 Climate STAC Item Requirements (v11)

Climate Items MUST include:

```json
"climate:vars": ["tmax","tmin","prcp","vpd","srad"],
"climate:temporal_resolution": "daily|hourly|monthly",
"climate:spatial_resolution_m": 1000,
"climate:processing_level": "L1|L2|L3",
"proj:epsg": 4326,
"kfm:cf_positive": "up",
"vertical:reference_frame": "NAVD88",
"vertical:geoid_model": "GEOID18",
"kfm:lineage": {...}
```

Raster climate assets MUST be COGs with pyramids (see tiling-and-pyramids.md).

---

# 🧠 Neo4j Sync Behavior

Each STAC Item becomes:

- A `ClimateObservation` or `ClimateGrid` node  
- Connected to:
  - `Place` (GeoSPARQL geometry)  
  - `TimeSpan` (OWL-Time interval)  
  - `Dataset` & `Provider` (DCAT 3.0)  

Climate variables become typed properties with unit metadata aligned to Data Contract v3.

---

# 🔍 CI/CD Rule Set

CI checks MUST validate:

- JSON Schema (`climate_v1.schema.json`)  
- STAC validation  
- CRS + vertical datum correctness  
- COG + pyramid correctness  
- Checksum manifest consistency  
- Neo4j dry-run index sync  
- OpenLineage event structure  
- Zero nondeterminism across repeated runs  

PRs failing any check → **blocked**.

---

# 🕰 Version History

- **v11.0.0 (2025-11-22)** — Initial KFM v11 Autonomous Climate Refresh pipeline.

---

<div align="center">

**Kansas Frontier Matrix — Climate Refresh Pipeline (v11)**  
*Autonomous · Deterministic · Scientifically Traceable*

</div>

---

### 🔗 Footer  
[⬅ Back to Autonomous Pipelines](../README.md) · [🧰 Utilities](../utils/README.md) · [🏛 Governance](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

