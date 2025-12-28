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

- Define **frontend state conventions** for the KFM web app (React SPA under `web/`).
- Keep **map**, **timeline**, and **Focus Mode** panels in sync using a **predictable state container**
  (e.g., Redux or React Context/Reducers — exact library **not confirmed in repo**).
- Make KFM’s UI boundary rules easy to follow (and hard to violate):
  - **UI reads only from contracted APIs** (no direct reads from Neo4j or internal stores).
  - **Focus Mode consumes provenance-linked context bundles only** (no unsourced narrative).
  - **Sensitivity/redaction flags are authoritative** and must be preserved end-to-end (API → state → render).

### Scope

| In Scope | Out of Scope |
|---|---|
| Cross-component application state (Focus Mode, layer toggles, selected entities, timeline window, UI prefs) | Backend query logic, Neo4j/Cypher, graph ingestion |
| Async request orchestration and request-status tracking (loading/error/refresh) | Defining/altering API contracts (see API contract template + `src/server/contracts/**` if present) |
| “Serializable state only” rules (no map engine instances in store) | Styling/theming and component layout details |
| Patterns for consuming Story Node focus hints and evidence pointers | Authoring Story Nodes themselves (see `docs/reports/story_nodes/` *(pattern; not confirmed in repo)* ) |
| Deep-linking and restore behavior (recommended) | CI/workflow implementation details (belong in `.github/` / `tools/`) |

### Audience

- **Primary:** Frontend contributors working under `web/`.
- **Secondary:** API contract contributors (to understand UI expectations), Story/Focus authors (to understand how the UI consumes focus hints + evidence).

### Definitions

- Link: `docs/glossary.md` *(not confirmed in repo; recommended)*

Terms used in this doc:

- **State container**: predictable global store for cross-component state.
- **Slice**: cohesive, namespaced subset of state and its reducers/actions.
- **Selector**: pure function that derives view-ready data from state.
- **Effect / thunk**: async orchestration that calls APIs and dispatches actions.
- **Context bundle**: API payload that contains narrative + entities + evidence refs + sensitivity flags for Focus Mode.
- **Layer registry**: configuration describing map layers (including provenance pointers + sensitivity flags).
- **Provenance panel**: UI surface that maps narrative claims to dataset/evidence IDs.
- **Redaction/generalization**: policy-driven omission or coarsening of sensitive fields/geometry.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical ordering + boundary rules |
| Universal governed doc structure | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | This README follows the Universal template |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative | Defines optional focus hints (e.g., `focus_center`, `focus_time`, `focus_layers`) |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API owners | Use for new/changed Focus Mode endpoints |
| v13 redesign blueprint (draft) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | “one canonical home”; contract-first; evidence-first |
| UI schemas | `schemas/ui/` *(not confirmed in repo)* | Data/Platform | JSON schemas for layer registry, UI payload validation |
| Telemetry schemas | `schemas/telemetry/` *(if present)* | Platform | Governance + observability signals |

### Definition of done

- [ ] Front-matter complete and `path` matches `web/src/state/README.md`
- [ ] State responsibilities and boundaries are explicit (global vs local component state)
- [ ] “No UI direct-to-graph reads” is explicit and enforced by design
- [ ] Focus Mode state flow is documented (enter → fetch context bundle → render → exit/restore)
- [ ] Layer registry + sensitivity handling is documented
- [ ] Examples are either repo-accurate or explicitly marked **not confirmed in repo**
- [ ] Governance, CARE/sovereignty considerations, and AI constraints are stated

---

## 🗂️ Directory Layout

### This document

