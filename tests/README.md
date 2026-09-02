<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-readme
title: tests/ — Canonical Enforceability Root and Mixed-Maturity Test Matrix
type: README
version: v1.5
status: draft; repository-grounded; canonical test root; mixed-maturity; no-full-suite-established; non-authoritative
owner: "@bartytime4life — CONFIRMED CODEOWNERS review route; independent QA/test stewardship and separation-of-duties enforcement remain NEEDS VERIFICATION"
created: NEEDS VERIFICATION — file predates the v1.2 repository-grounded rewrite
updated: 2026-08-09
supersedes: v1.4 documentation at the same path; no executable behavior, fixture, workflow, release object, or public surface is superseded
policy_label: repository-facing; canonical-root; enforceability-proof; deterministic; no-network-default; fail-closed; public-safe; non-publisher
owning_root: tests/
responsibility: executable conformance, boundary, negative, integration, and end-to-end evidence for bounded KFM claims and behavior
truth_posture: cite-or-abstain; a passing test supports only its named assertion and checked revision and does not establish truth, source authority, policy approval, review completion, release, publication, or production parity
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 3a9715582adf17a682920ca98f15aa3582ee8cdc
  prior_blob: e639801cdda9a4e4df3ef01303103adc3aa556a4
  tests_tree: 48a0b599f93d5fef55e42ee3337dd0677e449773
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_decision: ADR-0029 accepted
  root_registry_blob: 024f668b5f0a9239bafa4f8b09e2afd86300ff8c
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  makefile_blob: 4abc7f941ce25d7d14703e87e387cef6e96d1592
  pyproject_blob: 074e2c505bcd748788c494bb9d0dd56e13ad91a9
  workflows_readme_blob: 6d83ab369cbb474be874130dc3cadc645c77323e
  current_workflows_tree: 8a7cb4967289754d59006447d0a2d002c53b4970
