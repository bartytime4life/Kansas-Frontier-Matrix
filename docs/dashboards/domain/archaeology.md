<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-domain-archaeology
title: Archaeology / Cultural Heritage Dashboard Specification (PROPOSED lane; per-domain instance of Atlas §24.11)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: archaeology-domain steward + sensitivity reviewer + sovereignty representative + governance-health steward
created: 2026-05-26
updated: 2026-05-26
policy_label: public
related:
  - kfm://doc/dashboards-domain-readme
  - kfm://doc/atlas-v1-1
  - kfm://doc/atlas-v1-1-ch24-5-sensitivity-tier-reference
  - kfm://doc/atlas-v1-1-ch24-6-pipeline-gate-reference
  - kfm://doc/domains-archaeology-dossier                    # CONFIRMED dossier home: docs/domains/archaeology/
  - kfm://adr/dashboards-lane-existence                      # PROPOSED candidate: OPEN-DASH-01
tags: [kfm, dashboards, domain, archaeology, cultural-heritage, sovereignty, t4, indicators, governance-health, specification]
notes:
  - Per-domain instance of Atlas v1.1 §24.11. Specification only; not an implementation.
  - Default T4 — archaeological site coordinates and culturally affiliated material are sovereignty-governed by default.
  - The dashboard reports posture; sovereignty is held by the affiliated nation, not by KFM.
  - Atlas §24.11 wins on indicator conflicts; archaeology dossier wins on context conflicts.
[/KFM_META_BLOCK_V2] -->

# Archaeology / Cultural Heritage Dashboard Specification

