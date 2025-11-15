---
title: "🌐 Kansas Frontier Matrix — Web Application & Focus Mode Platform (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly / Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../releases/v10.4.0/manifest.zip"
telemetry_ref: "../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/web-readme-v3.json"
governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Architecture"
intent: "web-platform"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/README.md@v10.3.2"
  - "web/README.md@v10.3.1"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "WebApplication"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../schemas/json/web-readme.schema.json"
shape_schema_ref: "../schemas/shacl/web-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-platform"
event_source_id: "ledger:web/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public Document"
role: "architecture"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next major KFM web platform protocol release"
---

<div align="center">

# 🌐 **Kansas Frontier Matrix — Web Application & Focus Mode Platform**  
`web/README.md`

**Purpose:**  
Define the complete **architecture and behavioral contract** for the Kansas Frontier Matrix (KFM) v10.4 Web Platform,
including: UI/UX design system, rendering pipelines (2D/3D), Focus Mode v2.5+ intelligence, Story Node v3 integration,
STAC/DCAT explorers, provenance overlays, A11y-first patterns, FAIR+CARE governance hooks, and full-stack telemetry
instrumentation.

</div>

---

# 📘 Overview

The **KFM Web Application** is a next-generation spatial-temporal intelligence interface integrating:

- **MapLibre GL** for 2D vector/raster cartography  
- **CesiumJS** for high-fidelity 3D terrain + deep-time exploration  
- **Focus Mode v2.5** for narrative reasoning, entity-centric discovery, and ontology-driven explainability  
- **Story Node v3** narrative units synchronized with map + timeline  
- **STAC/DCAT Explorer** with dataset lineage, COG previews, and temporal slicing  
- **Neo4j-backed reasoning** via REST/GraphQL/JSON-LD  
- **Timeline Engine** powered by D3/Recharts with multi-range brushing  
- **A11y-first React** design compliant with WCAG 2.1 AA  
- **Governance overlays** (CARE, FAIR, provenance, SBOM, SLSA)  
- **OpenTelemetry** telemetry for performance, energy, carbon, and ethical metrics  

The KFM Web Platform is the **public gateway** to the full knowledge system.

---

# 🎯 Purpose

This document exists to:

- Establish the authoritative **KFM v10.4 web architecture specification**.  
- Ensure coherence across all UI, rendering, Focus Mode, timeline, and governance components.  
- Provide a single reference for developers, designers, and FAIR+CARE council reviewers.  
- Guarantee that the web platform aligns with:
  - MCP-DL v6.3  
  - Markdown Rules v10.4  
  - FAIR+CARE standards  
  - KFM v10 architecture (backend, pipelines, Neo4j, STAC)  

**Primary consumers:**  
Frontend engineers, platform architects, FAIR+CARE council, governance reviewers, telemetry/observability engineers.

---

# 📍 Scope

## In Scope

- All code under `web/**` including:
  - UI components (MapView, CesiumView, FocusPanel, StoryNodes)  
  - Pages, hooks, context, theming  
  - API clients (REST, GraphQL, JSON-LD)  
  - A11y, telemetry, governance overlays  
- Mapping over time (2D/3D)  
- Focus Mode & Story Node rendering flows  
- STAC/DCAT dataset exploration  
- Provenance display & FAIR+CARE compliance elements  

## Out of Scope

- Backend pipeline logic  
- ETL, AI training, or data ingestion details  
- Infrastructure configuration outside the web app  

**Related Documents:**

- `src/ARCHITECTURE.md`  
- `src/pipelines/architecture/observability/README.md`  
- `src/pipelines/architecture/reliable-pipelines.md`  
- `docs/standards/markdown_rules.md`  

---

# 📚 Definitions

- **Focus Mode v2.5** — Adaptive reasoning UI driven by ontology-linked narratives, explainability, CARE governance, and
  spatial-temporal synthesis.  
- **Story Node v3** — Narrative + spatial + temporal unit rendered as cards, timelines, and map overlays.  
- **STAC Explorer** — Viewer for STAC Collections/Items, COG previews, temporal slicing, and lineage trees.  
- **Governance Overlay** — UI layer displaying provenance, CARE labels, SBOM identity, and ethical restrictions.  
- **A11y Tokens** — Theme and spacing values ensuring accessibility across components.  
- **Deep-Time Mode** — 3D paleogeography + predictive climate/hydrology layers (2030–2100).  

---

# 🏗 Architecture / Context

## High-Level Architecture

