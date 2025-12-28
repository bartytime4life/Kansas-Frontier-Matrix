---
title: "Kansas Frontier Matrix — Repository README"
path: "README.md"
version: "v1.0.4"
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

doc_uuid: "urn:kfm:doc:readme:v1.0.4"
semantic_document_id: "kfm-readme-v1.0.4"
event_source_id: "ledger:kfm:doc:readme:v1.0.4"
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

Kansas Frontier Matrix, or KFM, is a geospatial and historical knowledge system built around **governed data**, **catalog outputs (STAC/DCAT/PROV)**, **graph semantics (Neo4j)**, **contracted APIs**, and a **map and narrative UI**.

**Canonical pipeline ordering (non‑negotiable):**  
**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

**API boundary (non‑negotiable):** The UI never reads Neo4j directly; all access is via contracted APIs.

---

## 📘 Overview

### Purpose

- Provide a single entry point for contributors and readers to understand:
  - what KFM is,
  - how the repository is organized,
  - where artifacts “live” across the pipeline,
  - and which governance/validation rules must not be broken.
- Preserve an evidence-first workflow where downstream views (including Focus Mode narrative) remain traceable back to catalogs and provenance.

### Scope

| In Scope | Out of Scope |
|---|---|
| Repository orientation, canonical pipeline, directory layout, contribution pointers | Full subsystem implementations, deployment specifics, and domain-specific dataset documentation (see domain READMEs + subsystem docs) |

### Audience

- Primary: maintainers and contributors (data, catalog, graph, API, UI, narrative).
- Secondary: reviewers (governance/ethics/sovereignty), historians/editors, external collaborators.

### Definitions

- Glossary: `docs/glossary.md` (not confirmed in repo — add/repair link if glossary lives elsewhere)
- Terms used in this doc:
  - **Domain pack**: the minimal governed components that let a domain participate in the pipeline (inputs + transforms + catalogs + mappings + validations + docs).
  - **Contract artifact**: machine-validated schema/spec (JSON Schema, OpenAPI, GraphQL SDL, UI registry schema).
  - **Evidence artifact**: catalog + provenance outputs consumed downstream (STAC/DCAT/PROV and derived evidence products).
  - **Story Node**: a provenance-linked narrative artifact designed to render in the UI.
  - **Focus Mode**: an immersive UI view that consumes provenance-linked context only.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline + invariants + extension matrix |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Default governed doc template |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative | Focus Mode narrative artifacts |
| API Contract Extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | REST/GraphQL contract changes |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Draft proposal; treat as “if adopted” |
| Repo structure standard | `docs/standards/KFM_REPO_STRUCTURE_STANDARD.md` | Standards | Not confirmed in repo |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Standards | Not confirmed in repo |

Suggested reading order (if the paths exist; otherwise treat as not confirmed and repair links):

1) `docs/MASTER_GUIDE_v12.md`  
2) `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`  
3) `docs/templates/TEMPLATE__STORY_NODE_V3.md`  
4) `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`  
5) `docs/architecture/` (blueprints/ADRs/diagrams)

### Definition of done

- [ ] Front-matter complete + valid (`path: README.md`)
- [ ] H2 sections match the Universal template heading set (no extra H2 headings)
- [ ] Canonical pipeline + invariants stated clearly (pipeline order, API boundary, provenance rules)
- [ ] Canonical roots described (and marked if not confirmed in repo)
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
| Docs | `docs/` | Canonical governed docs, templates, standards, architecture |
| Data domains + staging | `data/` | Raw/work/processed data, domain modules, and evidence artifacts |
| Catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC, DCAT, and PROV outputs |
| Graph | `src/graph/` + `data/graph/` + `docs/graph/` | Ontology-governed ingest + fixtures + graph docs |
| Pipelines | `src/pipelines/` + `docs/pipelines/` | Deterministic transforms; outputs written under `data/**` |
| API boundary | `src/server/` | Contracted access layer (REST/GraphQL); redaction + provenance refs |
| Frontend | `web/` | React map UI (MapLibre/Cesium as configured); no direct graph access |
| Schemas | `schemas/` | JSON Schemas for catalogs, story nodes, UI registries, telemetry |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published narratives + assets |
| Telemetry | `docs/telemetry/` + `schemas/telemetry/` | Telemetry docs and schema contracts |
| Security | `.github/SECURITY.md` + `docs/security/` | Security policy, threat models, redaction guidance |
| MCP / experiments | `mcp/` | Run manifests, evaluations, model cards, SOPs |
| CI | `.github/` | Workflows, issue templates, security policies |
| Tests | `tests/` | Unit + integration + contract tests |
| Tooling | `tools/` | Validators, scripts, repo lint |
| Releases | `releases/` | Release manifests/SBOMs/attestations/telemetry snapshots |

