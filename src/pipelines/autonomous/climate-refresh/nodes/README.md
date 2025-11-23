---
title: "🧩 KFM v11 — Climate Refresh Nodes Module (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/autonomous/climate-refresh/nodes/README.md"
version: "v11.0.0"
last_updated: "2025-11-22"
review_cycle: "Daily · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/telemetry/autonomous-climate-refresh.json"
telemetry_schema: "../../../../../schemas/telemetry/autonomous-climate-refresh-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
data_contract_ref: "../../../../../docs/contracts/data-contract-v3.json"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Module"
semantic_document_id: "kfm-autonomous-climate-nodes-v11"
doc_uuid: "urn:kfm:pipelines:autonomous:climate-refresh:nodes:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🧩 **Climate Refresh Nodes Module (v11)**  
`src/pipelines/autonomous/climate-refresh/nodes/README.md`

**Purpose:**  
Document the individual **node components** that form the **Autonomous Climate Refresh** LangGraph DAG.  
Each node is a small, deterministic Python unit performing one ETL/AI step with full **STAC**, **schema**,  
and **lineage** guarantees under KFM v11.

</div>

---

# 📘 Overview

The **nodes** in this module are the building blocks of the **Autonomous Climate Refresh** pipeline:

- Each file exposes a single `run(...)` function wired from `dag.yaml`  
- Inputs/outputs are passed via dictionaries (LangGraph context)  
- All nodes MUST be:
  - Idempotent  
  - Deterministic  
  - Side-effect minimal (beyond declared outputs)  
  - Documented with MCP-DL v6.3  
  - Validated against `climate_v1.schema.json` and STAC v11 requirements  

The DAG-level orchestration is defined in:  
`src/pipelines/autonomous/climate-refresh/README.md` and `dag.yaml`.

---

# 🗂 Directory Layout (v11)

```text
src/pipelines/autonomous/climate-refresh/nodes/
│
├── README.md                  # This file (v11 MDP)
│
├── detect_stale.py            # Identify stale climate datasets (station + gridded)
├── fetch_sources.py           # Download climate feeds (NOAA, Daymet, PRISM, Mesonet)
├── normalize_station.py       # Normalize station-based time series
├── normalize_gridded.py       # Normalize gridded climate rasters
├── build_stac_items.py        # Build climate STAC Items (station + gridded)
├── validate_checksums.py      # Verify checksum manifest integrity
├── stac_validate.py           # STAC + schema validation
├── neo4j_sync.py              # Sync climate entities into Neo4j
└── post_hooks.py              # Telemetry, notifications, post-run housekeeping
```

---

# 🧠 Node Responsibilities

## 🔎 detect_stale.py

**Role:** Determine which climate provider datasets are **stale** and need refresh.

**Inputs:**

- `context["providers_cfg"]` — YAML listing providers (NOAA, Daymet, PRISM, Mesonet, etc.)  
- `context["checksum_manifest"]` — known checksums and last-update info  

**Outputs:**

- `stale_targets: list[str]` — provider IDs requiring refresh

**Behavior:**

- Compare remote ETag / Last-Modified headers vs local manifest timestamps  
- Use deterministic rules (no randomness)  
- Emit OpenLineage Job/Run events via `utils.lineage`  

---

## 🌐 fetch_sources.py

**Role:** Fetch raw climate data from configured providers.

**Inputs:**

- `stale_targets: list[str]`  
- `context["workdir"]`  
- `context["providers_cfg"]`  

**Outputs:**

- `raw_files: list[str]` — local paths to downloaded raw datasets  

**Behavior:**

- Uses `utils.file_io` for HTTP requests, retries, backoff  
- Writes to `workdir/raw/`  
- Emits OpenLineage events for each fetch operation  

---

## 🌡 normalize_station.py

**Role:** Normalize station-based climate data (e.g., NOAA, Mesonet).

**Inputs:**

- `raw_files: list[str]`  
- `context["schema"]` — `climate_v1.schema.json`  

**Outputs:**

- `station_norm: list[str]` — normalized Parquet/CSV station time-series files  

**Behavior:**

- Harmonizes fields: `STATION_ID`, `DATE`, `TMAX`, `TMIN`, `PRCP`, `WSPD`, etc.  
- Ensures units and missing-value handling align with Data Contract v3  
- Validates against `climate_v1.schema.json` (station subset)  
- Writes to `workdir/station_norm/`  

---

## 🛰 normalize_gridded.py

**Role:** Normalize gridded climate datasets (Daymet, PRISM, NCEI grids).

**Inputs:**

- `station_norm: list[str]` (optional context if station data is used for QC/QA)  
- `context["schema"]` — `climate_v1.schema.json`  

**Outputs:**

- `grid_norm: list[str]` — normalized gridded rasters or multi-band COGs  

**Behavior:**

