---
title: "🛰️ Kansas Frontier Matrix — Landsat Event Logs"
path: "docs/events/remote-sensing/landsat/README.md"
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
    - "docs/events/remote-sensing/landsat/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
indigenous_rights_flag: false
data_steward: "Remote Sensing & Earth Observation Committee"

ttl_policy: "24 months"
sunset_policy: "Superseded by next Landsat-events README version"

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

doc_uuid: "urn:kfm:doc:events:landsat:readme:v11.2.6"
semantic_document_id: "kfm-landsat-events-readme-v11.2.6"

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

# 🛰️ **Kansas Frontier Matrix — Landsat Event Logs**

`docs/events/remote-sensing/landsat/README.md`

**Purpose**

Define conventions, structure, and governance for **Landsat 8–9 remote-sensing event Markdown
files** (interruptions, reprocessing campaigns, algorithm changes, mission-status events) that
impact the KFM pipeline:

Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode.

[![KFM-MDP v11.2.6](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.6-informational "Markdown Protocol v11.2.6")]() ·
[![Domain: Remote Sensing](https://img.shields.io/badge/Domain-Remote_Sensing-blue "Remote Sensing Domain")]() ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold "FAIR+CARE Compliant")]() ·
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen "Status: Active & Governed")]()

</div>

---

## 📘 Overview

### Scope

This README governs **all Markdown event docs under**:

- `docs/events/remote-sensing/landsat/*.md`

These documents record **upstream Landsat 8–9 events** that affect:

- Deterministic Landsat ETL and backfill behaviour  
- STAC Collections/Items and DCAT datasets for Landsat-derived products  
- Neo4j event/incident graph nodes and relationships  
- API responses and UI indicators (gaps, outages, reprocessing notices)  
- Story Nodes and Focus Mode timelines for satellite narratives over Kansas  

Event types include (non-exhaustive):

- Product availability interruptions (unplanned maintenance, outages)  
- Bulk reprocessing or calibration campaigns  
- Algorithm or product-definition changes (e.g., cloud mask vX → vY)  
- Mission status changes (e.g., safe-mode episodes, orbit changes impacting coverage)

---

## 🗂️ Directory Layout

~~~text
📁 Kansas-Frontier-Matrix/
└── 📁 docs/
    └── 📁 events/
        └── 📁 remote-sensing/
            └── 📁 landsat/
                ├── 📄 README.md                               # This document
                ├── 📄 2025-12-08-landsat-interruption.md       # Landsat 8–9 product outage log
                ├── 📄 YYYY-MM-DD-landsat-<short-slug>.md       # Other event logs (one per event)
                └── 📄 YYYY-MM-DD-landsat-<another-event>.md    # Additional events as needed
~~~

**Rules**

- `README.md` is the **canonical standard** for this directory.  
- **One event per file**, named:  
  - `YYYY-MM-DD-landsat-<short-slug>.md`  
  - Date = official **event posting date (UTC)**.  
  - `<short-slug>` = concise, lowercase, hyphenated label: `interruption`, `l2-reprocessing`, `alg-update`, etc.  
- No nested subfolders here without a **governance RFC**.

---

## 🧭 Context

Landsat events sit **between** upstream providers (USGS/NASA) and KFM’s ETL/catalog/graph pipeline.

- **Upstream**  
  - USGS EROS, NASA mission ops, official bulletins & status pages.  
- **KFM internal**  
  - Landsat ingestion DAGs and validation.  
  - STAC/DCAT catalogs and Neo4j event nodes.  
  - Story Nodes and Focus Mode overlays explaining temporal data gaps.

This directory is the **human-readable, governed log** of those events. Other layers (STAC, Neo4j)
are expected to **derive from these Markdown docs**, not the other way around.

---

## 📦 Data & Metadata

### File Naming

Each event file MUST follow:

- Pattern: `YYYY-MM-DD-landsat-<short-slug>.md`  
- Date = **official event posting date** (not start date).  
- Short slug examples:
  - `interruption`  
  - `l2-reprocessing`  
  - `sr-alg-update`  
  - `thermal-anomaly`  
  - `mission-status`  

Example filenames:

- `2025-12-08-landsat-interruption.md`  
- `2026-03-15-landsat-l2-reprocessing.md`  

