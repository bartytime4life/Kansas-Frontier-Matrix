---
title: "🛰️ Remote-Sensing Orchestration — Prefect 3 & Airflow 3 Pattern Index"
path: "docs/events/remote-sensing/orchestration/prefect-airflow/README.md"
version: "v11.2.6"
last_updated: "2025-12-10"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Working Group & Pipelines & Provenance Working Group"
content_stability: "stable"

doc_kind: "Events / Pipelines Index"
status: "Active / Canonical"
intent: "remote-sensing-orchestration-prefect-airflow-index"
semantic_document_id: "kfm-doc-events-remote-sensing-orchestration-prefect-airflow-index-v11.2.6"

license: "CC-BY 4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
prov_profile: "KFM-PROV v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

header_profile: "standard"
footer_profile: "standard"

sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"
attestation_ref: "../../../../releases/v11.2.6/slsa-attestation.json"
signature_ref: "../../../../releases/v11.2.6/signature.sig"
telemetry_ref: "../../../../releases/v11.2.6/remote-sensing-orchestration-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/remote-sensing-orchestration-v11.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
---

# 🛰️ Remote-Sensing Orchestration — Prefect 3 & Airflow 3 Pattern Index

Index and runbook for **remote-sensing orchestration patterns** using **Prefect 3** and **Airflow 3** in KFM v11.2.6.

> Scope: remote-sensing pipelines that feed the KFM chain  
> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → Story Nodes → Focus Mode

This file ties together:

- remote-sensing **events** (`docs/events/remote-sensing/**`)  
- global **Event→Action** routing (`docs/events/README.md`)  
- **Prefect 3 / Airflow 3** orchestration update (`docs/events/orchestration/prefect-airflow/**`)  

---

## 🗂️ Directory Layout

~~~text
docs/
└── 📁 events/
    ├── 📁 remote-sensing/
    │   ├── 📄 README.md                               # Remote-sensing events index
    │   ├── 📄 2025-12-10-remote-sensing-event.md      # 📡 Example remote-sensing event summary
    │   └── 📁 orchestration/
    │       └── 📁 prefect-airflow/
    │           ├── 📄 README.md                       # 🛰️ This file — RS orchestration index & patterns
    │           ├── 📁 flows/
    │           │   ├── 📄 sentinel-2-prefect-flows.md # Prefect 3 patterns for Sentinel-2
    │           │   └── 📄 landsat-prefect-flows.md    # Prefect 3 patterns for Landsat
    │           ├── 📁 dags/
    │           │   ├── 📄 sentinel-2-airflow-dags.md  # Airflow 3 DAG patterns for Sentinel-2
    │           │   └── 📄 modis-airflow-dags.md       # Airflow 3 DAG patterns for MODIS
    │           └── 📁 playbooks/
    │               └── 📄 backfill-and-reprocess.md   # Operator playbooks (outage, backfill, reproc)
    │
    └── 📁 orchestration/
        └── 📁 prefect-airflow/
            └── 📄 2025-12-10-orchestration-update.md  # Global Prefect/Airflow orchestration event
~~~

Implementation & data (documented in their own READMEs):

- `src/pipelines/remote_sensing/` — Sentinel-2, Landsat, MODIS, radar, etc. ETL  
- `src/pipelines/orchestration/` — orchestration adapters for Prefect 3 and Airflow 3  
- `configs/remote_sensing/**` — mission-specific pipeline configs  
- `configs/orchestration/**` — platform & environment bindings  
- `data/events/orchestration/` — normalized orchestration event logs  
- `data/provenance/remote_sensing/` — PROV/OpenLineage bundles for remote-sensing ETL  

---

## 📘 Purpose & Scope

This README:

- indexes **remote-sensing orchestration docs** under:
  - `docs/events/remote-sensing/orchestration/prefect-airflow/**`  
- explains how these patterns integrate with:
  - **Event→Action Map** (`docs/events/README.md`)  
  - **Prefect 3 & Airflow 3 orchestration update**  
