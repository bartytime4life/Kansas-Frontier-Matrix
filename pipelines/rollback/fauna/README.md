<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-rollback-fauna-readme
title: Fauna Rollback Adapter README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-owner>
  - <rollback-steward>
  - <fauna-domain-steward>
  - <release-steward>
  - <evidence-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/rollback/fauna/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/architecture/release-discipline.md
  - pipelines/README.md
  - pipelines/rollback/README.md
  - pipelines/domains/fauna/README.md
  - docs/domains/fauna/ARCHITECTURE.md
  - pipeline_specs/rollback/fauna.yaml
  - pipeline_specs/fauna/
  - policy/domains/fauna/
  - policy/sensitivity/fauna/
  - data/published/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/
  - release/manifests/
tags: [kfm, pipelines, rollback, fauna, adapter, release-manifest, rollback-card, correction-notice, invalidation, geoprivacy, receipts, governance]
notes:
  - "This README fills the blank pipelines/rollback/fauna path as a Fauna adapter/profile under the shared rollback lane."
  - "This path is rollback-readiness support only. It is not release authority and does not own Fauna truth, ReleaseManifests, RollbackCards, EvidenceBundles, policy, catalog records, or public serving behavior."
  - "Because pipelines/rollback/fauna creates a domain-named segment under a shared helper lane, long-term placement remains NEEDS VERIFICATION / ADR if it hardens beyond adapter/profile support."
  - "Fauna rollback checks must preserve restricted/public split, geoprivacy receipt refs, EvidenceBundle refs, ReviewRecord refs, release-manifest refs, correction refs, and rollback targets."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Rollback Adapter

