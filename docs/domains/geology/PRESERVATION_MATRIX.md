<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/geology-preservation-matrix
title: Geology Preservation Matrix
type: standard
version: v1
status: draft
owners: Geology domain steward (TBD); Docs steward (TBD)
created: 2026-05-17
updated: 2026-05-17
policy_label: public
related:
  - docs/domains/geology/README.md (PROPOSED)
  - docs/standards/PROV.md
  - docs/doctrine/directory-rules.md (PROPOSED canonical home)
  - control_plane/policy_gate_register.yaml (PROPOSED)
  - policy/domains/geology/ (PROPOSED lane root)
  - schemas/contracts/v1/domains/geology/ (PROPOSED lane root)
tags: [kfm, geology, preservation, sensitivity, lifecycle, governance]
notes:
  - Per-family tier assignments are PROPOSED extensions of confirmed DOM-GEOL §I posture and Atlas v1.1 §24.5 tier scheme.
  - All repo-shaped paths PROPOSED pending mounted-repo and ADR verification.
[/KFM_META_BLOCK_V2] -->

# Geology Preservation Matrix

> Per-object-family preservation, sensitivity, transform, and release rules for the **Geology and Natural Resources** domain — the operational table that binds DOM-GEOL doctrine to the RAW → PUBLISHED lifecycle.

