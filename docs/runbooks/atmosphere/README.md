<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/atmosphere/readme
title: Atmosphere / Air Runbooks · Lane Boundary and Navigation
type: readme
version: v1.2
status: draft; repository-grounded; documentation-only; mixed-child-operational-maturity; non-authoritative; non-publisher; not-for-life-safety
owners:
  - "@bartytime4life — verified GitHub review route only"
owner_status: "Atmosphere, source, validation, evidence, policy, rights, sensitivity, Hazards-seam, review, promotion, release, correction, rollback, operations, and independent-review assignments remain NEEDS VERIFICATION; CODEOWNERS routing does not create those authorities."
created: 2026-08-24
updated: 2026-08-24
policy_label: public; atmosphere; runbook-index; mixed-maturity; non-release; not-for-life-safety
current_path: docs/runbooks/atmosphere/README.md
owning_root: docs/
responsibility: "Define the human-facing Atmosphere runbook lane boundary, disclose current child maturity, and route operators to the narrowest applicable procedure without granting source, evidence, policy, review, lifecycle, promotion, release, deployment, rollback-execution, or publication authority."
truth_posture: cite-or-abstain
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  initial_base_commit: df6c3f5dadd2800fdc2356ceb540ca4e448f6c7a
  first_reconciled_base_commit: 6e1bc94ea13fc0c7429fb824b62099ed1871598b
  current_base_commit: fdf513f9b450aef016ea47b599cf0b6d6e8db04d
  prior_blob: 89f76bcb650950c04be47109739d11908f545991
  release_rollback_runbook_blob: 24a61405e65bd2f24e4793c4566b2b6cd052dc1b
  child_count: 9
  substantive_repository_grounded_children: 9
  proposal_era_substantive_children: 0
  proposed_scaffold_children: 0
related:
  - ../README.md
  - ../../domains/atmosphere/README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, runbooks, atmosphere, air, navigation, boundary, mixed-maturity, promotion, hold]
notes:
  - "All nine child procedures are substantive repository-grounded drafts after reconciling the combined release/rollback coordination update and the promotion modernization."
  - "The combined release/rollback child is composition-only and does not supersede the separate release and rollback procedures or authorize execution."
  - "The promotion procedure reflects the bounded shared A-G readiness validator, empty Atmosphere candidate lane, empty source-authority projection, inactive policy sources, and operational promotion hold."
  - "Document maturity, a passing fixture, or a green workflow is not operational readiness, promotion, release, deployment, rollback execution, or publication evidence."
  - "This README changes no contract, schema, policy, fixture, validator, workflow, evidence object, lifecycle object, promotion decision, release object, runtime, deployment, rollback execution, or publication state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere / Air Runbooks

> Human-facing navigation for inspecting, validating, refreshing, containing, correcting, and preparing accountable review handoffs for the Atmosphere lane. These documents explain procedures; they do not create authority or operational state.

> [!IMPORTANT]
> A runbook, passing fixture, green workflow, review note, pull request, merge, readiness `PASS`, or `APPROVE_READY` result is not source admission, scientific endorsement, an `EvidenceBundle`, policy approval, lifecycle promotion, release authorization, deployment, rollback execution, or publication.

> [!WARNING]
> KFM is not an official AQI, medical, regulatory, emergency-alerting, or life-safety authority. Atmosphere may preserve observations, forecasts, smoke context, and official advisory context, but it must not originate health or emergency instructions. Route life-safety interpretation to the Hazards lane and the official issuing authority.

> [!CAUTION]
> All nine child procedures are now substantive repository-grounded drafts, but **operational maturity remains mixed and held**. [`PROMOTION_RUNBOOK.md`](PROMOTION_RUNBOOK.md) stops at bounded readiness or hold. [`RELEASE_ROLLBACK_RUNBOOK.md`](RELEASE_ROLLBACK_RUNBOOK.md) is composition-only: it binds release-readiness and rollback-assurance handoffs without superseding the separate procedures or authorizing operational action. Source admission, evidence closure, policy activation, accountable authority, transition application, release, deployment, public read-back, and operational rollback remain separate.

## Lane boundary

This directory owns human procedures for Atmosphere / Air work. It does not own machine meaning, admissibility, evidence, policy, review decisions, lifecycle transitions, promotion decisions, release state, runtime behavior, or public carriers. Those remain with their accepted doctrine and ADRs, contracts, schemas, policy, evidence, review, release, application, and pipeline surfaces.

The lane preserves these domain boundaries:

- observations, modeled fields, forecasts, climate products, smoke context, and advisory context keep distinct source roles;
- AQI is not a concentration, AOD is not PM2.5, and modeled values are not observations;
- low-cost sensor output requires the applicable correction, caveat, confidence, and limitation controls before any public-use claim;
- Atmosphere context does not replace Hazards authority or an official issuer;
- time, freshness, source role, knowledge character, units, averaging window, and official-authority posture remain visible; and
- generated language remains subordinate to resolvable evidence and accepted policy.

