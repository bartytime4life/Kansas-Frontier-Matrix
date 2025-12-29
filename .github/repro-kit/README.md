---
title: "KFM Reproducibility Kit"
path: ".github/repro-kit/README.md"
version: "v1.0.1"
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

doc_uuid: "urn:kfm:doc:github:repro-kit-readme:v1.0.1"
semantic_document_id: "kfm-github-repro-kit-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:github:repro-kit-readme:v1.0.1"
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

# KFM Reproducibility Kit

## 📘 Overview

### Purpose

This directory is the home for reproducibility helpers and review guidance that make it easier to:

- reproduce **pipeline runs end-to-end** (ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode),
- validate outputs against **governed contracts and schemas**,
- review PRs with a consistent “can we reproduce this?” checklist,
- keep KFM’s “deterministic + provenance-first” promise operational in both **local development** and **CI**.

This kit is intentionally **public-safe**: it must not include secrets, credentials, or privileged access paths.

### Scope

| In scope | Out of scope |
|---|---|
| Reproducing ETL outputs from the same **inputs + config + code revision** | Handling production secrets/credentials or privileged access paths |
| Validating STAC/DCAT/PROV artifacts and run provenance bundles | Defining new governance policies (use governed docs for that) |
| Re-running CI-like checks locally (schema validation, contract tests, lint) | Large-scale “full data” production replays of restricted datasets |
| Providing PR review checklists for reproducibility & provenance | Bypassing CARE/sovereignty, redaction, or security gates |

### Audience

- Maintainers and reviewers validating “v12-ready” (and future v13) contributions
- Contributors authoring pipelines, catalogs, schemas, APIs, UI layers, and Story Nodes
- CI maintainers (GitHub workflows / actions)

### Definitions

- **Deterministic pipeline**: idempotent, config-driven transforms with logged inputs/outputs and stable IDs.
- **Idempotent**: running the same job twice does not duplicate records or produce inconsistent results.
- **Run manifest**: a portable record that captures how to reproduce a run (inputs, config, commit SHA, versions, parameters).
- **PROV bundle**: provenance artifacts describing inputs, activities, outputs, and agents (W3C PROV-O aligned).
- **Boundary artifacts**: catalogs + lineage outputs (STAC/DCAT/PROV) that are required before data proceeds downstream.
- **Stable identifier**: an ID that does not change unexpectedly between runs; used to link STAC/DCAT/PROV to graph, APIs, and UI.
- **Contract-first**: schemas + API contracts are first-class artifacts; breaking changes require versioning and compatibility testing.
- **Focus Mode rule**: Focus Mode consumes only provenance-linked context bundles (no unsourced narrative).

Glossary link: `docs/glossary.md` (**not confirmed in repo**).

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Repro kit README (this doc) | `.github/repro-kit/README.md` | TBD | Repro helpers + checklists |
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | TBD | System + pipeline source of truth |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Default governed doc template |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Story | Narrative + Focus Mode surfacing |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | REST/GraphQL contract changes |
| Ingestion architecture | `docs/architecture/KFM_INGEST_ARCHITECTURE.md` | Architecture | ETL + catalog patterns (**doc name from intake design**) |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs | **not confirmed in repo** (linked by Master Guide) |

### Definition of done

For this README:

- [ ] Front-matter complete + valid
- [ ] Canonical pipeline ordering and invariants stated (no shortcuts)
- [ ] Canonical paths (data staging + catalogs + provenance) are correct
- [ ] Repro steps are repeatable and do not bypass governance/sensitivity checks
- [ ] This README is updated when repro-kit scripts/actions/fixtures are added or changed

For any new repro-kit helper (script/action/fixture):

- [ ] Usage instructions added (inputs, outputs, expected artifacts)
- [ ] “Public-safe” check completed (no secrets, no sensitive coordinates, no restricted data)
- [ ] A reviewer can run the helper locally or in CI and understand pass/fail criteria
- [ ] Where applicable, helper produces a machine-readable report (hash diff / schema summary)

## 🗂️ Directory Layout

### This document

| Artifact | Path |
|---|---|
| Repro kit README | `.github/repro-kit/README.md` |

### Related repository paths

