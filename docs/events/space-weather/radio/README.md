---
title: "📻 Kansas Frontier Matrix — Radio Blackout & Propagation Event Logs"
path: "docs/events/space-weather/radio/README.md"
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
  domain: "space-weather-radio-events"
  applies_to:
    - "docs/events/space-weather/radio/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
indigenous_rights_flag: false
data_steward: "Space Weather & Solar-Terrestrial Committee"

ttl_policy: "24 months"
sunset_policy: "Superseded by next radio events README version"

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

doc_uuid: "urn:kfm:doc:events:space-weather:radio:readme:v11.2.6"
semantic_document_id: "kfm-space-weather-radio-events-readme-v11.2.6"

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

# 📻 Kansas Frontier Matrix — Radio Blackout & Propagation Event Logs  

Category-specific standard for **radio space-weather events** that affect KFM:

> HF/VHF/UHF blackouts · ionospheric absorption · satellite comms impacts → ETL reliability → catalog quality → graph & Story Nodes

This README specializes the parent space-weather standard:

- `docs/events/space-weather/README.md`

for the **radio** subdomain under `docs/events/space-weather/radio/`.

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
        │   │   ├── 📄 README.md                      # 📻 This document — radio event standard
        │   │   ├── 📄 YYYY-MM-DD-radio-*.md          # Radio blackout / propagation event logs
        │   │   │   # e.g., 2025-05-18-radio-r3-hf-blackout-kansas.md
        │   │   └── 📁 misc/ 🧩
        │   │       └── 📄 YYYY-MM-DD-radio-misc-*.md
        │   │           # Optional: cross-linked or exploratory radio events
        │   └── 📁 misc/ 🧩
        │       └── 📄 README.md                      # Misc space-weather standard
        │
        └── 📁 remote-sensing/ 📡
            └── 📄 README.md                          # Remote-sensing events (imagery, radar, etc.)
~~~

**Directory rules (radio)**

- All radio blackout / propagation event docs MUST live under `docs/events/space-weather/radio/`.  
- Optional `misc/` MAY be used for:
  - cross-category events primarily documented from the **radio** perspective, or  
  - exploratory/early-phase events pending reclassification.  
- New subfolders under `radio/` that introduce new schema or semantics require **Space Weather & Solar-Terrestrial Committee** review.  

---

## 📘 Overview & Scope

This README governs **radio space-weather event docs** under:

- `docs/events/space-weather/radio/**/*.md`

These documents capture radio-space-weather conditions that:

- degrade or interrupt:
  - HF/VHF/UHF communications  
  - satellite communication links relevant to Kansas  
  - radar and other RF-based sensing chains where applicable  
- alter:
  - timeliness and completeness of upstream data feeds relied on by KFM  
  - quality and latency of derived products whose ingestion depends on radio links  

Typical radio event types:

- HF/VHF radio blackouts (NOAA R1–R5 scale)  
- shortwave fadeouts and ionospheric absorption events  
- satellite communication disruptions affecting Kansas data feeds  
- regionally significant disturbances to emergency comms or telemetry links that influence KFM data availability  

Radio event docs are **canonical, human-readable records** that drive catalog annotations, graph nodes, telemetry analyses, and space-weather narratives.

---

## 📦 Data & Metadata Conventions (Radio)

### File Naming

Under `docs/events/space-weather/radio/`:

- Core events:

~~~text
YYYY-MM-DD-radio-<short-slug>.md
~~~

Examples:

- `2025-05-18-radio-r3-hf-blackout-kansas.md`  
- `2026-02-03-radio-vhf-degradation-midcontinent.md`  

Where:

- `YYYY-MM-DD` — date the event is logged (UTC), typically near onset or bulletin issuance  
- `<short-slug>` — concise hyphenated description:
  - may include R-scale, band, and region (e.g., `r3-hf-blackout-kansas`, `vhf-degradation-midcontinent`)  

- Optional misc:

~~~text
misc/YYYY-MM-DD-radio-misc-<short-slug>.md
~~~

### Required Front Matter (Radio Event Files)

Radio events refine the parent space-weather pattern as:

~~~yaml
title: "📻 Kansas Frontier Matrix — Radio Space-Weather Event: <Short Title>"
path: "docs/events/space-weather/radio/YYYY-MM-DD-radio-<short-slug>.md"
version: "v11.2.x"
last_updated: "YYYY-MM-DD"

release_stage: "Stable / Governed"
lifecycle: "Event Record"
status: "Active / Informational · External Event Log"
doc_kind: "Event Summary · Space Weather · Radio"

provider: "<upstream-organization>"             # e.g., NOAA SWPC, ESA, NASA
space_weather_category: "radio-blackout"       # radio-blackout | radio-degradation | propagation-anomaly

