---
title: "GitHub Action — Markdown Lint"
path: ".github/actions/markdown-lint/README.md"
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

doc_uuid: "urn:kfm:doc:github:action:markdown-lint:v1.0.0"
semantic_document_id: "kfm-github-action-markdown-lint-v1.0.0"
event_source_id: "ledger:kfm:doc:github:action:markdown-lint:v1.0.0"
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

# GitHub Action — Markdown Lint

## 📘 Overview

### Purpose
- Provide a single, reusable GitHub Action entrypoint for **Markdown linting** across the repository.
- Reduce review burden by catching formatting/style issues early in CI, while preserving KFM’s **documentation-as-code** approach.

### Scope
| In Scope | Out of Scope |
|---|---|
| Running a Markdown linter in CI (PRs/pushes) using a shared action. | Defining the full KFM Markdown Protocol (template/front-matter governance). |
| Documenting configuration expectations and how to reproduce lint checks locally. | Semantic validation of Story Nodes (citations, evidence linkage) beyond formatting. |
| Clear inputs/outputs guidance for workflow authors. | Any non-Markdown linting (YAML, JSON, Python, etc.). |

### Audience
- Primary: CI maintainers and repo maintainers authoring workflows under `.github/workflows/`.
- Secondary: Contributors who want to run the same lint checks locally before opening a PR.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: **Markdown lint**, **GFM** (GitHub Flavored Markdown), **CI gate**, **composite action**.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `.github/actions/markdown-lint/README.md` | CI maintainers | Usage + reproduction guidance. |
| Action definition | `.github/actions/markdown-lint/action.yml` | CI maintainers | **Not confirmed in repo** (expected for an action). |
| Repo Markdown rules | `.markdownlint.{yml,yaml,json}` | CI maintainers | **Not confirmed in repo** (config location may vary). |
| Markdown Protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Governance | **Not confirmed in repo** (separate from lint rules). |

### Definition of done (for this document)
- [x] Front-matter complete + structurally valid
- [x] Action purpose + scope documented
- [x] Validation steps listed and repeatable (with placeholders where repo-specific)
- [x] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/markdown-lint/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| GitHub Actions (workflows) | `.github/workflows/` | CI workflows that call this action |
| GitHub Actions (local actions) | `.github/actions/` | Composite / JS / Docker actions vendored in-repo |
| Documentation | `docs/` | Governed docs that must pass doc checks |
| Templates | `docs/templates/` | Governed Markdown templates used across KFM |

### Expected file tree for this sub-area
~~~text
📁 .github/
└── 📁 actions/
    └── 📁 markdown-lint/
        ├── 📄 README.md
        ├── 📄 action.yml                 # not confirmed in repo
        └── 📁 scripts/                   # optional helpers; not confirmed in repo
            └── 📄 run.sh                 # not confirmed in repo
~~~

## 🧭 Context

### Background
KFM treats documentation as a first-class, versioned artifact. CI gates exist to prevent docs from drifting into inconsistent or unreviewable states. Markdown linting is the **fastest** feedback loop to catch mechanical issues (broken list indentation, trailing whitespace, inconsistent heading spacing, etc.) before reviewers spend time on manual cleanup.

### Assumptions
- Workflows calling this action have already checked out the repo (e.g., `actions/checkout`).
- A Markdown linter is used consistently (the exact tool and rule set are repo-defined and **not confirmed in repo** in this document alone).
- The action is intended to be deterministic: same input files + same config → same results.

### Constraints / invariants
- Canonical system ordering remains: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- This action is a **CI validation step only**: it must not mutate data artifacts committed to the repo (unless explicitly used in a local “fix” workflow).
- The frontend/UI never reads Neo4j directly; linting does not change API/graph boundaries.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Which Markdown lint engine is standard here (markdownlint-cli, markdownlint-cli2, remark-lint, etc.)? | CI maintainers | TBD |
| Where is the canonical lint config stored (repo root, `.github/`, `docs/`)? | CI maintainers | TBD |
| Should “autofix” be allowed in CI, or only locally? | Governance + CI maintainers | TBD |

### Future extensions
- Add an explicit “changed files only” optimization (lint only Markdown touched in a PR).
- Add a separate **Markdown Protocol** validator gate (structure/front-matter/template compliance) if not already present.
- Add link-checking as a separate action (avoid coupling lint + link validation).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  PR[Pull Request / Push] --> WF[GitHub Workflow]
  WF --> ML[markdown-lint action]
  ML --> RES{Lint passes?}
  RES -- yes --> OK[CI gate green]
  RES -- no --> FAIL[CI gate red + annotations]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Dev as Contributor
  participant GH as GitHub Actions
  participant ML as markdown-lint action
  Dev->>GH: Push / open PR
  GH->>ML: Run lint step
  ML-->>GH: Exit code + annotations
  GH-->>Dev: Status check (pass/fail)
