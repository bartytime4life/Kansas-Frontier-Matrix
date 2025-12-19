---
title: ".github/apps — GitHub App Integrations"
path: ".github/apps/README.md"
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

# .github/apps — GitHub App Integrations

## 📘 Overview

### Purpose
- This directory documents **GitHub Apps and equivalent repository-integrated automation** used by KFM repos (installed GitHub Apps, bots, and third-party repo integrations that operate via GitHub’s API/webhooks).
- It provides a **reviewable inventory** of app intent, permission surface area, operational owners, and how each integration interacts with CI/CD.

> This directory is documentation-first. Do **not** store credentials, private keys, webhook secrets, or other sensitive values in-repo.

### Scope
| In Scope | Out of Scope |
|---|---|
| Installed GitHub Apps (org/repo installs) and their permissions, event subscriptions, and operational runbooks | GitHub Actions workflow logic itself (`.github/workflows/`) |
| Bot identities used by integrations (naming, ownership, access patterns) | Pure documentation for contributors (use root `README.md` / `CONTRIBUTING.md`) |
| Where configuration lives for a given integration (e.g., repo files, org settings, secrets) | Secrets values, private keys, tokens (must remain in GitHub Secrets / org secret stores) |
| Governance/security review notes for third-party integrations | “Which apps are installed right now” if not maintained in this directory |

### Audience
- Primary: maintainers, security reviewers, CI/CD owners
- Secondary: contributors proposing new automation

### Definitions
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc:
  - **GitHub App**: a GitHub-native integration installed onto repos/orgs with scoped permissions.
  - **Installation scope**: org-wide vs repo-specific install.
  - **Permissions**: the GitHub API scopes granted to the app.
  - **Webhook events**: repository/org events delivered to the app.
  - **Operational owner**: human(s) responsible for reviewing permissions, incidents, and rotations.

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This index | `.github/apps/README.md` | Repo maintainers | Inventory + governance expectations |
| Per-app documentation | `.github/apps/<app-slug>/README.md` | App owner | Required for each installed integration |
| Security policy | `.github/SECURITY.md` | Security owners | Canonical security policy location (expected by KFM) |
| CI workflows | `.github/workflows/` | CI/CD owners | Where workflows call actions / use app tokens |
| System pipeline reference | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical pipeline + governance invariants |

### Definition of done
- [ ] Front-matter complete + valid
- [ ] Every installed app has a corresponding `.github/apps/<app-slug>/README.md`
- [ ] Each app doc includes: purpose, permissions, data handling, secrets mapping (names only), last review date
- [ ] No secrets committed to the repo
- [ ] Governance + CARE/sovereignty considerations explicitly stated when applicable
- [ ] Validation steps listed and repeatable

### If you are adding a new app
- Create a folder: `.github/apps/<app-slug>/`
- Add a per-app README (minimum fields listed below)
- Document requested permissions (and why each one is needed)
- Confirm where secrets are stored (secret names only; never values)
- Add/Update required status checks if the app participates in CI

---

## 🗂️ Directory Layout

