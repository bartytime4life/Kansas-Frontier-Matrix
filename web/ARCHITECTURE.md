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
Define the complete, FAIR+CARE-aligned Web Platform architecture for the Kansas Frontier Matrix (KFM), including
rendering pipelines, narrative systems, STAC/DCAT explorers, governance overlays, accessibility requirements,
temporal/spatial synchronization, and integration with the KFM API, Knowledge Graph, and Ops Plane.

</div>

---

# 📘 Overview

The Web Platform (`web/`) is the primary cognitive and narrative interface of the Kansas Frontier Matrix.

It provides:

- 2D and 3D map rendering (MapLibre, Cesium)  
- Timeline-driven temporal navigation  
- Focus Mode v2.5 for entity-centric reasoning  
- Story Node v3 rendering and sequencing  
- STAC/DCAT dataset exploration and previews  
- Governance overlays for FAIR+CARE and provenance  
- WCAG 2.1 AA–compliant user interfaces  
- Telemetry, observability, and structured error reporting  

This document formalizes responsibilities, boundaries, and flows within the `web/` subsystem.

---

# 🎯 Purpose & Scope

## Purpose

- Serve as the canonical architecture specification for `web/**`.  
- Align the Web Platform with `src/ARCHITECTURE.md` and KFM governance standards.  
- Encode rendering, interaction, and state management contracts.  
- Make FAIR+CARE, provenance, and accessibility non-optional architectural constraints.

## Scope

**In scope**

- React SPA structure and routing  
- MapLibre and Cesium integrations  
- Contexts and hooks for shared state  
- Story Node v3 and Focus Mode v2.5 flows  
- STAC/DCAT browsing and previews  
- Governance overlays and accessibility layers  
- Telemetry instrumentation and error taxonomy  

**Out of scope**

- ETL / AI pipelines and model training  
- Neo4j schema design and backend services  
- Infrastructure and deployment primitives  

---

# 🧱 Internal Directory Structure

The Web Platform directory is organized as follows (monospace tree with aligned comments):

    web/                               # KFM web client root
    ├── README.md                      # High-level web overview
    ├── ARCHITECTURE.md                # This architecture document
    ├── package.json                   # Dependencies and npm scripts
    ├── vite.config.ts                 # Vite build configuration
    ├── public/                        # Static assets served as-is
    │   ├── index.html                 # SPA entry HTML shell
    │   ├── manifest.json              # PWA/app metadata
    │   ├── icons/                     # Favicons and app icons
    │   └── images/                    # Shared static imagery
    └── src/                           # React/TypeScript SPA source
        ├── main.tsx                   # SPA bootstrap and React root mount
        ├── App.tsx                    # Top-level app shell and routing
        ├── components/                # Reusable UI building blocks
        │   ├── map/                   # MapLibre frames, layers, controls
        │   ├── timeline/              # Timeline track, handles, markers
        │   ├── focus/                 # Focus Mode panels and widgets
        │   ├── story/                 # Story Node cards and detail views
        │   ├── governance/            # CARE/provenance overlays and badges
        │   ── stac/                  # STAC/DCAT explorer components
        │   └── layout/                # Shells, sidebars, responsive grids
        ├── pages/                     # Page-level route containers
        ├── hooks/                     # Custom hooks (useMap, useTimeline, etc.)
        ├── context/                   # React Context providers (time, focus, theme, a11y)
        ├── services/                  # REST/GraphQL/STAC/telemetry clients
        ├── utils/                     # Helpers, guards, JSON-LD builders, URL tools
        └── styles/                    # Global styles, tokens, themes, map styling

---

# 🧩 System Architecture

The Web Platform is structured into five conceptual layers:

1. **Rendering Layer**  
   MapLibre (2D), Cesium (3D), charts, overlays, and markers.

2. **Narrative & Interaction Layer**  
   Story Node v3 cards and pages, Focus Mode v2.5 panels, timeline navigation, contextual linking.

3. **State & Context Layer**  
   React contexts for time, focus, theme, accessibility, map state, governance, and telemetry.

4. **API Integration Layer**  
   REST/GraphQL clients, STAC/DCAT discovery clients, JSON-LD utilities, schema-aware request/response handling.

5. **Governance & Compliance Layer**  
   CARE labels, provenance chains, redaction/generalization rules, WCAG 2.1 AA accessibility guarantees.

Each layer has clear responsibilities and avoids direct coupling to storage or infrastructure details.

---

# 🔄 Temporal & Spatial Synchronization

Temporal and spatial synchronization is a hard architectural requirement.

- Time changes in the Timeline update TimeContext and propagate to:
  - MapView filters for layers and features  
  - Story Node lists and markers  
  - Focus Mode panels and related entity ordering  

- Map interactions update FocusContext:
  - Selecting a feature on the map sets the active focus entity  
  - Map viewport changes may adjust Story Node or dataset suggestions  

- Story Node selections drive:
  - Map highlighting of footprints  
  - Timeline highlighting of relevant intervals  
  - Focus Mode context for related entities  

All time- or space-aware components must subscribe to TimeContext and FocusContext rather than maintaining
their own unsynchronized state.

---

# 📖 Story Node v3 Integration

Story Nodes are the primary narrative units in KFM.

## Inputs

