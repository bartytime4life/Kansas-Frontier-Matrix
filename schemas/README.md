---
title: "Schemas — Contract Registry"
path: "schemas/README.md"
version: "v1.0.3"
last_updated: "2025-12-29"
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

doc_uuid: "urn:kfm:doc:schemas:readme:v1.0.3"
semantic_document_id: "kfm-schemas-readme-v1.0.3"
event_source_id: "ledger:kfm:doc:schemas:readme:v1.0.3"
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

# Schemas — Contract Registry

This folder is the **schema registry** for KFM: machine-validated contracts that define the file formats and payload shapes that are allowed to cross subsystem boundaries.

KFM is **contract-first** and **evidence-first**: producers and consumers can evolve independently, while CI fails deterministically when artifacts drift out of compliance.

The schema registry supports (and must remain aligned with) the canonical pipeline ordering:

**ETL → Catalogs (STAC/DCAT/PROV) → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

> Note: some KFM references describe the Catalogs stage as a *catalog sub-order* (STAC → DCAT → PROV) inside the single “Catalogs” boundary. The non-negotiable rule is that *catalog artifacts exist and validate before graph ingest and UI/narrative surfacing*.  

---

## 📘 Overview

### Purpose

- Provide **one canonical home** for schema contracts (no per-domain “mystery duplicates”).
- Enable repeatable validation in CI and local development to prevent **silent drift** across ETL, catalog outputs, graph ingest, API payloads, UI registries, Story Nodes, and telemetry.
- Make governance and provenance enforceable by design:
  - schemas define **what we accept** at boundaries;
  - provenance documents **how we got it**;
  - both are required for Focus Mode consumption.

### Scope

| In scope | Out of scope |
|---|---|
| JSON Schemas used to validate repo artifacts at boundaries | Implementing ETL jobs, APIs, UI features, or graph queries |
| Optional SHACL shape bundles if adopted by the repo | Defining or generating governance policy (policy lives under `docs/governance/`) |
| Schema versioning, deprecation expectations, and validation boundaries | Hosting raw or processed data, or catalog outputs (these live under `data/`) |

### Audience

- Primary: schema maintainers, catalog maintainers, CI/workflow maintainers
- Secondary: domain contributors adding datasets, Story Node authors/editors, UI maintainers, API maintainers

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo; recommended)*

Terms used in this doc:

- **Contract:** a machine-validated schema/spec that producers and consumers agree on.
- **Schema family:** a logical group of schemas for a boundary (STAC, DCAT, PROV, story nodes, UI registries, telemetry).
- **Producer:** subsystem that emits an artifact (ETL, catalog builder, Story Node publish step, UI config author, API runtime, etc.).
- **Consumer:** subsystem that reads an artifact (graph ingest, API, UI runtime, Focus Mode, audit tools).
- **Boundary validation:** validate an artifact as soon as it is produced, before any downstream system accepts it.
- **Profile:** a governed standardization layer (e.g., KFM-STAC/KFM-DCAT/KFM-PROV). Schemas are the executable enforcement of those profiles.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | Core | Canonical pipeline + invariants |
| Data Intake & Ingestion Architecture | `docs/architecture/KFM_INGEST_ARCHITECTURE.md` | Data Engineering | Intake patterns + contract boundaries |
| v13 Redesign Blueprint (draft) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Canonical homes + contract-first |
| Schema registry (this area) | `schemas/` | Core | Canonical schema contracts |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Governing structure for this README |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Story | Governing structure for Story Nodes |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | Contract changes for REST/GraphQL |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs | *not confirmed in repo* |
| Provenance rules | `docs/standards/KFM_PROVENANCE_RULES.md` | Catalog | *not confirmed in repo (referenced by design docs)* |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (`path` matches file location)
- [ ] Registry invariants are documented and consistent with canonical homes
- [ ] Versioning + deprecation rules are explicit and actionable
- [ ] Validation expectations are listed and repeatable
- [ ] Governance + CARE/sovereignty triggers for schema changes are explicit
- [ ] Open questions are tracked with owners and targets

---

## 🗂️ Directory Layout

### This document

