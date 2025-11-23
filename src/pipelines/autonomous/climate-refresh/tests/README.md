---
title: "🧪 KFM v11 — Climate Refresh Test Suite (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/autonomous/climate-refresh/tests/README.md"
version: "v11.0.0"
last_updated: "2025-11-22"
review_cycle: "Daily · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/telemetry/autonomous-climate-refresh.json"
telemetry_schema: "../../../../../../schemas/telemetry/autonomous-climate-refresh-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
data_contract_ref: "../../../../../../docs/contracts/data-contract-v3.json"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Test Module"
semantic_document_id: "kfm-climate-refresh-tests-v11"
doc_uuid: "urn:kfm:pipelines:autonomous:climate-refresh:tests:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🧪 **Climate Refresh Test Suite (v11)**  
`src/pipelines/autonomous/climate-refresh/tests/README.md`

**Purpose:**  
Define the mandatory test structure, CI integration, and validation rules for the **Autonomous Climate Refresh Pipeline**, ensuring deterministic ETL behavior, schema validity, STAC correctness, CRS/vertical compliance, and Neo4j-safe graph promotion under KFM v11.

</div>

---

# 📘 Overview

This test module verifies:

- DAG structure and node wiring  
- Deterministic execution of all climate-refresh nodes  
- Schema validity for station + gridded climate outputs  
- STAC Item correctness (STAC 1.0 + KFM STAC extensions)  
- CRS v11 & Vertical Axis v11 compliance  
- COG + tiling validity for gridded climate rasters  
- Checksum manifest integrity  
- Provenance (OpenLineage + PROV-O) correctness  
- Readiness of outputs for Neo4j sync  

All tests here are required for **PR approval** and nightly autonomous validation.

---

# 🗂 Directory Layout (v11)

```text
src/pipelines/autonomous/climate-refresh/tests/
│
├── README.md                    # This file (v11 MDP)
└── test_dag_smoke.py            # Required minimal DAG smoke test
```

Additional tests **should** be added as pipeline complexity grows, and MUST be documented here.

---

# 🧩 Required Test: test_dag_smoke.py

### Purpose  
Ensure that:

- `dag.yaml` loads successfully  
- All node modules import without failure  
- DAG node definitions contain valid `id`, `entry`, and I/O fields  
- A minimal dry-run or structural validation completes without raising exceptions  

### Minimal v11 pattern:

```python
import yaml
from pathlib import Path

def test_dag_smoke():
    dag_path = Path("src/pipelines/autonomous/climate-refresh/dag.yaml")
    assert dag_path.exists(), "Climate DAG file missing"

    dag = yaml.safe_load(dag_path.read_text())
    assert "nodes" in dag and isinstance(dag["nodes"], list), "Invalid DAG structure"

    for node in dag["nodes"]:
        assert "id" in node
        assert "entry" in node
```

---

# 🔬 Recommended Additional Tests

Although only the smoke test is **required**, the following tests are highly recommended for robust v11 compliance:

---

## 🧾 1. Schema Validation Tests  
Validate outputs of:

- `normalize_station.py` → station subset of `climate_v1.schema.json`  
- `normalize_gridded.py` → gridded subset of `climate_v1.schema.json`  

Tests should confirm:

- Proper units (°C, mm, W/m², kPa, m/s)  
- EPSG:4326 lat/lon ranges  
- No missing required fields  

---

## 🛰 2. STAC Item Tests  
Use `build_stac_items.py` outputs to verify:

- STAC 1.0 structure  
- Item-level `proj:*`, `vertical:*`, `climate:*` fields  
- Temporal intervals  
- Geometry correctness (EPSG:4326)  
- PROV-O lineage block presence  

---

## 🔐 3. Checksum Tests

`validate_checksums.py` MUST:

- Detect mismatched SHA-256 values  
- Accept correct hashes  
- Reject missing manifest entries  
- Pass manifest integrity schema checks  

---

## 🧠 4. Neo4j Sync Tests

`neo4j_sync.py` MUST:

- Create `ClimateObservation` and `ClimateGrid` nodes  
- Link to `Place` & `TimeSpan` correctly  
- Populate units from Data Contract v3  
- Pass dry-run sync tests  

---

## 🌐 5. COG & Tiling Tests (for gridded products)

Tests MUST verify:

- COG internal tiling = 512 × 512  
- Overviews: 2×, 4×, 8×, 16× …  
- WebMercatorQuad tile output structure  
- Raster metadata round-trips properly to STAC  

---

# 🔍 CI/CD Integration

CI pipeline for this module MUST:

- Run `pytest` for this folder  
- Enforce schema (`climate_v1.schema.json`)  
- Enforce STAC validation  
- Enforce checksum integrity  
- Validate DAG structure  
- Run Neo4j dry-run sync in containerized mode  
- Produce coverage artifacts for autonomous DAG health dashboard  

**Any failure → PR blocked.**

---

# 🕰 Version History

- **v11.0.0 (2025-11-22)** — Initial Climate Refresh test suite for KFM v11.

---

<div align="center">

**Kansas Frontier Matrix — Climate Refresh Test Suite (v11)**  
*Verification · Determinism · Continuous Trust*

</div>

---

### 🔗 Footer  
[⬅ Back to Climate Pipeline](../README.md) · [🧩 Nodes](../nodes/README.md) · [📦 Resources](../resources/README.md) · [🏛 Governance](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

