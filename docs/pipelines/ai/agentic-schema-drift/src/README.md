---
title: "🤖 KFM v11.2.2 — Agentic Schema Drift Steward: Source Modules (Pydantic AI · LangGraph · Governance Hooks)"
path: "docs/pipelines/ai/agentic-schema-drift/src/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Draft / Experimental"
lifecycle: "Prototype"
review_cycle: "Quarterly · Autonomous Systems · FAIR+CARE Council"
content_stability: "experimental"

status: "Active / Experimental"
doc_kind: "Source Code Index"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
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
sensitivity: "AI-Agent-Orchestration"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "schema-drift"
  - "agentic-etl"
  - "pydantic-ai"
  - "langgraph-dag"
  - "validation-tools"
  - "stac-updaters"
  - "dcat-updaters"
  - "graph-migration"
  - "faircare-governance"

scope:
  domain: "agentic-schema-drift-src"
  applies_to:
    - "deterministic-drift-detection"
    - "steward-agent"
    - "benchmarker-agent"
    - "stac-dcat-evolution"
    - "neo4j-migration"
    - "governance-hooks"
    - "telemetry-emitters"
    - "prov-generation"
    - "prefect-tooling"
    - "langgraph-subgraphs"

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

# 🤖 **Agentic Schema Drift Steward — Source Modules**  
`docs/pipelines/ai/agentic-schema-drift/src/README.md`

**Purpose:**  
Document all **runtime modules** that implement the KFM v11.2.2 Agentic Schema Drift Steward:  
a Pydantic-AI + LangGraph + Prefect system for detecting schema drift, proposing safe migration patches, validating them, and promoting them under strict governance and lineage controls.

</div>

---

## 📘 Overview

This directory contains the **core execution modules** for:

- Deterministic schema drift detection  
- Pydantic AI agents (Schema Drift Steward + Transform Benchmarker)  
- LangGraph subgraphs (tool routing, multi-step reasoning)  
- STAC/DCAT metadata evolution tools  
- Neo4j schema migration logic  
- Governance enforcement (FAIR+CARE, sovereignty)  
- Telemetry + PROV-O lineage emitters  

These modules are imported by:

```
docs/pipelines/ai/agentic-schema-drift/flows/
```

which provide durable Prefect flow orchestration.

---

## 🗂️ Directory Layout (v11.2.2)

    docs/pipelines/ai/agentic-schema-drift/src/
    ├── 📄 README.md                                     # This file
    │
    ├── 📜 steward_agent.py                              # Core Pydantic-AI Schema Drift Steward
    ├── 📜 transform_benchmarker.py                      # Patch ranking & evaluation agent
    ├── 📜 schema_diff_detector.py                       # Deterministic drift detector
    ├── 📜 stac_updater.py                               # STAC schema evolution utilities
    ├── 📜 dcat_updater.py                               # DCAT metadata updater (JSON-LD)
    ├── 📜 graph_migration.py                            # Neo4j Cypher generation for schema updates
    ├── 📜 governance_hooks.py                           # FAIR+CARE + sovereignty rules
    ├── 📜 telemetry_emitters.py                         # Telemetry + energy/carbon emitters
    ├── 📜 prov_generator.py                             # PROV-O lineage builder
    └── 📜 utils.py                                      # Shared helpers (hashing, diffing, config loading)

---

## 🧬 Module Descriptions

### 1. 🛰️ `steward_agent.py`
Implements the **Schema Drift Steward Agent**:

- Pydantic AI model with typed input/output  
- Drift classification (cosmetic, structural, semantic)  
- ETL patch proposal  
- STAC/DCAT evolution plan generation  
- Neo4j migration proposals  
- FAIR+CARE safety notes & risk levels  

Integrated into LangGraph for tool orchestration.

---

### 2. 🧪 `transform_benchmarker.py`
Evaluates alternative patch strategies:

- Data-quality impact  
- ML model impact (if drift affects downstream pipelines)  
- Runtime/cost profiles  
- Produces a structured `PatchEvaluation` result  

Used by governance to decide whether changes may auto-apply.

---

### 3. 🧭 `schema_diff_detector.py`
Deterministic, non-AI drift detector:

- Diffs old vs new schemas  
- Identifies added, removed, renamed, type-changed fields  
- Computes `SchemaDriftEvent` severity  
- Supports:
  - STAC items  
  - DCAT datasets  
  - Neo4j constraints  
  - Tabular schemas  
  - Raster/NetCDF metadata  

---

### 4. 🌐 `stac_updater.py`  
Automates STAC schema updates:

- Adds/removes/renames STAC properties  
- Ensures KFM-STAC v11 compliance  
- Recomputes multihash checksums  
- Writes patch manifests  

---

### 5. 📘 `dcat_updater.py`  
Updates DCAT dataset metadata:

- JSON-LD evolution (new fields, updated descriptions)  
- Rewrites distribution metadata  
- Keeps CARE + license metadata aligned  

---

### 6. 🕸️ `graph_migration.py`
Generates Neo4j migrations:

- Node label evolution  
- Relationship type changes  
- Property renames and type adjustments  
- Cypher patches for safe rollout  
- PREVIEW-MODE for shadow environment testing  

---

### 7. 🛡️ `governance_hooks.py`
Enforces KFM governance & CARE rules:

- H3 generalization for sensitive spatial data  
- Sovereignty policy validation  
- CARE scope injection  
- Rejects unsafe or culturally inappropriate schema changes  
- Logs all governance decisions  

---

### 8. 📡 `telemetry_emitters.py`
Emits telemetry for each drift cycle:

- Schema drift metrics  
- Patch choice & evaluation metrics  
- Prefect flow/task IDs  
- Energy/Carbon v2 usage  
- OpenLineage facets  

---

### 9. 🧾 `prov_generator.py`
Builds PROV-O JSON-LD artifacts:

- `prov:Entity` for old/new schemas  
- `prov:Activity` for drift processing  
- `prov:Agent` for human + software actors  
- Outputs lineage for Focus Mode v3 + Story Node v3  

---

### 10. 🔧 `utils.py`
Shared helpers:

- Stable hashing  
- Type normalization  
- Diff utilities  
- Config loading  
- Safe filesystem + lakeFS access  

---

## 🔧 Minimal Usage Example (from Prefect Flow)

```python
from steward_agent import schema_drift_steward
from schema_diff_detector import detect_schema_drift

event = detect_schema_drift(...)
patch = schema_drift_steward.run(event)
```

Used inside:

```
docs/pipelines/ai/agentic-schema-drift/flows/prefect_schema_drift_flow.py
```

---

## 📡 Integration Targets

Modules here feed:

- Prefect durable flow  
- LangGraph agent DAG  
- STAC/DCAT metadata generators  
- Neo4j migrations  
- Governance ledger  
- Focus Mode v3 narrative overlays  
- Story Node v3 “schema evolution” entries  

---

## 🧪 Testing Requirements

CI tests must verify:

- Drift detection correctness  
- Patch generation stability  
- FAIR+CARE rule enforcement  
- STAC/DCAT schema validation  
- Neo4j migration safety  
- PROV generation correctness  
- Telemetry schema compliance  

---

## 🕰 Version History

| Version  | Date       | Notes                                                   |
|----------|------------|---------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Full implementation uplift, governance hooks, telemetry |
| v11.0.0  | 2025-11-22 | Initial source layer scaffold                            |

---

<div align="center">

### 🔗 Footer  
[⬅ Agentic Schema Drift Index](../README.md) · [🤖 Architecture Guide](../../agentic-schema-drift-durable-execution.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

