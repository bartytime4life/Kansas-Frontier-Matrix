# Geology public-safe geometry assessment contract

Status: **PROPOSED fixture profile**

Profile: `kfm-geology-public-safe-geometry-fixture-v1`

Schema: `schemas/contracts/v1/domains/geology/public_safe_geometry_assessment.schema.json`

## Purpose

`GeologyPublicSafeGeometryAssessment` is a closed, synthetic, metadata-only
preflight for one proposed Geology geometry disposition on a public map, API,
or export surface. It tests whether declared exact/internal geometry remains
restricted and whether the public disposition is generalized, withheld, or an
exact request that must be denied.

The profile carries opaque fixture references, CRS labels, scale denominators,
governance summaries, and a deterministic assessment. It contains no
coordinates or geometry bytes and does not execute a geometry transform.

## Deterministic outcomes

| Disposition | Profile outcome | Meaning |
|---|---|---|
| `GENERALIZED` | `HOLD` | The candidate is internally consistent, but release and publication remain separate, unwired gates. |
| `WITHHELD` | `DENY` | No public geometry may be served for this request. |
| `EXACT_REQUEST` | `DENY` | Exact public geometry is denied even when the request is represented only by an opaque fixture reference. |

Any schema, identity, sensitivity, transform-receipt, rights, review, policy,
scale, uncertainty, or authority inconsistency also fails closed as `DENY`.
`HOLD` does not mean that a transform occurred or that a real policy, review,
release, or publication decision exists.

## Bounded object-family mapping

The fixture profile freezes these repository-grounded safety classes:

| Object family | Expected sensitivity class |
|---|---|
| `BoreholeReference` | `EXACT_SUBSURFACE` |
| `GeochemistrySample` | `SAMPLE_LOCALITY` |
| `MineralOccurrence` | `RESOURCE_TARGET` |
| `ResourceDeposit` | `RESOURCE_TARGET` |
| `GeologyBoundaryVersion` | `CANONICAL_BOUNDARY` |

This mapping is a test profile, not a complete sensitivity registry or a
canonical Geology vocabulary.

## Required separation

- Exact source geometry is represented only by an opaque fixture reference,
  must declare `INTERNAL_EXACT`, and must remain `RESTRICTED`.
- No fixture may contain coordinates, bounding boxes, centroids, or equivalent
  location material.
- A generalized candidate needs a synthetic transform-receipt reference,
  verified-rights summary, generalized-policy summary, approved-review summary,
  coarser public scale, and uncertainty disclosure.
- A withheld candidate carries no public geometry reference.
- The profile always declares `NOT_RELEASED`, `publication_authorized: false`,
  and assessment authority `NONE`.

## Responsibility signature

| Responsibility | Owner |
|---|---|
| Semantic meaning | `contracts/domains/geology/` |
| Machine shape | `schemas/contracts/v1/domains/geology/` |
| Synthetic fixture inputs | `fixtures/contracts/v1/domains/geology/public_safe_geometry/` |
| Deterministic validation | `tools/validators/geology/public_safe_geometry/` |
| Regression tests | `tests/domains/geology/` |
| Policy, sensitivity, review, receipts, release, and publication | Their existing owning roots; not this profile |

## Non-effects

Validation does not read exact geometry, transform coordinates, resolve source
rights, evaluate live policy, authenticate receipt or review references, create
a release manifest, write lifecycle state, serve a map, authorize export, or
publish anything. A green workflow proves only deterministic fixture behavior.

## Source basis

The source-to-repository mapping and truth labels are recorded in
`docs/intake/exploratory/geology-public-safe-geometry-source-map.md`.
