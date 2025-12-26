---
title: "KFM — GitHub App Workflow Mapping — <app_slug>"
path: ".github/apps/<app_slug>/workflows.md"
version: "v1.0.0"
last_updated: "2025-12-26"
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

doc_uuid: "urn:kfm:doc:github:apps:<app_slug>:workflows:v1.0.0"
semantic_document_id: "kfm-github-app-<app_slug>-workflows-v1.0.0"
event_source_id: "ledger:kfm:doc:github:apps:<app_slug>:workflows:v1.0.0"
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

# GitHub App Workflow Mapping — `<app_slug>`

> Replace `<app_slug>` everywhere in this document with the folder slug for this GitHub App integration.
> This document is **public** and must remain **secret-free**.

## 📘 Overview

### Purpose
- Map **exactly which GitHub Actions workflows + jobs** depend on this GitHub App.
- Make least-privilege review concrete by linking each workflow usage to `./permissions.md`.
- Provide an audit-friendly checklist for changes: if the app’s usage changes in CI, update this file in the same PR.

### Scope

| In Scope | Out of Scope |
|---|---|
| Mapping workflows → jobs that use the app (file, job id, trigger, why needed) | Full workflow definitions (they live in `.github/workflows/*.yml`) |
| Secret *names* referenced (never values) | Private keys, webhook secrets, installation tokens, PATs |
| Repo write surfaces / artifacts created by app-authenticated jobs | Editing org/repo settings directly from this repo (document only) |

### Audience
- Primary: repo maintainers, CI/CD owners, security reviewers
- Secondary: contributors who need to understand why an app token is used

### App identity (non-secret metadata)

| Field | Value |
|---|---|
| `app_slug` | `<app_slug>` |
| Display name | `<TBD>` |
| App ID | `<TBD>` |
| Installation scope | `<org or repo>` |
| Installed in | `<org>/<repo> (TBD)` |
| Owner | `<TBD>` |
| Rotation expectations | `<TBD>` (optional: link `./rotation.md` if present) |

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| GitHub Apps overview | `.github/apps/README.md` | Repo maintainers | Defines governance + invariants |
| Permission justification | `./permissions.md` | App owner | Must justify all requested permissions |
| App manifest | `./manifest.json` | App owner | Optional; must be secret-free |
| Workflow mapping (this doc) | `./workflows.md` | App owner + CI owners | Must stay in sync with actual workflows |
| CI workflow inventory | `.github/workflows/` | CI owners | Source of truth for pipeline execution |
| CI governance notes | `.github/workflows/README.md` | CI owners | CI “contract enforcement” expectations |
| Security standards | `.github/SECURITY.md` + `docs/security/` | Security reviewers | Credential handling & incident process |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] All workflows/jobs using the app are listed below (no “implicit” usage)
- [ ] Each listed workflow usage links to the exact permission block(s) in `./permissions.md`
- [ ] No secrets committed (private keys/webhook secrets/tokens); secret names only
- [ ] Workflows referencing the app are updated and still pass (when workflows are changed)
- [ ] Version history entry added for each meaningful change

## 🗂️ Directory Layout

