<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/evidence/evidence-bundle/invalid/readme
title: fixtures/contracts/v1/evidence/evidence_bundle/invalid/ — EvidenceBundle Negative Fixture Contract
type: readme; directory-readme; invalid-contract-fixture-lane; evidence-contract; json-schema-negative-case; non-authoritative
version: v0.2
status: draft; repository-grounded; one-invalid-fixture-confirmed; dedicated-validator-wrapper-confirmed; generic-pytest-harness-confirmed; broad-expected-error-matcher; partial-negative-coverage
owners: OWNER_TBD — Evidence steward · Evidence-contract steward · Schema steward · Fixture steward · Validator steward · Test/QA steward · Policy steward · Docs steward
created: NEEDS VERIFICATION — file predates the 2026-06-30 v0.1 expansion
updated: 2026-07-19
supersedes: v0.1.0
policy_label: public-review; fixtures; contracts; evidence; evidence-bundle; invalid; synthetic-only; evidence-closure-not-proof; non-authoritative
owning_root: fixtures/
current_path: fixtures/contracts/v1/evidence/evidence_bundle/invalid/README.md
truth_posture: >
  CONFIRMED target v0.1 README and prior blob; one invalid fixture; one broad
  expected-error sidecar; sibling valid case; EvidenceBundle semantic contract;
  Draft 2020-12 schema and nested EvidenceRef, SensitivityLabel, and SpecHash schemas;
  dedicated validator wrapper, shared runner, local resolver, generic pytest harness,
  and reconstructed exact-fixture results / PROPOSED exact bundle_id error text and
  one-failure-per-fixture coverage expansion / UNKNOWN production consumers,
  canonicalization, policy/release adoption, branch-protection significance, and
  external fixtures / NEEDS VERIFICATION owners, CODEOWNERS, exact pytest case id,
  complete coverage, format-enforcement decision, CI admission, and current full-repo pass state
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 7bf8b8d6e797bb9930ae73830029dccfbbda3846
  prior_blob: 154e5f72a7d9c7a44fbac368813b56e3aa11cd3d
  invalid_fixture_blob: 63986c0b9e3f09415a3f41290f64df229fd1d603
  expected_error_blob: fad9e164aec60a8ec755ab4b7a235a4a76a7b9f6
  valid_fixture_blob: c0e41762e4318907acbc8425f2be77da4af43b8c
  schema_blob: cf5256831b63dca46a5f68b168441adcf68b8751
  semantic_contract_blob: 731c348832add23cddd14e796aa56ce2b9268259
  validator_wrapper_blob: c1760c5e92eae6390f5adcde4593e8e9bab26535
  jsonschema_runner_blob: ce05ae25d0cb6fc29a2ea41db6c65a99ca5e13e6
  local_resolver_blob: 171a2b8251d10fcc276107459a41056cdedc8ff5
  generic_harness_blob: b04342cc034d7f1cc554e155fdd02d6e972976e6
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
related:
  - ../README.md
  - ../valid/README.md
  - ../valid/valid_1.json
  - invalid_1.json
  - invalid_1.expected_error.txt
  - ../../../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json
  - ../../../../../../schemas/contracts/v1/evidence/evidence_ref.schema.json
  - ../../../../../../schemas/contracts/v1/policy/sensitivity_label.schema.json
  - ../../../../../../schemas/contracts/v1/common/spec_hash.schema.json
  - ../../../../../../contracts/evidence/evidence_bundle.md
  - ../../../../../../tools/validators/validate_evidence_bundle.py
  - ../../../../../../tools/validators/_common/jsonschema_runner.py
  - ../../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, evidence, evidence-bundle, invalid-fixtures, json-schema, expected-error, negative-tests, cite-or-abstain, non-authoritative]
notes:
  - "The direct lane contains one invalid JSON fixture and one broad expected-error sidecar."
  - "The dedicated EvidenceBundle validator is an executable wrapper, not a placeholder."
  - "Single-file exit code 1 is ambiguous between schema rejection and exceptions; cause-specific evidence is required."
  - "This documentation-only revision changes no fixture payload, schema, contract, validator, test, policy, proof, receipt schema, release record, lifecycle state, or public behavior."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# EvidenceBundle Negative Fixture Contract

`fixtures/contracts/v1/evidence/evidence_bundle/invalid/`

> **Purpose.** Hold deterministic EvidenceBundle-shaped JSON instances that must be rejected by the paired schema for a known reason, without allowing fixture failure, validator output, or a schema-valid object to become evidence authority, proof authority, policy clearance, release approval, or public truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Family: evidence" src="https://img.shields.io/badge/family-evidence-blue">
  <img alt="Fixture kind: invalid" src="https://img.shields.io/badge/fixture-invalid-critical">
  <img alt="Coverage: one case" src="https://img.shields.io/badge/coverage-one__case-orange">
  <img alt="Validator: wrapper confirmed" src="https://img.shields.io/badge/validator-wrapper__confirmed-success">
