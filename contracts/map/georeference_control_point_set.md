<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/map/georeference-control-point-set
title: GeoreferenceControlPointSet
type: semantic-contract
version: v0.2
status: draft; repository-grounded; PROPOSED_INACTIVE; fixture-only
owners: [OWNER_TBD]
created: 2026-09-08
updated: 2026-09-08
policy_label: public; fixture-only; no-public-use
owning_root: contracts/
responsibility: Explain the existing v1 control-point-set identity and validation boundary without changing its machine profile.
truth_posture: CONFIRMED pinned implementation; PROPOSED_INACTIVE profile; production fitness and independent stewardship remain unverified.
evidence_snapshot: 6087d07b49362540e437dc666d1cbaa6eb6b82c3
related:
  - ../../schemas/contracts/v1/map/georeference_control_point_set.schema.json
  - ../../tools/validators/map/validate_georeference_control_point_set.py
  - ../../tests/map/test_georeference_control_point_set.py
  - ../../fixtures/contracts/v1/map/georeference_control_point_set/cases.json
  - ../../fixtures/contracts/v1/map/georeference_control_point_set/valid.json
  - ../../tools/generators/project_georeference_transform_quality.py
  - ./georeference_control_point_evidence_assessment.md
  - ../../docs/intake/exploratory/georeference-control-point-set-source-map.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [georeference, control-points, identity, contracts, fixture-only]
notes:
  - Metadata introduced in this documentation edition; created is the metadata-record date, not the original profile's creation date.
  - This edition changes no schema version, validator, numeric algorithm, fixture, or publication authority.
[/KFM_META_BLOCK_V2] -->

# GeoreferenceControlPointSet

`GeoreferenceControlPointSet` is a fixture-first identity envelope for the exact
ground-control-point (GCP) set used by georeference quality assessments. It binds
ordered point IDs, resource coordinates, target coordinates, resource dimensions,
and target-unit declarations so adjacent assessments can identify their inputs
without treating an identity match as evidence of accuracy.

## Status, evidence, and placement

| Concern | Bounded statement |
|---|---|
| Evidence snapshot | `main@6087d07b49362540e437dc666d1cbaa6eb6b82c3` |
| Machine profile | `kfm.georeference.control-point-set.v1`, schema version `1.0.0` |
| Authority / maturity | `PROPOSED_INACTIVE` profile; implemented fixture validator, not a production georeferencing service |
| Semantic responsibility | Existing `contracts/map/georeference_control_point_set.md`; machine shape remains in `schemas/` and execution in `tools/` |
| Review / public use | Independent review is not established; public use is explicitly forbidden by this profile |

The [schema](../../schemas/contracts/v1/map/georeference_control_point_set.schema.json)
owns machine shape. The [validator](../../tools/validators/map/validate_georeference_control_point_set.py)
provides the implementation described below, especially `identity()`, `derive()`,
`validate_candidate()`, and `_read()`. The [tests](../../tests/map/test_georeference_control_point_set.py)
and [case manifest](../../fixtures/contracts/v1/map/georeference_control_point_set/cases.json)
provide bounded conformance evidence. Repository claims in this edition refer to
the pinned snapshot, not whatever a later default branch contains.

