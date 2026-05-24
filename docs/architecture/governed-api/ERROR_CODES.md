<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture-governed-api-error-codes
title: Governed API — Error Codes
type: standard
version: v0.1
status: draft
owners: API steward + Security steward · NEEDS VERIFICATION
created: 2026-05-24
updated: 2026-05-24
policy_label: public
related:
  - README.md
  - ../governed-api.md
  - ENVELOPES.md
  - THREAT_MODEL.md
  - LIFECYCLE_GATES.md
  - AUDIENCE_CLASSES.md
  - DEPLOYMENT_RULES.md
tags: [kfm, architecture, governed-api, error-codes, vocabulary, doctrine]
notes:
  - PROPOSED. Canonical vocabulary for the ERROR outcome of RuntimeResponseEnvelope.
  - Codes are part of the public contract — adding, renaming, or retiring is schema-evolution discipline.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed API — Error Codes

> *The canonical vocabulary for the `ERROR` outcome of `RuntimeResponseEnvelope`. Stable, namespaced, audit-grade. Adding, renaming, or retiring a code is a schema-evolution event.*

![status](https://img.shields.io/badge/status-draft-yellow)
![doctrine](https://img.shields.io/badge/doctrine-PROPOSED%20(vocabulary)-blue)
![path-status](https://img.shields.io/badge/path-PROPOSED-orange)
![namespaces](https://img.shields.io/badge/namespaces-9-blue)

**Status:** draft · **Owners:** API steward + Security steward *(NEEDS VERIFICATION)* · **Last updated:** 2026-05-24

> [!IMPORTANT]
> **`ERROR` is a finite outcome, not a free-text bucket.** It carries a stable `reason.reason_code` of the form `error/<class>/<detail>`. Clients react on the code; humans read the operations log. No PII, no policy internals, no stack traces in the code or the reason envelope.

> [!NOTE]
> **This doc enumerates the `error/*` namespace.** Reason codes in other namespaces *(`evidence/*`, `release/*`, `policy/*`, `auth/*`, `rate/*`, `schema/*`, `adapter/*`, `ai/*`)* are listed in `ENVELOPES.md` §6 and are used by `ABSTAIN` / `DENY`; this doc focuses on `ERROR` codes.

---

## Table of contents

1. [Scope](#1-scope)
2. [Code shape](#2-code-shape)
3. [Classes — at-a-glance](#3-classes--ataglance)
4. [Class — `error/schema`](#4-class--errorschema)
5. [Class — `error/rate`](#5-class--errorrate)
6. [Class — `error/upstream`](#6-class--errorupstream)
7. [Class — `error/internal`](#7-class--errorinternal)
8. [Class — `error/timeout`](#8-class--errortimeout)
9. [Class — `error/storage`](#9-class--errorstorage)
10. [Class — `error/adapter`](#10-class--erroradapter)
11. [Class — `error/audit`](#11-class--erroraudit)
12. [Class — `error/contract`](#12-class--errorcontract)
13. [Stability discipline](#13-stability-discipline)
14. [Anti-patterns](#14-anti-patterns)
15. [Open questions and ADR triggers](#15-open-questions-and-adr-triggers)
16. [Related docs](#16-related-docs)
17. [Appendix](#17-appendix)

---

## 1. Scope

This doc enumerates the canonical `error/<class>/<detail>` codes the governed API emits, lists what each code means, and tells implementers what shape the `reason` envelope takes.

> [!TIP]
> **When this doc binds.** Designing or reviewing a route's error paths, building a client that reacts on error codes, or adding a new error class.

[↑ Back to top](#top)

---

## 2. Code shape

| Field | Form | Example |
|---|---|---|
| Code | `error/<class>/<detail>` *(slash-separated)* | `error/schema/invalid-response` |
| Class | Lowercase, one of the canonical nine *(§3)* | `schema` |
| Detail | Lowercase, kebab-case, ≤32 chars | `invalid-response` |
| Stability | Stable across schema-versions; deprecation discipline in [§13](#13-stability-discipline). | — |

**`reason` envelope shape *(inside `RuntimeResponseEnvelope.reason`)*:**

| Field | Type | Required | Meaning |
|---|---|---|---|
| `reason_code` | string `error/<class>/<detail>` | yes | Stable code. |
| `severity` | enum `info` · `warn` · `error` · `fatal` | yes | Operational severity. |
| `retryable` | boolean | yes | Whether a client may retry safely. |
| `retry_after_seconds` | integer ≥0 | conditional | Required when `retryable == true`. |
| `correlation_id` | string | yes | Matches `trace.request_id`. |
| `human_hint` | short string | optional | Brief, non-leaky hint *(e.g., "service degraded")*. Never includes stack traces or internal ids. |

> [!CAUTION]
> **`human_hint` is not a debug field.** It is a one-line, audience-safe phrase. Internal diagnostics go to `data/receipts/` and structured logs, not into the wire envelope.

[↑ Back to top](#top)

---

## 3. Classes — at-a-glance

| Class | Meaning | Retryable default |
|---|---|---|
| **`error/schema`** | Request or response violates a schema contract. | No *(client must fix payload)*. |
| **`error/rate`** | Rate limit exhausted. | Yes *(after backoff)*. |
| **`error/upstream`** | Upstream dependency *(release manifest store, evidence resolver, adapter)* failed. | Yes *(transient class)*. |
| **`error/internal`** | API internal failure not attributable to a named class. | Yes. |
| **`error/timeout`** | A dependency or step exceeded its budget. | Yes. |
| **`error/storage`** | Receipts store or content store failed. | Yes. |
| **`error/adapter`** | Runtime adapter or external provider failed. | Yes. |
| **`error/audit`** | Receipts could not be emitted; response refused. | No *(operations issue)*. |
| **`error/contract`** | A KFM contract was violated *(e.g., envelope assembly inconsistent)*. | No. |

[↑ Back to top](#top)

---

## 4. Class — `error/schema`

> Used when an inbound request or outbound response violates a JSON Schema contract.

| Code | Meaning | Severity | Retryable | Likely client action |
|---|---|---|---|---|
| `error/schema/invalid-request` | Inbound request failed schema validation. | warn | No | Fix payload shape. |
| `error/schema/invalid-response` | Outbound payload failed schema validation *(assembler refused)*. | error | No | Operations: triage schema or code. |
| `error/schema/unknown-version` | Client referenced a schema version the API does not serve. | warn | No | Use supported version. |
| `error/schema/oversized-payload` | Request body exceeded size cap. | warn | No | Reduce payload. |

[↑ Back to top](#top)

---

## 5. Class — `error/rate`

| Code | Meaning | Severity | Retryable | Notes |
|---|---|---|---|---|
| `error/rate/exhausted` | Rate limit hit for the audience class. | warn | Yes | `retry_after_seconds` required. |
| `error/rate/burst-exhausted` | Burst budget exhausted but steady-state ok. | info | Yes | Shorter `retry_after_seconds`. |
| `error/rate/global-cap` | Global API cap hit *(overload)*. | error | Yes | Coordinated retry; operations alert. |

> [!IMPORTANT]
> **`error/rate/*` is `ERROR`, not `DENY`.** A rate event is operational; a denied request *(e.g., insufficient class)* is policy. See `AUDIENCE_CLASSES.md` §9.

[↑ Back to top](#top)

---

## 6. Class — `error/upstream`

| Code | Meaning | Severity | Retryable | Notes |
|---|---|---|---|---|
| `error/upstream/release-manifest-unavailable` | Manifest store unreachable. | error | Yes | Operations: release plane investigate. |
| `error/upstream/evidence-resolver-unavailable` | Resolver unreachable. | error | Yes | — |
| `error/upstream/policy-bundle-unavailable` | Policy bundle store unreachable. | error | Yes | Fail-closed posture; no `ANSWER`. |
| `error/upstream/dependency-degraded` | A dependency reported degraded health. | warn | Yes | Backoff; observability tracks. |

[↑ Back to top](#top)

---

## 7. Class — `error/internal`

| Code | Meaning | Severity | Retryable | Notes |
|---|---|---|---|---|
| `error/internal/unhandled` | Unhandled exception; caught by envelope assembler. | error | Yes | Operations triage; stack to logs only. |
| `error/internal/inconsistency` | API observed inconsistent state *(e.g., manifest hash mismatch)*. | error | No | Operations: integrity check. |
| `error/internal/feature-disabled` | Route is feature-flagged off. | info | No | Documented when route is flagged. |

> [!CAUTION]
> **`error/internal/unhandled` is not a debug fallback.** Each occurrence is alertable; recurring instances upgrade to a named code.

[↑ Back to top](#top)

---

## 8. Class — `error/timeout`

| Code | Meaning | Severity | Retryable | Notes |
|---|---|---|---|---|
| `error/timeout/resolver` | Evidence resolver exceeded budget. | warn | Yes | — |
| `error/timeout/policy` | Policy evaluator exceeded budget. | warn | Yes | — |
| `error/timeout/adapter` | Runtime adapter exceeded budget. | warn | Yes | Operations: adapter health. |
| `error/timeout/citation` | Citation validator exceeded budget. | warn | Yes | Falls to `ABSTAIN` if budget allows partial. |

[↑ Back to top](#top)

---

## 9. Class — `error/storage`

| Code | Meaning | Severity | Retryable | Notes |
|---|---|---|---|---|
| `error/storage/receipts-write-failed` | Receipt store write failed. | error | Yes | API refuses response if receipts can't be emitted. |
| `error/storage/content-unavailable` | Released content blob unreachable. | error | Yes | Falls to `error/upstream/*` if a sibling system. |
| `error/storage/integrity-mismatch` | Content hash mismatch against manifest. | fatal | No | Operations: integrity incident. |

[↑ Back to top](#top)

---

## 10. Class — `error/adapter`

| Code | Meaning | Severity | Retryable | Notes |
|---|---|---|---|---|
| `error/adapter/provider-failure` | External provider returned error. | warn | Yes | Sanitized; no provider details on wire. |
| `error/adapter/sanitizer-failed` | Adapter sanitizer refused provider output. | error | No | Operations: sanitizer review. |
| `error/adapter/secret-missing` | Adapter could not load required secret. | error | Yes | Operations: secret rotation. |
| `error/adapter/sdk-bypass-detected` | Route attempted to import provider SDK directly *(static + runtime check)*. | fatal | No | Build / review failure. |

[↑ Back to top](#top)

---

## 11. Class — `error/audit`

| Code | Meaning | Severity | Retryable | Notes |
|---|---|---|---|---|
| `error/audit/missing-policy-receipt` | `PolicyDecision` receipt could not be emitted. | error | No | API refuses response. |
| `error/audit/missing-citation-report` | `CitationValidationReport` could not be emitted. | error | No | API refuses response. |
| `error/audit/missing-ai-receipt` | `AIReceipt` could not be emitted on an AI surface. | error | No | API refuses response. |
| `error/audit/pii-in-receipt` | PII redaction failed pre-write. | fatal | No | Operations: redaction pipeline. |

[↑ Back to top](#top)

---

## 12. Class — `error/contract`

| Code | Meaning | Severity | Retryable | Notes |
|---|---|---|---|---|
| `error/contract/envelope-malformed` | Assembler produced an envelope that fails contract checks *(e.g., `ANSWER` with empty `evidence_refs`)*. | fatal | No | Build / code defect. |
| `error/contract/invariant-violation` | A cross-lane invariant *(ownership / role / sensitivity / evidence)* was violated mid-response. | fatal | No | Operations: invariant validator. |
| `error/contract/receipt-shape-invalid` | Receipt schema validation failed at write. | error | No | Receipts pipeline issue. |
| `error/contract/spec-hash-mismatch` | `trace.spec_hash` did not match expected pin. | error | No | Build / drift investigation. |

[↑ Back to top](#top)

---

## 13. Stability discipline

| Discipline | Rule |
|---|---|
| Codes are part of the public contract | Clients react on the code; the code MUST NOT silently change meaning. |
| Adding a code | Allowed in the same schema-version; new code appears in this doc. |
| Renaming a code | Forbidden in same major version; deprecate + add new + retire. |
| Retiring a code | Mark deprecated for one major version with stable behavior; remove in the next major. |
| Changing severity | Allowed *(observability)*; not a contract change. |
| Changing retryable | Treated as a contract change; deprecate + replace. |
| Codes not in this doc | Not part of the contract; `error/internal/unhandled` is the fallback. |

> [!IMPORTANT]
> **The audit trail is the code, not the message.** When investigating a stable behavior across releases, operators search by `reason_code`, not by `human_hint`.

[↑ Back to top](#top)

---

## 14. Anti-patterns

| Anti-pattern | Mitigation |
|---|---|
| **Stack trace in `human_hint`** | Strip; trace to structured logs. |
| **Provider name / vendor id leaked in `error/adapter/*`** | Sanitize; codes describe behavior class, not vendor. |
| **`error/internal/unhandled` left in production for known issue** | Promote to a named code. |
| **Reusing an existing code with new semantics** | Deprecate + add new. |
| **Code missing `retry_after_seconds` when `retryable == true`** | Schema requires the pair. |
| **Different routes returning different codes for the same root cause** | Codes are vocabulary; routes share them. |

[↑ Back to top](#top)

---

## 15. Open questions and ADR triggers

| Open item | Class | Suggested ADR title |
|---|---|---|
| Codespace governance — single doc registry vs split per namespace? | Layout | "Error-code codespace governance". |
| Should `error/rate/*` move into `rate/*` *(its own outcome — DEGRADED?)* or stay under `error/*`? | Vocabulary | "Rate-limit outcome class". |
| Public publication of the full code list — yes or partner-only? | Disclosure | "Error-code disclosure surface". |
| Should `severity` be part of the wire envelope or derived in observability? | Envelope | "Severity in wire envelope". |
| Should `fatal` codes always carry `operations_alert: true`? | Operations | "Fatal-code alert posture". |

[↑ Back to top](#top)

---

## 16. Related docs

| Reference | Role | Truth label |
|---|---|---|
| `README.md` *(this folder)* | Landing | CONFIRMED doctrine |
| `../governed-api.md` §4, App. A | Finite-outcome contract | CONFIRMED doctrine |
| `ENVELOPES.md` §6 | Reason-code namespaces *(all)* | PROPOSED |
| `THREAT_MODEL.md` | Where each error class arises | PROPOSED |
| `LIFECYCLE_GATES.md` | Gate-D / Gate-G errors | PROPOSED |
| `AUDIENCE_CLASSES.md` §9 | Rate-class to `error/rate/*` mapping | PROPOSED |
| `DEPLOYMENT_RULES.md` | Log discipline; error redaction | PROPOSED |

[↑ Back to top](#top)

---

## 17. Appendix

<details>
<summary><strong>17.1 Code quick-reference</strong></summary>

```text
error/schema/{invalid-request, invalid-response, unknown-version, oversized-payload}
error/rate/{exhausted, burst-exhausted, global-cap}
error/upstream/{release-manifest-unavailable, evidence-resolver-unavailable,
                policy-bundle-unavailable, dependency-degraded}
error/internal/{unhandled, inconsistency, feature-disabled}
error/timeout/{resolver, policy, adapter, citation}
error/storage/{receipts-write-failed, content-unavailable, integrity-mismatch}
error/adapter/{provider-failure, sanitizer-failed, secret-missing, sdk-bypass-detected}
error/audit/{missing-policy-receipt, missing-citation-report,
             missing-ai-receipt, pii-in-receipt}
error/contract/{envelope-malformed, invariant-violation, receipt-shape-invalid,
                spec-hash-mismatch}
```

</details>

<details>
<summary><strong>17.2 Truth-label legend</strong></summary>

- **CONFIRMED** — verified this session from attached docs.
- **PROPOSED** — design / placement / inference not yet verified in implementation.
- **INFERRED** — derivable from confirmed evidence but not directly stated.
- **NEEDS VERIFICATION** — checkable, but not yet checked strongly enough to act as fact.

</details>

---

**Related (mini)** · [`README.md`](README.md) · [`../governed-api.md`](../governed-api.md) · [`ENVELOPES.md`](ENVELOPES.md) · [`THREAT_MODEL.md`](THREAT_MODEL.md) · [`LIFECYCLE_GATES.md`](LIFECYCLE_GATES.md) · [`AUDIENCE_CLASSES.md`](AUDIENCE_CLASSES.md) · [`DEPLOYMENT_RULES.md`](DEPLOYMENT_RULES.md)

**Last updated:** 2026-05-24 · **Doc version:** v0.1 · **Doc status:** draft · **Path status:** PROPOSED *(OPEN-DR-12 META)*

[↑ Back to top](#top)
