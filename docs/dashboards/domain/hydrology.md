<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-domain-hydrology
title: Hydrology Dashboard Specification (PROPOSED lane; per-domain instance of Atlas §24.11)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: hydrology-domain steward + governance-health steward
created: 2026-05-26
updated: 2026-05-26
policy_label: public
related:
  - kfm://doc/dashboards-domain-readme                       # CONFIRMED authored sibling
  - kfm://doc/atlas-v1-1                                     # PROPOSED: docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf §24.11
  - kfm://doc/atlas-v1-1-ch24-5-sensitivity-tier-reference   # CONFIRMED authored sibling
  - kfm://doc/atlas-v1-1-ch24-6-pipeline-gate-reference      # CONFIRMED authored sibling
  - kfm://doc/domains-hydrology-dossier                      # CONFIRMED dossier home: docs/domains/hydrology/
  - kfm://adr/dashboards-lane-existence                      # PROPOSED candidate: OPEN-DASH-01
tags: [kfm, dashboards, domain, hydrology, indicators, governance-health, specification]
notes:
  - Per-domain instance of the master indicator catalog (Atlas v1.1 §24.11). Specification only; not an implementation.
  - Atlas §24.11 wins on indicator-definition conflicts; the hydrology dossier wins on context conflicts.
  - Mounted-repo implementation status is NEEDS VERIFICATION.
[/KFM_META_BLOCK_V2] -->

# Hydrology Dashboard Specification