| Area | Canonical path | What lives here |
|---|---|---|
| Pipelines (ETL) | `src/pipelines/` | Extract/transform/load logic + configs (repo-defined) |
| Data staging (raw) | `data/raw/<domain>/` | Source snapshots / raw inputs (versioned where allowed) |
| Data staging (work) | `data/work/<domain>/` | Intermediate artifacts (deterministic, reproducible) |
| Data staging (processed) | `data/processed/<domain>/` | Final derived outputs for publication/use |
| STAC catalogs | `data/stac/collections/` and `data/stac/items/` | Collection + Item JSON |
| DCAT catalogs | `data/catalog/dcat/` | Dataset discovery records (JSON-LD/RDF) |
| PROV bundles | `data/prov/` | W3C PROV-O lineage (e.g., JSON-LD) |
| Graph layer | `src/graph/` | Ontology/ingest/migrations (repo-defined) |
| Graph import artifacts | `data/graph/` | Import/export artifacts (**not confirmed in repo**) |
| API boundary | `src/server/` | Contracted access + redaction + policy enforcement (repo-defined) |
| API contracts | `src/server/contracts/` | OpenAPI/GraphQL contracts (**not confirmed in repo**) |
| UI | `web/` | React/MapLibre frontend |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published Story Nodes (repo-defined) |
| Schemas | `schemas/` | JSON Schemas for catalogs/contracts/registries |
| Tests | `tests/` | Unit/integration tests |
| Tools | `tools/` | Utilities / validators (**not confirmed in repo**) |
| MCP runs / experiments | `mcp/runs/` and `mcp/experiments/` | Run logs, experiment artifacts (repo-defined) |
| CI workflows | `.github/workflows/` | GitHub Actions workflows |

### Expected file tree for this sub-area

> Recommended structure. Some directories may not exist yet (**not confirmed in repo**).

~~~text
📁 .github/
└── 📁 repro-kit/
    ├── 📄 README.md
    ├── 📁 actions/            # optional: composite actions for CI reproducibility
    ├── 📁 scripts/            # optional: local wrappers for CI-equivalent checks
    ├── 📁 fixtures/           # optional: small “golden” datasets (public-safe only)
    ├── 📁 env/                # optional: environment lockfiles (container/lockfiles)
    └── 📁 reports/            # optional: hash diffs / validation summaries (often CI artifacts)
~~~

## 🧭 Context

### Background

KFM’s architecture is intentionally reproducible and auditable:

- The pipeline ordering is non-negotiable: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.
- Catalog + provenance outputs are treated as “boundary artifacts” and should exist before data moves into downstream stages.
- Focus Mode is a hard gate: user-facing context must remain provenance-linked (no unsourced narrative).

This repro-kit is the practical “glue” that helps maintainers and contributors uphold those rules in PRs and CI.

### Assumptions

- The canonical flow is preserved end-to-end (no shortcuts across stages).
- The UI does not read Neo4j directly; the API boundary mediates access and enforces redaction/generalization.
- Contract and schema validation are treated as first-class build gates.

### Constraints / invariants

- Pipelines are idempotent and deterministic (config-driven; log inputs/outputs; stable IDs).
- Data moves through standardized staging areas:
  - `data/raw/<domain>/` → `data/work/<domain>/` → `data/processed/<domain>/`
- At publication boundaries, datasets produce governed artifacts:
  - STAC: `data/stac/collections/` and `data/stac/items/`
  - DCAT: `data/catalog/dcat/`
  - PROV: `data/prov/`
- Sensitivity must not weaken across stages:
  - No output is less restricted than its input.
  - Any restricted/sensitive location handling must be documented and governance-reviewed.

### Reproducibility contract

A change is “reproducible” (reviewable) when a reviewer can:

1. Check out the referenced `commit_sha` (or PR SHA),
2. Identify the run entrypoint (manifest/script/workflow),
3. Obtain the same allowed inputs (or fixtures),
4. Re-run the pipeline step(s),
5. Validate outputs (schemas + contracts),
6. Compare expected fingerprints (hashes, stable IDs, counts, invariants),
7. Inspect lineage (PROV + boundary artifacts) without ambiguity.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Where is the authoritative run manifest location for this repo: `data/prov/` vs `releases/<version>/`? | TBD | TBD |
| Which fixture datasets are safe to include publicly under `.github/repro-kit/fixtures/`? | TBD | TBD |
| What is the standard environment locking approach for pipelines and tests (container, lockfiles, both)? | TBD | TBD |
| Where do validators live (e.g., `tools/`, `src/pipelines/`, CI-only)? | TBD | TBD |

