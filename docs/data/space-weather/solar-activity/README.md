---
title: "🌞 KFM v11 — Solar Activity & Space-Weather Ingestion Module"
description: "Real-time and archival ingestion of solar activity and space-weather data (flares, CMEs, Kp index, solar wind) into KFM STAC and the Neo4j knowledge graph."
path: "docs/data/space-weather/solar-activity/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric & Space-Weather Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x ingestion-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.3/space-weather-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/space-weather-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

status: "Active / Enforced"
doc_kind: "Dataset Ingestion Module"
header_profile: "standard"
footer_profile: "standard"

intent: "space-weather-ingestion"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"

scope:
  domain: "space-weather"
  applies_to:
    - "solar-activity-ingestion"
    - "geomagnetic-indexes"
    - "space-weather-story-nodes"

semantic_intent:
  - "dataset-ingestion"
  - "time-series"
  - "story-node-source"
category: "Data · Space-Weather · Ingestion"

sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Global / Space-Weather"
indigenous_rights_flag: false

data_steward: "Atmospheric & Space-Weather Council"
ttl_policy: "Indefinite (subject to archive policy)"
sunset_policy: "Supersede when v12 ingestion architecture is deployed"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Activity"
  owl_time: "ProperInterval"
  geosparql: "geo:Feature"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "GeoSPARQL"
  - "FAIR+CARE"

provenance_chain:
  - "docs/data/space-weather/solar-activity/README.md@v11.2.2"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-space-weather-solar-activity-v11.2.3.schema.json"
shape_schema_ref: "schemas/shacl/docs-space-weather-solar-activity-v11.2.3-shape.ttl"
story_node_refs:
  - "solar.alert"
  - "solar.cme"
  - "solar.geomagnetic"

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:data:space-weather:solar-activity:v11.2.3"
semantic_document_id: "kfm-data-space-weather-solar-activity-v11.2.3"
event_source_id: "ledger:kfm:doc:data:space-weather:solar-activity:v11.2.3"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "provenance-check"
  - "footer-check"
---

<div align="center">

# 🌞 KFM v11 — Solar Activity & Space-Weather Ingestion Module  

`docs/data/space-weather/solar-activity/README.md`

**Purpose:**  
Ingest **real-time and archival solar activity** (flares, CMEs, Kp index, solar wind) into **KFM-STAC Solar v2** and the Neo4j knowledge graph using the **Space-Weather CIDOC-CRM extension**, enabling Story Nodes and Focus Mode narratives around geomagnetic events.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../README.md) ·
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-informational)](../../../standards/kfm_markdown_protocol_v11.2.2.md) ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../../releases/v11.2.3/manifest.zip)

</div>

---

## 📘 1. Overview

This module captures **real-time and archival solar activity**, including:

- Solar flares (C/M/X classes)  
- CME propagation and trajectory models  
- NOAA SWPC alerts (R-scale, S-scale, G-scale)  
- Kp index and planetary geomagnetic activity  
- GOES XRS flux streams  
- LASCO CME velocity snapshots  
- ACE/DSCOVR solar wind measurements  

All data are standardized into **KFM-STAC Solar v2** and automatically ingested into the Neo4j knowledge graph via the **Space-Weather CIDOC-CRM extension**, with:

- Time-anchored events (OWL-Time intervals).  
- Spatial footprints for CME / geomagnetic impacts (GeoSPARQL).  
- Provenance chains from **instrument → product → transformation** (PROV-O).

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/data/space-weather/solar-activity/
├── 📄 README.md                                   # This file
│
├── 🛰️ realtime/                                   # Live streams & alerts
│   ├── xrs-goes/                                  # GOES 1–8Å & 0.5–4Å flux
│   ├── swpc-alerts/                               # R/S/G alerts (NOAA)
│   └── solar-wind/                                # ACE/DSCOVR proton density, speed, Bz
│
├── 🗂️ stac/                                        # STAC Collections / Items
│   ├── flares/                                    # Solar flare event STAC items
│   ├── cme/                                       # CME models, velocities, trajectories
│   ├── kp-index/                                  # Planetary Kp time-series STAC items
│   └── metadata/                                  # Collection-level metadata
│
├── 🧾 metadata/                                    # PROV-O lineage, DCAT, JSON-LD
│
├── 🛠️ transforms/                                  # Pipeline transforms, harmonization
│   ├── normalize-flare-levels.py
│   ├── cme-trajectory-merge.py
│   └── kp-index-clean.py
│
└── 📊 qc/                                          # Quality control & validation
    ├── flare-signal-qc.md
    └── cme-range-checks.md
~~~

The ingestion pipelines and QC notebooks referenced here MUST align with:

