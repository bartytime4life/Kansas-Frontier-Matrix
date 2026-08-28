<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/identifier-precision-lineage-assessment
title: IdentifierPrecisionLineageAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Data steward · Geoprivacy steward · Evidence steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; identifier-lineage; precision-lineage; fixture-only
owning_root: contracts/
responsibility: deterministic declaration of identifier assertions, crosswalk outcomes, and effective spatial precision without resolving identity, disclosing raw identifiers or coordinates, or granting policy, review, release, publication, or public-use authority
truth_posture: CONFIRMED synthetic fixture behavior / PROPOSED semantic contract pending steward review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../source/source_descriptor.md
  - ../runtime/precision_actually_used.md
  - ../../schemas/contracts/v1/common/identifier_precision_lineage_assessment.schema.json
  - ../../fixtures/contracts/v1/common/identifier_precision_lineage_assessment/cases.json
  - ../../tools/validators/validate_identifier_precision_lineage_assessment.py
  - ../../tests/validators/test_validate_identifier_precision_lineage_assessment.py
  - ../../docs/intake/exploratory/identifier-precision-lineage-assessment-source-map.md
tags: [kfm, identifier, crosswalk, precision, lineage, geoprivacy, fixture]
notes:
  - "Adapts Full Atlas KFM-TRIAD-034 / KFM-CAND-0100..0102 as one bounded declaration profile."
  - "A coherent declaration cannot establish identity, transform geometry, or authorize public use."
[/KFM_META_BLOCK_V2] -->

# IdentifierPrecisionLineageAssessment Candidate Contract

`IdentifierPrecisionLineageAssessmentCandidate` records a bounded set of identifier assertions, one declared crosswalk outcome, and the spatial precision actually retained after a declared transform. Identifier values are represented only by SHA-256 digests; the candidate contains no raw identifier or coordinate payload.

## Source-derived gap

Full Atlas triad `KFM-TRIAD-034` proposes time-aware identifier assertions, explicit crosswalk decisions, effective-precision disclosure, and transform receipts. Domain-specific identity and geoprivacy artifacts exist, but the reviewed base has no reusable cross-cutting declaration that binds those three concerns while preserving their separate authorities.

This profile intentionally narrows the proposed object family. It does not create an identity registry, geometry transform, redaction policy, or public derivative.

## Authority boundary

The candidate validates declarations only. It does not fetch a source, inspect an identifier value, resolve a person, place, feature, or taxon, compare coordinates, run a transform, authenticate evidence, approve a crosswalk, or determine public safety.

`MATCHED` means only that the fixture declares a reviewed relationship under the referenced method. `RESOLVED` is a replay result for the declaration, not canonical identity authority. `HOLD` and `ABSTAIN` remain explicit finite outcomes.

## Deterministic invariants

- Identifier assertions are sorted and unique by `assertion_id`; namespace-plus-digest pairs cannot repeat.
- At least one source-native assertion is retained; value fields are digest-only.
- Crosswalk endpoints name distinct assertions in the same candidate.
- A `MATCHED` crosswalk requires evidence, a reviewed state, and an active `RESOLVED` target.
- An `AMBIGUOUS` or `UNRESOLVED` crosswalk cannot produce a resolved outcome.
- Supersession references remain internal, cannot self-reference, and cannot form a cycle.
- `NONE` preserves source precision exactly and carries no transform references.
- `GENERALIZED` and `AGGREGATED` cannot claim finer precision and require profile and receipt references.
- `WITHHELD` carries no effective precision and requires profile and receipt references.
- Summary counts and finite outcome reproduce the declared rows.
- Identity resolution, policy, review, release, publication, and public use remain unauthorized.

`spec_hash` is RFC 8785 JCS plus SHA-256 over the object excluding only `assessment_id` and `spec_hash`. The assessment ID is derived from the first 24 digest characters through the repository hashing package.

## Validator status

`PASS` means a coherent `RESOLVED` synthetic declaration. `ABSTAIN` means a coherent `HOLD` or `ABSTAIN` declaration. `DENY` identifies a declaration defect; `ERROR` identifies unsafe input. None of these statuses authenticates a real identifier, geometry, source, evidence item, or reviewer.

## Directory Rules basis

The responsibility is shared identifier and precision semantics, so meaning belongs in `contracts/common/`; machine shape in `schemas/contracts/v1/common/`; synthetic cases in `fixtures/contracts/v1/common/`; executable validation in `tools/validators/`; tests in `tests/validators/`; read-only orchestration in `.github/workflows/`; source adaptation in `docs/intake/exploratory/`; and authoring accountability in `data/receipts/generated/`.

No parallel identity, evidence, geoprivacy, policy, review, release, or publication authority is created.

## Rollback

Before merge, close the draft PR and retire its branch. After an authorized merge, revert the additive packet. It has no runtime consumer or source action, so no identity correction, geometry withdrawal, release rollback, or public correction is required.
