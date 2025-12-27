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

This folder is the **schema registry** for KFM: machine-validated contracts that define the file formats and payload shapes that are allowed to cross subsystem boundaries.

KFM is **contract-first** and **evidence-first**. Schemas exist so producers and consumers can evolve independently while CI fails deterministically when artifacts drift out of compliance.

The schema registry supports (and must remain aligned with) the canonical pipeline ordering:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

---

## 📘 Overview

### Purpose

- Provide **one canonical home** for schema contracts (no per-domain “mystery duplicates”).
- Enable repeatable validation in CI and local development to prevent **silent drift** across ETL, catalog outputs, graph ingest, API payloads, UI registries, Story Nodes, and telemetry.
- Make governance and provenance enforceable by design:
  - schemas define “what we accept”;
  - provenance documents “how we got it”;
  - both are required for Focus Mode consumption.

### Scope

| In scope | Out of scope |
|---|---|
| JSON Schemas used to validate repo artifacts at boundaries | Implementing ETL jobs, APIs, UI features, or graph queries |
| Optional SHACL shape bundles if adopted by the repo | Defining new governance policy (policy lives under `docs/governance/`) |
| Schema versioning, deprecation expectations, and validation boundaries | Hosting raw data, processed data, or catalog outputs (these live under `data/`) |

### Audience

- Primary: schema maintainers, catalog maintainers, CI/workflow maintainers
- Secondary: domain contributors adding datasets, Story Node authors/editors, UI maintainers, API maintainers

### Definitions

- **Contract:** a machine-validated schema/spec that producers and consumers agree on.
- **Schema family:** a logical group of schemas for a boundary (STAC, DCAT, PROV, story nodes, UI registries, telemetry).
- **Producer:** subsystem that emits an artifact (ETL, catalog builder, Story Node publish step, UI config author, API runtime, etc.).
- **Consumer:** subsystem that reads an artifact (graph ingest, API, UI runtime, Focus Mode, audit tools).
- **Boundary validation:** validate an artifact as soon as it is produced, before any downstream system accepts it.
- **Profile:** a governed standardization layer (e.g., KFM-STAC/KFM-DCAT/KFM-PROV). Schemas are the executable enforcement of those profiles.

Glossary reference:
- `docs/glossary.md` (**not confirmed in repo** — create or update link if absent)

### Key artifacts and canonical homes

| Artifact | Canonical path | Notes |
|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | Canonical pipeline + invariants |
| v13 Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Canonical roots + minimum contract set |
| Schema registry | `schemas/` | This folder |
| STAC outputs | `data/stac/collections/` and `data/stac/items/` | Catalog stage outputs (validate before graph ingest) |
| DCAT outputs | `data/catalog/dcat/` | Catalog stage outputs |
| PROV bundles | `data/prov/` | ETL + catalog provenance outputs |
| Graph ingest artifacts | `data/graph/` | Import fixtures (CSV/Cypher) as defined by graph subsystem |
| API boundary | `src/server/` | UI must access graph via APIs (no direct graph reads) |
| API contracts | `src/server/contracts/` | OpenAPI / GraphQL contracts |
| UI layer registries | `web/` | Configs validate against `schemas/ui/` |
| Story Nodes | `docs/reports/story_nodes/` | Draft + published nodes must validate |
| Telemetry docs | `docs/telemetry/` | Pairs with `schemas/telemetry/` |

### Quickstart for common changes

- Adding a new dataset:
  - you likely need schema-governed outputs under `data/stac/**`, `data/catalog/dcat/**`, and `data/prov/**`.
- Adding a new UI layer registry entry:
  - update the UI registry file(s) under `web/` and ensure they validate against `schemas/ui/`.
- Adding a new Story Node field:
  - update `schemas/storynodes/` and ensure publish-time validation remains deterministic.
- Adding a new telemetry signal:
  - define the event shape under `schemas/telemetry/` and document it under `docs/telemetry/`.

### Definition of done

- [ ] This README front-matter is complete and `path` matches file location
- [ ] The minimum contract set is documented and consistent with canonical homes
- [ ] Versioning + deprecation rules are explicit and actionable
- [ ] Validation expectations are listed and repeatable
- [ ] Governance / CARE / sovereignty triggers are documented for schema changes
- [ ] Open questions are tracked with owners and next actions

---

## 🗂️ Directory Layout

### This document

- `path`: `schemas/README.md`

