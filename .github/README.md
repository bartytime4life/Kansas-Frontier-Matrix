<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/3c0d5c1f-14d4-4b4f-9b2b-9bc3d5c1c7b0
title: .github/README — GitHub Governance & Community Files
type: standard
version: v3
status: draft
owners: kfm-engineering; kfm-governance
created: 2026-02-22
updated: 2026-02-27
policy_label: restricted
related:
  - kfm://doc/kfm-definitive-design-governance-guide-vnext
  - ../README.md
  - ../CONTRIBUTING.md
  - ../SECURITY.md
  - ../CODE_OF_CONDUCT.md
  - ./CONTRIBUTING.md
  - ./SECURITY.md
  - ./CODE_OF_CONDUCT.md
tags:
  - kfm
  - github
  - governance
notes:
  - Badge row uses Shields.io (static) until repo identifiers are wired for dynamic badges.
  - This README is the GitHub-side “trust membrane”: templates + workflows + required checks registry.
  - Promotion Contract gates map to required checks; implement an “always-runs” gate-summary job to prevent skips.
  - This document references a target posture; do not claim a workflow/job/check exists until confirmed on your branch.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KFM GitHub Operations
Map-first • time-aware • governed delivery — **community files + CI/policy gate index**

**Status:** Draft (v3) • **Owners:** KFM Engineering + Governance  
**Core posture:** default-deny • fail-closed • reproducible by digest • policy enforced in CI + runtime

