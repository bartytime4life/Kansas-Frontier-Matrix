---
title: "KFM Reproducibility Kit"
path: ".github/repro-kit/README.md"
version: "v1.0.1"
last_updated: "2025-12-24"
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

> **Purpose (required):** Provide reproducibility helpers (scripts, composite actions, fixtures, and environment locks) that let contributors and reviewers reproduce KFM pipeline outputs and validation gates **without** relocating canonical artifacts from their governed homes.  

## 📘 Overview

### Purpose

This directory is the home for reproducibility helpers that make it easy to:

- reproduce **meaningful pipeline runs** across the canonical pipeline:
  **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**
- validate outputs against governed contracts and schemas,
- review PRs with a consistent “can we reproduce this?” checklist.

KFM’s architecture emphasizes deterministic, configuration-driven processing with comprehensive logging (including hashing inputs/outputs) so runs are verifiable and audit-friendly.

### Quick start (what to do in a PR)

1. Identify which pipeline stage(s) your change impacts (schemas / pipeline / graph / API / UI / story).
2. Run the smallest reproducible check (fixture or targeted validation) that exercises your change.
3. Create or update a **run record** under `mcp/runs/**` (manifest + hashes + provenance pointers).
4. Link the run record path in the PR description.

> Not confirmed in repo: the exact CLI commands/Make targets. Use the project’s existing scripts if present; otherwise, add wrappers under `.github/repro-kit/scripts/` and document them here.

### Scope

| In scope | Out of scope |
|---|---|
| Reproducing ETL/catalog/graph/API/UI/story outputs from the same inputs + config + code revision | Handling production secrets, credentials, or privileged access paths |
| Local/CI validation of STAC/DCAT/PROV artifacts and run provenance bundles | Defining new governance policies |
| CI-parity checks locally (“repo lint”, schema validation, contract tests) | Large-scale “full data” production replays of restricted datasets |
| Fixture-based regression runs (“golden” inputs + expected hashes/tolerances) | Publishing raw snapshots under `.github/` (use `data/<domain>/raw/`) |

### Audience

- Maintainers and reviewers validating reproducibility claims
- Contributors authoring pipelines, catalogs, schemas, APIs, UI layers, and Story Nodes
- CI maintainers (GitHub workflows / actions)

### Definitions

- **Deterministic:** same inputs + same config + same code revision ⇒ same outputs (byte-for-byte when practical).
- **Numerically reproducible:** outputs match within declared tolerances when bitwise identity is unrealistic (floating point / platform differences).
- **Idempotent:** running the same job twice does not duplicate records or produce inconsistent results.
- **Run record:** a portable folder capturing how to reproduce a run (manifest, hashes, pointers).
- **Run manifest:** the machine-readable part of a run record (inputs, config, versions, parameters, outputs).
- **PROV bundle:** provenance artifacts describing inputs, activities, outputs, and agents (`data/prov/**`).
- **Stable identifier:** an ID that should not change unexpectedly between runs; used to link STAC/DCAT/PROV to graph and UI.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical pipeline ordering + system inventory |
| Markdown templates | `docs/templates/` | Docs maintainers | Universal / Story Node / API contract templates |
| CI workflows README | `.github/workflows/README.md` | CI maintainers | CI gates, determinism, and contract checks |
| MCP workspace README | `mcp/README.md` | Research/AI maintainers | Run records live under `mcp/runs/**` |
| Releases README | `releases/README.md` | Release maintainers | Packaging/distribution edge (not canonical) |
| Schemas | `schemas/**` | Schema maintainers | Validation sources of truth |

### Definition of done

- [ ] This README is updated when repro-kit scripts/actions/fixtures are added or changed.
- [ ] Reviewers can identify the reproduction entrypoint (script, fixture, or run record) for substantive PRs.
- [ ] Repro steps align with minimum CI gates and do not bypass governance/sensitivity checks.
- [ ] Run records point to canonical artifacts (`data/prov/**`, `data/stac/**`, `data/catalog/dcat/**`) and do not duplicate them.

## 🗂️ Directory Layout

### This document

- `path`: `.github/repro-kit/README.md`

### Related repository paths

