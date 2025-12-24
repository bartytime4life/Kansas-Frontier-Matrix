---
title: "KFM Web UI Source README"
path: "web/src/README.md"
version: "v1.0.1"
last_updated: "2025-12-24"
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

doc_uuid: "urn:kfm:doc:web:src:readme:v1.0.1"
semantic_document_id: "kfm-web-src-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:web:src:readme:v1.0.1"
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

# KFM Web UI Source README (`web/src/`)

> **Purpose (required):** Provide a contract-first, provenance-first guide for implementing KFM Web UI source code under `web/src/`, without breaking the API boundary, redaction/generalization rules, or Focus Mode provenance requirements.

## 📘 Overview

### Purpose

- Define what belongs in `web/src/` and how frontend work stays architecture-synced to KFM’s canonical pipeline:  
  **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**
- Make frontend invariants explicit:
  - **contract-bound data access** (no direct graph reads),
  - **provenance and citation UX** (audit affordances),
  - **Focus Mode constraints** (provenance-linked only; AI opt-in if present).

### Scope

| In Scope | Out of Scope |
|---|---|
| Runtime UI code under `web/src/` (React components, map UI, state, API clients, Story Node rendering, Focus Mode UX, frontend tests) | ETL/pipelines (`src/pipelines/`), catalog generation (`data/**`), graph ingest (`src/graph/`), server implementation details (`src/server/`), infra/deployments |
| UI layer registry consumption behavior | Authoring Story Nodes themselves (canonical home: `docs/reports/story_nodes/`) |
| UI-side accessibility, performance, and telemetry wiring (if implemented) | Governance policy authoring (see `docs/governance/**`) |

### Audience

- Primary: Frontend engineers working in `web/` and `web/src/`.
- Secondary: API engineers validating UI↔API contracts; story curators validating provenance UX; governance/security reviewers.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo — add or repair link if glossary lives elsewhere)*

Terms used in this doc:
- **API boundary**: contracted server layer under `src/server/` that enforces redaction/generalization and serves governed payloads.
- **Story Node**: a governed narrative artifact (Markdown + assets + citations), canonical home: `docs/reports/story_nodes/`.
- **Focus Mode**: immersive, deep-dive UX that must remain **provenance-linked only**.
- **Provenance**: explicit links/IDs back to STAC/DCAT/PROV identifiers (and/or document IDs) supporting displayed claims.
- **Layer registry**: declarative map layer catalog used by the UI (schema-validated if `schemas/ui/` exists).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Root README | `README.md` | Maintainers | Canonical pipeline + repo navigation |
| Web UI README | `web/README.md` | UI Team | What belongs in `web/` |
| Master Guide v12 (draft) | `docs/MASTER_GUIDE_v12.md` | TBD | System + pipeline source of truth |
| v13 redesign blueprint (draft; if adopted) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | TBD | Canonical homes + readiness gates |
| Story Node Template v3 | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | TBD | Story Node structure + citation rules |
| API contracts | `src/server/contracts/` | TBD | UI must consume contracts; no direct graph reads |
| UI schemas | `schemas/ui/` | TBD | Layer registry validation *(not confirmed in repo)* |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | TBD | Repo Markdown standards *(not confirmed in repo)* |

### Definition of done (for this document)

- [ ] Front-matter complete + valid; `path:` matches file location (`web/src/README.md`)
- [ ] Uses required KFM-MDP section structure (Overview → Directory Layout → Context → …)
- [ ] Any “must/shall” rule stated here is also reflected in the Master Guide, or explicitly marked as **not confirmed in repo**
- [ ] Validation steps are listed and repeatable (commands may be placeholders if tooling is not yet wired)
- [ ] Governance + CARE/sovereignty considerations are explicitly stated for UI changes that may expose data

## 🗂️ Directory Layout

### This document

