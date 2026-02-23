<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/0f9f4cf3-6e9d-4f0b-b8c0-0e0ee9c79b7a
title: Alerts
type: standard
version: v1
status: draft
owners: TBD (Platform Observability)
created: 2026-02-23
updated: 2026-02-23
policy_label: restricted
related:
  - configs/observability/README.md
tags: [kfm, observability, alerts, ops]
notes:
  - This README is toolchain-agnostic by default. Replace TODOs with your actual stack (Prometheus/Alertmanager, Grafana, cloud-native, etc.).
  - Do not commit secrets or private contact info. Use secret references and approved routing targets.
[/KFM_META_BLOCK_V2] -->

# Alerts
Declarative alert rules and routing policy for KFM observability.

**Status:** Draft  
**Owners:** TBD (Platform Observability)  
**Path:** `configs/observability/alerts/`

![status](https://img.shields.io/badge/status-draft-lightgrey)
![policy](https://img.shields.io/badge/policy-restricted-orange)
![domain](https://img.shields.io/badge/domain-observability-blue)
![ci](https://img.shields.io/badge/ci-TODO-lightgrey)

---

## Quick navigation
- [Overview](#overview)
- [Directory layout](#directory-layout)
- [What belongs here](#what-belongs-here)
- [What must not go here](#what-must-not-go-here)
- [Alert metadata contract](#alert-metadata-contract)
- [Telemetry identifiers](#telemetry-identifiers)
- [Design guidelines](#design-guidelines)
- [Change workflow](#change-workflow)
- [Testing and CI gates](#testing-and-ci-gates)
- [Promotion and rollback](#promotion-and-rollback)
- [Security and redaction](#security-and-redaction)
- [Appendix](#appendix)

---

## Overview
This directory contains **alert definitions** and **alert routing policy** for KFM. Alerts are treated as *production controls*:

- They must be **reviewable**, **deterministic**, and **auditable**.
- They must produce **actionable signals** (low noise, clear ownership, runbook-first).
- They must support KFM’s “trust membrane”: each operational claim (a page, a ticket, a block) should be traceable to evidence and policy.

> NOTE  
> This README is intentionally **toolchain-agnostic**. If your stack is already decided (Prometheus/Alertmanager, Grafana Unified Alerting, cloud provider alerts, etc.), add a short “Stack” section below and replace the TODOs.

[Back to top](#alerts)

---

## Directory layout
Recommended layout (update to match the real tree):

```text
configs/observability/alerts/
├─ README.md
├─ rules/                    # Alert rules (metrics/logs/traces based)
│  ├─ platform/              # Cluster/runtime/platform alerts
│  ├─ services/              # Service-level alerts (API, web, workers)
│  └─ pipelines/             # Data/pipeline run + promotion gate alerts
├─ routes/                   # Routing policy (who gets what)
│  ├─ receivers/             # Receiver definitions (no secrets committed)
│  └─ routing/               # Matchers, grouping, dedupe, silences policy
├─ templates/                # Message templates (if supported by your tool)
└─ tests/                    # Rule tests, snapshots, fixtures (if supported)
```

[Back to top](#alerts)

---

## What belongs here
Acceptable inputs in this directory:

- Alert rule files (YAML/JSON) for the chosen alert engine.
- Routing policy (matchers, grouping keys, notification policy).
- Message templates used by routing/notification (no secrets).
- Tests/fixtures/snapshots for alert rules.
- Minimal documentation needed to operate alerts (this README + conventions).

[Back to top](#alerts)

---

## What must not go here
Do **not** commit:

- Secrets: API keys, webhook URLs, SMTP creds, tokens, paging keys, signing keys.
- Private contact details: personal phone numbers, personal emails, private Slack handles.
- Any sensitive location specifics or restricted coordinates (use coarse geography + policy review).
- Ad-hoc one-off silences without governance (use a tracked workflow; prefer time-bounded silences).

> WARNING  
> Treat alert routing as **security-relevant configuration**: it controls who gets operational signals and can leak environment details if misconfigured.

[Back to top](#alerts)

---

## Alert metadata contract
All alerts **must** carry enough metadata to be actionable and governable.

### Required fields
| Field | Type | Required | Purpose |
|---|---:|:---:|---|
| `severity` | label | ✅ | Drive routing + urgency (page vs ticket vs info). |
| `kfm_owner` | label | ✅ | Owning team or role (e.g., `platform-observability`, `data-platform`). |
| `kfm_service` | label | ✅ | Service/pipeline name (stable slug). |
| `env` | label | ✅ | Environment (dev/stage/prod). |
| `summary` | annotation | ✅ | One-line human summary. |
| `description` | annotation | ✅ | What happened + why it matters + next best action. |
| `runbook_url` | annotation | ✅ | Link to runbook section for responders. |

### Strongly recommended fields
| Field | Type | Recommended | Notes |
|---|---:|:---:|---|
| `dataset_id` | label | ✅ | If the alert is dataset/pipeline scoped. |
| `job_run_id` | label | ✅ | If the alert is run-scoped. |
| `commit_sha` | label | ✅ | If the alert is tied to deploy/run revision. |
| `evidence_ref` | annotation | ✅ | Pointer to receipt/trace/dashboard snapshot (format is stack-specific). |
| `slo` | label | ✅ | Link alert to an SLO objective name when applicable. |

> TIP  
> If an alert cannot answer: **Who owns this? What do I do next? Where is the evidence?** — it’s not ready to ship.

[Back to top](#alerts)

---

## Telemetry identifiers
To support cross-system traceability (metrics ↔ traces ↔ catalogs/receipts), use consistent identifiers in telemetry and propagate them into alert labels/annotations when available.

### Canonical identifier set
Use the following canonical concepts (adapt names to your telemetry stack):

| Concept | Example label/field | Used for |
|---|---|---|
| Run ID | `job_run_id` | Link alerts to a specific pipeline run / execution. |
| Commit | `commit_sha` | Tie alerts to a code revision. |
| Status | `status` | Derive alerts from job lifecycle states. |
| Started | `started_at` | Time-bounding; debugging and evidence. |
| Ended | `ended_at` | Completion and duration reasoning. |
| Dataset | `dataset_id` | Join operational alert to cataloged artifact. |
| Pipeline | `pipeline` | Stable routing + grouping. |

[Back to top](#alerts)

---

## Design guidelines
### Reduce noise by design
- Prefer **SLO-based** alerts (burn rate) over raw threshold alerts.
- Use **multi-window** confirmation for paging alerts (short + long windows).
- Make non-page alerts default to tickets and dashboards.

### Make alerts actionable
- Every alert has a **runbook**.
- Every alert includes **what changed** (labels that identify the run, commit, dataset, env).
- Every alert includes a **default first step**.

### Use clear severity semantics
Recommended severity model (adapt to your incident tooling):

| Severity | Meaning | Notification | Expectations |
|---|---|---|---|
| `page` | Immediate human action required | On-call page | Fast response, mitigation-first. |
| `ticket` | Needs attention soon | Ticket queue | Triage within business hours. |
| `info` | Informational | Optional channel | No action required by default. |

[Back to top](#alerts)

---

## Change workflow
Use PR-driven changes with explicit review and test gates.

### Definition of done
- [ ] Alert has required metadata (see [Alert metadata contract](#alert-metadata-contract)).
- [ ] Alert has a runbook link and the runbook section exists.
- [ ] Routing rules updated (if needed) and do not widen blast radius accidentally.
- [ ] Tests pass locally and in CI (see [Testing and CI gates](#testing-and-ci-gates)).
- [ ] No secrets or private contact info added.
- [ ] Rollback plan is clear (revert PR, disable route, or time-bound silence with ticket).

### Review expectations
- **Platform/Observability** approves changes that affect shared routing, paging, or global rules.
- Service owners approve changes that page their teams.

[Back to top](#alerts)

---

## Testing and CI gates
This directory is expected to be CI-validated. Replace the commands below with your real toolchain.

### Recommended minimum gates
- YAML/JSON format validation
- Schema validation (if you maintain JSONSchema/OpenAPI-like contracts for alert objects)
- Lint rules for required labels/annotations
- Tool-native config checks (e.g., rule parse/compile)
- “No secrets” scanners on config changes

### Example local commands
```bash
# TODO: replace with your repo's actual targets/tools

# 1) Format/lint
make alerts-lint

# 2) Validate rule syntax
make alerts-validate

# 3) Run rule tests
make alerts-test
```

> NOTE  
> If you use a supply-chain posture for configs, add a gate that ensures configs are canonicalized before hashing and that attestation verification is required for promotion.

[Back to top](#alerts)

---

## Promotion and rollback
### Promotion principles
- Treat alert configs as **versioned artifacts**.
- Prefer deterministic builds: canonicalize → hash → diff.
- Promotion to “prod routing/page” is gated by CI checks and review.

### Rollback principles
- Roll back by reverting the PR.
- For urgent noise: apply a **time-bounded silence** with a tracking ticket, then fix the rule.

[Back to top](#alerts)

---

## Security and redaction
- Do not commit secret material. Use secret references (Kubernetes secrets, vault refs, managed integrations).
- Keep receiver names generic (e.g., `pager_primary`, `ticket_ops`) and bind to real endpoints outside git.
- Avoid leaking internal topology in alert messages. Prefer stable service names over hostnames/IPs.
- For sensitive datasets/locations: do not include precise coordinates or restricted descriptors in labels or descriptions.

[Back to top](#alerts)

---

## Appendix
<details>
<summary><strong>Example: alert rule skeleton</strong></summary>

```yaml
# This is a schematic example. Replace fields/structure with your alert engine’s format.
groups:
  - name: kfm.example
    rules:
      - alert: KfmExampleAlert
        expr: TODO_EXPRESSION_HERE
        for: 10m
        labels:
          severity: ticket
          kfm_owner: platform-observability
          kfm_service: TODO_SERVICE_SLUG
          env: TODO_ENV
        annotations:
          summary: "TODO short summary"
          description: "TODO what happened, why it matters, first action"
          runbook_url: "../../docs/runbooks/observability.md#kfmexamplealert"
          evidence_ref: "TODO dashboard/trace/receipt reference"
```

</details>

<details>
<summary><strong>Example: routing skeleton</strong></summary>

```yaml
# Schematic example. Replace with your routing engine’s format.
route:
  group_by: ["alertname", "kfm_service", "env"]
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 2h
  routes:
    - matchers:
        - severity="page"
      receiver: pager_primary
    - matchers:
        - severity="ticket"
      receiver: ticket_ops

receivers:
  - name: pager_primary
    # TODO: secret-managed integration reference, not a raw URL/token
  - name: ticket_ops
    # TODO
```

</details>
