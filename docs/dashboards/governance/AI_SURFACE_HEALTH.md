<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid-pending>
title: AI Surface Health Dashboard — specification
type: standard
version: v0.1
status: draft
owners: <ai-surface-steward>  # PROPOSED placeholder; resolve before review
created: 2026-05-20
updated: 2026-05-20
policy_label: public
related:
  - docs/dashboards/README.md
  - docs/dashboards/governance/README.md
  - docs/dashboards/INDICATOR_CATALOG.md
  - docs/dashboards/DASHBOARD_CATALOG.md
  - docs/atlases/Kansas_Frontier_Matrix_-_Domains_v1_1.md   # §24.11.4
  - docs/governed-ai/
tags: [kfm, dashboards, governance, ai-surface, focus-mode, aireceipt, indicators]
notes:
  - "Source of indicators: Atlas v1.1 §24.11.4 (CONFIRMED doctrine)."
  - "This is a SPEC for a dashboard, not the running dashboard. Indicators are reported, not enforced."
  - "Mounted-repo state UNKNOWN; running-surface and receipt-path claims are PROPOSED / NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

# AI Surface Health Dashboard · `governance/AI_SURFACE_HEALTH.md`

> Dashboard specification for the **AI surface health** governance-health category
> (Atlas v1.1 §24.11.4). Tracks whether Focus Mode answers carry receipts, abstain
> honestly, and never present synthetic content as observed.

![Authority](https://img.shields.io/badge/authority-PROPOSED-orange)
![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Category](https://img.shields.io/badge/category-governance-blue)
![Source](https://img.shields.io/badge/source-Atlas%20%C2%A724.11.4-informational)
![Policy label](https://img.shields.io/badge/policy-public-brightgreen)

**Status:** draft · **Owners:** `<ai-surface-steward>` (PROPOSED) · **Last reviewed:** 2026-05-20

---

> [!IMPORTANT]
> The cite-or-abstain rule is doctrine: a Focus Mode answer either resolves to evidence
> or it abstains. This dashboard **reports** how well that holds; the validator and the
> `AIReceipt` are what **enforce** and **prove** it.

---

## 1. Description

The AI Surface Health dashboard answers: **is the governed AI behaving honestly?** It
surfaces the four Atlas v1.1 §24.11.4 indicators so the AI surface steward can see
receipt coverage, abstain behavior by template, the distribution of denial reasons, and
any incidence of synthetic claims being presented as observed fact.

## 2. Indicators surfaced

| # | Indicator | Measures | Healthy posture (PROPOSED) | Negative state |
|---|---|---|---|---|
| 1 | AIReceipt presence rate | % of Focus Mode answers with an `AIReceipt`. | 100%. | `MISSING_AIRECEIPT` |
| 2 | ABSTAIN rate by template | How often each Focus Mode template abstains. | Visibly tracked; very low suggests over-fitting, very high suggests evidence gaps. | `REVIEW_PENDING` / `MISSING_EVIDENCE` |
| 3 | DENY reason distribution | Reason codes returned by Focus Mode denials. | Stable; large new-reason spikes investigated. | `DENIED_BY_POLICY` |
| 4 | Synthetic-claim incidence | % of audited AI answers flagged for presenting synthetic content as observed. | Approaches zero; never silently. | `SYNTHETIC_AS_OBSERVED` |

## 3. Panels (PROPOSED)

- **AIReceipt coverage** — single-stat at 100%; any miss drills to the answer.
- **ABSTAIN by template** — bar chart per template, with over-fit / evidence-gap bands.
- **DENY reasons** — stacked-area distribution; new-reason spikes flagged.
- **Synthetic-claim audit** — incidence rate from the audit sample, target ~0.

## 4. Inputs — receipts and records read

CONFIRMED receipt types (Atlas v1.1 §24.2); mounted-repo paths NEEDS VERIFICATION.

- `AIReceipt` — receipt presence, ABSTAIN flags, template identity, citations.
- `PolicyDecision` — denial reason codes for Focus Mode requests.
- Audit sample — manually-reviewed answers flagged for synthetic-as-observed content.

## 5. Files

| Path | Role | spec_hash |
|---|---|---|
| `docs/dashboards/governance/AI_SURFACE_HEALTH.md` | This dashboard specification. | PROPOSED — pending JCS+SHA-256 |
| Running surface (PROPOSED) | `apps/review-console/` AI-surface panel. | NEEDS VERIFICATION |

## 6. Ownership and review burden

- **Owning steward (PROPOSED):** AI surface steward (all four indicators).
- **Review burden:** docs steward + AI surface steward. Resolve the placeholder role
  against Atlas v1.1 §24.7 before review.

## 7. Acceptance

- [ ] All four §24.11.4 indicators present and matching [`INDICATOR_CATALOG.md`](../INDICATOR_CATALOG.md).
- [ ] Every receipt type in §4 exists in the Atlas v1.1 §24.2 receipt catalog.
- [ ] Owner named (no anonymous spec at v1).
- [ ] Link check passes; row present in [`DASHBOARD_CATALOG.md`](../DASHBOARD_CATALOG.md).
- [ ] Truth badges are generated, not hand-edited (Atlas `KFM-P3-FEAT-0005`).

## 8. Open questions

- [ ] **AISH-OQ-01** — Confirm the running surface and downgrade if unverified.
- [ ] **AISH-OQ-02** — Define the over-fit / evidence-gap ABSTAIN bands per template.
- [ ] **AISH-OQ-03** — Define the audit-sample size and cadence for indicator 4.
- [ ] **AISH-OQ-04** — Confirm `SYNTHETIC_AS_OBSERVED` against Unified Doctrine §19;
      it may be a proposed addition.

---

**Related docs:** [governance/README.md](README.md) · [dashboards/README.md](../README.md) · [INDICATOR_CATALOG.md](../INDICATOR_CATALOG.md) ·
[DASHBOARD_CATALOG.md](../DASHBOARD_CATALOG.md) · [governed-ai/](../../governed-ai/)

**Last updated:** 2026-05-20 · **Edition:** v0.1 (draft) · **Owners:** `<ai-surface-steward>` (PROPOSED)
