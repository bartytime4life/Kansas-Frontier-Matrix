<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/common/spec-hash/invalid/readme
title: fixtures/contracts/v1/common/spec_hash/invalid/ — SpecHash Negative Fixture Contract
type: readme; directory-readme; invalid-contract-fixture-lane; common-contract; json-schema-negative-case; non-authoritative
version: v0.2
status: draft; repository-grounded; one-invalid-fixture-confirmed; generic-pytest-harness-confirmed; dedicated-validator-placeholder; partial-negative-coverage
owners: OWNER_TBD — Schema steward · Common-contract steward · Fixture steward · Validator steward · Test/QA steward · Docs steward
created: NEEDS VERIFICATION — file predates the 2026-06-30 v0.1 expansion
updated: 2026-07-19
supersedes: v0.1.0
policy_label: public-review; fixtures; contracts; common; spec-hash; invalid; synthetic-only; non-authoritative
owning_root: fixtures/
current_path: fixtures/contracts/v1/common/spec_hash/invalid/README.md
truth_posture: >
  CONFIRMED target v0.1 README and prior blob; invalid_1.json content; expected-error
  sidecar content; sibling valid fixture lane; parent fixture-family guidance; SpecHash
  semantic contract; Draft 2020-12 schema shape, required value field, lowercase SHA-256
  pattern, closed object shape, and x-kfm fixture/validator metadata; generic pytest
  collection and expected-error matching; dedicated validator placeholder behavior /
  PROPOSED broader negative matrix for missing value, wrong root type, wrong value type,
  missing prefix, wrong digest length, uppercase hex, non-hex characters, extra properties,
  and stable reason-token coverage / UNKNOWN exhaustive fixture inventory outside the
  inspected direct lane, dynamic consumers, branch-protection significance, current
  repository-wide pass state, production producers, canonicalization behavior, and release
  use / NEEDS VERIFICATION accepted owners, CODEOWNERS, dedicated validator implementation,
  complete negative coverage, exact collected case count, CI requirement, and downstream
  correction obligations
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 2783739bba744f560772388a9969ed3107d08930
  prior_blob: bf9fa6f13c0b93e7f64d70885e64a60275e69500
  invalid_fixture_blob: 0967ef424bce6791893e9a57bb952f80fd536e93
  expected_error_blob: cb128ae0e4af3f627f25520854312fef678d50e5
  schema_blob: 80b496b01b8de8c0e8ba67bf020977e6b1f3c652
  validator_blob: de69c6c7001082af29827a4b287a80b7c6a05af3
  test_harness_blob: b04342cc034d7f1cc554e155fdd02d6e972976e6
related:
  - ../README.md
  - ../valid/README.md
  - ../valid/valid_1.json
  - invalid_1.json
  - invalid_1.expected_error.txt
  - ../../../../../../schemas/contracts/v1/common/spec_hash.schema.json
  - ../../../../../../contracts/common/spec_hash.md
  - ../../../../../../tools/validators/validate_spec_hash.py
  - ../../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, common, spec-hash, invalid-fixtures, json-schema, expected-error, negative-tests, fail-closed, non-authoritative]
notes:
  - "v0.2 replaces the v0.1 historical blank-file narrative with current repository evidence."
  - "The direct lane contains one confirmed invalid JSON fixture and one expected-error sidecar."
  - "The generic pytest harness is executable; the schema-declared dedicated validator remains a NotImplementedError placeholder."
  - "This README changes documentation only. It creates no new fixture case and claims no broader negative coverage."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# SpecHash Negative Fixture Contract

`fixtures/contracts/v1/common/spec_hash/invalid/`

> **Purpose.** Hold deterministic JSON instances that must be rejected by the `spec_hash` schema, together with narrowly scoped expected-error text, without turning fixtures or test output into schema, contract, policy, proof, release, or production authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Fixture kind: invalid" src="https://img.shields.io/badge/fixture-invalid-critical">
  <img alt="Coverage: one case" src="https://img.shields.io/badge/coverage-one__case-orange">
  <img alt="Dedicated validator: placeholder" src="https://img.shields.io/badge/dedicated__validator-placeholder-red">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture__only-success">
</p>

> [!IMPORTANT]
> Every `invalid_*.json` file in this directory is expected to fail the paired JSON Schema. A failure caused by a missing file, parser crash, unresolved schema, dependency error, or placeholder validator is **not** proof that the intended negative condition was enforced.

