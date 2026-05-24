<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/focus-mode-state-finite-outcomes
title: Focus Mode — Finite Outcome State
type: standard
version: v0.1
status: draft
owners: <FOCUS-MODE-DOCTRINE-OWNER> · NEEDS VERIFICATION
created: 2026-05-24
updated: 2026-05-24
policy_label: public
related:
  - docs/focus-mode/state/README.md §7
  - docs/focus-mode/state/transitions/answer-to-abstain.md
  - docs/focus-mode/state/transitions/hold-to-deny.md
  - schemas/contracts/v1/runtime/decision_envelope.schema.json (PROPOSED)
  - schemas/contracts/v1/runtime/ai_receipt.schema.json (PROPOSED)
  - contracts/focus_mode/focus_mode_payload.md (PROPOSED)
tags: [kfm, focus-mode, state, finite-outcomes, decision-envelope, ai-receipt, cite-or-abstain]
notes:
  - Path placement diverges from Directory Rules v1.2 §6.7.2; tracked as OPEN-DR-09 in docs/focus-mode/state/README.md §15.
  - No mounted repo evidence; all repo-shaped claims labeled PROPOSED.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Focus Mode — Finite Outcome State

> *Per-outcome semantics, required artifacts, reason-code shape, and surface mappings for the seven finite outcomes a governed Focus Mode surface MAY return.*

