---
title: "KFM Web UI — State Effects"
path: "web/src/state/effects/README.md"
version: "v1.0.0"
last_updated: "2025-12-25"
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

doc_uuid: "urn:kfm:doc:web:state:effects:readme:v1.0.0"
semantic_document_id: "kfm-web-state-effects-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:state:effects:readme:v1.0.0"
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

# Web UI — State Effects

**Directory:** `web/src/state/effects/`

> **Purpose (required):** Define the **side-effect boundary** for the KFM web app’s state system:
> network calls to contracted APIs, persistence, telemetry, routing sync, and orchestration needed to keep **Map + Timeline + Story/Focus Mode** consistent—while enforcing KFM’s non‑negotiables (API boundary, provenance-only Focus Mode, and governance constraints).

---

## 📘 Overview

### Purpose

This directory contains the **effect layer** for the web UI state system: code that:
- reacts to state transitions and UI intents (e.g., “enter Focus Mode”),
- performs side effects (fetch, cache, persist, log, abort),
- dispatches state updates back into the store.

Effects are where the UI “touches the outside world”—so they must be **contract-first**, **auditable**, and **safe-by-default**.

### Scope

| In Scope | Out of Scope |
|---|---|
| Fetching data via API contracts (REST/GraphQL) | Any direct Neo4j access or Cypher execution |
| Focus Mode context-bundle loads + lifecycle | Defining new API endpoints (belongs in `src/server/` + contract docs) |
| Layer registry loading + validation integration (consumer side) | Authoring schemas (`schemas/**`) or catalogs (`data/**`) |
| Request cancellation, de-duping, caching keys | Domain ETL logic (belongs in `src/pipelines/**`) |
| Telemetry events from UI interactions | Governance policy creation (must be in governed docs only) |

### Audience

- **Primary:** Frontend engineers working in `web/` on state, map, timeline, and Focus Mode UX.
- **Secondary:** API/contract owners who need to understand how the UI consumes contracts and enforces redaction/provenance.
- **Tertiary:** Governance reviewers validating that the UI cannot leak restricted information through interaction patterns.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Effect:** side-effectful workflow that may call APIs/persistence/telemetry and then updates state.
  - **Context bundle:** API response providing Focus Mode content + provenance references (structure **not confirmed in repo**; see API contracts).
  - **Provenance-linked:** content carries resolvable evidence IDs (STAC/DCAT/PROV and/or Story Node citations).
  - **Redaction/generalization:** policies enforced at the API boundary and honored by UI rendering and behavior.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Effects directory | `web/src/state/effects/` | Web/UI | This boundary: side effects only |
| API contracts | `src/server/contracts/**` | API | Canonical contract home (v13 target) |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Curators | Defines optional Focus Mode controls |
| Master guide | `docs/MASTER_GUIDE_v12.md` | Core | Canonical pipeline and invariants |
| Governance | `docs/governance/**` | Council | Sensitivity + sovereignty rules |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (path matches file location)
- [ ] Effects responsibilities clearly separated from reducers/selectors/components
- [ ] Constraints explicitly stated: **UI → API only**, **provenance-only Focus Mode**, **no sensitive inference**
- [ ] Examples use **inner tildes** fencing and remain **implementation-agnostic** where repo details are unknown
- [ ] Telemetry + governance review triggers listed (no secrets/PII)

---

## 🗂️ Directory Layout

### This document

