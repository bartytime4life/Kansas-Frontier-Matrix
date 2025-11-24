---
title: "🌐 Kansas Frontier Matrix — Web Application Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/ARCHITECTURE.md"
version: "v11.0.0"
last_updated: "2025-11-24"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"

sbom_ref: "../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../releases/v11.0.0/manifest.zip"
telemetry_ref: "../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/web-architecture-v11.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
status: "Active · Enforced"
doc_kind: "Architecture"
intent: "web-platform-architecture"
fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/ARCHITECTURE.md@v10.0.0"
  - "web/ARCHITECTURE.md@v10.3.2"
  - "web/ARCHITECTURE.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "WebApplication"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../schemas/json/web-architecture-v11.schema.json"
shape_schema_ref: "../schemas/shacl/web-architecture-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-architecture-v11.0.0"
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
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
classification: "Public Document"
role: "architecture"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next major KFM web platform protocol release"
---

<div align="center">

# 🌐 **Kansas Frontier Matrix — Web Application Architecture (v11)**  
`web/ARCHITECTURE.md`

**Purpose**  
Define the detailed, FAIR+CARE-aligned **Web Platform architecture** for the Kansas Frontier Matrix (KFM) v11 —  
covering rendering pipelines (2D/3D), narrative systems (Story Node v3), Focus Mode v3 flows, STAC/DCAT explorers,  
governance overlays, accessibility requirements, temporal/spatial synchronization, and integration with the KFM API,  
Knowledge Graph, Tools Platform, and Telemetry systems.

</div>

---

# 📘 1. Architectural Overview

The Web Platform (`web/`) is the **primary cognitive and narrative interface** to KFM. It:

- Presents maps, timelines, and narratives in a coherent, governed, and A11y-compliant way  
- Interfaces with backend services solely through governed APIs (REST + GraphQL + JSON-LD endpoints)  
- Visualizes data and narratives linked by Neo4j graph, STAC/DCAT catalogs, and governance ledgers  
- Implements the **Focus Mode v3** and **Story Node v3** experience  
- Emits telemetry and error data through **OpenTelemetry v11**  

This document formalizes responsibilities, boundaries, and flows within the `web/` subsystem and describes how it fits into the broader KFM v11 architecture.

---

# 🎯 2. Purpose & Scope

## 2.1 Purpose

- Serve as the canonical **architecture specification** for `web/**`.  
- Align Web Platform implementation with:
  - `src/ARCHITECTURE.md` (system-wide view)  
  - `tools/ARCHITECTURE.md` (tools platform)  
  - Validation & governance standards (`tools/validation/**`, `tools/governance/**`)  
- Encode **rendering**, **interaction**, **state management**, and **governance** contracts.  
- Make **FAIR+CARE**, **sovereignty**, and **A11y** non-optional architectural constraints.

## 2.2 Scope

**In scope**

- React SPA structure and routing  
- MapLibre (2D) and Cesium (3D) integrations  
- Shared state via context/hooks (time, focus, theme, A11y, governance)  
- Story Node v3 and Focus Mode v3 flows  
- STAC/DCAT browsing and previews  
- Governance overlays and accessibility overlays  
- Telemetry instrumentation and error taxonomy  

**Out of scope**

- ETL / AI pipelines and model training logic  
- Neo4j schema and backend service implementation  
- Cloud infrastructure, network policy, and container orchestration  

---

# 🧱 3. Internal Directory Structure

The Web Platform directory is organized as:

