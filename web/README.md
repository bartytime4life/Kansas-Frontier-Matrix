---
title: "Kansas Frontier Matrix — Web UI (web/)"
path: "web/README.md"
version: "v1.0.1"
last_updated: "2025-12-24"
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

doc_uuid: "urn:kfm:doc:web:readme:v1.0.1"
semantic_document_id: "kfm-web-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:web:readme:v1.0.1"
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

# Kansas Frontier Matrix Web UI

`web/` is the canonical home for KFM’s user-facing **map + narrative UI**, downstream of the governed pipeline.

**Canonical pipeline ordering (non‑negotiable):**  
**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

## 🚦 Start here

If you are new to KFM UI work, read in this order:

1) `README.md` (repo root) — overall repo navigation and pipeline invariants  
2) `docs/MASTER_GUIDE_v12.md` — canonical pipeline + invariants  
3) `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` — contract-first + canonical homes  
4) `src/server/contracts/` — API contracts the UI must consume (if present)  
5) `schemas/ui/` — UI registry schemas (layer registry validation) (if present)  
6) `docs/reports/story_nodes/` — Story Nodes rendered in Focus Mode

> If any path is missing, treat it as **not confirmed in repo** and update references accordingly.

## 📘 Overview

### Purpose

- Define what belongs in `web/` and how the Web UI participates in the canonical KFM pipeline.
- Make UI invariants explicit:
  - **API boundary**
  - **provenance visibility**
  - **Focus Mode “no uncited content by default” rule**
  - **layer registry validation**

### Scope

| In Scope | Out of Scope |
|---|---|
| Web application code under `web/` (map, timeline, Story Node rendering, Focus Mode UI state) | ETL/pipelines (`src/pipelines/`) |
| UI layer registries + UI-specific schemas/validation hooks | Catalog generation outputs (`data/stac/`, `data/catalog/dcat/`, `data/prov/`) |
| UI-side contract consumption (API clients, request/response typing) | Graph build/migrations (`src/graph/`) |
| UI testing, accessibility, performance budgets, and UI telemetry (if implemented) | API contract definition and enforcement (`src/server/`) |

### Audience

- Primary: frontend engineers working in `web/`.
- Secondary: API engineers validating UI→API contracts; curators working on Story Nodes; reviewers for governance/a11y.

### Definitions

- Glossary: `docs/glossary.md` *(not confirmed in repo — add or repair link if the glossary lives elsewhere)*
- Terms used in this doc:
  - **Story Node** — governed narrative artifact rendered in the UI and used by Focus Mode.
  - **Focus Mode** — immersive deep-dive view restricted to provenance-linked content only.
  - **Layer registry** — schema-validated configuration describing map layers, sources, attribution, and sensitivity flags.
  - **Evidence artifacts** — STAC/DCAT/PROV products referenced by the UI for traceability and audit.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline ordering + invariants |
| Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | TBD | Canonical homes + v13 readiness rules |
| Story Node Template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | TBD | Required structure for published Story Nodes |
| API Contracts | `src/server/contracts/` | TBD | UI must consume contracts; no direct graph reads |
| UI schemas | `schemas/ui/` | TBD | Layer registry schema validation lives here |
| Layer registries | `web/**/layers/**` | TBD | Target location pattern; concrete subpath is repo-specific |
| Story Nodes | `docs/reports/story_nodes/` | TBD | Published narrative content rendered in UI |

### Definition of done

