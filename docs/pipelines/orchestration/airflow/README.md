---
title: "🌀 Kansas Frontier Matrix — Airflow Orchestration Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/orchestration/airflow/README.md"
version: "v11.2.0"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.0/pipelines-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/airflow-index-v11.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

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
intent: "airflow-orchestration-index"
category: "Orchestration · Pipelines · CI/CD · Governance"

classification: "Public Document"
sensitivity: "General"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

fair_category: "F1-A1-I2-R1"
care_label: "CARE-Aware · Low-Risk"

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
  - "docs/pipelines/orchestration/airflow/README.md@v11.0.0"
  - "docs/pipelines/orchestration/airflow/README.md@v10.4.1"
  - "docs/pipelines/orchestration/airflow/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true

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
  - "governance-override"
  - "content-alteration"
  - "narrative-fabrication"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

doc_uuid: "urn:kfm:doc:pipelines:orchestration:airflow:index:v11.2.0"
semantic_document_id: "kfm-airflow-orchestration-index"
event_source_id: "ledger:docs/pipelines/orchestration/airflow/README.md"
immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

jurisdiction: "Kansas · United States"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon orchestration-platform-v12"
---

<div align="center">

# 🌀 **Kansas Frontier Matrix — Airflow Orchestration Index (v11.2)**  
`docs/pipelines/orchestration/airflow/README.md`

