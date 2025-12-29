---
title: "Kansas Frontier Matrix — Repository README"
path: "README.md"
version: "v1.0.5"
last_updated: "2025-12-29"
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

doc_uuid: "urn:kfm:doc:readme:v1.0.5"
semantic_document_id: "kfm-readme-v1.0.5"
event_source_id: "ledger:kfm:doc:readme:v1.0.5"
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

# Kansas Frontier Matrix — Repository README

Kansas Frontier Matrix (KFM) is an open-source **geospatial + historical** knowledge system (a “living atlas” of Kansas) that ingests heterogeneous sources, publishes governed evidence catalogs (**STAC/DCAT/PROV**), builds a semantically structured **Neo4j graph**, and serves evidence through **contracted APIs** into a **map + narrative UI**. KFM is designed so that **every narrative claim can be traced to versioned evidence**, and every derived product has explicit lineage.

**Canonical pipeline ordering (non‑negotiable):**  
**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

**API boundary (non‑negotiable):** The UI never reads Neo4j directly; all access is via contracted APIs.

**Repo hygiene invariant:** KFM enforces “one canonical home per subsystem” and “one source of truth” for schemas/contracts/docs to reduce repo drift; avoid ad‑hoc folders outside canonical roots.

---

## 📘 Overview

### Purpose

- Provide a single entry point for contributors and readers to understand:
  - what KFM is,
  - the canonical pipeline ordering and non‑negotiables,
  - where artifacts live across the pipeline,
  - and which governance/validation constraints must not be broken.
- Preserve an evidence-first workflow where downstream views (including Focus Mode narrative) remain traceable back to catalogs and provenance.

### Scope

| In Scope | Out of Scope |
|---|---|
| Repository orientation; canonical pipeline; directory layout; contribution pointers; governance/validation invariants | Full subsystem implementations; deployment specifics; domain-specific dataset documentation (see domain READMEs + subsystem docs) |

### Audience

- Primary: maintainers and contributors (data, catalog, graph, API, UI, narrative).
- Secondary: reviewers (governance/ethics/sovereignty), historians/editors, external collaborators.

### Definitions

- Glossary: `docs/glossary.md` (*not confirmed in repo* — add/repair link if glossary lives elsewhere)

Core terms used in this README:

- **Domain pack**: the minimal governed components that let a domain participate end-to-end (staging + transforms + catalogs + graph mappings + tests + docs).
- **Contract artifact**: machine-validated schema/spec (JSON Schema, OpenAPI, GraphQL SDL, UI registry schema).
- **Evidence artifact**: catalog + provenance outputs consumed downstream (STAC/DCAT/PROV and derived evidence products).
- **Story Node**: a governed narrative artifact that is machine‑ingestible and provenance‑linked.
- **Focus Mode**: a UI experience that consumes only provenance‑linked context bundles (no unsourced narrative).
- **Contract-first**: schemas + API contracts are first‑class artifacts; breaking changes require versioning + compatibility tests.
- **Deterministic pipeline**: idempotent, config-driven transforms with logged inputs/outputs and stable IDs.

### Quick links

Suggested reading order (treat any missing paths as “not confirmed in repo” and repair as part of repo hygiene):

1) `docs/MASTER_GUIDE_v12.md` (system + pipeline source of truth)  
2) `docs/README.md` (docs index; *not confirmed in repo*)  
3) `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`  
4) `docs/templates/TEMPLATE__STORY_NODE_V3.md`  
5) `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`  
6) `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` (draft; “if adopted”)  
7) `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` (*not confirmed in repo*)  
8) `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` (*not confirmed in repo*)

### Key artifacts

| Artifact | Path / Identifier | Status | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | present | Canonical pipeline + invariants + extension matrix |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | present | Default governed doc template |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | present | Focus Mode narrative artifacts |
| API Contract Extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | present | REST/GraphQL contract changes |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | present | Draft proposal; treat as “if adopted” |
| Repo structure standard | `docs/standards/KFM_REPO_STRUCTURE_STANDARD.md` | not confirmed in repo | Proposed standard; keep paths canonical |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | not confirmed in repo | Referenced standard; create if missing |
| Full architecture vision | `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` | not confirmed in repo | Vision doc; create/repair if missing |
| Next stages blueprint | `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` | not confirmed in repo | Roadmap doc; create/repair if missing |

