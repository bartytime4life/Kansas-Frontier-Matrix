---
title: "🛰️ Kansas Frontier Matrix — Space-Weather Event Logs"
path: "docs/events/space-weather/README.md"
version: "v11.2.6"
last_updated: "2025-12-10"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Space Weather & Solar-Terrestrial Committee"
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
  domain: "space-weather-events"
  applies_to:
    - "docs/events/space-weather/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
indigenous_rights_flag: false
data_steward: "Space Weather & Solar-Terrestrial Committee"

ttl_policy: "24 months"
sunset_policy: "Superseded by next space-weather events README version"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"
signature_ref: "../../../releases/v11.2.6/signature.sig"

telemetry_ref: "../../../releases/v11.2.6/space-weather-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/space-weather-v1.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

story_node_refs: []
immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:events:space-weather:readme:v11.2.6"
semantic_document_id: "kfm-space-weather-events-readme-v11.2.6"

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

# 🛰️ Kansas Frontier Matrix — Space-Weather Event Logs  

Define conventions, structure, and governance for **space-weather event Markdown files**:

- solar flares and radiation storms  
- geomagnetic storms and Kp spikes  
- radio blackouts, GNSS degradation, ionospheric disturbances  
- upstream alerts and status changes from space-weather providers  

that materially affect the KFM pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode

This README is the **parent standard** for all space-weather event folders and files under `docs/events/space-weather/`.

---

## 🗂️ Directory Layout

~~~text
📁 Kansas-Frontier-Matrix/
└── 📁 docs/
    └── 📁 events/
        ├── 📄 README.md                               # 🧭 Event→Action Map (global routing runbook)
        ├── 📁 remote-sensing/ 📡                      # Remote-sensing events (imagery, radar, etc.)
        │   └── 📄 README.md
        └── 📁 space-weather/ 🌞
            ├── 📄 README.md                           # 🛰️ This document — space-weather event standard
            ├── 📁 solar/ 🌞                           # Solar flares, CMEs, radiation storms
            │   ├── 📄 README.md                       # Solar event standard
            │   └── 📄 YYYY-MM-DD-solar-*.md           # Solar event logs (e.g., X-class flares)
            ├── 📁 geomagnetic/ 🧲                     # Geomagnetic storms, Kp/Ap events
            │   ├── 📄 README.md                       # Geomagnetic event standard
            │   └── 📄 YYYY-MM-DD-geomagnetic-*.md     # Geomagnetic storm logs
            ├── 📁 ionosphere/ 📡                      # Ionospheric disturbances, GNSS impacts
            │   ├── 📄 README.md                       # Ionosphere event standard
            │   └── 📄 YYYY-MM-DD-ionosphere-*.md      # Ionospheric event logs
            ├── 📁 radio/ 📻                           # Radio blackouts, HF/VHF impacts
            │   ├── 📄 README.md                       # Radio event standard
            │   └── 📄 YYYY-MM-DD-radio-*.md           # Radio blackout logs
            └── 📁 misc/ 🧩                            # Other or cross-category space-weather events
                └── 📄 YYYY-MM-DD-space-weather-*.md   # Generic or multi-channel events
~~~

**Directory rules**

- Category-specific folders (e.g., `solar`, `geomagnetic`) MAY define their own `README.md` that **specializes but does not contradict** this standard.  
- Event docs MUST live in an appropriate category folder; cross-category events MAY use `misc/` or a reviewed dedicated folder.  
- New top-level subdirectories under `docs/events/space-weather/` require **Space Weather & Solar-Terrestrial Committee** review.  

---

## 📘 Overview & Scope

This README governs all **space-weather event docs** under:

- `docs/events/space-weather/**/*.md`

These documents record **space-weather conditions and alerts** that affect:

- reliability and latency of remote-sensing and communications feeds used by KFM  
- STAC Collections/Items and DCAT Datasets whose quality is space-weather dependent  
- Neo4j event and incident graph structures related to space-weather impacts  
- API responses and data-availability flags for impacted products  
- Story Nodes and Focus Mode timelines describing solar–terrestrial narrative over Kansas  

