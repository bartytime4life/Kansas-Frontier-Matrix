<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-connector-load-budget-assessment
title: Pass 18 Connector Load-Budget Assessment Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD — Intake steward · Source steward · Connector steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; source-lineage; connector; load-budget; no-authority
responsibility: Preserve source lineage and repository reconciliation for a bounded connector load-budget assessment without promoting proposal material into source, activation, scheduling, lifecycle, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card transcription and inspected-repository comparison; PROPOSED bounded adaptation; UNKNOWN consumers and live source budgets; NEEDS VERIFICATION steward review and hosted exact-head CI"
related:
  - ../../../contracts/source/connector_load_budget_assessment.md
  - ../../../contracts/source/web_acquisition_conduct_assessment.md
  - ../../standards/connector-rate-limits.md
  - ../../../docs/doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Connector Load-Budget Assessment Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, physical page 62 / printed page 59 | `KFM-P18-INV-217` proposes recording rate-limit posture, concurrency/threading budgets, politeness constraints, and provider terms before threaded or distributed fetching. | `CONFIRMED` |
| Same dossier, physical page 76 / printed page 73 | `KFM-P18-INV-422` requires source load budgets, concurrency limits, and stop conditions before distributed or threaded activation. Cards `KFM-P18-INV-372` and `KFM-P18-INV-447` reinforce concurrency as stewardship rather than throughput tuning. | `CONFIRMED` |
| Google Drive `Kansas Frontier Matrix — Connected-Dots Architecture Brief` and `KFM Unified Doctrine Synthesis`, inspected 2026-08-11 | Corroborate depth-first proof slices, watcher non-publication, finite outcomes, and no-network fixture posture. | `PROPOSAL LINEAGE` |
| `main@074a39c4acb8e4e72cafe4bdea4c9e237dbf2496` | `docs/standards/connector-rate-limits.md` names the gap; `WebAcquisitionConductAssessmentCandidate` checks route/terms/robots/basic rate posture; connectors-core has injected retry mechanics. Exact searches found no source-wide budget contract, schema, fixture family, validator, workflow, branch, or pull request. | `CONFIRMED` for the inspected snapshot |

The supplied and Drive materials are design evidence, not source terms, legal advice, activation instructions, or proof of repository runtime behavior.

## Reconciliation and selected increment

The existing web-conduct profile already owns terms, robots, route, identity, proxy, distribution review, and a basic concurrency/delay declaration. The connectors-core package already owns reusable injected transport and retry mechanics. This change does not duplicate either surface.

The remaining gap is the relationship between a proposed execution and one shared source-wide budget: per-worker budgets must not multiply under threading or distribution, requested concurrency must fit the declared ceiling, distributed workers must share a coordination key, and retry/stop controls must remain fail-closed.

## Source-to-profile mapping

| Source pressure | Bounded adaptation | Held boundary |
|---|---|---|
| Record a rate and concurrency budget. | Closed pace, capacity, retry, and stop declarations. | No policy dereference or live quota discovery. |
| Treat concurrency as source stewardship. | Only `PER_SOURCE` scope can pass; `PER_WORKER` denies. | No ethical or legal conclusion beyond local declaration coherence. |
| Coordinate distributed acquisition. | Distributed mode requires one shared coordination key. | No scheduler, lock service, queue, or worker is created. |
| Obey throttling and stop safely. | `Retry-After` compliance and four minimum stop conditions are mandatory. | No request, sleep, retry, or throttle observation occurs. |
| Preserve existing conduct authority. | Opaque reference and declared outcome for the existing conduct assessment. | The referenced record is not resolved or authenticated. |

## Directory Rules path decision

```yaml
path_decision:
  artifact: ConnectorLoadBudgetAssessmentCandidate packet
  proposed_path: contracts/source/connector_load_budget_assessment.md
  artifact_kind: semantic contract plus dependency-closed validation packet
  authority_owner: source acquisition contract stewardship
  lifecycle_stage: not_applicable
  execution_role: none
  scope_kind: object_family
  scope_id: connector-load-budget-assessment
  exposure: internal
  mutability: versioned
  evidence:
    - docs/doctrine/directory-rules.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - contracts/source/web_acquisition_conduct_assessment.md
  rules: [DIR-SIGNATURE-001, DIR-PLACE-003, DIR-PLACE-004]
  outcome: PLACE
```

Meaning, shape, synthetic cases, executable validation, tests, CI orchestration, exploratory source reconciliation, and generated accountability remain in their separate established roots. No new root or parallel authority is created.

## Validation and rollback

Focused validation covers three execution modes, unresolved abstention, source-policy hold, denied conduct, per-worker scope, demand above budget and worker count, missing/unexpected distributed keys, retry bounds, `Retry-After`, stop conditions, review references, canonical arrays, content identity, hostile JSON, no-network replay, and schema closure.

Rollback is a focused revert of this additive packet. No live source, connector, schedule, registry, payload, lifecycle state, evidence, policy, review, release, deployment, or public artifact is changed.
