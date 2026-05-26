<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-domain-habitat
title: Habitat Dashboard Specification (PROPOSED lane; per-domain instance of Atlas §24.11)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: habitat-domain steward + governance-health steward
created: 2026-05-26
updated: 2026-05-26
policy_label: public
related:
  - kfm://doc/dashboards-domain-readme
  - kfm://doc/atlas-v1-1
  - kfm://doc/atlas-v1-1-ch24-5-sensitivity-tier-reference
  - kfm://doc/atlas-v1-1-ch24-6-pipeline-gate-reference
  - kfm://doc/domains-habitat-dossier                        # CONFIRMED dossier home: docs/domains/habitat/
  - kfm://adr/dashboards-lane-existence                      # PROPOSED candidate: OPEN-DASH-01
tags: [kfm, dashboards, domain, habitat, indicators, governance-health, specification]
notes:
  - Per-domain instance of the master indicator catalog (Atlas v1.1 §24.11). Specification only; not an implementation.
  - Habitat carries sensitivity exposure where polygons touch sensitive-species range; T-tier per dossier §I.
  - Atlas §24.11 wins on indicator-definition conflicts; the habitat dossier wins on context conflicts.
[/KFM_META_BLOCK_V2] -->

# Habitat Dashboard Specification

<!-- [doc: kfm://doc/dashboards-domain-habitat] -->
<a id="top"></a>

> Per-domain dashboard specification for **Habitat** (Atlas v1.0 Ch. 6). Instances the Atlas §24.11 governance health indicators at the habitat scale; surfaces sensitivity-and-rights posture wherever habitat polygons intersect sensitive-species range.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Atlas chapter: Ch. 6" src="https://img.shields.io/badge/atlas-Ch.%206-purple">
  <img alt="Indicator emphasis: 24.11.1 / 24.11.3" src="https://img.shields.io/badge/emphasis-24.11.1%20%C2%B7%2024.11.3-informational">
  <img alt="Policy label: public" src="https://img.shields.io/badge/policy--label-public-lightgrey">
</p>

> [!IMPORTANT]
> **Truth posture.** Indicator catalog from Atlas §24.11 is PROPOSED. Per-domain instances PROPOSED. Lane PROPOSED per OPEN-DASH-01. Implementation status NEEDS VERIFICATION.

> [!CAUTION]
> **Sensitivity coupling.** Habitat polygons are not themselves sensitive, but their intersection with fauna/flora T4 range can leak species locations. This dashboard surfaces the **fail-closed rate** at that intersection; the dashboard does not, itself, decide redaction.

---

## 1. Domain scope

- **Atlas chapter:** v1.0 Ch. 6 (Habitat).
- **Default sensitivity tier(s):** T1–T2 baseline; **escalates to T3/T4** by intersection with fauna/flora sensitive-species range.
- **Pipeline shape:** Standard intake → validation → derive → publish, with sensitive-lane fail-closed gate on cross-domain join with fauna/flora.
- **Dossier:** `docs/domains/habitat/` — `K.` validators (cover-class taxonomy, ecoregion membership), `I.` sensitivity coupling rules.

[↑ back to top](#top)

---

## 2. Indicator subset

Emphasis per README §5.1: **Evidence-and-source · Sensitivity-and-rights**.

| Indicator | §24.11 cat. | Domain-scale healthy posture | Receipt / signal source |
|:---|:---|:---|:---|
| EvidenceRef resolution rate | 24.11.1 | > 99.9% across NLCD/LANDFIRE/KBS habitat cites; per-source rate visible. | `ValidationReport`, EvidenceBundle index |
| Source-role distribution drift | 24.11.1 | NLCD remains the canonical cover-class role; LANDFIRE / Kansas Biological Survey roles tracked separately. | Source descriptors |
| Stale source rate | 24.11.1 | NLCD epoch refresh tracked; lag dispositioned, not silent. | Source descriptors, freshness cadence metadata |
| Quarantine throughput | 24.11.1 | Cause distribution visible (cover-class taxonomy drift, projection); no sustained backlog. | `ValidationReport`, quarantine ledger |
| **Sensitive-lane fail-closed rate** | 24.11.3 | **100% at the first gate** for any habitat × sensitive-species join. | `PolicyDecision` DENY counts |
| RedactionReceipt coverage | 24.11.3 | 100% on habitat layers public-safe-derived from sensitive-species joins. | `RedactionReceipt` |
| Review-aged-out incidence | 24.11.3 | Habitat-as-proxy claims past review cadence dispositioned within tolerance. | `ReviewRecord` |
| Sensitive-content side-channel audit | 24.11.3 | Periodic audit for habitat-polygon vertex density that could re-identify sensitive nest / den sites. | Audit logs, `RepresentationReceipt` |

[↑ back to top](#top)

---

## 3. Domain-specific indicators (PROPOSED)

| PROPOSED indicator | Why habitat-specific | Candidate §24.11 home |
|:---|:---|:---|
| Cover-class taxonomy version skew | Mixed NLCD epochs / LANDFIRE versions across a single map sheet is a recurrent defect. | §24.11.5 |
| Vertex-density side-channel exposure | Habitat polygons with abnormally tight vertex density at sensitive-species range edges. | §24.11.3 |

[↑ back to top](#top)

---

## 4. Ownership

- **Domain steward:** OWNER_TBD (habitat dossier owner).
- **Governance-health steward:** OWNER_TBD (sensitivity reviewer + source steward).
- **Implementation owner:** OWNER_TBD (`apps/review-console/` team).

[↑ back to top](#top)

---

## 5. Implementation pointer

- **Dashboard app:** `apps/review-console/` (PROPOSED) — `UNKNOWN` until verified.
- **Telemetry:** `runtime/observability/` (PROPOSED) — `UNKNOWN`.
- **Schemas read:** `schemas/contracts/v1/validation/`, `schemas/contracts/v1/sensitivity/`, `schemas/contracts/v1/redaction/`.
- **Policy bundles emitting signals:** `policy/sensitivity/`, `policy/sources/`.

[↑ back to top](#top)

---

## 6. Review cadence

- **Trigger events:** NLCD/LANDFIRE epoch bump; fauna/flora dossier edition (sensitivity coupling); Atlas §24.11 amendment.
- **Default cadence:** quarterly; **immediate** review on any sensitive-lane denial pattern change.

[↑ back to top](#top)

---

## 7. Open questions

- [ ] **OPEN-DASH-HABITAT-01** — Define the vertex-density side-channel threshold (per cover class? per ecoregion?).
- [ ] **OPEN-DASH-HABITAT-02** — Reconcile NLCD-epoch skew detection between this spec and the soil spec (cross-domain).

[↑ back to top](#top)

---

## 8. Evidence basis & citations

<details>
<summary><strong>Source ledger</strong></summary>

| Source | Status | Supports | Limits |
|:---|:---|:---|:---|
| Atlas v1.1 §24.11.1 / §24.11.3 | CONFIRMED (manuscript) | §2 indicator subset. | Indicators PROPOSED at source. |
| Atlas v1.0 Ch. 6 (Habitat dossier) | CONFIRMED (manuscript) | §1 scope; §3 candidates. | Mounted dossier presence NEEDS VERIFICATION. |
| Atlas v1.1 §24.10 (Risk register) | CONFIRMED (manuscript) | §2 sensitive-lane emphasis (habitat × T4 species). | Risk severities PROPOSED. |
| `docs/dashboards/domain/README.md` §5.1, §6 | CONFIRMED | §2 emphasis (Evidence-and-source · Sensitivity-and-rights); template. | Lane PROPOSED (OPEN-DASH-01). |

</details>

[↑ back to top](#top)

---

<sub>Per-domain habitat dashboard specification. **Specification only — implementations live in `apps/`; indicator definitions live in Atlas §24.11; domain context lives in `docs/domains/habitat/`.** Habitat sensitivity escalates via intersection with fauna/flora; the gate enforces, the dashboard reports.</sub>
