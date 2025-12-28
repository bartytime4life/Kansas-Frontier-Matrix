---
title: "KFM Web UI Source README"
path: "web/src/README.md"
version: "v1.0.4"
last_updated: "2025-12-28"
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

doc_uuid: "urn:kfm:doc:web:src:readme:v1.0.4"
semantic_document_id: "kfm-web-src-readme-v1.0.4"
event_source_id: "ledger:kfm:doc:web:src:readme:v1.0.4"
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
**Companion docs:** `README.md` (repo root), `web/README.md` (web root; if present).  
**Canonical pipeline ordering (non-negotiable):** **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

> Purpose: Provide a **contract-first, provenance-first** guide for implementing UI code under `web/src/` without breaking the API boundary, sovereignty/generalization rules, or Focus Mode provenance requirements.

---

## 📘 Overview

### Purpose

This README governs **how frontend work is organized and reviewed** under `web/src/` so it stays synced to KFM’s canonical pipeline and contract boundaries.

It makes UI invariants explicit and testable:
- **API boundary only** (no direct graph/database access),
- **contract-first** behavior (UI shape follows governed contracts/schemas),
- **evidence-first** UX (citations + provenance are first-class affordances),
- **Focus Mode hard gate**: no unsourced narrative.

### Scope

| In Scope | Out of Scope |
|---|---|
| React/map UI source code under `web/src/` (map runtime, Focus Mode UI, Story Node rendering, citation/provenance UX, state management, frontend tests) | ETL/pipelines (`src/pipelines/`), catalog generation outputs (`data/**`), graph ingest/migrations (`src/graph/`), server implementation internals (`src/server/`), infra/deployments |
| UI consumption of API contracts + schema-governed registries (layer registry, Story Node schema, telemetry schema) | Authoring/editing STAC/DCAT/PROV from the UI (catalogs are produced upstream) |
| Accessibility, performance, and telemetry wiring (when implemented) | Governance policy authoring (`docs/governance/**`) |
| Contract-safe UI evolution (semver + deprecation readiness) | Any attempt to bypass redaction/generalization or infer restricted locations client-side |

### Audience

- Primary: frontend engineers implementing features in `web/src/`.
- Secondary: API engineers validating UI↔API contracts; story curators validating provenance UX; governance/security reviewers.

### Definitions

- Glossary link: `docs/glossary.md` — if missing, treat as **not confirmed in repo** and fix links rather than creating a parallel glossary.
- Terms used in this document:
  - **API boundary:** the contracted server layer under `src/server/` that enforces redaction/generalization and serves governed payloads.
  - **Contract-first:** the UI is a strict consumer of versioned schemas/contracts; it does not “guess” field shapes.
  - **Story Node:** a governed narrative artifact (machine-ingestible + provenance-linked); canonical home is `docs/reports/story_nodes/`.
  - **Focus Mode:** deep-dive UX that renders only provenance-linked context bundles (no unsourced narrative).
  - **Evidence artifacts:** STAC/DCAT/PROV products referenced by the UI for traceability and audit.
  - **Classification propagation:** the UI must not present outputs less restrictive than upstream inputs in their lineage.

### Quick rules (read before coding)

1) **UI never reads Neo4j (or any database) directly.**  
2) **UI consumes governed data only via contracted APIs** (REST/GraphQL).  
3) **If you need a new field:** update contracts first → implement server → then consume in UI.  
4) **Focus Mode only shows provenance-linked narrative.** Missing evidence must show a “missing provenance” state.  
5) **Do not infer sensitive locations** through client-side correlation (joins, caching, reverse geocoding, centroid guessing, zoom-based deduction).

### When do I need an API Contract Extension?

Use `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` when:
- The UI needs **new fields** or **new endpoints**.
- Focus Mode needs a new **context bundle** element (citations, map payload, policy flags).
- You need a new **filter/search** behavior that changes request/response shapes.