| Area | Canonical path | What lives here |
|---|---|---|
| Repro kit helpers | `.github/repro-kit/` | Scripts/actions/fixtures/env locks (helpers only) |
| CI workflows | `.github/workflows/` | Validation gates |
| Runs / experiments | `mcp/` | **Run records** (`mcp/runs/**`), experiments, SOPs |
| Pipelines | `src/pipelines/` | ETL + transforms + catalog build |
| Domain outputs | `data/<domain>/{raw,work,processed}/` | Canonical data products |
| STAC catalogs | `data/stac/collections/` and `data/stac/items/` | Canonical STAC outputs |
| DCAT catalogs | `data/catalog/dcat/` | Canonical DCAT outputs |
| PROV bundles | `data/prov/` | Canonical lineage bundles |
| Graph | `src/graph/` and import artifacts under `data/graph/` | Graph build + ingest artifacts |
| API boundary | `src/server/` (v13 target) or `src/api/` (legacy — not confirmed in repo) | Contracts + redaction rules |
| UI | `web/` | Map UI + layer registries |
| Story Nodes | `docs/reports/story_nodes/` | Governed narrative artifacts |
| Schemas | `schemas/` | JSON schemas + constraints |
| Tests | `tests/` | Unit/integration/contract tests |
| Tools | `tools/` | Operational tooling |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 repro-kit/
    ├── 📄 README.md
    ├── 📁 actions/            # optional: composite actions for CI reproducibility
    ├── 📁 scripts/            # optional: local wrappers for CI-equivalent checks
    ├── 📁 fixtures/           # optional: small “golden” datasets for deterministic test runs
    └── 📁 env/                # optional: environment lockfiles for deterministic execution
~~~

### Adjacent canonical homes this kit must point to

~~~text
📁 mcp/
└── 📁 runs/
    └── 📁 <run_id>/
        ├── 📄 manifest.json          # machine-readable run manifest (recommended)
        ├── 📄 run_report.md          # human-readable notes (optional)
        ├── 📄 checksums.sha256       # output hashes (recommended)
        └── 📄 provenance_refs.json   # pointers to data/prov/** (recommended)
~~~

> Not confirmed in repo: the exact filenames used in `mcp/runs/**`. Use this layout as a default until a governed schema exists under `schemas/telemetry/**`.

### Optional: release bundle layout (distribution only)

A “release” is a packaging/distribution event. Releases are **not** the canonical home for raw/working outputs; they should link back to canonical pipeline artifacts.

~~~text
📁 releases/
└── 📁 <version>/
    ├── 📄 manifest.zip
    ├── 📄 sbom.spdx.json
    ├── 📄 slsa-attestation.intoto.json
    ├── 📄 signature.sig
    └── 📄 checksums.sha256
~~~

## 🧭 Context

### Background

KFM’s platform emphasizes reproducibility:

- ETL steps are designed to be deterministic and logged, including hashing of input/output transformations for traceability.
- The system is configuration-driven so past versions can be regenerated by checking out the same code/config revision and re-running.

KFM also distinguishes between:
- **canonical evidence & lineage** (`data/stac/**`, `data/catalog/dcat/**`, `data/prov/**`), and
- **run records / research workspace** (`mcp/runs/**`), which should **point to** canonical artifacts rather than duplicating them.

### Assumptions

- The pipeline flow is preserved: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- The UI does not read Neo4j directly; the API boundary mediates access and enforces redaction/generalization.
- Contract and schema validation are treated as first-class build gates.

### Constraints / invariants

- Pipelines should be idempotent and deterministic (or tolerance-bounded with declared tolerance).
- Prefer every meaningful run to produce (or link to) a PROV activity bundle under `data/prov/**`.
- Run records under `mcp/runs/**` should contain **pointers/IDs** to PROV bundles and other canonical artifacts rather than duplicating provenance payloads.
- Catalog artifacts must validate against schemas under `schemas/**`.
- Do not commit secrets, tokens, or sensitive location details into repro-kit scripts, fixtures, logs, or CI artifacts.
- Releases (`releases/**`) are a distribution edge; do not treat them as canonical sources of truth for working data.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical run manifest schema for `mcp/runs/**`? | TBD | TBD |
| Which fixture datasets are safe to include publicly under `.github/repro-kit/fixtures/`? | TBD | TBD |
| What is the standard environment locking approach for pipelines and tests? | TBD | TBD |

