<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-flora-rollback-readme
title: Flora Rollback Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <flora-pipeline-owner>
  - <flora-domain-steward>
  - <release-steward>
  - <correction-reviewer>
  - <sensitivity-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-flora-rollback-and-correction-gates
path: pipelines/domains/flora/rollback/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/flora/README.md
  - pipelines/domains/flora/publish/README.md
  - pipelines/domains/flora/redact/README.md
  - pipelines/domains/flora/catalog/README.md
  - docs/domains/flora/README.md
  - docs/domains/flora/DATA_LIFECYCLE.md
  - docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - docs/domains/flora/RELEASE_INDEX.md
  - policy/domains/flora/
  - policy/sensitivity/flora/
  - pipeline_specs/flora/rollback.yaml
  - contracts/domains/flora/
  - schemas/contracts/v1/domains/flora/
  - data/catalog/domain/flora/
  - data/triplets/flora/
  - data/published/layers/flora/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/flora/
  - release/manifests/flora/
tags:
  - kfm
  - pipelines
  - domains
  - flora
  - rollback
  - rollback-card
  - correction-notice
  - release-manifest
  - invalidation-list
  - reverse-diff
  - evidence-bundle
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/flora/rollback path as a nested executable Flora rollback-support sublane."
  - "Flora rollback logic is executable support only; it does not own rollback decisions, release decisions, ReleaseManifests, RollbackCards, CorrectionNotices, policy, sensitivity decisions, EvidenceBundle truth, catalog truth, schemas, source descriptors, or public API authority."
  - "Rollback is authenticated, receipt-backed, and history-preserving. It is not ad-hoc cleanup, silent replacement, or manual file removal."
  - "Rollback requires a target prior release, correction context, derivative invalidation, policy/review refs, reverse-diff or equivalent verification, and receipt emission before public artifact state changes."
  - "Concrete executable behavior, CI coverage, release wiring, public API/map behavior, and rollback schemas remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Rollback Pipeline

