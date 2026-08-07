# GeoreferenceControlPointSet

`GeoreferenceControlPointSet` is a fixture-first identity envelope for the exact ground-control-point (GCP) set used by georeference quality assessments.

The object exists to prevent adjacent validators from silently evaluating different point sets. It canonically binds point IDs, image-resource coordinates, target coordinates, resource dimensions, and target-unit semantics into deterministic SHA-256 identities.

## Deterministic identities

The profile computes three related identities:

- `resource_set_hash` binds point IDs plus image-resource coordinates and resource dimensions;
- `target_set_hash` binds point IDs plus target coordinates and target-unit declaration; and
- `set_id` binds both coordinate-space declarations and every full GCP tuple.

Point IDs MUST be unique and lexicographically ordered. Resource and target coordinates MUST be unique within the set. JSON numeric spelling is not identity-bearing: coordinates are normalized to canonical decimal strings before hashing.

## Coordinate posture

This initial inactive profile intentionally supports only fixture coordinate systems already used by neighboring tests:

- resource coordinates are image pixels with explicit width and height; and
- target coordinates use `synthetic_meters` or `synthetic_feet`.

No CRS, datum, epoch, axis transformation, or geodetic interpretation is implied.

## Finite validation

- `VALID` means the record has a reproducible canonical identity and internally coherent declarations.
- `ERROR` means shape, ordering, uniqueness, bounds, count, digest, or claimed-decision validation failed.

## Trust boundary

A valid control-point-set identity is not evidence that the GCPs are accurate, admissible, independently sourced, or appropriate for a transform. The profile does not open imagery, georeference or warp data, evaluate residuals or spatial distribution, resolve EvidenceBundles, evaluate rights/CARE/policy, or authorize lifecycle promotion, release, publication, or public use.
