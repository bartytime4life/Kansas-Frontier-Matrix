---
title: "GitHub App Permissions — <app_slug>"
path: ".github/apps/<app_slug>/permissions.md"
version: "v1.0.0"
last_updated: "2025-12-29"
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

doc_uuid: "urn:kfm:doc:github:app:<app_slug>:permissions:v1.0.0"
semantic_document_id: "kfm-github-app-<app_slug>-permissions-v1.0.0"
event_source_id: "ledger:kfm:doc:github:app:<app_slug>:permissions:v1.0.0"
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

# GitHub App Permissions — <app_slug>

## 📘 Overview

### Purpose
This document defines and justifies the **least-privilege** GitHub App permission set for `<app_slug>` as used by the Kansas Frontier Matrix (KFM) repository. It is intended to:
- map every requested permission to a concrete CI / policy-gate need, and
- prevent automation from bypassing KFM’s governance and provenance requirements.

This file is the **permissions contract**: changing GitHub App permissions requires updating this document and passing review gates.

### Scope
| In Scope | Out of Scope |
|---|---|
| GitHub App permission settings (repo/org) and their justifications | Authoring/modifying CI workflow logic under `.github/workflows/**` |
| Repository selection rules (all vs selected repositories) | Branch protections, CODEOWNERS, and repo administration policy *(tracked elsewhere)* |
| Token-handling expectations (installation tokens, key storage) | Storing/rotating secrets (implementation details) |
| Webhook event subscriptions *(only if the app is event-driven)* | Any non-GitHub credentials (cloud, DB, third-party APIs) |
| Prohibited permissions + prohibited behaviors | “How to install the app” user guide |

### Audience
- Primary: repo administrators, security reviewers, and CI/policy-gate maintainers.
- Secondary: contributors who need to understand why automation can/can’t take certain actions.

### Definitions (link to glossary)
- Link: `docs/glossary.md` *(not confirmed in repo; recommended)*
- **GitHub App**: an installed application that receives an installation token with explicitly granted permissions.
- **Installation token**: short-lived token minted for a specific installation + repository set.
- **Policy gate**: CI checks that enforce KFM standards (schema validity, sovereignty scanning, etc.).
- **Check Run**: GitHub “Checks” API object used to report structured CI results to commits/PRs.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (pipeline + CI expectations) | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical ordering + minimum CI gates |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Structure used by this document |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Story | Story Node validation inputs |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | Contract tests + API evolution |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs | *not confirmed in repo* |
| CI workflows | `.github/workflows/` | CI maintainers | Policy gates + validations |
| This permissions contract | `.github/apps/<app_slug>/permissions.md` | Security/CI | Must match GitHub App settings |
| JSON schemas | `schemas/` | TBD | STAC/DCAT/PROV/story/ui/telemetry schema validation inputs |
| Catalog outputs | `data/stac/` `data/catalog/dcat/` `data/prov/` | Data stewards | Must validate in CI before publish |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Permissions table is complete (every granted permission is listed and justified)
- [ ] Prohibited permissions are explicitly listed
- [ ] GitHub App settings (in GitHub UI) match this document exactly
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `.github/apps/<app_slug>/permissions.md` *(must match front-matter)*

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| CI | `.github/` | Workflows + policy gates |
| Documentation | `docs/` | Canonical governed docs (guides, designs, domain notes) |
| Schemas | `schemas/` | JSON schemas (STAC/DCAT/PROV/story/ui/telemetry) |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Graph | `src/graph/` | Ontology bindings + graph build/migrations |
| API boundary | `src/server/` | REST/GraphQL contracts + redaction enforcement |
| Frontend | `web/` | React + map clients + Focus Mode UI |
| MCP | `mcp/` | Experiments, runs, model cards, SOPs |
| Tests | `tests/` | Unit + integration tests |
| Tools | `tools/` | Validators, utilities, QA scripts |

### Expected file tree for this sub-area
~~~text
📁 .github/
├── 📁 apps/
│   └── 📁 <app_slug>/
│       └── 📄 permissions.md
└── 📁 workflows/
    └── 📄 <workflow_files>.yml