- `path`: `web/src/state/README.md` *(must match front-matter)*

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI | `web/` | React + map client + Focus Mode UX |
| UI state layer | `web/src/state/` | Global state container, slices, selectors, effects |
| UI components | `web/src/components/` *(not confirmed in repo)* | Map panel, timeline, story panel, Focus Mode panels |
| API clients | `web/src/api/` *(not confirmed in repo)* | Typed fetch clients/adapters calling `src/server` endpoints |
| Layer registry | `web/**/layers/**` *(not confirmed in repo)* | Layer configuration (incl. sensitivity + provenance pointers) |
| API boundary | `src/server/` | Contracted API layer (REST/GraphQL); redaction enforcement |
| API contracts | `src/server/contracts/**` *(if present)* | OpenAPI/GraphQL schemas; contract tests |
| Graph | `src/graph/` | Ontology bindings + graph build/migrations |
| Story Nodes | `docs/reports/story_nodes/` *(pattern; not confirmed in repo)* | Draft/published narratives consumed in Focus Mode |
| Schemas | `schemas/` | JSON schemas (STAC/DCAT/PROV/story/ui/telemetry) |
| Tools | `tools/` | Validators, repo lint, QA scripts |

### Expected file tree for this sub-area

> Recommended structure. Some files/dirs may not exist yet (**not confirmed in repo**).

~~~text
📁 web/
└── 📁 src/
    ├── 📁 state/
    │   ├── 📄 README.md                   # this file
    │   ├── 📄 store.ts                    # store setup (not confirmed in repo)
    │   ├── 📄 types.ts                    # shared state types (not confirmed in repo)
    │   ├── 📁 slices/                     # feature slices (recommended)
    │   │   ├── 📄 focus.slice.ts          # Focus Mode state + context bundle refs (not confirmed in repo)
    │   │   ├── 📄 map.slice.ts            # viewport + active layers + selection (not confirmed in repo)
    │   │   ├── 📄 timeline.slice.ts       # time window + playback (not confirmed in repo)
    │   │   ├── 📄 registry.slice.ts       # layer registry + sensitivity flags (not confirmed in repo)
    │   │   ├── 📄 data.slice.ts           # normalized cache + request status (not confirmed in repo)
    │   │   └── 📄 ui.slice.ts             # preferences (panels, reduced motion, etc.) (not confirmed in repo)
    │   ├── 📁 selectors/                  # derived view state (recommended)
    │   ├── 📁 effects/                    # async orchestration / thunks (recommended)
    │   ├── 📁 middleware/                 # request dedupe/logging (optional; not confirmed in repo)
    │   └── 📁 __tests__/                  # reducer + selector tests (recommended)
    ├── 📁 api/                            # HTTP clients / adapters (not confirmed in repo)
    └── 📁 components/                     # React components (not confirmed in repo)
~~~

---

## 🧭 Context

### Background

KFM’s UI is map-and-story-driven. The state layer exists to:

- coordinate **map / timeline / narrative** panels so they remain consistent,
- orchestrate **Focus Mode** requests and restore behavior,
- preserve KFM’s governance posture at the UI boundary:
  - the UI only consumes data through **contracted APIs**,
  - Focus Mode is **evidence-linked** (citations + provenance pointers are first-class).

### Assumptions

- The web app is a React SPA living under `web/`.
- The map renderer is **2D MapLibre** and may optionally support a **3D Cesium** mode switch.
  - 3D support is optional and repository implementation details are **not confirmed in repo**.
- A **predictable state container** is used (Redux or Context/Reducers — exact choice **not confirmed in repo**).
- Layer toggles are driven by a **layer registry config** (JSON), rather than hardcoded UI lists (**path not confirmed in repo**).
- Focus Mode data arrives as a **context bundle** from the API boundary (a “Focus API” endpoint — exact route **not confirmed in repo**).

### Constraints / invariants

Non-negotiables that the state layer must support:

1. **Canonical pipeline ordering is preserved**
   - UI exists downstream of catalogs/graph/API and must not bypass them.

2. **No UI direct-to-graph reads**
   - `web/` must never query Neo4j directly; graph access is only via `src/server/` APIs.

3. **Serializable, deterministic state**
   - Store only JSON-serializable values.
   - Never store MapLibre/Cesium instances, DOM nodes, or class instances.

4. **Contract-first consumption**
   - Treat API payload shapes as contracts; state should store raw payloads only in well-defined caches.
   - Avoid “inventing” fields client-side that could conflict with contract evolution.

