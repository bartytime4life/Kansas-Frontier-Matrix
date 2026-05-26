<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-governance-rollback-correction-lineage
title: Rollback & Correction Lineage Timeline (cross-cutting governance health spec)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: docs steward + governance-health steward + release authority
created: 2026-05-26
updated: 2026-05-26
policy_label: public
related:
  - kfm://doc/dashboards-governance-readme
  - kfm://doc/atlas-v1-1                      # §24.6 (correction/rollback gates) + §24.8 (stale-state/supersession)
  - kfm://card/p32-feat-0020                  # PROPOSED card: rollback and correction lineage timeline
tags: [kfm, dashboards, governance, rollback, correction, lineage, supersession, cross-cutting]
notes:
  - Source card KFM-P32-FEAT-0020 is PROPOSED in the Pass 32 New Cards Register.
  - Genuine overlap with the PROPOSED docs/dashboards/release/ sibling — OPEN-DASH-GOV-01 boundary applies.
[/KFM_META_BLOCK_V2] -->

# Rollback & Correction Lineage Timeline

<!-- [doc: kfm://doc/dashboards-governance-rollback-correction-lineage] -->
<a id="top"></a>

> Cross-cutting governance view that renders the full timeline of correction notices, rollback cards, and supersession events — showing how a current artifact came to be the current artifact.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Scope: cross-cutting" src="https://img.shields.io/badge/scope-cross--cutting-informational">
  <img alt="Source: KFM-P32-FEAT-0020" src="https://img.shields.io/badge/source-KFM--P32--FEAT--0020-purple">
  <img alt="Atlas §24.6 + §24.8" src="https://img.shields.io/badge/atlas-%C2%A724.6%20%2B%20%C2%A724.8-purple">
  <img alt="Policy label: public" src="https://img.shields.io/badge/policy--label-public-lightgrey">
</p>

> [!IMPORTANT]
> **Truth posture.** Source card KFM-P32-FEAT-0020 is PROPOSED. Atlas §24.6 (Correction / Rollback gates) and §24.8 (Stale-State / Supersession) are CONFIRMED. This dashboard renders existing record chains — it never creates lineage; the lineage lives in `CorrectionNotice`, `RollbackCard`, and `SupersessionRecord` artifacts.

> [!NOTE]
> **Boundary with `release/` sibling.** Per parent README §5.2 and OPEN-DASH-GOV-01, this view is genuinely at the boundary between governance and release-lifecycle. Current convention: governance-posture view (trend + posture) lives here; per-release detail browser lives in the PROPOSED `release/` sibling.

---

## 1. Scope

- **Source anchor:** KFM-P32-FEAT-0020 *(PROPOSED)* + Atlas §24.6 (Correction / Rollback gates) + §24.8 (Stale-State / Supersession).
- **Audience:** Release authority, governance-health steward, reviewer.
- **Aggregation scope:** Cross-cutting — per-artifact lineage traversal, with system-wide rollup.

[↑ back to top](#top)

---

## 2. Indicators

| Indicator | What it measures | Healthy posture (PROPOSED) | Signal source |
|:---|:---|:---|:---|
| Correction-event count (rolling 90d) | Count of `CorrectionNotice` publications in trailing 90d | Tracked; alert on rapid growth | `CorrectionNotice` records |
| Rollback-event count (rolling 90d) | Count of `RollbackCard` activations in trailing 90d | Tracked; alert on rapid growth | `RollbackCard` records |
| Supersession-chain depth median | Median depth of `supersededBy` chains for current artifacts | Tracked; growth indicates churn | Supersession validator (Atlas §24.8) |
| Open-correction count | Corrections in published-but-not-closed state | Tracked; alert on long tail | `CorrectionNotice` records |
| Lineage-completeness rate | % of `CorrectionNotice`/`RollbackCard` carrying full provenance back to the originating release | 100% | Lineage validator |

[↑ back to top](#top)

---

## 3. Per-domain breakdowns

Per-domain correction/rollback patterns differ by release cadence and materiality profile:

- `docs/dashboards/domain/hydrology.md` *(frequent low-materiality corrections)*
- `docs/dashboards/domain/archaeology.md` *(episodic high-materiality corrections)*
- *…other domain specs as applicable.*

[↑ back to top](#top)

---

## 4. Ownership

- **Docs steward:** OWNER_TBD
- **Governance-health steward:** OWNER_TBD
- **Release authority:** OWNER_TBD
- **Implementation owner:** OWNER_TBD

[↑ back to top](#top)

---

## 5. Implementation pointer

- **Dashboard app:** `apps/review-console/lineage-timeline/` *(PROPOSED; NEEDS VERIFICATION)*.
- **Telemetry:** Release-pipeline OTel root traces; cross-link to `docs/dashboards/observability/openlineage-event-stream.md`.
- **Schemas read:** `schemas/contracts/v1/release/CorrectionNotice.schema.json`, `RollbackCard.schema.json`, `SupersessionRecord.schema.json` *(NEEDS VERIFICATION).*
- **Policy bundles emitting signals:** `policy/release/lineage-completeness/` *(PROPOSED).*
- **Registers visualized:** `docs/registers/DRIFT_REGISTER.md` *(when lineage-completeness gaps surface as drift).*
- **Related governance specs:** `release-correction-rollback.md` (trend posture parent).
- **Related release-lifecycle spec:** `docs/dashboards/release/` *(PROPOSED — per-release browser).*

[↑ back to top](#top)

---

## 6. Review cadence

- Reviewed quarterly.
- Trigger events: Atlas §24.6 / §24.8 amendment, `CorrectionNotice` / `RollbackCard` schema change, lineage-validator revision.

[↑ back to top](#top)

---

## 7. Open questions

- **OPEN-DASH-GOV-RCL-01** — Boundary with the PROPOSED `release/` sibling (inherits OPEN-DASH-GOV-01).
- **OPEN-DASH-GOV-RCL-02** — Should "lineage-completeness rate" sub-100% block release (policy enforcement) or be alert-only (dashboard indicator)?

[↑ back to top](#top)

---

## 8. Evidence basis & citations

| Source | Status | Supports |
|:---|:---|:---|
| KFM-P32-FEAT-0020 (Rollback and correction lineage timeline) | PROPOSED in corpus | §1 source anchor. |
| Atlas v1.1 §24.6 (Correction / Rollback gates) | CONFIRMED (manuscript) | §2 indicators. |
| Atlas v1.1 §24.8 (Stale-State / Supersession Reference) | CONFIRMED (manuscript) | §2 supersession chain depth. |
| `docs/dashboards/governance/README.md` | CONFIRMED (this folder) | §6 template; OPEN-DASH-GOV-01 boundary. |

<sub>Specification only. Visualizes lineage records; never creates them. Boundary with `release/` is unresolved (OPEN-DASH-GOV-01).</sub>
