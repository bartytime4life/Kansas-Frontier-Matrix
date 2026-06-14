<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-archaeology-rollback-readme
title: Archaeology Rollback Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <archaeology-pipeline-owner>
  - <archaeology-domain-steward>
  - <rollback-steward>
  - <release-steward>
  - <review-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-archaeology-rollback-review-and-evidence-gates
path: pipelines/domains/archaeology/rollback/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/archaeology/README.md
  - pipelines/domains/archaeology/validate/README.md
  - docs/domains/archaeology/DATA_LIFECYCLE.md
  - docs/domains/archaeology/VALIDATORS.md
  - docs/runbooks/archaeology/ROLLBACK_RUNBOOK.md
  - docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - docs/domains/archaeology/RELEASE_INDEX.md
  - pipeline_specs/archaeology/rollback.yaml
  - contracts/domains/archaeology/
  - schemas/contracts/v1/domains/archaeology/
  - policy/domains/archaeology/
  - data/catalog/domain/archaeology/
  - data/triplets/archaeology/
  - data/published/layers/archaeology/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/archaeology/
  - release/manifests/archaeology/
tags: [kfm, pipelines, domains, archaeology, rollback, release-manifest, rollback-card, correction-notice, evidence-bundle, policy, governance]
notes:
  - "This README fills the blank pipelines/domains/archaeology/rollback path as a nested executable Archaeology rollback-support sublane."
  - "Rollback logic is executable support only; it does not own rollback decisions, release decisions, ReleaseManifests, RollbackCards, CorrectionNotices, policy, review decisions, EvidenceBundle truth, catalog truth, schemas, source descriptors, or public API authority."
  - "Rollback is receipt-backed, review-gated, and history-preserving. It is not ad-hoc cleanup, silent replacement, or manual file removal."
  - "Concrete executable behavior, CI coverage, release wiring, public API/map behavior, and rollback schemas remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Rollback Pipeline

