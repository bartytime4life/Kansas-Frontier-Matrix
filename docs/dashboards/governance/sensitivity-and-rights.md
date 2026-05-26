<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-governance-sensitivity-and-rights
title: Sensitivity and Rights (system-wide governance health spec; Atlas §24.11.3)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: docs steward + governance-health steward + sensitivity reviewer (Atlas §24.7)
created: 2026-05-26
updated: 2026-05-26
policy_label: public
related:
  - kfm://doc/dashboards-governance-readme
  - kfm://doc/atlas-v1-1                      # §24.11.3 — 5 indicators
  - kfm://doc/atlas-v1-1-ch24-5-sensitivity-tier-reference
  - kfm://doc/dashboards-domain-readme
  - kfm://register/drift
tags: [kfm, dashboards, governance, sensitivity, rights, license, 24-11-3]
notes:
  - Indicator catalog: Atlas §24.11.3 (5 indicators); labeled PROPOSED in source.
  - Sensitivity reviewer (Atlas §24.7 reviewer/SoD matrix) MUST be on the owner roster.
  - Some indicators (side-channel audits) may be steward-only — OPEN-DASH-GOV-06 from parent README.
[/KFM_META_BLOCK_V2] -->

# Sensitivity and Rights

<!-- [doc: kfm://doc/dashboards-governance-sensitivity-and-rights] -->
<a id="top"></a>

> System-wide governance health view of sensitivity tier handling and rights compliance — sensitivity-label coverage, license-clearance coverage, T3+ redaction conformance, review-aged-out count, and side-channel audit posture. Atlas §24.11.3.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Scope: system-wide" src="https://img.shields.io/badge/scope-system--wide-informational">
  <img alt="Atlas §24.11.3" src="https://img.shields.io/badge/atlas-%C2%A724.11.3-purple">
  <img alt="Indicators: 5" src="https://img.shields.io/badge/indicators-5-yellow">
  <img alt="Policy label: public (with steward-only exception)" src="https://img.shields.io/badge/policy--label-public%20%28steward--only%20exception%29-orange">
</p>

> [!IMPORTANT]
> **Truth posture.** Indicator catalog from Atlas §24.11.3 (CONFIRMED text, PROPOSED indicators). The **side-channel audit** indicator may need to live as a steward-only periodic report rather than a public dashboard panel — see OPEN-DASH-GOV-06 from the parent README.

> [!CAUTION]
> **Sensitive-content posture for this dashboard itself.** Aggregate indicators are safe for public surfacing; per-record drill-downs and side-channel audit detail are **internal-only** with named sensitivity-reviewer access (Atlas §24.7).

---

## 1. Scope

- **Atlas reference:** §24.11.3 — Sensitivity and Rights (5 indicators).
- **Audience:** Sensitivity reviewer (Atlas §24.7), governance-health steward, docs steward, license owner.
- **Aggregation scope:** System-wide rollups. Per-domain and per-tier breakdowns live in `docs/dashboards/domain/<domain>.md`.

[↑ back to top](#top)

---

## 2. Indicators

| Indicator | What it measures | Healthy posture (PROPOSED) | Signal source |
|:---|:---|:---|:---|
| Sensitivity-label coverage | % of records carrying a declared sensitivity tier (T0–T4) | 100% on the active manifest | `policy_label` facet + sensitivity-tier validator |
| License-clearance coverage | % of records carrying a resolved license declaration | 100% for public-facing records | License-clearance validator |
| T3+ redaction conformance | % of public-surface emissions that comply with T3/T4 default-deny rules | 100% *(non-100% is an incident)* | Redaction-enforcement processor + audit log |
| Review-aged-out count | Count of records past the review-window-due-date without re-review | 0 on the active manifest *(trending metric otherwise)* | Review-tracking validator |
| Side-channel audit posture | Posture summary of side-channel-audit findings (see §24.11.3 last indicator) | All open findings have a triage state | Side-channel audit reports *(see OPEN-DASH-GOV-06)* |

[↑ back to top](#top)

---

## 3. Per-domain breakdowns

Sensitivity indicators are strongly per-domain because tier defaults differ (archaeology T4 default-deny; hydrology mostly T0–T1). Reciprocal links:

- `docs/dashboards/domain/archaeology.md` *(T4 default-deny — coordinate-suppression conformance)*
- `docs/dashboards/domain/fauna-flora.md` *(rare-species T4)*
- `docs/dashboards/domain/settlements-infrastructure.md` *(critical-infrastructure T4)*
- `docs/dashboards/domain/hydrology.md` *(predominantly T0–T1; license-clearance focus)*
- *…other domain specs as applicable.*

[↑ back to top](#top)

---

## 4. Ownership

- **Docs steward:** OWNER_TBD
- **Governance-health steward:** OWNER_TBD
- **Sensitivity reviewer (Atlas §24.7):** OWNER_TBD *(required).*
- **License owner:** OWNER_TBD
- **Implementation owner:** OWNER_TBD

[↑ back to top](#top)

---

## 5. Implementation pointer

- **Dashboard app:** `apps/review-console/sensitivity-rights/` *(PROPOSED; NEEDS VERIFICATION)*; side-channel audit panel may live in a steward-only `apps/admin/` view.
- **Telemetry:** `runtime/observability/sensitivity-enforcement/` *(PROPOSED).*
- **Schemas read:** `schemas/contracts/v1/sensitivity/SensitivityLabel.schema.json`, `schemas/contracts/v1/license/LicenseDeclaration.schema.json` *(NEEDS VERIFICATION).*
- **Policy bundles emitting signals:** `policy/sensitivity/tier-defaults/`, `policy/license/clearance/` *(PROPOSED).*
- **Registers visualized:** `docs/registers/DRIFT_REGISTER.md` (label-coverage gaps), `docs/registers/VERIFICATION_BACKLOG.md` (review-aged-out backlog).
- **Related observability:** `docs/dashboards/observability/pmtiles-range-diagnostics.md` (suppressed-region access attempts), `docs/dashboards/observability/focus-overlay-telemetry.md` (UI dwell suppression).

[↑ back to top](#top)

---

## 6. Review cadence

- Reviewed quarterly.
- Trigger events: Atlas §24.11.3 amendment, §24.5 sensitivity-tier reclassification, license-policy change, side-channel-audit finding intake.

[↑ back to top](#top)

---

## 7. Open questions

- **OPEN-DASH-GOV-SR-01** — Side-channel audit posture: public summary panel, steward-only panel, or periodic report only? Inherits OPEN-DASH-GOV-06 from parent.
- **OPEN-DASH-GOV-SR-02** — How is "review-aged-out" age budget set — per-tier (T2: 90d, T3: 60d, T4: 30d PROPOSED) or per-domain?
- **OPEN-DASH-GOV-SR-03** — Reconcile this kebab-case spec with the pre-existing `SENSITIVITY_RIGHTS.md`.

[↑ back to top](#top)

---

## 8. Evidence basis & citations

| Source | Status | Supports |
|:---|:---|:---|
| Atlas v1.1 §24.11.3 (Sensitivity and Rights — 5 indicators) | CONFIRMED (manuscript) | §1, §2 indicator catalog. |
| Atlas v1.1 §24.5 (Sensitivity Tier Reference) | CONFIRMED (prior-session authored chapter file) | §2 tier defaults; §3 per-domain breakdowns. |
| Atlas v1.1 §24.7 (Reviewer / SoD Matrix) | CONFIRMED (manuscript) | §4 sensitivity-reviewer ownership requirement. |
| `docs/dashboards/governance/README.md` | CONFIRMED (this folder) | §6 template; OPEN-DASH-GOV-06. |

<sub>Specification only. Aggregate posture is public; per-record drill-down and side-channel detail are sensitivity-reviewer-gated.</sub>
