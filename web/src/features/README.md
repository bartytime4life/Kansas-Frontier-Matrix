---
title: "KFM Web UI — Feature Modules"
path: "web/src/features/README.md"
version: "v1.0.1"
last_updated: "2025-12-28"
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

doc_uuid: "urn:kfm:doc:web:features:readme:v1.0.1"
semantic_document_id: "kfm-web-features-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:web:features:readme:v1.0.1"
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

# KFM Web UI — Feature Modules

## 📘 Overview

### Purpose
- Define the canonical conventions for feature modules under `web/src/features/` in the KFM Web UI.
- Encode the UI-side “do not break” rules: **UI → API only**, **provenance-first UX**, and **contract-first integration** across schemas + APIs.

### Scope

| In Scope | Out of Scope |
|---|---|
| Feature-oriented modules under `web/src/features/**` (components, hooks, state, API adapters, tests) | Global app shell/bootstrap (routing, providers), shared UI kit, build tooling (lives elsewhere in `web/`) |
| Feature integration rules for Focus Mode, citations, provenance drawers, layer registry usage | Server implementation details (`src/server/**`) and graph internals (`src/graph/**`) |
| UI validation expectations (a11y, schema checks, contract compatibility) | Authoring Story Nodes (belongs under `docs/reports/story_nodes/**`) |

### Audience
- Primary: UI contributors working in `web/` (React + MapLibre/Cesium, narrative UX)
- Secondary: API maintainers and story curators who need predictable UI integration points

### Definitions (link to glossary)
- Link: `docs/glossary.md` (expected per v13 blueprint; **not confirmed in repo**)  
  - Relative from this file: `../../../docs/glossary.md`
- Terms used in this doc:
  - **Feature module** — bounded UI capability (Map Layers, Search, Timeline, Focus Mode, etc.) packaged with its UI + state + adapters.
  - **Layer registry** — declarative layer config consumed by the UI; schema-validated (`schemas/ui/`).
  - **Context bundle** — API-delivered payload that includes narrative + evidence/provenance references used by Focus Mode.
  - **Provenance panel / Sources drawer** — UI affordance that exposes “why/where from” (STAC/DCAT/PROV IDs and links).
  - **Focus Mode** — provenance-only view for deep exploration of a story/entity.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master guide (pipeline + invariants) | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Pipeline ordering + subsystem contracts |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Governs this README structure |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Story maintainers | Narrative + citations + Focus Mode surfacing |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API maintainers | REST/GraphQL contract change workflow |
| v13 redesign blueprint (draft) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture maintainers | Contract-first, evidence-first, UI→API only |
| UI schemas | `schemas/ui/**` | Schema maintainers | Layer registry + UI contract validation |
| API contracts | `src/server/contracts/**` | API maintainers | The only supported boundary to graph/data |
| Story Nodes | `docs/reports/story_nodes/**` | Story maintainers | Draft/published split if defined |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Feature-module boundaries and invariants are explicit (UI→API only, provenance-only Focus Mode)
- [ ] Expected directory layout documented (file tree + import rules)
- [ ] Validation + CI expectations listed (UI, schema, contract checks)
- [ ] Governance / CARE considerations included (sensitivity, redaction, AI constraints)

## 🗂️ Directory Layout

### This document
- `path`: `web/src/features/README.md` *(must match front-matter)*

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed + catalog outputs (STAC/DCAT/PROV) |
| Documentation | `docs/` | Canonical governed docs (guides, designs, domain notes) |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) |
| Pipelines | `src/pipelines/` | ETL + catalog generation code |
| Graph | `src/graph/` | Ontology bindings + graph build/migrations |
| API boundary | `src/server/` | API service + contracts + redaction/generalization |
| UI | `web/` | React + map client + Focus Mode UI |
| MCP runs/experiments | `mcp/` | Runs, experiments, model cards, SOPs (if present) |
| Tests | `tests/` | Cross-cutting tests |
| Tools | `tools/` | Validators, QA scripts |
| CI | `.github/` | Workflows + policy gates |

### Expected file tree for this sub-area
~~~text
📁 web/
└── 📁 src/
    ├── 📁 features/
    │   ├── 📄 README.md
    │   ├── 📁 <feature-name>/                    # kebab-case recommended
    │   │   ├── 📁 components/                    # feature-scoped UI components
    │   │   ├── 📁 hooks/                         # feature-scoped hooks
    │   │   ├── 📁 services/                      # API adapters + parsing + validation
    │   │   ├── 📁 state/                         # feature-scoped state (if used)
    │   │   ├── 📁 __tests__/                     # feature unit/integration tests
    │   │   ├── 📄 index.(ts|js)                  # public surface (barrel export)
    │   │   └── 📄 README.md                      # optional: feature-local notes
    │   └── 📁 <another-feature-name>/
    └── 📁 <app-shell-and-shared-areas>           # routing/providers/shared libs (not here)
~~~

#### Module boundaries (rules of thumb)
- **Only import a feature through its public surface.**  
  Other features and the app shell should import from `features/<feature-name>/index.*` (avoid deep imports).
