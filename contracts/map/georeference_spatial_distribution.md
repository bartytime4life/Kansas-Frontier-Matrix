<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/map/georeference-spatial-distribution
title: GeoreferenceSpatialDistributionAssessment
type: contract
version: v0.2.0
status: proposed-inactive; fixture-only; repository-grounded
owners: OWNER_TBD — Map-quality steward · Contract steward · Validation steward
updated: 2026-09-08
owning_root: contracts/
evidence_snapshot: 6087d07b49362540e437dc666d1cbaa6eb6b82c3
prior_blob: 1577902afa7420c3b05874d17661f02a52b64647
policy_label: repository-facing; synthetic; non-publisher
related:
  - ./README.md
  - ./georeference_control_point_set.md
  - ./georeference_control_point_evidence_assessment.md
  - ./georeference_transform_quality.md
  - ../../schemas/contracts/v1/map/georeference_spatial_distribution.schema.json
  - ../../tools/validators/map/validate_georeference_spatial_distribution.py
  - ../../fixtures/contracts/v1/map/georeference_spatial_distribution/cases.json
  - ../../tests/map/test_georeference_spatial_distribution.py
  - ../../.github/workflows/map-georeference-spatial-distribution.yml
notes:
  - "Documentation edition only; machine schema_version remains 1.0.0."
  - "Numerical declarations and thresholds do not authenticate GCPs or authorize public use."
[/KFM_META_BLOCK_V2] -->

# GeoreferenceSpatialDistributionAssessment

`GeoreferenceSpatialDistributionAssessment` is a fixture-first, source-agnostic
quality record for the **resource-space arrangement of ground control points
(GCPs)**. It complements transform residual checks with bounded distribution
proxies; it does not measure historical or geodetic accuracy.

**Status:** the [schema](../../schemas/contracts/v1/map/georeference_spatial_distribution.schema.json)
remains `PROPOSED_INACTIVE`. Its validator, fixtures, tests, and workflow exist at
`main@6087d07b49362540e437dc666d1cbaa6eb6b82c3`, inspected on 2026-09-08 UTC.
Implemented fixture mathematics, an accepted operational profile, and permission
to publish are separate claims. This revision changes no numerical behavior.

