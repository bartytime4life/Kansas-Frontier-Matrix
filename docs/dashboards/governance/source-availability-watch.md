<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-governance-source-availability-watch
title: Source Availability Watchlist (cross-cutting governance health spec)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: docs steward + governance-health steward + source-roster owner
created: 2026-05-26
updated: 2026-05-26
policy_label: public
related:
  - kfm://doc/dashboards-governance-readme
  - kfm://doc/atlas-v1-1                      # §24.11.1 stale-source rate + §24.1 source roles
  - kfm://card/p32-feat-0016                  # PROPOSED card: source availability watchlist
tags: [kfm, dashboards, governance, source, availability, watchlist, cross-cutting]
notes:
  - Source card KFM-P32-FEAT-0016 is PROPOSED in the Pass 32 New Cards Register.
  - Maps to Atlas §24.11.1 stale-source rate (rendered here as a per-source drill-down) and §24.1 source roles.
[/KFM_META_BLOCK_V2] -->

# Source Availability Watchlist

<!-- [doc: kfm://doc/dashboards-governance-source-availability-watch] -->
<a id="top"></a>

> Cross-cutting governance view of upstream source liveness — per-source reachability, retrieval-success rate, license-clearance status, and staleness budget consumption.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Scope: cross-cutting" src="https://img.shields.io/badge/scope-cross--cutting-informational">
  <img alt="Source: KFM-P32-FEAT-0016" src="https://img.shields.io/badge/source-KFM--P32--FEAT--0016-purple">
  <img alt="Atlas §24.11.1 + §24.1" src="https://img.shields.io/badge/atlas-%C2%A724.11.1%20%2B%20%C2%A724.1-purple">
  <img alt="Policy label: public" src="https://img.shields.io/badge/policy--label-public-lightgrey">
</p>

> [!IMPORTANT]
> **Truth posture.** Source card KFM-P32-FEAT-0016 is PROPOSED. The top-line "stale-source rate" indicator is also rendered in `evidence-and-source.md`; this spec is the **per-source drill-down**. Atlas §24.1 source-role vocabulary is CONFIRMED.

---

## 1. Scope

- **Source anchor:** KFM-P32-FEAT-0016 *(PROPOSED)* + Atlas §24.11.1 (stale-source indicator) + Atlas §24.1 (source roles).
- **Audience:** Source-roster owner, governance-health steward, reviewer.
- **Aggregation scope:** Cross-cutting — per upstream source, rolled up to source-role categories.

[↑ back to top](#top)

---

## 2. Indicators

| Indicator | What it measures | Healthy posture (PROPOSED) | Signal source |
|:---|:---|:---|:---|
| Per-source reachability | % of recent fetch attempts succeeding per source | ≥ 99% on tier-A sources; tracked-only on tier-B/C | Connector telemetry |
| Retrieval-success rate (24h) | Aggregate fetch success in trailing 24h | ≥ 99% | Connector telemetry |
| License-clearance status | Boolean per source: has a current license clearance | TRUE for every source on the active manifest | License-clearance validator |
| Staleness-budget consumption | % of staleness budget consumed per source | < 80% triggers attention; > 100% triggers stale-source incident | Source-watch validator |
| Watchlist size | Count of sources currently flagged (any indicator red) | Tracking metric; alert on rapid growth | Watchlist rollup |

[↑ back to top](#top)

---

## 3. Per-domain breakdowns

Each domain that depends on external sources has a corresponding watchlist slice:

- `docs/dashboards/domain/hydrology.md` *(NWS, USGS gauge sources)*
- `docs/dashboards/domain/archaeology.md` *(state archives, restricted sources)*
- `docs/dashboards/domain/fauna-flora.md` *(species observation databases)*
- *…other domain specs as applicable.*

[↑ back to top](#top)

---

## 4. Ownership

- **Docs steward:** OWNER_TBD
- **Governance-health steward:** OWNER_TBD
- **Source-roster owner:** OWNER_TBD
- **Implementation owner:** OWNER_TBD

[↑ back to top](#top)

---

## 5. Implementation pointer

- **Dashboard app:** `apps/review-console/source-watchlist/` *(PROPOSED; NEEDS VERIFICATION)*.
- **Telemetry:** Connector OTel spans; source-watch validator output.
- **Schemas read:** `schemas/contracts/v1/source/SourceRoster.schema.json`, `LicenseDeclaration.schema.json` *(NEEDS VERIFICATION).*
- **Policy bundles emitting signals:** `policy/source/staleness-budget/` *(PROPOSED).*
- **Registers visualized:** `docs/registers/DRIFT_REGISTER.md` (license-clearance lapses, staleness-budget overruns).
- **Related governance specs:** `evidence-and-source.md` (top-line stale-source rate).
- **Related observability:** `docs/dashboards/observability/service-uptime-latency.md` (connector SLO).

[↑ back to top](#top)

---

## 6. Review cadence

- Reviewed quarterly.
- Trigger events: Source-roster change, Atlas §24.1 source-role amendment, staleness-budget revision, addition/removal of a tier-A source.

[↑ back to top](#top)

---

## 7. Open questions

- **OPEN-DASH-GOV-SAW-01** — Source-tier classification (A/B/C): where is the canonical roster — `docs/registers/SOURCE_ROSTER.md` (PROPOSED) or here?
- **OPEN-DASH-GOV-SAW-02** — Per-source staleness budget: in this spec, in `policy/source/staleness-budget/`, or in the roster itself?

[↑ back to top](#top)

---

## 8. Evidence basis & citations

| Source | Status | Supports |
|:---|:---|:---|
| KFM-P32-FEAT-0016 (Source availability watchlist) | PROPOSED in corpus | §1 source anchor. |
| Atlas v1.1 §24.11.1 (stale-source indicator) | CONFIRMED (manuscript) | §2 staleness-budget signal. |
| Atlas v1.1 §24.1 (Source roles) | CONFIRMED (manuscript) | §1, §2 source-tier vocabulary. |
| `docs/dashboards/governance/README.md` | CONFIRMED (this folder) | §6 template. |

<sub>Specification only. Per-source drill-down here; system-wide stale-source rate at `evidence-and-source.md`. Roster data lives in `docs/registers/`, not here.</sub>
