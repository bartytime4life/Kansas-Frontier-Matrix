<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-governance-promotion-gate-status
title: Promotion Gate Status Board (cross-cutting governance health spec)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: docs steward + governance-health steward + release authority
created: 2026-05-26
updated: 2026-05-26
policy_label: public
related:
  - kfm://doc/dashboards-governance-readme
  - kfm://doc/atlas-v1-1                      # §24.6 pipeline gates + §24.6.3 reason codes
  - kfm://card/p32-feat-0014                  # PROPOSED card: promotion gate status board
tags: [kfm, dashboards, governance, promotion, gates, reason-codes, cross-cutting]
notes:
  - Source card KFM-P32-FEAT-0014 is PROPOSED in the Pass 32 New Cards Register.
  - Maps to Atlas §24.6 pipeline gates and §24.6.3 reason-code catalog.
[/KFM_META_BLOCK_V2] -->

# Promotion Gate Status Board

<!-- [doc: kfm://doc/dashboards-governance-promotion-gate-status] -->
<a id="top"></a>

> Cross-cutting governance view of pipeline promotion gates — per-gate pass-rate, denial-reason-code distribution, override rate, and gate-wallclock posture across all in-flight promotions.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Scope: cross-cutting" src="https://img.shields.io/badge/scope-cross--cutting-informational">
  <img alt="Source: KFM-P32-FEAT-0014" src="https://img.shields.io/badge/source-KFM--P32--FEAT--0014-purple">
  <img alt="Atlas §24.6" src="https://img.shields.io/badge/atlas-%C2%A724.6-purple">
  <img alt="Policy label: public" src="https://img.shields.io/badge/policy--label-public-lightgrey">
</p>

> [!IMPORTANT]
> **Truth posture.** Source card KFM-P32-FEAT-0014 is PROPOSED. Gate vocabulary and reason-code catalog come from Atlas §24.6 and §24.6.3 (CONFIRMED). This dashboard visualizes the gate signals; gate enforcement lives in `policy/`.

---

## 1. Scope

- **Source anchor:** KFM-P32-FEAT-0014 *(PROPOSED card)* + Atlas §24.6 (Pipeline Gates) + §24.6.3 (reason codes).
- **Audience:** Release authority, governance-health steward, gate owner, reviewer.
- **Aggregation scope:** Cross-cutting — every promotion gate across pipelines.

[↑ back to top](#top)

---

## 2. Indicators

| Indicator | What it measures | Healthy posture (PROPOSED) | Signal source |
|:---|:---|:---|:---|
| Per-gate pass-rate | % of promotion attempts passing each gate | ≥ 95% on stable gates; tracking metric on new gates | Gate-decision telemetry |
| Denial-reason-code distribution | Distribution of denials across §24.6.3 reason codes | Tracked; alert on a single code dominating > 50% of denials | `PolicyDecision` outcomes |
| Override rate | % of denials overridden by a named authority | < 1% *(PROPOSED)* | Override-decision records |
| Gate-wallclock p95 | p95 time a candidate spends at each gate | Per-gate budget *(PROPOSED)* | Gate-stage OTel spans |
| Stuck-at-gate count | Candidates at a gate longer than the gate's SLA window | 0 | Gate-state validator |

[↑ back to top](#top)

---

## 3. Per-domain breakdowns

Promotion gates are pipeline-wide, but per-domain pipelines have different gate profiles:

- `docs/dashboards/domain/<domain>.md` *(per-domain gate pass-rate when domain pipelines materially differ).*

[↑ back to top](#top)

---

## 4. Ownership

- **Docs steward:** OWNER_TBD
- **Governance-health steward:** OWNER_TBD
- **Release authority:** OWNER_TBD
- **Gate owners:** OWNER_TBD *(per gate)*
- **Implementation owner:** OWNER_TBD

[↑ back to top](#top)

---

## 5. Implementation pointer

- **Dashboard app:** `apps/review-console/promotion-gates/` *(PROPOSED; NEEDS VERIFICATION)*.
- **Telemetry:** Gate-stage OTel spans; cross-link to `docs/dashboards/observability/ingest-run-trace-coverage.md` (policy span structure).
- **Schemas read:** `schemas/contracts/v1/policy/PolicyDecision.schema.json`, `schemas/contracts/v1/release/GateDecision.schema.json` *(NEEDS VERIFICATION).*
- **Policy bundles emitting signals:** `policy/promotion/gates/` *(PROPOSED).*
- **Registers visualized:** `docs/registers/DRIFT_REGISTER.md` (override events recorded as drift).
- **Related governance specs:** `denial-reason-explorer.md` (DENY drill-down), `release-correction-rollback.md` (release-readiness gate pass-rate shared signal).

[↑ back to top](#top)

---

## 6. Review cadence

- Reviewed quarterly.
- Trigger events: Atlas §24.6 gate vocabulary change, §24.6.3 reason-code addition, addition of a new gate, override-policy change.

[↑ back to top](#top)

---

## 7. Open questions

- **OPEN-DASH-GOV-PGS-01** — Per-gate wallclock budget table: in this spec or in `policy/promotion/gates/`?
- **OPEN-DASH-GOV-PGS-02** — Override-rate threshold: 1% PROPOSED — sensitive to override-policy maturity.
- **OPEN-DASH-GOV-PGS-03** — Boundary with `denial-reason-explorer.md`: top-line distribution here, full drill-down there.

[↑ back to top](#top)

---

## 8. Evidence basis & citations

| Source | Status | Supports |
|:---|:---|:---|
| KFM-P32-FEAT-0014 (Promotion gate status board) | PROPOSED in corpus | §1 source anchor. |
| Atlas v1.1 §24.6 (Pipeline Gate Reference) | CONFIRMED (manuscript) | §2 gate vocabulary. |
| Atlas v1.1 §24.6.3 (Reason codes) | CONFIRMED (manuscript) | §2 denial-reason distribution. |
| `docs/dashboards/governance/README.md` | CONFIRMED (this folder) | §6 template. |

<sub>Specification only. Gate enforcement in policy bundles; this is the visibility surface.</sub>
