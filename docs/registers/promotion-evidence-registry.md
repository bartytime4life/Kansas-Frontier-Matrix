# Promotion Evidence Registry

## KFM Meta Block V2
- status: PROPOSED
- owners: <TODO>
- policy_label: kfm.promotion.governed.v1

## Purpose
Defines a local, deterministic evidence carrier for governed promotion replay.

## Lifecycle placement
Candidate -> Decision -> Registration -> Publish -> Replay Verification.

## Evidence chain diagram
artifact payload -> spec_hash -> decision_log -> run_receipt -> steward_attestation -> signing -> gatehouse_registration -> publish_manifest.

## Artifact separation
RAW/WORK/QUARANTINE remain non-public; registry tracks only release-safe paths.

## Fail-closed matrix
Missing/invalid spec_hash, decision_log, run_receipt, steward approval, signing, registration, or ordering => fail/deny.

## CLI examples
`python tools/validators/governance/validate_promotion_registry.py tests/fixtures/governance/promotion/valid/minimal_registry.json`
`python tools/governance/replay_promotion.py tests/fixtures/governance/promotion/valid/replay_request_minimal.json`

## Fixture inventory
See `tests/fixtures/governance/promotion/{valid,invalid}`.

## Replay semantics
VERIFIED: complete + matching.
DENY: policy-blocking evidence.
ABSTAIN: incomplete but parseable evidence.
ERROR: malformed/unreadable input.

## Definition of done
Schemas + fixtures + validator + replay + policy + tests + workflow integrated.

## Rollback/correction notes
Obligations must include rollback/correction references before allow.
