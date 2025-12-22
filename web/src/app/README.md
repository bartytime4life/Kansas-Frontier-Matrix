---
title: "KFM Web App — src/app README"
path: "web/src/app/README.md"
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

doc_uuid: "urn:kfm:doc:web:src-app-readme:v1.0.0"
semantic_document_id: "kfm-web-src-app-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:src-app-readme:v1.0.0"
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

# KFM Web App — web/src/app

## 📘 Overview

### Purpose

- Define what belongs in `web/src/app/` (the application composition layer for the KFM web UI).
- Encode the UI’s non-negotiable contracts with adjacent pipeline stages (API boundary, Story Nodes, Focus Mode).
- Provide a contribution guide for adding routes/views, wiring Focus Mode, and rendering provenance/citations safely.

### Scope

| In Scope | Out of Scope |
|---|---|
| Application shell composition (routes/views/layout), cross-route providers, UI orchestration for map + narrative panels, Focus Mode view/state wiring, story-node rendering expectations, provenance/citation UI patterns, UI-side layer registry consumption | ETL/catalog/graph implementation, API query/business logic, ontology design, story node authoring itself, schema authoring, CI/workflow configuration, secrets/infra |

### Audience

- Primary: Frontend engineers working under `web/`
- Secondary: API engineers validating contracts consumed by UI; curators/authors verifying Story Node and Focus Mode presentation

### Definitions (link to glossary)

