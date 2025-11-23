---
title: "🧪 KFM v11 — Hazards Refresh Test Suite (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/autonomous/hazards-refresh/tests/README.md"
version: "v11.0.0"
last_updated: "2025-11-22"
review_cycle: "Daily · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/telemetry/autonomous-hazards-refresh.json"
telemetry_schema: "../../../../../../schemas/telemetry/autonomous-hazards-refresh-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
data_contract_ref: "../../../../../../docs/contracts/data-contract-v3.json"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Test Module"
semantic_document_id: "kfm-hazards-refresh-tests-v11"
doc_uuid: "urn:kfm:pipelines:autonomous:hazards-refresh:tests:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🧪 **Hazards Refresh Test Suite (v11)**  
`src/pipelines/autonomous/hazards-refresh/tests/README.md`

**Purpose:**  
Define the test structure, coverage, and CI requirements for the **Autonomous Hazards Refresh pipeline**.  
These tests guarantee that DAG wiring, node contracts, schemas, and STAC outputs remain correct, deterministic,  
and compliant with KFM v11 standards.

</div>

---

# 📘 Overview

The **tests** in this module ensure that the hazards-refresh pipeline:

- Loads and executes its **LangGraph DAG** without errors  
- Wires node inputs/outputs correctly  
- Produces **normalized events** that match `hazards_v1.schema.json`  
- Generates **valid STAC Items** conforming to `stac-geo-spec.md` and hazards extensions  
- Honors CRS, vertical, and hydrology/hazards standards  
- Emits lineage and telemetry as expected  
- Remains deterministic across runs  

All tests are **mandatory** for CI pass before merging PRs that touch this pipeline.

---

# 🗂 Directory Layout (v11)

```text
src/pipelines/autonomous/hazards-refresh/tests/
│
├── README.md                    # This file
└── test_dag_smoke.py            # Minimal DAG + node smoke test (required)
```

Future files (e.g., `test_normalize_events.py`, `test_stac_items.py`) MUST be added here and documented in this README.

---

# 🧩 test_dag_smoke.py — Required Smoke Test

The **smoke test** verifies:

- `dag.yaml` can be parsed  
- Each node module is importable  
- A minimal DAG run completes without raising exceptions  
- `run_summary` is returned and indicates success  

### 🧪 Minimal Pattern (Conceptual)

```python
import json
import yaml
from pathlib import Path

def test_dag_smoke():
    dag_path = Path("src/pipelines/autonomous/hazards-refresh/dag.yaml")
    assert dag_path.exists(), "DAG file is missing"

    dag = yaml.safe_load(dag_path.read_text())
    assert "nodes" in dag and dag["nodes"], "DAG must define nodes"

    # Optionally: simulate a very thin run using a test runner or mocked nodes
    # For v11, at least assert that node entries are structurally valid.
    for node in dag["nodes"]:
        assert "id" in node
        assert "entry" in node
```

Pipeline-specific projects may extend this smoke test to run a **full in-memory DAG execution** with stubbed inputs.

---

# 🧬 Recommended Additional Tests

While not strictly required for v11 minimal compliance, the following tests are **strongly recommended**:

## 🧾 Schema Validation

- `test_normalize_events_schema.py`  
  - Feed a small fixture of raw hazard records into `normalize_events.py`  
  - Assert outputs validate against `hazards_v1.schema.json`  
  - Assert CRS = EPSG:4326 and lat/lon are within valid ranges  

## 🛰 STAC Item Tests

- `test_stac_items_valid.py`  
  - Call `build_stac_items.py` with a small fixture `norm_files`  
  - Validate each resulting STAC Item with:
    - STAC 1.0 validator  
    - KFM STAC Geo Spec (CRS, vertical, hazard fields)  

## 🔐 Checksum & Manifest Tests

- `test_checksums.py`  
  - Use temporary files + `validate_checksums.py`  
  - Ensure mismatched checksums cause failures  
  - Ensure manifest updates follow governance rules (if supported in tests)  

## 🧠 Neo4j Sync Tests

- `test_neo4j_sync.py`  
  - Use an ephemeral Neo4j container or in-memory mock  
  - Confirm that `neo4j_sync.py` creates the expected nodes and relationships  

---

# 🔍 CI/CD Integration

CI for this module MUST:

- Run `pytest src/pipelines/autonomous/hazards-refresh/tests/`  
- Fail PRs when any test fails  
- Treat `test_dag_smoke.py` as **non-optional**  
- Optionally run these tests as part of a **nightly autonomous suite**  

Additionally, pipeline-wide CI (defined elsewhere) must also include:

- STAC validation  
- Schema validation  
- Lineage + checksum validations  

This README forms part of the CI contract: any removal or substantial modification of tests requires  
governance review and version bump (`version` + `last_updated` in front-matter).

---

# 🕰 Version History

- **v11.0.0 (2025-11-22)** — Initial hazards-refresh tests module for KFM v11.

---

<div align="center">

**Kansas Frontier Matrix — Hazards Refresh Test Suite (v11)**  
*Guardrails · Reliability · Confidence*

</div>

---

### 🔗 Footer  
[⬅ Back to Hazards Pipeline](../README.md) · [🧩 Nodes](../nodes/README.md) · [📦 Resources](../resources/README.md) · [🏛 Governance](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