5. **Layer registry is configuration-driven**
   - Layer toggles, attribution, provenance pointers, and sensitivity flags come from the registry.

6. **2D/3D switching preserves conceptual state**
   - Switching MapLibre ↔ (optional) Cesium must preserve:
     - active conceptual layers,
     - focused entity/story,
     - timeline window.

7. **Focus Mode is provenance-linked**
   - Focus Mode renders story text with **resolvable citations/evidence IDs** in a provenance panel.
   - AI narrative is **opt-in**, clearly labeled, and separable from curated narrative.

8. **Sensitivity propagation**
   - If API payloads mark fields/layers as generalized or restricted, state must carry those flags through to rendering.
   - Do not persist restricted fields to local storage.

### Practical “what goes where” rule of thumb

- Put it in **global state** when:
  - multiple components need it (map + timeline + story panel),
  - it must survive route changes,
  - it needs URL deep-linking (recommended),
  - it affects governance/sensitivity (e.g., whether sensitive layers are visible).

- Keep it **component-local** when:
  - it is purely visual (hover, local input draft),
  - it does not need to persist,
  - it has no governance impact.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which state container library is canonical (Redux Toolkit vs Context/Reducers)? | TBD | TBD |
| What is the canonical deep-link format (query params vs route segments) for Focus Mode + timeline + layers? | TBD | TBD |
| What is the canonical layer registry location + schema versioning rule? | TBD | TBD |
| Should normalized caches be LRU-bounded, and where is eviction configured? | TBD | TBD |
| What fields (if any) are permitted in persisted user prefs (local storage) given sensitivity rules? | TBD | TBD |

### Future extensions

- URL deep-linking for Focus Mode (`entity_id`, `story_id`, `time_range`, `layers`)
- Pluggable caching strategy (request dedupe, stale-while-revalidate, offline read-only)
- “Audit overlay” features (click any visual element → show evidence + PROV lineage)
- Telemetry hooks for governance signals (e.g., redaction notice shown)

---

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### UI state dataflow

~~~mermaid
flowchart LR
  U[User actions] -->|dispatch| S[State container<br/>web/src/state]
  S -->|effects/thunks| C[API clients<br/>web/src/api]
  C -->|HTTP| A[API boundary<br/>src/server]
  A -->|queries| G[Graph<br/>Neo4j via src/graph]
  A -->|contracted payloads + provenance refs| C
  C -->|normalize + cache| S
  S -->|selectors| R[React views<br/>map · timeline · story]
~~~

### Optional: sequence diagram (Focus Mode)

~~~mermaid
sequenceDiagram
  participant User
  participant UI as UI (web/)
  participant Store as State (web/src/state)
  participant API as API (src/server)

  User->>UI: Click entity / story link
  UI->>Store: dispatch enterFocus(entityId)
  Store->>API: GET Focus context bundle (includeAI? false by default)
  API-->>Store: context bundle + citations + sensitivity flags
  Store-->>UI: state update (focus + map + timeline)
  UI-->>User: Story panel + provenance panel + highlighted map context
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Layer registry | JSON | `web/**/layers/**` *(not confirmed in repo)* | `schemas/ui/` *(if present)* |
| Focus Mode context bundle | JSON | `src/server` Focus API | API contract tests *(if present)* |
| Story Node content | Markdown + front-matter | `docs/reports/story_nodes/**` *(pattern; not confirmed in repo)* | Story Node schema *(if present)* |
| Provenance/evidence refs | IDs/arrays | Focus bundle (`sources`, STAC/DCAT/PROV IDs) | “no orphan refs” check (recommended) |
| Deep-link params | URL | router | stable IDs only; no sensitive payloads |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| UI view state | in-memory | state container | serialization discipline (this doc) |
| User preferences | JSON | local storage/session *(not confirmed in repo)* | must not persist restricted fields |
| Deep links | URL | router *(not confirmed in repo)* | stable IDs only |
| UI telemetry events | JSON | telemetry sink *(not confirmed in repo)* | `schemas/telemetry/` *(if present)* |

