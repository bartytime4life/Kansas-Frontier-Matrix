---
title: "🧲 Kansas Frontier Matrix — Geomagnetic Storm Event Logs"
path: "docs/events/space-weather/geomagnetic/README.md"
version: "v11.2.6"
last_updated: "2025-12-10"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Space Weather & Solar-Terrestrial Committee"
content_stability: "stable"
status: "Active / Standard"
doc_kind: "Guide · Category Standard"
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
  domain: "space-weather-geomagnetic-events"
  applies_to:
    - "docs/events/space-weather/geomagnetic/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
indigenous_rights_flag: false
data_steward: "Space Weather & Solar-Terrestrial Committee"

ttl_policy: "24 months"
sunset_policy: "Superseded by next geomagnetic events README version"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"
attestation_ref: "../../../../releases/v11.2.6/slsa-attestation.json"
signature_ref: "../../../../releases/v11.2.6/signature.sig"

telemetry_ref: "../../../../releases/v11.2.6/space-weather-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/space-weather-v1.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

story_node_refs: []
immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:events:space-weather:geomagnetic:readme:v11.2.6"
semantic_document_id: "kfm-space-weather-geomagnetic-events-readme-v11.2.6"

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

# 🧲 Kansas Frontier Matrix — Geomagnetic Storm Event Logs  

Category-specific standard for **geomagnetic space-weather events** that affect KFM:

> Geomagnetic storms · Kp/Ap spikes · G1–G5 events → ETL reliability → catalog quality → graph & Story Nodes

This README specializes the parent space-weather standard:

- `docs/events/space-weather/README.md`

for the **geomagnetic** subdomain under `docs/events/space-weather/geomagnetic/`.

---

## 🗂️ Directory Layout

~~~text
📁 Kansas-Frontier-Matrix/
└── 📁 docs/
    └── 📁 events/
        ├── 📁 space-weather/ 🌞
        │   ├── 📄 README.md                      # Space-weather event standard (parent)
        │   └── 📁 geomagnetic/ 🧲
        │       ├── 📄 README.md                  # 🧲 This document — geomagnetic event standard
        │       ├── 📄 YYYY-MM-DD-geomagnetic-*.md
        │       │   # Geomagnetic storm event logs (e.g., G3_Kp7-storm-over-kansas.md)
        │       └── 📁 misc/ 🧩
        │           └── 📄 YYYY-MM-DD-geomagnetic-misc-*.md
        │               # Optional: cross-linked or experimental geomagnetic events
        │
        └── 📁 remote-sensing/ 📡
            └── 📄 README.md                      # Remote-sensing events (imagery, radar, etc.)
~~~

**Directory rules (geomagnetic)**

- All geomagnetic storm event docs MUST live under `docs/events/space-weather/geomagnetic/`.  
- Optional `misc/` MAY be used for cross-category events (geomagnetic + radio, etc.) where no single folder is a perfect fit.  
- New subfolders under `geomagnetic/` require review by the **Space Weather & Solar-Terrestrial Committee** if they introduce new schema or semantics.

---

## 📘 Overview & Scope

This README governs **geomagnetic storm event docs** under:

- `docs/events/space-weather/geomagnetic/**/*.md`

These documents capture **G-scale / Kp / Ap** geomagnetic events that:

- affect satellite operations, GNSS, HF/VHF comms, and ground-based infrastructure  
- may degrade or delay:
  - remote-sensing products over Kansas  
  - model and forecast pipelines relying on GNSS or magnetospheric inputs  
- need to be visible to:
  - ETL/orchestration systems (for resilience)  
  - STAC/DCAT catalogs (for quality annotation)  
  - Neo4j graph and Story Nodes (for narrative and causal context)  

Typical geomagnetic event types:

- G1–G5 storms (NOAA G-scale)  
- extended periods of **elevated Kp/Ap**  
- geomagnetically induced current (GIC) risk events  
- regional geomagnetic disturbances relevant to Kansas and the Great Plains  

Geomagnetic event docs are **canonical, human-readable records** that drive catalog annotations, graph nodes, and space-weather narrative layers.

---

## 📦 Data & Metadata Conventions (Geomagnetic)

### File Naming

Under `docs/events/space-weather/geomagnetic/`:

- Core events:

  ~~~text
  YYYY-MM-DD-geomagnetic-<short-slug>.md
  ~~~

  Examples:

  - `2025-05-18-geomagnetic-g3-kp7-storm-kansas.md`  
  - `2026-02-03-geomagnetic-g2-recurrent-storm.md`  

Where:

- `YYYY-MM-DD` — date the event is logged (UTC), usually near onset  
- `<short-slug>` — short, hyphenated description:
  - may include G-scale, Kp peak, or region (e.g., `g3-kp7-storm-kansas`)  

- Optional misc:

  ~~~text
  misc/YYYY-MM-DD-geomagnetic-misc-<short-slug>.md
  ~~~