<!-- Badge row — placeholders until CI/registries are wired. -->
![Status: draft](https://img.shields.io/badge/status-draft-yellow)
![Authority: domain doctrine](https://img.shields.io/badge/authority-domain%20doctrine-blue)
![Lifecycle: RAW%20%E2%86%92%20PUBLISHED](https://img.shields.io/badge/lifecycle-RAW%20%E2%86%92%20PUBLISHED-informational)
![Tier scheme: T0%E2%80%93T4 (PROPOSED)](https://img.shields.io/badge/tiers-T0%E2%80%93T4%20PROPOSED-orange)
![Domain: geology](https://img.shields.io/badge/domain-geology-brown)
<!-- TODO: replace with real CI / coverage / last-validated Shields.io endpoints once a workflow exists. -->

**Status:** `draft` · **Owners:** Geology domain steward *(TBD)* + Docs steward *(TBD)* · **Last updated:** 2026‑05‑17

---

## Contents

1. [Purpose & Scope](#1-purpose--scope)
2. [Doctrinal Basis & Authority](#2-doctrinal-basis--authority)
3. [Lifecycle Preservation (RAW → PUBLISHED)](#3-lifecycle-preservation-raw--published)
4. [Sensitivity / Rights Tier Scheme (T0–T4)](#4-sensitivity--rights-tier-scheme-t0t4)
5. [Per-Object-Family Preservation Matrix](#5-per-object-family-preservation-matrix)
6. [Source-Role Preservation](#6-source-role-preservation)
7. [Claim-Class Preservation (Occurrence ≠ Deposit ≠ Estimate ≠ Reserve)](#7-claim-class-preservation-occurrence--deposit--estimate--reserve)
8. [Allowed Transforms, Receipts, and Required Gates](#8-allowed-transforms-receipts-and-required-gates)
9. [Tier Transitions](#9-tier-transitions)
10. [Correction, Rollback, and Re-Preservation](#10-correction-rollback-and-re-preservation)
11. [Validators, Tests, and Fixtures](#11-validators-tests-and-fixtures)
12. [Open Questions & Verification Backlog](#12-open-questions--verification-backlog)
13. [Related Docs](#13-related-docs)
14. [Appendix A — Truth Labels Used in This Document](#appendix-a--truth-labels-used-in-this-document)

---

## 1. Purpose & Scope

The Geology Preservation Matrix is the **per-object-family operational expression** of DOM-GEOL's sensitivity, rights, and publication posture. It answers, for every canonical geology object family, four questions:

- **What is the default sensitivity / rights tier** at which the object family is preserved and exposed?
- **Which lifecycle phases** must the object survive intact, and which phases are permitted to derive public-safe forms?
- **Which transforms** are admissible to move the object from one tier to another, and **what receipts** must accompany each transform?
- **Which gates** must close before the object can advance toward `PUBLISHED`?

This document does **not** redefine geology's object families, schemas, or APIs — those live in `contracts/`, `schemas/`, and `apps/governed-api/` lanes. It encodes only the **preservation policy view** of those objects.

> [!IMPORTANT]
> This matrix is **subordinate to** the [KFM Operating Law](#2-doctrinal-basis--authority): the public unit of value is an **inspectable claim** whose evidence, source role, policy posture, review state, and release state are auditable. The matrix below is one of the surfaces that makes that auditability concrete for geology.

<details>
<summary><strong>Out of scope (explicit non-ownership)</strong></summary>

- Hydrology measurements (geology may **reference** hydrostratigraphy without owning gauge or flow truth — see DOM-HYD).
- Soils, hazards risk, ownership/lease/permit/title claims, and UI/AI statements — these are governed by their own domain lanes and **never** become canonical geology truth.
- The decision of *whether* a geology object exists — that is a `contracts/` + `policy/` + `ADR` decision, not a Preservation Matrix decision.
- Field-level schema shape — owned by `schemas/contracts/v1/domains/geology/` *(PROPOSED path)*.

</details>

[Back to top ↑](#geology-preservation-matrix)

---

## 2. Doctrinal Basis & Authority

| Source | Status | What it grounds in this doc |
|---|---|---|
| KFM Operating Law — inspectable claim, evidence hierarchy, lifecycle law, trust membrane, publication gate, correction/rollback | **CONFIRMED** doctrine | The non-negotiable spine of every row below. |
| DOM-GEOL §A–§I — geology mission, object families, sensitivity posture | **CONFIRMED** doctrine / **PROPOSED** implementation | Object inventory, claim-class distinctions, exact-location defaults. |
| Atlas v1.1 §24.5 — Master Sensitivity / Rights Tier Reference (T0–T4) | **PROPOSED** scheme | The tier vocabulary; per-domain rows for geology were not enumerated in v1.1 §24.5.2 and are introduced here. |
| Atlas v1.1 §24.14 — Master Object Family × Domain Reference Matrix | Owner column **CONFIRMED**; sensitivity defaults **PROPOSED** | Geology owns `GeologicUnit/Lithology`, etc.; `MineralOccurrence/ResourceEstimate` carry "T0 aggregate / T2 detail in sensitive contexts" defaults. |
| Directory Rules §12 — Domain Placement Law | **CONFIRMED** doctrine | This file lives under `docs/domains/geology/` as a lane segment, never as a root folder. |
| ADR-0001 — Schema-home rule (`schemas/contracts/v1/...`) | **CONFIRMED** referenced doctrine; **NEEDS VERIFICATION** in mounted repo | Anchors any schema-bearing claim in this doc. |

> [!NOTE]
> When this matrix appears to contradict DOM-GEOL or Atlas v1.0/v1.1 doctrine, **doctrine wins**. Open a drift entry in `docs/registers/DRIFT_REGISTER.md` *(PROPOSED path)* and an ADR if the doctrine itself needs amendment.

[Back to top ↑](#geology-preservation-matrix)

---

## 3. Lifecycle Preservation (RAW → PUBLISHED)

**CONFIRMED doctrine** — every geology object traverses the standard KFM lifecycle. Promotion between phases is a **governed state transition**, not a file move. Preservation discipline differs by phase.

```mermaid
flowchart LR
    A["RAW<br/><sub>immutable source payload<br/>+ SourceDescriptor</sub>"] --> B["WORK / QUARANTINE<br/><sub>schema · geometry · time · identity<br/>· rights · sensitivity normalization</sub>"]
    B --> C["PROCESSED<br/><sub>validated objects<br/>+ EvidenceRef + ValidationReport</sub>"]
    C --> D["CATALOG / TRIPLET<br/><sub>EvidenceBundle + graph projection<br/>+ release candidate</sub>"]
    D --> E["PUBLISHED<br/><sub>ReleaseManifest + LayerManifest<br/>+ correction path + rollback target</sub>"]

    B -. fails closed .-> Q[("QUARANTINE<br/>reason recorded")]
    E -. CorrectionNotice / RollbackCard .-> E

    classDef phase fill:#f5f0e6,stroke:#7a5a2e,stroke-width:1px,color:#3b2a12;
    classDef fail fill:#fde7e7,stroke:#a33,stroke-width:1px,color:#700;
    class A,B,C,D,E phase;
    class Q fail;
```

**Per-phase preservation rules** *(CONFIRMED doctrine / PROPOSED lane application)*:

| Phase | What MUST be preserved | What MUST NOT be discarded | Gate |
|---|---|---|---|
| **RAW** | Immutable source payload (or signed reference), `SourceDescriptor`, source role, rights, sensitivity flag, citation, observation/retrieval times, content hash. | Original source bytes; original coordinate precision; original units; vendor identifiers. | `SourceDescriptor` exists and resolves. |
| **WORK / QUARANTINE** | Normalization receipts; geometry-validity report; identity assignment receipt; quarantine reason if held. | Original RAW lineage pointer; transform receipts; failure metadata. | Validation + policy gate pass, **or** quarantine reason recorded. |
| **PROCESSED** | Validated normalized objects; `EvidenceRef`; `ValidationReport`; public-safe candidate geometry (where applicable). | Coordinate-precision generalization receipt; transform chain back to RAW. | `EvidenceRef`, `ValidationReport`, and digest closure exist. |
| **CATALOG / TRIPLET** | Catalog records; `EvidenceBundle`; graph/triplet projection; release candidate envelope. | Bundle-level provenance; per-claim sensitivity tier; review state. | Catalog/proof closure passes. |
| **PUBLISHED** | `ReleaseManifest`; `LayerManifest`; correction path; rollback target; `ReviewRecord` where required. | Public-safe layer artifacts; sensitivity-redacted receipts; signature/digest evidence. | `ReleaseManifest` + correction path + rollback target + review/policy state exist. |

> [!WARNING]
> **Watcher-as-non-publisher invariant.** Geology watchers (e.g., source-drift detectors for KGS, KCC, USGS NGMDB) observe and record only. They emit `RunReceipt` and candidate decisions; they **never** write to `data/catalog/` or `data/published/`. Promotion remains a governed transition under steward and release-authority control.

[Back to top ↑](#geology-preservation-matrix)

---

## 4. Sensitivity / Rights Tier Scheme (T0–T4)

The tier scheme below is **PROPOSED** doctrine from Atlas v1.1 §24.5.1 and is reused verbatim here; the per-geology-family rows in §5 extend the scheme into this domain.

| Tier | Name | Definition | Default audience |
|---|---|---|---|
| **T0** | Open | Public-safe with no transformation required beyond standard release. | Any public client via governed API. |
| **T1** | Generalized | Public-safe only after generalization, fuzzing, aggregation, or redaction; the transform is reviewed and recorded. | Any public client via governed API. |
| **T2** | Reviewer | Released only to authenticated reviewers or domain stewards; policy-bounded; correction path active. | Stewards, reviewers, named research collaborators. |
| **T3** | Restricted | Released only under named agreement (rights, sovereignty, or consent) and recorded. | Named authorized parties only. |
| **T4** | Denied | Not released to any audience; existence of a record may be released only as steward review permits. | — |

> [!TIP]
> Tier ≠ phase. A `MineralOccurrence` at **T0** aggregate may still sit in `WORK/QUARANTINE` if validation has not yet closed. A `WellLog` at **T4** is still preserved through all lifecycle phases — it is the **release** that is denied, not the preservation.

[Back to top ↑](#geology-preservation-matrix)

---

## 5. Per-Object-Family Preservation Matrix

**CONFIRMED object-family spine (DOM-GEOL §C):** `GeologicUnit`, `Lithology`, `StratigraphicInterval`, `GeologicAge`, `FaultStructure`, `Borehole`, `WellLog`, `CoreSample`, `GeophysicalObservation`, `GeochemistrySample`, `MineralOccurrence`, `ResourceDeposit`, `ExtractionSite`, `ReclamationRecord`, `CrossSection`, `HydrostratigraphicUnit`.

The default tier and allowed transforms below are **PROPOSED extensions** of the confirmed DOM-GEOL §I posture ("exact borehole, sample, sensitive resource, well-log, and private well locations default to restricted or generalized public geometry") and Atlas v1.1 §24.14 ("`MineralOccurrence/ResourceEstimate` — T0 aggregate; T2 detail in sensitive contexts").

| Object family | Default tier | Allowed transforms (PROPOSED) | Required gates | Notes |
|---|---|---|---|---|
| `GeologicUnit` | **T0** | None required for published bedrock/surficial maps; generalization for cartographic scale. | `ReleaseManifest` + `LayerManifest`. | Unit polygons are the canonical public surface; interpretation version preserved. |
| `Lithology` | **T0** | None required. | `ReleaseManifest`. | Bound to `GeologicUnit`; descriptive, not locational. |
| `StratigraphicInterval` | **T0** | None required. | `ReleaseManifest`. | Correlation strength preserved as uncertainty annotation. |
| `GeologicAge` | **T0** | None required. | `ReleaseManifest`. | Age model version preserved with `spec_hash`. |
| `FaultStructure` | **T0** *(public maps)* / **T2** *(detailed seismotectonic detail)* | Generalization of trace where sensitive infrastructure proximity applies. | `RedactionReceipt` if generalized; steward review for sensitive joins. | Hazards lane consumes via `kfm:` namespace relation; geology does not own risk. |
| `Borehole` *(public well)* | **T1** | Coordinate fuzzing to a cell size set by steward review; `RedactionReceipt`. | `RedactionReceipt` + `ReviewRecord`. | DOM-GEOL §I: exact borehole locations default to restricted or generalized public geometry. |
| `Borehole` *(private well / proprietary)* | **T4** | T3 only under explicit data-use agreement; T2 to named reviewers; generalized aggregate → T1. | Named agreement + `ReviewRecord` + `PolicyDecision`. | "Private well locations default to restricted or generalized public geometry" — CONFIRMED posture. |
| `WellLog` *(KGS LAS public archive)* | **T1** | Generalization of well coordinate + curve-level metadata published; raw LAS access via reviewer tier. | `RedactionReceipt` + `ReviewRecord`. | DOM-GEOL §K names borehole/well-log rights tests as PROPOSED. |
| `WellLog` *(proprietary / embargoed)* | **T4** | T3 under named research agreement only. | Named agreement + `PolicyDecision`. | Rights and embargo status preserved on `SourceDescriptor`. |
| `CoreSample` | **T2** | Aggregate sample-density layer → T1; sample-level access via reviewer tier. | `AggregationReceipt` + `ReviewRecord`. | Physical sample existence may be public; precise locality and analytical detail tier-gated. |
| `GeophysicalObservation` | **T1** | Generalized raster product public; full-resolution gridded data via reviewer tier where rights permit. | `RedactionReceipt` or `ReviewRecord`. | Raster vintages preserved per `DatasetVersion`. |
| `GeochemistrySample` | **T2** | Aggregated/binned anomaly layer → T1; sample-level access via reviewer tier. | `AggregationReceipt` + `ReviewRecord`. | Anomaly mapping risks resource fingerprinting — see §7. |
| `MineralOccurrence` | **T0** *(aggregate)* / **T2** *(detail in sensitive contexts)* | Generalized occurrence-density layer at T0; locality detail via reviewer tier when sensitivity applies. | `AggregationReceipt` for T0 rollups; `ReviewRecord` for T2. | Atlas v1.1 §24.14 — CONFIRMED owner, **PROPOSED** sensitivity default. |
| `ResourceDeposit` | **T2** *(default)* | Generalized resource-context layer → T1 only after steward review. | `RedactionReceipt` + `ReviewRecord`. | Distinct from `MineralOccurrence` (see §7). |
| `ResourceEstimate` | **T2** *(default)* | Aggregate basin/play-level estimate → T1 only after steward and rights review. | `ReviewRecord` + `PolicyDecision`. | Estimate ≠ reserve ≠ production. Class-mixing is anti-doctrine (DOM-GEOL §K). |
| `ExtractionSite` | **T1** | Generalized site footprint public; operator-linked condition detail tier-gated. | `RedactionReceipt`. | Operator-linkage to People/Land must preserve PEOPLE-domain restrictions. |
| `ReclamationRecord` | **T0** | None required. | `ReleaseManifest`. | Reclamation status is a public-interest signal. |
| `CrossSection` | **T0** *(public maps)* / **T2** *(detailed proprietary)* | Generalized cross-section for public display; full geophysical/well-derived sections via reviewer tier. | `RedactionReceipt` if derived from T2/T4 sources. | Carries interpretation-version receipt. |
| `HydrostratigraphicUnit` | **T0** | None required. | `ReleaseManifest`. | Cross-domain bridge to Hydrology; preserves "context without replacing measurements" (DOM-GEOL §F). |

> [!CAUTION]
> A **T0 aggregate does not authorize T0 detail.** Aggregating `MineralOccurrence` to a county-level rollup is a transform with a receipt; the underlying point-level records remain at their default tier. Do not back-fill the T0 label onto the source records.

[Back to top ↑](#geology-preservation-matrix)

---

## 6. Source-Role Preservation

Source role is recorded on `SourceDescriptor` and **must be preserved** through every transform. Confusing a `model` source with an `observation` source is a doctrinal violation that this matrix must defend against.

| Source family | Typical role(s) | Rights / sensitivity | Freshness | Preservation note |
|---|---|---|---|---|
| Kansas Geological Survey (KGS) — geologic maps, surficial geology | authority / context | NEEDS VERIFICATION; sensitive joins fail closed | source-vintage-specific | KGS map vintages preserved per `DatasetVersion`. |
| USGS NGMDB / GeMS | authority / context | NEEDS VERIFICATION | source-vintage-specific | GeMS-style attributes preserved during normalization; no schema flattening at WORK. |
| KGS oil and gas wells / production | authority / observation | NEEDS VERIFICATION | source-vintage / cadence | Public-vs-proprietary split must be preserved at RAW. |
| KCC oil and gas regulatory data | authority | NEEDS VERIFICATION | cadence-specific | Regulatory channel — distinct provenance from observation. |
| KGS/KDHE WWC5 water-well program | authority / observation | NEEDS VERIFICATION | cadence-specific | Private-well coordinates default to T4 — see §5. |
| KGS LAS digital well logs / well tops | observation | rights-bearing; NEEDS VERIFICATION | source-vintage | LAS curves and well tops carry separate rights envelopes. |
| USGS MRDS | authority / context | NEEDS VERIFICATION | source-vintage-specific | Occurrence vs deposit class must be preserved. |
| USGS 3DEP terrain | authority / observation | typically open | release-specific | Used as geomorphology context; preserve resolution and acquisition date. |

> [!NOTE]
> All rights/sensitivity entries above are **NEEDS VERIFICATION** until current source-use terms are recorded in `data/registry/sources/geology/` *(PROPOSED path)* and signed off by the source steward.

[Back to top ↑](#geology-preservation-matrix)

---

## 7. Claim-Class Preservation (Occurrence ≠ Deposit ≠ Estimate ≠ Reserve)

**CONFIRMED doctrine (DOM-GEOL §I):** *"Occurrence, deposit, estimate, permit, production, and reserve claims must remain distinct."*

| Claim class | Definition (CONFIRMED term / PROPOSED field realization) | Distinct from | Anti-collapse rule |
|---|---|---|---|
| **Occurrence** | A documented observation of a mineral or hydrocarbon presence at a location. | Deposit, Estimate, Reserve. | Aggregation into a "deposit" layer requires a transform receipt; the source occurrence records preserve their class. |
| **Deposit** | A geologically delineated body of resource material with characterized extent. | Estimate, Reserve. | Delineation method, vintage, and authority preserved; no implicit promotion from "many occurrences" to "deposit." |
| **Estimate** | A quantitative resource estimate produced under a stated reporting framework. | Reserve, Production. | Reporting framework preserved on the estimate; cross-framework comparison requires explicit crosswalk receipt. |
| **Reserve** | An economically recoverable subset of an estimate under specified conditions. | Estimate, Production. | Economic and regulatory conditions preserved; a reserve never decays silently into an estimate or vice versa. |
| **Permit** | A regulatory authorization tied to a site or operator. | Production, Extraction Site. | Regulatory provenance (e.g., KCC) preserved; permits are not production evidence. |
| **Production** | Reported extraction over a defined interval. | Permit, Estimate. | Operator self-reporting role preserved on `SourceDescriptor`; production never proves estimate. |

> [!IMPORTANT]
> Anti-collapse is enforced at three places: (1) the `contracts/` Markdown for each class, (2) `schemas/contracts/v1/domains/geology/` *(PROPOSED)* via distinct types, and (3) a PROPOSED `tests/domains/geology/` resource-class anti-collapse fixture (DOM-GEOL §K). This matrix is the **doctrinal** anchor for those enforcement points.

[Back to top ↑](#geology-preservation-matrix)

---

## 8. Allowed Transforms, Receipts, and Required Gates

Every demotion in sensitivity ("show less precisely") or aggregation ("show in summary") is a **transform** with a **receipt** linked into the object's `EvidenceBundle`. The catalog below enumerates the geology-relevant transforms.

| Transform | Effect | Receipt | Tier motion |
|---|---|---|---|
| **Coordinate generalization (cell-binning)** | Snap point to a cell of stated size (e.g., 1 km, 10 km PROPOSED defaults). | `RedactionReceipt` (records cell size, method, reason). | T4 → T1, T2 → T1, T1 → T0 *(only with steward + release authority)*. |
| **Coordinate fuzzing** | Apply a randomized offset within a stated radius. | `RedactionReceipt` (radius, RNG seed reference). | T4 → T1, T2 → T1. |
| **Geometry generalization** | Reduce polyline/polygon vertices, snap to scale. | `RedactionReceipt` (scale target, simplification method). | T0 *(scale variant)*, T2 → T1. |
| **Aggregation** | Roll up point/feature records to a coarser unit (county, HUC, basin, play). | `AggregationReceipt` (aggregation unit, count, threshold). | T2 → T1, T1 → T0. |
| **Attribute suppression** | Remove a sensitive attribute (operator, owner, condition). | `RedactionReceipt` (attribute list, reason). | T2 → T1, T4 → T2. |
| **Interpretation versioning** | Mark interpretation vintage on cross-section, age model, or correlation. | `DatasetVersion` annotation. | Within-tier — does not move tier. |
| **Reality boundary annotation** *(3D only)* | Distinguish measured vs interpretive 3D content. | `RepresentationReceipt` (per MAP-MASTER / UIAI). | Required for any geology object exposed via Planetary/3D admission. |

> [!CAUTION]
> **Style filters are not a valid sensitive-geometry protection mechanism** (Master MapLibre ML-Q-082). Hiding a layer with a renderer filter does not redact the underlying tile. Generalization, suppression, and aggregation are the only doctrinally sound mechanisms; receipts must reflect the change at the data layer.

[Back to top ↑](#geology-preservation-matrix)

---

## 9. Tier Transitions

**PROPOSED transitions** (Atlas v1.1 §24.5.3 scheme, geology-applied):

| From → To | Required artifact | Required reviewer | Reversibility |
|---|---|---|---|
| T4 → T3 | `PolicyDecision` + `ReviewRecord` + named agreement | Geology steward + rights-holder where applicable | Reversible: agreement revocation returns to T4 with `CorrectionNotice`. |
| T4 → T2 | `PolicyDecision` + `ReviewRecord` | Geology steward | Reversible: review revocation returns to T4. |
| T4 → T1 | `RedactionReceipt` + `ReviewRecord` | Geology steward | Reversible: redaction may be re-evaluated; a correction may demote a published T1 back to T4 via `RollbackCard`. |
| T3 → T2 | `PolicyDecision` + `ReviewRecord` | Geology steward | Reversible. |
| T2 → T1 | `RedactionReceipt` + `ReviewRecord` | Geology steward | Reversible. |
| T1 → T0 | `ReleaseManifest` + `ReviewRecord` | Geology steward + release authority | Reversible: rollback via `RollbackCard`. |

```mermaid
stateDiagram-v2
    [*] --> T4: ingest (default-deny)
    T4 --> T3: PolicyDecision + Agreement
    T4 --> T2: PolicyDecision + Review
    T4 --> T1: RedactionReceipt + Review
    T3 --> T2: PolicyDecision + Review
    T2 --> T1: RedactionReceipt + Review
    T1 --> T0: ReleaseManifest + Review + Release Authority
    T0 --> T1: CorrectionNotice / RollbackCard
    T1 --> T4: CorrectionNotice / RollbackCard (severe)
    T2 --> T4: Review revocation
```

> [!NOTE]
> **Default-deny on ingest.** New geology source families enter the WORK lane with an implicit T4 sensitivity flag until a `SourceDescriptor` + rights review establish a higher-trust default. This is consistent with the KFM "safe state is quarantine, denial, restriction, or abstention until rights, source role, access conditions, cadence, and release class are recorded" posture.

[Back to top ↑](#geology-preservation-matrix)

---

## 10. Correction, Rollback, and Re-Preservation

Geology preservation is **reversible by design**.

| Event | Required artifact | Effect on tier | Effect on lifecycle |
|---|---|---|---|
| Source-side correction (KGS, USGS, KCC issues an erratum) | `CorrectionNotice` linked to the source's `EvidenceBundle`. | May trigger tier re-evaluation. | Released artifact remains; supersession entry recorded. |
| Rights change (license revocation, embargo activation) | `PolicyDecision` + `RollbackCard`. | T0/T1 published may demote to T4. | Released artifact withdrawn via `RollbackCard`; correction path active. |
| Steward review revocation | `ReviewRecord` (revocation) + `CorrectionNotice`. | Returns object to default tier. | Published descendants tracked through release supersession. |
| Discovered class-collapse error (e.g., estimate published as reserve) | `CorrectionNotice` + `ReleaseManifest` revision. | Class-class correction; tier may shift. | Republish under the correct class; the wrong publication retained for audit. |
| Discovered geometry over-exposure (e.g., raw borehole published instead of generalized) | `RollbackCard` + `RedactionReceipt`. | T0/T1 → T4 immediate. | Layer withdrawn; corrected layer republished only after re-review. |

> [!WARNING]
> **Corrections are not silent.** A released layer that demotes from T0 to T4 leaves a public, citable `CorrectionNotice`. Re-publishing under the same name without lineage is anti-doctrine and reviewable as drift.

[Back to top ↑](#geology-preservation-matrix)

---

## 11. Validators, Tests, and Fixtures

The validators listed below are **PROPOSED** per DOM-GEOL §K and bind directly into the Preservation Matrix rows.

| Validator (PROPOSED) | What it enforces | Likely home *(PROPOSED)* |
|---|---|---|
| Source-role validator | `SourceDescriptor.role` is one of the canonical roles; no role drift across pipeline phases. | `tools/validators/source/` |
| Resource-class anti-collapse test | `MineralOccurrence`, `ResourceDeposit`, `ResourceEstimate`, `Reserve`, `Permit`, `Production` types do not interchange. | `tests/domains/geology/claim-class/` |
| Public-safe geometry test | Published geology layers carry the appropriate `RedactionReceipt` or `AggregationReceipt` when their source class defaults to T1+. | `tests/domains/geology/public-safe-geometry/` |
| Borehole / well-log rights test | Private and proprietary `Borehole` / `WellLog` records never appear at T0/T1 without rights closure. | `tests/domains/geology/well-rights/` |
| Catalog closure test | Geology `CATALOG` records resolve to a complete `EvidenceBundle` with all referenced sources, transforms, and reviews. | `tests/domains/geology/catalog-closure/` |
| AI evidence-before-model test | Geology Focus Mode answers ABSTAIN when `EvidenceBundle` is insufficient and DENY when policy blocks. | `tests/domains/geology/governed-ai/` |
| Tier-transition fixture set | Each row in §9 has a positive (valid transition) and negative (forbidden transition) fixture. | `fixtures/domains/geology/tier-transitions/` |

> [!TIP]
> These tests are the enforcement surface of this matrix. Adding a new geology object family or source family **without** adding the corresponding fixtures is a drift event.

[Back to top ↑](#geology-preservation-matrix)

---

## 12. Open Questions & Verification Backlog

| # | Question / item | Why it matters | Status |
|---|---|---|---|
| Q1 | Confirm the canonical home for geology schemas (`schemas/contracts/v1/domains/geology/` per ADR-0001). | Anchors every schema-bearing claim in this doc. | **NEEDS VERIFICATION** — mounted repo + ADR. |
| Q2 | Are KGS LAS public archive coordinates already generalized at the source, or is generalization the KFM's responsibility on ingest? | Determines whether the WORK phase needs a coordinate-generalization step by default. | **NEEDS VERIFICATION** — source-use terms + steward sign-off. |
| Q3 | What cell size(s) are the canonical defaults for borehole coordinate generalization (proposed: 1 km, 10 km)? | Cell-size selection is a steward decision with downstream tile-pyramid implications. | **PROPOSED** — needs steward decision + ADR. |
| Q4 | Where is the canonical `data/registry/sources/geology/` index and what is its source-of-truth relationship to `control_plane/source_authority_register.yaml`? | Required to resolve rights/sensitivity claims to operational state. | **NEEDS VERIFICATION**. |
| Q5 | Should `FaultStructure` carry a sensitive-infrastructure proximity override (auto-T2 within N meters of named critical assets)? | Cross-lane policy interaction with Settlements/Infrastructure. | **OPEN** — cross-domain ADR likely required. |
| Q6 | What is the canonical `RedactionReceipt` schema home, and does it differ for geology vs other domains? | Determines whether per-domain receipt subclasses exist or a single envelope governs. | **NEEDS VERIFICATION** — referenced in Atlas v1.1 §24.5 transforms but not enumerated. |
| Q7 | Does the planetary/3D admission policy for `CrossSection` rendering require a per-section `RepresentationReceipt`, or is one bundle-level receipt sufficient? | Affects 3D scene release flow for subsurface views. | **OPEN** — MAP-MASTER / UIAI doctrine intersection. |
| Q8 | Confirm `ResourceEstimate` reporting frameworks supported on the public surface (e.g., CRIRSCO-family vs USGS Circular 831 vs internal). | Cross-framework comparison without an explicit crosswalk receipt is anti-doctrine. | **OPEN** — needs source-steward enumeration. |

[Back to top ↑](#geology-preservation-matrix)

---

## 13. Related Docs

- `docs/domains/geology/README.md` — geology domain landing page *(PROPOSED home — verify path)*.
- `docs/standards/PROV.md` — provenance standard governing `EvidenceBundle` lineage.
- `docs/doctrine/directory-rules.md` — §12 Domain Placement Law authorizing this file's location *(PROPOSED canonical home)*.
- `docs/doctrine/lifecycle-law.md` — RAW → PUBLISHED invariant *(PROPOSED path)*.
- `docs/doctrine/trust-membrane.md` — public client / governed API discipline *(PROPOSED path)*.
- `contracts/domains/geology/` — geology object-family meaning *(PROPOSED lane)*.
- `schemas/contracts/v1/domains/geology/` — geology object-family machine shape *(PROPOSED lane, ADR-0001)*.
- `policy/domains/geology/` — geology admissibility, sensitivity, release policy *(PROPOSED lane)*.
- `policy/sensitivity/` — cross-domain sensitivity rules *(PROPOSED lane)*.
- `control_plane/source_authority_register.yaml` — source rights and authority state *(PROPOSED)*.
- `docs/registers/DRIFT_REGISTER.md` — open the entry here when this matrix conflicts with implementation *(PROPOSED)*.
- KFM Domains Culmination Atlas v1.1 §7 / §24.5 / §24.14 — tier scheme and master family × domain matrix.
- KFM Encyclopedia §7.8 — Geology and Natural Resources domain doctrine.

[Back to top ↑](#geology-preservation-matrix)

---

## Appendix A — Truth Labels Used in This Document

| Label | Meaning in this doc |
|---|---|
| **CONFIRMED** | Anchored in attached KFM doctrine (DOM-GEOL, Atlas v1.0/v1.1, Encyclopedia, Directory Rules, Unified Build Manual). |
| **PROPOSED** | Extension, recommendation, path, or placement not yet verified in a mounted repo or ratified by ADR. |
| **NEEDS VERIFICATION** | Checkable against repo evidence or steward sign-off; not yet checked strongly enough to act as fact. |
| **OPEN** | Cross-domain or scope question whose resolution requires more than a single ADR or review. |
| **UNKNOWN** | Not resolvable in the current session. |

> [!NOTE]
> Memory is not evidence. Any specific path, route, owner, or maturity claim in this document remains **PROPOSED / NEEDS VERIFICATION** until inspected against the mounted repository.

---

<sub>**Related docs:** see [§13](#13-related-docs) · **Doctrine basis:** see [§2](#2-doctrinal-basis--authority) · **Open verification items:** see [§12](#12-open-questions--verification-backlog)</sub>

<sub>**Last updated:** 2026‑05‑17 · [Back to top ↑](#geology-preservation-matrix)</sub>
