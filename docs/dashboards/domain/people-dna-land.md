<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-domain-people-dna-land
title: People / Genealogy / DNA / Land Ownership Dashboard Specification (PROPOSED lane; per-domain instance of Atlas §24.11)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: people-dna-land-domain steward + sensitivity reviewer + AI-surface steward + governance-health steward
created: 2026-05-26
updated: 2026-05-26
policy_label: public
related:
  - kfm://doc/dashboards-domain-readme
  - kfm://doc/atlas-v1-1
  - kfm://doc/atlas-v1-1-ch24-5-sensitivity-tier-reference
  - kfm://doc/atlas-v1-1-ch24-6-pipeline-gate-reference
  - kfm://doc/domains-people-dna-land-dossier                # CONFIRMED dossier home: docs/domains/people-dna-land/
  - kfm://adr/dashboards-lane-existence                      # PROPOSED candidate: OPEN-DASH-01
tags: [kfm, dashboards, domain, people, genealogy, dna, land-ownership, t4, ai-surface, sensitivity, indicators, governance-health, specification]
notes:
  - Per-domain instance of Atlas v1.1 §24.11. Specification only; not an implementation.
  - Living-person records and DNA evidence default to T4; AI-surface posture is critical because synthetic genealogical claims are the recurrent risk.
  - The strictest single domain in KFM — three reviewer roles, two gates, and the lowest tolerance for synthetic-claim incidents.
  - Atlas §24.11 wins on indicator conflicts; people-dna-land dossier wins on context conflicts.
[/KFM_META_BLOCK_V2] -->

# People / Genealogy / DNA / Land Ownership Dashboard Specification

