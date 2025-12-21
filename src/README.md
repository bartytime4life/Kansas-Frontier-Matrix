---
title: "Kansas Frontier Matrix — `src/` README"
path: "src/README.md"
version: "v1.0.0"
last_updated: "2025-12-21"
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

doc_uuid: "urn:kfm:doc:repo:src-readme:v1.0.0"
semantic_document_id: "kfm-repo-src-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:repo:src-readme:v1.0.0"
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

# Kansas Frontier Matrix — `src/` (Code)

This directory is the canonical **code** home for the KFM backend subsystems that implement the governed pipeline:

**ETL → STAC/DCAT/PROV catalogs → Graph → API boundary → UI → Story Nodes → Focus Mode**.

If you are unsure where something belongs, prefer **canonical homes** over convenience. The repo structure is part of KFM’s compliance mechanism (auditable ordering + interfaces).

---

## 📘 Overview

### Purpose

- Define what belongs under `src/` and what does not.
- Record **canonical subsystem homes** and critical **boundaries** (e.g., UI must not access Neo4j directly; access is via the API boundary).
- Keep `src/` aligned with governed standards and CI expectations (schemas, contracts, provenance, validation).

### Scope

| In Scope | Out of Scope |
|---|---|
| Pipeline code (`src/pipelines/`) | Derived datasets (belong under `data/<domain>/processed/`) |
| Graph build / ontology bindings (`src/graph/`) | Published narrative content (belongs under `docs/reports/story_nodes/`) |
| API boundary code (`src/server/`) + contracts (`src/server/contracts/`) | UI code (belongs under `web/`) |
| Shared libraries used by the above | Catalog outputs (STAC/DCAT/PROV belong under `data/`) |

### Audience

- Primary: Contributors working on **pipelines**, **graph**, and **API boundary** code.
- Secondary: UI contributors needing to understand the API boundary and contract expectations.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc: pipeline, catalog (STAC/DCAT/PROV), provenance, ontology, contract, Story Node, Focus Mode.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (v12 draft) | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline ordering + directory map |
| API Contract Extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | Contracts owners | Required when changing REST/GraphQL contracts |
| Universal governed-doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | Structure for governed docs like this README |
| Repo standards | `docs/standards/` | Governance | KFM-MDP + profiles (STAC/DCAT/PROV) |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Directory layout matches canonical homes and boundaries
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Links point to governed docs/templates (no ad-hoc process in README)

---

## 🗂️ Directory Layout

### This document