### Required Front Matter (Geomagnetic Event Files)

Geomagnetic events refine the parent space-weather pattern as:

~~~yaml
title: "🧲 Kansas Frontier Matrix — Geomagnetic Storm Event: <Short Title>"
path: "docs/events/space-weather/geomagnetic/YYYY-MM-DD-geomagnetic-<short-slug>.md"
version: "v11.2.x"
last_updated: "YYYY-MM-DD"

release_stage: "Stable / Governed"
lifecycle: "Event Record"
status: "Active / Informational · External Event Log"
doc_kind: "Event Summary · Space Weather · Geomagnetic"

provider: "<upstream-organization>"       # e.g., NOAA SWPC, ESA, NRCan
space_weather_category: "geomagnetic-storm"

event_kind: "space-weather"
routing_event_kind: null                  # optional: product-availability | reprocessing | algorithm-change | mission-status
event_id: "space-weather:geomagnetic:event:YYYY-MM-DD:<short-slug>"

event_start: "YYYY-MM-DDThh:mm:ssZ"
event_posted: "YYYY-MM-DD"
event_end: null                           # null until resolved

kp_peak: 7                                # integer or float
ap_max: 150                               # integer, Ap index
noaa_scale:
  g_scale: "G3"                           # G1–G5
  s_scale: null
  r_scale: null

affected_regions:
  - "Kansas"
  - "Great Plains"
affected_systems:
  - "gnss"
  - "hf-radio"
  - "remote-sensing-downlink"

severity: "high"                          # low | moderate | high | extreme

upstream_reference_url: "https://www.swpc.noaa.gov/products/alerts-watches-and-warnings"
upstream_bulletin_id: null

markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"
license: "CC-BY 4.0"
~~~

Additional keys are allowed but MUST NOT:

- conflict with these fields  
- contradict the parent `docs/events/space-weather/README.md` standard  

---

## 📄 Recommended Body Structure (Geomagnetic Events)

Geomagnetic event docs SHOULD follow this body structure:

1. **📘 Overview**  
   - brief, non-technical summary of the storm and its relevance to Kansas  

2. **🧲 Event Summary**  
   - Kp, Ap, and G-scale values  
   - start/end times, peak indices, upstream bulletin references  

3. **🌍 Spatial & Temporal Extent**  
   - global vs regional character; explicit Kansas focus  
   - local impact window in UTC  

4. **⚙️ ETL & Pipeline Impact**  
   - remote-sensing ingest delays or anomalies  
   - GNSS-based product degradation or uncertainty  
   - changes in error rates, retries, or backoff in ETL  

5. **🔗 STAC / DCAT / PROV Integration**  
   - how this event is represented:
     - as STAC Items in `kfm-space-weather-events` / `kfm-geomagnetic-events`  
     - as DCAT Datasets with appropriate keywords and temporal coverage  
     - as PROV Entities/Activities/Agents  

6. **🧭 Neo4j & Story Node Integration**  
   - `:SpaceWeatherEvent { category: "geomagnetic-storm" }` node details  
   - relationships to:
     - missions, datasets, AOIs  
     - Story Nodes about statewide impacts  

7. **📊 Telemetry & Validation**  
   - metrics showing:
     - latency spikes  
     - failure bursts  
     - quality flags or noise increases in downstream products  

8. **🤝 Sovereignty & FAIR+CARE Considerations**  
   - ethical framing when relating geomagnetic impacts to infrastructure or communities  

9. **📝 Version History**  
   - versioned edits and clarifications  

10. **🏛️ Governance Footer**  
    - compliance statement and CI requirements  

---

## 🌐 STAC, DCAT & PROV Alignment (Geomagnetic)

### STAC

Geomagnetic events SHOULD be represented in STAC as:

- collection: `kfm-space-weather-events` and/or `kfm-geomagnetic-events`  
- item `id`: `space-weather:geomagnetic:event:YYYY-MM-DD:<short-slug>`  

Core STAC properties:

- `kfm:event_kind = "space-weather"`  
- `kfm:space_weather_category = "geomagnetic-storm"`  
- `kfm:g_scale`, `kfm:kp_peak`, `kfm:ap_max`  
- `kfm:severity`  
- `kfm:affected_regions`  
- `kfm:event_ref` (matching `event_id`)  

Assets MAY include:

- upstream bulletin (PDF, HTML snapshot)  
- rendered event Markdown/HTML  

Geomagnetic STAC Items SHOULD live under:

- `data/stac/events/space-weather/geomagnetic/<event-id>.json`

and pass KFM-STAC v11 validation in CI.

### DCAT

Geomagnetic events as DCAT `dcat:Dataset` SHOULD include:

