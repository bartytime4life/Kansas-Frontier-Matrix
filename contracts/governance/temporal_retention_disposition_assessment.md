<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/temporal-retention-disposition-assessment
title: Temporal Retention Disposition Assessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed; inactive; fixture-only; review-required
owners: OWNER_TBD — Governance steward · Temporal steward · Evidence steward · Privacy steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
policy_label: internal; governance; temporal; retention; archival; compaction; erasure
owning_root: contracts/
responsibility: Define a bounded review assessment that keeps retention, archival, compaction, and erasure distinct without deleting history, deciding policy, or executing a disposition.
truth_posture: CONFIRMED source-card and repository-gap evidence / PROPOSED inactive assessment / NEEDS VERIFICATION human review and hosted exact-head CI
related:
  - ../evidence/after_image_reconstruction_record.md
  - ../correction/correction_propagation_plan.md
  - ./temporal_query_disclosure.md
  - ../../schemas/contracts/v1/governance/temporal_retention_disposition_assessment.schema.json
  - ../../fixtures/contracts/v1/governance/temporal_retention_disposition_assessment/cases.json
  - ../../tools/validators/governance/validate_temporal_retention_disposition_assessment.py
  - ../../tests/validators/governance/test_temporal_retention_disposition_assessment.py
  - ../../docs/intake/exploratory/pass-18-temporal-retention-disposition-assessment-source-map.md
tags: [kfm, governance, temporal, retention, archive, compaction, erasure, fixture-only]
notes:
  - "Implements the smallest inactive slice of Pass 18 card KFM-P18-INV-439."
  - "PASS means locally coherent and ready for human review; it never authorizes storage maintenance, erasure, policy change, release, or publication."
[/KFM_META_BLOCK_V2] -->

# Temporal Retention Disposition Assessment Candidate

> A deterministic, fixture-only assessment for a proposed temporal-record disposition. It prevents storage maintenance from silently becoming evidence deletion and keeps privacy or erasure obligations visible without granting authority to act.

## Purpose

Temporal records may need to remain active, move to an archive, be compacted into a lossless or digest-preserving form, or be erased under separately established authority. Those operations do not have the same evidentiary, correction, release, privacy, or rollback consequences.

This profile records one proposed `RETAIN`, `ARCHIVE`, `COMPACT`, or `ERASE` disposition and checks whether its declared controls are internally coherent. It does not establish a retention schedule, interpret law, resolve a right-to-erasure request, inspect database rows, run `VACUUM`, mutate lifecycle state, or delete any artifact.

## Preserved distinctions

| Concern | Required separation |
|---|---|
| Retention | Keeping the active temporal record and its full history. |
| Archival | Moving a complete history to a separately referenced archive while keeping it reconstructable and reversible. |
| Compaction | Reducing active record count only when archived support, a disposition receipt, proof preservation, and rollback remain explicit. |
| Erasure | A separately authorized privacy/legal process that this profile can only hold for review. |
| Evidence | Evidence dependencies are declared independently from retention policy and cannot be destroyed by a local `PASS`. |
| Correction and release | Correction history and released dependents remain visible before any disposition is considered. |

## Finite outcomes

| Outcome | Meaning | Non-effect |
|---|---|---|
| `PASS` | A synthetic `RETAIN`, `ARCHIVE`, or `COMPACT` proposal is locally coherent and ready for human review. | No disposition is authorized or executed. |
| `ABSTAIN` | Policy, legal basis, dependency closure, active-release handling, or erasure authority remains unresolved. | No default or inferred disposition is selected. |
| `DENY` | The proposal would silently delete history, erase without an obligation, contradict policy, break references, or claim destructive authority. | No partial disposition is accepted. |
| `ERROR` | The bounded assessment could not be completed safely. | No candidate state is trusted. |

Even a verified erasure obligation returns `ABSTAIN`: the handoff requires separate policy, privacy/legal, evidence, correction, release, and execution authority.

## Invariants

1. `RETAIN` preserves the full record count and history.
2. `ARCHIVE` preserves the full record count, full proof, archive reference, disposition receipt, reversibility, and rollback target.
3. `COMPACT` reduces record count only with preserved history, an archive, a disposition receipt, at least digest-level proof, reversibility, and rollback.
4. `ERASE` never passes locally. Missing or unresolved erasure authority fails closed, and active released dependents deny erasure.
5. Evidence, correction, and release reference sets must agree with their declared dependency states.
6. Policy and legal-basis references must agree with their declared states.
7. Every mutation, deletion, policy, erasure, evidence, correction, release, lifecycle-write, and publication authority flag is fixed to `false`.

## Deterministic identity

The validator computes RFC 8785 JCS plus SHA-256 over the complete candidate except `assessment_id` and `spec_hash`:

```text
spec_hash     = SHA-256(JCS(identity subject))
assessment_id = "kfm:temporal-retention:" + first_24_hex(spec_hash)
```

The identity binds the proposed disposition, dependency states, controls, decision, limitations, and all-false authority surface. It is not a policy decision, receipt, proof, or execution token.

## Composition boundary

- `AfterImageReconstructionRecord` remains the reference-only reconstruction-support object.
- `CorrectionPropagationPlan` remains the dependency inventory for correction, withdrawal, and rollback propagation.
- Existing release, rollback, evidence, consent, and policy objects retain their own authority.

This profile composes those concerns by reference and creates no retention-policy registry, legal rule, privacy decision, archive writer, database maintenance job, evidence store, or deletion service.

## Directory Rules basis

Governance assessment meaning belongs under `contracts/governance/`; machine shape under `schemas/contracts/v1/governance/`; synthetic cases under `fixtures/contracts/v1/governance/`; deterministic validation under `tools/validators/governance/`; executable conformance evidence under `tests/validators/governance/`; hosted orchestration under `.github/workflows/`; source adaptation under `docs/intake/exploratory/`; and authoring accountability under `data/receipts/generated/`.

Accepted ADR-0029 and the adopted Directory Rules were consulted. No new root or parallel retention, evidence, correction, policy, receipt, release, or publication authority is created.

## Validation

```bash
python -m unittest -v tests.validators.governance.test_temporal_retention_disposition_assessment
python tools/validators/governance/validate_temporal_retention_disposition_assessment.py --fixtures
```

## Rollback

Before merge, close the draft pull request and remove its branch. After an authorized merge, revert this additive contract/schema/fixture/validator/test/workflow/source-map/receipt packet. It has no runtime consumer and changes no database, archive, evidence record, correction, consent state, release, cache, deployment, or public surface.
