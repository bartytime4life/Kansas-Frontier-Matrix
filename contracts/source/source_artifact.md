<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-artifact
title: SourceArtifact Contract
type: semantic-contract; immutable-source-capture-metadata
version: v0.1.0
status: proposed; fixture-first; no-network; validator-implemented
owners: OWNER_TBD — Source steward · Contracts steward · Evidence steward · Validation steward · Rights/sensitivity steward
created: 2026-08-04
updated: 2026-08-04
policy_label: public; source; immutable-capture; no-public-authority
related:
  - ./README.md
  - ./source_descriptor.md
  - ./ingest_receipt.md
  - ./source_adapter.md
  - ../../schemas/contracts/v1/source/source_artifact.schema.json
  - ../../fixtures/contracts/v1/source/source_artifact/
  - ../../tools/validators/validate_source_artifact.py
  - ../../tools/source_artifacts/README.md
  - ../../tests/validators/test_validate_source_artifact.py
  - ../../docs/architecture/source-verification.md
tags: [kfm, source-artifact, immutable-bytes, sha256, content-addressed, rights-snapshot, parser-version, correction, conflict]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# SourceArtifact Contract

> `SourceArtifact` is the immutable metadata record for exact captured source bytes. It binds the captured bytes to a governed source reference, safe source locator, retrieval and source-reported times, finite capture outcome, media type, exact byte length, SHA-256 digest, content-addressed storage reference, retrieval-time rights snapshot, parser identity, and correction/conflict lineage.

## Status and authority boundary

| Field | Value |
|---|---|
| Status | `PROPOSED` / fixture-first / no-network |
| Semantic home | `contracts/source/source_artifact.md` |
| Machine shape | `schemas/contracts/v1/source/source_artifact.schema.json` |
| Validator | `tools/validators/validate_source_artifact.py` |
| Local store helper | `tools/source_artifacts/content_addressed_store.py` |
| Public use | Fixed to `false` in this profile |
| Authority created | None |

A valid SourceArtifact proves only that the declared metadata is internally consistent and, when a payload is supplied to the validator, that the exact local bytes match the recorded SHA-256 and byte length. It does not:

- admit or activate the source;
- prove the source statement is true;
- resolve an `EvidenceRef` or close an `EvidenceBundle`;
- decide rights, sensitivity, policy, review, lifecycle transition, release, or publication;
- replace `SourceDescriptor`, `IngestReceipt`, `RunReceipt`, `ParseResult`, or `ReleaseManifest`.

## Why this object exists

Source verification needs a durable boundary between transport/process memory and the exact captured source object:

```text
SourceDescriptor
  -> SourceAdapter retrieval outcome
  -> exact captured bytes
  -> IngestReceipt / RunReceipt process memory
  -> SourceArtifact immutable metadata + content digest
  -> ParseResult + field-level EvidenceRef candidates
  -> evidence, policy, review, release, correction, rollback
```

`IngestReceipt` records an ingest run. `SourceArtifact` identifies one exact captured byte stream produced or preserved by that run. One ingest can produce multiple SourceArtifacts; one SourceArtifact must have exactly one byte identity.

## Required semantic surface

| Field | Meaning |
|---|---|
| `artifact_id` | Deterministic `source-artifact:sha256:<hex>` identity derived from `content_digest`. |
| `source_descriptor_ref` | Reference to the governed source identity and treatment posture. |
| `ingest_receipt_ref` | Process-memory reference for the capture run. |
| `source_locator` | Exact source-native locator class and value, first-party authority reference, and locator digest. |
| `retrieved_at` | KFM capture time, with timezone. |
| `source_reported_at` | Source update/publication time when available; never silently replaced by retrieval time. |
| `retrieval_outcome` | Captured-byte outcome: `FETCHED`, `MALFORMED`, or `SOURCE_CONFLICT`. |
| `status_code` | HTTP status when an HTTP/API locator is used; otherwise nullable. |
| `media_type` | Explicit native media type, not inferred later from a filename. |
| `byte_length` | Exact positive byte count of the captured object. |
| `content_digest` | SHA-256 over the exact captured bytes. |
| `immutable_storage_ref` | `cas:sha256:<hex>` logical reference derived from the same digest. |
| `request_context` | Reproducibility metadata limited to method, profile, parameter/header names, optional body digest, and `secrets_embedded=false`. |
| `rights_snapshot` | Terms/license/access posture recorded at retrieval time; not a final policy decision. |
| `parser` | Parser identity, version, and spec digest used or intended for the capture. |
| `source_surface_type` | Source-native surface such as API record, current table, PDF, GIS package, or repository object. |
| `lineage` | Supersession, correction, and conflict-group references. |
| `public_use_allowed` | Always false for this internal verification object. |

