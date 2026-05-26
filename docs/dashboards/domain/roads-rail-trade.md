<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-domain-roads-rail-trade
title: Roads / Rail / Trade Routes Dashboard Specification (PROPOSED lane; per-domain instance of Atlas §24.11)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: roads-rail-trade-domain steward + governance-health steward
created: 2026-05-26
updated: 2026-05-26
policy_label: public
related:
  - kfm://doc/dashboards-domain-readme
  - kfm://doc/atlas-v1-1
  - kfm://doc/atlas-v1-1-ch24-5-sensitivity-tier-reference
  - kfm://doc/atlas-v1-1-ch24-6-pipeline-gate-reference
  - kfm://doc/domains-roads-rail-trade-dossier               # CONFIRMED dossier home: docs/domains/roads-rail-trade/
  - kfm://adr/dashboards-lane-existence                      # PROPOSED candidate: OPEN-DASH-01
tags: [kfm, dashboards, domain, roads, rail, trade, transit, indicators, governance-health, specification]
notes:
  - Per-domain instance of Atlas v1.1 §24.11. Specification only; not an implementation.
  - Historical trade-route corpora (Santa Fe / Chisholm / Oregon-California Trail) carry edition lineage; modern transit feeds carry SLO emphasis.
  - Atlas §24.11 wins on indicator conflicts; roads-rail-trade dossier wins on context conflicts.
[/KFM_META_BLOCK_V2] -->

# Roads / Rail / Trade Routes Dashboard Specification

