<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/focus-mode-state-transitions-rollback-to-prior
title: Transition — PUBLISHED → rolled-back (prior release re-promoted)
type: standard
version: v0.1
status: draft
owners: <FOCUS-MODE-DOCTRINE-OWNER> · NEEDS VERIFICATION
created: 2026-05-24
updated: 2026-05-24
policy_label: public
related:
  - docs/focus-mode/state/revocation-state.md §6
  - docs/focus-mode/state/transitions/published-to-revoked.md
  - docs/focus-mode/state/lifecycle-states.md
  - docs/focus-mode/state/README.md §11
tags: [kfm, focus-mode, state, transition, rollback, rollback-card, supersession, correction-notice]
notes:
  - One of five prose transition specs under docs/focus-mode/state/transitions/.
  - Path placement diverges from Directory Rules v1.2 §6.7.2; tracked as OPEN-DR-09.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Transition — `PUBLISHED` → `rolled-back` (prior release re-promoted)

> *A prior `ReleaseManifest` is re-promoted as the current release. The new release transitions to `rolled-back`; the prior release transitions back to `live`. A `RollbackCard` and (usually) a `CorrectionNotice` are issued.*

![status](https://img.shields.io/badge/status-draft-yellow)
![class](https://img.shields.io/badge/class-restoration-orange)
![rollback-card](https://img.shields.io/badge/RollbackCard-required-success)
![supersession-chain](https://img.shields.io/badge/supersession--chain-preserved-success)
![path-status](https://img.shields.io/badge/path-PROPOSED-orange)

**Status:** draft · **Owners:** `<FOCUS-MODE-DOCTRINE-OWNER>` *(NEEDS VERIFICATION)* · **Last updated:** 2026-05-24

> [!IMPORTANT]
> **Rollback is a forward state transition, not an undo.** The rolled-back release remains addressable for replay; the prior release becomes current again as a new event in the audit chain. The `supersession_chain` records the order. Rollback does not delete history.

---

## Contents

1. [Trigger conditions](#1-trigger-conditions)
2. [Pre-conditions](#2-pre-conditions)
3. [Post-conditions](#3-post-conditions)
4. [Required receipts](#4-required-receipts)
5. [Forward path after rollback](#5-forward-path-after-rollback)
6. [Diagram](#6-diagram)
7. [Pairing with revocation](#7-pairing-with-revocation)
8. [Anti-patterns](#8-anti-patterns)
9. [Cross-references](#9-cross-references)

---

## 1. Trigger conditions

| Trigger | Rollback reason code *(per [`revocation-state.md` §6.1](../revocation-state.md#61-rollback-reason-codes-proposed-enum))* |
|---|---|
| New release retracted; prior release more accurate. | `evidence_invalidated_post_release` |
| New release broke a working behavior; revert. | `regression` |
| Policy bundle change reverted; matching release reverted. | `policy_revert` |
| Temporary rollback while a fix is built; expected to be re-rolled-forward later. | `correction_pending_rebuild` |
| Urgent rollback for safety/legal reasons. | `emergency` |

[↑ Back to top](#top)

---

## 2. Pre-conditions

| Pre-condition | Source |
|---|---|
| A current `PUBLISHED` release exists *(the one to be rolled back)*. | Release store. |
| A prior `PUBLISHED` release exists for the same artifact and is addressable. | Release store; `supersession_chain`. |
| The prior release's state has been re-validated *(its evidence still resolves; it has not itself been independently revoked)*. | Pre-flight check. |
| Rollback issuer has authority for this lane *(role-checked; sensitive lanes may require multi-signature)*. | Role allowlist. |
| Rollback reason is within the §6.1 enum. | `RollbackCard` validation. |

> [!NOTE]
> **Rollback requires an addressable prior release.** A rollback into "the state before anything was published" is not a rollback — it is effectively a revocation with no replacement *(see [`published-to-revoked.md`](./published-to-revoked.md))*.

[↑ Back to top](#top)

---

## 3. Post-conditions

| Post-condition | Carrier |
|---|---|
| Signed `RollbackCard` issued, linking rolled-back release ↔ restored prior release. | `schemas/contracts/v1/release/rollback_card.schema.json` *(PROPOSED)*. |
| Rolled-back release transitions to state `rolled-back`. | Release record. |
| Prior release transitions back to `live` *(it is the current release again)*. | Release record. |
| `supersession_chain` updated to record the new ordering. | Release index. |
| `CorrectionNotice` *(public-facing)* issued for non-trivial rollbacks. | Public-facing record. |
| Public surfaces re-bind to the restored prior release *(clients see the prior release's content as current)*. | UI / governed API behavior. |
| Cached payloads referencing the rolled-back release transition to payload state `stale` and re-resolve on next request *(may produce `ANSWER` from the restored release, or `ABSTAIN` if the request scope no longer aligns)*. | Runtime behavior. |
| Audit chain link: rollback receipt references both releases and the reason code. | Receipt chain. |

[↑ Back to top](#top)

---

## 4. Required receipts

| Receipt | Required? | Notes |
|---|---|---|
| `RollbackCard` | yes | Full field set per [`revocation-state.md` §6](../revocation-state.md#6-rollback-card-contract). |
| Issuer identity + signature | yes | Detached signature over the card body. |
| Rolled-back release ref | yes | The release being demoted from `live`. |
| Restored release ref | yes | The prior release being re-promoted to `live`. |
| `supersession_chain` entry | yes | Records the chronological ordering. |
| `CorrectionNotice` *(public-facing)* | yes for non-trivial rollbacks | Explains the rollback to public users. |
| Reason code from §1 | yes | Routing and metrics. |

[↑ Back to top](#top)

---

## 5. Forward path after rollback

| Scenario | Next state |
|---|---|
| Rollback was `emergency` or `regression`; engineering fix in flight. | New release candidate prepared; standard promotion pipeline; eventual `PUBLISHED` supersedes the restored prior release. |
| Rollback was `policy_revert`; policy bundle revision restored. | No new release needed *(unless content also needs to change)*; prior release continues as `live`. |
| Rollback was `correction_pending_rebuild`. | New release candidate prepared with the corrected content; standard pipeline; eventual `PUBLISHED` re-rolls-forward. |
| Rollback was `evidence_invalidated_post_release`. | The rolled-back release may also be revoked separately *(see §7 pairing)*. |

> [!NOTE]
> **A re-roll-forward is a new transition.** A future `PUBLISHED` that supersedes the restored prior release goes through the full promotion pipeline — gate A through G. It is not a "undo the rollback" operation.

[↑ Back to top](#top)

---

## 6. Diagram

```mermaid
sequenceDiagram
  participant Issuer
  participant RelStore as Release store
  participant Idx as Supersession chain
  participant Client as Public client
  Note over RelStore: prior release R_n-1 exists (state: superseded-by R_n)<br/>current release R_n is live
  Issuer->>RelStore: prepare RollbackCard<br/>(R_n → rolled-back, R_n-1 → live, reason)
  Issuer->>Issuer: sign card
  Issuer->>RelStore: issue RollbackCard
  RelStore->>Idx: update supersession chain<br/>(R_n-1 restored as live)
  RelStore->>RelStore: publish CorrectionNotice (if non-trivial)
  Note over Client: next request triggers re-resolution
  Client->>RelStore: GET current release for area/subject
  RelStore-->>Client: R_n-1 (restored)
  Client-->>Client: rebind; serve ANSWER from R_n-1
```

[↑ Back to top](#top)

---

## 7. Pairing with revocation

Rollback and revocation are **distinct transitions**; either may occur without the other, or both may occur together.

| Scenario | Issue rollback? | Issue revocation? |
|---|---|---|
| New release has a bug; prior release is fine; revert. | yes | no — the new release remains addressable as a historical mistake |
| New release contains content that should never have been published *(rights, sensitivity, legal)*; prior release is fine. | yes *(restore prior)* | yes *(withdraw the new release entirely)* — pair the two transitions |
| Prior release is the problem; new release is also a problem. | no — there is no good release to restore | yes for current; separate revocation for prior *(consider whether anything should be served)* |
| Current release is fine; prior release retroactively found problematic. | no — no rollback needed | yes for the prior release; `live` state of current is unaffected |

> [!IMPORTANT]
> **If pairing, issue both receipts.** A `RollbackCard` does not implicitly revoke; a revocation manifest does not implicitly rollback. Each transition carries its own audit chain link. *(See [`published-to-revoked.md` §5](./published-to-revoked.md#5-rollback-target).)*

[↑ Back to top](#top)

---

## 8. Anti-patterns

| Anti-pattern | Why it breaks doctrine |
|---|---|
| **Rollback deletes the rolled-back release** — release record removed from the store. | Audit replay impossible; chain broken. |
| **No `CorrectionNotice` on user-visible rollback** — public users see content change without explanation. | Audit transparency broken from the user's perspective. |
| **`supersession_chain` overwritten** — chain edited in place to hide the rolled-back release. | Audit chain destroyed. |
| **Implicit revocation** — rollback issued with the assumption that the rolled-back release is also revoked, but no revocation manifest issued. | Two transitions conflated; rolled-back release remains technically serveable in some paths. |
| **Rollback without prior release** — "rollback to nothing". | Not a rollback; should be modeled as revocation with no replacement. |
| **Signature missing** — unsigned `RollbackCard` accepted. | Anyone can forge a rollback. |
| **Rolling back to a release that is itself revoked** — restored release was independently revoked. | Pre-flight check should reject; otherwise the restored release stops serving immediately and the rollback is moot. |
| **Reason code free-form** — rollback reason text outside the enum. | Routing broken; metrics broken. |
| **Re-roll-forward without new pipeline pass** — restored release "promoted" to current again without going through gates A–G. | Bypasses promotion contract; new content reaches users without re-validation. |

[↑ Back to top](#top)

---

## 9. Cross-references

- [`docs/focus-mode/state/revocation-state.md`](../revocation-state.md) §6 — full `RollbackCard` contract.
- [`docs/focus-mode/state/transitions/published-to-revoked.md`](./published-to-revoked.md) — companion revocation transition.
- [`docs/focus-mode/state/lifecycle-states.md`](../lifecycle-states.md) §3 — gate G (release & rollback).
- [`docs/focus-mode/state/payload-state.md`](../payload-state.md) §2 — `stale` payload state on rollback.
- [`docs/focus-mode/state/finite-outcomes.md`](../finite-outcomes.md) — outcomes after rebinding to restored release.

---

**Last updated:** 2026-05-24 · **Doc version:** v0.1 · **Doc status:** draft · **Path status:** PROPOSED *(OPEN-DR-09)*

[↑ Back to top](#top)
