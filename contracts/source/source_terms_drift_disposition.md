<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-terms-drift-disposition
title: Source Terms Drift Disposition
type: semantic-contract
version: v0.1.0
status: proposed; inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Source steward · Rights reviewer · Policy steward · Release steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; source; rights; terms-drift; review-required
owning_root: contracts/
responsibility: Define a deterministic comparison seam for evidence-backed source-terms snapshots and downstream review proposals.
truth_posture: PROPOSED source-grounded adaptation / CONFIRMED fixture validation only / no legal, lifecycle, release, or publication authority
related:
  - ./source_descriptor.md
  - ./source_rights_currentness_assessment.md
  - ../../schemas/contracts/v1/source/source_terms_drift_disposition.schema.json
  - ../../docs/intake/exploratory/source-terms-drift-disposition-source-map.md
tags: [kfm, source, terms, rights, drift, downstream-obligations, fixture-only]
[/KFM_META_BLOCK_V2] -->

# Source Terms Drift Disposition

A `SourceTermsDriftDisposition` compares two evidence-backed declarations of
the terms governing the same source scope. It makes changed duties and affected
downstream dependencies reviewable without treating access, a terms URL, a
license label, or validator success as legal or publication authority.

## Bounded responsibility

The profile binds:

- one versioned `SourceDescriptor`;
- prior and current terms snapshots, their captured content hashes, scope
  hashes, license identifiers, effective windows, use posture, and obligation
  references;
- a closed drift classification and exact changed-field list;
- downstream dependency references with proposed review actions; and
- a finite non-authoritative disposition.

The snapshots are declarations over synthetic fixtures. The validator neither
fetches nor republishes governing text and does not decide whether a real use is
lawful.

## Relationship to currentness

`SourceRightsCurrentnessAssessment` answers whether a dated descriptor review
is coherent and still within its review window. This contract has a different
responsibility: it compares two exact terms snapshots and demonstrates whether
changed or unresolved duties reached every declared downstream dependency.
Neither object activates a source or authorizes use.

## Finite states

| Drift class | Disposition | Meaning |
|---|---|---|
| `NO_CHANGE` | `NO_ACTION` | Verified snapshot content, scope, posture, and expiry are unchanged. |
| `NON_RESTRICTIVE_CHANGE` | `REASSESS` | A verified change exists but does not increase a declared restriction. Human rights review remains required. |
| `RESTRICTIVE_CHANGE` | `HOLD` | A declared duty becomes more restrictive or expires; affected products require review. |
| `UNRESOLVED` | `HOLD` | Evidence, verification, or scope is insufficient for comparison. |

`ERROR` is reserved for an explicitly recorded assessment error. Proposed
actions such as `WITHDRAWAL_REVIEW` and `RECOMPUTE_REVIEW` are routing
signals only; the contract cannot execute them.

## Fail-closed invariants

- Snapshot evidence must be verified, scoped, ordered, and time-coherent.
- `changed_fields` must equal the deterministic comparison of the two
  snapshots.
- Changed terms content or license identity requires reassessment even when no
  declared posture becomes more restrictive.
- Unknown, prohibited, more restrictive, expired, unverified, unavailable, or
  scope-mismatched current terms cannot return `NO_ACTION`.
- Every downstream dependency must be unique and lexically ordered.
- A changed or unresolved posture must be propagated to every dependency; a
  missing propagation returns `HOLD`.
- RFC 8785 JCS plus SHA-256 binds the assessment identity.
- All legal, activation, lifecycle-write, hold, recomputation, withdrawal,
  release, and publication effects remain false.

## Directory Rules basis

| Responsibility | Home |
|---|---|
| Source-terms comparison meaning | `contracts/source/` |
| Closed machine shape | `schemas/contracts/v1/source/` |
| Synthetic examples | `fixtures/contracts/v1/source/` |
| Deterministic enforcement | `tools/validators/source/` |
| Executable checks | `tests/validators/` |
| Source reconciliation | `docs/intake/exploratory/` |
| Read-only orchestration | `.github/workflows/` |
| AI authoring provenance | `data/receipts/generated/` |

This placement extends the existing source responsibility without creating a
parallel rights, policy, correction, release, or legal-decision root.

## Validation

```bash
python -m unittest -v tests.validators.test_validate_source_terms_drift_disposition
python tools/validators/source/validate_source_terms_drift_disposition.py --fixtures
```

## Non-effects and rollback

A green result does not authenticate source terms, approve a license, change
source admission, mutate a lifecycle object, place a real product on hold,
recompute or withdraw an artifact, or authorize release or publication.
Rollback is an ordinary revert of this additive fixture-only packet.