- `path`: `schemas/README.md` *(must match front-matter)*

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) |
| Data domains | `data/` | Staged data (`raw/`, `work/`, `processed/`) + published catalogs (STAC/DCAT/PROV) |
| Pipelines | `src/pipelines/` | ETL + catalog generation code |
| Tools | `tools/` | Validators, utilities, QA scripts |
| Graph | `src/graph/` | Ontology bindings + ingest/migrations + integrity constraints |
| API boundary | `src/server/` | API service + contracts + redaction/generalization logic |
| UI | `web/` | React + map client + Focus Mode UI |
| Story Nodes | `docs/reports/story_nodes/` *(pattern)* | Draft + published story nodes (if used) |
| MCP runs/experiments | `mcp/` | Runs, experiments, model cards, SOPs |
| Tests | `tests/` | Unit + integration tests |
| CI | `.github/` | Workflows + policy gates |
| Releases | `releases/` | Versioned packaged artifacts (if used) |

### Expected file tree for this sub-area

~~~text
📁 schemas/
├── 📄 README.md
├── 📁 stac/
├── 📁 dcat/
├── 📁 prov/
├── 📁 story_nodes/
├── 📁 ui/
├── 📁 telemetry/
└── 📁 shacl/                              # optional; only if adopted
~~~

### Minimum contract set

The minimum contract set for “pipeline-complete” schema coverage is:

- `schemas/stac/` — STAC JSON Schemas plus KFM constraints
- `schemas/dcat/` — DCAT constraints and shape bundles as needed
- `schemas/prov/` — PROV constraints and profiles
- `schemas/story_nodes/` — Story Node schema
- `schemas/ui/` — UI layer registry schema(s)
- `schemas/telemetry/` — telemetry schemas used by CI and runs

### What belongs in each folder

| Folder | What it holds | Primary producers | Primary consumers |
|---|---|---|---|
| `schemas/stac/` | STAC collection/item validation schemas + KFM constraints | Catalog build stage | Graph ingest, API, UI |
| `schemas/dcat/` | DCAT dataset/distribution validation constraints | Catalog build stage | API, external catalog export |
| `schemas/prov/` | PROV validation constraints (JSON-LD or other repo-chosen encoding) | ETL + catalog stages | Audit, reproducibility, Focus Mode |
| `schemas/story_nodes/` | Story Node validation schemas (front-matter + structure) | Story Node publish workflow | Story publishing, Focus Mode |
| `schemas/ui/` | UI registry schemas for layer/config files | UI maintainers | UI build + runtime |
| `schemas/telemetry/` | Telemetry/event schemas (CI + runtime) | ETL/API/UI | CI quality gates, monitoring, governance signals |
| `schemas/shacl/` | Optional SHACL shapes (if adopted) | Graph/ontology | Graph validation/audit |

### Registry invariants (must not regress)

- **Schemas and specs live here** (`schemas/`). Do not create per-domain schema registries.
- **API contracts live at the API boundary** (`src/server/`), not in `schemas/`.
  - Example locations (if present): `src/server/openapi.yaml` (REST), GraphQL SDL files (GraphQL).
- **Data outputs are not code**: derived datasets and catalogs must not be written into `src/` or `docs/`.
- **Pipelines never write STAC/DCAT/PROV into `docs/`**.
- **No YAML front-matter in code files**: JSON Schemas and shape bundles must not use YAML front-matter.
- **Fail closed at boundaries**: validate artifacts where they are produced; consumers assume validated input.
- **Breaking changes require versioning**: breaking schema changes require a clear version bump + migration/compat plan.

### Schema authoring conventions (recommended defaults)

These conventions improve determinism and resolver stability. If the repo already has stricter rules, the stricter rules win.

- **Resolver stability:** prefer local `$ref` targets that resolve inside the repo (no network-required refs unless explicitly allowlisted).
- **Uniqueness:** if using `$id`, ensure uniqueness within the registry (and avoid changing `$id` once published).
- **Version traceability:** schema files and/or directories should make version provenance obvious (SemVer per family recommended).
- **Fixtures:** maintain at least one valid and one invalid fixture per new/changed contract *(fixture convention not confirmed in repo)*.

---

## 🧭 Context

