<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TBD-roads-rail-trade-sublane-rail
title: Roads/Rail/Trade Routes — Rail Sublane Dossier
type: standard
version: v0.2
status: draft
owners: Roads/Rail/Trade Routes domain stewards (TBD — placeholder)
created: 2026-05-19
updated: 2026-06-07
policy_label: public (sublane scaffold) — content tiers vary; operationally sensitive rail detail defaults to deny
related:
  - docs/domains/roads-rail-trade/README.md            # PROPOSED parent dossier
  - docs/domains/roads-rail-trade/sublanes/README.md   # PROPOSED sublane index
  - docs/domains/roads-rail-trade/sublanes/roads.md    # PROPOSED sibling sublane
  - docs/domains/roads-rail-trade/sublanes/trade.md    # PROPOSED sibling sublane
  - docs/domains/settlements-infrastructure/README.md  # canonical owner of depot/facility identity
  - docs/domains/hydrology/README.md                   # bridge/ferry/ford/river-crossing context
  - docs/domains/archaeology/README.md                 # historic & Indigenous corridor sensitivity
  - docs/doctrine/directory-rules.md                   # placement authority
notes:
  - 'CONTRACT_VERSION = "3.0.0" pinned per ai-build-operating-contract.md'
  - "The 'sublanes/' organizational layer is a PROPOSED extension of docs/domains/<domain>/; not yet in Directory Rules (OPEN-DR-SUBLANE-01)."
  - "TERMINOLOGY: 'sublane' is not established KFM doctrine. 'lane' is defined; 'sub-lane' exists only in the Focus Mode cross-root sense (Directory Rules §6.7). See OPEN-DR-SUBLANE-01."
  - "Roads/Rail schema/contract home per Atlas §24.13 is schemas/contracts/v1/transport/ + contracts/transport/ (slug drift vs roads-rail-trade). See OPEN-RAIL-05."
  - "Canonical renderer adapter is packages/maplibre-runtime/ (v1.3, supersedes v1.2 packages/maplibre/; Cesium retired)."
  - "All path, route, schema, and tooling claims remain PROPOSED until a mounted repository is inspected."
[/KFM_META_BLOCK_V2] -->

# Roads / Rail / Trade Routes — **Rail Sublane Dossier**

> _Governance scaffold for Kansas rail evidence — modern, historic, freight, crossings, facilities, restrictions, and graph projections — within the Roads/Rail/Trade Routes domain lane._