- Reprojects data into required CRSs (EPSG:26914 for processing, EPSG:4326 for STAC geometry)  
- Ensures each grid has:
  - Proper `proj:*` metadata  
  - CF-compliant variable naming (e.g., `tmax`, `tmin`, `prcp`)  
- Produces COG-ready rasters with correct nodata and scaling  
- Validates grid metadata against schema and tiling standards  

---

## 🗂 build_stac_items.py

**Role:** Build **STAC Items** for station and gridded climate datasets.

**Inputs:**

- `grid_norm: list[str]`  
- Potentially `station_norm` (if Items include embedded station summaries)  
- `context["stac_out"]`  
- `context["providers_cfg"]`  

**Outputs:**

- `stac_items: list[str]` — paths to STAC Item JSON files  

**Behavior:**

- Uses `utils.stac_tools` to construct Items with:
  - `climate:vars`, `climate:temporal_resolution`, `climate:spatial_resolution_m`  
  - `datetime` or interval fields  
  - `geometry`, `bbox`, `proj:*`, `vertical:*` (NAVD88/GEOID18)  
  - PROV-O lineage (`kfm:lineage`)  
- Writes Items to `data/stac/climate/statewide/items/`  

---

## 🔐 validate_checksums.py

**Role:** Verify that all STAC assets match the checksum manifest.

**Inputs:**

- `stac_items: list[str]`  
- `context["checksum_manifest"]`  

**Outputs:**

- `validated_items: list[str]`  

**Behavior:**

- Uses `utils.checksum_tools` to compute SHA-256 for referenced assets (COGs, station files)  
- Compares to `manifest.json`  
- Fails on mismatch in strict CI mode  
- Optionally updates manifest in governance-approved modes  

---

## ✅ stac_validate.py

**Role:** Enforce STAC 1.0 and KFM **STAC Geo Spec v11** compliance.

**Inputs:**

- `validated_items: list[str]`  

**Outputs:**

- `ready_items: list[str]`  

**Behavior:**

- Uses STAC validators + `utils.stac_tools`  
- Ensures:
  - Core STAC fields present  
  - CRS, vertical, hydrology/climate extensions populated  
  - DCAT 3.0 mapping possible  
- Outputs error reports for CI and telemetry  

---

## 🧠 neo4j_sync.py

**Role:** Sync climate STAC Items into the Neo4j graph.

**Inputs:**

- `ready_items: list[str]`  

**Outputs:**

- `graph_report: dict` — e.g., `{"items": N, "status": "ok"}`  

**Behavior:**

- Uses `utils.neo4j_tools` to:
  - Create/merge `ClimateGrid` and `ClimateObservation` nodes  
  - Link to `Place` (GeoSPARQL) and `TimeSpan` (OWL-Time)  
  - Attach climate variables and units as properties  
- Refreshes relevant indexes  
- Emits metrics for telemetry and health dashboard  

---

## 📬 post_hooks.py

**Role:** Post-run housekeeping and telemetry.

**Inputs:**

- `graph_report: dict`  

**Outputs:**

- `run_summary: dict` — e.g., `{"ok": True, "details": graph_report}`  

**Behavior:**

- Writes telemetry bundle referenced by `telemetry_ref`  
- Optionally sends notifications (Slack/email)  
- Cleans up temp files/logs according to retention policy  
- Finalizes OpenLineage run with success/failure status  

---

# 🧪 Testing & MCP Requirements

Each node MUST:

- Define a top-level `run(...)` function  
- Be covered by at least one test (direct or via DAG smoke test)  
- Use configuration from `context` only (no hard-coded paths/endpoints)  
- Avoid non-deterministic behavior (no random without fixed seed)  
- Document its purpose, inputs, and outputs per MCP-DL v6.3  

`tests/test_dag_smoke.py` must:

- Verify DAG can be parsed  
- Verify nodes are structurally valid  
- Optionally simulate a mini-run with mocked inputs  

---

# 🧭 Recommended Node Signature

Nodes SHOULD use this pattern:

```python
def run(*, context, **kwargs) -> dict:
    """
    Parameters
    ----------
    context : dict
        Global DAG-level context (paths, configs, schemas).
    **kwargs :
        Node-specific inputs wired from DAG (e.g., stale_targets, raw_files).

    Returns
    -------
    dict
        Outputs keyed by DAG `outputs` names.
    """
```

This keeps the contract:

- Explicit  
- Type-hint friendly  
- LangGraph/YAML-DAG compatible  

---

# 🕰 Version History

- **v11.0.0 (2025-11-22)** — Initial climate-refresh nodes module for KFM v11.

---

<div align="center">

**Kansas Frontier Matrix — Climate Refresh Nodes (v11)**  
*Clear Contracts · Deterministic Behavior · Climate-Safe ETL*

</div>

---

### 🔗 Footer  
[⬅ Back to Climate Pipeline](../README.md) · [🤖 Autonomous Pipelines Index](../../README.md) · [🧰 Autonomous Utils](../../utils/README.md) · [🏛 Governance](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

