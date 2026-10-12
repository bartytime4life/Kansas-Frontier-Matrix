<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-release-rollback-card
title: contracts/release/rollback_card.md — RollbackCard Contract
type: contract
version: v1.0
status: draft; PROPOSED; schema-paired; fixture-first; non-executing
owners:
  - "NEEDS VERIFICATION — release and rollback stewardship assignment"
created: NEEDS VERIFICATION — file predates this convergence
updated: 2026-08-15
policy_label: public; contracts; release; rollback-card; correction-aware; reversible; fail-closed; no-erasure
owning_root: contracts/
responsibility: Define RollbackCard semantic meaning and invariants without executing rollback or creating release authority.
truth_posture: cite-or-abstain
schema: schemas/contracts/v1/release/rollback_card.schema.json
schema_version: 1.0.0
validator: tools/validators/release/validate_rollback_card.py
fixtures: fixtures/release/rollback_card/
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  baseline: 7b0b31613f9623771dc893146826e053d1c248b5
  prior_contract_blob: 72ab9e148491243cc8a374556350ab94c2557ab4
  schema_blob: e0a9edf02dd5d6997eda60a054a5bf19636c3dd4
  validator_blob: 9e9ed5a92851935b41a36698e4bead13ef4edf57
  workflow_blob: 24d1cf575528f70ace558de6cf93b70249ce1a0a
related:
  - ./README.md
  - ./release_manifest.md
  - ./promotion_decision.md
  - ./withdrawal_notice.md
  - ../correction/correction_notice.md
  - ../../schemas/contracts/v1/release/rollback_card.schema.json
  - ../../fixtures/release/rollback_card/
  - ../../tools/validators/release/validate_rollback_card.py
  - ../../tests/validators/test_validate_rollback_card.py
  - ../../docs/adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "This revision removes stale thin-schema claims and synchronizes the semantic contract with the existing closed 1.0.0 fixture-first schema and validator."
  - "The schema, fixtures, validator, tests, workflow, and ADR remain separate authorities and are not accepted or promoted by this document."
  - "A valid candidate proves shape and local consistency only; governance flags remain false and release_ref remains null."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# RollbackCard Contract

> `RollbackCard` records a proposed rollback, withdrawal, hold, or error disposition against an affected release. It identifies the intended target, support references, correction linkage, invalidation scope, restoration posture, timing, lineage, and explicit non-authority state. It is not proof that rollback was approved or executed.