Missing authority or support fails closed with the outcome owned by the selected procedure. Do not infer permission from a public URL, a tracked path, a plausible filename, document length, a validator pass, or the absence of an explicit denial.

## Choose the narrowest procedure

| Need | Procedure | Terminal boundary |
|---|---|---|
| Run deterministic checks without network access | [`NO_NETWORK_TEST_RUNBOOK.md`](NO_NETWORK_TEST_RUNBOOK.md) | Bounded synthetic result and review handoff only |
| Validate an Atmosphere object or profile | [`VALIDATION_RUNBOOK.md`](VALIDATION_RUNBOOK.md) | Bounded validation result; broader validation remains held |
| Refresh an already-admitted source | [`SOURCE_REFRESH_RUNBOOK.md`](SOURCE_REFRESH_RUNBOOK.md) | Reviewable candidate only; live source execution remains held |
| Assess or contain aged state | [`STALE_STATE_RUNBOOK.md`](STALE_STATE_RUNBOOK.md) | Assessment and handoff; live propagation remains held |
| Correct already released material | [`CORRECTION_RUNBOOK.md`](CORRECTION_RUNBOOK.md) | Correction preparation and review; no release mutation |
| Assess final promotion readiness | [`PROMOTION_RUNBOOK.md`](PROMOTION_RUNBOOK.md) | Bounded A–G readiness or hold packet; no transition, release, or public write |
| Assess release readiness | [`RELEASE_RUNBOOK.md`](RELEASE_RUNBOOK.md) | Fixture-first, no-public-write review handoff |
| Prepare or rehearse rollback | [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md) | Candidate and synthetic rehearsal; operational rollback remains held |
| Coordinate release readiness with rollback assurance | [`RELEASE_ROLLBACK_RUNBOOK.md`](RELEASE_ROLLBACK_RUNBOOK.md) | Joint review handoff only; operational release, correction, withdrawal, and rollback remain held |

If more than one procedure applies, preserve the state boundaries between them. Validation does not promote; promotion readiness does not create a `PromotionDecision` or apply a transition; release readiness does not deploy or publish; correction planning does not mutate a prior release; and synthetic rollback rehearsal does not alter public state. The combined procedure coordinates those boundaries; it does not collapse them.

## Current child maturity

The labels below describe the repository documents at current `main@fdf513f9b450aef016ea47b599cf0b6d6e8db04d` plus the same-branch promotion modernization. They do not prove that a live source, accountable actor, accepted policy, deployed consumer, released artifact, or public carrier exists.

| Procedure | Current document maturity | Verified limit |
|---|---|---|
| [`CORRECTION_RUNBOOK.md`](CORRECTION_RUNBOOK.md) | Substantive repository-grounded draft | Generic bounded checks exist; Atmosphere-specific schema, policy, worker, review, and release-lane closure remain incomplete or conflicted |
| [`NO_NETWORK_TEST_RUNBOOK.md`](NO_NETWORK_TEST_RUNBOOK.md) | Substantive repository-grounded draft | Bounded synthetic profiles are executable; live sources and broader proof remain held |
| [`PROMOTION_RUNBOOK.md`](PROMOTION_RUNBOOK.md) | Substantive repository-grounded draft | Shared deterministic A–G readiness validator is present; no active Atmosphere candidate, admitted source authority, accepted proof packet, active policy, accountable review, applied transition, manifest, or released carrier was established |
| [`RELEASE_ROLLBACK_RUNBOOK.md`](RELEASE_ROLLBACK_RUNBOOK.md) | Substantive repository-grounded coordination draft | Composes release readiness, first-release withdrawal/hold assurance, successor rollback assurance, synthetic checks, incident routing, and joint handoff; no operational release or rollback effect |
| [`RELEASE_RUNBOOK.md`](RELEASE_RUNBOOK.md) | Substantive repository-grounded draft | Fixture-first readiness checks and handoff only; operational release remains held |
| [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md) | Substantive repository-grounded draft | Bounded `RollbackCard` validation and marker-protected synthetic rehearsal; operational rollback remains held |
| [`SOURCE_REFRESH_RUNBOOK.md`](SOURCE_REFRESH_RUNBOOK.md) | Substantive repository-grounded draft | No-network procedure and graduation sequence; live source refresh remains held |
| [`STALE_STATE_RUNBOOK.md`](STALE_STATE_RUNBOOK.md) | Substantive repository-grounded draft | Shared fixture-only assessment; Atmosphere policy and live propagation remain held |
| [`VALIDATION_RUNBOOK.md`](VALIDATION_RUNBOOK.md) | Substantive repository-grounded draft | Multiple bounded synthetic profiles; no accepted aggregate or release-grade producer |

## Promotion-readiness boundary

The current shared promotion validator is a bounded, deterministic, no-network, read-only check for a declared:

```text
CATALOG or TRIPLET -> PUBLISHED
```

packet. Its finite outcomes are `PASS`, `ABSTAIN`, `DENY`, and `ERROR`. `PASS` means `APPROVE_READY` for accountable review only.

