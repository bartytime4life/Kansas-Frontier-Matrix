---
title: "KFM GitHub Action — Security Scan"
path: ".github/actions/security-scan/README.md"
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

doc_uuid: "urn:kfm:doc:github-actions:security-scan:readme:v1.0.0"
semantic_document_id: "kfm-github-actions-security-scan-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:security-scan:readme:v1.0.0"
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

# KFM GitHub Action — Security Scan

## 📘 Overview

### Purpose

- Document the **local GitHub Action** in this directory (`.github/actions/security-scan/`) and how to use it as a **CI gate**.
- Capture the action’s **high-level contract** (what it is responsible for, how it is invoked, and what “pass/fail” means), without duplicating the source-of-truth in `action.yml`.

### Scope

| In Scope | Out of Scope |
|---|---|
| How to invoke this action from workflows <br/> What categories of checks it enforces (security + sovereignty) <br/> Expected failure behavior (CI gate / branch protection) <br/> Redaction rules for scan outputs <br/> Governance expectations for changes to this action | Detailed implementation docs for each underlying scanner tool <br/> Organization-wide security policy text (belongs in `.github/SECURITY.md` + `docs/security/`) <br/> Incident response procedures |

### Audience

- **Primary:** KFM repo maintainers and CI/CD owners (workflow + branch protection maintainers).
- **Secondary:** Contributors adding data/code/docs who need to understand required CI gates.

### Definitions

- Link: `docs/glossary.md`
- Terms used in this doc include: **CI gate**, **secret scanning**, **dependency vulnerability scanning**, **sovereignty rules**, **restricted locations**, **redaction/generalization**, **artifact hygiene**.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Security Scan Action (this) | `.github/actions/security-scan/` | CI/CD Maintainers | Reusable action invoked by workflows |
| Action definition | `.github/actions/security-scan/action.yml` | CI/CD Maintainers | **Source of truth** for inputs/outputs/runtime behavior |
| Workflows (call sites) | `.github/workflows/*.yml` | CI/CD Maintainers | Where this action is invoked (PR/push/release) |
| Security policy + standards | `.github/SECURITY.md` + `docs/security/` | Security Owners | Canonical policy location; keep action aligned |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | Governance Council | Rules that may require additional checks/redaction |
| Ethics policy | `docs/governance/ETHICS.md` | Governance Council | AI + narrative constraints (if relevant to scan scope) |

### Definition of done

- [ ] Front-matter complete + valid
- [ ] README matches `action.yml` inputs/outputs and behavior (no drift)
- [ ] Validation steps listed and repeatable (CI + local where possible)
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Output handling avoids leaking secrets or restricted coordinates

## 🗂️ Directory Layout

### This document