~~~

## 🔌 Action Interface

> Authoritative inputs/outputs should be defined in `.github/actions/markdown-lint/action.yml` (**not confirmed in repo**).  
> This README documents **intended** usage patterns and safe defaults.

### Recommended usage (in a workflow)
~~~yaml
jobs:
  markdown_lint:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Markdown lint
        uses: ./.github/actions/markdown-lint
        # with:
        #   config_path: ".markdownlint.yml"     # not confirmed in repo
        #   targets: "**/*.md"                  # not confirmed in repo
~~~

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| (see `action.yml`) | TBD | Workflow `with:` block | Must be schema-valid per GitHub Actions |
| `config_path` (recommended) | string path | repo root or `.github/` | fail if file missing (policy TBD) |
| `targets` (recommended) | glob(s) | workflow | must expand to files; empty-set behavior TBD |
| `fail_on_warning` (recommended) | boolean | workflow | default true recommended |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| (none required) | — | — | GitHub Actions status is the contract |
| `summary` (optional) | string | step output | not confirmed in repo |

### Sensitivity & redaction
- This action must not print secrets (tokens, keys) to logs.
- Avoid echoing environment variables unless explicitly safe.
- If lint tooling generates file snippets, ensure it does not expose redacted/sensitive content.

### Quality signals
- Lint results are deterministic across runs.
- Errors are actionable (clear rule + file + line/column).
- CI runtime remains low (ideally seconds to a few minutes).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Not applicable: Markdown lint does not generate or modify STAC artifacts.

### DCAT
- Not applicable: Markdown lint does not generate or modify DCAT artifacts.

### PROV-O
- Not applicable: Markdown lint does not generate provenance bundles.
- Optional future enhancement: emit a lightweight CI “activity log” (not a PROV bundle) for observability.

### Versioning
- This README follows semver in `version:` front-matter.
- The action implementation should be versioned via git history; if externally reused, consider tagging releases.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Workflow | Triggers lint checks | `.github/workflows/*.yml` |
| markdown-lint action | Runs repo-standard Markdown lint | `uses: ./.github/actions/markdown-lint` |
| Lint config | Encodes repo style rules | `.markdownlint.*` (not confirmed in repo) |
| Contributors | Fix issues locally | local tooling + PR |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Action interface | `.github/actions/markdown-lint/action.yml` | Any breaking change requires coordinated workflow updates |
| Lint ruleset | `.markdownlint.*` | Changes should be reviewed; prefer additive changes |

### Extension points checklist (for future work)
- [ ] Add “only changed Markdown files” mode
- [ ] Add GitHub annotation formatting (file/line)
- [ ] Add pre-commit integration guidance (local dev)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Indirect: keeping Markdown well-formed reduces rendering issues in Story Node viewers.
- Does not validate evidence linkage; that belongs to Story Node rules and protocol checks.

### Provenance-linked narrative rule
- Not enforced here. This action only checks Markdown formatting.

### Optional structured controls
~~~yaml
# Not applicable for this action.
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown lint checks (this action)
- [ ] Markdown protocol checks (template/front-matter compliance) — not confirmed here
- [ ] Link checks — not confirmed here

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands.
#
# Option A (not confirmed): markdownlint-cli2
#   npx markdownlint-cli2 "**/*.md" "#node_modules"
#
# Option B (not confirmed): markdownlint-cli
#   npx markdownlint "**/*.md"
#
# Option C (not confirmed): run via a repo script
#   ./tools/lint/markdown.sh
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| lint_error_count | CI run logs | `mcp/runs/` or CI artifacts (not confirmed in repo) |

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes to lint rules should be reviewed by maintainers, since they affect contributor experience and CI pass/fail rates.
- Any changes that risk leaking sensitive content in CI logs require human review.

### CARE / sovereignty considerations
- This action does not process community-sensitive datasets directly.
- Still: documentation can contain sensitive context; avoid printing large file excerpts into public CI logs.

### AI usage constraints
- This document permits summarization/structure extraction per front-matter.
- Do not use AI tooling to infer sensitive locations or generate policy from this action’s outputs.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for markdown-lint action | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
