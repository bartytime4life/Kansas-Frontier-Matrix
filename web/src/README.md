---
title: "💻 Kansas Frontier Matrix — Web Source Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
review_cycle: "Quarterly · FAIR+CARE Council & Web Architecture Board"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-src-readme-v11.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"

data_contract_ref: "../../docs/contracts/data-contract-v3.json"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Overview"
intent: "web-src-overview"
role: "overview"
category: "Web · Source · Architecture · UI"

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
  - "web/src/README.md@v11.0.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: false

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../schemas/json/web-src-readme-v11.schema.json"
shape_schema_ref: "../../schemas/shacl/web-src-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:web-src-readme:v11.2.2"
semantic_document_id: "kfm-doc-web-src-readme"
event_source_id: "ledger:web/src/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
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
sunset_policy: "Superseded upon next web/src overhaul"
---

<div align="center">

# 💻 **Kansas Frontier Matrix — Web Source Overview (v11.2.2)**  
`web/src/README.md`

**Purpose**  
Provide a FAIR+CARE-governed overview of `web/src/**`, the **entire frontend application layer** of the Kansas Frontier Matrix (KFM) Web Platform.  
All React components, contexts, services, styles, pipelines, and utilities under `web/src/` are part of this architecture and MUST conform to:

- KFM-MDP v11.2.2 (Markdown + metadata protocol)  
- MCP-DL v6.3 (documentation-first)  
- FAIR+CARE and sovereignty rules  
- WCAG 2.1 AA+ accessibility requirements  
- KFM v11 system & web architecture contracts  

</div>

---

## 📘 1. Overview

The `web/src/` tree contains the **core React/TypeScript source** for the KFM Web Platform:

- **React 18 + TypeScript (strict)** SPA  
- **Tailwind + design tokens** for accessible theming  
- **MapLibre (2D) + Cesium (3D)** visualization layers  
- **Focus Mode v3** entity-centric reasoning UI  
- **Story Node v3** narrative visualization components  
- **Timeline engine** for temporal navigation and brushing  
- **STAC/DCAT explorers** and dataset views  
- **Governance overlays** for CARE, sovereignty, provenance, licensing & SBOM/SLSA  
- **Accessibility systems** (contexts, hooks, primitives)  
- **Telemetry & sustainability instrumentation** (WebVitals, energy, carbon)  
- **Pipelines & services** orchestrating data flow between UI and KFM backend services  

All logic in this directory must be:

- Deterministic  
- Testable (unit, integration, E2E)  
- FAIR+CARE-compliant  
- Sovereignty-safe  
- WCAG 2.1 AA+ accessible  

---

## 🎯 2. Purpose & Contract for `web/src/`

This document defines:

- The **architecture and layering** of `web/src/**`  
- The **behavioral contract** for Focus Mode v3 and Story Node v3 presentation  
- How **time + space synchronization** works between map, timeline, and focus UI  
- Requirements for:
  - Governance overlays (CARE, sovereignty, provenance)  
  - A11y patterns and primitives  
  - Telemetry emission from frontend code  

This file is the **reference point** for:

- Web engineers implementing or refactoring components  
- Governance and FAIR+CARE reviewers checking UI behavior  
- A11y reviewers evaluating compliance  
- Observability engineers wiring telemetry and error taxonomies  

---

## 🗂 3. Directory Structure (v11.2.2 · Emoji-Aligned)

