---
title: "Schema Validate Action — KFM CI Contract Gate"
path: ".github/actions/schema-validate/README.md"
version: "v1.0.0"
last_updated: "2025-12-23"
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

doc_uuid: "urn:kfm:doc:ci:action:schema-validate-readme:v1.0.0"
semantic_document_id: "kfm-ci-action-schema-validate-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:ci:action:schema-validate-readme:v1.0.0"
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

# Schema Validate Action

## 📘 Overview

### Purpose

- Document the reusable GitHub Action in `.github/actions/schema-validate/` that implements KFM’s **schema validation** CI gate.
- Provide a stable place for contributors to understand what “schema validation” means in KFM, what it targets, and how to run it consistently across workflows.

### Scope

| In Scope | Out of Scope |
|---|---|
| Validating **contract artifacts** and **evidence artifacts** (e.g., STAC/DCAT/PROV JSON/JSON-LD) against schemas in `schemas/`. | Running ETL, generating catalogs, or producing graph imports. |
| Deterministic pass/fail behavior suitable for CI gating. | “Best effort” linting that never fails the build. |
| Repo-local usage via `uses: ./.github/actions/schema-validate`. | Enforcing repository structure beyond what is required to validate the targeted files. |

### Audience

- Primary: KFM maintainers and CI owners working on validation gates.
- Secondary: Domain contributors adding datasets, catalogs, and schemas.

### Definitions

- Link: `docs/glossary.md`
- **Contract artifact**: machine-validated schema/spec that governs an interface boundary (e.g., JSON Schema).
- **Evidence artifact**: machine-validated outputs consumed downstream (e.g., STAC/DCAT/PROV artifacts).
- **Schema validation gate**: CI step that fails the build when governed artifacts are present but invalid.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM Core Team | Canonical pipeline and non-negotiable ordering. |
| Schemas root | `schemas/` | Contracts maintainers | Authoritative schemas for governed outputs. |
| STAC outputs | `data/stac/` | Catalog maintainers | Collections + Items to validate when present. |
| DCAT outputs | `data/catalog/dcat/` | Catalog maintainers | DCAT JSON-LD to validate when present. |
| PROV outputs | `data/prov/` | Pipeline maintainers | Lineage bundles to validate when present. |
| This action | `.github/actions/schema-validate/` | CI maintainers | Reusable gate invoked from workflows. |

### Definition of done

- [ ] Front-matter complete + valid
- [ ] README describes what is validated and what is skipped
- [ ] Usage example shows how workflows should call the action
- [ ] Behavior is deterministic: valid → pass; invalid → fail; absent targets → skip with clear messaging
- [ ] Governance and sovereignty considerations for logs are stated

## 🗂️ Directory Layout

### This document

