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
Define the *complete architecture and behavioral contract* for the Kansas Frontier Matrix (KFM) v10.4 Web Platform, including:  
UI/UX design system, rendering pipelines (2D/3D), Focus Mode v2.5+ intelligence, Story Node v3 integration, STAC/DCAT explorers, provenance overlays, A11y-first patterns, FAIR+CARE governance hooks, and full-stack telemetry instrumentation.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../docs/README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../docs/standards/faircare.md)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../LICENSE)  
[![A11y](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-blueviolet)]()  
[![Web Status](https://img.shields.io/badge/Web_App-Stable-success)]()

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

The KFM Web Platform is the *public gateway to the full knowledge system*.

---

# 🎯 Purpose

This document exists to:

- Establish the **authoritative KFM v10.4 web architecture specification**.  
- Ensure coherence across all UI, rendering, Focus Mode, timeline, and governance components.  
- Provide a **single reference** for developers, designers, and FAIR+CARE council reviewers.  
- Guarantee that the web platform aligns with:
  - MCP-DL v6.3  
  - Markdown Rules v10.4  
  - FAIR+CARE standards  
  - KFM v10 architecture (backend, pipelines, Neo4j, STAC)  

**Primary consumers:**  
Frontend engineers, platform architects, FAIR+CARE council, governance reviewers, telemetry/observability engineers.

---

# 📍 Scope

### In Scope
- All code under `web/**` including:
  - UI components (MapView, CesiumView, FocusPanel, StoryNodes)
  - Pages, hooks, context, theming
  - API clients (REST, GraphQL, JSON-LD)
  - A11y, telemetry, governance overlays
- Mapping over time (2D/3D)
- Focus Mode & Story Node rendering flows
- STAC/DCAT dataset exploration
- Provenance display & FAIR+CARE compliance elements

### Out of Scope
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

- **Focus Mode v2.5:** Adaptive reasoning UI driven by ontology-linked narratives, SHAP explainability, CARE governance, and spatial-temporal synthesis.  
- **Story Node v3:** Narrative + spatial + temporal unit rendered as cards, timelines, and map overlays.  
- **STAC Explorer:** A viewer for STAC Collections/Items, COG previews, temporal slicing, and lineage trees.  
- **Governance Overlay:** UI layer displaying provenance, CARE labels, SBOM identity, and ethical restrictions.  
- **A11y Tokens:** Theme and spacing values ensuring accessibility across components.  
- **Deep-Time Mode:** 3D paleogeography + predictive climate/hydrology layers (2030–2100).  

---

# 🏗 Architecture / Context

## High-Level Architecture

```mermaid
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
````

The web platform sits atop the **backend APIs** and is responsible for:

* Rendering
* Narrative reasoning
* Data exploration
* Governance visibility
* Accessibility compliance
* Telemetry capture

---

# ⚙️ Procedures / Implementation

### Component Responsibilities Overview

* **MapView:** 2D geographic renderer with STAC layers
* **CesiumView:** 3D terrain, DEM, predictive/climate overlays
* **FocusPanel:** narrative engines, explainability modules, CARE filters
* **TimelineView:** multi-range brushing, map sync, temporal reasoning
* **StoryNodes:** narrative overlay synchronized to map/time
* **Layer Explorers:** STAC/DCAT search, load, preview
* **Governance UI:** provenance badges, CARE labeling, SBOM links
* **Telemetry Hooks:** FPS, energy, user interactions, accessibility usage

Preconditions & Postconditions are described per-component in `web/ARCHITECTURE.md`.

---

# 📑 Data Contracts & Schemas

The web platform consumes structured data from:

### 1. Focus Mode API Contract

* Narrative nodes
* Entity context
* SHAP vectors
* CARE labels
* Spatial/temporal entities

### 2. Story Node Schema

Defined in:
`schemas/json/story-node.schema.json`
Includes:

* `id`, `title`, `summary`
* `narrative.body`, `media`, `alternates`
* `spacetime.geometry`, `bbox`, `when`
* `relations[]`
* STAC export hints

### 3. STAC/DCAT Schemas

* STAC: `stac-spec v1.0.0`
* DCAT: `DCAT v3.0`

---

# 🧬 Ontology Alignment

This web platform aligns to multiple ontologies:

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

### STAC

* Item/Collection search
* Raster previews
* Asset lineage trees
* Temporal slicing
* COG stats

### DCAT

* Dataset → Distribution mapping
* Keyword, theme, spatial, temporal filters

Example snippet:

```json
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
```

---

# 📖 Story Node Integration

Story Nodes appear as:

* Narrative cards
* Timeline markers
* Spatial overlays
* 3D extrusions

Web UI responsibilities:

* Render `story_node_id` entities
* Apply CARE filtering
* Display provenance metadata
* Bind time and space

---

# 🧠 Focus Mode Integration

Focus Mode v2.5 enables:

* Adaptive narrative generation
* Map + timeline sync
* Ontology-based explainability
* CARE-aware filtering
* Identity provenance
* Multi-source synthesis (text, raster, vector, events)

Boundaries:

* No speculative history
* No invented motives
* No hallucinated citations

---

# 🔐 Ethics & CARE

The UI MUST:

* Display CARE labels
* Show redaction/masking states
* Respect sovereignty & culturally sensitive data
* Apply H3 r7 generalization for heritage sites
* Provide ethical context warnings in Focus Mode

---

# 🛡 Privacy & Security

* JWT/RBAC
* Rate limiting
* Query depth/complexity limits
* Secure map tiles
* Local sandbox isolation
* No PII logged
* Secure provenance handling

---

# 🧪 Validation & Testing

Validation includes:

* Snapshot tests for UI components
* A11y tests via Axe-core
* Telemetry schema tests
* STAC/DCAT explorer tests
* Focus Mode invariants (CARE, explainability)

---

# 📈 Telemetry

Client-side telemetry captures:

* FPS/performance
* User interactions
* Layer usage
* Narrative calls
* Energy & CO₂ estimates
* A11y tools usage

Exported to:

```
releases/<version>/focus-telemetry.json
```

---

# 🎧 Accessibility (WCAG 2.1 AA)

Plain-language summary:

> The KFM Web App helps users explore Kansas history in space and time through maps, timelines, and guided narratives. It includes accessibility features such as keyboard navigation, high contrast, and screen reader support.

UI Requirements:

* Keyboard navigation
* Reduced motion
* Large-text mode
* Semantic HTML & ARIA
* Accessible color ramps
* High contrast map themes
* Focus trapping in modals

---

# 🤖 Machine Extractability

* Consistent heading hierarchy
* Machine-friendly tables
* JSON-LD where relevant
* Schemas validated by CI
* Semantic region tags in HTML

---

# ♻️ Dataset Evolution / Deltas

Compared to previous versions:

* **v10.3.2 → v10.4.0:**

  * Upgraded to strict KFM-MDP v10.4 formatting
  * Added ontology alignment
  * Added Story Node v3 + STAC/DCAT details
  * Added ethics, governance, A11y, and telemetry sections
  * Added error taxonomy + explicit scope/purpose

---

# 🧩 Error Taxonomy

* **RenderingError** — map/tile loading failures
* **NarrativeError** — Focus Mode generation failures
* **GovernanceError** — CARE label or masking failure
* **A11yError** — accessibility compliance failures
* **DataLoadError** — STAC/DCAT/network issues
* **TelemetryError** — missing/wrong schema metrics
* **APIError** — REST/GraphQL failure modes

---

# 📁 Directory Layout

```text
web/
├── README.md
├── ARCHITECTURE.md
├── public/
│   ├── images/
│   ├── icons/
│   ├── manifest.json
│   ├── robots.txt
│   └── favicon.ico
├── src/
│   ├── components/
│   ├── pages/
│   ├── hooks/
│   ├── context/
│   ├── services/
│   ├── utils/
│   └── styles/
├── package.json
└── vite.config.ts
```

---

# 🕰 Version History

|     Version | Date       | Author            | Summary                                                                                                                      |
| ----------: | ---------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **v10.4.0** | 2025-11-15 | Web Platform Team | Fully upgraded to KFM-MDP v10.4; added ontology, CARE, Story Node v3, Focus Mode v2.5, telemetry, A11y, governance overlays. |
| **v10.3.2** | 2025-11-14 | Web Platform Team | Deep architecture rebuild; 3D integration, Focus Mode v2.5, STAC/DCAT Explorer.                                              |
| **v10.3.1** | 2025-11-13 | Web Platform Team | Standard update; A11y + STAC improvements.                                                                                   |
| **v10.2.2** | 2025-11-12 | Web Platform Team | Predictive overlays & governance dashboard integration.                                                                      |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT License**
Validated under **Master Coder Protocol v6.3**
FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified
[Back to Web Architecture](./ARCHITECTURE.md) · [Root Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
