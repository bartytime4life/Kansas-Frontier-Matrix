<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture-governed-api-error-codes
title: Governed API — Error Codes
type: architecture-standard
version: v0.2
status: draft; repository-grounded; vocabulary-unratified; compatibility-conflicted; non-authoritative
maturity: bounded ERROR scaffold; no accepted public reason-code registry
owners:
  - "@bartytime4life — verified CODEOWNERS review route"
  - "NEEDS VERIFICATION — governed API maintainer"
  - "NEEDS VERIFICATION — runtime, contract, schema, policy, security, client, and release reviewers"
created: 2026-05-24
updated: 2026-08-19
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
current_path: docs/architecture/governed-api/ERROR_CODES.md
responsibility: "Explain current error-code evidence, preserve the v0.1 catalogue as proposal lineage, and define the evidence required before a registry becomes stable client behavior."
authority_limit: "This document does not define machine shape, activate a registry or HTTP binding, configure retry behavior, execute policy, deploy a service, or publish a claim."
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  authoring_base_commit: 0a547c12e7965565d397fcad46d94c1c7b41f0c7
  reconciled_main_commit: e13f99b623e53d710d64dc2328eeb1471abf7f84
  target_prior_blob: ae59686dfea140866e9b6194bb9964ade629e020
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  envelopes_doc_blob: 4c80f1d1808d5bed8f56bc2fd1fb73222d65ee42
  threat_model_blob: 583db17425073995b25828818ef63b4cc7d1db73
  lifecycle_gates_blob: 29b5a82fc058c7eb66228c77edf9a9a9f4d567ee
  deployment_rules_blob: 863ce5b35138f3f8a817bbe85a89a923892215e5
  runtime_response_schema_blob: 8b86e7db8b18b65a56a4e639dfc54e1b2db93155
  runtime_response_builder_blob: 5dacededc1bda64292259ba39b6387facafbd1e8
  runtime_response_validator_blob: 44ce7d51038a9adf9fcbdb18108cc27da8381e33
  governed_api_main_blob: 4eb335c7c0b27f62c7419c478542e8fe40e1ff38
  governed_api_stub_blob: 371e60d9f96c78e31c8a1e6109d19dee5da4213b
  governed_api_route_test_blob: 2be20f5d93c03da7677c34b11a31875a00b2ed28
  governed_api_boundary_test_blob: 4035e537e6c52194928df5ab8ceb41a35f5f30ca
  runtime_http_binding_blob: bccf51983d1818e74528b83d1f8f425488608d1e
inspection_boundary: >-
  Current-session GitHub reads covered the complete prior page, accepted Directory
  Rules, the grounded ENVELOPES, THREAT_MODEL, LIFECYCLE_GATES, and
  DEPLOYMENT_RULES companions, RuntimeResponseEnvelope contract and schema,
  candidate builder, validator, fixtures, WSGI dispatcher, stub builder, route
  tests, boundary tests, inactive HTTP binding, open overlap, and post-authoring
  main advancement. No mounted checkout, deployed service, browser client, live
  dependency, identity provider, policy evaluator, receipt sink, or operational
  log was used.
related:
  - README.md
  - ENVELOPES.md
  - AUDIENCE_CLASSES.md
  - THREAT_MODEL.md
  - LIFECYCLE_GATES.md
  - DEPLOYMENT_RULES.md
  - ../../../contracts/runtime/runtime_response_envelope.md
  - ../../../contracts/runtime/runtime_response_http_binding_v1.md
  - ../../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../../packages/envelopes/src/envelopes/runtime_response.py
  - ../../../tools/validators/validate_runtime_response_envelope.py
  - ../../../apps/governed-api/src/governed_api/main.py
  - ../../../apps/governed-api/src/governed_api/stub.py
  - ../../../apps/governed-api/tests/test_boundary_guards.py