<!-- [doc: kfm://doc/dashboards-domain-archaeology] -->
<a id="top"></a>

> Per-domain dashboard specification for **Archaeology / Cultural Heritage** (Atlas v1.0 Ch. 15). Site locations, culturally affiliated material, NAGPRA-class records. **T4 by default; sovereignty-governed.**

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Atlas chapter: Ch. 15" src="https://img.shields.io/badge/atlas-Ch.%2015-purple">
  <img alt="Indicator emphasis: 24.11.3 (T4 defaults, sovereignty) / 24.11.1" src="https://img.shields.io/badge/emphasis-24.11.3%20%C2%B7%2024.11.1-informational">
  <img alt="Default tier: T4 / sovereignty" src="https://img.shields.io/badge/default--tier-T4%20%C2%B7%20sovereignty-red">
  <img alt="Policy label: public" src="https://img.shields.io/badge/policy--label-public-lightgrey">
</p>

> [!IMPORTANT]
> **Truth posture.** Indicators PROPOSED; instances PROPOSED; lane PROPOSED (OPEN-DASH-01); implementation NEEDS VERIFICATION.

> [!CAUTION]
> **Sovereignty.** Tribal sovereignty over culturally affiliated archaeological material is not a permission KFM grants — it is held by the affiliated nation. The dashboard reports KFM's compliance posture against sovereignty rules; it does not enumerate or expose the underlying records.

> [!WARNING]
> **Authoring control.** Per OPEN-DASH-08, this spec **requires** a sensitivity reviewer **and** a sovereignty representative on the PR. Authoring without both is a process defect.

---

## 1. Domain scope

- **Atlas chapter:** v1.0 Ch. 15 (Archaeology / Cultural Heritage).
- **Default sensitivity tier(s):** **T4** for site coordinates and culturally affiliated material; **T1–T2** for de-identified, sovereignty-cleared aggregate reporting.
- **Pipeline shape:** Standard intake → validation → derive → publish, with **sensitive-lane fail-closed gate** before any public-surface emission and **sovereignty review** as a SoD-named role.
- **Dossier:** `docs/domains/archaeology/` — `I.` sovereignty + sensitivity rules, `K.` validators (site-type vocabulary, NAGPRA flags), `M.` correction posture, `N.` verification backlog.

[↑ back to top](#top)

---

## 2. Indicator subset

Emphasis per README §5.1: **Sensitivity-and-rights (T4 defaults, sovereignty) · Evidence-and-source**.

| Indicator | §24.11 cat. | Domain-scale healthy posture | Receipt / signal source |
|:---|:---|:---|:---|
| **Sensitive-lane fail-closed rate** | 24.11.3 | **100% at the first gate** for any T4 archaeology emission. | `PolicyDecision` DENY counts |
| RedactionReceipt coverage | 24.11.3 | 100% on public-safe derivatives (de-identified summaries, generalized regions). | `RedactionReceipt` |
| **Sovereignty review presence** | 24.11.3 | 100% — every claim involving culturally affiliated material carries a sovereignty `ReviewRecord`. | `ReviewRecord` (sovereignty-typed) |
| Review-aged-out incidence | 24.11.3 | Sensitive-lane / sovereignty claims past review cadence dispositioned within tolerance. | `ReviewRecord` |
| Rights-change response time | 24.11.3 | Median time from sovereignty-rule change (nation request, NAGPRA decision) to tier reassignment within tolerance. | Source descriptors, `ReviewRecord` |
| Sensitive-content side-channel audit | 24.11.3 | Periodic audit for label / popup / vertex-density / AI-text leaks of site location or affiliation. | Audit logs, `RepresentationReceipt` |
| EvidenceRef resolution rate | 24.11.1 | > 99.9% across KSHS / NPS / state archaeological-survey / scholarly cites; per-source rate visible (counting only metadata, not site coordinates). | `ValidationReport`, EvidenceBundle index |
| Quarantine throughput | 24.11.1 | Cause distribution visible (site-type vocabulary, NAGPRA flag, geometry precision); no sustained backlog. | `ValidationReport`, quarantine ledger |

[↑ back to top](#top)

---

## 3. Domain-specific indicators (PROPOSED)

| PROPOSED indicator | Why archaeology-specific | Candidate §24.11 home |
|:---|:---|:---|
| Sovereignty-decision lineage coverage | % of culturally affiliated claims with a resolvable sovereignty-decision lineage. | §24.11.3 |
| NAGPRA-flag completeness | % of records carrying a NAGPRA classification flag where applicable. | §24.11.3 |
| Cultural-affiliation vocabulary drift | Shift in cultural-affiliation vocabulary without an ADR or sovereignty-record amendment. | §24.11.5 |

[↑ back to top](#top)

---

## 4. Ownership

- **Domain steward:** OWNER_TBD (archaeology dossier owner).
- **Governance-health steward:** OWNER_TBD (**sensitivity reviewer** + **sovereignty representative** + rights-holder representative; **all three** required).
- **Implementation owner:** OWNER_TBD (`apps/review-console/` team).

[↑ back to top](#top)

---

## 5. Implementation pointer

- **Dashboard app:** `apps/review-console/` (PROPOSED) — `UNKNOWN` until verified.
- **Telemetry:** `runtime/observability/sensitivity/`, `runtime/observability/sovereignty/` (PROPOSED) — `UNKNOWN`.
- **Schemas read:** `schemas/contracts/v1/sensitivity/`, `schemas/contracts/v1/redaction/`, `schemas/contracts/v1/review/` (sovereignty-typed), `schemas/contracts/v1/correction/`.
- **Policy bundles emitting signals:** `policy/sensitivity/sovereignty/`, `policy/sources/`, `policy/correction/`.

[↑ back to top](#top)

---

## 6. Review cadence

- **Trigger events:** sovereignty-rule change (nation request, NAGPRA decision, scholar consultation); archaeology dossier edition; Atlas §24.11 amendment.
- **Default cadence:** quarterly; **immediate** review on any sovereignty-related correction or denial pattern shift.

[↑ back to top](#top)

---

## 7. Open questions

- [ ] **OPEN-DASH-ARCH-01** — Confirm sovereignty `ReviewRecord` schema (is it a typed variant, or a separate receipt family?).
- [ ] **OPEN-DASH-ARCH-02** — Define NAGPRA-flag completeness scope (which record families are in scope).
- [ ] **OPEN-DASH-ARCH-03** — Confirm sensitivity-reviewer + sovereignty-representative dual-gate per OPEN-DASH-08.

[↑ back to top](#top)

---

## 8. Evidence basis & citations

<details>
<summary><strong>Source ledger</strong></summary>

| Source | Status | Supports | Limits |
|:---|:---|:---|:---|
| Atlas v1.1 §24.11.3 / §24.11.1 | CONFIRMED (manuscript) | §2 indicator subset; sovereignty emphasis. | Indicators PROPOSED at source. |
| Atlas v1.0 Ch. 15 (Archaeology dossier) | CONFIRMED (manuscript) | §1 scope, T4-default + sovereignty; §3 candidates. | Mounted dossier presence NEEDS VERIFICATION. |
| Atlas v1.1 §24.5 / §24.7 | CONFIRMED authored sibling | T4 default; sovereignty representative as SoD-named role. | Tier table + role matrix PROPOSED. |
| `docs/dashboards/domain/README.md` §5.1, §6 | CONFIRMED | Emphasis (Sensitivity-and-rights, T4 defaults, sovereignty); template. | Lane PROPOSED (OPEN-DASH-01). |

</details>

[↑ back to top](#top)

---

<sub>Per-domain archaeology / cultural heritage dashboard specification. **Specification only — implementations live in `apps/`; indicator definitions live in Atlas §24.11; domain context lives in `docs/domains/archaeology/`.** Sovereignty is held by the affiliated nation; the dashboard reports KFM's compliance posture only.</sub>
