<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<TODO-uuid>
title: Fauna — Expansion Plan
type: standard
version: v1
status: draft
owners: <TODO: fauna-domain-steward, security-and-privacy-reviewer, release-manager>
created: 2026-05-16
updated: 2026-05-16
policy_label: public
related:
  - docs/domains/fauna/README.md
  - docs/domains/habitat/README.md
  - docs/domains/flora/README.md
  - docs/domains/spatial-foundation/README.md
  - docs/doctrine/evidence-first.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/policy-aware.md
  - docs/doctrine/map-first.md
  - docs/doctrine/ai-as-assistant.md
  - docs/doctrine/corrections-first-class.md
  - docs/architecture/data-classification-framework.md
  - docs/architecture/sensitive-domain-fail-closed.md
tags: [kfm, domain, fauna, expansion, roadmap, tier-3, deny-by-default, sensitive-species]
notes:
  - Fauna is a Tier 3 (deny-by-default) lane; this plan is the operational roadmap that phases its expansion to public surfaces.
  - The Fauna README is the field spec (purpose, owned terms, sources, validators); this plan is the build sequence and gating logic.
  - Phase identifiers F0–F4 are local to Fauna and nest beneath the project-wide L0/L1/L2 conformance levels.
  - All repository-path, schema, fixture-name, owner, and CI-target claims are PROPOSED until verified in the mounted repository.
[/KFM_META_BLOCK_V2] -->

# Fauna — Expansion Plan

> The phased rollout plan for the Fauna domain — from deny-by-default fixtures, through a generalized public surface, to broad multi-source coverage — written so the build order honors KFM's sensitive-domain doctrine.

