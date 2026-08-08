<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/runtime/runtime-response-precision-profile
title: RuntimeResponseEnvelope precision-actually-used profile
type: semantic-contract-extension; runtime-boundary; evidence-bound-precision
version: v0.1.0
status: proposed; schema-paired; fixture-first
owners: OWNER_TBD — Runtime steward · Evidence steward · Schema steward · API steward · UI steward
created: 2026-08-08
updated: 2026-08-08
policy_label: public-safe; runtime; precision; cite-or-abstain; non-authoritative
related:
  - ./runtime_response_envelope.md
  - ../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../fixtures/contracts/v1/runtime/runtime_response_envelope/
  - ../../tests/runtime_proof/test_envelope_finite_outcomes.py
  - ../../apps/explorer-web/src/features/evidence_drawer/precision.ts
tags: [kfm, runtime-response, precision, evidence, spatial, temporal, attribute, disclosure]
[/KFM_META_BLOCK_V2] -->

# RuntimeResponseEnvelope precision-actually-used profile

This subordinate profile realizes **KFM-P6-FEAT-0001** without creating a second
runtime-envelope authority. The canonical machine shape remains
`schemas/contracts/v1/runtime/runtime_response_envelope.schema.json`.

Every `ANSWER` must disclose `precision_actually_used`: the precision supported
by the cited evidence and transforms, not the precision requested by a caller,
implied by map zoom, or formatted by the client.

## Multidimensional precision

The disclosure is a closed object with four required sections.

| Section | Required meaning |
|---|---|
| `spatial` | Representation, actual resolution, and whether generalization was applied. |
| `temporal` | Granularity and the observation interval actually supporting the answer. |
| `attribute` | Measure, unit, significant digits, or classification granularity actually supported. |
| `basis` | EvidenceRefs, source refs, and transform refs from which the disclosure was derived. |

Precision is therefore not a confidence score. It must not collapse spatial,
temporal, attribute, evidence, source, or transform support into one number.

## Finite-outcome rule

- `ANSWER` requires the disclosure.
- `ABSTAIN`, `DENY`, and `ERROR` may omit it.
- A missing or malformed disclosure makes an `ANSWER` schema-invalid.
- An EvidenceRef in `basis.evidence_refs` is still only a reference. Runtime
  evidence resolution, admissibility, policy, review, release, and correction
  remain separately governed.
- A client may display the disclosure but must not increase, round up, or infer
  a stronger precision.

## UI projection boundary

`apps/explorer-web/src/features/evidence_drawer/precision.ts` is a strict,
fixture-driven formatter for the new object. It produces bounded labels and
fails closed on malformed input. This slice does not yet amend the canonical
public `EvidenceDrawerPayload` schema or wire the formatter into the drawer
component; that integration remains a separately reviewable public-contract
change.

## Non-effects

This profile does not retrieve evidence, decide source authority, calculate
precision from raw data, approve a transform, authorize an answer, release a
claim, or publish a map layer. A schema pass proves shape only.

## Rollback

Before merge, close the draft pull request and delete its feature branch. After
an authorized merge, revert the schema/profile/fixture/test/formatter packet.
No source, API route, lifecycle record, release, cache, deployment, or public
artifact is activated.
