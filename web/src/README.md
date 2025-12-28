---
title: "KFM Web UI Source README"
path: "web/src/README.md"
version: "v1.0.3"
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

doc_uuid: "urn:kfm:doc:web:src:readme:v1.0.3"
semantic_document_id: "kfm-web-src-readme-v1.0.3"
event_source_id: "ledger:kfm:doc:web:src:readme:v1.0.3"
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
**Non-negotiable pipeline ordering:** **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

> Purpose: Provide a contract-first, provenance-first guide for implementing KFM Web UI source code under `web/src/` without breaking the API boundary, redaction/generalization rules, or Focus Mode provenance requirements.

## 📘 Overview

### Purpose

- Define what belongs in `web/src/` and how UI work stays architecture-synced to KFM’s canonical pipeline.
- Make frontend invariants explicit and implementable:
  - contract-bound data access via the API boundary,
  - provenance and citation affordances as first-class UX,
  - Focus Mode rule enforcement, including **no unsourced narrative in Focus Mode contexts**.

### Scope

| In Scope | Out of Scope |
|---|---|
| React UI source code under `web/src/` including map runtime, Focus Mode UI, Story Node rendering, citations, state, and frontend tests | ETL/pipelines (`src/pipelines/`), catalog generation outputs (`data/**`), graph ingest/migrations (`src/graph/`), server implementation internals (`src/server/`), infra and deployments |
| UI consumption of API contracts and schema-governed registries (layer registry, Story Node schema, telemetry schema) | Editing catalogs directly from UI code (STAC/DCAT/PROV authoring belongs upstream) |
| UI-side accessibility, performance, and telemetry wiring when implemented | Governance policy authoring (`docs/governance/**`) |
| Contract-safe UI evolution (feature work that respects semver + deprecation rules) | Bypassing the API boundary (direct Neo4j, direct `data/**` reads, or client-side reconstruction of restricted data) |

### Audience

- Primary: frontend engineers implementing features in `web/src/`.
- Secondary: API engineers validating UI↔API contracts; story curators validating provenance UX; governance and security reviewers.

### Definitions

- Glossary: `docs/glossary.md` — if missing or incomplete in your checkout, treat as **not confirmed in repo** and repair links rather than creating an alternate glossary.
- Terms used in this doc:
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
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | Maintainers | System + pipeline source of truth |
| v13 Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Maintainers | Canonical homes, drift fixes, contract-first workflow |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Maintainers | Governing markdown rules; **not confirmed in repo** if absent |
| Story Node template v3 | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Story curators | Story structure + citation requirements |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | Governing structure for this README |
| API Contract Extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API team | Contract-first change workflow |
| API contracts | `src/server/contracts/` | API team | OpenAPI/GraphQL contracts; **not confirmed in repo** if absent |
| UI schemas | `schemas/ui/` | Maintainers | Layer registry schema validation; **not confirmed in repo** if absent |
| Story Node schemas | `schemas/storynodes/` | Maintainers | Story Node validation; **not confirmed in repo** if absent |
| Telemetry schemas | `schemas/telemetry/` | Maintainers | Telemetry schema validation; **not confirmed in repo** if absent |
| Telemetry docs | `docs/telemetry/` | Maintainers | Signal definitions and retention; **not confirmed in repo** if absent |
| Story Nodes | `docs/reports/story_nodes/` | Story curators | Templates + draft/published story bundles + assets |
| Governance | `docs/governance/` | Governance | Ethics, sovereignty, review gates |

### Definition of done

- [ ] Front-matter is complete and `path:` matches `web/src/README.md`.
- [ ] Section structure aligns to `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`.
- [ ] Canonical pipeline ordering matches `docs/MASTER_GUIDE_v12.md`.
- [ ] All “must/shall” statements are traceable to existing governed docs or explicitly marked **not confirmed in repo**.
- [ ] Validation steps are listed and reproducible.
- [ ] Governance, CARE, and sovereignty considerations are explicitly stated for UI changes that could expose sensitive data.

### Start here

If you are implementing or changing UI behavior in `web/src/`, read in this order:

