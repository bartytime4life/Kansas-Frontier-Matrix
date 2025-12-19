---
title: "KFM GitHub Actions Local Actions"
path: ".github/actions/README.md"
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

doc_uuid: "urn:kfm:doc:github:actions-readme:v1.0.0"
semantic_document_id: "kfm-github-actions-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:actions-readme:v1.0.0"
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

# KFM GitHub Actions Local Actions

## 📘 Overview

### Purpose
- Provide a single place to document **local GitHub Actions** (usually composite actions) stored in `.github/actions/`.
- Standardize how local actions are authored and consumed by workflows in `.github/workflows/` so CI gates remain consistent and reusable across the repository.

### Scope

| In Scope | Out of Scope |
|---|---|
| Local actions in `.github/actions/` | Editing workflow definitions in `.github/workflows/` |
| How to add, version, and test local actions | Production deployment infrastructure |
| How local actions map to KFM CI gates | Replacing project governance/security policies |

### Audience
- Primary: repo maintainers and contributors who create or modify CI checks
- Secondary: reviewers who need to understand what CI jobs are doing and where logic lives

### Definitions
- Link: `../../docs/glossary.md`
- Terms used in this doc:
  - **Local action**: a repo-contained action referenced as `./.github/actions/<name>`
  - **Composite action**: an action that composes multiple steps and shells via `runs: using: composite`
  - **Workflow**: a `.github/workflows/*.yml` pipeline that calls actions
  - **CI gate**: a required validation check enforced on PRs and mainline builds

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This directory | `.github/actions/` | TBD | Local actions live here |
| Workflow entry points | `.github/workflows/` | TBD | Calls local actions |
| Canonical pipeline and CI gates | `docs/MASTER_GUIDE_v12.md` | TBD | Defines minimum CI gates and pipeline ordering |
| Doc templates | `docs/templates/` | TBD | Used for governed documentation |
| Schemas | `schemas/` | TBD | JSON schemas, telemetry schemas |
| Data catalogs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | TBD | Standard outputs validated by CI |

### Definition of done
- [ ] Front-matter complete + valid
- [ ] Local actions directory conventions explained
- [ ] Action inventory table exists (even if partially populated)
- [ ] CI gates mapping is documented
- [ ] Security and sovereignty considerations are stated

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Local actions | `.github/actions/` | Reusable repo-contained actions |
| Workflows | `.github/workflows/` | CI pipelines that call local actions |
| Documentation | `docs/` | Canonical governed docs and templates |
| Data domains | `data/` | Raw/work/processed outputs and catalogs |
| Schemas | `schemas/` | Schema definitions and validators |
| Graph | `src/graph/` | Graph build + ontology bindings |
| APIs | `src/server/` | API layer that fronts the graph |
| Frontend | `web/` | React and map UI |

### Expected file tree for this sub-area
~~~text
📁 .github/
├── 📁 actions/
│   ├── 📄 README.md
│   ├── 📁 <action_name>/
│   │   ├── 📄 action.yml
│   │   ├── 📄 README.md
│   │   ├── 📁 scripts/
│   │   │   └── 📄 <optional helper scripts>
│   │   └── 📁 fixtures/
│   │       └── 📄 <optional test fixtures>
└── 📁 workflows/
    └── 📄 <workflow>.yml
~~~

## 🧭 Context

### Background
KFM uses CI not only to run tests, but to enforce:
- governed Markdown protocol and documentation structure
- standards-based catalogs and provenance outputs
- stable graph and API contracts
- UI registry consistency and security safeguards

Local actions are the mechanism to keep these checks:
- consistent across workflows
- easier to update without copy-pasting YAML
- reviewable as “units” of CI behavior

### Assumptions
- Workflows use a repository checkout step before calling local actions.
- Local actions may call repository scripts or validators (preferred) rather than duplicating logic in YAML.

