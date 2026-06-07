<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domain-hydrology-readme
title: Hydrology Domain — README
type: domain_readme
version: v2
status: draft
owners: <hydrology-domain-stewards@kfm — assign in CODEOWNERS>   # TODO confirm handles
created: 2026-05-17
updated: 2026-06-07
policy_label: public
related:
  - ai-build-operating-contract.md
  - directory-rules.md
  - docs/architecture/
  - docs/registers/DRIFT_REGISTER.md
  - docs/domains/hydrology/PUBLICATION_POSTURE.md
  - contracts/domains/hydrology/                     # PROPOSED; path CONFLICTED vs Atlas §24.13 — see §17
  - schemas/contracts/v1/domains/hydrology/          # PROPOSED; path CONFLICTED vs Atlas §24.13 — see §17
  - policy/domains/hydrology/
  - kfm://source-id/DOM-HYD
  - kfm://source-id/ENCY
  - kfm://source-id/DIRRULES
  - kfm://source-id/BLD-COMP
  - kfm://source-id/IMPL-PIPE
tags: [kfm, domain, hydrology, watershed, huc, gauge, nhdplus, nfhl, evidence-bundle]
notes:
  - 'CONTRACT_VERSION = "3.0.0"'
  - "Hydrology is the early proof-bearing thin slice (roadmap phase 5; BLD-COMP §8 / IMPL-PIPE §14)."
  - "Implementation maturity is PROPOSED until mounted-repo evidence is checked."
  - "NFHL is regulatory context only; never published as observed flooding."
  - "Domain-segment path form (.../domains/hydrology/) follows Directory Rules §12 but CONFLICTS with Atlas §24.13 (.../hydrology/). Tracked in §17."
[/KFM_META_BLOCK_V2] -->

# 💧 Hydrology — Domain README

> Evidence-bound, time-aware Kansas hydrology: watersheds, HUCs, reaches, gauges, observations, regulatory context, and flood-context overlays — **never** an emergency flood-warning system.

