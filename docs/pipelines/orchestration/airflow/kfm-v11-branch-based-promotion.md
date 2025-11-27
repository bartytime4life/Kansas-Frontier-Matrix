---
title: "🌀 KFM v11.1 — Airflow Branch-Based Promotion DAG (lakeFS + OpenLineage · Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/orchestration/airflow/kfm-v11-branch-based-promotion.md"
version: "v11.2.0"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../releases/v11.2.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.0/pipelines-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/airflow-branch-based-promotion-v11.1.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../contracts/data-contract-v3.json"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Pipeline Architecture"
intent: "airflow-branch-based-promotion-dag"
category: "Pipelines · Orchestration · Lineage"

fair_category: "F1-A1-I2-R1"
care_label: "CARE-Aware · No Direct Cultural Content"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "PROV-O"
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "FAIR+CARE"

provenance_chain:
  - "docs/pipelines/orchestration/airflow/kfm-v11-branch-based-promotion.md@v11.1.1"
  - "docs/pipelines/orchestration/airflow/kfm-v11-branch-based-promotion.md@v11.1.0"
  - "docs/pipelines/orchestration/airflow/README.md@v11.0.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

json_schema_ref: "../../../../schemas/json/airflow-index-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/airflow-index-v11-shape.ttl"

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
requires_directory_layout_section: false
requires_version_history: true
requires_governance_links_in_footer: true

doc_uuid: "urn:kfm:doc:pipelines:orchestration:airflow:branch-based-promotion:v11.2.0"
semantic_document_id: "kfm-airflow-branch-based-promotion"
event_source_id: "ledger:docs/pipelines/orchestration/airflow/kfm-v11-branch-based-promotion.md"
immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

jurisdiction: "Kansas · United States"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon orchestration-platform-v12"
---

<div align="center">

# 🌀 **KFM v11.1 — Airflow Branch-Based Promotion DAG**  
lakeFS Branches · OpenLineage Provenance · Safe Rollback  

`docs/pipelines/orchestration/airflow/kfm-v11-branch-based-promotion.md`  

DAG ID: `kfm_v11_branch_based_promotion` · Runtime: Apache Airflow 2.11.x · lakeFS v1.x · OpenLineage v1.20+  

[📚 CI/CD Architecture](../../../../.github/ARCHITECTURE.md) ·  
[📝 Markdown — KFM-MDP v11.2.2](../../../standards/kfm_markdown_protocol_v11.2.2.md) ·  
[⚖ FAIR+CARE Governance](../../../standards/governance/ROOT-GOVERNANCE.md) ·  
[📜 License: MIT](../../../../LICENSE)

</div>

---

## 📘 1. Purpose & Scope

This document defines the **KFM v11.1 branch-based promotion DAG** implemented in Airflow, using:

- **lakeFS** for Git-like data versioning and branch-based promotion.  
- **OpenLineage** for dataset-level and run-level provenance.  
- **Deterministic, idempotent ETL tasks** that are WAL-aware and rollback-safe.  

The DAG is the **reference pattern** for:

- Ingesting and transforming geospatial, environmental, and heritage-adjacent datasets.  
- Validating against **Data Contracts v3**, FAIR+CARE rules, and sovereignty constraints.  
- Promoting only validated data from a **feature branch** into the **`main`** branch.  
- Providing a controlled rollback path when promotion fails.  

It is reusable for:

- Hydrology (streamflow, bathymetry, reservoir operations)  
- Terrain and land-cover updates  
- Archaeology-derived geospatial products (subject to H3 + CARE rules)  
- Climate and hazard layers (wildfire, flood, heat, severe weather)  

---

## 🧭 2. Runtime & Locations

### 2.1 DAG Python File

The canonical DAG lives under the orchestration tree:

```text
src/pipelines/orchestration/airflow/dags/kfm_v11_branch_based_promotion.py
```

This file contains:

- DAG definition using `openlineage.airflow.DAG` (often aliased as `OL_DAG`)  
- Core tasks: `create_feature_branch`, `copy_ingest_data`, `extract`, `transform`, `validate`, `commit`, `merge`, `rollback`, `cleanup`  
- lakeFS operators for branch operations, commit, merge, revert, cleanup  

### 2.2 Documentation File

This document is the **authoritative reference** for the DAG:

```text
docs/pipelines/orchestration/airflow/kfm-v11-branch-based-promotion.md
```

Any behavioral change MUST:

1. Update the DAG file.  
2. Update this document.  
3. Bump `version` + `previous_version_hash`.  
4. Pass KFM-MDP v11.2.2 documentation checks in CI.  

---

## 🔁 3. High-Level Flow

### 3.1 Conceptual Steps

1. Create feature branch from `main`.  
2. Copy or materialize inputs (raw ingest) onto the feature branch.  
3. Run ETL tasks: `extract` → `transform` → `validate`.  
4. Commit processed state to the feature branch.  
5. Merge the validated commit into `main`.  
6. Run post-merge checks (contract + governance).  
7. Rollback `main` if post-merge checks fail.  
8. Delete feature branch (success or failure).  

### 3.2 Logical DAG Topology

Tasks (simplified):

- `create_feature_branch`  
- `copy_ingest_data`  
- `extract` (@task)  
- `transform` (@task)  
- `validate` (@task)  
- `commit_feature_branch`  
- `merge_to_main`  
- `post_merge_checks`  
- `rollback_main` (triggered `one_failed`)  
- `delete_feature_branch` (`all_done`)  

