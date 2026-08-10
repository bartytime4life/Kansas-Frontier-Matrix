# `schemas/contracts/v1/validation/` — Validation Assurance Schemas

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-validation-readme
title: schemas/contracts/v1/validation/ README
type: readme; schema-family-index; validation-assurance; machine-shape
version: v0.1.0
status: draft; PROPOSED; fixture-first
updated: 2026-08-05
policy_label: public; schemas; contracts-v1; validation; assurance; non-authoritative
tags: [kfm, schemas, validation, mutation-testing, adversarial-assurance, qa]
related:
  - ../../../../contracts/validation/README.md
  - ../../../../contracts/validation/validator_assurance_report.md
  - ../../../../fixtures/contracts/v1/validation/validator_assurance_report/
  - ../../../../tools/validators/validate_validator_assurance_report.py
  - ../../../../tests/validators/test_validate_validator_assurance_report.py
notes:
  - "Introduces the bounded KFM-TRIAD-063 ValidatorAssuranceReport shape."
  - "This lane records assurance evidence; it does not run mutants, approve validators, define a universal score threshold, or authorize merge or release."
[/KFM_META_BLOCK_V2] -->

## Purpose

This lane owns machine-checkable shape for validation-assurance records: the exact target and profile, deterministic campaign identity, mutation-operator inventory, mutant arithmetic, survivor classifications, finite assurance outcome, provenance, and explicit non-authority fields.

It does not own validator execution, mutation engines, policy decisions, branch protection, human review, merge authorization, release, or publication.

## Current proposed schema

| Schema | Contract | Status | Scope |
|---|---|---|---|
| [`validator_assurance_report.schema.json`](./validator_assurance_report.schema.json) | [`ValidatorAssuranceReport`](../../../../contracts/validation/validator_assurance_report.md) | `PROPOSED` / fixture-first | Bounded adversarial/mutation assurance evidence with semantic survivor inventory and no universal threshold. |
| [`pipeline_replay_assessment.schema.json`](./pipeline_replay_assessment.schema.json) | [`PipelineReplayAssessmentCandidate`](../../../../contracts/validation/pipeline_replay_assessment.md) | `PROPOSED` / fixture-only | Exact comparison of pinned source, transform, model, validator, and output identities without pipeline execution. |

## Required separation

- A report is not proof that its referenced campaign actually ran; the real campaign runner, mutant manifest, logs, test outputs, and RunReceipt must support that claim.
- `PASS` is not validator approval, policy authority, merge permission, promotion, release, or public fitness.
- A high aggregate kill rate cannot hide a surviving fail-open or policy-bypass mutant.
- Equivalent and out-of-scope mutants must remain explicitly reviewed rather than silently omitted.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_validator_assurance_report.py' \
  --verbose

python tools/validators/validate_validator_assurance_report.py --fixtures
```

A green result proves only the proposed shape, exact fixture polarity, arithmetic, finite-outcome consistency, and authority separation.

## Rollback

Before merge, close the draft pull request and abandon its branch. After an authorized merge, revert the dependency-closed contract/schema/fixture/validator/test/workflow/receipt change. No existing validator, policy, branch setting, release, or published artifact is modified by this slice.
