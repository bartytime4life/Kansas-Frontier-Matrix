<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid-pending>
title: Documentation Drift Dashboard — specification
type: standard
version: v0.1
status: draft
owners: <docs-steward>  # PROPOSED placeholder; resolve before review
created: 2026-05-20
updated: 2026-05-20
policy_label: public
related:
  - docs/dashboards/README.md
  - docs/dashboards/INDICATOR_CATALOG.md
  - docs/dashboards/DASHBOARD_CATALOG.md
  - docs/atlases/Kansas_Frontier_Matrix_-_Domains_v1_1.md   # §24.11.5
  - docs/doctrine/directory-rules.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/adr/
tags: [kfm, dashboards, governance, documentation, drift, adr, indicators]
notes:
  - "Source of indicators: Atlas v1.1 §24.11.5 (CONFIRMED doctrine)."
  - "This is a SPEC for a dashboard, not the running dashboard. Indicators are reported, not enforced."
  - "Mounted-repo state UNKNOWN; running-surface and receipt-path claims are PROPOSED / NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

# Documentation Drift Dashboard · `governance/DOCUMENTATION_DRIFT.md`

> Dashboard specification for the **Documentation and drift** governance-health category
> (Atlas v1.1 §24.11.5). Tracks whether structural moves carry ADRs, whether the drift
> register is managed, and whether every canonical root has a current README.

![Authority](https://img.shields.io/badge/authority-PROPOSED-orange)
![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Category](https://img.shields.io/badge/category-governance-blue)
![Source](https://img.shields.io/badge/source-Atlas%20%C2%A724.11.5-informational)
![Policy label](https://img.shields.io/badge/policy-public-brightgreen)

**Status:** draft · **Owners:** `<docs-steward>` (PROPOSED) · **Last reviewed:** 2026-05-20

---

> [!IMPORTANT]
> This dashboard measures the health of the documentation control plane itself —
> including, recursively, the PROPOSED placement of `docs/dashboards/`. Its own folder
> is a live drift case (see [README drift notice](../README.md)).

---

## 1. Description

The Documentation Drift dashboard answers: **is the human-facing control plane keeping
pace with the repo?** It surfaces the four Atlas v1.1 §24.11.5 indicators so the docs
steward can see ADR completeness, the size and age of the drift register, README
coverage of canonical roots, and Atlas/supplement lineage clarity.

## 2. Indicators surfaced

| # | Indicator | Measures | Healthy posture (PROPOSED) | Negative state |
|---|---|---|---|---|
| 1 | ADR completeness | % of structural moves with an accepted ADR. | 100% for Directory Rules §2.4 cases. | `ADR_MISSING` |
| 2 | Drift register size | Open entries in `docs/registers/DRIFT_REGISTER.md`. | Visibly tracked; aged entries investigated. | `DRIFT_BACKLOG` |
| 3 | Per-root README presence | % of canonical roots with a current README declaring authority class. | 100%. | `README_MISSING` |
| 4 | Atlas / supplement lineage clarity | Each Atlas/supplement carries a current supersession entry. | 100%. | `LINEAGE_GAP` |

## 3. Panels (PROPOSED)

- **ADR completeness** — single-stat; structural moves without an accepted ADR drill out.
- **Drift register** — open-entry count + age histogram, aged entries highlighted.
- **README coverage** — % of canonical roots with a current authority-declaring README.
- **Atlas lineage** — table of Atlas/supplements with their current supersession entry.

## 4. Inputs — records read

Mounted-repo paths NEEDS VERIFICATION.

- `docs/adr/` — accepted ADRs, matched against structural moves.
- `docs/registers/DRIFT_REGISTER.md` — open-entry count and entry ages.
- Repo tree scan — canonical-root README presence and authority-class declaration.
- Atlas / supplement front-matter — supersession entries.

## 5. Files

| Path | Role | spec_hash |
|---|---|---|
| `docs/dashboards/governance/DOCUMENTATION_DRIFT.md` | This dashboard specification. | PROPOSED — pending JCS+SHA-256 |
| Running surface (PROPOSED) | `apps/review-console/` documentation-health panel. | NEEDS VERIFICATION |

## 6. Ownership and review burden

- **Owning steward (PROPOSED):** Docs steward (all four indicators).
- **Review burden:** docs steward. Resolve the placeholder role against Atlas v1.1 §24.7
  before review.

## 7. Acceptance

- [ ] All four §24.11.5 indicators present and matching [`INDICATOR_CATALOG.md`](../INDICATOR_CATALOG.md).
- [ ] Owner named (no anonymous spec at v1).
- [ ] Link check passes; row present in [`DASHBOARD_CATALOG.md`](../DASHBOARD_CATALOG.md).
- [ ] The `docs/dashboards/` placement drift case is itself reflected in indicator 2's
      source register once a `DRIFT_REGISTER.md` entry is opened (`DASH-OQ-01`).

## 8. Open questions

- [ ] **DD-OQ-01** — Confirm the running surface and downgrade if unverified.
- [ ] **DD-OQ-02** — Define the canonical-root list indicator 3 scans against
      (source: Directory Rules §6.1).
- [ ] **DD-OQ-03** — Confirm negative-state names against Unified Doctrine §19.

---

**Related docs:** [README.md](../README.md) · [INDICATOR_CATALOG.md](../INDICATOR_CATALOG.md) ·
[DASHBOARD_CATALOG.md](../DASHBOARD_CATALOG.md) ·
[doctrine/directory-rules.md](../../doctrine/directory-rules.md) ·
[registers/DRIFT_REGISTER.md](../../registers/DRIFT_REGISTER.md)

**Last updated:** 2026-05-20 · **Edition:** v0.1 (draft) · **Owners:** `<docs-steward>` (PROPOSED)
