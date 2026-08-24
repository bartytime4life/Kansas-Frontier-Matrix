<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/fauna/readme
title: Fauna Runbooks · Lane Boundary and Navigation
type: readme
version: v1.0
status: draft; repository-grounded; documentation-only; mixed-child-maturity; sensitive-domain; non-authoritative; non-publisher; not-for-life-safety
owners:
  - "@bartytime4life — verified GitHub review route only"
owner_status: "Fauna, taxonomy, source, rights, stewardship, sensitivity/geoprivacy, evidence, policy, validation, review, release, correction, rollback, operations, and independent-review assignments remain NEEDS VERIFICATION; CODEOWNERS routing does not create those authorities."
created: 2026-08-24
updated: 2026-08-24
policy_label: public-review; fauna; runbook-index; mixed-maturity; sensitive-location; fail-closed; non-release; not-for-life-safety
current_path: docs/runbooks/fauna/README.md
owning_root: docs/
responsibility: "Define the human-facing Fauna runbook lane boundary, disclose current child maturity, and route operators to the narrowest applicable procedure without granting taxonomy, source, rights, sensitivity, evidence, policy, review, lifecycle, release, deployment, promotion, rollback-execution, or publication authority."
truth_posture: cite-or-abstain
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 6e1bc94ea13fc0c7429fb824b62099ed1871598b
  prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
  child_count: 9
  substantive_repository_grounded_children: 8
  proposal_era_substantive_children: 1
  sensitive_occurrence_review_blob: e783cb4f643b250a456162699fb9768aa8364241
  sensitive_occurrence_review_merge: 8fd0d46f948d5776ee3c4fe710f1cf21aed0d1ad
related:
  - ../README.md
  - ../../domains/fauna/README.md
  - ../../domains/fauna/SENSITIVITY.md
  - ../../domains/fauna/POLICY.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, runbooks, fauna, taxonomy, occurrence, geoprivacy, rights, navigation, boundary, mixed-maturity, hold]
notes:
  - "Replaces the prior one-byte placeholder with a lane boundary and navigation contract only."
  - "Eight child procedures are substantive repository-grounded drafts; the rollback runbook remains substantive but proposal-era."
  - "PR #3509 merged the sensitive-occurrence review before this branch settled; this revision reconciles the README to that current-main fact without treating the merge as policy or release authority."
  - "Document length, path presence, merge state, and workflow success are inventory evidence, not operational-readiness or publication evidence."
  - "This README changes no contract, schema, policy, fixture, validator, workflow, source record, evidence object, lifecycle object, review record, release object, runtime, deployment, promotion, rollback execution, or publication state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Runbooks

> Human-facing navigation for testing, refreshing, classifying, reviewing, rehearsing, and preparing governed handoffs for the Fauna lane. These documents explain procedures; they do not create authority or operational state.

> [!IMPORTANT]
> A runbook, passing fixture, green workflow, review note, pull request, or merge is not source admission, taxonomic endorsement, an `EvidenceBundle`, rights clearance, sensitivity approval, policy approval, lifecycle promotion, release authorization, deployment, rollback execution, or publication.

> [!WARNING]
> Exact or reverse-engineerable wildlife locations fail closed. Nests, dens, roosts, hibernacula, spawning or breeding sites, aggregation sites, telemetry paths, private-land joins, observer-linked records, steward-controlled detail, and geoprivacy transform parameters must not appear in public fixtures, logs, issues, pull requests, screenshots, exports, maps, or generated answers.

> [!CAUTION]
> Child maturity is mixed. Use the maturity table before following a procedure. In particular, [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md) remains proposal-era and links to a Fauna `VALIDATION_RUNBOOK.md` that is not present. [`SENSITIVE_OCCURRENCE_REVIEW.md`](SENSITIVE_OCCURRENCE_REVIEW.md) is now repository-grounded after merged PR #3509, but production Fauna sensitivity policy, public/restricted conversion enforcement, accountable review authority, and public release remain held or unverified.

> [!NOTE]
> KFM is not an official wildlife, law-enforcement, hunting, veterinary, legal-status, regulatory, disease-response, emergency, or life-safety authority. Use the responsible issuing agency or steward for current determinations and operational instructions.

## Lane boundary

Accepted Directory Rules place human operational procedures under `docs/runbooks/`; the Fauna domain remains a segment inside that responsibility root. This README is therefore a same-path documentation boundary, not a new schema, policy, source-registry, evidence, release, or public-serving authority.

This directory owns human procedures for Fauna work. It does not own object meaning, machine shape, admissibility, source rights, sensitivity classification, evidence, policy, human review decisions, lifecycle transitions, release state, runtime behavior, or public carriers. Those remain with their accepted doctrine and ADRs, contracts, schemas, registries, policy, evidence, review, release, application, and pipeline surfaces.

The lane preserves these domain boundaries:

