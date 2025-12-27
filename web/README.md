---
title: "Kansas Frontier Matrix — Web UI"
path: "web/README.md"
version: "v1.1.0"
last_updated: "2025-12-27"
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

doc_uuid: "urn:kfm:doc:web:readme:v1.1.0"
semantic_document_id: "kfm-web-readme-v1.1.0"
event_source_id: "ledger:kfm:doc:web:readme:v1.1.0"
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

`web/` is the canonical home for KFM’s **user-facing map + narrative UI** (React/Map UI), including **Focus Mode** experiences.

**Canonical pipeline ordering (non‑negotiable):**  
**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

**UI non‑negotiables (v13-forward):**
- **API boundary is mandatory:** the UI consumes graph + catalog content **only** via API endpoints and catalog endpoints (no direct Neo4j/graph access).  
- **Layer registries are contract artifacts:** layer registries must validate against `schemas/ui/`.  
- **Focus Mode is provenance-only:** Focus Mode must only surface provenance-linked content; AI/predictive content must be opt-in and clearly labeled with uncertainty metadata.  
- **No client-side reconstruction of sensitive locations:** do not infer or re-join partial coordinates to reveal restricted sites; treat API redaction/generalization as authoritative.

If any referenced path is missing, treat it as **not confirmed in repo** and update this README to match the repo’s canonical homes (avoid creating “mystery duplicates”).

## 📘 Overview

### Purpose

- Define what belongs in `web/` and how the Web UI participates in the canonical KFM pipeline.
- Make UI invariants explicit and testable:
  - **API boundary**
  - **provenance visibility**
  - **Focus Mode provenance-only rule**
  - **layer registry schema validation**

### Scope

| In Scope | Out of Scope |
|---|---|
| Front-end application code under `web/` (map runtime, timelines, Story Node rendering, Focus Mode UI state) | ETL/pipelines (`src/pipelines/`) |
| UI layer registries + UI-specific schemas/validation hooks | Catalog generation outputs (`data/stac/`, `data/catalog/dcat/`, `data/prov/`) |
| UI-side contract consumption (API clients, request/response typing, caching policy) | Graph build/migrations (`src/graph/`) |
| UI testing, accessibility, performance budgets, and UI telemetry hooks (if implemented) | API contract definition/enforcement (`src/server/`) |

### Audience

- Primary: frontend engineers working in `web/`.
- Secondary: API engineers validating UI→API contracts; curators working on Story Nodes; reviewers for governance/a11y.

### Start here

If you are new to KFM UI work, read in this order:

1) Repo root `README.md` — repo navigation + canonical roots *(not confirmed in repo in this export)*  
2) `docs/MASTER_GUIDE_v12.md` — canonical pipeline + invariants  
3) `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` — contract-first + canonical homes  
4) `src/server/contracts/` — API contracts the UI must consume *(if present)*  
5) `schemas/ui/` — UI layer registry schemas *(if present)*  
6) `docs/reports/story_nodes/` — Story Nodes rendered in Focus Mode *(if present)*

### Quickstart (repo-specific)

Commands and tooling are repo-specific. Prefer `web/package.json` scripts if present.

~~~bash
# Placeholders — replace with repo-approved tooling.

# cd web
# <install deps>         # e.g., npm ci / pnpm i / yarn
# <run dev server>       # e.g., npm run dev
# <run unit tests>       # e.g., npm test
# <run e2e tests>        # e.g., npm run e2e
# <validate registries>  # schema validation for layer registries (if wired)
~~~

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo — add or repair link if glossary lives elsewhere)*
- Terms used in this doc:
  - **Story Node** — governed narrative artifact rendered in the UI and used by Focus Mode.
  - **Focus Mode** — immersive deep-dive view restricted to provenance-linked content.
  - **Layer registry** — schema-validated configuration describing map layers, sources, attribution, and sensitivity flags.
  - **Evidence artifacts** — STAC/DCAT/PROV products referenced by the UI for traceability and audit.
  - **Focus context bundle** — the contracted API response that packages narrative + evidence references + flags for Focus Mode.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline ordering + invariants |
| Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | TBD | Canonical homes + v13 readiness rules |
| Story Node Template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | TBD | Required structure for published Story Nodes |
| API Contracts | `src/server/contracts/` | TBD | UI must consume contracts; no direct graph reads |
| UI schemas | `schemas/ui/` | TBD | Layer registry schema validation lives here |
| Layer registries | `web/**/layers/**` | TBD | Canonical location pattern for UI registries |
| Story Nodes | `docs/reports/story_nodes/` | TBD | Published narrative content rendered in UI |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (path matches, governance refs included)
- [ ] Uses approved governed headings and fencing (outer backticks, inner tildes)
- [ ] UI invariants explicit (API boundary, provenance visibility, Focus Mode rules)
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
| Schemas | `schemas/` | JSON schemas for catalogs, Story Nodes, UI registries |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts consumed by UI |
| Web UI | `web/` | This directory |

### Expected file tree for this sub-area

This is a **target / typical** layout. Update it if the repo differs.

~~~text
📁 web/
├── 📄 README.md
├── 📄 package.json                      # if present (build + dev scripts)
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
└── 📁 layers/                           # layer registries (config) — canonical pattern: web/**/layers/**
~~~

## 🧭 Context

### Background

KFM’s UI is the user-facing map + narrative experience. It is downstream of a governed pipeline:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

The UI is not where “truth is manufactured.” It is where **contracts are consumed** and **provenance is made legible**.

### Assumptions

- The Web UI is a single-page application under `web/`. *(not confirmed in repo)*
- The UI consumes all graph, catalog, and provenance information **through API contracts** and/or catalog endpoints.
- Focus Mode is implemented as a UI state that renders a contracted context bundle.

### Constraints and invariants

- **Pipeline ordering is preserved.**
- **API boundary is mandatory:**
  - UI consumes data via API endpoints and catalog endpoints only.
  - UI must not connect to Neo4j directly.
- **Layer registries must be schema-valid** (canonical schema home: `schemas/ui/`).
- **Provenance-first UX is required:**
  - Focus Mode surfaces only provenance-linked narrative and evidence references.
  - If predictive/AI-generated content is displayed, it must be opt-in and labeled with uncertainty metadata.
- **Client-side reconstruction is forbidden:**
  - Do not reconstruct sensitive locations from partial coordinates, inferred joins, or zoom interactions.
- **Safety in rendering:**
  - Treat Story Node markdown as untrusted input; sanitize and prevent XSS-style injection.

### Extension Matrix mindset (when UI work is required)

From the Master Guide’s extension framing: adding a capability often touches multiple stages.

- New dataset → UI changes are **optional** (unless you want it visible on the map).
- New evidence/analysis product → UI changes are often **required** to surface it responsibly.
- New narrative node type → UI/Focus changes are often **required**.

Keep changes vertical-slice aware: avoid UI-only features that lack catalog/provenance references or API support.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Where is the concrete layer registry directory in this repo (target: `web/**/layers/**`)? | TBD | TBD |
| What is the Focus Mode contract surface (endpoint names, payload shapes) in `src/server/contracts/`? | TBD | TBD |
| How are citations rendered (footnotes vs popovers vs side panel), and what is the accessibility baseline? | TBD | TBD |
| What is the current UI test stack (unit + e2e) and command set? | TBD | TBD |

### Future extensions

- Optional 3D views (e.g., Cesium) without breaking 2D contracts.
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

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| API responses | JSON | `src/server/` endpoints | Contract tests + runtime guards |
| Catalog endpoints | JSON | STAC/DCAT/PROV outputs | Schema validation + link integrity |
| Layer registry | JSON/TS | `web/**/layers/**` | Validate against `schemas/ui/` |
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