~~~text
web/src/
├── 📄 README.md                        # This web source overview
├── 🧱 ARCHITECTURE.md                  # Detailed web architecture spec for src layer
│
├── 🚀 main.tsx                         # SPA bootstrap and React root mount
├── 🧩 App.tsx                          # Top-level app shell and routing
│
├── 🧱 components/                      # React UI components (presentational + containers)
│   ├── 🗺️ MapView/                     # 2D map experience (MapLibre GL)
│   ├── 🌍 CesiumView/                  # 3D terrain & deep-time visuals (CesiumJS)
│   ├── 🕒 TimelineView/                # Temporal navigation controls
│   ├── 🎯 FocusMode/                   # Focus Mode v3 panels
│   ├── 📖 Story/                       # Story Node v3 UI components
│   ├── ⚖️ Governance/                  # CARE/provenance/sovereignty overlays and badges
│   ├── 📦 Stac/                        # STAC/DCAT explorer widgets
│   ├── 🧱 Layout/                      # Shells, sidebars, split views, headers/footers
│   └── 🧩 Shared/                      # Primitives: buttons, modals, tabs, tooltips, icons
│
├── 📄 pages/                           # Route-level views (Landing, Explore, Focus, About, etc.)
│
├── 🧵 hooks/                           # Custom hooks (logic, not UI)
│   ├── useMap.ts                      # Map state sync (TimeContext + MapContext)
│   ├── useTimeline.ts                 # Timeline logic & TimeContext orchestration
│   ├── useFocus.ts                    # Focus Mode state machine and API interactions
│   ├── useStoryNodes.ts               # Story Node list/detail state
│   ├── useStacExplorer.ts             # STAC/DCAT browsing and filtering
│   ├── useA11y.ts                     # Accessibility preferences and focus helpers
│   └── useTelemetry.ts                # Telemetry emission helpers (WebVitals, events)
│
├── 🧠 context/                         # React Context providers
│   ├── TimeContext.tsx                # Central time range and granularity
│   ├── FocusContext.tsx               # Current focused entity/story/dataset
│   ├── ThemeContext.tsx               # UI theme (light/dark/high-contrast)
│   ├── A11yContext.tsx                # Reduced motion, large text, screen reader hints
│   ├── GovernanceContext.tsx          # CARE, sovereignty, licensing, risk flags
│   ├── MapContext.tsx                 # Map viewport, layers, and selection state
│   └── UIContext.tsx                  # Shell-level UI state (drawers, modals, toasts)
│
├── 🌐 services/                        # API integration layer (no React here)
│   ├── apiClient.ts                   # REST/GraphQL base client
│   ├── focusService.ts                # Focus Mode API integration
│   ├── storyService.ts                # Story Node v3 retrieval & search
│   ├── stacService.ts                 # STAC catalog + item APIs
│   ├── dcatService.ts                 # DCAT dataset/distribution APIs
│   ├── telemetryService.ts            # Telemetry event submission
│   └── governanceService.ts           # Governance metadata lookups (CARE, sovereignty)
│
├── 🔁 pipelines/                       # Frontend orchestration pipelines
│   ├── focusPipeline.ts               # Focus Mode workflows (fetch + merge graph contexts)
│   ├── storyPipeline.ts               # Story Node flows (selection + fetch + sync)
│   ├── timelinePipeline.ts            # Timeline update → TimeContext propagation
│   └── stacPipeline.ts                # STAC/DCAT search + map/timeline sync
│
├── 🛠 utils/                           # Pure utility modules (no side effects)
│   ├── formatters.ts                  # Formatting helpers (text, dates, numbers)
│   ├── jsonld.ts                      # JSON-LD builders aligned with ontologies
│   ├── guards.ts                      # Runtime type guards, schema guards
│   ├── bbox.ts                        # Bounding box & geometry utilities
│   ├── a11y.ts                        # Accessibility helpers (focus traps, SR text)
│   ├── color.ts                       # WCAG contrast computations & color helpers
│   └── temporal.ts                    # Temporal logic aligned with OWL-Time
│
├── 🎨 styles/                          # Styling and theming system
│   ├── tokens/                        # Design tokens (color, spacing, typography)
│   ├── themes/                        # Theme maps (light, dark, high-contrast)
│   ├── maps/                          # MapLibre/Cesium style configs
│   └── global.css                     # Global CSS (reset, base styles)
│
└── 🧾 types/                           # Shared TypeScript types
    ├── api.ts                         # Core API DTO shapes
    ├── domain.ts                      # Domain entities (Place, StoryNode, Dataset, Event, etc.)
    ├── governance.ts                  # CARE, sovereignty, provenance-related types
    ├── spatial.ts                     # GeoJSON, BBox, H3 types
    ├── temporal.ts                    # Time periods, instants, granularity
    ├── ui.ts                          # UI & component prop contracts
    ├── telemetry.ts                   # Telemetry event types
    └── index.ts                       # Barrel exporting shared types