~~~

## 🧭 Context

### Background
KFM’s repository process is contract-first and governance-driven. CI is expected to enforce, at minimum:
- Markdown protocol validation (front-matter + required sections)
- Link/reference checks (no orphan pointers)
- JSON schema validation for STAC/DCAT/PROV (and story/ui/telemetry schemas if present)
- Graph integrity tests (constraints, expected labels/edges)
- API contract tests (OpenAPI/GraphQL schema + resolver tests)
- Security + sovereignty scanning gates (as applicable), including secret scanning, PII scanning, sensitive-location leakage checks, and classification propagation checks

Automation credentials must therefore be:
- **least-privilege**, and
- **unable to bypass human review** for protected operations (publishing, classification changes, sensitive data exposure).

### Assumptions
- `<app_slug>` is primarily used by CI/policy gates to authenticate GitHub API calls with explicit, auditable permissions.
- The app should not merge PRs, push directly to default branches, or change repo administration settings.
- If the app needs to write anything, it should be limited to “feedback channels” (checks, statuses, comments) and never to “state-changing channels” (repo contents, releases) without explicit review.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode ordering is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- **Least privilege is mandatory:** request the minimum permissions needed for the *current* feature set.
- **No sensitive-location inference or leakage:** bot outputs (check summaries/comments) must not reveal sensitive locations or restricted details.
- **No secret leakage:** never echo tokens, keys, or raw scan findings that contain secrets/PII into PR comments or public logs.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Does `<app_slug>` need to write PR comments, or are check-run summaries sufficient? | TBD | TBD |
| Does `<app_slug>` create custom Check Runs (Checks API), or rely solely on GitHub Actions job checks? | TBD | TBD |
| Is cross-repo access needed (multiple repositories), or single-repo installation is sufficient? | TBD | TBD |
| Is workflow dispatch required (Workflows: write), or prohibited? | TBD | TBD |

