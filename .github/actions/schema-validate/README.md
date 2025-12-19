---
title: "GitHub Action — Schema Validate"
path: ".github/actions/schema-validate/README.md"
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

doc_uuid: "urn:kfm:doc:github-actions:schema-validate:readme:v1.0.0"
semantic_document_id: "kfm-gha-schema-validate-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:schema-validate:readme:v1.0.0"
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

# GitHub Action — Schema Validate

## 📘 Overview

### Purpose
This GitHub Action runs **schema validation** as a CI gate, ensuring that JSON-based artifacts in the repo
(e.g., schemas, registries, catalogs, and other contract files) remain **machine-validated** and safe to consume
downstream.

This supports KFM’s pipeline invariant: **ETL → Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode** by
catching contract breaks early. See: `docs/MASTER_GUIDE_v12.md`.

### Scope

| In Scope | Out of Scope |
|---|---|
| Validate JSON files against JSON Schema contracts | STAC semantic checks (use `.github/actions/stac-validate`) |
| Validate schema files for basic correctness and reference resolution | Vulnerability/dependency scanning (use `.github/actions/security-scan`) |
| Enforce “CI-clean” contract discipline for schemas/registries used by the pipeline | Neo4j constraint checks / graph integrity checks (handled elsewhere) |

### Audience
- Primary: CI maintainers, DataOps maintainers, pipeline engineers
- Secondary: Contributors adding or modifying schemas, catalog JSON, or UI registries

### Definitions
- Link: `docs/glossary.md`
- Terms used in this doc: JSON Schema, contract, registry, STAC, DCAT, PROV, telemetry

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This action README | `.github/actions/schema-validate/README.md` | CI maintainers | Governed description of intent + usage |
| Action definition | `.github/actions/schema-validate/action.yml` | CI maintainers | Source of truth for inputs/outputs |
| JSON Schemas | `schemas/` | DataOps | SemVer + changelog expected |
| Catalog and metadata JSON | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | DataOps | Validity is required for downstream graph/API work |
| UI registries | `web/` | UI team | Any registry files should be schema validated |

### Definition of done
- [ ] Front-matter complete + `path` matches file location
- [ ] Validation intent is clearly stated (what is validated vs not validated)
- [ ] Local reproduction guidance exists (even if tool-specific details live in `action.yml`)
- [ ] Security notes included (no secrets, no sensitive leakage in logs)
- [ ] References to KFM invariants and governance are present

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/schema-validate/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub Actions | `.github/actions/` | Composite/local actions used by CI workflows |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Data catalogs | `data/stac/` | STAC Items + Collections |
| Dataset catalogs | `data/catalog/dcat/` | DCAT 3 records |
| Lineage | `data/prov/` | PROV-O bundles |
| Frontend registries | `web/` | Layer registries and UI configuration files |

### Expected file tree for this sub-area
~~~text
📁 .github/
├── 📁 actions/
│   ├── 📁 schema-validate/
│   │   ├── 📄 README.md
│   │   └── 📄 action.yml
│   ├── 📁 stac-validate/
│   └── 📁 security-scan/
~~~

## 🧭 Context

### Background
KFM depends on **contracted, machine-validated artifacts**. Schema drift or invalid JSON commonly fails late
(at catalog build, API contract tests, or UI runtime). This action pushes those failures left into CI.

### Assumptions
- JSON Schemas are stored under `schemas/`.
- The action’s authoritative behavior (inputs/outputs/globs/validator runtime) is defined in `action.yml`.
- CI workflows call this action on PRs that touch schema-governed files.

### Constraints / invariants
- The canonical pipeline ordering is preserved and documented in `docs/MASTER_GUIDE_v12.md`.
- The UI never reads Neo4j directly; contracts must be enforced at the API layer.
- Validation must be deterministic and reproducible (same inputs → same results).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What file globs are covered by default | TBD | TBD |
| Which validator runtime is standard for the repo | TBD | TBD |
| Do we emit structured results (e.g., SARIF) | TBD | TBD |

### Future extensions
- Add schema validation for additional registries (e.g., layer registries, telemetry payloads).
- Add a “changed files only” mode to speed up PR checks while keeping full validation on main.

## 🗺️ Diagrams