[![Airflow](https://img.shields.io/badge/Orchestrator-Apache_Airflow-1e88e5)]()
[![OpenLineage](https://img.shields.io/badge/Lineage-OpenLineage_v1.20-9c27b0)]()
[![lakeFS](https://img.shields.io/badge/Data_Versioning-lakeFS-6a1b9a)]()
[![KFM Reliability](https://img.shields.io/badge/Reliability-Core_v11.2-success)]()
[![FAIR+CARE](https://img.shields.io/badge/Governance-FAIR%2BCARE-gold)]()

**Purpose**  
Serve as the authoritative index for **Airflow-based orchestration pipelines** in the Kansas Frontier Matrix (KFM).  
Define the Airflow orchestration model, governance constraints, OpenLineage integration, lakeFS branch-based promotion pattern, reliability rules, and metadata/telemetry required under KFM v11.2.

</div>

---

## 📘 1. Overview

Airflow in KFM v11.2 provides:

- Deterministic ETL scheduling and multi-step orchestration  
- Strict adherence to **lakeFS branch-based promotion workflow**  
- Full **OpenLineage** dataset/job lineage emission  
- Automatic correlation with **KFM OTEL traces**  
- FAIR+CARE-aware promotion gating  
- Reliability-first execution (WAL, retry, rollback, kill-switch)  
- Production promotion through environment-gated CI workflows  

Airflow DAGs do **not** embed domain logic—they control **orchestration**, not computation.

Domain logic resides under:

```
src/pipelines/<domain>/...
```

---

## 🗂️ 2. Directory Layout (v11.2 · Immediate + One Branch)

```text
📁 docs/pipelines/orchestration/airflow/         — Airflow orchestration documentation root
│   📄 README.md                                — This index
│   📄 kfm-v11-branch-based-promotion.md         — Canonical promotion DAG architecture

📁 src/pipelines/orchestration/airflow/          — Airflow implementation root
│   📂 dags/                                     — Airflow DAG definitions
│   📂 utils/                                    — lakeFS + lineage + promotion helpers
│   📄 README.md                                 — Implementation-level Airflow docs
```

This layout is authoritative for Airflow orchestration documentation & code in KFM v11.2.

---

## 🧱 3. Orchestration Role in the KFM Pipeline Stack

Airflow functions as the **control-plane orchestrator** coordinating:

- Extract → Transform → Validate DAG steps  
- Schema & data-contract checking  
- lakeFS-based dataset versioning  
- Deterministic promotion to curated layers  
- OpenLineage dataset-run transitions  
- Reliability checks (retry, rollback, failure thresholds)  
- OTEL trace correlation  
- FAIR+CARE governance enforcement  

Airflow DAGs initiate operations but delegate processing to reusable ETL modules.

---

## 🔁 4. Canonical Pattern: Branch-Based Promotion (KFM v11.2)

Every Airflow pipeline that produces curated data must implement:

1. Create feature branch (`lakefs branch`)  
2. Ingest raw inputs  
3. Transform + Validate  
4. Run reliability checks (hash stability, schema invariants)  
5. Commit to feature branch  
6. Merge → `main` (curated layer)  
7. Emit lineage (OpenLineage + PROV-O)  
8. Rollback if any step fails  
9. Delete temporary branch  

Canonical example:

- DAG: `kfm_v11_branch_based_promotion.py`  
- Doc: `kfm-v11-branch-based-promotion.md`

---

## 🛰️ 5. OpenLineage & OTEL Requirements

Every Airflow DAG must:

### OpenLineage
- Emit `START`, `RUNNING`, `COMPLETE`, `FAIL` events  
- Include dataset facets for:
  - input datasets  
  - output datasets  
  - modified branch  
  - producer metadata  

### OTEL Tracing
- Every DAG → trace  
- Every task → span  
- Correlated via:
  - `trace_id` (OTEL)  
  - `run_id` (OpenLineage)  
  - `focus_id` (Focus Mode v3)  

This allows deterministic replay + lineage → narrative coherence.

---

## ⚙️ 6. DAG Requirements (KFM v11.2)

All Airflow DAGs must:

- Be deterministic (no hidden nondeterminism)  
- Support idempotent task execution  
- Use lakeFS for version control operations (commit/merge/revert)  
- Enforce KFM data contracts  
- Generate provenance and metadata in STAC/DCAT-compatible formats  
- Respect CARE/sovereignty constraints  
- Emit telemetry (latency, lineage counts, energy/carbon)  

Promotion cannot proceed unless:

- Contract checks pass  
- Schema invariants hold  
- FAIR+CARE gate passes  
- Security checks pass (supply-chain defense)  

---

## 📊 7. Telemetry & Observability

All orchestrated runs contribute to:

```
releases/<version>/pipelines-telemetry.json
```

Telemetry includes:

- Task-level + DAG-level durations  
- Promotion rate / rollback rate  
- Error classes & retry patterns  
- lineage completeness  
- OTEL trace statistics  
- Energy Wh + Carbon gCO₂e (ISO 14064-compliant)  
- Governance results (FAIR+CARE)

---

## ⚖️ 8. FAIR+CARE / Sovereignty Enforcement

Airflow orchestration must ensure:

- Sensitive datasets are masked/generalized before merge  
- No curated dataset can contain unreviewed tribal or heritage data  
- CARE labels flow into dataset lineage  
- Sovereignty policies are honored at promotion boundaries  
- Branch promotion halts on:
  - missing CARE metadata  
  - unapproved coordinate precision  
  - licensing violations  

---

## 🧭 9. Integration with CI/CD & Auto-Update Engine

Airflow orchestration interacts with:

### `.github/workflows/` — CI/CD
- `data_pipeline.yml` validates DAG semantics & contract compliance  
- `faircare_validate.yml` ensures governance constraints  
- `security_audit.yml` ensures DAG dependencies are safe  
- `kfm-auto-update.yml` triggers Airflow DAG runs indirectly via ETL agents  

### Auto-Update → Promotion
- Airflow pipelines participate in runtime ingest  
- CI/CD controls when promotion → prod may occur  
- All merges require environment gating  

This establishes Airflow as a **governed pipeline executor** under KFM’s CI/CD framework.

---

## 🧪 10. Testing Requirements

Each Airflow pipeline must include:

- DAG parse validation  
- lakeFS branch lifecycle tests  
- Schema + contract validation  
- Reliability tests (WAL/retry/rollback)  
- OpenLineage event correctness tests  
- OTEL span structure tests  
- CARE/sovereignty gating tests  

Tests are required to pass before merging or promoting any DAG changes.

---

## 🕰️ 11. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| **v11.2.0** | 2025-11-27 | Upgraded to KFM-MDP v11.2.2; added directory layout, lineage/OTEL requirements, FAIR+CARE gating, and CI/CD integration. |
| **v11.0.0** | 2025-11-27 | Initial v11 orchestration-Airflow index with deterministic DAG + branch-based promotion specification. |

---

<div align="center">

**Kansas Frontier Matrix — Airflow Orchestration Architecture**  
*Deterministic · Governed · Lineage-Rich · FAIR+CARE Aligned*

[⬅ Back to Orchestration Index](../README.md) ·  
[📘 Pipelines Overview](../../README.md) ·  
[⚖ Governance Standards](../../../standards/README.md)  

</div>
