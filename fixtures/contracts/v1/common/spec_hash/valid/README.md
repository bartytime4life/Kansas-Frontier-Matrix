<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/common/spec-hash/valid/readme
title: fixtures/contracts/v1/common/spec_hash/valid/ — SpecHash Positive Fixture Contract
type: readme; directory-readme; valid-contract-fixture-lane; common-contract; json-schema-positive-case; non-authoritative
version: v0.2
status: draft; repository-grounded; one-valid-fixture-confirmed; generic-pytest-harness-confirmed; dedicated-validator-placeholder; partial-positive-coverage
owners: OWNER_TBD — Schema steward · Common-contract steward · Fixture steward · Validator steward · Test/QA steward · Docs steward
created: NEEDS VERIFICATION — file predates the 2026-06-30 v0.1 expansion
updated: 2026-07-19
supersedes: v0.1.0
policy_label: public-review; fixtures; contracts; common; spec-hash; valid; synthetic-only; non-authoritative
owning_root: fixtures/
current_path: fixtures/contracts/v1/common/spec_hash/valid/README.md
truth_posture: >
  CONFIRMED target v0.1 README and prior blob; valid_1.json content; sibling invalid
  lane; SpecHash contract and Draft 2020-12 schema; generic pytest positive-polarity
  assertion; dedicated validator placeholder / PROPOSED distinct future positive boundary
  cases only when they add coverage / UNKNOWN production consumers, canonicalization,
  branch-protection significance, and repository-wide pass state / NEEDS VERIFICATION
  owners, CODEOWNERS, dedicated validator implementation, exact collected case count,
  complete positive coverage, and CI requirement
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: f31613299e6b0c1fc3ac37f2bbf08bc56af49e42
  prior_blob: 928c0758c1f7450f9afd3787a4d272cd6cb12b2d
  valid_fixture_blob: 5bad69059af065fd6b0488f4ece8dce98890bce3
  invalid_readme_blob: ca4e78c0115e6843b8123e6d626cd41221c6c43e
  schema_blob: 80b496b01b8de8c0e8ba67bf020977e6b1f3c652
  contract_blob: 0c2c1161ddb565d4f9f17ef81080b27b8d951937
  validator_blob: de69c6c7001082af29827a4b287a80b7c6a05af3
  test_harness_blob: b04342cc034d7f1cc554e155fdd02d6e972976e6
related:
  - ../README.md
  - valid_1.json
  - ../invalid/README.md
  - ../invalid/invalid_1.json
  - ../invalid/invalid_1.expected_error.txt
  - ../../../../../../schemas/contracts/v1/common/spec_hash.schema.json
  - ../../../../../../contracts/common/spec_hash.md
  - ../../../../../../tools/validators/validate_spec_hash.py
  - ../../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, common, spec-hash, valid-fixtures, json-schema, positive-tests, deterministic, non-authoritative]
notes:
  - "v0.2 replaces the v0.1 historical blank-file narrative with current repository evidence."
  - "The direct lane contains one confirmed valid JSON fixture."
  - "The generic pytest harness is executable; the dedicated validator remains a NotImplementedError placeholder."
  - "This documentation-only revision creates no fixture, schema, contract, validator, test, policy, release, or runtime behavior."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# SpecHash Positive Fixture Contract

`fixtures/contracts/v1/common/spec_hash/valid/`

> **Purpose.** Hold deterministic JSON instances that must be accepted by the `spec_hash` schema, without turning fixtures, valid strings, or test output into semantic truth, canonicalization proof, artifact integrity, policy approval, release authority, or production data.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Fixture kind: valid" src="https://img.shields.io/badge/fixture-valid-2ea44f">
  <img alt="Coverage: one case" src="https://img.shields.io/badge/coverage-one__case-orange">
  <img alt="Validator: placeholder" src="https://img.shields.io/badge/validator-placeholder-red">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture__only-success">
</p>

> [!IMPORTANT]
> Every `valid_*.json` file here must parse, be collected by the intended harness, and produce zero errors from the paired schema. Empty collection, skipped discovery, missing assertions, or a crashing placeholder validator is not positive validation.

> [!WARNING]
> Schema-valid shape does not prove which bytes were hashed, canonicalization consistency, producer identity, correctness, freshness, evidence closure, policy allowance, release state, or publication safety.