### Minimum contract set

The minimum contract set for v13 readiness is:

- `schemas/stac/` — STAC JSON Schemas plus KFM constraints  
- `schemas/dcat/` — DCAT constraints and shape bundles as needed  
- `schemas/prov/` — PROV constraints and profiles  
- `schemas/storynodes/` — Story Node schema  
- `schemas/ui/` — UI layer registry schema  
- `schemas/telemetry/` — telemetry schemas used by CI and runs

Expected layout:

~~~text
📁 schemas/
├── 📄 README.md
├── 📁 stac/
├── 📁 dcat/
├── 📁 prov/
├── 📁 storynodes/
├── 📁 ui/
├── 📁 telemetry/
└── 📁 shacl/                  (optional; not confirmed in repo)
~~~

### What belongs in each folder

| Folder | What it holds | Primary producers | Primary consumers |
|---|---|---|---|
| `schemas/stac/` | STAC collection/item validation schemas + KFM constraints | Catalog build stage | Graph ingest, API, UI |
| `schemas/dcat/` | DCAT dataset/distribution validation constraints | Catalog build stage | API, external catalog export |
| `schemas/prov/` | PROV validation constraints (JSON-LD or other repo-chosen encoding) | ETL + catalog stages | Audit, reproducibility, Focus Mode |
| `schemas/storynodes/` | Story Node validation schemas (front-matter + structure) | Story Node authors/publish workflow | Story publishing, Focus Mode |
| `schemas/ui/` | UI registry schemas for layer/config files | UI maintainers | UI build + runtime |
| `schemas/telemetry/` | Telemetry/event schemas | ETL/API/UI | CI quality gates, monitoring, governance signals |

### Registry invariants

- **Schemas and specs live here** (`schemas/`). Do not create per-domain schema registries.
- **API contracts live at the API boundary** (`src/server/contracts/`), not in `schemas/`.
- **Data outputs are not code**: derived datasets and catalogs must not be written into `src/` or `docs/`.
- **No YAML front-matter in code files**: JSON Schemas and shape bundles are code artifacts and must not use YAML front matter.

---

## 🧭 Context

### Why schemas are first-class

Schemas are the enforcement mechanism for contract-first behavior: artifacts must be valid at the boundary where they are produced.

This prevents “silent drift” such as:
- ETL emits a new field without updating catalog builders
- catalog outputs diverge from profile expectations
- UI registry config changes break map rendering in production
- Story Nodes accumulate unvalidated narrative structure
- telemetry payload shape changes make CI signals incomparable

### Constraints and invariants

Non-negotiables across the system that schemas help enforce:

1. **No UI direct-to-graph reads**
   - `web/` must not query Neo4j directly; all graph access is via `src/server/`.
2. **No unsourced narrative**
   - Published Story Nodes must be provenance-linked and must validate.
3. **Contracts are canonical**
   - Schemas/specs must live in `schemas/` and API contracts under `src/server/contracts/`.
4. **Deterministic validation**
   - CI should validate if present; fail if invalid; skip cleanly only when a check is not applicable.

---

## 🗺️ Diagrams

### System and contract boundaries

~~~mermaid
flowchart LR
  A[ETL<br/>src/pipelines] --> B[Catalogs<br/>data/stac + data/catalog/dcat + data/prov]
  B --> C[Graph Ingest<br/>src/graph + data/graph]
  C --> D[APIs<br/>src/server]
  D --> E[UI<br/>web]
  E --> F[Story Nodes<br/>docs/reports/story_nodes]
  F --> G[Focus Mode]

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
| Reference artifacts | JSON | `data/**`, `web/**`, `docs/reports/story_nodes/**` | Validated against schemas |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Schema contracts | JSON / SHACL | `schemas/**` | This registry |
| Validation results | logs / manifests | `mcp/runs/**` and/or `data/prov/**` | Tooling-specific |

### Sensitivity and redaction

Schemas influence what can be produced and what can be displayed. Treat schema changes as governance-relevant if they affect:
- location precision,
- redaction/generalization behavior,
- attribution fields,
- fields that could enable inference of sensitive locations or protected community data.

### Provenance hooks

Where possible, run manifests and provenance bundles should capture:
- schema family and schema version used to validate each artifact,
- validator tool and version,
- timestamp and result (pass/fail).

---

## 🌐 STAC, DCAT & PROV Alignment

