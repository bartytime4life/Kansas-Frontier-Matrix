<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/github-workflows-readme
title: .github/workflows README
type: README
version: v0.4
status: draft; repository-grounded workflow governance reference
owners: ["@bartytime4life"]
created: 2026-07-08
updated: 2026-07-23
policy_label: public; github-actions; workflow-governance; fail-closed; non-publisher
owning_root: .github/
responsibility: GitHub Actions orchestration, trigger and permission boundaries, check-name stability, and CI maturity disclosure
truth_posture: cite-or-abstain; a workflow file, green job, commit, or pull request is not release or publication authority
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  read_ref: main
  read_commit: f93357688c0178e90db7cb976798ef998995d009
  workflow_inventory_snapshot: 1180cf7ec53d5acbbb859a39d93c1d129ec83df9
  documented_workflow_files: 41
  inventory_method: complete tracked-tree inspection and static workflow review recorded in v0.3
related:
  - ../README.md
  - ../CODEOWNERS
  - ../PULL_REQUEST_TEMPLATE.md
  - ../../CONTRIBUTING.md
  - ../../SECURITY.md
  - ../../Makefile
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/ai-build-operating-contract.md
  - ../../docs/adr/README.md
  - ../../tools/validators/README.md
  - ../../policy/
  - ../../schemas/
  - ../../contracts/
  - ../../tests/
  - ../../fixtures/
  - ../../release/
