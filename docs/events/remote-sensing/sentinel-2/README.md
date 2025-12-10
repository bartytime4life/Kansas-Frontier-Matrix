---
title: "🛰️ Kansas Frontier Matrix — Sentinel‑2 Event Logs"
path: "docs/events/remote-sensing/sentinel-2/README.md"
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
    - "docs/events/remote-sensing/sentinel-2/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
indigenous_rights_flag: false
data_steward: "Remote Sensing & Earth Observation Committee"

ttl_policy: "24 months"
sunset_policy: "Superseded by next Sentinel‑2 events README version"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"
attestation_ref: "../../../../releases/v11.2.6/slsa-attestation.json"
signature_ref: "../../../../releases/v11.2.6/signature.sig"

telemetry_ref: "../../../../releases/v11.2.6/earth-observation-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/earth-observation-v3.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

story_node_refs: []
immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:events:remote-sensing:sentinel-2:readme:v11.2.6"
semantic_document_id: "kfm-sentinel-2-events-readme-v11.2.6"

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

# 🛰️ **Kansas Frontier Matrix — Sentinel‑2 Event Logs**

`docs/events/remote-sensing/sentinel-2/README.md`

**Purpose**

Define conventions, structure, and governance for **Sentinel‑2 remote‑sensing event Markdown
files** (availability interruptions, reprocessing campaigns, algorithm changes, mission‑status
events) that impact the KFM pipeline:

Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode.

This README specializes the remote‑sensing events parent standard for **Sentinel‑2A/B** (and
future Sentinel‑2 units) under `docs/events/remote-sensing/sentinel-2/`.

</div>

---

## 📘 Overview

### Scope

This README governs **all Sentinel‑2 event docs** under:

- `docs/events/remote-sensing/sentinel-2/*.md`

These documents record **upstream Sentinel‑2 provider events** (principally ESA / Copernicus
and partners) that affect:

- Ingestion of Sentinel‑2 Level‑1C and Level‑2A products in KFM ETL
- STAC Collections/Items and DCAT datasets for Sentinel‑2–derived products
- Neo4j event and incident graph structures
- API responses and data‑availability flags
- Story Nodes and Focus Mode timelines for Sentinel‑2 narratives over Kansas

Typical events:

- Product availability interruptions and outages
- Bulk reprocessing campaigns (e.g., new atmospheric corrections, calibration updates)
- Algorithm or product‑definition changes (e.g., cloud mask evolution, QA band semantics)
- Mission‑status events that alter coverage, latency, or acquisition patterns

---

## 🗂️ Directory Layout

~~~text
📁 Kansas-Frontier-Matrix/
└── 📁 docs/
    └── 📁 events/
        └── 📁 remote-sensing/
            └── 📁 sentinel-2/
                ├── 📄 README.md                               # This document (Sentinel‑2 event standard)
                ├── 📄 YYYY-MM-DD-sentinel-2-<short-slug>.md    # Sentinel‑2 event logs (one event per file)
                └── 📄 YYYY-MM-DD-sentinel-2-<another>.md       # Additional Sentinel‑2 events
~~~

**Rules**

- This README is the **canonical standard** for Sentinel‑2 event docs.
- Each event MUST be recorded in its own file:
  - `YYYY-MM-DD-sentinel-2-<short-slug>.md`
  - Date = official **event posting date** (UTC), not necessarily the start date.
  - `<short-slug>` is a concise, lowercase, hyphenated label (e.g., `interruption`,
    `l2a-reprocessing`, `cloud-mask-update`).
- No nested subfolders under `sentinel-2/` without governance approval.

---

## 🧭 Context

Sentinel‑2 events sit between **upstream providers** and **KFM internal pipelines**:

- Upstream:
  - ESA / Copernicus, EUMETSAT, and associated processing centers
  - Mission status pages, product notices, and reprocessing announcements
- KFM internal:
  - Sentinel‑2 ETL DAGs and validation
  - STAC/DCAT catalogs and Neo4j event nodes
  - APIs, Story Nodes, and Focus Mode overlays

This directory is the **human‑readable, governed log** of Sentinel‑2 events. STAC/DCAT/Neo4j
representations are expected to **derive from these Markdown docs**, not vice versa.

---

## 📦 Data & Metadata

### File Naming

Sentinel‑2 event files MUST follow:

- Pattern:
  - `YYYY-MM-DD-sentinel-2-<short-slug>.md`
- Date:
  - Official event **posting date** (UTC).
- Short slug examples:
  - `interruption`
  - `l2a-reprocessing`
  - `pdgs-outage`
  - `alg-update`
  - `calibration-update`

Example filenames:

- `2026-01-12-sentinel-2-interruption.md`
- `2026-03-01-sentinel-2-l2a-reprocessing.md`

### Required Front Matter (Sentinel‑2 Event Files)

