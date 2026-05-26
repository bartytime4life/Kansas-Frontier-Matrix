<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-domain-fauna
title: Fauna Dashboard Specification (PROPOSED lane; per-domain instance of Atlas §24.11)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: fauna-domain steward + sensitivity reviewer + governance-health steward
created: 2026-05-26
updated: 2026-05-26
policy_label: public
related:
  - kfm://doc/dashboards-domain-readme
  - kfm://doc/atlas-v1-1
  - kfm://doc/atlas-v1-1-ch24-5-sensitivity-tier-reference
  - kfm://doc/atlas-v1-1-ch24-6-pipeline-gate-reference
  - kfm://doc/domains-fauna-dossier                          # CONFIRMED dossier home: docs/domains/fauna/
  - kfm://adr/dashboards-lane-existence                      # PROPOSED candidate: OPEN-DASH-01
tags: [kfm, dashboards, domain, fauna, sensitivity, t4, indicators, governance-health, specification]
notes:
  - Per-domain instance of Atlas v1.1 §24.11. Specification only; not an implementation.
  - Default sensitivity tier is T4 (sensitive-species localities, listed-species range, observation lineage).
  - Atlas §24.11 wins on indicator-definition conflicts; the fauna dossier wins on context conflicts.
[/KFM_META_BLOCK_V2] -->

# Fauna Dashboard Specification

