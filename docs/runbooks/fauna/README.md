<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/fauna/readme
title: Fauna Runbooks · Lane Boundary and Navigation
type: readme
version: v1.1.0
status: draft; repository-grounded; documentation-only; all-substantive-children-repository-grounded; mixed-operational-maturity; sensitive-domain; non-authoritative; non-publisher; not-for-life-safety
owners:
  - "@bartytime4life — verified GitHub review route only"
owner_status: "Fauna, taxonomy, source, rights, stewardship, sensitivity/geoprivacy, evidence, policy, validation, review, release, correction, rollback, operations, and independent-review assignments remain NEEDS VERIFICATION; CODEOWNERS routing does not create those authorities."
created: 2026-08-24
updated: 2026-08-28
policy_label: public-review; fauna; runbook-index; sensitive-location; fail-closed; synthetic-proof-bounded; non-release; not-for-life-safety
current_path: docs/runbooks/fauna/README.md
owning_root: docs/
responsibility: Define the human-facing Fauna runbook boundary, disclose current child maturity, and route maintainers to the narrowest applicable procedure without granting taxonomy, source, rights, sensitivity, evidence, policy, review, lifecycle, release, deployment, rollback-execution, or publication authority.
truth_posture: cite-or-abstain
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 6e02ced04834c8f9f2210da8c655cdef626a3b08
  target_prior_blob: 5989e996d317cace6d63c0fc6b22c2cdf9f0c207
  rollback_runbook_prior_blob: d8d7d3bb9c40d3de50d484e6d13640bee5baaa58
  rollback_drill_blob: 78a0c3663ef30e5edb9260c0c5ab58d6e7f860fb
  rollback_card_contract_blob: c6d3c35c56b064e04c3a2532f4709d938d7b0c1a
  rollback_card_validator_blob: 9e9ed5a92851935b41a36698e4bead13ef4edf57
  generic_rehearsal_test_blob: b644ca6c4185b3f81bc339c077eae85299833261
  direct_markdown_children: 9
  substantive_repository_grounded_children_after_this_change: 9
  proposal_era_substantive_children_after_this_change: 0
related:
  - ../README.md
  - ../../domains/fauna/README.md
  - ../../domains/fauna/SENSITIVITY.md
  - ../../domains/fauna/POLICY.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, runbooks, fauna, taxonomy, occurrence, geoprivacy, rights, rollback, navigation, boundary, hold]
notes:
  - "Version 1.1 reconciles the child-maturity map after ROLLBACK_RUNBOOK.md was grounded in current shared rollback controls."
  - "ROLLBACK_RUNBOOK.md is the primary full Fauna rollback classification and review-handoff procedure; ROLLBACK_DRILL.md owns the bounded tabletop and shared synthetic rehearsal."
  - "Shared RollbackCard validation and generic synthetic mechanics are executable, but an integrated or operational Fauna rollback remains held."
  - "Document length, path presence, workflow success, pull-request state, and merge state are inventory evidence, not source admission, policy approval, rollback authority, release, deployment, or publication evidence."
  - "This README changes no contract, schema, policy, fixture, validator, workflow, source record, evidence object, lifecycle object, review record, release object, runtime, deployment, rollback execution, or publication state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Runbooks

> Human-facing navigation for testing, refreshing, resolving taxonomy, reviewing sensitive occurrences, evaluating rights-constrained derivatives, assessing promotion/publication readiness, rehearsing rollback, and preparing governed Fauna handoffs.

> [!IMPORTANT]
> A runbook, fixture, green workflow, review note, pull request, or merge is not source admission, taxonomic endorsement, an `EvidenceBundle`, rights clearance, sensitivity approval, policy approval, lifecycle promotion, rollback authorization, release, deployment, or publication.

> [!WARNING]
> Exact or reverse-engineerable wildlife locations fail closed. Nests, dens, roosts, hibernacula, spawning or breeding sites, aggregation sites, telemetry paths, observer-linked records, private-land joins, steward-controlled detail, and geoprivacy transform parameters must not appear in public fixtures, logs, issues, pull requests, screenshots, exports, maps, or generated answers.

