<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid-pending>
title: Dashboard Catalog — index of all KFM dashboard specifications
type: standard
version: v0.1
status: draft
owners: <dashboards-stewards>  # PROPOSED placeholder; resolve before review
created: 2026-05-20
updated: 2026-05-20
policy_label: public
related:
  - docs/dashboards/README.md
  - docs/dashboards/INDICATOR_CATALOG.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
tags: [kfm, docs, dashboards, catalog, index]
notes:
  - "Every dashboard spec under docs/dashboards/ MUST appear in this catalog."
  - "Each spec is PROPOSED until mounted-repo evidence confirms a running implementation."
[/KFM_META_BLOCK_V2] -->

# Dashboard Catalog · `docs/dashboards/DASHBOARD_CATALOG.md`

> The single index of every dashboard specification under `docs/dashboards/`. Each row
> links a spec file to its category, its source Atlas card or indicator section, its
> owning steward (PROPOSED), and where the dashboard actually runs.

![Authority](https://img.shields.io/badge/authority-PROPOSED-orange)
![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Truth posture](https://img.shields.io/badge/truth-cite--or--abstain-blue)
![Policy label](https://img.shields.io/badge/policy-public-brightgreen)
![Specs](https://img.shields.io/badge/specs-24%20proposed-yellow)

**Status:** draft · **Owners:** `<dashboards-stewards>` (PROPOSED) · **Last reviewed:** 2026-05-20

---

> [!IMPORTANT]
> Every dashboard spec carries its own truth posture. The dashboards indexed here are
> **PROPOSED designs**, not claims of running surfaces. A spec moves from PROPOSED to
> a verified status only when mounted-repo evidence confirms a running implementation.

---

## Quick jump

- [1. How to use this catalog](#1-how-to-use-this-catalog)
- [2. Governance dashboards](#2-governance-dashboards)
- [3. Operational dashboards](#3-operational-dashboards)
- [4. Domain dashboards](#4-domain-dashboards)
- [5. Observability dashboards](#5-observability-dashboards)
- [6. Lifecycle states](#6-lifecycle-states)
- [7. Open questions](#7-open-questions)

---

## 1. How to use this catalog

- **Adding a dashboard?** Author the spec under the right category folder (see
  [README §10](README.md#10-quickstart--authoring-a-dashboard-spec)), then add a row here.
- **Auditing coverage?** Cross-check against [`INDICATOR_CATALOG.md`](INDICATOR_CATALOG.md)
  — every Atlas v1.1 §24.11 indicator must be surfaced by some governance dashboard.
- **Statuses** use the lifecycle vocabulary in [§6](#6-lifecycle-states).

[↑ back to top](#dashboard-catalog--docsdashboardsdashboard_catalogmd)

---

## 2. Governance dashboards

Governance-health dashboards mirror Atlas v1.1 Ch. 24.11. They **report** posture; the
validator **enforces**.

| Spec file | Documents | Source | Owner (PROPOSED) | Runs on (PROPOSED) | Status |
|---|---|---|---|---|---|
| [`governance/EVIDENCE_INTEGRITY.md`](governance/EVIDENCE_INTEGRITY.md) | EvidenceRef resolution, cite-or-abstain compliance, source-role drift, stale-source rate, quarantine throughput. | Atlas v1.1 §24.11.1 | Release / Source / AI surface stewards | `apps/review-console/` | PROPOSED |
| [`governance/RELEASE_CORRECTION_ROLLBACK.md`](governance/RELEASE_CORRECTION_ROLLBACK.md) | Rollback-target coverage, correction lead time, derivative-invalidation coverage, rollback rehearsal rate, supersession lineage gaps. | Atlas v1.1 §24.11.2 | Release steward · Correction reviewer | `apps/review-console/` | PROPOSED |
| [`governance/SENSITIVITY_RIGHTS.md`](governance/SENSITIVITY_RIGHTS.md) | Sensitive-lane fail-closed rate, RedactionReceipt coverage, review-aged-out incidence, rights-change response time, side-channel audit cadence. | Atlas v1.1 §24.11.3 | Sensitivity reviewer · Rights-holder representative | `apps/review-console/` | PROPOSED |
| [`governance/AI_SURFACE_HEALTH.md`](governance/AI_SURFACE_HEALTH.md) | AIReceipt presence rate, ABSTAIN rate by template, DENY reason distribution, synthetic-claim incidence. | Atlas v1.1 §24.11.4 | AI surface steward | `apps/review-console/` | PROPOSED |
| [`governance/DOCUMENTATION_DRIFT.md`](governance/DOCUMENTATION_DRIFT.md) | ADR completeness, drift register size, per-root README presence, atlas/supplement lineage clarity. | Atlas v1.1 §24.11.5 | Docs steward | `apps/review-console/` | PROPOSED |

[↑ back to top](#dashboard-catalog--docsdashboardsdashboard_catalogmd)

---

## 3. Operational dashboards

Feed, artifact, and QC dashboards. They watch the pipeline's day-to-day health.

| Spec file | Documents | Source | Owner (PROPOSED) | Runs on (PROPOSED) | Status |
|---|---|---|---|---|---|
| [`operational/SLO_LIVE_FEEDS.md`](operational/SLO_LIVE_FEEDS.md) | Standards-first SLOs for live transit and other high-cadence feeds: freshness, schema validation, latency, deduplication, non-material suppression, agency license terms. | `KFM-P11-FEAT-0002` | Source steward · Observability steward | OpenTelemetry stack / `apps/review-console/` | PROPOSED |
| [`operational/REALTIME_FEED_FRESHNESS.md`](operational/REALTIME_FEED_FRESHNESS.md) | Realtime feed health: schema validation, SLO freshness, canonical identity, partition output, promotion/hold state. | `KFM-P31-FEAT-0015` | Source steward | OpenTelemetry stack / `apps/review-console/` | PROPOSED |
| [`operational/COG_ZARR_REPRODUCIBILITY.md`](operational/COG_ZARR_REPRODUCIBILITY.md) | Raster/datacube artifacts: build container, GDAL/numcodecs versions, chained hashes, overview/block layout, reproducibility verdict. | `KFM-P31-FEAT-0016` | Pipeline steward | `apps/review-console/` | PROPOSED |
| [`operational/GEOSPATIAL_QC_PANEL.md`](operational/GEOSPATIAL_QC_PANEL.md) | Quick geospatial QC panel — fast inspectable surface for geometry / CRS / topology checks. | `KFM-P31-FEAT-0017` | Pipeline steward · Domain steward | `apps/review-console/` | PROPOSED |

[↑ back to top](#dashboard-catalog--docsdashboardsdashboard_catalogmd)

---

## 4. Domain dashboards

Domain-specific dashboards live under `domain/<domain>/`. The `<domain>` segment MUST
match a Directory Rules §6.1 `docs/domains/` name.

| Spec file | Documents | Source | Owner (PROPOSED) | Runs on (PROPOSED) | Status |
|---|---|---|---|---|---|
| [`domain/hydrology.md`](domain/hydrology.md) | Per-domain instance of §24.11 for hydrology: EvidenceRef resolution, rollback coverage, correction lead time, derivative invalidation, documentation drift. | Atlas v1.1 §24.11.1 / §24.11.2 / §24.11.5 | Hydrology domain steward | `apps/review-console/` | PROPOSED |
| [`domain/soil.md`](domain/soil.md) | Per-domain instance of §24.11 for soil: evidence resolution, source-role drift, taxonomy-edition skew, MUKEY stability. | Atlas v1.1 §24.11.1 / §24.11.5 | Soil domain steward | `apps/review-console/` | PROPOSED |
| [`domain/habitat.md`](domain/habitat.md) | Per-domain instance of §24.11 for habitat: evidence integrity plus sensitive-lane gating on habitat × sensitive-species intersection. | Atlas v1.1 §24.11.1 / §24.11.3 | Habitat domain steward · Sensitivity reviewer | `apps/review-console/` | PROPOSED |
| [`domain/fauna.md`](domain/fauna.md) | Per-domain instance of §24.11 for fauna (T4 defaults): fail-closed rate, redaction coverage, rights-change response, side-channel audit. | Atlas v1.1 §24.11.3 / §24.11.1 | Fauna domain steward · Sensitivity reviewer · Rights-holder rep | `apps/review-console/` | PROPOSED |
| [`domain/flora.md`](domain/flora.md) | Per-domain instance of §24.11 for flora (T4 defaults for poaching-vulnerable taxa): fail-closed, voucher coverage, poaching-pattern audit. | Atlas v1.1 §24.11.3 / §24.11.1 | Flora domain steward · Sensitivity reviewer · Rights-holder rep | `apps/review-console/` | PROPOSED |
| [`domain/agriculture.md`](domain/agriculture.md) | Per-domain instance of §24.11 for agriculture: evidence resolution, NASS suppression-rule compliance, CDL taxonomy skew, irrigation classification confidence. | Atlas v1.1 §24.11.1 / §24.11.5 | Agriculture domain steward | `apps/review-console/` | PROPOSED |
| [`domain/geology.md`](domain/geology.md) | Per-domain instance of §24.11 for geology / natural resources: source breadth, stratigraphic canonicalization, well-record identifiability gate. | Atlas v1.1 §24.11.1 | Geology domain steward | `apps/review-console/` | PROPOSED |
| [`domain/atmosphere.md`](domain/atmosphere.md) | Per-domain instance of §24.11 for atmosphere / air: source posture plus AI-surface forecasting cite-or-abstain, ABSTAIN by template, synthetic-claim incidence. | Atlas v1.1 §24.11.1 / §24.11.4 | Atmosphere domain steward · AI-surface steward | `apps/review-console/` | PROPOSED |
| [`domain/hazards.md`](domain/hazards.md) | Per-domain instance of §24.11 for hazards: rollback coverage, correction lead time, alert-authority DENY rate, derivative invalidation cascade. | Atlas v1.1 §24.11.2 / §24.11.1 | Hazards domain steward · Release steward | `apps/review-console/` | PROPOSED |
| [`domain/roads-rail-trade.md`](domain/roads-rail-trade.md) | Per-domain instance of §24.11 for roads / rail / trade routes: source breadth, functional-class canonicalization, historical-corpus edition pinning; rolls up transit SLOs. | Atlas v1.1 §24.11.1 / §24.11.5 | Roads-rail-trade domain steward · Source steward | `apps/review-console/` | PROPOSED |
| [`domain/settlements-infrastructure.md`](domain/settlements-infrastructure.md) | Per-domain instance of §24.11 for settlements / infrastructure (critical-asset T4): fail-closed gate, redaction coverage, rollback coverage, service-area cascade. | Atlas v1.1 §24.11.3 / §24.11.2 | Settlements-infrastructure domain steward · Sensitivity reviewer | `apps/review-console/` | PROPOSED |
| [`domain/archaeology.md`](domain/archaeology.md) | Per-domain instance of §24.11 for archaeology / cultural heritage (T4 defaults, sovereignty): sovereignty review presence, NAGPRA-flag completeness, side-channel audit. | Atlas v1.1 §24.11.3 / §24.11.1 | Archaeology domain steward · Sensitivity reviewer · Sovereignty rep | `apps/review-console/` | PROPOSED |
| [`domain/people-dna-land.md`](domain/people-dna-land.md) | Per-domain instance of §24.11 for people / genealogy / DNA / land ownership (living-person T4, DNA T4): fail-closed, rights-change response time, AIReceipt presence, synthetic-claim incidence (target zero). | Atlas v1.1 §24.11.3 / §24.11.4 / §24.11.1 | People-DNA-land domain steward · Sensitivity reviewer · AI-surface steward · Rights-holder rep | `apps/review-console/` | PROPOSED |
| [`domain/air/PM_SENSOR_CALIBRATION_REVIEW.md`](domain/air/PM_SENSOR_CALIBRATION_REVIEW.md) | PM-sensor trust scores, meteorology features, co-location windows, low-concentration safeguards. | `KFM-P30-FEAT-0001` | Atmosphere domain steward | `apps/review-console/` | PROPOSED |

[↑ back to top](#dashboard-catalog--docsdashboardsdashboard_catalogmd)

---

## 5. Observability dashboards

CI / pipeline observability surfaces — the stack the other dashboards may read from.

| Spec file | Documents | Source | Owner (PROPOSED) | Runs on (PROPOSED) | Status |
|---|---|---|---|---|---|
| [`observability/OPENTELEMETRY_STACK.md`](observability/OPENTELEMETRY_STACK.md) | CI/pipeline observability via OpenTelemetry Collector → Tempo (traces) + Mimir (metrics) + Loki (logs), one agent shape across runners. | `KFM-P8-PROG-0026` | Observability steward | OpenTelemetry stack (Tempo · Mimir · Loki) | PROPOSED |

[↑ back to top](#dashboard-catalog--docsdashboardsdashboard_catalogmd)

---

## 6. Lifecycle states

PROPOSED vocabulary for the **Status** column. Aligns with the Atlas truth labels and
Directory Rules §17.

| Status | Meaning |
|---|---|
| `PROPOSED` | Spec drafted; no verified running implementation. Default for every new spec. |
| `NEEDS VERIFICATION` | Spec claims a running surface, but mounted-repo evidence is not yet confirmed. |
| `CONFIRMED` | Mounted-repo evidence confirms the dashboard runs and reads the receipts named in the spec. |
| `SUPERSEDED` | Replaced by another spec; the row keeps a forward link to its successor. |
| `RETIRED` | Dashboard decommissioned; spec kept for lineage. |

[↑ back to top](#dashboard-catalog--docsdashboardsdashboard_catalogmd)

---

## 7. Open questions

- [ ] **CAT-OQ-01 — Catalog completeness CI.** Add a check that every `.md` under
  `docs/dashboards/{governance,operational,domain,observability}/` has a row here.
- [ ] **CAT-OQ-02 — Running-surface verification.** Confirm each "Runs on" value against
  mounted-repo state; downgrade unverified rows to `NEEDS VERIFICATION`.
- [ ] **CAT-OQ-03 — Owner reconciliation.** Resolve every PROPOSED owner against
  Atlas v1.1 §24.7 (tracked with `DASH-OQ-04`).

[↑ back to top](#dashboard-catalog--docsdashboardsdashboard_catalogmd)

---

**Related docs:** [README.md](README.md) · [INDICATOR_CATALOG.md](INDICATOR_CATALOG.md) ·
[registers/DRIFT_REGISTER.md](../registers/DRIFT_REGISTER.md)

**Last updated:** 2026-05-20 · **Edition:** v0.1 (draft) · **Owners:** `<dashboards-stewards>` (PROPOSED)