[![Status: CONFIRMED doctrine / PROPOSED impl](https://img.shields.io/badge/status-CONFIRMED%20doctrine%20%2F%20PROPOSED%20impl-blue)](#status)
[![Authority: canonical (docs)](https://img.shields.io/badge/authority-canonical%20(docs)-informational)](#authority-level)
[![Policy label: public](https://img.shields.io/badge/policy-public-brightgreen)](#11-sensitivity-rights--publication-posture)
[![Lane: early proof (phase 5)](https://img.shields.io/badge/lane-early%20proof%20(phase%205)-orange)](#1-scope--boundary)
[![Lifecycle: RAW→PUBLISHED](https://img.shields.io/badge/lifecycle-RAW%E2%86%92PUBLISHED-lightgrey)](#7-pipeline-shape-raw--published)
[![CONTRACT_VERSION: 3.0.0](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-informational)](#authority-level)
[![CI: TODO](https://img.shields.io/badge/CI-TODO-lightgrey)](#10-validators-tests-and-fixtures-proposed)
[![Last reviewed: 2026-06-07](https://img.shields.io/badge/last%20reviewed-2026--06--07-lightgrey)](#last-reviewed)

| Field             | Value                                                                 |
| ----------------- | --------------------------------------------------------------------- |
| **Status**        | CONFIRMED doctrine / PROPOSED implementation                          |
| **Authority**     | Canonical (documentation) — `docs/domains/hydrology/`                 |
| **Owners**        | `<hydrology-domain-stewards>` — _placeholder; assign in CODEOWNERS_   |
| **Lane role**     | Early proof-bearing thin slice (roadmap phase 5; per `BLD-COMP §8`, `IMPL-PIPE §14`) |
| **Policy label**  | `public` (doctrine; per-artifact label still governs at publication)  |
| **Contract**      | `CONTRACT_VERSION = "3.0.0"` (`ai-build-operating-contract.md` v3.0)   |
| **Last reviewed** | 2026-06-07                                                            |

> [!NOTE]
> This README is **doctrinal documentation**, not the truth store. Object meaning lives in
> `contracts/domains/hydrology/`; machine shape in `schemas/contracts/v1/domains/hydrology/`;
> admissibility in `policy/domains/hydrology/`; lifecycle artifacts under `data/.../hydrology/`.
> Public surfaces consume **`apps/governed-api/`**, never canonical stores directly.

---

## Table of contents

1. [Scope & boundary](#1-scope--boundary)
2. [Repo fit & directory pattern](#2-repo-fit--directory-pattern)
3. [Ubiquitous language](#3-ubiquitous-language)
4. [Source families & source roles](#4-source-families--source-roles)
5. [Object families](#5-object-families)
6. [Cross-lane relations](#6-cross-lane-relations)
7. [Pipeline shape (RAW → PUBLISHED)](#7-pipeline-shape-raw--published)
8. [Map & viewing products](#8-map--viewing-products)
9. [API / contract / schema surfaces (PROPOSED)](#9-api--contract--schema-surfaces-proposed)
10. [Validators, tests, and fixtures (PROPOSED)](#10-validators-tests-and-fixtures-proposed)
11. [Sensitivity, rights, & publication posture](#11-sensitivity-rights--publication-posture)
12. [Governed AI behavior](#12-governed-ai-behavior)
13. [Publication, correction, & rollback](#13-publication-correction--rollback)
14. [Thin-slice plan](#14-thin-slice-plan)
15. [Verification backlog & open questions](#15-verification-backlog--open-questions)
16. [Related folders & docs](#16-related-folders--docs)
17. [ADRs & open path conflicts](#17-adrs--open-path-conflicts)

---

## 1. Scope & boundary

**CONFIRMED doctrine / PROPOSED implementation** _([DOM-HYD], [ENCY §7.2])._

Hydrology represents Kansas water systems as **evidence-bound, time-aware** hydrologic features, observations, and regulatory contexts. It is the **first proof-lane candidate** in the KFM build sequence — chosen because it exercises every governance primitive (source-role discipline, identity ambiguity, regulatory-vs-observed separation, NFHL handling, gauge time series, EvidenceBundle closure) in a single coherent slice _([BLD-COMP §8 / IMPL-PIPE §10.2], [Atlas §21 roadmap phase 5])._

### What hydrology owns

> [!IMPORTANT]
> Ownership is **doctrinal**, not implementation-state. The mounted-repo realization is PROPOSED.

- Watersheds and HUC units (`Watershed`, `HUCUnit`).
- Stream/river identity and geometry (`HydroFeature`, `ReachIdentity`).
- In-situ observation sites (`GaugeSite`, `GroundwaterWell`).
- Hydrologic time series (`FlowObservation`, `WaterLevelObservation`, `WaterQualityObservation`, `AquiferObservation`, `Hydrograph`).
- Regulatory flood **context** (`NFHLZone`) — read explicitly as regulatory context, never as observed inundation.
- Topological analysis (`UpstreamTrace`).
- Cross-domain links surfaced from a hydrologic anchor (`WaterUseLink`, `DroughtLink`, `IrrigationLink`).

### What hydrology explicitly **does not** own

- **Emergency alerts & life-safety warnings.** CONFIRMED doctrine places Hydrology (with Hazards and Air) on the emergency-alert boundary: KFM used as a life-safety instruction is a **DENY** surface. KFM is not an emergency warning system. _([Atlas §20.4 emergency-alert boundary], [DOM-HAZ])._
- **NFHL ≠ observed inundation.** Regulatory flood-hazard layers are not observed events, not forecasts, not hydraulic model output. The role separation is **fail-closed**. _([DOM-HYD], [Atlas §24.1 source-role anti-collapse])._
- **Soil, agriculture, geology, infrastructure** keep their own canonical claims; hydrology cites them, it does not absorb them. _([DOM-HYD])._
- **Modeled hydrograph reconstructions** are modeled outputs carrying a `ModelRunReceipt` — they are not relabeled as observations on publication. _([Atlas §24.1])._

> [!CAUTION]
> Collapsing **observed gauge readings**, **regulatory NFHL zones**, **modeled hydrographs**, and
> **operational warnings** into a single truth class is a publication-blocking violation. See
> [§11. Sensitivity, rights, & publication posture](#11-sensitivity-rights--publication-posture).

[⬆ Back to top](#-hydrology--domain-readme)

---

## 2. Repo fit & directory pattern

**CONFIRMED placement pattern** _([DIRRULES §12 Domain Placement Law])._ Hydrology is **not** a root folder — it is a **segment** inside each responsibility root.

> [!WARNING]
> **Path-form conflict (CONFLICTED).** Directory Rules §12 spells the lane with a `domains/`
> segment (`schemas/contracts/v1/domains/hydrology/`, `contracts/domains/hydrology/`). The
> Atlas §24.13 crosswalk spells the same lane **without** it (`schemas/contracts/v1/hydrology/`,
> `contracts/hydrology/`). This README follows **Directory Rules** (which win on path
> questions) and logs the divergence in [§17](#17-adrs--open-path-conflicts) for ADR resolution.
> Treat the segment as PROPOSED until reconciled.

### Lane pattern across responsibility roots — _PROPOSED tree (NEEDS VERIFICATION in mounted repo)_

```text
docs/domains/hydrology/                           ← this README + domain dossiers (canonical docs)
contracts/domains/hydrology/                      ← object meaning (.md): Watershed, ReachIdentity, …
schemas/contracts/v1/domains/hydrology/           ← JSON Schema (per ADR-0001 schema-home rule)
policy/domains/hydrology/                         ← admissibility (rego/OPA or equivalent)
tests/domains/hydrology/                          ← validator & policy enforcement tests
fixtures/domains/hydrology/                       ← golden / valid / invalid fixtures
packages/domains/hydrology/                       ← shared hydrology library code (if any)
pipelines/domains/hydrology/                      ← executable pipeline logic
pipeline_specs/hydrology/                         ← declarative pipeline spec
connectors/<source>/                              ← source-specific fetchers (usgs-water/, wbd/, nhdplus-hr/, nfhl/)
data/raw/hydrology/                               ← immutable source capture
data/work/hydrology/                              ← normalization workspace
data/quarantine/hydrology/                        ← failed-gate hold area
data/processed/hydrology/                         ← validated, public-safe candidates
data/catalog/domain/hydrology/                    ← catalog records
data/triplets/<...>/                              ← graph projection (cross-domain placement)
data/published/layers/hydrology/                  ← released artifacts (served via governed API)
data/registry/sources/hydrology/                  ← SourceDescriptor + source-role registry entries
data/receipts/<...>/  data/proofs/<...>/          ← receipts & proofs (sibling, not under hydrology)
release/candidates/hydrology/                     ← release decisions, manifests, rollback cards
```

> [!NOTE]
> The pattern itself is **CONFIRMED** by `directory-rules.md §12`. The actual existence of any
> given subdirectory or file is **NEEDS VERIFICATION** until inspected in the mounted repo.
> Anything not present yet remains **PROPOSED**.

### Lifecycle, end to end

```mermaid
flowchart LR
  subgraph Sources["Source families — data/registry/sources/hydrology/"]
    direction TB
    SRC_USGSW["USGS Water Data API<br/>(EXT-USGS-WATER)"]
    SRC_WBD["WBD / HUC<br/>(EXT-WBD)"]
    SRC_NHD["NHDPlus HR / 3DHP<br/>(EXT-NHDHR)"]
    SRC_NFHL["FEMA NFHL / MSC<br/>(EXT-NFHL)"]
    SRC_3DEP["3DEP terrain<br/>(EXT-3DEP)"]
    SRC_STATE["State water — WQ — groundwater"]
  end

  Sources -->|"connectors/*/"| RAW
  RAW["data/raw/hydrology/<br/><i>SourceDescriptor exists</i>"]
  RAW --> WORK["data/work/hydrology/<br/><i>normalize geometry, time, identity</i>"]
  WORK -.->|"gate fails"| QUAR["data/quarantine/hydrology/<br/><i>reason recorded</i>"]
  WORK --> PROC["data/processed/hydrology/<br/><i>EvidenceRef + ValidationReport + digest closure</i>"]
  PROC --> CAT["data/catalog/domain/hydrology/<br/>+ data/triplets/<br/><i>EvidenceBundle + catalog/proof closure</i>"]
  CAT --> REL["release/candidates/hydrology/<br/><i>PromotionDecision + ReleaseManifest + RollbackCard</i>"]
  REL --> PUB["data/published/layers/hydrology/<br/><i>served via apps/governed-api/</i>"]

  classDef gate fill:#fff5e6,stroke:#b8860b,color:#000;
  classDef pub fill:#e8f5e9,stroke:#2e7d32,color:#000;
  class REL gate;
  class PUB pub;
```

> [!TIP]
> Promotion is a **governed state transition**, not a file move. Each upward arrow requires its
> gate-specific evidence (`SourceDescriptor`, `ValidationReport`, `EvidenceBundle`,
> `PromotionDecision`, `ReleaseManifest`, `RollbackCard`), and every required artifact must
> *resolve* — not merely reference — its dependencies, or the transition fails closed.

[⬆ Back to top](#-hydrology--domain-readme)

---

## 3. Ubiquitous language

**CONFIRMED terms / PROPOSED field realization** _([DOM-HYD], [ENCY §7.2.C], [Atlas §4.C])._ Meaning inside this lane is constrained by source role, evidence, time, and release state. Field-level realization belongs in `contracts/domains/hydrology/` Markdown.

| Term                           | Working definition (constrained by source role, evidence, time, release state) |
| ------------------------------ | ------------------------------------------------------------------------------ |
| **Watershed**                  | Drainage area bounded by surface-flow topology; KFM realization uses WBD/HUC anchors. |
| **HUCUnit**                    | A Hydrologic Unit identified by a HUC code at a specified digit level (HUC8/10/12). |
| **HydroFeature**               | Generic hydrographic feature (stream, river, lake, reservoir, wetland, canal). |
| **ReachIdentity**              | Stable identity of a stream reach across NHD vintages; ambiguous identity → ABSTAIN. |
| **GaugeSite**                  | A USGS Water Data monitoring location with site metadata (id, coords, datum, units). |
| **FlowObservation**            | An observed discharge reading (param `00060`, cfs) at a `GaugeSite` and time. _Observed role._ |
| **WaterLevelObservation**      | An observed gage-height / stage reading. _Observed role._                      |
| **WaterQualityObservation**    | An observed water-quality measurement with parameter code, unit, qualifier.    |
| **GroundwaterWell**            | A registered well location with construction/use metadata where rights permit. |
| **AquiferObservation**         | An observed aquifer-state reading (water level, withdrawal) bound to a well or aquifer. |
| **NFHLZone**                   | A FEMA-designated flood-hazard zone. _Regulatory role only — never observed event._ |
| **Hydrograph**                 | Time-series projection of flow or level; flagged Observed vs Modeled per `source_role`. |
| **UpstreamTrace**              | A network-traversal result identifying upstream/downstream reaches of a feature. |
| **WaterUseLink / DroughtLink / IrrigationLink** | Surfaced cross-domain edges anchored on a hydrologic feature.   |
| **Observed Flood Event**       | An observed inundation evidence record. _Distinct object family from `NFHLZone`._ |
| **Flood Context**              | Composite view of regulatory + observed + modeled flood material, kept role-separated. |

> [!IMPORTANT]
> "Source role" is a first-class attribute, not a stylistic tag. See
> [§4. Source families & source roles](#4-source-families--source-roles).

[⬆ Back to top](#-hydrology--domain-readme)

---

## 4. Source families & source roles

**CONFIRMED source families / PROPOSED governance instances** _([DOM-HYD §D], [ENCY §7.2.B])._ Each row carries an explicit role; rights & sensitivity are NEEDS VERIFICATION per source until reviewed.

> [!NOTE]
> The Atlas states the canonical role for every Hydrology source family as
> **"authority / observation / context / model as source role requires"** — i.e. the role is
> assigned per claim at admission, not fixed per source. The "typical role(s)" column below is
> an INFERRED reading of which role each family most often carries; it does not narrow the
> Atlas's per-claim rule.

| Source family                                   | Source ID        | Typical role(s)                       | Rights / sensitivity                          | Freshness               | Status                |
| ----------------------------------------------- | ---------------- | ------------------------------------- | --------------------------------------------- | ----------------------- | --------------------- |
| USGS Water Data / NWIS APIs                     | `EXT-USGS-WATER` | **observation** (flow, level, WQ)     | Public; rate-limits NEEDS VERIFICATION        | Near real-time + daily  | CONFIRMED ext. / PROPOSED impl. |
| USGS Watershed Boundary Dataset (WBD) / HUC12   | `EXT-WBD`        | **authority** (HUC geography)         | Public; vintage-sensitive                     | Snapshot vintages       | CONFIRMED ext. / PROPOSED impl. |
| USGS NHDPlus HR / 3DHP hydrography              | `EXT-NHDHR`      | **authority** (hydrography, network)  | Public; identity-ambiguity-sensitive          | Snapshot vintages       | CONFIRMED ext. / PROPOSED impl. |
| FEMA NFHL / MSC                                 | `EXT-NFHL`       | **regulatory/context** (flood zones)  | Public; never relabel as observed flooding    | Localized, event-driven | CONFIRMED ext. / PROPOSED impl. |
| USGS 3DEP terrain                               | `EXT-3DEP`       | **authority/context** (terrain, derived hydro) | Public                               | Snapshot vintages       | CONFIRMED ext. / PROPOSED impl. |
| State water offices (Kansas DWR / KGS / KDHE)   | _various_        | **observation / administrative**      | Mostly public; some restricted joins          | Varies                  | NEEDS VERIFICATION    |
| Water-quality & groundwater sources             | _various_        | **observation**                       | Public; parameter & QA metadata required; restricted well/owner detail | Varies | NEEDS VERIFICATION    |
| Irrigation / drought sources                    | _various_        | **observation / aggregate / model**   | Public; aggregation receipts required         | Varies                  | NEEDS VERIFICATION    |
| Historical observed flood evidence              | _various_        | **observation (historical)**          | Public where archival; review where uncertain | One-shot / historical   | NEEDS VERIFICATION    |

> [!CAUTION]
> **Source-role anti-collapse** _([Atlas §24.1])._ A single source family may participate in
> multiple claims, but the role per claim is fixed at admission and validated on publication;
> a role is **never upgraded by promotion**:
>
> - **Observation** (USGS gauge reading) ≠ **Regulatory** (NFHL zone)
> - **Model** (reconstructed hydrograph, suitability raster) ≠ **Observation**
> - **Aggregate** (HUC rollup) ≠ per-place truth
> - **Administrative** (state water-right roster) ≠ observed event timeline
> - **Operational warning** ≠ KFM life-safety authority
>
> Role mismatch is a **DENY condition**, not a quality issue. Enforcement lives in
> `policy/domains/hydrology/`.

[⬆ Back to top](#-hydrology--domain-readme)

---

## 5. Object families

**CONFIRMED catalog / PROPOSED implementation** _([DOM-HYD §C, §E], [ENCY §7.2.C], [Atlas §4.E])._

Identity rule (PROPOSED, deterministic basis): `source_id + object_role + temporal_scope + normalized_digest`. CONFIRMED temporal rule: source / observed / valid / retrieval / release / correction times remain distinct where material.

| Object family             | Geometry                | Purpose                                                            |
| ------------------------- | ----------------------- | ----------------------------------------------------------------- |
| `Watershed`               | Polygon                 | Top-level drainage area; aggregation anchor.                      |
| `HUCUnit`                 | Polygon                 | HUC at a declared digit level (HUC8/10/12); cross-temporal anchor. |
| `HydroFeature`            | Line / Polygon          | Hydrographic feature (stream, lake, reservoir, wetland).          |
| `ReachIdentity`           | Line (linked)           | Stable reach identity across NHD vintages; ambiguity → ABSTAIN.   |
| `GaugeSite`               | Point                   | USGS monitoring location with site metadata.                      |
| `FlowObservation`         | (linked to point + time)| Observed discharge reading at a site/time.                        |
| `WaterLevelObservation`   | (linked)                | Observed gage-height / stage reading.                             |
| `WaterQualityObservation` | (linked)                | Observed WQ parameter reading with qualifier & unit.              |
| `GroundwaterWell`         | Point                   | Registered well with construction/use metadata (rights-sensitive). |
| `AquiferObservation`      | (linked)                | Aquifer-state reading (level, withdrawal).                        |
| `NFHLZone`                | Polygon                 | FEMA regulatory flood-hazard zone; **regulatory role only.**      |
| `Hydrograph`              | Time series             | Flow or level series; Observed vs Modeled flagged per role.       |
| `UpstreamTrace`           | (line collection)       | Result of an upstream/downstream traversal.                       |
| `WaterUseLink`            | (edge)                  | Cross-domain link to agriculture / permits / withdrawals.         |
| `DroughtLink`             | (edge)                  | Cross-domain link to drought monitor / context.                   |
| `IrrigationLink`          | (edge)                  | Cross-domain link to irrigation systems / permits.                |

> [!NOTE]
> The Atlas §4.E object table CONFIRMS `Watershed`, `HUCUnit`, `HydroFeature`, `ReachIdentity`,
> `GaugeSite`, `FlowObservation`, `WaterLevelObservation`, `Water Quality Observation`,
> `Groundwater Well`, and `NFHLZone`. The remaining families (`AquiferObservation`,
> `Hydrograph`, `UpstreamTrace`, `*Link`) are INFERRED from the lane's coverage description and
> are PROPOSED until confirmed in `contracts/domains/hydrology/`.

<details>
<summary><b>Field shape note (PROPOSED)</b></summary>

Every object family is expected to carry at minimum:

- `object_type`, `schema_version`, `object_id`
- `source_id`, `source_role` _(authority | observation | regulatory/context | model | aggregate | administrative | candidate)_
- `geometry` (typed, CRS-tagged via Spatial Foundation rules)
- temporal fields: `observed_time`, `valid_time`, `source_time`, `retrieval_time`, `release_time`, `correction_time`
- `provisional_status` / qualifiers / parameter code / unit / uncertainty (where applicable)
- `evidence_ref` → resolves to an `EvidenceBundle`
- `spec_hash` (canonical-JSON digest, e.g. JCS + SHA-256)

Exact field names and the canonical role enum are NEEDS VERIFICATION against
`schemas/contracts/v1/domains/hydrology/` and the source-role ADR (ADR-S-04 / OPEN-DR-source-role).

</details>

[⬆ Back to top](#-hydrology--domain-readme)

---

## 6. Cross-lane relations

**CONFIRMED relations / PROPOSED bindings** _([Atlas §4.F])._ Each relation must preserve ownership, source role, sensitivity, and EvidenceBundle support.

```mermaid
flowchart TB
  SF["Spatial Foundation<br/>CRS · geometry · scale"] ==>|"clipping, projection,<br/>generalization tolerances"| HYD
  HYD["💧 Hydrology<br/>(owner)"]
  HYD -->|"HUC / watershed identity;<br/>soil-moisture, hydrologic group"| SOIL["Soil"]
  HYD -->|"wetland & reach identity"| HAB["Habitat"]
  HYD -->|"wetland & reach context"| FAUNA["Fauna"]
  HYD -->|"wetland & reach context"| FLORA["Flora"]
  HYD -->|"reach identity, water availability<br/>(flow is not yield)"| AG["Agriculture"]
  HYD -->|"observed flow/level as context;<br/>NFHL as regulatory context only"| HAZ["Hazards"]
  HYD -->|"floodplain, bridges, dams,<br/>utilities exposure context"| SETTLE["Settlements /<br/>Infrastructure"]
  HYD -->|"HUC / reach as<br/>temporal anchors"| FM["Frontier Matrix"]

  classDef owner fill:#e3f2fd,stroke:#1565c0,color:#000;
  classDef upstream fill:#f3e5f5,stroke:#6a1b9a,color:#000;
  class HYD owner;
  class SF upstream;
```

| Related lane                    | Relation type                                  | Constraint                                                                                  |
| ------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Spatial Foundation _(upstream)_ | CRS, geometry, generalization, scale rules     | Hydrology consumes Spatial Foundation conventions, never overrides them. _(INFERRED upstream edge.)_ |
| Hazards                         | Flood, drought, warning, declaration, resilience context | Observed flow/level is **context** for flood events; NFHL is **regulatory** context only.  |
| Soil                            | Soil moisture, hydrologic group, infiltration, runoff | HUC / watershed identity bounds soil hydrologic-group context.                          |
| Agriculture                     | Irrigation, drought stress, crop-water context | Reach identity & water availability bound irrigation; **observed flow is not a yield input** without modeling. |
| Settlements / Infrastructure    | Floodplain, bridges, dams, utilities exposure  | Reach proximity & HUC drive crossing analyses; do not override settlement identity.         |
| Habitat / Fauna / Flora         | Wetland / reach feeds habitat & occurrence context | Sensitive habitat / occurrence redaction rules still govern joins. _(INFERRED edges.)_  |
| Frontier Matrix                 | HUC / reach as cross-temporal anchors          | Water-availability cells anchor on HUC / reach identity. _(INFERRED edge.)_                 |

> [!NOTE]
> Atlas §4.F CONFIRMS the Hazards, Soil, Agriculture, and Settlements/Infrastructure edges.
> The Spatial Foundation, Habitat/Fauna/Flora, and Frontier Matrix edges are INFERRED from the
> lane coverage and cross-cutting doctrine; treat them as PROPOSED until confirmed.

[⬆ Back to top](#-hydrology--domain-readme)

---

## 7. Pipeline shape (RAW → PUBLISHED)

**CONFIRMED doctrine / PROPOSED lane application** _([DIRRULES], [DOM-HYD §H], [ENCY §7.2])._ Promotion is a governed state transition, not a file move.

| Stage              | Handling                                                                                                | Gate                                                                                                          | Status     |
| ------------------ | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------- |
| **RAW**            | Capture immutable source payload (or reference) with source role, rights, sensitivity, citation, time, hash. | `SourceDescriptor` exists.                                                                                | PROPOSED   |
| **WORK / QUARANTINE** | Normalize schema, geometry, time, identity, evidence, rights, policy. Hold failures explicitly.      | Validation & policy gates pass, **or** quarantine reason recorded.                                            | PROPOSED   |
| **PROCESSED**      | Emit validated normalized objects, receipts, public-safe candidates.                                    | `EvidenceRef` resolvable + `ValidationReport` + digest (`spec_hash`) closure.                                  | PROPOSED   |
| **CATALOG / TRIPLET** | Emit catalog records, `EvidenceBundle`s, graph/triplet projections, release candidates.              | Catalog / proof closure passes.                                                                               | PROPOSED   |
| **PUBLISHED**      | Serve released public-safe artifacts through governed APIs and manifests.                               | `ReleaseManifest`, correction path, rollback target (`RollbackCard`), and policy/review state all present.    | PROPOSED   |

> [!WARNING]
> **Watcher-as-non-publisher invariant.** Watchers and connectors **observe and propose**; they
> never publish. Connector output enters a work-candidate state, not `data/processed/`,
> `data/catalog/`, or `data/published/`. Writing directly to those from a connector violates
> the invariant. _([Atlas Pass-20 cross-cutting themes])._

[⬆ Back to top](#-hydrology--domain-readme)

---

## 8. Map & viewing products

**PROPOSED domain products / CONFIRMED cross-cutting products** _([DOM-HYD §G], [ENCY §7.2.G], [MAP-MASTER], [GAI])._ All public surfaces consume governed APIs only; raw/work/quarantine and canonical stores are not exposed.

- HUC8 / HUC10 / HUC12 watershed view and drilldown.
- Stream / reach overlay.
- Gauge / site time-series view with hydrograph panel.
- Flow / water-level time-slider.
- Water-quality layer with parameter & qualifier disclosure.
- Groundwater context (rights-permitting, with redaction).
- Irrigation / drought context overlays.
- **Regulatory flood-context layer (NFHL)** — labeled regulatory; never as observed event.
- **Observed flood-event layer** — distinct from the regulatory layer, with role badges.
- **Terrain-derived hydrology layer** (3DEP-derived; modeled/derived role).
- Upstream / downstream tracing tool.
- **Cross-cutting (CONFIRMED doctrine):** Evidence Drawer, time-aware state, trust badges, sensitivity-redacted view, correction / stale-state view, governed Focus Mode.

[⬆ Back to top](#-hydrology--domain-readme)

---

## 9. API / contract / schema surfaces (PROPOSED)

All surfaces below are **PROPOSED** _([DOM-HYD §J], [ENCY §7.2.J])._ Exact routes, DTO names, and schema file paths are UNKNOWN until verified against `apps/governed-api/` and `schemas/contracts/v1/domains/hydrology/`.

| Surface                        | Proposed DTO / artifact                                | Finite outcomes                       | Status   |
| ------------------------------ | ------------------------------------------------------ | ------------------------------------- | -------- |
| Feature / detail resolver      | `HydrologyDecisionEnvelope`                            | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED; route TBD |
| Layer manifest resolver        | `LayerManifest` + hydrology layer descriptor           | `ANSWER` / `DENY` / `ERROR`           | PROPOSED; public-safe only |
| Evidence Drawer payload        | `EvidenceDrawerPayload` + `EvidenceBundle` projection  | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED; evidence & policy filtered |
| Focus Mode answer              | `RuntimeResponseEnvelope` + `AIReceipt`                | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED; AI never root truth |
| Evidence bundle fetch          | `GET /evidence/{evidence_ref}` → `EvidenceBundle`      | `ANSWER` / `DENY` / `ERROR`           | PROPOSED; route illustrative |
| Correction submit              | `POST /corrections` → `CorrectionNoticeCandidate`      | `ACCEPTED` / `DENY` / `ERROR`         | PROPOSED; route illustrative |
| Review decision                | `POST /review/.../decision` → `ReviewRecord`           | `ALLOW` / `RESTRICT` / `DENY` / `ERROR` | PROPOSED; route illustrative |

> [!NOTE]
> Schema responsibility root is `schemas/contracts/v1/...` per **ADR-0001 (schema-home rule)**;
> the `domains/hydrology/` segment under it is CONFLICTED per [§2](#2-repo-fit--directory-pattern)
> and [§17](#17-adrs--open-path-conflicts). Any `contracts/<domain>/<x>.schema.json` is
> lineage / CONFLICTED until migrated. The last three routes carry **illustrative** verbs/paths
> and are not Atlas-sourced.

[⬆ Back to top](#-hydrology--domain-readme)

---

## 10. Validators, tests, and fixtures (PROPOSED)

All entries below are **PROPOSED** _([DOM-HYD §K])._ Implementation against `tests/domains/hydrology/`, `fixtures/domains/hydrology/`, and a hydrology validator home (path NEEDS VERIFICATION) is unverified.

| Category                        | Validator / test                                                                                  | Status   |
| ------------------------------- | ------------------------------------------------------------------------------------------------- | -------- |
| Geometry & identity             | HUC12 fingerprint validation                                                                      | PROPOSED |
| Identity ambiguity              | NHDPlus HR identity-ambiguity tests (fail-closed on multi-COMID matches)                          | PROPOSED |
| Observation integrity           | USGS parameter / unit / qualifier / no-data tests                                                 | PROPOSED |
| Role separation                 | NFHL role-separation tests (DENY when NFHL cited as observed/forecast)                            | PROPOSED |
| Evidence closure                | `EvidenceBundle` closure tests (every claim resolves to admissible support)                       | PROPOSED |
| Offline fixture                 | No-network hydrology proof fixture (deterministic, side-effect-free)                              | PROPOSED |
| COMID ↔ HUC12 crosswalk         | Structural, governance, and hydrologic-sanity gates (alignment-score floor, decision-reason enum) | PROPOSED |
| Source-head drift               | ETag / Last-Modified / content-hash drift detection                                               | PROPOSED |
| Stale-state                     | Stale source / stale release fixture → triggers `ABSTAIN` or stale badge                          | PROPOSED |
| `spec_hash` determinism         | Canonical-JSON digest stability across environments                                               | PROPOSED |
| Trust-membrane                  | No public route reads from `data/raw/`, `data/work/`, `data/quarantine/`, or canonical stores     | PROPOSED |

<details>
<summary><b>Recommended negative-fixture catalog (PROPOSED, illustrative)</b></summary>

```text
fixtures/domains/hydrology/
├── valid/
│   ├── huc12_kansas_sample.json
│   ├── usgs_gauge_obs_window.json
│   ├── nhdplus_reach_identity.json
│   └── nfhl_zone_context.json
└── invalid/
    ├── invalid_huc12_length.json          → DENY
    ├── missing_source_role.json           → DENY
    ├── nfhl_as_observed_event.json        → DENY
    ├── ambiguous_reach_identity.json      → ABSTAIN
    ├── missing_spec_hash.json             → DENY
    ├── raw_path_exposure.json             → DENY
    ├── stale_source_head.json             → ABSTAIN
    ├── unresolved_evidence_ref.json       → DENY
    └── parameter_unit_mismatch.json       → DENY
```

Finite-outcome expectations:

| Outcome    | Meaning                                    |
| ---------- | ------------------------------------------ |
| `ANSWER`   | Valid, authoritative.                      |
| `ABSTAIN`  | No defensible mapping / stale / ambiguous. |
| `DENY`     | Policy, role, or sensitivity violation.    |
| `ERROR`    | Structural / runtime failure.              |

Validator exit-code → outcome mapping is **ADR-class and OPEN** (OPEN-DR-03; see
[§17](#17-adrs--open-path-conflicts)). The filenames above are illustrative, not Atlas-sourced.

</details>

[⬆ Back to top](#-hydrology--domain-readme)

---

## 11. Sensitivity, rights, & publication posture

**CONFIRMED / PROPOSED** _([DOM-HYD §I], [ENCY §7.2.I])._ For the full lane posture, see
[`docs/domains/hydrology/PUBLICATION_POSTURE.md`](./PUBLICATION_POSTURE.md).

> [!IMPORTANT]
> Hydrology denies unclear rights and flood-role misuse. **NFHL-as-observed-flood claims are
> denied.** Infrastructure and private-property implications (well locations, dam internals,
> water-right owner identity) require steward review before any public surface exposure.

CONFIRMED doctrine: **publication is fail-closed.** Any of the following blocks public promotion:

- Unclear or unresolved rights state on a constituent source.
- Unresolved source role (`source_role` undefined or in conflict).
- Missing or unresolvable `EvidenceRef`.
- Unresolved sensitivity (well ownership, infrastructure exposure, restricted joins).
- Absent release state (`ReleaseManifest` or rollback target missing).
- Stale source-head without explicit stale-state handling.
- Operational-warning content presented as KFM authority rather than cited, attributed context.

Transforms applied to make material public-safe (generalization, redaction, aggregation) are
recorded via receipts (e.g., `RedactionReceipt`, `AggregationReceipt`) and reproducible.

> [!NOTE]
> Hydrology is **not** primarily a sensitive-location lane like Archaeology, Fauna, Flora, or
> People/DNA. Its sensitivity surface concentrates in **infrastructure exposure** and
> **private-property implication**. Route any genuinely sensitive disposition through the
> operating contract's §23.2 sensitive-domain decision matrix rather than re-deriving it here.

[⬆ Back to top](#-hydrology--domain-readme)

---

## 12. Governed AI behavior

**CONFIRMED doctrine / PROPOSED implementation** _([GAI], [DOM-HYD §L])._

<details>
<summary><b>What AI <i>may</i> do for hydrology</b></summary>

- Summarize released hydrology `EvidenceBundle`s.
- Compare cited evidence across sources.
- Explain limitations, source roles, vintages, and uncertainty.
- Draft steward-review notes.
- Project Focus Mode answers grounded in resolved `EvidenceBundle`s.

</details>

<details>
<summary><b>What AI <i>must abstain or deny</i> on</b></summary>

- **ABSTAIN** when `EvidenceBundle` is missing, citations cannot be validated, source roles conflict, temporal scope is insufficient, or the request implies unsupported inference (e.g., predicting future flooding).
- **DENY** direct `data/raw/` / `data/work/` / `data/quarantine/` exposure, sensitive-location exposure, restricted personal/owner inference, **emergency-alerting / life-safety replacement**, or uncited authoritative claims.
- Every response carries an `AIReceipt` and a `RuntimeResponseEnvelope` with finite outcome `ANSWER | ABSTAIN | DENY | ERROR`, `evidence_refs`, `policy_decision`, and citation validation.

</details>

> [!CAUTION]
> A request that frames a KFM Hydrology answer as a flood warning, evacuation instruction, or
> other life-safety directive returns **DENY**. KFM presents cited, time-stamped evidence; it is
> never the alerting authority _([Atlas §20.4 emergency-alert boundary])._

[⬆ Back to top](#-hydrology--domain-readme)

---

## 13. Publication, correction, & rollback

**CONFIRMED doctrine / PROPOSED implementation** _([DOM-HYD §M], [ENCY Appendix E], [Atlas §24.2])._

<details open>
<summary><b>Required for any hydrology publication</b></summary>

- `ReleaseManifest` — the single signed, hashable artifact listing every dataset, bundle, and tile archive in the release.
- Resolvable `EvidenceBundle` for every public claim.
- `ValidationReport`(s) supporting normalization & integrity.
- `PolicyDecision` granting public exposure (rights, sensitivity, role checks pass).
- `ReviewRecord`(s) where steward review is required (new source admission, sensitive joins; author ≠ release authority when material).
- `CorrectionNotice` path for downstream consumers.
- Stale-state rule + freshness handling.
- Rollback target (`RollbackCard`) naming the previous release, with a rehearsed rollback drill.

</details>

CONFIRMED doctrine: KFM separates **stale** from **wrong**. A correction (`PUBLISHED → PUBLISHED'`)
must list invalidated derivatives; a rollback (`PUBLISHED → prior release`) reverts the manifest
and invalidates downstream derivatives. **No silent edits.**

> [!TIP]
> If any required artifact is missing, the publication **does not advance** and the candidate
> remains at `release/candidates/hydrology/` with a recorded reason. A release missing a
> `ReleaseManifest` or rollback target is a release-queue anti-pattern (Atlas §24.9.2): the
> public surface cannot be rolled back and the release is not auditable → `HOLD` / `DENY`.

[⬆ Back to top](#-hydrology--domain-readme)

---

## 14. Thin-slice plan

**PROPOSED first credible slice** _([DOM-HYD §N], [IMPL-PIPE §10.2], [Atlas §21 phase 5])._

> One Kansas **HUC12** public-safe fixture + **`SourceDescriptor`** + one **USGS gauge** fixture
> + one **NHDPlus identity crosswalk** + **NFHL contextual overlay** + **hydrograph panel** +
> **`EvidenceBundle` closure** + **`LayerManifest` / `MapReleaseManifest` dry run** + **ABSTAIN**
> on ambiguous reach identity. Guardrail: **never label NFHL as observed flood** _([Atlas §21 phase-5 rollback posture])._

The slice is deliberately narrow — one domain, one representative query — to prove the runtime
stack end-to-end as a cheap, repeatable CI check (the reusable runtime-proof-lane methodology,
Atlas `KFM-P6-IDEA-0001`). Recommended build order (validators → negative-path tests → policy →
proof → publication):

1. `README.md` (this file).
2. Object & source-role contracts in `contracts/domains/hydrology/`.
3. JSON schemas in `schemas/contracts/v1/domains/hydrology/`.
4. Offline fixtures (valid + invalid) in `fixtures/domains/hydrology/`.
5. Validator CLI(s) (validator home NEEDS VERIFICATION).
6. Negative-path tests in `tests/domains/hydrology/`.
7. CI gates wired (placeholder `.github/workflows/<name>.yml`).
8. Policy bundle in `policy/domains/hydrology/`.
9. Catalog/proof closure → `data/catalog/domain/hydrology/`, `data/proofs/`.
10. `ReleaseManifest` + `RollbackCard` rehearsal → first public-safe release.

[⬆ Back to top](#-hydrology--domain-readme)

---

## 15. Verification backlog & open questions

These items remain `NEEDS VERIFICATION` / `OPEN` before the lane's docs and code are mergeable.

| #  | Item                                                                                                  | Evidence that would settle it                                  | Status              |
| -- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ------------------- |
| 1  | Confirm `docs/domains/hydrology/` exists and follows the Directory Rules README contract.             | Direct mounted-repo inspection.                                | NEEDS VERIFICATION  |
| 2  | **Resolve schema/contract path form:** `.../domains/hydrology/` (DIRRULES §12) vs `.../hydrology/` (Atlas §24.13). | ADR + accepted Directory Rules / Atlas reconciliation. | CONFLICTED          |
| 3  | Confirm `schemas/contracts/v1/...` is the schema home (ADR-0001).                                     | Mounted schemas tree + accepted ADR-0001.                      | NEEDS VERIFICATION  |
| 4  | Validator exit-code → finite-outcome contract (cross-tool standard).                                  | ADR (OPEN-DR-03) + tooling audit.                              | OPEN ADR            |
| 5  | Source-role anti-collapse ADR (formalize `observation ≠ regulatory ≠ model ≠ aggregate`).             | ADR drafted, accepted, wired into policy + validators (ADR-S-04). | OPEN ADR         |
| 6  | NHDPlus version lock (v2.1 vs HR vs 3DHP); forbid mixing snapshots without `nhdplus_version`.         | SourceDescriptor schema + crosswalk validator coverage.        | NEEDS VERIFICATION  |
| 7  | USGS Water Data API endpoint posture (legacy vs current `api.waterdata.usgs.gov`).                    | Connector code review + SourceDescriptor entries.              | NEEDS VERIFICATION  |
| 8  | `EvidenceBundle` extension fields for hydrology (`observation_basis`, `units`, `temporal_basis`).      | Confirmed schema diff in evidence schema home.                 | PROPOSED            |
| 9  | Sensitive-content posture for well locations, dam internals, infrastructure exposure.                  | `policy/sensitivity/` rules + enforcement tests.               | NEEDS VERIFICATION  |
| 10 | Public-route discipline — verify `apps/explorer-web/` never reads `data/processed/hydrology/` directly. | Trust-membrane integration tests.                            | NEEDS VERIFICATION  |
| 11 | Confirm the canonical web shell is `apps/explorer-web/` (not `apps/web/`) for hydrology Focus surfaces. | DIRRULES §11 + live-repo evidence (CONFIRMED at commit `b6a279…`). | CONFIRMED (DIRRULES) |
| 12 | Hydrology connector list and per-connector rights state.                                              | `data/registry/sources/hydrology/` entries.                    | NEEDS VERIFICATION  |
| 13 | Source-role registry entry per source family.                                                         | `data/registry/sources/hydrology/<source>.yaml` + schema check. | PROPOSED            |
| 14 | Cadence policy — observational sources (USGS gauges) vs low-churn (WBD, NHDPlus HR snapshots).         | `policy/promotion/` cadence rules.                             | OPEN ADR            |
| 15 | Confirm the Directory Rules section number for the "Required README contract" cited in this doc.       | DIRRULES inspection (cited as §15 in prior draft — unverified). | NEEDS VERIFICATION  |

[⬆ Back to top](#-hydrology--domain-readme)

---

## 16. Related folders & docs

**Doctrine & dossiers**

- `ai-build-operating-contract.md` — canonical operating contract (`CONTRACT_VERSION = "3.0.0"`).
- `KFM_Encyclopedia` §7.2 Hydrology — primary doctrinal source `[ENCY]`.
- `Kansas_Frontier_Matrix_-_Domains_v1_1___Pass_23_32_Consolidated_Atlas` §4 Hydrology + §24.1 source-role anti-collapse + §24.13 dossier ↔ responsibility-root crosswalk `[DOM-HYD]`.
- `KFM_Unified_Implementation_Architecture_Build_Manual` §10.2 — identifies hydrology as the first proof-lane candidate `[IMPL-PIPE]`.
- `directory-rules.md` §12 (Domain Placement Law).
- [`docs/domains/hydrology/PUBLICATION_POSTURE.md`](./PUBLICATION_POSTURE.md) — lane publication posture.

**Lane siblings (PROPOSED placements — NEEDS VERIFICATION; path form CONFLICTED per §17)**

- [`contracts/domains/hydrology/`](../../../contracts/domains/hydrology/) — semantic object meaning.
- [`schemas/contracts/v1/domains/hydrology/`](../../../schemas/contracts/v1/domains/hydrology/) — JSON Schemas.
- [`policy/domains/hydrology/`](../../../policy/domains/hydrology/) — admissibility & publication policy.
- [`tests/domains/hydrology/`](../../../tests/domains/hydrology/) — enforcement tests.
- [`fixtures/domains/hydrology/`](../../../fixtures/domains/hydrology/) — valid & invalid fixtures.
- [`pipelines/domains/hydrology/`](../../../pipelines/domains/hydrology/) — pipeline logic.
- [`pipeline_specs/hydrology/`](../../../pipeline_specs/hydrology/) — declarative specs.
- [`data/registry/sources/hydrology/`](../../../data/registry/sources/hydrology/) — `SourceDescriptor` entries.
- [`release/candidates/hydrology/`](../../../release/candidates/hydrology/) — release decisions.

**Standards profiles** _(naming convention is itself OPEN — `PROV.md` vs `PROVENANCE.md`, OPEN-DR-01)_

- `docs/standards/PROV.md` — provenance vocabulary _(naming variance, OPEN-DR-01)_.
- `docs/standards/PMTILES.md`, `docs/standards/OGC-API-TILES.md` — public tile delivery posture.
- `docs/standards/OAI-PMH.md`, `docs/standards/ISO-19115.md` — metadata harvest & crosswalk posture.

> [!NOTE]
> All link targets above are **PROPOSED** until verified in the mounted repo. Broken links are a
> drift signal; report via [`docs/registers/DRIFT_REGISTER.md`](../../registers/DRIFT_REGISTER.md).

[⬆ Back to top](#-hydrology--domain-readme)

---

## 17. ADRs & open path conflicts

| ID                          | Title                                                            | Status                          |
| --------------------------- | ---------------------------------------------------------------- | ------------------------------- |
| **ADR-0001**                | Schema-home rule (`schemas/contracts/v1/...` canonical)          | Accepted (DIRRULES-referenced)  |
| **OPEN-DR-HYD-PATH**        | Lane path form: `.../domains/hydrology/` (DIRRULES §12) vs `.../hydrology/` (Atlas §24.13) | **CONFLICTED / open** |
| **ADR-S-04** _(source-role)_| Source-role vocabulary & anti-collapse (`observation ≠ model ≠ regulatory ≠ aggregate`) | **Open / proposed** |
| **OPEN-DR-03** _(exit-codes)_| Validator exit-code → finite-outcome contract                  | **Open / proposed (ADR-class)** |
| **OPEN-DR-01** _(prov-naming)_| `PROV.md` vs `PROVENANCE.md` naming                            | **Open / proposed**             |
| **ADR-S-12** _(low-churn)_  | Connector cadence & quarantine-recovery (HEAD-only drift, annual promotion review) | **Open / proposed** |

> [!CAUTION]
> **OPEN-DR-HYD-PATH is the highest-priority conflict on this lane.** Until reconciled, every
> `schemas/contracts/v1/domains/hydrology/` and `contracts/domains/hydrology/` reference in this
> README is the **Directory Rules form** (which wins on path questions) and is simultaneously
> **CONFLICTED** with the Atlas crosswalk form. Log it in `docs/registers/DRIFT_REGISTER.md`.

[⬆ Back to top](#-hydrology--domain-readme)

---

### <a id="last-reviewed"></a>Last reviewed

`2026-06-07` — _v2 update-and-polish pass; surfaced the §24.13-vs-§12 path conflict, the
emergency-alert-boundary DENY, the canonical `apps/explorer-web/` shell, and Atlas-vs-INFERRED
provenance on object/relation tables. Pending review by hydrology stewards and a Directory Rules
conformance review._

> Older than 6 months → flag for review (freshness rule, DIRRULES — section number NEEDS VERIFICATION).

---

**Related docs:** [`docs/domains/hydrology/PUBLICATION_POSTURE.md`](./PUBLICATION_POSTURE.md) · [`docs/standards/`](../../standards/) · [`docs/runbooks/`](../../runbooks/) · [`docs/architecture/`](../../architecture/) · [`docs/registers/DRIFT_REGISTER.md`](../../registers/DRIFT_REGISTER.md) · [`directory-rules.md`](../../../directory-rules.md) · [`ai-build-operating-contract.md`](../../../ai-build-operating-contract.md)

*Last updated: 2026-06-07 · `CONTRACT_VERSION = "3.0.0"` · status: `draft`*

[⬆ Back to top](#-hydrology--domain-readme)
