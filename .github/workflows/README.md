<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/github-workflows-readme
title: .github/workflows README
type: README
version: v0.2
status: draft; repository-grounded workflow inventory
owners: <repo stewards · governance reviewers · CI maintainers — placeholder, confirm via .github/CODEOWNERS>
created: 2026-07-08
updated: 2026-07-17
policy_label: public; github-actions; workflow-governance; ci; fail-closed; non-publisher; release-gated; non-authoritative
owning_root: .github/
responsibility: workflow-subtree README for GitHub Actions orchestration; records the repository-grounded workflow inventory, trigger and permission posture, local-parity commands, stub-vs-command-bearing maturity, check-name discipline, non-publisher constraints, generated-output boundaries, and open verification work while deferring validator logic, policy, schemas, contracts, tests, fixtures, evidence, proofs, receipts, release decisions, lifecycle data, and public runtime behavior to their owning roots
truth_posture: cite-or-abstain; implementation claims are bounded to the evidence snapshot below
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 66610a2ee8bdc15713d1e5a5b0350081a1d7771c
  inventory_method: GitHub connector file reads plus code-index queries for workflow jobs and explicit greenfield-stub markers
related:
  - ../README.md
  - ../CODEOWNERS
  - ../PULL_REQUEST_TEMPLATE.md
  - ../../README.md
  - ../../SECURITY.md
  - ../../Makefile
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/ai-build-operating-contract.md
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../../tools/ci/README.md
  - ../../tools/validators/README.md
  - ../../policy/
  - ../../schemas/
  - ../../contracts/
  - ../../tests/
  - ../../fixtures/
  - ../../release/
  - ../../data/receipts/generated/README.md
  - ../../data/proofs/
  - ../../infra/
notes:
  - "The indexed runnable-job inventory at the pinned base contains 41 workflow files with `runs-on`; 34 explicitly identify themselves as PROPOSED greenfield scaffolds and seven contain command-bearing CI wiring."
  - "The inventory is repository-grounded but bounded: branch-protection settings, effective default token permissions, workflow run history, any workflow without an indexed `runs-on` match, and any `.yaml` file remain NEEDS VERIFICATION."
  - "Workflow YAML orchestrates authority owned elsewhere. A check run, log, uploaded artifact, or passing workflow is not by itself EvidenceBundle closure, proof, release approval, or publication authority."
  - "No workflow YAML, branch protection, repository setting, policy, schema, contract, test, runtime, release, or lifecycle artifact is changed by this documentation-only revision."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `.github/workflows/`

