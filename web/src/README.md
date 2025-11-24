---
title: "💻 Kansas Frontier Matrix — Web Source Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/README.md"
version: "v11.0.0"
last_updated: "2025-11-24"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-src-readme-v11.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"

data_contract_ref: "../../docs/contracts/data-contract-v3.json"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
status: "Active · Enforced"
doc_kind: "Overview"
intent: "web-src-overview"

fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/src/README.md@v10.0.0"
  - "web/src/README.md@v10.3.2"
  - "web/src/README.md@v10.4.2"

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../schemas/json/web-src-readme-v11.schema.json"
shape_schema_ref: "../../schemas/shacl/web-src-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:web-src-readme-v11.0.0"
semantic_document_id: "kfm-doc-web-src-readme"
event_source_id: "ledger:web/src/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
classification: "Public Document"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next web/src overhaul"
---

<div align="center">

# 💻 **Kansas Frontier Matrix — Web Source Overview (v11)**  
`web/src/README.md`

**Purpose**  
Provide a FAIR+CARE-governed overview of `web/src/**`, the **entire frontend application layer** of the Kansas Frontier Matrix (KFM) Web Platform.  
All React components, contexts, services, styles, and utilities under `web/src/` are part of this architecture and MUST conform to:

- KFM-MDP v11.0 (markdown + metadata protocol)  
- MCP-DL v6.3 (documentation-first)  
- FAIR+CARE and sovereignty rules  
- WCAG 2.1 AA+ accessibility requirements  
- KFM v11 system architecture contracts  

</div>

---

# 📘 1. Overview

The `web/src/` tree contains:

- **React 18 + TypeScript (strict)** application code  
- **Tailwind + design tokens** for accessible UI theming  
- **MapLibre (2D) + Cesium (3D)** visualization layers  
- **Focus Mode v3** entity-centric reasoning UI  
- **Story Node v3** narrative visualization components  
- **Timeline engine** for temporal navigation  
- **STAC/DCAT explorers** and dataset views  
- **Governance overlays** for CARE, sovereignty, provenance, licensing  
- **Accessibility systems** (contexts, hooks, patterns)  
- **Telemetry and sustainability instrumentation** for WebVitals, energy, and carbon  
- **Pipelines, services, and utilities** orchestrating data flow between UI and KFM backend services  

All logic in this directory must be:

- Deterministic  
- Testable (unit, integration, E2E)  
- FAIR+CARE-compliant  
- Sovereignty-safe  
- WCAG 2.1 AA+ accessible  

---