- The STAC/JSON schemas in `stac/metadata/`.  
- The telemetry schema at `telemetry_schema`.  
- The ingestion contract `ingest_space_weather_v11` (see section 5).

---

## ⚡ 3. Features

### 3.1 Real-Time Ingestion

- Direct fetch from **NOAA SWPC**, **GOES**, and **DSCOVR** endpoints.  
- Robust retry logic with deterministic **WAL replay** semantics.  
- Minute-level refresh rate for GOES XRS streams (1–8Å and 0.5–4Å).  
- Graceful degradation when upstream feeds are temporarily unavailable.

### 3.2 CME Trajectory Modeling

- Line-of-sight (LOS) velocity integration from coronagraph imagery.  
- References to **Enlil** and related heliospheric models.  
- **Earth-impact probability** tagging (and optional flags for Mars/L1).  
- Time-window alignment with geomagnetic response (Kp, Dst) for graph linking.

### 3.3 Unified Space-Weather Ontology

- **Solar flare → CME → geomagnetic impact** causal chain modeled as:
  - `:SolarFlareEvent`  
  - `:CoronalMassEjection`  
  - `:GeomagneticDisturbance` / `:GeomagneticStorm`  
- Time-anchored event windows using **OWL-Time** intervals.  
- Provenance via **PROV-O** (instrument → product → transformation pipelines).  
- Spatial context via **GeoSPARQL** geometries and KFM tiling standards.

### 3.4 KFM-Native Quality Checks

Implemented under `qc/` and telemetry rules:

- Flux spike detection for GOES XRS streams.  
- CME velocity plausibility tests (min/max/median ranges).  
- Kp smoothing and gap filling with explicit **uncertainty bands**.  
- Flags for data segments impacted by spacecraft anomalies or known calibration issues.

---

## 🔗 4. Story Node Integration (Focus Mode v3)

This module exposes the following Story Node families:

- **`solar.alert`** — High-level alerts derived from SWPC (R/S/G scales).  
- **`solar.cme`** — CME-centric narratives (launch time, velocity, target, probability).  
- **`solar.geomagnetic`** — Geomagnetic impact windows, Kp peaks, and auroral potential.

Capabilities:

- Automatic narrative generation for:
  - Solar storms and CME arrival windows.  
  - Aurora potential (e.g., G1–G3 events relevant to Kansas latitudes).  
  - Space-weather-linked impacts on:
    - HF radio communications  
    - GNSS accuracy  
    - Power infrastructure and pipelines across the KFM domain.  

Integration rules:

- Story Nodes MUST reference:
  - Underlying STAC Items (`stac/flares/`, `stac/cme/`, `stac/kp-index/`).  
  - PROV-O lineage identifiers for traceability.  
- Narratives MUST avoid speculative claims beyond the modeled uncertainty bands.

---

## 🧪 5. Validation & Reliability

Key properties:

- Deterministic ingestion contract: **`ingest_space_weather_v11`**  
- SLO-compliant latency: **< 120 seconds** from NOAA source → KFM STAC entry.  
- All transformations idempotent and re-runnable based on WAL logs.

Validation framework:

- **Schema validation** for STAC Collections/Items in `stac/`.  
- **Telemetry checks** against `space-weather-v2` schema:
  - Input availability  
  - Latency distributions  
  - Error/exception rates  
- **QC documents** in `qc/` define:
  - Thresholds for flux spikes and outliers.  
  - CME velocity envelope rules.  
  - Kp gap-filling logic and flags.

Any deviation from the ingestion contract MUST:

- Be recorded in telemetry as a governed exception.  
- Trigger reliability and/or space-weather council review.

---

## 📜 6. Version History

| Version  | Date       | Changes                                                         |
|----------|------------|-----------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Added X1.9 flare ingestion, CME tracking updates, ontology refinements. |
| v11.2.2  | 2025-10-14 | Kp STAC normalization, latency improvements, expanded QC checks. |
| v11.2.0  | 2025-08-01 | Initial v11 pipeline architecture and STAC/graph integration.  |

---

## 🏁 7. Governance & Oversight

**Governance Bodies:**

- Atmospheric & Space-Weather Council  
- FAIR+CARE Council  
- Provenance & Ethics Committee  

Responsibilities:

- Approve upstream source lists and modeling assumptions.  
- Review QC thresholds and telemetry SLOs.  
- Ensure FAIR+CARE application where space-weather data intersect with:
  - Critical infrastructure modeling.  
  - Community-facing alerting and Story Nodes.

---

<div align="center">

🌞 **KFM v11 — Solar Activity & Space-Weather Ingestion Module**  
Space-Weather Intelligence · Graph-Ready Events · FAIR+CARE-Aligned Data  

[📘 Data Index](../../README.md) · [🛰 Space-Weather Root](../README.md) · [⚖ Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>