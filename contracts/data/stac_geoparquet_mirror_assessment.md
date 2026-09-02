<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/stac-geoparquet-mirror-assessment
title: STAC GeoParquet Mirror Assessment Contract
type: semantic-contract
version: v0.1.0
status: proposed; experimental-profile; fixture-only; non-authoritative
owners: OWNER_TBD — Catalog steward · STAC steward · Data steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public; contracts; data; stac; geoparquet; mirror; cite-or-abstain
owning_root: contracts/
responsibility: Define bounded content-parity meaning between a declared STAC Item set and a declared STAC GeoParquet collection-mirror projection without opening Parquet, resolving catalog objects, or granting catalog, evidence, policy, review, release, or publication authority.
truth_posture: PROPOSED contract / CONFIRMED deterministic synthetic implementation / NEEDS VERIFICATION upstream stability, steward approval, byte-level readers, catalog closure, and operational integration
related:
  - ../../schemas/contracts/v1/data/stac_geoparquet_mirror_assessment.schema.json
  - ../../fixtures/contracts/v1/data/stac_geoparquet_mirror_assessment/cases.json
  - ../../tools/validators/catalog/validate_stac_geoparquet_mirror_assessment.py
  - ../../docs/intake/exploratory/stac-geoparquet-mirror-assessment-source-map.md
  - ../../docs/standards/STAC.md
  - ./catalog_health_report.md
tags: [kfm, catalog, stac, geoparquet, collection-mirror, parity]
notes:
  - "A PASS proves exact parity only for the supplied declared projections; it does not prove the source STAC objects, Parquet bytes, catalog closure, or release state."
[/KFM_META_BLOCK_V2] -->

# STAC GeoParquet mirror assessment

## Status and purpose

`StacGeoParquetMirrorAssessment` is a **PROPOSED**, experimental, fixture-only contract for comparing declared STAC Item projections with declared rows in a STAC GeoParquet collection mirror. It implements a narrow parity gate while the upstream mapping specification remains version-sensitive.

The profile is pinned by upstream repository, document, Git blob SHA, mapping version, STAC version, and GeoParquet version. Moving the pin requires a reviewed contract and fixture update; `main` or a mutable URL alone is not identity.

## Bounded mapping

Each declared source item and mirror row carries the same comparison projection:

- collection and item identity;
- ordered STAC extension identifiers;
- geometry and bbox representation through a declared digest and finite bbox coordinates;
- link, asset, and non-temporal property digests;
- ordered property names, with reserved top-level-name collision denial; and
- either an instant timestamp or a complete start/end interval.

The mirror additionally declares its collection-mirror asset, media type, role, geometry encoding, native timestamp storage, mapping metadata version, and collection metadata digests. This keeps mapping parity distinct from physical Parquet conformance.

## Finite outcomes

| Validator outcome | Assessment result | Meaning |
|---|---|---|
| `PASS` | `PARITY_CONFIRMED` | Every declared full-collection source item has one byte-for-byte-equivalent projection row, with no extras. |
| `ABSTAIN` | `PARTIAL_SAMPLE` | The supplied sample matches, but the assessment cannot claim collection-wide parity. |
| `DENY` | `PARITY_CONFLICT` or validation finding | Items are missing, unexpected, divergent, duplicated, noncanonical, malformed, or outside the fixed trust boundary. |
| `ERROR` | `ERROR` | The assessment explicitly declares failure, or input could not be safely parsed. |

`PASS` is not a catalog, evidence, policy, review, release, or publication decision.

## Invariants

1. Source items and mirror rows have unique `(collection_id, item_id)` keys in lexical order.
2. Both sides belong to the one declared source collection.
3. Mirror collection metadata contains exactly that collection identifier and digest.
4. Extension and property-name lists are unique and lexical; property names cannot collide with reserved top-level fields.
5. Temporal shape is exactly one instant or one complete interval.
6. The report is mechanically derived from the two declared projections.
7. `spec_hash` and `assessment_id` are deterministic over canonical content excluding those fields.
8. Network, Parquet access, source resolution, catalog mutation, evidence resolution, policy, review, release, publication, and public use remain false.

## Explicit non-claims

This validator does not:

- open or validate a Parquet file, Arrow schema, WKB, GeoArrow geometry, or native timestamp;
- fetch or validate STAC Items or Collections;
- prove that a mirror asset exists or that its digest, size, rights, sensitivity, or release state is valid;
- replace KFM STAC, DCAT, PROV, EvidenceBundle, catalog-health, catalog-closure, correction, or rollback responsibilities; or
- adopt the experimental upstream mapping specification as KFM doctrine.

Operational integration must add byte-level reader validation, authoritative source resolution, catalog closure, rights and sensitivity checks, review, release, correction, and rollback evidence.

## Validation and rollback

Validation covers Draft 2020-12 shape, exact `PASS/ABSTAIN/DENY/ERROR` fixture polarity, full versus sample scope, content divergence, key and collection integrity, canonical lists, property collision, temporal shape, deterministic identity, hostile parsing, no-network/import posture, workflow parsing, metadata, and generated-receipt replay.

Rollback is an ordinary revert of this additive packet. It creates no catalog record, mirror asset, evidence object, policy decision, release, correction, rollback, deployment, or publication state.
