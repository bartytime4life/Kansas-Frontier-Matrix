<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/policy/readme
title: Policy contract fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): policy steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related:
  - policy_decision/README.md
  - policy_decision/valid/README.md
  - policy_decision/valid/valid_1.json
  - policy_decision/invalid/README.md
  - policy_decision/invalid/invalid_1.json
  - policy_decision/invalid/invalid_1.expected_error.txt
  - ../../../../schemas/contracts/v1/policy/policy_decision.schema.json
  - ../../../../schemas/contracts/v1/policy/sensitivity_label.schema.json
  - ../../../../contracts/policy/README.md
  - ../../../../contracts/policy/policy_decision.md
  - ../../../../contracts/policy/sensitivity_label.md
  - ../../../../policy/
  - ../../../../tools/validators/
  - ../../../../tests/schemas/test_common_contracts.py
  - ../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, policy, policy-decision, sensitivity-label, valid-fixtures, invalid-fixtures, expected-error, json-schema, finite-outcomes, fail-closed, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/policy/README.md`."
  - "This directory groups policy contract fixture families."
  - "Current confirmed populated fixture family: `policy_decision/`."
  - "The `sensitivity_label` schema declares `fixtures/contracts/v1/policy/sensitivity_label/`, but that fixture family was not confirmed during this update."
  - "No tests, validators, policy bundles, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Policy contract fixtures

Fixture lane for KFM policy contract schemas under `schemas/contracts/v1/policy/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: policy" src="https://img.shields.io/badge/family-policy-blue">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
  <img alt="Schema home: schemas/contracts/v1" src="https://img.shields.io/badge/schema__home-schemas%2Fcontracts%2Fv1-informational">
</p>

**Path:** `fixtures/contracts/v1/policy/README.md`  
**Fixture posture:** schema-oriented valid/invalid example lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/policy/`  
**Quick links:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Current inventory](#current-inventory) · [Authority boundary](#authority-boundary) · [Fixture rules](#fixture-rules) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are examples for schema and validator checks. They are not semantic contracts, schema authority, executable policy, policy approval, release approval, review approval, evidence, receipts, proofs, runtime envelopes, or publication authority.

---

## Purpose

This directory groups fixture families for policy contract schemas.

Use this lane for small, public-safe JSON examples that help prove policy object shapes are enforceable through schema tests. A fixture here can demonstrate that a policy-shaped object is accepted or rejected by a schema, but it cannot decide whether an action is allowed, denied, restricted, abstained from, promoted, published, redacted, or rendered.

---

## Placement basis

Directory Rules treats `fixtures/` as a canonical root for golden, valid, and invalid test inputs and separates it from semantic contracts, schemas, policy, release decisions, lifecycle data, and runtime surfaces.

The responsibility split for this lane is:

| Responsibility | Canonical home | This README posture |
|---|---|---|
| Sample inputs for tests | `fixtures/contracts/v1/policy/` | Documents fixture families only. |
| Machine-checkable shape | `schemas/contracts/v1/policy/` | Referenced, not duplicated. |
| Semantic meaning | `contracts/policy/` | Referenced, not replaced. |
| Executable policy and admissibility rules | `policy/` | Out of scope for fixtures. |
| Runtime policy helpers | `packages/policy-runtime/` or accepted runtime package home | Out of scope for fixtures. |
| Enforceability proof | `tests/schemas/` and validator tooling | Referenced, not claimed as executed here. |

> [!NOTE]
> The root `fixtures/README.md` currently emphasizes runtime and benchmark corpora. This existing `fixtures/contracts/v1/...` lane is also used by the schema fixture harness. Until the per-root fixture contract is reconciled, this README narrows only the policy contract fixture subtree and does not claim to settle the whole `fixtures/` root policy.

---

## Current inventory

| Fixture family | Directory | Related schema | Current fixture status | Notes |
|---|---|---|---|---|
| `policy_decision` | [`policy_decision/`](policy_decision/README.md) | `schemas/contracts/v1/policy/policy_decision.schema.json` | CONFIRMED populated | Contains valid and invalid examples for the current `policy_decision` schema. |
| `sensitivity_label` | `sensitivity_label/` | `schemas/contracts/v1/policy/sensitivity_label.schema.json` | NOT PRESENT / NEEDS VERIFICATION | Schema declares this fixture root, but a populated fixture family was not confirmed during this update. |

Expected family shape:

```text
fixtures/contracts/v1/policy/<contract_name>/
├── README.md
├── valid/
│   ├── README.md
│   └── valid_<n>.json
└── invalid/
    ├── README.md
    ├── invalid_<n>.json
    └── invalid_<n>.expected_error.txt
