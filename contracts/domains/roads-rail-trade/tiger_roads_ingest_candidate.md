<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/roads-rail-trade/tiger-roads-ingest-candidate
title: TIGER Roads Ingest Candidate
type: semantic-contract
version: v0.1.0
status: proposed; fixture-first; no-network; non-writing
owners: OWNER_TBD — Source steward · Roads/Rail/Trade steward · Validation steward
created: 2026-11-19
updated: 2026-11-19
policy_label: public; source-capture; candidate-only; no-road-authority
owning_root: contracts/
responsibility: define the bounded held TIGER ingest projection of existing package inspection
truth_posture: PROPOSED candidate semantics; CONFIRMED no-authority envelope; NEEDS VERIFICATION human review and source admission
[/KFM_META_BLOCK_V2] -->

# TIGER roads ingest candidate

`TigerRoadsIngestCandidate` is a proposed, bounded ingest projection of the existing
Census `PackageCandidate`. It records inspection of one supplied Kansas county
2025 ROADS package. It is source-capture metadata and is never a
[Road Segment](./road_segment.md), graph edge, route, legal-access statement,
closure event, public-safe road product or traffic instruction.

The profile reuses the established `roads-rail-trade` ingest implementation and
candidate homes under ADR-0029. It does not resolve the broader documented
`transport` / `roads-rail-trade` home conflict or move any existing object family.

## Identity and reference meaning

The artifact digest binds exact supplied ZIP bytes. The candidate identity is
`tiger-roads-ingest:` followed by SHA-256 of canonical JSON containing only
`file_name` and `artifact`. Retrieval time does not change that byte identity.
`spec_hash` binds the complete candidate excluding its own hash, so capture-time,
reference or inspection changes remain visible. Timestamps normalize to UTC;
capture cannot precede the filename's vintage year.

The committed provider manifest supplies the permitted county filenames and
expected SHA-256 and length. Its complete bytes are separately hash-bound.
`exact_bytes_match` is true only when both expected values match the supplied
artifact. Synthetic captures deliberately do not match Census bytes; they do
not replace or modify the provider manifest. A match never grants admission.

## Inspection and finite outcomes

The implementation caps supplied ZIPs at 2 MiB, each expanded member at 2 MiB,
combined expansion at 8 MiB, and member count at 16. It reads all member bytes
for CRC integrity; rejects encrypted, symlink, nested, duplicate, unsupported
compression and excessive expansion cases; then invokes the existing package
inspector. Only stored and deflated members are accepted.

The inspector checks SHP/SHX headers, feature-count agreement, DBF identities and
any supplied state/county attributes. CRS recognition is a header-text check;
it does not validate transformations or individual geometries. County scope
comes from the filename unless attributes independently support it. The fixtures
have no state/county DBF columns, so their Kansas-feature count remains null.
Unknown CRS, duplicate identity, deleted rows and other inspector findings stay
explicit as `QUARANTINE_CANDIDATE`. Structurally clean material has provisional
`RAW_CANDIDATE`; neither route causes a write. Malformed packages raise bounded
errors instead of minting a successful candidate.

Every final route is `HOLD`: source admission, the domain descriptor, rights and
sensitivity remain unresolved. All eight authority flags are false. The Census
connector's family role/rights settings do not resolve the separate domain
[source descriptor](../../../data/registry/roads-rail-trade/sources/census_tiger_roads.yaml).
Geometry, CRS transformation, provider coverage, legal status and operational
routing remain unverified. JSON/schema/CI success cannot resolve these limits.

## Conformance and rollback

The [closed schema](../../../schemas/contracts/v1/domains/roads-rail-trade/tiger_roads_ingest_candidate.schema.json)
checks shape and denied authority. Runtime validation additionally checks both
hashes, the current manifest binding, UTC time, route/reason consistency and
count relationships. The [runbook](../../../docs/runbooks/tiger-roads-fixture-ingest.md)
binds sealed goldens, negative tests, aggregate-only CLI and no-network CI.

Revert the bounded implementation/declaration/schema/test/workflow change to
restore the inactive stub. Preserve earlier receipts and the provider reference;
no lifecycle data or source activation is changed by this profile.