- **Network and parsing live in `services/`.**  
  Components render; services adapt API payloads into UI-ready, redaction-safe shapes.
- **No direct reads from the graph or raw data.**  
  `web/` consumes data only through contracted APIs (and catalog endpoints when explicitly exposed via API boundary).
- **Cross-feature reuse belongs outside `features/`.**  
  If a utility/component is used by multiple features, lift it into the repo’s shared UI/lib area (**not confirmed in repo**; commonly `web/src/shared/` or `web/src/lib/`).

## 🧭 Context

### Background
KFM’s canonical system flow is:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

`web/src/features/` is in the **UI stage** and is the primary location where user-facing capabilities are implemented while preserving provenance and contract constraints.

### Assumptions
- The web app is a React-based UI under `web/`, with a 2D map engine (MapLibre) and optional 3D (Cesium) support.
- The UI is configured by a **layer registry** that can be extended without code changes (by editing configuration) (**exact file location not confirmed in repo**).
- Focus Mode is implemented as a dedicated feature state: selecting an entity/story triggers an API request for a **context bundle**, then renders narrative + map/timeline focus + provenance UI.

### Constraints / invariants
- **Pipeline ordering is non-negotiable**: ETL → Catalogs → Graph → API → UI → Story Nodes → Focus Mode.
- **Frontend consumes contracts via APIs**: no direct Neo4j access, no bypassing contract tests.
- **Focus Mode is provenance-only**: no uncited narrative; any AI/predictive content is opt-in, labeled, and includes uncertainty metadata.
- **No hidden data leakage**: respect sensitivity flags; do not “zoom-to-exact” on redacted/generalized content.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Where is the canonical layer registry located in `web/` (and what is the schema entrypoint in `schemas/ui/`)? | UI + Schema maintainers | TBD |
| Where do UI telemetry events live (if used): `docs/telemetry/` vs `mcp/runs/` vs other? | UI + MCP maintainers | TBD |
| Is there a repo glossary at `docs/glossary.md` (as expected by v13 blueprint)? | Docs maintainers | TBD |
| What is the canonical API contract format (OpenAPI vs GraphQL schema) and where is it versioned? | API maintainers | TBD |

### Future extensions
- Extension point (UI): feature-level layer registry additions with provenance pointers + CARE gating.
- Extension point (Story/Focus): richer context bundles (images, excerpts, PROV activity summaries) while preserving redaction.
- Extension point (AI evidence): AI artifacts as evidence (STAC assets) surfaced only with explicit labeling and uncertainty.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL<br/>src/pipelines] --> B[Catalogs<br/>data/stac + data/catalog/dcat + data/prov]
  B --> C[Graph<br/>Neo4j<br/>src/graph]
  C --> D[API boundary<br/>src/server]
  D --> E[UI Features<br/>web/src/features]
  E --> F[Story Nodes<br/>docs/reports/story_nodes]
  F --> G[Focus Mode<br/>provenance-linked only]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant User
  participant UI as UI Feature (web)
  participant API as API boundary (src/server)
  participant Graph as Graph (Neo4j)

  User->>UI: select entity / story link
  UI->>API: Focus query(entity_id, optional time_window)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: context bundle
  API-->>UI: narrative + citations + audit flags
  UI-->>User: render story + sources + map/timeline focus
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Layer registry | JSON | `web/**/layers/**` (or legacy `web/cesium/layers/*.json`) (**not confirmed**) | `schemas/ui/**` schema validation |
| Focus Mode context bundle | JSON | Focus API under `src/server/` | API contract tests + UI runtime guards |
| Story Nodes | Markdown | `docs/reports/story_nodes/**` | Story Node schema + citation rules |
| Evidence identifiers | IDs/refs | STAC/DCAT/PROV outputs | Must be stable + traceable |
| UI schema bundles | JSON Schema | `schemas/ui/**` | CI schema validation |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Rendered map + narrative UI | Web runtime | `web/` | a11y checks + provenance affordances |
| Feature tests | JS/TS test outputs | `web/src/features/**/__tests__/` | CI test runner |
| UI telemetry (optional) | events/logs | `schemas/telemetry/**` + runtime sink (**not confirmed**) | telemetry schema validation |

### Sensitivity & redaction
- Treat any layer or content marked **restricted/sensitive** as requiring:
  - API-level redaction/generalization as the source of truth,
  - UI behaviors that cannot leak precision (clamped zoom, obfuscated coordinates, hidden “zoom-to”),
  - explicit labeling in the UI (e.g., “generalized for safety / sovereignty”).

### Quality signals
- Rendering is deterministic for a fixed input payload (testable snapshots where applicable).
- Citations render and resolve to evidence identifiers (STAC/DCAT/PROV) without broken links.
- Layer toggles match the registry and respect sensitivity flags.
- Focus Mode always provides a provenance/sources view (no “invisible sources”).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: *N/A for UI code generation* (UI consumes cataloged STAC IDs via APIs).
- Items involved: any item/asset references surfaced in Focus Mode and provenance panels.
- Extension(s): as defined by `schemas/stac/**` and KFM profiles (UI must not assume extensions not present).

