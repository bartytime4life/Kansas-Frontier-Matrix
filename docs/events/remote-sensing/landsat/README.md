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
    - "docs/events/remote-sensing/landsat/*"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded when Landsat event standard v12 is adopted"

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

Define the conventions, structure, and governance for all **Landsat 8–9 remote-sensing event
Markdown files** (interruptions, algorithm changes, reprocessing campaigns, etc.) that impact:

- Deterministic ETL
- STAC / DCAT / PROV catalogs
- Neo4j event graph
- Earth-observation APIs
- React / MapLibre / Cesium layers
- Story Nodes and Focus Mode timelines

so that every Landsat-related upstream disruption or change is recorded once, deterministically,
and propagated safely through the KFM v11 pipeline.

[![KFM-MDP v11.2.6](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.6-informational "Markdown Protocol v11.2.6")]() ·
[![Domain: Remote Sensing](https://img.shields.io/badge/Domain-Remote_Sensing-blue "Remote Sensing Domain")]() ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold "FAIR+CARE Compliant")]() ·
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen "Status: Active & Governed")]()

</div>

---

## 📘 Overview

### 1. Scope

This README governs **all Markdown event files** under:

- `docs/events/remote-sensing/landsat/*.md`

These documents capture **external events** originating from Landsat upstream providers
(e.g., USGS EROS, NASA) that affect KFM’s ability to:

- Ingest Landsat 8/9 scenes (L1/L2/L3)
- Produce deterministic derived products
- Maintain continuous time-series for Kansas-focused analyses
- Render correct temporal coverage in Story Nodes and Focus Mode

Event examples:

- Product availability interruptions (e.g., unplanned maintenance)
- Bulk reprocessing campaigns (new calibration, new atmospheric correction)
- Product definition changes (e.g., new bands, cloud mask semantics)
- Long-term outages or mission status changes

### 2. Relationship to the KFM Pipeline

Every Landsat event file is treated as a **pipeline-facing contract** that:

1. **Anchors ETL behavior**  
   - When an event is active, ETL treats missing scenes as *expected missingness*, not failures.
2. **Drives catalog annotations**  
   - STAC, DCAT and PROV layers carry explicit references to the event ID.
3. **Populates the graph**  
   - Neo4j holds a typed event node with time bounds, provider, severity and affected products.
4. **Configures UI behavior**  
   - APIs and frontend surfaces indicate data gaps and link back to the event document.
5. **Feeds Story Nodes / Focus Mode**  
   - Timelines visually mark Landsat disruptions with narrative context and links to sources.

---

## 🗂️ Directory Layout

The Landsat event directory MUST follow this layout:

~~~text
docs/
└── events/
    └── remote-sensing/
        └── landsat/
            ├── README.md
            ├── 2025-12-08-landsat-interruption.md
            ├── YYYY-MM-DD-landsat-<short-slug>.md
            └── YYYY-MM-DD-landsat-<another-event>.md
~~~

**Rules**

- **README.md** — This file; defines conventions and governance.
- **One file per event window** — Use ISO date (UTC) of **event posting** in the filename.
- **Short slug** — Lowercase, hyphen-separated, 3–5 tokens (`interruption`, `reprocessing`,
  `alg-update`, etc.).
- No nested subfolders in this directory without governance review.

---

## 🧭 Context

Landsat events live **between** external providers and KFM’s internal pipelines:

- **External sources**  
  - USGS / NASA notifications (status pages, mailing lists, data release notes)
- **Internal responses**  
  - ETL scheduling changes, retries, and backfilling
  - STAC/DCAT catalog gaps and annotations
  - Graph nodes and temporal relationships
  - API responses and UI overlays

This directory is the **human-readable, governance-approved log** that the rest of the KFM
system treats as the single source of truth for “what happened, when, and to which products”
for Landsat.

---

## 📦 Data & Metadata

### 1. File Naming

Each Landsat event file MUST be named:

- Pattern:  
  `YYYY-MM-DD-landsat-<short-slug>.md`
- `YYYY-MM-DD` = date the notification is officially posted (UTC)
- `<short-slug>` = concise, semantic, lowercase (`interruption`, `l2-reprocessing`, `sr-alg-update`)

Examples:

- `2025-12-08-landsat-interruption.md`
- `2026-03-15-landsat-l2-reprocessing.md`

### 2. Front Matter Requirements (Event Files)

