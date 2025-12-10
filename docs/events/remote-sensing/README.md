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

<div align="center">

# 🛰️ **Kansas Frontier Matrix — Remote-Sensing Event Logs**

`docs/events/remote-sensing/README.md`

**Purpose**

Define the conventions, structure, and governance for **remote-sensing event Markdown files**
(availability interruptions, reprocessing campaigns, algorithm changes, mission-status events)
that impact the KFM pipeline:

Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode.

This README is the parent standard for all sensor-specific event folders (e.g., Landsat,
Sentinel‑2, MODIS, VIIRS) under `docs/events/remote-sensing/`.

</div>

---

## 📘 Overview

### Scope

This README governs all **remote-sensing event docs** under:

- `docs/events/remote-sensing/**/*.md`

These documents record **upstream provider events** that affect:

- Ingestion of satellite/airborne products in KFM ETL
- STAC collections/items and DCAT datasets derived from those products
- Neo4j event and incident graph structures
- API responses and data-availability flags
- Story Nodes and Focus Mode timelines for Earth-observation narratives over Kansas

Event types include, but are not limited to:

- Product availability interruptions and outages
- Bulk reprocessing campaigns and calibration updates
- Algorithm or product-definition changes
- Mission-status events that alter coverage or data latency

---

## 🗂️ Directory Layout

~~~text
📁 Kansas-Frontier-Matrix/
└── 📁 docs/
    └── 📁 events/
        └── 📁 remote-sensing/
            ├── 📄 README.md                          # This document (remote-sensing event standard)
            ├── 📁 landsat/                           # Landsat-specific events
            │   ├── 📄 README.md                      # Landsat event standard
            │   └── 📄 YYYY-MM-DD-landsat-*.md        # Landsat event logs
            ├── 📁 sentinel-2/                        # Sentinel-2-specific events
            │   └── 📄 YYYY-MM-DD-sentinel-2-*.md     # Sentinel-2 event logs
            ├── 📁 modis/                             # MODIS-specific events
            │   └── 📄 YYYY-MM-DD-modis-*.md          # MODIS event logs
            ├── 📁 viirs/                             # VIIRS-specific events
            │   └── 📄 YYYY-MM-DD-viirs-*.md          # VIIRS event logs
            └── 📁 misc/                              # Other sensors or cross-sensor events
                └── 📄 YYYY-MM-DD-remote-*.md         # Generic or multi-sensor events
~~~

**Rules**

- Sensor-specific folders (e.g., `landsat`, `sentinel-2`) MAY define their own `README.md` that
  specializes this parent standard.
- Event docs MUST live in a sensor-appropriate folder; cross-sensor events MAY live under `misc/`
  or a dedicated subfolder if governance approves.
- No new top-level directories under `docs/events/remote-sensing/` without review by the Remote
  Sensing & Earth Observation Committee.

---

## 🧭 Context

Remote-sensing events sit between **upstream providers** and **KFM internal pipelines**:

- Upstream: mission ops, ground segments, processing centers (USGS, NASA, ESA, etc.)
- Internal: ETL DAGs, validation, STAC/DCAT catalogs, Neo4j graph, APIs, Story Nodes and Focus Mode

This directory is the **human-readable, governed log** of those events. Other layers (STAC, DCAT,
Neo4j) are expected to **derive from these Markdown docs**, not vice versa.

---

## 📦 Data & Metadata

### File Naming

Sensor-specific READMEs SHOULD define their own exact filename patterns. At this level:

- This file is always:
  - `docs/events/remote-sensing/README.md`
- Sensor-specific events follow the pattern (inside their folder):
  - `YYYY-MM-DD-<sensor>-<short-slug>.md`
  - Date = official event posting date (UTC)
  - `<sensor>` example values: `landsat`, `sentinel-2`, `modis`, `viirs`
  - `<short-slug>` is a concise, hyphenated descriptor (e.g., `interruption`, `l2-reprocessing`)

### Required Front Matter (Event Files, Generic Pattern)

Sensor-specific READMEs may refine this, but the base expectations are:

~~~yaml
title: "🛰️ Kansas Frontier Matrix — <Sensor> Remote-Sensing Event: <Short Title>"
path: "docs/events/remote-sensing/<sensor>/YYYY-MM-DD-<sensor>-<short-slug>.md"
version: "v11.2.x"
last_updated: "YYYY-MM-DD"

release_stage: "Stable / Governed"
lifecycle: "Event Record"
status: "Active / Informational · External Event Log"
doc_kind: "Event Log · Remote Sensing"

provider: "<upstream-organization>"
missions:
  - "<mission-name>"

event_kind: "<kind>"           # e.g., product-availability | reprocessing | algorithm-change | mission-status
event_id: "<sensor>:event:YYYY-MM-DD:<short-slug>"
event_start: "YYYY-MM-DDThh:mm:ssZ"
event_posted: "YYYY-MM-DD"
event_end: null                # null until resolved

affected_products:
  - "<sensor>-L1"
  - "<sensor>-L2"

severity: "low"                # low | moderate | high | critical

upstream_reference_url: "https://example.provider.org/..."
upstream_ticket_id: null

markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"
license: "CC-BY 4.0"
~~~

Additional fields are allowed but MUST NOT conflict with these keys or the relevant sensor-specific README.

### Body Structure (Event Files)

Event docs SHOULD follow a structure compatible with:

