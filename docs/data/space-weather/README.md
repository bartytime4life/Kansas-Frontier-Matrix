---
title: "🛰️ KFM v11 — Space-Weather Data Domain Overview"
description: "Domain-level overview for space-weather datasets in KFM, including solar activity, geomagnetic indexes, and pipeline integration into STAC and the knowledge graph."
path: "docs/data/space-weather/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric & Space-Weather Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x space-weather-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/space-weather-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/space-weather-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

status: "Active / Enforced"
doc_kind: "Domain Overview"
header_profile: "standard"
footer_profile: "standard"

intent: "space-weather-domain"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"

scope:
  domain: "space-weather"
  applies_to:
    - "solar-activity"
    - "geomagnetic-indexes"
    - "space-weather-ingestion"
    - "space-weather-story-nodes"

semantic_intent:
  - "domain-overview"
  - "dataset-architecture"
  - "story-node-source"
category: "Data · Space-Weather · Domain"

sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Global / Space-Weather"
indigenous_rights_flag: false

data_steward: "Atmospheric & Space-Weather Council"
ttl_policy: "Indefinite (subject to archive policy)"
sunset_policy: "Supersede when v12 domain architecture is adopted"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "GeoSPARQL"
  - "FAIR+CARE"

provenance_chain:
  - "docs/data/space-weather/README.md@v11.2.2"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-space-weather-domain-v11.2.3.schema.json"
shape_schema_ref: "schemas/shacl/docs-space-weather-domain-v11.2.3-shape.ttl"
story_node_refs:
  - "solar.alert"
  - "solar.cme"
  - "solar.geomagnetic"

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:data:space-weather:ROOT:v11.2.3"
semantic_document_id: "kfm-data-space-weather-domain-v11.2.3"
event_source_id: "ledger:kfm:doc:data:space-weather:ROOT:v11.2.3"

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

# 🛰️ KFM v11 — Space-Weather Data Domain Overview  

`docs/data/space-weather/README.md`

**Purpose:**  
Provide a governed, architecture-safe overview of the **space-weather data domain** in KFM v11, including solar activity, geomagnetic responses, ingestion pipelines, STAC/graph integration, and Story Node usage.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md) ·
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-informational)](../../standards/kfm_markdown_protocol_v11.2.2.md) ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)](../../standards/faircare/FAIRCARE-GUIDE.md) ·
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../releases/v11.2.3/manifest.zip)

</div>

---

## 📘 1. Domain Overview

The **space-weather domain** covers datasets and pipelines that describe:

- **Solar activity** (flares, CMEs, active regions).  
- **Heliospheric conditions** (solar wind, interplanetary magnetic field).  
- **Geomagnetic responses** (Kp index, storms, auroral activity).  

These datasets are used to:

- Contextualize **GNSS accuracy**, **communications reliability**, and **power/infra risk** within Kansas and surrounding regions.  
- Provide **Story Nodes** and **Focus Mode** narratives around major space-weather events (e.g., strong CMEs, elevated Kp).  
- Support research on correlations between space weather and:
  - Remote sensing anomalies  
  - Infrastructure telemetry  
  - Environmental time series in the KFM knowledge graph.

All space-weather sources are harmonized into:

- **KFM-STAC Solar / Geomagnetic collections**.  
- A **CIDOC-CRM + PROV-O + OWL-Time** aligned ontology in Neo4j.  
- Telemetry under `space-weather-v2` schemas for latency, reliability, and QC tracking.

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/data/space-weather/
├── 📄 README.md                              # This file (domain overview)
│
├── 🌞 solar-activity/                        # Solar flares, CMEs, solar wind, Kp
│   └── 📄 README.md                          # Solar activity ingestion module
│
├── 🌐 geomagnetic/                           # (Planned) geomagnetic field & indices
│   └── 📄 README.md                          # Domain-specific geomagnetic docs (TBD)
│
├── 🧭 ionosphere/                            # (Planned) ionospheric TEC & disturbances
│   └── 📄 README.md                          # Ionospheric products & integrations (TBD)
│
└── 🧪 qa/                                    # Shared space-weather QA policies
    └── 📄 README.md                          # Cross-module QC & validation guidelines
~~~

**Rules:**

- Each subdirectory MUST have its own README aligned with **KFM-MDP v11.2.2**.  
- Shared schemas (STAC, JSON-LD, SHACL) SHOULD live under `metadata/` or `stac/metadata/` in the relevant submodule.  
- Domain-wide QA policies should be centralized in `qa/`.

---

## 🧬 3. Data Sources & Products (High-Level)

Core upstream sources (non-exhaustive):

- **NOAA SWPC** — Alerts (R/S/G scales), Kp index, solar event reports.  
- **GOES** — XRS flux, proton flux, X-ray classifications.  
- **DSCOVR / ACE** — Solar wind speed, proton density, IMF/Bz.  
- **LASCO / coronagraphs** — CME detections, velocities, directions.

