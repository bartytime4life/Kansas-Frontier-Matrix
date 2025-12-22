---
title: "KFM Web — UI State Layer"
path: "web/src/state/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "draft"
doc_kind: "Guide"
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

# KFM Web — UI State Layer

## 📘 Overview

### Purpose

- Provide a single, predictable source of truth for cross-cutting UI state (map layers, timeline, Focus Mode selection, etc.).
- Define invariants so the map, story panel, and search results stay in sync.
- Enforce the KFM UI contract: **API-only consumption** and **provenance-first Focus Mode** (no direct graph access; no uncited narrative by default).

### Scope

| In Scope | Out of Scope |
|---|---|
| State shape + module conventions for `web/src/state/` (actions/events, reducers/slices, selectors, middleware) | ETL, STAC/DCAT/PROV generation, graph ingest/migrations |
| Focus Mode UI state (selected entity/story node, context bundle cache, breadcrumbs/back navigation) | API implementation and contracts (`src/server/`) |
| Map + timeline synchronization state (viewport, layer toggles, time window, filters) | Authoring Story Nodes under `docs/reports/story_nodes/` |
| Provenance references carried through UI state (IDs/citations passed through from the API) | Storing secrets/credentials in any client-side state |

### Audience

- Primary: UI/frontend developers working in `web/` (React/MapLibre/Cesium)
- Secondary: API engineers (contract alignment), QA (Focus Mode regression tests), governance reviewers (sensitivity leakage checks)

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Focus Mode** — a dedicated view that deep-dives into a single story/entity.
  - **Context bundle** — Focus Mode API payload (narrative + citations + audit/provenance + map/timeline hints).
  - **Provenance** — dataset/document identifiers and lineage references (STAC/DCAT/PROV and/or graph lineage) surfaced to the UI.
  - **Layer registry** — schema-validated configuration describing map layers and sensitivity/access flags.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM Core Team | Canonical pipeline + invariants |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs Team | Focus hints (`focus_layers`, `focus_time`, `focus_center`) |
| API contracts | `src/server/` + docs | API Team | Source of truth for UI payload shapes + redaction |
| Layer registry | `web/**/layers/**/*.json` | UI Team | Must be schema-validated |
| System/UI architecture docs | `docs/architecture/` | Architecture Team | Focus Mode provenance + opt-in AI rules (not confirmed in repo) |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Describes Focus Mode state transitions (enter/exit, restore previous view state, breadcrumbs/back)
- [ ] Describes how provenance + citations are carried through UI state
- [ ] Validation steps listed and repeatable (unit + integration + e2e)
- [ ] Governance + CARE/sovereignty considerations explicitly stated (sensitive layers, restricted locations)

## 🗂️ Directory Layout

### This document