~~~

---

## 🧬 4. Architectural Layers in `web/src/`

1. **Presentation Layer** (`components/`, `pages/`)  
   - Renders UI based on contexts, services, pipelines, and types.  
   - Contains no direct backend calls; uses hooks and services only.

2. **State & Context Layer** (`context/`, `hooks/`)  
   - Hosts global state for Time, Focus, Theme, A11y, Governance, Map, and UI shell.  
   - Prevents duplication or drift between map, timeline, and Focus components.

3. **Integration Layer** (`services/`)  
   - Handles all communication with backend APIs (REST, GraphQL, STAC/DCAT, telemetry).  
   - Ensures adherence to KFM-PDC v11 data contracts and API schemas.

4. **Pipeline Layer** (`pipelines/`)  
   - Encodes orchestration logic for complex flows (Focus, Story Nodes, STAC, Timeline).  
   - Pure functions (where possible) with clearly documented side effects.

5. **Support Layer** (`utils/`, `styles/`, `types/`)  
   - Shared utilities, design tokens, and type definitions.  
   - Must remain side-effect-free (except for styling).

---

## 🔄 5. Temporal & Spatial Synchronization

Time and space in the web UI must be driven by **TimeContext** and **FocusContext**:

- Time mutations (via Timeline) propagate to:
  - MapView & CesiumView (filters visible features & layers)
  - Story Node lists and highlight windows
  - Focus Mode context and AI reasoning inputs
  - STAC/DCAT filters where applicable

- Focus mutations (via search, map click, Story Node selection):
  - Update `FocusContext`  
  - Highlight relevant geometries & Story Nodes  
  - Re-center timeline & map around the focus entity’s time and place  

**Rules:**

- No component may invent its own global time or focus state outside shared contexts.  
- Synchronization logic belongs in `context/`, `hooks/`, or `pipelines/`, not individual components.

---

## 📖 6. Story Node v3 Presentation

Story Node v3 is rendered by `components/Story/` and orchestrated via `storyPipeline.ts` and `storyService.ts`:

- All Story Node payloads must be validated against the Story Node v3 schema.  
- Story Node UIs must:
  - Show time and space clearly (interval + geometry preview).  
  - Indicate masking/generalization when applied.  
  - Surface provenance: underlying datasets, documents, and agents.  
  - Distinguish archival text, curated summaries, and AI-generated segments.  

Widgets include:

- `StoryCard` — summary for lists and map/timeline overlays.  
- `StoryDetail` — full narrative + provenance + governance overlays.  
- `StoryRelations` — related Places, Events, Datasets, and other Story Nodes.  

---

## 🎯 7. Focus Mode v3 Implementation in `web/src/`

Core Focus Mode v3 logic spans:

- `components/FocusMode/`  
- `context/FocusContext.tsx`  
- `hooks/useFocus.ts`  
- `pipelines/focusPipeline.ts`  
- `services/focusService.ts`  

Behavioral contract:

- All Focus narratives are labeled and visually separated from archival texts.  
- Provenance chips and governance overlays are visible and contextual.  
- Any masked or generalized content must be indicated via labels and legends.  
- Focus Mode must comply with AI safety workflows in `.github/workflows/ai_behavior_check.yml` and `focusmode_mlops.yml`.  

---

## 🛰 8. STAC/DCAT Explorer Integration

