---
title: "🛰️ Kansas Frontier Matrix — MODIS Event Logs"
path: "docs/events/remote-sensing/modis/README.md"
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
    - "docs/events/remote-sensing/modis/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
indigenous_rights_flag: false
data_steward: "Remote Sensing & Earth Observation Committee"

ttl_policy: "24 months"
sunset_policy: "Superseded by next MODIS events README version"

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

doc_uuid: "urn:kfm:doc:events:remote-sensing:modis:readme:v11.2.6"
semantic_document_id: "kfm-modis-events-readme-v11.2.6"

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

# 🛰️ **Kansas Frontier Matrix — MODIS Event Logs**

`docs/events/remote-sensing/modis/README.md`

**Purpose**

Define conventions, structure, and governance for **MODIS remote‑sensing event Markdown
files** (availability interruptions, reprocessing campaigns, algorithm changes, mission‑status
events) that impact the KFM pipeline:

Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode.

This README specializes the remote‑sensing events parent standard for **MODIS Terra/Aqua**
under `docs/events/remote-sensing/modis/`.

</div>

---

## 📘 Overview

### Scope

This README governs **all MODIS event docs** under:

- `docs/events/remote-sensing/modis/*.md`

These documents record **upstream MODIS provider events** (primarily NASA / EOS / DAACs) that
affect:

- Ingestion of MODIS Level‑1B and Level‑2/3 land products in KFM ETL
- STAC Collections/Items and DCAT datasets for MODIS‑derived products
- Neo4j event and incident graph structures
- API responses and data‑availability flags
- Story Nodes and Focus Mode timelines for MODIS narratives over Kansas

Typical events:

- Product availability interruptions and outages (e.g., ground‑segment issues, archive delays)
- Bulk reprocessing campaigns (e.g., Collection updates, calibration changes)
- Algorithm or product‑definition changes (e.g., NDVI, albedo, snow, land‑surface temperature)
- Mission‑status events that alter coverage, latency, or sensor health

---

## 🗂️ Directory Layout

~~~text
📁 Kansas-Frontier-Matrix/
└── 📁 docs/
    └── 📁 events/
        └── 📁 remote-sensing/
            └── 📁 modis/
                ├── 📄 README.md                             # This document (MODIS event standard)
                ├── 📄 YYYY-MM-DD-modis-<short-slug>.md      # MODIS event logs (one event per file)
                └── 📄 YYYY-MM-DD-modis-<another>.md         # Additional MODIS events
~~~

**Rules**

- This README is the **canonical standard** for MODIS event docs.
- Each event MUST be recorded in its own file:
  - `YYYY-MM-DD-modis-<short-slug>.md`
  - Date = official **event posting date** (UTC), not necessarily the start date.
  - `<short-slug>` is a concise, lowercase, hyphenated label (e.g., `interruption`,
    `collection-update`, `l2-reprocessing`, `alg-change`).
- No nested subfolders under `modis/` without governance approval.

---

## 🧭 Context

MODIS events sit between **upstream providers** and **KFM internal pipelines**:

- Upstream:
  - NASA / EOS, LAADS DAAC, NSIDC and related MODIS data centers
  - Official status pages, Collection announcements, reprocessing notices
- KFM internal:
  - MODIS ETL DAGs and validation
  - STAC/DCAT catalogs and Neo4j event nodes
  - APIs, Story Nodes, and Focus Mode overlays

This directory is the **human‑readable, governed log** of MODIS events. STAC/DCAT/Neo4j
representations are expected to **derive from these Markdown docs**, not vice versa.

---

## 📦 Data & Metadata

### File Naming

MODIS event files MUST follow:

- Pattern:
  - `YYYY-MM-DD-modis-<short-slug>.md`
- Date:
  - Official event **posting date** (UTC).
- Short slug examples:
  - `interruption`
  - `collection-update`
  - `l2-reprocessing`
  - `archive-latency`
  - `alg-change`

Example filenames:

- `2026-02-10-modis-interruption.md`
- `2026-04-01-modis-collection-update.md`

### Required Front Matter (MODIS Event Files)

Each MODIS event doc MUST begin with a YAML block including at least:

- Identity and location:

  - `title`  
    `"🛰️ Kansas Frontier Matrix — MODIS Event: <Short Title>"`
  - `path`  
    `"docs/events/remote-sensing/modis/YYYY-MM-DD-modis-<short-slug>.md"`
  - `version`  
    e.g. `"v11.2.x"`
  - `last_updated`  
    ISO date