![Status](https://img.shields.io/badge/status-draft-yellow) ![Doc Type](https://img.shields.io/badge/type-sublane%20dossier-blue) ![Domain](https://img.shields.io/badge/domain-roads--rail--trade-informational) ![Contract](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-informational) ![Lifecycle](https://img.shields.io/badge/lifecycle-RAW%20%E2%86%92%20PUBLISHED-lightgrey) ![Policy](https://img.shields.io/badge/sensitivity-deny--default%20on%20operational%20rail-orange) ![Term](https://img.shields.io/badge/%22sublane%22-NOT%20DOCTRINE-red) ![Labels](https://img.shields.io/badge/labels-CONFIRMED%20%7C%20PROPOSED%20%7C%20NEEDS%20VERIFICATION-blueviolet)

<sub><strong>Status:</strong> draft · <strong>Owners:</strong> Roads/Rail/Trade Routes stewards (TBD placeholder) · <strong>Last updated:</strong> 2026-06-07 · <strong>Supersedes:</strong> v0.1 (first edition)</sub>

> [!IMPORTANT]
> **Scaffolding posture.** This file inherits all canonical authority from the parent `[DOM-ROADS]` dossier and from Directory Rules. The `docs/domains/<domain>/sublanes/` organizational layer is **PROPOSED** — it is not yet enumerated in `docs/doctrine/directory-rules.md`. Until an ADR settles the convention (see [§ O](#o-verification-backlog-and-open-questions), **OPEN-DR-SUBLANE-01**), treat this dossier as a doctrine **scaffold**. The sublane does **not** own root authority, schema homes, contract homes, policy homes, release surfaces, or governed-API routes.

> [!WARNING]
> **Terminology flag — "sublane" is not KFM doctrine.** The corpus defines **lane** (a domain/topic *segment inside a responsibility root*) and uses **sub-lane** only for **Focus Modes** (a geographic *area* appearing as a per-root segment across responsibility roots, Directory Rules §6.7). This document's "sublane" — a per-mode partition *within one domain* — is a **coined reading aid** that collides with the Focus Mode sense. Tracked as **OPEN-DR-SUBLANE-01**; every grouping here is PROPOSED and carries no placement authority. `[DIRRULES]`

---

## Quick jump

- [A. Sublane identity & one-line purpose](#a-sublane-identity-and-one-line-purpose)
- [B. Scope, boundary, and explicit non-ownership](#b-scope-boundary-and-explicit-non-ownership)
- [C. Repo fit — parent dossier and responsibility roots](#c-repo-fit--parent-dossier-and-responsibility-roots)
- [D. Ubiquitous language (rail-applicable terms)](#d-ubiquitous-language-rail-applicable-terms)
- [E. Key source families for rail](#e-key-source-families-for-rail)
- [F. Main object families realized in rail](#f-main-object-families-realized-in-rail)
- [G. Cross-lane relations](#g-cross-lane-relations)
- [H. Map and viewing products](#h-map-and-viewing-products)
- [I. Pipeline shape (RAW → PUBLISHED)](#i-pipeline-shape-raw--published)
- [J. Sensitivity, rights, and publication posture](#j-sensitivity-rights-and-publication-posture)
- [K. API, contract, and schema surfaces](#k-api-contract-and-schema-surfaces)
- [L. Validators, tests, fixtures](#l-validators-tests-fixtures)
- [M. Governed AI behavior for the rail sublane](#m-governed-ai-behavior-for-the-rail-sublane)
- [N. Publication, correction, and rollback](#n-publication-correction-and-rollback)
- [O. Verification backlog and open questions](#o-verification-backlog-and-open-questions)
- [Related docs](#related-docs)
- [Appendix — Atlas citation map](#appendix--atlas-citation-map)

---

## A. Sublane identity and one-line purpose

**CONFIRMED doctrine / PROPOSED implementation:** the **Rail sublane** is the rail-mode partition of the Roads/Rail/Trade Routes domain lane (`[DOM-ROADS]`). It governs Kansas rail segments, historic rail alignments, depots, sidings, yards, crossings, rail bridges, operator status, restrictions, and rail-graph projections; it introduces **no** new lifecycle phases, schema homes, policy homes, or release surfaces. All canonical authority continues to flow through the parent `[DOM-ROADS]` dossier and through Directory Rules. `[DOM-ROADS]` `[ENCY]` `[DIRRULES]`

> [!NOTE]
> **Why a separate sublane file?** The parent domain spans **three mode-families** — roads, rail, and trade routes/corridors — each with distinct source ecosystems, sensitivity surfaces, and viewing products. A per-mode file makes scope, sources, and validators easier to reason about without re-opening canonical responsibility boundaries. **PROPOSED:** sibling sublane files at `roads.md` and `trade.md` mirror this one, indexed from `sublanes/README.md`.

[↑ back to top](#roads--rail--trade-routes--rail-sublane-dossier)

---

## B. Scope, boundary, and explicit non-ownership

### B.1 In-scope object families (rail-specific realizations)

**CONFIRMED in `[DOM-ROADS]` scope statement / PROPOSED rail-specific realization:** from the parent domain's owned set, the rail sublane covers these object families when applied to rail evidence:

- **Rail Segment** — track centerlines, alignments, branchlines, mainlines (historic and current).
- **Historic Route / Historic RouteClaim** — historic rail alignments, abandoned lines, predecessor-railroad corridors.
- **Depot, Siding, Yard** — rail-network facility types **whose identity remains settlement/infrastructure-owned** (see [§ G](#g-cross-lane-relations)).
- **Crossing** — at-grade and grade-separated rail-roadway interactions; **highway-rail grade crossings** are the FRA GCIS anchor.
- **Bridge** — rail bridges over water or other infrastructure.
- **CorridorRoute** and **RouteMembership** — multi-segment named rail corridors and segment-to-corridor assignments.
- **Operator Status / OperatorAssignment** — rail-operator (Class I, regional, short-line) ownership and operational control over time.
- **Access Restriction / RestrictionEvent** — embargoes, slow orders, closures, weight/clearance restrictions on rail.
- **Route Event / Status Event** — rail incidents, outages, service interruptions (sources permitting).
- **Network Edge / Network Node** — rail-graph projections derived from validated evidence.
- **Movement Story Node** — narrative/interpretive nodes tied to rail movement evidence.

`[DOM-ROADS]` `[ENCY]`

> [!NOTE]
> **Term provenance.** `Rail Segment`, `Historic Route`, `Depot`, `Siding`, `Yard`, `Crossing`, `Bridge`, `Freight Corridor`, `Route Event`, `Operator Status`, `Access Restriction`, `Network Edge`, `Movement Story Node`, `Historic RouteClaim`, `CorridorRoute`, `RouteMembership`, `TransportFacility`, and `RestrictionEvent` are **CONFIRMED** terms from `[DOM-ROADS]` §B/§C/§E. `OperatorAssignment` and `StatusEvent` are **PROPOSED** rail-specific term realizations, not yet in the dossier's owned-object list.

### B.2 Explicit non-ownership

**CONFIRMED / PROPOSED:** the rail sublane explicitly does **not** own:

| Concern | Owning lane | Why this matters |
|---|---|---|
| Depot / station / facility canonical identity | Settlements / Infrastructure (`[DOM-SETTLE]`) | A depot **as a place / settlement-infrastructure object** is settlement-owned; the rail sublane consumes that identity and contributes the rail-network role. |
| Water-feature evidence at river crossings | Hydrology (`[DOM-HYD]`) | A rail bridge crosses a hydrologic feature; the feature itself is owned by hydrology. |
| Historic Indigenous corridor truth and sensitivity | Archaeology / Cultural Heritage (`[DOM-ARCH]`) | Where rail alignments overlap or recapitulate Indigenous trade and mobility corridors, the cultural-heritage sensitivity policy of `[DOM-ARCH]` is authoritative. |
| Hazard event truth | Hazards (`[DOM-HAZ]`) | Closures / detours caused by floods, fires, or other hazards are cited from `[DOM-HAZ]`, not authored here. |
| Person / parcel / operator legal-entity facts | People / Land (`[DOM-PEOPLE]`) | Rail-operator identity as a legal entity is people/land-owned; the rail sublane carries the operational-control relation. |

`[DOM-ROADS]` `[DOM-SETTLE]` `[DOM-HYD]` `[DOM-ARCH]` `[DOM-HAZ]` `[DOM-PEOPLE]` `[ENCY]`

[↑ back to top](#roads--rail--trade-routes--rail-sublane-dossier)

---

## C. Repo fit — parent dossier and responsibility roots

### C.1 PROPOSED tree (this sublane in its dossier context)

> [!CAUTION]
> The tree below is **PROPOSED** and **NEEDS VERIFICATION** against a mounted repository. The `roads-rail-trade/` subfolder under `docs/domains/` is **CONFIRMED** in the `docs/doctrine/directory-rules.md` §6.1 domain listing; the `sublanes/` layer is **not yet enumerated** there. Treat the structure as a working scaffold pending **OPEN-DR-SUBLANE-01** (§ O).

```text
docs/
└── domains/
    └── roads-rail-trade/                     # CONFIRMED in directory-rules.md §6.1 listing
        ├── README.md                         # PROPOSED parent dossier README (NEEDS VERIFICATION)
        ├── ARCHITECTURE.md                   # PROPOSED — parallel to other dossiers
        ├── PRESERVATION_MATRIX.md            # PROPOSED — parallel to other dossiers
        ├── VERIFICATION_BACKLOG.md           # PROPOSED (and see canonical docs/registers/VERIFICATION_BACKLOG.md)
        └── sublanes/                         # PROPOSED organizational layer — see OPEN-DR-SUBLANE-01
            ├── README.md                     # PROPOSED — sublane index
            ├── roads.md                      # PROPOSED sibling
            ├── rail.md                       # THIS FILE
            └── trade.md                      # PROPOSED sibling
```

### C.2 Canonical responsibility roots this dossier defers to

The rail sublane is a **doctrine surface**, not an authority root. Per `docs/doctrine/directory-rules.md` (CONFIRMED rules; specific repo presence PROPOSED), all of the following remain anchored elsewhere:

| Concern | Canonical root (per Directory Rules / Atlas §24.13) | Status |
|---|---|---|
| Object meaning | `contracts/transport/` — Atlas §24.13 maps `[DOM-ROADS]` to the `transport` slug | PROPOSED — see **OPEN-RAIL-05** (slug drift) |
| Machine-checkable shape | `schemas/contracts/v1/transport/` — Atlas §24.13; ADR-0001 schema home | PROPOSED — see **OPEN-RAIL-05** |
| Admissibility / sensitivity | `policy/domains/roads-rail-trade/...` or `policy/sensitivity/...` (lane pattern) | PROPOSED — NEEDS VERIFICATION |
| Source registry | `data/registry/sources/...` + `control_plane/source_authority_register.yaml` (CONFIRMED roots; entries PROPOSED) | PROPOSED — NEEDS VERIFICATION |
| Pipelines | `pipelines/` / `pipeline_specs/` | PROPOSED — NEEDS VERIFICATION |
| Release decisions | `release/` | PROPOSED — NEEDS VERIFICATION |
| Public surface | `apps/governed-api/` | PROPOSED — NEEDS VERIFICATION |
| Browser renderer adapter | `packages/maplibre-runtime/` — v1.3 sole governed renderer (supersedes v1.2 `packages/maplibre/`; Cesium retired) | CONFIRMED canonical name; repo presence NEEDS VERIFICATION |

`[DIRRULES]` `[ENCY]`

> [!CAUTION]
> **Slug drift (OPEN-RAIL-05).** Atlas §24.13 assigns this domain the `transport` slug for schema/contract homes (`schemas/contracts/v1/transport/`, `contracts/transport/`) while the docs lane is `roads-rail-trade`. The earlier v0.1 of this dossier used `…/domains/roads-rail-trade/…` for those homes; that is **CONFLICTED** with §24.13. Resolution is an ADR; do not treat either form as canonical until settled. `[DIRRULES]` `[ENCY]`

> [!NOTE]
> **No parallel homes.** Per Directory Rules §2.4 / §5, the rail sublane MUST NOT introduce a parallel schema, contract, policy, source, registry, release, or proof home. Any new home requires an ADR.

[↑ back to top](#roads--rail--trade-routes--rail-sublane-dossier)

---

## D. Ubiquitous language (rail-applicable terms)

**CONFIRMED terms / PROPOSED field realization** — terms inherited from `[DOM-ROADS]` §C and applied within rail evidence; meaning is constrained by source role, evidence, time, and release state. `[DOM-ROADS]` `[ENCY]`

| Term | Rail-specific meaning | Term status | Citation |
|---|---|---|---|
| **Rail Segment** | A linear unit of rail track with a single role/operator/time scope. | CONFIRMED | `[DOM-ROADS]` |
| **CorridorRoute** | A named multi-segment rail corridor (e.g., a mainline across operators or eras). | CONFIRMED | `[DOM-ROADS]` |
| **RouteMembership** | Time-bounded membership of a Rail Segment in a CorridorRoute. | CONFIRMED | `[DOM-ROADS]` |
| **Network Node** | Junction, switch, interchange, or crossing terminus in the rail graph projection. | CONFIRMED | `[DOM-ROADS]` |
| **Crossing** | Highway-rail or rail-rail crossing; the GCIS-anchored object for at-grade crossings. | CONFIRMED | `[DOM-ROADS]` |
| **TransportFacility** | A rail-network facility (depot, station, signal facility, intermodal yard) — **identity owned by Settlements/Infrastructure**, rail-network role owned here. | CONFIRMED | `[DOM-ROADS]` `[DOM-SETTLE]` |
| **RestrictionEvent** | A time-bounded restriction (embargo, slow order, weight/clearance limit, closure) on a Rail Segment or facility. | CONFIRMED | `[DOM-ROADS]` |
| **OperatorAssignment** | Time-bounded assignment of an operator (Class I, regional, short-line) to a Rail Segment or CorridorRoute. | PROPOSED (rail realization of Operator Status) | `[DOM-ROADS]` |
| **StatusEvent** | An observed rail-status event (incident, outage, service interruption) admissible only with source-role discipline. | PROPOSED (rail realization of Route Event) | `[DOM-ROADS]` |
| **Historic RouteClaim** | A claim about historic rail alignment, recorded with evidence and uncertainty rather than as fact. | CONFIRMED | `[DOM-ROADS]` |
| **TradeRouteCorridor** | Pre-rail or rail-era trade/mobility corridor that may parallel, anticipate, or interact with rail alignments. | CONFIRMED | `[DOM-ROADS]` |

> [!TIP]
> **Naming hygiene.** Preserve KFM compound terms (e.g., `Rail Segment`, `RestrictionEvent`, `Historic RouteClaim`) exactly. Do not collapse them into generic industry vocabulary ("rail link," "incident," "abandoned line") in normative content.

[↑ back to top](#roads--rail--trade-routes--rail-sublane-dossier)

---

## E. Key source families for rail

**CONFIRMED source families / PROPOSED activation / NEEDS VERIFICATION rights, terms, cadence, and current behavior.** Rights and current terms for every entry MUST be reviewed in the source registry before activation. `[DOM-ROADS]` `[ENCY]` `[DIRRULES]`

| Source family | Role candidates (per source-role doctrine) | Rail-specific role | Evidence |
|---|---|---|---|
| **FRA GCIS** (Grade Crossing Inventory System) | authority / observation / context | Canonical inventory of public and private highway-rail grade crossings; per-crossing safety attributes. | C10-05 (CONFIRMED); activation PROPOSED |
| **FRA Form 57** (incident reports) | authority / observation | Standardized rail incident report; **observation role**, not life-safety authority within KFM. | C10-05 (CONFIRMED); activation PROPOSED |
| **STB Class I weekly reports** | authority (operational metrics) | Operational metrics from the seven Class I carriers; weekly snapshot cadence with overlap-deduplication concern. | C10-05 (CONFIRMED); activation PROPOSED |
| **HIFLD / NTAD rail layers** | authority / context | Geospatial layers for rail lines, yards, structures. | C10-05 (CONFIRMED); activation PROPOSED |
| **NARN** (North American Rail Network) | authority / context | Rail lines/nodes for topology pairing with GCIS — card **KFM-P14-PROG-0014**. | KFM-P14-PROG-0014 (PROPOSED card); activation PROPOSED |
| **OpenStreetMap** (rail features) | observation / context (**not** legal-status authority) | Community-mapped rail features; legal-status joins fail closed. | `[DOM-ROADS]` source list (CONFIRMED); OSM/GNIS legal-status denial test PROPOSED |
| **USGS GNIS names** | authority (place names) | Anchor for facility/place names along rail; vernacular/Indigenous names route to TGN or local authorities. | `[DOM-ROADS]` source list (CONFIRMED); activation PROPOSED |
| **KDOT / KanPlan / KanDrive / Kansas GIS** | authority / observation (mostly road-oriented) | Context for at-grade crossings, work zones, rail-roadway interactions in Kansas. | `[DOM-ROADS]` source list (CONFIRMED); activation PROPOSED |
| **WZDx feeds** | authority / observation | Work-zone events; may include rail-crossing-adjacent closures. | `[DOM-ROADS]` source list + C10-04 (CONFIRMED); activation PROPOSED |
| **County/state bridge & restriction data** | authority / observation | Rail-bridge condition, weight/clearance restriction context where available. | `[DOM-ROADS]` source list (CONFIRMED); activation PROPOSED |

> [!WARNING]
> **Source-role anti-collapse.** Source role **cannot be inferred from convenience**. OpenStreetMap and GNIS are **not legal-status authorities** for rail; STB weekly metrics are **not real-time operational truth**; FRA Form 57 incidents are **observations**, not safety-authority outputs within KFM. Activation must assign each source its correct role before ingest. `[DOM-ROADS]` `[ENCY]`

> [!NOTE]
> **STB snapshot-week handling.** C10-05 warns that STB Class I reports are weekly snapshots that overlap; ingest receipts MUST capture the snapshot-week precisely to prevent downstream double-counting. Treat as a PROPOSED ingest invariant (see **OPEN-RAIL-02**). `[ENCY]`

[↑ back to top](#roads--rail--trade-routes--rail-sublane-dossier)

---

## F. Main object families realized in rail

**CONFIRMED object purposes / PROPOSED deterministic identity basis / CONFIRMED temporal-time discipline.** Identity rule inherited from `[DOM-ROADS]` §E: deterministic basis = `source id + object role + temporal scope + normalized digest`. Temporal handling inherited: source, observed, valid, retrieval, release, and correction times stay distinct where material. `[DOM-ROADS]` `[ENCY]`

| Object | Purpose (within rail) | Identity rule | Temporal handling |
|---|---|---|---|
| Rail Segment | Represents Rail Segment evidence or released derivative within rail. | PROPOSED deterministic. | CONFIRMED multi-time discipline. |
| CorridorRoute | Represents a named multi-segment rail corridor. | PROPOSED deterministic. | CONFIRMED multi-time discipline. |
| RouteMembership | Represents segment-to-corridor membership with temporal scope. | PROPOSED deterministic. | CONFIRMED multi-time discipline. |
| Network Node | Represents a rail-graph junction/switch/interchange. | PROPOSED deterministic. | CONFIRMED multi-time discipline. |
| Crossing | Represents a highway-rail crossing (GCIS-anchored when available). | PROPOSED deterministic. | CONFIRMED multi-time discipline. |
| Bridge | Represents a rail bridge (with hydrology cross-lane relation when over water). | PROPOSED deterministic. | CONFIRMED multi-time discipline. |
| TransportFacility (rail role) | Represents a rail-network facility role over a settlement-owned identity. | PROPOSED deterministic. | CONFIRMED multi-time discipline. |
| RestrictionEvent | Represents an embargo, slow order, or closure on rail evidence. | PROPOSED deterministic. | CONFIRMED multi-time discipline. |
| StatusEvent | Represents a rail-status observation from an admissible source role. | PROPOSED deterministic. | CONFIRMED multi-time discipline. |
| OperatorAssignment | Represents time-bounded operator control over a Rail Segment or CorridorRoute. | PROPOSED deterministic. | CONFIRMED multi-time discipline. |
| Historic RouteClaim | Represents a historic rail-alignment claim with evidence and uncertainty. | PROPOSED deterministic. | CONFIRMED multi-time discipline. |

[↑ back to top](#roads--rail--trade-routes--rail-sublane-dossier)

---

## G. Cross-lane relations

**CONFIRMED / PROPOSED:** every cross-lane relation must preserve ownership, source role, sensitivity, and EvidenceBundle support. `[DOM-ROADS]` `[ENCY]`

```mermaid
flowchart LR
  subgraph Rail["Rail Sublane (this dossier)"]
    RS["Rail Segment"]
    CR["Crossing"]
    BR["Bridge"]
    RE["RestrictionEvent"]
    OA["OperatorAssignment"]
    HRC["Historic RouteClaim"]
  end
  subgraph Settle["Settlements / Infrastructure"]
    DEP["Depot / Station / Yard (identity)"]
  end
  subgraph Hyd["Hydrology"]
    WF["Water feature (river / floodplain)"]
  end
  subgraph Haz["Hazards"]
    HE["Closure / detour / flood / fire context"]
  end
  subgraph Arch["Archaeology / Cultural Heritage"]
    INDIG["Historic & Indigenous corridor sensitivity"]
  end
  subgraph People["People / Land"]
    OP["Operator legal-entity identity"]
  end
  CR -. "consumes identity" .-> DEP
  BR -. "crosses" .-> WF
  RE -. "cites" .-> HE
  HRC -. "defers sensitivity to" .-> INDIG
  OA -. "cites identity from" .-> OP
  RS -. "aligns to" .-> HRC
  classDef rail fill:#eef6ff,stroke:#1f6feb,stroke-width:1px
  classDef other fill:#f6f8fa,stroke:#8b949e,stroke-width:1px
  class RS,CR,BR,RE,OA,HRC rail
  class DEP,WF,HE,INDIG,OP other
```

<sub><strong>Diagram status:</strong> PROPOSED visualization. Relations are CONFIRMED in doctrine via `[DOM-ROADS]` §F; the rendering is illustrative and <strong>NEEDS VERIFICATION</strong> against a mounted contract/schema layer.</sub>

| This sublane | Related lane | Relation type | Constraint |
|---|---|---|---|
| Rail | Settlements / Infrastructure | Depot, yard, station, signal-facility identity → rail-network role. | Must preserve ownership and EvidenceBundle support. |
| Rail | Hydrology | Rail-bridge / ford / river-crossing geometry. | Must preserve ownership and EvidenceBundle support. |
| Rail | Hazards | Closures, detours, flood/fire/smoke exposure on rail. | Must preserve ownership and EvidenceBundle support; KFM is **never** an alert authority. |
| Rail | Archaeology / Cultural Heritage | Historic rail alignments paralleling Indigenous corridors; cultural-heritage sensitivity policy is authoritative. | Default-deny on exact location for sensitive cultural overlap. |
| Rail | People / Land | Rail-operator legal-entity identity. | Living-person and operator-entity facts deferred to `[DOM-PEOPLE]`. |
| Rail | Roads (sibling sublane) | Highway-rail crossing geometry shared with road segments. | Crossing object resolves on both sides; one Crossing per real-world feature. |
| Rail | Trade (sibling sublane) | Historic rail alignments interacting with pre-rail TradeRouteCorridors. | Two object families; uncertainty discipline preserved. |

`[DOM-ROADS]` `[DOM-SETTLE]` `[DOM-HYD]` `[DOM-HAZ]` `[DOM-ARCH]` `[DOM-PEOPLE]` `[ENCY]`

[↑ back to top](#roads--rail--trade-routes--rail-sublane-dossier)

---

## H. Map and viewing products

**PROPOSED** rail-mode viewing products inherited from `[DOM-ROADS]` §G:

- Rail alignment layer (modern + historic eras with time-aware state).
- Highway-rail crossing layer (GCIS-anchored where available).
- Rail-facility / yard / depot context view (settlement-identity-linked).
- Operator/Status timeline (Class I / regional / short-line over time).
- Restriction/embargo timeline.
- Freight-corridor context (HIFLD/NTAD/NARN derived).
- Historic rail claim view with uncertainty surface.
- Derived rail-graph / connectivity view (clearly labeled as derived).

**CONFIRMED doctrine** for every viewing product: cross-cutting viewing products include **Evidence Drawer**, **time-aware state**, **trust badges**, **sensitivity-redacted view**, **correction/stale-state view**, and **governed Focus Mode**. `[MAP-MASTER]` `[GAI]`

> [!IMPORTANT]
> **Derived layers are not canonical.** Rail-graph projections, connectivity views, and shortest-path overlays are **derived layers**, never the source of truth. Public clients see them through the governed API; canonical records remain the rail segments and their EvidenceBundles. The browser renderer is `packages/maplibre-runtime/` (v1.3; sole governed renderer). `[DIRRULES]` `[GAI]` `[MAP-MASTER]`

[↑ back to top](#roads--rail--trade-routes--rail-sublane-dossier)

---

## I. Pipeline shape (RAW → PUBLISHED)

**CONFIRMED doctrine / PROPOSED lane application:** the rail sublane inherits the canonical lifecycle from `[DOM-ROADS]` §H without modification. Promotion is a **governed state transition**, not a file move. `[DIRRULES]` `[DOM-ROADS]` `[ENCY]`

```mermaid
flowchart LR
  RAW["RAW — SourceDescriptor exists (rights, sensitivity, citation, time, hash)"]
  WQ["WORK / QUARANTINE — normalize schema, geometry, time, identity, evidence, rights, policy"]
  PROC["PROCESSED — EvidenceRef, ValidationReport, digest closure"]
  CAT["CATALOG / TRIPLET — EvidenceBundle, graph/triplet projection, release candidate"]
  PUB["PUBLISHED — ReleaseManifest, correction path, rollback target, review/policy state"]
  RAW --> WQ
  WQ -->|"gate pass"| PROC
  WQ -. "gate fail → quarantine reason recorded" .-> WQ
  PROC --> CAT
  CAT --> PUB
  classDef stage fill:#fff8e1,stroke:#b08800,stroke-width:1px
  class RAW,WQ,PROC,CAT,PUB stage
```

| Stage | Handling (rail-specific notes) | Gate | Status |
|---|---|---|---|
| **RAW** | Capture immutable FRA / STB / HIFLD / NTAD / NARN / OSM / GNIS / KDOT payloads or references with source role, rights, sensitivity, citation, time, and hash. STB snapshot-week MUST be captured in the receipt. | SourceDescriptor exists. | PROPOSED |
| **WORK / QUARANTINE** | Normalize rail-segment geometry, GCIS-anchored crossing identity, time, operator assignment, evidence, rights, policy; hold failures. | Validation and policy gate pass, or quarantine reason recorded. | PROPOSED |
| **PROCESSED** | Emit validated normalized rail objects, receipts, and public-safe candidates. | EvidenceRef, ValidationReport, digest closure exist. | PROPOSED |
| **CATALOG / TRIPLET** | Emit catalog records, EvidenceBundles, rail-graph triplet projections, release candidates. | Catalog / proof closure passes. | PROPOSED |
| **PUBLISHED** | Serve released public-safe rail artifacts (alignment layers, crossing layer, historic-claim view) through governed APIs and manifests. | ReleaseManifest, correction path, rollback target, review/policy state exist. | PROPOSED |

`[DIRRULES]` `[DOM-ROADS]` `[ENCY]`

[↑ back to top](#roads--rail--trade-routes--rail-sublane-dossier)

---

## J. Sensitivity, rights, and publication posture

**CONFIRMED / PROPOSED defaults** inherited from `[DOM-ROADS]` §I and cross-domain doctrine:

- **Indigenous trade and mobility corridors** that overlap historic rail alignments default to **steward review** and **generalized public geometry**. `[DOM-ROADS]` `[DOM-ARCH]` `[ENCY]`
- **Critical transport facilities** (major yards, intermodal terminals, signal facilities) require review before precise public exposure. `[DOM-ROADS]` `[DOM-SETTLE]`
- **Operational rail status / real-time incident detail** defaults to **deny / generalize** until role and review states are settled; KFM is **not** an alert authority. `[DOM-HAZ]` `[DOM-ROADS]` `[ENCY]`
- **Operator-identity living-person fields** (if any leak through STB or other sources) defer to `[DOM-PEOPLE]` consent/redaction discipline. `[DOM-PEOPLE]`
- **CONFIRMED doctrine:** unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state **blocks public promotion**. `[ENCY]` `[DIRRULES]`

> [!CAUTION]
> **Default-deny on operational rail detail.** Real-time or near-real-time rail-incident detail, precise yard / signal-facility schematics, and operator-internal embargo notices default to **deny / redact / generalize**. Record transforms and reasons via **Redaction Receipt**. The most-restrictive applicable row of the operating contract's §23.2 matrix governs; route uncertain source material to QUARANTINE and ABSTAIN when support is inadequate. `[ENCY]`

[↑ back to top](#roads--rail--trade-routes--rail-sublane-dossier)

---

## K. API, contract, and schema surfaces

**PROPOSED governed-API surfaces** (route names UNKNOWN — exact routes are decided in the parent domain and the governed-API app, not here):

| Endpoint or artifact (PROPOSED) | DTO / schema (PROPOSED) | Outcomes (CONFIRMED finite set per `[GAI]`) | Status |
|---|---|---|---|
| Rail feature / detail resolver | RoadsRailDecisionEnvelope (rail-typed) | ANSWER / ABSTAIN / DENY / ERROR | PROPOSED; exact route UNKNOWN. |
| Rail layer manifest resolver | LayerManifest / domain layer descriptor (rail-typed) | ANSWER / DENY / ERROR | PROPOSED; public-safe release only. |
| Rail Evidence Drawer payload | EvidenceDrawerPayload + EvidenceBundle projection | ANSWER / ABSTAIN / DENY / ERROR | PROPOSED; evidence and policy filtered. |
| Rail Focus Mode answer | RuntimeResponseEnvelope + AIReceipt | ANSWER / ABSTAIN / DENY / ERROR | PROPOSED; AI never root truth. |
| Schema responsibility root | `schemas/contracts/v1/transport/` (Atlas §24.13; ADR-0001 home) | finite validator outcomes | PROPOSED; verify with Directory Rules + ADR (OPEN-RAIL-05). |

`[DOM-ROADS]` `[GAI]` `[DIRRULES]`

[↑ back to top](#roads--rail--trade-routes--rail-sublane-dossier)

---

## L. Validators, tests, fixtures

**PROPOSED** rail-mode validators and tests (inheriting and specializing the `[DOM-ROADS]` §K list). All PROPOSED until project evidence places them in `tests/`, `schemas/`, `policy/`, or `fixtures/`:

- Route membership and designation separation tests (rail corridors vs. segments).
- Operator/status temporal tests (overlapping assignments, succession events).
- **OSM/GNIS legal-status denial test** for rail (community-source-as-authority is a closed gate).
- Historic-overprecision denial test (no false precision on historic alignments).
- Public generalization receipt tests (Redaction Receipt for sensitive alignments).
- Transport-graph projection rollback tests (derived layers can be repointed without losing canonical truth).
- **PROPOSED (rail-specific):** STB snapshot-week deduplication test (per C10-05 warning; **OPEN-RAIL-02**).
- **PROPOSED (rail-specific):** FRA GCIS vs. HIFLD coordinate-conflict resolution test (per C10-05 open question; **OPEN-RAIL-01**).
- **PROPOSED (rail-specific):** GCIS↔NARN topology pairing test (per card KFM-P14-PROG-0014; **OPEN-RAIL-04**).

`[DOM-ROADS]` `[ENCY]`

[↑ back to top](#roads--rail--trade-routes--rail-sublane-dossier)

---

## M. Governed AI behavior for the rail sublane

**CONFIRMED doctrine / PROPOSED implementation:** AI may

- summarize released rail EvidenceBundles;
- compare evidence across rail sources;
- explain limitations and uncertainty;
- draft steward-review notes.

AI **must ABSTAIN** when evidence is insufficient, and **must DENY** where policy, rights, sensitivity, or release state blocks the request. AI is never the root truth source; EvidenceBundle outranks generated language. `[GAI]` `[DOM-ROADS]` `[ENCY]`

> [!IMPORTANT]
> **AIReceipt required on Focus Mode.** Every rail Focus Mode answer must carry an **AIReceipt** with bounded confidence, evidence references, and a finite outcome (ANSWER / ABSTAIN / DENY / ERROR). `[GAI]`

[↑ back to top](#roads--rail--trade-routes--rail-sublane-dossier)

---

## N. Publication, correction, and rollback

**CONFIRMED doctrine / PROPOSED implementation:** rail publication requires **ReleaseManifest**, **EvidenceBundle**, validation/policy support, review state where required, **correction path**, **stale-state rule**, and **rollback target**. Publication is **never** a file move; it is a governed state transition recorded by **PromotionDecision** and reversed by **RollbackCard**. `[ENCY Appendix E]` `[DOM-ROADS]` `[ENCY]` `[DIRRULES]`

| Mechanism | Purpose | Status |
|---|---|---|
| ReleaseManifest | Records released rail artifacts and the gates they passed. | PROPOSED |
| EvidenceBundle | Resolves every public rail claim's EvidenceRef. | PROPOSED |
| PromotionDecision | Records the governed transition into PUBLISHED. | PROPOSED |
| RollbackCard | Names the rollback target and preserves history while repointing release state. | PROPOSED |
| CorrectionNotice | Records corrections to released rail artifacts without rewriting history. | PROPOSED |
| RedactionReceipt | Records any public-safe geometry or field transformation. | PROPOSED |

[↑ back to top](#roads--rail--trade-routes--rail-sublane-dossier)

---

## O. Verification backlog and open questions

### O.1 Domain-inherited items (from `[DOM-ROADS]` §N)

| Item to verify | Evidence that would settle it | Status |
|---|---|---|
| Verify KDOT / FHWA / FRA / WZDx source rights and terms. | Mounted repo source registry, schemas, tests, logs, emitted artifacts, review records, or release manifests. | NEEDS VERIFICATION |
| Verify Indigenous / cultural corridor policy on rail overlap. | Mounted repo `policy/sensitivity/` and `[DOM-ARCH]` review records. | NEEDS VERIFICATION |
| Implement RouteUncertaintyProfile for historic rail claims. | Mounted repo schemas / contracts / tests. | NEEDS VERIFICATION |
| Verify transport graph and MapLibre integration for rail. | Mounted repo `packages/maplibre-runtime/`, `apps/explorer-web/`, layer manifests. | NEEDS VERIFICATION |

### O.2 New (this dossier)

| ID | Question | Why it's open | Suggested resolution |
|---|---|---|---|
| **OPEN-DR-SUBLANE-01** | Should `docs/domains/<domain>/sublanes/` be a canonical organizational layer, or should multi-mode domains use a different decomposition (chapter files, atlas extensions, flat sibling READMEs)? And is "sublane" the right term given it collides with the Focus Mode "sub-lane" (§6.7)? | The `sublanes/` layer is not in `directory-rules.md` §6.1; "sublane" is not a defined term. Parallel to **OPEN-DR-02** (runbooks subfolder vs flat) and **OPEN-DR-01** (PROV vs PROVENANCE naming). | ADR. Until resolved, treat this dossier as a scaffold deferring all canonical authority to `[DOM-ROADS]`; consider renaming to a non-colliding term. |
| **OPEN-DR-SUBLANE-02** | Naming and casing for sublane filenames. | This file uses lowercase `rail.md`; siblings likely follow. Possible mismatch with other docs (e.g., UPPERCASE `ISO-19115.md`). | Per-root README decision under the §6.1.a-equivalent of Directory Rules. |
| **OPEN-RAIL-01** | GCIS vs HIFLD coordinate-disagreement policy for the same crossing. | C10-05 open question; rail-specific. | Validator rule + sensitivity-aware default; documented in the parent README and here. |
| **OPEN-RAIL-02** | STB Class I snapshot-week deduplication contract. | C10-05 warning; rail-specific ingest invariant. | Receipt invariant + ingest test. |
| **OPEN-RAIL-03** | Operational-rail-detail sensitivity tier (yard schematics, signal facilities, real-time embargo). | Default-deny is doctrinally clear; the **specific tier (T0–T4)** and review cadence are not set for rail. | ADR-S-05 (sensitivity tier scheme) downstream. |
| **OPEN-RAIL-04** | Pairing of FRA GCIS crossings with NARN rail lines/nodes. | Card **KFM-P14-PROG-0014** PROPOSES the pairing but does not prove repo implementation. | Pipeline spec + validator + test fixture. |
| **OPEN-RAIL-05** | Schema/contract slug for this domain: `transport` (Atlas §24.13) vs `roads-rail-trade` (docs lane). | Atlas §24.13 uses `schemas/contracts/v1/transport/` + `contracts/transport/`; the docs lane is `roads-rail-trade`. Slug drift. | ADR; align schema/contract homes with docs lane or document the divergence. |

[↑ back to top](#roads--rail--trade-routes--rail-sublane-dossier)

---

## Related docs

- `docs/domains/roads-rail-trade/README.md` — PROPOSED parent dossier (NEEDS VERIFICATION in repo).
- `docs/domains/roads-rail-trade/sublanes/README.md` — PROPOSED sublane index.
- `docs/domains/roads-rail-trade/sublanes/roads.md` — PROPOSED sibling sublane.
- `docs/domains/roads-rail-trade/sublanes/trade.md` — PROPOSED sibling sublane.
- `docs/domains/settlements-infrastructure/README.md` — depot / station / facility identity owner.
- `docs/domains/hydrology/README.md` — bridge / ferry / ford / river-crossing context.
- `docs/domains/archaeology/README.md` — historic + Indigenous corridor sensitivity authority.
- `docs/domains/hazards/README.md` — closure / detour / flood / fire / smoke event context.
- `docs/domains/people-dna-land/README.md` — operator legal-entity identity authority.
- `docs/doctrine/directory-rules.md` — placement and lifecycle authority (CONFIRMED root listing for `docs/domains/roads-rail-trade/`).
- `docs/standards/PROV.md` — provenance reference (naming variance with `PROVENANCE.md` per **OPEN-DR-01**).
- `docs/registers/VERIFICATION_BACKLOG.md` — canonical destination for items above once triaged.
- `docs/registers/DRIFT_REGISTER.md` — destination for the slug-drift (OPEN-RAIL-05) and sublane-layer (OPEN-DR-SUBLANE-01) conflicts.
- `docs/adr/` — destination for **OPEN-DR-SUBLANE-01** and **OPEN-RAIL-05** resolution.

---

## Appendix — Atlas citation map

<details>
<summary><strong>Open: short-name citations used in this dossier</strong></summary>

| Short-name | Source | Role in this dossier |
|---|---|---|
| `[DOM-ROADS]` | Roads / Rail / Trade Routes dossier | Primary domain dossier; this sublane inherits scope, terminology, source families, object families, cross-lane relations, pipeline shape, governed-AI rules, publication discipline, and the verification backlog. |
| `[DOM-SETTLE]` | Settlements / Infrastructure dossier | Owner of depot / station / facility canonical identity. |
| `[DOM-HYD]` | Hydrology dossier | Owner of water-feature evidence under rail bridges. |
| `[DOM-HAZ]` | Hazards dossier | Owner of closure / detour / flood / fire / smoke event context cited by rail. |
| `[DOM-ARCH]` | Archaeology / Cultural Heritage dossier | Sensitivity authority for historic and Indigenous corridor overlap. |
| `[DOM-PEOPLE]` | People / Genealogy / DNA / Land Ownership dossier | Authority for operator legal-entity identity and any living-person fields. |
| `[ENCY]` | KFM Encyclopedia | Master domain / object / source / capability spine; lifecycle and EvidenceBundle doctrine. |
| `[DIRRULES]` | Directory Rules | Placement and lifecycle authority; CONFIRMED root listing of `docs/domains/roads-rail-trade/`. |
| `[MAP-MASTER]` | MapLibre Master | Renderer, tiles, Evidence Drawer, Focus Mode doctrine; cross-cutting viewing products. |
| `[GAI]` | Governed AI dossier | AIReceipt doctrine; finite outcomes (ANSWER / ABSTAIN / DENY / ERROR). |

</details>

<details>
<summary><strong>Open: card-level references (Pass 10 / Pass 23–32)</strong></summary>

- **Pass-10 C10-05 — Rail Stack: FRA GCIS, FRA Form 57, STB Class I, HIFLD/NTAD** (CONFIRMED). Includes the snapshot-week warning and the GCIS↔HIFLD coordinate-disagreement open question.
- **Pass-10 C10-04 — Transit Stack: GTFS, GTFS-rt, KCATA, KanDrive, WZDx** (CONFIRMED; tangential for rail-crossing-adjacent work-zone events).
- **KFM-P14-PROG-0014 — FRA GCIS / NARN rail-crossing topology package** (PROPOSED; carried forward through Pass 32; repo implementation unverified).
- **KFM-P20-PROG-0013 — Frontier routes FeatureCollection builder** (PROPOSED; includes depots and historic transport corridors). NEEDS VERIFICATION against the corpus before relying on this card.

Atlas v1.1 reference for `[DOM-ROADS]` (Chapter 13): begins at the §13 chapter opener in the v1.0 interior; §24.13 carries the responsibility-root crosswalk (`transport` slug).

</details>

<details>
<summary><strong>Open: doctrine boundaries this dossier MUST NOT bend</strong></summary>

- MUST NOT introduce a parallel schema, contract, policy, source, registry, release, or proof home (Directory Rules §2.4 / §5).
- MUST NOT publish via a path that bypasses the governed API (`apps/governed-api/`).
- MUST NOT collapse generation and approval into one unreviewed path.
- MUST NOT treat derived rail-graph layers as sovereign truth.
- MUST NOT claim repo maturity, route names, deployed behavior, test coverage, or CI enforcement without mounted-repo evidence.

`[DIRRULES]` `[ENCY]` `[GAI]`

</details>

---

**Related:** [Roads/Rail/Trade Routes README](../README.md) · [Sublane index](./README.md) · [Roads sublane](./roads.md) · [Trade sublane](./trade.md) · [Directory Rules](../../../doctrine/directory-rules.md)

**Last updated:** 2026-06-07 · **Edition:** v0.2 · **Supersedes:** v0.1 (first edition)

[↑ back to top](#roads--rail--trade-routes--rail-sublane-dossier)
