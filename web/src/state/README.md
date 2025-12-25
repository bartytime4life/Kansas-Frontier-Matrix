---
title: "KFM web/src/state — State Layer (README)"
path: "web/src/state/README.md"
version: "v1.0.0"
last_updated: "2025-12-25"
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

doc_uuid: "urn:kfm:doc:web:state:readme:v1.0.0"
semantic_document_id: "kfm-web-state-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:state:readme:v1.0.0"
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

# KFM web/src/state — State Layer

## 📘 Overview

### Purpose

- Define the **frontend state conventions** for KFM’s web UI (React SPA under `web/`).
- Keep **map**, **timeline**, and **Focus Mode** panels in sync using a **predictable state container** (e.g., Redux or React Context/Reducers — exact library **not confirmed in repo**).
- Enforce KFM invariants at the UI boundary:
  - **no UI direct-to-graph reads** (UI only calls contracted APIs),
  - **provenance-first UX** (citations + evidence identifiers are first-class),
  - **sensitivity-aware rendering** (respect redaction/generalization and “sensitive layer” flags).

### Scope

| In Scope | Out of Scope |
|---|---|
| Cross-component application state (Focus Mode, layer toggles, selected entities, timeline window, UI prefs) | Backend query logic, Neo4j/Cypher, graph ingestion |
| Async request orchestration and request-status tracking (loading/error/refresh) | Defining/altering API contracts (see `src/server/contracts/` — not confirmed in repo) |
| “Serializable state only” rules (no map engine instances in store) | Styling/theming (CSS) and component layout details |
| Patterns for consuming Story Node metadata (focus_center/time/layers) | Authoring Story Nodes themselves (see `docs/reports/story_nodes/` — not confirmed in repo) |

### Audience

- **Primary:** Frontend contributors working under `web/`.
- **Secondary:** API contract contributors (to understand UI expectations), Story/Focus Mode authors (to understand how UI consumes focus hints).

### Definitions

- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc:
  - **State container**: A predictable global store for cross-component state.
  - **Slice**: A cohesive, namespaced subset of state and its reducers/actions.
  - **Selector**: A pure function that derives view-ready data from state.
  - **Effect / thunk**: Async orchestration that calls APIs and dispatches actions.
  - **Layer registry**: JSON configuration describing map layers (including sensitivity flags).
  - **Focus Mode**: UI state for deep, provenance-linked exploration of an entity/story.
  - **Provenance panel**: UI surface that maps narrative claims to dataset/evidence IDs.
  - **Redaction/generalization**: Policy-driven omission or coarsening of sensitive fields.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical ordering + minimum gates *(not confirmed in repo)* |
| Universal governed doc structure | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | This README follows the Universal template shape *(not confirmed in repo)* |
| v13 architecture alignment | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | KFM Core | “No UI direct-to-graph reads”; one canonical home per subsystem *(not confirmed in repo)* |
| Story Node schema + focus hints | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative | Defines optional `focus_center`, `focus_time`, `focus_layers` *(not confirmed in repo)* |
| API contract extensions | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API owners | Contracts define what Focus Mode can request/receive *(not confirmed in repo)* |
| Layer registry config | `web/**/layers/*.json` | Frontend | Registry entries include “sensitive” flag *(path not confirmed in repo)* |
| UI schemas | `schemas/ui/` | Data/Platform | Used for registry/schema validation *(not confirmed in repo)* |

### Definition of done

- [ ] Front-matter complete and `path` matches `web/src/state/README.md`
- [ ] State responsibilities and boundaries are explicit (what belongs in global state vs local component state)
- [ ] “No UI direct-to-graph reads” is explicit and enforced by design
- [ ] Focus Mode state flow is documented (enter → fetch context bundle → render → exit)
- [ ] Layer registry + sensitivity handling is documented
- [ ] Examples are either repo-accurate or explicitly marked **not confirmed in repo**
- [ ] Governance, CARE/sovereignty considerations, and AI opt-in constraints are stated

---

## 🗂️ Directory Layout

### This document

