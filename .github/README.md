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
![Trust Membrane](https://img.shields.io/badge/trust%20membrane-enforced-important)
![CI](https://img.shields.io/badge/CI-merge%20gates-success)
![Rulesets](https://img.shields.io/badge/GitHub-rulesets%20%7C%20branch%20protection-334155)
![Supply Chain](https://img.shields.io/badge/supply%20chain-pinned%20actions%20%7C%20sbom-6b7280)
![Evidence](https://img.shields.io/badge/evidence-cite%20or%20abstain-critical)

> [!IMPORTANT]
> **What this file is:** the repo’s **governance gatehouse contract**.
>
> **What it prevents:** “paper governance” (docs that promise things CI doesn’t prove).
>
> **How to read it:** start with **Executive Gate Summary**, then **Required Today**, then **Contract-to-Gate Map**.

---

## Executive Gate Summary

### The promise we are making to leadership

We are not “adding process.” We are **turning our platform guarantees into machine-enforced reality**:

- **No bypass:** UI/external clients never access DB/object storage directly (trust membrane).
- **Fail closed:** if policy/proofs are missing, KFM denies promotion/serving by default.
- **Served truth is provable:** processed artifacts are only servable if backed by receipts + catalogs.
- **User-facing claims are accountable:** Story Nodes and Focus Mode cite evidence or abstain, and emit an audit reference.

### The practical contract we enforce in GitHub

1) Protected branches require PRs + CODEOWNERS reviews.  
2) Required checks are stable, predictable, and mapped to job names.  
3) Checks upload reviewable artifacts (machine + human) so reviewers can verify.  
4) Promotion and release are blocked when proofs are missing.

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

## Directory Snapshot

This file is the **front door** to the repo’s enforcement surfaces.

```text
.github/
├─ README.md                  # this contract (governed)
├─ CODEOWNERS                 # path-based review enforcement (governed)
├─ SECURITY.md                # vuln reporting + expectations
├─ workflows/                 # CI gates (governed when referenced by branch protections/rulesets)
├─ PULL_REQUEST_TEMPLATE.md   # evidence checklist (recommended → may become required)
├─ dependabot.yml             # dependency update config (recommended; required if deps exist)
└─ ISSUE_TEMPLATE/            # incident + standard issues (recommended)
```

> [!NOTE]
> If a path is referenced as REQUIRED in this contract, it must exist **and** be enforced by GitHub settings and/or CI today.

---

## Table of Contents

- [Governance Header](#governance-header)
- [Change Log](#change-log)
- [Definitions](#definitions)
- [Authority Ladder](#authority-ladder)
- [Non-Negotiable Invariants](#non-negotiable-invariants)
- [Governance Readiness Levels](#governance-readiness-levels)
- [Required Today](#required-today)
- [Planned Not Yet Enforced](#planned-not-yet-enforced)
- [Repo Settings Baseline](#repo-settings-baseline)
- [Rulesets and Branch Protection](#rulesets-and-branch-protection)
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
| Applies to | workflows, rulesets/branch protections, CODEOWNERS, templates, release gating |

> [!WARNING]
> If a **REQUIRED (Enforced Today)** item cannot be satisfied, we fail closed and treat it as a governance incident.

---

## Change Log

### v2.1.0 — 2026-02-16

- Clarified **Rulesets vs Branch Protection** and how they layer.
- Added required-check reliability notes (merge queue, workflow skips, path filters).
- Strengthened the check-name stability contract (unique job names, wrapper jobs for matrices).
- Improved maintainability (directory snapshot, less duplication).

---

## Definitions

| Term | Meaning in KFM |
|---|---|
| **Guarantee** | A statement proven by GitHub settings + CI. If not proven, it’s not a guarantee. |
| **Gate** | A merge-blocking condition (status check +/or GitHub setting). |
| **Workflow** | A GitHub Actions YAML file. |
| **Check run name** | The name GitHub uses as a merge requirement for Actions checks (must be stable). |
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

### 1) Trust membrane

- UI/external clients never access databases or object storage directly.
- All access is via governed API gateway + policy decision point.
- Core backend logic never bypasses repository interfaces to talk directly to storage.

### 2) Fail-closed policy

- Default deny at policy boundaries (CI + runtime).
- Missing policy inputs / missing receipts / missing catalogs / missing citations → deny/abstain.

### 3) Promotion Contract

- Raw → Work → Processed promotion requires:
  - receipts (run manifest / validation reports)
  - deterministic checksums
  - catalogs (DCAT always; STAC conditional; PROV required)
  - sensitivity classification + redaction provenance when relevant
- No contract → no publish.

### 4) Deterministic identity

- `spec_hash = sha256(JCS(spec))` (RFC 8785 canonical JSON).
- Receipts include `spec_schema_id` + `spec_recipe_version` where applicable.

### 5) Evidence-first claim surfaces

- Evidence references are resolvable (`prov://`, `stac://`, `dcat://`, `doc://`, `graph://`, optional `oci://`).
- Story Nodes + Focus Mode must cite or abstain and always return `audit_ref`.

### 6) Release immutability

- `releases/` is append-only. Never edit an existing release folder.

---

## Governance Readiness Levels

This prevents “moving backwards” by making **what’s enforced now** vs **what’s coming next** explicit.

| Level | Description | What is REQUIRED at this level |
|---|---|---|
| **L0 — Scaffold** | Repo protected + basic CI health | Branch protections/rulesets + CODEOWNERS + `build` |
| **L1 — Contract Core** | Schemas + docs are testable | `contracts` + `docs` |
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
| `.github/PULL_REQUEST_TEMPLATE.md` | ⛳ | PR evidence checklist (recommended) |
| `.github/dependabot.yml` | ⛳ | Dependency updates (recommended) |
| `.github/ISSUE_TEMPLATE/` | ⛳ | Incidents and standard issues (recommended) |

### Required status checks (enforced today)

| Check name (stable) | Intent | Fail-closed definition |
|---|---|---|
| `build` | repo health | build/lint/unit/smoke must pass |
| `docs` | doc correctness | markdown lint + link checks pass |
| `contracts` | schemas | contract validation + fixtures pass |

> [!IMPORTANT]
> If you rename any required check name, you must:
> 1) update the workflow job name(s),  
> 2) update rulesets/branch protection required checks, and  
> 3) update this document in the same PR.

---

## Planned Not Yet Enforced

These are **desired** but **not merge-blocking today** until wired into CI and rulesets/branch protections.

> [!WARNING]
> Do not claim guarantees tied to Planned gates until they are enforced.

### Planned gates registry

| Check | Why it matters | Target readiness | Owner | Tracking issue | Promotion to “Required” depends on |
|---|---|---|---|---|---|
| `policy` | default deny regression protection | L2 | TBD | TBD | OPA/conftest suite exists + stable check name |
| `receipts` | promotion proof integrity | L2 | TBD | TBD | receipt schema + validator + artifacts uploaded |
| `catalogs` | DCAT/STAC/PROV validity | L2 | TBD | TBD | validators + cross-link tests exist |
| `stories` | cite-or-abstain enforcement | L2 | TBD | TBD | story schema + citation resolver tests |
| `api-contract` | prevent breaking `/api/v1` | L1–L2 | TBD | TBD | OpenAPI diff gate exists |
| `security` | SAST/SCA/secrets | L3 | TBD | TBD | CodeQL + dependency review configured |
| `config-drift` | repo settings integrity | L3 | TBD | TBD | read-only drift workflow exists |
| `supply-chain` | SBOM/attestations | L3 | TBD | TBD | release pipeline emits/verifies SBOM + provenance |

> [!NOTE]
> “TBD” means “not confirmed in repo.” Planned gates **must** be assigned before being promoted to Required.

---

## Repo Settings Baseline

These are GitHub settings (not files). If not configured, treat as a governance gap.

### REQUIRED (baseline)

- PRs required on protected branches (no direct pushes)
- Require CODEOWNERS reviews
- Require required status checks to pass (no bypass)
- Disallow force-push to protected branches
- Enable secret scanning + push protection (if available in org/plan)
- Enable dependency graph + Dependabot alerts (if dependencies exist)

### RECOMMENDED hardening (next)

- Require conversation resolution before merge
- Require branches be up to date before merge (**or** use merge queue)
- Require signed commits (and signed tags for releases, when feasible)
- Require linear history (squash/rebase only) when audit strategy prefers
- Restrict bypass permissions to a minimal break-glass group
- Protect release tags (e.g., `v*`) and/or use rulesets for tag protections

<details>
  <summary><strong>Maintainer verification checklist</strong></summary>

- [ ] A ruleset or branch protection exists for `main` (and `release/*` if used)
- [ ] Required status checks list matches “Required Today”
- [ ] CODEOWNERS review is required and bypass is restricted
- [ ] Secret scanning / push protection enabled (where available)
- [ ] Dependency graph/alerts enabled (where dependencies exist)
- [ ] Merge method policy is explicit and consistent with audit needs

</details>

---

## Rulesets and Branch Protection

GitHub now supports **rulesets** that can govern branches and tags and layer with existing protections.

### What KFM expects

- **Preferred enforcement surface:** rulesets (when available)  
- **Allowed enforcement surface:** branch protection rules (when rulesets are unavailable or legacy-managed)

> [!IMPORTANT]
> Rulesets can layer (multiple can apply) and are visible to readers, which helps auditing.  
> Branch protection rules can be harder to reason about when patterns overlap.

### KFM rule layering policy

If both exist, **the most restrictive outcome wins**:
- If one rule requires 2 reviews and another requires 3, KFM treats it as **3**.
- If one rule allows bypass and another forbids it, KFM treats it as **no bypass**.

---

## Required Status Checks

Branch protections/rulesets reference **stable check names**.

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

### Reliability rules for required checks (critical)

> [!CAUTION]
> Required checks that “sometimes don’t run” become an accidental denial of service (PRs stuck in pending).

1) **Do not use workflow-level path filters** (`paths` / `paths-ignore`) on workflows containing required checks.  
2) If you must conditionally skip expensive work, keep the *required check job* always reporting a result:
   - Use a wrapper/summary job with `needs:` and `if: always()` to emit a stable success/failure.  
3) If you enable **merge queue**, required-check workflows must also trigger on `merge_group`.

---

## Check Run Naming Contract

> [!IMPORTANT]
> Required checks must have **stable names** and be **unique across workflows**.

### Rules

- Every required check has a **single job** whose `name:` equals the check name (`build`, `docs`, `contracts`).
- **Job names must be unique across all workflows** (avoid “duplicate” check names that cause ambiguity).
- Avoid matrix jobs as required checks. If you need a matrix:
  - Use matrix jobs for coverage, but add **one** final “gate” job with a stable name that depends on them.
- If you use reusable workflows, verify the resulting check names are stable.

<details>
  <summary><strong>Minimal stable check skeleton</strong></summary>

```yaml
name: docs

on:
  pull_request:
  # Include this if using merge queue:
  # merge_group:
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

<details>
  <summary><strong>Matrix pattern with a single required “gate” job</strong></summary>

```yaml
name: build

on:
  pull_request:
  # merge_group:
  push:
    branches: [main]

permissions:
  contents: read

jobs:
  test-matrix:
    name: test-matrix
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node: [18, 20]
    steps:
      - uses: actions/checkout@<PINNED_SHA>
      - run: make test

  build:
    name: build
    needs: [test-matrix]
    if: ${{ always() }}
    runs-on: ubuntu-latest
    steps:
      - run: |
          echo "Matrix completed."
          # Optionally fail if any needs failed:
          # (GitHub exposes needs.*.result in expressions in more advanced patterns)
```
</details>

---

## Workflow Inventory and Outputs

> [!WARNING]
> The failure mode is “checks exist, but nobody knows what they prove.”
> This section makes the mapping explicit.

### Enforced-today workflows

| Workflow file | Workflow `name:` | Required job name | Required events | Purpose |
|---|---|---|---|---|
| `.github/workflows/build.yml` | `build` | `build` | `pull_request` (+ `merge_group` if merge queue) | build + unit tests + smoke |
| `.github/workflows/docs.yml` | `docs` | `docs` | `pull_request` (+ `merge_group` if merge queue) | markdown lint + link checks |
| `.github/workflows/contracts.yml` | `contracts` | `contracts` | `pull_request` (+ `merge_group` if merge queue) | schema validation + fixtures |

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
| Branches are protected | GitHub settings + CODEOWNERS | rulesets/branch protection |
| Docs are correct | `docs` | N/A (reduces UI/claim drift) |
| Contracts are valid | `contracts` | API input validation + promotion rules |
| Trust membrane | *(planned)* `security` + architecture tests | network policy + API gateway + authz |
| Fail-closed policy | *(planned)* `policy` | PDP denies on missing inputs |
| Promotion proof required | *(planned)* `receipts` + `catalogs` | deny serving artifacts lacking proofs |
| Cite-or-abstain | *(planned)* `stories` + policy rules | response validator + evidence resolver |
| Immutable releases | *(planned)* `supply-chain` + release checks | append-only release folder + checksum verify |

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

### REQUIRED rules

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

### REQUIRED (manual, quarterly)

Confirm:
- rulesets/branch protections still exist and required checks match
- CODEOWNERS review still required and non-bypassable
- secret scanning + push protection enabled (if available)
- dependency graph/alerts enabled (if dependencies exist)

### PLANNED (automated)

A `config-drift` workflow that:
- queries GitHub API (read-only) for rulesets/branch protections
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
- [ ] Rulesets/branch protections enforce PR + CODEOWNERS + Required Today checks
- [ ] Required Today check names are stable and unique across workflows
- [ ] Required Today gates upload reviewable proof artifacts
- [ ] Planned gates have owners + tracking issues + promotion criteria to Required
- [ ] Workflow security rules are applied (pinned actions + least privilege + fork-safe)

---