- `path`: `web/src/state/effects/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Frontend | `web/` | React/Map UI, layer registry consumption, Focus Mode UX |
| API boundary | `src/server/` | Contracted access layer, redaction enforcement |
| API contracts | `src/server/contracts/` | OpenAPI/GraphQL contracts + tests |
| Schemas | `schemas/` | UI registry schema, story node schema, telemetry schemas |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published narrative artifacts |
| Governance | `docs/governance/` | FAIR+CARE, sovereignty, review gates |

### Expected file tree for this sub-area

> The exact filenames below are **not confirmed in repo**. This is the **recommended shape** for a maintainable effects layer.

~~~text
📁 web/
└── 📁 src/
    └── 📁 state/
        └── 📁 effects/
            ├── 📄 README.md
            ├── 📄 index.ts                 (exports effect entrypoints)            (not confirmed in repo)
            ├── 📄 focusMode.effects.ts     (Focus Mode orchestration)              (not confirmed in repo)
            ├── 📄 layerRegistry.effects.ts (load/validate layer registry)          (not confirmed in repo)
            ├── 📄 timeline.effects.ts      (time window sync + URL/state)          (not confirmed in repo)
            ├── 📄 map.effects.ts           (map intent orchestration)              (not confirmed in repo)
            ├── 📄 persistence.effects.ts   (local storage / session restore)       (not confirmed in repo)
            └── 📄 telemetry.effects.ts     (audit-safe UI telemetry emission)      (not confirmed in repo)
~~~

---

## 🧭 Context

### Background

KFM’s canonical system ordering is:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

The UI must remain a **consumer** of contracts and evidence; it must not become a “second backend.”
Effects are the best place to enforce that separation: they can call **only contracted APIs**, apply **cancellation and caching**, and update the store with results that are safe to render.

### Assumptions

- State management library is **not confirmed in repo** (Redux, Context/Reducers, Zustand, etc.). This README describes patterns compatible with any predictable state container.
- API clients likely live under `web/src/**` (exact location **not confirmed in repo**). Effects should depend on **interfaces** rather than importing fetch logic ad hoc.
- Layer registry config exists (location **not confirmed in repo**), but must be schema-validated against `schemas/ui/` at some boundary (build/CI and/or runtime).

### Constraints / invariants (non-negotiables)

1. **No UI direct-to-graph reads**
   - `web/` must never query Neo4j directly; all graph access is via the API boundary.
2. **Focus Mode is provenance-only**
   - No “orphan facts” in Focus Mode UI state. If an effect cannot attach evidence IDs, it must not promote content into Focus Mode as fact.
3. **Contracts are canonical**
   - Effects consume API contracts and must not “invent” fields; contract mismatches are treated as errors (surfaceable in an audit panel).
4. **No sensitive inference**
   - Effects must not combine layers/interactions in a way that reconstructs restricted locations or culturally sensitive knowledge.

### Open questions

| Question | Owner | Target |
|---|---|---|
| Where is the layer registry located in `web/` and how is it validated in CI? | Web + Contracts | TBD |
| What is the canonical Focus Mode context bundle contract (OpenAPI/GraphQL type)? | API | TBD |
| What telemetry schema(s) exist for UI events? | Telemetry owners | TBD |

---

## 🗺️ Diagrams

### Effects boundary in the canonical pipeline

~~~mermaid
flowchart LR
  UI[React UI<br/>components] -->|dispatch intents| Store[State store]
  Store -->|state changes| Effects[Effects layer<br/>web/src/state/effects]
  Effects -->|contracted calls| API[API boundary<br/>src/server]
  API -->|redacted + provenance-linked| Effects
  Effects -->|dispatch updates| Store
  Store --> UI

  API --> Evidence[STAC/DCAT/PROV refs<br/>evidence IDs]
  Evidence --> UI
~~~

### Sequence: Enter Focus Mode (recommended)

~~~mermaid
sequenceDiagram
  participant User
  participant UI
  participant Store
  participant Effects
  participant API

  User->>UI: Click entity / story link
  UI->>Store: dispatch enterFocus(entity_id)
  Store->>Effects: effect triggered (enterFocus)
  Effects->>API: fetch Focus context bundle (contracted)
  API-->>Effects: bundle (narrative + citations + evidence IDs + flags)
  Effects->>Store: dispatch focusBundleLoaded(bundle)
  Store-->>UI: render narrative + audit panel + map/timeline focus
~~~

---

## 🧠 Story Node & Focus Mode Integration

### How effects should treat Focus Mode content

Effects must assume Focus Mode is **strict**:
- If a response cannot be provenanced (missing citations/evidence IDs), the effect should:
  - keep it in a “draft/unverified” state channel, or
  - surface it only behind an explicit warning/opt-in control,
  - and/or reject it (depending on UI policy).

### Optional Focus Mode controls (from Story Node template)

Story Nodes may include structured hints that an effect can apply to state (map focus, layers, time):

~~~yaml
focus_layers:
  - "TBD-layer-id"
focus_time: "YYYY-MM-DD/YYYY-MM-DD"
focus_center: [ -98.0000, 38.0000 ]
~~~

### Recommended responsibilities for `focusMode.effects.*` (conceptual)

- Resolve the navigation intent (entity ID / story ID).
- Fetch the Focus context bundle from the API.
- Apply:
  - `focus_center` → map viewport intent,
  - `focus_time` → timeline window intent,
  - `focus_layers` → layer toggle intent.
- Emit telemetry that is:
  - **non-PII**, and
  - does not leak restricted coordinates.

---

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- [ ] Typecheck and lint (web)
- [ ] Unit tests for effect orchestration (mock API client)
- [ ] Contract compatibility checks (API schema snapshots vs UI types) (**not confirmed in repo**)
- [ ] UI registry schema checks (`schemas/ui/**`) wherever the registry is produced/consumed
- [ ] Security/sovereignty checks where applicable (no sensitive leakage by interaction patterns)

### Reproduction (deterministic)

> Commands are **not confirmed in repo**; replace with canonical project scripts.

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) Typecheck
# npm run typecheck

# 2) Unit tests
# npm test

# 3) UI layer registry schema validation (if present)
# node tools/validate_ui_registry.js web/<path-to-layer-registry>

# 4) Contract checks (if present)
# npm run contract:test
~~~

### Telemetry signals (recommended minimum)

| Signal | When emitted | Notes |
|---|---|---|
| `ui_effect_started` | effect begins | include effect name + correlation id |
| `ui_effect_succeeded` | effect completes | include duration + cache hit/miss |
| `ui_effect_failed` | effect errors | include error class (no secrets) |
| `focus_mode_entered` | enter Focus Mode | include entity/story identifier (non-sensitive) |
| `focus_bundle_loaded` | Focus bundle received | include counts of citations/evidence IDs |
| `redaction_notice_shown` | when UI displays redaction/generalization | include reason code only |

---

## 📦 Data & Metadata

### Inputs

| Input | Source | Notes |
|---|---|---|
| User intents | UI components | clicks, toggles, navigation |
| Context bundle | API boundary | must be provenance-linked |
| Layer registry | web config + schemas | validate against `schemas/ui/` |
| Story Node metadata | `docs/reports/story_nodes/**` | focus hints, citations |

### Outputs

| Output | Destination | Notes |
|---|---|---|
| State updates | store reducers/slices | effects should not mutate state directly |
| Cached responses | in-memory cache/local storage | include version keys to avoid stale schema |
| Telemetry events | telemetry sink | follow privacy + sovereignty constraints |

### Sensitivity & redaction

- Treat “location-like” values as potentially sensitive.
- Never persist exact coordinates unless the data is explicitly classified as safe for persistence and display.
- Honor API-provided redaction/generalization flags in both rendering **and** behavior (e.g., disable zoom-to-precise-point if generalized).

---

## 🌐 STAC, DCAT & PROV Alignment

Effects do not generate catalogs, but they must **preserve evidence references** so downstream UI features (audit panel, citations, exports) can remain provenance-complete.

Recommended practice:
- Store “evidence pointers” as opaque IDs:
  - STAC Item IDs
  - DCAT dataset IDs
  - PROV activity IDs
- Avoid flattening evidence into human-only strings.

Versioning expectations (consumer-side):
- Cache keys should include:
  - `api_contract_version` (or equivalent; **not confirmed in repo**),
  - `dataset_version` or catalog version when available.

---

## 🧱 Architecture

### Design principles for effects (UI-side)

1. **Effects are orchestration, not business logic**
   - Keep domain logic in API/services. Effects coordinate calls + state updates.

2. **Dependency-injection friendly**
   - Effects should accept an `apiClient`, `telemetry`, and `clock` interface so they are testable.

3. **Cancellation and “latest wins”**
   - Use AbortController (fetch) or “takeLatest” semantics (if using sagas/observables; **not confirmed in repo**).

4. **No implicit data promotion**
   - Effects must not elevate content into Focus Mode unless the evidence requirements are satisfied.

### Example: effect signature (implementation-agnostic)

~~~ts
// Pseudocode (not confirmed in repo)

type EffectDeps = {
  api: { fetchFocusBundle: (id: string, opts?: { signal?: AbortSignal }) => Promise<unknown> };
  telemetry: { emit: (name: string, props?: Record<string, unknown>) => void };
};

export async function enterFocusModeEffect(
  deps: EffectDeps,
  params: { entityId: string; correlationId: string; signal?: AbortSignal }
): Promise<void> {
  deps.telemetry.emit("focus_mode_entered", { entityId: params.entityId, correlationId: params.correlationId });

  const bundle = await deps.api.fetchFocusBundle(params.entityId, { signal: params.signal });

  // validate bundle shape against contract types (not confirmed in repo)
  // dispatch focusBundleLoaded(bundle)
  deps.telemetry.emit("focus_bundle_loaded", { correlationId: params.correlationId });
}
~~~

---

## ⚖ FAIR+CARE & Governance

### Review gates (when governance review is required)

Governance review is required when an effects change:
- introduces a new interaction that could reveal restricted locations by aggregation/zoom,
- changes how redaction/generalization flags are interpreted,
- adds new telemetry fields that could encode sensitive identifiers,
- adds any AI-driven narrative behaviors surfaced to users (opt-in + clearly marked required).

### CARE / sovereignty considerations

- Do not infer or reconstruct sensitive locations from multiple “safe” layers.
- If an effect composes multiple datasets, ensure the most restrictive policy dominates.
- Prefer coarse/aggregate behaviors in public mode (e.g., bounding boxes, region-level summaries).

### AI usage constraints (UI-side)

- Allowed: summarization or explanation **only** when provenance-linked and clearly labeled.
- Prohibited: generating new policy, inferring sensitive locations, or presenting AI output as unmarked fact.

---

## 🕰️ Version History

| Version | Date | Summary | Author | PR / Issue |
|---|---:|---|---|---|
| v1.0.0 | 2025-12-25 | Initial effects-layer README (contracts + provenance boundary guidance) | TBD | TBD |

---

### Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- v13 redesign blueprint (draft): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`

