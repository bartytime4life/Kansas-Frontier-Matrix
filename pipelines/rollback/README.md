<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-rollback-readme
title: Rollback Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-owner>
  - <rollback-steward>
  - <release-steward>
  - <evidence-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/rollback/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/architecture/release-discipline.md
  - pipelines/README.md
  - pipeline_specs/rollback/
  - pipelines/domains/
  - tests/pipelines/rollback/
  - fixtures/rollback/
  - data/published/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/
  - release/manifests/
tags: [kfm, pipelines, rollback, rollback-card, correction-notice, release-manifest, invalidation, receipts, evidence-bundle, governance]
notes:
  - "This README replaces the greenfield stub at pipelines/rollback/README.md with a governed implementation-lane contract."
  - "pipelines/ is executable pipeline logic; pipeline_specs/ is declarative configuration."
  - "This lane supports rollback readiness checks. It is not release authority and does not own ReleaseManifests, RollbackCards, policies, proofs, catalog records, or public serving behavior."
  - "Domain-specific rollback support remains under domain lanes unless an ADR says otherwise."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Rollback Pipelines

> Shared executable rollback-support lane for checking prior-release targets, rollback-readiness inputs, correction notices, invalidation plans, artifact digests, receipts, and release-steward handoffs.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-shared%20rollback-2e7d32)
![authority](https://img.shields.io/badge/authority-readiness%20support%20only-0a7ea4)
![release](https://img.shields.io/badge/release%20authority-separate-d62728)

**Status:** Draft  
**Path:** `pipelines/rollback/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Sublane:** Shared rollback-readiness support  
**Placement posture:** implementation sublane under `pipelines/`; long-term framework authority remains `NEEDS VERIFICATION / ADR`.  
**Public posture:** no release decision here; outputs are readiness checks, blocker reports, invalidation plans, receipt fragments, and release-steward handoffs.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Anti-collapse rules](#3-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Lifecycle contract](#6-lifecycle-contract)
- [7. Required gates](#7-required-gates)
- [8. Directory contract](#8-directory-contract)
- [9. Inputs and outputs](#9-inputs-and-outputs)
- [10. Minimal readiness receipt](#10-minimal-readiness-receipt)
- [11. Tests and fixtures](#11-tests-and-fixtures)
- [12. Definition of done](#12-definition-of-done)
- [13. Open questions](#13-open-questions)

---

## 1. Purpose

`pipelines/rollback/` is the shared executable lane for rollback-readiness support that can be reused by domain rollback lanes and release-steward workflows.

It may support:

- current ReleaseManifest and prior ReleaseManifest comparison helpers;
- prior release target checks;
- RollbackCard input checks;
- CorrectionNotice and invalidation-list checks;
- published artifact digest checks;
- affected artifact, tile, index, graph, triplet, and API-payload inventory helpers;
- rollback drill fixtures;
- readiness receipt and blocker builders;
- adapters used by domain rollback lanes.

This directory implements the **how** of rollback-readiness checking. It does not decide that rollback should occur, author release decisions, own ReleaseManifests, create EvidenceBundles, or rewrite lifecycle history.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | Rollback helpers are executable logic: the **how**. | CONFIRMED root responsibility |
| Why a shared `rollback/` lane? | It can hold reusable readiness helpers for release and domain rollback lanes. | PROPOSED / NEEDS VERIFICATION |
| Does this replace domain rollback lanes? | No. Domain-owned rollback support stays under domain lanes unless an ADR says otherwise. | CONFIRMED boundary posture |
| Is this release authority? | No. Release decisions, manifests, and approval records remain in release responsibility roots. | CONFIRMED authority separation |
| Can public clients read this lane? | No. Public clients use governed APIs and released artifacts only. | CONFIRMED trust-membrane posture |

> [!IMPORTANT]
> Rollback is a governed release action, not cleanup and not a file move. This lane may verify and prepare rollback support, but release authority controls the transition.

[⬆ Back to top](#top)

---

## 3. Anti-collapse rules

Disallowed collapses:

```text
rollback helper pass -> rollback approval
helper output -> ReleaseManifest
RollbackCard input -> RollbackCard approval
CorrectionNotice draft -> public correction
artifact restore -> publication
cache refresh -> rollback complete
prior release pointer -> evidence proof
generated rollback summary -> evidence
pipeline run -> release authority
```

Required distinctions:

- current release, prior release, ReleaseManifest, RollbackCard, CorrectionNotice, invalidation list, EvidenceBundle, ReviewRecord, public artifact, graph/triplet state, and rollback receipt remain separate;
- rollback support can check readiness and emit blockers but cannot decide release state;
- rollback must preserve lineage, prior state, supersession, stale-state, correction, and audit trails;
- every claim about why rollback is required resolves evidence or abstains.

[⬆ Back to top](#top)

---

## 4. What belongs here

Appropriate contents include:

- fixture-only rollback drill entrypoints;
- ReleaseManifest comparison helpers;
- prior release target validators;
- RollbackCard input validators;
- CorrectionNotice and invalidation-list validators;
- artifact digest and manifest checkers;
- graph/triplet/index invalidation inventory helpers;
- rollback readiness blocker builders;
- rollback receipt builders;
- shared adapters used by domain rollback lanes.

A good placement test:

> If the code helps multiple domain or release lanes prove rollback readiness without owning the rollback decision, it may belong here.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Domain-specific rollback workflows | `pipelines/domains/<domain>/rollback/` |
| Release decisions, approvals, manifests, RollbackCards | `release/` |
| Correction decision records | `release/` or accepted correction/review home |
| Public API or UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Source access clients | `connectors/<source_id>/` or accepted connector home |
| Domain doctrine | `docs/domains/<domain>/` |
| Schemas | `schemas/contracts/v1/...` accepted schema home |
| Contracts/object meaning | `contracts/...` accepted contract home |
| Policy | `policy/...` responsibility roots |
| Declarative rollback specs | `pipeline_specs/rollback/` or domain-specific spec homes |
| Fixtures | `fixtures/rollback/` or domain fixture homes |
| Tests | `tests/pipelines/rollback/` or domain test homes |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |

[⬆ Back to top](#top)

---

## 6. Lifecycle contract

Rollback support must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
PUBLISHED -> CORRECTION or ROLLBACK, with lineage preserved
```

Normal stance:

1. **Read** fixture, ReleaseManifest, published artifact, prior release, CorrectionNotice, ReviewRecord, EvidenceBundle, policy, and receipt refs provided by an authorized caller.
2. **Verify** current and prior release refs, rollback target, artifact digests, evidence refs, review refs, correction notice, invalidation list, and rollback reason codes.
3. **Emit** rollback-readiness reports, receipts, blockers, and invalidation plans.
4. **Return** to release authority for approval and state transition.
5. **Never rewrite history, create release decisions, or publish directly.**

[⬆ Back to top](#top)

---

## 7. Required gates

Every shared rollback component must check or fail closed on:

1. **Caller authority gate** — release steward, domain rollback lane, or approved drill scope must be present.
2. **Current release gate** — current ReleaseManifest and artifact digests resolve.
3. **Prior release gate** — rollback target and prior release refs resolve.
4. **RollbackCard gate** — required RollbackCard inputs exist before approval handoff.
5. **CorrectionNotice gate** — correction or rollback reason packet is present where required.
6. **Evidence gate** — evidence refs supporting the rollback reason resolve or the reason abstains.
7. **Review gate** — material rollback has review posture and separation-of-duties posture.
8. **Invalidation gate** — affected artifacts, indexes, graph/triplets, and API payloads are inventoried.
9. **Receipt gate** — every readiness invocation emits deterministic receipt/report metadata.
10. **No-history-rewrite gate** — rollback support never erases lineage or prior receipts.
11. **No-direct-release gate** — rollback support does not author or approve ReleaseManifests.
12. **No-direct-publish gate** — rollback support does not change public artifacts as a side effect.

[⬆ Back to top](#top)

---

## 8. Directory contract

Recommended shape:

```text
pipelines/rollback/
├── README.md
├── ROLLBACK_SHARED_CONTRACT.md        # PROPOSED
├── run_dry_fixture.py                 # PROPOSED
├── validate_current_release.py        # PROPOSED
├── validate_prior_release_target.py   # PROPOSED
├── validate_rollback_card_inputs.py   # PROPOSED
├── validate_correction_notice.py      # PROPOSED
├── inventory_invalidation_targets.py  # PROPOSED
├── validate_artifact_digests.py       # PROPOSED
├── build_readiness_report.py          # PROPOSED
├── emit_rollback_receipt.py           # PROPOSED only if not shared
└── adapters/                          # PROPOSED domain/release adapters only
```

Declarative specs should live outside this directory:

```text
pipeline_specs/rollback/<profile>.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted homes under `data/receipts/pipeline/`, `release/candidates/`, `release/manifests/`, and domain release/rollback homes as governed by release stewards.

[⬆ Back to top](#top)

---

## 9. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Rollback fixture | `fixtures/rollback/` or domain fixture home | Synthetic/public-safe by default. |
| Declarative spec | `pipeline_specs/rollback/` or domain spec home | The what, not executable logic. |
| Current ReleaseManifest | `release/manifests/` | Read-only input unless release authority updates. |
| Prior release target | `release/manifests/` or release index home | Must resolve by stable ref/digest. |
| Published artifact refs | `data/published/` or accepted public artifact home | Read by stable refs/digests. |
| CorrectionNotice / RollbackCard | `release/` or accepted release-control home | Release authority owns approval. |
| Invalidation plan | `release/candidates/` or accepted readiness home | Handoff only. |
| Receipt | `data/receipts/pipeline/<domain-or-release>/rollback/` or accepted receipt home | Records inputs, checks, blockers, and output refs. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced only; not created here. |

[⬆ Back to top](#top)

---

## 10. Minimal readiness receipt

```yaml
schema_version: kfm.shared_rollback_support_receipt.v1
rollback_support_run_id: rollback_support_run_YYYYMMDDThhmmssZ
pipeline_id: rollback.<profile_id>
status: HELD
caller:
  owner: release-steward-or-domain-rollback-lane
  profile_ref: pipeline_specs/rollback/<profile_id>.yaml
release:
  current_release_manifest_ref: release/manifests/<current>.json
  prior_release_manifest_ref: release/manifests/<prior>.json
checks:
  current_release_resolved: false
  prior_release_resolved: false
  rollback_target_resolved: false
  correction_notice_ready: false
  rollback_card_inputs_ready: false
  evidence_refs_resolved: false
  review_ready: false
  invalidation_inventory_ready: false
  artifact_digests_match: false
anti_collapse:
  helper_pass_is_rollback_approval: false
  helper_output_is_release_manifest: false
  cache_refresh_is_rollback_complete: false
outputs:
  readiness_report_ref: null
  invalidation_plan_ref: null
  blocker_refs: []
  receipt_ref: data/receipts/pipeline/rollback/run_YYYYMMDDThhmmssZ.yml
```

[⬆ Back to top](#top)

---

## 11. Tests and fixtures

Recommended tests:

```text
tests/pipelines/rollback/
├── test_no_network_dry_run.py              # PROPOSED
├── test_caller_authority_required.py       # PROPOSED
├── test_current_release_required.py        # PROPOSED
├── test_prior_release_target_required.py   # PROPOSED
├── test_rollback_card_inputs_required.py   # PROPOSED
├── test_correction_notice_required.py      # PROPOSED
├── test_evidence_refs_required.py          # PROPOSED
├── test_invalidation_inventory_required.py # PROPOSED
├── test_artifact_digest_checks.py          # PROPOSED
├── test_no_history_rewrite.py              # PROPOSED
├── test_no_release_manifest_side_effect.py # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, caller authority is required, current and prior releases resolve, rollback target is explicit, evidence/review context is preserved, invalidation targets are inventoried, receipts are deterministic, and no run rewrites lineage, authors ReleaseManifests, or changes public artifacts as a side effect.

[⬆ Back to top](#top)

---

## 12. Definition of done

This README is done when it:

- replaces the greenfield stub at `pipelines/rollback/README.md`;
- identifies this directory as a shared executable rollback-support lane under `pipelines/`;
- prevents release-decision authority, domain truth, schemas, contracts, policy, source descriptors, lifecycle data, EvidenceBundles, catalog authority, and publication authority from being placed here;
- preserves current release, prior release, RollbackCard, CorrectionNotice, ReleaseManifest, EvidenceBundle, ReviewRecord, invalidation plan, receipt, correction, and rollback boundaries;
- blocks helper-pass-as-approval, helper-output-as-ReleaseManifest, cache-refresh-as-complete-rollback, generated-summary-as-evidence, history rewrite, and direct publication writes;
- gives maintainers a fixture-first, receipt-emitting, fail-closed expansion pattern.

Future executable work in this lane is done only when it has public-safe rollback fixtures, no-network tests, current/prior release checks, RollbackCard/CorrectionNotice checks, evidence/review checks, invalidation inventory tests, artifact digest tests, deterministic receipts, CI coverage, release-steward handoff, and post-rollback verification documentation.

[⬆ Back to top](#top)

---

## 13. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-ROLLBACK-001` | Is `pipelines/rollback/` the final accepted home for shared rollback helpers, or should this move under `packages/`, `tools/release/`, or domain lanes by ADR? | NEEDS VERIFICATION / ADR |
| `PIPE-ROLLBACK-002` | Which schema owns shared rollback support receipts, readiness reports, invalidation plans, and blocker reason codes? | NEEDS VERIFICATION |
| `PIPE-ROLLBACK-003` | Should every domain rollback sublane call shared helpers, or only use them for current/prior release and invalidation checks? | NEEDS VERIFICATION |
| `PIPE-ROLLBACK-004` | Which CI job owns shared rollback invariant tests? | UNKNOWN |
| `PIPE-ROLLBACK-005` | Which rollback profiles belong in `pipeline_specs/rollback/` versus domain-specific specs? | NEEDS VERIFICATION |
| `PIPE-ROLLBACK-006` | Should shared rollback helpers emit full readiness reports or only receipt fragments for release stewards to adopt? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/public-safe rollback fixtures and negative tests. Do not add live public-surface changes, release-decision authority, schema authority, domain truth ownership, public API code, UI code, release-manifest writes, published-layer writes, or generated summaries until caller authority, current/prior release refs, rollback targets, correction notices, evidence refs, invalidation inventory, deterministic receipts, and post-rollback verification are proven.
