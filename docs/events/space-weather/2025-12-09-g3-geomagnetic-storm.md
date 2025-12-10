---
title: "🌌 Kansas Frontier Matrix — Geomagnetic Storm Event Briefing (G3 Watch · Dec 9 2025)"
path: "docs/events/space-weather/2025-12-09-g3-geomagnetic-storm.md"
version: "v11.2.5"
last_updated: "2025-12-10"

release_stage: "Stable / Observational Record"
lifecycle: "Long-Term Reference"
review_cycle: "Annual · Environmental & Space Weather Steering Group"
content_stability: "stable"

status: "Active / Published"
doc_kind: "Environmental / Space Weather Event Record"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<sha256-prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.5/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.5/manifest.zip"
telemetry_ref: "../../../releases/v11.2.5/space-weather-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/space-weather-v2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "space-weather"
  applies_to:
    - "geomagnetic-storm"
    - "g3-watch"
    - "space-weather-events"
    - "instrumentation-annotations"
    - "power-grid-telemetry-links"
    - "story-nodes"
    - "focus-mode"

semantic_intent:
  - "space-weather-event-record"
  - "instrument-error-annotation"
  - "cross-domain-environmental-perturbation"
  - "governed-story-node-source"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "Space weather (non-sensitive)"
sensitivity_level: "None"
public_exposure_risk: "Low"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:events:space-weather:g3-watch-2025-12-09:v11.2.5"
semantic_document_id: "kfm-event-space-weather-g3-watch-2025-12-09-v11.2.5"
event_source_id: "ledger:events:space-weather:g3-watch-2025-12-09:v11.2.5"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "footer-check"
  - "accessibility-check"
  - "diagram-check"
  - "metadata-check"
  - "provenance-check"
  - "secret-scan"
  - "pii-scan"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"
---

<div align="center">

# 🌌 **Geomagnetic Storm Event Briefing — G3 Watch (Dec 9 2025)**  
`docs/events/space-weather/2025-12-09-g3-geomagnetic-storm.md`

**Purpose**  
Provide a governed, provenance-complete record of the **Strong (G3) Geomagnetic Storm Watch** on **Dec 9 2025**, and define how this event is represented across the KFM pipeline:  

**Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode.** :contentReference[oaicite:0]{index=0}  

This record is used to annotate potential **instrument error envelopes**, **remote-sensing artifacts**, and **space-weather-related risks** for Kansas-centric research domains (hydrology, ecology, archaeology, infrastructure, and cultural heritage). :contentReference[oaicite:1]{index=1}  

</div>

---

## 📘 Overview

On **2025‑12‑06**, an **M8.1 solar flare** launched a **fast, Earth-directed full‑halo CME**, leading NOAA SWPC to issue a **Strong (G3) Geomagnetic Storm Watch** for **2025‑12‑09**. Arrival windows and magnetic field orientation were uncertain, but strong geomagnetic disturbances were plausible for several multi‑hour intervals.

For Kansas Frontier Matrix, this event functions as a **cross-domain “umbrella annotation”**: a bounded time window during which we expect elevated **magnetospheric and ionospheric perturbations** that may influence:

- GNSS/GPS accuracy and drift corrections used in field archaeology and hydrology campaigns :contentReference[oaicite:2]{index=2}  
- Satellite-derived rasters and atmospheric reanalyses used in ecological and climate studies :contentReference[oaicite:3]{index=3}  
- Power‑grid and communications telemetry linked to Kansas infrastructure and historical narratives :contentReference[oaicite:4]{index=4}  

This event record is **descriptive**, not predictive: it captures what was forecast/observed and how KFM should mark affected data, without asserting new physical science beyond source bulletins.

---

## 🗂️ Directory Layout

~~~text
docs/
└── events/
    └── space-weather/
        └── 2025-12-09-g3-geomagnetic-storm.md   # This file (governed event record)
~~~

This Markdown file is the **human-facing narrative** companion to machine-readable metadata:

- DCAT/STAC/PROV records under `data/stac/` and `data/catalog/space-weather/` (see below)  
- Graph ingestion configs under `src/graph/ingest/space-weather/`  
- ETL/validation configs under `src/pipelines/atmo/space-weather/`  

All such assets are documented-first under the **Master Coder Protocol 2.0**. :contentReference[oaicite:5]{index=5}  

---

## 🧭 Context

### 🛰 Space-Weather Event Snapshot

