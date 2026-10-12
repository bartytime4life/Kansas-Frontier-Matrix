<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/drone-capture-authorization-metadata
title: DroneCaptureAuthorizationMetadata Candidate Contract
type: semantic-contract
version: v0.1.0
status: proposed; inactive; fixture-only; review-required
owners: OWNER_TBD — Evidence steward · Field-capture steward · Safety policy steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
policy_label: internal; evidence; field-capture; drone; authorization-metadata; no-network
owning_root: contracts/
responsibility: Define fixture-only metadata coherence for the authorization reference used by drone field-capture handoff without granting legal, operational, evidence, policy, review, release, or publication authority.
truth_posture: CONFIRMED source-card, connected-source, and repository-gap evidence / PROPOSED inactive profile / NEEDS VERIFICATION current authority sources, steward adoption, and hosted exact-head execution
related:
  - ./field_capture_evidence_handoff.md
  - ../source/source_descriptor.md
  - ../../schemas/contracts/v1/evidence/drone_capture_authorization_metadata.schema.json
  - ../../fixtures/contracts/v1/evidence/drone_capture_authorization_metadata/cases.json
  - ../../tools/validators/evidence/validate_drone_capture_authorization_metadata.py
  - ../../tests/validators/evidence/test_validate_drone_capture_authorization_metadata.py
  - ../../docs/intake/exploratory/pass-18-drone-capture-authorization-metadata-source-map.md
[/KFM_META_BLOCK_V2] -->

# DroneCaptureAuthorizationMetadata Candidate

`DroneCaptureAuthorizationMetadata` is an inactive, fixture-only record for the
opaque `capture_authorization_ref` already required by
`FieldCaptureEvidenceHandoffAssessment` when `capture_kind=DRONE_CAPTURE`.
It implements the bounded metadata seam proposed by Pass 18 card
`KFM-P18-INV-466` without changing the existing handoff contract.

## Recorded dimensions

The candidate binds synthetic references and bounded values for:

- capture, source-descriptor, run-receipt, handoff-assessment, and aircraft
  model references;
- capture and declared authorization time windows;
- authorization-evidence, authority-source, parameter, and hashed identifier
  references;
- operating-area digest and `EXACT_RESTRICTED`, `GENERALIZED`, or `WITHHELD`
  geometry posture, never coordinates;
- declared altitude reference, ceiling, observed maximum, and basis;
- airspace-review result and constraint references; and
- safety constraint codes, plan, acknowledgement, rights, policy, evidence,
  and review references.

The source material is historical and regulations can change. This profile
therefore checks only local metadata coherence relative to a declared capture
window. It does not determine whether authorization was legally required,
authentic, sufficient, current now, or operationally valid.

## Finite result

| Outcome | Meaning |
|---|---|
| `PASS` | The synthetic metadata is internally coherent for evidence-handoff review. |
| `ABSTAIN` | Authorization evidence, area match, altitude, airspace, safety, rights, policy, evidence, or review information is unresolved. |
| `DENY` | Shape, identity, temporal, altitude, geometry, conflict, review, or no-authority declarations conflict. |
| `ERROR` | The record declares an error or bounded file handling cannot proceed safely. |

A `PASS` is not permission to fly and does not authenticate an authorization.

## Deterministic identity

The validator hashes canonical JSON after removing only `spec_hash` and
`metadata_id`. The ID is `kfm:drone-authorization-metadata:` plus the first 24
digest hex characters. Safety constraint codes are unique and lexicographically
ordered. Authorization identifiers are represented only by SHA-256 digest.

## Trust boundary, Directory Rules, and rollback

Validation performs no network request, identity lookup, geometry resolution,
airspace query, legal analysis, flight planning, evidence creation, policy or
review decision, lifecycle transition, release, deployment, or publication.
All authority claims are fixed to `false`.

Accepted ADR-0029 keeps this capture-metadata meaning in the existing evidence
family, with shape, fixtures, reusable validation, tests, workflow, source map,
and generated receipt in their paired roots. Rollback is one additive
feature-commit revert; no external or operational state is mutated.