**Quick links:** [Status](#status-and-evidence-boundary) · [Purpose](#purpose-and-scope) · [Placement](#placement-and-authority) · [Inventory](#confirmed-inventory) · [Schema](#schema-and-contract-basis) · [Harness](#executable-test-harness) · [Acceptance](#positive-fixture-acceptance-contract) · [Coverage](#coverage-boundary) · [Authoring](#authoring-contract) · [Validation](#validation) · [Rollback](#correction-and-rollback) · [Open](#open-verification-register) · [Evidence](#evidence-ledger)

---

## Status and evidence boundary

| Surface | Status | Safe conclusion |
|---|---|---|
| This README | **CONFIRMED existing v0.1** | Revised in place; prior blob is pinned. |
| `valid_1.json` | **CONFIRMED** | One minimal object matches the current pattern. |
| Sibling invalid lane | **CONFIRMED v0.2 documentation** | One missing-required-field case is documented and cause-matched. |
| Paired schema | **CONFIRMED file / `PROPOSED` metadata** | Requires `value`, enforces lowercase SHA-256 form, and closes the object. |
| Semantic contract | **CONFIRMED draft contract** | Defines a representation reference, not proof or release authority. |
| Generic pytest harness | **CONFIRMED executable code** | Discovers this family and asserts zero errors for valid fixtures. |
| Dedicated validator | **CONFIRMED placeholder** | Raises `NotImplementedError`; not usable enforcement. |
| Current PR-head test result | **NEEDS VERIFICATION** | File evidence is not a complete execution log. |
| Complete positive coverage | **NOT ESTABLISHED** | One positive case is confirmed. |

### Truth labels

- **CONFIRMED** — verified from repository evidence or bounded direct execution.
- **PROPOSED** — recommended behavior or coverage not yet implemented.
- **UNKNOWN** — unresolved from inspected evidence.
- **NEEDS VERIFICATION** — checkable but not sufficiently proven.

[Back to top](#top)

---

## Purpose and scope

This lane answers one question:

> Does the current `spec_hash` schema accept a deliberately valid instance with the required closed-object shape?

In scope:

- deterministic, synthetic valid JSON instances;
- positive-polarity schema checks;
- schema drift detection;
- comparison with the sibling invalid lane;
- clear separation between shape acceptance and operational authority.

Out of scope:

- invalid cases, which belong in [`../invalid/`](../invalid/README.md);
- schema, contract, canonicalization, hash generation, or validator implementation;
- evidence, policy, proof, receipt, release, lifecycle, or publication records;
- production digests and real artifact identifiers.

[Back to top](#top)

---

## Placement and authority

### Directory Rules basis

```text
fixtures/
└── contracts/
    └── v1/
        └── common/
            └── spec_hash/
                ├── valid/     # this lane
                └── invalid/
```

| Responsibility | Owning surface |
|---|---|
| Semantic meaning | [`contracts/common/spec_hash.md`](../../../../../../contracts/common/spec_hash.md) |
| Machine shape | [`spec_hash.schema.json`](../../../../../../schemas/contracts/v1/common/spec_hash.schema.json) |
| Positive inputs | This directory |
| Negative inputs | [`../invalid/`](../invalid/README.md) |
| Executable generic test | [`test_common_contracts.py`](../../../../../../tests/schemas/test_common_contracts.py) |
| Dedicated validator | [`validate_spec_hash.py`](../../../../../../tools/validators/validate_spec_hash.py) |

Fixtures are enforceability inputs, not authority. This README references the owning surfaces and does not redefine them.

[Back to top](#top)

---

## Confirmed inventory

| Path | Content | Expected outcome |
|---|---|---|
| [`valid_1.json`](valid_1.json) | `value` is `sha256:` followed by 64 lowercase `a` characters. | Zero JSON Schema errors. |

No additional direct valid fixture is claimed.

[`../invalid/invalid_1.json`](../invalid/invalid_1.json) is the complementary negative case: `{}` must fail because `value` is required.

[Back to top](#top)

---

## Schema and contract basis

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

The contract says a valid value identifies a hashed specification representation. It does not establish what was hashed, how it was canonicalized, who produced it, or whether it is authoritative, current, admissible, evidence-backed, or released.

[Back to top](#top)

---

## Executable test harness

`tests/schemas/test_common_contracts.py`:

1. includes `common` in its family list;
2. discovers immediate common-family schemas;
3. maps `spec_hash` to this fixture family;
4. loads every `valid/valid_*.json`;
5. validates through the repository-local Draft 2020-12 resolver;
6. asserts that the error list is empty.

The dedicated validator currently raises:

```python
NotImplementedError("Greenfield placeholder")
```

Therefore:

```text
generic pytest harness = executable evidence path
dedicated validator CLI = placeholder, not enforcement
```

[Back to top](#top)

---

## Positive fixture acceptance contract

| Condition | Required posture |
|---|---|
| JSON parses | Yes |
| Paired schema loads | Yes |
| Validation returns zero errors | Yes |
| Intended fixture is collected | Yes |
| Success comes from skipped or empty collection | Reject the result |
| Success is inferred from the placeholder validator | Reject the claim |
| Fixture contains a real production digest or restricted material | Reject the fixture |

### Finite outcomes

| Outcome | Meaning |
|---|---|
| `EXPECTED_ACCEPTANCE` | Parsed, schema loaded, zero errors. |
| `UNEXPECTED_REJECTION` | One or more schema errors; fail. |
| `FIXTURE_ERROR` | Missing or malformed fixture; fail. |
| `HARNESS_ERROR` | Schema, import, dependency, or runner failure; do not report acceptance. |
| `NOT_COLLECTED` | Intended case did not execute; do not report acceptance. |

These names are documentation vocabulary unless separately standardized.

[Back to top](#top)

---

## Coverage boundary

Current coverage proves one positive dimension:

- a minimal object with the `sha256:` prefix and exactly 64 lowercase hexadecimal characters.

It does not provide distinct positive cases for mixed hex characters, boundary digits, multiple synthetic digests, producer metadata, canonicalization, source artifact, issuer, timestamp, signature, alternative algorithms, semantic correctness, or release state.

Add a positive fixture only when it exercises a distinct accepted boundary. Repeating arbitrary valid digests without a coverage purpose adds maintenance cost but little assurance.

[Back to top](#top)

---

## Authoring contract

Before adding or changing a valid fixture:

- use `valid_<n>.json`;
- keep it synthetic, minimal, deterministic, and reviewable;
- ensure it parses and matches the schema exactly;
- avoid extra properties unless schema and contract change deliberately;
- state the distinct accepted boundary it adds;
- update positive and negative siblings together when polarity changes;
- update this README and the parent inventory;
- do not add production hashes, secrets, source payloads, receipts, proofs, or release records;
- do not claim canonicalization or integrity proof from string shape.

Expected-error sidecars belong only in the invalid lane.

[Back to top](#top)

---

## Validation

Repository-native check:

```bash
python -m pytest -q tests/schemas/test_common_contracts.py
```

A bounded direct check must parse `valid_1.json`, load the paired Draft 2020-12 schema, and assert that `iter_errors()` is empty.

For README-only changes also verify one H1, closed metadata, balanced fences, valid anchors and links, no tabs or trailing whitespace, final newline, no secrets or production payloads, and a generated receipt when required.

Review-ready acceptance:

1. every listed fixture exists and parses;
2. every valid fixture is accepted;
3. intended cases are actually collected;
4. the placeholder validator is not presented as implemented;
5. coverage gaps remain visible;
6. no authority or lifecycle boundary is collapsed.

[Back to top](#top)

---

## Correction and rollback

If a valid fixture begins failing:

1. determine whether schema meaning changed intentionally;
2. confirm the fixture still expresses an accepted shape;
3. update contract, schema, valid and invalid fixtures, tests, and docs together when semantics changed;
4. do not weaken the schema merely to restore green status;
5. record compatibility and downstream correction obligations.

If it passes only because collection stopped, restore collection before claiming validation.

Rollback for this documentation-only revision: restore prior blob `928c0758c1f7450f9afd3787a4d272cd6cb12b2d` and remove the paired generated receipt.

[Back to top](#top)

---

## Open verification register

- **NEEDS VERIFICATION** — current PR-head result of `test_common_contracts.py`.
- **NEEDS VERIFICATION** — exact collected case identifier and nonempty collection guarantee.
- **NEEDS VERIFICATION** — owners and CODEOWNERS enforcement.
- **NEEDS VERIFICATION** — positive-coverage threshold.
- **NEEDS VERIFICATION** — implementation of the dedicated validator.
- **NEEDS VERIFICATION** — branch-protection significance.
- **UNKNOWN** — production consumers and canonicalization rules.
- **UNKNOWN** — ignored, generated, branch-local, or external fixture cases.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Limit |
|---|---|---|---|
| Prior README blob `928c0758…` | **CONFIRMED** | Existing v0.1 scope. | Historical claims are not current execution evidence. |
| [`valid_1.json`](valid_1.json) | **CONFIRMED** | Exact minimal positive object. | One shape only. |
| [`../invalid/README.md`](../invalid/README.md) | **CONFIRMED v0.2** | Negative polarity and harness boundary. | Does not prove positive execution. |
| [`../README.md`](../README.md) | **CONFIRMED documentation** | Family placement and linkage. | Contains older maturity wording. |
| [`spec_hash.schema.json`](../../../../../../schemas/contracts/v1/common/spec_hash.schema.json) | **CONFIRMED schema** | Shape and metadata. | Status remains `PROPOSED`. |
| [`spec_hash.md`](../../../../../../contracts/common/spec_hash.md) | **CONFIRMED contract** | Meaning and anti-overclaim boundary. | Canonicalization remains unverified. |
| [`validate_spec_hash.py`](../../../../../../tools/validators/validate_spec_hash.py) | **CONFIRMED placeholder** | Declared path exists. | Raises `NotImplementedError`. |
| [`test_common_contracts.py`](../../../../../../tests/schemas/test_common_contracts.py) | **CONFIRMED executable code** | Discovery and positive assertion. | Current run result is separate evidence. |

[Back to top](#top)