- **Phenomenon:** Full-halo CME following M8.1 solar flare  
- **Source Region:** NOAA‑designated active region (per SWPC reports)  
- **CME Type:** Fast, Earth-directed, full-halo  
- **Forecast Severity:** G3 — *Strong Geomagnetic Storm*  
- **Forecast Validity Window:** **2025‑12‑09** (UTC), with possible spillover into adjacent UT days  
- **Primary Impacts Considered by KFM:**  
  - Satellite drag and orbital perturbations affecting LEO platform ephemerides  
  - HF radio and GNSS/GPS positioning degradation  
  - Expansion of auroral oval toward mid‑latitudes, including possible visibility in or near Kansas  
  - Increased risk envelopes for transformer loading, reactive power swings, and voltage regulation issues in regional grids  
  - Elevated noise in ionosphere‑sensitive remote sensing, including some atmospheric products used in KFM climate/ecology layers :contentReference[oaicite:6]{index=6}  

### 🌾 Kansas-Focused Relevance

Kansas has a long history of **environmental extremes** (drought, Dust Bowl, severe storms) that KFM documents as part of its historical-environmental tapestry. :contentReference[oaicite:7]{index=7}  This G3 watch extends that story into **near‑Earth space**, providing:

- A time‑bounded **“annotation window”** for Kansas‑centric datasets (gauges, radars, remote sensing)  
- A cross‑cutting context layer that sits alongside droughts, floods, and major storms in the KFM event timeline :contentReference[oaicite:8]{index=8}  

---

## 📦 Data & Metadata

### 🗃 DCAT Dataset & DatasetSeries

The event is represented as a **DCAT dataset**:

- `dcat:Dataset` — `kfm:space-weather-event-g3-2025-12-09`  
- Belongs to a `dcat:DatasetSeries` for **space-weather events 2025** (e.g., `kfm:space-weather-events-2025-series`)  

Key DCAT fields:

- `dct:title`: "G3 Geomagnetic Storm Watch — 2025‑12‑09"  
- `dct:description`: Structured summary aligned with this Markdown record  
- `dct:temporal`: [2025‑12‑06T00:00Z, 2025‑12‑10T23:59Z] (flare → decay window)  
- `dct:spatial`: Kansas‑wide envelope (generalized polygon / bbox)  
- `dcat:distribution`:  
  - Links to archived NOAA SWPC bulletins and Kp/Dst indices (where redistributable)  
  - Links to internal KFM JSON/JSON‑LD event object used by ETL and graph ingestion  

Versioning uses **DCAT 3.0** dataset series and version properties to track updates if NOAA revises assessments. :contentReference[oaicite:9]{index=9}  

### 🛰 STAC Items & Collections

When KFM ingests **space-weather‑impacted raster products** (e.g., auroral imagery, magnetometer grids, ionospheric maps), each derived asset is described as a **STAC Item** within a `space-weather` or `atmo-events` Collection:

- `collection`: `"kfm-space-weather-events"`  
- `properties.kfm:space_weather_event_id`: link back to this event’s `doc_uuid`  
- `properties.kfm:g_scale`: `"G3"`  
- `properties.kfm:storm_window_start` / `_end`  
- `assets` for rasters (e.g., auroral probability maps) and ancillary metadata  

This aligns space-weather assets with the broader KFM STAC strategy for environmental and Earth‑observation data. :contentReference[oaicite:10]{index=10} :contentReference[oaicite:11]{index=11}  

### 🧬 PROV-O Lineage

We treat this event as a **PROV entity** with explicit lineage:

- `prov:Entity` — `kfm:SpaceWeatherEvent_G3_2025_12_09`  
- `prov:wasGeneratedBy` — ingestion activity `kfm:Ingest_NOAA_SWPC_G3_2025_12_09`  
- `prov:wasAttributedTo` — `NOAA SWPC` (source) and `KFM Space-Weather ETL` (processing agent)  
- `prov:used` — specific NOAA bulletins, Kp/Dst time series, and summary products  

Where downstream datasets (e.g., Kansas magnetometer aggregates or GNSS error statistics) are flagged as affected, we add:

- `prov:wasInfluencedBy` → `kfm:SpaceWeatherEvent_G3_2025_12_09`  

This keeps **cause–effect traceable** from raw bulletins through ETL runs into final graph nodes and Story Nodes. :contentReference[oaicite:12]{index=12}  

### 🌐 GeoSPARQL & Spatial Semantics

Graph nodes for Kansas sensors, grids, and regions maintain **GeoSPARQL geometries** so the event can be spatially joined:

- `geo:Feature` — sensors, grids, counties, transmission corridors  
- `geo:Geometry` — generalized geometries (`geo:asWKT`, `geo:asGeoJSON`)  