```text
web/                               # KFM web client root
├── README.md                      # High-level web overview
├── ARCHITECTURE.md                # This architecture document
├── package.json                   # Dependencies and npm scripts
├── vite.config.ts                 # Vite build configuration
│
├── public/                        # Static assets served as-is
│   ├── index.html                 # SPA entry HTML shell
│   ├── manifest.json              # PWA/app metadata
│   ├── icons/                     # Favicons and app icons
│   └── images/                    # Shared static imagery
│
└── src/                           # React/TypeScript SPA source
    ├── main.tsx                   # SPA bootstrap and React root mount
    ├── App.tsx                    # Top-level app shell and routing
    ├── components/                # Reusable UI building blocks
    │   ├── map/                   # MapLibre frames, layers, controls
    │   ├── timeline/              # Timeline track, handles, markers
    │   ├── focus/                 # Focus Mode v3 panels and widgets
    │   ├── story/                 # Story Node cards and detail views
    │   ├── governance/            # CARE/provenance overlays and badges
    │   ├── stac/                  # STAC/DCAT explorer components
    │   └── layout/                # Shells, sidebars, responsive grids
    ├── pages/                     # Page-level route containers (Landing, Explore, Focus, etc.)
    ├── hooks/                     # Custom hooks (useMap, useTimeline, useFocus, useStacExplorer, etc.)
    ├── context/                   # React Context providers (Time, Focus, Theme, A11y, Governance)
    ├── services/                  # REST/GraphQL/STAC/telemetry clients
    ├── utils/                     # Helpers, guards, JSON-LD builders, URL tools
    └── styles/                    # Global styles, tokens, themes, map styling
```

---

# 🧩 4. Layered Architecture

The Web Platform comprises five primary layers:

1. **Rendering Layer**  
   - MapLibre (2D), Cesium (3D), charts, story cards, overlays.

2. **Narrative & Interaction Layer**  
   - Story Node v3 cards & pages, Focus Mode v3 panel, timeline interactions.

3. **State & Context Layer**  
   - React contexts and hooks for time, focus, theming, A11y, governance, map state.

4. **API Integration Layer**  
   - Services for REST/GraphQL, STAC/DCAT queries, JSON-LD serialization, schema-aware responses.

5. **Governance & Compliance Layer**  
   - Visualization of CARE labels, sovereignty flags, provenance, and risk information, plus A11y enforcement.

Each layer must be as independent as possible and avoid directly embedding backend logic or bypassing governance decisions.

---

# 🔄 5. Temporal & Spatial Synchronization

Temporal and spatial synchronization is a **hard architectural requirement**:

- **TimeContext** controls the active temporal window.
- **FocusContext** controls the active entity/story.
- **Map state** tracks current viewport and relevant selection.

**Rules:**

- Time changes via TimelineView update the TimeContext → MapView, StoryNode lists, FocusPanel, and STAC filters all react to this change.
- Map interactions (clicking features) update FocusContext and may adjust recommended Story Nodes and Focus narratives.
- Story Node selections update TimeContext and FocusContext and highlight geometry and intervals accordingly.

All components affected by time or space must consume **TimeContext** and **FocusContext**.  
Local, uncoordinated state must be avoided for cross-component synchronization.

---

# 📖 6. Story Node v3 Integration

Story Nodes are the primary narrative units of KFM.

## 6.1 Inputs

- Story Node v3 payloads (GraphQL/REST), validated against JSON Schema.  
- Geometry and temporal extents derived from Story Node metadata.  
- Relationship graph data (e.g., related places, events, documents).

## 6.2 Rendering Contracts

- **Card Component (StoryCard)**  
  - Displays title, summary, time, place chips, CARE label, provenance chips.  
- **Detail Component (StoryDetail)**  
  - Shows narrative, media, and related nodes with clear sections for:
    - Archival content (quotations)  
    - Structured factual summaries  
    - AI-assisted commentary (if allowed & explicitly labeled)  

All Story Node v3 content must:

- Respect CARE labels and sovereignty restrictions.  
- Show provenance chips linked to provenance records.  
- Provide clear UI hints when AI-assisted content appears.

---

# 🎯 7. Focus Mode v3

Focus Mode is an AI-assisted entity-centric exploration mode:

## 7.1 Focus Flow

1. User selects a focus entity (map feature, story, dataset, search result).  
2. FocusContext updates and triggers API calls to Focus Mode endpoints.  
3. Backend returns:
   - Entity graph neighborhood
   - Story Node v3 references
   - STAC/DCAT dataset links
   - CARE + sovereignty metadata
   - AI narratives & explanations (if allowed)
4. FocusPanel renders a **governance-safe** view:
   - Summary
   - Related story + dataset lists
   - Explainability panel (“Why this?”)
   - Provenance chips and CARE overlays

## 7.2 Constraints

