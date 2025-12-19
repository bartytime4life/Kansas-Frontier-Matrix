---
title: "GitHub Action — markdown-lint"
path: ".github/actions/markdown-lint/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
status: "draft"
doc_kind: "CI Action Doc"
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

doc_uuid: "urn:kfm:doc:github:actions:markdown-lint:readme:v1.0.0"
semantic_document_id: "kfm-github-action-markdown-lint-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:actions:markdown-lint:readme:v1.0.0"
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

# GitHub Action — markdown-lint

## 📘 Overview

### Purpose
This composite GitHub Action runs a Markdown lint pass as part of KFM’s CI gates, helping keep governed documentation (including templates, Story Nodes, and subsystem docs) consistent and reviewable.

This action is intended to support the “Markdown protocol checks” expectation for v12-ready contributions, alongside other validators (e.g., schema validation for catalogs).  

### Scope

| In Scope | Out of Scope |
|---|---|
| Lint Markdown files using a repo-approved ruleset and/or config. | Validating STAC/DCAT/PROV JSON/JSON-LD schemas (use dedicated validators). |
| Failing CI on lint violations to keep docs consistent. | Auto-generating or rewriting narrative content. |
| Producing actionable CI feedback (exit code / annotations if supported by implementation). | Enforcing historical truth or source correctness (handled by review + evidence linking rules). |

### Audience
- Primary: Repo maintainers and CI/CD owners
- Secondary: Contributors authoring docs, Story Nodes, or action READMEs

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: “governed docs”, “Markdown protocol”, “Story Node”, “CI gate”

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Composite action definition | `.github/actions/markdown-lint/action.yml` | CI maintainers | **not confirmed in repo** (expected GitHub Action entrypoint). |
| Local lint config (action-scoped) | `.github/actions/markdown-lint/config/` | CI maintainers | **not confirmed in repo** (recommended place for action-specific config). |
| Helper scripts | `.github/actions/markdown-lint/scripts/` | CI maintainers | **not confirmed in repo** (recommended for deterministic script wrappers). |
| Markdown protocol baseline | `docs/MASTER_GUIDE_v12.md` | Docs maintainers | Source of truth for pipeline invariants and CI expectations. |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Mentions only repo-grounded paths or clearly labels “not confirmed in repo”
- [ ] Explains where configuration and scripts should live (and how they relate to CI)
- [ ] Validation steps listed and repeatable

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/markdown-lint/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub Actions (local) | `.github/actions/` | Composite/local actions used by workflows |
| Workflows | `.github/workflows/` | CI pipelines that call this action |
| Documentation | `docs/` | Canonical governed docs (templates, guides, story nodes) |

### Expected file tree for this sub-area
~~~text
📁 .github/
└── 📁 actions/
    └── 📁 markdown-lint/
        ├── 📄 README.md
        ├── 📄 action.yml                  (not confirmed in repo)
        ├── 📁 config/                     (not confirmed in repo)
        │   └── 📄 README.md               (optional; explain config usage)
        └── 📁 scripts/                    (not confirmed in repo)
            └── 📄 README.md               (optional; explain helper scripts)
~~~

## 🧭 Context

### Background
KFM relies on governed Markdown documentation to keep the pipeline understandable, auditable, and reviewable. The canonical pipeline ordering must remain intact, and CI gates are expected to enforce documentation quality alongside schema validation and tests.

A Markdown lint action provides a consistent, automated check so documentation stays readable and structurally consistent across:
- subsystem docs (`docs/`)
- templates (`docs/templates/`)
- Story Nodes (`docs/reports/.../story_nodes/`)
- action docs (`.github/actions/**/README.md`)

### Assumptions
- The lint engine and rule configuration are defined in the composite action implementation (**not confirmed in repo**).
- The lint process is deterministic and does not mutate repository files (no auto-fix in CI unless explicitly designed and approved).

### Constraints / invariants
- The canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- This action must not bypass governance (e.g., must not introduce generated policy text or infer sensitive locations).
- CI should remain reproducible (same inputs → same results).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What lint engine is standardized (and where is its version pinned)? | CI maintainers | TBD |
| Where is the canonical lint ruleset stored (root config vs action-scoped config)? | CI maintainers + Docs maintainers | TBD |
| Do we want “warnings only” in PRs, or “fail on error” for all protected branches? | Repo maintainers | TBD |