> [!WARNING]
> A rejected fixture proves only the tested machine-shape condition. It does not prove semantic correctness, canonicalization, evidence closure, policy admissibility, artifact integrity, release readiness, or publication safety.

**Quick links:** [Status](#status-and-evidence-boundary) · [Purpose](#purpose-and-scope) · [Placement](#placement-and-authority) · [Inventory](#confirmed-inventory) · [Schema](#schema-and-contract-basis) · [Harness](#executable-test-harness) · [Failure contract](#negative-fixture-failure-contract) · [Coverage](#coverage-boundary) · [Authoring](#authoring-contract) · [Validation](#validation) · [Correction](#correction-and-rollback) · [Open items](#open-verification-register) · [Evidence](#evidence-ledger)

---

## Status and evidence boundary

| Surface | Status at the pinned snapshot | Safe conclusion |
|---|---|---|
| This README | **CONFIRMED existing v0.1** | Revised in place; prior blob is pinned above. |
| `invalid_1.json` | **CONFIRMED** | Contains an empty JSON object. |
| `invalid_1.expected_error.txt` | **CONFIRMED** | Requires the missing-`value` message. |
| Paired schema | **CONFIRMED file / `PROPOSED` metadata status** | Requires `value`, enforces a lowercase SHA-256 pattern, and rejects additional properties. |
| Generic pytest harness | **CONFIRMED executable code** | Discovers this fixture family and checks invalid polarity plus expected-error text. |
| Dedicated `validate_spec_hash.py` | **CONFIRMED placeholder** | Raises `NotImplementedError`; it is not usable validator enforcement. |
| Current test result for this exact repository head | **NEEDS VERIFICATION** | File inspection is not an execution log. |
| Complete negative-case coverage | **NOT ESTABLISHED** | One missing-required-field case is confirmed. |
| Production or release use | **UNKNOWN** | Fixtures do not establish downstream consumers or authority. |

### Truth labels

- **CONFIRMED** — verified from repository files or local execution against the pinned content.
- **PROPOSED** — recommended behavior or coverage not yet implemented.
- **UNKNOWN** — not resolved from current evidence.
- **NEEDS VERIFICATION** — checkable but not sufficiently proven for reliance.

[Back to top](#top)

---

## Purpose and scope

This lane answers a narrow question:

> Does the current `spec_hash` schema reject a deliberately invalid instance for the intended reason?

### In scope

- intentionally invalid JSON instances;
- one failure concern per fixture when practical;
- expected-error sidecars used by the repository schema test harness;
- deterministic, synthetic, reviewable cases;
- schema drift detection;
- clear separation between fixture failure and infrastructure failure.

### Out of scope

- valid examples, which belong in [`../valid/`](../valid/README.md);
- schema or semantic-contract definitions;
- canonicalization algorithms;
- hash generation;
- validator implementation;
- evidence, proof, policy, release, lifecycle, or publication records;
- production digests or real artifact identifiers.

[Back to top](#top)

---

## Placement and authority

### Directory Rules basis

`fixtures/` is an enforceability-input root adjacent to `tests/`. This path is further partitioned by contract version, family, object name, and polarity:

```text
fixtures/
└── contracts/
    └── v1/
        └── common/
            └── spec_hash/
                ├── valid/
                └── invalid/   # this lane
```

The path is correct for reusable contract-fixture inputs. Responsibility remains separated:

| Responsibility | Owning surface |
|---|---|
| Semantic meaning | [`contracts/common/spec_hash.md`](../../../../../../contracts/common/spec_hash.md) |
| Machine shape | [`schemas/contracts/v1/common/spec_hash.schema.json`](../../../../../../schemas/contracts/v1/common/spec_hash.schema.json) |
| Invalid fixture inputs | This directory |
| Positive fixture inputs | [`../valid/`](../valid/README.md) |
| Generic executable test | [`tests/schemas/test_common_contracts.py`](../../../../../../tests/schemas/test_common_contracts.py) |
| Dedicated validator implementation | [`tools/validators/validate_spec_hash.py`](../../../../../../tools/validators/validate_spec_hash.py) |
| Policy, proofs, receipts, and release | Their separate authority roots |

This README coordinates those references but owns none of their authority.

[Back to top](#top)

---

## Confirmed inventory

| Path | Content | Expected outcome |
|---|---|---|
| [`invalid_1.json`](invalid_1.json) | `{}` | Schema rejection because required property `value` is absent. |
| [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt) | `'value' is a required property` | The generic harness must find this normalized text in the combined schema errors. |

No additional direct invalid fixture is claimed by this README.

### Positive comparison

[`../valid/valid_1.json`](../valid/valid_1.json) provides the sibling positive shape. The valid and invalid lanes are complementary inputs, not competing authority.

[Back to top](#top)

---

## Schema and contract basis

The schema requires this shape:

```json
{
  "value": "sha256:<64 lowercase hexadecimal characters>"
}
```

| Constraint | Current requirement |
|---|---|
| Root type | `object` |
| Required property | `value` |
| `value` type | `string` |
| Pattern | `^sha256:[a-f0-9]{64}$` |
| Additional properties | rejected |
| Schema metadata status | `PROPOSED` |
| Declared fixture root | `fixtures/contracts/v1/common/spec_hash/` |
| Declared validator | `tools/validators/validate_spec_hash.py` |

The semantic contract further limits interpretation: a shape-valid `spec_hash` identifies a hashed specification representation. It does not prove correctness, authority, admissibility, freshness, evidence closure, or release state.

[Back to top](#top)

---

## Executable test harness

`tests/schemas/test_common_contracts.py`:

1. includes `common` in its hard-coded family list;
2. discovers immediate `*.schema.json` files under the common schema family;
3. maps each schema name to `fixtures/contracts/v1/common/<name>/`;
4. validates `invalid/invalid_*.json`;
5. requires at least one JSON Schema error;
6. reads the matching `.expected_error.txt` when present;
7. normalizes and matches expected text against combined validator messages.

For this fixture, the expected text is specific enough to distinguish the intended missing-field rejection from an unrelated schema failure.

### Dedicated validator boundary

`tools/validators/validate_spec_hash.py` currently raises:

```python
NotImplementedError("Greenfield placeholder")
```

Therefore:

```text
generic pytest harness = executable evidence path
dedicated validator CLI = placeholder, not enforcement
```

A placeholder exception must never be counted as successful rejection of an invalid fixture.

[Back to top](#top)

---

## Negative fixture failure contract

A case is acceptable only when all applicable conditions hold:

| Condition | Required posture |
|---|---|
| Fixture parses as JSON | Yes |
| Matching schema loads and resolves | Yes |
| Validation returns one or more schema errors | Yes |
| Expected-error sidecar exists when stable cause matching is needed | Preferred |
| Expected text matches the intended cause | Yes |
| Failure is caused by missing file, crash, import error, or placeholder validator | Reject the test result |
| Fixture contains real production hash or restricted material | Reject the fixture |

### Finite outcomes

| Outcome | Meaning |
|---|---|
| `EXPECTED_REJECTION` | Fixture parsed, schema loaded, and the intended invalid condition was detected. |
| `UNEXPECTED_PASS` | Fixture produced no schema errors; fail the test. |
| `WRONG_REJECTION` | Fixture failed, but expected cause text did not match; fail the test. |
| `FIXTURE_ERROR` | JSON or sidecar is malformed or missing; fail the test. |
| `HARNESS_ERROR` | Schema, dependency, import, or runner failed; do not report expected rejection. |

These labels are documentation vocabulary unless separately standardized by a contract.

[Back to top](#top)

---

## Coverage boundary

The current lane proves one negative dimension:

- missing required `value`.

It does **not** currently prove rejection of:

- non-object roots;
- non-string `value`;
- missing `sha256:` prefix;
- uppercase hexadecimal;
- non-hexadecimal characters;
- digest shorter or longer than 64 characters;
- leading or trailing whitespace;
- additional properties;
- alternative hash algorithms;
- canonicalization mismatch.

These are sensible **PROPOSED** future cases, not current repository facts. Each added fixture should isolate one primary failure where practical.

[Back to top](#top)

---

## Authoring contract

Before adding or changing an invalid fixture:

- use `invalid_<n>.json`;
- keep the payload synthetic and minimal;
- target one primary schema invariant;
- ensure the JSON parses before schema validation;
- add `invalid_<n>.expected_error.txt` when cause stability matters;
- use expected text emitted by the actual Draft 2020-12 validator path;
- avoid broad patterns that could match unrelated errors;
- add or update the positive sibling only when needed to preserve polarity;
- update this inventory and the parent README when coverage changes;
- do not place production hashes, secrets, source payloads, receipts, proofs, or release records here;
- do not edit schema or contract meaning inside fixture prose.

### Naming and pairing

```text
invalid_<n>.json
invalid_<n>.expected_error.txt
```

The sidecar is optional in the generic harness, but omission reduces cause-specific assurance.

[Back to top](#top)

---

## Validation

### Repository-native check

The executable schema lane is:

```bash
python -m pytest -q tests/schemas/test_common_contracts.py
```

A narrower parametrized selector may be used only after collection names are verified.

### Documentation checks

For README-only changes, verify:

- one H1;
- a closed KFM Meta Block;
- balanced code fences;
- valid internal anchors;
- repository-relative links resolve;
- no tabs or trailing whitespace;
- final newline;
- no secret, production hash, or restricted payload;
- generated receipt present when required.

### Acceptance criteria

A change is review-ready when:

1. every listed fixture exists;
2. each JSON fixture parses;
3. each expected-error sidecar is non-empty;
4. the schema rejects every invalid fixture;
5. expected text matches the intended failure;
6. the dedicated validator is not represented as implemented while it remains a placeholder;
7. coverage gaps remain visible;
8. no authority or lifecycle boundary is collapsed.

[Back to top](#top)

---

## Correction and rollback

If a fixture begins passing unexpectedly:

1. determine whether the schema changed intentionally;
2. check whether the fixture no longer expresses the intended invalid condition;
3. update schema, contract, valid fixtures, invalid fixtures, expected errors, tests, and docs together when semantics changed;
4. do not weaken expected-error matching merely to restore a green test;
5. record compatibility and downstream correction obligations where the changed schema is consumed.

For this README revision, rollback is mechanical: restore prior blob `bf9fa6f13c0b93e7f64d70885e64a60275e69500` and remove the paired generated receipt. No fixture or schema rollback is required because this change modifies documentation only.

[Back to top](#top)

---

## Open verification register

- **NEEDS VERIFICATION** — current pass result of `test_common_contracts.py` at the PR head.
- **NEEDS VERIFICATION** — accepted owners and CODEOWNERS enforcement.
- **NEEDS VERIFICATION** — complete invalid-case matrix and required coverage threshold.
- **NEEDS VERIFICATION** — implementation and admission of the dedicated `spec_hash` validator.
- **NEEDS VERIFICATION** — branch-protection status of schema-validation checks.
- **UNKNOWN** — production consumers and canonicalization rules used by producers.
- **UNKNOWN** — whether ignored, generated, branch-local, or external fixture cases exist.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Limit |
|---|---|---|---|
| Prior README blob `bf9fa6f…` | **CONFIRMED** | Existing v0.1 scope and historical claims. | Prior-session history is not current implementation evidence. |
| [`invalid_1.json`](invalid_1.json) | **CONFIRMED** | Empty-object negative case. | Covers one invariant only. |
| [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt) | **CONFIRMED** | Expected missing-field cause. | Coupled to validator wording. |
| [`../valid/README.md`](../valid/README.md) | **CONFIRMED documentation** | Positive-lane boundary and sibling case. | Does not prove execution. |
| [`../README.md`](../README.md) | **CONFIRMED documentation** | Fixture-family placement and schema linkage. | Contains older maturity wording. |
| [`spec_hash.schema.json`](../../../../../../schemas/contracts/v1/common/spec_hash.schema.json) | **CONFIRMED schema file** | Shape, required field, pattern, closed object, metadata. | `x-kfm.status` remains `PROPOSED`. |
| [`spec_hash.md`](../../../../../../contracts/common/spec_hash.md) | **CONFIRMED semantic contract** | Meaning and anti-overclaim boundary. | Canonicalization and producers remain unverified. |
| [`validate_spec_hash.py`](../../../../../../tools/validators/validate_spec_hash.py) | **CONFIRMED placeholder** | Dedicated path exists. | Raises `NotImplementedError`. |
| [`test_common_contracts.py`](../../../../../../tests/schemas/test_common_contracts.py) | **CONFIRMED executable code** | Discovery, invalid polarity, and sidecar matching. | Current run result is separate evidence. |

[Back to top](#top)