> Some directories may not exist yet (not confirmed in repo). If a canonical root is missing, treat it as a gap and implement it per the Master Guide.

### Expected file tree

~~~text
📁 Kansas-Frontier-Matrix/
├── 📄 README.md
├── 📁 .github/
├── 📁 data/
├── 📁 docs/
├── 📁 mcp/
├── 📁 schemas/
├── 📁 src/
├── 📁 tests/
├── 📁 tools/
├── 📁 web/
└── 📁 releases/
~~~

---

## 🧭 Context

### Background

KFM’s design goal is an **evidence-first, provenance-linked** system where every downstream view (including narrative Focus Mode) remains traceable back to catalog and provenance artifacts.

### Assumptions

- Canonical pipeline ordering is preserved.
- Schemas/contracts are treated as first-class artifacts.
- Pipelines are deterministic, reproducible, and produce diffable outputs.

### Constraints and invariants

- The canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**
- The UI consumes contracted data via the API boundary only (no direct Neo4j dependency).
- Focus Mode only presents provenance-linked content (no uncited facts).
- Any AI-generated/predictive content is opt-in, clearly labeled, and includes uncertainty metadata.
- Classification/sensitivity must propagate forward: no output can be less restricted than any input in its lineage.
- For culturally sensitive materials: avoid publishing raw coordinates or re-identifying spatial precision in public artifacts; generalize/mask as required.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which paths are currently implemented vs target layout? | TBD | TBD |
| Which staging is canonical per domain: stage-first vs domain-pack? | TBD | TBD |
| Do legacy duplicate roots exist and what is the migration/deprecation plan? | TBD | TBD |
| Where is the canonical glossary located and is it complete? | TBD | TBD |
| Which CI validators exist today (Markdown protocol, schema lint, contract tests, link checks)? | TBD | TBD |
| Confirm Story Node publish workflow (`draft/` vs `published/`) and any legacy path. | TBD | TBD |
| Are domain naming conventions standardized (kebab-case vs snake_case)? | TBD | TBD |

### Future extensions

- New domains built as domain packs: inputs + ETL + catalogs + graph + API + UI + Story Node.
- New evidence products treated as catalog assets and linked into Focus Mode.
- Expanded Story Node types (schema-validated; provenance-linked).
- Composite CI actions and reproducibility kits (if adopted) to standardize validation and regression testing.

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
  F --> G["Focus Mode — provenance-linked"]
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

- Preferred staging model (baseline):
  - `data/raw/<domain>/` — immutable source snapshots
  - `data/work/<domain>/` — intermediate transforms
  - `data/processed/<domain>/` — normalized outputs used for catalogs and graph ingest
- Optional domain module home for governance/runbooks:
  - `data/<domain>/governance/` and `data/<domain>/README.md` (recommended)
- Upstream source manifests (recommended):
  - `data/sources/**` (or repo-approved equivalent) containing source ID, license, providers, spatial/temporal extent, and provenance pointers.

### Outputs

- Global evidence artifacts:
  - STAC: `data/stac/collections/` + `data/stac/items/`
  - DCAT: `data/catalog/dcat/`
  - PROV: `data/prov/`