event_kind: "space-weather"
routing_event_kind: null                        # optional: product-availability | reprocessing | algorithm-change | mission-status
event_id: "space-weather:radio:event:YYYY-MM-DD:<short-slug>"

event_start: "YYYY-MM-DDThh:mm:ssZ"
event_posted: "YYYY-MM-DD"
event_end: null                                 # null until resolved

bands_affected:
  - "HF"
  - "VHF"
  - "UHF"

r_scale: "R3"                                   # R1–R5 (NOAA radio blackout scale), or null
frequencies_hz:
  min_hz: null                                  # numeric Hz if known
  max_hz: null

affected_regions:
  - "Kansas"
  - "Great Plains"
affected_systems:
  - "hf-radio"
  - "vhf-radio"
  - "satcom"
  - "telemetry-links"

severity: "high"                                # low | moderate | high | extreme

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

## 📄 Recommended Body Structure (Radio Events)

Radio event docs SHOULD follow this body structure:

1. **📘 Overview**  
   - plain-language summary of the blackout/propagation anomaly and its relevance to Kansas  

2. **📻 Event Summary**  
   - affected bands (HF/VHF/UHF) and, when available, frequency ranges  
   - R-scale classification (R1–R5) and duration  
   - references to upstream bulletins and any multi-agency alerts  

3. **🌍 Spatial & Temporal Extent**  
   - global vs regional character; explicit Kansas AOI  
   - local impact window in UTC  
   - notes on diurnal/terminator effects if relevant  

4. **⚙️ ETL & Pipeline Impact**  
   - disruptions to:
     - satellite telemetry used as KFM inputs  
     - radar or RF-based sensor chains (where relevant)  
   - degraded or delayed:
     - ingestion of remote-sensing or environmental feeds over RF links  
   - changes in:
     - error rates, timeouts, retries, failover behavior across ETL pipelines  

5. **🔗 STAC / DCAT / PROV Integration**  
   - how this radio event is represented as:
     - STAC Items in `kfm-space-weather-events` / `kfm-radio-events`  
     - DCAT Datasets with radio-focused keywords and temporal coverage  
     - PROV entities/activities/agents linking to impacted datasets  

6. **🧭 Neo4j & Story Node Integration**  
   - `:SpaceWeatherEvent { category: "radio-blackout" | "radio-degradation" }` node details  
   - relationships to:
     - remote-sensing and telemetry-dependent datasets  
     - Kansas regions where communication-dependent feeds were impacted  

7. **📊 Telemetry & Validation**  
   - metrics showing:
     - increased ETL timeout rates  
     - gaps or lags in RF-delivered feeds  
     - service-level SLO violations related to RF connectivity  

8. **🤝 Sovereignty & FAIR+CARE Considerations**  
   - ethical framing when radio events intersect with public safety, infrastructure, or community comms  

9. **📝 Version History**  
   - table of event record edits  

10. **🏛️ Governance Footer**  
    - compliance statement and CI expectations  

---

## 🌐 STAC, DCAT & PROV Alignment (Radio)

### STAC

Radio blackout / propagation events SHOULD be represented in STAC as:

- collection: `kfm-space-weather-events` and/or `kfm-radio-events`  
- item `id`: `space-weather:radio:event:YYYY-MM-DD:<short-slug>`  

Core STAC properties:

- `kfm:event_kind = "space-weather"`  
- `kfm:space_weather_category` ∈ {`radio-blackout`, `radio-degradation`, `propagation-anomaly`}  
- `kfm:r_scale` (if applicable)  
- `kfm:bands_affected`  
- `kfm:affected_regions`, `kfm:affected_systems`  
- `kfm:severity`  
- `kfm:event_ref` (matching `event_id`)  
- `kfm:upstream_reference_url`  

Assets MAY include:

- upstream radio blackout plots or bulletins  
- rendered event Markdown/HTML  

STAC JSON SHOULD live under:

- `data/stac/events/space-weather/radio/<event-id>.json`

and must pass `KFM-STAC v11` validation in CI.

### DCAT

Radio events as DCAT `dcat:Dataset` SHOULD include:

- `dct:title` — event title  
- `dct:description` — overview and impact summary  
- `dct:temporal` — start/end interval  
- `dct:spatial` — Kansas or regional AOI  
- `dcat:keyword` — `space-weather`, `radio-blackout`, `R3`, `hf-radio`, `satcom`, etc.  
- `dcat:distribution` — links to:
  - Markdown source  
  - rendered HTML  
  - event STAC Items  

### PROV-O

In PROV terms:

- `prov:Entity` — the radio event record (Markdown + STAC/DCAT derivatives)  
- `prov:Activity` — the radio blackout / propagation anomaly as physical/operational activity  
- `prov:Agent` — upstream providers (NOAA SWPC/ESA/NASA/etc.) + KFM committees  

