<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/geology/geology-pipeline-specification-assessment
title: Geology Pipeline Specification Assessment Candidate Contract
type: contract
version: v1.0.0
status: proposed; inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Geology steward · Pipeline-spec steward · Source/rights steward · Spatial/datum reviewer · Validation steward
created: 2026-08-12
updated: 2026-08-12
owning_root: contracts/
policy_label: internal; proposed; geology; natural-resources; pipeline-spec; fixture-only
responsibility: Define a bounded declaration contract for assessing whether a proposed Geology pipeline specification preserves source role, object role, knowledge character, scale/depth/datum, sensitivity, lifecycle, correction, and anti-collapse boundaries without activating a source or pipeline.
truth_posture: "CONFIRMED uploaded Geology architecture support and current repository placeholder gap; PROPOSED inactive declaration semantics; UNKNOWN real source admission, parser/consumer fitness, runtime behavior, rights, sensitivity, evidence, and review acceptance; NEEDS VERIFICATION geology, source, rights, spatial, validation, policy, and release review"
related:
  - ../../../pipeline_specs/geology/README.md
  - ../../../schemas/contracts/v1/domains/geology/geology_pipeline_specification_assessment.schema.json
  - ../../../docs/intake/exploratory/geology-pipeline-specification-assessment-source-map.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Geology Pipeline Specification Assessment Candidate Contract

## 1. Status and purpose

This contract is `PROPOSED_INACTIVE` and `FIXTURE_ONLY`. It defines a
`GeologyPipelineSpecificationAssessmentCandidate` that can evaluate a synthetic
pipeline-specification declaration without executing the specification, contacting
a source, resolving a reference, or moving any lifecycle object.

The assessment exists because the current Geology specification lane contains six
named placeholder files but no accepted active specification, parser, registry,
consumer binding, source activation record, or executable conformance profile. It
turns that documented gap into one bounded, deterministic review surface rather
than silently upgrading any placeholder to operational authority.

## 2. Source basis and bounded adaptation

The uploaded *KFM Geology & Natural Resources Architecture* report requires the
Geology lane to preserve observed, interpreted, modeled, administrative, resource,
and public-visualization roles instead of flattening them into one truth layer. It
also recommends beginning with source descriptors, schema/contract closure,
fixtures, source-role policy, public-safe geometry checks, and one offline slice
before live harvesting or UI work.

Current repository evidence sharpens that recommendation: `pipeline_specs/geology/`
contains six seven-line `PROPOSED` placeholders and explicitly reports no active
specification. This contract therefore assesses declarations only. It does not
replace the existing Geology object-family, source-registry, policy, pipeline,
receipt, proof, or release owners.

## 3. Canonical object

The paired schema requires:

- fixed object, schema, profile, and source-packet identifiers;
- deterministic `spec_hash` and `assessment_id` values;
- a UTC `recorded_at` timestamp;
- a proposed inactive specification identity, family, parser and consumer bindings;
- admitted-source references, source roles, rights posture, and an inactive source state;
- object roles, knowledge character, resource-claim class, and anti-collapse assertions;
- spatial support, horizontal CRS, scale, vertical/depth references where material,
  source vintage, temporal scope, uncertainty, and sensitivity posture;
- fixture-only/no-network lifecycle constraints plus validation, evidence-requirement,
  correction, and rollback references;
- source-rights, sensitivity, geology, and validation review references; and
- explicit limitations and schema-locked false authority claims.

References are opaque synthetic identifiers. Their presence demonstrates declared
closure only; the validator never dereferences or authenticates them.

## 4. Identity

Identity is content-derived:

1. Remove `spec_hash` and `assessment_id`.
2. Serialize the remaining object as UTF-8 JSON with sorted keys, no insignificant
   whitespace, and no non-finite numbers.
3. Set `spec_hash` to `sha256:<lowercase digest>`.
4. Set `assessment_id` to
   `kfm:geology:pipeline-specification-assessment:<first 24 digest characters>`.

Reference and vocabulary arrays must be sorted and duplicate-free. Any material
change to source roles, object roles, spatial/temporal support, lifecycle, reviews,
limitations, or authority declarations changes identity.

## 5. Profile-specific anti-collapse rules