### This document
- `path`: `.github/apps/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| GitHub Apps documentation | `.github/apps/` | This inventory and per-app docs |
| GitHub workflows | `.github/workflows/` | GitHub Actions workflows and status checks |
| Security | `.github/SECURITY.md` + `docs/security/` | Policy and technical standards (not confirmed in repo) |
| Governance | `docs/governance/` | Governance, ethics, sovereignty policies (not confirmed in repo) |
| System guide | `docs/MASTER_GUIDE_v12.md` | Canonical pipeline + invariants |

### Expected file tree for this sub-area
~~~text
📁 .github/
└── 📁 apps/
    ├── 📄 README.md
    ├── 📁 <app-slug>/
    │   ├── 📄 README.md
    │   ├── 📄 permissions.md
    │   ├── 📄 data-handling.md
    │   └── 📄 runbook.md
    └── 📄 APP_INVENTORY.yaml  (optional; see “Future extensions”)
~~~

---

## 🧭 Context

### Background
KFM has a governed pipeline with strong provenance and validation expectations. Repository automation (including GitHub Apps) can materially affect:
- CI/CD checks and merges
- Code scanning and security posture
- Generation of derived artifacts (data catalogs, documentation, reports)

This directory exists so integrations do not become “invisible infrastructure.”

### Assumptions
- Repositories use GitHub-native CI (Actions) and/or GitHub Apps for checks.
- Some integrations may be installed at the organization level and apply to multiple repos.

### Constraints / invariants
- **No secrets in-repo**: never commit private keys, tokens, webhook secrets, or credentials.
- **Least privilege**: permissions should be the minimum needed to accomplish the task.
- **No bypassing the KFM pipeline**: if an integration generates artifacts (data, catalogs, graphs, docs), it must respect the canonical pipeline ordering and placement rules (e.g., derived outputs in `data/processed/`, catalogs in `data/stac/`, lineage in `data/prov/`).
- **API boundary remains intact**: integrations must not introduce “UI reads graph directly” patterns; UI remains contract-driven via the API layer.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we maintain an explicit machine-readable inventory file (e.g., `APP_INVENTORY.yaml`)? | TBD | TBD |
| What is the required review cadence for app permissions (quarterly, semiannual)? | TBD | TBD |
| Do we require a “permissions diff” in PRs when an app’s scopes change? | TBD | TBD |

### Future extensions
- Add `APP_INVENTORY.yaml` and a CI check to ensure every installed app appears in the inventory (and vice versa).
- Add an automation to generate a per-app “permissions snapshot” from GitHub metadata for review.

---

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  Dev[Developer] -->|push / PR| GH[GitHub Repo]
  GH -->|webhook events| App[GitHub App or Integration]
  App -->|check runs / comments| GH
  GH -->|required checks| Merge[Merge gate]
  GH -->|workflow jobs| CI[GitHub Actions]
~~~

---

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| GitHub events | Webhook payloads | GitHub | Validate signatures (implementation-specific) |
| Repo contents | Git trees/blobs | GitHub API | Scope via permissions; restrict to needed paths |
| Secrets | GitHub Secrets | Repo/org secret store | Names documented here; values never stored here |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Check runs | GitHub Checks API | GitHub UI | Required checks configured in repo settings |
| PR comments | Markdown | PR timeline | Follow repo contribution norms |
| Artifacts | Files | GitHub Actions artifacts / releases | Must not leak sensitive data |

### Sensitivity & redaction
- If an integration posts content externally (PR comments, issues, job logs), it must avoid:
  - disclosing secrets
  - disclosing restricted locations or sensitive dataset details without governance approval
  - reproducing protected/PII content from datasets

### Quality signals
- Required checks pass on default branch
- App permissions reviewed and documented
- Any generated artifacts link to provenance/run outputs where applicable

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- If an integration generates or updates STAC outputs, it must:
  - write to `data/stac/` and preserve collection/item integrity
  - avoid “silent updates” without provenance references

### DCAT
- If an integration publishes or alters dataset catalog metadata:
  - it must update DCAT mappings in the canonical location (expected: `data/catalog/dcat/`)

### PROV-O
- If an integration triggers transformations that create derived artifacts:
  - record lineage (expected: `data/prov/`) so outputs can be traced to inputs and activities

### Versioning
- Generated outputs should follow documented versioning expectations and avoid unreviewed breaking changes.

---

## 🧱 Architecture

### Components
| Component | Responsibility | Notes |
|---|---|---|
| GitHub App | Receives events and performs repo actions | Scoped permissions; webhook-driven |
| GitHub Actions | Runs CI workflows | May use app tokens or GitHub-provided tokens |
| Repo settings | Required checks / branch protection | Must align with CI + app checks |
| Secrets store | Holds sensitive material | Never commit secrets into repo |

### Interfaces and contracts
| Interface | Contract | Where documented |
|---|---|---|
| App permissions | GitHub permission list | `.github/apps/<app-slug>/permissions.md` |
| App config | Config files or org settings | `.github/apps/<app-slug>/README.md` |
| CI gating | Required checks | `.github/workflows/` + repo settings |

### Per-app README minimum fields
For each app under `.github/apps/<app-slug>/README.md`, include:
- App name + vendor
- Installation scope (org/repo) and where to manage it
- Purpose and what workflows it supports
- Permissions list with rationale per permission
- Webhook events used
- Secrets required (names only) and rotation notes
- Data handling notes (what repo paths/data it reads)
- Incident runbook / contact
- Last reviewed date

---

## 🧠 Story Node & Focus Mode Integration

If an integration generates narrative artifacts (e.g., Story Nodes):
- every factual claim must be provenance-linked
- any predictive content must be clearly labeled and governed
- no unsourced narrative should be introduced into Focus Mode contexts

---

## 🧪 Validation & CI/CD

### Minimum CI gates
At a minimum, app-driven or app-impacted changes should not weaken these gates:
- Markdown protocol validation
- JSON schema validation (STAC/DCAT/telemetry)
- Graph integrity tests
- API contract tests
- UI layer registry schema checks
- Security + sovereignty scanning gates (where applicable)

### App change checklist
- [ ] Permissions reviewed for least privilege
- [ ] Branch protections and required checks updated as needed
- [ ] Secrets are referenced by name only (no values committed)
- [ ] Any generated artifacts have provenance/run references
- [ ] Documentation updated in `.github/apps/`

---

## ⚖ FAIR+CARE & Governance

### Governance review triggers
- Adding a new external integration (GitHub App, Marketplace app, bot)
- Expanding app permissions
- Apps that post derived or sensitive information into PRs/issues/logs
- Automation that affects public-facing endpoints or story outputs

### Sovereignty safety
- If an integration touches restricted locations or culturally sensitive materials:
  - document redaction/generalization rules
  - require explicit governance review before enabling automated publication

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial `.github/apps` README scaffold | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