notes:
  - "v1.5 is a same-path documentation refresh. It changes no tests, fixtures, validators, workflows, policy, release state, or public surface."
  - "The accepted Directory Rules authority is docs/doctrine/directory-rules.md through ADR-0029; the older architecture copy is a compatibility surface and is no longer cited as canonical."
  - "The direct-child map is exact for the pinned tests tree. Deeper module inventories are selective and must not be read as a complete recursive audit."
  - "The prior 41-workflow snapshot and later 191-workflow snapshot are historical evidence only; current-main workflow count and complete behavior remain NEEDS VERIFICATION."
  - "No root-wide full-suite command, complete collected-case inventory, coverage report, mutation score, flake report, branch-protection mapping, or production-parity proof is established by this README."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/` — Canonical Enforceability Root and Mixed-Maturity Test Matrix

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Authority: canonical test root](https://img.shields.io/badge/authority-canonical%20test%20root-1f6feb?style=flat-square)](#authority-level)
[![Maturity: mixed](https://img.shields.io/badge/maturity-mixed-8250df?style=flat-square)](#status)
[![Full suite: not established](https://img.shields.io/badge/full%20suite-not%20established-b42318?style=flat-square)](#validation)
[![Network: denied by default](https://img.shields.io/badge/network-denied%20by%20default-15803d?style=flat-square)](#determinism-network-security-and-side-effects)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-level)

> **One-line purpose.** `tests/` owns authored, executable evidence that a declared KFM rule or behavior is enforceable for a bounded scope; it never becomes the authority for truth, contracts, schemas, policy, evidence, review, release, publication, or production state.

> [!IMPORTANT]
> A green test supports only the named assertion, fixture, gate, command, and checked revision. It does **not** by itself prove that a real-world claim is true, a source is admissible, evidence is adequate, policy approved exposure, human review occurred, a release is authorized, or production behaves the same way.

> [!CAUTION]
> No canonical root-wide full-suite command is established. [`make test`](../Makefile) runs only `tests/schemas` and `tests/contracts`; [`make validate`](../Makefile) adds the configured shared-validator aggregate but still omits many app-owned, package-local, domain, ingest, browser, release, runtime-proof, and workflow-specific suites.

## Navigation

- [Purpose](#purpose)
- [Authority level](#authority-level)
- [Status](#status)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Exposure, sensitivity, and storage](#public-exposure-sensitivity-mutability-retention-generation-and-storage)
- [Validation](#validation)
- [Review burden](#review-burden)
- [Related folders](#related-folders)
- [ADRs, migration, and aliases](#adrs-migrations-and-aliases)
- [Direct-child map](#direct-child-directory-map)
- [Last reviewed](#last-reviewed)
- [Verified execution surfaces](#verified-execution-surfaces)
- [Lane maturity](#lane-maturity-and-routing-matrix)
- [Minimum test contract](#minimum-test-case-contract)
- [Fixture contract](#fixture-and-test-data-contract)
- [Determinism and security](#determinism-network-security-and-side-effects)
- [CI maturity](#workflow-and-ci-maturity)
- [Open verification](#open-verification-register)
- [Rollback](#documentation-correction-and-rollback)

---

<a id="purpose-and-audience"></a>

## Purpose

`tests/` is KFM's canonical responsibility root for **executable conformance evidence**. It answers one bounded question:

> Can a declared contract, schema, policy boundary, source rule, lifecycle transition, validator behavior, application boundary, release prerequisite, or public-surface invariant be exercised deterministically with explicit expected outcomes and without the test becoming authority?

The root serves maintainers, reviewers, domain stewards, source and rights reviewers, contract and schema owners, validator authors, application and pipeline teams, CI owners, security reviewers, and release stewards.

A consequential test should make these facts inspectable:

- the system or rule under test;
- the implementation, contract, schema, policy, validator, fixture, and workflow bindings;
- the positive, negative, deny, restrict, abstain, stale, correction, withdrawal, or rollback condition expected;
- the filesystem, network, time, locale, randomness, and sensitivity assumptions;
- what a pass proves and what it explicitly does not prove;
- how a failure is diagnosed without leaking restricted material;
- whether correction or rollback of a test, fixture, workflow, baseline, or downstream artifact is required.

Tests participate in KFM's working control plane, but they remain subordinate to the responsibility roots that own meaning, shape, admissibility, evidence, release, and publication.

[Back to top](#top)

---

<a id="authority-and-directory-rules-basis"></a>

## Authority level

Accepted [`ADR-0029`](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) makes [`docs/doctrine/directory-rules.md`](../docs/doctrine/directory-rules.md) the single writable human Directory Rules authority. Its machine projection in [`control_plane/root_registry.yaml`](../control_plane/root_registry.yaml) classifies `tests/` as canonical and assigns it the responsibility **“Executable conformance, boundary, negative, integration, and end-to-end evidence.”**

| Field | Authority or boundary |
|---|---|
| **Root class** | Canonical, implementation-bearing responsibility root |
| **Primary responsibility** | Authored executable conformance and test routing |
| **Allowed canonical artifact kind** | `test` |
| **Prohibited canonical artifact kinds** | `data_instance`, `release_decision`, `test_fixture` |
| **Exposure** | Public repository content; committed tests and diagnostics must be public-safe for their declared review class |
| **Mutation** | Versioned through reviewed repository changes |
| **Retention** | Repository lifetime unless a narrower accepted rule applies |
| **Validation profile** | `executable_conformance` |
| **Review route** | `/tests/` routes to `@bartytime4life` in [CODEOWNERS](../.github/CODEOWNERS); required independent QA stewardship remains unverified |
| **Publisher status** | **No.** Tests and workflow results are review signals, not release or publication authority |

The existing path `tests/README.md` is correctly placed because it documents the root that owns test responsibility. This same-path update creates no root, moves no file, changes no lifecycle phase, and requires no new ADR.

### Responsibility boundary

| Responsibility | Authority home | Role of `tests/` |
|---|---|---|
| Semantic meaning and invariants | [`contracts/`](../contracts/README.md) | Assert against; never redefine |
| Machine-checkable shape | [`schemas/`](../schemas/README.md) | Validate against; never become schema authority |
| Admissibility, rights, sensitivity, access, obligations | [`policy/`](../policy/README.md) | Exercise reviewed rules or explicit mocks; never approve |
| Reusable validator implementation | [`tools/validators/`](../tools/validators/README.md) | Test entrypoints, diagnostics, polarity, replay, and side effects |
| Reusable deterministic fixtures | [`fixtures/`](../fixtures/README.md) | Consume and verify; do not shadow their authority |
| Test-local support inputs | `tests/fixtures/` | Existing bounded lane; conformance with the root prohibition on `test_fixture` authority remains **NEEDS VERIFICATION** |
| Source identity and activation | Governed source registry and control-plane surfaces | Exercise source admission; never admit or activate |
| Lifecycle material | Governed `data/` phases | Use synthetic or review-safe examples; never mutate canonical stores |
| Receipts and proofs | [`data/receipts/`](../data/receipts/README.md), [`data/proofs/`](../data/proofs/README.md) | Validate shapes and linkage; test output is not canonical by location |
| Promotion, release, correction, withdrawal, rollback | [`release/`](../release/README.md) | Exercise prerequisites and denial paths; never promote or publish |
| CI orchestration | [`.github/workflows/`](../.github/workflows/README.md) | Workflows invoke tests and report bounded outcomes |
| Application, package, runtime, renderer behavior | Accepted `apps/`, `packages/`, and `runtime/` homes | Exercise through bounded interfaces; adjacent owner-local tests may remain there when indexed |
| Temporary QA output | `artifacts/qa/` | Emit only with declared cleanup, retention, sensitivity, and claim limits |

> [!WARNING]
> `tests/` must not become a second schema, contract, policy, source registry, reusable fixture registry, validator implementation, data store, receipt store, proof store, release system, runtime, application, renderer, or publication root.

[Back to top](#top)

---

<a id="status-and-evidence-boundary"></a>

## Status

Snapshot: `main@3a9715582adf17a682920ca98f15aa3582ee8cdc`, tests tree `48a0b599f93d5fef55e42ee3337dd0677e449773`, inspected for this documentation revision on 2026-08-09.

### Confirmed at the pinned snapshot

- `tests/README.md` exists at prior blob `e639801cdda9a4e4df3ef01303103adc3aa556a4`.
- `tests/` has 28 direct child directories, listed in [Direct-child directory map](#direct-child-directory-map).
- Root Python test configuration and dependency bounds are present in [`pyproject.toml`](../pyproject.toml).
- The current [`Makefile`](../Makefile) exposes narrow aggregate targets plus bounded source, policy-boundary, release-prerequisite, evidence-resolver, hazards, governed-API, and MapLibre checks.
- `tests/contracts/` contains executable contract-fixture-manifest and identity-token-wiring tests.
- `tests/cross_domain/` contains executable classification/observation and environmental-observation boundary tests.
- `tests/evidence/`, `tests/governance/`, `tests/proof_pack/`, `tests/release/`, and `tests/runtime_proof/` contain executable modules.
- `tests/ingest/` contains executable watcher, materiality, and preflight suites with test-local inputs; the recursive inventory is not fully enumerated here.
- `tests/release/` now covers more than PromotionDecision shape: review records, promotion gates and receipts, verification execution, trust projection, carrier readiness, and a cosign-verification plan are represented by direct tests.
- Current CODEOWNERS routes `/tests/` and `/fixtures/` to `@bartytime4life`.
- Accepted ADR-0029 governs placement and supersedes the old architecture copy as canonical Directory Rules authority.

### Bounded or unverified

| Surface | Safe status | Claim limit |
|---|---|---|
| Root-wide full suite | `UNKNOWN / not established` | No accepted command explicitly composes all root, app, package, domain, browser, validator, and governed live tiers |
| Complete recursive test inventory and collected case count | `UNKNOWN` | Direct-child and selected-module evidence is not a full collection artifact |
| Coverage, mutation, duration, and flake metrics | `UNKNOWN` | No current governed aggregate report was inspected |
| Default no-network enforcement | `PARTIAL / NEEDS VERIFICATION` | Several Make targets set deterministic environment variables; no universal socket/network deny harness is proven |
| Policy evaluator and accepted bundle | `UNKNOWN` | Readiness and boundary tests do not establish active policy authority |
| UI, accessibility, browser, and composed E2E depth | `MIXED / NEEDS VERIFICATION` | Directory/workflow presence is not browser behavior proof |
| Current workflow count and complete workflow behavior | `NEEDS VERIFICATION` | The 41- and 191-workflow counts belong to older pinned snapshots; no current-main full audit is claimed |
| Required checks and branch protection | `UNKNOWN` | Repository ruleset evidence was not inspected for this revision |
| Production parity, release, publication | `DENIED as inference` | Tests, commits, workflows, and PRs do not establish those states |

### Material corrections from v1.4

- Replaced the obsolete canonical Directory Rules link with `docs/doctrine/directory-rules.md` and recorded accepted ADR-0029.
- Removed the stale current-tree implication from the historical 41-workflow inventory and bounded the later 191-workflow snapshot as historical.
- Corrected `tests/contracts/` from “no direct semantic suite established” to a bounded executable manifest/identity lane.
- Corrected `tests/cross_domain/` from documentation-only to executable boundary coverage while preserving its naming/authority question.
- Corrected `tests/release/` from a single PromotionDecision fixture check to a broader, still non-authoritative release-prerequisite suite.
- Corrected `tests/runtime_proof/` to acknowledge finite-outcome and soil runtime-mapper tests.
- Added the exact direct-child directory map required by Directory Rules v2's `ROOT_FULL` README profile.
- Preserved the no-full-suite, no-network-default, fail-closed, public-safe, non-publisher, and “passing does not prove” boundaries.

No test result, pass rate, source activation, policy approval, review completion, release readiness, deployment, or publication state is claimed by this README.

[Back to top](#top)

---

## What belongs here

Good fits for `tests/` include:

- deterministic schema, contract, validator, policy-boundary, source-admission, lifecycle, evidence-resolution, release, correction, rollback, API, runtime, UI, map, integration, and end-to-end assertions;
- positive and negative controls proving that a gate distinguishes supported from rejected states;
- test helpers whose sole responsibility is exercising tests;
- test-local configuration, collection rules, markers, manifests, and temporary inputs whose scope is explicit;
- regression tests for stable IDs, aliases, temporal semantics, source roles, citations, sensitivity transforms, correction propagation, and rollback;
- public-safe security tests for path traversal, boundary bypass, leakage, malformed input, resource limits, interrupted runs, and prohibited side effects;
- owner-local app, package, connector, or pipeline tests when adjacency is intentional and root orchestration indexes them.

### Route by the primary assertion

| Primary assertion | Preferred lane or owner |
|---|---|
| Machine shape, `$id`, `$ref`, fixture polarity | `tests/schemas/` |
| Semantic contract meaning, manifest binding, exclusions | `tests/contracts/` |
| Policy, obligations, rights, sensitivity, access | `tests/policy/` |
| Validator CLI, resolver, diagnostics, exit code, side effects | `tests/validators/` |
| Source identity, role, rights, cadence, citation, activation | `tests/source/` or the owning connector/domain lane |
| Ingest/watch/materiality/preflight behavior | `tests/ingest/` |
| Pipeline transformation, lifecycle, idempotency, partial failure | `tests/pipelines/` or owning package/domain suite |
| Governed API route and envelope behavior | `tests/api/` or explicit app-owned tests |
| Finite runtime outcome composition | `tests/runtime_proof/` or accepted owner-local suite |
| UI trust-state rendering, interaction, accessibility | `tests/ui/` or explicit app-owned suite |
| Map and georeference behavior | `tests/map/` |
| MapLibre renderer/performance boundary | `tests/maplibre/` pending complete placement and browser-depth review |
| Promotion, review, release prerequisite, correction, rollback | `tests/release/` |
| Proof-pack assembly and validation | `tests/proof_pack/` |
| Domain behavior | `tests/domains/<domain>/` |
| Genuinely cross-domain boundary | `tests/cross_domain/`, with namespace/conformance status stated |
| Complete composed request path | `tests/e2e/<owner>/` |
| Generic “valid” or “invalid” result | Route to the gate owner; `tests/valid/` and `tests/invalid/` are not default authority homes |

Tests should be near enough to their responsibility owner to remain intelligible and visible enough to avoid disappearing from orchestration, review, or promotion significance.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tests/` | Correct home or boundary |
|---|---|
| Canonical object meaning or invariants | `contracts/` |
| Canonical JSON Schema, enums, DTOs, OpenAPI | `schemas/` and verified API contract homes |
| Policy rules, allowlists, denylists, hidden thresholds, release decisions | `policy/` and accepted decision homes |
| Production validator logic hidden in tests | `tools/validators/`, packages, or the implementation owner |
| Reusable cross-cutting fixtures | `fixtures/` |
| Source descriptors, activation decisions, registry records | governed source registry/control-plane homes |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED payloads | correct governed `data/` phase |
| Canonical EvidenceBundle, receipt, proof, manifest, signature, rollback card | `data/proofs/`, `data/receipts/`, `release/` |
| Pipeline orchestration | `pipelines/` and `pipeline_specs/` |
| Application, shared library, renderer, or runtime implementation | `apps/`, `packages/`, `runtime/` |
| Production secrets, tokens, private endpoints, logs, personal data | denied; use synthetic/public-safe material |
| Exact protected species, archaeology, infrastructure, private-land, living-person, genealogy, DNA/genomic coordinates or identifiers | denied; use synthetic, withheld, generalized, aggregated, redacted, or denial cases |
| A generated report presented as evidence authority, policy approval, or release approval | accepted QA artifact lane with explicit claim limits |

