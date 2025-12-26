---
title: "Map State — Map UI State Contracts (web/src/map/state)"
path: "web/src/map/state/README.md"
version: "v0.1.0-draft"
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

doc_uuid: "urn:kfm:doc:web:map:state:readme:v0.1.0-draft"
semantic_document_id: "kfm-web-map-state-readme-v0.1.0-draft"
event_source_id: "ledger:kfm:doc:web:map:state:readme:v0.1.0-draft"
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

# web/src/map/state — Map UI State

## 📘 Overview

### Purpose

This folder documents the **state model and conventions** for KFM’s **map UI** (React + MapLibre, with optional Cesium 3D). The goal is to make map behavior **deterministic**, **serializable**, and **contract-aligned** so that the map, timeline, and Focus Mode story panel remain synchronized without leaking sensitive content.

This README is written as a **contract-oriented guide**: it describes what “must be true” about map state (invariants), how it integrates with API + Focus Mode, and what is expected to be test-validated.

### Scope

| In Scope | Out of Scope |
|---|---|
| Canonical **map UI state** shape, slice boundaries, serialization rules, and update patterns | Implementing specific ETL / catalog / graph pipelines |
| Focus Mode state transitions (enter/exit, loading, pivoting) as UI orchestration | Defining or changing API endpoints/contracts (see API contract docs) |
| Layer toggle state driven by a schema-validated **layer registry** | Defining new layer registry schema fields (belongs under `schemas/` + governance) |
| Provenance + redaction signals **as displayed/handled in UI state** | Bypassing API boundary (UI never reads Neo4j directly) |

### Audience

- Primary: UI maintainers implementing map/timeline/Focus Mode synchronization.
- Secondary: API maintainers (contract alignment), governance reviewers (sensitivity leakage risk), story node curators (Focus Mode behavior expectations).

### Definitions (link to glossary)

- Glossary: `../../../../docs/glossary.md` *(not confirmed in repo — adjust link if glossary lives elsewhere)*
- Terms used in this doc:
  - **View state**: map camera position/orientation (center, zoom, bearing, pitch; 3D: camera).
  - **Layer registry**: schema-validated JSON describing map layers (sources, attribution, sensitivity).
  - **Focus Mode**: immersive narrative UI mode; **provenance-linked content only**.
  - **Context bundle**: API response payload for Focus Mode (story + data + citations + audit flags).
  - **Sensitivity / classification**: governance labels affecting what can be shown at what zoom/precision.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master guide | `../../../../docs/MASTER_GUIDE_v12.md` | KFM core maintainers | Canonical pipeline ordering + invariants |
