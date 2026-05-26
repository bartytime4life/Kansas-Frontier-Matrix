<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid-pending>
title: PM Sensor Calibration Review Dashboard — specification
type: standard
version: v0.1
status: draft
owners: <atmosphere-domain-steward>  # PROPOSED placeholder; resolve before review
created: 2026-05-20
updated: 2026-05-20
policy_label: public
related:
  - docs/dashboards/README.md
  - docs/dashboards/domain/README.md
  - docs/dashboards/domain/atmosphere.md
  - docs/dashboards/DASHBOARD_CATALOG.md
  - docs/domains/
tags: [kfm, dashboards, domain, air, atmosphere, pm-sensor, calibration, air-quality]
notes:
  - "Source card: KFM-P30-FEAT-0001 (PM Sensor Calibration Review Dashboard) — UNCHANGED, active."
  - "Card self-check: UNKNOWN — repository implementation status remains unverified."
  - "Domain segment 'air' maps to the atmosphere domain — confirm against Directory Rules §6.1 docs/domains/."
  - "This is a SPEC for a dashboard, not the running dashboard."
[/KFM_META_BLOCK_V2] -->

# PM Sensor Calibration Review Dashboard · `domain/air/PM_SENSOR_CALIBRATION_REVIEW.md`

> Dashboard specification for the **PM Sensor Calibration Review Dashboard** (Atlas card
> `KFM-P30-FEAT-0001`). A domain dashboard for low-cost particulate-matter (PM) sensors:
> trust scores, meteorology features, co-location windows, and low-concentration
> safeguards.

![Authority](https://img.shields.io/badge/authority-PROPOSED-orange)
![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Category](https://img.shields.io/badge/category-domain%20%C2%B7%20air-teal)
![Source](https://img.shields.io/badge/source-KFM--P30--FEAT--0001-informational)
![Policy label](https://img.shields.io/badge/policy-public-brightgreen)

**Status:** draft · **Owners:** `<atmosphere-domain-steward>` (PROPOSED) · **Last reviewed:** 2026-05-20

---

> [!IMPORTANT]
> A calibrated reading is still an *estimate*. This dashboard reports calibration quality
> and a trust score; it does not turn a low-cost PM sensor into a reference monitor.
> Calibration provenance belongs in the reading's `EvidenceBundle`.

---

> [!NOTE]
> **Domain-segment placement.** This spec lives under `domain/air/`. The KFM canonical
> domain name is **atmosphere** (Directory Rules §6.1 `docs/domains/`). Whether the
> segment should be `air/` or `atmosphere/` is an open question — see `PMC-OQ-04`.

---

## 1. Description

The PM Sensor Calibration Review dashboard answers: **how much should we trust each PM
sensor's reading right now?** Low-cost PM sensors drift with humidity, temperature, and
aging. This dashboard surfaces calibration quality against co-located reference monitors,
the meteorology features used in the calibration model, and explicit safeguards for the
low-concentration regime where these sensors are least reliable.

## 2. Metrics surfaced (PROPOSED)

| # | Metric | Measures | Healthy posture (PROPOSED) | Negative state |
|---|---|---|---|---|
| 1 | Sensor trust score | A composite trust score per sensor from calibration fit + recency. | Above the per-network trust threshold. | `SENSOR_LOW_TRUST` |
| 2 | Meteorology features | Humidity / temperature features feeding the calibration model. | Present and within model-valid ranges. | `MET_FEATURE_MISSING` |
| 3 | Co-location window | Recency and length of co-location with a reference monitor. | Within the required co-location cadence. | `COLOCATION_STALE` |
| 4 | Low-concentration safeguard | Behavior in the low-concentration regime where PM sensors are least reliable. | Safeguard active; readings flagged or widened. | `LOW_CONC_UNSAFEGUARDED` |
| 5 | Calibration residual | Error vs. the co-located reference monitor. | Within the network's residual tolerance. | `CALIBRATION_RESIDUAL_HIGH` |

## 3. Panels (PROPOSED)

- **Trust scores** — per-sensor trust score vs. the network threshold.
- **Met features** — humidity/temperature feature availability and range checks.
- **Co-location** — last co-location window per sensor; stale windows flagged.
- **Low-concentration** — safeguard status and flagged low-concentration readings.
- **Residuals** — calibration residual vs. reference, against the tolerance band.

## 4. Inputs

Mounted-repo paths NEEDS VERIFICATION.

- PM sensor readings + calibration model outputs (atmosphere domain pipeline).
- Reference-monitor data for co-located sensors.
- Meteorology features (humidity, temperature) used by the calibration model.
- `ValidationReport` — calibration-check outcomes.
- `EvidenceBundle` — calibration provenance per reading.

## 5. Files

| Path | Role | spec_hash |
|---|---|---|
| `docs/dashboards/domain/air/PM_SENSOR_CALIBRATION_REVIEW.md` | This dashboard specification. | PROPOSED — pending JCS+SHA-256 |
| Running surface (PROPOSED) | `apps/review-console/` air-domain panel. | NEEDS VERIFICATION |

## 6. Ownership and review burden

- **Owning steward (PROPOSED):** Atmosphere (air) domain steward.
- **Review burden:** docs steward + atmosphere domain steward. Resolve the placeholder
  against Atlas v1.1 §24.7 before review.

## 7. Acceptance

- [ ] All five metrics present; the dashboard does not claim reference-grade accuracy.
- [ ] Owner named (no anonymous spec at v1).
- [ ] The `domain/<domain>/` segment matches a Directory Rules §6.1 `docs/domains/` name
      (or `PMC-OQ-04` is open).
- [ ] Link check passes; row present in [`DASHBOARD_CATALOG.md`](../../DASHBOARD_CATALOG.md).
- [ ] Negative states use the Unified Doctrine §19 vocabulary.

## 8. Open questions

- [ ] **PMC-OQ-01** — Confirm the running surface and downgrade if unverified.
- [ ] **PMC-OQ-02** — Set per-network trust thresholds and residual tolerances.
- [ ] **PMC-OQ-03** — Define the low-concentration regime boundary and safeguard rule.
- [ ] **PMC-OQ-04** — Confirm the domain segment name: `air/` vs. `atmosphere/`
      (Directory Rules §6.1 `docs/domains/`).
- [ ] **PMC-OQ-05** — Confirm `KFM-P30-FEAT-0001` implementation status against
      mounted-repo state (card self-check: UNKNOWN).

---

**Related docs:** [domain/README.md](../README.md) · [domain/atmosphere.md](../atmosphere.md) · [dashboards/README.md](../../README.md) · [DASHBOARD_CATALOG.md](../../DASHBOARD_CATALOG.md) ·
[domains/](../../../domains/)

**Last updated:** 2026-05-20 · **Edition:** v0.1 (draft) · **Owners:** `<atmosphere-domain-steward>` (PROPOSED)
