<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/policy/policy-obligation-set
title: PolicyObligationSet Contract
type: contract
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD — Policy steward · Contracts steward · Schema steward · Validation steward
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; fixture-only; non-authoritative
related:
  - ../../schemas/contracts/v1/policy/policy_obligation_set.schema.json
  - ../../fixtures/contracts/v1/policy/policy_obligation_set/
  - ../../tools/validators/policy/validate_policy_obligation_set.py
  - ../../tests/validators/test_validate_policy_obligation_set.py
  - policy_obligation_reduction.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, policy, obligations, rights, attribution, share-alike, retention, aggregation, consent, embargo]
notes:
  - "This contract defines a fixture-only carrier for already-declared downstream duties."
  - "It does not evaluate policy, enforce a duty, mutate an EvidenceBundle, or authorize release."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# PolicyObligationSet Contract

> **Purpose.** Carry structured downstream duties with a candidate subject so attribution, share-alike, retention, aggregation-only, redistribution, notice, consent, and embargo requirements are visible and machine-checkable instead of buried in prose.

## Status and boundary

| Field | Value |
|---|---|
| Contract status | `PROPOSED_INACTIVE` |
| Execution mode | `FIXTURE_ONLY` |
| Machine shape | `schemas/contracts/v1/policy/policy_obligation_set.schema.json` |
| Validator | `tools/validators/policy/validate_policy_obligation_set.py` |
| Live policy engine | None |
| EvidenceBundle integration | None |
| Enforcement effect | None |
| Promotion, release, publication effect | None |

A conforming object proves only that one synthetic obligation set matches this closed candidate contract and its deterministic identity rules. It does **not** prove that an accepted policy decision issued any duty, that the referenced basis is current or authorized, that a consumer complied, or that a candidate may be promoted, released, or published.

## Source-derived design

Pass 7 card `KFM-P7-PROG-0004` distinguishes permission from obligation: licensing and policy may answer whether an operation is allowed, while an obligations object records what a downstream consumer must do. The card names attribution, share-alike, retention, and aggregation-only duties as examples. The repository already contains `PolicyObligationReduction`, which mechanically combines transform-oriented obligations that have already been issued. This contract fills the narrower carrier gap without changing that reducer or any current `PolicyDecision` or `EvidenceBundle` schema.

## Directory Rules basis

ADR-0029 adopts Directory Rules v2. This slice uses existing responsibility roots:

| Responsibility | Path family |
|---|---|
| Semantic meaning | `contracts/policy/` |
| Machine shape | `schemas/contracts/v1/policy/` |
| Synthetic examples | `fixtures/contracts/v1/policy/` |
| Executable validation | `tools/validators/policy/` |
| Behavior proof | `tests/validators/` |
| Hosted orchestration | `.github/workflows/` |
| AI-authoring accountability | `data/receipts/generated/` |

No root, policy-rule home, source registry, evidence store, release home, proof home, or publication surface is created.

## Object meaning

A `PolicyObligationSet` binds:

1. a candidate `subject_ref`;
2. one or more unresolved `policy_decision_refs`;
3. a canonical ordered list of obligations;
4. kind-specific parameters;
5. stable reason codes and basis references;
6. RFC 8785 JCS plus SHA-256 deterministic identity;
7. explicit non-authority flags.

References are carried, not resolved or authenticated, by this profile.

## Obligation kinds

| Kind | Required parameter | Intended downstream duty |
|---|---|---|
| `ATTRIBUTION_REQUIRED` | `attribution_ref` | Preserve the cited attribution statement or record. |
| `SHARE_ALIKE_REQUIRED` | `share_alike_license` | Apply the declared compatible share-alike license to a derivative. |
| `RETENTION_LIMIT` | `retention_days` | Do not retain the governed material beyond the declared period. |
| `AGGREGATION_ONLY` | `minimum_aggregation_count` | Use or expose only aggregates meeting the minimum group size. |
| `NO_REDISTRIBUTION` | none | Do not redistribute the governed material. |
| `EMBARGO` | `embargo_until` | Hold the governed operation until the declared date. |
| `NOTICE_REQUIRED` | `notice_ref` | Surface the referenced notice when the operation occurs. |
| `CONSENT_REQUIRED` | `consent_ref` | Require a separately governed consent record before the operation. |

Every non-applicable parameter is `null`. This makes kind/parameter mismatches visible and prevents an open-ended prose bag.

## Canonical and semantic rules

A stored candidate is conformant only when:

- obligations are sorted by `obligation_id` and IDs are unique;
- each `applies_to` and `reason_codes` array is sorted and unique;
- `policy_decision_refs` exactly equals the sorted unique union of obligation references;
- each kind has exactly its required parameter and all other parameters are `null`;
- `NO_REDISTRIBUTION` applies to `REDISTRIBUTE`;
- the stored `spec_hash` equals the RFC 8785 JCS hash of all fields except `spec_hash` and `obligation_set_id`;
- `obligation_set_id` equals `kfm://policy/obligation-set/` plus the first 24 hexadecimal characters of that digest;
- all governance flags remain `false`.

The profile is deterministic, order-sensitive at storage time, side-effect free, and no-network.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, canonical ordering, kind/parameter coherence, identity, and non-authority checks succeeded. |
| `FAIL` | The candidate was readable and schema-valid but a semantic invariant failed. |
| `ERROR` | The candidate or schema could not be evaluated safely, including closed-schema failure. |

These are validator outcomes, not policy or release decisions.

## Compatibility and future binding

This additive profile does not change existing `PolicyDecision`, `PolicyInputBundle`, `PolicyObligationReduction`, `EvidenceBundle`, runtime envelope, release, or receipt schemas. A later reviewed slice may:

- bind `PolicyObligationSet` into a shared EvidenceBundle extension point;
- authenticate `policy_decision_refs`;
- map a subset of obligations into `PolicyObligationReduction`;
- add enforcement and `TransformReceipt` or consumption-receipt evidence;
- add the consent-card UI from `KFM-P7-FEAT-0002`.

Those steps must not be inferred from this fixture profile.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_policy_obligation_set.py' \
  --verbose

python tools/validators/policy/validate_policy_obligation_set.py --fixtures
```

## Rollback

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the additive commits. Because the object is inactive and fixture-only, rollback requires no policy-bundle change, evidence migration, release withdrawal, cache invalidation, or public correction.

## Open verification

- Which accepted policy vocabulary issues each obligation kind?
- Which shared EvidenceBundle extension point should carry `obligation_set_ref`?
- Which obligations require public notice versus steward-only visibility?
- Which enforcement component emits proof of compliance or violation?
- Which reviewer classes may approve consent, embargo, or redistribution obligations?