Event types include (non-exhaustive):

- **Solar events** — flares, CMEs, energetic particle events (SEPs)  
- **Geomagnetic storms** — Kp/Ap spikes, G1–G5 storm classifications  
- **Radio/ionospheric events** — HF/VHF blackouts, GNSS degradation, TEC anomalies  
- **Space-weather alerts** — NOAA SWPC, ESA, or other upstream warnings  

Space-weather event docs are **governed, human-readable log entries** that other layers (STAC, DCAT, Neo4j, Story Nodes) derive from.

---

## 📦 Data & Metadata Conventions

### File Naming

Category-specific READMEs may refine patterns; at this level:

- This file is always:
  - `docs/events/space-weather/README.md`  
- Category-specific events (inside their folder) SHOULD follow:
  - `YYYY-MM-DD-<category>-<short-slug>.md`  

Where:

- `YYYY-MM-DD` — official event posting date (UTC)  
- `<category>` — e.g. `solar`, `geomagnetic`, `ionosphere`, `radio`, `space-weather`  
- `<short-slug>` — concise hyphenated descriptor, e.g. `g3-storm`, `x1-1-flare`, `gnss-degradation`  

### Required Front Matter (Event Files — Base Pattern)

Category-specific READMEs may extend, but MUST respect this base pattern:

~~~yaml
title: "🛰️ Kansas Frontier Matrix — <Category> Space-Weather Event: <Short Title>"
path: "docs/events/space-weather/<category>/YYYY-MM-DD-<category>-<short-slug>.md"
version: "v11.2.x"
last_updated: "YYYY-MM-DD"

release_stage: "Stable / Governed"
lifecycle: "Event Record"
status: "Active / Informational · External Event Log"
doc_kind: "Event Summary · Space Weather"

provider: "<upstream-organization>"     # e.g., NOAA SWPC, ESA, NASA
space_weather_category: "<sw-category>" # e.g., solar-flare | cme | geomagnetic-storm | radio-blackout | ionospheric-disturbance

event_kind: "space-weather"             # domain tag; optionally pair with routing_event_kind for Event→Action
routing_event_kind: null                # optional: product-availability | reprocessing | algorithm-change | mission-status
event_id: "space-weather:event:YYYY-MM-DD:<short-slug>"

event_start: "YYYY-MM-DDThh:mm:ssZ"
event_posted: "YYYY-MM-DD"
event_end: null                         # null until resolved

affected_regions:
  - "Kansas"
  - "Great Plains"
affected_systems:
  - "gnss"
  - "hf-radio"
  - "satcom"

severity: "moderate"                    # low | moderate | high | extreme
noaa_scale:
  g_scale: null                         # G1–G5 (geomagnetic)
  s_scale: null                         # S1–S5 (solar radiation)
  r_scale: null                         # R1–R5 (radio blackout)

upstream_reference_url: "https://example.swpc.noaa.gov/..."
upstream_bulletin_id: null

markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"
license: "CC-BY 4.0"
~~~

Additional fields are allowed but MUST NOT conflict with these keys or contradict category-specific standards.

### Body Structure (Event Files)

Event docs SHOULD follow a structure that is easy to transform into Story Nodes and graph entities:

1. **📘 Overview** — concise description of the event and its importance  
2. **🌞 Event Summary** — indices, scales (Kp, G/S/R), upstream bulletins, classification  
3. **🌍 Spatial & Temporal Extent** — global vs regional relevance, Kansas impact window  
4. **⚙️ ETL & Pipeline Impact** — ingestion delays, increased error rates, degraded observations  
5. **🔗 STAC / DCAT / PROV Integration** — how catalogs/provenance encode the event  
6. **🧭 Neo4j & Story Node Integration** — event nodes, relationships, narrative hooks  
7. **📊 Telemetry & Validation** — metrics that corroborate the event (latency, error spikes, quality flags)  
8. **🤝 Sovereignty & FAIR+CARE Considerations** — ethical and sovereignty notes  
9. **📝 Version History** — event record edits  
10. **🏛️ Governance Footer** — compliance and CI requirements  

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