### DCAT
- Dataset identifiers: surfaced in Sources panels for dataset-level discovery (license, publisher, coverage).
- License mapping: UI must display license/attribution where provided (do not strip).
- Contact / publisher mapping: UI may display for transparency (do not invent).

### PROV-O
- `prov:wasDerivedFrom`: surfaced as lineage links when available (raw → work → processed).
- `prov:wasGeneratedBy`: surfaced as run/activity IDs when available (auditability).
- Activity / Agent identities: surfaced in provenance panels (pipeline run IDs, tools, stewards).

### Versioning
- UI must preserve version identifiers and predecessor/successor links when provided by the API.
- If the API exposes dataset/version selection, the UI must treat selection as part of provenance (e.g., “you are viewing vX of dataset Y”).

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Accessed only via API boundary |
| APIs | Serve contracts + redaction | REST/GraphQL (`src/server/`) |
| UI | Map + narrative | API calls + UI schemas (`web/`) |
| Story Nodes | Curated narrative | Markdown templates + validators |
| Focus Mode | Contextual synthesis | Provenance-linked context bundle |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API contracts | `src/server/contracts/` | Contract tests required; breaking changes require versioning/compat strategy |
| UI layer registry | `web/**/layers/**` | Schema-validated (`schemas/ui/`) |
| Story Node schema + template | `schemas/story_nodes/**` + `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Template/schema versions pinned |
| UI provenance UX contract | `web/` (this README + a11y + audits) | Must not regress “no hidden data leakage” |

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/{raw,work,processed}/`
- [ ] STAC: new collection(s)/item(s) validate against `schemas/stac/`
- [ ] DCAT: dataset/distribution records validate against `schemas/dcat/`
- [ ] PROV: activity + agent identifiers recorded under `data/prov/`
- [ ] Graph: new labels/relations mapped + migration plan (stable IDs preserved)
- [ ] APIs: contract version bump + tests + redaction/generalization rules
- [ ] UI: layer registry entry + access rules + a11y checks
- [ ] Focus Mode: provenance references enforced; AI content opt-in + uncertainty metadata
- [ ] Telemetry: new signals + schema version bump (if telemetry is used)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
Feature modules that participate in Focus Mode must:
- Render narrative text **with citations** (and refuse/flag missing citations in published content).
- Provide an “audit/provenance” panel or “Sources” drawer for traceability (STAC/DCAT/PROV IDs).
- Synchronize map + timeline to Story Node metadata (e.g., `focus_center`, `focus_time`, `focus_layers`) when present.
- Support “pivot” navigation: clicking an entity in the narrative can request that entity’s context bundle (without losing provenance).

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.
- Any predictive/AI content must be explicitly labeled, opt-in, and carry uncertainty metadata.
- Never infer or reveal sensitive locations (directly or indirectly).

### Optional structured controls
~~~yaml
# Example only — see TEMPLATE__STORY_NODE_V3.md for the canonical schema
focus_layers:
  - "trail_segments:primary"
focus_time: "1861-01-01/1865-12-31"
focus_center: [-98.0000, 38.0000]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front-matter + required sections)
- [ ] UI lint + typecheck (if TypeScript is used)
- [ ] Unit/integration tests for features (rendering + adapters)
- [ ] Integration tests for Focus Mode (citations, provenance UI, map/time sync)
- [ ] UI schema checks (layer registry validates against `schemas/ui/`)
- [ ] API contract compatibility checks (when upgrading API client/adapters)
- [ ] Security checks (no secrets/PII leakage), sovereignty/sensitivity checks (as applicable)
- [ ] Accessibility (a11y) checks for user-facing flows

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) install deps
# 2) run lint/typecheck
# 3) run unit/integration tests
# 4) validate UI schemas (layer registry)
# 5) run e2e smoke tests (optional)
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| ui.focusmode.open | UI | `schemas/telemetry/**` + runtime sink (**not confirmed**) |
| ui.layer.toggle | UI | `schemas/telemetry/**` + runtime sink (**not confirmed**) |
| ui.sources.open | UI | `schemas/telemetry/**` + runtime sink (**not confirmed**) |

## ⚖ FAIR+CARE & Governance

### Review gates
- Adding a **new layer** that could reveal sensitive locations via interaction/zoom
- Adding or changing **AI narrative behaviors** (especially anything that could be mistaken for fact)
- Adding new **public-facing endpoints** (API review + contract tests required)
- Downgrading sensitivity/classification for any surfaced content

### CARE / sovereignty considerations
- If a feature can expose culturally sensitive knowledge or restricted locations:
  - prefer coarse/aggregate public products,
  - enforce redaction at the API boundary,
  - document handling decisions (and require human review where appropriate).

### AI usage constraints
- Allowed (per front-matter): summarization, structure extraction, translation, keyword indexing
- Prohibited: generating new policy; inferring sensitive locations
- Any AI-derived content surfaced in Focus Mode must be opt-in, labeled, and include uncertainty metadata.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-25 | Initial `web/src/features` README scaffold | TBD |
| v1.0.1 | 2025-12-28 | Aligned to Universal template; strengthened UI→API + Focus Mode provenance gates | TBD |

---

Footer refs:
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