### Future extensions

- Add composite actions under `.github/repro-kit/actions/` that run schema validation, contract tests, and reproducibility checks.
- Add fixture datasets and “golden output” hashes (or tolerances) for deterministic regression tests.
- Add environment locks under `.github/repro-kit/env/` for consistent local/CI execution.

## 🗺️ Diagrams

### System / reproducibility dataflow diagram

~~~mermaid
flowchart LR
  RK[Repro Kit<br/>.github/repro-kit] --> CI[CI Workflows<br/>.github/workflows]
  RK --> RUNS[Run Records<br/>mcp/runs]

  ETL[ETL] --> CATS[STAC/DCAT/PROV Catalogs]
  CATS --> GRAPH[Neo4j Graph]
  GRAPH --> API[API boundary]
  API --> UI[UI]
  UI --> SN[Story Nodes]
  SN --> FM[Focus Mode]

  RUNS -. pointers .-> CATS
~~~

### Optional sequence diagram: recording a repro run

~~~mermaid
sequenceDiagram
  participant Dev as Contributor
  participant RK as repro-kit
  participant V as Validators
  participant MCP as mcp/runs

  Dev->>RK: run local repro (fixture or targeted validation)
  RK->>V: validate docs + schemas + contracts
  V-->>RK: pass/fail + reports
  RK->>MCP: write manifest + hashes + provenance pointers
  MCP-->>Dev: run_id to link in PR
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Run record (manifest + logs) | JSON/YAML + text | `mcp/runs/**` | schema (if present) + review |
| Pipeline configuration | YAML/JSON | `src/pipelines/**` | lint + schema (if present) |
| Source references | URL/file refs | `data/<domain>/raw/**` | checksums + license metadata |
| Schemas | JSON Schema | `schemas/**` | CI schema validation |
| PROV bundles | JSON/Turtle | `data/prov/**` | PROV profile + integrity checks |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Run logs | text/JSON | `mcp/runs/**` | run-manifest schema if defined (not confirmed in repo) |
| PROV activity bundle | JSON/Turtle | `data/prov/**` | PROV profile |
| STAC collections/items | JSON | `data/stac/{collections,items}/` | STAC schemas |
| DCAT records | JSON-LD/RDF | `data/catalog/dcat/` | DCAT profile |
| Repro checksums | text | `mcp/runs/**/checksums.sha256` | sha256 format rule |

### Sensitivity & redaction

- Do not commit secrets or credentials into repro-kit.
- If a reproduction path touches sensitive locations or restricted data, ensure public artifacts are generalized/redacted and governance-reviewed.
- Treat CI logs and artifacts as public by default.

### Quality signals

- Determinism: repeated runs match expected hashes (or declared tolerances).
- Completeness: required catalogs and provenance artifacts exist for promoted outputs.
- Contract integrity: schemas and API contracts pass tests.

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Collections and Items live under `data/stac/collections/` and `data/stac/items/`.
- Repro steps should include validating these JSON artifacts against the repo’s STAC schemas.

### DCAT

- DCAT records live under `data/catalog/dcat/`.
- Repro steps should confirm minimal DCAT mappings exist for each dataset when required.

### PROV-O

- Prefer every meaningful run to produce (or link to) a PROV activity record linking inputs to outputs under `data/prov/**`.
- Run records in `mcp/runs/**` should point to PROV bundles, not duplicate them.

### Versioning

- Prefer stable identifiers and explicit predecessor/successor relationships for lineage.
- When output formats or schemas change, bump versions and update validation expectations.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Repro kit | Reproduction helpers and guidance | `.github/repro-kit/` |
| CI workflows | Gatekeeping + validation orchestration | GitHub checks + artifacts |
| MCP workspace | Run records & experiments | `mcp/runs/**` |
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
| Run record schema | `schemas/telemetry/**` (recommended) | SemVer + changelog (not confirmed in repo) |
| JSON schemas | `schemas/` | SemVer + changelog |
| STAC catalogs | `data/stac/` | Validate against schemas |
| DCAT catalogs | `data/catalog/dcat/` | Validate against schemas |
| PROV bundles | `data/prov/` | Validate to profile and integrity rules |
| API contracts | `src/server/contracts/` | Contract tests required |
| UI registries | `web/` | Validate against `schemas/ui/` |

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Reproducibility ensures Focus Mode’s context bundle remains provenance-linked and auditable.

