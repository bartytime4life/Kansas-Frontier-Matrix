<!--
GOVERNED ARTIFACT NOTICE
FILE: .github/README.md

This README is part of KFM’s governance “control plane.”
It defines REQUIRED GitHub settings + CI gate behavior for protected branches.

⚠️ Contract rule (fail-closed):
- Anything marked **REQUIRED (Enforced Today)** is a hard guarantee.
- If the repo cannot satisfy a REQUIRED item, that is a governance gap and MUST fail closed
  until the gap is remediated (or the contract is amended via governance review).

✅ Forward-motion rule (prevents “we’re moving backwards”):
- Do NOT label a capability as REQUIRED unless (a) it exists, and (b) it is enforceable by CI
  and/or GitHub settings today.
- Capabilities that are desired but not yet enforced belong in **PLANNED (Not Yet Enforced)**
  with an owner + tracking issue.

Change impact:
- Treat edits to this file as production changes.
- Meaning changes require governance review (CODEOWNERS + CI gates).
-->

# .github/ — KFM Governance Gatehouse (GitHub Operations + CI Enforcement)

![Governed Artifact](https://img.shields.io/badge/governed-artifact-critical)
![Fail Closed](https://img.shields.io/badge/policy-fail--closed-111827)
![Trust Membrane](https://img.shields.io/badge/trust%20membrane-contract%20only-6b7280)
![CI](https://img.shields.io/badge/CI-merge%20gates-success)
![Supply Chain](https://img.shields.io/badge/supply%20chain-planned-6b7280)
![Evidence](https://img.shields.io/badge/evidence-cite%20or%20abstain-critical)

> [!IMPORTANT]
> **What this file is:** the repo’s **governance gatehouse contract**.
>
> **What it prevents:** “paper governance” (docs that promise things CI doesn’t prove).
>
> **How to read it:** start with **Executive Gate Summary**, then **Required Today**, then **Contract-to-Gate Map**.

> [!CAUTION]
> **Reality-check rule:** if GitHub settings / required checks do **not** match this document,
> treat that mismatch as a **governance incident** and fail closed until corrected.

---

## Executive Gate Summary

### The promise we are making to leadership

We are not “adding process.” We are turning platform guarantees into **machine-enforced reality**:

- **Fail closed:** missing policy/proofs => deny promotion/merge/release by default.
- **Served truth is provable:** artifacts are servable only if backed by receipts + catalogs (planned gates).
- **User-facing claims are accountable:** Story Nodes and Focus Mode cite evidence or abstain (planned gates).

### The practical contract we enforce in GitHub (today)

1) Protected branches require PRs + CODEOWNERS reviews.  
2) Required checks are stable, predictable, and mapped to **job names**.  
3) Checks upload reviewable artifacts (machine + human).  
4) Promotion and release are blocked when proofs are missing (**once planned gates are wired**).

---

## Quick Links

**Repo governance surfaces**
- Root guarantees: `../README.md`
- CODEOWNERS: `./CODEOWNERS`
- Security policy: `./SECURITY.md`
- Workflows: `./workflows/`
- Dependabot: `./dependabot.yml` *(if dependencies exist)*

**Governed planes**
- Docs: `../docs/README.md`
- Data: `../data/README.md`
- Policy: `../policy/README.md`
- Backend: `../src/README.md`
- Web UI: `../web/README.md`
- Tests: `../tests/README.md`
- Releases: `../releases/README.md`

---

## Table of Contents

- [Governance Header](#governance-header)
- [Legend](#legend)
- [Definitions](#definitions)
- [Authority Ladder](#authority-ladder)
- [Non-Negotiable Invariants](#non-negotiable-invariants)
- [Governance Readiness Levels](#governance-readiness-levels)
- [Required Today](#required-today)
- [Planned Not Yet Enforced](#planned-not-yet-enforced)
- [Repo Settings Baseline](#repo-settings-baseline)
- [Verification](#verification)
- [Branch Protection Rules](#branch-protection-rules)
- [Required Status Checks](#required-status-checks)
- [Check Run Naming Contract](#check-run-naming-contract)
- [Workflow Inventory and Outputs](#workflow-inventory-and-outputs)
- [CI Artifact Contract](#ci-artifact-contract)
- [Contract-to-Gate Map](#contract-to-gate-map)
- [Promotion and Release Enforcement](#promotion-and-release-enforcement)
- [Workflow Security](#workflow-security)
- [Config Drift](#config-drift)
- [Governance Incidents and Break-Glass](#governance-incidents-and-break-glass)
- [Definition of Done](#definition-of-done)

---

## Governance Header

| Field | Value |
|---|---|
| Document | `.github/README.md` |
| Status | **Governed** (contract + enforcement surface) |
| Version | `v2.1.0` *(bump when meaning changes)* |
| Effective date | `2026-02-16` |
| Owners | defined in `.github/CODEOWNERS` |
| Review cadence | quarterly + out-of-band for security/toolchain changes |
| Applies to | workflows, branch protections, CODEOWNERS, templates, release gating |

> [!WARNING]
> If a **REQUIRED (Enforced Today)** item cannot be satisfied, we fail closed and treat it as a governance incident.

---

## Legend

| Marker | Meaning |
|---|---|
| ✅ | **REQUIRED (Enforced Today)** — must be provably in place |
| 🟡 | Recommended — valuable, but not a hard guarantee today |
| 🧪 | Planned — do **not** claim as enforced until wired + stable |

---

## Definitions

| Term | Meaning in KFM |
|---|---|
| **Guarantee** | A statement proven by GitHub settings + CI. If not proven, it’s not a guarantee. |
| **Gate** | A merge-blocking condition (status check +/or GitHub setting). |
| **Workflow** | A GitHub Actions YAML file. |
| **Check run name** | The **job name** that branch protection uses (not the workflow file name). |
| **Receipt** | A run record + checksums + spec hash proving how an artifact was created. |
| **Catalogs** | Machine-readable metadata (DCAT, STAC, PROV) linking outputs to provenance. |
| **Promotion** | Raw → Work → Processed transition, only allowed with proofs. |
| **Fail closed** | Missing inputs/proofs/validators => deny/abstain, never “best effort allow.” |

---

## Authority Ladder

If something conflicts, resolve in this order:

1) Repo guarantees (`../README.md` and this file)  
2) Fail-closed policy boundaries (default deny beats convenience)  
3) Contracts/schemas (`contracts/**` or `schemas/**`)  
4) Receipts + catalogs (`data/**` truth path artifacts)  
5) Workflows (`.github/workflows/**`) implement the contract (do not redefine it)  
6) Runbooks/docs (`docs/**`) clarify but do not weaken gates  

> [!NOTE]
> To relax an invariant: write an ADR, update contracts + tests, then update gates. Never weaken gates as a shortcut.

---

## Non-Negotiable Invariants

These are **system invariants**. If you find a path that violates them, you found a governance bug.

### 1) Trust membrane (contract-level; enforcement is planned)

- UI/external clients never access databases or object storage directly.
- All access is via governed API gateway + policy decision point.
- Core backend logic never bypasses repository interfaces to talk directly to storage.

### 2) Fail-closed policy (contract-level; enforcement is planned)

- Default deny at policy boundaries (CI + runtime).
- Missing policy inputs / missing receipts / missing catalogs / missing citations → deny/abstain.

### 3) Promotion Contract (contract-level; enforcement is planned)

- Raw → Work → Processed promotion requires:
  - receipts (run manifest / validation reports)
  - deterministic checksums
  - catalogs (DCAT always; STAC conditional; PROV required)
  - sensitivity classification + redaction provenance when relevant
- No contract → no publish.

### 4) Deterministic identity (contract-level; enforcement is planned)

- `spec_hash = sha256(JCS(spec))` (RFC 8785 canonical JSON).
- Receipts include `spec_schema_id` + `spec_recipe_version` where applicable.

### 5) Evidence-first claim surfaces (contract-level; enforcement is planned)

- Evidence references are resolvable (`prov://`, `stac://`, `dcat://`, `doc://`, `graph://`, optional `oci://`).
- Story Nodes + Focus Mode must cite or abstain and always return `audit_ref`.

### 6) Release immutability (contract-level; enforcement is planned)

- `releases/` is append-only. Never edit an existing release folder.

---

## Governance Readiness Levels

This prevents “moving backwards” by making **what’s enforced now** vs **what’s coming next** explicit.

| Level | Description | What is REQUIRED at this level |
|---|---|---|
| **L0 — Scaffold** | Repo protected + basic CI health | Branch protections + CODEOWNERS + `build/docs/contracts` |
| **L1 — Contract Core** | Schemas + policy are testable | `contracts` + `policy` + `docs` |
| **L2 — Truth Path** | Promotion proofs enforced | `receipts` + `catalogs` + `stories` |
| **L3 — Release Integrity** | Supply chain + drift controls | `supply-chain` + `config-drift` + tag protection |

> [!IMPORTANT]
> **Only the checks listed under “Required Today” are enforced today.**
> Everything else is **Planned** until wired and proven.

---

## Required Today

These are **merge-blocking** on protected branches.

### Required `.github/` inventory (enforced today)

| Path | Required | Purpose |
|---|---:|---|
| `.github/README.md` | ✅ | This governance + CI contract |
| `.github/CODEOWNERS` | ✅ | Review enforcement for governed paths |
| `.github/SECURITY.md` | ✅ | Vulnerability reporting + security expectations |
| `.github/workflows/` | ✅ | CI gatehouse |
| `.github/PULL_REQUEST_TEMPLATE.md` | 🟡 | PR evidence checklist |
| `.github/dependabot.yml` | 🟡 | Dependency updates (if dependencies exist) |
| `.github/ISSUE_TEMPLATE/` | 🟡 | Incidents and standard issues |

### Required status checks (enforced today)

| Check name (job name) | Intent | Fail-closed definition |
|---|---|---|
| `build` | repo health | build/lint/unit/smoke must pass |
| `docs` | doc correctness | markdown lint + link checks pass |
| `contracts` | schema validity | contract validation + fixtures pass |

> [!NOTE]
> If you rename any required check job, you must update branch protections and this document.

---

## Planned Not Yet Enforced

These are desired but not merge-blocking until wired into CI and branch protections.

| Check | Why it matters | Promotion to “Required” depends on |
|---|---|---|
| `policy` | default deny regression protection | policy test suite exists + stable job name |
| `receipts` | promotion proof integrity | receipt schema + validator + artifacts uploaded |
| `catalogs` | DCAT/STAC/PROV validity | validators + cross-link tests exist |
| `stories` | cite-or-abstain enforcement | story schema + citation resolver tests |
| `api-contract` | prevent breaking `/api/v1` | OpenAPI diff gate exists |
| `security` | SAST/SCA/secrets | CodeQL + dependency review configured |
| `config-drift` | repo settings integrity | read-only drift workflow exists |
| `supply-chain` | SBOM/attestations | release pipeline emits/verifies SBOM + provenance |

> [!WARNING]
> Do not claim guarantees tied to Planned gates until they are enforced.

---

## Repo Settings Baseline

These are GitHub settings (not files). If not configured, treat as a governance gap.

### Required settings (baseline)

- PRs required on protected branches (no direct pushes)
- Require CODEOWNERS reviews
- Require required status checks to pass (no bypass)
- Disallow force-push to protected branches
- Enable secret scanning + push protection (if available)
- Enable dependency graph + Dependabot alerts
- Enable code scanning on default branch (e.g., CodeQL)

### Recommended hardening (next)

- Require 2FA for org members
- Require signed commits + signed tags (when feasible)
- Require branches be up to date before merge
- Restrict bypass permissions to a minimal break-glass group
- Protect tags used for releases (e.g., `v*`)

---

## Verification

This is how maintainers prove the contract matches reality.

### Human verification (GitHub UI)

- Branch protection / ruleset exists for `main` (and `release/*` if used)
- Required status checks list contains exactly:
  - `build`
  - `docs`
  - `contracts`
- CODEOWNERS reviews are required and cannot be bypassed casually
- “Allow force pushes” is disabled for protected branches
- Secret scanning + push protection enabled (if available)
- Code scanning enabled + scheduled

### Machine verification (recommended; drift-safe)

> [!NOTE]
> These commands are examples for maintainers and drift tooling. They are not required for contributors.

Using GitHub CLI (requires appropriate permissions):

```bash
# Example placeholders:
#   OWNER=your-org
#   REPO=kansas-frontier-matrix
#   BRANCH=main

gh api repos/$OWNER/$REPO/branches/$BRANCH/protection

# Newer orgs may use repository rulesets; list them if available:
gh api repos/$OWNER/$REPO/rulesets
```

If the outputs do not align with **Required Today**, open a `governance-incident` issue and fail closed until corrected.

---

## Branch Protection Rules

### Required protection settings (for `main`)

- PRs required; no direct pushes
- CODEOWNERS reviews required
- Required status checks must pass (**no bypass**)
- No force push
- “Require branches to be up to date” (recommended)
- Signed commits/tags (recommended; enforce when org is ready)

> [!NOTE]
> GitHub may implement protections via “branch protection rules” or “repository rulesets.”
> Either is acceptable if it enforces the same guarantees.

---

## Required Status Checks

Branch protection references **check run names** (job names).

### Enforced today (must exist and run on every PR)

- `build`
- `docs`
- `contracts`

### Planned checks (do not enforce until wired)

- `policy`
- `receipts`
- `catalogs`
- `stories`
- `api-contract`
- `security`
- `config-drift`
- `supply-chain`

---

## Check Run Naming Contract

> [!IMPORTANT]
> Branch protection requires **job check run names**.
> For GitHub Actions, that’s effectively the job `name:` (or job ID if no name is set).

### Rules

- Every required check has a **single job** whose `name:` equals the check name.
- Prefer one required job per workflow to keep check names stable.
- If using reusable workflows, verify the resulting check names are still stable.

### Safe procedure for renaming a required check

1) Add the new job name **in parallel** (keep the old one)  
2) Update branch protection to require the new name  
3) Remove the old job name  
4) Update this document (and any docs referencing the gate map)

<details>
  <summary><strong>Minimal stable check skeleton</strong></summary>

```yaml
name: docs

on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read

jobs:
  docs:
    name: docs
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<PINNED_SHA>
      - run: make docs-lint
```
</details>

---

## Workflow Inventory and Outputs

> [!WARNING]
> The boss-level failure mode is “checks exist, but nobody knows what they prove.”
> This section makes the mapping explicit.

### Enforced-today workflows

| Workflow file | Workflow `name:` | Required job name | Purpose |
|---|---|---|---|
| `.github/workflows/build.yml` | `build` | `build` | build + unit tests + smoke |
| `.github/workflows/docs.yml` | `docs` | `docs` | markdown lint + link checks |
| `.github/workflows/contracts.yml` | `contracts` | `contracts` | schema validation + fixtures |

### Planned workflows

| Workflow file | Job name | When | Becomes required when |
|---|---|---|---|
| `policy.yml` | `policy` | PR + push | policy tests + default deny regressions exist |
| `receipts.yml` | `receipts` | PR + push | receipt validator exists + artifacts uploaded |
| `catalogs.yml` | `catalogs` | PR + push | DCAT/STAC/PROV validators exist |
| `stories.yml` | `stories` | PR + push | Story schema + citation resolution exists |
| `api-contract.yml` | `api-contract` | PR + push | OpenAPI diff gate exists |
| `security.yml` | `security` | schedule + PR | CodeQL/dep review configured |
| `config-drift.yml` | `config-drift` | schedule | drift inspection works read-only |
| `supply-chain.yml` | `supply-chain` | tag/release | SBOM/attestations produced/verified |

---

## CI Artifact Contract

CI must upload **reviewable proof**, not just pass/fail.

### Artifact expectations (for enforced-today gates)

| Gate | Must upload | Minimum structure |
|---|---|---|
| `docs` | lint + link reports | `reports/docs/report.json` + `reports/docs/report.md` |
| `contracts` | schema + compat output | `reports/contracts/report.json` + `reports/contracts/report.md` |
| `build` | unit + smoke logs | `reports/build/report.json` + `reports/build/report.md` |

### Standard artifact naming

- Artifact name: `kfm-ci-<gate>-reports`
- Inside artifact:
  - `reports/<gate>/report.json` *(machine)*
  - `reports/<gate>/report.md` *(human)*
  - optional raw logs under `reports/<gate>/logs/**`

### Step Summary requirement

Each gate writes a short `GITHUB_STEP_SUMMARY` that includes:
- what was checked,
- what artifacts were uploaded,
- top 3 failure hints (when failing).

---

## Contract-to-Gate Map

This makes it impossible to “feel” governed while not proving it.

| Repo guarantee | Proved by gates | Enforced at runtime by |
|---|---|---|
| Branches are protected | GitHub settings + CODEOWNERS | GitHub branch protection / rulesets |
| Docs are correct | `docs` | N/A (reduces claim drift) |
| Contracts are valid | `contracts` | API input validation + promotion rules |
| Trust membrane | 🧪 `security` + architecture tests | network policy + API gateway + authz |
| Fail-closed policy | 🧪 `policy` | PDP denies on missing inputs |
| Promotion proof required | 🧪 `receipts` + `catalogs` | deny serving artifacts lacking proofs |
| Cite-or-abstain | 🧪 `stories` + policy rules | response validator + evidence resolver |
| Immutable releases | 🧪 `supply-chain` + release checks | append-only release folder + checksum verify |

> [!IMPORTANT]
> If a guarantee has no proving gate, it is not a guarantee yet.

---

## Promotion and Release Enforcement

### Promotion contract (planned → must become enforced)

Rules for any PR that changes `data/processed/**` (once enabled):
- must include receipts/run manifests
- must include checksums
- must include catalogs (DCAT + PROV; STAC when spatial)
- missing proofs => fail closed

### Release immutability (planned → must become enforced)

- `releases/` is append-only
- each release folder includes:
  - checksums
  - catalog references
  - provenance/audit refs
  - optional SBOM + attestations
- editing an existing release folder is a governance incident

---

## Workflow Security

Applies to **all** workflows.

### Required rules

- Third-party actions pinned by **commit SHA**
- Least-privilege `permissions:` per workflow/job
- Fork-safe workflows (no secrets exposed to untrusted PRs)
- Avoid `pull_request_target` unless absolutely required
- Prefer GitHub-hosted runners for untrusted PRs

<details>
  <summary><strong>Permissions skeleton</strong></summary>

```yaml
permissions:
  contents: read

jobs:
  build:
    name: build
    permissions:
      contents: read
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<PINNED_SHA>
      - run: make test
```
</details>

---

## Config Drift

GitHub settings are governance infrastructure. Drift = governance break.

### Required (manual, quarterly)

Confirm:
- branch protections still exist and required checks match
- CODEOWNERS review still required and non-bypassable
- secret scanning + push protection enabled (if available)
- code scanning enabled and scheduled

### Planned (automated)

A `config-drift` workflow that:
- queries GitHub API (read-only) for branch protections/rulesets
- flags mismatch (fails and/or opens a labeled issue)
- never exposes secrets

---

## Governance Incidents and Break-Glass

> [!CAUTION]
> Governance incident = any change that weakens fail-closed behavior, trust membrane enforcement,
> provenance/citation guarantees, or release immutability.

### Break-glass rule

Break-glass is allowed **only for security containment**, not “ship faster.”

Minimum requirements:
- issue created with label `governance-incident`
- CODEOWNERS approval required (even expedited)
- post-incident follow-up:
  - restore missing gates
  - add regression tests proving bypass is closed
  - publish incident summary (internal ok)

---

## Definition of Done

This document is “done” when:

- [ ] Required Today inventory exists and is CODEOWNED
- [ ] Branch protections enforce PR + CODEOWNERS + Required Today checks
- [ ] Required Today check names are stable and map to job names
- [ ] Required Today gates upload reviewable proof artifacts
- [ ] Planned gates have owners + tracking issues + promotion criteria to Required
- [ ] Workflow security rules are applied (pinned actions + least privilege + fork-safe)