- a taxonomic mapping is not an occurrence, legal status, conservation status, range, abundance estimate, or release decision;
- an occurrence is not a range polygon, absence claim, population estimate, habitat-suitability claim, disease conclusion, mortality cause, or regulatory determination;
- public and restricted occurrence families remain distinct;
- exact or inferable sensitive locations require governed withholding or generalization, traceable transform support, policy, review, and release closure before public use;
- source roles remain explicit across direct observation, checklist/event data, specimen or collection record, agency or regulatory record, model or derived surface, and contextual material;
- eBird Basic Dataset use remains governed by the exact access agreement, approved purpose, source conditions, privacy constraints, and derivative-review posture applicable to the actual access;
- synthetic fixtures, schema-valid packets, workflow results, maps, tiles, dashboards, indexes, and generated language remain subordinate to resolvable evidence and accepted policy.

Missing authority or support fails closed with the outcome owned by the selected procedure. Do not infer permission from a public URL, tracked path, plausible filename, long document, validator pass, merge, or absence of an explicit denial.

## Choose the narrowest procedure

| Need | Procedure | Terminal boundary |
|---|---|---|
| Run deterministic checks without network access | [`NO_NETWORK_TEST_RUNBOOK.md`](NO_NETWORK_TEST_RUNBOOK.md) | Bounded synthetic validation and review handoff only |
| Refresh an already admitted Fauna source or product | [`SOURCE_REFRESH_RUNBOOK.md`](SOURCE_REFRESH_RUNBOOK.md) | Reviewable `RAW` or `QUARANTINE` handoff candidate; live refresh remains held |
| Preserve and classify an unresolved taxonomic mapping | [`TAXONOMY_RESOLUTION_RUNBOOK.md`](TAXONOMY_RESOLUTION_RUNBOOK.md) | Manual candidate and review handoff; executable resolution remains held |
| Review a potentially sensitive occurrence | [`SENSITIVE_OCCURRENCE_REVIEW.md`](SENSITIVE_OCCURRENCE_REVIEW.md) | Public-safe review handoff only; production sensitivity clearance and public release remain held |
| Assess a proposed eBird Basic Dataset derivative | [`EBD_DERIVATIVE_RELEASE.md`](EBD_DERIVATIVE_RELEASE.md) | Rights-sensitive review handoff only; current derivative release remains held |
| Assess promotion readiness | [`PROMOTION_RUNBOOK.md`](PROMOTION_RUNBOOK.md) | Generic readiness result and human handoff; no Fauna transition or release |
| Rehearse publication denial and assess dry-run readiness | [`PUBLICATION_GATE_DRY_RUN.md`](PUBLICATION_GATE_DRY_RUN.md) | Shared synthetic denial result; candidate-specific Fauna gate remains held |
| Run a bounded rollback tabletop or synthetic rehearsal | [`ROLLBACK_DRILL.md`](ROLLBACK_DRILL.md) | Shared candidate/rehearsal evidence and Fauna review handoff only |
| Read the planned full published-release rollback procedure | [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md) | Proposal-era guidance only; verify every path, actor, command, and target before use |

If more than one procedure applies, preserve the state boundaries between them. No-network validation does not resolve taxonomy or geoprivacy; taxonomy review does not admit a source; source refresh does not normalize or promote; sensitive-occurrence review does not create sensitivity policy or release clearance; promotion readiness does not release; publication-gate rehearsal does not deploy or publish; and a rollback drill does not mutate public state.

## Current child maturity

The labels below describe repository documents at `main@6e1bc94ea13fc0c7429fb824b62099ed1871598b`. They do not prove that a live source, qualified actor, accepted policy, released artifact, deployed consumer, or public carrier exists.

| Procedure | Current document maturity | Verified limit |
|---|---|---|
| [`EBD_DERIVATIVE_RELEASE.md`](EBD_DERIVATIVE_RELEASE.md) | Substantive repository-grounded draft | Agreement- and purpose-sensitive review procedure; no EBD bytes were accessed and current EBD derivative release remains `HOLD` |
| [`NO_NETWORK_TEST_RUNBOOK.md`](NO_NETWORK_TEST_RUNBOOK.md) | Substantive repository-grounded draft | Bounded fixture-hygiene suite and adjacent occurrence/tile profiles are executable; live sources, proof closure, and release remain held |
| [`PROMOTION_RUNBOOK.md`](PROMOTION_RUNBOOK.md) | Substantive repository-grounded draft | Generic A–G readiness validation and synthetic Fauna safety checks exist; Fauna candidate, active promotion policy, proof, decision, and release remain absent or held |
| [`PUBLICATION_GATE_DRY_RUN.md`](PUBLICATION_GATE_DRY_RUN.md) | Substantive repository-grounded draft | Shared synthetic publication-denial profile is executable; no accepted candidate-specific Fauna dry-run contract or candidate is established |
| [`ROLLBACK_DRILL.md`](ROLLBACK_DRILL.md) | Substantive repository-grounded draft | Shared `RollbackCard` candidate validation and marker-protected synthetic rehearsal are executable; integrated and operational Fauna rollback remain held |
| [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md) | **Substantive proposal-era draft** | Placeholder owners, proposed paths, and a stale link to absent `VALIDATION_RUNBOOK.md`; not a verified operational rollback procedure |
| [`SENSITIVE_OCCURRENCE_REVIEW.md`](SENSITIVE_OCCURRENCE_REVIEW.md) | Substantive repository-grounded draft | Bounded fail-closed review/handoff procedure; current `OccurrenceEvidence` fixture-first validator can prove internal draft-profile consistency, but production sensitivity policy, public/restricted conversion enforcement, accountable review, and public release remain `HOLD` or unproved |
| [`SOURCE_REFRESH_RUNBOOK.md`](SOURCE_REFRESH_RUNBOOK.md) | Substantive repository-grounded draft | Fixture-first source-edge procedure; concrete admitted descriptors, source authority, active connectors, and live sensitivity-policy enforcement remain insufficient for live refresh |
| [`TAXONOMY_RESOLUTION_RUNBOOK.md`](TAXONOMY_RESOLUTION_RUNBOOK.md) | Substantive repository-grounded draft | Manual fail-closed mapping and review handoff; no admitted version-pinned authority inputs or executable resolver are established |

