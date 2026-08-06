<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/retrieval-artifact-handoff
title: Retrieval-to-SourceArtifact Handoff Contract
type: semantic-contract; source-agnostic-internal-handoff
version: v0.1.0
status: proposed; fixture-first; no-network
owners: OWNER_TBD — Connector steward · SourceArtifact steward · Ingest receipt steward · Validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: public; source; exact-byte-handoff; no-lifecycle-authority; no-publication
related:
  - ./source_adapter.md
  - ./source_artifact.md
  - ./ingest_receipt.md
  - ../../packages/connectors-core/src/connectors_core/ARTIFACT_HANDOFF.md
  - ../../packages/connectors-core/src/connectors_core/artifact_handoff.py
  - ../../schemas/contracts/v1/source/source_artifact.schema.json
  - ../../tools/validators/validate_source_artifact.py
  - ../../tests/packages/connectors_core/test_artifact_handoff.py
tags: [kfm, connector, retrieval, source-artifact, exact-bytes, handoff, no-network]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Retrieval-to-SourceArtifact Handoff Contract

> A retrieval-artifact handoff converts one already-successful, source-agnostic injected `GET` result into exact captured bytes plus a `SourceArtifact` metadata candidate. It does not fetch, store, emit a receipt, write a lifecycle stage, resolve evidence, decide policy, release, or publish.

## Why the boundary exists

KFM now has separate internal foundations for:

1. deterministic source-head, retry, integrity, and redaction primitives;
2. caller-injected transport execution with exact captured bytes; and
3. a fixture-first `SourceArtifact` contract, schema, validator, and local reference store.

Those surfaces must not be joined through ad-hoc dictionaries in source-specific adapters. The handoff makes the boundary explicit while preserving separation:

```text
caller-owned transport + source profile
  -> RetrievalResult
  -> retrieval-artifact handoff candidate
  -> existing SourceArtifact schema/semantic validation
  -> caller-owned IngestReceipt correspondence and storage decision
  -> later evidence, policy, review, lifecycle, release, correction, rollback
```

The handoff cannot skip any downstream step.

## Admitted input

A handoff is admitted only when:

- the result is `TransportCategory.SUCCESS`;
- the method is `GET`;
- exact non-empty `CapturedPayload` bytes exist;
- a `SourceHeadObservation` exists;
- source-head digest and optional content length match the payload;
- final attempt status, digest, and byte length are coherent;
- the caller supplies a governed source descriptor reference and ingest receipt reference;
- retrieval-time rights, parser identity, request-profile metadata, source-surface type, and governance-spec hash are explicit; and
- correction/conflict lineage is internally coherent.

`HEAD`, `NOT_MODIFIED`, timeout, access denied, rate limit, cancellation, partial, unsafe, integrity-failed, oversized, and exhausted outcomes produce no handoff. They remain process/source-health observations.

## Output

The output carries:

- immutable exact payload chunks;
- a deep-frozen metadata candidate matching the existing `SourceArtifact` shape;
- deterministic `artifact_id`, `content_digest`, `immutable_storage_ref`, and locator digest;
- redacted locator and value-minimized request context;
- explicit rights snapshot, parser identity, source surface, and lineage; and
- fixed `public_use_allowed=false`, `authority_created=false`, `lifecycle_write_allowed=false`, `receipt_created=false`, and `repository_mutation_allowed=false` boundaries.

The handoff object can produce a plain metadata dictionary for the existing validator, but it never validates itself into authority or writes the bytes.

## Caller obligations

A governed caller must separately:

1. prove that the referenced `SourceDescriptor` and `IngestReceipt` exist and correspond to the run;
2. validate the metadata and bytes using the repository-owned SourceArtifact validator;
3. decide whether and where exact bytes may be stored;
4. preserve rights, sensitivity, correction, conflict, and retention requirements;
5. perform any RAW-or-QUARANTINE handoff through an accepted writer boundary; and
6. withhold evidence, catalog, release, API, map, or public use until their own gates pass.

## Directory Rules basis

Accepted ADR-0029 makes Directory Rules v2 effective. Reusable source-agnostic implementation remains under `packages/connectors-core/`; semantic meaning remains under `contracts/source/`; executable proof remains under `tests/packages/connectors_core/`; fixture context remains under `fixtures/packages/connectors_core/`; CI remains under `.github/workflows/`; and generated authoring provenance remains under `data/receipts/generated/`.

No new root, schema authority, source registry, lifecycle lane, receipt authority, policy home, proof store, release home, public route, or source-specific connector is created.

## Validation

The first implementation must prove:

- exact payload chunk, digest, and length preservation;
- deterministic artifact and locator identity;
- successful validation by the current SourceArtifact schema and semantic validator;
- rejection of no-byte, `HEAD`, `NOT_MODIFIED`, failed, mismatched-head, and self-superseding inputs;
- conflict and correction lineage polarity;
- immutable metadata and secret-safe representation;
- package import without network or filesystem effects; and
- absence of storage, lifecycle, receipt, evidence, policy, release, and publication dependencies.

## Rollback

Before merge, close the draft pull request and abandon the branch. After a future merge, revert the bounded implementation commit. The handoff creates no external object, lifecycle record, receipt, evidence, release, or public product requiring cleanup.

[Back to top](#top)
