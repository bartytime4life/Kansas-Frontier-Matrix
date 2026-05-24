<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/focus-mode-state-transitions-answer-to-abstain
title: Transition — ANSWER → ABSTAIN
type: standard
version: v0.1
status: draft
owners: <FOCUS-MODE-DOCTRINE-OWNER> · NEEDS VERIFICATION
created: 2026-05-24
updated: 2026-05-24
policy_label: public
related:
  - docs/focus-mode/state/finite-outcomes.md
  - docs/focus-mode/state/payload-state.md
  - docs/focus-mode/state/revocation-state.md
  - docs/focus-mode/state/README.md §7, §10, §11
tags: [kfm, focus-mode, state, transition, answer, abstain, demotion, freshness]
notes:
  - One of five prose transition specs under docs/focus-mode/state/transitions/.
  - Path placement diverges from Directory Rules v1.2 §6.7.2; tracked as OPEN-DR-09.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Transition — `ANSWER` → `ABSTAIN`

> *Demotion path: a previously-served `ANSWER` becomes unservable because the underlying payload aged, was revoked, or failed re-closure. The runtime MUST publicly transition to `ABSTAIN` — silent removal is anti-pattern.*

![status](https://img.shields.io/badge/status-draft-yellow)
![class](https://img.shields.io/badge/class-demotion-orange)
![preserves-prior-state](https://img.shields.io/badge/preserves--prior--state-no%20(public%20transition)-orange)
![path-status](https://img.shields.io/badge/path-PROPOSED-orange)

**Status:** draft · **Owners:** `<FOCUS-MODE-DOCTRINE-OWNER>` *(NEEDS VERIFICATION)* · **Last updated:** 2026-05-24

> [!IMPORTANT]
> **This is a public-facing transition.** Unlike a `HOLD` *(which preserves the prior claim)*, an `ANSWER → ABSTAIN` transition strips the prior claim from the surface and surfaces the abstention reason. The user sees the change. *(See [`finite-outcomes.md` §7](../finite-outcomes.md#7-composition-rules) — composition rule "no silent demotion".)*

---

## Contents

1. [Trigger conditions](#1-trigger-conditions)
2. [Pre-conditions](#2-pre-conditions)
3. [Post-conditions](#3-post-conditions)
4. [Required receipts](#4-required-receipts)
5. [Rollback target](#5-rollback-target)
6. [Diagram](#6-diagram)
7. [Anti-patterns](#7-anti-patterns)
8. [Cross-references](#8-cross-references)

---

## 1. Trigger conditions

Any of the following — evaluated on the next request after a prior `ANSWER` was served — drives the transition:

| Trigger | Driving state | `ABSTAIN` reason code |
|---|---|---|
| Cited bundle's freshness window expired. | `payload state: stale` | `payload_stale` |
| Cited bundle revoked; no `replaces_with`. | `payload state: revoked-but-cached` | `revoked_no_alternative` |
| Cited bundle revoked; `replaces_with` resolved → rebound; rebinding failed closure. | `payload state: revoked-but-cached` then closure fail | `citation_closure_failed` |
| Cited bundle's release ref no longer resolves *(release record deleted/moved)*. | `payload state: unknown` | `citation_closure_failed` *(or `ERROR (resolver_failure)` if non-deterministic)* |
| Confidence threshold raised by policy update; prior `ANSWER` no longer clears. | new policy applied | `confidence_below_threshold` |
| Scope drift — request scope changed *(new envelope `time_window` outside prior cited bundle's coverage)*. | `payload state: stale` *(scope-relative)* | `query_out_of_scope` |

> [!NOTE]
> Trigger evaluation happens **per request**. A previously-served `ANSWER` on request N may transition to `ABSTAIN` on request N+1 if any trigger fires between them.

[↑ Back to top](#top)

---

## 2. Pre-conditions

| Pre-condition | Source |
|---|---|
| Prior `DecisionEnvelope (outcome=ANSWER)` exists for the same `(area, time_window, query)`. | Prior `AIReceipt` log. |
| The prior `AIReceipt` lists the bundle(s) that drove the trigger. | Replay requirement. |
| The runtime is processing a fresh `MapContextEnvelope` *(envelope `current`, see [`map-context-state.md` §4](../map-context-state.md#4-freshness-rules))*. | Envelope admission passed. |
| No policy/rights/sensitivity rule now applies that would drive `DENY` instead. | If `DENY` fits better, use the `DENY` transition path, not `ABSTAIN`. |

[↑ Back to top](#top)

---

## 3. Post-conditions

| Post-condition | Carrier |
|---|---|
| New `DecisionEnvelope` with `outcome=ABSTAIN`, reason code per §1. | Returned to caller. |
| New `AIReceipt` referencing the prior receipt and the trigger evidence *(stale bundle, revocation manifest, etc.)*. | Audit chain. |
| Public surface no longer renders the prior claim; renders abstention reason instead. | UI state change. |
| Surface-side cache invalidated for the `(area, time_window, query)` key. | Re-request would re-evaluate, not re-render. |
| If `replaces_with` exists *(revocation case)*, surface MAY immediately re-issue a request against the replacement *(receipt records the rebinding attempt)*. | Optional follow-up. |

> [!IMPORTANT]
> **The user-visible change is part of the contract.** A surface that swaps the prior claim for "we don't know" without telling the user — same widget, no notice — fails the transition. The UI MUST indicate that the prior claim was withdrawn and why.

[↑ Back to top](#top)

---

## 4. Required receipts

| Receipt | Required? | Notes |
|---|---|---|
| New `AIReceipt (outcome=ABSTAIN)` | yes | Lists trigger evidence; references prior `AIReceipt`. |
| Reference to prior `AIReceipt` | yes | Audit chain link. |
| Reference to trigger artifact | yes | Stale bundle ID, revocation manifest ID, policy version, or scope-drift envelope diff. |
| `DecisionEnvelope` | yes | `outcome=ABSTAIN`, reason code from §1. |
| `EvidenceDrawerPayload` | no | Drawer MUST NOT render the prior evidence; carries the abstention reason only. |

[↑ Back to top](#top)

---

## 5. Rollback target

Demotions to `ABSTAIN` are themselves **reversible**: a later request MAY produce `ANSWER` again if:

- The cited bundle is rebound to a fresh release, **or**
- A new release covers the same subject and the runtime re-closes citation, **or**
- The policy threshold returns to a state that admits the original evidence.

> [!NOTE]
> **No rollback artifact is required on the `ANSWER → ABSTAIN` transition itself.** The transition is forward; re-promotion to `ANSWER` later happens via a normal new request. Audit replay walks the `AIReceipt` chain in either direction.

[↑ Back to top](#top)

---

## 6. Diagram

```mermaid
sequenceDiagram
  participant UI as Public UI
  participant RT as Focus Mode runtime
  participant ST as Evidence + Revocation store
  Note over UI,RT: prior request → ANSWER served
  UI->>RT: request N+1 (same query)
  RT->>ST: re-resolve cited bundle
  ST-->>RT: stale | revoked | unresolved
  RT->>RT: try rebind to newer release / replaces_with
  alt rebind succeeds
    RT-->>UI: ANSWER (new AIReceipt, refs new bundle)
  else rebind fails / not attempted
    RT-->>UI: DecisionEnvelope(outcome=ABSTAIN, reason=<from §1>)
    Note over UI: strip prior claim; show abstention reason
  end
```

[↑ Back to top](#top)

---

## 7. Anti-patterns

| Anti-pattern | Why it breaks doctrine |
|---|---|
| **Silent demotion** — surface stops rendering the claim without telling the user. | User believes the prior claim is current; cite-or-abstain transparency broken. |
| **Cached `ANSWER` re-served after revocation** — runtime didn't re-check the revocation channel. | See [`revocation-state.md` §8](../revocation-state.md#8-cached-but-revoked-enforcement). |
| **Demote to free-form prose** — surface returns "we're not sure" without a `DecisionEnvelope`. | Outcome enum bypassed; audit broken. |
| **Demote without referencing prior receipt** — new `AIReceipt` does not link the prior. | Audit chain broken; replay impossible. |
| **Re-promote silently** — later request returns `ANSWER` without a new evidence binding. | Skipped citation closure; AI promoted to truth. |

[↑ Back to top](#top)

---

## 8. Cross-references

- [`docs/focus-mode/state/finite-outcomes.md`](../finite-outcomes.md) §4.1 — `ABSTAIN` reason codes.
- [`docs/focus-mode/state/payload-state.md`](../payload-state.md) §2 — payload states that drive demotion.
- [`docs/focus-mode/state/revocation-state.md`](../revocation-state.md) §8 — cached-but-revoked enforcement.
- [`docs/focus-mode/state/map-context-state.md`](../map-context-state.md) §4 — envelope freshness vs payload freshness.

---

**Last updated:** 2026-05-24 · **Doc version:** v0.1 · **Doc status:** draft · **Path status:** PROPOSED *(OPEN-DR-09)*

[↑ Back to top](#top)