Do **not** “work around” missing fields by scraping, guessing, or reading `data/**` at runtime.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | Maintainers | System + pipeline source of truth |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | Governs this document’s structure |
| Story Node template v3 | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Story curators | Narrative structure + citation rules |
| API Contract Extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API team | Contract-first change workflow |
| v13 redesign blueprint (draft) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Maintainers | One canonical home per subsystem; schemas/contracts first-class |
| Web root README | `web/README.md` | UI team | Web directory build/run rules (**not confirmed in repo** if absent) |
| API contracts | `src/server/contracts/**` | API team | OpenAPI/GraphQL contracts (**not confirmed in repo** if absent) |
| Schemas | `schemas/**` | Maintainers | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) (**not confirmed in repo** if absent) |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Maintainers | Markdown governance (**not confirmed in repo** if absent) |
| Governance | `docs/governance/**` | Governance | Ethics, sovereignty, review gates |

### Definition of done

- [ ] Front-matter is complete and `path:` matches `web/src/README.md`.
- [ ] Section structure aligns to `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`.
- [ ] Canonical pipeline ordering is preserved (no stage reordering or “shortcut” claims).
- [ ] All **MUST/SHALL** statements are traceable to governed docs, or downgraded to **recommended**.
- [ ] Validation steps are listed and reproducible (source of truth: `web/package.json` if present).
- [ ] Governance, CARE, and sovereignty considerations are explicit for UI changes that could expose sensitive data.

---

## 🗂️ Directory Layout

### This document

- `path`: `web/src/README.md`

### Related repository paths (canonical homes)

| Area | Path | What lives here |
|---|---|---|
| UI (canonical home) | `web/` | React + map client + Focus Mode UI |
| UI source | `web/src/` | UI source code + tests |
| API boundary | `src/server/` | Contracted data access + redaction/generalization enforcement |
| Graph build | `src/graph/` | Ontology bindings + graph build/migrations |
| Pipelines | `src/pipelines/` | ETL + catalog generation code |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV evidence products |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published story bundles + assets |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) (**not confirmed in repo** if absent) |
| MCP runs | `mcp/runs/` | Run logs + artifacts (**not confirmed in repo** if absent) |
| Tests | `tests/` | Unit + integration tests |
| Tools | `tools/` | Validators/QA scripts |
| CI | `.github/` | Workflows + policy gates |

### Expected file tree for `web/src/` (recommended shape)

This is a recommended shape aligned to “one canonical home per subsystem.” If the repo already has an established structure (e.g., `web/src/story/focus_mode/`), **prefer matching the existing canonical home** rather than creating parallel roots.

~~~text
📁 web/
├── 📄 README.md                              # web root rules (if present)
└── 📁 src/
    ├── 📁 api/                               # API clients + contract-bound types
    ├── 📁 map/                               # Map runtime adapters (MapLibre; optional 3D adapters)
    ├── 📁 layers/                            # Layer registry loader + validation hooks
    ├── 📁 story/                             # Story Node rendering + narrative utilities
    │   └── 📁 focus_mode/                    # Focus Mode UI + provenance/citation panels (preferred single home)
    ├── 📁 features/                          # Vertical feature slices (Search, Timeline, Layers)
    ├── 📁 ui/                                # Shared components
    ├── 📁 state/                             # State management
    ├── 📁 styles/                            # Tokens + global styles
    ├── 📁 telemetry/                         # Telemetry emitters + privacy guards (optional)
    ├── 📁 utils/                             # Guards, formatters, evidence helpers
    ├── 📁 test/                              # Fixtures + test helpers
    └── 📄 README.md                          # this file
~~~

### Import + runtime boundaries (do not cross)

- ✅ Allowed: `web/src/**` importing `web/src/**` and consuming API contracts via generated/manual clients.
- 🚫 Forbidden: UI importing from `src/server/**` or `src/graph/**` (server internals / graph internals).
- 🚫 Forbidden: UI directly connecting to Neo4j, Postgres, or other DBs.
- 🚫 Discouraged: treating `data/**` as a runtime source of truth (UI should render evidence refs returned by the API boundary).

---

## 🧭 Context

### Background

`web/src/` implements the user-facing KFM map + narrative experience. The UI is strictly downstream:
it visualizes governed payloads returned by the API boundary and renders provenance and evidence for end users.

Because the UI is downstream of catalogs + graph, **provenance visibility, sensitivity handling, and contract adherence are functional requirements**.

### Assumptions

- The UI is a web application (React-based) under `web/`, typically using MapLibre for mapping; optional 3D adapters may exist/configure alongside (e.g., Cesium). Treat optionality as configuration, not a second UI root.
- The UI reads from the API layer and does not require direct access to raw catalogs/graph; it displays layers + Story Nodes returned by the API boundary.
- Focus Mode is a first-class UX and is provenance-linked by default.

