<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-xy-point-transform-receipt
title: Pass 18 XY Point Transform Receipt Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD — Intake steward · Spatial Foundation steward · Evidence steward
created: 2026-08-10
updated: 2026-08-10
owning_root: docs/
policy_label: internal; source-lineage; spatial-foundation; coordinate-creation
responsibility: Preserve exact source lineage and repository reconciliation for the bounded XY point-transform receipt adaptation without promoting proposal material into coordinate truth, evidence, policy, release, or publication authority.
truth_posture: "CONFIRMED attached-card transcription and inspected-repository comparison; PROPOSED bounded adaptation; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/spatial-foundation/xy_point_transform_receipt.md
  - ../../../schemas/contracts/v1/spatial-foundation/xy_point_transform_receipt.schema.json
  - ../../../fixtures/contracts/v1/spatial-foundation/xy_point_transform_receipt/cases.json
  - ../../../docs/doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 XY Point Transform Receipt Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, physical page 42 / printed page 39 | Card `KFM-P18-INV-174` proposes treating XY-to-point conversion as coordinate creation with declared X/Y fields, CRS, precision, source table, validation checks, and fixtures for axis swap, out-of-range coordinates, and missing CRS. | `CONFIRMED` |
| Connected Drive `KFM_Full_Atlas_seed_cards` (`1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`) | The Drive atlas contains broader transform-receipt and no-network fixture pressure, but no exact `KFM-P18-INV-174` identity was established. It was used as thematic discovery input, not exact-card authority. | `CONFIRMED` thematic-only |
| `main@ef1ba46a19e4de7c176e9d093c1285e73a0af75a` | Exact card-ID, XY-to-point, table-to-point, and candidate branch/PR searches found no matching contract, schema, fixture family, validator, workflow, or active implementation branch. Existing Spatial Foundation contracts cover boundary derivation and lidar lineage, not tabular coordinate creation. | `CONFIRMED` for the inspected snapshot |

The supplied and Drive artifacts are proposal evidence, not repository instruction authority. No external CRS registry, GIS package, or live source was consulted or activated.

## Reconciliation and selected increment

The repository already owns geometry and transform-lineage concepts across domain and cross-domain surfaces. Expanding an existing object without an exact semantic match could create compatibility or authority drift.

The selected increment is therefore one additive Spatial Foundation receipt **candidate**. It records declared inputs, assumptions, checks, and count consequences without executing a transform or changing an existing object family.

## Source-to-profile mapping

| Source pressure | Bounded adaptation | Held boundary |
|---|---|---|
| Declare X and Y fields. | Distinct field names plus one of three supported semantic-role pairs. | No field-name inference or source-table access. |
| Declare CRS. | Pinned opaque CRS ref/digest and explicit resolution state. | No CRS parsing, registry admission, reprojection, or suitability claim. |
| Declare precision. | Maximum and observed decimal-place counts for both fields. | No claim about measurement accuracy or source resolution. |
| Validate coordinate ranges. | Declared and observed finite envelopes with containment checks. | No proof that declared bounds are correct for a real CRS. |
| Detect swapped axes. | Exact X/Y semantic-role pairing and a declared check result. | No heuristic detection from real values. |
| Preserve transform evidence. | Source/output digests, count reconciliation, validation reason counts, and evidence refs. | Receipt candidate is process memory, not an EvidenceBundle, proof, review, or release decision. |
| Prevent direct-observation collapse. | All observation, evidence, policy, review, promotion, release, publication, and public-use claims are fixed false. | No domain observation or public layer is created. |

## Directory Rules basis

`contracts/spatial-foundation/README.md` assigns cross-domain spatial representation, reference-system, transform-lineage, and fitness-for-use semantics to this contract lane. Shape, fixtures, validator, tests, workflow, source mapping, and generated receipt remain in their established responsibility roots under accepted ADR-0029. No new root or parallel authority is introduced.

## Deferred questions

- Which admitted CRS registry and parser may authenticate CRS identity and axis semantics?
- Which source roles, rights, sensitivity postures, and review classes may permit real table access?
- Which transforms require manual reviewer approval?
- How should vertical, temporal, compound, dynamic, or uncertain reference systems be represented?
- Which downstream lifecycle object may consume a reviewed receipt candidate?

These questions require separate decisions. This profile fixes none of them.

## Validation and rollback

Focused validation covers closed shape, deterministic identity, UTC timestamps, unresolved-binding abstention, distinct and correctly paired axes, declared/observed bounds, decimal precision, row/rejection/output count reconciliation, CRS binding parity, canonical evidence references, hash tampering, and unknown-field rejection.

Rollback is a focused revert of this additive packet. No source reprocessing, point deletion, correction notice, release withdrawal, cache invalidation, UI cleanup, or public cleanup is required because the profile has no consumer and contains no coordinates.
