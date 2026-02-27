<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/9438c30d-c510-495b-ad06-a3e8d7f044a3
title: API Observability Logging
type: standard
version: v1
status: draft
owners: platform-observability (TODO)
created: 2026-02-27
updated: 2026-02-27
policy_label: restricted
related:
  - apps/api/src/observability/README.md
  - docs/governance/safety_checks.md
  - docs/ops/runbooks/logging.md
tags: [kfm, api, observability, logging, audit, redaction]
notes:
  - This is contract-first documentation. Update code and README together.
  - Update related paths once repo reality is confirmed.
[/KFM_META_BLOCK_V2] -->

# 🧭 Observability: Logging (API)

> Governed, structured, policy-aware logging for the KFM API service.

![status](https://img.shields.io/badge/status-draft-orange)
![policy](https://img.shields.io/badge/policy-restricted-red)
![scope](https://img.shields.io/badge/scope-apps%2Fapi-blue)
![component](https://img.shields.io/badge/component-observability%2Flogging-purple)

**Owners:** `platform-observability` (TODO)  
**Status:** Draft (contract-first)  
**Policy:** This doc is `restricted` because it describes operational controls.

**Quick links:**  
[Purpose](#purpose) · [Truth status](#truth-status) · [Directory structure](#directory-structure) ·
[Quick start](#quick-start) · [Event contract](#event-contract) · [Redaction](#redaction) ·
[Audit logs](#audit-logs) · [Testing & gates](#testing--gates) · [FAQ](#faq)

---

## Purpose

This directory defines the **standard way** the API emits logs so that:

- Operational events are debuggable (production-safe, structured, queryable).
- Governed API actions are traceable (policy decision IDs, run receipts/audit IDs).
- Sensitive information is **not** leaked (PII, secrets, restricted locations, restricted metadata).

> **Contract-first rule:** if implementation differs from this README, treat it as a bug: update code and README in the **same PR**.

---

## Truth status

This README intentionally distinguishes what is **CONFIRMED** (from KFM governance requirements) vs what is **PROPOSED** (implementation choices).

### CONFIRMED requirements (non-negotiable)

- Logging is part of the **trust membrane**: governed API access consistently applies policy decisions, redactions, and logging.  
- Audit logging must be **append-only**, **redacted**, **access-restricted**, and governed by defined retention/deletion policies.  
- Governed operations should be traceable via **run receipts** and an **audit ledger**.

### PROPOSED implementation details (verify in repo)

- Event envelope field names (`event`, `ts`, `trace_id`, `decision_id`, etc.).
- Specific logging library, transport, and collectors (stdout JSON, OTEL/Fluent, etc.).
- The exact exported API (e.g., `createLogger`, `withLogContext`, middleware names).

### UNKNOWN until verified

- Actual sink(s) and deployment topology (Kubernetes, ECS, bare metal, etc.).
- Retention windows, access model, encryption-at-rest, and break-glass procedures.
- Existing conventions in `apps/api` (lint rules, error model, request context plumbing).

---

## Where this fits in the repo

This folder is intended to be the **single home** for API logging primitives:

- request-context propagation (request ID / trace correlation)
- structured log event schema/types
- redaction rules and tests
- HTTP middleware instrumentation (start/end/error)
- audit-event emission interface (append-only, policy-aware)

**Related:** `apps/api/src/observability/*` (tracing/metrics if present) and policy/audit infrastructure.

---

## Directory structure

> Update this tree to match reality (don’t guess). Keep this section current—it's part of onboarding.

Suggested minimum layout:

```text
apps/api/src/observability/logging/
  README.md                 # you are here
  index.(ts|js)             # public exports (logger + middleware + types)
  logger.(ts|js)            # logger factory + standard serializers
  context.(ts|js)           # request context storage (async-local / equivalent)
  http.(ts|js)              # HTTP middleware/interceptor logs
  redact.(ts|js)            # redaction utilities + allow/deny field lists
  audit.(ts|js)             # audit-event emission interface (append-only sink)
  schema.(ts|js)            # log event types / JSON schema (optional but recommended)
  __tests__/                # unit tests (redaction, schema, context propagation)
```

---

## Non-goals

- Replacing tracing/metrics systems (this is **logs**, not the whole observability stack).
- Building dashboards/alerts (document links to runbooks instead).
- Logging raw payloads “for convenience” in production.
- Logging anything that could meaningfully increase harm if accessed (PII, secrets, precise restricted locations).

---

## Quick start

> These snippets are **illustrative**. Verify actual imports/exports in `index.*`.

### 1) Create / access a logger

```ts
// PSEUDO (adapt to repo conventions)
import { getLogger } from "./index";

const log = getLogger();

log.info({ event: "app.start", component: "api" }, "API starting");
```

### 2) Attach per-request context (request_id, trace_id)

```ts
// PSEUDO
import { withLogContext } from "./index";

await withLogContext(
  { request_id: "req_123", trace_id: "..." },
  async () => {
    log.info({ event: "http.request.start" }, "incoming request");
  }
);
```

### 3) Use HTTP middleware for automatic request start/end logs

```ts
// PSEUDO
import { httpLoggingMiddleware } from "./index";

app.use(httpLoggingMiddleware());
```

### Proposed environment variables (verify)

```bash
# PROPOSED: keep names stable once implemented
LOG_LEVEL=info
LOG_FORMAT=json           # json | pretty
LOG_REDACTION_MODE=strict # strict | relaxed | off (off should never be used in prod)
```

---

## Event contract

### Design goals

- **Structured-first**: logs are JSON objects; `msg` is optional sugar.
- **Context-rich**: every log event can be tied to request + trace + actor + policy decision (when applicable).
- **Stable**: field names don’t churn (breaking changes require a migration note).
- **Safe**: redaction happens before serialization/transport.

### Base envelope (recommended)

Every log event SHOULD include:

| Field | Type | Notes |
|------|------|------|
| `ts` | ISO-8601 string | Event timestamp (UTC) |
| `level` | string | `debug|info|warn|error` (add `trace/fatal` only if you truly need them) |
| `event` | string | Stable event name; use `dot.case` |
| `msg` | string | Optional human message |
| `service` | object | `{ name, version }` (version = git commit / build id) |
| `env` | object | `{ name }` e.g. `dev|staging|prod` |
| `request` | object | `{ id, method, route, status, duration_ms }` |
| `trace` | object | `{ trace_id, span_id }` |
| `actor` | object | `{ principal, role }` (avoid direct PII) |
| `policy` | object | `{ decision_id, policy_label, obligations }` (when governed) |
| `kfm` | object | `{ run_id, dataset_version_id, evidence_refs_digest }` (when applicable) |

> **Tip:** Prefer IDs/digests over raw values. If you need a value for debugging, log a **hash** (with a rotation salt) instead of the raw string.

### Event naming

Use stable names that describe the **operation**, not the implementation:

- `http.request.start`
- `http.request.end`
- `http.request.error`
- `policy.decision`
- `audit.append`
- `evidence.resolve.start`
- `evidence.resolve.end`
- `focus.query.start`
- `focus.query.end`
- `storage.read` / `storage.write` (only at boundaries; do not log raw SQL / queries by default)

### Example event (application log)

```json
{
  "ts": "2026-02-27T18:12:07.123Z",
  "level": "info",
  "event": "http.request.end",
  "msg": "request complete",
  "service": { "name": "kfm-api", "version": "deadbeef" },
  "env": { "name": "prod" },
  "request": {
    "id": "req_01J...XYZ",
    "method": "GET",
    "route": "/v1/layers/:id",
    "status": 200,
    "duration_ms": 34
  },
  "trace": { "trace_id": "4bf92f...", "span_id": "00f067..." },
  "actor": { "principal": "user:12345", "role": "public" },
  "policy": {
    "decision_id": "kfm://policy_decision/xyz",
    "policy_label": "public",
    "obligations": ["redact:precise_location"]
  }
}
```

---

## Redaction

### Why strict-by-default

Logs are high-leverage data. They often flow to centralized systems, are retained for long periods, and are queried broadly during incidents. A single leaked token or PII field can become a breach.

### Redaction rules

**1) Never log secrets**
- Authorization headers
- cookies / session IDs
- API keys
- signed URLs
- private keys
- database connection strings

**2) Don’t log raw PII**
Examples: email, phone, home address, names tied to individual-level records.

If you must correlate, log:
- a stable internal identifier (preferred), or
- a salted hash (rotate salt periodically), or
- a coarse bucket (age range instead of exact DOB).

**3) Treat restricted locations as high risk**
- Do not log raw coordinates for restricted layers/datasets.
- If location context is needed, log a **coarse geography** identifier (e.g., county FIPS) or a generalized tile index.

**4) Redact before transport**
Redaction must occur:
- in-process
- before serialization
- before log shipping

### Redaction matrix (recommended)

| Data type | Example | Policy | How to log |
|---|---|---|---|
| Secret | bearer token | **Never** | omit / `[REDACTED]` |
| PII | email | **Avoid** | internal ID / salted hash |
| Restricted location | exact lat/lon | **Default deny** | coarse region ID only |
| Large payload | request body | **Avoid** | size + digest (optional) |
| Policy decision | decision id | **OK** | log `decision_id` + obligation names |
| Evidence bundle | citations | **OK with care** | log digest/ID, not full text |

> **Warning:** “debug logs” are not safe logs. If debug is enabled in production, assume it will leak.

---

## Audit logs

Audit logs are not “just logs.” They are governed records of governed actions.

### Audit log properties (required)

- **Append-only**
- **Redacted** for PII + restricted info
- **Access-restricted** to stewards/operators
- **Retention and deletion policies** are defined and enforced

### What goes in audit logs

Examples (governed events):

- policy decisions affecting access/redaction
- Focus Mode queries and their evidence bundles (by digest/ID)
- promotion / publish / quarantine actions
- administrative changes to policy packs, roles, or key governance configs

> **Rule of thumb:** if an action affects *what users can see* or *why a claim is allowed*, it’s a strong audit candidate.

### Relationship to run receipts

Run receipts are structured provenance/audit artifacts for operations. This logging module should support **linking** operational logs to run receipts via IDs, not duplicating full receipts in log streams.

---

## Testing & gates

### Minimum tests for this directory

- **Redaction unit tests**
  - known secret fields are always redacted
  - PII fields are redacted/hashed according to mode
  - restricted-location fields are suppressed or generalized
- **Context propagation tests**
  - request_id/trace_id persist across async boundaries
- **Schema tests (recommended)**
  - log events validate against a JSON schema (or TS type tests)
- **Audit sink tests**
  - append-only behavior is enforced (no update/delete path)
  - unauthorized access attempts are denied (if applicable)

### Definition of Done checklist (logging changes)

- [ ] Event name is stable and documented in the registry
- [ ] Event includes request + trace context (where applicable)
- [ ] Redaction rules applied and tested (fixtures included)
- [ ] No raw secrets/PII in output (add a “canary” test)
- [ ] Audit events (if added/changed) include decision/run IDs and are append-only
- [ ] README updated (this file) + any runbook references updated

---

## Operational notes (runbooks)

- Log volume and retention directly affect cost and breach surface area.
- Production defaults should be `info` with sampling for noisy events.
- Debug should be:
  - allowed only in dev/local, or
  - guarded behind short-lived feature flags with strict access controls.

See:
- `docs/ops/runbooks/logging.md` (TODO)
- `docs/ops/runbooks/incident-response.md` (TODO)

---

## FAQ

### “Can I log the request body to debug an issue?”
**No** (not by default). Log a digest + size, and add targeted instrumentation behind a short-lived, access-restricted feature flag in non-production first.

### “Where do we store audit logs?”
This README doesn’t decide storage. The requirement is append-only + redacted + access-restricted + governed retention. Storage choice belongs in an ADR/runbook.

### “How do I add a new event type?”
1. Pick a stable `event` name (`domain.action.state`).
2. Add it to the event registry table.
3. Ensure it carries context (`request`, `trace`, `actor`, `policy` as appropriate).
4. Add redaction + schema tests.
5. Update this README if the contract changes.

---

<details>
<summary>Appendix: Suggested event registry template</summary>

```markdown
| Event | Level | When | Required fields | Notes |
|---|---|---|---|---|
| http.request.start | info | request accepted | request.id, request.method, request.route | no body |
| http.request.end | info | request finished | request.status, request.duration_ms | |
| http.request.error | error | handler throws | error.name, error.code | sanitize stack |
| policy.decision | info | policy evaluated | policy.decision_id, policy.policy_label | no sensitive resource details |
| audit.append | info | audit written | audit_id/run_id, actor, policy | append-only |
```
</details>

---

_Back to top:_ [↑](#-observability-logging-api)
