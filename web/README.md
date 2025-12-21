---
title: "Kansas Frontier Matrix — Web UI (web/)"
path: "web/README.md"
version: "v1.0.0"
last_updated: "2025-12-21"
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

doc_uuid: "urn:kfm:doc:web:readme:v1.0.0"
semantic_document_id: "kfm-web-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:readme:v1.0.0"
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

# Kansas Frontier Matrix — Web UI (`web/`)

## 📘 Overview

### Purpose

- Define what belongs in `web/` and how the Web UI participates in the canonical KFM pipeline.
- Make UI invariants explicit (API boundary, provenance, Focus Mode rules, layer registry validation).

### Scope

| In Scope | Out of Scope |
|---|---|
| Web application code under `web/` (map, timeline, Story Nodes, Focus Mode) | ETL/pipelines (`src/pipelines/`) |
| UI layer registries + UI-specific schemas/validation hooks | Catalog generation (`data/stac/`, `data/catalog/dcat/`, `data/prov/`) |
| UI-side contract consumption (API clients, request/response typing) | Graph build/migrations (`src/graph/`) |
| UI testing, a11y, performance budgets, and UI telemetry (if implemented) | API contract definition and enforcement (`src/server/`) |

### Audience

- Primary: Frontend engineers working in `web/`.
- Secondary: API engineers validating UI→API contracts; curators working on Story Nodes; reviewers for governance/a11y.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Story Node** — narrative artifact rendered in the UI and used by Focus Mode.
  - **Focus Mode** — immersive deep-dive view restricted to provenance-linked content.
  - **Layer registry** — JSON (or equivalent) configuration describing map layers, sources, attributions, and sensitivity flags.
  - **Evidence artifacts** — STAC/DCAT/PROV products referenced by the UI for traceability.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM Core Team | Canonical pipeline ordering + invariants |
| Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture Team | Canonical homes + v13 readiness rules |
| Story Node Template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Story Team | Required structure for published Story Nodes |
| API Contracts | `src/server/contracts/` | API Team | UI must consume contracts; no direct graph reads |
| UI schemas | `schemas/ui/` | UI + Schemas owners | Layer registry validation lives here (if present) |
| Story Nodes | `docs/reports/story_nodes/` | Curators | Published narrative content rendered in UI |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Directory layout and invariants match current repo reality (update the “Expected file tree” section if structure changes)
- [ ] UI invariants are explicit (API boundary, provenance visibility, Focus Mode rules)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `web/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed outputs by domain |
| Catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Evidence artifacts for traceability |
| Graph | `src/graph/` + `data/graph/` | Ontology + ingest + import artifacts |
| API boundary | `src/server/` | Contracted access, redaction, provenance linking |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts consumed by UI |
| Schemas | `schemas/` | JSON schemas for catalogs, Story Nodes, UI registries |
| Web UI | `web/` | This directory |

### Expected file tree for this sub-area

> This is a **target/typical** layout. If your actual tree differs, keep this section updated.

~~~text
📁 web/
├── 📄 README.md
├── 📄 package.json                # if present (build + dev scripts)
├── 📄 tsconfig.json               # if present (TypeScript)
├── 📁 public/                     # if present (static assets)
├── 📁 src/                        # if present (UI source)
│   ├── 📁 api/                    # API client + contract bindings
│   ├── 📁 map/                    # Map runtime (MapLibre / optional 3D)
│   ├── 📁 story/                  # Story Node rendering + Focus Mode UI
│   ├── 📁 ui/                     # shared UI components
│   └── 📁 telemetry/              # optional (event schemas + emitters)
└── 📁 layers/                     # layer registries (schema-validated) — exact location is repo-specific
~~~

## 🧭 Context

### Background

KFM’s UI is the user-facing map + narrative experience. It is downstream of a governed pipeline:
ETL → STAC/DCAT/PROV catalogs → graph → APIs → UI → Story Nodes → Focus Mode.

### Assumptions

- The Web UI is a single-page application (SPA) under `web/`.
- The Web UI **never reads Neo4j directly**. It consumes graph/cat/provenance through API contracts.
- The UI renders Story Nodes and provides a Focus Mode view for deep dives, with provenance visible.

### Constraints / invariants

- **Pipeline ordering is preserved**: ETL → catalogs → graph → APIs → UI → Story Nodes → Focus Mode.
- **API boundary is mandatory**:
  - UI consumes all graph and catalog content via API endpoints and catalog endpoints.
  - Redaction/generalization rules are enforced at the API layer.
- **Provenance-first UX**:
  - Focus Mode displays only provenance-linked narrative.
  - If any predictive/AI-generated content is displayed, it must be opt-in and labeled with uncertainty.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Where is the canonical layer registry stored in this repo (`web/**/layers/**`)? | UI Team | TBD |
| What is the current API contract surface for map layers + Focus Mode bundles? | API Team | TBD |
| What is the current test stack (unit + e2e) and command set? | UI Team | TBD |

### Future extensions

- Optional 3D views (if enabled) without breaking 2D map contracts.
- Offline-friendly caching for Story Nodes and layer metadata (governance-safe).
- Expanded accessibility audits (screen-reader maps, keyboard-first Focus Mode).

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
graph LR
  A["ETL"] --> B["STAC / DCAT / PROV Catalogs"];
  B --> C["Neo4j Graph"];
  C --> D["APIs / Contracts"];
  D --> E["Web UI (web/)"];
  E --> F["Story Nodes"];
  F --> G["Focus Mode"];
~~~


### Optional: Focus Mode request sequence

~~~mermaid
sequenceDiagram
  participant UI as Web UI
  participant API as API Boundary
  participant Graph as Graph (Neo4j + catalogs)

  UI->>API: GET /focus?entity_id=...
  API->>Graph: Fetch subgraph + evidence refs (STAC/DCAT/PROV IDs)
  Graph-->>API: Context bundle + provenance identifiers
  API-->>UI: Contracted payload (narrative + citations + flags)
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| API responses | JSON | `src/server/` endpoints | Contract tests + runtime guards |
| Layer registry | JSON | `web/**/layers/**` | `schemas/ui/` (if present) |
| Story Nodes | Markdown | `docs/reports/story_nodes/**` | Story Node schema + lint |
| Evidence links | IDs/URLs | STAC/DCAT/PROV artifacts | Broken-link + ID integrity checks |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Web bundle | static build | `web/` build output (repo-specific) | CI build + a11y |
| UI telemetry (optional) | JSON events | repo-specific | `schemas/telemetry/` (if present) |

### Sensitivity & redaction

- Do not “reconstruct” sensitive locations client-side from partial data.
- Respect API-delivered redaction/generalization; treat it as authoritative.
- Avoid logging PII or sensitive geo-coordinates in client telemetry.

### Quality signals

- Contract adherence (no breaking changes without versioning).
- Layer registry schema validation.
- a11y checks (keyboard nav, focus management, readable citations).
- Performance budgets (tile/layer load, Focus Mode time-to-interactive).

## 🌐 STAC, DCAT & PROV Alignment

The UI should make provenance **visible and inspectable**, not implicit:

- Map features and Story Nodes link back to:
  - STAC Item/Collection identifiers (what data/asset is being shown),
  - DCAT dataset identifiers (dataset-level description and licensing),
  - PROV activity/run identifiers (how the data was produced).

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| API client | Typed calls to API contracts | REST/GraphQL (repo-specific) |
| Map runtime | Render layers + handle interaction | Layer registry + API data |
| Story Node renderer | Render narrative + citations | Story Node v3 structure |
| Focus Mode | Deep-dive view + provenance sidebar | “focus bundle” payload |
| Layer registry loader | Load/validate layer configs | `schemas/ui/` |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/contracts/` | Contract tests required |
| Story Node schema/template | `schemas/storynodes/` + `docs/templates/` | Must validate before publish |
| Layer registry schema | `schemas/ui/` | Must validate before UI build |

### Extension points checklist (for future work)

- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Focusable targets (examples): a Story Node, Place, Person, Event, Organization.
- Focus Mode payload should include:
  - narrative content,
  - explicit citations / evidence identifiers,
  - sensitivity/redaction flags,
  - optional “includePredictions” or “opt-in AI” fields (if supported).

### Provenance-linked narrative rule

- Every displayed claim must trace to a dataset / record / asset ID.
- Never display AI-generated text as unmarked fact.

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD:layer_id"
focus_time: "TBD:YYYY or YYYY-MM-DD range"
focus_center: [ -98.0000, 38.0000 ] # lon, lat (example only)
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (if README is governed by KFM-MDP checks)
- [ ] UI schema checks (layer registry validation)
- [ ] API contract tests (UI consumption stays compatible)
- [ ] Unit/integration tests (repo-specific)
- [ ] e2e smoke tests (repo-specific)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) install deps
# 2) run lint
# 3) run unit tests
# 4) run e2e tests
# 5) validate layer registry schema
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| Focus Mode opens | UI | `schemas/telemetry/` + `docs/telemetry/` |
| Layer load timing | UI | `schemas/telemetry/` + `docs/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates

- UI changes that affect redaction/provenance display should be reviewed by API + governance owners.
- UI changes that add/alter Story Node rendering should be reviewed by curators/story owners.

### CARE / sovereignty considerations

- Identify any community-sensitive knowledge that could be exposed via map layers, tooltips, or deep links.
- Enforce “generalize or omit” rules via the API boundary; do not bypass in UI.

### AI usage constraints

- If the UI renders predictive/AI-generated content:
  - it must be opt-in,
  - must show uncertainty/confidence metadata,
  - must not appear as unmarked fact.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial `web/README.md` | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
