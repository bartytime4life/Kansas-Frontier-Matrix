---
title: "KFM Web UI Source README"
path: "web/src/README.md"
version: "v1.0.2"
last_updated: "2025-12-27"
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

doc_uuid: "urn:kfm:doc:web:src:readme:v1.0.2"
semantic_document_id: "kfm-web-src-readme-v1.0.2"
event_source_id: "ledger:kfm:doc:web:src:readme:v1.0.2"
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

# KFM Web UI Source README

**Path:** `web/src/`  
**Companion docs:** `web/README.md` (directory-level scope) and `README.md` (repo-level scope).  
**Non-negotiable pipeline ordering:** **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

> **Purpose required:** Provide a contract-first, provenance-first guide for implementing KFM Web UI source code under `web/src/` without breaking the API boundary, redaction and generalization rules, or Focus Mode provenance requirements.

## 📘 Overview

### Purpose

- Define what belongs in `web/src/` and how UI work stays architecture-synced to KFM’s canonical pipeline.
- Make frontend invariants explicit and implementable:
  - contract-bound data access via the API boundary,
  - provenance and citation affordances as first-class UX,
  - Focus Mode rule enforcement, including “no uncited content by default.”

### Scope

| In Scope | Out of Scope |
|---|---|
| React UI source code under `web/src/` including map runtime, Focus Mode UI, Story Node rendering, citations, state, and frontend tests | ETL/pipelines (`src/pipelines/`), catalog generation outputs (`data/**`), graph ingest/migrations (`src/graph/`), server implementation internals (`src/server/`), infra and deployments |
| UI consumption of API contracts and schema-governed registries | Authoring Story Nodes themselves (`docs/reports/story_nodes/`) |
| UI-side accessibility, performance, and telemetry wiring when implemented | Governance policy authoring (`docs/governance/**`) |

### Audience

- Primary: frontend engineers implementing features in `web/src/`.
- Secondary: API engineers validating UI↔API contracts; story curators validating provenance UX; governance and security reviewers.

### Definitions

- Glossary: `docs/glossary.md` — **not confirmed in repo**; repair link if glossary lives elsewhere.

Terms used in this doc:

- **API boundary**: contracted server layer under `src/server/` that enforces redaction/generalization and serves governed payloads.
- **Story Node**: a governed narrative artifact rendered in the UI and used by Focus Mode; canonical home is `docs/reports/story_nodes/`.
- **Focus Mode**: deep-dive UX restricted to provenance-linked narrative and evidence by default.
- **Layer registry**: declarative map layer configuration intended to be schema-validated.
- **Evidence artifacts**: STAC/DCAT/PROV products referenced by the UI for traceability and audit.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Root README | `README.md` | Maintainers | Repo navigation and pipeline invariants |
| Web UI README | `web/README.md` | UI team | Directory-level rules for `web/` |
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | TBD | System + pipeline source of truth |
| v13 Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | TBD | Contract-first design rules and canonical homes |
| Story Node template v3 | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | TBD | Story Node structure and citation rules |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | TBD | Governing structure for this README |
| API contracts | `src/server/contracts/` | TBD | Canonical contract artifacts consumed by UI |
| UI schemas | `schemas/ui/` | TBD | Layer registry schema validation; **not confirmed in repo** |
| Story Nodes | `docs/reports/story_nodes/` | TBD | Published narrative content rendered in UI |

### Definition of done

- [ ] Front-matter is complete and `path:` matches `web/src/README.md`.
- [ ] Uses governed section structure per Universal template.
- [ ] All “must/shall” statements are either traceable to existing governed docs or explicitly marked **not confirmed in repo**.
- [ ] Validation steps are listed and reproducible.
- [ ] Governance, CARE, and sovereignty considerations are explicitly stated for UI changes that could expose sensitive data.

### Start here

If you are implementing or changing UI behavior in `web/src/`, read in this order:

