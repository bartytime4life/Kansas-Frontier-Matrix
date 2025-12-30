---
title: "KFM — GitHub App Workflow Mapping — <app_slug>"
path: ".github/apps/<app_slug>/workflows.md"
version: "v1.0.1"
last_updated: "2025-12-30"
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

doc_uuid: "urn:kfm:doc:github:apps:<app_slug>:workflows:v1.0.1"
semantic_document_id: "kfm-github-app-<app_slug>-workflows-v1.0.1"
event_source_id: "ledger:kfm:doc:github:apps:<app_slug>:workflows:v1.0.1"
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

> Replace `<app_slug>` everywhere in this document, including the front-matter identifiers.  
> This document is **public** and must remain **secret-free**: secret names are allowed; secret values are prohibited.

## 📘 Overview

### Purpose
- Map **exactly which GitHub Actions workflows and jobs** authenticate as GitHub App `<app_slug>`.
- Make least-privilege review concrete by linking each workflow usage to `./permissions.md`.
- Make CI changes auditable: if app usage changes, update this file in the same PR as the workflow change.

### Scope

| In Scope | Out of Scope |
|---|---|
| Mapping workflows → jobs that use the app (file, job id, trigger, why needed) | Full workflow definitions (they live in `.github/workflows/*.yml`) |
| Secret *names* referenced (never values) | Private keys, webhook secrets, installation tokens, PATs |
| Repo write surfaces / artifacts created by app-authenticated jobs | Editing org/repo settings directly from this repo (document only) |
| Change-review triggers when app auth is added/removed | Describing security policy beyond what is referenced in governance docs |

### Audience
- Primary: repo maintainers, CI/CD owners, security reviewers
- Secondary: contributors who need to understand why an app token is used

### Definitions
- Link: `docs/glossary.md` *(not confirmed in repo; use if present)*
- Terms used in this doc:
  - **GitHub App**: an installed integration with explicitly granted permissions.
  - **Installation**: the app installed into an org or repo.
  - **Installation token**: short-lived token minted at workflow runtime.
  - **Workflow / job**: GitHub Actions units that may request app-authenticated access.
  - **Repo write surface**: the set of paths/targets a job can modify when authenticated.
  - **Contract change**: any change that alters where/how the app is used or what it can do.

### App identity
Only non-secret metadata belongs here.

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
| Master Guide | `docs/MASTER_GUIDE_v12.md` | Docs | Canonical pipeline ordering + invariants |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Default governed doc template |
| GitHub App permissions justification | `.github/apps/<app_slug>/permissions.md` | App owner | Must justify all requested permissions |
| App manifest | `.github/apps/<app_slug>/manifest.json` | App owner | Optional; must be secret-free |
| Rotation runbook | `.github/apps/<app_slug>/rotation.md` | App owner | Optional; recommended if key rotation is operationally important |
| Workflow mapping | `.github/apps/<app_slug>/workflows.md` | App owner + CI owners | This document; must stay in sync with actual workflows |
| CI workflow inventory | `.github/workflows/` | CI owners | Source of truth for pipeline execution |
| Workflows overview | `.github/workflows/README.md` | CI owners | *not confirmed in repo*; add if missing |
| GitHub Apps overview | `.github/apps/README.md` | Repo maintainers | *not confirmed in repo*; add if multiple apps exist |
| Security standards | `.github/SECURITY.md` + `docs/security/` | Security reviewers | *not confirmed in repo*; use your repo’s canonical security docs |

### Definition of done
- [ ] Front-matter complete + valid
- [ ] All workflows/jobs using the app are listed below (no “implicit” usage)
- [ ] Each listed workflow usage links to the exact permission block in `./permissions.md`
- [ ] No secrets committed (private keys/webhook secrets/tokens); secret names only
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Version history entry added for each meaningful change

## 🗂️ Directory Layout