## Captured-byte outcomes versus no-byte outcomes

A SourceArtifact exists only when bytes are preserved. The first profile therefore admits three outcomes:

| Outcome | Meaning |
|---|---|
| `FETCHED` | Bytes were captured and are available for parse and validation. |
| `MALFORMED` | Bytes were captured but the declared parser could not safely interpret the expected layout. The bytes remain evidence of what the source returned. |
| `SOURCE_CONFLICT` | Bytes were captured from one official surface participating in a material conflict. Each conflicting surface remains a distinct artifact linked by `conflict_group_ref`. |

No-byte transport outcomes—timeout, access denied, rate limited, not found, redirect blocked, response too large, and similar states—belong in the SourceAdapter result and `RunReceipt`/source-health process memory. They must not mint a fake zero-byte SourceArtifact. `NOT_MODIFIED` likewise refers back to a prior artifact identity rather than creating duplicate captured bytes.

## Deterministic identity and locator binding

```text
content_digest          = sha256(exact captured bytes)
artifact_id             = source-artifact:<content_digest>
immutable_storage_ref   = cas:<content_digest>
locator_digest          = sha256(locator_kind + "\n" + locator_value)
```

The locator digest does not prove the source is safe or authoritative. It makes later mutation of the locator detectable. HTTP/API locator values must use HTTPS and exclude credentials, queries, fragments, controls, malformed escapes, and unsafe backslashes in this first profile. Reproducibility-sensitive query semantics belong in a governed request profile and safe parameter-name/body-digest records, not embedded secrets.

## Time, rights, parser, and media rules

- `source_reported_at` cannot occur after `retrieved_at` in the represented capture.
- `rights_snapshot.captured_at` cannot occur after `retrieved_at`.
- Every timestamp is timezone-aware.
- API-record surfaces require a structured media type.
- PDF surfaces require `application/pdf`.
- Parser version and parser-spec digest remain visible even when the bytes are malformed.
- An all-zero digest is never accepted as an identity placeholder.

A later source-specific profile may narrow allowed media types, hosts, response codes, sizes, request profiles, or parser requirements. It must not weaken the shared identity or public-use boundary.

## Correction, conflict, and supersession

Source correction does not overwrite prior bytes.

- A corrected capture creates a new SourceArtifact.
- `supersedes_artifact_ref` points to the prior artifact.
- At least one correction reference is required when supersession is declared.
- An artifact cannot supersede itself.
- Conflicting official surfaces remain separate artifacts and share a conflict-group reference.
- A conflict must not be “resolved” by deleting, rewriting, or selecting the more plausible source statement.

## Validation and local content-addressed storage

The validator checks closed schema shape, duplicate-key/non-finite/complexity bounds, deterministic identities, safe locator posture, temporal ordering, media compatibility, canonical request arrays, self-supersession, and optional exact-byte SHA-256/length binding.

```bash
python tools/validators/validate_source_artifact.py --fixtures
python tools/validators/validate_source_artifact.py METADATA.json --payload CAPTURED_BYTES
```

The local store accepts only already-valid metadata/byte pairs:

```bash
python tools/source_artifacts/content_addressed_store.py store \
  METADATA.json CAPTURED_BYTES STORE_ROOT
python tools/source_artifacts/content_addressed_store.py verify \
  METADATA.json STORE_ROOT
```

The helper is a fixture/reference implementation. It does not define production object-storage topology, retention, credentials, legal holds, lifecycle promotion, or public delivery.

## Rollback

Before merge, close the draft pull request and delete the feature branch. After merge, revert the scoped contract/schema/fixture/validator/store/workflow change through review. Do not delete captured evidence merely because a contract revision is rolled back; any real artifact already relied on requires correction/supersession handling appropriate to its use.

[Back to top](#top)