Spatial joins (e.g., “all sensors within Kansas bounding geometry during event window”) use GeoSPARQL functions (`geof:sfWithin`, `geof:distance`) inside the KFM semantic access layer. :contentReference[oaicite:13]{index=13}  

---

## 🧱 Architecture

This event record participates in the **canonical KFM pipeline**:  

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j graph → API → React/MapLibre/Cesium → Story Nodes → Focus Mode. :contentReference[oaicite:14]{index=14} :contentReference[oaicite:15]{index=15}  

### 1️⃣ ETL (Deterministic & Config-Driven)

Location (normative):

- `src/pipelines/atmo/space-weather/noaa-swpc-g3/` (Python/Rust or similar)  
- Config: `configs/pipelines/space-weather/noaa-swpc-g3-2025-12-09.yaml`  

Responsibilities:

- Fetch relevant NOAA SWPC bulletins (watch issuance, updates, cancellation)  
- Normalize timestamps to UTC and KFM canonical time model (OWL‑Time aligned)  
- Compute a **canonical event window** and tag as `pre_event`, `main_phase`, `recovery`  
- Emit:  
  - DCAT dataset + DatasetSeries JSON‑LD  
  - STAC Collection/Items for any associated rasters  
  - PROV bundles for ingestion steps and derived annotations  

All ETL steps are **config‑first, deterministic, and fully re‑runnable**, following KFM’s ETL architecture standards. :contentReference[oaicite:16]{index=16}   

### 2️⃣ Catalogs: STAC / DCAT / PROV

Outputs land under:

- `data/catalog/space-weather/g3-2025-12-09.dcat.jsonld`  
- `data/stac/collections/space-weather-events.json`  
- `data/stac/items/space-weather/2025/2025-12-09-g3-event.json`  
- `data/prov/space-weather/2025-12-09-g3-event.prov.jsonld`  

These are validated in CI against **STAC 1.0.0**, **DCAT 3.0**, and **PROV‑O** schemas before merging. :contentReference[oaicite:18]{index=18} :contentReference[oaicite:19]{index=19} :contentReference[oaicite:20]{index=20}  

### 3️⃣ Graph (Neo4j / KFM-OP)

Core nodes and edges (draft schema, KFM‑OP‑aligned):

- `(:SpaceWeatherEvent { id, g_scale, kp_max, window_start, window_end })`  
- `(:SolarRegion { noaa_region_id })`  
- `(:Sensor { kind, operator, location })`  
- `(:Dataset { id, kind, temporal_extent, source })`  

Relationships:

- `(:SpaceWeatherEvent)-[:EMITTED_BY]->(:SolarRegion)`  
- `(:SpaceWeatherEvent)-[:AFFECTS_SENSOR]->(:Sensor)`  
- `(:SpaceWeatherEvent)-[:AFFECTS_DATASET]->(:Dataset)`  
- `(:SpaceWeatherEvent)-[:HAS_SEVERITY]->(:GeomagneticScale { code: "G3" })`  

These graph patterns align with KFM’s broader event and environmental modeling expansion. :contentReference[oaicite:21]{index=21}   

### 4️⃣ API & Frontend

API (normative):

- `src/api/events/space-weather/`  
  - `GET /events/space-weather` — search by date, severity, affected domains  
  - `GET /events/space-weather/{id}` — details, linked sensors/datasets  

Frontend:

- React + MapLibre/Cesium overlays showing:  
  - Event window on the timeline  
  - Optional **auroral visibility estimates** across North America  
  - A Kansas‑level “risk indicator” stripe for affected domains (GNSS, remote sensing, grid, archives)  

This extends KFM’s interactive map/timeline patterns to include space‑weather context. :contentReference[oaicite:23]{index=23} :contentReference[oaicite:24]{index=24}  

---

## 🧠 Story Node & Focus Mode Integration

This document is a **governed Story Node source** for Focus Mode.

### Story Node Template

- **Title:** `G3 Geomagnetic Storm Watch — 9 Dec 2025`  
- **Type:** `SpaceWeatherEventStoryNode`  
- **Spatial extent:**  
  - Primary: generalized Kansas bbox (no sensitive infrastructure detail)  
  - Secondary: optional continental auroral footprint in separate, non‑Kansas node  
- **Temporal extent:** `[2025‑12‑06T00:00Z, 2025‑12‑10T23:59Z]`  
- **Linked graph entities:**  
  - `SpaceWeatherEvent` node for this event  
  - Affected `Sensor` and `Dataset` nodes (by relationship)  
  - Relevant `HydrologicEvent`, `ClimateAnomaly`, `ArchaeologySurvey`, or `PowerGridAsset` nodes where overlaps exist :contentReference[oaicite:25]{index=25}  

