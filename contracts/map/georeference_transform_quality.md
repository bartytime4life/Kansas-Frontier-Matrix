# Georeference Transform Quality Assessment

Status: `PROPOSED_INACTIVE`

`GeoreferenceTransformQualityAssessment` is a fixture-only mathematical quality gate for a declared two-dimensional affine georeference transform. It is reusable by IIIF/Allmaps overlays and other historic-map workflows, but it is not a renderer, CRS transformer, policy decision, evidence object, or release authority.

## Input model

Each GCP binds one image/resource coordinate pair `[x, y]` to one target planar coordinate pair `[X, Y]`. Target coordinates are synthetic fixture coordinates expressed in one declared linear unit. This profile intentionally does not transform longitude/latitude or contact a CRS service.

The validator fits:

```text
X = a0 + a1*x + a2*y
Y = b0 + b1*x + b2*y
```

using deterministic decimal normal equations and Gaussian elimination. It recomputes:

- the six affine coefficients;
- in-sample RMS residual;
- in-sample maximum residual;
- leave-one-out RMS residual when at least four GCPs exist; and
- leave-one-out maximum residual when at least four GCPs exist.

All reported metrics are rounded to six decimal places using round-half-even before comparison with the candidate declaration.

## Outcomes

- `READY`: at least four nondegenerate GCPs and every configured residual threshold passes.
- `HOLD`: the transform is mathematically fit but lacks redundant control points or exceeds one or more quality thresholds.
- `ERROR`: malformed shape, duplicate resource GCPs, singular control-point geometry, claimed metric drift, or claimed decision drift.

`READY` means only that this synthetic affine fit satisfies the declared numeric thresholds. It does not establish historical cartographic accuracy, geodetic accuracy, rights, CARE state, evidence closure, release readiness, or public-use authority.

## Anti-collapse boundary

Transform fit quality is separate from:

- upstream IIIF or archival source identity;
- exact annotation/source bytes;
- interpretive or historical uncertainty;
- rights and sensitivity policy;
- reviewer judgment;
- browser-rendering behavior; and
- release/publication state.

A low RMS cannot turn an interpretive overlay into surveyed truth.

## Non-effects

The implementation performs no network access, image warp, reprojection, file publication, lifecycle transition, policy evaluation, promotion, release, deployment, or public routing. Governance flags remain fixed false and `release_ref` remains null.