- provides **guidance** on when remote-sensing pipelines should:
  - run under **Prefect 3** vs **Airflow 3**  
  - respond to **product-availability**, **reprocessing**, and **algorithm-change** events  
- ensures all orchestration behavior is:
  - deterministic  
  - provenance-complete  
  - aligned with **FAIR+CARE** and remote-sensing governance  

---

## 🧬 Relationship to Global Orchestration & Events

Remote-sensing orchestration patterns sit at the intersection of:

- **Global orchestration event**  
  - `docs/events/orchestration/prefect-airflow/2025-12-10-orchestration-update.md`  
  - describes platform capabilities and high-level KFM guidance  

- **Event→Action Map**  
  - `docs/events/README.md`  
  - defines canonical mapping from `event_kind` / `status` → ETL/Catalog/Graph actions  

- **Remote-sensing events**  
  - `docs/events/remote-sensing/2025-12-10-remote-sensing-event.md`  
  - documents specific outages, tiling issues, reprocessing campaigns, etc.

This README constrains how **remote-sensing flows/DAGs**:

- respond to **events** (product-availability, reprocessing, algorithm-change)  
- implement the corresponding **Event→Action** behaviors  
- emit **telemetry and lineage** compatible with KFM-PROV v11 and STAC/DCAT requirements  

---

## ⚙️ Orchestration Patterns for Remote Sensing

### When to Prefer Prefect 3

Use **Prefect 3** for **lightweight, high-frequency** remote-sensing workflows, for example:

- small STAC update flows:
  - asset enrichment  
  - telemetry field updates (freshness, energy, SLO)  
- HRRR or model-driven subset extraction for remote-sensing overlays  
- micro-flows that glue:
  - downloads → quick transforms → STAC updates  

Characteristics:

- flow-level `retries` and `retry_delay_seconds` provide **fine-grained resiliency**  
- easier integration with **LangGraph** and Story Node pre-computation flows  
- good fit when:
  - lineage is captured via OpenLineage / PROV hooks at the **flow** level  
  - infrastructure footprint is relatively small  

### When to Prefer Airflow 3

Use **Airflow 3** for **heavier, regulated, or multi-mission** remote-sensing workflows:

- large DAGs for:
  - Sentinel-2 Level-2A tile processing  
  - Landsat gridded mosaics  
  - MODIS daily composites  
  - bulk reprocessing campaigns  

Characteristics:

- **DAG versioning** aligns with KFM’s versioned-transformation requirements  
- stronger native integration with OpenLineage  
- robust for:
  - long-running batch jobs  
  - cross-team pipelines  
  - complex dependencies (multi-dataset/multi-region)  

### Hybrid Patterns

Common hybrid pattern:

- **Airflow 3** orchestrates:
  - major reprocessing DAGs  
  - algorithm branches (e.g., new atmospheric correction model)  
- **Prefect 3** orchestrates:
  - downstream STAC/DCAT updates  
  - telemetry enrichment flows  
  - Story Node / Focus Mode layer-materialization flows  

Both platforms must adhere to the **Event→Action Map** and produce **coherent PROV/telemetry**.

---

## 🧭 Event→Action Integration (Remote Sensing)

Remote-sensing orchestration must implement the global routing rules:

### `event_kind=product-availability`

- **status=ongoing**
  - suspend or reduce ingest of affected missions (S2, Landsat, MODIS, etc.)  
  - mark STAC Collections/Items with:
    - `kfm:ingest_state="paused"`  
    - `kfm:qc="unverified"`  
    - `kfm:event_ref` pointing to the remote-sensing event  

- **status=resolved**
  - trigger **backfill** flows/DAGs:
    - Prefect: backfill flows per tile/scene group  
    - Airflow: backfill DAG runs per date window  
  - ensure new `DatasetVersion` nodes and STAC/DCAT version metadata are created  

### `event_kind=reprocessing`