For each space-weather event, KFM SHOULD create STAC Items under a space-weather event collection:

- Collections:
  - `kfm-space-weather-events` (global), and/or  
  - category-specific collections (e.g., `kfm-geomagnetic-events`)  

STAC Item conventions:

- `id` SHOULD equal `event_id`  
- geometry:
  - often global or hemisphere-scale; for KFM use:
    - Kansas bounding box when focusing on local impact  
    - generalized polygons when global but still relevant  
- temporal:
  - `properties.datetime` = `event_start`  
  - optional `properties.start_datetime` / `properties.end_datetime`  

Recommended properties:

- `kfm:event_kind = "space-weather"`  
- `kfm:space_weather_category`  
- `kfm:severity`, `kfm:noaa_scale` (if applicable)  
- `kfm:affected_regions`, `kfm:affected_systems`  
- `kfm:event_ref` (matching `event_id`)  
- `kfm:upstream_reference_url`  

Assets MAY include:

- `upstream_bulletin` — snapshot of NOAA/ESA/NASA bulletins  
- `event_markdown` — rendered HTML or source Markdown for this event doc  

STAC JSON SHOULD live under:

- `data/stac/events/space-weather/<category>/<event-id>.json`

and must pass `KFM-STAC v11` validation in CI.

### DCAT

Each space-weather event SHOULD be represented as a `dcat:Dataset`:

- `dct:title` — event title  
- `dct:description` — overview and impact summary  
- `dct:temporal` — start/end interval  
- `dct:spatial` — Kansas or larger AOI, as appropriate  
- `dct:publisher` — KFM / Space Weather & Solar-Terrestrial Committee  
- `dcat:keyword` — `space-weather`, `geomagnetic-storm`, etc.  
- `dcat:distribution` — links to:
  - Markdown source  
  - rendered HTML  
  - event STAC Items  

### PROV-O

Treat space-weather events as:

- `prov:Entity` — the canonical event record (Markdown + derived catalogs)  
- `prov:Activity` — the physical/operational phenomenon (solar event, storm, blackout)  
- `prov:Agent` — upstream providers (e.g., NOAA SWPC) and KFM committees  

Conceptual PROV pattern:

~~~text
Entity:   space-weather:event:YYYY-MM-DD:<short-slug>
Agent:    NOAA SWPC / ESA / NASA / KFM Space Weather & Solar-Terrestrial Committee
Activity: space-weather:solar-geomagnetic-phenomenon
Started:  event_start
Ended:    event_end (null if ongoing)
Status:   ongoing | resolved
~~~

PROV bundles are ingested into Neo4j and connected to affected datasets, regions, and Story Nodes.

---

## 🧱 Position in the KFM Pipeline

Space-weather event docs inform and constrain:

1. **ETL & Orchestration**  
   - Prefect 3 / Airflow 3 flows and DAGs can:
     - distinguish **space-weather-driven anomalies** from ordinary outages  
     - adjust backoff, retries, or ingest cadence during severe events  
     - tag ETL runs with `space_weather_event_id` for later analysis  

2. **STAC/DCAT/PROV Catalogs**  
   - event-aware collections/items and datasets provide:
     - explicit context when observations are degraded or delayed  
     - clear links between environmental data and space-weather conditions  

3. **Neo4j Graph**  
   - nodes like `:SpaceWeatherEvent` with properties:
     - `event_id`, `space_weather_category`, `severity`, `noaa_scale`  
   - relationships:
     - `(:SpaceWeatherEvent)-[:AFFECTS_MISSION]->(:Mission)`  
     - `(:SpaceWeatherEvent)-[:AFFECTS_REGION]->(:Region)`  
     - `(:SpaceWeatherEvent)-[:AFFECTS_DATASET]->(:Dataset)`  

4. **API**  
   - endpoints can surface:
     - flags indicating data intervals overlapping severe space-weather events  
     - explanatory context next to quality metrics or latency  