- Story Node records from GraphQL (validated against the Story Node JSON Schema).  
- Spatial footprints (GeoJSON geometries).  
- Temporal extents aligned with OWL-Time.  
- Relations to entities, datasets, and events from the Knowledge Graph.

## Rendering

- **Story Node Card**  
  - Title and concise summary  
  - Temporal band and place labels  
  - Inline CARE label and provenance chips  
  - Optional media thumbnails  

- **Story Node Detail View**  
  - Full narrative text, clearly segmented into:
    - Archival quotations  
    - System summaries  
    - AI-generated insights (if permitted)  
  - Spatial preview (mini-map)  
  - Related Story Nodes, entities, and datasets  

## Rules

- Story Node payloads must be JSON Schema–valid before rendering.  
- CARE labels and provenance chips must be visible by default.  
- AI-generated content must be clearly labeled and traceable to source data.

---

# 🎯 Focus Mode v2.5

Focus Mode is an entity-centric exploration experience layered over maps, timelines, and stories.

## Flow

1. User selects an entity (map feature, Story Node, list item).  
2. Focus controller updates FocusContext and calls backend Focus API.  
3. Backend returns:
   - Core entity attributes  
   - Graph neighborhood (related entities and relations)  
   - Relevant Story Nodes and datasets  
   - CARE/provenance metadata  
   - Optional AI narrative (if allowed by document-level flags)  
4. Focus Panel renders:
   - Summary and key facts  
   - Relation groups (places, events, documents, datasets)  
   - Story Node recommendations  
   - Provenance chips and governance information  

## Constraints

- Respect `ai_transform_permissions` and `ai_transform_prohibited` from the front matter.  
- Mark inferred or low-confidence segments explicitly.  
- Avoid any speculative claims not grounded in backend data.  
- Provide a non-AI fallback (graph-only context) if AI is disabled or unavailable.

---

# 🛰 STAC/DCAT Exploration

## STAC

- STAC Collections and Items are discovered through STAC endpoints exposed by the backend.  
- MapView previews footprints for selected Items (e.g., COG footprints).  
- Asset metadata (band information, resolution, temporal range) is rendered alongside provenance and license.

## DCAT

- DCAT Datasets are listed in a DCAT Explorer interface.  
- Each dataset view includes:
  - Title, description, publisher  
  - Spatial and temporal extent  
  - Distributions, often linked to STAC Collections or Items  

Both STAC and DCAT views must show clear licensing, provenance, and CARE information, surfaced via Governance
components.

---

# 🔐 Governance & CARE Controls

Governance and CARE constraints are enforced at the UI layer:

- CARE labels must be clearly visible on relevant entities, Story Nodes, and datasets.  
- Provenance chains are rendered as chips or expandable sections listing sources, pipelines, and transformations.  
- Sensitive geometries must be generalized (for example, H3 cells) and labeled as such.  
- Any notices relating to Indigenous data or sensitive sites must be shown alongside affected content.  

The Web Platform must not allow users to bypass governance overlays through configuration or theme changes.

---

# ♿ Accessibility (WCAG 2.1 AA)

Accessibility is a first-class architectural requirement.

- All interactive components must be fully keyboard operable with visible focus indicators.  
- Color contrast ratios must meet or exceed WCAG 2.1 AA thresholds.  
- ARIA roles and labels are used where necessary and kept minimal.  
- Motion and animation honor the `prefers-reduced-motion` setting.  
- Maps and 3D scenes are accompanied by textual summaries where practical.  

Accessibility regressions are treated as release-blocking issues.

---

# 📈 Telemetry & Error Taxonomy

## Telemetry

Telemetry must be non-PII and include:

- Performance metrics (LCP, CLS, TTI, etc.).  
- Usage events (Focus activations, Story Node views, STAC previews).  
- Map interactions (zoom, pan, layer toggles) at aggregate level.  
- Error categories and counts.

## Error Types

- RenderingError – React rendering failures.  
- DataLoadError – network or schema issues.  
- NarrativeError – Focus narrative retrieval or AI pipeline problems.  
- GovernanceError – missing or inconsistent CARE/provenance metadata.  
- A11yError – accessibility test failures.  
- TelemetryError – telemetry submission or validation failures.  

Errors are logged through TelemetryContext and sent to backend observability systems.

---

# 🧪 Testing & CI/CD Validation

The Web Platform must satisfy:

- TypeScript strict type checking (typecheck).  
- ESLint/Prettier linting (lint).  
- Unit/integration tests (test).  
- Stylelint checks for `styles/**`.  
- Optional but recommended: automated accessibility tests.  
- Production build verification (build).  

GitHub Actions workflows for `web/**` must block merges on any failing check.

---

# 🕰 Version History

Version | Date       | Summary  
------- |----------- |---------  
v10.4.0 | 2025-11-15 | Rebuilt under KFM-MDP v10.4; directory tree format stabilized; alignment with Focus v2.5 and Story Node v3.  
v10.3.2 | 2025-11-14 | Cesium integration; STAC/DCAT explorer refinement; A11y improvements.  
v10.3.1 | 2025-11-13 | Timeline synchronization, Focus Mode stabilization, governance overlay tuning.  
v10.0.0 | 2025-11-09 | Initial v10 Web Platform architecture baseline.  

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
Validated under MCP-DL v6.3 and KFM-MDP v10.4 · FAIR+CARE Certified · Public Document · Version-Pinned  

</div>