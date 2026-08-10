<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/asynchronous-transfer-assessment
title: Asynchronous Transfer Assessment Candidate Contract
type: semantic-contract
version: v0.1.0
status: proposed; inactive; fixture-only; review-required
owners: OWNER_TBD — Source steward · Ingest steward · Contract steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public; source; transfer; provenance; no-network
owning_root: contracts/
responsibility: Define a bounded assessment that keeps provider job state, local transfer state, partial bytes, retry lineage, final artifact identity, and ingest eligibility separate without contacting a provider or writing RAW data.
truth_posture: CONFIRMED synthetic validator behavior / PROPOSED inactive transfer profile / NEEDS VERIFICATION steward adoption, provider adapters, and hosted exact-head execution
related:
  - ./source_descriptor.md
  - ./source_polling_checkpoint.md
  - ../../schemas/contracts/v1/source/asynchronous_transfer_assessment.schema.json
  - ../../fixtures/contracts/v1/source/asynchronous_transfer_assessment/cases.json
  - ../../tools/validators/source/validate_asynchronous_transfer_assessment.py
  - ../../tests/validators/test_validate_asynchronous_transfer_assessment.py
  - ../../docs/intake/exploratory/asynchronous-transfer-assessment-source-map.md
tags: [kfm, source, asynchronous-job, partial-transfer, resume, checksum, fixture-only]
notes:
  - "Implements the bounded KFM-TRIAD-050 and KFM-CAND-0148 through KFM-CAND-0150 gap from the Full Atlas."
  - "All provider identifiers, sizes, hashes, timestamps, and byte ranges in the fixtures are synthetic."
[/KFM_META_BLOCK_V2] -->

# Asynchronous Transfer Assessment Candidate

> A deterministic, fixture-only profile for preserving provider-job and local-transfer provenance across queued, partial, resumable, expired, failed, cancelled, complete, and quarantined states. It performs no request or download and grants no ingest authority.

## Purpose

Large-source acquisition often spans two state machines: a provider prepares an archive asynchronously, then a client transfers bytes locally. Treating either job success or the existence of a local file as completed ingest can admit truncated bytes, duplicate a resumed artifact, or erase retry and expiry lineage.

`AsynchronousTransferAssessment` binds a normalized query identity and idempotency key to one provider request, ordered polling history, byte-range checkpoint, digest posture, retry lineage, and downstream candidate state. Provider-specific endpoints, authentication, polling intervals, and resume mechanisms remain adapter concerns.

## Object surface

The assessment records:

- source and descriptor identity, normalized-query hash, request idempotency key, and provider request identifier;
- finite provider job state, attempt number, request and observation clocks, completion time, and archive expiry;
- ordered polling observations without treating a poll as source evidence;
- transfer state, expected and local size, completed byte ranges, partial/final/expected hashes, digest result, and resume basis;
- a sequenced transfer checkpoint with matching byte offset and state snapshot;
- optional prior-assessment retry lineage; and
- ingest-candidate posture, derived decision, deterministic identity, and fixed non-authority flags.

## Finite decisions

| Decision | Validator result | Meaning |
|---|---|---|
| `WAITING` | `PASS` | The provider job is active and no local bytes exist. |
| `RESUME_ELIGIBLE` | `PASS` | A coherent local prefix and checkpoint exist; a later adapter may request governed review before resuming. |
| `COMPLETE_CANDIDATE` | `PASS` | Size and digest are coherent and the artifact is only a quarantine/validation candidate. |
| `QUARANTINED` | `ABSTAIN` | Complete local bytes disagree with the expected digest. |
| `TERMINAL_NO_ARTIFACT` | `ABSTAIN` | A failed, cancelled, or expired job ended without local bytes. |
| malformed or contradictory packet | `DENY` | Shape, identity, ordering, byte-range, checkpoint, digest, retry, ingest, decision, or authority invariants failed. |
| `ERROR` or unreadable input | `ERROR` | The bounded assessment could not complete safely. |

`PASS` proves local consistency only. `COMPLETE_CANDIDATE` does not prove source authority, evidence fitness, rights, sensitivity clearance, validation, promotion, or publication readiness.

## Anti-collapse invariants

1. Provider request identity, normalized query identity, transfer checkpoint, and final artifact digest remain distinct.
2. Poll sequence and time are strictly increasing, and the last observed provider state equals the job snapshot.
3. Completed byte ranges form one contiguous prefix beginning at byte zero; gaps and overlaps are denied.
4. `PARTIAL` requires nonzero bytes below the expected size, a partial digest, and a checkpoint whose offset equals local size.
5. `COMPLETE` requires exact size, matching expected and final digests, and a quarantine-candidate reference.
6. `QUARANTINED` requires a digest mismatch and cannot expose an ingest candidate.
7. Incomplete bytes are never marked as processed downstream.
8. Retry lineage cannot reference the assessment being constructed.
9. No state authorizes network access, RAW writes, ingest, promotion, release, publication, or public use.

## Deterministic identity

The validator computes RFC 8785 JCS plus SHA-256 over the complete candidate after removing only `assessment_id` and `spec_hash`.

```text
spec_hash      = SHA-256(JCS(identity subject))
assessment_id  = kfm:async-transfer:<first 24 digest hex>
```

## Existing-family boundary

- `SourceDescriptor` remains the source identity, role, rights, sensitivity, cadence, and activation surface.
- `SourcePollingCheckpoint` remains conditional-request validator state for ordinary polling.
- RAW/WORK/QUARANTINE storage and promotion contracts remain lifecycle authorities.

This profile owns only the missing audit surface across asynchronous job preparation and local partial transfer. It does not replace those families or define a provider adapter.

## Directory Rules basis

Source semantics belong under `contracts/source/`; machine shape under `schemas/contracts/v1/source/`; synthetic cases under `fixtures/contracts/v1/source/`; reusable validation under `tools/validators/source/`; executable evidence under `tests/validators/`; orchestration under `.github/workflows/`; exploratory adaptation under `docs/intake/exploratory/`; and authoring accountability under `data/receipts/generated/`. The packet creates no new root or parallel source, policy, evidence, receipt, proof, release, or publication authority.

## Validation

```bash
python -m unittest -v tests.validators.test_validate_asynchronous_transfer_assessment
python tools/validators/source/validate_asynchronous_transfer_assessment.py --fixtures
```

## Rollback

Before merge, close the draft pull request and remove its branch. After an authorized merge, revert this additive contract/schema/fixture/validator/test/workflow/source-map/receipt packet. No provider job, local transfer, RAW object, ingest run, release, or publication requires operational rollback.
