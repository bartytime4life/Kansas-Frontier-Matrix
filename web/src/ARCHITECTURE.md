---
title: "💻 Kansas Frontier Matrix — Web Source Architecture Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/ARCHITECTURE.md"
version: "v10.4.1"
last_updated: "2025-11-15"
review_cycle: "Quarterly / Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.4.1/sbom.spdx.json"
manifest_ref: "../../releases/v10.4.1/manifest.zip"
telemetry_ref: "../../releases/v10.4.1/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-src-architecture-v3.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Architecture"
intent: "web-src-architecture"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/ARCHITECTURE.md@v10.0.0"
  - "web/src/ARCHITECTURE.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "N/A"
json_schema_ref: "../../schemas/json/web-src-architecture.schema.json"
shape_schema_ref: "../../schemas/shacl/web-src-architecture-shape.ttl"
doc_uuid: "urn:kfm:doc:web-src-architecture-v10.4.1"
semantic_document_id: "kfm-doc-web-src-architecture"
event_source_id: "ledger:web/src/ARCHITECTURE.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-enhancement"
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
sunset_policy: "Superseded upon next major web-src architecture update"
---

<div align="center">

# 💻 **Kansas Frontier Matrix — Web Source Architecture Specification**  
`web/src/ARCHITECTURE.md`

**Purpose:**  
Define the complete **source-level technical architecture** for `web/src/**` in the Kansas Frontier Matrix (KFM)
Web Platform — including UI composition, state management, Focus Mode v2.5 flows, 2D/3D rendering pipelines,
accessibility architecture, FAIR+CARE enforcement, provenance visibility, typed DTO boundaries, STAC/DCAT
integration, and telemetry & sustainability instrumentation.  
This document governs all contributors modifying `web/src/`.

</div>

---

## 📘 Overview

The `web/src/` directory contains all **frontend source code** that powers the KFM Web Platform UI:

- React 18 + TypeScript (strict mode)  
- Tailwind-based design system & A11y tokens  
- MapLibre GL for 2D cartography and STAC-driven layers  
- CesiumJS for 3D terrain, paleogeography, and future overlays  
- Focus Mode v2.5 entity reasoning flows (narrative, explainability, CARE gating)  
- Story Node v3 rendering synced to map and timeline  
- STAC/DCAT dataset explorers and layer controls  
- Governance UI (CARE labels, sovereignty, licenses, provenance trails)  
- Accessibility (WCAG 2.1 AA) as a hard requirement  
- Telemetry & sustainability instrumentation (WebVitals, ethics, A11y events)  

The architecture ensures that changes in `web/src/**` are:

- Deterministic and type-safe  
- Ethically governed and CARE-aware  
- Accessible and observable  
- Compatible with KFM’s global architecture (`src/ARCHITECTURE.md`)

---

## 🎯 Purpose

This specification:

- Defines the **source-layer architecture** for `web/src/**`.  
- Establishes boundaries and responsibilities for components, hooks, context, services, and pipelines.  
- Ensures the source code implements:
  - Focus Mode v2.5 requirements  
  - Story Node v3 rendering rules  
  - STAC/DCAT integration contracts  
  - A11y & FAIR+CARE governance overlays  
  - Telemetry and observability contracts  

**Primary consumers:** web engineers, architects, FAIR+CARE reviewers, SRE/observability teams, and maintainers
responsible for `web/src/**`.

---

## 📍 Scope

### In Scope

- All source files under `web/src/**`, including:
  - `components/**`, `context/**`, `entities/**`, `features/**`, `hooks/**`, `pages/**`, `pipelines/**`, `services/**`,
    `styles/**`, `utils/**`, `types/**`  
- UI-level pipelines (client-only orchestration)  
- Governance and A11y integration at the UI layer  
- Telemetry emission from the web client  

### Out of Scope

- Backend ETL, AI, and pipeline architecture (covered under `src/pipelines/**`)  
- System deployment and infra specifics (CDN, gateways, etc.)  
- Neo4j schema and backend-only modeling details  

---

## 📚 Definitions

