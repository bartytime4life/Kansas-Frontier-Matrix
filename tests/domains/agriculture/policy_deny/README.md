<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-agriculture-policy-deny-readme
title: tests/domains/agriculture/policy_deny/ — Agriculture Policy-Deny and Fail-Closed Test Boundary
type: readme; directory-readme; domain-test-sublane; policy-deny-enforceability-boundary
version: v0.2
status: draft; repository-grounded; README-only; policy-scaffolds-confirmed; outcome-contract-unresolved; fixture-payloads-unconfirmed; validator-unconfirmed; ci-stub; non-authoritative
owners: OWNER_TBD — Agriculture test steward · Agriculture domain steward · Policy steward · Sensitivity steward · Rights steward · Evidence steward · Fixture steward · Contract and schema steward · Validator steward · Runtime steward · Release steward · Security steward · Docs steward
created: NEEDS VERIFICATION — empty placeholder was expanded before v0.2
updated: 2026-07-16
supersedes: v0.1 Agriculture policy-deny test guide
policy_label: "public-review; tests; agriculture; policy-deny; fail-closed; field-level-deny; farm-operator-join-deny; unpublished-deny; ambiguity-abstain; rights-aware; sensitivity-aware; evidence-aware; source-role-preserving; no-network; synthetic-fixtures; release-gated; rollback-aware; no-public-authority"
current_path: tests/domains/agriculture/policy_deny/README.md
truth_posture: >
  CONFIRMED target v0.1 README and prior blob; canonical tests root; Agriculture parent
  test README; bounded repository search establishing no executable file under the policy_deny
  child lane; Agriculture policy parent README; policy intent and sensitivity documents;
  deny_unpublished.rego and abstain_on_ambiguous.rego as fourteen-line proposed stubs with
  default deny false and commented example rules; deny-field-level.rego and
  policy/sensitivity/agriculture/farm_operator_join.rego as six-line proposed scaffolds with
  default allow false; redaction_profiles.yaml as a proposed placeholder; field-level-attempt
  fixture README with no payload inventory confirmed; two competing Agriculture decision-envelope
  schema scaffolds; missing declared decision-envelope validator; policy-test and domain-agriculture
  workflows containing TODO-only echo jobs /
  PROPOSED policy-deny case contract, entrypoint normalization, finite outcome and reason-code
  vocabulary, negative and positive-control fixture matrices, no-network enforcement, public-surface
  leakage tests, policy unavailable behavior, correction and rollback cases, implementation
  sequence, definition of done, and migration plan /
  CONFLICTED default deny false in deny-named/abstain-named packages versus default allow false in
  field-level and farm-operator packages; abstain_on_ambiguous expressing a deny relation rather
  than an abstain relation; hyphenated and underscored package/path conventions; generic
  decision_envelope versus agriculture_decision_envelope schema families; policy intent claiming an
  executable bundle while inspected files remain scaffolds /
  UNKNOWN collected Agriculture policy-deny tests, actual fixture payloads, accepted policy
  query interface, OPA bundle manifest, reason-code contract, rights evaluator, EvidenceRef resolver,
  runtime adapter, Agriculture validator implementation, public API/UI denial integration, CI
  enforcement, current test results, coverage, owners, branch-protection significance, and
  production use /
  NEEDS VERIFICATION canonical policy package namespace, unified decision envelope, default outcome
  semantics, policy-data input contract, accepted fixture identity, output redaction contract,
  error handling, CODEOWNERS, release-gate adoption, correction propagation, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 01026cd58b1e687c4f8fa3363229b9857613102b
  prior_blob: 2921807aaf7c1881660d8fd7da4b35f9b6a613ba
  tests_root_blob: 5614de99433bca29d6a03d665fb4e00ec23eb5fb
  agriculture_tests_parent_blob: 35ebf2a578f2a39b4f4766cc4146aafde8124e67
  agriculture_policy_readme_blob: ba73c387e16f70895f32444e489d6d55dd577b75
  agriculture_policy_intent_blob: be42d02fae601f4b90a220f336ec36a848d2e51a
  agriculture_sensitivity_blob: 9d25f63d471af78899d8db2ad39a3921c4f11fac
  deny_unpublished_blob: 35c813606f37d3578230092fc526430e256b134d
  abstain_on_ambiguous_blob: 7733c0d6389e5e159346ab0bbd118b300970d728
  deny_field_level_blob: dc626a6975309e1356876715385c748bc30c18c2
  farm_operator_join_blob: 1b6128c4e2470f198edb6464424c6effc9d246dd
  redaction_profiles_blob: f13fbb93fb4b0b53f764c1d21b8189f81cfc0304
  field_level_fixture_readme_blob: b42a56c7dd3d22861818f734541eb36db05ace2f
  decision_envelope_schema_blob: 081d703e005ec192dd8c9f645e8dc8f7618f4fae
  agriculture_decision_envelope_schema_blob: 576685693115be431399d0b758686d7d806e371e
  agriculture_validator_readme_blob: ba9009bdecb6e007423122c32c53fffc3559976d
  policy_test_workflow_blob: 2bba88bb018600f54995d06b03cac02145b96fe7
  agriculture_workflow_blob: a9f5f212ef61d72fdc209d9f8b173bbf87fb1803
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
related:
  - ../README.md
  - ../aggregate_only/README.md
  - ../catalog_closure/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../policy/domains/agriculture/README.md
  - ../../../../policy/domains/agriculture/deny_unpublished.rego
  - ../../../../policy/domains/agriculture/abstain_on_ambiguous.rego
  - ../../../../policy/domains/agriculture/deny-field-level.rego
  - ../../../../policy/domains/agriculture/redaction_profiles.yaml
  - ../../../../policy/sensitivity/agriculture/farm_operator_join.rego
  - ../../../../fixtures/domains/agriculture/field_level_attempt/README.md
  - ../../../../schemas/contracts/v1/domains/agriculture/decision_envelope.schema.json
  - ../../../../schemas/contracts/v1/domains/agriculture/agriculture_decision_envelope.schema.json
  - ../../../../tools/validators/agriculture/README.md
  - ../../../../docs/domains/agriculture/POLICY.md
  - ../../../../docs/domains/agriculture/SENSITIVITY.md
  - ../../../../docs/runbooks/agriculture/NO_NETWORK_TEST_RUNBOOK.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../.github/workflows/policy-test.yml
  - ../../../../.github/workflows/domain-agriculture.yml
tags: [kfm, tests, agriculture, policy, deny, abstain, hold, restrict, fail-closed, opa, rego, field-level, farm-operator, evidence, rights, sensitivity, release, rollback, no-network]
notes:
  - "This revision changes only tests/domains/agriculture/policy_deny/README.md."
  - "The target lane remains README-only in bounded repository evidence; no executable test is created."
  - "Four Agriculture policy files are confirmed, but each is explicitly a proposed stub or scaffold."
  - "The current policy and Agriculture workflows execute TODO echo commands rather than OPA or Agriculture tests."
  - "No policy, fixture, schema, contract, validator, workflow, receipt, proof, release record, data object, or public route is modified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/domains/agriculture/policy_deny/` — Agriculture Policy-Deny and Fail-Closed Test Boundary