![status](https://img.shields.io/badge/status-draft-yellow) ![lane-tier](https://img.shields.io/badge/lane%20tier-3%20%E2%80%94%20deny%20by%20default-8b1c1c) ![conformance](https://img.shields.io/badge/conformance%20target-L1%20via%20F3-blue) ![policy](https://img.shields.io/badge/policy%20label-public-2ea44f) ![evidence](https://img.shields.io/badge/evidence-CONFIRMED%20%2B%20PROPOSED-lightgrey) ![last-updated](https://img.shields.io/badge/last%20updated-2026--05--16-informational)

> [!IMPORTANT]
> Fauna is a **Tier 3 deny-by-default** lane. `[CONFIRMED from the Lane Sensitivity Tier table.]` This plan does **not** authorize live Fauna activation; it sequences the *evidence, fixtures, validators, redaction receipts, and steward agreements that must be in place* before activation may be approved. **No phase below grants release authority by itself** — release authority remains with the human roles and decisions described in [`docs/doctrine/lifecycle-law.md`](../../doctrine/lifecycle-law.md). `[PROPOSED path.]`

---

**Status:** draft · **Owners:** `<TODO — fauna-domain-steward, security-and-privacy-reviewer, release-manager>` · **Last updated:** 2026-05-16

## Quick jump

- [1. Purpose and scope](#1-purpose-and-scope)
- [2. Where this plan sits in KFM](#2-where-this-plan-sits-in-kfm)
- [3. What Fauna owns — and what it does not](#3-what-fauna-owns--and-what-it-does-not)
- [4. The expansion path at a glance](#4-the-expansion-path-at-a-glance)
- [5. Phase ladder F0 → F4](#5-phase-ladder-f0--f4)
- [6. Phase F0 — Membrane, fixtures, validators](#6-phase-f0--membrane-fixtures-validators)
- [7. Phase F1 — Public-safe proof slice (range only, no occurrences)](#7-phase-f1--public-safe-proof-slice-range-only-no-occurrences)
- [8. Phase F2 — Steward-restricted live activation](#8-phase-f2--steward-restricted-live-activation)
- [9. Phase F3 — Generalized public occurrences](#9-phase-f3--generalized-public-occurrences)
- [10. Phase F4 — Broad coverage and federation](#10-phase-f4--broad-coverage-and-federation)
- [11. Source admission roadmap](#11-source-admission-roadmap)
- [12. Validator readiness per phase](#12-validator-readiness-per-phase)
- [13. Sensitivity gate posture per phase](#13-sensitivity-gate-posture-per-phase)
- [14. Cross-lane dependencies that gate expansion](#14-cross-lane-dependencies-that-gate-expansion)
- [15. AI posture per phase](#15-ai-posture-per-phase)
- [16. Risk register](#16-risk-register)
- [17. Verification backlog](#17-verification-backlog)
- [18. Anti-patterns to reject](#18-anti-patterns-to-reject)
- [19. Acceptance checklist per phase](#19-acceptance-checklist-per-phase)
- [20. Related docs](#20-related-docs)
- [21. Glossary and abbreviations (appendix)](#21-glossary-and-abbreviations-appendix)

---

## 1. Purpose and scope

This document is the **operational expansion plan** for the Fauna domain. It answers the question *"how does Fauna move from doctrine-only to a governed, public-safe surface without violating the sensitive-domain posture?"* It is intentionally narrow:

- **In scope.** Phase sequencing for Fauna; per-phase gates, fixtures, validators, source admissions, sensitivity posture, AI posture, and acceptance criteria; the cross-lane preconditions Fauna inherits from Spatial Foundation, Habitat, Flora, and the trust membrane; the risks and unknowns Fauna carries.
- **Out of scope.** Per-source ingestion code, per-validator schema layouts, per-tile cartography, per-API endpoint shapes, per-fixture file contents. Those are owned by the [`docs/domains/fauna/README.md`](./README.md) field spec, the contracts under `schemas/contracts/v1/domains/fauna/` `[PROPOSED path]`, and the per-source descriptors under `sources/fauna/` `[PROPOSED path]`.

> [!NOTE]
> This plan describes *what the system must prove before each phase advances.* It does **not** assert that any phase is currently implemented. Every "current state" claim is labeled.

[⬆ Back to top](#fauna--expansion-plan)

---

## 2. Where this plan sits in KFM

Fauna's expansion does not happen in isolation. The build order and the sensitivity posture are inherited from project-wide doctrine.

### 2.1 Tier and build order

Fauna sits in the most sensitive build tier alongside archaeology, genealogy, infrastructure, land-records, and public-safety. `[CONFIRMED from the Lane Sensitivity Tier table.]`

| Tier | Lanes | Build rule |
|---|---|---|
| **Tier 1 — public-safe first** | hydrology, soils, atmosphere, agriculture, settlements, boundaries, imagery, elevation | Build proof slice here first. `[CONFIRMED.]` |
| **Tier 2 — mixed sensitivity** | ecology, habitat, flora, geology, history, hazards, roads-rail-trade-routes | Build after Tier 1 is stable. `[CONFIRMED.]` |
| **Tier 3 — deny-by-default** | **fauna (rare/protected)**, archaeology, genealogy, infrastructure, land-records, public-safety | Build last, only after Tier-2 covariate lanes and domain-specific controls are proven. `[CONFIRMED.]` |

> [!WARNING]
> **Fauna does not begin live activation before Spatial Foundation, Habitat, and the trust membrane have reached L1.** `[CONFIRMED build-order rule from the greenfield Build Strategy.]` Generalization receipts, Redaction Receipts, sensitivity inheritance, and habitat covariates are all upstream of any Fauna release.

### 2.2 Conformance levels (project-wide) and phases (Fauna-local)

KFM defines three project-wide conformance levels (L0 / L1 / L2). `[CONFIRMED vocabulary; per-doc implementation PROPOSED.]` This plan adds five **Fauna-local phases** that nest within those levels, so the lane's expansion is sequenced honestly inside the wider system.

| KFM level | Fauna phase that reaches it | What the Fauna lane proves at that level |
|---|---|---|
| **L0 — Fixture-level** | **F0** | Doctrine + fixtures + validators + zero public traffic. |
| **L1 — Provable trust (public-safe proof lane)** | **F1 → F3** | F1 = range-only public; F2 = steward-only live; F3 = generalized public occurrences. |
| **L2 — Federated + attested** | **F4** | Multi-source coverage, attested releases, federated correction notices. |

The Fauna phase identifiers `F0…F4` are **local to this plan** and do not redefine the project's L0/L1/L2 vocabulary.

### 2.3 Doctrine documents Fauna inherits from

| Doctrine | What Fauna inherits | Path |
|---|---|---|
| Evidence-first | `EvidenceBundle` / `EvidenceRef` closure for every occurrence claim. | [`docs/doctrine/evidence-first.md`](../../doctrine/evidence-first.md) `[PROPOSED path]` |
| Lifecycle law | `RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED` is non-negotiable. | [`docs/doctrine/lifecycle-law.md`](../../doctrine/lifecycle-law.md) `[PROPOSED path]` |
| Policy-aware | Six-dimension policy gate; sensitivity ladder C0–C5; reason codes are finite. | [`docs/doctrine/policy-aware.md`](../../doctrine/policy-aware.md) `[PROPOSED path]` |
| Map-first | Public map surfaces consume only `DecisionEnvelope` payloads; sensitive geometry denied at the layer. | [`docs/doctrine/map-first.md`](../../doctrine/map-first.md) `[PROPOSED path]` |
| AI as assistant | AI may summarize, never authorize; ABSTAIN on sensitivity uncertainty. | [`docs/doctrine/ai-as-assistant.md`](../../doctrine/ai-as-assistant.md) `[PROPOSED path]` |
| Corrections first-class | Sensitivity reclassification and source-rights changes propagate through `CorrectionNotice`. | [`docs/doctrine/corrections-first-class.md`](../../doctrine/corrections-first-class.md) `[PROPOSED path]` |

[⬆ Back to top](#fauna--expansion-plan)

---

## 3. What Fauna owns — and what it does not

The expansion plan only sequences what Fauna **owns**. Boundary leakage is the most common Tier-3 failure mode, so the boundary is restated up front.

### 3.1 Owned by Fauna

`[CONFIRMED from the Domains Culmination Atlas entry for Fauna.]`

| Object | One-line role |
|---|---|
| `Taxon` | Canonical species record with name authority + global ID (ITIS TSN / GBIF key / equivalent). |
| `Taxon Crosswalk` | Registered authority-to-authority mapping; the **only** object that may assert name equivalence. |
| `Conservation Status` | Framework-qualified status (IUCN / USFWS ESA / state list / NatureServe G/S rank) with effective date. |
| `Occurrence Evidence` | Raw occurrence object; never published directly if sensitive. |
| `Occurrence Restricted` | Exact-location occurrence retained internally; deny-by-default at public surfaces. |
| `Occurrence Public` | Generalized public-safe derivative; carries a `Redaction Receipt`. |
| `RangePolygon` | Range distribution polygon with authoring lineage. |
| `SeasonalRange` | Season-qualified range; never collapsed across seasons. |
| `MigrationRoute` | Movement corridor; stopover detail may be restricted. |
| `SensitiveSite` | Nest / den / roost / hibernaculum / spawning / concentration location; deny-by-default. |
| `MortalityObservation` | Mortality event with cause qualifier; never aggregated into status. |
| `DiseaseObservation` | Wildlife disease detection (CWD, HPAI, white-nose, etc.); **never** a public-health alert. |

### 3.2 Not owned by Fauna

`[CONFIRMED — explicit non-ownership from the Domains Culmination Atlas.]`

| Not-owned by Fauna | Owned by | Why this matters to the plan |
|---|---|---|
| Habitat classification and quality | Habitat | Fauna consumes habitat as a covariate; does not author it. |
| Plant taxa and occurrences | Flora | Crosswalks across kingdoms are explicitly forbidden. |
| Hunt regulations / harvest quotas | State wildlife agencies | KFM is not a regulatory authority. |
| Disease outbreaks framed for human public health | Public-health authorities | A `DiseaseObservation` is a wildlife observation, not a public-health alert. |

> [!CAUTION]
> A common drift mode: framing a wildlife-disease cluster ("CWD positives in unit X", "HPAI detections at site Y") as a *public-health communication.* This is a **`DENY` at the policy gate** — Fauna's `DiseaseObservation` is *observation*, not *alert*. `[CONFIRMED rule.]` The expansion plan must not breach this even informally in marketing or release notes.

[⬆ Back to top](#fauna--expansion-plan)

---

## 4. The expansion path at a glance

```mermaid
flowchart LR
    classDef gov   fill:#ECECEC,stroke:#444,color:#1a1a1a;
    classDef pub   fill:#D9EAD3,stroke:#3B7A57,color:#1B3A24;
    classDef mid   fill:#FFF4D6,stroke:#A88419,color:#3A2C00;
    classDef deny  fill:#F2D7D7,stroke:#A33,color:#5A0A0A;
    classDef stew  fill:#E3EBF4,stroke:#406090,color:#1A2A40;

    M[Trust membrane<br/>+ Spatial Foundation L1<br/>+ Habitat L1]:::gov

    F0["F0 — Membrane &amp; fixtures<br/>(no live traffic)"]:::gov
    F1["F1 — Public-safe<br/>range + status only<br/>(no occurrences)"]:::pub
    F2["F2 — Steward-restricted<br/>live activation<br/>(C1 surface)"]:::stew
    F3["F3 — Generalized<br/>public occurrences<br/>(via Redaction Receipt)"]:::mid
    F4["F4 — Broad coverage<br/>federated + attested"]:::pub

    SENS["Sensitive taxa &amp; sites<br/>remain DENY-by-default<br/>at every public phase"]:::deny

    M --> F0 --> F1 --> F2 --> F3 --> F4
    SENS -. enforces .-> F1
    SENS -. enforces .-> F3
    SENS -. enforces .-> F4
```

> The Fauna lane never collapses into a single "go-live" event. Each arrow above is gated by named acceptance criteria (§19) and a `ReviewRecord` from a steward role distinct from the engineer who built the phase. `[PROPOSED implementation; vocabulary CONFIRMED.]`

[⬆ Back to top](#fauna--expansion-plan)

---

## 5. Phase ladder F0 → F4

| Phase | One-line outcome | What is allowed to flow | KFM level reached |
|---|---|---|---|
| **F0** | Fauna doctrine + fixtures + validators + zero public traffic. | Synthetic fixtures only. No connectors. | **L0** |
| **F1** | Range polygons and conservation status reach the public surface; **no occurrence data, generalized or otherwise**. | `RangePolygon`, `SeasonalRange`, `Conservation Status`. | **L1 — partial** |
| **F2** | Steward-only live activation: occurrences ingested live, retained internally, never public. | `Occurrence Restricted` to steward console only (`C1`). | **L1 — partial** |
| **F3** | Generalized public occurrences (non-sensitive taxa only) reach the public surface via `Redaction Receipt` and `Generalization Transform` receipt. | `Occurrence Public` for non-sensitive taxa; sensitive taxa remain in F2 posture. | **L1 — full** |
| **F4** | Multi-source coverage, attested releases, federated `CorrectionNotice` feed for downstream wildlife republishers. | All Fauna objects under per-source rights; sensitive taxa still `C4`. | **L2** |

> [!TIP]
> A public communication that claims "Fauna is live" is meaningful only when paired with a phase identifier. *"Fauna is at **F1**"* and *"Fauna is at **F3**"* describe very different public surfaces. The vocabulary above is the only correct shorthand.

[⬆ Back to top](#fauna--expansion-plan)

---

## 6. Phase F0 — Membrane, fixtures, validators

**Outcome.** The Fauna lane exists in the repository as doctrine + contracts + fixtures + validators with **no live connectors, no public route, and no real occurrence data.**

### 6.1 What F0 produces

| Artifact | Where it lives | Status |
|---|---|---|
| Fauna README (field spec) | `docs/domains/fauna/README.md` `[PROPOSED path]` | NEEDS VERIFICATION |
| This expansion plan | `docs/domains/fauna/EXPANSION_PLAN.md` | draft (this doc) |
| Contracts for owned objects | `schemas/contracts/v1/domains/fauna/` `[PROPOSED path]` | PROPOSED |
| Fixture set | `fixtures/fauna/` `[PROPOSED path]` | PROPOSED |
| Validator set (five tests) | `tools/validators/fauna/` or equivalent `[PROPOSED path]` | PROPOSED |
| Source descriptors (no-network) | `sources/fauna/<source-id>/descriptor.yaml` `[PROPOSED path]` | PROPOSED |
| Policy rules for Fauna | `policy/domains/fauna/*.rego` `[PROPOSED path]` | PROPOSED |

### 6.2 The five F0 validators

`[CONFIRMED validator names and acceptance criteria from the Domains Culmination Atlas.]`

| # | Validator | Subject | Acceptance | Failure |
|---|---|---|---|---|
| 1 | Sensitive-taxon redaction test | candidate published occurrence row | row tied to a sensitive taxon resolves to generalized geometry + Redaction Receipt | `DENY fauna.sensitive.exact_geom` |
| 2 | Taxon crosswalk closure test | `Taxon` + `Taxon Crosswalk` rows | every `Taxon` resolves under at least one supported authority and has a registered crosswalk where required | `DENY fauna.taxon.unresolved` |
| 3 | Conservation status framework anti-collapse test | `Conservation Status` rows | framework is stated; not collapsed across IUCN / USFWS / state | `DENY fauna.status.framework_collapse` |
| 4 | Sensitive-site denial test | `SensitiveSite` rows | no public surface returns `SensitiveSite` geometry | `DENY fauna.sensitive_site.exposed` |
| 5 | Citizen-science observer privacy test | occurrence rows from citizen-science sources | observer identifiers pseudonymized in public surfaces | `DENY fauna.observer.identifiable` |

> [!NOTE]
> Each validator must ship with **at least one positive fixture and one negative fixture** before F0 is considered complete. `[CONFIRMED policy-doctrine rule for L0 conformance.]` "The validator exists" is not the bar; *"the validator denies a real failure case in CI"* is.

### 6.3 What F0 does **not** authorize

- No connectors run against live endpoints.
- No `SourceRightsAssessment` is converted into a `SourceActivationDecision`.
- No public route reads from a Fauna fixture path.
- No AI Focus Mode answers a Fauna question against fixture data.

[⬆ Back to top](#fauna--expansion-plan)

---

## 7. Phase F1 — Public-safe proof slice (range only, no occurrences)

**Outcome.** The public map surface displays Fauna *range and status* — no occurrence points, no migration stopovers, no sensitive sites. This is the first phase that emits real public-facing Fauna content, and it deliberately avoids the most sensitive object families.

### 7.1 What flows in F1

| Object | Public-route disposition | Notes |
|---|---|---|
| `Taxon` | `ANSWER` via `/api/v1/fauna/taxon/{id}` `[PROPOSED route]` | Authority + global ID resolution only. |
| `Taxon Crosswalk` | `ANSWER` for non-sensitive taxa | Authority-to-authority mapping is metadata, not occurrence. |
| `Conservation Status` | `ANSWER` per registered framework | Framework named; no framework collapse permitted. |
| `RangePolygon` | `ANSWER` for non-sensitive taxa | Carries authoring lineage. |
| `SeasonalRange` | `ANSWER` for non-sensitive taxa | Never collapsed across seasons. |
| `MigrationRoute` | `ANSWER` with sensitive stopovers withheld | Withholding carries a `Redaction Receipt`. |
| `Occurrence *` | **not admitted to public route** | F1 does not publish occurrences. |
| `SensitiveSite` | **not admitted to public route** | Continues to `DENY policy.sensitive_geometry`. |
| `MortalityObservation` | **not admitted to public route** | Held for F3+ review. |
| `DiseaseObservation` | **not admitted to public route** | Held for F3+ review with explicit framing guardrails. |

### 7.2 What must be true upstream

`[CONFIRMED build-order rules.]`

- **Spatial Foundation at L1.** Generalization Transform receipts and Coordinate Reference Profiles are live for the Fauna geometry classes used in F1.
- **Habitat at L1.** Habitat covariates referenced by `SeasonalRange` and `RangePolygon` are released.
- **Policy gate at L1.** All six policy dimensions pass for at least one Fauna fixture path.
- **Map-first at L1.** The Evidence Drawer renders a Fauna feature click with `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` / `STALE` reachable. `[CONFIRMED finite outcomes vocabulary.]`

### 7.3 What F1 does **not** authorize

- No occurrence data — restricted or generalized — at any public route.
- No live citizen-science observer attribution at any public route.
- No model-derived range polygon without a `Model Run Receipt`. `[CONFIRMED requirement from the Habitat domain spec, inherited.]`

[⬆ Back to top](#fauna--expansion-plan)

---

## 8. Phase F2 — Steward-restricted live activation

**Outcome.** Live connectors begin ingesting occurrence data into `Occurrence Restricted`. The data is visible **only** to authenticated stewards on the `C1` surface (`/steward/v1/*` `[PROPOSED route]`). Nothing reaches the public surface that did not already reach it in F1.

### 8.1 Connectors that may activate at F2

`[CONFIRMED source roster from the Domains Culmination Atlas; activation order PROPOSED.]`

| Source | Role | Rights posture | F2 admission |
|---|---|---|---|
| GBIF / iDigBio | observation / aggregate | open; per-record license matters | yes, with per-record license honored |
| eBird | observation | Cornell Lab terms | yes, with observer pseudonymization |
| USFWS IPaC / ECOS | authority (regulatory) | public; vintaged | yes (already public, kept for completeness) |
| USGS NAS (Nonindigenous Aquatic Species) | observation | public | yes |
| Specimen records (museum / herbarium) | observation (authority) | per-institution | yes, on per-institution agreement |
| State Wildlife Agency datasets | observation / context | varies; rights `NEEDS VERIFICATION` per source | only after rights review |
| State Natural Heritage Programs | authority (restricted) | restricted; per-state agreement | **deferred to F3+** under written agreement |

> [!WARNING]
> Live connectors are **not** activated until rights, sensitivity, activation, retry/failure, and monitoring are all in place for the specific source. `[CONFIRMED build-order rule from policy-aware doctrine.]` "We have the API key" is not the bar; the `SourceRightsAssessment` and `SourceActivationDecision` are.

### 8.2 What F2 produces internally

- `Occurrence Restricted` rows for non-sensitive and sensitive taxa alike — but **gated to the steward surface**.
- A `ReleaseManifest` is **not** required for F2 internal ingestion, because nothing is being *released* — but `IntakeReceipt`, `TransformReceipt`, and `ValidationReport` artifacts are still mandatory. `[CONFIRMED lifecycle-law shape.]`
- Steward-console UI showing `Occurrence Restricted` with a clear C1 badge and policy posture in the Evidence Drawer. `[CONFIRMED drawer rule — exact coordinates of sensitive features do not enter the public response payload.]`

### 8.3 What F2 does **not** authorize

- No public route reads `Occurrence Restricted` under any circumstance.
- No AI Focus Mode summarizes occurrence data — sensitive or otherwise — on the public surface. AI may operate against `RangePolygon` / `Conservation Status` only.

[⬆ Back to top](#fauna--expansion-plan)

---

## 9. Phase F3 — Generalized public occurrences

**Outcome.** Non-sensitive taxa get an `Occurrence Public` derivative on the public surface — geometry obscured per a `Generalization Transform` receipt, redactions recorded per a `Redaction Receipt`. Sensitive taxa remain in the F2 posture (steward-only).

### 9.1 The F3 promotion pipeline

```mermaid
flowchart LR
    classDef raw  fill:#eef7ff,stroke:#1f6feb,color:#0b3d91;
    classDef der  fill:#fff5e6,stroke:#bf8700,color:#5a3e00;
    classDef pol  fill:#f4ecf7,stroke:#6a3d9a,color:#2a1a40;
    classDef pub  fill:#D9EAD3,stroke:#3B7A57,color:#1B3A24;
    classDef deny fill:#F2D7D7,stroke:#A33,color:#5A0A0A;

    src["Connector capture"]:::raw
    raw["RAW capture"]:::raw
    work["WORK / QUARANTINE"]:::der
    occ_r["Occurrence Restricted<br/>(internal only)"]:::der
    gate["Sensitivity gate<br/>+ Redaction Receipt<br/>+ Generalization Transform"]:::pol
    occ_p["Occurrence Public<br/>(generalized)"]:::pub
    sens["Sensitive taxa<br/>→ public publication DENIED"]:::deny

    src --> raw --> work --> occ_r --> gate
    gate -->|non-sensitive taxon| occ_p
    gate -->|sensitive taxon| sens
```

> The diagram is illustrative; canonical pipeline stage names are `RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED`. `[CONFIRMED lifecycle-stage vocabulary.]`

### 9.2 What is required before F3 can begin

| Precondition | Why it is required |
|---|---|
| Sensitive-taxon registry exists and aligns with Natural Heritage Program agreements. | F3 publishes *non*-sensitive occurrences; the registry is what distinguishes them. `[CONFIRMED verification item.]` |
| `Redaction Receipt` schema accepted and produced end-to-end. | Every generalized occurrence carries one. `[CONFIRMED verification item.]` |
| `Generalization Transform` receipt schema accepted; transforms reproducible. | Inherited from Spatial Foundation. `[CONFIRMED inherited rule.]` |
| `Taxon Crosswalk` completeness across primary authorities documented. | A taxon whose authority cannot be resolved cannot be published. `[CONFIRMED verification item.]` |
| Citizen-science observer-privacy pipeline verified. | Pseudonymization is a public-surface invariant. `[CONFIRMED validator scope.]` |

### 9.3 What F3 still does **not** authorize

- Exact occurrence geometry on any public surface — even for "abundant" species — unless a specific source's `SourceRightsAssessment` allows it *and* sensitivity gate clears. `[CONFIRMED policy posture.]`
- Publication of `SensitiveSite`, `MigrationRoute` stopover detail, or `MortalityObservation` aggregated into a status-like assertion.
- Public-health framing of `DiseaseObservation`. `[CONFIRMED — wildlife-disease detection is not a public-health alert.]`

[⬆ Back to top](#fauna--expansion-plan)

---

## 10. Phase F4 — Broad coverage and federation

**Outcome.** Fauna reaches **L2** for the parts of the lane that have been individually proven through F1–F3. This is the federation phase: multi-source coverage with cryptographic attestation on `ProofPack`, machine-readable `CorrectionNotice` feeds, and multi-party approval on release-significant Fauna changes.

### 10.1 What L2 adds for Fauna specifically

`[CONFIRMED vocabulary; per-lane implementation PROPOSED.]`

| L2 capability (project-wide) | Fauna-specific implication |
|---|---|
| Signed `ProofPack` attestations | Downstream wildlife republishers can verify a Fauna release was reviewed and not silently altered. |
| Machine-readable `CorrectionNotice` feed | Sensitivity reclassification of a taxon (e.g., listing change, agreement change) propagates to downstream consumers without manual re-fetching. |
| Multi-party approval on release-significant actions | Adding a new sensitive-taxa source, or changing the redaction transform, requires two distinct human roles to sign. |
| Reproducible builds at byte level | A re-built Fauna release at a given version is bit-identical to the original. |

### 10.2 What F4 still does **not** change

- The sensitivity ladder. `C4` remains `C4`; federation does not lower its posture.
- Cross-kingdom equivalence. A Fauna `Taxon` and a Flora `Plant Taxon` are never reconciled by a shared crosswalk. `[CONFIRMED ownership boundary.]`
- The disease-observation framing rule. Federation does not turn `DiseaseObservation` into a public-health alert under any circumstance. `[CONFIRMED.]`

[⬆ Back to top](#fauna--expansion-plan)

---

## 11. Source admission roadmap

Source admission is the most common path by which a sensitive-domain expansion drifts. The plan below is **deliberately conservative** — each source is admitted only at the earliest phase whose posture matches its rights and sensitivity profile.

| Source | Role | Earliest admission | Rationale | Status |
|---|---|---|---|---|
| USFWS IPaC / ECOS | authority (regulatory) | **F0** (fixture) → **F1** (live, public) | Public regulatory authority; ESA listing + critical habitat boundaries. | `CONFIRMED public; vintaged.` |
| USGS NAS | observation | **F0** (fixture) → **F2** (live, internal) → **F3** (generalized public) | Public invasive-aquatic occurrences. | `CONFIRMED public.` |
| GBIF / iDigBio | observation / aggregate | **F2** (live, internal) → **F3** (generalized public per per-record license) | Aggregator; per-record license must be honored. | `CONFIRMED open; per-record license matters.` |
| eBird | observation | **F2** (live, internal) → **F3** (generalized public with observer pseudonymization) | Cornell Lab terms; observer-privacy gate. | `CONFIRMED Cornell Lab terms.` |
| Specimen records (museum / herbarium) | observation (authority) | **F2** (live, internal per institution agreement) → **F3** (generalized public per agreement) | Per-institution rights vary. | `NEEDS VERIFICATION per institution.` |
| State Wildlife Agency datasets | observation / context | **F2 or later**, only with rights review | Surveys, harvest, disease surveillance; rights vary. | `NEEDS VERIFICATION per source.` |
| State Natural Heritage Programs | authority (restricted) | **F2 (steward-only)**; never in public surface beyond what the agreement permits | Element occurrence records, deny-by-default exact location. | `CONFIRMED restricted; per-state agreement.` |

> [!CAUTION]
> The temptation to admit a Natural Heritage Program feed "because it's authoritative" is the canonical Tier-3 failure mode. **Authority does not relax sensitivity.** A more authoritative source for a sensitive taxon is a *higher-care* obligation, not a lower one. `[CONFIRMED doctrine posture.]`

[⬆ Back to top](#fauna--expansion-plan)

---

## 12. Validator readiness per phase

| Validator | F0 | F1 | F2 | F3 | F4 |
|---|:--:|:--:|:--:|:--:|:--:|
| 1. Sensitive-taxon redaction test | ✓ (fixture) | ✓ | ✓ | ✓ + live | ✓ + attested |
| 2. Taxon crosswalk closure test | ✓ (fixture) | ✓ | ✓ | ✓ | ✓ + attested |
| 3. Conservation status framework anti-collapse | ✓ (fixture) | ✓ | ✓ | ✓ | ✓ + attested |
| 4. Sensitive-site denial test | ✓ (fixture) | ✓ | ✓ | ✓ | ✓ + attested |
| 5. Citizen-science observer-privacy test | ✓ (fixture) | n/a | ✓ | ✓ | ✓ + attested |

> "✓ (fixture)" means the validator runs against synthetic data. "✓" means it runs against the live ingested data at that phase. "✓ + attested" means the validator result becomes part of a signed `ProofPack`. `[PROPOSED implementation; vocabulary CONFIRMED.]`

[⬆ Back to top](#fauna--expansion-plan)

---

## 13. Sensitivity gate posture per phase

The sensitivity ladder is project-wide. `[CONFIRMED classification framework — verbatim from the Data Classification Framework.]` This table fixes how each ladder class is handled inside Fauna at each phase.

| Class | F0 | F1 | F2 | F3 | F4 |
|---|---|---|---|---|---|
| **C0 — Public-safe** | fixture | public via API | public via API | public via API | public + attested |
| **C1 — Steward-only** | fixture | n/a | steward console | steward console | steward console + attested |
| **C2 — Admin-only** | fixture | n/a | admin console | admin console | admin console + attested |
| **C3 — Restricted-by-rights** | fixture | per-source review | per-source review | per-source review | per-source review + attested |
| **C4 — Sensitive-deny-default** | fixture | `DENY` at public | `DENY` at public; steward-only with cultural/legal authorization | `DENY` at public exact; generalized derivative may be admissible | unchanged at L2 |
| **C5 — Forbidden-from-storage** | n/a | n/a | n/a | n/a | n/a — connectors MUST drop these fields |

> [!IMPORTANT]
> The doctrine answer to *"may we publish a generalized version of a `C4` sensitive-taxon occurrence?"* is **only with**: (a) `Redaction Receipt`, (b) `Generalization Transform` receipt, (c) `ReviewRecord` by a steward role with explicit cultural / legal authorization, and (d) the underlying `SourceRightsAssessment` permitting that generalization. All four. The absence of any one is a `DENY`. `[CONFIRMED rule structure.]`

[⬆ Back to top](#fauna--expansion-plan)

---

## 14. Cross-lane dependencies that gate expansion

Fauna is a **downstream consumer** in the lane dependency graph. The lanes below must reach the indicated level before Fauna may advance to the corresponding phase.

| Upstream lane | Must reach | Before Fauna may reach | Why |
|---|---|---|---|
| Spatial Foundation | L1 — CRS, GeographyVersion, Generalization Transform receipts live | **F1** | All Fauna geometry transformations cite Spatial Foundation receipts. `[CONFIRMED cross-lane edge.]` |
| Habitat | L1 — habitat covariates released; Habitat sensitivity inheritance wired | **F1** | `RangePolygon` and `SeasonalRange` consume habitat covariates; sensitivity propagation must flow correctly. `[CONFIRMED cross-lane edge.]` |
| Trust membrane (policy gate, evidence resolver, finite outcomes) | L1 | **F1** | The Evidence Drawer must round-trip a Fauna feature click with `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` / `STALE` reachable. `[CONFIRMED.]` |
| Hazards | L0 fixture-level + framing guardrails | **F2 (for `DiseaseObservation` capture)** | Wildlife disease ingestion is allowed only when the public-health framing guardrail is provably enforced. `[CONFIRMED rule.]` |
| Atmosphere / Air | L1 — weather covariates released | **F2 (for migration/phenology context)** | Covariate use never re-authors weather observations. `[CONFIRMED rule.]` |
| People / DNA / Land | privacy gate proven for observer-attribution | **F2 (for citizen-science live)** | Observer identity is a separate privacy concern from occurrence privacy. `[CONFIRMED rule.]` |

[⬆ Back to top](#fauna--expansion-plan)

---

## 15. AI posture per phase

`[CONFIRMED — AI rules from the Fauna domain spec.]` AI is an assistant, not an authority. The phase-by-phase posture below is **a tightening**, not a permission ladder: AI may do *less* against Fauna than against Tier-1 lanes, even at L2.

| Phase | What AI MAY do | What AI MUST ABSTAIN on | What AI MUST DENY |
|---|---|---|---|
| **F0** | Nothing against real data. May summarize *fixtures* for internal review. | Anything that crosses the trust membrane. | Anything that would imply a Fauna claim against live data. |
| **F1** | Summarize public `RangePolygon` / `SeasonalRange` / `Conservation Status`. Explain framework semantics. | Where the taxon's sensitivity is uncertain or its crosswalk unresolved. | Any request that would resolve exact sensitive-site geometry. |
| **F2** | Nothing additional on the public surface (steward console out of scope here). | Same as F1 on the public surface. | Same as F1 on the public surface. |
| **F3** | F1 capabilities + describing generalized `Occurrence Public` distributions. | Where the rare-taxon flag or sensitivity is unresolved. | Exact occurrence geometry; any request that would resolve a sensitive-site via habitat proxy. |
| **F4** | F3 capabilities + describing source-coverage and correction history. | Same as F3, plus where attestation is missing or stale. | Same as F3. |

> [!IMPORTANT]
> AI must **never emit a `PolicyDecision`, `ReviewRecord`, or `SensitivityAssessment` for Fauna.** Those are human-role outputs. `[CONFIRMED — AI-as-assistant doctrine.]`

[⬆ Back to top](#fauna--expansion-plan)

---

## 16. Risk register

| ID | Risk | Likelihood | Impact | Mitigation | Status |
|---|---|---|---|---|---|
| FAU-R-01 | A Natural Heritage Program feed is admitted with exact geometry before agreement is in writing. | medium | severe (legal + ethical) | F2 admission gate requires written per-state agreement; CI fails if agreement record is missing. | PROPOSED mitigation |
| FAU-R-02 | A `DiseaseObservation` is framed in a public release note as a "public-health alert." | medium | severe (regulatory + trust) | Release-note linting rejects public-health framing on Fauna lane; `ReviewRecord` required. | PROPOSED mitigation |
| FAU-R-03 | A citizen-science observer is identifiable via an occurrence published at F3. | medium | high (privacy) | Validator 5 + cross-lane review with People / DNA / Land at F2. | CONFIRMED validator exists; coverage NEEDS VERIFICATION |
| FAU-R-04 | A sensitive taxon's exact occurrence leaks via *habitat proxy* — a habitat polygon so narrow it implies the location. | medium | severe | Sensitive-species inheritance test on Habitat (cross-lane). AI must DENY habitat-proxy resolution. | CONFIRMED rule; CI coverage NEEDS VERIFICATION |
| FAU-R-05 | A `Taxon Crosswalk` collision (two authorities asserting equivalent names that the project treats as distinct). | low | moderate (data quality) | Crosswalk closure test (Validator 2); steward review on conflicts. | PROPOSED |
| FAU-R-06 | Conservation Status frameworks collapsed across IUCN / USFWS / state in a UI summary. | medium | moderate (truth) | Framework anti-collapse test (Validator 3); microcopy guidance in the Evidence Drawer. | PROPOSED |
| FAU-R-07 | A wildlife disease cluster triggers external media interpretation as a public-health story. | medium | high (reputational) | Release note framing rules; steward response runbook. | NEEDS VERIFICATION runbook |

[⬆ Back to top](#fauna--expansion-plan)

---

## 17. Verification backlog

These are the open `NEEDS VERIFICATION` items inherited from the Domains Culmination Atlas Fauna entry. The expansion plan cannot advance past F0 on any of them until they're resolved.

| # | Item | Where it must show up | Status |
|---|---|---|---|
| 1 | Verify sensitive-taxon registry and Natural Heritage agreement scope. | registry artifact, written per-state agreements, validator coverage | `NEEDS VERIFICATION` |
| 2 | Verify `Taxon Crosswalk` completeness across primary authorities (ITIS / GBIF / equivalents). | crosswalk artifacts, coverage report | `NEEDS VERIFICATION` |
| 3 | Verify `Redaction Receipt` schema and propagation. | schema, propagation tests | `NEEDS VERIFICATION` |
| 4 | Verify per-source rights for State Wildlife Agency datasets. | per-source `SourceRightsAssessment` | `NEEDS VERIFICATION` |
| 5 | Verify per-institution rights for Specimen records. | per-institution agreement, descriptor | `NEEDS VERIFICATION` |
| 6 | Verify release-note framing-linter rule set rejects public-health framing on `DiseaseObservation`. | linter rule, fixtures | `NEEDS VERIFICATION` |
| 7 | Verify the steward runbook for wildlife-disease media response. | runbook artifact, rehearsal record | `NEEDS VERIFICATION` |

[⬆ Back to top](#fauna--expansion-plan)

---

## 18. Anti-patterns to reject

Each row below is a `DENY` outcome, not a stylistic preference.

| Anti-pattern | Why rejected | Corrective doctrine line |
|---|---|---|
| Publishing exact `SensitiveSite` geometry "because the species isn't on the federal list this year." | State and Natural Heritage classifications may still apply; framework collapse is not allowed. | Validator 3 + §13 sensitivity-gate posture. |
| Treating "abundant" species as automatically public-occurrence-safe. | Per-record license still governs; observer-privacy still applies. | §11 source admission roadmap. |
| Crosswalking a `Taxon` (animal) with a Flora `Plant Taxon` (plant). | Cross-kingdom equivalence is forbidden. | §3.2 not-owned table. |
| Letting AI emit a `SensitivityAssessment` for a newly observed taxon. | AI is assistant, not authority. | §15 AI posture. |
| Promoting `Occurrence Restricted` directly to `Occurrence Public` without `Redaction Receipt` and `Generalization Transform`. | Skips the sensitivity gate. | §9.1 promotion pipeline. |
| Framing a `DiseaseObservation` cluster as a public-health alert in a release note. | Public-health authority is not KFM's. | §3.2 not-owned table; §16 risk FAU-R-02. |
| Citing an `Occurrence Public` row's exact-looking coordinates as evidence in an AI Focus Mode answer. | The exact coordinates do not enter the public response payload. | Evidence Drawer rule; §15 AI posture. |
| Hot-fixing a sensitivity reclassification by editing the registry in place. | Sensitivity changes flow through `CorrectionNotice` + superseding release. | Corrections-first-class doctrine. |
| Adding a Natural Heritage Program feed at F1 "because the proof slice needs more species." | F1 publishes range and status only; live occurrences arrive no earlier than F2. | §5 phase ladder + §11 source admission roadmap. |
| Trust-badging a `RangePolygon` as `ANSWER` when its model has no `Model Run Receipt`. | Model lineage is mandatory for any model-derived public claim. | Inherited Habitat rule. |

[⬆ Back to top](#fauna--expansion-plan)

---

## 19. Acceptance checklist per phase

Each phase advances only when **every applicable item** below is checked.

### 19.1 F0 — acceptance

- [ ] [`docs/domains/fauna/README.md`](./README.md) exists with the field spec from the Domains Culmination Atlas. `[PROPOSED path]`
- [ ] [`docs/domains/fauna/EXPANSION_PLAN.md`](./EXPANSION_PLAN.md) (this doc) exists.
- [ ] Contracts for all twelve owned objects exist under `schemas/contracts/v1/domains/fauna/`. `[PROPOSED path]`
- [ ] Fixture set covers every owned object family.
- [ ] Five validators implemented; each has at least one positive and one negative fixture.
- [ ] Policy rules for Fauna implemented with positive + negative fixtures.
- [ ] No-network CI green for Fauna.
- [ ] No public route reads Fauna fixtures.

### 19.2 F1 — acceptance

- [ ] All F0 items still pass.
- [ ] Spatial Foundation at L1.
- [ ] Habitat at L1.
- [ ] Public route serves `Taxon` / `Taxon Crosswalk` / `Conservation Status` / `RangePolygon` / `SeasonalRange` / `MigrationRoute` (sensitive stopovers withheld).
- [ ] Evidence Drawer round-trips a Fauna feature click; all five finite outcomes reachable. `[CONFIRMED finite outcomes.]`
- [ ] Validators 1–4 run live; observer-privacy validator (5) remains fixture-only.
- [ ] AI Focus Mode answers only against F1-admitted objects.

### 19.3 F2 — acceptance

- [ ] All F1 items still pass.
- [ ] At least one live connector active with `SourceRightsAssessment` + `SourceActivationDecision` recorded.
- [ ] `Occurrence Restricted` accessible **only** via steward console.
- [ ] Citizen-science observer-privacy validator runs live on ingested rows.
- [ ] Day-2 runbook for source-failure rehearsed at least once.
- [ ] Steward review record exists for the F2 advancement.

### 19.4 F3 — acceptance

- [ ] All F2 items still pass.
- [ ] Sensitive-taxon registry exists and is aligned with written agreements.
- [ ] `Redaction Receipt` and `Generalization Transform` receipt produced end-to-end.
- [ ] `Occurrence Public` published only for non-sensitive taxa.
- [ ] Sensitive-species habitat-proxy inheritance test passes on the Habitat side.
- [ ] Wildlife-disease framing linter rejects public-health framing.

### 19.5 F4 — acceptance

- [ ] All F3 items still pass.
- [ ] `ProofPack` attestations signed for Fauna releases.
- [ ] Machine-readable `CorrectionNotice` feed live for Fauna sensitivity reclassifications.
- [ ] Multi-party approval enforced on release-significant Fauna actions.
- [ ] Reproducible build verified for at least one Fauna release.

[⬆ Back to top](#fauna--expansion-plan)

---

## 20. Related docs

- [`docs/domains/fauna/README.md`](./README.md) — Fauna field spec (purpose, owned objects, sources, validators, AI notes). `[PROPOSED path; existence NEEDS VERIFICATION]`
- [`docs/domains/habitat/README.md`](../habitat/README.md) — upstream covariate lane. `[PROPOSED path]`
- [`docs/domains/flora/README.md`](../flora/README.md) — sibling sensitive-occurrence lane; sensitivity pattern is parallel. `[PROPOSED path]`
- [`docs/domains/spatial-foundation/README.md`](../spatial-foundation/README.md) — owns CRS, GeographyVersion, generalization receipts. `[PROPOSED path]`
- [`docs/doctrine/evidence-first.md`](../../doctrine/evidence-first.md) — `EvidenceBundle` / `EvidenceRef` closure rules.
- [`docs/doctrine/lifecycle-law.md`](../../doctrine/lifecycle-law.md) — `RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED`.
- [`docs/doctrine/policy-aware.md`](../../doctrine/policy-aware.md) — six-dimension policy gate; sensitivity ladder C0–C5.
- [`docs/doctrine/map-first.md`](../../doctrine/map-first.md) — public map surface rules; Evidence Drawer; finite outcomes.
- [`docs/doctrine/ai-as-assistant.md`](../../doctrine/ai-as-assistant.md) — AI posture, ABSTAIN/DENY rules.
- [`docs/doctrine/corrections-first-class.md`](../../doctrine/corrections-first-class.md) — `CorrectionNotice` flow.
- [`docs/architecture/data-classification-framework.md`](../../architecture/data-classification-framework.md) — full C0–C5 framework. `[PROPOSED path]`
- [`docs/architecture/sensitive-domain-fail-closed.md`](../../architecture/sensitive-domain-fail-closed.md) — cross-domain fail-closed matrix. `[PROPOSED path]`

[⬆ Back to top](#fauna--expansion-plan)

---

## 21. Glossary and abbreviations (appendix)

<details>
<summary><b>Acronyms used in this plan</b></summary>

| Abbreviation | Expansion |
|---|---|
| CWD | Chronic Wasting Disease |
| eDNA | Environmental DNA |
| ESA | Endangered Species Act (United States) |
| GBIF | Global Biodiversity Information Facility |
| HPAI | Highly Pathogenic Avian Influenza |
| iDigBio | Integrated Digitized Biocollections |
| IUCN | International Union for Conservation of Nature |
| ITIS | Integrated Taxonomic Information System |
| NAS | Nonindigenous Aquatic Species (USGS) |
| TSN | Taxonomic Serial Number (ITIS identifier) |
| USFWS | United States Fish and Wildlife Service |
| USGS | United States Geological Survey |

> Abbreviations are provided for reader convenience; their expansion is generally accepted in the field and is not a KFM-internal definition.

</details>

<details>
<summary><b>KFM vocabulary used in this plan</b></summary>

| Term | Meaning (verbatim from project doctrine) |
|---|---|
| `EvidenceBundle` | The closure container that resolves every public claim to its source artifacts. |
| `EvidenceRef` | A stable reference into an `EvidenceBundle`. |
| `DecisionEnvelope` | The payload shape every governed API returns; carries an outcome and reason code. |
| `SourceDescriptor` | The declared identity, role, rights, and freshness of an upstream data source. |
| `SourceRightsAssessment` | The human-role determination of what may be done with a source's data. |
| `SourceActivationDecision` | The human-role decision to move a source from fixture-only to live. |
| `IntakeReceipt` / `TransformReceipt` / `ValidationReport` | Lifecycle artifacts that close audit on every promotion event. |
| `Generalization Transform` receipt | Records the parameters of geometric generalization for sensitive features. |
| `Redaction Receipt` | Records the withholding of a record or sub-record for sensitivity reasons. |
| `ReleaseManifest` / `ProofPack` / `ReviewRecord` | Release-time artifacts that close audit on publication. |
| `CorrectionNotice` | First-class object for sensitivity reclassification, source-rights changes, and superseding releases. |
| `RollbackPlan` | A pre-authored, rehearsed reversion path for a release. |
| `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` / `STALE` | The five finite outcomes any public surface may emit. |
| `CONFIRMED` / `PROPOSED` / `INFERRED` / `NEEDS VERIFICATION` / `UNKNOWN` | Truth labels used throughout KFM documentation. |
| `RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED` | The lifecycle-stage invariant. |

</details>

<details>
<summary><b>Fauna-local phase identifiers</b></summary>

`F0` — Membrane and fixtures. No live connectors. No public route.

`F1` — Public-safe proof slice: `Taxon` / `Taxon Crosswalk` / `Conservation Status` / `RangePolygon` / `SeasonalRange` / `MigrationRoute` (sensitive stopovers withheld). No occurrences.

`F2` — Steward-restricted live activation: occurrences flow into `Occurrence Restricted`; visible only on the steward console.

`F3` — Generalized public occurrences for non-sensitive taxa via `Redaction Receipt` + `Generalization Transform` receipt.

`F4` — Broad coverage + federation: multi-source coverage with attested `ProofPack`, federated `CorrectionNotice`, multi-party approval.

</details>

[⬆ Back to top](#fauna--expansion-plan)

---

**Related docs:** [Fauna README](./README.md) `[PROPOSED path]` · [Habitat README](../habitat/README.md) `[PROPOSED path]` · [Spatial Foundation README](../spatial-foundation/README.md) `[PROPOSED path]` · [evidence-first.md](../../doctrine/evidence-first.md) · [lifecycle-law.md](../../doctrine/lifecycle-law.md) · [policy-aware.md](../../doctrine/policy-aware.md) · [map-first.md](../../doctrine/map-first.md) · [ai-as-assistant.md](../../doctrine/ai-as-assistant.md) · [corrections-first-class.md](../../doctrine/corrections-first-class.md)

**Last updated:** 2026-05-16 · **Version:** v1 (draft) · **Status:** awaiting steward and security review

[⬆ Back to top](#fauna--expansion-plan)
