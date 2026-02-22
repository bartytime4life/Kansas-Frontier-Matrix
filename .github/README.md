<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/7d8e0c8d-7c61-4b2a-8f9b-7f0a8c0a8e55
title: .github Governance and Automation Hub for Kansas Frontier Matrix
type: standard
version: v1
status: review
owners: kfm-governance,kfm-security,kfm-platform
created: 2026-02-22
updated: 2026-02-22
policy_label: public
related:
  - ../README.md
  - ../CONTRIBUTING.md
  - ../SECURITY.md
  - ../docs/
  - ../policy/
  - ../contracts/
tags:
  - kfm
  - governance
  - github
  - ci
notes:
  - This document describes target posture and recommended structure; reconcile filenames and required check names to repo reality.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# .github — Governance and Automation Hub for Kansas Frontier Matrix

**Purpose:** Turn governance intent into enforceable behavior at merge-time: **CI gates**, **CODEOWNERS**, **templates**, and **workflow security**.  
**Operating rule:** *If it can merge, it can ship. If it can ship, it must be governed.*

**Acronym:** Kansas Frontier Matrix = **KFM**  
**Status:** vNext (target conventions; align to repo reality)  
**Posture:** default-deny • fail-closed • reproducible by digest • policy enforced in CI + runtime  
**Scope:** This directory governs how changes enter KFM — treat changes here as **production**.  
**Owners:** enforced via **CODEOWNERS** (see below)

**Signal row:** `status:vNext` • `governance:fail-closed` • `policy:default-deny` • `evidence:cite-or-abstain` • `security:least-privilege`

**Jump links:**  
[Main README](../README.md) • [Contributing](../CONTRIBUTING.md) • [Security](../SECURITY.md) • [Docs](../docs/) • [Policy](../policy/) • [Contracts](../contracts/)

---

## Quick navigation