### This document
- `path`: `.github/apps/<app_slug>/workflows.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| App docs & artifacts | `.github/apps/<app_slug>/` | This app’s docs, manifest, and assets |
| Workflows | `.github/workflows/` | CI pipelines that may use app-based auth |
| Local composite actions | `.github/actions/` | Reusable actions (if present) |
| Pipelines | `src/pipelines/` | ETL + catalog + transforms (may be triggered by CI) |
| API server | `src/server/` | Contracted access layer (REST/GraphQL) |
| UI | `web/` | React/MapLibre app (no direct graph calls) |

### Expected local file tree

~~~text
📁 .github/
└── 📁 apps/
    └── 📁 <app_slug>/
        ├── 📄 permissions.md
        ├── 📄 manifest.json
        ├── 📄 workflows.md
        └── 📁 assets/
            └── 📄 <optional_files>
~~~

## 🧭 Context

### Background
- GitHub Apps are preferred over long-lived personal tokens when automation needs to interact with GitHub (least privilege + auditable installations).
- This mapping exists to make “who can do what in CI” reviewable and reproducible.

### Assumptions
- This repository may be public; anything committed here should be safe to disclose.
- Secrets are managed via GitHub Environments/Secrets or an external secret manager (not stored in git).

### Constraints / invariants
- Preserve the canonical ordering: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend consumes contracts via APIs (**no direct graph dependency**).
- Never commit private keys, webhook secrets, tokens, or any credential material to `.github/apps/**`.

### Change-management rule (workflow ↔ app coupling)
Treat any of the following as a **contract change** requiring human review and a version-history entry:
- New workflow/job begins using this app
- A workflow/job stops using this app
- Permission scope increases (or a new permission is requested)
- A job’s repo-write surface expands (e.g., begins writing to `data/`, `docs/reports/`, or publishing story artifacts)

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  PR[Pull Request] --> WF[GitHub Actions Workflow]
  WF --> V[Validation Jobs]
  WF --> APP[GitHub App Auth: <app_slug>]
  APP --> GH[GitHub API]
  V --> ART[Artifacts: logs/reports]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Dev as Contributor
  participant GH as GitHub
  participant WF as Actions Workflow
  participant App as GitHub App (<app_slug>)
  participant API as KFM API

  Dev->>GH: Open PR / push
  GH->>WF: Trigger workflow
  WF->>App: Request installation token (via stored credentials)
  App-->>WF: Short-lived token
  WF->>GH: Comment/status/update checks
  WF->>API: (Optional) call KFM API for contract tests (never direct Neo4j)
~~~

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Typically indirect: CI automation may generate or validate Story Node artifacts, data catalogs, or provenance bundles that later surface in the UI.

### Provenance-linked narrative rule
- Any automation that generates narrative content must preserve provenance and avoid unsourced narrative claims (link story artifacts to dataset/document IDs and/or PROV run IDs).

### Optional structured controls (if this app is used to publish narrative-facing artifacts)
- Approval gate before publishing
- Provenance completeness check
- Redaction/generalization step for sensitive locations

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Secret scan passes (no keys/tokens in `.github/apps/**`)
- [ ] `./permissions.md` exists and is up to date for `<app_slug>`
- [ ] Any permission change is reviewed by a security reviewer
- [ ] Workflows referencing the app are updated and still pass
- [ ] This `workflows.md` mapping is updated in the same PR as any workflow auth change

### Reproduction (documented procedure)
- To recreate or re-install this app:
  1. Use the secret-free manifest file in `./manifest.json` (if present)
  2. Create/install the app in GitHub UI (org/repo settings)
  3. Store generated private key and webhook secret in secret storage
  4. Ensure each workflow references secrets by **name** only (never copy secrets into git)

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| App permission changes | PR review + GitHub audit logs | `docs/telemetry/` (not confirmed in repo) |
| Workflow auth failures | Actions logs | `docs/telemetry/` (not confirmed in repo) |
| Unexpected repo writes | GitHub audit logs | Security incident process |

## 📦 Data & Metadata

### Inputs

| Input | Source | Sensitivity | Notes |
|---|---|---|---|
| App manifest | `./manifest.json` | public | Must not contain secrets |
| Permission justification | `./permissions.md` | public | Required for review |
| Workflow definitions | `.github/workflows/*.yml` | public | Actual pipeline logic |
| Secret material | GitHub Secrets/Environments or external secret store | secret | **Never** committed |

### Outputs

| Output | Where it lives | Sensitivity | Notes |
|---|---|---|---|
| Installed GitHub App integration | GitHub org/repo settings | restricted | Not stored in repo |
| Private key / webhook secret | Secret store | secret | Never commit |
| Short-lived installation tokens | Workflow runtime memory only | secret | Must not be logged |
| Audit trail | GitHub audit logs / PR history | restricted | Use for investigations |

### Workflow inventory (fill in with real workflows)

> Keep this table synchronized with `.github/workflows/` (do not leave “unknown” entries once the app is in use).

| Workflow file | Job id(s) | Trigger(s) | Why the app token is needed | Permissions used (link) | Repo write surface | Secrets referenced (names only) | Notes |
|---|---|---|---|---|---|---|---|
| `.github/workflows/<workflow>.yml` | `<job_id>` | `<pull_request / push / schedule / workflow_dispatch>` | `<e.g., comment on PR with elevated perms>` | `./permissions.md#<anchor>` | `<read-only / writes docs/ / writes data/>` | `<SECRET_NAME_1>, <SECRET_NAME_2>` | `<risk, approvals, environments>` |
| `.github/workflows/<workflow>.yml` | `<job_id>` | `<...>` | `<...>` | `./permissions.md#<anchor>` | `<...>` | `<...>` | `<...>` |

### Token + secret reference notes
- This repo must remain secret-free. Only list **secret names** here.
- Secret naming conventions are **not confirmed in repo**; align with your existing org/repo standard.

Suggested (example-only) secret name placeholders:
- `<APP_SLUG>_APP_ID`
- `<APP_SLUG>_APP_PRIVATE_KEY`
- `<APP_SLUG>_INSTALLATION_ID` (optional; non-secret, but treat carefully)

### Sensitivity & redaction
- Allowed in repo: public manifests, non-secret IDs, and documentation.
- Prohibited in repo: private keys (`*.pem`), webhook secrets, installation access tokens, PATs, or any credential material.
- If a configuration requires a shared secret, store it in GitHub Secrets/Environments and reference it in workflows.

### Quality signals
- Permissions are minimal and justified in writing (`./permissions.md`).
- Workflows use short-lived auth (where possible) and scope-limited permissions.
- Secret scanning and CI checks pass on every PR touching `.github/apps/`.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- N/A unless a workflow using this app publishes STAC artifacts.
- If publishing is automated, outputs must land in the canonical STAC directory (typically `data/stac/`) and include stable IDs.

### DCAT
- N/A unless a workflow using this app publishes DCAT outputs.
- If publishing is automated, outputs must land in the canonical DCAT directory (typically `data/catalog/dcat/`).

### PROV-O
- N/A unless a workflow using this app generates provenance bundles for a run.
- If used, provenance artifacts should land in the canonical provenance directory (typically `data/prov/`) and reference stable run IDs.

### Versioning
- Changes to app permissions or scopes should be treated like contract changes:
  - document the change,
  - link to the PR/ticket,
  - and ensure review gates are followed.

## 🧱 Architecture

### Components
- GitHub App `<app_slug>` (installed at org/repo scope) for automation requiring GitHub API access
- GitHub Actions workflows that may authenticate via the app
- Secret storage for private keys / webhook secrets / other credentials

### Interfaces / contracts
- GitHub App → GitHub API permissions: defined and justified in `./permissions.md`
- Workflow → App credentials: referenced via GitHub Secrets/Environments (never committed)
- KFM boundary: workflows should call the KFM API layer rather than reading Neo4j directly

### Extension points checklist (for future work)
- [ ] Add or update workflow inventory rows for each workflow using `<app_slug>`
- [ ] Add `./rotation.md` if key rotation cadence or incident posture needs to be explicit
- [ ] Add telemetry documentation if auth failures or repo writes are operationally important
- [ ] Flag any permission increases as **requires human review**

## ⚖ FAIR+CARE & Governance

### Review gates
- Permission increases and any automation that writes to `data/`, `docs/reports/`, or publishes story artifacts should be reviewed by:
  - CI owners
  - a security reviewer
  - and (if narrative-facing) the governance/review gate owners

### CARE / sovereignty considerations
- If a workflow using this app processes culturally sensitive or restricted information, follow:
  - redaction/generalization rules
  - access controls
  - and any sovereignty constraints referenced in the governance docs

### AI usage constraints
- Ensure this document’s AI permissions/prohibitions match intended use (see front matter).
- Do not use automated tooling to infer sensitive locations or generate new policy text.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-26 | Initial workflow mapping template for `<app_slug>` | TBD |

---

Footer refs:
- GitHub Apps overview: `.github/apps/README.md`
- Workflows overview: `.github/workflows/README.md`
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