[Directory Rules §7.2](../../docs/doctrine/directory-rules.md#72-canonical-responsibility-table),
adopted by [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md),
place semantic meaning under `contracts/`. This is same-path maintenance, not a
new contract home. The [parent README](README.md) still describes map-folder
compatibility and unresolved broader placement; this edition does not resolve
that discrepancy, migrate objects, or ratify the entire folder as canonical.

## Record shape

All fields below are required. The root, coordinate-space declarations, point
records, decision, and governance objects reject additional properties.

| Field | Existing v1 requirement and meaning |
|---|---|
| `object_type` | Exactly `GeoreferenceControlPointSet` |
| `schema_version` / `profile` | Exactly `1.0.0` / `kfm.georeference.control-point-set.v1` |
| `fixture_only` / `network_access` | Exactly `true` / `forbidden`; declarations, not an operating-system sandbox |
| `set_id` | `kfm:georeference-gcp-set:sha256:` followed by 64 lowercase hexadecimal characters |
| `resource_set_hash` / `target_set_hash` | `sha256:` followed by 64 lowercase hexadecimal characters |
| `resource_space` | `kind: image_pixel`, `axis_order: ["x", "y"]`, integer `width_px` and `height_px`, each from 1 through 1,000,000 |
| `target_space` | `kind: synthetic_planar`, `axis_order: ["X", "Y"]`, and `unit: synthetic_meters` or `synthetic_feet` |
| `control_point_count` | Integer from 3 through 256; must equal the array length |
| `control_points` | 3–256 objects, each containing `id`, `resource`, and `target` |
| Point `id` | 1–80 characters matching `^[A-Za-z0-9_.:-]+$`; unique and lexicographically ordered across the array |
| Point `resource` / `target` | Exactly two JSON numbers, not strings or an optional third coordinate |
| `decision` | Outcome `VALID` or `ERROR`; 1–16 unique uppercase/digit/underscore reason strings; exact agreement with the derived result |
| `governance` | All six authority booleans are `false`, and `release_ref` is `null` |

The six booleans are `authority_created`, `policy_evaluated`,
`promotion_authorized`, `release_authorized`, `publication_authorized`, and
`public_use_allowed`. Adding a real CRS, evidence payload, image URL, release
reference, or permissive flag is not a compatible way to activate this object.

## Deterministic identities

The profile computes three related identities. Their inputs are different
projections, not three hashes of the complete record.

| Identity | Exact projection keys and content |
|---|---|
| `resource_set_hash` | `resource_space` with `kind`, `axis_order`, `width_px`, `height_px`; `points` containing ordered `{id, resource}` records |
| `target_set_hash` | `target_space` with `kind`, `axis_order`, `unit`; `points` containing ordered `{id, target}` records |
| `set_id` | Both complete space declarations above; `points` containing ordered `{id, resource, target}` records |

For each projection, both numbers in every coordinate pair become decimal
**strings** through `_decimal_text()`. Zero becomes `"0"`; the implementation
uses `Decimal.normalize()`, fixed-point formatting, and removal of trailing
fractional zeros. The shipped `50` / `50.0` fixture demonstrates equivalent
coordinate spelling. Coordinates remain JSON numbers in the input record.
Dimensions are not passed through this coordinate-string normalization.

Projection objects are serialized with sorted object keys, compact separators
`(',', ':')`, `ensure_ascii=False`, and UTF-8 encoding, then hashed with SHA-256.
Array order is preserved. The partial hashes use the `sha256:` prefix; the full
projection uses the `kfm:georeference-gcp-set:sha256:` prefix. `set_id` is **not**
the hash of the two partial-hash strings. This is the repository's projection
algorithm; this contract does not claim general JSON canonicalization conformance.

Point IDs MUST be unique and lexicographically ordered. `identity()` does not
sort or validate them. Call `validate_candidate()` for acceptance, not the
identity helper alone. Duplicate detection compares normalized **coordinate
pairs** within each space; sharing only one axis value is not a duplicate pair.

The identity projections exclude the object's type/profile/version fields,
count, decision, governance, and already-computed identity strings. Exclusion
from a hash is not permission to omit or change required fields: the schema and
semantic checks remain mandatory. Identity alone does not bind an image file,
source artifact, evidence bundle, review, or release.

### Change behavior and regression vector

A resource-coordinate or dimension change changes the resource and full
identities, but not the target identity. A target-coordinate or unit-declaration
change changes the target and full identities, but not the resource identity.
A point-ID change affects all three. Reordering an array is rejected rather
than silently repaired. Unit relabeling computes a different identity; it does
not convert coordinate values.

The [complete five-point synthetic fixture](../../fixtures/contracts/v1/map/georeference_control_point_set/valid.json)
uses a 1000 × 800 resource and `synthetic_meters`. Its checked regression vector
is given below in the return order of `identity()`:

```text
set_id = kfm:georeference-gcp-set:sha256:9d9da050628e5efe57737fa791116066a1bab4921e28a98d70ec7603730a174a
resource_set_hash = sha256:30d9ac02ce788cc1e5c74162ca432bd40b46d779564468547729342930f2db81
target_set_hash = sha256:bc2a8f740578f6f1112e888126eef236fb0a81a594e95dad3f977037ed373ad5
```

### Numeric compatibility limit

The current normalizer uses the active Decimal context; it does not pin an
independent precision/rounding context. The set CLI parses fractional JSON
numbers as Decimal, whereas the neighboring quality projector parses them as
float. Consequently, the fixture spelling test is not proof of arbitrary-precision,
context-independent, or cross-parser identity preservation. Keep this profile
fixture-only. Broader numeric support needs an explicit normalization envelope,
independent regression vectors, consumer compatibility analysis, and a reviewed
migration; do not silently change v1 identities in a documentation update.

## Coordinate posture

This inactive profile supports image-pixel resource coordinates and only the
synthetic planar target declarations listed above. The resource bounds check is
inclusive: `0 <= x <= width_px` and `0 <= y <= height_px`. It is **not** the
integer pixel-index rule ending at `width_px - 1` / `height_px - 1`. Fractional
resource coordinates are permitted; the code supplies no pixel-center/corner,
image-origin, or axis-direction convention beyond the declared axis labels.

No CRS, datum, coordinate epoch, vertical reference, axis transformation,
geodetic interpretation, or real metre/foot conversion is implied. Target
coordinates have no analogous width/height bounds. Three distinct points satisfy
only the identity profile's minimum count: count and unique pairs do not prove
non-collinearity, spatial coverage, independence, residual quality, or suitability
for a transform.

## Finite validation

`VALID` means that a schema-conforming record has matching computed identities,
coherent checked declarations, and an exactly matching claimed decision under
the current fixture implementation. `ERROR` means a handled input, schema,
semantic, digest, or decision check failed. Neither result is a policy or release
decision, and neither is interchangeable with a neighboring `PASS` or `READY`.

The implementation evaluates the following sequence:

| Stage | Result / precedence |
|---|---|
| Root and schema | Non-object gives `ROOT_NOT_OBJECT`; any schema failure, including unavailable schema handling, becomes `SCHEMA_INVALID` |
| Count | `CONTROL_POINT_COUNT_MISMATCH` |
| Ordered unique IDs | `POINT_IDS_NOT_CANONICAL` |
| Unique resource pairs | `DUPLICATE_RESOURCE_POINT` |
| Unique target pairs | `DUPLICATE_TARGET_POINT` |
| Resource bounds | `RESOURCE_POINT_OUT_OF_BOUNDS` |
| All three identities | Collect `RESOURCE_SET_HASH_MISMATCH`, `TARGET_SET_HASH_MISMATCH`, and/or `SET_ID_MISMATCH`; sort the emitted reasons lexicographically |
| Otherwise | `VALID` with exactly `GEOREFERENCE_CONTROL_POINT_SET_VALID` |
| Claimed decision, after semantic derivation | Any outcome or ordered-reason-list disagreement overrides that derived result with `ERROR / DECISION_MISMATCH` |

Semantic checks stop at the first failing stage except for the combined digest
checks. For example, a bad resource coordinate left with a claimed `VALID`
decision returns `DECISION_MISMATCH`, not the otherwise applicable bounds reason.
A faithfully declared negative fixture remains `ERROR`; matching its claimed
error does not make it an accepted set.

The file reader checks a 1,048,576-byte pre-read size limit and rejects a final
symlink. Its handled diagnostics include `INPUT_SYMLINK_DENIED`, `FILE_NOT_FOUND`,
`FILE_TOO_LARGE`, `JSON_NOT_UTF8`, `JSON_DUPLICATE_KEY`,
`JSON_NONFINITE_NUMBER`, `JSON_INVALID`, `FILE_READ_ERROR`, and
`JSON_COMPLEXITY_LIMIT`. These checks are not a proven atomic filesystem snapshot,
ancestor-symlink confinement, or comprehensive numeric/resource-exhaustion boundary.
Do not equate the CLI reader with validation of arbitrary in-process objects.

## Consumers and adjacent responsibilities

| Surface | Verified relationship; separate responsibility |
|---|---|
| [Quality projector](../../tools/generators/project_georeference_transform_quality.py) | Requires a `VALID` source set, copies the ordered points and target unit into its quality candidate, and carries all three identities in `source_control_point_set`; quality computation and its `READY` / `HOLD` outcome remain separate |
| [Control-point evidence assessment](georeference_control_point_evidence_assessment.md) | Declares a `control_point_set_ref` and point IDs, but does not dereference the set or verify that the referenced coordinates are accurate; a reference string is not proven join closure |
| [Source-map follow-up](../../docs/intake/exploratory/georeference-control-point-set-source-map.md#follow-up-candidates) | Resource-hash binding for spatial-distribution assessment remains a follow-up candidate in this source map, not an integration guarantee from the identity object |

A consumer needing resource-plus-target correspondence needs the full set
identity; a resource-only hash cannot establish target-coordinate agreement.
Preserve upstream identity and any independently assessed outcome rather than
reconstructing, rounding, reordering, or relabeling points without an explicit
transformation and compatibility record.

## Trust boundary

A valid control-point-set identity is not evidence that GCPs are accurate,
admissible, independently sourced, or appropriate for a transform. This validator
does not open imagery, georeference or warp data, compute residuals or spatial
distribution, resolve `EvidenceRef -> EvidenceBundle`, evaluate rights/CARE/policy,
approve human review, or authorize promotion, release, publication, or public use.

`RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED` remains a
governed lifecycle, not a consequence of hashing. Public clients still consume
governed APIs and released public-safe artifacts, never internal or unreleased
stores. Maps, tiles, scenes, and AI explanations are downstream carriers. A public
contract document does not grant permission to publish real control points,
restricted imagery, or sensitive exact locations.

## Validation and maintenance

From a repository checkout with the declared test dependencies installed:

```bash
python -m pytest -q tests/map/test_georeference_control_point_set.py
python tools/validators/map/validate_georeference_control_point_set.py --fixtures
python tools/validators/map/validate_georeference_control_point_set.py fixtures/contracts/v1/map/georeference_control_point_set/valid.json
```

The pinned suite defines **11 tests** and the manifest contains **11 cases: two
`VALID` and nine `ERROR`**. The fixture command exits zero only when all expected
outcomes and reason arrays match and both outcome classes are covered. Normal
file validation exits zero only when every supplied file is `VALID`; otherwise
it exits one. Missing arguments are a command-usage error, not a valid set.

The [dedicated workflow](../../.github/workflows/map-georeference-control-point-set.yml)
selects this contract path for pull requests and pushes to `main`. Its declared
Python version is 3.11. It runs the focused tests, fixture polarity, and authoring
receipt validation. `KFM_NO_NETWORK=1` and the source-import denylist test are not
proof of operating-system network isolation or production confinement. A feature
branch push alone does not select this dedicated workflow's `push` trigger.

This documentation update does not establish hosted exact-head CI, full-repository
validation, real-coordinate fitness, cross-profile reference closure, independent
review, or release readiness. Keep native Python 3.11 execution, numeric-portability
work, and any broader consumer checks explicit in the review handoff.

Preserve the existing schema version, profile, identity prefixes, golden vector,
and the four original section anchors when maintaining this file. A later
normalization, coordinate convention, or schema change needs corresponding tests,
consumer impact, migration, and rollback rather than prose-only activation.

## Correction and rollback

Correct erroneous documentation through a reviewed forward change. For this
edition, the prior contract is blob `c11165f9e1dacfccd2604035a2bc24b765d433c8`
at the evidence snapshot. Revert the complete authoring slice, including its
workflow receipt binding, if this edition must be withdrawn; do not leave a
receipt checking different bytes or rewrite a historical receipt to claim a new
review. Such a repository revert is not a data-release rollback.

Changing a real point correspondence would require a new validated set identity
and explicit downstream reassessment/correction. This inactive object contains
no implemented release, correction-propagation, or public rollback mechanism.