- orchestrators must:
  - **pin** previous `DatasetVersion` as default  
  - run new reprocessing line in **parallel**  
  - produce separate STAC assets and graph nodes for the new line  
  - emit OpenLineage / PROV linking both lines  

### `event_kind=algorithm-change`

- orchestrators must:
  - branch into **new Collections / product IDs** when necessary  
  - update `processing_level` and algorithm metadata  
  - ensure Story Nodes expose differences between old and new algorithms  

Routing config in:

- `configs/events/router-events-routing.yaml`  

MUST be honored by both Prefect and Airflow remote-sensing entrypoints.

---

## 📊 Telemetry & Lineage for Remote-Sensing Orchestration

Remote-sensing orchestration runs must emit:

- **Telemetry** (per `telemetry_schema`):
  - run-level metrics:
    - start/end timestamps  
    - runtime, retries, failure counts  
    - number of scenes/tiles processed  
  - if available:
    - energy / CO₂ estimates tied to heavy remote-sensing jobs  

- **OpenLineage / PROV-O**:
  - each Prefect flow / Airflow DAG run is a `prov:Activity`  
  - inputs/outputs are `prov:Entity` nodes:
    - raw scenes  
    - processed products  
    - STAC Collections/Items  
  - orchestrator, worker pools, and services are `prov:Agent`  

PROV bundles SHOULD be stored under:

- `data/provenance/remote_sensing/orchestration/**`

and referenced from:

- STAC `kfm:lineage_run_id`  
- DCAT `prov:wasGeneratedBy` / `prov:wasDerivedFrom`  

---

## 📖 Story Nodes & Focus Mode

Remote-sensing orchestration patterns must support narrative surfaces:

- **Story Nodes**:
  - describe remote-sensing outages, tiling issues, reprocessing campaigns  
  - reference:
    - this orchestration index  
    - specific event docs  
    - affected Collections/Items and `DatasetVersion`s  

- **Focus Mode**:
  - uses orchestration-related provenance to:
    - explain **data gaps**  
    - differentiate **old vs new algorithms**  
    - show **backfill progress** or open reprocessing campaigns  

This README is written so content can be transformed into structured Story Node templates for remote-sensing orchestration incidents.

---

## 🕰️ Version History

| Version  | Date       | Notes                                                           |
|----------|------------|-----------------------------------------------------------------|
| v11.2.6  | 2025-12-10 | Initial remote-sensing Prefect/Airflow orchestration index.     |

---

### ⚖ FAIR+CARE & Governance Footer

This document:

- complies with **KFM-MDP v11.2.6**, **KFM-OP v11**, **KFM-PDC v11**, **KFM-STAC v11**, **KFM-DCAT v11**, and **KFM-PROV v11**  
- is governed by the **Remote Sensing Working Group** and **Pipelines & Provenance Working Group**, with co-review by the FAIR+CARE Council and Governance Council  
- must be updated when:
  - remote-sensing orchestration patterns change  
  - Prefect 3 / Airflow 3 integration behavior changes  
  - Event→Action mappings for remote-sensing pipelines are updated  

Edits require approval from the Remote Sensing Working Group and Pipelines & Provenance WG and must pass
`markdown-lint`, `schema-lint`, `footer-check`, and orchestration telemetry/lineage validation workflows.

<br/>

<sub>© Kansas Frontier Matrix · CC‑BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM‑MDP v11.2.6</sub>

<br/>

<div align="center">

🛰️ **Kansas Frontier Matrix — Remote-Sensing Orchestration (Prefect 3 & Airflow 3) Index v11.2.6**  
Deterministic RS Pipelines · Catalog–Graph Harmony · FAIR+CARE Governance  

[📘 Docs Root](../../../../README.md) · [📡 Events Index](../../../README.md) · [🛰️ Remote-Sensing Events](../../README.md) · [⚙️ Global Orchestration Update](../../../orchestration/prefect-airflow/2025-12-10-orchestration-update.md) · [⚖ Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>