<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/map/georeference-control-point-evidence-assessment
title: Georeference Control-Point Evidence Assessment
type: semantic-contract
version: v0.2.0
status: proposed; inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Map steward · Evidence steward · Documentation steward
created: 2026-08-11
updated: 2026-09-08
policy_label: public; map; georeference; evidence; fixture-only
owning_root: contracts/
responsibility: Define the bounded meaning, deterministic outcomes, evidence-reference posture, and false-authority boundary for qualitative GCP evidence assessment candidates.
truth_posture: CONFIRMED deterministic synthetic implementation / PROPOSED inactive profile / NEEDS VERIFICATION real evidence, operational consumers, policy, and steward review
related:
  - ../../schemas/contracts/v1/map/georeference_control_point_evidence_assessment.schema.json
  - ../../fixtures/contracts/v1/map/georeference_control_point_evidence_assessment/cases.json
  - ../../tools/validators/map/validate_georeference_control_point_evidence_assessment.py
  - ../../tests/map/test_georeference_control_point_evidence_assessment.py
  - ../../.github/workflows/map-georeference-control-point-evidence.yml
  - ../../docs/intake/exploratory/pass-18-georeference-control-point-evidence-source-map.md
  - ../../data/receipts/generated/genrec-pass18-georeference-control-point-evidence-20260811.json
  - ../../data/receipts/generated/genrec-georeference-control-point-evidence-contract-currentness-20260908.json
  - georeference_control_point_set.md
  - georeference_spatial_distribution.md
  - georeference_transform_quality.md
tags: [kfm, map, georeference, gcp, evidence, deterministic-identity, fixture-only]
notes:
  - "This edition documents the existing schema, validator, fixture, test, and workflow behavior without changing machine semantics or activating the profile."
  - "The source-backed adaptation remains recorded in the Pass 18 exploratory source map."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# GeoreferenceControlPointEvidenceAssessment

## Status and purpose

`GeoreferenceControlPointEvidenceAssessmentCandidate` is a **PROPOSED_INACTIVE**, fixture-only record for asking whether a declared ground-control-point (GCP) set carries internally reviewable qualitative evidence about:

- target visibility, contrast, and marker scale;
- the declared surveyed-coordinate method and reference system;
- the declared image-matching method and review posture; and
- binding between per-source, per-match, and per-point evidence references and one canonical aggregate list.

The profile implements the narrow evidence-quality seam identified by Pass 18 idea `KFM-P18-INV-317`. Its [source map](../../docs/intake/exploratory/pass-18-georeference-control-point-evidence-source-map.md) records the research lineage and the adaptation decision. That lineage motivates the fields; it does not prove any candidate observation.

The current repository contains a closed JSON Schema, a deterministic no-network validator, 34 reviewed fixture cases, 14 focused tests, and a dedicated workflow. This is a bounded synthetic implementation, not evidence of runtime use or operational maturity.

## Authoritative surfaces

| Responsibility | Current surface | What it owns |
|---|---|---|
| Semantic meaning | This document | Purpose, interpretation, outcome semantics, and non-effects. |
| Machine shape | [Draft 2020-12 schema](../../schemas/contracts/v1/map/georeference_control_point_evidence_assessment.schema.json) | Required fields, closed objects, enums, cardinality, patterns, constants, and fixed-false effects. |
| Deterministic evaluation | [Validator](../../tools/validators/map/validate_georeference_control_point_evidence_assessment.py) | Input safety, coherence findings, recommendation derivation, identity checks, outcome precedence, and diagnostics. |
| Synthetic examples | [Fixture manifest](../../fixtures/contracts/v1/map/georeference_control_point_evidence_assessment/cases.json) | One common synthetic base plus exact mutations and expected findings for 34 cases. |
| Executable proof | [Focused tests](../../tests/map/test_georeference_control_point_evidence_assessment.py) | Four-way polarity, identity, summary, input-safety, no-network, false-authority, and redacted-diagnostic assertions. |
| Hosted orchestration | [Dedicated workflow](../../.github/workflows/map-georeference-control-point-evidence.yml) | Focused tests, exact fixture replay, historical receipt replay at its originating commit, and current receipt integrity for relevant changes. |

No surface in this table owns real imagery, survey measurements, resolved evidence, policy, review approval, release state, or public-use authority.

## Candidate shape

The schema is closed: undeclared properties are invalid.