![status](https://img.shields.io/badge/status-repo--grounded%20draft-orange)
![root](https://img.shields.io/badge/root-.github%2F-blue)
![scope](https://img.shields.io/badge/scope-github--actions-informational)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)
![publisher](https://img.shields.io/badge/publisher-no-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)
![inventory](https://img.shields.io/badge/indexed%20workflows-41-1f6feb)

> **One-line purpose.** `.github/workflows/` is KFM's GitHub Actions orchestration lane: it runs repository-owned commands and exposes review signals without becoming policy authority, validator authority, evidence authority, release authority, lifecycle authority, or publisher.

## Quick navigation

- [Purpose](#purpose)
- [Authority level](#authority-level)
- [Status](#status)
- [What belongs here](#what-belongs-here)
- [What does NOT belong here](#what-does-not-belong-here)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Validation](#validation)
- [Review burden](#review-burden)
- [Related folders](#related-folders)
- [ADRs](#adrs)
- [Last reviewed](#last-reviewed)
- [Repository fit](#repository-fit)
- [Indexed workflow inventory](#indexed-workflow-inventory)
- [Trigger and permission preflight](#trigger-and-permission-preflight)
- [Workflow authoring contract](#workflow-authoring-contract)
- [Required negative checks](#required-negative-checks)
- [Maintenance checklist](#maintenance-checklist)
- [FAQ](#faq)
- [Open verification items](#open-verification-items)
- [Changelog](#changelog)

---

## Purpose

`.github/workflows/` holds GitHub Actions workflow definitions for the Kansas Frontier Matrix repository.

This subtree answers one bounded operational question:

> Which GitHub-hosted checks should run for a change, and how should they report deterministic, reviewable outcomes without inventing authority or bypassing KFM's trust membrane?

### Scope and audience

This README is for maintainers, reviewers, CI/tooling stewards, domain-lane owners, policy reviewers, release stewards, and coding agents that create or revise workflow YAML.

It documents:

- the workflow subtree's authority boundary;
- the indexed default-branch inventory at a pinned commit;
- the difference between command-bearing workflows and explicit greenfield stubs;
- trigger, token-permission, action-pinning, and fork-PR risks;
- local-parity commands and current placeholder limits;
- review, rollback, and documentation obligations.

It does **not** certify that branch protection requires any named job, that a workflow has passed recently, that a report is release-grade proof, or that a stub implements its advertised check.

[Back to top](#top)

---

## Authority level

**Implementation-bearing platform orchestration.** Workflow YAML can execute commands and create GitHub check signals, but it does not define KFM truth or authorize publication.

| Workflow concern | Authority owned by | Workflow role |
|---|---|---|
| Trigger selection, job graph, runner, GitHub token permissions | `.github/workflows/` | Own and document the GitHub Actions orchestration. |
| Validator behavior | `tools/validators/` and tests | Invoke; do not reimplement inline. |
| Policy decisions | `policy/` | Evaluate the pinned policy inputs; do not author policy in YAML. |
| Object meaning and machine shape | `contracts/`, `schemas/` | Validate; do not redefine. |
| Fixtures and expected behavior | `fixtures/`, `tests/` | Consume and execute. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Generate or verify through accepted tools; logs are not substitutes. |
| Catalog and release closure | `data/catalog/`, `release/` | Dry-run or verify; do not approve or publish by workflow existence alone. |
| Public API, map, UI, or AI behavior | governed app/runtime roots | Test the boundary; do not become the public path. |
| Deployment and exposure posture | `infra/`, `runtime/`, `configs/` | Validate declared posture; do not hide deployment authority in CI. |

> [!IMPORTANT]
> A green check means the declared job completed successfully for its declared inputs. It does not automatically mean the underlying claim is true, the artifact is public-safe, or promotion is authorized.

[Back to top](#top)

---

## Status

The table below is bounded to `main@66610a2ee8bdc15713d1e5a5b0350081a1d7771c` and the GitHub connector searches used for this revision.

| Surface | Status | Evidence-bounded interpretation |
|---|---|---|
| This README | **CONFIRMED file / draft documentation** | Existing README fetched and revised in place. |
| Indexed runnable-job inventory | **CONFIRMED: 41 files with `runs-on`** | Code-index search found 41 workflow files that define jobs. This does not prove there are no additional `.yaml`, reusable, disabled, or unindexed files. |
| Explicit greenfield stubs | **CONFIRMED: 34 indexed files** | These files contain `Status: PROPOSED greenfield scaffold` and primarily execute `echo TODO ...`. |
| Command-bearing workflows | **CONFIRMED: 7 indexed files** | These invoke Make targets, Python tests/validators, Node scripts, or artifact upload steps. Execution success remains **NEEDS VERIFICATION** without current runs. |
| Required checks / branch protection | **UNKNOWN / NEEDS VERIFICATION** | Repository settings were not inspected. A workflow or job name must not be called required without settings evidence. |
| Workflow run history, logs, artifacts, and recent pass rates | **NOT INSPECTED** | No current run proves these workflows pass at this snapshot. |
| Effective default `GITHUB_TOKEN` permissions | **UNKNOWN** for workflows without an explicit `permissions:` block | Repository and organization defaults were not inspected. |
| CODEOWNERS enforcement | **NEEDS VERIFICATION** | `.github/CODEOWNERS` exists, but it is a greenfield placeholder and branch-protection enforcement was not verified. |
| Action pinning | **CONFIRMED major-tag usage in inspected files / hardening needed** | Inspected workflows use refs such as `actions/checkout@v7`, not immutable commit SHAs. |

[Back to top](#top)

---

## What belongs here

- GitHub Actions workflow files: `*.yml` or `*.yaml`.
- Trigger definitions for `pull_request`, `push`, `workflow_dispatch`, schedules, or approved reusable-workflow calls.
- Stable workflow names, job ids, dependency graphs, concurrency controls, timeouts, matrices, and conditions.
- Explicit least-privilege `permissions:` declarations.
- Thin installation and command-invocation steps needed to run repository-owned validators, tests, policy checks, builds, and dry-runs.
- Artifact uploads for reviewer aids, with bounded retention and clear non-authority labels.
- Failure-only diagnostics that do not convert errors into success.
- Comments documenting why a trigger, permission, network exception, or write is necessary.

[Back to top](#top)

---

## What does NOT belong here

- Canonical validator or business logic that belongs in `tools/`, `packages/`, or app code.
- Rego policy, allowlists, sensitivity rules, rights rules, or release decisions that belong in `policy/`.
- JSON Schema or semantic object definitions that belong in `schemas/` and `contracts/`.
- Golden or invalid fixtures that belong in `fixtures/` or `tests/`.
- Source descriptors, source registry records, or source admission decisions.
- Canonical lifecycle data, EvidenceBundles, receipts, proofs, catalog records, release manifests, rollback cards, or correction notices.
- Credentials, private endpoints, exact sensitive locations, restricted source payloads, or secrets echoed to logs.
- Direct writes to `data/published/`, catalog/triplet authority, release authority, or public runtime truth by ordinary CI or watcher jobs.
- A second copy of logic already reproducible through the Makefile, package scripts, or accepted tools.

[Back to top](#top)

---

## Inputs

Workflows may read:

- the checked-out repository state for the triggering commit;
- changed-path and event metadata supplied by GitHub;
- `Makefile` targets and package-native scripts;
- validators, QA helpers, and CI support code under `tools/`;
- tests and deterministic fixtures;
- schemas, contracts, policies, source descriptors, and control-plane registers from their canonical roots;
- release candidates, receipts, proofs, and manifests when the job is explicitly a verifier or dry-run;
- secrets or identity tokens only when a reviewed workflow has a documented, least-privilege requirement.

Untrusted pull-request content remains data, not instructions. A workflow handling forks or external contributions must assume the submitted code and files are hostile until validated.

[Back to top](#top)

---

## Outputs

| Output | Accepted use | Boundary |
|---|---|---|
| Check run / job conclusion | Branch-protection and review signal. | Not evidence or release authority by itself. |
| Log and annotation | Debugging and reviewer context. | Must not disclose secrets or sensitive data. |
| JUnit, coverage, lint, accessibility, or QA report | Review artifact. | Does not become canonical data or proof merely because it was uploaded. |
| Deterministic PR summary | Human-readable obligations and failures. | Must be idempotent and avoid restricted details. |
| Uploaded artifact | Temporary reviewer aid with retention policy. | Promotion into a governed receipt/proof/release home requires an accepted tool and state transition. |
| Candidate receipt, proof, or release dry-run output | Input to review and later verification. | Candidate status must remain visible; workflow completion is not approval. |
| Failure bundle | Diagnostic and rollback/correction aid. | `|| true` may preserve diagnostics but must not mask the governing job failure. |

[Back to top](#top)

---

## Validation

### Repository-grounded local-parity surface

| Command or target | Current implementation at the evidence snapshot | Workflow users | Status |
|---|---|---|---|
| `make schemas` | Runs `python tools/validators/_common/run_all.py`. | `schema-validation.yml`, `validator-suite.yml` | **CONFIRMED command wiring / run result not inspected** |
| `make test` | Runs `pytest tests/schemas tests/contracts -q`. | `contracts-validate.yml` | **CONFIRMED command wiring / run result not inspected** |
| `make governed-api-smoke` | Runs the governed API test directory. | `api-test.yml` | **CONFIRMED command wiring / run result not inspected** |
| `make boundary-guards-ci` | Runs four policy/API boundary test modules and emits JUnit. | `policy-boundary-guards.yml` | **CONFIRMED command wiring / run result not inspected** |
| MapLibre perf scripts and validators | Builds smoke, render-diff, receipt, manifest, proof-pack, and failure artifacts. | `maplibre-perf-governance.yml` | **CONFIRMED command wiring / path drift and run result NEED VERIFICATION** |
| PMTiles validators | Conditional header, Merkle-sidecar, and shape-only signature validation. | `pmtiles-attestation.yml` | **CONFIRMED command wiring / no-artifact paths currently skip successfully** |
| `make policy`, `release-dry-run`, `publish-check`, `deny-test`, `ui-build` | Emit `TODO` messages in the current Makefile. | Advertised by several stubs | **PROPOSED placeholder; must not be treated as enforcement** |

### README validation for this subtree

A documentation-only change should at minimum verify:

1. one H1 and a valid KFM Meta Block;
2. all required Directory Rules README sections are present in order;
3. repository-relative links resolve;
4. named workflow files exist at the pinned snapshot;
5. inventory totals match the evidence method;
6. no credential or sensitive payload is introduced;
7. no workflow or branch setting is changed unintentionally;
8. a generated receipt is emitted when the change is AI-authored and the repository contract requires one.

[Back to top](#top)

---

## Review burden

Changes under `.github/workflows/` are security- and governance-significant even when they appear small.

- The current `.github/CODEOWNERS` is a **greenfield placeholder** with a global `@kfm/maintainers` entry; team validity and enforcement remain **NEEDS VERIFICATION**.
- A workflow PR should receive CI/tooling review plus the owner of every authority root the job invokes materially.
- Policy, release, sensitive-domain, identity-token, secret, deployment, artifact-signing, or write-permission changes require the corresponding steward review.
- Renaming a workflow or job that may be a required check requires branch-protection coordination before merge.
- Stub graduation is behavior change: reviewers must inspect the exact command, inputs, outputs, negative fixtures, permissions, network posture, and rollback/disable path.

[Back to top](#top)

---

## Related folders

| Path | Relationship |
|---|---|
| [`.github/`](../README.md) | Parent GitHub platform-governance root. |
| [`.github/CODEOWNERS`](../CODEOWNERS) | Review-routing file; current entries are placeholders. |
| [`.github/PULL_REQUEST_TEMPLATE.md`](../PULL_REQUEST_TEMPLATE.md) | PR evidence, validation, rollback, and generated-receipt contract. |
| [`Makefile`](../../Makefile) | Local-parity command surface used by several workflows. |
| [`tools/ci/`](../../tools/ci/README.md) | Long-lived CI summary/helper logic. |
| [`tools/validators/`](../../tools/validators/README.md) | Validator implementation authority. |
| [`policy/`](../../policy/) | Policy authority. |
| [`schemas/`](../../schemas/) | Machine-shape authority. |
| [`contracts/`](../../contracts/) | Semantic object meaning. |
| [`tests/`](../../tests/) | Executable behavior evidence. |
| [`fixtures/`](../../fixtures/) | Deterministic test inputs. |
| [`data/receipts/generated/`](../../data/receipts/generated/README.md) | AI-authored artifact provenance records. |
| [`data/proofs/`](../../data/proofs/) | Proof objects. |
| [`release/`](../../release/) | Release decisions, manifests, corrections, and rollback. |
| [`infra/`](../../infra/) | Deployment, identity, network, and exposure posture. |
| [`DRIFT_REGISTER.md`](../../docs/registers/DRIFT_REGISTER.md) | Placement or behavior drift requiring explicit tracking. |

[Back to top](#top)

---

## ADRs

| ADR | Status at the evidence snapshot | Relevance |
|---|---|---|
| [`ADR-0018 — Promotion Gate Sequence`](../../docs/adr/ADR-0018-promotion-gate-sequence.md) | **PROPOSED, not accepted** | Defines a proposed canonical A–G outcome sequence. Do not claim current workflow enforcement from the ADR alone. |
| [`ADR-0011 — Receipts vs Proofs vs Manifests vs Catalog Separation`](../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) | **PROPOSED, not accepted** | Supports keeping CI artifacts distinct from receipts, proofs, catalog records, and publication. |

A new ADR is required when workflow work changes a KFM invariant, creates a parallel authority home, changes lifecycle or release semantics, or establishes a new privileged publication path. Routine workflow corrections and command wiring usually require a reviewed PR, not an ADR.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Date | **2026-07-17** |
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Base ref | `main` |
| Pinned evidence commit | `66610a2ee8bdc15713d1e5a5b0350081a1d7771c` |
| Review type | Repository-grounded documentation revision; workflow files and settings were not mutated. |
| Next review trigger | Any workflow add/delete/rename, stub graduation, permission change, trigger change, required-check change, or six months after this date. |

[Back to top](#top)

---

## Repository fit

```text
.github/
├── README.md                       # parent platform-governance documentation
├── CODEOWNERS                      # review routing; greenfield placeholder
├── PULL_REQUEST_TEMPLATE.md        # PR evidence and receipt contract
└── workflows/
    ├── README.md                   # this inventory and operating boundary
    ├── <command-bearing>.yml       # invokes repository-owned checks
    └── <greenfield-stub>.yml       # named future responsibility; no enforcement claim
```

The workflow subtree is a GitHub-shaped implementation lane inside the canonical `.github/` responsibility root. It must remain thin: GitHub-specific orchestration here, reusable logic in its owning implementation or authority root.

[Back to top](#top)

---

## Indexed workflow inventory

### Inventory summary

| Class | Count | Definition used in this revision |
|---|---:|---|
| Command-bearing | **7** | Indexed workflow with `runs-on` that invokes a repository test, validator, Make target, Node build/attestation chain, or artifact upload beyond an `echo TODO` scaffold. |
| Explicit greenfield stub | **34** | Indexed workflow with `runs-on` and the exact marker `Status: PROPOSED greenfield scaffold`. |
| Total indexed runnable-job files | **41** | Union of the two sets above. |

> [!NOTE]
> This is an **indexed runnable-job inventory**, not a byte-for-byte directory-tree proof. Any workflow without `runs-on`, any `.yaml` file, reusable workflow, disabled file, or search-index omission remains outside the confirmed count.

### Command-bearing workflows

| Workflow | Triggers observed | Command surface | Current limitations |
|---|---|---|---|
| [`api-test.yml`](api-test.yml) | Pull requests; pushes to `main` | `make governed-api-smoke`; targeted abstain-route pytest | File labels itself **PROPOSED trust-membrane CI wiring**; run results and branch requirement unknown. |
| [`contracts-validate.yml`](contracts-validate.yml) | All pushes and pull requests | Installs `.[test]`; runs `make test` | Broad trigger; effective token permissions and recent pass state unknown. |
| [`maplibre-perf-governance.yml`](maplibre-perf-governance.yml) | Path-scoped PR/push; manual dispatch | Node/Python setup, Playwright, perf/render/receipt/manifest/proof/failure chain, artifact uploads | Uses `id-token: write`; references `apps/web/**` and `schemas/maplibre/**`, which conflict with current Directory Rules guidance and require reconciliation. |
| [`pmtiles-attestation.yml`](pmtiles-attestation.yml) | PMTiles/tool/policy path-scoped PR; manual dispatch | Header, Merkle-sidecar, and COSE shape validation | Missing artifacts exit successfully; signature verification is shape-only. This is not publication attestation closure. |
| [`policy-boundary-guards.yml`](policy-boundary-guards.yml) | Path-scoped PR; manual dispatch | `make boundary-guards-ci`; JUnit upload | No explicit top-level `permissions:` block observed; effective permissions unknown. |
| [`schema-validation.yml`](schema-validation.yml) | Pull requests; pushes to `main` | Installs package; runs `make schemas` | Overlaps `validator-suite.yml`; duplication rationale and required-check status unknown. |
| [`validator-suite.yml`](validator-suite.yml) | Pull requests; pushes to `main` | `make schemas`; explicit invalid-EvidenceBundle fail-closed check | Covers only the declared invalid fixture in its negative job; broader gate coverage unknown. |

### Explicit greenfield stubs

These files are **CONFIRMED present as named scaffolds**. Their advertised function is **PROPOSED**, and an `echo TODO ...` job must not be represented as implemented validation.

| Family | Stub workflows |
|---|---|
| Platform, docs, UI, and security | `accessibility.yml`, `codeql.yml`, `dependency-scan.yml`, `docs-build.yml`, `docs-control-plane.yml`, `e2e-smoke.yml`, `link-check.yml`, `ui-build.yml` |
| Governance, trust, release, and source control | `citation-validation.yml`, `connector-gate.yml`, `contract-drift.yml`, `deny-test.yml`, `evidence-resolver.yml`, `focus-mock-test.yml`, `hydrology-proof-slice.yml`, `policy-test.yml`, `promotion-gate.yml`, `release-dry-run.yml`, `rollback-drill.yml`, `source-descriptor-validate.yml`, `telemetry-policy.yml` |
| Domain lanes | `domain-agriculture.yml`, `domain-archaeology.yml`, `domain-atmosphere.yml`, `domain-fauna.yml`, `domain-flora.yml`, `domain-geology.yml`, `domain-habitat.yml`, `domain-hazards.yml`, `domain-hydrology.yml`, `domain-people-dna-land.yml`, `domain-roads-rail-trade.yml`, `domain-settlements-infrastructure.yml`, `domain-soil.yml` |

### Stub graduation rule

A stub is ready to become command-bearing only when the PR identifies:

1. owner and reviewer burden;
2. trigger and changed-path scope;
3. explicit minimal permissions;
4. exact repository-native command;
5. deterministic valid and invalid fixtures;
6. network and secret posture;
7. outputs and retention;
8. stable job/check name;
9. failure and finite-outcome behavior;
10. disable, rollback, and documentation path.

[Back to top](#top)

---

## Trigger and permission preflight

### README-only change impact

At the pinned snapshot, a change to `.github/workflows/README.md` does **not** match the observed path filters in the MapLibre, PMTiles, or policy-boundary workflows. It does match broad `pull_request` workflows that do not narrow `paths`, including command-bearing validation workflows and several greenfield stubs.

Expected broad-trigger candidates include:

- `api-test.yml`;
- `contracts-validate.yml`;
- `schema-validation.yml`;
- `validator-suite.yml`;
- `codeql.yml` stub;
- `docs-build.yml` stub;
- `docs-control-plane.yml` stub;
- `link-check.yml` stub.

This means a documentation-only PR may launch jobs whose names imply more validation than they perform. Reviewers must inspect the job steps, not infer coverage from workflow names.

### Threat-preflight findings

| Check | Finding at the evidence snapshot | Posture |
|---|---|---|
| `pull_request_target` | No indexed match found. | **No privileged target-context trigger observed; inventory boundary applies.** |
| `workflow_run` chaining | No indexed match found. | **No chained privileged handoff observed; inventory boundary applies.** |
| Self-hosted runners | No indexed `self-hosted` match found. | **Hosted runners observed in inspected files.** |
| Secret references | No indexed `secrets.` match found. | **No direct secret reference observed; repository/environment secret policy remains unknown.** |
| Explicit write scopes | No indexed `contents: write`, `pull-requests: write`, `issues: write`, or `packages: write` match found. | **No ordinary write scope observed; effective defaults still need verification.** |
| OIDC | `id-token: write` appears in `maplibre-perf-governance.yml`. | **Requires justification and periodic review; that workflow is not triggered by this README path.** |
| Action refs | Inspected workflows use floating major tags (`@v6`, `@v7`). | **Supply-chain hardening needed; immutable SHA pinning is not confirmed.** |
| Fork-PR secret/write posture | No dedicated fork guard was established in this review. | **NEEDS VERIFICATION before any secret-bearing or write-emitting PR job is introduced.** |

[Back to top](#top)

---

## Workflow authoring contract

Every new or materially changed workflow should document these fields in the YAML comments, this README, a runbook, or the PR body:

| Field | Required answer |
|---|---|
| Responsibility | What single workflow family does this file own? |
| Trigger | Why these events, branches, paths, and schedules? |
| Untrusted-code posture | Can fork or external PR code execute, and in what token context? |
| Permissions | What is the minimal explicit `permissions:` set? |
| Runner | Why GitHub-hosted or self-hosted, and what is the trust boundary? |
| Network | Is the job no-network, dependency-network only, or source-activated live? |
| Command | Which repository-native command carries the logic? |
| Inputs | Which schemas, policies, fixtures, manifests, or source descriptors are pinned? |
| Outputs | What reports or artifacts are emitted, where, and for how long? |
| Outcome | What constitutes pass, fail, deny, hold, abstain, restrict, explicit skip, or system error? |
| Check name | Is the workflow/job name referenced by branch protection? |
| Rollback / disable | How can the workflow be safely disabled or reverted without weakening hidden obligations? |

### Naming and branch-protection discipline

- Workflow filenames should be stable, kebab-case, and responsibility-specific.
- Workflow `name`, job ids, and matrix-generated check names are compatibility surfaces once branch protection references them.
- A rename requires branch-protection verification and a migration note; never assume GitHub updates required checks automatically.
- A skipped gate is not a pass. Use explicit conditions and visible outcomes.
- Avoid duplicate workflows that run the same command unless the distinct responsibility, trigger, and required-check purpose are documented.

### Standard operational outcomes

| Outcome | Meaning |
|---|---|
| `WORKFLOW_PASS` | All declared checks ran and passed for the declared scope. |
| `WORKFLOW_FAIL` | Checks ran and found a defect. |
| `WORKFLOW_DENY` | Policy or governance blocks the requested action or exposure. |
| `WORKFLOW_HOLD` | Human, rights, sensitivity, release, correction, or rollback review is required. |
| `WORKFLOW_ABSTAIN` | The workflow lacks enough supported input to evaluate the requested gate. |
| `WORKFLOW_RESTRICT` | The action may proceed only under explicit constraints. |
| `WORKFLOW_SKIPPED_EXPLICIT` | A documented condition skipped the job visibly. |
| `WORKFLOW_KILL_SWITCH_ACTIVE` | An explicit kill switch prevented execution. |
| `WORKFLOW_PUBLIC_SURFACE_DENIED` | Public exposure is blocked. |
| `WORKFLOW_SYSTEM_ERROR` | Infrastructure, dependency, malformed configuration, or unexpected runtime failure prevented evaluation. |

These names are documentation vocabulary unless a contract/schema makes them normative. Do not emit a new machine enum from README prose alone.

[Back to top](#top)

---

## Required negative checks

Workflow suites should prove unsafe states fail closed, including:

- public API, UI, map, or AI access to RAW, WORK, QUARANTINE, candidate, internal/canonical, or direct-model stores;
- missing, stale, or mismatched policy bundles;
- contract/schema/fixture/validator/document drift;
- missing EvidenceRef-to-EvidenceBundle resolution, citation validation, receipt, proof, release reference, rollback target, or correction path where required;
- public exposure of rare-species, archaeology, cultural, critical-infrastructure, living-person, DNA/genomic, private-land, exact sensitive geometry, or source-restricted material;
- connector, watcher, or pipeline code promoting or publishing directly;
- source-role collapse, modeled-to-observed upgrade, AI-inferred authority, or aggregate-to-place overclaim;
- a required input missing while the job still reports success;
- diagnostic `|| true` masking the governing validation result;
- floating action or dependency drift changing behavior without review;
- secret, token, private endpoint, or restricted payload disclosure in logs or artifacts.

[Back to top](#top)

---

## Maintenance checklist

A workflow or workflow-documentation PR is ready for review when:

- [ ] The exact base commit and target files were inspected.
- [ ] Directory Rules placement and README requirements were checked.
- [ ] Overlapping workflow branches and pull requests were checked.
- [ ] Trigger expansion and privileged-event risk were reviewed.
- [ ] Permissions are explicit and least-privilege, or the unresolved default is documented.
- [ ] External actions are immutably pinned, or the pinning gap is recorded.
- [ ] Repository-native local parity exists for the governing command.
- [ ] Stub/TODO behavior is not described as implemented enforcement.
- [ ] Valid and invalid fixtures exercise finite outcomes and fail-closed behavior.
- [ ] Logs and artifacts are sensitivity-safe and retention-bounded.
- [ ] Workflow/job/check names are coordinated with branch protection.
- [ ] Release, publication, catalog, receipt, and proof boundaries remain separate.
- [ ] Failure diagnostics do not suppress the governing failure.
- [ ] A rollback/disable path is documented.
- [ ] `.github/README.md`, this README, Makefile/runbooks, and verification backlog are updated when behavior—not merely prose—changes.
- [ ] AI-authored changes include a schema-valid generated receipt and remain pending human review until approved.

[Back to top](#top)

---

## FAQ

### Does a workflow file's presence prove the check is implemented?

No. Thirty-four indexed workflow files explicitly call themselves greenfield scaffolds. Read the steps and invoked command before assigning implementation status.

### Is a passing stub safe to require in branch protection?

Not as substantive enforcement. An `echo TODO ...` job can pass while checking nothing. A required stub may create false assurance and should be graduated or clearly named as a placeholder before it carries governance weight.

### Can a workflow publish to `data/published/` or create a release?

Only through separately governed release machinery with explicit authority, policy, review, receipts/proofs, correction, and rollback. Ordinary CI and watchers are non-publishers.

### Are uploaded GitHub Actions artifacts KFM proof objects?

No. They are temporary platform artifacts unless an accepted, validated tool promotes their content into the correct governed home through an auditable state transition.

### Why are actions such as `actions/checkout@v7` called a risk?

A major tag is mutable. It is easier to maintain than a full SHA but does not provide immutable supply-chain pinning. KFM should record and deliberately resolve that tradeoff rather than calling it pinned.

### Why does the MapLibre workflow need special attention?

It is the only inspected workflow with `id-token: write`, it installs multiple network dependencies, and its path filters reference `apps/web/**` and `schemas/maplibre/**`, while current Directory Rules point to `apps/explorer-web/` and `schemas/contracts/v1/maplibre/`. That is a repository-grounded drift candidate, not a reason to rewrite it inside this README PR.

### Should duplicate schema-validation workflows be deleted here?

No. `schema-validation.yml` and `validator-suite.yml` both invoke `make schemas`, but deletion could break branch protection or reviewer expectations. First verify required checks, run history, intended ownership, and migration/rollback impact in a separate workflow PR.

[Back to top](#top)

---

## Open verification items

- **NEEDS VERIFICATION** — byte-complete inventory of `.github/workflows/`, including `.yaml`, reusable workflows, disabled files, and files without `runs-on`.
- **NEEDS VERIFICATION** — exact required-check names and branch-protection rules on `main`.
- **NEEDS VERIFICATION** — effective default `GITHUB_TOKEN` permissions at repository and organization scope.
- **NEEDS VERIFICATION** — current workflow run history, failure causes, duration, artifact contents, and pass rates.
- **NEEDS VERIFICATION** — whether `.github/CODEOWNERS` teams exist and required-review enforcement is active.
- **NEEDS VERIFICATION** — immutable SHA pinning plan for third-party actions and setup actions.
- **NEEDS VERIFICATION** — dependency-network and source-network allowlists for jobs that install packages or fetch browser binaries.
- **NEEDS VERIFICATION** — whether broad PR workflows should receive path filters to avoid unrelated doc-only execution.
- **NEEDS VERIFICATION** — whether `schema-validation.yml` and `validator-suite.yml` are intentionally distinct required checks or accidental overlap.
- **NEEDS VERIFICATION** — whether PMTiles no-artifact skips and shape-only signature checks meet their advertised assurance level.
- **CONFLICTED / NEEDS VERIFICATION** — MapLibre workflow paths `apps/web/**` and `schemas/maplibre/**` versus current Directory Rules placement.
- **NEEDS VERIFICATION** — parent `.github/README.md` still describes workflow inventory as unverified and should be synchronized in a separate bounded documentation change or the next behavior-changing workflow PR.
- **UNKNOWN** — which of the 34 stubs should be graduated, retired, consolidated, or kept as explicit roadmap placeholders.

[Back to top](#top)

---

## Changelog

| Date | Version | Change | Status |
|---|---|---|---|
| 2026-07-08 | v0.1 | Replaced the empty placeholder with a workflow-subtree governance README. | **CONFIRMED README / workflow behavior largely NEEDS VERIFICATION** |
| 2026-07-17 | v0.2 | Replaced the speculative future catalog with a pinned, repository-grounded 41-file indexed inventory; separated 34 explicit greenfield stubs from seven command-bearing workflows; added trigger/permission threat preflight, local-parity evidence, drift findings, stub-graduation rules, maintenance checks, and bounded open verification items. | **CONFIRMED documentation update / workflow execution and branch protection not changed** |

[Back to top](#top)
