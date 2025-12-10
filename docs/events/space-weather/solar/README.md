---
title: "🌞 Kansas Frontier Matrix — Solar Flare & CME Event Logs"
path: "docs/events/space-weather/solar/README.md"
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
  domain: "space-weather-solar-events"
  applies_to:
    - "docs/events/space-weather/solar/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
indigenous_rights_flag: false
data_steward: "Space Weather & Solar-Terrestrial Committee"

ttl_policy: "24 months"
sunset_policy: "Superseded by next solar events README version"

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

doc_uuid: "urn:kfm:doc:events:space-weather:solar:readme:v11.2.6"
semantic_document_id: "kfm-space-weather-solar-events-readme-v11.2.6"

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

# 🌞 Kansas Frontier Matrix — Solar Flare & CME Event Logs  

Category-specific standard for **solar space-weather events** that affect KFM:

> Solar flares · CMEs · solar radiation storms (SEPs) → ETL reliability → catalog quality → graph & Story Nodes

This README specializes the parent space-weather standard:

- `docs/events/space-weather/README.md`

for the **solar** subdomain under `docs/events/space-weather/solar/`.

---

## 🗂️ Directory Layout

~~~text
📁 Kansas-Frontier-Matrix/
└── 📁 docs/
    └── 📁 events/
        ├── 📁 space-weather/ 🌞
        │   ├── 📄 README.md                          # Space-weather event standard (parent)
        │   ├── 📁 geomagnetic/ 🧲
        │   │   └── 📄 README.md                      # Geomagnetic storm standard
        │   ├── 📁 ionosphere/ 📡
        │   │   └── 📄 README.md                      # Ionospheric disturbance standard
        │   ├── 📁 radio/ 📻
        │   │   └── 📄 README.md                      # Radio blackout / propagation standard
        │   ├── 📁 misc/ 🧩
        │   │   └── 📄 README.md                      # Misc space-weather standard
        │   └── 📁 solar/ 🌞
        │       ├── 📄 README.md                      # 🌞 This document — solar event standard
        │       ├── 📄 YYYY-MM-DD-solar-*.md          # Solar flare / CME / SEP event logs
        │       │   # e.g., 2025-05-18-solar-x1-1-flare-cme-earth-directed.md
        │       └── 📁 misc/ 🧩
        │           └── 📄 YYYY-MM-DD-solar-misc-*.md
        │               # Optional: cross-linked or exploratory solar events
        │
        └── 📁 remote-sensing/ 📡
            └── 📄 README.md                          # Remote-sensing events (imagery, radar, etc.)
~~~

**Directory rules (solar)**

- All solar flare / CME / SEP event docs MUST live under `docs/events/space-weather/solar/`.  
- Optional `misc/` MAY be used for:
  - cross-category events that are primarily documented from the **solar** perspective, or  
  - exploratory events pending reclassification.  
- New subfolders under `solar/` that introduce new schema or semantics require **Space Weather & Solar-Terrestrial Committee** review.  

---

## 📘 Overview & Scope

This README governs **solar space-weather event docs** under:

- `docs/events/space-weather/solar/**/*.md`

These documents capture solar conditions that:

- trigger:
  - X/M/C-class solar flares  
  - CMEs that may be Earth-directed or glancing  
  - solar energetic particle (SEP) events (S-scale)  
- affect:
  - geomagnetic conditions and subsequent ground/ionospheric impacts  
  - satellite operations and radiation environment  
  - radio blackouts and GNSS quality (via R/S/G linkages)  

Impacts on KFM may include:

- degraded or delayed:
  - upstream remote-sensing data relayed via satellites  
  - GNSS-based products affected by increased radiation or outages  
- altered:
  - reliability windows for high-latitude / dayside observations  
  - risk posture for RS missions and data ingestion pipelines  

Solar event docs are **canonical, human-readable records** that feed catalog annotations, Neo4j event nodes, telemetry analyses, and Story Node narratives.

---

## 📦 Data & Metadata Conventions (Solar)

### File Naming