[Scope](#scope) · [Fields](#required-fields) · [Metrics](#metric-definitions) ·
[Outcomes](#finite-outcomes) · [Trust boundary](#trust-boundary) ·
[Adjacent profiles](#relationship-to-adjacent-profiles) ·
[Validation](#validation) · [Rollback](#rollback)

## Scope

The inactive profile uses synthetic resource coordinates and a declared mask in
one image-resource plane. It opens JSON, not imagery, and does not inspect target
coordinates, fit a transform, warp pixels, reproject, or contact a service.
`fixture_only: true` is a required declaration, not authentication that supplied
coordinates came from a synthetic source. Operational source use is not admitted.

The [validator](../../tools/validators/map/validate_georeference_spatial_distribution.py)
recomputes the GCP hull, hull/mask area ratio, mask-vertex extrapolation proxy,
centroid offset, and quadrant occupancy. It compares these with the supplied
metrics and checks the declared decision. It does not repair input declarations.

### Required fields

All fourteen top-level fields are mandatory. The schema closes the top-level
object and nested records against additional properties.

| Field or group | Current machine requirement and meaning |
| --- | --- |
| `object_type`, `schema_version`, `profile` | Constants `GeoreferenceSpatialDistributionAssessment`, `1.0.0`, and `kfm.georeference.spatial-distribution.v1`. |
| `fixture_only`, `network_access` | Constants `true` and `forbidden`. |
| `assessed_at` | Date-time string checked with a format checker; not image acquisition, source publication, or release time. |
| `transform_quality_ref` | String of 1–256 characters; linkage declaration only, not a resolved or authenticated assessment. |
| `support` | Integer `resource_width_px` and `resource_height_px`, each 1–1,000,000; a `resource_mask` ring of 4–257 coordinate pairs. |
| `gcp_count`, `gcps` | Count and array length each 3–256; validator requires equality. Each GCP has an `id` of 1–80 characters and a two-number `resource` pair. |
| `thresholds` | Five explicit thresholds below; no omitted/default threshold is supplied by the validator. |
| `computed` | All five recomputable metrics below. |
| `decision` | `outcome` and 1–16 unique uppercase reason tokens; exact outcome, reasons, and order must match derivation. |
| `governance` | Six false authority flags and null `release_ref`, detailed under Trust boundary. |

The mask must close explicitly, have at least three distinct non-closing
vertices and positive area, pass the implemented self-intersection check, and
stay within the resource rectangle. The rectangle uses `[0, width]` and
`[0, height]`, not a pixel-index maximum of `width - 1` or `height - 1`.
GCP resource coordinates must be distinct and inside or on the mask boundary.
The hull must be nondegenerate. Geometry comparisons use the implementation's
`EPS = 1e-24`; that tolerance is not an accuracy or precision guarantee.

**Identity limitation:** this profile does not enforce unique or sorted GCP IDs.
It has no `set_id`, `resource_set_hash`, `spec_hash`, or `control_point_set_ref`
field. Do not borrow identity guarantees from the adjacent control-point-set
contract or add those fields to a v1 instance; additional fields are rejected.

### Metric definitions

Let `M` be the mask polygon, `H` the convex hull of the unique resource points,
`C_M` the area-weighted polygon centroid, and `C_G` the arithmetic mean of **all**
GCP resource points. Let `D` be the diagonal length of the mask's axis-aligned
bounding box. `D` is not necessarily the full image-resource diagonal.

| `computed` field | Implemented calculation |
| --- | --- |
| `hull_vertex_count` | Number of vertices retained by the monotone-chain GCP hull; not the total GCP count. |
| `hull_area_ratio` | `area(H) / area(M)`. The hull is not clipped to the mask. |
| `max_extrapolation_ratio` | Maximum distance from a listed non-closing mask vertex to the filled GCP hull, divided by `D`. Distance is zero inside/on the hull; otherwise it is the minimum point-to-hull-edge distance. |
| `centroid_offset_ratio` | Euclidean distance from `C_M` to `C_G`, divided by `D`. It does not use the hull centroid. |
| `occupied_quadrants` | Distinct sign pairs around `C_M`. A point within `EPS` of either centroid axis contributes no quadrant. |

These are dimensionless resource-space diagnostics. In particular,
`hull_area_ratio` is **not a clipped coverage percentage**: for a concave mask,
the hull can bridge excluded space and the ratio can exceed one. The computed
schema has no upper bound of one for this field. The extrapolation
proxy evaluates mask vertices; it does not evaluate a warped image or provide a
positional-error estimate. Quadrant occupancy does not prove uniform sampling.

### Rounding and thresholds

The validator converts parsed numbers through `Decimal(str(value))`. The three
ratios are quantized to `0.000001` using `ROUND_HALF_EVEN`, converted to floats,
and compared numerically with `computed`; counts compare as integers. This is
not a requirement to spell every JSON number with six trailing decimal places.
The JSON reader first parses floating-point tokens as finite floats, so the
profile does not promise preservation of arbitrary decimal-token precision.

**Threshold comparisons use the unrounded metrics**, not the rounded declarations.
Minimum checks fail on `<`; maximum checks fail on `>`. Equality passes.
All failing threshold reasons are accumulated and sorted.

| Threshold | Schema constraint | Baseline fixture value |
| --- | --- | ---: |
| `minimum_gcps` | Fixed at `4`; three nondegenerate points can be shape-valid but still yield `HOLD`. | 4 |
| `min_hull_area_ratio` | Number in `[0, 1]`. | 0.35 |
| `max_extrapolation_ratio` | Number in `[0, 1]`. | 0.2 |
| `max_centroid_offset_ratio` | Number in `[0, 1]`. | 0.15 |
| `minimum_occupied_quadrants` | Integer from 1 through 4. | 4 |

These values are synthetic fixture choices, **not universally accepted
georeferencing thresholds**. Caller-declared thresholds are not checked against
an independently approved threshold registry. Representative-data qualification
and steward approval remain future work, as recorded in the
[source map](../../docs/intake/exploratory/georeference-spatial-distribution-source-map.md).

## Finite outcomes

| Assessment outcome | Meaning within this inactive profile |
| --- | --- |
| `READY` | Shape, geometry, metric declarations, decision declarations, and all supplied thresholds agree. Reason: `GCP_SPATIAL_DISTRIBUTION_READY`. |
| `HOLD` | Coherent geometry and declarations fail one or more supplied thresholds. Reasons are a sorted subset of `INSUFFICIENT_GCPS`, `HULL_COVERAGE_LOW`, `EXTRAPOLATION_RISK_HIGH`, `CENTROID_OFFSET_HIGH`, and `QUADRANT_COVERAGE_LOW`. |
| `ERROR` | Input, shape, count, geometry, metric, or decision checking fails. No readiness claim is made. |

Validation order matters. A non-object yields `ROOT_NOT_OBJECT`; schema failure
or an unavailable schema yields `SCHEMA_INVALID`. Derivation then checks count,
geometry, metric equality, and thresholds in that order. Geometry diagnostics
include `RESOURCE_MASK_OPEN`, `RESOURCE_MASK_DEGENERATE`,
`RESOURCE_MASK_SELF_INTERSECTION`, `RESOURCE_MASK_OUT_OF_BOUNDS`,
`DUPLICATE_RESOURCE_GCP`, `GCP_OUTSIDE_RESOURCE_MASK`, and `GCP_HULL_DEGENERATE`.
Count and metric discrepancies yield `GCP_COUNT_MISMATCH` and `METRIC_MISMATCH`.

Finally, the declared decision must equal the derived result, including reason
order. Otherwise the outward result is `ERROR / DECISION_MISMATCH`, even when
derivation found another error. For example, a duplicate-coordinate candidate
still claiming `READY` reports decision mismatch rather than automatically
rewriting its declaration to `DUPLICATE_RESOURCE_GCP`.

File reading separately reports missing/unreadable, oversized, symlinked,
non-UTF-8, duplicate-key, invalid JSON, non-finite-number, and excessive-complexity
input errors. The reader uses a 1 MiB file-size precheck. These checks are not a
claim of complete filesystem-race protection or an operating-system sandbox.

## Trust boundary

A `READY` result is **not georeference truth**. It does not authenticate GCPs,
prove historical alignment, calculate an image warp, establish transform accuracy,
evaluate rights/CARE/policy, resolve evidence, or authorize promotion, release,
publication, or public use. `transform_quality_ref` is not dereferenced.

The schema fixes `authority_created`, `policy_evaluated`,
`promotion_authorized`, `release_authorized`, `publication_authorized`, and
`public_use_allowed` to `false`; `release_ref` remains `null`.

The lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This validator performs none of those transitions. Public use still requires
identity, rights, sensitivity, validation, provenance, integrity, evidence/proof,
policy, review, release, correction, and rollback checks. Evidence-dependent
claims require `EvidenceRef -> EvidenceBundle` resolution elsewhere. Public
clients use governed APIs or released artifacts, not internal/unreleased stores.
MapLibre displays, tiles, overlays, exports, and AI summaries remain carriers,
not evidence or approval authorities. Use only synthetic examples in this lane;
a numeric quality result cannot make sensitive control points public-safe.

## Relationship to adjacent profiles

| Existing profile | Separate responsibility |
| --- | --- |
| [GeoreferenceControlPointSet](./georeference_control_point_set.md) | Exact ordered point identity, resource/target coordinates, and lane-specific hashes. This distribution schema does not consume those hashes. |
| [GeoreferenceControlPointEvidenceAssessment](./georeference_control_point_evidence_assessment.md) | Qualitative visibility, contrast, marker-scale, coordinate-source, and image-matching declarations; not distribution mathematics. Its `PASS / ABSTAIN / DENY / ERROR` vocabulary is separate. |
| [GeoreferenceTransformQualityAssessment](./georeference_transform_quality.md) | Synthetic affine fit and residual/leave-one-out behavior; not spatial coverage or source authentication. |

**PROPOSED integration:** require suitable distribution and residual assessments
for the same demonstrably bound GCP set, plus the separate evidence and governance
gates. The existence of both assessments or a shared-looking reference does not
prove that their points, source version, resource dimensions, or transform agree.
This revision adds no adapter, resolver, canonical set binding, or public route.

## Validation

The [test module](../../tests/map/test_georeference_spatial_distribution.py)
contains 11 focused tests. The
[fixture matrix](../../fixtures/contracts/v1/map/georeference_spatial_distribution/cases.json)
contains 11 cases: one `READY`, three `HOLD`, and seven `ERROR`. It covers the
baseline, clustered/asymmetric/three-point cases, duplicate/outside/collinear
points, open/self-intersecting masks, metric drift, and decision drift.
This is a bounded inventory, not exhaustive hostile-input or geometry coverage.

The baseline's five GCPs on a 1000-by-800 rectangular resource produce:
`hull_vertex_count=4`, `hull_area_ratio=0.7875`,
`max_extrapolation_ratio=0.055216`, `centroid_offset_ratio=0`, and
`occupied_quadrants=4`. Those values describe synthetic input only.

From a provisioned repository root, the existing focused commands are:

```bash
python -m pytest -q tests/map/test_georeference_spatial_distribution.py
python tools/validators/map/validate_georeference_spatial_distribution.py --fixtures
```

For explicit files, the CLI exits `0` only when every result is `READY`; any
`HOLD` or `ERROR` exits `1`. Invalid command usage exits `2`. In contrast,
`--fixtures` exits `0` when all expected outcomes match and all three outcome
classes occur, including correctly held and erroneous fixtures. It cannot be
combined with explicit files. Fixture success is not universal readiness.

The [dedicated workflow](../../.github/workflows/map-georeference-spatial-distribution.yml)
selects this contract in its PR/main-push path filters, runs the focused tests and
fixture replay, and checks generated-receipt integrity. Its definition is not a
hosted pass or proof of required-check enforcement. The accompanying delivery
record distinguishes executed checks, environment limits, hosted results, and
pending independent review. No prior test result is inherited as current proof.

## Placement and evidence basis

This is a same-path clarification of an existing numerical contract under
`contracts/`, the semantic-meaning responsibility root in
[Directory Rules](../../docs/doctrine/directory-rules.md), adopted by
[ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md).
The [map-family README](./README.md) retains compatibility/placement questions;
this edit does not declare the whole family canonical, move it, or create a
parallel schema, policy, proof, or release home.

The paired schema, validator, fixtures, tests, workflow, source map, and adjacent
contracts linked above were inspected at the evidence snapshot. Their current
bytes govern machine-behavior descriptions; source-map proposals do not establish
operational adoption. The generated receipt belongs in the existing
`data/receipts/generated/` lane. A bounded workflow receipt-reference update keeps
current integrity checking separate from the retained historical authoring receipt.

## Rollback

The prior document is nonblank blob
`1577902afa7420c3b05874d17661f02a52b64647` at the evidence snapshot. Before
integration, retain or abandon the isolated branch under the delivery controls.
After separately authorized integration, use a reviewed forward correction or
revert of the document and its coupled workflow reference. Preserve historical
receipts and distinguish obsolete bindings from a current integrity check.
No reset, force-push, source activation, data migration, warp reversal, cache
purge, release withdrawal, or public-state mutation follows from this edit.

Remaining qualification work includes exact GCP-set/assessment binding, reviewed
threshold profiles, full numerical/geometry edge coverage, operational evidence
resolution, rights/sensitivity decisions, and independent stewardship. None is
completed by documenting or validating this fixture profile.
