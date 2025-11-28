---
title: "🧪 KFM v11.2.2 — Agentic Schema Drift Steward Test Suite (Determinism · Governance · Lineage · Safety)"
path: "docs/pipelines/ai/agentic-schema-drift/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Draft / Experimental"
lifecycle: "Prototype"
review_cycle: "Quarterly · Automated Testing · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Experimental"
doc_kind: "Test Suite Index"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/agentic-schema-drift-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/agentic-schema-drift-v11.2.2.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "AI-Agent-Test-Suite"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "test-suite"
  - "schema-drift-validation"
  - "patch-evaluation-testing"
  - "lineage-testing"
  - "governance-testing"
  - "faircare-testing"
  - "deterministic-ai-testing"

scope:
  domain: "agentic-schema-drift-tests"
  applies_to:
    - "schema-drift-detector-tests"
    - "agent-testing"
    - "patch-evaluation-tests"
    - "stac-dcat-tests"
    - "neo4j-migration-tests"
    - "governance-rule-tests"
    - "telemetry-tests"
    - "lineage-tests"
    - "determinism-tests"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🧪 **Agentic Schema Drift Steward — Automated Test Suite**  
`docs/pipelines/ai/agentic-schema-drift/tests/README.md`

**Purpose:**  
Provide the **governed, deterministic, FAIR+CARE-compliant** test suite for validating the behavior of the KFM v11.2.2 Agentic Schema Drift Steward — including drift detection, patch generation, LangGraph tool use, Prefect durable execution, governance gating, PROV-O lineage, and telemetry correctness.

</div>

---

## 📘 Overview

This directory contains the **entire CI test battery** required for promoting the Schema Drift Steward from *Experimental → Governed* status.

The suite ensures:

- Deterministic outputs (agent stability + reproducibility)  
- Patch safety (no unsafe schema mutations)  
- ETL + STAC + DCAT integrity  
- Neo4j graph migration correctness  
- FAIR+CARE / Sovereignty rule enforcement  
- Telemetry + PROV-O lineage correctness  
- Proper integration with Prefect durable execution  

---

## 🗂️ Directory Layout (v11.2.2)

    docs/pipelines/ai/agentic-schema-drift/tests/
    ├── 📄 README.md                          # This file
    │
    ├── 📄 test_drift_detector.py             # Deterministic schema diffing tests
    ├── 📄 test_patch_generation.py           # Schema Drift Steward patch generation tests
    ├── 📄 test_patch_evaluation.py           # Transform Benchmarker tests
    ├── 📄 test_stac_dcat_validation.py       # STAC/DCAT evolution correctness tests
    ├── 📄 test_graph_migration.py            # Neo4j Cypher migration safety tests
    ├── 📄 test_governance_rules.py           # FAIR+CARE + sovereignty enforcement
    ├── 📄 test_telemetry_bundle.py           # Telemetry v2 (energy/carbon) schema validation
    ├── 📄 test_prov_generation.py            # PROV-O lineage chain validation
    ├── 📄 test_prefect_durable_flow.py       # Prefect durable execution: resume, retries, caching
    ├── 📄 test_langgraph_subgraph.py         # LangGraph DAG determinism + tool routing
    │
    └── 📁 fixtures/                          # Synthetic test data
        ├── 📄 schema_old.json
        ├── 📄 schema_new.json
        ├── 📄 drift_event_minimal.json
        ├── 📄 drift_event_complex.json
        ├── 📄 patch_expected.json
        ├── 📄 lineage_expected.jsonld
        └── 📄 telemetry_expected.json

---

## 🧬 Test Categories

### 1. 🛰 Drift Detector Tests (`test_drift_detector.py`)
Verifies:

- Correct classification of added/removed/renamed/type-changed fields  
- Severity scoring  
- Deterministic diff behavior across repeated runs  
- Compliance with KFM schema diff spec  

---

### 2. 🤖 Agent Patch Generation Tests (`test_patch_generation.py`)
Ensures the Schema Drift Steward:

- Produces valid `TransformPatch` outputs  
- Does not propose unsafe or semantic-breaking mutations  
- Follows FAIR+CARE rules (no leakage of sensitive content)  
- Generates proper STAC/DCAT update instructions  
- Produces stable output across repeated runs  

---

### 3. 🧪 Patch Evaluation Tests (`test_patch_evaluation.py`)
Verifies:

- Data quality metrics  
- Runtime deltas  
- ML feature-impact evaluation  
- Recommendation quality (`accept/reject/manual_review`)  

---

### 4. 🌐 STAC/DCAT Validation Tests (`test_stac_dcat_validation.py`)
Confirms:

- New/updated schema is valid per KFM-STAC v11  
- DCAT JSON-LD structure is correct  
- No breaking changes to dataset metadata  

---

### 5. 🕸 Neo4j Migration Tests (`test_graph_migration.py`)
Checks:

- Cypher generation correctness  
- Non-destructive migrations  
- Idempotent graph evolution  
- No loss of provenance or spatial relationships  

---

### 6. 🛡 Governance Rule Tests (`test_governance_rules.py`)
Ensures:

- CARE masking  
- H3 generalization on spatially sensitive collections  
- Sovereignty rules applied correctly  
- No narrative/speculative fields leaked into patches  

---

### 7. 📡 Telemetry Tests (`test_telemetry_bundle.py`)
Validates:

- Telemetry bundle schema  
- Energy/Carbon v2 fields  
- Prefect + LangGraph run IDs  
- Drift metrics  
- Governance event markers  

---

### 8. 🧾 PROV-O Lineage Tests (`test_prov_generation.py`)
Verifies:

- Entity/Activity/Agent structure  
- Correct linking of before/after schemas  
- Patch-level lineage correctness  
- Compatibility with Story Node v3 + Focus Mode   

---

### 9. 🔁 Prefect Durable Execution Tests (`test_prefect_durable_flow.py`)
Ensures:

- Resume-after-failure works  
- Cached steps behave consistently  
- Task-level retry logic is correct  
- Flow emits governance & telemetry correctly  

---

### 10. 🧭 LangGraph Subgraph Tests (`test_langgraph_subgraph.py`)
Checks:

- Deterministic tool routing  
- Correct fallback behavior  
- No nondeterministic state across runs  
- Structured Pydantic outputs for each tool  

---

## 📦 Fixtures

Fixtures are synthetic, privacy-safe examples for deterministic testing.

Includes:

- Old/new schema snapshots  
- Minimal/complex drift events  
- Expected patches  
- Expected lineage  
- Expected telemetry  

All fixtures must be:

- Deterministic  
- FAIR+CARE safe  
- Sovereignty-safe  
- JSON Schema aligned  

---

## 🧪 CI Enforcement Rules

A PR **cannot merge** unless all tests pass:

- Drift detector correctness  
- Patch stability  
- Governance/CARE compliance  
- STAC/DCAT validation  
- Neo4j safety  
- Telemetry schema correctness  
- Lineage correctness  
- Deterministic LangGraph & Prefect behavior  

These tests guard KFM against unsafe autonomous modifications.

---

## 🕰 Version History

| Version  | Date       | Notes                                                       |
|----------|------------|-------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Full uplift; expanded fixtures + governance tests          |
| v11.0.0  | 2025-11-22 | Initial test suite scaffold                                |

---

<div align="center">

### 🔗 Footer  
[⬅ Agentic Schema Drift Examples](../examples/README.md) · [🤖 Flows](../flows/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

