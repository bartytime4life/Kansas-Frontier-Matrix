---
title: "🛰️ Kansas Frontier Matrix — Remote-Sensing Orchestration Events Index"
path: "docs/events/remote-sensing/orchestration/README.md"
version: "v11.2.6"
last_updated: "2025-12-10"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Working Group & Pipelines & Provenance Working Group"
content_stability: "stable"

doc_kind: "Events / Pipelines Index"
status: "Active / Canonical"
intent: "remote-sensing-orchestration-index"
semantic_document_id: "kfm-doc-events-remote-sensing-orchestration-index-v11.2.6"

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
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
---

# 🛰️ Remote-Sensing Orchestration Events & Patterns Index  

Index and runbook for **remote-sensing orchestration events and patterns** in KFM v11.2.6, covering how:

> Prefect 3 & Airflow 3 → orchestrate remote-sensing ETL → update STAC/DCAT/PROV → sync Neo4j → feed Story Nodes & Focus Mode.

---

## 🗂️ Directory Layout

~~~text
docs/
└── 📁 events/
    ├── 📄 README.md                               # 🧭 Global Event→Action Map
    ├── 📁 remote-sensing/
    │   ├── 📄 README.md                           # 📡 Remote-sensing events index
    │   ├── 📄 2025-12-10-remote-sensing-event.md  # 📡 Example RS event summary
    │   └── 📁 orchestration/
    │       ├── 📄 README.md                       # 🛰️ This file — RS orchestration events & patterns index
    │       └── 📁 prefect-airflow/
    │           └── 📄 README.md                   # 🛰️ Prefect 3 & Airflow 3 RS orchestration patterns
    │
    └── 📁 orchestration/
        └── 📁 prefect-airflow/
            └── 📄 2025-12-10-orchestration-update.md  # ⚙️ Global Prefect/Airflow orchestration event
~~~

Implementation & data paths (documented in their own READMEs):

- `src/pipelines/remote_sensing/` — Sentinel-2, Landsat, MODIS, radar, etc. ETL  
- `src/pipelines/orchestration/` — Prefect 3 / Airflow 3 adapters and runners  
- `configs/remote_sensing/**` — mission-specific configs for RS pipelines  
- `configs/orchestration/**` — platform & environment bindings for orchestrators  
- `data/events/orchestration/` — normalized orchestration event logs  
- `data/provenance/remote_sensing/**` — PROV/OpenLineage bundles for RS ETL & orchestration  

---

## 📘 Purpose & Scope

This README is the **entry point** for all **remote-sensing orchestration events and patterns**:

- indexes RS orchestration docs under `docs/events/remote-sensing/orchestration/**`  
- connects RS orchestration to:
  - **global Event→Action Map** (`docs/events/README.md`)  
  - **global Prefect/Airflow orchestration update**  
  - **remote-sensing event records** (outages, reprocessing, algorithm changes)  
- ensures RS orchestrators:
  - behave **deterministically**  
  - emit **telemetry & PROV** compatible with KFM-PROV v11  
  - keep **STAC/DCAT/Neo4j** aligned with event semantics  
  - remain **FAIR+CARE** and sovereignty-aware  

Scope includes:

- Sentinel-2 / Landsat / MODIS / radar orchestration patterns  
- RS-specific event handling (product-availability, reprocessing, algorithm-change)  
- future RS orchestrator integrations (e.g., Dask-based or HPC schedulers)  

---

## 🧬 Relationship to Global Events & Orchestration

Remote-sensing orchestration sits at the intersection of three canonical docs:

1. **Event→Action Map** — `docs/events/README.md`  
   - defines `event_kind` + `status` → ETL / catalog / graph actions for all domains.  

2. **Global Prefect & Airflow Orchestration Update**  
   - `docs/events/orchestration/prefect-airflow/2025-12-10-orchestration-update.md`  
   - captures platform capabilities and high-level pipeline guidance.  

3. **Remote-Sensing Event Records**  
   - e.g., `docs/events/remote-sensing/2025-12-10-remote-sensing-event.md`  
   - describe specific RS outages, anomalies, reprocessing, or algorithm changes.  

This README constrains how **RS pipelines**:

- interpret and react to events via Prefect 3 / Airflow 3  
- embed event context into STAC, DCAT, and PROV  
- use telemetry to monitor orchestration-level SLOs for RS workloads  

---

## ⚙️ Remote-Sensing Orchestration Use-Cases

### Prefect 3 — Light & Narrative-Aligned RS Flows

Preferred for:

- small STAC update flows:
  - asset/reference updates  
  - telemetry enrichment (freshness, energy, SLO fields)  
- tile/scene-level microflows:
  - quick downloads + mask/compress + STAC write  
- LangGraph / Story Node preparation pipelines:
  - materializing RS layers for Focus Mode timelines  

Characteristics:

- fine-grained retry control at flow level  
- seamless integration with narrative pipelines  
- lineage captured via flow-run metadata → OpenLineage/PROV  

### Airflow 3 — Heavy, Historic, Multi-Mission RS DAGs