PROV bundles SHOULD:

- live under `data/provenance/space-weather/radio/**`  
- be ingested into Neo4j and linked to affected datasets, missions, and regions  

---

## 🧱 Position in the KFM Pipeline (Radio Focus)

Radio event docs inform:

1. **ETL & Orchestration**  
   - Prefect 3 / Airflow 3 orchestrators can:
     - tag RF-dependent ETL runs with `event_id`  
     - adjust retry and backoff for satellite / RF-based data sources during events  
   - pipelines may:
     - treat some missing data as **event-expected** rather than generic failures  
     - queue replays/backfill once radio conditions normalize.  

2. **STAC/DCAT/PROV Catalogs**  
   - event-aware catalogs:
     - explain time ranges where RS or other RF-delivered feeds show gaps  
     - annotate products with `kfm:event_ref` and radio-specific quality notes.  

3. **Neo4j Graph**  
   - nodes: `(:SpaceWeatherEvent {category: "radio-blackout" | "radio-degradation"})`  
   - relationships:
     - `:AFFECTS_DATASET` ↔ telemetry-dependent datasets  
     - `:AFFECTS_REGION` ↔ Kansas AOIs  

4. **Story Nodes & Focus Mode**  
   - narratives linking:
     - radio blackouts → missing or noisy data → Kansas temporal patterns  
   - Focus Mode overlays to show:
     - blackout intervals as ribbons across layers reliant on RF.  

---

## 🧪 Validation & CI/CD

Changes under `docs/events/space-weather/radio/**` SHOULD trigger CI workflows that:

- run markdown lint and internal link checks  
- validate front matter against this radio pattern and parent space-weather schema  
- enforce **KFM-MDP v11.2.6** requirements:
  - directory layout section  
  - version history  
  - governance footer  
- validate any associated STAC/DCAT updates (if included)  
- run security/secret scans to confirm:
  - no credentials  
  - no PII  
  - no sensitive infrastructure topologies or non-public operational details  

Example workflow:

- `.github/workflows/docs-events-space-weather.yml`  
  - SHOULD include radio-specific fixtures or schema tests.  

---

## 🧠 Story Nodes & Focus Mode

Radio event docs should be optimized for Story Node extraction:

- **Title** — e.g., “R3 HF Radio Blackout Over Kansas (2025-05-18)”  
- **Spatial extent** — Kansas AOI; optional broader context for mid-continent or hemisphere-level effects  
- **Temporal extent** — precise UTC start/end times  
- **Narrative** — factual description of:
  - bands affected  
  - R-scale classification  
  - observed or anticipated effects on KFM feeds and products  

Story Nodes derived from radio events MUST clearly separate:

- **facts** — bulletins, indices, and observed impacts  
- **interpretation** — KFM’s reading of how radio conditions influence data availability or latency  
- **speculation** — possible longer-term or systemic effects, clearly labeled as speculative  

Focus Mode can then:

- overlay radio event markers on maps and timelines  
- support filtering by R-scale, band, or affected systems  
- visualize correlations across radio events and Kansas data anomalies.  

---

## ⚖ FAIR+CARE, Sovereignty & Ethics

Radio event docs primarily describe global/large-scale propagation phenomena, but:

- MUST NOT:
  - expose detailed critical infrastructure layout  
  - reveal sensitive non-public comms vulnerabilities or configurations  
- When used to interpret potential impacts on:
  - Indigenous lands  
  - culturally significant communities or infrastructures  
  narrative sections MUST:
    - generalize spatial descriptions  
    - avoid exposing restricted locations or knowledge  
    - reference `sovereignty_policy` and any applicable agreements.  

Licensing:

- docs: `CC-BY 4.0`  
- upstream bulletins/data: governed by provider licenses (NOAA, ESA, NASA, etc.) and MUST be respected.  

Key governance references:

- `docs/standards/governance/ROOT-GOVERNANCE.md`  
- `docs/standards/faircare/FAIRCARE-GUIDE.md`  
- `docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`  

---

## 🕰️ Version History

| Version | Date       | Summary                                                  |
|--------:|-----------:|----------------------------------------------------------|
| v11.2.6 | 2025-12-10 | Initial v11.2.6-aligned README for radio space-weather events. |

---

<sub>© Kansas Frontier Matrix · CC‑BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM‑MDP v11.2.6</sub>

<br/>

<div align="center">

📻 **Kansas Frontier Matrix — Radio Blackout & Propagation Event Logs v11.2.6**  
RF & Comms Narratives · Catalog–Graph Harmony · FAIR+CARE Space-Weather Governance  

[📘 Docs Root](../../../README.md) · [🧭 Event→Action Map](../../README.md) · [🌞 Space-Weather Events](../README.md) · [📡 Remote-Sensing Events](../../remote-sensing/README.md) · [⚖ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>