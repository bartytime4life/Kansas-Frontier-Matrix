<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-domain-settlements-infrastructure
title: Settlements / Infrastructure Dashboard Specification (PROPOSED lane; per-domain instance of Atlas §24.11)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: settlements-infrastructure-domain steward + sensitivity reviewer + governance-health steward
created: 2026-05-26
updated: 2026-05-26
policy_label: public
related:
  - kfm://doc/dashboards-domain-readme
  - kfm://doc/atlas-v1-1
  - kfm://doc/atlas-v1-1-ch24-5-sensitivity-tier-reference
  - kfm://doc/atlas-v1-1-ch24-6-pipeline-gate-reference
  - kfm://doc/domains-settlements-infrastructure-dossier     # CONFIRMED dossier home: docs/domains/settlements-infrastructure/
  - kfm://adr/dashboards-lane-existence                      # PROPOSED candidate: OPEN-DASH-01
tags: [kfm, dashboards, domain, settlements, infrastructure, critical-asset, t4, indicators, governance-health, specification]
notes:
  - Per-domain instance of Atlas v1.1 §24.11. Specification only; not an implementation.
  - Critical-asset infrastructure (water, power, wastewater, hospitals, emergency services) defaults to T4.
  - Atlas §24.11 wins on indicator conflicts; settlements-infrastructure dossier wins on context conflicts.
[/KFM_META_BLOCK_V2] -->

# Settlements / Infrastructure Dashboard Specification

