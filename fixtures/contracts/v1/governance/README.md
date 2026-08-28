<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/governance/readme
title: Governance contract fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): governance steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related:
  - review_record/README.md
  - ../../../../schemas/contracts/v1/governance/review_record.schema.json
  - ../../../../schemas/contracts/v1/governance/promotion_decision.schema.json
  - ../../../../schemas/contracts/v1/governance/redaction_receipt.schema.json
  - ../../../../contracts/governance/README.md
  - ../../../../contracts/governance/ReviewRecord.md
  - ../../../../policy/governance/
  - ../../../../tests/schemas/test_common_contracts.py
  - ../../../../tools/validators/validate_review_record.py
  - ../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, governance, review-record, promotion-decision, redaction-receipt, json-schema, valid-fixtures, invalid-fixtures, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/governance/README.md`."
  - "This directory is a fixture lane only. It does not define semantic contract meaning, machine schema shape, policy decisions, release decisions, or validation implementation."
  - "Current confirmed populated fixture family: `review_record/`. Other governance schemas may exist without fixture families here yet."
  - "The schema metadata for `review_record` declares `contracts/governance/review_record.md`, while the current semantic contract path observed in the repo is `contracts/governance/ReviewRecord.md`; reconcile through schema/contract review before treating that naming as settled."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governance contract fixtures

Fixture lane for KFM governance contract schemas under `schemas/contracts/v1/governance/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: governance" src="https://img.shields.io/badge/family-governance-blue">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
  <img alt="Schema home: schemas/contracts/v1" src="https://img.shields.io/badge/schema__home-schemas%2Fcontracts%2Fv1-informational">
</p>

**Path:** `fixtures/contracts/v1/governance/README.md`  
**Fixture posture:** schema-oriented valid/invalid example lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/governance/`  
**Quick links:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Current inventory](#current-inventory) · [Authority boundary](#authority-boundary) · [Fixture rules](#fixture-rules) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are examples for schema and validator checks. They are not semantic contracts, schema authority, policy authority, review approval, promotion approval, release approval, or evidence.

---

## Purpose

This directory groups fixture families for governance contract schemas.

Use this lane for small, public-safe JSON examples that help prove governance object shapes are enforceable through schema tests. A fixture here can demonstrate that a governance object is accepted or rejected, but it cannot decide whether an artifact is reviewed, promoted, published, redacted, or released.

---

## Placement basis

Directory Rules treats `fixtures/` as a canonical root for golden, valid, and invalid test inputs and separates it from semantic contracts, schemas, policy, release decisions, and lifecycle data.

The responsibility split for this lane is:

| Responsibility | Canonical home | This README posture |
|---|---|---|
| Sample inputs for tests | `fixtures/contracts/v1/governance/` | Documents fixture families only. |
| Machine-checkable shape | `schemas/contracts/v1/governance/` | Referenced, not duplicated. |
| Semantic meaning | `contracts/governance/` | Referenced, not replaced. |
| Admissibility / allow-deny policy | `policy/governance/` and related release/sensitivity policy lanes | Out of scope for fixtures. |
| Enforceability proof | `tests/schemas/` and validator tooling | Referenced, not claimed as executed here. |

> [!NOTE]
> The root `fixtures/README.md` currently describes runtime and benchmark corpora. This existing `fixtures/contracts/v1/...` lane is also used by the schema fixture harness. Until the per-root fixture contract is reconciled, this README narrows only the governance contract fixture subtree and does not claim to settle the whole `fixtures/` root policy.

---

## Current inventory

| Fixture family | Directory | Related schema | Current fixture status | Notes |
|---|---|---|---|---|
| `review_record` | [`review_record/`](review_record/README.md) | `schemas/contracts/v1/governance/review_record.schema.json` | CONFIRMED populated | Contains valid and invalid examples for the current `review_record` schema. |
| `promotion_decision` | `promotion_decision/` | `schemas/contracts/v1/governance/promotion_decision.schema.json` | NOT PRESENT / NEEDS VERIFICATION | Schema scaffold exists; no fixture family confirmed in this subtree during this update. |
| `redaction_receipt` | `redaction_receipt/` | `schemas/contracts/v1/governance/redaction_receipt.schema.json` | NOT PRESENT / NEEDS VERIFICATION | Schema scaffold exists; no fixture family confirmed in this subtree during this update. |

Expected family shape:

```text
fixtures/contracts/v1/governance/<contract_name>/
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
| Small JSON fixtures for governance schemas. | `.schema.json` files. |
| `valid/` examples expected to pass schema validation. | Semantic contract prose as the source of meaning. |
| `invalid/` examples expected to fail schema validation. | Rego/OPA policy bundles or release rules. |
| Expected-error text for negative tests. | Release manifests, promotion decisions as authoritative records, receipts, proofs, or rollback cards. |
| Fixture READMEs that explain test intent and known limits. | RAW, WORK, QUARANTINE, sensitive exact geometry, private records, or source-system exports. |

