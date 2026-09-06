<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/github-workflows-readme
title: .github/workflows README
type: README
version: v0.18
status: draft; repository-grounded workflow governance reference; exact filename inventory; static and hosted behavior bounded
owners: ["@bartytime4life"]
created: 2026-07-08
updated: 2026-09-06
policy_label: public; github-actions; workflow-governance; fail-closed; non-publisher
owning_root: .github/
responsibility: GitHub Actions orchestration, trigger and permission boundaries, check-name stability, CI maturity disclosure, and workflow inventory accountability
truth_posture: cite-or-abstain; a workflow file, green job, commit, or pull request is not release or publication authority
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  read_ref: main
  read_commit: 4a2ddb9abe7ae64aad7c2d650478a7a14af1b73c
  workflows_tree: f0cc4efee0649f20c0d2c2006642270c50076042
  readme_prior_blob: 0b19d140a568114f4cef66cf7dac04df2d4e9585
  current_workflow_files: 486
  workflow_security_rules: 20
  workflow_security_baseline_entries: 0
  workflow_security_result_at_read_commit: NOT RUN
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
  - ../../docs/runbooks/pr-reliability-guide.md
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
  - "The 486-file count is exact for the pinned Git tree. The twenty-rule static ratchet and empty implementation-waiver baseline exist at that ref, but the ratchet was not executed for this documentation refresh."
  - "The v0.14 detailed forty-four-workflow classification and action inventory remain historical process evidence in Git history, not current-tree evidence."
  - "Workflow filenames and green checks are orchestration evidence only; they do not create policy, review, release, lifecycle, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `.github/workflows/`

> GitHub Actions orchestration for repository-owned checks, bounded automation, and explicit readiness outcomes. Workflow YAML may invoke tools and report results; it does not become policy, evidence, review, release, lifecycle-transition, or publication authority.

> [!IMPORTANT]
> A green workflow, governed hold, skip, static-readiness pass, and substantive validator pass are different outcomes. Names and summaries must not imply more maturity than the executed steps establish.

## At a glance

| Item | Current repository-grounded statement |
|---|---|
| Responsibility | GitHub Actions orchestration under the `.github/` platform-integration root. |
| Inventory | 486 tracked `.yml` workflows and this README at the pinned tree. |
| Static guardrail profile | 20 repository-owned rules with an empty implementation-waiver baseline. |
| Exact-current static result | `NOT RUN` for the pinned read commit; do not inherit the older 425-workflow result. |
| Hosted and ruleset state | `NEEDS VERIFICATION`; inspect GitHub object state at the exact ref. |
| Publication authority | None. Workflows and their outputs remain carriers or review signals unless a separate governed transition says otherwise. |

## Navigation

