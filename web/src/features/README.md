---
title: "KFM Web UI — Feature Modules"
path: "web/src/features/README.md"
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

doc_uuid: "urn:kfm:doc:web:features:readme:v1.0.0"
semantic_document_id: "kfm-web-features-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:features:readme:v1.0.0"
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
This directory contains **feature-oriented modules** for the KFM web application (the canonical UI home is `web/`). Feature modules package UI, state, and API-adapter logic around a single user-facing capability (e.g., “Focus Mode”, “Map Layers”, “Search”, “Timeline”), while enforcing KFM’s core invariants:

- **UI → API only** (no direct graph access)
- **Provenance-first UX** (citations and source audit always visible)
- **Contract-first integration** (UI schemas + API contracts are canonical)

### Scope

| In Scope | Out of Scope |
|---|---|
| Code under `web/src/features/**` | Global app shell (routing/bootstrap), shared UI kit, build tooling (lives elsewhere in `web/`) |
| Feature-specific components, hooks, services/adapters, tests | Server implementation details (`src/server/**`) |
| Feature integration rules for Focus Mode, citations, layer registry, and governance | Authoring Story Nodes (belongs under `docs/reports/story_nodes/**`) |

### Audience
- Primary: UI contributors working in `web/` (React/Map UI, narrative UX)
- Secondary: API maintainers and story curators who need predictable UI integration points

### Definitions (link to glossary)
- Link: `../../../docs/glossary.md` (**not confirmed in repo**; follow repo canonical glossary if different)
- Terms used: **Feature module**, **Layer registry**, **Focus Mode**, **Story Node**, **Context bundle**, **Provenance panel**, **UI schema**

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master guide | `../../../docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical pipeline + invariants |
| Redesign blueprint v13 | `../../../docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture maintainers | “UI→API only”, minimum contract set, CI gates |
| Implementation guide (PDF) | *(repo location not confirmed)* | Dev maintainers | UI architecture patterns (React/MapLibre, Focus Mode flow) |
| Story Node template | `../../../docs/templates/TEMPLATE__STORY_NODE_V3.md` | Story maintainers | Narrative + citation requirements |
| UI schemas | `../../../schemas/ui/**` (**may be placeholder in early v13**) | Schema maintainers | Validates layer registry + UI contracts |
| API contracts | `../../../src/server/contracts/**` | API maintainers | The only supported boundary to graph/data |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] “Feature module” boundaries and invariants are explicit
- [ ] Expected directory layout documented (with examples)
- [ ] Validation + CI expectations listed (UI + contract checks)
- [ ] Governance / CARE considerations included

## 🗂️ Directory Layout

