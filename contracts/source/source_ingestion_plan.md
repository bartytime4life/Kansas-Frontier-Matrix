<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-ingestion-plan
title: SourceIngestionPlanCandidate Contract
type: semantic-contract; source-ingestion; fixture-first
version: v0.1.0
status: proposed; no-network; no-source-activation
owners: OWNER_TBD — Source steward · Connector steward · Contracts steward · Validation steward · Security reviewer
created: 2026-08-05
updated: 2026-08-05
policy_label: public; source; ingestion-plan; non-authoritative
related:
  - ./source_adapter.md
  - ./source_descriptor.md
  - ./ingest_receipt.md
  - ../../schemas/contracts/v1/source/source_ingestion_plan.schema.json
  - ../../fixtures/contracts/v1/source/source_ingestion_plan/
  - ../../tools/validators/validate_source_ingestion_plan.py
  - ../../tests/validators/test_validate_source_ingestion_plan.py
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, source-ingestion, http-conditional, cdc, scheduled-etl, deterministic, no-network]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# SourceIngestionPlanCandidate

> A `SourceIngestionPlanCandidate` records why one ingestion mode is proposed for one source, which replay and determinism controls the lane requires, and which authority it explicitly does **not** create. It is planning metadata, not a connector, source activation, live request, lifecycle mutation, release, or publication decision.

## Source-derived need

The attached *New Ideas 3-19-26* packet distinguishes three ingestion patterns:

1. scheduled ETL for bulk, predictable, backfill-oriented work;
2. conditional HTTP polling using ETag and Last-Modified for remote sources KFM does not control; and
3. event-driven CDC for authoritative transactional systems KFM controls.

It also requires deterministic identity from the source specification, upstream validators or offsets, partition keys, and transform digest; every lane emits a run receipt; and no automated materialization silently publishes.

This contract implements only that shared decision seam. It does not implement Debezium, Kafka, an HTTP client, a scheduler, OCI/ORAS, cosign, OPA, or live source access.

## Directory Rules basis

ADR-0029 adopts Directory Rules v2. This slice uses existing responsibility homes:

| Responsibility | Home |
|---|---|
| Semantic meaning | `contracts/source/` |
| Machine shape | `schemas/contracts/v1/source/` |
| Synthetic examples | `fixtures/contracts/v1/source/` |
| Executable validation | `tools/validators/` |
| Enforceability | `tests/validators/` |
| Read-only hosted orchestration | `.github/workflows/` |
| AI authoring provenance | `data/receipts/generated/` |

No new root or parallel source, contract, schema, policy, registry, receipt, proof, release, or publication authority is created.

## Mode semantics

### `HTTP_CONDITIONAL`

Use for an approved remote HTTP source outside KFM control.

Required posture:

- request method is `GET`;
- at least one of ETag or Last-Modified is expected;
- validators are persisted per approved locator;
- `NOT_MODIFIED` emits no new source artifact;
- retries use bounded exponential jitter;
- large-file resume is declared explicitly.

A `304`-equivalent no-change outcome is process memory, not a new source version and not proof that a volatile real-world condition ended.

### `EVENT_CDC`

Use for an authoritative transactional database KFM controls.

Required posture:

- offsets/checkpoints are durable;
- schema compatibility is declared;
- replay drills are required;
- stream partitioning is explicit; and
- the candidate does not claim exactly-once semantics.

A CDC plan does not authorize broker deployment, database credentials, table capture, or public release.

### `SCHEDULED_ETL`

Use for bulk or slow-changing corpora, backfills, and partition rebuilds.

Required posture:

- a partition plan exists;
- partial reruns are supported;
- checkpointing and resumable temporary artifacts are required; and
- a finite cost guardrail is declared.

A schedule is a proposed execution cadence, not source activation.

## Deterministic identity

For the fixture profile:

1. remove top-level `plan_id`;
2. remove `determinism.spec_hash`;
3. serialize canonical JSON with sorted keys, compact separators, finite numbers, and array order preserved;
4. compute SHA-256;
5. set `determinism.spec_hash = "sha256:<hex>"`;
6. set `plan_id = "kfm://candidate/source-ingestion/<source_id>/<hex>"`.

The dataset-version seed remains the ordered tuple:

```text
spec_hash + source_head + partition_key + transform_digest
```

This fixture identity is local and proposed; it does not settle a repository-wide hash-policy decision.

## Governance boundary

Every v1 candidate fixes:

- `source_activation_allowed = false`;
- `network_execution_authorized = false`;
- `authority_created = false`;
- `promotion_authorized = false`;
- `release_state = HOLD`;
- `public_use_allowed = false`;
- rights and sensitivity review to `NEEDS_VERIFICATION`.

A green result proves only candidate shape, mode compatibility, replay controls, deterministic identity, and fixed non-authority posture.

## Rollback

Before merge, close the pull request and abandon its branch. After an authorized merge, revert the dependency-closed contract/schema/fixtures/validator/tests/workflow/receipt commit. No source, network request, offset, scheduler state, lifecycle data, release, deployment, or published artifact requires restoration.

[Back to top](#top)