Schemas in this registry are aligned to KFM profiles and enforce boundary validity before downstream ingest.

### STAC

- Output location:
  - Collections: `data/stac/collections/`
  - Items: `data/stac/items/`
- Validation:
  - Validate JSON structure and required fields at catalog build time.
  - Validate any KFM-specific constraints (extensions, identifiers, asset conventions) via KFM schema overlays.

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

### Versioning expectations

- New versions should link predecessor/successor in the relevant standard mechanism when applicable.
- The graph should mirror version lineage (entities point to catalog/provenance identifiers).

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Schema registry (`schemas/`) | Contract definitions for artifacts | JSON Schema + optional SHACL |
| Producers | Emit artifacts at boundaries | ETL outputs, catalogs, Story Nodes, UI registries, telemetry |
| Validators | Enforce contract compliance | CI jobs + local scripts |
| Consumers | Read artifacts | Graph ingest, API, UI runtime, Focus Mode |

### Interfaces and contract locations

| Contract type | Canonical location | Versioning rule |
|---|---|---|
| Data output schemas | `schemas/` | Semver + changelog (location TBD) |
| API contracts | `src/server/contracts/` | Contract tests required |
| UI layer registry schemas | `schemas/ui/` | Schema-validated before runtime |
| Story Node schemas | `schemas/storynodes/` | Publish must validate |
| Telemetry schemas | `schemas/telemetry/` | Contracted signals for CI/governance |

### Extension points checklist

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

### Story Nodes as machine-ingestible storytelling

Story Nodes are governed narrative artifacts:
- they must validate structurally,
- they must reference provenance-linked evidence,
- they must connect to entities in the graph by stable identifiers.

### Focus Mode rule

Focus Mode only consumes provenance-linked content:
- any predictive or AI-generated content must be opt-in,
- must include uncertainty metadata,
- must never appear as unmarked fact.

### Optional structured controls

The Story Node schema may define structured “Focus Mode controls” for UI behavior. Any such fields must be schema-defined and validated.

~~~yaml
# Illustrative placeholders only; actual supported fields are defined by schemas/storynodes/**
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

---

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks for governed docs (including this README)
- [ ] JSON Schema parse/lint checks for schema files
- [ ] Artifact validation:
  - [ ] STAC Collections and Items (`data/stac/**`) validate against `schemas/stac/`
  - [ ] DCAT records (`data/catalog/dcat/**`) validate against `schemas/dcat/`
  - [ ] PROV bundles (`data/prov/**`) validate against `schemas/prov/`
  - [ ] Story Nodes (`docs/reports/story_nodes/**`) validate against `schemas/storynodes/`
  - [ ] UI registries (`web/**`) validate against `schemas/ui/`
  - [ ] Telemetry payloads validate against `schemas/telemetry/`
- [ ] API contract tests at `src/server/contracts/`
- [ ] Security and sovereignty scanning gates (as applicable)

### Deterministic CI behavior

- If a schema-governed root exists and artifacts are invalid, CI must **fail**.
- If a check is not applicable to a change, CI may **skip** cleanly.
- Link/reference checks should ensure internal links resolve and that “not confirmed in repo” markers are used where appropriate.

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands and tools
# 1) validate schemas
# 2) validate schema-governed artifacts (STAC/DCAT/PROV/storynodes/ui/telemetry)
# 3) run tests + contract checks
# 4) run doc lint / link checks
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| Schema validation pass/fail | CI validators | `docs/telemetry/` + `schemas/telemetry/` |
| Story Node publish validation | Story pipeline | `docs/telemetry/` + `schemas/storynodes/` |
| UI registry validation | UI build | `docs/telemetry/` + `schemas/ui/` |

---

## ⚖ FAIR+CARE and Governance

### Review gates

Schema changes require careful review when they affect:
- what becomes public-facing,
- what becomes inferable (especially locations and protected community data),
- redaction/generalization behavior,
- API payload expectations that UI depends on.

### CARE and sovereignty considerations

- If a schema enables higher precision locations, expands identity-revealing fields, or reduces redaction, treat the change as sovereignty-sensitive and require governance review.
- When in doubt, prefer conservative defaults and explicitly document exceptions under governance.

### AI usage constraints

This document’s front matter sets the allowed and prohibited AI transforms. Schema content must not be used as a backdoor to create policy; policy belongs under `docs/governance/`.

---

## 🕰️ Version History

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
