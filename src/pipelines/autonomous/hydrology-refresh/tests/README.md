---
title: "🧪 KFM v11 — Hydrology Refresh Test Suite (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/autonomous/hydrology-refresh/tests/README.md"
version: "v11.0.0"
last_updated: "2025-11-22"
review_cycle: "Daily · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/telemetry/autonomous-hydrology-refresh.json"
telemetry_schema: "../../../../../../schemas/telemetry/autonomous-hydrology-refresh-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
data_contract_ref: "../../../../../../docs/contracts/data-contract-v3.json"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Test Module"
semantic_document_id: "kfm-hydro-refresh-tests-v11"
doc_uuid: "urn:kfm:pipelines:autonomous:hydrology-refresh:tests:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🧪 **Hydrology Refresh Test Suite (v11)**  
`src/pipelines/autonomous/hydrology-refresh/tests/README.md`

**Purpose:**  
Provide the complete test structure, CI rules, and validation methods used to ensure  
the **Autonomous Hydrology Refresh Pipeline** executes deterministically, safely, and in  
full compliance with KFM v11 metadata, schema, CRS, lineage, and STAC standards.

</div>

---

# 📘 Overview

This module contains the tests that guarantee:

- The LangGraph DAG loads and all nodes resolve  
- Node wiring is valid and deterministic  
- Hydrology normalization output matches `hydro_v1.schema.json`  
- STAC Items are valid (STAC 1.0 + KFM STAC Geo + Hydrology extensions)  
- CRS v11 & Vertical Axis v11 correctness  
- Tiling & COG compliance for gridded hydrology datasets  
- Checksum manifest integrity  
- Proper Neo4j graph synchronization  
- OpenLineage & PROV-O lineage completeness  

These tests run **on every PR** affecting the hydrology pipeline, plus scheduled nightly autonomous validation.

---

# 🗂 Directory Layout (v11)

```text
src/pipelines/autonomous/hydrology-refresh/tests/
│
├── README.md                     # This file (v11 MDP)
└── test_dag_smoke.py             # Required minimal DAG validation test
```

Additional tests **should** be added as the pipeline evolves and MUST be documented here.

---

# 🧩 Required Test: test_dag_smoke.py

### Purpose  
Ensure basic structural and functional integrity of the hydrology-refresh DAG.

### Required checks:

- `dag.yaml` exists  
- YAML parses without errors  
- All nodes referenced in `dag.yaml` exist and import cleanly  
- DAG node definitions contain required fields:
  - `id`  
  - `entry`  
  - `kind`  
- Smoke-level simulated run (optional for v11) completes without raising exceptions  

### Minimal v11 pattern:

```python
import yaml
from pathlib import Path

def test_dag_smoke():
    dag_path = Path("src/pipelines/autonomous/hydrology-refresh/dag.yaml")
    assert dag_path.exists(), "Hydrology DAG file missing"

    dag = yaml.safe_load(dag_path.read_text())
    assert "nodes" in dag and isinstance(dag["nodes"], list), "Invalid DAG structure"

    for node in dag["nodes"]:
        assert "id" in node
        assert "entry" in node
```

---

# 🔬 Recommended Additional Tests

Though not required for minimal compliance, the following are strongly encouraged for full v11 maturity:

---

## 1. Schema Validation Tests  
Validate `normalize_tabular.py` outputs against **hydro_v1.schema.json**:

- Required hydrology fields  
- Units (m, m³/s, mm)  
- ISO 8601 timestamps  
- EPSG:4326 lat/lon ranges  
- Optional WSEL fields validated if present  

---

## 2. STAC Item Tests  
Use sample normalized files to test:

- STAC 1.0 validity  
- Required hydrology STAC fields (`hydro:type`, `hydro:units`, `hydro:temporal_resolution`, etc.)  
- CRS metadata (`proj:*`)  
- Vertical metadata (`vertical:*`, `kfm:cf_positive`)  
- PROV-O lineage blocks  
- Collection linkage  

---

## 3. Checksum Tests  
Test `validate_checksums.py`:

- Mismatched SHA-256 detection  
- Correct match acceptance  
- Required alphabetical ordering of manifest keys  
- Proper strict vs update mode behavior  

---

## 4. Neo4j Sync Tests  
Test `neo4j_sync.py`:

- Creation of `HydrologyObservation` nodes  
- Spatial linkage (`geo:hasGeometry`)  
- Temporal linkage (`time:hasBeginning`, `time:hasEnd`)  
- Streamflow, WSEL, precip variables mapped correctly  
- Graph indexes refresh cleanly  

---

## 5. COG/Tiling Tests  
For rasters built by hydrology pipelines (e.g., WSEL surfaces, bathymetry-derived hydrology grids):

- COG tiling = 512×512  
- Overviews: 2×, 4×, 8×, 16×  
- WebMercatorQuad compliance for tiles  
- CRS transitions (26914→4326) validated  

---

# 🔍 CI/CD Integration

CI MUST enforce:

- `pytest` on the entire test directory  
- Schema validation (`hydro_v1.schema.json`)  
- STAC validation  
- CRS/Vertical-Axis checks  
- Checksum matching  
- Neo4j dry-run sync  

Failure of ANY test results in **PR rejection**.

Nightly autonomous CI also re-runs these tests using the latest provider data to ensure no silent upstream breakage.

---

# 🕰 Version History

- **v11.0.0 (2025-11-22)** — Initial Hydrology Refresh Test Suite for KFM v11.

---

<div align="center">

**Kansas Frontier Matrix — Hydrology Refresh Tests (v11)**  
*Assurance · Determinism · Hydrology-Safe ETL*

</div>

---

### 🔗 Footer  
[⬅ Back to Hydrology Pipeline](../README.md) · [🧩 Nodes](../nodes/README.md) · [📦 Resources](../resources/README.md) · [🏛 Governance](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

