# Observability Configs
Declarative, governed observability configuration for Kansas Frontier Matrix (KFM): **logs**, **metrics**, **traces**, **dashboards**, and **alerts**.

**Status:** Draft (vNext) • **Scope:** Runtime + Pipelines • **Environments:** dev / staging / prod • **Owners:** Steward + Operator (assign in CODEOWNERS)

---

## Quick navigation
- [What lives here](#what-lives-here)
- [Minimum required telemetry](#minimum-required-telemetry)
- [Telemetry contract](#telemetry-contract)
- [Dashboards and alerting](#dashboards-and-alerting)
- [Governance and safety](#governance-and-safety)
- [Suggested directory layout](#suggested-directory-layout)
- [Deployment model](#deployment-model)
- [Change workflow](#change-workflow)
- [Appendix](#appendix)

---

## What lives here
This folder is the **configuration surface** for KFM observability. It should let operators and stewards answer:

- **Is the platform healthy?** (availability, latency, capacity, errors)
- **Are governed operations compliant?** (policy denials, rights issues, quarantines, audit integrity)
- **Is user experience degrading?** (UI performance and a11y regression signals)
- **Can we trace a specific governed action end-to-end?** (from UI → API → evidence resolver/pipelines → catalogs/run receipts)

Non-goals:
- Application instrumentation code (belongs in service repos/modules).
- Business analytics (belongs in product analytics; keep separate from governance telemetry).

---

## Minimum required telemetry
KFM’s **minimum observability** baseline (do not ship without it):

- **Structured logs** with `correlation_id` and `audit_ref`
- **Metrics**:
  - request latency (**P95**) per endpoint
  - evidence resolver latency
  - tile response latency
  - pipeline run durations and failures
- **Traces**: optional early, but supported by contract if enabled

> NOTE: “Minimum” is the floor. Add more as you learn, but keep contracts stable.

---

## Telemetry contract
This section defines the **expected semantics** for identifiers and fields so that dashboards, alerts, and investigations remain consistent across services.

### Correlation and audit identifiers
- `correlation_id`  
  A request-scoped ID used to join logs/metrics/traces across components (UI ↔ API ↔ downstream services).
- `audit_ref`  
  A governed-operation reference. It must be emitted in logs and returned by governed API operations and policy-safe errors (so investigations can be audited without leaking restricted details).

### Audit record minimum fields (governed operations)
Every governed operation MUST emit an audit log record that captures:

- **who**: principal + role  
- **what**: endpoint + parameters (policy-safe)  
- **when**: timestamp  
- **why**: purpose if declared  
- **inputs/outputs**: by **digest** (not raw payloads)  
- **policy decisions**: allow/deny, obligations, reason codes

> WARNING: Audit logs are sensitive. See [Governance and safety](#governance-and-safety).

### Standard run identifiers (pipelines + governed runs)
KFM benefits from stable identifiers shared across telemetry and catalogs (DCAT/STAC/PROV/run receipts). If you implement OpenTelemetry and/or Prometheus-style labels, standardize on the following keys.

| Concept | OTel attribute (recommended) | Prom label (recommended) | Notes |
|---|---|---|---|
| Run ID | `kfm.job.run_id` | `job_run_id` | UUID/ULID |
| Commit SHA | `kfm.git.commit_sha` | `commit_sha` | 7–40 hex |
| Status | `kfm.job.status` | `status` | scheduled/running/succeeded/failed/canceled |
| Started | `kfm.job.started_at` | `started_at` | RFC3339; also emit unix seconds |
| Ended | `kfm.job.ended_at` | `ended_at` | RFC3339; also emit unix seconds |
| Dataset ID | `kfm.dataset.id` | `dataset_id` | DCAT/STAC id |
| Pipeline | `kfm.pipeline.name` | `pipeline` | stable slug |

### Metrics naming rules (recommended)
These rules keep dashboards coherent even as implementations change.

- Prefer **RED** (Rate/Errors/Duration) for APIs and **USE** (Utilization/Saturation/Errors) for infrastructure.
- Include **service**, **env**, and **endpoint** labels for request metrics.
- Do **not** label metrics with high-cardinality values (raw query text, coordinates, user identifiers).

---

## Dashboards and alerting
Dashboards should support three primary “views”:

### Steward view (governance health)
Focus: policy and rights compliance.

Examples of panels:
- policy denials by rule / dataset / endpoint
- rights issues (unclear rights, blocked publish attempts)
- quarantine counts / backlogs
- evidence resolver allow/deny rates and latency

### Operator view (platform health)
Focus: runnability and SLOs.

Examples of panels:
- pipeline run success rate and duration distributions
- storage usage (raw/work/processed/catalog)
- API error rates and saturation (CPU/mem), queue depths
- deployment status signals (rollouts, crash loops)

### Product view (experience health)
Focus: user-facing quality.

Examples of panels:
- UI performance (page load, map interaction latency)
- tile latency and error rates
- a11y regression indicators (from CI and/or runtime checks)

### Alerting (recommended minimum)
Alerts should be actionable and routed by severity.

- **P0 / Page**
  - sustained API unavailability
  - sustained tile failures
  - pipeline runs failing above threshold
  - evidence resolver failing or timing out
- **P1 / Ticket**
  - SLO burn (latency P95 elevated)
  - storage nearing capacity
  - rising policy denial rate (potential misconfig or attempted misuse)

> TIP: Track alert fatigue. Prefer multi-window burn-rate alerts over noisy threshold alerts.

---

## Governance and safety
Observability is part of governance: it must not leak restricted data or personal data.

### Audit log protections (required)
Audit logs MUST be treated as sensitive operational data:

- append-only
- redacted for PII and restricted info
- access restricted to stewards/operators
- retention + deletion policies defined and enforced

### Sensitive location and restricted data leakage
Do not log:
- raw restricted geometries or precise coordinates
- policy-protected dataset existence hints in “public” contexts
- full query payloads if they contain restricted identifiers

Preferred patterns:
- log dataset_version_id + digests, not raw records
- log generalized/coarsened spatial filters (if needed), or store details in the audit ledger under restricted access controls

---

## Suggested directory layout
This repository may choose any observability stack. The following layout is RECOMMENDED because it cleanly separates concerns and makes GitOps overlays straightforward.

~~~text
configs/observability/
  README.md

  # Metrics (Prometheus-style) — scrape + rules
  metrics/
    # scrape/        # scrape configs (if not operator-managed)
    # rules/         # recording and alert rules

  # Logs — parsing, routing, retention
  logs/
    # pipelines/     # parsing rules (json, grok, etc.)
    # retention/     # retention configs/policies

  # Traces — sampling, tail-based policies, exporters
  traces/
    # sampling/      # sampling strategies
    # processors/    # attribute redaction, batching, etc.

  # Dashboards — JSON, provisioning, folders
  dashboards/
    # steward/
    # operator/
    # product/

  # Stack deployment glue (if managed in-repo)
  deploy/
    # base/          # baseline manifests/helm values
    # overlays/      # dev/staging/prod overlays
~~~

> NOTE: Don’t create empty folders just to match this tree. Add only what you actually use, and keep the README accurate.

---

## Deployment model
Preferred operational posture is GitOps:

- declarative manifests in repo
- environments: dev, staging, prod
- promotion between environments is controlled and audited
- secrets are managed outside git but referenced declaratively

For Kubernetes/OpenShift-style deployments, observability should cover:
- pipeline runner (batch jobs)
- API service
- evidence resolver (may be part of API)
- policy engine (sidecar or embedded)
- search/db services (managed where possible)

---

## Change workflow
When you change observability configs, treat it like an API contract change: dashboards and alerts depend on it.

### Required steps
1. Describe the intent in the PR (what question are we trying to answer?).
2. Keep identifier contracts stable (`audit_ref`, `correlation_id`, run ids/labels).
3. Update dashboards and alerts (or justify why not).
4. Confirm no high-cardinality labels were introduced.
5. Confirm redaction/retention impact (audit logs are sensitive).

### Suggested CI gates (PROPOSED)
- validate dashboard JSON schema (and provisioning)
- validate alert rules syntax
- run a “metrics contract” test (expected series names exist)
- run a “no secrets in configs” scan
- run a “no restricted leakage” lint (deny known coordinate fields in audit logs)

---

## Appendix

<details>
<summary><strong>Example: audit log record shape (illustrative)</strong></summary>

This example shows a *shape* that satisfies the governed audit requirements. Field names may vary by implementation, but the semantics should remain stable.

~~~json
{
  "ts": "2026-02-22T18:12:03.123Z",
  "level": "INFO",
  "service": "kfm-api",
  "env": "staging",

  "correlation_id": "01HZZZZZZZZZZZZZZZZZZZZZZZ",
  "audit_ref": "kfm://audit/01HYYYYYYYYYYYYYYYYYYYYYYYY",

  "who": { "principal": "user:123", "role": "steward" },
  "what": { "endpoint": "POST /api/v1/focus/ask", "params": { "scope": "public" } },
  "why": "investigation",

  "io": {
    "inputs": [{ "digest": "sha256:..." }],
    "outputs": [{ "digest": "sha256:..." }]
  },

  "policy": {
    "decision": "allow",
    "obligations": ["attribution_required"],
    "reason_codes": ["P-ALLOW-001"]
  },

  "latency_ms": 842
}
~~~

</details>

<details>
<summary><strong>Example: metric checklist (copy/paste)</strong></summary>

- [ ] API request latency P95 per endpoint
- [ ] Evidence resolver latency
- [ ] Tile response latency
- [ ] Pipeline run durations (histogram)
- [ ] Pipeline run failures (counter)
- [ ] Policy denials (counter)
- [ ] Rights blocks (counter)
- [ ] Quarantine backlog (gauge)

</details>
