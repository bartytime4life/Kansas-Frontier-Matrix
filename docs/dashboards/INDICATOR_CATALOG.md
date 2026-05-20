<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid-pending>
title: Indicator Catalog — Master Governance Health Indicators (mirror of Atlas v1.1 Ch. 24.11)
type: standard
version: v0.1
status: draft
owners: <dashboards-stewards>  # PROPOSED placeholder; resolve before review
created: 2026-05-20
updated: 2026-05-20
policy_label: public
related:
  - docs/dashboards/README.md
  - docs/dashboards/DASHBOARD_CATALOG.md
  - docs/atlases/Kansas_Frontier_Matrix_-_Domains_v1_1.md   # Ch. 24.11 (authoritative source)
  - docs/registers/VERIFICATION_BACKLOG.md                  # VB-11-08
tags: [kfm, docs, dashboards, indicators, governance, health]
notes:
  - "This file is a human-readable MIRROR of Atlas v1.1 Ch. 24.11. The Atlas is authoritative."
  - "If this mirror and the Atlas disagree, the Atlas wins; the discrepancy goes to the drift register."
  - "Indicators are REPORTED, not enforced — enforcement is the validator's job (Atlas v1.1 §24.11 preamble)."
[/KFM_META_BLOCK_V2] -->

# Indicator Catalog · `docs/dashboards/INDICATOR_CATALOG.md`

> A human-readable mirror of the **Master Governance Health Indicators** (Atlas v1.1
> Ch. 24.11, CONFIRMED doctrine), with each indicator's measurement, healthy posture,
> owning steward (PROPOSED), receipt sources, and the dashboard spec that surfaces it.