Primary product classes in KFM:

- **Solar event catalogs** (flares, CMEs, shocks).  
- **Heliospheric time series** (solar wind / IMF).  
- **Geomagnetic time series** (Kp, Dst, local indices).  
- **Derived risk indicators** (e.g., Kp thresholds relevant to Kansas latitudes).

Every product must:

- Carry clear **provenance** (instrument, processing chain).  
- Reference **units**, **uncertainty**, and **limitations**.  
- Support **interoperability** with hydrology, remote sensing, and infrastructure data where relevant.

---

## 🧭 4. Integration with ETL, STAC, and Knowledge Graph

### 4.1 ETL / Ingestion

- Pipelines ingest raw feeds into **landing zones**, then into normalized **STAC Collections/Items**.  
- Ingestion contracts (e.g., `ingest_space_weather_v11`) define:
  - Frequency and latency SLOs.  
  - Retry, WAL, and idempotency requirements.  
  - QC hooks and telemetry emission.

### 4.2 STAC & DCAT

- Solar/geomagnetic products live in dedicated STAC Collections under `docs/data/space-weather/*/stac/`.  
- Each Collection/Item MUST:
  - Conform to **STAC 1.0.0** core.  
  - Use custom KFM extensions for solar/geomagnetic attributes.  
  - Map cleanly to DCAT `Dataset` and `Distribution` concepts.

### 4.3 Neo4j Ontology

- Events and products are represented as nodes such as:
  - `:SolarFlareEvent`, `:CoronalMassEjection`, `:GeomagneticDisturbance`.  
- Key relationships include:
  - `:CAUSES`, `:ASSOCIATED_WITH`, `:OBSERVED_BY`.  
- Time intervals modeled using **OWL-Time**.  
- Provenance modeled using **PROV-O** activities and agents.

---

## 🔗 5. Story Nodes & Focus Mode

Space-weather data drive several Story Node families, particularly from `solar-activity/`:

- `solar.alert` — Summaries of high-impact alerts and storm conditions.  
- `solar.cme` — CME-centric episodes with arrival windows and risk.  
- `solar.geomagnetic` — Geomagnetic storm phases and auroral potential.

Integration requirements:

- Story Nodes MUST reference underlying STAC Items and graph nodes.  
- Focus Mode MUST:
  - Provide clear time windows and uncertainty.  
  - Avoid deterministic claims about local impacts beyond modeled scope.  
  - Respect FAIR+CARE when relating space-weather events to critical infrastructure or community-facing narratives.

---

## 🧪 6. Telemetry, QC, and Reliability

Domain-wide telemetry SHOULD capture:

- Ingestion latency (upstream → STAC → graph).  
- Data availability and completeness per source.  
- QC outcomes (flux spikes, missing intervals, anomalous Kp runs).  

The `space-weather-v2` telemetry schema defines:

- Standard fields for **success/failure**, **latency**, **record counts**, and **QC flags**.  
- Hooks for feeding reliability dashboards and operational alerts.

Cross-module QC policies live in `docs/data/space-weather/qa/` and MUST be referenced by:

- `solar-activity/README.md`  
- Future `geomagnetic/` and `ionosphere/` modules.

---

## ⚖️ 7. FAIR+CARE & Governance Considerations

While space-weather data are non-sensitive, governance still applies:

- **FAIR:**
  - Findable: standardized STAC Collections and graph nodes.  
  - Accessible: documented access paths and licensing.  
  - Interoperable: consistent units and ontologies across KFM domains.  
  - Reusable: versioned schemas, proven provenance, and uncertainty.

- **CARE:**
  - Consider downstream use when linking space-weather events to:
    - Infrastructure risk models.  
    - Public-facing alerts or narratives.  
  - Avoid alarmist or speculative framing in Story Nodes.  
  - Ensure that any policy/infrastructure impacts are grounded in vetted models.

The Atmospheric & Space-Weather Council and FAIR+CARE Council jointly oversee:

- Source selection and reliability.  
- Model assumptions for derived risk indicators.  
- Telemetry thresholds that might trigger operational responses.

---

## 🕰️ 8. Version History

| Version  | Date       | Author                             | Summary                                                      |
|----------|------------|------------------------------------|--------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Atmospheric & Space-Weather Council | Established v11 domain overview; aligned with solar-activity module. |
| v11.2.2  | 2025-10-14 | Atmospheric & Space-Weather Council | Refined STAC/graph alignment for solar activity; added telemetry schema v2. |
| v11.2.0  | 2025-08-01 | Atmospheric & Space-Weather Council | Initial v11 space-weather domain skeleton.                   |

---

<div align="center">

🛰️ **KFM v11 — Space-Weather Data Domain**  
Heliophysics-Aware Intelligence · Graph-Ready Events · FAIR+CARE-Aligned  

[📘 Data Index](../README.md) · [🌞 Solar Activity Module](solar-activity/README.md) · [⚖ Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>