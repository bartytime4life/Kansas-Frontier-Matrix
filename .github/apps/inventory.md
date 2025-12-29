---
title: "GitHub Apps — Inventory"
path: ".github/apps/inventory.md"
version: "v1.0.0"
last_updated: "2025-12-29"
status: "draft"
doc_kind: "Inventory"
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

doc_uuid: "urn:kfm:doc:github:apps-inventory:v1.0.0"
semantic_document_id: "kfm-github-apps-inventory-v1.0.0"
event_source_id: "ledger:kfm:doc:github:apps-inventory:v1.0.0"
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

# GitHub Apps — Inventory

## 📘 Overview

### Purpose

- Maintain a single, repo-versioned inventory of **GitHub App** integrations used by repository automation.
- Provide traceability from each app → its repo folder (`.github/apps/<app_slug>/`) → the workflows/jobs that depend on it.
- Support least-privilege review and contract-first pipeline governance (see `docs/MASTER_GUIDE_v12.md`).

### Scope

| In Scope | Out of Scope |
|---|---|
| Installed/used GitHub Apps (active/planned/deprecated), installation scope (org/repo), repo targets, workflow/job mapping, required secret **names only**, pointers to per-app docs (manifest/permissions/workflows/rotation), review/last-reviewed tracking | Private keys, webhook secrets, installation tokens, PATs, or any credential *values*; full workflow definitions; generating new policy text; inferring sensitive locations |

### Audience

- Primary: repo maintainers, CI/CD owners, security reviewers
- Secondary: contributors who need to understand why an integration exists and how it is governed

### Definitions

- Glossary link: `docs/glossary.md` *(expected canonical location; if missing, update to repo’s glossary path)*
- Terms used in this doc:
  - **GitHub App**: GitHub-native integration with scoped permissions and auditable installations.
  - **app_slug**: Stable kebab-case identifier used as the folder name under `.github/apps/<app_slug>/`.
  - **Installation scope**: Where the app is installed (`org` or `repo`) and which repositories it can access.
  - **Secrets (names only)**: Identifiers of secrets stored in GitHub Secrets/Environments or an external secret manager (values never committed).
  - **Least privilege**: Only the permissions required for the mapped workflows/jobs and operations.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| GitHub Apps README | `.github/apps/README.md` | Repo maintainers | Folder contract + auth guidance |
| GitHub Apps inventory | `.github/apps/inventory.md` | Repo maintainers | This document (authoritative list) |
| App folders | `.github/apps/<app_slug>/` | App owner | Secret-free manifests + permission/workflow docs |
| Workflows | `.github/workflows/` | CI owners | Workflows that may use app-based auth |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | Pipeline ordering + CI gates + subsystem homes |
| Security / governance refs | `docs/governance/*` + `.github/SECURITY.md` *(if present)* | Security reviewers | Review gates, incidents, sovereignty |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (path/version/last_updated)
- [ ] Every `.github/apps/<app_slug>/` folder has a matching entry in the inventory table
- [ ] Every inventory entry links to required per-app docs (permissions/manifest/workflows)
- [ ] Secrets are documented by **name only** (no values in repo)
- [ ] Permission increases have explicit security review recorded in the PR
- [ ] Validation steps below are repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `.github/apps/inventory.md` *(must match front-matter)*

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI | `.github/` | Workflows + policy gates |
| GitHub Apps docs | `.github/apps/` | App manifests + permission/runbook docs (secret-free) |
| Workflows | `.github/workflows/` | CI/CD pipelines that may call GitHub APIs |
| Local actions | `.github/actions/` *(if present)* | Repo-local composite actions (preferred for reusable gate logic) |
| Documentation | `docs/` | Canonical governed docs (architecture, standards, runbooks) |
| Pipelines | `src/pipelines/` | ETL + catalog + transforms (may be triggered by CI) |
| Graph | `src/graph/` | Ontology bindings, ingest/migrations, integrity constraints |
| API boundary | `src/server/` | Contracted access layer; redaction enforcement |
| UI | `web/` | React + MapLibre (+ optional Cesium); Focus Mode UX |
| Story Nodes | `docs/reports/story_nodes/` *(pattern)* | Templates, draft/published narratives, assets |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV outputs (when pipelines run) |
| MCP artifacts | `mcp/runs/` + `mcp/experiments/` | Run logs, experiments, model cards, SOPs |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 apps/
    ├── 📄 README.md
    ├── 📄 inventory.md
    └── 📁 <app_slug>/
        ├── 📄 permissions.md
        ├── 📄 manifest.json
        ├── 📄 workflows.md
        ├── 📄 rotation.md               # optional but recommended
        └── 📁 assets/                   # optional
~~~

### Inventory ↔ per-app folder contract

- Every GitHub App used by any workflow in this repository must have:
  - an inventory entry in this file, **and**
  - a corresponding folder at `.github/apps/<app_slug>/`.
- The `app_slug` is the canonical identifier for cross-references.
- If an app is deprecated, mark it as `deprecated` here and keep documentation until all workflows are migrated.

## 🧭 Context

