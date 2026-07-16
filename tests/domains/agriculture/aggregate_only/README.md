<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-agriculture-aggregate-only-readme
title: tests/domains/agriculture/aggregate_only/ — Aggregate-Only Agriculture Test Boundary
type: readme; directory-readme; domain-test-sublane; aggregate-only-enforceability-boundary
version: v0.2
status: draft; repository-grounded; README-only; sibling-placeholder-test-confirmed; implementation-unconfirmed; ci-stub; non-authoritative
owners: OWNER_TBD — Agriculture test steward · Agriculture domain steward · Policy steward · Sensitivity and rights steward · Fixture steward · Contract and schema steward · Validator steward · Release steward · Docs steward
created: NEEDS VERIFICATION — empty placeholder was expanded before v0.2
updated: 2026-07-16
supersedes: v0.1 aggregate-only Agriculture test guide
policy_label: "public-review; tests; agriculture; aggregate-only; no-network; synthetic-fixtures; field-level-deny; source-role-preservation; evidence-gated; policy-gated; receipt-aware; release-gated; no-live-private-data; no-public-authority"
current_path: tests/domains/agriculture/aggregate_only/README.md
truth_posture: >
  CONFIRMED target v0.1 README; canonical tests root; Agriculture parent test README;
  bounded repository search returning this README for the aggregate_only child lane; sibling
  tests/domains/agriculture/test_nass_aggregate_only.py containing only a PROPOSED placeholder
  docstring; Agriculture sensitivity doctrine requiring aggregate outputs not be presented as
  field/operator truth and field-level NASS claims to deny; no-network Agriculture runbook;
  NASS QuickStats fixture README with no payload inventory confirmed; aggregation-threshold
  policy README with no accepted numeric thresholds or runtime enforcement; draft
  AggregationReceipt semantic contract; permissive scaffold aggregation_receipt schema with
  empty properties and a hyphen/underscore contract-path conflict; Agriculture validator README
  with no confirmed executable; and domain-agriculture workflow containing TODO-only jobs /
  PROPOSED aggregate-only test contract, case matrix, finite assertion outcomes, fixture
  admission requirements, no-network guards, public-surface anti-overclaim checks, placement
  reconciliation, validation commands, definition of done, and rollback /
  CONFLICTED aggregate_only child-lane documentation versus the current sibling placeholder
  module at tests/domains/agriculture/test_nass_aggregate_only.py; hyphenated
  contracts/domains/agriculture/aggregation-receipt.md versus the schema metadata's underscore
  contract path; domain-specific AggregationReceipt home versus broader receipt-family placement /
  UNKNOWN executable aggregate-only assertions, collected pytest cases, fixture payloads,
  accepted threshold profiles, policy evaluator wiring, Agriculture validator implementation,
  EvidenceRef resolution, receipt validation, public API/UI integration tests, CI enforcement,
  current test results, coverage, owners, and release-gate adoption /
  NEEDS VERIFICATION lane retention versus flat-module migration, canonical receipt contract and
  schema alignment, accepted aggregation thresholds, reason-code vocabulary, fixture identity,
  network-denial enforcement, CODEOWNERS, correction/rollback coverage, and fail-closed workflow
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 377caf85cb87486f19e31f06f3a932963c21bb0a
  prior_blob: b82e359eb9478a38a06fc71214972591ffd2f9df
  tests_root_blob: 5614de99433bca29d6a03d665fb4e00ec23eb5fb
  agriculture_tests_parent_blob: 35ebf2a578f2a39b4f4766cc4146aafde8124e67
  sibling_placeholder_test_blob: 97939b939122f029f35ecf12c81f5989df00ae63
  agriculture_sensitivity_blob: 9d25f63d471af78899d8db2ad39a3921c4f11fac
  no_network_runbook_blob: 15a94c9f7a92f2f258a85200c7d49f01293fd10b
  nass_fixture_readme_blob: a9fb9ff71eaecbee3e4b73a907538daaeb2a5616
  aggregation_threshold_policy_blob: acc7d7b4edcd52bb01303bda117f2969be4121f1
  aggregation_receipt_contract_blob: 7a658c579011dad0636025f502419372294d9086
  aggregation_receipt_schema_blob: 16c55157c07d3115bfb540b2064e0401bc71b564
  agriculture_validator_readme_blob: ba9009bdecb6e007423122c32c53fffc3559976d
  agriculture_workflow_blob: a9f5f212ef61d72fdc209d9f8b173bbf87fb1803
