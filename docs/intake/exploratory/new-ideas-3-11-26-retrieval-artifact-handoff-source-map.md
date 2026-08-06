# New Ideas 3-11-26 — retrieval-to-SourceArtifact handoff adaptation

## Status

- **Exploratory source:** `New Ideas 3-11-26.pdf`
- **Repository assay base:** `main@3ef64eca521d18f8df04014d768219e8dba36150`
- **Selected increment:** internal source-agnostic retrieval-to-SourceArtifact candidate handoff
- **Implementation status:** `PROPOSED` until reviewed and merged
- **Network, source activation, storage, lifecycle, evidence, release, and publication effects:** none

## Evidence-led selection

The source packet advocates deterministic source processing in which fetched bytes, hashes, validation, receipts, and review remain explicit. Current repository evidence already contains three separately governed foundations:

1. `connectors_core` source-head, retry, integrity, and redaction primitives;
2. caller-injected transport execution returning immutable exact payload bytes and finite outcomes; and
3. the fixture-first `SourceArtifact` contract, schema, validator, and local reference store.

The inspected base did not contain an explicit join between a successful `RetrievalResult` and a `SourceArtifact` candidate. Source-specific adapters would otherwise need to recreate that join independently, increasing the risk of inconsistent identity, locator redaction, time binding, request context, rights snapshots, correction lineage, and no-authority semantics.

## Repository adaptation

| Source/process idea | Bounded repository adaptation |
|---|---|
| Preserve exact source bytes and hashes. | Carry the exact immutable `CapturedPayload` chunks, SHA-256, byte length, and media type without normalization. |
| Bind source-head and run context. | Require matching source-head digest/length, final HTTP status, source descriptor reference, ingest receipt reference, request-profile names, rights snapshot, and parser identity. |
| Emit reviewable provenance. | Produce a metadata candidate conforming to the current SourceArtifact profile; do not emit an authoritative receipt or persist bytes. |
| Fail closed. | Reject `HEAD`, `NOT_MODIFIED`, failures, missing/mismatched metadata, invalid conflict/correction lineage, and self-supersession. |
| Keep publication behind review. | Fix all handoff and SourceArtifact public/release/authority flags to false or null. |

## Directory Rules basis

Accepted ADR-0029 makes Directory Rules v2 effective. Reusable source-agnostic implementation stays in `packages/connectors-core/`; object meaning, fixtures, tests, workflow evidence, source adaptation, and authoring provenance remain in their established responsibility roots.

This change creates no new root, schema authority, source registry, lifecycle stage, receipt authority, policy home, proof store, release home, public route, or source-specific adapter.

## Deferred candidates

- SourceDescriptor and IngestReceipt existence/correspondence resolver;
- content-addressed storage invocation and accepted RAW-or-QUARANTINE writer boundary;
- source-specific adapter mapping and parser execution;
- rights/sensitivity policy decisions;
- EvidenceRef/EvidenceBundle creation;
- catalog, release, API, map, and public-use integration.

Each deferred item requires its own evidence assay, authority boundary, fixtures, negative tests, review, and rollback.

## Rollback

Close the draft pull request before merge or revert the bounded implementation after merge. No external object or governed lifecycle state is created.