Each event file MUST start with a YAML block containing at least:

~~~yaml
title: "🛰️ Kansas Frontier Matrix — <Landsat Event Title>"
path: "docs/events/remote-sensing/landsat/YYYY-MM-DD-landsat-<short-slug>.md"
version: "v11.2.x"
last_updated: "YYYY-MM-DD"

release_stage: "Stable / Governed"
lifecycle: "Event Record"
status: "Active / Informational · External Event Log"

provider: "USGS EROS"
missions:
  - "Landsat 8"
  - "Landsat 9"

event_kind: "product-availability"   # or: "reprocessing" | "algorithm-change" | "mission-status"
event_id: "landsat:event:YYYY-MM-DD:<short-slug>"
event_start: "YYYY-MM-DDThh:mm:ssZ"
event_posted: "YYYY-MM-DD"
event_end: null                      # null until confirmed

affected_products:
  - "L8-L1"
  - "L8-L2"
  - "L9-L1"
severity: "low"                      # low | moderate | high | critical

upstream_reference_url: "https://example.usgs.gov/..."
upstream_ticket_id: null             # if applicable

license: "CC-BY 4.0"
markdown_protocol_version: "KFM-MDP v11.2.6"
---
~~~

Additional fields may be added, but MUST NOT conflict with these keys.

### 3. Body Structure (Event Files)

Event files SHOULD use the following structure (adapt as needed per event):

1. `# 🛰️ <Title>` — H1 with short descriptor and event timing line.
2. **Overview** — Short narrative of what happened and why it matters.
3. **Event Summary** — Bulleted description of products, cause, impact, and expected duration.
4. **KFM Impact Assessment** — Table describing impact on ETL, STAC, DCAT, graph, APIs, UI.
5. **Downstream Effects** — Domain-specific notes (agriculture, hydrology, archaeology, etc.).
6. **Provenance** — PROV-O-style snippet for event entity/activity/agent.
7. **Validation & Telemetry** — Notes on schema drift (if any), expected missingness vs. ETL errors.
8. **Version History** — Table of document versions and summary changes.
9. **Governance Footer** — Links back to ROOT-GOVERNANCE and relevant policy docs.

This ensures consistency across all Landsat events and keeps them compatible with automated
parsers and Story Node generation.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. STAC Mapping

For each Landsat event:

- A STAC **Item** SHOULD be generated under a dedicated `Collection`, e.g.:
  - Collection ID: `kfm-landsat-events`
  - Item ID: same as `event_id` from front matter.
- Geometry:
  - Use a Kansas-wide bounding box for spatial extent.
- Temporal:
  - `properties.datetime` = `event_start`
  - `properties.start_datetime` / `properties.end_datetime` when appropriate.
- Properties SHOULD include:
  - `kfm:event_kind`
  - `kfm:affected_products`
  - `kfm:severity`
  - `kfm:upstream_reference_url`
- Assets MAY include:
  - `upstream_notice` (PDF/HTML snapshot)
  - `kfm_event_md` (rendered HTML of the Markdown doc)

The STAC JSON SHOULD live under:

- `data/stac/events/remote-sensing/landsat/<event-id>.json`

and be validated by the standard STAC CI pipeline.

### 2. DCAT Mapping

Each event is exposed as a DCAT `dcat:Dataset` in the KFM catalog to support search and
federation:

- `dct:title` ← `title`
- `dct:description` ← event Overview text
- `dct:temporal` ← event interval
- `dct:spatial` ← Kansas extent
- `dct:publisher` ← KFM project / relevant committee
- `dcat:distribution`:
  - Markdown source (this file)
  - Rendered HTML
  - STAC Item

### 3. PROV-O Modeling

We treat each event as:

- `prov:Entity` — the event record: `event_id`
- `prov:Activity` — the upstream maintenance/change activity
- `prov:Agent` — upstream provider (e.g., `usgs:eros`) and KFM committee that logged the event

Minimal pattern:

~~~text
Entity:   landsat:event:YYYY-MM-DD:<short-slug>
Agent:    usgs:eros
Activity: eros:system-maintenance
Started:  event_start
Ended:    event_end (nullable)
Status:   ongoing | resolved
~~~

This PROV representation is ingested into Neo4j and linked to affected collections, STAC Items,
and KFM products.

---

## 🧱 Architecture

### 1. Place in the KFM Pipeline

