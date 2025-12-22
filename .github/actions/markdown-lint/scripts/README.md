---
title: "GitHub Action — Markdown Lint Scripts"
path: ".github/actions/markdown-lint/scripts/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "active"
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

doc_uuid: "urn:kfm:doc:github-actions:markdown-lint:scripts-readme:v1.0.0"
semantic_document_id: "kfm-github-actions-markdown-lint-scripts-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:markdown-lint:scripts-readme:v1.0.0"
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

# GitHub Action — Markdown Lint Scripts

## 📘 Overview

### Purpose

This folder documents the helper scripts used by the repository’s **Markdown linting** GitHub Action. The goal is to support CI checks such as **Markdown protocol validation** (KFM‑MDP) and any style/link rules configured for Markdown in this repo.

### Scope

| In Scope | Out of Scope |
|---|---|
| Scripts executed by the `.github/actions/markdown-lint/` action to validate Markdown | Writing/editing rules for the full KFM documentation set (see `docs/MASTER_GUIDE_v12.md`) |
| How these scripts should behave (inputs/outputs/exit codes) | Data pipeline processing (ETL/catalog/graph build) |
| Where to look when CI fails on Markdown checks | Changing governance policy (handled in `docs/governance/…`) |

### Audience

- Primary: repo maintainers, CI maintainers, contributors touching Markdown files
- Secondary: external contributors troubleshooting PR checks

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **KFM‑MDP**: KFM Markdown Protocol (version referenced in governed templates)
  - **CI gate**: a required check that must pass before merge
  - **Action**: `.github/actions/markdown-lint/` (custom action wrapper)
  - **Scripts**: the executable helpers in this folder

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `.github/actions/markdown-lint/scripts/README.md` | Repo maintainers | You are here |
| Action definition | `.github/actions/markdown-lint/` | Repo maintainers | Entry point not confirmed in this document |
| Workflows invoking the action | `.github/workflows/` | Repo maintainers | Search for `markdown-lint` usage |
| Governed Markdown templates | `docs/templates/` | Docs governance | Source of required front-matter keys + structure |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] This README explains what belongs in `scripts/` and how scripts are expected to behave
- [ ] A contributor can determine where the action is invoked and how to troubleshoot a failure
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `.github/actions/markdown-lint/scripts/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub Actions | `.github/actions/` | Local action definitions (composite/Docker) |
| Workflows | `.github/workflows/` | CI entry points that call actions |
| Docs templates | `docs/templates/` | Governed Markdown templates (required front matter + structure) |
| Canonical guide | `docs/MASTER_GUIDE_v12.md` | Pipeline ordering + invariants |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 markdown-lint/
        └── 📁 scripts/
            ├── 📄 README.md
            └── 📄 <script files live here>
~~~

## 🧭 Context

### Background

KFM documentation is governed and versioned, and CI is expected to enforce Markdown conformance (including “Markdown protocol validation”) so that Story Nodes and other Markdown artifacts remain machine-validated and consistent.

### Assumptions

- This directory is called by a GitHub Action step (CI context).
- Scripts are expected to run non-interactively and deterministically.
- Scripts should not mutate repository files during CI runs.

### Constraints / invariants

- The canonical pipeline ordering is preserved:
  - ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode
- API boundary is preserved:
  - UI does **not** read Neo4j directly; contracts live at the API layer.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which markdown linter/validator(s) are used (e.g., markdownlint, custom KFM-MDP validator, link checker)? | TBD | TBD |
| Where do configuration files live (e.g., `.markdownlint.*`, ignore patterns, protocol rules)? | TBD | TBD |
| Does the action emit SARIF / annotations / PR comments, or only logs? | TBD | TBD |

### Future extensions

- Add a “changed files only” mode for faster PR runs (while keeping a full scan option for main/nightly).
- Add explicit link-check and image/path integrity checks (if not already present).
- Add a standard “How to fix” mapping from rule IDs to remediation steps.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[Markdown files in repo] --> B[GitHub Workflow]
  B --> C[Local Action: markdown-lint]
  C --> D[Scripts in scripts/]
  D --> E[Lint / protocol results]
  E --> F[Pass or fail CI gate]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant Dev as Contributor (PR)
  participant GH as GitHub Actions
  participant Act as markdown-lint action
  participant Scr as scripts/*
  Dev->>GH: Push / open PR
  GH->>Act: Run workflow job step
  Act->>Scr: Execute scripts (lint + protocol checks)
  Scr-->>Act: Exit code + logs/results
  Act-->>GH: Job status
  GH-->>Dev: Check results in PR
~~~

## 📦 Data & Metadata

### What the scripts operate on

- Inputs: tracked Markdown files in the working tree (typically `*.md`, plus governed docs generated during CI if applicable).
- Outputs: console logs and CI job status (and optionally reports/artifacts, if configured in the workflow).

### Non-mutation rule (recommended)

- Scripts should treat the repo as **read-only** in CI runs (no auto-fixing unless explicitly enabled in a separate “format” workflow).

## 🌐 STAC, DCAT & PROV Alignment

This action does not generate STAC/DCAT/PROV artifacts. It exists to ensure Markdown artifacts that describe or reference those standards remain structurally valid and consistent with governed templates.

## 🧱 Architecture

### Script interface expectations (recommended)

- **Inputs**
  - Prefer explicit CLI args and/or well-scoped environment variables.
  - Honor `GITHUB_WORKSPACE` when running in Actions.
- **Outputs**
  - Human-readable log output to stdout/stderr.
  - Exit code `0` for success; non-zero for failure.
- **Determinism**
  - Avoid network calls.
  - Avoid “current time” content unless explicitly part of the check.

### Security + hygiene (required)

- Do not print secrets or tokens.
- Do not echo environment variables that may contain credentials.
- Do not upload file contents to third-party services.

## 🧠 Story Node & Focus Mode Integration

Story Nodes are Markdown artifacts that must remain consistent and machine-ingestible for narrative UX. Keeping Markdown documents structurally valid supports downstream Story/Focus tooling and preserves the governed pipeline’s integrity.

## 🧪 Validation & CI/CD

### Where this runs

- CI: invoked by workflows under `.github/workflows/` that reference the local action.
- Local debugging (suggested):
  - Locate the invoking workflow(s):
    - `git grep -n "markdown-lint" .github/workflows`
    - `git grep -n ".github/actions/markdown-lint" .github/workflows`
  - Run the script(s) directly if they are standalone executables (depends on script implementation).

### Troubleshooting checklist

- Confirm the failing file’s front-matter is present and valid.
- Confirm `path:` matches the actual file path (if required by the protocol validator).
- Check for broken relative links and missing referenced files.

## ⚖ FAIR+CARE & Governance

### Review gates

- Any changes to lint/protocol enforcement behavior should be reviewed by:
  - Docs governance / maintainers
  - CI maintainers

### CARE / sovereignty considerations

- Linting must not encourage exposing sensitive locations or restricted content in Markdown.
- If a check touches culturally sensitive topics, treat rule changes as **requires human review**.

### AI usage constraints

- This document’s AI permissions/prohibitions are defined in front-matter.
- Do not add automation that “generates policy” or infers sensitive locations from content.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for markdown-lint action scripts | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

