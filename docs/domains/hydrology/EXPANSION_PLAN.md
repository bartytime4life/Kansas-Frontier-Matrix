<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid-to-assign>
title: Hydrology — Domain Expansion Plan
type: standard
version: v1
status: draft
owners: <hydrology lane steward> + <docs steward>
created: 2026-05-17
updated: 2026-05-17
policy_label: public
related:
  - docs/domains/README.md
  - docs/domains/hydrology/README.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - docs/standards/PROV.md
tags: [kfm, domain, hydrology, expansion-plan, governance, thin-slice]
notes:
  - All path and implementation claims are PROPOSED until verified against mounted repo.
  - Naming discrepancy between PROV.md and PROVENANCE.md is tracked in a separate ADR.
[/KFM_META_BLOCK_V2] -->

# 💧 Hydrology — Domain Expansion Plan

> The proof-bearing, reversible roadmap from a single Kansas HUC12 thin slice to a governed,
> publication-grade hydrology lane — under the responsibility-rooted Domain Placement Law.

<!-- Badges: placeholders until CI and registry endpoints are confirmed -->
![Status: Draft](https://img.shields.io/badge/status-draft-yellow)
![Doctrine: CONFIRMED](https://img.shields.io/badge/doctrine-CONFIRMED-blue)
![Implementation: PROPOSED](https://img.shields.io/badge/implementation-PROPOSED-orange)
![Lifecycle: RAW→PUBLISHED](https://img.shields.io/badge/lifecycle-RAW%E2%86%92PUBLISHED-informational)
![Trust: Cite-or-Abstain](https://img.shields.io/badge/trust-cite--or--abstain-success)
![Policy: Public](https://img.shields.io/badge/policy-public-lightgrey)
<!-- TODO replace with verified CI badge: ![CI](https://img.shields.io/github/actions/workflow/status/<org>/<repo>/<workflow>.yml?branch=main) -->
<!-- TODO replace with verified release tag badge: ![Release](https://img.shields.io/github/v/tag/<org>/<repo>) -->

**Status:** Draft · **Owners:** `<hydrology lane steward>` + `<docs steward>` · **Last updated:** 2026-05-17

---

## Contents

- [1. Purpose and Posture](#1-purpose-and-posture)
- [2. Scope and Boundary](#2-scope-and-boundary)
- [3. Domain Placement Law — Lane File Homes](#3-domain-placement-law--lane-file-homes)
- [4. Phased Expansion Plan](#4-phased-expansion-plan)
- [5. Lifecycle and Promotion Flow](#5-lifecycle-and-promotion-flow)
- [6. Source Families and Source-Role Discipline](#6-source-families-and-source-role-discipline)
- [7. COMID ↔ HUC12 Crosswalk and Hydrology Edge Cases](#7-comid--huc12-crosswalk-and-hydrology-edge-cases)
- [8. Validators, Tests, and Fixtures](#8-validators-tests-and-fixtures)
- [9. Sensitivity, Rights, and Publication Posture](#9-sensitivity-rights-and-publication-posture)
- [10. API, Contract, and Schema Surfaces](#10-api-contract-and-schema-surfaces)
- [11. Governed AI Behavior in the Hydrology Lane](#11-governed-ai-behavior-in-the-hydrology-lane)
- [12. Publication, Correction, and Rollback](#12-publication-correction-and-rollback)
- [13. Small Reversible PR Sequence](#13-small-reversible-pr-sequence)
- [14. Watcher and Material-Change Governance](#14-watcher-and-material-change-governance)
- [15. Verification Backlog and Open Questions](#15-verification-backlog-and-open-questions)
- [16. Related Docs](#16-related-docs)

---

## 1. Purpose and Posture

This document is the **hydrology lane's expansion plan**: it sequences the work that turns
CONFIRMED hydrology doctrine into a verifiable, PROPOSED-then-CONFIRMED lane implementation,
without bypassing the KFM trust membrane.

> [!IMPORTANT]
> Hydrology doctrine — what the lane owns, what it must not collapse, what fails closed — is
> **CONFIRMED**. Every claim about repo state, paths, route names, schemas, tests, CI, and
> runtime behavior in this document is **PROPOSED** until verified against a mounted repo.

**Posture in one line.** Domain expansion is **proof-bearing, not coverage-bearing**: a single
small AOI with closed descriptor, evidence, policy, validation, and release proves the lane
before any horizontal expansion is earned.

| Concern | Posture |
|---|---|
| Lifecycle | `RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED` |
| Promotion | Governed state transition, **never** a file move |
| Truth | Cite-or-abstain; `EvidenceRef` resolves to `EvidenceBundle` |
| Watchers | Observe, emit receipts and candidates; **never** publish |
| Reversibility | Every release carries `ReleaseManifest` + rollback target + correction path |
| Public path | Public clients use **governed API only**; no direct canonical or RAW reads |

[⬆ back to top](#contents)

---

## 2. Scope and Boundary

### 2.1 What the hydrology lane owns

The hydrology lane governs watersheds, hydrologic accounting units, the surface-water network,
in-situ observations, regulatory flood context, and observed flood evidence. Object families
follow the Culmination Atlas A–N scope for this domain.

| Object family | Role |
|---|---|
| `Watershed`, `HUCUnit` | Hydrologic accounting geometry and identity |
| `HydroFeature`, `ReachIdentity` | Surface-water network features and reach identity |
| `GaugeSite` | Monitoring location identity and metadata |
| `FlowObservation`, `WaterLevelObservation` | Time-stamped, in-situ observations |
| `WaterQualityObservation` | Parameter/value/unit/qualifier observations |
| `GroundwaterWell` | Well identity, screened interval context, level observations |
| `NFHLZone`, `FloodContext` | Regulatory flood context (**not** observed inundation) |
| `ObservedFloodEvent` | Historical or sourced inundation evidence |
| `Hydrograph`, `UpstreamTrace` | Derived analytical projections of admitted observations |

### 2.2 What the hydrology lane does **not** own

> [!CAUTION]
> Hydrology must **not** collapse regulatory flood context, observed inundation, model
> forecasts, and emergency warnings into a single truth class. Collapsing these is a
> source-role violation and fails closed.

| Out of scope | Owning lane |
|---|---|
| Emergency alerts, life-safety warnings | **Hazards** (official-source posture) |
| Soil hydric class, SSURGO/SDA canonical claims | **Soil** |
| Crop, yield, irrigation administration claims | **Agriculture** |
| Lithology, boreholes, stratigraphy | **Geology** |
| Roads, bridges, transport facility identity | **Roads / Rail** |
| Critical infrastructure asset identity | **Settlements / Infrastructure** |

[⬆ back to top](#contents)

---

## 3. Domain Placement Law — Lane File Homes

> [!NOTE]
> Domain Placement Law: a domain is a **segment** inside a responsibility root, never a root
> folder of its own. Every hydrology file lives under an existing canonical root with a
> `domains/hydrology/` or `<root>/hydrology/` segment.

The table below is the **proposed** file-home map for the hydrology lane. Every row is
**PROPOSED** until a mounted-repo inspection confirms presence; ticking a row CONFIRMED is
gated on `git`-equivalent verification.

| Responsibility root | Proposed hydrology home | Holds |
|---|---|---|
| `docs/` | `docs/domains/hydrology/` | This plan, lane README, design notes, ADR links |
| `contracts/` | `contracts/domains/hydrology/` | Semantic object meaning (Markdown) |
| `schemas/` | `schemas/contracts/v1/domains/hydrology/` | JSON Schemas (per ADR-0001 default) |
| `policy/` | `policy/domains/hydrology/` | Allow / deny / restrict / abstain bundles |
| `tests/` | `tests/domains/hydrology/` | Schema, policy, evidence-closure, no-network tests |
| `fixtures/` | `fixtures/domains/hydrology/` | Golden, valid, and negative-path fixtures |
| `packages/` | `packages/domains/hydrology/` | Shared lane libraries |
| `pipelines/` | `pipelines/domains/hydrology/` | Executable lane pipeline logic |
| `pipeline_specs/` | `pipeline_specs/hydrology/` | Declarative pipeline spec |
| `data/raw/` | `data/raw/hydrology/` | Immutable source captures |
| `data/work/` | `data/work/hydrology/` | Normalization workspace |
| `data/quarantine/` | `data/quarantine/hydrology/` | Held-failed items with reason |
| `data/processed/` | `data/processed/hydrology/` | Validated normalized objects |
| `data/catalog/` | `data/catalog/domain/hydrology/` | Catalog records, `EvidenceBundle`s |
| `data/published/` | `data/published/layers/hydrology/` | Public-safe released artifacts |
| `data/registry/` | `data/registry/sources/hydrology/` | Source descriptors and registry entries |
| `release/` | `release/candidates/hydrology/` | Release candidates and `ReleaseManifest`s |

> [!WARNING]
> Do **not** create a root `hydrology/` folder. Do **not** create parallel schema, policy,
> registry, release, or proof homes under `docs/domains/hydrology/`. Any such home requires
> an ADR amending Directory Rules.

[⬆ back to top](#contents)

---

## 4. Phased Expansion Plan

Phases are sized to be **small, reversible, and proof-bearing**. Phase 1 is the encyclopedia
thin slice. Each subsequent phase earns its scope by demonstrating closure on the previous.

```mermaid
flowchart LR
  P0["Phase 0<br/>Repo preflight<br/>Doctrine alignment"]
  P1["Phase 1 — Thin slice<br/>Kansas HUC12 +<br/>1 gauge + 1 crosswalk +<br/>NFHL overlay + hydrograph"]
  P2["Phase 2<br/>Governed API surface<br/>+ Evidence Drawer payload"]
  P3["Phase 3<br/>MapLibre layer manifest<br/>+ time slider"]
  P4["Phase 4<br/>Focus Mode / Governed AI<br/>(read-only over bundles)"]
  P5["Phase 5<br/>Watchers + material-change<br/>(USGS, NHDPlus, NFHL)"]
  P6["Phase 6<br/>Coverage expansion<br/>(more HUC12s, gauges, layers)"]

  P0 --> P1 --> P2 --> P3 --> P4 --> P5 --> P6

  classDef now fill:#dbeafe,stroke:#1d4ed8,color:#0b1e3a;
  classDef next fill:#fef3c7,stroke:#b45309,color:#451a03;
  class P1 now
  class P2 next
```

### 4.1 Phase 0 — Repo preflight (doctrine alignment)

**Goal.** Confirm Directory Rules conformance for the hydrology lane and resolve open ADR
items (schema home, `PROV.md` vs `PROVENANCE.md`, runbook subfolder convention) before any
lane code is written.

| Activity | Status |
|---|---|
| Inspect mounted repo for existing `docs/domains/hydrology/`, `schemas/contracts/v1/domains/hydrology/`, etc. | NEEDS VERIFICATION |
| Confirm ADR-0001 schema-home default applies to hydrology | NEEDS VERIFICATION |
| Record any drift in `docs/registers/DRIFT_REGISTER.md` | PROPOSED |

### 4.2 Phase 1 — Thin slice

**Goal.** Deliver the encyclopedia-defined thin slice: Kansas HUC12 + one USGS gauge fixture +
one NHDPlus identity crosswalk + NFHL contextual overlay + hydrograph panel + `EvidenceBundle`
closure + ABSTAIN on ambiguous reach identity.

| Artifact | Home | Status |
|---|---|---|
| AOI selection (one Kansas HUC12) | `docs/domains/hydrology/THIN_SLICE.md` | PROPOSED |
| `SourceDescriptor` (USGS WBD/HUC12) | `data/registry/sources/hydrology/` | PROPOSED |
| `SourceDescriptor` (NHDPlus HR sample) | `data/registry/sources/hydrology/` | PROPOSED |
| `SourceDescriptor` (USGS Water Data / NWIS) | `data/registry/sources/hydrology/` | PROPOSED |
| `SourceDescriptor` (FEMA NFHL — context only) | `data/registry/sources/hydrology/` | PROPOSED |
| No-network fixture set | `fixtures/domains/hydrology/` | PROPOSED |
| `EvidenceBundle` for one HydroFeature | `data/catalog/domain/hydrology/` | PROPOSED |
| `ReleaseManifest` (dry-run) | `release/candidates/hydrology/` | PROPOSED |
| Ambiguous-reach ABSTAIN fixture | `fixtures/domains/hydrology/negative/` | PROPOSED |

> [!TIP]
> The thin slice's job is **closure** across descriptor, evidence, policy, validation, and
> release for **one** small AOI — not coverage. A Kansas county or single HUC12 with rich,
> public-safe sources is sufficient.

### 4.3 Phase 2 — Governed API surface

**Goal.** Stand up the governed API endpoints that resolve `EvidenceRef → EvidenceBundle` and
return finite `ANSWER / ABSTAIN / DENY / ERROR` envelopes for hydrology features.

| Surface | DTO | Status |
|---|---|---|
| Hydrology feature/detail resolver | `HydrologyDecisionEnvelope` (PROPOSED name) | PROPOSED |
| Hydrology layer manifest resolver | `LayerManifest` projection | PROPOSED |
| Hydrology Evidence Drawer payload | `EvidenceDrawerPayload` + `EvidenceBundle` projection | PROPOSED |

### 4.4 Phase 3 — MapLibre layer manifest and time slider

**Goal.** Public-safe MapLibre layers backed by `LayerManifest` reads only; no renderer reads
canonical or RAW stores. Time slider carries source / observed / valid / retrieval / release
times distinctly.

### 4.5 Phase 4 — Focus Mode / Governed AI

**Goal.** Mock-adapter Focus Mode that summarizes **released** hydrology `EvidenceBundle`s
and ABSTAINs on missing bundles. No direct browser-to-model path; no AI as truth source.

### 4.6 Phase 5 — Watchers and material-change governance

**Goal.** Source-watch and material-change records for USGS flow anomalies, reservoir-level
changes, NHDPlus version drift, NFHL revisions, and floodplain geometry drift. Watchers emit
observations and candidate decisions only; **promotion stays governed**.

### 4.7 Phase 6 — Coverage expansion

**Goal.** Earn horizontal expansion by repeating thin-slice closure across additional HUC12s,
gauges, and layers — never by skipping closure.

[⬆ back to top](#contents)

---

## 5. Lifecycle and Promotion Flow

```mermaid
flowchart TD
  subgraph SRC[Sources — observation / authority / context / model]
    S1[USGS WBD/HUC12]
    S2[NHDPlus HR / 3DHP]
    S3[USGS Water Data / NWIS]
    S4[FEMA NFHL / MSC]
    S5[3DEP terrain]
    S6[Water quality / groundwater]
    S7[Historical flood evidence]
  end

  SRC --> RAW[(data/raw/<br/>hydrology/)]
  RAW --> WORK{{Normalize, validate,<br/>policy-gate}}
  WORK -->|fail closed| Q[(data/quarantine/<br/>hydrology/)]
  WORK -->|pass| PROC[(data/processed/<br/>hydrology/)]
  PROC --> CAT[(data/catalog/domain/<br/>hydrology/<br/>+ EvidenceBundle)]
  CAT --> REL{Release gate<br/>EvidenceBundle?<br/>ValidationReport?<br/>Policy decision?}
  REL -->|deny| HOLD[Block public release]
  REL -->|allow| PUB[(data/published/layers/<br/>hydrology/)]
  PUB --> API[apps/governed-api/<br/>hydrology resolvers]
  API --> UI[MapLibre shell<br/>Evidence Drawer<br/>Focus Mode]

  classDef quar fill:#fee2e2,stroke:#b91c1c,color:#450a0a;
  classDef pub fill:#dcfce7,stroke:#166534,color:#052e16;
  class Q quar
  class PUB pub
  class API pub
```

| Stage | Handling | Gate |
|---|---|---|
| `RAW` | Capture immutable source payload/reference with source role, rights, sensitivity, citation, time, hash | `SourceDescriptor` exists |
| `WORK / QUARANTINE` | Normalize schema, geometry, time, identity, evidence, rights, policy; hold failures | Validation and policy gate pass, or quarantine reason recorded |
| `PROCESSED` | Emit validated normalized objects, receipts, public-safe candidates | `EvidenceRef`, `ValidationReport`, digest closure exist |
| `CATALOG / TRIPLET` | Emit catalog records, `EvidenceBundle`s, graph/triplet projections, release candidates | Catalog/proof closure passes |
| `PUBLISHED` | Serve released public-safe artifacts through governed APIs and manifests | `ReleaseManifest`, correction path, rollback target, review/policy state exist |

[⬆ back to top](#contents)

---

## 6. Source Families and Source-Role Discipline

The hydrology lane admits sources only after their **source role** is declared and constrained.
Source roles must remain distinct in evidence, policy, and any public-safe derivative.

| Source family | Source role | Notes |
|---|---|---|
| USGS WBD / HUC12 | **authority** (accounting geometry) | Watershed boundary, nested HUC codes; vintage-sensitive |
| NHDPlus HR / 3DHP | **authority** (network) | Flow network, catchments, VAAs; preserve permanent IDs |
| USGS Water Data / NWIS | **observation** | Real-time and historical streamflow, gauge height; legacy WaterServices phasing out |
| FEMA NFHL / MSC | **regulatory context** | Effective flood hazard data; **not** observed inundation, **not** forecast |
| 3DEP terrain | **observation / context** | DEM products supporting hydrologic derivatives |
| Water-quality / groundwater | **observation** | Parameter/unit/qualifier discipline required |
| Historical observed flood evidence | **observation** (archival) | Source vintage and citation required |

> [!IMPORTANT]
> **Three role separations the lane must enforce:**
> 1. NFHL regulatory context **≠** observed inundation **≠** forecast **≠** emergency warning.
> 2. NHDPlus v2.1, NHDPlus HR, and WBD snapshot vintages must not be silently mixed; carry
>    `nhdplus_version` and `wbd_snapshot` fields explicitly.
> 3. Models, observations, regulatory interpretations, and legal status are distinct truth
>    classes — labels travel with every emitted object.

### 6.1 Rights, freshness, and admission

| Source | Rights / sensitivity | Freshness | Admission posture |
|---|---|---|---|
| USGS WBD / HUC12 | Public; redistribution terms NEEDS VERIFICATION | Vintage-pinned snapshots | Admit with `wbd_snapshot` |
| NHDPlus HR | Public; redistribution terms NEEDS VERIFICATION | Version-pinned | Admit with `nhdplus_version` |
| USGS NWIS / Water Data | Public observation | Real-time / daily | Admit with retrieval-time band |
| FEMA NFHL | Regulatory; **DENY** as observed inundation | Localized, `EFFECTIVE_DATE`-bound | Admit as context-only |
| 3DEP terrain | Public | Tile-version-pinned | Admit with tile identity |
| Water-quality / groundwater | Mixed; rights NEEDS VERIFICATION | Parameter-cadence specific | Admit on rights review |

[⬆ back to top](#contents)

---

## 7. COMID ↔ HUC12 Crosswalk and Hydrology Edge Cases

A clean, defensible COMID → HUC12 join is foundational for the lane. The deterministic
fallback order below comes directly from the Pass 19 `5-8` operational packet.

### 7.1 Deterministic fallback order

| Tier | Method | When to use |
|---|---|---|
| 1 | Official USGS NHDPlus v2.1 → WBD HU‑12 crosswalk | Primary — every networked flowline |
| 2 | Polygon overlay (area-weighted, max-overlap fraction kept) | Official crosswalk missing or insufficient |
| 3 | Centroid-in-polygon heuristic | Overlay ambiguous; record as heuristic |
| 4 | Snap-to-outlet / pour-point (constrained ≤ 3× DEM grid; PRNG seed recorded for ties) | Problematic geometry |

### 7.2 Required provenance manifest fields (per row)

```text
spec_hash             # sha256 of canonical, key-sorted JSON row
source_head           # { url, ETag, Last-Modified } of crosswalk inputs
source_doi            # e.g., USGS crosswalk DOI if present
algorithm_version     # crosswalk tool version string
comid                 # NHDPlus identifier
huc12                 # WBD HUC12 identifier
catchment_poly_hash   # wkb sha256
geometry_sanity_flags # self-intersection, tiny area, invalid ring, ...
alignment_score       # area overlap fraction used for decision
decision_reason       # official_crosswalk | area_weighted_overlay |
                      # centroid_in_polygon | snap_to_pour_point
provenance            # { tool, tool_version }
```

### 7.3 Edge cases that must not be silently collapsed

| Edge case | Required field / handling |
|---|---|
| NHDPlus version drift | `nhdplus_version` and `wbd_snapshot` carried on every row |
| Non-CONUS (e.g., Alaska) | `coverage_scope: "CONUS"`; **fail closed** outside supported extents unless explicitly supported |
| Coastal / braided systems | `multi_huc_candidate: true` + ranked `candidate_huc12s` with `overlap` |
| Ambiguous reach identity | ABSTAIN at the governed API; do not guess |

### 7.4 Validator behavior

> [!CAUTION]
> The crosswalk validator MUST be **deterministic, offline-capable, reproducible, and
> side-effect free**. It MUST NOT fetch live authoritative data during validation, mutate
> catalogs, publish records, or infer truth from AI outputs. It validates **declared
> evidence and lineage** only.

[⬆ back to top](#contents)

---

## 8. Validators, Tests, and Fixtures

Hydrology shares the cross-domain validator suite (schema, source descriptor, rights,
sensitivity, evidence closure, temporal logic, geometry validity, policy deny, citation,
release manifest, rollback drill, no-network, non-regression) and adds the following
**lane-specific** checks, all **PROPOSED** until implemented in the mounted repo.

### 8.1 Lane-specific validators

| Validator | Purpose | Status |
|---|---|---|
| HUC12 fingerprint validation | Canonicalize geometry + ID fingerprint; reject drift | PROPOSED |
| NHDPlus HR identity ambiguity tests | ABSTAIN on unresolved reach identity | PROPOSED |
| USGS parameter / unit / qualifier / no-data tests | Reject ambiguous observation semantics | PROPOSED |
| NFHL role-separation tests | Reject NFHL-as-observed-flood claims | PROPOSED |
| `EvidenceBundle` closure tests | Every public claim resolves to a closed bundle | PROPOSED |
| No-network hydrology proof fixture | Deterministic, offline, reproducible lane proof | PROPOSED |
| COMID ↔ HUC12 manifest validation | Per-row provenance manifest; fail closed on missing fields or low alignment | PROPOSED |

### 8.2 Required negative fixtures

| Fixture | Expected outcome |
|---|---|
| `invalid_huc12_length.json` | `FAIL_INVALID_HUC12` |
| `low_alignment_overlay.json` (`alignment_score` < threshold) | `FAIL_LOW_ALIGNMENT` |
| `missing_provenance.json` | `FAIL_MISSING_PROVENANCE` |
| `nfhl_as_observed_flood.json` | `DENY` (source-role violation) |
| `ambiguous_reach_identity.json` | `ABSTAIN` |
| `stale_source_head.json` | `ABSTAIN` or stale-state badge per policy |
| `unresolved_evidence_ref.json` | `ABSTAIN` |
| `non_conus_aoi.json` (e.g., Alaska) | `DENY` unless explicitly supported |
| `mixed_nhdplus_versions.json` | `DENY` (version-drift collapse) |

### 8.3 CI gating

CI MUST fail when any of the following hold:

- Crosswalk manifest missing `spec_hash`, `source_head`, or `algorithm_version`
- `alignment_score` below the policy threshold without an explicit override receipt
- Any validator emits non-finite output (must be `ANSWER` / `ABSTAIN` / `DENY` / `ERROR`)
- A negative fixture passes (i.e., fails to fail)
- Direct RAW or canonical-store exposure detected from the public path
- `EvidenceRef` resolution skipped on a public claim surface

[⬆ back to top](#contents)

---

## 9. Sensitivity, Rights, and Publication Posture

| Trigger | Posture |
|---|---|
| Unclear source rights | **DENY** public release until terms and redistribution class are recorded |
| NFHL framed as observed inundation | **DENY** (source-role violation) |
| Private property or critical-infrastructure implication | **REVIEW** before any public release |
| Stale source vs release window | Stale-state badge or `ABSTAIN` per freshness policy |
| Precise sensitive-asset geometry | **DENY** unless a redaction / generalization receipt exists |

> [!WARNING]
> Hydrology has lower default sensitivity than fauna nests or archaeology, **but** it can
> still touch private property, infrastructure, and life-safety adjacencies. Default to
> redaction, generalization, or delayed publication when in doubt. Record every transform
> and reason on a `RedactionReceipt`.

[⬆ back to top](#contents)

---

## 10. API, Contract, and Schema Surfaces

All surfaces below are **PROPOSED**. Route names, DTO names, and schema homes are placeholders
until verified against the mounted repo and named in an ADR where required.

| Endpoint / artifact | DTO / schema | Finite outcomes | Status |
|---|---|---|---|
| Hydrology feature / detail resolver | `HydrologyDecisionEnvelope` (PROPOSED) | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED — route TBD |
| Hydrology layer manifest resolver | `LayerManifest` / domain layer descriptor | `ANSWER` / `DENY` / `ERROR` | PROPOSED — public-safe release only |
| Hydrology Evidence Drawer payload | `EvidenceDrawerPayload` + `EvidenceBundle` projection | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED — evidence and policy filtered |
| Hydrology Focus Mode answer | Runtime Response Envelope + `AIReceipt` | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED — AI never root truth |
| Schema responsibility root | `schemas/contracts/v1/domains/hydrology/` | finite validator outcomes | PROPOSED — verify with Directory Rules + ADR-0001 |

<details>
<summary>Proposed schema list under <code>schemas/contracts/v1/domains/hydrology/</code></summary>

> [!NOTE]
> All filenames below are **PROPOSED**. Final names depend on the cross-domain object-map ADR
> and on whether the lane uses singular or plural object names in file paths.

- `Watershed.v1.schema.json`
- `HUCUnit.v1.schema.json`
- `HydroFeature.v1.schema.json`
- `ReachIdentity.v1.schema.json`
- `GaugeSite.v1.schema.json`
- `FlowObservation.v1.schema.json`
- `WaterLevelObservation.v1.schema.json`
- `WaterQualityObservation.v1.schema.json`
- `GroundwaterWell.v1.schema.json`
- `NFHLZone.v1.schema.json` (regulatory context only)
- `ObservedFloodEvent.v1.schema.json`
- `Hydrograph.v1.schema.json`
- `UpstreamTrace.v1.schema.json`
- `ComidHuc12CrosswalkRow.v1.schema.json`

</details>

[⬆ back to top](#contents)

---

## 11. Governed AI Behavior in the Hydrology Lane

> [!IMPORTANT]
> AI is **interpretive, not the root truth source**. AI may summarize **released** hydrology
> `EvidenceBundle`s, compare evidence, explain limitations, and draft steward-review notes.
> AI MUST `ABSTAIN` when evidence is insufficient and `DENY` where policy, rights,
> sensitivity, or release state blocks the request.

| AI behavior | Permitted? | Rationale |
|---|---|---|
| Summarize released `EvidenceBundle` | ✅ | Bounded by citation validation; `AIReceipt` recorded |
| Compare two released observations | ✅ | If both bundles closed; otherwise ABSTAIN |
| Generate hydrologic forecast or model output | ❌ | AI is not a hydrologic model; forecasts require sourced models |
| Reframe NFHL as observed flood | ❌ | Source-role violation; DENY |
| Read RAW / WORK / QUARANTINE | ❌ | Trust-membrane violation |
| Direct browser-to-model call | ❌ | Routed through governed API only |
| Emit uncited public claim | ❌ | Cite-or-abstain |

[⬆ back to top](#contents)

---

## 12. Publication, Correction, and Rollback

Every hydrology public release MUST carry:

1. A `ReleaseManifest` listing artifact digests and the release decision.
2. A closed `EvidenceBundle` for every public claim.
3. A `ValidationReport` and policy decision support.
4. A review state where required by sensitivity or rights.
5. A correction path (how to file a correction, who handles it, what supersedes what).
6. A `RollbackCard` with a concrete rollback target and a drilled rollback procedure.

```mermaid
flowchart LR
  RC[Release Candidate] --> GATES{All gates pass?<br/>EvidenceBundle?<br/>Validation?<br/>Policy?<br/>Review?}
  GATES -->|no| HOLD[Hold or quarantine]
  GATES -->|yes| RM[ReleaseManifest signed]
  RM --> PUB[Publish to data/published/<br/>+ governed API]
  PUB --> CORR[CorrectionNotice path open]
  PUB --> RB[RollbackCard with rollback target]
  CORR --> RM2[Supersession or amendment]
  RB --> PREV[Restore prior manifest if needed]
```

> [!TIP]
> A rollback drill MUST be performed against at least one dry-run hydrology release before the
> first live publication. The rollback receipt is itself part of the lane's proof set.

[⬆ back to top](#contents)

---

## 13. Small Reversible PR Sequence

The PR sequence below adapts the encyclopedia PR-00..PR-10 roadmap to the hydrology lane.
Every PR is small, reversible, and tied to validation and rollback. All proposed homes are
responsibility roots under Domain Placement Law.

| # | PR | Proposed home(s) | Acceptance | Rollback |
|---|---|---|---|---|
| PR-00 | No-network hydrology fixture | `fixtures/domains/hydrology/`, `tests/domains/hydrology/` | Fixture validates with no network access | Revert PR |
| PR-01 | Schema-home ADR (hydrology) | `docs/adr/` | ADR accepted; Directory Rules conformance | Supersede ADR |
| PR-02 | `SourceDescriptor` + source registry | `contracts/domains/hydrology/`, `schemas/contracts/v1/domains/hydrology/`, `data/registry/sources/hydrology/` | Valid/invalid fixtures; deny unknown rights | Disable descriptor |
| PR-03 | Lane validators (schema/evidence/rights/sensitivity/temporal/geometry) | `tools/validators/`, `tests/domains/hydrology/` | Negative tests fail closed | Revert / pin previous |
| PR-04 | `EvidenceBundle` resolver for one HydroFeature | `packages/evidence/`, `apps/governed-api/` | `ABSTAIN` on missing bundle | Disable route |
| PR-05 | Catalog closure stub (CatalogMatrix, DatasetVersion, ValidationReport) | `data/catalog/domain/hydrology/`, `schemas/...`, `tests/...` | Closure test rejects incomplete bundle | Delete release candidate |
| PR-06 | MapLibre `LayerManifest` + public-safe layer fixture + badges | `apps/explorer-web/` (or shell), `data/published/layers/hydrology/` | Map layer reads only released manifest | Remove layer from registry |
| PR-07 | Evidence Drawer (feature click → governed API → payload) | UI + `apps/governed-api/` | Citation / evidence tests pass | Disable drawer link |
| PR-08 | Focus Mode mock-adapter (read-only over released bundles) | `runtime/model_adapters/mock/`, `tests/...` | Finite-outcome tests pass | Disable adapter |
| PR-09 | Promotion dry-run (no public publication) | `release/candidates/hydrology/`, `policy/domains/hydrology/`, `tests/...` | `no-public-write` test passes | Discard candidate |
| PR-10 | Rollback drill against a dry-run release | `release/`, `docs/runbooks/hydrology/` | Rollback drill receipt produced | Restore prior `ReleaseManifest` |

[⬆ back to top](#contents)

---

## 14. Watcher and Material-Change Governance

Hydrology watchers observe and record; they do not publish. The lane's first watchers,
drawn from Pass 19 operational packets, are:

| Watcher | Trigger | Emits |
|---|---|---|
| USGS flow anomaly | Anomaly above policy threshold over rolling window | Observation receipt + candidate decision |
| Reservoir level change | Level delta above threshold for a monitored reservoir | Observation receipt + candidate decision |
| NHDPlus version drift | New NHDPlus HR / v2.1 release; WBD snapshot change | Material-change record + supersession candidate |
| NFHL revision | New `EFFECTIVE_DATE` or `VERSION_ID` on a tracked panel | Material-change record (regulatory context only) |
| Floodplain geometry drift | Geometry-fingerprint change beyond tolerance | Material-change record + review candidate |

> [!IMPORTANT]
> Watcher invariants:
> - MUST NOT mutate catalog truth
> - MUST NOT publish directly
> - MUST NOT overwrite canonical records
> - MUST NOT bypass review states
> - MAY emit observations, receipts, and candidate decisions only

[⬆ back to top](#contents)

---

## 15. Verification Backlog and Open Questions

| Item | What would settle it | Status |
|---|---|---|
| Verify actual schema home and path conventions in mounted repo | `schemas/contracts/v1/domains/hydrology/` presence + ADR-0001 conformance | NEEDS VERIFICATION |
| Verify HUC12 fixture and fingerprint canonicalization rule | Fixture files, validator code, validator tests | NEEDS VERIFICATION |
| Verify NHDPlus HR crosswalk and ambiguity ABSTAIN behavior | Route logic, validator outputs, negative fixtures | NEEDS VERIFICATION |
| Verify USGS Water normalizer and NFHL source-role separation | Normalizer code + policy bundle | NEEDS VERIFICATION |
| Verify hydrology API and MapLibre layer adapter | Route registry, `LayerManifest` reads, e2e smoke | NEEDS VERIFICATION |
| Confirm `release/candidates/hydrology/` exists or needs to be created | Repo inspection | NEEDS VERIFICATION |
| Decide singular vs plural in `data/triplet(s)/` path | One-line ADR | OPEN |
| Resolve `PROV.md` vs `PROVENANCE.md` naming discrepancy | Cross-document ADR (tracked separately) | OPEN |
| Confirm runbook subfolder convention (`docs/runbooks/hydrology/` vs flat-prefix) | ADR or repo evidence | OPEN |
| Identify the Kansas HUC12 to seed the thin slice | Selection note in `docs/domains/hydrology/THIN_SLICE.md` | OPEN |
| Decide whether `EvidenceBundle` is always stored or sometimes generated at request time | ADR | OPEN |
| Identify watcher cadence and threshold-drift policy for USGS flow anomalies | Operational ADR + policy bundle | OPEN |

> [!NOTE]
> Items marked `NEEDS VERIFICATION` are checkable against a mounted repository. Items marked
> `OPEN` require an ADR or steward decision before they can be settled. Until both are
> resolved, all path-bearing claims in this document remain PROPOSED.

[⬆ back to top](#contents)

---

## 16. Related Docs

- [`docs/domains/README.md`](../README.md) — Domain lane index and source-role burden logic (PROPOSED)
- [`docs/domains/hydrology/README.md`](./README.md) — Hydrology lane landing page (PROPOSED)
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — Domain Placement Law (§12) and lifecycle invariants
- [`docs/doctrine/lifecycle-law.md`](../../doctrine/lifecycle-law.md) — RAW → PUBLISHED governed transitions (PROPOSED)
- [`docs/doctrine/trust-membrane.md`](../../doctrine/trust-membrane.md) — Public-path discipline (PROPOSED)
- [`docs/sources/SOURCE_DESCRIPTOR_STANDARD.md`](../../sources/SOURCE_DESCRIPTOR_STANDARD.md) — Standard source descriptor fields (PROPOSED)
- [`docs/standards/PROV.md`](../../standards/PROV.md) — W3C PROV-O / PAV provenance profile
- [`docs/standards/PMTILES.md`](../../standards/PMTILES.md) — PMTiles v3 governance profile
- [`docs/standards/OGC-API-TILES.md`](../../standards/OGC-API-TILES.md) — OGC API Tiles delivery profile
- [`docs/standards/OAI-PMH.md`](../../standards/OAI-PMH.md) — OAI-PMH 2.0 harvest governance
- [`docs/standards/ISO-19115.md`](../../standards/ISO-19115.md) — ISO 19115 crosswalk profile
- [`docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md`](../../runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md) — Companion runbook pattern
- `docs/adr/` — ADR home for schema-home, runbook convention, and `PROV.md` / `PROVENANCE.md` decisions (PROPOSED)

---

<sub>Status: Draft · Version: v1 · Last updated: 2026-05-17 · Owners: `<hydrology lane steward>` + `<docs steward>`</sub>

[⬆ back to top](#contents)
