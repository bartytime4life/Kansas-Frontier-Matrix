<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-governance-ai-surface-health
title: AI Surface Health (system-wide governance health spec; Atlas §24.11.4)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: docs steward + governance-health steward + AI surface owner
created: 2026-05-26
updated: 2026-05-26
policy_label: public
related:
  - kfm://doc/dashboards-governance-readme
  - kfm://doc/atlas-v1-1                      # §24.11.4 — 4 indicators
  - kfm://doc/dashboards-domain-readme
tags: [kfm, dashboards, governance, ai, aireceipt, abstain, deny, 24-11-4]
notes:
  - Indicator catalog: Atlas §24.11.4 (4 indicators); labeled PROPOSED in source.
  - DENY-reason distribution detail relates to denial-reason-explorer.md (§5.2 cross-cutting).
[/KFM_META_BLOCK_V2] -->

# AI Surface Health

<!-- [doc: kfm://doc/dashboards-governance-ai-surface-health] -->
<a id="top"></a>

> System-wide governance health view of AI-surfaced outputs — AIReceipt presence rate, ABSTAIN rate, DENY-reason distribution, and citation-with-evidence rate. Atlas §24.11.4.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Scope: system-wide" src="https://img.shields.io/badge/scope-system--wide-informational">
  <img alt="Atlas §24.11.4" src="https://img.shields.io/badge/atlas-%C2%A724.11.4-purple">
  <img alt="Indicators: 4" src="https://img.shields.io/badge/indicators-4-yellow">
  <img alt="Policy label: public" src="https://img.shields.io/badge/policy--label-public-lightgrey">
</p>

> [!IMPORTANT]
> **Truth posture.** Indicator catalog from Atlas §24.11.4 (CONFIRMED text, PROPOSED indicators). AIReceipt outcome envelope shape per Atlas §24.3 (CONFIRMED). DENY-reason distribution detail is rendered by `denial-reason-explorer.md` (cross-cutting); this dashboard surfaces the top-line rate.

---

## 1. Scope

- **Atlas reference:** §24.11.4 — AI Surface Health (4 indicators).
- **Audience:** AI surface owner, governance-health steward, reviewer, docs steward.
- **Aggregation scope:** System-wide across all AI-surfaced outputs (chat, summarization, search ranking, etc.).

[↑ back to top](#top)

---

## 2. Indicators

| Indicator | What it measures | Healthy posture (PROPOSED) | Signal source |
|:---|:---|:---|:---|
| AIReceipt presence rate | % of AI-surfaced outputs carrying a valid `AIReceipt` | 100% | AIReceipt writer + AI-surface gateway |
| ABSTAIN rate | % of AI requests answered with `ABSTAIN` (governed refusal) | Tracking metric; alert on sudden swings *(>2× rolling-30d baseline)* | AIReceipt outcome envelope (Atlas §24.3) |
| DENY-reason distribution | Distribution of `PolicyDecision` denials by reason code | Tracked, not thresholded; explored via `denial-reason-explorer.md` | `PolicyDecision` outcomes; Atlas §24.6.3 reason codes |
| Citation-with-evidence rate | % of cited AI outputs whose citations resolve to an `EvidenceBundle` | ≥ 99% | AIReceipt + EvidenceBundle resolver; cross-link to `evidence-and-source.md` |

[↑ back to top](#top)

---

## 3. Per-domain breakdowns

AI surfaces are typically domain-agnostic at the infrastructure layer, but domain-specific denial patterns matter:

- `docs/dashboards/domain/archaeology.md` *(T4 default-deny — expect higher ABSTAIN rate)*
- `docs/dashboards/domain/fauna-flora.md` *(rare-species coordinate suppression — DENY-reason distribution shifts)*
- *…other domain specs as applicable.*

[↑ back to top](#top)

---

## 4. Ownership

- **Docs steward:** OWNER_TBD
- **Governance-health steward:** OWNER_TBD
- **AI surface owner:** OWNER_TBD
- **Implementation owner:** OWNER_TBD

[↑ back to top](#top)

---

## 5. Implementation pointer

- **Dashboard app:** `apps/review-console/ai-surface/` *(PROPOSED; NEEDS VERIFICATION)*.
- **Telemetry:** `runtime/observability/ai-surface/` *(PROPOSED)*; cross-link to `docs/dashboards/observability/telemetry-contract-health.md`.
- **Schemas read:** `schemas/contracts/v1/ai/AIReceipt.schema.json`, `schemas/contracts/v1/policy/PolicyDecision.schema.json` *(NEEDS VERIFICATION).*
- **Policy bundles emitting signals:** `policy/ai/cite-or-abstain/`, `policy/ai/deny-reasons/` *(PROPOSED).*
- **Registers visualized:** `docs/registers/DRIFT_REGISTER.md` (sudden ABSTAIN/DENY-rate swings recorded as drift).
- **Related governance specs:** `denial-reason-explorer.md` (DENY drill-down), `evidence-and-source.md` (citation-with-evidence rate shared signal).

[↑ back to top](#top)

---

## 6. Review cadence

- Reviewed quarterly.
- Trigger events: Atlas §24.11.4 amendment, AIReceipt schema change, addition of a new DENY reason code (§24.6.3), AI-surface model upgrade.

[↑ back to top](#top)

---

## 7. Open questions

- **OPEN-DASH-GOV-AI-01** — ABSTAIN-rate alert threshold: 2× rolling baseline is PROPOSED — appropriate, or should it be model-specific?
- **OPEN-DASH-GOV-AI-02** — Per-model breakdown: surface here, or only in `apps/admin/` (because model identity is internal architecture)?
- **OPEN-DASH-GOV-AI-03** — Reconcile this kebab-case spec with the pre-existing `AI_SURFACE_HEALTH.md`.

[↑ back to top](#top)

---

## 8. Evidence basis & citations

| Source | Status | Supports |
|:---|:---|:---|
| Atlas v1.1 §24.11.4 (AI Surface Health — 4 indicators) | CONFIRMED (manuscript) | §1, §2 indicator catalog. |
| Atlas v1.1 §24.3 (AIReceipt outcome envelope) | CONFIRMED (manuscript) | §2 ABSTAIN / DENY shape. |
| Atlas v1.1 §24.6.3 (Reason codes) | CONFIRMED (manuscript) | §2 DENY-reason distribution. |
| `docs/dashboards/governance/README.md` | CONFIRMED (this folder) | §6 template. |

<sub>Specification only. AI outputs are surfaced; AIReceipts carry trust — the dashboard reports, the receipt is what reviewers ultimately read.</sub>
