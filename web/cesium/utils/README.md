---
title: "KFM Web — Cesium Utils (README)"
path: "web/cesium/utils/README.md"
version: "v1.0.0"
last_updated: "2025-12-21"
status: "draft"
doc_kind: "README"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:web:cesium:utils:readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-utils-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:utils:readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# KFM Web — Cesium Utils (README)

## 📘 Overview

### Purpose
- Define what belongs in `web/cesium/utils/`, how utilities in this folder should be structured, and the invariants they must respect.
- Reduce duplication across Cesium-facing UI code by centralizing shared, low-level behaviors (e.g., coordinate conversions, camera helpers, entity lifecycle helpers) in a **framework-agnostic** way.

### Scope
| In Scope | Out of Scope |
|---|---|
| Cesium-specific helper functions (math, camera, picking, coordinate transforms, entity helpers, performance-safe wrappers) | React components/hooks (belongs in `web/cesium/components/`) |
| Utilities with explicit, testable side-effects on a provided Cesium Viewer/Scene | Network calls / API clients (belongs in API layer clients; utilities should accept already-fetched data) |
| Conventions for units, determinism, and safe handling of “possibly sensitive” coordinates | Data ingestion, STAC/DCAT/PROV generation, graph queries |

### Audience
- Primary: Frontend engineers working on the Cesium 3D experience and 2D/3D interoperability.
- Secondary: Reviewers validating governance constraints, test coverage, and Focus Mode UX integrity.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Cesium Viewer/Scene**: CesiumJS runtime objects for 3D map rendering and interaction.
  - **Layer registry**: Schema-validated UI configuration describing layers and access rules.
  - **Focus Mode**: A UI state that “deep-dives” into a single story/entity, with provenance-first constraints.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `web/cesium/utils/README.md` | Web/UI | Conventions + invariants for this folder |
