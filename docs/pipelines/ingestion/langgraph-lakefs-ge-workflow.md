---
title: "🔁 KFM v11.2 — LangGraph + lakeFS + Great Expectations Ingestion Pipeline (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ingestion/langgraph-lakefs-ge-workflow.md"
version: "v11.2.0"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../releases/v11.2.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.0/manifest.zip"
telemetry_ref: "../../../releases/v11.2.0/pipelines-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/langgraph-lakefs-ge-workflow-v11.1.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v4.0"
focus_mode_profile: "Focus Transformer v3.x · Story Node v3.x"

status: "Active · Enforced"
doc_kind: "Pipeline Architecture"
intent: "langgraph-lakefs-ge-ingestion"
category: "FAIR Data Pipelines · Reproducible Ingestion"

fair_category: "F1-A1-I2-R1"
care_label: "CARE-aware · Heritage-capable"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
sensitivity: "Can ingest heritage-adjacent datasets; CARE + sovereignty policies apply at config and promotion boundaries."
risk_category: "Medium"
redaction_required: true

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/pipelines/ingestion/langgraph-lakefs-ge-workflow.md@v11.1.0"
  - "LangGraph ingestion prototypes v10.x"
  - "lakeFS ingest design notes"
  - "Great Expectations policy drafts"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true

json_schema_ref: "../../../schemas/json/langgraph-lakefs-ge-workflow-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/langgraph-lakefs-ge-workflow-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "content-alteration"
  - "governance-override"
  - "narrative-fabrication"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

doc_uuid: "urn:kfm:doc:pipelines:ingestion:langgraph-lakefs-ge:v11.2.0"
semantic_document_id: "kfm-langgraph-lakefs-ge-workflow"
event_source_id: "ledger:docs/pipelines/ingestion/langgraph-lakefs-ge-workflow.md"
immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

classification: "Public Document"
jurisdiction: "Kansas · United States"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next ingestion-architecture update"
---

<div align="center">

# 🔁 **KFM v11.2 — LangGraph + lakeFS + Great Expectations Ingestion Pipeline**  
`docs/pipelines/ingestion/langgraph-lakefs-ge-workflow.md`

