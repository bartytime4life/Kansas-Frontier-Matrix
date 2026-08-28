# GeoreferenceControlPointEvidenceAssessment

`GeoreferenceControlPointEvidenceAssessment` is an inactive, fixture-only profile for recording whether a ground-control-point (GCP) set has reviewable evidence about target visibility, target contrast, marker scale, surveyed-coordinate source, and image matching.

The profile implements the narrow evidence-quality seam identified by `KFM-P18-INV-317`. It complements rather than replaces the existing `GeoreferenceControlPointSet`, `GeoreferenceSpatialDistribution`, and `GeoreferenceTransformQuality` profiles.

## Inputs and boundaries

The candidate binds an existing `control_point_set_ref` but never dereferences it. Each point repeats only the upstream point ID and qualitative evidence observations; coordinates remain owned by the control-point-set profile.

The candidate records:

- a declared surveyed-coordinate method and evidence reference;
- a declared image-matching method and evidence reference;
- per-point visibility, contrast, marker-scale, and match-review states;
- per-point evidence references and one canonical aggregate evidence-reference list; and
- deterministic summary counts, `spec_hash`, and `assessment_id` values.

The initial profile intentionally does not set a public-geometry adequacy threshold. `PASS` means only that a synthetic candidate is internally coherent and ready for human review under this fixture profile. `ABSTAIN` preserves unknown, partial, or unreviewed evidence without guessing. `DENY` identifies internally declared adverse states or coherence failures. `ERROR` is reserved for invalid input, schema, or deterministic identity.

## Deterministic identity

`spec_hash` is the SHA-256 digest of canonical JSON after removing only `assessment_id` and `spec_hash`. `assessment_id` is the first 24 hexadecimal characters of that digest prefixed with `gcp-evidence-assessment:`.

Point IDs and `evidence_refs` MUST be unique and lexicographically ordered. Summary counts MUST be recomputable from the point observations. Every non-null evidence reference MUST appear in the canonical `evidence_refs` array.

## Trust boundary

Validation does not open imagery, resolve references, contact a GNSS service, verify surveyed coordinates, inspect marker pixels, match photographs, measure accuracy, assess GCP distribution, compute a transform, evaluate residuals, evaluate policy or rights, approve human review, or authorize promotion, release, publication, or public use.

A green result is not evidence that a real GCP, coordinate, image, transform, or public geometry is accurate or admissible.
