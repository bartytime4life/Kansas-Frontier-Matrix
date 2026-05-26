<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-domain-flora
title: Flora Dashboard Specification (PROPOSED lane; per-domain instance of Atlas §24.11)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: flora-domain steward + sensitivity reviewer + governance-health steward
created: 2026-05-26
updated: 2026-05-26
policy_label: public
related:
  - kfm://doc/dashboards-domain-readme
  - kfm://doc/atlas-v1-1
  - kfm://doc/atlas-v1-1-ch24-5-sensitivity-tier-reference
  - kfm://doc/atlas-v1-1-ch24-6-pipeline-gate-reference
  - kfm://doc/domains-flora-dossier                          # CONFIRMED dossier home: docs/domains/flora/
  - kfm://adr/dashboards-lane-existence                      # PROPOSED candidate: OPEN-DASH-01
tags: [kfm, dashboards, domain, flora, sensitivity, t4, indicators, governance-health, specification]
notes:
  - Per-domain instance of Atlas v1.1 §24.11. Specification only; not an implementation.
  - Default sensitivity tier T4 for poaching-vulnerable taxa, T1–T2 for non-sensitive flora.
  - Atlas §24.11 wins on indicator conflicts; flora dossier wins on context conflicts.
[/KFM_META_BLOCK_V2] -->

# Flora Dashboard Specification