### Fact / Interpretation / Speculation

Focus Mode renderers must clearly separate:

- **Facts**  
  - NOAA‑reported flare class, CME description, G‑scale watch issuances  
  - Observed geomagnetic indices (Kp, Dst), where available  

- **Interpretation** (KFM‑labeled)  
  - “During this interval, GNSS and remote‑sensing products may have elevated error envelopes; KFM marks these datasets accordingly.”  

- **Speculation (Disallowed by Default)**  
  - No claims about unobserved impacts (e.g., human behavior, specific infrastructure failures) may be auto‑generated.  

These rules follow KFM’s AI narrative and sovereignty safeguards for sensitive domains. :contentReference[oaicite:26]{index=26} :contentReference[oaicite:27]{index=27}  

---

## 🧪 Validation & CI/CD

KFM applies **CI/CD controls** to this event’s metadata and code, consistent with its broader DevSecOps practices. :contentReference[oaicite:28]{index=28}   

### Automated Checks

For any change touching this file or associated configs:

- **Markdown & Schema Linting**  
  - Validate YAML front‑matter against `kfm-markdown-protocol-v11.2.6` schema  
  - Enforce H2 heading and fencing rules (outer backticks, inner tildes) per KFM‑MDP v11.2.6 :contentReference[oaicite:30]{index=30}  

- **Data & Catalog Validation**  
  - STAC validation for `space-weather` Collections/Items  
  - JSON‑LD validation for DCAT and PROV records  
  - Graph schema checks for `SpaceWeatherEvent` label and relationships  

- **Security & Supply‑Chain**  
  - SBOM/SPDX verification for release artifacts  
  - Dependency scanning for ETL and API components  
  - SLSA‑style provenance attestations for event ingestion pipelines :contentReference[oaicite:31]{index=31}  

### Telemetry

CI stores results in `space-weather-telemetry.json`:

- Validation status for STAC/DCAT/PROV artifacts  
- CI job status for ETL and API components linked to this event  
- Energy/carbon estimates for related CI workloads (for sustainability tracking) :contentReference[oaicite:32]{index=32}  

---

## ⚖ FAIR+CARE & Governance

Although **space-weather data are non‑sensitive**, the *connections* we draw (e.g., to culturally sensitive sites or critical infrastructure) can have governance implications. :contentReference[oaicite:33]{index=33}   

### FAIR

- **Findable:** Event is indexed in DCAT catalog and Neo4j with stable IDs (`doc_uuid`, `semantic_document_id`). :contentReference[oaicite:35]{index=35}  
- **Accessible:** Public narrative in this Markdown file; machine‑readable JSON‑LD/GeoJSON exposed via KFM APIs. :contentReference[oaicite:36]{index=36}  
- **Interoperable:** STAC/DCAT/PROV/GeoSPARQL alignment ensures semantic reuse across tools and disciplines. :contentReference[oaicite:37]{index=37} :contentReference[oaicite:38]{index=38} :contentReference[oaicite:39]{index=39}  
- **Reusable:** Explicit license (CC‑BY 4.0), provenance chains, and schema references.   

### CARE & Indigenous Sovereignty

- No **sacred sites** or sensitive Indigenous locations are exposed with high precision solely due to this space‑weather event.  
- When linking to Indigenous heritage sites and archaeological projects, we use **generalized geometries** and respect pre‑existing masking policies.   
- Any future use of this event in narratives involving Indigenous communities must be co‑governed under KFM’s Indigenous Data Protection policy. :contentReference[oaicite:42]{index=42}  

---

## 🕰️ Version History

| Version | Date       | Description                                                         |
|---------|------------|---------------------------------------------------------------------|
| v11.2.5 | 2025-12-10 | Aligned with KFM‑MDP v11.2.6; added STAC/DCAT/PROV & CI/CD wiring. |
| v11.2.5 | 2025-12-09 | Initial governed publication of the G3 event record.               |

---

<div align="center">

### 🏛️ Governance Footer

Reviewed under **FAIR+CARE**, KFM provenance standards, Diamond⁹ Ω / Crown∞Ω certification,  
and the **Environmental & Space Weather Steering Group**.  

[🌐 KFM Home](../../README.md) ·  
[📚 Standards](../../standards/README.md) ·  
[⚖ Governance](../../standards/governance/ROOT-GOVERNANCE.md) ·  
[🕊 FAIR+CARE Guide](../../standards/faircare/FAIRCARE-GUIDE.md) ·  
[🛡 Security Policy](../../security/SECURITY.md)

</div>