5. **Frontend (React / MapLibre / Cesium)**  
   - overlays and timeline markers show:
     - G-scale/S-scale/R-scale periods  
     - GNSS degradation intervals  
     - cross-links to affected environmental layers  

6. **Story Nodes & Focus Mode**  
   - narratives explaining:
     - why certain RS products are degraded during specific intervals  
     - links between geomagnetic storms and downstream hydrology, power, comms, or observational gaps  

---

## 🧪 Validation & CI/CD

Changes under `docs/events/space-weather/**` SHOULD trigger CI workflows that:

- run markdown linting and internal link checks  
- validate front-matter schemas for:
  - this README  
  - category-specific READMEs  
  - event docs  
- check compliance with **KFM-MDP v11.2.6**:
  - directory layout section present  
  - version history section present  
  - governance footer present  
- validate STAC event artifacts for `KFM-STAC v11` compliance  
- validate DCAT metadata where applicable (`KFM-DCAT v11`)  
- run security/secret scans:
  - no credentials  
  - no PII  
  - no sensitive infrastructure topology  

Example workflow:

- `.github/workflows/docs-events-space-weather.yml`

must block merges on any validation failure.

---

## 🧠 Story Nodes & Focus Mode Integration

Space-weather events are first-class drivers for Story Nodes that explain:

- **Why** certain data intervals (GNSS, radar, remote-sensing) show degraded quality or gaps.  
- **When** severe events (e.g., G3+ storms) coincide with other environmental phenomena in Kansas.  

Each space-weather event doc SHOULD support at least one Story Node with:

- title and short, fact-based narrative  
- spatial extent (global/hemisphere, with explicit Kansas view)  
- temporal extent (start/end times)  
- links to:
  - space-weather event STAC/DCAT entities  
  - affected missions/datasets in the graph  

Story Nodes MUST clearly separate:

- **facts** — bulletins, indices, cataloged impacts  
- **interpretation** — KFM’s reading of how space weather affects local data and infrastructure  
- **speculation** — hypotheses about longer-term effects or interactions  

Focus Mode uses this structure to:

- overlay space-weather events on data availability maps  
- drive temporal filters and contextual tooltips  
- support richer Kansas space-weather narratives.

---

## ⚖ FAIR+CARE, Sovereignty & Ethics

Space-weather event docs typically describe global physical phenomena and operational context:

- generally **public, low-risk**, but still subject to:
  - FAIR (findable, accessible, interoperable, reusable)  
  - CARE (Collective benefit, Authority to control, Responsibility, Ethics) principles  

Constraints:

- MUST NOT disclose:
  - sensitive infrastructure topologies  
  - internal-only operational configurations of third parties  
- When events are used to interpret impacts on:
  - Indigenous lands  
  - culturally significant sites  
  narrative sections MUST:
    - generalize spatial references  
    - avoid exposing restricted locations or knowledge  
    - reference `sovereignty_policy` and any local agreements  

Licensing:

- event docs: `CC-BY 4.0`  
- upstream data/bulletins: governed by provider licenses (e.g., NOAA SWPC policies) and MUST be respected.  

Key governance references:

- `docs/standards/governance/ROOT-GOVERNANCE.md`  
- `docs/standards/faircare/FAIRCARE-GUIDE.md`  
- `docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`  

---

## 🕰️ Version History

| Version | Date       | Summary                                                          |
|--------:|-----------:|------------------------------------------------------------------|
| v11.2.6 | 2025-12-10 | Initial v11.2.6-aligned README for space-weather events.         |

---

<sub>© Kansas Frontier Matrix · CC‑BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM‑MDP v11.2.6</sub>

<br/>

<div align="center">

🛰️ **Kansas Frontier Matrix — Space-Weather Event Logs v11.2.6**  
Solar–Terrestrial Narratives · Catalog–Graph Harmony · FAIR+CARE Governance  

[📘 Docs Root](../../README.md) · [🧭 Event→Action Map](../README.md) · [📡 Remote-Sensing Events](../remote-sensing/README.md) · [📚 Standards Index](../../standards/README.md) · [⚖ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md)

</div>