- **Source Architecture** — organization, responsibilities, and constraints of `web/src/**` modules.  
- **Feature Slice** — a vertical domain module (e.g., `focus-mode`, `data-explorer`) with related components/hooks/services.  
- **Context Provider** — top-level React provider that manages global state (focus, a11y, theme, time, governance).  
- **Service** — module under `services/` encapsulating calls to REST/GraphQL/STAC/DCAT endpoints.  
- **Pipeline (frontend)** — client-only orchestration layer combining hooks, services, and state to implement flows (e.g.,
  `focusPipeline`, `stacPipeline`, `storyPipeline`, `timelinePipeline`).  
- **Story Node v3** — narrative + spatial + temporal unit rendered by Story Node components, conforming to the Story Node
  schema.  
- **Focus Mode v2.5** — frontend orchestrator that calls backend reasoning endpoints; no heavy AI models run in-browser.

---

## 🧱 High-Level Module Layout

~~~text
web/src/
├── components/    # Presentational React components
├── context/       # Global React Context providers
├── entities/      # Domain-level helpers & adapters
├── features/      # Feature slices (Focus, Timeline, Story, Data Explorer, etc.)
├── hooks/         # Shared hooks (logic, no JSX)
├── pages/         # Route containers (Map, Focus, Story, etc.)
├── pipelines/     # Frontend orchestration pipelines
├── services/      # API, STAC/DCAT, telemetry, governance clients
├── styles/        # Tokens, themes, global styles
├── types/         # Shared TypeScript types and DTOs
└── utils/         # Stateless helper modules
~~~

---

## 🏗 Architecture / Context

### Source Architecture in Context

~~~mermaid
flowchart TD
    UI[UI Components<br/>React · Tailwind] --> CTX[Context Providers]
    UI --> FEAT[Feature Slices]
    UI --> MAP[MapView]
    UI --> TL[TimelineView]
    UI --> FM[Focus Mode]
    UI --> STORY[Story Node Renderer]
    UI --> GOVUI[Governance & A11y UI]

    FEAT --> HK[Custom Hooks]
    HK --> SVC[Services Layer]
    MAP --> SVC
    TL --> SVC
    FM --> SVC
    STORY --> SVC

    SVC --> API[Backend APIs<br/>REST · GraphQL · STAC · DCAT]
~~~

The code in `web/src/**` sits between user interactions and backend APIs, enforcing:

- Type safety (TypeScript + runtime guards)  
- Governance (CARE, sovereignty, provenance)  
- Accessibility (WCAG 2.1 AA)  

at the UI boundary.

---

## ⚙️ Implementation Pattern

Source code implementation follows this layered pattern:

- **Components (`components/**`)**  
  Presentational React components  
  - No business logic  
  - No direct API calls  
  - Receive props from hooks/contexts/pipelines  
  - Emit callback events upward  

- **Hooks (`hooks/**`)**  
  Encapsulate data fetching, transient state, and side-effects  
  - `useMap`, `useTimeline`, `useFocus`, `useStac`, `useTelemetry`, etc.  

- **Context (`context/**`)**  
  Provide global, shared state  
  - TimeContext, FocusContext, ThemeContext, A11yContext, GovernanceContext, MapContext, UIContext  

- **Pipelines (`pipelines/**`)**  
  Compose hooks and services into end-to-end flows  
  - `focusPipeline.ts`  
  - `stacPipeline.ts`  
  - `storyPipeline.ts`  
  - `timelinePipeline.ts`  

- **Services (`services/**`)**  
  Provide typed, governance-aware gateway to backend and catalogs  
  - `apiClient.ts`, `stacService.ts`, `dcatService.ts`, `telemetryService.ts`, `governanceService.ts`  

All changes must respect:

- TypeScript strictness  
- Schema guard validation before rendering  
- Governance and CARE rules  
- WCAG 2.1 AA accessibility  

---

## 📑 Data Contracts & Schemas

`web/src/**` operates on **structured data contracts** rather than untyped blobs:

- API DTOs defined in `types/api.ts`  
- Domain types defined in `types/domain.ts`  
- Governance types in `types/governance.ts`  
- Spatial/temporal types in `types/spatial.ts`, `types/temporal.ts`  
- Story Node v3 types in `types/story.ts`  
- Focus Mode types in `types/focus.ts`  
- STAC & DCAT types in `types/stac.ts`, `types/dcat.ts`  
- Telemetry events in `types/telemetry.ts`  

Runtime validation:

- `utils/guards.ts` (schema / type guards) ensures backend responses conform to expectations  
- Invalid responses are handled via:
  - User-friendly error states  
  - Governance-safe fallbacks (e.g., hiding restricted content)  
  - Telemetry error events for observability  

Contracts map directly to backend JSON Schemas, STAC/DCAT specs, and GraphQL schemas to ensure strong alignment.

---

## 🧬 Ontology Alignment

The web source aligns with KFM’s ontology strategy:

| System     | Mapping                                                          |
|-----------:|------------------------------------------------------------------|
| CIDOC-CRM  | UI-level interactions and Story Nodes bound to CIDOC entities    |
| OWL-Time   | Timeline ranges and temporal fields as `time:TemporalEntity`     |
| PROV-O     | ProvenanceChip / ProvenanceTrail reflect `prov:Entity` links     |
| schema.org | App described as `WebApplication`; Story Nodes as `CreativeWork` |
| STAC/DCAT  | Dataset browsing follows STAC 1.0 and DCAT 3.0 semantics         |

The frontend does not invent ontology; it reflects ontologies exposed by the backend and documentation.

---

## 🛰 STAC/DCAT Metadata

The frontend **consumes**, but does not author, STAC/DCAT metadata:

- `stacService.ts` handles:
  - Collections & Items  
  - Asset metadata  
  - Spatial/temporal extent extraction  

- `dcatService.ts` handles:
  - DCAT v3 Datasets & Distributions  
  - Publisher/licensing metadata  

All flows are:

- Strongly typed against `types/stac.ts` and `types/dcat.ts`  
- Validated via `utils/guards.ts`  
- CARE-governed via `useGovernance.ts` and GovernanceContext  

---

## 📖 Story Node Integration

Story Node v3 integration includes:

- UI components in `components/story/**`:
  - `StoryCard`, `StoryDetail`, `StoryMedia`, `StoryMapPreview`, `StoryRelations`  

- Types in `types/story.ts`:  
  - Narrative, spatial, temporal, and relations structures  

- Pipelines in `pipelines/storyPipeline.ts`:
  - Connect Story Nodes to Focus Mode  
  - Sync with TimeContext and MapContext  

Architectural invariants:

- Story Nodes must pass schema + type checks before rendering  
- CARE labels and provenance chips must be visible where content appears  
- Map and timeline must highlight Story Node footprints and time spans consistently  

---

## 🧠 Focus Mode v2.5 Integration

Client-side Focus Mode architecture:

~~~mermaid
flowchart LR
    U[User selects entity] --> C[useFocus (Focus Controller)]
    C --> Q["/api/focus/{id}"]
    Q --> R[Focus DTO<br/>Narrative + Context]
    R --> N[StoryNode Composer]
    R --> X[Explainability Layer]
    R --> E[Ethics & CARE Guard]
    N --> MV[MapView Highlights]
    N --> TL[Timeline Highlights]
~~~

- `hooks/useFocus.ts` manages:
  - Active focus entity + type  
  - Loading/error state  
  - Governance/A11y constraints  

- `pipelines/focusPipeline.ts` orchestrates:
  - Focus API calls  
  - Story Node suggestions  
  - Map and timeline highlights  
  - Explainability metadata injection  

No AI model runs in-browser; all AI content comes from backend services and is labeled as such.

---

## 🔐 Ethics & CARE Requirements

`web/src/**` must:

- Apply CARE labels when rendering content about:
  - Indigenous data  
  - Sovereignty-related places  
  - Culturally sensitive sites  

- Use H3 (or similar) spatial generalization for sensitive sites  
- Avoid revealing:
  - Exact coordinates  
  - Overly precise temporal labels without proper context  

- Show:
  - SovereigntyNotice for relevant layers  
  - CAREBadge and MaskingIndicator where masking is in effect  
  - AIGeneratedTag or equivalent for AI-derived text  

Speculative narrative or invented history at the UI layer is **prohibited**.

---

## 🛡 Governance Architecture

The source architecture enforces governance by:

- Rendering license, provenance, and CARE metadata via governance components  
- Using GovernanceContext + `useGovernance.ts` to:
  - Check rules before rendering  
  - Gate or generalize restricted content  
  - Emit governance telemetry events  

- Enforcing:
  - No bypass of masking/generalization in MapView  
  - No bypass of CARE warnings in Focus Mode or Story Nodes  
  - No bypass of licensing display requirements in dataset UIs  