Under `docs/events/space-weather/solar/`:

- Core events:

~~~text
YYYY-MM-DD-solar-<short-slug>.md
~~~

Examples:

- `2025-05-18-solar-x1-1-flare-cme-earth-directed.md`  
- `2026-02-03-solar-s2-sep-event-long-duration.md`  

Where:

- `YYYY-MM-DD` — date the event is logged (UTC), usually near flare onset or bulletin issuance  
- `<short-slug>` — concise hyphenated description:
  - may include flare class, CME type, SEP scale, or direction (e.g., `x1-1-flare-cme-earth-directed`, `s2-sep-event-long-duration`)  

- Optional misc:

~~~text
misc/YYYY-MM-DD-solar-misc-<short-slug>.md
~~~

### Required Front Matter (Solar Event Files)

Solar events refine the parent space-weather pattern as:

~~~yaml
title: "🌞 Kansas Frontier Matrix — Solar Event: <Short Title>"
path: "docs/events/space-weather/solar/YYYY-MM-DD-solar-<short-slug>.md"
version: "v11.2.x"
last_updated: "YYYY-MM-DD"

release_stage: "Stable / Governed"
lifecycle: "Event Record"
status: "Active / Informational · External Event Log"
doc_kind: "Event Summary · Space Weather · Solar"

provider: "<upstream-organization>"             # e.g., NOAA SWPC, ESA, NASA
space_weather_category: "solar-flare"           # solar-flare | cme | solar-radiation-storm | combined

event_kind: "space-weather"
routing_event_kind: null                        # optional: product-availability | reprocessing | algorithm-change | mission-status
event_id: "space-weather:solar:event:YYYY-MM-DD:<short-slug>"

event_start: "YYYY-MM-DDThh:mm:ssZ"
event_posted: "YYYY-MM-DD"
event_end: null                                 # null until resolved or decay

flare:
  class: "X1.1"                                 # e.g., X1.1, M5.2; null if not flare-focused
  active_region: null                           # AR number, e.g., 3664
  longitude: null                               # heliographic longitude (deg), if known
  latitude: null                                # heliographic latitude (deg), if known

cme:
  has_cme: true                                 # true | false | null
  speed_kms: null                               # CME plane-of-sky speed (km/s)
  direction: null                               # earth-directed | partial-halo | backside | unknown

sep:
  s_scale: null                                 # S1–S5 (solar radiation storm scale), or null
  proton_flux_pfu: null                         # at >10 MeV, where available

noaa_scale:
  g_scale: null                                 # G1–G5, if geomagnetic storm expected or observed
  r_scale: null                                 # R1–R5 (radio blackout), if associated
  s_scale: null                                 # S1–S5, if SEP classification used here instead of sep.s_scale

affected_regions:
  - "Kansas"
  - "Great Plains"
affected_systems:
  - "remote-sensing"
  - "gnss"
  - "satcom"

severity: "moderate"                            # low | moderate | high | extreme

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
- contradict the parent `space-weather` README standard  

---

## 📄 Recommended Body Structure (Solar Events)

Solar event docs SHOULD follow this body structure:

1. **📘 Overview**  
   - plain-language summary of the flare/CME/SEP and why it matters for Kansas and KFM.  

2. **🌞 Event Summary**  
   - flare class (X/M/C), active region, and timing  
   - CME parameters (presence, speed, Earth-directed status)  
   - SEP indicators (S-scale, proton flux)  
   - linked bulletin identifiers and upstream summaries  

3. **🌍 Spatial & Temporal Extent**  
   - solar/heliospheric context (disk location, limb, backside)  
   - expected/observed impact window for Earth and specifically Kansas (UTC)  

4. **⚙️ ETL & Pipeline Impact**  
   - expected or observed downstream effects on:
     - remote-sensing missions relied on by KFM  
     - GNSS-based pipelines and timing-sensitive processes  
     - RF-based telemetry relevant to Kansas data feeds  
   - changes in:
     - error rates, missing data windows, or latencies  
     - risk posture for certain ingestion jobs or backfill strategies  