- Governance:

  - `release_stage` (e.g., `"Stable / Governed"`)
  - `lifecycle` (e.g., `"Event Record"`)
  - `status` (e.g., `"Active / Informational · External Event Log"`)
  - `doc_kind` = `"Event Log · Remote Sensing"`

- Provider and mission:

  - `provider`: e.g. `"NASA / EOSDIS"`
  - `missions`:
    - `"Terra MODIS"`
    - `"Aqua MODIS"`

- Event core fields:

~~~yaml
event_kind: "product-availability"   # or: "reprocessing" | "algorithm-change" | "collection-update" | "mission-status"
event_id: "modis:event:YYYY-MM-DD:<short-slug>"
event_start: "YYYY-MM-DDThh:mm:ssZ"
event_posted: "YYYY-MM-DD"
event_end: null                      # null until resolved

affected_products:
  - "MOD09"
  - "MYD09"
  - "MOD11"
  - "MYD11"

severity: "low"                      # low | moderate | high | critical

upstream_reference_url: "https://example.modis.nasa.gov/..."
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

Sensor‑specific projects MAY add keys such as `collection_id`, `processing_version`,
`product_shortnames`, but MUST NOT conflict with these base keys.

### Body Structure (MODIS Event Files)

MODIS event docs SHOULD follow this structure:

1. `# 🛰️ <Title>` — H1 plus an identifier or path line.  
2. **Overview** — What happened, where, when, and why it matters.  
3. **Event Summary** — Products affected, severity, expected duration.  
4. **KFM Impact Assessment** — ETL, catalog, graph, API, and UI impacts.  
5. **Downstream Effects** — Domain‑specific implications (agriculture, hydrology, climate, etc.).  
6. **STAC/DCAT/PROV hooks** — ID patterns and mapping guidance.  
7. **Validation & Telemetry** — Checks triggered, classification of gaps.  
8. **Story Node & Focus Mode** — Narrative integration guidance.  
9. **Version History** — Table of changes to the document.  
10. **Governance Footer** — Links to governance and policy docs.  

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

For each MODIS event:

- **Collection**  
  - Prefer a sensor‑specific collection such as `kfm-modis-events`, or use a unified
    `kfm-remote-sensing-events` with a sensor field.
- **Item ID**  
  - SHOULD match `event_id` (e.g., `modis:event:YYYY-MM-DD:<short-slug>`).
- **Geometry**  
  - Kansas‑wide bounding box, or a more constrained region if the event is spatially localized.
- **Temporal**  
  - `properties.datetime` = `event_start`  
  - `properties.start_datetime` / `properties.end_datetime` as applicable.
- **Properties** SHOULD include:
  - `kfm:event_kind`
  - `kfm:affected_products`
  - `kfm:severity`
  - `kfm:upstream_reference_url`
  - Optional `kfm:collection_id`, `kfm:processing_version`.
- **Assets** MAY include:
  - `upstream_notice` — snapshot of NASA/DAAC notice.
  - `kfm_event_md` — rendered HTML of the event document.

STAC JSON SHOULD be stored under:

- `data/stac/events/remote-sensing/modis/<event-id>.json`

and MUST pass STAC validation in CI.

### DCAT

Each MODIS event SHOULD be exposed as a DCAT `dcat:Dataset`:

- `dct:title` ← MODIS event title.  
- `dct:description` ← overview section.  
- `dct:temporal` ← event interval.  
- `dct:spatial` ← Kansas extent or relevant AOI.  
- `dct:publisher` ← KFM / Remote Sensing & Earth Observation Committee.  
- `dcat:distribution`:
  - Markdown source.  
  - Rendered HTML.  
  - STAC Item.  

### PROV-O

Treat each MODIS event as:

- `prov:Entity` — the event record (`event_id`).  
- `prov:Activity` — upstream maintenance/change activity (e.g., `nasa:archive-maintenance`).  
- `prov:Agent` — `nasa:eosdis`, relevant DAAC, and KFM committees.  

Minimal PROV pattern:

~~~text
Entity:   modis:event:YYYY-MM-DD:<short-slug>
Agent:    nasa:eosdis
Activity: nasa:archive-maintenance
Started:  event_start
Ended:    event_end
Status:   ongoing | resolved
~~~

Neo4j ingestion uses these entities and activities to connect events with collections, datasets,
and Story Nodes.

---

## 🧱 Architecture

### Position in the KFM Pipeline

MODIS event docs influence the entire pipeline:

1. **ETL**  
   - MODIS ETL DAGs read event metadata to:
     - Mark missing or delayed products as expected missingness.
     - Gate reprocessing and backfills after Collection updates.
     - Adjust scheduling and retry windows during outages.

2. **STAC/DCAT/PROV**  
   - Event docs generate STAC Items and DCAT Datasets with PROV links.
   - Catalog queries can answer “why are MODIS data missing or different here?”

3. **Neo4j**  
   - Graph nodes (e.g., `:ModisEvent`) store event details and connect to:
     - `:Collection` nodes for MODIS products.
     - `:Pipeline` or `:PipelineRunPattern` nodes for ETL behaviors.
     - Spatial/temporal nodes representing Kansas regions and time windows.

4. **API**  
   - API endpoints surface MODIS events in:
     - Data‑availability responses.
     - Quality and provenance summaries.
     - Cross‑sensor comparison endpoints (MODIS vs. Landsat vs. Sentinel‑2).

5. **Frontend (React / MapLibre / Cesium)**  
   - UI renders:
     - Timeline markers over MODIS time series (e.g., NDVI, LST, snow cover).
     - Map overlays for MODIS event windows.
     - Links from UI annotations back to this README and specific event docs.

6. **Story Nodes / Focus Mode**  
   - Narrative elements explain MODIS‑driven data gaps or product changes.
   - Focus Mode uses event metadata to annotate charts and scenes with “upstream MODIS event”
     labels and links.

---

## 🧪 Validation & CI/CD

Changes under `docs/events/remote-sensing/modis/**` SHOULD trigger CI workflows that:

- Run markdown linting and link checks.  
- Validate front‑matter schema for MODIS event docs.  
- Confirm KFM‑MDP v11.2.6 conformance (headings, directory layout, version history, footer).  
- Validate corresponding STAC Items for affected events, when present.  
- Run security and secret scans to ensure no credentials or PII appear.  

Typical workflow file:

- `.github/workflows/docs-events-modis.yml`

which blocks merges on any validation failure.

---

## 🧠 Story Node & Focus Mode Integration

MODIS events should map cleanly into Story Nodes that explain:

- Why MODIS time series (e.g., NDVI, EVI, albedo, LST) have gaps, steps, or reprocessed
  segments.  
- How Collection or algorithm updates affect long‑term climate and land‑surface indicators.  

Each event doc SHOULD support at least one Story Node pattern, for example:

- **Title:** “MODIS Quiet Days Over Kansas (Feb 2026)”  
  - Facts: outage interval, affected products, cross‑sensor fallback (e.g., Landsat, Sentinel‑2).  

- **Title:** “When Collections Shift the Baseline”  
  - Facts: Collection update or algorithm change that adjusts long‑term MODIS series.  

In Focus Mode:

- **Facts**  
  - Mark MODIS coverage gaps or product changes with clear, data‑backed labels.  

- **Interpretation** (clearly labeled)  
  - Explain how these events influence KFM analyses and visualizations.  

- **Speculation** (optional, clearly labeled and minimal)  
  - Possible long‑term impacts on MODIS weighting vs. other sensors in fusion products.  

---

## ⚖ FAIR+CARE & Governance

- MODIS event docs capture **operational meta‑information**, generally low‑risk.  
- They MUST NOT:
  - Include sensitive coordinates or internal provider‑only operational data.  
  - Expose restricted Indigenous or culturally sensitive locations.  

When events interact with Indigenous lands or sensitive archaeological/ecological sites:

- Use generalized locations and coarse extents.  
- Route concerns through FAIR+CARE and sovereignty policies referenced in the front matter.  

Licensing:

- This README and MODIS event docs: `CC-BY 4.0`.  
- Underlying MODIS data are governed by NASA/EOSDIS licensing and public‑domain rules and
  must be respected independently of this documentation.  

Key governance references:

- `docs/standards/governance/ROOT-GOVERNANCE.md`  
- `docs/standards/faircare/FAIRCARE-GUIDE.md`  
- `docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`  

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                     |
|--------:|-----------:|---------------------------------------------------------------------------------------------|
| v11.2.6 | 2025-12-10 | Initial README for MODIS event directory; aligned with remote-sensing parent and KFM-MDP v11.2.6. |

---

<div align="center">

📑 **Kansas Frontier Matrix — MODIS Event Logs**  
Scientific Insight · Documentation‑First · FAIR+CARE Ethics · Sustainable Intelligence  

[📘 Docs Root](../../../..) · [📂 Remote-Sensing Events](../README.md) · [⚖ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

