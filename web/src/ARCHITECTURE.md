---
title: "💻 Kansas Frontier Matrix — Web Source Architecture Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/ARCHITECTURE.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly / Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-src-architecture-v3.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
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
doc_uuid: "urn:kfm:doc:web-src-architecture-v10.4.0"
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
Define the *complete source-level technical architecture* for `web/src/**` in the Kansas Frontier Matrix (KFM) Web Platform — including UI composition, state management, Focus Mode v2.5 flows, 2D/3D rendering pipelines, accessibility architecture, FAIR+CARE enforcement, provenance visibility, typed DTO boundaries, STAC/DCAT integration, and telemetry & sustainability instrumentation. This document governs **all contributors** modifying `web/src/`.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../docs/README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-UI_Certified-orange)](../../docs/standards/faircare.md)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../LICENSE)  
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)]()  
[![A11y](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-blueviolet)]()

</div>

---

# 📘 Overview

The `web/src/` directory contains **all frontend source code** that powers the KFM Web Platform UI:

- React 18 + TypeScript (strict mode)  
- Tailwind-based design system & A11y tokens  
- **MapLibre GL** for 2D cartography and STAC-driven layers  
- **CesiumJS** for 3D terrain, paleogeography, and future overlays  
- **Focus Mode v2.5** entity reasoning flows (narrative, explainability, CARE gating)  
- **Story Node v3** rendering synced to map and timeline  
- STAC/DCAT dataset explorers and layer controls  
- Governance UI (CARE labels, sovereignty, licenses, provenance trails)  
- Accessibility (WCAG 2.1 AA) as a **hard requirement**  
- Telemetry & sustainability instrumentation (WebVitals, ethics, A11y events)  

The architecture ensures that changes in `web/src/**` are:

- Deterministic and type-safe  
- Ethically governed and CARE-aware  
- Accessible and observable  
- Compatible with KFM’s global architecture (`src/ARCHITECTURE.md`)

---

# 🎯 Purpose

This specification:

- Defines the **source-layer architecture** for `web/src/**`.  
- Establishes boundaries and responsibilities for components, hooks, context, services, and pipelines.  
- Ensures the source code implements:
  - Focus Mode v2.5 requirements  
  - Story Node v3 rendering rules  
  - STAC/DCAT integration contracts  
  - A11y & FAIR+CARE governance overlays  
  - Telemetry and observability contracts  

Primary consumers: web engineers, architects, FAIR+CARE reviewers, SRE/observability teams, and maintainers responsible for `web/src/**`.

---

# 📍 Scope

## In Scope

- All source files under `web/src/**`, including:
  - `components/**`, `context/**`, `features/**`, `hooks/**`, `pages/**`, `pipelines/**`, `services/**`, `styles/**`, `utils/**`, `types/**`.  
- UI-level pipelines (client-only orchestration).  
- Governance and A11y integration at the UI layer.  
- Telemetry emission from the web client.

## Out of Scope

- Backend ETL, AI, and pipeline architecture (covered under `src/pipelines/**`).  
- System deployment and infra specifics (CDN, gateways, etc.).  
- Neo4j schema and backend-only modeling details.

---

# 📚 Definitions

- **Source Architecture:** Organization, responsibilities, and constraints of `web/src/**` modules.  
- **Feature Slice:** A focused vertical domain implementation (e.g., `focus-mode`, `map-layers`).  
- **Context Provider:** Top-level React provider that manages global state (focus, a11y, theme).  
- **Service:** A module under `services/` encapsulating calls to REST/GraphQL/STAC/DCAT endpoints.  
- **Pipeline (frontend):** Client-only orchestration layer combining hooks, services, and state to implement flows (e.g., focusPipeline, stacPipeline).  
- **Story Node v3:** Narrative + spatial + temporal unit rendered by StoryNode components, conforming to the Story Node schema.  
- **Focus Mode v2.5:** Frontend orchestrator that calls backend reasoning endpoints; no heavy AI models run in-browser.

---

# 🏗 Architecture / Context

## Source Architecture in Context