End-to-end chain:

1. **Deterministic ETL**  
   - ETL configuration reads Landsat event metadata to:
     - Back off retries during outages.
     - Mark missing scenes as “expected” for telemetry.
2. **STAC / DCAT / PROV Catalogs**  
   - Event metadata is transformed into STAC Items and DCAT Datasets with PROV links.
3. **Neo4j Graph**  
   - A node (e.g., `:RemoteSensingEvent` / `:LandsatEvent`) is created with:
     - `event_id`, `event_kind`, `start`, `end`, `severity`, `provider`, `doc_path`.
   - Relationships (draft schema, subject to review):
     - `(:LandsatEvent)-[:AFFECTS_COLLECTION]->(:Collection)`
     - `(:LandsatEvent)-[:AFFECTS_PIPELINE]->(:Pipeline)`
4. **API**  
   - REST/GraphQL endpoints expose event timelines and affected product lists.
5. **React / MapLibre / Cesium**  
   - UI components render:
     - Timeline ribbons showing Landsat outages.
     - Map overlays (e.g., hatching for missing-data periods).
6. **Story Nodes & Focus Mode**  
   - Narrative nodes link event context to visible gaps or anomalies in data.

### 2. Boundaries

- This directory is **documentation-only**; no ETL logic is implemented here.
- ETL/graph/API code MUST live under:
  - `src/pipelines/**`
  - `src/graph/**`
  - `src/api/**`
  - `src/web/**`
- Any new graph labels or relationships defined here remain **draft** until approved by the
  ontology / graph schema review.

---

## 🧪 Validation & CI/CD

Landsat event docs participate in standard CI checks:

- **Markdown linting** — style, heading order, links.
- **Front-matter schema validation** — YAML keys and types (event_start, severity, etc.).
- **Provenance checks** — ensure `event_id` is unique and correctly formed.
- **STAC validation (if applicable)** — for generated STAC Items.
- **Security & privacy scans** — ensure no secrets, PII, or sensitive coordinates are present.

Recommended (or existing) workflows:

- `.github/workflows/docs-events-landsat.yml`
  - Runs on PRs touching `docs/events/remote-sensing/landsat/**`.
  - Fails if schema or lint checks fail.
- Release workflows ensure event docs are included in:
  - SBOM
  - Manifest
  - SLSA attestation
  - Telemetry summaries

---

## 🧠 Story Node & Focus Mode Integration

For each Landsat event:

1. A **Story Node v3** SHOULD be generated with:
   - Title: short event name.
   - Spatial extent: Kansas bounding box.
   - Temporal extent: `event_start` → `event_end` (or open-ended).
   - Narrative: short, fact-based summary referencing this Markdown file.
   - Links: upstream notice, STAC Item, graph node ID.
2. Focus Mode uses these nodes to:
   - Explain gaps in Landsat-derived indicators.
   - Annotate time-series charts (NDVI, water extent, etc.) with event markers.
   - Provide contextual tooltips when users hover over missing-data periods.

The body text of each event file SHOULD clearly distinguish:

- **Facts** — backed by upstream notices and KFM telemetry.
- **Interpretation** — KFM’s assessment of likely impact.
- **Speculation** — clearly labeled as such and kept minimal.

---

## ⚖ FAIR+CARE & Governance

- Landsat events typically involve **public, low-risk operational information**.
- No PII or culturally sensitive data SHOULD appear in these docs.
- When an event has implications for Indigenous communities (e.g., imagery impacting sacred
  sites), those considerations MUST be captured in:
  - Impact sections, and
  - Linked governance or sovereignty notes, without revealing precise sensitive locations.

Governance links:

- Root governance:  
  `docs/standards/governance/ROOT-GOVERNANCE.md`
- Markdown protocol:  
  `docs/standards/kfm_markdown_protocol_v11.2.6.md`
- Security policy:  
  `.github/SECURITY.md`

---

## 🕰️ Version History

| Version   | Date       | Summary                                      |
|----------:|------------|----------------------------------------------|
| v11.2.6   | 2025-12-10 | Initial README for Landsat event directory.  |

---

## 🛡️ Governance Footer

This document is governed under **KFM-MDP v11.2.6**, KFM-OP v11, and KFM-PDC v11,
and is subject to FAIR+CARE, security, and sovereignty policies as defined in
`docs/standards/governance/ROOT-GOVERNANCE.md`.


