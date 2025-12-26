---
title: "KFM Web UI — app/_lib README"
path: "web/src/app/_lib/README.md"
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

doc_uuid: "urn:kfm:doc:web:app:_lib:readme:v1.0.0"
semantic_document_id: "kfm-web-app-lib-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:app:_lib:readme:v1.0.0"

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

# KFM Web UI — `web/src/app/_lib`

> **Purpose (required):** This folder hosts **shared, contract-aligned UI logic** used by the KFM web application routes/components under `web/src/app/`.  
> It centralizes **API-bound data access**, **citation/provenance rendering helpers** for Story Nodes & Focus Mode, and **layer-registry utilities**, while preventing architecture drift (e.g., “UI talking directly to the graph”).

## 📘 Overview

### Purpose

- Provide a single “source of truth” for shared helpers used across `web/src/app/**`.
- Encode UI-side invariants:
  - **UI reads through the API boundary only** (never directly from Neo4j/graph storage).
  - **No unsourced narrative rendering** (citations and provenance must be preserved and visible).
  - **Layer registries are schema-validated** before use (where registry/schema infrastructure exists).

### Scope

| In Scope | Out of Scope |
|---|---|
| API client helpers (typed request/response wrappers, error normalization, redaction-aware display helpers) | API/server code (belongs under `src/server/`) |
| Story Node rendering helpers (Markdown → HTML pipeline hooks, citation parsing, source popovers) | Direct database/graph connectivity (Neo4j driver, raw Cypher calls) |
| Focus Mode UI helpers (context-bundle shaping, audit/provenance panel helpers, focus hints) | Data pipeline logic or catalog/provenance generation (belongs under `src/pipelines/` + `data/`) |
| Layer registry utilities (loading, validating, normalizing layer configs) | Authoring story nodes (belongs under `docs/reports/story_nodes/`) |
| Small deterministic utilities (formatting, pure transforms, type guards) | Heavy side-effect modules (global state singletons, hidden I/O, “do everything” god modules) |

### Audience

- **Primary:** KFM frontend contributors working in `web/`.
- **Secondary:** API/Graph contributors reviewing UI boundary compliance; maintainers enforcing CI gates.

### Definitions (link to glossary)

- Glossary: `docs/glossary.md` (**not confirmed in repo** — update if glossary lives elsewhere)
- Terms used in this doc:
  - **API boundary:** Contracted interface under `src/server/` (REST/GraphQL) used by UI.
  - **Story Node:** Governed narrative artifact with citations and focus hints.
  - **Focus Mode:** UI state that displays provenance-linked context for a selected entity/story.
  - **Layer registry:** Machine-readable layer configuration(s) used to drive map overlays.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master guide (canonical ordering + invariants) | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical flow + constraints |
| v13 blueprint (contract + folder “truth”) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` (**not confirmed in repo**) | Architecture | Reinforces UI/API boundary + Focus Mode constraints |
| API contracts | `src/server/contracts/` | API | UI must follow contracts |
| UI schemas | `schemas/ui/` (**not confirmed in repo**) | UI/Platform | Layer registry schemas + validation |
| Story Nodes | `docs/reports/story_nodes/` | Narrative | Governed narrative artifacts |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative/Core | Front-matter + citation expectations |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | This README structure |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API/Core | Contract-first boundary changes |

### Definition of done (for this document)

- [ ] Front-matter complete + `path` matches `web/src/app/_lib/README.md`
- [ ] “In scope / out of scope” clearly prevents UI→Graph coupling
- [ ] Layer registry + citation handling expectations are described
- [ ] Validation steps are listed (commands are either accurate or explicitly “not confirmed in repo”)
- [ ] Governance + CARE considerations for UI redaction/sensitive layers are explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `web/src/app/_lib/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI | `web/` | Front-end application code (React/MapLibre/Cesium), Focus Mode UX, layer registries |
| API boundary | `src/server/` | Contracted access to graph + catalogs; redaction/generalization enforcement |
| API contracts | `src/server/contracts/` | OpenAPI/GraphQL contracts (semver + contract tests) |
| Graph | `src/graph/` | Ontology bindings + ingest/build tooling |
| Pipelines | `src/pipelines/` | ETL + catalog builders |
| Schemas | `schemas/` | JSON schemas (STAC/DCAT/PROV, telemetry, UI) |
| Story Nodes | `docs/reports/story_nodes/` | Governed narratives with citations + focus hints |
| Data outputs | `data/` | raw/work/processed + STAC/DCAT/PROV + PROV bundles |

