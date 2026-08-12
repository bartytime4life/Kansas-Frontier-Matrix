<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/github-workflows-readme
title: .github/workflows README
type: README
version: v0.16
status: draft; repository-grounded workflow governance reference; current filename count; static guardrail audit implemented; hosted behavior bounded
owners: ["@bartytime4life"]
created: 2026-07-08
updated: 2026-08-12
policy_label: public; github-actions; workflow-governance; fail-closed; non-publisher
owning_root: .github/
responsibility: GitHub Actions orchestration, trigger and permission boundaries, check-name stability, CI maturity disclosure, and workflow inventory accountability
truth_posture: cite-or-abstain; a workflow file, green job, commit, or pull request is not release or publication authority
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  read_ref: main
  read_commit: c2594045856765c8b155020d9cd2e95b5db873f2
  workflows_tree: 52ca3751c26e4680411af8ce056fc2757427030c
  readme_prior_blob: e88e3a5d4b76d02edc55885274a21523e39ae044
  current_workflow_files: 424
  workflow_security_rules: 20
  workflow_security_findings_after_hardening: 0
  current_workflow_extension: .yml
  current_workflow_readme_files: 1
  prior_detailed_inventory: 44 workflow files at v0.14; retained in Git history; superseded as current inventory
related:
  - ../README.md
  - ../CODEOWNERS
  - ../PULL_REQUEST_TEMPLATE.md
  - ../../CONTRIBUTING.md
  - ../../SECURITY.md
  - ../../Makefile
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/doctrine/ai-build-operating-contract.md
  - ../../docs/adr/README.md
  - ../../tools/validators/README.md
  - ../../tests/README.md
  - ../../fixtures/README.md
  - ../../policy/README.md
  - ../../schemas/README.md
  - ../../contracts/README.md
  - ../../release/README.md
