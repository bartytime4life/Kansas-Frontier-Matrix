---
title: "🛰️ Kansas Frontier Matrix — Remote-Sensing Event Logs"
path: "docs/events/remote-sensing/README.md"
version: "v11.2.6"
last_updated: "2025-12-10"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Remote Sensing & Earth Observation Committee"
content_stability: "stable"
status: "Active / Standard"
doc_kind: "Guide"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "remote-sensing-events"
  applies_to:
    - "docs/events/remote-sensing/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
indigenous_rights_flag: false
data_steward: "Remote Sensing & Earth Observation Committee"

ttl_policy: "24 months"
sunset_policy: "Superseded by next remote-sensing events README version"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"
signature_ref: "../../../releases/v11.2.6/signature.sig"

telemetry_ref: "../../../releases/v11.2.6/earth-observation-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/earth-observation-v3.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

story_node_refs: []
immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:events:remote-sensing:readme:v11.2.6"
semantic_document_id: "kfm-remote-sensing-events-readme-v11.2.6"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
---

# 🛰️ Kansas Frontier Matrix — Remote-Sensing Event Logs  

Define conventions, structure, and governance for **remote-sensing event Markdown files**:

- availability interruptions  
- reprocessing campaigns  
- algorithm changes  
- mission-status events  

that impact the KFM pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode

This README is the **parent standard** for all sensor-specific event folders (Landsat, Sentinel‑2, MODIS, VIIRS, radar, and orchestration-related RS events) under `docs/events/remote-sensing/`.

---

## 🗂️ Directory Layout

~~~text
📁 Kansas-Frontier-Matrix/
└── 📁 docs/
    └── 📁 events/
        ├── 📄 README.md                               # 🧭 Event→Action Map (global routing runbook)
        └── 📁 remote-sensing/ 📡
            ├── 📄 README.md                           # 🛰️ This document (remote-sensing event standard)
            ├── 📄 2025-12-10-remote-sensing-event.md  # 📡 Example RS event summary
            ├── 📄 stac-telemetry-overview.md          # 📡 STAC telemetry spec (freshness, energy, SLO)
            │
            ├── 📁 orchestration/ ⚙️                   # Remote-sensing orchestration patterns & events
            │   ├── 📄 README.md                       # RS orchestration index (Prefect/Airflow patterns)
            │   └── 📁 prefect-airflow/ 🛰️
            │       └── 📄 README.md                   # Prefect 3 & Airflow 3 RS orchestration patterns
            │
            ├── 📁 landsat/ 🛰️                         # Landsat-specific events
            │   ├── 📄 README.md                       # Landsat event standard
            │   └── 📄 YYYY-MM-DD-landsat-*.md         # Landsat event logs
            ├── 📁 sentinel-2/ 🛰️                      # Sentinel-2-specific events
            │   ├── 📄 README.md                       # Sentinel-2 event standard
            │   └── 📄 YYYY-MM-DD-sentinel-2-*.md      # Sentinel-2 event logs
            ├── 📁 modis/ 🌍                           # MODIS-specific events
            │   ├── 📄 README.md                       # MODIS event standard
            │   └── 📄 YYYY-MM-DD-modis-*.md           # MODIS event logs
            ├── 📁 viirs/ 🌌                           # VIIRS-specific events
            │   ├── 📄 README.md                       # VIIRS event standard
            │   └── 📄 YYYY-MM-DD-viirs-*.md           # VIIRS event logs
            └── 📁 misc/ 🧩                            # Other or cross-sensor events
                └── 📄 YYYY-MM-DD-remote-*.md          # Generic or multi-sensor events
~~~

**Directory rules**

- Sensor-specific folders (e.g., `landsat`, `sentinel-2`) MAY define their own `README.md` that **specializes but does not contradict** this standard.  
- Event docs MUST live in a sensor-appropriate folder; cross-sensor events MAY use `misc/` or a dedicated folder after committee approval.  
- New top-level subdirectories under `docs/events/remote-sensing/` require **Remote Sensing & Earth Observation Committee** review.  

---

## 📘 Overview & Scope

This README governs all **remote-sensing event docs** under:

- `docs/events/remote-sensing/**/*.md`

These documents record **upstream provider events** that affect:

- ingestion of satellite/airborne products in KFM ETL  
- STAC Collections/Items and DCAT Datasets derived from those products  
- Neo4j event and incident graph structures  
- API responses and data-availability flags  
- Story Nodes and Focus Mode timelines for Earth-observation narratives over Kansas  

Event types include, but are not limited to:

- product-availability interruptions and outages  
- bulk reprocessing campaigns and calibration updates  
- algorithm or product-definition changes  
- mission-status events that alter coverage, cadence, or latency  
- orchestration-side incidents specifically impacting remote-sensing ETL (via Prefect 3 / Airflow 3)  

Remote-sensing event docs are **governed log entries** that other layers (STAC, DCAT, Neo4j, Story Nodes) derive from—not the other way around.

---

## 📦 Data & Metadata Conventions

### File Naming (Sensor Events)