| Cesium UI components | `web/cesium/components/` | Web/UI | Viewer + UI elements that call these utils |
| Component-level utils | `web/cesium/components/utils/` | Web/UI | React-specific helpers/hooks; keep UI state logic out of `web/cesium/utils/` |
| Layer registry (config) | `web/cesium/layers/` | Web/UI | JSON registry for layers; schema-validated in CI |
| Canonical pipeline + UI constraints | `docs/MASTER_GUIDE_v12.md` | Platform | Non-negotiable ordering + “no hidden leakage” rules |
| Story Node controls (focus hints) | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Platform | Shows optional `focus_center`, `focus_time`, `focus_layers` |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Folder purpose + boundaries are explicit (what goes here vs elsewhere)
- [ ] Units + determinism conventions documented
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `web/cesium/utils/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Frontend root | `web/` | React + map clients |
| Cesium integration | `web/cesium/` | Cesium viewer wiring, layers, helpers |
| This folder | `web/cesium/utils/` | Cesium-focused, framework-agnostic utility modules |
| React-level Cesium utils | `web/cesium/components/utils/` | React-specific helpers/hooks for Cesium components |
| Layer registry | `web/cesium/layers/` | JSON config for layers, access rules, and UI behavior |
| Canonical docs | `docs/` | Governed system docs + templates |
| Schemas | `schemas/` | JSON schemas (incl. UI layer registry schemas, if present) |

### Expected file tree for this sub-area
~~~text
📁 web/
└── 📁 cesium/
    ├── 📁 components/
    │   ├── 📁 utils/
    │   │   └── 📄 README.md
    │   └── 📄 <viewer-components>.<ts|tsx|js|jsx>
    ├── 📁 layers/
    │   └── 📄 <layer-registry>.json
    └── 📁 utils/
        ├── 📄 README.md
        └── 📄 <utility-modules>.<ts|js>
~~~

## 🧭 Context

### Background
KFM’s UI may support switching between 2D and 3D map contexts (e.g., MapLibre ↔ Cesium) without losing conceptual state (active layers, focus context). Utilities in this folder exist to keep Cesium behaviors consistent and testable, so the UI can preserve state transitions and Focus Mode interactions without duplicating Cesium-specific logic.

### Assumptions
- The Cesium Viewer/Scene lifecycle is owned by higher-level UI components; utilities **receive** a viewer/scene reference and do not own global initialization.
- Layer activation is configuration-driven (via a layer registry) rather than hard-coded.
- Focus Mode may provide structured “focus hints” (center/time/layers) from Story Nodes or API-delivered context bundles.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode ordering is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Utilities must not “reconstruct” or infer restricted/sensitive locations from generalized data.
- Utilities must not introduce hidden data leakage (e.g., exposing raw coordinates if upstream redaction/generalization has occurred).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we standardize coordinate types (degrees vs radians vs meters) at the utility boundary? | TBD | TBD |
| Do we enforce a “pure by default” rule, and isolate side-effects to a small `effects/` subset? | TBD | TBD |
| How are provenance IDs preserved and surfaced (e.g., tooltips/audit panel) for 3D entities? | TBD | TBD |

### Future extensions
- Establish a minimal “Cesium value objects” convention (e.g., `LonLatDeg`, `Cartesian3`, `JulianDate`) to prevent unit confusion.
- Add performance guidelines for per-frame code paths (avoid allocations, reuse scratch objects where safe).
- Add a small set of “Focus helpers” that apply `focus_center`, `focus_time`, and `focus_layers` consistently.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  UI[React/Cesium Components] --> U[web/cesium/utils/*]
  U --> C[CesiumJS API]

  UI --> API[API client layer]
  API --> UI

  subgraph Governance
    G[CARE/Sovereignty Rules]
  end

  UI -.enforces.-> G
  U -.must respect.-> G
~~~

### Optional: sequence diagram (Focus Mode → map adjustments)
~~~mermaid
sequenceDiagram
  participant User
  participant UI as UI (FocusMode + Map)
  participant API as API Layer
  participant Utils as Cesium Utils
  participant Cesium as Cesium Viewer/Scene

  User->>UI: Select entity/story
  UI->>API: Fetch Focus context bundle (by entity_id)
  API-->>UI: Context + provenance refs + focus hints
  UI->>Utils: Apply focus hints (center/time/layers)
  Utils->>Cesium: Set camera / toggle entities
  UI-->>User: Narrative + map view updated
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Viewer/Scene reference | runtime object | Provided by Cesium UI components | Non-null guard + lifecycle-safe checks |
| Focus hints | object | Story Node metadata or API context bundle | Schema/shape validation at API/UI boundary |
| Layer config | JSON | `web/cesium/layers/*.json` | Schema-validated in CI (where present) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Camera options / computed extents | object | returned from utils | Internal utility contract (documented here) |
| Cesium entities/primitives | runtime object(s) | created/updated by caller or effect helpers | Must retain provenance metadata in UI-facing state |
| Derived coordinates | numbers/tuples | returned from utils | Unit conventions documented (degrees/radians/meters) |

### Sensitivity & redaction
- Utilities must treat coordinates/locations as potentially sensitive.
- If upstream systems generalize/redact location precision, utilities must not attempt to reverse or “improve precision” through inference.

### Quality signals
- Clear unit naming (e.g., suffixes like `Deg`, `Rad`, `Meters`).
- Deterministic outputs for deterministic inputs (avoid hidden time/global state dependencies).
- Errors are explicit and recoverable (return `null`/`Result` patterns as appropriate; avoid swallowing exceptions silently).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Utilities do not generate STAC.
- If a utility is passed STAC-linked identifiers (e.g., item IDs or asset IDs), it must preserve those IDs in any UI metadata attached to Cesium entities (to support audit/provenance panels).

### DCAT
- Utilities do not publish DCAT.
- Dataset identifiers passed down from API responses should remain intact when used for UI labeling/audit.

### PROV-O
- Utilities should not “invent” provenance.
- If passed `prov:wasDerivedFrom` / `prov:wasGeneratedBy` references, do not drop them when transforming UI state.

### Versioning
- When utility behavior changes materially (e.g., coordinate conventions or camera behavior), bump `version` and summarize in Version History.
- Prefer additive changes; if breaking changes are needed, coordinate with UI consumers and update tests.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Cesium UI components | Own viewer lifecycle + render | Calls into utils with viewer/scene refs |
| Cesium utils (this folder) | Shared Cesium behaviors | Pure helpers + explicit side-effect helpers |
| Layer registry | Declarative layer behaviors | JSON config (schema validated) |
| API layer (client) | Fetch contracted data + provenance | REST/GraphQL clients; no direct graph access |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Utility contracts (implicit) | `web/cesium/utils/*` | Keep stable names/units; version + changelog in this README |
| UI layer registry | `web/cesium/layers/*.json` | Schema-validated; breaking changes require migration |
| Focus hints shape | API response + Story Node metadata | Must remain compatible with Focus Mode expectations |

### Extension points checklist (for future work)
- [ ] UI: add layer registry entry + access rules
- [ ] Focus Mode: focus hints mapping (center/time/layers) is consistent across 2D/3D
- [ ] Telemetry: optional signals for “focus applied”, “camera moved”, etc., with schema updates if recorded
- [ ] Governance: new sensitive layers trigger review gates

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Utilities may be used to:
  - apply `focus_center` (camera movement)
  - apply `focus_time` (timeline sync)
  - apply `focus_layers` (turn on/off configured layers for a story)

### Provenance-linked narrative rule
- Any UI behavior that changes what is shown must preserve provenance visibility: users should be able to trace what they’re seeing back to source IDs.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (if enforced for `web/**` docs in CI)
- [ ] UI unit tests for critical Cesium utility behavior (math/coords determinism)
- [ ] Integration tests for Focus Mode map adjustments (2D/3D parity where applicable)
- [ ] UI schema checks (layer registry), if layer configs are changed
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run UI unit tests
# 2) run UI integration/e2e tests
# 3) run doc lint / markdown validation (if configured)
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| focus_applied | UI/FocusMode | `docs/telemetry/` + `schemas/telemetry/` |
| camera_transition | Cesium viewer events | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes that enable new public-facing layers or expose new location precision may require governance review.
- Changes that alter Focus Mode evidence/provenance behavior should be reviewed for “no hidden leakage”.

### CARE / sovereignty considerations
- If any utility could increase sensitivity (e.g., converting generalized areas to point markers), treat as a governance trigger and document the mitigation.

### AI usage constraints
- Ensure doc’s AI permissions/prohibitions match intended use.
- Utilities must not imply or implement prohibited AI actions like inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial README for `web/cesium/utils/` | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