A test must not redefine the rule it claims to verify in a way that makes the assertion tautological or creates a second authority.

[Back to top](#top)

---

<a id="inputs-and-outputs"></a>

## Inputs

Tests may read, when their contract permits:

- implementation code from accepted app, package, connector, pipeline, runtime, tool, and script homes;
- semantic contracts from `contracts/`;
- machine schemas from `schemas/`;
- reviewed policy and explicit policy fixtures from `policy/`;
- reusable fixtures from `fixtures/`;
- bounded local support inputs from `tests/fixtures/` pending fixture-placement conformance review;
- synthetic or review-safe source descriptors, registry records, receipts, proofs, and release objects;
- repository configuration, manifests, workflow metadata, and generated projections needed to test declared boundaries;
- explicit temporary directories, fixed clocks, deterministic environment variables, and caller-provided local paths.

### Input admission rules

- Pin or freeze inputs where reproducibility requires it.
- Deny undeclared outbound network access in default tests.
- Use public-safe, synthetic, generalized, or redacted values.
- Distinguish a fixture representing an object from an authoritative instance of that object.
- Make source role, temporal scope, expected outcome vocabulary, and review class explicit.
- Never invent a missing contract, schema, policy, registry, or fixture path to keep a test green.
- Fail or hold on unexpected empty discovery where nonempty coverage is required.

[Back to top](#top)

---

## Outputs

Accepted outputs include:

- test-framework results and exit codes;
- bounded stdout/stderr diagnostics;
- JUnit XML or equivalent QA reports;
- collection, skip, xfail, duration, and flake observations;
- coverage and mutation reports when configured and bounded;
- temporary files under test-owned directories;
- explicit readiness or hold summaries;
- candidate validation reports or receipts only when the owning schema, destination, cleanup, and claim limit are established.

Every output must state its role. A test log, JUnit file, screenshot, visual diff, fixture, generated report, or workflow summary is a **review signal**, not source truth, evidence closure, policy approval, release approval, or publication.

### Output safety

Outputs must not reveal credentials, tokens, private endpoints, internal filesystem secrets, exact sensitive locations or reconstruction hints, living-person or genomic data, private source terms, restricted payloads, or critical-infrastructure details beyond the approved review class.

Temporary QA outputs may use accepted locations such as `artifacts/qa/` only with explicit retention, correction, and cleanup behavior. Trust-bearing receipts, proofs, release records, and published objects remain in their canonical roots.

[Back to top](#top)

---

## Public exposure, sensitivity, mutability, retention, generation, and storage

| Dimension | Root contract |
|---|---|
| Public exposure | Repository-visible test source and committed diagnostics must be public-safe; public clients must not consume test files as normal data or authority |
| Sensitivity | Default to synthetic, generalized, redacted, withheld, or explicit denial cases; exact protected values are prohibited |
| Mutability | Versioned repository changes; no direct mutation of canonical stores or release records |
| Retention | Test source follows repository history; temporary outputs follow their artifact retention contract |
| Generated content | Must declare generator, source, edit policy, and claim limit; generated text is not authority |
| Physical storage | Test code belongs under its accepted owner; reusable fixtures under `fixtures/`; temporary QA output under an accepted artifact lane |
| Canonical writes | Denied. Tests must not write contracts, schemas, policy, registries, lifecycle stores, release decisions, or published carriers except through an explicit reviewed update action outside ordinary execution |

`tests/fixtures/` exists in the pinned tree. This README treats it as a bounded local-support lane, not reusable fixture authority. Its long-term conformance with the root registry's prohibition on `test_fixture` artifacts under `tests/` remains **NEEDS VERIFICATION**; no move or deletion is proposed here.

[Back to top](#top)

---

## Validation

### README validation

This file is evaluated against the accepted Directory Rules v2 `ROOT_FULL` profile:

- one H1, logical heading order, stable custom anchors, balanced fences, tables, alerts, and final newline;
- `kfm://doc/tests-readme`, the same path, the H1, and maintained compatibility anchors preserved;
- repository-relative links and named current commands checked against the pinned sources;
- current direct-child map derived from the pinned `tests/` tree;
- stale workflow counts and outdated lane-maturity claims removed or bounded;
- no secrets, real sensitive values, unsupported owners, pass rates, coverage, release, or production claims introduced.

### Repository-native commands

| Command | Confirmed current scope | Important limit |
|---|---|---|
| `make test` | `python -m pytest tests/schemas tests/contracts -q` | Narrow schema/contract aggregate only |
| `make schemas` | `python tools/validators/_common/run_all.py` | Configured shared-validator aggregate; not all validators or semantics |
| `make validate` | `make schemas` then `make test` | Partial aggregate, not full suite |
| `make hazards-validate` | Bounded synthetic USDM materiality unit tests and fixture validator with no-network environment | Hazards slice only |
| `make publish-check` | ReviewRecord and PromotionGate fixtures plus direct release tests with deterministic environment | Candidate prerequisite checks; no promotion or publication |
| `make evidence-resolver` | Candidate validator plus package tests | Internal candidate profile; not public evidence authority |
| `make evidence-resolver-deny` | Negative-only candidate fixtures plus package tests | Fail-closed profile; not complete resolver assurance |
| `make deny-test` | Governed API boundary tests under strict pytest settings | Narrow public-route/store/import boundary |
| `make boundary-guards` | Root policy-boundary and app API boundary tests | Structural/bounded, not an accepted policy evaluator |
| `make boundary-guards-ci` | Same suite plus JUnit under `artifacts/qa/` | QA report, not proof or release authority |
| `make governed-api-smoke` | App-owned governed API tests | App scope; not production parity |
| `make governed-api-verify` | App tests plus blocking forbidden renderer/model import scan | Import/source boundary, not runtime isolation |
| `make maplibre-perf` / `maplibre-govern` / `maplibre-proof` | MapLibre smoke, governance, and proof-shaped artifact checks | May generate artifacts; not root suite or release authority |

The following Make targets remain readiness markers that print `TODO` and return zero; they are not validation evidence: `policy`, `fixtures`, `proof-slice`, `catalog`, and `release-dry-run`.

### Documentation validation for v1.5

Performed for this update:

- complete prior-file read and material no-loss review;
- current main, target blob, tests tree, accepted Directory Rules, ADR-0029, root registry, CODEOWNERS, Makefile, pyproject, workflow README, and selected direct test trees inspected;
- stable-anchor and navigation review;
- Markdown structure, fence, link-target, stale-claim, and sensitive-content checks;
- remote byte and changed-path readback required after repository mutation.

Not performed by this documentation update:

- no repository test, validator, browser suite, policy engine, source connector, release dry run, rollback drill, deployment, or live endpoint was executed;
- no branch-protection setting, required-check mapping, production log, dashboard, coverage report, mutation score, or runtime trace was inspected;
- no executable behavior changed.

### Full-suite status

The following remains **PROPOSED**, not canonical:

```bash
python -m pytest tests -q
```

Even successful collection would not automatically include app-owned tests, package-local suites, Node/browser checks, validator CLIs, workflow readiness assertions, or governed live tiers. A canonical orchestrator must enumerate those surfaces, exclusions, budgets, and outcome semantics explicitly.

[Back to top](#top)

---

<a id="review-burden-and-change-control"></a>

## Review burden

Current [CODEOWNERS](../.github/CODEOWNERS) routes `/tests/` and `/fixtures/` to `@bartytime4life`. That is confirmed GitHub review routing, not proof of required code-owner review, independent QA stewardship, completed review, policy approval, release approval, or ruleset enforcement.

| Change type | Minimum review burden |
|---|---|
| Root test contract or full-suite semantics | Test/QA architecture, affected lane owners, CI, documentation |
| New direct lane or placement change | Test/QA, Directory Rules/architecture, implementation owner |
| Schema or contract tests | Test/QA, schema/contract owner, fixture owner |
| Policy, rights, sensitivity, access, or sensitive-data tests | Test/QA, policy, security/sensitivity, affected domain |
| Source-admission or ingest tests | Test/QA, source/registry, rights/sensitivity, connector/domain |
| Validator mechanics or CLI tests | Test/QA, validator/tooling, schema and fixture owners |
| Pipeline behavior tests | Test/QA, pipeline/package/domain, receipt/release reviewers where material |
| API, runtime, UI, browser, or E2E tests | Test/QA, app/runtime/UI, evidence/policy/release owners |
| Map/browser performance tests | Test/QA, renderer/UI, performance, security/release |
| Promotion, release, correction, withdrawal, rollback tests | Test/QA, release, evidence/policy, correction/rollback |
| Fixture changes | Test/QA, fixture consumer, domain/sensitivity reviewer where applicable |
| Workflow trigger, command, check-name, or artifact change | CI plus affected test owners; required-check coupling review |
| Skip, xfail, deletion, or narrowing of trust-spine coverage | Affected owners plus explicit risk and rollback note |
| Snapshot or baseline acceptance | Owning UI/map/test lane, source-fixture owner, human-reviewed reason |

### Separation of duties

- Test authors do not become sole approvers of policy-significant behavior.
- A passing test does not approve a source, policy decision, promotion, release, correction, or rollback.
- Workflow authorship, test authorship, human review, merge approval, and release/publication authority remain distinct where risk warrants it.
- Sensitive cases require the appropriate domain, rights, sovereignty, privacy, or security review.
- Generated test content and reports remain subordinate to accepted authority and human review.

[Back to top](#top)

---

## Related folders

| Related surface | Relationship to `tests/` |
|---|---|
| [`fixtures/`](../fixtures/README.md) | Reusable deterministic valid, invalid, deny, abstain, correction, and rollback examples |
| [`contracts/`](../contracts/README.md) | Meaning and invariants tests exercise |
| [`schemas/`](../schemas/README.md) | Machine shapes and identities tests validate |
| [`policy/`](../policy/README.md) | Admissibility rules and obligations tests exercise |
| [`tools/validators/`](../tools/validators/README.md) | Reusable validators whose mechanics require direct tests |
| [`apps/governed-api/`](../apps/governed-api/README.md) | App-owned governed API tests and boundary checks |
| [`apps/explorer-web/`](../apps/explorer-web/README.md) | Canonical public shell; browser/UI/a11y depth remains bounded |
| [`pipelines/`](../pipelines/README.md) | Lifecycle and non-publisher behavior under test |
| [`release/`](../release/README.md) | Promotion, correction, withdrawal, and rollback authority tests must not replace |
| [`data/receipts/`](../data/receipts/README.md) | Canonical process-memory records; test reports are not receipts by location |
| [`data/proofs/`](../data/proofs/README.md) | Proof authority; test results are supporting evidence only when explicitly admitted |
| [`.github/workflows/`](../.github/workflows/README.md) | Orchestrates CI, permissions, triggers, artifacts, holds, and check names |
| [`artifacts/qa/`](../artifacts/qa/README.md) | Temporary QA outputs under a declared contract |
| [`CONTRIBUTING.md`](../CONTRIBUTING.md) | Contribution, evidence, validation, review, and rollback expectations |
| [Directory Rules v2](../docs/doctrine/directory-rules.md) | Accepted placement doctrine and root README contract |
| [Root Registry](../control_plane/root_registry.yaml) | Machine projection of root classes and allowed/prohibited artifact kinds |

[Back to top](#top)

---

## ADRs, migrations, and aliases

| Decision or compatibility surface | Current status | Test-root consequence |
|---|---|---|
| [`ADR-0029`](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | **ACCEPTED** | `docs/doctrine/directory-rules.md` is canonical; `tests/` is a canonical test root |
| Root-wide full-suite orchestration | **OPEN / no accepted decision established** | Do not label partial Make targets as the full suite |
| `tests/fixtures/` versus `fixtures/` | **NEEDS VERIFICATION** | Reusable fixture authority remains `fixtures/`; no move is authorized here |
| `tests/valid/` and `tests/invalid/` | **OPEN** | Generic polarity lanes must not replace gate-owned suites |
| `tests/cross_domain/` namespace | **NEEDS VERIFICATION** | Executable tests exist; naming and long-term authority remain to be reconciled |
| `tests/maplibre/` versus owner-local renderer tests | **NEEDS VERIFICATION** | Preserve current bounded coverage; resolve before broad expansion |
| Runtime and policy outcome vocabularies | **CONFLICTED / NEEDS VERIFICATION** | Every test must name the profile it exercises |

No migration, alias, rename, deletion, or compatibility writer is introduced by v1.5. The path, document ID, H1, and custom compatibility anchors are preserved.

[Back to top](#top)

---

## Direct-child directory map

The map below is exact for `tests/` at the pinned tree and intentionally shows direct children only, as required by Directory Rules.

```text
tests/
├── api/             # Governed API routing and boundary tests
├── ci/              # CI helper, summary, and synchronization contract tests
├── contracts/       # Contract manifest, identity, and bounded semantic tests
├── cross_domain/    # Cross-domain boundary tests; namespace status needs verification
├── diff/            # Stable-diff and review-handoff tests
├── domains/         # Domain-specific test lanes
├── e2e/             # Composed-path and end-to-end tests or readiness surfaces
├── evidence/        # Evidence, temporal, reality-boundary, and representation tests
├── experiments/     # Experimental test work; not promotion evidence
├── fixtures/        # Bounded local support inputs; not reusable fixture authority
├── generators/      # Generator behavior and reproducibility tests
├── governance/      # Briefing, routing, issue-inventory, and governance tests
├── infra/           # Infrastructure and exposure-boundary tests
├── ingest/          # Ingest, watcher, materiality, and preflight tests
├── invalid/         # Generic invalid compatibility/routing lane
├── map/             # Map, geometry, and georeference tests
├── maplibre/        # MapLibre renderer and performance-governance tests
├── packages/        # Shared-package test lanes
├── pipelines/       # Pipeline, lifecycle, and non-publisher tests
├── policy/          # Policy shape, readiness, obligation, and boundary tests
├── proof_pack/      # Proof-pack assembly and verification tests
├── release/         # Review, promotion, release-prerequisite, and rollback tests
├── runtime_proof/   # Finite-outcome and runtime-mapping tests
├── schemas/         # Schema, identity, resolver, and fixture-binding tests
├── source/          # Source identity, role, descriptor, intake, and activation tests
├── ui/              # UI trust-state, interaction, and accessibility tests/readiness
├── valid/           # Generic valid compatibility/routing lane
└── validators/      # Validator CLI, resolver, diagnostics, and exit-contract tests
```

A child directory name proves only that the path exists. It does not establish owner, complete coverage, current passing state, workflow coupling, or production parity.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| **Date** | 2026-08-09 |
| **Repository snapshot** | `main@3a9715582adf17a682920ca98f15aa3582ee8cdc` |
| **Tests tree** | `48a0b599f93d5fef55e42ee3337dd0677e449773` |
| **Prior README blob** | `e639801cdda9a4e4df3ef01303103adc3aa556a4` |
| **Review class** | Documentation-only, repository-grounded, same-path semantic refresh |
| **Implementation changes** | None |
| **Review trigger** | Re-review when root/lane ownership, direct children, commands, aggregate membership, fixture authority, workflow maturity, required checks, outcome vocabularies, exposure, or correction/rollback behavior changes materially |

### Changelog

| Date | Version | Change | Status |
|---|---:|---|---|
| 2026-08-09 | v1.5 | Re-pinned the README to current main; adopted the canonical Directory Rules v2 path and ADR-0029 status; added the exact 28-child root map; corrected contracts, cross-domain, release, runtime-proof, evidence, governance, proof-pack, and ingest maturity; removed stale workflow-count claims; and preserved the non-authoritative test contract. | **CONFIRMED documentation change / executable maturity bounded** |
| 2026-07-31 | v1.4 | Reconciled the policy-boundary inventory with PR #1860's additional security regression test. | **LINEAGE / prior bounded correction** |
| 2026-07-23 | v1.3 | Reordered and refreshed the repository-grounded root contract. | **LINEAGE / prior repository-grounded edition** |
| 2026-07-16 | v1.2 | Replaced broad scaffold claims with a mixed-maturity test matrix and trust-spine contract. | **LINEAGE** |

[Back to top](#top)

---

<a id="confirmed-current-inventory"></a>

## Verified execution surfaces

This inventory is selective and evidence-bounded. It confirms representative executable surfaces without pretending to be a complete recursive count.

### Root orchestration and configuration

| Surface | Current behavior | Boundary |
|---|---|---|
| [`pyproject.toml`](../pyproject.toml) | Python `>=3.11`; `jsonschema>=4.26,<5`; exact RFC 3339, JCS, and YAML helpers; optional `pytest>=9.1.1,<10`; root `pythonpath` | Configuration, not collection or pass proof |
| [`Makefile`](../Makefile) `test` | `python -m pytest tests/schemas tests/contracts -q` | Narrow |
| `schemas` | Shared validator aggregate | Fixture-based, bounded |
| `validate` | `schemas` then `test` | Partial aggregate |
| `hazards-validate` | Synthetic USDM materiality tests and validator | Domain slice only |
| `publish-check` | ReviewRecord/PromotionGate fixtures and tests | No promotion or release |
| `evidence-resolver` / `evidence-resolver-deny` | Candidate positive/negative resolver profiles | Internal candidate, no publication |
| `boundary-guards` / `boundary-guards-ci` | Policy/API boundary tests; optional JUnit output | Structural/bounded |
| `governed-api-smoke` / `governed-api-verify` | App tests and blocking import-boundary check | App scope |
| MapLibre targets | Smoke, governance, proof-shaped artifact, cleanup | Mixed maturity; not root suite |

### Selected direct test lanes verified

| Lane | Representative current evidence | Safe conclusion |
|---|---|---|
| `tests/contracts/` | `test_contract_fixture_manifest.py`, `test_identity_token_wiring.py`, manifest fixtures | Bounded executable contract/identity coverage exists |
| `tests/cross_domain/` | classification/observation and environmental-observation boundary tests | Executable cross-domain boundary coverage exists; namespace acceptance remains open |
| `tests/evidence/` | reality-boundary, representation-fitness, temporal-authority, temporal-support tests | Bounded evidence/representation/temporal coverage exists |
| `tests/governance/` | BriefingSignal, deduplication, issue inventory, live inventory, materiality, GitHub inventory-read tests | Executable governance/intake routing coverage exists; live/network classification must be inspected per module |
| `tests/ingest/` | AQS watch, CDL watch, CSV/GeoJSON preflight, hydrology watcher and related suites | Substantial executable ingest/watch coverage exists; this README does not claim complete enumeration |
| `tests/proof_pack/` | proof-pack assembly and checker tests | Bounded proof-pack mechanics coverage exists; tests are not proof authority |
| `tests/release/` | cosign-plan, carrier-readiness, PromotionDecision, PromotionGate, PromotionReceipt, verification-execution, ReviewRecord, trust-projection tests | Broad prerequisite/shape/fixture coverage exists; no release is authorized |
| `tests/runtime_proof/` | finite-outcome envelope test and soil-moisture runtime mapper test | Bounded runtime composition coverage exists; full runtime proof is not established |
| `tests/schemas/` | common contracts, identity/resolver/fixture binding and family-specific checks | Partial machine-shape coverage exists |
| `tests/policy/` | boundary, readiness, obligation, vocabulary, and related checks | Mixed policy-shaped and structural coverage; active evaluator remains unverified |
| `tests/maplibre/` | renderer/performance-governance negative paths and related tests | Partial non-browser and governance evidence; browser/performance parity remains unverified |

### App- and owner-local companion suites

Tests outside the root may remain valid when their implementation owner is explicit. The current Makefile invokes app-owned governed-API tests. A future root registry must index owner-local suites so that adjacency does not make them invisible to orchestration, review, or promotion significance.

[Back to top](#top)

---

<a id="lane-maturity-and-routing-matrix"></a>

## Lane maturity and routing matrix

| Lane group | Current maturity | Safe conclusion | Preferred next proof |
|---|---|---|---|
| Contracts, schemas, validators | `EXECUTABLE / PARTIAL` | Shape, manifest, identity, resolver, and fixture checks exist | Complete discovery, semantic bindings, exit contracts, nonempty polarity |
| Policy and governance | `EXECUTABLE / MIXED` | Boundary/readiness/governance tests exist | Accepted evaluator/bundle, obligation replay, rights/sensitivity behavior |
| Source and ingest | `EXECUTABLE / MIXED` | Descriptor, intake, watcher, materiality, and preflight tests exist | Complete source-role, rights, cadence, activation, outage/replay matrix |
| Evidence and runtime proof | `EXECUTABLE / PARTIAL` | Temporal, representation, finite-outcome, and mapper tests exist | EvidenceRef→EvidenceBundle composition, freshness, policy/release coupling |
| Release and proof pack | `EXECUTABLE / BOUNDED` | Review/gate/receipt/verification/proof-pack mechanics are tested | Correction, withdrawal, rollback, signatures, cache invalidation, separation of duties |
| API | `MIXED / OWNER-LOCAL` | Governed API tests are invoked from the app owner | Auth, evidence, policy, release, abuse, and deployment-boundary coverage |
| UI, accessibility, browser, E2E | `NEEDS VERIFICATION / PARTIAL` | Paths and readiness surfaces exist | Hermetic browser harness, keyboard/ARIA, visible negative states, composed path |
| Map and MapLibre | `EXECUTABLE / PARTIAL` | Scalar/governance and map-related tests exist | Hermetic renderer fixtures, visual diff, runtime metrics, sensitivity/release parity |
| Domains and cross-domain | `MIXED` | Domain and boundary suites exist; depth varies | Per-lane owner, command, fixture, workflow, and collected-case registry |
| Generic `valid/` and `invalid/` lanes | `COMPATIBILITY / OPEN` | Path presence does not establish authority | Route each case to its owning gate or preserve explicit compatibility rationale |
| `tests/fixtures/` | `BOUNDED / NEEDS VERIFICATION` | Local support inputs exist | Decide conformance and migrate only with consumer/identity/rollback evidence |
| Experiments | `NON-PROMOTING` | Experimental checks may inform design | Graduation criteria before required-check or release significance |

A README, directory, workflow, or badge is not proof of executable depth. Use exact modules, commands, fixtures, collected cases, and run evidence for stronger claims.

[Back to top](#top)

---

<a id="trust-spine-and-lifecycle-invariants"></a>

## Trust spine and lifecycle invariants

Every consequential test should name the segment of the KFM trust spine it exercises:

```text
SOURCE ADMISSION
  -> RAW
  -> WORK / QUARANTINE
  -> PROCESSED
  -> CATALOG / TRIPLET
  -> PUBLISHED
  -> GOVERNED API / UI / MAP / AI CARRIERS
  -> CORRECTION / WITHDRAWAL / ROLLBACK
```

Promotion is a governed state transition, not a file move, test pass, workflow conclusion, commit, pull request, or merge.

### Required invariants

1. **No public/internal-store bypass.** Standard clients use governed interfaces, not RAW, WORK, QUARANTINE, candidate, canonical, or internal stores.
2. **No source-role upgrade.** Ingest, normalization, joining, rendering, AI summary, cataloging, and release do not silently increase authority.
3. **Cite or abstain.** Evidence-dependent claims resolve bounded support or narrow/abstain.
4. **Policy before exposure.** Rights, sensitivity, sovereignty, consent, living-person, infrastructure, archaeology, species, and location risks fail closed.
5. **Tests are not release.** Success cannot create or approve a PromotionDecision, ReleaseManifest, CorrectionNotice, WithdrawalNotice, or RollbackCard.
6. **Generated output is subordinate.** Model text, screenshots, tiles, graphs, indexes, summaries, and reports do not become truth because a test accepts them.
7. **Correction remains reachable.** Consequential paths preserve correction, invalidation, supersession, withdrawal, and rollback targets.
8. **Sensitive values do not leak.** Failures, snapshots, logs, JUnit XML, artifacts, and diagnostics remain public-safe for the declared review class.
9. **Empty discovery is not success.** Required suites and fixture polarities fail when nothing meaningful runs.
10. **Expected rejection is not harness failure.** Negative cases assert intended reason, output, and exit semantics.

[Back to top](#top)

---

<a id="minimum-test-case-contract"></a>

## Minimum test case contract

Every new consequential test should make support and limits reviewable.

```yaml
test_id: kfm.test.<owner>.<behavior>
owner:
  responsibility_root: tests
  lane: tests/<lane>
  steward: NEEDS VERIFICATION

system_under_test:
  implementation_refs:
    - path/to/code
  contract_refs:
    - contracts/...
  schema_refs:
    - schemas/...
  policy_refs:
    - policy/...
  validator_refs:
    - tools/validators/...

case:
  purpose: one bounded assertion
  preconditions: []
  fixture_refs: []
  fixture_class: valid | invalid | deny | restrict | abstain | error | stale | correction | rollback
  expected_test_result: pass
  expected_system_outcome: optional and vocabulary-qualified
  companion_case: kfm.test....
  deterministic: true
  network: denied
  filesystem:
    writes: temporary-only
    canonical_store_mutation: denied
  sensitivity:
    class: public-safe-synthetic
    exact_sensitive_values: denied
  evidence_posture: synthetic-ref | resolved-test-bundle | not-applicable
  policy_posture: exercised | mocked-explicitly | not-applicable
  release_posture: unreleased-test-only
  correction_ref: optional
  rollback_ref: optional

claim_limit:
  proves: named gates only
  does_not_prove:
    - truth
    - source authority
    - policy approval
    - review completion
    - production parity
    - release approval
    - publication
```

The YAML need not be serialized, but the same facts must be inspectable in code, metadata, fixtures, documentation, or an accepted registry.

[Back to top](#top)

---

<a id="required-test-classes"></a>

## Required test classes

### Foundation and governance

| Class | Required assertion |
|---|---|
| Schema conformance | Supported shape passes; unsupported shape fails; coverage cannot disappear silently |
| Contract semantics | Meaning, exclusions, maturity, and responsibility boundaries remain explicit |
| Validator mechanics | Registry, resolver, CLI, exit codes, diagnostics, polarity, replay, and side effects are predictable |
| Fixture integrity | Expected classes are present, public-safe, and linked to consumers |
| Identity and time | Stable identity and distinct time kinds remain explicit where material |
| Source admission | Identity, role, rights, sensitivity, cadence, citation, and activation fail closed |
| Evidence resolution | EvidenceRef resolves to adequate bounded support or result narrows/abstains |
| Policy behavior | Inputs, outcomes, obligations, reason codes, versions, digests, and replay are enforceable |
| Lifecycle transition | No phase is skipped and no public path reads pre-PUBLISHED state |
| Receipt and proof | Records match what ran and remain distinct from evidence and release authority |
| Release governance | Promotion, correction, withdrawal, supersession, and rollback require explicit support and review |

### Public, runtime, and reliability

| Class | Required assertion |
|---|---|
| Governed API | Routes, methods, envelopes, access, evidence, policy, release, and leakage boundaries hold |
| Runtime proof | Finite outcomes compose from evidence, policy, freshness, and release state under a named profile |
| UI trust state | Evidence, caveats, denial, correction, rollback, time, and accessibility remain visible |
| Map and renderer | Renderer consumes governed public-safe artifacts and preserves sensitivity/release boundaries |
| End-to-end | Complete request path composes lower-level gates without bypass |
| AI boundary | Generated language remains subordinate to resolved evidence and policy; unsupported claims abstain |
| No-network default | Default suite fails or blocks undeclared outbound access |
| Idempotency and replay | Fixed inputs produce equivalent results and no duplicate authority objects |
| Partial failure | Interrupted runs leave no silent promotion or canonical mutation |
| Correction propagation | Corrected/withdrawn support invalidates dependent carriers where required |
| Rollback drill | Targets are testable without treating the drill as an actual release action |
| Non-regression | Stable IDs, aliases, lineage, compatibility windows, and public behavior are preserved or migrated intentionally |

[Back to top](#top)

---

<a id="fixture-and-test-data-contract"></a>

## Fixture and test-data contract

| Home | Intended use | Guardrail |
|---|---|---|
| [`fixtures/`](../fixtures/README.md) | Reusable cross-cutting deterministic examples shared by tests, validators, and pipelines | Canonical reusable fixture responsibility; never source or lifecycle data |
| `tests/fixtures/` | Existing inputs local to one test area | Must not become independent reusable fixture authority; placement remains under review |

### Expected fixture families

| Family | Purpose |
|---|---|
| `valid` | One supported path succeeds at named gates |
| `invalid` | Malformed or unsupported shape/meaning fails |
| `deny` | Policy or access refusal is explicit and non-leaking |
| `restrict` / `redact` | Public-safe transform or staged access is enforced |
| `abstain` / `hold` | Insufficient evidence, freshness, review, or policy closure does not invent an answer |
| `error` | Harness, dependency, configuration, or runtime failure remains bounded |
| `stale` / `superseded` / `withdrawn` | Temporal and release-state invalidation works |
| `correction` | Correction linkage and dependent invalidation are testable |
| `rollback` | Reversal target and prerequisites remain inspectable |

A fixture-backed suite should fail or hold when a required family is empty, zero targets are discovered unexpectedly, an invalid case passes, a valid case fails, a consequential invalid case lacks expected-error evidence, a static negative scanner lacks a positive control, a path changes without consumer updates, sensitive values lack an approved transform, or a harness crash is misclassified as expected rejection.

### Sensitive-fixture safeguards

Never commit real exact protected-species locations, archaeology-sensitive coordinates, living-person identifiers, DNA/genomic material, private genealogy/consent data, critical-infrastructure details, restricted private-land records, secrets, credentials, private endpoints, or production logs.

Use synthetic, generalized, aggregated, redacted, withheld, or denied examples, and record why the transform is sufficient for the test.

[Back to top](#top)

---

<a id="outcome-vocabularies-and-claim-discipline"></a>

## Outcome vocabularies and claim discipline

Do not collapse result systems.

| Layer | Example vocabulary | Meaning |
|---|---|---|
| Test framework | passed, failed, skipped, error, xfail | Did the assertion execute as expected? |
| Process/CLI | exit `0`, `1`, `2`, or tool-specific nonzero | Did the command complete under its contract? |
| Schema validator | valid, invalid, harness/config error | Did the instance conform to configured shape? |
| Runtime envelope | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | What bounded runtime result is returned? |
| Policy | `ALLOW`, `RESTRICT`, `HOLD`, `DENY`, `ABSTAIN`, or named profile | What use is permitted and with which obligations? |
| Workflow readiness | hold, explicit skip, partial, failure, substantive pass | What maturity or drift state did CI establish? |
| Lifecycle | RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED | What governed state is material in? |
| Release | candidate, reviewed, promoted, held, withdrawn, superseded, rolled back | What is the governed release state? |

Tests must name the vocabulary/profile exercised and must not silently normalize conflicts.

```text
test executed
  -> named assertion passed
  -> configured gate behaved as expected
  -> bounded workflow step may rely on that result
  -> broader reliance requires every declared dependency
  -> release still requires governed promotion
```

Forbidden upgrades include: schema-valid to semantically true, fixture-accepted to source-admitted, validator-pass to evidence-closed, policy-shaped to policy-approved, workflow-green to full-suite-green, test-green to production parity, CI-green to release-approved, and rendered-output to published truth.

[Back to top](#top)

---

<a id="determinism-network-security-and-side-effects"></a>

## Determinism, network, security, and side effects

### Default posture

Default tests should be deterministic, local, no-network, synthetic or public-safe, time-controlled, locale-controlled where relevant, side-effect bounded, repeatable from a clean checkout, and explicit about temporary artifacts.

Several current Make targets set `KFM_NO_NETWORK=1`, `PYTHONHASHSEED=0`, `PYTHONDONTWRITEBYTECODE=1`, `PYTHONUNBUFFERED=1`, and `TZ=UTC`. That is bounded command evidence, not proof of universal enforcement across every Python, Node, browser, app-local, or package-local suite.

### Network classification

| Class | Rule |
|---|---|
| Default PR/local suite | Network denied; use deterministic fixtures and local mocks |
| Dependency installation | Separate build concern; does not permit test logic to call live sources |
| Explicit live tier | Opt-in, named, credential-scoped, rate-aware, non-publishing, and excluded from ordinary gates unless separately governed |
| Production or private endpoint | Denied from ordinary tests |

### Filesystem and side effects

Tests may write only to framework temporary directories, explicit temporary artifact roots, or accepted ignored QA locations with cleanup and retention rules. They must not mutate canonical contracts, schemas, policies, registries, lifecycle stores, release records, production configuration, published aliases, or committed baselines without an explicit reviewed update action.

Consequential suites should cover path traversal, symlink and repository-root escape, malformed/oversized payloads, recursion and resource bounds, secret/sensitive leakage, subprocess argument safety, temporary-file cleanup, sensitive-geometry reconstruction risk, no-publication and no-canonical-mutation side effects, cancellation cleanup, cache invalidation after correction/withdrawal/rollback, and public-client denial of pre-PUBLISHED stores.

[Back to top](#top)

---

<a id="coverage-non-vacuity-and-anti-tautology"></a>

## Coverage, non-vacuity, and anti-tautology

A green result is unacceptable when nothing meaningful ran.

| Risk | Required control |
|---|---|
| Zero tests collected | Assert expected minimum or registered count |
| Fixture-gated discovery disappears | Require expected bindings and nonempty polarity |
| Static scan sees no targets | Fail unless an approved empty state exists |
| Workflow reports readiness only | Label hold/skip; do not claim substantive behavior |
| Path filter misses an authority dependency | Test trigger manifest and update filters atomically |
| Negative case has no positive control | Pair with known-safe input |
| Positive case has no negative companion | Prove the gate is not unconditional |
| Aggregate omits executable validator | Compare membership to an accepted registry/manifest |
| Expected invalid prints generic failure | Assert reason, exit contract, and output prefix |
| `continue-on-error` or `|| true` masks a gate | Treat as informational unless separately asserted |
| Skips/xfails grow silently | Report and review changes |
| Snapshot changes auto-accept | Require human-reviewed reason and source-fixture linkage |
| Test reimplements the rule inline | Bind to independent contract/schema/policy/implementation authority |

A future governed coverage artifact should report lane, modules, collected cases, fixture polarity, implementation/contract/schema/policy bindings, commands, workflow callers and triggers, pass/fail/skip/xfail counts, metrics where meaningful, artifacts, promotion significance, and unresolved gaps. No complete artifact of that kind is established here.

[Back to top](#top)

---

<a id="current-local-execution-surfaces"></a>

## Current local execution surfaces

### Confirmed bounded commands

```bash
make test
make schemas
make validate
make hazards-validate
make publish-check
make evidence-resolver
make evidence-resolver-deny
make deny-test
make boundary-guards
make boundary-guards-ci
make governed-api-smoke
make governed-api-verify
```

MapLibre commands are also implemented but may create QA/performance artifacts and should be run only when that changed area is in scope.

### Important command limits

| Command | Major omissions |
|---|---|
| `make test` | Policy, source, ingest, evidence, governance, release, proof-pack, runtime-proof, MapLibre, app-owned, domain, E2E, UI, pipelines, most validator tests |
| `make schemas` | Validators outside the configured aggregate and semantic/policy/release behavior |
| `make validate` | Everything omitted by `make schemas` and `make test` |
| `make boundary-guards` | Accepted policy evaluator, obligations, complete source/lifecycle/release behavior, browser/UI runtime |
| `make publish-check` | Full evidence/policy/review/signature/release/correction/rollback closure |
| `make governed-api-smoke` | Root tests and production deployment behavior |
| Evidence-resolver commands | Live registry, public runtime outcome, complete policy/release composition |

A future command taxonomy should separate fast, standard, extended, browser, integration, security, release-drill, and governed live tiers.

[Back to top](#top)

---

<a id="workflow-and-ci-maturity"></a>

## Workflow and CI maturity

The current workflow tree is broader than the historical inventories documented in prior README editions. The `.github/workflows/README.md` records an exact 191-workflow count only for its pinned 2026-08-08 snapshot, not for the current main commit used here. This README therefore makes no current workflow-count claim.

### Safe workflow conclusions

- Workflow YAML is orchestration evidence, not current run evidence.
- Workflow names do not prove substantive commands, complete path filters, least privilege, required-check coupling, or production maturity.
- Holds, explicit skips, static readiness checks, schema-shape checks, and behavior tests are distinct outcomes.
- Workflows may invoke tests and produce review aids; they do not become policy, review, release, correction, rollback, or publication authority.
- Current exact triggers, path filters, permissions, actions, network, caches, artifacts, secrets/OIDC, job names, and hosted conclusions require a per-workflow audit at the exact head.

### CI acceptance contract

A workflow is not substantive test coverage until it invokes real assertions, fails on unexpected zero collection, covers authoritative dependencies, records exact commands and versions, declares network and secret posture, distinguishes expected rejection from harness failure, reports skips and exclusions, has an owner and correction path, states promotion significance, is locally reproducible where applicable, and has rollback/disable guidance.

[Back to top](#top)

---

<a id="failure-interpretation"></a>

## Failure interpretation

| Failure | Safe interpretation | Do not infer |
|---|---|---|
| Valid fixture fails | Shape, resolver, fixture, or binding drift | Real-world claim is false |
| Invalid fixture passes | Gate is too permissive | Policy approved the object |
| Contract test absent | Semantic enforceability is unproven | Contract prose is necessarily wrong |
| Validator exits nonzero | Validator or harness failed for that invocation | Automatic rollback or release denial beyond its contract |
| Boundary test fails | Named boundary may be violated | Complete policy decision exists |
| API test fails | Named route/envelope/boundary behavior drifted | Production service health is known |
| MapLibre scalar test fails | Local guard is violated | Browser rendering or map correctness is known |
| Readiness workflow succeeds | Inspected prerequisites/holds remain visible | Named implementation is complete |
| Readiness workflow fails | A boundary or assumption needs review | Surfaced code is necessarily wrong |
| Promotion prerequisite fails | Candidate chain is incomplete for that run | This README caused the gap |
| Zero tests collected | Coverage or routing is absent | Success |
| Sensitive-fixture review fails | Fixture is unsafe for the declared class | Real sensitive data should be exposed for debugging |

Failures should be actionable, bounded, and non-leaking.

[Back to top](#top)

---

<a id="what-a-passing-check-does-not-prove"></a>

## What a passing check does not prove

A pass does not by itself prove:

- source authority, admission, activation, current rights, or freshness;
- semantic correctness or evidence adequacy;
- sovereignty, cultural approval, consent, or sensitivity clearance;
- complete schema, validator, contract, or fixture coverage;
- complete policy evaluation or obligation fulfillment;
- review completion or separation of duties;
- lifecycle promotion, catalog/triplet closure, release approval, or publication;
- public safety, production deployment, production parity, or runtime availability;
- correction propagation or operational rollback readiness;
- branch-protection significance;
- absence of untested dynamic, owner-local, domain, browser, external, or live paths.

Use the narrowest statement supported by the assertion and all declared dependencies.

[Back to top](#top)

---

<a id="definition-of-done-for-the-root-test-system"></a>

## Definition of done for the root test system

The root test system is not complete merely because individual checks are green.

- [ ] Machine-readable registry of lanes, owners, modules, implementation bindings, fixtures, commands, workflows, and maturity.
- [ ] Accepted full-suite orchestrator or explicit tiered orchestration.
- [ ] Explicit inclusion of owner-local app, package, domain, validator, Node, and browser suites.
- [ ] No readiness or TODO marker reported as substantive testing.
- [ ] Zero-collection and nonempty-fixture safeguards.
- [ ] Stable test, CLI, validator, runtime, policy, workflow, lifecycle, and release vocabularies.
- [ ] Enforced deterministic no-network default.
- [ ] Sensitive-fixture review and leakage tests.
- [ ] Coverage for source admission, evidence resolution, policy, lifecycle, receipts/proofs, release, correction, rollback, API, runtime, UI, map, and E2E composition.
- [ ] Explicit contract/schema/policy/fixture/validator bindings.
- [ ] Structured QA artifacts with revision, command, environment, counts, failures, skips, and hashes.
- [ ] Trigger coverage for authoritative dependencies.
- [ ] Local/CI parity or documented, tested differences.
- [ ] Required-check and promotion significance recorded.
- [ ] Correction and rollback procedures for tests, fixtures, baselines, workflows, and QA artifacts.
- [ ] Accepted owners and review routes.
- [ ] Current pass, coverage, mutation, duration, and flake metrics reported without production-parity overclaim.

[Back to top](#top)

---

<a id="smallest-sound-improvement-sequence"></a>

## Smallest sound improvement sequence

1. **Inventory and register.** Record direct modules, helpers, fixture bindings, commands, workflows, owners, and maturity without making the registry authority.
2. **Make discovery non-vacuous.** Add zero-collection, nonempty-polarity, nonempty-target, and positive-control checks.
3. **Define tiered orchestration.** Separate fast, standard, extended, browser, security, release-drill, and governed live tiers with explicit budgets and exclusions.
4. **Audit triggers and artifacts.** Bind path filters to implementation, contract, schema, fixture, policy, helper, config, and documentation dependencies; define retention and sensitivity.
5. **Close governance behavior.** Add accepted policy evaluator, source-role/rights/sensitivity, lifecycle/idempotency, receipt, release, correction, withdrawal, and rollback tests.
6. **Close public surfaces.** Implement substantive UI, accessibility, browser, renderer, and composed E2E suites with hermetic defaults.
7. **Integrate promotion carefully.** Decide required checks through governed review and keep test authorship, policy review, merge approval, and release authority distinct.

Each step should be a dependency-closed, reviewable, reversible slice rather than a broad test-tree rewrite.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Question | Status | Required evidence |
|---|---|---|---|
| TEST-ROOT-01 | Who owns root test architecture and each lane beyond CODEOWNERS routing? | `NEEDS VERIFICATION` | Accepted stewardship and review/ruleset evidence |
| TEST-ROOT-02 | What is the canonical full-suite or tiered orchestrator? | `OPEN` | Accepted command contract and implementation |
| TEST-ROOT-03 | Should `make test` be renamed or expanded because it is narrow? | `OPEN` | Compatibility and maintainer decision |
| TEST-ROOT-04 | What belongs in `make validate`? | `OPEN` | Tier design, budget, and ownership |
| TEST-ROOT-05 | What is the complete root, app, package, domain, browser, and workflow test inventory? | `UNKNOWN` | Recursive inventory plus dynamic collection |
| TEST-ROOT-06 | What are complete collected case counts and metrics? | `UNKNOWN` | Governed QA collection artifact |
| TEST-ROOT-07 | Which fixture families require positive and negative polarity? | `OPEN` | Fixture contract and reviewed exceptions |
| TEST-ROOT-08 | Is `tests/fixtures/` a permitted local-support lane or a migration target? | `NEEDS VERIFICATION` | Directory conformance decision, consumer map, rollback plan |
| TEST-ROOT-09 | Should `tests/valid/` and `tests/invalid/` remain? | `OPEN` | Inbound-reference inventory and migration plan |
| TEST-ROOT-10 | How should app-owned tests be indexed by the root? | `OPEN` | Accepted ownership/routing registry |
| TEST-ROOT-11 | Is `tests/cross_domain/` the accepted namespace? | `NEEDS VERIFICATION` | Naming/placement decision with current consumers |
| TEST-ROOT-12 | Is `tests/maplibre/` the accepted renderer-test home? | `NEEDS VERIFICATION` | Package/app/root placement decision |
| TEST-ROOT-13 | Which runtime and policy outcome profiles are canonical? | `CONFLICTED` | Accepted contract/schema/policy decision |
| TEST-ROOT-14 | Which executable validators belong in the aggregate? | `UNKNOWN` | Entrypoint registry and completeness rule |
| TEST-ROOT-15 | What is the stable validator exit-code and diagnostics contract? | `OPEN` | Versioned contract and direct tests |
| TEST-ROOT-16 | Which policy evaluator and bundle are active? | `UNKNOWN` | Executable binding and run evidence |
| TEST-ROOT-17 | Which checks are required by branch protection? | `UNKNOWN` | Current repository ruleset evidence |
| TEST-ROOT-18 | Which checks block governed promotion? | `UNKNOWN` | Promotion policy and required-check mapping |
| TEST-ROOT-19 | Are current workflow path filters complete? | `NEEDS VERIFICATION` | Dependency-to-trigger audit at exact head |
| TEST-ROOT-20 | How is no-network behavior enforced across Python, Node, browser, and owner-local tiers? | `NEEDS VERIFICATION` | Harness and deny canaries |
| TEST-ROOT-21 | What resource limits apply? | `OPEN` | Security/performance contract |
| TEST-ROOT-22 | What sensitive-fixture review is mandatory? | `NEEDS VERIFICATION` | Review workflow and ownership |
| TEST-ROOT-23 | Which QA artifacts are retained and for how long? | `OPEN` | Artifact policy and cleanup evidence |
| TEST-ROOT-24 | How do correction and withdrawal invalidate baselines, caches, and dependent carriers? | `OPEN` | Consumer map and invalidation tests |
| TEST-ROOT-25 | Has an operational rollback drill executed? | `UNKNOWN` | Logs, receipts, and review record |
| TEST-ROOT-26 | Should readiness workflows share a machine-readable maturity vocabulary? | `OPEN` | Workflow contract and migration plan |
| TEST-ROOT-27 | What exact current-main workflow inventory and behavior is established? | `UNKNOWN` | Generated inventory and reviewed static/hosted audit |

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | Status | Supports | Limit |
|---|---:|---|---|
| Prior `tests/README.md` blob `e639801c...` | `CONFIRMED` | v1.4 doctrine, anchors, prior inventory, test/fixture/security/review contract | Stale authority path and several stale maturity claims |
| Accepted Directory Rules blob `fd49a0b8...` | `CONFIRMED doctrine` | Canonical root law, `ROOT_FULL` profile, dependency and public-client boundaries | Does not prove test behavior |
| ADR-0029 | `ACCEPTED` | Canonical Directory Rules identity and controlled compatibility migration | Does not approve tests or workflows |
| Root Registry blob `024f668b...` | `CONFIRMED projection` | `tests/` root class, responsibility, artifact kinds, exposure, mutation | Projection cannot amend doctrine or prove conformance |
| CODEOWNERS blob `dd2a84aa...` | `CONFIRMED routing` | `/tests/` and `/fixtures/` review route | Not completed review, policy, release, or ruleset evidence |
| Makefile blob `4abc7f94...` | `CONFIRMED` | Current commands, narrow aggregates, readiness markers | Command presence is not pass evidence |
| pyproject blob `074e2c50...` | `CONFIRMED` | Python and dependency constraints, pytest pythonpath | Does not prove collection or pass state |
| tests tree `48a0b599...` | `CONFIRMED` | Direct-child map and selected current module presence | No dynamic collection, pass result, or complete semantic audit |
| Workflow README blob `6d83ab36...` | `CONFIRMED pinned documentation` | Non-publisher and threat-preflight rules; historical 191-file snapshot | Not current-main workflow count or hosted result |
| Selected current test subtrees | `CONFIRMED source` | Contracts, cross-domain, evidence, governance, ingest, proof-pack, release, runtime-proof maturity corrections | Selective, not exhaustive |

### Material no-loss ledger

| Disposition | v1.5 treatment |
|---|---|
| `KEEP` | Document ID, path, H1, stable anchors, canonical-test-root purpose, trust spine, non-publisher rule, no-network default, public-safe fixture posture, outcome distinctions, pass limits, review and rollback discipline |
| `CLARIFY` | Tests as bounded evidence; root registry artifact restrictions; owner-local tests; test-local fixture tension; workflow/readiness distinctions |
| `REPAIR` | Canonical Directory Rules path and accepted ADR status; stale 41-workflow implication; outdated contracts/cross-domain/release/runtime maturity |
| `ENRICH` | Exact direct-child map, current evidence matrix, root-full exposure/storage fields, current Make targets, material change ledger, review triggers |
| `REMOVE_WITH_EVIDENCE` | Exact inventory/count claims that were not valid for current main; obsolete “one release test” and “documentation-only” lane statements |
| `SURFACE_CONFLICT` | `tests/fixtures/`, generic polarity lanes, cross-domain naming, MapLibre ownership, runtime/policy vocabularies, full-suite orchestration |

[Back to top](#top)

---

<a id="documentation-correction-and-rollback"></a>

## Documentation correction and rollback

This README is a routing and evidence-boundary document. It changes no executable behavior.

### Before merge

- close or abandon the draft pull request; or
- restore prior blob `e639801cdda9a4e4df3ef01303103adc3aa556a4` on the feature branch.

### After merge

- revert the documentation commit; or
- submit a corrective documentation PR pinned to the actual merged commit and current evidence.

### When implementation changes

Update this README when root or lane ownership, direct children, commands, fixture discovery or authority, aggregate membership, workflow commands/path filters/check names/permissions/artifacts, readiness graduation, outcome profiles, browser/UI/MapLibre/E2E placement, no-network enforcement, sensitive-case policy, required checks, QA artifact retention, or correction/rollback behavior changes materially.

A documentation rollback does not roll back tests, fixtures, validators, workflows, applications, data, releases, or production systems. Each has its own governed correction and rollback path.

[Back to top](#top)