> [!CAUTION]
> All nine substantive child documents are now repository-grounded, but operational maturity remains mixed. Shared `RollbackCard` candidate validation and marker-protected synthetic rollback mechanics exist; an integrated or operational Fauna rollback does not. Follow the terminal boundary in each procedure.

> [!NOTE]
> KFM is not an official wildlife, law-enforcement, hunting, veterinary, legal-status, regulatory, disease-response, emergency, or life-safety authority. Use the responsible issuing agency or steward for current determinations and operational instructions.

## Lane boundary

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the [Directory Rules](../../doctrine/directory-rules.md), which place human procedures under `docs/runbooks/`. Fauna remains a domain segment inside that responsibility root.

This directory owns human procedures. It does not own object meaning, machine shape, source admission, taxonomy authority, rights, sensitivity classification, evidence, policy, human review decisions, lifecycle transitions, release state, runtime behavior, rollback execution, or public carriers.

The lane preserves these distinctions:

- a taxonomic mapping is not an occurrence, status, range, abundance estimate, habitat claim, or release decision;
- an occurrence is not a range polygon, absence claim, population estimate, disease conclusion, mortality cause, or regulatory determination;
- public and restricted occurrence families remain distinct;
- exact or inferable sensitive detail requires governed withholding/generalization, traceable transform support, policy, review, and release closure before public use;
- source roles remain explicit across observation, checklist/event data, specimen/collection record, agency/legal record, model/derived surface, and context;
- agreement- or purpose-constrained sources remain governed by the exact terms applicable to the actual access;
- synthetic fixtures, schema-valid packets, workflows, maps, tiles, dashboards, indexes, and generated language remain subordinate to resolvable evidence and accepted policy.

## Choose the narrowest procedure

| Need | Procedure | Terminal boundary |
|---|---|---|
| Run deterministic checks without network access | [`NO_NETWORK_TEST_RUNBOOK.md`](NO_NETWORK_TEST_RUNBOOK.md) | Bounded synthetic validation and review handoff only |
| Refresh an already admitted source or product | [`SOURCE_REFRESH_RUNBOOK.md`](SOURCE_REFRESH_RUNBOOK.md) | Reviewable `RAW` or `QUARANTINE` handoff candidate; live refresh remains held |
| Preserve and classify an unresolved taxonomic mapping | [`TAXONOMY_RESOLUTION_RUNBOOK.md`](TAXONOMY_RESOLUTION_RUNBOOK.md) | Manual candidate and review handoff; executable resolution remains held |
| Review a potentially sensitive occurrence | [`SENSITIVE_OCCURRENCE_REVIEW.md`](SENSITIVE_OCCURRENCE_REVIEW.md) | Public-safe review handoff only; production clearance and release remain held |
| Assess an eBird Basic Dataset derivative | [`EBD_DERIVATIVE_RELEASE.md`](EBD_DERIVATIVE_RELEASE.md) | Agreement- and purpose-sensitive review handoff; derivative release remains held |
| Assess promotion readiness | [`PROMOTION_RUNBOOK.md`](PROMOTION_RUNBOOK.md) | Generic readiness result and human handoff; no Fauna transition or release |
| Rehearse publication denial | [`PUBLICATION_GATE_DRY_RUN.md`](PUBLICATION_GATE_DRY_RUN.md) | Shared synthetic denial result; candidate-specific Fauna gate remains held |
| Run a rollback tabletop and shared synthetic rehearsal | [`ROLLBACK_DRILL.md`](ROLLBACK_DRILL.md) | `DRILL_HANDOFF_READY`, `HOLD`, or `ERROR`; no public mutation |
| Classify a suspected release defect and prepare rollback/withdrawal review | [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md) | Review handoff only; operational rollback remains held |