### Constraints and invariants

**Pipeline ordering is preserved**  
- **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

**One canonical home per subsystem**  
- UI lives under `web/` (do not introduce new UI roots).
- API boundary lives under `src/server/`.
- Story Nodes live under `docs/reports/story_nodes/`.

**API boundary (hard rule)**  
- UI consumes data only through contracted endpoints (REST/GraphQL).
- UI must not connect to Neo4j, import server internals, or query DBs directly.

**Contract-first behavior**  
- UI does not guess field shapes or silently accept breaking changes.
- If UI needs new data: update the API contract first (and tests), then implement server behavior, then consume in UI.

**Evidence-first / provenance-first UX**  
- Every visible layer and narrative claim should be traceable to an evidence identifier.
- Missing evidence is handled as a user-visible “missing provenance” state (not silently ignored).

**Redaction + generalization awareness**  
- Treat API-delivered redaction/generalization flags as authoritative.
- UI must not provide an interaction path that defeats redaction (e.g., “zoom to exact point” when only generalized geometry is allowed).

**No sensitive location inference**  
- Do not reconstruct restricted locations via client-side correlation (joins, reverse geocoding, centroid guessing, zoom-based deduction, caching).

### Open questions (resolve before “hardening”)

| Question | Owner | Target date |
|---|---|---|
| Where is the layer registry stored and what schema validates it (`schemas/ui/`?) | UI | TBD |
| What is the Focus Mode context bundle contract and required provenance fields | API | TBD |
| Where are Story Node schemas located (`schemas/story_nodes/` vs `schemas/storynodes/`) | Maintainers | TBD |
| What is the frontend test stack + command set (source of truth: `web/package.json`) | UI | TBD |
| Where are telemetry event schemas stored and how are events validated (`schemas/telemetry/`?) | Maintainers | TBD |

### Future extensions (must not break invariants)

- Optional 3D views without breaking 2D contracts or introducing a second UI home.
- Offline-safe caching of Story Nodes and layer metadata with governance-approved storage rules.
- Improved provenance browsing UX: keyboard-first citation navigation and copyable evidence IDs.

---

## 🗺️ Diagrams

### System and dataflow diagram

~~~mermaid
flowchart LR
  A["ETL — src/pipelines/"] --> B["STAC/DCAT/PROV catalogs — data/stac · data/catalog/dcat · data/prov"]
  B --> C["Neo4j graph — src/graph/"]
  C --> D["APIs — src/server/ (contracts, redaction, access control)"]
  D --> E["React/Map UI — web/src/"]
  E --> F["Story Nodes — docs/reports/story_nodes/"]
  F --> G["Focus Mode — provenance-linked by default"]
~~~

### Focus Mode request sequence

~~~mermaid
sequenceDiagram
  participant UI as Web UI
  participant API as API Boundary
  participant Graph as Graph + Catalog access

  UI->>API: Focus query(entity_id, options)
  API->>Graph: fetch context + evidence refs (with policy)
  Graph-->>API: context bundle + provenance identifiers + policy flags
  API-->>UI: contracted payload (narrative + citations + audit flags)
~~~

### Contract-first UI change workflow (when UI needs new data)

~~~mermaid
flowchart TD
  A[UI needs a new field / behavior] --> B[Author API Contract Extension doc]
  B --> C[Update OpenAPI/GraphQL contract + tests]
  C --> D[Implement in src/server with redaction/generalization]
  D --> E[Ship UI change in web/src using contract-bound client]
  E --> F[Validate Focus Mode provenance + a11y + leakage checks]
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| API responses | JSON | `src/server/` endpoints | Contract tests + UI runtime guards |
| Layer registry configs | JSON/TS | repo-defined | Schema validation if present |
| Story Nodes | Markdown + assets | `docs/reports/story_nodes/**` | Template/schema validation if present |
| Evidence identifiers | IDs + links | STAC/DCAT/PROV artifacts (referenced by API) | Link checks + integrity checks if tooling exists |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Browser UI | runtime | browser | a11y + contract adherence |
| Build bundle | static output | repo-specific | CI build gate + a11y gates |
| Telemetry events | JSON | repo-specific | `schemas/telemetry/` if present |

