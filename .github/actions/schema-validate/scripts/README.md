---
title: "KFM Schema Validate Action — Scripts README"
path: ".github/actions/schema-validate/scripts/README.md"
version: "v1.0.0"
last_updated: "2025-12-23"
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
care_label: "N/A"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:ci:schema-validate-scripts-readme:v1.0.0"
semantic_document_id: "kfm-ci-schema-validate-scripts-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:ci:schema-validate-scripts-readme:v1.0.0"
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

# KFM Schema Validate Action — Scripts README

## 📘 Overview

### Purpose
- This README documents the helper scripts used by the repository’s `schema-validate` GitHub Action.
- These scripts enforce “contract validity” in CI by validating structured artifacts (schemas + generated outputs) before merge.

### Scope
| In Scope | Out of Scope |
|---|---|
| Scripts in `.github/actions/schema-validate/scripts/` | Defining the schemas themselves (owned by `schemas/`) |
| How scripts should behave (deterministic, read-only, actionable errors) | ETL logic, catalog build logic, graph build logic |
| Local reproduction guidance for contributors | Changing workflow triggers / branch protections |

### Audience
- Primary: CI/CD maintainers, DataOps, schema owners
- Secondary: ETL/catalog/graph/API/UI contributors debugging contract failures

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **JSON Schema**: Machine-checkable definition of structure/constraints.
  - **Contract artifact**: STAC/DCAT/PROV outputs (and other registries) that must validate against schemas.
  - **Validator**: Tooling (node/python/etc.) that evaluates data files against schemas.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Schema validation action | `.github/actions/schema-validate/` | CI/CD | Action wrapper (entrypoint not confirmed in repo) |
| Scripts directory | `.github/actions/schema-validate/scripts/` | CI/CD | This README + script implementations |
| Schema store | `schemas/` | Schema owners | Expected home for JSON Schemas |
| Contract outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Pipelines | Typical catalog/provenance outputs (verify in repo) |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Script behavior rules (determinism, exit codes, logging) are explicit
- [ ] Local reproduction steps are present (even if placeholders)
- [ ] Governance/security considerations documented

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/schema-validate/scripts/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| GitHub Actions | `.github/actions/` | Local actions used by workflows |
| Workflows | `.github/workflows/` | CI pipelines that call actions |
| Schemas | `schemas/` | JSON Schemas for catalogs/registries/contracts |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Generated contract artifacts |
| API contracts (if present) | `src/server/contracts/` | Contract tests at API boundary |

### Expected file tree for this sub-area
~~~text
📁 .github/
└── 📁 actions/
    └── 📁 schema-validate/
        └── 📁 scripts/
            ├── 📄 README.md
            ├── 📄 validate-stac.<sh|py|js>
            ├── 📄 validate-dcat.<sh|py|js>
            ├── 📄 validate-prov.<sh|py|js>
            └── 📄 validate-ui-registry.<sh|py|js>
~~~

## 🧭 Context

### Background
KFM treats catalog and provenance artifacts as contracts that bound the system. CI schema validation ensures these artifacts remain machine-valid and consistent with the schema store.

### Assumptions
- GitHub-hosted runners provide a POSIX shell; additional runtimes (Python/Node) depend on workflow setup.
- Scripts are invoked by a local action (e.g., `action.yml`) and should run from repository root.

### Constraints / invariants
- **Deterministic**: same inputs → same results; no nondeterministic ordering in outputs.
- **Read-only**: scripts must not modify tracked files.
- **Offline**: no external network calls during validation.
- **Clear exit codes**: `0` success, non-zero failure.
- **Actionable logs**: errors must identify file path + rule/schema name (when possible).
- **Safe logging**: do not dump full sensitive payloads; show minimal snippets.

### Open questions
- Which validator stack is canonical (Node Ajv vs Python jsonschema vs other)? (not confirmed in repo)

