<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-18-claim-scope-dimension-assessment-source-map
title: Pass 18 Claim Scope Dimension Assessment Source Map
type: source-map
version: v1.0.0
status: exploratory; implementation-mapped; non-authoritative
owners: OWNER_TBD — Intake steward · Evidence steward · Spatial representation steward
created: 2026-08-10
updated: 2026-08-10
owning_root: docs/
policy_label: internal; exploratory; source-reconciliation; claim-scope
responsibility: Reconcile one supplied time-space-attribute idea with current repository evidence while withholding private discovery-source identifiers from public provenance.
truth_posture: "CONFIRMED supplied-card and repository gap; PROPOSED inactive implementation profile; UNKNOWN consumer adoption; NEEDS VERIFICATION human review and hosted CI"
related:
  - ../../../contracts/evidence/claim_scope_dimension_assessment.md
  - ../../../contracts/evidence/measurement_scale_operation_assessment.md
  - ../../../contracts/evidence/representation_fitness_assessment.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Claim Scope Dimension Assessment Source Map

## Source and gap

| Evidence | Observation | Status |
|---|---|---|
| Supplied Pass 18 card `KFM-P18-INV-376` | A spatial claim should make clear which of time, space, and attribute is controlled and which is measured so its representation scope is inspectable. | `CONFIRMED` source statement |
| Existing representation and measurement assessments | Current profiles address representation support and operation compatibility but do not declare the time-space-attribute role partition for one claim. | `CONFIRMED` adjacent contracts |
| Current `main` search | No exact claim-scope dimension assessment contract, schema, fixture family, validator, workflow, or matching historical PR was found before implementation. | `CONFIRMED` bounded gap |
| Connected private research corpus | Used only for candidate discovery and corroboration. Private filenames, IDs, URLs, hashes, and copied prose are intentionally excluded. | `CONFIRMED` provenance boundary |

## Adaptation

The implementation is a closed synthetic assessment candidate under the existing evidence family. It records references and digests for one claim, one declared EvidenceBundle scope, and three dimension declarations. A complete candidate requires at least one controlled and one measured dimension; unresolved dimensions or evidence scope abstain unless a complete declaration overstates closure, which fails closed.

The profile does not encode coordinates, observed values, or source payloads. It does not infer dimension roles, resolve evidence, evaluate representation fitness, authorize review, or change any lifecycle, release, or publication state.

## Directory Rules basis

The packet uses existing responsibility roots: semantic meaning in `contracts/evidence/`, shape in `schemas/contracts/v1/evidence/`, synthetic replay in `fixtures/contracts/v1/evidence/`, repository validation in `tools/validators/evidence/`, conformance evidence in `tests/validators/evidence/`, orchestration in `.github/workflows/`, this reconciliation in `docs/intake/exploratory/`, and authoring accountability in `data/receipts/generated/`.

No claim registry, EvidenceBundle, layer manifest, source, policy rule, runtime consumer, lifecycle state, release record, or public surface is created.

## Non-effects and rollback

A local validator result is only declaration coherence. It is not evidence validity, scientific fitness, policy approval, review completion, release, publication, or public-answer authority. Rollback is a single additive commit revert with no external cleanup.