- `path`: `web/src/state/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI (frontend) | `web/` | React + map/narrative UI |
| UI state | `web/src/state/` | State container setup, reducers/slices, selectors, middleware |
| APIs | `src/server/` | Contracted access layer (REST/GraphQL); redaction rules |
| Schemas | `schemas/` | JSON schemas (including layer registry + telemetry) |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts with provenance |

### Expected file tree for this sub-area

~~~text
📁 web/
└── 📁 src/
    └── 📁 state/
        ├── 📄 README.md
        ├── 📄 index.ts                  # public exports (optional)
        ├── 📄 store.ts                  # store config (if using Redux-style container)
        ├── 📄 types.ts                  # shared state types (TypeScript)
        ├── 📁 slices/                   # feature reducers (Focus Mode, map, timeline, settings…)
        ├── 📁 selectors/                # shared + feature selectors
        ├── 📁 middleware/               # provenance/telemetry interceptors (optional)
        ├── 📁 persistence/              # hydration (URL state, localStorage) (optional)
        └── 📁 __tests__/                # reducer/selector tests
~~~

## 🧭 Context

### Background

- The KFM UI must keep multiple components in sync (map view, timeline, story panel, search), while supporting a dedicated Focus Mode flow.
- A predictable state container (e.g., Redux or Context/Reducers) helps coordinate these transitions consistently.

### Assumptions

- The frontend lives under `web/`.
- State is managed via a predictable container (e.g., Redux or React Context/Reducers).
- Focus Mode enters via a user selection, then an API request fetches a “context bundle” (narrative + citations + map/timeline hints).

### Constraints / invariants

- Canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend consumes contracts via **APIs only** (no direct graph dependency).
- Focus Mode must only present content with provenance; any AI-generated/predictive content is clearly labeled and opt-in.
- Sensitive layer or restricted-location handling must prevent “hidden data leakage” (including persistence and telemetry).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which state container is canonical in this repo (Redux vs Context/Reducers)? | UI Team | TBD |
| What parts of state are persisted (URL/localStorage) and what is explicitly non-persisted (sensitive)? | UI + Governance | TBD |
| Do we standardize an “audit/provenance panel” state shape across Focus Mode? | UI + Docs | TBD |

### Future extensions

- URL-driven state (deep links into Focus Mode with entity ID + time window).
- Offline-friendly caching for non-sensitive layers (opt-in).
- Telemetry hooks for state transitions (focus enter/exit, layer toggles) tied to a schema.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[User interaction] --> B[UI Components]
  B --> C[State container (web/src/state)]
  C --> D[API layer (contracted)]
  D --> E[Render: map + timeline + narrative]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant UI as UI (FocusMode)
  participant State as State container
  participant API as API
  participant Graph as Graph

  UI->>State: dispatch(enterFocus(entity_id))
  State->>API: request Focus context bundle (entity_id)
  API->>Graph: fetch subgraph + provenance refs (with redaction)
  Graph-->>API: context bundle
  API-->>State: narrative + citations + audit flags + focus hints
  State-->>UI: update focus + map/timeline hints
~~~

## 📦 Data & Metadata

### Inputs

| Input | Source | Sensitivity | Notes |
|---|---|---|---|
| Focus Mode context bundle | API (`src/server/`) | mixed | Narrative + citations + audit flags + focus hints |
| Search results / entity lists | API | public/mixed | Should include provenance refs where applicable |
| Layer registry config | UI config (`web/**/layers/**/*.json`) | mixed | Includes layer metadata + sensitivity/access flags |
| Map interaction events | MapLibre/Cesium component | public | Viewport, selected feature IDs, hover state |
| Timeline interaction events | Timeline component | public | Selected time window, cursor, filters |
| User preferences | UI | public | Accessibility toggles, display preferences |

### Sensitivity & redaction

- Treat API payloads as the source of truth for sensitivity flags; state must preserve these flags so UI gates match.
- Avoid persisting sensitive state by default (e.g., restricted layer selections, precise coordinates when flagged).
- If URL state is used, ensure it does not encode restricted locations without a governance-reviewed generalization rule.

### Quality signals

- Deterministic state transitions (same inputs → same state).
- Focus Mode always has an “audit path” from rendered narrative to sources (IDs/citations present).
- State cleanup is reliable on exit (no cross-entity bleed; prior layers/viewport restored correctly).

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Collections involved: returned indirectly via API payloads (store IDs as opaque strings).
- Items involved: returned indirectly via API payloads (store IDs as opaque strings).
- Extension(s): not confirmed in repo (UI should not assume any specific STAC extensions).

### DCAT

- Dataset identifiers: displayed in audit/provenance panels when provided by the API.
- License mapping: UI should be able to show dataset license/attribution if present.
- Contact / publisher mapping: optional; display if present.

### PROV-O

- `prov:wasDerivedFrom`: store and render “source list” when provided (do not invent).
- `prov:wasGeneratedBy`: store run/activity IDs when provided.
- Activity / Agent identities: display if present.

### Versioning

- Treat IDs as versioned references; if the API exposes predecessor/successor links, use them for navigation/history.
- Never “merge” versions client-side without an explicit contract; defer to the API.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| UI state (`web/src/state`) | Predictable UI state, sync map/timeline/narrative, caching + persistence rules | store/actions/selectors |
| APIs | Serve contracts + redaction | REST/GraphQL |
| UI | Map + narrative rendering | API calls + selectors |
| Focus Mode | Contextual narrative view | provenance-linked bundle |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| API schemas | `src/server/` + docs | Contract tests required |
| Layer registry | `web/**/layers/**/*.json` | Schema-validated |
| Telemetry schemas | `schemas/telemetry/` | Semver + changelog |
| State types | `web/src/state/types.ts` (proposed) | Semver at app-level |

### Extension points checklist (for future work)

- [ ] UI: add new feature state slice + selectors + tests
- [ ] APIs: contract updates for new Focus Mode bundle fields + tests
- [ ] UI: layer registry entry + access rules (if new layers)
- [ ] Focus Mode: provenance references enforced (no uncited default rendering)
- [ ] Telemetry: new signals + schema version bump (if adding new UI events)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

State should hold:

- the active focus target (`entity_id` / `story_node_id`)
- the loaded context bundle (narrative + citations + audit/provenance + flags)
- view synchronization hints (map center/zoom, time window, suggested layers)
- navigation history (breadcrumbs / back stack) so prior view state can be restored on exit

### Provenance-linked narrative rule

- Every narrative claim shown in Focus Mode must trace to a dataset / record / asset ID.
- If a context bundle contains narrative without citations/provenance, treat it as **non-displayable by default** (or display only with an explicit, governance-approved warning).

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (this README included)
- [ ] Unit tests for reducers/slices + selectors (`__tests__/`)
- [ ] Integration tests for Focus Mode flow (enter/exit, restore state, citation rendering)
- [ ] UI schema checks (layer registry)
- [ ] E2E test for critical paths (map click → focus → back navigation)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) run unit tests
# pnpm test

# 2) run e2e tests
# pnpm test:e2e

# 3) lint markdown
# pnpm lint:docs
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| focus_enter / focus_exit | state container | `docs/telemetry/` + `schemas/telemetry/` |
| layer_toggle | map layer UI | `docs/telemetry/` + `schemas/telemetry/` |
| citation_click | story renderer | `docs/telemetry/` + `schemas/telemetry/` |
| api_focus_latency_ms | API client | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates

- UI maintainer review is required for changes affecting Focus Mode state, provenance rendering, or persistence behavior.
- Governance review is required if a change can expose sensitive layers/locations or weakens opt-in requirements for AI-generated content.

### CARE / sovereignty considerations

- Sensitive or culturally restricted locations must not be revealed via:
  - persisted state (localStorage/URL)
  - telemetry events
  - screenshots/export flows
- Prefer generalization (area/region) over point precision when sensitivity flags require it.

### AI usage constraints

- State must not automatically surface AI-generated summaries or predictions; they must be opt-in and clearly labeled with uncertainty metadata.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial `web/src/state` README | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

