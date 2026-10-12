<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/new-ideas-2-spatial-geometry-property-validation-source-map
title: New Ideas 2 - Spatial Geometry Property Validation Source Map
type: exploratory-intake-source-map
version: v0.1.0
status: implemented-proposal; review-required; non-authoritative
owners: OWNER_TBD - Geometry steward; schema steward; validation steward; policy steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; intake; exploratory; geometry; hostile-input; validation
truth_posture: CONFIRMED private-source extraction and repository-gap reconciliation / PROPOSED bounded validator profile / NEEDS VERIFICATION hosted exact-head validation and steward acceptance
owning_root: docs/
responsibility: Privacy-minimized reconciliation of the private New Ideas 2 hostile-geometry property-testing proposal with the existing SpatialGeometry contract, schema, placeholder validator, accepted fixture lane, dependency posture, and geometry authority boundaries.
source_class: connected private document
source_title: New Ideas 2
source_section: property-based hostile-geometry validation harness
source_status: non-authoritative exploratory proposal
source_disclosure: privacy-minimized; full text, code sample, connector locator, private link, timestamps, digest, and file size omitted
repository: bartytime4life/Kansas-Frontier-Matrix
repository_snapshot: e663400eddaef042486dfe73ae558e6d0d9e4694
repository_verified_on: 2026-08-10
related:
  - ./README.md
  - ../../../contracts/common/spatial_geometry.md
  - ../../../schemas/contracts/v1/common/spatial_geometry.schema.json
  - ../../../fixtures/contracts/v1/common/spatial_geometry/README.md
  - ../../../fixtures/contracts/v1/common/spatial_geometry/cases.json
  - ../../../tools/validators/validate_spatial_geometry.py
  - ../../../tools/validators/geometry/README.md
  - ../../../tests/validators/test_validate_spatial_geometry.py
  - ../../../pyproject.toml
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, geometry, property-testing, hostile-input, hypothesis, deterministic, fail-closed, abstain]
notes:
  - "The source is evidence that generated hostile geometries and invariant-oriented tests were proposed; it is not evidence that its code, libraries, paths, repair operations, or assumptions are safe or implemented."
  - "This slice retains generated property testing but does not copy the source sample, add Shapely, implement MakeValid, snap coordinates, transform CRS, or add WKT/WKB conversion behavior."
  - "Current-repository conclusions are limited to the pinned main snapshot; hosted exact-head CI remains NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# New Ideas 2 - spatial geometry property validation source map

> **Outcome:** the inspected repository already declared one shared
> `SpatialGeometry` contract, schema, fixture root, and validator path, but the
> validator was an executable placeholder and the fixture root had no reviewed
> hostile-input profile. This slice implements that existing owner with bounded,
> deterministic carrier checks and generated property tests. It creates no
> second geometry authority.

> [!CAUTION]
> The connected source's sample code and third-party geometry stack are not
> adopted. Generated language and sample code do not outrank repository
> contracts, dependency boundaries, sensitivity rules, or review.

## Source boundary and method

| Field | Bounded value |
|---|---|
| Supplied title | *New Ideas 2* |
| Reviewed cluster | Property-based hostile-geometry validation harness |
| Source posture | Non-authoritative exploratory proposal |
| Repository comparison | `main@e663400eddaef042486dfe73ae558e6d0d9e4694`, inspected `2026-08-10` |
| Private material | Full text, sample code, Drive locator, private link, connector metadata, digest, and file size omitted |

The source was treated as idea evidence only. Current repository files, accepted
Directory Rules, dependency declarations, and executable gaps determined the
scope. No source data, real location, or private coordinate was copied.

## Repository-grounded reconciliation

| Source pressure | Current repository evidence | Disposition |
|---|---|---|
| Generate malformed, degenerate, and edge-case geometries | The shared contract named coordinate order, dimensionality, ring closure, topology, and validity as open checks; its declared validator raised `NotImplementedError`. | `RETAIN` as bounded carrier validation. |
| Store failing examples for reproducibility | The schema already declared `fixtures/contracts/v1/common/spatial_geometry/`, but no reviewed profile was present at the pinned snapshot. | `RETAIN` as synthetic exact-polarity cases plus deterministic generated seeds. |
| Use property-oriented invariants | The root test dependencies provided pytest only; no property-test library was declared. | `RETAIN` through a bounded Hypothesis test dependency and focused generated tests. |
| Use Shapely operations such as MakeValid, grid snapping, and WKB/WKT round trips | No accepted Shapely dependency or implemented shared geometry package was established; the common contract explicitly excludes repair and transformation. | `DEFER / REJECT FROM THIS OWNER`. |
| Treat geometric validity as correctness | KFM doctrine and the contract separate carrier validation from source, evidence, domain, survey, policy, review, and release authority. | `DENY`. |
| Copy paths and sample implementation from the source | The source paths and code were not repository evidence and included assumptions not accepted by current contracts. | `REJECT`. |

This is distinct from the geometry-delta review seam: this validator checks one
carrier's bounded structure. It neither compares baseline and candidate states
nor decides materiality.

## Directory Rules and authority basis

