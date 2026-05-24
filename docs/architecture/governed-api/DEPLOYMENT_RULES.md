<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture-governed-api-deployment-rules
title: Governed API — Deployment Rules
type: standard
version: v0.1
status: draft
owners: API steward + Security steward + Operations steward · NEEDS VERIFICATION
created: 2026-05-24
updated: 2026-05-24
policy_label: public
related:
  - README.md
  - ../governed-api.md
  - ../deployment-topology.md
  - THREAT_MODEL.md
  - AUDIENCE_CLASSES.md
  - ENVELOPES.md
  - ERROR_CODES.md
tags: [kfm, architecture, governed-api, deployment, tls, cors, rate-limit, doctrine]
notes:
  - PROPOSED. Expands docs/architecture/governed-api.md §11.1 (deployment placement) and §11.3 (security/policy boundary summary).
  - Operational expression of the trust-membrane posture; not a substitute for the deployment-topology doc.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed API — Deployment Rules

> *The operational expression of the trust-membrane posture: TLS, CORS, rate limits, secret hygiene, log discipline, network policy, health checks, and tracing.*

![status](https://img.shields.io/badge/status-draft-yellow)
![doctrine](https://img.shields.io/badge/doctrine-CONFIRMED%20(posture)%20·%20PROPOSED%20(specifics)-blue)
![path-status](https://img.shields.io/badge/path-PROPOSED-orange)
![posture](https://img.shields.io/badge/posture-deny--by--default-success)

**Status:** draft · **Owners:** API steward + Security steward + Operations steward *(NEEDS VERIFICATION)* · **Last updated:** 2026-05-24

> [!IMPORTANT]
> **Deployment is downstream of doctrine, not upstream.** Audience class, envelope contract, lifecycle gates, and threat boundaries are decided in design *(this folder)*; deployment **realizes** those choices through TLS, CORS, rate limits, secret stores, log pipelines, and network policy. A deployment posture that contradicts doctrine is a drift event *(record in `DRIFT_REGISTER.md`)*.

> [!NOTE]
> **This doc is operational doctrine, not a runbook.** Specific provider names, IP allowlists, certificate authorities, and rotation cadences belong in operational config inside `apps/governed-api/` and in runbooks under `docs/runbooks/`. This doc names the rules; ops implements them.

---

## Table of contents

1. [Scope](#1-scope)
2. [Deployment placement](#2-deployment-placement)
3. [TLS posture](#3-tls-posture)
4. [CORS posture](#4-cors-posture)
5. [Rate limits](#5-rate-limits)
6. [Secret hygiene](#6-secret-hygiene)
7. [Log discipline](#7-log-discipline)
8. [Network policy](#8-network-policy)
9. [Health, readiness, and tracing](#9-health-readiness-and-tracing)
10. [Anti-patterns](#10-anti-patterns)
11. [Open questions and ADR triggers](#11-open-questions-and-adr-triggers)
12. [Related docs](#12-related-docs)
13. [Appendix](#13-appendix)

---

## 1. Scope

This doc names the operational rules the governed API runs under. It does not specify a cloud provider, a load balancer model, or a specific TLS library. It tells implementers what postures must hold regardless of the chosen stack.

> [!TIP]
> **When this doc binds.** Standing up the API for the first time, hardening an existing deployment, adding a new region, integrating a new provider *(model, tile, vector store)*, or auditing a deployment against doctrine.

[↑ Back to top](#top)

---

## 2. Deployment placement

> **Evidence basis:** `governed-api.md` §11.1 *(deployment placement, CONFIRMED doctrine · PROPOSED implementation)*; `directory-rules.md` §7.1.

| Question | Answer | Status |
|---|---|---|
| Where does the API live in the repo? | `apps/governed-api/` *(Directory Rules §7.1 canonical)*. | CONFIRMED doctrine · PROPOSED implementation |
| Where do runtime adapters live? | `runtime/` *(canonical)*. | CONFIRMED doctrine |
| Where does the public web client live? | `apps/explorer-web/` *(canonical)*. | CONFIRMED doctrine |
| Where does the service deploy? | A single, named environment per release channel *(dev / staging / prod)*. | PROPOSED |
| Are there per-region replicas? | If yes, all replicas serve identical envelopes; manifest pinning ensures cross-region consistency. | PROPOSED |

[↑ Back to top](#top)

---

## 3. TLS posture

| Rule | Detail |
|---|---|
| TLS-only at ingress | Plaintext HTTP refused at the edge; ingress redirects 80 → 443. |
| Modern protocols | TLS 1.3 preferred; TLS 1.2 allowed only with PFS ciphersuites; TLS ≤1.1 refused. |
| Certificate management | Automated rotation; no manual certs in source control; CT logging enforced. |
| HSTS | `Strict-Transport-Security` with a long max-age and `includeSubDomains`. *(Whether `preload` is set is an open ADR.)* |
| OCSP stapling | Enabled when supported by the edge. |
| Mutual TLS | Required for `internal` audience class *(`AUDIENCE_CLASSES.md` §6)*. |

> [!CAUTION]
> **TLS termination location is part of the trust posture.** If a TLS-terminating proxy sits in front of the API, the proxy MUST be inside the trust boundary; otherwise plaintext travels on untrusted hops.

[↑ Back to top](#top)

---

## 4. CORS posture

| Rule | Detail |
|---|---|
| Default | Deny *(no `Access-Control-Allow-Origin` header)*. |
| Allowed origins | Explicit allowlist per audience class; `public` routes permit the canonical KFM web client origins only. |
| Allowed methods | Per route; `OPTIONS` answers preflight; no wildcard methods. |
| Allowed headers | Per route; auth headers are listed explicitly for non-`public` classes. |
| Credentials | `Access-Control-Allow-Credentials: true` only on routes that require auth; never on `public` anonymous routes. |
| Wildcard origin | Forbidden. A wildcard CORS is a public exposure event. |
| Preflight cache | Bounded *(short max-age)*; never long-lived. |

> [!IMPORTANT]
> **CORS is not a security boundary; it is a browser hint.** Auth and policy enforcement still happen at the API. CORS posture exists so a misconfigured client cannot accidentally invoke `partner` / `steward` routes from a public origin.

[↑ Back to top](#top)

---

## 5. Rate limits

> **Evidence basis:** `AUDIENCE_CLASSES.md` §9 *(tier table, PROPOSED)*; `governed-api.md` §11.3 *(security/policy boundary summary, CONFIRMED posture)*.

| Rule | Detail |
|---|---|
| Tier per class | T-PUB / T-PART / T-STEW / T-INT per `AUDIENCE_CLASSES.md` §9. |
| Scope | Per-IP for `public`; per-key for `partner`; per-user for `steward`; per-workload for `internal`. |
| Burst | Allowed within a bounded multiple of steady-state. |
| Response on exhaustion | `ERROR` envelope with `error/rate/exhausted` and `retry_after_seconds`. |
| Headers | `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `Retry-After`. |
| Global cap | Above all per-class tiers; protects against runaway aggregate load. |
| Anti-abuse | Tar-pit response *(slow `ERROR`)* for repeated abuse from the same source is acceptable; never `ANSWER` to abusive clients. |

[↑ Back to top](#top)

---

## 6. Secret hygiene

| Rule | Detail |
|---|---|
| Source of secrets | Secret manager *(provider-specific)*; never `.env` checked in. |
| Loading | At process start *(or short-lived workload identity)*; not at request time unless required for rotation. |
| Rotation | Automated; deployment continues across rotation without restart where possible. |
| Logging | Secrets never logged; redaction at the boundary; structured-log fields allowlisted. |
| Environment variables | Allowed for non-secret config; secret env vars are sourced from the secret manager at boot, not stored in deployment manifests. |
| Telemetry | Secrets never appear in events *(see [§7](#7-log-discipline))*. |
| Error envelopes | Secrets never appear in error envelopes *(see `ERROR_CODES.md` §14)*. |

> [!CAUTION]
> **A secret leaked once is a secret forever-rotated.** Treat any suspected leak as a real leak: rotate, audit, and post-mortem.

[↑ Back to top](#top)

---

## 7. Log discipline

| Rule | Detail |
|---|---|
| Structured logs only | JSON or equivalent; allowlisted fields; no free-form text dumps. |
| Severity | Aligns with `reason.severity` *(`ERROR_CODES.md` §2)*. |
| Correlation | `correlation_id` matches `trace.request_id`; every log line carries it. |
| Forbidden fields | Raw evidence, prompts, secrets, restricted coordinates, PII, internal store ids, full URLs of upstream provider calls. |
| Allowed fields | `request_id`, `route`, `audience_class`, `outcome`, `reason_code`, `policy_bundle_hash`, `release_ref` hash. |
| Retention | Bounded; older logs aggregate to summary metrics; raw logs deleted per retention policy. |
| Access | Operators only; logs are inside the membrane. |
| Sampling | Acceptable for `public`; full retention for `partner`/`steward`/`internal`. |

> [!IMPORTANT]
> **Logs are evidence too.** They are governed alongside content. A log line that would `DENY` if rendered to a user MUST NOT be retained in plaintext.

[↑ Back to top](#top)

---

## 8. Network policy

| Rule | Detail |
|---|---|
| Ingress | Only the edge ingress can reach the API; direct pod / VM access forbidden. |
| Egress | API egress allowlisted to named upstreams *(release manifest store, evidence resolver, adapter targets, telemetry sink, receipts store)*. |
| Adapter → external provider | Egress permitted from `runtime/` adapter only; never from route handlers. |
| Canonical stores | No public egress route; the API reaches them via the resolver inside the membrane. |
| Admin endpoints | If present, on a separate ingress / network segment; never advertised on the public surface *(`governed-api.md` invariant 9)*. |
| DNS posture | Resolver pinned; DNS rebinding defended at edge. |

[↑ Back to top](#top)

---

## 9. Health, readiness, and tracing

### 9.1 Health and readiness

| Endpoint | Class | Purpose |
|---|---|---|
| `/healthz` | `internal` *(operator-only)* | Process liveness. |
| `/readyz` | `internal` *(operator-only)* | All required upstreams reachable; policy bundle loaded; manifest store reachable. |
| `/metrics` | `internal` *(operator-only)* | Prometheus-style metrics; no PII; bounded cardinality. |

> [!CAUTION]
> **`/healthz` and `/readyz` are not public routes.** They never appear in the public envelope contract; they are operator-only and behind the network policy in §8.

### 9.2 Tracing

| Rule | Detail |
|---|---|
| Trace context | Standard tracing context propagated *(W3C Trace Context preferred)*. |
| Spans | One span per envelope step *(ingress, policy, release, resolver, adapter, citation, assembler, audit)*. |
| Trace ids | Match `trace.request_id` in `RuntimeResponseEnvelope`. |
| Sensitive attributes | Never as span attributes *(raw evidence, prompts, secrets, restricted coords)*. |
| Sampling | High-rate for `public`; full for `partner`/`steward`/`internal`. |

[↑ Back to top](#top)

---

## 10. Anti-patterns

| Anti-pattern | Mitigation |
|---|---|
| **Wildcard CORS** | Explicit allowlist per audience. |
| **TLS terminated outside the trust boundary** | Termination inside the membrane. |
| **Secrets in env files in the repo** | Secret manager; secret env vars sourced at boot. |
| **Free-form log lines with payload echo** | Structured logs only; allowlist. |
| **`/healthz` exposed publicly** | Internal-class; behind network policy. |
| **Provider URL or vendor id in `error/adapter/*`** | Sanitize. |
| **Per-route TLS / CORS / rate-limit ad-hoc** | Centralized in deployment config; reviewed against this doc. |
| **Trace attribute carries raw evidence** | Span attribute allowlist; redaction at boundary. |

[↑ Back to top](#top)

---

## 11. Open questions and ADR triggers

| Open item | Class | Suggested ADR title |
|---|---|---|
| HSTS `preload` opt-in | Posture | "HSTS preload posture". |
| Rate-limit tier disclosure on public manifest | Disclosure | "Rate-limit tier disclosure". |
| Workload identity provider — SPIFFE adoption or cloud-native? | Auth | "Internal-class workload identity provider". |
| TLS terminator placement — in-process vs proxy | Architecture | "TLS termination boundary". |
| Tracing backend choice and retention | Observability | "Tracing backend and retention". |
| Log sink — cloud provider vs self-hosted | Observability | "Log sink home". |

[↑ Back to top](#top)

---

## 12. Related docs

| Reference | Role | Truth label |
|---|---|---|
| `README.md` *(this folder)* | Landing | CONFIRMED doctrine |
| `../governed-api.md` §11 | Operational posture spine | CONFIRMED doctrine |
| `../deployment-topology.md` | Broader deployment topology | CONFIRMED scaffold |
| `THREAT_MODEL.md` | Boundaries 1 and 8 in particular | PROPOSED |
| `AUDIENCE_CLASSES.md` §9 | Rate-tier per class | PROPOSED |
| `ENVELOPES.md` | Envelope on rate / TLS / CORS failure | PROPOSED |
| `ERROR_CODES.md` | `error/rate/*` and operational codes | PROPOSED |
| `directory-rules.md` §7.1 | Governed-API canonical placement | CONFIRMED doctrine |
| `docs/runbooks/` *(future)* | Operational procedures | PROPOSED |

[↑ Back to top](#top)

---

## 13. Appendix

<details>
<summary><strong>13.1 Deployment posture — at-a-glance</strong></summary>

```text
TLS                — TLS 1.3 preferred; HSTS; mTLS for internal
CORS               — deny by default; explicit allowlist per class; no wildcard
Rate limits        — T-PUB / T-PART / T-STEW / T-INT; ERROR error/rate/* on exhaust
Secrets            — secret manager; never in repo; never in logs / envelopes
Logs               — structured; allowlisted fields; correlation_id ↔ request_id
Network            — ingress restricted; egress allowlisted; admin separate
Health / ready     — internal-class endpoints only
Tracing            — W3C context; span allowlist; never raw evidence
```

</details>

<details>
<summary><strong>13.2 Truth-label legend</strong></summary>

- **CONFIRMED** — verified this session from attached docs.
- **PROPOSED** — design / placement / inference not yet verified in implementation.
- **INFERRED** — derivable from confirmed evidence but not directly stated.
- **NEEDS VERIFICATION** — checkable, but not yet checked strongly enough to act as fact.

</details>

---

**Related (mini)** · [`README.md`](README.md) · [`../governed-api.md`](../governed-api.md) · [`THREAT_MODEL.md`](THREAT_MODEL.md) · [`AUDIENCE_CLASSES.md`](AUDIENCE_CLASSES.md) · [`ENVELOPES.md`](ENVELOPES.md) · [`ERROR_CODES.md`](ERROR_CODES.md) · [`LIFECYCLE_GATES.md`](LIFECYCLE_GATES.md)

**Last updated:** 2026-05-24 · **Doc version:** v0.1 · **Doc status:** draft · **Path status:** PROPOSED *(OPEN-DR-12 META)*

[↑ Back to top](#top)
