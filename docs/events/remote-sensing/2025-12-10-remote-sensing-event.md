---
title: "📡 Kansas Frontier Matrix — Remote-Sensing Event Overview"
path: "docs/events/remote-sensing/2025-12-10-remote-sensing-event.md"
version: "v11.2.6"
last_updated: "2025-12-10"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council & Remote Sensing Working Group"
content_stability: "stable"
status: "Active"

doc_kind: "Event Summary"
intent: "remote-sensing-event"
semantic_document_id: "kfm-doc-remote-sensing-event-2025-12-10"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../releases/v11.2.6/telemetry/remote-sensing-event.json"
telemetry_schema: "../../../schemas/telemetry/remote-sensing-event-v11.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"

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

# 📡 Remote-Sensing Event — Overview

Remote-sensing events capture **time-bounded occurrences** that impact KFM’s:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j graph → API → Story Nodes → Focus Mode

This template documents a specific remote-sensing event (e.g., tiling outage, calibration issue, orbit anomaly) and its effects on ingestion, catalogs, graph, telemetry, and narrative surfaces.

---

## 🗂️ Directory Layout

~~~text
docs/
└── 📁 events/
    └── 📁 remote-sensing/
        ├── 📄 README.md                            # Remote-sensing events index
        ├── 📁 sentinel-2/                          # 🛰️ ESA Sentinel-2 MSI-specific events
        │   └── 📄 README.md
        ├── 📁 landsat/                             # 🛰️ USGS/NASA Landsat events
        │   └── 📄 README.md
        ├── 📁 modis/                               # 🌍 NASA MODIS Terra/Aqua events
        │   └── 📄 README.md
        ├── 📁 hrrr/                                # 🌫️ NOAA HRRR / model-linked remote-sensing events
        │   └── 📄 README.md
        ├── 📁 nexrad/                              # 🌪️ NEXRAD radar events
        │   └── 📄 README.md
        └── 📄 2025-12-10-remote-sensing-event.md   # 📡 This file (event summary)
~~~

Related (implementation & data) — see their own READMEs:

- `src/pipelines/remote_sensing/` — ingestion and preprocessing for S2, Landsat, MODIS, radar, etc.  
- `data/stac/remote_sensing/` — STAC Collections/Items for remote-sensing assets  
- `data/catalogs/remote_sensing/` — DCAT datasets and distributions  
- `src/graph/remote_sensing/` — Neo4j graph ingestion and constraints  

---

## 📘 Overview

Use this section to summarize the **event in plain language**:

- What happened? (e.g., “Sentinel-2 tiling outage over Kansas AOI”)  
- Why does it matter for KFM users and downstream analyses?  
- Is the event **ongoing**, **resolved**, or **intermittent**?  
- Which missions/sensors and data products are affected?  

This paragraph should be suitable for conversion into a **Story Node** description.

---

## 🛰️ Event Summary

Provide a clear description of the remote-sensing event. At minimum:

- **Sensors / missions involved**  
  - e.g., Sentinel-2, Landsat 8/9, MODIS Terra/Aqua, NEXRAD, HRRR-analogue products  
- **Temporal window**
  - explicit UTC start/end times (ISO 8601)  
- **Collections / product IDs**
  - STAC Collection IDs, mission/product names  
- **Nature of the event**
  - instrument anomalies, tiling or reprojection issues, outages, quality warnings, reprocessing campaigns  
- **Initial assessment**
  - suspected root cause (if known)  
  - whether data are missing, degraded, or delayed  

---

## 🌍 Spatial & Temporal Extent

Document the **where** and **when**:

- **Spatial extent**
  - AOIs (Kansas-wide, specific counties, watersheds, tiles)  
  - STAC geometries or grid/tile identifiers (e.g., Sentinel-2 MGRS tiles)  
- **Temporal extent**
  - `start_time` and `end_time` in UTC  
  - note if event is ongoing (open-ended end time)  
- **Affected coverage**
  - percent of nominal coverage impacted  
  - any relevant spatial patterns (e.g., only the western half of Kansas)  

This section must be specific enough that APIs and Story Nodes can expose the event as a filterable extent.

---

## 🔗 STAC / DCAT / PROV Integration

Summarize how this event is reflected in the catalogs and provenance:

- **STAC**
  - affected Collections and Items  
  - status flags and properties:
    - `kfm:ingest_state`, `kfm:qc`, `kfm:event_ref`, `kfm:mission:status` (if applicable)  
  - changes to:
    - `links` (e.g., alternate assets, replacement collections)  
    - `assets` (e.g., masked or removed bands)  

- **DCAT**
  - affected Datasets and Distributions  
  - updates to:
    - `dct:hasVersion`, `dct:isVersionOf`, `prov:wasDerivedFrom`  
    - `dcat:versionNotes` describing outage, backfill, or reprocessing  

- **PROV / OpenLineage**
  - new `prov:Activity` records for:
    - outage detection  
    - reprocessing or backfill  
  - `prov:Entity` updates for:
    - degraded vs corrected products  
  - `prov:Agent` for:
    - pipelines, operators, and upstream agencies involved  

---

## 🔁 ETL & Pipeline Impact

