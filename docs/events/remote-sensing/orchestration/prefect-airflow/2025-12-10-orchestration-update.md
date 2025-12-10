---
title: "🛰️ Kansas Frontier Matrix — Prefect 3 & Airflow 3 Orchestration Update"
path: "docs/events/orchestration/prefect-airflow/2025-12-10-orchestration-update.md"
version: "v11.2.6"
last_updated: "2025-12-10"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Pipelines & Provenance Working Group"
content_stability: "stable"
status: "Active / In-Repo Canonical"

doc_kind: "Event Summary"
intent: "orchestration-platform-update"
semantic_document_id: "kfm-doc-orchestration-prefect-airflow-2025-12-10"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"
signature_ref: "../../../releases/v11.2.6/signature.sig"
telemetry_ref: "../../../releases/v11.2.6/orchestration-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/orchestration-update-v11.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"

license: "CC-BY 4.0"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

header_profile: "standard"
footer_profile: "standard"
---

# 🛰️ Prefect 3 & Airflow 3 — Orchestration Update for KFM Pipelines  

**Event Date:** 2025-12-10  
**Relevance:** Production ETL stability, lineage capture, and scheduling modernization for KFM v11.2.x pipelines.

This event describes how updates in **Prefect 3** and **Airflow 3** change KFM’s:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → Story Nodes → Focus Mode

orchestration layer, with specific guidance on governance, lineage, and deterministic behavior.

---

## 🗂️ Directory Layout

~~~text
docs/
└── 📁 events/
    ├── 📄 README.md                                  # 🧭 Event→Action Map
    └── 📁 orchestration/
        ├── 📄 README.md                              # ⚙️ Orchestration events index
        └── 📁 prefect-airflow/
            └── 📄 2025-12-10-orchestration-update.md # 🛰️ This file (Prefect 3 & Airflow 3 update)
~~~

Related implementation and data paths (documented in their own READMEs):

- `src/pipelines/orchestration/` — integration with Prefect 3 / Airflow 3  
- `configs/orchestration/` — orchestration configs and environment bindings  
- `data/events/orchestration/` — normalized orchestration event logs  
- `data/provenance/orchestration/` — PROV/OpenLineage bundles for orchestration runs  

---

## 📘 Overview

Both **Prefect 3** and **Airflow 3** introduced features that directly affect KFM’s orchestration of:

> deterministic ETL → catalog updates → graph synchronization → Story Node pipelines.

This event:

- records the **platform capabilities** KFM recognizes and uses  
- describes **approved integration patterns** for Prefect 3 and Airflow 3  
- aligns orchestration behavior with:
  - KFM-MDP v11.2.6 (authoring and documentation)  
  - KFM-PDC v11 (pipeline/data contracts)  
  - KFM-PROV v11 (provenance and lineage)  

---

## 🚦 Key Improvements & Impacts on KFM

### 1️⃣ Prefect 3 Flow Retries

- Native `@flow(retries=n, retry_delay_seconds=x)` now maps cleanly to KFM’s reliability envelope.  
- Enables deterministic replay without custom retry wrappers.  
- Recommended for **lightweight**, high-frequency workflows such as:
  - HRRR subset extraction  
  - geophysics preprocessors  
  - STAC asset enrichment microflows  

### 2️⃣ Prefect 3 Deployments

- Cron, interval, and event-based triggering supported.  
- Flow-run metadata can be wired into **OpenLineage / PROV** to enrich STAC and DCAT provenance:
  - `lineage_run_id`  
  - configuration hashes  
  - environment bindings  

### 3️⃣ Airflow 3 DAG Versioning

- DAG version binding per DAG run supports KFM’s strict reproducibility (versioned transformations).  
- Facilitates stable archival for:
  - archaeology ingestion DAGs  
  - hydrology batch transforms  
  - Focus Mode / Story Node pre-computation DAGs  

### 4️⃣ Airflow 3 Architecture & Scheduling

- React UI + FastAPI backend improve auditability and incident review.  
- Distributed task execution supports **HPC-style batching** (soil tiles, SAR scenes, remote-sensing grids).  
- Event-based scheduling allows:
  - NEXRAD quality-flag triggered re-runs  
  - KDHE water-quality submission triggers  
  - cross-system event routing consistent with the Event→Action Map  

### 5️⃣ Lineage Integration

- **Prefect 3**:
  - lineage emitted via explicit hooks / flow-run metadata  
- **Airflow 3**:
  - native OpenLineage provider support  
- Both can emit PROV-compatible information that feeds **KFM-PROV v11**, including:
  - `prov:Activity` for runs  
  - `prov:Entity` for outputs  
  - `prov:Agent` for orchestrators and services  

---

## 🧩 KFM Architectural Guidance

### Recommended Hybrid Strategy

~~~text
Legend:
- ✅ = preferred platform for this use case
- (ok) = acceptable but not preferred
~~~

