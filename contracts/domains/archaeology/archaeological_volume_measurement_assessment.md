<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/archaeology/archaeological-volume-measurement-assessment
title: Archaeological Volume Measurement Assessment Candidate Contract
type: contract
version: v1.0.0
status: proposed; inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Archaeology steward · 3D documentation steward · Evidence steward · Cultural review steward · Validation steward
created: 2026-08-12
updated: 2026-08-12
owning_root: contracts/
policy_label: internal; proposed; archaeology; three-d; measurement; uncertainty; fixture-only
responsibility: Define a bounded declaration contract that keeps archaeological volume measurements and their uncertainty distinct from visual 3D carriers while granting no measurement-truth, evidence, interpretation, policy, review, release, publication, or public-use authority.
truth_posture: "CONFIRMED source-card support and current repository gap; PROPOSED inactive declaration semantics; UNKNOWN real measurements, asset/reference validity, method fitness, uncertainty fitness, and review acceptance; NEEDS VERIFICATION archaeology, cultural, technical, evidence, policy, release, and human review"
related:
  - three_d_documentation.md
  - ../../../schemas/contracts/v1/domains/archaeology/archaeological_volume_measurement_assessment.schema.json
  - ../../../docs/intake/exploratory/pass-18-archaeological-volume-measurement-assessment-source-map.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Archaeological Volume Measurement Assessment Candidate Contract

## 1. Status and purpose

This contract is `PROPOSED_INACTIVE` and `FIXTURE_ONLY`. It defines the shape
and deterministic coherence checks for an
`ArchaeologicalVolumeMeasurementAssessmentCandidate`.

The object records a volume value, its declared method, source-documentation
references, measurement receipt, uncertainty, and governance closure as a
separate analytical candidate. A mesh, CT volume, voxel carrier, or other 3D
asset may be an input reference; it is never the assessment object itself.

Conformance means only that the supplied declaration is structurally and
semantically coherent under this profile. It does not establish that a volume
is true, that a method is appropriate, that an asset or reference exists, or
that any review or release decision has occurred.

## 2. Source and bounded adaptation

Pass 18 card `KFM-P18-INV-435` proposes treating archaeological volume
measurements, including CT-derived and deposit-volume estimates, as evidence
objects distinct from visual meshes. This implementation adapts that proposal
into the existing Archaeology contract family and composes with
`ThreeDDocumentation` by opaque reference.

It does not create a second 3D asset owner, duplicate capture or processing
paradata, or alter any existing runtime. All examples use synthetic references
and contain no coordinates or real site identifiers.

## 3. Canonical object

The paired JSON Schema is the machine-readable shape owner. The object requires:

- fixed `object_type`, profile, schema version, and source-card identifiers;
- a deterministic `assessment_id` and `spec_hash`;
- a UTC `recorded_at` timestamp;
- an opaque archaeological subject reference, kind, and measurement scope;
- an opaque `ThreeDDocumentation` reference plus declared analytical inputs;
- distinct visual-mesh and volumetric-input roles;
- method, algorithm, scale-basis, processing-receipt, and specialist-review declarations;
- measurement state, positive value, unit, precision, and measurement receipt;
- quantified, qualitative, or unresolved uncertainty declarations;
- evidence, rights, technical/cultural review, policy, sensitivity, and reversible lifecycle references; and
- explicit limitations and schema-locked false authority claims.

Reference strings are opaque identifiers. The validator does not dereference
them. Reference arrays must be sorted and duplicate-free so identity and
replay remain deterministic.

## 4. Identity

Identity is content-derived:

1. Remove `spec_hash` and `assessment_id`.
2. Serialize the remaining object as UTF-8 JSON with sorted keys, no
   insignificant whitespace, and no non-finite numbers.
3. Set `spec_hash` to `sha256:<lowercase digest>`.
4. Set `assessment_id` to
   `kfm:archaeology:volume-measurement-assessment:<first 24 digest characters>`.

Any change to the subject, source roles, method, value, uncertainty, governance,
limitations, or authority declarations therefore changes identity.

## 5. Separation from 3D carriers

`source_documentation` preserves the boundary between analytical claim and
carrier:

- `three_d_documentation_ref` points to the governing 3D documentation object;
- `input_asset_refs` declares every synthetic input used by the assessment;
- `visual_mesh_refs` identifies inputs serving as visual meshes;
- `volumetric_input_refs` identifies CT, voxel, segmentation, or other
  volumetric inputs; and
- `source_separation_statement` explains why the measurement record remains a
  separate analytical candidate.

Every visual or volumetric role must also appear in `input_asset_refs`.
`CT_DERIVED` and `VOXEL_COUNT` methods require a volumetric input.
`MESH_DERIVED` requires a visual-mesh input. These checks describe reference
coherence only; they do not inspect or calculate from an asset.

## 6. Measurement and uncertainty

A `COMPLETE` measurement requires a positive value, declared unit and
precision, measurement receipt, scale-basis reference, and processing receipt.
Missing closure is a `DENY`, because a declaration cannot claim completeness
while omitting the records that explain the calculation.

For `QUANTIFIED` uncertainty, lower and upper bounds, confidence level, and an
uncertainty-profile reference are required. Bounds must be ordered and contain
the declared measurement. `QUALITATIVE` uncertainty requires a narrative and
must not carry numeric bounds. `UNRESOLVED` uncertainty must not invent numeric
detail and results in `ABSTAIN`.

The validator does not judge scientific adequacy, compare methods, calculate
statistics, or convert units.

## 7. Governance posture

The candidate records opaque references for evidence bundle, rights,
technical review, cultural review, policy decision, and reversible publication
closure. Their presence is not proof that the referenced actions occurred.

An `INTERNAL_REVIEW` candidate must not carry publication-transform, release,
correction, or rollback references. A `PUBLIC_CANDIDATE` must declare a
`PUBLIC_SAFE_REVIEWED` sensitivity posture and all four reversible closure
references. Even then, this contract grants no release or publication authority.

If specialist review is declared necessary and no technical-review reference
is present, the validator returns `ABSTAIN`.

## 8. Outcomes

The local validator returns one finite outcome with sorted finding codes:

| Outcome | Meaning |
|---|---|
| `PASS` | The synthetic declaration is schema-valid, identity-valid, complete, and coherent under this inactive profile. |
| `ABSTAIN` | Required measurement, uncertainty, governance, or specialist-review information remains unresolved. |
| `DENY` | The declaration is invalid, contradictory, improperly closed, or claims forbidden authority. |
| `ERROR` | The measurement or governance declaration explicitly reports an error, or safe JSON loading fails. |

Outcome precedence is schema, identity, declared error, coherence, unresolved
information, then pass. `PASS` never upgrades any truth or authority label.

## 9. Input safety and deterministic replay

The validator:

- accepts one local JSON object no larger than 1 MiB;
- rejects symlinks, missing/non-file inputs, duplicate keys, non-finite numbers,
  invalid UTF-8, malformed JSON, and non-object roots;
- performs no network access or reference resolution;
- sorts findings and derives identity from canonical JSON; and
- replays a fixed synthetic fixture matrix covering `PASS`, `ABSTAIN`, `DENY`,
  and `ERROR`.

## 10. Explicit non-effects

This packet does not:

- read, write, transform, render, publish, or delete a 3D asset;
- calculate or certify a volume;
- establish archaeological evidence, provenance, interpretation, significance,
  ownership, rights, or site status;
- reveal coordinates, geometry, exact locations, or protected-site details;
- approve technical, cultural, policy, privacy, security, or release review;
- activate a data source, API, map layer, renderer, workflow trigger outside the
  path-scoped fixture check, or deployment; or
- authorize release, publication, public use, correction, or rollback.

## 11. Activation and rollback

Activation requires a later, separately reviewed decision that identifies the
canonical runtime owner, migration path, real data classification, method and
uncertainty governance, cultural and technical reviewers, evidence handling,
release controls, correction plan, and rollback authority. This proposal makes
none of those decisions.

Rollback of this inactive slice is deletion of the paired contract, schema,
fixtures, validator, tests, workflow, source map, and authoring receipt. Because
the slice has no live consumers or source activation, rollback requires no data
migration.