![status](https://img.shields.io/badge/status-draft-blue)
![policy](https://img.shields.io/badge/policy-restricted-orange)
![trust-membrane](https://img.shields.io/badge/trust%20membrane-merge--time%20gates-critical)
![promotion](https://img.shields.io/badge/promotion-contract%20enforced-critical)
![evidence-first](https://img.shields.io/badge/evidence--first-required-6f42c1)
![cite-or-abstain](https://img.shields.io/badge/cite--or--abstain-enforced-6f42c1)
![ci](https://img.shields.io/badge/CI-gates%20required-informational)
![security](https://img.shields.io/badge/security-default--deny-critical)
![repo](https://img.shields.io/badge/repo-wiring%20pending-lightgrey)

[Quick start](#quick-start) •
[Scope](#scope) •
[Directory contract](#directory-contract) •
[Truth discipline](#truth-discipline) •
[Reality check](#reality-check) •
[Wiring checklist](#wiring-checklist) •
[Folder map](#folder-map) •
[Machine-readable registries](#machine-readable-registries) •
[Required GitHub settings](#required-github-settings) •
[Workflow inventory](#workflow-inventory) •
[Promotion Contract mapping](#promotion-contract-mapping) •
[Required checks registry](#required-checks-registry) •
[CI and promotion gates](#ci-and-promotion-gates) •
[Issue and PR templates](#issue-and-pr-templates) •
[Governance and policy](#governance-and-policy) •
[Security](#security-and-responsible-disclosure) •
[Contacts](#contacts-and-owners) •
[Definition of Done](#definition-of-done)

---

## Quick start

- **Filing an issue:** use the templates in `.github/ISSUE_TEMPLATE/` (bug, feature, governance, data/pipeline, story node).
- **Opening a PR:** follow `CONTRIBUTING.md`, keep changes small, and include evidence (links, citations, artifact hashes).
- **Changing data/policy behavior:** expect CI to **fail-closed** until promotion/metadata/policy gates pass.

> [!IMPORTANT]
> **Policy labels are KFM metadata, not GitHub ACLs.**  
> Nothing in `.github/` should contain secrets, private keys, or restricted coordinates—even if `policy_label` is `restricted`.

> [!NOTE]
> This README is an **index + contract** for the GitHub-side “trust membrane” (workflows, templates, and guardrails).  
> If a link 404s, treat the linked artifact as **missing** (and therefore **merge-blocking** if it’s required by contract).

[Back to top](#top)

---

## Scope

**This README *is*:**
- an index of the repo’s **community health files** (CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, templates)
- an index of **governance & promotion gates** enforced by CI
- a **registry of required status checks** branch protection / rulesets should enforce

**This README is *not*:**
- product documentation (see repo root `README.md` and `/docs`)
- policy source-of-truth (see `/policy` and governance docs referenced by MetaBlock)

> [!WARNING]
> Do not “fix” failing gates by weakening them. Fix the underlying metadata, provenance, tests, redaction/generalization, or rights.

[Back to top](#top)

---

## Directory contract

This section makes `.github/` behave like a governed module.

### Where it fits

`.github/` is the repo’s **merge-time trust membrane**: it defines what GitHub enforces (templates, CODEOWNERS routing, required checks, and CI gates).

### Acceptable inputs

- Community health files (`CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, optional `SUPPORT.md`)
- Issue forms and PR templates (YAML/Markdown)
- CI workflows and shared composite actions used by workflows
- CODEOWNERS rules that route governance-critical changes

### Exclusions

- **Secrets** or credentials (never store in-repo)
- Operational runbooks and product docs that belong in `/docs`
- Dataset specs, catalogs, or policy bundles (those belong in their governed folders and are referenced from CI)

[Back to top](#top)

---

## Truth discipline

KFM docs use three tags. Apply them here too.

- **CONFIRMED** — backed by branch artifacts (files exist, workflows emit named checks, validators run).
- **PROPOSED** — a recommended default / template / build plan.
- **UNKNOWN** — needs verification; treat as **fail-closed** until confirmed.

> [!TIP]
> GitHub governance docs should aggressively label assumptions. It prevents “green builds” built on fantasy.

[Back to top](#top)

---

## Reality check

This README contains **placeholders** until the repo is wired (org/repo names, default branch, and *actual* emitted check names).

Before enforcing anything:
1. Confirm whether your org uses **repo rulesets** or **classic branch protection** (or both).
2. Confirm the workflows and jobs exist under `.github/workflows/`.
3. Open a PR and copy exact status check names from the PR **Checks** UI.

> [!IMPORTANT]
> **No invention rule:** do not claim specific workflow files, job names, or submodules exist until verified on the active branch.
> Keep unknowns as “TBD” and block merges rather than weakening gates.

### Minimum verification steps (do these once per branch)

```bash
# Capture branch + commit for audit trail
git rev-parse --abbrev-ref HEAD
git rev-parse HEAD

# Capture a shallow directory map (adjust depth as needed)
find . -maxdepth 3 -type d | sort

# Inspect GitHub workflows
ls -la .github/workflows
```

[Back to top](#top)

---

## Wiring checklist

Fill these in **once**, then convert badges + branch protection from placeholders → reality.

| Wiring item | Where it is used | Current value | Target value |
|---|---|---|---|
| Org | Dynamic badges, links | `<ORG>` | TODO |
| Repo | Dynamic badges, links | `<REPO>` | TODO |
| Default branch | Dynamic badges, rulesets | `<DEFAULT_BRANCH>` | TODO |
| Ruleset / protection name | Admin UI + audit trail | `<RULESET_NAME>` | TODO |
| Deployment environments | GitHub Environments (optional) | `<ENVIRONMENTS>` | TODO |
| Workflow filenames | Required check mapping | `ci.yml`, `policy-gates.yml`, `provenance-audit.yml`, `release.yml` | TODO |
| Required check names | Branch protection / rulesets | placeholders below | TODO |
| Required checks registry file | Keeps names stable + reviewable | `.github/required-checks.v1.json` | TODO |

> [!TIP]
> The safest way to fill in **Required check names** is to open a PR and copy exact names from the PR **Checks** UI.
> Don’t guess—GitHub check names vary with workflow/job names and reusable workflow wrappers.

[Back to top](#top)

---

## Folder map

Recommended (minimum) structure for `.github/`:

```text
.github/                                           # Repo governance + CI (gatehouse)
├─ README.md                                       # This file: governance/CI index + where to start
├─ CODEOWNERS                                      # REQUIRED: ownership + review routing
│
├─ CODE_OF_CONDUCT.md                              # Recommended: community standards
├─ CONTRIBUTING.md                                 # Recommended: contribution workflow + gates
├─ SECURITY.md                                     # Recommended: vuln reporting and disclosure
│
├─ SUPPORT.md                                      # Optional: where/how to get help (channels, office hours, links)
├─ dependabot.yml                                  # Optional: dependency update policy (governed if enabled)
├─ FUNDING.yml                                     # Optional
│
├─ required-checks.v1.json                         # PROPOSED: machine-readable required checks registry
│
├─ PULL_REQUEST_TEMPLATE.md                        # Optional: single default PR template
├─ PULL_REQUEST_TEMPLATE/                          # Optional: multiple PR templates (?template=... URL param)
│  ├─ default.md                                   # General PR checklist
│  ├─ governance.md                                # Governance/policy-impact PR checklist
│  └─ data-pipeline.md                             # Data/pipeline promotion PR checklist
│
├─ ISSUE_TEMPLATE/                                 # Recommended: issue forms (triage + governance discipline)
│  ├─ config.yml                                   # Template chooser (contact_links + blank_issues_enabled)
│  ├─ bug_report.yml
│  ├─ feature_request.yml
│  ├─ governance_request.yml
│  ├─ data_pipeline_change.yml
│  └─ story_node.yml
│
├─ actions/                                        # Optional: shared composite actions used by workflows
│  ├─ setup-conftest/action.yml                    # PROPOSED: install Conftest for policy gates
│  ├─ setup-opa/action.yml                         # PROPOSED: install OPA for policy evaluation
│  ├─ setup-node/action.yml                        # Optional: standardize Node toolchain
│  └─ setup-python/action.yml                      # Optional: standardize Python toolchain
│
└─ workflows/                                      # REQUIRED: CI + policy gates + release/promotion
   ├─ ci.yml                                       # Core CI (lint, unit tests, build, docs linkcheck)
   ├─ policy-gates.yml                             # Policy checks (labels, redaction, story claim hygiene)
   ├─ provenance-audit.yml                         # Promotion eligibility: receipts/manifests/checksums
   ├─ gates.yml                                    # PROPOSED: always-runs gate summary job (anti-skip)
   ├─ supply-chain.yml                             # Optional: SBOM + signing/attestations
   ├─ codeql.yml                                   # Optional: code scanning / SAST
   ├─ dependency-review.yml                        # Optional: dependency diff gate
   └─ release.yml                                  # Release/promotion orchestration (tags, packaging, publish)
```

> [!NOTE]
> GitHub also supports org-wide default community health files via a dedicated `.github` repository.
> If your org uses defaults, per-repo files should override intentionally (and be reviewed as governance-critical).

### Community health file location policy (avoid duplication)

GitHub recognizes some community files in:
- repo root (`/CONTRIBUTING.md`, `/SECURITY.md`, `/CODE_OF_CONDUCT.md`)
- `.github/` (`/.github/CONTRIBUTING.md`, etc.)
- `docs/` (varies by file)

> [!PROPOSED]
> Pick **one** canonical location per file (root *or* `.github/`) and avoid drift (duplicate copies).
> If you keep canonical files at repo root, this `.github/README.md` should link to `../CONTRIBUTING.md`, etc.

### Required files checklist

| File | Why it exists | Minimum expectation |
|---|---|---|
| `CODEOWNERS` | Routes required reviews (governance, data, policy) | Patterns cover governance + data promotion paths |
| `CONTRIBUTING.md` | Contributor workflow + guardrails | Explains PR expectations + how gates work |
| `CODE_OF_CONDUCT.md` | Community standards | Publicly readable; includes enforcement scope |
| `SECURITY.md` | Responsible disclosure | Private reporting path; “don’t post exploits in issues” |
| `.github/workflows/*` | Automated gates | Emits stable, required check names |

### CODEOWNERS expectations

`CODEOWNERS` is the router for required reviews. Minimum expectation:

- governance-sensitive files route to **kfm-governance**
- build/runtime code routes to **kfm-engineering**
- data promotion artifacts route to **both** (default-deny if unclear)

Example (replace with repo-real paths):

```text
# Global default
* @kfm-engineering

# Governance & trust membrane
.github/** @kfm-engineering @kfm-governance
/docs/governance/** @kfm-governance
/policy/** @kfm-governance
/contracts/** @kfm-governance @kfm-engineering

# Data + promotion surfaces (example)
data/** @kfm-engineering @kfm-governance
tools/** @kfm-engineering @kfm-governance
infra/** @kfm-engineering @kfm-governance
```

> [!TIP]
> Keep CODEOWNERS patterns boring. Prefer directories over fragile filename rules.

[Back to top](#top)

---

## Machine-readable registries

Humans forget; CI doesn’t. Prefer small registries that can be validated.

### Required checks registry (PROPOSED)

Store the canonical required checks set in a machine-readable file:

- `.github/required-checks.v1.json` (or `.github/required-checks.v1.json`)

Example template:

```json
{
  "kfm_required_checks_version": "v1",
  "default_branch": "<DEFAULT_BRANCH>",
  "ruleset_name": "<RULESET_NAME>",
  "required_checks": [
    {
      "gate": "gate_summary",
      "check_name": "gates / gate-summary",
      "source_workflow": ".github/workflows/gates.yml",
      "notes": "Always-runs anti-skip gate aggregator."
    }
  ],
  "gate_mapping": [
    { "gate": "A", "label": "identity-versioning" },
    { "gate": "B", "label": "rights-licensing" },
    { "gate": "C", "label": "sensitivity-redaction" },
    { "gate": "D", "label": "catalog-validate-linkcheck" },
    { "gate": "E", "label": "receipts-checksums" },
    { "gate": "F", "label": "policy-fixtures-contracts" }
  ]
}
```

> [!PROPOSED]
> Add a validator (e.g., `tools/validators/gh-required-checks`) so PRs that change workflow/job names must update this JSON in the same PR.

[Back to top](#top)

---

## Required GitHub settings

These settings must align with workflows and required checks below.

### Default-branch protection baseline

Recommended for the default branch (ruleset or classic branch protection):

- Require PRs (no direct pushes)
- Require approvals (≥ 1; increase for governance-critical changes)
- Require CODEOWNERS review
- Require status checks to pass (see **Required checks registry**)
- Require conversation resolution (recommended)
- Restrict who can push to the default branch (recommended)

> [!WARNING]
> If protection requires a check that no longer exists, merges can become permanently blocked.
> If a workflow/job is renamed, update protection **in the same PR** as the rename.

### Security feature baseline

Enable (where available):

- secret scanning (and push protection, if available)
- dependency alerts and (optionally) dependency updates (Dependabot)
- code scanning / SAST (or a documented substitute)

> [!NOTE]
> Availability depends on org policy + repo visibility.
> If a feature isn’t available, document a substitute (and enforce it via CI where possible).

### Deployment protection (optional but recommended)

> [!PROPOSED]
> If this repo deploys to shared environments, use GitHub Environments:
- require approvals for `production`
- restrict who can deploy
- ensure deployments cannot bypass Promotion Contract gates

[Back to top](#top)

---

## Workflow inventory

This section documents the *intended* responsibilities of each workflow file.

| Workflow file | Purpose | Fail-closed expectation | Typical outputs (examples) |
|---|---|---|---|
| `.github/workflows/ci.yml` | Build/test/lint/typecheck for code + docs | PR cannot merge if checks fail or do not run | test reports, build artifacts, lint summaries |
| `.github/workflows/policy-gates.yml` | Policy label checks, sensitive-location/redaction checks, Story Node claim hygiene | PR blocked if policy/sensitivity is unclear | policy decision log, redaction scan report |
| `.github/workflows/provenance-audit.yml` | Promotion eligibility verification (spec_hash stability, receipts/manifests, checksums) | Promotion blocked if provenance/audit is incomplete | checksum report, manifest lint, receipt validation |
| `.github/workflows/gates.yml` | **Always-runs** aggregator (“anti-skip” summary job) | If any required gate is skipped or fails, this fails | single required status check |
| `.github/workflows/release.yml` | Release/promotion orchestration (tags, packaging, publish) | No RAW→Published jumps; gates must pass | release manifest, publish logs |
| `.github/workflows/supply-chain.yml` | Optional: SBOM + signing/attestations | Release blocked if attestations required and missing | SBOM, provenance attestations |

> [!IMPORTANT]
> This table is a **contract**. If you add a workflow, add it here.
> If you remove/rename a workflow, update this table and protection rulesets in the same PR.

[Back to top](#top)

---

## Promotion Contract mapping

KFM’s Promotion Contract turns governance intent into enforceable behavior. In GitHub terms:
- CI must block merges when required promotion artifacts are missing or invalid.
- Release/promotion workflows must block promotion when gates fail.

### Baseline gates (Promotion Contract v1)

These gates are framed so they can be automated in CI and reviewed during steward sign-off.

| Gate | What it means (summary) | What CI must check (typical) |
|---|---|---|
| **A — Identity & versioning** | Dataset + DatasetVersion are deterministic and stable | spec_hash golden tests; naming lint; digest verification |
| **B — Licensing & rights** | License/rights/attribution explicit; terms snapshot exists | fail if missing/unknown; terms snapshot artifact |
| **C — Sensitivity + redaction plan** | policy_label assigned; obligations defined for sensitive outputs | default-deny tests; redaction/generalization proof |
| **D — Catalog triplet validation** | DCAT/STAC/PROV validate and cross-link; EvidenceRefs resolve | profile validators + linkcheck; resolvability tests |
| **E — Run receipts + checksums** | receipts exist; inputs/outputs enumerated with digests | receipt schema validation; checksum match checks |
| **F — Policy + contract tests** | policy fixtures pass; contracts validate; resolver behaviors tested | fixtures-driven policy tests; OpenAPI/schema validation |

> [!NOTE]
> Some branches/operators also track “QA thresholds” and “release manifest” as separate gates.
> That’s compatible — treat them as additional required checks, not a weakening of v1.

### Anti-skip rule (non-negotiable)

A required gate MUST NOT be skippable via:
- `paths:` filters that accidentally exclude it,
- `if:` conditions that bypass it,
- upstream job failures that prevent the “required” job from running.

**Recommended pattern:** include a final `gate-summary` job that always runs and fails if any required sub-gate did not run or did not pass. Mark *that* summary job as the required status check.

<details>
<summary><strong>PROPOSED: minimal gate-summary job pattern (copy/paste)</strong></summary>

```yaml
name: gates
on:
  pull_request:

jobs:
  lint:
    name: ci / lint
    runs-on: ubuntu-latest
    steps:
      - run: echo "lint"

  policy:
    name: policy / gates
    runs-on: ubuntu-latest
    steps:
      - run: echo "policy"

  provenance:
    name: provenance / audit
    runs-on: ubuntu-latest
    steps:
      - run: echo "provenance"

  gate_summary:
    name: gates / gate-summary
    if: always()
    needs: [lint, policy, provenance]
    runs-on: ubuntu-latest
    steps:
      - name: Assert required jobs ran and succeeded
        run: |
          echo "lint: ${{ needs.lint.result }}"
          echo "policy: ${{ needs.policy.result }}"
          echo "provenance: ${{ needs.provenance.result }}"
          test "${{ needs.lint.result }}" = "success"
          test "${{ needs.policy.result }}" = "success"
          test "${{ needs.provenance.result }}" = "success"
```

> Mark **`gates / gate-summary`** as the required status check in rulesets/branch protection.
> It fails closed if any dependency fails **or is skipped**.
</details>

[Back to top](#top)

---

## Required checks registry

Branch protection / rulesets should require a stable set of checks corresponding to the gate categories above.

> [!IMPORTANT]
> **Check names are repo-specific.** Replace placeholders with the *actual* status check names emitted by your workflows.

### Status check naming pitfalls

- **Skipped jobs can look “green.”** If a required gate can be skipped, fail-closed is compromised.
- **Downstream jobs may be skipped** when an upstream job fails; be careful which job you mark “required”.
- **Reusable workflows can change name formats.** Copy the exact name from the PR Checks UI.

### Registry table (recommended pattern)

> [!PROPOSED]
> Require only **one** check: the always-runs `gate-summary` check.

| Gate | Required check name (preferred) | Source workflow | Notes |
|---|---|---|---|
| gate_summary | `gates / gate-summary` | `gates.yml` | Aggregates and fails on skipped/failed gates |

### Registry table (expanded pattern, if you require individual checks)

| Gate | Required check name (placeholder) | Source workflow | Notes |
|---|---|---|---|
| A (Identity) | `promotion / identity-versioning` | `provenance-audit.yml` or `ci.yml` | spec_hash stability + naming + digest |
| B (Rights) | `promotion / rights-licensing` | `policy-gates.yml` or `provenance-audit.yml` | quarantine if unclear |
| C (Sensitivity) | `policy / sensitivity-redaction` | `policy-gates.yml` | default-deny; generalized derivatives |
| D (Catalogs) | `catalog / validate-linkcheck` | `ci.yml` or `provenance-audit.yml` | profiles + cross-links |
| E (Receipts) | `provenance / receipts-checksums` | `provenance-audit.yml` | receipts + digests |
| F (Policy/Contracts) | `policy / fixtures-contracts` | `policy-gates.yml` + `ci.yml` | fixtures + OpenAPI/schema |

**Quality gates (recommended additional required checks):**
- `ci / lint`
- `ci / build-test`
- `ci / docs-linkcheck` (if docs are part of the deliverable)
- `security / secret-scan` (or substitute)
- `security / dependency-review` (or substitute)

### When a required check goes missing

If merges are blocked because a required check “doesn’t exist”:

1. Confirm the workflow still exists under `.github/workflows/`.
2. Confirm workflow/job `name:` fields didn’t change.
3. Open a PR and confirm the check name in the PR Checks list.
4. Update rulesets/branch protection in the same PR that changed workflow/job names.

[Back to top](#top)

---

## CI and promotion gates

KFM uses fail-closed gates to protect integrity, provenance, rights, and policy obligations.

```mermaid
flowchart LR
  dev[Contributor] --> pr[Pull Request]
  pr --> ci[CI Workflows]
  ci --> q[Quality]
  ci --> s[Security]
  ci --> p[Policy]
  ci --> prov[Provenance]
  q --> decision{All required gates pass?}
  s --> decision
  p --> decision
  prov --> decision
  decision -->|No| block[Block merge + report]
  decision -->|Yes| merge[Merge]
  merge --> promote[Promotion / Release]
```

### PR-based promotion workflow (recommended)

Promotion should be social + technical, not ad hoc:

1) Contributor opens PR adding:
- source registry entry
- dataset spec / pipeline spec
- small fixtures + expected outputs (where feasible)

2) CI runs:
- schema validation
- fixtures-driven policy tests
- spec_hash stability test
- catalog/profile validation + link-check

3) Steward review:
- licensing/rights clarity
- sensitivity classification + redaction/generalization plan

4) Operator merges and triggers a controlled pipeline run.

5) Outputs are written to processed + catalogs.

6) Release/promotion manifest is created and tagged.

---

## Trust membrane reminder

```mermaid
flowchart LR
  ui[UI / Clients] --> api[Governed APIs]
  api --> policy[Policy Boundary]
  policy --> storage[(Storage / Index)]
  ui -. never direct .-> storage
```

- UI/clients **must not** talk to storage/DB directly.
- Core/domain logic **must not** bypass repositories to reach storage.
- Policy boundary decisions should be **auditable**.

[Back to top](#top)

---

## Issue and PR templates

### Issue templates

Use templates to keep triage consistent:

- **Bug report:** expected vs actual, reproducible steps, logs/artifacts.
- **Feature request:** user story, acceptance criteria, policy impacts.
- **Governance request:** policy label changes, redaction guidance, release criteria.
- **Data/pipeline change:** source/license, schema, validation rules, promotion plan.
- **Story Node:** narrative claim + EvidenceRefs + map footprint + time bounds.

### PR expectations

A PR should include:

- scope: what changed + why
- evidence: links/artifact IDs/checksums (as applicable)
- tests: added/updated, or justification if not possible
- rollback: how to revert safely
- governance: policy labels, redaction notes, approval path

> [!TIP]
> For governance-sensitive PRs, ensure `CODEOWNERS` routes review to both engineering and governance owners.

[Back to top](#top)

---

## Governance and policy

Non-negotiables enforced through CI + review:

- **Evidence-first:** every claim should link back to resolvable evidence (or be explicitly marked unknown).
- **Promotion Contract:** no RAW → Published jumps; each promotion emits receipts + audit entries.
- **Default-deny:** if sensitivity is unclear, deny publication; generalize/redact; request governance review.
- **Rights-aware:** “online ≠ permission”; rights metadata is enforced in UI/export paths.

[Back to top](#top)

---

## Security and responsible disclosure

- Use `SECURITY.md` for reporting vulnerabilities.
- Never post secrets or exploit details in public issues.
- Security fixes should land with tests and clear rollback notes.

> [!NOTE]
> If secret scanning / push protection is enabled, treat alerts as merge-blocking for protected branches.

[Back to top](#top)

---

## Badge maintenance

Badges at the top use Shields.io and are intentionally **static** until org/repo identifiers and workflow filenames are finalized.

When ready, swap in dynamic badges (examples):

```md
![CI](https://img.shields.io/github/actions/workflow/status/<ORG>/<REPO>/ci.yml?branch=<DEFAULT_BRANCH>)
![License](https://img.shields.io/github/license/<ORG>/<REPO>)
![Last commit](https://img.shields.io/github/last-commit/<ORG>/<REPO>)
```

> [!TIP]
> Once wired, delete the “repo-wiring pending” badge and replace it with one or more workflow badges.

[Back to top](#top)

---

## Contacts and owners

- **Engineering owners:** see `CODEOWNERS`
- **Governance owners:** see `CODEOWNERS`
- **Security contact:** see `SECURITY.md`

[Back to top](#top)

---

## Definition of Done

### Content & structure

- [ ] Badges render and reflect reality (or are clearly marked “static”)
- [ ] At least one Mermaid diagram renders
- [ ] Directory contract section is present (acceptable inputs + exclusions)
- [ ] Directory tree is present and matches current structure
- [ ] Templates exist for the main work types (bug/feature/governance/data/story)
- [ ] Links are relative and lintable (no broken internal links)
- [ ] Wiring checklist is complete (no `<ORG>`, `<REPO>`, `<DEFAULT_BRANCH>` left behind)

### Governance & enforcement

- [ ] Workflows enforce fail-closed behavior for Promotion Contract gates
- [ ] A gate-summary job exists and is the preferred required check (anti-skip)
- [ ] Required checks registry matches actual emitted check names used by rulesets/branch protection
- [ ] Policy fixtures run in CI (not only locally)
- [ ] Evidence resolver contract tests exist (at least one EvidenceRef resolvable in CI)
- [ ] Workflow inventory is kept current when workflows change
- [ ] Rulesets/branch protection updated whenever workflow/job names change

---

[Back to top](#top)