notes:
  - "The 424-file count is exact for the pinned Git tree. This edition adds a deterministic twenty-rule static ratchet but does not claim current hosted results, ruleset coupling, runtime safety, or complete behavioral maturity."
  - "The v0.14 detailed forty-four-workflow classification and action inventory remain historical process evidence in Git history, not current-tree evidence."
  - "Workflow filenames and green checks are orchestration evidence only; they do not create policy, review, release, lifecycle, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `.github/workflows/`

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status-and-evidence-boundary)
[![Current inventory: 424 workflows](https://img.shields.io/badge/current%20inventory-424%20workflows-1f6feb?style=flat-square)](#current-inventory-boundary)
[![Static ratchet: 20 rules](https://img.shields.io/badge/static%20ratchet-20%20rules-1f883d?style=flat-square)](#current-inventory-boundary)
[![Publisher: no](https://img.shields.io/badge/publisher-no-b91c1c?style=flat-square)](#authority-level)
[![Truth: cite or abstain](https://img.shields.io/badge/truth-cite--or--abstain-8250df?style=flat-square)](../../docs/doctrine/ai-build-operating-contract.md)

> GitHub Actions orchestration for repository-owned checks, bounded automation, and explicit readiness outcomes. Workflow YAML may invoke tools and report results; it does not become policy, evidence, review, release, lifecycle-transition, or publication authority.

> [!IMPORTANT]
> A green workflow, governed hold, skip, static-readiness pass, and substantive validator pass are different outcomes. Names and summaries must not imply more maturity than the executed steps establish.

## Navigation

- [Purpose](#purpose)
- [Authority level](#authority-level)
- [Status and evidence boundary](#status-and-evidence-boundary)
- [Current inventory boundary](#current-inventory-boundary)
- [Workflow families](#workflow-families)
- [Historical inventory boundary](#historical-inventory-boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Trigger, permission, and threat preflight](#trigger-permission-and-threat-preflight)
- [Validation](#validation)
- [Workflow authoring contract](#workflow-authoring-contract)
- [Review burden](#review-burden)
- [Related folders](#related-folders)
- [ADRs](#adrs)
- [Rollback and correction](#rollback-and-correction)
- [Open verification items](#open-verification-items)
- [Changelog](#changelog)

## Purpose

This subtree answers one bounded operational question:

> Which GitHub-hosted jobs run for a repository event, with which declared orchestration, and what review signal do they produce?

It exists to make triggers, path filters, permissions, runners, commands, dependencies, check names, failure behavior, caches, artifacts, and rollback coupling inspectable. Reusable validator, policy, domain, pipeline, release, and application logic stays in its owning root and is invoked from workflow YAML.

## Authority level

**Authority class:** implementation-bearing orchestration under the canonical `.github/` platform-integration root.

| Concern | Authority owner | Workflow role |
|---|---|---|
| Trigger, path filters, job graph, runner, token permissions, concurrency, timeout, cache, artifact orchestration, and check name | `.github/workflows/` | Own GitHub Actions orchestration. |
| Validator and domain behavior | `tools/`, `packages/`, `pipelines/`, applications | Invoke repository-owned commands; do not duplicate their logic in YAML. |
| Policy decisions | `policy/` | Evaluate reviewed policy inputs; never create inline policy authority. |
| Object meaning and machine shape | `contracts/`, `schemas/` | Validate without redefining. |
| Expected behavior | `tests/`, `fixtures/` | Execute deterministic positive, negative, and regression cases. |
| Evidence, receipts, proofs, catalogs, and data lifecycle | governed `data/` lanes | Emit only candidates or reviewer aids unless a separate governed transition admits them. |
| Promotion, release, correction, withdrawal, and rollback | `release/` | Verify or dry-run; do not approve or execute authority by workflow success alone. |
| Branch protection and required checks | GitHub repository rulesets | Workflow and job names may be coupled to rules, but YAML files do not define those rules. |

The workflow layer is a **non-publisher**. Watchers, drift detectors, documentation checks, promotion simulations, and release dry-runs may propose or verify work; they must not silently write public truth or change lifecycle state.

## Status and evidence boundary

This edition was prepared against `main@c2594045856765c8b155020d9cd2e95b5db873f2` and workflow tree `52ca3751c26e4680411af8ce056fc2757427030c`.

**CONFIRMED for that snapshot:**

- the workflow subtree contains one README and **424 tracked `.yml` workflow files**;
- the old v0.14 README blob remains in Git history;
- the current tree includes rapidly expanded domain, source, evidence, policy, review, artifact, map, runtime, and governance lanes;
- the proposed branch keeps the workflow-file count stable while adding bounded static enforcement; it changes no GitHub repository setting.

**NEEDS VERIFICATION beyond the bounded static scan of the complete 424-file tree:**

- every trigger and path filter;
- every permission and write scope;
- `pull_request_target`, `workflow_run`, privileged dispatch, and schedule exposure;
- self-hosted runners, containers, services, secrets, OIDC, network access, caches, and artifacts;
- external action provenance and immutable pinning;
- duplicate or misleading workflow and job names;
- current hosted conclusions, required-check coupling, and failure causes;
- whether each command is substantive, partial, held, skipped, or placeholder behavior.

A filename proves only that bytes exist. It does not establish that the lane is safe, required, current, complete, or production-ready.

## Current inventory boundary

| Inventory fact | Current value | Interpretation |
|---|---:|---|
| Workflow files | **424** | Exact count of tracked `.yml` files in the pinned tree. |
| Workflow README files | **1** | This file. |
| Alternative `.yaml` workflow files | **0 observed** | The pinned workflow tree contains `.yml` files and this README. |
| Prior documented workflow set | **44** | Historical v0.14 classification; no longer a complete current inventory. |
| Net growth since prior detailed snapshot | **380** | Maintenance and audit pressure, not maturity. |
| Deterministic static guardrails | **20** | Local source checks with exact inherited-drift ratcheting; not hosted or runtime proof. |
| Proposed-head static result | **PASS: 424 workflows, 0 findings, 0 waivers** | Reproducible local source result; hosted execution and required-check state remain unverified. |
| Complete current behavioral audit | **Not performed** | Hosted conclusions, rulesets, runtime behavior, and semantic maturity remain `NEEDS VERIFICATION`. |

The count should be regenerated from the Git tree whenever workflows change. A future repository-owned inventory validator is preferred over manual arithmetic.

## Workflow families

The current filenames show these broad orchestration families. The grouping is navigational only; it does not assign authority or certify behavior.

| Family | Examples visible in the pinned tree | Review focus |
|---|---|---|
| Repository and documentation control | `repository-control.yml`, `docs-control-plane.yml`, `docs-meta-block.yml`, `docs-document-graph.yml`, `docs-stale-scan.yml`, `link-check.yml` | Trusted base, metadata scope, freshness semantics, local-only checks, ruleset coupling. |
| Domain lanes | `domain-hydrology.yml`, `domain-soil.yml`, `domain-fauna.yml`, `domain-geology.yml`, and other `domain-*` workflows | Fixture polarity, source-role boundaries, domain-specific holds, public-safety limits. |
| Source, evidence, and identity | `source-descriptor-validate.yml`, `source-event-envelope.yml`, `evidence-resolver.yml`, `spec-hash.yml`, `trace-receipt-link.yml` | Source authority, deterministic identity, evidence closure, no live-source overreach. |
| Policy, review, and obligations | `policy-test.yml`, `policy-obligation-set.yml`, `review-authority-binding.yml`, `implementation-decision-review.yml` | Policy inputs, reviewer identity, self-review denial, obligation reduction, fail-closed behavior. |
| Promotion, release, proof, and rollback | `promotion-gate.yml`, `promotion-receipt.yml`, `release-dry-run.yml`, `proof-pack-closure.yml`, `rollback-drill.yml` | State-transition boundaries, synthetic-vs-live distinction, signatures, correction and rollback. |
| Map, runtime, UI, and delivery carriers | `maplibre-perf-governance.yml`, `map-context-envelope.yml`, `runtime-evidence-resolution.yml`, `ui-build.yml`, `pmtiles-attestation.yml` | Governed API boundary, renderer-as-carrier, artifact integrity, performance and public exposure. |
| Artifact and catalog projections | `artifact-delta-receipt.yml`, `catalog-closure-packet.yml`, `catalog-trust-extension.yml`, `openlineage-run-event-projection.yml` | Candidate-vs-authority separation, provenance, catalog closure, receipt/proof distinctions. |

Review the exact workflow before relying on any example above. Similar names do not imply equivalent triggers, permissions, commands, or maturity.

## Historical inventory boundary

Version v0.14 documented a detailed **44-workflow** classification, selected command semantics, and an external-action inventory. That material was useful for its pinned snapshots, but the current tree is more than nine times larger.

This edition therefore:

- preserves v0.14 in Git history at prior blob `e88e3a5d4b76d02edc55885274a21523e39ae044`;
- supersedes its 44-file count and “complete workflow inventory” label as current evidence;
- does not copy stale per-workflow conclusions onto 380 additional files;
- retains the underlying authoring, threat-model, validation, non-publisher, and rollback rules;
- enforces a bounded 424-workflow static ratchet while keeping hosted behavior an explicit verification item.

Historical evidence remains citable at its pinned commit. It must not be silently presented as current-main behavior.

## What belongs here

- GitHub Actions workflow files using the repository-approved `.yml` extension;
- event triggers and changed-path filters;
- workflow and job permissions;
- runner, container, service, timeout, concurrency, cache, and artifact orchestration;
- calls to repository-owned validators, tests, builders, scanners, and dry-run commands;
- explicit job summaries that distinguish pass, fail, hold, skip, partial coverage, and error;
- reusable workflow definitions when actual reuse is established;
- workflow-specific documentation in this README.

## What does not belong here

- semantic contracts, JSON Schemas, normative policy rules, domain algorithms, or reusable validator logic;
- canonical source data, evidence, proofs, receipts, release manifests, rollback cards, or publication records;
- secrets, credentials, signed URLs, private endpoints, or sensitive data;
- application logic embedded in YAML merely to avoid its owning implementation root;
- workflows created solely to obtain a green badge;
- direct watcher-to-default-branch, watcher-to-release, or CI-to-published mutation paths;
- privileged event use without a dedicated threat model, least privilege, and explicit approval;
- unbounded network fetches where deterministic fixtures can prove the behavior;
- duplicated policy or validation implementations that can drift from canonical owners.

## Inputs

- the checked-out triggering revision;
- GitHub event, actor, ref, and changed-path metadata;
- repository-owned Make targets, validators, tests, fixtures, packages, pipelines, and scripts;
- schemas, contracts, policies, source descriptors, registers, candidates, and release objects when a job is explicitly a verifier;
- caches and prior artifacts only when trust, keys, retention, and poisoning risks are understood;
- network dependencies only when the workflow declares and justifies them.

Treat submitted code, Markdown, issue or pull-request text, metadata, downloaded content, caches, and artifacts as untrusted input.

## Outputs

| Output | Accepted role | Limit |
|---|---|---|
| Check conclusion | Review or ruleset signal | Not release approval or publication. |
| Log, annotation, or job summary | Diagnostic and maturity context | Must not disclose secrets, private data, or protected locations. |
| JUnit, lint, scan, or QA report | Reviewer aid | Not canonical evidence or proof by location alone. |
| Uploaded workflow artifact | Temporary reviewer aid | Admission into governed data or release homes requires a separate transition. |
| Hold, skip, partial, or error summary | Honest readiness outcome | Must not be named as completed enforcement. |
| Candidate receipt, proof, catalog, or release output | Review input | Remains candidate until validated and approved by its owning process. |
| Dependency or security finding | Remediation input | Does not self-authorize a fix, waiver, merge, or release. |

## Trigger, permission, and threat preflight

Before changing or relying on a workflow, record:

| Question | Required answer |
|---|---|
| Event | Which of `pull_request`, `pull_request_target`, `push`, `workflow_dispatch`, `schedule`, `workflow_call`, or `workflow_run` triggers it? |
| Path scope | Which changed paths activate it, and which expected paths are excluded? |
| Untrusted input | Can fork code, issue text, pull-request metadata, artifacts, caches, or downloaded content influence execution? |
| Token | What is the smallest explicit `permissions` set? |
| Secrets/OIDC | Why is identity or secret access required, and is it reachable from untrusted code? |
| Runner | Is the runner GitHub-hosted or self-hosted, and what trust boundary follows? |
| Network | Which registries or endpoints are contacted, and can deterministic fixtures replace them? |
| Dependency | Is every external action necessary, maintained, licensed, and pinned according to repository policy? |
| Output | Is the output a check signal, log, report, artifact, candidate object, or governed object? |
| Failure | Can `continue-on-error`, `if: always()`, `|| true`, or conditionals mask the governing result? |
| Check name | Is the workflow or job name coupled to a current ruleset? |
| Rollback | How can the workflow be disabled or reverted without weakening unrelated gates? |

A `pull_request_target`, self-hosted runner, write token, secret/OIDC path, deployment, package publication, or lifecycle mutation is a materially higher-risk boundary and requires explicit threat review.

## Validation

### Workflow source checks

```bash
actionlint .github/workflows/*.yml
git diff --check
```

Use a YAML 1.2-aware parser when `actionlint` is unavailable; YAML 1.1 parsers can misinterpret the GitHub Actions `on` key.

### Repository behavior checks

Run only established commands applicable to the changed workflow. Representative repository commands include:

```bash
make validate
make schemas
make test
```

Inspect each target before relying on it. A Make target that only echoes a hold, a skipped job, or a non-enforcing readiness check is not substantive validation.

### Documentation and inventory checks

- regenerate workflow filename counts from the proposed head;
- verify relative links and fragments;
- verify balanced fences, alerts, tables, HTML anchors, and final newline;
- distinguish current findings from pinned historical snapshots;
- record outcomes as `PASS`, `FAIL`, `PARTIAL`, `PENDING`, `NOT RUN`, `NOT APPLICABLE`, or `UNKNOWN`;
- do not claim current action-pin, permission, or threat posture without scanning every workflow at the exact head.

### Required negative checks

Where relevant, include deterministic tests for malformed input, missing evidence, policy denial, sensitive-location leakage, direct public reads from internal stores, watcher publication attempts, stale or corrected state, invalid receipt/proof/release linkage, unsafe caches, and secret-bearing logs.

## Workflow authoring contract

1. Use stable, unique workflow names and job identifiers.
2. Declare least-privilege permissions and narrow further at job level when needed.
3. Prefer `pull_request` for untrusted contributions; use privileged triggers only with a dedicated threat model and approval.
4. Use GitHub-hosted runners unless a reviewed self-hosted boundary is required.
5. Call repository-owned commands instead of embedding policy, validators, or domain logic in YAML.
6. Keep default CI deterministic and no-network where practical; pin runtimes and dependencies according to repository policy.
7. Make holds, skips, partial coverage, errors, and missing prerequisites visible.
8. Do not let diagnostic error suppression convert governing failure into success.
9. Keep public clients behind governed APIs and keep watchers and ordinary CI non-publishing.
10. Coordinate workflow and job renames with rulesets, documentation, and rollback planning.
11. Bound caches and artifacts by content, trust, key, retention, and sensitivity.
12. Preserve correction and supersession visibility; do not silently remove a relied-upon gate.
13. Avoid one-workflow-per-idea growth when an existing bounded workflow or reusable lane can own the same responsibility safely.
14. Reconcile overlap by behavior and authority, not by filename similarity alone.

## Review burden

Workflow changes require review through the current [`CODEOWNERS`](../CODEOWNERS) route and from the affected subsystem, governance, policy, release, or security owner when relevant.

Review must cover more than YAML syntax:

1. trigger and path-filter correctness;
2. untrusted-input reachability;
3. token, secret, OIDC, and network exposure;
4. action provenance and pinning posture;
5. command maturity and failure masking;
6. check-name stability and ruleset coupling;
7. artifact and cache retention;
8. non-publisher and rollback boundaries;
9. overlap with existing workflows and whether consolidation is safer.

The author must not treat a self-generated check, badge, receipt, or pull request as independent approval.

## Related folders

| Path | Relationship |
|---|---|
| [`.github/`](../README.md) | Parent GitHub governance and collaboration surface. |
| [`tools/`](../../tools/README.md) | Repository-wide validators, builders, and checkers invoked by workflows. |
| [`tests/`](../../tests/README.md) and [`fixtures/`](../../fixtures/README.md) | Deterministic positive, negative, and regression evidence. |
| [`contracts/`](../../contracts/README.md) and [`schemas/`](../../schemas/README.md) | Semantic meaning and machine-checkable shape. |
| [`policy/`](../../policy/README.md) | Allow, deny, restrict, hold, and abstain decisions. |
| [`pipelines/`](../../pipelines/README.md) and [`pipeline_specs/`](../../pipeline_specs/README.md) | Executable and declarative pipeline behavior. |
| [`release/`](../../release/README.md) | Promotion, release, correction, withdrawal, and rollback authority. |
| [`SECURITY.md`](../../SECURITY.md) | Vulnerability reporting and repository security posture. |
| [`CONTRIBUTING.md`](../../CONTRIBUTING.md) | Contributor workflow and review expectations. |

## ADRs

Accepted ADR-0029 establishes the canonical Directory Rules authority and confirms `.github/` as the platform-integration root. It does not approve any particular workflow behavior or privileged boundary.

Inspect [`docs/adr/`](../../docs/adr/README.md) before a workflow change bends a trust or placement invariant. A dedicated accepted decision or equivalent explicit authority is expected before introducing:

- a privileged trigger or self-hosted runner;
- ordinary repository, deployment, package, or identity-token write scopes;
- a workflow-controlled publication or lifecycle-transition path;
- a required-check rename or ruleset migration;
- a parallel policy, schema, receipt, proof, catalog, or release authority in workflow YAML.

## Rollback and correction

A workflow rollback should identify:

1. the workflow commit to revert;
2. any required-check or ruleset coupling;
3. caches, artifacts, comments, deployments, or external effects to invalidate;
4. the validation set to rerun;
5. whether any release, report, badge, or public artifact referenced the withdrawn result;
6. whether this README inventory or maturity classification must be corrected.

Before merge, close or revert the unmerged workflow change without weakening unrelated checks. After merge, use a transparent revert or forward correction; never rewrite shared history.

## Open verification items

- **NEEDS VERIFICATION** — behavioral review of commands, trigger reachability, secrets/OIDC, network, caches, artifacts, and write effects beyond the twenty static rules for all 424 files.
- **NEEDS VERIFICATION** — current rulesets and exact required-check coupling.
- **NEEDS VERIFICATION** — recent hosted outcomes, failure causes, logs, rerun state, and artifact retention.
- **NEEDS VERIFICATION** — duplicate, overlapping, obsolete, or misleading workflow/check identities created during rapid growth.
- **NEEDS VERIFICATION** — commands that remain placeholders, readiness holds, or partial validation despite authoritative-sounding names.
- **NEEDS VERIFICATION** — complete policy-bundle, schema, fixture, and runtime parity.
- **NEEDS VERIFICATION** — whether workflow-generated artifacts contain sensitive data or outlive their review purpose.
- **CONFIRMED in this branch / hosted result NEEDS VERIFICATION** — a repository-owned, no-network workflow-security ratchet now emits reviewable findings without becoming policy or release authority.
- **PROPOSED consolidation** — prefer reusable validators and bounded workflows where multiple files share the same trigger, permissions, and acceptance boundary.

## Changelog

| Date | Version | Change |
|---|---|---|
| 2026-08-12 | v0.16 | Re-pinned the subtree to `main@c259404…`; recorded the exact 424-workflow count; added a deterministic twenty-rule workflow-security ratchet with inherited-drift accounting; and kept hosted conclusions, ruleset state, and runtime maturity explicitly unverified. |
| 2026-08-08 | v0.15 | Re-pinned the subtree to `main@d4586ec…`; recorded the exact 191-workflow count; superseded the 44-file classification as current inventory while preserving it in Git history; separated filename facts from unverified per-workflow behavior; and retained the non-publisher, threat-preflight, validation, review, and rollback contracts. |
| 2026-08-03 | v0.14 | Reconciled promotion workflow documentation with a bounded fixture-only ReviewRecord candidate inside the prior 44-workflow snapshot. |
| 2026-08-02 | v0.13 | Added a deterministic finite-envelope shape proof while preserving mock-runtime and composed-E2E holds. |
| 2026-08-02 | v0.12 | Added focused `GENERATED_RECEIPT` validation to the validator suite without changing publication authority. |
| 2026-08-01 | v0.11 | Replaced then-current floating executable action references with reviewed immutable commits for the pinned 44-workflow-era snapshot. |
| 2026-08-01 | v0.10 | Extended the bounded no-network documentation link checker. |
| 2026-08-01 | v0.9 | Added shared JSON Schema runner tests and aligned negative-fixture diagnostics. |
| 2026-07-31 | v0.8 | Replaced a stale inline E2E readiness assumption with a repository-owned checker. |
| 2026-07-31 | v0.7 | Reconciled the prior 44-workflow tree and documented the repository-control threat boundary. |

[Back to top](#top)