- [ ] Front-matter complete + valid
- [ ] Directory layout and invariants match current repo reality
- [ ] UI invariants are explicit (API boundary, provenance visibility, Focus Mode rules)
- [ ] Validation steps listed and repeatable (commands may be placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `web/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Domain outputs; catalogs and provenance produced upstream |
| Catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Evidence artifacts for traceability |
| Graph | `src/graph/` + `data/graph/` | Ontology + ingest + import artifacts |
| API boundary | `src/server/` | Contracted access, redaction, provenance linking |
| API contracts | `src/server/contracts/` | Contract artifacts the UI consumes |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts consumed by UI |
| Schemas | `schemas/` | JSON schemas for catalogs, Story Nodes, UI registries |
| Web UI | `web/` | This directory |

### Expected file tree

> This is a **target / typical** layout. If your actual tree differs, update this section (and avoid duplicating canonical homes).

~~~text
📁 web/
├── 📄 README.md
├── 📄 package.json                      # if present (build + dev scripts)
├── 📄 tsconfig.json                     # if present (TypeScript)
├── 📁 public/                           # if present (static assets)
├── 📁 src/                              # if present (UI source)
│   ├── 📁 api/                          # API client + contract bindings
│   ├── 📁 app/                          # routing/state shell (repo-specific)
│   ├── 📁 map/                          # map runtime (MapLibre and/or other)
│   ├── 📁 story/                        # Story Node rendering
│   ├── 📁 focus/                        # Focus Mode UI state + components
│   ├── 📁 layers/                       # runtime layer registry loader (code)
│   ├── 📁 ui/                           # shared UI components
│   └── 📁 telemetry/                    # optional (event emitters)
└── 📁 layers/                           # layer registries (config) — location is repo-specific
~~~

## 🧭 Context

### Background

KFM’s UI is the user-facing map + narrative experience. It is downstream of a governed pipeline:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

### Assumptions

- The Web UI is a single-page application under `web/`. *(not confirmed in repo)*
- The UI consumes all graph, catalog, and provenance information **through API contracts**.
- Focus Mode is a UI mode for deep dives, and provenance is visible/inspectable.

### Constraints and invariants

- **Pipeline ordering is preserved.**
- **API boundary is mandatory:**
  - UI consumes data via API endpoints and catalog endpoints only.
  - UI must not connect to Neo4j directly.
- **Layer registries must be schema-valid** (canonical schema home: `schemas/ui/`).
- **Provenance-first UX is required:**
  - Focus Mode displays only provenance-linked narrative and evidence references.
  - If predictive/AI-generated content is displayed, it must be opt-in and labeled with uncertainty metadata.
- **Client-side reconstruction is forbidden:**
  - Do not “reconstruct” sensitive locations from partial coordinates or inferred joins.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Where is the concrete layer registry directory in this repo (target: `web/**/layers/**`)? | TBD | TBD |
| What is the Focus Mode contract surface (endpoint names, payload shapes) in `src/server/contracts/`? | TBD | TBD |
| How are citations rendered (footnotes vs popovers vs side panel), and what is the accessibility baseline? | TBD | TBD |
| What is the current UI test stack (unit + e2e) and command set? | TBD | TBD |

### Future extensions

- Optional 3D views (if adopted) without breaking 2D contracts.
- Offline-friendly caching for Story Nodes and layer metadata (governance-safe).
- Improved citation UX (keyboard-first provenance browsing, copyable evidence IDs).
- Expanded accessibility audits (Focus Mode semantics, reduced motion, map alternatives).

## 🗺️ Diagrams

### System and dataflow diagram

~~~mermaid
flowchart LR
  A["ETL — src/pipelines"] --> B["STAC/DCAT/PROV — data/stac · data/catalog/dcat · data/prov"]
  B --> C["Graph — src/graph + data/graph"]
  C --> D["API boundary — src/server + contracts"]
  D --> E["UI — web/"]
  E --> F["Story Nodes — docs/reports/story_nodes"]
  F --> G["Focus Mode — provenance-linked only"]
~~~

### Focus Mode request sequence

~~~mermaid
sequenceDiagram
  participant UI as Web UI
  participant API as API Boundary
  participant Graph as Graph + Catalogs

  UI->>API: Focus query(entity_id, options)
  API->>Graph: fetch subgraph + evidence refs (STAC/DCAT/PROV IDs)
  Graph-->>API: context bundle + provenance identifiers
  API-->>UI: contracted payload (narrative + citations + flags)
~~~

## 📦 Data and metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| API responses | JSON | `src/server/` endpoints | Contract tests + runtime guards |
| Layer registry | JSON (or TS) | `web/**/layers/**` | `schemas/ui/` (if present) |
| Story Nodes | Markdown | `docs/reports/story_nodes/**` | Story Node schema + lint |
| Evidence references | IDs/URLs | STAC/DCAT/PROV artifacts | Broken-link + ID integrity checks |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Web bundle | static build | repo-specific build output | CI build + a11y |
| UI telemetry | JSON events | repo-specific | `schemas/telemetry/` (if present) |

### Sensitivity and redaction

- Treat API-delivered redaction/generalization as authoritative.
- Do not log PII or sensitive coordinates in client telemetry.
- Avoid caching sensitive content in persistent client storage unless governance-approved.

### Quality signals

- Contract adherence (no breaking changes without versioning).
- Layer registry schema validation.
- Citation UX correctness (clickable evidence refs, readable provenance panel).
- Accessibility baseline (keyboard navigation, focus management, readable citations).
- Performance budgets (tile/layer load, Focus Mode time-to-interactive).

## 🌐 STAC, DCAT and PROV alignment

The UI should make provenance **visible and inspectable**, not implicit:

- Map features and Focus Mode narrative must link back to:
  - STAC Item/Collection identifiers,
  - DCAT dataset identifiers,
  - PROV activity/run identifiers.

If a UI view lacks evidence identifiers, it must present that as a **missing provenance** state rather than implying certainty.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| API client | Typed calls to API contracts | REST/GraphQL (repo-specific) |
| Map runtime | Render layers + interactions | Layer registry + API data |
| Story Node renderer | Render narrative + citations | Story Node v3 structure |
| Focus Mode | Deep-dive view + provenance/audit panel | Focus “context bundle” payload |
| Layer registry loader | Load/validate layer configs | `schemas/ui/` |

### Interfaces and contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog (if adopted) |
| API contracts | `src/server/contracts/` | Contract tests required |
| Story Node schema/template | `schemas/storynodes/` + `docs/templates/` | Must validate before publish |
| Layer registry schema | `schemas/ui/` | Must validate before UI build |

### Extension points checklist

- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + sensitivity flags + attribution
- [ ] Focus Mode: provenance references enforced and visible
- [ ] A11y: keyboard and screen-reader acceptance criteria updated
- [ ] Telemetry: signals schema versioned (if telemetry is enabled)

## 🧠 Story Node and Focus Mode integration

### Focus Mode behavior expectations

Focus Mode is a UI state where the user views a story or entity in detail:

- Enter Focus Mode by entity/story selection.
- Request a Focus context bundle from the API boundary.
- Render:
  - narrative content,
  - explicit citations and evidence identifiers,
  - a provenance/audit panel,
  - map and timeline adjustments that reflect story context.

### Provenance-linked narrative rule

- Every displayed claim must trace to evidence identifiers.
- Never display AI-generated text as unmarked fact.
- Opt-in AI elements must be visibly labeled and include uncertainty metadata.

### Optional structured controls

These fields are typically derived from Story Node metadata and/or the Focus context bundle:

~~~yaml
focus_layers:
  - "TBD:layer_id"
focus_time: "TBD:YYYY or YYYY-MM-DD range"
focus_center: [-98.0000, 38.0000] # lon, lat (example only)
~~~

## 🧪 Validation and CI/CD

### Validation steps

- [ ] Markdown protocol checks (if this README is governed)
- [ ] UI schema checks (layer registry validation)
- [ ] API contract compatibility (UI consumption stays compatible)
- [ ] Unit tests (repo-specific)
- [ ] E2E smoke tests (repo-specific)
- [ ] Security and sovereignty checks (as applicable)

### Local reproduction

~~~bash
# Placeholders — replace with repo-specific commands defined in web/package.json (if present)

# 1) install deps
# 2) run lint
# 3) run unit tests
# 4) run e2e tests
# 5) validate layer registry schema
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| Focus Mode opens | UI | `schemas/telemetry/` + `docs/telemetry/` (if present) |
| Layer load timing | UI | `schemas/telemetry/` + `docs/telemetry/` (if present) |

## ⚖ FAIR+CARE and governance

### Review gates

- UI changes that affect redaction/provenance display require API + governance review.
- UI changes that add/alter Story Node rendering require curator/story owner review.

### CARE and sovereignty considerations

- Identify any community-sensitive knowledge that could be exposed via layers, tooltips, or deep links.
- Enforce “generalize or omit” rules via the API boundary; do not bypass in UI.

### AI usage constraints

If the UI renders predictive/AI-generated content:

- it must be opt-in,
- must show uncertainty/confidence metadata,
- must not appear as unmarked fact.

## 🕰️ Version history

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial `web/README.md` | TBD |
| v1.0.1 | 2025-12-24 | Clarified layer registry contract location pattern; strengthened Focus Mode provenance + audit expectations; aligned directory layout language to v13 canonical homes | TBD |

---

Footer refs:
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`