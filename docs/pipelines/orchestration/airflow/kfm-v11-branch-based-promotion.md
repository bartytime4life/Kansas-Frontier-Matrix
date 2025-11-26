---
title: "🌀 KFM v11.1 — Airflow Branch-Based Promotion DAG (lakeFS + OpenLineage · Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/orchestration/airflow/kfm-v11-branch-based-promotion.md"
version: "v11.1.1"
last_updated: "2025-11-27"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"
sbom_ref: "../../../../releases/v11.1.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.1.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.1.0/pipelines-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/airflow-branch-based-promotion-v11.1.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-gco2e-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
data_contract_ref: "../../../contracts/data-contract-v3.json"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
status: "Active / Enforced"
doc_kind: "Pipeline Architecture"
intent: "airflow-branch-based-promotion-dag"
fair_category: "Pipelines · Orchestration · Lineage"
care_label: "CARE-Aware · No Direct Cultural Content"
---

<div align="center">

# 🌀 KFM v11.1 — Airflow Branch-Based Promotion DAG  
lakeFS Branches · OpenLineage Provenance · Safe Rollback  

`docs/pipelines/orchestration/airflow/kfm-v11-branch-based-promotion.md`  

DAG ID: `kfm_v11_branch_based_promotion` · Runtime: Apache Airflow 2.11.x · lakeFS v1.x · OpenLineage v1.20+  

[Docs – MCP-DL v6.3](../../../../ARCHITECTURE.md) · [Markdown – KFM-MDP v11.2.2](../../../standards/markdown/kfm-mdp-v11.md) · [FAIR+CARE Governance](../../../standards/governance/ROOT-GOVERNANCE.md) · [License: MIT](../../../../LICENSE)

</div>

---

## 1. Purpose and Scope

This document defines the **KFM v11.1 branch-based promotion DAG** implemented in Airflow, using:

- lakeFS for Git-like data versioning and branch-based promotion.  
- OpenLineage for dataset-level and run-level provenance.  
- Deterministic ETL tasks that are idempotent, WAL-aware, and rollback-safe.  

The DAG is the reference pattern for:

- Ingesting and transforming geospatial and heritage-adjacent datasets.  
- Validating them against data contracts and FAIR+CARE checks.  
- Promoting only validated data from a feature branch into the main branch.  
- Providing a controlled rollback path when promotion fails.  

The pattern is generic and can be reused for:

- Hydrology (streamflow, bathymetry, reservoir operations).  
- Terrain and land-cover updates.  
- Archaeology-derived geospatial products (subject to H3 + CARE rules).  
- Climate and hazard layers (wildfire, flood, heat, severe weather).  

---

## 2. Runtime and File Locations

### 2.1 DAG Python File

The canonical Airflow DAG file must live under the orchestration tree:

- `src/pipelines/orchestration/airflow/dags/kfm_v11_branch_based_promotion.py`

That file hosts:

- DAG definition using `openlineage.airflow.DAG` (aliased as `OL_DAG`).  
- Task functions `extract`, `transform`, `validate`.  
- lakeFS operators for branch operations, commit, merge, revert, and cleanup.  

### 2.2 Documentation File

This document is the authoritative reference for the DAG:

- `docs/pipelines/orchestration/airflow/kfm-v11-branch-based-promotion.md` (this file).  

Any behavioral change to the DAG (branch naming, rollback semantics, lineage configuration) must:

1. Update the DAG file.  
2. Update this document.  
3. Bump `version` and `previous_version_hash` in the front-matter.  
4. Pass v11.2.2 documentation checks in CI.  

---

## 3. High-Level Flow

### 3.1 Conceptual Steps

1. Create feature branch from `main`.  
2. Copy or materialize inputs (for example raw ingest) into the feature branch.  
3. Run ETL tasks (`extract` → `transform` → `validate`).  
4. Commit processed state on the feature branch.  
5. Merge the validated commit into `main`.  
6. Rollback `main` if merge or post-merge checks fail.  
7. Delete feature branch in all cases (success or failure).  

### 3.2 DAG Topology (Logical)

Logical task sequence:

- `create_feature_branch`  
- `copy_ingest_data`  
- `extract` (@task)  
- `transform` (@task)  
- `validate` (@task)  
- `commit_feature_branch`  
- `merge_to_main`  
- `rollback_main` (triggered only on failure)  
- `delete_feature_branch` (triggered on `all_done`)  