### System and CI dataflow
~~~mermaid
flowchart LR
  PR[Pull Request changes] --> CI[CI job: schema-validate]
  CI --> S1[Validate schemas]
  CI --> S2[Validate instances]
  S1 --> Gate[Pass or fail gate]
  S2 --> Gate
  Gate --> Downstream[Safe to run catalogs/API/UI checks]
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Schema documents | JSON | `schemas/` | Must be valid JSON + internally consistent |
| Schema-governed instances | JSON | Repo paths configured in `action.yml` | Must validate against selected schema(s) |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| CI pass/fail | Exit code | GitHub Actions step result | Non-zero on any validation error |
| Human-readable report | Log output | Workflow logs | Keep logs free of secrets/PII |

### Sensitivity & redaction
- Do not print secrets, tokens, or environment values.
- If validation errors include excerpts from documents, ensure those documents are not restricted content
  (or redact in logging behavior as required by governance).

### Quality signals
- Total validations run (schemas + instances)
- Error count by category (parse error vs schema error vs reference error)
- Deterministic ordering for output to make diffs stable

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- This action may validate STAC JSON against local schemas if configured, but **STAC semantic validation**
  (collection-item integrity, required links, extension rules) is handled by `.github/actions/stac-validate`.

### DCAT
- DCAT records should be validated against a repo-approved schema or shape (implementation-specific).

### PROV-O
- PROV bundles should be validated for structural correctness where schemas exist.

### Versioning
- If schemas are versioned (recommended), this action should enforce:
  - stable schema IDs and references
  - backwards-compat behavior rules (where defined by repo standards)

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| GitHub workflow | Orchestrates CI | `.github/workflows/*.yml` |
| schema-validate action | Runs validations | `.github/actions/schema-validate/action.yml` |
| Schemas | Define contracts | `schemas/` |
| Instances | Must conform | configured globs |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | SemVer + changelog recommended |
| UI registries schemas | `schemas/` + `web/` | Schema change requires UI review |
| Catalog schemas | `schemas/` + `data/stac/` / `data/catalog/dcat/` / `data/prov/` | Must remain machine-validated |

### Extension points checklist
- [ ] Add new schema under `schemas/` with a stable ID
- [ ] Update `action.yml` globs/mapping to include new instance locations
- [ ] Add tests (if repo has contract tests) for representative valid/invalid instances
- [ ] Ensure downstream docs reference the new schema

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
Schema validity is a prerequisite for any content served into Focus Mode contexts:
- Catalog JSON validity supports provenance-linked narratives.
- Registry validity supports consistent UI rendering of layers and audit notices.

### Provenance-linked narrative rule
- This action does not create narratives.
- It supports the rule by preventing broken contracts that would block provenance linkage downstream.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Run schema validator against schema files
- [ ] Validate instances against schemas per `action.yml` mapping
- [ ] Fail CI on any errors

### Reproduction
The exact validator and command line are implementation-defined. Use `action.yml` as the source of truth.

Examples of local approaches (choose the one matching the repo’s implementation):

~~~bash
# Example approach A: Node-based validator (AJV)
# npx ajv-cli validate -s schemas/<schema>.json -d <instances-glob>

# Example approach B: Python-based validator
# python -m pip install jsonschema
# python -c "import json, jsonschema; ..."

# Example approach C: Dedicated schema tool
# <tool> validate --schema <schema> --data <file-or-glob>
~~~

### Telemetry signals
| Signal | Source | Where recorded |
|---|---|---|
| Validation errors count | CI job logs | Workflow logs (and optional artifacts) |
| Files validated | CI job logs | Workflow logs |

## ⚖ FAIR+CARE & Governance

### Review gates
- Schema changes that affect public outputs: requires human review (DataOps + relevant subsystem owner).
- Any schema that touches sensitive/restricted content: requires governance review per:
  - `docs/governance/ROOT_GOVERNANCE.md`
  - `docs/governance/SOVEREIGNTY.md`

### CARE / sovereignty considerations
- This action should not broaden access to restricted data.
- Validation logs must avoid echoing restricted content.

### AI usage constraints
- This doc does not authorize AI-generated policy. It permits summarization/structure extraction only.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial action README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`