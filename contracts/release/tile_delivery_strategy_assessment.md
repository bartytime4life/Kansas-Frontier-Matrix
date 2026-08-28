<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/release/tile-delivery-strategy-assessment
title: Tile Delivery Strategy Assessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed; inactive; fixture-only; no-network; review-required
owners: OWNER_TBD — Map steward · Release steward · Runtime steward · Rights reviewer · Sensitivity reviewer · Validation steward
created: 2026-08-12
updated: 2026-08-12
policy_label: internal; release; map; tile-delivery; pmtiles; xyz; martin; mbtiles
owning_root: contracts/
responsibility: Define a bounded release-facing assessment for choosing among PMTiles archive, XYZ service, Martin/PostGIS mediation, and local MBTiles without hosting, activating, deploying, releasing, or publishing anything.
truth_posture: CONFIRMED supplied-source and repository-gap evidence / PROPOSED inactive assessment / NEEDS VERIFICATION human review, real consumers, measured hosting evidence, and hosted exact-head CI
related:
  - ./tile_artifact_manifest.md
  - ../source/map_service_protocol_assessment.md
  - ../runtime/pmtiles_release_cache.md
  - ../../schemas/contracts/v1/release/tile_delivery_strategy_assessment.schema.json
  - ../../fixtures/contracts/v1/release/tile_delivery_strategy_assessment/cases.json
  - ../../tools/validators/release/validate_tile_delivery_strategy_assessment.py
  - ../../tests/release/test_tile_delivery_strategy_assessment.py
  - ../../docs/intake/exploratory/tile-delivery-strategy-assessment-source-map.md
tags: [kfm, release, map, tile-delivery, pmtiles, xyz, martin, mbtiles, fixture-only]
notes:
  - "Adapts the supplied MapLibre operating guidance into a declaration assessment, not an automatic hosting or release decision."
  - "PASS means the declared strategy is locally coherent and ready for human review; it never verifies artifact bytes, a service, rights, sensitivity, performance, release, or public use."
[/KFM_META_BLOCK_V2] -->

# Tile Delivery Strategy Assessment Candidate

> A deterministic, no-network assessment that keeps immutable public archives,
> mutable tile services, server-mediated spatial queries, and local offline
> packages from collapsing into one generic delivery choice.

## Purpose

The supplied MapLibre operating manual distinguishes four responsibilities:

- PMTiles for stable, public-safe, immutable or rebuildable bundles with
  range-capable hosting;
- XYZ when a mutable service needs per-tile invalidation;
- Martin/PostGIS when dynamic queries, access control, steward mediation, or
  database-backed slicing are required; and
- MBTiles as a local/offline package rather than a public hosting default.

This contract turns that distinction into one closed review candidate. It
checks declared update, audience, safety, mediation, invalidation, offline, and
hosting requirements against one selected strategy. It does not select a
vendor, contact a service, inspect tiles, open a database, measure performance,
mutate a cache, host an artifact, deploy a renderer, or authorize release.

## Strategy matrix

| Strategy | Coherent declared need | Required reference boundary | Explicit limit |
|---|---|---|---|
| `PMTILES_ARCHIVE` | Immutable or append-only versioned artifact; public-safe input; no per-tile invalidation or server mediation; range hosting ready. | Tile artifact manifest and cache policy refs. | No dynamic query, access-control, or PostGIS bypass. |
| `XYZ_SERVICE` | Partial mutation with per-tile invalidation. | Map-service protocol assessment and cache policy refs. | Service health, endpoint behavior, and tile bytes are not verified. |
| `MARTIN_POSTGIS` | Dynamic query, access control, steward/server mediation, or PostGIS-backed slicing. | Map-service protocol assessment ref. | No database, policy, credential, or runtime is activated. |
| `MBTILES_LOCAL` | Local audience plus explicit offline requirement. | Tile artifact manifest ref. | Never accepted as a public delivery declaration. |

## Finite outcomes

| Outcome | Meaning | Non-effect |
|---|---|---|
| `PASS` | The selected strategy matches the declared need and its local reference obligations. | Ready for review only. |
| `HOLD` | The strategy is unsupported, mismatched, or missing a required declared control. | No optimistic default is selected. |
| `DENY` | The declaration would expose non-public-safe input, make MBTiles public, conflict public audience with access control, or bypass required mediation. | No partial delivery is allowed. |
| `ERROR` | The bounded assessment could not be completed safely. | No candidate state is trusted. |

## Invariants

1. Public delivery requires `public_safe_input=true`.
2. `MBTILES_LOCAL` requires `audience=LOCAL` and
   `offline_required=true`; public MBTiles delivery is denied.
3. Static PMTiles/XYZ declarations cannot bypass required server mediation,
   access control, or PostGIS slicing.
4. PMTiles requires an immutable versioned artifact, range-capable hosting,
   artifact-manifest ref, cache-policy ref, and no partial mutation.
5. XYZ requires partial mutation, per-tile invalidation, protocol-assessment
   ref, and cache-policy ref.
6. Martin/PostGIS requires a real declared mediation need and a
   protocol-assessment ref.
7. The validator recomputes the recommended strategy, outcome, reason code,
   deterministic identity, and `spec_hash`.
8. Network, service activation, artifact hosting, database query, cache
   mutation, release, deployment, publication, and public-use authority are
   fixed to `false`.

## Composition boundary

- `MapServiceProtocolAssessment` owns protocol-specific source/service
  coherence; this assessment references it but does not replace it.
- `TileArtifactManifest` owns artifact identity, format, bounds, and digest;
  this assessment does not inspect bytes.
- `PMTilesReleaseCache` and other runtime cache controls retain runtime
  behavior.
- Rights, sensitivity, review, promotion, release, correction, and rollback
  objects retain their own authority.

## Deterministic identity

RFC 8785 JCS plus SHA-256 is computed over the full candidate except
`assessment_id` and `spec_hash`:

```text
spec_hash     = SHA-256(JCS(identity subject))
assessment_id = "kfm:tile-delivery-strategy:" + first_24_hex(spec_hash)
```

The identity is a local replay pin, not proof of an artifact, service, hosting
environment, cache, policy, release, or public behavior.

## Directory Rules basis

Release-facing delivery-choice meaning belongs under `contracts/release/`;
machine shape under `schemas/contracts/v1/release/`; synthetic cases under
`fixtures/contracts/v1/release/`; deterministic validation under
`tools/validators/release/`; executable proof under `tests/release/`;
read-only orchestration under `.github/workflows/`; source adaptation under
`docs/intake/exploratory/`; and AI authoring accountability under
`data/receipts/generated/`.

No new root or parallel map protocol, artifact, cache, policy, release, or
publication authority is created.

## Validation

```bash
python -m pytest -q tests/release/test_tile_delivery_strategy_assessment.py
python tools/validators/release/validate_tile_delivery_strategy_assessment.py --fixtures
```

## Rollback

Before merge, close the draft pull request and remove its branch. After an
authorized merge, revert this additive packet. It has no runtime consumer and
changes no endpoint, artifact, database, cache, layer, release, deployment, or
public surface.
