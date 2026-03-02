<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/3c0d5c1f-14d4-4b4f-9b2b-9bc3d5c1c7b0
title: .github/README — GitHub Governance & Community Files
type: standard
version: v4
status: draft
owners: kfm-engineering; kfm-governance
created: 2026-02-22
updated: 2026-03-02
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
  - ./CODEOWNERS
  - ./workflows/
tags:
  - kfm
  - github
  - governance
  - ci
  - rulesets
notes:
  - This README is the GitHub-side “trust membrane”: templates + workflows + required checks registry.
  - Badge row uses Shields.io (static) until repo identifiers are wired for dynamic badges.
  - Do not claim a workflow/job/check exists until confirmed on your branch. Unknowns stay Unknown.
  - Promotion Contract gates map to required checks; prefer an “always-runs” gate-summary job to prevent skips.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KFM GitHub Gatehouse
Map-first • time-aware • governed delivery — **community files + CI/ruleset index**

**Status:** Draft (v4) • **Owners:** KFM Engineering + Governance  
**Posture:** default-deny • fail-closed • reproducible by digest • policy enforced in CI + runtime

![status](https://img.shields.io/badge/status-draft-blue)
![policy](https://img.shields.io/badge/policy-restricted-orange)
![fail-closed](https://img.shields.io/badge/fail--closed-required-critical)
![no-invention](https://img.shields.io/badge/no%20invention-enforced-6f42c1)
![trust-membrane](https://img.shields.io/badge/trust%20membrane-merge--time%20gates-critical)
![promotion-contract](https://img.shields.io/badge/promotion%20contract-gated-critical)
![cite-or-abstain](https://img.shields.io/badge/cite--or--abstain-hard%20gate-6f42c1)
![repo](https://img.shields.io/badge/repo-wiring%20pending-lightgrey)

> [!IMPORTANT]
> **Policy labels are KFM metadata, not GitHub ACLs.**  
> Nothing in `.github/` should contain secrets, private keys, credentials, or restricted coordinates.

**Quick links:**  
[Quick start](#quick-start) •
[What this governs](#what-this-governs) •
[Status legend](#status-legend) •
[Reality check](#reality-check) •
[Directory contract](#directory-contract) •
[Core invariants](#core-invariants) •
[Required GitHub settings](#required-github-settings) •
[Required checks registry](#required-checks-registry) •
[Workflow design rules](#workflow-design-rules) •
[Workflow inventory](#workflow-inventory) •
[Promotion Contract mapping](#promotion-contract-mapping) •
[Templates](#templates) •
[Security](#security-and-responsible-disclosure) •
[Definition of Done](#definition-of-done)

---

## Quick start

### For contributors
- **File an issue:** use `.github/ISSUE_TEMPLATE/` templates (bug, feature, governance, data/pipeline, story node).
- **Open a PR:** follow `../CONTRIBUTING.md`. Keep changes small and attach evidence (links, artifact IDs, digests).
- **If you touch policy/data/promotion:** expect CI to **fail-closed** until promotion/metadata/policy gates pass.

### For maintainers
- **Never weaken gates to “get green.”** Fix the underlying metadata, provenance, tests, redaction/generalization, or rights.
- **If a check name changes:** update rulesets/branch protection **in the same PR**.
- **Prefer one required check:** an always-runs `gate-summary` (“anti-skip”) check.

[Back to top](#top)

---

## What this governs

`.github/` is the repo’s **merge-time trust membrane**: it defines what GitHub enforces at PR time.

This README is:
- an index of **community health files** and templates (CONTRIBUTING, CODE_OF_CONDUCT, SECURITY)
- a contract for **CI/policy gates** and how they map to promotion/governance requirements
- a registry home for **required status checks** and their stable names

This README is not:
- product documentation (see repo root `README.md` and `/docs`)
- policy source-of-truth (see `/policy` and governance docs referenced in the MetaBlock)

[Back to top](#top)

---

## Status legend

KFM governance docs use three tags.

- **CONFIRMED** — verified on the *current branch* (file exists; workflows emit named checks; validators run).
- **PROPOSED** — recommended default / template / target posture.
- **UNKNOWN** — not verified; treat as **fail-closed** if it’s required by contract.

> [!TIP]
> This README intentionally labels unknowns rather than “making it sound nice.” Green builds built on fantasy are not acceptable.

[Back to top](#top)

---

## Reality check

This README references a **target posture**. Before enforcing it with branch protection:

1. Confirm whether your org uses **repo rulesets** or **classic branch protection** (or both).
2. Confirm workflows exist under `.github/workflows/`.
3. Confirm **exact** status check names from the PR **Checks** UI (don’t guess).

### Minimum verification steps
Run these once per branch and attach outputs to a governance PR or a “wiring” issue:

```bash
# Capture branch + commit for audit trail
git rev-parse --abbrev-ref HEAD
git rev-parse HEAD

# Inspect current .github structure (truth, not vibes)
tree -a -L 4 .github || find .github -maxdepth 4 -print | sort

# Inspect workflows
ls -la .github/workflows
```

> [!IMPORTANT]
> If a link 404s, treat the linked artifact as **missing** (and therefore merge-blocking if required by contract).

[Back to top](#top)

---

## Directory contract

This section makes `.github/` behave like a governed module.

### Where it fits
`.github/` is the repo’s **gatehouse**: PR templates, CODEOWNERS routing, required checks, and CI workflows live here.

### Acceptable inputs
- Community health files (`CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, optional `SUPPORT.md`)
- Issue forms and PR templates (YAML/Markdown)
- CI workflows and shared composite actions used by workflows
- `CODEOWNERS` rules that route governance-critical changes
- Machine-readable registries that stabilize branch protection (e.g., required checks registry)

### Exclusions
- **Secrets** or credentials (never store in-repo)
- Operational runbooks and product docs that belong in `/docs`
- Dataset specs, catalogs, or policy bundles that belong in their governed folders (reference them; don’t duplicate them)

[Back to top](#top)

---

## Core invariants

These invariants are why `.github/` is treated as a protected surface.

### Invariants and GitHub enforcement map

| Invariant | Why it exists | How GitHub helps enforce it |
|---|---|---|
| **Fail-closed** | Unknown rights/sensitivity/provenance must block publication | Required checks + branch rulesets; `gate-summary` anti-skip |
| **Trust membrane** | Prevent policy bypass (no direct DB/storage from clients) | CODEOWNERS for policy/API boundaries; CI tests for “no bypass” invariants |
| **Truth path** | Reproducibility + audit + rollback for data | Promotion gates in CI; required receipts/manifests; release manifests |
| **Cite-or-abstain** | Prevent hallucination and restricted leakage | CI gates that verify EvidenceRefs resolve + are policy-allowed |

> [!NOTE]
> GitHub doesn’t enforce all invariants by itself. It enforces the *inputs* to enforcement: required checks, CODEOWNERS reviews, and workflow execution.

[Back to top](#top)

---

## Wiring checklist

Fill these in once, then convert placeholders → reality.

| Wiring item | Where it is used | Current value | Target value |
|---|---|---|---|
| Org | Dynamic badges, links | `<ORG>` | TODO |
| Repo | Dynamic badges, links | `<REPO>` | TODO |
| Default branch | Rulesets/badges | `<DEFAULT_BRANCH>` | TODO |
| Ruleset / protection name | Admin UI + audit | `<RULESET_NAME>` | TODO |
| Workflow filenames | Required check mapping | `<WORKFLOW_FILES>` | TODO |
| Required check names | Rulesets/branch protection | `<CHECK_NAMES>` | TODO |
| Required checks registry file | Reviewable stability | `.github/required-checks.v1.json` | PROPOSED |

[Back to top](#top)

---

## Folder map

### Actual on this branch
Generate and paste into a wiring PR (this is the only map that counts):

```bash
tree -a -L 4 .github
```

### Target shape
> **PROPOSED** minimum structure for `.github/` (adjust to match reality):

```text
.github/                                                 # GitHub-side trust boundary: ownership, community files, and CI workflows that enforce governance + gates
├─ README.md                                             # How .github works: governance intent, required reviews/checks, and how CI maps to gates/labels/waivers
├─ CODEOWNERS                                            # Review authority map (decision rights wiring): required approvers by path (policy/docs/data/contracts/apps)
│
├─ CODE_OF_CONDUCT.md                                    # Community behavior standards (GitHub-surface copy of repository-wide code of conduct)
├─ CONTRIBUTING.md                                       # Contribution rules (PR hygiene, required templates, CI expectations, governance touchpoints)
├─ SECURITY.md                                           # Security policy (vuln reporting, disclosure process, secret handling expectations)
├─ SUPPORT.md                                            # Optional: where to ask for help (issues/discussions), maintainer response expectations, escalation paths
│
├─ required-checks.v1.json                               # PROPOSED: canonical required status checks list (source-of-truth for branch protection + gate aggregator)
├─ labels.v1.yml                                         # PROPOSED: canonical GitHub label taxonomy (type/area/severity/governance) for consistent triage + automation
├─ required-labels.v1.json                               # PROPOSED: machine-checkable label rules (e.g., “governance PRs must carry governance/* label”)
│
├─ PULL_REQUEST_TEMPLATE.md                              # Optional single default PR template (quick checklist + links to governance/gates expectations)
├─ PULL_REQUEST_TEMPLATE/                                # Optional multi-template set (choose template per change type to enforce correct review/gates)
│  ├─ default.md                                         # General PR template (summary, tests, docs, risks, rollout/rollback)
│  ├─ governance.md                                      # Governance PR template (policy/labels/gates changes, decision record links, risk acceptance)
│  ├─ data-pipeline.md                                   # Data pipeline PR template (inputs/outputs, receipts, QA, promotion gates, rerun notes)
│  ├─ api-contract.md                                    # API contract PR template (OpenAPI/schema diffs, compatibility, versioning, obligations)
│  └─ security.md                                        # Security PR template (threat model notes, secrets scan, access control impact, logging/audit)
│
├─ ISSUE_TEMPLATE/                                       # Issue forms for consistent intake (triage labels, required fields, routing to owners)
│  ├─ config.yml                                         # Issue form configuration (contact links, disable blank issues, routing hints)
│  ├─ bug_report.yml                                     # Bug intake (repro steps, expected/actual, environment, logs, severity)
│  ├─ feature_request.yml                                # Feature intake (problem, scope, acceptance criteria, alternatives)
│  ├─ governance_request.yml                              # Governance intake (policy change request, label/gate impact, decision record requirement)
│  ├─ data_pipeline_change.yml                            # Data change intake (dataset, cadence, schema, QA, provenance, promotion plan)
│  └─ story_node.yml                                     # Story intake (claims, sources, timeline, map layers, sensitivity/obligations)
│
├─ actions/                                              # Optional: composite actions (shared CI building blocks used across workflows)
│  ├─ changed-files/action.yml                           # PROPOSED: change classifier (paths → affected gates/reviewers/checklists)
│  ├─ gate-summary/action.yml                            # PROPOSED: aggregates required checks into a single “gates” status (fail-closed summary)
│  └─ upload-receipts/action.yml                          # PROPOSED: collects/upload run receipts (digests, manifests, logs) as CI artifacts
│
└─ workflows/                                            # CI workflows: enforce quality, policy, provenance, and publication readiness
   ├─ ci.yml                                             # Baseline CI: build/test/lint/typecheck/docs (fast feedback + required checks)
   ├─ policy-gates.yml                                   # Policy tests: OPA/conftest fixtures (default-deny, obligations correctness, regression suite)
   ├─ provenance-audit.yml                                # Provenance gate: receipts/manifests/digests integrity + reproducibility checks
   ├─ catalog-validate.yml                                # PROPOSED: catalog validation (STAC/DCAT/PROV schema validation + link checking)
   ├─ gates.yml                                          # PROPOSED: always-runs aggregator producing a single normalized gate status for branch protection
   ├─ supply-chain.yml                                   # Optional: SBOM generation + attestations/signing (SLSA-ish posture; dependency integrity)
   ├─ dependency-review.yml                               # Optional: dependency change review (license/security diffs) for PRs touching lockfiles
   └─ codeql.yml                                         # Optional: CodeQL analysis (security scanning) with configured query packs and upload steps
```

[Back to top](#top)

---

## Required GitHub settings

### Default-branch protection baseline
Recommended on default branch via ruleset or classic protection:

- Require PRs (no direct pushes)
- Require approvals (≥ 1; increase for governance-critical changes)
- Require CODEOWNERS review
- Require status checks to pass (see required checks registry)
- Require conversation resolution
- Restrict who can push to default branch (optional but recommended)

> [!WARNING]
> If protection requires a check that no longer exists, merges can become permanently blocked.
> Rename a job? Update rulesets/protection **in the same PR**.

### Security features baseline
Enable where available (or document substitutes):

- secret scanning (and push protection, if available)
- dependency alerts + updates (Dependabot/Renovate)
- code scanning / SAST (or a documented equivalent)

[Back to top](#top)

---

## Required checks registry

### Why this exists
GitHub required checks are fragile because check names change with workflow/job renames.

**PROPOSED:** store the canonical check list in a machine-readable file and validate it in CI:

- `.github/required-checks.v1.json`

### Recommended required check strategy
Prefer **one** required check:

- `gates / gate-summary` (always-runs, fails if any required gate fails **or is skipped**)

If org policy requires multiple checks, require:
- `ci / ...` (quality)
- `policy / ...` (default-deny + fixtures)
- `provenance / ...` (receipts/manifests/digests)
- `catalog / ...` (triplet validation + linkcheck)

### Example registry file
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
  "promotion_contract_gates": [
    { "gate": "A", "label": "identity-versioning" },
    { "gate": "B", "label": "rights-licensing" },
    { "gate": "C", "label": "sensitivity-redaction" },
    { "gate": "D", "label": "catalog-triplet-validation" },
    { "gate": "E", "label": "receipts-checksums" },
    { "gate": "F", "label": "policy-and-contract-tests" },
    { "gate": "G", "label": "optional-production-posture" }
  ]
}
```

### PROPOSED validator rule
If a PR changes:
- `.github/workflows/**` (workflow/job names), or
- `.github/actions/**` (shared actions), or
- `.github/required-checks.v1.json`

…then CI must validate that:
- all `required_checks[*].check_name` values appear in PR Checks, and
- required checks registry updated in the same PR.

[Back to top](#top)

---

## Workflow design rules

### Fail-closed is a build property
A gate is only meaningful if it cannot be bypassed by:
- `paths:` filters that exclude it,
- `if:` conditions that skip it,
- upstream failures that prevent the “required” job from running.

**Design rule:** required gates must be reachable from a single always-runs summary job.

### Minimal gate-summary pattern
<details>
<summary><strong>PROPOSED: copy/paste gates.yml pattern</strong></summary>

```yaml
name: gates
on:
  pull_request:

permissions:
  contents: read

jobs:
  ci:
    name: ci / build-test
    runs-on: ubuntu-latest
    steps:
      - run: echo "run unit tests, build, etc."

  policy:
    name: policy / fixtures
    runs-on: ubuntu-latest
    steps:
      - run: echo "run OPA/conftest fixtures, deny-by-default"

  provenance:
    name: provenance / audit
    runs-on: ubuntu-latest
    steps:
      - run: echo "validate receipts/manifests/digests"

  gate_summary:
    name: gates / gate-summary
    if: always()
    needs: [ci, policy, provenance]
    runs-on: ubuntu-latest
    steps:
      - name: Assert required jobs ran and succeeded
        run: |
          echo "ci:        ${{ needs.ci.result }}"
          echo "policy:    ${{ needs.policy.result }}"
          echo "provenance:${{ needs.provenance.result }}"
          test "${{ needs.ci.result }}" = "success"
          test "${{ needs.policy.result }}" = "success"
          test "${{ needs.provenance.result }}" = "success"
```

> Mark **`gates / gate-summary`** as the required status check in rulesets/branch protection.
</details>

### Workflow security defaults
**PROPOSED defaults for all workflows:**
- minimal permissions (`contents: read` unless write is required)
- pin third-party actions to versions (or commit SHAs where required by policy)
- never print secrets; never echo raw tokens; prefer OIDC to mint short-lived creds
- upload artifacts (receipts, manifests, reports) for auditability

### Kill switch
> **PROPOSED:** a “break glass” mechanism that fails the required checks fast (minutes, not hours) if a critical governance issue is discovered.

Implement as either:
- a repo file (e.g., `.github/killswitch.yml`), and/or
- an org/repo secret flag consumed by required checks.

[Back to top](#top)

---

## Workflow inventory

This section is intentionally a contract for what workflows *mean*.  
**UNKNOWN:** replace filenames/check names with reality once verified on your branch.

| Workflow | Responsibility | Fail-closed expectation | Notes |
|---|---|---|---|
| `ci.yml` | Lint, typecheck, tests, build, docs checks | merge blocked on failure | Prefer fast “always” suite + optional heavy suites |
| `policy-gates.yml` | Default-deny policy fixtures; sensitivity/redaction checks | merge blocked if policy unclear | Policy is not advisory |
| `provenance-audit.yml` | Receipts/manifests/digests; promotion eligibility | merge blocked if provenance incomplete | Treat missing receipts as blocking |
| `catalog-validate.yml` | STAC/DCAT/PROV validate + cross-link + linkcheck | merge blocked if catalogs break | EvidenceRefs must resolve |
| `gates.yml` | Anti-skip aggregator | required check | Preferred single required check |
| `supply-chain.yml` | SBOM + attestations (optional) | release blocked if enabled | Only enforce if org posture requires |

> [!IMPORTANT]
> Add/remove/rename workflows? Update this table and `.github/required-checks.v1.json` in the same PR.

[Back to top](#top)

---

## Promotion Contract mapping

This section ties GitHub merge-time enforcement to KFM’s promotion posture.

### Truth path zones
> **CONFIRMED (design intent):** RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED  
Promotion is the act of moving a dataset version forward *only* when gates pass.

### Promotion Contract v1 gates
**Minimum credible set** (block promotion if missing):

| Gate | Meaning | CI “shape” (typical checks) |
|---|---|---|
| **A — Identity and versioning** | Stable dataset_id + immutable dataset_version_id via spec_hash | spec_hash recompute + golden tests |
| **B — Licensing and rights** | Explicit license; rights/attribution captured; unclear = quarantine | fail if missing/unknown |
| **C — Sensitivity and redaction plan** | policy_label assigned; obligations recorded in PROV | deny-by-default policy tests |
| **D — Catalog triplet validation** | DCAT/STAC/PROV exist, validate, and cross-link | validators + linkcheck |
| **E — Run receipt and checksums** | run_receipt exists; inputs/outputs enumerated with digests | receipt schema + checksum verification |
| **F — Policy tests and contract tests** | OPA policy fixtures pass; EvidenceRef resolves in CI; contracts validate | fixture tests + resolver contract tests |

**Optional but recommended production posture:**
- SBOM + build provenance (pipeline + API/UI artifacts)
- performance and accessibility smoke checks

### Anti-skip rule
A required gate MUST NOT be skippable. If you need “selective execution,” do it like this:

- required checks: **always run**
- optional checks: gated by change-scope (paths) or “materiality” logic
- required `gate-summary`: fails if any required check failed/skipped

[Back to top](#top)

---

## Templates

### Issue templates
Use templates to enforce evidence + governance hygiene:

- **Bug report:** expected vs actual, reproducible steps, logs/artifacts
- **Feature request:** user story, acceptance criteria, policy impacts
- **Governance request:** policy label changes, redaction guidance, release criteria
- **Data/pipeline change:** source/license, schema, validation rules, promotion plan
- **Story Node:** narrative claim + EvidenceRefs + map footprint + time bounds

### PR expectations
A PR should include:
- **scope:** what changed + why
- **evidence:** links/artifact IDs/checksums (as applicable)
- **tests:** added/updated, or justification if not possible
- **rollback:** how to revert safely
- **governance:** policy labels, redaction notes, approval path

> [!TIP]
> For governance-sensitive PRs, ensure `CODEOWNERS` routes review to **both** engineering and governance owners.

[Back to top](#top)

---

## Security and responsible disclosure

- Use `SECURITY.md` for reporting vulnerabilities.
- Never post secrets or exploit details in public issues.
- Security fixes should land with tests and clear rollback notes.

> [!NOTE]
> Treat secret-scanning alerts as merge-blocking for protected branches.

[Back to top](#top)

---

## Badge maintenance

Badges at the top are intentionally **static** until org/repo identifiers and workflow filenames are finalized.

When ready, switch to dynamic badges (examples):

```md
![CI](https://img.shields.io/github/actions/workflow/status/<ORG>/<REPO>/ci.yml?branch=<DEFAULT_BRANCH>)
![Last commit](https://img.shields.io/github/last-commit/<ORG>/<REPO>)
```

[Back to top](#top)

---

## Contacts and owners

- **Engineering owners:** see `CODEOWNERS`
- **Governance owners:** see `CODEOWNERS`
- **Security contact:** see `SECURITY.md`

[Back to top](#top)

---

## Definition of Done

### Content and structure
- [ ] Badges render and reflect reality (or are clearly marked static)
- [ ] Directory contract section is present (acceptable inputs + exclusions)
- [ ] Folder map includes an **actual** `tree -a -L 4 .github` snapshot (or linked)
- [ ] Links are relative and lintable (no broken internal links)
- [ ] Wiring checklist complete (no `<ORG>`, `<REPO>`, `<DEFAULT_BRANCH>` left behind)

### Governance and enforcement
- [ ] Workflows enforce fail-closed behavior for Promotion Contract gates
- [ ] A gate-summary job exists and is the preferred required check (anti-skip)
- [ ] Required checks registry matches emitted check names used by rulesets/branch protection
- [ ] Policy fixtures run in CI (not only locally)
- [ ] Evidence resolver contract tests exist (at least one EvidenceRef resolvable in CI)
- [ ] Workflow inventory updated whenever workflows change
- [ ] Rulesets/branch protection updated whenever workflow/job names change

[Back to top](#top)

---

## Glossary

- **PEP:** Policy Enforcement Point (governed API boundary)
- **EvidenceRef:** A structured reference that resolves to an inspectable evidence bundle
- **Evidence bundle:** Metadata + artifacts + provenance needed to inspect/reproduce a claim
- **Cite-or-abstain:** If citations can’t be verified and policy-allowed, reduce scope or abstain
