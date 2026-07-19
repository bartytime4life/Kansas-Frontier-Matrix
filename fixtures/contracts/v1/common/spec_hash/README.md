<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/common/spec-hash/readme
title: fixtures/contracts/v1/common/spec_hash/ — SpecHash Contract Fixture Family
type: readme; directory-readme; contract-fixture-family; valid-invalid-schema-cases; non-authoritative
version: v0.2
status: draft; repository-grounded; one-valid-one-invalid-confirmed; generic-pytest-confirmed; dedicated-validator-placeholder; partial-coverage
owners: OWNER_TBD — Schema steward · Common-contract steward · Fixture steward · Validator steward · Test/QA steward · Docs steward
created: NEEDS VERIFICATION — file predates the 2026-06-30 v0.1 expansion
updated: 2026-07-19
supersedes: v0.1.0
policy_label: public-review; fixtures; common-contract; spec-hash; synthetic-only; non-authoritative
owning_root: fixtures/
current_path: fixtures/contracts/v1/common/spec_hash/README.md
truth_posture: >
  CONFIRMED prior README; merged v0.2 valid and invalid child READMEs; one valid JSON
  fixture, one invalid JSON fixture, and one expected-error sidecar; paired draft contract;
  Draft 2020-12 schema; generic pytest discovery and polarity checks; dedicated validator
  placeholder / PROPOSED only distinct, reviewable future cases / UNKNOWN production
  consumers, producers, canonicalization, branch protection, and external fixtures /
  NEEDS VERIFICATION owners, CODEOWNERS, exact collected case id, complete coverage,
  dedicated validator implementation, policy integration, and current full-repo pass state
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 1e192dcb99682cc6637e90b80a659f1a0a1797e3
  prior_blob: bc787595d5869c7bd212b0c7909c3eb0b980daf9
  valid_readme_blob: ecd1340ea4cad7106402cea47024ae9973b4cc30
  invalid_readme_blob: ca4e78c0115e6843b8123e6d626cd41221c6c43e
  valid_fixture_blob: 5bad69059af065fd6b0488f4ece8dce98890bce3
  invalid_fixture_blob: 0967ef424bce6791893e9a57bb952f80fd536e93
  expected_error_blob: cb128ae0e4af3f627f25520854312fef678d50e5
  schema_blob: 80b496b01b8de8c0e8ba67bf020977e6b1f3c652
  contract_blob: 0c2c1161ddb565d4f9f17ef81080b27b8d951937
  validator_blob: de69c6c7001082af29827a4b287a80b7c6a05af3
  test_harness_blob: b04342cc034d7f1cc554e155fdd02d6e972976e6
related:
  - ../README.md
  - valid/README.md
  - valid/valid_1.json
  - invalid/README.md
  - invalid/invalid_1.json
  - invalid/invalid_1.expected_error.txt
  - ../../../../../schemas/contracts/v1/common/spec_hash.schema.json
  - ../../../../../contracts/common/spec_hash.md
  - ../../../../../tools/validators/validate_spec_hash.py
  - ../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, common, spec-hash, valid, invalid, json-schema, expected-error, fail-closed, non-authoritative]
notes:
  - "v0.2 aligns this parent with the grounded v0.2 valid and invalid child lanes."
  - "The generic pytest harness is executable; the dedicated validator raises NotImplementedError."
  - "No fixture, schema, contract, validator, test, policy, lifecycle, release, or runtime behavior changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# SpecHash Contract Fixture Family

`fixtures/contracts/v1/common/spec_hash/`

> **Purpose.** Coordinate deterministic positive and negative fixtures for the `spec_hash` schema without allowing fixtures or test output to become semantic truth, canonicalization proof, artifact integrity, policy approval, release authority, or production data.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Valid: one" src="https://img.shields.io/badge/valid-one-2ea44f">
  <img alt="Invalid: one" src="https://img.shields.io/badge/invalid-one-critical">
  <img alt="Validator: placeholder" src="https://img.shields.io/badge/validator-placeholder-red">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture__only-success">
