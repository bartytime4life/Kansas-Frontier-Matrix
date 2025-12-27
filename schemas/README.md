---
title: "Schemas — Contract Registry"
path: "schemas/README.md"
version: "v1.0.0"
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

doc_uuid: "urn:kfm:doc:schemas:readme:v1.0.0"
semantic_document_id: "kfm-schemas-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:schemas:readme:v1.0.0"
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

This folder is the **schema registry** for KFM: machine-validated contracts that define file formats and interface payloads at key pipeline boundaries.

KFM is contract-first and evidence-first. Schemas exist so producers and consumers can evolve independently while CI fails deterministically when artifacts are invalid.

## 📘 Overview

### Purpose

- Provide a single canonical home for **data-output schemas** (STAC/DCAT/PROV), **Story Node schemas**, **UI registry schemas**, and **telemetry schemas**.
- Enable repeatable validation in CI and in local dev to prevent “silent drift” across ETL, catalogs, graph ingest, APIs, and UI.

### Scope

| In scope | Out of scope |
|---|---|
| JSON Schemas and optional shape bundles used to validate repo artifacts | Implementing ETL jobs, APIs, or UI features |
| Folder conventions, schema versioning expectations, and validation boundaries | Defining new governance policy (policy lives under `docs/governance/`) |
| Guidance for adding/updating schemas and wiring validators | Hosting raw data, processed data, or catalog outputs (those live under `data/`) |

### Audience

- Primary: schema maintainers, pipeline/catalog maintainers, CI maintainers
- Secondary: domain contributors adding datasets, Story Node authors/editors, UI maintainers

### Definitions

- Glossary reference: `docs/glossary.md` (**not confirmed in repo** — create or update link if absent)
- Terms used here:
  - **Contract**: a machine-validated schema/spec that producers and consumers agree on.
  - **Producer**: the subsystem that emits an artifact (ETL, catalog builder, UI config author, etc.).
  - **Consumer**: the subsystem that reads an artifact (graph ingest, API, UI runtime, Focus Mode, etc.).
  - **Boundary validation**: validating an artifact as soon as it crosses a subsystem boundary.
  - **Schema version**: semantic version identifier tied to a schema’s meaning and compatibility.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline + invariants |
| Redesign blueprint (v13) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Maintainers | Canonical roots + minimum contract set |
| This registry | `schemas/README.md` | Schema maintainers | Explains schema layout + usage |
| STAC outputs | `data/stac/` | Catalog stage | Collections + Items |
| DCAT outputs | `data/catalog/dcat/` | Catalog stage | Dataset records |
| PROV lineage bundles | `data/prov/` | ETL + catalog | Provenance for runs and artifacts |
| API contracts | `src/server/contracts/` (**or repo-defined equivalent**) | API maintainers | OpenAPI / GraphQL specs live outside `schemas/` |
| Story Nodes | `docs/reports/story_nodes/` | Story editors | Draft + published nodes |
| UI app + registries | `web/` | UI maintainers | UI configs must validate against UI schemas |

### Definition of done

- [ ] Front-matter complete and consistent with path/version
- [ ] Minimum contract set folder layout is documented and understandable
- [ ] Schema versioning rules are explicit and actionable
- [ ] Validation steps are listed and repeatable
- [ ] Governance and CARE/sovereignty considerations are stated where relevant
- [ ] Open questions are tracked with owners

## 🗂️ Directory Layout

### This document

