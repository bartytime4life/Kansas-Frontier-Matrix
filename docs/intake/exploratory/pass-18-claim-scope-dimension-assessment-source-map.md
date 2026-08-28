<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-18-claim-scope-dimension-assessment-source-map
title: Pass 18 Claim Scope Dimension Assessment Source Map
type: source-map
version: v1.0.0
status: exploratory; implementation-mapped; non-authoritative
owners: OWNER_TBD — Intake steward · Evidence steward · Spatial-representation steward
created: 2026-08-10
updated: 2026-08-10
owning_root: docs/
policy_label: internal; exploratory; source-reconciliation; claim-scope; representation
responsibility: Reconcile one supplied time-space-attribute claim-scope idea with current repository evidence while withholding private discovery-source identifiers from public provenance.
truth_posture: "CONFIRMED supplied-card and repository gap; PROPOSED inactive implementation profile; UNKNOWN consumer adoption; NEEDS VERIFICATION human review and hosted CI"
related:
  - ../../../contracts/evidence/claim_scope_dimension_assessment.md
  - ../../../contracts/evidence/evidence_bundle.md
  - ../../../contracts/evidence/representation_fitness_assessment.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Claim Scope Dimension Assessment Source Map

## Source and gap

| Evidence | Observation | Status |
|---|---|---|
| Supplied Pass 18 card `KFM-P18-INV-376` | Spatial claims should disclose which of time, space, or attribute is measured and which dimensions are controlled so the representation frame is inspectable. | `CONFIRMED` source statement |
| `contracts/evidence/evidence_bundle.md` | Existing EvidenceBundle meaning establishes claim-scope closure but does not define a closed measured-versus-controlled dimension profile. | `CONFIRMED` adjacent contract |
| `contracts/evidence/representation_fitness_assessment.md` | Existing representation fitness assesses suitability for an intended use but does not record the time-space-attribute measurement frame. | `CONFIRMED` adjacent contract |
| Current `main@ef1ba46a19e4de7c176e9d093c1285e73a0af75a` search | No exact claim-scope dimension assessment contract, schema, fixture family, validator, workflow, branch, or PR was found before implementation. | `CONFIRMED` bounded gap |
| Connected private research corpus | Used only for candidate discovery and corroboration. Private filenames, IDs, URLs, hashes, and copied prose are intentionally excluded. | `CONFIRMED` provenance boundary |

## Adaptation

The implementation is a closed synthetic assessment candidate under the existing evidence family. It records one claim and EvidenceBundle reference, a complete/incomplete/unknown assessment state, exactly one measured dimension and two controlled dimensions when complete, an interpretation label derived from the measured dimension, and explicit fixed-false authority claims.

The profile stores no claim text, coordinates, timestamps, attribute values, or source payloads. It does not decide which KFM claim families must adopt the triad; adoption remains a later review and contract-evolution decision.

## Directory Rules basis

The packet uses existing responsibility roots: semantic meaning in `contracts/evidence/`, shape in `schemas/contracts/v1/evidence/`, synthetic replay in `fixtures/contracts/v1/evidence/`, repository validation in `tools/validators/evidence/`, conformance evidence in `tests/validators/evidence/`, orchestration in `.github/workflows/`, this reconciliation in `docs/intake/exploratory/`, and authoring accountability in `data/receipts/generated/`.

No claim registry, EvidenceBundle replacement, spatial or temporal authority, attribute registry, layer manifest mutation, policy rule, runtime adapter, lifecycle state, release record, or public surface is created.

## Non-effects and rollback

A local `PASS` authenticates no referenced object and grants no truth, evidence, representation, policy, review, release, publication, or public-use authority. Rollback is a single additive commit revert with no external cleanup.
