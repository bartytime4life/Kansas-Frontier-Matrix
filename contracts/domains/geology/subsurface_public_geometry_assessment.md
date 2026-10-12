<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/geology/subsurface-public-geometry-assessment
title: Geology Subsurface Public Geometry Assessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed; inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Geology steward · Subsurface-data steward · Sensitivity reviewer · Contract steward · Validation steward
created: 2026-08-14
updated: 2026-08-14
owning_root: contracts/
policy_label: internal; geology; subsurface; public-safe-geometry; fixture-only; deny-by-default
responsibility: Define the finite declaration contract used to assess whether a synthetic BoreholeReference or WellLogReference public-geometry projection preserves internal/external geometry separation, rights and sensitivity holds, transform receipts, quality-scope references, and non-authority boundaries.
truth_posture: "CONFIRMED current repository BoreholeReference and WellLogReference semantic contracts, open schema scaffolds, shared fixture-only RedactionReceipt profile, GeometryQualityScopeAssessment profile, and prior Geology pipeline-specification assessment; PROPOSED this inactive assessment profile; UNKNOWN real source rights, protected geometry, policy decisions, authenticated review, operational transforms, release fitness, and public-use authority; NEEDS VERIFICATION hosted exact-head CI and human review"
related:
  - ./BoreholeReference.md
  - ./WellLogReference.md
  - ../../../schemas/contracts/v1/domains/geology/subsurface_public_geometry_assessment.schema.json
  - ../../../docs/domains/geology/SENSITIVITY.md
  - ../../../docs/domains/geology/sublanes/boreholes-wells.md
  - ../../shared/redaction_receipt.md
  - ../../evidence/geometry_quality_scope_assessment.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Geology Subsurface Public Geometry Assessment Candidate

## 1. Status and purpose

This contract is `PROPOSED_INACTIVE` and `FIXTURE_ONLY`. It defines
`GeologySubsurfacePublicGeometryAssessmentCandidate`, a declaration that can be
validated without opening restricted source material, embedding coordinates,
executing a transform, contacting a source, making a policy decision, authenticating
a reviewer, changing lifecycle state, or authorizing release or publication.

The assessment closes one bounded gap between existing repository surfaces:

- `BoreholeReference` already requires restricted internal geometry and governed
  generalized or aggregated public derivatives;
- `WellLogReference` already keeps exact well/log geometry and LAS or digital payloads
  restricted by default;
- `GeometryQualityScopeAssessmentCandidate` already distinguishes accuracy,
  precision, attachment scope, and declared derivation without deciding fitness;
- `RedactionReceipt` already records fixture-only transform classes while granting no
  policy, review, release, or publication authority; and
- `GeologyPipelineSpecificationAssessmentCandidate` already requires controlled
  sensitivity for boreholes and well logs but does not assess a specific public
  projection declaration.

This packet assesses only the last declaration boundary. It does not replace any of
those owners.

## 2. Canonical subject

A candidate describes one synthetic subject:

- `BoreholeReference`; or
- `WellLogReference`.

The subject is represented by an opaque SHA-256 digest and synthetic references. No
coordinate, geometry, site name, well identifier, protected payload, or reversible
transform parameter is allowed in the candidate or fixture manifest.

## 3. Internal-support boundary

Every candidate declares:

- `geometry_state = REFERENCED_NOT_EMBEDDED`;
- an input precision class of `EXACT` or `SOURCE_PRECISION`;
- horizontal CRS, vertical datum, and depth-reference posture;
- restricted-access status;
- a payload state; and
- source role, rights, sensitivity, and inactive source state.

A complete borehole declaration requires horizontal CRS and depth reference. A
complete well-log declaration also requires vertical datum. These declarations do not
prove that the referenced values are correct.

## 4. Public-projection boundary

The public projection uses one finite disposition:

| Disposition | Required declaration | Forbidden implication |
|---|---|---|
| `GENERALIZED` | Public-safe digest, non-exact precision class, geometry-quality-scope assessment reference, redaction-receipt reference, reason code, public summary | Generalization is not policy approval, source accuracy, review, release, or exact geometry. |
| `WITHHELD` | No public geometry digest, `WITHHELD` precision, redaction-receipt reference, reason code, public summary | Withholding does not prove a policy decision was executed. |
| `DENIED` | No public geometry digest, `NONE` precision, denial reason and summary | A denial declaration is not an authenticated policy decision. |
| `NONE` | Used only while the assessment is incomplete or unknown | No public projection is claimed. |

`EXACT` and `SOURCE_PRECISION` are valid input precision classes but are always denied
for a public projection. Well-log payload state must remain `REFERENCE_ONLY` or
`WITHHELD`; borehole source payloads must not be declared public.

## 5. Anti-collapse assertions

Every complete candidate carries all of these assertions:

1. `BOREHOLE_POINT_NOT_REGIONAL_CONTINUITY`;
2. `EXACT_INTERNAL_GEOMETRY_NOT_PUBLIC`;
3. `GENERALIZED_GEOMETRY_NOT_PUBLIC_APPROVAL`;
4. `SUCCESSFUL_ASSESSMENT_NOT_POLICY_REVIEW_RELEASE`; and
5. `WELL_LOG_REFERENCE_NOT_PAYLOAD_RELEASE`.

The fixed shared set is intentional. It prevents a family-specific declaration from
silently weakening the cross-family boundary.

## 6. Deterministic identity

Identity is content-derived:

1. Remove `spec_hash` and `assessment_id`.
2. Serialize canonical UTF-8 JSON with sorted keys, no insignificant whitespace, and
   no non-finite numbers.
3. Set `spec_hash` to `sha256:<lowercase digest>`.
4. Set `assessment_id` to
   `kfm:geology:subsurface-public-geometry-assessment:<first 24 digest characters>`.

Reference and vocabulary arrays must be sorted and duplicate-free. Any material
change to source role, precision, CRS/datum/depth posture, transform closure, rights,
sensitivity, review references, correction/rollback references, or authority claims
changes identity.

## 7. Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The synthetic declaration is schema-valid, identity-valid, complete, and internally coherent. It is ready only for human review of the declaration. |
| `ABSTAIN` | Rights, sensitivity, assessment state, parser-equivalent closure, or required review/validation references remain unresolved without an adverse contradiction. |
| `DENY` | The declaration is invalid, contradictory, non-canonical, exposes or implies unsafe precision/payload, lacks transform closure, or claims forbidden authority. |
| `ERROR` | The declaration reports an assessment error or safe JSON loading fails. |

A `PASS` grants no source admission, policy permission, authenticated review, geometry
fitness, evidence authority, lifecycle transition, release, publication, or public use.

## 8. Input safety and replay

The validator accepts one local JSON object no larger than 1 MiB and rejects symlinks,
missing files, duplicate keys, non-finite numbers, malformed UTF-8/JSON, and non-object
roots. Fixture replay is deterministic and performs no network access.

## 9. Explicit non-effects

This packet does not:

- open, store, transform, compare, or expose real geometry;
- establish public-safe distance, grid, county, or aggregation thresholds;
- execute `policy/`, authenticate a review record, or certify rights;
- create or activate a source descriptor, connector, parser, pipeline, layer, API,
  EvidenceBundle, proof, release candidate, or published artifact;
- release a LAS file, digital well log, private-well location, borehole identifier, or
  transform parameter;
- mutate RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, PUBLISHED,
  receipt, proof, correction, rollback, or release state; or
- supersede the existing BoreholeReference, WellLogReference,
  GeometryQualityScopeAssessment, RedactionReceipt, or Geology pipeline-specification
  assessment contracts.

## 10. Activation and rollback

Operational activation requires a separate reviewed decision that selects canonical
object schemas, source descriptors, policy and sensitivity rules, authenticated review
records, transform implementations, geometry-quality profiles, release integration,
correction propagation, rollback authority, and public-interface behavior.

Before merge, abandon this additive packet. After an authorized merge, revert its one
bounded commit. No live source, geometry, lifecycle object, cache, release, deployment,
or public surface requires restoration.