Governance rules are validated by CI via `faircare-validate` workflows.

---

## 🧪 Validation & Testing

Validation in `web/src/**` includes:

- **TypeScript strict** (`npm run typecheck`)  
- **Linting** (`npm run lint`)  
- **Unit tests** (components/hooks/utils)  
- **Integration tests**:
  - Map + Timeline + Focus sync  
  - Story + Focus + Map interplay  
- **A11y tests** (axe-core, Jest integration)  
- **Governance tests**:
  - CARE enforcement  
  - Sovereignty masking  
  - Provenance visibility  
- **Telemetry tests**:
  - Event shape validity  
  - Aggregation behavior  

CI workflows:

- `web-build.yml` — build + typecheck  
- `web-lint.yml` — lint + format checks  
- `web-test.yml` — unit + integration tests  
- `telemetry-export.yml` — telemetry integrity  
- `faircare-validate.yml` — CARE and governance compliance  

---

## 📈 Telemetry Architecture

Telemetry in `web/src/**` is handled by:

- `hooks/useTelemetry.ts` — collects:
  - WebVitals  
  - UI interactions  
  - Map/timeline events  
  - Focus Mode usage  
  - Story Node engagement  
  - A11y preference usage  

- `services/telemetryService.ts` — sends:
  - Non-PII, aggregate events  
  - Schema-validated payloads  
  - Release-bundled metrics  

Telemetry feeds:

```text
releases/<version>/focus-telemetry.json
````

and drives sustainability and UX dashboards.

---

## 🎧 Accessibility (WCAG 2.1 AA)

Accessibility principles are enforced at the architecture level:

* All interactive components must be:

  * Keyboard operable
  * Screen-reader friendly
  * Focus-visible
  * Respectful of reduced-motion preferences

* Styles must:

  * Use WCAG AA-compliant color contrasts
  * Provide accessible color ramps for map & charts

* Layout must:

  * Organize content with semantic landmarks (`<main>`, `<nav>`, `<header>`, `<aside>`)
  * Maintain logical heading order

A11y test failures are treated as **release-blocking**.

---

## 🤖 Machine Extractability

This document and all architecture docs are:

* YAML-front-matter tagged
* Heading-structured for NLP/AI ingestion
* Free of nested conflicting fences (inner code uses `~~~`)
* Suitable for tools that:

  * Build architecture diagrams
  * Validate module boundaries
  * Index documentation for search

---

## 🛡 Privacy & Security

`web/src/**` must:

* Avoid logging PII
* Not embed secrets or privileged tokens
* Respect CSP and security headers from infra
* Use safe defaults in API clients (timeouts, retries, error redaction)

Security-sensitive docs live in `.github/SECURITY.md` and backend security specs; `web/src/` must not contradict them.

---

## 📁 Directory Layout (Summary)

```text
web/src/
├── ARCHITECTURE.md    # This document
├── README.md          # Developer overview
├── components/        # UI components
├── context/           # Context providers
├── entities/          # Domain helpers
├── features/          # Feature slices
├── hooks/             # Custom hooks
├── pages/             # Route containers
├── pipelines/         # Orchestration pipelines
├── services/          # API + STAC/DCAT + telemetry clients
├── styles/            # Styling system
├── types/             # Shared TS types
└── utils/             # Stateless helpers
```

---

## 🕰 Version History

| Version | Date       | Author / Team     | Summary                                                                                            |
| ------: | ---------- | ----------------- | -------------------------------------------------------------------------------------------------- |
| v10.4.1 | 2025-11-15 | Web Platform Team | Aligned architecture spec with new MapView/TimelineView/FocusMode structures and updated pipelines |
| v10.4.0 | 2025-11-15 | Web Platform Team | Upgraded to KFM-MDP v10.4; full YAML metadata; clarified ontology & CARE integration               |
| v10.3.2 | 2025-11-14 | Web Platform Team | Deep source architecture clarification for v10.3.2                                                 |
| v10.3.1 | 2025-11-13 | Web Platform Team | Initial source architecture outline for `web/src`                                                  |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License
Validated under Master Coder Protocol (MCP-DL v6.3) and KFM-MDP v10.4.1
FAIR+CARE Certified · Public Document · Version-Pinned

</div>
