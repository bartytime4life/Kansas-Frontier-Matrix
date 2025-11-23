---
title: "🧩 KFM v11 — Hazards Refresh Nodes Module (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/autonomous/hazards-refresh/nodes/README.md"
version: "v11.0.0"
last_updated: "2025-11-22"
review_cycle: "Daily · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/telemetry/autonomous-hazards-refresh.json"
telemetry_schema: "../../../../../schemas/telemetry/autonomous-hazards-refresh-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
data_contract_ref: "../../../../../docs/contracts/data-contract-v3.json"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Module"
semantic_document_id: "kfm-autonomous-hazards-nodes-v11"
doc_uuid: "urn:kfm:pipelines:autonomous:hazards-refresh:nodes:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🧩 **Hazards Refresh Nodes Module (v11)**  
`src/pipelines/autonomous/hazards-refresh/nodes/README.md`

**Purpose:**  
Document the individual **node components** that make up the **Autonomous Hazards Refresh** LangGraph DAG.  
Each node is a small, deterministic Python unit that performs one ETL/AI step with full **STAC**, **lineage**, and **schema** guarantees.

</div>

---

# 📘 Overview

The **nodes** in this module are the building blocks of the **Autonomous Hazards Refresh** pipeline:

- Each file implements a single `run(...)` function wired from `dag.yaml`  
- Inputs/outputs are passed via in-memory dictionaries (LangGraph context)  
- All nodes must be:
  - Idempotent  
  - Deterministic  
  - Side-effect minimal (beyond declared outputs)  
  - Fully documented and covered by tests  
  - Compliant with hazards_v1 schema and STAC v11 requirements  

The DAG-level behavior for this module is specified in:  
`src/pipelines/autonomous/hazards-refresh/README.md` and `dag.yaml`.

---

# 🗂 Directory Layout (v11)

```text
src/pipelines/autonomous/hazards-refresh/nodes/
│
├── README.md                 # This file (v11 MDP)
│
├── detect_stale.py           # Identify which hazard datasets need refresh
├── fetch_sources.py          # Download NOAA/FEMA/USGS hazard feeds
├── normalize_events.py       # Normalize tabular/polygon hazard records
├── build_stac_items.py       # Build STAC Items with hazard extensions
├── validate_checksums.py     # Verify checksum manifest integrity
├── stac_validate.py          # Run STAC schema validation
├── neo4j_sync.py             # Sync hazard events into Neo4j graph
└── post_hooks.py             # Telemetry, notifications, post-run housekeeping
```

---

# 🧠 Node Responsibilities

## 🔎 detect_stale.py

**Role:** Determine which hazard provider datasets are **stale** and require refresh.

**Inputs:**

- `context["providers_cfg"]` — YAML listing hazard providers  
- `context["checksum_manifest"]` — known checksums, last-update info  

**Outputs:**

- `stale_targets: list[str]` — provider IDs requiring refresh

**Behavior:**

- Compare remote etags / Last-Modified to local manifest  
- Use deterministic rules (no randomness)  
- Emit OpenLineage start/end events via `utils.lineage`  

---

## 🌐 fetch_sources.py

**Role:** Fetch raw hazard data from remote providers.

**Inputs:**

- `stale_targets: list[str]`  
- `context["workdir"]` — base path for staging  
- `context["providers_cfg"]`  

**Outputs:**

- `raw_files: list[str]` — file paths to local raw downloads  

**Behavior:**

- Uses `utils.file_io` for HTTP requests, ETag/Last-Modified, retries  
- Produces machine-readable OpenLineage Job/Run events  
- Writes raw files under `workdir/raw/`  

---

## 🧾 normalize_events.py

**Role:** Normalize raw hazard feeds into consistent schemas and coordinate systems.

**Inputs:**

- `raw_files: list[str]`  
- `context["schema"]` — hazards_v1.schema.json  

**Outputs:**

- `norm_files: list[str]` — Parquet/CSV files with normalized hazard events  

**Behavior:**

- Harmonizes columns: `EVENT_ID`, `HAZARD_TYPE`, `START_TIME`, `END_TIME`, `LAT`, `LON`, `COUNTY_FIPS`, etc.  
- Normalizes **hazard_type** taxonomy: `tornado`, `hail`, `wind`, `flood`, `wildfire`, `earthquake`, `storm`  
- Projects any spatial data into EPSG:4326 (CRS Standard v11)  
- Validates against `hazards_v1.schema.json`  
- Writes `workdir/norm/` outputs  

---

## 🛰 build_stac_items.py

**Role:** Build **STAC Items** for each normalized hazard dataset.

**Inputs:**