Describe how the event changes ETL and pipelines across the KFM stack:

- **Ingestion workflows**
  - pause/resume behavior  
  - reduced polling or fail-open/fail-closed strategies  
  - temporary source substitution (if any)  

- **Data validation**
  - Great Expectations or equivalent checks triggered/failing  
  - schema-lint or structural anomalies observed  

- **Derivation hashes & versions**
  - any changes to derivation hashes for affected STAC/DCAT artifacts  
  - new `DatasetVersion` nodes or version labels created  

- **Outage & replay**
  - outage window(s) that require backfill  
  - replay strategy and ordering (e.g., ingest after provider reprocessing)  

- **WAL / retries / idempotency**
  - WAL (write-ahead log) implications  
  - retry strategies adjusted for this event  
  - guarantees that re-runs produce consistent outcomes  

---

## 🧭 Neo4j Graph Modeling Notes

Explain the graph-model changes this event implies:

- **Node labels**
  - new or affected labels, e.g.:
    - `RemoteSensingEvent`  
    - `Mission`, `Dataset`, `DatasetVersion`  
    - `Scene`, `Tile`, `Acquisition`  

- **Relationships**
  - edges connecting the event to:
    - missions, datasets, tiles, regions, Story Nodes  
  - examples:
    - `(:RemoteSensingEvent)-[:AFFECTS_DATASET]->(:Dataset)`  
    - `(:RemoteSensingEvent)-[:AFFECTS_REGION]->(:Region)`  
    - `(:RemoteSensingEvent)-[:EXPLAINED_BY]->(:StoryNode)`  

- **Provenance edges**
  - `:DERIVED_FROM`, `:WAS_GENERATED_BY`, or equivalent mappings from PROV  
  - pointers from graph nodes back to STAC/DCAT IDs and PROV bundles  

- **Story Node / Focus Mode integration**
  - how this event should appear:
    - ribbons or callouts in timelines  
    - filters by mission/region/time  
    - “data gap / outage” annotations on layers  

---

## 📉 Downstream Effects

Capture impacts beyond ingestion:

- **Analytics & models**
  - which models or analyses are affected (e.g., NDVI trends, drought indices, air-quality fusion)  
  - whether training or inference runs must be discarded or re-run  

- **APIs & dashboards**
  - API endpoints that may return partial or degraded results  
  - dashboards or maps showing gaps or delayed updates  

- **User-facing notes**
  - recommended messaging for:
    - researchers  
    - public-facing interfaces  
    - partners relying on time-critical products  

This section should provide enough guidance for reliability, product, and communication teams.

---

## 🤝 Sovereignty & FAIR+CARE Considerations

Note any considerations related to FAIR+CARE and sovereignty:

- **Indigenous data sovereignty**
  - whether affected regions overlap Indigenous lands or sensitive cultural areas  
  - if special handling or consultation is required for data interpretation  

- **FAIR+CARE alignment**
  - how transparency and accountability are preserved:
    - clear annotation of gaps or anomalies  
    - accessible documentation of event impacts  

- **Ethical storytelling**
  - any constraints on how this event should be contextualized in Story Nodes and Focus Mode  
  - avoidance of misleading narratives or misuse of incomplete/reprocessed data  

---

## 📊 Telemetry References

Link this event to telemetry sources:

- **Telemetry files**
  - `telemetry_ref` for event-specific metrics (runtime, errors, gaps)  
  - any additional telemetry streams (e.g., STAC telemetry for impacted Collections)  

- **Key metrics**
  - ingestion latency and failure rates  
  - volume of missing/degraded scenes  
  - energy and CO₂ metrics (if reprocessing is required)  

- **Correlation**
  - notes on matching telemetry timestamps and IDs to:
    - pipeline runs  
    - graph nodes  
    - STAC/DCAT artifacts  

---

## 📝 Version History

| Version | Date       | Author  | Notes                      |
|---------|------------|---------|----------------------------|
| v11.2.6 | 2025-12-10 | system  | Initial remote-sensing event template. |

---

### 🏛️ Governance & Compliance Footer

This document:

- complies with **KFM-MDP v11.2.6**, **KFM-OP v11**, **KFM-PDC v11**, **KFM-STAC v11**, **KFM-DCAT v11**, and **KFM-PROV v11**  
- is governed by the **Remote Sensing Working Group** with co-review by the **FAIR+CARE Council** and Governance Council  
- must be updated when remote-sensing event documentation patterns, routing semantics, or catalog/graph integration change

Edits require approval from the Remote Sensing Working Group and FAIR+CARE Council and must pass
`markdown-lint`, `schema-lint`, `footer-check`, and remote-sensing event validation workflows (including telemetry and provenance checks).

<br/>

<sub>© Kansas Frontier Matrix · CC‑BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM‑MDP v11.2.6</sub>

<br/>

<div align="center">

📡 **Kansas Frontier Matrix — Remote-Sensing Event Template v11.2.6**  
Deterministic Events · Catalog–Graph Harmony · FAIR+CARE Remote Sensing Governance  

[📘 Docs Root](../../README.md) · [📡 Events Index](../README.md) · [🛰️ Remote-Sensing Events Index](./README.md) · [⚖ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md)

</div>