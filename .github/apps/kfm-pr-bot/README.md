---
title: "kfm-pr-bot — GitHub App (PR Governance Assistant)"
path: ".github/apps/kfm-pr-bot/README.md"
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

doc_uuid: "urn:kfm:doc:github:apps:kfm-pr-bot:readme:v1.0.0"
semantic_document_id: "kfm-github-app-kfm-pr-bot-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:apps:kfm-pr-bot:readme:v1.0.0"
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

# kfm-pr-bot — GitHub App (PR Governance Assistant)

## 📘 Overview

### Purpose
`kfm-pr-bot` is a GitHub App intended to assist pull request reviews by:
- Surfacing **governance / documentation** expectations early,
- Pointing contributors to the correct KFM templates and required artifacts,
- Reducing reviewer load while preserving required **human approvals**.

### Scope

| In Scope | Out of Scope |
|---|---|
| PR guidance via comments and/or check runs | Automatically merging PRs |
| Path-based reminders (docs, schemas, data, API contracts) | Approving PRs on behalf of humans |
| Least-privilege permissions + security notes | Posting secrets, dataset contents, or sensitive locations |
| Routing to correct governed templates | Generating “policy” beyond repo-governed docs |

### Audience
- Primary: Maintainers + reviewers
- Secondary: Contributors who need to satisfy repo governance and CI expectations

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used: PR, check run, required review, provenance, contract test, redaction

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This doc | `.github/apps/kfm-pr-bot/README.md` | Maintainers | Repo-facing behavior |
| Templates | `docs/templates/` | Maintainers | Used for guidance links |
| Master guide | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline + invariants |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Documented: events, permissions, security posture, runbook
- [ ] Any write capabilities are justified and least-privilege
- [ ] “Fork PR” safety behavior documented
- [ ] Explicitly states what the bot will **not** do

## 🗂️ Directory Layout

### This document
- `path`: `.github/apps/kfm-pr-bot/README.md`

### Expected file tree for this sub-area
~~~text
📁 .github/
├── 📁 apps/
│   ├── 📄 README.md
│   └── 📁 kfm-pr-bot/
│       └── 📄 README.md
~~~

## 🧭 Context

### Background
KFM relies on governed documentation and an ordered data → catalog → graph → API → UI pipeline. A PR bot can help keep PRs aligned with that structure by flagging missing artifacts early (before reviewer time is spent).

### Constraints / invariants (must not be violated)
- Canonical ordering preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend never reads Neo4j directly; UI consumes API contracts.
- No unsourced narrative introduced into Focus Mode contexts.

### Safety posture (high-level)
- Prefer **read-only** analysis of changed files.
- If the bot writes (comments/check runs), it should never echo sensitive data and must avoid running untrusted code.
- Any permission expansion requires security review.

## 🗺️ Diagrams

### Bot positioning in PR workflow
~~~mermaid
flowchart LR
  PR[Pull Request] --> Bot[kfm-pr-bot]
  PR --> CI[GitHub Actions CI]
  Bot --> Out1[Guidance Comment / Checklist]
  Bot --> Out2[Check Run Status]
  CI --> Out2
  Out1 --> Review[Human Review]
  Out2 --> Review
~~~

### Optional: sequence diagram (conceptual)
~~~mermaid
sequenceDiagram
  participant Dev as Contributor
  participant GH as GitHub
  participant Bot as kfm-pr-bot
  participant Maint as Maintainer

  Dev->>GH: Open PR / push commits
  GH->>Bot: webhook event (PR updated)
  Bot-->>GH: check run + guidance comment
  Maint->>GH: review, request changes, approve
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| PR event payload | JSON | GitHub webhooks | Signature verification |
| PR file diff | Git tree | GitHub API | Path allowlist rules |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Guidance checklist | PR comment | PR timeline | Deterministic wording + links |
| Check run | GitHub Checks API | PR status | Clear “pass/fail” criteria |

### Sensitivity & redaction
- Do not quote large chunks of sensitive documents or raw dataset values in PR comments.
- Prefer referencing file paths, dataset IDs, schema IDs, and required templates.

## 🌐 STAC, DCAT & PROV Alignment
When PRs touch data/catalog areas, the bot may remind contributors to include:
- STAC Collection + Item(s)
- DCAT dataset mapping
- PROV activity record for transformations

(Implementation may be delegated to CI checks; the bot’s role is to help reviewers and contributors spot omissions early.)

## 🧱 Architecture

### Responsibilities (intended)
- Detect broad change categories by path patterns, e.g.:
  - `data/` changes → remind about catalogs/provenance expectations
  - `schemas/` changes → remind about validators + contract tests
  - `src/server/` / API changes → remind about API contract extension docs
  - `web/` UI changes → remind about API-only access and provenance rendering expectations
  - `docs/` narrative changes → remind about provenance / citations

### Non-goals (explicit)
- The bot does not merge PRs.
- The bot does not approve PRs.
- The bot does not generate new governance policy beyond governed docs.
- The bot does not expose secrets or privileged information.

## 🔌 Interfaces & Contracts

### GitHub API usage
- Webhooks: PR opened/synchronized/reopened, issue comments (optional)
- Outputs: check runs, PR comments

### Contract alignment
- Links to canonical docs and templates (Master Guide and templates) should be included in bot feedback.
- The bot should never instruct contributors to violate the “API boundary” or pipeline ordering.

## 🔐 Permissions & Events

### Recommended minimal permission set (documented for least privilege)
> Final permissions depend on how the app is implemented, but the default should be “minimum required”.

| Capability | GitHub permission area | Level (recommended) | Why |
|---|---|---|---|
| Read repository contents | Contents | Read | Inspect changed files |
| Comment on PRs | Pull requests / Issues | Write | Post checklist guidance |
| Create check runs | Checks | Write | Provide pass/fail signal |
| Read workflow results (optional) | Actions | Read | Summarize CI status (no secrets) |

### Event triggers (conceptual)
- `pull_request` (opened, synchronize, reopened)
- `pull_request_review` (optional, for follow-up guidance)
- `check_suite` (optional, if summarizing CI outcomes)

## 🧪 Validation & CI/CD

### Validation checklist
- [ ] Bot feedback is deterministic for identical inputs
- [ ] No secret material in logs or PR comments
- [ ] Fork PR handling is safe (no privileged execution of untrusted code)
- [ ] Bot does not bypass required human approvals
- [ ] Clear mapping from advice → canonical KFM docs/templates

## ⚖ FAIR+CARE & Governance

### Governance approvals required (if any)
- Security council review: **required** for installation and any permission expansion
- Maintainer review: **required** for changes to bot behavior and docs
- Historian/editor review: **recommended** if bot affects narrative validation guidance

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README for kfm-pr-bot governance documentation | TBD |