### Background

KFM’s repository structure is not aesthetic—it is a compliance mechanism. The system relies on deterministic contract enforcement so that:

- catalog outputs can be trusted as evidence products,
- ingest into the graph is controlled and repeatable,
- the API can enforce redaction/generalization without ambiguity,
- the UI and Focus Mode can render only provenance-linked narrative.

### Assumptions

- Neo4j remains the primary graph database.
- STAC, DCAT, and PROV remain first-class and required for datasets and evidence products.
- The UI is a React-based web app and must not connect to Neo4j directly.

### Constraints / invariants

Non-negotiables across the system that schemas help enforce:

1. **Pipeline ordering is non-negotiable**
   - ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode
2. **No UI direct-to-graph reads**
   - `web/` must not query Neo4j directly; all graph access is via `src/server/`.
3. **No unsourced narrative**
   - Published Story Nodes must be provenance-linked and must validate.
4. **Contracts are canonical**
   - Schemas/specs must live in `schemas/` and API contracts under `src/server/`; both must validate in CI.
5. **Classification must not downgrade**
   - No output may be less restricted than any upstream input in its lineage (classification propagation).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What JSON Schema draft/version is canonical for KFM validation tooling? | Contracts owners | v13.0.0 |
| Do we publish schemas as packages (npm/pip) or keep schemas repo-local only? | Core maintainers | v13.1.0 |
| Do we adopt SHACL for graph validation, and if so, where is it enforced? | Catalog + graph owners | v13.1.0 |
| Where are schema change logs recorded (per family or global)? | Docs + contracts owners | v13.0.0 |
| Which artifact families must have fixtures, and where do fixtures live? | CI + contracts owners | v13.0.0 |

### Future extensions

- Schema coverage for graph ingest fixtures (CSV/Cypher) *(not confirmed in repo)*.
- Contracted “evidence products” beyond catalogs (e.g., derived AI evidence artifacts published as STAC assets).
- Typed redaction/generalization policies bound to schema fields (governance review required).

---

## 🗺️ Diagrams

### System and contract boundaries

~~~mermaid
flowchart LR
  A[ETL<br/>src/pipelines] --> B[Catalogs<br/>data/stac + data/catalog/dcat + data/prov]
  B --> C[Graph Ingest<br/>src/graph]
  C --> D[APIs<br/>src/server]
  D --> E[UI<br/>web]
  E --> F[Story Nodes<br/>docs/reports/story_nodes]
  F --> G[Focus Mode<br/>provenance-linked only]

  S[schemas/] --> B
  S --> C
  S --> D
  S --> E
  S --> F
~~~

### Validation boundary pattern

~~~mermaid
flowchart TB
  P1[Producer emits artifact] --> V1[Validate against schema]
  V1 -->|valid| C1[Consumer accepts artifact]
  V1 -->|invalid| F1[Fail closed: block publish/ingest]

  subgraph Examples
    X1[Catalog emits STAC JSON] --> X2[Validate STAC schema] --> X3[Graph ingest reads STAC]
    Y1[Story author edits Story Node] --> Y2[Validate story node schema] --> Y3[Publish step]
    Z1[UI registry updated] --> Z2[Validate UI registry schema] --> Z3[UI build/runtime]
  end
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Standard profiles and constraints | Markdown | `docs/standards/` | Human review + link checks |
| Contract schemas | JSON / SHACL | `schemas/**` | Schema lint + CI contract checks |
| Reference artifacts (fixtures) | JSON / MD | `data/**`, `web/**`, `docs/reports/story_nodes/**` | Validated against schemas |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Schema contracts | JSON / SHACL | `schemas/**` | This registry |
| Validation results | logs / manifests | `mcp/runs/**` and/or `data/prov/**` | Tooling-specific |

### Sensitivity & redaction

Schemas influence what can be produced and what can be displayed. Treat schema changes as governance-relevant if they affect:

- location precision,
- redaction/generalization behavior,
- attribution fields,
- fields that could enable inference of sensitive locations or protected community data.

> Implementation note (optional): schema property metadata can support field-level sensitivity tagging for downstream redaction at the API boundary.

### Quality signals