### Provenance-linked narrative rule

- Every factual claim must trace to a dataset, record, or asset identifier.
- Predictive or AI-generated content must be opt-in and carry uncertainty metadata; it must never appear as unmarked fact.

### Evidence rule (fact vs inference)

When a repro run produces narrative-adjacent artifacts (summaries, extractions, classifications):

- label **fact vs inference vs hypothesis** in run reports,
- link to the underlying evidence (STAC/DCAT/PROV + source documents),
- require human review before publishing downstream narrative.

## 🧪 Validation & CI/CD

### Validation steps

Minimum CI gates for “v12/v13-ready” contributions include:

- [ ] Markdown protocol validation
- [ ] JSON schema validation for STAC, DCAT, PROV, Story Nodes, UI registries, and telemetry (when present)
- [ ] Graph integrity tests (where graph outputs are impacted)
- [ ] API contract tests (where API boundary changes)
- [ ] UI layer registry schema checks
- [ ] Secret/PII scans
- [ ] Security and sovereignty scanning gates where applicable

### Run manifest skeleton (example)

~~~yaml
# Example only — not a governed schema (yet)
run_id: "2025-12-24T000000Z__example__<shortsha>"
commit_sha: "<latest-commit-hash>"
pipeline_stage: ["ETL", "Catalog", "Graph"]
inputs:
  - ref: "data/<domain>/raw/<file-or-url>"
    sha256: "<sha256>"
outputs:
  prov_bundle_ref: "data/prov/<bundle>.json"
  stac_refs:
    - "data/stac/collections/<collection>.json"
    - "data/stac/items/<item>.json"
  dcat_refs:
    - "data/catalog/dcat/<dataset>.jsonld"
checks:
  schema_validation: "pass|fail"
  contract_tests: "pass|fail|skip"
environment:
  os: "<runner-os>"
  python: "<version>"
  node: "<version>"
parameters:
  random_seed: 12345
notes:
  numeric_tolerance: "TBD (only if needed)"
~~~

### Reproduction

~~~bash
# Replace with repo-specific commands as they are added.

# 1) Run schema validation for catalogs and metadata
# <TBD>

# 2) Run unit/integration tests (pipelines / graph / API / UI)
# <TBD>

# 3) Run doc lint and markdown protocol checks
# <TBD>

# 4) Write a run record under mcp/runs/** and link it in your PR
# <TBD>
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| repro_run_id | repro-kit scripts/actions | `mcp/runs/**` |
| schema_validation_summary | validators | CI logs / `mcp/runs/**` |
| hash_comparison_report | repro-kit | CI artifacts / `mcp/runs/**` |
| provenance_bundle_ref | pipeline | `data/prov/**` (referenced from `mcp/runs/**`) |

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is required when changes introduce:

- new sensitive layers,
- new AI narrative behaviors,
- new external data sources,
- new public-facing endpoints,
- changes that affect classification/sensitivity handling or redaction rules.

### CARE / sovereignty considerations

- Do not commit fixtures that reveal restricted locations or culturally sensitive details.
- Prefer synthetic test data and generalized coordinates where needed.
- Outputs derived from restricted inputs must not be published as open unless proven safe and governance-reviewed.

### AI usage constraints

- AI-assisted outputs that surface in user-facing contexts must remain evidence-led and provenance-linked.
- Prohibited: generating new policy text or inferring sensitive locations (see front-matter).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.1 | 2025-12-24 | Align repro-kit with MCP run-record conventions and release packaging boundaries | TBD |
| v1.0.0 | 2025-12-22 | Initial repro-kit README scaffold | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- CI workflows: `.github/workflows/README.md`
- MCP workspace: `mcp/README.md`
- Releases: `releases/README.md`
