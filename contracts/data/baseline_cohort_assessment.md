<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/baseline-cohort-assessment
title: BaselineCohortAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Data steward · Domain steward · Evidence steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; baseline; cohort; discontinuity; fixture-only
owning_root: contracts/
responsibility: deterministic declaration of a versioned baseline window, cohort eligibility, exclusions, holds, and discontinuities without calculating a baseline, evaluating anomalies, mutating data, or granting policy, review, release, publication, or public-use authority
truth_posture: CONFIRMED synthetic fixture behavior / PROPOSED semantic contract pending steward review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../source/source_descriptor.md
  - ../evidence/observation_fitness_assessment.md
  - ../evidence/evidence_ref.md
  - ../../schemas/contracts/v1/data/baseline_cohort_assessment.schema.json
  - ../../fixtures/contracts/v1/data/baseline_cohort_assessment/cases.json
  - ../../tools/validators/data/validate_baseline_cohort_assessment.py
  - ../../tests/validators/test_validate_baseline_cohort_assessment.py
  - ../../docs/intake/exploratory/baseline-cohort-assessment-source-map.md
tags: [kfm, baseline, cohort, drift, discontinuity, provenance, fixture]
notes:
  - "Adapts Full Atlas KFM-TRIAD-036 / KFM-CAND-0106..0108 as one bounded assessment profile."
  - "A coherent cohort declaration cannot calculate, rebuild, approve, publish, or apply a baseline."
[/KFM_META_BLOCK_V2] -->

# BaselineCohortAssessment Candidate Contract

`BaselineCohortAssessmentCandidate` records the exact time window, method profile, candidate observations, eligibility dispositions, and discontinuities declared for one synthetic baseline cohort. It makes exclusions and holds replayable without calculating a statistic or anomaly.

## Source-derived gap

Full Atlas triad `KFM-TRIAD-036` proposes versioned baseline manifests, inspectable cohort eligibility, discontinuity records, validation reports, and rebuild receipts. The reviewed base uses baseline vocabulary in domain fixtures, but it has no reusable data-lifecycle candidate that binds cohort membership, method continuity, relocation handling, and correction-aware timestamps.

This profile intentionally narrows the proposed family. It references a method profile and prior baseline but does not create a baseline value, anomaly threshold, validation approval, or rebuild receipt.

## Authority boundary

The validator checks declarations only. It does not fetch an observation, inspect a measured value, calculate a baseline, infer drift, decide materiality, rebuild an artifact, alter a source record, evaluate policy, or authorize use of a baseline.

`COMPLETE` means only that the declared cohort has at least one included member and no unresolved holds. `HOLD` and `ABSTAIN` are finite non-success outcomes. Excluded members remain in the declaration so their absence is inspectable.

## Deterministic invariants

- Baseline valid time is a nonempty interval; its recorded time is not earlier than the interval end.
- Candidate rows are sorted and unique by `member_id`.
- Observation time cannot be later than record time.
- Included members fall inside the baseline window, match its method profile, have complete support, and carry evidence.
- Excluded and held members carry a compatible finite reason code.
- Discontinuity rows are sorted, bind to one candidate, carry evidence, and agree with that candidate's disposition.
- A relocation, method change, instrument change, gap, or correction cannot be silently included.
- Summary counts, outcome, and rebuild signal reproduce candidate and discontinuity rows.
- The candidate contains references and digests only; no observation values or baseline statistics are present.
- Policy, review, release, publication, and public use remain unauthorized.

`spec_hash` is RFC 8785 JCS plus SHA-256 over the object excluding only `assessment_id` and `spec_hash`. The assessment ID is derived from the first 24 digest characters through the repository hashing package.

## Validator status

`PASS` means a coherent synthetic `COMPLETE` cohort declaration. `ABSTAIN` means a coherent `HOLD` or `ABSTAIN` declaration. `DENY` identifies a declaration defect; `ERROR` identifies unsafe input. None authenticates source data, calculates a baseline, or approves downstream use.

## Directory Rules basis

The primary responsibility is baseline input lifecycle and provenance, so meaning belongs in `contracts/data/`; machine shape in `schemas/contracts/v1/data/`; synthetic cases in `fixtures/contracts/v1/data/`; executable validation in `tools/validators/data/`; tests in `tests/validators/`; read-only orchestration in `.github/workflows/`; source adaptation in `docs/intake/exploratory/`; and authoring accountability in `data/receipts/generated/`.

No parallel source, evidence, statistical, policy, review, release, or publication authority is created.

## Rollback

Before merge, close the draft PR and retire its branch. After an authorized merge, revert the additive packet. It has no runtime consumer or source action, so no baseline rebuild, data correction, release rollback, or public correction is required.
