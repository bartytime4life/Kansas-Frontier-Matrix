<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-domain-agriculture
title: Agriculture Dashboard Specification (PROPOSED lane; per-domain instance of Atlas §24.11)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: agriculture-domain steward + governance-health steward
created: 2026-05-26
updated: 2026-05-26
policy_label: public
related:
  - kfm://doc/dashboards-domain-readme
  - kfm://doc/atlas-v1-1
  - kfm://doc/atlas-v1-1-ch24-5-sensitivity-tier-reference
  - kfm://doc/atlas-v1-1-ch24-6-pipeline-gate-reference
  - kfm://doc/domains-agriculture-dossier                    # CONFIRMED dossier home: docs/domains/agriculture/
  - kfm://adr/dashboards-lane-existence                      # PROPOSED candidate: OPEN-DASH-01
tags: [kfm, dashboards, domain, agriculture, indicators, governance-health, specification]
notes:
  - Per-domain instance of Atlas v1.1 §24.11. Specification only; not an implementation.
  - Atlas §24.11 wins on indicator conflicts; agriculture dossier wins on context conflicts.
[/KFM_META_BLOCK_V2] -->

# Agriculture Dashboard Specification

<!-- [doc: kfm://doc/dashboards-domain-agriculture] -->
<a id="top"></a>

> Per-domain dashboard specification for **Agriculture** (Atlas v1.0 Ch. 9). Cropland data layer (CDL), Census of Agriculture, NASS QuickStats, irrigation, and farm-level claims; **operator-identifiability** is the recurrent sensitivity exposure.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Atlas chapter: Ch. 9" src="https://img.shields.io/badge/atlas-Ch.%209-purple">
  <img alt="Indicator emphasis: 24.11.1 / 24.11.5" src="https://img.shields.io/badge/emphasis-24.11.1%20%C2%B7%2024.11.5-informational">
  <img alt="Policy label: public" src="https://img.shields.io/badge/policy--label-public-lightgrey">
</p>

> [!IMPORTANT]
> **Truth posture.** Indicators PROPOSED; instances PROPOSED; lane PROPOSED (OPEN-DASH-01); implementation NEEDS VERIFICATION.

> [!CAUTION]
> **Operator identifiability.** NASS suppression rules (n<3 cell suppression, complementary suppression) are a sensitivity gate, not a styling preference. The dashboard surfaces compliance posture; the gate enforces the suppression itself.

---

## 1. Domain scope

- **Atlas chapter:** v1.0 Ch. 9 (Agriculture).
- **Default sensitivity tier(s):** T1–T2 for state/county aggregates within NASS suppression rules; **T3** where parcel-level cropping pattern + irrigation type makes operator identification plausible.
- **Pipeline shape:** Standard intake → validation → derive → publish, with NASS-suppression validator on every aggregation.
- **Dossier:** `docs/domains/agriculture/` — `K.` validators (CDL class taxonomy, NASS suppression), `M.` correction posture for CDL re-releases.

[↑ back to top](#top)

---

## 2. Indicator subset

Emphasis per README §5.1: **Evidence-and-source · Documentation-and-drift**.

| Indicator | §24.11 cat. | Domain-scale healthy posture | Receipt / signal source |
|:---|:---|:---|:---|
| EvidenceRef resolution rate | 24.11.1 | > 99.9% across CDL / NASS QuickStats / Census of Agriculture / KDA cites; per-source rate visible. | `ValidationReport`, EvidenceBundle index |
| Source-role distribution drift | 24.11.1 | CDL remains the canonical cover-class role; NASS reported-vs-modeled mix tracked. | Source descriptors |
| Stale source rate | 24.11.1 | CDL annual epoch + NASS QuickStats refresh tracked; Census of Agriculture quinquennial alignment dispositioned. | Source descriptors, freshness cadence metadata |
| Quarantine throughput | 24.11.1 | Cause distribution visible (suppression-rule violation, CDL class drift); no sustained backlog. | `ValidationReport`, quarantine ledger |
| ADR completeness | 24.11.5 | Open agriculture ADRs (CDL class canonicalization, irrigation classification) tracked to a state. | ADR index |
| Drift register size | 24.11.5 | Agriculture-derivative drift surfaced; trend not regressing across crop years. | `docs/registers/DRIFT_REGISTER.md` |
| Per-root README presence | 24.11.5 | `docs/domains/agriculture/README.md` exists and is current. | Directory-rules linter output |
| Atlas / supplement lineage clarity | 24.11.5 | Each crop-year supplement carries forward/back links. | Supersession entries |

[↑ back to top](#top)

---

## 3. Domain-specific indicators (PROPOSED)

| PROPOSED indicator | Why agriculture-specific | Candidate §24.11 home |
|:---|:---|:---|
| NASS suppression-rule compliance | % of published aggregates that pass NASS n<3 + complementary suppression checks. | §24.11.3 (sensitivity variant) |
| CDL class taxonomy version skew | Cross-year aggregates silently mixing CDL class definitions. | §24.11.5 |
| Irrigation-classification confidence | Distribution of irrigation classification confidence (remote-sensed vs. WIMAS-derived). | §24.11.1 |

[↑ back to top](#top)

---

## 4. Ownership

- **Domain steward:** OWNER_TBD (agriculture dossier owner).
- **Governance-health steward:** OWNER_TBD (source steward + docs steward).
- **Implementation owner:** OWNER_TBD (`apps/review-console/` team).

[↑ back to top](#top)

---

## 5. Implementation pointer

- **Dashboard app:** `apps/review-console/` (PROPOSED) — `UNKNOWN` until verified.
- **Telemetry:** `runtime/observability/` (PROPOSED) — `UNKNOWN`.
- **Schemas read:** `schemas/contracts/v1/validation/`, `schemas/contracts/v1/source/`.
- **Policy bundles emitting signals:** `policy/sources/`, `policy/documentation/`, `policy/sensitivity/` (suppression).

[↑ back to top](#top)

---

## 6. Review cadence

- **Trigger events:** CDL annual release; NASS QuickStats schema change; Census of Agriculture quinquennial publication; agriculture dossier edition.
- **Default cadence:** annual (post-CDL release); semi-annual review of suppression-rule compliance.

[↑ back to top](#top)

---

## 7. Open questions

- [ ] **OPEN-DASH-AG-01** — Confirm NASS suppression-rule compliance home (§24.11.3 vs. agriculture-local).
- [ ] **OPEN-DASH-AG-02** — Define irrigation-classification confidence indicator scope (vs. hydrology spec).
- [ ] **OPEN-DASH-AG-03** — Decide whether parcel-level T3 lift triggers fauna/flora-style sensitivity-reviewer gating.

[↑ back to top](#top)

---

## 8. Evidence basis & citations

<details>
<summary><strong>Source ledger</strong></summary>

| Source | Status | Supports | Limits |
|:---|:---|:---|:---|
| Atlas v1.1 §24.11.1 / §24.11.5 | CONFIRMED (manuscript) | §2 indicator subset. | Indicators PROPOSED at source. |
| Atlas v1.0 Ch. 9 (Agriculture dossier) | CONFIRMED (manuscript) | §1 scope; §3 candidates. | Mounted dossier presence NEEDS VERIFICATION. |
| `docs/dashboards/domain/README.md` §5.1, §6 | CONFIRMED | Emphasis; template. | Lane PROPOSED (OPEN-DASH-01). |

</details>

[↑ back to top](#top)

---

<sub>Per-domain agriculture dashboard specification. **Specification only — implementations live in `apps/`; indicator definitions live in Atlas §24.11; domain context lives in `docs/domains/agriculture/`.** NASS suppression rules are enforced at the gate; the dashboard reports compliance posture.</sub>
