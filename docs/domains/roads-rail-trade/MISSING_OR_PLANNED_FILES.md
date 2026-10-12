<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs.domains.roads-rail-trade.missing-or-planned-files
title: Roads, Rail, and Trade Routes — Missing or Planned Files
type: standard
version: v0.2
status: draft
owners: Roads/Rail/Trade domain steward (PLACEHOLDER) + Directory Rules steward (PLACEHOLDER)
created: 2026-05-19
updated: 2026-06-07
policy_label: public
related:
  - docs/doctrine/directory-rules.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/domains/roads-rail-trade/README.md
  - docs/domains/roads-rail-trade/FILE_SYSTEM_PLAN.md
  - docs/domains/roads-rail-trade/DATA_LIFECYCLE.md
  - docs/domains/roads-rail-trade/EXPANSION_BACKLOG.md
  - docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf
  - ai-build-operating-contract.md            # CONTRACT_VERSION = "3.0.0"
tags: [kfm, roads, rail, trade, transport, planning, directory-rules, backlog]
notes:
  - CONTRACT_VERSION = "3.0.0" pinned; planning register (inventory, not roadmap).
  - Repository not mounted in this session; all path claims are PROPOSED unless cited to doctrine.
  - Tracks the roads-rail-trade domain lane file inventory per Directory Rules §12 (Domain Placement Law).
  - Known slug-vs-segment variance - docs/domains/roads-rail-trade/ (Directory Rules §12, verbatim) vs schemas/contracts/v1/transport/ (Atlas §24.13) - see §6; aligned to FILE_SYSTEM_PLAN OPEN-RRT-FSP-01.
  - This register overlaps the FILE_SYSTEM_PLAN companion; see §1 for the division of labor.