related:
  - ../README.md
  - ../test_nass_aggregate_only.py
  - ../../README.md
  - ../../../README.md
  - ../../../../fixtures/domains/agriculture/nass_quickstats/README.md
  - ../../../../fixtures/domains/agriculture/no_network/nass/README.md
  - ../../../../contracts/domains/agriculture/aggregation-receipt.md
  - ../../../../schemas/contracts/v1/domains/agriculture/aggregation_receipt.schema.json
  - ../../../../policy/domains/agriculture/aggregation_thresholds/README.md
  - ../../../../tools/validators/agriculture/README.md
  - ../../../../docs/domains/agriculture/SENSITIVITY.md
  - ../../../../docs/domains/agriculture/FILE_SYSTEM_PLAN.md
  - ../../../../docs/runbooks/agriculture/NO_NETWORK_TEST_RUNBOOK.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../.github/workflows/domain-agriculture.yml
tags: [kfm, tests, agriculture, aggregate-only, nass, quickstats, county-year, crd-year, source-role, anti-collapse, no-network, synthetic-fixtures, aggregation-receipt, deny, abstain, rollback]
notes:
  - "This revision changes only tests/domains/agriculture/aggregate_only/README.md."
  - "The aggregate_only child lane remains README-only at the bounded search; no executable test is created."
  - "The sibling test_nass_aggregate_only.py file remains a docstring-only placeholder and is not treated as collected test coverage."
  - "No contract, schema, policy, fixture, validator, workflow, receipt, data, release record, or public-client behavior is modified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/domains/agriculture/aggregate_only/` — Aggregate-Only Agriculture Test Boundary

> **One-line purpose.** Define the enforceability boundary for proving that Agriculture outputs remain explicitly aggregate, source-role faithful, public-safe only after evidence and policy gates, and incapable of being presented as field-, operator-, parcel-, or private-party truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: aggregate only" src="https://img.shields.io/badge/lane-aggregate__only-success">
  <img alt="Maturity: README only" src="https://img.shields.io/badge/maturity-README__only-lightgrey">
  <img alt="Network: denied by default" src="https://img.shields.io/badge/network-denied__by__default-critical">
  <img alt="Field-level NASS: deny" src="https://img.shields.io/badge/field__level__NASS-DENY-red">
</p>

> [!IMPORTANT]
> **Aggregate-only is a testable boundary, not an automatic release permission.** A county-year or crop-reporting-district summary is not public-safe merely because it is aggregated. Tests must also exercise source role, geography and time scope, support and suppression posture, evidence, rights, policy, receipt, review, release, correction, and rollback conditions.

> [!CAUTION]
> **Current implementation is not established.** The `aggregate_only/` directory is README-only in the bounded repository search. The sibling file [`test_nass_aggregate_only.py`](../test_nass_aggregate_only.py) contains only a placeholder docstring and defines no collected pytest test.

> [!WARNING]
> **Tests must never launder precision.** Aggregate NASS or other Agriculture statistics must not be reinterpreted as a specific field, operator, farm, parcel, private party, or exact-location observation. Missing support must produce a failing, denied, held, abstaining, or error case—not a fluent fallback.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Does not](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed)

---

## Purpose

`tests/domains/agriculture/aggregate_only/` is the Agriculture test sublane for **aggregate-preservation and precision anti-collapse proof**.

A complete aggregate-only test family should answer:

1. Is the aggregation unit explicit and supported?
2. Is the temporal bucket explicit and source-aligned?
3. Does the output preserve the source's aggregate role?
4. Are geography, measure, support count, suppression, and derivation posture bounded?
5. Does the candidate resolve the required evidence and rights context?
6. Is an `AggregationReceipt`, redaction receipt, or equivalent governed support object required and present?
7. Does policy allow, restrict, hold, abstain, or deny the requested audience and use?
8. Can a public API, UI, tile, report, export, or AI response imply more precision than the source supports?
9. Does correction, supersession, withdrawal, and rollback posture remain visible?
10. Does the default suite remain deterministic, synthetic, and no-network?

The lane focuses on aggregate Agriculture products such as:

- county-year crop or acreage statistics;
- crop-reporting-district-year summaries;
- state-year or regional summaries;
- accepted grid, HUC, or generalized-region products where policy explicitly permits them;
- derived aggregate indicators that retain modeled or contextual source roles;
- aggregate public-surface responses that preserve caveats and finite outcomes.

This lane does **not** decide that a product is safe, true, current, rights-cleared, or releasable. It proves declared rules only when backed by real tests, fixtures, contracts, schemas, policy, validators, and current execution evidence.