> Shared rollback-readiness adapter/profile for Fauna releases, focused on checking prior-release targets, Fauna release manifests, rollback-card inputs, correction-notice refs, invalidation plans, geoprivacy receipt refs, artifact digests, and release-steward handoffs without approving rollback or mutating public surfaces directly.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-fauna%20rollback%20adapter-2e7d32)
![authority](https://img.shields.io/badge/authority-readiness%20support%20only-0a7ea4)
![release](https://img.shields.io/badge/release%20authority-separate-d62728)

**Status:** Draft  
**Path:** `pipelines/rollback/fauna/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Sublane:** Shared rollback / Fauna adapter-profile support  
**Placement posture:** `PROPOSED / NEEDS VERIFICATION`; use this only as a shared adapter/profile lane. Domain-owned Fauna rollback support remains under `pipelines/domains/fauna/` unless an ADR or migration note says otherwise.  
**Public posture:** no release decision here; outputs are readiness checks, blocker reports, invalidation plans, receipt fragments, and release-steward handoffs only.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Anti-collapse rules](#3-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Adapter scope](#6-adapter-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal adapter readiness receipt](#11-minimal-adapter-readiness-receipt)
- [12. Tests and fixtures](#12-tests-and-fixtures)
- [13. Definition of done](#13-definition-of-done)
- [14. Open questions](#14-open-questions)

---

## 1. Purpose

`pipelines/rollback/fauna/` is a Fauna-specific adapter/profile under the shared rollback-readiness lane.

It may support reusable rollback-readiness checks for:

- Fauna ReleaseManifest refs and prior release targets;
- rollback-card input packets;
- correction-notice refs and reason packets;
- public-safe Fauna artifact digests;
- affected Fauna layer, index, tile, graph, triplet, and API-payload inventories;
- `OccurrencePublic`, `OccurrenceRestricted`, range, monitoring-event, status, mortality, disease, invasive-species, and derived-indicator release classes;
- geoprivacy and RedactionReceipt refs attached to public-safe Fauna derivatives;
- release-blocker and post-rollback verification handoffs.

This directory implements **adapter support** only. It does not replace `pipelines/domains/fauna/`, does not own Fauna object meaning, does not approve release state, does not author ReleaseManifests or RollbackCards, does not create EvidenceBundles, and does not rewrite lifecycle history.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable readiness-check logic: the **how**. | CONFIRMED root responsibility |
| Why `rollback/`? | Parent lane holds shared rollback-readiness helpers and adapter profiles. | CONFIRMED parent-lane posture |
| Why `fauna/` under shared rollback? | It can hold Fauna-specific adapter glue for shared helpers, but should not become primary domain authority. | PROPOSED / NEEDS VERIFICATION |
| Does this replace `pipelines/domains/fauna/`? | No. Fauna domain behavior remains under the domain pipeline lane. | CONFIRMED boundary posture |
| Is this release authority? | No. Release decisions, manifests, approvals, and rollback cards remain in release responsibility roots. | CONFIRMED authority separation |
| Can public clients read this lane? | No. Public clients use governed APIs and released artifacts only. | CONFIRMED trust-membrane posture |

> [!IMPORTANT]
> This folder is an adapter/profile lane, not a canonical Fauna release or rollback authority. If it starts owning full domain rollback behavior, it should move to `pipelines/domains/fauna/rollback/` or be governed by an ADR.

[⬆ Back to top](#top)

---

## 3. Anti-collapse rules

Disallowed collapses:

```text
adapter pass -> rollback approval
adapter output -> ReleaseManifest
RollbackCard input -> RollbackCard approval
CorrectionNotice draft -> public correction
geoprivacy receipt ref -> release approval
OccurrencePublic restore -> complete rollback
artifact digest match -> evidence proof
generated rollback summary -> evidence
pipeline run -> release authority
```

Required distinctions:

- current release, prior release, Fauna ReleaseManifest, RollbackCard, CorrectionNotice, invalidation list, EvidenceBundle, ReviewRecord, public-safe derivative, graph/triplet projection, and rollback receipt remain separate;
- Fauna object-family ownership remains in the Fauna domain lane;
- restricted/public split and geoprivacy receipt refs remain visible through rollback checks;
- rollback support can emit blockers and readiness reports but cannot decide release state;
- every claim about why rollback is required resolves evidence or abstains.

[⬆ Back to top](#top)

---

## 4. What belongs here

Appropriate contents include:

- fixture-only Fauna rollback drill entrypoints;
- Fauna ReleaseManifest comparison helpers;
- prior Fauna release target validators;
- RollbackCard input validators for Fauna release classes;
- CorrectionNotice and invalidation-list validators;
- public-safe derivative digest checkers;
- geoprivacy and RedactionReceipt ref validators;
- affected artifact, tile, index, graph, and triplet inventory helpers;
- rollback readiness blocker builders;
- rollback receipt builders;
- handoff helpers that return control to release stewards or Fauna domain lanes.

A good placement test:

> If the code adapts shared rollback-readiness helpers for Fauna while returning control to release authority, it may belong here. If it approves rollback, authors release manifests, owns Fauna truth, or changes public serving behavior directly, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Primary Fauna domain workflow | `pipelines/domains/fauna/` or accepted Fauna sublane |
| Full domain-specific rollback workflow | `pipelines/domains/fauna/rollback/` if/when accepted |
| Release decisions, manifests, approvals, RollbackCards | `release/` |
| Correction decision records | `release/` or accepted correction/review home |
| Fauna doctrine and object meaning | `docs/domains/fauna/`, `contracts/domains/fauna/` |
| JSON Schemas | `schemas/contracts/v1/domains/fauna/` or accepted schema home |
| Policy / geoprivacy / review decisions | `policy/domains/fauna/`, `policy/sensitivity/fauna/`, review roots |
| Fixtures | `fixtures/rollback/fauna/` or `fixtures/domains/fauna/` |
| Tests | `tests/pipelines/rollback/fauna/` or domain test homes |
| Lifecycle data | `data/raw/fauna/`, `data/work/fauna/`, `data/quarantine/fauna/`, `data/processed/fauna/`, `data/catalog/domain/fauna/`, `data/published/layers/fauna/` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Adapter scope

| Scope area | Adapter responsibility | Failure behavior |
|---|---|---|
| Caller authority | Require release steward, Fauna rollback lane, or approved rollback drill scope. | Hold if ownerless. |
| Current release | Resolve current Fauna ReleaseManifest, artifact refs, digests, and release-state refs. | Fail readiness. |
| Prior target | Resolve prior Fauna release target and rollback target refs. | Fail readiness. |
| Fauna release class | Preserve object-family labels and restricted/public split. | Fail on collapse. |
| Geoprivacy refs | Verify public-safe derivatives carry required transform and receipt refs. | Emit blockers. |
| Evidence/review | Preserve EvidenceBundle and ReviewRecord refs that justify rollback. | Hold or abstain. |
| Invalidation | Inventory affected artifacts, indexes, graph/triplets, and API payload refs. | Emit blockers. |
| Handoff | Return readiness report and blockers to release authority. | No release mutation side effects. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Fauna rollback support must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
PUBLISHED -> CORRECTION or ROLLBACK, with lineage preserved
```

Normal stance:

1. **Read** fixture, Fauna ReleaseManifest, public-safe artifact, prior release, CorrectionNotice, ReviewRecord, EvidenceBundle, geoprivacy receipt, and receipt refs provided by an authorized caller.
2. **Verify** current and prior release refs, rollback target, artifact digests, evidence refs, review refs, correction notice, invalidation list, geoprivacy receipt refs, and rollback reason codes.
3. **Emit** Fauna rollback-readiness reports, receipts, blockers, and invalidation plans.
4. **Return** to release authority for approval and state transition.
5. **Never rewrite history, approve release, create EvidenceBundles, or publish directly.**

[⬆ Back to top](#top)

---

## 8. Required gates

Every Fauna rollback adapter run must check or fail closed on:

1. **Caller authority gate** — release steward, Fauna rollback lane, or approved drill scope must be present.
2. **Current release gate** — current Fauna ReleaseManifest and artifact digests resolve.
3. **Prior release gate** — rollback target and prior Fauna release refs resolve.
4. **RollbackCard gate** — required RollbackCard inputs exist before approval handoff.
5. **CorrectionNotice gate** — correction or rollback reason packet is present where required.
6. **Fauna object-family gate** — taxon, occurrence, range, monitoring, status, health/death, invasive, and derived-indicator boundaries are preserved.
7. **Restricted/public split gate** — public-safe and restricted representations remain distinct.
8. **Geoprivacy receipt gate** — transform and RedactionReceipt refs are checked where required.
9. **Evidence/review gate** — evidence and review refs supporting the rollback reason resolve or the reason abstains.
10. **Invalidation gate** — affected artifacts, indexes, graph/triplets, and API payloads are inventoried.
11. **No-history-rewrite gate** — rollback support never erases lineage or prior receipts.
12. **No-direct-release gate** — rollback support does not author or approve ReleaseManifests.
13. **No-direct-publish gate** — rollback support does not change public artifacts as a side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/rollback/fauna/
├── README.md
├── FAUNA_ROLLBACK_ADAPTER_CONTRACT.md # PROPOSED
├── run_dry_fixture.py                 # PROPOSED
├── validate_current_release.py        # PROPOSED
├── validate_prior_release_target.py   # PROPOSED
├── validate_rollback_card_inputs.py   # PROPOSED
├── validate_correction_notice.py      # PROPOSED
├── validate_geoprivacy_receipts.py    # PROPOSED
├── inventory_invalidation_targets.py  # PROPOSED
├── validate_artifact_digests.py       # PROPOSED
├── emit_adapter_receipt_fragment.py   # PROPOSED
└── adapters/                          # PROPOSED caller adapters only
```

Declarative specs should live outside this directory:

```text
pipeline_specs/rollback/fauna.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use the owning Fauna domain/release homes under `release/`, `data/receipts/pipeline/`, and approved release-candidate homes.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Adapter fixture | `fixtures/rollback/fauna/` or accepted fixture home | Synthetic/public-safe by default. |
| Caller scope | release steward, `pipelines/domains/fauna/`, or approved drill | Required; this adapter does not run ownerless. |
| Current release | `release/manifests/` | Read-only input unless release authority updates. |
| Prior release target | `release/manifests/` or release index home | Must resolve by stable ref/digest. |
| Fauna artifact refs | `data/published/` or accepted public artifact home | Read by stable refs/digests. |
| CorrectionNotice / RollbackCard | `release/` or accepted release-control home | Release authority owns approval. |
| Invalidation plan | `release/candidates/` or accepted readiness home | Handoff only. |
| Receipt fragment | `data/receipts/pipeline/fauna/rollback/` or accepted receipt home | Inputs, checks, blockers, output refs. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced only; not created here. |

[⬆ Back to top](#top)

---

## 11. Minimal adapter readiness receipt

```yaml
schema_version: kfm.rollback.fauna_adapter_receipt.v1
adapter_run_id: fauna_rollback_adapter_run_YYYYMMDDThhmmssZ
pipeline_id: rollback.fauna
status: HELD
caller:
  owner: release-steward-or-fauna-rollback-lane
  profile_ref: pipeline_specs/rollback/fauna.yaml
release:
  current_release_manifest_ref: release/manifests/fauna/<current>.json
  prior_release_manifest_ref: release/manifests/fauna/<prior>.json
fauna:
  release_classes: []
  geoprivacy_receipt_refs: []
checks:
  current_release_resolved: false
  prior_release_resolved: false
  rollback_target_resolved: false
  correction_notice_ready: false
  rollback_card_inputs_ready: false
  restricted_public_split_preserved: false
  evidence_refs_resolved: false
  review_ready: false
  invalidation_inventory_ready: false
  artifact_digests_match: false
anti_collapse:
  adapter_pass_is_rollback_approval: false
  adapter_output_is_release_manifest: false
  occurrence_public_restore_is_complete_rollback: false
outputs:
  readiness_report_ref: null
  invalidation_plan_ref: null
  blocker_refs: []
  receipt_fragment_ref: data/receipts/pipeline/fauna/rollback/run_YYYYMMDDThhmmssZ.yml
```

[⬆ Back to top](#top)

---

## 12. Tests and fixtures

Recommended tests:

```text
tests/pipelines/rollback/fauna/
├── test_no_network_dry_run.py              # PROPOSED
├── test_caller_authority_required.py       # PROPOSED
├── test_current_release_required.py        # PROPOSED
├── test_prior_release_target_required.py   # PROPOSED
├── test_rollback_card_inputs_required.py   # PROPOSED
├── test_correction_notice_required.py      # PROPOSED
├── test_restricted_public_split.py         # PROPOSED
├── test_geoprivacy_receipt_refs_required.py # PROPOSED
├── test_evidence_refs_required.py          # PROPOSED
├── test_invalidation_inventory_required.py # PROPOSED
├── test_artifact_digest_checks.py          # PROPOSED
├── test_no_release_manifest_side_effect.py # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, caller authority is required, current and prior Fauna releases resolve, rollback target is explicit, restricted/public split is preserved, geoprivacy receipt refs are checked, evidence/review context is preserved, invalidation targets are inventoried, receipts are deterministic, and no run authors ReleaseManifests or changes public artifacts as a side effect.

[⬆ Back to top](#top)

---

## 13. Definition of done

This README is done when it:

- fills the blank `pipelines/rollback/fauna/README.md` file;
- identifies this directory as a Fauna adapter/profile under the shared rollback-readiness lane;
- prevents primary Fauna domain logic, release-decision authority, schemas, contracts, policy, lifecycle data, EvidenceBundles, public API, UI, catalog, and publication authority from being placed here;
- preserves caller authority, current release, prior release, RollbackCard, CorrectionNotice, ReleaseManifest, EvidenceBundle, ReviewRecord, Fauna object-family, restricted/public split, geoprivacy receipt, invalidation plan, receipt, correction, and rollback boundaries;
- blocks adapter-pass-as-approval, adapter-output-as-ReleaseManifest, public-safe-restore-as-complete-rollback, generated-summary-as-evidence, history rewrite, and direct publication writes;
- gives maintainers a fixture-first, receipt-emitting, fail-closed expansion pattern.

Future executable work in this adapter lane is done only when it has public-safe rollback fixtures, no-network tests, current/prior release checks, RollbackCard/CorrectionNotice checks, Fauna object-family checks, restricted/public split tests, geoprivacy receipt tests, evidence/review checks, invalidation inventory tests, artifact digest tests, deterministic receipts, CI coverage, release-steward handoff, and post-rollback verification documentation.

[⬆ Back to top](#top)

---

## 14. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-ROLLBACK-FAUNA-001` | Should this adapter remain under `pipelines/rollback/fauna/`, or should it move to `pipelines/domains/fauna/rollback/` once domain rollback scaffolding is accepted? | NEEDS VERIFICATION / ADR |
| `PIPE-ROLLBACK-FAUNA-002` | Which schema owns Fauna rollback readiness receipts, invalidation plans, and blocker reason codes? | NEEDS VERIFICATION |
| `PIPE-ROLLBACK-FAUNA-003` | Which Fauna release fixture set should be first-wave for no-network rollback drills? | NEEDS VERIFICATION |
| `PIPE-ROLLBACK-FAUNA-004` | Which CI job owns shared Fauna rollback adapter invariant tests? | UNKNOWN |
| `PIPE-ROLLBACK-FAUNA-005` | Should this adapter emit receipt fragments only, or full Fauna rollback readiness reports? | NEEDS VERIFICATION |
| `PIPE-ROLLBACK-FAUNA-006` | Which geoprivacy receipt vocabulary is canonical for Fauna rollback checks? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Start with synthetic/public-safe rollback fixtures and negative tests. Do not add live public-surface changes, Fauna truth ownership, release-decision authority, schema authority, policy/geoprivacy authority, public API code, UI code, release-manifest writes, published-layer writes, or generated summaries until caller authority, current/prior release refs, rollback targets, correction notices, Fauna object-family checks, restricted/public split, geoprivacy receipts, evidence refs, invalidation inventory, deterministic receipts, and post-rollback verification are proven.
