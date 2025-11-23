---
title: "🧩 KFM v11 — Hydrology Refresh Nodes Module (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/autonomous/hydrology-refresh/nodes/README.md"
version: "v11.0.0"
last_updated: "2025-11-22"
review_cycle: "Daily · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/telemetry/autonomous-hydrology-refresh.json"
telemetry_schema: "../../../../../schemas/telemetry/autonomous-hydrology-refresh-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
data_contract_ref: "../../../../../docs/contracts/data-contract-v3.json"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Module"
semantic_document_id: "kfm-autonomous-hydro-nodes-v11"
doc_uuid: "urn:kfm:pipelines:autonomous:hydrology-refresh:nodes:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🧩 **Hydrology Refresh Nodes Module (v11)**  
`src/pipelines/autonomous/hydrology-refresh/nodes/README.md`

**Purpose:**  
Document each **node component** that composes the **Autonomous Hydrology Refresh pipeline**.  
These nodes deliver deterministic ingestion, normalization, STAC generation, checksum validation,  
and Neo4j graph synchronization for hydrology datasets under KFM v11.

</div>

---

# 📘 Overview

The nodes in this module form the *atomic ETL/AI building blocks* of the Autonomous Hydrology Refresh DAG:

- Every node exposes a **single** `run(...)` function  
- I/O is passed via LangGraph context dictionaries  
- Nodes MUST be:
  - Idempotent  
  - Deterministic  
  - Side-effect minimal  
  - Scope-minimal  
  - JSON/YAML schema-safe  
  - STAC v11 + Hydrology v11 compliant  
- All nodes follow **MCP-DL v6.3** documentation-first engineering rules

The full DAG behavior is defined at:  
`src/pipelines/autonomous/hydrology-refresh/README.md`.

---

# 🗂 Directory Layout (v11)

```text
src/pipelines/autonomous/hydrology-refresh/nodes/
│
├── README.md                   # This file (v11 MDP)
│
├── detect_stale.py             # Identify stale hydrology data (etag / Last-Modified)
├── fetch_sources.py            # Download sources from USGS, NOAA, KDHE, etc.
├── normalize_tabular.py        # Harmonize tabular station/flow/precip datasets
├── build_stac_items.py         # Generate STAC Items for hydrology datasets
├── validate_checksums.py       # Verify SHA-256 asset integrity
├── stac_validate.py            # Validate STAC Items against STAC v11 + Hydro schemas
├── neo4j_sync.py               # Write hydrology entities to Neo4j graph
└── post_hooks.py               # Telemetry, lineage completion, notifications
```

---

# 🧠 Node Responsibilities

## 🔎 detect_stale.py
**Role:** Determine which water/hydrology datasets must be refreshed.

**Inputs:**
- `context["providers_cfg"]`  
- `context["checksum_manifest"]`  

**Outputs:**
- `stale_targets: list[str]`

**Actions:**
- Compare provider etags + Last-Modified timestamps  
- Evaluate checksum age & upstream drift  
- Emit OpenLineage start/end events

---

## 🌐 fetch_sources.py
**Role:** Download hydrology datasets (e.g., USGS flow CSV, NOAA precip, KDHE water-quality).

**Inputs:**  
`stale_targets`, `context["workdir"]`, `providers_cfg`

**Outputs:**  
`raw_files: list[str]`

**Actions:**
- Fetch remote feeds with retry/backoff  
- Preserve provider timestamps for STAC lineage  
- Save raw files under `workdir/raw/`

---

## 📊 normalize_tabular.py
**Role:** Normalize hydrology tabular data (streamflow, groundwater, precip, etc.)

**Inputs:**  
`raw_files`, `context["schema"]`

**Outputs:**  
`norm_files: list[str]`

**Actions:**
- Standardize column names: `SITE_ID`, `DATETIME`, `FLOW_CFS`, `STAGE_M`, etc.  
- Enforce units (m, m³/s) per **Hydrology Standard v11**  
- Handle timezone → UTC normalization  
- Validate against hydrology schema  
- Output Parquet/CSV under `workdir/norm/`

