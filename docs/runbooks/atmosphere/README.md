<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/atmosphere/readme
title: Atmosphere / Air Runbooks · Lane Boundary and Navigation
type: readme
version: v1.0
status: draft; repository-grounded; documentation-only; mixed-child-maturity; non-authoritative; non-publisher; not-for-life-safety
owners:
  - "@bartytime4life — verified GitHub review route only"
owner_status: "Atmosphere, source, validation, evidence, policy, rights, sensitivity, Hazards-seam, review, release, correction, rollback, operations, and independent-review assignments remain NEEDS VERIFICATION; CODEOWNERS routing does not create those authorities."
created: 2026-08-24
updated: 2026-08-24
policy_label: public; atmosphere; runbook-index; mixed-maturity; non-release; not-for-life-safety
current_path: docs/runbooks/atmosphere/README.md
owning_root: docs/
responsibility: "Define the human-facing Atmosphere runbook lane boundary, disclose current child maturity, and route operators to the narrowest applicable procedure without granting source, evidence, policy, review, lifecycle, release, deployment, promotion, rollback-execution, or publication authority."
truth_posture: cite-or-abstain
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 67e1e2c698dff941b689dba35cfc968ac573a5af
  prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
  child_count: 9
  substantive_repository_grounded_children: 7
  proposal_era_substantive_children: 1
  proposed_scaffold_children: 1
related:
  - ../README.md
  - ../../domains/atmosphere/README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, runbooks, atmosphere, air, navigation, boundary, mixed-maturity, hold]
notes:
  - "Replaces the prior one-byte placeholder with a lane boundary and navigation contract only."
  - "Seven child procedures are substantive repository-grounded drafts; the promotion runbook is substantive but proposal-era; the combined release/rollback surface remains a proposed scaffold."
  - "Document length is inventory evidence, not operational readiness evidence."
  - "This README changes no contract, schema, policy, fixture, validator, workflow, evidence object, lifecycle object, release object, runtime, deployment, promotion, rollback execution, or publication state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere / Air Runbooks

> Human-facing navigation for inspecting, validating, refreshing, containing, correcting, and preparing review handoffs for the Atmosphere lane. These documents explain procedures; they do not create authority or operational state.

> [!IMPORTANT]
> A runbook, passing fixture, green workflow, review note, pull request, or merge is not source admission, scientific endorsement, an `EvidenceBundle`, policy approval, lifecycle promotion, release authorization, deployment, rollback execution, or publication.

> [!WARNING]
> KFM is not an official AQI, medical, regulatory, emergency-alerting, or life-safety authority. Atmosphere may preserve observations, forecasts, smoke context, and official advisory context, but it must not originate health or emergency instructions. Route life-safety interpretation to the Hazards lane and the official issuing authority.

> [!CAUTION]
> Child maturity is mixed. Use the maturity table below before following a procedure. In particular, [`PROMOTION_RUNBOOK.md`](PROMOTION_RUNBOOK.md) remains proposal-era and [`RELEASE_ROLLBACK_RUNBOOK.md`](RELEASE_ROLLBACK_RUNBOOK.md) remains only a proposed scaffold.

## Lane boundary

This directory owns human procedures for Atmosphere / Air work. It does not own machine meaning, admissibility, evidence, policy, review decisions, lifecycle transitions, release state, runtime behavior, or public carriers. Those remain with their accepted doctrine and ADRs, contracts, schemas, policy, evidence, review, release, application, and pipeline surfaces.

The lane preserves these domain boundaries:

- observations, modeled fields, forecasts, climate products, smoke context, and advisory context keep distinct source roles;
- AQI is not a concentration, AOD is not PM2.5, and modeled values are not observations;
- low-cost sensor output requires the applicable correction, caveat, confidence, and limitation controls before any public-use claim;
- Atmosphere context does not replace Hazards authority or an official issuer;
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
| Assess promotion readiness | [`PROMOTION_RUNBOOK.md`](PROMOTION_RUNBOOK.md) | Proposal-era guidance only; verify every implementation claim |
| Assess release readiness | [`RELEASE_RUNBOOK.md`](RELEASE_RUNBOOK.md) | Fixture-first, no-public-write review handoff |
| Prepare or rehearse rollback | [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md) | Candidate and synthetic rehearsal; operational rollback remains held |
| Follow the planned combined release/rollback surface | [`RELEASE_ROLLBACK_RUNBOOK.md`](RELEASE_ROLLBACK_RUNBOOK.md) | Partial scaffold only; use the separate release and rollback procedures instead |

If more than one procedure applies, preserve the state boundaries between them. Validation does not promote; promotion readiness does not release; release readiness does not deploy or publish; correction planning does not mutate a prior release; and synthetic rollback rehearsal does not alter public state.

## Current child maturity

