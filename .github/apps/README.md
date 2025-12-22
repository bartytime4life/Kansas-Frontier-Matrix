---
title: "GitHub Apps — Repository Automation"
path: ".github/apps/README.md"
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
- Link: `docs/glossary.md`
- Terms used in this doc: **GitHub App**, **App manifest**, **installation**, **webhook secret**, **private key**, **least privilege**, **OIDC**

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| GitHub Apps README | `.github/apps/README.md` | Repo maintainers | This document |
| App definition folder | `.github/apps/<app_slug>/` | App owner | One folder per GitHub App integration |
| Workflow inventory | `.github/workflows/` | CI owners | Workflows that may use app-based auth |
| Security standards | `.github/SECURITY.md` + `docs/security/` | Security reviewers | Cross-reference for credential handling |

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
  participant API as KFM API
  Dev->>GH: Open PR
  GH->>WF: Trigger workflow
  WF->>App: Request installation token (via stored credentials)
  App-->>WF: Short-lived token
  WF->>GH: Comment/status/update checks
  WF->>API: (Optional) call KFM API to run contract tests
~~~

## 📦 Data & Metadata

### Inputs

| Input | Source | Sensitivity | Notes |
|---|---|---|---|
| App manifest | `.github/apps/<app_slug>/manifest.json` | public | Must not contain secrets |
| Permission justification | `.github/apps/<app_slug>/permissions.md` | public | Required for review |
| Workflow mapping | `.github/apps/<app_slug>/workflows.md` | public | Which workflows rely on the app |

### Outputs

| Output | Where it lives | Sensitivity | Notes |
|---|---|---|---|
| Installed GitHub App integration | GitHub org/repo settings | restricted | Not stored in repo |
| Private key / webhook secret | Secret store | secret | Never commit |
| Audit trail | GitHub audit logs / PR history | restricted | Use for investigations |

### Sensitivity & redaction
- Allowed in repo: public manifests, non-secret IDs, and documentation.
- Prohibited in repo: private keys (`*.pem`), webhook secrets, installation access tokens, PATs, or any credential material.
- If a configuration requires a shared secret, store it in GitHub Secrets/Environments and reference it in workflows.

### Quality signals
- Permissions are minimal and justified in writing.
- Workflows use short-lived auth (where possible) and scope-limited permissions.
- Secret scanning and CI checks pass on every PR touching `.github/apps/`.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- N/A unless an app/workflow publishes STAC artifacts.
- If publishing is automated, outputs must land in the canonical STAC directory and include stable IDs.

### DCAT
- N/A unless an app/workflow publishes DCAT outputs.

### PROV-O
- N/A unless an app/workflow generates provenance bundles for a run.

### Versioning
- Changes to app permissions or scopes should be treated like contract changes:
  - document the change,
  - link to the PR/ticket,
  - and ensure review gates are followed.

## 🧱 Architecture

### Components
- GitHub Apps (installed at org/repo scope) for automation requiring GitHub API access
- GitHub Actions workflows that may authenticate via a GitHub App
- Secret storage for private keys / webhook secrets / other credentials

### Interfaces / contracts
- GitHub App → GitHub API permissions: defined and justified in `permissions.md`
- Workflow → App credentials: referenced via GitHub Secrets/Environments (never committed)
- KFM boundary: workflows should call the KFM API layer rather than reading Neo4j directly

### Extension points checklist (for future work)
- [ ] Create `.github/apps/<app_slug>/`
- [ ] Add `permissions.md` (required)
- [ ] Add `manifest.json` (optional; must be secret-free)
- [ ] Add `workflows.md` mapping which workflows/jobs depend on the app
- [ ] Document any rotation/revocation expectations (optional `rotation.md`)
- [ ] Flag any permission increases as **requires human review**

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Typically indirect: CI automation may generate or validate Story Node artifacts, data catalogs, or provenance bundles that later surface in the UI.

### Provenance-linked narrative rule
- Any automation that generates narrative content must preserve provenance and avoid unsourced narrative claims (link story artifacts to dataset/document IDs and/or PROV run IDs).

### Optional structured controls
- If an app is used to publish story artifacts automatically, consider adding:
  - an approval gate before publishing
  - a provenance completeness check
  - a redaction/generalization step for sensitive locations

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Secret scan passes (no keys/tokens in `.github/apps/**`)
- [ ] `permissions.md` exists for every `.github/apps/<app_slug>/`
- [ ] Any permission change is reviewed by a security reviewer
- [ ] Workflows referencing the app are updated and still pass
- [ ] Documentation in this README (or per-app docs) updated

### Reproduction
- To recreate an app from a manifest:
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
| v1.0.0 | 2025-12-22 | Initial README for `.github/apps/` | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
