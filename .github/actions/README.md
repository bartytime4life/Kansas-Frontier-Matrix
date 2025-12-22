---
title: ".github/actions — Local GitHub Actions (KFM)"
path: ".github/actions/README.md"
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

doc_uuid: "urn:kfm:doc:github:actions:readme:v1.0.0"
semantic_document_id: "kfm-github-actions-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:actions:readme:v1.0.0"
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

# .github/actions — Local GitHub Actions (KFM)

## 📘 Overview

### Purpose
This directory holds **repository-local GitHub Actions** (primarily *composite actions*) used by CI workflows to enforce KFM’s **contract-first** validation gates across the canonical pipeline:

**ETL → STAC/DCAT/PROV → Neo4j Graph → API → UI → Story Nodes → Focus Mode**

This README defines how actions in this folder should be structured, documented, and safely reused.

### Scope

| In Scope | Out of Scope |
|---|---|
| Reusable actions called by `.github/workflows/*` | Defining workflow triggers / job matrices (belongs in workflows) |
| Validation “gates” (schema checks, Story Node checks, contract checks) | Cloud deployment and runtime ops |
| Action structure, naming, inputs/outputs, and safety rules | Secret provisioning/rotation and org-level GitHub settings |
| Repo-lint guardrails for action authoring | Non-CI automation not run by GitHub Actions |

### Audience
- Primary: CI maintainers, contracts owners (schemas + API contracts), repo maintainers
- Secondary: Contributors adding new datasets/domains, Story Node authors/curators

### Definitions (link to glossary)
- Glossary: `docs/glossary.md` (if present)
- **Composite Action**: A GitHub Action implemented as a YAML step list in `action.yml`
- **Gate**: A required check that must pass for “CI green”
- **Contract**: A schema/spec that producers/consumers must obey (e.g., STAC/DCAT/PROV, Story Nodes, API contracts)

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Local reusable actions | `.github/actions/` | TBD | This folder |
| Workflows (callers) | `.github/workflows/` | TBD | Workflows invoke local actions |
| Schemas (contracts) | `schemas/` | TBD | Canonical schema home; validated in CI |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | TBD | Validated against schemas |
| Story Nodes | `docs/reports/story_nodes/` | TBD | Must validate before publish |
| API contracts | `src/server/contracts/` | TBD | Must validate + pass contract tests |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory conventions documented (action layout, naming, inputs/outputs)
- [ ] CI gate mapping aligns with current KFM design docs
- [ ] Safety guidance included (permissions, secrets hygiene, determinism)
- [ ] Examples clearly marked as placeholders where repo content is unknown

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Local GitHub Actions | `.github/actions/` | Reusable actions (composite, node, docker) used by workflows |
| GitHub Workflows | `.github/workflows/` | CI definitions that call these actions |
| Schemas/contracts | `schemas/` | JSON Schema / constraints used by validators |
| Pipelines | `src/pipelines/` | ETL + catalog build (validated via CI gates) |
| Graph | `src/graph/` | Ontology bindings + ingest tooling (validated via integrity tests) |
| API | `src/server/` | Contracted API boundary (contract tests in CI) |
| UI | `web/` | Map UI + layer registries (schema-checked in CI) |
| Story | `docs/reports/story_nodes/` | Draft/published story nodes + assets |

### Suggested local action structure (example skeleton)
> This is a recommended structure. Folder/action names below are illustrative.

~~~text
📁 .github/
└── 📁 actions/
    ├── 📄 README.md
    └── 📁 <action-name>/                  # kebab-case (recommended)
        ├── 📄 action.yml                  # GitHub Action definition
        ├── 📄 README.md                   # action-specific docs (inputs/outputs/examples)
        ├── 📁 scripts/                    # optional helper scripts (bash/python/node)
        └── 📁 fixtures/                   # optional lightweight test fixtures (if needed)
~~~

### Naming conventions
- Action folder names: `kebab-case` (recommended)
- Prefer names that match CI gates (examples): `validate-markdown`, `validate-schemas`, `validate-story-nodes`, `api-contract-tests`, `security-scan`
- Avoid ambiguous names like `check` or `validate`

## 🧭 Context

### Why this folder exists
KFM’s v12+ direction is “contracts-first” and “evidence-first”, with CI expected to enforce:
- Markdown protocol validation
- Schema validation
- Story Node validation
- API contract tests
- Security and sovereignty scanning gates

Local actions allow these checks to be:
- **Reusable** across workflows
- **Consistent** across domains
- **Versionable** (by commit SHA via the repo)