<!-- [doc: kfm://doc/dashboards-domain-roads-rail-trade] -->
<a id="top"></a>

> Per-domain dashboard specification for **Roads / Rail / Trade Routes** (Atlas v1.0 Ch. 13). Modern road & rail networks, transit feeds, historical trade-route corpora.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Atlas chapter: Ch. 13" src="https://img.shields.io/badge/atlas-Ch.%2013-purple">
  <img alt="Indicator emphasis: 24.11.1 / 24.11.5" src="https://img.shields.io/badge/emphasis-24.11.1%20%C2%B7%2024.11.5-informational">
  <img alt="Policy label: public" src="https://img.shields.io/badge/policy--label-public-lightgrey">
</p>

> [!IMPORTANT]
> **Truth posture.** Indicators PROPOSED; instances PROPOSED; lane PROPOSED (OPEN-DASH-01); implementation NEEDS VERIFICATION.

> [!NOTE]
> **Real-time transit.** SLO posture for live transit feeds is already surfaced by [`operational/SLO_LIVE_FEEDS.md`](../operational/SLO_LIVE_FEEDS.md) and [`operational/REALTIME_FEED_FRESHNESS.md`](../operational/REALTIME_FEED_FRESHNESS.md). This per-domain spec roll-ups domain coverage; it does not duplicate operational SLOs.

---

## 1. Domain scope

- **Atlas chapter:** v1.0 Ch. 13 (Roads / Rail / Trade Routes).
- **Default sensitivity tier(s):** T1 (public road/rail networks, transit schedules, historical trade routes).
- **Pipeline shape:** Standard intake → validation → derive → publish; live transit feeds emit additional SLO signals (see operational dashboards).
- **Dossier:** `docs/domains/roads-rail-trade/` — `K.` validators (functional-class taxonomy, GTFS schema, trade-route corpus version), `M.` correction posture for re-routed or re-classified segments.

[↑ back to top](#top)

---

## 2. Indicator subset

Emphasis per README §5.1: **Evidence-and-source · Documentation-and-drift**.

| Indicator | §24.11 cat. | Domain-scale healthy posture | Receipt / signal source |
|:---|:---|:---|:---|
| EvidenceRef resolution rate | 24.11.1 | > 99.9% across KDOT / OSM / GTFS / historical-trade-corpus cites. | `ValidationReport`, EvidenceBundle index |
| Source-role distribution drift | 24.11.1 | KDOT canonical for state highway functional class; OSM auxiliary; historical-trade routes carry corpus-edition pinning. | Source descriptors |
| Stale source rate | 24.11.1 | KDOT base, GTFS feed cadence, OSM diff cadence all monitored. | Source descriptors, freshness cadence metadata |
| Quarantine throughput | 24.11.1 | Cause distribution visible (functional-class drift, GTFS validation, geometry); no sustained backlog. | `ValidationReport`, quarantine ledger |
| ADR completeness | 24.11.5 | Open ADRs (route-segment canonicalization, historical-corpus edition pinning) tracked. | ADR index |
| Drift register size | 24.11.5 | Route-network derivative drift surfaced; trend tracked. | `docs/registers/DRIFT_REGISTER.md` |
| Per-root README presence | 24.11.5 | `docs/domains/roads-rail-trade/README.md` exists and is current. | Directory-rules linter output |
| Atlas / supplement lineage clarity | 24.11.5 | Each historical trade-route corpus supplement carries forward/back links; no orphan supplements. | Supersession entries |

[↑ back to top](#top)

---

## 3. Domain-specific indicators (PROPOSED)

| PROPOSED indicator | Why this-domain-specific | Candidate §24.11 home |
|:---|:---|:---|
| Functional-class canonicalization coverage | % of road segments mapped to a canonical functional class (FHWA / KDOT / OSM). | §24.11.1 |
| Historical-corpus edition pinning | % of trade-route derivative claims pinned to a specific corpus edition. | §24.11.5 |
| Live-transit SLO coverage roll-up | Roll-up of `SLO_LIVE_FEEDS` posture per agency (RideKC, Topeka Metro, KSL services). | §24.11.1 (coverage variant) |

[↑ back to top](#top)

---

## 4. Ownership

- **Domain steward:** OWNER_TBD (roads-rail-trade dossier owner).
- **Governance-health steward:** OWNER_TBD (source steward + docs steward; observability steward for transit SLOs).
- **Implementation owner:** OWNER_TBD (`apps/review-console/` team).

[↑ back to top](#top)

---

## 5. Implementation pointer

- **Dashboard app:** `apps/review-console/` (PROPOSED) — `UNKNOWN` until verified.
- **Telemetry:** `runtime/observability/` (PROPOSED) — `UNKNOWN`.
- **Schemas read:** `schemas/contracts/v1/validation/`, `schemas/contracts/v1/source/`, `schemas/contracts/v1/release/`.
- **Policy bundles emitting signals:** `policy/sources/`, `policy/documentation/`.

[↑ back to top](#top)

---

## 6. Review cadence

- **Trigger events:** KDOT major-network update; GTFS feed agency change; trade-route corpus edition bump; roads-rail-trade dossier edition.
- **Default cadence:** semi-annual.

[↑ back to top](#top)

---

## 7. Open questions

- [ ] **OPEN-DASH-RRT-01** — Reconcile live-transit SLO roll-up here vs. authoritative home in `operational/SLO_LIVE_FEEDS.md`.
- [ ] **OPEN-DASH-RRT-02** — Confirm historical-trade-corpus edition-pinning surface (per-route or per-derivative).

[↑ back to top](#top)

---

## 8. Evidence basis & citations

<details>
<summary><strong>Source ledger</strong></summary>

| Source | Status | Supports | Limits |
|:---|:---|:---|:---|
| Atlas v1.1 §24.11.1 / §24.11.5 | CONFIRMED (manuscript) | §2 indicator subset. | Indicators PROPOSED at source. |
| Atlas v1.0 Ch. 13 (Roads / Rail / Trade Routes dossier) | CONFIRMED (manuscript) | §1 scope; §3 candidates. | Mounted dossier presence NEEDS VERIFICATION. |
| `docs/dashboards/operational/SLO_LIVE_FEEDS.md`, `…/REALTIME_FEED_FRESHNESS.md` | CONFIRMED (this folder) | Live-transit SLO authority; this spec rolls up rather than duplicates. | Operational specs are PROPOSED. |
| `docs/dashboards/domain/README.md` §5.1, §6 | CONFIRMED | Emphasis; template. | Lane PROPOSED (OPEN-DASH-01). |

</details>

[↑ back to top](#top)

---

<sub>Per-domain roads / rail / trade routes dashboard specification. **Specification only — implementations live in `apps/`; indicator definitions live in Atlas §24.11; domain context lives in `docs/domains/roads-rail-trade/`.** Live-transit SLOs live in the operational dashboards; this spec only rolls them up.</sub>