| Use Case                  | Prefect 3 | Airflow 3 |
|---------------------------|----------:|----------:|
| Lightweight ETL           | ✅        | (ok)      |
| Heavy regulated ETL       | (ok)      | ✅        |
| High-frequency retry flows| ✅        | (ok)      |
| Historic batch DAGs       |           | ✅        |
| Lineage strictness        | Moderate  | Strong    |
| Multi-team workflows      |           | ✅        |

### Governance Alignment

- Both **Prefect 3** and **Airflow 3** can meet **FAIR+CARE** expectations when:
  - flows/DAGs are registered with KFM metadata templates  
  - run metadata is recorded via OpenLineage/PROV  
  - SBOM and attestations are kept in sync (`sbom_ref`, `attestation_ref`, `signature_ref`).  

- Airflow DAG version pinning helps satisfy **reproducible transformation** requirements for:
  - archaeology and hydrology stakeholders  
  - regulated data products with strict audit trails  

- Prefect flows integrate smoothly with **LangGraph / Story Node** pipelines, where orchestration is closer to narrative logic than heavy batch processing.

---

## 🔁 Integration With Event→Action Map

This orchestration update must be compatible with the **Event→Action Map** in `docs/events/README.md`:

- Orchestration platforms should react to **event_kind / status** combinations by:
  - pausing or resuming flows/DAGs  
  - triggering reprocessing or backfill runs  
  - branching on algorithm-change events  

- Declarative routing config (`configs/events/router-events-routing.yaml`) MUST be:
  - respected by both Prefect and Airflow entrypoints  
  - captured in provenance when orchestration responds to events.  

---

## 🧪 ETL, Telemetry & Lineage Changes

### ETL Behavior

- **Retries**:
  - standardized on Prefect 3’s `retries` or Airflow 3’s retry semantics  
  - recorded in telemetry as:
    - number of attempts  
    - success/failure outcomes  

- **Scheduling**:
  - cron/interval schedules must map to KFM’s **cadence** expectations per data source.  
  - event-based triggers must align with:
    - Event→Action Map  
    - SLO and error-budget rules  

### Telemetry

- `orchestration-telemetry.json` captures:
  - per-run runtime, failure counts, retry counts  
  - energy / CO₂ metrics tied to orchestration workloads (if available)  
  - SLO indicators (e.g., late-start, late-finish, missed run)  

- Telemetry schema (`orchestration-update-v11.json`) defines:
  - **required fields** (run_id, platform, dag_id/flow_name, status)  
  - optional **linking fields** (OpenLineage run IDs, PROV bundle IDs)  

### Lineage & PROV

- Every orchestrated run affecting catalogs or graph SHOULD:
  - emit OpenLineage events or equivalent  
  - be represented as a `prov:Activity` in KFM-PROV bundles  
  - link to:
    - `DatasetVersion` entities  
    - configuration entities (DAG/flow definitions, environment configs)  

---

## 🗂️ Orchestration Docs & Index

Family index for orchestration events and guidance:

- `docs/events/orchestration/README.md` — orchestration events index and conventions  
- `docs/events/orchestration/prefect-airflow/2025-12-10-orchestration-update.md` — this event  
- future docs may cover:
  - message bus integrations  
  - rollbacks or migrations between orchestrators  
  - deprecation of legacy tooling  

All orchestration events must tie back to:

- **Event→Action Map** (routing)  
- **KFM-PDC** (pipeline contracts)  
- **KFM-PROV** (lineage and reproducibility)  

---

## 📜 Version History

| Version  | Date       | Summary                                      |
|----------|------------|----------------------------------------------|
| v11.2.6  | 2025-12-10 | Initial orchestration update event recorded. |

---

### 🧭 Governance & Compliance Footer

This document:

- complies with **KFM-MDP v11.2.6**, **KFM-OP v11**, **KFM-PDC v11**, **KFM-STAC v11**, **KFM-DCAT v11**, and **KFM-PROV v11**  
- is governed by the **Pipelines & Provenance Working Group**, with co-review by the FAIR+CARE Council and Governance Council  
- must be updated when orchestration platforms, lineage integration patterns, or event-routing semantics change in ways that affect KFM determinism or governance

Edits require approval from the Pipelines & Provenance Working Group and FAIR+CARE Council and must pass
`markdown-lint`, `schema-lint`, `footer-check`, and orchestration telemetry + lineage validation workflows.

<br/>

<sub>© Kansas Frontier Matrix · CC‑BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM‑MDP v11.2.6</sub>

<br/>

<div align="center">

🛰️ **Kansas Frontier Matrix — Prefect 3 & Airflow 3 Orchestration Update v11.2.6**  
Deterministic Pipeline Orchestration · Lineage-First Scheduling · FAIR+CARE Governance  

[📘 Docs Root](../../../README.md) · [📡 Events Index](../../README.md) · [⚙️ Orchestration Events](../README.md) · [⚖ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>