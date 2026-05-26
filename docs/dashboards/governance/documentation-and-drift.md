<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-governance-documentation-and-drift
title: Documentation and Drift (system-wide governance health spec; Atlas §24.11.5)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: docs steward + governance-health steward
created: 2026-05-26
updated: 2026-05-26
policy_label: public
related:
  - kfm://doc/dashboards-governance-readme
  - kfm://doc/atlas-v1-1                      # §24.11.5 — 4 indicators
  - kfm://register/drift                      # docs/registers/DRIFT_REGISTER.md
  - kfm://register/verification-backlog       # docs/registers/VERIFICATION_BACKLOG.md
tags: [kfm, dashboards, governance, documentation, drift, adr, 24-11-5]
notes:
  - Indicator catalog: Atlas §24.11.5 (4 indicators); labeled PROPOSED in source.
  - Strong register-mirror watch — this dashboard visualizes drift, ADR completeness, doc freshness; it does NOT mirror those data sources.
[/KFM_META_BLOCK_V2] -->

# Documentation and Drift

<!-- [doc: kfm://doc/dashboards-governance-documentation-and-drift] -->
<a id="top"></a>

> System-wide governance health view of documentation freshness and drift posture — doc-freshness coverage, drift-register triage state, ADR completeness, and stale-link rate. Atlas §24.11.5.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Scope: system-wide" src="https://img.shields.io/badge/scope-system--wide-informational">
  <img alt="Atlas §24.11.5" src="https://img.shields.io/badge/atlas-%C2%A724.11.5-purple">
  <img alt="Indicators: 4" src="https://img.shields.io/badge/indicators-4-yellow">
  <img alt="Policy label: public" src="https://img.shields.io/badge/policy--label-public-lightgrey">
</p>

> [!IMPORTANT]
> **Truth posture.** Indicator catalog from Atlas §24.11.5 (CONFIRMED text, PROPOSED indicators). This dashboard is **the** most register-adjacent spec in this folder — strict register-mirror watch applies (parent README §4 / §11). It visualizes counts and trends; the canonical data lives in `docs/registers/DRIFT_REGISTER.md`, `docs/adr/`, and the docs-freshness validator.

---

## 1. Scope

- **Atlas reference:** §24.11.5 — Documentation and Drift (4 indicators).
- **Audience:** Docs steward, governance-health steward, ADR-owner roster.
- **Aggregation scope:** System-wide rollup; per-lane breakdown supported (per `docs/` lane); register-data drill-down lives in the registers themselves.

[↑ back to top](#top)

---

## 2. Indicators

| Indicator | What it measures | Healthy posture (PROPOSED) | Signal source |
|:---|:---|:---|:---|
| Doc-freshness coverage | % of doctrine docs with a `last-reviewed` date within their cadence budget | ≥ 95% system-wide | Docs-freshness validator |
| Drift-register triage state | % of open drift entries with a triage state (new / accepted / scheduled / closed) | 100% have a state; **no item is "unset"** | `docs/registers/DRIFT_REGISTER.md` *(pointer, not mirror)* |
| ADR completeness | % of significant decisions captured as ADRs in `docs/adr/` | ≥ 90% *(PROPOSED — relates to OPEN-DASH-GOV-04)* | `docs/adr/` registry |
| Stale-link rate | % of internal cross-references that resolve | ≥ 99.5% | Link-check validator (CI) |

[↑ back to top](#top)

---

## 3. Per-domain breakdowns

Most §24.11.5 indicators are doc-lane-scoped rather than domain-scoped. Per-domain breakdowns surface only where doctrine docs are domain-specific:

- `docs/dashboards/domain/<domain>.md` *(per-domain doc-freshness when domain doctrine docs exist)*

Per-lane breakdowns (e.g., `docs/atlases/`, `docs/standards/`, `docs/doctrine/`) are not in scope for this folder — they belong in a future lane-health spec or as a `docs/registers/` view.

[↑ back to top](#top)

---

## 4. Ownership

- **Docs steward:** OWNER_TBD
- **Governance-health steward:** OWNER_TBD
- **ADR-owner roster:** OWNER_TBD *(rotating per ADR class).*
- **Implementation owner:** OWNER_TBD

[↑ back to top](#top)

---

## 5. Implementation pointer

- **Dashboard app:** `apps/review-console/docs-drift/` *(PROPOSED; NEEDS VERIFICATION)*.
- **Telemetry:** Docs-freshness validator CI output; link-check CI output.
- **Schemas read:** `schemas/contracts/v1/drift/DriftEntry.schema.json` *(PROPOSED / NEEDS VERIFICATION).*
- **Policy bundles emitting signals:** `policy/docs/freshness-cadence/`, `policy/docs/link-integrity/` *(PROPOSED).*
- **Registers visualized:** `docs/registers/DRIFT_REGISTER.md` *(pointer only — never mirror)*, `docs/adr/` *(pointer only)*, `docs/registers/VERIFICATION_BACKLOG.md`.

> [!WARNING]
> **Register-mirror watch.** This spec MUST NOT enumerate drift entries, ADR IDs, or backlog items. Counts and trends only; click-through goes to the canonical register.

[↑ back to top](#top)

---

## 6. Review cadence

- Reviewed quarterly.
- Trigger events: Atlas §24.11.5 amendment, `DriftEntry` schema change, ADR template revision, link-check validator change.

[↑ back to top](#top)

---

## 7. Open questions

- **OPEN-DASH-GOV-DOC-01** — ADR-completeness home: here as a dashboard or as a section in `docs/adr/README.md`? Inherits OPEN-DASH-GOV-04 from parent.
- **OPEN-DASH-GOV-DOC-02** — Per-lane doc-freshness rollup: in this spec, in a sibling spec, or in `docs/registers/`?
- **OPEN-DASH-GOV-DOC-03** — Self-referential indicator: should this dashboard report on its own last-reviewed date? Inherits OPEN-DASH-GOV-08 from parent.
- **OPEN-DASH-GOV-DOC-04** — Reconcile this kebab-case spec with the pre-existing `DOCUMENTATION_DRIFT.md`.

[↑ back to top](#top)

---

## 8. Evidence basis & citations

| Source | Status | Supports |
|:---|:---|:---|
| Atlas v1.1 §24.11.5 (Documentation and Drift — 4 indicators) | CONFIRMED (manuscript) | §1, §2 indicator catalog. |
| `docs/registers/DRIFT_REGISTER.md` | CONFIRMED (corpus, mounted-repo NEEDS VERIFICATION) | §5 register pointer. |
| `docs/adr/` (lane) | CONFIRMED (corpus, mounted-repo NEEDS VERIFICATION) | §2 ADR-completeness signal. |
| `docs/registers/VERIFICATION_BACKLOG.md` | CONFIRMED | §5 backlog pointer. |
| `docs/dashboards/governance/README.md` | CONFIRMED (this folder) | §6 template; §4 register-mirror watch. |

<sub>Specification only. Visualizes registers; never mirrors them. Counts and trends here; canonical data in `docs/registers/` and `docs/adr/`.</sub>