- Graph import fixtures (if used): `data/graph/**`
- Downstream consumers:
  - Graph ingest references STAC/DCAT/PROV IDs.
  - API responses include provenance references and apply redaction/generalization.
  - UI renders evidence and Story Nodes with citations and disclosure flags.

### Sensitivity and redaction

- Public artifacts must not reveal restricted locations or culturally sensitive knowledge.
- Apply generalization/redaction at the earliest safe boundary:
  - geometry generalization in catalog outputs when required,
  - API-level redaction for sensitive fields and precision,
  - Story Node asset review gates before publication.

### Quality signals

- All STAC/DCAT/PROV artifacts validate against schemas in `schemas/**`.
- No orphan references: entity refs, evidence refs, and Story Node refs resolve.
- Deterministic runs and diffable outputs; stable IDs and versioned artifacts.
- Provenance is complete enough to answer: what changed, why, when, and by what process.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

For each dataset/evidence product:
- STAC Collection + Item(s) exist and validate.
- Items reference assets and (where permitted) geometry; geometry may be generalized for public release.

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

- IDs are stable; versions are explicit.
- Backward-incompatible changes require schema/contract version bumps.
- Catalogs and graph should link predecessor/successor versions where applicable.

---

## 🧱 Architecture

### Components

- **ETL / pipelines:** deterministic transforms in `src/pipelines/**`
- **Catalogs:** STAC/DCAT/PROV evidence in `data/**`
- **Graph:** ontology-aligned ingest in `src/graph/**` with fixtures in `data/graph/**`
- **API boundary:** contracted REST/GraphQL interface in `src/server/**`
- **UI:** `web/**` renders map and Focus Mode from API payloads
- **Story Nodes:** `docs/reports/story_nodes/**` for provenance-linked narratives
- **Telemetry/security/governance:** docs + schemas to keep behavior auditable

### Interfaces and contracts

- Governed docs: `docs/templates/**`
- JSON schemas: `schemas/**` (STAC, DCAT, PROV, story nodes, UI registries, telemetry)
- API contracts: `src/server/contracts/**` (or repo-defined equivalent)
- UI registries: schema-validated layer registries under `web/**` and `schemas/ui/**`

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

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Focus Mode is a UI view over provenance-linked context returned by the API.
- The context bundle includes:
  - entity references,
  - evidence references (STAC/DCAT/PROV),
  - disclosure flags (redaction/generalization applied).

### Provenance-linked narrative rule

- Story Nodes must cite:
  - graph entity IDs,
  - STAC/DCAT/PROV evidence IDs,
  - local assets with attribution.
- No uncited factual claims in published Story Nodes.

### Optional structured controls

If implemented, support:
- opt-in toggles for predictive/AI content,
- uncertainty display and provenance pointers,
- audit-visible “why is this shown” explanations.

---

## 🧪 Validation & CI/CD

### Validation steps

Recommended minimum checks:

- [ ] Markdown protocol validation for governed docs
- [ ] Schema validation (STAC/DCAT/PROV, Story Nodes, UI registries, telemetry)
- [ ] Graph integrity checks when graph fixtures/mappings change
- [ ] API contract tests for `src/server/**`
- [ ] UI registry validation and accessibility checks
- [ ] Link integrity checks for docs (if tooling exists)
- [ ] Security, PII, and sovereignty scanning gates as applicable

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

---

## ⚖ FAIR+CARE & Governance

### Review gates

Changes that typically require elevated review:

- Adding new sensitive layers (restricted locations, cultural knowledge, PII)
- Introducing/changing AI-generated narrative behavior visible to users
- Adding new external data sources
- Adding new public-facing endpoints
- Changing classification/sensitivity for any artifact
- Adding UI layers that could reveal sensitive locations by interaction/zoom

### CARE and sovereignty considerations

- Identify communities impacted and protection rules.
- Use generalization/redaction for restricted locations.
- Ensure sensitive assets (images/docs) follow review gates before publication.

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