Each Sentinel‑2 event doc MUST begin with a YAML block including at least:

- Identity and location:

  - `title`:  
    `"🛰️ Kansas Frontier Matrix — Sentinel‑2 Event: <Short Title>"`
  - `path`:  
    `"docs/events/remote-sensing/sentinel-2/YYYY-MM-DD-sentinel-2-<short-slug>.md"`
  - `version`:  
    e.g. `"v11.2.x"`
  - `last_updated`:  
    ISO date

- Governance:

  - `release_stage`: e.g. `"Stable / Governed"`
  - `lifecycle`: e.g. `"Event Record"`
  - `status`: e.g. `"Active / Informational · External Event Log"`
  - `doc_kind`: `"Event Log · Remote Sensing"`

- Provider and mission:

  - `provider`: `"ESA / Copernicus"`
  - `missions`:
    - `"Sentinel‑2A"`
    - `"Sentinel‑2B"`

- Event core fields:

~~~yaml
event_kind: "product-availability"   # or: "reprocessing" | "algorithm-change" | "mission-status"
event_id: "sentinel-2:event:YYYY-MM-DD:<short-slug>"
event_start: "YYYY-MM-DDThh:mm:ssZ"
event_posted: "YYYY-MM-DD"
event_end: null                      # null until resolved

affected_products:
  - "S2-L1C"
  - "S2-L2A"

severity: "low"                      # low | moderate | high | critical

upstream_reference_url: "https://example.copernicus.eu/..."
upstream_ticket_id: null
~~~

- Standards and profiles:

~~~yaml
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"
license: "CC-BY 4.0"
~~~

Sensor-specific projects MAY add additional keys (e.g., `processing_baseline`,
`product_definition_version`), but MUST NOT conflict with these base keys.

### Body Structure (Sentinel‑2 Event Files)

Sentinel‑2 event docs SHOULD follow this structure:

1. `# 🛰️ <Title>` — H1 plus a one‑line identifier or path.
2. **Overview** — What happened, where, when, and why it matters.
3. **Event Summary** — Key products affected, severity, expected duration.
4. **KFM Impact Assessment** — ETL, catalog, graph, API, and UI impacts.
5. **Downstream Effects** — Domain‑specific implications (agriculture, hydrology, etc.).
6. **STAC/DCAT/PROV hooks** — IDs and mapping guidance.
7. **Validation & Telemetry** — Checks triggered and classification of gaps.
8. **Story Node & Focus Mode** — Narrative integration guidance.
9. **Version History** — Table of changes to the document.
10. **Governance Footer** — Links to governance and policy docs.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

For each Sentinel‑2 event:

- Collection:
  - Use a sensor‑specific STAC Collection such as `kfm-sentinel-2-events`, or a unified
    `kfm-remote-sensing-events` if configured that way.
- Item ID:
  - SHOULD match `event_id` (e.g., `sentinel-2:event:YYYY-MM-DD:<short-slug>`).
- Geometry:
  - Kansas-wide bounding box, or a more specific AOI if the event is spatially localized.
- Temporal:
  - `properties.datetime` = `event_start`
  - `properties.start_datetime` / `properties.end_datetime` as appropriate.
- Properties SHOULD include:
  - `kfm:event_kind`
  - `kfm:affected_products`
  - `kfm:severity`
  - `kfm:upstream_reference_url`
  - Optional sensor-specific keys (e.g., `kfm:s2_processing_baseline`).
- Assets MAY include:
  - `upstream_notice` — snapshot of ESA/Copernicus notice.
  - `kfm_event_md` — rendered HTML of the event document.

STAC JSON SHOULD be stored under:

- `data/stac/events/remote-sensing/sentinel-2/<event-id>.json`

and MUST pass STAC validation in CI.

### DCAT

Each Sentinel‑2 event SHOULD be described as a DCAT `dcat:Dataset`:

- `dct:title` ← Sentinel‑2 event title.
- `dct:description` ← overview section.
- `dct:temporal` ← event interval.
- `dct:spatial` ← Kansas extent or relevant AOI.
- `dct:publisher` ← KFM / Remote Sensing & Earth Observation Committee.
- `dcat:distribution`:
  - Markdown source.
  - Rendered HTML.
  - STAC Item.

### PROV-O

Treat each Sentinel‑2 event as:

- `prov:Entity` — the event record (`event_id`).
- `prov:Activity` — upstream maintenance/change activity (e.g., `esa:pdgs-maintenance`).
- `prov:Agent` — `esa:copernicus`, `eumetsat`, and relevant KFM committees.

Minimal PROV pattern:

~~~text
Entity:   sentinel-2:event:YYYY-MM-DD:<short-slug>
Agent:    esa:copernicus
Activity: esa:pdgs-maintenance
Started:  event_start
Ended:    event_end
Status:   ongoing | resolved
~~~