### Required Front Matter (per event file)

Each Landsat event doc MUST begin with a YAML block including at least:

- `title`  
  - `"🛰️ Kansas Frontier Matrix — <Landsat Event Title>"`  
- `path`  
  - `"docs/events/remote-sensing/landsat/YYYY-MM-DD-landsat-<short-slug>.md"`  
- `version`  
  - KFM doc version (`v11.2.x`)  
- `last_updated`  
- `release_stage`, `lifecycle`, `status`  
- `doc_kind`  
  - `"Event Log · Remote Sensing"`  
- `provider`  
  - e.g. `"USGS EROS"`, `"NASA"`  
- `missions`  
  - list of `"Landsat 8"`, `"Landsat 9"`, etc.  
- Event fields (minimum):

~~~yaml
event_kind: "product-availability"   # or: "reprocessing" | "algorithm-change" | "mission-status"
event_id: "landsat:event:YYYY-MM-DD:<short-slug>"
event_start: "YYYY-MM-DDThh:mm:ssZ"
event_posted: "YYYY-MM-DD"
event_end: null                      # null until resolved

affected_products:
  - "L8-L1"
  - "L8-L2"
  - "L9-L1"

severity: "low"                      # low | moderate | high | critical

upstream_reference_url: "https://example.usgs.gov/..."
upstream_ticket_id: null
~~~

- Standards and governance:

~~~yaml
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"
~~~

Additional fields are allowed but MUST NOT conflict with these keys.

### Body Structure (per event file)

Event docs SHOULD follow this structure:

1. `# 🛰️ <Title>` — H1 plus a one-line identifier or path.  
2. **Overview** — what happened, where, when, why it matters.  
3. **Event Summary** — key products affected, duration, severity.  
4. **KFM Impact Assessment** — ETL, catalog, graph, API, UI impacts.  
5. **Downstream Effects** — domain-specific implications.  
6. **STAC/DCAT/PROV hooks** — ID patterns and mapping guidance.  
7. **Validation & Telemetry** — what checks fired, how gaps are classified.  
8. **Story Node & Focus Mode** — narrative integration guidance.  
9. **Version History** — table of changes to the document.  

---

## 🌐 STAC, DCAT & PROV Alignment

Each Landsat event SHOULD have matching entries in STAC and DCAT.

### STAC

- Collection (example): `kfm-landsat-events`.  
- Item ID = `event_id` (`landsat:event:YYYY-MM-DD:<short-slug>`).  
- Geometry: Kansas-wide bounding box (or more constrained if appropriate).  
- Temporal:
  - `properties.datetime` = `event_start`.  
  - `properties.start_datetime` / `properties.end_datetime` when applicable.  
- Core properties:
  - `kfm:event_kind`  
  - `kfm:affected_products`  
  - `kfm:severity`  
  - `kfm:upstream_reference_url`  
- Assets:
  - `upstream_notice`: {href, type} (PDF/HTML snapshot).  
  - `kfm_event_md`: rendered HTML of the Markdown doc.  

STAC JSON MUST live under:

- `data/stac/events/remote-sensing/landsat/<event-id>.json`

and pass STAC validation in CI.

### DCAT

For each event, expose a DCAT `dcat:Dataset`:

- `dct:title` ← event title.  
- `dct:description` ← overview section.  
- `dct:temporal` ← event interval.  
- `dct:spatial` ← Kansas extent geometry.  
- `dct:publisher` ← KFM / relevant committee.  
- `dcat:distribution`:
  - Markdown source.  
  - Rendered HTML.  
  - STAC Item.  

### PROV-O

Treat each event as:

- `prov:Entity` — the event record (`event_id`).  
- `prov:Activity` — upstream maintenance/change (e.g. `eros:system-maintenance`).  
- `prov:Agent` — `usgs:eros`, `nasa:landsat`, and KFM committees.  

Minimal pattern:

~~~text
Entity:   landsat:event:YYYY-MM-DD:<short-slug>
Agent:    usgs:eros
Activity: eros:system-maintenance
Started:  event_start
Ended:    event_end
Status:   ongoing | resolved
~~~

These entities & activities are used in Neo4j ingestion and story-level provenance.

---

## 🧱 Architecture

