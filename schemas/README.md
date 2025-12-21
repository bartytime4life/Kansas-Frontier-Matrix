---
title: "KFM Schemas — Registry & Validation"
path: "schemas/README.md"
version: "v1.0.0"
last_updated: "2025-12-21"
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

# KFM Schemas

## 📘 Overview

### Purpose

`schemas/` is the canonical home for **machine-readable interface contracts** used across the Kansas Frontier Matrix pipeline. These contracts enable deterministic validation at subsystem boundaries (catalog outputs, graph ingest fixtures, API payloads, UI registries, Story Nodes, and telemetry).

### Scope

In scope:

- JSON Schemas (and where adopted, optional shape bundles) for:
  - Catalog outputs: **STAC**, **DCAT**, **PROV**
  - Story Node validation inputs (front-matter structure, citation shapes, entity references)
  - UI configuration registries (map layer registries and other structured UI configs)
  - Telemetry/event payloads emitted by pipelines and applications

Out of scope:

- The catalogs themselves (`data/stac/**`, `data/catalog/dcat/**`, `data/prov/**`)
- API specifications and tests (live under the API subsystem, see `src/server/`)

### Audience

- Catalog maintainers and ETL authors
- Graph and ontology maintainers
- API maintainers
- UI maintainers
- Story Node authors and editors
- CI and release maintainers

### Definitions

- Link: `docs/glossary.md`
- “Contract” in this repo means: a machine-validated schema/spec that producers and consumers agree on.

### Key artifacts

| Artifact | Path | Notes |
|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | Canonical pipeline + invariants |
| Redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Canonical roots + minimum contract set |
| Schemas registry | `schemas/README.md` | This file |
| STAC catalogs | `data/stac/` | Collections + Items |
| DCAT catalogs | `data/catalog/dcat/` | Dataset records |
| PROV lineage bundles | `data/prov/` | Run/provenance bundles |
| API contracts | `src/server/contracts/` | OpenAPI/GraphQL, etc. |
| Story Nodes | `docs/reports/story_nodes/` | Draft + published nodes |
| UI | `web/` | React map/narrative app |

### Definition of Done

- [ ] `schemas/` contains the minimum contract set for v13 readiness.
- [ ] Every schema change follows semantic versioning and includes a changelog entry.
- [ ] CI fails deterministically when schemas are present but invalid.
- [ ] Producers/consumers validate outputs/configs against these schemas at the correct boundary.

## 🗂️ Directory Layout

### This document lives at

- `schemas/README.md`

### Related repository paths

| Artifact | Path |
|---|---|
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` |
| Graph import artifacts | `data/graph/` |
| API boundary | `src/server/` |
| UI boundary | `web/` |
| Story Nodes | `docs/reports/story_nodes/` |
| CI workflows | `.github/workflows/` |

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

## 🧭 Context

### Why this folder exists

KFM is contract-first: every interface boundary has a defined schema/spec so that producers and consumers can evolve independently.

Non-negotiables to keep in mind:

- The UI must not read Neo4j directly — all graph access is mediated by the API boundary.
- Contracts are canonical — schema/spec changes must be intentional and validated in CI.

### How to add or update a schema

1. Pick the boundary: STAC, DCAT, PROV, Story Nodes, UI registry, or telemetry.
2. Add or update schema files in the relevant subfolder.
3. Version appropriately:
   - Breaking change → major bump
   - Backward-compatible addition → minor bump
   - Bugfix/clarification → patch bump
4. Update changelog for the affected contract set.
5. Update producers/consumers and their tests.
6. Validate locally and in CI.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[ETL<br/>src/pipelines] --> B[Catalog outputs<br/>data/stac + data/catalog/dcat + data/prov]
  B --> C[Graph ingest<br/>src/graph + data/graph]
  C --> D[API boundary<br/>src/server]
  D --> E[UI<br/>web]
  E --> F[Story Nodes<br/>docs/reports/story_nodes]
  F --> G[Focus Mode]

  S[schemas/] -. validates .-> B
  S -. validates .-> D
  S -. validates .-> E
  S -. validates .-> F
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Contract definitions | JSON Schema, shape bundles | `schemas/**` | Schema lint + CI |
| Standard profiles | STAC/DCAT/PROV specs | `docs/standards/**` | Governance review |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| STAC Collections/Items | JSON | `data/stac/**` | `schemas/stac/**` |
| DCAT datasets | JSON-LD | `data/catalog/dcat/**` | `schemas/dcat/**` |
| PROV bundles | JSON, TTL | `data/prov/**` | `schemas/prov/**` |
| Story Nodes | Markdown + YAML front-matter | `docs/reports/story_nodes/**` | `schemas/storynodes/**` |
| UI registries | JSON | `web/**` | `schemas/ui/**` |
| Telemetry events | JSON | TBD | `schemas/telemetry/**` |

### Sensitivity & redaction

- Schemas that surface to public outputs should support redaction/generalization fields where governance requires it.
- Any schema touching protected locations or culturally sensitive data requires governance review.

### Quality signals

- Schema validation pass/fail is a minimum quality gate.
- Domain-specific checks (e.g., geometry validity, temporal ranges) belong in ETL and should be reflected in CI checks.

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Validate that STAC catalogs conform to required STAC structure and KFM-specific constraints.
- Prefer stable identifiers and consistent extensions where used.

### DCAT

- Validate that DCAT outputs capture minimum required dataset metadata (title/description/license/keywords).
- Where JSON-LD shapes are used, store shape bundles alongside DCAT constraints.

### PROV-O

- Validate that every pipeline run can be expressed as provenance:
  - sources (`prov:wasDerivedFrom`)
  - generation activity (`prov:wasGeneratedBy`)
  - agent attribution (human/script identifiers)

### Versioning

- Use semantic versioning for schema evolution.
- Maintain a changelog so downstream producers/consumers can track contract changes and deprecations.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Cypher + API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Graph + docs |
| Focus Mode | Contextual synthesis | Provenance-linked |

### Interfaces and contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/` + `docs/api/` | Contract tests required |
| Layer registry | `web/**` | Schema-validated |

### Extension points checklist

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

- Focus Mode should only consume provenance-linked, schema-valid content.
- Story Node contracts should ensure:
  - citations are present and resolvable
  - referenced entities have canonical IDs
  - sensitive content is correctly generalized/redacted

### Provenance-linked narrative rule

- Every factual claim must trace to a dataset / record / asset identifier.

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks
- [ ] Schema validation
- [ ] Story Node validation
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI schema checks
- [ ] Security and sovereignty checks

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate schemas
# 2) run unit/integration tests
# 3) run doc lint
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| Schema validation results | CI | CI logs + artifacts |
| Pipeline run signals | ETL/catalog runs | `data/prov/` and/or run manifests |
| UI runtime events | Web app | telemetry sink defined by UI |

## ⚖ FAIR+CARE & Governance

### Review gates

- Schema changes that affect public-facing payloads or any sensitive data fields require governance review.

### CARE and sovereignty considerations

- Identify communities impacted by changes.
- Document redaction/generalization rules for restricted locations.

### AI usage constraints

- This document permits structural extraction, summarization, translation, and keyword indexing.
- Prohibited: generating new policy text or inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial schemas registry README | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