Neo4j ingestion uses these entities and activities to connect events with collections, datasets,
and Story Nodes.

---

## 🧱 Architecture

### Position in the KFM Pipeline

Sentinel‑2 event docs influence the entire pipeline:

1. **ETL**  
   - Sentinel‑2 ETL DAGs read event metadata to:
     - Distinguish between expected missingness vs. ETL failure.
     - Adjust scheduling, retries, or backfills after reprocessing campaigns.

2. **STAC/DCAT/PROV**  
   - Event docs drive creation of STAC Items and DCAT Datasets with PROV links.
   - Catalog queries can answer “why is Sentinel‑2 data missing or changed here?”

3. **Neo4j**  
   - Graph nodes (e.g., `:Sentinel2Event`) store event details and connect to:
     - `:Collection` nodes for Sentinel‑2 products.
     - `:Pipeline` or `:PipelineRunPattern` nodes for ETL behaviors.
     - Spatial and temporal nodes representing Kansas regions and time windows.

4. **API**  
   - API endpoints surface Sentinel‑2 events alongside:
     - Data availability.
     - Quality flags.
     - Fallback sensor usage (e.g., Landsat during Sentinel‑2 outages).

5. **Frontend (React / MapLibre / Cesium)**  
   - UI renders:
     - Timeline markers over Sentinel‑2 time series.
     - Map overlays for event windows (e.g., hatched periods for outages).
     - Links from UI annotations back to this README and specific event docs.

6. **Story Nodes / Focus Mode**  
   - Narrative elements explain Sentinel‑2‑driven data gaps or product changes.
   - Focus Mode uses event metadata to annotate charts and scenes with “upstream
     Sentinel‑2 event” labels and links.

---

## 🧪 Validation & CI/CD

Changes under `docs/events/remote-sensing/sentinel-2/**` SHOULD trigger CI workflows that:

- Run markdown linting and link checks.
- Validate front‑matter schema for Sentinel‑2 event docs.
- Confirm KFM‑MDP v11.2.6 conformance (headings, directory layout, version history, footer).
- Validate corresponding STAC Items for affected events, when present.
- Run security and secret scans to ensure no credentials or PII appear.

Typical workflow file:

- `.github/workflows/docs-events-sentinel-2.yml`

which blocks merges on any validation failure.

---

## 🧠 Story Node & Focus Mode Integration

Sentinel‑2 events should map cleanly into Story Nodes that explain:

- Why Sentinel‑2 imagery is missing, delayed, or changed for certain periods.
- How reprocessing or algorithm updates affect derived indicators (NDVI, NDMI, water extent).

Each event doc SHOULD support at least one Story Node pattern, for example:

- **Title:** “Sentinel‑2 Quiet Days Over Kansas (Jan 2026)”  
  - Facts: outage interval, affected products, fallback to Landsat where available.

- **Title:** “When Algorithms Change the Picture”  
  - Facts: Sentinel‑2 atmospheric correction or cloud mask update, impact on time series.

In Focus Mode:

- **Facts**  
  - Mark Sentinel‑2 coverage gaps or product changes with clear, data‑backed labels.  

- **Interpretation** (clearly labeled)  
  - Explain how these events influence KFM analyses and visualizations.  

- **Speculation** (optional, clearly labeled and minimal)  
  - Consider possible long‑term impacts on sensor weighting or fusion strategies.  

---

## ⚖ FAIR+CARE & Governance

- Sentinel‑2 event docs capture **operational meta‑information**, generally low‑risk.
- They MUST NOT:
  - Include sensitive coordinates or internal provider‑only information.
  - Expose restricted Indigenous or culturally sensitive locations.

When events interact with Indigenous lands or sensitive archaeological/ecological sites:

- Use generalized locations and coarse extents.
- Route concerns through the FAIR+CARE and sovereignty policies referenced in the front matter.

Licensing:

- This README and Sentinel‑2 event docs: `CC-BY 4.0`.
- Underlying Sentinel‑2 data adhere to Copernicus/ESA licensing and must be respected
  independently of this documentation.

Key governance references:

- `docs/standards/governance/ROOT-GOVERNANCE.md`
- `docs/standards/faircare/FAIRCARE-GUIDE.md`
- `docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                     |
|--------:|-----------:|---------------------------------------------------------------------------------------------|
| v11.2.6 | 2025-12-10 | Initial README for Sentinel‑2 event directory; aligned with remote-sensing parent standard and KFM-MDP v11.2.6. |

---

<div align="center">

📑 **Kansas Frontier Matrix — Sentinel‑2 Event Logs**  
Scientific Insight · Documentation‑First · FAIR+CARE Ethics · Sustainable Intelligence  

[📘 Docs Root](../../../..) · [📂 Remote-Sensing Events](../README.md) · [⚖ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