[Back to top](#top)

---

## Authority level

**Canonical test responsibility / non-authoritative Agriculture sublane.**

`tests/` owns enforceability proof. Agriculture is a domain segment under that root. This child README refines aggregate-only test expectations; it does not define Agriculture meaning, machine shape, policy, thresholds, evidence, receipts, release, or public behavior.

| Concern | Authority home | This lane's role |
|---|---|---|
| Enforceability proof | `tests/` | Owns authored tests and assertions. |
| Agriculture test organization | `tests/domains/agriculture/` | Owns domain test grouping and cross-lane test coordination. |
| Aggregate-only test family | This lane or an accepted flat-module convention | Owns test cases only after placement is resolved. |
| Agriculture object meaning | `contracts/domains/agriculture/` | Tests the contract; does not redefine it. |
| Agriculture machine shape | `schemas/contracts/v1/domains/agriculture/` | Tests schema behavior; does not author schemas. |
| Aggregation threshold and disclosure policy | `policy/domains/agriculture/` | Tests decisions and obligations; does not invent thresholds. |
| Agriculture validator implementation | `tools/validators/agriculture/` or accepted validator lane | Tests validators; does not implement them here. |
| Synthetic fixture families | `fixtures/domains/agriculture/` | Consumes fixtures; does not duplicate fixture authority. |
| Evidence, receipts, proofs, lifecycle data | Governed `data/` roots | Uses bounded references or synthetic examples only. |
| Release, correction, withdrawal, rollback | `release/` | Tests readiness and denial; cannot approve transitions. |
| Governed API/UI rendering | Accepted `apps/`, API, UI, and map roots | Tests bounded output behavior; cannot expose a route. |
| CI workflow definition | `.github/workflows/` | May be a caller; workflow presence is not proof of substantive execution. |

### Anti-collapse rules

This lane must not collapse:

- aggregate data into field-level observation;
- modeled or remotely sensed context into observed truth;
- a schema-valid object into policy permission;
- a receipt into evidence or proof;
- test success into release approval;
- fixture data into source truth;
- a public-safe example into a blanket audience decision;
- a README into executable coverage;
- pytest collection into test correctness;
- a workflow badge or green TODO job into fail-closed enforcement.

[Back to top](#top)

---

## Status

### Confirmed repository state

At `main@377caf85cb87486f19e31f06f3a932963c21bb0a`:

```text
tests/domains/agriculture/
├── README.md
├── aggregate_only/
│   └── README.md                         # this lane; README-only in bounded search
└── test_nass_aggregate_only.py           # sibling placeholder docstring only
```

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| Target README | Present, prior v0.1 | Documentation exists. |
| Direct executable under `aggregate_only/` | Not established by bounded search | Do not claim lane-local tests. |
| `test_nass_aggregate_only.py` | Eight-line docstring placeholder | No pytest function, class, assertion, fixture, or marker is defined. |
| Parent Agriculture test README | Present | Lists aggregate-only as a planned child test family. |
| NASS QuickStats fixture lane | README present; payload inventory unverified | Fixture intent exists; test data does not. |
| No-network Agriculture runbook | Present, draft/proposed | Defines deterministic no-network expectations; not execution proof. |
| Sensitivity doctrine | Present, draft | Requires aggregate outputs not be field/operator truth and field-level NASS claims to deny. |
| Aggregation threshold policy | README present; no numeric thresholds accepted | Policy classes exist as proposals; enforcement is unproved. |
| AggregationReceipt contract | Draft semantic contract present | Meaning and recommended fields exist; canonical path/home remains conflicted. |
| AggregationReceipt schema | Present, `PROPOSED`, empty properties, `additionalProperties: true` | Schema cannot enforce the recommended receipt fields. |
| Agriculture validator lane | README only in inspected evidence | No executable aggregate validator is confirmed. |
| `domain-agriculture` workflow | TODO-only echo jobs | Workflow success would not prove Agriculture tests ran. |
| Current test run, coverage, pass rate | Unknown | No result is claimed. |

### Placement drift

The repository currently expresses two possible test layouts:

```text
tests/domains/agriculture/aggregate_only/test_*.py
```

and:

```text
tests/domains/agriculture/test_nass_aggregate_only.py
```

The first is represented by this child-lane README. The second is represented by the current sibling placeholder module.

This documentation update does not move, rename, or delete either path. Maintainers should choose one reviewed convention:

1. **Child-lane implementation:** place aggregate-only test modules under `aggregate_only/` and keep the parent root for shared Agriculture tests.
2. **Flat-module implementation:** keep `test_nass_aggregate_only.py` at the Agriculture test root and treat `aggregate_only/README.md` as an index/contract or retire it through a migration note.
3. **Hybrid only with justification:** shared aggregate tests at the parent plus source-specific child tests, with explicit ownership and no duplicate cases.

Until resolved, do not create parallel test suites with diverging policy or expected outcomes.

### Contract and schema drift

The confirmed contract path is hyphenated:

```text
contracts/domains/agriculture/aggregation-receipt.md
```

The schema metadata points to an underscore path:

```text
contracts/domains/agriculture/aggregation_receipt.md
```

The schema itself is an empty permissive scaffold. Aggregate-only tests must not pretend this drift is resolved or that schema validation proves receipt completeness.

[Back to top](#top)

---

## What belongs here

When implementation is admitted, this lane may contain:

- this README and aggregate-only test indexes;
- deterministic pytest modules for aggregate-preservation behavior;
- positive county-year, CRD-year, state-year, HUC, grid, or generalized-region cases approved by policy;
- negative field-, operator-, farm-, parcel-, and exact-location interpretation cases;
- source-role anti-collapse assertions;
- aggregation-unit and temporal-bucket assertions;
- small-cell, re-identification, support-count, and source-diversity denial cases;
- evidence, rights, sensitivity, policy, receipt, review, release, correction, and rollback integration assertions;
- public API/UI/map/report/AI anti-overclaim assertions;
- no-network and synthetic-fixture guards;
- test-local parametrization and helper code that is not reusable production or validator logic;
- test metadata documenting the contract, schema, policy profile, fixture, and reason code exercised.

### Minimum case metadata

Each implemented case should identify:

| Field | Purpose |
|---|---|
| `case_id` | Stable test-case identity. |
| `source_family` | NASS QuickStats, CDL, derived indicator, or other reviewed source. |
| `source_role` | `aggregate`, `modeled`, `context`, or another accepted role. |
| `aggregation_unit` | County, CRD, state, HUC, grid, region, or accepted class. |
| `time_bucket` | Crop year, calendar year, season, month, or accepted interval. |
| `measure` | Acreage, yield, crop count, index, or other bounded measure. |
| `audience` | Public, reviewer, restricted, or denied. |
| `policy_profile` | Threshold/redaction/generalization profile under test. |
| `expected_outcome` | Pass, deny, restrict, hold, abstain, or error posture. |
| `reason_code` | Stable expected reason where applicable. |
| `fixture_refs` | Synthetic fixture paths and hashes where practical. |
| `contract_schema_refs` | Exact contract and schema versions under test. |
| `receipt_expectation` | Required, optional, forbidden, or unresolved. |
| `release_context` | Candidate, released, superseded, withdrawn, rollback, or not applicable. |

[Back to top](#top)

---

## What does not belong here

| Do not place here | Correct home or handling |
|---|---|
| Agriculture implementation code | `packages/domains/agriculture/`, pipelines, connectors, or owning implementation root |
| Canonical contracts or schemas | `contracts/`, `schemas/` |
| Policy rules or numeric aggregation thresholds | `policy/` plus accepted ADR/review |
| Agriculture validator implementation | `tools/validators/agriculture/` or accepted validator root |
| General fixture payloads, source dumps, or golden libraries | `fixtures/domains/agriculture/` |
| Live USDA NASS, CDL, SSURGO, Mesonet, HLS, SMAP, or other source calls | Connector/integration test lane outside the default no-network suite |
| Real operator, farm, parcel, field, pesticide, insurance, proprietary yield, or restricted records | Governed private/quarantine systems; never public test fixtures |
| Exact sensitive coordinates or identifying joins | Synthetic generalized fixtures only |
| EvidenceBundle, receipt, proof, catalog, lifecycle, release, correction, or rollback instances | Governed `data/` and `release/` roots |
| Public API/UI/map/tile/report implementation | Accepted application and presentation roots |
| Generated model text treated as expected truth | Use authored expected outcomes and evidence-backed assertions |
| Test-generated files committed as governed artifacts | Route through accepted temporary/report or governed artifact paths after review |
| Duplicate flat and child-lane suites with different rules | Reconcile placement first |
| `|| true`, swallowed exceptions, unconditional skips, or assertions that cannot fail | Remove or document a temporary, reviewed reason with expiry |

### Forbidden fixture content

Default aggregate-only tests must reject or prevent:

- source credentials, tokens, cookies, or private endpoints;
- live network requests;
- raw private or licensed source payloads;
- real farm/operator identifiers;
- exact private parcel-to-operator joins;
- exact sensitive coordinates;
- unredacted stack traces or logs containing protected data;
- fixture values that could plausibly be mistaken for released evidence without an obvious synthetic marker.

[Back to top](#top)

---

## Inputs

Permitted test inputs are bounded, synthetic, version-pinned references.

| Input family | Required posture |
|---|---|
| Aggregate source fixture | Synthetic, compact, deterministic, obvious mock marker, explicit source role. |
| Agriculture contract | Exact path/version; path conflicts remain visible. |
| Agriculture schema | Exact `$id` and status; permissive scaffolds must not be treated as enforcement. |
| Policy profile | Accepted profile or explicit unresolved/deny case; no invented thresholds. |
| Aggregation unit | Explicit geography class and identifier. |
| Temporal bucket | Explicit, source-aligned period. |
| Support metrics | Count, area, source diversity, suppression marker, or explicit unknown state. |
| Evidence context | Synthetic `EvidenceRef`/`EvidenceBundle` status or expected missing-support case. |
| Rights and sensitivity context | Explicit tier, license/rights state, private-join posture, most-restrictive-row handling. |
| Receipt context | Synthetic `AggregationReceipt` or expected missing/invalid case. |
| Release context | Candidate/released/superseded/withdrawn/rollback state or not applicable. |
| Public-surface request | Synthetic API/UI/map/report/AI request context with requested precision and audience. |
| Correction context | Prior output, correction/supersession reference, cache invalidation, and rollback target where material. |

### Input invariants

Tests should fail or deny when:

- the aggregation geography is absent or incompatible with the source;
- the temporal bucket is absent, stale, or falsely precise;
- the source role is missing or rewritten;
- aggregate support is unknown where policy requires it;
- a small cell or single-source aggregate risks re-identification;
- evidence, rights, sensitivity, policy, receipt, or release context is missing;
- an aggregate is joined to operator, parcel, living-person, or restricted-source detail;
- the requested audience or precision exceeds the permitted representation;
- correction or rollback state makes the candidate stale or withdrawn;
- a fixture loader attempts network access or reads undeclared local data.

[Back to top](#top)

---

## Outputs

The primary outputs of this lane are **test assertions and finite test results**.

Permitted outputs include:

- pytest pass/fail/error/skip results with reviewed skip reasons;
- deterministic assertion messages;
- temporary test reports or coverage data in accepted ignored/CI artifact locations;
- expected decision/envelope comparisons;
- bounded diffs between actual and expected public-safe representations;
- test evidence that a forbidden interpretation was denied;
- test evidence that missing support caused abstention, hold, denial, or error;
- review notes linking a failure to contract, schema, policy, fixture, validator, correction, or rollback work.

This lane must not emit or approve:

- canonical Agriculture observations;
- source registry entries;
- EvidenceBundles, governed receipts, proofs, catalogs, or release manifests as authoritative instances;
- public layers, tiles, APIs, reports, exports, or generated answers;
- policy approvals or sensitivity determinations;
- lifecycle promotion, release, correction, withdrawal, or rollback decisions.

### Assertion outcome vocabulary

Separate the **test runner result** from the **domain decision under test**.

| Layer | Suggested values | Meaning |
|---|---|---|
| Test runner | `PASS`, `FAIL`, `ERROR`, reviewed `SKIP` | Whether the test executed and its assertion held. |
| Domain/runtime decision | `ALLOW`/`ANSWER`, `RESTRICT`, `HOLD`, `ABSTAIN`, `DENY`, `ERROR` | The governed outcome expected from the system under test. |
| Candidate lifecycle | `candidate`, `released`, `superseded`, `withdrawn`, `rollback_required` | Release/correction state supplied to the test. |

A runner `PASS` means the expected decision occurred. It does not mean the underlying data is true or releasable outside the fixture case.

[Back to top](#top)

---

## Validation

### Current collection boundary

The sibling placeholder currently contains no pytest tests. Therefore:

- syntax success would prove only that the placeholder parses;
- `pytest --collect-only` may collect zero cases;
- a zero-test result is not aggregate-only coverage;
- the `domain-agriculture` workflow's TODO echoes are not test execution;
- README presence and schema presence are not validation.

### Required test families

#### 1. Positive aggregate preservation

At minimum, implemented positive cases should cover:

| Case | Expected behavior |
|---|---|
| County-year NASS aggregate with explicit source role and period | Accepted only within declared aggregate scope. |
| CRD-year or state-year aggregate with adequate support | Accepted only when policy profile, evidence, receipt, and release context permit. |
| Modeled aggregate indicator | Preserves `modeled` or `context` role; never rewritten as observed field truth. |
| Generalized grid/HUC/region output | Requires an accepted generalization/aggregation profile and obligations. |
| Public response from released aggregate | Carries caveats, source role, aggregation unit, time, evidence/citation pointers, and correction state. |

#### 2. Source-role anti-collapse

Tests should prove that:

- QuickStats aggregate cells never become field observations;
- CDL or remote-sensing classification does not become operator-confirmed crop truth;
- modeled stress or suitability indicators remain modeled/contextual;
- Soil, Hydrology, Atmosphere, and People/Land authority is cited rather than redefined;
- joining an aggregate to exact private detail adopts the most restrictive posture.

#### 3. Precision and disclosure denial

Required negative cases include:

| Case | Expected domain posture |
|---|---|
| Field-level NASS claim | `DENY` |
| Operator- or farm-resolved claim | `DENY` |
| Private parcel join | `DENY` or restricted review; never public |
| Exact sensitive geometry | `DENY`, generalize, or hold according to accepted policy |
| Missing aggregation unit | `HOLD`, `ABSTAIN`, or validation failure |
| Missing time bucket | Validation failure or hold |
| Missing source role | Validation failure |
| Small-cell or single-source re-identification risk | Suppress, restrict, hold, or deny |
| Unsupported precision requested by API/UI/AI | Deny or return a coarser permitted representation |
| Aggregate re-described as a specific place's truth | Test failure and deny |

#### 4. Evidence, receipt, and release separation

Tests must distinguish:

```text
receipt != proof != catalog != release != publication
```

Coverage should include:

- missing `EvidenceRef` or unresolved `EvidenceBundle`;
- missing or invalid aggregation receipt;
- receipt present but no evidence support;
- receipt present but policy denied;
- schema-valid receipt missing semantic requirements because the current schema is permissive;
- catalog entry present but release absent;
- release candidate present but rollback target absent;
- superseded, corrected, withdrawn, or stale aggregate;
- public response attempted before governed release.

#### 5. Threshold-policy behavior

Until numeric thresholds are accepted:

- tests must not invent authoritative counts, areas, source-diversity minima, or time windows;
- unresolved threshold profiles should produce hold, abstain, restrict, or deny behavior;
- exact field/operator/parcel exposure remains deny-default;
- threshold internals must not leak sensitive information;
- future numeric profiles require policy ownership, fixtures, schema/contract references, and negative boundary cases.

#### 6. No-network and fixture safety

Default tests should:

- block socket, DNS, HTTP, SDK, browser, and live model-provider access;
- use synthetic identifiers and non-routable examples;
- load fixtures only from declared repository paths;
- avoid environment-dependent timestamps, locale, unordered traversal, and random IDs unless controlled;
- fail when a fixture lacks an obvious mock marker;
- scan test output for credentials and protected values;
- avoid recording private chain-of-thought or raw sensitive prompts.

#### 7. Public-surface anti-overclaim

API, UI, map, report, export, and AI integration tests should verify:

- the aggregation unit and period are visible;
- source role and derivation posture are visible;
- uncertainty, suppression, caveats, and obligations are preserved;
- exact field/operator/parcel inference is not exposed;
- evidence and citation pointers resolve or the result abstains;
- stale, corrected, superseded, withdrawn, or rollback-required state is visible;
- the UI does not imply point precision from county/region aggregates;
- generated language cannot upgrade an aggregate into per-place truth.

#### 8. Correction and rollback

Coverage should include:

- replacement of an aggregate after source correction;
- supersession of an aggregation receipt;
- cache and derived-product invalidation;
- withdrawal from public surfaces;
- restoration of a prior known-good released aggregate;
- receipt/proof/release lineage preserved across rollback;
- denied use of stale or withdrawn aggregate outputs.

### Suggested commands

These commands describe the intended inspection and execution surface. They were not run by this documentation change.

```bash
find tests/domains/agriculture/aggregate_only -maxdepth 5 -type f | sort
find tests/domains/agriculture -maxdepth 2 -type f -name '*aggregate*' | sort
python -m py_compile tests/domains/agriculture/test_nass_aggregate_only.py
pytest --collect-only -q tests/domains/agriculture/test_nass_aggregate_only.py
pytest --collect-only -q tests/domains/agriculture/aggregate_only
pytest -q tests/domains/agriculture/test_nass_aggregate_only.py
pytest -q tests/domains/agriculture/aggregate_only
```

When real tests exist, the accepted CI command should be fail-closed and should not use `|| true`.

### Minimum implementation sequence

1. Resolve flat-module versus child-lane placement.
2. Pin the aggregate-only contract, source roles, and decision vocabulary.
3. Reconcile the AggregationReceipt contract filename and schema metadata.
4. Replace the permissive schema scaffold with reviewed required fields or explicitly select another receipt profile.
5. Accept threshold-policy classes and any numeric profiles through policy review.
6. Add synthetic valid, invalid, denied, abstain, correction, and rollback fixtures.
7. Implement deterministic validator or system-under-test behavior.
8. Replace the sibling docstring placeholder with collected tests or retire it through migration.
9. Add no-network enforcement and credential/sensitive-data guards.
10. Add public-surface anti-overclaim tests.
11. Wire a substantive Agriculture workflow that actually invokes the suite.
12. Record current CI results, correction path, and rollback target.

### Definition of done

This lane is not implementation-complete until all applicable items are satisfied:

- [ ] Placement is accepted and duplicate suite risk is removed.
- [ ] At least one positive aggregate case is collected and passes.
- [ ] Field-level NASS, operator, parcel, and unsupported-precision cases deny or fail closed.
- [ ] Source-role preservation is asserted.
- [ ] Aggregation unit, period, measure, and support context are asserted.
- [ ] Evidence and citation failure produces abstention or denial.
- [ ] Receipt, proof, catalog, release, and publication separation is asserted.
- [ ] AggregationReceipt contract/schema drift is resolved or explicitly profiled.
- [ ] Accepted policy profiles and reason codes are fixture-tested.
- [ ] Fixtures are synthetic, public-safe, deterministic, and no-network.
- [ ] No live source, live model, or secret is required.
- [ ] Public API/UI/map/report/AI anti-overclaim behavior is covered.
- [ ] Correction, supersession, withdrawal, and rollback are covered.
- [ ] Dedicated test and validator implementation is confirmed.
- [ ] CI invokes the real suite and fails on negative regressions.
- [ ] Current run evidence is recorded without treating a green result as release approval.
- [ ] Owners and CODEOWNERS are accepted.
- [ ] Documentation and rollback instructions are current.

[Back to top](#top)

---

## Review burden

### Required reviewers by change

| Change | Minimum review |
|---|---|
| README wording or links only | Agriculture test steward + docs steward |
| Positive/negative aggregate test case | Agriculture test steward + domain steward |
| Threshold or disclosure expectation | Agriculture policy + sensitivity/rights steward |
| AggregationReceipt assertion | Contract/schema + receipt/evidence steward |
| Fixture addition | Fixture steward + sensitivity/privacy review |
| NASS source-role behavior | Agriculture source steward + domain steward |
| Public API/UI/map/report/AI assertion | Governed API/UI steward + evidence/policy reviewer |
| Correction/rollback case | Release/correction/rollback steward |
| Test placement move or lane retirement | Tests root owner + Agriculture owner + migration/docs review |
| CI gate change | CI steward + Agriculture test steward; release review if promotion-blocking |

### Review checklist

- [ ] Claim status is labeled `CONFIRMED`, `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION`.
- [ ] Test placement matches the accepted convention.
- [ ] Test inputs are synthetic, bounded, and no-network.
- [ ] Aggregate source role is never upgraded.
- [ ] Geography and time scope are explicit.
- [ ] Support, suppression, and threshold posture are explicit.
- [ ] Policy is consumed, not invented in the test.
- [ ] Receipt is not treated as proof or release.
- [ ] Missing evidence produces abstain/deny/failure.
- [ ] Field/operator/parcel and exact-sensitive cases fail closed.
- [ ] Public output cannot imply unsupported precision.
- [ ] Correction and rollback behavior is covered where material.
- [ ] No secrets or protected context appear in fixtures, logs, snapshots, or PR text.
- [ ] Test names and assertion messages identify the invariant.
- [ ] Skips and xfails have owners, reasons, and expiry.
- [ ] CI claims are backed by current workflow evidence.

[Back to top](#top)

---

## Related folders

| Path | Relationship |
|---|---|
| [`../README.md`](../README.md) | Agriculture domain test parent and child-lane index. |
| [`../test_nass_aggregate_only.py`](../test_nass_aggregate_only.py) | Current sibling placeholder; no executable test established. |
| [`../../README.md`](../../README.md) | Domain test grouping under the canonical tests root. |
| [`../../../README.md`](../../../README.md) | Canonical tests-root authority and trust-spine requirements. |
| [`../../../../fixtures/domains/agriculture/nass_quickstats/README.md`](../../../../fixtures/domains/agriculture/nass_quickstats/README.md) | QuickStats aggregate fixture intent; payload inventory unverified. |
| [`../../../../fixtures/domains/agriculture/no_network/nass/README.md`](../../../../fixtures/domains/agriculture/no_network/nass/README.md) | No-network NASS fixture lane. |
| [`../../../../contracts/domains/agriculture/aggregation-receipt.md`](../../../../contracts/domains/agriculture/aggregation-receipt.md) | Draft AggregationReceipt semantic contract. |
| [`../../../../schemas/contracts/v1/domains/agriculture/aggregation_receipt.schema.json`](../../../../schemas/contracts/v1/domains/agriculture/aggregation_receipt.schema.json) | Permissive scaffold schema with path conflict. |
| [`../../../../policy/domains/agriculture/aggregation_thresholds/README.md`](../../../../policy/domains/agriculture/aggregation_thresholds/README.md) | Proposed threshold classes; no accepted numeric thresholds. |
| [`../../../../tools/validators/agriculture/README.md`](../../../../tools/validators/agriculture/README.md) | Proposed Agriculture validator lane; no executable confirmed. |
| [`../../../../docs/domains/agriculture/SENSITIVITY.md`](../../../../docs/domains/agriculture/SENSITIVITY.md) | Aggregate/public-release and field-level deny doctrine. |
| [`../../../../docs/domains/agriculture/FILE_SYSTEM_PLAN.md`](../../../../docs/domains/agriculture/FILE_SYSTEM_PLAN.md) | Agriculture responsibility-root placement plan. |
| [`../../../../docs/runbooks/agriculture/NO_NETWORK_TEST_RUNBOOK.md`](../../../../docs/runbooks/agriculture/NO_NETWORK_TEST_RUNBOOK.md) | Deterministic synthetic no-network test design. |
| [`../../../../.github/workflows/domain-agriculture.yml`](../../../../.github/workflows/domain-agriculture.yml) | TODO-only Agriculture workflow scaffold. |
| `../../../../data/receipts/` | Governed receipt instances; tests use synthetic references only. |
| `../../../../data/proofs/` | Evidence/proof authority; separate from receipts and tests. |
| `../../../../release/` | Release, correction, withdrawal, and rollback authority. |

### Dependency direction

```text
contracts + schemas + policy + fixtures + implementation
                         ↓
       aggregate-only tests and validators
                         ↓
       CI / review / promotion prerequisites
```

Tests consume authority surfaces. They do not redefine or replace them.

[Back to top](#top)

---

## ADRs

The following decisions remain open or require verification:

| Decision | Current status | Required outcome |
|---|---|---|
| Aggregate-only test placement | NEEDS VERIFICATION | Select child-lane, flat-module, or justified hybrid convention. |
| AggregationReceipt contract filename | CONFLICTED | Reconcile hyphenated contract path with underscore schema metadata. |
| AggregationReceipt canonical family home | NEEDS VERIFICATION | Decide domain contract/receipt placement without creating parallel authority. |
| AggregationReceipt schema maturity | PROPOSED scaffold | Define required fields, close unknown properties as appropriate, add fixtures and validator tests. |
| Aggregation threshold profiles | NEEDS VERIFICATION | Accept policy-owned classes, numeric values where justified, obligations, and reason codes. |
| Agriculture validator entry point | NEEDS VERIFICATION | Confirm durable implementation path and command contract. |
| No-network enforcement | NEEDS VERIFICATION | Select fixture/network guard mechanism and negative tests. |
| Public-surface precision profile | NEEDS VERIFICATION | Pin API/UI/map/report/AI response obligations for aggregate products. |
| Domain workflow gate | TODO scaffold | Replace echoes with real fail-closed test invocations before claiming CI enforcement. |
| Correction and rollback profile | NEEDS VERIFICATION | Define stale/corrected/superseded/withdrawn behavior and cache invalidation proof. |
| Ownership | OWNER_TBD | Pin test, policy, fixture, validator, release, and docs owners in CODEOWNERS. |

Do not resolve these questions by adding a second schema, policy, receipt, fixture, validator, or test authority home. Use an ADR, migration note, or accepted maintainer decision when the choice affects compatibility or responsibility boundaries.

### Rollback triggers

Rollback or correct this README if it:

- claims collected tests where only placeholders exist;
- presents TODO workflow success as Agriculture validation;
- treats the permissive schema as receipt completeness;
- invents numeric aggregation thresholds;
- treats aggregation as automatic public permission;
- treats a receipt as evidence, proof, or release;
- hides the flat-module/child-lane placement conflict;
- weakens field/operator/parcel denial;
- permits live network or private fixtures in the default suite;
- implies release, correction, or rollback authority.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-16 |
| Evidence base | `main@377caf85cb87486f19e31f06f3a932963c21bb0a` |
| Target prior blob | `b82e359eb9478a38a06fc71214972591ffd2f9df` |
| Review mode | Repository-grounded documentation revision; one-file scope |
| Current lane maturity | README-only |
| Current sibling test maturity | Docstring-only placeholder |
| Implementation effect | None — documentation only |
| Rollback | Revert the update commit or restore the prior blob; no test, fixture, contract, schema, policy, validator, workflow, data, receipt, release, or public behavior changes |

### Maintenance triggers

Re-review when:

- an executable test is added under this lane or at the Agriculture test root;
- the flat versus child-lane placement is resolved;
- NASS or other aggregate fixtures gain payloads;
- the AggregationReceipt contract or schema changes;
- aggregation thresholds or reason codes are accepted;
- Agriculture validator code is implemented;
- no-network enforcement is added;
- EvidenceRef resolution or receipt validation becomes executable;
- public API/UI/map/report/AI aggregate behavior changes;
- the Agriculture workflow invokes real tests;
- correction, withdrawal, or rollback behavior changes;
- Directory Rules, test-root doctrine, or an accepted ADR changes placement.

### v0.1 → v0.2 change summary

- Grounds the README against current repository evidence.
- Corrects the implementation posture from aspirational tests to README-only plus a sibling docstring placeholder.
- Records the flat-module versus child-lane placement conflict.
- Records the AggregationReceipt contract/schema filename conflict and permissive schema scaffold.
- Records that threshold policy has no accepted numeric values, validator implementation is unconfirmed, and CI is TODO-only.
- Adds bounded inputs, outputs, source-role anti-collapse, no-network, public-surface, correction, rollback, validation, review, and definition-of-done requirements.
- Preserves the central Agriculture invariant: aggregate outputs must never become field-, operator-, parcel-, or private-party truth.

<p align="right"><a href="#top">Back to top</a></p>