### Position in KFM Pipeline

1. **ETL**  
   - Landsat ETL jobs read event metadata to adapt scheduling (e.g. backoff during outages, requeue after resolution).  

2. **STAC/DCAT/PROV**  
   - Event docs → STAC Items + DCAT Datasets → ingested into catalogs, with PROV links from events to products and pipelines.  

3. **Neo4j**  
   - Nodes like `(:LandsatEvent {event_id, kind, severity, start, end})`.  
   - Relationships (draft, subject to schema review):
     - `(:LandsatEvent)-[:AFFECTS_COLLECTION]->(:Collection)`  
     - `(:LandsatEvent)-[:AFFECTS_PIPELINE]->(:PipelineRunPattern)`  

4. **API**  
   - Endpoints to query events by time, severity, and product.  
   - API responses may include event metadata alongside Landsat data availability flags.  

5. **Frontend (React / MapLibre / Cesium)**  
   - Map and timeline overlays for event windows (“Landsat Quiet Days”).  
   - Tooltips linking to event docs and STAC/DCAT/PROV representations.  

6. **Story Nodes / Focus Mode**  
   - Narrative explanations linked to event nodes and impacted datasets.  
   - Focus Mode uses event metadata to annotate charts and maps with clear “upstream event” labels.  

---

## 🧪 Validation & CI/CD

Event docs MUST pass:

- **Markdown linting** (style, heading order, links).  
- **Front-matter schema validation** (YAML shape for event fields).  
- **Provenance checks** (ID uniqueness, correct `event_kind`, etc.).  
- **STAC validation** for any linked STAC Items.  
- **Security scanning** (no secrets, no PII).  

Recommended workflow:

- `.github/workflows/docs-events-landsat.yml`:
  - Triggers on changes under `docs/events/remote-sensing/landsat/**`.  
  - Runs markdown-lint, front-matter schema validation, STAC validation, and secret/PII scans.  
  - Blocks merge on any failure.  

---

## 🧠 Story Node & Focus Mode Integration

Every event SHOULD define at least one Story Node pattern, e.g.:

- **Title:** “Landsat Quiet Days Over Kansas (Dec 2025)”  
  - **Facts:** product outage interval, affected missions, fallback sensors in use.  

- **Title:** “Upstream Maintenance, Downstream Gaps”  
  - **Facts:** ETL runs waiting, STAC gaps, UI warnings and banners.  

In Focus Mode:

- **Facts**  
  - Mark Landsat coverage gaps on temporal charts and maps with clear event labels.  

- **Interpretation** (clearly labelled)  
  - Explain that gaps are due to upstream maintenance or reprocessing, not missing archives or deletion.  

- **Speculation** (optional, clearly labelled and minimal)  
  - Possible long-term implications for reliance on multi-sensor fusion, shift in temporal weighting to Sentinel-2, etc.  

---

## ⚖ FAIR+CARE & Governance

- **FAIR**  
  - Events are discoverable, documented, and linked to catalogs and graph entities.  
  - Re-use is enabled via stable IDs and mapping into STAC/DCAT/PROV.  

- **CARE & sovereignty**  
  - Landsat events are generally low-risk, operational information.  
  - If an event has implications for Indigenous communities (e.g., imagery policies or access changes), those MUST be captured in the impact sections and routed through the FAIR+CARE Council, without exposing sensitive locations.  

- **Licensing**  
  - This README and associated event docs: `CC-BY 4.0`.  
  - Underlying Landsat data follow USGS/NASA licensing and public-domain status.  

Key governance references:

- `docs/standards/governance/ROOT-GOVERNANCE.md`  
- `docs/standards/faircare/FAIRCARE-GUIDE.md`  
- `docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`  

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                 |
|--------:|-----------:|-----------------------------------------------------------------------------------------|
| v11.2.6 | 2025-12-10 | Initial v11.2.6 README for Landsat event directory; aligned with KFM-MDP and emoji tree. |

---

<div align="center">

📑 **Kansas Frontier Matrix — Landsat Event Logs**  
Scientific Insight · Documentation-First · FAIR+CARE Ethics · Sustainable Intelligence  

[📘 Docs Root](../../..) · [📂 Standards Index](../../../standards/README.md) · [⚖ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