### Sensitivity & redaction

- Treat sensitivity flags as **authoritative**:
  - do not reconstruct precise locations from generalized fields,
  - do not persist restricted fields to local storage.
- If an API response marks fields as restricted/generalized, the state layer must carry those flags to rendering.
- If a sensitive layer is disabled or generalized, UI should render an explicit “generalized/redacted” affordance.

### Quality signals

- State updates are traceable and namespaced (e.g., `focus/enter`, `timeline/setRange`).
- Normalized caches use stable IDs (entity_id, dataset_id, stac_item_id).
- No orphan references: narrative citations resolve to evidence/source entries present in the same context bundle.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Treat STAC identifiers as first-class for:
  - linking map overlays to catalog items,
  - powering “source details” views in the provenance panel.
- Prefer storing **IDs** and small display metadata in state; fetch full item/asset detail via API as needed.

### DCAT

- Display dataset-level metadata (publisher, license, description) using DCAT dataset IDs when supplied by APIs.

### PROV-O

- Surface lineage relationships when available:
  - `prov:wasDerivedFrom` / `prov:wasGeneratedBy` for evidence transparency,
  - activity/agent IDs when available via Focus bundle or evidence detail endpoints.

### Versioning

- If payloads include version links (predecessor/successor), state should store them so the UI can show:
  - “this narrative/data changed” affordances,
  - pinned “as-of” views for reproducible browsing.

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | ingest + normalize | configs + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validators |
| Graph | Neo4j | graph ingest + query via API boundary |
| APIs | serve contracts + enforce redaction | REST/GraphQL |
| UI | map + narrative + Focus Mode | API clients + state container |
| Story Nodes | curated narrative artifacts | docs + stable IDs + citations |
| Focus Mode | provenance-linked exploration | context bundles + audit affordances |

### State layer components (UI sub-layer)

| Component | Responsibility | Interface |
|---|---|---|
| State container | global app state (serializable) | `dispatch`, `getState`, selectors |
| Slices | cohesive domain state (focus/map/timeline/registry/ui/data) | actions + reducers |
| Selectors | derived view-ready data | pure functions |
| Effects/thunks | async orchestration (fetch, dedupe, retry) | calls API clients |
| API clients | typed calls to `src/server` | `fetch` wrappers *(not confirmed in repo)* |
| Map renderer | MapLibre/Cesium instances (NOT in state) | driven by state via props/hooks |
| Story renderer | Markdown → UI + citations | uses state for sources/provenance |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| API contracts | `src/server/contracts/**` *(if present)* | backwards compatible or version bump |
| UI layer registry schema | `schemas/ui/` *(if present)* | schema version bump + validation gate |
| Story Node schema | `schemas/story_nodes/` *(if present)* | validate before publish |
| Telemetry schema | `schemas/telemetry/` *(if present)* | schema version bump + CI lint |

### State domains (recommended)

> Names are illustrative; align to repo conventions (**not confirmed in repo**).

| Domain | Examples | Notes |
|---|---|---|
| `focus` | active target, breadcrumb stack, context bundle refs | must carry sensitivity flags + evidence refs |
| `map` | viewport, selection, active layer IDs, hover | store conceptual state only |
| `timeline` | time window, playback, highlights | supports Focus Mode hints |
| `registry` | layer registry entries, sensitivity flags | registry is config-driven |
| `data` | normalized entities, sources, request status | stable IDs + request IDs |
| `ui` | panel layout, reduced motion, filters | do not persist restricted data |

### Extension points checklist

- [ ] Add a new slice for a new UX surface (keep it serializable)
- [ ] Add a new effect for a new API call (request IDs + dedupe)
- [ ] Add a new selector for derived view state (pure + tested)
- [ ] Add a new layer registry entry and ensure sensitivity flags are handled
- [ ] Ensure Focus Mode provenance rule remains intact (citations resolvable)