## Authority and handoff rules

1. Pin the repository revision and identify the exact object, taxon assertion, source or source product, time scope, sensitivity scope, intended consumer, and requested terminal boundary.
2. Read the selected child's status, evidence boundary, preconditions, stop conditions, outcomes, and terminal boundary before running a command.
3. Resolve contracts, schemas, source admission, rights, sensitivity, evidence, policy, review, release, correction, and rollback objects from their owning roots. This README and its children do not replace them.
4. Keep exact or reconstructable sensitive detail out of public channels and review packets. A display style that hides detail is not a geoprivacy transform or release control.
5. Use only verified actors and environments. `@bartytime4life` is the verified GitHub route; accountable Fauna, taxonomy, scientific, source-rights, stewardship, sensitivity, policy, review, release, rollback, operations, and independent-review assignments remain to be verified where required.
6. Preserve each producer's finite outcome vocabulary. A `PASS`, `READY`, or `REVIEW_HANDOFF_READY` means only what that exact profile declares.
7. Keep review, merge, source activation, lifecycle transition, release, deployment, promotion, rollback execution, and publication as separate events with separate evidence.

Stop and create a public-safe handoff when required authority, source identity, approved purpose, rights, taxonomy snapshot, evidence, policy, sensitivity transform, review, correction support, rollback target, or consumer binding is missing; when a taxon, occurrence, range, model, legal-status, or source role would collapse; when sensitive precision could leak; when a named path or command does not match the pinned repository; or when the proposed rollback target has not been rechecked under current rights and sensitivity controls.

## Open verification

| Item | Current posture | Smallest truthful next step |
|---|---|---|
| Sensitive occurrence production controls | `RUNBOOK GROUNDED / POLICY-RELEASE HOLD` | Keep the merged review/handoff procedure bounded; separately implement and review executable sensitivity policy, public/restricted conversion enforcement, accountable review, and release closure before any public-sensitive occurrence path graduates |
| Full rollback procedure | `PARTIAL / PROPOSAL-ERA` | Reconcile it against the current shared `RollbackCard`, synthetic rehearsal, Fauna release topology, current policy, actors, commands, and holds; remove or repair the absent validation-runbook reference |
| Parent runbook index | `STALE` | Recompute its local-README inventory after the merged Atmosphere and Fauna boundary work settles; do not broaden this one-file lane update into an unverified subtree recount |
| Accountable roles | `NEEDS VERIFICATION` | Record verified scope, authority, separation, and revocation for every required Fauna role |
| Live Fauna operations | `HOLD / UNKNOWN` | Require admitted sources, executable connectors, rights and sensitivity closure, version-pinned taxonomy, evidence, policy, review, release topology, correction, rollback, monitoring, and current runtime evidence |

## Related surfaces

- Parent runbook index: [`docs/runbooks/README.md`](../README.md)
- Fauna domain boundary: [`docs/domains/fauna/README.md`](../../domains/fauna/README.md)
- Fauna sensitivity doctrine: [`docs/domains/fauna/SENSITIVITY.md`](../../domains/fauna/SENSITIVITY.md)
- Fauna policy documentation: [`docs/domains/fauna/POLICY.md`](../../domains/fauna/POLICY.md)
- Directory Rules: [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md)
- Accepted placement decision: [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)

## Maintenance and document rollback

Update this README when a child is added, removed, renamed, materially re-scoped, or changes maturity; when Fauna taxonomy, source-role, EBD-rights, sensitivity, geoprivacy, evidence, policy, release, correction, or rollback boundaries change; or when accountable authority, executable validation, live-source, runtime, deployment, promotion, or publication evidence changes.

This is a documentation-only change. Before merge, close or abandon its draft pull request. After merge, revert the documentation commit or submit a smaller reviewed forward fix. Blob `8b137891791fe96927ad78e64b0aad7bded08bdc` restores the prior one-byte file, but reverting this README would not change source, lifecycle, release, runtime, rollback, or public state.

[Back to top](#top)
