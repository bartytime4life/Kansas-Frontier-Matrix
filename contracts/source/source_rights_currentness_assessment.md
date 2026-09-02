<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-rights-currentness-assessment
title: SourceRightsCurrentnessAssessment Contract
type: semantic-contract; source governance; fixture-only assessment
version: v0.1.0
status: proposed; inactive; fixture-only; no-network; non-activating
owners: OWNER_TBD — Source steward · Rights reviewer · Policy steward · Contracts steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; source; rights; currentness; review-required
related:
  - ./source_descriptor.md
  - ../../schemas/contracts/v1/source/source_rights_currentness_assessment.schema.json
[/KFM_META_BLOCK_V2] -->

# SourceRightsCurrentnessAssessment

A `SourceRightsCurrentnessAssessment` is a dated, deterministic review record that evaluates whether the publisher, product, official locator, terms, rights, attribution, redistribution, derivative-use, access, and cadence posture attached to a source are sufficiently resolved and current for later steward decisions.

It complements `SourceDescriptor` and `SourceActivationDecision`; it does not replace either object. A `PASS` means only that the fixture declaration is internally coherent and the stated review posture is current. It does not activate a source, fetch bytes, admit RAW data, approve rights, authorize a connector, or permit release or publication.

## Finite assessment states

| State | Meaning | Validator outcome |
|---|---|---|
| `CURRENT` | Required identity, terms, and rights checks are resolved and the next review is in the future. | `PASS` |
| `REVIEW_DUE` | Prior checks are coherent but the review window has expired. | `ABSTAIN` |
| `BLOCKED` | Identity, terms, rights, redistribution, derivative use, or access remains unresolved or denied. | `DENY` |
| `ERROR` | The assessment explicitly records an evaluation failure. | `ERROR` |

Known restrictions may still be `CURRENT`; currentness is not permission. Downstream source admission, activation, evidence use, release, and publication must independently enforce the recorded restrictions.

## Invariants

- `source_descriptor_ref` binds exactly to `source_id`.
- `descriptor_spec_hash` pins the reviewed descriptor version.
- unknown, denied, or permission-dependent rights fail closed.
- unknown or denied redistribution and derivative-use posture fail closed.
- unresolved publisher, product, terms, or access posture fails closed.
- the review window is evaluated against `assessed_at` without contacting a source.
- `assessment_id` and `spec_hash` are derived with repository RFC 8785 JCS plus SHA-256.
- all network, activation, fetch, RAW-write, promotion, release, and publication effects remain false.

## Directory Rules basis

Semantic meaning belongs in `contracts/source/`; machine shape in `schemas/contracts/v1/source/`; synthetic review records in `fixtures/contracts/v1/source/`; validation in `tools/validators/source/`; tests in `tests/validators/`; read-only CI in `.github/workflows/`; source adaptation notes in `docs/intake/exploratory/`; and generated authoring provenance in `data/receipts/generated/`.

## Validation

```bash
python -m unittest tests.validators.test_validate_source_rights_currentness_assessment -v
python tools/validators/source/validate_source_rights_currentness_assessment.py --fixtures
```

## Rollback

Revert the additive fixture-only packet. No source, connector, registry record, lifecycle object, release, deployment, or public artifact is changed by this profile.