- `path`: `web/src/state/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Frontend root | `web/` | React SPA + map/timeline + Focus Mode UI |
| State layer | `web/src/state/` | Global state container, slices, selectors, effects |
| UI components | `web/src/components/` | React components (map, story panel, timeline, etc.) *(not confirmed in repo)* |
| API clients | `web/src/api/` | Typed fetch clients / adapters calling `src/server` endpoints *(not confirmed in repo)* |
| Layer registry | `web/**/layers/*.json` | Layer configuration (incl. sensitivity) *(not confirmed in repo)* |
| API boundary | `src/server/` | Contracted REST/GraphQL API layer (no UI direct graph access) *(not confirmed in repo)* |
| API contracts | `src/server/contracts/` | OpenAPI/GraphQL schemas; contract tests *(not confirmed in repo)* |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published narrative content used in Focus Mode *(not confirmed in repo)* |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/story/UI/telemetry) *(not confirmed in repo)* |

### Expected file tree for this sub-area

> This is the **recommended** structure. Some files/dirs may not exist yet (**not confirmed in repo**).

~~~text
📁 web/
└── 📁 src/
    ├── 📁 state/
    │   ├── 📄 README.md                 # this file
    │   ├── 📄 store.ts                  # store setup (not confirmed in repo)
    │   ├── 📄 types.ts                  # shared state types (not confirmed in repo)
    │   ├── 📁 slices/                   # feature slices (recommended)
    │   │   ├── 📄 focus.slice.ts        # Focus Mode state + context bundle refs (not confirmed in repo)
    │   │   ├── 📄 map.slice.ts          # viewport + active layers + selection (not confirmed in repo)
    │   │   ├── 📄 timeline.slice.ts     # time window + playback (not confirmed in repo)
    │   │   ├── 📄 registry.slice.ts     # layer registry + sensitivity flags (not confirmed in repo)
    │   │   ├── 📄 data.slice.ts         # normalized cache + request status (not confirmed in repo)
    │   │   └── 📄 ui.slice.ts           # preferences (theme, reduced motion, panels) (not confirmed in repo)
    │   ├── 📁 selectors/                # pure derived state (recommended)
    │   ├── 📁 effects/                  # async orchestration / thunks (recommended)
    │   ├── 📁 middleware/               # request dedupe, logging, etc. (optional; not confirmed in repo)
    │   └── 📁 __tests__/                # reducer + selector tests (recommended)
    ├── 📁 api/                          # HTTP clients / adapters (not confirmed in repo)
    └── 📁 components/                   # React components (not confirmed in repo)
~~~

---

## 🧭 Context

### Background

KFM’s frontend is a map-and-story-driven UI. The state layer exists to:

- coordinate **map/timeline/story panels** so they are consistent,
- orchestrate **Focus Mode** requests and rendering,
- enforce boundary rules:
  - **UI never queries Neo4j directly**,
  - UI uses contracted APIs and renders provenance-linked narratives.

### Constraints and invariants

Non-negotiables that the state layer must make easy (and hard to violate):

1. **No UI direct-to-graph reads**
   - `web/` must never query Neo4j directly; all graph access is via `src/server/` APIs.

2. **Serializable, deterministic state**
   - Store only JSON-serializable values; treat the state as a deterministic function of actions.
   - Never put MapLibre/Cesium instances, DOM nodes, or class instances in global state.

3. **Layer registry is configuration-driven**
   - Layer toggles should be driven by a registry JSON (including **sensitive** flags).

4. **2D/3D mode switching must not lose conceptual state**
   - Switching MapLibre (2D) ↔ Cesium (3D) should preserve:
     - active conceptual layers,
     - focused entity/story,
     - timeline window.

5. **Focus Mode is provenance-linked**
   - Focus Mode renders story text and shows evidence/citations via a provenance panel.
   - AI narrative is **opt-in** and must be explicitly labeled and separable.

### Practical “what goes where” rule of thumb

- Put it in **global state** when:
  - multiple components need it (map + timeline + story panel),
  - it must survive route/page transitions,
  - it needs URL-deep-linking (recommended),
  - it affects governance/sensitivity (e.g., whether sensitive layers are visible).

- Keep it **component-local** when:
  - it is purely visual and isolated (hover state, local input draft),
  - it does not need to persist,
  - it has no governance impact.

---

## 🗺️ Diagrams

### UI state dataflow

~~~mermaid
flowchart LR
  U[User actions] -->|dispatch| S[State container<br/>web/src/state]
  S -->|effects/thunks| C[API clients<br/>web/src/api]
  C -->|HTTP| A[API boundary<br/>src/server]
  A -->|queries| G[Graph<br/>Neo4j via src/graph]
  A -->|contracted payloads + provenance refs| C
  C -->|normalized data| S
  S -->|selectors| R[React views<br/>map · timeline · story]
~~~

### Focus Mode sequence

~~~mermaid
sequenceDiagram
  participant User
  participant UI as UI (web/)
  participant Store as State (web/src/state)
  participant API as API (src/server)

  User->>UI: Click entity / story link
  UI->>Store: dispatch enterFocus(entityId)
  Store->>API: GET /focus/{entityId} (includeAI? false by default)
  API-->>Store: context bundle + sources/citations + sensitivity flags
  Store-->>UI: state update (focus + map + timeline)
  UI-->>User: Story panel + provenance panel + highlighted map context
~~~

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- **What becomes focusable?**
  - Entities that have stable identifiers returned by APIs (entity IDs) and/or Story Nodes.
- **What evidence must be shown?**
  - Every claim should map to a dataset/record/asset identifier that can be inspected in the provenance panel.

### Provenance-linked narrative rule

- Every factual claim presented in Focus Mode must trace to a dataset / record / asset identifier.
- UI state should preserve:
  - the selected focus target,
  - the evidence/source list (or references to it),
  - any redaction/sensitivity flags needed for correct rendering.

### Optional structured controls from Story Nodes

Story Nodes may include structured hints used by the UI:

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

State-layer guidance:

- Store these hints in Focus Mode state when present.
- Apply them by dispatching updates to:
  - map state (viewport center/zoom + layer toggles),
  - timeline state (time window, highlight interval).

### Recommended “enter focus” pattern

1. **Set focus target immediately** (fast UI response)
2. **Fetch context bundle** (async)
3. **Normalize & store payload** (entities, sources, flags)
4. **Apply view hints** (center/time/layers)
5. **Render narrative + citations + provenance panel**
6. **Exit Focus Mode restores prior state** (breadcrumbs/back)

---

## 🧪 Validation & CI/CD

### Validation steps

- [ ] State is serializable (no MapLibre/Cesium instances in store)
- [ ] Reducers/selectors are deterministic (pure functions)
- [ ] Request/effect layer handles races (request IDs, cancel/ignore stale responses)
- [ ] Layer registry consumption validates sensitivity flags
- [ ] Focus Mode requires provenance references when rendering narrative
- [ ] “include AI” behavior is explicit, off by default, and clearly labeled when enabled
- [ ] UI a11y checks for Focus Mode panels and map controls (recommended)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) run unit tests for reducers/selectors
# 2) run typecheck / lint
# 3) run UI schema validation for layer registry (if present)
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| UI request errors | Web app | telemetry sink defined by UI *(not confirmed in repo)* |
| Focus Mode usage events | Web app | telemetry sink *(not confirmed in repo)* |
| Sensitive layer access attempts | Web app + API | API logs + governance review trail *(not confirmed in repo)* |

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Layer registry | JSON | `web/**/layers/*.json` *(not confirmed in repo)* | UI schema checks *(not confirmed in repo)* |
| Focus Mode context bundle | JSON | `src/server` Focus API | Contract tests *(not confirmed in repo)* |
| Story Node content | Markdown + structured hints | Story Node store (docs/graph) | Story schema validation *(not confirmed in repo)* |
| Provenance refs | IDs/arrays | Focus API payload (`sources`, dataset IDs, etc.) | “no orphan refs” checks (recommended) |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| UI view state | in-memory | state container | serialization discipline (this doc) |
| User preferences | JSON | local storage/session *(not confirmed in repo)* | do not persist sensitive data |
| Deep links | URL params | router *(not confirmed in repo)* | stable IDs only |

### Sensitivity & redaction

- Treat sensitivity flags as **authoritative**:
  - do not “reconstruct” precise locations from generalized fields,
  - do not persist restricted fields to local storage.
- If an API response marks fields as restricted/generalized, the state layer must carry those flags through to rendering.

### Quality signals

- State updates are traceable (action naming conventions).
- Normalized caches use stable IDs.
- No orphan references: narrative citations resolve to source entries in the same context bundle.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- UI should treat STAC item identifiers as first-class for:
  - linking map overlays to catalog items,
  - powering “source details” views in the provenance panel.

### DCAT

- UI may display dataset-level metadata (publisher, license, description) using DCAT dataset IDs.

### PROV-O

- UI should surface provenance relationships (derived-from, generated-by, activity/agent IDs) when available via APIs.

### Versioning

- If payloads include version links (e.g., predecessor/successor), state should store them so the UI can show “this narrative/data changed” affordances.

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| State container | Global app state + serialization discipline | `dispatch`, `getState`, selectors |
| Slices | Cohesive domain state (focus/map/timeline/ui/data) | actions + reducers |
| Selectors | Derived view-ready data | pure functions |
| Effects/thunks | Async orchestration (fetch, dedupe, retry) | calls API clients |
| API clients | Typed network calls to `src/server` | `fetch` wrappers (not confirmed in repo) |
| Map renderer | MapLibre/Cesium instances (NOT in state) | driven by state via props/hooks |
| Story renderer | Markdown → UI, citations clickable | uses state for sources/provenance |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| API contracts | `src/server/contracts/` *(not confirmed in repo)* | contract tests required |
| UI registry schema | `schemas/ui/` *(not confirmed in repo)* | schema validation gate |
| Story Node schema | `schemas/story_nodes/` *(not confirmed in repo)* | validate before publish |

### Extension points checklist

- [ ] Add a new slice for new UX surface (keep it serializable)
- [ ] Add a new effect for a new API call (request IDs + dedupe)
- [ ] Add a new selector for derived view state (pure + tested)
- [ ] Add a new layer registry entry and ensure sensitivity flags are handled
- [ ] Ensure Focus Mode provenance rule remains intact (citations resolvable)

---

## ⚖ FAIR+CARE & Governance

### Review gates

Changes to state design should require governance review if they:

- introduce storage/persistence of any sensitive fields,
- add new UI affordances that could reveal restricted locations through interaction/zoom,
- add AI-generated narrative into Focus Mode without an explicit opt-in and labeling path,
- weaken provenance traceability between narrative claims and evidence identifiers.

### CARE and sovereignty considerations

- Identify communities impacted by new narrative render paths or layer toggles.
- Preserve redaction/generalization rules end-to-end: API → state → UI.

### AI usage constraints

- Permitted: summarize/structure/translate/index this document.
- Prohibited: generating new policy text or inferring sensitive locations.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-25 | Initial state layer README (conventions + boundaries + Focus Mode integration) | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
