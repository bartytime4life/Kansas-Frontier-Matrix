---
title: "🌐 Kansas Frontier Matrix — Web Application Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/ARCHITECTURE.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly / Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../releases/v10.4.0/manifest.zip"
telemetry_ref: "../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/web-architecture-v3.json"
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
  - "web/ARCHITECTURE.md@v10.0.0"
  - "web/ARCHITECTURE.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "WebApplication"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../schemas/json/web-architecture.schema.json"
shape_schema_ref: "../schemas/shacl/web-architecture-shape.ttl"
doc_uuid: "urn:kfm:doc:web-architecture-v10.4.0"
semantic_document_id: "kfm-doc-web-architecture"
event_source_id: "ledger:web/ARCHITECTURE.md"
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

# 🌐 **Kansas Frontier Matrix — Web Application Architecture**  
`web/ARCHITECTURE.md`

**Purpose:**  
Define the complete, FAIR+CARE-aligned **web application architecture** for the Kansas Frontier Matrix (KFM),
structured according to KFM-MDP v10.4.  
This document governs the technical layout, layering model, data flow, governance obligations, accessibility
requirements, and narrative interfaces of the Web Platform (`web/**`).

</div>

---

## 📘 Overview

The KFM Web Platform is the primary interactive, narrative, and exploratory surface for the Kansas Frontier Matrix.

It provides:

- 2D and 3D geospatial exploration (MapLibre and Cesium)  
- Timeline-driven temporal navigation  
- Focus Mode v2.5 for entity-centric reasoning  
- Story Node v3 rendering and contextual narrative sequencing  
- STAC/DCAT dataset exploration  
- Governance overlays for FAIR+CARE and provenance  
- WCAG 2.1 AA–compliant interfaces  
- Telemetry instrumentation and error taxonomies  
- Contract-driven integration with backend API and Knowledge Graph  

This architecture defines responsibilities, boundaries, and flows within the `web/` subsystem.

---

## 🎯 Purpose & Scope

### Purpose

- Establish the canonical **web subsystem architecture**  
- Enforce alignment with global KFM architecture and governance  
- Provide implementation guidance for:
  - 2D/3D visualization  
  - Story Node rendering  
  - Focus Mode interactions  
  - STAC/DCAT integration  
  - Governance surfaces  
  - Telemetry and observability  
  - Accessibility guarantees  

### Scope

**In scope**

- SPA logic, rendering pipelines, state management, contexts, API clients, styles, governance overlays  

**Out of scope**

- Backend schema design  
- ETL pipelines  
- Infrastructure provisioning  

---

## 🧩 System Architecture (Conceptual)

The Web Platform consists of five coordinated layers:

1. **Rendering Layer**  
   MapLibre (2D), Cesium (3D), charts, overlays, markers, geometry, COG previews.

2. **Narrative & Interaction Layer**  
   Story Nodes, Focus Mode, timeline navigation, contextual entity highlighting.

3. **State & Context Layer**  
   React contexts for theme, time, focus, governance, telemetry, accessibility.

4. **API Integration Layer**  
   REST, GraphQL, and STAC/DCAT clients; JSON-LD generation; provenance integration.

5. **Governance & Compliance Layer**  
   CARE labels, provenance chains, A11y contracts, redaction rules, FAIR+CARE visualizations.

---

## 🧱 Internal Directory Structure

web/
├── README.md
├── ARCHITECTURE.md
├── package.json
├── vite.config.ts
├── public/
│   ├── index.html
│   ├── manifest.json
│   ├── icons/
│   └── images/
└── src/
    ├── main.tsx
    ├── App.tsx
    ├── components/
    │   ├── map/
    │   ├── timeline/
    │   ├── focus/
    │   ├── story/
    │   ├── governance/
    │   ├── stac/
    │   └── layout/
    ├── pages/
    ├── hooks/
    ├── context/
    ├── services/
    ├── utils/
    └── styles/  

### Directory Responsibilities

- `web/` — KFM web client root.  
- `README.md` — High-level web platform overview.  
- `ARCHITECTURE.md` — This architecture document.  
- `package.json` — Web dependencies and npm scripts.  
- `vite.config.ts` — Vite build configuration.  
- `public/` — Static assets served as-is.  
- `src/` — TypeScript/React source for the SPA.  
- `src/components/` — Reusable UI building blocks (map, timeline, focus, story, governance, STAC, layout).  
- `src/pages/` — Route-level containers.  
- `src/hooks/` — Custom hooks (`useMap`, `useTimeline`, `useFocus`, etc).  
- `src/context/` — React Context providers (time, theme, focus, accessibility, governance).  
- `src/services/` — API clients (REST, GraphQL, STAC/DCAT, telemetry).  
- `src/utils/` — Helpers, guards, JSON-LD builders, URL tools.  
- `src/styles/` — Global styles, tokens, themes, map styling (see `web/src/styles/README.md`).  

---

## 🔄 Temporal & Spatial Synchronization Model

### Map Synchronization