5. **🔗 STAC / DCAT / PROV Integration**  
   - how this solar event is represented as:
     - STAC Items in `kfm-space-weather-events` / `kfm-solar-events`  
     - DCAT Datasets with solar-focused keywords and temporal coverage  
     - PROV entities/activities/agents that connect solar phenomena to affected datasets  

6. **🧭 Neo4j & Story Node Integration**  
   - `:SpaceWeatherEvent { category: "solar-flare" | "cme" | "solar-radiation-storm" | "combined" }` node details  
   - relationships to:
     - geomagnetic / ionospheric / radio event nodes (when cascades occur)  
     - RS, GNSS, and model datasets impacted in Kansas  

7. **📊 Telemetry & Validation**  
   - metrics showing:
     - correlated changes in latency/failure across multiple pipelines  
     - quality flags or uncertainty increases in RS or GNSS-derived products  

8. **🤝 Sovereignty & FAIR+CARE Considerations**  
   - ethical framing when connecting global solar events to local communities and infrastructures  

9. **📝 Version History**  
   - table of event record edits and clarifications  

10. **🏛️ Governance Footer**  
    - compliance statement and CI expectations  

---

## 🌐 STAC, DCAT & PROV Alignment (Solar)

### STAC

Solar events SHOULD be represented in STAC as:

- collection: `kfm-space-weather-events` and/or `kfm-solar-events`  
- item `id`: `space-weather:solar:event:YYYY-MM-DD:<short-slug>`  

Core STAC properties:

- `kfm:event_kind = "space-weather"`  
- `kfm:space_weather_category` ∈ {`solar-flare`, `cme`, `solar-radiation-storm`, `combined`}  
- `kfm:flare_class`, `kfm:cme_speed_kms`, `kfm:cme_direction`, `kfm:sep_scale` (if known)  
- `kfm:noaa_scale` (G/R/S) summaries when applicable  
- `kfm:affected_regions`, `kfm:affected_systems`  
- `kfm:severity`  
- `kfm:event_ref` (matching `event_id`)  
- `kfm:upstream_reference_url`  

Assets MAY include:

- upstream solar event bulletins and plots (e.g., GOES X-ray flux)  
- rendered event Markdown/HTML  

STAC JSON SHOULD live under:

- `data/stac/events/space-weather/solar/<event-id>.json`

and must pass `KFM-STAC v11` validation in CI.

### DCAT

Solar events as DCAT `dcat:Dataset` SHOULD include:

- `dct:title` — solar event title (e.g., “X1.1 Flare & CME 2025-05-18”)  
- `dct:description` — overview and impact summary  
- `dct:temporal` — start/end interval for expected/observed impact  
- `dct:spatial` — Kansas or broader AOI as appropriate  
- `dcat:keyword` — `space-weather`, `solar-flare`, `cme`, `sep`, etc.  
- `dcat:distribution` — links to:
  - Markdown source  
  - rendered HTML  
  - event STAC Items  

### PROV-O

In PROV terms:

- `prov:Entity` — the solar event record (Markdown + STAC/DCAT derivatives)  
- `prov:Activity` — the solar physical event (flare/CME/SEP) as an activity  
- `prov:Agent` — upstream providers (NOAA SWPC/ESA/NASA/etc.) + KFM committees  

PROV bundles SHOULD:

- live under `data/provenance/space-weather/solar/**`  
- be ingested into Neo4j and linked to affected datasets and cascaded space-weather events  

---

## 🧱 Position in the KFM Pipeline (Solar Focus)

Solar event docs inform:

1. **ETL & Orchestration**  
   - Prefect 3 / Airflow 3 orchestrators can:
     - adjust risk posture and retry strategies for RS / GNSS / RF-dependent ETL during high-activity windows  
     - tag ETL runs with `event_id` when outages or anomalies correlate with solar events.  

2. **STAC/DCAT/PROV Catalogs**  
   - event-aware catalogs allow:
     - long-term analysis of data quality vs solar cycle and major events  
     - explicit annotation of days where solar conditions may explain anomalies in Kansas data.  

