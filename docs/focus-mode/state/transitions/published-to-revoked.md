<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/focus-mode-state-transitions-published-to-revoked
title: Transition — PUBLISHED → REVOKED
type: standard
version: v0.1
status: draft
owners: <FOCUS-MODE-DOCTRINE-OWNER> · NEEDS VERIFICATION
created: 2026-05-24
updated: 2026-05-24
policy_label: public
related:
  - docs/focus-mode/state/revocation-state.md
  - docs/focus-mode/state/payload-state.md
  - docs/focus-mode/state/finite-outcomes.md §4.1 (revoked_no_alternative)
  - docs/focus-mode/state/transitions/rollback-to-prior.md
  - docs/focus-mode/state/README.md §11
tags: [kfm, focus-mode, state, transition, published, revoked, revocation-manifest, KFM-P19-FEAT-0002]
notes:
  - One of five prose transition specs under docs/focus-mode/state/transitions/.
  - Path placement diverges from Directory Rules v1.2 §6.7.2; tracked as OPEN-DR-09.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Transition — `PUBLISHED` → `REVOKED`

> *Withdrawal of a released artifact: a signed revocation manifest is issued and clients (UI, governed APIs, cached payloads) stop serving the artifact. Cached-but-revoked payloads transition to `ABSTAIN (revoked_no_alternative)` or rebind to a `replaces_with` release.*

