<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid-pending>
title: Evidence Integrity Dashboard — specification
type: standard
version: v0.1
status: draft
owners: <release-steward>, <source-steward>  # PROPOSED placeholders; resolve before review
created: 2026-05-20
updated: 2026-05-20
policy_label: public
related:
  - docs/dashboards/README.md
  - docs/dashboards/governance/README.md
  - docs/dashboards/INDICATOR_CATALOG.md
  - docs/dashboards/DASHBOARD_CATALOG.md
  - docs/atlases/Kansas_Frontier_Matrix_-_Domains_v1_1.md   # §24.11.1
  - docs/standards/EVIDENCE_BUNDLE.md
tags: [kfm, dashboards, governance, evidence, source-integrity, indicators]
notes:
  - "Source of indicators: Atlas v1.1 §24.11.1 (CONFIRMED doctrine)."
  - "This is a SPEC for a dashboard, not the running dashboard. Indicators are reported, not enforced."
  - "Mounted-repo state UNKNOWN; running-surface and receipt-path claims are PROPOSED / NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

# Evidence Integrity Dashboard · `governance/EVIDENCE_INTEGRITY.md`

> Dashboard specification for the **Evidence and source integrity** governance-health
> category (Atlas v1.1 §24.11.1). Describes what the dashboard shows, what receipts it
> reads, what posture is "healthy," and who owns it.

![Authority](https://img.shields.io/badge/authority-PROPOSED-orange)
![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Category](https://img.shields.io/badge/category-governance-blue)
![Source](https://img.shields.io/badge/source-Atlas%20%C2%A724.11.1-informational)
![Policy label](https://img.shields.io/badge/policy-public-brightgreen)

**Status:** draft · **Owners:** `<release-steward>`, `<source-steward>` (PROPOSED) · **Last reviewed:** 2026-05-20

---

> [!IMPORTANT]
> This dashboard **reports** evidence-integrity posture; it does **not** establish trust.
> The canonical proof of any claim remains its `EvidenceBundle`. If the dashboard and a
> receipt disagree, the receipt wins.

---

## 1. Description

The Evidence Integrity dashboard answers one question for stewards: **can every public
claim still be backed by resolvable evidence?** It surfaces the five Atlas v1.1 §24.11.1
indicators as time-series panels with negative-state callouts, so that a degradation
(an `EvidenceRef` that stopped resolving, a source past its freshness cadence) is visible
before it becomes a release defect.

## 2. Indicators surfaced

| # | Indicator | Measures | Healthy posture (PROPOSED) | Negative state |
|---|---|---|---|---|
| 1 | EvidenceRef resolution rate | % of public-surface EvidenceRefs that resolve to an EvidenceBundle on demand. | > 99.9% over the trailing release window. | `MISSING_EVIDENCE` |
| 2 | Cite-or-abstain compliance | % of Focus Mode answers with non-empty, resolving evidence citations. | 100% (any miss is a defect). | `MISSING_EVIDENCE` |
| 3 | Source-role distribution drift | Distribution of admitted source roles over time per domain. | No silent shift without a documented ADR or steward note. | `SOURCE_ROLE_DRIFT` |
| 4 | Stale source rate | % of admitted sources past their freshness cadence. | Stewards dispositioned within tolerance. | `SOURCE_STALE` |
| 5 | Quarantine throughput | % of admitted records that quarantine + the clearance rate. | Visible, with cause distribution; sustained backlog is a defect. | `QUARANTINE_BACKLOG` |

## 3. Panels (PROPOSED)

- **Resolution rate** — line chart, trailing release window, with the 99.9% target line.
- **Cite-or-abstain** — single-stat with drill-down to any answer missing a citation.
- **Source-role mix** — stacked area per domain; an ADR/steward-note marker overlay.
- **Stale sources** — table sorted by days-overdue, with disposition state.
- **Quarantine flow** — admitted → quarantined → cleared, with cause distribution.

## 4. Inputs — receipts and records read

CONFIRMED receipt types (Atlas v1.1 §24.2); mounted-repo paths NEEDS VERIFICATION.

- `ValidationReport` — quarantine causes, schema-validation outcomes.
- `AIReceipt` — citation presence/resolution for Focus Mode answers.
- EvidenceBundle index — resolution checks for `EvidenceRef`s.
- Source descriptors + freshness cadence metadata (`connectors/`, `data/registry/`).

## 5. Files

| Path | Role | spec_hash |
|---|---|---|
| `docs/dashboards/governance/EVIDENCE_INTEGRITY.md` | This dashboard specification. | PROPOSED — pending JCS+SHA-256 |
| Running surface (PROPOSED) | `apps/review-console/` evidence-integrity panel. | NEEDS VERIFICATION |

## 6. Ownership and review burden

- **Owning stewards (PROPOSED):** Release steward (indicators 1–2), Source steward
  (indicators 3–5).
- **Review burden:** docs steward + the owning stewards above. Resolve placeholder roles
  against Atlas v1.1 §24.7 before review.

## 7. Acceptance

A change to this spec is "correct enough to publish" when:

- [ ] All five §24.11.1 indicators are present and match [`INDICATOR_CATALOG.md`](../INDICATOR_CATALOG.md).
- [ ] Every receipt type in §4 exists in the Atlas v1.1 §24.2 receipt catalog.
- [ ] Owners are named (no anonymous spec at v1).
- [ ] Link check passes; the spec has a row in [`DASHBOARD_CATALOG.md`](../DASHBOARD_CATALOG.md).
- [ ] Negative states use the Unified Doctrine §19 vocabulary.

## 8. Open questions

- [ ] **EI-OQ-01** — Confirm the running surface (`apps/review-console/`) and downgrade
  to `NEEDS VERIFICATION` if unconfirmed.
- [ ] **EI-OQ-02** — Define the precise "trailing release window" length for indicator 1.
- [ ] **EI-OQ-03** — Decide whether `SOURCE_ROLE_DRIFT` is an existing negative state or
  a proposed addition to the Unified Doctrine §19 vocabulary.

---

**Related docs:** [governance/README.md](README.md) · [dashboards/README.md](../README.md) · [INDICATOR_CATALOG.md](../INDICATOR_CATALOG.md) ·
[DASHBOARD_CATALOG.md](../DASHBOARD_CATALOG.md) · [standards/EVIDENCE_BUNDLE.md](../../standards/EVIDENCE_BUNDLE.md)

**Last updated:** 2026-05-20 · **Edition:** v0.1 (draft) · **Owners:** `<release-steward>`, `<source-steward>` (PROPOSED)