### Expected file tree for this sub-area

> **Note:** This tree is a **recommended** organization pattern and may not match the current repo. If it differs, treat this README as the target convention and migrate incrementally.

~~~text
web/
└── 📁 src/
    └── 📁 app/
        └── 📁 _lib/
            ├── 📄 README.md
            ├── 📁 api/               # API client wrappers (contract-aligned)
            ├── 📁 citations/          # Story Node citations parsing/rendering helpers
            ├── 📁 focus/              # Focus Mode context shaping + audit helpers
            ├── 📁 layers/             # Layer registry loading/normalization/validation
            ├── 📁 telemetry/          # UI telemetry helpers (if adopted)
            └── 📁 utils/              # Small deterministic helpers (format/time/geo)
~~~

## 🧭 Context

### Background

The KFM UI is the user-facing “living atlas” layer: map exploration (2D MapLibre, optional 3D Cesium), narrative reading (Story Nodes), and contextual synthesis (Focus Mode).  
This folder exists to prevent duplicated ad-hoc logic across routes/components and to make core rules **easy to do** and **hard to bypass**.

### Assumptions

- The frontend is a React-based app under `web/` (often with a map + narrative panels).
- Story Nodes are authored in Markdown and include inline citations in the `【source†Lx-Ly】` style.
- Focus Mode is a dedicated UI state/component that renders narrative + map + audit/provenance panel.

(Where any assumption is wrong for the current repo, update this README to match reality rather than ignoring the mismatch.)

### Constraints / invariants

- **Canonical pipeline order is non-negotiable:**  
  ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode.
- **Decoupled contracts:** UI never queries Neo4j/graph storage directly; all graph access is through the API boundary.
- **No unsourced narratives:** the UI must not present factual narrative claims without citations/provenance references.
- **Redaction is enforced at/through the boundary:** UI must respect redaction flags/constraints returned by APIs and/or layer registry metadata.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Where are layer registries located in this repo (`web/**/layers/**` vs a different structure)? | UI | TBD |
| What is the canonical “context bundle” shape returned by Focus Mode APIs (fields for narrative, provenance, map hints)? | API/UI | TBD |
| What renderer is used for Story Node markdown (and how do we hook citations safely)? | UI | TBD |
| What UI schema(s) exist under `schemas/ui/` for layer registry validation? | UI/Platform | TBD |

### Future extensions

- Generate a typed UI client from `src/server/contracts/**` (contract-first client generation).
- Add a strict CI gate: “UI build fails if a Neo4j driver package is imported in `web/`.”
- Add runtime schema validation for layer registries (e.g., `schemas/ui/layer-registry.schema.json`).
- Add a standard “Provenance/Audit Panel” component library that renders STAC/DCAT/PROV references consistently.

## 🗺️ Diagrams

### System / dataflow diagram (how `_lib` fits)

~~~mermaid
flowchart LR
  subgraph UI[UI (web)]
    A[Routes & Components] --> L[_lib helpers]
    L --> R[Rendered Map + Narrative + Focus Mode]
  end

  R --> API[API boundary (src/server)]
  API --> G[Graph (src/graph / Neo4j)]
  API --> C[Catalogs (STAC/DCAT/PROV)]
~~~

### Optional: sequence diagram (Focus Mode)

~~~mermaid
sequenceDiagram
  participant User
  participant UI as UI (web)
  participant Lib as _lib
  participant API as API boundary
  participant Graph as Graph
  participant Cat as STAC/DCAT/PROV

  User->>UI: Select entity / open story
  UI->>Lib: buildFocusQuery(entity_id)
  Lib->>API: request Focus context bundle
  API->>Graph: fetch subgraph + ids
  API->>Cat: fetch provenance refs (optional)
  API-->>Lib: context bundle (narrative + citations + audit refs)
  Lib-->>UI: parsed citations + view models
  UI-->>User: Story + citations + audit panel + focused map state
~~~

## 🧠 Story Node & Focus Mode Integration

### Story Node rendering + citations

Story Nodes are Markdown narratives with inline citation tokens (e.g., `【source†L12-L18】`).  
The UI should render Markdown to HTML while **preserving citations** as interactive elements (links/popovers/footnotes).

Recommended responsibilities for `_lib`:

- Parse citation tokens from raw text into a structured representation (source id, line range, optional label).
- Provide a renderer adapter that:
  - renders citation tokens as interactive UI elements,
  - routes “show source” interactions to the audit/provenance panel, and
  - blocks or visually flags narrative sections that are missing required citations (if a governed policy exists).

