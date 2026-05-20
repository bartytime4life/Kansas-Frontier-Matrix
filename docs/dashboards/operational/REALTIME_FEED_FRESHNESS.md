<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid-pending>
title: Realtime Feed Freshness Monitor — specification
type: standard
version: v0.1
status: draft
owners: <source-steward>  # PROPOSED placeholder; resolve before review
created: 2026-05-20
updated: 2026-05-20
policy_label: public
related:
  - docs/dashboards/README.md
  - docs/dashboards/DASHBOARD_CATALOG.md
  - docs/dashboards/operational/SLO_LIVE_FEEDS.md
  - docs/dashboards/observability/OPENTELEMETRY_STACK.md
  - docs/standards/SMART_SYNC.md
tags: [kfm, dashboards, operational, realtime, freshness, promotion, partitions]
notes:
  - "Source card: KFM-P31-FEAT-0015 (Realtime Feed Freshness Monitor) — UNCHANGED, active."
  - "Card self-check: UNKNOWN — repository implementation status remains unverified."
  - "This is a SPEC for a dashboard, not the running dashboard."
[/KFM_META_BLOCK_V2] -->

# Realtime Feed Freshness Monitor · `operational/REALTIME_FEED_FRESHNESS.md`

> Dashboard specification for the **Realtime Feed Freshness Monitor** (Atlas card
> `KFM-P31-FEAT-0015`). Tracks schema validation, SLO freshness, canonical identity,
> partition output, and promotion/hold state for realtime feeds.

![Authority](https://img.shields.io/badge/authority-PROPOSED-orange)
![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Category](https://img.shields.io/badge/category-operational-blueviolet)
![Source](https://img.shields.io/badge/source-KFM--P31--FEAT--0015-informational)
![Policy label](https://img.shields.io/badge/policy-public-brightgreen)

**Status:** draft · **Owners:** `<source-steward>` (PROPOSED) · **Last reviewed:** 2026-05-20

---

> [!IMPORTANT]
> "Fresh" means recently ingested and well-formed. It does not mean "promoted." This
> dashboard shows promotion/hold state explicitly so freshness is never mistaken for
> admission into a PUBLISHED surface.

---

## 1. Description

The Realtime Feed Freshness Monitor answers: **for each realtime feed, is the latest data
recent, schema-valid, correctly identified, correctly partitioned, and is it held or
promoted?** It complements [`SLO_LIVE_FEEDS.md`](SLO_LIVE_FEEDS.md): SLO_LIVE_FEEDS
tracks SLO targets against published standards; this monitor tracks per-feed pipeline
state through to the promotion gate.

## 2. Metrics surfaced (PROPOSED)

| # | Metric | Measures | Healthy posture (PROPOSED) | Negative state |
|---|---|---|---|---|
| 1 | Schema validation | % of realtime messages passing schema validation. | ~100%. | `SCHEMA_INVALID` |
| 2 | SLO freshness | Age of the latest message vs. the feed's freshness SLO. | Within SLO. | `SOURCE_STALE` |
| 3 | Canonical identity | % of records resolving to a stable canonical identity. | 100%. | `IDENTITY_UNRESOLVED` |
| 4 | Partition output | Whether each ingest writes the expected partition layout. | Expected partitions present and complete. | `PARTITION_INCOMPLETE` |
| 5 | Promotion / hold state | Whether the feed's latest window is promoted or held. | Held only with a documented reason. | `REVIEW_PENDING` / `PROMOTION_HELD` |

## 3. Panels (PROPOSED)

- **Schema validation** — per-feed pass rate, failures linked to `ValidationReport`.
- **Freshness** — per-feed age vs. SLO line.
- **Canonical identity** — % resolved; unresolved records drill out.
- **Partition map** — expected vs. observed partitions per ingest window.
- **Promotion board** — per-feed promoted / held state with hold reason.

## 4. Inputs

Mounted-repo paths NEEDS VERIFICATION.

- Connector run telemetry — fetch and ingest timestamps (`connectors/`).
- `ValidationReport` — schema validation and identity-resolution outcomes.
- Partition manifests — expected vs. observed partition layout.
- Promotion gate records — promoted / held state and hold reasons.

## 5. Files

| Path | Role | spec_hash |
|---|---|---|
| `docs/dashboards/operational/REALTIME_FEED_FRESHNESS.md` | This dashboard specification. | PROPOSED — pending JCS+SHA-256 |
| Running surface (PROPOSED) | OpenTelemetry-backed surface / `apps/review-console/`. | NEEDS VERIFICATION |

## 6. Ownership and review burden

- **Owning steward (PROPOSED):** Source steward.
- **Review burden:** docs steward + source steward. Resolve the placeholder against
  Atlas v1.1 §24.7 before review.

## 7. Acceptance

- [ ] All five metrics present; promotion/hold state is explicit and distinct from freshness.
- [ ] Owner named (no anonymous spec at v1).
- [ ] Link check passes; row present in [`DASHBOARD_CATALOG.md`](../DASHBOARD_CATALOG.md).
- [ ] Negative states use the Unified Doctrine §19 vocabulary.

## 8. Open questions

- [ ] **RFF-OQ-01** — Confirm the running surface and downgrade if unverified.
- [ ] **RFF-OQ-02** — Reconcile scope overlap with [`SLO_LIVE_FEEDS.md`](SLO_LIVE_FEEDS.md);
      decide whether they merge into one operational feed surface.
- [ ] **RFF-OQ-03** — Confirm `KFM-P31-FEAT-0015` implementation status against
      mounted-repo state (card self-check: UNKNOWN).

---

**Related docs:** [README.md](../README.md) · [DASHBOARD_CATALOG.md](../DASHBOARD_CATALOG.md) ·
[operational/SLO_LIVE_FEEDS.md](SLO_LIVE_FEEDS.md) ·
[observability/OPENTELEMETRY_STACK.md](../observability/OPENTELEMETRY_STACK.md)

**Last updated:** 2026-05-20 · **Edition:** v0.1 (draft) · **Owners:** `<source-steward>` (PROPOSED)
