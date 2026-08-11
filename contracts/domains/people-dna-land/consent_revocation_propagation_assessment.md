<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/people-dna-land/consent-revocation-propagation-assessment
title: Consent Revocation Propagation Assessment Contract
type: semantic-contract; consent-scope; revocation-propagation; fixture-first
version: v0.1.0
status: proposed; inactive; synthetic-fixture-only; no-consent-or-release-authority
owners: OWNER_TBD - Consent steward; Privacy steward; People/DNA/Land steward; Contracts steward; Validation steward
created: 2026-08-11
updated: 2026-08-11
policy_label: restricted-review; consent; revocation; fail-closed; non-authoritative
owning_root: contracts/
responsibility: Define a bounded assessment of current consent scope and withdrawal propagation across consequential derived surfaces without creating consent, identity, evidence, policy, release, deletion, or publication authority.
related:
  - ./consented_genealogy_overlay.md
  - ../../../docs/domains/people-dna-land/CONSENT_MODEL.md
  - ../../../docs/runbooks/people-dna-land/CONSENT_RUNBOOK.md
  - ../../../schemas/contracts/v1/domains/people-dna-land/consent_revocation_propagation_assessment.schema.json
  - ../../../fixtures/domains/people-dna-land/consent_revocation_propagation/
  - ../../../tools/validators/domains/people-dna-land/validate_consent_revocation_propagation_assessment.py
  - ../../../tests/domains/people-dna-land/consent/revocation/test_consent_revocation_propagation_assessment.py
  - ../../../docs/intake/exploratory/full-atlas-consent-revocation-propagation-source-map.md
tags: [kfm, consent, revocation, propagation, dependency-index, cache-invalidation, privacy, fixture-first]
notes:
  - "Implements the bounded programming seam in Full Atlas KFM-TRIAD-038."
  - "SATISFIED means only that the declared consent dimension is current and in scope; every independent evidence, rights, sensitivity, policy, review, release, and publication gate remains unresolved."
[/KFM_META_BLOCK_V2] -->

# Consent Revocation Propagation Assessment

`ConsentRevocationPropagationAssessment` is an inactive, synthetic-fixture profile for checking two questions:

1. Is the referenced consent grant currently active and within its declared purpose, operation, fields, relationships, audience, retention, and time scope?
2. If consent is revoked or expired, are the next consequential reads, answers, exports, tiles, graphs, indexes, and caches blocked, invalidated, or purged with receipt references?

The assessment does not issue consent, authenticate a subject or representative, execute deletion, prove cleanup, resolve evidence, clear rights or sensitivity, evaluate policy, approve review, release data, or publish.

## Directory Rules basis

| Responsibility | Home | Role in this slice |
|---|---|---|
| Domain object meaning | `contracts/domains/people-dna-land/` | This semantic contract. |
| Machine shape | `schemas/contracts/v1/domains/people-dna-land/` | Closed Draft 2020-12 fixture shape. |
| Synthetic cases | `fixtures/domains/people-dna-land/` | No real people, DNA, consent credentials, or locations. |
| Validation | `tools/validators/domains/people-dna-land/` | Deterministic no-network local checks. |
| Proof of behavior | `tests/domains/people-dna-land/` | Exact finite outcome and negative-path tests. |
| Policy, consent records, receipts, release | Their existing owning roots | Referenced only; never created here. |

No new root, consent authority, policy authority, receipt store, cleanup executor, or release lane is created.

## Assessment boundary

The object binds one declared consent status observation to one exact seven-surface dependency inventory:

| Surface | Consequential effect represented |
|---|---|
| `READ` | A protected derived record can be read. |
| `ANSWER` | A governed answer can use the protected derivative. |
| `EXPORT` | A derivative can leave the governed context. |
| `TILE` | A map artifact or tile projection can expose the derivative. |
| `GRAPH` | A graph projection can retain or reveal the relationship. |
| `INDEX` | A search/vector/lookup index can retain the derivative. |
| `CACHE` | A cache can continue serving a stale authorization state. |

The inventory is deliberately closed and ordered so omission cannot masquerade as successful propagation.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `SATISFIED` | The declared consent status is active, unexpired, and all seven scope dimensions match. This passes only the consent dimension to independent gates. |
| `DENY` | Consent is revoked, expired, or out of scope. Consequential surfaces must fail closed. |
| `ABSTAIN` | Current consent status cannot be established. Consequential surfaces remain blocked or pending review. |
| `ERROR` | Status evaluation failed. Consequential surfaces remain blocked or pending review. |

## Required propagation behavior

- `ACTIVE` plus a complete scope match requires `SATISFIED`; all seven dependencies are `READY` with action `NONE`.
- `ACTIVE` plus any scope mismatch requires `DENY`; every dependency is `BLOCKED` with `DENY_NEXT_USE` and an action receipt reference.
- `REVOKED` or `EXPIRED` requires `DENY`.
  - `READ`, `ANSWER`, and `EXPORT` are `BLOCKED` with `DENY_NEXT_USE`.
  - `TILE`, `GRAPH`, `INDEX`, and `CACHE` are `INVALIDATED` or `PURGED` with the matching action.
  - every action is receipt-bound.
- `UNKNOWN` requires `ABSTAIN`; `ERROR` requires `ERROR`; both keep every dependency `BLOCKED` or `PENDING`.
- A revocation receipt is mandatory for `REVOKED`.
- Status observation time cannot be after assessment time, and an active grant cannot be used after `valid_until`.

## Non-authority rule

Every fixture fixes these declarations:

- consent dimension only;
- no identity, kinship, evidence, rights, sensitivity, policy, review, release, or publication authority;
- no execution of deletion, withdrawal, cache invalidation, graph cleanup, index cleanup, or artifact removal;
- no real person, DNA, credential, consent token, location, or protected relationship data.

Receipt references are assertions supplied to the assessment. This validator does not resolve or authenticate them.

## Validation

```bash
python \
  tests/domains/people-dna-land/consent/revocation/test_consent_revocation_propagation_assessment.py \
  --verbose

python tools/validators/domains/people-dna-land/validate_consent_revocation_propagation_assessment.py \
  --fixtures
```

A green result proves only schema validity, deterministic fixture materialization, declared local consistency, exact finite outcomes, and fail-closed dependency coverage. It does not prove a production consent store, subject authority, cleanup execution, policy, release, or public safety.

## Rollback

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the feature commit. The slice creates no real consent record, cleanup job, lifecycle transition, cache mutation, graph mutation, index mutation, release, or publication to unwind.
