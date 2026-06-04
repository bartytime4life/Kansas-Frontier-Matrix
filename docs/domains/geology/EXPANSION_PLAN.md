<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domain-geology-expansion-plan
title: Geology and Natural Resources — Expansion Plan
type: standard
subtype: domain-expansion-plan
version: v0.2
status: draft
owners: <PLACEHOLDER — geology domain steward + release manager + policy admin>
created: 2026-05-16
updated: 2026-06-03
policy_label: public
authoring_session: Docs-only. No mounted repo, CI run, workflow, dashboard, runtime log, or release artifact inspected. Implementation maturity is bounded per the current-session evidence limit.
authority_posture: Domain-scoped expansion plan. Subordinate to ai-build-operating-contract.md (CONTRACT_VERSION 3.0.0), directory-rules.md, and accepted ADRs. Supersedes no source doctrine.
related:
  - docs/domains/geology/README.md
  - docs/domains/geology/EXPANSION_BACKLOG.md          # companion backlog (GEOL-EXP-* IDs)
  - docs/doctrine/ai-build-operating-contract.md       # CONTRACT_VERSION 3.0.0
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/directory-rules.md                   # v1.3
  - docs/architecture/governed-api.md
  - docs/adr/ADR-0001-schema-home.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - docs/registers/DRIFT_REGISTER.md
tags: [kfm, domain, geology, natural-resources, expansion, thin-slice, planning, doctrine-adjacent]
notes:
  - PROPOSED placement under docs/domains/geology/ per Directory Rules §6.1 and §12.
  - All implementation-layer claims are PROPOSED until a mounted repo verifies them.
  - Doctrine-adjacent — pins CONTRACT_VERSION = 3.0.0 (ai-build-operating-contract.md).
  - v0.2 reconciles §6/§7 to the canonical seven-class source-role enum (Atlas §24.1) and surfaces the contracts/schemas path-form drift as CONFLICTED (CDR-GEOL-01), consistent with the companion backlog.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology and Natural Resources — Expansion Plan

> Phased, thin-slice-first plan for promoting the KFM **Geology and Natural Resources** domain from CONFIRMED doctrine into proof-bearing, public-safe releases under the KFM trust membrane.