| Redesign blueprint | `../../../../docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture maintainers | Contract-first + provenance-first expectations |
| Story Node template | `../../../../docs/templates/TEMPLATE__STORY_NODE_V3.md` | Story maintainers | Supports `focus_center`, `focus_time`, `focus_layers` metadata |
| API contracts | `../../../../src/server/contracts/**` *(v13 target)* or `../../../../src/api/**` *(if legacy; not confirmed in repo)* | API maintainers | UI consumes graph via API boundary only |
| UI layer registry | `../../../**/layers/**` | UI maintainers | Registry drives layer toggles; must schema-validate |
| UI registry schemas | `../../../../schemas/**` | Schema maintainers | Expected to include UI registry schemas *(exact path not confirmed in repo)* |

### Definition of done (for this sub-area)

- [ ] Map state is **serializable** (can be persisted/replayed) and excludes non-serializable engine instances.
- [ ] Focus Mode transitions are deterministic and **enforce provenance-only rendering** by default.
- [ ] Layer registry consumption is validated (schema + safe defaults) and gated by sensitivity.
- [ ] State changes support map/timeline sync without “ghost” mismatches.
- [ ] No secrets, tokens, PII, or restricted coordinates are stored in UI state.

---

## 🗂️ Directory Layout

### This document

- `path`: `web/src/map/state/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI app root | `web/` | React/Map UI |
| Map UI components | `web/src/map/**` | Map view, timeline wiring, Focus Mode integration |
| Map UI state | `web/src/map/state/**` | Store/slices/selectors/types for map-related state |
| Layer registry | `web/**/layers/**` | JSON layer definitions (source URLs, attribution, sensitivity) |
| API boundary | `src/server/**` *(or legacy `src/api/**`)* | Contracted access to graph + redaction logic |
| Story Nodes | `docs/reports/story_nodes/**` | Governed narrative artifacts rendered in Focus Mode |
| Schemas | `schemas/**` | JSON schemas including UI registries, story nodes, telemetry |

### Expected file tree for this sub-area

> Note: the specific filenames below are **intended canonical structure**. If the repo already contains a different layout, keep this README synchronized with what exists in-repo.

~~~text
📁 web/
└── 📁 src/
    └── 📁 map/
        └── 📁 state/
            ├── 📄 README.md
            ├── 📄 index.ts                (public exports: types, selectors, actions)
            ├── 📄 types.ts                (MapState, ViewState, LayerState, FocusModeState)
            ├── 📄 selectors.ts            (pure selectors; memoized where appropriate)
            ├── 📄 actions.ts              (action creators / intents)
            ├── 📁 slices/                 (if using Redux-style organization)
            │   ├── 📄 view.slice.ts
            │   ├── 📄 layers.slice.ts
            │   ├── 📄 time.slice.ts
            │   ├── 📄 selection.slice.ts
            │   └── 📄 focusMode.slice.ts
            ├── 📁 adapters/               (engine adapters: MapLibre vs Cesium)
            │   ├── 📄 maplibre.adapter.ts
            │   └── 📄 cesium.adapter.ts
            ├── 📁 middleware/             (side effects / async orchestration)
            └── 📁 __tests__/              (unit tests for reducers/selectors)
~~~

---

## 🧭 Context

### Background

KFM’s architecture is intentionally staged to keep the system modular and auditable:

**ETL → STAC/DCAT/PROV catalogs → Graph → APIs → UI → Story Nodes → Focus Mode**

This folder is in the **UI stage**, but it must preserve upstream contracts (catalog IDs, provenance links, redaction rules) and enforce Focus Mode presentation constraints (no uncited content by default).

### Assumptions

- The frontend is a SPA under `web/` using React.
- Map rendering uses **MapLibre GL** for 2D, with optional **Cesium** for 3D.
- A predictable state container exists (Redux or React Context/Reducers) to keep map + story panel in sync.
- A JSON **layer registry** exists under `web/**/layers/**` and is intended to be schema-validated.
- Focus Mode is driven by an API call that returns a **context bundle**.

### Constraints / invariants

- **No UI direct-to-graph reads**. UI consumes graph data only through API contracts.
- **Focus Mode rule (non-negotiable):**
  - Focus Mode must only consume **provenance-linked** content.
  - Any predictive/AI content must be clearly marked, opt-in, and include uncertainty metadata.
- State must be:
  - **Serializable** (persistable to URL/session/local storage if adopted).
  - **Deterministic** (same inputs → same next state).
  - **Minimal** (store references/IDs, not entire map engine objects).
- Sensitivity must be respected:
  - Do not store or cache restricted coordinates or PII in client state.
  - If a layer or feature is redacted/generalized, state must preserve the redaction signal and display a notice.

### Open questions (track; do not guess)

| Question | Owner | Notes |
|---|---|---|
| Which state library is canonical (Redux Toolkit, Zustand, Context+Reducer, etc.)? | TBD | **not confirmed in repo** |
| Is view state persisted to URL (shareable links) or only session memory? | TBD | **not confirmed in repo** |
| What is the canonical layer registry schema + location under `schemas/`? | TBD | **not confirmed in repo** |
| Do we support dual-engine mode (MapLibre 2D ↔ Cesium 3D) in v1? | TBD | **not confirmed in repo** |

### Future extensions

- Shareable Focus Mode URLs: `?entity=...&t=...&layers=...&center=...`
- Offline/edge caching of “context bundles” with governance-safe TTL
- Collaborative cursors / multi-user annotations *(requires security + governance review)*

---

## 🗺️ Diagrams

### Map state within the canonical pipeline

~~~mermaid
flowchart LR
  A[ETL<br/>src/pipelines] --> B[Catalogs<br/>data/stac + data/catalog/dcat + data/prov]
  B --> C[Graph<br/>Neo4j]
  C --> D[API Boundary<br/>src/server]
  D --> E[UI Map Client<br/>web/]
  E --> F[Map State<br/>web/src/map/state]
  F --> G[Map Renderers<br/>MapLibre / Cesium]
  F --> H[Story Nodes + Focus Mode UI]
~~~

### Focus Mode UI state machine (client-side)

~~~mermaid
stateDiagram-v2
  [*] --> Idle

  Idle --> EnteringFocus: focus/enter(entity_id)
  EnteringFocus --> LoadingBundle: api/request(context_bundle)
  LoadingBundle --> FocusActive: api/success(bundle)
  LoadingBundle --> FocusError: api/failure(error)

  FocusActive --> Pivoting: focus/pivot(new_entity_id)
  Pivoting --> LoadingBundle: api/request(context_bundle)

  FocusActive --> ExitingFocus: focus/exit
  FocusError --> ExitingFocus: focus/exit
  ExitingFocus --> Idle
~~~

### Sequence: user clicks entity → Focus Mode context bundle

~~~mermaid
sequenceDiagram
  participant User
  participant UI as UI (Map/Panel)
  participant State as Map State
  participant API as API Boundary

  User->>UI: Click entity on map / link in narrative
  UI->>State: dispatch focus/enter(entity_id)
  State->>API: GET /focus/{entityId} (includeAI=false default)
  API-->>State: context bundle (story + citations + audit flags + map/timeline hints)
  State-->>UI: derived props via selectors
  UI->>UI: render Focus Mode (map zoom + timeline range + story panel)
~~~

---

## 🧱 Architecture

### Design goals

- Keep map state **engine-agnostic**: MapLibre and Cesium should interpret the same conceptual state.
- Keep side effects outside reducers:
  - reducers = “pure state transitions”
  - middleware/hooks/services = “async orchestration / API calls”
- Keep state **reference-based**:
  - store IDs and minimal metadata
  - prefer normalized structures for features and layers

### Recommended slice boundaries

> Slice names are illustrative; align to actual repo code if different.

| Slice | Owns | Must NOT own |
|---|---|---|
| `view` | center, zoom, bearing, pitch; viewport bounds | map engine instances, DOM refs |
| `time` | time window, cursor position, granularity | derived charts/data (keep derived in selectors) |
| `layers` | active layer IDs, opacity, per-layer filters | fetching logic (keep in middleware/services) |
| `selection` | hovered/selected feature refs, multi-select | raw feature geometry blobs if sensitive |
| `focusMode` | mode status, focused entity/story node IDs, bundle refs | rendering components or text formatting |

### Example state shape (illustrative)

~~~ts
type ViewState = {
  center: [number, number]; // [lon, lat]
  zoom: number;
  bearing: number;          // degrees
  pitch: number;            // degrees
  bounds?: [number, number, number, number]; // [w,s,e,n]
  engine: "maplibre-2d" | "cesium-3d";
};

type LayerToggles = {
  active: string[]; // layer_ids from layer registry
  opacity: Record<string, number>;
  filters: Record<string, unknown>; // schema-defined per layer (not confirmed)
};

type FocusModeState = {
  status: "idle" | "entering" | "loading" | "active" | "error" | "exiting";
  entityId?: string;
  storyNodeId?: string;
  contextBundleId?: string;  // reference to cached bundle payload
  includeAI: boolean;        // must be explicit opt-in
  lastError?: { code?: string; message: string };
};

type MapState = {
  view: ViewState;
  time: { start?: string; end?: string; cursor?: string };
  layers: LayerToggles;
  selection: { hovered?: FeatureRef; selected?: FeatureRef };
  focus: FocusModeState;
  governance: {
    // UI-facing signals; should come from API + registry metadata
    redactionNotices: Array<{ layerId: string; reason: string }>;
  };
};

type FeatureRef = { layerId: string; featureId: string };
~~~

### Non-serializable boundary (hard rule)

Do **not** store any of the following in state:
- MapLibre/Cesium engine instances
- DOM elements, class instances, functions
- Unbounded caches of raw geometry or large arrays

Instead:
- keep engine instances in React refs
- store only IDs, view parameters, and minimal flags in state

---

## 🧠 Story Node & Focus Mode Integration

### How Story Nodes influence map state

Story Nodes may optionally include Focus Mode “controls” that the UI uses to set view/time/layers:

- `focus_center`: map center to use on entry (lon/lat)
- `focus_time`: time window to highlight
- `focus_layers`: layer IDs to enable

~~~yaml
# Example (illustrative; see Story Node v3 template)
focus_layers:
  - "treaty_boundaries_1854"
  - "historic_trails"
focus_time: "1854-01-01/1854-12-31"
focus_center: [-98.0000, 38.0000]
~~~

Map state should apply these controls **idempotently**:
- entering Focus Mode should set/merge view + time + layers from the bundle
- pivoting should replace with the new focus controls (unless explicitly pinned by user)

### Focus Mode rule enforcement at the state boundary

- Default `includeAI = false`.
- UI should not render any AI summary/prediction fields unless:
  - `includeAI === true`, and
  - the response includes explicit uncertainty/confidence fields, and
  - the UI visually labels the content as AI-generated.

Recommended pattern:
- treat AI content as a separate slice or separate sub-field so it is easy to hide by default.

### Context bundle mapping (recommended)

The API response should be treated as “data” and map state should store references:
- `contextBundleId` points to a cached bundle record
- selectors derive:
  - narrative model for the story panel
  - map highlight instructions
  - citations/provenance references
  - audit flags and redaction notices

---

## 🧪 Validation & CI/CD

### CI behavior contract

- **Validate if present**: if a canonical root exists (or changes), validate its artifacts.
- **Fail if invalid**: schema errors, missing links, or orphan references fail deterministically.
- **Skip if not applicable**: optional roots absent → skip without failing the overall pipeline.

### Minimum checks (expected)

- [ ] Markdown protocol checks (for governed docs)
- [ ] UI registry checks (layer registry schema validation)
- [ ] Unit tests for reducers/selectors (pure state)
- [ ] Integration tests for Focus Mode entry/pivot/exit orchestration
- [ ] Contract tests for API responses consumed by Focus Mode (owned by API; validated here via fixtures if adopted)
- [ ] Security + sovereignty checks (as applicable)

### Local reproduction (placeholders)

~~~bash
# NOTE: commands are placeholders; replace with repo-approved tooling.

# 1) run UI unit tests
# 2) validate UI registries against schemas
# 3) run lint + typecheck
# 4) run integration tests (if present)

# make test-ui
# make validate-ui-registries
# make lint
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Source | Validation expectation |
|---|---|---|---|
| Layer registry | JSON | `web/**/layers/**` | Schema-validated; includes sensitivity flags |
| Focus Mode context bundle | JSON | API boundary | Must include provenance links + audit flags |
| User interactions | events | UI | Mapped to explicit actions/intents |
| Story Node controls | YAML/MD fields | Story Node v3 | Validated by story node schema |

### Outputs

| Output | Format | Consumer | Notes |
|---|---|---|---|
| Render instructions | derived | MapLibre/Cesium adapters | Derived from state + registry |
| API query params | derived | API client | Derived via selectors; keep deterministic |
| Redaction notices | state | UI panels | Must be visible to user where relevant |

### Sensitivity & redaction

- If a layer is sensitive, the UI must:
  - respect any API redactions/generalization
  - show a notice when a user action would otherwise reveal restricted precision (zoom-based gating)
- State should carry a minimal “redaction notice ledger” (layerId + reason), **not** the restricted data itself.

### Quality signals (recommended)

- As-of timestamps for context bundle and layer registry
- “Data incomplete / under review” badge for draft story nodes
- Audit flags surfaced to the UI

---

## 🌐 STAC, DCAT & PROV Alignment

### What map state must preserve

UI state should preserve (and never rewrite) canonical identifiers coming from upstream:

- STAC IDs (collection/item/asset IDs) for geospatial artifacts
- DCAT dataset/distribution identifiers for discovery/licensing context
- PROV activity/run identifiers for lineage/audit

### Recommended linkage points

- Layer registry entries should include pointers such as:
  - `stac_collection_id` (or item IDs if layer is a single asset)
  - `dcat_dataset_id`
  - `prov_bundle_id` / `prov_activity_id`
  - `license` + `attribution`

> Exact field names and schema are **not confirmed in repo**. If introducing these fields, update the UI registry schema under `schemas/` and add CI validation.

---

## ⚖ FAIR+CARE & Governance

### Review gates (typical)

Governance review is required when:
- adding a new UI layer that could reveal sensitive locations by interaction/zoom,
- changing a layer’s sensitivity/classification,
- introducing new AI-visible narrative behavior in Focus Mode,
- adding new public-facing UI access paths to data that was previously internal.

### CARE / sovereignty considerations

- Treat culturally sensitive locations as high-risk by default.
- Prefer coarse/aggregate public products and document redaction/generalization choices.
- Ensure classification propagation: no output is “less restricted” than any input in its lineage.

### AI usage constraints (for this sub-area)

Allowed:
- summarization, structure extraction, translation, keyword indexing

Prohibited:
- generating new policy
- inferring sensitive locations (directly or indirectly)

---

## 🕰️ Version History

| Version | Date | Summary | Author | PR / Issue |
|---|---:|---|---|---|
| v0.1.0-draft | 2025-12-25 | Initial scaffold for map UI state contracts + Focus Mode integration expectations | TBD | TBD |

---

Footer refs (do not remove):
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
---

