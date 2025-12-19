---
title: "KFM Repro Kit README"
path: ".github/repro-kit/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:github:repro-kit:readme:v1.0.0"
semantic_document_id: "kfm-github-repro-kit-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:repro-kit:readme:v1.0.0"
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

# KFM Repro Kit

## 📘 Overview

### Purpose
- Provide a **single, contributor-facing entry point** for how to reproduce KFM checks locally and how to capture run metadata consistently.
- Reduce review friction by making “CI parity” expectations explicit and repeatable.

### Scope
| In Scope | Out of Scope |
|---|---|
| Local reproduction workflow guidance | Defining new project-wide policy |
| Checklists that mirror expected CI gates | Provisioning cloud infra, deploying services |
| Run metadata capture conventions (manifests/logs) | Storing secrets or privileged credentials |
| Cross-stage “what to validate” guidance | Writing or modifying the actual pipeline implementation |

### Audience
- Primary: contributors preparing PRs (data, ETL, graph, API, UI, Story Nodes)
- Secondary: reviewers, maintainers, CI workflow authors

### Definitions
- Link: `docs/glossary.md` (if present)
- Terms used here:
  - **Repro run**: a locally-executed set of validations intended to match CI behavior.
  - **CI parity**: local results match (or explainably differ from) CI checks.
  - **Repro manifest**: a small record of *what ran*, *with what inputs*, *what outputs*, and *from which commit*.

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Canonical pipeline + invariants | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Non-negotiable ordering + subsystem contracts |
| Documentation templates | `docs/templates/` | Core maintainers | Use governed templates for docs/contracts |
| Data staging + catalog outputs | `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` | Data owners | Outputs must be machine-validated |
| Catalog schemas + validators | `schemas/` | Data/Platform | STAC/DCAT/PROV alignment expectations |
| Runs / experiment artifacts | `mcp/runs/` (recommended) | Contributors | Store run logs, manifests, diffs |
| Tests | `tests/` | Contributors | Unit/integration/contract tests |

### Definition of done for this document
- [ ] Front-matter complete + valid
- [ ] Contains a clear “what to run” checklist for CI parity
- [ ] Does **not** prescribe unverifiable repo-specific commands as facts
- [ ] Includes provenance and sensitivity guidance (FAIR+CARE + sovereignty)
- [ ] Aligns with KFM pipeline ordering and API boundary invariants

## 🗂️ Directory Layout