### Why this inventory exists

GitHub Apps provide scoped permissions and auditable installations, but they introduce moving parts (permissions, installation scope, key rotation, workflow dependencies). KFM treats these as governed interfaces that must be documented and reviewable.

### Pipeline alignment

KFM’s pipeline ordering is non-negotiable:

- **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

A GitHub App that can write governed artifacts (e.g., `data/**`, `docs/**`, `mcp/**`) must be documented here so reviewers can confirm the correct validations run before publish/merge.

### Assumptions

- This repository may be public; anything in `.github/apps/**` must be safe to disclose.
- Secrets are stored in GitHub Secrets/Environments or an external secret manager (never committed to git).
- Frontend consumes data via contracted APIs (no direct graph access from UI).

### Constraints / invariants

- Never commit private keys, webhook secrets, installation tokens, PATs, or credential values to this directory.
- Permission increases require explicit security review.
- If an app-authenticated workflow publishes governed artifacts, outputs must be deterministic and land in canonical homes.

## 🗺️ Diagrams

### Inventory relationship diagram

~~~mermaid
flowchart LR
  INV[.github/apps/inventory.md] --> APPDIR[.github/apps/<app_slug>/]
  APPDIR --> MAN[manifest.json]
  APPDIR --> PERM[permissions.md]
  APPDIR --> WFMAP[workflows.md]
  WFMAP --> WF[.github/workflows/*.yml]
  WF -->|may write| DATA[data/**]
  WF -->|may write| DOCS[docs/**]
  WF -->|may write| MCP[mcp/**]
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Source | Validation / constraints |
|---|---|---|---|
| Per-app docs | Markdown + JSON | `.github/apps/<app_slug>/` | Required files present; no secrets; links resolve |
| Workflow references | YAML (by reference) | `.github/workflows/` | Inventory should name workflows/jobs using the app |
| Installation scope | GitHub settings | GitHub UI/API | Record scope at a high level; avoid sensitive operational detail |
| Secret names | Text | Secret manager + workflow docs | Names only; values never appear in repo |

### Outputs

| Output | Format | Where recorded | Contract / notes |
|---|---|---|---|
| App inventory | Markdown | `.github/apps/inventory.md` | This file; governed documentation |
| Review evidence | PR metadata | GitHub PR | Approvals/justifications live in PR reviews |
| Optional machine-readable inventory | YAML/JSON | *(not confirmed in repo)* | Future extension for CI validation |

### Sensitivity & redaction

- This file is `classification: open` and `sensitivity: public`.
- Document secret **names only** (never values).
- Avoid operational details that would weaken security posture (e.g., full incident playbooks with sensitive steps).

### Current inventory summary (fill in)

| Metric | Value | Notes |
|---|---|---|
| Total apps recorded | TBD | Count of entries in the table below |
| Active apps | TBD | `status: active` |
| Deprecated apps | TBD | `status: deprecated` |
| Planned apps | TBD | `status: planned` |
| Last reviewed | TBD | Date + reviewer role(s) |
| Next review due | TBD | Suggested: quarterly or on permission changes |

### Inventory table (authoritative)

> If an app is used by workflows but missing from this table, treat it as **non-compliant** and block until inventory + per-app docs exist.

| app_slug | GitHub App name | status | installation_scope | installation_target | workflows/jobs | per-app docs | secrets (names only) | governed outputs written | owner | security reviewer | last_reviewed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `<app_slug>` | `<display_name>` | planned | repo/org | `<org>/<repo(s)>` | `<workflow>.yml :: <job>` | `.github/apps/<app_slug>/` | `<SECRET_NAME_1>`, `<SECRET_NAME_2>` | `none/TBD` | TBD | TBD | YYYY-MM-DD |

### Per-app entry template (copy/paste)

#### `<app_slug>`

- **GitHub App name:** `<display_name>`
- **Status:** `active | planned | deprecated`
- **Installation scope:** `repo | org`
- **Repositories in scope:** `<org>/<repo>` (list)
- **Primary purpose:** `<1–2 sentences>`
- **Workflows/jobs using this app:**
  - `.github/workflows/<workflow>.yml` → `<job>` — `<brief purpose>`
- **Per-app docs:**
  - Permissions: `.github/apps/<app_slug>/permissions.md`
  - Manifest: `.github/apps/<app_slug>/manifest.json` *(secret-free)*
  - Workflow mapping: `.github/apps/<app_slug>/workflows.md`
  - Rotation/runbook: `.github/apps/<app_slug>/rotation.md` *(recommended)*
- **Secrets (names only):**
  - `<SECRET_NAME>` (stored in: `GitHub Secrets` / `GitHub Environments` / external manager)
- **Governed outputs written (if any):**
  - `data/**` (ETL/catalog outputs)
  - `docs/**` (docs/story)
  - `mcp/**` (runs/experiments)
- **Last reviewed:** `YYYY-MM-DD` (by: `<name/role>`)

### Future extensions

- Add a machine-readable companion (e.g., `.github/apps/inventory.yaml`) for CI validation. *(not confirmed in repo)*
- Add a validator job that:
  - enumerates `.github/apps/*/` folders,
  - asserts each folder appears in the inventory table,
  - asserts required files exist,
  - runs secret scan + link checks.

## 🌐 STAC, DCAT & PROV Alignment

> GitHub Apps do not inherently produce STAC/DCAT/PROV, but they may be used by workflows that run KFM pipelines that do.

### STAC

- If an app-authenticated workflow generates STAC, outputs must land in:
  - `data/stac/collections/`
  - `data/stac/items/`
- Validate item/collection integrity and stable IDs before publishing.

### DCAT

- If produced, DCAT discovery outputs must land in `data/catalog/dcat/` and remain schema-valid.

### PROV-O

- If produced, provenance bundles must land in `data/prov/` and include run identifiers and traceability metadata.

### Inventory hook

For each app entry, populate “governed outputs written” to help reviewers verify that the right validation/provenance steps exist in workflows.

## 🧱 Architecture

### Components (high level)

| Component | Responsibility | Notes |
|---|---|---|
| Inventory (this file) | Authoritative list of GitHub Apps and usage | Governed documentation |
| Per-app folder | Secret-free manifest + permissions + workflow mapping | `.github/apps/<app_slug>/` |
| GitHub Actions workflows | Trigger, validate, run pipelines, publish artifacts | `.github/workflows/**` |
| Secret storage | Store private keys/webhook secrets | GitHub Secrets/Environments or external manager |
| KFM subsystems | Pipelines, catalogs, graph, API, UI, story | Canonical homes per Master Guide |

### Interfaces / contracts

| Interface | Contract | Where defined |
|---|---|---|
| Inventory ↔ per-app folder | Every folder has an inventory row; every row points to a folder | `.github/apps/inventory.md` + `.github/apps/README.md` |
| Least privilege justification | Explicit permission list mapped to workflows/jobs | `.github/apps/<app_slug>/permissions.md` |
| Secret handling | Names only in repo; values only in secret storage | `.github/apps/README.md` + governance refs |
| Pipeline ordering | ETL → catalogs → graph → API → UI → story → Focus Mode | `docs/MASTER_GUIDE_v12.md` |
| API boundary | UI never reads Neo4j directly | `src/server/**` + contracts *(location may vary)* |

### Extension points checklist (when adding a new GitHub App)

- [ ] Create `.github/apps/<app_slug>/` with required files
- [ ] Add an entry to this inventory in the same PR
- [ ] Document permissions with least-privilege justification
- [ ] Document secrets by **name only** (and where they live)
- [ ] Map the app to specific workflows/jobs
- [ ] Add security review requirement for permission increases
- [ ] If workflows publish governed artifacts, ensure validations + provenance generation are present

## 🧠 Story Node & Focus Mode Integration

### Narrative-facing workflows

If a GitHub App–authenticated workflow writes narrative-facing artifacts (e.g., `docs/reports/story_nodes/**`), it must enforce:

- provenance links (run IDs / dataset IDs),
- citations/evidence pointers for factual claims,
- explicit labeling of fact vs inference vs hypothesis,
- adherence to “do not infer sensitive locations.”

### Inventory field for narrative impact (optional)

- In the per-app entry, list whether `docs/reports/story_nodes/**` is touched under “governed outputs written.”

## 🧪 Validation & CI/CD

### Validation steps (minimum)

- [ ] Secret scan passes (no keys/tokens in `.github/apps/**`)
- [ ] `permissions.md`, `manifest.json`, `workflows.md` exist for every `.github/apps/<app_slug>/`
- [ ] Every `.github/apps/<app_slug>/` folder appears in the inventory table
- [ ] Inventory links resolve (workflows, per-app docs, governance refs)
- [ ] Permission changes have security approval recorded in PR

### Recommended CI gates for `.github/apps/**` changes

- Markdown protocol validation (front-matter + required headings)
- Link/reference checks (no orphan pointers)
- JSON parsing/validation for `manifest.json` (schema if available)
- Security + sovereignty scanning (as applicable):
  - secret scan
  - PII scan
  - sensitive-location leakage checks
  - classification propagation checks

## ⚖ FAIR+CARE & Governance

### Review gates

Permission increases and any automation that writes to governed outputs (e.g., `data/`, `docs/reports/`, `mcp/`) should be reviewed by:

- CI owners
- security reviewers
- and (if narrative-facing) governance/story review gate owners

### CARE / sovereignty considerations

- If an app/workflow processes culturally sensitive or restricted information, follow sovereignty and redaction/generalization rules.
- Do not infer sensitive locations; ensure any redaction policies are enforced in datasets, catalogs, APIs, and UI.

### AI usage constraints

- This document’s AI permissions/prohibitions are declared in the front matter.
- Do not use automated tooling to infer sensitive locations or generate new policy text.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-29 | Initial GitHub Apps inventory scaffold aligned to `.github/apps/README.md` and KFM Universal template | TBD |

---

Footer refs (canonical pointers):

- GitHub Apps README: `.github/apps/README.md`
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Markdown work protocol: `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` *(not confirmed in repo)*
