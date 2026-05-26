<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-domain-geology
title: Geology / Natural Resources Dashboard Specification (PROPOSED lane; per-domain instance of Atlas §24.11)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: geology-domain steward + governance-health steward
created: 2026-05-26
updated: 2026-05-26
policy_label: public
related:
  - kfm://doc/dashboards-domain-readme
  - kfm://doc/atlas-v1-1
  - kfm://doc/atlas-v1-1-ch24-5-sensitivity-tier-reference
  - kfm://doc/atlas-v1-1-ch24-6-pipeline-gate-reference
  - kfm://doc/domains-geology-dossier                        # CONFIRMED dossier home: docs/domains/geology/
  - kfm://adr/dashboards-lane-existence                      # PROPOSED candidate: OPEN-DASH-01
tags: [kfm, dashboards, domain, geology, natural-resources, indicators, governance-health, specification]
notes:
  - Per-domain instance of Atlas v1.1 §24.11. Specification only; not an implementation.
  - Operator/well-owner identifiability lifts T from T1–T2 to T3 on certain well-record products.
  - Atlas §24.11 wins on indicator conflicts; geology dossier wins on context conflicts.
[/KFM_META_BLOCK_V2] -->

# Geology / Natural Resources Dashboard Specification

<!-- [doc: kfm://doc/dashboards-domain-geology] -->
<a id="top"></a>

> Per-domain dashboard specification for **Geology / Natural Resources** (Atlas v1.0 Ch. 10). Bedrock/surficial geology, mineral resources, oil & gas, well records, geophysics. Source coverage breadth is the dominant signal.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Atlas chapter: Ch. 10" src="https://img.shields.io/badge/atlas-Ch.%2010-purple">
  <img alt="Indicator emphasis: 24.11.1" src="https://img.shields.io/badge/emphasis-24.11.1-informational">
  <img alt="Policy label: public" src="https://img.shields.io/badge/policy--label-public-lightgrey">
</p>

> [!IMPORTANT]
> **Truth posture.** Indicators PROPOSED; instances PROPOSED; lane PROPOSED (OPEN-DASH-01); implementation NEEDS VERIFICATION.

---

## 1. Domain scope

- **Atlas chapter:** v1.0 Ch. 10 (Geology / Natural Resources).
- **Default sensitivity tier(s):** T1 for bedrock/surficial geology and aggregate resources; **T3** where well-record granularity reveals operator/owner identity.
- **Pipeline shape:** Standard intake → validation → derive → publish; well-record products carry an additional operator-identifiability gate.
- **Dossier:** `docs/domains/geology/` — `K.` validators (lithology, stratigraphy, KGS WIZARD schema), `M.` correction posture for re-interpreted units.

[↑ back to top](#top)

---

## 2. Indicator subset

Emphasis per README §5.1: **Evidence-and-source**.

| Indicator | §24.11 cat. | Domain-scale healthy posture | Receipt / signal source |
|:---|:---|:---|:---|
| EvidenceRef resolution rate | 24.11.1 | > 99.9% across KGS / USGS / KDHE cites; per-source rate visible. | `ValidationReport`, EvidenceBundle index |
| Cite-or-abstain compliance | 24.11.1 | 100% — any AI-generated lithology / age claim must cite or abstain. | `AIReceipt` |
| Source-role distribution drift | 24.11.1 | KGS canonical for bedrock map units; USGS for stratigraphy. No silent role shift. | Source descriptors |
| Stale source rate | 24.11.1 | KGS WIZARD / well-record refresh tracked; lag dispositioned. | Source descriptors, freshness cadence metadata |
| Quarantine throughput | 24.11.1 | Cause distribution visible (stratigraphic-unit drift, datum, lithology vocabulary); no sustained backlog. | `ValidationReport`, quarantine ledger |

[↑ back to top](#top)

---

## 3. Domain-specific indicators (PROPOSED)

| PROPOSED indicator | Why geology-specific | Candidate §24.11 home |
|:---|:---|:---|
| Stratigraphic-unit canonicalization coverage | % of map units mapped to a canonical KGS stratigraphic ID. | §24.11.1 |
| Well-record operator-identifiability gate compliance | % of published well-record derivatives that passed the operator-identifiability gate. | §24.11.3 |
| Lithology vocabulary version skew | Cross-product use of differing lithology vocabularies (BGS / USGS-NGD / KGS). | §24.11.5 |

[↑ back to top](#top)

---

## 4. Ownership

- **Domain steward:** OWNER_TBD (geology dossier owner).
- **Governance-health steward:** OWNER_TBD (source steward; sensitivity reviewer for well-record products).
- **Implementation owner:** OWNER_TBD (`apps/review-console/` team).

[↑ back to top](#top)

---

## 5. Implementation pointer

- **Dashboard app:** `apps/review-console/` (PROPOSED) — `UNKNOWN` until verified.
- **Telemetry:** `runtime/observability/` (PROPOSED) — `UNKNOWN`.
- **Schemas read:** `schemas/contracts/v1/validation/`, `schemas/contracts/v1/source/`, `schemas/contracts/v1/sensitivity/` (well records).
- **Policy bundles emitting signals:** `policy/sources/`, `policy/sensitivity/` (well-record gate).

[↑ back to top](#top)

---

## 6. Review cadence

- **Trigger events:** KGS publication cycle; well-record schema change; geology dossier edition.
- **Default cadence:** annual; semi-annual for well-record products.

[↑ back to top](#top)

---

## 7. Open questions

- [ ] **OPEN-DASH-GEO-01** — Confirm operator-identifiability gate scope (which well-record fields trigger).
- [ ] **OPEN-DASH-GEO-02** — Reconcile stratigraphic vocabulary canonicalization with USGS NGD adoption.

[↑ back to top](#top)

---

## 8. Evidence basis & citations

<details>
<summary><strong>Source ledger</strong></summary>

| Source | Status | Supports | Limits |
|:---|:---|:---|:---|
| Atlas v1.1 §24.11.1 | CONFIRMED (manuscript) | §2 indicator subset. | Indicators PROPOSED at source. |
| Atlas v1.0 Ch. 10 (Geology dossier) | CONFIRMED (manuscript) | §1 scope; §3 candidates. | Mounted dossier presence NEEDS VERIFICATION. |
| `docs/dashboards/domain/README.md` §5.1, §6 | CONFIRMED | Emphasis; template. | Lane PROPOSED (OPEN-DASH-01). |

</details>

[↑ back to top](#top)

---

<sub>Per-domain geology dashboard specification. **Specification only — implementations live in `apps/`; indicator definitions live in Atlas §24.11; domain context lives in `docs/domains/geology/`.** Well-record products carry an additional identifiability gate; the dashboard reports gate-compliance posture.</sub>
