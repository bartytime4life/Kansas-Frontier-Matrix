# Georeference transform-quality — source map

Status: `PROPOSED_INACTIVE`

## Mined need

`docs/standards/IIIF.md` requires historic-map overlays to record GCPs, transform method, uncertainty, and where possible a quantitative transform RMS. The IIIF readiness slice intentionally carries those declarations without calculating them. Repository search at authoring time found no executable GCP/RMS transform-quality validator.

## Adaptation

This slice extracts the math into a source-agnostic `GeoreferenceTransformQualityAssessment` rather than coupling it to IIIF, Allmaps, one archive, or one renderer.

It deterministically fits a 2D affine model using committed synthetic points, measures in-sample and leave-one-out residuals, checks redundancy and threshold posture, and verifies that the candidate's declared metrics match recomputation.

## Deliberate limits

- Synthetic planar coordinates only; no CRS library or reprojection.
- Affine transform only; no polynomial/TPS/projective implementation.
- No imagery, map warp, visual inspection, historical interpretation, or geodetic truth claim.
- No source, evidence, rights, CARE, policy, release, or public-use authority.

## Follow-up candidates

1. Cross-validation profile comparison for affine vs projective/TPS when an admitted numerical dependency exists.
2. GCP spatial-distribution diagnostics (convex-hull coverage and edge extrapolation risk).
3. Binding an accepted quality result into the IIIF historic-overlay readiness profile after both profiles are independently reviewed.