- `path`: `src/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Pipelines | `src/pipelines/` | ETL, transforms, catalog build helpers, graph build helpers |
| Graph | `src/graph/` | Graph build + ontology bindings + migrations/utilities |
| API boundary | `src/server/` | Contracted access layer (REST/GraphQL) |
| API contracts | `src/server/contracts/` | OpenAPI/GraphQL SDL/etc. Contracts are canonical + CI-validated |
| Schemas | `schemas/` | STAC/DCAT/PROV/StoryNode/UI/Telemetry schemas (canonical) |
| Data lifecycle | `data/` | `raw/`, `work/`, `processed/`, plus catalog outputs and graph imports |
| UI | `web/` | React + map UI (never queries Neo4j directly) |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published narrative artifacts with provenance |
| Pipeline docs | `docs/pipelines/<domain>/` | Runbooks + domain documentation |

### Expected file tree for this sub-area

~~~text
📁 src/
├── 📄 README.md
├── 📁 pipelines/                 # ETL + transforms + (catalog/graph build code)
├── 📁 graph/                     # Ontology bindings + migrations + graph build helpers
├── 📁 server/                    # API boundary (REST/GraphQL) + enforcement (redaction/contract)
│   └── 📁 contracts/             # API contracts (canonical; CI-validated)
└── 📁 _legacy/                   # (optional; if present) deprecated modules during migration
~~~

---

## 🧭 Context

### Background

KFM is a governed, provenance-centric knowledge system. The pipeline ordering and subsystem boundaries are **non-negotiable** because they ensure reproducibility, auditability, and safe publication.

### Assumptions

- Neo4j is the primary graph database.
- STAC, DCAT, and PROV remain first-class and required for datasets and evidence products.
- The UI is a React-based web app and must not connect to Neo4j directly (API boundary only).

### Constraints and invariants (non-negotiables)

1. **No UI direct-to-graph reads**
   - `web/` must never query Neo4j directly; all graph access is via `src/server/`.

2. **No unsourced narrative**
   - Published Story Nodes must be provenance-linked and must validate.

3. **Contracts are canonical**
   - Schemas/specs live in `schemas/`.
   - API contracts live in `src/server/contracts/` and must validate in CI.

4. **Data outputs are not code**
   - Derived datasets belong under `data/<domain>/processed/`, not under `src/`.

### Migration note (repo drift)

If both `src/api/` and `src/server/` exist, treat `src/server/` as canonical. `src/api/` should be migrated to `src/_legacy/api/` or removed after migration.

### Extension points checklist (for future work)

- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[ETL<br/>src/pipelines] --> B[Catalogs<br/>data/stac + data/catalog/dcat + data/prov]
  B --> C[Graph<br/>src/graph]
  C --> D[API boundary<br/>src/server]
  D --> E[UI<br/>web]
  E --> F[Story Nodes<br/>docs/reports/story_nodes]
  F --> G[Focus Mode<br/>provenance-linked only]
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Raw source snapshots | files (varies) | `data/<domain>/raw/` | domain-specific checks + checksums |
| Work intermediates | files (varies) | `data/<domain>/work/` | pipeline stage checks |
| Processed outputs | files (varies) | `data/<domain>/processed/` | schema + consistency checks |
| Schemas/contracts | JSON / YAML / SDL | `schemas/` + `src/server/contracts/` | CI schema + contract validation |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| STAC collections/items | JSON | `data/stac/**` | `schemas/stac/**` |
| DCAT dataset records | JSON-LD/JSON | `data/catalog/dcat/**` | `schemas/dcat/**` |
| PROV bundles | JSON-LD/JSON | `data/prov/**` | `schemas/prov/**` |
| Graph import artifacts | CSV/Cypher | `data/graph/**` | schema/shape checks + import validation |
| API contracts | OpenAPI/SDL/etc. | `src/server/contracts/**` | contract tests in CI |

### Sensitivity & redaction

- Never hardcode secrets/credentials in `src/`.
- Any restricted locations or culturally sensitive knowledge must be protected by:
  - generalization of geometry where required,
  - API-level redaction,
  - Story Node asset review gates.

### Quality signals

- All STAC/DCAT/PROV artifacts validate against schemas in `schemas/`.
- No orphan references (entity refs, evidence refs, Story Node refs resolve).
- Deterministic runs and diffable outputs.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Canonical output: `data/stac/collections/` and `data/stac/items/`
- Contract: STAC artifacts must validate against `schemas/stac/`.

### DCAT

- Canonical output: `data/catalog/dcat/`
- Contract: DCAT artifacts must validate against `schemas/dcat/`.

### PROV-O

- Canonical output: `data/prov/`
- Policy: every pipeline run emits a PROV activity bundle; catalogs + graph ingest should retain PROV identifiers.

### Graph linkage

Graph nodes should reference:
- STAC Item IDs
- DCAT dataset IDs
- PROV activity/run IDs

---

## 🧱 Architecture

### Components

| Component | Canonical home | Responsibility | Notes |
|---|---|---|---|
| Pipelines | `src/pipelines/` | ETL/normalization + producing processed outputs | Deterministic + idempotent |
| Catalog build | `src/pipelines/` (or a catalog submodule) | Emit STAC/DCAT/PROV into `data/` | Never write catalogs into `docs/` |
| Graph build | `src/graph/` | Ingest processed outputs + catalogs + provenance | Import artifacts live under `data/graph/` |
| API boundary | `src/server/` | Contracted access to graph + catalogs | Enforces redaction/generalization + contract tests |
| Contracts | `src/server/contracts/` | OpenAPI/SDL/etc. | Canonical + CI validated |

### Contract governance reminder (API changes)

When you change API contracts:
- Use `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Evaluate backward compatibility; breaking changes require a version bump or compatibility layer.

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Focus Mode must only display **provenance-linked** context.
- Story Nodes must validate (front-matter, citations, entity refs, redaction compliance).
- Predictive/AI-generated content is:
  - opt-in,
  - uncertainty-annotated,
  - never presented as unmarked fact.

### Optional structured controls (if a subsystem feeds Focus Mode)

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

---

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV/StoryNodes/UI/Telemetry as applicable)
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] Security and sovereignty checks (as applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate schemas
# 2) run unit/integration tests
# 3) run doc lint
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

---

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes to contracts/schemas/ontology require review (and possibly version bumps).
- Story Node publication requires validation + redaction compliance review.

### CARE / sovereignty considerations

- Identify communities impacted and protection rules.
- Apply geometry generalization / access controls when required by policy.

### AI usage constraints

- Ensure doc’s AI permissions/prohibitions match intended use (see front-matter).

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial `src/` README (governed template) | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