- `path`: `.github/actions/schema-validate/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub actions | `.github/actions/` | Reusable actions used by CI workflows |
| Schemas | `schemas/` | JSON Schemas and other contract artifacts |
| STAC | `data/stac/` | STAC collections/items produced by pipelines |
| DCAT | `data/catalog/dcat/` | DCAT outputs (often JSON-LD) |
| PROV | `data/prov/` | PROV bundles for lineage |
| Workflows | `.github/workflows/` | CI workflows that call this action |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 schema-validate/
        ├── 📄 README.md
        ├── 📄 action.yml
        ├── 📁 scripts/
        │   └── 📄 validate.* 
        └── 📁 fixtures/
            └── 📁 catalogs/
                └── 📁 stac/
                    └── 📁 edge_cases/
                        └── 📄 README.md
~~~

## 🧭 Context

### Background

KFM relies on governed contracts so that each stage can evolve without breaking downstream consumers. Schema validation is a minimum CI gate to prevent invalid STAC/DCAT/PROV artifacts from entering the repo and cascading into graph ingest, API responses, and UI evidence rendering.

### Assumptions

- `schemas/` contains the authoritative schemas for the governed artifacts this action checks.
- Catalog outputs are stored under canonical homes (`data/stac/`, `data/catalog/dcat/`, `data/prov/`) when present.
- Workflows may run on repos/branches that do not contain all optional roots; the action must handle that cleanly.

### Constraints / invariants

- Preserve the canonical ordering: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- Deterministic CI behavior:
  - Skip when optional roots or targets are absent.
  - Fail when targets are present but invalid.
- Do not leak sensitive information in logs:
  - Prefer printing file paths and validation errors without dumping full payloads.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which validator(s) are used for JSON Schema and JSON-LD validation | CI maintainers | TBD |
| What is the standard output format for CI annotations and summaries | CI maintainers | TBD |
| Should schema validation be strict-by-default or allow warning-only modes | Governance + CI | TBD |

### Future extensions

- Add SHACL validation for RDF-aligned outputs when applicable.
- Add a “changed-files only” mode to reduce CI time for large catalogs.
- Add a machine-readable report artifact for downstream CI gates.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  PR[Pull Request / Push] --> WF[GitHub Workflow Job]
  WF --> ACT[Action: schema-validate]
  ACT --> S[schemas/]
  ACT --> STAC[data/stac/]
  ACT --> DCAT[data/catalog/dcat/]
  ACT --> PROV[data/prov/]
  ACT -->|valid| OK[✅ Pass gate]
  ACT -->|invalid| FAIL[❌ Fail gate]
~~~

### Sequence diagram

~~~mermaid
sequenceDiagram
  participant WF as Workflow
  participant ACT as schema-validate action
  participant FS as Repo files
  WF->>ACT: uses ./.github/actions/schema-validate
  ACT->>FS: read schemas + targeted artifacts
  ACT->>ACT: run validators
  ACT-->>WF: exit 0 on success
  ACT-->>WF: exit 1 on failure
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Contract schemas | JSON Schema (and related) | `schemas/` | Must be internally consistent and resolvable |
| STAC Collections/Items | JSON | `data/stac/**` | Validate against STAC-related schemas when present |
| DCAT datasets | JSON-LD or JSON | `data/catalog/dcat/**` | Validate against DCAT mapping schema when present |
| PROV bundles | JSON-LD or JSON | `data/prov/**` | Validate against PROV mapping schema when present |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| CI pass/fail | process exit code | workflow job | GitHub Actions convention |
| Validation summary | text / markdown | GitHub step summary | Must not leak sensitive data |
| Optional report artifact | JSON | workflow artifact | Not yet standardized |

### Sensitivity & redaction

- Validation output must avoid printing full document bodies when they may contain sensitive location details or other restricted fields.
- Prefer reporting: file path, schema name, and the smallest possible error context.

### Quality signals

- Number of files validated (by type).
- “Skipped because absent” counts (explicitly reported).
- Strictness mode (if configurable) recorded in the summary.

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Collections involved: `data/stac/collections/**`
- Items involved: `data/stac/items/**`
- Extensions: profile-specific; governed under `schemas/` and KFM STAC profile.

### DCAT

- Dataset identifiers: governed by KFM DCAT profile.
- License mapping: required fields must validate at the schema level.

### PROV-O

- `prov:wasDerivedFrom`: must be representable in the chosen PROV serialization and validated at the schema level where applicable.
- `prov:wasGeneratedBy`: activity identity should remain stable and machine-checkable.

### Versioning

- Schemas should follow semantic versioning and maintain a changelog.
- Changes that tighten validation rules should be communicated clearly because they can break existing artifacts.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| GitHub workflow | Calls validation gates | `.github/workflows/*.yml` |
| schema-validate action | Runs validators and reports results | `uses: ./.github/actions/schema-validate` |
| Schemas root | Holds authoritative contracts | `schemas/` |
| Catalog outputs | Evidence artifacts to validate | `data/stac/`, `data/catalog/dcat/`, `data/prov/` |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| Action interface | `.github/actions/schema-validate/action.yml` | Inputs/outputs versioned with action |

### Usage

In a workflow job:

~~~yaml
jobs:
  schema_validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Validate governed schemas and artifacts
        uses: ./.github/actions/schema-validate
        with:
          # See action.yml for the authoritative list of inputs.
          # Keys below are illustrative placeholders and may differ.
          schemas_dir: schemas
          targets: |
            schemas/**/*.json
            data/stac/**/*.json
            data/catalog/dcat/**/*.json
            data/catalog/dcat/**/*.jsonld
            data/prov/**/*.json
            data/prov/**/*.jsonld
~~~

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- This action does not render UI itself, but it protects downstream Focus Mode by ensuring the evidence artifacts (catalogs + provenance) are structurally valid before they are ingested or served.

### Provenance-linked narrative rule

- Schema validation supports the “provenance-first” rule by ensuring catalog/provenance artifacts remain machine-readable and contract-compliant.

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
- [ ] Schema validation for governed outputs (STAC/DCAT/PROV and other contract artifacts as configured)
- [ ] Deterministic behavior: skip absent targets; fail invalid targets

### Reproduction

~~~bash
# CI path (recommended):
# - run the workflow that invokes this action

# Local path (TBD; must match the implementation in action.yml/scripts):
# - run the same validator command(s) pinned by the action
# - validate the same target globs used in CI
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| Files validated | action runtime | workflow logs / summaries |
| Failures by type | validator output | workflow logs / summaries |

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes to schemas or validation rules can change what is acceptable as evidence artifacts and should be reviewed by the relevant maintainers.
- If new artifact types are validated here, ensure their canonical home and governance review triggers are documented.

### CARE / sovereignty considerations

- Avoid emitting sensitive locations or restricted details into public CI logs.
- Prefer high-level error summaries and link contributors to local reproduction steps.

### AI usage constraints

- This document inherits the repo’s governance references and prohibits generating policy or inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial action README scaffold | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