Governance fixtures are intentionally downstream of the contract/schema/policy split:

```text
contracts/governance/          # semantic meaning
schemas/contracts/v1/governance/ # machine shape
policy/governance/             # admissibility and gate logic
fixtures/contracts/v1/governance/ # sample test inputs
```

---

## Fixture rules

- Keep fixtures small enough to review in a normal pull request.
- Prefer deterministic, public-safe examples.
- Use `valid/valid_<n>.json` for positive cases.
- Use `invalid/invalid_<n>.json` plus `invalid_<n>.expected_error.txt` for negative cases.
- Keep expected-error text stable enough for CI while avoiding overfitting to one validator's full wording.
- Do not include real sensitive records, living-person private data, exact protected-site coordinates, source credentials, or unpublished source dumps.
- Update the fixture README whenever a schema change changes what should pass or fail.

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

For the governance family, that means fixture families under:

```text
fixtures/contracts/v1/governance/<schema_name>/
```

This README documents expected harness behavior only. It does not claim pytest, CI, or dedicated validators were run during this documentation update.

---

## Maintenance checklist

Before changing this subtree:

- [ ] Confirm the related schema path under `schemas/contracts/v1/governance/`.
- [ ] Confirm the semantic contract path under `contracts/governance/` or record the naming mismatch in the verification backlog.
- [ ] Keep sample data in `fixtures/`, not in `schemas/`, `contracts/`, `policy/`, `release/`, or `data/`.
- [ ] Add both positive and negative cases for new governance fixture families.
- [ ] Keep `expected_error.txt` beside the invalid fixture it describes.
- [ ] Avoid sensitive, private, unpublished, or policy-restricted content.
- [ ] Run schema tests before claiming validation success.
- [ ] Update this README and the family README when fixture coverage changes.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Owning root | CONFIRMED | `fixtures/` is a canonical root in Directory Rules and exists in the repo. |
| Parent lane | NEEDS VERIFICATION | `fixtures/contracts/v1/README.md` exists but is blank at the time of this update. |
| Populated governance fixture family | CONFIRMED | `review_record/` is populated and documented. |
| Other governance schemas | CONFIRMED / PARTIAL | `promotion_decision` and `redaction_receipt` schemas exist as scaffolds, but matching fixture families were not confirmed here. |
| Test execution | NOT RUN | No tests, validators, or CI were run as part of this README update. |
| Contract naming | NEEDS VERIFICATION | `review_record.schema.json` metadata declares `contracts/governance/review_record.md`, while the observed semantic contract is `contracts/governance/ReviewRecord.md`. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `fixtures/contracts/v1/governance/README.md` existed as a blank file. | Did not define lane purpose or boundaries. |
| `docs/doctrine/directory-rules.md` | CONFIRMED | Placement protocol, canonical `fixtures/` root, schema-home convention, and contract/schema/policy split. | Does not prove every current nested fixture is complete. |
| `fixtures/README.md` | CONFIRMED / CONFLICT SIGNAL | Documents current root-level fixture purpose and boundary. | Its runtime-fixture wording does not fully describe the existing schema fixture harness. |
| `tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN | Discovers schemas and matching fixture directories under `fixtures/contracts/v1/<family>/<name>/`. | Presence of the harness does not prove tests passed. |
| `schemas/contracts/v1/governance/review_record.schema.json` | CONFIRMED | Defines the `review_record` schema and declares a governance fixture root. | Schema status is `PROPOSED`; metadata contract path needs reconciliation. |
| `schemas/contracts/v1/governance/promotion_decision.schema.json` | CONFIRMED SCAFFOLD | Confirms a governance schema file exists for `Promotion Decision`. | No populated fixture family confirmed in this subtree. |
| `schemas/contracts/v1/governance/redaction_receipt.schema.json` | CONFIRMED SCAFFOLD | Confirms a governance schema file exists for `Redaction Receipt`. | No populated fixture family confirmed in this subtree. |
| `contracts/governance/ReviewRecord.md` | CONFIRMED | Current semantic contract for `ReviewRecord`. | Naming differs from the schema metadata path. |
| `review_record/README.md` | CONFIRMED | Documents the populated `review_record` fixture family. | Does not define the parent governance fixture lane by itself. |

[Back to top](#top)
