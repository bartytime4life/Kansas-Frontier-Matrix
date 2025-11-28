---
title: "🤖 KFM v11.2.2 — Agentic Schema Drift Steward (Implementation Layer · Pydantic AI + Prefect + LangGraph)"
path: "docs/pipelines/ai/agentic-schema-drift/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Draft / Experimental"
lifecycle: "Prototype"
review_cycle: "Quarterly · Autonomous Systems · FAIR+CARE Council"
content_stability: "experimental"

status: "Active / Experimental"
doc_kind: "Implementation Guide"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/agentic-schema-drift-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/agentic-schema-drift-v11.2.2.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

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
sensitivity: "AI-Agentic-System"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "schema-drift"
  - "agentic-etl"
  - "durable-execution"
  - "pydantic-ai"
  - "prefect"
  - "langgraph"
  - "governed-ai"
  - "self-healing-pipelines"

scope:
  domain: "agentic-schema-drift"
  applies_to:
    - "schema-drift-detector"
    - "steward-agent"
    - "transform-benchmarker"
    - "prefect-flows"
    - "langgraph-subgraphs"
    - "stac-dcat-updaters"
    - "neo4j-migration-tools"
    - "governance-ledger-writers"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
---

<div align="center">

# 🤖 **Agentic Schema Drift Steward — Implementation Layer**  
`docs/pipelines/ai/agentic-schema-drift/README.md`

**Purpose:**  
Provide the **implementation-level specification** for the KFM v11.2.2 Schema Drift Steward:  
a hybrid **Pydantic-AI + LangGraph + Prefect (durable execution)** system that detects schema drift, proposes safe migration patches, validates them in shadow environments, and promotes changes under strict **FAIR+CARE**, **governance**, and **lineage** constraints.

</div>

---

## 📘 Overview

This directory contains:

- All **runtime code** for the Schema Drift Steward  
- Deterministic drift detectors  
- Pydantic AI agents (typed LLM tools)  
- Prefect flows for durable execution  
- LangGraph subgraphs for multi-tool orchestration  
- Tests, governance hooks, telemetry emitters  

This is the operational counterpart to the architecture document:

```
docs/pipelines/ai/agentic-schema-drift-durable-execution.md
```

---

## 🗂️ Directory Layout (v11.2.2)

    docs/pipelines/ai/agentic-schema-drift/
    ├── 📄 README.md                              # This file (implementation guide)
    │
    ├── 📁 src/                                   # Core implementation modules
    │   ├── 📜 steward_agent.py                   # Primary Pydantic AI Schema Drift Steward
    │   ├── 📜 transform_benchmarker.py           # Benchmarking agent for patch options
    │   ├── 📜 schema_diff_detector.py            # Deterministic drift detector
    │   ├── 📜 stac_updater.py                    # STAC schema evolution tool
    │   ├── 📜 dcat_updater.py                    # DCAT / JSON-LD metadata updater
    │   ├── 📜 graph_migration.py                 # Neo4j Cypher migration generator
    │   └── 📜 governance_hooks.py                # FAIR+CARE, sovereignty, policy enforcement
    │
    ├── 📁 flows/                                 # Orchestration layer
    │   ├── 📜 prefect_schema_drift_flow.py       # Durable Prefect flow
    │   └── 📜 langgraph_subgraph.py              # LangGraph DAG for agent reasoning
    │
    ├── 📁 examples/                              # Example events, patches, traces
    │   ├── 📄 schema_drift_event_sample.json
    │   ├── 📄 transform_patch_sample.json
    │   └── 📄 patch_evaluation_sample.json
    │
    ├── 📁 tests/                                 # CI test suites
    │   ├── 📄 test_drift_detector.py
    │   ├── 📄 test_patch_evaluation.py
    │   ├── 📄 test_prov_generation.py
    │   └── 📄 test_governance_rules.py
    │
    └── 📁 telemetry/                             # Telemetry + lineage artifacts
        ├── 📄 telemetry-schema.json
        ├── 📄 telemetry-sample.json
        └── 📄 lineage-facets.json

---

## 🧩 Core Components

### 1. 🛰️ Schema Drift Detector (Deterministic)
Responsible for:

- Comparing baseline schemas with current snapshots  
- Producing `SchemaDriftEvent` objects  
- Severity scoring  
- No AI use → purely deterministic  

Supports:

- STAC metadata  
- DCAT datasets  
- Neo4j labels/relationships  
- KDW/tabular schemas  
- NetCDF/GRIB metadata  

---

### 2. 🤖 Schema Drift Steward Agent (Pydantic AI)
Responsibilities:

- Classify drift  
- Propose ETL transform patches  
- Propose STAC/DCAT schema updates  
- Propose Neo4j migration plans  
- Produce structured `TransformPatch` object  
- Emit FAIR+CARE notes & risk flags  

Wrapped in:

- **LangGraph subgraph** for tool routing  
- **Prefect durable execution** for reliability  

---

### 3. 🧪 Transform Benchmarker
Evaluates alternative patches:

- Data quality impact  
- ML model impact (weather, hydro, hazard pipelines)  
- Runtime/cost delta  
- Provides an `PatchEvaluation` object  

Used for decision making and ranking.

---

### 4. 🧱 Governance Hooks
Guarantees:

- CARE masking  
- H3 generalization (for sensitive spatial assets)  
- Sovereignty policy enforcement  
- Preventing unsafe auto-promotion  
- Writing governance entries to:
  - Governance Ledger  
  - Telemetry Bundle  
  - Lineage Graph (PROV-O)  

---

### 5. ⚙️ Prefect Durable Flow
Implements:

- Retry logic  
- Durable state resume  
- Shadow environment application  
- Test suite execution  
- Promotion gatekeeping  
- Telemetry emission  

This is the **outer execution engine**.

---

### 6. 🧬 LangGraph Subgraph
Implements the **inner agent execution**, including:

- Tools: STAC validator, DCAT validator, Cypher generator  
- Memory-safe DAG  
- Deterministic ordering  
- Reliable tool routing  

---

## 🔧 Minimal Usage Example

### Trigger manually:

```python
from steward_agent import schema_drift_steward
from models import SchemaDriftEvent

event = SchemaDriftEvent(...)        # constructed by detector
patch = schema_drift_steward.run(event)
```

### Trigger via Prefect flow:

```python
from flows.prefect_schema_drift_flow import kfm_schema_drift_steward_flow

kfm_schema_drift_steward_flow(event)
```

Prefect resumes if an AI/tool step fails.

---

## 📡 Telemetry & Lineage Outputs

Each drift-handling execution emits:

- Telemetry bundle (`agentic-schema-drift-telemetry.json`)  
- OpenLineage spans  
- PROV-O JSON-LD bundles  
- CARE-scope metadata  
- Energy & carbon usage  
- Governance references  

These integrate with:

- KFM validation dashboards  
- Focus Mode v3 narrative overlays  
- Story Node v3 “schema evolution” entries  

---

## 🧪 Testing Requirements

All components must pass:

- Drift detection correctness  
- Patch validation (semantic + regression tests)  
- Governance checks (CARE, sovereignty)  
- STAC + DCAT schema validation  
- Neo4j migration safety tests  
- Telemetry schema validation  
- Replay determinism tests  

PRs failing any → **blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                      |
|----------|------------|------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Full implementation-layer uplift, new governance hooks     |
| v11.0.0  | 2025-11-22 | Initial directory + early prototypes                       |

---

<div align="center">

### 🔗 Footer  
[⬅ Pipelines & AI Index](../README.md) · [🤖 Architecture Guide](../agentic-schema-drift-durable-execution.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