| Family | Required object/support | Required knowledge and boundary |
|---|---|---|
| `BEDROCK_UNITS` | `GeologicUnit`; `MAP_UNIT_POLYGON` | `INTERPRETED`; `MAP_UNIT_NOT_POINT_TRUTH` |
| `SURFICIAL_UNITS` | `SurficialUnit`; `MAP_UNIT_POLYGON` | `INTERPRETED`; `MAP_UNIT_NOT_POINT_TRUTH` |
| `BOREHOLES` | `BoreholeReference`; `BOREHOLE_POINT` | `OBSERVED`; controlled sensitivity; depth reference; `GENERALIZED_GEOMETRY_NOT_PUBLIC_APPROVAL` |
| `WELL_LOGS` | `WellLogReference`; `WELL_LOG_INTERVAL` | `MEASURED` or `OBSERVED`; controlled sensitivity; depth and vertical-datum references |
| `CROSS_SECTIONS` | `CrossSection`; `CROSS_SECTION_2D` | `INTERPRETED` or `MODELED`; `INTERPRETATION_NOT_OBSERVATION`; scale, depth, and vertical datum |
| `MINERAL_OCCURRENCES` | `MineralOccurrence`; `OCCURRENCE_POINT_OR_AREA` | resource class `OCCURRENCE`; `OCCURRENCE_NOT_DEPOSIT_OR_ESTIMATE` |

A valid declaration cannot turn a map-unit polygon into verified point geology, a
borehole or well log into regional continuity, a cross-section or model into an
observation, a mineral occurrence into a deposit/estimate/reserve, an
administrative record into physical geology, generalized geometry into public
approval, or a successful run into evidence or release.

## 6. Completeness and unresolved states

A `COMPLETE` assessment requires parser and consumer references, a claim-scope
statement, source and review closure, horizontal CRS, source vintage, temporal and
uncertainty references, validation/evidence-requirement profiles, correction and
rollback references, and profile-specific scale/depth/datum fields.

`INCOMPLETE` and `UNKNOWN` assessments return `ABSTAIN`. Unresolved rights or
sensitivity also return `ABSTAIN`. A denied rights posture or a contradictory
profile declaration returns `DENY`. A declared assessment error returns `ERROR`.

## 7. Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The synthetic inactive declaration is schema-valid, identity-valid, complete, and coherent under this profile. |
| `ABSTAIN` | Parser/consumer, rights, sensitivity, review, or closure information remains unresolved. |
| `DENY` | The declaration is invalid, contradictory, collapses source/object meaning, or claims forbidden authority. |
| `ERROR` | The declaration reports an assessment error, or safe JSON loading fails. |

Outcome precedence is schema, identity, declared error, semantic coherence,
unresolved information, then pass. `PASS` is never source admission, pipeline
activation, evidence, policy, review, release, publication, or public-use authority.

## 8. Input safety and deterministic replay

The validator accepts one local JSON object no larger than 1 MiB and rejects
symlinks, missing/non-file inputs, duplicate keys, non-finite numbers, invalid
UTF-8, malformed JSON, and non-object roots. It performs no network access and
replays a synthetic fixture matrix across all four finite outcomes.

## 9. Explicit non-effects

This packet does not:

- replace or activate any of the six existing Geology placeholder specifications;
- establish a parser, registry, scheduler, consumer, connector, source descriptor,
  rights decision, or runtime configuration;
- retrieve, transform, model, infer, map, expose, or publish geology or natural-resource data;
- establish evidence, positional/geologic truth, resource status, title, permit,
  production, reserve, reclamation completion, or public safety;
- expose exact borehole, well-log, resource-target, infrastructure, parcel, or site geometry;
- mutate RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, PUBLISHED,
  receipt, proof, release, correction, or rollback state; or
- authorize policy, review, promotion, release, deployment, publication, or public use.

## 10. Activation and rollback

Activation requires a later separately reviewed decision that selects the canonical
specification schema, parser, registry, executable consumer, admitted sources,
rights and sensitivity posture, object/claim roles, spatial/temporal contracts,
receipt/proof/release integration, operational limits, correction propagation, and
rollback authority.

Rollback of this inactive slice is deletion of its contract, schema, fixtures,
validator, tests, workflow, source map, and generated authoring receipt. It has no
live consumer, data migration, source activation, or external state to unwind.
