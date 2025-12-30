---
title: "GitHub App Rotation Runbook — <app_slug>"
path: ".github/apps/<app_slug>/rotation.md"
version: "v1.0.0"
last_updated: "2025-12-29"
status: "draft"
doc_kind: "Runbook"
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

doc_uuid: "urn:kfm:doc:github-app-rotation:<app_slug>:v1.0.0"
semantic_document_id: "kfm-github-app-rotation-<app_slug>-v1.0.0"
event_source_id: "ledger:kfm:doc:github-app-rotation:<app_slug>:v1.0.0"
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

# GitHub App Rotation Runbook — <app_slug>

## 📘 Overview

### Purpose

- This runbook defines how to rotate credentials associated with the GitHub App **`<app_slug>`** used by repository automation (e.g., GitHub Actions), without leaking secrets or breaking CI-dependent pipeline work.
- It governs:
  - rotation triggers and cadence (policy),
  - the step-by-step rotation procedure (process),
  - and the minimum verification + logging requirements (evidence).

> Replace `<app_slug>` everywhere in this file with the actual GitHub App slug (the directory name under `.github/apps/`).

### Scope

| In Scope | Out of Scope |
|---|---|
| Rotate GitHub App **private key(s)** used for GitHub Actions auth | Changing GitHub App permissions/scopes (separate change control) |
| Rotate webhook secret (only if this repo operates a GitHub App webhook receiver) | Rotating Personal Access Tokens (PATs) unless explicitly required by legacy tooling |
| Update GitHub Actions org/repo/environment secrets/vars used by workflows | Refactoring workflows, except minimal edits required to restore broken auth |
| Validate with CI gates and a known-good workflow/job | Broader org-wide incident response (coordinate with security/ops) |
| Record a rotation event using **fingerprints/IDs only** (never key material) | Storing or documenting secret values anywhere in git |

### Audience

- Primary: Repo administrators, CI maintainers, security/ops on-call for CI integrity.
- Secondary: Owners of pipeline subsystems that rely on CI automation (ETL/Catalog/Graph/API/UI/Story).

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo — add if missing)*
- Terms used in this doc:
  - **GitHub App**: An app installed into an org/repo that can issue installation tokens.
  - **Private key (PEM)**: A key used to sign JWTs for GitHub App authentication.
  - **Installation token**: Short-lived token minted for an app installation.
  - **Rotation**: Replacing a credential with a new one while minimizing downtime.
  - **Overlap window**: Period where both old and new keys may be valid, enabling safe cutover.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Rotation runbook | `.github/apps/<app_slug>/rotation.md` | Repo admins | This file |
| Workflows using app auth | `.github/workflows/` | CI maintainers | Search for secret/var names used for app auth |
| GitHub App admin page | GitHub UI → Org Settings → Developer settings → GitHub Apps → `<app_slug>` | Org admins | Admin-only; do not copy URLs into public docs if they embed org identifiers |
| Security policy | `.github/SECURITY.md` *(if present)* | Security council / repo admins | Reference for incident handling expectations |
| Telemetry/ops logs | `docs/telemetry/` + `schemas/telemetry/` *(if present)* | Observability owners | Optional, if repo has telemetry schema |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] No secrets or credential material included anywhere in git (only fingerprints/IDs)
- [ ] Rotation procedure includes pre-flight, cutover, verification, revocation, rollback guidance
- [ ] Validation steps listed and repeatable (UI steps and/or CLI steps)
- [ ] Governance + CARE/sovereignty considerations explicitly stated (even if “N/A”)
- [ ] A Rotation Log section exists and is append-only

### Rotation policy (normative)

#### Rotation cadence

- **Cadence:** `TBD` (set by repo/org security policy; do not guess).
- Rotate immediately on any **suspected compromise** or accidental exposure.

#### Rotation triggers

- Scheduled rotation per cadence policy.
- Personnel/access change affecting GitHub App administration.
- Suspected or confirmed secret exposure (logs, screenshots, pasted key material, etc.).
- Auth failures in CI that point to app key/installation issues (after verifying non-key root causes).

#### Overlap window

- Preferred: rotate using an overlap window (introduce new key → update secrets → verify → revoke old key).
- If compromise is suspected: shorten overlap and revoke old keys immediately after verification.