### Layer registry guidance (conceptual)

When integrating new domain data into the UI, the expected pattern is:

1) Ensure the data exists upstream with STAC/DCAT/PROV lineage and an API surface.
2) Register the layer in the UI’s layer registry (often JSON config or TS definition).
3) Validate the registry entry against `schemas/ui/`.
4) Ensure layer UX surfaces:
   - attribution + license,
   - description from metadata,
   - sensitivity flags and any redaction notice,
   - provenance pointers (evidence IDs or resolvable references).

## 🌐 STAC, DCAT & PROV Alignment

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

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as “machine-ingestible storytelling”

- Story Nodes are governed Markdown artifacts consumed by the UI.
- Story Nodes should link to:
  - graph entity IDs,
  - STAC/DCAT/PROV evidence IDs,
  - local assets with attribution.

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

### Optional Focus Mode controls

These controls may be provided by Story Node metadata and/or the Focus context bundle:

~~~yaml
focus_layers:
  - "TBD:layer_id"
focus_time: "TBD:YYYY or YYYY-MM-DD/YYYY-MM-DD"
focus_center: [-98.0000, 38.0000] # lon, lat (example only)
~~~

### Citation rendering expectations (UI)

- Citations should be navigable by keyboard and screen readers.
- Evidence identifiers should be copyable.
- The UI should provide a consistent “audit panel” affordance for:
  - provenance links,
  - sensitivity/redaction notices,
  - missing provenance warnings.

## 🧪 Validation & CI/CD

### CI behavior contract

- **Validate if present:** if a canonical root exists (or changes), validate its artifacts.
- **Fail if invalid:** schema errors, missing links, or orphan references fail deterministically.
- **Skip if not applicable:** optional roots absent → skip without failing the overall pipeline.

### Validation steps

- [ ] Markdown protocol checks (for governed docs)
- [ ] UI schema checks (layer registry validation)
- [ ] API contract compatibility (UI consumption stays compatible)
- [ ] Unit tests (repo-specific)
- [ ] E2E smoke tests (repo-specific)
- [ ] Accessibility checks (keyboard navigation, reduced motion, readable citations)
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

### Telemetry signals (optional)

| Signal | Source | Where recorded |
|---|---|---|
| focus_mode_opened | UI | `schemas/telemetry/` + `docs/telemetry/` (if present) |
| layer_load_timing | UI | `schemas/telemetry/` + `docs/telemetry/` (if present) |
| focus_mode_redaction_notice_shown | UI | `schemas/telemetry/` + `docs/telemetry/` (if present) |

## ⚖ FAIR+CARE & Governance

### Review gates

UI changes that typically require elevated review:

- Adding new sensitive layers (restricted locations, cultural knowledge, PII, etc.)
- Introducing/changing AI-generated narrative behavior visible to users
- Adding new external data sources (as surfaced in UI)
- Adding new public-facing endpoints or sharing links

### CARE / sovereignty considerations

- Identify communities impacted and protection rules.
- Use generalization/redaction for restricted locations (enforced at the API boundary).
- Ensure sensitive assets (images/docs) follow review gates before publication.

### AI usage constraints

If the UI renders predictive/AI-generated content:

- it must be opt-in,
- must show uncertainty/confidence metadata,
- must not appear as unmarked fact,
- must not be used to infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial `web/README.md` | TBD |
| v1.0.1 | 2025-12-24 | Clarified layer registry contract location pattern; strengthened Focus Mode provenance + audit expectations; aligned directory layout language to v13 canonical homes | TBD |
| v1.1.0 | 2025-12-27 | Rewritten to conform to Universal governed-doc headings; tightened v13 UI invariants (API-only, registry schema validation, provenance-only Focus Mode); added quickstart, CI behavior contract, and integration checklists | TBD |

---

Footer refs (do not remove):
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal doc template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
