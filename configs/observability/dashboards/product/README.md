<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/d0f294a9-71bd-4a1c-ad60-0eb343fabd1e
title: KFM Product Observability Dashboards
type: standard
version: v1
status: draft
owners: kfm-platform-observability (TODO confirm)
created: 2026-02-23
updated: 2026-02-23
policy_label: restricted
related:
  - (TODO) ../README.md
  - (TODO) ../steward/README.md
  - (TODO) ../operator/README.md
tags: [kfm, observability, dashboards, product]
notes:
  - Product view dashboards focus on UI performance and accessibility regression indicators.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KFM Product Observability Dashboards

![status](https://img.shields.io/badge/status-draft-blue)
![view](https://img.shields.io/badge/view-product-6f42c1)
![area](https://img.shields.io/badge/area-observability-0aa)
![policy](https://img.shields.io/badge/policy_label-restricted-critical)

Internal dashboards for the **product view**: **UI performance** and **accessibility (a11y) regression indicators**.

> **Audience:** product engineers, frontend maintainers, UX/a11y reviewers, on-call  
> **Goal:** detect and diagnose user-facing regressions early—without leaking sensitive details.

**Quick navigation:**  
[Purpose](#purpose) • [Directory contents](#directory-contents) • [Dashboard registry](#dashboard-registry) • [Signals](#signals-and-dimensions) • [Conventions](#conventions) • [Change process](#change-process) • [Definition of done](#definition-of-done) • [Troubleshooting](#troubleshooting) • [References](#references)

---

## Purpose

KFM’s observability guidance calls for dashboards that support three perspectives: **steward**, **operator**, and **product**.  
This folder is the **product** slice: dashboards that make **UX regressions visible** (performance + accessibility), so we can fix them before they become incidents.

This folder is **not** the public-facing “data dashboards” shown on the portal. It is for **internal operational visibility**.

[Back to top](#top)

---

## Where this fits in the repo

This folder is intended to live at:

- `configs/observability/dashboards/product/`

It should sit alongside other observability configuration and (expected) sibling dashboard views:

- `configs/observability/dashboards/steward/` *(policy denials, rights issues, quarantines)*
- `configs/observability/dashboards/operator/` *(pipeline health, storage usage, deployment status)*

> NOTE: Sibling paths are expected by convention; confirm the actual repo layout in your tree.

[Back to top](#top)

---

## Directory contents

This README documents the intended structure. Your repo may have fewer or different files.

```text
configs/
└─ observability/
   └─ dashboards/
      └─ product/                                    # Product-facing dashboards (usage + UX + performance)
         ├─ README.md                                 # Purpose, ownership, and how dashboards are validated/deployed
         │
         ├─ dashboards/                               # Dashboard definitions (JSON/YAML) — preferred source of truth
         ├─ panels/                                   # Optional reusable panel snippets (shared queries/visuals)
         ├─ assets/                                   # Optional screenshots/thumbnails for docs/PR review
         │
         └─ registry.yaml                             # Recommended: dashboard registry (CI discovery + deploy wiring)
```

### Acceptable inputs

- Dashboard definitions for **product view** signals:
  - UI performance trends and regressions
  - A11y regression indicators
  - UX-critical path health (map load, search, evidence drawer, exports)
- Reusable panel snippets and variables (optional)
- Lightweight documentation assets (screenshots)

### Exclusions

- **Secrets** (datasource credentials, tokens, API keys)
- **PII or user identifiers** (raw IPs, emails, session IDs tied to a person). Use aggregates.
- Steward/operator-only dashboards (keep those in their view folders)
- One-off, environment-specific dashboard edits that aren’t reproducible via GitOps

[Back to top](#top)

---

## Dashboard registry

To keep dashboards discoverable and CI-checkable, maintain a small registry (recommended).

### Suggested registry fields

If you use `registry.yaml`, aim for:

- stable `dashboard_id`
- `owner` (team/role)
- `purpose` (one sentence)
- `primary_signals`
- `datasources` (logical names, not secrets)
- `slo_or_thresholds` (link or inline)
- `links` (runbooks, playbooks)

Example (schema is intentionally lightweight):

```yaml
# registry.yaml (example)
dashboards:
  - dashboard_id: kfm-product-overview
    file: dashboards/kfm-product-overview.json
    owner: kfm-platform-observability
    purpose: "Top-line UX health and release regression signals."
    primary_signals:
      - "UI availability"
      - "Frontend error rate"
      - "Core UX latency percentiles"
      - "A11y regression trend"
    datasources:
      - metrics
      - logs
      - traces
    slo_or_thresholds:
      - "TODO: link to SLO doc or inline thresholds"
    links:
      runbook: "TODO"
      incident_playbook: "TODO"
```

### Starter dashboard set (proposed)

Replace these with the actual dashboards you ship.

| Dashboard ID | Example file | Primary signals | Notes |
|---|---|---|---|
| `kfm-product-overview` | `dashboards/kfm-product-overview.json` | UX health rollup, regression flags | Landing page for product/on-call |
| `kfm-ui-performance` | `dashboards/kfm-ui-performance.json` | Route latency, map load, tile latency | Slice by release + route |
| `kfm-a11y-regressions` | `dashboards/kfm-a11y-regressions.json` | Automated a11y checks, score trends | Tracks keyboard nav + ARIA coverage |
| `kfm-frontend-errors` | `dashboards/kfm-frontend-errors.json` | JS errors, API failures surfaced to UI | Connect to release + route |
| `kfm-evidence-drawer-ux` | `dashboards/kfm-evidence-drawer-ux.json` | Evidence drawer latency + failure rate | Evidence UX is a trust surface |

[Back to top](#top)

---

## Signals and dimensions

Product dashboards should be optimized for answering two questions fast:

1. **Did the user experience regress?** (what changed, when, where)
2. **Where do we look next?** (which layer: UI, API, tiles, evidence, policy boundary)

### Minimum signals (product view focus)

**UI performance indicators**
- Page/route latency percentiles (P50/P95) for key flows
- Map load time (initial + interaction)
- Tile request latency and errors (as experienced by UI)
- Evidence drawer open/resolve latency
- Export latency and failures (when exports are available)

**A11y regression indicators**
- Automated accessibility check trend (pass/fail, counts by severity)
- Keyboard navigation smoke checks (critical flows)
- ARIA coverage checks for map controls + key widgets
- “Color-only meaning” regressions (status badges / indicators must have text labels)

> TIP: Treat these as *signals*, not a single “score.” The goal is to quickly isolate regressions.

### Standard dimensions to keep dashboards debuggable

Prefer panels/queries that can be broken down by:

- **environment** (dev/stage/prod)
- **release identifier** (e.g., `commit_sha`, build id, or semantic version)
- **route / UI surface** (e.g., `/explore`, `/story/:id`)
- **component** (map, search, evidence drawer, export)
- **status** (`ok`, `error`, `denied`, etc., aggregated)

If your telemetry supports it, preserve correlation paths via:
- `correlation_id` (request/interaction correlation)
- `audit_ref` (links UX events to governed audit trails)

[Back to top](#top)

---

## Conventions

### 1) Determinism and stable diffs

Dashboards are configuration. Prefer **stable formatting** and deterministic identifiers so diffs are meaningful.

**Do:**
- canonicalize JSON/YAML ordering/formatting
- keep dashboard IDs stable across edits
- prefer small, reversible changes

**Don’t:**
- commit tool-generated noise (reordered keys, random UIDs) without canonicalization

### 2) Tagging

Add tags/labels that make dashboards filterable by view and ownership. Example tags:

- `kfm`
- `view:product`
- `area:observability`
- `component:ui` / `component:map` / `component:evidence` / `component:export`
- `owner:<team>`

### 3) Privacy and policy posture

Product dashboards must be safe by default.

- Collect and display **aggregate metrics** wherever possible.
- Redact or avoid **PII** in logs/events used for dashboards.
- Avoid “leaky” dimensions that reveal restricted facts (e.g., unique identifiers that map to sensitive records).

If you need user-level debugging, do it behind strict access controls and retention limits, and keep this directory free of those configs.

[Back to top](#top)

---

## Change process

This repo treats operational config as a governed, reviewable artifact (GitOps-friendly).

### Adding or updating a dashboard

1. **Create/edit** the dashboard definition under `dashboards/`
2. **Update** `registry.yaml` (if present) so the dashboard is discoverable
3. **Canonicalize** the dashboard format (avoid diff noise)
4. **Add/refresh** a screenshot in `assets/` (optional but helpful)
5. **Verify** in a preview environment (or local renderer) that:
   - panels load with expected filters
   - labels/dimensions work (environment, release, route)
   - no PII appears
6. **PR requirements**
   - purpose + intended audience stated
   - rollback note (what to revert if it breaks)
   - link to runbook/playbook (or create one)

### Suggested CI checks (recommended)

- schema validation for dashboard files (JSON/YAML)
- lint: stable formatting and deterministic IDs
- denylist: secrets patterns and PII fields
- registry validation: every registry entry points to an existing file

[Back to top](#top)

---

## Definition of done

Use this as a lightweight gate for dashboard PRs.

- [ ] Dashboard is in the **product view** scope (UI performance / a11y regression)
- [ ] Dashboard file is **deterministic** (canonical formatting; no random IDs)
- [ ] No secrets or PII are present in configs or committed examples
- [ ] Panels support **environment** + **release** breakdown
- [ ] A11y indicators include at least: keyboard nav checks + ARIA checks for key controls
- [ ] A short “how to read this dashboard” note exists (panel descriptions or README update)
- [ ] Optional: screenshot added/updated in `assets/`

[Back to top](#top)

---

## Troubleshooting

**Dashboards are empty**
- Check environment filters (labels often differ between dev/stage/prod)
- Confirm the data source is receiving UI telemetry (synthetic checks or RUM)
- Ensure release labels exist (otherwise regressions can’t be sliced by deploy)

**A11y dashboard shows regressions but no obvious code change**
- Confirm the a11y scanner version/config changed
- Check if route coverage expanded (new pages scanned)
- Validate that results are aggregated consistently (same severity mapping)

**Performance regression flagged**
- Slice by route/component to find the hotspot
- Check tile latency and error rates (map UX commonly degrades due to tile delivery)
- Correlate with API error rate and evidence resolver latency (trust surfaces depend on it)

[Back to top](#top)

---

## References

- *Kansas Frontier Matrix (KFM) — Definitive Design & Governance Guide (vNext)*  
  - Observability requirements (dashboards by view)  
  - Accessibility and inclusive design (minimum a11y requirements)  
  - Telemetry privacy guidance (aggregate metrics, redact PII)

- *KFM Integration Idea Pack (cultivated for ingestion)*  
  - Telemetry pattern: OpenTelemetry mapping and canonical keys

---
