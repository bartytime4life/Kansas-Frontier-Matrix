<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/asynchronous-transfer-assessment-source-map
title: Asynchronous Transfer Assessment - Source Map and Implementation Boundary
type: exploratory-intake-source-map
version: v0.1.0
status: promoted-to-fixture-candidate; non-authoritative; repository-grounded
owners: OWNER_TBD — Intake steward · Source steward · Ingest steward · affected domain stewards
created: 2026-08-10
updated: 2026-08-10
policy_label: public; intake; source; transfer; provenance; cite-or-abstain
owning_root: docs/
responsibility: Preserve traceability from supplied Full Atlas asynchronous-transfer cards to one bounded repository candidate without adopting provider behavior or promoting source prose into network, ingest, release, or publication authority.
truth_posture: CONFIRMED source-card traceability and inspected-tree collision review / PROPOSED bounded adaptation / NEEDS VERIFICATION steward review, provider adapters, and later-main collisions
related:
  - ../../kfm_full_atlas_seed_cards.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../contracts/source/asynchronous_transfer_assessment.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../contracts/source/source_polling_checkpoint.md
tags: [kfm, intake, full-atlas, asynchronous-job, partial-transfer, resume, checksum]
notes:
  - "Provider names in the source cards motivate the pattern only; this packet adopts no provider API fact."
  - "Repository collision review was refreshed against main during authoring; exact base SHA is preserved in the generated receipt and pull request."
[/KFM_META_BLOCK_V2] -->

# Asynchronous transfer assessment - source map

> **Outcome:** `KFM-TRIAD-050` and `KFM-CAND-0148` through `KFM-CAND-0150` are adapted into one synthetic, no-network contract packet. It preserves job, transfer, checkpoint, digest, retry, and ingest-candidate state while fixing every operational authority effect to false.

## Source lineage

| Source | Relevant proposal | Posture used here |
|---|---|---|
| Supplied/Drive `KFM_Full_Atlas_seed_cards.md` | `KFM-TRIAD-050`, `KFM-CAND-0148` through `KFM-CAND-0150` | Design lineage for separate provider-job and local-transfer state machines. |
| Existing source contracts | Descriptor identity and conditional polling checkpoint | Adjacent semantic boundaries retained without modification. |
| `docs/doctrine/directory-rules.md` plus accepted ADR-0029 | Responsibility-root placement and no-parallel-authority rules | Placement authority. |

## Current-main collision review

Bounded repository and pull-request searches found extensive download, checksum, checkpoint, and source-health behavior, including `SourcePollingCheckpoint`, but no common contract named `AsyncFetchRun`, `TransferCheckpoint`, `DownloadReceipt`, or `AsynchronousTransferAssessment` that jointly binds provider job state, partial local byte ranges, archive expiry, retry lineage, final digest, and no-incomplete-ingest posture. This is **CONFIRMED for the inspected tree**, not a timeless repository claim.

`SourcePollingCheckpoint` retains conditional-request validator state. This candidate adds no endpoint, credential, scheduler, provider adapter, request executor, downloader, RAW writer, or ingest executor.

## Bounded adaptation

The candidate keeps:

- normalized query identity and request idempotency separate from provider request identity;
- ordered finite provider job and local transfer states;
- expected and local sizes plus an exact contiguous-prefix byte-range rule;
- expected, partial, and final digest roles;
- checkpoint sequence, offset, and matching job/transfer snapshot;
- retry lineage, archive expiry, and explicit downstream incomplete-byte prohibition;
- complete artifacts as quarantine/validation candidates only; and
- deterministic identity, exact fixture polarity, and fixed false authority flags.

It deliberately excludes live requests, credentials, provider-specific polling, byte transfer, filesystem mutation, archive extraction, RAW/WORK writes, ingest execution, evidence resolution, source activation, policy decisions, review approval, promotion, release, deployment, publication, and public use.

## Directory Rules placement

| Artifact responsibility | Path |
|---|---|
| Source semantic meaning | `contracts/source/asynchronous_transfer_assessment.md` |
| Canonical machine shape | `schemas/contracts/v1/source/asynchronous_transfer_assessment.schema.json` |
| Reusable synthetic cases | `fixtures/contracts/v1/source/asynchronous_transfer_assessment/cases.json` |
| Repository validator | `tools/validators/source/validate_asynchronous_transfer_assessment.py` |
| Executable evidence | `tests/validators/test_validate_asynchronous_transfer_assessment.py` |
| Hosted orchestration | `.github/workflows/asynchronous-transfer-assessment.yml` |
| Human source adaptation | This file under `docs/intake/exploratory/` |
| AI-authoring process memory | `data/receipts/generated/` |

No new root or parallel source, schema, policy, evidence, lifecycle, receipt, proof, release, or publication home is created.

## Verification still required

Provider-specific adapters must independently verify official API states, expiry semantics, retry limits, checksum availability, byte-range support, credentials, rights, and rate limits before activation. Human stewards must review any path from `COMPLETE_CANDIDATE` into the governed RAW/WORK/QUARANTINE lifecycle.

## Validation and rollback

Validation covers Draft 2020-12 schema validity, exact `PASS/ABSTAIN/DENY/ERROR` fixture polarity, provider/poll coherence, contiguous ranges, checkpoint offsets, size and digest invariants, deterministic identity, parser bounds, no-network behavior, workflow parsing, documentation metadata, and generated-receipt hashes.

Rollback is an ordinary revert of the additive packet. Because no request, transfer, stored artifact, ingest run, policy, release, runtime, cache, or publication state is created, no operational data migration is required.