### Future extensions

- Add composite actions under `.github/repro-kit/actions/` that run schema validation, contract tests, and reproducibility checks.
- Add fixture datasets and “golden output” hashes for deterministic regression tests.
- Capture environment fingerprints (container digests / lockfiles) as part of run manifests.
- Extend catalogs/provenance to better encode uncertainty/quality metadata for derived or modeled layers (**coordinate with schemas**).

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A["Raw Sources — data/raw/<domain>"] --> B["ETL — src/pipelines"]
  B --> C["Work + Processed — data/work + data/processed"]
  C --> D["STAC/DCAT/PROV — data/stac · data/catalog/dcat · data/prov"]
  D --> E["Neo4j Graph — src/graph"]
  E --> F["API boundary — src/server"]
  F --> G["UI — web/"]
  G --> H["Story Nodes — docs/reports/story_nodes"]
  H --> I["Focus Mode — provenance-linked only"]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant UI as UI (web/)
  participant API as API (src/server)
  participant Graph as Graph (Neo4j via src/graph)
  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: context bundle (entities + evidence refs)
  API-->>UI: narrative + citations + audit flags
~~~

## 📦 Data & Metadata

### Data lifecycle

- Required staging: `data/raw/<domain>/` → `data/work/<domain>/` → `data/processed/<domain>/`
- Publication boundary artifacts:
  - STAC: `data/stac/collections/` + `data/stac/items/`
  - DCAT: `data/catalog/dcat/`
  - PROV: `data/prov/`

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Raw sources | file/url/db snapshot | `data/raw/<domain>/` | checksums + license metadata |
| Pipeline configuration | YAML/JSON | `src/pipelines/` + domain runbooks (repo-defined) | lint + schema |
| Schemas | JSON Schema | `schemas/` | CI schema validation |
| Run manifest | YAML/JSON | repo-defined (often `data/prov/` adjacent) | schema if defined |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Processed outputs | domain-specific | `data/processed/<domain>/` | domain checks + invariants |
| Run logs | text/JSON | `mcp/runs/` or CI artifacts | log schema if defined |
| PROV activity bundle | JSON-LD / Turtle | `data/prov/` | PROV profile |
| STAC collections/items | JSON | `data/stac/{collections,items}/` | STAC schemas |
| DCAT records | JSON-LD / RDF | `data/catalog/dcat/` | DCAT profile |
| Repro checksums | text/JSON | repo-defined | sha256 format rule |

### Suggested minimal run manifest shape

> Optional guidance (not a governed schema). If a governed schema exists, follow that instead.

~~~yaml
run_id: "run-YYYYMMDD-HHMMSS-<shortsha>"
commit_sha: "<git-sha>"
pipeline:
  name: "<pipeline-name>"
  entrypoint: "<script|workflow|command>"
  config_paths:
    - "<path>"
inputs:
  - id: "<source-id-or-path>"
    sha256: "<hash>"
outputs:
  - id: "<dataset-id-or-path>"
    sha256: "<hash>"
boundary_artifacts:
  stac_collections:
    - "data/stac/collections/<collection>.json"
  stac_items:
    - "data/stac/items/<item>.json"
  dcat_records:
    - "data/catalog/dcat/<dataset>.jsonld"
  prov_records:
    - "data/prov/<activity>.jsonld"
notes:
  sensitivity: "public|internal|restricted"
  determinism: "byte-for-byte when practical; tolerance-based where necessary"
~~~

### Sensitivity & redaction

- Do not commit secrets or credentials into repro-kit.
- If a reproduction path touches sensitive locations or restricted data:
  - Ensure public artifacts are generalized/redacted,
  - Ensure the dataset sensitivity labels are preserved,
  - Ensure governance review occurs before publishing artifacts.

### Quality signals

- Determinism: repeated runs match expected hashes and stable identifiers (byte-for-byte when practical).
- Completeness: required catalogs and provenance artifacts exist for outputs.
- Contract integrity: schemas and API contracts pass tests.
- Safety: outputs are never less restricted than inputs; redaction/generalization is documented.

## 🌐 STAC, DCAT & PROV Alignment

### Alignment policy

At publication boundaries, datasets are expected to have:

- STAC Collection + Item(s),
- DCAT dataset mapping (minimum title/description/license/keywords),
- PROV activity describing lineage.