**Status:** draft / **PROPOSED**  
**Path:** `contracts/release/rollback_card.md`  
**Paired schema:** `schemas/contracts/v1/release/rollback_card.schema.json`  
**Schema profile:** `RollbackCard` `1.0.0`, closed (`additionalProperties: false`), fixture-first  
**Validator:** `tools/validators/release/validate_rollback_card.py` — implemented, no-network, candidate-only  
**Current fixture inventory:** 3 valid candidates and 6 invalid candidates plus the expected-findings manifest  
**Authority limit:** candidate shape and local consistency only; no review, policy decision, rollback execution, public mutation, release, or publication

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Schema-paired field surface](#schema-paired-field-surface) · [Finite vocabularies](#finite-vocabularies) · [Field semantics](#field-semantics) · [Invariants](#invariants) · [Lifecycle role](#lifecycle-role) · [Boundaries](#boundaries) · [Validation expectations](#validation-expectations) · [Fixtures](#fixtures) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`RollbackCard` makes a candidate recovery transition inspectable before any operational mutation. It answers:

- which release is affected;
- whether the candidate proposes a prior release, withdrawal, hold, or error posture;
- what evidence, policy, review, and correction records are referenced;
- which caches, catalogs, tiles, indexes, AI caches, and downstream derivatives require invalidation;
- what release, if any, should be restored;
- when the issue was detected, decided, and expected to become effective;
- how this card relates to earlier or later cards;
- whether any authority or public mutation has occurred.

A card does not execute those actions. Operational rollback requires separate accountable decision, review, release, correction, execution, invalidation, and receipt surfaces.

---

## Meaning

A `RollbackCard` is an immutable candidate plan and target binding. It may represent:

- `ROLLBACK_CANDIDATE` — restore a distinct prior release;
- `WITHDRAWAL_CANDIDATE` — withdraw without selecting a prior release;
- `HOLD` — stop or delay a transition pending resolution;
- `ERROR` — record an invalid or failed recovery evaluation without mutating public state.

Rollback is not deletion or silent mutation. Audit history remains inspectable unless a separate lawful and policy-governed removal process applies.

---

## Schema-paired field surface

Every schema-valid candidate contains all fields below. The semantic contract explains their meaning; the paired JSON Schema defines machine shape.

| Field | Required | Semantic role |
|---|---:|---|
| `object_type` | yes | Constant `RollbackCard`. |
| `schema_version` | yes | Constant `1.0.0`. |
| `id` | yes | Stable card identifier matching `rollback:<scope>:...`. |
| `version` | yes | Semantic version of the candidate. |
| `spec_hash` | yes | Non-placeholder SHA-256 binding for the candidate profile. |
| `disposition` | yes | Finite candidate outcome. |
| `trigger` | yes | Safe reason code and timezone-aware detection time. |
| `affected_release_ref` | yes | Release whose current use is under review. |
| `target` | yes | Prior-release, withdrawal, or hold target. |
| `evidence_bundle_refs` | yes | Canonical, sorted, unique evidence support references. |
| `policy_decision_refs` | yes | Canonical, sorted, unique policy references. |
| `review_record_refs` | yes | Canonical, sorted, unique review references. |
| `correction_notice_ref` | yes | Correction/notice reference or `null` when public notice is not required. |
| `invalidations` | yes | One or more bounded invalidation classes. |
| `restoration` | yes | Intended restored release, notice requirement, and validation requirement. |
| `timing` | yes | Decision and optional effective times. |
| `lineage` | yes | `supersedes` and `superseded_by` references. |
| `governance` | yes | Explicit non-authority flags and `release_ref: null`. |

---

## Finite vocabularies

### Disposition

`ROLLBACK_CANDIDATE`, `WITHDRAWAL_CANDIDATE`, `HOLD`, or `ERROR`.

### Trigger reason code

`RELEASE_DEFECT`, `EVIDENCE_CONTRADICTION`, `RIGHTS_CHANGE`, `SENSITIVITY_DISCOVERY`, `VALIDATION_FAILURE`, `SOURCE_WITHDRAWAL`, `POLICY_FAILURE`, `SECURITY_ISSUE`, `OPERATIONAL_FAILURE`, `EMERGENCY_HOLD`, `INSUFFICIENT_EVIDENCE`, or `INPUT_INVALID`.

### Target mode

`PRIOR_RELEASE`, `WITHDRAWAL`, or `HOLD`.

### Invalidation class

`API_CACHE`, `CDN`, `TILES`, `CATALOG`, `TRIPLETS`, `SEARCH_INDEX`, `VECTOR_INDEX`, `AI_CACHE`, or `DOWNSTREAM_DERIVATIVES`.

---

## Field semantics

### Identity and digest

`id` identifies one candidate card and must not act as a mutable pointer. `version` records its semantic version. `spec_hash` binds the candidate's deterministic representation and must not use the all-zero placeholder digest.

### Trigger and affected release

`trigger.reason_code` is a public-safe classification, not a place to expose secrets, private review text, exploit details, or protected locations. `trigger.detected_at` is timezone-aware. `affected_release_ref` must resolve through the release process before any operational action.

### Target and restoration

For `ROLLBACK_CANDIDATE`, `target.mode` is `PRIOR_RELEASE`, `target.release_ref` is a distinct release, and `restoration.restore_release_ref` matches it. Withdrawal and hold dispositions use `null` release targets as defined by the validator. `restoration.validation_required` is always `true`.

### Support references

Evidence, policy, and review references remain separate arrays. Their presence does not prove resolution or approval. The validator requires non-empty evidence and policy references for a rollback candidate and canonical ordering for every populated reference or invalidation array.

### Correction and public notice

When `restoration.public_notice_required` is `true`, `correction_notice_ref` is required. The CorrectionNotice surface explains the public change; the RollbackCard does not replace it.

### Timing and lineage

Detection must not occur after decision; an effective time must not precede decision. A card cannot supersede itself or name itself as its superseding card.

### Governance boundary

The fixture-first profile deliberately requires all of these to remain false:

- `authority_created`;
- `policy_evaluated`;
- `review_completed`;
- `rollback_executed`;
- `public_state_mutated`.

`governance.release_ref` remains `null`. Any contrary claim fails validation with `GOVERNANCE_BOUNDARY_VIOLATION`.

---

## Invariants

The current schema and validator jointly enforce these bounded invariants:

1. The object is closed and versioned as `RollbackCard` `1.0.0`.
2. Required fields are present and use the finite vocabularies above.
3. The spec hash is not the all-zero placeholder.
4. Populated reference and invalidation arrays are sorted and unique.
5. Disposition and target mode agree.
6. A rollback candidate names a distinct prior release and supplies evidence and policy references.
7. The restoration release matches the prior-release target.
8. A required public notice has a correction reference.
9. Detection, decision, and effective times are ordered.
10. Lineage is not self-referential.
11. Candidate validation cannot claim authority, completed policy/review, execution, public mutation, or release.

These checks do **not** resolve references, authenticate actors, verify signatures, execute policy, confirm a prior release is safe, mutate an alias, invalidate a cache, issue a correction, execute rollback, release, or publish.

---

## Lifecycle role

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
                                                                    |
                                                                    v
                                             candidate correction / withdrawal / rollback
```

`RollbackCard` belongs to release and recovery planning. Candidate instances and validated fixture examples remain distinct from accepted rollback decisions, executed rollback receipts, and public correction records.

---

## Boundaries

| Boundary | Rule |
|---|---|
| Contract vs schema | This file defines meaning; the schema defines machine shape. |
| Contract vs validator | The validator proves bounded shape and local cross-field consistency. |
| RollbackCard vs ReleaseManifest | The card names affected and target releases; the manifest binds released contents. |
| RollbackCard vs CorrectionNotice | The notice explains public correction, withdrawal, or supersession. |
| RollbackCard vs PromotionDecision | Promotion may require rollback support; the card does not authorize promotion. |
| RollbackCard vs receipt/proof | A card may reference them; it is not proof of decision or execution. |
| RollbackCard vs public clients | Public clients consume governed released state and never execute rollback. |

---

## Validation expectations

Repository-native focused checks:

```bash
python tools/validators/release/validate_rollback_card.py --fixtures
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_rollback_card.py' \
  --verbose
python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/genrec-rollback-card-contract-current-binding-20260815.json \
  --repo-root .
make workflow-security
```

A green result proves only the scope named by each validator. Hosted execution, policy activation, reviewer authority, branch-protection coupling, and operational rollback remain `NEEDS VERIFICATION`.

---

## Fixtures

### Valid candidates

- `valid_hold.json`;
- `valid_prior_release_candidate.json`;
- `valid_withdrawal_candidate.json`.

### Invalid candidates

- `invalid_authority_claim.json`;
- `invalid_missing_correction_notice.json`;
- `invalid_missing_target_release.json`;
- `invalid_same_release_target.json`;
- `invalid_time_order.json`;
- `invalid_zero_digest.json`.

`invalid/expected_findings_manifest.json` binds each invalid fixture to its exact expected finding set.

---

## Open questions

- Which accepted actor and separation-of-duties model may approve or execute a RollbackCard?
- Which policy profile resolves support references and authorizes emergency handling?
- What accepted physical alias/profile, if any, will operational rollback mutate?
- Which execution receipt records cache, tile, catalog, API, search, vector, and AI invalidation completion?
- Should accepted rollback decisions and execution receipts be signed or DSSE-wrapped?
- What public correction and status surfaces are required for each consequence class?

Until those questions are resolved by accepted governance and implementation evidence, the candidate profile remains non-executing and non-publishing.

---

## Rollback

Revert this contract convergence and its paired workflow current-binding receipt if the document diverges from the existing schema/validator, overstates authority, breaks stable anchors, or causes repository-native checks to fail. Reverting this documentation packet does not alter schemas, candidate fixtures, release state, published data, caches, sources, or public surfaces.

<p align="right"><a href="#top">Back to top</a></p>