1) `README.md` (repo root)  
2) `docs/MASTER_GUIDE_v12.md`  
3) `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`  
4) `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` (**not confirmed in repo** if absent)  
5) `web/README.md`  
6) `src/server/contracts/` (if present)  
7) `docs/reports/story_nodes/` and `docs/templates/TEMPLATE__STORY_NODE_V3.md`

If a path is missing, treat it as **not confirmed in repo** and do not hard-code assumptions into the UI.

## 🗂️ Directory Layout

### This document

- `path`: `web/src/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Frontend canonical home | `web/` | React/Map UI root: tooling, public assets, build config |
| Frontend source | `web/src/` | UI source code and tests |
| UI design notes | `docs/design/` | UI/UX specs (**not confirmed in repo**) |
| Pipelines | `src/pipelines/` | ETL transforms (upstream) |
| Catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV evidence products |
| Graph | `src/graph/` | Ontology, labels/edges, ingest tooling |
| API boundary canonical home | `src/server/` | Contracted access + redaction/generalization enforcement |
| API contracts | `src/server/contracts/` | OpenAPI/GraphQL contracts + tests (**not confirmed in repo** if absent) |
| Story Nodes canonical home | `docs/reports/story_nodes/` | Templates + draft/published story bundles + assets |
| Schemas | `schemas/` | STAC/DCAT/PROV + Story Nodes + UI + telemetry schemas (**not confirmed in repo** if absent) |
| Telemetry docs | `docs/telemetry/` | Signal definitions (**not confirmed in repo**) |
| Governance | `docs/governance/` | Ethics, sovereignty, review gates |
| MCP runs | `mcp/runs/` | Run logs and artifacts (**not confirmed in repo** if absent) |

### Expected file tree for this sub-area

This is a recommended shape. Update it to match the actual repo and avoid creating duplicate “canonical homes.”

~~~text
📁 web/
├── 📄 README.md
└── 📁 src/
    ├── 📁 api/                      # API clients + contract-bound types (generated or hand-written)
    ├── 📁 map/                      # Map runtime adapters (MapLibre; optional 3D adapters)
    ├── 📁 layers/                   # Registry loader + schema validation hooks
    ├── 📁 focus/                    # Focus Mode UI shell + provenance panel
    ├── 📁 story/                    # Story Node renderer + citation UI
    ├── 📁 features/                 # Vertical feature slices (Search, Timeline, Layers)
    ├── 📁 ui/                       # Shared components
    ├── 📁 state/                    # State management
    ├── 📁 styles/                   # Tokens + global styles
    ├── 📁 telemetry/                # Optional: event emitters + guards
    ├── 📁 utils/                    # Guards, formatters, evidence helpers
    ├── 📁 test/                     # Fixtures + test helpers
    └── 📄 README.md                 # this file
~~~

## 🧭 Context

### Background

`web/src/` implements the user-facing KFM map and narrative experience. The UI visualizes governed data returned by the API layer; it does not store additional authoritative data and must not bypass the pipeline.

Because the UI sits downstream of catalogs and graph, it must treat provenance, sensitivity, and contract adherence as functional requirements, not optional polish.

### Assumptions

- The UI is a React-based web application under `web/` (typically React + MapLibre for 2D; optional Cesium for 3D).
- The UI never reads Neo4j directly. The API boundary is the enforcement point for redaction and generalization.
- Focus Mode is a first-class UX that surfaces provenance and restricts unsourced narrative by default.

### Constraints and invariants

- Pipeline ordering is preserved: **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**.
- Canonical homes are not optional:
  - UI lives under `web/` (avoid adding new UI code under `src/`).
  - API boundary lives under `src/server/`.
  - Story Nodes live under `docs/reports/story_nodes/`.
- API boundary is mandatory:
  - UI consumes data only through contracted endpoints and API-mediated catalog access.
  - UI must not connect to Neo4j or bypass server redaction/generalization.
- Contracts are canonical:
  - UI does not “guess” field shapes or silently accept breaking changes.
  - If the UI needs new fields, the correct workflow is contract update → API implementation → UI consumption.
- Provenance-first UX:
  - Focus Mode surfaces evidence identifiers and shows missing provenance states explicitly.
  - Narrative shown in Focus Mode must be provenance-linked.
- No sensitive location inference:
  - Do not reconstruct restricted locations through client-side joins, zoom behavior, “centroid guessing,” reverse-geocoding, or caching artifacts.
- Classification propagation:
  - UI must not present outputs that are less restrictive than the classifications provided by upstream layers.
  - If the API indicates redaction/generalization, the UI must not provide a control path that defeats it.
- One source of truth:
  - Do not fork schemas or contracts into UI-local copies without governance review; link to canonical `schemas/` or `src/server/contracts/` artifacts instead.
- Drift guardrails (v13 alignment):
  - If both `src/map/` and `web/` exist, treat `web/` as the UI canonical home and avoid introducing new “third homes.”
  - If both `src/api/` and `src/server/` exist, treat `src/server/` as the canonical API boundary and avoid importing server internals into the UI.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Where is the layer registry stored and what schema validates it (`schemas/ui/`?) | UI | TBD |
| What is the Focus Mode context bundle contract surface and required provenance fields | API | TBD |
| What is the current frontend test stack and command set | UI | TBD |
| How are citations rendered and what is the accessibility baseline for citation UX | UI | TBD |
| Where are telemetry event schemas stored and how are events validated (`schemas/telemetry/`?) | Maintainers | TBD |

### Future extensions

- Optional 3D views without breaking 2D contracts.
- Offline-safe caching of Story Nodes and layer metadata with governance-approved storage rules.
- Improved provenance browsing UX with keyboard-first citation navigation and copyable evidence IDs.

## 🗺️ Diagrams

### System and dataflow diagram

~~~mermaid
flowchart LR
  A["ETL — src/pipelines"] --> B["STAC/DCAT/PROV catalogs — data/stac · data/catalog/dcat · data/prov"]
  B --> C["Neo4j graph — src/graph + ingest"]
  C --> D["APIs — src/server + contracts"]
  D --> E["React/Map UI — web/src"]
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
  Graph-->>API: context bundle + provenance identifiers + policy flags
  API-->>UI: contracted payload (narrative + citations + audit flags)
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| API responses | JSON | `src/server/` endpoints | Contract tests + UI runtime guards |
| Layer registry configs | JSON or TS | `web/**/layers/**` | `schemas/ui/` validation if present |
| Story Nodes | Markdown + assets | `docs/reports/story_nodes/**` | Story Node template conformance; schema validation if present |
| Evidence identifiers | IDs and links | STAC/DCAT/PROV artifacts | Integrity checks and link checks if tooling exists |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Browser UI | runtime | browser | a11y + contract adherence |
| Build bundle | static output | repo-specific | CI build gate + a11y gates |
| Telemetry events | JSON | repo-specific | `schemas/telemetry/` if present |

### Sensitivity and redaction

- Treat API-delivered redaction and generalization as authoritative.
- Do not log PII, sensitive identifiers, or precise coordinates in client telemetry.
- Avoid persistent storage of sensitive content unless governance-approved.
- If a dataset or response is labeled with a restrictive classification, UI presentation must not downgrade it.

### Quality signals

- Contract adherence and explicit error handling for contract mismatches.
- Layer registry validation and attribution completeness.
- Provenance UX correctness and discoverability in Focus Mode.
- Accessibility baseline for map controls, Focus Mode, and citation interactions (target WCAG 2.1 AA or higher if governed).
- Performance budgets for layer load, Focus bundle fetch, and Story Node render.

## 🌐 STAC, DCAT & PROV Alignment

The UI makes provenance visible and inspectable. The UI does not author STAC/DCAT/PROV artifacts; it consumes evidence references returned by the API boundary and renders them consistently.

### STAC

- Expect STAC identifiers (collection/item IDs, asset keys) to arrive via API payloads.
- Surface STAC identifiers as explicit “Sources” affordances (copyable, linkable), not hidden metadata.
- If evidence identifiers are missing, show a missing-provenance state rather than implying certainty.

### DCAT

- Surface dataset-level metadata when provided (title, description, license, publisher, distributions).
- Ensure attribution and license indicators remain visible in UI surfaces that visualize the dataset.

### PROV-O

- Surface lineage identifiers when provided (run IDs, activity IDs, derivation relationships).
- Prefer a clear “how this was produced” affordance in Focus Mode rather than embedding lineage in tooltips only.

### Versioning

- When the API returns dataset/version metadata, display it and treat it as part of the evidence context.
- Cache keys and client persistence should be version-aware to avoid mixing versions of evidence or narrative.
- When a contract version mismatch is detected, fail loudly (user-visible) rather than silently degrading.

## 🧱 Architecture

### Components

| Component | Responsibility | Location |
|---|---|---|
| ETL | Acquire/normalize sources into governed outputs | `src/pipelines/` |
| Catalogs | Publish STAC/DCAT/PROV evidence products | `data/stac/` + `data/catalog/dcat/` + `data/prov/` |
| Graph | Semantics + relationships (Neo4j) | `src/graph/` |
| API boundary | Contracted data access + policy enforcement | `src/server/` |
| Web UI | Map + narrative experience | `web/src/` |
| Story Nodes | Governed narrative content | `docs/reports/story_nodes/` |
| Focus Mode | Provenance-linked deep dive UX | `web/src/focus/` + API payloads |

### Interfaces and contracts

| Contract / schema | Location | Versioning rule |
|---|---|---|
| API contracts | `src/server/contracts/` | Semver; breaking changes require version bump and deprecation plan |
| UI layer registry schema | `schemas/ui/` | Schema versioned; validation required if present |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Template updates require curator review |
| Story Node schema | `schemas/storynodes/` | Versioned; validation required if present |
| Telemetry event schemas | `schemas/telemetry/` | Versioned; event names stable once published |
| Markdown protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Governs fences/headings; **not confirmed in repo** if absent |

### Extension points checklist

- [ ] Data: new dataset under `data/<domain>/` and upstream docs updated
- [ ] Catalogs: STAC collection + items, DCAT mapping, PROV lineage updated
- [ ] Graph: ontology/constraints updated and ingest fixtures added
- [ ] APIs: contract update documented and versioned; implementation passes contract tests
- [ ] UI: feature implemented in `web/src/` using contract-bound clients (no direct graph access)
- [ ] UI: layer registry entry added/updated with attribution and sensitivity flags
- [ ] Story Nodes: new/updated story bundles validate against template and citation rules
- [ ] Focus Mode: provenance display enforced; missing-provenance UX verified
- [ ] A11y: keyboard navigation and citation UX acceptance criteria verified
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

Story Node bundles are expected to live under `docs/reports/story_nodes/` (with draft/published split if present). UI should prefer published Story Nodes for end-user experiences.

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
- [ ] Schema validation for `schemas/ui/`, `schemas/storynodes/`, and `schemas/telemetry/` if present.
- [ ] Accessibility checks for Focus Mode and citation interactions.
- [ ] Forbidden-pattern checks to prevent direct graph access from `web/`.
- [ ] Security and sovereignty checks to prevent leakage of sensitive locations and PII.
- [ ] Classification propagation checks where applicable (no “less restrictive output” paths).

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
| `focus_mode_entered` | UI | `docs/telemetry/` + `schemas/telemetry/` if present |
| `citation_opened` | UI | `docs/telemetry/` + `schemas/telemetry/` if present |
| `layer_toggled` | UI | `docs/telemetry/` + `schemas/telemetry/` if present |
| `api_error` | UI error boundary | `docs/telemetry/` + `schemas/telemetry/` if present |

## ⚖ FAIR+CARE & Governance

### Review gates

UI changes that typically require elevated review:

- Adding a new layer that could reveal sensitive locations by interaction or zoom.
- Changing redaction or generalization handling.
- Changing citation or provenance display behavior in Focus Mode.
- Adding AI-generated or predictive narrative surfaces visible to users.
- Adding or changing client-side storage behavior for content marked sensitive.

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
| v1.0.2 | 2025-12-27 | Tightened contract-first workflow, provenance UX requirements, and validation gates | TBD |
| v1.0.3 | 2025-12-27 | Aligned canonical pipeline wording to Master Guide; expanded STAC/DCAT/PROV subsections; added v13 drift guardrails and schema/telemetry path alignment | TBD |

---

Footer refs:
- Root README: `README.md`
- Web UI README: `web/README.md`
- Master guide: `docs/MASTER_GUIDE_v12.md`
- v13 blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Markdown work protocol: `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
