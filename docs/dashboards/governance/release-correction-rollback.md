<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-governance-release-correction-rollback
title: Release, Correction, Rollback (system-wide governance health spec; Atlas §24.11.2)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: docs steward + governance-health steward + release authority
created: 2026-05-26
updated: 2026-05-26
policy_label: public
related:
  - kfm://doc/dashboards-governance-readme
  - kfm://doc/atlas-v1-1                      # §24.11.2 — 5 indicators
  - kfm://doc/dashboards-domain-readme
  - kfm://register/drift
tags: [kfm, dashboards, governance, release, correction, rollback, 24-11-2]
notes:
  - Indicator catalog: Atlas §24.11.2 (5 indicators); labeled PROPOSED in source.
  - Release authority MUST be on the owner roster for this spec (per parent README §3).
  - Per-release detail belongs in docs/dashboards/release/; this spec carries trend posture only.
[/KFM_META_BLOCK_V2] -->

# Release, Correction, Rollback

<!-- [doc: kfm://doc/dashboards-governance-release-correction-rollback] -->
<a id="top"></a>

> System-wide governance health view of release lifecycle integrity — release-manifest completeness, correction-notice latency, rollback-card coverage, supersession-chain integrity, and release-readiness gate pass-rate. Atlas §24.11.2.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Scope: system-wide" src="https://img.shields.io/badge/scope-system--wide-informational">
  <img alt="Atlas §24.11.2" src="https://img.shields.io/badge/atlas-%C2%A724.11.2-purple">
  <img alt="Indicators: 5" src="https://img.shields.io/badge/indicators-5-yellow">
  <img alt="Policy label: public" src="https://img.shields.io/badge/policy--label-public-lightgrey">
</p>

> [!IMPORTANT]
> **Truth posture.** Indicator catalog from Atlas §24.11.2 (CONFIRMED text, PROPOSED indicators). Per-release detail (per-manifest browser, per-rollback timeline) belongs in the PROPOSED sibling `docs/dashboards/release/`, not here — this spec carries the **trend / posture** view. See OPEN-DASH-GOV-01.

---

## 1. Scope

- **Atlas reference:** §24.11.2 — Release, Correction, Rollback (5 indicators).
- **Audience:** Release authority, governance-health steward, reviewer, docs steward.
- **Aggregation scope:** System-wide trend across releases. Per-release detail belongs in `docs/dashboards/release/`.

[↑ back to top](#top)

---

## 2. Indicators

| Indicator | What it measures | Healthy posture (PROPOSED) | Signal source |
|:---|:---|:---|:---|
| Release-manifest completeness | % of releases shipping with a `ReleaseManifest` carrying all required facets | 100% | `ReleaseManifest` validator |
| Correction-notice latency | Time from defect-confirmation to `CorrectionNotice` publication | p95 < 5 business days *(PROPOSED)* | `CorrectionNotice` records |
| Rollback-card coverage | % of released artifacts with a corresponding `RollbackCard` plan on file | 100% for materiality ≥ moderate; ≥ 95% overall | `RollbackCard` registry |
| Supersession-chain integrity | % of superseded artifacts whose `supersededBy` chain resolves to a current artifact | 100% | Atlas §24.8 supersession validator |
| Release-readiness gate pass-rate | % of release candidates passing all promotion gates without override | ≥ 90% over trailing 90d *(PROPOSED)* | Promotion-gate signals; cross-link to `promotion-gate-status.md` |

[↑ back to top](#top)

---

## 3. Per-domain breakdowns

Most §24.11.2 indicators apply system-wide, not per-domain. Where per-domain release cadences differ materially (e.g., hydrology continuous releases vs archaeology episodic releases), the per-domain spec calls out the variation:

- `docs/dashboards/domain/hydrology.md` *(continuous release cadence)*
- `docs/dashboards/domain/archaeology.md` *(episodic; correction-notice latency budget may differ)*
- *…other domain specs as applicable.*

[↑ back to top](#top)

---

## 4. Ownership

- **Docs steward:** OWNER_TBD
- **Governance-health steward:** OWNER_TBD
- **Release authority:** OWNER_TBD *(required — §24.11.2 indicators trigger release-authority owner per parent README §3).*
- **Implementation owner:** OWNER_TBD

[↑ back to top](#top)

---

## 5. Implementation pointer

- **Dashboard app:** `apps/review-console/release-health/` *(PROPOSED; NEEDS VERIFICATION)*; alternatively future `apps/dashboards/governance/release/`.
- **Telemetry:** Release-pipeline OTel root trace (cross-link to `docs/dashboards/observability/ingest-run-trace-coverage.md`).
- **Schemas read:** `schemas/contracts/v1/release/ReleaseManifest.schema.json`, `CorrectionNotice.schema.json`, `RollbackCard.schema.json` *(NEEDS VERIFICATION).*
- **Policy bundles emitting signals:** `policy/release/manifest-completeness/`, `policy/release/rollback-coverage/` *(PROPOSED).*
- **Registers visualized:** `docs/registers/DRIFT_REGISTER.md` (correction-notice latency overruns recorded as drift); cross-link to `docs/dashboards/governance/rollback-correction-lineage.md` for per-event lineage.
- **Related release-lifecycle spec:** `docs/dashboards/release/` *(PROPOSED sibling — per-release detail).*

[↑ back to top](#top)

---

## 6. Review cadence

- Reviewed quarterly.
- Trigger events: Atlas §24.11.2 amendment, `ReleaseManifest` schema change, addition of a new release gate, materiality threshold revision.

[↑ back to top](#top)

---

## 7. Open questions

- **OPEN-DASH-GOV-RCR-01** — Boundary with the PROPOSED `release/` sibling (inherits OPEN-DASH-GOV-01).
- **OPEN-DASH-GOV-RCR-02** — Correction-notice latency budget: is p95 < 5 business days the right system-wide threshold, or per-materiality?
- **OPEN-DASH-GOV-RCR-03** — Reconcile this kebab-case spec with the pre-existing `RELEASE_CORRECTION_ROLLBACK.md`.

[↑ back to top](#top)

---

## 8. Evidence basis & citations

| Source | Status | Supports |
|:---|:---|:---|
| Atlas v1.1 §24.11.2 (Release, Correction, Rollback — 5 indicators) | CONFIRMED (manuscript) | §1, §2 indicator catalog. |
| Atlas v1.1 §24.8 (Stale-State / Supersession Reference) | CONFIRMED (manuscript) | §2 supersession-chain integrity. |
| Atlas v1.1 §24.6 (Pipeline Gates) | CONFIRMED (manuscript) | §2 release-readiness gate cross-link. |
| `docs/dashboards/governance/README.md` | CONFIRMED (this folder) | §6 template; OPEN-DASH-GOV-01 boundary. |
| `docs/registers/DRIFT_REGISTER.md` | CONFIRMED (corpus, mounted-repo NEEDS VERIFICATION) | §5 register pointer. |

<sub>Specification only. System-wide trend; per-release detail lives in the PROPOSED `release/` sibling.</sub>
