<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-source-http-api-intake-v1
title: Shared HTTP API intake and private review interface
type: contract
version: v1
status: draft; implementation-aligned; private-intake-only; source-admission-and-release-held
owners: ["@bartytime4life"]
created: 2026-10-14
updated: 2026-10-14
policy_label: public
owning_root: contracts/
responsibility: Describe the shared source-capture and private-review semantics used by both host compositions
[/KFM_META_BLOCK_V2] -->

# Shared HTTP API intake and private review interface

This semantic contract describes the implemented `kfm-api-connections-v1`
interface. Placement follows the adopted Directory Rules and ADR-0029:
source-capture semantics extend the existing `contracts/source/` lane;
executable acquisition remains in `connectors/`, portable primitives in
`packages/connectors-core/`, orchestration in `pipelines/ingest/shared/`,
and host composition in the application. This document grants no admission,
rights, policy, review or release authority.

The source-specific executable profiles, common request/replay implementation,
application DTOs and changed-area tests enforce this bounded intake interface.
It does not introduce a parallel machine-schema home or replace the existing
SourceDescriptor, IngestReceipt, RunReceipt or EvidenceBundle contracts.

## Operations and recipients

| Operation | Authority | Result |
|---|---|---|
| GET /api/connections (catalog) | Visitor metadata access | Source specifications/configuration holds, host status, owner boolean; no captures |
| GET action=captures | Existing archive owner | Bounded recent API receipt history |
| GET action=view&id=SHA256 | Existing archive owner | Verified saved view and receipt |
| GET action=entity&id=SHA256 | Existing archive owner | Verified final native entity; sandboxed attachment except reviewed PNG |
| GET action=bundle&id=SHA256 | Existing archive owner | Whole stored bundle with verified digest; may include invalid quarantine material |
| POST /api/connections | Same-origin existing archive owner and ready/unpaused host | Capture or cached saved readback/replay |
| POST /api/connections/run | Existing capture-worker or same-origin archive owner | At most two configured-profile outcomes, never entity bytes |

Query keys are closed to action/id; duplicate and unknown keys reject.
Capture input is a duplicate-free, bounded JSON object containing sourceId
and optional query. sourceId selects a fixed profile; query contains only
that profile's field keys and string/enumeration/date/numeric bounds.
The caller supplies no URL, SQL, key, pagination traversal, storage root or
release decision. Configuration-derived scheduling defaults disabled and
accepts at most 16 reviewed profiles in 4096 characters.

## Identity, storage and replay

Identity binds runtime version, provider profile, exact normalized selection,
time bucket, methods, destinations and request bodies. Both hosts share the
same builder/parser/replay bytes and application DTOs. They use independent
owner/environment/store adapters: Node MySQL and Sites D1/R2.

The bundle retains bounded decoded entities and SHA-256 integrity, including
preflight metadata, retrieval times and explicit transforms. Credentialed
JSON is validated before storage; decoded string/key echoes are redacted.
Malformed keyed JSON and redaction collisions reject before persistence.
Unnecessary MIME parameters and keyed validator headers are omitted.
Received/stored body digests make the transform inspectable. Anonymous
source bodies remain unchanged.

A result requires durable saved-byte readback, whole-bundle/entity integrity,
canonical request identity and source-specific parsing. Views preserve native
rows, actual geometry/raster support, dates, units, flags, censoring, missingness,
partial/empty states and limitations. They do not synthesize measurements.
Host accounting, pause and lease controls precede acquisition and acceptance;
failed/interrupted history is retained.

## Governance boundary

Every API receipt remains WORK/QUARANTINE, unreleased, pending rights/sensitivity
review and EXTERNAL_CONTEXT_ONLY. Provider profile IDs are an executable
allowlist; they are not admitted source-registry identities. This intake receipt
is not asserted to satisfy the governed IngestReceipt schema.

Before promotion, bind an admitted SourceDescriptor and governed run/ingest
identities, perform validation/rights/sensitivity/provenance/integrity review,
construct the required EvidenceBundle and release package, and use the existing
review/correction/rollback transition. Public data clients receive only those
released governed projections. The present routes cannot promote, publish,
delete history, grant release authority or activate main-map layers.

Implementation and operator evidence are in
[the dual-host runbook](../../docs/runbooks/api-connections.md).
Rollback pauses/removes the new intake surfaces while preserving captures,
receipts, reservations, source identities and both hosts' existing histories.