| Field or group | Required meaning | Bounded rule |
|---|---|---|
| Identity and profile | `object_type`, `schema_version`, `profile`, `status`, `assessment_id`, and `spec_hash` | Constants identify fixture profile v1; status remains `PROPOSED_INACTIVE`. |
| Lineage and time | `source_idea_id`, `evaluated_at` | The idea ID is fixed to `KFM-P18-INV-317`; time must be a valid date-time and use the UTC `Z` form. |
| Upstream set | `control_point_set_ref` | Must use the `kfm:georeference-gcp-set:sha256:<64 lowercase hex>` shape; it is never dereferenced. |
| Coordinate source | `method`, `status`, `reference_system_ref`, `evidence_ref` | Declares surveyed-coordinate provenance without verifying a receiver, survey, CRS, datum, epoch, or accuracy. |
| Image matching | `method`, `status`, `image_observation_set_ref`, `evidence_ref` | Declares matching and review posture without opening or matching imagery. |
| Point evidence | `control_point_count`, `control_points` | Between 3 and 256 point records; the count must equal the array length. |
| Summary | Four recomputable counts | Derived only from the point observations described below. |
| Aggregate evidence | `evidence_refs` | Between 1 and 512 unique internal KFM references in canonical lexical order. |
| Review posture | `recommendation`, `review_state` | Recommendation is derived; `review_state` is always `HOLD`. |
| Boundary declarations | `limitations`, `effects` | Limitations are an exact fixed list and every effect is fixed `false`. |

The `3..256` point bound is a serialization and fixture-safety constraint. It is **not** a claim that three points are adequate for a particular terrain, sensor, transform, accuracy target, or public use.

## Controlled vocabularies

### Coordinate-source declarations

- `method`: `RTK_GNSS`, `PPK_GNSS`, `TOTAL_STATION`, `SURVEY_NETWORK`, `OTHER_REVIEWED`, or `UNKNOWN`.
- `status`: `VERIFIED`, `UNKNOWN`, or `INVALID`.
- A `VERIFIED` declaration requires a non-`UNKNOWN` method plus non-null `reference_system_ref` and `evidence_ref` values.

These labels describe a candidate's declaration. The validator does not independently verify the equipment, correction service, survey network, coordinate reference system, datum, epoch, field procedure, or positional accuracy.

### Image-matching declarations

- `method`: `MANUAL_VERIFIED`, `AUTOMATED_WITH_MANUAL_REVIEW`, `AUTOMATED_UNREVIEWED`, or `UNKNOWN`.
- `status`: `VERIFIED`, `UNKNOWN`, or `INVALID`.
- A `VERIFIED` declaration requires `MANUAL_VERIFIED` or `AUTOMATED_WITH_MANUAL_REVIEW`, a non-null `image_observation_set_ref`, and a non-null `evidence_ref`.

`AUTOMATED_UNREVIEWED` is unresolved, not verified evidence.

### Per-point observations

| Dimension | Reviewable values | Unresolved values | Adverse values |
|---|---|---|---|
| `visibility` | `CLEAR` | `PARTIAL`, `UNKNOWN` | `OBSCURED` |
| `contrast` | `HIGH`, `ADEQUATE` | `UNKNOWN` | `LOW` |
| `marker_scale` | `ADEQUATE` | `UNKNOWN` | `INADEQUATE` |
| `match_status` | `VERIFIED` | `UNVERIFIED`, `UNKNOWN` | — |

Every point has an upstream point `id` but repeats no coordinates. Any point with at least one observation other than `UNKNOWN` requires a non-null `evidence_ref`.

## Coherence and evidence-binding rules

The validator applies these deterministic invariants after schema validation:

1. `evaluated_at` ends in `Z` and represents UTC.
2. `control_point_count` equals the number of `control_points`.
3. Point IDs are strings, unique, and lexicographically ordered.
4. `summary` exactly equals:
   - `clear_visibility_count`: points whose visibility is `CLEAR`;
   - `acceptable_contrast_count`: points whose contrast is `HIGH` or `ADEQUATE`;
   - `adequate_scale_count`: points whose marker scale is `ADEQUATE`; and
   - `verified_match_count`: points whose match status is `VERIFIED`.
5. `evidence_refs` is the lexicographically sorted unique list form required by the validator.
6. Every non-null coordinate-source, matching, and per-point `evidence_ref` appears in `evidence_refs`.
7. A verified coordinate-source or matching declaration carries its required supporting references.
8. `recommendation` equals the deterministic recommendation derived from the findings.
9. `spec_hash` and `assessment_id` equal the identities recomputed from the complete candidate.