<!-- [doc: kfm://doc/dashboards-domain-settlements-infrastructure] -->
<a id="top"></a>

> Per-domain dashboard specification for **Settlements / Infrastructure** (Atlas v1.0 Ch. 14). Cities, towns, places, plus the **critical-asset** infrastructure that supports them (water, power, wastewater, hospitals, emergency services).

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Atlas chapter: Ch. 14" src="https://img.shields.io/badge/atlas-Ch.%2014-purple">
  <img alt="Indicator emphasis: 24.11.3 (critical-asset T4) / 24.11.2" src="https://img.shields.io/badge/emphasis-24.11.3%20%C2%B7%2024.11.2-informational">
  <img alt="Critical-asset tier: T4" src="https://img.shields.io/badge/critical--asset-T4-red">
  <img alt="Policy label: public" src="https://img.shields.io/badge/policy--label-public-lightgrey">
</p>

> [!IMPORTANT]
> **Truth posture.** Indicators PROPOSED; instances PROPOSED; lane PROPOSED (OPEN-DASH-01); implementation NEEDS VERIFICATION.

> [!CAUTION]
> **Critical-asset T4.** Settlements themselves are public (T1); **critical-asset infrastructure** (water treatment, power substations, wastewater, hospital MEP, EOC siting) defaults to T4 under a threat-model assumption that fine-grained location aids targeting. The dashboard reports the fail-closed gate; the gate enforces.

> [!WARNING]
> **Authoring control.** Per OPEN-DASH-08, sensitive-domain specs should require a sensitivity reviewer on the PR. Treat this spec accordingly.

---

## 1. Domain scope

- **Atlas chapter:** v1.0 Ch. 14 (Settlements / Infrastructure).
- **Default sensitivity tier(s):** **T1** for settlements (places, populations, boundaries); **T4** for critical-asset infrastructure components.
- **Pipeline shape:** Standard intake → validation → derive → publish, with **sensitive-lane fail-closed gate** before any critical-asset emission and **rollback** required on every release.
- **Dossier:** `docs/domains/settlements-infrastructure/` — `I.` sensitivity rules (critical-asset taxonomy), `K.` validators, `M.` rollback & correction posture.

[↑ back to top](#top)

---

## 2. Indicator subset

Emphasis per README §5.1: **Sensitivity-and-rights (critical-asset T4) · Release-correction-rollback**.

| Indicator | §24.11 cat. | Domain-scale healthy posture | Receipt / signal source |
|:---|:---|:---|:---|
| **Sensitive-lane fail-closed rate** | 24.11.3 | **100% at the first gate** for any critical-asset infrastructure emission. | `PolicyDecision` DENY counts |
| RedactionReceipt coverage | 24.11.3 | 100% on public-safe derivatives of critical-asset data. | `RedactionReceipt` |
| Review-aged-out incidence | 24.11.3 | Critical-asset claims past review cadence dispositioned within tolerance. | `ReviewRecord` |
| Sensitive-content side-channel audit | 24.11.3 | Periodic audit for vertex-density / labeling / popup leakage at critical-asset locations. | Audit logs, `RepresentationReceipt` |
| Release with rollback target | 24.11.2 | 100% — every published settlement / infrastructure layer names a valid rollback target. | `ReleaseManifest`, `RollbackCard` |
| Correction lead time | 24.11.2 | Median tracked; faster cadence for critical-asset corrections (within stated tolerance). | `CorrectionNotice` |
| Derivative-invalidation coverage | 24.11.2 | Approaches 100% — corrections cascade-invalidate downstream service-area / accessibility derivatives. | `CorrectionNotice`, lineage graph |
| Rollback rehearsal rate | 24.11.2 | Non-zero per release window; rehearsals exercise critical-asset redaction path. | `RollbackCard` |
| EvidenceRef resolution rate | 24.11.1 | > 99.9% across Census / KDHE / KCC / utility-commission / hospital-licensing cites. | `ValidationReport`, EvidenceBundle index |

[↑ back to top](#top)

---

## 3. Domain-specific indicators (PROPOSED)

| PROPOSED indicator | Why this-domain-specific | Candidate §24.11 home |
|:---|:---|:---|
| Critical-asset taxonomy completeness | % of asset records mapped to a canonical critical-asset class. | §24.11.5 |
| Vertex-density side-channel exposure (critical-asset) | Polygon vertex density at critical-asset boundaries that could re-identify exact siting. | §24.11.3 |
| Service-area derivative correction cascade | Time from critical-asset correction to all service-area / accessibility derivatives invalidated. | §24.11.2 |

[↑ back to top](#top)

---

## 4. Ownership

- **Domain steward:** OWNER_TBD (settlements-infrastructure dossier owner).
- **Governance-health steward:** OWNER_TBD (**sensitivity reviewer** + release steward; mandatory pair).
- **Implementation owner:** OWNER_TBD (`apps/review-console/` team).

[↑ back to top](#top)

---

## 5. Implementation pointer

- **Dashboard app:** `apps/review-console/` (PROPOSED) — `UNKNOWN` until verified.
- **Telemetry:** `runtime/observability/sensitivity/`, `runtime/observability/release/` (PROPOSED) — `UNKNOWN`.
- **Schemas read:** `schemas/contracts/v1/sensitivity/`, `schemas/contracts/v1/redaction/`, `schemas/contracts/v1/release/`, `schemas/contracts/v1/correction/`.
- **Policy bundles emitting signals:** `policy/sensitivity/critical-asset/`, `policy/release/`, `policy/correction/`.

[↑ back to top](#top)

---

## 6. Review cadence

- **Trigger events:** critical-asset taxonomy bump; utility / hospital licensing schema change; settlements-infrastructure dossier edition.
- **Default cadence:** quarterly; **immediate** review on side-channel audit failure or critical-asset correction emission.

[↑ back to top](#top)

---

## 7. Open questions

- [ ] **OPEN-DASH-SI-01** — Confirm critical-asset taxonomy completeness threshold (per asset class).
- [ ] **OPEN-DASH-SI-02** — Define service-area cascade target latency (minutes vs hours).
- [ ] **OPEN-DASH-SI-03** — Confirm sensitivity-reviewer-on-PR gate per OPEN-DASH-08.

[↑ back to top](#top)

---

## 8. Evidence basis & citations

<details>
<summary><strong>Source ledger</strong></summary>

| Source | Status | Supports | Limits |
|:---|:---|:---|:---|
| Atlas v1.1 §24.11.3 / §24.11.2 | CONFIRMED (manuscript) | §2 indicator subset. | Indicators PROPOSED at source. |
| Atlas v1.0 Ch. 14 (Settlements / Infrastructure dossier) | CONFIRMED (manuscript) | §1 scope, critical-asset T4 default; §3 candidates. | Mounted dossier presence NEEDS VERIFICATION. |
| Atlas v1.1 §24.5 / §24.10 | CONFIRMED authored sibling | Critical-asset T4 justification; threat model. | Tier table + risk severities PROPOSED. |
| `docs/dashboards/domain/README.md` §5.1, §6 | CONFIRMED | Emphasis (Sensitivity-and-rights, critical-asset T4 · Release-correction-rollback); template. | Lane PROPOSED (OPEN-DASH-01). |

</details>

[↑ back to top](#top)

---

<sub>Per-domain settlements / infrastructure dashboard specification. **Specification only — implementations live in `apps/`; indicator definitions live in Atlas §24.11; domain context lives in `docs/domains/settlements-infrastructure/`.** Critical-asset T4 default: the dashboard reports posture, the gate enforces redaction, the receipts back the trust.</sub>