1) `README.md` (repo root)  
2) `docs/MASTER_GUIDE_v12.md`  
3) `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`  
4) `web/README.md`  
5) `src/server/contracts/` (if present)  
6) `docs/reports/story_nodes/` and `docs/templates/TEMPLATE__STORY_NODE_V3.md`

If a path is missing, treat it as **not confirmed in repo** and do not hard-code assumptions into the UI.

## 🗂️ Directory Layout

### This document

- `path`: `web/src/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Frontend root | `web/` | Web app root: tooling, public assets, build config |
| Frontend source | `web/src/` | UI source code and tests |
| Layer registries | `web/**/layers/**` | Layer registry configs; exact location is repo-specific |
| API boundary | `src/server/` | Redaction/generalization + contracted access |
| API contracts | `src/server/contracts/` | OpenAPI/GraphQL contracts and contract tests |
| Story Nodes | `docs/reports/story_nodes/` | Draft and published story bundles and assets |
| UI schemas | `schemas/ui/` | Layer registry schemas; **not confirmed in repo** |
| Evidence catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Evidence artifacts referenced via API and UI |
| Governance | `docs/governance/` | Ethics, sovereignty, review gates |

### Expected file tree for this sub-area

This is a recommended shape. Update it to match the actual repo and avoid creating duplicate “canonical homes.”

~~~text
📁 web/
├── 📄 README.md
└── 📁 src/
    ├── 📁 api/                      # API clients + contract-bound types
    ├── 📁 map/                      # Map runtime adapters (MapLibre and optional 3D wrappers)
    ├── 📁 layers/                   # Registry loader + validation hooks
    ├── 📁 focus/                    # Focus Mode UI shell + provenance panel
    ├── 📁 story/                    # Story Node renderer + citation UI
    ├── 📁 features/                 # Vertical feature slices (Search, Timeline, Layers)
    ├── 📁 ui/                       # Shared components
    ├── 📁 state/                    # State management
    ├── 📁 styles/                   # Tokens + global styles
    ├── 📁 telemetry/                # Optional: event emitters
    ├── 📁 utils/                    # Guards, formatters, evidence helpers
    ├── 📁 test/                     # Fixtures + test helpers
    └── 📄 README.md                 # this file
~~~

## 🧭 Context

### Background

`web/src/` implements the user-facing KFM map and narrative experience. Because the UI sits downstream of catalogs and graph, it must treat provenance, sensitivity, and contract adherence as functional requirements, not optional polish.

### Assumptions

- UI is a React-based web application under `web/` with map clients, potentially MapLibre and optional 3D. If your repo differs, update this doc.
- The UI never reads Neo4j directly. The API boundary is the enforcement point for redaction and generalization.
- Focus Mode is a first-class UX that surfaces provenance and restricts uncited content by default.

### Constraints and invariants

- Pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.
- API boundary is mandatory:
  - UI consumes data through contracted endpoints and API-mediated catalog access.
  - UI must not connect to Neo4j or bypass server redaction/generalization.
- Contracts are canonical:
  - UI does not “guess” field shapes or silently accept breaking changes.
  - If the UI needs new fields, the correct workflow is contract update → API implementation → UI consumption.
- Provenance-first UX:
  - Focus Mode surfaces evidence identifiers and shows missing provenance states explicitly.
  - Narrative claims shown in Focus Mode must be provenance-linked.
- No sensitive location inference:
  - Do not reconstruct restricted locations through client-side joins, zoom behavior, “centroid guessing,” or caching artifacts.
- Redaction is authoritative:
  - If the API indicates redaction/generalization, the UI must not provide a control path that defeats it.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Where is the layer registry stored and what schema validates it | UI | TBD |
| What is the Focus bundle contract surface and required provenance fields | API | TBD |
| What is the current frontend test stack and command set | UI | TBD |
| How are citations rendered and what is the accessibility baseline for citation UX | UI | TBD |

### Future extensions

- Optional 3D views without breaking 2D contracts.
- Offline-safe caching of Story Nodes and layer metadata with governance-approved storage rules.
- Improved provenance browsing UX with keyboard-first citation navigation and copyable evidence IDs.

## 🗺️ Diagrams

### System and dataflow diagram

~~~mermaid
flowchart LR
  A["ETL — src/pipelines"] --> B["STAC/DCAT/PROV — data/stac · data/catalog/dcat · data/prov"]
  B --> C["Graph — src/graph + Neo4j ingest"]
  C --> D["API boundary — src/server + contracts"]
  D --> E["UI — web/src"]
  E --> F["Story Nodes — docs/reports/story_nodes"]
  F --> G["Focus Mode — provenance-linked by default"]
~~~

### Focus Mode request sequence

~~~mermaid
sequenceDiagram
  participant UI as Web UI
  participant API as API Boundary
  participant Graph as Graph + Catalog access

  UI->>API: Focus query(entity_id, options)
  API->>Graph: fetch context + evidence refs
  Graph-->>API: context bundle + provenance identifiers + redaction flags
  API-->>UI: contracted payload (narrative + citations + audit flags)
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| API responses | JSON | `src/server/` endpoints | Contract tests + UI runtime guards |
| Layer registry configs | JSON or TS | `web/**/layers/**` | `schemas/ui/` schema validation if present |
| Story Nodes | Markdown + assets | `docs/reports/story_nodes/**` | Story Node template conformance and lint if present |
| Evidence identifiers | IDs and links | STAC/DCAT/PROV artifacts | Integrity checks and link checks if tooling exists |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Browser UI | runtime | browser | a11y + contract adherence |
| Build bundle | static output | repo-specific | CI build gate + a11y gates |
| Telemetry events | JSON | repo-specific | `schemas/telemetry/` if present |

### Sensitivity and redaction

- Treat API-delivered redaction and generalization as authoritative.
- Do not log PII or sensitive coordinates in client telemetry.
- Avoid persistent storage of sensitive content unless governance-approved.

### Quality signals

- Contract adherence and explicit error handling for contract mismatches.
- Layer registry validation and attribution completeness.
- Provenance UX correctness and discoverability in Focus Mode.
- Accessibility baseline for map controls, Focus Mode, and citation interactions.
- Performance budgets for layer load, Focus bundle fetch, and Story Node render.

## 🌐 STAC, DCAT & PROV Alignment

The UI makes provenance visible and inspectable:

- **STAC**: asset-level identifiers that describe spatial and temporal artifacts.
- **DCAT**: dataset-level identifiers for discovery, license, publisher, and distributions.
- **PROV-O**: activity and agent identifiers that capture lineage across transformations.

UI obligations:

- When the API returns evidence identifiers, present them as an explicit “Sources” affordance, not hidden metadata.
- When evidence identifiers are missing, show a missing-provenance state rather than implying certainty.
- Keep evidence identifiers copyable and consistent across map tooltips, entity drawers, and Focus Mode.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| API client | Typed calls to API contracts | REST or GraphQL defined by `src/server/contracts/` |
| Map runtime | Render layers and interactions | Layer registry + API-provided data |
| Layer registry loader | Load and validate layer configs | `schemas/ui/` if present |
| Story renderer | Render Story Nodes and citations | Story Node v3 structure |
| Focus Mode | Deep-dive view with provenance panel | Focus context bundle payload |
| Shared UI | Reusable components | Accessibility-first components |
| Telemetry | Optional event emitters | `schemas/telemetry/` if present |

### Interfaces and contracts

| Contract | Location | Versioning rule |
|---|---|---|
| API contracts | `src/server/contracts/` | Semver and contract tests for breaking changes |
| JSON schemas | `schemas/` | Semver and schema validation |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Template updates require curator review |
| UI schemas | `schemas/ui/` | Schema validation required if present |

### Extension points checklist

- [ ] APIs: contract update, version bump if needed, tests updated
- [ ] UI: feature implementation in `web/src/` using contract-bound clients
- [ ] UI: layer registry entry added or updated with attribution and sensitivity flags
- [ ] Focus Mode: provenance display enforced and audit UX verified
- [ ] Story Nodes: references and citations validate against template rules
- [ ] A11y: keyboard navigation and citation UX acceptance criteria updated
- [ ] Telemetry: signals added and schema versioned if governed

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

Focus Mode is a UI state where users deep-dive into an entity or story:

- Entry via map selection, search results, Story Node deep links, or entity drawers.
- Focus Mode loads a context bundle via the API boundary.
- The UI renders:
  - narrative content,
  - explicit citations and evidence identifiers,
  - a provenance panel,
  - redaction and sensitivity messaging where applicable.

### Provenance-linked narrative rule

- Every displayed factual claim in Focus Mode must trace to evidence identifiers.
- Never display AI-generated text as unmarked fact.
- Any AI or predictive content must be opt-in, visibly labeled, and include uncertainty metadata.

### Optional structured controls

These hints may be returned by the API or embedded in Story Node content.

~~~yaml
focus_layers:
  - "TBD:layer_id"
focus_time: "TBD:YYYY or YYYY-MM-DD range"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks for governed docs in `web/`.
- [ ] UI lint and type checks as defined in `web/package.json` if present.
- [ ] Unit tests for:
  - citation parsing and rendering,
  - Focus Mode state transitions,
  - layer registry loading and validation behavior.
- [ ] Contract alignment checks against `src/server/contracts/`.
- [ ] Accessibility checks for Focus Mode and citation interactions.
- [ ] Security and sovereignty checks to prevent leakage of sensitive locations and PII.
- [ ] Optional forbidden pattern checks to prevent direct graph access from `web/`.

### Reproduction

Replace these placeholders with your repo’s actual scripts.

~~~bash
# install dependencies
# (npm|pnpm|yarn) install

# dev server
# (npm|pnpm|yarn) run dev

# lint and typecheck
# (npm|pnpm|yarn) run lint
# (npm|pnpm|yarn) run typecheck

# unit tests
# (npm|pnpm|yarn) test

# build
# (npm|pnpm|yarn) run build
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| `focus_mode_entered` | UI | telemetry pipeline and schemas if present |
| `citation_opened` | UI | telemetry pipeline and schemas if present |
| `layer_toggled` | UI | telemetry pipeline and schemas if present |
| `api_error` | UI error boundary | telemetry pipeline and schemas if present |

## ⚖ FAIR+CARE & Governance

### Review gates

UI changes that typically require elevated review:

- Adding a new layer that could reveal sensitive locations by interaction or zoom.
- Changing redaction or generalization handling.
- Changing citation or provenance display behavior in Focus Mode.
- Adding AI-generated or predictive narrative surfaces visible to users.

### CARE and sovereignty considerations

- Identify communities impacted by new UI surfaces that expose location-bearing data.
- Do not add UI affordances that encourage discovery of restricted or culturally sensitive locations.
- Treat the API boundary as the enforcement point for redaction and generalization; UI must not bypass it.

### AI usage constraints

- Allowed AI transforms for this document: summarization, structure extraction, translation, keyword indexing.
- Prohibited: generating policy or inferring sensitive locations.
- If the UI renders predictive or AI-generated content, it must be opt-in and clearly labeled with uncertainty metadata.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial README for `web/src` | TBD |
| v1.0.1 | 2025-12-24 | Aligned to governed section structure and clarified invariants | TBD |
| v1.0.2 | 2025-12-27 | Tightened contract-first workflow, provenance UX requirements, and validation gates; removed parenthetical headers for protocol consistency | TBD |

---

Footer refs:
- Root README: `README.md`
- Web UI README: `web/README.md`
- Master guide: `docs/MASTER_GUIDE_v12.md`
- v13 blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
