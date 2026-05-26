<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-domain-atmosphere
title: Atmosphere / Air Dashboard Specification (PROPOSED lane; per-domain instance of Atlas §24.11)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: atmosphere-domain steward + AI-surface steward + governance-health steward
created: 2026-05-26
updated: 2026-05-26
policy_label: public
related:
  - kfm://doc/dashboards-domain-readme
  - kfm://doc/atlas-v1-1
  - kfm://doc/atlas-v1-1-ch24-5-sensitivity-tier-reference
  - kfm://doc/atlas-v1-1-ch24-6-pipeline-gate-reference
  - kfm://doc/domains-atmosphere-dossier                     # CONFIRMED dossier home: docs/domains/atmosphere/
  - kfm://doc/dashboards-domain-air-pm-sensor-calibration    # CONFIRMED sibling: domain/air/PM_SENSOR_CALIBRATION_REVIEW.md
  - kfm://adr/dashboards-lane-existence                      # PROPOSED candidate: OPEN-DASH-01
tags: [kfm, dashboards, domain, atmosphere, air, ai-surface, indicators, governance-health, specification]
notes:
  - Per-domain instance of Atlas v1.1 §24.11. Specification only; not an implementation.
  - Atmosphere is the home for AI-surface forecasting (cite-or-abstain emphasis); air-quality sub-surfaces live under domain/air/.
  - Atlas §24.11 wins on indicator conflicts; atmosphere dossier wins on context conflicts.
[/KFM_META_BLOCK_V2] -->

# Atmosphere / Air Dashboard Specification

