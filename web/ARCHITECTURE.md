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

The KFM Web Platform is the primary **interactive, narrative, and exploratory surface** for the Kansas Frontier Matrix.

It provides:

- 2D and 3D geospatial exploration (MapLibre and Cesium).  
- Timeline-driven temporal navigation.  
- Focus Mode v2.5 for entity-centric reasoning.  
- Story Node v3 rendering and contextual narrative sequencing.  
- STAC/DCAT dataset exploration.  
- Governance overlays for FAIR+CARE and provenance.  
- WCAG 2.1 AA–compliant interfaces.  
- Telemetry instrumentation and error taxonomies.  
- Contract-driven integration with backend API and Knowledge Graph.

This architecture defines responsibilities, boundaries, and flows within the `web/` subsystem.

---

## 🎯 Purpose & Scope

### Purpose

- Establish the canonical **web subsystem architecture**.  
- Enforce alignment with global KFM architecture.  
- Provide implementation guidance for:
  - 2D/3D visualization,  
  - Story Node rendering,  
  - Focus Mode interactions,  
  - STAC/DCAT integration,  
  - Governance surfaces,  
  - Telemetry and observability,  
  - Accessibility guarantees.

### Scope

**In scope:**  
Core SPA logic, rendering pipelines, state management, context systems, API clients, styles, and governance surfaces.

**Out of scope:**  
Backend schema design, ETL pipelines, data curation workflows, infrastructure provisioning.

---

## 🧩 System Architecture

### Layered Architecture (Conceptual)

The Web Platform consists of five coordinated layers:

1. **Rendering Layer**  
   MapLibre (2D), Cesium (3D), charts, overlays, markers, geometry, COG previews.

2. **Narrative & Interaction Layer**  
   Story Nodes, Focus Mode, timeline navigation, contextual entity highlighting.

3. **State & Context Layer**  
   React contexts for theme, time, focus, governance, telemetry.

4. **API Integration Layer**  
   REST, GraphQL, and STAC/DCAT clients; JSON-LD generation; provenance integration.

5. **Governance & Compliance Layer**  
   CARE labels, provenance chains, A11y contracts, redaction rules, FAIR+CARE visualizations.

---

## 🧱 Internal Directory Structure

The architecture relies on a stable and predictable directory system.

    web/
      README.md
      ARCHITECTURE.md
      package.json
      vite.config.ts
      public/
        index.html
        manifest.json
        icons/
        images/
      src/
        main.tsx
        App.tsx
        components/
          map/
          timeline/
          focus/
          story/
          governance/
          stac/
          layout/
        pages/
        hooks/
        context/
        services/
        utils/
        styles/

Responsibilities:

- components/** – UI pieces for map, story, focus, timeline, governance  
- hooks/** – Core interaction logic (useMap, useTimeline, useFocus, etc.)  
- context/** – Application state providers (time, theme, focus, A11y)  
- services/** – API clients (REST, GraphQL, STAC/DCAT, telemetry)  
- utils/** – Formatting helpers, guards, JSON-LD utilities  
- styles/** – Style tokens, mixins, themes, map styling (see `web/src/styles/README.md`)

---

## 🔄 Temporal & Spatial Synchronization Model

Temporal and spatial synchronization is a core architectural requirement.

### Map Synchronization

- MapView listens to **TimeContext** and applies filters to:  
  - STAC assets,  
  - Feature layers,  
  - Story Node geometries,  
  - Focus Mode highlights.

- Spatial events (click, hover) update **FocusContext**.

### Timeline Synchronization

- Timeline updates propagate to map, Focus Panel, and Story Node lists.  
- Scroll and drag gestures adjust the active time window.  
- Zooming time modifies aggregation level (decade, year, month).

---

## 📖 Story Node v3 Architecture

Story Node rendering supports narrative consistency and entity relationships.

### Inputs

- Story Node document (via GraphQL).  
- Related entities (graph neighbors).  
- Spatial footprints (GeoJSON).  
- Temporal ranges (OWL-Time compliant).

### Outputs

- Story Node Cards  
- Narrative sequences  
- Micro-map previews  
- Timeline marks  
- Focus Mode recommendations

### Rendering Rules

- Must preserve provenance and CARE labels.  
- Must distinguish between:
  - Original historical excerpts,  
  - System-generated summaries,  
  - AI-generated contextual insights.  
- All content must pass JSON Schema validation.

---

## 🎯 Focus Mode v2.5

Focus Mode is a cross-cutting subsystem.

### Workflow Overview

1. User selects entity.  
2. Focus controller prepares request.  
3. Backend resolves:
   - Core fields  
   - Graph neighborhood  
   - STAC assets  
   - CARE metadata  
   - AI narratives (if allowed)  
4. Focus Panel renders:
   - Summary  
   - Related entities  
   - Story Nodes  
   - Provenance chain  
   - Spatial/temporal highlights  

### Frontend Constraints

- AI content must respect **ai_transform_prohibited** fields.  
- Must display provenance chips for any model-derived text.  
- Low-confidence sections must be explicitly marked.

---

## 🛰 STAC/DCAT Architecture

### STAC

- Collections and Items fetched through STAC endpoints.  
- Assets previewed on MapView (COG footprints, vector data).  
- Metadata shown in dataset panels.

### DCAT

- Dataset summaries shown through DCAT Explorer.  
- Spatial/temporal extents mapped to UI components.  
- Distributions integrated into STAC explorer when applicable.

---

## 🔐 Governance, Compliance, and CARE Controls

The Web Platform must:

- Display CARE labels visibly and consistently.  
- Honor redaction and generalization (H3) rules.  
- Show provenance chips for all datasets, entities, and narratives.  
- Prevent display of non-public or restricted content.  
- Support notices for sensitive or Indigenous data protections.

Governance overlays must remain present even in offline or degraded rendering modes.

---

## ♿ Accessibility Architecture (WCAG 2.1 AA)

All UI components must:

- Provide keyboard-accessible interactions.  
- Use sufficient color contrast.  
- Expose ARIA roles.  
- Respect reduced-motion settings.  
- Provide textual equivalents for map/3D content.

Accessibility failures are treated as architectural violations.

---

## 📈 Telemetry, Observability, and Error Contracts

### Telemetry

- Performance metrics (LCP, TTI, CLS).  
- Usage events (Focus Mode activations, Story Node opens).  
- Map interactions (zoom, pan, layer toggles).  
- Error reporting (non-PII).

### Error Taxonomy

- RenderingError  
- DataLoadError  
- NarrativeError  
- GovernanceError  
- A11yError  
- TelemetryError

All errors feed into backend observability dashboards.

---

## 🧪 Testing, CI/CD, and Validation

The Web Platform must pass:

- TypeScript strict type checks.  
- ESLint/Prettier linting.  
- Stylelint checks (styles/**).  
- JSON Schema validation for Story Nodes and STAC responses.  
- Accessibility tests.  
- Build pipeline validation.

GitHub Actions MUST block merges on failure.

---

## 🕰 Version History

Version        Date          Summary  
v10.4.0        2025-11-15    Full rewrite to KFM-MDP v10.4; alignment with Story Node v3 and Focus v2.5.  
v10.3.2        2025-11-14    Cesium integration, STAC/DCAT explorer upgrades, accessibility refinements.  
v10.3.1        2025-11-13    Timeline sync improvements, Focus Mode stability, governance overlays.  
v10.0.0        2025-11-09    Initial v10 architecture.

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
This document is validated under MCP-DL v6.3 and KFM-MDP v10.4.  
FAIR+CARE Certified · Public Document · Version-Pinned

</div>