![status: draft](https://img.shields.io/badge/status-draft-lightgrey)
![doctrine: CONFIRMED](https://img.shields.io/badge/doctrine-CONFIRMED-blue)
![implementation: PROPOSED](https://img.shields.io/badge/implementation-PROPOSED-orange)
![lifecycle: RAW→PUBLISHED](https://img.shields.io/badge/lifecycle-RAW%E2%86%92PUBLISHED-success)
![policy: public](https://img.shields.io/badge/policy_label-public-brightgreen)
![sensitivity: tiered](https://img.shields.io/badge/sensitivity-tiered-yellow)
![contract: 3.0.0](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-informational)
![CI: TODO](https://img.shields.io/badge/CI-TODO-lightgrey)

> [!IMPORTANT]
> **Status:** draft  ·  **Owners:** `<PLACEHOLDER — geology domain steward + release manager + policy admin>`  ·  **Updated:** 2026-06-03  ·  **Contract:** `CONTRACT_VERSION = "3.0.0"`
>
> This is a **plan**, not an implementation record. Every claim about repository files, schemas, validators, tests, CI, routes, deployment, or runtime behavior is **PROPOSED** until verified against a mounted KFM repository.

---

## Contents

1. [Purpose and posture](#1-purpose-and-posture)
2. [Scope, boundary, and non-ownership](#2-scope-boundary-and-non-ownership)
3. [Pipeline shape (RAW → PUBLISHED)](#3-pipeline-shape-raw--published)
4. [Thin-slice plan (Phase A — one county)](#4-thin-slice-plan-phase-a--one-county)
5. [Phased expansion roadmap](#5-phased-expansion-roadmap)
6. [Source families and source roles](#6-source-families-and-source-roles)
7. [Source-role anti-collapse register (Geology)](#7-source-role-anti-collapse-register-geology)
8. [Sensitivity, rights, and public-safe posture](#8-sensitivity-rights-and-public-safe-posture)
9. [Validators, tests, and fixtures backlog](#9-validators-tests-and-fixtures-backlog)
10. [API, contract, and schema surfaces](#10-api-contract-and-schema-surfaces)
11. [Governed AI behavior for Geology](#11-governed-ai-behavior-for-geology)
12. [Cross-domain relations](#12-cross-domain-relations)
13. [Acceptance criteria and release gates](#13-acceptance-criteria-and-release-gates)
14. [Verification backlog and open questions](#14-verification-backlog-and-open-questions)
15. [Open verification backlog](#15-open-verification-backlog)
16. [Changelog](#16-changelog)
17. [Definition of done](#17-definition-of-done)
18. [Related docs](#18-related-docs)

---

## 1. Purpose and posture

This plan operationalizes the **Geology and Natural Resources** domain — bedrock and surficial geology, stratigraphy, lithology, structures, boreholes, well logs, cores, geophysics, geochemistry, mineral/resource distinctions, extraction and reclamation context, public-safe layers, and bounded AI — without turning interpretations or extraction records into unreviewed public truth. The mission statement is CONFIRMED doctrine (`[DOM-GEOL §A]`, `[ENCY §7.8]`); the realization is PROPOSED.

**Doctrinal anchors.** Three things govern this plan:

- **Trust membrane** — public clients consume only released artifacts through governed APIs; no public RAW/WORK/QUARANTINE/candidate path; no direct model client.
- **Lifecycle law** — `RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED`, with **promotion as a governed state transition**, not a file move.
- **Proof-bearing thin slices** — domain expansion is judged by closure (descriptor → evidence → policy → validation → release) on a small AOI, not by horizontal coverage.

> [!NOTE]
> **Cite-or-abstain.** Geology surfaces — including AI answers, Evidence Drawer payloads, layer manifests, and Focus Mode envelopes — default to **ABSTAIN** when evidence is insufficient and **DENY** when policy, rights, sensitivity, or release state blocks the request.

[⬆ Back to top](#top)

---

## 2. Scope, boundary, and non-ownership

CONFIRMED doctrine (`[DOM-GEOL §B]`, `[ENCY §7.8]`) — the lists below are normative; field-level realization is PROPOSED.

### 2.1 Owns

The Geology domain owns the following canonical object families:

| Object family | Role |
|---|---|
| `GeologicUnit` | Bedrock and surficial polygon units |
| `Lithology` | Rock/sediment type description bound to a unit |
| `StratigraphicInterval` | Chronostratigraphic / lithostratigraphic interval |
| `GeologicAge` | Age assignment and its evidence basis |
| `FaultStructure` | Faults and other structural lines |
| `Borehole` | Borehole reference + location class |
| `WellLog` | LAS / digital well log reference |
| `CoreSample` | Physical core reference |
| `GeophysicalObservation` | Geophysics raster/profile reference |
| `GeochemistrySample` | Geochemistry sample reference |
| `MineralOccurrence` | Reported occurrence (observed source role) |
| `ResourceDeposit` | Named deposit (administrative / aggregate) |
| `ResourceEstimate` | Estimate (aggregate or modeled) |
| `ExtractionSite` | Mine / well / quarry feature (sensitivity-tiered) |
| `ReclamationRecord` | Reclamation status record |
| `CrossSection` | 2D/2.5D subsurface section |
| `HydrostratigraphicUnit` | Hydrostratigraphy linkage to Hydrology |

### 2.2 Does **not** own

CONFIRMED / PROPOSED (`[DOM-GEOL §B §F]`):

- Hydrology measurements (owned by Hydrology; Geology contributes hydrostratigraphic context only).
- Soils (owned by Soil; Geology contributes parent material / surficial context).
- Hazards **risk** (owned by Hazards; Geology contributes fault / landslide / subsidence **context** only).
- Ownership / lease / permit / title claims (owned by People/Land or Settlements).
- UI and AI statements (carriers, not authorities).

> [!CAUTION]
> **Anti-collapse invariant.** `MineralOccurrence`, `ResourceDeposit`, `ResourceEstimate`, permits, production records, and reserves are **not interchangeable**. They have different source roles, different temporal semantics, and different public-release postures. A query that joins them silently is a **DENY** condition at publication and an **ABSTAIN** at the AI surface. The canonical guardrails are in [§7](#7-source-role-anti-collapse-register-geology). CONFIRMED doctrine (`[DOM-GEOL §I]`, Atlas §24.1.2).

[⬆ Back to top](#top)

---

## 3. Pipeline shape (RAW → PUBLISHED)

CONFIRMED lifecycle law; geology lane application PROPOSED (`[DOM-GEOL §H]`).

```mermaid
flowchart LR
    A["RAW<br/>SourceDescriptor exists"] --> B["WORK / QUARANTINE<br/>schema, geometry, time,<br/>identity, evidence, rights,<br/>policy gates"]
    B -->|"gates pass"| C["PROCESSED<br/>EvidenceRef + ValidationReport<br/>+ digest closure"]
    B -->|"gates fail"| Q["QUARANTINE<br/>reason recorded"]
    C --> D["CATALOG / TRIPLET<br/>EvidenceBundle + graph projection<br/>+ release candidate"]
    D --> E["PUBLISHED<br/>ReleaseManifest + correction path<br/>+ rollback target + review state"]
    E -.->|"served via"| API["Governed API<br/>ANSWER / ABSTAIN / DENY / ERROR"]
    API -.->|"consumed by"| UI["Public clients<br/>MapLibre · Evidence Drawer · Focus Mode"]

    classDef raw fill:#fff4e6,stroke:#d97706
    classDef work fill:#fef3c7,stroke:#b45309
    classDef proc fill:#e0f2fe,stroke:#0369a1
    classDef cat fill:#dbeafe,stroke:#1d4ed8
    classDef pub fill:#dcfce7,stroke:#15803d
    classDef api fill:#f3e8ff,stroke:#6d28d9
    classDef q fill:#fee2e2,stroke:#b91c1c
    class A raw
    class B work
    class C proc
    class D cat
    class E pub
    class API,UI api
    class Q q
```

**Gate summary (PROPOSED for Geology lane):**

| Stage | Gate |
|---|---|
| RAW | `SourceDescriptor` exists; source role, rights, sensitivity, citation, time, hash captured. |
| WORK / QUARANTINE | Schema, geometry, time, identity, evidence, rights, policy gates; failures held in `quarantine` with a reason. |
| PROCESSED | `EvidenceRef`, `ValidationReport`, digest closure. |
| CATALOG / TRIPLET | `EvidenceBundle`, graph/triplet projection, release-candidate closure. |
| PUBLISHED | `ReleaseManifest`, `CorrectionNotice` path, `RollbackCard` target, review/policy state. |

[⬆ Back to top](#top)

---

## 4. Thin-slice plan (Phase A — one county)

CONFIRMED doctrine (encyclopedia thin-slice plan, `[ENCY §7.8]` / `[DOM-GEOL §N]`); PROPOSED implementation.

The first Geology release **is not** a state-wide bedrock map. It is:

> **One county `GeologicUnit` fixture with borehole/cross-section evidence, public-safe generalized resource context, and an `EvidenceBundle`-backed unit inspector.**

### 4.1 Slice contents

| Element | Description | Status |
|---|---|---|
| **AOI** | One Kansas county | PROPOSED — **steward decision**; criteria below |
| **`GeologicUnit` fixture** | Bedrock + surficial polygon set with `LayerManifest` | PROPOSED |
| **Borehole fixture** | ≥1 borehole with generalized public geometry + sensitivity transform receipt | PROPOSED |
| **`CrossSection`** | 1 cross-section linked to fixture boreholes | PROPOSED |
| **`MineralOccurrence` / `ResourceDeposit`** | Public-safe generalized resource context, **not** an estimate | PROPOSED |
| **`EvidenceBundle`** | Resolves every claim in the unit inspector | PROPOSED |
| **`LayerManifest` + `ReleaseManifest`** | Public-safe published layer | PROPOSED |
| **Evidence Drawer payload** | `ANSWER` / `ABSTAIN` / `DENY` states proven by fixture | PROPOSED |
| **Focus Mode answer (mock)** | Bounded summary citing the bundle; `ABSTAIN` on unsupported | PROPOSED |
| **`RollbackCard`** | Drill executed against the slice release | PROPOSED |

### 4.2 AOI selection criteria

> [!NOTE]
> The AOI is a **steward decision**, not a Claude decision. Candidates should be scored against the criteria below; the picked county is then recorded in an ADR or in `docs/registers/`.

| Criterion | Why it matters |
|---|---|
| **Evidence richness** | Existing KGS bedrock + surficial maps, KGS oil/gas, WWC5 wells, LAS well logs, NGMDB coverage. |
| **Source-rights clarity** | Terms for KGS, KCC, KDHE, USGS are documented and current. |
| **Sensitivity tractability** | Private well coordinates, sensitive resource sites, and proprietary log data can be generalized or excluded cleanly. |
| **Cross-domain test value** | Adjacent hydrology (hydrostratigraphy) and soil (parent material) evidence are available for cross-lane proof. |
| **Reclamation footprint** | Some active or historical extraction context is present to exercise `ReclamationRecord`. |

### 4.3 Slice closure checklist

- [ ] Source descriptors exist and resolve for every contributing source.
- [ ] Schema home decided per ADR-0001 root (`schemas/contracts/v1/`), with the geology sub-path resolved — segment-vs-flat is **CONFLICTED**, see [§8.3](#83-path-form-drift-cdr-geol-01).
- [ ] Public-safe geometry transform produces a **transform receipt** (`RedactionReceipt`) for every generalized feature.
- [ ] `EvidenceBundle` resolves for every claim in the unit inspector and the cross-section.
- [ ] `LayerManifest` references only `PUBLISHED` artifacts.
- [ ] `ReleaseManifest` and `RollbackCard` exist; rollback drill executed.
- [ ] Negative fixtures: missing rights → DENY; missing evidence → ABSTAIN; aggregate-as-per-place query → DENY.
- [ ] No-network dry run passes end-to-end.

[⬆ Back to top](#top)

---

## 5. Phased expansion roadmap

PROPOSED sequencing. Aligned with the Unified Build Manual greenfield phases and the IMPL-PIPE loop overlay; **does not** rename or extend greenfield phase identifiers.

```mermaid
flowchart TB
    P0["Phase 0<br/>Source descriptors<br/>+ schema index"] --> P1["Phase A<br/>One-county fixture<br/>+ public-safe slice"]
    P1 --> P2["Phase B<br/>Second AOI<br/>+ cross-section depth"]
    P2 --> P3["Phase C<br/>Multi-county bedrock<br/>+ KGS LAS well logs"]
    P3 --> P4["Phase D<br/>Resource-class<br/>anti-collapse harness"]
    P4 --> P5["Phase E<br/>Hydrostratigraphy<br/>+ Hazards context"]
    P5 --> P6["Phase F<br/>3D admission<br/>review"]

    classDef now fill:#dcfce7,stroke:#15803d
    classDef next fill:#fef3c7,stroke:#b45309
    classDef later fill:#e5e7eb,stroke:#6b7280
    class P0,P1 now
    class P2,P3 next
    class P4,P5,P6 later
```

### 5.1 Phase-by-phase summary

| Phase | Goal | Done criterion | Status |
|---|---|---|---|
| **0** — Bootstrap | `SourceDescriptor`s for KGS, KCC, KDHE-WWC5, USGS NGMDB/MRDS; schema home; offline fixtures; source-role policy | All descriptors validate; no-network fixture pass | PROPOSED |
| **A** — One-county slice | Section 4 thin-slice | All Section 4.3 checks pass; one release + rollback drill | PROPOSED |
| **B** — Second AOI + depth | Add a second county with `CrossSection` depth and ≥3 boreholes; exercise `CorrectionNotice` | Two releases, one supersession, one correction notice | PROPOSED |
| **C** — Bedrock multi-county | Extend bedrock + surficial coverage to a contiguous N-county block; ingest KGS LAS well-log references (not LAS payloads) | Multi-county `LayerManifest`; no rights violations | PROPOSED |
| **D** — Resource anti-collapse | Implement `MineralOccurrence` / `ResourceDeposit` / `ResourceEstimate` separation harness; add USGS MRDS context | Anti-collapse negative tests all DENY at publication | PROPOSED |
| **E** — Cross-domain | Hydrostratigraphic link to Hydrology; fault/landslide context to Hazards; parent-material to Soil | Cross-lane bundles resolve; ownership preserved | PROPOSED |
| **F** — 3D admission | Optional 3D subsurface view per 3D admission decision; `SceneManifest` + Reality Boundary Note | 3D admission gate passes; no-leak tests pass | PROPOSED |

> [!TIP]
> **Greenfield alignment.** Phases A–F sit *inside* greenfield phases that already require signing, attestation, watcher, and catalog closure (greenfield Phases 16–17 per the Unified Build Manual: Phase 16 = 3D/digital-twin/synthetic scenes; Phase 17 = live source activation maturity). The geology lane does not introduce a new lifecycle phase; it instantiates the existing one. *(Milestone identifiers like "M10–M11" are illustrative and **NEEDS VERIFICATION** against the build manual.)*

[⬆ Back to top](#top)

---

## 6. Source families and source roles

CONFIRMED doctrine (Atlas v1.1 Ch. 10 §D); rights, cadence, and current terms **NEEDS VERIFICATION** per source.

> [!CAUTION]
> **Two distinct vocabularies — do not conflate them.** KFM uses *two* role-like vocabularies, and they are not the same axis:
> 1. **Canonical source-role enum** (Atlas §24.1.1, a `SourceDescriptor` field): exactly seven classes — `observed | regulatory | modeled | aggregate | administrative | candidate | synthetic`. This is the axis the anti-collapse register and the trust membrane fail closed on.
> 2. **Per-domain descriptor language** in `[DOM-GEOL §D]`: *"authority / observation / context / model as source role requires."* Here **"authority"** denotes a *descriptor stance toward a source* (an authoritative reference), **not** a canonical source role.
>
> The table below assigns the **canonical seven-class roles** (vocabulary 1). v0.1 of this plan mixed "Authority," "Administrative / Aggregate," and an "Operational" cadence label, which blurred the two vocabularies; v0.2 reconciles to the canonical enum and keeps cadence as a separate, source-vintage attribute. Per-family role assignment is **INFERRED** and **NEEDS VERIFICATION** against each eventual `SourceDescriptor`.

| Source family | Canonical source role(s) | Sensitivity posture | Cadence | Status |
|---|---|---|---|---|
| Kansas Geological Survey — bedrock / surficial maps | `observed` (mapped units) | Public-safe at unit polygon scale | source-vintage | NEEDS VERIFICATION |
| KGS surficial geology and geologic maps | `observed` | Public-safe; precision controls on outcrop points | source-vintage | NEEDS VERIFICATION |
| USGS **NGMDB** and **GeMS** | `observed` | Public-safe; preserve unit codes | source-vintage | NEEDS VERIFICATION |
| KGS **oil & gas wells** and production | `administrative` (roster); `aggregate` (production totals) | Generalize private/proprietary fields; deny exact location for active sensitive wells | source-vintage / periodic | NEEDS VERIFICATION |
| **KCC** oil & gas regulatory data | `regulatory` | Cite as regulatory context; never collapse with observation | periodic | NEEDS VERIFICATION |
| KGS/KDHE **WWC5** and water-well program | `administrative` (program registry); `observed` (per-well log fields) | Default-deny exact private well location; generalize | periodic | NEEDS VERIFICATION |
| KGS **LAS digital well logs** and well tops | `observed` (log measurements); `modeled` (interpreted tops) | Strict rights review; LAS payloads excluded from public release by default | source-vintage | NEEDS VERIFICATION |
| USGS **MRDS** mineral resources | `aggregate` (compiled records) | Generalize per occurrence sensitivity | source-vintage | NEEDS VERIFICATION |
| USGS **3DEP** terrain | `observed` (DEM) | Public-safe | periodic | NEEDS VERIFICATION |

> [!WARNING]
> **No source activation without rights review.** A `SourceDescriptor` may exist in `RAW` for evaluation; promotion of its data into `PROCESSED` is blocked until source role, rights, sensitivity, cadence, and steward are recorded. The `source_role` field itself is a **cross-cutting** `SourceDescriptor` field whose canonical home is `schemas/contracts/v1/source/source-descriptor.json` (Atlas §24.1.3, ADR-0001) — it is **not** a geology-lane schema.

[⬆ Back to top](#top)

---

## 7. Source-role anti-collapse register (Geology)

CONFIRMED doctrine (Atlas v1.1 §24.1.2); PROPOSED implementation in this lane.

Geology is one of the domains the Atlas explicitly names as at-risk for the **aggregate-cited-as-per-place** collapse pattern (Atlas §24.1.2). The table below makes the geology-specific collapse map explicit, using the canonical guardrails from §24.1.2.

| Collapse pattern | Geology example | Required guardrail (Atlas §24.1.2) | Outcome on collapse |
|---|---|---|---|
| Modeled product labeled or queried as observed | A `modeled` interpreted well-top surface returned as if it were an `observed` reading at a point | Run receipt + uncertainty surface + role-preserving DTO field | **DENY** at publication; **ABSTAIN** at AI |
| Aggregate cited as a per-place truth | An `aggregate` `MineralOccurrence`/MRDS cell joined to a parcel as if it asserted that parcel | Aggregation receipt + geometry-scope guard + matrix-cell semantics | **DENY** join from aggregate cell to single record; **ABSTAIN** at AI |
| Administrative compilation cited as observation | An `administrative` KGS oil & gas well roster cited as "production observed here" | Source-role tag preserved; separate administrative-compilation and observed lanes | **DENY** publication of compilation as observed timeline |
| Regulatory determination cited as observation | A `regulatory` KCC permit cited as "extraction confirmed" | Separate regulatory-context and observed-event lanes; UI banner | **DENY** publication of regulatory layer as event evidence |
| Candidate exposed on a public surface | A `candidate` quarantined connector output of a `Borehole` cited in a public layer | Promotion gate; no `PUBLISHED` edge to `WORK`/`QUARANTINE` | **DENY** at trust membrane; route to QUARANTINE |
| Synthetic cited as observed | A `synthetic` AI-drafted unit summary or reconstructed cross-section displayed without a Reality Boundary Note | Reality Boundary Note + Representation Receipt + UI badge | **DENY** sovereign display; **HOLD** for steward review; **ABSTAIN** at AI |

> [!NOTE]
> All six rows map directly to Atlas §24.1.2 DENY conditions. The geology examples are domain-specific instantiations; the *roles*, *guardrails*, and *denied outcomes* are CONFIRMED cross-cutting doctrine. Source role is set at admission (`SourceDescriptor`) and preserved through every promotion — promotion never upgrades a `modeled` value to `observed` or an `aggregate` to a per-place record (Atlas §24.1.1 reading note).

[⬆ Back to top](#top)

---

## 8. Sensitivity, rights, and public-safe posture

CONFIRMED / PROPOSED (`[DOM-GEOL §I]`): exact borehole, sample, sensitive resource, well-log, and private-well locations default to **restricted or generalized** public geometry. Occurrence, deposit, estimate, permit, production, and reserve claims must remain distinct.

### 8.1 Sensitivity tiers (PROPOSED)

> [!NOTE]
> The tier labels below are a **PROPOSED, plan-local** four-band scheme for readability. The corpus-wide canonical scheme is the **T0–T4** tier rubric (ADR-S-05; `kfm_unified_doctrine_synthesis.md`). A future revision SHOULD map these bands onto T0–T4 once that rubric is adopted as canonical. The mapping is **NEEDS VERIFICATION**.

| Plan-local band | Likely T-tier (NEEDS VERIFICATION) | Examples | Default public posture |
|---|---|---|---|
| **Open** | T0 | Bedrock unit polygons; 3DEP terrain; USGS NGMDB unit codes | Public-safe |
| **Generalize** | T1–T2 | Borehole locations; `WellLog` references (not LAS payloads); mineral occurrence point footprints | Generalize to grid/township/county; **transform receipt required** |
| **Restricted** | T3 | LAS payload contents; private well exact coordinates; proprietary geochemistry; active extraction site exact location | Deny by default; steward-only behind governed API |
| **Deny** | T4 | Any unclear-rights source; any unresolved sensitivity; any active investigation flagged by steward | Deny; no public artifact |

### 8.2 Public-safe transforms

Every generalization or redaction must emit a **transform receipt** (`RedactionReceipt`) stating input class, output class, reason, policy, reviewer, and residual risk. Sensitive geometry **cannot be hidden by style alone** — it must be generalized or redacted **before** publication, with receipts.

```text
RedactionReceipt / geoprivacy transform receipt (PROPOSED)
├── input_geometry_class        # exact, township, county, grid_N
├── output_geometry_class       # one of the above
├── transform_type              # suppress | generalize | buffer | jitter | delay
├── reason                      # policy_id / sensitivity_label
├── policy_decision_ref         # PolicyDecision.decision_id
├── reviewer                    # steward identity
└── residual_risk               # documented and bounded
```

> [!IMPORTANT]
> **Default-deny promotion.** Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state **blocks public promotion**. The default is not "publish unless flagged"; it is "do not publish unless cleared." CONFIRMED doctrine (`[ENCY]`, `[DIRRULES]`).

### 8.3 Path-form drift (CDR-GEOL-01)

> [!WARNING]
> **CDR-GEOL-01 — Geology contract/schema path-form drift (CONFLICTED, ADR-class).**
> KFM doctrine carries **two live path forms** for a domain's contract and schema homes, and they disagree for geology. ADR-0001 fixes the schema **root** at `schemas/contracts/v1/` but does **not** decide the segment-vs-flat sub-path:
> - **Segment form** *(Directory Rules §6.3, §6.4 trees)* — `contracts/domains/geology/`, `schemas/contracts/v1/domains/geology/`, and (by extension) `tests/domains/geology/`, `fixtures/domains/geology/`, `policy/domains/geology/`.
> - **Flat form** *(Atlas §24.13 crosswalk; Encyclopedia §7.1)* — `contracts/geology/`, `schemas/contracts/v1/geology/`.
>
> Per Directory Rules §2.5, affected paths are marked **PROPOSED / CONFLICTED** and divergent siblings MUST NOT be created until an ADR resolves it. Every `…/domains/geology/…` path in [§9](#9-validators-tests-and-fixtures-backlog) and [§10](#10-api-contract-and-schema-surfaces) below is shown in the segment form for continuity with v0.1, but its sub-path form is **CONFLICTED**. Tracked at companion-backlog **GEOL-EXP-008** / **Q-09** and to be entered in `docs/registers/DRIFT_REGISTER.md`.

[⬆ Back to top](#top)

---

## 9. Validators, tests, and fixtures backlog

PROPOSED. Each row is a thin-slice deliverable; none are claimed as implemented. These mirror the companion backlog's `GEOL-EXP-*` rows.

| Validator / test | Purpose | Phase | Status |
|---|---|---|---|
| Source-role validator | Reject promotion when canonical source role is missing or mismatched | A | PROPOSED |
| Resource-class anti-collapse tests | DENY joins / labels that collapse `MineralOccurrence` / `ResourceDeposit` / `ResourceEstimate` / permit / production / reserve | D | PROPOSED |
| Public-safe geometry tests | DENY publication of exact sensitive geometry; verify `RedactionReceipt`s | A | PROPOSED |
| Borehole / well-log rights tests | DENY publication of restricted-rights well logs; verify generalization | A–C | PROPOSED |
| Catalog closure tests | Reject release candidates with missing `EvidenceBundle`, `ReleaseManifest`, or `RollbackCard` | A | PROPOSED |
| AI evidence-before-model tests | Focus Mode **ABSTAIN** when no `EvidenceBundle` resolves; **DENY** on policy block | A | PROPOSED |
| Hydrostratigraphy cross-lane test | Geology hydrostratigraphic link does not replace Hydrology measurements | E | PROPOSED |
| 3D admission gate test | Geology cross-sections in 3D require Reality Boundary Note + admission decision | F | PROPOSED |
| Stale-source fixture | Stale `SourceDescriptor` produces ABSTAIN or DENY with badge | A | PROPOSED |
| Rollback drill | A geology release can be rolled back via `RollbackCard`; viewer reflects the prior state | A | PROPOSED |

<details>
<summary><strong>PROPOSED fixture homes</strong> (sub-path form CONFLICTED per CDR-GEOL-01; root per ADR-0001)</summary>

```text
# Sub-path form is CONFLICTED (segment vs flat) — see §8.3 / CDR-GEOL-01.
# Shown in segment form for continuity with v0.1. Root is CONFIRMED (ADR-0001).

tests/domains/geology/        # or tests/geology/ (flat form) — CONFLICTED
├── valid/                    # passes all gates
├── invalid/                  # fails one gate at a time, fails closed
└── rollback/                 # rollback-drill fixtures

fixtures/domains/geology/     # or fixtures/geology/ (flat form) — CONFLICTED
├── source_descriptors/       # KGS, KCC, KDHE-WWC5, USGS NGMDB/MRDS (PROPOSED)
├── geologic_units/           # one-county bedrock + surficial polygons
├── boreholes/                # generalized public geometry + transform receipt
├── cross_sections/           # one CrossSection bound to fixture boreholes
├── evidence_bundles/         # bundles resolving every claim in the inspector
└── release/                  # ReleaseManifest + RollbackCard

policy/domains/geology/       # or policy/geology/ (flat form) — CONFLICTED
├── source_role.rego          # PROPOSED — validator language not yet decided (ADR-S-07)
├── sensitivity.rego          # PROPOSED — validator language not yet decided
└── resource_anti_collapse.rego  # PROPOSED — validator language not yet decided
```

All paths above are **PROPOSED**, and the **sub-path form is CONFLICTED**. The validator language (Rego, JSON-Schema-driven, or other) is **NEEDS VERIFICATION** until ADR (ADR-S-07, validator exit-code/engine convention).
</details>

[⬆ Back to top](#top)

---

## 10. API, contract, and schema surfaces

PROPOSED. Exact routes, DTO fields, and schema paths are **UNKNOWN** until verified against a mounted repo and ADR-0001. These mirror Atlas Ch. 10 §J.

| Surface | DTO / schema (PROPOSED) | Outcomes | Status |
|---|---|---|---|
| Geology feature/detail resolver (route TBD) | `GeologyDecisionEnvelope` | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED; exact route UNKNOWN |
| Geology layer-manifest resolver | `LayerManifest` (domain layer descriptor) | `ANSWER` / `DENY` / `ERROR` | PROPOSED; public-safe release only |
| Geology Evidence Drawer payload | `EvidenceDrawerPayload` + `EvidenceBundle` projection | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED; evidence and policy filtered |
| Geology Focus Mode answer | Runtime Response Envelope + `AIReceipt` | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED; AI never root truth |
| Schema responsibility root | `schemas/contracts/v1/` (geology sub-path CONFLICTED) | Finite validator outcomes | PROPOSED per ADR-0001; sub-path per CDR-GEOL-01 |

```text
# Root CONFIRMED (ADR-0001). Geology sub-path form CONFLICTED — see §8.3 / CDR-GEOL-01.
# Shown in segment form for continuity with v0.1.

schemas/contracts/v1/domains/geology/                # or .../v1/geology/ (flat) — CONFLICTED
├── geologic_unit.schema.json                        # PROPOSED
├── lithology.schema.json                            # PROPOSED
├── stratigraphic_interval.schema.json               # PROPOSED
├── fault_structure.schema.json                      # PROPOSED
├── borehole_reference.schema.json                   # PROPOSED
├── well_log_reference.schema.json                   # PROPOSED
├── core_sample.schema.json                          # PROPOSED
├── geophysical_observation.schema.json              # PROPOSED
├── geochemistry_sample.schema.json                  # PROPOSED
├── mineral_occurrence.schema.json                   # PROPOSED
├── resource_deposit.schema.json                     # PROPOSED
├── resource_estimate.schema.json                    # PROPOSED — distinct from occurrence
├── extraction_site.schema.json                      # PROPOSED — sensitivity-tiered
├── reclamation_record.schema.json                   # PROPOSED
├── cross_section.schema.json                        # PROPOSED
└── hydrostratigraphic_unit.schema.json              # PROPOSED — cross-lane link to Hydrology
```

> [!NOTE]
> `source_role` is **not** in the geology schema tree above. It is a cross-cutting `SourceDescriptor` field at `schemas/contracts/v1/source/source-descriptor.json` (Atlas §24.1.3, ADR-0001). Geology objects *carry* a source role; they do not *define* the enum.

[⬆ Back to top](#top)

---

## 11. Governed AI behavior for Geology

CONFIRMED doctrine / PROPOSED implementation (`[DOM-GEOL §L]`, `[GAI]`). AI is interpretive, never authoritative.

| Capability | Allowed? | Constraint |
|---|---|---|
| Summarize a released Geology `EvidenceBundle` | ✅ | Must cite bundle ids; citation validation must pass |
| Compare two released bundles | ✅ | Both bundles resolved and within policy scope |
| Explain unit/limit boundaries and uncertainty | ✅ | Bound by `ValidationReport` and uncertainty surface |
| Draft a steward-review note | ✅ | Flagged as draft; not published until reviewed |
| Answer with no `EvidenceBundle` resolved | ❌ | **ABSTAIN** |
| Answer where policy / rights / sensitivity / release state blocks | ❌ | **DENY** |
| Generate a borehole exact-location surface or a synthetic well log | ❌ | **DENY**; treat as `synthetic` — never presented as observed reality |
| Treat an aggregate estimate as a per-place observation | ❌ | **DENY** — anti-collapse register [§7](#7-source-role-anti-collapse-register-geology) |

Every Focus Mode answer carries an `AIReceipt` (model identity, context hash, evidence ids used, citation report id, policy decisions, runtime, outcome). AI **never** reads RAW/WORK/QUARANTINE/candidate stores and never emits direct model output to a public surface.

[⬆ Back to top](#top)

---

## 12. Cross-domain relations

CONFIRMED relation types (`[DOM-GEOL §F]`); PROPOSED field realizations. Every cross-lane relation must preserve **ownership**, **source role**, **sensitivity**, and **`EvidenceBundle` support**.

| This domain | Related lane | Relation | Constraint |
|---|---|---|---|
| Geology | **Soil** | Parent material; surficial context | Soil owns soil measurements; Geology does not replace them. |
| Geology | **Hydrology** | Hydrostratigraphy; aquifer context | Hydrology owns measurements; Geology contributes unit context only. |
| Geology | **Hazards** | Fault / landslide / subsidence context | Hazards owns risk truth; Geology contributes structural context only. |
| Geology | **People / Land** | Lease / parcel / operator references | People/Land owns ownership claims; Geology cannot prove deposits from parcels. |
| Geology | **3D / Planetary** | Subsurface cross-sections; 3D admission | Admission decision required; Reality Boundary Note for any synthetic surface (Atlas Ch. 18 §I). |

[⬆ Back to top](#top)

---

## 13. Acceptance criteria and release gates

CONFIRMED / PROPOSED. KFM does not work merely because a folder tree, map layer, route, or model response exists. A Geology release is acceptable only when **all** of the following are true for the released slice:

- [ ] **Source-role validation** — every contributing `SourceDescriptor` resolves and its canonical role is preserved on every object.
- [ ] **Public-safe geometry** — every sensitive geometry carries a `RedactionReceipt`; no sensitive geometry hidden by style alone.
- [ ] **Resource anti-collapse** — `MineralOccurrence`, `ResourceDeposit`, `ResourceEstimate`, permit, production, and reserve claims are distinct in the DTO and in the UI.
- [ ] **Rights review** — borehole/well-log rights cleared; LAS payloads excluded from public artifacts.
- [ ] **Evidence closure** — `EvidenceRef` → `EvidenceBundle` resolves for every public claim.
- [ ] **Catalog/proof closure** — `RunReceipt`, `ValidationReport`, `PromotionDecision`, and `ReleaseManifest` consistent and signed.
- [ ] **Correction path** — `CorrectionNotice` flow rehearsed against a deliberate error.
- [ ] **Rollback target** — `RollbackCard` exists; a rollback drill restores the prior release manifest in a dry run.

> [!IMPORTANT]
> **Watcher-as-non-publisher.** Any future ingest watcher (e.g., a KGS source-drift watcher analogous to the cross-cutting CDL/agriculture drift slice) emits **candidate** records and signed receipts only. Watchers never write to `data/catalog/` or `data/published/`. CONFIRMED doctrine (`[DIRRULES]`). *(The specific "EXP-001" / "EXP-002" identifiers from prior agriculture/PMTiles work are cross-lane references and **NEEDS VERIFICATION** for geology applicability.)*

[⬆ Back to top](#top)

---

## 14. Verification backlog and open questions

NEEDS VERIFICATION items. Each is checkable against a mounted KFM repository, schema set, registry, tests, logs, or release manifests.

| Item to verify | Evidence that would settle it | Status |
|---|---|---|
| KGS and KCC source descriptors | Mounted repo files, schemas, registry entries, tests, logs | NEEDS VERIFICATION |
| Borehole / well-log public policy | Policy files, deny fixtures, transform-receipt validators | NEEDS VERIFICATION |
| Resource classification scheme and tests | Schemas + anti-collapse fixtures + validators | NEEDS VERIFICATION |
| Geology API routes, MapLibre binding, Evidence Drawer integration | API routes, layer manifest, drawer fixtures, viewer release | NEEDS VERIFICATION |
| Validator language and policy engine | ADR (ADR-S-07) + working CI job | NEEDS VERIFICATION |
| Hydrostratigraphy cross-lane bundle shape | Cross-lane fixture + Hydrology coordination | NEEDS VERIFICATION |
| 3D admission posture for subsurface views | `SceneManifest` + admission decision fixture | NEEDS VERIFICATION |
| Geology contract/schema sub-path form (CDR-GEOL-01) | Accepted ADR (ADR-0001 amendment or sibling) + drift-register entry | CONFLICTED |
| Thin-slice AOI (Kansas county) | Steward decision recorded in ADR or register | UNKNOWN |
| Connection to a Geology-specific source-drift watcher | Watcher receipts + steward review summary | PROPOSED |

### 14.1 Open questions

- Which Kansas county offers the right combination of evidence richness, sensitivity, and review feasibility for the Phase A AOI? *(steward decision required)*
- How does the resource taxonomy formally distinguish `MineralOccurrence` / `ResourceDeposit` / `ResourceEstimate` / permit / production / reserve at the schema level? *(NEEDS ADR)*
- Are KGS LAS well logs admissible at all for public release, or only as references with payload excluded? *(rights review required)*
- Should the geology contract/schema home use the segment form or the flat form? *(CDR-GEOL-01 — NEEDS ADR; affects this plan, the companion backlog, and every other domain lane)*
- Should `HydrostratigraphicUnit` live under the geology schema home or be hosted cross-domain? *(NEEDS ADR; affects Hydrology and Geology jointly)*
- How do the plan-local sensitivity bands (§8.1) map onto the canonical T0–T4 rubric? *(ADR-S-05)*

[⬆ Back to top](#top)

---

## 15. Open verification backlog

These items remain `NEEDS VERIFICATION` before this document is promoted from `draft` to `review`/`published`:

1. Repo presence of every PROPOSED path in §4, §9, §10.
2. Owner assignment (replace the §0 placeholder with real role bindings).
3. CDR-GEOL-01 resolution by ADR (segment vs flat sub-path).
4. Source-role enum conformance — confirm the seven-class `source_role` field shape in the mounted `SourceDescriptor` schema (Atlas §24.1.3).
5. Validator language / policy engine (ADR-S-07).
6. Sensitivity-band → T0–T4 mapping (ADR-S-05).
7. Greenfield phase / milestone identifiers (Phases 16–17; "M10–M11" milestone labels).
8. `GENERATED_RECEIPT.json` wired into CI per operating-contract §34.

[⬆ Back to top](#top)

---

## 16. Changelog

| Version | Date | Change | Type | Reason |
|---|---|---|---|---|
| v0.1 | 2026-05-16 | Initial draft. Purpose, scope, pipeline, thin-slice, phased roadmap, source families, anti-collapse register, sensitivity posture, validator backlog, API surfaces, governed AI, cross-domain relations, acceptance gates, verification backlog. | new | First-pass domain expansion plan. |
| v0.2 | 2026-06-03 | **Reconciled §6 and §7 to the canonical seven-class source-role enum** (`observed / regulatory / modeled / aggregate / administrative / candidate / synthetic`, Atlas §24.1); replaced non-canonical "Authority" / "Administrative / Aggregate" / "Operational" labels; added a CAUTION distinguishing the source-role enum from the per-domain "authority/observation/context/model" descriptor language. | reconciliation | v0.1 blurred two distinct KFM vocabularies; doctrine fixes the source-role axis at seven classes. |
| v0.2 | 2026-06-03 | Added **§8.3 CDR-GEOL-01** surfacing the contracts/schemas segment-vs-flat path-form drift as CONFLICTED; annotated §9/§10 trees accordingly. | reconciliation | DIRRULES §6.3–§6.4 (segment) conflicts with Atlas §24.13 / ENCY §7.1 (flat); DIRRULES §2.5 requires surfacing, not silent choice. Consistent with companion backlog GEOL-EXP-008 / Q-09. |
| v0.2 | 2026-06-03 | Clarified that `source_role` is a cross-cutting `SourceDescriptor` field (`…/v1/source/source-descriptor.json`), not a geology-lane schema. | clarification | Atlas §24.1.3 / ADR-0001. |
| v0.2 | 2026-06-03 | Added `CONTRACT_VERSION = "3.0.0"` pin; named transform receipts as `RedactionReceipt`; mapped §8.1 bands to T0–T4 (NEEDS VERIFICATION); softened "EXP-001/EXP-002" and "M10–M11" references to NEEDS VERIFICATION. | clarification | Doctrine-adjacent doc; avoid asserting cross-lane identifiers as geology fact. |
| v0.2 | 2026-06-03 | Added companion sections (Open verification backlog, Changelog, Definition of done); wrapped all Mermaid node labels in quotes per KFM Mermaid-safety rules; refreshed date and badges. | enhancement / housekeeping | Doctrine-doc pattern + Mermaid safety. |

> **Backward compatibility.** All section anchors §1–§14 are preserved; §15–§17 are appended. The Mermaid diagrams render identically (label text unchanged; only quoting added). No object-family names, gate names, or outcome vocabularies were altered.

[⬆ Back to top](#top)

---

## 17. Definition of done

This document is done enough to enter the repository when:

- it is placed according to Directory Rules under the geology lane docs home;
- the geology domain steward, a release manager, and a policy admin review it;
- it is linked from the geology lane README and the companion `EXPANSION_BACKLOG.md`;
- it does not conflict with accepted ADRs;
- CDR-GEOL-01 and any other conflict with current repo conventions is logged in `docs/registers/DRIFT_REGISTER.md`;
- the `GENERATED_RECEIPT.json` planned for this AI-authored doc is wired into CI per operating-contract §34;
- owner placeholders are replaced with real bindings;
- future changes follow the operating contract's §37 lifecycle.

[⬆ Back to top](#top)

---

## 18. Related docs

- `docs/domains/geology/README.md` — domain README *(TODO — verify presence)*
- `docs/domains/geology/EXPANSION_BACKLOG.md` — companion backlog (`GEOL-EXP-*` IDs)
- `docs/doctrine/ai-build-operating-contract.md` — operating contract (`CONTRACT_VERSION = "3.0.0"`) *(CONFIRMED in attached doctrine)*
- `docs/doctrine/lifecycle-law.md` — `RAW → PUBLISHED` law *(TODO — verify)*
- `docs/doctrine/trust-membrane.md` — public-client posture *(TODO — verify)*
- `docs/doctrine/directory-rules.md` — placement authority *(CONFIRMED in attached doctrine, v1.3)*
- `docs/architecture/governed-api.md` — `ANSWER / ABSTAIN / DENY / ERROR` surface *(TODO — verify)*
- `docs/adr/ADR-0001-schema-home.md` — `schemas/contracts/v1/…` root as canonical *(referenced in attached doctrine)*
- `docs/registers/VERIFICATION_BACKLOG.md` — global verification register *(TODO — verify)*
- `docs/registers/DRIFT_REGISTER.md` — drift register (CDR-GEOL-01 lands here) *(TODO — verify)*
- `docs/standards/PROV.md` *(or `PROVENANCE.md` — pending ADR, OPEN-DR-01)* — provenance profile
- `docs/standards/PMTILES.md` — PMTiles governance profile *(referenced in prior project work)*
- `docs/standards/OGC-API-TILES.md` — tiles delivery standard *(referenced in prior project work)*

---

> [!NOTE]
> **Authority order.** Where this plan and a future Geology ADR or per-root README differ, the ADR or README wins; this plan is updated accordingly with a drift-register entry. The operating contract (`CONTRACT_VERSION = "3.0.0"`) and Directory Rules outrank this plan in all cases.

---

*Last updated: 2026-06-03  ·  Doc id: `kfm://doc/domain-geology-expansion-plan`  ·  Doc version: v0.2  ·  Status: draft  ·  Contract: `CONTRACT_VERSION = "3.0.0"`*

[⬆ Back to top](#top)