- Overview
- Event Summary
- Impact Assessment (ETL, catalogs, graph, APIs, UI)
- Downstream Effects (domain-specific)
- STAC/DCAT/PROV hooks
- Validation & Telemetry
- Story Node & Focus Mode integration
- Version History
- Governance Footer

Sensor-specific READMEs may prescribe stricter variants.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

For each remote-sensing event:

- Use a dedicated STAC Collection, such as `kfm-remote-sensing-events`, or sensor-specific
  collections (`kfm-landsat-events`, `kfm-sentinel-2-events`, etc.).
- STAC Item ID SHOULD match the `event_id`.
- Geometry: typically a Kansas-wide bounding box; MAY be more constrained if appropriate.
- Temporal:
  - `properties.datetime` = `event_start`
  - `properties.start_datetime` / `properties.end_datetime` as needed
- Properties SHOULD include:
  - `kfm:event_kind`
  - `kfm:affected_products`
  - `kfm:severity`
  - `kfm:upstream_reference_url`
- Assets MAY include:
  - `upstream_notice` snapshot
  - `kfm_event_md` rendered HTML of the Markdown event doc

STAC JSON SHOULD live under:

- `data/stac/events/remote-sensing/<sensor>/<event-id>.json`

and pass STAC validation in CI.

### DCAT

Each event SHOULD be described as a DCAT `dcat:Dataset`:

- `dct:title` ← event title
- `dct:description` ← overview
- `dct:temporal` ← event interval
- `dct:spatial` ← Kansas extent or relevant AOI
- `dct:publisher` ← KFM / relevant committee
- `dcat:distribution`:
  - Markdown source
  - Rendered HTML
  - STAC Item

### PROV-O

Treat each event as:

- `prov:Entity` — the event record
- `prov:Activity` — the upstream change/maintenance activity
- `prov:Agent` — upstream provider and KFM committee

A minimal pattern:

~~~text
Entity:   <sensor>:event:YYYY-MM-DD:<short-slug>
Agent:    <provider>
Activity: <provider>:system-maintenance-or-change
Started:  event_start
Ended:    event_end
Status:   ongoing | resolved
~~~

These PROV entities are ingested into Neo4j and linked to impacted collections, datasets, and Story Nodes.

---

## 🧱 Architecture

### Position in the KFM Pipeline

Remote-sensing event docs influence the entire pipeline:

1. ETL  
   - Schedulers and DAGs read event metadata to treat missing or late scenes as expected
     missingness rather than failures and to guide reprocessing/backfill.

2. STAC/DCAT/PROV  
   - Event docs drive generation of STAC Items and DCAT Datasets, with PROV links that explain
     catalog gaps or anomalies.

3. Neo4j  
   - Graph nodes (e.g., `:RemoteSensingEvent`, specialized by sensor) capture event details.
   - Relationships connect events to collections, datasets, regions, and time periods.

4. API  
   - Endpoints surface event flags and details alongside data-availability responses.

5. Frontend (React / MapLibre / Cesium)  
   - UI renders overlays, banners, and timeline markers to explain gaps or changes.

6. Story Nodes / Focus Mode  
   - Narrative elements explain to users why certain data intervals are missing or different.

---

## 🧪 Validation & CI/CD

Changes under `docs/events/remote-sensing/**` SHOULD trigger CI workflows that:

- Run markdown linting and link checks.
- Validate front-matter schemas for event docs and sensor-specific READMEs.
- Validate compatibility with KFM-MDP v11.2.6 (headings, directory layout section, version history, footer).
- Run STAC validation for any generated or updated STAC Items.
- Run security/secret scans to ensure no credentials or PII are present.

A typical workflow file might be:

- `.github/workflows/docs-events-remote-sensing.yml`

which blocks merges on any validation failure.

---

## 🧠 Story Node & Focus Mode Integration

Remote-sensing events are primary drivers for Story Nodes that explain:

- Why Landsat, Sentinel-2, or other series have gaps or unusual patterns.
- When reprocessing or algorithm changes may alter derived metrics.

Each event doc SHOULD make it easy to synthesize at least one Story Node per sensor, including:

- Title, spatial extent, temporal extent.
- A short, fact-based narrative.
- Links to graph entities (event node, affected datasets).
- Explicit separation between facts, interpretation, and speculation.

Focus Mode uses this information to annotate maps and timelines so users understand when a
pattern is data-driven vs. pipeline- or provider-driven.

---

## ⚖ FAIR+CARE & Governance

- Remote-sensing event docs describe **operational meta-information**, typically low risk.
- They MUST NOT include sensitive coordinates or internal-only operational details from providers.
- When events interact with Indigenous lands or sensitive cultural/archaeological contexts, the
  implications MUST be addressed in impact sections using generalized extents and without
  disclosing restricted locations.
- Licensing for these docs is `CC-BY 4.0`; underlying data licensing is determined by the
  original providers and MUST be respected.

Key governance references:

- `docs/standards/governance/ROOT-GOVERNANCE.md`
- `docs/standards/faircare/FAIRCARE-GUIDE.md`
- `docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                         |
|--------:|-----------:|-------------------------------------------------------------------------------------------------|
| v11.2.6 | 2025-12-10 | Initial README for remote-sensing events; parent standard for sensor-specific event directories.|

---

<div align="center">

📑 **Kansas Frontier Matrix — Remote-Sensing Event Logs**  
Scientific Insight · Documentation-First · FAIR+CARE Ethics · Sustainable Intelligence  

[📘 Docs Root](../../..) · [📂 Standards Index](../../standards/README.md) · [⚖ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md)

</div>

