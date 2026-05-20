<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid-pending>
title: Live-Feeds SLO Dashboard — specification
type: standard
version: v0.1
status: draft
owners: <source-steward>, <observability-steward>  # PROPOSED placeholders; resolve before review
created: 2026-05-20
updated: 2026-05-20
policy_label: public
related:
  - docs/dashboards/README.md
  - docs/dashboards/DASHBOARD_CATALOG.md
  - docs/dashboards/observability/OPENTELEMETRY_STACK.md
  - docs/standards/TELEMETRY_MINIMUMS.md
  - docs/standards/connector-rate-limits.md
tags: [kfm, dashboards, operational, slo, live-feeds, gtfs-rt, freshness]
notes:
  - "Source card: KFM-P11-FEAT-0002 (Standards-first SLO dashboard for live feeds) — EXPANDED, active."
  - "Card self-check: UNKNOWN — repository implementation status remains unverified."
  - "This is a SPEC for a dashboard, not the running dashboard."
[/KFM_META_BLOCK_V2] -->

# Live-Feeds SLO Dashboard · `operational/SLO_LIVE_FEEDS.md`

> Dashboard specification for **standards-first SLOs on live, high-cadence feeds**
> (Atlas card `KFM-P11-FEAT-0002`). Covers live transit and similar feeds: freshness,
> schema validation, latency, deduplication, non-material suppression, and agency
> license terms.

![Authority](https://img.shields.io/badge/authority-PROPOSED-orange)
![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Category](https://img.shields.io/badge/category-operational-blueviolet)
![Source](https://img.shields.io/badge/source-KFM--P11--FEAT--0002-informational)
![Policy label](https://img.shields.io/badge/policy-public-brightgreen)

**Status:** draft · **Owners:** `<source-steward>`, `<observability-steward>` (PROPOSED) · **Last reviewed:** 2026-05-20

---

> [!IMPORTANT]
> SLOs are **operational targets**, not trust claims. A feed meeting its SLO is fresh and
> well-formed — it is not thereby *admitted*. Admission still runs through the validator.

---

## 1. Description

The Live-Feeds SLO dashboard answers: **are our high-cadence external feeds healthy
against published, standards-first service-level objectives?** It is "standards-first"
because each SLO is anchored to a published spec (e.g., GTFS-Realtime) and to the source
agency's license terms — not to ad-hoc thresholds.

## 2. Metrics surfaced (PROPOSED)

| # | Metric | Measures | Healthy posture (PROPOSED) | Negative state |
|---|---|---|---|---|
| 1 | Feed freshness | Age of the most recent successfully-ingested message vs. the feed's cadence. | Within the feed's declared cadence. | `SOURCE_STALE` |
| 2 | Schema validation rate | % of fetched messages passing schema validation. | ~100%; sustained failures are a defect. | `SCHEMA_INVALID` |
| 3 | Fetch latency | Time from scheduled fetch to ingest completion. | Within the per-feed latency budget. | `LATENCY_BUDGET_EXCEEDED` |
| 4 | Deduplication rate | % of messages dropped as duplicates. | Stable; spikes investigated. | `DEDUP_ANOMALY` |
| 5 | Non-material suppression | Updates suppressed as non-material (no meaningful change). | Visibly tracked; high rates reviewed. | — (informational) |
| 6 | License-terms compliance | Whether ingest respects the agency's license / attribution / rate terms. | 100% compliant. | `LICENSE_VIOLATION` |

## 3. Panels (PROPOSED)

- **Freshness** — per-feed age vs. cadence, with the SLO line.
- **Schema validation** — pass-rate trend, failures linked to `ValidationReport`.
- **Latency** — p50 / p95 fetch-to-ingest, against the per-feed budget.
- **Dedup & suppression** — duplicate and non-material rates side by side.
- **License compliance** — per-agency status with attribution / rate-limit checks.

## 4. Inputs

Mounted-repo paths NEEDS VERIFICATION.

- Connector run telemetry — fetch timestamps, latencies, message counts (`connectors/`).
- `ValidationReport` — schema-validation outcomes per message.
- Source descriptors — feed cadence, latency budget, license terms.
- OpenTelemetry stack metrics — see [`observability/OPENTELEMETRY_STACK.md`](../observability/OPENTELEMETRY_STACK.md).

## 5. Files

| Path | Role | spec_hash |
|---|---|---|
| `docs/dashboards/operational/SLO_LIVE_FEEDS.md` | This dashboard specification. | PROPOSED — pending JCS+SHA-256 |
| Running surface (PROPOSED) | OpenTelemetry-backed surface / `apps/review-console/`. | NEEDS VERIFICATION |

## 6. Ownership and review burden

- **Owning stewards (PROPOSED):** Source steward (feed health), Observability steward
  (telemetry plumbing).
- **Review burden:** docs steward + the owning stewards. Resolve placeholders against
  Atlas v1.1 §24.7 before review.

## 7. Acceptance

- [ ] Every SLO is anchored to a published standard and the source's license terms.
- [ ] Owners named (no anonymous spec at v1).
- [ ] Link check passes; row present in [`DASHBOARD_CATALOG.md`](../DASHBOARD_CATALOG.md).
- [ ] Negative states use the Unified Doctrine §19 vocabulary.

## 8. Open questions

- [ ] **SLF-OQ-01** — Confirm the running surface (OTEL-backed vs. review-console).
- [ ] **SLF-OQ-02** — Set per-feed cadence and latency budgets; source from descriptors.
- [ ] **SLF-OQ-03** — Confirm `KFM-P11-FEAT-0002` implementation status against
      mounted-repo state (card self-check: UNKNOWN).

---

**Related docs:** [README.md](../README.md) · [DASHBOARD_CATALOG.md](../DASHBOARD_CATALOG.md) ·
[observability/OPENTELEMETRY_STACK.md](../observability/OPENTELEMETRY_STACK.md) ·
[standards/TELEMETRY_MINIMUMS.md](../../standards/TELEMETRY_MINIMUMS.md)

**Last updated:** 2026-05-20 · **Edition:** v0.1 (draft) · **Owners:** `<source-steward>`, `<observability-steward>` (PROPOSED)
