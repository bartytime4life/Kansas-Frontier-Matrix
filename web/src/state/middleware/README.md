---
title: "KFM UI State Middleware — README"
path: "web/src/state/middleware/README.md"
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

doc_uuid: "urn:kfm:doc:web:state:middleware:readme:v1.0.0"
semantic_document_id: "kfm-web-state-middleware-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:state:middleware:readme:v1.0.0"
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

# KFM UI State Middleware — README

## 📘 Overview

### Purpose

- Define the **responsibilities, constraints, and conventions** for UI state middleware under `web/src/state/middleware/`.
- Ensure UI state side-effects remain **architecture-synced** with the canonical KFM pipeline and contracts:
  - UI reads **only** from contracted APIs (never from Neo4j directly).
  - Focus Mode surfaces **provenance-linked** context only.
- Provide a single place to document:
  - how to add middleware safely,
  - how to keep middleware deterministic/testable,
  - how to prevent “accidental policy” decisions in the UI layer (e.g., ad-hoc redaction logic).

### Scope

| In Scope | Out of Scope |
|---|---|
| Middleware responsibilities (network side-effects, caching rules, telemetry, error normalization) | Choosing the global state library (Redux/Zustand/etc. — **not confirmed in repo**) |
| Focus Mode triggers (enter/exit/fetch context bundle) at the UI boundary | Implementing the API server / graph queries (`src/server/**`) |
| Guardrails: provenance-required content, AI opt-in labeling, sensitive-location protection | Story Node authoring rules (lives in Story Node docs/templates) |
| Recommended tests and validation steps for middleware | Styling/UI layout details (components live elsewhere) |

### Audience

- **Primary:** Frontend contributors working on `web/**` state flow and data fetching.
- **Secondary:** API/Graph contributors reviewing UI integration and contract alignment.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc include: **middleware**, **action**, **side-effect**, **contract**, **Focus Mode**, **Story Node**, **context bundle**, **provenance**, **redaction**, **classification**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Canonical pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Non‑negotiable ordering + boundaries |
| v13 blueprint (if adopted) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Arch Team | Explicit API boundary + Focus Mode provenance rule |
| API boundary + contracts | `src/server/` + `src/server/contracts/` | API Team | UI consumes contracted responses only |
| UI schemas | `schemas/ui/` | Platform | Layer registries + UI artifacts should validate here (if present) |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative | Defines story structure/citations/focus hints |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Ensures structure + CI-ready docs |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (path matches; required fields present)
- [ ] Middleware constraints/invariants explicitly documented (API boundary, provenance-only Focus Mode, AI opt-in)
- [ ] Directory layout included (expected file tree)
- [ ] Validation & CI steps listed and repeatable (or explicitly marked “not confirmed in repo”)
- [ ] Governance considerations stated (sensitive locations, sovereignty, no policy-by-UI)

## 🗂️ Directory Layout

### This document