Rule 6 is one-way containment. The validator proves that local non-null references are bound into the aggregate list; it does not resolve them, authenticate them, or prove that every aggregate entry is used by a subrecord.

## Finite outcomes and precedence

Precedence is `ERROR > DENY > ABSTAIN > PASS`.

| Outcome | Deterministic meaning | Recommendation rule |
|---|---|---|
| `PASS` | Schema, coherence, recommendation, and identity checks produce no finding. | `READY_FOR_REVIEW` |
| `ABSTAIN` | Every finding is an unresolved-evidence finding from the bounded abstention set. | `HOLD` |
| `DENY` | At least one adverse-state, coherence, binding, UTC, or recommendation finding exists and no higher-precedence error exists. | Semantic denial findings derive `DENY`; any disagreement adds `RECOMMENDATION_MISMATCH`. |
| `ERROR` | Input cannot be read safely, schema validation fails, the fixture manifest is invalid, or deterministic identity disagrees. | Candidate recommendation has no authority. |

`PASS` still leaves `review_state` at `HOLD` and every authority flag false. It means only “internally coherent and ready for human review under this fixture profile.”

### Reason-code classification

| Class | Codes |
|---|---|
| `ABSTAIN` | `COORDINATE_SOURCE_UNRESOLVED`, `MATCHING_REVIEW_UNRESOLVED`, `MATCHING_UNRESOLVED`, `POINT_VISIBILITY_PARTIAL`, `POINT_VISIBILITY_UNKNOWN`, `POINT_CONTRAST_UNKNOWN`, `MARKER_SCALE_UNKNOWN`, `POINT_MATCH_UNRESOLVED` |
| `DENY` when no error is present | `EVALUATED_AT_NOT_UTC`, `CONTROL_POINT_COUNT_MISMATCH`, `POINT_IDS_NOT_CANONICAL`, `SUMMARY_MISMATCH`, `EVIDENCE_REFERENCES_NOT_CANONICAL`, `EVIDENCE_REFERENCE_UNBOUND`, `COORDINATE_SOURCE_INVALID`, `COORDINATE_SOURCE_STATUS_INCOHERENT`, `VERIFIED_REFERENCE_SYSTEM_MISSING`, `VERIFIED_SOURCE_EVIDENCE_MISSING`, `MATCHING_INVALID`, `MATCHING_STATUS_INCOHERENT`, `VERIFIED_MATCHING_INPUT_MISSING`, `VERIFIED_MATCHING_EVIDENCE_MISSING`, `POINT_VISIBILITY_OBSCURED`, `POINT_CONTRAST_LOW`, `MARKER_SCALE_INADEQUATE`, `POINT_EVIDENCE_MISSING`, `RECOMMENDATION_MISMATCH` |
| `ERROR` | `FILE_NOT_FOUND`, `FILE_READ_ERROR`, `FILE_TOO_LARGE`, `INPUT_SYMLINK_DENIED`, `JSON_DUPLICATE_KEY`, `JSON_INVALID`, `JSON_NONFINITE_NUMBER`, `ROOT_NOT_OBJECT`, `SCHEMA_INVALID`, `SCHEMA_UNAVAILABLE`, `SPEC_HASH_MISMATCH`, `ASSESSMENT_ID_MISMATCH`, `FIXTURE_MANIFEST_INVALID` |

Findings are de-duplicated and sorted by code and JSON Pointer path. A mixture of unresolved and denial findings resolves to `DENY`; any error code resolves to `ERROR`.

The internal assessment helper also has a defensive `CONTROL_POINTS_INVALID` fallback. Public validation is schema-first, so a non-array `control_points` value returns `SCHEMA_INVALID` before that fallback is reached.

## Deterministic identity

`spec_hash` is the SHA-256 digest of the candidate's canonical JSON after removing only `assessment_id` and `spec_hash`:

- keys are sorted;
- separators are `,` and `:` with no insignificant whitespace;
- encoding is UTF-8;
- non-ASCII text is retained rather than escaped solely for hashing; and
- non-finite numbers are forbidden.

`assessment_id` is `gcp-evidence-assessment:` followed by the first 24 lowercase hexadecimal characters of the `spec_hash` digest.

All remaining fields are identity-bearing, including `evaluated_at`, `recommendation`, `review_state`, limitations, fixed-false effects, array order, and every reference. Canonical point and evidence-reference ordering therefore matters.

## Input and diagnostic safety