[![LangGraph](https://img.shields.io/badge/Orchestrator-LangGraph_v11-1976d2)]()
[![lakeFS](https://img.shields.io/badge/Data_Versioning-lakeFS-6a1b9a)]()
[![Great Expectations](https://img.shields.io/badge/Validation-Great_Expectations-ff9800)]()
[![FAIR](https://img.shields.io/badge/FAIR-Reproducible-brightgreen)]()
[![CARE](https://img.shields.io/badge/CARE-Heritage--Capable-important)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-blue)]()

**Purpose**  
Define a **reference ingestion workflow pattern** for KFM that combines **LangGraph** (stateful DAG runtime), **lakeFS** (branch-based data versioning), and **Great Expectations** (data-quality gates) to realize:

> _Raw fetch → Transform → Validate → lakeFS commit or rollback_  
> with full **PROV-O lineage**, **OpenTelemetry traces**, **STAC/DCAT metadata**, and **Focus Mode / Story Node hooks**.

</div>

---

## 📘 1. High-Level Overview

This pipeline pattern specifies how KFM ingestion pipelines SHOULD:

1. Express orchestration as a **LangGraph DAG**:
   - Nodes = deterministic steps (fetch, transform, validate, register)
   - Edges = explicit success/error flows
   - State = durable and resumable via checkpoints/WAL

2. Use **lakeFS** branches as ingestion sandboxes:
   - Ingest into `ingest/<dataset>/<run_id>` branches  
   - Only validated runs merge into `main` (or other curated branches)

3. Enforce data-quality gates via **Great Expectations**:
   - Expectations = policy-as-code  
   - Results emitted as PROV-O, STAC/DCAT metadata, and OTEL events

4. Emit **full lineage + governance metadata**:
   - lakeFS commits  
   - PROV-O activities & entities  
   - Story Node v3 & Focus Mode v3 overlays  

---

## 🗂️ 2. Directory Layout (v11.2 · Immediate + One Branch)

```text
📁 src/pipelines/ingestion/                     — Ingestion pipelines root
│   📂 langgraph_lakefs_ge/                     — Reference LangGraph + lakeFS + GE workflow implementation
│       📄 README.md                            — (Optional) implementation-level details

📁 docs/pipelines/ingestion/                    — Ingestion documentation root
│   📄 langgraph-lakefs-ge-workflow.md          — This architecture & workflow specification
│   📂 datasets/                                — Dataset-specific ingestion docs (hydrology, archaeology, wildfire, etc.)
```

Deeper structures (nodes, configs, GE suites) are documented in the implementation README or dataset-specific docs.

---

## 🧬 3. Conceptual Pipeline Phases

### 3.1 Phase 0 — Configuration & Dataset Definition

Each ingestion run is defined by a **dataset config** (YAML or JSON):

- `dataset_id` (aligned to STAC Collection ID)  
- Source endpoints (APIs, S3, file drops, etc.)  
- lakeFS repo/branch parameters  

  - `repo`, `base_branch`, `ingest_branch_prefix`  

- Great Expectations suites to run  
- CARE / sovereignty flags (heritage-sensitive / publishable)  
- Focus Mode narrative template choices  

Configurations MUST be versioned and referenced in lineage metadata.

---

### 3.2 Phase 1 — lakeFS Ingest Branch Creation

LangGraph node: `create_ingest_branch`

Responsibilities:

- Compute ingest branch name, e.g. `ingest/<dataset_id>/<run_id>`  
- Create branch from `base_branch` (e.g. `main`)  
- Store `lakefs_branch` in DAG state  
- Emit OTEL span with attributes: repo, base, ingest branch, dataset_id  

Idempotency:

- If ingest branch already exists and is marked `running`, resume.  
- If marked `failed` and policy disallows resume → abort.

---

### 3.3 Phase 2 — Raw Data Fetch

LangGraph node: `fetch_raw_data`

Responsibilities:

- Pull data from upstream systems (HTTP, APIs, cloud storage)  
- Write into `raw/<domain>/<dataset_id>/...` within the ingest branch  
- Capture metadata:

  - Source URIs  
  - Fetch time  
  - Checksums (SHA-256)  

- Emit PROV-O entities for each raw artifact and an activity describing the fetch step.

Idempotency:

- If content + checksum already present → skip, annotate run as reuse of existing raw.

---

### 3.4 Phase 3 — Transform & Harmonize

LangGraph node: `transform_to_curated`

Responsibilities:

- Decode/parse raw data  
- Apply harmonization (CRS, units, naming, vertical datums)  
- Create STAC Items and DCAT distributions  
- Write to `curated/<domain>/<dataset_id>/...`  

Metadata:

- STAC properties (spatial/temporal extent, collection ID)  
- DCAT dataset & distribution references  
- PROV-O links between raw entities and curated outputs  

Failures MUST:

- Indicate which records/files failed  
- Allow partial success when permitted by policy  
- Set flags for validation and gating logic

---

### 3.5 Phase 4 — Validation (Great Expectations)

LangGraph node: `run_ge_validation`

Responsibilities:

- Run one or more GE expectation suites configured for `dataset_id`  
- Persist results under, e.g.:

  - `curated/<domain>/<dataset_id>/_validation/<run_id>/<suite_name>.json`  

- Instrument OTEL spans with:

  - `validation.failed_critical`  
  - `validation.failed_warning`  

Policy:

- Critical expectation failures → `hard_fail = True` (no merge)  
- Warnings can still allow merge but mark run as “elevated risk”  

Summary is stored in state, e.g.:

```json
{
  "total_suites": 3,
  "failed_critical": 0,
  "failed_warning": 2,
  "hard_fail": false
}
```

---

### 3.6 Phase 5 — Gate, Commit & Merge (lakeFS)

LangGraph node: `finalize_ingest_branch`

If `hard_fail`:

- Commit with status `failed_validation`  
- Tag branch as failed  
- Skip merge to `base_branch`  
- Emit incident telemetry  

If validation passes:

- Commit ingest branch with status `validated`  
- Merge ingest branch → `base_branch`  
- Tag commit with dataset and run metadata  
- Update STAC/graph references to point to new curated state  

Rollback policies should be invoked from higher-level tools (e.g. Airflow or CI/CD) when needed.

---

### 3.7 Phase 6 — Registration & Narrative Hooks

LangGraph node: `register_metadata_and_story_node`

Responsibilities:

- Write STAC Collection/Item definitions under `data/stac/<domain>/<dataset_id>/`  
- Export DCAT records (if relevant)  
- Generate a Story Node v3 artifact describing the ingest run:

  - time range  
  - coverage  
  - validation summary  
  - CARE/FAIR flags  

This Story Node can be consumed by Focus Mode for narrative overlays.

---

## 🧠 4. LangGraph DAG Skeleton (Illustrative)

```python
from langgraph.graph import StateGraph, END

def build_ingestion_graph():
    graph = StateGraph(dict)

    graph.add_node("create_branch", create_ingest_branch)
    graph.add_node("fetch_raw", fetch_raw_data)
    graph.add_node("transform", transform_to_curated)
    graph.add_node("validate", run_ge_validation)
    graph.add_node("finalize", finalize_ingest_branch)
    graph.add_node("register", register_metadata_and_story_node)

    graph.set_entry_point("create_branch")

    graph.add_edge("create_branch", "fetch_raw")
    graph.add_edge("fetch_raw", "transform")
    graph.add_edge("transform", "validate")

    def route_after_validation(state: dict) -> str:
        return "finalize" if state["validation"]["hard_fail"] else "register"

    graph.add_conditional_edges(
        "validate",
        route_after_validation,
        {
            "finalize": "finalize",
            "register": "register",
        },
    )

    graph.add_edge("register", "finalize")
    graph.add_edge("finalize", END)

    instrument_graph(graph)  # attach OTEL + energy/carbon
    return graph
```

*Note: This is conceptual; production code is defined in `src/pipelines/ingestion/langgraph_lakefs_ge/`.*

---

## 📊 5. Telemetry, Energy & Carbon

Each run MUST emit:

- **Traces (OTEL)**  
  - One trace per run; spans per node
- **Metrics**  
  - Duration, row counts, error counts
- **Energy/Carbon**  
  - Estimated energy Wh and derived gCO₂e per run, per pipeline

These are aggregated into:

```text
releases/<version>/focus-telemetry.json
```

using the schemas referenced in `telemetry_schema`, `energy_schema`, and `carbon_schema`.

---

## ⚖️ 6. Governance & CARE

This ingestion pattern is subject to:

- KFM Governance Charter (ROOT-GOVERNANCE)  
- Dynamic H3 generalization & CARE screening for heritage datasets  
- Vertical/CRS standards for spatial outputs  

Dataset configs MUST indicate:

- Whether CARE screening is required  
- Whether manual heritage review is required  
- Maximum spatial resolution allowed for public outputs  

Ingestion MUST NOT publish:

- Unscreened heritage-sensitive content  
- Raw sensitive coordinates when generalized views are required  

---

## 🧩 7. Implementation Checklist

1. Define dataset config under `config/pipelines/ingestion/`.  
2. Implement dataset-specific nodes in `langgraph_lakefs_ge/`.  
3. Create GE suites in `config/expectations/<dataset>/`.  
4. Wire DAG using the reference graph pattern.  
5. Instrument with OTEL + energy/carbon metrics.  
6. Register STAC/DCAT + Story Node artifacts.  
7. Document dataset-specific details in `docs/pipelines/ingestion/datasets/<dataset>.md`.  

---

## 🕰️ 8. Version History

| Version  | Date       | Summary                                                                                   |
|---------:|------------|-------------------------------------------------------------------------------------------|
| v11.2.0  | 2025-11-27 | Upgraded to KFM-MDP v11.2.2; added layout, telemetry, FAIR+CARE hooks, and narrative links. |
| v11.1.0  | 2025-11-26 | Initial v11.1 spec for LangGraph + lakeFS + GE ingestion pattern.                         |

---

<div align="center">

**Kansas Frontier Matrix — LangGraph + lakeFS + GE Ingestion**  
*Deterministic · FAIR+CARE-Aligned · Lineage-First*

[⬅ Back to Pipelines Index](../README.md) ·  
[🏗 Repository Architecture](../../../ARCHITECTURE.md) ·  
[⚖ Governance Standards](../../standards/README.md)

</div>
