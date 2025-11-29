---
title: "🌐 Kansas Frontier Matrix — Web Application & Focus Mode Platform (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
review_cycle: "Quarterly · FAIR+CARE Council & Web Architecture Board"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
commit_sha: "<latest-commit-hash>"

sbom_ref: "../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../releases/v11.2.2/manifest.zip"
telemetry_ref: "../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/web-readme-v11.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "web-platform"
role: "architecture"
category: "Web · Architecture · UI · Focus Mode"

fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/README.md@v10.3.1"
  - "web/README.md@v10.3.2"
  - "web/README.md@v10.4.0"
  - "web/README.md@v11.0.0"
previous_version_hash: "<previous-sha256>"

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "WebApplication"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../schemas/json/web-readme-v11.schema.json"
shape_schema_ref: "../schemas/shacl/web-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:web-readme-v11.2.2"
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
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"
  - "content-alteration"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
classification: "Public Document"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next major KFM web platform protocol release"
---

<div align="center">

# 🌐 **Kansas Frontier Matrix — Web Application & Focus Mode Platform (v11)**  
`web/README.md`  

Defines the complete **architecture and behavioral contract** for the Kansas Frontier Matrix (KFM) v11 Web Platform, including:  
UI/UX design system, 2D/3D rendering pipelines, **Focus Mode v3** intelligence, **Story Node v3** integration, STAC/DCAT explorers, provenance overlays, A11y-first patterns, FAIR+CARE governance hooks, and full-stack telemetry instrumentation.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../mcp/MCP-README.md)
· [![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Aligned-orange)](../docs/standards/faircare/FAIRCARE-GUIDE.md)
· [![License: MIT](https://img.shields.io/badge/License-MIT-green)](../LICENSE)

</div>

---

## 📘 1. Overview

The **KFM Web Application** is a spatial–temporal intelligence interface integrating:

- 🗺️ **MapLibre GL** for 2D vector/raster cartography  
- 🌍 **CesiumJS** for high-fidelity 3D terrain and deep-time exploration  
- 🎯 **Focus Mode v3** for entity-centric reasoning, narratives, and explainability  
- 📖 **Story Node v3** narrative units synchronized with map and timeline  
- 📦 **STAC/DCAT Explorer** for dataset discovery, lineage, and temporal slicing  
- 🧠 **Neo4j-backed reasoning** via REST/GraphQL/JSON-LD APIs  
- 🕒 **Timeline Engine** with multi-range brushing and linked filtering  
- ♿ **A11y-first React/TypeScript** design compliant with WCAG 2.1 AA+  
- ⚖️ **Governance overlays** (CARE labels, provenance chips, SBOM/SLSA indicators)  
- 📈 **OpenTelemetry v11** hooks for performance, energy, carbon, and ethics metrics  

The Web Platform is the **primary public entrypoint** into KFM and must consistently reflect:

- FAIR+CARE governance  
- Indigenous data sovereignty  
- Sustainability commitments  
- Security & supply-chain integrity  

---

## 🎯 2. Purpose of this Document

This specification:

- Establishes the **v11 Web Platform architecture** for `web/**`  
- Aligns frontend implementation with:
  - System architecture (`../ARCHITECTURE.md`)  
  - GitHub infrastructure (`../.github/ARCHITECTURE.md`)  
  - Data & validation contracts (`../docs/data/contracts/**`, `../schemas/**`)  
- Sets expectations for:
  - Focus Mode v3 behavior and guardrails  
  - Story Node v3 presentation and interaction patterns  
  - STAC/DCAT exploration workflows  
  - Governance overlays and telemetry hooks  
- Serves as the **review reference** for:
  - Frontend engineers  
  - FAIR+CARE and sovereignty reviewers  
  - A11y and ethics governance  
  - Observability and sustainability analysts  

---

## 📍 3. Scope

### 3.1 In Scope

All code and assets under `web/**`, including:

- React components, pages, layouts, and routing  
- Hooks, context providers, and state management  
- MapLibre/Cesium integration and visualization layers  
- Focus Mode v3 and Story Node v3 presentation logic  
- STAC/DCAT explorer components and dataset previews  
- Governance overlays (CARE labels, provenance, SBOM/SLSA)  
- Telemetry emission for web events and performance metrics  
- Theming, design tokens, and adaptive UI behaviors  

### 3.2 Out of Scope

- Backend ETL/AI pipelines (see `src/pipelines/**`, `src/ai/**`)  
- Low-level storage and indexing internals (DB schemas, data lake layout)  
- CI/CD workflow definitions (see `.github/workflows/**`)  
- Local Neo4j and API infrastructure setup (covered by backend docs)  

**Related Documents:**

- `../ARCHITECTURE.md`  
- `../.github/ARCHITECTURE.md`  
- `../docs/architecture/system_overview.md`  
- `../docs/standards/governance/ROOT-GOVERNANCE.md`  

---

## 📚 4. Key Concepts & Definitions

- **Focus Mode v3** — AI-assisted, entity-centric exploration interface that uses graph context, Story Nodes, and datasets to generate governance-safe explanations.  
- **Story Node v3** — Structured narrative objects (text, time, space, relations) rendered as cards, overlays, and timeline entries (see Story Node schema in `docs/standards/story-nodes/**`).  
- **STAC Explorer** — UI for browsing, filtering, and previewing STAC Collections/Items with map-based previews and lineage links.  
- **DCAT Explorer** — UI for dataset-level metadata browsing, license awareness, and FAIR+CARE attributes.  
- **Governance Overlay** — Visual layer carrying CARE labels, provenance icons, risk flags, and enforcement hints (e.g., masking, generalization).  
- **Deep-Time Mode** — Combined timeline + 3D path mode that visualizes paleogeography and future scenarios (e.g., ancient seas, 2050 climate).  

All concepts must align with the ontologies and policies referenced in `docs/standards/**`.

---

## 🏗 5. High-Level Web Architecture

```mermaid
flowchart TD
    subgraph UI["UI Layer · React/TypeScript"]
      MV["MapView · MapLibre GL"]
      CV["CesiumView · 3D"]
      FP["FocusPanel · Focus Mode v3"]
      SN["StoryNodes · Narrative Cards"]
      TL["TimelineView"]
      LX["Layer Explorer · STAC/DCAT"]
      GOV["GovernanceOverlay"]
    end

    UI --> API["API Client · REST/GraphQL/JSON-LD"]
    API --> BE["Backend Services · FastAPI / GraphQL"]
    BE --> KG["Knowledge Graph · Neo4j"]
    BE --> STAC["STAC/DCAT Catalogs"]
    BE --> GOVDB["Governance Ledgers · FAIR+CARE / SBOM / SLSA"]
    BE --> TEL["Telemetry Backend · OTel v11, energy, carbon, ethics"]
```

The Web Platform is **read-only** against core content (except for local preferences) and must never bypass backend governance or CARE enforcement.

---

## 🗂 6. Web Directory Layout (v11.2.2)

~~~text
web/
├── 📄 README.md                   # This web platform overview (architecture & behavior)
├── 🧱 ARCHITECTURE.md             # Detailed web architecture specification
│
├── 📦 public/                     # Static assets
│   ├── 🖼️ images/
│   ├── 🧿 icons/
│   ├── 📜 manifest.json
│   ├── 🤖 robots.txt
│   └── 🪪 favicon.ico
│
├── 🧩 src/                        # React/TypeScript SPA
│   ├── 🧱 components/             # Map, focus panel, story cards, overlays, dialogs
│   ├── 📄 pages/                  # Route-level containers (Home, Explore, Focus, About)
│   ├── 🧵 hooks/                  # useFocusMode, useTimeline, useMap, useStacExplorer, etc.
│   ├── 🧠 context/                # Theme, Focus, Time, A11y, Governance state providers
│   ├── 🌐 services/               # API clients: REST, GraphQL, STAC/DCAT, telemetry
│   ├── 🛠 utils/                  # Helpers: formatting, schema/utils, JSON-LD builders
│   └── 🎨 styles/                 # CSS/Tailwind, design tokens, map & 3D styles
│
├── 📦 package.json                # Dependencies & npm scripts
├── 📦 package-lock.json           # Deterministic dependency lock
└── ⚙️ vite.config.ts              # Build configuration (Vite)
~~~

All structural changes MUST be reflected here and in `web/ARCHITECTURE.md`.

---

## 🎛 7. Major UI Modules & Responsibilities

### 7.1 MapView (MapLibre GL)

- Render basemaps, historical maps, and STAC-derived overlays.  
- Respond to Focus Mode context (e.g., highlight focal places, events, H3 cells).  
- Indicate generalized vs precise locations, with visual cues for masked sites.  
- Support Story Node footprints (Points, Lines, Polygons, Multi* geometries).

### 7.2 CesiumView (3D)

- Provide 3D views for elevation, extruded features, and time-aware geometry changes.  
- Host deep-time visualizations (e.g., ancient seas, future climate scenarios).  
- Support “fly-through” narratives triggered by Story Nodes or Focus Mode.

### 7.3 FocusPanel (Focus Mode v3)

- Present AI-generated, governance-filtered narratives about the current focus entity.  
- Show provenance chips, CARE labels, and data sources behind each narrative.  
- Provide “Why am I seeing this?” pattern with links to underlying graph entities.  
- Respect transform prohibitions (no speculative or unverified claims).

### 7.4 StoryNode Cards (Story Node v3)

- Render narrative cards with title, summary, spatial footprint, time range, and links.  
- Synchronize with map & timeline (hover/click = highlight on map + timeline).  
- Enforce sovereignty, sensitivity, and masking rules per Story Node metadata.

### 7.5 TimelineView

- Implement multi-range brushing & zoom across full KFM temporal coverage.  
- Coordinate time filters across MapView, CesiumView, FocusPanel, StoryNodes, and STAC layers.  
- Distinguish historical data vs future projections via styling and captions.

### 7.6 Layer Explorer (STAC/DCAT)

- Query STAC Collections & Items (e.g., climate, hydrology, hazards) and DCAT Datasets.  
- Filter by temporal coverage, spatial extent, license, FAIR+CARE attributes.  
- Preview layers directly on MapView/CesiumView with provenance and risk badges.

### 7.7 GovernanceOverlay

- Show CARE labels and sovereignty status for displayed data.  
- Indicate redaction or generalization (e.g., “location generalized to H3 cell for protection”).  
- Convey A11y hints (e.g., high-contrast mode active) and risk indications.

---

## ⚖️ 8. Ethics, FAIR+CARE & Sovereignty

The web layer must:

- Display CARE labels and sovereignty indicators on relevant content.  
- Surface when data or narratives are masked/generalized/redacted.  
- Clearly distinguish between:
  - Archival content  
  - Derived model output  
  - AI-generated textual explanations  
- Avoid manipulative UX patterns around sensitive topics, events, or communities.  
- Follow all policies in:
  - `../docs/standards/faircare/FAIRCARE-GUIDE.md`  
  - `../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`  

Any new UI pattern that touches sensitive or governed content must undergo FAIR+CARE review.

---

## ♿ 9. Accessibility (WCAG 2.1 AA+)

Accessibility requirements include:

- Full keyboard navigation (no trapped focus, logical tab order).  
- Screen reader support (semantic HTML, ARIA roles/labels).  
- High-contrast theme; color is never the sole encoding for meaning.  
- Optional reduced-motion behavior for animated/3D visualizations.  
- Clear focus states, text scaling, and responsive layouts.

Accessibility is tested in CI (Axe, Lighthouse) and manually for key flows (Explore, Focus, Story Node).

---

## 📈 10. Telemetry & Observability

The Web Platform emits telemetry (via OpenTelemetry v11) for:

- Performance metrics (LCP, TTFB, route transitions, render cost)  
- Component-level usage (aggregated, non-PII)  
- A11y usage signals (high contrast, keyboard-only, reduced motion)  
- Focus Mode failures, fallback flows, and error boundaries  

All telemetry:

- Conforms to `../schemas/telemetry/web-readme-v11.json` and related schemas.  
- Excludes PII and any prohibited attributes under FAIR+CARE.  
- Is aggregated into `../releases/<version>/focus-telemetry.json` and the global `github-infra-telemetry.json` bundle.

---

## 🧪 11. Testing & QA

KFM web code MUST be covered by:

- Unit tests (components, hooks, reducers, utils).  
- Integration tests (map/timeline/focus interactions).  
- E2E tests for canonical flows (Explore → Focus → Story Node → STAC).  
- Snapshot tests for critical visual components (where stable).  
- Accessibility tests (Axe, Lighthouse, keyboard-only).  
- Telemetry schema tests (ensuring events match telemetry schemas).  

No changes to `web/**` may be merged without passing these tests in CI.

---

## 🕰 12. Version History

| Version | Date       | Summary                                                                                                  |
|--------:|------------|----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Updated metadata, directory layout, and architecture narrative; aligned with latest Focus Mode v3 & CI/CD. |
| v11.0.1 | 2025-11-27 | Web platform refinement; clarified Focus Mode v3 + Story Node v3 contracts.                             |
| v11.0.0 | 2025-11-24 | v11 upgrade; integrated Focus Mode v3, Story Node v3, STAC/DCAT explorer, and telemetry v11.            |
| v10.4.0 | 2025-11-15 | v10.4 architecture; Focus v2.5, Story Node v3, telemetry v3, FAIR+CARE overlays.                        |
| v10.3.2 | 2025-11-14 | Deep rebuild; 3D integration and initial STAC/DCAT explorer flows.                                       |
| v10.3.1 | 2025-11-13 | Early v10.3 web architecture and A11y improvements.                                                     |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧭 System Architecture](../ARCHITECTURE.md) · [🛡 Governance](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>