# 🧱 2. Directory Structure (Labeled, Box-Safe)

    web/src/
    ├── README.md                        # This web source overview
    ├── ARCHITECTURE.md                  # Detailed web architecture spec
    │
    ├── main.tsx                         # SPA bootstrap and React root mount
    ├── App.tsx                          # Top-level app shell and routing
    │
    ├── components/                      # React UI components (presentational layer)
    │   ├── MapView/                     # 2D map experience (MapLibre GL)
    │   ├── TimelineView/                # Temporal navigation controls
    │   ├── FocusMode/                   # Focus Mode v3 panels
    │   ├── Story/                       # Story Node v3 UI components
    │   ├── Governance/                  # CARE/provenance overlays and badges
    │   ├── Stac/                        # STAC/DCAT explorer widgets
    │   ├── Layout/                      # Shells, sidebars, split views
    │   └── Shared/                      # Low-level primitives (buttons, modals, tabs)
    │
    ├── pages/                           # Route-level views (Landing, Explore, Focus, About)
    │
    ├── hooks/                           # Custom hooks (logic, not UI)
    │   ├── useMap.ts                    # Map state sync; TimeContext + MapContext
    │   ├── useTimeline.ts               # TimeContext orchestration and timeline logic
    │   ├── useFocus.ts                  # Focus Mode state machine and API calls
    │   ├── useStacExplorer.ts           # STAC/DCAT browsing and filtering
    │   ├── useA11y.ts                   # Accessibility preferences and signals
    │   └── useTelemetry.ts              # Telemetry emission from the front end
    │
    ├── context/                         # React Context providers
    │   ├── TimeContext.tsx              # Central time range and granularity
    │   ├── FocusContext.tsx             # Current focused entity/story/dataset
    │   ├── ThemeContext.tsx             # UI theme (light/dark/high-contrast)
    │   ├── A11yContext.tsx              # Reduced motion, large text, etc.
    │   ├── GovernanceContext.tsx        # CARE, sovereignty, license, and risk flags
    │   ├── MapContext.tsx               # Map viewport and layer selections
    │   └── UIContext.tsx                # App shell state (drawers, modals, toasts)
    │
    ├── services/                        # API integration layer
    │   ├── apiClient.ts                 # REST/GraphQL base client
    │   ├── focusService.ts              # Focus Mode API integration
    │   ├── storyService.ts              # Story Node v3 retrieval and search
    │   ├── stacService.ts               # STAC catalog + item APIs
    │   ├── dcatService.ts               # DCAT dataset/distribution APIs
    │   ├── telemetryService.ts          # Telemetry event submission
    │   └── governanceService.ts         # Governance metadata lookups
    │
    ├── pipelines/                       # Frontend orchestration pipelines
    │   ├── focusPipeline.ts             # Focus Mode workflows (fetch + merge contexts)
    │   ├── storyPipeline.ts             # Story Node flows (selection + fetch + sync)
    │   ├── timelinePipeline.ts          # Timeline update → TimeContext propagation
    │   └── stacPipeline.ts              # STAC/DCAT search + map interaction sync
    │
    ├── utils/                           # Pure utility modules (no side effects)
    │   ├── formatters.ts                # Formatting helpers for text, dates, numbers
    │   ├── jsonld.ts                    # JSON-LD builders and schema-mapped entities
    │   ├── guards.ts                    # Runtime type guards and schema guards
    │   ├── bbox.ts                      # Bounding box and geometry utilities
    │   ├── a11y.ts                      # Accessibility helpers (focus trapping, SR text)
    │   ├── color.ts                     # WCAG contrast computations and helpers
    │   └── temporal.ts                  # Temporal computations aligned with OWL-Time
    │
    ├── styles/                          # Styling and theming system
    │   ├── tokens/                      # Design tokens (color, spacing, typography)
    │   ├── themes/                      # Theme maps (light, dark, high-contrast)
    │   ├── maps/                        # Style definitions for MapLibre/Cesium
    │   └── global.css                   # Global CSS (reset, base styles)
    │
    └── types/                           # Shared TypeScript types
        ├── api.ts                       # Core API DTO shapes
        ├── domain.ts                    # Domain types (Place, StoryNode, Dataset, Event)
        ├── governance.ts                # CARE, sovereignty, provenance types
        ├── spatial.ts                   # GeoJSON, BBox, H3, geometry enums
        ├── temporal.ts                  # Time periods and instants
        ├── ui.ts                        # UI and component prop contracts
        ├── telemetry.ts                 # Telemetry event types
        └── index.ts                     # Barrel exporting shared types

---

# 🧬 3. Architectural Layers in `web/src/`

1. **Presentation Layer**: `components/`, `pages/`  
   - Renders UI based on contexts, services, and pipelines  
   - No direct API calls; uses hooks/services

2. **State & Context Layer**: `context/`, `hooks/`  
   - Provides global state: Time, Focus, Theme, A11y, Governance, Map  
   - Prevents local, unsynchronized state in cross-cutting concerns

3. **Integration Layer**: `services/`  
   - Handles all communication with backend APIs (REST/GraphQL/STAC/DCAT/telemetry)  
   - Responsible for schema & contract adherence

4. **Pipeline Layer**: `pipelines/`  
   - Orchestrates multi-step flows (Focus Mode, Story Node, STAC, Timeline)  
   - Encodes client-side orchestration logic

5. **Support Layer**: `utils/`, `styles/`, `types/`  
   - Shared utilities, styling tokens, and type definitions  
   - Must remain side-effect-free (except for styles)  

---

# 🔄 4. Temporal & Spatial Synchronization

All time and space related components must be driven by **TimeContext** and **FocusContext**:

- Time changes (via `TimelineView`) propagate to:
  - `MapView` (filter visible layers and features)
  - Story Node lists and markers
  - Focus Mode suggestions and context

- Focus changes (via selection or Story Node choice) propagate to:
  - Highlight geometry on the map
  - Scroll or adjust timeline to relevant intervals
  - Update FocusPanel narratives and evidence

**Rules:**

- No component may independently maintain its own “GLOBAL” time or focus state.  
- MapView, TimelineView, FocusMode, and Story components must subscribe to shared contexts.  

---

# 📖 5. Story Node v3 Presentation