If multiple procedures apply, keep their states separate. Validation does not resolve taxonomy or geoprivacy; taxonomy review does not admit a source; source refresh does not promote; sensitive-occurrence review does not create policy or release clearance; promotion readiness does not release; a dry run does not publish; a rollback drill does not mutate public state; and a rollback handoff does not authorize execution.

## Current child maturity

The labels below describe repository documents at the change base `main@6e02ced04834c8f9f2210da8c655cdef626a3b08` plus this documentation correction. They do not prove live sources, qualified actors, accepted policy, released artifacts, deployed consumers, or public carriers.

| Procedure | Current document maturity | Verified limit |
|---|---|---|
| [`EBD_DERIVATIVE_RELEASE.md`](EBD_DERIVATIVE_RELEASE.md) | Substantive repository-grounded draft | Agreement- and purpose-sensitive review procedure; no EBD bytes accessed and current derivative release remains `HOLD` |
| [`NO_NETWORK_TEST_RUNBOOK.md`](NO_NETWORK_TEST_RUNBOOK.md) | Substantive repository-grounded draft | Bounded fixture-hygiene and adjacent occurrence/tile checks; live sources, proof closure, and release held |
| [`PROMOTION_RUNBOOK.md`](PROMOTION_RUNBOOK.md) | Substantive repository-grounded draft | Generic A–G readiness validation and synthetic safety checks; Fauna candidate, active promotion policy, proof, decision, and release absent or held |
| [`PUBLICATION_GATE_DRY_RUN.md`](PUBLICATION_GATE_DRY_RUN.md) | Substantive repository-grounded draft | Shared synthetic publication-denial profile; no accepted candidate-specific Fauna dry-run contract or candidate |
| [`ROLLBACK_DRILL.md`](ROLLBACK_DRILL.md) | Substantive repository-grounded drill procedure | Shared candidate validation and marker-protected synthetic rehearsal plus Fauna tabletop; integrated and operational Fauna rollback held |
| [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md) | **Substantive repository-grounded primary procedure** | Classifies rollback/withdrawal/hold/error/forward correction, validates shared candidates, interprets synthetic mechanics, and prepares accountable handoff; no execution |
| [`SENSITIVE_OCCURRENCE_REVIEW.md`](SENSITIVE_OCCURRENCE_REVIEW.md) | Substantive repository-grounded draft | Bounded fail-closed review/handoff; production sensitivity policy, public/restricted conversion enforcement, accountable review, and public release held or unproved |
| [`SOURCE_REFRESH_RUNBOOK.md`](SOURCE_REFRESH_RUNBOOK.md) | Substantive repository-grounded draft | Fixture-first source-edge procedure; admitted descriptors, source authority, live connectors, and live sensitivity enforcement insufficient for live refresh |
| [`TAXONOMY_RESOLUTION_RUNBOOK.md`](TAXONOMY_RESOLUTION_RUNBOOK.md) | Substantive repository-grounded draft | Manual fail-closed mapping and review handoff; no admitted version-pinned authority inputs or executable resolver established |

Length is not maturity. Read each document's current evidence, stop conditions, finite outcomes, and non-effects before running a command.

## Current rollback capability

| Capability | Current evidence | Bounded conclusion |
|---|---|---|
| Shared `RollbackCard` candidate profile | Contract, closed schema, fixtures, validator, and tests | Candidate shape/local consistency only |
| Shared synthetic mechanics | Marker-protected helper and eight generic tests | Synthetic rollback/withdrawal mechanics only |
| Hosted rollback workflow | Shared fixture checks plus generic and Hazards tests | Not a Fauna integrated proof |
| Fauna rollback tabletop | `ROLLBACK_DRILL.md` | Public-safe handoff only |
| Fauna direct fixtures/tests | Test-lane README/scaffold | Integrated proof absent |
| Operational executor, alias mutation, invalidation, and read-back | Not established | `HOLD` |
| Accountable Fauna rollback authority | Roles unverified | `HOLD` |