![status](https://img.shields.io/badge/status-draft-yellow)
![class](https://img.shields.io/badge/class-withdrawal-red)
![signed](https://img.shields.io/badge/manifest-signed-success)
![ttl](https://img.shields.io/badge/TTL-honored-success)
![path-status](https://img.shields.io/badge/path-PROPOSED-orange)

**Status:** draft · **Owners:** `<FOCUS-MODE-DOCTRINE-OWNER>` *(NEEDS VERIFICATION)* · **Last updated:** 2026-05-24

> [!CAUTION]
> **A revocation takes effect immediately.** TTL governs the re-fetch cadence of the manifest, not a grace period for continued serving. The moment a client fetches a valid revocation manifest, the revoked artifact MUST stop serving. *(See [`revocation-state.md` §4](../revocation-state.md#4-ttl-semantics).)*

---

## Contents

1. [Trigger conditions](#1-trigger-conditions)
2. [Pre-conditions](#2-pre-conditions)
3. [Post-conditions](#3-post-conditions)
4. [Required receipts](#4-required-receipts)
5. [Rollback target](#5-rollback-target)
6. [Diagram](#6-diagram)
7. [Replacement vs no-replacement paths](#7-replacement-vs-no-replacement-paths)
8. [Anti-patterns](#8-anti-patterns)
9. [Cross-references](#9-cross-references)

---

## 1. Trigger conditions

| Trigger | Revocation reason code *(per [`revocation-state.md` §3.1](../revocation-state.md#31-revocation-reason-codes-proposed-enum))* |
|---|---|
| Post-release review found evidence does not support the claim. | `evidence_invalidated` |
| Rights holder revoked the license to publish. | `rights_withdrawn` |
| New sensitivity classification forbids further publication. | `sensitivity_escalation` |
| Court order, takedown notice, regulatory action. | `legal_order` |
| Hash mismatch detected post-release *(tamper or pipeline bug)*. | `integrity_breach` |
| Newer release available; this one stays addressable but no longer current. | `superseded_with_replacement` *(in this case, prefer `superseded-by` state — see §7)* |
| Policy bundle revision forbids previously-allowed publication. | `policy_change` |

[↑ Back to top](#top)

---

## 2. Pre-conditions

| Pre-condition | Source |
|---|---|
| Artifact is currently `PUBLISHED` *(has a current `ReleaseManifest`)*. | Release store. |
| Issuer has authority to revoke for this lane *(role-checked)*. | Role allowlist; for sensitive lanes, multi-signature MAY be required *(see [`revocation-state.md` §10 open question RV-Q4](../revocation-state.md#10-open-questions))*. |
| Revocation reason is within the §3.1 enum. | Manifest validation. |
| If a replacement is intended, the replacement is itself `PUBLISHED`. | Pre-flight check. |
| Hash of the artifact to be revoked is known *(content hash + `spec_hash`)*. | Release record. |

[↑ Back to top](#top)

---

## 3. Post-conditions

| Post-condition | Carrier |
|---|---|
| Signed revocation manifest issued and published to the revocation channel. | `schemas/contracts/v1/release/revocation_manifest.schema.json` *(PROPOSED)*. |
| Artifact's state transitions to `revoked`. | Release record updated. |
| Governed APIs stop serving the artifact *(layer manifest resolver returns `DENY (release_state_deny)` with revocation reason)*. | Resolver behavior. |
| Clients that fetch the revocation manifest stop rendering the artifact. | UI behavior — see [`revocation-state.md` §8](../revocation-state.md#8-cached-but-revoked-enforcement). |
| Cached payloads that depend on the revoked evidence transition to payload state `revoked-but-cached` → `ABSTAIN (revoked_no_alternative)` *(or rebind if `replaces_with` exists)*. | Runtime behavior. |
| `CorrectionNotice` *(public-facing)* is published referencing the revocation for non-trivial cases. | Public-facing record. |
| Audit chain link: revocation manifest references the revoked `ReleaseManifest` and the issuer's role. | Receipt chain. |

> [!IMPORTANT]
> **The revoked artifact remains addressable for replay and audit.** Revocation withdraws *serving*, not the artifact itself. Future audits walking the chain can still read the revoked `ReleaseManifest` and the revocation manifest. *(See [`revocation-state.md` §6 note on rolled-back addressability](../revocation-state.md#6-rollback-card-contract).)*

[↑ Back to top](#top)

---

## 4. Required receipts

| Receipt | Required? | Notes |
|---|---|---|
| Signed revocation manifest | yes | Full field set per [`revocation-state.md` §3](../revocation-state.md#3-revocation-manifest-contract). |
| Issuer identity + signature | yes | Detached signature over the manifest body. |
| `spec_hash` binding | yes | Specific spec under which the artifact was released. |
| `content_hash` of revoked artifact | yes | So clients can verify they hold the exact form being revoked. |
| TTL setting | yes | Default 60s; `0` for hard revocations. |
| `replaces_with` reference *(optional but RECOMMENDED)* | conditional | Pointer to successor release if available. |
| `CorrectionNotice` *(public-facing)* | yes for non-trivial cases | Explains the revocation to public users. |
| Run-receipt attestations *(PROPOSED — KFM-P19-FEAT-0002)* | yes | Links the revocation to its review/audit chain. |

[↑ Back to top](#top)

---

## 5. Rollback target

Revocation is **not a rollback**. The two are distinct:

| Concern | Revocation | Rollback |
|---|---|---|
| What happens | Artifact stops serving. | A prior release is re-promoted as current. |
| Successor state | `revoked` *(no current artifact unless `replaces_with` set)* | `rolled-back` on the new release; prior release becomes `live` |
| Receipt | Revocation manifest | `RollbackCard` |

A revocation MAY be paired with a rollback if appropriate — see [`rollback-to-prior.md`](./rollback-to-prior.md). The pairing is two distinct transitions with two distinct receipts; do not collapse them.

> [!NOTE]
> **Revocation does not, by itself, restore an earlier release.** If the intent is "stop serving this release **and** restore the prior one as current", issue both a revocation manifest **and** a `RollbackCard`. Each carries its own audit chain link.

[↑ Back to top](#top)

---

## 6. Diagram

```mermaid
sequenceDiagram
  participant Issuer
  participant RelStore as Release store
  participant RevChan as Revocation channel
  participant Client as Public client (UI / governed API)
  Issuer->>RelStore: prepare revocation (content_hash + spec_hash + reason)
  Issuer->>Issuer: sign manifest
  Issuer->>RevChan: publish signed revocation manifest
  Note over Client: next request OR TTL expiry triggers re-fetch
  Client->>RevChan: GET revocation manifest
  RevChan-->>Client: signed manifest (TTL, reason, replaces_with?)
  Client->>Client: verify signature + spec_hash + content_hash
  alt verification passes, replaces_with present
    Client->>Client: rebind to replaces_with release
    Client-->>Client: new ANSWER (new AIReceipt, refs new bundle)
  else verification passes, no replacement
    Client-->>Client: ABSTAIN (revoked_no_alternative); surface revocation reason
  else verification fails (signature/hash)
    Client-->>Client: ERROR (integrity_breach); keep current cached state
  end
```

[↑ Back to top](#top)

---

## 7. Replacement vs no-replacement paths

| Path | Behavior |
|---|---|
| `replaces_with: <PUBLISHED release ref>` | Clients rebind to the replacement; surface continues with `ANSWER` from the new release; revocation receipt and rebinding receipt both recorded. |
| `replaces_with: null` | No replacement; surface demotes to `ABSTAIN (revoked_no_alternative)`; revocation reason rendered to user. |
| `superseded_with_replacement` reason code | Prefer modeling as `superseded-by` state instead of `revoked` — the artifact remains addressable as a historical record but is no longer current. See [`revocation-state.md` §2](../revocation-state.md#2-the-four-revocationrollback-states). |

> [!CAUTION]
> **`superseded-by` is not the same as `revoked`.** A superseded artifact is still part of the historical record and remains addressable for replay. A revoked artifact stops serving entirely *(though it remains addressable for audit)*. The distinction matters: revoking when you meant to supersede destroys the historical record's serveability without cause; superseding when you meant to revoke leaves bad content serveable as history.

[↑ Back to top](#top)

---

## 8. Anti-patterns

| Anti-pattern | Why it breaks doctrine |
|---|---|
| **Silent revoked render** — UI continues to render after revocation arrives. | See [`revocation-state.md` §9](../revocation-state.md#9-anti-patterns) — the canonical anti-pattern. |
| **Unsigned revocation** — manifest published without a signature. | Anyone can forge a revocation; or no one can issue a real one. |
| **TTL as grace period** — clients serve revoked artifact "until TTL expires". | Revocation is immediate; TTL is a re-fetch hint. |
| **Revocation deletes the artifact** — revoked release removed from the store. | Audit replay impossible; chain broken. |
| **Pairing implicit** — revocation issued with the assumption that a rollback will also happen, but no `RollbackCard` issued. | Implicit chaining; two distinct transitions conflated. |
| **`spec_hash` over-broad** — revocation matches multiple unintended releases. | Collateral revocation; releases not meant to be revoked stop serving. |
| **Revocation reason free-form** — reason text outside the enum. | Downstream consumers cannot route; metrics broken. |
| **Revocation without `CorrectionNotice` on a user-visible case** — public user sees content disappear with no public-facing explanation. | Audit transparency broken from the user's perspective. |

[↑ Back to top](#top)

---

## 9. Cross-references

- [`docs/focus-mode/state/revocation-state.md`](../revocation-state.md) — full revocation contract, TTL, `spec_hash` binding.
- [`docs/focus-mode/state/payload-state.md`](../payload-state.md) §2 — `revoked-but-cached` payload state.
- [`docs/focus-mode/state/finite-outcomes.md`](../finite-outcomes.md) §4.1 — `revoked_no_alternative` `ABSTAIN` reason.
- [`docs/focus-mode/state/transitions/answer-to-abstain.md`](./answer-to-abstain.md) — the public-side demotion that pairs with this transition.
- [`docs/focus-mode/state/transitions/rollback-to-prior.md`](./rollback-to-prior.md) — companion transition when a prior release is re-promoted.
- KFM-P19-FEAT-0002 *(PROPOSED — Focus Mode revocation verifier)*.

---

**Last updated:** 2026-05-24 · **Doc version:** v0.1 · **Doc status:** draft · **Path status:** PROPOSED *(OPEN-DR-09)*

[↑ Back to top](#top)