### This document
- `path`: `.github/apps/<app_slug>/workflows.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub App docs & artifacts | `.github/apps/<app_slug>/` | This app’s docs, manifest, and assets |
| Workflows | `.github/workflows/` | CI pipelines that may use app-based auth |
| Local composite actions | `.github/actions/` | Reusable actions (if present) |
| Data domains | `data/` | `raw/`, `work/`, `processed/`, `stac/`, `catalog/dcat/`, `prov/` |
| Pipelines | `src/pipelines/` | ETL + catalog + transforms |
| Graph | `src/graph/` | Graph build + ontology bindings |
| API server | `src/server/` | Contracted access layer |
| UI | `web/` | React/MapLibre app (no direct graph calls) |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| MCP | `mcp/` | Runs/experiments and model artifacts |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 apps/
    └── 📁 <app_slug>/
        ├── 📄 permissions.md
        ├── 📄 manifest.json
        ├── 📄 workflows.md
        ├── 📄 rotation.md
        └── 📁 assets/
            └── 📄 <optional_files>
~~~

## 🧭 Context

### Background
- GitHub Apps are preferred over long-lived personal tokens when automation needs to interact with GitHub.
- This mapping exists to make “who can do what in CI” reviewable and reproducible.

### Assumptions
- This repository may be public; anything committed here should be safe to disclose.
- Secrets are managed via GitHub Environments/Secrets or an external secret manager and are not stored in git.
- Workflows use short-lived installation tokens, and tokens are never printed to logs.

### Constraints / invariants
- Preserve the canonical ordering: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend consumes contracts via APIs and never reads Neo4j directly.
- Never commit private keys, webhook secrets, tokens, or any credential material to `.github/apps/**`.
- Repo write access must be explicit, justified, and mapped to `./permissions.md`.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Confirm App ID + Display name | `<TBD>` | `<TBD>` |
| Confirm installation scope and installed repo/org | `<TBD>` | `<TBD>` |
| Confirm which workflows/jobs actually use `<app_slug>` | CI owners | `<TBD>` |
| Confirm secret naming convention for app credentials | Security + CI owners | `<TBD>` |
| Confirm whether rotation runbook is required | App owner | `<TBD>` |

### Future extensions
- Add an automated check that fails PRs if a workflow begins using `<app_slug>` but this mapping table is not updated.
- Add `rotation.md` and document revocation/rotation steps if the app is operationally critical.
- Add telemetry documentation if auth failures or repo writes are operationally important.

### Change-management rule
Treat any of the following as a contract change requiring human review and a version-history entry:
- New workflow/job begins using this app
- A workflow/job stops using this app
- Permission scope increases or a new permission is requested
- A job’s repo-write surface expands, especially into `data/`, `docs/`, or story artifacts

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  PR[Pull Request / Push] --> WF[GitHub Actions Workflow]

  WF --> V[Validation Jobs]
  WF --> AUTH[GitHub App Auth: <app_slug>]
  AUTH --> GH[GitHub API]

  V --> ART[Artifacts: logs / reports]

  WF --> KFM[Optional: KFM pipeline tasks]
  subgraph KFM[Canonical KFM pipeline ordering]
    ETL[ETL] --> CAT[STAC/DCAT/PROV]
    CAT --> G[Neo4j Graph]
    G --> API[API Layer]
    API --> UI[React/Map UI]
    UI --> SN[Story Nodes]
    SN --> FM[Focus Mode]
  end
~~~

### Optional sequence diagram

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
  WF->>API: Optional contract tests (never direct Neo4j)
~~~

## 📦 Data & Metadata

### Inputs

| Input | Source | Sensitivity | Notes |
|---|---|---|---|
| App manifest | `.github/apps/<app_slug>/manifest.json` | public | Must not contain secrets |
| Permission justification | `.github/apps/<app_slug>/permissions.md` | public | Required for review |
| Workflow definitions | `.github/workflows/*.yml` | public | Actual pipeline logic |
| Secret material | GitHub Secrets/Environments or external secret store | secret | Never committed |

### Outputs

| Output | Where it lives | Sensitivity | Notes |
|---|---|---|---|
| Installed GitHub App integration | GitHub org/repo settings | restricted | Not stored in repo |
| Private key / webhook secret | Secret store | secret | Never commit |
| Short-lived installation tokens | Workflow runtime memory only | secret | Must not be logged |
| Audit trail | GitHub audit logs / PR history | restricted | Use for investigations |
| Optional published artifacts | repo paths (e.g., `data/`, `docs/`) | varies | Must be explicitly mapped per workflow below |

### Workflow inventory
Keep this table synchronized with `.github/workflows/`. Do not leave “unknown” entries once the app is in use.

| Workflow file | Job id(s) | Trigger(s) | KFM stage(s) touched | Why the app token is needed | Permissions used | Repo write surface | Secrets referenced (names only) | Environment | Notes |
|---|---|---|---|---|---|---|---|---|---|
| `.github/workflows/<workflow>.yml` | `<job_id>` | `<pull_request / push / schedule / workflow_dispatch>` | `<ETL / Catalog / Graph / API / UI / Story / None>` | `<e.g., comment on PR with elevated perms>` | `./permissions.md#<anchor>` | `<read-only / writes docs/ / writes data/>` | `<SECRET_NAME_1>, <SECRET_NAME_2>` | `<env-name or none>` | `<risk, approvals, environments>` |
| `.github/workflows/<workflow>.yml` | `<job_id>` | `<...>` | `<...>` | `<...>` | `./permissions.md#<anchor>` | `<...>` | `<...>` | `<...>` | `<...>` |

### Token and secret reference notes
- This repo must remain secret-free. Only list **secret names** here.
- Secret naming conventions are **not confirmed in repo**; align with your existing org/repo standard.

Suggested example placeholders:
- `<APP_SLUG>_APP_ID`
- `<APP_SLUG>_APP_PRIVATE_KEY`
- `<APP_SLUG>_INSTALLATION_ID` (optional; may be non-secret, but treat carefully)

### Sensitivity and redaction
- Allowed in repo: public manifests, non-secret IDs, and documentation.
- Prohibited in repo: private keys (`*.pem`), webhook secrets, installation access tokens, PATs, or any credential material.
- If a configuration requires a shared secret, store it in GitHub Secrets/Environments and reference it in workflows.

### Quality signals
- Permissions are minimal and justified in writing (`./permissions.md`).
- Workflows use short-lived auth and scope-limited permissions.
- Secret scanning and CI checks pass on every PR touching `.github/apps/`.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Current status: none published via `<app_slug>`-authenticated jobs (as of `v1.0.1`).
- If a workflow using this app publishes STAC artifacts:
  - outputs must land in `data/stac/collections/` and `data/stac/items/`
  - stable IDs must be used
  - the workflow row above must indicate the repo write surface and STAC scope

### DCAT
- Current status: none published via `<app_slug>`-authenticated jobs (as of `v1.0.1`).
- If automated, outputs must land in `data/catalog/dcat/` and align to the project DCAT profile.

### PROV-O
- Current status: none generated via `<app_slug>`-authenticated jobs (as of `v1.0.1`).
- If used, provenance artifacts should land in `data/prov/` and reference stable run IDs.

### Versioning
- Changes to app permissions or scopes are contract changes:
  - document the change,
  - link to the PR/ticket,
  - and ensure review gates are followed.

## 🧱 Architecture

### Components
- GitHub App `<app_slug>` installed at org/repo scope for automation requiring GitHub API access
- GitHub Actions workflows that may authenticate via the app
- Secret storage for private keys/webhook secrets/other credentials

### Interfaces / contracts
- GitHub App → GitHub API permissions: defined and justified in `./permissions.md`
- Workflow → App credentials: referenced via GitHub Secrets/Environments (never committed)
- KFM boundary: workflows should call the KFM API layer rather than reading Neo4j directly

### Extension points checklist
- [ ] Add or update workflow inventory rows for each workflow using `<app_slug>`
- [ ] Add `rotation.md` if key rotation cadence or incident posture needs to be explicit
- [ ] Add telemetry documentation if auth failures or repo writes are operationally important
- [ ] Flag any permission increases as requires human review

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Typically indirect: CI automation may generate or validate Story Node artifacts, data catalogs, or provenance bundles that later surface in the UI.

### Provenance-linked narrative rule
- Any automation that generates narrative content must preserve provenance and avoid unsourced narrative claims.

### Optional structured controls
Use if this app is involved in publishing narrative-facing artifacts.
- Approval gate before publishing
- Provenance completeness check
- Redaction/generalization step for sensitive locations

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Secret scan passes (no keys/tokens in `.github/apps/**`)
- [ ] `.github/apps/<app_slug>/permissions.md` exists and is up to date
- [ ] Any permission change is reviewed by a security reviewer
- [ ] Workflows referencing the app still pass after changes
- [ ] This `workflows.md` mapping is updated in the same PR as any workflow auth change
- [ ] If repo write surface includes governed outputs (`data/`, `docs/reports/`, story artifacts), ensure additional review gates are applied

### Reproduction
To recreate or re-install this app:
1. Use the secret-free manifest file in `./manifest.json` (if present)
2. Create/install the app in GitHub UI (org/repo settings)
3. Store generated private key and webhook secret in secret storage
4. Ensure each workflow references secrets by name only and never copies secrets into git

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| App permission changes | PR review + GitHub audit logs | `docs/telemetry/` *(not confirmed in repo)* |
| Workflow auth failures | Actions logs | `docs/telemetry/` *(not confirmed in repo)* |
| Unexpected repo writes | GitHub audit logs | Security incident process |

## ⚖ FAIR+CARE & Governance

### Review gates
Permission increases and any automation that writes to `data/`, `docs/`, or publishes story artifacts should be reviewed by:
- CI owners
- a security reviewer
- and, if narrative-facing, governance/review gate owners

### CARE / sovereignty considerations
If a workflow using this app processes culturally sensitive or restricted information, follow:
- redaction/generalization rules
- access controls
- sovereignty constraints referenced in governance docs

### AI usage constraints
- Ensure this document’s AI permissions/prohibitions match intended use.
- Do not use automated tooling to infer sensitive locations or generate new policy text.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.1 | 2025-12-30 | Align to KFM Universal template structure; add definitions, open questions, and stronger workflow inventory fields | TBD |
| v1.0.0 | 2025-12-26 | Initial workflow mapping template for `<app_slug>` | TBD |

---

Footer refs:
- GitHub Apps overview: `.github/apps/README.md` *(not confirmed in repo)*
- Workflows overview: `.github/workflows/README.md` *(not confirmed in repo)*
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