```mermaid
flowchart TD
    UI[UI Components<br/>React · Tailwind] --> CTX[Context Providers]
    UI --> FEAT[Feature Slices]
    UI --> MAP[MapView]
    UI --> TL[TimelineView]
    UI --> FP[FocusPanel]
    UI --> STORY[StoryNode Renderer]
    UI --> GOVUI[Governance & A11y UI]

    FEAT --> HK[Custom Hooks]
    HK --> SVC[Services Layer]
    MAP --> SVC
    TL --> SVC
    FP --> SVC
    STORY --> SVC

    SVC --> API[Backend APIs<br/>REST · GraphQL · STAC · DCAT]
````

The code in `web/src/**` sits between user interactions and backend APIs, enforcing **typing, governance, and accessibility** at the UI boundary.

---

# ⚙️ Procedures / Implementation

Source code implementation follows:

* **Components**: Mostly presentational; read data from hooks/context, emit callbacks.
* **Hooks**: Encapsulate data fetching, state, and side-effects (e.g., `useFocus`, `useStac`).
* **Context**: Provide global state: focus entity, a11y preferences, theme, etc.
* **Pipelines**: Compose hooks and services into end-to-end flows:

  * `focusPipeline.ts`
  * `stacPipeline.ts`
  * `entityPipeline.ts`
  * `timelinePipeline.ts`
  * `layerPipeline.ts`

All changes must respect:

* TypeScript strictness.
* Schema guard validation before rendering.
* Governance and CARE rules.

---

# 📑 Data Contracts & Schemas

Although `web/src/**` does not define primary data schemas, it **consumes**:

* **API DTOs** defined in `types/api.ts`.
* **Domain types** defined in `types/domain.ts`.
* **Story Node JSON schema** via `schemaGuards.ts` and type mapping.
* STAC/DCAT responses converted into typed models via `stacService.ts`/`dcatService.ts`.

Runtime validation is performed by:

* `utils/schemaGuards.ts` — ensures backend responses conform to expectations.
* Failing responses are handled gracefully with error boundaries and governance-safe fallbacks.

---

# 🧬 Ontology Alignment

The source architecture reflects KFM’s ontology alignment:

|     System | Mapping                                                          |
| ---------: | ---------------------------------------------------------------- |
|  CIDOC-CRM | UI interactions considered as `E7 Activity`                      |
|   OWL-Time | Timeline structures as `time:TemporalEntity`                     |
|     PROV-O | Provenance badges and chips representing `prov:Entity` links     |
| schema.org | Source code doc as `SoftwareSourceCode`; app as `WebApplication` |
|  STAC/DCAT | Dataset browsing follows STAC 1.0 and DCAT 3.0 semantics         |

---

# 🛰 STAC/DCAT Metadata

The frontend **does not author** STAC/DCAT; it:

* Uses `stacService.ts` to search and fetch STAC Collections/Items.
* Uses `dcatService.ts` to explore DCAT datasets & distributions.
* Renders dataset metadata, coverage, and assets in components (`LayerControls`, STAC/DCAT explorers).

This architecture ensures all STAC/DCAT interactions are:

* Typed (`types/api.ts`)
* Validated (`schemaGuards.ts`)
* CARE-governed (`useGovernance.ts`)

---

# 📖 Story Node Integration

Story Node v3 support:

* `components/StoryNode/**` renders:

  * Title/summary
  * Temporal extents
  * Geospatial hints (for map sync)
  * Relations and media chips

* `pipelines/storyPipeline.ts` (if present) or `focusPipeline.ts` composes:

  * Story Node DTOs
  * Focus Mode narratives
  * Governance labels

The architecture ensures:

* Story Nodes are validated via schema guards.
* Displayed only when provenance and CARE metadata are present.
* Synced with MapView and TimelineView under Focus Mode and Story Nodes pages.

---

# 🧠 Focus Mode v2.5 Integration

Client-side Focus Mode architecture:

```mermaid
flowchart LR
    U[User selects entity] --> C[FocusController Hook]
    C --> Q["/api/focus/{id}"]
    Q --> R[Narrative & Context]
    R --> N[StoryNode Composer]
    R --> X[Explainability Layer]
    R --> E[Ethics & CARE Guard]
    N --> MV[MapView Highlights]
    N --> TL[TimelineView Highlights]
```

* `hooks/useFocus.ts` manages:

  * Active focus entity
  * Loading state
  * Error, governance, and A11y considerations

* `pipelines/focusPipeline.ts` orchestrates:

  * API calls
  * Narrative + explainability metadata
  * Story Node composition
  * Map/timeline syncing

No AI model runs in-browser; the client is an orchestrator and guardian.

---

# 🔐 Ethics & CARE Requirements

`web/src/**` must:

* Apply CARE labels to data displays (e.g., `Governance` components).
* Use H3 or similar spatial generalization for sensitive sites (config from backend).
* Never reveal exact coordinates for restricted cultural or heritage locations.
* Show consent banners when required by governance policies.
* Avoid speculative or invented narrative behavior in Focus Mode.

---

# 🛡 Governance

The source architecture enforces governance by:

* Rendering license and provenance badges for:

  * STAC/DCAT datasets
  * Story Nodes
  * Focus Mode outputs

* Using `useGovernance.ts` to:

  * Check CARE & license rules before showing data
  * Gate restricted content
  * Emit governance telemetry events

---

# 🧪 Validation & Testing

Required validations:

* TypeScript strict compilation (`npm run typecheck`)
* Linting (`npm run lint`)
* Unit tests for hooks, pipelines, and utilities
* Integration tests for multi-component flows (map+timeline+focus)
* A11y tests (axe-core, Lighthouse)

CI workflows enforce this via:

* `web-build.yml`
* `web-lint.yml`
* `telemetry-export.yml`
* `faircare-validate.yml` (for UI telemetry/governance outputs)

---

# 📈 Telemetry

Source architecture includes:

* `hooks/useTelemetry.ts` for gathering:

  * WebVitals (LCP, FID, CLS)
  * Map and 3D interactions
  * Focus Mode activations
  * Story Node interactions
  * A11y feature usage

* `services/telemetryService.ts` for:

  * Sending telemetry in a non-PII, aggregated format
  * Validating payloads against `telemetry_schema`

Telemetry is merged into global `focus-telemetry.json` artifact.

---

# 🎧 Accessibility (WCAG 2.1 AA)

Plain-language summary:

> This architecture organizes the source code of the KFM web app so that it can show maps, timelines, and stories in ways that everyone can use, including people who rely on keyboard navigation, screen readers, or high-contrast display modes.

Architecture requirements:

* All interactive components must support keyboard navigation.
* A11y tokens must be applied consistently (color, spacing, text size).
* ARIA attributes must describe roles, regions, and relationships.
* Reduced-motion and high-contrast preferences must be honored across all components.

---

# 🤖 Machine Extractability

This document is designed to be machine-parsable:

* Complete YAML front-matter according to `web-src-architecture.schema.json`.
* Predictable heading structure and section ordering.
* Valid mermaid diagrams (with labels properly quoted when needed).
* Structured tables for tool consumption.
* Fenced blocks with explicit language tags.

---

# 🛡 Privacy & Security

`web/src/**` must:

* Avoid logging PII or sensitive information.
* Not embed secrets or privileged tokens in client bundles.
* Respect security headers configured at the deployment layer.
* Apply safe defaults in API clients (e.g., not leaking internal IDs unnecessarily).

Security failures should be handled by separate security docs in `docs/security/**`, but the source architecture must not contradict them.

---

# ♻️ Dataset Evolution / Deltas

Relative to `v10.3.2`:

* Upgraded to full KFM-MDP v10.4 YAML and section structure.
* Added ontology alignment and AI transform controls.
* Clarified Focus Mode v2.5 and Story Node v3 integration paths.
* Documented error taxonomy for source-level concerns.
* Explicitly wired A11y, governance, and telemetry into architecture.

Future versions may:

* Introduce additional feature slices (e.g., “3D deep-time explorer” feature).
* Extend pipelines for real-time collaboration or annotation flows.

---

# 🧩 Error Taxonomy

Source-level errors include:

* **RenderingError** — UI fails to render a component or state.
* **DataLoadError** — services fail to fetch/parse backend responses.
* **GovernanceError** — missing/inconsistent CARE or license labels.
* **A11yError** — failure to meet accessibility requirements.
* **TelemetryError** — invalid or missing telemetry events.
* **FocusError** — Focus Mode orchestration failures (e.g., missing narrative sections).

Error handling must preserve user trust, avoid leaking sensitive info, and log anonymized telemetry events.

---

# 📁 Directory Layout

```text
web/src/
├── ARCHITECTURE.md
├── README.md
├── components/
├── context/
├── entities/
├── features/
├── hooks/
├── pages/
├── pipelines/
├── services/
├── styles/
├── utils/
└── types/
```

---

# 🕰 Version History

| Version | Date       | Author / Team     | Summary                                                                                            |
| ------: | ---------- | ----------------- | -------------------------------------------------------------------------------------------------- |
| v10.4.0 | 2025-11-15 | Web Platform Team | Upgraded to strict KFM-MDP v10.4; added full YAML metadata, error taxonomy, ontology & CARE hooks. |
| v10.3.2 | 2025-11-14 | Web Platform Team | Deep source architecture clarification for v10.3.2.                                                |
| v10.3.1 | 2025-11-13 | Web Platform Team | Initial source architecture outline for web/src.                                                   |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT License**
Validated under **Master Coder Protocol v6.3**
FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified
[Back to Web Source README](README.md) · [Root Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
