<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-governance-denial-reason-explorer
title: Denial Reason Explorer (cross-cutting governance health spec)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: docs steward + governance-health steward + policy owner
created: 2026-05-26
updated: 2026-05-26
policy_label: public
related:
  - kfm://doc/dashboards-governance-readme
  - kfm://doc/atlas-v1-1                      # §24.3 outcome envelope + §24.11.4 DENY distribution + §24.6.3 reason codes
  - kfm://card/p32-feat-0017                  # PROPOSED card: denial reason explorer
tags: [kfm, dashboards, governance, denial, deny, reason-codes, cross-cutting]
notes:
  - Source card KFM-P32-FEAT-0017 is PROPOSED in the Pass 32 New Cards Register.
  - Drill-down companion to ai-surface-health.md (DENY-reason top-line) and promotion-gate-status.md.
[/KFM_META_BLOCK_V2] -->

# Denial Reason Explorer

<!-- [doc: kfm://doc/dashboards-governance-denial-reason-explorer] -->
<a id="top"></a>

> Cross-cutting governance view that lets reviewers drill into `PolicyDecision` denials by reason code, surface, time window, and origin — the operational tool behind the DENY-reason-distribution indicators.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Scope: cross-cutting" src="https://img.shields.io/badge/scope-cross--cutting-informational">
  <img alt="Source: KFM-P32-FEAT-0017" src="https://img.shields.io/badge/source-KFM--P32--FEAT--0017-purple">
  <img alt="Atlas §24.3 + §24.6.3 + §24.11.4" src="https://img.shields.io/badge/atlas-multiple-purple">
  <img alt="Policy label: public" src="https://img.shields.io/badge/policy--label-public-lightgrey">
</p>

> [!IMPORTANT]
> **Truth posture.** Source card KFM-P32-FEAT-0017 is PROPOSED. The reason-code catalog comes from Atlas §24.6.3 (CONFIRMED); outcome envelope shape from §24.3 (CONFIRMED). This dashboard is a **drill-down** — top-line DENY distributions also appear in `ai-surface-health.md` and `promotion-gate-status.md`.

---

## 1. Scope

- **Source anchor:** KFM-P32-FEAT-0017 *(PROPOSED)* + Atlas §24.3 (outcome envelope) + §24.6.3 (reason codes) + §24.11.4 (DENY distribution).
- **Audience:** Policy owner, governance-health steward, reviewer, AI-surface owner.
- **Aggregation scope:** Cross-cutting — DENY events across all surfaces (AI surface, promotion gates, ingest pipeline, governed-API).

[↑ back to top](#top)

---

## 2. Indicators

| Indicator | What it measures | Healthy posture (PROPOSED) | Signal source |
|:---|:---|:---|:---|
| DENY-by-reason-code | Per-reason-code DENY counts and trend | Tracked; alert on a new reason code suddenly dominating | `PolicyDecision` outcomes |
| DENY-by-surface | DENY counts per surface (AI / gate / ingest / API) | Tracked | `PolicyDecision` outcomes |
| Time-window DENY heatmap | DENY rate by hour-of-day / day-of-week | Tracking metric | `PolicyDecision` outcomes |
| Top-10 DENY origins | Origins generating the most DENYs (e.g., tenant / pipeline / model) | Tracked; not thresholded | `PolicyDecision` outcomes |
| Unknown-reason-code count | DENYs carrying a reason code not in the §24.6.3 catalog | 0 | Reason-code validator |

[↑ back to top](#top)

---

## 3. Per-domain breakdowns

DENY events are domain-tagged where applicable:

- `docs/dashboards/domain/archaeology.md` *(T4 default-deny — most DENYs expected here)*
- `docs/dashboards/domain/fauna-flora.md` *(rare-species suppression DENYs)*
- *…other domain specs as applicable.*

[↑ back to top](#top)

---

## 4. Ownership

- **Docs steward:** OWNER_TBD
- **Governance-health steward:** OWNER_TBD
- **Policy owner:** OWNER_TBD
- **Implementation owner:** OWNER_TBD

[↑ back to top](#top)

---

## 5. Implementation pointer

- **Dashboard app:** `apps/review-console/denial-explorer/` *(PROPOSED; NEEDS VERIFICATION)*.
- **Telemetry:** `PolicyDecision` outcome stream; cross-link to `docs/dashboards/observability/openlineage-event-stream.md` (`policy_labels` facet).
- **Schemas read:** `schemas/contracts/v1/policy/PolicyDecision.schema.json` *(NEEDS VERIFICATION).*
- **Policy bundles emitting signals:** All `policy/` bundles that emit DENY decisions.
- **Registers visualized:** None directly — this dashboard surfaces events.
- **Related governance specs:** `ai-surface-health.md`, `promotion-gate-status.md`, `sensitivity-and-rights.md`.

[↑ back to top](#top)

---

## 6. Review cadence

- Reviewed quarterly.
- Trigger events: Atlas §24.6.3 reason-code addition or rename, addition of a new DENY surface, `PolicyDecision` schema change.

[↑ back to top](#top)

---

## 7. Open questions

- **OPEN-DASH-GOV-DRE-01** — Does "top-10 DENY origins" need PII-handling rules if "origin" includes tenant/user IDs? Cross-link to `sensitivity-and-rights.md`.
- **OPEN-DASH-GOV-DRE-02** — Unknown-reason-code alert: page on first occurrence, or aggregate?

[↑ back to top](#top)

---

## 8. Evidence basis & citations

| Source | Status | Supports |
|:---|:---|:---|
| KFM-P32-FEAT-0017 (Denial reason explorer) | PROPOSED in corpus | §1 source anchor. |
| Atlas v1.1 §24.3 (Outcome envelope) | CONFIRMED (manuscript) | §2 PolicyDecision shape. |
| Atlas v1.1 §24.6.3 (Reason codes) | CONFIRMED (manuscript) | §2 reason-code catalog. |
| Atlas v1.1 §24.11.4 (AI Surface Health — DENY distribution) | CONFIRMED (manuscript) | §3 cross-link to AI surface. |
| `docs/dashboards/governance/README.md` | CONFIRMED (this folder) | §6 template. |

<sub>Specification only. Drill-down tool; top-line distributions live in `ai-surface-health.md` and `promotion-gate-status.md`.</sub>
