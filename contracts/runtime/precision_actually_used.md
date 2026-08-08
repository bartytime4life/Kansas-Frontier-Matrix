<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/runtime/precision-actually-used
title: PrecisionActuallyUsed Runtime Response Profile
type: contract-profile
version: v1.0
status: draft; proposed; schema-bound
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: public-contract; runtime; precision-disclosure; cite-or-abstain
owning_root: contracts/
responsibility: Define the semantic meaning and anti-overclaim rules for precision_actually_used inside ANSWER RuntimeResponseEnvelope objects.
truth_posture: CONFIRMED current branch contract/schema/fixture implementation; runtime/API/UI adoption remains NEEDS VERIFICATION.
related:
  - ./runtime_response_envelope.md
  - ../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../fixtures/contracts/v1/runtime/runtime_response_envelope/
  - ../../tools/validators/validate_runtime_response_envelope.py
  - ../../tests/validators/test_validate_runtime_response_envelope.py
  - ../../docs/doctrine/directory-rules.md
notes:
  - "Implements the bounded precision-disclosure direction from KFM-P6-FEAT-0001."
  - "This profile does not calculate precision, resolve evidence, decide policy, or authorize an answer."
  - "Requested precision is informative; actual precision is evidence-derived and controlling."
[/KFM_META_BLOCK_V2] -->

# `precision_actually_used`

`precision_actually_used` records the spatial, temporal, and attribute precision that an `ANSWER` actually used. It prevents a requested resolution, map zoom, display formatting, model confidence, or source filename from being presented as evidence-supported precision.

> [!IMPORTANT]
> Actual precision is a bounded disclosure about cited evidence and recorded transforms. It is not a quality score, confidence score, fitness-for-use approval, policy decision, or release decision.

## Outcome law

| Runtime outcome | Precision field |
|---|---|
| `ANSWER` | Required. At least one top-level evidence reference is required. |
| `ABSTAIN` | Forbidden. The reason code and safe negative-state fields explain why no answer is supported. |
| `DENY` | Forbidden. Precision detail must not leak restricted or sensitive source information. |
| `ERROR` | Forbidden. Operational failure must not manufacture a precision statement. |

## Required dimensions

### Spatial

- `representation`: the representation actually used: point, line, polygon, grid, raster, aggregate, or none.
- `resolution`: bounded human-readable resolution or aggregation level.
- `accuracy`: bounded support statement; it must not imply accuracy the evidence does not establish.
- `generalization_applied`: whether a public-safe or other governed spatial transform changed precision.

When `generalization_applied` is true, at least one `transform_receipt_ref` is required.

### Temporal

- `granularity`: actual time granularity used by the answer.
- `observation_interval.start` and `.end`: bounded evidence interval, with start no later than end.
- `freshness_class`: `current`, `stale-accepted`, `historical`, or `unknown`.

### Attribute

- `measure`: the measure or classification actually used.
- `unit`: unit or explicit unitless label.
- `significant_precision`: supported decimal/significant precision, from 0 through 12.
- `classification_granularity`: the used class/bin/taxonomic/administrative granularity, or null when not applicable.

## Requested versus actual

`requested_precision` is optional and may record the user's requested spatial, temporal, or attribute precision. It never controls the answer. When requested and actual precision differ, the actual fields remain authoritative for disclosure.

Example:

```text
requested spatial precision: 30 m
actual spatial precision: 250 m modeled grid
result: ANSWER with the reduced precision disclosed
```

A caller that requires the unavailable 30 m support should narrow the claim or return `ABSTAIN`; it must not interpolate, resample, zoom, or format its way into a stronger claim.

## Evidence and transform binding

- `precision_actually_used.evidence_refs` must be a nonempty subset of the envelope's top-level `evidence_refs`.
- `transform_receipt_refs` identify transforms that materially changed outward precision.
- A receipt is process memory, not proof that the transform was policy-approved or released.
- Evidence resolution, policy state, review state, release state, correction, and rollback remain governed elsewhere.

## Consumer behavior

Governed APIs and Evidence Drawer surfaces should expose the disclosure without silently simplifying it. They should distinguish:

- requested versus actual precision;
- source resolution versus asserted accuracy;
- source interval versus response issuance time;
- original versus generalized spatial precision;
- measurement precision versus classification granularity.

Public clients must not derive stronger precision from camera zoom, client-side filtering, interpolation, smoothing, resampling, symbol size, or decimal formatting.

## Validation boundary

The paired validator checks:

- JSON Schema closure and fixture polarity;
- ANSWER-only presence;
- negative-state non-disclosure;
- precision evidence references are present at the envelope top level;
- generalized spatial precision cites a transform receipt;
- temporal precision intervals are not inverted;
- duplicate keys, nonfinite numbers, oversized inputs, unsafe symlinks, and malformed JSON fail closed.

A green result does not prove evidence truth, source authority, rights, sensitivity clearance, fitness for use, policy approval, review, release, or publication.

## Rollback

Revert the implementation commit. Existing non-ANSWER envelopes remain compatible because the field is forbidden there both before and after rollback. ANSWER producers must be rolled back atomically with the schema if they have begun emitting the field.