<!-- [doc: kfm://doc/dashboards-domain-hydrology] -->
<a id="top"></a>

> Per-domain dashboard specification for **Hydrology** (Atlas v1.0 Ch. 4). Instances the Atlas §24.11 governance health indicators at the hydrology scale; does **not** redefine them.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Atlas chapter: Ch. 4" src="https://img.shields.io/badge/atlas-Ch.%204-purple">
  <img alt="Indicator emphasis: 24.11.1 / 24.11.2 / 24.11.5" src="https://img.shields.io/badge/emphasis-24.11.1%20%C2%B7%2024.11.2%20%C2%B7%2024.11.5-informational">
  <img alt="Policy label: public" src="https://img.shields.io/badge/policy--label-public-lightgrey">
</p>

> [!IMPORTANT]
> **Truth posture.** Indicator catalog from Atlas §24.11 is PROPOSED. Per-domain instances in this file are PROPOSED. The lane (`docs/dashboards/`) is PROPOSED per OPEN-DASH-01. Implementation status is NEEDS VERIFICATION.

> [!NOTE]
> **Anti-collapse rule.** This spec **reports** posture; it does not enforce it. Hydrology decisions rest on the receipts, evidence bundles, and validators this spec points to. *(Atlas v1.1 §24.11, CONFIRMED.)*

---

## 1. Domain scope

- **Atlas chapter:** v1.0 Ch. 4 (Hydrology).
- **Default sensitivity tier(s):** T1–T2 (public hydrography; well-record privacy escalates to T3 on identifiability). *(See `docs/atlases/chapters/24-5-sensitivity-tier-reference.md`.)*
- **Pipeline shape:** Standard intake → validation → derive → publish, with rollback-target requirement on every published gauge/derived layer. *(See `docs/atlases/chapters/24-6-pipeline-gate-reference.md`.)*
- **Dossier:** `docs/domains/hydrology/` — the dossier's `K.` validators, `M.` publication/correction/rollback, and `N.` verification backlog supply the *why* behind every healthy-posture value below. **Dossier wins on context conflicts.**

[↑ back to top](#top)

---

## 2. Indicator subset

The hydrology dashboard surfaces the §24.11 indicators below. Emphasis follows README §5.1: **Evidence-and-source · Release-correction-rollback · Documentation-and-drift**.

| Indicator | §24.11 cat. | Domain-scale healthy posture | Receipt / signal source |
|:---|:---|:---|:---|
| EvidenceRef resolution rate | 24.11.1 | > 99.9% over trailing release window (matches master); per-source rate visible for USGS NWIS, KGS WIZARD, NOAA NWM, KDA WIMAS. | `ValidationReport`, EvidenceBundle index |
| Source-role distribution drift | 24.11.1 | No silent shift in observed-vs-modeled mix without an ADR or steward note. | Source descriptors, `ValidationReport` |
| Stale source rate | 24.11.1 | All NWIS/WIMAS feeds within freshness cadence; stewards dispositioned within tolerance. | Source descriptors, freshness cadence metadata |
| Quarantine throughput | 24.11.1 | Quarantine cause distribution visible (units, projection, gauge-state); no sustained backlog. | `ValidationReport`, quarantine ledger |
| Release with rollback target | 24.11.2 | 100% — every published flow-network / floodplain / drought layer names a valid rollback target. | `ReleaseManifest`, `RollbackCard` |
| Correction lead time | 24.11.2 | Median lead time tracked; trend not regressing across drought / flood seasons. | `CorrectionNotice` |
| Derivative-invalidation coverage | 24.11.2 | Corrections to upstream hydrography cascade-invalidate downstream flood-extent / water-budget derivatives. | `CorrectionNotice`, lineage graph |
| Supersession lineage gap | 24.11.5 | Zero — every superseded hydrography product carries a forward link. | `ReleaseManifest`, supersession entries |
| ADR completeness | 24.11.5 | Open hydrography ADRs (CRS choice, gauge-canonicalization rule) tracked to a state. | ADR index |
| Per-root README presence | 24.11.5 | `docs/domains/hydrology/README.md` exists and is current. | Directory-rules linter output |

> [!TIP]
> Indicators not listed above are not silenced — they still roll up at the system scale via the cross-domain dashboard. They are simply not the **defining** signals for hydrology posture.

[↑ back to top](#top)

---

## 3. Domain-specific indicators (PROPOSED)

Candidates surfaced from the hydrology dossier (`docs/domains/hydrology/` §K / §N). Each is a **candidate §24.11 amendment**, not a local redefinition. Escalate via ADR per README §4.

| PROPOSED indicator | Why hydrology-specific | Candidate §24.11 home |
|:---|:---|:---|
| Gauge-state coverage | Operational gauges per HUC-8 vs declared baseline; flags silent gauge dropouts. | §24.11.1 (source-coverage variant) |
| Datum / CRS drift | Mixed-datum publication is a hydrology-recurrent defect (NAVD88 vs NGVD29). | §24.11.5 (documentation drift) |
| Hydrologic-year alignment | Year-on-year comparisons silently using calendar year instead of water year. | §24.11.5 (documentation drift) |

[↑ back to top](#top)

---

## 4. Ownership

- **Domain steward:** OWNER_TBD (hydrology dossier owner — resolve against Atlas v1.1 §24.7).
- **Governance-health steward:** OWNER_TBD (release steward + source steward — see Atlas §24.7 matrix).
- **Implementation owner:** OWNER_TBD (`apps/review-console/` team, pending OPEN-DASH-03).

[↑ back to top](#top)

---

## 5. Implementation pointer

- **Dashboard app:** `apps/review-console/` (PROPOSED, pending OPEN-DASH-03) — `UNKNOWN` until mounted-repo evidence confirms.
- **Telemetry:** `runtime/observability/` (PROPOSED) — `UNKNOWN` until confirmed.
- **Schemas read:** `schemas/contracts/v1/validation/`, `schemas/contracts/v1/release/`, `schemas/contracts/v1/correction/`.
- **Policy bundles emitting signals:** `policy/release/`, `policy/correction/`, `policy/sources/`.

[↑ back to top](#top)

---

## 6. Review cadence

- **Trigger events:** edition bump in `docs/domains/hydrology/`; Atlas §24.11 amendment; new `KFM-P*-FEAT-*` card naming a hydrology dashboard.
- **Default cadence:** quarterly review by docs steward + hydrology domain steward + governance-health steward.
- **Drift watch:** if `apps/` implementation diverges from this spec, log the divergence in `docs/registers/DRIFT_REGISTER.md` rather than silently reconciling.

[↑ back to top](#top)

---

## 7. Open questions

- [ ] **OPEN-DASH-HYDRO-01** — Confirm dashboard app path (`apps/review-console/` vs a future `apps/dashboards/`) per OPEN-DASH-03.
- [ ] **OPEN-DASH-HYDRO-02** — Resolve gauge-state coverage as either a hydrology-local indicator or a candidate §24.11.1 amendment.
- [ ] **OPEN-DASH-HYDRO-03** — Define the "hydrologic year" alignment check — flag, denial, or steward-note only?

[↑ back to top](#top)

---

## 8. Evidence basis & citations

<details>
<summary><strong>Source ledger</strong></summary>

| Source | Status | Supports | Limits |
|:---|:---|:---|:---|
| Atlas v1.1 §24.11.1 / §24.11.2 / §24.11.5 | CONFIRMED (manuscript) | §2 indicator subset rows. | Indicators labeled PROPOSED in source; VB-11-08 open. |
| Atlas v1.0 Ch. 4 (Hydrology dossier) | CONFIRMED (manuscript) | §1 domain scope; §3 candidate hydrology-specific indicators. | Mounted dossier presence NEEDS VERIFICATION. |
| `docs/dashboards/domain/README.md` §5.1, §6 template | CONFIRMED (this folder) | Skeleton used by this file; indicator emphasis (Evidence-and-source · Release-correction-rollback · Documentation-and-drift). | This folder is the PROPOSED lane (OPEN-DASH-01). |
| `docs/dashboards/INDICATOR_CATALOG.md` | CONFIRMED (this folder) | §2 indicator names and master healthy postures. | Mirror of Atlas; Atlas wins on conflicts. |

</details>

[↑ back to top](#top)

---

<sub>Per-domain hydrology dashboard specification. **Specification only — implementations live in `apps/`; indicator definitions live in Atlas §24.11; domain context lives in `docs/domains/hydrology/`.** Atlas v1.1 §24.11 wins on indicator conflicts; the hydrology dossier wins on context conflicts.</sub>