### Future extensions
- Add summary annotations for PRs (GitHub step summary) with counts and top failures.
- Parallelize validation by domain (STAC/DCAT/PROV/UI) for faster CI.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart TB
  PR[Pull Request] --> WF[GitHub Workflow]
  WF --> ACT[Local Action: schema-validate]
  ACT --> SCRIPTS[Scripts in /scripts]
  SCRIPTS --> SCHEMAS[Schemas in /schemas]
  SCRIPTS --> TARGETS[Targets: data/*, docs/*, web/*]
  SCRIPTS --> RESULT{Pass?}
  RESULT -- yes --> MERGE[Allow merge]
  RESULT -- no --> FAIL[Fail check + report]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant GH as GitHub Actions
  participant Act as schema-validate action
  participant S as scripts/
  participant Sch as schemas/
  participant T as target files
  GH->>Act: Invoke action
  Act->>S: Run validators
  S->>Sch: Load schema(s)
  S->>T: Validate files
  S-->>Act: Report pass/fail + diagnostics
  Act-->>GH: Set job status (success/failure)
~~~

## 📦 Data & Metadata

### Inputs
- Target file globs/paths provided by workflow/action configuration.
- Schema files from `schemas/`.
- Optional configuration for exclusions/allowlists (not confirmed in repo).

### Outputs
- Console logs suitable for CI.
- Optional machine-readable report artifact (JSON) for downstream parsing (not confirmed in repo).

### Sensitivity & redaction
- Do not print full contents of failing files if they can contain sensitive locations or personal data.
- Prefer:
  - File path + JSON pointer (if available)
  - Schema rule name
  - Small excerpt around the failing field

### Quality signals
- Coverage: % of expected contract artifacts validated.
- Clarity: errors pinpoint the failing file + reason.
- Speed: runtime stays within CI budget.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Expected: validate STAC Items/Collections against STAC + KFM STAC profile.
- Expected: enforce item↔collection integrity and broken-link checks (implementation not confirmed in repo).

### DCAT
- Expected: validate DCAT records against KFM DCAT profile and required fields.

### PROV-O
- Expected: validate provenance bundles (structure + required identifiers) against KFM PROV profile.

### Versioning
- Scripts should report (in logs) the active schema/profile version(s) when possible.
- Changes to `schemas/` should be reviewed as contract changes and may require updating script logic.

## 🧱 Architecture

### Components
- Local GitHub Action: `.github/actions/schema-validate/`
- Validator scripts: `.github/actions/schema-validate/scripts/`
- Schema store: `schemas/`
- Targets: generated artifacts under `data/` and other registries/docs as configured

### Interfaces / contracts
- Contract: scripts accept target path(s) via arguments or environment variables (match the action implementation).
- Contract: scripts must return a non-zero exit code on the first failure (or after collecting failures, if designed that way).

### Extension points checklist (for future work)
- [ ] Shared “common” library script for:
  - glob expansion
  - ignore patterns
  - stable sorting of file lists
- [ ] Per-domain validators (STAC/DCAT/PROV/UI) that compose cleanly
- [ ] Structured report output (`json`), plus a concise CI summary

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Indirect: Story Nodes/Focus Mode depend on provenance-linked artifacts being structurally valid.
- If Story Node validation is part of CI, document the target + schema in this action (not confirmed in repo).

### Provenance-linked narrative rule
- Schema validation is a prerequisite for provenance-linked UI consumption: invalid catalogs/provenance should never be merged.

### Optional structured controls
- N/A

## 🧪 Validation & CI/CD

### Validation steps
- Run schema validation in CI on every PR that touches:
  - `schemas/`
  - `data/**` contract outputs
  - any registry files consumed by UI/API (as configured)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) list scripts and run help
ls -la .github/actions/schema-validate/scripts
bash .github/actions/schema-validate/scripts/<script-name> --help

# 2) run a validator against a target directory
bash .github/actions/schema-validate/scripts/<script-name> --target data/<domain> --schema schemas/<schema>.json
~~~

### Telemetry signals (if applicable)
- CI failure rate by domain (STAC/DCAT/PROV/UI)
- Runtime per validator
- Top recurring schema violations

## ⚖ FAIR+CARE & Governance

### Review gates
- Human review required for:
  - Any changes to `schemas/` (contract changes)
  - Any changes to validation behavior that might allow invalid artifacts to pass
- Prefer having a schema owner approve schema changes.

### CARE / sovereignty considerations
- Validation logs should not increase disclosure risk; keep errors minimal and avoid dumping sensitive records.

### AI usage constraints
- N/A for scripts themselves, but do not use AI tools to generate schemas or validators without review + test coverage.

## 🕰️ Version History
| Version | Date | Change | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial governed README for schema-validate scripts | <author> |
