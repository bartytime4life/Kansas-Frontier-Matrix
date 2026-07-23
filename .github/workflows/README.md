<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/github-workflows-readme
title: .github/workflows README
type: README
version: v0.3
status: draft; repository-grounded workflow inventory
owners: ["@bartytime4life"]
created: 2026-07-08
updated: 2026-07-22
policy_label: public; github-actions; workflow-governance; fail-closed; non-publisher
owning_root: .github/
responsibility: GitHub Actions orchestration, trigger and permission boundaries, check-name stability, and CI maturity disclosure
truth_posture: cite-or-abstain; a workflow file or green job is not proof of release or publication readiness
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 1180cf7ec53d5acbbb859a39d93c1d129ec83df9
  workflow_files: 41
  inventory_method: complete tracked-tree inspection and static workflow review
related:
  - ../README.md
  - ../CODEOWNERS
  - ../PULL_REQUEST_TEMPLATE.md
  - ../../CONTRIBUTING.md
  - ../../SECURITY.md
  - ../../Makefile
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/ai-build-operating-contract.md
  - ../../tools/validators/README.md
  - ../../policy/
  - ../../schemas/
  - ../../contracts/
  - ../../tests/
  - ../../fixtures/
  - ../../release/
notes:
  - "The 41-file inventory is complete for tracked .github/workflows/*.yml at the pinned commit."
  - "Maturity groups are derived from each workflow's current status comments and executable steps; they do not certify current run success."
  - "Branch protection, repository token defaults, workflow history, logs, and artifact retention remain external verification items."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `.github/workflows/`

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b)](#status)
[![Inventory: 41 workflows](https://img.shields.io/badge/inventory-41%20workflows-1f6feb)](#complete-workflow-inventory)
[![Permissions: explicit](https://img.shields.io/badge/permissions-41%2F41%20explicit-15803d)](#trigger-and-permission-preflight)
[![Publisher: no](https://img.shields.io/badge/publisher-no-b91c1c)](#authority-boundary)
[![Action refs: major tags](https://img.shields.io/badge/action%20refs-major%20tags-f97316)](#external-action-inventory)

> GitHub Actions orchestration for repository-owned checks and explicit readiness holds. Workflow YAML may run tools and report outcomes; it does not become policy, evidence, release, or publication authority.

## Quick navigation

- [Purpose](#purpose)
- [Authority boundary](#authority-boundary)
- [Status](#status)
- [Complete workflow inventory](#complete-workflow-inventory)
- [Trigger and permission preflight](#trigger-and-permission-preflight)
- [External action inventory](#external-action-inventory)
- [Inputs and outputs](#inputs-and-outputs)
- [Workflow authoring contract](#workflow-authoring-contract)
- [Validation](#validation)
- [Review and rollback](#review-and-rollback)
- [Open verification items](#open-verification-items)
- [Changelog](#changelog)

## Purpose

This subtree answers one bounded operational question:

> Which GitHub-hosted jobs run for a repository event, with which permissions and inputs, and what review signal do they produce?

It supports maintainers, reviewers, CI/tooling stewards, domain owners, policy reviewers, and agents working on workflow changes.

## Authority boundary

| Concern | Authority owner | Workflow role |
|---|---|---|
| Trigger, path filters, job graph, runner, token permissions, concurrency, timeout, and check name | `.github/workflows/` | Own GitHub Actions orchestration. |
| Validator and domain behavior | `tools/`, `packages/`, `pipelines/`, applications | Invoke repository-owned commands; do not reproduce the logic in YAML. |
| Policy decisions | `policy/` | Evaluate reviewed policy inputs; never create inline policy authority. |
| Meaning and shape | `contracts/`, `schemas/` | Validate without redefining. |
| Expected behavior | `tests/`, `fixtures/` | Execute deterministic positive and negative cases. |
| Evidence, receipts, proofs, catalogs, and releases | governed `data/` and `release/` lanes | Produce candidates or verification aids only through accepted tools and transitions. |

> [!IMPORTANT]
> `WORKFLOW_HOLD`, a skip, a static-readiness pass, and a substantive validator pass are different outcomes. A job name must not imply more maturity than its executed steps establish.

## Status

Snapshot: `main@1180cf7ec53d5acbbb859a39d93c1d129ec83df9`, inspected 2026-07-22.

| Finding | Status | Interpretation |
|---|---|---|
| Workflow inventory | **CONFIRMED: 41 tracked `.yml` files** | Complete for the pinned tree. No `.yaml` workflow is tracked. |
| Explicit permissions | **CONFIRMED: 41/41** | Every workflow declares a top-level permissions boundary. |
| Privileged PR trigger | **CONFIRMED absent** | No `pull_request_target` trigger key. A safety comment names the trigger without enabling it. |
| Runner trust | **CONFIRMED GitHub-hosted** | No `self-hosted` occurrence. |
| Secret references | **CONFIRMED absent in workflow YAML** | No direct `secrets.*` occurrence; external settings remain unknown. |
| Write scopes | **CodeQL only** | `security-events: write` is present for code-scanning upload. No `contents`, `issues`, `pull-requests`, `packages`, `deployments`, or `id-token` write grant is present. |
| External action pinning | **Major-version tags** | Action refs are reviewable but not immutable commit pins. |
| Branch protection | **NEEDS VERIFICATION** | File inspection cannot establish required checks or rulesets. |
| Workflow execution | **NEEDS VERIFICATION** | This inventory does not assert recent pass/fail results. |

## Complete workflow inventory

The maturity groups below describe current code and status comments. A group is not a release-readiness grade.

### Explicit greenfield, non-enforcing scaffolds

These files declare themselves proposed greenfield scaffolds and expose visible TODO/hold behavior:

- [`accessibility.yml`](accessibility.yml)
- [`citation-validation.yml`](citation-validation.yml)
- [`ui-build.yml`](ui-build.yml)

They must not be required as proof that accessibility, citation resolution, or the UI build is implemented.

### Bounded domain readiness and governed holds

These workflows inspect domain structure, placeholders, negative boundaries, or readiness evidence while explicitly withholding unproved implementation claims:

- [`domain-agriculture.yml`](domain-agriculture.yml)
- [`domain-archaeology.yml`](domain-archaeology.yml)
- [`domain-atmosphere.yml`](domain-atmosphere.yml)
- [`domain-fauna.yml`](domain-fauna.yml)
- [`domain-flora.yml`](domain-flora.yml)
- [`domain-geology.yml`](domain-geology.yml)
- [`domain-habitat.yml`](domain-habitat.yml)
- [`domain-hazards.yml`](domain-hazards.yml)
- [`domain-hydrology.yml`](domain-hydrology.yml)
- [`domain-people-dna-land.yml`](domain-people-dna-land.yml)
- [`domain-roads-rail-trade.yml`](domain-roads-rail-trade.yml)
- [`domain-settlements-infrastructure.yml`](domain-settlements-infrastructure.yml)
- [`domain-soil.yml`](domain-soil.yml)

### Bounded system readiness and governed holds

- [`docs-build.yml`](docs-build.yml)
- [`e2e-smoke.yml`](e2e-smoke.yml)
- [`evidence-resolver.yml`](evidence-resolver.yml)
- [`focus-mock-test.yml`](focus-mock-test.yml)
- [`hydrology-proof-slice.yml`](hydrology-proof-slice.yml)
- [`link-check.yml`](link-check.yml)

These jobs intentionally make missing executables, fixtures, proof closure, or runtime readiness visible. A hold is a truthful finite outcome, not a passing implementation claim.

### Command-bearing and partial gates

These workflows invoke repository commands, third-party analysis, static checks, shape validators, or partial gates. Several still contain explicit holds for unimplemented downstream obligations:

- [`api-test.yml`](api-test.yml)
- [`codeql.yml`](codeql.yml)
- [`connector-gate.yml`](connector-gate.yml)
- [`contract-drift.yml`](contract-drift.yml)
- [`contracts-validate.yml`](contracts-validate.yml)
- [`deny-test.yml`](deny-test.yml)
- [`dependency-scan.yml`](dependency-scan.yml)
- [`docs-control-plane.yml`](docs-control-plane.yml)
- [`maplibre-perf-governance.yml`](maplibre-perf-governance.yml)
- [`pmtiles-attestation.yml`](pmtiles-attestation.yml)
- [`policy-boundary-guards.yml`](policy-boundary-guards.yml)
- [`policy-test.yml`](policy-test.yml)
- [`promotion-gate.yml`](promotion-gate.yml)
- [`release-dry-run.yml`](release-dry-run.yml)
- [`rollback-drill.yml`](rollback-drill.yml)
- [`schema-validation.yml`](schema-validation.yml)
- [`source-descriptor-validate.yml`](source-descriptor-validate.yml)
- [`telemetry-policy.yml`](telemetry-policy.yml)
- [`validator-suite.yml`](validator-suite.yml)

Read the exact steps and job summaries before relying on any of these as a merge gate. “Command-bearing” does not mean complete or production-ready.

## Trigger and permission preflight

Before changing or relying on a workflow, record:

| Question | Required answer |
|---|---|
| Event | Which of `pull_request`, `push`, `workflow_dispatch`, schedule, or reusable call triggers it? |
| Path scope | Which changed paths activate it, and which expected paths are excluded? |
| Untrusted input | Can fork code, issue text, PR metadata, artifacts, caches, or downloaded content influence execution? |
| Token | What is the smallest explicit `permissions` set? |
| Secrets/OIDC | Why is identity or secret access required, and is it reachable from untrusted code? |
| Network | Which registries or endpoints are contacted, and can deterministic fixtures replace them? |
| Output | Check signal, log, report, artifact, candidate receipt, or governed object? |
| Failure | Does failure stay visible, or can `continue-on-error` / `\|\| true` mask the governing result? |
| Check name | Is the workflow/job name coupled to branch protection? |
| Rollback | How can the workflow be safely disabled or reverted without weakening unrelated gates? |

### Static threat findings at the pinned snapshot

| Threat surface | Finding |
|---|---|
| `pull_request_target` | No trigger key; one safety comment names it without enabling it. |
| Self-hosted runner | No occurrence. |
| Direct secret expressions | No `secrets.*` occurrence. |
| Ordinary write permissions | No `contents`, `issues`, `pull-requests`, `packages`, `deployments`, or `id-token` write grant. |
| Code scanning | [`codeql.yml`](codeql.yml) grants `security-events: write`; review this if its event or trust boundary changes. |
| External action immutability | All refs use major-version tags, not commit SHAs. |
| Publication path | No file-presence claim authorizes publication; inspect every command before changing this finding. |

## External action inventory

| Action reference | Occurrences | Pinning posture |
|---|---:|---|
| `actions/checkout@v7` | 88 | Major tag; mutable. |
| `actions/setup-python@v7` | 54 | Major tag; mutable. |
| `actions/setup-node@v7.0.0` | 3 | Release tag; mutable. |
| `actions/upload-artifact@v7` | 1 | Major tag; mutable. |
| `github/codeql-action/init@v4` | 1 | Major tag; mutable. |
| `github/codeql-action/analyze@v4` | 1 | Major tag; mutable. |

Dependabot monitors the GitHub Actions ecosystem. That reduces update toil but does not make tags immutable or establish compatibility.

## Inputs and outputs

### Inputs

- the checked-out triggering revision;
- GitHub event and changed-path metadata;
- repository-owned Make targets, validators, tests, fixtures, packages, and scripts;
- schemas, contracts, policies, source descriptors, registers, candidates, and release objects when the job is explicitly a verifier;
- network dependencies only when the workflow declares and justifies them.

Treat submitted code, Markdown, issue text, PR metadata, downloaded data, caches, and artifacts as untrusted input.

### Outputs

| Output | Accepted role | Limit |
|---|---|---|
| Check conclusion | Review or branch-protection signal | Not release approval or publication. |
| Log/annotation | Diagnostic context | Must not disclose secrets or sensitive data. |
| JUnit, lint, scan, or QA report | Reviewer aid | Not canonical evidence or proof by location alone. |
| Uploaded artifact | Temporary reviewer aid | Admission into a governed data/release home requires a separate transition. |
| Hold/skip summary | Honest readiness outcome | Must not be named or described as completed enforcement. |
| Candidate receipt/proof/release output | Review input | Remains candidate until validated and approved by its owning process. |

## Workflow authoring contract

1. Use stable, unique workflow names and job ids.
2. Declare least-privilege permissions at workflow level and narrow further at job level when needed.
3. Prefer `pull_request` for untrusted contributions; do not introduce `pull_request_target` without a dedicated threat model and approval.
4. Use GitHub-hosted runners unless a reviewed self-hosted boundary is required.
5. Call repository-owned commands instead of embedding policy, validators, or domain logic in YAML.
6. Keep default CI deterministic and no-network where practical; pin runtime and dependency versions.
7. Make holds, skips, partial coverage, and missing prerequisites visible in job summaries.
8. Do not let diagnostic `|| true` or `continue-on-error` convert the governing failure into success.
9. Keep public clients behind governed APIs and keep watchers and ordinary CI non-publishing.
10. Coordinate workflow/job renames with branch protection and rollback planning.

### Required negative checks

Where relevant, include deterministic tests for:

- malformed or unsupported input;
- missing evidence and cite-or-abstain behavior;
- policy denial and restricted fields;
- exact sensitive-location leakage;
- direct public reads from canonical/internal stores;
- watcher or CI attempts to publish;
- stale, superseded, quarantined, or withdrawn state;
- invalid receipt, proof, manifest, rollback, or correction linkage;
- secret-bearing logs and artifact over-retention.

## Validation

### Workflow syntax

```bash
actionlint .github/workflows/*.yml
git diff --check
```

Use a YAML 1.2-aware parser when `actionlint` is unavailable; YAML 1.1 parsers can misinterpret the GitHub Actions `on` key.

### Repository behavior

Run only established commands applicable to the changed workflow. Examples currently referenced by this subtree include:

```bash
make validate
make schemas
make test
make governed-api-smoke
make boundary-guards-ci
```

Inspect a target before running it. A Make target that only echoes `TODO` is not validation.

### Documentation and inventory

- verify all 41 files are classified exactly once;
- verify action-ref and permission counts from the proposed head;
- verify relative links and fragments;
- verify balanced code fences, alerts, tables, and final newline;
- record checks as `PASS`, `FAIL`, `PARTIAL`, `NOT RUN`, `NOT APPLICABLE`, or `UNKNOWN`.

## Review and rollback

Workflow changes require review from the current CODEOWNERS route and from the affected subsystem, governance, policy, release, or security owner when relevant. The author must not treat a self-generated check as independent approval.

Rollback should identify:

1. the workflow commit to revert;
2. any branch-protection check-name coupling;
3. caches, artifacts, comments, or external effects to invalidate;
4. the validation set to rerun;
5. whether any release or public artifact referenced the withdrawn result.

## Open verification items

- **NEEDS VERIFICATION** — required checks, rulesets, and exact branch-protection coupling.
- **NEEDS VERIFICATION** — current workflow run results, failure causes, logs, and artifact retention.
- **NEEDS VERIFICATION** — repository and organization default token permissions.
- **NEEDS VERIFICATION** — whether every path filter covers the intended implementation and documentation surfaces.
- **NEEDS VERIFICATION** — whether the current hold/readiness job names could be mistaken for substantive enforcement in branch protection.
- **NEEDS VERIFICATION** — whether action SHA pinning will be adopted and enforced.
- **NEEDS VERIFICATION** — complete CI/runtime policy-bundle parity and proof/release closure.

## Changelog

| Date | Version | Change |
|---|---|---|
| 2026-07-22 | v0.3 | Replaced the stale 34-stub/7-command snapshot with the complete 41-file inventory; reconciled maturity groups, explicit permissions, action refs, and the removal of prior OIDC drift. |
| 2026-07-17 | v0.2 | Added the first repository-grounded inventory from indexed searches. |
| 2026-07-08 | v0.1 | Established the workflow governance README. |

[Back to top](#top)
