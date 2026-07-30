<a id="top"></a>

# Processed RAC region geometry

[![Lifecycle: PROCESSED](https://img.shields.io/badge/lifecycle-PROCESSED-0969da?style=flat-square)](../../README.md#status)
[![Release: not released](https://img.shields.io/badge/release-not--released-b42318?style=flat-square)](../../../registry/datasets/water_planning/kwo_rac_regions_2026-06-24.json)
[![Validation: deterministic and no-network](https://img.shields.io/badge/validation-deterministic%20%2B%20no--network-1f883d?style=flat-square)](../../../../tools/validators/domains/water_planning/validate_rac_registry.py)
[![Source: Kansas Water Office](https://img.shields.io/badge/source-Kansas%20Water%20Office-8250df?style=flat-square)](../../../registry/sources/water_planning/kwo_rac_feature_service.source.json)

Versioned Kansas Water Office (KWO) Regional Advisory Committee (RAC)
planning-area geometry for KFM's internal `PROCESSED` lifecycle lane.

> [!IMPORTANT]
> These bytes are a digest-pinned internal product, not a published map layer.
> A current registry pointer, a passing validator, a pull request, or a merge
> does not provide rights clearance, release approval, public-serving
> authority, or KFM publication.

**Quick navigation:** [Purpose and boundary](#purpose-and-boundary) ·
[Inventory](#inventory) · [Geometry contract](#geometry-contract) ·
[Source and lifecycle](#source-authority-and-lifecycle) ·
[County crosswalk](#related-county-crosswalk) · [Validation](#validation) ·
[Correction](#correction-review-and-rollback) ·
[Related authority](#related-authority) ·
[Open verification](#open-verification-items)

## Purpose and boundary

This directory owns one normalized, versioned RAC geometry payload and the
local documentation needed to interpret it. It inherits the
[`data/processed/` contract](../../README.md): processed placement records an
internal lifecycle state and does not make the payload public.

The placement outcome is `PLACE` under the accepted
[Directory Rules](../../../../docs/doctrine/directory-rules.md). The payload is
a processed data instance under `data/`; `water_planning` is a domain scope
lane; `rac_regions` is the leaf object-family directory. This README does not
create schema, contract, registry, policy, proof, release, or publication
authority.

| Field | Confirmed repository state |
|---|---|
| Owning responsibility | `data/processed/` |
| Domain scope | `water_planning` |
| Object family | KWO RAC planning-area geometry |
| Dataset ID | `kfm:dataset:water-planning:kwo-rac-regions` |
| Dataset version ID | `kfm:dataset-version:water-planning:kwo-rac-regions:2026-06-24` |
| Record status | `current` — the current internal pointer for this observed source version |
| Release status | `not-released` |
| Rights posture | `source-statement-recorded-review-pending` |
| Sensitivity posture | `public-administrative-boundary` |
| Local steward | **NEEDS VERIFICATION** |

### What belongs here

- the versioned GeoJSON payload named by the dataset registry record;
- a local README that explains the payload's bounded role, integrity,
  validation, correction, and release posture; and
- future successor payload versions only when their identity, lineage,
  registry metadata, validation, and correction posture are updated together.

### What does not belong here

| Excluded material or authority | Owning surface or required action |
|---|---|
| Source descriptors, dataset identities, or crosswalk identities | [`data/registry/`](../../../registry/) |
| Semantic meaning and anti-collapse rules | [`contracts/domains/water_planning/`](../../../../contracts/domains/water_planning/) |
| Machine-readable shapes | [`schemas/contracts/v1/domains/water_planning/`](../../../../schemas/contracts/v1/domains/water_planning/) |
| Validation code and regression tests | [`tools/validators/`](../../../../tools/validators/domains/water_planning/) and [`tests/`](../../../../tests/domains/water_planning/) |
| Proofs, policy decisions, release decisions, or published carriers | `data/proofs/`, `policy/`, `release/`, and `data/published/` |
| Guessed county membership, project location, or governance jurisdiction | Deny the inference; resolve through an applicable governed authority |

## Inventory

The current direct children are:

```text
rac_regions/
├── README.md
└── kwo_rac_regions_2026-06-24.geojson  # digest-pinned 14-feature payload
```

| Payload | Features | Size | Integrity and source version | Registry |
|---|---:|---:|---|---|
| [`kwo_rac_regions_2026-06-24.geojson`](./kwo_rac_regions_2026-06-24.geojson) | 14 | 9,995,739 bytes | SHA-256 `545b18b1b49a68c6359fefb80f8e8b80f885a94381dc87e0ef942eb8829cb738`; KWO item `cd87ef7a0bb34cc4a7f57e662d73ec0f`, layer `0`, modified `2026-06-24T15:17:37Z` | [`kwo_rac_regions_2026-06-24.json`](../../../registry/datasets/water_planning/kwo_rac_regions_2026-06-24.json) |

The registry record, not this prose table, is the machine-readable authority
for the payload path, byte count, digest, source observation, and release
posture.

## Geometry contract

The payload is a GeoJSON `FeatureCollection` with these pinned properties:

| Property | Bounded meaning |
|---|---|
| Geometry count and type | Exactly 14 `Polygon` or `MultiPolygon` features |
| Coordinate reference system | `OGC:CRS84` longitude/latitude |
| Coordinate handling | Retrieval requested ArcGIS `outSR=4326`; coordinates otherwise preserved without simplification |
| Feature order | `kwo-rac-01` through `kwo-rac-14` |
| Stable identity | KFM `region_id`, source-grounded `name`, and KFM `rac_number` ordinal |
| Source projection | Source feature ID, source name, and source abbreviation |
| Provenance | KWO item, owner, layer, modified time, CRS transform statement, and property-projection statement |

The numeric suffix in `kwo-rac-01` through `kwo-rac-14` is a stable KFM
ordinal. It is not represented as a KWO-native region number.

<details>
<summary>View the pinned 14-region identity inventory</summary>

| KFM ID | Source-grounded name |
|---|---|
| `kwo-rac-01` | Cimarron |
| `kwo-rac-02` | Equus-Walnut |
| `kwo-rac-03` | Great Bend Prairie |
| `kwo-rac-04` | Kansas |
| `kwo-rac-05` | Marais des Cygnes |
| `kwo-rac-06` | Missouri |
| `kwo-rac-07` | Neosho |
| `kwo-rac-08` | Red Hills |
| `kwo-rac-09` | Smoky Hill-Saline |
| `kwo-rac-10` | Solomon-Republican |
| `kwo-rac-11` | Upper Arkansas |
| `kwo-rac-12` | Upper Republican |
| `kwo-rac-13` | Upper Smoky Hill |
| `kwo-rac-14` | Verdigris |

</details>

## Source authority and lifecycle

| Surface | Role | Current posture |
|---|---|---|
| [KWO source descriptor](../../../registry/sources/water_planning/kwo_rac_feature_service.source.json) | Official administrative planning-boundary source | `proposed`, `needs_review`, connector `disabled`, `not_released` |
| [Processed GeoJSON](./kwo_rac_regions_2026-06-24.geojson) | Normalized internal geometry bytes | Digest-pinned `PROCESSED` payload |
| [Dataset registry record](../../../registry/datasets/water_planning/kwo_rac_regions_2026-06-24.json) | Stable dataset/version identity and payload metadata | `current`, `not-released` |
| [RAC geometry registry contract](../../../../contracts/domains/water_planning/rac_geometry_registry.md) | Semantic and derivation boundary | `PROPOSED`, source-grounded, not released |
| [Registry validator](../../../../tools/validators/domains/water_planning/validate_rac_registry.py) | Deterministic checked-in byte and metadata checks | Read-only and no-network |

The KWO source item was modified on `2026-06-24` and observed for this bounded
candidate on `2026-07-30`. Those dates identify the pinned observation; they
do not prove that the upstream source remains unchanged now. No recurring
connector or watcher is authorized by this directory.

The source's recorded statement says there are no special restrictions on the
content. KFM's independent rights review remains pending, so the payload stays
internal and `not-released` even though its sensitivity is classified as a
public administrative boundary.

## Related county crosswalk

The separate
[RAC-to-county crosswalk](../../../registry/crosswalks/water_planning/kwo_rac_counties_2026-06-24__tiger2025.json)
derives positive-area intersections between this KWO geometry and the U.S.
Census Bureau TIGERweb 2025 Kansas county geometry. It contains 209 retained
mappings across all 105 Kansas counties: 50 `dominant`, 122
`material-partial`, and 37 `boundary-sliver`.

These rows describe measured geometry overlap only. They do not establish
political, administrative, advisory, funding, or governance membership, and
they must not be used to infer project location.

## Validation

Run the deterministic registry validator from the repository root:

```bash
python tools/validators/domains/water_planning/validate_rac_registry.py
```

Expected success output:

```text
RAC_REGISTRY_OK regions=14 counties=105 mappings=209
```

Run the focused no-network regression suite:

```bash
python -m unittest discover \
  --start-directory tests/domains/water_planning \
  --pattern 'test_rac_registry.py' \
  --verbose
```

The validator and tests check:

- the payload byte count and SHA-256 digest;
- the exact 14-feature identity, name, order, coordinate, property, and
  provenance constraints;
- agreement among the payload, dataset record, crosswalk, and two source
  descriptors;
- all 105 Kansas county GEOIDs, the ordered 209-row mapping digest, overlap
  classes, and duplicate denial;
- disabled source connectors and the `not-released` posture; and
- deterministic, read-only, no-network behavior.

Changes under this directory are included in the read-only
[`briefing-integration`](../../../../.github/workflows/briefing-integration.yml)
workflow path filter. Its water-planning job runs the domain tests and the
canonical RAC registry validator with `contents: read`.

> [!WARNING]
> A pass proves only that checked-in bytes and metadata satisfy the validator's
> pinned rules. It does not refetch KWO or Census sources, recompute spatial
> intersections, prove freshness or completeness, clear rights, complete
> evidence review, or authorize release, deployment, public serving, or
> publication.

## Correction, review, and rollback

Treat a source refresh, payload replacement, identity change, geometry edit,
or crosswalk change as a governed baseline change:

1. record a new source observation and response digest;
2. create a new dataset version or an explicit correction with
   forward/backward lineage instead of silently overwriting history;
3. update the payload, dataset record, affected crosswalk metadata, source
   descriptors, validator baseline, and regression tests together;
4. rerun the focused validator and no-network tests; and
5. obtain the applicable domain, rights, evidence, and release reviews before
   any downstream public use.

The default GitHub review route is
[`@bartytime4life`](../../../../.github/CODEOWNERS), but CODEOWNERS routing is
not proof of independent review, policy approval, rights clearance, or release
authority. Local data stewardship remains **NEEDS VERIFICATION**.

For this Markdown-only update, rollback is a normal revert of the scoped
documentation commit. For a future payload correction, preserve the prior
version and digest, revert through reviewed history, and separately correct or
withdraw any downstream derived or released object.

## Related authority

| Surface | Responsibility |
|---|---|
| [`data/processed/`](../../README.md) | Parent lifecycle and authority contract |
| [Dataset registry record](../../../registry/datasets/water_planning/kwo_rac_regions_2026-06-24.json) | Dataset identity, version, payload digest, rights/sensitivity, and release posture |
| [County crosswalk record](../../../registry/crosswalks/water_planning/kwo_rac_counties_2026-06-24__tiger2025.json) | Derived county-intersection identity and measurements |
| [KWO source descriptor](../../../registry/sources/water_planning/kwo_rac_feature_service.source.json) | KWO source role, observation, access, rights, and activation posture |
| [Census source descriptor](../../../registry/sources/water_planning/census_tigerweb_counties_2025.source.json) | County-source role, vintage, observation, rights, and activation posture |
| [RAC geometry registry contract](../../../../contracts/domains/water_planning/rac_geometry_registry.md) | Semantic geometry and crosswalk boundary |
| [Water-planning schemas](../../../../schemas/contracts/v1/domains/water_planning/README.md) | Proposed machine shapes |
| [Registry validator](../../../../tools/validators/domains/water_planning/validate_rac_registry.py) | Deterministic finite checks |
| [Registry tests](../../../../tests/domains/water_planning/test_rac_registry.py) | No-network positive and negative regression evidence |
| [KWO source catalog entry](../../../../docs/sources/catalog/kansas/kwo.md) | Human-readable source family and bounded-admission context |
| [Directory Rules](../../../../docs/doctrine/directory-rules.md) | Placement and responsibility authority |
| [ADR-0029](../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adoption record for the canonical Directory Rules |

## Open verification items

| Item | Current state | Closure evidence |
|---|---|---|
| Upstream freshness after the pinned observation | **NEEDS VERIFICATION** | New bounded source observation and digest comparison |
| Independent KWO/Census rights review | **NEEDS VERIFICATION** | Recorded rights decision for the intended use |
| Water-planning domain review | **NEEDS VERIFICATION** | Recorded review against the contract and source roles |
| Local data steward and independent reviewer | **NEEDS VERIFICATION** | Verified responsibility assignments |
| Release and public-serving eligibility | `not-released` / **DENY BY DEFAULT** | Evidence, policy, review, release decision, correction path, and rollback target |

Unknowns narrow use; they do not authorize plausible defaults.

## Last evidence review

- **Date:** 2026-07-30
- **Repository checkpoint:** `main@af782516085171962c0063b688b3e0b42ee8523b`
- **Inspected evidence:** complete prior README; payload blob existence; dataset
  and crosswalk records; KWO and Census source descriptors; contract;
  validator; tests; path-triggered workflow; CODEOWNERS; Directory Rules; and
  ADR-0029.
- **Not performed:** live source refresh, spatial recomputation, rights
  decision, independent domain review, release decision, deployment, or
  publication.
- **Review trigger:** source, payload, identity, digest, geometry, crosswalk,
  contract/schema, validator, rights, sensitivity, writer, consumer, release,
  correction, rollback, or public-exposure change.

[Back to top](#top)