> Executable Flora sublane for materializing rollback support packages, reverse-diff checks, invalidation lists, receipts, artifact reversion plans, and release-system handoffs after a governed rollback decision — while preserving ReleaseManifest authority, RollbackCard authority, CorrectionNotice lineage, EvidenceBundle bindings, policy/review refs, public artifact digests, correction paths, and audit history.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-flora%20rollback-2e7d32)
![authority](https://img.shields.io/badge/authority-rollback%20support%20only-0a7ea4)
![history](https://img.shields.io/badge/history-preserved-d62728)
![release](https://img.shields.io/badge/release-authority%20external-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/flora/rollback/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Flora  
**Sublane:** Rollback / correction support / release reversion materialization  
**Placement posture:** nested executable sublane under `pipelines/domains/flora/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no independent rollback or release authority; this lane may materialize rollback support only after a governed RollbackCard / release-authority decision and must preserve correction, invalidation, evidence, policy, artifact-digest, and rollback lineage.

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

`pipelines/domains/flora/rollback/` is the executable sublane for Flora rollback support.

It supports materialization for:

- rollback preflight checks after a rollback has been requested or authorized by the release workflow;
- `RollbackCard`-referenced prior-release verification;
- `CorrectionNotice` and invalidation-list handoffs;
- reverse-diff or inverse-patch verification where an implementation exists;
- release-manifest reversion handoff packages;
- public artifact digest comparison, artifact reversion planning, and artifact receipt emission;
- downstream derivative invalidation for catalog projections, graph/triplet projections, tiles, extracts, cards, indexes, and governed API/UI caches;
- controlled Flora release rollback where public representation, transform receipt, policy, review, and rollback target refs must remain visible;
- hold records for missing rollback target, invalid prior release, missing CorrectionNotice, missing ReviewRecord, missing EvidenceBundle, invalid artifact digest, unresolved policy, or derivative-invalidation gaps.

This directory implements or will implement the **how** of rollback support. It does not decide rollback, decide release, author the RollbackCard, author the ReleaseManifest, define policy, decide sensitivity handling, own EvidenceBundle truth, own catalog truth, mutate canonical stores by itself, serve public API responses, or silently remove public history.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/flora/`? | Flora is a domain lane under the domain-pipeline umbrella. | CONFIRMED path responsibility pattern; behavior NEEDS VERIFICATION |
| Why `rollback/`? | This is a narrow executable sublane for materializing rollback checks, receipts, invalidations, and release-system handoffs. | PROPOSED / NEEDS VERIFICATION |
| Does this decide rollback? | No. Rollback authority lives in the release workflow through `RollbackCard`, review, and release-authority records. | CONFIRMED governance posture |
| Does this edit history? | No. It prepares authenticated, receipt-backed reversion/invalidation support while preserving prior releases. | CONFIRMED doctrine posture |
| Can public clients read this lane? | No. Public clients use governed APIs and released artifacts only. | CONFIRMED trust membrane posture |

> [!IMPORTANT]
> A rollback-support run is not a rollback decision. Flora rollback is valid only when a prior release target, RollbackCard, CorrectionNotice, review state, policy context, affected derivatives, and receipt-backed reversion/invalidation plan are present and resolvable.

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
triplet rollback -> graph truth overwrite without mutation receipt
public cache purge -> rollback completion
artifact digest mismatch -> acceptable drift
generated rollback summary -> evidence
```

Required distinctions:

- rollback request, ReviewRecord, PolicyDecision, RollbackCard, CorrectionNotice, ReleaseManifest, prior release target, reverse diff, RunReceipt, invalidation list, catalog projection, graph projection, public artifact, and cache invalidation remain separate;
- rollback preserves prior releases for audit and does not erase history;
- every artifact reversion is content-addressed and receipt-backed;
- stale, superseded, corrected, withdrawn, denied, and held states remain visible;
- downstream derivatives are invalidated or superseded, not silently ignored;
- public clients never read RAW, WORK, QUARANTINE, canonical/internal stores, source APIs, graph internals, vector indexes, or direct model outputs.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Flora rollback support.

Appropriate contents include:

- fixture-only rollback dry-run entrypoints;
- RollbackCard and prior-release target validators;
- CorrectionNotice and ReviewRecord presence validators;
- ReleaseManifest digest and prior-release manifest validators;
- reverse-diff / inverse-patch verification helpers;
- artifact digest comparison and reversion-plan builders;
- invalidation-list builders for Flora catalog, triplet, graph, tile, extract, card, index, and governed API/UI cache derivatives;
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
| Ingest, normalize, validate, redact, publish, or catalog logic | sibling Flora pipeline sublanes |
| Source descriptors / source registry entries | `data/registry/sources/flora/` or approved registry home |
| Flora doctrine and object meaning | `docs/domains/flora/`, `contracts/domains/flora/` |
| JSON Schemas | `schemas/contracts/v1/domains/flora/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Rollback decisions, ReleaseManifest authorship, RollbackCards | `release/...` responsibility roots |
| Fixtures | `fixtures/domains/flora/rollback/` or accepted fixture home |
| Tests | `tests/pipelines/domains/flora/rollback/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet lifecycle records | `data/...` lifecycle homes |
| Public API or map viewer code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Direct model summaries or generated answer text | Governed AI/released artifact paths only after review |
| Manual public artifact cleanup scripts | Release/correction/rollback governance roots, not this lane |

[⬆ Back to top](#top)

---

## 6. Rollback support scope

| Scope area | Rollback-lane responsibility | Failure behavior |
|---|---|---|
| Rollback authority | Confirm RollbackCard / authorized rollback request exists and resolves. | Hold; no artifact change. |
| Prior release target | Verify prior ReleaseManifest, content hashes, and rollback target. | Hold. |
| Correction context | Confirm CorrectionNotice and review refs exist where required. | Hold if missing. |
| Evidence binding | Confirm current and prior EvidenceBundle refs resolve. | Hold. |
| Artifact integrity | Compare current and target artifacts by digest. | Fail closed on digest mismatch. |
| Reverse diff | Verify inverse patch or equivalent reversion plan where implemented. | Hold on unverifiable patch. |
| Derivative invalidation | Emit invalidation list for dependent outputs and caches. | Hold if incomplete. |
| Release handoff | Prepare receipt-backed reversion handoff for release system. | No direct release decision. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Flora rollback support run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Rollback is a release-stage correction operation, not a shortcut around the lifecycle.

Normal stance:

1. **Read** authorized rollback inputs only: RollbackCard refs, CorrectionNotice refs, ReviewRecord refs, PolicyDecision refs, current ReleaseManifest refs, prior ReleaseManifest refs, artifact refs, catalog/triplet refs, EvidenceBundle refs, and rollback specs.
2. **Verify** every required reference resolves and every digest matches expected current and target states.
3. **Build** reversion and invalidation support: reverse diffs, artifact target refs, derivative invalidation lists, cache invalidation hints, and receipt payloads.
4. **Emit** rollback support receipts, digest checks, and release-system handoff packages.
5. **Hold** missing rollback, evidence, correction, review, policy, freshness, derivative, or integrity preconditions.
6. **Never silently remove, overwrite, or mutate canonical stores, source captures, release decisions, public UI state, or direct API behavior.**

Rollback here means support-material assembly after a governed rollback decision. It is not approval and not cleanup.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Flora rollback support run must check or explicitly fail closed on:

1. **RollbackCard gate** — rollback identity, target prior release, reason, review ref, and invalidation scope are present.
2. **ReleaseManifest gate** — current and target release manifests resolve and content hashes match expectations.
3. **CorrectionNotice gate** — what changed, why, and what derivatives are invalidated are explicit.
4. **Review/separation gate** — correction reviewer and release authority are distinct when materiality requires it.
5. **EvidenceBundle gate** — current and target evidence refs resolve or the rollback holds.
6. **Policy gate** — finite policy outcome exists for rollback action and controlled derivative handling.
7. **Artifact digest gate** — current and target artifacts, tiles, extracts, cards, indexes, and manifests match their recorded hashes.
8. **Reverse-diff gate** — inverse patch or equivalent reversion plan is verified before any handoff changes public artifacts.
9. **Derivative invalidation gate** — catalog, triplet, graph, tile, extract, card, index, API cache, and UI cache dependencies are listed.
10. **History-preservation gate** — prior and failed releases remain queryable/auditable; rollback is not erasure.
11. **Trust membrane gate** — outputs are suitable for release system / governed API consumption only.
12. **No-direct-decision gate** — this lane does not create rollback, correction, release, or policy decisions.
13. **No-direct-UI/API gate** — no side effects in public UI, public API routes, or direct model responses.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/flora/rollback/
├── README.md                         # this file
├── ROLLBACK_CONTRACT.md              # PROPOSED: Flora rollback support execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted release fixture only
├── validate_rollback_card.py         # PROPOSED
├── validate_release_manifests.py     # PROPOSED
├── validate_correction_notice.py     # PROPOSED
├── validate_evidence_bundle_refs.py  # PROPOSED
├── validate_policy_review.py         # PROPOSED
├── verify_reverse_diff.py            # PROPOSED
├── build_invalidation_list.py        # PROPOSED
├── build_release_handoff.py          # PROPOSED, no release authority
├── emit_rollback_receipt.py          # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/flora/rollback.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted release/receipt homes under `release/candidates/flora/`, `release/manifests/flora/`, `data/receipts/`, and approved artifact homes, with rollback decisions remaining in `release/` and public serving remaining behind governed API/UI roots.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/flora/rollback/` or accepted fixture home | Synthetic or redacted release/rollback fixture. |
| RollbackCard | `release/manifests/flora/` or accepted release rollback home | Decision authority, not owned here. |
| CorrectionNotice | `release/...` or accepted correction home | Required for rollback context. |
| Current ReleaseManifest | `release/manifests/flora/` | Input by stable ref and digest. |
| Target prior ReleaseManifest | `release/manifests/flora/` | Rollback target by stable ref and digest. |
| Evidence proof | `data/proofs/evidence_bundle/` | Required and resolved before reversion handoff. |
| Public artifacts | `data/published/layers/flora/` or accepted public artifact home | Input/output by content hash only. |
| Rollback support receipt | `data/receipts/pipeline/flora/rollback/<run_id>.yml` or accepted receipt home | Records refs, diffs, checks, invalidations, outputs. |
| Release handoff | `release/candidates/flora/` | Reviewable, release-system handoff only. |

[⬆ Back to top](#top)

---

## 11. Minimal rollback support receipt

The final schema is not defined here. This example shows the minimum information a Flora rollback support run should preserve.

```yaml
schema_version: kfm.flora_rollback_support_receipt.v1
rollback_run_id: flora_rollback_run_YYYYMMDDThhmmssZ
pipeline_id: domains.flora.rollback
status: HELD
rollback_control:
  rollback_card_ref: release/manifests/flora/<rollback_card_id>.json
  rollback_card_hash: sha256:<hash>
  reason: needs_review
  authorized_by_release_workflow: false
release_state:
  current_release_manifest_ref: release/manifests/flora/<current_release_id>.json
  current_release_manifest_hash: sha256:<hash>
  target_release_manifest_ref: release/manifests/flora/<target_release_id>.json
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
  reverse_diff_verified: false
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
  receipt_ref: data/receipts/pipeline/flora/rollback/run_YYYYMMDDThhmmssZ.yml
  release_handoff_ref: null
history:
  prior_release_preserved: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/redacted, and no-network** until rollback specs, release fixtures, evidence, policy, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/flora/rollback/
├── test_no_network_dry_run.py                  # PROPOSED
├── test_rollback_card_required.py              # PROPOSED
├── test_current_release_manifest_required.py   # PROPOSED
├── test_target_release_manifest_required.py    # PROPOSED
├── test_correction_notice_required.py          # PROPOSED
├── test_review_record_required.py              # PROPOSED
├── test_evidence_bundle_required.py            # PROPOSED
├── test_policy_decision_required.py            # PROPOSED
├── test_artifact_digests_match.py              # PROPOSED
├── test_reverse_diff_verified.py               # PROPOSED
├── test_derivative_invalidation_complete.py    # PROPOSED
├── test_no_history_removal.py                  # PROPOSED
├── test_rollback_run_not_approval.py           # PROPOSED
└── test_no_direct_ui_api_side_effect.py        # PROPOSED
```

A dry run should prove fixtures load without network access, RollbackCard/current/target manifests are required, CorrectionNotice and review refs are required, evidence and policy refs resolve, artifact digests match, reverse diffs are verified, invalidation lists are complete, receipts are deterministic, and no run mutates release decisions, canonical stores, public UI, or public API routes.

[⬆ Back to top](#top)

---

## 13. Correction, stale state, and derivative invalidation

Flora rollback support exists because public artifacts can become unsafe, wrong, stale, superseded, or inconsistent with their release evidence.

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
  -> reverse-diff + invalidation receipt
  -> release-system handoff
  -> ReleaseManifest reversion / supersession
  -> governed API/UI consumption of the reverted release
```

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/flora/rollback/README.md` file;
- identifies this directory as a nested executable Flora rollback-support sublane;
- prevents source, ingest, normalize, validate, redact, publish, catalog, schema, contract, policy, rollback-decision, release-decision, public API, UI, and canonical-store authority from being placed here;
- preserves RollbackCard, ReleaseManifest, CorrectionNotice, ReviewRecord, EvidenceBundle, PolicyDecision, reverse diff, invalidation list, artifact digest, correction, release, and rollback boundaries;
- blocks pipeline-run-as-approval, file-removal-as-rollback, correction-as-silent-edit, mutable-latest-as-release, generated-summary-as-evidence, direct UI/API side effects, and history removal;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has rollback-fixture coverage, schema-backed rollback receipts, RollbackCard/ReleaseManifest/CorrectionNotice/EvidenceBundle/policy/reverse-diff/invalidation tests, deterministic receipts, CI coverage, steward-review handoff, and rollback/correction documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `FLORA-ROLLBACK-001` | Should Flora rollback remain one sublane, or split into manifest validation, artifact reversion, graph rollback, and cache invalidation processors? | NEEDS VERIFICATION / ADR |
| `FLORA-ROLLBACK-002` | Which schema owns Flora rollback support receipts, invalidation lists, and reverse-diff manifests? | NEEDS VERIFICATION |
| `FLORA-ROLLBACK-003` | Which release root owns RollbackCards versus ReleaseManifests versus CorrectionNotices? | NEEDS VERIFICATION |
| `FLORA-ROLLBACK-004` | Which CI job owns Flora rollback invariant tests? | UNKNOWN |
| `FLORA-ROLLBACK-005` | What is the minimum reverse-diff proof for PMTiles, catalog records, graph projections, and API caches? | NEEDS VERIFICATION / ADR |
| `FLORA-ROLLBACK-006` | How should rollback handle multi-domain artifacts where Flora, Habitat, Hydrology, and Hazards layers are bundled together? | NEEDS VERIFICATION / ADR |
| `FLORA-ROLLBACK-007` | Which public negative state should be shown while rollback is authorized but not fully materialized? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/redacted release and rollback fixtures plus negative tests. Do not add live source fetching, schema authority, policy authority, rollback-decision authority, release-decision authority, direct catalog writes, public UI code, public API code, release-manifest authorship, manual cleanup scripts, or generated rollback summaries until RollbackCard refs, current/target ReleaseManifest refs, CorrectionNotice refs, EvidenceBundle refs, policy decisions, reverse diffs, invalidation lists, artifact digests, and deterministic receipts are proven.