---

## 🛰 build_stac_items.py
**Role:** Build **STAC Items** for each processed hydrology dataset.

**Inputs:**  
`norm_files`, `context["stac_out"]`, `context["providers_cfg"]`

**Outputs:**  
`stac_items: list[str]`

**Actions:**
- Generates Items with:
  - `hydro:type` (streamflow/bathymetry/water_surface/etc.)  
  - `datetime` or interval  
  - `geometry`, `bbox` (EPSG:4326)  
  - Vertical-axis metadata (NAVD88, GEOID18)  
  - CF-positive rules (`up` or `down`)  
  - Hydrology rasters tagged as COGs  
  - Full PROV-O lineage  

---

## 🔐 validate_checksums.py
**Role:** Check SHA-256 hashes for all STAC assets.

**Inputs:**  
`stac_items`, `checksum_manifest`

**Outputs:**  
`validated_items: list[str]`

**Actions:**
- Compute SHA-256 per asset  
- Compare to `manifest.json`  
- Fail/alert on mismatch  
- Update manifest only under governance-approved mode  

---

## 🧪 stac_validate.py
**Role:** Run comprehensive STAC validation.

**Inputs:**  
`validated_items`

**Outputs:**  
`ready_items: list[str]`

**Actions:**
- Validate against:
  - STAC 1.0  
  - KFM STAC Geo Spec v11  
  - Hydrology STAC extension  
  - CRS v11  
  - Vertical Axis v11  
- Emit structured error logs for CI  

---

## 🧠 neo4j_sync.py
**Role:** Convert hydrology STAC Items into Neo4j graph entities.

**Inputs:**  
`ready_items`

**Outputs:**  
`graph_report: dict`

**Actions:**
- Create/merge:
  - `HydrologyObservation`  
  - `StreamflowSeries`  
  - `ReservoirLevel`  
  - `BathymetryGrid`  
- Map geometry to GeoSPARQL WKT  
- Map datetime to OWL-Time  
- Refresh spatial & temporal indexes  
- Log statistics for telemetry

---

## 📬 post_hooks.py
**Role:** Post-run housekeeping and telemetry emission.

**Inputs:**  
`graph_report`

**Outputs:**  
`run_summary: dict`

**Actions:**
- Emit pipeline run telemetry  
- Close OpenLineage run event  
- Handle notifications (email/Slack if configured)  
- Rotate logs, update DAG health metrics  

---

# 🧪 Testing Requirements

All nodes MUST:

- Provide a top-level `run()` function  
- Be covered by at least one test (direct test or DAG smoke test)  
- Use only `context` for configuration (no hardcoded paths)  
- Produce deterministic outputs  
- Pass schema validation & STAC validation in CI  
- Provide error messages in machine-readable form  

A minimal smoke test is required at:  
`src/pipelines/autonomous/hydrology-refresh/tests/test_dag_smoke.py`

---

# 🧭 Node Signature (Recommended)

```python
def run(*, context, **kwargs) -> dict:
    """
    Parameters
    ----------
    context : dict
        Pipeline context: paths, schemas, configuration.
    **kwargs :
        Node-specific inputs (e.g., raw_files, stale_targets).

    Returns
    -------
    dict
        Keys match DAG `outputs` declarations.
    """
```

---

# 🕰 Version History

- **v11.0.0 (2025-11-22)** — Initial Hydrology Refresh nodes module for KFM v11.

---

<div align="center">

**Kansas Frontier Matrix — Hydrology Refresh Nodes (v11)**  
*Clear Contracts · Deterministic Behavior · Water-Safe ETL*

</div>

---

### 🔗 Footer  
[⬅ Back to Hydrology Pipeline](../README.md) · [🧰 Autonomous Utils](../../utils/README.md) · [🏛 Governance](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

