# GeoreferenceSpatialDistributionAssessment

`GeoreferenceSpatialDistributionAssessment` is a fixture-first, source-agnostic quality record for the **resource-space arrangement of ground control points (GCPs)** used by a georeference transform.

It complements, but does not replace, `GeoreferenceTransformQualityAssessment`. Residual error answers whether a fitted transform agrees with the supplied control points; this profile asks whether those control points are spatially distributed well enough to reduce interpolation/extrapolation risk across the declared resource mask.

## Scope

The assessment is inactive and no-network. It operates only on committed synthetic resource coordinates and a declared resource mask. It computes:

- the convex-hull vertex count for unique GCP resource points;
- GCP convex-hull area divided by resource-mask area;
- maximum normalized distance from any resource-mask vertex to the GCP hull (`max_extrapolation_ratio`);
- normalized offset between the resource-mask centroid and mean GCP centroid; and
- the number of occupied resource-space quadrants around the resource-mask centroid.

All ratios are recomputed and compared to six-decimal, round-half-even declarations.

## Finite outcomes

- `READY` — the GCP set is nondegenerate, satisfies minimum count, hull coverage, extrapolation, centroid-offset, and quadrant thresholds.
- `HOLD` — the geometry is valid but one or more distribution thresholds are not met.
- `ERROR` — malformed shape, count drift, duplicate points, open/degenerate/self-intersecting mask, out-of-mask GCP, degenerate GCP hull, metric mismatch, or claimed-decision mismatch.

Reason-code ordering is deterministic.

## Trust boundary

A `READY` result is **not** georeference truth. It does not authenticate GCPs, prove historical alignment, calculate an image warp, reproject coordinates, establish transform accuracy, evaluate rights/CARE/policy, close evidence, or authorize promotion, release, publication, or public use.

`transform_quality_ref` is carried only as a linkage declaration. This validator does not dereference or authenticate that record.

## Relationship to adjacent profiles

A future integration may require both:

1. an acceptable `GeoreferenceTransformQualityAssessment` for residual behavior; and
2. an acceptable `GeoreferenceSpatialDistributionAssessment` for resource-space control coverage.

Neither profile should be collapsed into source admissibility, rights, evidence, review, or release authority.