### Future extensions
- Extension point A: Split “read-only validator” and “publisher” responsibilities into separate apps if publish automation is ever required.
- Extension point B: Add a dedicated “sensitive output redaction” step for any bot-authored summaries that may surface in public PR threads.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  PR[Pull Request] --> WF[GitHub Actions workflow<br/>.github/workflows/**]
  WF --> TOK[Mint installation token<br/>(GitHub App <app_slug>)]
  TOK --> GHAPI[GitHub API]
  WF --> VAL[Run validators<br/>markdown, schemas, scans, tests]
  VAL --> RES[Validation results]
  RES --> GHAPI
  GHAPI --> CHECKS[Checks / Statuses]
  GHAPI --> COMMENTS[PR comments (optional)]
  CHECKS --> PR
  COMMENTS --> PR
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant WF as Workflow (Actions)
  participant APP as GitHub App (<app_slug>)
  participant API as GitHub API
  participant PR as Pull Request / Commit

  WF->>APP: Request installation token
  APP-->>WF: Installation token (scoped)
  WF->>API: Create check run / comment (scoped token)
  API-->>PR: Check run / comment visible to reviewers
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Repository contents (schemas, docs, code) | Git repo | Checkout + GitHub API (if used) | CI validators + tests |
| PR metadata (title, labels, changed files) | GitHub API payload | Pull request event context | N/A (trusted platform data) |
| Catalog artifacts (STAC/DCAT/PROV) | JSON | `data/stac/` `data/catalog/dcat/` `data/prov/` | JSON schema validation in CI |
| Governance docs / templates | Markdown | `docs/` `docs/templates/` | Markdown protocol validation |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Check runs (recommended) | GitHub Checks API | GitHub (not in repo) | This permissions contract + GitHub API |
| Commit statuses (optional) | GitHub Status API | GitHub (not in repo) | This permissions contract + GitHub API |
| PR comments (optional) | GitHub Issues/PR API | GitHub (not in repo) | This permissions contract + redaction rules |
| Labels / triage signals (optional) | GitHub Issues API | GitHub (not in repo) | Governance-approved label taxonomy *(not confirmed in repo)* |

### Sensitivity & redaction
- Treat PR comments and check summaries as **public by default**.
- Do not include:
  - secrets/credentials (including partials),
  - raw PII,
  - restricted/sensitive location details,
  - unreviewed “policy” statements (keep outputs descriptive and evidence-linked).

### Quality signals
- Permission-denied rate (indicates missing permission or over-scoped workflow)
- Rate-limiting incidents (may require caching or reduced API calls)
- Deterministic outputs (same inputs → same validation results)

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: `data/stac/collections/**` *(if present)*
- Items involved: `data/stac/items/**` *(if present)*
- Extension(s): `KFM-STAC v11.0.0` (profile)

### DCAT
- Dataset identifiers: `data/catalog/dcat/**` *(if present)*
- License mapping: must remain consistent with catalog metadata
- Contact / publisher mapping: as specified in DCAT outputs

### PROV-O
- `prov:wasDerivedFrom`: link validation findings back to source artifacts (file paths + IDs where available)
- `prov:wasGeneratedBy`: workflow run ID and/or KFM pipeline run ID *(if emitted)*
- Activity / Agent identities: identify automation as an agent (GitHub App) in PROV where applicable *(optional; not confirmed in repo)*

### Versioning
- This document uses semver; any permission expansion requires at least a patch/minor bump and review.
- If the app ever writes catalog artifacts, versioning rules must follow STAC/DCAT/PROV governance (do not “rewrite history”).

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| GitHub App `<app_slug>` | Scoped auth for automation | Installation token + configured permissions |
| GitHub Actions workflows | Execute CI gates + validators | `.github/workflows/**` |
| Validators / scanners | Enforce KFM contracts + safety | `tools/` + `tests/` + schema validators *(paths vary)* |
| GitHub API | Checks, statuses, comments | GitHub REST API / GraphQL API |
| KFM artifacts | Docs, schemas, catalogs, code | Repo filesystem layout per Master Guide |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| **GitHub App permissions contract** | `.github/apps/<app_slug>/permissions.md` | Semver; changes require review |
| Markdown protocol + governed templates | `docs/templates/**` | Template versioning |
| JSON schemas | `schemas/` | Semver + changelog; breaking changes require bump |
| CI workflows (implementation) | `.github/workflows/**` | Review required; treat as “security-sensitive code” |

### GitHub App permission matrix (least privilege)
> Mark each permission as **Required**, **Optional**, or **Prohibited** for `<app_slug>`. If a permission is granted in GitHub, it must be **Required** or **Optional** here with a concrete justification.

| Scope | Permission | Access | Required? | Why it exists (KFM mapping) | Risk controls / notes |
|---|---|---:|---|---|---|
| Repository | Metadata | Read | Required | Baseline repo identification for API calls | Low risk; keep read-only |
| Repository | Contents | Read | Required | Read files for validation/reporting when using GitHub API (if applicable) | Do not grant write by default |
| Repository | Pull requests | Read | Optional | Read PR context (files, author, state) for richer validation feedback | Prefer using workflow context where possible |
| Repository | Issues | Write | Optional | Post PR/issue comments, labels, or triage signals | Comments must be redacted and non-sensitive |
| Repository | Pull requests | Write | Optional | Create PR review comments (inline) if needed | Avoid unless truly required |
| Repository | Checks | Write | Optional (recommended) | Create custom Check Runs for KFM validators beyond default workflow checks | Preferred over noisy PR comments |
| Repository | Commit statuses | Write | Optional | Set commit statuses for external gates | Prefer Checks API if possible |
| Repository | Actions | Read | Optional | Read workflow metadata/log pointers for linking in check summaries | Avoid reading logs that may contain secrets |
| Repository | Workflows | Write | Prohibited (default) | Dispatching workflows programmatically | Allow only with explicit governance approval |
| Repository | Contents | Write | Prohibited (default) | Pushing commits / modifying repo files | If ever needed, split into separate “publisher” app |
| Repository | Administration | Read/Write | Prohibited | Repo settings are governance-controlled | Never grant |
| Organization | Members / Administration / Webhooks | Any | Prohibited | Org-wide access not needed for repo CI | Install app at repo scope only |

### Repository selection rules (installation scope)
- Default: **Selected repositories only**, ideally *only* the KFM repository that owns this document.
- If multi-repo access is required, list approved repos here (with justification and review record):
  - `TBD`

### Webhook event subscriptions (only if needed)
| Event | Needed? | Why | Notes |
|---|---|---|---|
| `pull_request` | Optional | Trigger non-Actions automation (if any) | Prefer Actions triggers when possible |
| `check_run` / `check_suite` | Optional | React to check completion | Only if app performs orchestration |
| `issues` | Optional | Label/triage automation | Ensure label taxonomy is governance-approved |

### Prohibited behaviors (hard rules)
- No direct pushes to protected branches (e.g., `main`/`master`) via the app.
- No automatic merges.
- No release publishing or asset uploads.
- No changes to repository settings, permissions, branch protections, or secrets.
- No posting of raw scan outputs that could reveal secrets/PII/sensitive locations.

### Extension points checklist (for future work)
- [ ] If new write operations are introduced (e.g., opening PRs), split into a separate app and re-run governance review.
- [ ] If cross-repo operations are introduced, document approved repo list + constraints.
- [ ] If outputs could contain sensitive locations, add enforced redaction/generalization before publishing bot feedback.
- [ ] If release automation is introduced, align with supply-chain controls (SBOM/SLSA attestations) and restrict permissions accordingly.

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- This GitHub App does **not** directly surface in Focus Mode.
- Indirectly, it supports Focus Mode integrity by ensuring Story Nodes and other governed docs meet template/provenance requirements during CI.

### Provenance-linked narrative rule
- Any bot-authored summaries (check outputs, comments) must be:
  - descriptive of validation results,
  - linked to specific file paths / schema IDs / run logs, and
  - free of uncited historical interpretation.

### Optional structured controls
~~~yaml
focus_layers:
  - "ci-policy-gates"   # not a map layer; used here as a trace label (optional)
focus_time: "N/A"
focus_center: [ -98.0000, 38.0000 ]   # canonical KS center (for consistency; not used by this doc)
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front-matter + required sections)
- [ ] Verify GitHub App settings match the “permission matrix” above (manual + screenshot evidence recommended)
- [ ] Run a PR “smoke test” workflow using the app token:
  - check run creation (if enabled)
  - optional PR comment creation (if enabled)
- [ ] Confirm prohibited operations fail (e.g., attempts to write repo contents)
- [ ] Security and sovereignty checks (as applicable): secret scan, PII scan, sensitive-location leakage checks

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) open a PR with a known schema/docs change and run CI
# 2) confirm checks/comments appear and contain no sensitive data
# 3) confirm the workflow does NOT have permissions to push commits
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| permission_denied | GitHub API responses | `schemas/telemetry/` + `docs/telemetry/` *(if present)* |
| rate_limited | GitHub API responses | `schemas/telemetry/` + `docs/telemetry/` *(if present)* |
| check_run_created | CI workflow | Workflow logs + telemetry *(if emitted)* |
| comment_posted | CI workflow | Workflow logs + telemetry *(if emitted)* |
| promotion_blocked | CI policy gates | Workflow logs + telemetry *(if emitted)* |

## ⚖ FAIR+CARE & Governance

### Review gates
- Any change to this document or the GitHub App permission settings requires:
  - repository administrator review, and
  - security/governance review if new write permissions are requested.
- Adding any permission that could change published outputs (repo contents, workflows, releases) is a **high-risk change** and should trigger council/board sign-off per governance policy *(see `docs/governance/REVIEW_GATES.md` if present; not confirmed in repo)*.

### CARE / sovereignty considerations
- Bot outputs must not reveal sensitive locations or restricted community information.
- Where validation results touch governance-sensitive datasets, feedback should be generalized (e.g., “redaction required”) rather than printing exact restricted values.

### AI usage constraints
- Ensure doc’s AI permissions/prohibitions match intended use:
  - AI may summarize or structure-extract.
  - AI must not generate new policy or infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-29 | Initial GitHub App permissions contract for `<app_slug>` | TBD |

---
Footer refs:
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Universal doc template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
