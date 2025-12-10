---
title: "🛰️ Kansas Frontier Matrix — Landsat 8–9 Product Availability Interruption (2025-12-08)"
path: "docs/events/remote-sensing/landsat/2025-12-08-landsat-interruption.md"
version: "v11.2.2"
last_updated: "2025-12-10"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing & Earth Observation Committee"
content_stability: "stable"
status: "Active / Informational · External Event Log"
doc_kind: "Event Log · Remote Sensing"
classification: "Public"

doc_uuid: "urn:kfm:doc:event:remote-sensing:landsat:interruption:2025-12-05"
semantic_document_id: "landsat-8-9-product-interruption-2025-12-05"
event_source_id: "ledger:kfm:event:remote-sensing:landsat:product-interruption:2025-12-05"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
attestation_ref: "../../../../releases/v11.2.2/slsa-attestation.json"
signature_ref: "../../../../releases/v11.2.2/signature.sig"

telemetry_ref: "../../../../releases/v11.2.2/earth-observation-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/earth-observation-v3.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
---

# 🛰️ **Landsat 8–9 Product Availability Interruption (2025-12-08)**  
`docs/events/remote-sensing/landsat/2025-12-08-landsat-interruption.md`

**Purpose**  
Record the December 2025 Landsat 8 and Landsat 9 Level-1/2/3 product availability interruption reported by USGS EROS, assess its impact on KFM’s **Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode** pipeline, and provide provenance hooks for downstream datasets and Story Nodes.

`USGS EROS Data Notification · External Event Record`  
`Event Start: 2025-12-05 · Event Posted: 2025-12-08 · End Time: Unknown`

---

## 📘 Overview

On **2025-12-08**, the **USGS Earth Resources Observation and Science (EROS) Center** released a data notification reporting a disruption in the availability of **Landsat 8 and Landsat 9 Level‑1, Level‑2, and Level‑3 products**.

The interruption began on **Friday, 2025-12-05**, due to unplanned maintenance affecting science‑data processing and distribution systems. At the time of notification, **no estimated resolution time** was provided.

Within Kansas Frontier Matrix (KFM), this document functions as:

- An **external event log** for long‑term historical continuity.
- A **stability marker** for Landsat‑based ETL pipelines and STAC/DCAT catalogs.
- A **provenance anchor** for any datasets or Story Nodes that depend on Landsat 8/9 acquisitions affected by the interruption window.

---

## 🗂️ Directory Layout

~~~text
📁 Kansas-Frontier-Matrix/
└── 📁 docs/
    └── 📁 events/
        └── 📁 remote-sensing/
            └── 📁 landsat/
                └── 📄 2025-12-08-landsat-interruption.md   # This document
~~~

---

## 🧭 Context

### 📡 Event Summary

- **Products affected**
  - **Landsat 8:** Level‑1, Level‑2, Level‑3  
  - **Landsat 9:** Level‑1, Level‑2, Level‑3
- **Root cause (reported):** Unplanned maintenance impacting EROS science‑data production and distribution workflows.
- **User impact:** Newly acquired Landsat 8/9 scenes after **2025-12-05** are delayed; no new Level‑1+ products available to downstream users during the interruption.
- **Expected delay:** **Unknown** at time of notice (open‑ended event).

### 🛠️ KFM Impact Assessment

#### ✔️ Affected Systems

| Subsystem                                  | Impact       | Notes |
|-------------------------------------------|-------------|-------|
| **Remote‑Sensing ETL (Landsat pipeline)** | **Moderate** | Scene ingestion resumes automatically once USGS resumes product generation. |
| **STAC Catalog Synchronization**          | **Low–Moderate** | New STAC Items for Landsat 8/9 are missing for acquisitions after 2025‑12‑05 until Level‑1 products reappear. |
| **DCAT Derivation Chain**                 | **Low**      | Deterministic, but downstream DCAT nodes for affected dates are not yet materialized. |
| **Focus Mode v3 Story Nodes**             | **Variable** | Recent satellite‑driven narratives may show a data‑gap period for the interruption window. |
| **Predictive Ecology / Soil / Hydrology Models** | **Low–Moderate** | Time‑series features may contain gaps; imputations remain deterministic and documented. |

#### 🧭 Mitigation Actions (Automated)

KFM remote‑sensing infrastructure reacts to this event through existing safeguards:

- **Auto‑requeue:** All missing Landsat acquisitions are **automatically requeued** for processing every 6 hours.
- **Daily verification step** checks for:
  - Newly released **Level‑1** scenes.
  - Required **auxiliary atmospheric data**.
  - Completion of **Level‑2 (surface reflectance)** and **Level‑3 (surface temperature or derivatives)**.
- **Provenance markers**:
  - A “**external delay – upstream data provider**” flag is attached to relevant pipeline runs.
  - Temporal gaps in expected scene cadence are recorded as **expected missingness**, not ETL failure.

### 📊 Downstream Effects for Kansas‑Focused Work

#### 🌾 Agriculture & Vegetation Monitoring

- Weekly NDVI/NDMI and related vegetation composites for **December 2025** may show reduced fidelity or increased reliance on multi‑sensor fusion.
- Where coverage and cloud conditions allow, **Sentinel‑2A/B** acts as a primary fallback for vegetation indices over Kansas.

#### 🌊 Hydrology & Sedimentation Studies

- Landsat‑based water‑extent snapshots around:
  - **Kansas River**
  - **Tuttle Creek**
  - **Cheney Reservoir**
- may show **missing or delayed scenes** during the interruption window, affecting short‑term water‑extent and turbidity analyses.

#### 🏺 Archaeology & Historical Landscape Dynamics