> Executable Archaeology sublane for materializing rollback support packages, manifest checks, inverse-diff checks, invalidation lists, receipts, artifact reversion plans, and release-system handoffs after a governed rollback decision — while preserving ReleaseManifest authority, RollbackCard authority, CorrectionNotice lineage, EvidenceBundle bindings, policy/review refs, artifact digests, correction paths, and audit history.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-archaeology%20rollback-8a6d3b)
![authority](https://img.shields.io/badge/authority-rollback%20support%20only-0a7ea4)
![history](https://img.shields.io/badge/history-preserved-d62728)
![publication](https://img.shields.io/badge/publication-release%20authority%20external-d62728)

**Status:** Draft  
**Path:** `pipelines/domains/archaeology/rollback/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Archaeology  
**Sublane:** Rollback / correction support / release reversion materialization  
**Placement posture:** nested executable sublane under `pipelines/domains/archaeology/`; concrete behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no independent rollback or release authority; this lane may materialize rollback support only after a governed rollback decision and must preserve correction, invalidation, evidence, policy, artifact-digest, and rollback lineage.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Rollback anti-collapse rules](#3-rollback-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Rollback support scope](#6-rollback-support-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal rollback support receipt](#11-minimal-rollback-support-receipt)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Correction, stale state, and derivative invalidation](#13-correction-stale-state-and-derivative-invalidation)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/archaeology/rollback/` is the executable sublane for Archaeology rollback support.

It supports materialization for:

- rollback preflight checks after a rollback has been requested or authorized by release workflow;
- prior-release verification using ReleaseManifest refs and recorded digests;
- CorrectionNotice and invalidation-list handoffs;
- inverse-diff or equivalent reversion-plan verification where an implementation exists;
- release-manifest reversion handoff packages;
- public artifact digest comparison, artifact reversion planning, and artifact receipt emission;
- downstream derivative invalidation for catalog projections, graph/triplet projections, tiles, extracts, cards, indexes, and governed API/UI caches;
- controlled-domain rollback where public representation, transform receipt, policy, review, and rollback-target refs must remain visible;
- hold records for missing rollback target, invalid prior release, missing CorrectionNotice, missing ReviewRecord, missing EvidenceBundle, invalid artifact digest, unresolved policy, or derivative-invalidation gaps.

This directory implements or will implement the **how** of rollback support. It does not decide rollback, decide release, author the RollbackCard, author the ReleaseManifest, define policy, decide review outcomes, own EvidenceBundle truth, own catalog truth, mutate canonical stores by itself, serve public API responses, or silently remove public history.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/archaeology/`? | Archaeology is a domain lane under the domain-pipeline umbrella. | CONFIRMED path pattern; behavior NEEDS VERIFICATION |
| Why `rollback/`? | This sublane materializes rollback checks, receipts, invalidations, and release-system handoffs. | PROPOSED / NEEDS VERIFICATION |
| Does this decide rollback? | No. Rollback authority lives in release workflow through RollbackCard, review, and release-authority records. | CONFIRMED governance posture |
| Does this edit history? | No. It prepares receipt-backed reversion and invalidation support while preserving release history. | CONFIRMED doctrine posture |
| Can public clients read this lane? | No. Public clients use governed APIs and released artifacts only. | CONFIRMED trust membrane posture |

> [!IMPORTANT]
> A rollback-support run is not a rollback decision. Archaeology rollback is valid only when a prior release target, RollbackCard, CorrectionNotice, review state, policy context, affected derivatives, and receipt-backed reversion/invalidation plan are present and resolvable.

[⬆ Back to top](#top)

---

## 3. Rollback anti-collapse rules

Rollback support must preserve release authority, correction authority, artifact lineage, evidence bindings, and rollback receipts as separate objects.

Disallowed collapses:

```text
pipeline run -> rollback approval
RollbackCard -> executable patch without verification
CorrectionNotice -> silent edit
file removal -> rollback
copy prior artifact -> release reversion
ReleaseManifest -> mutable latest pointer
prior release target -> current truth without manifest update
catalog invalidation -> catalog erasure
triplet rollback -> graph truth overwrite without receipt
public cache purge -> rollback completion
artifact digest mismatch -> acceptable drift
generated rollback summary -> evidence
```

Required distinctions:

- rollback request, ReviewRecord, PolicyDecision, RollbackCard, CorrectionNotice, ReleaseManifest, prior release target, inverse diff, RunReceipt, invalidation list, catalog projection, graph projection, public artifact, and cache invalidation remain separate;
- rollback preserves prior releases for audit and does not erase history;
- every artifact reversion is content-addressed and receipt-backed;
- stale, superseded, corrected, withdrawn, denied, and held states remain visible;
- downstream derivatives are invalidated or superseded, not silently ignored;
- public clients never read RAW, WORK, QUARANTINE, canonical/internal stores, source APIs, graph internals, vector indexes, or direct model outputs.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Archaeology rollback support.

Appropriate contents include:

- fixture-only rollback dry-run entrypoints;
- RollbackCard and prior-release target validators;
- CorrectionNotice and ReviewRecord presence validators;
- ReleaseManifest digest and prior-release manifest validators;
- inverse-diff / reversion-plan verification helpers;
- artifact digest comparison and reversion-plan builders;
- invalidation-list builders for catalog, triplet, graph, tile, extract, card, index, and governed API/UI cache derivatives;
- rollback receipt emitters;
- hold routing helpers for missing rollback preconditions;
- release-system handoff helpers that do not decide rollback or release.

A good placement test:

> If the code materializes receipt-backed rollback support from an already governed rollback request or RollbackCard, it may belong here. If it decides rollback, edits policy, authors release decisions, owns catalog truth, serves the public API, writes UI state, or removes history, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers, API clients, watchers | `connectors/` or watcher roots |
| Ingest, normalize, validate, publish, or catalog logic | sibling Archaeology pipeline sublanes |
| Source descriptors / source registry entries | `data/registry/sources/archaeology/` or approved registry home |
| Domain doctrine and object meaning | `docs/domains/archaeology/`, `contracts/domains/archaeology/` |
| JSON Schemas | `schemas/contracts/v1/domains/archaeology/` or accepted schema home |
| Policy, rights, review, release rules | `policy/...` and review responsibility roots |
| Rollback decisions, ReleaseManifest authorship, RollbackCards | `release/...` responsibility roots |
| Fixtures | `fixtures/domains/archaeology/rollback/` or accepted fixture home |
| Tests | `tests/pipelines/domains/archaeology/rollback/` or accepted test home |
| Lifecycle records | `data/...` lifecycle homes |
| Public API or map viewer code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Direct model summaries or generated answer text | Governed AI/released artifact paths only after review |

[⬆ Back to top](#top)

---

## 6. Rollback support scope

| Scope area | Rollback-lane responsibility | Failure behavior |
|---|---|---|
| Rollback authority | Confirm RollbackCard or authorized rollback request exists and resolves. | Hold; no artifact change. |
| Prior release target | Verify prior ReleaseManifest, content hashes, and rollback target. | Hold. |
| Correction context | Confirm CorrectionNotice and review refs exist where required. | Hold if missing. |
| Evidence binding | Confirm current and prior EvidenceBundle refs resolve. | Hold. |
| Artifact integrity | Compare current and target artifacts by digest. | Fail closed on mismatch. |
| Reversion plan | Verify inverse patch or equivalent reversion plan where implemented. | Hold on unverifiable plan. |
| Derivative invalidation | Emit invalidation list for dependent outputs and caches. | Hold if incomplete. |
| Release handoff | Prepare receipt-backed reversion handoff for release system. | No direct release decision. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Archaeology rollback support run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Rollback is a release-stage correction operation, not a shortcut around the lifecycle.

Normal stance:

1. **Read** authorized rollback inputs only: RollbackCard refs, CorrectionNotice refs, ReviewRecord refs, PolicyDecision refs, current ReleaseManifest refs, prior ReleaseManifest refs, artifact refs, catalog/triplet refs, EvidenceBundle refs, and rollback specs.
2. **Verify** every required reference resolves and every digest matches expected current and target states.
3. **Build** reversion and invalidation support: inverse diffs, artifact target refs, derivative invalidation lists, cache invalidation hints, and receipt payloads.
4. **Emit** rollback support receipts, digest checks, and release-system handoff packages.
5. **Hold** missing rollback, evidence, correction, review, policy, freshness, derivative, or integrity preconditions.
6. **Never silently remove, overwrite, or mutate canonical stores, source captures, release decisions, public UI state, or direct API behavior.**

Rollback here means support-material assembly after a governed rollback decision. It is not approval and not cleanup.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Archaeology rollback support run must check or explicitly fail closed on:

1. **RollbackCard gate** — rollback identity, target prior release, reason, review ref, and invalidation scope are present.
2. **ReleaseManifest gate** — current and target release manifests resolve and content hashes match expectations.
3. **CorrectionNotice gate** — what changed, why, and what derivatives are invalidated are explicit.
4. **Review/separation gate** — review and release authority separation is present where materiality requires it.
5. **EvidenceBundle gate** — current and target evidence refs resolve or the rollback holds.
6. **Policy gate** — finite policy outcome exists for rollback action and controlled derivative handling.
7. **Artifact digest gate** — current and target artifacts, tiles, extracts, cards, indexes, and manifests match their recorded hashes.
8. **Reversion-plan gate** — inverse patch or equivalent reversion plan is verified before any handoff changes public artifacts.
9. **Derivative invalidation gate** — catalog, triplet, graph, tile, extract, card, index, API cache, and UI cache dependencies are listed.
10. **History-preservation gate** — prior and failed releases remain queryable/auditable; rollback is not erasure.
11. **Trust membrane gate** — outputs are suitable for release-system / governed API consumption only.
12. **No-direct-decision gate** — this lane does not create rollback, correction, release, or policy decisions.
13. **No-direct-UI/API gate** — no side effects in public UI, public API routes, or direct model responses.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/archaeology/rollback/
├── README.md                         # this file
├── ROLLBACK_CONTRACT.md              # PROPOSED: Archaeology rollback support execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/public-safe release fixture only
├── validate_rollback_card.py         # PROPOSED
├── validate_release_manifests.py     # PROPOSED
├── validate_correction_notice.py     # PROPOSED
├── validate_evidence_bundle_refs.py  # PROPOSED
├── validate_policy_review.py         # PROPOSED
├── verify_reversion_plan.py          # PROPOSED
├── build_invalidation_list.py        # PROPOSED
├── build_release_handoff.py          # PROPOSED, no release authority
├── emit_rollback_receipt.py          # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/archaeology/rollback.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted release/receipt homes under `release/candidates/archaeology/`, `release/manifests/archaeology/`, `data/receipts/`, and approved artifact homes, with rollback decisions remaining in `release/` and public serving remaining behind governed API/UI roots.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/archaeology/rollback/` or accepted fixture home | Synthetic/public-safe release fixture. |
| RollbackCard | `release/manifests/archaeology/` or accepted release rollback home | Decision authority, not owned here. |
| CorrectionNotice | `release/...` or accepted correction home | Required for rollback context. |
| Current ReleaseManifest | `release/manifests/archaeology/` | Input by stable ref and digest. |
| Target prior ReleaseManifest | `release/manifests/archaeology/` | Rollback target by stable ref and digest. |
| Evidence proof | `data/proofs/evidence_bundle/` | Required and resolved before reversion handoff. |
| Public artifacts | `data/published/layers/archaeology/` or accepted public artifact home | Input/output by content hash only. |
| Rollback support receipt | `data/receipts/pipeline/archaeology/rollback/<run_id>.yml` or accepted receipt home | Records refs, diffs, checks, invalidations, outputs. |
| Release handoff | `release/candidates/archaeology/` | Reviewable, release-system handoff only. |

[⬆ Back to top](#top)

---

## 11. Minimal rollback support receipt

The final schema is not defined here. This example shows the minimum information an Archaeology rollback support run should preserve.

```yaml
schema_version: kfm.archaeology_rollback_support_receipt.v1
rollback_run_id: archaeology_rollback_run_YYYYMMDDThhmmssZ
pipeline_id: domains.archaeology.rollback
status: HELD
rollback_control:
  rollback_card_ref: release/manifests/archaeology/<rollback_card_id>.json
  rollback_card_hash: sha256:<hash>
  reason: needs_review
  authorized_by_release_workflow: false
release_state:
  current_release_manifest_ref: release/manifests/archaeology/<current_release_id>.json
  current_release_manifest_hash: sha256:<hash>
  target_release_manifest_ref: release/manifests/archaeology/<target_release_id>.json
  target_release_manifest_hash: sha256:<hash>
correction:
  correction_notice_ref: null
  review_record_ref: null
inputs:
  evidence_bundle_refs: []
  policy_decision_refs: []
  catalog_refs: []
  triplet_refs: []
  artifact_refs: []
checks:
  rollback_card_resolved: false
  target_release_resolved: false
  correction_notice_resolved: false
  evidence_resolved: false
  policy_resolved: false
  current_digests_match: false
  target_digests_match: false
  reversion_plan_verified: false
  invalidation_complete: false
invalidation:
  catalog_refs: []
  triplet_refs: []
  graph_projection_refs: []
  tile_refs: []
  extract_refs: []
  card_refs: []
  cache_keys: []
anti_collapse:
  rollback_run_is_approval: false
  file_removal_is_rollback: false
  correction_notice_is_silent_edit: false
  prior_release_is_mutated: false
outputs:
  receipt_ref: data/receipts/pipeline/archaeology/rollback/run_YYYYMMDDThhmmssZ.yml
  release_handoff_ref: null
history:
  prior_release_preserved: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/public-safe, and no-network** until rollback specs, release fixtures, evidence, policy, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/archaeology/rollback/
├── test_no_network_dry_run.py                  # PROPOSED
├── test_rollback_card_required.py              # PROPOSED
├── test_current_release_manifest_required.py   # PROPOSED
├── test_target_release_manifest_required.py    # PROPOSED
├── test_correction_notice_required.py          # PROPOSED
├── test_review_record_required.py              # PROPOSED
├── test_evidence_bundle_required.py            # PROPOSED
├── test_policy_decision_required.py            # PROPOSED
├── test_artifact_digests_match.py              # PROPOSED
├── test_reversion_plan_verified.py             # PROPOSED
├── test_derivative_invalidation_complete.py    # PROPOSED
├── test_no_history_removal.py                  # PROPOSED
├── test_rollback_run_not_approval.py           # PROPOSED
└── test_no_direct_ui_api_side_effect.py        # PROPOSED
```

A dry run should prove fixtures load without network access, RollbackCard/current/target manifests are required, CorrectionNotice and review refs are required, evidence and policy refs resolve, artifact digests match, reversion plans are verified, invalidation lists are complete, receipts are deterministic, and no run mutates release decisions, canonical stores, public UI, or public API routes.

[⬆ Back to top](#top)

---

## 13. Correction, stale state, and derivative invalidation

Archaeology rollback support exists because released artifacts can become unsafe, wrong, stale, superseded, or inconsistent with their release evidence.

Rollback support must:

- preserve the failed release and target prior release for audit;
- emit or verify a `CorrectionNotice` for the public-facing change;
- identify affected derivatives before handoff;
- keep stale/wrong/withdrawn/superseded states visible;
- provide deterministic invalidation lists for tiles, extracts, cards, graph projections, catalog projections, search indexes, and cache keys;
- verify that the target prior release remains internally consistent and not merely older;
- avoid rewriting history or hiding the reason for rollback.

Required chain:

```text
failure / correction trigger
  -> review
  -> RollbackCard
  -> rollback support checks
  -> reversion-plan + invalidation receipt
  -> release-system handoff
  -> ReleaseManifest reversion / supersession
  -> governed API/UI consumption of the reverted release
```

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/archaeology/rollback/README.md` file;
- identifies this directory as a nested executable Archaeology rollback-support sublane;
- prevents source, ingest, normalize, validate, catalog, schema, contract, policy, rollback-decision, release-decision, public API, UI, and canonical-store authority from being placed here;
- preserves RollbackCard, ReleaseManifest, CorrectionNotice, ReviewRecord, EvidenceBundle, PolicyDecision, reversion plan, invalidation list, artifact digest, correction, release, and rollback boundaries;
- blocks pipeline-run-as-approval, file-removal-as-rollback, correction-as-silent-edit, mutable-latest-as-release, generated-summary-as-evidence, direct UI/API side effects, and history removal;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has rollback-fixture coverage, schema-backed rollback receipts, RollbackCard/ReleaseManifest/CorrectionNotice/EvidenceBundle/policy/reversion/invalidation tests, deterministic receipts, CI coverage, steward-review handoff, and rollback/correction documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `ARCH-ROLLBACK-001` | Should Archaeology rollback remain one sublane, or split into manifest validation, artifact reversion, graph rollback, and cache invalidation processors? | NEEDS VERIFICATION / ADR |
| `ARCH-ROLLBACK-002` | Which schema owns Archaeology rollback support receipts, invalidation lists, and reversion manifests? | NEEDS VERIFICATION |
| `ARCH-ROLLBACK-003` | Which release root owns RollbackCards versus ReleaseManifests versus CorrectionNotices? | NEEDS VERIFICATION |
| `ARCH-ROLLBACK-004` | Which CI job owns Archaeology rollback invariant tests? | UNKNOWN |
| `ARCH-ROLLBACK-005` | What is the minimum reversion proof for PMTiles, catalog records, graph projections, and API caches? | NEEDS VERIFICATION / ADR |
| `ARCH-ROLLBACK-006` | How should rollback handle multi-domain artifacts bundled with Archaeology context? | NEEDS VERIFICATION / ADR |
| `ARCH-ROLLBACK-007` | Which public negative state should be shown while rollback is authorized but not fully materialized? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/public-safe release and rollback fixtures plus negative tests. Do not add live source fetching, schema authority, policy authority, rollback-decision authority, release-decision authority, direct catalog writes, public UI code, public API code, release-manifest authorship, manual cleanup scripts, or generated rollback summaries until RollbackCard refs, current/target ReleaseManifest refs, CorrectionNotice refs, EvidenceBundle refs, policy decisions, reversion plans, invalidation lists, artifact digests, and deterministic receipts are proven.