Preferred for:

- large DAGs:
  - Sentinel-2 L2A tiling and mosaicking  
  - Landsat composites  
  - MODIS daily/weekly RS products  
- reprocessing campaigns and algorithm-branch rollouts  
- cross-team workflows with strict audit requirements  

Characteristics:

- DAG version pinning aligned with **DatasetVersion** and PROV expectations  
- strong OpenLineage integration  
- robust scheduling for long-running, multi-step RS jobs  

### Hybrid RS Orchestration

Typical pattern:

- **Airflow 3**:
  - orchestrates heavy RS ETL / reprocessing jobs  
  - enforces DAG-version ↔ DatasetVersion mapping  

- **Prefect 3**:
  - orchestrates lighter, downstream RS flows:
    - STAC/DCAT metadata updates  
    - Story Node / Focus Mode layer-diffs  
    - cross-collection telemetry calculations  

All flows and DAGs MUST:

- respect **Event→Action routing**  
- emit event references (`kfm:event_ref`) into STAC/DCAT and graph nodes  

---

## 🧭 Event→Action Routing for Remote Sensing

Remote-sensing orchestration must implement the same core event families as the global runbook:

- **`product-availability`**
  - `ongoing` → pause or degrade RS ingest, mark STAC as `paused`/`unverified`  
  - `resolved` → resume ingest and trigger backfill DAGs/flows  

- **`reprocessing`**
  - pin prior RS DatasetVersion as default  
  - run new RS line in parallel  
  - register new versions and link via PROV and graph edges  

- **`algorithm-change`**
  - branch to new RS Collections or product IDs where necessary  
  - bump `processing_level` / algorithm metadata  
  - preserve old Collections and versions for historical queries  

Router config in `configs/events/router-events-routing.yaml` MUST be:

- consumed by RS Prefect flows and Airflow DAGs  
- reflected in provenance and telemetry outputs  

---

## 📊 Telemetry & Provenance Expectations

RS orchestration runs must emit:

- **Telemetry** (per `telemetry_schema`):
  - run id, platform (prefect/airflow), mission/pipeline id  
  - runtime, retries, failures, scenes/tiles processed  
  - (where available) energy / CO₂ metrics for RS workloads  

- **OpenLineage / PROV-O**:
  - each flow/DAG run ↦ `prov:Activity`  
  - RS artifacts (scenes, tiles, composites, STAC Items) ↦ `prov:Entity`  
  - orchestrators, worker pools, service accounts ↦ `prov:Agent`  

PROV bundles for RS orchestration SHOULD live under:

- `data/provenance/remote_sensing/orchestration/**`

and link back to:

- STAC `kfm:lineage_run_id`  
- DCAT `prov:wasGeneratedBy` / `prov:wasDerivedFrom`  

---

## 📖 Story Nodes & Focus Mode

RS orchestration behavior directly affects narratives:

- **Story Nodes**
  - remote-sensing outages / degradation events  
  - tiling or algorithm-change campaigns  
  - reprocessing and backfill progress stories  

- **Focus Mode**
  - layer-level diffs across versions (before/after reprocessing or algo change)  
  - temporal ribbons for outages and reprocessing windows  
  - cross-linking RS events with environmental, hydrologic, or air-quality stories  

This README is written so its concepts can be mapped into structured Story Node templates and graph entities.

---

## 🕰️ Version History

| Version  | Date       | Notes                                            |
|----------|------------|--------------------------------------------------|
| v11.2.6  | 2025-12-10 | Initial remote-sensing orchestration index.      |

---

### ⚖ FAIR+CARE & Governance Footer

This document:

- complies with **KFM-MDP v11.2.6**, **KFM-OP v11**, **KFM-PDC v11**, **KFM-STAC v11**, **KFM-DCAT v11**, and **KFM-PROV v11**  
- is governed by the **Remote Sensing Working Group** and **Pipelines & Provenance Working Group**, with co-review by the FAIR+CARE Council and Governance Council  
- must be updated when:
  - RS orchestration patterns change  
  - Prefect 3 / Airflow 3 integration evolves  
  - Event→Action routing rules for RS pipelines change  

Edits require approval from the Remote Sensing WG and Pipelines & Provenance WG and must pass
`markdown-lint`, `schema-lint`, `footer-check`, and RS orchestration telemetry & provenance validation workflows.

<br/>

<sub>© Kansas Frontier Matrix · CC‑BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM‑MDP v11.2.6</sub>

<br/>

<div align="center">

🛰️ **Kansas Frontier Matrix — Remote-Sensing Orchestration Events Index v11.2.6**  
Deterministic RS Pipelines · Catalog–Graph Harmony · FAIR+CARE Remote-Sensing Governance  

[📘 Docs Root](../../../README.md) · [📡 Events Index](../../README.md) · [🛰️ Remote-Sensing Events](../README.md) · [⚙ Global Orchestration Update](../../orchestration/prefect-airflow/2025-12-10-orchestration-update.md) · [⚖ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>