</p>

> [!IMPORTANT]
> A valid fixture proves only that the paired schema accepts the tested shape. An invalid fixture proves only that it rejects the tested shape for the expected reason. Neither proves what bytes were hashed, that producers used the same canonicalization, or that any evidence, policy, review, release, or publication gate passed.

> [!WARNING]
> `tools/validators/validate_spec_hash.py` currently raises `NotImplementedError`. The executable evidence path is the generic pytest harness. A placeholder exception, missing file, parser crash, schema-resolution error, or dependency failure is not successful fixture enforcement.

**Quick links:** [Status](#status-and-evidence-boundary) · [Purpose](#purpose-and-scope) · [Placement](#placement-and-authority) · [Inventory](#confirmed-inventory) · [Schema](#schema-and-contract-basis) · [Harness](#executable-harness) · [Polarity](#polarity-contract) · [Coverage](#coverage-boundary) · [Authoring](#authoring-contract) · [Validation](#validation) · [Correction](#correction-and-rollback) · [Open items](#open-verification-register) · [Evidence](#evidence-ledger)

---

## Status and evidence boundary

| Surface | Status | Safe conclusion |
|---|---|---|
| This README | **CONFIRMED v0.1 file** | Revised in place; prior blob is pinned above. |
| [`valid/`](valid/README.md) | **CONFIRMED v0.2 documentation** | One direct positive case is documented. |
| [`invalid/`](invalid/README.md) | **CONFIRMED v0.2 documentation** | One direct negative case and one sidecar are documented. |
| Paired schema | **CONFIRMED file / `PROPOSED` metadata** | Requires `value`, lowercase SHA-256 form, and no extra fields. |
| Semantic contract | **CONFIRMED draft** | Defines an integrity/reference carrier, not correctness or authority. |
| Generic pytest harness | **CONFIRMED executable code** | Checks valid, invalid, and expected-error behavior. |
| Dedicated validator | **CONFIRMED placeholder** | Not usable enforcement. |
| Complete coverage | **NOT ESTABLISHED** | One positive and one negative dimension are confirmed. |
| Current full-repo test result | **NEEDS VERIFICATION** | Bounded execution is not a full checkout run. |
| Production adoption | **UNKNOWN** | Fixture presence does not establish consumers. |

[Back to top](#top)

---

## Purpose and scope

This family answers two questions:

1. Does the current schema accept the minimal valid `spec_hash` object?
2. Does it reject a deliberately invalid object for the expected reason?

It owns fixture-family coordination, inventory, polarity, and links to authority surfaces. It does **not** own hash computation, canonicalization, semantic meaning, schema shape, validator code, policy, evidence, release, or publication.

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
                ├── README.md
                ├── valid/
                │   ├── README.md
                │   └── valid_1.json
                └── invalid/
                    ├── README.md
                    ├── invalid_1.json
                    └── invalid_1.expected_error.txt
```

| Responsibility | Owning surface |
|---|---|
| Semantic meaning | [`contracts/common/spec_hash.md`](../../../../../contracts/common/spec_hash.md) |
| Machine shape | [`schemas/contracts/v1/common/spec_hash.schema.json`](../../../../../schemas/contracts/v1/common/spec_hash.schema.json) |
| Family coordination | This README |
| Positive cases | [`valid/README.md`](valid/README.md) |
| Negative cases | [`invalid/README.md`](invalid/README.md) |
| Executable generic test | [`tests/schemas/test_common_contracts.py`](../../../../../tests/schemas/test_common_contracts.py) |
| Dedicated validator | [`tools/validators/validate_spec_hash.py`](../../../../../tools/validators/validate_spec_hash.py) |
| Policy, evidence, receipts, proofs, lifecycle, and release | Their separate roots |

[Back to top](#top)

---

## Confirmed inventory

| Lane | File | Expected result |
|---|---|---|
| Positive | [`valid/valid_1.json`](valid/valid_1.json) | Zero schema errors. |
| Negative | [`invalid/invalid_1.json`](invalid/invalid_1.json) | Rejected because `value` is absent. |
| Negative expectation | [`invalid/invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | Combined errors contain `'value' is a required property`. |

No additional direct fixture is claimed.

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
| Required field | `value` |
| Value type | `string` |
| Pattern | `^sha256:[a-f0-9]{64}$` |
| Additional properties | rejected |
| Schema metadata status | `PROPOSED` |
| Declared fixture root | `fixtures/contracts/v1/common/spec_hash/` |
| Declared validator | `tools/validators/validate_spec_hash.py` |

A shape-valid value does not establish the hashed bytes, canonicalization method, producer, authority, freshness, evidence closure, policy allowance, or release state.

[Back to top](#top)

---

## Executable harness

`tests/schemas/test_common_contracts.py`:

1. includes `common` in its family list;
2. maps each common schema to `fixtures/contracts/v1/common/<name>/`;
3. requires every `valid/valid_*.json` to produce no errors;
4. requires every `invalid/invalid_*.json` to produce one or more errors;
5. matches a sibling `.expected_error.txt` when present.

The dedicated validator is separate and currently contains:

```python
NotImplementedError("Greenfield placeholder")
```

Therefore:

```text
generic pytest harness = executable schema-fixture path
dedicated validator CLI = placeholder, not enforcement
```

[Back to top](#top)

---

## Polarity contract

| Outcome | Meaning |
|---|---|
| `EXPECTED_ACCEPTANCE` | Collected valid fixture parsed and produced zero errors. |
| `EXPECTED_REJECTION` | Collected invalid fixture failed for the intended reason. |
| `UNEXPECTED_ACCEPTANCE` | Invalid fixture produced no errors. |
| `UNEXPECTED_REJECTION` | Valid fixture produced errors. |
| `WRONG_REJECTION` | Invalid fixture failed for a different cause. |
| `FIXTURE_ERROR` | JSON or sidecar is malformed or missing. |
| `HARNESS_ERROR` | Schema loading, imports, dependencies, or runner failed. |
| `UNCOLLECTED` | Fixture exists but did not match harness discovery. |

These are documentation labels unless standardized elsewhere.

[Back to top](#top)

---

## Coverage boundary

### Confirmed

- minimal required `value`;
- `sha256:` prefix;
- 64 lowercase hexadecimal characters;
- closed object shape in the positive case;
- missing required `value` in the negative case.

### Not established by direct fixtures

- wrong root or value type;
- missing/changed prefix;
- uppercase or non-hex characters;
- short or long digest;
- whitespace;
- extra properties as a negative case;
- alternative algorithms;
- multiple valid digest examples;
- canonicalization equivalence;
- producer, timestamp, signature, or attestation behavior.

Add cases only when they isolate a distinct schema boundary and improve reviewable coverage.

[Back to top](#top)

---

## Authoring contract

- Use `valid/valid_<n>.json` for positive cases.
- Use `invalid/invalid_<n>.json` for negative cases.
- Use `invalid/invalid_<n>.expected_error.txt` for stable cause matching.
- Keep payloads synthetic, minimal, deterministic, and reviewable.
- Prefer one primary negative concern per fixture.
- Ensure every file matches the current harness glob.
- Update the child README and this inventory together.
- Update contract, schema, fixtures, tests, validator, and consumers together when meaning changes.
- Never store production hashes, credentials, source payloads, receipts, proofs, manifests, release records, or published artifacts here.

[Back to top](#top)

---

## Validation

### Repository-native command

```bash
python -m pytest -q tests/schemas/test_common_contracts.py
```

A narrower selector requires verification of the collected parametrized identifier.

### Acceptance criteria

1. Every documented file exists and parses.
2. Valid fixtures produce zero schema errors.
3. Invalid fixtures produce at least one schema error.
4. Expected-error text matches the intended cause.
5. Every fixture is collected.
6. The dedicated validator remains visibly marked placeholder until implemented.
7. Coverage gaps and schema `PROPOSED` status remain visible.
8. No authority or lifecycle boundary is collapsed.

README-only checks also require one H1, a closed meta block, balanced fences, valid anchors and links, clean whitespace, final newline, no secrets or production digest, and the required generated receipt.

[Back to top](#top)

---

## Correction and rollback

If polarity changes unexpectedly:

1. determine whether the schema changed intentionally;
2. confirm the fixture still expresses its intended case;
3. inspect harness collection and expected-error coupling;
4. update contract, schema, both child lanes, tests, validator, and docs together when meaning changed;
5. never weaken a fixture or sidecar merely to restore a green test;
6. record downstream migration and rollback obligations.

Rollback for this documentation-only revision: restore blob `bc787595d5869c7bd212b0c7909c3eb0b980daf9` and remove the paired generated receipt.

[Back to top](#top)

---

## Open verification register

- **NEEDS VERIFICATION** — PR-head result of `tests/schemas/test_common_contracts.py`.
- **NEEDS VERIFICATION** — exact collected `common/spec_hash` case identifier.
- **NEEDS VERIFICATION** — owners and CODEOWNERS enforcement.
- **NEEDS VERIFICATION** — complete positive/negative coverage threshold.
- **NEEDS VERIFICATION** — dedicated validator implementation.
- **NEEDS VERIFICATION** — required-check and policy integration status.
- **UNKNOWN** — production producers, consumers, and canonicalization rules.
- **UNKNOWN** — ignored, generated, branch-local, LFS, or external fixtures.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Limit |
|---|---|---|---|
| Prior blob `bc787595…` | **CONFIRMED** | v0.1 scope and inventory. | Historical maturity wording is stale. |
| [`valid/README.md`](valid/README.md) | **CONFIRMED v0.2** | Positive-lane boundary and one-case coverage. | Not a current run log. |
| [`valid_1.json`](valid/valid_1.json) | **CONFIRMED** | Minimal accepted shape. | One representative digest. |
| [`invalid/README.md`](invalid/README.md) | **CONFIRMED v0.2** | Negative-lane boundary and cause matching. | Not a current run log. |
| [`invalid_1.json`](invalid/invalid_1.json) | **CONFIRMED** | Missing-value case. | One negative invariant. |
| [`invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | **CONFIRMED** | Expected rejection text. | Coupled to validator wording. |
| [`spec_hash.schema.json`](../../../../../schemas/contracts/v1/common/spec_hash.schema.json) | **CONFIRMED file** | Shape and metadata. | Status remains `PROPOSED`. |
| [`spec_hash.md`](../../../../../contracts/common/spec_hash.md) | **CONFIRMED draft contract** | Meaning and anti-overclaim boundary. | Canonicalization unverified. |
| [`validate_spec_hash.py`](../../../../../tools/validators/validate_spec_hash.py) | **CONFIRMED placeholder** | Dedicated path exists. | Not implemented. |
| [`test_common_contracts.py`](../../../../../tests/schemas/test_common_contracts.py) | **CONFIRMED executable code** | Discovery and polarity checks. | Full-repo result is separate evidence. |

[Back to top](#top)

---

## Changelog

| Date | Version | Change | Status |
|---|---|---|---|
| 2026-06-30 | v0.1.0 | Initial expanded fixture-family README. | Historical baseline |
| 2026-07-19 | v0.2 | Aligned parent with grounded child lanes; pinned evidence; clarified harness, validator, polarity, coverage, correction, and rollback. | **PROPOSED pending review** |

[Back to top](#top)
