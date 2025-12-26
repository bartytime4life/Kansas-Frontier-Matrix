---
title: "KFM Reproducibility Kit"
path: ".github/repro-kit/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
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

doc_uuid: "urn:kfm:doc:github:repro-kit-readme:v1.0.0"
semantic_document_id: "kfm-github-repro-kit-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:repro-kit-readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions: [ "summarize", "structure_extract", "translate", "keyword_index" ]
ai_transform_prohibited: [ "generate_policy", "infer_sensitive_locations" ]

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# KFM Reproducibility Kit

## 📘 Overview

### Purpose

This directory is the home for reproducibility helpers that make it easy to:

- reproduce **pipeline runs** (ETL → Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode),
- validate outputs against governed contracts and schemas,
- review PRs with a consistent “can we reproduce this?” checklist.

KFM’s architecture emphasizes deterministic processing and traceable lineage: ETL is deterministic and logged with hashes of inputs/outputs, enabling results to be verifiable and audit-friendly. This repro-kit exists to keep that promise operational for both local dev and CI.

### Scope

| In scope | Out of scope |
|---|---|
| Reproducing ETL outputs from the same input + config + code revision | Handling production secrets, credentials, or privileged access paths |
| Validating STAC/DCAT/PROV artifacts and run provenance bundles | Defining new governance policies |
| Re-running CI-like checks locally | Large-scale “full data” production replays of restricted datasets |

### Audience

- Maintainers and reviewers validating “v12-ready” contributions
- Contributors authoring pipelines, catalogs, schemas, APIs, UI layers, and Story Nodes
- CI maintainers (GitHub workflows / actions)

### Definitions

- **Deterministic**: same inputs + same config + same code revision ⇒ same outputs (byte-for-byte when practical).
- **Idempotent**: running the same job twice does not duplicate records or produce inconsistent results.
- **Run manifest**: a small, portable record that captures how to reproduce a run (inputs, config, commit SHA, versions, parameters).
- **PROV bundle**: provenance artifacts describing inputs, activities, outputs, and agents.
- **Stable identifier**: an ID that does not change unexpectedly between runs; used to link STAC/DCAT/PROV to graph and UI.

### Key artifacts

- `docs/MASTER_GUIDE_v12.md`
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- `docs/architecture/` (system architecture PDFs, if present)

### Definition of done

- [ ] This README is updated when repro-kit scripts/actions are added or changed.
- [ ] For any pipeline/catalog/graph/API/UI change, reviewers can identify the reproduction entrypoint (manifest, fixture, or scripted run).
- [ ] Repro steps are aligned with minimum CI gates and do not bypass governance/sensitivity checks.

## 🗂️ Directory Layout

### This document

| Artifact | Path |
|---|---|
| Repro kit README | `.github/repro-kit/README.md` |

### Related repository paths

| Area | Canonical path |
|---|---|
| Pipelines | `src/pipelines/` |
| Pipeline runbooks | `docs/pipelines/<domain>/` |
| Domain outputs | `data/<domain>/{raw,work,processed}/` |
| STAC catalogs | `data/stac/collections/` and `data/stac/items/` |
| DCAT catalogs | `data/catalog/dcat/` |
| PROV bundles | `data/prov/` |
| Graph | `src/graph/` and import artifacts under `data/graph/` |
| API boundary | `src/server/` and contracts under `src/server/contracts/` |
| UI | `web/` |
| Story Nodes | `docs/reports/story_nodes/` |
| Schemas | `schemas/` |
| Tests | `tests/` |
| MCP experiments | `mcp/` |

### Expected file tree for this sub-area

> This is the recommended structure. Some directories may not exist yet (**not confirmed in repo**).

~~~text
📁 .github/
└── 📁 repro-kit/
    ├── 📄 README.md
    ├── 📁 actions/            # optional: composite actions for CI reproducibility
    ├── 📁 scripts/            # optional: local wrappers for CI-equivalent checks
    ├── 📁 fixtures/           # optional: small “golden” datasets for deterministic test runs
    └── 📁 env/                # optional: environment lockfiles for deterministic execution
~~~

## 🧭 Context

### Background

KFM’s platform emphasizes reproducibility:

- ETL steps are designed to be deterministic and logged, including hashing of input/output transformations for traceability.
- The system is configuration-driven so past versions can be regenerated by checking out the same code/config revision and re-running.

This kit is the documentation and “glue” layer to keep that reproducibility usable for contributors and reviewers.

### Assumptions

- The pipeline flow is preserved: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- The UI does not read Neo4j directly; the API boundary mediates access and enforces redaction/generalization.
- Contract and schema validation are treated as first-class build gates.

### Constraints / invariants

- Pipelines are idempotent and deterministic.
- Every pipeline run emits a PROV activity bundle and a run manifest (location may be under `data/prov/` or `releases/<version>/`).
- Catalog artifacts validate against schemas under `schemas/`.
- UI consumes graph and catalog content through APIs and catalog endpoints only.
- Focus Mode consumes provenance-linked content only.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Where is the authoritative run manifest location for this repo: `data/prov/` vs `releases/<version>/`? | TBD | TBD |
| Which fixture datasets are safe to include publicly under `.github/repro-kit/fixtures/`? | TBD | TBD |
| What is the standard environment locking approach for pipelines and tests? | TBD | TBD |