### Future extensions
- Add a dedicated “KFM Markdown Protocol” validator step (beyond style lint) if the repo defines machine-checkable protocol rules.
- Emit GitHub annotations to highlight exact lint failures inline in PR diffs (if not already supported).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Pull Request / Push] --> B[GitHub Workflow Job]
  B --> C[Local Composite Action: markdown-lint]
  C --> D[Markdown Lint Engine + Ruleset]
  D --> E{Violations?}
  E -- No --> F[CI Pass]
  E -- Yes --> G[CI Fail + Feedback]
~~~

## 📦 Data & Metadata

### Inputs
> Authoritative inputs MUST be documented in `.github/actions/markdown-lint/action.yml`.  
> The list below is a suggested shape only (**not confirmed in repo**).

| Input | Format | Where from | Validation |
|---|---|---|---|
| `paths` | glob(s) / newline list | workflow `with:` | Ensure paths stay within repo |
| `config_path` | file path | workflow `with:` or default | File must exist (if set) |
| `fail_on_error` | boolean | workflow `with:` or default | Must be explicit for protected branches |

### Outputs
This action is expected to communicate results via step exit code; it may optionally emit structured outputs (**not confirmed in repo**).

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Lint status | exit code | CI logs | GitHub Actions conventions |
| Optional report | JSON/text | workspace artifact | **not confirmed in repo** |

### Sensitivity & redaction
- Markdown lint should not print secrets or tokens.
- If logs include file paths, avoid leaking sensitive directories beyond repo contents (standard GitHub Actions behavior is acceptable).

### Quality signals
- Clean lint pass indicates consistent formatting and reduces review friction.
- Persistent failure patterns can signal needed template updates or clearer authoring guidelines.

## 🌐 STAC, DCAT & PROV Alignment
This action does not validate STAC/DCAT/PROV artifacts directly. It complements catalog validators by ensuring the *documentation describing* those artifacts remains consistent and readable.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Workflow job | Invokes lint gate | `.github/workflows/*.yml` |
| Composite action | Wraps lint behavior | `uses: ./.github/actions/markdown-lint` |
| Lint engine + config | Applies rules to Markdown | Defined by action implementation |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| This action’s contract | `.github/actions/markdown-lint/action.yml` | Semver bump if inputs/behavior change |
| Markdown protocol baseline | `docs/MASTER_GUIDE_v12.md` | Update with governance review |

### Extension points checklist (for future work)
- [ ] Add action-scoped config under `.github/actions/markdown-lint/config/`
- [ ] Add helper scripts under `.github/actions/markdown-lint/scripts/` for determinism
- [ ] Add workflow-level allowlist for docs paths vs generated artifacts

## 🧠 Story Node & Focus Mode Integration
This action helps ensure Story Node Markdown remains consistent with repo-wide lint rules, which supports:
- consistent headings/structure for ingestion and rendering
- cleaner diffs and review cycles
- fewer formatting regressions in Focus Mode narrative surfaces

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Run markdown lint in CI using this action
- [ ] Ensure the workflow targets all governed docs directories
- [ ] Confirm no auto-fix behavior occurs unless explicitly approved

### Reproduction
~~~bash
# Replace these placeholders with the repo’s chosen lint command/tooling.
# Goal: make local results match CI results exactly.

# 1) Install the repo’s lint tooling (if needed)
# 2) Run lint against the same paths as CI
# 3) Confirm the same config is applied
~~~

### Example workflow usage (illustrative; align with repo workflow conventions)
~~~yaml
jobs:
  markdown_lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Markdown lint (KFM)
        uses: ./.github/actions/markdown-lint
        with:
          # paths/config inputs are illustrative; see action.yml for authoritative inputs
          paths: |
            docs/**/*.md
            .github/**/*.md
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| Lint pass/fail rate | CI logs | GitHub Actions run history |

## ⚖ FAIR+CARE & Governance

### Review gates
- Doc lint rule changes should be reviewed by:
  - Docs maintainers
  - CI maintainers
- If lint rules affect public-facing narrative behavior, mark **requires human review**.

### CARE / sovereignty considerations
- Linting does not change content, but it should not encourage adding sensitive location detail.
- Maintain the prohibition on inferring sensitive locations in narratives.

### AI usage constraints
- This doc inherits the repo’s baseline AI constraints from governed documentation templates.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README for markdown-lint action | TBD |