### Definition of done

- [ ] Front-matter complete + valid (`path: README.md`)
- [ ] H2 sections match the Universal template heading set (no extra H2 headings)
- [ ] Canonical pipeline + invariants stated clearly (pipeline order, API boundary, provenance rules)
- [ ] Canonical roots described; no new top-level “drift” encouraged
- [ ] Any repo path references are either verifiably present or explicitly marked *not confirmed in repo*
- [ ] Validation/CI expectations stated (commands may be placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Footer refs preserved (governance + templates + architecture pointers)

---

## 🗂️ Directory Layout

### This document

- `path`: `README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Canonical governed docs (guides, designs, domain notes) |
| Templates | `docs/templates/` | Governed doc templates (universal/story/API) |
| Architecture | `docs/architecture/` | System designs, roadmaps, ADRs (if present) |
| Data domains + staging | `data/` | Raw/work/processed data + evidence artifacts |
| Catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC, DCAT, and PROV outputs |
| Pipelines | `src/pipelines/` | Deterministic transforms; outputs written under `data/**` |
| Graph | `src/graph/` + `data/graph/` | Ontology-governed ingest + fixtures/imports |
| API boundary | `src/server/` | Contracted access layer (REST/GraphQL); redaction + provenance refs |
| UI | `web/` | React map UI (MapLibre/Cesium as configured); no direct graph access |
| Schemas | `schemas/` | JSON Schemas for catalogs, Story Nodes, UI registries, telemetry |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published narratives + assets |
| MCP / experiments | `mcp/` | Run manifests, evaluations, model cards, SOPs |
| Tests | `tests/` | Unit + integration + contract tests |
| Tooling | `tools/` | Validators, scripts, repo lint |
| CI | `.github/` | Workflows, issue templates, security policies |
| Releases | `releases/` | Release manifests/SBOMs/attestations/telemetry snapshots (if used) |

Optional roots (if present; keep one canonical home per concern):

- Security: `.github/SECURITY.md` and/or `docs/security/`
- Telemetry docs: `docs/telemetry/` and schemas under `schemas/telemetry/`
- Standards: `docs/standards/`

> Some directories may not exist yet. If a canonical root is missing, treat it as a gap and implement it per the Master Guide rather than introducing new top-level structure.

### Repo top-levels (expected)

~~~text
📁 .
├── 📄 README.md
├── 📁 .github/
│   ├── 📁 workflows/
│   └── 📄 SECURITY.md                         # if present
├── 📁 data/
│   ├── 📁 raw/
│   │   └── 📁 <domain>/
│   ├── 📁 work/
│   │   └── 📁 <domain>/
│   ├── 📁 processed/
│   │   └── 📁 <domain>/
│   ├── 📁 stac/
│   │   ├── 📁 collections/
│   │   └── 📁 items/
│   ├── 📁 catalog/
│   │   └── 📁 dcat/
│   └── 📁 prov/
├── 📁 docs/
│   ├── 📄 MASTER_GUIDE_v12.md
│   ├── 📁 templates/
│   │   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│   │   ├── 📄 TEMPLATE__STORY_NODE_V3.md
│   │   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
│   ├── 📁 architecture/
│   │   ├── 📄 KFM_REDESIGN_BLUEPRINT_v13.md
│   │   ├── 📄 KFM_NEXT_STAGES_BLUEPRINT.md
│   │   └── 📄 KFM_VISION_FULL_ARCHITECTURE.md
│   ├── 📁 data/
│   │   └── 📁 <domain>/
│   └── 📁 reports/
│       └── 📁 story_nodes/                    # pattern; draft/published split if defined
├── 📁 mcp/
│   ├── 📁 runs/
│   └── 📁 experiments/
├── 📁 schemas/
│   ├── 📁 stac/
│   ├── 📁 dcat/
│   ├── 📁 prov/
│   ├── 📁 story_nodes/
│   ├── 📁 ui/
│   └── 📁 telemetry/
├── 📁 src/
│   ├── 📁 pipelines/
│   ├── 📁 graph/
│   └── 📁 server/
├── 📁 web/
├── 📁 tests/
├── 📁 tools/
└── 📁 releases/
~~~

### Documentation map

- `docs/MASTER_GUIDE_v12.md` (system + pipeline source of truth)
- `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` (draft reference; if adopted)
- `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` (roadmap; *not confirmed in repo*)
- `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` (vision; *not confirmed in repo*)
- `docs/standards/` (governed standards; *some items not confirmed in repo*)
- `docs/templates/` (document + MCP templates)

---

## 🧭 Context

### Background

KFM’s design goal is an **evidence-first, provenance-linked** system where every downstream view (including narrative Focus Mode) remains traceable back to catalog and provenance artifacts.

As KFM scales to more domains and evidence products, it also hardens repository hygiene by enforcing **one canonical home per subsystem** and making **schemas/contracts** first-class artifacts.

### Assumptions

- Canonical pipeline ordering is preserved.
- Schemas/contracts are treated as first-class artifacts.
- Pipelines are deterministic, reproducible, and produce diffable outputs.

### Constraints and invariants

- **Pipeline ordering is non-negotiable:** **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**
- **API boundary is non-negotiable:** UI consumes contracted data via the API boundary only (no direct Neo4j dependency).
- **Evidence-first narrative:** no unsourced narrative in Story Nodes; Focus Mode is provenance-only.
- **Maintain one source of truth:** avoid duplicating schemas/contracts/docs across the repo; minimize redundancy to prevent drift.
- **One canonical home per subsystem:** do not introduce new top-level roots for convenience.
- **Contract-first versioning:** breaking changes require schema/contract version bumps and compatibility tests.
- **Sensitivity propagation:** no output can be less restricted than any input in its lineage.
- **No sensitive-location leakage:** for culturally sensitive materials, avoid publishing raw coordinates or re-identifying spatial precision; generalize/mask as required.
- **AI/predictive content constraints:** opt-in only, clearly labeled, includes uncertainty metadata, and must not infer or reveal sensitive locations.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which paths are currently implemented vs target layout? | TBD | TBD |
| Which staging model is canonical per domain: stage-first vs domain-pack? | TBD | TBD |
| Do legacy duplicate roots exist and what is the migration/deprecation plan? | TBD | TBD |
| Where is the canonical glossary located and is it complete? | TBD | TBD |
| Which CI validators exist today (Markdown protocol, schema lint, contract tests, link checks)? | TBD | TBD |
| Confirm Story Node publish workflow (`draft/` vs `published/`) and any legacy path. | TBD | TBD |
| Are domain naming conventions standardized (kebab-case vs snake_case)? | TBD | TBD |

### Future extensions

- New domains built as domain packs: inputs + ETL + catalogs + graph + API + UI + at least one Story Node.
- AI evidence products treated as catalog assets (STAC) and linked into Focus Mode with explicit uncertainty.
- External entity linking (optional): reconcile to external identifiers (e.g., Wikidata/GeoNames/VIAF) without violating governance constraints.
- Graph nuance (optional): represent contested knowledge / uncertainty (confidence/qualification fields) while preserving provenance.
- “Vertical slice” expectation for readiness (recommended): one dataset → STAC/DCAT/PROV → graph ingest fixture → API endpoint → UI layer → one published Story Node.

---

## 🗺️ Diagrams

### System and dataflow diagram

~~~mermaid
flowchart LR
  R["Raw sources — data/**"] --> A["ETL — src/pipelines/**"]
  A --> B["STAC/DCAT/PROV — data/stac · data/catalog/dcat · data/prov"]
  B --> C["Graph — src/graph + data/graph"]
  C --> D["API boundary — src/server + contracts"]
  D --> E["UI — web/"]
  E --> F["Story Nodes — docs/reports/story_nodes"]
  F --> G["Focus Mode — provenance-linked only"]
~~~

### Optional sequence diagram

~~~mermaid
sequenceDiagram
  participant UI as UI (web/)
  participant API as API (src/server)
  participant Graph as Graph (Neo4j via src/graph)
  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs (with redaction rules)
  Graph-->>API: context bundle + evidence references
  API-->>UI: contracted payload (narrative + citations + audit flags)
~~~

---

## 📦 Data & Metadata

### Inputs

Preferred staging model (baseline):

- `data/raw/<domain>/` — immutable source snapshots
- `data/work/<domain>/` — intermediate transforms
- `data/processed/<domain>/` — normalized outputs used for catalogs and graph ingest

Recommended metadata/supporting inputs (as applicable):

- `data/sources/**` — upstream source manifests (source_id, provider, license, spatial/temporal extent, attribution)
- run logs/manifests (record inputs, code version, outputs, and validation results) — map to PROV Activities where possible

### Outputs

Global evidence artifacts:

- STAC: `data/stac/collections/` + `data/stac/items/`
- DCAT: `data/catalog/dcat/`
- PROV: `data/prov/`

Downstream consumers:

- Graph ingest references STAC/DCAT/PROV identifiers.
- API responses include provenance references and apply redaction/generalization.
- UI renders evidence and Story Nodes with citations and disclosure flags.

### Sensitivity and redaction

Public artifacts must not reveal restricted locations or culturally sensitive knowledge. Apply generalization/redaction at the earliest safe boundary:

- geometry generalization in catalog outputs when required,
- API-level redaction for sensitive fields and spatial precision,
- Story Node review gates before publication (especially for sensitive domains/assets).

### Quality signals

- STAC/DCAT/PROV validate against schemas in `schemas/**`.
- No orphan references: entity refs, evidence refs, and Story Node refs resolve.
- Deterministic runs and diffable outputs; stable IDs and versioned artifacts.
- Provenance is complete enough to answer: what changed, why, when, and by what process.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

For each dataset/evidence product:

- STAC Collection + Item(s) exist and validate.
- Items reference assets and, where permitted, geometry; geometry may be generalized for public release.
- IDs are stable; versions are explicit.

### DCAT

- Each STAC Collection should map to a DCAT dataset record.
- Each publishable artifact/export bundle should map to a DCAT distribution record.
- DCAT records include license, description, keywords, and distribution access metadata.

### PROV-O

- PROV bundles describe lineage across raw → work → processed → catalog → graph ingest.
- Include:
  - `prov:Entity` for artifacts,
  - `prov:Activity` for pipeline runs and validation,
  - `prov:Agent` for tools and responsible parties.
- Prefer one PROV activity bundle per meaningful run under `data/prov/**`.

### Versioning

- IDs are stable; versions are explicit and machine-readable.
- Backward-incompatible changes require schema/contract version bumps.
- Catalogs and graph should link predecessor/successor versions where applicable.

---

## 🧱 Architecture

### Components

- **ETL / pipelines:** deterministic transforms in `src/pipelines/**`
- **Catalogs:** STAC/DCAT/PROV evidence in `data/**`
- **Graph:** ontology-aligned ingest in `src/graph/**` with fixtures/imports in `data/graph/**`
- **API boundary:** contracted REST/GraphQL interface in `src/server/**`
- **UI:** `web/**` renders map and Focus Mode from API payloads
- **Story Nodes:** `docs/reports/story_nodes/**` for provenance-linked narratives
- **Telemetry/security/governance:** docs + schemas to keep behavior auditable

### Interfaces and contracts

- Governed docs: `docs/templates/**`
- JSON schemas: `schemas/**` (STAC, DCAT, PROV, story nodes, UI registries, telemetry)
- API contracts: `src/server/contracts/**` (or repo-defined equivalent; if different, *not confirmed in repo*)
- UI registries: schema-validated layer registries under `web/**` and `schemas/ui/**`

### Story Nodes and Focus Mode

- Story Nodes must:
  - carry explicit citations to cataloged artifacts (STAC/DCAT/PROV),
  - connect to graph entities (Place/Person/Event/Document/etc.) via stable identifiers,
  - separate **fact vs inference vs hypothesis** where applicable (especially if AI-generated text is included).
- Focus Mode is a hard-gated provenance-only view:
  - no narrative text is shown without proper citations or lineage ties,
  - predictive/suggestive content must be opt-in, carry uncertainty/confidence metadata, and must not infer or reveal sensitive locations,
  - redaction/generalization must be visible via disclosure/audit affordances.

### Extension points checklist

For every new capability (dataset, domain, endpoint, UI layer, Story Node type):

- [ ] Add or update deterministic pipeline steps (`src/pipelines/**`)
- [ ] Produce/refresh STAC/DCAT/PROV evidence (`data/**`)
- [ ] Validate against schemas (`schemas/**`)
- [ ] Update graph mappings/fixtures (`src/graph/**`, `data/graph/**`)
- [ ] Add/update API contracts + tests (`src/server/**`)
- [ ] Add/update UI registry entries (`web/**`)
- [ ] Add/update Story Node(s) with provenance-linked citations (`docs/reports/story_nodes/**`)
- [ ] Record telemetry signals + update schema if needed (`schemas/telemetry/**`)
- [ ] Add regression tests/validators and update release notes if applicable

---

## 🧪 Validation & CI/CD

### Minimum CI gates

Recommended minimum checks:

- [ ] Markdown protocol validation (front-matter + required sections)
- [ ] Link/reference checks (no orphan pointers; “not confirmed in repo” used where appropriate)
- [ ] JSON schema validation:
  - STAC/DCAT/PROV
  - Story Node schemas (if present)
  - telemetry schemas (if present)
  - UI layer registry schemas (if present)
- [ ] Graph integrity tests (constraints, expected labels/edges)
- [ ] API contract tests (OpenAPI/GraphQL schema + resolver tests)
- [ ] Security + sovereignty scanning gates (as applicable):
  - secret scan
  - PII scan
  - sensitive-location leakage checks
  - classification propagation checks (no downgrades without review)

### Reproduction

~~~bash
# NOTE: commands are placeholders; replace with repo-approved tooling.

# 1) validate schemas (STAC/DCAT/PROV/story nodes/UI/telemetry)
# 2) run unit/integration tests
# 3) run doc lint / markdown protocol checks
# 4) run sovereignty/PII scans (where applicable)

# make validate-schemas
# make test
# make lint-docs
# make scan-governance
~~~

### Telemetry signals

If telemetry is implemented, useful signals include:

| Signal | Why it matters |
|---|---|
| `classification_assigned` | proves classification decisions were recorded |
| `redaction_applied` | proves masking/generalization is auditable |
| `promotion_blocked` | proves unsafe promotion was prevented |
| `catalog_published` | proves catalog publication is tracked |
| `focus_mode_redaction_notice_shown` | proves UI disclosure for redaction |

### Release hardening

If releases are packaged under `releases/`, recommended artifacts include:

- SBOM (Software Bill of Materials)
- build provenance attestations (e.g., SLSA)
- signed manifests / versioned release bundles

---

## ⚖ FAIR+CARE & Governance

### Review gates

Changes that typically require elevated review:

- Adding new sensitive layers (restricted locations, cultural knowledge, PII)
- Introducing/changing AI-generated narrative behavior visible to users
- Adding new external data sources (license/provenance review)
- Adding new public-facing endpoints
- Changing classification/sensitivity for any artifact
- Adding UI layers or interactions that could reveal sensitive locations by interaction/zoom

### CARE and sovereignty considerations

- Identify communities impacted and protection rules.
- Use generalization/redaction for restricted locations.
- Ensure sensitive assets (images/docs) follow review gates before publication.
- Redaction/generalization must be documented and enforced:
  - in datasets (`data/processed/**`),
  - in catalogs (STAC/DCAT),
  - in API responses (redaction policies),
  - and in UI rendering (CARE gating).

### AI usage constraints

- Ensure this document’s AI permissions/prohibitions match intended use.
- Do not infer or generate sensitive locations.
- User-facing AI outputs must remain evidence-led, provenance-linked, and clearly labeled.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial repository README in governed-doc format | TBD |
| v1.0.1 | 2025-12-23 | Added repo navigation + clarified canonical roots/CI behavior | TBD |
| v1.0.2 | 2025-12-24 | Added architecture pointers; clarified data layout options; tightened doc/code separation | TBD |
| v1.0.3 | 2025-12-26 | Clarified staging vs domain-pack patterns; added provenance/run-pointer guidance | TBD |
| v1.0.4 | 2025-12-27 | Aligned sections and subheadings to Universal template; synced directory roots to Master Guide v12 inventory; normalized Data & Metadata and STAC/DCAT/PROV subsections | TBD |
| v1.0.5 | 2025-12-29 | Synced README language and file tree to Master Guide v12; consolidated Story Node/Focus Mode guidance under Architecture; tightened “one source of truth” + link-check expectations | TBD |

---

Footer refs (do not remove):
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Next stages blueprint: `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Full architecture vision: `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API Contract Extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`