The labels below describe the repository documents at `main@67e1e2c698dff941b689dba35cfc968ac573a5af`. They do not prove that a live source, accountable actor, accepted policy, deployed consumer, released artifact, or public carrier exists.

| Procedure | Current document maturity | Verified limit |
|---|---|---|
| [`CORRECTION_RUNBOOK.md`](CORRECTION_RUNBOOK.md) | Substantive repository-grounded draft | Generic bounded checks exist; Atmosphere-specific schema, policy, worker, review, and release-lane closure remain incomplete or conflicted |
| [`NO_NETWORK_TEST_RUNBOOK.md`](NO_NETWORK_TEST_RUNBOOK.md) | Substantive repository-grounded draft | Bounded synthetic profiles are executable; live sources and broader proof remain held |
| [`PROMOTION_RUNBOOK.md`](PROMOTION_RUNBOOK.md) | Substantive proposal-era draft | Doctrine-oriented guidance; owners, paths, commands, CI bindings, and implementation claims require current verification |
| [`RELEASE_ROLLBACK_RUNBOOK.md`](RELEASE_ROLLBACK_RUNBOOK.md) | **Partial — 785-byte proposed scaffold** | Navigation lineage only; not a usable release or rollback procedure |
| [`RELEASE_RUNBOOK.md`](RELEASE_RUNBOOK.md) | Substantive repository-grounded draft | Fixture-first readiness checks and handoff only; operational release remains held |
| [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md) | Substantive repository-grounded draft | Bounded `RollbackCard` validation and marker-protected synthetic rehearsal; operational rollback remains held |
| [`SOURCE_REFRESH_RUNBOOK.md`](SOURCE_REFRESH_RUNBOOK.md) | Substantive repository-grounded draft | No-network procedure and graduation sequence; live source refresh remains held |
| [`STALE_STATE_RUNBOOK.md`](STALE_STATE_RUNBOOK.md) | Substantive repository-grounded draft | Shared fixture-only assessment; Atmosphere policy and live propagation remain held |
| [`VALIDATION_RUNBOOK.md`](VALIDATION_RUNBOOK.md) | Substantive repository-grounded draft | Multiple bounded synthetic profiles; no accepted aggregate or release-grade producer |

## Authority and handoff rules

1. Pin the repository revision and identify the exact object, source role, time scope, and intended consumer.
2. Read the selected child's status, evidence boundary, preconditions, stop conditions, and terminal boundary before running a command.
3. Resolve contracts, schemas, policy, evidence, review, release, correction, and rollback objects from their owning roots; this README and its children do not replace them.
4. Use only verified actors and environments. `@bartytime4life` is the verified GitHub route; the accountable domain, scientific, source-rights, sensitivity, Hazards-seam, policy, review, release, rollback, operations, and independent-review assignments remain to be verified where required.
5. Record finite outcomes and unresolved holds without upgrading them through prose. A `PASS` means only what the producing profile declares.
6. Keep review, merge, release, deployment, promotion, rollback execution, and publication as separate events with separate evidence.

Stop and create a public-safe handoff when required authority, source identity, rights, sensitivity, evidence, policy, time semantics, correction support, rollback target, or consumer binding is missing; when an observation/model/forecast/advisory role would collapse; when life-safety language would be originated; or when a named path or command does not match the pinned repository.

## Open verification

| Item | Current posture | Smallest truthful next step |
|---|---|---|
| Promotion procedure | `PARTIAL / NEEDS VERIFICATION` | Reconcile the proposal-era document against current paths, controls, fixtures, workflows, owners, and holds |
| Combined release/rollback procedure | `PARTIAL / PROPOSED SCAFFOLD` | Either replace it through domain review or explicitly retire it in favor of the separate release and rollback procedures; do not infer the decision here |
| Accountable roles | `NEEDS VERIFICATION` | Record verified scope, authority, separation, and revocation for each required role |
| Live Atmosphere operations | `HOLD / UNKNOWN` | Require admitted sources, executable connectors, evidence and policy closure, review, release topology, correction, rollback, monitoring, and current runtime evidence |

## Related surfaces

- Parent runbook index: [`docs/runbooks/README.md`](../README.md)
- Atmosphere domain boundary: [`docs/domains/atmosphere/README.md`](../../domains/atmosphere/README.md)
- Directory Rules: [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md)
- Accepted placement decision: [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)

## Maintenance and document rollback

Update this README when a child is added, removed, renamed, materially re-scoped, or changes maturity; when the Atmosphere/Hazards seam changes; or when accountable authority, executable validation, live-source, policy, release, rollback, deployment, or publication evidence changes.

This is a documentation-only change. Before merge, close or abandon its draft pull request. After merge, revert the documentation commit or submit a smaller reviewed forward fix. Blob `8b137891791fe96927ad78e64b0aad7bded08bdc` restores the prior one-byte file, but reverting this README would not change any operational or public state.

[Back to top](#top)