![Authority](https://img.shields.io/badge/authority-PROPOSED-orange)
![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Truth posture](https://img.shields.io/badge/truth-cite--or--abstain-blue)
![Policy label](https://img.shields.io/badge/policy-public-brightgreen)
![Source](https://img.shields.io/badge/source-Atlas%20v1.1%20Ch.%2024.11-informational)

**Status:** draft · **Owners:** `<dashboards-stewards>` (PROPOSED) · **Last reviewed:** 2026-05-20

---

> [!IMPORTANT]
> **This catalog mirrors doctrine; it is not doctrine.** Atlas v1.1 Ch. 24.11 is the
> authoritative source. This file adds dashboard mappings and receipt pointers for
> day-to-day authoring. None of these indicators is a *sufficient* condition for trust —
> together they describe a healthy posture. Indicators are **reported, not enforced**.

---

## Quick jump

- [1. Scope](#1-scope)
- [2. Category 24.11.1 — Evidence and source integrity](#2-category-24111--evidence-and-source-integrity)
- [3. Category 24.11.2 — Release, correction, rollback](#3-category-24112--release-correction-rollback)
- [4. Category 24.11.3 — Sensitivity and rights](#4-category-24113--sensitivity-and-rights)
- [5. Category 24.11.4 — AI surface health](#5-category-24114--ai-surface-health)
- [6. Category 24.11.5 — Documentation and drift](#6-category-24115--documentation-and-drift)
- [7. Coverage matrix](#7-coverage-matrix)
- [8. Open questions](#8-open-questions)

---

## 1. Scope

This catalog enumerates the **23 governance health indicators** across five categories
defined in Atlas v1.1 Ch. 24.11. For each indicator it records:

- **Measures** — what the signal counts or computes.
- **Healthy posture (PROPOSED)** — the target state per the Atlas.
- **Owning steward (PROPOSED)** — the role accountable for the indicator; resolve against
  Atlas v1.1 §24.7 (Reviewer Role and Separation-of-Duties Matrix).
- **Receipt sources** — the receipt/record types a dashboard reads to compute the signal.
- **Dashboard spec** — the `docs/dashboards/` spec file that surfaces the indicator.

[↑ back to top](#indicator-catalog--docsdashboardsindicator_catalogmd)

---

## 2. Category 24.11.1 — Evidence and source integrity

Surfaced by [`governance/EVIDENCE_INTEGRITY.md`](governance/EVIDENCE_INTEGRITY.md).

| Indicator | Measures | Healthy posture (PROPOSED) | Owning steward (PROPOSED) | Receipt sources |
|---|---|---|---|---|
| EvidenceRef resolution rate | % of public-surface EvidenceRefs that resolve to an EvidenceBundle on demand. | > 99.9% over the trailing release window. | Release steward | `ValidationReport`, EvidenceBundle index |
| Cite-or-abstain compliance | % of Focus Mode answers with non-empty, resolving evidence citations. | 100% (any miss is a defect to investigate). | AI surface steward | `AIReceipt` |
| Source-role distribution drift | Distribution of admitted source roles over time per domain. | No silent shift without a documented ADR or steward note. | Source steward | Source descriptors, `ValidationReport` |
| Stale source rate | % of admitted sources past their freshness cadence. | Stewards dispositioned (refresh / supersede / mark stale) within tolerance. | Source steward | Source descriptors, freshness cadence metadata |
| Quarantine throughput | % of admitted records that quarantine + the rate of clearance. | Visible, with cause distribution; sustained backlog is a defect. | Source steward | `ValidationReport`, quarantine ledger |

[↑ back to top](#indicator-catalog--docsdashboardsindicator_catalogmd)

---

## 3. Category 24.11.2 — Release, correction, rollback

Surfaced by [`governance/RELEASE_CORRECTION_ROLLBACK.md`](governance/RELEASE_CORRECTION_ROLLBACK.md).

| Indicator | Measures | Healthy posture (PROPOSED) | Owning steward (PROPOSED) | Receipt sources |
|---|---|---|---|---|
| Release with rollback target | % of PUBLISHED releases that name a valid rollback target. | 100%. | Release steward | `ReleaseManifest`, `RollbackCard` |
| Correction lead time | Median time from defect detection to `CorrectionNotice`. | Visibly tracked; trend not regressing. | Correction reviewer | `CorrectionNotice` |
| Derivative-invalidation coverage | % of corrections that name and invalidate downstream derivatives. | Approaches 100% as coverage matures. | Correction reviewer | `CorrectionNotice`, lineage graph |
| Rollback rehearsal rate | Number of rehearsed rollbacks per release window. | Non-zero; periodic, scheduled. | Release steward | `RollbackCard` |
| Supersession lineage gap | Number of supersessions without a forward link. | Zero. | Docs steward | `ReleaseManifest`, supersession entries |

[↑ back to top](#indicator-catalog--docsdashboardsindicator_catalogmd)

---

## 4. Category 24.11.3 — Sensitivity and rights

Surfaced by [`governance/SENSITIVITY_RIGHTS.md`](governance/SENSITIVITY_RIGHTS.md).

| Indicator | Measures | Healthy posture (PROPOSED) | Owning steward (PROPOSED) | Receipt sources |
|---|---|---|---|---|
| Sensitive-lane fail-closed rate | % of unauthorized sensitive-lane requests that DENY at the first gate. | 100% at the first gate. | Sensitivity reviewer | `PolicyDecision` |
| RedactionReceipt coverage | % of public-safe transformations that emit a `RedactionReceipt`. | 100% for sensitive lanes. | Sensitivity reviewer | `RedactionReceipt` |
| Review-aged-out incidence | Number of sensitive-lane claims past their review cadence. | Visibly tracked; trend not regressing. | Sensitivity reviewer | `ReviewRecord` |
| Rights-change response time | Median time from rights-change detection to tier reassignment. | Within stated tolerance per source family. | Rights-holder representative | Source descriptors, `ReviewRecord` |
| Sensitive-content side-channel audit | Frequency of automated checks for label / popup / AI-text leaks. | Periodic; documented. | Sensitivity reviewer | Audit logs, `RepresentationReceipt` |

[↑ back to top](#indicator-catalog--docsdashboardsindicator_catalogmd)

---

## 5. Category 24.11.4 — AI surface health

Surfaced by [`governance/AI_SURFACE_HEALTH.md`](governance/AI_SURFACE_HEALTH.md).

| Indicator | Measures | Healthy posture (PROPOSED) | Owning steward (PROPOSED) | Receipt sources |
|---|---|---|---|---|
| AIReceipt presence rate | % of Focus Mode answers with an `AIReceipt`. | 100%. | AI surface steward | `AIReceipt` |
| ABSTAIN rate by template | How often each Focus Mode template abstains. | Visibly tracked; very low suggests over-fitting; very high suggests evidence gaps. | AI surface steward | `AIReceipt` |
| DENY reason distribution | Reason codes returned by Focus Mode denials. | Stable; large new-reason spikes investigated. | AI surface steward | `AIReceipt`, `PolicyDecision` |
| Synthetic-claim incidence | % of audited AI answers flagged for presenting synthetic content as observed. | Approaches zero; never silently. | AI surface steward | `AIReceipt`, audit sample |

[↑ back to top](#indicator-catalog--docsdashboardsindicator_catalogmd)

---

## 6. Category 24.11.5 — Documentation and drift

Surfaced by [`governance/DOCUMENTATION_DRIFT.md`](governance/DOCUMENTATION_DRIFT.md).

| Indicator | Measures | Healthy posture (PROPOSED) | Owning steward (PROPOSED) | Receipt sources |
|---|---|---|---|---|
| ADR completeness | % of structural moves with an accepted ADR. | 100% for Directory Rules §2.4 cases. | Docs steward | `docs/adr/`, drift register |
| Drift register size | Open entries in `docs/registers/DRIFT_REGISTER.md`. | Visibly tracked; aged entries investigated. | Docs steward | `DRIFT_REGISTER.md` |
| Per-root README presence | % of canonical roots with a current README declaring authority class. | 100%. | Docs steward | Repo tree scan |
| Atlas / supplement lineage clarity | Each Atlas/supplement carries a current supersession entry. | 100%. | Docs steward | Atlas front-matter, supersession entries |

[↑ back to top](#indicator-catalog--docsdashboardsindicator_catalogmd)

---

## 7. Coverage matrix

CONFIRMED: every Atlas v1.1 Ch. 24.11 indicator below maps to exactly one dashboard spec.
Coverage is checked by `DASH-OQ-08` (indicator-coverage CI check).

| Atlas section | Indicators | Dashboard spec | Status |
|---|---|---|---|
| §24.11.1 Evidence and source integrity | 5 | `governance/EVIDENCE_INTEGRITY.md` | PROPOSED |
| §24.11.2 Release, correction, rollback | 5 | `governance/RELEASE_CORRECTION_ROLLBACK.md` | PROPOSED |
| §24.11.3 Sensitivity and rights | 5 | `governance/SENSITIVITY_RIGHTS.md` | PROPOSED |
| §24.11.4 AI surface health | 4 | `governance/AI_SURFACE_HEALTH.md` | PROPOSED |
| §24.11.5 Documentation and drift | 4 | `governance/DOCUMENTATION_DRIFT.md` | PROPOSED |
| **Total** | **23** | 5 governance specs | — |

[↑ back to top](#indicator-catalog--docsdashboardsindicator_catalogmd)

---

## 8. Open questions

- [ ] **IND-OQ-01 — Owner reconciliation.** Replace every PROPOSED owning-steward value
  with a concrete role from Atlas v1.1 §24.7. Tracked alongside `DASH-OQ-04`.
- [ ] **IND-OQ-02 — Receipt-source verification.** Confirm each "Receipt sources" cell
  against the canonical receipt catalog (Atlas v1.1 §24.2) and `schemas/contracts/v1/receipts/`.
- [ ] **IND-OQ-03 — Mirror freshness check.** Add a CI check that diffs this mirror
  against Atlas v1.1 Ch. 24.11 and fails on divergence (links to `DASH-OQ-08`).
- [ ] **IND-OQ-04 — `VB-11-08` linkage.** Atlas v1.1 Appendix G `VB-11-08` requires each
  indicator to be "instrumented or owned by a steward." Close the catalog half here.

[↑ back to top](#indicator-catalog--docsdashboardsindicator_catalogmd)

---

**Related docs:** [README.md](README.md) · [DASHBOARD_CATALOG.md](DASHBOARD_CATALOG.md) ·
[atlases/ — Atlas v1.1 Ch. 24.11](../atlases/) ·
[registers/VERIFICATION_BACKLOG.md](../registers/VERIFICATION_BACKLOG.md)

**Last updated:** 2026-05-20 · **Edition:** v0.1 (draft) · **Owners:** `<dashboards-stewards>` (PROPOSED)