</p>

> [!IMPORTANT]
> Every `invalid_*.json` file here must parse as JSON, resolve the paired schema and nested references, and fail for its intended machine-shape condition. A missing file, parser exception, unresolved `$ref`, import failure, or runner crash is **not** an expected rejection.

> [!CAUTION]
> These fixtures are test inputs only. They are not operational EvidenceBundles, ProofPacks, PolicyDecisions, ReviewRecords, ReleaseManifests, receipts, source records, catalog records, published data, or AI-answer authority.

**Quick links:** [Status](#status-and-evidence-boundary) · [Purpose](#purpose-and-authority) · [Inventory](#confirmed-inventory) · [Schema](#schema-and-contract-basis) · [Validation](#executable-validation-surfaces) · [Failure contract](#negative-fixture-failure-contract) · [Coverage](#coverage-boundary) · [Maintenance](#maintenance-and-validation) · [Rollback](#correction-and-rollback) · [Open items](#open-verification-register) · [Evidence](#evidence-ledger)

---

## Status and evidence boundary

| Surface | Status | Safe conclusion |
|---|---|---|
| This README | **CONFIRMED existing v0.1** | Revised in place; prior blob is pinned above. |
| `invalid_1.json` | **CONFIRMED** | Matches the positive case except required `bundle_id` is absent. |
| Expected-error sidecar | **CONFIRMED / broad** | Contains `required`; it matches the current message but is not field-specific. |
| Sibling valid case | **CONFIRMED** | Includes `bundle_id` and produced zero Draft 2020-12 errors in reconstruction. |
| EvidenceBundle schema | **CONFIRMED file / `PROPOSED` metadata status** | Closed required-field object with three nested schema references. |
| Nested reference resolution | **CONFIRMED in reconstruction** | EvidenceRef, SensitivityLabel, and SpecHash resolved. |
| Generic pytest harness | **CONFIRMED code / reconstructed PASS** | Checks valid/invalid polarity and sidecar text. |
| Dedicated wrapper | **CONFIRMED executable / reconstructed behavior checked** | Targets this exact schema and fixture root. |
| Full-repository PR-head result | **NEEDS VERIFICATION** | Reconstructed execution is not current full-repo CI. |
| Complete negative coverage | **NOT ESTABLISHED** | One missing-`bundle_id` case is confirmed. |

### Truth labels

- **CONFIRMED** — verified from repository files or deterministic reconstructed execution.
- **PROPOSED** — recommended future behavior or coverage.
- **UNKNOWN** — not resolved from current evidence.
- **NEEDS VERIFICATION** — checkable but not sufficiently proven for reliance.

[Back to top](#top)

---

## Purpose and authority

This lane answers one narrow question:

> Does the current EvidenceBundle schema reject a deliberately incomplete instance for the intended missing-`bundle_id` reason?

Directory Rules places reusable valid/invalid test inputs under `fixtures/`, paired with `tests/`. This path remains partitioned by contract version, family, object, and polarity.

| Responsibility | Owning surface |
|---|---|
| EvidenceBundle meaning | [`contracts/evidence/evidence_bundle.md`](../../../../../../contracts/evidence/evidence_bundle.md) |
| Machine shape | [`schemas/contracts/v1/evidence/evidence_bundle.schema.json`](../../../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json) |
| Invalid fixtures | This directory |
| Valid fixtures | [`../valid/`](../valid/README.md) |
| Generic schema harness | [`tests/schemas/test_common_contracts.py`](../../../../../../tests/schemas/test_common_contracts.py) |
| Dedicated validator entry point | [`tools/validators/validate_evidence_bundle.py`](../../../../../../tools/validators/validate_evidence_bundle.py) |
| Policy, proofs, receipts, release, publication | Their separate KFM authority roots |

This README coordinates fixture behavior only. It does not become semantic, schema, policy, proof, release, or public authority.

[Back to top](#top)

---

## Confirmed inventory

| Path | Content | Expected result |
|---|---|---|
| [`invalid_1.json`](invalid_1.json) | EvidenceBundle-shaped object with every current required top-level field except `bundle_id`. | Reject for missing `bundle_id`. |
| [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt) | `required` | Harness finds this token in combined schema messages. |
| [`../valid/valid_1.json`](../valid/valid_1.json) | Same minimal family shape plus `bundle_id: bundle:1`. | Zero schema errors. |

The exact reconstructed error was:

```text
'bundle_id' is a required property
```

The current `required` sidecar matches but is broad. Tightening it to the exact message is **PROPOSED**, not part of this README-only change.

[Back to top](#top)

---

## Schema and contract basis

The paired schema requires:

| Field | Current machine requirement |
|---|---|
| `bundle_id` | Required string matching `^[a-z][a-z0-9_:.-]*$`. |
| `claim_scope` | Required string. |
| `evidence_refs` | Required non-empty array of EvidenceRef objects. |
| `source_records` | Required non-empty string array. |
| `citations` | Required non-empty string array. |
| `rights` | Required object with required `license`; extra fields rejected. |
| `sensitivity` | Required SensitivityLabel reference. |
| `transforms` | Required string array; current schema permits empty. |
| `checksums` | Required non-empty object; values match `sha256:<64 lowercase hex>`. |
| `spec_hash` | Required SpecHash reference. |
| Undeclared top-level fields | Rejected. |

Nested schema chain:

```text
evidence_bundle.schema.json
├── evidence/evidence_ref.schema.json
├── policy/sensitivity_label.schema.json
└── common/spec_hash.schema.json
```

The semantic contract defines EvidenceBundle as claim-scope evidence closure. Schema validity does **not** prove referenced evidence exists, citations support the claim, rights and sensitivity are correct, transforms are reproducible, checksums cover the right artifacts, or release/publication is authorized.

### Format-enforcement limitation

`SensitivityLabel.applied_at` declares `format: date-time`, but the shared runner creates `Draft202012Validator` without a `FormatChecker`. In reconstruction, invalid date-time syntax produced no schema error. Date-time format enforcement is therefore **not established** by this lane.

[Back to top](#top)

---

## Executable validation surfaces

### Generic pytest harness

```bash
python -m pytest -q tests/schemas/test_common_contracts.py
```

The harness discovers evidence-family fixture directories, requires valid cases to produce zero errors, requires invalid cases to produce errors, and matches sidecar text. The reconstructed EvidenceBundle case passed.

### Dedicated family wrapper

```bash
python tools/validators/validate_evidence_bundle.py --fixtures
```

Observed reconstructed output:

```text
OK fixtures/contracts/v1/evidence/evidence_bundle/valid/valid_1.json
FAIL fixtures/contracts/v1/evidence/evidence_bundle/invalid/invalid_1.json: 'bundle_id' is a required property
```

Observed exit code: `0`.

The per-file `FAIL` is expected for the negative fixture; suite success comes from the subsequent polarity check.

### Single-file and error behavior

```bash
python tools/validators/validate_evidence_bundle.py fixtures/contracts/v1/evidence/evidence_bundle/invalid/invalid_1.json
```

Observed exit code: `1`.

A missing file also returned `1`, so single-file code `1` is not cause-specific. No arguments returned `2` with `No files provided`.

[Back to top](#top)

---

## Negative fixture failure contract

| Outcome | Meaning |
|---|---|
| `EXPECTED_REJECTION` | JSON parsed, schema resolved, and intended condition was detected. |
| `UNEXPECTED_PASS` | Invalid fixture produced no schema errors. |
| `WRONG_REJECTION` | Fixture failed, but the expected cause did not match. |
| `FIXTURE_ERROR` | Fixture or sidecar is malformed, missing, or unreadable. |
| `HARNESS_ERROR` | Schema resolution, dependency, import, or runner failed. |
| `UNCOLLECTED` | Expected fixture was not discovered. |
| `FAMILY_POLARITY_PASS` | All discovered valid cases passed and invalid cases were rejected. |

A result is acceptable only when the fixture exists, parses, resolves all nested schemas, fails schema validation, and matches the intended cause. Exceptions and missing files must not be counted as expected rejection.

These outcome names are documentation vocabulary unless separately standardized.

[Back to top](#top)

---

## Coverage boundary

Current coverage proves only:

- missing required `bundle_id`.

It does not establish negative coverage for:

- invalid `bundle_id` type or pattern;
- missing or wrong-type `claim_scope`;
- empty or malformed `evidence_refs`;
- empty `source_records` or `citations`;
- missing `rights.license` or extra rights fields;
- sensitivity enum or date-time failures;
- missing or wrong-type `transforms`;
- invalid checksum or SpecHash values;
- undeclared top-level properties;
- resolver failure;
- semantic claim/evidence mismatch;
- rights, policy, review, release, or publication failure.

These are **PROPOSED** future cases. Each should isolate one primary failure where practical.

[Back to top](#top)

---

## Maintenance and validation

Before adding or changing an invalid fixture:

- use `invalid_<n>.json`;
- keep the payload synthetic and minimal;
- target one primary machine-shape invariant;
- ensure JSON parses before schema validation;
- keep unrelated nested references valid;
- add a narrow `.expected_error.txt` when cause-specific assurance matters;
- verify expected text against the actual runner;
- update sibling and parent documentation when coverage changes;
- never place real evidence, source records, citations, rights records, sensitive data, production identifiers, or production hashes here.

Run:

```bash
python tools/validators/validate_evidence_bundle.py --fixtures
python -m pytest -q tests/schemas/test_common_contracts.py
```

A README change is review-ready when Markdown structure and links pass, fixtures and sidecars exist, nested schemas resolve, polarity is correct, the intended cause matches, coverage gaps remain visible, and authority boundaries remain separate.

[Back to top](#top)

---

## Correction and rollback

If the invalid fixture begins passing:

1. determine whether the schema changed intentionally;
2. verify the fixture still omits the intended field;
3. inspect nested schema and resolver changes;
4. update contract, schema, valid/invalid fixtures, sidecars, tests, validators, and docs together when semantics changed;
5. do not weaken sidecar matching merely to restore green CI;
6. assess downstream producers, consumers, proofs, policy decisions, release records, and public surfaces when compatibility changed.

README rollback:

- restore prior blob `154e5f72a7d9c7a44fbac368813b56e3aa11cd3d`;
- remove the paired generated receipt;
- leave fixture JSON, sidecar, schema, validator, and tests unchanged.

[Back to top](#top)

---

## Open verification register

- **NEEDS VERIFICATION** — current PR-head full-repository schema result.
- **NEEDS VERIFICATION** — exact collected pytest identifier for EvidenceBundle.
- **NEEDS VERIFICATION** — required-check and branch-protection status.
- **NEEDS VERIFICATION** — owners and CODEOWNERS enforcement.
- **NEEDS VERIFICATION** — accepted negative-case coverage threshold.
- **NEEDS VERIFICATION** — whether `required` should become the exact `bundle_id` error.
- **NEEDS VERIFICATION** — whether format checking should be enabled in the shared runner.
- **NEEDS VERIFICATION** — dedicated wrapper admission in CI and release gates.
- **UNKNOWN** — production producers, consumers, canonicalization, and external fixtures.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Limit |
|---|---|---|---|
| Prior README blob `154e5f72…` | **CONFIRMED** | Existing v0.1 scope. | Historical narrative is not current implementation evidence. |
| [`invalid_1.json`](invalid_1.json) | **CONFIRMED** | Missing-`bundle_id` negative case. | One invariant only. |
| [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt) | **CONFIRMED / broad** | Matches current required-property message. | Could match another required-field error. |
| [`../valid/valid_1.json`](../valid/valid_1.json) | **CONFIRMED** | Positive comparison and zero-error polarity. | One positive case. |
| [`evidence_bundle.schema.json`](../../../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json) | **CONFIRMED schema** | Required fields, nested refs, closed object, metadata. | Status remains `PROPOSED`; shape is not semantic closure. |
| [`evidence_bundle.md`](../../../../../../contracts/evidence/evidence_bundle.md) | **CONFIRMED contract** | Claim-scope closure and anti-collapse boundary. | Runtime, policy, and release require separate evidence. |
| [`validate_evidence_bundle.py`](../../../../../../tools/validators/validate_evidence_bundle.py) | **CONFIRMED wrapper** | Exact schema and fixture-root wiring. | Delegates to shared runner. |
| [`jsonschema_runner.py`](../../../../../../tools/validators/_common/jsonschema_runner.py) | **CONFIRMED code** | Exit codes, per-file output, polarity, exceptions. | Single-file code `1` is ambiguous. |
| [`test_common_contracts.py`](../../../../../../tests/schemas/test_common_contracts.py) | **CONFIRMED code / reconstructed PASS** | Discovery, polarity, sidecar matching. | Full-repo current run is separate evidence. |
| [`directory-rules.md`](../../../../../../docs/doctrine/directory-rules.md) | **CONFIRMED doctrine** | Placement and tests/fixtures separation. | Specific paths require live repo evidence. |

[Back to top](#top)

---

## Changelog

### v0.2 — 2026-07-19

- replaced stale blank-file history with current repository evidence;
- confirmed executable dedicated-wrapper behavior;
- recorded exact fixture, nested-schema, and harness results;
- documented broad sidecar and format-checking limitations;
- added failure outcomes, coverage, correction, and rollback;
- changed documentation only.

### v0.1.0 — 2026-06-30

- expanded the previously blank README into initial fixture guidance.

[Back to top](#top)
