<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-obligation-propagation-assessment
title: SourceObligationPropagationAssessment Contract
type: semantic-contract; source-rights propagation; fixture-only assessment
version: v0.1.0
status: proposed; inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Source steward · Rights reviewer · Release steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
policy_label: internal; source; rights; attribution; derivative-use; review-required
related:
  - ./source_descriptor.md
  - ./source_artifact.md
  - ./source_rights_currentness_assessment.md
  - ../../contracts/release/release_manifest.md
  - ../../schemas/contracts/v1/source/source_obligation_propagation_assessment.schema.json
  - ../../fixtures/contracts/v1/source/source_obligation_propagation_assessment/cases.json
  - ../../tools/validators/source/validate_source_obligation_propagation_assessment.py
  - ../../tests/validators/test_validate_source_obligation_propagation_assessment.py
tags: [kfm, source, attribution, rights, redistribution, derivative-use, propagation, fixture-only]
notes:
  - "Adapts the comprehensive research report's requirement that attribution and use restrictions survive into every derived and exported carrier."
  - "References existing source-rights/currentness and artifact objects opaquely; it creates no rights, policy, release, or publication authority."
[/KFM_META_BLOCK_V2] -->

# SourceObligationPropagationAssessment

## Status and purpose

`SourceObligationPropagationAssessment` is a **PROPOSED**, fixture-only
declaration that checks whether source attribution, terms, required notices,
redistribution posture, and derivative-use posture remain visible across a
bounded carrier chain.

It complements the existing `SourceRightsCurrentnessAssessment`. That existing
object asks whether source identity, terms, rights, attribution, redistribution,
derivative use, access, and cadence have a coherent dated review posture. This
candidate asks a different question:

> Once those obligations are declared, did every downstream carrier preserve
> them, or did a derivative, catalog record, or export candidate silently drop
> them?

A validator `PASS` proves only internal consistency of a synthetic declaration.
It does not verify the referenced source, terms, rights review, artifacts,
transform receipts, catalog records, release manifests, or exported bytes.

## Bounded carrier chain

The candidate recognizes three target scopes and one exact stage sequence for
each:

| Target | Required sequence |
|---|---|
| `INTERNAL_DERIVATIVE` | `SOURCE_ARTIFACT -> PROCESSED_DERIVATIVE` |
| `CATALOG_CANDIDATE` | previous stages, then `CATALOG_RECORD` |
| `EXPORT_CANDIDATE` | previous stages, then `EXPORT_CANDIDATE` |

Every carrier declares an artifact reference, exact-byte digest, terms
reference, attribution reference when required, required notices,
transform-receipt reference for downstream stages, and whether it is being
considered for public exposure.

The stage sequence is a review declaration, not a lifecycle write or release
manifest.

## Finite states

| Assessment status | Validator outcome | Meaning |
|---|---|---|
| `COMPLETE` | `PASS` | The synthetic chain preserves all declared obligations for the target scope. |
| `REVIEW_DUE` | `ABSTAIN` | The upstream rights/currentness review must be refreshed before relying on the propagation result. |
| `BLOCKED` | `DENY` | Rights, attribution, use posture, chain closure, notices, terms, transform lineage, or restricted-public posture is unresolved or inconsistent. |
| `ERROR` | `ERROR` | The assessment explicitly records an evaluation failure. |

## Core invariants

- `source_descriptor_ref` binds exactly to `source_id`.
- The source-rights/currentness assessment is referenced, not replaced.
- Unknown, denied, or permission-dependent rights fail closed.
- An export candidate requires explicitly `ALLOWED` redistribution.
- Every derivative target requires explicitly `ALLOWED` derivative use.
- Required notices are a subset of every carrier's notices.
- Terms references remain identical through the whole chain.
- Required attribution uses one declared attribution reference through the
  whole chain.
- Every downstream carrier has a transform receipt reference; the source
  artifact does not.
- A restricted-rights source cannot be represented as a public candidate by
  this fixture lane.
- `assessment_id` and `spec_hash` are deterministic RFC 8785 JCS plus SHA-256
  identities over the complete declaration.
- All source activation, artifact creation, evidence, lifecycle write, policy,
  promotion, release, publication, export execution, and public-use effects
  remain false.

## Directory Rules basis

Accepted ADR-0029 makes Directory Rules v2 effective. The primary authority is
the semantic meaning of source obligations and their declared propagation, so
the contract belongs under `contracts/source/`. Machine shape, synthetic
fixtures, validation, executable proof, read-only CI, source adaptation, and
generated authoring provenance remain in their owning responsibility roots.

The candidate composes `SourceRightsCurrentnessAssessment`, `SourceArtifact`,
transform receipts, catalog records, and release candidates by opaque reference.
It does not create a parallel source registry, rights registry, policy home,
receipt family, catalog authority, proof store, release home, or public route.

## Validation

```bash
python -m unittest -v tests.validators.test_validate_source_obligation_propagation_assessment
python tools/validators/source/validate_source_obligation_propagation_assessment.py --fixtures
```

## Non-effects

This packet does not:

- fetch a source, open bytes, or activate a connector;
- make a copyright, license, terms, consent, or public-domain decision;
- resolve the referenced rights assessment, artifacts, notices, or receipts;
- create evidence, catalog closure, proof, policy, review, or release authority;
- execute an export or publish a carrier; or
- weaken any more restrictive upstream obligation.

## Rollback

Before merge, close the draft pull request and delete only its feature branch.
After an authorized merge, revert the additive packet and rerun the dedicated
workflow. No source, external artifact, lifecycle record, release, deployment,
export, or public state requires restoration.