The DAG is typically **manually or event-triggered** (`schedule_interval=None`), used for:

- Controlled promotions after staging validation  
- Domain-specific release flows (geology, hydrology, atmospheric, etc.)

---

## 🌿 4. lakeFS Branching Model

### 4.1 Branch Naming

- Repository: `kfm-datalake`  
- Mainline: `main`  
- Feature branch pattern: `feature/ingest-<domain>-<timestamp>-<run_id>`  
  - Example: `feature/ingest-hydrology-20251127-abcdef`  

Branch naming MUST:

- Be derivable from Airflow run context  
- Avoid collisions across concurrent runs  

### 4.2 Path Conventions

Examples:

- `incoming/<domain>/raw/` → raw ingest
- `curated/<domain>/` → validated outputs

Domain DAGs SHOULD maintain clear separation between `incoming/` vs `curated/` and ensure:

- Paths align with STAC/DCAT metadata  
- Paths align with Data Contract v3 schemas  

### 4.3 Commit & Merge Semantics

- `LakeFSCommitOperator` records a commit on the feature branch after `validate`.  
- `LakeFSMergeOperator` merges that commit into `main` with structured metadata.  
- `LakeFSRevertOperator` rolls back `main` if post-merge checks fail.  

Guarantees:

- Promotions are **atomic** at the branch level.  
- `main` is modified only via merges from controlled feature branches.  

---

## 🛰️ 5. OpenLineage Provenance Pattern

The DAG MUST:

- Use `openlineage.airflow.DAG` or equivalent integration  
- Emit run-level OpenLineage events for:

  - DAG run start/complete/fail  
  - Task-level lineage (input/output datasets)  

### 5.1 Dataset Modeling

For each dataset:

- `namespace`: `kfm://lakefs/kfm-datalake`  
- `name`: e.g. `kfm-datalake/main/curated/hydrology/streamflow/`  

Facets SHOULD include:

- STAC Collection & Item IDs  
- DCAT dataset ID  
- CARE labels when relevant  
- FAIR maturity annotations  

### 5.2 Required Facets per Run

Each run MUST emit:

- **Run facet**: DAG version, git commit of DAG file, config hash  
- **Job facet**: domain, KFM pipeline ID, data contract reference  
- **Dataset facets**: sources, targets, and their CARE/FAIR metadata  

---

## 🧱 6. Reliability & Rollback Semantics

This DAG adheres to KFM’s **Reliable Pipelines v11** guidelines:

- Idempotent ETL operations  
- WAL-backed intermediate states (as appropriate)  
- Configurable retries on transient failures  
- Strict boundaries at commit/merge steps  

### 6.1 WAL & Idempotency

ETL tasks MUST:

- Use WAL or checkpoint markers as needed  
- Make re-runs safe with respect to:

  - Idempotent writes  
  - No duplication of derived data  
  - Reproducible outputs for given inputs  

### 6.2 Rollback Behavior

If `merge_to_main` or `post_merge_checks` fail:

- `rollback_main` MUST revert `main` to the previous stable commit  
- Rollback MUST be recorded in OpenLineage and PROV-O lineage models  
- A governance record should capture:

  - Reasons for rollback  
  - SLO and error-budget impact  

---

## 🧂 7. Governance, FAIR+CARE, and Data Contracts

The DAG MUST respect:

- Data contract specified in `data_contract_ref`  
- FAIR+CARE guidelines for all datasets  
- Sovereignty policies when dealing with heritage layers  

### 7.1 Governance Integration

Before promotion:

- Data contracts MUST validate (schema, types, allowed ranges)  
- CARE labels MUST be present when needed  
- Sensitive coordinates MUST be properly generalized (H3 or equivalent)  

Promotion MUST NOT:

- Introduce unreviewed sensitive heritage data into curated branches  
- Violate licensing terms or dataset sharing policies  

---

## 🧬 8. Story Nodes, Focus Mode & Narrative Hooks

This DAG supports narrative-level constructs by:

- Producing promotion events that can be surfaced in Story Nodes v3  
- Providing Focus Mode with:

  - Dataset update timing  
  - Affected regions  
  - Up/downstream chains (e.g. reservoir or basin)  

Implementations MAY add a final task to:

- Push “promotion event” metadata into the graph  
- Tag related Story Nodes with:

  - `last_promotion_time`  
  - `promoted_branch`  
  - `rollback_state` (if any)  

---

## 🕰️ 9. Version History

| Version  | Date       | Summary                                                                                             |
|---------:|------------|-----------------------------------------------------------------------------------------------------|
| v11.2.0  | 2025-11-27 | Upgraded to KFM-MDP v11.2.2; added governance/telemetry metadata, OTEL/OpenLineage alignment, and layout normalization. |
| v11.1.1  | 2025-11-27 | Refined docs, clarified rollback semantics & documentation update rules.                           |
| v11.1.0  | 2025-11-26 | Initial v11.1 DAG documentation; defined basic lakeFS + OpenLineage branch-based promotion pattern. |

---

<div align="center">

[⬅ Back to Airflow Orchestration Index](README.md) ·  
[📘 Pipelines Overview](../../README.md) ·  
[⚖ Governance Standards](../../../standards/README.md)

</div>