### Focus Mode context helpers

Focus Mode typically:
- is entered via an entity selection,
- calls a Focus API to fetch a **context bundle**,
- renders narrative + citations + map/time hints + provenance.

Recommended responsibilities for `_lib`:

- Normalize Focus API payloads into UI-friendly view models.
- Provide helpers for reading focus hints (e.g., focus center/time/layers) and applying them to UI state.
- Provide utilities for the “audit/provenance panel” (format STAC/DCAT/PROV ids into user-readable references).

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- Markdown/doc checks (for this README):
  - front-matter present,
  - required sections exist,
  - footer refs present.
- Frontend checks (repo-dependent):
  - lint, typecheck, unit tests,
  - a11y checks for components consuming `_lib` helpers,
  - schema validation for any layer registries used by `_lib`.

### Example placeholders (replace with repo-specific commands)

~~~bash
# not confirmed in repo — replace with the actual commands/package manager
# npm run lint
# npm run typecheck
# npm run test

# If layer registries are schema-validated (recommended):
# node tools/validate_schema.js schemas/ui/layer-registry.schema.json web/**/layers/**/*.json
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| API responses (entities, focus bundles, search) | JSON | `src/server/` endpoints | Contract tests + runtime guards (recommended) |
| Story Node markdown | Markdown | `docs/reports/story_nodes/` | Story Node validation gates |
| Layer registries | JSON | `web/**/layers/**` (recommended) | `schemas/ui/**` (recommended) |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Parsed citations | In-memory structure | N/A | UI internal type contract |
| View models for Focus Mode | In-memory structure | N/A | UI internal type contract |
| Normalized layer registry entries | In-memory structure | N/A | UI schema (recommended) |

### Sensitivity & redaction

- Treat “sensitive” as a **first-class UI concern**:
  - if the API indicates redaction/generalization, UI must display it clearly and avoid “reconstructing” detail.
- UI must not cache or log sensitive payloads in a way that bypasses policy (client telemetry must respect governance rules).

### Quality signals

- Citation completeness (story nodes render without missing/invalid citation tokens).
- Focus bundle integrity (required fields present, ids link to provenance references).
- Layer registry validation passes (where schema is adopted).

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- UI should treat STAC identifiers as the primary handle for spatial/temporal evidence where present.
- If the API returns STAC Item/Collection IDs (or resolvable references), `_lib` should provide formatting + linking helpers.

### DCAT

- DCAT dataset/distribution records (if exposed via API) should be surfaced in audit panels as “dataset provenance.”

### PROV-O

- Where Focus Mode returns PROV bundle references, UI should present a clear lineage summary:
  - “Where did this come from?”
  - “What process generated it?”
  - “What was the source evidence?”

### Versioning

- When API contracts or schemas change, update `_lib` adapters and treat it as a contract change (semver mindset).

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| UI routes/components | Render map + narrative | Internal UI props/state |
| `_lib` | Shared helpers; enforce invariants; reduce duplication | Imports from UI code |
| API boundary | Serve contracted content; enforce redaction | REST/GraphQL contracts |
| Graph | Store semantic relationships | Accessed only via API |
| Catalogs (STAC/DCAT/PROV) | Evidence + provenance | Exposed via API (preferred) |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| API contracts | `src/server/contracts/` | Semver + contract tests |
| UI schemas | `schemas/ui/` (**not confirmed in repo**) | Semver + schema validation |
| Story Node schema/template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Semver + validation |
| Markdown protocol | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Semver + changelog |

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is required when changes in `_lib`:
- enable a new UI layer or interaction that could reveal sensitive locations by zoom/overlay,
- alter how redaction/generalization is displayed (risk of re-identification),
- change citation/provenance behavior in a way that could allow unsourced narrative display.

(**Approval roles not confirmed in repo** — follow `docs/governance/ROOT_GOVERNANCE.md`.)

### CARE / sovereignty considerations

- Treat culturally sensitive knowledge and sovereignty-controlled information as high-risk by default.
- Prefer aggregation/generalization in UI for public surfaces when sensitive layers are in play.
- Never “infer” restricted locations in UI code or client-side helpers.

### AI usage constraints

- Allowed: summarization/structure extraction for documentation; keyword indexing.
- Prohibited: generating new policy; inferring sensitive locations; fabricating narrative.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---:|---|---|
| v1.0.0 | 2025-12-25 | Initial README for `web/src/app/_lib` conventions + invariants | TBD |

---

## Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- v13 blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API Contract Extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---