Accepted [Directory Rules v2](../../doctrine/directory-rules.md), adopted through
[ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md), place
artifacts by responsibility:

| Responsibility | Existing owner used by this slice |
|---|---|
| Shared geometry meaning | [`contracts/common/spatial_geometry.md`](../../../contracts/common/spatial_geometry.md) |
| Machine shape | [`schemas/contracts/v1/common/spatial_geometry.schema.json`](../../../schemas/contracts/v1/common/spatial_geometry.schema.json) |
| Reusable synthetic cases | [`fixtures/contracts/v1/common/spatial_geometry/`](../../../fixtures/contracts/v1/common/spatial_geometry/README.md) |
| Repository-wide validator | [`tools/validators/validate_spatial_geometry.py`](../../../tools/validators/validate_spatial_geometry.py) |
| Executable conformance | [`tests/validators/test_validate_spatial_geometry.py`](../../../tests/validators/test_validate_spatial_geometry.py) |
| Test dependency declaration | [`pyproject.toml`](../../../pyproject.toml) |
| Private-source reconciliation | This file under `docs/intake/exploratory/` |

No new root, schema family, geometry-repair package, policy bundle, proof store,
receipt store, lifecycle lane, release family, or public route is introduced.

## Implemented bounded profile

The proposed validator profile checks:

- strict UTF-8 JSON with duplicate-key, non-finite-number, symlink, size, and
  schema-failure handling;
- the current Draft 2020-12 schema;
- `Point`, `MultiPoint`, `LineString`, `MultiLineString`, `Polygon`, and
  `MultiPolygon` coordinate structures;
- finite, consistently 2D or 3D positions;
- minimum line and polygon-ring cardinality;
- closed, non-degenerate polygon rings and detected simple-ring
  self-intersections;
- uppercase `EPSG:<positive integer>` identifier syntax;
- longitude/latitude bounds for declared `EPSG:4326`; and
- stable finding codes and JSON pointers without echoing coordinate values.

The schema remains unchanged and more permissive than this validator profile.
That distinction is deliberate and review-significant: schema-valid does not
mean profile-valid, and profile-valid does not mean correct or publishable.

## Generated property profile

Focused Hypothesis tests use fixed replay seeds and bounded example counts to
exercise properties, not a list of hand-picked samples only:

| Generated property | Expected invariant |
|---|---|
| Finite in-bounds points | Pass the bounded carrier profile. |
| Unique finite lines with at least two positions | Pass without repair or normalization. |
| Closed synthetic rectangles | Pass simple-ring checks. |
| The same rectangles with closure removed | Fail with `POLYGON_RING_OPEN`. |
| Longitudes outside EPSG:4326 bounds | Fail with `COORDINATE_OUT_OF_BOUNDS`. |
| Repeated validation of the same generated carrier | Produce byte-identical diagnostics. |
| Generated coordinate values | Never appear in diagnostics. |

Reviewed fixtures additionally cover unsupported types, malformed positions,
short lines, bow-tie rings, mixed dimensions, invalid CRS syntax, collinear
rings, and schema-forbidden top-level fields. Duplicate keys and non-finite JSON
numbers are exercised through raw hostile files.

## Explicit non-effects and deferred work

A passing result does **not**:

- repair topology, snap coordinates, transform CRS, or convert WKT/WKB;
- resolve whether an EPSG code exists, is suitable, or has the declared axis
  order or units;
- prove hole containment, polygon-to-polygon relationships, manifold topology,
  survey quality, spatial accuracy, source authority, or domain truth;
- resolve an `EvidenceRef` to an `EvidenceBundle`;
- evaluate rights, sovereignty, sensitivity, geoprivacy, consent, or living-
  person exposure;
- decide policy, approve review, mutate lifecycle state, promote, release,
  deploy, publish, or authorize public use; or
- make AI-generated language or a passing test sovereign truth.

Shapely-backed repair and transformation invariants remain deferred until an
accepted package owner, dependency/security review, operation contract,
provenance receipt, and rollback behavior exist. They must not be smuggled into
carrier validation as convenience helpers.

## Validation and review posture

Local validation must include schema self-check, exact fixture replay, focused
generated tests, deterministic diagnostics, source-code compilation, dependency
policy checks, workflow syntax, documentation metadata/links, and exact diff
scope. Hosted exact-head checks remain `NEEDS VERIFICATION` until GitHub Actions
completes.

Human review should focus on:

1. whether the validator's stricter supported-type profile is compatible with
   the intentionally open current schema;
2. whether EPSG identifier syntax without registry resolution is sufficiently
   narrow and clearly labeled;
3. whether polygon checks avoid implying complete computational topology;
4. whether property-test dependency bounds fit repository dependency policy;
5. whether diagnostics remain safe for sensitive geometry; and
6. whether future repair/transform behavior stays in a separate accepted owner.

## Rollback and correction

Before merge, close the draft pull request and abandon its isolated branch.
After an authorized merge, revert the additive fixture, test, workflow, source-
map, and dependency changes and restore the prior validator/contract/README
bytes through a reviewed corrective pull request. No source, real geometry,
lifecycle record, policy decision, release, deployment, or published artifact
requires restoration.

[Back to top](#top)