### Sensitivity and redaction

- Treat API-delivered redaction/generalization as authoritative.
- Do not log PII, sensitive identifiers, or precise coordinates in client telemetry.
- Avoid persistent storage of sensitive content unless governance-approved.
- If a dataset/response is labeled restrictive, UI presentation must not downgrade it.

### Contract mismatch behavior (recommended)

- Fail loudly (user-visible) on contract incompatibilities.
- Prefer explicit “This view requires a newer server contract” messaging over silent degradation.
- Log a structured error event (without sensitive payloads) if telemetry is enabled.

---

## 🌐 STAC, DCAT & PROV Alignment

The UI makes provenance visible and inspectable. The UI **does not author** STAC/DCAT/PROV artifacts; it consumes evidence references returned by the API boundary and renders them consistently.

### Evidence linking UI conventions (recommended)

| Reference type | Typical identifier | UI behavior |
|---|---|---|
| STAC Item | `stac_item_id` | “Source” link/affordance; map asset attribution; copyable ID |
| STAC Collection | `stac_collection_id` | Collection-level context + grouping |
| DCAT Dataset | `dcat_dataset_id` | Dataset metadata panel (license/publisher/distributions) |
| PROV Activity/Run | `prov_activity_id` / `run_id` | “How produced” lineage panel |
| Graph Entity | `entity_id` (stable) | Related items navigation (via API only) |

### STAC

- Expect STAC identifiers (collection/item IDs, asset keys) via API payloads.
- Surface STAC identifiers as explicit “Sources” affordances (copyable/linkable), not hidden metadata.
- If evidence identifiers are missing, show a missing-provenance state rather than implying certainty.

### DCAT

- Surface dataset-level metadata when provided (title, description, license, publisher, distributions).
- Ensure attribution and license indicators remain visible wherever the dataset is visualized.

### PROV-O

- Surface lineage identifiers when provided (run IDs, activity IDs, derivation relationships).
- Prefer a “how this was produced” affordance in Focus Mode (panel/section), not tooltips only.

### Versioning

- When API returns dataset/version metadata, display it and treat it as part of evidence context.
- Client caching must be version-aware (avoid mixing evidence versions).
- When a contract version mismatch is detected: fail loudly (user-visible), not silently.

---

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
| Focus Mode | Provenance-linked deep dive UX | `web/src/story/focus_mode/` + API payloads |

### Interfaces and contracts

| Contract / schema | Location | Versioning rule |
|---|---|---|
| API contracts | `src/server/contracts/**` | Semver; breaking changes require version bump + deprecation plan (**not confirmed in repo** if absent) |
| UI layer registry schema | `schemas/ui/` | Schema versioned; validation required if present (**not confirmed in repo** if absent) |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Template updates require curator review |
| Story Node schema | `schemas/story_nodes/` | Versioned; validation required if present (**not confirmed in repo** if absent) |
| Telemetry event schemas | `schemas/telemetry/` | Versioned; event names stable once published (**not confirmed in repo** if absent) |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Governs fences/headings (**not confirmed in repo** if absent) |

### Extension points checklist (vertical-slice aligned)

- [ ] Data: new dataset under `data/<domain>/...` and domain docs updated
- [ ] Catalogs: STAC collection + items, DCAT mapping, PROV lineage updated
- [ ] Graph: ontology/constraints updated and ingest fixtures added
- [ ] APIs: contract update documented + versioned; implementation passes contract tests + redaction rules
- [ ] UI: feature implemented in `web/src/` using contract-bound clients (**no direct graph access**)
- [ ] UI: layer registry entry added/updated with attribution + sensitivity flags
- [ ] Story Nodes: new/updated story bundles validate against template + citation rules
- [ ] Focus Mode: provenance display enforced; missing-provenance UX verified
- [ ] A11y: keyboard navigation + citation UX acceptance criteria verified
- [ ] Telemetry: signals added and schema versioned if governed

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

Focus Mode is a UI state where users deep-dive into an entity or story:

- Entry via map selection, search results, Story Node deep links, or entity drawers.
- Focus Mode loads a **context bundle** via the API boundary.
- The UI renders:
  - narrative content,
  - explicit citations and evidence identifiers,
  - a provenance panel,
  - redaction/sensitivity messaging when applicable.