- Link: `../../../docs/glossary.md` (relative from this folder; may differ in your repo viewer)
- Terms used in this doc: Focus Mode, Story Node, Context Bundle, Provenance, Citation Rendering, Redaction/Generalization, Layer Registry

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `../../../docs/MASTER_GUIDE_v12.md` | KFM maintainers | Canonical pipeline order + invariants |
| Redesign Blueprint v13 | `../../../docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | KFM maintainers | Canonical homes by stage; v13 readiness checklist |
| Story Node Template v3 | `../../../docs/templates/TEMPLATE__STORY_NODE_V3.md` | KFM maintainers | Story node structure + optional focus controls |
| Universal Doc Template | `../../../docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM maintainers | Govered doc structure used here |
| API contracts | `../../../src/server/contracts/` | API team | OpenAPI/GraphQL contracts; contract tests required |
| UI layer registry schema | `../../../schemas/ui/` | Web team | Schema for layer registry validation (not confirmed in repo) |
| UI layer registry config | `../../../web/**/layers/**` | Web team | Canonical location pattern; exact files vary (not confirmed in repo) |
| Story Nodes | `../../../docs/reports/story_nodes/` | Curators | Published nodes consumed by UI feeds |
| Telemetry schemas | `../../../schemas/telemetry/` | Platform | Optional; used if UI emits governed telemetry |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] `path` matches repository location: `web/src/app/README.md`
- [ ] UI invariants are stated (API boundary, provenance rules, redaction expectations)
- [ ] File tree and contribution expectations are documented
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `web/src/app/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI root | `web/` | Map layers, Focus Mode UX, citation rendering |
| UI app composition | `web/src/app/` | App-level routes/views/layout + providers (this folder) |
| API boundary | `src/server/` | Contracted access layer; redaction/generalization enforcement |
| API contracts | `src/server/contracts/` | OpenAPI/GraphQL contracts and versions |
| Graph | `src/graph/` | Graph build + ontology bindings (UI never queries this directly) |
| Story Nodes | `docs/reports/story_nodes/` | Curated narratives with provenance; validate before publish |
| Schemas | `schemas/` | STAC/DCAT/PROV/storynodes/ui/telemetry schemas |
| Security docs | `.github/SECURITY.md` + `docs/security/` | Policy + technical standards (not confirmed in repo) |

### Expected file tree for this sub-area

~~~text
📁 web/
└── 📁 src/
    └── 📁 app/
        ├── 📄 README.md
        ├── 📁 <routes-or-views>/            # framework-specific route/view structure (not confirmed in repo)
        ├── 📁 components/                   # app-shell components (shell, panels, navigation)
        ├── 📁 providers/                    # context providers (auth/theme/data/state)
        ├── 📁 hooks/                        # app-scoped hooks (focus, layer toggles, timeline sync)
        ├── 📁 lib/                          # app-scoped utilities (API client wrappers, formatters)
        └── 📁 styles/                       # app-scoped styles (tokens, globals, route styles)
~~~

> If your framework does not use file-based routing, treat `<routes-or-views>/` as the app’s view modules and keep navigation wiring here.

## 🧭 Context

### Background

KFM’s web UI is the user-facing stage of the governed pipeline: it renders maps/timelines and narrative artifacts while preserving provenance and sovereignty constraints. `web/src/app/` is expected to hold the “composition layer” that binds together:

- Map UI + layer toggles (driven by a layer registry contract where used)
- Story Node rendering (Markdown + citation UX)
- Focus Mode (contextual deep dive driven by an API-provided context bundle)

### Assumptions

- The KFM UI is a React-based “Map UI” housed under `web/` (framework specifics not confirmed in repo).
- Focus Mode is implemented as either:
  - a distinct route/view, or
  - a dedicated UI state within the app shell.
- The UI obtains all graph/catalog content through the API boundary (`src/server/`); no direct Neo4j connectivity from `web/`.

### Constraints / invariants

- **Canonical pipeline order is non-negotiable:** ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- **API boundary is mandatory:** UI reads only from API endpoints and catalog endpoints; the UI never queries the graph directly.
- **Provenance-first UI rule:** Focus Mode and Story Nodes must never display uncited assertions. If a narrative fragment has no evidence link, it must not be shown.
- **AI content is always opt-in and labeled:** any AI-generated or predictive content must be clearly indicated and include uncertainty/confidence metadata; it must not appear as unmarked fact.
- **Redaction/generalization is enforced at the API boundary** and must be respected in UI rendering (do not “reconstruct” redacted values client-side).
- **Layer registries (when used) must be schema-validated** and treated as governed configuration (do not bypass schema by ad-hoc layer definitions in code).
- **Accessibility is a governed requirement** for Focus Mode and narrative UX (keyboard navigation, readable citations, map controls).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What routing/view framework governs `web/src/app/` (file-based routing vs. app-shell router)? | TBD | TBD |
| Where is the canonical layer registry config in this repo instance (if present)? | TBD | TBD |
| Where does the typed API client live (if generated from OpenAPI/GraphQL)? | TBD | TBD |
| What is the expected citation UX (popover, side panel, footnotes) and where is it implemented? | TBD | TBD |

### Future extensions

- A richer “audit/provenance panel” in Focus Mode that surfaces: STAC/DCAT/PROV IDs, graph entity IDs, and policy flags.
- Optional 3D mode toggle (if adopted), without losing Focus state continuity.
- Offline-friendly caching of context bundles for curated experiences (requires governance review).

## 🗺️ Diagrams

### System/dataflow diagram

~~~mermaid
flowchart LR
  A[ETL / Normalization] --> B[STAC/DCAT/PROV]
  B --> C[Neo4j Graph]
  C --> D[API Boundary]
  B --> D
  D --> E[Web UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Focus Mode request flow

~~~mermaid
sequenceDiagram
  participant U as User
  participant UI as Web UI (web/src/app)
  participant API as API Boundary (src/server)
  participant G as Graph/Catalog Sources

  U->>UI: Select entity/story (enter Focus Mode)
  UI->>API: Request context bundle (Focus API)
  API->>G: Fetch related entities + evidence + provenance
  API-->>UI: Context bundle (narrative + structured data + provenance)
  UI-->>U: Render map/timeline + story w/ citations
  U->>UI: Optional "AI Insight" toggle
  UI->>API: Request opt-in AI content (if available)
  API-->>UI: AI content + uncertainty + source list
  UI-->>U: Render AI content clearly labeled
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Focus context bundle | JSON | API boundary (`src/server/`) | API contract tests; provenance completeness checks |
| Story node narrative | Markdown | API feed and/or `docs/reports/story_nodes/` pipeline | Story node validation (front-matter, citations, redaction compliance) |
| Layer registry | JSON | `web/**/layers/**` (if present) | Validate against `schemas/ui/` |
| Catalog/provenance metadata | JSON/JSON-LD | API boundary (STAC/DCAT/PROV services) | Schema validation in `schemas/` |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Map + timeline rendering | UI | `web/` runtime | UI a11y + functional tests |
| Focus Mode view/state | UI | `web/src/app/` | Provenance display rules; opt-in AI toggles |
| Citation interactions | UI | `web/src/app/` | Citation syntax support (Story Node format) |
| Optional telemetry | JSON events | `docs/telemetry/` pipelines (if present) | `schemas/telemetry/` (if used) |

### Sensitivity & redaction

- Treat all “sensitive by policy” fields as potentially redacted or generalized.
- UI must render “restricted/redacted” placeholders rather than attempting client-side inference.
- Any new UI element that increases discoverability of restricted locations requires governance review.

### Quality signals

- Story node render must preserve citations; citations must remain clickable/inspectable.
- No broken evidence references (catalog IDs, provenance IDs, entity IDs) in Focus Mode.
- Layer registry loads without schema violations (if registry pattern exists).
- Focus Mode never shows uncited narrative by default.

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Collections involved: via API-provided STAC collections/items as needed
- Items involved: referenced by Story Nodes and/or Focus bundles
- Extension(s): project-specific STAC profile (see `schemas/stac/` if present)

### DCAT

- Dataset identifiers: surfaced via API metadata endpoints
- License mapping: UI displays licensing/attribution where provided
- Contact / publisher mapping: UI surfaces publisher/contact as metadata (when present)

### PROV-O

- `prov:wasDerivedFrom`: rendered as evidence links in audit/provenance UI
- `prov:wasGeneratedBy`: used to show which run/activity produced an evidence artifact
- Activity / Agent identities: display in provenance panel where available

### Versioning

- UI should treat identifiers as stable and versioned.
- When the API reports predecessor/successor relationships, UI should present “this artifact was superseded” cues rather than silently swapping.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Cypher behind API boundary |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Graph + docs |
| Focus Mode | Contextual synthesis | Provenance-linked |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API contracts | `src/server/contracts/` | Contract tests required |
| Story node schema | `schemas/storynodes/` | Semver + validation gates |
| Layer registry schema | `schemas/ui/` | Semver + validation gates |
| Layer registry config | `web/**/layers/**` | Schema-validated; additive changes should be backward compatible |

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

- Focusable units: Story Nodes and graph entities (Place, Person, Event, Organization, Document, Artifact) as supported by API bundles.
- Evidence UI expectations:
  - Every claim has a citation/evidence affordance.
  - Users can pivot from cited entity mentions to entity focus views without losing provenance context.

### Provenance-linked narrative rule

- Every claim must trace to a dataset / record / asset ID.
- If a narrative fragment lacks a source link, it must not be rendered in Focus Mode.

### Optional structured controls

Story Nodes may include optional focus hints that the UI can apply (exact embedding/transport is implementation-specific).

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV/storynodes/ui/telemetry)
- [ ] API contract tests
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)
- [ ] Accessibility checks (as applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate schemas
# 2) run unit/integration tests
# 3) run doc lint
# 4) run accessibility checks
~~~

### Telemetry signals (if applicable)

- UI emits governed telemetry only if a schema exists under `schemas/telemetry/`.
- Telemetry must not contain secrets, raw PII, or disallowed sensitive locations.

## ⚖ FAIR+CARE & Governance

### Review gates

Changes in `web/src/app/` require additional review when they:

- Add a new layer toggle or change how layers are discoverable (risk: sensitive layer exposure).
- Modify citation/provenance presentation (risk: uncited narrative or broken audit UX).
- Introduce or expand AI-generated content presentation (risk: uncited/uncalibrated claims).
- Change Focus Mode entry/exit flows affecting what content is shown by default.

### Sensitive content handling

- Follow sovereignty policies for culturally sensitive knowledge.
- Ensure restricted locations are generalized/redacted at the API boundary and presented as such in UI.
- Any UI feature that increases inference potential around protected sites requires human review.

### Accessibility

- Focus Mode, story panels, citations, and map controls must remain keyboard accessible.
- Citation affordances must be readable and operable for screen readers (no “icon-only” citations).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for `web/src/app` | TBD |

