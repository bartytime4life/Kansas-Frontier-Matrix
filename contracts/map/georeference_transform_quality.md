<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/map/georeference-transform-quality
title: Georeference Transform Quality Assessment
type: semantic-contract
version: v0.2.0
status: draft; repository-grounded; PROPOSED_INACTIVE; fixture-only; non-publisher
owners: NEEDS VERIFICATION — map-contract and numerical-validation stewardship
updated: 2026-09-08
owning_root: contracts/
current_path: contracts/map/georeference_transform_quality.md
responsibility: Explain the existing affine-quality assessment, deterministic comparisons, finite outcomes, projection boundary, and validation limits without changing its machine profile.
evidence_snapshot: bartytime4life/Kansas-Frontier-Matrix@af724db2278bc59395ca3817622df43e7be767b9
audit_baseline: 6087d07b49362540e437dc666d1cbaa6eb6b82c3
prior_blob: 4fbab9697ef4f838747d9c9d18eaa5f6922bd36f
truth_posture: CONFIRMED source behavior at the pinned snapshot; PROPOSED_INACTIVE profile; no production or approval claim
policy_label: repository-facing; synthetic-coordinates; no-network; no-release; no-public-use
supersedes: Earlier prose at this path only; schema_version 1.0.0 and numerical behavior are unchanged.
related:
  - ./README.md
  - ./georeference_control_point_set.md
  - ./georeference_control_point_evidence_assessment.md
  - ./georeference_spatial_distribution.md
  - ../../schemas/contracts/v1/map/georeference_transform_quality.schema.json
  - ../../tools/validators/map/validate_georeference_transform_quality.py
  - ../../tools/generators/project_georeference_transform_quality.py
  - ../../tests/map/test_georeference_transform_quality.py
  - ../../fixtures/contracts/v1/map/georeference_transform_quality/cases.json
  - ../../.github/workflows/map-georeference-transform-quality.yml
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Georeference Transform Quality Assessment

Status: `PROPOSED_INACTIVE` / fixture-only. Document edition: `v0.2.0`;
machine `schema_version`: **`1.0.0`, unchanged**.

`GeoreferenceTransformQualityAssessment` is a fixture-only mathematical quality
gate for a declared two-dimensional affine georeference transform. It is reusable
as a candidate building block for IIIF/Allmaps overlays and other historic-map
workflows, but it is not a renderer, CRS transformer, policy decision, evidence
object, or release authority. No live integration follows from this contract.

## Status and placement

This same-path revision is grounded in the schema, validator, fixtures, tests,
and projection adapter at the metadata's immutable evidence snapshot. The
[paired schema](../../schemas/contracts/v1/map/georeference_transform_quality.schema.json)
controls machine shape; the
[validator](../../tools/validators/map/validate_georeference_transform_quality.py)
controls the implemented comparisons described below. This document explains
meaning and limitations, not a new algorithm or approval process.

Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts [Directory Rules](../../docs/doctrine/directory-rules.md):
`DIR-AUTHROOT-001` and `DIR-AUTHROOT-002` separate machine schemas from semantic
contracts. The existing `contracts/map/` path is retained; the
[parent README](README.md)'s broader compatibility and family-routing questions
are not resolved by editing this already paired object. No file moves, new
schema home, policy home, or map-family adoption are authorized here.

## Input model

Each ground control point (GCP) binds one image/resource coordinate pair `[x, y]`
to one target planar coordinate pair `[X, Y]`. Target coordinates are synthetic
fixture coordinates expressed in one declared linear unit. This profile does
not transform longitude/latitude, convert units, or contact a CRS service.

The root and nested record objects are closed: unrecognized fields are rejected.
The following is an orientation table, not a duplicate JSON Schema.

