---
title: "GitHub Apps — Repository Automation"
path: ".github/apps/README.md"
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

doc_uuid: "urn:kfm:doc:github:apps-readme:v1.0.0"
semantic_document_id: "kfm-github-apps-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:apps-readme:v1.0.0"
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

# GitHub Apps

## 📘 Overview

### Purpose

- Provide a single, repo-versioned location for GitHub App manifests and operational documentation used by repository automation.
- Standardize how we request/review app permissions and how CI workflows authenticate **without committing secrets**.

### Scope

| In Scope | Out of Scope |
|---|---|
| Public GitHub App manifests (no secrets), permission justifications, rotation/runbook notes, mapping apps → workflows/jobs | Private keys, webhook secrets, installation tokens, and other credentials (must live in secret storage); GitHub Action workflow definitions themselves |

### Audience

- Primary: repo maintainers, CI/CD owners, security reviewers
- Secondary: contributors who need to understand why an integration exists

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc: **GitHub App**, **App manifest**, **installation**, **webhook secret**, **private key**, **least privilege**, **OIDC**

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| GitHub Apps README | `.github/apps/README.md` | Repo maintainers | This document |
| App definition folder | `.github/apps/<app_slug>/` | App owner | One folder per GitHub App integration |
| Workflow inventory | `.github/workflows/` | CI owners | Workflows that may use app-based auth |
| Security standards | `.github/SECURITY.md` + `docs/security/` | Security reviewers | Credential handling and incident process *(paths may be optional depending on repo snapshot)* |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | Pipeline invariants + contract-first rules |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] App permission requests are documented and justified (least privilege)
- [ ] No secrets committed (private keys/webhook secrets/tokens)
- [ ] Workflows depending on an app are listed and reviewed
- [ ] Validation steps below are repeatable

## 🗂️ Directory Layout

### This document

- `path`: `.github/apps/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub platform config | `.github/` | Workflows, issue templates, security policy |
| Workflows | `.github/workflows/` | CI/CD pipelines that may call GitHub APIs |
| Local actions | `.github/actions/` | Repo-local composite actions (preferred for reusable gate logic) |
| Documentation | `docs/` | Canonical governed docs (architecture, standards, runbooks) |
| Pipelines | `src/pipelines/` | ETL + catalog + transforms (may be triggered by CI) |
| API server | `src/server/` | Contracted access layer (REST/GraphQL) |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 apps/
    ├── 📄 README.md
    └── 📁 <app_slug>/
        ├── 📄 permissions.md
        ├── 📄 manifest.json
        ├── 📄 workflows.md
        └── 📁 assets/
            └── 📄 <optional_files>
~~~

### Per-app folder contract

For every `.github/apps/<app_slug>/`:

- `permissions.md` (required): permission list + justification, including why the workflow cannot use a built-in token.
- `manifest.json` (required): **secret-free** GitHub App manifest (safe to commit).
- `workflows.md` (required): which workflows/jobs depend on the app, and which secrets are expected by name (but never the secret values).
- `assets/` (optional): diagrams/screenshots or supporting docs that are safe to publish.

## 🧭 Context

### Background

- KFM uses repository automation (CI/CD + governance gates) to keep data, catalogs, graph, APIs, UI, and narrative outputs synchronized and reviewable.
- GitHub Apps are preferred over long-lived personal tokens when automation needs to interact with GitHub (least privilege + auditable installations).

### Assumptions

- This repository may be public; anything committed here should be safe to disclose.
- Secrets are managed via GitHub Environments/Secrets or an external secret manager (not stored in git).

### Constraints / invariants

- Preserve the canonical ordering: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Never commit private keys, webhook secrets, or tokens into this directory.
- If an app/workflow writes to governed artifacts (e.g., `data/**`, `docs/reports/**`), it must remain:
  - deterministic and diffable, and
  - aligned to contract validation (schemas, catalogs, provenance) before any publication steps.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which GitHub Apps are installed and used for this repo/org? | TBD | TBD |
| Do we require org-level installs for any automation, or repo-level only? | TBD | TBD |
| Do any apps trigger/publish data artifacts (STAC/DCAT/PROV) as part of CI? | TBD | TBD |

### Future extensions

- Add an `inventory.md` listing every installed app, installation scope (org/repo), and the workflows/jobs that depend on it.
- Add a standardized `rotation.md` per app (key rotation cadence + incident response pointers).

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  PR[Pull Request] --> WF[GitHub Actions Workflow]
  WF --> V[Validation Jobs]
  WF --> APP[GitHub App Auth]
  APP --> GH[GitHub API]
  V --> ART[Artifacts: logs/reports]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant Dev as Contributor
  participant GH as GitHub
  participant WF as Actions Workflow
  participant App as GitHub App

  Dev->>GH: Open PR
  GH->>WF: Trigger workflow
  WF->>App: Request installation token (via stored credentials)
  App-->>WF: Short-lived token
  WF->>GH: Comment/status/update checks
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Secret scan passes (no keys/tokens in `.github/apps/**`)
- [ ] `permissions.md` exists for every `.github/apps/<app_slug>/`
- [ ] Any permission change is reviewed by a security reviewer
- [ ] Workflows referencing the app are updated and still pass
- [ ] Documentation in this README (or per-app docs) updated

### Reproduction

To recreate an app from a manifest:

1. Use the secret-free manifest file in `.github/apps/<app_slug>/manifest.json`
2. Create/install the app in GitHub UI (org/repo settings)
3. Store generated private key and webhook secret in secret storage
4. Update workflows to reference secrets by name (never copy secrets into git)

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| App permission changes | PR review + GitHub audit logs | `docs/telemetry/` |
| Workflow auth failures | Actions logs | `docs/telemetry/` |
| Unexpected repo writes | GitHub audit logs | Security incident process |

## ⚖ FAIR+CARE & Governance

### Review gates

- Permission increases and any automation that writes to `data/`, `docs/reports/`, or publishes story artifacts should be reviewed by:
  - CI owners
  - a security reviewer
  - and (if narrative-facing) the governance/review gate owners

### CARE / sovereignty considerations

- If an app/workflow processes culturally sensitive or restricted information, follow:
  - redaction/generalization rules
  - access controls
  - and any sovereignty constraints referenced in the governance docs

### AI usage constraints

- Ensure this document’s AI permissions/prohibitions match intended use (see front matter).
- Do not use automated tooling to infer sensitive locations or generate new policy text.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-26 | Initial README for `.github/apps/` | TBD |

---

Footer refs:

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
