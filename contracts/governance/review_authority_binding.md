<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/review-authority-binding
title: ReviewAuthorityBinding Contract
type: semantic-contract; fixture-first; non-authoritative
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD — governance steward · validation steward · release steward
created: 2026-08-06
updated: 2026-08-06
policy_label: internal; fixture-only; no-authority
related:
  - ./ReviewRecord.md
  - ./steward_assignment.md
  - ../../schemas/contracts/v1/governance/review_authority_binding.schema.json
  - ../../tools/validators/governance/validate_review_authority_binding.py
  - ../../fixtures/contracts/v1/governance/review_authority_binding/
  - ../../tests/validators/governance/test_review_authority_binding.py
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, governance, review, stewardship, authority-binding, fixture-only, no-write]
[/KFM_META_BLOCK_V2] -->

# ReviewAuthorityBinding

> A deterministic, fixture-only binding report that checks whether one exact `ReviewRecord`, one exact `StewardshipAssignment`, and one exact reviewed subject agree.

## Why this slice comes before an apply preflight

The merged query/save/recompile and conditional-write slices already bind a candidate, subject preimage, deterministic output, rollback identity, and optimistic condition. Their contracts explicitly do not authenticate policy or review authority. The repository also contained permissive review and stewardship schema stubs.

Creating a purported authenticated apply preflight over those stubs would overclaim. This slice first closes the machine-checkable review/assignment dependency while preserving the stronger boundary: structural binding is not actor authentication and is not write authority.

## Outcomes

| Outcome | Meaning |
|---|---|
| `BOUND` | The exact records validate; actor, role, subject, time window, active status, approved disposition, and declared separation of duties agree. |
| `HOLD` | The records are valid but the assignment is provisional or the review is conditional/non-approving. |
| `DENY` | A record is invalid, mismatched, outside the effective window, inactive, or fails separation of duties. |

`BOUND` is an input to a later apply-preflight design. It never emits a request or authorizes mutation.

## Binding checks

The validator independently recomputes:

- both source-object hashes and identifiers;
- reviewer actor and role agreement;
- exact subject reference and content identity;
- review time within the assignment interval;
- active versus provisional/inactive status;
- review disposition eligibility;
- author/reviewer separation where required;
- the binding report hash and identifier.

## Deterministic identity

```text
spec_hash = SHA-256(RFC8785-JCS(binding excluding binding_id and spec_hash))
binding_id = "kfm:review-authority-binding:" + hex(spec_hash)
```

## Non-effects

A valid binding does not authenticate an actor or platform account, resolve policy, emit a write request, apply a candidate, mutate repository or lifecycle state, merge, promote, release, deploy, publish, or authorize public use.

## Follow-up boundary

The next dependency-closed slice may add a no-write steward-apply preflight that consumes:

1. a valid `RecompileManifest`;
2. a valid conditional-write preflight;
3. a `BOUND` review-authority binding;
4. an independently resolved policy decision;
5. current subject identity and destination ownership; and
6. required future operational-receipt declarations.

That later slice must still stop before an actual write.

## Rollback

Close the draft pull request before merge or revert the implementation commit after merge. No external state or public product exists.
