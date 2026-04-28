# Ecology Sensitivity and Geoprivacy

This policy note defines publication-safe handling for ecological records.

## Sensitivity Classes

| Class | Summary | Public Geometry Policy |
|---|---|---|
| `public` | Low-risk records approved for normal disclosure. | Exact geometry may be published. |
| `generalize` | Moderate-risk records requiring reduced precision. | Publish only generalized geometry. |
| `restricted` | High-risk records (rare species/nests/private land concerns). | No public exact coordinates; withheld or coarse cell only. |
| `review_required` | Sensitivity unresolved. | Not publishable until steward review closes. |

## Generalization Methods

Approved geoprivacy methods include:

- Grid-cell rounding (e.g., 10km cell)
- Polygon aggregation to admin/eco region
- Coordinate jitter with minimum displacement threshold
- Geometry suppression with non-spatial summary only

Each transform should preserve:

- `generalization_method`
- `precision_served`
- `redaction_receipt_ref` (if available)

## Fail-Closed Conditions

A record must not be published if any of the following are true:

- sensitivity class is missing,
- rights status is unknown/restricted for publication,
- record carries exact geometry with `restricted` class,
- policy decision is `deny` or `hold`.

## Recommended Audit Fields

For every published ecology object, keep:

- policy id
- decision (`allow`, `generalize`, `deny`, `hold`)
- reviewer or automated gate id
- decision timestamp (UTC)
- source and dataset references