Schema quality is part of system quality. Recommended signals for schema changes:

- **Reference resolvability:** all `$ref` targets resolve in CI (avoid network-required refs unless explicitly allowed).
- **Uniqueness:** `$id` values are unique within the registry (if used).
- **Compatibility impact:** PR declares whether changes are breaking (major) vs additive (minor) vs patch.
- **Fixture coverage:** at least one valid and one invalid fixture per new/changed contract *(fixture convention not confirmed in repo)*.

### Provenance hooks

Where possible, run manifests and provenance bundles should capture:

- schema family and schema version used to validate each artifact,
- validator tool and version,
- timestamp and result (pass/fail),
- link to schema file(s) used (or schema package version if packaged).

---

## 🌐 STAC, DCAT & PROV Alignment

Schemas in this registry align to KFM profiles and enforce boundary validity before downstream ingest.

### STAC

- Output location:
  - Collections: `data/stac/collections/`
  - Items: `data/stac/items/`
- Validation:
  - Validate JSON structure and required fields at catalog build time.
  - Validate KFM-specific constraints (extensions, identifiers, asset conventions) via KFM schema overlays.

### DCAT

- Output location:
  - `data/catalog/dcat/`
- Validation:
  - Validate dataset/distribution metadata required for discovery, reuse, and external federation.

### PROV-O

- Output location:
  - `data/prov/`
- Validation:
  - Validate lineage bundles that connect raw → work → processed → catalog outputs and publish steps.

### Versioning & deprecation policy (schemas)

Schemas follow semantic versioning: any change that breaks consumers triggers a version bump and a changelog entry.

- **SemVer applies per schema family (recommended):**
  - **MAJOR**: breaking change (required field added, renamed, type changed, tightened constraints that invalidate existing artifacts).
  - **MINOR**: backwards-compatible addition (new optional fields, new schema definitions, new allowed enum values).
  - **PATCH**: non-functional fixes (typos, clarifications, metadata updates, docs).
- **Deprecation:**
  - Mark deprecated fields/contracts explicitly in schema comments/metadata (mechanism depends on chosen JSON Schema draft).
  - Maintain deprecated fields for at least one MINOR release unless governance requires immediate removal.
  - Provide a migration note and (if feasible) an auto-migration script *(tooling path not confirmed in repo)*.
- **Compatibility tests:**
  - For MAJOR changes, include fixtures showing: previous version fails where expected, new version passes, and migration path is documented.

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Schema registry (`schemas/`) | Contract definitions for artifacts | JSON Schema + optional SHACL |
| Producers | Emit artifacts at boundaries | ETL outputs, catalogs, Story Nodes, UI registries, telemetry |
| Validators | Enforce contract compliance | CI jobs + local scripts |
| Consumers | Read artifacts | Graph ingest, API, UI runtime, Focus Mode, audit tools |

### Interfaces / contracts

| Contract type | Canonical location | Versioning rule |
|---|---|---|
| Data output schemas | `schemas/` | SemVer (per family) + changelog |
| API contracts | `src/server/` | Contract tests required |
| UI layer registry schemas | `schemas/ui/` | Validate before build/runtime |
| Story Node schemas | `schemas/story_nodes/` | Publish must validate |
| Telemetry schemas | `schemas/telemetry/` | Contracted signals for CI/governance |

### Extension points checklist (for future work)

- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] DCAT: dataset/distribution validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Story Nodes: schema updates + publish validation
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

Story Nodes are governed narrative artifacts:

- they must validate structurally,
- they must reference provenance-linked evidence,
- they must connect to entities in the graph by stable identifiers.

### Provenance-linked narrative rule

Focus Mode only consumes provenance-linked content:

- any predictive or AI-generated content must be opt-in,
- must include uncertainty metadata,
- must never appear as unmarked fact,
- must never infer or reveal sensitive locations.

### Optional structured controls

The Story Node schema may define structured “Focus Mode controls” for UI behavior. Any such fields must be schema-defined and validated.

~~~yaml
# Illustrative placeholders only; actual supported fields are defined by schemas/story_nodes/**
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

---

## 🧪 Validation & CI/CD

### Validation steps (minimum gates)