- [At a glance](#at-a-glance)
- [Purpose](#purpose)
- [Authority level](#authority-level)
- [Status and evidence boundary](#status-and-evidence-boundary)
- [Current inventory boundary](#current-inventory-boundary)
- [Find and assess a workflow](#find-and-assess-a-workflow)
- [Workflow families](#workflow-families)
- [Historical inventory boundary](#historical-inventory-boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Trigger, permission, and threat preflight](#trigger-permission-and-threat-preflight)
- [Validation](#validation)
- [Workflow authoring contract](#workflow-authoring-contract)
- [Change and review sequence](#change-and-review-sequence)
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

This edition was prepared against `main@4a2ddb9abe7ae64aad7c2d650478a7a14af1b73c` and workflow tree `f0cc4efee0649f20c0d2c2006642270c50076042` on 2026-09-06.

**CONFIRMED for that snapshot:**

- the workflow subtree contains one README and **486 tracked `.yml` workflow files**;
- the subtree contains no `.yaml` workflows, non-Markdown companion files, or nested directories;
- the old v0.14 README blob remains in Git history;
- the current tree includes rapidly expanded domain, source, evidence, policy, review, artifact, map, runtime, and governance lanes;
- the 20-rule workflow-security scanner, empty implementation-waiver baseline, Make targets, and `security.yml` and `validator-suite.yml` bindings exist at the pinned ref;
- this documentation change does not modify workflow YAML or a GitHub repository setting.

**NEEDS VERIFICATION for the pinned 486-workflow tree:**

- every trigger and path filter;
- every permission and write scope;
- `pull_request_target`, `workflow_run`, privileged dispatch, and schedule exposure;
- self-hosted runners, containers, services, secrets, OIDC, network access, caches, and artifacts;
- external action provenance and immutable pinning;
- duplicate or misleading workflow and job names;
- current hosted conclusions, required-check coupling, and failure causes;
- whether each command is substantive, partial, held, skipped, or placeholder behavior.

The exact-current workflow-security scan was not run while preparing this README. The scanner's empty baseline is not a substitute for executing it against the exact head.

A filename proves only that bytes exist. It does not establish that the lane is safe, required, current, complete, or production-ready.

## Current inventory boundary

| Inventory fact | Current value | Interpretation |
|---|---:|---|
| Workflow files | **486** | Exact count of tracked `.yml` files in the pinned tree. |
| Workflow README files | **1** | This file. |
| Alternative `.yaml` workflow files | **0 observed** | The pinned workflow tree contains `.yml` files and this README. |
| Growth since the v0.16 snapshot | **61** | New workflow files since the prior 425-file inventory; growth is maintenance pressure, not maturity. |
| Prior documented workflow set | **44** | Historical v0.14 classification; no longer a complete current inventory. |
| Net growth since prior detailed snapshot | **438** | Inventory delta only; it does not establish coverage or readiness. |
| Deterministic static guardrails | **20** | Repository-owned local source rules; not hosted or runtime proof. |
| Implementation-waiver baseline entries | **0** | Exact count in `workflow_security_baseline.json`; not a current scan result. |
| Exact-current static result | **`NOT RUN`** | Run `make workflow-security` at the exact head before reporting a result. |
| Complete current behavioral audit | **Not performed** | Hosted conclusions, rulesets, runtime behavior, and semantic maturity remain `NEEDS VERIFICATION`. |

Regenerate the count from the Git index whenever workflows change:

```bash
git ls-files '.github/workflows/*.yml' | wc -l
```

## Trigger fan-out control boundary

The pinned tree contains 486 workflow files. This revision narrows four responsibility-owned lanes to changed-path triggers: `object-family-register` watches its own workflow plus object-family inputs; `docs-build` watches documentation/build-contract inputs; `docs-control-plane` watches control-plane and documentation governance inputs; and `link-check` watches Markdown plus its validator/test inputs. Manual dispatch remains available for each lane. This is a bounded reduction, not a complete trigger audit, required-check map, or shared-install redesign.

## Find and assess a workflow

Start from tracked files rather than a copied inventory:

```bash
git ls-files '.github/workflows/*.yml' | sort
rg -n '^(name|on|"on"|permissions):' .github/workflows
rg -n 'pull_request_target|workflow_run|id-token: write|contents: write|packages: write|secrets: inherit|self-hosted' .github/workflows
```

Then answer the exact question with the correct authority surface:

| Question | Evidence to inspect | Do not infer |
|---|---|---|
| Does a workflow file exist? | Git tree at the exact ref | That it runs, passes, or is required. |
| What activates it? | Its `on` block and path filters | Hosted event reachability from its filename. |
| What can it access? | Workflow/job `permissions`, secrets, OIDC, runner, cache, artifact, and network configuration | Least privilege from a read-only job alone. |
| What does it actually prove? | Invoked command, tests and fixtures, negative cases, logs, and exact-head conclusion | Substantive validation from a green name or skipped scaffold. |
| Is its check required? | Live repository ruleset and branch-protection state | Ruleset coupling from YAML or this README. |
| Can it publish or change lifecycle state? | Accepted policy and release authority plus an authenticated transition record | Authority from an artifact, receipt, workflow success, merge, or badge. |

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

Version v0.14 documented a detailed **44-workflow** classification, selected command semantics, and an external-action inventory. That material was useful for its pinned snapshots, but the current tree is more than ten times larger.

This edition therefore:

- preserves v0.15 in Git history at prior blob `6d83ab369cbb474be874130dc3cadc645c77323e`;
- supersedes its 44-file count and “complete workflow inventory” label as current evidence;
- does not copy stale per-workflow conclusions onto 438 additional files;
- retains the underlying authoring, threat-model, validation, non-publisher, and rollback rules;
- retains the bounded 20-rule static ratchet while keeping its exact-current result and hosted behavior explicit verification items.

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
make validator-registry-check
make workflow-security
git diff --check
```

For a workflow change, `make repository-guardrails` runs the registry, workflow-security, and repository-topology guardrails together. Attribute each outcome separately; a topology baseline or inherited finding is not a workflow-security result.

`actionlint` may be used when it is installed, but it is not a repository-pinned dependency at the pinned ref. Use a YAML 1.2-aware parser for any supplemental YAML parsing because YAML 1.1 parsers can misinterpret the GitHub Actions `on` key.

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

For Markdown changes, run the bounded local link-check tests and changed-file checker described by [`link-check.yml`](link-check.yml). The repository does not define a general Markdown-lint profile at the pinned ref, so do not report one as run.

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

## Change and review sequence

1. Record the default branch and exact base SHA.
2. Search open pull requests and coordination notes for path or authority overlap.
3. Read this README, the target workflow, its invoked implementation, relevant tests and fixtures, [`CODEOWNERS`](../CODEOWNERS), and the [PR reliability guide](../../docs/runbooks/pr-reliability-guide.md).
4. Define the observable outcome, non-goals, trigger and permission changes, negative cases, validation, rollback, and any required-check name impact.
5. Make one dependency-closed change; keep reusable logic in its owning root.
6. Run changed-area checks and the workflow-security ratchet at the exact head.
7. Open or update a focused draft pull request and report exact base/head evidence.
8. Classify failures as introduced, inherited, resolved, integration/base drift, environmental/flaky, pending, not run, not applicable, or unknown using comparable evidence.
9. Recheck hosted state, review state, changed paths, and ruleset coupling before changing readiness claims.

Branch work and a draft pull request do not authorize approval, merge, release, deployment, promotion, publication, source activation, or repository-setting changes.

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

- **NEEDS VERIFICATION** — behavioral review of commands, trigger reachability, secrets/OIDC, network, caches, artifacts, and write effects for all 486 files.
- **NEEDS VERIFICATION** — exact-current execution of the twenty-rule static ratchet for all 482 workflow files.
- **NEEDS VERIFICATION** — current rulesets and exact required-check coupling.
- **NEEDS VERIFICATION** — recent hosted outcomes, failure causes, logs, rerun state, and artifact retention.
- **NEEDS VERIFICATION** — duplicate, overlapping, obsolete, or misleading workflow/check identities created during rapid growth.
- **NEEDS VERIFICATION** — commands that remain placeholders, readiness holds, or partial validation despite authoritative-sounding names.
- **NEEDS VERIFICATION** — complete policy-bundle, schema, fixture, and runtime parity.
- **NEEDS VERIFICATION** — whether workflow-generated artifacts contain sensitive data or outlive their review purpose.
- **NEEDS VERIFICATION** — the governance-validator README still describes its receipt-bound 424-workflow snapshot as current; correct it only with a provenance-safe receipt update or supersession.
- **CONFIRMED at the pinned ref / exact-current result NEEDS VERIFICATION** — the repository-owned, no-network workflow-security ratchet and its empty implementation-waiver baseline exist; no current pass is claimed here.
- **PROPOSED consolidation** — prefer reusable validators and bounded workflows where multiple files share the same trigger, permissions, and acceptance boundary.

## Changelog

| Date | Version | Change |
|---|---|---|
| 2026-08-31 | v0.17 | Re-pinned the subtree to `main@1b654851…`; recorded 482 `.yml` workflows and 57-file growth since v0.16; separated the empty waiver baseline from an unrun exact-current scan; added practical discovery, evidence-routing, repository-supported validation, and review guidance; and removed the badge wall. |
| 2026-09-06 | v0.18 | Re-pinned the subtree to `main@4a2ddb9…` and `486` tracked `.yml` workflows; narrowed four responsibility-owned lanes to changed-path triggers while retaining manual dispatch, check names, and historical evidence; complete trigger reachability, required-check mapping, and shared-install consolidation remain open. |
| 2026-08-12 | v0.16 | Re-pinned the subtree to `main@bff35f5…`; recorded the exact 425-workflow count; added a deterministic twenty-rule workflow-security ratchet with inherited-drift accounting; and kept hosted conclusions, ruleset state, and runtime maturity explicitly unverified. |
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