notes:
  - "The current README bytes were inspected at main@f93357688c0178e90db7cb976798ef998995d009."
  - "The detailed 41-file workflow inventory and static findings remain pinned to 1180cf7ec53d5acbbb859a39d93c1d129ec83df9 until a new complete inventory is generated."
  - "Workflow maturity groups describe inspected files and steps; they do not certify current run success, branch protection, release readiness, or KFM publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `.github/workflows/`

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Inventory snapshot: 41 workflows](https://img.shields.io/badge/inventory%20snapshot-41%20workflows-1f6feb?style=flat-square)](#complete-workflow-inventory)
[![Permissions snapshot: explicit](https://img.shields.io/badge/permissions%20snapshot-41%2F41%20explicit-15803d?style=flat-square)](#trigger-permission-and-workflow-threat-preflight)
[![Publisher: no](https://img.shields.io/badge/publisher-no-b91c1c?style=flat-square)](#authority-level)
[![Truth posture: cite or abstain](https://img.shields.io/badge/truth-cite--or--abstain-8250df?style=flat-square)](../../docs/doctrine/ai-build-operating-contract.md)

> GitHub Actions orchestration for repository-owned checks, bounded automation, and explicit readiness holds. Workflow YAML may invoke tools and report outcomes; it does not become policy, evidence, review, release, or publication authority.

> [!IMPORTANT]
> A green workflow, `WORKFLOW_HOLD`, skip, static-readiness pass, and substantive validator pass are different outcomes. Names and summaries must never imply more maturity than the executed steps establish.

## Navigation

- [Purpose](#purpose)
- [Authority level](#authority-level)
- [Status](#status)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Validation](#validation)
- [Review burden](#review-burden)
- [Related folders](#related-folders)
- [ADRs](#adrs)
- [Last reviewed](#last-reviewed)
- [Complete workflow inventory](#complete-workflow-inventory)
- [Trigger, permission, and workflow-threat preflight](#trigger-permission-and-workflow-threat-preflight)
- [External action inventory](#external-action-inventory)
- [Workflow authoring contract](#workflow-authoring-contract)
- [Rollback and correction](#rollback-and-correction)
- [Open verification items](#open-verification-items)
- [Changelog](#changelog)

## Purpose

This subtree answers one bounded operational question:

> Which GitHub-hosted jobs run for a repository event, with which permissions and inputs, and what review signal do they produce?

It supports maintainers, reviewers, CI/tooling stewards, domain owners, policy reviewers, release stewards, security reviewers, and agents changing workflow orchestration.

The subtree exists to make triggers, path filters, permissions, runners, commands, dependencies, check names, failure behavior, and rollback coupling inspectable. It is not a general-purpose home for repository logic.

## Authority level

**Authority class:** implementation-bearing orchestration under the canonical `.github/` responsibility root.

| Concern | Authority owner | Workflow role |
|---|---|---|
| Trigger, path filters, job graph, runner, token permissions, concurrency, timeout, cache use, artifact retention, and check name | `.github/workflows/` | Own GitHub Actions orchestration. |
| Validator and domain behavior | `tools/`, `packages/`, `pipelines/`, applications | Invoke repository-owned commands; do not reproduce their logic in YAML. |
| Policy decisions | `policy/` | Evaluate reviewed policy inputs; never create inline policy authority. |
| Object meaning and machine shape | `contracts/`, `schemas/` | Validate without redefining. |
| Expected behavior | `tests/`, `fixtures/` | Execute deterministic positive and negative cases. |
| Evidence, receipts, proofs, catalogs, and releases | governed `data/` and `release/` lanes | Emit only candidates or verification aids through accepted tools and transitions. |
| Branch protection and required checks | GitHub repository rules | Workflow names may be coupled to rules, but workflow files do not define those rules. |
| KFM publication | governed promotion and release process | Never inferred from a workflow, artifact upload, commit, merge, or GitHub Release alone. |

The workflow layer is a **non-publisher**. Watchers, drift detectors, documentation checks, release dry-runs, and promotion-gate simulations may propose or verify work; they must not silently promote candidates or write public truth.

## Status

### Current document state

- **CONFIRMED:** this README was read on `main@f93357688c0178e90db7cb976798ef998995d009`.
- **CONFIRMED / LINEAGE:** the detailed static inventory below was generated from `main@1180cf7ec53d5acbbb859a39d93c1d129ec83df9` and documented 41 tracked `.yml` workflows.
- **NEEDS VERIFICATION:** whether workflow files, action references, permissions, triggers, or maturity groups changed between the inventory snapshot and the current read commit.
- **UNKNOWN:** current branch-protection coupling, recent workflow conclusions, logs, organization defaults, artifact retention, and runtime behavior unless separately inspected.

### Documented inventory findings

| Finding | Snapshot status | Interpretation |
|---|---|---|
| Workflow inventory | **CONFIRMED at inventory commit: 41 tracked `.yml` files** | Complete for the pinned tree. No `.yaml` workflow was recorded. |
| Explicit permissions | **CONFIRMED at inventory commit: 41/41** | Every inspected workflow declared a top-level permissions boundary. |
| Privileged PR trigger | **CONFIRMED absent at inventory commit** | No active `pull_request_target` trigger key. |
| Runner trust | **CONFIRMED GitHub-hosted at inventory commit** | No `self-hosted` occurrence. |
| Direct secret expressions | **CONFIRMED absent at inventory commit** | No direct `secrets.*` occurrence; repository and organization settings remain external. |
| Write scopes | **CodeQL only at inventory commit** | `security-events: write` supported code-scanning upload; ordinary repository write grants were absent. |
| External action pinning | **Version tags, not immutable SHAs** | Reviewable and Dependabot-visible, but not immutable. |
| Branch protection | **NEEDS VERIFICATION** | Static workflow inspection cannot establish required checks or rulesets. |
| Workflow execution | **NEEDS VERIFICATION** | Inventory does not establish recent success, failure, or readiness. |

## What belongs here

- GitHub Actions workflow files using `.yml` or a repository-approved equivalent;
- event triggers and changed-path filters;
- workflow and job permissions;
- runner, container, service, timeout, concurrency, cache, and artifact orchestration;
- calls to repository-owned validators, tests, builders, scanners, and dry-run commands;
- explicit job summaries that distinguish pass, fail, hold, skip, and partial coverage;
- narrowly scoped workflow comments explaining security or compatibility constraints;
- reusable workflow definitions when the repository adopts them;
- workflow-specific documentation in this README.

## What does not belong here

- semantic contract definitions, JSON Schemas, policy rules, domain algorithms, or reusable validator logic;
- canonical source data, evidence, proofs, receipts, release manifests, rollback cards, or publication records;
- secrets, credentials, signed URLs, private endpoints, or sensitive data;
- application logic embedded in YAML merely to avoid placing it in `tools/`, `packages/`, `pipelines/`, or an application;
- workflows created solely to obtain a green badge;
- direct watcher-to-default-branch, watcher-to-release, or CI-to-published mutation paths;
- `pull_request_target` use without a dedicated threat model, least-privilege design, and explicit approval;
- unbounded network fetches where deterministic fixtures can prove the behavior;
- duplicated policy or validation implementations that can drift from canonical owners.

## Inputs

- the checked-out triggering revision;
- GitHub event, actor, ref, and changed-path metadata;
- repository-owned Make targets, validators, tests, fixtures, packages, pipelines, and scripts;
- schemas, contracts, policies, source descriptors, registers, candidates, and release objects when a job is explicitly a verifier;
- caches and prior workflow artifacts only when their trust, keys, retention, and poisoning risks are understood;
- network dependencies only when the workflow declares and justifies them.

Treat submitted code, Markdown, issue or pull-request text, metadata, downloaded content, caches, and artifacts as untrusted input.

## Outputs

| Output | Accepted role | Limit |
|---|---|---|
| Check conclusion | Review or branch-protection signal | Not release approval or publication. |
| Log, annotation, or job summary | Diagnostic and maturity context | Must not disclose secrets, private data, or protected locations. |
| JUnit, lint, scan, or QA report | Reviewer aid | Not canonical evidence or proof by location alone. |
| Uploaded workflow artifact | Temporary reviewer aid | Admission into governed data or release homes requires a separate transition. |
| Hold or skip summary | Honest readiness outcome | Must not be named or described as completed enforcement. |
| Candidate receipt, proof, or release output | Review input | Remains candidate until validated and approved by its owning process. |
| Dependency or security finding | Remediation input | Does not self-authorize a fix, waiver, merge, or release. |

## Validation

### Workflow source checks

```bash
actionlint .github/workflows/*.yml
git diff --check
```

Use a YAML 1.2-aware parser when `actionlint` is unavailable; YAML 1.1 parsers can misinterpret the GitHub Actions `on` key.

### Repository behavior checks

Run only established commands applicable to the changed workflow. Commands referenced by this subtree include:

```bash
make validate
make schemas
make test
make governed-api-smoke
make boundary-guards-ci
```

Inspect the target before relying on it. A Make target that only echoes `TODO`, a skipped job, or a hold condition is not substantive validation.

### Documentation and inventory checks

- verify every tracked workflow is classified exactly once;
- regenerate workflow, action-reference, trigger, permission, runner, secret-expression, and write-scope counts from the proposed head;
- verify all relative links and fragments;
- verify balanced code fences, alerts, tables, HTML anchors, and final newline;
- distinguish current findings from pinned historical snapshots;
- record checks as `PASS`, `FAIL`, `PARTIAL`, `PENDING`, `NOT RUN`, `NOT APPLICABLE`, or `UNKNOWN`.

### Required negative checks

Where relevant, include deterministic tests for:

- malformed or unsupported input;
- missing evidence and cite-or-abstain behavior;
- policy denial and restricted fields;
- exact sensitive-location leakage;
- direct public reads from canonical or internal stores;
- watcher or CI attempts to publish;
- stale, superseded, quarantined, withdrawn, or corrected state;
- invalid receipt, proof, manifest, rollback, or correction linkage;
- secret-bearing logs, unsafe caches, and artifact over-retention.

## Review burden

Workflow changes require review through the current [`CODEOWNERS`](../CODEOWNERS) route and from the affected subsystem, governance, policy, release, or security owner when relevant.

Review must cover more than YAML syntax:

1. trigger and changed-path correctness;
2. untrusted-input reachability;
3. token, secret, OIDC, and network exposure;
4. action provenance and pinning posture;
5. command maturity and failure masking;
6. check-name stability and branch-protection coupling;
7. artifact and cache retention;
8. non-publisher and rollback boundaries.

The author must not treat a self-generated check, badge, receipt, or pull request as independent approval.

## Related folders

| Path | Relationship |
|---|---|
| [`.github/`](../README.md) | Parent GitHub governance and collaboration surface. |
| [`tools/`](../../tools/README.md) | Repository-wide validators, builders, and checkers invoked by workflows. |
| [`tests/`](../../tests/README.md) and [`fixtures/`](../../fixtures/README.md) | Deterministic positive, negative, and regression proof. |
| [`contracts/`](../../contracts/README.md) and [`schemas/`](../../schemas/README.md) | Semantic meaning and machine-checkable shape. |
| [`policy/`](../../policy/README.md) | Allow, deny, restrict, hold, and abstain decisions. |
| [`pipelines/`](../../pipelines/README.md) and [`pipeline_specs/`](../../pipeline_specs/README.md) | Executable and declarative pipeline behavior. |
| [`release/`](../../release/README.md) | Promotion, release, correction, withdrawal, and rollback authority. |
| [`SECURITY.md`](../../SECURITY.md) | Vulnerability reporting and repository security posture. |
| [`CONTRIBUTING.md`](../../CONTRIBUTING.md) | Contributor workflow and review expectations. |

## ADRs

No workflow-specific ADR is asserted here without a verified accepted record.

Before a workflow change bends a trust or placement invariant, inspect [`docs/adr/`](../../docs/adr/README.md). A dedicated ADR or equivalent approved decision is expected for materially consequential changes such as:

- enabling `pull_request_target`;
- introducing self-hosted runners;
- granting ordinary repository, deployment, package, or identity-token write scopes;
- creating a workflow-controlled publication path;
- changing required check names or branch-protection contracts;
- creating a parallel policy, schema, receipt, proof, catalog, or release authority in workflow YAML.

## Last reviewed

| Field | Value |
|---|---|
| README content read | 2026-07-23 |
| Read ref | `main` |
| Read commit | `f93357688c0178e90db7cb976798ef998995d009` |
| Detailed workflow inventory snapshot | `1180cf7ec53d5acbbb859a39d93c1d129ec83df9` |
| Inventory refresh status | **NEEDS VERIFICATION** against the proposed head before relying on counts as current |

## Complete workflow inventory

The groups below preserve the repository-grounded v0.3 inventory. They describe the inspected code and status comments at the inventory commit; they are not release-readiness grades.

### Explicit greenfield, non-enforcing scaffolds

- [`accessibility.yml`](accessibility.yml)
- [`citation-validation.yml`](citation-validation.yml)
- [`ui-build.yml`](ui-build.yml)

These files declared proposed greenfield scaffolds and visible TODO or hold behavior. They must not be required as proof that accessibility, citation resolution, or the UI build is implemented.

### Bounded domain readiness and governed holds

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

These jobs intentionally expose missing executables, fixtures, proof closure, or runtime readiness. A hold is a truthful finite outcome, not a passing implementation claim.

### Command-bearing and partial gates

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

Read the exact steps and job summaries before relying on any workflow as a merge gate. “Command-bearing” does not mean complete, current, or production-ready.

## Trigger, permission, and workflow-threat preflight

Before changing or relying on a workflow, record:

| Question | Required answer |
|---|---|
| Event | Which of `pull_request`, `push`, `workflow_dispatch`, `schedule`, `workflow_call`, or `workflow_run` triggers it? |
| Path scope | Which changed paths activate it, and which expected paths are excluded? |
| Untrusted input | Can fork code, issue text, pull-request metadata, artifacts, caches, or downloaded content influence execution? |
| Token | What is the smallest explicit `permissions` set? |
| Secrets/OIDC | Why is identity or secret access required, and is it reachable from untrusted code? |
| Runner | Is the runner GitHub-hosted or self-hosted, and what trust boundary follows? |
| Network | Which registries or endpoints are contacted, and can deterministic fixtures replace them? |
| Dependency | Is every external action necessary, maintained, licensed, and pinned according to repository policy? |
| Output | Check signal, log, report, artifact, candidate receipt, or governed object? |
| Failure | Does failure stay visible, or can `continue-on-error`, `if: always()`, or `|| true` mask the governing result? |
| Check name | Is the workflow or job name coupled to branch protection? |
| Rollback | How can the workflow be disabled or reverted without weakening unrelated gates? |

### Static threat findings at the inventory snapshot

| Threat surface | Finding |
|---|---|
| `pull_request_target` | No active trigger key; one safety comment named it without enabling it. |
| Self-hosted runner | No occurrence. |
| Direct secret expressions | No `secrets.*` occurrence. |
| Ordinary write permissions | No `contents`, `issues`, `pull-requests`, `packages`, `deployments`, or `id-token` write grant. |
| Code scanning | [`codeql.yml`](codeql.yml) granted `security-events: write`; re-review if its event or trust boundary changes. |
| External action immutability | Action refs used version tags, not immutable commit SHAs. |
| Publication path | No file-presence claim authorized publication; every invoked command still requires inspection. |

## External action inventory

Snapshot at `1180cf7ec53d5acbbb859a39d93c1d129ec83df9`:

| Action reference | Occurrences | Pinning posture |
|---|---:|---|
| `actions/checkout@v7` | 88 | Major tag; mutable. |
| `actions/setup-python@v7` | 54 | Major tag; mutable. |
| `actions/setup-node@v7.0.0` | 3 | Release tag; mutable. |
| `actions/upload-artifact@v7` | 1 | Major tag; mutable. |
| `github/codeql-action/init@v4` | 1 | Major tag; mutable. |
| `github/codeql-action/analyze@v4` | 1 | Major tag; mutable. |

Dependabot monitoring reduces update toil but does not make tags immutable, establish compatibility, or replace review of changelogs and runtime requirements.

## Workflow authoring contract

1. Use stable, unique workflow names and job identifiers.
2. Declare least-privilege permissions at workflow level and narrow further at job level when needed.
3. Prefer `pull_request` for untrusted contributions; do not introduce `pull_request_target` without a dedicated threat model and approval.
4. Use GitHub-hosted runners unless a reviewed self-hosted boundary is required.
5. Call repository-owned commands instead of embedding policy, validators, or domain logic in YAML.
6. Keep default CI deterministic and no-network where practical; pin runtimes and dependencies according to repository policy.
7. Make holds, skips, partial coverage, and missing prerequisites visible in names and job summaries.
8. Do not let diagnostic `|| true`, `continue-on-error`, or unconditional follow-up steps convert governing failure into success.
9. Keep public clients behind governed APIs and keep watchers and ordinary CI non-publishing.
10. Coordinate workflow and job renames with branch protection, documentation, and rollback planning.
11. Bound caches and artifacts by content, trust, key, retention, and sensitivity.
12. Preserve correction and supersession visibility; do not silently remove a gate that public or review processes rely on.

## Rollback and correction

A workflow rollback should identify:

1. the workflow commit to revert;
2. any required-check or branch-protection coupling;
3. caches, artifacts, comments, deployments, or external effects to invalidate;
4. the validation set to rerun;
5. whether any release, report, badge, or public artifact referenced the withdrawn result;
6. whether the README inventory or maturity classification must be corrected.

Before merge, the normal rollback is to revert or close the unmerged workflow change without weakening unrelated checks. After merge, use a transparent revert commit or follow-up pull request; never rewrite shared history.

## Open verification items

- **NEEDS VERIFICATION** — regenerate the complete workflow inventory against the proposed head and reconcile any delta from the 41-file snapshot.
- **NEEDS VERIFICATION** — required checks, rulesets, and exact branch-protection coupling.
- **NEEDS VERIFICATION** — current workflow run results, failure causes, logs, and artifact retention.
- **NEEDS VERIFICATION** — repository and organization default token permissions.
- **NEEDS VERIFICATION** — whether every path filter covers intended implementation and documentation surfaces.
- **NEEDS VERIFICATION** — whether hold and readiness job names could be mistaken for substantive enforcement.
- **NEEDS VERIFICATION** — whether immutable action SHA pinning will be adopted and enforced.
- **NEEDS VERIFICATION** — complete CI/runtime policy-bundle parity and proof/release closure.
- **NEEDS VERIFICATION** — whether workflow-generated artifacts contain sensitive data or outlive their review purpose.

## Changelog

| Date | Version | Change |
|---|---|---|
| 2026-07-23 | v0.4 | Aligned the README with the canonical-root contract; separated current document evidence from the pinned workflow inventory; added belongs/non-belongs, review burden, related-folder, ADR, threat-preflight, rollback, accessibility, and anti-overclaim guidance. |
| 2026-07-22 | v0.3 | Replaced the stale 34-stub/7-command snapshot with the complete 41-file inventory; reconciled maturity groups, explicit permissions, action refs, and removal of prior OIDC drift. |
| 2026-07-17 | v0.2 | Added the first repository-grounded inventory from indexed searches. |
| 2026-07-08 | v0.1 | Established the workflow governance README. |

[Back to top](#top)