- `path`: `.github/actions/security-scan/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub local actions | `.github/actions/` | Reusable, repo-local actions (composite or JS actions) |
| Security scan action | `.github/actions/security-scan/` | This action’s definition + supporting scripts/assets |
| GitHub workflows | `.github/workflows/` | CI pipelines that call this action |
| Security policy | `.github/SECURITY.md` | Security policy entry point |
| Security documentation | `docs/security/` | Detailed security standards, threat model notes, SOPs |
| Governance policies | `docs/governance/` | FAIR/CARE, ethics, sovereignty policies |
| Telemetry docs | `docs/telemetry/` | Documented metrics/events (if emitted) |
| Telemetry schemas | `schemas/telemetry/` | JSON schemas for telemetry event payloads |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 security-scan/
        ├── 📄 README.md
        ├── 📄 action.yml
        └── 📁 scripts/   (optional; only if the action needs helper scripts)
~~~

## 🧭 Context

### Background

KFM uses CI gates to ensure repository changes remain trustworthy and compliant. Security-focused gates include:
- **Dependency vulnerability scanning**
- **Secret/PII leakage prevention** (including checks that outputs don’t inadvertently contain secrets or personal data)
- **Sovereignty-rule compliance checks** (e.g., ensuring restricted locations are generalized/redacted in outputs)

This action is intended to provide a single reusable place to implement that gate and keep workflows consistent.

### Assumptions

- This action is invoked from GitHub workflows (PR + push) and participates in branch protection checks.
- The action may need access to generated artifacts (e.g., `data/processed/`, `data/stac/`, build outputs) depending on the workflow.

### Constraints / invariants

- **Least privilege:** workflows should grant only the minimum permissions required for the chosen scanners and reporting.
- **No sensitive leakage:** do not print raw findings that include secrets/PII/restricted coordinates to public logs.
- **Sovereignty-aware outputs:** if a dataset or output is labeled restricted, the action must treat it according to `docs/governance/SOVEREIGNTY.md` (redaction/generalization rules).
- **Architecture boundary stays intact:** UI does not read Neo4j directly; contracts remain at the API layer. (This action must not introduce backdoor data flows.)
- **Deterministic and reproducible:** scans should be stable and produce consistent results given the same inputs and pinned tool versions.

### Open questions

| Question | Why it matters | Owner | Status |
|---|---|---|---|
| Which scanners are used (deps, secrets, code, data-output checks)? | Determines tool configuration, permissions, runtime | CI/CD Maintainers | TBD |
| Do we publish SARIF (GitHub Code Scanning) or artifacts? | Affects permissions + data leakage risk | Security Owners | TBD |
| What are the failing thresholds (severity, allowlists, suppression policy)? | Defines consistent “pass/fail” | Security Owners | TBD |
| What exact “sovereignty compliance checks” are implemented? | Ensures restricted location handling is enforced | Governance Council | TBD |
| Where are redaction/generalization rules encoded? | Prevents accidental leaks | Governance Council | TBD |

### Future extensions

- Add optional reporting outputs (e.g., SARIF) *only if* redaction and permissions are correct.
- Add domain-aware checks that validate restricted datasets are generalized prior to publication.
- Add a “policy profile” input to support different enforcement modes (e.g., `pr` vs `release`), if needed.

## 🖼️ Diagrams

### CI gate placement

~~~mermaid
flowchart LR
  Dev[Contributor PR / Push] --> CI[GitHub Workflow Job]
  CI --> Action[security-scan action]
  Action --> Findings[Findings / Reports]
  Findings --> Gate{Pass?}
  Gate -- yes --> Merge[Merge / Release eligible]
  Gate -- no --> Block[Block merge + require remediation]
~~~

### Typical invocation sequence

~~~mermaid
sequenceDiagram
  participant Dev as Contributor
  participant GH as GitHub Actions
  participant SS as security-scan action
  participant BP as Branch Protection

  Dev->>GH: Open PR / Push commit
  GH->>SS: Run security scan job step
  SS-->>GH: Exit 0 (pass) or non-zero (fail)
  GH-->>BP: Report check status
  BP-->>Dev: Allow merge (pass) / Block merge (fail)
~~~

## 📦 Data & Metadata

### Inputs

> Source of truth: `.github/actions/security-scan/action.yml`  
> Keep this table synced with the `inputs:` section there.

| Input | Format | Required? | Default | Description |
|---|---|---|---|---|
| (sync from `action.yml`) | — | — | — | Copy the action’s defined inputs here |

### Outputs

> Source of truth: `.github/actions/security-scan/action.yml`  
> Keep this table synced with the `outputs:` section there (if any).

| Output | Format | Description |
|---|---|---|
| (sync from `action.yml`) | — | Copy the action’s defined outputs here |

### Sensitivity & redaction

- Treat scan results as **potentially sensitive**:
  - Secret findings should be **redacted** in logs.
  - Data-output checks that touch restricted datasets should **not** emit raw restricted coordinates.
- Prefer:
  - Minimal summaries in logs (counts + severity)
  - Artifacts stored with appropriate access controls (when applicable)

### Quality signals

- The CI job provides a clear, deterministic **pass/fail**.
- Findings are categorized (at least: dependency, secret/PII, sovereignty policy).
- Output is consistent across runs (tool versions pinned, stable config).

## 🌐 STAC, DCAT & PROV Alignment

This action does **not** produce STAC/DCAT/PROV by itself, but it may:

- Validate that generated outputs **do not violate** sovereignty/security rules (e.g., restricted coordinate leakage).
- Run as part of the broader CI gate set that also validates STAC/DCAT/PROV schemas.

### Versioning

- This README uses **semver** (`version:` in front-matter).
- The action versioning strategy should be documented in `action.yml` and/or workflow pinning conventions (local action path vs ref).

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| GitHub workflow job | Orchestrates CI, supplies checkout/build outputs | `.github/workflows/*.yml` |
| `security-scan` action | Runs configured security + sovereignty checks | `.github/actions/security-scan/action.yml` |
| Scanner toolchain | Performs actual scanning (deps/secrets/data-output) | Implementation detail (must be documented) |
| Policies + standards | Define what is allowed/prohibited | `.github/SECURITY.md`, `docs/security/`, governance docs |
| Branch protection | Enforces gate before merge/release | GitHub settings + required checks |

### Contracts & interfaces

- **Action contract:** `action.yml` defines:
  - inputs / outputs
  - required permissions (if any)
  - expected runtime behavior
- **Policy contract:** `.github/SECURITY.md` + `docs/security/` define:
  - security expectations
  - allowed tools / disallowed behaviors (e.g., prohibited outbound calls)
- **Sovereignty contract:** `docs/governance/SOVEREIGNTY.md` defines:
  - restricted data handling rules (generalization/redaction)

### Extension points (checklist)

- [ ] Add/replace a scanner tool (document the change + rationale)
- [ ] Add a new policy rule (document and link to governance decision)
- [ ] Add “release mode” stricter enforcement (document thresholds + permissions)
- [ ] Add artifact publishing (document redaction + retention + access)

## 🧠 Story Node & Focus Mode Integration

This action does not generate Story Nodes directly. It supports Focus Mode quality by preventing:
- Secret/PII leakage into published artifacts or data exports
- Restricted location leakage (sovereignty violations) into public-facing outputs

If your workflow builds narrative artifacts (e.g., story node drafts), include them in the scan scope and apply the same redaction rules.

## 🧪 Validation & CI/CD

### Validation steps

- Run in CI via a workflow that invokes this action.
- Confirm the action:
  - Fails when a **known canary secret pattern** is introduced (use *dummy test strings only*; never real secrets).
  - Fails when restricted outputs violate sovereignty rules (using a controlled test fixture).
  - Passes when findings are remediated or legitimately allowlisted per policy.

### Reproduction

- CI is the primary execution environment.
- Local reproduction depends on the scanner toolchain selected by the action.
  - If local reproduction is required, document the exact commands here once toolchain is confirmed.

### Telemetry signals (if applicable)

| Signal | Source | Where recorded | Schema |
|---|---|---|---|
| TBD | GitHub Actions | `docs/telemetry/` | `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates

Changes to this action can affect repository safety and sovereignty compliance. Treat the following as governance-sensitive:
- Changing scan coverage (what is/ isn’t scanned)
- Changing thresholds (what blocks merges)
- Changing redaction behavior (what is logged or uploaded)

### CARE / sovereignty considerations

- Ensure sovereignty-labeled datasets and restricted locations are handled according to:
  - `docs/governance/SOVEREIGNTY.md`
- Default stance: **generalize/redact** for public outputs unless policy explicitly allows detail.

### AI usage constraints

- Ensure the doc’s `ai_transform_permissions` and `ai_transform_prohibited` remain aligned with intended use.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README scaffold for the security-scan action | TBD |

---

Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Security policy: `.github/SECURITY.md` and `docs/security/`
