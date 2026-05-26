<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-domain-hazards
title: Hazards Dashboard Specification (PROPOSED lane; per-domain instance of Atlas §24.11)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: hazards-domain steward + release steward + governance-health steward
created: 2026-05-26
updated: 2026-05-26
policy_label: public
related:
  - kfm://doc/dashboards-domain-readme
  - kfm://doc/atlas-v1-1
  - kfm://doc/atlas-v1-1-ch24-5-sensitivity-tier-reference
  - kfm://doc/atlas-v1-1-ch24-6-pipeline-gate-reference
  - kfm://doc/domains-hazards-dossier                        # CONFIRMED dossier home: docs/domains/hazards/
  - kfm://adr/dashboards-lane-existence                      # PROPOSED candidate: OPEN-DASH-01
tags: [kfm, dashboards, domain, hazards, alerts, release-correction-rollback, indicators, governance-health, specification]
notes:
  - Per-domain instance of Atlas v1.1 §24.11. Specification only; not an implementation.
  - Hazards carries an alert-authority gate — KFM does not issue official alerts; the dashboard reports DENY-by-authority posture.
  - Atlas §24.11 wins on indicator conflicts; hazards dossier wins on context conflicts.
[/KFM_META_BLOCK_V2] -->

# Hazards Dashboard Specification

