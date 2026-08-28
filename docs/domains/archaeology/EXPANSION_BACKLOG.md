<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-domains-archaeology-expansion-backlog
title: Archaeology & Cultural Heritage — Expansion Backlog
type: standard
version: v0.3
status: draft
owners: <Archaeology domain steward — TODO>, <Docs steward — TODO>
created: 2026-05-15
updated: 2026-05-29
policy_label: public
contract_version: "3.0.0"
related: [
  docs/domains/archaeology/README.md,
  docs/domains/archaeology/EXPANSION_PLAN.md,
  docs/domains/archaeology/FILE_SYSTEM_PLAN.md,
  docs/doctrine/directory-rules.md,
  docs/doctrine/ai-build-operating-contract.md,
  docs/doctrine/authority-ladder.md,
  docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf,
  docs/registers/VERIFICATION_BACKLOG.md,
  docs/registers/DRIFT_REGISTER.md
]
tags: [kfm, archaeology, backlog, expansion, governance, sensitivity, doctrine-adjacent]
notes: [
  "CONTRACT_VERSION = \"3.0.0\" — pinned per ai-build-operating-contract.md §0 / §37.",
  "PROPOSED placement per Directory Rules v1.3 §12 (Domain Placement Law); no mounted repo verified this session.",
  "All implementation-shaped claims default to PROPOSED until repo evidence resolves them.",
  "External standards (CARE, H3, FAIR) referenced only through KFM project sources.",
  "Normative language follows RFC 2119 / RFC 8174 per ai-build-operating-contract.md §5.1.1.",
  "v0.3 corrections: Directory Rules is the live v1.3 edition; contracts-home is contracts/domains/archaeology/ (the v0.2 contracts/archaeology/ omitted the domains/ segment and matched the DR §12 CONFLICTED anti-pattern); schema-home shorthand schemas/contracts/v1/archaeology/ is flagged against the canonical schemas/contracts/v1/domains/archaeology/; the §23.2 county/region floor is named the authoritative public floor and H3 r7 / 5 km are reframed as PROPOSED lane refinements."
]
[/KFM_META_BLOCK_V2] -->

# Archaeology & Cultural Heritage — Expansion Backlog

> Forward-work register for the KFM Archaeology and Cultural Heritage domain — feature candidates, verification gaps, validator gaps, cross-lane edges, and Pass 18 expansion ideas, with truth labels preserved.

<p align="left">
  <img alt="status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="domain: archaeology" src="https://img.shields.io/badge/domain-archaeology%20%26%20cultural%20heritage-8a4f7d">
  <img alt="doctrine: CONFIRMED" src="https://img.shields.io/badge/doctrine-CONFIRMED-2ea043">
  <img alt="implementation: PROPOSED" src="https://img.shields.io/badge/implementation-PROPOSED-orange">
  <img alt="directory rules: v1.3" src="https://img.shields.io/badge/Directory%20Rules-v1.3-8957e5">
  <img alt="sensitivity default: T4" src="https://img.shields.io/badge/sensitivity%20default-T4%20(fail--closed)-b30000">
  <img alt="contract: v3.0.0" src="https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-2ea043">
  <img alt="last-updated: 2026-05-29" src="https://img.shields.io/badge/last%20updated-2026--05--29-blue">
</p>

| | |
|---|---|
| **Status** | Draft — review pending |
| **Owners** | Archaeology domain steward · Docs steward *(names — TODO)* |
| **Last reviewed** | 2026-05-29 |
| **Authority class** | Doctrine-grounded planning register (subordinate to ADRs, Directory Rules, and per-root READMEs) |
| **Operating contract** | `ai-build-operating-contract.md` v3.0 (`CONTRACT_VERSION = "3.0.0"`) |
| **Directory Rules** | v1.3 (renderer-decision refresh) |
| **Repository state** | UNKNOWN — no repo mounted this session; all path / route / file-presence claims are **PROPOSED** |

---

## Contents

