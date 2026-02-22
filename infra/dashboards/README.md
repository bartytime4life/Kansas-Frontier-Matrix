# KFM Infra Dashboards
Dashboards-as-code for **KFM operational observability** (steward / operator / product views) with governance-safe defaults.

**Status:** draft  
**Owners:** _TBD (platform + governance)_  
**Scope:** infra-only dashboards (not public-facing data explorers)

![status](https://img.shields.io/badge/status-draft-lightgrey)
![scope](https://img.shields.io/badge/scope-infra%2Fdashboards-blue)
![governance](https://img.shields.io/badge/governance-audit%20%2B%20policy-important)

## Navigation
- [What lives here](#what-lives-here)
- [Non-negotiable requirements](#non-negotiable-requirements)
- [Dashboard views](#dashboard-views)
- [Minimum telemetry contract](#minimum-telemetry-contract)
- [Directory layout](#directory-layout)
- [Add or change a dashboard](#add-or-change-a-dashboard)
- [Governance and security](#governance-and-security)
- [Definition of Done](#definition-of-done)

---

## What lives here

This folder is for **operational dashboards** that help KFM run safely:

- **Platform health** (API latency, pipeline failures, tile performance)
- **Governance health** (policy denials, rights issues, quarantines)
- **Product health** (UI performance + accessibility regression signals)

This folder is **not** the implementation for the public portal’s interactive maps/charts/data explorers. Those are application-layer features and should live with the UI codebase.

---

## Non-negotiable requirements

KFM is explicit that the platform must be operable, and that “minimum observability” and dashboard support must exist early (not bolted on later). This repo folder is the place where we keep those dashboards **versioned, reviewed, and promoted**.

### Governance-first observability
Dashboards must be compatible with KFM’s governed operations model:

- Every governed operation emits auditable records (who/what/when/why + inputs/outputs by digest + policy decisions).
- Audit logs are sensitive and require redaction/retention controls.
- Dashboards must not create a “side channel” that leaks restricted existence, locations, or rights status to unauthorized roles.

### GitOps-compatible
Dashboards should be managed like other infra artifacts:
- declarative, reviewed via PR
- promoted across environments (dev → staging → prod)
- secrets managed outside git but referenced declaratively

---

## Dashboard views

KFM calls out three dashboard “views” that must be supported. Treat these as separate “packs” with minimal overlap.

| View | Primary audience | Must answer | Examples (non-exhaustive) |
|---|---|---|---|
| **Steward** | governance / data stewardship | “Are policy/rights gates working and is anything quarantined?” | policy denials, rights issues, quarantines, approval backlog, restricted-leakage signals |
| **Operator** | platform / SRE / infra | “Is the system healthy and cost-contained?” | pipeline health, storage usage, deployment status, queue depth, error rates |
| **Product** | UI / product / QA | “Is the user experience degrading?” | UI performance, tile latency, frontend errors, accessibility regression indicators |

---

## Minimum telemetry contract

Dashboards should assume KFM’s baseline observability is present:

### Logs (structured)
- structured logs with **correlation IDs** and `audit_ref`
- dashboards that link logs ↔ traces ↔ run receipts should prefer `audit_ref` as the join key

### Metrics
Dashboards must cover, at minimum:
- request latency **P95 per endpoint**
- evidence resolver latency
- tile response latency
- pipeline run durations and failures

### Traces
- optional early (but design dashboards so they can attach traces later without changing semantics)

> Practical implication: if a dashboard depends on a metric that doesn’t exist, the *fix* is to instrument the service, not to accept blind spots.

---

## Directory layout

> **NOTE:** The exact backend (Grafana / other) is not enforced by this README. Keep the layout backend-agnostic, but organized by **view** so governance review is straightforward.

Suggested structure:

```text
infra/dashboards/
  README.md

  dashboards/
    steward/
      README.md
      kfm-steward-policy-denials.json
      kfm-steward-rights-quarantine.json

    operator/
      README.md
      kfm-operator-api-latency.json
      kfm-operator-pipeline-health.json
      kfm-operator-storage-usage.json

    product/
      README.md
      kfm-product-ui-performance.json
      kfm-product-a11y-regressions.json

  provisioning/               # optional: if your dashboard tool supports provisioning-as-code
    datasources/
    folders/
    dashboards/

  alerts/                      # optional: alert rules close to the dashboard pack they support
    steward/
    operator/
    product/
```

### Naming conventions (recommended)
- Dashboard files: `kfm-<view>-<topic>.json`
- Dashboard title prefix: `KFM / <View> / <Topic>`
- Keep identifiers stable across renames (don’t “break links” in incident retros).

---

## Add or change a dashboard

### 1) Decide which view owns it
- If it includes policy denials, rights states, or quarantines → **Steward**
- If it includes infra health, uptime, storage, deployments → **Operator**
- If it includes UX/perf/a11y signals → **Product**

If a dashboard spans multiple views, prefer **two dashboards** over one mixed dashboard. This reduces access-control confusion.

### 2) Add the dashboard file
- Place dashboard definitions under `dashboards/<view>/`
- Keep queries free of secrets and role-unsafe fields

### 3) Update the dashboard index
Until there is an automated registry, the README tables (here and per-pack) are the source of truth.

Add a row to the appropriate pack’s `README.md` (or here if pack READMEs don’t exist yet):

| Dashboard | File | Datasource(s) | Inputs | Notes |
|---|---|---|---|---|
| `KFM / Operator / API Latency` | `dashboards/operator/kfm-operator-api-latency.json` | metrics | `http_request_duration_seconds` | includes P95 per endpoint |

### 4) Validate
Backend-agnostic baseline checks (recommended):
- JSON is valid (`jq . <file> > /dev/null`)
- no secrets accidentally committed (`git grep -nE "(api[_-]?key|token|password|secret)" infra/dashboards`)
- dashboard queries do not expose restricted entities/locations

### 5) Review gates (strongly recommended)
- Steward dashboards: require governance/steward review
- Operator dashboards: require platform/SRE review
- Product dashboards: require UI/perf/a11y owner review

---

## Governance and security

### Dashboards are governed artifacts
Even if dashboards are “just visualization,” they can leak:
- restricted dataset existence
- sensitive locations via drill-down
- rights/contract status
- operational details that enable abuse

Therefore:
- default to policy-safe aggregates
- avoid exact coordinates or identifiers in dashboards unless explicitly approved for the viewer role
- treat audit logs as sensitive (redact and apply retention)

### Join keys
Prefer `audit_ref` and correlation IDs as universal join keys across:
- logs
- traces
- run receipts / audit ledger

This enables investigations without copying sensitive payloads into metrics labels.

---

## Definition of Done

A dashboard change is “done” when:

- [ ] Dashboard is placed under the correct **view pack**
- [ ] Dashboard uses **policy-safe** queries and fields
- [ ] Covers (or explicitly references) the minimum required metrics for the relevant surface:
  - [ ] P95 latency (endpoint-level where applicable)
  - [ ] evidence resolver latency (if applicable)
  - [ ] tile latency (if applicable)
  - [ ] pipeline run durations/failures (if applicable)
- [ ] Links investigations via **audit_ref / correlation ID** (where possible)
- [ ] Validated (JSON + secret scan)
- [ ] Reviewed by the owning role (steward/operator/product)
- [ ] Promoted via GitOps process (dev → staging → prod) with an auditable PR trail

---

<details>
<summary>Appendix: Suggested core dashboards (starter set)</summary>

### Steward (governance health)
- Policy denials over time by reason code (policy-safe)
- Rights issues / missing rights metadata counts
- Quarantine queue (count + age)

### Operator (platform health)
- API latency P95 per endpoint + error rate
- Pipeline run duration + failure rate by dataset_slug
- Storage growth rate (raw/work/processed/catalog)
- Deployment rollouts + restart loops

### Product (UX health)
- Tile latency vs time range + region (aggregate)
- Frontend error rate
- A11y regression indicators (trend + thresholds)

</details>

---

_Back to top_: [KFM Infra Dashboards](#kfm-infra-dashboards)