tags: [kfm, architecture, governed-api, error-codes, reason-codes, finite-outcomes, compatibility, repository-grounded]
notes:
  - "The current wire profile has a top-level reason_code string and no nested reason object."
  - "The current app emits ERROR / SAFE_RUNTIME_ERROR for unknown routes and unsupported methods."
  - "All nine v0.1 classes and 33 error/<class>/<detail> identifiers remain proposal lineage, not an accepted enum."
  - "This documentation-only change has no runtime, release, deployment, or publication effect."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed API — Error Codes

> **Operating boundary.** KFM has a finite `ERROR` outcome and a bounded
> fail-closed scaffold. It does **not** yet have an accepted public
> error-code registry. The current app emits `SAFE_RUNTIME_ERROR`; the v0.1
> `error/<class>/<detail>` catalogue remains proposal lineage.

[![status](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status-and-authority)
[![placement](https://img.shields.io/badge/path-confirmed-0969da?style=flat-square)](#directory-rules-basis)
[![current code](https://img.shields.io/badge/current%20ERROR-SAFE__RUNTIME__ERROR-2da44e?style=flat-square)](#current-runtime-boundary)
[![registry](https://img.shields.io/badge/registry-not%20adopted-b42318?style=flat-square)](#13-stability-discipline)
[![publisher](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#status-and-authority)

> [!IMPORTANT]
> **The current machine profile uses a top-level `reason_code` string.** It
> does not define the v0.1 nested `reason` object, `severity`, `retryable`,
> `retry_after_seconds`, `correlation_id`, `human_hint`, `trace`, or a
> slash-namespace pattern.

> [!CAUTION]
> **HTTP status, finite outcome, reason code, response identity, and internal
> diagnostics are separate channels.** None alone proves evidence, policy,
> release state, resource existence, or retry safety.

> [!WARNING]
> **Do not treat the v0.1 catalogue as deployed behavior.** Its nine classes
> and 33 slash-namespaced codes are not constrained by the current
> RuntimeResponseEnvelope schema or emitted by the inspected app.

**Quick navigation:** [Status](#status-and-authority) · [Scope](#1-scope) ·
[Shape](#2-code-shape) · [Classes](#3-classes--at-a-glance) ·
[`schema`](#4-class--errorschema) · [`rate`](#5-class--errorrate) ·
[`upstream`](#6-class--errorupstream) · [`internal`](#7-class--errorinternal) ·
[`timeout`](#8-class--errortimeout) · [`storage`](#9-class--errorstorage) ·
[`adapter`](#10-class--erroradapter) · [`audit`](#11-class--erroraudit) ·
[`contract`](#12-class--errorcontract) · [Stability](#13-stability-discipline) ·
[Anti-patterns](#14-anti-patterns) ·
[Decisions](#15-open-questions-and-adr-triggers) · [Related](#16-related-docs) ·
[Appendix](#17-appendix)

---

<a id="status-and-authority"></a>

## Status and authority

| Question | Current evidence-backed answer |
|---|---|
| Is this a tracked architecture document? | **CONFIRMED.** The existing path is under `docs/architecture/governed-api/`. |
| Is placement still merely proposed? | **No.** Accepted ADR-0029 adopts Directory Rules v2; this same-path human documentation update receives `PLACE`. |
| Is this page the semantic or machine registry? | **No.** It explains evidence and preserves lineage. |
| Does RuntimeResponseEnvelope support `ERROR`? | **CONFIRMED / proposed profile.** Its finite outcomes are `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`. |
| Is `reason_code` constrained to a registry? | **No.** The current schema declares a string only. |
| Does the current app emit ERROR? | **CONFIRMED bounded.** Its 404 and 405 paths emit `SAFE_RUNTIME_ERROR`. |
| Are the v0.1 slash codes current? | **Not established.** They remain `PROPOSED_LINEAGE`. |
| Is retryability or severity current wire behavior? | **No.** Those fields are absent from the current schema. |
| Is the separate HTTP binding active? | **No.** It is `PROPOSED_INACTIVE` and fixture-oriented. |
| Did adjacent Governed API docs advance during authoring? | **CONFIRMED.** `THREAT_MODEL.md`, `LIFECYCLE_GATES.md`, and `DEPLOYMENT_RULES.md` were grounded on main; the target and runtime-envelope implementation evidence were unchanged. |

<a id="directory-rules-basis"></a>

### Directory Rules basis

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts [Directory Rules](../../doctrine/directory-rules.md).

| Responsibility | Owning surface |
|---|---|
| Human explanation | `docs/architecture/governed-api/` |
| Meaning and compatibility | `contracts/` |
| Machine grammar | `schemas/` |
| Runtime selection | `apps/`, `packages/`, and `policy/` |
| HTTP behavior | Active profile, route implementation, and tests |
| Client compatibility | Client code and focused tests |
| Operational detail | Authorized runtime, observability, receipt, and incident surfaces |
| Release, correction, and rollback | Their distinct governed object families and state-transition surfaces |

[Back to top](#top)

---

<a id="1-scope"></a>

## 1. Scope

This page records:

1. the current `reason_code` shape;
2. the current app's bounded ERROR behavior;
3. the complete v0.1 catalogue as proposal lineage;
4. minimum safety rules before registry adoption;
5. open compatibility decisions and graduation evidence.

This page does **not** change contracts, schemas, policy, fixtures, validators,
tests, code, routes, clients, HTTP behavior, release state, deployment, or
publication.

### 1.1 Authority order

| Claim | Controlling evidence |
|---|---|
| Outcome meaning | [`RuntimeResponseEnvelope` contract](../../../contracts/runtime/runtime_response_envelope.md) |
| Valid members | [RuntimeResponseEnvelope schema](../../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json) |
| Current app output | Pinned app code and app-local tests |
| Builder rejection | Pinned package implementation and tests |
| Public/stable code | Future adopted registry/profile plus client compatibility proof |
| Retry safety | Operation idempotency, transport profile, runtime behavior, and tests |
| Public detail | Threat, privacy, sensitivity, audience, and anti-enumeration review |
| Release eligibility | Evidence, policy, review, release, correction, and rollback records |

### 1.2 Evidence boundary

**CONFIRMED:** current scaffold routes, 404/405 behavior, exact response-field
tests, current schema, candidate builder, validator, fixtures, inactive HTTP
profile, and grounded adjacent architecture boundaries.

**UNKNOWN / not proved:** production registry, public-client fallback, rate
limiting, live dependencies, storage, provider adapters, audit persistence,
global exception handling, deployment, or incidents.

[Back to top](#top)

---

<a id="2-code-shape"></a>

## 2. Code shape

### 2.1 Current field

The complete closed RuntimeResponseEnvelope includes ten unconditional required
fields:

```text
id · spec_hash · version · issued_at · outcome · reason_code
evidence_refs · policy_state · freshness · correction_state
```

The current schema rule is:

```json
"reason_code": { "type": "string" }
```

It does not define a pattern, enum, outcome pairing, retry rule, severity,
deprecation, or client fallback. The candidate builder adds a bounded
non-empty-string check; that is not a global registry.

<a id="current-runtime-boundary"></a>

### 2.2 Current runtime matrix

| Request condition | HTTP | Outcome | `reason_code` | Envelope `id` |
|---|---:|---|---|---|
| `GET /bootstrap` | `200` | `ABSTAIN` | `NOT_IMPLEMENTED` | `stub:bootstrap` |
| `GET /layers` | `200` | `ABSTAIN` | `NOT_IMPLEMENTED` | `stub:layers` |
| `GET /evidence` | `200` | `ABSTAIN` | `NOT_IMPLEMENTED` | `stub:evidence` |
| Unknown path | `404` | `ERROR` | `SAFE_RUNTIME_ERROR` | `stub:error:route-not-found` |
| Unsupported method | `405` | `ERROR` | `SAFE_RUNTIME_ERROR` | `stub:error:method-not-allowed` |

The current app exposes one coarse ERROR reason while retaining a bounded
distinction in response identity. That is executable scaffold behavior, not an
accepted public taxonomy.

### 2.3 Channels that remain separate

| Channel | Current purpose | Must not be inferred |
|---|---|---|
| HTTP status | Transport result | KFM truth, policy verdict, evidence state, or retry safety |
| `outcome` | Finite response posture | Detailed root cause or HTTP mapping |
| `reason_code` | Safe high-level discriminator | Internal diagnostic, evidence, or policy proof |
| Envelope `id` | Response identity | Public registry or authorization fact |
| `policy_state` | Envelope posture string | Proof that a policy engine ran |
| `freshness` | Envelope posture string | Source-currentness proof |
| `correction_state` | Envelope posture string | CorrectionNotice, WithdrawalNotice, or RollbackCard |
| Logs, receipts, incidents | Authorized operational detail | A field to expose automatically on the public wire |

### 2.4 Prior nested proposal

v0.1 proposed:

```text
reason.reason_code · reason.severity · reason.retryable
reason.retry_after_seconds · reason.correlation_id · reason.human_hint
```

**Disposition:** `PROPOSED_LINEAGE / incompatible with the current closed
profile`. A future version must coordinate contract, schema, validator, runtime,
client, disclosure, migration, and rollback.

### 2.5 Repository-present literals

| Literal | Surface | Status |
|---|---|---|
| `OK` | Valid synthetic ANSWER fixture | Fixture example |
| `NOT_IMPLEMENTED` | Current ABSTAIN stubs and fixture | Executable scaffold literal |
| `ACCESS_DENIED` | Valid synthetic DENY fixture | Fixture example |
| `SAFE_RUNTIME_ERROR` | Current 404/405 stubs and fixture | Executable coarse ERROR literal |
| Builder and validator findings | Local rejection/validation | Not public registry adoption |

[Back to top](#top)

---

<a id="3-classes--at-a-glance"></a>

## 3. Classes — at-a-glance

All nine v0.1 classes and 33 v0.1 codes are retained as
`PROPOSED_LINEAGE`.

| Legacy class | Intended concern | Current proof gap |
|---|---|---|
| `error/schema` | Request/response shape | No app mapping from request/version/size failures |
| `error/rate` | Quota exhaustion | No inspected limiter or retry profile |
| `error/upstream` | Required dependency failure | Current routes use local stubs |
| `error/internal` | Internal runtime failure | Current app has only coarse 404/405 ERROR handling |
| `error/timeout` | Budget exhaustion | No inspected route budgets |
| `error/storage` | Content/receipt store failure | No inspected app store access |
| `error/adapter` | Provider/runtime adapter failure | No provider call in current routes |
| `error/audit` | Required audit artifact failure | No inspected durable audit sink |
| `error/contract` | Invariant or profile failure | Current findings are local validator/builder output |

A class name does not decide whether the finite outcome is `ABSTAIN`, `DENY`,
or `ERROR`.

[Back to top](#top)

---

<a id="4-class--errorschema"></a>

## 4. Class — `error/schema`

| Proposed code | Legacy meaning | Current status |
|---|---|---|
| `error/schema/invalid-request` | Inbound request fails schema | `PROPOSED_LINEAGE` |
| `error/schema/invalid-response` | Outbound response fails schema | `PROPOSED_LINEAGE`; tests reject invalid output but emit no such code |
| `error/schema/unknown-version` | Unsupported contract version | `PROPOSED_LINEAGE` |
| `error/schema/oversized-payload` | Input exceeds size cap | `PROPOSED_LINEAGE` |

Current builder/validator findings such as `FIELD_INVALID` and
`SCHEMA_INVALID` are local diagnostics, not automatic wire codes.

**Graduation:** define request boundaries, safe disclosure, HTTP/outcome
mapping, schema enforcement, version negotiation, size accounting, client
fallback, and rollback.

[Back to top](#top)

---

<a id="5-class--errorrate"></a>

## 5. Class — `error/rate`

| Proposed code | Legacy meaning | Current status |
|---|---|---|
| `error/rate/exhausted` | Sustained budget exhausted | `PROPOSED_LINEAGE` |
| `error/rate/burst-exhausted` | Burst budget exhausted | `PROPOSED_LINEAGE` |
| `error/rate/global-cap` | Service-wide cap reached | `PROPOSED_LINEAGE` |

No inspected surface proves caller identity, canonical audience classes,
quotas, `Retry-After`, counters, or idempotency.

**HOLD:** do not promise retry until operation-specific idempotency and
transport behavior are proved.

[Back to top](#top)

---

<a id="6-class--errorupstream"></a>

## 6. Class — `error/upstream`

| Proposed code | Legacy meaning | Current status |
|---|---|---|
| `error/upstream/release-manifest-unavailable` | Release manifest dependency unavailable | `PROPOSED_LINEAGE` |
| `error/upstream/evidence-resolver-unavailable` | Evidence resolver unavailable | `PROPOSED_LINEAGE`; `/evidence` is a stub |
| `error/upstream/policy-bundle-unavailable` | Policy dependency unavailable | `PROPOSED_LINEAGE` |
| `error/upstream/dependency-degraded` | Required dependency degraded | `PROPOSED_LINEAGE` |

Future handling must not reveal protected topology, imply that a protected
resource exists, or fall back to internal, privileged, unreleased, or
model-only material.

[Back to top](#top)

---

<a id="7-class--errorinternal"></a>

## 7. Class — `error/internal`

| Proposed code | Legacy meaning | Current status |
|---|---|---|
| `error/internal/unhandled` | Safely caught unclassified exception | `PROPOSED_LINEAGE`; no global wrapper established |
| `error/internal/inconsistency` | Runtime inconsistency | `PROPOSED_LINEAGE` |
| `error/internal/feature-disabled` | Capability disabled | `PROPOSED_LINEAGE` |

Current executable ERROR behavior is the coarse literal `SAFE_RUNTIME_ERROR`
for 404 and 405. Response identity distinguishes the two conditions. This does
not prove a general exception fallback.

A future fallback must remain non-leaky, must not imply requested facts are
false, and must not authorize a less-governed content path.

[Back to top](#top)

---

<a id="8-class--errortimeout"></a>

## 8. Class — `error/timeout`

| Proposed code | Legacy meaning | Current status |
|---|---|---|
| `error/timeout/resolver` | Resolver budget exceeded | `PROPOSED_LINEAGE` |
| `error/timeout/policy` | Policy budget exceeded | `PROPOSED_LINEAGE` |
| `error/timeout/adapter` | Adapter budget exceeded | `PROPOSED_LINEAGE` |
| `error/timeout/citation` | Citation budget exceeded | `PROPOSED_LINEAGE` |

A timeout may require `ABSTAIN`, `DENY`, or `ERROR` depending on the
operation. Define budgets, cancellation, cleanup, idempotency, client behavior,
and test clocks before adoption.

[Back to top](#top)

---

<a id="9-class--errorstorage"></a>

## 9. Class — `error/storage`

| Proposed code | Legacy meaning | Current status |
|---|---|---|
| `error/storage/receipts-write-failed` | Required receipt cannot be written | `PROPOSED_LINEAGE`; no app receipt write proved |
| `error/storage/content-unavailable` | Released content unavailable | `PROPOSED_LINEAGE` |
| `error/storage/integrity-mismatch` | Content digest mismatch | `PROPOSED_LINEAGE` |

A storage code is not a receipt, proof, release decision, correction record,
or rollback record. The v0.1 claim that all receipt-write failures refuse
responses remains proposed, not current behavior.

[Back to top](#top)

---

<a id="10-class--erroradapter"></a>

## 10. Class — `error/adapter`

| Proposed code | Legacy meaning | Current status |
|---|---|---|
| `error/adapter/provider-failure` | Provider returned failure | `PROPOSED_LINEAGE` |
| `error/adapter/sanitizer-failed` | Provider output rejected | `PROPOSED_LINEAGE` |
| `error/adapter/secret-missing` | Required runtime credential unavailable | `PROPOSED_LINEAGE` |
| `error/adapter/sdk-bypass-detected` | Governed adapter boundary bypassed | `PROPOSED_LINEAGE` as wire code; current import guard is a test concern |

Build-time boundary violations, runtime provider failures, governance
admission, and outward response codes are different surfaces.

[Back to top](#top)

---

<a id="11-class--erroraudit"></a>

## 11. Class — `error/audit`

| Proposed code | Legacy meaning | Current status |
|---|---|---|
| `error/audit/missing-policy-receipt` | Policy receipt unavailable | `PROPOSED_LINEAGE` |
| `error/audit/missing-citation-report` | Citation report unavailable | `PROPOSED_LINEAGE` |
| `error/audit/missing-ai-receipt` | AI receipt unavailable | `PROPOSED_LINEAGE` |
| `error/audit/pii-in-receipt` | Receipt redaction rejected content | `PROPOSED_LINEAGE` |

A reason code does not prove the required artifact, write attempt, response
refusal, review, incident, correction, or rollback. Those require separate
governed records.

[Back to top](#top)

---

<a id="12-class--errorcontract"></a>

## 12. Class — `error/contract`

| Proposed code | Legacy meaning | Current status |
|---|---|---|
| `error/contract/envelope-malformed` | Envelope profile violation | `PROPOSED_LINEAGE` |
| `error/contract/invariant-violation` | Cross-field/lane invariant violation | `PROPOSED_LINEAGE` |
| `error/contract/receipt-shape-invalid` | Receipt profile violation | `PROPOSED_LINEAGE` |
| `error/contract/spec-hash-mismatch` | Spec pin mismatch | `PROPOSED_LINEAGE`; current `spec_hash` is top-level |

Local findings including `PRECISION_INTERVAL_INVERTED`,
`GENERALIZATION_RECEIPT_REQUIRED`, and `SCHEMA_INVALID` must not become public
wire codes without a reviewed safe translation.

[Back to top](#top)

---

<a id="13-stability-discipline"></a>

## 13. Stability discipline

**Current status:** no accepted registry or versioning guarantee was
established.

Before declaring codes stable, a reviewed profile must define:

| Requirement | Needed decision |
|---|---|
| Authority | One contract/schema registry home |
| Grammar | Upper snake, slash namespace, or another bounded form |
| Outcome compatibility | Allowed code/outcome pairs |
| Disclosure | Public-safe versus restricted detail |
| HTTP binding | Active status/outcome/code mapping |
| Retry | Idempotency, delay source, attempts, and cancellation |
| Unknown codes | Generic safe client fallback |
| Versioning | Add, deprecate, replace, retire, and mixed versions |
| Enforcement | Schema, semantic validator, runtime, and client tests |
| Correction and rollback | Alias window, revert target, and public correction behavior |

Until then, clients should trust `outcome` over the code text, show a generic
safe state, avoid guessing retry or policy, and never fall back to
less-governed content.

[Back to top](#top)

---

<a id="14-anti-patterns"></a>

## 14. Anti-patterns

| Anti-pattern | Correction |
|---|---|
| Treating v0.1 codes as current | Mark them `PROPOSED_LINEAGE`; cite runtime evidence |
| Adding nested reason fields to the current closed schema | Version the contract/schema first |
| Inferring outcome from HTTP alone | Validate the envelope outcome |
| Inferring evidence or policy from a code | Resolve the governing objects |
| Returning internal diagnostic text on the public wire | Use a coarse safe reason and restricted operational detail |
| Converting validator findings directly to public codes | Add a reviewed translation |
| Marking all transient failures retryable | Prove idempotency and backoff |
| Retrying mutations on generic ERROR | Require operation-specific replay controls |
| Returning detail that reveals a protected resource exists | Use non-enumerating fail-closed behavior |
| Crashing on unknown codes | Render a generic safe state |
| Falling back to internal, privileged, withdrawn, or model-only content | Fail closed |
| Treating a fixture, receipt, PR, merge, release, or deployment as registry adoption | Keep governance transitions separate |
| Removing old identifiers without lineage | Record supersession and rollback |

[Back to top](#top)

---

<a id="15-open-questions-and-adr-triggers"></a>

## 15. Open questions and ADR triggers

| ID | Decision | Status |
|---|---|---|
| `ERR-01` | Canonical registry authority | `UNKNOWN` |
| `ERR-02` | Upper-snake versus lower-case slash grammar | `CONFLICTED` |
| `ERR-03` | Schema-level non-empty and pattern rule | `NEEDS VERIFICATION` |
| `ERR-04` | Top-level code versus nested reason object | `HOLD` |
| `ERR-05` | Public versus restricted severity, retry, hint, and correlation | `UNKNOWN` |
| `ERR-06` | Separate 404 and 405 public codes | `PROPOSED decision` |
| `ERR-07` | Active HTTP/outcome mapping | `CONFLICTED / inactive profile` |
| `ERR-08` | Code-to-outcome compatibility | `UNKNOWN` |
| `ERR-09` | Unknown/deprecated code behavior | `UNKNOWN` |
| `ERR-10` | Retry and idempotency rules | `UNKNOWN` |
| `ERR-11` | Registry version binding and deprecation window | `UNKNOWN` |
| `ERR-12` | Adopt, narrow, replace, or retire the v0.1 catalogue | `PROPOSED_LINEAGE` |

### 15.1 Smallest graduation slice

A future no-network slice could:

1. choose one registry authority and version;
2. constrain `reason_code` grammar without adding a nested reason object;
3. define only the already executable `NOT_IMPLEMENTED` and
   `SAFE_RUNTIME_ERROR` literals, or explicitly version replacements;
4. bind allowed outcome/code pairs;
5. add positive and negative fixtures;
6. test unknown-code client behavior, 404/405 non-leakage, and no-detail
   exposure;
7. activate the HTTP binding only after implementation parity; and
8. preserve rollback to the current coarse literals.

Rate, upstream, storage, adapter, audit, and richer internal classes remain
held until their dependencies exist. This page does not implement the slice.

[Back to top](#top)

---

<a id="16-related-docs"></a>

## 16. Related docs

| Reference | Role | Posture |
|---|---|---|
| [`README.md`](README.md) | Governed API architecture boundary | Repository-grounded guidance |
| [`ENVELOPES.md`](ENVELOPES.md) | Current envelope profiles and reason conflict | Repository-grounded guidance |
| [`AUDIENCE_CLASSES.md`](AUDIENCE_CLASSES.md) | Audience/auth/capability boundary | Repository-grounded guidance |
| [`THREAT_MODEL.md`](THREAT_MODEL.md) | Current scaffold safeguards and held threat boundaries | Repository-grounded guidance |
| [`LIFECYCLE_GATES.md`](LIFECYCLE_GATES.md) | Current readiness evidence and request-time transition HOLDs | Repository-grounded guidance |
| [`DEPLOYMENT_RULES.md`](DEPLOYMENT_RULES.md) | Deployment preparation and operational-proof boundary | Repository-grounded guidance |
| [RuntimeResponseEnvelope contract](../../../contracts/runtime/runtime_response_envelope.md) | Semantic profile | Draft / proposed |
| [RuntimeResponseEnvelope schema](../../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json) | Machine shape | Draft / proposed |
| [HTTP binding profile](../../../contracts/runtime/runtime_response_http_binding_v1.md) | Proposed status/outcome mapping | `PROPOSED_INACTIVE` |
| [Candidate builder](../../../packages/envelopes/src/envelopes/runtime_response.py) | Local deterministic construction | Bounded executable |
| [Envelope validator](../../../tools/validators/validate_runtime_response_envelope.py) | Local conformance | Bounded executable |
| [Dispatcher](../../../apps/governed-api/src/governed_api/main.py) | Current HTTP behavior | Executable scaffold |
| [Stub builder](../../../apps/governed-api/src/governed_api/stub.py) | Current literals and fields | Executable scaffold |
| [Boundary tests](../../../apps/governed-api/tests/test_boundary_guards.py) | 404/405 and no-detail checks | Bounded proof |
| [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Placement authority | Accepted |
| [Directory Rules](../../doctrine/directory-rules.md) | Responsibility boundaries | Adopted through ADR-0029 |

[Back to top](#top)

---

<a id="17-appendix"></a>

## 17. Appendix

### 17.1 Current executable quick reference

```text
GET /bootstrap   -> 200 -> ABSTAIN -> NOT_IMPLEMENTED
GET /layers      -> 200 -> ABSTAIN -> NOT_IMPLEMENTED
GET /evidence    -> 200 -> ABSTAIN -> NOT_IMPLEMENTED
unknown path     -> 404 -> ERROR   -> SAFE_RUNTIME_ERROR
unsupported verb -> 405 -> ERROR   -> SAFE_RUNTIME_ERROR
```

### 17.2 Full v0.1 catalogue retained without adoption

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

Count check:

```text
schema 4 + rate 3 + upstream 4 + internal 3 + timeout 4
+ storage 3 + adapter 4 + audit 4 + contract 4 = 33
```

Every identifier above is `PROPOSED_LINEAGE`.

### 17.3 Minimum graduation tests

| Case | Required result |
|---|---|
| Known compatible code | Schema, runtime, and client agree |
| Incompatible code/outcome | Rejected |
| Unknown future code | Generic safe client state |
| Nested reason on current profile | Rejected |
| Internal detail in outward response | Rejected |
| 404/405 behavior | Tested without unsafe enumeration |
| Retry | Allowed only with idempotency proof |
| Registry rollback | Older clients handle newer unknown codes |
| No-network fixtures | Deterministic positive and negative coverage |

### 17.4 No-loss ledger

| v0.1 surface | v0.2 disposition |
|---|---|
| Path marked proposed | Corrected to confirmed same-path docs placement |
| Canonical public vocabulary claim | Corrected to non-authoritative, unratified guidance |
| Nested reason shape | Retained as incompatible proposal lineage |
| Nine classes and 33 codes | Retained in full as proposal lineage |
| Retry/severity guarantees | Held pending implementation and client proof |
| `error/internal/unhandled` fallback | Corrected to current coarse 404/405 behavior |
| Validator findings | Separated from wire reasons |
| Stability guarantee | Held until registry adoption |
| Adjacent docs advanced during authoring | Re-read and reconciled before final exact-head delivery |
| Rollback | Prior blob retained below |

### 17.5 Rollback

Prior target blob:

```text
ae59686dfea140866e9b6194bb9964ade629e020
```

Before merge, close the draft PR and delete the feature branch. After an
authorized merge, revert the documentation commit and remove or supersede its
generated authoring receipt. No service, release, deployment, or public state
changes.

---

**Last updated:** 2026-08-19 · **Version:** v0.2 ·
**Status:** repository-grounded draft · **Registry:** not adopted

[Back to top](#top)
