# Georeference spatial-distribution source map

## Source seam

This slice is mined from the repository's IIIF/historic-map conformance guidance and the landed georeference transform-quality profile.

The IIIF guidance requires historic overlays to carry GCPs, uncertainty, and transform-quality information. The existing affine-quality validator recomputes residuals and leave-one-out residuals, but residual quality alone does not reveal whether all GCPs are clustered in one small part of the source image.

## Adapted idea

Add a second, independent fixture-only quality assessment that measures **resource-space control coverage** without opening imagery or executing a transform.

The profile uses deterministic geometry only:

- convex hull of GCP resource coordinates;
- hull-to-resource-mask area ratio;
- resource-mask vertex distance to the GCP hull as an extrapolation-risk proxy;
- GCP-centroid offset from resource-mask centroid; and
- quadrant occupancy.

## Deliberate boundaries

This adaptation does not:

- assert that a threshold is universally correct for production imagery;
- inspect target-space GCP coordinates;
- compare affine/projective/TPS models;
- authenticate GCP provenance;
- open or warp imagery;
- reproject coordinates;
- resolve the linked transform-quality record;
- evaluate rights, CARE, policy, evidence, review, promotion, release, or publication.

The thresholds are synthetic review-fixture policy only and remain `PROPOSED_INACTIVE`.

## Follow-up candidates

1. Bind the resource GCP set to the exact GCP set used by a reviewed transform-quality record through a deterministic set digest.
2. Add target-space distribution diagnostics only after a CRS/units contract is admitted.
3. Compare affine versus projective/TPS models in a separate numerical profile.
4. Add overlay-domain threshold profiles only after steward review and representative fixtures.