| Field | Implemented meaning and constraint |
| --- | --- |
| `object_type`, `schema_version`, `profile` | Constants `GeoreferenceTransformQualityAssessment`, `1.0.0`, and `kfm.georeference.affine-quality.v1`. |
| `fixture_only`, `network_access` | Fixed to `true` and `forbidden`. |
| `assessed_at` | Required date-time string checked with the validator's format checker; not a source observation date, verified clock, or release time. |
| `target_unit` | `synthetic_meters` or `synthetic_feet`; one unit applies to target coordinates, residual metrics, and residual thresholds. |
| `gcp_count`, `gcps` | Both bounded to 3–64 points; the declared count must equal the array length. Each point has `id`, `resource`, and `target`; each coordinate pair contains exactly two numbers. |
| `thresholds` | All five keys are required: `minimum_gcps` is fixed to `4`; `max_rms`, `max_residual`, `max_loo_rms`, and `max_loo_residual` are positive numbers. The schema supplies no numeric defaults or production tolerances. |
| `computed` | Six coefficients in order `[a0, a1, a2, b0, b1, b2]`, plus `rms`, `max_residual`, `loo_rms`, and `loo_max_residual`. LOO values are nullable in shape and checked by recomputation. |
| `decision` | A claimed `READY`, `HOLD`, or `ERROR` with an ordered reason list; the validator independently derives and compares both. |
| `governance` | Six authority flags fixed false and `release_ref` fixed null; see [Non-effects](#non-effects). |

The direct assessment rejects duplicate **resource-coordinate pairs** after
numeric conversion. It does not independently enforce unique/sorted point IDs,
unique target coordinates, resource-image bounds, or a shared-set digest.
Those are separate responsibilities of
[GeoreferenceControlPointSet](georeference_control_point_set.md), not guarantees
inferred from this object's `id` fields.

## Computation and comparison

The validator fits an unweighted affine model using decimal normal equations
and Gaussian elimination:

```text
X_hat = a0 + a1*x + a2*y
Y_hat = b0 + b1*x + b2*y
r_i = sqrt((X_hat_i - X_i)^2 + (Y_hat_i - Y_i)^2)
rms = sqrt(sum(r_i^2) / n)
max_residual = max(r_i)
```

`rms` is the RMS of the two-dimensional residual distances across `n` GCPs.
It is not a per-axis statistic, a degrees-of-freedom-adjusted uncertainty estimate,
or a confidence radius. Residuals are computed from the fitted coefficients
before the coefficients are rounded for reporting.

### Leave-one-out evaluation

For at least four GCPs, each point is omitted in turn, the affine model is refit
on the remaining points, and the omitted point's residual is measured. The RMS
and maximum of those held-out residuals become `loo_rms` and
`loo_max_residual`. With three points, both values are `null`, not zero, and
an otherwise coherent fit is `HOLD / INSUFFICIENT_REDUNDANCY`.

Every leave-one-out subset must be solvable. A full-set fit can succeed while
one omitted-point subset is singular; this is `ERROR / LOO_GEOMETRY_DEGENERATE`,
not a missing measurement that may be silently excluded. Leave-one-out
validation reuses the supplied set; it does not establish independently surveyed
checkpoints or authenticate those points.

### Two distinct comparison rules

**Declaration integrity:** all six coefficients and all non-null reported
metrics are rounded to six decimal places using round-half-even, converted to
numeric report values, and compared with the entire supplied `computed` object.
This is numeric-value equality, not equality of JSON spelling or source bytes.
A mismatch produces the derived reason `METRIC_MISMATCH`.

**Quality thresholds:** the validator compares the **unrounded recomputed
Decimal residual metrics** with the supplied thresholds. Only strict `>` is an
exceedance; equality passes that individual threshold. Do not substitute rounded
report values for these comparisons.

For example, the existing `ready_small_noise` fixture has RMS approximately
`0.1407463101` and reports `0.140746`. Changing its `max_rms` to `0.140746`
exceeds that threshold even though the displayed numbers appear equal. The
candidate must then declare the correctly derived `HOLD` decision. The unchanged
fixture's own thresholds still yield `READY`.

### Numerical scope

The implementation converts parsed numbers with `Decimal(str(value))`; JSON
fractional values first pass through a finite Python float parser. The solver
and square-root operations use local precision 50, while other arithmetic and
quantization use the ambient Decimal context. The solver treats an absolute
pivot at or below `1e-30` as degenerate.

These are implementation details, not a claim of lossless decimal ingestion,
scale-independent conditioning, full context independence, or robust results
for every magnitude admitted by the schema. Extreme numeric behavior and a
broader numerical-stability profile remain **NEEDS VERIFICATION** before
expanding this synthetic-use boundary.

## Outcomes

| Outcome | Meaning within this profile |
| --- | --- |
| `READY` | At least four GCPs, a solvable full fit and every LOO fit, matching declarations, and no residual threshold exceedance. |
| `HOLD` | The fit and declarations are coherent, but redundancy or one or more residual thresholds fail. |
| `ERROR` | Input, shape, count, geometry, metric declaration, or decision declaration cannot be accepted under the implemented checks. |

The candidate validator first checks root shape and schema, then derives the
count/geometry/metric/threshold result, and finally verifies the declared
`decision`. The table below names derived reasons; the declaration must match
that result for it to be returned unchanged.

| Result class | Reason codes |
| --- | --- |
| Ready | `GEOREFERENCE_TRANSFORM_QUALITY_READY` |
| Hold | `INSUFFICIENT_REDUNDANCY`, `RMS_THRESHOLD_EXCEEDED`, `MAX_RESIDUAL_THRESHOLD_EXCEEDED`, `LOO_RMS_THRESHOLD_EXCEEDED`, `LOO_MAX_RESIDUAL_THRESHOLD_EXCEEDED` |
| Count or geometry error | `GCP_COUNT_MISMATCH`, `DUPLICATE_RESOURCE_GCP`, `DEGENERATE_GCP_GEOMETRY`, `LOO_GEOMETRY_DEGENERATE` |
| Declaration error | `METRIC_MISMATCH`, `DECISION_MISMATCH` |
| Candidate input error | `ROOT_NOT_OBJECT`, `SCHEMA_INVALID` |

Multiple hold reasons are sorted lexicographically. Reordering even the same
reasons, inventing a reason, or claiming a different outcome yields
`ERROR / DECISION_MISMATCH`. That final check also applies after a derived
error: an incorrect error declaration can mask the earlier reason with
`DECISION_MISMATCH`. The schema's uppercase reason-string pattern is not the
semantic reason-code validator. Schema-loading/evaluation failures are currently
normalized by `validate_candidate` to `SCHEMA_INVALID`.

The file reader additionally reports `INPUT_SYMLINK_DENIED`, `FILE_NOT_FOUND`,
`FILE_TOO_LARGE`, `JSON_NOT_UTF8`, `JSON_DUPLICATE_KEY`, `JSON_NONFINITE_NUMBER`,
`JSON_INVALID`, `FILE_READ_ERROR`, or `JSON_COMPLEXITY_LIMIT`. It checks the
file size against 1 MiB before parsing and rejects a directly supplied symlink;
this is not a claim of race-free filesystem snapshots or bounded handling of
all computational inputs. Call the validated candidate/CLI boundary, not
`derive` or `compute_quality` alone, for untrusted records.

`READY` means only that this synthetic affine fit satisfies the declared numeric
thresholds. It does not establish historical cartographic accuracy, geodetic
accuracy, rights, CARE state, evidence closure, release readiness, or public-use
authority. It is not a PR delivery state or review approval.

## Projection and adjacent profiles

The existing
[projection adapter](../../tools/generators/project_georeference_transform_quality.py)
validates an upstream `GeoreferenceControlPointSet` as `VALID` and combines its
points and target unit with a separate projection request. It recomputes the
quality candidate and permits a generated inner assessment of `READY` or `HOLD`.

Its output is a **wrapper**, `GeoreferenceTransformQualityProjection`, with
`status: CANDIDATE`. `source_control_point_set` preserves `set_id`,
`resource_set_hash`, and `target_set_hash`; `transform_quality_candidate`
contains the unchanged assessment-v1 shape. Do not submit the entire wrapper
to the assessment validator or add these lineage fields to the closed inner
assessment. The wrapper's carried IDs are not an EvidenceBundle.

The adapter's request uses a stricter whole-second UTC `assessed_at` spelling
than the assessment's date-time schema. Default output is stdout; `--write`
is an explicit local-file operation, not release or publication. A successful
generator exit does not mean the inner assessment is `READY`.

[Control-point evidence assessment](georeference_control_point_evidence_assessment.md)
addresses declared visibility, contrast, marker scale, source, and matching
support. [Spatial distribution](georeference_spatial_distribution.md) addresses
resource-space coverage and extrapolation. Neither is executed or resolved by
this quality validator. Their distinct outcomes and references must not be
collapsed into the quality result or treated as automatic end-to-end closure.

## Anti-collapse boundary

Transform fit quality remains separate from upstream archival/IIIF identity,
exact annotation/source bytes, shared-set identity, interpretive or historical
uncertainty, rights and sensitivity policy, reviewer judgment, browser behavior,
and release/publication state.

A low RMS cannot turn an interpretive overlay into surveyed truth. The direct
profile also does not test affine invertibility, certify target geometry,
measure resource-mask coverage, or prove real-world positional accuracy.
Thresholds are declarations, not approved accuracy standards.

Any future public consumer must use governed APIs or released public-safe
artifacts, with required `EvidenceRef -> EvidenceBundle` resolution, policy,
rights, sensitivity, review, integrity, correction, and rollback checks. There
is no shortcut from this numeric result to a public layer or AI claim. Sensitive
locations must not be introduced into the synthetic fixture lane.

## Validation

From the repository root:

```bash
python -m pytest -q tests/map/test_georeference_transform_quality.py
python tools/validators/map/validate_georeference_transform_quality.py --fixtures
```

The [focused suite](../../tests/map/test_georeference_transform_quality.py)
contains ten source-defined tests. The
[fixture matrix](../../fixtures/contracts/v1/map/georeference_transform_quality/cases.json)
contains ten exact-polarity cases: two `READY`, three `HOLD`, and five `ERROR`.
Those inventories do not imply complete numerical, parser, or integration
coverage. The original import-string test is not a universal network-isolation
proof.

The file-mode CLI exits `0` only when every supplied assessment is `READY`;
`HOLD` or `ERROR` produces exit `1`. Fixture replay instead exits `0` when all
expected outcomes and reasons match, including expected holds and errors.
Do not describe a green fixture replay as ten approved transforms.

The [dedicated workflow](../../.github/workflows/map-georeference-transform-quality.yml)
retains focused tests and fixture replay. Its receipt checks distinguish the
historical authoring snapshot from the current contract/workflow revision:
the old receipt is replayed against its exact ancestor, while the new receipt
binds current changed bytes. Historical receipts are not rewritten to follow
this document. Hosted execution, supported Python 3.11 validation, and
independent review remain separate evidence from local tests or workflow text.

## Non-effects

The quality implementation performs no network access, image warp, reprojection,
file publication, lifecycle transition, policy evaluation, promotion, release,
deployment, or public routing. `authority_created`, `policy_evaluated`,
`promotion_authorized`, `release_authorized`, `publication_authorized`, and
`public_use_allowed` remain false; `release_ref` remains null.

The lifecycle remains
`RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED`.
Neither a fit, fixture, generated wrapper, commit, receipt, nor green CI performs
that governed transition.

## Compatibility and rollback

This revision changes documentation and its receipt-check wiring only. It does
not alter schema identity, fields, threshold values, numerical code, fixtures,
tests, generator behavior, or adjacent contracts. Drive planning material and
Notion coordination were consulted as lineage, not numerical or adoption
authority; no external tolerance or new transform method is introduced.

Rollback is an ordinary reviewed revert of this bounded change, restoring the
prior contract blob `4fbab9697ef4f838747d9c9d18eaa5f6922bd36f` and its previous
workflow wiring. Preserve the historical receipt and disclose that reverting
wiring also restores its old current-tree receipt interpretation. No data,
registry, published layer, release, or cache rollback is performed by a document
revert. Any future profile change needs its own compatibility, validation,
review, and rollback evidence.
