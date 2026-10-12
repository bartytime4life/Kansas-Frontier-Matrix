<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-18-participatory-planning-weight-receipt-source-map
title: Pass 18 Participatory Planning Weight Receipt Source Map
type: source-map
version: v1.0.0
status: exploratory; implementation-mapped; non-authoritative
owners: OWNER_TBD — Intake steward · Evidence steward · Planning-analysis steward · Participation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; exploratory; source-reconciliation; planning; participation
responsibility: Reconcile supplied participatory-planning weight and facilitation ideas with current repository evidence while preserving privacy, evidence, policy, review, planning-decision, release, and publication boundaries.
truth_posture: "CONFIRMED supplied-card and bounded repository gap; PROPOSED inactive implementation profile; UNKNOWN consumer adoption; NEEDS VERIFICATION human review and hosted CI"
related:
  - ../../../contracts/evidence/participatory_planning_weight_receipt.md
  - ../../../contracts/evidence/planning_proxy_uncertainty_assessment.md
  - ../../../contracts/governance/public_participation_submission_assessment.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Participatory Planning Weight Receipt Source Map

## Source and gap

| Evidence | Observation | Status |
|---|---|---|
| Supplied Pass 18 card KFM-P18-INV-060 | Stakeholder preference weights, target populations, and criteria should remain auditable and must not masquerade as neutral GIS output. | CONFIRMED source statement |
| Supplied Pass 18 card KFM-P18-INV-203 | Participatory site-suitability work should preserve criteria, rankings, stakeholder-group weights, and sensitivity settings before any public claim. | CONFIRMED source statement |
| Supplied Pass 18 card KFM-P18-INV-421 | Participatory evidence should record facilitation method, participant role, deliberation context, dissent, and uncertainty while protecting participant detail. | CONFIRMED source statement |
| Connected Drive KFM Full Atlas seed cards | The participatory-planning implementation surface calls for stakeholder-input receipts, scenario/indicator declarations, equity and sensitivity checks, and bounded decision-support validation. | CONFIRMED thematic corroboration |
| Current repository participation and planning families | PublicParticipationSubmissionAssessment owns submission intake; PlanningScenarioManifest owns scenario declaration; PlanningProxyUncertaintyAssessment owns proxy limits. None owns separate stakeholder-group weight normalization, dissent, and facilitation coherence. | CONFIRMED adjacent responsibilities |
| Current main and PR search | No exact participatory planning weight receipt contract, schema, fixture family, validator, workflow, source map, or matching pull request was found before authoring. | CONFIRMED bounded gap |

## Adaptation

The implementation is a closed synthetic candidate under the existing evidence family. It records bounded planning scope, criteria references, separate group weight sets in integer basis points, consent and facilitation references, dissent, unresolved conflicts, sensitivity-analysis posture, privacy exclusions, governance state, and fixed-false authority claims.

The profile does not collect identities or raw notes, infer or aggregate preferences, calculate scores, rank sites or routes, determine consensus, evaluate policy, approve review, authorize a planning decision, resolve evidence, promote, release, deploy, or publish.

## Directory Rules basis

The accepted responsibility-root model places semantic meaning in contracts/evidence/, machine shape in schemas/contracts/v1/evidence/, synthetic replay in fixtures/contracts/v1/evidence/, executable validation in tools/validators/evidence/, conformance proof in tests/validators/evidence/, orchestration in .github/workflows/, reconciliation in docs/intake/exploratory/, and generated authoring provenance in data/receipts/generated/.

Evidence owns the packet because it preserves how stakeholder-derived planning weights were produced and bounded. No participant registry, criteria registry, planning source, EvidenceBundle, policy, review, release, publication, or public-product authority is created.

## Non-effects and rollback

A local validator result is only declaration coherence. It is not consent, evidence closure, stakeholder consensus, planning advice, policy approval, review completion, release, publication, or public-answer authority. Rollback is an additive commit revert with no external cleanup.
