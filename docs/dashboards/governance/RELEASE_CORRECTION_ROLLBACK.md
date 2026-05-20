<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid-pending>
title: Release / Correction / Rollback Dashboard — specification
type: standard
version: v0.1
status: draft
owners: <release-steward>, <correction-reviewer>  # PROPOSED placeholders; resolve before review
created: 2026-05-20
updated: 2026-05-20
policy_label: public
related:
  - docs/dashboards/README.md
  - docs/dashboards/INDICATOR_CATALOG.md
  - docs/dashboards/DASHBOARD_CATALOG.md
  - docs/atlases/Kansas_Frontier_Matrix_-_Domains_v1_1.md   # §24.11.2
  - docs/standards/RELEASE_MANIFEST.md
  - docs/runbooks/ROLLBACK_RUNBOOK.md
  - docs/runbooks/EVIDENCE_CORRECTION.md
tags: [kfm, dashboards, governance, release, correction, rollback, indicators]
notes:
  - "Source of indicators: Atlas v1.1 §24.11.2 (CONFIRMED doctrine)."
  - "This is a SPEC for a dashboard, not the running dashboard. Indicators are reported, not enforced."
  - "Mounted-repo state UNKNOWN; running-surface and receipt-path claims are PROPOSED / NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

# Release / Correction / Rollback Dashboard · `governance/RELEASE_CORRECTION_ROLLBACK.md`

> Dashboard specification for the **Release, correction, rollback** governance-health
> category (Atlas v1.1 §24.11.2). Tracks whether every PUBLISHED release can be safely
> withdrawn and whether corrections propagate to their derivatives.

![Authority](https://img.shields.io/badge/authority-PROPOSED-orange)
![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Category](https://img.shields.io/badge/category-governance-blue)
![Source](https://img.shields.io/badge/source-Atlas%20%C2%A724.11.2-informational)
![Policy label](https://img.shields.io/badge/policy-public-brightgreen)

**Status:** draft · **Owners:** `<release-steward>`, `<correction-reviewer>` (PROPOSED) · **Last reviewed:** 2026-05-20

---

> [!IMPORTANT]
> This dashboard **reports** release-safety posture. A green panel is not a release
> decision — the `ReleaseManifest` and the release steward's `ReviewRecord` are.

---

## 1. Description

The Release / Correction / Rollback dashboard answers: **if a PUBLISHED release turns out
to be wrong, can we withdraw it cleanly, and do corrections reach everything downstream?**
It surfaces the five Atlas v1.1 §24.11.2 indicators so the release and correction
reviewers see rollback readiness and correction propagation at a glance.

## 2. Indicators surfaced

| # | Indicator | Measures | Healthy posture (PROPOSED) | Negative state |
|---|---|---|---|---|
| 1 | Release with rollback target | % of PUBLISHED releases that name a valid rollback target. | 100%. | `RELEASE_NO_ROLLBACK` |
| 2 | Correction lead time | Median time from defect detection to `CorrectionNotice`. | Visibly tracked; trend not regressing. | `CORRECTION_LAGGING` |
| 3 | Derivative-invalidation coverage | % of corrections that name and invalidate downstream derivatives. | Approaches 100% as coverage matures. | `DERIVATIVE_NOT_INVALIDATED` |
| 4 | Rollback rehearsal rate | Number of rehearsed rollbacks per release window. | Non-zero; periodic, scheduled. | `ROLLBACK_UNREHEARSED` |
| 5 | Supersession lineage gap | Number of supersessions without a forward link. | Zero. | `SUPERSESSION_GAP` |

## 3. Panels (PROPOSED)

- **Rollback coverage** — single-stat, % of PUBLISHED releases with a valid target.
- **Correction lead time** — median + p90 trend line, per defect class.
- **Derivative invalidation** — Sankey from `CorrectionNotice` to invalidated derivatives.
- **Rehearsal calendar** — heatmap of rehearsed rollbacks per release window.
- **Lineage gaps** — table of supersessions missing a forward link (target: empty).

## 4. Inputs — receipts and records read

CONFIRMED receipt types (Atlas v1.1 §24.2); mounted-repo paths NEEDS VERIFICATION.

- `ReleaseManifest` — release identity, rollback target, supersession entries.
- `RollbackCard` — rehearsal records and rollback-target validity.
- `CorrectionNotice` — defect-detection timestamps, derivative invalidation lists.
- Lineage graph — derivative relationships for invalidation coverage.

## 5. Files

| Path | Role | spec_hash |
|---|---|---|
| `docs/dashboards/governance/RELEASE_CORRECTION_ROLLBACK.md` | This dashboard specification. | PROPOSED — pending JCS+SHA-256 |
| Running surface (PROPOSED) | `apps/review-console/` release-health panel. | NEEDS VERIFICATION |

## 6. Ownership and review burden

- **Owning stewards (PROPOSED):** Release steward (indicators 1, 4), Correction reviewer
  (indicators 2–3), Docs steward (indicator 5).
- **Review burden:** docs steward + the owning stewards. Resolve placeholders against
  Atlas v1.1 §24.7 before review.

## 7. Acceptance

- [ ] All five §24.11.2 indicators present and matching [`INDICATOR_CATALOG.md`](../INDICATOR_CATALOG.md).
- [ ] Every receipt type in §4 exists in the Atlas v1.1 §24.2 receipt catalog.
- [ ] Owners named (no anonymous spec at v1).
- [ ] Link check passes; row present in [`DASHBOARD_CATALOG.md`](../DASHBOARD_CATALOG.md).
- [ ] Cross-links to `docs/runbooks/ROLLBACK_RUNBOOK.md` and `EVIDENCE_CORRECTION.md` resolve.

## 8. Open questions

- [ ] **RCR-OQ-01** — Confirm the running surface and downgrade if unverified.
- [ ] **RCR-OQ-02** — Define the "release window" unit (per tag? per calendar quarter?).
- [ ] **RCR-OQ-03** — Confirm negative-state names against Unified Doctrine §19; several
  here (`RELEASE_NO_ROLLBACK`, `SUPERSESSION_GAP`) may be proposed additions.

---

**Related docs:** [README.md](../README.md) · [INDICATOR_CATALOG.md](../INDICATOR_CATALOG.md) ·
[DASHBOARD_CATALOG.md](../DASHBOARD_CATALOG.md) ·
[runbooks/ROLLBACK_RUNBOOK.md](../../runbooks/ROLLBACK_RUNBOOK.md)

**Last updated:** 2026-05-20 · **Edition:** v0.1 (draft) · **Owners:** `<release-steward>`, `<correction-reviewer>` (PROPOSED)
