<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-domain-soil
title: Soil Dashboard Specification (PROPOSED lane; per-domain instance of Atlas §24.11)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: soil-domain steward + governance-health steward
created: 2026-05-26
updated: 2026-05-26
policy_label: public
related:
  - kfm://doc/dashboards-domain-readme
  - kfm://doc/atlas-v1-1
  - kfm://doc/atlas-v1-1-ch24-5-sensitivity-tier-reference
  - kfm://doc/atlas-v1-1-ch24-6-pipeline-gate-reference
  - kfm://doc/domains-soil-dossier                           # CONFIRMED dossier home: docs/domains/soil/
  - kfm://adr/dashboards-lane-existence                      # PROPOSED candidate: OPEN-DASH-01
tags: [kfm, dashboards, domain, soil, indicators, governance-health, specification]
notes:
  - Per-domain instance of the master indicator catalog (Atlas v1.1 §24.11). Specification only; not an implementation.
  - Atlas §24.11 wins on indicator-definition conflicts; the soil dossier wins on context conflicts.
  - Mounted-repo implementation status is NEEDS VERIFICATION.
[/KFM_META_BLOCK_V2] -->

# Soil Dashboard Specification

<!-- [doc: kfm://doc/dashboards-domain-soil] -->
<a id="top"></a>

> Per-domain dashboard specification for **Soil** (Atlas v1.0 Ch. 5). Instances the Atlas §24.11 governance health indicators at the soil scale; does **not** redefine them.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Atlas chapter: Ch. 5" src="https://img.shields.io/badge/atlas-Ch.%205-purple">
  <img alt="Indicator emphasis: 24.11.1 / 24.11.5" src="https://img.shields.io/badge/emphasis-24.11.1%20%C2%B7%2024.11.5-informational">
  <img alt="Policy label: public" src="https://img.shields.io/badge/policy--label-public-lightgrey">
</p>

> [!IMPORTANT]
> **Truth posture.** Indicator catalog from Atlas §24.11 is PROPOSED. Per-domain instances in this file are PROPOSED. The lane is PROPOSED per OPEN-DASH-01. Implementation status is NEEDS VERIFICATION.

> [!NOTE]
> **Anti-collapse rule.** A soil dashboard reports posture; soil **decisions** rest on SSURGO/STATSGO receipts, KGS profile records, and the validators this spec points to.

---

## 1. Domain scope

- **Atlas chapter:** v1.0 Ch. 5 (Soil).
- **Default sensitivity tier(s):** T1 (public soil survey products); T2 where parcel-level resolution invites re-identification.
- **Pipeline shape:** Standard intake → validation → derive → publish; long-stable upstream sources (SSURGO) emphasize **documentation-and-drift** posture over release cadence.
- **Dossier:** `docs/domains/soil/` — `K.` validators (texture / classification / map-unit), `M.` correction posture for survey re-issues, `N.` verification backlog.

[↑ back to top](#top)

---

## 2. Indicator subset

Emphasis per README §5.1: **Evidence-and-source · Documentation-and-drift**.

| Indicator | §24.11 cat. | Domain-scale healthy posture | Receipt / signal source |
|:---|:---|:---|:---|
| EvidenceRef resolution rate | 24.11.1 | > 99.9% across SSURGO/STATSGO/KGS profile cites; per-source rate visible. | `ValidationReport`, EvidenceBundle index |
| Source-role distribution drift | 24.11.1 | SSURGO remains the canonical map-unit role; auxiliary roles (KGS, USDA-NRCS interpretations) tracked separately. | Source descriptors |
| Stale source rate | 24.11.1 | Survey-area refresh aligns with NRCS publication cadence; lag is dispositioned, not silent. | Source descriptors, freshness cadence metadata |
| Quarantine throughput | 24.11.1 | Quarantine causes visible (map-unit-key mismatch, attribute-domain violation); no sustained backlog. | `ValidationReport`, quarantine ledger |
| ADR completeness | 24.11.5 | Open soil ADRs (taxonomy version, map-unit canonicalization) tracked to a state. | ADR index |
| Drift register size | 24.11.5 | Hydric-soil and prime-farmland derivative drift surfaced; trend not regressing. | `docs/registers/DRIFT_REGISTER.md` |
| Per-root README presence | 24.11.5 | `docs/domains/soil/README.md` exists and is current. | Directory-rules linter output |
| Atlas / supplement lineage clarity | 24.11.5 | Each soil-supplement carries forward/back links; no orphan supplements. | Supersession entries |

[↑ back to top](#top)

---

## 3. Domain-specific indicators (PROPOSED)

| PROPOSED indicator | Why soil-specific | Candidate §24.11 home |
|:---|:---|:---|
| Map-unit-key stability | SSURGO MUKEY changes across survey areas / years are a recurrent silent-drift source. | §24.11.5 |
| Soil-taxonomy edition skew | Mixing Keys-to-Soil-Taxonomy editions across map sheets is a documentation drift. | §24.11.5 |
| Hydric-soil derivative coverage | Coverage of hydric-soil derivative against the publication baseline. | §24.11.1 (coverage variant) |

[↑ back to top](#top)

---

## 4. Ownership

- **Domain steward:** OWNER_TBD (soil dossier owner).
- **Governance-health steward:** OWNER_TBD (source steward + docs steward per Atlas §24.7).
- **Implementation owner:** OWNER_TBD (`apps/review-console/` team).

[↑ back to top](#top)

---

## 5. Implementation pointer

- **Dashboard app:** `apps/review-console/` (PROPOSED) — `UNKNOWN` until verified.
- **Telemetry:** `runtime/observability/` (PROPOSED) — `UNKNOWN`.
- **Schemas read:** `schemas/contracts/v1/validation/`, `schemas/contracts/v1/source/`.
- **Policy bundles emitting signals:** `policy/sources/`, `policy/documentation/`.

[↑ back to top](#top)

---

## 6. Review cadence

- **Trigger events:** SSURGO/STATSGO publication-window bump; soil dossier edition; Atlas §24.11 amendment.
- **Default cadence:** semi-annual review (soil sources change slowly).

[↑ back to top](#top)

---

## 7. Open questions

- [ ] **OPEN-DASH-SOIL-01** — Confirm MUKEY-stability indicator scope (across survey years vs. across upstream re-issues).
- [ ] **OPEN-DASH-SOIL-02** — Decide whether the hydric-soil coverage indicator belongs here or in habitat (cross-domain dependency).

[↑ back to top](#top)

---

## 8. Evidence basis & citations

<details>
<summary><strong>Source ledger</strong></summary>

| Source | Status | Supports | Limits |
|:---|:---|:---|:---|
| Atlas v1.1 §24.11.1 / §24.11.5 | CONFIRMED (manuscript) | §2 indicator subset. | Indicators PROPOSED at source. |
| Atlas v1.0 Ch. 5 (Soil dossier) | CONFIRMED (manuscript) | §1 scope; §3 candidates. | Mounted dossier presence NEEDS VERIFICATION. |
| `docs/dashboards/domain/README.md` §5.1, §6 | CONFIRMED | §2 emphasis; this file's skeleton. | Lane PROPOSED (OPEN-DASH-01). |

</details>

[↑ back to top](#top)

---

<sub>Per-domain soil dashboard specification. **Specification only — implementations live in `apps/`; indicator definitions live in Atlas §24.11; domain context lives in `docs/domains/soil/`.**</sub>
