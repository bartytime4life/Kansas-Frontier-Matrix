<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/geology-subsurface-public-geometry-assessment-source-map
title: Geology Subsurface Public Geometry Assessment — Source and Repository Reconciliation Map
type: source-map
version: v1.0.0
status: proposed; exploratory; non-canonical; no-source-activation
owners: OWNER_TBD — Geology steward · Subsurface-data steward · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-08-14
updated: 2026-08-14
owning_root: docs/
policy_label: internal; intake; exploratory; geology; subsurface; public-safe-geometry; fixture-only
responsibility: Reconcile the uploaded Geology public-safe geometry plan with current repository BoreholeReference, WellLogReference, geometry-quality, redaction-receipt, and pipeline-assessment evidence and record the smallest distinct no-network implementation slice.
truth_posture: "CONFIRMED uploaded Geology plan and current repository evidence at main@6f095e3c999c9edbfbf3762d7399aac066a08d73; PROPOSED inactive fixture-only assessment semantics; UNKNOWN real source rights, protected geometry, transform fitness, policy/review state, release fitness, and public use; NEEDS VERIFICATION hosted exact-head CI and human review"
related:
  - ../../../contracts/domains/geology/subsurface_public_geometry_assessment.md
  - ../../../schemas/contracts/v1/domains/geology/subsurface_public_geometry_assessment.schema.json
  - ../../../contracts/domains/geology/BoreholeReference.md
  - ../../../contracts/domains/geology/WellLogReference.md
  - ../../../contracts/evidence/geometry_quality_scope_assessment.md
  - ../../../contracts/shared/redaction_receipt.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Geology Subsurface Public Geometry Assessment — Source and Repository Reconciliation Map

## 1. Decision

`IMPLEMENT_REPOSITORY_SLICE` — add one inactive, fixture-only
`GeologySubsurfacePublicGeometryAssessmentCandidate` packet. Do not activate a
source, open restricted material, embed coordinates, execute a transform, change
policy, authenticate a review, create a release candidate, or expose a public layer.

## 2. Source-derived requirement

The uploaded *KFM Geology & Natural Resources Architecture* states that exact
internal geometry may exist only where policy permits and that public geometry must
be generalized, withheld, or denied when sensitivity requires it. It requires every
transform to emit a redaction/generalization receipt and specifically treats private
water-well/borehole and well-log/LAS locations as restricted or withheld by default.
Its thin-slice matrix calls for paired restricted/public borehole and well-log fixtures
that preserve internal references while proving public-safe behavior and evidence
linkage.

The source is a planning report. It does not prove current repository paths, source
rights, policy decisions, transform quality, review, release, or public use.

## 3. Current repository evidence

Pinned comparison: `main@6f095e3c999c9edbfbf3762d7399aac066a08d73`.

| Evidence | CONFIRMED finding |
|---|---|
| `contracts/domains/geology/BoreholeReference.md` | Draft semantic contract already treats a borehole as location-sensitive point evidence, requires internal/public separation, and proposes redaction/aggregation, policy, review, release, correction, and rollback references. |
| `contracts/domains/geology/WellLogReference.md` | Draft semantic contract already keeps exact geometry and LAS/digital payloads restricted by default and allows public references or summaries only with governed support. |
| `schemas/contracts/v1/domains/geology/borehole_reference.schema.json` | Open scaffold with no field-level enforcement. |
| `schemas/contracts/v1/domains/geology/well_log_reference.schema.json` | Open scaffold with no field-level enforcement. |
| `contracts/evidence/geometry_quality_scope_assessment.md` and paired packet | Existing inactive profile owns accuracy/precision separation, attachment scope, and declared derivation coherence, but explicitly does not decide fitness or policy. |
| `schemas/contracts/v1/receipts/redaction_receipt.schema.json` and paired packet | Existing inactive shared profile records transform classes and public summaries while all policy/review/lifecycle/release/publication authority remains false. |
| `tools/validators/validate_geology_pipeline_specification_assessment.py` | Existing inactive Geology profile requires controlled sensitivity and datum/depth closure for borehole and well-log specification declarations but does not assess one public projection. |
| Repository-wide candidate search | No `GeologySubsurfacePublicGeometryAssessmentCandidate` or equivalent closed profile was found. |

## 4. Distinctness and dependency closure

This packet composes existing owners rather than replacing them:

1. `BoreholeReference` and `WellLogReference` remain semantic object owners.
2. `GeometryQualityScopeAssessmentCandidate` remains quality/precision and derivation-declaration owner.
3. `RedactionReceipt` remains transform process-memory owner.
4. Policy, review, evidence, lifecycle, release, and publication owners remain outside this packet.
5. The new assessment owns only declaration coherence across those references for a synthetic public projection.

The candidate stores only opaque digests and synthetic references. No geometry,
coordinates, source IDs, site names, protected values, or transform parameters are
present.

## 5. Directory Rules decision

Accepted ADR-0029 and the adopted Directory Rules assign:

- meaning to `contracts/domains/geology/`;
- machine shape to `schemas/contracts/v1/domains/geology/`;
- synthetic replay to `fixtures/contracts/v1/domains/geology/`;
- bounded validation entry points to top-level `tools/validators/validate_*.py`;
- focused tests to `tests/validators/domains/geology/`;
- read-only orchestration to `.github/workflows/`;
- non-canonical source reconciliation to `docs/intake/exploratory/`; and
- AI authoring provenance to `data/receipts/generated/`.

The top-level validator entry point is deliberate. The `domain-geology` workflow has
a frozen accepted-validator inventory for substantive files under its domain-specific
validator directories; this candidate is a contract assessment, not an accepted live
Geology pipeline validator.

No new responsibility root or parallel source, policy, evidence, receipt, proof,
release, or publication authority is created.

## 6. Validation boundary

Local validation proves Draft 2020-12 schema meta-validity, Python compilation,
exact fixture polarity, deterministic identity and replay, duplicate/non-finite JSON
rejection, no-network behavior, workflow YAML syntax, generated-receipt hash closure,
and whitespace hygiene.

It cannot prove source admission, source rights, protected-geometry handling,
transform correctness, geometry fitness, policy execution, authenticated review,
evidence support, lifecycle transitions, release, deployment, publication, or public
use. Those remain `UNKNOWN` or `NEEDS VERIFICATION`.

Current-main `telemetry-policy` failure from the latest ADR documentation merge
predates this branch and is classified as inherited baseline until exact-head evidence
proves otherwise.

## 7. Rollback

Before merge, abandon the additive packet. After an authorized merge, revert its one
bounded commit. No live source, geometry, lifecycle object, cache, release,
deployment, or public artifact requires restoration.