### This document
- `path`: `web/src/features/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI (canonical home) | `web/` | Web application runtime (map + narrative UX) |
| API boundary (canonical home) | `src/server/` | REST/GraphQL services + redaction + contract tests |
| UI schema contracts | `schemas/ui/` | Layer registry schemas + UI validation |
| Story Nodes (canonical home) | `docs/reports/story_nodes/` | Draft/published narratives + assets |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Evidence products + provenance bundles |

### Recommended feature module structure

> This is the **recommended** layout for each feature directory. Exact filenames/framework choices are **not confirmed in repo**; treat this as a contract-friendly pattern that keeps UI testable and bounded.

~~~text
📁 web/
└── 📁 src/
    └── 📁 features/
        ├── 📁 <feature-name>/               # kebab-case (recommended)
        │   ├── 📁 components/               # UI components (feature-scoped)
        │   ├── 📁 hooks/                    # feature-scoped hooks
        │   ├── 📁 services/                 # API adapters + parsing + redaction-safe helpers
        │   ├── 📁 state/                    # reducers/stores (if used)
        │   ├── 📁 __tests__/                # unit/integration tests for this feature
        │   ├── 📄 index.(ts|js)             # public surface (barrel export)
        │   └── 📄 README.md                 # optional: feature-local notes
        └── 📄 README.md                     # (this file)
~~~

#### Rules of thumb
- **Feature internals stay internal.** Other features should only import from `features/<feature-name>/index.*` (public surface).
- **Network calls belong in `services/`.** Components should not “reach into” APIs directly; they consume typed/validated adapters.
- **Cross-feature/shared utilities** belong outside `features/` (e.g., `web/src/shared/` or `web/src/lib/`) (**not confirmed in repo**). Avoid creating ad-hoc “shared” folders inside a single feature.

## 🧭 Context

### Background
KFM’s canonical system flow is:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

`web/src/features/` sits in the **UI** stage and must preserve downstream rules: UI never bypasses contracts, and narrative UX must remain evidence-linked.

### Architecture assumptions (UI)
The intended UI is a React-based SPA under `web/` with a map engine (MapLibre GL JS) and optional 3D support (Cesium). The UI loads map layers from a **layer registry** (JSON config) and provides a governed “Focus Mode” experience that fetches a **context bundle** via the API and renders narrative + citations + provenance affordances.  
(**Some details may vary by implementation; treat these as the target architecture.**)

### Constraints / invariants (non‑negotiables)
1. **No UI direct-to-graph reads**  
   - `web/` must never query Neo4j directly; all graph access is via `src/server/`.

2. **No unsourced narrative**  
   - Published Story Nodes must be provenance-linked and validate (front-matter, citations, entity refs, redaction compliance).

3. **Contracts are canonical**  
   - Schemas live in `schemas/` and API contracts under `src/server/contracts/` and must validate in CI.

4. **Data outputs are not code**  
   - Derived datasets belong under `data/**`, not under `src/` or `web/`.

5. **Focus Mode is provenance-only**  
   - Focus Mode consumes only provenance-linked content. Predictive/AI content is opt-in, labeled, and includes uncertainty metadata.

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Layer registry | JSON | `web/**/layers/**` (or legacy `web/cesium/layers/*.json`) | `schemas/ui/**` (schema validation) |
| Focus Mode context bundle | JSON | `src/server/` Focus API | API contract tests + UI runtime checks |
| Story Nodes | Markdown | `docs/reports/story_nodes/**` | Story Node schema + citation rules |
| Evidence identifiers | IDs/refs | STAC/DCAT/PROV outputs | Must remain stable + traceable |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Rendered map + narrative UI | Web runtime | `web/` | UI a11y + provenance affordances |
| UI telemetry (optional) | JSON/logs | `docs/telemetry/` (**not confirmed**) | `schemas/telemetry/**` |

### Sensitivity & redaction
- Treat any layer or content marked **sensitive/restricted** as requiring:
  - reduced precision / generalized geometry,
  - API-level redaction as the source of truth,
  - UI affordances that avoid “zoom-to-exact” leaks (e.g., clamp zoom, blur locations, or hide toggles).

### Quality signals
- Feature renders are deterministic for a fixed input payload (testable)
- Citations render correctly and link back to evidence identifiers
- Layer toggles reflect the registry and sensitivity rules
- Focus Mode always provides a provenance/sources view

## 🌐 STAC, DCAT & PROV Alignment

Even though UI code does not *produce* STAC/DCAT/PROV, features must **surface and preserve** these identifiers:

- When showing narrative claims, the UI should provide a **Sources** view that lists cited documents/datasets (STAC items, DCAT datasets, PROV activities where available).
- When showing map markers or derived facts, the UI should expose “why/where from” via tooltips, side panels, or provenance drawers.

## 🧱 Architecture

### Components (pipeline context)

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Accessed **only** via API layer |
| APIs | Serve contracts + redaction | REST/GraphQL (`src/server/`) |
| UI | Map + narrative | API calls + UI schemas (`web/`) |
| Story Nodes | Curated narrative | Markdown templates + validators |
| Focus Mode | Contextual synthesis | Provenance-linked context bundle |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API contracts | `src/server/contracts/` | Contract tests required |
| UI layer registry | `web/**/layers/**` | Schema-validated (`schemas/ui/`) |
| Story Node template | `docs/templates/` | Template versions pinned |

## 🗺️ Diagrams

### Target system flow (UI in context)
~~~mermaid
flowchart LR
  A[ETL<br/>src/pipelines] --> B[Catalogs<br/>data/stac + data/catalog/dcat + data/prov]
  B --> C[Graph<br/>Neo4j]
  C --> D[API<br/>src/server]
  D --> E[UI Features<br/>web/src/features]
  E --> F[Story Nodes<br/>docs/reports/story_nodes]
  F --> G[Focus Mode<br/>feature module]
~~~

### Focus Mode sequence (feature-to-API boundary)
~~~mermaid
sequenceDiagram
  participant User
  participant UI as UI Feature (web)
  participant API as API (src/server)
  participant Graph as Graph (Neo4j)

  User->>UI: select entity / story link
  UI->>API: Focus query(entity_id, optional time_window)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: context bundle
  API-->>UI: narrative + citations + audit flags
  UI-->>User: render story + sources + map/timeline focus
~~~

## 🧠 Story Node & Focus Mode Integration

### How features surface in Focus Mode
Feature modules that render Focus Mode must:
- Render narrative text **with citations** (and refuse/flag missing citations in published content).
- Provide an “audit/provenance” panel and/or “Sources” drawer for traceability.
- Synchronize map + timeline to Story Node metadata (e.g., `focus_center`, `focus_time`, `focus_layers`) when present.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.
- Any predictive/AI content must be explicitly labeled, opt-in, and carry uncertainty metadata.

### Optional structured controls (Story Node front-matter example)
~~~yaml
# Example only — see TEMPLATE__STORY_NODE_V3.md for the canonical schema
focus_layers:
  - "trail_segments:primary"
focus_time: "1861-01-01/1865-12-31"
focus_center: [-98.0000, 38.0000]
~~~

## 🧪 Validation & CI/CD

### Validation steps (expected)
- [ ] UI lint + typecheck (if TypeScript is used)
- [ ] Unit tests for feature logic and rendering
- [ ] Integration tests for Focus Mode rendering (citations, provenance UI)
- [ ] E2E smoke tests for critical flows (map → focus mode → sources)
- [ ] UI schema checks (layer registry validates against `schemas/ui/`)
- [ ] Repo lint: forbid patterns like direct DB calls from `web/` code

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) install deps
# 2) run unit tests
# 3) run e2e tests (optional)
# 4) validate UI schemas (layer registry)
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| ui.focusmode.open | UI | `docs/telemetry/` + `schemas/telemetry/` (**not confirmed**) |
| ui.layer.toggle | UI | `docs/telemetry/` + `schemas/telemetry/` (**not confirmed**) |

## ⚖ FAIR+CARE & Governance

### Governance review triggers
- Adding a **new layer** that could reveal sensitive locations by interaction/zoom
- Adding or changing **AI narrative behaviors**
- Adding new **public-facing endpoints** (requires API review + contract tests)
- Downgrading sensitivity/classification for any surfaced content

### CARE / sovereignty considerations
- If a feature can expose culturally sensitive knowledge or restricted locations:
  - prefer coarse/aggregate public products,
  - ensure redaction is applied at the API boundary,
  - document handling decisions in governance notes.

### AI usage constraints
- Allowed: summarization, structure extraction, translation, keyword indexing (as governed)
- Prohibited: generating new policy; inferring sensitive locations (directly or indirectly)
- Human review required for any sensitivity or governance label changes

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-25 | Initial `web/src/features` README scaffold | TBD |

---

## Footer refs (do not remove)
- Master guide: `../../../docs/MASTER_GUIDE_v12.md`
- Template: `../../../docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Redesign blueprint: `../../../docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Governance: `../../../docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `../../../docs/governance/SOVEREIGNTY.md`
- Ethics: `../../../docs/governance/ETHICS.md`