### Drift prevention (design intent)
Design notes indicate the repo has referenced **schemas and composite actions** in CI/workflows even when canonical roots were missing; local actions should help make CI deterministic and explicit.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  PR[Pull Request / Push] --> WF[.github/workflows/*]
  WF --> ACT[.github/actions/* (local actions)]
  ACT --> G1[Markdown protocol gate]
  ACT --> G2[Schema validation gate]
  ACT --> G3[Story Node validation gate]
  ACT --> G4[API contract tests]
  ACT --> G5[Security & sovereignty scans]
~~~

## 📦 Data & Metadata

### Artifacts commonly validated by CI actions
| Artifact type | Canonical path (expected) | Notes |
|---|---|---|
| Schemas (contracts) | `schemas/**` | Validators should read from canonical contract home |
| STAC outputs | `data/stac/**` | Validate against `schemas/stac/**` |
| DCAT outputs | `data/catalog/dcat/**` | Validate against `schemas/dcat/**` |
| PROV outputs | `data/prov/**` | Validate against `schemas/prov/**` |
| Story Nodes | `docs/reports/story_nodes/**` | Validate front-matter, citations, entity refs, redaction rules |
| API contracts | `src/server/contracts/**` | Validate + contract-test responses |
| UI registries | `web/**/layers/**` | Schema validation for layer registry configs |

### Determinism rule (CI)
Actions should:
- fail deterministically when a required artifact exists but is invalid
- optionally skip checks when optional roots are absent (when configured)

## 🌐 STAC, DCAT & PROV Alignment

### What actions must preserve
Where actions validate STAC/DCAT/PROV artifacts:
- validation must reference the canonical schemas under `schemas/`
- validators must treat machine-validated catalogs as first-class artifacts
- failures must include actionable error messages (what failed + where)

## 🧱 Architecture

### Action design principles
- **Single responsibility**: one action ≈ one “gate”
- **Parameterize paths**: default to canonical paths; allow overrides via inputs
- **Least privilege**: prefer minimal permissions in workflows; actions should not assume elevated privileges
- **No secrets leakage**: never echo secrets; redact env output; avoid printing full tokens/credentials
- **No YAML front-matter in code files**: do not use `---` YAML front-matter separators inside `action.yml` or scripts

### Contracts are canonical (reminder)
- Schema/spec sources belong in `schemas/`
- API contracts belong under the canonical API contract home
- CI actions should validate contracts and fail when contracts are present but invalid

## 🧠 Story Node & Focus Mode Integration

### Story Node validation intent
Actions supporting Story Nodes should ensure:
- front-matter present and valid
- citations/evidence references resolve
- entity references are consistent with the graph/IDs (where validation is available)
- redaction/generalization rules are enforced for restricted content

### Focus Mode rule of thumb
Focus Mode should only consume provenance-linked content; Story Node validation actions are a primary enforcement point.

## 🧪 Validation & CI/CD

### Recommended gate-to-action mapping (suggested)
> Names are illustrative; create/rename actions to match repo reality.

| Gate | Suggested local action | Typical inputs |
|---|---|---|
| Markdown protocol validation | `validate-markdown` | `paths`, `fail_on_warnings` |
| Schema validation | `validate-schemas` | `schemas_dir`, `targets`, `fail_on_missing` |
| Story Node validation | `validate-story-nodes` | `story_dir`, `published_only` |
| API contract tests | `api-contract-tests` | `contract_dir`, `base_url` (if applicable) |
| Security/sovereignty scans | `security-scan` | `policy_refs`, `severity_threshold` |

### Example workflow usage (placeholder)
~~~yaml
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # Placeholder example — replace with the actual action names in this repo
      - name: Validate schemas
        uses: ./.github/actions/validate-schemas
        with:
          schemas_dir: schemas
          fail_on_missing: false
~~~

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate schemas
# 2) run unit/integration tests
# 3) run doc lint
~~~

## ⚖ FAIR+CARE & Governance

### Governance approvals required (if any)
- FAIR+CARE council review: TBD
- Security council review: TBD
- Historian/editor review: TBD

### CARE / sovereignty considerations
- Actions that validate or publish artifacts should not expand or expose restricted locations.
- Any redaction/generalization rules must be enforced at the appropriate boundary (CI validation, API contracts, Story Node publication rules).

### AI usage constraints
- This document’s AI permissions/prohibitions must be respected (see front-matter).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial `.github/actions` README scaffold | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
