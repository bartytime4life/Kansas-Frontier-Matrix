<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/github-workflows-readme
title: .github/workflows README
type: README
version: v0.14
status: draft; repository-grounded workflow governance reference
owners: ["@bartytime4life"]
created: 2026-07-08
updated: 2026-08-03
policy_label: public; github-actions; workflow-governance; fail-closed; non-publisher
owning_root: .github/
responsibility: GitHub Actions orchestration, trigger and permission boundaries, check-name stability, and CI maturity disclosure
truth_posture: cite-or-abstain; a workflow file, green job, commit, or pull request is not release or publication authority
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  read_ref: main
  read_commit: 68069dce9e292649697f63f96fa57edd07181a27
  workflow_inventory_snapshot: 68069dce9e292649697f63f96fa57edd07181a27
  current_workflow_files: 44
  documented_workflow_files: 44
  inventory_method: complete tracked-tree inspection and static workflow review recorded in v0.3
validator_runner_change_evidence:
  base_commit: cb8a46fff89861b8f0ca57c1c29bacf1fec885a5
  readme_prior_blob: 5d1ab22c5dac921c86c64c138c35a16adac0738a
  runner_prior_blob: ce05ae25d0cb6fc29a2ea41db6c65a99ca5e13e6
  validator_suite_prior_blob: 1694afdd762ce515b53fc8e9d7d51324c2d0929d
  schema_validation_prior_blob: fd0e53722b9d8406c5fde052672f760f00f2626b
  source_descriptor_validate_prior_blob: fc808375a73e0d4ddfdc80fd5f0199a0486c93ce
  focused_test: ../../tests/validators/test_jsonschema_runner.py
  local_result: PASS; 10 tests
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
  - ../../tools/validators/_common/README.md
  - ../../tools/validators/_common/jsonschema_runner.py
  - ../../tests/validators/README.md
  - ../../tests/validators/test_jsonschema_runner.py
  - ../../tools/validators/validate_generated_receipt.py
  - ../../tests/validators/test_validate_generated_receipt.py
  - ../../fixtures/generated_receipt/
  - ../../tools/validators/e2e_readiness.py
  - ../../tests/validators/test_e2e_readiness.py
  - ../../tests/runtime_proof/test_envelope_finite_outcomes.py
  - ../../tests/e2e/README.md
  - ../../policy/
  - ../../schemas/
  - ../../contracts/
  - ../../tests/
  - ../../fixtures/
  - ../../release/