- `path`: `schemas/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| ETL and catalog code | `src/pipelines/` | Ingest + normalize + produce derived artifacts |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Standardized discovery + provenance |
| Graph ingest | `src/graph/` and `data/graph/` | Ontology bindings + import artifacts |
| API boundary | `src/server/` | APIs expose graph/data to UI; contracts under `src/server/contracts/` |
| UI boundary | `web/` | React + map clients; no direct graph access |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published narrative nodes |
| CI workflows | `.github/workflows/` | Validation gates |
| Reproducibility evidence | `mcp/runs/` | Run manifests + pointers to provenance |

### Minimum contract set

Organize schemas into these canonical roots:

~~~text
📁 schemas/
├── 📄 README.md
├── 📁 stac/
├── 📁 dcat/
├── 📁 prov/
├── 📁 storynodes/
├── 📁 ui/
└── 📁 telemetry/
~~~

Suggested contents by folder:

| Folder | What it holds | Primary producers | Primary consumers |
|---|---|---|---|
| `schemas/stac/` | STAC schemas + KFM constraints | Catalog build stage | Graph ingest, API, UI |
| `schemas/dcat/` | DCAT constraints + any required shape bundles | Catalog build stage | API, external catalogs |
| `schemas/prov/` | PROV constraints/profiles | ETL + catalog stages | Audit, reproducibility, Focus Mode |
| `schemas/storynodes/` | Story Node validation schemas | Story Node authors/editors | Story publishing, Focus Mode |
| `schemas/ui/` | UI registry schemas | UI maintainers | UI build + runtime config |
| `schemas/telemetry/` | Telemetry/event schemas | ETL, API, UI | CI quality gates, monitoring |

Optional extensions (allowed, but not part of the minimum contract set):

- `schemas/shacl/` for SHACL shape bundles (**not confirmed in repo**)
- `schemas/common/` for shared definitions across schema families (**not confirmed in repo**)

### Schema naming and versioning conventions

Schema changes must be versioned. Recommended practices:

- Use semantic versioning for schema meaning:
  - **Major**: breaking change (consumer updates required)
  - **Minor**: backward-compatible additions (new optional fields, relaxed constraints)
  - **Patch**: non-semantic fixes (typos, metadata changes, refactor with identical validation)
- Keep a changelog for schema evolution:
  - Option A: `schemas/CHANGELOG.md` (**not confirmed in repo**)
  - Option B: per-schema `CHANGELOG.md` inside each root (e.g., `schemas/stac/CHANGELOG.md`)

Recommended schema metadata (for JSON Schema files):

- `$id` (stable identifier)
- `title`, `description`
- A machine-readable version field (either inside schema or in filename)
- Clear compatibility notes (breaking vs non-breaking)

## 🧭 Context

### Background

KFM’s canonical pipeline ordering is preserved:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

Schemas are the enforcement mechanism for “contract-first” behavior: artifacts must be valid at the boundary where they are produced.

### Assumptions

- The folders in the minimum contract set exist (even if some are empty placeholders).
- If a referenced path is missing in a given checkout, treat it as **not confirmed in repo** and either:
  - add the canonical path and link to it, or
  - update this README to point to the repo’s true canonical location.

### Constraints and invariants

- UI must not read Neo4j directly. All graph access is mediated by the API boundary.
- Documentation and Story Nodes must not introduce unsourced narrative.
- Schema validation should fail deterministically:
  - if schema roots are present but invalid, CI should fail,
  - if optional roots are absent, CI should skip cleanly.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which JSON Schema dialect and validator are canonical (AJV, check-jsonschema, other)? | TBD | TBD |
| Where should SHACL shapes live if adopted (`schemas/shacl/` vs per-domain)? | TBD | TBD |
| Do we want generated types (TypeScript/Python) from schemas, and where do they live? | TBD | TBD |
| What is the canonical location for schema changelogs? | TBD | TBD |

### Future extensions

- Add a small “schema registry index” file to enumerate canonical schema IDs and versions (**not confirmed in repo**).
- Add fixtures for schema validation under `tests/fixtures/` (**not confirmed in repo**).
- Add schema-driven type generation for API and UI consumers (**not confirmed in repo**).

## 🗺️ Diagrams

### System and contract boundaries

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Graph Ingest]
  C --> D[APIs]
  D --> E[UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]

  S[schemas/] --> B
  S --> C
  S --> D
  S --> E
  S --> F
~~~

### Validation boundaries

~~~mermaid
flowchart TB
  P1[Producer emits artifact] --> V1[Validate against schema]
  V1 -->|valid| C1[Consumer accepts artifact]
  V1 -->|invalid| F1[Fail closed: block publish/ingest]

  subgraph Examples
    X1[Catalog emits STAC JSON] --> X2[Validate STAC schema] --> X3[Graph ingest reads STAC]
    Y1[Story author edits Story Node] --> Y2[Validate story node schema] --> Y3[Publish step]
    Z1[UI layer registry updated] --> Z2[Validate UI registry schema] --> Z3[UI build/runtime]
  end
~~~

## 📦 Data and Metadata

### Inputs

Schemas in this directory are used to validate artifacts such as:

- STAC Collections and Items (`data/stac/**`)
- DCAT dataset records (`data/catalog/dcat/**`)
- PROV bundles (`data/prov/**`)
- Story Node metadata extracted at publish time (`docs/reports/story_nodes/**`)
- UI registry/config files (`web/**`)
- Telemetry/event payloads emitted by pipeline/API/UI systems

### Outputs

This folder produces:

- A versioned set of schemas used by validators
- A stable contract surface for producers/consumers
- A reviewable set of “what we accept” constraints for audit and governance

### Provenance hooks

Where possible, capture:

- schema version used to validate each artifact,
- validator tool/version,
- validation timestamp and result,
in run manifests and/or provenance bundles.

## 🧩 STAC/DCAT/PROV Alignment

Schemas support the catalog stage and are aligned to KFM profiles:

| Standard family | Output location | Schema root | Notes |
|---|---|---|---|
| STAC | `data/stac/` | `schemas/stac/` | Used to validate Collections and Items before graph ingest |
| DCAT | `data/catalog/dcat/` | `schemas/dcat/` | Used to validate discovery metadata for non-map consumers |
| PROV | `data/prov/` | `schemas/prov/` | Used to validate lineage for audit, reproducibility, and Focus Mode |

Note:
- The profiles referenced in front-matter (`KFM-STAC`, `KFM-DCAT`, `KFM-PROV`) define constraints that schemas implement.
- If profile documents are missing or incomplete, treat those paths as **not confirmed in repo** and add the canonical profile docs before tightening schemas.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Schema registry (`schemas/`) | Contract definitions for artifacts | JSON Schema files and optional shape bundles |
| Producers | Emit artifacts at boundaries | ETL outputs, catalogs, Story Nodes, UI registries, telemetry events |
| Validators | Enforce contract compliance | CI jobs and local scripts (**validator tooling not confirmed in repo**) |
| Consumers | Read artifacts | Graph ingest, API, UI runtime, Focus Mode |

### Interfaces and contract locations

Representative contract locations across the repo:

| Contract type | Canonical location | Versioning rule |
|---|---|---|
| Data output schemas | `schemas/` | semantic versioning + changelog |
| API schemas (OpenAPI/GraphQL) | `src/server/` + `src/server/contracts/` (**or repo-defined equivalent**) | versioned APIs + contract tests |
| UI layer registry | `web/` (layer config files) | validated against `schemas/ui/` |

## ⚙️ Validation and CI/CD

### Validation steps

Recommended checks when schemas or schema-governed artifacts change:

- Markdown protocol validation for governed docs (including this README)
- Schema syntax validation (JSON Schema parse/lint)
- Artifact validation:
  - STAC JSON against `schemas/stac/`
  - DCAT records against `schemas/dcat/`
  - PROV bundles against `schemas/prov/`
  - Story Node publish validation using `schemas/storynodes/` (typically applied to extracted metadata representation)
  - UI registry config validation using `schemas/ui/`
  - Telemetry payload validation using `schemas/telemetry/`
- Secrets/PII scanning and sovereignty gates where configured

Example command patterns (illustrative only — tooling not confirmed in repo):

~~~bash
# Validate a JSON artifact against a schema (tooling not confirmed in repo)
# check-jsonschema --schemafile schemas/stac/<schema>.json data/stac/items/<item>.json

# Validate UI registry config (tooling not confirmed in repo)
# check-jsonschema --schemafile schemas/ui/<layer-registry>.json web/<layers>.json
~~~

### CI expectations

Minimum CI gates for “v13 readiness” should include:

- Markdown protocol validation
- Schema validation
- Story Node validation
- API contract tests
- Security and sovereignty scanning gates

CI should fail deterministically when schema roots exist but contain invalid schemas or invalid governed artifacts.

## ⚖ FAIR+CARE and Governance

Schemas influence what can be produced, published, and displayed. Treat schema changes as governance-relevant when they affect:

- redaction rules,
- classification sensitivity,
- location precision requirements,
- fields that could enable inference of sensitive locations or protected community data.

AI usage constraints for this document and this repo area:

- Allowed: summarization, structure extraction, translation, keyword indexing
- Prohibited: generating new policy, inferring sensitive locations

## 🧾 Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-27 | Initial `schemas/` README establishing schema registry layout and contract rules | (you) |

---

Footer refs:
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
