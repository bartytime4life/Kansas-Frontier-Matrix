# .github — Governance and Automation Hub for Kansas Frontier Matrix
> **If it can merge, it can ship. If it can ship, it must be governed.**  
> This folder is where KFM turns governance intent into enforceable behavior: **CI gates**, **CODEOWNERS**, **issue + PR templates**, and **security guardrails**.

**Acronym:** Kansas Frontier Matrix = **KFM**  
**Status:** vNext (target conventions; align to repo reality)  
**Posture:** default-deny • fail-closed • reproducible by digest • policy enforced in CI + runtime  
**Scope:** This directory governs how changes enter KFM—treat changes here as **production**.  
**Owners:** enforced via **CODEOWNERS** (see below)

[![Status](https://img.shields.io/badge/status-vNext-blue)](#)
[![Governance](https://img.shields.io/badge/governance-fail--closed-critical)](#)
[![Policy](https://img.shields.io/badge/policy-default--deny-critical)](#)
[![Evidence](https://img.shields.io/badge/evidence-cite--or--abstain-important)](#)
[![Security](https://img.shields.io/badge/security-CODEOWNERS%20%2B%20CI%20gates-important)](#)

**Jump links:**  
[Main README](../README.md) • [Contributing](../CONTRIBUTING.md) • [Security](../SECURITY.md) • [Docs](../docs/) • [Policy](../policy/) • [Contracts](../contracts/)

---

## Quick navigation
- [Why this folder matters](#why-this-folder-matters)
- [What lives in `.github/`](#what-lives-in-github)
- [PR → CI → Merge: the governance flow](#pr--ci--merge-the-governance-flow)
- [CI gates: Promotion Contract to GitHub Actions](#ci-gates-promotion-contract-to-github-actions)
- [Workflow catalog](#workflow-catalog)
- [Branch protection posture](#branch-protection-posture)
- [CODEOWNERS: required reviewers for high-risk changes](#codeowners-required-reviewers-for-high-risk-changes)
- [Issue templates](#issue-templates)
- [PR template](#pr-template)
- [Security guardrails for workflows](#security-guardrails-for-workflows)
- [Adding or changing a gate](#adding-or-changing-a-gate)
- [Definition of Done for `.github/` changes](#definition-of-done-for-github-changes)

---

## Why this folder matters

KFM’s trust membrane starts **before runtime**—in the merge process.  
If CI allows a change that violates policy, evidence resolvability, or deterministic identity, the platform can no longer claim *map-first + cite-or-abstain* integrity.

> **Rule:** anything that changes enforcement (**workflows**, **CODEOWNERS**, **contracts**, **policy**, **validators**) is governance-critical.  
> Treat `.github/` edits like production configuration changes.

[↑ Back to top](#github--governance-and-automation-hub-for-kansas-frontier-matrix)

---

## What lives in `.github/`

> **NOTE**  
> The exact files present may vary by branch. This README describes **target** structure + expectations.

### Core contents

| Path | Purpose | Governance risk | Expected controls |
|---|---|---:|---|
| `.github/workflows/` | CI gates and automation | **High** | Required reviews + required status checks |
| `.github/ISSUE_TEMPLATE/` | Structured intake (datasets/policy/stories/bugs) | Medium | Template owners |
| `.github/PULL_REQUEST_TEMPLATE.md` | PR checklist (governance-aware) | Medium | Codeowner review recommended |
| `.github/CODEOWNERS` | Mandatory reviewers for protected paths | **High** | Steward/operator ownership |
| `.github/README.md` | This file: how GitHub governance works | Low | Keep current |

### Recommended additions

These are common “missing pieces” that make governance scalable:

| File/Dir | Why it helps | Notes |
|---|---|---|
| `.github/dependabot.yml` | Automated dependency PRs with controlled cadence | Pair with CODEOWNERS + required checks |
| `.github/actions/` | Composite Actions to avoid duplicated workflow logic | Pin versions; treat as critical code |
| `.github/labeler.yml` (or similar) | Auto-label PRs (policy/contracts/data/UI) | Enables routing + dashboards |
| `.github/release-drafter.yml` | Draft release notes from merged PRs | Optional early, valuable later |
| `.github/FUNDING.yml` | Sponsorship links | Optional |

[↑ Back to top](#github--governance-and-automation-hub-for-kansas-frontier-matrix)

---

## PR → CI → Merge: the governance flow

~~~mermaid
flowchart LR
  A[Contributor opens PR] --> B[CI: lint + tests + contract validation]
  B --> C[CI: policy tests + catalog validators + linkcheck]
  C --> D[CI: evidence resolver contract tests]
  D --> E[Optional: Focus eval + UI e2e smoke]
  E --> F[CODEOWNERS review required]
  F --> G[Merge allowed only if all required checks pass]
  G --> H[Release/publish automation (if configured)]
~~~

**KFM posture:** failures **block**. Waivers (if allowed) are governed artifacts and must be explicit, time-bounded, and recorded.

[↑ Back to top](#github--governance-and-automation-hub-for-kansas-frontier-matrix)

---

## CI gates: Promotion Contract to GitHub Actions

KFM’s Promotion Contract defines what must be true before anything becomes user-visible. GitHub workflows should enforce the **merge-time** portion of those gates.

### Gate mapping

| Promotion gate | What must be true | CI check (recommended) |
|---|---|---|
| **A — Identity & versioning** | `spec_hash` deterministic; drift prevented | `spec-hash` job + golden tests |
| **B — Licensing & rights** | rights metadata required; “metadata-only” allowed when mirroring is prohibited | schema validation + rights lint |
| **C — Sensitivity & redaction plan** | policy_label assigned; obligations testable; leakage prevented | policy tests + leakage scans |
| **D — Catalog triplet validation** | DCAT/STAC/PROV validate under profiles | validators for each profile |
| **E — Run receipts & checksums** | digests + environment capture | receipt schema validation + artifact digest checks |
| **F — Policy + contract tests** | policy fixtures pass; API/evidence contracts pass | OPA tests + OpenAPI tests + evidence tests |
| **G — Operational readiness** | SBOM/provenance + smoke checks | optional security scans + e2e smoke |

> **Fail-closed behavior:** if any required check fails, the PR must not merge.

[↑ Back to top](#github--governance-and-automation-hub-for-kansas-frontier-matrix)

---

## Workflow catalog

> **NOTE**  
> Filenames below are **recommended**. If your repo uses different names, keep the semantics but update names and links.

### Recommended workflow set

| Workflow | Trigger | Minimum jobs (suggested) | Why it exists |
|---|---|---|---|
| `ci.yml` | `pull_request` | lint, typecheck, unit tests | fast feedback, blocks broken merges |
| `policy.yml` | `pull_request` (paths: `policy/**`) | OPA/Rego tests + fixtures | policy semantics must match CI + runtime |
| `contracts.yml` | `pull_request` (paths: `contracts/**`) | schema validation + OpenAPI lint | contracts are runtime boundaries |
| `catalog-validate.yml` | `pull_request` (paths: `data/catalog/**`) | DCAT/STAC/PROV validators | prevents silent metadata drift |
| `linkcheck.yml` | `pull_request` | cross-link + EvidenceRef resolvability | makes citations real |
| `evidence-contract.yml` | `pull_request` | evidence resolver contract tests | ensures cite-or-abstain is enforceable |
| `focus-eval.yml` *(optional early)* | scheduled + `workflow_dispatch` | golden queries + abstention tests | prevents regressions in Focus Mode |
| `security.yml` *(recommended)* | scheduled + `pull_request` | dep audit, SAST, container scan | shift-left security posture |

### Reusable workflows

If you anticipate multiple pipelines or repos, prefer a reusable workflow pattern:

- `.github/workflows/_reusable/validate-contracts.yml`
- `.github/workflows/_reusable/policy-tests.yml`

…and call them from thin “entry” workflows. This keeps governance logic centralized and reviewable.

[↑ Back to top](#github--governance-and-automation-hub-for-kansas-frontier-matrix)

---

## Branch protection posture

> **PROPOSED** (align to your org’s rulesets)

Minimum recommended branch protection for `main` (and any `release/*` branches):

- Require **status checks** (CI) to pass before merging
- Require **CODEOWNERS review**
- Require PRs (no direct pushes)
- Require conversation resolution
- Restrict who can dismiss reviews
- Protect `.github/**`, `policy/**`, `contracts/**`, `infra/**` with stricter reviewers
- Stabilize required check names (branch protection depends on them)
- Prefer merge methods that preserve auditability (squash or merge commit—choose and document)

[↑ Back to top](#github--governance-and-automation-hub-for-kansas-frontier-matrix)

---

## CODEOWNERS: required reviewers for high-risk changes

`CODEOWNERS` is how KFM enforces “the right eyes on the right files.”

> **PROPOSED CODEOWNERS intent (examples)**  
> Replace `<TEAM>` placeholders with real GitHub teams.

| Path pattern | Why it’s protected | Typical owners |
|---|---|---|
| `.github/workflows/**` | CI gate logic = governance | `@<DEVOPS_TEAM>` + `@<SECURITY_TEAM>` |
| `policy/**` | default-deny semantics + obligations | `@<POLICY_TEAM>` + `@<STEWARD_TEAM>` |
| `contracts/**` | API + schema boundaries | `@<PLATFORM_TEAM>` |
| `data/registry/**` | source/dataset/layer registries affect what can be promoted | `@<DATA_STEWARDS>` |
| `infra/**` | deployment + runtime posture | `@<DEVOPS_TEAM>` |
| `apps/api/**` | policy enforcement point | `@<PLATFORM_TEAM>` |
| `apps/ui/**` | evidence-first UX trust surface | `@<UI_TEAM>` + `@<STEWARD_TEAM>` |

[↑ Back to top](#github--governance-and-automation-hub-for-kansas-frontier-matrix)

---

## Issue templates

Issue templates are how KFM avoids “governance by tribal memory.”

Recommended templates (names may vary):

- **Dataset onboarding**: requires source registry entry, rights snapshot, sensitivity classification, and intended cadence.
- **Policy change**: requires rationale, fixture updates, and “expected allow/deny outcomes.”
- **Story publish request**: requires Story Node ID, citations resolvable, rights for embedded media, and review triggers.
- **Bug report**: requires steps to reproduce + environment + dataset_version_id (if relevant).
- **Security report**: points to `SECURITY.md` process.

> **Rule:** if an issue changes what becomes user-visible, it must reference evidence/versions (or explicitly state why it cannot yet).

[↑ Back to top](#github--governance-and-automation-hub-for-kansas-frontier-matrix)

---

## PR template

The PR template should make governance “the default path,” not a special burden.

Minimum checklist concepts:

- no secrets
- contracts updated when shapes change
- policy tests updated when enforcement changes
- catalogs validated when publishing/metadata changes
- evidence resolvability tests present for new citations
- Focus eval run for model/prompt changes (when applicable)

If the current PR template doesn’t cover these, update it.

[↑ Back to top](#github--governance-and-automation-hub-for-kansas-frontier-matrix)

---

## Security guardrails for workflows

**Workflows are privileged code.** Treat them accordingly.

### Recommended GitHub Actions hygiene

- Prefer `pull_request` workflows for untrusted contributions.
- Avoid `pull_request_target` unless you deeply understand the risk model and restrict what the workflow does.
- Pin third-party actions to a commit SHA when practical.
- Scope workflow permissions to least privilege:

~~~yaml
# In a workflow file (example)
permissions:
  contents: read
  pull-requests: read
  # add write scopes only if needed
~~~

- Keep secrets out of PR contexts (especially forks).  
- Treat artifact uploads as official build outputs; caches are for speed, not provenance.

[↑ Back to top](#github--governance-and-automation-hub-for-kansas-frontier-matrix)

---

## Adding or changing a gate

When you add a new CI gate, you’re changing KFM’s enforcement behavior.

**Procedure (recommended):**
1. Document the intent (link to an ADR if architectural).
2. Add the deterministic tool/validator (prefer `tools/`).
3. Add fixtures + golden tests.
4. Add a workflow job that runs the validator.
5. Add/adjust branch protection required checks.
6. Update this `.github/README.md` and the main `README.md` if the gate affects contributors.

**Fail-closed principle:** if the gate cannot run reliably, it should block (or be explicitly waived with governance approval).

[↑ Back to top](#github--governance-and-automation-hub-for-kansas-frontier-matrix)

---

## Definition of Done for `.github/` changes

Use this checklist when changing workflows/templates/owners.

- [ ] Change is reversible (rollback plan or simple revert)
- [ ] Workflow permissions are least-privileged
- [ ] No secrets added or exposed in logs
- [ ] Required checks list is updated (if needed)
- [ ] CODEOWNERS coverage is correct for protected paths
- [ ] Templates enforce KFM’s evidence/version requirements (where applicable)
- [ ] Documentation updated (this file + any referenced runbooks)
- [ ] Changes tested (dry-run or PR verification)

---

### Where to learn more

- Main system contract: `../README.md`
- Governance docs: `../docs/governance/`
- Policy-as-code: `../policy/`
- Contracts: `../contracts/`

> **Reminder:** In KFM, documentation that changes enforcement is **production**.

[↑ Back to top](#github--governance-and-automation-hub-for-kansas-frontier-matrix)