<!-- [doc: kfm://doc/dashboards-domain-people-dna-land] -->
<a id="top"></a>

> Per-domain dashboard specification for **People / Genealogy / DNA / Land Ownership** (Atlas v1.0 Ch. 16). Living-person records, DNA evidence, genealogical reasoning, land-ownership chains. The **strictest** domain in the project: T4 by default, AI-surface posture in the critical band, three reviewer roles.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Atlas chapter: Ch. 16" src="https://img.shields.io/badge/atlas-Ch.%2016-purple">
  <img alt="Indicator emphasis: 24.11.3 (living-person T4, DNA T4) / 24.11.4" src="https://img.shields.io/badge/emphasis-24.11.3%20%C2%B7%2024.11.4-informational">
  <img alt="Default tier: T4" src="https://img.shields.io/badge/default--tier-T4-red">
  <img alt="Policy label: public" src="https://img.shields.io/badge/policy--label-public-lightgrey">
</p>

> [!IMPORTANT]
> **Truth posture.** Indicators PROPOSED; instances PROPOSED; lane PROPOSED (OPEN-DASH-01); implementation NEEDS VERIFICATION.

> [!CAUTION]
> **Living-person T4 + DNA T4.** Records of living people, DNA evidence at any resolution, and identifiable land-ownership chains touching living owners default to T4. Deceased-person records de-escalate per dossier rules; DNA never de-escalates by age alone.

> [!CAUTION]
> **AI-surface critical band.** Genealogical reasoning is a natural attractor for AI synthesis (relationship inference, surname/locality bridging). Synthetic-claim incidence in this domain must be **zero**; any non-zero count is a defect that pauses publication.

> [!WARNING]
> **Authoring control.** Per OPEN-DASH-08, this spec **requires** sensitivity reviewer **and** AI-surface steward **and** rights-holder representative on the PR. Authoring without all three is a process defect.

---

## 1. Domain scope

- **Atlas chapter:** v1.0 Ch. 16 (People / Genealogy / DNA / Land Ownership).
- **Default sensitivity tier(s):** **T4** for living-person, DNA, and identifiable land-ownership chains touching living owners; **T3** for recently deceased with surviving identifiable kin; **T1–T2** for historical (well past life-of-natural-person thresholds) records.
- **Pipeline shape:** Standard intake → validation → derive → publish, with **sensitive-lane fail-closed gate** before any public-surface emission, **AI-surface gate** on any genealogical-reasoning emission, and **rollback** required on every release.
- **Dossier:** `docs/domains/people-dna-land/` — `I.` sensitivity + sovereignty rules (DNA, GDPR-analog, NAGPRA), `K.` validators (relationship-graph, source-strength, locality bridging), `M.` correction + rollback posture for genealogical defects.

[↑ back to top](#top)

---

## 2. Indicator subset

Emphasis per README §5.1: **Sensitivity-and-rights (living-person T4, DNA T4) · AI-surface-health**.

| Indicator | §24.11 cat. | Domain-scale healthy posture | Receipt / signal source |
|:---|:---|:---|:---|
| **Sensitive-lane fail-closed rate** | 24.11.3 | **100% at the first gate** for any T4 emission (living person, DNA, identifiable owner). | `PolicyDecision` DENY counts |
| RedactionReceipt coverage | 24.11.3 | 100% on every public-safe derivative of T4 records. | `RedactionReceipt` |
| Review-aged-out incidence | 24.11.3 | Sensitive-lane claims past review cadence dispositioned within tolerance; trend tracked. | `ReviewRecord` |
| Rights-change response time | 24.11.3 | Median time from rights-change event (death, court order, takedown) to tier reassignment within stated (short) tolerance. | Source descriptors, `ReviewRecord` |
| Sensitive-content side-channel audit | 24.11.3 | Periodic checks for label / popup / map-marker / AI-text leakage of living-person identifiers. | Audit logs, `RepresentationReceipt` |
| **AIReceipt presence rate** | 24.11.4 | **100%** on every genealogical-reasoning or land-chain-inference emission. | `AIReceipt` |
| **ABSTAIN rate by template** | 24.11.4 | Tracked per template (relationship inference, locality bridging, surname disambiguation); no template silently drops abstain. | `AIReceipt`, prompt registry |
| **DENY reason distribution** | 24.11.4 | Genealogical DENYs surface source-strength / contradiction / privacy reasons; trend tracked. | `PolicyDecision` |
| **Synthetic-claim incidence** | 24.11.4 | **Zero.** Any non-zero count pauses publication and triggers incident review. | `AIReceipt`, audit logs |
| Cite-or-abstain compliance | 24.11.1 / 24.11.4 | 100% on every AI-derived genealogical or land-ownership claim. | `AIReceipt` |
| EvidenceRef resolution rate | 24.11.1 | > 99.9% across vital records / census / probate / DNA-source cites; per-source rate visible. | `ValidationReport`, EvidenceBundle index |

[↑ back to top](#top)

---

## 3. Domain-specific indicators (PROPOSED)

| PROPOSED indicator | Why this-domain-specific | Candidate §24.11 home |
|:---|:---|:---|
| Source-strength distribution | Distribution of cited source-strengths (primary / secondary / tertiary) per genealogical claim; surfaces lineage built on weak chains. | §24.11.1 |
| Living-person screen-out rate | % of intake records that screen out living-person at admission vs. later in the pipeline. | §24.11.3 |
| DNA-evidence handling chain completeness | % of DNA-based claims with a resolvable handling-chain back to the source repository's release. | §24.11.1 + §24.11.3 |
| Genealogical contradiction surfacing | Cases of contradicting evidence that produce DENY/ABSTAIN rather than silent merge. | §24.11.4 |
| Land-chain identifiable-owner gate compliance | % of land-chain claims that hit the identifiable-owner gate before emission. | §24.11.3 |

[↑ back to top](#top)

---

## 4. Ownership

- **Domain steward:** OWNER_TBD (people-dna-land dossier owner).
- **Governance-health steward:** OWNER_TBD (**sensitivity reviewer** + **AI-surface steward** + **rights-holder representative**; all three required).
- **Implementation owner:** OWNER_TBD (`apps/review-console/` team).

[↑ back to top](#top)

---

## 5. Implementation pointer

- **Dashboard app:** `apps/review-console/` (PROPOSED) — `UNKNOWN` until verified.
- **Telemetry:** `runtime/observability/sensitivity/`, `runtime/observability/ai-surface/` (PROPOSED) — `UNKNOWN`.
- **Schemas read:** `schemas/contracts/v1/sensitivity/`, `schemas/contracts/v1/redaction/`, `schemas/contracts/v1/review/`, `schemas/contracts/v1/ai-receipt/`, `schemas/contracts/v1/correction/`.
- **Policy bundles emitting signals:** `policy/sensitivity/living-person/`, `policy/sensitivity/dna/`, `policy/ai-surface/`, `policy/sources/`, `policy/correction/`.

[↑ back to top](#top)

---

## 6. Review cadence

- **Trigger events:** rights-change event (death notification, court order, takedown request); DNA-source repository policy change; people-dna-land dossier edition; any synthetic-claim incident.
- **Default cadence:** quarterly; **immediate** review on any synthetic-claim count, side-channel audit failure, or rights-change response-time miss.

[↑ back to top](#top)

---

## 7. Open questions

- [ ] **OPEN-DASH-PDL-01** — Define rights-change response-time tolerance per event class (death vs court order vs takedown).
- [ ] **OPEN-DASH-PDL-02** — Confirm source-strength taxonomy alignment between this spec and the genealogy dossier `K.` validators.
- [ ] **OPEN-DASH-PDL-03** — Define the "pause publication" trigger for synthetic-claim incidents (single count? rate?).
- [ ] **OPEN-DASH-PDL-04** — Confirm three-reviewer authoring gate per OPEN-DASH-08.
- [ ] **OPEN-DASH-PDL-05** — Reconcile DNA-evidence handling-chain indicator with any cross-domain biometric data policy (if surfaced separately).

[↑ back to top](#top)

---

## 8. Evidence basis & citations

<details>
<summary><strong>Source ledger</strong></summary>

| Source | Status | Supports | Limits |
|:---|:---|:---|:---|
| Atlas v1.1 §24.11.3 / §24.11.4 / §24.11.1 | CONFIRMED (manuscript) | §2 indicator subset; T4 + AI-surface emphasis. | Indicators PROPOSED at source. |
| Atlas v1.0 Ch. 16 (People / Genealogy / DNA / Land Ownership dossier) | CONFIRMED (manuscript) | §1 scope, T4-default; §3 candidates. | Mounted dossier presence NEEDS VERIFICATION. |
| Atlas v1.1 §24.5 / §24.7 / §24.10 | CONFIRMED authored sibling | T4 default (living person, DNA); reviewer role matrix; threat model. | All PROPOSED. |
| `docs/dashboards/domain/README.md` §5.1, §6 | CONFIRMED | Emphasis (Sensitivity-and-rights, living-person T4, DNA T4 · AI-surface-health); template. | Lane PROPOSED (OPEN-DASH-01). |
| `docs/dashboards/governance/SENSITIVITY_RIGHTS.md`, `…/AI_SURFACE_HEALTH.md` | CONFIRMED (this folder) | Cross-references for master indicator catalogs; this spec does not redefine them. | Master specs PROPOSED. |

</details>

[↑ back to top](#top)

---

<sub>Per-domain people / genealogy / DNA / land ownership dashboard specification. **Specification only — implementations live in `apps/`; indicator definitions live in Atlas §24.11; domain context lives in `docs/domains/people-dna-land/`.** Living-person T4 + DNA T4 + AI-surface critical band: the dashboard reports posture, the gate enforces, the receipts back the trust, and synthetic-claim incidence must be zero.</sub>
