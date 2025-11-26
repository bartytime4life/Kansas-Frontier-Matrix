---
title: "🌀 Kansas Frontier Matrix — Airflow Orchestration Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/orchestration/airflow/README.md"
version: "v11.0.0"
last_updated: "2025-11-27"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/pipelines-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/airflow-index-v11.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
data_contract_ref: "../../../contracts/data-contract-v3.json"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
status: "Active / Enforced"
doc_kind: "Pipeline Architecture"
intent: "airflow-orchestration-index"
fair_category: "F1-A1-I2-R1"
care_label: "CARE-Aware · Low-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
risk_category: "Low"
indigenous_rights_flag: false
redaction_required: false
data_steward: "KFM FAIR+CARE Council"
provenance_chain:
  - "docs/pipelines/orchestration/airflow/README.md@v10.4.0"
  - "docs/pipelines/orchestration/airflow/README.md@v10.4.1"
  - "docs/pipelines/orchestration/airflow/README.md@v11.0.0"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "N/A"
json_schema_ref: "../../../../schemas/json/airflow-index-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/airflow-index-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:pipelines:orchestration:airflow:index:v11.0.0"
semantic_document_id: "kfm-airflow-orchestration-index"
event_source_id: "ledger:docs/pipelines/orchestration/airflow/README.md"
immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas · United States"
classification: "Public Document"
role: "pipeline-architecture"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon orchestration-platform-v12"
---

# 🌀 Kansas Frontier Matrix — Airflow Orchestration Index (v11)

This document provides the governed index of **Airflow-based orchestration pipelines** in the Kansas Frontier Matrix (KFM). It defines the Airflow-specific orchestration model, directory layout, governance constraints, and integration with lakeFS, OpenLineage, and KFM reliability requirements.

Airflow orchestration governs multi-stage data promotion flows, deterministic ETL operations, and lineage-rich dataset transitions across branches in the KFM datalake.

## 📘 Overview

Airflow pipelines in KFM v11 are responsible for:

- Coordinating extract → transform → validate flows.  
- Executing lakeFS branch-based versioning and controlled promotion.  
- Emitting OpenLineage events for all dataset transitions.  
- Integrating with reliability, rollback, and SLO-driven safeguards.  
- Ensuring promotion decisions comply with FAIR+CARE and sovereignty requirements.

Airflow DAGs are deterministic, explicitly documented, versioned, and subject to strict CI validation.

## 🧱 Directory Structure

```text
docs/
  pipelines/
    orchestration/
      airflow/
        README.md                                  # This index
        kfm-v11-branch-based-promotion.md          # Reference DAG architecture
        <future-dag-architecture-docs>.md

src/
  pipelines/
    orchestration/
      airflow/
        dags/                                      # Airflow DAGs
          kfm_v11_branch_based_promotion.py
          <future-dags>.py
        utils/                                     # Shared Airflow helpers
          lineage.py
          lakefs.py
```

This structure is normative for all Airflow orchestration pipelines.

## 🔁 Airflow Role in the KFM Pipeline Layer

Airflow acts as the orchestration tier connecting:

- Data ingestion and transformation tasks.  
- lakeFS version control operations.  
- OpenLineage lineage recording.  
- Contract validation workflows.  
- Fault-tolerant promotion and rollback procedures.  

Airflow DAGs function exclusively as **controllers**; they do not embed domain logic. Domain logic is implemented in reusable ETL and utility modules under `src/pipelines/`.

## ⚙ DAG Requirements

All Airflow DAGs must:

- Use deterministic task composition.  
- Support idempotent ETL behavior.  
- Integrate with WAL-style checkpointing where applicable.  
- Use lakeFS operators for commit, merge, revert, and cleanup.  
- Emit OpenLineage events for:

  - Run-level metadata.  
  - Job-level metadata.  
  - Dataset-level transitions.  

- Respect data contracts specified in `data_contract_ref`.  
- Conform to KFM-MDP v11.2.2 documentation and metadata standards.  

## 🪢 Common DAG Pattern: Branch-Based Promotion

KFM Airflow pipelines typically follow the branch-based promotion pattern:

1. Create feature branch.  
2. Ingest/copy raw input data.  
3. Run extract / transform / validate tasks.  
6. Commit to feature branch.  
7. Merge into main.  
8. Roll back on failure.  
9. Delete feature branch.

The canonical example is:

- `kfm_v11_branch_based_promotion.py`  
- Documented in:  
  - `kfm-v11-branch-based-promotion.md`

This pattern is required for all pipelines that modify curated dataset layers.

## 📊 Telemetry and Observability

Airflow orchestration pipelines must produce telemetry conforming to:

- `airflow-index-v11.json`  
- `energy-v2.json`  
- `carbon-v2.json`  

Telemetry includes:

- Task duration and DAG latency.  
- Reliability and promotion success metrics.  
- Rollback frequency.  
- Energy and carbon approximations.  
- Lineage completeness statistics.

Telemetry is aggregated into:

- `releases/<version>/pipelines-telemetry.json`

## ⚖ FAIR+CARE and Sovereignty

Airflow pipelines must uphold:

- CARE labeling and masking (domain-dependent).  
- Sovereignty rules encoded in data contracts.  
- Rejection of datasets failing CARE or license constraints.  
- Emission of CARE-related lineage facets when relevant.  

Promotion must never introduce unreviewed sensitive data into curated branches.

## 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.0.0 | 2025-11-27 | Initial v11 orchestration-Airflow index following KFM-MDP v11.2.2; fully governed layout and behavioral constraints. |

[Back to Orchestration Index](../README.md) · [Pipelines Overview](../../README.md) · [Governance Standards](../../../standards/README.md)