Story Node bundles are expected to live under `docs/reports/story_nodes/` (with draft/published split if present). UI should prefer published Story Nodes for end-user experiences.

### Provenance-linked narrative rule (hard gate)

- Every displayed factual claim in Focus Mode must trace to evidence identifiers.
- Never display AI-generated text as unmarked fact.
- Any predictive/suggestive content must be opt-in, visibly labeled, and include uncertainty metadata.
- Do not infer or reveal sensitive locations through UI behavior.

### Optional structured controls (if supported)

These hints may be returned by the API or embedded in Story Node content.

~~~yaml
focus_layers:
  - "TBD:layer_id"
focus_time: "TBD:YYYY or YYYY-MM-DD range"
focus_center: [ -98.0000, 38.0000 ]
~~~

---

## 🧪 Validation & CI/CD

### Validation steps (minimum gates)

- [ ] Markdown protocol validation (front-matter + required sections).
- [ ] Link/reference checks (no orphan pointers).
- [ ] UI lint + type checks (source of truth: `web/package.json` scripts, if present).
- [ ] Unit tests for:
  - citation parsing/rendering,
  - Focus Mode state transitions,
  - layer registry loading + validation behavior.
- [ ] Contract alignment checks against `src/server/contracts/**` (if present).
- [ ] JSON schema validation for:
  - UI layer registry (if present),
  - Story Node schemas (if present),
  - telemetry schemas (if present).
- [ ] Accessibility checks for Focus Mode and citation interactions.
- [ ] Forbidden-pattern checks to prevent direct graph access from `web/`.
- [ ] Security + sovereignty scanning gates (where applicable):
  - secret scan
  - PII scan
  - sensitive-location leakage checks
  - classification propagation checks (no downgrades without review)

### Reproduction

Replace placeholders with repo scripts (use `web/package.json` as source of truth).

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

### Telemetry signals (recommended)

| Signal | Source | Where recorded |
|---|---|---|
| `focus_mode_entered` | UI | `docs/telemetry/` + `schemas/telemetry/` if present |
| `citation_opened` | UI | `docs/telemetry/` + `schemas/telemetry/` if present |
| `layer_toggled` | UI | `docs/telemetry/` + `schemas/telemetry/` if present |
| `api_error` | UI error boundary | `docs/telemetry/` + `schemas/telemetry/` if present |
| `focus_mode_redaction_notice_shown` | UI | `docs/telemetry/` + `schemas/telemetry/` if present |

---

## ⚖ FAIR+CARE & Governance

### Review gates

UI changes that typically require elevated review:

- Adding a new layer that could reveal sensitive locations by interaction or zoom.
- Changing redaction or generalization handling.
- Changing citation/provenance display behavior in Focus Mode.
- Adding AI-generated or predictive narrative surfaces visible to users.
- Adding/changing client-side storage behavior for content marked sensitive.
- New public-facing endpoints or interactions that could reveal restricted locations.

### CARE / sovereignty considerations

- Identify communities impacted by new UI surfaces that expose location-bearing data.
- Do not add UI affordances that encourage discovery of restricted or culturally sensitive locations.
- Treat the API boundary as the enforcement point for redaction/generalization; UI must not bypass it.
- No output may be less restricted than any upstream input in its lineage.

### AI usage constraints

- Allowed AI transforms for this document: summarization, structure extraction, translation, keyword indexing.
- Prohibited: generating policy or inferring sensitive locations.
- If the UI renders predictive or AI-generated content, it must be opt-in and clearly labeled with uncertainty metadata.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.4 | 2025-12-28 | Template-synced rewrite; tightened API boundary + “one canonical home” alignment; clarified Focus Mode + provenance expectations | TBD |
| v1.0.3 | 2025-12-27 | Aligned canonical pipeline wording; expanded provenance + schema/telemetry sections; added drift guardrails | TBD |
| v1.0.2 | 2025-12-27 | Tightened contract-first workflow, provenance UX requirements, and validation gates | TBD |
| v1.0.1 | 2025-12-24 | Clarified invariants and section structure | TBD |
| v1.0.0 | 2025-12-21 | Initial README for `web/src` | TBD |

---

Footer refs:
- Root README: `README.md`
- Web root README: `web/README.md`
- Master guide: `docs/MASTER_GUIDE_v12.md`
- v13 blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API Contract Extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
