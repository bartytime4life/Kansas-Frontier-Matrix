<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/0f7f3e3f-4db0-4d1a-9f5a-21c8df9c2f6f
title: Observability Overview
type: standard
version: v1
status: draft
owners: TBD
created: 2026-03-01
updated: 2026-03-01
policy_label: restricted
related:
  - TODO: link to system overview doc
  - TODO: link to promotion contract doc
  - TODO: link to run receipt schema
tags: [kfm, architecture, observability]
notes:
  - Requirements grounded in the KFM vNext governance/ops guidance; concrete tooling choices are PROPOSED until selected and verified in-repo.
[/KFM_META_BLOCK_V2] -->

# Observability
Telemetry + audit that keep KFM operable **and** trustworthy.

![Status](https://img.shields.io/badge/status-draft-yellow)
![Area](https://img.shields.io/badge/area-architecture-blue)
![Policy](https://img.shields.io/badge/policy-restricted-red)
![Scope](https://img.shields.io/badge/scope-runtime%20%2B%20pipelines-blueviolet)

**Purpose:** define the *minimum* observability requirements and contracts for KFM so operators, stewards, and product owners can (1) detect failures, (2) explain behavior, and (3) prove governance controls are working.

**Where it fits:** `docs/architecture/overview/` — complements system architecture + promotion contract docs by specifying what must be observable across the truth path and trust membrane.

**Acceptable inputs:**
- Requirements (“MUST/SHOULD”) for logs/metrics/traces/receipts/audit.
- Identifier + correlation conventions.
- Dashboard and alert *requirements* (not vendor screenshots).
- Verification checklist for CI + runtime posture.

**Exclusions (do not put here):**
- Vendor-specific install/runbooks (Prometheus/Grafana/etc.) → put in `docs/runbooks/` (or equivalent).
- Secrets, credentials, or environment-specific endpoints.
- Full incident runbooks → link out to incident response docs.

---

## Quick navigation
- [Principles](#principles)
- [Signal taxonomy](#signal-taxonomy)
- [Identifiers and correlation](#identifiers-and-correlation)
- [Minimum requirements](#minimum-requirements)
- [Dashboards](#dashboards)
- [Alerting and incidents](#alerting-and-incidents)
- [Instrumentation patterns](#instrumentation-patterns)
- [Data handling and redaction](#data-handling-and-redaction)
- [Verification checklist](#verification-checklist)
- [Appendix: proposed schemas](#appendix-proposed-schemas)

---

## Principles

### Observability is part of the trust membrane
KFM’s trust membrane means clients do not directly access storage/DB; **all** access flows through governed interfaces where policy is evaluated and **logged**. Observability MUST therefore be strongest at the policy enforcement boundary (governed API + evidence resolver) and the promotion boundary (pipelines + gates).

### Two planes of observability
1. **Operational telemetry (ops plane)**  
   Logs, metrics, and traces used to run the system: latency, error rates, saturation, pipeline failures, etc.
2. **Governance telemetry (trust plane)**  
   Audit logs + run receipts + provenance links used to *explain and justify* what happened: who/what/when/why, policy decisions, inputs/outputs by digest, and promotion receipts.

> NOTE: In KFM, a “receipt” is not a nice-to-have log line. Run receipts and audit records are part of the promotion gates and “cite-or-abstain” controls.

### Start minimal, but make it enforceable
KFM’s minimum set prioritizes:
- structured logs with correlation identifiers
- key latency + failure metrics
- audit records for governed operations  
Distributed tracing is optional early, but the contracts should be tracing-ready (trace_id propagation).

---

## Signal taxonomy

| Signal | What it is | Why it exists in KFM | Examples |
|---|---|---|---|
| **Structured logs** | Machine-parseable event records | Debugging + forensic correlation across layers | request logs, pipeline step logs |
| **Metrics** | Aggregated numeric time series | SLOs, capacity planning, alerting | P95 latency, pipeline duration |
| **Traces** *(optional early)* | End-to-end request spans | Root-cause analysis across services/modules | API → evidence resolver → stores |
| **Audit log records** | Governance-grade log record for governed ops | Explain policy decisions without guessing | focus ask, story publish, promotion |
| **Run receipts** | Append-only receipts capturing inputs/tooling/hashes/policy decisions | Required for promotion + reproducibility | pipeline run receipt; focus run receipt |

---

## Identifiers and correlation

### Required identifiers
The following identifiers MUST appear where applicable to support correlation across telemetry and governance artifacts.

| Identifier | Scope | Required in | Notes |
|---|---|---|---|
| `correlation_id` | Request/run correlation | logs (API + jobs) | used to join log streams |
| `audit_ref` | Governed operation record | logs + API responses (governed ops) | primary handle for review and debugging |
| `run_id` | Pipeline/Focus run identity | run receipts + provenance | supports repeatability and lineage |
| `dataset_id` | Dataset identity | catalogs + receipts + UI surfaces | stable identity across versions |
| `dataset_version_id` | Version identity | API responses, receipts, catalogs | required for trust surfaces |
| `spec_hash` | Deterministic spec/versioning | receipts + promotion gates | blocks silent drift |
| `artifact_digests` | Content identity | receipts + some responses | ties outputs to immutable content |

> TIP: Prefer *digest-first* linking wherever possible (artifact digests, bundle digests). If an identifier is missing, treat it as an observability defect.

### Propagation rules
- **API requests:** correlation_id MUST be generated/accepted at ingress and propagated through all internal calls.
- **Governed operations:** any operation that can change state, publish, or answer as “truth” MUST emit an `audit_ref`.
- **Pipelines:** each run MUST generate a `run_id` and a run receipt; promotion MUST link to that receipt.

---

## Minimum requirements

### Minimum observability (MUST)
**Logs**
- Structured logs with `correlation_id` and `audit_ref` (where applicable).

**Metrics**
- request latency (P95) per endpoint
- evidence resolver latency
- tile response latency
- pipeline run durations and failures

**Traces**
- optional early (but recommended once the system splits or becomes performance-sensitive)

### Minimum audit logging (MUST)
Every governed operation MUST emit an audit log record including:
- who (principal, role)
- what (endpoint, parameters)
- when (time)
- why (purpose if declared)
- inputs/outputs (by digest)
- policy decisions (allow/deny, obligations, reason codes)

> WARNING: Audit logs are themselves sensitive. Apply log redaction and retention policy.

---

## Dashboards

Dashboards MUST support the distinct needs of three audiences:

### Steward view (governance health)
Required panels:
- policy denials (rate, top reason codes)
- rights/licensing issues
- quarantines (counts by gate and dataset)
- non-resolvable citations / evidence resolution failures
- “what changed” signals that correlate with new denials or failures

### Operator view (system health)
Required panels:
- pipeline health (success rate, duration, current backlog)
- storage usage (canonical stores and projections)
- deployment status (rollouts, restarts, error spikes)
- API and tile latency (P50/P95) + error rate
- evidence resolver latency + error rate

### Product view (UX health)
Required panels:
- UI performance (client-perceived latency if available)
- a11y regression indicators (test failures / audits)
- Focus Mode outcomes (abstain rate, citation verification failures)
- adoption funnels (optional, policy-safe)

---

## Alerting and incidents

### Incident types (must be supported)
At minimum, define detection + severity + on-call routing for:
- restricted data leakage
- licensing violation risk (unlicensed media published)
- corrupted catalogs or broken citations
- pipeline producing non-deterministic outputs

### Alert matrix (starter)
| Alert | Signal(s) | Severity | Primary responder | Notes |
|---|---|---:|---|---|
| Citation resolution failures spike | evidence resolver error rate | High | Steward + Operator | risks trust surfaces + Focus Mode |
| Policy denials spike after deploy | denial rate by reason | High | Steward | possible policy regression |
| Pipeline failure rate > threshold | job failures, gate failures | Medium/High | Operator | quarantine growth |
| Latency regression (P95) | endpoint P95, tile latency | Medium | Operator | may impact UX; verify caches |
| Possible leakage indicator | forbidden field detection | Critical | Steward + Security | fail closed + incident protocol |

> NOTE: “Leakage indicators” are policy-defined. Detection rules MUST not themselves leak restricted data.

---

## Instrumentation patterns

### Governed API
Instrument every request with:
- correlation_id
- dataset_version_id when applicable
- policy label (public-safe)
- audit_ref for governed operations (e.g., Focus Mode, story publishing)
- stable error model with policy-safe messages; avoid leaking sensitive existence via 403/404 differences

### Evidence resolver
Instrument:
- resolution latency
- resolution failure reasons (policy-safe)
- number of EvidenceRefs resolved per request
- obligations applied counts (redaction/generalization)

### Pipelines and promotion
Instrument:
- run duration by phase (acquire, normalize, QA, redact/generalize, package, catalog, index)
- gate outcomes (pass/fail by gate)
- deterministic checks (spec_hash stability tests) if available
- run receipt emission + linkage to audit ledger

### Focus Mode
Treat each Focus request as a governed run:
- inputs: query + optional view_state + user policy context
- outputs: answer + EvidenceRefs + audit_ref
- control loop MUST include a hard citation verification gate
- run receipt MUST store query, evidence bundle digests, policy decisions, model version, latency, and output hash

---

## Data handling and redaction

### Policy-safe logging rules (MUST)
- Do not log restricted coordinates, restricted identifiers, or restricted catalog existence in plaintext unless policy explicitly allows and logs are access-controlled.
- External errors MUST be policy-safe and stable; internal logs MAY include reason codes but still must follow redaction + retention controls.
- Audit logs should be treated as sensitive operational data.

### Retention (PROPOSED until governed)
Retention and access policy MUST exist for:
- audit ledger records
- run receipts
- structured logs
- metrics
- traces  
…and MUST be reviewed under governance (default-deny when uncertain).

---

## Verification checklist

Use this checklist to convert Unknown → Confirmed in-repo without overreach:

- [ ] Logs are structured and include `correlation_id` everywhere; include `audit_ref` for governed operations.
- [ ] Metrics exist for: endpoint P95, evidence resolver latency, tile latency, pipeline durations/failures.
- [ ] Governed operations emit audit log records with who/what/when/why + digests + policy decision details.
- [ ] Pipelines emit run receipts and promotion is blocked without them.
- [ ] Dashboards exist (or can be generated) for steward/operator/product views.
- [ ] Alert routes exist for the four minimum incident types.
- [ ] Log redaction + retention policy is documented and enforced (fail closed).

---

## Appendix: proposed schemas

### A. Proposed structured log envelope
```json
{
  "ts": "2026-03-01T12:34:56Z",
  "level": "info",
  "msg": "request complete",
  "correlation_id": "c_01HR....",
  "audit_ref": "kfm://audit/entry/123",
  "actor": {"principal": "user:123", "role": "steward"},
  "http": {"method": "POST", "path": "/api/v1/focus/ask", "status": 200, "latency_ms": 842},
  "kfm": {
    "dataset_version_id": "2026-02.abcd1234",
    "policy": {"decision": "allow", "reason_code": "OK", "obligations_applied": ["generalize_geometry_1km"]},
    "digests": {"input": ["sha256:..."], "output": ["sha256:..."]}
  }
}
```

### B. Proposed metric names (starter)
- `kfm_api_request_latency_ms{route,method,status_quantile="p95"}`
- `kfm_evidence_resolve_latency_ms{quantile="p95"}`
- `kfm_tile_latency_ms{layer,quantile="p95"}`
- `kfm_pipeline_run_duration_s{pipeline,phase,quantile="p95"}`
- `kfm_pipeline_run_failures_total{pipeline,gate}`
- `kfm_policy_denials_total{reason_code}`
- `kfm_focus_citation_verification_failures_total`
- `kfm_focus_abstain_total{reason_code}`

---

<details>
<summary>Changelog</summary>

- 2026-03-01: Initial draft created.

</details>