Sensor-specific READMEs may refine patterns, but at this level:

- This file is always:
  - `docs/events/remote-sensing/README.md`  
- Sensor-specific events (inside their sensor folder) SHOULD follow:
  - `YYYY-MM-DD-<sensor>-<short-slug>.md`  

Where:

- `YYYY-MM-DD` — official event posting date (UTC)  
- `<sensor>` — e.g. `landsat`, `sentinel-2`, `modis`, `viirs`, `nexrad`  
- `<short-slug>` — concise hyphenated descriptor, e.g. `tiling-outage`, `l2-reprocessing`, `calibration-update`  

### File Naming (Cross-Sensor / Generic Events)

- Under `misc/`:
  - `YYYY-MM-DD-remote-<short-slug>.md`  

### Required Front Matter (Event Files — Base Pattern)

Sensor-specific READMEs may extend, but MUST respect this base pattern:

~~~yaml
title: "🛰️ Kansas Frontier Matrix — <Sensor> Remote-Sensing Event: <Short Title>"
path: "docs/events/remote-sensing/<sensor>/YYYY-MM-DD-<sensor>-<short-slug>.md"
version: "v11.2.x"
last_updated: "YYYY-MM-DD"

release_stage: "Stable / Governed"
lifecycle: "Event Record"
status: "Active / Informational · External Event Log"
doc_kind: "Event Summary · Remote Sensing"

provider: "<upstream-organization>"
missions:
  - "<mission-name>"

event_kind: "<kind>"    # product-availability | reprocessing | algorithm-change | mission-status | orchestration
event_id: "<sensor>:event:YYYY-MM-DD:<short-slug>"
event_start: "YYYY-MM-DDThh:mm:ssZ"
event_posted: "YYYY-MM-DD"
event_end: null          # null until resolved

affected_products:
  - "<sensor>-L1"
  - "<sensor>-L2"

severity: "low"          # low | moderate | high | critical

upstream_reference_url: "https://example.provider.org/..."
upstream_ticket_id: null

markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"
license: "CC-BY 4.0"
~~~

Additional fields are allowed but MUST NOT conflict with these keys or contradict sensor-specific standards.

### Body Structure (Event Files)

Event docs SHOULD follow a structure that is easy to convert into Story Nodes and graph entities:

1. **📘 Overview** — concise narrative of what happened and why it matters  
2. **🛰️ Event Summary** — missions/sensors, temporal window, affected products, upstream summary  
3. **🌍 Spatial & Temporal Extent** — AOIs, tiles, bounding boxes, start/end times  
4. **⚙️ ETL & Pipeline Impact** — ingestion, validation, backfill/reprocessing behavior  
5. **🔗 STAC / DCAT / PROV Integration** — how catalogs and provenance are updated  
6. **🧭 Neo4j & Story Node Integration** — event nodes, relationships, narrative hooks  
7. **📊 Telemetry & Validation** — which telemetry files/series corroborate the event  
8. **🤝 Sovereignty & FAIR+CARE Considerations** — ethical and sovereignty aspects  
9. **📝 Version History** — versioned edits to the event record  
10. **🏛️ Governance Footer** — compliance, reviewers, CI/validation requirements  

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

For each remote-sensing event, KFM SHOULD create at least one STAC Item in an events-focused collection:

- collections:
  - `kfm-remote-sensing-events` (global), and/or  
  - sensor-specific collections (`kfm-landsat-events`, `kfm-sentinel-2-events`, etc.)  
- STAC Item conventions:
  - `id` SHOULD equal `event_id`  
  - geometry: Kansas-wide bounding box, or more constrained AOI where appropriate  
  - temporal:
    - `properties.datetime` = `event_start`  
    - optionally `properties.start_datetime` / `properties.end_datetime`  

Properties SHOULD include:

- `kfm:event_kind`  
- `kfm:affected_products`  
- `kfm:severity`  
- `kfm:upstream_reference_url`  
- `kfm:event_ref` (matching `event_id`)  

Assets MAY include:

- `upstream_notice` — snapshot of provider notice  
- `event_markdown` — rendered HTML or source Markdown for this event doc  

STAC files SHOULD live under:

- `data/stac/events/remote-sensing/<sensor>/<event-id>.json`

and must pass STAC validation in CI.

### DCAT

Each remote-sensing event SHOULD be described as a `dcat:Dataset`:

- `dct:title` — event title  
- `dct:description` — overview section content  
- `dct:temporal` — event interval (start/end)  
- `dct:spatial` — Kansas or AOI extent  
- `dct:publisher` — KFM / responsible committee  
- `dcat:distribution` — links to:
  - Markdown source  
  - rendered HTML  
  - STAC Item(s)  

### PROV-O

Treat each event as:

- `prov:Entity` — the **event record** (this Markdown + derived catalogs)  
- `prov:Activity` — the upstream maintenance/change or data-generation activity  
- `prov:Agent` — upstream provider and KFM committee  

Minimal conceptual pattern:

~~~text
Entity:   <sensor>:event:YYYY-MM-DD:<short-slug>
Agent:    <provider> and KFM Remote Sensing & EO Committee
Activity: <provider>:system-maintenance-or-change
Started:  event_start
Ended:    event_end (null if ongoing)
Status:   ongoing | resolved
~~~

These PROV entities are ingested into Neo4j and linked to impacted collections, datasets, regions, and Story Nodes.

---

## 🧱 Position in the KFM Pipeline

Remote-sensing event docs influence:

1. **ETL (Prefect 3 / Airflow 3 / other orchestrators)**  
   - schedulers treat missing or late scenes as **expected missingness** when annotated by events  
   - drive reprocessing and backfill DAGs for impacted missions  

2. **STAC/DCAT/PROV catalogs**  
   - generate event-focused STAC Items and DCAT Datasets  
   - annotate mission collections and product lines with event metadata  

3. **Neo4j**  
   - nodes like `:RemoteSensingEvent` annotated with `event_kind`, `severity`, `event_id`  
   - relationships:
     - `(:RemoteSensingEvent)-[:AFFECTS_DATASET]->(:Dataset)`  
     - `(:RemoteSensingEvent)-[:AFFECTS_REGION]->(:Region)`  

4. **API**  
   - API responses include event references near coverage and data-quality fields  
   - clients can filter data by event intervals or severity  

5. **Frontend (React / MapLibre / Cesium)**  
   - overlays, banners, and timeline markers explain gaps, reprocessing windows, and algorithm transitions  

6. **Story Nodes & Focus Mode**  
   - storylines describing:
     - outages (e.g., Sentinel-2 tiling issues)  
     - algorithm changes (new atmospheric correction)  
     - reprocessing campaigns (Landsat surface reflectance revisions)  

---

## 🧪 Validation & CI/CD

Changes under `docs/events/remote-sensing/**` SHOULD trigger CI workflows that:

- run markdown linting and internal link checks  
- validate front-matter schemas for:
  - this README  
  - sensor-specific READMEs  
  - event docs  
- validate KFM-MDP v11.2.6 compliance:
  - directory layout section present  
  - version history section present  
  - governance footer present  
- run STAC validation for any generated/updated event STAC Items  
- run basic DCAT JSON-LD validation where applicable  
- run security/secret scans to ensure:
  - no credentials  
  - no PII  
  - no restricted location details  

Example workflow:

- `.github/workflows/docs-events-remote-sensing.yml`

must block merges on any validation failure.

---

## 🧠 Story Node & Focus Mode Integration

Remote-sensing events are primary drivers for Story Nodes that explain:

- why Landsat, Sentinel-2, MODIS, VIIRS, radar, or model-linked remote-sensing series have gaps or unusual patterns  
- when reprocessing or algorithm changes may alter derived metrics (e.g. NDVI, burn indices, drought indicators)  

Each event doc SHOULD enable at least one Story Node per sensor/event, with:

- title, short narrative text (facts only)  
- spatial extent  
- temporal extent  
- links to:
  - event STAC Items and DCAT Datasets  
  - Neo4j event and dataset nodes  

Story Nodes MUST clearly separate:

- **facts** — directly supported by catalogs, telemetry, and provenance  
- **interpretation** — Remote Sensing & EO Committee analysis  
- **speculation** — hypotheses or future work  

Focus Mode uses this information to differentiate **data-driven patterns** from **pipeline- or provider-driven anomalies**.

---

## ⚖ FAIR+CARE, Sovereignty & Ethics

Remote-sensing event docs usually describe **operational meta-information** and are low risk, but:

- MUST NOT include sensitive coordinates or internal-only operational details from providers.  
- When events intersect **Indigenous lands or sensitive cultural/archaeological contexts**, impact sections MUST:
  - generalize spatial descriptions  
  - avoid exposing restricted locations or knowledge  
  - reference `sovereignty_policy` and relevant agreements.  

Licensing:

- event docs: `CC-BY 4.0` (this README and event Markdown files)  
- underlying data: governed by provider licenses (USGS, NASA, ESA, etc.) and MUST be respected.  

Key governance references:

- `docs/standards/governance/ROOT-GOVERNANCE.md`  
- `docs/standards/faircare/FAIRCARE-GUIDE.md`  
- `docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`  

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                         |
|--------:|-----------:|-------------------------------------------------------------------------------------------------|
| v11.2.6 | 2025-12-10 | Initial v11.2.6-aligned README for remote-sensing events; parent standard for sensor-specific event directories. |

---

<sub>© Kansas Frontier Matrix · CC‑BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM‑MDP v11.2.6</sub>

<br/>

<div align="center">

🛰️ **Kansas Frontier Matrix — Remote-Sensing Event Logs v11.2.6**  
Deterministic EO Event Logging · Catalog–Graph Harmony · FAIR+CARE Governance  

[📘 Docs Root](../../README.md) · [🧭 Event→Action Map](../README.md) · [⚙ RS Orchestration Index](./orchestration/README.md) · [📚 Standards Index](../../standards/README.md) · [⚖ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md)

</div>