[/KFM_META_BLOCK_V2] -->
# 🛤️ Roads, Rail, and Trade Routes — Missing or Planned Files
> Working inventory of every file the **roads-rail-trade** domain lane is expected to carry under Directory Rules §12 (Domain Placement Law), what its placement should be, and whether it is currently **present, planned, missing, deferred, or unverified**.
[![Status: Draft](https://img.shields.io/badge/status-draft-yellow)](#)
[![Doc type: Planning Register](https://img.shields.io/badge/doc%20type-planning%20register-blueviolet)](#)
[![Domain: Roads · Rail · Trade](https://img.shields.io/badge/domain-roads--rail--trade-2b6cb0)](#)
[![Truth posture: cite-or-abstain](https://img.shields.io/badge/truth%20posture-cite--or--abstain-2e7d32)](#)
[![CONTRACT_VERSION: 3.0.0](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-555)](#)
[![Repo state: NOT MOUNTED](https://img.shields.io/badge/repo%20state-not%20mounted-red)](#)
[![Directory Rules: §12](https://img.shields.io/badge/directory--rules-%C2%A712%20domain%20placement-blue)](../../doctrine/directory-rules.md)
[![Atlas: v1.1 ch.13](https://img.shields.io/badge/atlas-v1.1%20ch.13-informational)](#)
| Field | Value |
|---|---|
| **Status** | `draft` — not yet reviewed |
| **Domain slug (Directory Rules §12)** | `roads-rail-trade` |
| **Schema segment (Atlas v1.1 §24.13)** | `transport` — *variance, ADR needed (ROADS-DR-01)* |
| **Atlas chapter** | Ch. 13 — Roads, Rail, and Trade Routes |
| **Source dossier short-name** | `[DOM-ROADS]` |
| **Owners** | Roads/Rail/Trade steward (PLACEHOLDER) + Directory Rules steward (PLACEHOLDER) |
| **Last updated** | 2026-06-07 |
| **Repository inspection** | ❌ not performed this session — every path claim is **PROPOSED** until verified |
---
## Contents
- [1. Purpose and scope](#1-purpose-and-scope)
- [2. How to read this register](#2-how-to-read-this-register)
- [3. Status legend](#3-status-legend)
- [4. Lane summary diagram](#4-lane-summary-diagram)
- [5. Domain context — Roads, Rail, and Trade Routes](#5-domain-context--roads-rail-and-trade-routes)
- [6. Naming variance — `roads-rail-trade` vs `transport`](#6-naming-variance--roads-rail-trade-vs-transport)
- [7. File inventory by responsibility root](#7-file-inventory-by-responsibility-root)
  - [7.1 `docs/domains/roads-rail-trade/`](#71-docsdomainsroads-rail-trade)
  - [7.2 `contracts/domains/roads-rail-trade/`](#72-contractsdomainsroads-rail-trade)
  - [7.3 `schemas/contracts/v1/...` (transport / domains)](#73-schemascontractsv1-transport--domains)
  - [7.4 `policy/domains/roads-rail-trade/`](#74-policydomainsroads-rail-trade)
  - [7.5 `tests/domains/roads-rail-trade/`](#75-testsdomainsroads-rail-trade)
  - [7.6 `fixtures/domains/roads-rail-trade/`](#76-fixturesdomainsroads-rail-trade)
  - [7.7 `packages/domains/roads-rail-trade/`](#77-packagesdomainsroads-rail-trade)
  - [7.8 `pipelines/domains/roads-rail-trade/` and `pipeline_specs/roads-rail-trade/`](#78-pipelinesdomainsroads-rail-trade-and-pipeline_specsroads-rail-trade)
  - [7.9 `data/<phase>/roads-rail-trade/` (lifecycle lanes)](#79-dataphaseroads-rail-trade-lifecycle-lanes)
  - [7.10 `release/candidates/roads-rail-trade/`](#710-releasecandidatesroads-rail-trade)
  - [7.11 Connectors, registries, control plane](#711-connectors-registries-control-plane)
- [8. Cross-domain references](#8-cross-domain-references)
- [9. Open questions and verification backlog](#9-open-questions-and-verification-backlog)
- [10. Promotion and intake workflow](#10-promotion-and-intake-workflow)
- [11. Related docs](#11-related-docs)
- [12. Change log](#12-change-log)
---
## 1. Purpose and scope
This document is the **planning register** for the roads-rail-trade domain. It enumerates the files that the project's doctrine — Directory Rules §12 (Domain Placement Law), Atlas v1.1 Ch. 13 (Roads / Rail / Trade Routes), and the Encyclopedia spine — implies should exist for this domain lane, and tracks each file's current status against the repository.

> [!NOTE]
> **Relationship to `FILE_SYSTEM_PLAN.md`.** The companion `FILE_SYSTEM_PLAN.md` is the *placement standard* — it states where each artifact class must live and why, per responsibility root. **This register is the *status tracker*** — it lists concrete expected files and marks each present / planned / missing / deferred / unverified. The two are complementary: `FILE_SYSTEM_PLAN.md` is the law, this is the checklist. Where they describe the same path, `FILE_SYSTEM_PLAN.md` is authoritative for placement and this register is authoritative for status.

> [!IMPORTANT]
> **This is a register, not a roadmap.** Inclusion of a file in any table below is **not** authorization to create it. Creation requires the Directory Rules §4 Placement Protocol, an owning per-root README (§15), and — where §2.4 applies — an ADR. The register exists so that *omissions are visible* and so that drift between doctrine and implementation can be detected.
> [!NOTE]
> **Scope.** This register tracks files **owned by or primarily serving** the roads-rail-trade domain lane. Files that legitimately span multiple domains (e.g., shared geometry validators, the Spatial Foundation reference frame) belong under non-domain segments per Directory Rules §12 "Multi-domain and cross-cutting files" and are intentionally **not** listed here.
[↑ back to top](#-roads-rail-and-trade-routes--missing-or-planned-files)
---
## 2. How to read this register
Each section below maps to one **responsibility root** under Directory Rules §3. Within each section, a table lists:
- **Path** — the PROPOSED file path under that root, following the Directory Rules §12 lane pattern.
- **Purpose** — one-line statement of what the file does.
- **Status** — present / planned / missing / deferred / NEEDS VERIFICATION (see §3).
- **Citation basis** — the doctrine source(s) that justify the file's existence.
- **Notes** — gating conditions, ADR dependencies, naming variances, or risks.
> [!WARNING]
> **No path here is authoritative.** Every concrete repo path is **PROPOSED** until verified against a mounted repository. The "Status" column reflects this session's inspection — which was **not** performed against a live repo. When the repo is mounted, statuses should be revised in a follow-up pass and reflected in the `Change log` (§12).
[↑ back to top](#-roads-rail-and-trade-routes--missing-or-planned-files)
---
## 3. Status legend
| Symbol | Status | Meaning |
|:---:|---|---|
| ✅ | **present** | Verified in the mounted repo this session. (Currently unused — repo not mounted.) |
| 🟡 | **planned** | Path is PROPOSED in doctrine, an ADR, or a prior-session artifact; not yet authored. |
| 🔴 | **missing** | Doctrine clearly expects this file; no draft known to exist; gap is open. |
| ⏸️ | **deferred** | Doctrine expects this file but ADR or scoping decision blocks authoring (e.g., schema home pending ADR-0001 amendment). |
| 🔍 | **NEEDS VERIFICATION** | Existence or content cannot be determined this session; mounted-repo inspection required. |
| ⚠️ | **CONFLICTED** | Two or more candidate placements exist (e.g., parallel schema homes); ADR required. |
Truth labels per the project's standard discipline:
- **CONFIRMED** — verified from attached doctrine or workspace evidence this session.
- **PROPOSED** — design or placement not yet verified in implementation.
- **INFERRED** — reasonably derivable from visible evidence but not directly stated.
- **NEEDS VERIFICATION** — checkable, but not checked strongly enough to act as fact.
- **UNKNOWN** — not resolvable without more evidence.
[↑ back to top](#-roads-rail-and-trade-routes--missing-or-planned-files)
---
## 4. Lane summary diagram
The diagram below shows the **expected lane pattern** for the roads-rail-trade domain per Directory Rules §12. It is a *target shape*, not a claim about the current repo.
```mermaid
flowchart LR
  subgraph DOCS["docs/"]
    D1["docs/domains/roads-rail-trade/"]
  end
  subgraph SEM["Semantic meaning"]
    C1["contracts/domains/roads-rail-trade/"]
  end
  subgraph SHAPE["Machine shape"]
    S1["schemas/contracts/v1/domains/roads-rail-trade/ (or transport/ — variance §6)"]
  end
  subgraph POL["Admissibility"]
    P1["policy/domains/roads-rail-trade/"]
  end
  subgraph PROOF["Proof of enforceability"]
    T1["tests/domains/roads-rail-trade/"]
    F1["fixtures/domains/roads-rail-trade/"]
  end
  subgraph CODE["Executable"]
    PKG["packages/domains/roads-rail-trade/"]
    PIPE["pipelines/domains/roads-rail-trade/"]
    SPECS["pipeline_specs/roads-rail-trade/"]
    CONN["connectors/ (source-id)/"]
  end
  subgraph DATA["Lifecycle data"]
    R["data/raw/roads-rail-trade/"]
    W["data/work/roads-rail-trade/"]
    Q["data/quarantine/roads-rail-trade/"]
    PR["data/processed/roads-rail-trade/"]
    CAT["data/catalog/domain/roads-rail-trade/"]
    PUB["data/published/layers/roads-rail-trade/"]
    REG["data/registry/sources/roads-rail-trade/"]
  end
  subgraph REL["Release"]
    RC["release/candidates/roads-rail-trade/"]
  end
  D1 -. "documents" .-> C1
  C1 -. "shape implements meaning" .-> S1
  S1 -. "tested by" .-> T1
  T1 -. "consumes" .-> F1
  P1 -. "gates" .-> PROOF
  CONN -. "emits" .-> R
  R --> W
  W --> Q
  W --> PR
  PR --> CAT
  CAT --> PUB
  PIPE -. "driven by" .-> SPECS
  PIPE -. "uses" .-> PKG
  PUB -. "candidate for release" .-> RC
  classDef variance stroke:#d97706,stroke-width:2px,fill:#fef3c7,color:#000;
  class S1 variance;
```
> [!NOTE]
> The dashed lines are **doctrinal relationships** (Directory Rules §6.3–§6.5 and §9.1), not implementation arrows. The orange-bordered node marks a **known naming variance** discussed in §6.
[↑ back to top](#-roads-rail-and-trade-routes--missing-or-planned-files)
---
## 5. Domain context — Roads, Rail, and Trade Routes
CONFIRMED doctrine (Atlas v1.1 Ch. 13.A–B, `[DOM-ROADS]` `[ENCY]`): this domain governs Kansas roads, rail, historic routes, trade and mobility corridors, restrictions, facilities, graph projections, catalog/proof/release objects, governed APIs, MapLibre UI, Evidence Drawer, Focus Mode, correction, and rollback.
**This domain owns** (Atlas v1.1 §13.B):
> Road Segment · Historic Route · Rail Segment · Depot · Siding · Yard · Crossing · Bridge · Ferry · River Crossing · Freight Corridor · Route Event · Operator Status · Access Restriction · Network Edge · Movement Story Node

> [!NOTE]
> **Naming inconsistency (CONFLICTED).** The §13.B owns-list spells the object `Historic Route`; the §13.C ubiquitous-language table and §13.G viewing products spell it `Historic RouteClaim`. Both are confirmed-present in the corpus — see the companion `HISTORIC_ROUTES.md` (OQ-RRT-HR-04). This register uses `Historic RouteClaim` in contract/schema filenames and flags the inconsistency.

**This domain explicitly does not own** (Atlas v1.1 §13.B):
| Concern | Owner |
|---|---|
| Settlement and infrastructure canonical claims | Settlements/Infrastructure |
| Water evidence (bridge/ferry/ford context only) | Hydrology |
| Site truth and sensitivity for archaeological resources | Archaeology |
| Living-person and land-parcel claims | People/Land |
| Hazard event authority | Hazards |
**Source families** (Atlas v1.1 §13.D, plus Pass-10 C10-05 expansion):
| Source family | Typical role | Sensitivity / rights | Status |
|---|---|---|---|
| Census TIGER/Line roads | observation / context | NEEDS VERIFICATION | CONFIRMED in doctrine |
| FHWA HPMS | observation / context | NEEDS VERIFICATION | CONFIRMED in doctrine |
| FHWA National Highway Freight Network | observation | NEEDS VERIFICATION | CONFIRMED in doctrine |
| WZDx feeds (Work Zone Data Exchange v4.x) | observation, near-real-time | NEEDS VERIFICATION | CONFIRMED in doctrine |
| KDOT / KanPlan / KanDrive / Kansas GIS | authority (Kansas) | NEEDS VERIFICATION | CONFIRMED in doctrine |
| County/state bridge and restriction data | authority / observation | NEEDS VERIFICATION | CONFIRMED in doctrine |
| GNIS names (place anchor) | observation | public | CONFIRMED in doctrine |
| OpenStreetMap | context / model (candidate) | ODbL terms, legal-status DENY | CONFIRMED in doctrine |
| FRA GCIS (grade crossings) | authority | NEEDS VERIFICATION | INFERRED from Pass-10 C10-05 |
| FRA Form 57 (rail incidents) | authority | NEEDS VERIFICATION | INFERRED from Pass-10 C10-05 |
| STB Class I weekly reports | authority | NEEDS VERIFICATION | INFERRED from Pass-10 C10-05 |
| HIFLD / NTAD (rail geospatial) | context | NEEDS VERIFICATION | INFERRED from Pass-10 C10-05 |
| GTFS / GTFS-RT (transit) | observation | NEEDS VERIFICATION | INFERRED from Pass-10 C10-04 |

> [!NOTE]
> The eight families above the divider are the **CONFIRMED Atlas §13.D set**; the five below are the **Pass-10 C10-05 / C10-04 rail-and-transit expansion** (Rail Stack: FRA GCIS / Form 57 / STB Class I / HIFLD / NTAD; Transit Stack: GTFS / GTFS-RT). The canonical final source set is ROADS-V-11.

**Source-role mapping (CONFIRMED — Atlas §24.1).** Each source's role is one of the seven canonical roles `observed | regulatory | modeled | aggregate | administrative | candidate | synthetic`, fixed at admission. Note that FHWA/regulatory designations are `regulatory`, not `observed`; OSM is `candidate`; a published "facility roster" is `administrative` — and per §24.1.2 an administrative compilation cited as an observed event timeline is a **DENY** for Roads. See `IDENTITY_MODEL.md` §7.

**Sensitivity posture** (Atlas v1.1 §13.I, CONFIRMED doctrine): Indigenous trade and mobility corridors, oral history, treaty, cultural, and interpretive evidence default to **steward review and generalized public geometry**. Critical transport facilities require review. Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state blocks public promotion. See `HISTORIC_ROUTES.md` for the full disposition.
[↑ back to top](#-roads-rail-and-trade-routes--missing-or-planned-files)
---
## 6. Naming variance — `roads-rail-trade` vs `transport`
> [!WARNING]
> **ROADS-DR-01 — Domain folder slug vs schema-home segment.** Two project sources name this domain's repo home differently. The companion `FILE_SYSTEM_PLAN.md` verified that Directory Rules §12 names `roads-rail-trade` **verbatim**, making §12 the stronger placement authority; Atlas §24.13 self-marks its paths PROPOSED. This is tracked across the whole Roads/Rail dossier as one conflict (OPEN-RRT-FSP-01).
| Surface | Slug used | Source |
|---|---|---|
| Directory Rules §12 Domain Placement Law (verbatim list) | `roads-rail-trade` | **CONFIRMED — `directory-rules.md` §12 names it verbatim** |
| Directory Rules §6.1 `docs/` tree | `roads-rail-trade/` | CONFIRMED — `directory-rules.md` §6.1 |
| Atlas v1.1 §24.13 (Atlas ↔ Dossier ↔ Responsibility-Root Crosswalk) | `transport` | CONFIRMED — `schemas/contracts/v1/transport/`, `contracts/transport/`; row self-marked PROPOSED |
| Atlas v1.1 §24.13 notes | "Network identity governance" | CONFIRMED |
| Encyclopedia §7.1 | `transport` (mirrors §24.13) | CONFIRMED |
| Deep-research report | classifies this as a "slug drift requiring ADR resolution" | CONFIRMED |
**Why this matters.** Per Directory Rules §13.5 the *Schema mirror divergence* anti-pattern is "`schemas/` and `contracts/` (or `policies/` and `policy/`) evolve separately." A slug-vs-segment split that crosses responsibility roots — `docs/domains/roads-rail-trade/` but `contracts/transport/` — risks the same drift. Either:
- **Option A — slug parity.** Use `roads-rail-trade` everywhere: `docs/domains/roads-rail-trade/`, `schemas/contracts/v1/domains/roads-rail-trade/`, `contracts/domains/roads-rail-trade/`, etc. Matches Directory Rules §12 literally. ADR amends Atlas v1.1 §24.13.
- **Option B — semantic parity.** Use `transport` as the short, domain-meaning segment in `schemas/`, `contracts/`, and `policy/` (per Atlas v1.1 §24.13); keep `roads-rail-trade` only as the `docs/domains/` slug and `data/<phase>/` lane label. ADR amends Directory Rules §12.
- **Option C — dual slug.** Maintain both; declare one as the canonical segment with the other as compatibility alias. ADR documents both.
This register's tables below show **both forms** wherever the variance applies, and mark every affected path ⚠️ **CONFLICTED** until ADR resolution.
**Recommended posture pending ADR (Option A bias).** Because Directory Rules §12 names `roads-rail-trade` verbatim and Atlas Ch. 24 explicitly defers to v1.0 / Directory Rules on conflict, treat the **§12 slug `roads-rail-trade`** as the canonical lane label across **all** responsibility roots (not only `docs/`, `tests/`, `fixtures/`, `data/`, `release/`, `packages/`, but also `schemas/`, `contracts/`, `policy/`), and record the `transport` segment in `docs/registers/DRIFT_REGISTER.md` until reconciled.
| Verification target | Evidence that would settle it |
|---|---|
| Whether Directory Rules §12 list was authored before or after Atlas v1.1 §24.13 | Git log + commit metadata on `directory-rules.md` and the Atlas PDF generation date |
| Whether Atlas v1.1 §24.13 intended `transport` as a *short identifier* rather than a folder slug | Author intent in the Atlas v1.1 supersession appendix |
| Whether a prior-session ADR already settled this | `docs/adr/` inspection on a mounted repo |
| Whether other Atlas §24.13 rows have analogous variances (e.g., `settlements-infrastructure` vs `settlement`, `people-dna-land` vs `people`) | Cross-check all 14 rows in §24.13 against the Directory Rules §12 list |
[↑ back to top](#-roads-rail-and-trade-routes--missing-or-planned-files)
---
## 7. File inventory by responsibility root
> [!NOTE]
> Every path below is **PROPOSED** unless explicitly cited otherwise. The repository is not mounted in this session; ✅ "present" cannot truthfully be asserted for any row.
### 7.1 `docs/domains/roads-rail-trade/`
Human-facing documentation for the domain. Owned by `docs/` per Directory Rules §6.1.
| Path | Purpose | Status | Citation basis | Notes |
|---|---|:---:|---|---|
| `docs/domains/roads-rail-trade/README.md` | Domain entry-point: scope, boundaries, terminology, ownership, link-out hub | 🔴 | Directory Rules §15 (per-root README contract); Atlas v1.1 §13 | Should mirror Atlas v1.1 §13.A–N section headings |
| `docs/domains/roads-rail-trade/MISSING_OR_PLANNED_FILES.md` | **This file** — planning register | 🟡 | This document | Authored 2026-05-19; updated 2026-06-07 |
| `docs/domains/roads-rail-trade/FILE_SYSTEM_PLAN.md` | Placement *standard* (companion to this register) | 🟡 | Directory Rules §12 | Authored (companion); placement authority |
| `docs/domains/roads-rail-trade/DATA_LIFECYCLE.md` | RAW → PUBLISHED lifecycle standard for the lane | 🟡 | Atlas v1.1 §13.H | Authored (companion) |
| `docs/domains/roads-rail-trade/EXPANSION_BACKLOG.md` | Lane expansion backlog (Pass-10 tracks) | 🟡 | Pass-10 §10.4/§10.5 | Authored (companion) |
| `docs/domains/roads-rail-trade/GRAPH_PROJECTIONS.md` | Derived graph/connectivity view doctrine; non-canonical-truth rule | 🟡 | Atlas v1.1 §13.G; Encyclopedia §5.2 | Authored (companion) |
| `docs/domains/roads-rail-trade/HISTORIC_ROUTES.md` | Historic & Indigenous-corridor claim handling; sensitivity | 🟡 | Atlas v1.1 §13.B/§13.I; Pass-32 KFM-P20-PROG-0013 | Authored (companion); `Historic RouteClaim` semantics |
| `docs/domains/roads-rail-trade/IDENTITY_MODEL.md` | Identity composition + spec_hash + source-role | 🟡 | Atlas v1.1 §13.E, §24.1; Pass-10 C1-02 | Authored (companion) |
| `docs/domains/roads-rail-trade/MAP_UI_CONTRACTS.md` | Map-UI binding surface (LayerManifest, Evidence Drawer, Focus Mode) | 🟡 | MAP-MASTER §M; Atlas v1.1 §13.J | Authored (companion) |
| `docs/domains/roads-rail-trade/UBIQUITOUS_LANGUAGE.md` | Term glossary (Road Segment, Rail Segment, CorridorRoute, RouteMembership, Network Node, Crossing, TransportFacility, RestrictionEvent, StatusEvent, OperatorAssignment, Historic RouteClaim, TradeRouteCorridor) | 🔴 | Atlas v1.1 §13.C (CONFIRMED 12 terms) | DDD reference also cites Ubiquitous Language as pattern |
| `docs/domains/roads-rail-trade/OBJECT_FAMILIES.md` | Per-object purpose, identity rule, temporal handling | 🔴 | Atlas v1.1 §13.E (CONFIRMED list of 16 owned objects) | Should cross-reference `contracts/domains/roads-rail-trade/` |
| `docs/domains/roads-rail-trade/SOURCE_FAMILIES.md` | Per-source role, rights, freshness, ingest cadence | 🔴 | Atlas v1.1 §13.D; Pass-10 C10-05 (rail); Pass-10 C10-04 (transit) | Rights tier per source — NEEDS VERIFICATION |
| `docs/domains/roads-rail-trade/PIPELINE.md` | RAW → PUBLISHED diagram + per-stage gates for this domain | 🔴 | Atlas v1.1 §13.H | May be folded into `DATA_LIFECYCLE.md` — see ROADS-V-12 |
| `docs/domains/roads-rail-trade/SENSITIVITY.md` | Indigenous corridor posture, critical-facility review, historic uncertainty | 🔴 | Atlas v1.1 §13.I (CONFIRMED); `[DOM-ARCH]` cross-link required | May overlap `HISTORIC_ROUTES.md`; coordinate with archaeology sovereignty review |
| `docs/domains/roads-rail-trade/API_SURFACES.md` | Endpoint inventory and DTO map (RoadsRailDecisionEnvelope, LayerManifest, EvidenceDrawerPayload, AIReceipt) | 🔴 | Atlas v1.1 §13.J (PROPOSED; exact route UNKNOWN) | May overlap `MAP_UI_CONTRACTS.md`; endpoint routes NEEDS VERIFICATION |
| `docs/domains/roads-rail-trade/VERIFICATION_BACKLOG.md` | Domain-specific open questions (mirrors Atlas §13.N) | 🟡 | Atlas v1.1 §13.N (4 items) | May be folded into central `docs/registers/VERIFICATION_BACKLOG.md` — see ROADS-V-10 |
| `docs/domains/roads-rail-trade/CHANGELOG.md` | Lineage record for this domain's docs | 🟡 | DDD pattern; precedent from `docs/encyclopedia/` | Optional; depends on doc-velocity |
### 7.2 `contracts/domains/roads-rail-trade/`
Semantic meaning of domain objects (Markdown only — no `*.schema.json`). Per Directory Rules §13.1 (schema-in-contracts is drift).
> ⚠️ **CONFLICTED** path segment — Atlas v1.1 §24.13 uses `contracts/transport/`. See §6 (recommended posture: `domains/roads-rail-trade/`).
| Path (Option A — slug parity) | Purpose | Status | Citation basis | Notes |
|---|---|:---:|---|---|
| `contracts/domains/roads-rail-trade/README.md` | Per-root index of object meanings in this domain | 🔴 | Directory Rules §13.1, §15 | |
| `contracts/domains/roads-rail-trade/road_segment.md` | Meaning, invariants, time semantics for Road Segment | 🔴 | Atlas v1.1 §13.E | |
| `contracts/domains/roads-rail-trade/rail_segment.md` | Meaning, invariants for Rail Segment | 🔴 | Atlas v1.1 §13.E | |
| `contracts/domains/roads-rail-trade/historic_route_claim.md` | Claim semantics (not canonical geometry) | 🔴 | Atlas v1.1 §13.C; §13.I (overprecision DENY) | Tied to sensitivity policy; naming OQ-RRT-HR-04 |
| `contracts/domains/roads-rail-trade/trade_route_corridor.md` | Generalized corridor semantics | 🔴 | Atlas v1.1 §13.C | |
| `contracts/domains/roads-rail-trade/corridor_route.md` | Composite route identity rule | 🔴 | Atlas v1.1 §13.C | |
| `contracts/domains/roads-rail-trade/route_membership.md` | Membership relation between segments and a CorridorRoute | 🔴 | Atlas v1.1 §13.C | |
| `contracts/domains/roads-rail-trade/network_node.md` | Network identity governance unit | 🔴 | Atlas v1.1 §13.C; §24.13 notes ("Network identity governance") | |
| `contracts/domains/roads-rail-trade/network_edge.md` | Edge between Network Nodes | 🔴 | Atlas v1.1 §13.B | |
| `contracts/domains/roads-rail-trade/crossing.md` | Grade crossing semantics; FRA GCIS cross-reference | 🔴 | Atlas v1.1 §13.C; Pass-10 C10-05 | Coords disagreement (GCIS vs HIFLD) is a noted tension (ROADS-V-05) |
| `contracts/domains/roads-rail-trade/bridge.md` | Bridge semantics; Hydrology cross-lane link | 🔴 | Atlas v1.1 §13.B, §13.F | |
| `contracts/domains/roads-rail-trade/ferry.md` | Ferry semantics | 🔴 | Atlas v1.1 §13.E | |
| `contracts/domains/roads-rail-trade/river_crossing.md` | River-crossing semantics (ford/bridge/ferry) | 🔴 | Atlas v1.1 §13.B, §13.F | |
| `contracts/domains/roads-rail-trade/depot.md` | Depot semantics (rail) | 🔴 | Atlas v1.1 §13.B | |
| `contracts/domains/roads-rail-trade/siding.md` | Rail siding semantics | 🔴 | Atlas v1.1 §13.B | |
| `contracts/domains/roads-rail-trade/yard.md` | Rail yard semantics | 🔴 | Atlas v1.1 §13.B | |
| `contracts/domains/roads-rail-trade/transport_facility.md` | Generic transport facility (umbrella) | 🔴 | Atlas v1.1 §13.E | |
| `contracts/domains/roads-rail-trade/freight_corridor.md` | Freight corridor identity | 🔴 | Atlas v1.1 §13.B; FHWA NHFN source | |
| `contracts/domains/roads-rail-trade/route_event.md` | Route-level events (designation, decommission) | 🔴 | Atlas v1.1 §13.B | |
| `contracts/domains/roads-rail-trade/operator_status.md` | Operator/agency state at a point in time | 🔴 | Atlas v1.1 §13.B | |
| `contracts/domains/roads-rail-trade/operator_assignment.md` | OperatorAssignment relation semantics | 🔴 | Atlas v1.1 §13.C | |
| `contracts/domains/roads-rail-trade/access_restriction.md` | Access/closure/restriction semantics | 🔴 | Atlas v1.1 §13.B | |
| `contracts/domains/roads-rail-trade/restriction_event.md` | Time-bounded restriction event (e.g., WZDx work zone) | 🔴 | Atlas v1.1 §13.C; Pass-32 KFM-P8-PROG-0025 (WZDx v4.x) | |
| `contracts/domains/roads-rail-trade/status_event.md` | Time-bounded status change | 🔴 | Atlas v1.1 §13.C | |
| `contracts/domains/roads-rail-trade/movement_story_node.md` | Narrative anchor for movement stories | 🔴 | Atlas v1.1 §13.B | entity-vs-value-object: see IDENTITY_MODEL OQ-06 |
| `contracts/domains/roads-rail-trade/route_uncertainty_profile.md` | Per-route uncertainty profile (historic and modern) | 🔴 | Atlas v1.1 §13.N (item: "Implement RouteUncertaintyProfile") | Reconcile with doctrinal `UncertaintySurface` carrier (OQ-RRT-HR-05) |
### 7.3 `schemas/contracts/v1/...` (transport / domains)
Machine validation shape. Per Directory Rules §6.4 and **ADR-0001** (`schemas/contracts/v1/...` is canonical).
> ⚠️ **CONFLICTED** segment — Atlas v1.1 §24.13 lists `schemas/contracts/v1/transport/`; Directory Rules §12 names `schemas/contracts/v1/domains/roads-rail-trade/`. See §6 (recommended: `domains/roads-rail-trade/`).
| Path (showing both candidate forms) | Purpose | Status | Citation basis | Notes |
|---|---|:---:|---|---|
| `schemas/contracts/v1/domains/roads-rail-trade/README.md` OR `schemas/contracts/v1/transport/README.md` | Per-root index of machine schemas in this domain | 🔴 | Directory Rules §6.4, §15 | Pick one — §6 |
| `.../road_segment.schema.json` | JSON Schema for Road Segment | 🔴 | Atlas v1.1 §13.J ("Schema responsibility root: `schemas/contracts/v1/`") | |
| `.../rail_segment.schema.json` | JSON Schema for Rail Segment | 🔴 | Atlas v1.1 §13.J | |
| `.../historic_route_claim.schema.json` | JSON Schema for Historic Route Claim (includes overprecision DENY field constraints) | 🔴 | Atlas v1.1 §13.E, §13.I | |
| `.../trade_route_corridor.schema.json` | JSON Schema for Trade Route Corridor (generalized geometry) | 🔴 | Atlas v1.1 §13.C | |
| `.../corridor_route.schema.json` | JSON Schema for Corridor Route | 🔴 | Atlas v1.1 §13.C | |
| `.../route_membership.schema.json` | JSON Schema for Route Membership relation | 🔴 | Atlas v1.1 §13.C | |
| `.../network_node.schema.json` | JSON Schema for Network Node | 🔴 | Atlas v1.1 §13.C | |
| `.../network_edge.schema.json` | JSON Schema for Network Edge | 🔴 | Atlas v1.1 §13.B | |
| `.../crossing.schema.json` | JSON Schema for Crossing (with GCIS-compatible id space) | 🔴 | Atlas v1.1 §13.C; Pass-10 C10-05 | |
| `.../bridge.schema.json` | JSON Schema for Bridge | 🔴 | Atlas v1.1 §13.B | |
| `.../ferry.schema.json` | JSON Schema for Ferry | 🔴 | Atlas v1.1 §13.E | |
| `.../river_crossing.schema.json` | JSON Schema for River Crossing | 🔴 | Atlas v1.1 §13.B | |
| `.../depot.schema.json` | JSON Schema for Depot | 🔴 | Atlas v1.1 §13.B | |
| `.../siding.schema.json` | JSON Schema for Siding | 🔴 | Atlas v1.1 §13.B | |
| `.../yard.schema.json` | JSON Schema for Yard | 🔴 | Atlas v1.1 §13.B | |
| `.../transport_facility.schema.json` | JSON Schema for Transport Facility | 🔴 | Atlas v1.1 §13.E | |
| `.../freight_corridor.schema.json` | JSON Schema for Freight Corridor | 🔴 | Atlas v1.1 §13.B | |
| `.../route_event.schema.json` | JSON Schema for Route Event | 🔴 | Atlas v1.1 §13.B | |
| `.../operator_status.schema.json` | JSON Schema for Operator Status | 🔴 | Atlas v1.1 §13.B | |
| `.../operator_assignment.schema.json` | JSON Schema for Operator Assignment | 🔴 | Atlas v1.1 §13.C | |
| `.../access_restriction.schema.json` | JSON Schema for Access Restriction | 🔴 | Atlas v1.1 §13.B | |
| `.../restriction_event.schema.json` | JSON Schema for Restriction Event (WZDx-compatible) | 🔴 | Atlas v1.1 §13.C; Pass-32 KFM-P8-PROG-0025 | |
| `.../status_event.schema.json` | JSON Schema for Status Event | 🔴 | Atlas v1.1 §13.C | |
| `.../movement_story_node.schema.json` | JSON Schema for Movement Story Node | 🔴 | Atlas v1.1 §13.B | |
| `.../route_uncertainty_profile.schema.json` | JSON Schema for Route Uncertainty Profile | 🔴 | Atlas v1.1 §13.N (PROPOSED) | |
| `.../roads_rail_decision_envelope.schema.json` | JSON Schema for RoadsRailDecisionEnvelope (governed API DTO) | 🔴 | Atlas v1.1 §13.J; DecisionEnvelope shape KFM-P5-PROG-0001 | ANSWER / ABSTAIN / DENY / ERROR enum |
| `.../evidence_drawer_payload_roads.schema.json` | JSON Schema for Evidence Drawer payload projection in this domain | 🔴 | Atlas v1.1 §13.J; MAP-MASTER §M | UI family home is `schemas/contracts/v1/ui/` |
| `.../layer_manifest_roads.schema.json` | JSON Schema for layer manifest descriptor | 🔴 | Atlas v1.1 §13.J; MAP-MASTER §M | Map family home is `schemas/contracts/v1/map/` |
> [!NOTE]
> **Validity fixtures** for these schemas live under `schemas/tests/valid/roads-rail-trade/` and `schemas/tests/invalid/roads-rail-trade/` per Directory Rules §6.4 (separate from the cross-cutting `fixtures/` lane in §7.6).
### 7.4 `policy/domains/roads-rail-trade/`
Admissibility — allow / deny / restrict / abstain decisions. Per Directory Rules §6.5.
> ⚠️ **CONFLICTED** segment — see §6. Atlas v1.1 §24.13 does not explicitly call out a `policy/transport/` home; the Directory Rules pattern is `policy/domains/<slug>/`.
| Path | Purpose | Status | Citation basis | Notes |
|---|---|:---:|---|---|
| `policy/domains/roads-rail-trade/README.md` | Per-root index of policy bundles for this domain | 🔴 | Directory Rules §15 | |
| `policy/domains/roads-rail-trade/legal_status_deny.rego` | DENY when OSM / GNIS data is used as legal authority | 🔴 | Atlas v1.1 §13.K (PROPOSED test); §24.1.2 candidate-role guardrail | OSM/GNIS legal-status denial test |
| `policy/domains/roads-rail-trade/historic_overprecision_deny.rego` | DENY public exposure of overprecise historic geometry | 🔴 | Atlas v1.1 §13.K (PROPOSED test); §13.I sensitivity | Tied to `route_uncertainty_profile.schema.json` |
| `policy/domains/roads-rail-trade/indigenous_corridor_review.rego` | Require steward review for Indigenous trade/mobility corridors | 🔴 | Atlas v1.1 §13.I (CONFIRMED doctrine) | Consumes Archaeology-owned sensitivity policy |
| `policy/domains/roads-rail-trade/critical_facility_review.rego` | Require review for critical transport facilities (bridges, key crossings) | 🔴 | Atlas v1.1 §13.I (CONFIRMED doctrine) | Consumes Settlements `policy/sensitivity/infrastructure/` |
| `policy/domains/roads-rail-trade/route_designation_separation.rego` | Enforce separation between Route Designation, Route Membership, and Route Geometry | 🔴 | Atlas v1.1 §13.K (PROPOSED test: "Route membership and designation separation tests") | |
| `policy/domains/roads-rail-trade/operator_status_temporal.rego` | Enforce operator/status temporal validity | 🔴 | Atlas v1.1 §13.K (PROPOSED test) | |
| `policy/domains/roads-rail-trade/public_generalization_required.rego` | Public-release path MUST carry a generalization receipt | 🔴 | Atlas v1.1 §13.K (PROPOSED test); doctrine on Redaction Receipt | |
| `policy/domains/roads-rail-trade/graph_projection_non_canonical.rego` | DENY treating derived graph projections as canonical record source | 🔴 | Encyclopedia §5.2; doctrine on watcher-as-non-publisher | See `GRAPH_PROJECTIONS.md` |
| `policy/domains/roads-rail-trade/source_rights_gate.rego` | Per-source rights and current terms enforcement (TIGER, HPMS, NHFN, WZDx, KDOT, OSM, etc.) | 🔴 | Atlas v1.1 §13.D ("rights and current terms NEEDS VERIFICATION") | Per-source policy fragments |
### 7.5 `tests/domains/roads-rail-trade/`
Proof the rules are enforceable. Per Directory Rules §12 lane pattern.
| Path | Purpose | Status | Citation basis | Notes |
|---|---|:---:|---|---|
| `tests/domains/roads-rail-trade/README.md` | Per-root index of domain test layout | 🔴 | Directory Rules §15 | |
| `tests/domains/roads-rail-trade/test_route_designation_separation.py` | Route membership and designation separation tests | 🔴 | Atlas v1.1 §13.K (PROPOSED) | Negative-state rule applies |
| `tests/domains/roads-rail-trade/test_operator_status_temporal.py` | Operator/status temporal tests | 🔴 | Atlas v1.1 §13.K (PROPOSED) | |
| `tests/domains/roads-rail-trade/test_osm_gnis_legal_status_deny.py` | OSM/GNIS legal-status denial | 🔴 | Atlas v1.1 §13.K (PROPOSED) | |
| `tests/domains/roads-rail-trade/test_historic_overprecision_deny.py` | Historic overprecision denial | 🔴 | Atlas v1.1 §13.K (PROPOSED) | |
| `tests/domains/roads-rail-trade/test_public_generalization_receipt.py` | Public generalization receipt presence tests | 🔴 | Atlas v1.1 §13.K (PROPOSED) | |
| `tests/domains/roads-rail-trade/test_transport_graph_rollback.py` | Transport graph projection rollback tests | 🔴 | Atlas v1.1 §13.K (PROPOSED); §13.M | |
| `tests/domains/roads-rail-trade/test_wzdx_v4_validator.py` | WZDx v4.x roadworks validator and transformer | 🔴 | Pass-32 KFM-P8-PROG-0025 (CONFIRMED card; fail-closed schema gate) | |
| `tests/domains/roads-rail-trade/test_gcis_hifld_coords_disagreement.py` | GCIS vs HIFLD crossing coords disagreement handling | 🔴 | Pass-10 C10-05 (named open question) | (filename: HIFLD) |
| `tests/domains/roads-rail-trade/test_stb_snapshot_dedup.py` | STB Class I snapshot-week de-duplication | 🔴 | Pass-10 C10-05 (named tension) | |
| `tests/domains/roads-rail-trade/test_evidence_bundle_closure.py` | EvidenceBundle closure for domain claims | 🔴 | Atlas v1.1 §13.J, §13.M | |
| `tests/domains/roads-rail-trade/test_release_manifest_present.py` | ReleaseManifest presence on published artifacts | 🔴 | Atlas v1.1 §13.M | |
### 7.6 `fixtures/domains/roads-rail-trade/`
Golden valid / invalid sample data for tests. Per Directory Rules §12 lane pattern.
| Path | Purpose | Status | Citation basis | Notes |
|---|---|:---:|---|---|
| `fixtures/domains/roads-rail-trade/README.md` | Per-root index of fixtures | 🔴 | Directory Rules §15 | |
| `fixtures/domains/roads-rail-trade/valid/road_segment/` | Valid Road Segment examples | 🔴 | Schema testing standard | |
| `fixtures/domains/roads-rail-trade/valid/rail_segment/` | Valid Rail Segment examples | 🔴 | Schema testing standard | |
| `fixtures/domains/roads-rail-trade/valid/wzdx_v4/` | Valid WZDx v4.x payloads | 🔴 | Pass-32 KFM-P8-PROG-0025 | |
| `fixtures/domains/roads-rail-trade/valid/historic_route_claim/santa_fe_trail.json` | Santa Fe Trail claim fixture | 🔴 | Pass-32 KFM-P20-PROG-0013 (named) | Generalized geometry only |
| `fixtures/domains/roads-rail-trade/valid/historic_route_claim/pony_express.json` | Pony Express claim fixture | 🔴 | Pass-32 KFM-P20-PROG-0013 (named) | |
| `fixtures/domains/roads-rail-trade/valid/historic_route_claim/butterfield_smoky_hill.json` | Butterfield / Smoky Hill claim fixture | 🔴 | Pass-32 KFM-P20-PROG-0013 (named) | |
| `fixtures/domains/roads-rail-trade/valid/historic_route_claim/chisholm_trail.json` | Chisholm Trail claim fixture | 🔴 | Atlas v1.1 §13.B (historic routes) — **not** in KFM-P20-PROG-0013's named list | Generalized geometry only; see note below |
| `fixtures/domains/roads-rail-trade/invalid/overprecise_historic_geometry.json` | Trigger historic-overprecision DENY | 🔴 | Atlas v1.1 §13.K | |
| `fixtures/domains/roads-rail-trade/invalid/osm_as_legal_authority.json` | Trigger OSM/GNIS legal-status DENY | 🔴 | Atlas v1.1 §13.K | |
| `fixtures/domains/roads-rail-trade/invalid/missing_evidence_ref.json` | Trigger ABSTAIN on missing EvidenceRef | 🔴 | Atlas v1.1 §13.J | |
| `fixtures/domains/roads-rail-trade/invalid/operator_overlap.json` | Trigger temporal operator-status conflict | 🔴 | Atlas v1.1 §13.K | |
> [!NOTE]
> **Frontier-routes fixture scope (corrected).** Pass-32 `KFM-P20-PROG-0013` names exactly **Santa Fe Trail, Pony Express, Butterfield/Smoky Hill, forts, stations, and depots**. The Chisholm Trail is **not** in that card's list (it appears elsewhere in the corpus, e.g., the Dickinson/Abilene county build plan), so its fixture is justified by Atlas §13.B historic-routes scope, not by KFM-P20-PROG-0013. The companion catalog card `KFM-P20-PROG-0014` (frontier routes STAC collection builder; preserves `kfm_id, bbox, date uncertainty, confidence, source links`) is the STAC counterpart.
### 7.7 `packages/domains/roads-rail-trade/`
Shared library code used by multiple deployables. Per Directory Rules §12 lane pattern.
| Path | Purpose | Status | Citation basis | Notes |
|---|---|:---:|---|---|
| `packages/domains/roads-rail-trade/README.md` | Per-root index of domain libraries | 🔴 | Directory Rules §15 | |
| `packages/domains/roads-rail-trade/identity/` | Deterministic identity for Road Segment, Rail Segment, Crossing, etc. | 🔴 | Atlas v1.1 §13.E (PROPOSED identity rule); see `IDENTITY_MODEL.md` | |
| `packages/domains/roads-rail-trade/wzdx_v4_transformer/` | WZDx v4.x → GeoParquet/PMTiles transformer | 🔴 | Pass-32 KFM-P8-PROG-0025 | |
| `packages/domains/roads-rail-trade/graph_projection/` | Transport graph projection builder (non-canonical) | 🔴 | Encyclopedia §5.2; see `GRAPH_PROJECTIONS.md` | |
| `packages/domains/roads-rail-trade/generalization/` | Geometry generalization library with redaction-receipt emission | 🔴 | Atlas v1.1 §13.I, §13.K | |
| `packages/domains/roads-rail-trade/frontier_routes/` | Frontier routes FeatureCollection builder | 🔴 | Pass-32 KFM-P20-PROG-0013 | |
### 7.8 `pipelines/domains/roads-rail-trade/` and `pipeline_specs/roads-rail-trade/`
Executable pipeline logic + declarative pipeline configuration. Per Directory Rules §12 (note: `pipeline_specs/` takes the domain directly, **no** `domains/` segment).
| Path | Purpose | Status | Citation basis | Notes |
|---|---|:---:|---|---|
| `pipelines/domains/roads-rail-trade/README.md` | Per-root index | 🔴 | Directory Rules §15 | |
| `pipelines/domains/roads-rail-trade/ingest_tiger_roads.py` | TIGER/Line roads RAW capture | 🔴 | Atlas v1.1 §13.D, §13.H | |
| `pipelines/domains/roads-rail-trade/ingest_fhwa_hpms.py` | FHWA HPMS RAW capture | 🔴 | Atlas v1.1 §13.D | |
| `pipelines/domains/roads-rail-trade/ingest_fhwa_nhfn.py` | FHWA National Highway Freight Network RAW capture | 🔴 | Atlas v1.1 §13.D | |
| `pipelines/domains/roads-rail-trade/ingest_wzdx_v4.py` | WZDx v4.x feed RAW capture | 🔴 | Pass-32 KFM-P8-PROG-0025; KFM-P12-PROG-0005 (KDOT KanDrive+WZDx lane) | Near-real-time cadence |
| `pipelines/domains/roads-rail-trade/ingest_kdot_kanplan_kandrive.py` | KDOT / KanPlan / KanDrive RAW capture | 🔴 | Atlas v1.1 §13.D; Pass-32 KFM-P12-PROG-0005 | Kansas authority |
| `pipelines/domains/roads-rail-trade/ingest_fra_gcis.py` | FRA GCIS grade crossings RAW capture | 🔴 | Pass-10 C10-05 | |
| `pipelines/domains/roads-rail-trade/ingest_fra_form57.py` | FRA Form 57 RAW capture | 🔴 | Pass-10 C10-05 | |
| `pipelines/domains/roads-rail-trade/ingest_stb_class1.py` | STB Class I weekly snapshots | 🔴 | Pass-10 C10-05 | |
| `pipelines/domains/roads-rail-trade/ingest_hifld_ntad.py` | HIFLD / NTAD rail geospatial RAW capture | 🔴 | Pass-10 C10-05 | |
| `pipelines/domains/roads-rail-trade/normalize_to_road_segment.py` | RAW → PROCESSED for Road Segment | 🔴 | Atlas v1.1 §13.H | |
| `pipelines/domains/roads-rail-trade/normalize_to_rail_segment.py` | RAW → PROCESSED for Rail Segment | 🔴 | Atlas v1.1 §13.H | |
| `pipelines/domains/roads-rail-trade/build_corridor_route.py` | Composite CorridorRoute assembly | 🔴 | Atlas v1.1 §13.E | |
| `pipelines/domains/roads-rail-trade/build_historic_route_claim.py` | Historic Route Claim normalization (with generalization) | 🔴 | Atlas v1.1 §13.E, §13.I | |
| `pipelines/domains/roads-rail-trade/project_to_graph.py` | Derived graph projection (non-canonical) | 🔴 | Encyclopedia §5.2 | |
| `pipelines/domains/roads-rail-trade/emit_catalog_records.py` | STAC/DCAT/PROV records + EvidenceBundle | 🔴 | Atlas v1.1 §13.H, §13.J; Pass-32 KFM-P20-PROG-0014 (frontier STAC) | |
| `pipelines/domains/roads-rail-trade/emit_pmtiles_layers.py` | PMTiles per layer for published surface | 🔴 | Atlas v1.1 §13.G; Pass-32 KFM-P8-PROG-0025 / KFM-P10-PROG-0015 | |
| `pipeline_specs/roads-rail-trade/README.md` | Per-root index of pipeline specs | 🔴 | Directory Rules §15 | |
| `pipeline_specs/roads-rail-trade/tiger_roads.yaml` | Declarative spec for TIGER ingest | 🔴 | Atlas v1.1 §13.D | |
| `pipeline_specs/roads-rail-trade/wzdx_v4.yaml` | Declarative spec for WZDx ingest + validator | 🔴 | Pass-32 KFM-P8-PROG-0025 | |
| `pipeline_specs/roads-rail-trade/fra_gcis.yaml` | Declarative spec for GCIS ingest | 🔴 | Pass-10 C10-05 | |
| `pipeline_specs/roads-rail-trade/historic_routes.yaml` | Declarative spec for historic-route claim assembly | 🔴 | Pass-32 KFM-P20-PROG-0013 | |
### 7.9 `data/<phase>/roads-rail-trade/` (lifecycle lanes)
Lifecycle data. Per Directory Rules §9.1. **Promotion is a governed state transition, not a file move.**
| Path | Purpose | Status | Citation basis | Notes |
|---|---|:---:|---|---|
| `data/raw/roads-rail-trade/<source_id>/<run_id>/` | Source-edge captures with retrieval metadata and checksums | 🔴 | Directory Rules §9.1 | Per-source subdirectory |
| `data/work/roads-rail-trade/<run_id>/` | Normalized intermediates, candidate assertions | 🔴 | Directory Rules §9.1 | |
| `data/quarantine/roads-rail-trade/<reason>/<run_id>/` | Failed validation / rights / sensitivity / overprecise geometry | 🔴 | Directory Rules §9.1 | |
| `data/processed/roads-rail-trade/<dataset_id>/<version>/` | Validated canonical records | 🔴 | Directory Rules §9.1 | |
| `data/catalog/domain/roads-rail-trade/` | Domain catalog records (STAC/DCAT/PROV) | 🔴 | Directory Rules §9.1; Atlas v1.1 §13.H | Note: `catalog/domain/` singular per §9.1 |
| `data/published/layers/roads-rail-trade/` | Released public-safe artifacts (PMTiles, GeoParquet, FeatureCollections) | 🔴 | Directory Rules §9.1; Atlas v1.1 §13.G, §13.H | |
| `data/registry/sources/roads-rail-trade/` | Per-source SourceDescriptor records | 🔴 | Directory Rules §9.1; Atlas v1.1 §13.D | |
| `data/triplets/graph_deltas/roads-rail-trade/` | Derived graph projection deltas (non-canonical) | 🔴 | Encyclopedia §5.2; `GRAPH_PROJECTIONS.md` | `data/triplets/` plural is canonical |
| `data/rollback/roads-rail-trade/<release_id>/` | Alias-revert receipts (data plane) | 🔴 | Directory Rules §9.1 (OPEN: vs `release/rollback_cards/`) | See Directory Rules §18.a OPEN (ROADS-DR-02) |
| `data/receipts/ingest/<run_id>/` (cross-cutting) | Process memory — ingest run receipts | 🔴 | Directory Rules §9.1 | Not domain-scoped |
| `data/proofs/evidence_bundle/<bundle_id>/` (cross-cutting) | EvidenceBundle objects backing domain claims | 🔴 | Directory Rules §9.1 | Not domain-scoped |
> [!CAUTION]
> **CONFIRMED live-repo drift (commit `b6a279…`).** A root-adjacent `data/trade-routes/` folder exists in the live repo and is a drift: its contents belong under `data/{raw,processed,catalog,published}/roads-rail-trade/`. Track in `docs/registers/DRIFT_REGISTER.md` and migrate. (This is the one repo-state fact in this register that is CONFIRMED rather than NEEDS VERIFICATION.)
### 7.10 `release/candidates/roads-rail-trade/`
Release decisions. Per Directory Rules §9.2. (Final accepted manifests/notices/cards live under `release/manifests/`, `release/correction_notices/`, `release/rollback_cards/` — cross-domain, outside the domain segment.)
| Path | Purpose | Status | Citation basis | Notes |
|---|---|:---:|---|---|
| `release/candidates/roads-rail-trade/README.md` | Per-root index of pending release candidates for this domain | 🔴 | Directory Rules §15 | |
| `release/candidates/roads-rail-trade/<release_id>/manifest.json` | ReleaseManifest for a candidate release | 🔴 | Atlas v1.1 §13.M; Directory Rules §9.2 | |
| `release/candidates/roads-rail-trade/<release_id>/proof_pack/` | ProofPack bundle for the release | 🔴 | Atlas v1.1 §13.M | |
| `release/rollback_cards/roads-rail-trade/<release_id>.md` | Rollback decision record | 🔴 | Atlas v1.1 §13.M; Directory Rules §18.a OPEN | Placement vs `data/rollback/` is OPEN (ROADS-DR-02) |
| `release/correction_notices/roads-rail-trade/<notice_id>.md` | Correction notice records | 🔴 | Atlas v1.1 §13.M | |
### 7.11 Connectors, registries, control plane
Cross-cutting roots that touch this domain.
| Path | Purpose | Status | Citation basis | Notes |
|---|---|:---:|---|---|
| `connectors/wzdx/` | WZDx feed connector (not domain-scoped) | 🔴 | Pass-32 KFM-P8-PROG-0025; Directory Rules §12 | Per-source connector |
| `connectors/fhwa_hpms/` | FHWA HPMS connector | 🔴 | Atlas v1.1 §13.D | |
| `connectors/fhwa_nhfn/` | FHWA NHFN connector | 🔴 | Atlas v1.1 §13.D | |
| `connectors/kdot/` | KDOT / KanPlan / KanDrive connector | 🔴 | Atlas v1.1 §13.D; Pass-32 KFM-P12-PROG-0005 | |
| `connectors/fra_gcis/` | FRA GCIS connector | 🔴 | Pass-10 C10-05 | |
| `connectors/fra_form57/` | FRA Form 57 connector | 🔴 | Pass-10 C10-05 | |
| `connectors/stb_class1/` | STB Class I weekly reports connector | 🔴 | Pass-10 C10-05 | |
| `connectors/hifld/`, `connectors/ntad/` | HIFLD / NTAD connectors | 🔴 | Pass-10 C10-05 | |
| `connectors/tiger_line/` | Census TIGER/Line connector | 🔴 | Atlas v1.1 §13.D | Multi-domain |
| `connectors/osm/` | OSM connector (legal-status DENY enforced at policy) | 🔴 | Atlas v1.1 §13.D, §13.K | Multi-domain |
| `connectors/gnis/` | GNIS names connector | 🔴 | Atlas v1.1 §13.D | Multi-domain |
| `control_plane/source_authority_register.yaml` (entries for transport sources) | Per-source authority register entries | 🔴 | Directory Rules §6.2 | Not domain-scoped file; entries added |
| `control_plane/domain_lane_register.yaml` (entry for roads-rail-trade) | Domain lane register entry | 🔴 | Directory Rules §6.2 | |
[↑ back to top](#-roads-rail-and-trade-routes--missing-or-planned-files)
---
## 8. Cross-domain references
CONFIRMED doctrine (Atlas v1.1 §13.F, §24.4.11): the roads-rail-trade lane has explicit cross-lane relations whose evidence boundaries MUST be preserved.
| This domain | Related lane | Relation | Constraint |
|---|---|---|---|
| Roads/Rail/Trade | Settlements/Infrastructure | depots, crossings, facilities, dependencies | Settlements owns facility identity. EvidenceBundle support required. |
| Roads/Rail/Trade | Hydrology | bridge / ferry / ford / river crossing | Hydrology owns water evidence. |
| Roads/Rail/Trade | Hazards | closure, detour, flood/fire/smoke exposure | Hazards owns hazard events. Roads/Rail/Trade cites; never asserts hazard authority. |
| Roads/Rail/Trade | Archaeology / Cultural Heritage | historic routes, Indigenous corridors, forts, missions | Archaeology owns site truth and sovereignty review path. Exact archaeological coordinates DENIED. |
| Roads/Rail/Trade | People / Genealogy / Land | historic-route biographical anchoring | People/Land owns living-person and parcel privacy. |
| Roads/Rail/Trade | Frontier Matrix | access cells in the time-aware matrix | Roads/Rail/Trade emits access observations; matrix consumes (§24.4.11). |
| Roads/Rail/Trade | Atmosphere / Air | smoke / visibility context for status events | Atmosphere owns observations. |
> [!CAUTION]
> **Indigenous corridors and historic-route coordinates** are dual-sensitivity claims. Atlas v1.1 §13.I and §15 (Archaeology) both apply. Default to **steward review + generalized geometry + DENY on overprecision**. Treat any cross-lane import from archaeology as `T4 default-deny` in policy until reconciled per archaeology sovereignty workflow. See `HISTORIC_ROUTES.md`.
[↑ back to top](#-roads-rail-and-trade-routes--missing-or-planned-files)
---
## 9. Open questions and verification backlog
Items carried forward from Atlas v1.1 §13.N plus this register's new findings.
### 9.1 Carried from Atlas v1.1 §13.N
| ID | Item | Evidence that would settle it | Status |
|---|---|---|---|
| ROADS-V-01 | Verify KDOT / FHWA / FRA / WZDx source terms | Mounted repo files, source registry entries, rights tier per source | NEEDS VERIFICATION |
| ROADS-V-02 | Verify Indigenous / cultural corridor policy | Mounted policy bundles, archaeology coordination record, steward-review workflow | NEEDS VERIFICATION |
| ROADS-V-03 | Implement RouteUncertaintyProfile (reconcile with doctrinal `UncertaintySurface`) | Schema home, tests, fixtures, validator entry | NEEDS VERIFICATION |
| ROADS-V-04 | Verify transport graph and MapLibre integration | Layer manifest, governed API DTO, MapLibre layer wiring, Evidence Drawer payload | NEEDS VERIFICATION |
### 9.2 New in this register
| ID | Item | Evidence that would settle it | Status |
|---|---|---|---|
| ROADS-DR-01 | **Resolve `roads-rail-trade` vs `transport` naming variance** between Directory Rules §12 and Atlas v1.1 §24.13 | ADR reconciling slug vs segment; entry in `docs/registers/DRIFT_REGISTER.md` | OPEN — §12 names `roads-rail-trade` verbatim (Option A bias); aligned to FILE_SYSTEM_PLAN OPEN-RRT-FSP-01 |
| ROADS-DR-02 | Confirm `release/rollback_cards/roads-rail-trade/` vs `data/rollback/roads-rail-trade/` boundary | ADR — already noted as OPEN in Directory Rules §18.a | OPEN |
| ROADS-V-05 | Resolve GCIS vs HIFLD crossing-coordinate disagreement policy | Pass-10 C10-05 names the issue; ADR or per-source disambiguation rule | OPEN (Pass-10 named) |
| ROADS-V-06 | STB Class I weekly snapshot overlap — snapshot-week dedup contract | Pipeline spec + receipt design; pilot on BNSF Transcon per Pass-10 C10-05 | OPEN (Pass-10 named) |
| ROADS-V-07 | OSM ODbL terms current rights posture (re-publication, share-alike trigger) | Up-to-date OSMF licensing review + source registry rights tier | NEEDS VERIFICATION |
| ROADS-V-08 | Whether `connectors/wzdx/` should be domain-segmented or remain source-segmented | Directory Rules §12 (multi-domain/cross-cutting) prefers source-segmented; confirm | INFERRED — source-segmented |
| ROADS-V-09 | Whether historic-route claim handling needs its own ADR (highest-risk surface) | Sovereignty review interaction; archaeology coordination minutes; see `HISTORIC_ROUTES.md` | OPEN |
| ROADS-V-10 | Whether `docs/domains/roads-rail-trade/VERIFICATION_BACKLOG.md` is a separate file or folded into central `docs/registers/VERIFICATION_BACKLOG.md` | Docs steward decision per Directory Rules §6.1 | OPEN — recommended fold-in |
| ROADS-V-11 | Final list of source families (canonical set) — Atlas §13.D lists 8; Pass-10 expands to 13+ | Source-family register entry; ADR if new family added | OPEN |
| ROADS-V-12 | Whether `PIPELINE.md`/`SENSITIVITY.md`/`API_SURFACES.md` should be authored separately or folded into the existing companion docs (`DATA_LIFECYCLE.md` / `HISTORIC_ROUTES.md` / `MAP_UI_CONTRACTS.md`) | Docs steward decision; avoid duplicate-scope drift | OPEN — recommended fold-in to avoid overlap |
All NEEDS VERIFICATION items SHOULD be mirrored into `docs/registers/VERIFICATION_BACKLOG.md` per Directory Rules §18; OPEN items SHOULD have a corresponding `docs/registers/DRIFT_REGISTER.md` entry until ADR resolution per Directory Rules §2.5.
[↑ back to top](#-roads-rail-and-trade-routes--missing-or-planned-files)
---
## 10. Promotion and intake workflow
Before any file in this register is created, the Directory Rules §4 **Placement Protocol** must be applied:
```text
Step 1 — Identify the responsibility (exactly one)
Step 2 — Identify the lifecycle phase (data/ only)
Step 3 — Identify the domain segment (NEVER a root folder)
Step 4 — Confirm authority (per-root README exists per §15; ADR if §2.4 applies)
```
When marking a row in this register as ✅ **present** after authoring, include in the PR description:
<details>
<summary><b>Checklist (copy into PR description when authoring a file from this register)</b></summary>

```text
[ ] File path matches Directory Rules §12 lane pattern
[ ] Owning responsibility root has a current per-root README (§15)
[ ] If naming variance applies (§6), the chosen form is documented and a DRIFT entry exists until ADR
[ ] Truth labels (CONFIRMED / PROPOSED / NEEDS VERIFICATION) applied where confidence materially matters
[ ] EvidenceBundle / EvidenceRef closure obligations preserved
[ ] If sensitive (Indigenous corridor / historic-route / critical facility), sensitivity workflow followed (see HISTORIC_ROUTES.md)
[ ] If destructive (schema break, policy reverse, lifecycle skip), ADR exists per Directory Rules §2.4
[ ] This register's row updated from 🟡/🔴 → ✅ in the same PR
[ ] Changelog entry added in §12
[ ] GENERATED_RECEIPT.json wired per the operating contract
```

</details>

> [!TIP]
> Bias toward **smallest useful, reversible change**. A single new schema with its README, contract, fixtures, and a single denial test is a complete reversible slice. A whole-lane drop is not.
[↑ back to top](#-roads-rail-and-trade-routes--missing-or-planned-files)
---
## 11. Related docs
> Repository not mounted; all link targets are PROPOSED.
- 🟡 [`docs/domains/roads-rail-trade/README.md`](./README.md) — domain entry point (planned)
- 🟡 [`docs/domains/roads-rail-trade/FILE_SYSTEM_PLAN.md`](./FILE_SYSTEM_PLAN.md) — placement standard (companion; placement authority)
- 🟡 [`docs/domains/roads-rail-trade/DATA_LIFECYCLE.md`](./DATA_LIFECYCLE.md) — lifecycle standard (companion)
- 🟡 [`docs/domains/roads-rail-trade/EXPANSION_BACKLOG.md`](./EXPANSION_BACKLOG.md) — expansion backlog (companion)
- 🟡 [`docs/domains/roads-rail-trade/GRAPH_PROJECTIONS.md`](./GRAPH_PROJECTIONS.md) — derived graph (companion)
- 🟡 [`docs/domains/roads-rail-trade/HISTORIC_ROUTES.md`](./HISTORIC_ROUTES.md) — historic-route sensitivity (companion)
- 🟡 [`docs/domains/roads-rail-trade/IDENTITY_MODEL.md`](./IDENTITY_MODEL.md) — identity & spec_hash (companion)
- 🟡 [`docs/domains/roads-rail-trade/MAP_UI_CONTRACTS.md`](./MAP_UI_CONTRACTS.md) — map-UI contracts (companion)
- 🟡 [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — Domain Placement Law §12; per-root README §15; schema home §6.4; ADR triggers §2.4
- 🟡 [`docs/registers/VERIFICATION_BACKLOG.md`](../../registers/VERIFICATION_BACKLOG.md) — central verification register
- 🟡 [`docs/registers/DRIFT_REGISTER.md`](../../registers/DRIFT_REGISTER.md) — naming-variance + `data/trade-routes/` drift entries
- 🟡 [`docs/standards/PROV.md`](../../standards/PROV.md) — provenance standard profile (naming variance: `PROVENANCE.md` — Directory Rules §18.b OPEN-DR-01)
- 🟡 [`docs/adr/README.md`](../../adr/README.md) — ADR index (ROADS-DR-01 belongs here)
- 🟡 [`docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf`](../../atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf) — Atlas v1.1, Ch. 13 + §24.13
- 🟡 [`docs/runbooks/roads-rail-trade/`](../../runbooks/roads-rail-trade/) — runbook subfolder (none authored; convention pending Directory Rules §18.b OPEN-DR-02)
- 🟡 `ai-build-operating-contract.md` — operating contract; `CONTRACT_VERSION = "3.0.0"`
[↑ back to top](#-roads-rail-and-trade-routes--missing-or-planned-files)
---
## 12. Change log
| Date | Change | By |
|---|---|---|
| 2026-05-19 | Initial draft. Authored from doctrine — Atlas v1.1 Ch. 13, Directory Rules §12, Pass-10 C10-05 / C10-04, Pass-32 KFM-P8-PROG-0025 / KFM-P20-PROG-0013, Encyclopedia. Repo not mounted; all repo-state claims PROPOSED or NEEDS VERIFICATION. Naming variance flagged in §6 and ROADS-DR-01. | TBD |
| 2026-06-07 | v0.2 optimization. Corrected per-root README citations §9 → **§15** (the README-contract section; §9 is lifecycle); corrected schema-in-contracts basis to **§13.1**; corrected release-plane basis to **§9.2**. Verified Pass-32 cards KFM-P8-PROG-0025 (WZDx, normalized statement CONFIRMED) and KFM-P20-PROG-0013 (frontier routes — exact list: Santa Fe / Pony Express / Butterfield-Smoky Hill / forts / stations / depots); corrected the Chisholm-Trail fixture over-attribution; added companion card KFM-P20-PROG-0014 (STAC) and KFM-P12-PROG-0005 / KFM-P10-PROG-0015 (WZDx/KanDrive lanes). Aligned ROADS-DR-01 to FILE_SYSTEM_PLAN OPEN-RRT-FSP-01 (§12 verbatim). Added the seven companion docs to §7.1 and §11; added CONFIRMED `data/trade-routes/` live-repo drift to §7.9; added the source-role mapping note and `data/triplets/graph_deltas/` row. Pinned `CONTRACT_VERSION = "3.0.0"`; refreshed dates; added the FILE_SYSTEM_PLAN division-of-labor note (§1); added ROADS-V-12. | Roads/Rail steward (PLACEHOLDER) |
---
<sub>**Status:** draft · **Last updated:** 2026-06-07 · **Pins** `CONTRACT_VERSION = "3.0.0"` · **Doctrine basis:** Directory Rules §12 / §13.1 / §15; Atlas v1.1 Ch. 13 + §24.1 + §24.13; Pass-10 C10-05; Pass-32 KFM-P8-PROG-0025 / KFM-P20-PROG-0013; `[DOM-ROADS]` `[ENCY]`</sub>
[↑ back to top](#-roads-rail-and-trade-routes--missing-or-planned-files)