For explicit-file validation, the implementation:

- accepts only regular, non-symlink files no larger than 1,048,576 bytes;
- requires UTF-8 JSON with one object at the root;
- rejects duplicate object keys and non-finite numbers;
- emits compact JSON containing the finite outcome, sorted findings, scope, and an all-false authority map;
- returns exit code `0` only when every explicit candidate is `PASS`, `1` for any non-pass result, and `2` for CLI misuse; and
- does not echo `control_point_set_ref` or any candidate evidence reference in diagnostics.

Fixture replay materializes each reviewed mutation, recomputes summaries, recommendation, and identity unless the case explicitly tests drift, and requires the exact expected outcome and findings. It also requires all four outcomes to be represented.

## Relationship to adjacent contracts

| Question | Owning contract | This profile's relationship |
|---|---|---|
| Which exact point set and coordinates were declared? | [`GeoreferenceControlPointSet`](georeference_control_point_set.md) | Carries only its opaque content-addressed reference and ordered point IDs. |
| Are points distributed adequately in resource space? | [`GeoreferenceSpatialDistributionAssessment`](georeference_spatial_distribution.md) | Does not calculate hull coverage, extrapolation, centroid offset, or quadrant occupancy. |
| Does the fitted transform meet residual thresholds? | [`GeoreferenceTransformQualityAssessment`](georeference_transform_quality.md) | Does not fit a transform or calculate in-sample or leave-one-out residuals. |
| Are accuracy, precision, acquisition, and attachment scope distinguished? | [`GeometryQualityScopeAssessmentCandidate`](../evidence/geometry_quality_scope_assessment.md) | Does not turn qualitative marker evidence into positional accuracy. |
| Is a historic scan and derivative lineage coherent? | [`HistoricMapScanLineageAssessmentCandidate`](../evidence/historic_map_scan_lineage_assessment.md) | May be referenced by a separate lineage record without replacing its scan, rights, or derivative-use meaning. |

Composition does not collapse these responsibilities. A positive result from one profile cannot fill a missing result from another.

## Directory placement and maturity

The semantic contract remains under `contracts/map/`; machine shape, fixtures, validation, tests, workflow orchestration, intake lineage, and authoring provenance remain in their adopted responsibility roots. This edition creates no new root, alias, data instance, policy, or release surface.

The parent `contracts/map/` README still describes the lane as compatibility/proposed. This contract's existing dependency-closed implementation does not settle that broader directory-maturity question or activate this object family.

## Validation evidence

Run the focused proof from the repository root:

```bash
python -m pytest -q tests/map/test_georeference_control_point_evidence_assessment.py
python tools/validators/map/validate_georeference_control_point_evidence_assessment.py --fixtures
python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  contracts/map/georeference_control_point_evidence_assessment.md
```

The committed fixture matrix contains 34 cases with exact expected polarity: 1 `PASS`, 8 `ABSTAIN`, 19 `DENY`, and 6 `ERROR`. Passing local or hosted checks proves only the bounded behaviors asserted by those checks.

## Trust boundary and non-effects

Validation does not:

- dereference the control-point set, reference system, image-observation set, or evidence references;
- open imagery, inspect marker pixels, contact a GNSS/correction service, or verify field procedures;
- establish coordinate accuracy, distinguish accuracy from precision for a real observation, or calculate uncertainty;
- assess GCP distribution, fit a transform, calculate residuals, georeference, warp, tile, or render an image;
- resolve an EvidenceBundle, evaluate rights, CARE, sensitivity, or policy, or approve human review;
- activate a runtime consumer, mutate data, promote lifecycle state, or authorize release, deployment, publication, or public use.

A green result is not evidence that a real GCP, coordinate, image, reference system, transform, map, or public geometry is accurate, admissible, or safe.

## Rollback

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert this documentation-only change and rerun the focused tests, fixture replay, and local link check. No schema, fixture, validator, policy, data, release, deployment, or public state requires restoration.

## Change history

| Date | Edition | Change | Effect |
|---|---|---|---|
| 2026-08-11 | Initial | Recorded the narrow fixture-only GCP qualitative-evidence profile. | Proposed inactive semantics only. |
| 2026-09-08 | `v0.2.0` | Reconciled the contract with the implemented schema, validator, fixture matrix, tests, workflow, identity, reason codes, safety controls, and adjacent-owner boundaries. | Documentation only; no machine-semantic or authority change. |

<p align="right"><a href="#top">Back to top</a></p>