The shared release `RollbackCard` profile is the current executable candidate surface. The permissive Fauna-specific schema stub is not operational proof.

## Authority and handoff rules

1. Pin the repository revision and identify the exact object, taxon assertion, source/product, time scope, generalized geography, intended consumer, and requested terminal boundary.
2. Read the selected child's status, evidence boundary, preconditions, stop conditions, outcomes, and terminal boundary.
3. Resolve contracts, schemas, source admission, rights, sensitivity, evidence, policy, review, release, correction, and rollback from their owning roots.
4. Keep exact or reconstructable sensitive detail out of public channels and review packets. Style-only hiding is not a geoprivacy transform.
5. Use verified actors and environments. `@bartytime4life` is a verified GitHub route; accountable functional assignments remain to be verified.
6. Preserve each producer's finite vocabulary. Runtime `DENY` or `ABSTAIN` is not a `RollbackCard` disposition.
7. Keep review, merge, source activation, lifecycle transition, rollback authorization, execution, release, deployment, promotion, and publication as separate events.

Stop and produce a public-safe handoff when required authority, source identity, approved purpose, rights, taxonomy snapshot, evidence, policy, sensitivity transform, review, correction support, rollback target, consumer binding, invalidation, executor, or read-back is missing; when source roles or object families would collapse; when sensitive precision could leak; or when a named path or command differs from the pinned repository.

## Open verification

| Item | Current posture | Smallest truthful next step |
|---|---|---|
| Integrated Fauna rollback proof | `TABLETOP AVAILABLE / INTEGRATED PROOF ABSENT` | Add one public-safe synthetic affected/target pair, direct positive/negative tests, current sensitivity/taxonomy checks, and downstream invalidation assertions |
| Operational rollback | `HOLD` | Require accepted target/alias, executor, policy/review, invalidation adapters, receipt, monitoring, and independent public read-back |
| Sensitive occurrence production controls | `RUNBOOK GROUNDED / POLICY-RELEASE HOLD` | Implement and review executable sensitivity policy, public/restricted conversion enforcement, accountable review, and release closure |
| Accountable roles | `NEEDS VERIFICATION` | Record verified scope, authority, separation, and revocation for every required role |
| Live Fauna operations | `HOLD / UNKNOWN` | Require admitted sources, executable connectors, rights/sensitivity closure, version-pinned taxonomy, evidence, policy, review, release topology, correction, rollback, monitoring, and runtime evidence |
| Parent runbook index | `NEEDS VERIFICATION` | Recompute only when a bounded parent-index task owns the full runbook inventory |

## Related surfaces

- [Parent runbook index](../README.md)
- [Fauna domain boundary](../../domains/fauna/README.md)
- [Fauna sensitivity doctrine](../../domains/fauna/SENSITIVITY.md)
- [Fauna policy documentation](../../domains/fauna/POLICY.md)
- [Directory Rules](../../doctrine/directory-rules.md)
- [Accepted placement decision](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Shared rollback rehearsal](../rollback-rehearsal.md)
- [`RollbackCard` contract](../../../contracts/release/rollback_card.md)
- [Fauna rollback decision lane](../../../release/rollback/fauna/README.md)
- [Fauna data-plane rollback lane](../../../data/rollback/fauna/README.md)

## Maintenance and document rollback

Update this README when a child is added, removed, renamed, materially re-scoped, or changes maturity; when Fauna taxonomy, source role, rights, sensitivity, geoprivacy, evidence, policy, release, correction, or rollback boundaries change; or when accountable authority, executable validation, live-source, runtime, deployment, rollback, or publication evidence changes.

If this documentation change is abandoned before merge, close the draft and remove only its task-owned branch. After an authorized merge, revert the documentation commits or submit a smaller reviewed forward correction. Documentation rollback does not change source, lifecycle, evidence, release, deployed, public, or wildlife-management state.

[Back to top](#top)