<!-- [doc: kfm://doc/dashboards-domain-hazards] -->
<a id="top"></a>

> Per-domain dashboard specification for **Hazards** (Atlas v1.0 Ch. 12). Flood, wildfire, severe-weather, tornado, drought, seismicity. **Release-correction-rollback** is the central indicator family: hazards corrections must invalidate downstream derivatives quickly.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Atlas chapter: Ch. 12" src="https://img.shields.io/badge/atlas-Ch.%2012-purple">
  <img alt="Indicator emphasis: 24.11.2 / 24.11.1" src="https://img.shields.io/badge/emphasis-24.11.2%20%C2%B7%2024.11.1-informational">
  <img alt="Policy label: public" src="https://img.shields.io/badge/policy--label-public-lightgrey">
</p>

> [!IMPORTANT]
> **Truth posture.** Indicators PROPOSED; instances PROPOSED; lane PROPOSED (OPEN-DASH-01); implementation NEEDS VERIFICATION.

> [!CAUTION]
> **KFM is not an alerting authority.** Anything that resembles an official warning (NWS, USGS, KDEM) must be DENIED with `ALERT_AUTHORITY` reason and routed to the authoritative source. The dashboard reports the DENY-by-authority rate; the gate enforces it.

> [!WARNING]
> **Time pressure.** Hazards posture is consequential within minutes-to-hours. Indicator latencies here matter more than in slower domains.

---

## 1. Domain scope

- **Atlas chapter:** v1.0 Ch. 12 (Hazards).
- **Default sensitivity tier(s):** T1–T2 (public hazard event records, historical extents); T3 where individual loss/property impact is identifiable.
- **Pipeline shape:** Standard intake → validation → derive → publish, with **alert-authority gate** on any emission that resembles an active warning; rollback is mandatory for all hazard layers.
- **Dossier:** `docs/domains/hazards/` — `K.` validators (event-type vocabulary, severity scales), `M.` rollback + correction posture, `N.` verification backlog.

[↑ back to top](#top)

---

## 2. Indicator subset

Emphasis per README §5.1: **Release-correction-rollback (alert-authority denial) · Evidence-and-source**.

| Indicator | §24.11 cat. | Domain-scale healthy posture | Receipt / signal source |
|:---|:---|:---|:---|
| Release with rollback target | 24.11.2 | **100%** — every published hazard layer (flood-extent, fire-perimeter, severe-weather track) names a valid rollback target. | `ReleaseManifest`, `RollbackCard` |
| Correction lead time | 24.11.2 | **Median ≤ stated hazards-domain tolerance** (faster than slower domains; trend tracked). | `CorrectionNotice` |
| Derivative-invalidation coverage | 24.11.2 | Approaches 100% — corrections to event extents cascade-invalidate downstream impact / loss derivatives. | `CorrectionNotice`, lineage graph |
| Rollback rehearsal rate | 24.11.2 | Non-zero per release window; rehearsals exercise the alert-resembling-content path. | `RollbackCard` |
| Supersession lineage gap | 24.11.2 / 24.11.5 | Zero — every superseded hazard product carries a forward link. | `ReleaseManifest`, supersession entries |
| **`ALERT_AUTHORITY` DENY rate** | 24.11.2 / 24.11.4 | **Tracked, visible, expected to be non-zero.** Any silent zero with active hazard sources is a defect (gate not firing). | `PolicyDecision`, `AIReceipt` |
| EvidenceRef resolution rate | 24.11.1 | > 99.9% across NWS / USGS / KDEM / KS Mesonet cites; per-source rate visible. | `ValidationReport`, EvidenceBundle index |
| Stale source rate | 24.11.1 | Real-time hazard feeds monitored against freshness cadence; outage dispositioned. | Source descriptors, freshness cadence metadata |
| Quarantine throughput | 24.11.1 | Cause distribution visible (event-type vocabulary, severity, geometry); no sustained backlog. | `ValidationReport`, quarantine ledger |

[↑ back to top](#top)

---

## 3. Domain-specific indicators (PROPOSED)

| PROPOSED indicator | Why hazards-specific | Candidate §24.11 home |
|:---|:---|:---|
| Active-hazard rollback latency | Time from hazard correction emission to last derivative invalidation — minutes-grade target. | §24.11.2 |
| Authority routing coverage | % of `ALERT_AUTHORITY` DENYs that surface a routing link to the canonical source. | §24.11.2 |
| Event-type vocabulary drift | Drift in event-type vocabulary across years / sources (NWS storm-event database). | §24.11.5 |

[↑ back to top](#top)

---

## 4. Ownership

- **Domain steward:** OWNER_TBD (hazards dossier owner).
- **Governance-health steward:** OWNER_TBD (**release steward** + correction reviewer; mandatory pair).
- **Implementation owner:** OWNER_TBD (`apps/review-console/` team).

[↑ back to top](#top)

---

## 5. Implementation pointer

- **Dashboard app:** `apps/review-console/` (PROPOSED) — `UNKNOWN` until verified.
- **Telemetry:** `runtime/observability/release/`, `runtime/observability/` (PROPOSED) — `UNKNOWN`.
- **Schemas read:** `schemas/contracts/v1/release/`, `schemas/contracts/v1/correction/`, `schemas/contracts/v1/policy-decision/`.
- **Policy bundles emitting signals:** `policy/release/`, `policy/correction/`, `policy/alert-authority/`.

[↑ back to top](#top)

---

## 6. Review cadence

- **Trigger events:** any hazard correction issued; NWS / USGS schema bump; hazards dossier edition.
- **Default cadence:** monthly during active-hazard season (spring severe weather, summer fire, winter ice); **immediate** review on any silent-zero in `ALERT_AUTHORITY` DENY rate.

[↑ back to top](#top)

---

## 7. Open questions

- [ ] **OPEN-DASH-HAZ-01** — Define active-hazard rollback latency target (minutes vs hour-grade).
- [ ] **OPEN-DASH-HAZ-02** — Confirm `ALERT_AUTHORITY` is a single denial reason or a family (per-authority sub-reasons).
- [ ] **OPEN-DASH-HAZ-03** — Reconcile hazards spec's rollback-rehearsal cadence with the governance `RELEASE_CORRECTION_ROLLBACK` master spec.

[↑ back to top](#top)

---

## 8. Evidence basis & citations

<details>
<summary><strong>Source ledger</strong></summary>

| Source | Status | Supports | Limits |
|:---|:---|:---|:---|
| Atlas v1.1 §24.11.2 / §24.11.1 | CONFIRMED (manuscript) | §2 indicator subset. | Indicators PROPOSED at source. |
| Atlas v1.0 Ch. 12 (Hazards dossier) | CONFIRMED (manuscript) | §1 scope; §3 candidates. | Mounted dossier presence NEEDS VERIFICATION. |
| Atlas v1.1 §24.10 (Risk register) | CONFIRMED (manuscript) | §2 release-correction emphasis. | Risk severities PROPOSED. |
| `docs/dashboards/governance/RELEASE_CORRECTION_ROLLBACK.md` | CONFIRMED (this folder) | §2 cross-reference for master rollback indicators. | Master spec is itself PROPOSED. |
| `docs/dashboards/domain/README.md` §5.1, §6 | CONFIRMED | Emphasis; template. | Lane PROPOSED (OPEN-DASH-01). |

</details>

[↑ back to top](#top)

---

<sub>Per-domain hazards dashboard specification. **Specification only — implementations live in `apps/`; indicator definitions live in Atlas §24.11; domain context lives in `docs/domains/hazards/`.** KFM is not an alerting authority: the gate denies, the dashboard reports the denial rate, the receipts back the trust.</sub>
