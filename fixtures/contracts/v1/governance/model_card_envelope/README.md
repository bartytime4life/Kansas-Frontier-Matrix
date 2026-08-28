<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-model-card-envelope
title: ModelCardEnvelope fixture family
type: fixture-readme
version: v1.0.0
status: PROPOSED; synthetic; no-network
owners:
  - OWNER_TBD validation steward
  - OWNER_TBD model-governance steward
created: 2026-08-07
updated: 2026-08-07
policy_label: public; synthetic; governance; model-card; no real model data
owning_root: fixtures/
responsibility: Provide deterministic positive, hold, deny, and negative examples for ModelCardEnvelope validation.
truth_posture: CONFIRMED synthetic bytes and expected outcomes; PROPOSED profile; UNKNOWN production applicability.
related:
  - ../../../../../contracts/governance/model_card_envelope.md
  - ../../../../../schemas/contracts/v1/governance/model_card_envelope.schema.json
  - ../../../../../tools/validators/governance/model_card_envelope_core.py
  - ../../../../../tools/validators/governance/validate_model_card_envelope.py
  - ../../../../../tests/validators/governance/test_validate_model_card_envelope.py
[/KFM_META_BLOCK_V2] -->

# `ModelCardEnvelope` fixtures

`base.json` plus one JSON file per case under `cases/` form one deterministic, synthetic fixture packet. Names inspired by the source packet are used only to exercise model-kind boundaries. They do not prove that a model, dataset, evaluation, review, signature, attestation, or release exists.

## Finite valid states

| Case ID | Expected outcome | Boundary exercised |
|---|---|---|
| `pass-climate-reconstruction` | `PASS` | Released environmental reconstruction with citations, review, rights, correction, rollback, and forecast/alert prohibitions. |
| `hold-focus-mode-narrative` | `HOLD` | Governed narrative candidate awaiting human and sovereignty review. |
| `deny-sensitive-alignment` | `DENY` | Sensitive spatial alignment withdrawn because rights and sovereignty review are incomplete. |

## Negative states

| Case ID | Expected finding |
|---|---|
| `invalid-allow-without-review` | `ALLOW_REVIEW_INCOMPLETE` |
| `invalid-authority-overclaim` | `SCHEMA_INVALID` |
| `invalid-environmental-use-boundary` | `ENVIRONMENTAL_USE_BOUNDARY_MISSING` |
| `invalid-identity-mismatch` | `DOC_UUID_MISMATCH` |
| `invalid-narrative-missing-citation-control` | `NARRATIVE_CITATION_CONTROL_MISSING` |
| `invalid-released-without-rollback` | `RELEASE_ROLLBACK_REQUIRED` |
| `invalid-reference-role-mismatch` | `BINDING_ROLE_MISMATCH` |
| `invalid-spec-hash-mismatch` | `SPEC_HASH_MISMATCH` |
| `invalid-transform-overlap` | `TRANSFORM_PERMISSION_CONFLICT` |
| `invalid-unsafe-reference` | `REF_PATH_ESCAPE` |

The fixture-suite validator requires sorted unique case IDs, an exact `<case_id>.json` filename for every case, exact expected outcomes, and exact expected finding lists. Adding, removing, or changing a case without reviewing its expectation fails the replay.

## Replay

```bash
python tools/validators/governance/validate_model_card_envelope.py --fixtures
```

The replay makes no network request and creates no lifecycle, evidence, review, release, or publication state.