The DAG is non-scheduled (`schedule_interval=None`) and is intended for:

- Event-based triggers (webhooks, Git pushes, upstream stage completion).  
- Manual runs from Airflow or CLI for controlled promotions.  

---

## 4. lakeFS Branching Model

### 4.1 Branch Naming

- Repository: `kfm-datalake`.  
- Mainline branch: `main`.  
- Feature branch pattern: `feature/ingest-<domain>`.  
  - Example: `feature/ingest-geodata`.  

Branch naming must:

- Be deterministic and discoverable from run context (for example Airflow run ID, dataset ID).  
- Avoid collisions across concurrent runs (optional suffix by date or run UUID).  

Example pattern:

- `feature/ingest-geodata-{{ ds_nodash }}-{{ run_id }}`  

### 4.2 Paths

Typical path mapping in the DAG:

- `incoming/geodata/raw/` → raw ingest.  
- `curated/geodata/` → derived and validated outputs.  

Domain-specific DAGs should maintain:

- A clear distinction between `incoming/` and `curated/`.  
- Consistent naming across STAC/DCAT metadata and contracts.  

### 4.3 Commit and Merge Semantics

- `LakeFSCommitOperator` creates a commit on the feature branch after ETL and validation.  
- `LakeFSMergeOperator` merges that commit into `main` with a promotion message.  
- `LakeFSRevertOperator` can revert `main` to the previous commit if a failure occurs.  

Key guarantees:

- Promotion is atomic at the branch level.  
- If post-merge checks fail, `rollback_main` reverts the last commit on `main`.  
- No direct writes to `main` outside merges from controlled feature branches.  

---

## 5. OpenLineage and Provenance

This DAG uses `openlineage.airflow.DAG` (aliased as `OL_DAG`) to:

- Emit job and run metadata for each task.  
- Attach input and output datasets for ETL tasks and lakeFS operators.  
- Record namespace, job name, and run ID consistently.  

### 5.1 Dataset Modeling

Each logical dataset should map to an OpenLineage dataset with:

- `namespace`: KFM-wide URI (for example `kfm://lakefs/kfm-datalake`).  
- `name`: lakeFS path plus branch (for example `kfm-datalake/main/curated/geodata/`).  

Additional facets:

- STAC / DCAT reference IDs.  
- JSON-LD context for heritage or geo semantics.  
- PROV-O entities and activities.  

### 5.2 Minimum Required Facets per Run

At minimum, each DAG run must emit:

- **Run facet**:

  - KFM pipeline ID.  
  - Git commit reference of the DAG file.  
  - Configuration hash (for example ETL YAML or JSON configuration).  

- **Job facet**:

  - Domain (`hydrology`, `terrain`, `archaeology`, etc.).  
  - Data contract reference (same as `data_contract_ref` in this document).  

- **Dataset facets**:

  - STAC Item and Collection IDs for sources and targets.  
  - CARE labels when heritage or Indigenous data is involved.  
  - FAIR maturity hints (for example findable index flag).  

---

## 6. Reliability and Rollback Semantics

This DAG follows KFM v11.1 reliability standards and aligns with:

- `docs/pipelines/reliability/slo-error-budgets.md`  
- `docs/pipelines/release/runbooks/rollback-runbook.md`  

### 6.1 Idempotency and WAL

ETL tasks (`extract`, `transform`, `validate`) must be:

- Pure or idempotent with respect to inputs.  
- Backed by WAL-style checkpoints in lakeFS or object storage.  

Re-running the DAG for the same logical input should produce:

- The same outputs (or a controlled overwrite with a new commit).  
- A consistent provenance trail in OpenLineage and PROV-O.  

### 6.2 Retry and Failure Handling

- Default retries: `retries=3`, `retry_delay=10 minutes` (tunable).  
- `merge_to_main` is a critical reliability boundary:

  - On merge failure, `rollback_main` is triggered with `trigger_rule="one_failed"`.  
  - `rollback_main` must be treated as a safety net, not part of the normal success path.  

### 6.3 SLO Hooks

DAG-level SLO hooks (shared utilities) should:

- Emit:

  - Success and failure counts.  
  - End-to-end latency distributions.  
  - Promotion versus rollback ratio.  

- Feed:

  - Reliability dashboards.  
  - Error budget and SLO policy enforcement.  
  - Auto-pause or kill-switch behavior when SLOs are violated.  

---

## 7. Directory Layout

Reference layout for Airflow orchestration and this DAG:

```text
docs/
  pipelines/
    orchestration/
      airflow/
        kfm-v11-branch-based-promotion.md   # This file (architecture + runbook)

src/
  pipelines/
    orchestration/
      airflow/
        dags/
          kfm_v11_branch_based_promotion.py # DAG definition
        utils/
          lineage.py                         # OpenLineage helpers (dataset facets, STAC/DCAT)
          lakefs.py                          # lakeFS helpers (branch naming, repo config)

releases/
  v11.1.0/
    sbom.spdx.json
    manifest.zip

schemas/
  telemetry/
    airflow-branch-based-promotion-v11.1.json
    energy-v2.json
    carbon-gco2e-v1.json
```

This layout is normative for DAGs following the branch-based promotion pattern.

---

## 8. Configuration and Parameters

### 8.1 Required Configuration Keys

Supplied via Airflow Variables, Connections, or environment variables:

- `KFM_LAKEFS_REPO` (default `kfm-datalake`).  
- `KFM_LAKEFS_MAIN_BRANCH` (default `main`).  
- `KFM_LAKEFS_FEATURE_BRANCH_TEMPLATE`.  
- `KFM_LINEAGE_NAMESPACE`.  
- `KFM_DOMAIN` (for example `hydrology`, `terrain`, `archaeology`).  

### 8.2 Optional Parameters

- `KFM_ALLOW_AUTOMERGE`:

  - If disabled, merge to `main` is gated by a human approval stage.  

- `KFM_RUN_MODE`:

  - `dry-run`: execute ETL and validation but skip commit and merge.  
  - `promote`: perform full commit and merge sequence.  

- `KFM_ENERGY_TELEMETRY_ENABLED`:

  - Enables energy and carbon reporting for this DAG.  

---

## 9. Story Node and Focus Mode Integration

This DAG contributes to KFM’s narrative system by:

- Producing traceable dataset updates that can be referenced in Story Nodes.  
- Enabling Focus Mode v3 to surface dataset promotion events as part of context.  

### 9.1 Story Node Metadata Hooks

Each successful promotion may create or update a Story Node describing:

- Dataset identity and domain.  
- Promotion commit ID and time.  
- If applicable, subsequent rollback events.  
- Downstream impact regions (for example which reservoirs or basins).  

Metadata hooks are typically implemented in shared helpers:

- `src/pipelines/orchestration/airflow/utils/lineage.py`  

When story linkage is enabled, the DAG should add a final task to publish or update Story Node metadata in the graph.

---

## 10. Governance, Ethics, and CARE Alignment

### 10.1 FAIR+CARE

The DAG must:

- Respect data contracts that encode:

  - Coordinate generalization rules (for example H3).  
  - Masking requirements for sensitive sites.  
  - CARE labels and restrictions for cultural or Indigenous data.  

- Emit CARE-related facets when:

  - Source datasets include heritage or Indigenous content.  
  - Derived products represent cultural or sacred landscapes.  

### 10.2 Approvals and Change Control

Structural changes to this DAG require:

- Reliability Working Group review.  
- FAIR+CARE Council sign-off for heritage-relevant flows.  

Any change that weakens rollback or promotion guarantees must be accompanied by:

- Updates to the rollback runbook.  
- SLO and error-budget impact analysis.  

---

## 11. Version History

| Version | Date       | Summary                                                                                                   |
|--------:|------------|-----------------------------------------------------------------------------------------------------------|
| v11.1.1 | 2025-11-27 | Upgraded to KFM-MDP v11.2.2 format; normalized header, badges, and clarified CI documentation expectations. |
| v11.1.0 | 2025-11-26 | Initial v11.1 DAG documentation; defined lakeFS + OpenLineage pattern and Story Node / Focus integration. |

---

<div align="center">

[Back to Repository Architecture](../../../../ARCHITECTURE.md) · [Pipelines and Reliability Index](../../README.md) · [Standards and Governance Index](../../../standards/README.md)

</div>