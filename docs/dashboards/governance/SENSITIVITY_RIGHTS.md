<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid-pending>
title: Sensitivity / Rights Dashboard — specification
type: standard
version: v0.1
status: draft
owners: <sensitivity-reviewer>, <rights-holder-representative>  # PROPOSED placeholders; resolve before review
created: 2026-05-20
updated: 2026-05-20
policy_label: public
related:
  - docs/dashboards/README.md
  - docs/dashboards/INDICATOR_CATALOG.md
  - docs/dashboards/DASHBOARD_CATALOG.md
  - docs/atlases/Kansas_Frontier_Matrix_-_Domains_v1_1.md   # §24.11.3
  - docs/standards/SENSITIVITY_RUBRIC.md
  - docs/standards/REDACTION_PROFILES.md
  - docs/runbooks/SENSITIVITY_ESCALATION.md
tags: [kfm, dashboards, governance, sensitivity, rights, redaction, indicators]
notes:
  - "Source of indicators: Atlas v1.1 §24.11.3 (CONFIRMED doctrine)."
  - "This is a SPEC for a dashboard, not the running dashboard. Indicators are reported, not enforced."
  - "This dashboard itself must not leak sensitive content; see §9 (anti-leakage)."
  - "Mounted-repo state UNKNOWN; running-surface and receipt-path claims are PROPOSED / NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

# Sensitivity / Rights Dashboard · `governance/SENSITIVITY_RIGHTS.md`

> Dashboard specification for the **Sensitivity and rights** governance-health category
> (Atlas v1.1 §24.11.3). Tracks whether sensitive lanes fail closed and whether
> rights-holders' constraints are honored end to end.

![Authority](https://img.shields.io/badge/authority-PROPOSED-orange)
![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Category](https://img.shields.io/badge/category-governance-blue)
![Source](https://img.shields.io/badge/source-Atlas%20%C2%A724.11.3-informational)
![Policy label](https://img.shields.io/badge/policy-public-brightgreen)

**Status:** draft · **Owners:** `<sensitivity-reviewer>`, `<rights-holder-representative>` (PROPOSED) · **Last reviewed:** 2026-05-20

---

> [!WARNING]
> This dashboard reports on sensitive lanes. It **must surface aggregate posture only** —
> never the sensitive content itself. The dashboard reads `PolicyDecision` and
> `RedactionReceipt` *outcomes*, not the protected payloads. See §9.

---

## 1. Description

The Sensitivity / Rights dashboard answers: **does every unauthorized sensitive request
get denied at the first gate, and do public-safe transformations always leave a
`RedactionReceipt`?** It surfaces the five Atlas v1.1 §24.11.3 indicators so the
sensitivity reviewer and rights-holder representative can see fail-closed behavior and
rights-change responsiveness.

## 2. Indicators surfaced

| # | Indicator | Measures | Healthy posture (PROPOSED) | Negative state |
|---|---|---|---|---|
| 1 | Sensitive-lane fail-closed rate | % of unauthorized sensitive-lane requests that DENY at the first gate. | 100% at the first gate. | `DENIED_BY_POLICY` (expected); a non-first-gate deny is the defect |
| 2 | RedactionReceipt coverage | % of public-safe transformations that emit a `RedactionReceipt`. | 100% for sensitive lanes. | `MISSING_REDACTION_RECEIPT` |
| 3 | Review-aged-out incidence | Number of sensitive-lane claims past their review cadence. | Visibly tracked; trend not regressing. | `REVIEW_AGED_OUT` |
| 4 | Rights-change response time | Median time from rights-change detection to tier reassignment. | Within stated tolerance per source family. | `RIGHTS_CHANGE_LAGGING` |
| 5 | Sensitive-content side-channel audit | Frequency of automated checks for label / popup / AI-text leaks. | Periodic; documented. | `SIDE_CHANNEL_AUDIT_OVERDUE` |

## 3. Panels (PROPOSED)

- **Fail-closed rate** — single-stat at 100%; any deviation drills to the gate that failed.
- **Redaction coverage** — % of public-safe transforms with a receipt, per sensitive lane.
- **Review aging** — histogram of sensitive-lane claims by days-past-cadence.
- **Rights-change responsiveness** — median + p90 reassignment time per source family.
- **Side-channel audit cadence** — last-run timestamp + pass/fail per leak check.

## 4. Inputs — receipts and records read

CONFIRMED receipt types (Atlas v1.1 §24.2); mounted-repo paths NEEDS VERIFICATION.

- `PolicyDecision` — gate-level DENY outcomes for sensitive-lane requests.
- `RedactionReceipt` — coverage of public-safe transformations.
- `ReviewRecord` — review cadence and aging for sensitive-lane claims.
- `RepresentationReceipt` + audit logs — side-channel leak-check results.
- Source descriptors — rights-change detection and tolerance per source family.

## 5. Files

| Path | Role | spec_hash |
|---|---|---|
| `docs/dashboards/governance/SENSITIVITY_RIGHTS.md` | This dashboard specification. | PROPOSED — pending JCS+SHA-256 |
| Running surface (PROPOSED) | `apps/review-console/` sensitivity panel (restricted view). | NEEDS VERIFICATION |

## 6. Ownership and review burden

- **Owning stewards (PROPOSED):** Sensitivity reviewer (indicators 1–3, 5),
  Rights-holder representative (indicator 4).
- **Review burden:** docs steward + sensitivity reviewer + rights-holder representative.
  Resolve placeholders against Atlas v1.1 §24.7 before review.

## 7. Acceptance

- [ ] All five §24.11.3 indicators present and matching [`INDICATOR_CATALOG.md`](../INDICATOR_CATALOG.md).
- [ ] Every receipt type in §4 exists in the Atlas v1.1 §24.2 receipt catalog.
- [ ] Owners named (no anonymous spec at v1).
- [ ] §9 anti-leakage constraints are satisfied — no sensitive payload field appears in
      any panel definition.
- [ ] Link check passes; row present in [`DASHBOARD_CATALOG.md`](../DASHBOARD_CATALOG.md).

## 8. Open questions

- [ ] **SR-OQ-01** — Confirm the running surface and its access-control posture
      (this panel itself is a restricted view).
- [ ] **SR-OQ-02** — Define per-source-family rights-change tolerance values.
- [ ] **SR-OQ-03** — Confirm negative-state names against Unified Doctrine §19.

## 9. Anti-leakage constraints (CONFIRMED doctrine)

- The dashboard reads **outcomes** (`DENY`, receipt-present/absent, age, timestamps),
  never the protected payloads behind a sensitive lane.
- Panel definitions MUST NOT include free-text fields sourced from sensitive records.
- Access to the running surface is itself a sensitive lane — fail closed for
  unauthorized viewers, exactly like the requests it measures.

---

**Related docs:** [README.md](../README.md) · [INDICATOR_CATALOG.md](../INDICATOR_CATALOG.md) ·
[DASHBOARD_CATALOG.md](../DASHBOARD_CATALOG.md) ·
[standards/SENSITIVITY_RUBRIC.md](../../standards/SENSITIVITY_RUBRIC.md) ·
[runbooks/SENSITIVITY_ESCALATION.md](../../runbooks/SENSITIVITY_ESCALATION.md)

**Last updated:** 2026-05-20 · **Edition:** v0.1 (draft) · **Owners:** `<sensitivity-reviewer>`, `<rights-holder-representative>` (PROPOSED)