notes:
  - "v0.14 reconciles the promotion workflow description with the bounded fixture-only ReviewRecord candidate while preserving live identity, authority, governed-record, rollback, release, and publication holds."
  - "v0.13 graduates only focus-mock-test/finite-envelope-shape from static hold detection to a deterministic standard-library shape proof while preserving the mock-focus and composed-E2E holds, workflow/job identities, permissions, and non-publisher posture."
  - "v0.12 adds the focused no-network GENERATED_RECEIPT unittest suite and exact fixture-failure command to validator-suite before the unchanged seven-entry aggregate; workflow/job identities, triggers, permissions, actions, runners, artifact posture, and publication boundaries are unchanged."
  - "v0.11 pins every external GitHub Action reference to the immutable commit currently resolved by its existing tag; triggers, permissions, runners, workflow and job identities, inputs, commands, no-network semantics, artifact behavior, and publication boundaries are unchanged."
  - "v0.10 extends the existing link-check implementation and focused no-network suite to bounded defined reference-style links; workflow name, job ID, triggers, permissions, actions, runner, network posture, and artifact posture are unchanged."
  - "v0.9 wires ten focused standard-library shared-runner tests into validator-suite before make schemas and aligns schema/source workflow diagnostics with EXPECTED_FAIL versus FAIL; workflow names, job IDs, triggers, permissions, actions, runners, network posture, and artifact posture are unchanged."
  - "v0.8 replaces the stale inline exact-TODO Explorer assumption in e2e-smoke with a tested repository-owned readiness validator; the composed E2E suite remains explicitly held."
  - "The v0.6 prior README bytes and all 44 current-main workflow files were inspected at main@c455e51be776a355a392284711898af092fb423f."
  - "The detailed 41-file workflow inventory remains lineage at 1180cf7ec53d5acbbb859a39d93c1d129ec83df9; v0.7 reconciles the complete current 44-file inventory, including repository-control.yml and link-check.yml as implemented orchestration."
  - "Workflow maturity groups describe inspected files and steps; they do not certify current run success, branch protection, release readiness, or KFM publication."
  - "v0.5 narrowly reconciles shared domain holds and the E2E, Focus mock, and rollback-drill readiness checks; it does not establish UI or runtime readiness."
  - "v0.6 added one explicitly approved trusted-base pull_request_target guard with read-only permissions and a full-SHA checkout pin. Whether its exact check is currently required by the main ruleset remains NEEDS VERIFICATION from static repository bytes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `.github/workflows/`

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Current inventory: 44 workflows](https://img.shields.io/badge/current%20inventory-44%20workflows-1f6feb?style=flat-square)](#complete-workflow-inventory)
[![Permissions: explicit](https://img.shields.io/badge/permissions-44%2F44%20explicit-15803d?style=flat-square)](#trigger-permission-and-workflow-threat-preflight)
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

`promotion-gate.yml` and the `promotion-gate-check` job in
`release-dry-run.yml` execute `make publish-check`. That target validates one
bounded, synthetic A-G readiness profile and its exact failure matrix. A
`PASS` result means only `APPROVE_READY` for review; it does not assemble a
release candidate, authenticate supporting references, record human approval,
evaluate production policy, execute rollback, change lifecycle state, or
publish. Governed ReviewRecord production, live identity and authority
resolution, candidate assembly, and rollback-card execution remain separately
held; the wired validator covers only repository-owned synthetic projections.

## Status

### Current document state

- **CONFIRMED:** this README and all 44 current-main workflow files were read on `main@46d0536017655e69b6de451fd57759a463f0d252`.
- **CONFIRMED:** `repository-control.yml` is tracked on `main` and is the only active `pull_request_target` workflow.
- **CONFIRMED / LINEAGE:** the detailed static inventory below was generated from `main@1180cf7ec53d5acbbb859a39d93c1d129ec83df9` and documented 41 tracked `.yml` workflows.
- **CONFIRMED:** the current tree has 44 `.yml` workflows, 44 explicit top-level permission blocks, one privileged PR trigger, no self-hosted runner or direct `secrets.*` expression, one ordinary write grant, and the full-SHA action inventory below.
- **UNKNOWN:** current branch-protection coupling, recent workflow conclusions, logs, organization defaults, artifact retention, and runtime behavior unless separately inspected.

### Documented inventory findings

| Finding | Snapshot status | Interpretation |
|---|---|---|
| Workflow inventory | **CONFIRMED current main: 44 tracked `.yml` files** | `repository-control.yml` is part of the current tree; no `.yaml` workflow is present. |
| Explicit permissions | **CONFIRMED current main: 44/44** | Every workflow declares a top-level permissions boundary. |
| Privileged PR trigger | **CONFIRMED exactly one** | `repository-control.yml` uses `pull_request_target` with an inline threat model, a trusted-base-only checkout, bounded untrusted-data parsing, and read-only permissions. |
| Runner trust | **CONFIRMED at current snapshot** | No `self-hosted` occurrence. |
| Direct secret expressions | **CONFIRMED absent at current snapshot** | No direct `secrets.*` occurrence; repository and organization settings remain external. |
| Write scopes | **CodeQL only at current snapshot** | `security-events: write` supports code-scanning upload; the transition guard has no write grant. |
| External action pinning | **Full SHA** | All 161 external-action uses resolve through immutable 40-character commits; version comments preserve Dependabot update context. |
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
python -m unittest discover --start-directory tests/validators --pattern 'test_jsonschema_runner.py' --verbose
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
| README content read | 2026-08-01 |
| Read ref | `main` |
| Read commit | `cb8a46fff89861b8f0ca57c1c29bacf1fec885a5` |
| Detailed workflow inventory snapshot | `c455e51be776a355a392284711898af092fb423f` |
| Bounded readiness reconciliation | 2026-08-01; shared JSON Schema runner tests and three directly affected workflow definitions |
| Inventory refresh status | **CONFIRMED current static count: 44**; hosted execution and ruleset coupling remain separate |

## Complete workflow inventory

The groups below preserve the repository-grounded v0.3 classification and reconcile every current workflow filename exactly once. They describe inspected code and status comments; they are not release-readiness grades.

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

These workflows share a bounded readiness posture: they may confirm exact
repository scaffolds or selected synthetic validation slices while keeping
unimplemented validation, proof, and release lanes on explicit
`WORKFLOW_HOLD`. A green readiness/hold job does not establish complete domain,
runtime, UI, policy, proof, release, or publication readiness.

### Bounded system readiness and governed holds

- [`docs-build.yml`](docs-build.yml)
- [`e2e-smoke.yml`](e2e-smoke.yml)
- [`focus-mock-test.yml`](focus-mock-test.yml)
- [`hydrology-proof-slice.yml`](hydrology-proof-slice.yml)

These jobs expose missing executables, fixtures, proof closure, or runtime readiness. A hold is a truthful finite outcome, not a passing implementation claim. The `focus-mock-test / finite-envelope-shape` job is a bounded exception: it now executes canonical alias, closed-shape, four-outcome, and negative fixture tests while the mock Focus runtime lane remains held.

The current E2E inspection calls the repository-owned standard-library
`e2e_readiness.py` checker. It confirms the root manifest's exact fail-closed
`WORKFLOW_HOLD` scripts, the implemented Explorer Web build/unit-test baseline,
the adjacent UI/API orchestration markers, and the exact bounded placeholder
inventory while still running no composed browser/API journey. The Focus mock
inspection relies on structured synthetic, non-authoritative, do-not-publish,
expected-`ABSTAIN` markers and still produces no runtime response. Its sibling
finite-envelope job executes shape-only tests for all four outcomes and does
not establish semantic outcome selection, runtime behavior, policy, evidence,
release, or publication status. The rollback
drill relies on ADR-0015's structured draft/proposed and held/alias-absent
markers and remains read-only. Explorer UI build/unit-test readiness is separate
from composed E2E, runtime, evidence, policy, release, or publication readiness.

### Command-bearing and partial gates

- [`api-test.yml`](api-test.yml)
- [`briefing-integration.yml`](briefing-integration.yml)
- [`codeql.yml`](codeql.yml)
- [`connector-gate.yml`](connector-gate.yml)
- [`contract-drift.yml`](contract-drift.yml)
- [`contracts-validate.yml`](contracts-validate.yml)
- [`deny-test.yml`](deny-test.yml)
- [`dependency-scan.yml`](dependency-scan.yml)
- [`docs-control-plane.yml`](docs-control-plane.yml)
- [`evidence-resolver.yml`](evidence-resolver.yml)
- [`infra-compose-smoke.yml`](infra-compose-smoke.yml)
- [`link-check.yml`](link-check.yml)
- [`maplibre-perf-governance.yml`](maplibre-perf-governance.yml)
- [`pmtiles-attestation.yml`](pmtiles-attestation.yml)
- [`policy-boundary-guards.yml`](policy-boundary-guards.yml)
- [`policy-test.yml`](policy-test.yml)
- [`promotion-gate.yml`](promotion-gate.yml)
- [`release-dry-run.yml`](release-dry-run.yml)
- [`repository-control.yml`](repository-control.yml)
- [`rollback-drill.yml`](rollback-drill.yml)
- [`schema-validation.yml`](schema-validation.yml)
- [`source-descriptor-validate.yml`](source-descriptor-validate.yml)
- [`telemetry-policy.yml`](telemetry-policy.yml)
- [`validator-suite.yml`](validator-suite.yml)

Read the exact steps and job summaries before relying on any workflow as a merge gate. “Command-bearing” does not mean complete, current, or production-ready.

`evidence-resolver.yml` runs only the internal v1alpha1 candidate profile and
its exact synthetic negative suite, including bounded bitemporal verification
history replay. It performs no live lookup and cannot
establish evidence truth, policy clearance, review, release, public outcome,
or publication authority.

`link-check.yml` preserves the stable workflow and `docs-link-check` job names
while replacing the prior readiness hold with a standard-library, local-only
checker. It runs synthetic no-network tests and validates inline local file,
directory, image, and fragment targets plus bounded, defined reference-style
uses only in Markdown changed by the triggering revision. External targets are
reported as `EXTERNAL_TARGET_UNVERIFIED` and are never requested. Multiline or
nested-label reference definitions, undefined reference-like citations, inline
HTML links, redirects, ignore rules, and unchanged historical documents remain
outside this bounded check; a green result is documentation QA only.

`validator-suite.yml` preserves the stable `validator-suite` workflow and
`run-validators` / `ensure-fail-closed` job IDs. The first job installs the
declared Python dependencies, runs all ten focused standard-library cases in
`tests/validators/test_jsonschema_runner.py`, then runs the focused no-network
`test_validate_generated_receipt.py` unittest suite and the generated-receipt
fixture command before the unchanged seven-entry `make schemas` aggregate. The
generated-receipt negative lane must match its exact bounded expected-finding
sidecar; an unrelated rejection does not pass fixture polarity. The second job
remains the reviewed invalid EvidenceBundle canary. Triggers, permissions,
actions, hosted runner, network posture, artifact posture, and check names are
unchanged. Hosted execution at the proposed head remains **NEEDS VERIFICATION**;
a green result would prove only these bounded mechanics, not authenticated
review or mutation authority, semantic truth, policy, evidence closure, merge,
release readiness, or publication.

`schema-validation.yml` and `source-descriptor-validate.yml` retain their
existing commands, triggers, permissions, runners, and job names. Their
diagnostic text now names `EXPECTED_FAIL` as a successful schema-rejection
observation and reserves `FAIL` for harness, malformed-input, exception, or
polarity errors. This is an observability alignment with the shared runner, not
a broader validation or publication claim.

`dependency-scan.yml` preserves the stable `npm-audit` job id for check-name
compatibility but now proposes the repository's accepted pnpm contract. Its
repository-owned, no-network validator checks the exact manager pin, Node
engine, workspace definitions, lockfile version and importers, competing root
lockfiles, and safe manifest inputs before any registry access. The workflow
then runs `pnpm audit --audit-level high --json` and classifies the combined
report and command exit as `PASS`, `REGRESSION`, or `ERROR`. Threshold findings,
registry or command failures without confirmed findings, malformed reports, and
command/report polarity mismatches fail closed. The result is point-in-time
supply-chain evidence only; exact-head remote execution remains
**NEEDS VERIFICATION**, and this change does not satisfy the separate E2E hold.

`repository-control.yml` is a deliberately narrow exception to the usual
`pull_request` preference. It uses `pull_request_target` so a pull request
cannot replace the guard before evaluation, checks out only the GitHub-supplied
base SHA, never executes head code, reads only issue/event JSON, and grants only
read access to contents, issues, and pull requests. Its strict local validator
requires an unedited owner-account record for the exact repository, control
issue, PR, base, head, and four-hour-or-shorter window. The check is advisory
unless the `main` ruleset separately requires
`repository-control / authorize-ready-and-merge`; static repository bytes do
not establish that coupling, so its current enforcement is **NEEDS
VERIFICATION**. When relied upon, the check records an explicit owner-account
decision; it cannot distinguish a human browser from an installed app or token
acting through the same identity.
Expiry is evaluated when the workflow runs; GitHub does not automatically
time-expire a successful check or rerun it after the issue comment is edited or
deleted. The result is point-in-time evidence and must be rerun before reliance
after expiry or comment mutation.

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

### Static threat findings at the current snapshot

| Threat surface | Finding |
|---|---|
| `pull_request_target` | Exactly `repository-control.yml`; trusted-base checkout only, no head-code execution, bounded issue/event parsing, and read-only contents/issues/pull-requests access. |
| Self-hosted runner | No occurrence. |
| Direct secret expressions | No `secrets.*` occurrence. |
| Ordinary write permissions | No `contents`, `issues`, `pull-requests`, `packages`, `deployments`, or `id-token` write grant. |
| Code scanning | [`codeql.yml`](codeql.yml) granted `security-events: write`; re-review if its event or trust boundary changes. |
| External action immutability | All external action references are pinned to full 40-character commits that were verified against their official upstream tags at this snapshot. |
| Publication path | No file-presence claim authorized publication; every invoked command still requires inspection. |

## External action inventory

The dependency-closed pinning slice started from this complete floating
inventory at `main@46d0536017655e69b6de451fd57759a463f0d252`:

| Floating action reference | Occurrences | Workflow files | Official immutable commit verified for the existing tag |
|---|---:|---:|---|
| `actions/checkout@v7` | 93 | 41 | [`3d3c42e5aac5ba805825da76410c181273ba90b1`](https://github.com/actions/checkout/commit/3d3c42e5aac5ba805825da76410c181273ba90b1) (`v7.0.1`) |
| `actions/setup-python@v7` | 60 | 38 | [`5fda3b95a4ea91299a34e894583c3862153e4b97`](https://github.com/actions/setup-python/commit/5fda3b95a4ea91299a34e894583c3862153e4b97) (`v7.0.0`) |
| `actions/setup-node@v7.0.0` | 4 | 3 | [`820762786026740c76f36085b0efc47a31fe5020`](https://github.com/actions/setup-node/commit/820762786026740c76f36085b0efc47a31fe5020) (`v7.0.0`) |
| `actions/upload-artifact@v7` | 1 | 1 | [`043fb46d1a93c77aae656e7c1c64a875d1fc6a0a`](https://github.com/actions/upload-artifact/commit/043fb46d1a93c77aae656e7c1c64a875d1fc6a0a) (`v7.0.1`) |
| `github/codeql-action/init@v4` | 1 | 1 | [`f205ea1c3313d32999d8d6a48b4f6530d4437b38`](https://github.com/github/codeql-action/commit/f205ea1c3313d32999d8d6a48b4f6530d4437b38) (`v4.37.4`) |
| `github/codeql-action/analyze@v4` | 1 | 1 | [`f205ea1c3313d32999d8d6a48b4f6530d4437b38`](https://github.com/github/codeql-action/commit/f205ea1c3313d32999d8d6a48b4f6530d4437b38) (`v4.37.4`) |

The base also contained one already-immutable checkout use, so the complete
post-change inventory is:

| Action commit | Occurrences | Pinning posture |
|---|---:|---|
| `actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1` | 94 | Immutable full SHA; 93 uses document `v7.0.1`, and the pre-existing transition-guard use retains its `v7` comment. |
| `actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97` | 60 | Immutable full SHA resolving `v7.0.0`. |
| `actions/setup-node@820762786026740c76f36085b0efc47a31fe5020` | 4 | Immutable full SHA resolving `v7.0.0`. |
| `actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a` | 1 | Immutable full SHA resolving `v7.0.1`. |
| `github/codeql-action/init@f205ea1c3313d32999d8d6a48b4f6530d4437b38` | 1 | Immutable peeled commit for annotated tag `v4.37.4`. |
| `github/codeql-action/analyze@f205ea1c3313d32999d8d6a48b4f6530d4437b38` | 1 | Immutable peeled commit for annotated tag `v4.37.4`. |

The replacements freeze the exact commits the prior tags resolved to; they do
not change action inputs or outputs. Weekly GitHub Actions Dependabot monitoring
remains the reviewable update path. It reduces update toil but does not establish
compatibility or replace changelog, runner-runtime, and security review.

A repository-wide text scan also found 14 floating references inside fenced,
non-executing Markdown examples. They are inventoried but excluded from this
executable-workflow slice so historical and domain runbook examples are not
silently re-versioned:

| Non-executing example reference | Occurrences | Markdown documents | Official immutable commit verified for the existing tag | Disposition |
|---|---:|---:|---|---|
| `actions/checkout@v4` | 11 | 11 | [`11d5960a326750d5838078e36cf38b85af677262`](https://github.com/actions/checkout/commit/11d5960a326750d5838078e36cf38b85af677262) (`v4.4.0`) | Residual documentation-example modernization; never executed from `.github/workflows/`. |
| `actions/upload-artifact@v4` | 3 | 3 | [`ea165f8d65b6e75b540449e92b4886f43607fa02`](https://github.com/actions/upload-artifact/commit/ea165f8d65b6e75b540449e92b4886f43607fa02) (`v4.6.2`) | Residual documentation-example modernization; never executed from `.github/workflows/`. |

Historical generated receipts and documents explicitly pinned to older evidence
snapshots retain their original tag strings as lineage. They are not executable
Action references and are not rewritten as current-state evidence.

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

- **CONFIRMED current-main static inventory** — 44 workflows, 44 explicit permission blocks, one `pull_request_target`, one ordinary write grant (`security-events: write` in CodeQL), and GitHub-hosted runners only.
- **NEEDS VERIFICATION** — whether ruleset `15484585` currently requires the exact strict check `repository-control / authorize-ready-and-merge`; static workflow bytes and a successful canary do not prove current settings enforcement.
- **NEEDS VERIFICATION** — current rulesets and exact branch-protection coupling outside the 2026-07-29 settings snapshot.
- **NEEDS VERIFICATION** — current workflow run results, failure causes, logs, and artifact retention.
- **NEEDS VERIFICATION** — repository and organization default token permissions.
- **NEEDS VERIFICATION** — whether every path filter covers intended implementation and documentation surfaces.
- **NEEDS VERIFICATION** — whether hold and readiness job names could be mistaken for substantive enforcement.
- **NEEDS VERIFICATION** — whether a repository-owned validator or ruleset will enforce full-SHA action pinning and whether Dependabot action-update pull requests will meet the intended review cadence.
- **NEEDS VERIFICATION** — whether the 14 non-executing `v4` Action references in fenced Markdown examples should be modernized in a separate documentation-owned slice.
- **NEEDS VERIFICATION** — complete CI/runtime policy-bundle parity and proof/release closure.
- **NEEDS VERIFICATION** — whether workflow-generated artifacts contain sensitive data or outlive their review purpose.

## Changelog

| Date | Version | Change |
|---|---|---|
| 2026-08-03 | v0.14 | Reconciled promotion workflow documentation with the bounded fixture-only ReviewRecord candidate and retained every live-governance and non-publisher boundary. |
| 2026-08-02 | v0.13 | Replaced the finite-envelope assert-true/TODO hold with a deterministic standard-library four-outcome shape proof, preserved the mock-runtime and composed-E2E holds, and kept workflow/job identities and non-publisher boundaries unchanged. |
| 2026-08-02 | v0.12 | Added focused GENERATED_RECEIPT validation and exact positive/negative fixture behavior to `validator-suite/run-validators` without changing workflow identities, triggers, permissions, actions, runners, artifacts, aggregate membership, or publication authority. |
| 2026-08-01 | v0.11 | Replaced all 160 floating external-action references with the exact full commits resolved by their existing official tags, preserving all workflow behavior and leaving weekly Dependabot review as the update path. |
| 2026-08-01 | v0.10 | Extended the existing standard-library link checker and focused no-network suite to bounded defined reference-style links without changing workflow identity, triggers, permissions, actions, runner, network posture, artifacts, or publication authority. |
| 2026-08-01 | v0.9 | Added the focused shared JSON Schema runner suite to `validator-suite/run-validators`, aligned schema/source workflow diagnostics with `EXPECTED_FAIL` versus `FAIL`, and documented the bounded fixture semantics without changing triggers, permissions, names, runners, artifacts, or publication authority. |
| 2026-07-31 | v0.8 | Replaced `e2e-smoke`'s stale inline TODO-only Explorer assumption with the tested no-network `e2e_readiness.py` checker; documented the implemented Explorer build/unit-test baseline and preserved the explicit composed-suite hold. |
| 2026-07-31 | v0.7 | Reconciled all 44 workflows to current `main@c455e51…`; converted the repository-control guard from proposed-head language to current implementation fact while keeping ruleset enforcement unverified; refreshed static permission, trigger, runner, secret, write-scope, action-pin, and inventory evidence. |
| 2026-07-30 | v0.6 | Reconciled the current 43-file inventory plus the proposed trusted-base repository transition guard; documented its `pull_request_target` threat model, read-only token, immutable checkout pin, advisory check status, and human-versus-app attribution limit. |
| 2026-07-29 | v0.5 | Reconciled shared domain hold semantics and the bounded E2E, Focus mock, and rollback-drill readiness checks with current structured repository evidence; preserved explicit holds and no UI/runtime readiness claim. |
| 2026-07-23 | v0.4 | Aligned the README with the canonical-root contract; separated current document evidence from the pinned workflow inventory; added belongs/non-belongs, review burden, related-folder, ADR, threat-preflight, rollback, accessibility, and anti-overclaim guidance. |
| 2026-07-22 | v0.3 | Replaced the stale 34-stub/7-command snapshot with the complete 41-file inventory; reconciled maturity groups, explicit permissions, action refs, and removal of prior OIDC drift. |
| 2026-07-17 | v0.2 | Added the first repository-grounded inventory from indexed searches. |
| 2026-07-08 | v0.1 | Established the workflow governance README. |

[Back to top](#top)