- `dct:title` — geomagnetic storm title  
- `dct:description` — overview and impact summary  
- `dct:temporal` — event interval  
- `dct:spatial` — Kansas or regional AOI  
- `dcat:keyword` — `space-weather`, `geomagnetic-storm`, `G3`, etc.  
- `dcat:distribution` — links to Markdown, HTML, and STAC Items  

### PROV-O

In PROV terms:

- `prov:Entity` — the event record (Markdown + derived STAC/DCAT)  
- `prov:Activity` — the geomagnetic disturbance as a physical/operational activity  
- `prov:Agent` — NOAA SWPC/ESA/NASA + KFM committees  

PROV bundles SHOULD:

- live under `data/provenance/space-weather/geomagnetic/**`  
- be ingested into Neo4j and linked to affected missions/datasets  

---

## 🧱 Position in the KFM Pipeline (Geomagnetic Focus)

Geomagnetic event docs inform:

1. **ETL & Orchestration**  
   - remote-sensing and GNSS-reliant ETL may:
     - increase tolerance for missing or noisy data  
     - annotate runs with `event_id` for later analysis  
   - orchestrators (Prefect/Airflow) can:
     - temporarily alter retry/backoff strategies during severe G3+ events  

2. **STAC/DCAT/PROV Catalogs**  
   - event-aware catalogs explain:
     - why specific days show degraded quality  
     - why certain data products are delayed or flagged  

3. **Neo4j Graph**  
   - nodes: `(:SpaceWeatherEvent {category: "geomagnetic-storm"})`  
   - relationships:
     - `:AFFECTS_MISSION`, `:AFFECTS_DATASET`, `:AFFECTS_REGION`  
   - cross-links to remote-sensing event nodes when storms degrade imagery quality  

4. **Story Nodes & Focus Mode**  
   - narratives that connect:
     - geomagnetic storms → data anomalies → user-visible impacts in Kansas  

---

## 🧪 Validation & CI/CD

Changes under `docs/events/space-weather/geomagnetic/**` SHOULD trigger CI that:

- runs markdown lint and internal link checks  
- validates front matter against the geomagnetic pattern and parent space-weather schema  
- enforces KFM-MDP v11.2.6 requirements:
  - directory layout section  
  - version history  
  - governance footer  
- validates any associated STAC/DCAT updates (if present in the same PR)  
- runs security/secret scans for:
  - credentials  
  - PII  
  - sensitive infrastructure details  

Example workflow:

- `.github/workflows/docs-events-space-weather.yml`  
  - SHOULD include geomagnetic-specific schema tests or fixtures.  

---

## 🧠 Story Nodes & Focus Mode

Geomagnetic storm docs should be optimized for Story Node extraction:

- **Title** — e.g., “G3 Geomagnetic Storm Over Kansas (2025-05-18)”  
- **Spatial extent** — Kansas AOI with optional broader context  
- **Temporal extent** — precise UTC start/end times  
- **Narrative** — strictly factual description of:
  - storm scales  
  - potential/observed impacts on data and infrastructure  

Story Nodes derived from geomagnetic events MUST clearly separate:

- facts (indices, times, observed impacts)  
- interpretation (KFM’s reading of implications for data quality)  
- speculation (possible long-term effects, flagged as such)  

Focus Mode can then:

- overlay geomagnetic event ribbons on remote-sensing and environmental layers  
- allow users to filter by G-scale or Kp range  
- visualize joint patterns across space weather and Kansas data systems.  

---

## ⚖ FAIR+CARE, Sovereignty & Ethics

Geomagnetic event docs primarily describe global physical phenomena, but:

- MUST NOT:
  - include sensitive details about critical infrastructure topology  
  - reveal vulnerable operational configurations from third parties  
- When used to interpret impacts on:
  - Indigenous lands  
  - culturally significant sites  
  narrative sections MUST:
    - generalize spatial descriptions  
    - avoid exposing restricted locations or knowledge  
    - reference `sovereignty_policy` and relevant agreements.  

Licensing:

- docs: `CC-BY 4.0`  
- upstream bulletins/data: governed by provider (NOAA, ESA, etc.) licenses and MUST be respected.  

---

## 🕰️ Version History

| Version | Date       | Summary                                                |
|--------:|-----------:|--------------------------------------------------------|
| v11.2.6 | 2025-12-10 | Initial v11.2.6-aligned README for geomagnetic events. |

---

<sub>© Kansas Frontier Matrix · CC‑BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM‑MDP v11.2.6</sub>

<br/>

<div align="center">

🧲 **Kansas Frontier Matrix — Geomagnetic Storm Event Logs v11.2.6**  
Solar–Terrestrial Impacts · Catalog–Graph Harmony · FAIR+CARE Space-Weather Governance  

[📘 Docs Root](../../../README.md) · [🧭 Event→Action Map](../../README.md) · [🌞 Space-Weather Events](../README.md) · [📡 Remote-Sensing Events](../../remote-sensing/README.md) · [⚖ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>