<!-- [doc: kfm://doc/dashboards-domain-fauna] -->
<a id="top"></a>

> Per-domain dashboard specification for **Fauna** (Atlas v1.0 Ch. 7). A **T4-default sensitive domain** — the dashboard's primary job is reporting fail-closed posture, redaction coverage, and side-channel audit cadence.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Atlas chapter: Ch. 7" src="https://img.shields.io/badge/atlas-Ch.%207-purple">
  <img alt="Indicator emphasis: 24.11.3 (T4 defaults) / 24.11.1" src="https://img.shields.io/badge/emphasis-24.11.3%20%C2%B7%2024.11.1-informational">
  <img alt="Default tier: T4" src="https://img.shields.io/badge/default--tier-T4-red">
  <img alt="Policy label: public" src="https://img.shields.io/badge/policy--label-public-lightgrey">
</p>

> [!IMPORTANT]
> **Truth posture.** Atlas §24.11 catalog PROPOSED; per-domain instances PROPOSED; lane PROPOSED (OPEN-DASH-01); implementation NEEDS VERIFICATION.

> [!CAUTION]
> **T4 default.** Fauna observations of listed, sensitive, or vulnerable species are T4 by default. The dashboard reports posture; **the gate enforces**. Any apparent "false-positive DENY" must be diagnosed at the policy/, not by tuning this dashboard.

> [!WARNING]
> **Authoring control.** Per OPEN-DASH-08, sensitive-domain specs should require a sensitivity reviewer on the PR. Treat that as a soft gate until the ADR resolves.

---

## 1. Domain scope

- **Atlas chapter:** v1.0 Ch. 7 (Fauna).
- **Default sensitivity tier(s):** **T4** for listed-species localities, nest/den sites, observation lineage; T2–T3 for non-sensitive aggregate counts.
- **Pipeline shape:** Standard intake → validation → derive → publish, with **sensitive-lane fail-closed gate** before any public-surface emission; redaction receipts required on public-safe derivatives.
- **Dossier:** `docs/domains/fauna/` — `I.` sensitivity rules (KDWP / USFWS / state listings), `K.` validators, `M.` correction posture for misidentification rollback.

[↑ back to top](#top)

---

## 2. Indicator subset

Emphasis per README §5.1: **Sensitivity-and-rights (T4 defaults) · Evidence-and-source**.

| Indicator | §24.11 cat. | Domain-scale healthy posture | Receipt / signal source |
|:---|:---|:---|:---|
| **Sensitive-lane fail-closed rate** | 24.11.3 | **100% at the first gate.** Any DENY-leakage below the gate is a critical defect. | `PolicyDecision` DENY counts |
| RedactionReceipt coverage | 24.11.3 | 100% on every public-safe derivative of a T4 fauna record. | `RedactionReceipt` |
| Review-aged-out incidence | 24.11.3 | Sensitive-lane claims past review cadence dispositioned within tolerance; trend tracked. | `ReviewRecord` |
| Rights-change response time | 24.11.3 | Median time from rights-change detection (e.g., new state listing) to tier reassignment within stated tolerance. | Source descriptors, `ReviewRecord` |
| Sensitive-content side-channel audit | 24.11.3 | Periodic automated checks for label / map-popup / AI-text leaks; documented. | Audit logs, `RepresentationReceipt` |
| EvidenceRef resolution rate | 24.11.1 | > 99.9% across iNaturalist / KDWP / GBIF / KU Biodiversity Institute cites; per-source rate visible. | `ValidationReport`, EvidenceBundle index |
| Source-role distribution drift | 24.11.1 | Observation roles (museum specimen / citizen science / regulatory) tracked; no silent shift. | Source descriptors |
| Quarantine throughput | 24.11.1 | Cause distribution visible (misidentification, locality precision); no sustained backlog. | `ValidationReport`, quarantine ledger |

[↑ back to top](#top)

---

## 3. Domain-specific indicators (PROPOSED)

| PROPOSED indicator | Why fauna-specific | Candidate §24.11 home |
|:---|:---|:---|
| Locality-precision DENY pattern | DENYs triggered specifically by locality coarseness below threshold — a fauna-recurrent signal. | §24.11.3 |
| Citizen-science role drift | Shift in observation-role mix toward citizen science without an ADR — affects identification confidence. | §24.11.1 |
| Listing-change lag | Time between a state/federal listing change and the corresponding tier reassignment on local records. | §24.11.3 (rights-change variant) |

[↑ back to top](#top)

---

## 4. Ownership

- **Domain steward:** OWNER_TBD (fauna dossier owner — resolve against Atlas §24.7).
- **Governance-health steward:** OWNER_TBD (**sensitivity reviewer** + rights-holder representative; mandatory pair per Atlas §24.7).
- **Implementation owner:** OWNER_TBD (`apps/review-console/` team).

[↑ back to top](#top)

---

## 5. Implementation pointer

- **Dashboard app:** `apps/review-console/` (PROPOSED) — `UNKNOWN` until verified.
- **Telemetry:** `runtime/observability/sensitivity/` (PROPOSED) — `UNKNOWN`.
- **Schemas read:** `schemas/contracts/v1/sensitivity/`, `schemas/contracts/v1/redaction/`, `schemas/contracts/v1/review/`.
- **Policy bundles emitting signals:** `policy/sensitivity/`, `policy/sources/`.

[↑ back to top](#top)

---

## 6. Review cadence

- **Trigger events:** state/federal listing change; fauna dossier edition; Atlas §24.11 amendment; **any** unexplained drop in DENY rate.
- **Default cadence:** quarterly; **immediate** review on side-channel audit failure.

[↑ back to top](#top)

---

## 7. Open questions

- [ ] **OPEN-DASH-FAUNA-01** — Define locality-precision threshold per taxon group (mammals / birds / herps).
- [ ] **OPEN-DASH-FAUNA-02** — Confirm `RedactionReceipt` schema covers vertex-density side-channels (cross-reference habitat spec).
- [ ] **OPEN-DASH-FAUNA-03** — Confirm sensitivity-reviewer-on-PR gate per OPEN-DASH-08.

[↑ back to top](#top)

---

## 8. Evidence basis & citations

<details>
<summary><strong>Source ledger</strong></summary>

| Source | Status | Supports | Limits |
|:---|:---|:---|:---|
| Atlas v1.1 §24.11.3 / §24.11.1 | CONFIRMED (manuscript) | §2 indicator subset. | Indicators PROPOSED at source. |
| Atlas v1.0 Ch. 7 (Fauna dossier) | CONFIRMED (manuscript) | §1 scope, T4 default; §3 candidates. | Mounted dossier presence NEEDS VERIFICATION. |
| Atlas v1.1 §24.5 (Sensitivity tier reference) | CONFIRMED authored sibling | T4 default justification. | Tier table PROPOSED. |
| Atlas v1.1 §24.10 (Risk register) | CONFIRMED (manuscript) | Sensitive-lane risk severities. | PROPOSED severities. |
| `docs/dashboards/domain/README.md` §5.1, §6 | CONFIRMED | Emphasis (Sensitivity-and-rights, T4 defaults); template. | Lane PROPOSED (OPEN-DASH-01). |

</details>

[↑ back to top](#top)

---

<sub>Per-domain fauna dashboard specification. **Specification only — implementations live in `apps/`; indicator definitions live in Atlas §24.11; domain context lives in `docs/domains/fauna/`.** Default tier T4: the dashboard reports posture, the gate enforces, the receipts back the trust.</sub>