### Secrets + identifiers used by workflows (placeholders)

> **Do not add actual values.** Align names to what your workflows already use.

| Name (example) | Description | Where stored | Sensitivity |
|---|---|---|---|
| `<APP_SLUG>_APP_ID` | GitHub App ID | GitHub Actions secret/var | low (but treat as internal) |
| `<APP_SLUG>_INSTALLATION_ID` | App installation ID | GitHub Actions secret/var | internal |
| `<APP_SLUG>_PRIVATE_KEY_PEM` | App private key (PEM) | GitHub Actions **secret** | **restricted** |
| `<APP_SLUG>_WEBHOOK_SECRET` | Webhook secret (optional) | GitHub Actions secret / server env | **restricted** |

## 🗂️ Directory Layout

### This document

- `path`: `.github/apps/<app_slug>/rotation.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI policies + workflows | `.github/` | Workflows and security/policy gates |
| Workflows | `.github/workflows/` | Automation that may rely on the GitHub App |
| GitHub App runbooks | `.github/apps/` | Per-app operational docs (this file) |
| Documentation | `docs/` | Canonical governed docs |
| Pipelines | `src/pipelines/` | ETL/catalog build orchestration (may be triggered by CI) |
| Graph | `src/graph/` | Ontology + ingest/build (may be triggered by CI) |
| API layer | `src/server/` | Contracted access layer (may be built/tested in CI) |
| UI | `web/` | Frontend build/tests (may be built/tested in CI) |
| MCP logs/artifacts | `mcp/runs/` | Run logs and artifacts (if used) |

### Expected file tree for this sub-area

~~~text
📁 .github/
├── 📁 apps/
│   └── 📁 <app_slug>/
│       └── 📄 rotation.md
└── 📁 workflows/
    └── 📄 (workflows that reference the app secrets/vars)
~~~

## 🧭 Context

### Why this exists

- CI automation often depends on GitHub App authentication to perform privileged GitHub API operations (e.g., creating PRs/releases, labeling issues, writing status checks).
- Rotations are routine security hygiene, but are also a common source of CI outages if performed without validation and rollback planning.

### Key invariants

- **No secrets in git**: this runbook must never contain key material (PEM, webhook secret, tokens).
- **Pipeline ordering remains intact**: the repo’s canonical pipeline ordering and contract boundaries must not be bypassed by automation changes.
- **CI gates must stay green**: rotation must preserve required validation/security gates (including secret scanning).

## 🗺️ Diagrams

~~~mermaid
sequenceDiagram
  autonumber
  participant Operator as Maintainer/Operator
  participant App as GitHub App Settings
  participant Secrets as Repo/Org Secrets Store
  participant CI as GitHub Actions Workflows

  Operator->>App: Generate new private key
  App-->>Operator: Download .pem (SENSITIVE, do not commit)
  Operator->>Secrets: Update <APP_SLUG>_PRIVATE_KEY_PEM secret
  Operator->>CI: Run verification workflow/job
  CI->>App: Request installation token (via JWT)
  App-->>CI: Installation token issued
  CI-->>Operator: Verification passes
  Operator->>App: Revoke old private key(s)
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Rotation request | Issue/ticket | GitHub Issues / Ops tracker | Has reason, scope, approvers |
| New private key | PEM file | GitHub App settings UI | Stored securely; never committed |
| Inventory of usages | Search results | `.github/workflows/`, `src/`, etc. | Confirms which secret names are used |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Updated secret(s) | GitHub secret value | Repo/org/environment secrets | Must not appear in logs |
| Rotation log entry | Table row | This document | Append-only; no secret material |
| Verification evidence | Workflow run link / run ID | GitHub Actions | Confirms auth works post-rotation |

### Sensitivity & redaction

- The PEM file and any webhook secrets are **restricted**.
- Store only **fingerprints/IDs** in git:
  - allowed: key ID (from GitHub UI), SHA-256 fingerprint of public key
  - prohibited: private key content, JWTs, installation tokens, webhook secret values

### Quality signals

- Verification workflow succeeds end-to-end (auth → token mint → required GitHub API actions).
- No secret/PII scanning alerts triggered by the rotation PR/changes.
- No downstream pipeline jobs fail due to missing/invalid auth.

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Collections involved: N/A
- Items involved: N/A
- Extension(s): N/A

### DCAT

- Dataset identifiers: N/A
- License mapping: N/A
- Contact / publisher mapping: N/A

### PROV-O

- Operational provenance (optional): record rotation as an ops activity in a separate log system if available.
- `prov:wasGeneratedBy`: N/A (no dataset outputs).
- Activity / Agent identities: capture “who rotated” and “who verified” in the Rotation Log (below).

### Versioning

- Bump this document’s `version` when the **procedure/policy** changes.
- Do **not** bump document version for each routine rotation; append to Rotation Log instead.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| GitHub App `<app_slug>` | Issues installation tokens for automation | GitHub App auth (JWT → installation token) |
| GitHub Actions workflows | Executes repo automation | `.github/workflows/` + secrets/vars |
| KFM subsystems | ETL/Catalog/Graph/API/UI/Story execution | Code paths under `src/`, `web/`, `docs/` |
| Security gates | Prevent accidental leakage | Secret/PII scanning in CI (if configured) |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Workflow expectations | `.github/workflows/` | Changes require CI verification |
| Secret name conventions | Repo/org settings + workflow docs | Keep stable; treat renames as breaking |
| Operational runbooks | `.github/apps/<app_slug>/` | Semver for procedure changes |

### Extension points checklist (for future work)

- [ ] Add a “rotation reminder” automation (issue/PR) keyed to cadence policy *(requires governance review)*
- [ ] Add a dedicated verification workflow for GitHub App auth
- [ ] Add telemetry signal for rotations *(requires schema update if telemetry is governed)*

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Directly: N/A (this is operational infrastructure).
- Indirectly: stable CI auth helps ensure Story Node generation/validation and provenance publishing workflows can run.

### Provenance-linked narrative rule

- N/A (no narrative claims created here).
- This runbook must not introduce unsourced content into Focus Mode.

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Identify all workflows/jobs that depend on the app secrets/vars
- [ ] Generate a new private key in GitHub App settings (do not revoke old yet)
- [ ] Update the GitHub Actions secret value(s) with the new key
- [ ] Run a verification workflow/job and confirm:
  - app auth succeeds
  - installation token mint succeeds
  - downstream GitHub API steps succeed
- [ ] Revoke old key(s) in GitHub App settings after verification
- [ ] Ensure security scanning gates are clean (secret scan, PII scan) if configured

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands/workflow names.

# 1) inventory where the app is referenced
git grep -nE "<app_slug>|APP_ID|INSTALLATION_ID|PRIVATE_KEY" -- .github/workflows src web docs || true

# 2) trigger verification workflow (manual via GitHub UI is acceptable if CLI is not standardized)
# (no repo-wide CLI tooling is assumed here)
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| github_app_rotation_completed (TBD) | Operator | `docs/telemetry/` + `schemas/telemetry/` *(if present)* |
| promotion_blocked (existing) | CI gate | CI logs / telemetry store *(if present)* |

## ⚖ FAIR+CARE & Governance

### Review gates

- Who approves changes?
  - Procedure/policy edits: repo admins + security reviewer (recommended)
  - Emergency rotations: incident commander / security on-call (as defined by org policy)
- What requires council/board sign-off?
  - Any changes that alter secret storage strategy or weaken security scanning gates.

### CARE / sovereignty considerations

- Typically N/A for credential rotation, but do not publish any restricted identifiers or sensitive operational details that could increase attack surface.

### AI usage constraints

- Do not paste secret material (PEM, tokens, webhook secrets) into AI tools.
- AI may be used for:
  - summarizing procedures,
  - formatting/checklists,
  - drafting non-secret operational text.
- AI must not be used to “generate” security policy or invent rotation cadences.

## 🔁 Rotation Log (append-only)

| Date | Reason | Ticket/Issue | Key ID (GitHub) | Public key fingerprint (SHA-256) | Rotated by | Verified by | Notes |
|---|---|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | Use fingerprints/IDs only; never store key material |

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-29 | Initial runbook scaffold for GitHub App rotation | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