![status](https://img.shields.io/badge/status-draft-yellow)
![doctrine](https://img.shields.io/badge/doctrine-Focus%20Mode%20v0.2-blue)
![truth-posture](https://img.shields.io/badge/posture-cite--or--abstain-success)
![outcomes](https://img.shields.io/badge/outcomes-7%20enumerated-2b8a3e)
![path-status](https://img.shields.io/badge/path-PROPOSED-orange)

**Status:** draft · **Owners:** `<FOCUS-MODE-DOCTRINE-OWNER>` *(NEEDS VERIFICATION)* · **Last updated:** 2026-05-24

> [!CAUTION]
> **Path placement diverges from Directory Rules v1.2 §6.7.2** — see [README §2.1](./README.md#21-path-divergence-must-be-resolved). Doctrine here is **CONFIRMED**; the file's location is **PROPOSED** pending OPEN-DR-09.

> [!IMPORTANT]
> **The seven outcomes are a closed enum.** Every governed Focus Mode surface, every governed API, every validator, and every policy gate MUST terminate in exactly one of: `ANSWER` · `ABSTAIN` · `DENY` · `ERROR` · `HOLD` · `PASS` · `FAIL`. Free-form text without a finite-outcome envelope is a doctrine violation. *(CONFIRMED — Atlas v1.1 §24.3.1; Doctrine Synthesis §11.)*

---

## Contents

1. [Scope](#1-scope)
2. [The seven outcomes](#2-the-seven-outcomes)
3. [Per-outcome required artifacts](#3-per-outcome-required-artifacts)
4. [Reason-code vocabularies](#4-reason-code-vocabularies)
5. [Outcome × surface matrix](#5-outcome--surface-matrix)
6. [Public-class vs validator-class outcomes](#6-public-class-vs-validator-class-outcomes)
7. [Composition rules — outcomes do not chain](#7-composition-rules)
8. [Anti-patterns](#8-anti-patterns)
9. [Open questions](#9-open-questions)
10. [Cross-references](#10-cross-references)

---

## 1. Scope

This file enumerates the **finite outcome vocabulary** used at every governed surface inside a Focus Mode and describes, per outcome:

- the **trigger conditions** that justify the outcome,
- the **required artifacts** that MUST be emitted alongside it,
- the **reason-code shape** the outcome carries,
- which **public-facing surfaces** are allowed to return it.

It does **not** define the lifecycle stages an artifact passes through (that is `lifecycle-states.md`), nor the review state of any artifact (`review-state.md`), nor the freshness state of a payload (`payload-state.md`). Outcome state and lifecycle state are **independent vocabularies**; collapsing them is anti-pattern #1 in [README §14](./README.md#14-anti-patterns).

[↑ Back to top](#top)

---

## 2. The seven outcomes

> **CONFIRMED doctrine.** The enum is closed. Adding a new outcome requires an ADR per `directory-rules.md` §2.4.

| Outcome | Class | One-line definition |
|---|---|---|
| **`ANSWER`** | public | Substantive response backed by released, citation-closed evidence and an allowing policy decision. |
| **`ABSTAIN`** | public | Non-substantive response — evidence insufficient, citation closure fails, or no released alternative; **never invents**. |
| **`DENY`** | public | Refusal because policy, rights, sensitivity, or release state forbids the answer. |
| **`ERROR`** | public | Diagnostic refusal — governed API cannot evaluate *(malformed query, missing schema, contract violation, infra failure)*. |
| **`HOLD`** | public | Pending steward, rights-holder, or policy review; surface remains in its prior state — **no silent rollback**. |
| **`PASS`** | validator | Internal validator/admission terminal — input acceptable; does **not** itself emit a public answer. |
| **`FAIL`** | validator | Internal validator/admission terminal — input unacceptable; promotion blocked; quarantine where appropriate. |

> [!NOTE]
> **`HOLD` is the only public outcome that does not produce a new claim.** It signals "no change yet" — the previously-served claim continues to render, or `ABSTAIN` if no prior claim exists. The status of the underlying review is carried by `ReviewRecord` *(see [`review-state.md`](./review-state.md))*.

[↑ Back to top](#top)

---

## 3. Per-outcome required artifacts

> **PROPOSED contract shape.** Schemas live at `schemas/contracts/v1/runtime/` *(per directory-rules.md §6.4)*. This table is reference, not source.

| Outcome | `DecisionEnvelope` | `AIReceipt` | Evidence side-car | Claim emitted? |
|---|---|---|---|---|
| `ANSWER` | `outcome=ANSWER`, allowing `PolicyDecision`, applicable `ReleaseManifest` ref | required; lists provider, model, hashes, context | `EvidenceDrawerPayload` *(projection of `EvidenceBundle`)*, with at least one resolved `EvidenceRef` | **yes** — substantive claim with citations |
| `ABSTAIN` | `outcome=ABSTAIN`, reason from §4.1 | required; records why citation closure failed or evidence was insufficient | **none** — no claim, no evidence stitched | **no** |
| `DENY` | `outcome=DENY`, `PolicyDecision=DENY`, reason from §4.2 | required; records denial provenance and policy/rights authority | **none** — denying surfaces MUST NOT leak partial evidence | **no** |
| `ERROR` | `outcome=ERROR`, diagnostic code from §4.3, no policy/release refs | optional but RECOMMENDED *(for replay)* | **none** — claim leakage forbidden | **no** |
| `HOLD` | `outcome=HOLD`, `PolicyDecision=HOLD`, `ReviewRecord` ref | required; records hold reason and holder identity | **none** — held content does not render | **no** (prior claim, if any, continues) |
| `PASS` | `outcome=PASS`, validator family + check ID | n/a *(internal)* | `ValidationReport` *(PASS)* | n/a |
| `FAIL` | `outcome=FAIL`, validator family + check ID, failure list | n/a *(internal)* | `ValidationReport` *(failure list)* | n/a |

> [!IMPORTANT]
> **Every public outcome carries a `DecisionEnvelope`.** A surface that returns a payload without an envelope — even a successful one — is doctrine-violating. The envelope is the audit hook. *(Atlas v1.1 §24.3; Doctrine Synthesis §11; CONFIRMED doctrine.)*

[↑ Back to top](#top)

---

## 4. Reason-code vocabularies

Every non-`ANSWER` public outcome carries a reason. The reason-code namespace is enumerated per outcome and is part of the envelope contract — **not free-form**.

### 4.1 `ABSTAIN` reason codes *(PROPOSED enum)*

| Code | Meaning |
|---|---|
| `evidence_insufficient` | No `EvidenceRef` resolves to a released `EvidenceBundle` covering the query. |
| `citation_closure_failed` | One or more cited refs do not resolve, or fail digest closure. |
| `payload_stale` | `FocusModePayload` is stale and no released alternative was re-bound *(see [`payload-state.md`](./payload-state.md))*. |
| `not_yet_released` | At least one referenced artifact is still `PROCESSED` or `CATALOG`. |
| `revoked_no_alternative` | Cited evidence was revoked and no released alternative covers the query. |
| `query_out_of_scope` | The Focus Mode area or temporal window does not include the requested subject. |
| `confidence_below_threshold` | Available evidence does not meet the configured confidence threshold for `ANSWER`. |

### 4.2 `DENY` reason codes *(PROPOSED enum)*

| Code | Meaning |
|---|---|
| `policy_deny` | `PolicyDecision = DENY` from runtime policy bundle. |
| `rights_deny` | Rights holder *(per `data/catalog/`)* forbids the answer at this surface/role. |
| `sensitivity_deny` | Sensitive lane *(archaeology coordinates, rare-species exact locations, living-person, DNA, critical-infrastructure detail)* — `DENY` default applies. |
| `release_state_deny` | Underlying artifact is not in a release state that permits public exposure. |
| `role_deny` | Caller's role does not have access *(authenticated surfaces only)*. |
| `geofence_deny` | Query violates a configured geofence *(e.g., burial site coordinates)*. |

### 4.3 `ERROR` diagnostic codes *(PROPOSED enum)*

| Code | Meaning |
|---|---|
| `schema_missing` | Required schema for the envelope or payload not present in `schemas/contracts/v1/`. |
| `envelope_malformed` | `MapContextEnvelope` failed admission check — see [`map-context-state.md`](./map-context-state.md). |
| `contract_violation` | Caller violated the published contract *(e.g., unsupported field, version mismatch)*. |
| `resolver_failure` | Downstream evidence/layer resolver returned unhandled error. |
| `infra_failure` | Infrastructure-level failure *(timeout, store unavailable, network)*. |
| `internal_invariant` | A doctrinal invariant tripped *(e.g., outcome enum drift detected)*. |

### 4.4 `HOLD` reason codes *(PROPOSED enum)*

| Code | Meaning |
|---|---|
| `steward_review_pending` | Domain steward review queued. |
| `rights_holder_review_pending` | Rights holder review queued *(sovereignty, descendant community, license review)*. |
| `policy_review_pending` | Policy bundle revision pending; old bundle held. |
| `correction_pending` | Correction in flight against a prior release. |
| `release_gate_pending` | Promotion gate A–G blocked but recoverable. |

> [!NOTE]
> **Reason codes are part of the contract.** Renaming or removing one is ADR-class. Adding a new code is a minor contract revision but SHOULD be coordinated with consumers. *(directory-rules.md §2.4.)*

[↑ Back to top](#top)

---

## 5. Outcome × surface matrix

> Restated from [README §7.1](./README.md#71-outcome--surface-mapping-confirmed-doctrine--atlas-v11-24332) with surface-level expansion.

| Surface | `ANSWER` | `ABSTAIN` | `DENY` | `ERROR` | `HOLD` | `PASS`/`FAIL` |
|---|---|---|---|---|---|---|
| Focus Mode runtime *(`apps/explorer-web/src/focus-modes/<area>/`)* | yes | yes | yes | yes | yes | no |
| Evidence Drawer | yes *(projection)* | yes | yes | yes | display only | no |
| Layer manifest resolver | yes | **no** *(layers don't abstain)* | yes | yes | no | no |
| Source-summary resolver | yes | yes | yes | yes | no | no |
| Domain feature/detail lookup | yes | yes | yes | yes | yes | no |
| Evidence resolver | yes | yes | yes | yes | yes | no |
| Review queue *(role-scoped)* | `ALLOW` | n/a | yes | yes | yes | no |
| Validator orchestrator | n/a | n/a | n/a | yes | n/a | yes |

> [!CAUTION]
> **Layer manifests do not `ABSTAIN`.** A released layer either exists *(returns `ANSWER` with `ReleaseManifest` ref)*, is denied *(returns `DENY`)*, or the resolver errors *(returns `ERROR`)*. There is no half-released layer. *(CONFIRMED — Atlas v1.1 §24.3.2.)*

[↑ Back to top](#top)

---

## 6. Public-class vs validator-class outcomes

> **CONFIRMED separation.** `PASS` and `FAIL` are internal validator-class outcomes; they NEVER cross the trust membrane to a public surface.

| Property | Public-class *(`ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, `HOLD`)* | Validator-class *(`PASS`, `FAIL`)* |
|---|---|---|
| Where emitted | Governed APIs, Focus Mode runtime, public UI | `tools/validators/`, promotion gates, CI |
| Carries `AIReceipt`? | yes *(except `ERROR` where optional)* | no — carries `ValidationReport` |
| Visible to public client? | yes | no — internal only |
| Drives lifecycle promotion? | no | yes — `FAIL` blocks promotion |
| Reason-code namespace | §4.1–§4.4 | validator family + check ID |

> [!IMPORTANT]
> **A validator surface MUST NOT emit `ANSWER`/`ABSTAIN`/`DENY`/`ERROR`/`HOLD` as its own outcome.** A validator's job is to report `PASS` or `FAIL` on a check; the downstream surface that consumes the report then renders one of the public outcomes. Conflating the two creates a parallel decision authority. *(Anti-pattern — `state-family collapse`, [README §14](./README.md#14-anti-patterns).)*

[↑ Back to top](#top)

---

## 7. Composition rules

Outcomes do **not** chain into a richer outcome. A surface returns **exactly one** outcome per request.

| Rule | Consequence |
|---|---|
| **One outcome per request.** | A surface MUST NOT return `ANSWER` for part of a query and `ABSTAIN` for another part in the same envelope. Split the query or emit `ABSTAIN` for the whole. |
| **No silent promotion.** | A surface MUST NOT upgrade a prior `ABSTAIN` to `ANSWER` without a new resolution and a new `DecisionEnvelope`. |
| **No silent demotion.** | A previously-served `ANSWER` that becomes unservable *(stale, revoked, denied)* MUST transition publicly to `ABSTAIN`/`DENY`/`ERROR` via the documented transition — see [`transitions/answer-to-abstain.md`](./transitions/answer-to-abstain.md) and [`transitions/published-to-revoked.md`](./transitions/published-to-revoked.md). |
| **`HOLD` preserves prior state.** | A new `HOLD` envelope does NOT alter the surface's currently-rendered claim. The prior claim continues until the hold resolves to `ANSWER`/`ABSTAIN`/`DENY`. |
| **`ERROR` is recoverable.** | An `ERROR` envelope on one request does not poison subsequent requests; each is evaluated fresh. |

[↑ Back to top](#top)

---

## 8. Anti-patterns

| Anti-pattern | Why it breaks doctrine | Mitigation |
|---|---|---|
| **Free-form fallback** — surface returns prose without an envelope. | Breaks cite-or-abstain; makes audit impossible. | Every surface terminates in one finite outcome with a `DecisionEnvelope`. |
| **Outcome enum drift** — adding `STALE`, `MAYBE`, `PARTIAL`, etc. ad hoc. | Downstream consumers join on outcome string; new strings silently bypass them. | Outcome additions are ADR-class. Folding `STALE` into `ABSTAIN` is the current convention *(see [README §15 open question](./README.md#15-open-questions-and-adr-triggers))*. |
| **Reason-code free text** — putting a free-form string where an enum value belongs. | Defeats automated reason aggregation; consumers cannot route on free text. | Reason codes come from §4.1–§4.4; new codes are minor contract revisions. |
| **`HOLD` rolls back the surface** — UI strips the prior claim when a `HOLD` arrives. | Hides the prior state; users see flicker; audit loses the prior claim. | `HOLD` preserves prior state. The surface shows a held badge, not a rollback. |
| **Validator emits public outcomes** — `tools/validators/foo.py` returns `ANSWER`. | Validators are not authoritative for public claims. | Validators return `PASS`/`FAIL`; downstream surfaces map to public outcomes. |
| **`DENY` leaks partial evidence** — denial response embeds redacted fragments. | Defeats the denial; reconstructable from the fragment. | `DENY` carries reason code + alternative *(if any)* — no payload. |
| **`ERROR` swallowed silently** — surface returns empty `ANSWER` on infra failure. | Caller cannot distinguish "no evidence" from "infra broken". | `ERROR` is a first-class outcome; surface returns it explicitly. |

[↑ Back to top](#top)

---

## 9. Open questions

| ID | Question | Class |
|---|---|---|
| FO-Q1 | Should `STALE` become a distinct outcome instead of folding into `ABSTAIN`? *(See [README §15](./README.md#15-open-questions-and-adr-triggers).)* | Vocabulary |
| FO-Q2 | Is `HOLD` an outcome **and** a review state *(both currently)*, or should one collapse into the other? | Vocabulary / collision |
| FO-Q3 | Should `DENY` carry an `obligations[]` array *(e.g., "redirect to non-restricted alternative")*? | Contract shape |
| FO-Q4 | Are reason codes versioned independently of the envelope schema? | Contract evolution |
| FO-Q5 | Should validator-class `PASS`/`FAIL` envelopes ride the same schema as public-class outcomes or stay separate? | Schema home |

[↑ Back to top](#top)

---

## 10. Cross-references

- [`docs/focus-mode/state/README.md`](./README.md) — state-doctrine landing.
- [`docs/focus-mode/state/lifecycle-states.md`](./lifecycle-states.md) — RAW → PUBLISHED pipeline gates.
- [`docs/focus-mode/state/review-state.md`](./review-state.md) — `ReviewRecord` lifecycle and `HOLD` review semantics.
- [`docs/focus-mode/state/payload-state.md`](./payload-state.md) — `FocusModePayload` freshness states that drive `ABSTAIN` reasons.
- [`docs/focus-mode/state/transitions/answer-to-abstain.md`](./transitions/answer-to-abstain.md) — demotion path on staleness, revocation, or closure failure.
- [`docs/focus-mode/state/transitions/hold-to-deny.md`](./transitions/hold-to-deny.md) — `HOLD` → `DENY` transition when review resolves to refusal.
- `schemas/contracts/v1/runtime/decision_envelope.schema.json` *(PROPOSED)*.
- `schemas/contracts/v1/runtime/ai_receipt.schema.json` *(PROPOSED)*.
- `contracts/focus_mode/focus_mode_payload.md` *(PROPOSED)*.
- `kfm_unified_doctrine_synthesis.md` §11 — finite outcome envelope vocabulary.
- `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md` §24.3 — Master Decision Outcome Envelope Reference.

---

**Last updated:** 2026-05-24 · **Doc version:** v0.1 · **Doc status:** draft · **Path status:** PROPOSED *(OPEN-DR-09)*

[↑ Back to top](#top)