The current repository does **not** establish an operational Atmosphere promotion path because:

- no child Atmosphere candidate dossier is verified;
- the central source-authority register is an empty projection;
- Atmosphere and promotion policy sources are inactive;
- no accepted Atmosphere proof packet or resolver binding is established;
- accountable reviewer and promotion authority remain unverified;
- no Atmosphere `PromotionDecision`, applied transition, operational receipt, or ReleaseManifest is established; and
- deployed public carriers, aliases, caches, monitoring, and public read-back remain unknown.

Use [`PROMOTION_RUNBOOK.md`](PROMOTION_RUNBOOK.md) to produce a finite readiness or hold packet, then stop at its authority boundary.

## Authority and handoff rules

1. Pin the repository revision and identify the exact object, source role, knowledge character, time scope, audience, and intended consumer.
2. Read the selected child's status, evidence boundary, preconditions, stop conditions, and terminal boundary before running a command.
3. Resolve contracts, schemas, policy, evidence, review, promotion, release, correction, and rollback objects from their owning roots; this README and its children do not replace them.
4. Use only verified actors and environments. `@bartytime4life` is the verified GitHub route; the accountable domain, scientific, source-rights, sensitivity, Hazards-seam, evidence, policy, review, promotion, release, rollback, operations, and independent-review assignments remain to be verified where required.
5. Record finite outcomes and unresolved holds without upgrading them through prose. A `PASS` means only what the producing profile declares.
6. Keep validation, review, decision, transition application, release, merge, deployment, promotion, rollback execution, publication, and public read-back as separate events with separate evidence.
7. For a first Atmosphere release, use withdrawal or hold assurance when no distinct prior release exists; never invent a rollback target.
8. For a successor release, independently revalidate a prior target before treating it as safer than the affected release.

Stop and create a public-safe handoff when required authority, source identity, rights, sensitivity, evidence, policy, time semantics, correction support, rollback target, or consumer binding is missing; when an observation/model/forecast/advisory role would collapse; when life-safety language would be originated; or when a named path or command does not match the pinned repository.

## Open verification

| Item | Current posture | Smallest truthful next step |
|---|---|---|
| Operational promotion | `HOLD` | Establish one real candidate plus admitted source authority, evidence/proof closure, accepted policy, accountable review, correction, rollback, transition execution, release topology, and public read-back before any promotion claim |
| Combined release/rollback procedure | `SUBSTANTIVE COORDINATION / OPERATIONAL HOLD` | Graduate only after a real immutable Atmosphere candidate, accepted release and rollback profiles, EvidenceBundle and policy closure, authenticated authorities, safe executors, invalidation, and public read-back are verified |
| First Atmosphere release recovery | `HOLD / NO PRIOR RELEASE VERIFIED` | Define an accepted withdrawal and fail-closed public posture; do not invent a predecessor |
| Accountable roles | `NEEDS VERIFICATION` | Record verified scope, authority, separation, effective interval, obligations, and revocation for each required role |
| Live Atmosphere operations | `HOLD / UNKNOWN` | Require admitted sources, executable connectors, evidence and policy closure, review, release topology, correction, rollback, monitoring, and current runtime evidence |
| A–G vocabulary convergence | `CONFLICTED / proposed` | Reconcile lifecycle-wide and final-readiness profiles through the governing ADR process without treating the current validator names as silently accepted doctrine |
| Air/Atmosphere namespace | `CONFLICTED` | Resolve through accepted ADR or migration evidence and close consumers before moving authority |

## Related surfaces

- Parent runbook index: [`docs/runbooks/README.md`](../README.md)
- Atmosphere domain boundary: [`docs/domains/atmosphere/README.md`](../../domains/atmosphere/README.md)
- Directory Rules: [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md)
- Accepted placement decision: [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- Proposed promotion sequence: [`ADR-0018`](../../adr/ADR-0018-promotion-gate-sequence.md)
- Promotion policy boundary: [`policy/promotion/README.md`](../../../policy/promotion/README.md)
- Atmosphere policy boundary: [`policy/domains/atmosphere/README.md`](../../../policy/domains/atmosphere/README.md)
- Candidate lane: [`release/candidates/atmosphere/README.md`](../../../release/candidates/atmosphere/README.md)
- Promotion-gate validator: [`tools/validators/promotion_gate/README.md`](../../../tools/validators/promotion_gate/README.md)

## Maintenance and document rollback

Update this README when a child is added, removed, renamed, materially re-scoped, or changes maturity; when the Atmosphere/Hazards seam changes; or when accountable authority, executable validation, source admission, evidence, policy, promotion, release, rollback, deployment, publication, or public read-back evidence changes.

This is a documentation-only change. Before merge, close or abandon its draft pull request. After merge, revert the documentation commit or submit a smaller reviewed forward fix. Blob `89f76bcb650950c04be47109739d11908f545991` restores the current-main pre-promotion lane index, but reverting this index would not change any operational or public state.

[Back to top](#top)