- [ ] Markdown protocol validation (front-matter + required sections)
- [ ] Link/reference checks (no orphan pointers)
- [ ] JSON schema validation:
  - [ ] STAC (`data/stac/**` vs `schemas/stac/**`)
  - [ ] DCAT (`data/catalog/dcat/**` vs `schemas/dcat/**`)
  - [ ] PROV (`data/prov/**` vs `schemas/prov/**`)
  - [ ] Story Nodes (`docs/reports/story_nodes/**` vs `schemas/story_nodes/**`) *(if present)*
  - [ ] UI layer registries (`web/**` vs `schemas/ui/**`) *(if present)*
  - [ ] Telemetry payloads (`mcp/**` and/or logs vs `schemas/telemetry/**`) *(if present)*
- [ ] Graph integrity tests (constraints, expected labels/edges) *(if present)*
- [ ] API contract tests (`src/server/**`) *(if present)*
- [ ] Security + sovereignty scanning gates (as applicable):
  - [ ] secret scan
  - [ ] PII scan
  - [ ] sensitive-location leakage checks
  - [ ] classification propagation checks (no downgrades without review)

### Deterministic CI behavior

- If a schema-governed root exists and artifacts are invalid, CI must **fail**.
- If a check is not applicable to a change, CI may **skip** cleanly.
- Consumers should only accept **validated** artifacts.

### Repo lint rules (recommended)

Enforce:

- no YAML front-matter in code files,
- no duplicate canonical homes without explicit deprecation markers.

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands and tools

# 1) validate schemas (lint + $ref resolution)
# ./scripts/validate_schemas.sh

# 2) validate schema-governed artifacts (catalogs, story nodes, ui registries, telemetry)
# ./scripts/validate_all_catalogs.sh

# 3) run tests + contract checks
# pytest -q

# 4) run doc lint / link checks
# markdownlint docs/ schemas/ && ./scripts/check_links.sh
~~~

### Telemetry signals (recommended)

| Signal | Source | Where recorded |
|---|---|---|
| `classification_assigned` (dataset_id, sensitivity, classification) | ETL / catalog / governance | `mcp/runs/**` + `schemas/telemetry/**` |
| `redaction_applied` (method, fields_removed, geometry_generalization) | API boundary / ETL | `mcp/runs/**` + `schemas/telemetry/**` |
| `promotion_blocked` (reason, scan_results_ref) | CI / governance | `mcp/runs/**` + `schemas/telemetry/**` |
| `catalog_published` (scope, counts, validation_status) | Catalog stage | `mcp/runs/**` + `schemas/telemetry/**` |
| `focus_mode_redaction_notice_shown` (layer_id, redaction_method) | UI | `mcp/runs/**` + `schemas/telemetry/**` |

---

## ⚖ FAIR+CARE & Governance

### Review gates

Schema changes require careful review when they affect:

- what becomes public-facing,
- what becomes inferable (especially locations and protected community data),
- redaction/generalization behavior,
- API payload expectations that UI depends on.

### CARE / sovereignty considerations

- If a schema enables higher-precision locations, expands identity-revealing fields, or reduces redaction, treat the change as sovereignty-sensitive and require governance review.
- Prefer conservative defaults; explicitly document exceptions under governance.
- **No output may be less restricted than any upstream input** in its lineage.

### AI usage constraints

This document’s front matter sets the allowed and prohibited AI transforms. Schema content must not be used as a backdoor to create policy; policy belongs under `docs/governance/`.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-27 | Initial `schemas/` README establishing schema registry layout and contract rules | (you) |
| v1.0.1 | 2025-12-28 | Align schema subtree naming (`story_nodes/`), add versioning/deprecation policy + open questions | (you) |
| v1.0.2 | 2025-12-28 | Align to Universal Doc template sections, add CI gates + telemetry signals, tighten invariants | (you) |
| v1.0.3 | 2025-12-29 | Align contract boundaries with intake/design docs; clarify “Catalogs” boundary and schema authoring conventions | (you) |

---

Footer refs:
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Data Intake & Ingestion Architecture: `docs/architecture/KFM_INGEST_ARCHITECTURE.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`