<!-- [doc: kfm://doc/dashboards-domain-flora] -->
<a id="top"></a>

> Per-domain dashboard specification for **Flora** (Atlas v1.0 Ch. 8). A **T4-default sensitive domain** for poaching-vulnerable taxa (rare orchids, cacti, etc.); the dashboard's primary job is reporting fail-closed and redaction posture.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Atlas chapter: Ch. 8" src="https://img.shields.io/badge/atlas-Ch.%208-purple">
  <img alt="Indicator emphasis: 24.11.3 (T4 defaults) / 24.11.1" src="https://img.shields.io/badge/emphasis-24.11.3%20%C2%B7%2024.11.1-informational">
  <img alt="Default tier: T4" src="https://img.shields.io/badge/default--tier-T4-red">
  <img alt="Policy label: public" src="https://img.shields.io/badge/policy--label-public-lightgrey">
</p>

> [!IMPORTANT]
> **Truth posture.** Indicators PROPOSED; instances PROPOSED; lane PROPOSED (OPEN-DASH-01); implementation NEEDS VERIFICATION.

> [!CAUTION]
> **T4 default for poaching-vulnerable taxa.** The poaching risk model — not the science — drives T4 on rare orchids, cacti, and certain medicinals. Aggregate ecological reporting (Kansas grassland composition) remains T1–T2.

> [!WARNING]
> **Authoring control.** Per OPEN-DASH-08, sensitive-domain specs should require a sensitivity reviewer on the PR.

---

## 1. Domain scope

- **Atlas chapter:** v1.0 Ch. 8 (Flora).
- **Default sensitivity tier(s):** **T4** for poaching-vulnerable taxa and identified rare-plant localities; T1–T2 for aggregate cover, composition, and common-species range.
- **Pipeline shape:** Standard intake → validation → derive → publish, with sensitive-lane fail-closed gate on T4 emissions; redaction receipts required on public-safe derivatives.
- **Dossier:** `docs/domains/flora/` — `I.` sensitivity rules (KDWP / USFWS / KS state listings / herbarium policy), `K.` validators (taxonomy version, voucher requirement), `M.` correction posture.

[↑ back to top](#top)

---

## 2. Indicator subset

Emphasis per README §5.1: **Sensitivity-and-rights (T4 defaults) · Evidence-and-source**.

| Indicator | §24.11 cat. | Domain-scale healthy posture | Receipt / signal source |
|:---|:---|:---|:---|
| **Sensitive-lane fail-closed rate** | 24.11.3 | **100% at the first gate** for any T4 locality emission. | `PolicyDecision` DENY counts |
| RedactionReceipt coverage | 24.11.3 | 100% on public-safe derivatives of T4 records. | `RedactionReceipt` |
| Review-aged-out incidence | 24.11.3 | Sensitive-lane claims past review cadence dispositioned within tolerance. | `ReviewRecord` |
| Rights-change response time | 24.11.3 | Median time from listing change to tier reassignment within tolerance. | Source descriptors, `ReviewRecord` |
| Sensitive-content side-channel audit | 24.11.3 | Periodic checks for label / map-popup / AI-text leakage of T4 localities. | Audit logs, `RepresentationReceipt` |
| EvidenceRef resolution rate | 24.11.1 | > 99.9% across herbarium / iNaturalist / Kansas Native Plant Society / KBS cites. | `ValidationReport`, EvidenceBundle index |
| Source-role distribution drift | 24.11.1 | Voucher-specimen vs photo-observation mix tracked; no silent shift. | Source descriptors |
| Quarantine throughput | 24.11.1 | Cause distribution visible (taxonomy version, locality precision); no sustained backlog. | `ValidationReport`, quarantine ledger |

[↑ back to top](#top)

---

## 3. Domain-specific indicators (PROPOSED)

| PROPOSED indicator | Why flora-specific | Candidate §24.11 home |
|:---|:---|:---|
| Voucher-specimen coverage | % of identified rare-plant claims backed by a voucher specimen vs photo-only. | §24.11.1 |
| Taxonomy edition skew | Mixed APG / Flora of the Great Plains editions in a single derivative. | §24.11.5 |
| Poaching-pattern audit | Periodic check for repeat-pattern queries against the same T4 locality (defensive analytics). | §24.11.3 |

[↑ back to top](#top)

---

## 4. Ownership

- **Domain steward:** OWNER_TBD (flora dossier owner).
- **Governance-health steward:** OWNER_TBD (**sensitivity reviewer** + rights-holder representative).
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

- **Trigger events:** state/federal listing change; flora dossier edition; Atlas §24.11 amendment; side-channel audit alert.
- **Default cadence:** quarterly; **immediate** on poaching-pattern audit alert.

[↑ back to top](#top)

---

## 7. Open questions

- [ ] **OPEN-DASH-FLORA-01** — Confirm the voucher-specimen coverage threshold per taxon class.
- [ ] **OPEN-DASH-FLORA-02** — Define the poaching-pattern audit query shape — is it a §24.11.3 indicator or a separate defensive-analytics surface?
- [ ] **OPEN-DASH-FLORA-03** — Confirm sensitivity-reviewer-on-PR gate per OPEN-DASH-08.

[↑ back to top](#top)

---

## 8. Evidence basis & citations

<details>
<summary><strong>Source ledger</strong></summary>

| Source | Status | Supports | Limits |
|:---|:---|:---|:---|
| Atlas v1.1 §24.11.3 / §24.11.1 | CONFIRMED (manuscript) | §2 indicator subset. | Indicators PROPOSED at source. |
| Atlas v1.0 Ch. 8 (Flora dossier) | CONFIRMED (manuscript) | §1 scope, T4 default; §3 candidates. | Mounted dossier presence NEEDS VERIFICATION. |
| Atlas v1.1 §24.5 (Sensitivity tier reference) | CONFIRMED authored sibling | T4 default for poaching-vulnerable taxa. | Tier table PROPOSED. |
| `docs/dashboards/domain/README.md` §5.1, §6 | CONFIRMED | Emphasis; template. | Lane PROPOSED (OPEN-DASH-01). |

</details>

[↑ back to top](#top)

---

<sub>Per-domain flora dashboard specification. **Specification only — implementations live in `apps/`; indicator definitions live in Atlas §24.11; domain context lives in `docs/domains/flora/`.** T4 default for poaching-vulnerable taxa: dashboard reports, gate enforces, receipts back the trust.</sub>