- [Why this folder matters](#why-this-folder-matters)
- [What lives in `.github/`](#what-lives-in-github)
- [PR to CI to merge governance flow](#pr-to-ci-to-merge-governance-flow)
- [CI gates mapped to the Promotion Contract](#ci-gates-mapped-to-the-promotion-contract)
- [Required check naming contract](#required-check-naming-contract)
- [Workflow catalog](#workflow-catalog)
- [Branch protection and rulesets posture](#branch-protection-and-rulesets-posture)
- [CODEOWNERS required reviewers](#codeowners-required-reviewers)
- [Issue templates](#issue-templates)
- [PR template](#pr-template)
- [Workflow security guardrails](#workflow-security-guardrails)
- [Adding or changing a gate](#adding-or-changing-a-gate)
- [Definition of Done for `.github/` changes](#definition-of-done-for-github-changes)

---

## Why this folder matters

KFM’s trust membrane starts **before runtime** — in the merge process.  
If CI allows a change that violates policy, evidence resolvability, or deterministic identity, the platform can no longer claim *map-first + evidence-first + cite-or-abstain* integrity.

> **Governance-critical rule:** anything that changes enforcement (**workflows**, **CODEOWNERS**, **contracts**, **policy**, **validators**, **CI-required check names**) is production configuration.  
> Treat `.github/` edits as high-risk changes.

[↑ Back to top](#top)

---

## What lives in `.github/`

> **NOTE**  
> The exact files present may vary by branch. This README describes **target structure + expectations**.  
> If any item below is missing, treat it as an **integration gap** rather than silently relaxing enforcement.

### Target directory tree

~~~text
.github/
  README.md                         # This file (governance map)
  CODEOWNERS                        # Required reviewers for protected paths
  PULL_REQUEST_TEMPLATE.md          # PR checklist and governance prompts
  ISSUE_TEMPLATE/                   # Issue forms/templates (intake that is governance-aware)
  workflows/                        # CI gates and automation (privileged code)
  actions/                          # Composite actions (optional; treat as critical code)
  dependabot.yml                    # Dependency automation (optional; controlled cadence)
  labeler.yml                       # PR auto-labeling (optional; routing + dashboards)
  release-drafter.yml               # Draft release notes (optional)
~~~

### Core contents

| Path | Purpose | Governance risk | Expected controls |
|---|---|---:|---|
| `.github/workflows/` | CI gates and automation | **High** | Required reviews + required status checks |
| `.github/actions/` | Composite actions | **High** | Same review rigor as application code; pin dependencies |
| `.github/CODEOWNERS` | Mandatory reviewers for protected paths | **High** | Steward/operator ownership + least-privilege |
| `.github/ISSUE_TEMPLATE/` | Structured intake | Medium | Template owners + required fields |
| `.github/PULL_REQUEST_TEMPLATE.md` | PR checklist | Medium | Codeowner review recommended |
| `.github/README.md` | This file | Low | Keep current; treat as governed documentation |

### Recommended additions

| File/Dir | Why it helps | Notes |
|---|---|---|
| `.github/dependabot.yml` | Automated dependency PRs with controlled cadence | Pair with CODEOWNERS + required checks |
| `.github/actions/` | Composite Actions to reduce workflow drift | Version/pin dependencies; add tests where feasible |
| `.github/labeler.yml` | Auto-label PRs (policy/contracts/data/UI) | Enables routing + dashboards |
| `.github/release-drafter.yml` | Draft release notes from merged PRs | Optional early; valuable later |
| `.github/FUNDING.yml` | Sponsorship links | Optional |

[↑ Back to top](#top)

---

## PR to CI to merge governance flow

~~~mermaid
flowchart LR
  A[Contributor opens PR] --> B[CI: lint typecheck unit tests]
  B --> C[CI: policy tests catalog validators linkcheck]
  C --> D[CI: evidence contract and resolvability tests]
  D --> E[CI: supply chain and security checks]
  E --> F[CODEOWNERS reviews required]
  F --> G[Merge allowed only if all required checks pass]
  G --> H[Optional: release and publish automation]
~~~

**KFM posture:** failures **block**.  
**Waivers:** if waivers are allowed at all, they are governed artifacts: explicit, time-bounded, and recorded.

[↑ Back to top](#top)

---

## CI gates mapped to the Promotion Contract

KFM’s Promotion Contract defines what must be true before anything becomes user-visible. GitHub workflows enforce the **merge-time** portion of those gates.

### Gate mapping

| Promotion gate | What must be true | CI check concept |
|---|---|---|
| **A — Identity and versioning** | deterministic `spec_hash`; drift prevented | spec-hash job + golden tests |
| **B — Licensing and rights** | rights metadata required; “metadata-only” allowed when mirroring is prohibited | schema validation + rights lint |
| **C — Sensitivity and redaction plan** | `policy_label` assigned; obligations testable; leakage prevented | policy tests + leakage scans |
| **D — Catalog triplet validation** | DCAT/STAC/PROV validate under profiles | validators per profile |
| **E — Run receipts and checksums** | digests + environment capture | receipt schema validation + artifact digest checks |
| **F — Policy and contract tests** | policy fixtures pass; API/evidence contracts pass | policy tests + OpenAPI tests + evidence tests |
| **G — Operational readiness** | SBOM/provenance + smoke checks | security scans + optional e2e smoke |

> **Fail-closed behavior:** if any required check fails, the PR must not merge.

[↑ Back to top](#top)

---

## Required check naming contract

Branch protection and rulesets rely on **stable check names**. Accidental renames are a common “governance break” because GitHub treats renamed checks as “missing” required checks.

### Rules

- **Do not rename** workflow names or job names that are required checks without a coordinated protection update.
- Prefer **always-on workflows** that “no-op quickly” over `paths-ignore` that prevents a required check from appearing.
- Keep required checks **few, stable, and meaningful**; expand coverage within those checks via matrix jobs if needed.

### Recommended check name registry

> **NOTE**  
> Replace names below with your repo’s actual workflow/job names. The point is to keep them stable once protected.

| Required check name | What it covers | Owned by |
|---|---|---|
| `CI / lint` | formatting + lint | platform |
| `CI / test` | unit tests | platform |
| `Policy / tests` | policy fixtures + allow/deny outcomes | policy + stewards |
| `Contracts / validate` | schema + API lint/validate | platform |
| `Catalog / validate` | DCAT/STAC/PROV profile validation | data stewards |
| `Evidence / resolvability` | linkcheck + evidence bundle tests | platform + stewards |
| `Security / baseline` | dependency audit + SAST baseline | security |

[↑ Back to top](#top)

---

## Workflow catalog

> **NOTE**  
> Filenames below are **recommended**. If your repo uses different names, keep the semantics but update names and links.

### Recommended workflow set

| Workflow | Trigger | Minimum jobs | Why it exists |
|---|---|---|---|
| `ci.yml` | `pull_request` | lint, typecheck, unit tests | fast feedback, blocks broken merges |
| `policy.yml` | `pull_request` (paths: `policy/**`) | policy tests + fixtures | policy semantics must match CI + runtime |
| `contracts.yml` | `pull_request` (paths: `contracts/**`) | schema validation + API lint | contracts are runtime boundaries |
| `catalog-validate.yml` | `pull_request` (paths: `data/catalog/**`) | DCAT/STAC/PROV validators | prevents metadata drift |
| `evidence.yml` | `pull_request` | linkcheck + evidence resolvability | makes citations resolvable |
| `security.yml` | scheduled + `pull_request` | dependency audit + SAST baseline | shift-left security posture |
| `focus-eval.yml` | scheduled + `workflow_dispatch` | golden queries + abstention tests | prevents Focus regressions |

### Reusable workflows

If you anticipate multiple pipelines or repos, prefer reusable workflow patterns:

- `.github/workflows/_reusable/validate-contracts.yml`
- `.github/workflows/_reusable/policy-tests.yml`

Then call them from thin “entry” workflows. This keeps governance logic centralized and reviewable.

[↑ Back to top](#top)

---

## Branch protection and rulesets posture

> **PROPOSED**  
> Align to your organization’s GitHub branch protection or rulesets. Treat these as governance policy.

Minimum recommended protection for `main` (and any `release/*` branches):

- Require **status checks** (required checks above) to pass before merging
- Require **CODEOWNERS review**
- Require PRs (no direct pushes)
- Require conversation resolution
- Restrict who can dismiss reviews
- Protect high-risk paths (`.github/**`, `policy/**`, `contracts/**`, `infra/**`) with stricter review requirements
- Stabilize required check names (branch protection depends on them)
- Choose and document merge method (squash or merge commit) to preserve auditability

[↑ Back to top](#top)

---

## CODEOWNERS required reviewers

`CODEOWNERS` is how KFM enforces “the right eyes on the right files.”

> **PROPOSED intent**  
> Replace `<TEAM>` placeholders with real GitHub teams.

| Path pattern | Why it’s protected | Typical owners |
|---|---|---|
| `.github/workflows/**` | CI gate logic = governance | `@<DEVOPS_TEAM>` + `@<SECURITY_TEAM>` |
| `.github/actions/**` | privileged automation building blocks | `@<DEVOPS_TEAM>` + `@<SECURITY_TEAM>` |
| `policy/**` | default-deny semantics + obligations | `@<POLICY_TEAM>` + `@<STEWARD_TEAM>` |
| `contracts/**` | API + schema boundaries | `@<PLATFORM_TEAM>` |
| `data/registry/**` | registries affect promotion eligibility | `@<DATA_STEWARDS>` |
| `infra/**` | deployment + runtime posture | `@<DEVOPS_TEAM>` |
| `apps/api/**` | enforcement point | `@<PLATFORM_TEAM>` |
| `apps/ui/**` | evidence-first UX trust surface | `@<UI_TEAM>` + `@<STEWARD_TEAM>` |

[↑ Back to top](#top)

---

## Issue templates

Issue templates are how KFM avoids “governance by tribal memory.”

Recommended templates (names may vary):

- **Dataset onboarding**: requires source registry entry, rights snapshot, sensitivity classification, intended cadence.
- **Policy change**: requires rationale, fixture updates, and expected allow/deny outcomes.
- **Story publish request**: requires Story Node ID, citations resolvable, rights for embedded media, review triggers.
- **Bug report**: requires reproduction steps + environment + dataset_version_id (if relevant).
- **Security report**: points to `SECURITY.md` process.

> **Rule:** if an issue changes what becomes user-visible, it must reference evidence and versions (or explicitly state why it cannot yet).

[↑ Back to top](#top)

---

## PR template

The PR template should make governance “the default path,” not a special burden.

Minimum checklist concepts:

- no secrets
- contracts updated when shapes change
- policy tests updated when enforcement changes
- catalogs validated when publishing or metadata changes
- evidence resolvability tests present for new citations
- Focus eval run for model or prompt changes when applicable

If the current PR template doesn’t cover these, update it.

[↑ Back to top](#top)

---

## Workflow security guardrails

Workflows are privileged code. Treat them accordingly.

### Baseline hygiene

- Prefer `pull_request` workflows for untrusted contributions.
- Avoid `pull_request_target` unless you deeply understand the risk model and restrict what the workflow does.
- Pin third-party actions to a **commit SHA** when practical.
- Scope workflow permissions to least privilege:

~~~yaml
# In a workflow file (example)
permissions:
  contents: read
  pull-requests: read
  # add write scopes only if needed
~~~

- Prefer ephemeral auth (OIDC) over long-lived cloud secrets when available.
- Keep secrets out of PR contexts, especially forks.
- Treat artifact uploads as official build outputs; caches are for speed, not provenance.
- Use `timeout-minutes` and `concurrency` to limit resource abuse and runaway jobs.
- Prefer pinned runner images (e.g., `ubuntu-24.04`) over floating labels when determinism matters.

### Common foot-guns to avoid

- Checking out PR code in a job with write permissions or secrets.
- Using `pull_request_target` to run arbitrary PR code.
- Running untrusted code in composite actions that have elevated permissions by default.
- Renaming required checks without updating branch protections or rulesets.

[↑ Back to top](#top)

---

## Adding or changing a gate

When you add a new CI gate, you’re changing KFM’s enforcement behavior.

Procedure:

1. Document the intent (link to an ADR if architectural).
2. Add the deterministic tool or validator (prefer `tools/`).
3. Add fixtures + golden tests.
4. Add a workflow job that runs the validator.
5. Update the **required check naming contract** and branch protections or rulesets.
6. Update this `.github/README.md` and the main `README.md` if contributor behavior changes.

Fail-closed principle: if the gate cannot run reliably, it should block (or be explicitly waived with governance approval).

[↑ Back to top](#top)

---

## Definition of Done for `.github/` changes

Use this checklist when changing workflows, templates, owners, or required checks.

- [ ] Change is reversible (rollback plan or simple revert)
- [ ] Workflow permissions are least-privileged
- [ ] No secrets added or exposed in logs
- [ ] No unsafe trigger patterns introduced (fork safety preserved)
- [ ] Third-party actions are pinned where practical
- [ ] Required checks list is updated and check names remain stable
- [ ] CODEOWNERS coverage is correct for protected paths
- [ ] Templates enforce KFM evidence and version requirements where applicable
- [ ] Documentation updated (this file + any referenced runbooks)
- [ ] Changes tested via PR (expected checks appear and are required)

---

## Where to learn more

- Main system contract: `../README.md`
- Governance docs: `../docs/governance/`
- Policy-as-code: `../policy/`
- Contracts: `../contracts/`

> Reminder: In KFM, documentation that changes enforcement is production.

[↑ Back to top](#top)