~~~mermaid
flowchart TD
    UI[UI Layer<br/>React · Tailwind · Zustand] --> MV[MapView<br/>MapLibre GL]
    UI --> CV[CesiumView<br/>3D Terrain Engine]
    UI --> FP[FocusPanel<br/>Focus Mode v2 5]
    UI --> SN[StoryNode Cards<br/>Narrative Units]
    UI --> TL[TimelineView<br/>D3 Temporal Engine]
    UI --> LX[Layer Explorer<br/>STAC DCAT]
    FP --> API[API Client<br/>REST · GraphQL · JSON LD]
    MV --> API
    CV --> API
    TL --> API
    SN --> API
    API --> BE[Backend Services<br/>FastAPI · GraphQL · GovHooks]
    BE --> KG[Knowledge Graph<br/>Neo4j]
    BE --> STAC[STAC DCAT Catalogs]
    BE --> GOV[Governance Ledgers<br/>FAIRCARE · SBOM · SLSA]
    BE --> TEL[Telemetry<br/>Energy · Carbon · Drift · A11y]
~~~

The web platform sits atop the backend APIs and is responsible for:

- Rendering  
- Narrative reasoning  
- Data exploration  
- Governance visibility  
- Accessibility compliance  
- Telemetry capture  

---

# ⚙️ Procedures / Implementation

## Component Responsibilities (Summary)

- **MapView** — 2D geographic renderer with STAC-backed layers and temporal filters.  
- **CesiumView** — 3D terrain + predictive overlays (deep time, climate, hydrology).  
- **FocusPanel** — Focus Mode narratives, explainability, CARE filters, provenance chips.  
- **TimelineView** — Temporal brushing, multi-range selection, synchronization with map and stories.  
- **StoryNodes** — Narrative overlay synchronized to map/time with CARE + provenance.  
- **Layer Explorers** — STAC/DCAT search, load, preview, and filtering.  
- **Governance UI** — Provenance badges, CARE labeling, SBOM/SLSA identity.  
- **Telemetry Hooks** — Capture performance, interaction, A11y usage, and energy/carbon estimates.

Implementation details and per-component preconditions/postconditions are further detailed in `web/ARCHITECTURE.md`.

---

# 📑 Data Contracts & Schemas

The Web Platform consumes structured data from backend services:

## Focus Mode API Contract

- Narrative nodes  
- Entity context and relations  
- Explainability vectors (e.g., SHAP outputs)  
- CARE labels and governance flags  
- Spatial/temporal entities and bounds  

## Story Node Schema

Defined in: `schemas/json/story-node.schema.json`

Key fields:

- `id`, `title`, `summary`  
- `narrative.body`, `media`, `alternates`  
- `spacetime.geometry`, `bbox`, `when`  
- `relations[]` (typed links to other entities)  
- STAC export hints and provenance references  

## STAC/DCAT Schemas

- STAC: `stac-spec v1.0.0`  
- DCAT: `DCAT v3.0`  

---

# 🧬 Ontology Alignment

The Web Platform aligns UI concepts to multiple ontologies:

| Ontology   | Mapping                                               |
| ---------- | ----------------------------------------------------- |
| CIDOC-CRM  | UI events → `E7 Activity`; StoryNode → `E31 Document` |
| OWL-Time   | Timeline ranges → `time:TemporalEntity`               |
| GeoSPARQL  | Map features → `geo:hasGeometry`                      |
| PROV-O     | Provenance badges → `prov:wasDerivedFrom`             |
| schema.org | This doc → `WebApplication`                           |
| DCAT 3.0   | Dataset explorer → Dataset/Distribution               |
| STAC 1.0   | Collections/Items are rendered directly               |

---

# 🛰 STAC/DCAT Metadata

The web UI MUST support:

## STAC

- Item/Collection browsing and search.  
- Raster previews and footprint overlays.  
- Asset lineage trees and temporal slicing.  
- COG stats where available.

## DCAT

- Dataset → Distribution mapping.  
- Keyword, theme, spatial, temporal filters.  

Example snippet:

~~~json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "kfm-web-demo-2025",
  "license": "MIT",
  "extent": {
    "spatial": { "bbox": [[-102, 37, -94.6, 40]] },
    "temporal": { "interval": [["1850-01-01T00:00:00Z", null]] }
  }
}
~~~

---

# 📖 Story Node Integration

Story Nodes appear as:

- Narrative cards  
- Timeline markers  
- Spatial overlays  
- 3D extrusions in Cesium (optional)

Web UI responsibilities:

- Render `story_node_id` entities consistently.  
- Apply CARE filtering and redaction where required.  
- Display provenance metadata and source links.  
- Bind narratives to time and space (timeline + map sync).

---

# 🧠 Focus Mode Integration

Focus Mode v2.5 enables:

- Adaptive narrative generation and contextualization.  
- Map + timeline synchronization.  
- Ontology-based explainability and entity clustering.  
- CARE-aware filtering and redaction.  
- Provenance-aware summarization.  
- Multi-source synthesis (documents, rasters, vectors, events).