Story Node v3 payloads are rendered via components under `components/Story/` and must:

- Be validated against Story Node v3 schemas before rendering  
- Respect CARE labels and sovereignty masking  
- Clearly distinguish:
  - Archival content (citations, quotations)
  - Summaries (curated narrative)
  - AI-generated text (if enabled and allowed)

Widgets include:

- `StoryCard` — summarized view for lists and map/timeline markers  
- `StoryDetail` — full narrative with provenance panel  
- `StoryMapPreview` — generalized map preview with H3-level masking if required  
- `StoryRelations` — related entities and other Story Nodes with relational cues  

---

# 🎯 6. Focus Mode v3 in `web/src/`

Focus Mode v3 is implemented primarily in:

- `components/FocusMode/`  
- `context/FocusContext.tsx`  
- `hooks/useFocus.ts`  
- `pipelines/focusPipeline.ts`  
- `services/focusService.ts`  

The architecture must ensure:

- Every Focus view has provenance chips and CARE overlays  
- AI narratives are clearly labeled and separately styled from archival text  
- Sensitive entities or content trigger warnings or limited views  
- Focus UI does not misrepresent confidence of underlying AI outputs  

---

# 🛰 7. STAC/DCAT Explorer

STAC/DCAT Explorer components:

- `components/Stac/*`  
- `hooks/useStacExplorer.ts`  
- `services/stacService.ts`, `services/dcatService.ts`  

Responsibilities:

- Discover datasets and items via STAC/DCAT APIs  
- Render dataset cards with titles, summaries, license, CARE labels, and time/space coverage  
- Link to MapView for immediate spatial exploration  
- Surface dataset provenance and governance metadata  

---

# 🔐 8. Governance, CARE & Sovereignty

Components under `components/Governance/` and contexts in `GovernanceContext` provide UI-level enforcement of:

- CARE labels (e.g., Public, Indigenous-governed, Restricted)  
- Sovereignty notices for Indigenous datasets or sites  
- Masking indicators when coordinates are generalized  
- Provenance trails for Story Nodes and datasets  

The Web Source must never:

- Show precise coordinates of sensitive sites where policies demand generalization  
- Hide or remove governance cues at the request of users or configuration alone  

---

# ♿ 9. Accessibility Architecture

Accessibility is implemented via:

- `A11yContext` to store user preferences (e.g., large text, high contrast, reduced motion)  
- Shared accessible primitives in `components/Shared/` (button, modal, tabs, tooltips, etc.)  
- Proper ARIA roles and label usage where necessary  
- Semantic use of headings and landmarks  

Testing is done through:

- `tests/unit/web/*`  
- `tests/integration/web/*`  
- `tests/e2e/web-app/*`  

and enforced via CI workflows (e.g., `ui-accessibility.yml`).

---

# 📈 10. Telemetry & Error Taxonomy

`web/src/**` is responsible for client-side emission of:

- WebVitals (LCP, CLS, etc.)  
- Interaction event summaries (de-identified)  
- A11y usage metrics  
- Failure categories:

  - RenderingError  
  - DataLoadError  
  - FocusError  
  - GovernanceOverlayError  
  - TelemetryError  

Telemetry is normalized by `telemetryService.ts` and dashboards built from backend aggregations.

---

# 🧪 11. Testing Expectations

Minimum testing expectations:

- Unit tests for components in `components/**`  
- Hook tests for `hooks/**`  
- Integration tests for `pipelines/**` (Focus, Story, STAC, Timeline)  
- A11y and governance overlay tests for `components/Governance/**`  
- Type and schema guard tests for `types/**` and `utils/guards.ts`  

---

# 🕰 12. Version History

| Version | Date       | Summary                                                                                                 |
|--------:|------------|---------------------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-24 | Upgraded to KFM-MDP v11; clarified layers, enforcement rules, and added telemetry v11 references.       |
| v10.4.2 | 2025-11-15 | Expanded directory descriptions; labeled sources; aligned with KFM-MDP v10.4.1.                        |
| v10.3.2 | 2025-11-14 | Added governance & accessibility enhancements, improved Focus/Story integration.                        |
| v10.0.0 | 2025-11-09 | Initial v10 Web Source overview; base React/TS structure and Map/Timeline scaffolding.                 |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v11.0  

[Back to Web README](../README.md) · [System Architecture](../../src/ARCHITECTURE.md) · [Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>