- `path`: `web/src/state/middleware/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI app root | `web/` | React/Map UI, state, UI registries |
| UI state root | `web/src/state/` | Store/slices/selectors/actions (structure **not confirmed in repo**) |
| API boundary | `src/server/` | Contracted access layer (REST/GraphQL) |
| Graph | `src/graph/` | Ontology bindings + ingest logic (UI does not access directly) |
| Schemas | `schemas/` | JSON Schema (+ optional SHACL) for contracts and catalogs |
| Story Nodes | `docs/reports/story_nodes/` | Narrative docs consumed by Focus Mode |
| Governance | `docs/governance/` | Ethics/sovereignty/approval gates |

### Expected file tree for this sub-area

> This is the recommended layout for a Redux-style middleware chain. Specific filenames are **not confirmed in repo** unless already present.

~~~text
web/
└── 📁 src/
    └── 📁 state/
        └── 📁 middleware/
            ├── 📄 README.md                         # This file
            ├── 📄 index.ts                          # middleware export/compose (not confirmed in repo)
            ├── 📄 apiBoundary.middleware.ts          # API-only I/O + contract checks (not confirmed in repo)
            ├── 📄 focusMode.middleware.ts            # Focus Mode context bundle fetch (not confirmed in repo)
            ├── 📄 provenanceGuard.middleware.ts      # provenance-required enforcement (not confirmed in repo)
            ├── 📄 redactionGuard.middleware.ts       # prevents sensitive display paths (not confirmed in repo)
            ├── 📄 telemetry.middleware.ts            # UI telemetry emitters (not confirmed in repo)
            ├── 📄 errors.middleware.ts               # normalize errors/retries/backoff (not confirmed in repo)
            └── 📁 __tests__/                         # middleware unit tests (not confirmed in repo)
                └── 📄 *.test.ts
~~~

## 🧭 Context

### Background

KFM is intentionally **layered**. UI middleware exists to keep UI side-effects aligned with the **API boundary** and the provenance-first narrative rules.

Canonical (non‑negotiable) ordering:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

Middleware should help ensure the UI never “short-circuits” those boundaries by:
- making all network calls go through the API layer,
- carrying provenance/evidence IDs forward into state,
- blocking UI rendering paths that would create “unsourced narrative”.

### Assumptions

- A “middleware chain” concept exists in the UI state layer (Redux-like). If the state library differs, treat this folder as the “UI side-effect boundary” and adapt accordingly (**not confirmed in repo**).
- The API boundary provides a “Focus context bundle” (name/endpoint **not confirmed in repo**) that returns:
  - narrative content + citations,
  - provenance/evidence references,
  - optional focus hints (map center, time window, suggested layers).

### Constraints / invariants (must not be violated)

- **API boundary is mandatory:** UI never queries Neo4j directly. All graph/catalog access comes from contracted APIs.
- **Focus Mode is provenance-linked only:** Focus Mode must not display orphan facts or unsourced narrative.
- **Predictive / AI-generated content rules:**
  - opt-in only,
  - clearly labeled,
  - uncertainty metadata included,
  - never presented as unmarked fact.
- **Redaction & sensitive locations:**
  - UI must not reveal restricted/sensitive locations via interaction/zoom/tooltips,
  - redaction is enforced at API, but UI must avoid “reconstruction attacks” (e.g., caching exact points, showing raw coords).
- **Determinism:** middleware should be testable; avoid hidden global side-effects; use stable request IDs and explicit inputs.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the state library and middleware signature? | TBD | TBD |
| What is the canonical “Focus context bundle” contract (fields + schema)? | TBD | TBD |
| Where do telemetry schemas live (`schemas/telemetry/**`)? | TBD | TBD |
| What client-side persistence is allowed by classification (localStorage/cache rules)? | Governance + UI | TBD |

### Future extensions

- Add a **contract validation middleware** that checks (lightweight) response shape/version tags against `src/server/contracts/**` or derived schemas (**implementation not confirmed in repo**).
- Add a **provenance HUD/audit trail** middleware hook:
  - every “narrative render” action emits an auditable event with evidence IDs.
- Add an **offline mode** strategy:
  - allow pre-cached open/public bundles only,
  - never persist restricted coordinates locally.

## 🧱 Architecture

### Middleware goals

Middleware in KFM UI state exists to:
- keep side-effects centralized and testable,
- enforce boundary rules (API-only, provenance-required, redaction-aware),
- standardize retries/errors/telemetry so components stay simple.

### Responsibilities (recommended)

1. **API boundary middleware**
   - transforms UI intents into API calls
   - attaches request IDs + cancellation tokens
   - blocks any attempt to call “graph-like” endpoints not in contracts (**contract registry not confirmed in repo**)

2. **Focus Mode middleware**
   - on `enterFocusMode(entity_id, time_window?)`:
     - fetch context bundle via API,
     - store narrative + evidence IDs + focus hints,
     - dispatch “map focus” and “timeline focus” actions (exact action names **not confirmed in repo**)

3. **Provenance guard middleware**
   - blocks Focus Mode renders if evidence IDs are missing
   - forces explicit “insufficient evidence” UI state instead of silently rendering

4. **Redaction guard middleware**
   - prevents storing or emitting sensitive fields to logs/telemetry
   - prevents high-precision coordinate rendering when classification requires generalization

5. **Telemetry middleware**
   - emits analytics/telemetry events as schema-validated payloads (schema location **not confirmed in repo**)
   - recommended events:
     - `focus_mode_entered`, `focus_bundle_loaded`, `provenance_panel_opened`, `citation_clicked`, `redaction_notice_shown`

6. **Error normalization middleware**
   - standardizes API errors into:
     - retryable vs non-retryable
     - auth vs network vs contract mismatch
   - ensures UI components don’t interpret raw error payloads

### Ordering (recommended)

> Order matters. “Guards” should run before “effects,” and “telemetry” should run after state updates.

1) provenance/redaction guards  
2) API/fetch effects  
3) state update reducers  
4) telemetry emission  
5) error normalization (or error-first, depending on store design — **not confirmed in repo**)

### Suggested action conventions (optional)

> Field names are suggestions; align with the project’s actual store types (**not confirmed in repo**).

- All side-effect actions include:
  - `meta.request_id` (stable per request)
  - `meta.trace_id` (optional)
  - `meta.classification` (optional; inherited from API response if provided)
- Focus Mode actions include:
  - `payload.entity_id`
  - `payload.time_window` (optional)
  - `payload.intent` (story/event/place/person)

## 🗺️ Diagrams

### UI side-effect boundary (conceptual)

~~~mermaid
flowchart LR
  UI[React Components] -->|dispatch| A[Actions]
  A --> M[Middleware Chain]
  M -->|contracted call| API[API Boundary: src/server]
  API -->|response| M
  M --> R[Reducers / Store]
  R --> UI
~~~

### Focus Mode context bundle (conceptual sequence)

~~~mermaid
sequenceDiagram
  participant UI as UI
  participant MW as Middleware
  participant API as API
  UI->>MW: enterFocusMode(entity_id, time_window?)
  MW->>API: fetchContextBundle(entity_id, time_window?)
  API-->>MW: context bundle (narrative + citations + evidence IDs)
  MW-->>UI: store update + focus hints (map/time/layers)
~~~

## 🧠 Story Node & Focus Mode Integration

### Focus Mode flow (implementation-oriented)

A typical Focus Mode sequence is:

- user selects an entity/event in the map/narrative
- UI dispatches an action to enter Focus Mode with an entity ID
- middleware triggers an API request for a “context bundle”
- UI renders:
  - narrative text with citations,
  - an audit/provenance panel,
  - synchronized map + timeline state

(Exact component names are **not confirmed in repo**.)

### Context bundle expectations (client-side)

| Field | Why it matters | Notes |
|---|---|---|
| Narrative content (Markdown or structured blocks) | Focus Mode display | Rendering pipeline is UI concern |
| Citations / evidence refs | Enforce provenance-only rule | Must be present for Focus Mode |
| PROV/STAC/DCAT identifiers | Auditability + traceability | Prefer stable IDs over raw URLs |
| Focus hints (center/time/layers) | Map/timeline synchronization | Optional but recommended |
| AI flags + uncertainty metadata | Prevent “unmarked fact” | Required if predictive content present |

### Citation handling (UI + middleware boundary)

- Middleware should treat “narrative + citations” as a single atomic payload:
  - do not store narrative without its evidence references
  - do not allow Focus Mode render if evidence references are missing
- UI rendering of citations (e.g., transforming `【source†Lx-Ly】` references into clickable UI) lives in the rendering layer, but middleware should ensure the underlying source bundle is available (exact citation syntax/renderer **not confirmed in repo**).

### Predictive / AI-generated content

- Middleware should not silently merge predictive content into “facts.”
- If the API returns AI/prediction content:
  - it must be labeled and stored separately (recommended),
  - uncertainty metadata must be preserved,
  - UI must require explicit opt-in.

## 🌐 STAC, DCAT & PROV Alignment

### Why middleware cares

Even though STAC/DCAT/PROV are “data/catalog” concerns, the UI must carry **evidence identifiers** into state so that Focus Mode and Story Nodes remain auditable.

### Recommended client rules

- Preserve evidence identifiers end-to-end:
  - STAC Item/Collection IDs
  - DCAT dataset IDs
  - PROV activity IDs
- Avoid “evidence loss” transformations:
  - if middleware normalizes entities into store slices, it must keep the source/evidence references attached or cross-linked.

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- Markdown protocol check:
  - front-matter present,
  - required sections present,
  - no forbidden fields.
- Link/reference checks:
  - ensure referenced paths exist where applicable.
- Secrets + PII scans:
  - middleware must not hardcode tokens/keys,
  - telemetry must not emit sensitive coordinates.
- Tests:
  - middleware unit tests for guards and side-effect orchestration,
  - integration tests for Focus Mode load flow (if test harness exists).

### Example placeholders — replace with repo-specific commands

~~~bash
# Typecheck / lint (tooling not confirmed in repo)
# pnpm -C web lint
# pnpm -C web test

# Middleware unit tests (not confirmed in repo)
# pnpm -C web test middleware

# Contract checks (if available in CI; not confirmed in repo)
# pnpm -C web test:contracts
~~~

### CI expectations (if configured)

- Markdown lint + front-matter validation
- Unit tests for middleware and state layer
- Contract tests for API surfaces used by Focus Mode (if present)
- Security scans (secrets/PII) and governance gates where applicable

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is required when UI/middleware changes could:
- expand access to sensitive/restricted information,
- reveal sensitive locations via map interaction/zoom,
- persist sensitive fields locally (caches),
- change how AI/predictive content is labeled or gated.

(Approval roles/process: **not confirmed in repo** — follow `docs/governance/ROOT_GOVERNANCE.md`.)

### CARE / sovereignty considerations

- Treat culturally sensitive or sovereignty-controlled locations as **high-risk by default**.
- Prefer:
  - aggregation/generalization,
  - explicit access gating,
  - clear user-facing redaction notices where required.

### AI usage constraints

- Allowed (for this document): summarization, structure extraction, translation, keyword indexing.
- Prohibited: generating new policy; inferring sensitive locations (directly or indirectly).
- In product behavior:
  - AI/predictive outputs must be opt-in and clearly labeled,
  - uncertainty must be preserved and shown.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---:|---|---|
| v1.0.0 | 2025-12-25 | Initial middleware README (constraints + Focus Mode integration) | KFM UI |

---

### Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- v13 blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Implementation guidance (draft): `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` (**not confirmed in repo**)  
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---

