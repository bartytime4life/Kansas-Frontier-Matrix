---
title: ".github/actions/dcat-validate/config — README"
path: ".github/actions/dcat-validate/config/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:github-actions:dcat-validate:config-readme:v1.0.0"
semantic_document_id: "kfm-github-actions-dcat-validate-config-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:dcat-validate:config-readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# dcat-validate config

## 📘 Overview

### Purpose
This directory holds configuration files consumed by the `dcat-validate` composite GitHub Action.

The goal is to make DCAT validation behavior explicit, reviewable, and reproducible (configuration-as-code), without requiring code edits for routine rule/profile tuning.

### Scope
| In Scope | Out of Scope |
|---|---|
| Validator configuration (rules, profiles, paths, suppressions) | GitHub workflow wiring (`.github/workflows/*`) |
| Non-secret settings that should be code-reviewed | Secrets / tokens / credentials |
| Repo-default settings shared across workflows | Dataset content itself (`data/*`) |

### Audience
- Primary: CI/CD maintainers; catalog maintainers
- Secondary: contributors adding datasets or changing DCAT generation

### Definitions (link to glossary)
- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc:
  - **DCAT**: dataset catalog metadata (W3C vocabulary)
  - **Profile**: KFM’s constrained interpretation of a standard (e.g., `KFM-DCAT v11.0.0`)
  - **Suppression**: an explicit “allow this known issue” entry, time-bounded and justified

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Action overview | `.github/actions/dcat-validate/README.md` | CI maintainers | What the action validates + contract |
| Scripts overview | `.github/actions/dcat-validate/scripts/README.md` | CI maintainers | How config is loaded/used |
| Config files | `.github/actions/dcat-validate/config/*` | CI maintainers | This directory |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Config naming + purpose documented (no “mystery files”)
- [ ] Safe defaults explained (what fails CI vs what warns)
- [ ] “Where to change what” is clear for contributors
- [ ] No secrets encouraged or referenced

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/dcat-validate/config/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Workflows | `.github/workflows/` | CI pipelines calling composite actions |
| Action | `.github/actions/dcat-validate/` | Composite action entrypoint + docs |
| Config | `.github/actions/dcat-validate/config/` | Validator configuration (this folder) |
| Catalog outputs | `data/catalog/dcat/` *(expected; not confirmed in repo)* | DCAT datasets produced by pipeline |
| Schemas | `schemas/` *(expected; not confirmed in repo)* | Validation assets (JSON Schema / SHACL) |

### Expected file tree for this sub-area
~~~text
📁 .github/
└── 📁 actions/
    └── 📁 dcat-validate/
        ├── 📁 config/
        │   ├── 📄 README.md
        │   ├── 📄 <config-file-1>        # not confirmed in repo
        │   ├── 📄 <config-file-2>        # not confirmed in repo
        │   └── 📁 <optional-subdir>/     # not confirmed in repo
        ├── 📁 scripts/
        │   └── 📄 README.md
        └── 📄 README.md
~~~

## 🧭 Context

### Background
KFM’s pipeline treats **catalog artifacts** (STAC/DCAT/PROV) as machine-validated outputs. This configuration directory supports a CI validation gate by providing a stable, version-controlled place for validator settings.

### Assumptions
- The action’s scripts read at least one config file from this directory. *(not confirmed in repo)*
- The repo emits DCAT dataset metadata under `data/catalog/dcat/`. *(not confirmed in repo)*

### Constraints / invariants
- Config changes must be deterministic (no environment-specific behavior).
- Config changes must be reviewable (avoid hidden defaults in workflow YAML).
- UI/clients should not bypass the API layer to read catalogs directly.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the canonical config filename and schema for this action? | CI maintainer | TBD |
| Do we validate DCAT in JSON-LD, Turtle, or both? | Catalog maintainer | TBD |
| Do we publish a machine-readable validation report artifact? | CI maintainer | TBD |

### Future extensions
- Add schema validation for the config itself (JSON Schema) and run it in CI.
- Support “strict” vs “warn-only” policies by branch / tag / environment.
- Time-bound suppressions (expiry dates) to prevent permanent exceptions.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Catalog build] --> B[DCAT datasets<br/>data/catalog/dcat/]
  B --> C[CI: dcat-validate action]
  C --> D[PR status checks]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Validator config | YAML/JSON *(recommended)* | `.github/actions/dcat-validate/config/` | Config schema *(recommended; not confirmed in repo)* |
| DCAT dataset files | JSON-LD/Turtle *(not confirmed in repo)* | `data/catalog/dcat/` | DCAT validator (tooling depends on implementation) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| CI check result | GitHub Check | PR / workflow run | Action exit code + logs |
| Validation report *(optional)* | Text/JSON *(not confirmed in repo)* | workflow artifacts *(not confirmed in repo)* | TBD |

### Sensitivity & redaction
- Config files here should remain **non-sensitive**. Do not place secrets, credentials, or private endpoints in this folder.

### Quality signals
Recommended quality signals for validation config:
- Explicit “fail vs warn” policy separation
- Allowlist / suppression list is justified and time-bounded
- Stable path globs (avoid absolute paths or runner-specific directories)

## 🌐 STAC, DCAT & PROV Alignment

### DCAT
- Target profile: `KFM-DCAT v11.0.0`.
- Typical validation aims (examples; align with your validator implementation):
  - Required identifiers present
  - License/publisher/contact fields present
  - Spatial/temporal coverage present when applicable

### PROV-O
If validation reports are emitted as artifacts:
- Prefer a provenance note that can be tied back to the workflow run (e.g., workflow run ID as an Activity identifier).

## 🧱 Architecture

### How config should be used
- Scripts should load config from this directory via an explicit path (no implicit CWD assumptions).
- Defaults should live in-version here, not hidden inside workflow YAML.
- Tool versions (validator/runtime) should be pinned in the action to keep validation stable.

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Config schema *(recommended)* | `schemas/` *(not confirmed in repo)* | Semver + changelog |
| Validator behavior | `.github/actions/dcat-validate/scripts/` | Pin tool versions in the action |

## 🧠 Story Node & Focus Mode Integration
This action is CI-only and does not directly feed Story Nodes or Focus Mode.

However, passing validation is a prerequisite for catalog artifacts to be considered “publishable” inputs to downstream stages.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front-matter + structure)
- [ ] Config lint (YAML/JSON syntax) *(recommended)*
- [ ] DCAT validation against profile

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) Lint config (if adopted):
#    yamllint .github/actions/dcat-validate/config/

# 2) Run DCAT validation locally (example shape):
#    .github/actions/dcat-validate/scripts/validate_dcat.sh \
#      --config .github/actions/dcat-validate/config/<config-file> \
#      --inputs data/catalog/dcat/
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- CI maintainer review: required
- Data/catalog maintainer review: recommended when rule/profile changes affect data publication

### CARE / sovereignty considerations
- Ensure validation does not require exposing restricted datasets in CI logs/artifacts.

### AI usage constraints
- This directory is configuration for validation; no AI generation or inference is intended.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial config README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`