### Cross-layer linkage expectations

- Catalog identifiers (STAC/DCAT/PROV) should be the stable “evidence spine”:
  - Graph nodes reference catalog IDs (or can be resolved back to them),
  - API responses surface provenance references (directly or via resolvable IDs),
  - UI/Focus Mode experiences remain evidence-led and provenance-linked.

### Versioning expectations

- Prefer stable identifiers and explicit predecessor/successor relationships for version lineage.
- When output formats, schemas, or contracts change:
  - bump versions,
  - update validation expectations,
  - ensure compatibility tests (or migration notes) exist.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Repro kit | Reproduction helpers and guidance | `.github/repro-kit/` |
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV boundary artifacts | JSON/JSON-LD + validators |
| Graph | Neo4j semantic layer | Accessed via API layer |
| APIs | Serve contracts + enforce redaction | REST/GraphQL |
| UI | Map + narrative | API calls only |
| Story Nodes | Curated narrative | Provenance-linked references |
| Focus Mode | Contextual deep dives | Provenance-linked context bundles |

### Subsystem contracts

| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| ETL | configs + run logs + validation outputs | deterministic, replayable |
| Catalogs | STAC/DCAT/PROV schemas + validators | machine-validated boundary artifacts |
| Graph | ontology + migrations + constraints | stable labels/edges + provenance links |
| APIs | OpenAPI/GraphQL schema + tests | backward compat or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage / no direct graph reads |
| Focus Mode | provenance-linked context bundle | no hallucinated sources / no unsourced narrative |

### Next-evolution extension points

- (A) Data: new domain, new STAC/DCAT extensions
- (B) AI evidence: artifacts treated as first-class datasets with full provenance
- (C) Graph: new entity types with explicit provenance and stable IDs
- (D) API: new endpoints with contract tests and redaction expectations
- (E) UI: new layer registry entries with provenance pointers and CARE gating

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

### Minimum CI gates for “v12-ready” contributions

- [ ] Markdown protocol validation
- [ ] JSON schema validation for STAC, DCAT, and telemetry
- [ ] Graph integrity tests
- [ ] API contract tests
- [ ] UI layer registry schema checks
- [ ] Security and sovereignty scanning gates where applicable

### Reproduction workflow

~~~text
1) Identify what to reproduce
   - target commit SHA
   - target pipeline/module
   - target dataset(s) + boundary artifacts

2) Recreate the environment (repo-defined)
   - lockfiles / container / toolchain versions

3) Acquire inputs (public-safe or approved access)
   - confirm checksums + licensing

4) Run the pipeline entrypoint
   - capture logs + outputs + manifests

5) Validate boundary artifacts
   - schemas (STAC/DCAT/PROV) + link integrity

6) Compare fingerprints
   - stable IDs, hashes, counts, invariants

7) Record reproducibility evidence
   - run manifest + PROV + summary report
~~~

### Local commands (placeholders)

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

### Reviewer checklist (repro + governance)

- [ ] Reproduction entrypoint is clear (manifest/script/workflow)
- [ ] Inputs are documented and checksummed
- [ ] Outputs include STAC/DCAT/PROV boundary artifacts (or explicitly scoped out)
- [ ] Stable IDs do not drift unintentionally
- [ ] Sensitivity labels are present and not weakened downstream
- [ ] API/UI changes do not bypass contracts or redaction rules
- [ ] CI gates are satisfied (schemas, tests, security scans as applicable)

## ⚖ FAIR+CARE & Governance

### Governance review triggers

Governance review is required when changes introduce:

- new sensitive layers,
- new AI narrative behaviors,
- new external data sources,
- new public-facing endpoints.

### CARE / sovereignty considerations

- If reproduction involves culturally sensitive data or restricted locations:
  - document redaction/generalization behavior,
  - ensure review before publishing any artifacts,
  - ensure outputs are not less restricted than inputs.

### AI usage constraints

- AI-assisted outputs that surface in user-facing contexts must remain evidence-led, provenance-linked, and must not introduce unsourced claims.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial repro-kit README scaffold | TBD |
| v1.0.1 | 2025-12-29 | Align to canonical staging paths + boundary artifacts; add reproducibility contract + reviewer checklist | TBD |

---

Footer refs:

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract extension: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ingestion architecture: `docs/architecture/KFM_INGEST_ARCHITECTURE.md`