- `norm_files: list[str]`  
- `context["stac_out"]` — output directory for STAC Items  
- `context["providers_cfg"]`  

**Outputs:**

- `stac_items: list[str]` — filesystem paths to STAC Item JSON files  

**Behavior:**

- Uses `utils.stac_tools` to construct STAC Items with:
  - `hazard:type`, `hazard:severity`, `hazard:taxonomy`  
  - `datetime` or `start_datetime`/`end_datetime`  
  - `geometry` (EPSG:4326), `bbox`  
  - CRS + vertical metadata (as needed)  
  - PROV-O lineage block (`kfm:lineage`)  
- Writes STAC Items into `data/stac/hazards/statewide/items/`  

---

## 🔐 validate_checksums.py

**Role:** Ensure each STAC Item’s assets match known checksums.

**Inputs:**

- `stac_items: list[str]`  
- `context["checksum_manifest"]`  

**Outputs:**

- `validated_items: list[str]`  

**Behavior:**

- Uses `utils.checksum_tools` to compute SHA-256 for referenced assets  
- Compares against `manifest.json`  
- Operates in:
  - **strict mode** for PR validation  
  - **update mode** only where allowed by governance  
- Fails fast if any mismatch is detected  

---

## ✅ stac_validate.py

**Role:** Enforce **STAC 1.0** and **KFM STAC Geo Spec** compliance.

**Inputs:**

- `validated_items: list[str]`  

**Outputs:**

- `ready_items: list[str]` — STAC Items fully ready for Neo4j sync  

**Behavior:**

- Uses STAC validators + `utils.stac_tools`  
- Enforces:
  - `stac_version`  
  - required STAC core fields  
  - KFM STAC Geo, hydrology/hazard extensions  
  - DCAT-mappable metadata presence  
- On failure, outputs structured error logs for CI and telemetry  

---

## 🧠 neo4j_sync.py

**Role:** Sync hazard STAC Items into the **KFM Neo4j knowledge graph**.

**Inputs:**

- `ready_items: list[str]`  

**Outputs:**

- `graph_report: dict` — e.g. `{"items": N, "status": "ok"}`  

**Behavior:**

- Uses `utils.neo4j_tools` to:
  - Create/merge `HazardEvent` nodes  
  - Link to `Place` (GeoSPARQL) and `TimeSpan` (OWL-Time)  
  - Attach severity, type, impact metrics  
- Refreshes graph indexes (spatial & temporal)  
- Emits run metrics for telemetry  

---

## 📬 post_hooks.py

**Role:** Final housekeeping & telemetry after a successful (or failed) run.

**Inputs:**

- `graph_report: dict`  

**Outputs:**

- `run_summary: dict` — final pipeline status  

**Behavior:**

- Emits summary telemetry (to `telemetry_ref`)  
- Can notify Slack/email channels if configured  
- Archives logs/metrics for later analysis  
- Decorates OpenLineage run with a final “completed” status  

---

# 🧪 Testing & MCP Requirements

All nodes MUST:

- Expose a top-level `run(...)` function  
- Have at least one unit test (e.g., using stub inputs)  
- Respect MCP-DL v6.3 (documented behavior, clear inputs/outputs)  
- Avoid uncontrolled side effects (log/print only via standard logging)  
- Use configuration exclusively via `context`  

The `tests/test_dag_smoke.py` must at minimum:

- Import each node module  
- Execute a stubbed DAG run path  
- Assert that `run_summary.ok` is `True` for the happy path  

---

# 🧭 Node Contract Pattern (Recommended)

Each node’s `run` signature SHOULD follow:

```python
def run(*, context, **kwargs) -> dict:
    """
    Parameters
    ----------
    context : dict
        Global DAG-level context (paths, schemas, configs).
    **kwargs :
        Node-specific inputs wired from DAG (e.g., stale_targets, raw_files).

    Returns
    -------
    dict
        Outputs keyed by DAG `outputs` names.
    """
```

This keeps the node contract:

- Explicit  
- Type-hint friendly  
- LangGraph-compatible  

---

# 🕰 Version History

- **v11.0.0 (2025-11-22)** — Initial nodes module for Hazards Refresh pipeline (KFM v11).

---

<div align="center">

**Kansas Frontier Matrix — Hazards Refresh Nodes (v11)**  
*Small Units · Clear Contracts · Autonomous Reliability*

</div>

---

### 🔗 Footer  
[⬅ Back to Hazards Pipeline](../README.md) · [🤖 Autonomous Pipelines Index](../../README.md) · [🧰 Autonomous Utils](../../utils/README.md) · [🏛 Governance](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