### This document
- `path`: `.github/repro-kit/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| CI workflows | `.github/workflows/` | GitHub Actions workflows that enforce gates (if present) |
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Documentation | `docs/` | Canonical governed docs |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Graph | `src/graph/` | Ontology bindings + graph build |
| APIs | `src/server/` | Contracted access layer (REST/GraphQL) |
| Frontend | `web/` | React + map clients |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Tests | `tests/` | Test suites and fixtures |
| Tools | `tools/` | Dev utilities, validators, linters (if present) |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area
~~~text
📁 .github/
└── 📁 repro-kit/
    └── 📄 README.md
~~~

## 🧭 Context

### Background
KFM’s architecture is intentionally contract-driven: data is ingested and normalized, cataloged with STAC/DCAT/PROV, materialized into a graph, exposed through APIs, rendered in the UI, and finally used to build Story Nodes and Focus Mode narratives.

This “Repro Kit” exists to keep contributor workflows aligned with those contracts and to make it easy to reproduce checks consistently before submitting changes.

### Assumptions
- CI exists and enforces gates (check `.github/workflows/` if present).
- Contributors may run subsets of the pipeline locally depending on the change type.
- “Reproducible” means: identical or explainably equivalent results given the same inputs, commit, and environment constraints.

### Constraints and invariants
- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend consumes data via **API contracts**, not by querying the graph directly.
- Provenance is first-class: outputs should link back to inputs and transformation activities.
- No unsourced narrative in Focus Mode contexts.
- Do not introduce secrets, private keys, or sensitive location inference in artifacts committed to the repo.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What are the canonical local commands for “CI parity” checks (lint/test/schema/build)? | TBD | TBD |
| Where is the canonical location for repro manifests in this repo (`mcp/runs/` vs alternative)? | TBD | TBD |
| Which checks are mandatory for each change type (data-only vs code-only vs story-only)? | TBD | TBD |

### Future extensions
- Add `.github/repro-kit/checklists/` with stage-specific checklists.
- Add a `repro-manifest` schema and a small helper script to generate it.
- Add a “CI parity” composite action that standardizes common checks.

## 🗺️ Diagrams

### System and dataflow
~~~mermaid
flowchart LR
  Dev[Contributor] --> RK[Repro Kit guidance]
  RK --> A[ETL]
  A --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React and Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Optional sequence diagram
~~~mermaid
sequenceDiagram
  participant Dev as Contributor
  participant Local as Local Runner
  participant Art as Run Artifacts

  Dev->>Local: Run repro checks for change type
  Local->>Local: Validate schemas + tests + build steps
  Local->>Art: Write repro manifest + logs + diffs
  Art-->>Dev: Attach links/paths in PR description
~~~

## 📦 Data and Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Code revision | git commit | local checkout | clean working tree recommended |
| Raw sources | files / APIs | `data/raw/` or external | documented source + license |
| Working transforms | files | `data/work/` | deterministic transforms preferred |
| Processed outputs | files | `data/processed/` | schema + QA checks |
| Catalog artifacts | STAC/DCAT/PROV | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | schema validation + link integrity |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Repro manifest | JSON/YAML | `mcp/runs/<run_id>/manifest.(json|yaml)` (recommended) | TBD |
| Logs | text | `mcp/runs/<run_id>/logs/` (recommended) | n/a |
| Reports | files | `mcp/runs/<run_id>/reports/` (recommended) | n/a |
| Catalog diffs | text/json | alongside run artifacts | STAC/DCAT/PROV integrity |

### Sensitivity and redaction
- If artifacts include sensitive sites, locations, or culturally restricted information, follow `docs/governance/SOVEREIGNTY.md`.
- Prefer generalized geometry, bounding boxes, or redacted coordinates in public outputs when required.

### Quality signals
- Schema validation passes for STAC/DCAT/PROV artifacts.
- Deterministic outputs where expected (stable IDs, fixed seeds).
- Graph integrity checks pass (constraints, expected labels/relationships).
- API contract tests pass (or explicitly versioned changes are documented).
- UI builds and accessibility checks pass for affected components.
- Story Nodes are evidence-led with dataset/document identifiers for factual claims.

## 🌐 STAC, DCAT and PROV Alignment

### STAC
- Collections involved: change-dependent
- Items involved: change-dependent
- Extensions: change-dependent

### DCAT
- Dataset identifiers: change-dependent
- License mapping: ensure explicit license is recorded for published datasets
- Contact and publisher mapping: ensure publisher/contact fields exist where required

### PROV-O
- `prov:wasDerivedFrom`: raw → processed lineage should be representable
- `prov:wasGeneratedBy`: each significant transform should be representable as an activity
- Activity and agent identities: align with the repo’s PROV conventions (if defined)

### Versioning
- New dataset versions should link predecessor/successor.
- Graph should mirror dataset lineage where applicable.

## 🧱 Architecture

### Components and responsibilities
- **Repro Kit README**: defines “what to validate” and “how to capture evidence.”
- **CI workflows**: enforce gates on PRs (if present).
- **Pipeline code**: implements ETL/catalog/graph build.
- **Schemas and validators**: define machine-checkable expectations.
- **Run artifacts**: preserve reproducibility and review evidence.

### Interfaces and contracts
- Repro runs should validate **contracts at boundaries**:
  - Catalog schema integrity
  - Graph constraints and migrations
  - API contract compatibility
  - UI build correctness and a11y expectations
- Repro runs should not bypass the API boundary by coupling UI directly to graph internals.

### Extension points checklist
- Adding a dataset: validate ETL outputs + catalogs (+ optional graph/API/UI integrations).
- Adding a new analysis product: validate catalogs, graph ingestion, API exposure, UI rendering, story linkage.
- Adding a story node type: validate provenance, graph references, API payload shape, UI rendering, telemetry signals.

## 📚 Story Node and Focus Mode Integration

- Story Nodes should be evidence-led and should reference dataset/document identifiers.
- Focus Mode narratives must not introduce unsourced claims; reproduction checks should include a review step for provenance completeness.

## ✅ Validation and CI/CD

### CI parity checklist
Use the checklist below as a **minimum** before requesting review:

- [ ] Workspace clean: no uncommitted changes except intentional outputs excluded by `.gitignore`
- [ ] Lint and formatting checks pass for touched code
- [ ] Unit tests pass for touched packages/modules
- [ ] Integration tests pass for touched boundaries (graph/API/UI as applicable)
- [ ] STAC/DCAT/PROV outputs validate (if catalogs changed)
- [ ] Graph build and constraints checks pass (if graph changed)
- [ ] API contract checks pass (if API changed)
- [ ] UI build and a11y checks pass (if UI changed)
- [ ] Story Node evidence completeness reviewed (if story content changed)
- [ ] Repro manifest and logs captured for non-trivial changes

### How to run locally
This repo’s exact commands are intentionally **not hard-coded** here unless they exist and are stable.
Recommended approach:
1. Check for documented developer workflows in `docs/` (start with `docs/MASTER_GUIDE_v12.md`).
2. Check for repo helper entry points (examples: `Makefile`, `tools/`, `scripts/`, package managers) if present.
3. If no canonical command set exists yet, propose one in a PR and wire it into CI.

Example placeholder structure only:
~~~bash
# Example placeholders — replace with repo-specific commands if/when standardized.
# 1) Lint/format
# <lint-command>

# 2) Tests
# <test-command>

# 3) Catalog validation
# <stac-validate-command>
# <dcat-validate-command>
# <prov-validate-command>

# 4) Graph checks
# <graph-build-command>
# <graph-constraints-command>

# 5) API and UI
# <api-contract-test-command>
# <ui-build-command>
# <ui-a11y-command>
~~~

### Telemetry signals
When possible, record:
- run_id, timestamp, git SHA, OS/toolchain details
- datasets touched and their identifiers
- generated artifacts and their paths
- warnings/errors and mitigation notes

Store these in a repro manifest alongside logs to support review and future audits.

## 🧾 FAIR+CARE and Governance

- Treat sovereignty, culturally sensitive content, and location data with care:
  - generalize/redact when required
  - avoid “exact coordinate” disclosure in public artifacts when sensitive
- Follow `docs/governance/ETHICS.md` and `docs/governance/SOVEREIGNTY.md` where applicable.
- Avoid “policy invention” in documentation: changes that affect governance must be marked for human review.

## 🕰️ Version History
- v1.0.0 (2025-12-19): Initial Repro Kit README scaffold aligned to KFM governed doc protocol.