```

---

## Authority boundary

| This directory may contain | This directory must not contain |
|---|---|
| Small JSON fixtures for policy schemas. | `.schema.json` files. |
| `valid/` examples expected to pass schema validation. | Semantic contract prose as the source of meaning. |
| `invalid/` examples expected to fail schema validation. | Rego/OPA policy bundles or runtime policy code. |
| Expected-error text for negative tests. | Release manifests, promotion decisions as authoritative records, receipts, proofs, or rollback cards. |
| Fixture READMEs that explain test intent and known limits. | RAW, WORK, QUARANTINE, sensitive exact geometry, private records, secrets, or source-system exports. |

Policy fixtures are intentionally downstream of the contract/schema/policy split:

```text
contracts/policy/              # semantic meaning
schemas/contracts/v1/policy/   # machine shape
policy/                        # executable policy and admissibility logic
fixtures/contracts/v1/policy/  # sample test inputs
```

---

## Fixture rules

- Keep fixtures small enough to review in a normal pull request.
- Prefer deterministic, public-safe examples.
- Use `valid/valid_<n>.json` for positive cases.
- Use `invalid/invalid_<n>.json` plus `invalid_<n>.expected_error.txt` for negative cases.
- Keep expected-error text stable enough for CI while avoiding overfitting to one validator's full wording.
- Include at least one missing-required-field invalid fixture for each populated policy fixture family.
- Add enum, pattern, date-time, and additional-property cases as schema coverage matures.
- Do not include real sensitive records, living-person private data, exact protected-site coordinates, source credentials, unpublished source dumps, or runtime secrets.
- Update fixture docs whenever a schema change changes what should pass or fail.

---

## Harness behavior

The current common schema test harness discovers contract schemas from:

```text
schemas/contracts/v1/<family>/*.schema.json
```

When a matching fixture directory exists, it expects:

```text
fixtures/contracts/v1/<family>/<schema_name>/valid/valid_*.json
fixtures/contracts/v1/<family>/<schema_name>/invalid/invalid_*.json
fixtures/contracts/v1/<family>/<schema_name>/invalid/invalid_*.expected_error.txt
```

For policy schemas, that means fixture families under:

```text
fixtures/contracts/v1/policy/<schema_name>/
```

Observed expectations:

| Fixture pattern | Expected result |
|---|---|
| `valid/valid_*.json` | no JSON Schema errors |
| `invalid/invalid_*.json` | at least one JSON Schema error |
| `invalid/invalid_*.expected_error.txt` | expected text appears in combined error messages |

This README documents expected fixture behavior only. It does not claim that pytest, CI, policy bundles, or dedicated policy validators were run during this update.

---

## Maintenance checklist

Before changing this subtree:

- [ ] Confirm the related schema path under `schemas/contracts/v1/policy/`.
- [ ] Confirm the semantic contract path under `contracts/policy/`.
- [ ] Keep sample data in `fixtures/`, not in `schemas/`, `contracts/`, `policy/`, `release/`, or `data/`.
- [ ] Add both positive and negative cases for new policy fixture families.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Avoid sensitive, private, unpublished, or policy-restricted content.
- [ ] Run schema fixture tests before claiming validation success.
- [ ] Update this README and the family README when fixture coverage changes.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Owning root | CONFIRMED | `fixtures/` is a canonical root in Directory Rules and exists in the repo. |
| Populated policy fixture family | CONFIRMED | `policy_decision/` is populated and documented. |
| `policy_decision` valid lane | CONFIRMED | `policy_decision/valid/README.md` and `valid_1.json` exist. |
| `policy_decision` invalid lane | CONFIRMED | `policy_decision/invalid/README.md`, `invalid_1.json`, and `invalid_1.expected_error.txt` exist. |
| Other policy schema fixture roots | NEEDS VERIFICATION | `sensitivity_label.schema.json` declares a fixture root, but a populated fixture family was not confirmed during this update. |
| Test execution | NOT RUN | No validators, pytest, policy tests, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `fixtures/contracts/v1/policy/README.md` existed as a blank file. | Did not define lane purpose or boundaries. |
| `docs/doctrine/directory-rules.md` | CONFIRMED | Placement protocol, canonical `fixtures/` root, schema-home convention, and contract/schema/policy split. | Does not prove every current nested fixture is complete. |
| `fixtures/README.md` | CONFIRMED / CONFLICT SIGNAL | Documents current root-level fixture purpose and boundary. | Its runtime-fixture wording does not fully describe the existing schema fixture harness. |
| `tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN | Discovers schemas and matching fixture directories under `fixtures/contracts/v1/<family>/<name>/`. | Presence of the harness does not prove tests passed. |
| [`policy_decision/README.md`](policy_decision/README.md) | CONFIRMED | Documents the populated `policy_decision` fixture family. | Does not prove tests were run. |
| [`policy_decision/valid/README.md`](policy_decision/valid/README.md) | CONFIRMED | Documents the positive fixture lane. | Does not prove tests were run. |
| [`policy_decision/valid/valid_1.json`](policy_decision/valid/valid_1.json) | CONFIRMED | Current positive fixture includes all schema-required fields and allowed enum values. | Only one valid fixture is currently documented. |
| [`policy_decision/invalid/README.md`](policy_decision/invalid/README.md) | CONFIRMED | Documents the negative fixture lane. | Does not prove tests were run. |
| [`policy_decision/invalid/invalid_1.json`](policy_decision/invalid/invalid_1.json) | CONFIRMED | Current negative fixture omits required `decision_id`. | Only one invalid fixture is currently documented. |
| [`policy_decision/invalid/invalid_1.expected_error.txt`](policy_decision/invalid/invalid_1.expected_error.txt) | CONFIRMED | Current expected-error matcher is `required`. | Broad matcher; may be tightened later. |
| [`../../../../schemas/contracts/v1/policy/policy_decision.schema.json`](../../../../schemas/contracts/v1/policy/policy_decision.schema.json) | CONFIRMED | Schema shape, required fields, enum values, date-time format, fixture root, validator path, and status. | Schema status is `PROPOSED`; validator implementation was not verified. |
| [`../../../../schemas/contracts/v1/policy/sensitivity_label.schema.json`](../../../../schemas/contracts/v1/policy/sensitivity_label.schema.json) | CONFIRMED | A second policy schema exists and declares a fixture root. | Matching fixture family was not confirmed during this update. |
| [`../../../../contracts/policy/policy_decision.md`](../../../../contracts/policy/policy_decision.md) | CONFIRMED | Semantic meaning, finite outcome boundary, and distinction from schema, executable policy, release, and runtime envelopes. | Does not prove policy runtime enforcement or CI status. |

[Back to top](#top)