- `MapView` listens to **TimeContext** and applies filters to:
  - STAC assets  
  - Feature layers  
  - Story Node geometries  
  - Focus Mode highlights  

- Spatial events (click, hover) update **FocusContext**.

### Timeline Synchronization

- Timeline updates propagate to map, Focus Panel, and Story Node lists.  
- Scroll and drag gestures adjust the active time window.  
- Timeline zoom controls aggregation level (decade, year, month).

---

## 📖 Story Node v3 Architecture

### Inputs

- Story Node document (GraphQL).  
- Related entities (graph neighbors).  
- Spatial footprints (GeoJSON).  
- Temporal ranges (OWL-Time compliant).  

### Outputs

- Story Node Cards.  
- Narrative sequences.  
- Micro-map previews.  
- Timeline marks.  
- Focus Mode recommendations.  

### Rendering Rules

- Preserve provenance and CARE labels.  
- Explicitly differentiate:
  - Original historical excerpts.  
  - System-generated summaries.  
  - AI-generated contextual insights.  
- Validate all Story Node payloads against JSON Schema before rendering.

---

## 🎯 Focus Mode v2.5

### Workflow

1. User selects an entity from map, list, story, or timeline.  
2. Focus controller prepares and sends a request (REST or GraphQL).  
3. Backend returns:
   - Core entity fields.  
   - Graph neighborhood.  
   - STAC assets.  
   - CARE/provenance metadata.  
   - AI narratives (if allowed).  
4. Focus Panel renders:
   - Summary and key facts.  
   - Related entities by role and relation type.  
   - Story Node suggestions.  
   - Provenance chain and governance chips.  
   - Spatial and temporal highlights.  

### Frontend Constraints

- Respect `ai_transform_prohibited` flags (no speculative or unverified claims).  
- Mark inferred or low-confidence segments.  
- Always expose provenance chips for model-derived content.  
- Fallback to non-AI descriptions when AI is unavailable or disabled.

---

## 🛰 STAC/DCAT Integration

### STAC

- Collections and Items retrieved from STAC endpoints.  
- COG footprints and vector layers previewed on the map.  
- Asset metadata shown in dedicated panels with provenance details.  

### DCAT

- Dataset summaries listed in DCAT Explorer.  
- Spatial and temporal extents surfaced alongside dataset metadata.  
- DCAT Distributions may link into STAC collections or external services.

---

## 🔐 Governance, Compliance, and CARE Controls

The Web Platform must:

- Display CARE labels clearly on relevant entities and datasets.  
- Enforce redaction and generalization rules (e.g., H3-based masking).  
- Show provenance chains for datasets, story nodes, and AI outputs.  
- Prevent display of non-public or restricted content without appropriate gating.  
- Provide warnings and explanatory text for sensitive or Indigenous data protections.

Governance overlays must remain available even when map or narrative elements degrade.

---

## ♿ Accessibility Architecture (WCAG 2.1 AA)

All UI components must:

- Be fully keyboard accessible with visible focus indicators.  
- Use color palettes that satisfy minimum contrast ratios.  
- Expose correct and minimal ARIA roles.  
- Honor reduced-motion preferences.  
- Provide textual alternatives for map and 3D content.

Accessibility regressions are treated as architecture violations and must block release until resolved.

---

## 📈 Telemetry, Observability, and Error Contracts

### Telemetry

- Performance metrics (LCP, TTI, CLS).  
- Usage events (Focus activations, Story Node opens, STAC previews).  
- Map interactions (zoom, pan, layer toggles).  
- Non-PII error reports.

### Error Taxonomy

- `RenderingError` – component rendering failures.  
- `DataLoadError` – network/request/response issues.  
- `NarrativeError` – Focus narrative retrieval or generation problems.  
- `GovernanceError` – missing or inconsistent CARE/provenance metadata.  
- `A11yError` – accessibility violations.  
- `TelemetryError` – telemetry submission or validation failures.

All error events are forwarded to backend observability systems.

---

## 🧪 Testing, CI/CD, and Validation

The Web Platform must pass:

- TypeScript strict type checks.  
- ESLint/Prettier linting.  
- Stylelint checks for `styles/**`.  
- JSON Schema validation for Story Node and STAC/DCAT payloads.  
- Automated accessibility tests.  
- Production build verification.

GitHub Actions workflows MUST block merges on any failure affecting `web/**`.

---

## 🕰 Version History

Version        Date          Summary  
v10.4.0        2025-11-15    Aligned with KFM-MDP v10.4; refined internal structure, Story Node v3 and Focus v2.5.  
v10.3.2        2025-11-14    Cesium integration; STAC/DCAT explorer upgrades; accessibility refinements.  
v10.3.1        2025-11-13    Timeline synchronization improvements; Focus Mode stability; governance overlays.  
v10.0.0        2025-11-09    Initial v10 web architecture; baseline React/MapLibre layout and Focus Mode v2.  

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
Validated under MCP-DL v6.3 and KFM-MDP v10.4 · FAIR+CARE Certified · Public Document  

</div>