---

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as “machine-ingestible storytelling”

Story Nodes should:

- carry citations to cataloged artifacts (STAC/DCAT/PROV IDs or document IDs),
- reference graph entities (Place/Person/Event/Document/etc.) via stable IDs,
- separate fact vs inference vs hypothesis where applicable (especially for AI-generated text).

### Focus Mode rule (hard gate)

- Focus Mode consumes **provenance-linked** content only.
- Any predictive/suggestive/AI-generated content:
  - is **opt-in**,
  - includes uncertainty metadata (confidence, method),
  - must not infer or reveal sensitive locations.

### Optional structured controls from Story Nodes

Story Nodes may include structured focus hints:

~~~yaml
focus_layers:
  - "TBD_LAYER_ID"
focus_time: "TBD_TIME_RANGE"
focus_center: [-98.0000, 38.0000]
~~~

State-layer guidance:

- Store these hints as part of Focus Mode state when present.
- Apply them by dispatching updates to:
  - map state (viewport + layer toggles),
  - timeline state (time window + highlight interval).

### Recommended “enter focus” pattern

1. Set focus target immediately (fast UI response)
2. Fetch context bundle (async)
3. Normalize and cache payload (entities, sources, flags)
4. Apply view hints (center/time/layers) if provided
5. Render narrative + citations + provenance panel
6. Exit Focus Mode restores prior state (breadcrumbs/back)

### Example state shape (illustrative)

~~~ts
// Example only — align to repo conventions (not confirmed in repo)

type RequestStatus = "idle" | "loading" | "succeeded" | "failed";

type FocusTarget =
  | { kind: "entity"; id: string }
  | { kind: "story"; id: string };

interface FocusState {
  active: boolean;
  target: FocusTarget | null;

  // Context bundle references
  contextRequestId?: string;
  contextStatus: RequestStatus;

  // Evidence and governance
  sourceIds: string[];
  sensitivityFlags: Record<string, boolean>;

  // Optional focus hints (from Story Node / API)
  focusCenter?: [number, number];
  focusTime?: string;
  focusLayers?: string[];
}
~~~

---

## 🧪 Validation & CI/CD

### Validation steps

- [ ] State is serializable (no MapLibre/Cesium instances in store)
- [ ] Reducers/selectors are deterministic (pure functions)
- [ ] Effects handle races (request IDs; cancel/ignore stale responses)
- [ ] Layer registry validates and sensitivity flags are respected in UI
- [ ] Focus Mode requires provenance references when rendering narrative
- [ ] “Include AI” behavior is explicit, off by default, and clearly labeled when enabled
- [ ] A11y checks for Focus Mode panels and map controls (recommended)
- [ ] Tests for critical flows (Focus Mode enter/exit; layer toggles; timeline sync)

### Reproduction

~~~bash
# Placeholders — replace with repo-specific commands

# 1) run unit tests for reducers/selectors
# 2) run typecheck / lint
# 3) validate UI layer registry against schemas (if present)
# 4) run e2e flow for Focus Mode (if present)
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| UI request errors | Web app | telemetry sink *(not confirmed in repo)* |
| Focus Mode opened/closed | Web app | telemetry sink *(not confirmed in repo)* |
| `focus_mode_redaction_notice_shown` | Web app | telemetry sink *(if present)* |
| Sensitive layer access attempts | Web app + API | API logs + governance trail *(not confirmed in repo)* |

---

## ⚖ FAIR+CARE & Governance

### Governance review triggers

Changes to state design should require governance review if they:

- persist any sensitive fields (especially location/geometry) client-side,
- introduce interactions that could reveal restricted locations through zoom/selection,
- add AI narrative into Focus Mode without explicit opt-in + labeling + uncertainty metadata,
- weaken traceability between narrative claims and evidence identifiers.

### CARE / sovereignty considerations

- Identify communities impacted by new narrative paths or layer toggles.
- Preserve redaction/generalization rules end-to-end: API → state → UI.
- Do not “reconstruct” restricted information from generalized data.

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