> **One-line purpose.** Define the enforceability boundary for proving that unsafe, unsupported, unpublished, ambiguous, rights-unclear, sensitivity-unclear, or over-precise Agriculture requests cannot escape as public data, catalog truth, release approval, map output, report content, export, or AI answer.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: policy deny" src="https://img.shields.io/badge/lane-policy__deny-success">
  <img alt="Maturity: README only" src="https://img.shields.io/badge/maturity-README__only-lightgrey">
  <img alt="Policy: scaffolds" src="https://img.shields.io/badge/policy-scaffolds-orange">
  <img alt="CI: TODO only" src="https://img.shields.io/badge/CI-TODO__only-critical">
</p>

> [!IMPORTANT]
> **Policy denial is a governed outcome, not a generic rejection.** A meaningful deny test must identify the policy entrypoint, bounded input, expected finite outcome, safe reason code, obligations, redaction posture, audit linkage, and the downstream surfaces that must remain blocked.

> [!CAUTION]
> **Current enforcement is not established.** The `policy_deny/` directory is README-only in bounded search. The inspected Agriculture Rego files are proposed stubs or scaffolds, their defaults are not harmonized, fixture payloads are unconfirmed, decision-envelope schemas are permissive placeholders, and the workflows run TODO echo commands.

> [!WARNING]
> **Deny output must not leak what it protects.** Tests must verify both the decision and the response boundary. A correct `DENY` that returns private geometry, operator identity, parcel joins, proprietary yield, restricted source detail, or sensitive policy internals is still a failed test.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Does not](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Inventory](#confirmed-policy-inventory) · [Decision model](#policy-decision-model) · [Case matrix](#required-test-case-matrix) · [Fixtures](#no-network-and-fixture-posture) · [Public surfaces](#public-surface-denial-contract) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Rollback](#migration-correction-and-rollback) · [Open](#open-verification-register) · [Done](#definition-of-done) · [Last reviewed](#last-reviewed)

---

## Purpose

`tests/domains/agriculture/policy_deny/` is the Agriculture test sublane for **negative policy behavior and fail-closed proof**.

A complete policy-deny test family should answer:

1. Which Agriculture operation, object family, audience, precision, and lifecycle state is being evaluated?
2. Which policy package and stable decision entrypoint is queried?
3. Which source role, rights, sensitivity, evidence, validation, receipt, review, and release inputs are present?
4. Which required input is missing, negative, stale, contradictory, or unsafe?
5. Is the correct finite result `DENY`, `ABSTAIN`, `HOLD`, `RESTRICT`, or `ERROR`?
6. Is the reason code stable, bounded, and safe to expose?
7. Are obligations preserved without disclosing protected details?
8. Are catalog, release, API, UI, map, tile, report, export, graph, search, and AI paths blocked appropriately?
9. Is the denied candidate kept out of `PUBLISHED` state?
10. Can correction, supersession, withdrawal, or rollback restore a prior safe state when policy changes?

The lane focuses on Agriculture conditions such as:

- exact field-level public exposure;
- farm, operator, person, parcel, ownership, or private-party joins;
- proprietary yield or production records;
- pesticide or application detail;
- NASS-confidential or source-restricted content;
- unresolved rights, sensitivity, or EvidenceBundle support;
- unpublished or rollback-blocked release posture;
- missing aggregation, redaction, validation, review, or release support;
- aggregate or modeled products being presented with unsupported precision;
- quarantine-adjacent material reaching a public surface;
- policy runtime, bundle, or input-contract failure.

This README defines enforceability expectations. It does not claim the tests, fixtures, policy rules, evaluators, validators, runtime adapters, or release integrations are complete.

[Back to top](#top)

---

## Authority level

**Canonical test responsibility / non-authoritative Agriculture sublane.**

`tests/` owns authored enforceability proof. Agriculture is a domain segment under that root. This lane tests policy behavior; it does not create policy, domain meaning, schema shape, source authority, evidence, receipts, release decisions, or public interfaces.

| Concern | Authority home | This lane's role |
|---|---|---|
| Enforceability proof | `tests/` | Owns test modules and assertions. |
| Agriculture test organization | `tests/domains/agriculture/` | Owns domain test grouping. |
| Agriculture policy code | `policy/domains/agriculture/` and accepted cross-cutting policy lanes | Executes rules; tests do not redefine them. |
| Agriculture policy intent | `docs/domains/agriculture/POLICY.md` and sensitivity doctrine | Supplies review intent; not runtime proof. |
| Agriculture object meaning | `contracts/domains/agriculture/` | Tests meaning; does not redefine it. |
| Agriculture machine shape | `schemas/contracts/v1/domains/agriculture/` | Tests schema behavior; does not author schemas. |
| Rights and sensitivity | `policy/rights/`, `policy/sensitivity/`, source registry, and governed review | Tests decisions and inheritance. |
| Evidence support | Evidence contracts and `data/proofs/` | Tests resolution; does not create proof authority. |
| Receipts | `data/receipts/` and receipt contracts | Tests required linkage; does not store receipts here. |
| Fixtures | `fixtures/domains/agriculture/` | Consumes synthetic examples; does not duplicate fixture authority. |
| Validators and policy runtime | `tools/validators/`, `packages/policy-runtime/`, or accepted runtime lane | Tests behavior; does not implement durable tooling. |
| Lifecycle data | Governed `data/` lifecycle roots | Uses synthetic references only. |
| Release, correction, rollback | `release/` | Tests blocking/readiness; cannot approve transitions. |
| CI workflow | `.github/workflows/` | Calls substantive tests when implemented. |
| Public API/UI/map/AI behavior | Governed apps and released artifacts | Tests denial boundaries; cannot expose a route. |

### Anti-collapse rules

This lane must not collapse:

- a policy README into executable policy;
- a Rego file into a complete policy bundle merely because it parses;
- `default allow := false` into a fully reasoned deny decision;
- `default deny := false` into public permission;
- `DENY` into `ABSTAIN`, `HOLD`, or `RESTRICT` without a contract;
- schema validity into policy admissibility;
- EvidenceBundle support into release approval;
- a receipt into proof;
- a policy decision into catalog truth;
- a passing test into steward approval;
- a green TODO workflow into enforcement;
- aggregate data into field or operator truth;
- denied payloads into safe payloads merely because response status is denied.

[Back to top](#top)

---

## Status

### Confirmed repository evidence

At `main@01026cd58b1e687c4f8fa3363229b9857613102b`, bounded evidence establishes:

```text
tests/domains/agriculture/policy_deny/
└── README.md
```

No executable test under this child directory surfaced in the bounded repository search.

The policy surfaces inspected are:

```text
policy/domains/agriculture/
├── README.md
├── abstain_on_ambiguous.rego
├── deny-field-level.rego
├── deny_unpublished.rego
└── redaction_profiles.yaml

policy/sensitivity/agriculture/
└── farm_operator_join.rego
```

### Maturity matrix

| Surface | Status | Safe conclusion |
|---|---:|---|
| Target README | **CONFIRMED** | Prior v0.1 documentation existed. |
| Child-lane executable tests | **NOT ESTABLISHED** | No collected test module was found under this path. |
| `deny_unpublished.rego` | **PROPOSED STUB** | Declares `default deny := false`; real rule is commented out. |
| `abstain_on_ambiguous.rego` | **PROPOSED STUB / SEMANTIC MISMATCH** | Declares a `deny` relation rather than a confirmed abstain result. |
| `deny-field-level.rego` | **PROPOSED SCAFFOLD** | Declares only `default allow := false`. |
| `farm_operator_join.rego` | **PROPOSED SCAFFOLD** | Declares only `default allow := false`. |
| `redaction_profiles.yaml` | **PROPOSED PLACEHOLDER** | Contains status, source document, path, and one note only. |
| Field-level fixture payloads | **NOT ESTABLISHED** | Fixture README exists; payload inventory was not confirmed. |
| Policy input contract | **UNKNOWN** | No accepted input schema or bundle manifest was established. |
| Decision-envelope schema | **CONFLICTED / PLACEHOLDER** | Two schema names exist; both are permissive scaffolds. |
| Declared decision validator | **NOT FOUND** | Search surfaced the schema reference, not the implementation. |
| Policy runtime integration | **UNKNOWN** | No evaluated Agriculture policy adapter was verified. |
| `policy-test` workflow | **TODO ONLY** | Runs `echo TODO opa-test` and fixture-coverage TODO. |
| `domain-agriculture` workflow | **TODO ONLY** | Agriculture validation/build/publish jobs echo TODO. |
| Current OPA/pytest results | **UNKNOWN** | No execution evidence was established here. |
| Owners/CODEOWNERS | **OWNER_TBD** | Responsibility remains unresolved. |

### Default-rule conflict

The current policy scaffolds use two incompatible shapes:

| File family | Default | Risk if misread |
|---|---|---|
| `deny_unpublished.rego`, `abstain_on_ambiguous.rego` | `default deny := false` | Absence of implemented rules may appear non-denying. |
| `deny-field-level.rego`, `farm_operator_join.rego` | `default allow := false` | Absence of implemented rules may appear fail-closed but lacks reason/outcome semantics. |

These defaults are not automatically composable. A consumer must not infer a unified Agriculture policy result by OR-ing or inverting unrelated booleans.

### Decision-envelope conflict

Two machine-shape candidates exist:

| Path | Confirmed shape | Status |
|---|---|---|
| `schemas/contracts/v1/domains/agriculture/decision_envelope.schema.json` | Requires `id`; permits arbitrary fields; declares a validator path not found | PROPOSED placeholder |
| `schemas/contracts/v1/domains/agriculture/agriculture_decision_envelope.schema.json` | Empty `properties`; permits arbitrary fields; points to an unverified contract | PROPOSED scaffold |

No accepted relationship between these two schemas was verified.

[Back to top](#top)

---

## What belongs here

- This README and lane-local test indexes.
- Executable Agriculture negative-policy tests after placement is accepted.
- OPA/Rego unit tests for Agriculture policy entrypoints.
- Python or runtime-adapter tests that verify normalized finite outcomes.
- Tests for exact field, operator, farm, parcel, ownership, and private-party denial.
- Tests for unpublished, withdrawn, superseded, or rollback-blocked material.
- Tests for rights-, sensitivity-, evidence-, validation-, receipt-, review-, and release-missing cases.
- Tests that distinguish `DENY`, `ABSTAIN`, `HOLD`, `RESTRICT`, and `ERROR`.
- Tests for safe reason codes and non-leaking denial payloads.
- Tests that denied candidates cannot enter catalog, release, published, public API/UI, map, report, export, graph, search, or AI paths.
- Positive control tests proving that a reviewed aggregate/generalized/restricted case is not denied for the wrong reason.
- Deterministic no-network tests using synthetic public-safe fixtures.
- Regression tests for correction, supersession, withdrawal, and rollback behavior.
- Test-only references to policy, schemas, contracts, fixtures, validators, evidence, receipts, and release records.

[Back to top](#top)

---

## What does not belong here

| Do not place here | Correct authority home |
|---|---|
| Agriculture Rego or other policy implementation | `policy/domains/agriculture/` or accepted policy lane |
| Rights or sensitivity policy | `policy/rights/`, `policy/sensitivity/` |
| Policy intent or Agriculture doctrine | `docs/domains/agriculture/` |
| Semantic contracts | `contracts/` |
| JSON Schemas | `schemas/` |
| Policy-runtime implementation | `packages/policy-runtime/`, runtime, or accepted implementation lane |
| Durable validators | `tools/validators/` |
| General fixture libraries | `fixtures/` |
| SourceDescriptor or source activation records | source registry roots |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | governed `data/` lifecycle roots |
| EvidenceBundle, proofs, or claim support | `data/proofs/` |
| Receipts | `data/receipts/` |
| ReleaseManifest, PromotionDecision, CorrectionNotice, WithdrawalNotice, RollbackCard | `release/` |
| Public API, UI, map, tile, report, export, graph, search, or AI code | governed application and publication roots |
| Real private farm/operator/parcel data | approved private systems or QUARANTINE—not test fixtures |
| Secrets, credentials, private endpoints, or policy-sensitive internal thresholds | approved secret/configuration mechanisms |
| Generated language treated as expected policy truth | authored fixtures and explicit assertions |

[Back to top](#top)

---

## Inputs

Policy-deny tests should consume explicit, synthetic, bounded inputs.

### Required input families

| Input family | Minimum test context |
|---|---|
| Request context | operation, audience, route/surface, requested precision, purpose |
| Agriculture object context | object family, stable ID, version, source role, lifecycle state |
| Spatial context | county/region/grid/HUC versus field/parcel/exact geometry |
| Temporal context | crop year, season, observation period, freshness |
| Source context | source ID, source role, rights/license state, provenance |
| Evidence context | EvidenceRef, EvidenceBundle resolution, citation state |
| Sensitivity context | tier/classification, exactness, join risk, inheritance |
| Rights context | allowed, restricted, unknown, attribution required, agreement-bound |
| Transform context | aggregation, generalization, redaction, suppression profile |
| Receipt context | AggregationReceipt, RedactionReceipt, ValidationReceipt, RunReceipt refs |
| Review context | steward/reviewer status, unresolved questions |
| Release context | candidate, released, superseded, withdrawn, rollback requested |
| Policy context | package, version/digest, entrypoint, input schema version |
| Failure injection | missing field, malformed policy, runtime unavailable, conflicting policy result |

### Input admission rules

Tests must reject or explicitly classify:

- unknown policy package or query path;
- undeclared input fields that materially change a result;
- unversioned or unhashed policy bundles in release-sensitive tests;
- real credentials or live endpoint configuration;
- real field/operator/person/parcel identifiers;
- exact private geometry;
- ambiguous source roles;
- invented EvidenceBundle resolution;
- missing release or rollback state where public impact is tested;
- fixtures that can be mistaken for released records;
- network-dependent inputs in the default suite.

### Minimum synthetic marker

Every fixture should carry an obvious non-production marker, such as:

```json
{
  "_mock": true,
  "fixture_id": "kfm-test-agriculture-policy-deny-001",
  "public_safe": true
}
```

The exact field names are **PROPOSED** until fixture contracts are accepted.

[Back to top](#top)

---

## Outputs

A policy-deny test should produce authored assertions and, when a test runner supports it, a bounded test report.

It must not emit canonical policy decisions, release records, or public payloads.

### Expected assertion surface

| Field | Purpose |
|---|---|
| `case_id` | Stable test-case identity |
| `policy_package` | Package or bundle under test |
| `entrypoint` | Exact query/decision path |
| `input_ref` | Synthetic fixture reference |
| `expected_outcome` | `ALLOW`, `DENY`, `RESTRICT`, `HOLD`, `ABSTAIN`, or `ERROR` |
| `expected_reason_codes` | Exact bounded reason-code set |
| `expected_obligations` | Required aggregation, redaction, review, citation, rollback, etc. |
| `forbidden_fields` | Fields that must not appear in the response |
| `blocked_surfaces` | Catalog/release/API/UI/map/report/export/AI surfaces blocked |
| `expected_lifecycle_state` | Hold/quarantine/no-publish posture |
| `policy_digest` | Policy input/version binding when implemented |
| `result` | Test pass/fail only |

### Finite test outcomes

| Outcome | Test meaning |
|---|---|
| `PASS` | Actual policy behavior matches the authored case contract. |
| `FAIL` | Decision, reason, obligations, redaction, or downstream blocking differs. |
| `SKIP` | Allowed only for an explicitly unavailable optional dependency; not for missing core policy. |
| `ERROR` | Test infrastructure could not evaluate behavior. |
| `NOT_IMPLEMENTED` | Explicit maturity marker; must not count as passing enforcement. |

### Forbidden output claims

A test run must not claim:

- that a denied Agriculture claim is false;
- that an allowed case is true;
- that policy evaluation is release approval;
- that schema validity is policy validity;
- that a receipt is proof;
- that a fixture is source evidence;
- that a workflow passed substantive policy tests when it only ran TODO commands;
- that protected data may be echoed because the final outcome is `DENY`.

[Back to top](#top)

---

## Confirmed policy inventory

### `deny_unpublished.rego`

```rego
package kfm.agriculture_deny_unpublished

default deny := false
```

The file labels itself a proposed greenfield stub. Its only example deny rule is commented out.

**Safe conclusion:** the package exists and may parse; unpublished-denial behavior is not implemented by the inspected text.

### `abstain_on_ambiguous.rego`

```rego
package kfm.agriculture_abstain_on_ambiguous

default deny := false
```

The package name says “abstain,” but its only relation is `deny`, and the example is commented out.

**Safe conclusion:** the package name communicates intent; no confirmed abstain output contract exists.

### `deny-field-level.rego`

```rego
package kfm.generated.policy.domains.agriculture.deny_field_level

default allow := false
```

No rule, reason code, obligation, or decision object is present.

**Safe conclusion:** the scaffold defaults an `allow` boolean to false. That is not yet a complete deny decision.

### `farm_operator_join.rego`

```rego
package kfm.generated.policy.sensitivity.agriculture.farm_operator_join

default allow := false
```

No join classification, transform path, review obligation, or reason code is present.

**Safe conclusion:** exact farm/operator joins appear fail-closed at the single boolean default, but complete behavior is not established.

### `redaction_profiles.yaml`

```yaml
status: PROPOSED
source_doc: docs/domains/agriculture/MISSING_OR_PLANNED_FILES.md
path: policy/domains/agriculture/redaction_profiles.yaml
notes:
  - Placeholder created from docs/domains markdown inventory.
```

**Safe conclusion:** no executable redaction profile or threshold is defined.

### Workflow posture

`.github/workflows/policy-test.yml` currently runs:

```text
echo TODO opa-test
echo TODO policy-fixture-coverage
```

`.github/workflows/domain-agriculture.yml` currently runs TODO echo jobs for validation, proof building, and publication dry run.

A green result from either workflow does not establish Agriculture policy-deny enforceability.

[Back to top](#top)

---

## Policy decision model

### Required separation

A policy test must preserve:

```text
policy input
  -> policy evaluation
  -> finite decision + reason codes + obligations
  -> runtime/API translation
  -> catalog/release/public-surface blocking or bounded allowance
  -> audit/correction/rollback linkage
```

These are distinct steps. A raw Rego boolean is not automatically a complete governed decision envelope.

### Outcome semantics

The following meanings are **PROPOSED** until an accepted policy-decision contract pins them:

| Outcome | Meaning | Required downstream behavior |
|---|---|---|
| `ALLOW` | Operation may proceed under the exact tested scope | Preserve scope, evidence, policy version, and release state |
| `DENY` | Operation is prohibited | Do not expose protected detail; block downstream use |
| `RESTRICT` | Operation may proceed only with obligations | Enforce aggregation, redaction, generalization, audience, delay, or review |
| `HOLD` | Decision requires missing review/support | Do not promote or render publicly |
| `ABSTAIN` | Policy cannot safely decide from available support | Preserve safe unresolved handles; do not infer allow |
| `ERROR` | Policy engine, input, bundle, or adapter failed | Fail closed and record bounded technical failure |

### Deny versus abstain

Tests must distinguish:

- **DENY** — sufficient context exists to prohibit the requested action.
- **ABSTAIN** — the decision cannot be resolved safely because evidence, rights, source role, or policy context is insufficient.
- **HOLD** — a known review, receipt, validation, or release prerequisite is pending.
- **RESTRICT** — a bounded transformed or audience-limited path may exist.
- **ERROR** — machinery failed; no policy conclusion should be invented.

A consumer must never convert `ABSTAIN`, `HOLD`, or `ERROR` into `ALLOW`.

### Proposed reason-code vocabulary

The codes below are test-design proposals, not accepted implementation facts:

| Proposed code | Intended condition |
|---|---|
| `AG_DENY_FIELD_LEVEL_EXACT` | Exact field geometry/detail requested for public exposure |
| `AG_DENY_FARM_OPERATOR_JOIN` | Farm/operator/private-party join requested without approved path |
| `AG_DENY_PRIVATE_PARCEL_JOIN` | Private parcel-adjacent join requested |
| `AG_DENY_PROPRIETARY_YIELD` | Proprietary/operator-supplied yield exposure |
| `AG_DENY_PESTICIDE_DETAIL` | Restricted pesticide/application detail |
| `AG_DENY_UNPUBLISHED` | Candidate is not under an accepted released state |
| `AG_DENY_QUARANTINE_MATERIAL` | QUARANTINE material requested for public use |
| `AG_DENY_SOURCE_ROLE_COLLAPSE` | Aggregate/modeled/candidate role upgraded to observed field truth |
| `AG_ABSTAIN_EVIDENCE_UNRESOLVED` | EvidenceRef/EvidenceBundle support unresolved |
| `AG_ABSTAIN_SOURCE_ROLE_UNKNOWN` | Source role cannot be resolved |
| `AG_HOLD_RIGHTS_REVIEW` | Rights/license posture requires review |
| `AG_HOLD_SENSITIVITY_REVIEW` | Sensitivity classification requires review |
| `AG_HOLD_AGGREGATION_RECEIPT_MISSING` | Required aggregation support absent |
| `AG_HOLD_REDACTION_RECEIPT_MISSING` | Required redaction support absent |
| `AG_HOLD_RELEASE_OR_ROLLBACK_MISSING` | Release or rollback support incomplete |
| `AG_RESTRICT_GENERALIZATION_REQUIRED` | Generalized representation required |
| `AG_RESTRICT_AUDIENCE_REQUIRED` | Restricted reviewer/audience path required |
| `AG_ERROR_POLICY_UNAVAILABLE` | Policy engine or bundle unavailable |
| `AG_ERROR_POLICY_INPUT_INVALID` | Input fails policy input contract |
| `AG_ERROR_OUTCOME_CONFLICT` | Multiple policy entrypoints yield incompatible outcomes |

Reason codes must not expose private identifiers, exact coordinates, proprietary values, secret thresholds, or agreement terms.

[Back to top](#top)

---

## Required test-case matrix

### A. Policy package and entrypoint tests

| Case | Expected assertion |
|---|---|
| Package loads under the accepted namespace | Exact query succeeds |
| Unknown package | `ERROR` / fail closed |
| Unknown entrypoint | `ERROR` / fail closed |
| Duplicate or conflicting package namespace | Test failure |
| Policy bundle digest differs from expected | Hold/error; no release-sensitive evaluation |
| Stub policy is used as production-complete | Test failure |
| `abstain_on_ambiguous` returns only deny boolean | Contract mismatch until normalized |
| Mixed `allow` and `deny` defaults are composed without adapter contract | Test failure |

### B. Exact exposure and private-join tests

| Case | Expected policy posture |
|---|---|
| Public exact field geometry | `DENY` |
| Public operator identity | `DENY` |
| Public farm/operator join | `DENY` |
| Public person/parcel/field join | `DENY` |
| Proprietary yield detail | `DENY` |
| Pesticide/application detail | `DENY` |
| NASS-confidential or restricted source detail | `DENY` |
| Quarantine-adjacent exact material | `DENY` or `HOLD`, never allow |
| Reviewed generalized geometry | `RESTRICT` or bounded `ALLOW`, per accepted policy |
| Reviewer-only transformed record | `RESTRICT`, audience obligation required |

### C. Aggregate and source-role tests

| Case | Expected policy posture |
|---|---|
| County-year aggregate with support and released posture | Positive control; bounded allow/restrict |
| Aggregate missing aggregation unit | `HOLD` / fail closed |
| Aggregate missing AggregationReceipt | `HOLD` or `DENY` for public use |
| Aggregate presented as field truth | `DENY` |
| Modeled vegetation/crop context presented as observed truth | `DENY` or `RESTRICT` |
| Field candidate presented as confirmed field record | `DENY` |
| Source role missing | `ABSTAIN` or fail closed |
| Source role contradictory across objects | `DENY` / conflict error |
| Cross-lane Soil/Hydrology context presented as Agriculture-owned truth | `DENY` or boundary failure |

### D. Evidence, rights, and sensitivity tests

| Case | Expected policy posture |
|---|---|
| EvidenceRef missing for claim-bearing output | `ABSTAIN` / `HOLD` |
| EvidenceRef does not resolve | `ABSTAIN` |
| EvidenceBundle incomplete | `ABSTAIN` / `HOLD` |
| Rights unknown | `HOLD` / `ABSTAIN` |
| Rights explicitly prohibit public use | `DENY` |
| Sensitivity tier missing | `HOLD` / fail closed |
| Most-restrictive cross-lane tier is denied | `DENY` |
| Required reviewer absent | `HOLD` |
| Required redaction support absent | `HOLD` / `DENY` |
| Support record exists but is stale/superseded | `HOLD` / `ABSTAIN` |

### E. Lifecycle and release tests

| Case | Expected policy posture |
|---|---|
| RAW requested for public route | `DENY` |
| WORK requested for public route | `DENY` |
| QUARANTINE requested for public route | `DENY` |
| PROCESSED candidate lacks catalog/proof closure | `HOLD` |
| Catalog record exists but no release | `DENY` / `HOLD` |
| Release reference missing | `HOLD` |
| Release withdrawn | `DENY` |
| Release superseded with no replacement | `HOLD` / `DENY` |
| Rollback requested | deny current candidate; serve prior known-good only through governed release |
| Rollback target missing for public-impacting release | `HOLD` |
| Policy decision predates material policy/version change | `HOLD` / re-evaluate |

### F. Policy-engine failure tests

| Case | Expected posture |
|---|---|
| OPA/runtime unavailable | `ERROR`, fail closed |
| Policy source malformed | `ERROR`, fail closed |
| Input schema invalid | `ERROR`, fail closed |
| Query returns undefined | `ABSTAIN` or `ERROR`, per accepted adapter contract |
| Query returns conflicting allow and deny | `ERROR` or most restrictive result |
| Unknown reason code | Test failure |
| Protected details appear in error | Test failure |
| Evaluation timeout | `ERROR`, fail closed |
| Partial bundle load | `ERROR`, fail closed |
| Policy cache stale | `HOLD` / re-evaluate |

### G. Public-surface tests

| Surface | Denied-case expectation |
|---|---|
| Catalog | No public-ready or released state inferred |
| Governed API | Finite deny/abstain/error envelope; no protected payload |
| Explorer UI | Denial/caveat state; no hidden exact data |
| Map/tiles | No restricted geometry or attributes emitted |
| Report/export | No restricted rows, coordinates, or joins |
| Search/index | Denied candidate omitted or access-restricted |
| Graph/triplet | No public edge that reveals protected relation |
| AI answer | `DENY`/`ABSTAIN`; no fluent reconstruction |
| Focus Mode | Bounded explanation and safe evidence state only |
| Download | No signed/public artifact generated |
| Cache | Denied payload not retained in public cache |
| Telemetry/logs | No protected values or secret policy detail |

### H. Correction and rollback tests

| Case | Expected assertion |
|---|---|
| Previously allowed output becomes denied | Public state withdrawn/corrected through release authority |
| Policy bug exposed protected data | Incident/correction path activated; prior safe state restored |
| Decision reason changes but outcome remains deny | Audit lineage preserved |
| Deny rule removed without review | Test failure / release hold |
| Policy version rolled back | Decision reproducibility and prior digest verified |
| Corrected aggregate replaces denied exact output | New release and evidence chain required |
| Cached/public derived artifacts remain after denial | Test failure |
| Search/vector/graph index still exposes denied relation | Test failure |

[Back to top](#top)

---

## Policy scaffold harmonization requirements

Before enforcement maturity can be claimed, maintainers must resolve:

1. **Canonical package namespace.** Choose and document one Agriculture namespace pattern.
2. **Canonical entrypoint.** Pin a stable query such as `data.kfm...decision`, not ad hoc boolean inversion.
3. **Unified result shape.** Return one finite decision object with outcome, reason codes, obligations, policy version, and safe audit refs.
4. **Default behavior.** Define how undefined input, missing package, and no matching rule behave.
5. **Rule precedence.** Pin the most-restrictive-row rule and conflict handling.
6. **Cross-package composition.** Specify how rights, sensitivity, domain, runtime, and release policy combine.
7. **Decision envelope.** Resolve generic versus Agriculture-prefixed schema/contract families.
8. **Reason-code registry.** Pin public-safe codes and internal-only diagnostics.
9. **Protected-output filter.** Guarantee deny/error paths cannot leak sensitive payloads.
10. **Test binding.** Map every implemented rule to positive, negative, ambiguous, error, correction, and rollback cases.
11. **CI binding.** Replace TODO echo jobs with actual OPA/fixture/runtime-adapter commands.
12. **Release binding.** Block promotion on substantive deny-test failure.

No README should be used to paper over these conflicts.

[Back to top](#top)

---

## No-network and fixture posture

The default policy-deny suite must be deterministic and offline.

### Fixture rules

Fixtures must be:

- synthetic;
- minimized;
- public-safe;
- stable;
- explicit about expected outcome;
- explicit about forbidden output fields;
- free of real operator/person/parcel identifiers;
- free of live credentials and endpoints;
- free of exact private geometries;
- bound to a policy package/entrypoint/version;
- clearly distinct from released records.

### Suggested fixture families

```text
fixtures/domains/agriculture/policy_deny/
├── README.md
├── field_level_exact/
├── farm_operator_join/
├── unpublished/
├── ambiguous_evidence/
├── rights_unknown/
├── aggregation_missing/
├── source_role_collapse/
├── policy_unavailable/
├── public_payload_leak/
├── correction/
└── rollback/
```

This tree is **PROPOSED**. The confirmed existing field-level fixture lane is:

```text
fixtures/domains/agriculture/field_level_attempt/
└── README.md
```

No direct payload inventory was established there.

### Network denial

Tests should fail if they detect unapproved:

- HTTP/S requests;
- DNS resolution;
- sockets;
- database calls;
- cloud storage calls;
- live OPA bundle downloads;
- live model-provider calls;
- external source fetches.

A future integration suite may exercise deployed services under a separate profile, but it must not replace the deterministic no-network suite.

[Back to top](#top)

---

## Public-surface denial contract

A deny test is incomplete unless it validates the presentation boundary.

### Minimum deny envelope

A public-safe denial response should expose only what the accepted runtime contract permits, likely including:

- finite outcome;
- safe reason code;
- bounded human-readable explanation;
- safe remediation or review path;
- policy/version reference where appropriate;
- correction or support reference where safe.

It should not expose:

- denied source payload;
- exact coordinates;
- person/operator/owner identity;
- parcel identifiers;
- proprietary values;
- pesticide/application detail;
- NASS-confidential content;
- private agreement terms;
- internal suppression thresholds when sensitive;
- raw policy input;
- stack traces;
- secret paths or credentials.

### Cache and derived-system controls

Tests should verify denial propagates to:

- public caches;
- tile caches;
- export caches;
- search indexes;
- vector indexes;
- graph projections;
- AI retrieval indexes;
- report snapshots;
- generated summaries;
- notification systems.

A denied canonical candidate that remains discoverable through a derived surface is a failed trust boundary.

[Back to top](#top)

---

## Policy runtime adapter contract

If a Python/TypeScript/runtime adapter translates Rego output, tests must pin:

| Adapter behavior | Required test |
|---|---|
| Boolean `allow` result | Map only under accepted contract; false does not invent reason |
| Set/object `deny` result | Preserve exact safe reasons; empty set is not automatic allow unless contract says so |
| Undefined query | `ABSTAIN` or `ERROR`, never implicit allow |
| Multiple package results | Apply accepted precedence/combination rule |
| Runtime exception | `ERROR`, fail closed |
| Timeout | `ERROR`, fail closed |
| Stale bundle | `HOLD` or `ERROR` |
| Unknown outcome | `ERROR` |
| Missing obligations | Fail when required by restrict/hold result |
| Protected fields in result | Redact and fail the test |
| Policy version/digest absent | Fail release-sensitive test |
| Audit reference absent | Fail consequential-decision test |

The adapter must not convert current scaffold defaults into a mature policy decision without explicit rules and a decision contract.

[Back to top](#top)

---

## Test implementation contract

Each executable case should identify:

```yaml
case_id: ag-policy-deny-001
policy_package: kfm.generated.policy.domains.agriculture.deny_field_level
entrypoint: data.kfm.generated.policy.domains.agriculture.deny_field_level.decision
policy_version: NEEDS_VERIFICATION
fixture: fixtures/domains/agriculture/policy_deny/field_level_exact/public-request.json
expected_outcome: DENY
expected_reason_codes:
  - AG_DENY_FIELD_LEVEL_EXACT
expected_obligations: []
blocked_surfaces:
  - catalog
  - release
  - api
  - ui
  - map
  - export
  - ai
forbidden_fields:
  - exact_geometry
  - operator_id
  - parcel_id
network: denied
```

This profile is **PROPOSED**.

### Test naming

Prefer names that state behavior:

```python
def test_public_field_geometry_is_denied_without_leaking_geometry():
    ...

def test_unresolved_evidence_abstains_instead_of_allowing():
    ...

def test_policy_runtime_failure_returns_error_and_blocks_release():
    ...
```

Avoid names that merely restate implementation details.

### Positive controls

A deny-only suite can pass while denying everything. Each material deny family needs a positive control showing a valid, reviewed, public-safe, aggregate/generalized/restricted case is not denied for the wrong reason.

Positive controls do not prove release approval. They prove only that the tested policy can distinguish bounded allowed and prohibited cases.

[Back to top](#top)

---

## Validation

### Documentation checks completed for this revision

- one H1 outside fenced blocks;
- balanced fenced blocks;
- no trailing whitespace;
- no tabs;
- required folder-README sections present and ordered;
- high-signal credential-pattern scan;
- one-file Git diff;
- remote blob readback.

### Repository inspection commands

```bash
find tests/domains/agriculture/policy_deny -maxdepth 5 -type f | sort
find policy/domains/agriculture policy/sensitivity/agriculture -maxdepth 5 -type f | sort
find fixtures/domains/agriculture/field_level_attempt -maxdepth 5 -type f | sort
```

### Policy syntax checks

When OPA is available:

```bash
opa fmt --fail policy/domains/agriculture/*.rego
opa fmt --fail policy/sensitivity/agriculture/*.rego
opa check policy/domains/agriculture policy/sensitivity/agriculture
```

These commands check formatting or parse/static validity. They do not prove policy semantics.

### Future OPA tests

After authored Rego tests exist:

```bash
opa test \
  policy/domains/agriculture \
  policy/sensitivity/agriculture \
  tests/domains/agriculture/policy_deny \
  -v
```

The exact layout is **PROPOSED** and must match accepted OPA test placement.

### Future pytest adapter tests

```bash
pytest -q tests/domains/agriculture/policy_deny
```

This command is meaningful only after collected tests exist.

### CI gate requirements

A substantive CI job should:

1. install a pinned OPA version;
2. verify policy formatting/static checks;
3. execute Rego unit tests;
4. execute runtime-adapter tests;
5. verify fixture coverage;
6. run public-surface leakage tests;
7. exercise negative, positive-control, error, correction, and rollback cases;
8. fail on skipped core cases;
9. publish a bounded test report;
10. block promotion on failure.

The existing TODO workflows do not satisfy these requirements.

### Required negative-state coverage

At minimum:

- missing input;
- malformed input;
- unknown package;
- unknown entrypoint;
- undefined query;
- policy parse failure;
- policy runtime failure;
- field-level exact exposure;
- farm/operator join;
- rights unknown;
- sensitivity unknown;
- evidence unresolved;
- receipt missing;
- release missing;
- rollback missing;
- source-role collapse;
- payload leakage;
- stale policy bundle;
- conflicting policy results.

[Back to top](#top)

---

## Review burden

### Ordinary README changes

Require:

- Agriculture test maintainer;
- docs maintainer.

### Test-case changes

Require:

- Agriculture test steward;
- policy steward;
- fixture steward;
- relevant domain owner.

### Policy or outcome-contract changes

Require:

- Agriculture domain steward;
- policy steward;
- sensitivity and rights stewards;
- contract/schema stewards;
- policy-runtime or validator owner;
- security reviewer;
- release steward when promotion/public state is affected.

### High-consequence changes

Changes involving exact fields, operator/person/parcel joins, private yield, pesticide detail, restricted source terms, hidden thresholds, public response shapes, or release/rollback behavior require elevated review and public-safe fixture inspection.

### Reviewer checklist

- [ ] Policy package and entrypoint are explicit.
- [ ] Current scaffold maturity is not overstated.
- [ ] Outcome semantics are finite and distinct.
- [ ] Most-restrictive policy composition is tested.
- [ ] Deny does not leak protected data.
- [ ] Missing/undefined/error cases fail closed.
- [ ] Positive controls prevent deny-everything false confidence.
- [ ] No live network or private data enters default tests.
- [ ] Source role, evidence, rights, sensitivity, receipts, and release remain separate.
- [ ] Public and derived surfaces remain blocked.
- [ ] Policy version/digest is recorded when consequential.
- [ ] Correction and rollback behavior is covered.
- [ ] CI executes real commands rather than TODO echoes.
- [ ] Documentation, policy, fixtures, and tests change together when behavior changes.

[Back to top](#top)

---

## Related folders

| Path | Relationship |
|---|---|
| `../README.md` | Agriculture domain test parent. |
| `../aggregate_only/README.md` | Aggregate-preservation and precision anti-collapse tests. |
| `../catalog_closure/README.md` | Catalog/evidence/release closure tests. |
| `../rollback_drill/README.md` | Rollback-readiness test lane. |
| `../../README.md` | Domain-test parent index, if present. |
| `../../../README.md` | Canonical tests root. |
| `../../../../policy/domains/agriculture/` | Agriculture policy implementation lane. |
| `../../../../policy/sensitivity/agriculture/` | Agriculture sensitivity policy. |
| `../../../../policy/rights/` | Rights policy authority. |
| `../../../../fixtures/domains/agriculture/` | Agriculture fixture root. |
| `../../../../fixtures/domains/agriculture/field_level_attempt/` | Confirmed fixture documentation for exact-exposure attempts. |
| `../../../../contracts/domains/agriculture/` | Agriculture object meaning. |
| `../../../../schemas/contracts/v1/domains/agriculture/` | Agriculture machine shapes and current decision-envelope drift. |
| `../../../../tools/validators/agriculture/` | Proposed Agriculture validator lane. |
| `../../../../packages/policy-runtime/` | Policy evaluation helper/runtime lane. |
| `../../../../data/quarantine/agriculture/` | Unsafe/unresolved Agriculture lifecycle material. |
| `../../../../data/receipts/agriculture/` | Agriculture process-memory receipts. |
| `../../../../data/proofs/agriculture/` | Agriculture evidence/proof support. |
| `../../../../release/` | Promotion, correction, withdrawal, and rollback authority. |
| `../../../../docs/domains/agriculture/POLICY.md` | Agriculture policy intent. |
| `../../../../docs/domains/agriculture/SENSITIVITY.md` | Sensitivity and public-release posture. |
| `../../../../docs/runbooks/agriculture/NO_NETWORK_TEST_RUNBOOK.md` | Offline Agriculture test posture. |
| `../../../../.github/workflows/policy-test.yml` | Current TODO policy workflow. |
| `../../../../.github/workflows/domain-agriculture.yml` | Current TODO Agriculture workflow. |

Relative paths are documentation links, not proof that every related lane is complete or canonical.

[Back to top](#top)

---

## ADRs

### Decisions required before implementation claims

| Decision | Status |
|---|---|
| Canonical Agriculture policy namespace | NEEDS VERIFICATION |
| Canonical package and entrypoint naming convention | NEEDS VERIFICATION |
| Unified finite decision object | NEEDS VERIFICATION |
| Generic versus Agriculture-prefixed decision envelope | CONFLICTED |
| Meaning of undefined/no-match policy result | NEEDS VERIFICATION |
| Composition of domain, sensitivity, rights, runtime, and release policy | NEEDS VERIFICATION |
| Most-restrictive conflict algorithm | NEEDS VERIFICATION |
| Public-safe reason-code registry | NEEDS VERIFICATION |
| Internal versus public diagnostic separation | NEEDS VERIFICATION |
| OPA test placement under `tests/` | NEEDS VERIFICATION |
| Fixture family path and schema | NEEDS VERIFICATION |
| Policy bundle manifest/version/digest contract | NEEDS VERIFICATION |
| Release-gate and branch-protection binding | NEEDS VERIFICATION |
| Correction and rollback semantics after policy changes | NEEDS VERIFICATION |

### ADR posture

No new ADR is created by this README.

Until decisions are accepted:

- preserve existing files;
- do not create parallel policy roots;
- do not silently rename packages;
- do not treat either decision-envelope schema as canonical;
- do not infer allow from an empty deny set;
- do not infer a governed deny decision from `allow == false` alone;
- do not claim CI enforcement from TODO workflows.

[Back to top](#top)

---

## Migration, correction, and rollback

### Smallest safe implementation sequence

1. Pin the canonical policy decision contract.
2. Resolve the decision-envelope schema conflict.
3. Pin policy package and entrypoint names.
4. Define the input contract.
5. Define finite outcomes, reasons, obligations, and public-safe output.
6. Convert scaffold defaults into explicit rules.
7. Add synthetic fixtures.
8. Add Rego unit tests.
9. Add policy-runtime adapter tests.
10. Add public-surface leakage tests.
11. Add correction and rollback tests.
12. Replace TODO CI jobs with pinned substantive commands.
13. Bind promotion to fail-closed test results.
14. Update parent READMEs and runbooks.

### Correction triggers

Correction is required if:

- a denied request exposed protected fields;
- an ambiguous case was treated as allowed;
- a policy default changed behavior without tests;
- package renaming caused the wrong query to execute;
- a decision-envelope change broke downstream handling;
- a source-role collapse reached a public surface;
- a previously released Agriculture product becomes policy-inadmissible;
- logs, caches, indexes, exports, or AI retrieval retained denied material.

### Test-document rollback

This README change is documentation-only.

Rollback options:

```bash
git revert <change-commit>
```

or restore prior blob:

```text
2921807aaf7c1881660d8fd7da4b35f9b6a613ba
```

### Behavioral rollback

When future policy behavior changes, rollback must identify:

- prior policy bundle digest;
- prior decision contract/schema;
- affected releases and public surfaces;
- cache/index invalidation;
- correction/withdrawal records;
- prior known-good public artifact;
- verification tests;
- accountable owner.

Policy rollback must not resurrect material newly known to be unsafe merely because an older policy allowed it.

[Back to top](#top)

---

## Open verification register

| Item | Status | Verification needed |
|---|---|---|
| Direct executable tests under this lane | UNKNOWN | Repository inventory and pytest/OPA collection |
| Agriculture Rego test files | UNKNOWN | Search and `opa test` |
| Actual field-level fixture payloads | UNKNOWN | Recursive fixture inventory |
| Policy bundle manifest | UNKNOWN | Bundle/config inspection |
| Canonical policy package namespace | CONFLICTED | ADR/contract decision |
| Stable query entrypoint | UNKNOWN | Policy-runtime contract |
| Unified decision outcome object | UNKNOWN | Contract/schema decision |
| Generic vs Agriculture decision envelope | CONFLICTED | Schema/contract migration |
| Default allow/deny/no-match semantics | CONFLICTED | Policy composition decision |
| `abstain_on_ambiguous` semantics | CONFLICTED | Implement abstain contract or rename |
| Rights policy integration | UNKNOWN | Policy and runtime tests |
| Sensitivity inheritance | UNKNOWN | Cross-policy tests |
| EvidenceRef/EvidenceBundle integration | UNKNOWN | Resolver and policy adapter tests |
| Redaction/aggregation profile implementation | NOT ESTABLISHED | Accepted profiles and fixtures |
| Reason-code vocabulary | PROPOSED | Contract and review |
| Protected-output filter | UNKNOWN | Runtime/public-surface tests |
| Agriculture validator implementation | UNKNOWN | Tool inventory |
| Policy runtime implementation | UNKNOWN | Package/runtime inspection |
| OPA version and pinning | UNKNOWN | CI/toolchain config |
| `policy-test` workflow enforcement | NOT IMPLEMENTED | Replace TODO steps |
| `domain-agriculture` enforcement | NOT IMPLEMENTED | Replace TODO steps |
| Branch protection/promotion binding | UNKNOWN | Repository settings/workflow evidence |
| Current policy test result | UNKNOWN | Execute substantive suite |
| Coverage and mutation testing | UNKNOWN | Coverage/mutation reports |
| Owner and CODEOWNERS | OWNER_TBD | Governance assignment |
| Correction propagation | UNKNOWN | Release/correction tests |
| Rollback automation | UNKNOWN | Drill and receipts |
| Public cache/index invalidation | UNKNOWN | Integration tests |
| Production use | UNKNOWN | Deployment/runtime evidence |

[Back to top](#top)

---

## Definition of done

This lane is not implementation-complete until:

- [ ] canonical policy namespace and entrypoint are accepted;
- [ ] policy input contract is accepted;
- [ ] one finite decision object is accepted;
- [ ] decision-envelope schema conflict is resolved;
- [ ] policy defaults and rule precedence are explicit;
- [ ] domain, sensitivity, rights, runtime, and release composition is tested;
- [ ] field-level exact exposure is substantively denied;
- [ ] farm/operator/private parcel joins are substantively denied;
- [ ] unpublished and quarantine material is blocked;
- [ ] ambiguity yields accepted abstain/hold behavior;
- [ ] rights and sensitivity uncertainty fails closed;
- [ ] source-role collapse is denied;
- [ ] aggregation/redaction obligations are enforced;
- [ ] fixture payloads are synthetic and public-safe;
- [ ] positive controls prevent deny-everything false confidence;
- [ ] deny/error responses do not leak protected data;
- [ ] OPA tests exist and are collected;
- [ ] runtime-adapter tests exist and are collected;
- [ ] public API/UI/map/report/export/AI boundaries are tested;
- [ ] correction, withdrawal, supersession, and rollback cases pass;
- [ ] workflows execute real pinned commands;
- [ ] core tests cannot be skipped silently;
- [ ] failures block promotion;
- [ ] owners and CODEOWNERS are assigned;
- [ ] current successful execution evidence is recorded;
- [ ] docs, policy, schemas, fixtures, tests, and runbooks agree.

Until then, the lane remains **draft / README-only / implementation unconfirmed**.

[Back to top](#top)

---

## Evidence basis

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Prior target README | CONFIRMED | Existing lane intent and previous blob | Did not inspect current policy implementation deeply |
| `tests/README.md` | CONFIRMED doctrine/documentation | Tests are enforceability proof | Does not prove this lane's implementation |
| Agriculture parent test README | CONFIRMED | Domain test routing | Child implementation remains unverified |
| Agriculture policy README | CONFIRMED | Policy-lane boundaries and fail-closed intent | States concrete policy/runtime enforcement needs verification |
| Agriculture `POLICY.md` | CONFIRMED policy intent / draft | Deny-by-default taxonomy and test obligations | Not executable policy |
| Agriculture `SENSITIVITY.md` | CONFIRMED doctrine / draft | Field/operator/public-exposure restrictions | Runtime enforcement not established |
| `deny_unpublished.rego` | CONFIRMED file / proposed stub | Package and default relation exist | No active deny rule |
| `abstain_on_ambiguous.rego` | CONFIRMED file / proposed stub | Package exists | Uses deny relation; no active abstain rule |
| `deny-field-level.rego` | CONFIRMED scaffold | Default allow is false | No reasoned decision rule |
| `farm_operator_join.rego` | CONFIRMED scaffold | Default allow is false | No join logic or obligations |
| `redaction_profiles.yaml` | CONFIRMED placeholder | Intended profile path | No profile semantics |
| Field-level fixture README | CONFIRMED documentation | Intended negative-fixture lane | No payload inventory confirmed |
| Decision-envelope schemas | CONFIRMED scaffolds / conflicted | Two candidate machine-shape paths | Both permissive and incomplete |
| Decision validator search | CONFIRMED bounded search | Declared validator did not surface | Search is not exhaustive filesystem proof |
| Agriculture validator README | CONFIRMED documentation | Intended validator scope | No executable established |
| `policy-test.yml` | CONFIRMED workflow stub | Workflow name and TODO jobs | No OPA test execution |
| `domain-agriculture.yml` | CONFIRMED workflow stub | Agriculture workflow exists | No substantive Agriculture validation |
| Directory Rules | CONFIRMED doctrine | `tests/` and `policy/` responsibility separation | Does not prove implementation completeness |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-16 |
| Review state | Draft repository-grounded README replacement |
| Evidence base | `main@01026cd58b1e687c4f8fa3363229b9857613102b` |
| Current maturity | README-only test lane; policy scaffolds; TODO-only CI |
| Next smallest safe change | Resolve policy decision/entrypoint contract, then add one synthetic field-level deny case with an explicit safe reason and no-leak assertion |
| Rollback target | Prior blob `2921807aaf7c1881660d8fd7da4b35f9b6a613ba` |

[Back to top](#top)