- No hallucinated or unverified claims may be presented as facts.  
- Low-confidence AI inferences must be clearly flagged and optionally hidden based on user settings.  
- AI usage must follow the `ai_focusmode_usage` and `ai_transform_*` rules from front-matter.  
- Explanations must link back to the underlying data (Story Nodes, datasets, graph records).

---

# 🛰 8. STAC/DCAT Explorer Design

## 8.1 STAC Integration

- STAC Collections and Items retrieved via backend STAC APIs.  
- Explorer UI shows:
  - Titles, descriptions, extents, licensing  
  - Asset lists and band information  
  - Links to map previews (MapView)  

## 8.2 DCAT Integration

- DCAT Datasets and Distributions retrieved via DCAT or graph APIs.  
- Explorer UI shows:
  - Dataset metadata (title, description, publisher, license)  
  - Spatial & temporal extents  
  - Cross-links to STAC Collections and Items  

The explorer must:

- Reveal provenance (source, ETL, AI, etc).  
- Expose CARE labels.  
- Respect sovereignty flags (no disallowed downloads).

---

# 🔐 9. Governance & CARE Overlays

Governance overlays in the web UI must:

- Display CARE labels for Story Nodes, datasets, and Focus content.  
- Indicate when geometries are **generalized** or **masked** due to sensitivity.  
- Provide access to provenance chains via badges or expandable sections.  
- Reflect the status of FAIR+CARE certification or outstanding concerns.

The UI is not authorized to override these signals; it only presents them.

---

# ♿ 10. Accessibility Architecture

Accessibility requirements for the Web Platform:

- Semantic HTML structure (headings, landmarks, ARIA where required).  
- Keyboard accessibility for all interactive elements.  
- Visual focus indicators.  
- Support for high-contrast themes and text scaling.  
- Respect for `prefers-reduced-motion`.  
- Alternative text for non-decorative images and icons.  
- Textual summaries for complex map or 3D views when feasible.  

Accessibility tests are part of the test stack and CI gating.

---

# 📈 11. Telemetry & Error Reporting

The Web Platform emits telemetry via:

- In-app telemetry hooks (React contexts and hooks)  
- OTel v11 instrumentation tied into KFM observability stack  

Telemetry includes:

- Performance metrics (WebVitals)  
- Usage metrics (aggregated, de-identified)  
- Error metrics (error taxonomy matched with backend)  
- A11y usage metrics (keyboard nav, high-contrast, reduced-motion toggles)  

Errors are categorized into:

- Rendering errors  
- Data load errors  
- Focus Mode errors  
- Governance/CARE overlay errors  
- Telemetry submission failures  

All telemetry must be free from PII and align with telemetry schemas in `../schemas/telemetry/`.

---

# 🧪 12. Testing & CI/CD Integration

The Web Platform is validated via:

- `tests/unit/web/` — component and hook tests  
- `tests/integration/web/` — cross-component flows (map+timeline+Focus+Story Nodes)  
- `tests/e2e/web-app/` — full user journeys with Playwright/Cypress  
- `tools/ci/docs_validate.yml` — verifies this and related docs against KFM-MDP v11  
- `tools/ci/telemetry_report.yml` — ensures telemetry coverage and schema alignment  
- `tools/ci/faircare_validate.yml` — ensures ethical and CARE-related UI flows behave correctly  

CI/CD is considered **part of** the architecture; tests must align with this document and vice versa.

---

# 🕰 13. Version History

| Version  | Date       | Summary                                                                                                              |
|----------|------------|----------------------------------------------------------------------------------------------------------------------|
| v11.0.0  | 2025-11-24 | Upgraded architecture to KFM-MDP v11; Focus v3 alignment; Story Node v3 flows; telemetry v11; FAIR+CARE & A11y v11. |
| v10.4.0  | 2025-11-15 | v10.4 architecture; Focus v2.5 integration; Story Node v3; improved ontology and telemetry sections.                |
| v10.3.2  | 2025-11-14 | Cesium integration; STAC/DCAT explorer refinement; A11y improvements.                                               |
| v10.0.0  | 2025-11-09 | Initial v10 Web Platform architecture baseline.                                                                     |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
**KFM Web Application Architecture v11** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  
[Back to Web README](./README.md) · [System Architecture](../src/ARCHITECTURE.md) · [Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>