- **Long‑term comparative analyses** (multi‑year to multi‑decadal) remain effectively unaffected.
- **Short‑term seasonal monitoring** (e.g., December 2025 agricultural fallow patterns, vegetation stress near sites of interest) may contain temporal gaps in Landsat‑derived imagery.

---

## 🌐 STAC, DCAT & PROV Alignment

### 🔗 Integration With KFM Provenance Layers

KFM treats this interruption as a first‑class provenance event that can be linked to any impacted dataset.

**PROV‑O representation (conceptual)**

~~~text
Entity:   landsat:product:interruption:2025-12-05
Agent:    usgs:eros
Activity: eros:system-maintenance
Started:  2025-12-05T00:00Z
Ended:    null
Status:   ongoing
~~~

**Usage within the KFM pipeline:**

- **ETL / Pipelines**
  - ETL runs for Landsat 8/9 scenes with acquisition times ≥ **2025‑12‑05** may record:
    - `prov:wasInfluencedBy landsat:product:interruption:2025-12-05`
    - or a qualified association noting “upstream product delay.”
- **STAC**
  - Landsat‑related STAC Collections/Items in `data/stac/` for this period may include:
    - A collection‑level or item‑level metadata field (e.g., `kfm:provenance_events`) referencing the above PROV Entity.
- **DCAT**
  - DCAT Datasets representing Landsat‑derived products over Kansas can:
    - Declare themselves as `prov:Entity` and link to this event using `prov:wasInfluencedBy` or `prov:wasDerivedFrom` where appropriate.
    - Record temporal coverage gaps explicitly in `dct:temporal`.

Together, these hooks make it possible for graph queries and Story Nodes to explain **why** certain time slices lack Landsat coverage without misclassifying the situation as an internal KFM failure.

---

## 🧪 Validation & CI/CD

### 🧪 Data Validation & Telemetry Hooks

#### Validation

- No **schema drift** is observed in Landsat STAC Items or internal catalog schemas.
- Missing scenes for the interruption window are explicitly classified as **expected missingness**, not ETL or validation errors.
- Downstream validations (e.g., cross‑sensor comparisons against Sentinel‑2 composites) can use the interruption event to gate their checks and avoid false alarms.

#### Telemetry

- KFM telemetry shows a controlled elevation in:
  - `landsat.pipeline.waiting_scenes`
  - `landsat.ingest.missing_aux_data`
- CI/CD pipelines treating ETL configs and STAC/DCAT schemas as code:
  - Continue to pass, since no structural changes are introduced by the upstream maintenance.
- Energy/carbon impact is **lower than normal** for Landsat workloads during the interruption:
  - Processing cycles are halted or reduced rather than repeatedly failing.

---

## 🧠 Story Node & Focus Mode Integration

KFM v11 Story Nodes and Focus Mode should expose this event transparently to users relying on recent satellite narratives.

### 🧩 Candidate Story Nodes (Interpretive Layer)

- **Title:** “Landsat Quiet Days Over Kansas (December 2025)”  
  **Facts (graph‑backed):**
  - Landsat 8/9 Level‑1+ products missing or delayed for acquisitions ≥ **2025‑12‑05**.
  - Sentinel‑2 coverage often filling the gap in key agricultural and hydrologic areas.
- **Title:** “Upstream Maintenance, Downstream Gaps”  
  **Facts (graph‑backed):**
  - KFM ETL runs in a “waiting” state for Landsat acquisitions during the interruption.
  - STAC/DCAT/PROV metadata for affected datasets reference the `landsat:product:interruption:2025-12-05` Entity.

### 🧭 Focus Mode Behavior

In **Focus Mode**:

- **Facts (must be shown clearly)**
  - Time‑series visualizations involving Landsat over Kansas for December 2025 should visibly mark the interruption window as a **data gap linked to a USGS/EROS event**, not as a permanent absence of data.
- **Interpretation (clearly labeled as such)**
  - Narrative hints can explain that upstream maintenance at EROS occasionally affects downstream availability, and that KFM mitigates this via multi‑sensor strategies and requeueing.
- **Speculation (optional and clearly tagged)**
  - Story Nodes may optionally suggest that prolonged interruptions could shift reliance toward other sensors (e.g., Sentinel‑2, commercial imagery), but such statements must be tagged as **speculation**, not fact.

---

## ⚖ FAIR+CARE & Governance

- **Rights & licensing**
  - This event log is published under **CC‑BY 4.0** (see `license` in front‑matter).
  - Underlying Landsat data remain subject to **USGS/EROS licensing and public‑domain status** outside of this document.
- **CARE & sovereignty**
  - The event concerns **global satellite operations**, not specific Indigenous or culturally sensitive sites.
  - Any derived analyses that intersect with **Indigenous lands or sensitive archaeological contexts** must still respect:
    - Spatial generalization requirements (e.g., coarser grids for public maps).
    - The KFM **Indigenous Data Protection** standard referenced in `sovereignty_policy`.
- **Security & privacy**
  - No secrets, credentials, or PII are present in this event record.
  - The document may be surfaced publicly as part of KFM’s transparency around data quality and upstream dependencies.

---

## 🕰️ Version History

| Version  | Date       | Summary                                                                                             |
|---------:|-----------:|-----------------------------------------------------------------------------------------------------|
| v11.2.2  | 2025-12-10 | Initial public event log for the USGS EROS Landsat 8/9 product interruption; aligned with KFM-MDP v11.2.6 (H2 registry, directory layout, provenance hooks, Story Node & governance sections). |

---

<div align="center">

📑 **Kansas Frontier Matrix — Landsat 8–9 Product Availability Interruption (2025-12-08)**  
Scientific Insight · Documentation‑First · FAIR+CARE Ethics · Sustainable Intelligence  

[📘 Docs Root](../../..) · [📂 Standards Index](../../../standards/README.md) · [⚖ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