### Future extensions

- Add composite actions under `.github/repro-kit/actions/` that run schema validation, contract tests, and reproducibility checks.
- Add fixture datasets and “golden output” hashes for deterministic regression tests.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A["ETL — src/pipelines"] --> B["STAC/DCAT/PROV — data/stac · data/catalog/dcat · data/prov"]
  B --> C["Neo4j Graph — src/graph"]
  C --> D["API boundary — src/server"]
  D --> E["UI — web/"]
  E --> F["Story Nodes — docs/reports/story_nodes"]
  F --> G["Focus Mode — provenance-linked"]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant UI as UI (web/)
  participant API as API (src/server)
  participant Graph as Graph (Neo4j via src/graph contracts)
  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: context bundle (entities + evidence refs)
  API-->>UI: narrative + citations + audit flags
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Run manifest | YAML/JSON | `data/prov/` or `releases/<version>/` | schema if defined |
| Pipeline configuration | YAML/JSON | `src/pipelines/` + domain runbooks | lint + schema |
| Source references | URL/file refs | `data/<domain>/raw/` | checksums + license metadata |
| Schemas | JSON Schema | `schemas/` | CI schema validation |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Run logs | text/JSON | `mcp/runs/` or pipeline-defined output | log schema if defined |
| PROV activity bundle | JSON/Turtle | `data/prov/` | PROV profile |
| STAC collections/items | JSON | `data/stac/{collections,items}/` | STAC schemas |
| DCAT records | JSON-LD/RDF | `data/catalog/dcat/` | DCAT profile |
| Repro checksums | text/JSON | repo-defined | sha256 format rule |

### Sensitivity & redaction

- Do not commit secrets or credentials into repro-kit.
- If a reproduction path touches sensitive locations or restricted data, ensure the public artifact is generalized/redacted and governance-reviewed.

### Quality signals

- Determinism: repeated runs match expected hashes and stable identifiers.
- Completeness: required catalogs and provenance artifacts exist for outputs.
- Contract integrity: schemas and API contracts pass tests.

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Collections and Items live under `data/stac/collections/` and `data/stac/items/`.
- Repro steps should include validating these JSON artifacts against the repo’s STAC schemas.

### DCAT

- DCAT records live under `data/catalog/dcat/`.
- Repro steps should confirm minimal DCAT mappings exist for each dataset when required.

### PROV-O

- Every pipeline run should produce a PROV activity record linking inputs to outputs.
- Run logs may be treated as a PROV activity record when they capture commit SHA, inputs, and outputs.

### Versioning

- Prefer stable identifiers and explicit predecessor/successor relationships for version lineage.
- When output formats or schemas change, bump versions and update validation expectations.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Repro kit | Reproduction helpers and guidance | `.github/repro-kit/` |
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Cypher + API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Graph + docs |
| Focus Mode | Contextual synthesis | Provenance-linked |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| STAC catalogs | `data/stac/` | Validate against schemas |
| DCAT catalogs | `data/catalog/dcat/` | Validate against schemas |
| PROV bundles | `data/prov/` | Validate to profile and integrity rules |
| API contracts | `src/server/contracts/` | Contract tests required |
| UI registries | `web/` | Validate against `schemas/ui/` |

## 🧠 Story Node and Focus Mode Integration

### How this work surfaces in Focus Mode

- Reproducibility ensures Focus Mode’s context bundle remains provenance-linked and auditable.

### Provenance-linked narrative rule

- Every factual claim must trace to a dataset, record, or asset identifier.

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation and CI/CD

### Validation steps

Minimum CI gates for “v12-ready” contributions include:

- [ ] Markdown protocol validation
- [ ] JSON schema validation for STAC, DCAT, and telemetry
- [ ] Graph integrity tests
- [ ] API contract tests
- [ ] UI layer registry schema checks
- [ ] Security and sovereignty scanning gates where applicable

### Reproduction

~~~bash
# Replace with repo-specific commands as they are added.

# 1) Run schema validation for catalogs and metadata
# <TBD>

# 2) Run unit/integration tests (pipelines / graph / API / UI)
# <TBD>

# 3) Run doc lint and markdown protocol checks
# <TBD>

# 4) Optional: rerun a “golden” fixture pipeline and compare hashes
# <TBD>
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| Repro run id | repro-kit scripts/actions | `mcp/runs/` or CI artifacts |
| Schema validation summary | validators | CI logs |
| Hash comparison report | repro-kit | CI artifacts |

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is required when changes introduce:

- new sensitive layers,
- new AI narrative behaviors,
- new external data sources,
- new public-facing endpoints.

### CARE / sovereignty considerations

- If a reproduction involves culturally sensitive data or restricted locations, document the redaction/generalization behavior and ensure review before publishing artifacts.

### AI usage constraints

- AI-assisted outputs that surface in user-facing contexts must remain evidence-led, provenance-linked, and must not introduce unsourced claims.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial repro-kit README scaffold | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