### Constraints / invariants
- Canonical pipeline ordering is preserved: ETL → Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode.
- Frontend consumes contracts via APIs and does not read the graph directly.
- Local actions must not introduce secrets, credentials, or PII into logs.
- When checks concern sensitive or restricted locations, action behavior must support redaction or gating per governance docs.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which local actions currently exist in this repo | TBD | TBD |
| Do we require SHA pinning for third-party actions in workflows | TBD | TBD |
| How are CI reports persisted, if at all | TBD | TBD |

### Future extensions
- Add an automated “Action Index” check that validates each action has an `action.yml` and a per-action `README.md`.
- Add a consistent output format for CI gates so PR checks are predictable and easy to interpret.

## 🗺️ Diagrams

### CI and local actions flow
~~~mermaid
flowchart LR
  PR[Pull request] --> WF[Workflow in .github/workflows]
  WF --> LA[Local actions in .github/actions]
  LA --> REP[Checks and artifacts]
  LA --> REPO[Repo scripts, schemas, and validators]
  REPO --> REP
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Workflow definitions | YAML | `.github/workflows/` | YAML lint where applicable |
| Local action definitions | YAML + shell | `.github/actions/<name>/action.yml` | `action.yml` schema, basic smoke run |
| Schemas | JSON | `schemas/` | JSON schema validators |
| Catalog outputs | JSON | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Schema + integrity checks |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Job status | GitHub Checks | CI UI | Required checks configuration |
| Validation logs | text | CI logs | Must not leak secrets |
| Optional reports | SARIF / JSON / artifacts | Workflow artifacts | Must match repository expectations |

### Sensitivity and redaction
- Any action that scans content for restricted locations, credentials, or sensitive text must:
  - avoid printing sensitive matches
  - prefer counts, hashes, or redacted excerpts over raw content

### Quality signals
- Deterministic outcomes for identical inputs
- Clear error messages that identify:
  - the failing contract or schema
  - the file path or identifier involved
  - how to reproduce locally when possible

## 🌐 STAC, DCAT & PROV Alignment

### STAC
Local actions may validate:
- STAC JSON schema validity
- item and collection integrity
- link integrity and required fields

### DCAT
Local actions may validate:
- DCAT record schema validity
- required mappings such as title, description, license, and keywords

### PROV-O
Local actions may validate:
- existence and basic shape of PROV activity records for transforms
- presence of stable identifiers for activities and agents

## 🧱 Architecture

### Action design rules
- **Single responsibility**: one action corresponds to one CI gate or tightly related set of checks.
- **Parameterizable**: accept inputs for paths, strictness, or modes rather than hardcoding.
- **Deterministic**: avoid time-based outputs unless explicitly required.
- **No hidden network dependency**: if external calls are required, document them and ensure they are allowed by policy.

### Referencing local actions in workflows
~~~yaml
# Example usage pattern
- name: Run a local gate
  uses: ./.github/actions/<action_name>
  with:
    mode: "strict"
~~~

### Action inventory
Populate this table as local actions are created or discovered.

| Action | Path | CI gate category | Used by workflows | Notes |
|---|---|---|---|---|
| TBD | `.github/actions/TBD` | TBD | TBD | TBD |

## 🧪 Validation and CI/CD

### Minimum CI gates
See `docs/MASTER_GUIDE_v12.md` for the minimum CI gates expected for “v12-ready” contributions.

### Local testing
If you add or modify an action:
- Ensure the action has a per-action `README.md` explaining inputs, outputs, and examples.
- Ensure failure modes produce clear messages and do not leak sensitive data.
- Prefer exercising the action via its calling workflow in a PR to confirm end-to-end behavior.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial `.github/actions` documentation scaffold | TBD |

---

Footer refs:
- Master guide: `../../docs/MASTER_GUIDE_v12.md`
- Universal doc template: `../../docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `../../docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `../../docs/governance/ETHICS.md`
- Sovereignty: `../../docs/governance/SOVEREIGNTY.md`