STAC/DCAT explorer logic lives in:

- `components/Stac/`  
- `hooks/useStacExplorer.ts`  
- `services/stacService.ts`, `services/dcatService.ts`  
- `pipelines/stacPipeline.ts`  

UI responsibilities:

- Discover STAC Collections/Items and DCAT Datasets from backend APIs.  
- Indicate license, CARE labels, temporal coverage, and spatial extents.  
- Link to MapView/CesiumView for spatial preview and overlay.  
- Allow filtering by:
  - Time window  
  - Geography (bbox, H3)  
  - Category (climate, hydrology, hazards, etc.)  
  - FAIR+CARE attributes  

---

## 🔐 9. Governance, CARE & Sovereignty Rules

Components in `components/Governance/` and `GovernanceContext` must:

- Show CARE labels for datasets and Story Nodes.  
- Surface sovereignty/heritage notices for Indigenous or protected datasets.  
- Indicate when spatial data is generalized or masked due to policy.  
- Prevent UI from displaying precise locations of sensitive sites when not allowed.  

Violation of these rules by new code is considered a governance defect.

---

## ♿ 10. Accessibility Architecture

Accessibility is structured as:

- `A11yContext` for preferences (e.g., high contrast, reduced motion, large text).  
- A shared accessible component library under `components/Shared/` using:
  - Keyboard- and screen-reader-friendly patterns  
  - ARIA roles and attributes where essential  
- Utility helpers in `utils/a11y.ts` for focus management, off-screen text, skip links.  

All significant user flows must be navigable via keyboard and screen reader.

---

## 📈 11. Telemetry & Error Taxonomy

Client-side telemetry is handled by:

- `hooks/useTelemetry.ts`  
- `services/telemetryService.ts`  
- Types in `types/telemetry.ts`  

Emits:

- WebVitals and performance metrics  
- Aggregated interaction events (e.g., STAC search counts, Focus Mode opens)  
- A11y usage metrics (high-contrast usage, keyboard-only sessions)  
- Error events categorized as:
  - `RenderingError`
  - `DataLoadError`
  - `FocusError`
  - `GovernanceOverlayError`
  - `TelemetryError`  

Telemetry must conform to `telemetry_schema` and MAR be aggregated in CI into `focus-telemetry.json`.

---

## 🧪 12. Testing Expectations

Minimum testing requirements for `web/src/**`:

- Unit tests for:
  - Components in `components/**`
  - Hooks in `hooks/**`
  - Utilities in `utils/**`
- Integration tests for:
  - Pipelines (Focus, Story, STAC, Timeline)
  - Combined map/timeline/focus interactions
- E2E tests for:
  - `Home → Explore → Focus → Story Node → STAC` canonical journey
- A11y tests for:
  - Key modals, overlays, navigation, and forms
- Telemetry tests:
  - Event shapes validated against telemetry schemas  

CI must run and pass all relevant tests before merging changes to `web/src/`.

---

## 🕰 13. Version History

| Version | Date       | Summary                                                                                                        |
|--------:|------------|----------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Upgraded metadata & directory layout to v11.2.2; aligned with root & web READMEs; clarified governance/A11y/telemetry roles. |
| v11.0.0 | 2025-11-24 | Upgraded to KFM-MDP v11; clarified layers, enforcement rules, telemetry v11 references.                       |
| v10.4.2 | 2025-11-15 | Expanded directory descriptions; labeled sources; aligned with KFM-MDP v10.4.1.                              |
| v10.3.2 | 2025-11-14 | Added governance & accessibility enhancements; improved Focus/Story integration.                              |
| v10.0.0 | 2025-11-09 | Initial v10 Web Source overview; base React/TS structure and map/timeline scaffolding.                        |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  

[⬅️ Back to Web README](../README.md) · [🧭 System Architecture](../../ARCHITECTURE.md) · [🛡 Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>