- `path`: `web/src/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Frontend root | `web/` | Web app root (tooling/config + static assets) |
| Frontend source | `web/src/` | React/map UI source code |
| Layer registry | `web/**/layers/**` | Registry configs for map layers *(location not confirmed in repo)* |
| API boundary | `src/server/` | Redaction/generalization + contracted access |
| API contracts | `src/server/contracts/` | OpenAPI/GraphQL contracts + tests |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published story bundles + assets |
| UI schemas | `schemas/ui/` | UI registry schemas *(not confirmed in repo)* |
| Evidence catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Evidence artifacts referenced via API/UI |
| Governance | `docs/governance/` | Ethics + sovereignty + review gates |

### Expected file tree for this sub-area

> This is a **recommended** shape. Keep it aligned to actual repo layout (update if structure differs).

~~~text
📁 web/
└── 📁 src/
    ├── 📁 app/                      # app shell, routing, providers (not confirmed in repo)
    ├── 📁 api/                      # contract-bound API clients + types (preferred name)
    ├── 📁 features/                 # feature bundles (Focus Mode, Search, Layers)
    ├── 📁 map/                      # MapLibre (2D) adapters; optional 3D wrappers
    ├── 📁 story/                    # Story Node rendering + citation UX
    ├── 📁 ui/                       # shared UI components
    ├── 📁 state/                    # state management (not confirmed in repo)
    ├── 📁 styles/                   # design tokens + globals
    ├── 📁 telemetry/                # optional: event emitters (schema-governed if present)
    ├── 📁 utils/                    # helpers (e.g., citation parsing)
    ├── 📁 test/                     # fixtures + test helpers
    └── 📄 README.md                 # this file
~~~

## 🧭 Context

### Background

`web/src/` is where the KFM user experience is implemented: map interaction, layer toggles, search/navigation, Story Node reading, and Focus Mode deep dives.

Because the UI is downstream of catalogs/graph, it must treat provenance and redaction as first-class constraints, not “nice to have” UI polish.

### Assumptions

- The Web UI is a React-based SPA under `web/` *(framework/build tooling not confirmed in repo)*.
- The UI never reads Neo4j directly; all data is accessed through the API boundary (and/or API-mediated catalog access).
- Story Nodes are rendered in the UI and surfaced through Focus Mode.

### Constraints / invariants

- **Canonical pipeline ordering is preserved:**  
  **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**
- **API boundary is mandatory:**
  - UI must not connect directly to Neo4j or bypass API redaction/generalization.
  - UI should treat API-delivered redaction flags as authoritative.
- **Provenance-first UX:**
  - Focus Mode must only present provenance-linked content.
  - If AI/predictive content is ever displayed, it must be **opt-in**, clearly labeled, and include uncertainty metadata.
- **No sensitive location inference:**
  - Do not reconstruct precise restricted locations from partial data, zoom behavior, or UI composition.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Where is the canonical layer registry stored (`web/**/layers/**`) and what schema validates it? | UI Team | TBD |
| What is the current “Focus bundle” API contract surface (fields, evidence IDs, flags)? | API Team | TBD |
| What is the current test stack (unit + e2e) and command set? | UI Team | TBD |

### Future extensions

- Optional 3D views (if enabled) without breaking 2D map contracts.
- Offline-friendly caching for Story Nodes and layer metadata (governance-safe).
- Expanded accessibility audits (screen-reader map affordances; keyboard-first Focus Mode).

## 🗺️ Diagrams

### UI boundary (non-negotiable)

~~~mermaid
flowchart LR
  A["UI (web/src)"] --> B["API boundary (src/server)"]
  B --> C["Graph (Neo4j via src/graph)"]
  B --> D["Catalog artifacts (STAC/DCAT/PROV in data/**)"]
~~~

### Focus Mode request sequence (typical)

~~~mermaid
sequenceDiagram
  participant UI as Web UI (web/src)
  participant API as API Boundary (src/server)
  participant Graph as Graph + Catalog access

  UI->>API: GET /focus?entity_id=...
  API->>Graph: Fetch context + evidence refs (STAC/DCAT/PROV IDs)
  Graph-->>API: Context bundle + provenance identifiers + redaction flags
  API-->>UI: Contracted payload (narrative + citations + audit flags)
~~~

## 📦 Data & Metadata

### Inputs (to `web/src/`)

| Input | Format | Source | Validation |
|---|---|---|---|
| API responses | JSON | `src/server/` endpoints | Contract tests + UI runtime guards |
| Layer registry | JSON/TS | `web/**/layers/**` | `schemas/ui/` (if present) |
| Story Nodes | Markdown + assets | `docs/reports/story_nodes/**` | Story Node schema + lint (if present) |
| Evidence identifiers | IDs/URLs | STAC/DCAT/PROV artifacts | Broken-link + ID integrity checks *(if tooling exists)* |

### Outputs (from `web/src/` behavior)

| Output | Format | Where | Contract / Schema |
|---|---|---|---|
| Rendered UI | runtime | browser | a11y + contract adherence |
| Build bundle | static build | `web/` build output (repo-specific) | CI build + a11y |
| UI telemetry (optional) | JSON events | repo-specific | `schemas/telemetry/` (if present) |

### Sensitivity & redaction rules (UI obligations)

- Do not log PII or sensitive geo-coordinates in client telemetry.
- Do not “derive” restricted coordinates by combining multiple generalized views.
- Prefer server-provided generalized geometries over client-side simplification.

## 🌐 STAC, DCAT & PROV Alignment

The UI should make provenance **visible and inspectable**, not implicit:

- Features, tooltips, and Focus Mode claims should link back to:
  - **STAC** Item/Collection identifiers (asset-level metadata),
  - **DCAT** dataset identifiers (dataset-level description and licensing),
  - **PROV** activity/run identifiers (lineage: how it was produced).

When the API returns evidence identifiers, the UI should present them in a consistent “Sources / Evidence” affordance (panel, chips, footnotes, etc.).

## 🧱 Architecture

### Components (recommended responsibilities)

| Component | Responsibility | Notes / invariants |
|---|---|---|
| `api/` | Typed, contract-bound requests | No hand-waved fields; prefer generated types *(tooling repo-specific)* |
| `map/` | Map runtime, interaction, layer adapters | Layer behavior comes from registry; avoid hard-coded layer definitions |
| `story/` | Story Node renderer + citations | Citations are audit affordances, not decorative |
| `features/` | Vertical slices (Focus Mode, Search, Layers, Timeline) | Keep dependencies one-way (features use `api/`, `ui/`, `utils/`) |
| `ui/` | Shared components + layout primitives | Keyboard-first; accessible citation UI |
| `telemetry/` | Optional event emitters | Must align to `schemas/telemetry/` if governed |
| `utils/` | Parsing, formatting, guards | Include “redaction-aware” helpers |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| API schemas/contracts | `src/server/contracts/` | Backward compatible or version bump + tests |
| UI schemas | `schemas/ui/` | Semver + schema validation *(if present)* |
| Story Node schema/template | `docs/templates/` (+ `schemas/storynodes/` if present) | Must validate before publish *(schema path not confirmed)* |

### Non-negotiable frontend invariants (enforced by design)

- **API boundary only:** UI must not query Neo4j or internal graph export formats directly.
- **Provenance visible:** any narrative claim rendered in Focus Mode must surface its evidence/citation path.
- **Redaction respected:** if the API indicates generalization/redaction, the UI must not provide controls that defeat it (e.g., “show raw geometry” toggles).
- **Accessibility:** Focus Mode, map controls, and citation affordances must be keyboard accessible and screen-reader friendly.

### Extension points checklist (feature work)

- [ ] UI: add/modify a layer registry entry and validate it (if schema exists)
- [ ] UI: add/modify Story Node renderer and citation handling
- [ ] UI: add or extend Focus Mode UI for a new entity type
- [ ] API: add/extend an endpoint and update contracts (required if UI needs new fields)
- [ ] Security: confirm no leakage from generalized/redacted content
- [ ] Telemetry: add signals + schema version bump (if telemetry is governed)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Entry points: map click → entity drawer → Focus Mode, Story Node deep link, search result selection.
- Focus Mode should load:
  - narrative content (Story Node Markdown),
  - referenced assets (images/audio/video if present),
  - a structured provenance bundle (if provided by the API),
  - sensitivity/redaction flags and UI messaging.

### Provenance-linked narrative rule

- Every displayed factual claim must trace to a dataset / record / asset ID (or a governed document ID).
- Never display AI-generated text as unmarked fact.

### Optional structured controls

These hints may be returned by the API or embedded in Story Node content (template-dependent).

~~~yaml
focus_layers:
  - "TBD:layer_id"
focus_time: "TBD:YYYY or YYYY-MM-DD range"
focus_center: [ -98.0000, 38.0000 ] # lon, lat (example only)
~~~

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- [ ] Frontend lint + type checks *(commands not confirmed in repo)*
- [ ] Unit tests for:
  - citation parsing/rendering,
  - Focus Mode state transitions,
  - layer registry loading/parsing.
- [ ] Contract alignment checks:
  - UI requests match OpenAPI/GraphQL contracts,
  - required provenance fields are present for Focus Mode.
- [ ] UI schema checks for layer registry *(if `schemas/ui/` exists)*
- [ ] Accessibility checks for Focus Mode and citation interactions
- [ ] Security + sovereignty checks for restricted layers and generalization behavior

### Reproduction (placeholders)

~~~bash
# Replace with repo-specific commands from web/package.json

# install dependencies
# (npm|pnpm|yarn) install

# run dev server
# (npm|pnpm|yarn) run dev

# run unit tests
# (npm|pnpm|yarn) test

# lint / typecheck
# (npm|pnpm|yarn) run lint
# (npm|pnpm|yarn) run typecheck

# build
# (npm|pnpm|yarn) run build
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| `focus_mode_entered` | UI | `schemas/telemetry/` + telemetry pipeline *(not confirmed in repo)* |
| `citation_opened` | UI | `schemas/telemetry/` + telemetry pipeline *(not confirmed in repo)* |
| `layer_toggled` | UI | `schemas/telemetry/` + telemetry pipeline *(not confirmed in repo)* |
| `api_error` | UI error boundary | `schemas/telemetry/` + telemetry pipeline *(not confirmed in repo)* |

## ⚖ FAIR+CARE & Governance

### Review gates

UI changes that typically require elevated review:
- adding new layers that could expose sensitive locations (even via interaction/zoom),
- changing redaction/generalization handling,
- adding/altering Story Node rendering that affects provenance visibility,
- adding AI-generated/predictive narrative surfaces visible to users.

### CARE / sovereignty considerations

- Identify communities impacted by new UI features or content surfaces.
- Do not add UI affordances that encourage discovery of restricted or culturally sensitive locations.
- Treat the API boundary as the enforcement point for redaction/generalization; UI must not bypass it.

### AI usage constraints

- This document’s AI prohibitions include:
  - `generate_policy`
  - `infer_sensitive_locations`
- If the UI ever renders AI/predictive content, it must remain opt-in and clearly labeled with uncertainty metadata.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial README for `web/src` | TBD |
| v1.0.1 | 2025-12-24 | Aligned to KFM-MDP required sections; clarified architecture/invariants and added Data/Diagrams sections | TBD |

---

Footer refs (do not remove):
- Root README: `README.md`
- Web UI README: `web/README.md`
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`