3. **Neo4j Graph**  
   - nodes: `(:SpaceWeatherEvent {category: "solar-flare" | "cme" | "solar-radiation-storm" | "combined"})`  
   - relationships:
     - `:TRIGGERS_EVENT` links to geomagnetic/ionospheric/radio events  
     - `:AFFECTS_DATASET` / `:AFFECTS_REGION` links to Kansas products and AOIs.  

4. **Story Nodes & Focus Mode**  
   - narratives that connect:
     - solar eruptions → cascading space-weather conditions → KFM data patterns in Kansas.  

---

## 🧪 Validation & CI/CD

Changes under `docs/events/space-weather/solar/**` SHOULD trigger CI workflows that:

- run markdown lint and internal link checks  
- validate front matter against this solar pattern and parent space-weather schema  
- enforce **KFM-MDP v11.2.6** requirements:
  - directory layout section  
  - version history  
  - governance footer  
- validate any associated STAC/DCAT updates (if present in the same PR)  
- run security/secret scans to confirm:
  - no credentials  
  - no PII  
  - no sensitive infrastructure or non-public operational secrets  

Example workflow:

- `.github/workflows/docs-events-space-weather.yml`  
  - SHOULD include solar-specific fixtures or schema tests.  

---

## 🧠 Story Nodes & Focus Mode

Solar event docs should be optimized for Story Node extraction:

- **Title** — e.g., “X1.1 Solar Flare & Earth-Directed CME (2025-05-18)”  
- **Spatial extent** — global/heliospheric context with explicit Kansas view where relevant  
- **Temporal extent** — clear event onset and expected impact windows  
- **Narrative** — factual description of:
  - flare/CME/SEP characteristics  
  - observed or likely effects on KFM data feeds and products  

Story Nodes derived from solar events MUST clearly separate:

- **facts** — indices, fluxes, bulletins, observed impacts  
- **interpretation** — KFM’s reading of how solar conditions likely influenced Kansas data  
- **speculation** — potential longer-term effects, explicitly marked as speculative  

Focus Mode can then:

- overlay solar-event ribbons on:
  - remote-sensing, GNSS, and other data layers  
- support filtering by flare class, CME speed, or SEP scale  
- visualize correlations with downstream geomagnetic, ionospheric, and radio events.  

---

## ⚖ FAIR+CARE, Sovereignty & Ethics

Solar event docs mostly describe global, astrophysical phenomena, but:

- MUST NOT:
  - expose sensitive infrastructure layouts or operational vulnerabilities when discussing downstream impacts  
- When narratives connect solar events to:
  - impacts on Indigenous lands  
  - culturally significant sites or infrastructures  
  they MUST:
    - use generalized spatial descriptions  
    - avoid exposing restricted knowledge or locations  
    - reference `sovereignty_policy` and relevant agreements.  

Licensing:

- docs: `CC-BY 4.0`  
- upstream bulletins/data: governed by provider licenses (NOAA, ESA, NASA, etc.) and MUST be respected.  

Key governance references:

- `docs/standards/governance/ROOT-GOVERNANCE.md`  
- `docs/standards/faircare/FAIRCARE-GUIDE.md`  
- `docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`  

---

## 🕰️ Version History

| Version | Date       | Summary                                                |
|--------:|-----------:|--------------------------------------------------------|
| v11.2.6 | 2025-12-10 | Initial v11.2.6-aligned README for solar events.      |

---

<sub>© Kansas Frontier Matrix · CC‑BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM‑MDP v11.2.6</sub>

<br/>

<div align="center">

🌞 **Kansas Frontier Matrix — Solar Flare & CME Event Logs v11.2.6**  
Solar Cycle Narratives · Catalog–Graph Harmony · FAIR+CARE Space-Weather Governance  

[📘 Docs Root](../../../README.md) · [🧭 Event→Action Map](../../README.md) · [🌞 Space-Weather Events](../README.md) · [📡 Remote-Sensing Events](../../remote-sensing/README.md) · [⚖ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>