- [1. Scope and intent](#1-scope-and-intent)
- [2. Status snapshot](#2-status-snapshot)
- [3. Pipeline and backlog flow](#3-pipeline-and-backlog-flow)
- [4. Feature backlog](#4-feature-backlog)
- [5. Verification backlog](#5-verification-backlog)
- [6. Validator and test backlog](#6-validator-and-test-backlog)
- [7. Cross-lane backlog](#7-cross-lane-backlog)
- [8. Pass 18 expansion ideas (FIE category)](#8-pass-18-expansion-ideas-fie-category)
- [9. Sensitivity, rights, and sovereignty backlog](#9-sensitivity-rights-and-sovereignty-backlog)
- [10. Open ADRs that gate this backlog](#10-open-adrs-that-gate-this-backlog)
- [11. Risks and mitigations](#11-risks-and-mitigations)
- [12. Thin-slice plan](#12-thin-slice-plan)
- [13. Process for adding or closing a backlog item](#13-process-for-adding-or-closing-a-backlog-item)
- [Open questions register](#open-questions-register)
- [Open verification backlog](#open-verification-backlog)
- [Changelog](#changelog)
- [Definition of done](#definition-of-done)
- [14. Related docs](#14-related-docs)

---

## 1. Scope and intent

This document is the **forward-work register** for the Archaeology and Cultural Heritage domain. It collects, in one place:

- features the domain plans to build or extend,
- verification gaps that block confident implementation claims,
- validator / test work that must precede public release,
- cross-lane edges with other KFM domains,
- Pass 18 idea-index cards relevant to archaeology, and
- the open architectural questions (ADRs) that gate any of the above.

**What this backlog is not.** It is not a release plan, not an ADR, not a policy decision, and not the schema home for any archaeology object family. Backlog entries describe candidate work; nothing here promotes itself to canon. Promotion remains a governed state transition, not a file move. **CONFIRMED doctrine** per Directory Rules §3 and Atlas v1.1 §8 (Pipeline Gate Reference).

**Scope of the Archaeology domain itself.** **CONFIRMED doctrine / PROPOSED implementation:** the domain owns `ArchaeologicalSite`, `Survey`, `Artifact`, `Feature`, `Context`, `ExcavationUnit`, `RemoteSensingAnomaly`, `LiDARCandidate`, `GeophysicsObservation`, `ThreeDDocumentation`, `CulturalReview`, `StewardReview`, `CollectionAccession`, `ChronologyAssertion`, and `SensitivityTransform`. It explicitly **does not** own Roads/Rail, People/Land, Geology, Hazards, or Spatial Foundation; those lanes provide context but cannot confirm sites or bypass archaeological sensitivity.

**Conformance language.** Normative terms in this document — MUST, MUST NOT, SHOULD, SHOULD NOT, MAY — follow RFC 2119 / RFC 8174 as interpreted by `ai-build-operating-contract.md` §5.1.1: **MUST / MUST NOT** are non-negotiable; **SHOULD / SHOULD NOT** require a brief justification when deviated from (record it in a backlog-row note or in `docs/registers/DRIFT_REGISTER.md`); **MAY** is permitted with no justification required.

> [!IMPORTANT]
> Exact archaeological site locations are denied by default. Burial, human remains, sacred sites, unresolved cultural sensitivity, collection security, private-landowner details, and looting-risk exposure **fail closed**. Per operating contract §23.2, archaeology site locations `DENY` exact coordinates and **generalize to county/region**; burial / sacred sites `DENY` exact location. No backlog item in this document loosens that posture; items that touch sensitive geometry MUST route through steward review and a recorded `SensitivityTransform` before promotion.

[↑ back to top](#contents)

---

## 2. Status snapshot

The table below separates what KFM doctrine treats as **CONFIRMED** from what current-session evidence can only support as **PROPOSED** or worse. The Atlas v1.0 / v1.1 dossiers carry doctrine; current-session repository evidence is **UNKNOWN** because no repo is mounted.

| Layer | Status | Source of confidence |
|---|---|---|
| Domain mission and boundary | **CONFIRMED doctrine** | Encyclopedia §7.13; Atlas v1.1 §15.A–B |
| Object families and ubiquitous language | **CONFIRMED doctrine / PROPOSED field realization** | Atlas v1.1 §15.C–E |
| Cross-lane relations | **CONFIRMED doctrine / PROPOSED** | Atlas v1.1 §15.F, §24.4.13 |
| Pipeline shape (RAW → PUBLISHED) | **CONFIRMED doctrine / PROPOSED lane application** | Directory Rules §0, §3; Atlas v1.1 §15.H, §8 |
| Sensitivity tier defaults (T4 for exact coords; T1 only after steward review) | **CONFIRMED doctrine** | Atlas v1.1 §24.5; operating contract §23.2; MapLibre Master ML-061-159 |
| Public site-geometry floor (generalize to county/region) | **CONFIRMED doctrine** | operating contract §23.2 |
| Schema home — canonical `schemas/contracts/v1/domains/archaeology/` (DR §12); shorthand `schemas/contracts/v1/archaeology/` in some Atlas crosswalks | **PROPOSED** (canonical per ADR-0001 + DR §12); shorthand **CONFLICTED** pending ADR | Directory Rules v1.3 §12 / §7.4; Atlas v1.1 §24.13 row 15 |
| Policy home (`policy/sensitivity/archaeology/…`) | **PROPOSED** | Atlas v1.1 §24.13 row 15; Directory Rules §10/§12 |
| Specific routes / DTOs / runtime behavior | **UNKNOWN** (route TBD; pending mounted-repo inspection) | Atlas v1.1 §15.J |
| Test, fixture, and validator presence | **NEEDS VERIFICATION** | Atlas v1.1 §15.K |
| Steward identity, separation-of-duties, rollback drill | **NEEDS VERIFICATION** | Atlas v1.1 §15.N |

> [!NOTE]
> Truth labels in this document follow the label set codified in `ai-build-operating-contract.md` §8 and `docs/doctrine/authority-ladder.md` §7: **CONFIRMED**, **INFERRED**, **PROPOSED**, **UNKNOWN**, **NEEDS VERIFICATION**, **CONFLICTED**, **LINEAGE**, **EXPLORATORY**, **EXTERNAL**. Runtime outcomes (`ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, `NARROWED`, `BOUNDED`, `SOURCE_STALE`) are not used here as authoring labels; they appear only as expected behavior in validator and runtime references.

[↑ back to top](#contents)

---

## 3. Pipeline and backlog flow

The archaeology pipeline follows the universal lifecycle invariant — `RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED` — with no domain shortcut and no direct path from `RAW` to `PUBLISHED`. Backlog items map to specific gates; nothing in the backlog can re-order them.

```mermaid
flowchart LR
  subgraph BACKLOG["Backlog (this document)"]
    direction TB
    F["Feature candidates<br/><i>PROPOSED</i>"]
    V["Verification gaps<br/><i>NEEDS VERIFICATION</i>"]
    A["Open ADRs<br/><i>blocking</i>"]
    P["Pass 18 ideas<br/><i>PROPOSED expansion</i>"]
  end

  subgraph PIPE["Archaeology pipeline (CONFIRMED doctrine)"]
    direction LR
    RAW["RAW"] --> WQ["WORK /<br/>QUARANTINE"] --> PROC["PROCESSED"] --> CAT["CATALOG /<br/>TRIPLET"] --> PUB["PUBLISHED"]
  end

  subgraph GATES["Governed gates"]
    direction TB
    G1["SourceDescriptor +<br/>rights / sensitivity tag"]
    G2["TransformReceipt +<br/>ValidationReport +<br/>PolicyDecision"]
    G3["EvidenceBundle +<br/>RedactionReceipt"]
    G4["CatalogMatrix +<br/>graph / triplet"]
    G5["ReleaseManifest / MapReleaseManifest +<br/>RollbackCard +<br/>ReviewRecord"]
  end

  F -.promotes only via.-> A
  V -.unblocks promotion of.-> F
  P -.feeds.-> F
  A -.precedes.-> PIPE

  RAW -.- G1
  WQ -.- G2
  PROC -.- G3
  CAT -.- G4
  PUB -.- G5

  classDef confirmed fill:#dff5e3,stroke:#2ea043,color:#000;
  classDef proposed  fill:#ffe9cc,stroke:#cc6a00,color:#000;
  classDef unknown   fill:#f1f3f5,stroke:#8a8a8a,color:#000,stroke-dasharray:4 3;
  class RAW,WQ,PROC,CAT,PUB confirmed;
  class F,V,A,P proposed;
  class G1,G2,G3,G4,G5 unknown;
```

> [!NOTE]
> Gate labels above represent the **PROPOSED minimum** artifact set per Atlas v1.1 §8 (Master Pipeline Gate Reference). For archaeology map layers, §23.2 names `MapReleaseManifest` (with `RedactionReceipt` + `PolicyDecision`) as the release-gate receipt set. Whether each gate is implemented as code in the current repository remains **NEEDS VERIFICATION**.

[↑ back to top](#contents)

---

## 4. Feature backlog

These rows extend the Encyclopedia §7.13.L feature backlog and re-state it with archaeology-specific language and current-session truth labels. Every row is **PROPOSED** unless mounted-repo evidence raises it.

| Group | Feature | Actor / action | Evidence needed | Risk | Validation path | Status |
|---|---|---|---|---|---|---|
| Build first | Archaeology source registry + no-network fixture | steward / developer | `SourceDescriptor` + synthetic fixture | rights / source-role ambiguity | schema, source, rights validators | **PROPOSED** |
| Build first | Archaeology Evidence Drawer inspector for one generalized feature | public / researcher / steward | `EvidenceBundle` for one feature | uncited public claim | evidence-closure + citation tests | **PROPOSED** |
| Build first | Candidate-vs-confirmed UI distinction for `RemoteSensingAnomaly` / `LiDARCandidate` | public / researcher | candidate-not-site label rule | reading a candidate as a confirmed site | candidate-not-site fixture tests | **PROPOSED** |
| Build first | Public generalized site-summary tile (T1) wired to a `RedactionReceipt` (geometry generalized to county/region per §23.2) | public / steward | `RedactionReceipt` + `ReviewRecord` | exact-coordinate leak | sensitive-geometry no-leak tests | **PROPOSED** |
| After proof lane | Archaeology time slider + compare mode | researcher / steward | versioned observations / layers | false temporal alignment | temporal-logic tests | **PROPOSED** |
| After proof lane | Survey-coverage public summary (`SurveyProject` / `SurveyTransect`) | researcher / steward | survey extents + coverage stats | implying confirmed sites in unsurveyed gaps | coverage-vs-find rate tests | **PROPOSED** |
| After proof lane | Chronology / `ChronologyAssertion` timeline view with EDTF + OWL-Time alignment | researcher / steward | chronology assertions + uncertainty bands + calendar flag on Julian dates | overconfident period bands; implicit timezone | uncertainty-band tests; EDTF validity tests | **PROPOSED** |
| Ambitious / research | Cross-domain archaeology analytics and graph queries (with Roads / Settlements / Hazards) | researcher / AI assistant | source-backed triples + model receipts | derivative becomes truth | graph projection tests; cross-lane join policy | **PROPOSED** |
| Ambitious / research | 3D site documentation admission lane (`ThreeDDocumentation` + Scene Manifest) | steward | 3D admission policy + reality-boundary note | photorealism read as observation | 3D admission validator; renderer-boundary tests | **PROPOSED** (gated by **ADR-S-07**) |
| **DENY by default** | Unreviewed exact sensitive archaeology locations or private collection joins | public visitor | policy approval + `RedactionReceipt` | privacy / cultural / public-safety harm | policy deny tests | **DENY** *(runtime outcome — not a candidate)* |

> [!WARNING]
> The bottom row is not a "future feature." It is a permanent **DENY** lane, named here so that no later proposal accidentally reframes it as a backlog item to be unlocked. Any change that would soften this row requires an ADR routed through the rights-holder representative.

[↑ back to top](#contents)

---

## 5. Verification backlog

These items are taken directly from Atlas v1.1 §15.N and the Encyclopedia Appendix J / Appendix K, scoped to archaeology. Each is **NEEDS VERIFICATION** until mounted-repo or steward-review evidence settles it.

| ID *(local)* | Item to verify | Evidence that would settle it | Blocking | Status |
|---|---|---|---|---|
| ARCH-VER-01 | Steward authority and confidentiality scope for Archaeology lane | named stewards in repo governance; `ReviewRecord` examples | T1 / T2 publication of any site-derived summary | **NEEDS VERIFICATION** |
| ARCH-VER-02 | Public geometry thresholds relative to the §23.2 county/region floor — op-contract §23.2 names **county/region** as the authoritative floor; lane-local refinements (H3 r7 minimum; ≥5 km terrain generalization near sites) are **PROPOSED** tighter values | a published `policy/sensitivity/archaeology/` profile; fixture tests; §23.2 reconciliation | any generalized public layer | **NEEDS VERIFICATION** |
| ARCH-VER-03 | Oral history and cultural-knowledge handling protocol | a recorded protocol + steward sign-off + rights record | admission of oral-history sources | **NEEDS VERIFICATION** |
| ARCH-VER-04 | Emergency public-layer disablement and rollback drill | a dry-run drill log + `RollbackCard` artifact | any `PUBLISHED` archaeology layer | **NEEDS VERIFICATION** |
| ARCH-VER-05 | LiDAR vertical datum and vintage handling for candidate anomalies | terrain manifest test + vintage field on `LiDARCandidate` | promoting `LiDARCandidate` to `CandidateFeature` | **NEEDS VERIFICATION** |
| ARCH-VER-06 | Schema home for archaeology object families — canonical `schemas/contracts/v1/domains/archaeology/` per Directory Rules v1.3 §12; the shorthand `schemas/contracts/v1/archaeology/` (no `domains/` segment) appearing in some Atlas crosswalks is CONFLICTED | a tree under the canonical path + ADR-0001 confirmation; ADR reconciling the shorthand | every schema-tagged item below | **NEEDS VERIFICATION** *(pending **ADR-S-01**)* |
| ARCH-VER-07 | Specific governed-API route and DTO names for archaeology resolvers | route table or OpenAPI doc under `apps/governed-api/…` | runtime claims; client wiring | **UNKNOWN** |
| ARCH-VER-08 | Whether `policy/sensitivity/archaeology/` exists and is the canonical home (vs. `policies/`) | mounted-repo inspection; per-root README | every sensitivity claim below | **NEEDS VERIFICATION** *(pending **ADR-S-05**)* |
| ARCH-VER-09 | `ChronologyAssertion` temporal compliance (EDTF validity, OWL-Time mapping, CIDOC CRM E52 alignment, no implicit timezone, calendar flag on Julian dates) | temporal-validator fixture pass + cross-lane reference to temporal doctrine | any chronology-bearing surface (timeline view, period overlays, time slider) | **NEEDS VERIFICATION** |
| ARCH-VER-10 | Contracts-home segment — canonical `contracts/domains/archaeology/` per Directory Rules v1.3 §12; the bare `contracts/archaeology/` form matches the DR §12 CONFLICTED anti-pattern symptom | DR §12 confirmation; ADR if the bare form is ever intended | every semantic-contract reference | **NEEDS VERIFICATION** |

[↑ back to top](#contents)

---

## 6. Validator and test backlog

The Atlas v1.1 §15.K names seven **PROPOSED** validator classes for Archaeology. This backlog tracks each as a separate work item, with the fixture posture that should accompany it.

| ID *(local)* | Validator / test class | Purpose | Required fixtures | Status |
|---|---|---|---|---|
| ARCH-TST-01 | `EvidenceBundle`-required tests | refuse archaeology claims that lack a resolvable `EvidenceRef` → `EvidenceBundle` chain | positive (resolves) + negative (broken ref, missing bundle) | **PROPOSED** |
| ARCH-TST-02 | Candidate-not-site tests | refuse promotion of a `RemoteSensingAnomaly` or `LiDARCandidate` as a confirmed `ArchaeologicalSite` without `StewardReview` | candidate fixture + missing-review fixture | **PROPOSED** |
| ARCH-TST-03 | Public no-leak tests | refuse public emission of restricted fields (exact coords, internal identifiers, sensitive joins) | restricted-field corpus + redaction acceptance fixture | **PROPOSED** |
| ARCH-TST-04 | Rights and cultural-review tests | refuse promotion when `CulturalReview` / rights-holder representative sign-off is missing where required | review-present + review-absent fixtures | **PROPOSED** |
| ARCH-TST-05 | Exact sensitive geometry denial | refuse geometry finer than the §23.2 county/region floor (and any tighter ADR-ratified lane floor, e.g. sub-H3-r7 once **ADR-S-05** lands) for sensitive lanes | sub-floor geometry fixtures | **PROPOSED** |
| ARCH-TST-06 | Catalog closure tests | refuse release when `CatalogMatrix` entry, digests, or triplet projections do not close | closure-pass + closure-fail fixtures | **PROPOSED** |
| ARCH-TST-07 | AI exact-location denial | refuse AI generation of exact archaeology coordinates regardless of prompt phrasing | adversarial prompt fixtures + `AIReceipt` audit | **PROPOSED** |
| ARCH-TST-08 | Cultural-symbol policy tests *(from MapLibre ML-061 family)* | refuse style rules that use sacred symbols or tribal insignia for archaeology layers | symbol-set linter fixture | **PROPOSED** |
| ARCH-TST-09 | `PublicationTransformReceipt` parity tests | verify that every public archaeology artifact has a transform receipt that names method, threshold, and reviewer | receipt-present + receipt-missing fixtures | **PROPOSED** |
| ARCH-TST-10 | `ChronologyAssertion` temporal-validity tests | refuse chronology records that fail EDTF parsing, carry implicit timezones, or assert Julian dates without a calendar flag | EDTF-valid fixture + EDTF-invalid fixture + tz-naive fixture + Julian-no-flag fixture | **PROPOSED** |

> [!TIP]
> The Encyclopedia §7.13.K test list applies uniformly across domains; the archaeology-specific additions are ARCH-TST-02, ARCH-TST-05, ARCH-TST-07, ARCH-TST-08, and ARCH-TST-10. When a shared validator covers both archaeology and another lane (notably temporal validators shared with the chronology / time lane), prefer placement under `tools/validators/<topic>/…` per Directory Rules §12 "Multi-domain and cross-cutting files." Fixtures follow Directory Rules **§6.6**: you MAY keep them under `tests/fixtures/` instead of root `fixtures/`, but MUST NOT maintain two competing fixture homes unless both READMEs state the difference.

[↑ back to top](#contents)

---

## 7. Cross-lane backlog

These edges are owned by Archaeology and are restated here as backlog rows so the work is trackable per related lane. Each edge MUST preserve ownership, source role, sensitivity, and `EvidenceBundle` support. **CONFIRMED doctrine / PROPOSED implementation** throughout, per Atlas v1.1 §15.F and §24.4.13 ("Edges owned by Archaeology / Cultural Heritage").

| Related lane | Relation (CONFIRMED doctrine) | Backlog work | Status |
|---|---|---|---|
| Spatial Foundation | Exact / public geometry split + transform receipts | Profile every public geometry with a `PublicationTransformReceipt`; record method + threshold; generalize to the §23.2 county/region floor | **PROPOSED** |
| Roads / Rail / Trade Routes | Historic routes and cultural paths | Bind site interpretation to historic route evidence; deny exact coords; allow generalized corridor overlays only | **PROPOSED** |
| Settlements / Infrastructure | Forts, missions, townsites, reservation communities | Cultural temporal period + survey context anchors historical settlement interpretation; site coords denied | **PROPOSED** |
| Hazards | Threat / erosion / fire / flood / exposure context | Hazard exposure may inform threat ranking for sensitive sites; KFM is **never** an alert authority for archaeology | **PROPOSED** |
| Planetary / 3D | Sites admitted only via steward-reviewed, generalized 3D representation with reality-boundary note; sole renderer `packages/maplibre-runtime/`; 3D schemas at `schemas/contracts/v1/3d/` (Directory Rules v1.3) | 3D admission lane (`ThreeDDocumentation` + Scene Manifest); reality-boundary note required | **PROPOSED** *(gated by **ADR-S-07**)* |
| People / Genealogy / Land | Cultural affiliations cited with rights, sovereignty, and steward review | Indigenous community context: steward-reviewed, rights-bounded; living-person fields fail closed | **PROPOSED** |
| Time / Temporal doctrine | `ChronologyAssertion` and event-bearing records align with EDTF, OWL-Time, CIDOC CRM E52, Allen interval algebra, STAC datetime fields, and W3C PROV-O | Reuse shared temporal validators; uncertainty bands MUST be visible in any public chronology surface | **PROPOSED** |
| Frontier Matrix | (Inbound) Settlement-status cells may reference archaeology context generalized | Verify generalization sufficiency before any matrix snapshot carries an archaeology-derived field | **NEEDS VERIFICATION** |

[↑ back to top](#contents)

---

## 8. Pass 18 expansion ideas (FIE category)

The Pass 18 Idea Index assigns **59 cards** to the **FIE — Field Capture, Remote Sensing, 3D, and Archaeological Interpretation** category. The subset below is the slice most relevant to archaeology promotion candidates. Each card is **PROPOSED** with **UNKNOWN** implementation maturity (no current-session repo evidence proves any card is already implemented).

<details>
<summary><b>Archaeology-relevant Pass 18 FIE cards (click to expand)</b></summary>

<br/>

| Card ID | Title (normalized) | Carry state | Backlog implication |
|---|---|---|---|
| KFM-P18-INV-016 | 3D archaeology as evidence-rich spatial analysis | NEW | Define a `3DAssetAcquisitionReceipt` profile (method, instrument, processing, scale, CRS, uncertainty) |
| KFM-P18-INV-017 | 2.5D versus true 3D distinction | NEW | Add a representation-mode label to scene artifacts |
| KFM-P18-INV-019 | Trowel-edge anomaly detection as reviewed field inference | NEW | Treat field inference as `CandidateFeature`, never as confirmed site |
| KFM-P18-INV-020 | Subsurface, volume, and visibility analyses as derived evidence | NEW | Volumetric / visibility outputs require derivation receipts and uncertainty fields |
| KFM-P18-INV-089 | 3D GIS should support multi-model archaeological interpretation | EXPANDED | Add `interpretation_status`, `scenario_id`, `evidence_support_level`, and rejected-alternative links |
| KFM-P18-INV-090 | Volumetric and boundary models need acquisition and analysis lineage | EXPANDED | Define a `volumetric_derivative_receipt` for legacy inputs and density calculations |
| KFM-P18-INV-091 | 3D visualization settings are analytical choices | NEW | Record visualization-settings provenance with the asset |
| KFM-P18-INV-113 | 3D visibility analysis as bounded interpretive inference | NEW | Visibility analyses must travel with their `EvidenceBundle` and method receipt |
| KFM-P18-INV-248 | Offline field-capture packages need redaction and sync receipts | EXPANDED | Field-capture lane requires redaction-on-sync and a sync `RunReceipt` |
| KFM-P18-INV-294 | Trowel-edge 3D GIS becomes field-recording evidence | NEW | On-site 3D capture must record acquisition, scale, georeference, revision, and analyst |
| KFM-P18-INV-363 | Surface and subsurface 3D analysis as layered evidence rather than a single scene | EXPANDED | Separate surface, subsurface, point-cloud-derived, volume, and analysis layers |
| KFM-P18-INV-452 | Remote-sensing resolution metadata for raster and imagery layers | EXPANDED | Disclose sensor bands + spatial / temporal / radiometric resolution before derivative promotion |
| KFM-P18-INV-485 | 2.5D versus true 3D representation labels | NEW | Label elevation / scene artifacts as 2D, 2.5D, or true 3D where the distinction affects interpretation |
| **KFM-P18-INV-005** *(source-level)* | Surface / subsurface 3D analyses record preservation state, threat context, method, morphology-change | NEW | Add `preservation_state` and `threat_context` fields to archaeology 3D analysis records |

The Pass 18 Idea Index identifies the FIE category as containing **59 cards total**; rows above are the archaeology-relevant subset selected from Phase 5 batches 001, 003, 004, 010, 012, 015, 019, and 020. The remaining FIE cards primarily concern hazards, remote sensing of other phenomena, or generic 3D representation issues outside Archaeology's owning domain.

</details>

> [!NOTE]
> Pass 18 cards are inventory-level planning candidates with **CONFIRMED** source support but **UNKNOWN** repository implementation. They do not promote themselves to schema, contract, or policy entries; each MUST travel through the normal admission, validation, and ADR (where structural) gates before any path-shaped claim is made. The 3D-asset cards land their schemas under `schemas/contracts/v1/3d/` (Directory Rules v1.3 §6.4), not under the domain schema segment.

[↑ back to top](#contents)

---

## 9. Sensitivity, rights, and sovereignty backlog

The Archaeology lane is one of the highest-sensitivity lanes in KFM. The default tier is **T4** (fail-closed); generalized public release at **T1** requires `RedactionReceipt` + `ReviewRecord`. Tier transitions follow Atlas v1.1 §24.5 — upgrade (toward more public) always requires both a transform receipt and a review record; downgrade (toward less public) needs only a `CorrectionNotice`.

> [!CAUTION]
> This section governs the lane's hardest line. Every row below MUST be read against `ai-build-operating-contract.md` §23.2 (sensitive-domain decision matrix). When a row in this backlog and a row in §23.2 disagree, **the operating contract wins** and the conflict MUST be logged in `docs/registers/DRIFT_REGISTER.md`. Per §23.2: archaeology site locations `DENY` exact coordinates and **generalize to county/region** (reviewers: tribal/cultural + rights-holder rep; receipts `RedactionReceipt` + `PolicyDecision` + `MapReleaseManifest`); burial / sacred sites `DENY` exact location.

| Concern | Doctrine source | Backlog work | Status |
|---|---|---|---|
| Exact site coordinates fail closed by default; public floor is county/region | operating contract §23.2; Atlas v1.1 §15.I; Encyclopedia §7.13.M | Reify in `policy/sensitivity/archaeology/` once **ADR-S-05** lands | **PROPOSED** |
| Geometry below H3 r7 prohibited for sensitive archaeology products without review *(PROPOSED lane refinement tighter than the §23.2 county/region floor)* | MapLibre Master ML-061-159 | Implement and fixture-test the threshold; record per-feature `transform_method`; reconcile against §23.2 | **PROPOSED** |
| Terrain near archaeological locations needs ≥5 km coordinate generalization *(PROPOSED lane refinement)* | MapLibre Master ML-059-055 | Encode in terrain manifest; require `RedactionReceipt` with method + scale | **PROPOSED** |
| CARE labels and sovereignty notice chips required in UI | MapLibre Master ML-061-160 | Wire `CulturalReview` outcome to Evidence Drawer and Focus Mode chips | **PROPOSED** |
| Cultural symbols MUST avoid sacred symbols / tribal insignia and use neutral accessible vector forms | MapLibre Master ML-059-058 | Symbol-set linter (ARCH-TST-08) + steward-approved symbol catalog | **PROPOSED** |
| Focus Mode MUST be sovereignty-aware and explain which evidence influenced answers | MapLibre Master ML-061-162 | Bind Focus Mode templates to `AIReceipt` + sovereignty gating; audit `ABSTAIN` and `DENY` rates | **PROPOSED** |
| Generalization logs are validation evidence for sensitive map products | MapLibre Master ML-061-161 | Emit generalization logs alongside published tiles; admit them as `ValidationReport` inputs | **PROPOSED** |
| Steward authority and confidentiality scope | Atlas v1.1 §15.N row 1; §24.7 (Reviewer roles) | Name a domain steward, sensitivity reviewer, and rights-holder representative for this lane | **NEEDS VERIFICATION** |
| Oral history and cultural-knowledge protocol | Atlas v1.1 §15.N row 3 | Draft a protocol with rights-holder co-authoring; record admission criteria | **NEEDS VERIFICATION** |
| Living-person and DNA fields appearing alongside archaeology context | People-lane doctrine via Atlas v1.1 §24.4.14 | Cross-lane join policy MUST deny living-person joins through archaeology surfaces by default | **PROPOSED** *(gated by **ADR-S-14**)* |
| Ingested archaeology source files (PDF reports, scraped HTML, field notes) treated as inert data per `ai-build-operating-contract.md` §12 | Operating contract §12 (untrusted-content rule) | Add a pre-admission lint that flags imperative AI-directed strings in incoming archaeology documents and routes them to steward review without acting on them | **PROPOSED** |

[↑ back to top](#contents)

---

## 10. Open ADRs that gate this backlog

These ADRs are drawn from the **Master Open-ADR Backlog** in Atlas v1.1 §24.12. They are **PROPOSED** at the Atlas level; none has been observed accepted in this session. Each blocks at least one backlog row above.

| ADR | Question | Blocks |
|---|---|---|
| **ADR-S-01** | Where is the canonical schema home? (Default: `schemas/contracts/v1/domains/<domain>/` per ADR-0001 + Directory Rules v1.3 §12; the bare `schemas/contracts/v1/<domain>/` shorthand is CONFLICTED.) | ARCH-VER-06; ARCH-VER-10; every schema-shaped backlog row |
| **ADR-S-03** | Receipt class home: shared `schemas/contracts/v1/receipts/` vs. per-domain `schemas/contracts/v1/domains/<domain>/receipts/` | `RedactionReceipt`, `PublicationTransformReceipt`, `RunReceipt`, `GENERATED_RECEIPT.json` placement |
| **ADR-S-05** | Sensitivity tier scheme (T0–T4) — adopt as canonical or revise; reconcile any tighter lane floor (H3 r7 / 5 km) against the §23.2 county/region floor | All sensitivity rows in §9; ARCH-TST-05; ARCH-VER-02 |
| **ADR-S-07** | 3D admission policy: minimum required receipts, deny lanes, reality-boundary disclosure; 3D schema home `schemas/contracts/v1/3d/` (v1.3) | 3D admission lane in §4; `ThreeDDocumentation` rows in §7 and §8 |
| **ADR-S-09** | Reviewer role separation: when is separation enforced by tooling vs. custom | Steward authority items in §5 and §9 |
| **ADR-S-10** | Stale-state propagation: how does a stale upstream propagate to downstream claims | Time-slider and matrix-snapshot rows in §4 and §7 |
| **ADR-S-14** | Cross-lane join policy: which joins require steward review, which are denied, which are open | Cross-lane work in §7; living-person row in §9 |
| **OPEN-DR-10** *(Directory Rules v1.3 §18.e)* | MapLibre as sole browser-side renderer — governs the 3D archaeology handoff and `packages/maplibre-runtime/` placement | 3D admission lane in §4; Planetary/3D row in §7 |

> [!CAUTION]
> Any row that depends on an open ADR **MUST NOT** be implemented as if the ADR is already resolved. Pre-emptive implementation is one of the placement and authority anti-patterns named in Atlas v1.1 §24.9.1; it hardens drift into canon.

[↑ back to top](#contents)

---

## 11. Risks and mitigations

These rows specialize the Encyclopedia §7.13.M risk register to the archaeology lane. They are **CONFIRMED doctrine** at the risk level; specific mitigation implementations are **PROPOSED**.

| Risk | Mitigation (PROPOSED) |
|---|---|
| Rights uncertainty | Block public release until source terms and redistribution class are recorded on the `SourceDescriptor` |
| Sensitive-location exposure | Default redaction / generalization to the §23.2 county/region floor; restricted views; geoprivacy transform receipts; tighter H3-r7 lane refinement where ratified |
| False precision | Show uncertainty / support, scale and source-role badges; `ABSTAIN` on over-precise claims |
| Source-authority confusion (observation vs. model vs. authority record) | Source-role registry; separate observation / model / authority / context contexts at the `SourceDescriptor` |
| Model hallucination | Citation validation; finite outcomes (`ANSWER` / `ABSTAIN` / `DENY` / `ERROR`); no direct model-to-public path |
| Stale data | Freshness badges; retrieval / source / release time fields; stale-state policy with downstream propagation; emit `SOURCE_STALE` where applicable |
| Rollback complexity | `ReleaseManifest` + `RollbackCard` + a periodic rollback drill for every public layer |
| Candidate-as-confirmed drift | Candidate-not-site fixture tests (ARCH-TST-02); UI label discipline; reviewer separation |
| Photorealistic 3D read as direct observation | Reality-boundary note on every admitted 3D asset; representation-mode label (KFM-P18-INV-485) |
| Temporal misalignment (implicit timezone; un-flagged Julian dates; EDTF-invalid strings) | EDTF-validity tests (ARCH-TST-10); calendar flag required on Julian dates; OWL-Time mapping for interval logic; uncertainty bands on every `ChronologyAssertion` public surface |
| Prompt injection inside ingested archaeology source files | Pre-admission lint per §9; surface to steward review, do not act |
| Placement drift — domain folder forms that omit the `domains/` segment (`contracts/archaeology/`, `schemas/contracts/v1/archaeology/`) | Use the Directory Rules v1.3 §12 canonical forms (`contracts/domains/archaeology/`, `schemas/contracts/v1/domains/archaeology/`); log any divergence in `docs/registers/DRIFT_REGISTER.md` (ARCH-VER-06, ARCH-VER-10) |

[↑ back to top](#contents)

---

## 12. Thin-slice plan

The Encyclopedia §7.13 thin-slice for Archaeology — **CONFIRMED** as a doctrinal slice, **PROPOSED** as an implementation candidate — is:

> *Synthetic archaeology candidate fixture with exact geometry denied, public generalized tile, steward review record, and correction / rollback path.*

Restated as a checklist of artifacts the slice must produce (each **PROPOSED**):

- a synthetic `RemoteSensingAnomaly` and a synthetic `LiDARCandidate` fixture with deliberately invented coordinates,
- a `SourceDescriptor` for the synthetic source family,
- a `TransformReceipt` and `RedactionReceipt` showing generalization to the §23.2 county/region floor (tighter H3-r7 lane refinement applied where ratified),
- a `CandidateFeature` record that does **not** assert it is an `ArchaeologicalSite`,
- a public generalized vector tile served only through the governed API path,
- a `ReviewRecord` showing steward sign-off on the generalization,
- a `ReleaseManifest` + `RollbackCard` (and a `MapReleaseManifest` per §23.2 for the map layer),
- a dry-run rollback drill that restores the prior manifest,
- a `CorrectionNotice` round-trip showing a downgrade from a generalized state back to restricted,
- a `ChronologyAssertion` attached to the candidate with an EDTF-valid uncertain date and an explicit timezone or `Z`-anchored value.

> [!IMPORTANT]
> The thin slice's purpose is to prove the **trust membrane**, not to publish data. No real archaeology source MUST be admitted by this slice; all inputs MUST be deliberately synthetic until the verification rows in §5 are closed.

[↑ back to top](#contents)

---

## 13. Process for adding or closing a backlog item

Every change to this file should preserve the doctrine-to-implementation separation. A short discipline (PROPOSED for this document; not yet codified in repo tooling):

1. **Adding a row.** New rows arrive **PROPOSED** with at least one citation to project doctrine (Atlas, Encyclopedia, Pass 18 card, Directory Rules) or to a steward-recorded need. Rows without doctrine grounding belong in a discussion, not here.
2. **Promoting a row.** A backlog row does not become canon by being implemented. It promotes by: (a) the relevant ADR landing, (b) the artifact appearing in the repo at the **PROPOSED** path with a `ReviewRecord`, and (c) the matching validator producing a passing fixture run.
3. **Closing a row.** When closed, the row stays in the file with status `CLOSED` and a forward link to the artifact that closed it (ADR id, PR url, or release id). Removing rows silently is treated as drift.
4. **Conflicts.** If a row conflicts with a row in `docs/registers/VERIFICATION_BACKLOG.md` or with an accepted ADR, the ADR wins; if a row conflicts with Atlas v1.0 / v1.1, the Atlas governs and the conflict is logged in `docs/registers/DRIFT_REGISTER.md`. If a row conflicts with `ai-build-operating-contract.md` v3.0, the contract wins and the row becomes `CONFLICTED` until an ADR resolves it. When Directory Rules and an Atlas crosswalk disagree on a path (e.g., the `domains/` segment), Directory Rules v1.3 §12 governs and the conflict surfaces an ADR obligation.
5. **Cadence.** Recommend a quarterly steward review of this file with the open-ADR backlog open in another tab. Aging entries past two reviews without progress are candidates for explicit closure as `WONTFIX`, with reason.
6. **Receipts.** Any AI-authored revision to this file SHOULD produce a `GENERATED_RECEIPT.json` per `ai-build-operating-contract.md` §34, pinning `CONTRACT_VERSION = "3.0.0"`. A receipt with `human_review.state == "pending"` is well-formed but NOT mergeable until reviewed.

> [!TIP]
> Backlog hygiene is part of the trust posture, not extra paperwork. A stale backlog is one of the documentation drift signals named in Atlas v1.1 §24.11.5.

[↑ back to top](#contents)

---

## Open questions register

These are smaller, doc-scoped questions that sit below the formal ADRs in §10 but still need an owner and a resolution path. They are not architecture decisions; they are discipline decisions about how this backlog itself should behave.

| ID | Question | Owner role | Resolution path |
|---|---|---|---|
| OQ-ARCH-EXP-01 | Should backlog reviews be formalized at a fixed quarterly cadence with a docs-steward sign-off, or kept advisory until the lane reaches its first PROPOSED implementation? | Docs steward + Archaeology steward | Backlog-hygiene policy entry under `docs/registers/` (PROPOSED); promote to ADR if discipline becomes contract-grade |
| OQ-ARCH-EXP-02 | When this backlog accumulates more than ~50 entries, should it be split by sub-domain (LiDAR / remote sensing vs. survey / excavation vs. cultural review) or kept consolidated for cross-row visibility? | Archaeology steward | Re-evaluation at the next quarterly review with row count and reviewer time-on-doc |
| OQ-ARCH-EXP-03 | Does `ChronologyAssertion` validation belong in `tests/domains/archaeology/` or in a shared temporal-validators home alongside EDTF / OWL-Time / Allen-interval tests? | Archaeology steward + Temporal-doctrine owner | ADR-S-01 (schema home) + cross-reference to temporal doctrine docs |
| OQ-ARCH-EXP-04 | Should this backlog enumerate per-row `RuntimeResponseEnvelope` expectations (`ANSWER` / `ABSTAIN` / `DENY` / `NARROWED` / `BOUNDED` mix) for the candidate-vs-confirmed UI, or is that the runtime contract's job? | Archaeology steward + Contracts owner | Runtime contract review; reference, do not duplicate |
| OQ-ARCH-EXP-05 | Is a `CLOSED` row that links to a landed artifact authoritative for downstream readers, or does it require a parallel entry in `docs/registers/VERIFICATION_BACKLOG.md` for canonicity? | Docs steward | Closure-rule clarification in §13 Process; possibly an ADR |
| OQ-ARCH-EXP-06 | When ingested archaeology source content contains an apparent AI-directed instruction, where does the lint result live — on the `SourceDescriptor`, on a parallel `IngestionFlag` record, or in a `ReviewRecord` queue? | Archaeology steward + Contracts owner | Operating contract §12 cross-reference; admission-pipeline ADR if needed |
| OQ-ARCH-EXP-07 | The bare `contracts/archaeology/` and `schemas/contracts/v1/archaeology/` forms (no `domains/` segment) appear in some Atlas §24.13 crosswalk rows but conflict with Directory Rules v1.3 §12. Which governs the physical tree? | Archaeology steward + Docs steward | Directory Rules v1.3 §12 governs (canonical `domains/` segment); reconcile the crosswalk via ADR (ARCH-VER-06, ARCH-VER-10) |

[↑ back to top](#contents)

---

## Open verification backlog

The verification backlog for this lane is enumerated above in [§5](#5-verification-backlog) — rows **ARCH-VER-01** through **ARCH-VER-10**. Each row remains `NEEDS VERIFICATION` (or `UNKNOWN`, for routes / DTOs) until mounted-repo or steward-review evidence settles it. This document MUST NOT be promoted from `status: draft` to `status: published` until at minimum:

1. **ARCH-VER-01** (steward authority) is settled — owners are named, not placeholders.
2. **ARCH-VER-06** is settled by **ADR-S-01** landing — schema home is canonical (`schemas/contracts/v1/domains/archaeology/`), not PROPOSED, and the bare-segment shorthand is resolved.
3. **ARCH-VER-08** is settled by **ADR-S-05** landing — policy home is canonical, not PROPOSED.
4. **ARCH-VER-10** (contracts-home segment) is confirmed against Directory Rules v1.3 §12.

The remaining ARCH-VER rows may carry forward into `published` with their labels intact, provided each has at least an assigned owner.

[↑ back to top](#contents)

---

## Changelog

### v0.2 → v0.3

| Change | Type (per contract §37) | Reason |
|---|---|---|
| Named the live **Directory Rules v1.3** edition in the badge row, top-of-file table, §2 status snapshot, §7, §10, §11, and footer | reconciliation (MINOR) | The mounted-project Directory Rules header reads `Edition v1.3` (renderer-decision refresh). v0.2 cited Directory Rules without an edition; pinning it prevents silent staleness. |
| **Corrected the contracts-home path** `contracts/archaeology/` → **`contracts/domains/archaeology/`** in §14; added ARCH-VER-10 and OQ-ARCH-EXP-07 to track the segment | reconciliation (MINOR) | Directory Rules v1.3 §12 places domain semantic contracts at `contracts/domains/<domain>/`; the bare `contracts/archaeology/` form is exactly the DR §12 CONFLICTED anti-pattern symptom (divergent `contracts/<domain>/` vs `schemas/contracts/v1/domains/<domain>/`). |
| **Flagged the schema-home shorthand** `schemas/contracts/v1/archaeology/` against the canonical `schemas/contracts/v1/domains/archaeology/` (DR §12) in §2, ARCH-VER-06, ADR-S-01, §14 | reconciliation (MINOR) | DR §12 canonical form carries the `domains/` segment; the shorthand in the Atlas §24.13 crosswalk is CONFLICTED pending ADR. Not silently rewritten (the Atlas crosswalk is its source); flagged consistently with the sibling FILE_SYSTEM_PLAN treatment. |
| Named the operating contract **§23.2 county/region** generalization as the **authoritative public floor** in the §1 IMPORTANT, §2, §4, ARCH-VER-02, ARCH-TST-05, §9 (CAUTION + rows), §11, §12; reframed H3 r7 / ≥5 km as PROPOSED lane refinements | reconciliation (MINOR) | Aligns with the sibling docs' corrections; v0.2 cited H3 r7 / 5 km as operative thresholds without anchoring them to §23.2. |
| Added v1.3 3D context (`packages/maplibre-runtime/` sole renderer, `schemas/contracts/v1/3d/` schema home, OPEN-DR-10) to §7, §8, §10 | gap closure (MINOR) | Directory Rules v1.3 §6.4 / §18.e establishes the 3D schema home and sole-renderer posture; relevant to the `ThreeDDocumentation` / 3D-admission rows. |
| Noted `MapReleaseManifest` (per §23.2) in the §3 gate diagram, §3 note, §9 CAUTION, and §12 thin slice | clarification (PATCH) | §23.2 names `MapReleaseManifest` as a required receipt for archaeology map layers. |
| Added `EXPANSION_PLAN.md` and `FILE_SYSTEM_PLAN.md` to meta-block `related` | gap closure (PATCH) | Cross-link the sibling lane docs. |
| Added a placement-drift risk row to §11 | gap closure (PATCH) | Operationalize the segment-omission correction as a tracked risk. |
| Renamed the changelog section from "Changelog v0.1 → v0.2" to "Changelog" and nested the v0.1→v0.2 table beneath the new v0.2→v0.3 table | housekeeping (PATCH) | Keeps the `#changelog` anchor stable across future bumps. |
| Updated dates, badge, footer | housekeeping (PATCH) | Standard refresh. |

> **Backward compatibility (v0.2 → v0.3).** All §1–§14 anchors are **preserved**. The changelog-section anchor changed from `#changelog-v01--v02` to `#changelog` (the Contents list is updated to match; any external link to the old changelog anchor needs updating — flagged for the docs steward). New verification rows (ARCH-VER-10) and open questions (OQ-ARCH-EXP-07) are **appended**; no existing ARCH-VER / ARCH-TST / OQ id is renumbered. The contracts-home and schema-home edits are **corrections** (the bare-segment forms matched a DR §12 anti-pattern), and the §23.2-floor edits are **reconciliations** — they retire no anchor and rename no field. **MINOR** per contract §37.

### v0.1 → v0.2 (carried forward)

| Change | Type (per contract §37) | Reason |
|---|---|---|
| Added `CONTRACT_VERSION = "3.0.0"` pin to meta block, badge row, §13 process | clarification | Align with v3.0 doctrine-adjacent posture. |
| Added RFC 2119 / RFC 8174 conformance note (§1) and expanded the §2 truth-labels note | clarification | Anchor the MUST/SHOULD usage and label set. |
| Added ARCH-VER-09 (§5), ARCH-TST-10 (§6), the §7 Time/Temporal row, the §9 untrusted-content row | gap closure | Time fields and ingested content participate in the lane. |
| Added temporal-misalignment + prompt-injection risks (§11); a `ChronologyAssertion` thin-slice artifact (§12); receipt step (§13 item 6) | gap closure | Operationalize the new invariants. |
| Added Open questions register, Open verification backlog, Changelog, Definition of done | gap closure / housekeeping | Companion-section pattern. |
| Added the §9 CAUTION cross-referencing operating contract §23.2 | clarification | Make the precedence rule visible. |

[↑ back to top](#contents)

---

## Definition of done

This document is done enough to enter the repository when:

- it is placed under `docs/domains/archaeology/` per Directory Rules §12 (path is **PROPOSED** until repo evidence confirms);
- a docs steward and the named Archaeology domain steward review it, with the steward's identity recorded in `owners` (replacing the `TODO` placeholders);
- it is linked from `docs/domains/archaeology/README.md`, from the sibling [`EXPANSION_PLAN.md`](./EXPANSION_PLAN.md) and [`FILE_SYSTEM_PLAN.md`](./FILE_SYSTEM_PLAN.md), and from any docs index that routes to domain backlogs;
- it does not conflict with accepted ADRs in the §10 list — specifically **ADR-S-01**, **ADR-S-05**, **ADR-S-07**, **ADR-S-09**, **ADR-S-10**, **ADR-S-14**, and **OPEN-DR-10**;
- the Directory Rules edition cited here (**v1.3**) matches the live `docs/doctrine/directory-rules.md` edition at merge time, and the canonical domain-segment forms (`contracts/domains/archaeology/`, `schemas/contracts/v1/domains/archaeology/`) hold against §12;
- the §23.2 county/region generalization floor is honored, and any tighter lane-local floor (H3 r7 / 5 km) is resolved by ADR or logged in `docs/registers/DRIFT_REGISTER.md`;
- any conflict with current repo conventions is logged in `docs/registers/DRIFT_REGISTER.md`;
- the `GENERATED_RECEIPT.json` planned in the authoring pass (see §13 item 6) is wired into CI under `schemas/contracts/v1/receipts/generated_receipt.schema.json` (**PROPOSED** per operating contract §47), pinning `CONTRACT_VERSION = "3.0.0"`;
- at minimum **ARCH-VER-01**, **ARCH-VER-06**, **ARCH-VER-08**, and **ARCH-VER-10** are settled (see [Open verification backlog](#open-verification-backlog) above);
- future revisions follow `ai-build-operating-contract.md` §37 — **MINOR** is the default bump for row additions, label clarifications, and companion-section expansions; **MAJOR** is reserved for changes that touch the sensitivity defaults, the §23.2 / DENY-by-default lane, or the cross-lane ownership map.

[↑ back to top](#contents)

---

## 14. Related docs

Paths below are **PROPOSED** per Directory Rules v1.3 §12 and the Atlas v1.1 §24.13 crosswalk; presence and exact filenames remain **NEEDS VERIFICATION** until a repo is mounted. The canonical domain forms carry the `domains/` segment (DR §12); bare-segment variants in some Atlas crosswalk rows are CONFLICTED pending ADR (see ARCH-VER-06 / ARCH-VER-10).

- `docs/domains/archaeology/README.md` — domain landing page *(TODO: confirm presence and link target)*
- `docs/domains/archaeology/EXPANSION_PLAN.md` — companion expansion roadmap (sibling)
- `docs/domains/archaeology/FILE_SYSTEM_PLAN.md` — companion placement plan (sibling)
- `docs/doctrine/ai-build-operating-contract.md` — canonical operating contract (`CONTRACT_VERSION = "3.0.0"`)
- `docs/doctrine/directory-rules.md` — placement and lifecycle doctrine, **v1.3**
- `docs/doctrine/authority-ladder.md` — truth-label and authority source order
- `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf` — Atlas v1.1, §15 (Archaeology) and §24
- `docs/registers/VERIFICATION_BACKLOG.md` — repo-wide verification backlog
- `docs/registers/DRIFT_REGISTER.md` — drift entries when repo state and doctrine disagree
- `schemas/contracts/v1/domains/archaeology/` — **PROPOSED** canonical schema home for archaeology object families (DR §12; the bare `schemas/contracts/v1/archaeology/` form is CONFLICTED)
- `schemas/contracts/v1/receipts/generated_receipt.schema.json` — **PROPOSED** receipt schema home (per contract §47)
- `schemas/contracts/v1/3d/` — **PROPOSED** 3D-asset schema home (Directory Rules v1.3 §6.4)
- `policy/sensitivity/archaeology/` — **PROPOSED** sensitivity policy home
- `contracts/domains/archaeology/` — **PROPOSED** semantic Markdown for archaeology object families (DR §12; the bare `contracts/archaeology/` form is CONFLICTED — see ARCH-VER-10)
- `tests/domains/archaeology/` — **PROPOSED** test home; cross-domain validators belong under `tools/validators/<topic>/`
- `fixtures/domains/archaeology/` — **PROPOSED** fixture home (Directory Rules §6.6 fixtures rule)
- `release/candidates/archaeology/` — **PROPOSED** release-candidate staging

---

**Last reviewed:** 2026-05-29  ·  **Edition:** v0.3 draft  ·  **CONTRACT_VERSION:** `3.0.0`  ·  **Directory Rules:** v1.3  ·  [↑ back to top](#contents)