<!-- [doc: kfm://doc/dashboards-domain-atmosphere] -->
<a id="top"></a>

> Per-domain dashboard specification for **Atmosphere / Air** (Atlas v1.0 Ch. 11). Weather observations, climate normals, forecasts, air-quality, drought indices. Carries an **AI-surface forecasting cite-or-abstain emphasis** beyond the standard evidence indicators.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Atlas chapter: Ch. 11" src="https://img.shields.io/badge/atlas-Ch.%2011-purple">
  <img alt="Indicator emphasis: 24.11.1 / 24.11.4" src="https://img.shields.io/badge/emphasis-24.11.1%20%C2%B7%2024.11.4-informational">
  <img alt="Policy label: public" src="https://img.shields.io/badge/policy--label-public-lightgrey">
</p>

> [!IMPORTANT]
> **Truth posture.** Indicators PROPOSED; instances PROPOSED; lane PROPOSED (OPEN-DASH-01); implementation NEEDS VERIFICATION.

> [!CAUTION]
> **Forecast vs. observation.** Atmospheric forecasts are **derived AI/numerical claims**. They must cite the model run + boundary conditions or abstain. The dashboard's AI-surface-health indicators apply specifically to forecasting and downscaled-model emissions.

> [!NOTE]
> **Sub-surfaces.** Air-quality / PM-sensor sub-dashboards live under `domain/air/` (currently: [`domain/air/PM_SENSOR_CALIBRATION_REVIEW.md`](./air/PM_SENSOR_CALIBRATION_REVIEW.md)). The relationship between this domain-scoped spec and the per-card sub-surfaces is OPEN-DASH-ATMOS-03.

---

## 1. Domain scope

- **Atlas chapter:** v1.0 Ch. 11 (Atmosphere / Air).
- **Default sensitivity tier(s):** T1 (public weather / air-quality observations and forecasts).
- **Pipeline shape:** Standard intake → validation → derive → publish; forecast emissions carry an **AI-surface gate** requiring `AIReceipt` with model-run, boundary conditions, and cite-or-abstain.
- **Dossier:** `docs/domains/atmosphere/` — `K.` validators (station QC, calibration, forecast verification), `M.` correction posture for re-analysis revisions.

[↑ back to top](#top)

---

## 2. Indicator subset

Emphasis per README §5.1: **Evidence-and-source · AI-surface-health (forecasting cite-or-abstain)**.

| Indicator | §24.11 cat. | Domain-scale healthy posture | Receipt / signal source |
|:---|:---|:---|:---|
| EvidenceRef resolution rate | 24.11.1 | > 99.9% across NOAA / ASOS / Mesonet / EPA AQS / KS Mesonet cites; per-source rate visible. | `ValidationReport`, EvidenceBundle index |
| Source-role distribution drift | 24.11.1 | Observation-vs-model role split tracked; downscaled-product role explicit, never silent. | Source descriptors |
| Stale source rate | 24.11.1 | Sub-hourly cadence sources monitored; outage dispositioned within tolerance. | Source descriptors, freshness cadence metadata |
| Quarantine throughput | 24.11.1 | Cause distribution visible (sensor flag, range check, derived-product schema); no sustained backlog. | `ValidationReport`, quarantine ledger |
| **AIReceipt presence rate** | 24.11.4 | **100%** on every forecast / downscaled-model emission to a public surface. | `AIReceipt` |
| **ABSTAIN rate by template** | 24.11.4 | Tracked per forecast horizon and per-variable; no template silently drops abstain. | `AIReceipt`, prompt registry |
| DENY reason distribution | 24.11.4 | Forecast denials surface model-run-stale / boundary-mismatch causes; trend tracked. | `PolicyDecision` |
| Synthetic-claim incidence | 24.11.4 | Zero unverified forecast claims (e.g., AI text inventing a heat-index value not in the model output). | `AIReceipt`, audit logs |
| Cite-or-abstain compliance | 24.11.1 / 24.11.4 | 100% on all AI-derived atmospheric text (forecast summaries, drought commentary). | `AIReceipt` |

[↑ back to top](#top)

---

## 3. Domain-specific indicators (PROPOSED)

| PROPOSED indicator | Why atmosphere-specific | Candidate §24.11 home |
|:---|:---|:---|
| Forecast skill calibration drift | Verification-score drift per model / horizon; signals model decay. | §24.11.4 |
| Boundary-condition lineage completeness | % of forecast `AIReceipt`s naming model run + boundary conditions resolvable to source. | §24.11.4 |
| Air-quality calibration-residual roll-up | Aggregate roll-up of `domain/air/PM_SENSOR_CALIBRATION_REVIEW.md` residuals. | §24.11.1 (coverage variant) |

[↑ back to top](#top)

---

## 4. Ownership

- **Domain steward:** OWNER_TBD (atmosphere dossier owner).
- **Governance-health steward:** OWNER_TBD (**AI-surface steward** + source steward; mandatory pair).
- **Implementation owner:** OWNER_TBD (`apps/review-console/` team).

[↑ back to top](#top)

---

## 5. Implementation pointer

- **Dashboard app:** `apps/review-console/` (PROPOSED) — `UNKNOWN` until verified.
- **Telemetry:** `runtime/observability/ai-surface/`, `runtime/observability/` (PROPOSED) — `UNKNOWN`.
- **Schemas read:** `schemas/contracts/v1/ai-receipt/`, `schemas/contracts/v1/validation/`, `schemas/contracts/v1/source/`.
- **Policy bundles emitting signals:** `policy/ai-surface/`, `policy/sources/`.

[↑ back to top](#top)

---

## 6. Review cadence

- **Trigger events:** model upgrade (NWM/HRRR/RAP/global model migration); air-quality re-analysis; atmosphere dossier edition; Atlas §24.11 amendment.
- **Default cadence:** quarterly; **immediate** review on AI-surface DENY-pattern shift or synthetic-claim incident.

[↑ back to top](#top)

---

## 7. Open questions

- [ ] **OPEN-DASH-ATMOS-01** — Define the precise forecast-horizon partition for ABSTAIN-rate tracking.
- [ ] **OPEN-DASH-ATMOS-02** — Confirm boundary-condition lineage completeness scope (single model run vs. ensemble member).
- [ ] **OPEN-DASH-ATMOS-03** — Resolve relationship between this domain-scoped spec and per-card sub-surfaces under `domain/air/` (parent vs sibling).

[↑ back to top](#top)

---

## 8. Evidence basis & citations

<details>
<summary><strong>Source ledger</strong></summary>

| Source | Status | Supports | Limits |
|:---|:---|:---|:---|
| Atlas v1.1 §24.11.1 / §24.11.4 | CONFIRMED (manuscript) | §2 indicator subset; AI-surface emphasis. | Indicators PROPOSED at source. |
| Atlas v1.0 Ch. 11 (Atmosphere dossier) | CONFIRMED (manuscript) | §1 scope; §3 candidates. | Mounted dossier presence NEEDS VERIFICATION. |
| `docs/dashboards/domain/air/PM_SENSOR_CALIBRATION_REVIEW.md` | CONFIRMED (this folder) | §2 air-quality roll-up; §7 OPEN-DASH-ATMOS-03 parent/sub-surface relationship. | PM-sensor calibration is a single Pass-30 card; broader air-quality coverage NEEDS VERIFICATION. |
| `docs/dashboards/domain/README.md` §5.1, §6 | CONFIRMED | Emphasis (Evidence-and-source · AI-surface-health); template. | Lane PROPOSED (OPEN-DASH-01). |

</details>

[↑ back to top](#top)

---

<sub>Per-domain atmosphere dashboard specification. **Specification only — implementations live in `apps/`; indicator definitions live in Atlas §24.11; domain context lives in `docs/domains/atmosphere/`.** AI-surface forecasting cite-or-abstain is enforced at the policy gate; the dashboard reports posture.</sub>