Boundaries:

- No speculative history or invented events.  
- No invented motives or false attributions.  
- No hallucinated citations or unverified provenance.  

The UI must clearly distinguish between archival content and AI-derived summaries.

---

# 🔐 Ethics & CARE

The UI MUST:

- Display CARE labels prominently on relevant entities and datasets.  
- Show redaction/masking states for generalized geometries.  
- Respect sovereignty and culturally sensitive data.  
- Apply H3 r7 generalization (or equivalent) for heritage and sensitive sites.  
- Provide ethical context warnings in Focus Mode when content may be sensitive.

---

# 🛡 Privacy & Security

- JWT/RBAC where applicable.  
- Rate limiting and query complexity limits for API usage.  
- Secure map tiles and asset URLs.  
- Local sandbox isolation for dangerous or experimental features.  
- No PII is logged by the web app.  
- Provenance and governance information are handled securely and without leakage.

---

# 🧪 Validation & Testing

Validation includes:

- Snapshot tests for core UI components.  
- A11y tests via tooling (e.g., Axe).  
- Telemetry schema validation.  
- STAC/DCAT explorer tests (API + rendering).  
- Focus Mode invariants (CARE, provenance visibility, explainability).  

---

# 📈 Telemetry

Client-side telemetry captures:

- FPS/performance metrics.  
- User interactions (clicks, pans, zooms, focus activations).  
- Layer usage and Story Node view counts (aggregate).  
- Narrative call counts and error codes.  
- Estimated energy and CO₂ for performance analytics.  
- A11y tools usage (e.g., keyboard-only navigation, reduced motion).

Exported to:

- `releases/<version>/focus-telemetry.json`  
- Downstream observability dashboards.

---

# 🎧 Accessibility (WCAG 2.1 AA)

Plain-language summary:

> The KFM Web App helps users explore Kansas history in space and time through maps, timelines, and guided narratives.
> It includes accessibility features such as keyboard navigation, high contrast, and screen reader support.

UI requirements:

- Keyboard navigation for all interactive elements.  
- Reduced-motion modes for sensitive users.  
- Large-text mode support.  
- Semantic HTML and ARIA where needed.  
- Accessible color ramps and high-contrast themes.  
- Focus trapping in modals and dialogs.

---

# 🤖 Machine Extractability

The Web README is designed to be machine-extractable:

- Consistent heading hierarchy.  
- Machine-friendly tables.  
- JSON-LD or schema.org annotations where relevant.  
- Schemas validated by CI.  
- Minimal, stable HTML wrappers.

---

# 📁 Directory Layout

Directory layout, with aligned comments:

~~~text
web/                               # KFM web client root
├── README.md                      # This web platform overview
├── ARCHITECTURE.md                # Detailed web architecture specification
├── public/                        # Static assets served as-is
│   ├── images/                    # Shared static imagery
│   ├── icons/                     # Favicons and app icons
│   ├── manifest.json              # PWA/app metadata
│   ├── robots.txt                 # Robots exclusion rules
│   └── favicon.ico                # Primary favicon
├── src/                           # React/TypeScript SPA source
│   ├── components/                # Reusable UI components
│   ├── pages/                     # Page-level route containers
│   ├── hooks/                     # Custom hooks (useMap, useTimeline, useFocus, etc.)
│   ├── context/                   # React Context providers (time, theme, focus, a11y)
│   ├── services/                  # API clients (REST, GraphQL, STAC/DCAT, telemetry)
│   ├── utils/                     # Helpers, guards, JSON-LD builders, URL tools
│   └── styles/                    # Global styles, tokens, themes, map styling
├── package.json                   # Dependencies and npm scripts
└── vite.config.ts                 # Vite build configuration
~~~

---

# 🕰 Version History

| Version  | Date       | Author            | Summary                                                                                                                      |
|----------|------------|-------------------|------------------------------------------------------------------------------------------------------------------------------|
| v10.4.0  | 2025-11-15 | Web Platform Team | Upgraded to KFM-MDP v10.4; added ontology mapping, CARE, Story Node v3, Focus Mode v2.5, telemetry, and A11y sections.      |
| v10.3.2  | 2025-11-14 | Web Platform Team | Deep architecture rebuild; 3D integration, Focus Mode v2.5, STAC/DCAT Explorer.                                              |
| v10.3.1  | 2025-11-13 | Web Platform Team | Standard update; A11y + STAC improvements.                                                                                   |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
Validated under MCP-DL v6.3 and KFM-MDP v10.4 · FAIR+CARE Certified · Public Document · Version-Pinned  

</div>