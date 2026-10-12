<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-domains-roads-rail-trade-sublanes-trade-routes
title: Trade Routes & Historic Alignments Sublane — Roads, Rail, and Trade Routes Domain Dossier
type: standard
version: v0.2
status: draft
owners: <Roads/Rail/Trade Routes domain steward — TBD>; <cultural-heritage / sovereignty reviewer — TBD>
created: 2026-06-07
updated: 2026-10-12
policy_label: public (sublane scaffold) — content tiers vary; historic/Indigenous/cultural corridor detail defaults to steward review + generalized geometry
owning_root: docs/
responsibility: "Human-facing dossier for the historic / trade / Indigenous corridor sublane of the Roads, Rail & Trade Routes domain; not evidence, policy, release, or publication authority."
truth_posture: "Doctrine statements are CONFIRMED where cited; sublane structure, paths, routes, schemas, tiers, and tests are PROPOSED or NEEDS VERIFICATION."
supersedes:
  - kfm://doc/docs-domains-roads-rail-trade-sublanes-trade-routes-redirect
related:
  - docs/domains/roads-rail-trade/README.md
  - docs/domains/roads-rail-trade/sublanes/README.md
  - docs/domains/roads-rail-trade/sublanes/roads.md
  - docs/domains/roads-rail-trade/sublanes/rail.md
  - docs/domains/roads-rail-trade/sublanes/trade.md
  - docs/domains/archaeology/README.md
  - docs/domains/people-dna-land/README.md
  - docs/domains/settlements-infrastructure/README.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/architecture/governed-api/README.md
  - docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - docs/standards/PROV.md
  - docs/standards/REDACTION_DETERMINISM.md
tags: [kfm, domain, roads-rail-trade, sublane, trade-routes, historic-routes, cultural-heritage]
notes:
  - "2026-10-12: merged unique content from docs/domains/roads-rail-trade/sublanes/trade_routes.md (which shared this doc_id) — owner-directed duplicate removal"
  - 'CONTRACT_VERSION = "3.0.0" pinned per ai-build-operating-contract.md'
  - "Sublane subdivision under docs/domains/<domain>/ is PROPOSED structure; not in Directory Rules (OPEN-TRADE-01)."
  - "TERMINOLOGY: 'sublane' is not established KFM doctrine. 'lane' is defined; 'sub-lane' exists only in the Focus Mode cross-root sense (Directory Rules §6.7). See OPEN-TRADE-01."
  - "FILENAME is itself an open question: trade-routes.md vs historic-routes.md vs routes-historic.md (OPEN-TRADE-02). The underscore twin trade_routes.md is now a redirect stub to this file."
  - "TIER SCHEME T0–T4 (merged §7.1–§7.3) is PROPOSED pending ADR-S-05 (Atlas §24.5.1); tier transitions are PROPOSED motion, not adopted doctrine."
  - "Slug variance: Directory Rules §12 uses schemas/contracts/v1/domains/roads-rail-trade/; Atlas §24.13 uses schemas/contracts/v1/transport/. CONFLICTED — see OPEN-TRADE-03."
  - "HIGHEST-SENSITIVITY sublane: historic/Indigenous/cultural corridors default to steward review + generalized public geometry; cultural truth and sensitivity policy are owned by Archaeology/Cultural Heritage."
  - "All path, route, schema, and tooling claims remain PROPOSED until a mounted repository is inspected."
[/KFM_META_BLOCK_V2] -->

# Trade Routes & Historic Alignments Sublane — Roads, Rail, and Trade Routes Domain

> Historic and trade/mobility-corridor evidence inside the Roads, Rail, and Trade Routes domain — its scope, source posture, object spine, lifecycle, **sensitivity-first** publication posture, governed surfaces, and verification backlog.

<p align="left">
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue?style=flat-square">
  <img alt="Doc type: standard" src="https://img.shields.io/badge/doc-standard-informational?style=flat-square">
  <img alt="CONTRACT_VERSION 3.0.0" src="https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-1f6feb?style=flat-square">
  <img alt="Posture: governance-first" src="https://img.shields.io/badge/posture-governance--first-1f6feb?style=flat-square">
  <img alt="Sublane: PROPOSED" src="https://img.shields.io/badge/sublane-PROPOSED-orange?style=flat-square">
  <img alt="Term: sublane not doctrine" src="https://img.shields.io/badge/%22sublane%22-NOT%20DOCTRINE-red?style=flat-square">
  <img alt="Sensitivity: steward-review default" src="https://img.shields.io/badge/sensitivity-steward--review%20%2B%20generalize-d9480f?style=flat-square">
  <img alt="Last updated: 2026-10-12" src="https://img.shields.io/badge/updated-2026--10--12-555?style=flat-square">
</p>

**Status:** draft · **Version:** v0.2 · **Parent dossier:** [`docs/domains/roads-rail-trade/`](../README.md) · **Owners:** Roads/Rail/Trade Routes steward — `TBD` · cultural-heritage / sovereignty reviewer — `TBD` · **Last updated:** 2026-10-12

> 2026-10-12: merged unique content from `docs/domains/roads-rail-trade/sublanes/trade_routes.md` (which shared this doc_id) — owner-directed duplicate removal

> [!NOTE]
> **Merged from `trade_routes.md` (v2, 2026-06-07).** That underscore-named twin carried this file's `doc_id` and is now a redirect stub. Its unique content is folded in below: the out-of-scope routing table and parent-position table (§2.3–§2.4), the Freight Corridor term (§3), object-activity and cited-family tables (§5.1–§5.2) plus the object-topology diagram (§5.3), extra source families (§4), stage-specific pipeline handling (§6.1), the PROPOSED T0–T4 tier tables and transitions (§7.1–§7.3), publication/correction/rollback (§7.4), extra cross-lane rows (§11.1), viewing-product tiers (§12.1), contracts/policy surfaces and an illustrative envelope (§8), test details (§9.1), AI request examples (§10.1), and its open questions (§13.4). Where the two drafts disagreed, both positions are kept and the disagreement is recorded in §13.4.

> [!CAUTION]
> **This is the highest-sensitivity sublane of the three.** Historic, Indigenous, treaty, oral-history, and cultural-corridor evidence defaults to **steward review** and **generalized public geometry**. Cultural truth and sensitivity policy are **owned by Archaeology / Cultural Heritage** (`[DOM-ARCH]`), not here; this sublane carries the route-claim relation only. Do not publish exact historic/cultural-corridor geometry without reviewed evidence and a transform receipt. `[DOM-ROADS]` §I `[DOM-ARCH]` `[ENCY]`

---

## Quick navigation

- [1. Sublane in context](#1-sublane-in-context)
- [2. Scope, boundary, and explicit non-ownership](#2-scope-boundary-and-explicit-non-ownership)
- [3. Ubiquitous language (trade-routes sublane)](#3-ubiquitous-language-trade-routes-sublane)
- [4. Source posture](#4-source-posture)
- [5. Object families](#5-object-families)
- [6. Lifecycle — RAW → PUBLISHED](#6-lifecycle--raw--published)
- [7. Sensitivity, rights, and publication posture](#7-sensitivity-rights-and-publication-posture)
- [8. API, contract, and schema surfaces](#8-api-contract-and-schema-surfaces)
- [9. Validators, tests, fixtures](#9-validators-tests-fixtures)
- [10. Governed AI behavior](#10-governed-ai-behavior)
- [11. Cross-lane and cross-sublane relations](#11-cross-lane-and-cross-sublane-relations)
- [12. Map and viewing products](#12-map-and-viewing-products)
- [13. Open questions and verification backlog](#13-open-questions-and-verification-backlog)
- [14. Related docs](#14-related-docs)

---

## 1. Sublane in context

This file documents the **Trade Routes & Historic Alignments sublane** — the slice of the Roads, Rail, and Trade Routes domain that owns evidence and released derivatives for **historic and trade/mobility corridors**: historic routes, historic route *claims*, trade-route corridors, cross-period route memberships, and movement story nodes. The sister sublanes — `roads.md` and `rail.md` — own modern public-road and rail evidence respectively. All three sublanes share the same parent dossier, source-role doctrine, and lifecycle invariant. **[CONFIRMED domain scope from `[DOM-ROADS]` `[ENCY]`; PROPOSED sublane subdivision.]**

> [!IMPORTANT]
> **The `sublanes/` subdirectory is PROPOSED structure, not Directory Rules canon — and "sublane" is not a defined KFM term.**
> Directory Rules §12 ("Domain Placement Law") prescribes `docs/domains/<domain>/` as the dossier home and pins `roads-rail-trade` as the canonical domain slug, but does **not** define a `sublanes/` subdirectory pattern. Separately, KFM defines **lane** (a domain/topic segment inside a responsibility root) and uses **sub-lane** only for **Focus Modes** (a geographic *area* across responsibility roots, §6.7) — so this file's "sublane" (a per-mode partition within one domain) is a **coined term that collides with the Focus Mode sense**. Both the subdirectory pattern and the term should be ratified by the domain README or a small ADR before either is treated as canonical. Until then, treat `docs/domains/roads-rail-trade/sublanes/trade-routes.md` as `PROPOSED / NEEDS VERIFICATION`. See [§13 OPEN-TRADE-01](#13-open-questions-and-verification-backlog). `[DIRRULES]`

### 1.1 Why a Trade Routes sublane

The parent domain bundles three distinct temporal and authority regimes under one bounded context. The Unified Implementation Architecture Build Manual flags this directly: the public posture for this slice is that **historic and cultural routes are generalized unless reviewed evidence supports precision, and graph projections are derived only** — and the named risk is **conflating alignment, ownership, operator, legal status, and route claim, plus false precision for historic / Indigenous / cultural corridors**. `[DOM-ROADS via UNIFIED]` Separating this sublane from the modern roads/rail sublanes lets the sensitivity-first posture be the default *here* without weakening, or being weakened by, the modern-evidence posture there.

### 1.2 Three sublanes — at a glance

| Sublane | Owns (CONFIRMED scope per `[DOM-ROADS]`) | Dominant source-role posture | File |
|---|---|---|---|
| Roads | Road Segment; road-side of Bridge / Ferry / River Crossing; road-aligned Crossing, events, facilities; modern RouteMembership / CorridorRoute | authority / observation (modern) | `sublanes/roads.md` |
| Rail | Rail Segment; Depot; Siding; Yard; rail-aligned Crossing / Bridge; rail events; Freight Corridor (rail) | authority / observation (modern) | `sublanes/rail.md` |
| **Trade routes & historic alignments** *(this file)* | Historic Route; Historic RouteClaim; TradeRouteCorridor; Movement Story Node; cross-period RouteMembership | **claim / interpretive (historic)** | `sublanes/trade-routes.md` *(filename PROPOSED — OPEN-TRADE-02)* |

> [!NOTE]
> **Filename is an open question.** This file's name (`trade-routes.md` vs `historic-routes.md` vs `routes-historic.md`) is unsettled; the parent dossier should ratify it before either form is treated as canonical. See **OPEN-TRADE-02**.
>
> **Three spellings existed (merged 2026-10-12).** The historic-corridor sublane appeared as `trade-routes.md` (kebab — this file; the form sibling cross-links and contracts use), `trade_routes.md` (underscore; now a redirect stub to this file), and is adjacent to a separate sibling [`trade.md`](./trade.md) that covers the **modern trade / freight** slice. This file is scoped to **historic / trade / Indigenous corridors**; the modern-freight slice lives in `trade.md`. Whether `trade.md` and this file stay split (Option B) or fold into one third sublane remains open — see `trade.md` OPEN-TRADE-A1 and §13.4 OQ-TR-07.

[↑ back to top](#trade-routes--historic-alignments-sublane--roads-rail-and-trade-routes-domain)

---

## 2. Scope, boundary, and explicit non-ownership

### 2.1 What this sublane owns

CONFIRMED scope (subset of `[DOM-ROADS]` domain scope, narrowed to historic/trade corridors):

- **Historic Route** — a documented past alignment (trail, wagon road, abandoned corridor) carried as evidence with source role, time, and release state.
- **Historic RouteClaim** — a *claim* about a historic alignment, recorded **with evidence and uncertainty rather than as fact**. The claim is the object; the alignment it asserts is not promoted to truth without reviewed support.
- **TradeRouteCorridor** — a trade / mobility corridor as an entity, including Indigenous trade and mobility corridors where the cultural-heritage owner permits a route-relation projection.
- **Cross-period RouteMembership** — membership of a segment or feature in a corridor across eras, kept separate from any single segment.
- **Movement Story Node** — narrative / interpretive nodes tied to historic movement evidence.

### 2.2 What this sublane explicitly does not own

CONFIRMED non-ownership (inherited from `[DOM-ROADS]` parent rule):

- **Cultural and Indigenous corridor *truth and sensitivity policy*** stays with `archaeology` / cultural heritage (`[DOM-ARCH]`). This sublane carries the route-claim relation; it does **not** author cultural truth or set the sensitivity tier. `[DOM-ARCH]` `[DOM-ROADS]`
- **Forts, missions, settlements, and townsites** as place/settlement objects stay with `settlements-infrastructure`. `[DOM-SETTLE]` `[DOM-ROADS]`
- **Archaeological site identity and exact coordinates** stay with `archaeology`; exact site coordinates are **denied** by default and are never absorbed into a route claim. `[DOM-ARCH]`
- **Water evidence** at fords / river crossings stays with `hydrology`. `[DOM-HYD]`
- **Person / land / ownership facts** (e.g., a corridor crossing private land) stay with `people-dna-land`. `[DOM-PEOPLE]`
- **Modern road and rail objects** stay with the Roads and Rail sublanes.

> [!WARNING]
> **A modern alignment MUST NOT absorb a historic/cultural claim.** Where a present-day road or rail line overlies a historic or Indigenous corridor, the two are distinct objects with distinct sensitivity postures. The modern segment does not inherit, override, or silently publish the historic claim's geometry; the cross-sublane edge preserves the more-restrictive posture. `[DOM-ROADS]` §I `[DOM-ARCH]`

### 2.3 Out-of-scope routing table (merged from `trade_routes.md` §1)

| Out of scope here | Lives in |
|---|---|
| Modern road and rail geometry, KDOT/TIGER pipelines | `sublanes/roads.md`, `sublanes/rail.md` |
| Modern trade / freight corridors, NHFN, freight-flow aggregates | `sublanes/trade.md` (modern-freight slice) |
| Depots, sidings, yards, transport facility identity | Parent domain + cross-lane edge to Settlements / Infrastructure `[DOM-SETTLE]` |
| River-crossing hydrologic context | Cross-lane edge to Hydrology `[DOM-HYD]` |
| Archaeological site coordinates along historic alignments | Archaeology / Cultural Heritage (deny-default site coords) `[DOM-ARCH]` |
| Living-person, DNA, or person-parcel joins via genealogy of route operators | People / Genealogy / DNA / Land `[DOM-PEOPLE]` |
| Emergency-alert authority over current route closures | Never KFM; the alert-authority boundary holds `[DOM-HAZ]` |

**Why it is its own sublane (PROPOSED).** The trade-route and historic-corridor slice has distinct source genres (historic atlases, treaty material, ethnohistorical and oral evidence), a stricter sensitivity default (steward review and generalized public geometry for Indigenous corridors), and a different evidence-handling shape (claim-bearing rather than observation-bearing). `[DOM-ROADS]` `[ENCY]` `[UNIFIED]`

### 2.4 Position within the parent domain (merged from `trade_routes.md` §2)

CONFIRMED doctrine — this sublane sits **inside** the Roads / Rail / Trade Routes domain (Atlas v1.0 Ch. 13); the parent's identity, scope, and lifecycle invariants apply in full. `[DOM-ROADS]` `[ENCY]`

| Layer | Parent (CONFIRMED doctrine / PROPOSED home) | This sublane (PROPOSED scope) |
|---|---|---|
| Atlas chapter | Ch. 13 — Roads / Rail / Trade Routes `[DOM-ROADS]` | Trade-route + historic-corridor subset of Ch. 13 §B, §C, §I |
| Docs home | `docs/domains/roads-rail-trade/` `[DIRRULES]` | `docs/domains/roads-rail-trade/sublanes/trade-routes.md` (**PROPOSED**) |
| Contracts (meaning) | `contracts/transport/` (per Ch. 24.13 and the parent README v1.1 correction) **vs** `contracts/domains/roads-rail-trade/` (Directory Rules §12; where the current contract drafts actually sit) — CONFLICTED, see OPEN-TRADE-03 | _no separate sublane home — uses parent_ |
| Schemas (shape) | `schemas/contracts/v1/transport/` (per Ch. 24.13; ADR-0001) **vs** `…/domains/roads-rail-trade/` (§12) — CONFLICTED, see OPEN-TRADE-03 | _no separate sublane home — uses parent_ |
| Policy (admissibility) | `policy/domains/roads-rail-trade/` (PROPOSED per Directory Rules §12) `[DIRRULES]` | Generalization and cultural-route sensitivity rules concentrate here |
| Data lifecycle | `data/{raw,work,quarantine,processed,catalog,published}/roads-rail-trade/` (PROPOSED) `[DIRRULES]` | Historic-source carrier may need a distinct *processed*-stage projection from the modern-source carrier |

> [!NOTE]
> Per Directory Rules §12 (Domain Placement Law), domains MUST NOT become root folders, and sublanes MUST NOT split a domain's lifecycle into parallel data, schema, or policy homes. This sublane is **documentation-only**: it does not create a `data/trade-routes/` or `schemas/contracts/v1/trade-routes/` tree, and executable artefacts stay under the parent's responsibility roots. (A `schemas/contracts/v1/trade-routes/README.md` does exist in the repo; whether it is a compatibility pointer or drift is tracked under OPEN-TRADE-03.) `[DIRRULES]`

[↑ back to top](#trade-routes--historic-alignments-sublane--roads-rail-and-trade-routes-domain)

---

## 3. Ubiquitous language (trade-routes sublane)

CONFIRMED terms (from `[DOM-ROADS]` §C) used inside this sublane; field realization in any specific contract or schema is PROPOSED until verified in `schemas/contracts/v1/...`.

| Term | One-line definition (CONFIRMED meaning) | Field realization | Citation |
|---|---|---|---|
| **Historic Route** | A documented past alignment carried as evidence, constrained by source role, evidence, time, and release state. | PROPOSED | `[DOM-ROADS]` `[ENCY]` |
| **Historic RouteClaim** | A claim about a historic alignment, recorded with evidence and uncertainty rather than as fact. | PROPOSED | `[DOM-ROADS]` `[ENCY]` |
| **TradeRouteCorridor** | A trade / mobility corridor as an entity in its own right; may include Indigenous corridors under cultural-heritage governance. | PROPOSED | `[DOM-ROADS]` `[ENCY]` |
| **RouteMembership** *(cross-period)* | A sourced, temporal claim that a feature belongs to a corridor across one or more eras. | PROPOSED | `[DOM-ROADS]` `[ENCY]` |
| **Movement Story Node** | A narrative / interpretive node tied to historic movement evidence. | PROPOSED | `[DOM-ROADS]` `[ENCY]` |
| **CorridorRoute** | A route as an entity, separable from any single underlying segment (historic-mode here); trade-route corridors are a typed specialization. | PROPOSED | `[DOM-ROADS]` `[ENCY]` |
| **Freight Corridor** *(merged)* | CONFIRMED domain-owned object (Atlas Ch. 13 §B). Modern freight-context corridor; PROPOSED cross-citation pattern with `TradeRouteCorridor` where a modern corridor inherits historical context. Primary home is `sublanes/trade.md`. | PROPOSED | `[DOM-ROADS]` `[ENCY]` |

> [!TIP]
> **A claim is not a fact; a corridor is not a coordinate.** The defining discipline of this sublane is that a *Historic RouteClaim* records what a source asserts about an alignment together with its uncertainty — it never silently becomes a precise published line. Validators in §9 enforce historic-overprecision denial. `[DOM-ROADS K-tests]`

> [!IMPORTANT]
> **Geometry is not authority.** A polyline of any historic trail or Indigenous mobility corridor is **a claim**, not a fact. The sublane handles every trade-route geometry as `Historic RouteClaim` evidence under `EvidenceBundle` resolution. Promoting that evidence to a published `TradeRouteCorridor` is a governed state transition with its own gates. `[DOM-ROADS]` `[ENCY]` `[DIRRULES]`

[↑ back to top](#trade-routes--historic-alignments-sublane--roads-rail-and-trade-routes-domain)

---

## 4. Source posture

This sublane draws on the parent `[DOM-ROADS]` source families (TIGER/Line, FHWA HPMS, NHFN, WZDx, KDOT family, county bridge/restriction data, GNIS, OSM) for *modern geometry context only*, and depends on **cultural-heritage and archival sources governed by `[DOM-ARCH]`** for the historic/Indigenous claim side. Source role is fixed at admission and is **never** upgraded by promotion; rights and current terms remain `NEEDS VERIFICATION` until each descriptor and activation decision is mounted-repo-verified. `[DOM-ROADS]` `[ENCY]`

| Source posture | Role here | Sensitivity / rights | Status |
|---|---|---|---|
| **GNIS names** | context — gazetteer names only; vernacular / Indigenous names route to TGN or local authorities | open per USGS terms (NEEDS VERIFICATION); **not** a corridor-truth authority | CONFIRMED listing; descriptor PROPOSED `[DOM-ROADS]` |
| **OpenStreetMap (historic tags)** | observation / context — community geometry only | ODbL terms NEEDS VERIFICATION; **MUST NOT** confer historic-route legitimacy | CONFIRMED listing; descriptor PROPOSED `[DOM-ROADS]` |
| **TIGER/Line, KDOT family** | context — modern alignment that *may parallel* a historic corridor | rights NEEDS VERIFICATION; modern geometry only | CONFIRMED listing; descriptor PROPOSED `[DOM-ROADS]` |
| **Cultural-heritage / archival / oral-history sources** | claim / interpretive — the historic / Indigenous corridor side | **owned and gated by `[DOM-ARCH]`**; steward + rights-holder review; generalized geometry default | PROPOSED; governance deferred to `[DOM-ARCH]` |
| **Treaty / administrative compilations** | administrative — context, **not** observed-event timelines | source-role tag preserved; MUST NOT be cited as observation | PROPOSED `[ENCY]` |
| **Historic atlases and survey maps** (e.g., GLO, USGS historical topographic) *(merged)* | authority / observation / context / model as source role requires; freshness source-vintage specific | rights and current terms NEEDS VERIFICATION; sensitive joins fail closed | Cited to `[DOM-ROADS]` `[ENCY]` in the merged draft, but not in the parent §D roster quoted below — NEEDS VERIFICATION; descriptor PROPOSED |
| **Ethnohistorical and oral-history corpora** (Indigenous mobility, treaty, traveller accounts) *(merged)* | context / model as source role requires (rarely *authority*) | **steward-review default**; rights, sovereignty, and consent terms NEEDS VERIFICATION | PROPOSED `[DOM-ROADS]` `[DOM-ARCH]` `[ENCY]` |
| **Census TIGER/Line roads — historic editions** *(merged)* | authority / observation / context / model as source role requires; edition-specific | rights and current terms NEEDS VERIFICATION | CONFIRMED listing; descriptor PROPOSED `[DOM-ROADS]` |
| **National Park Service / National Historic Trail records** *(merged)* | authority / observation / context / model as source role requires | rights and current terms NEEDS VERIFICATION | **PROPOSED addition** — not in parent §D table |
| **County, state, and tribal historical-society holdings** *(merged)* | context / model as source role requires | **steward-review default**; rights NEEDS VERIFICATION | **PROPOSED addition** — not in parent §D table |

> [!CAUTION]
> The two rows marked **PROPOSED addition** extend the parent domain's §D roster (Census TIGER, FHWA HPMS, FHWA NHFN, WZDx, KDOT/KanPlan/KanDrive, county/state bridge data, GNIS, OpenStreetMap `[DOM-ROADS]` `[ENCY]`). Admission requires a `SourceDescriptor`, rights review, and the parent domain's RAW-stage gate before any historic-trail material is ingested. Do not treat them as accepted source families. OSM historic tags in scope are `historic=*`, `route=*`, `name=*`, `network=*` — observation/context only, never legal-status authority (validator-enforced; §9).

> [!CAUTION]
> **Source-role anti-collapse, sharpened for historic corridors.** Community-science and gazetteer sources (OSM, GNIS) **cannot** establish that a historic or Indigenous corridor existed at a given precise location. They supply names and modern geometry context only. The corridor claim itself is `claim`/`interpretive` evidence under `[DOM-ARCH]` governance. Administrative or treaty compilations are `administrative` context, never observed-event timelines. `[DOM-ROADS]` `[ENCY]`

[↑ back to top](#trade-routes--historic-alignments-sublane--roads-rail-and-trade-routes-domain)

---

## 5. Object families

CONFIRMED object-family spine from `[DOM-ROADS]` §E, narrowed to historic/trade objects. **Identity rule** and **temporal handling** rows are direct restatements of the parent-dossier rules.

| Object | Purpose (within this sublane) | Identity rule | Temporal handling | Status |
|---|---|---|---|---|
| **Historic Route** | Represents a documented past alignment as evidence or released derivative. | PROPOSED deterministic basis: `source id + object role + temporal scope + normalized digest` | CONFIRMED: source, observed, valid, retrieval, release, and correction times stay distinct where material. | CONFIRMED object / PROPOSED implementation `[DOM-ROADS]` `[ENCY]` |
| **Historic RouteClaim** | Represents a claim about a historic alignment, with evidence and uncertainty. | PROPOSED as above. | CONFIRMED temporal handling as above. | CONFIRMED object / PROPOSED implementation `[DOM-ROADS]` `[ENCY]` |
| **TradeRouteCorridor** | Represents a trade / mobility corridor as an entity; Indigenous corridors under `[DOM-ARCH]` governance. | PROPOSED as above. | CONFIRMED temporal handling as above. | CONFIRMED object / PROPOSED implementation `[DOM-ROADS]` `[ENCY]` |
| **RouteMembership** *(cross-period)* | Sourced, temporal claim that a feature belongs to a corridor across eras. | PROPOSED as above. | CONFIRMED temporal handling as above. | CONFIRMED object / PROPOSED implementation `[DOM-ROADS]` `[ENCY]` |
| **Movement Story Node** | Narrative / interpretive node tied to historic movement evidence. | PROPOSED as above. | CONFIRMED temporal handling as above. | CONFIRMED object / PROPOSED implementation `[DOM-ROADS]` `[ENCY]` |

### 5.1 Activity of parent-domain objects in this sublane (merged from `trade_routes.md` §4)

| Object | Activity in this sublane |
|---|---|
| `Historic RouteClaim`, `TradeRouteCorridor` | **TR-primary** |
| `RouteMembership` | **TR-primary** (period and alignment claims propagate via membership) |
| `CorridorRoute` | TR-supporting |
| `Movement Story Node` | TR-supporting (narrative surface) |
| `Freight Corridor` | TR-supporting (modern → historic cross-citation; primary home `trade.md`) |
| `Road Segment` / `Rail Segment` | Cited by `RouteMembership`; not owned by this sublane |
| `Route Event` / `Operator Status` | Out of scope here (current status; lives in `roads.md` / `rail.md`) |

> [!NOTE]
> `Route Event` and `Operator Status` are the CONFIRMED owned-object names from Atlas Ch. 13 §B; earlier drafts used `RestrictionEvent` / `StatusEvent` as field realizations. Those realizations are PROPOSED, not the dossier's canonical owned-object names.

### 5.2 Cross-cutting object families this sublane cites (merged)

| Cited object family | Owner | Default tier (PROPOSED, ADR-S-05) | Citation |
|---|---|---|---|
| `EvidenceBundle` | ENCY doctrine (cross-cutting) | mirrors claim tier | `[ENCY]` |
| `SourceDescriptor` | source steward (cross-cutting) | varies | `[ENCY]` |
| `ArchaeologicalSite` | Archaeology / Cultural Heritage | **deny-default site coords** | `[DOM-ARCH]` |
| `Settlement` / `Municipality` / `GhostTown` | Settlements / Infrastructure | T0 | `[DOM-SETTLE]` |
| `CulturalTemporalPeriod` | Archaeology / Cultural Heritage | T0 | `[DOM-ARCH]` |

### 5.3 Trade-route object topology (PROPOSED, merged)

```mermaid
flowchart TD
  subgraph SRC["Source families (SourceDescriptor-bearing)"]
    HIST["Historic atlases and survey maps"]
    GNIS["GNIS names"]
    OSM["OpenStreetMap (historic tags, context only)"]
    ARCH["Archaeology (cited context only)"]
    ETHNO["Ethnohistoric / oral (steward review)"]
  end
  subgraph OBJ["Trade-route objects (Roads/Rail-owned)"]
    HRC["Historic RouteClaim"]
    TRC["TradeRouteCorridor"]
    RM["RouteMembership"]
    RS["Road Segment (historic alignment)"]
    MSN["Movement Story Node"]
  end
  subgraph GATE["Governed transitions"]
    POL["PolicyDecision + ReviewRecord + RedactionReceipt"]
    REL["ReleaseManifest"]
  end
  subgraph PUB["Public surface (governed API only)"]
    GEN["Generalized TradeRouteCorridor"]
    EVD["Evidence Drawer"]
    FOC["Focus Mode (governed AI)"]
  end
  HIST --> HRC
  GNIS --> HRC
  OSM -. "context only" .-> HRC
  ARCH -. "cited context" .-> HRC
  ETHNO -. "steward review" .-> HRC
  HRC --> RM
  TRC --> RM
  RS --> RM
  HRC --> POL
  TRC --> POL
  MSN --> POL
  POL --> REL
  REL --> GEN
  REL --> EVD
  EVD --> FOC
```

The diagram reflects the doctrinal flow in Atlas Ch. 13 §B, §F, §H, §I and the crosswalk in §24.5 / §24.13; repo files, route names, and DTOs are NEEDS VERIFICATION.

<details>
<summary><strong>PROPOSED Historic RouteClaim object shape — illustrative only</strong></summary>

The block below is **illustrative**, not a contract. The canonical shape lives in `schemas/contracts/v1/...` per ADR-0001; the slug (`domains/roads-rail-trade/` per Directory Rules §12 vs. `transport/` per Atlas §24.13) is itself an open question — see [§13 OPEN-TRADE-03](#13-open-questions-and-verification-backlog). Do not use this shape to validate anything.

```jsonc
// PROPOSED — illustrative historic_route_claim object shape. Not a contract. Not a schema.
{
  "object_kind": "HistoricRouteClaim",
  "identity": {
    "source_id": "<source descriptor id>",
    "object_role": "HistoricRouteClaim",
    "temporal_scope": { "valid_from": "...", "valid_to": "..." },
    "normalized_digest": "<JCS+SHA-256 of canonical attributes>"
  },
  "asserted_geometry": {
    // PUBLIC GEOMETRY DEFAULTS TO GENERALIZED — exact line withheld pending review
    "public_representation": "generalized",
    "uncertainty": "<RouteUncertaintyProfile ref — PROPOSED>"
  },
  "times": {
    "source_time": "...", "observed_time": "...",
    "valid_time": { "from": "...", "to": "..." },
    "retrieval_time": "...", "release_time": "...", "correction_time": null
  },
  "source": {
    "source_descriptor_ref": "<...>",
    "source_role": "claim | interpretive | administrative | context",  // fixed at admission
    "rights_label": "<NEEDS VERIFICATION>"
  },
  "cultural_governance_ref": "<[DOM-ARCH] steward review / sensitivity record — required when cultural>",
  "evidence_ref": "<resolves to EvidenceBundle when released>",
  "policy": { "release_state": "...", "sensitivity_tier": "<steward-set>" },
  "redaction_receipt_ref": "<RedactionReceipt when generalized/redacted>"
}
```

</details>

[↑ back to top](#trade-routes--historic-alignments-sublane--roads-rail-and-trade-routes-domain)

---

## 6. Lifecycle — RAW → PUBLISHED

CONFIRMED doctrine / PROPOSED lane application: this sublane inherits the `[DIRRULES]` lifecycle invariant in full. **Promotion is a governed state transition, not a file move.** For historic/cultural evidence, the WORK/QUARANTINE gate carries an **added steward-review obligation** before any candidate becomes public-safe. `[DIRRULES]` `[DOM-ROADS]` `[ENCY]`

```mermaid
flowchart LR
  RAW["RAW — SourceDescriptor exists"]
  WORKQ["WORK / QUARANTINE — normalize + STEWARD REVIEW for cultural/historic"]
  PROC["PROCESSED — EvidenceRef, ValidationReport, generalized public candidate"]
  CATTR["CATALOG / TRIPLET — EvidenceBundles, derived projections"]
  PUB["PUBLISHED — ReleaseManifest, correction path, rollback target"]
  RAW --> WORKQ
  WORKQ -->|"review pass + gate pass"| PROC
  WORKQ -. "uncertain / unreviewed → quarantine reason recorded" .-> WORKQ
  PROC --> CATTR --> PUB
  classDef gov fill:#fff4e6,stroke:#d9480f,color:#3b1a05;
  class RAW,WORKQ,PROC,CATTR,PUB gov;
```

| Stage | Handling (CONFIRMED from `[DOM-ROADS]` §H, sensitivity-adjusted) | Gate | Status |
|---|---|---|---|
| **RAW** | Capture immutable source payload or reference with source role, rights, sensitivity, citation, time, and hash. | SourceDescriptor exists. | PROPOSED |
| **WORK / QUARANTINE** | Normalize schema, geometry, time, identity, evidence, rights, policy; **route cultural/historic material to steward review**; hold failures and unreviewed cultural claims. | Validation + policy gate pass **and** steward review where cultural, **or** quarantine reason recorded. | PROPOSED |
| **PROCESSED** | Emit validated normalized objects, receipts, and **generalized** public-safe candidates with `RedactionReceipt` where geometry is transformed. | EvidenceRef, ValidationReport, digest closure exist. | PROPOSED |
| **CATALOG / TRIPLET** | Emit catalog records, EvidenceBundles, derived projections, release candidates. | Catalog / proof closure passes. | PROPOSED |
| **PUBLISHED** | Serve released public-safe (generalized) historic/corridor artifacts through governed APIs and manifests. | ReleaseManifest, correction path, rollback target, review/policy state exist. | PROPOSED |

> [!IMPORTANT]
> **Watcher-as-non-publisher applies.** A worker that ingests an archival or gazetteer source emits receipts and candidate decisions; it does not write to `data/catalog/` or `data/published/`, and it cannot move a cultural-corridor claim past PROCESSED without the steward-review and policy gates. `[DIRRULES]`

### 6.1 Trade-route-specific stage handling (PROPOSED, merged from `trade_routes.md` §6)

| Stage | Additional trade-route handling |
|---|---|
| **RAW** | Payloads include historic atlas scans, ethnohistorical excerpts, and GNIS rows. Indigenous-corridor evidence enters with the steward-review flag already set. |
| **WORK / QUARANTINE** | Assign canonical corridor name, period of attestation, uncertainty bound, and alignment-evidence type. Quarantine with a recorded reason any legal-status assertion sourced only from OSM tags. |
| **PROCESSED** | Emit validated `Historic RouteClaim` objects, `TradeRouteCorridor` candidates, `RouteMembership` proposals, receipts, and public-safe candidate geometry. *Historic and modern carriers stay separate.* `[UNIFIED — PROPOSED]` |
| **CATALOG / TRIPLET** | Graph / triplet projections and graph-derived corridors are labelled **derived**, never canonical. `[DOM-ROADS]` `[ENCY]` |
| **PUBLISHED** | Released artifacts are generalized `TradeRouteCorridor` polylines, narrative `Movement Story Node`s, and Evidence Drawer payloads. |

> [!WARNING]
> **No back-channel publishing.** Public clients reach trade-route data only through the governed API. The browser renderer — `packages/maplibre-runtime/`, the **sole governed renderer** (v1.3; Cesium retired) — consumes the same `EvidenceBundle` and `DecisionEnvelope` as any other client; it is **not** a parallel truth path. `[DIRRULES §11]`

[↑ back to top](#trade-routes--historic-alignments-sublane--roads-rail-and-trade-routes-domain)

---

## 7. Sensitivity, rights, and publication posture

> [!CAUTION]
> **Sensitivity-first is the default for this sublane.** `[DOM-ROADS]` §I `[DOM-ARCH]` `[ENCY]`
> - **Indigenous trade and mobility corridors, oral history, treaty, cultural, and interpretive evidence default to steward review and generalized public geometry.**
> - **Historic / cultural routes are generalized unless reviewed evidence supports precision; graph projections are derived only.** (`[DOM-ROADS via UNIFIED]`)
> - **Exact archaeological site coordinates are denied by default** and are never absorbed into a route claim. `[DOM-ARCH]`
> - Cultural truth and the sensitivity tier are **owned by `[DOM-ARCH]`** and any rights-holder representative — not set here.

Default disposition when no specific row matches (operating contract §23.2 — most-restrictive applicable row governs):

```text
DENY public exact exposure
GENERALIZE before publication
REDACT when needed (RedactionReceipt)
QUARANTINE uncertain or unreviewed cultural source material
REQUIRE steward review (and rights-holder review where applicable)
ABSTAIN when support is inadequate
```

**CONFIRMED doctrine:** unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state **blocks public promotion**. `[ENCY]` `[DIRRULES]`

> [!IMPORTANT]
> Each cultural/historic entry MUST link to its `[DOM-ARCH]`-governed sensitivity record and, where geometry is transformed, its `RedactionReceipt`. If that record is missing, surface the gap and ABSTAIN rather than publishing. Link target is `TODO` / `NEEDS VERIFICATION`.

CONFIRMED doctrine (merged) — *critical transport facilities require review.* `[DOM-ROADS]` `[ENCY]`

> [!IMPORTANT]
> **The T0–T4 tier scheme in §7.1–§7.3 is PROPOSED, pending ADR-S-05.** Atlas §24.5.1 labels the scheme PROPOSED and ADR-S-05 ("adopt as canonical or revise") is open. The tables describe **proposed motion**, not adopted doctrine. The *underlying postures* they encode (steward review + generalized geometry for Indigenous corridors; deny-default site coords; cite-or-abstain) are CONFIRMED; the *tier labels and transition artifacts* are PROPOSED. `[ENCY §24.5.1]`

### 7.1 Default tier by trade-route claim class (PROPOSED, merged from `trade_routes.md` §7.1)

Per Atlas §24.5 (Master Sensitivity / Rights Tier Reference, PROPOSED):

| Claim class | Default tier | Allowed transforms (PROPOSED) | Required gates |
|---|---|---|---|
| Generic historic trail with broad public attestation (e.g., a named national historic trail) | **T1** | Generalize alignment to corridor (cell size pending the redaction-determinism profile); record `RedactionReceipt`. | `RedactionReceipt` + `ReviewRecord` |
| Indigenous trade / mobility corridor, sourced from steward-governed material | **T4** | Steward + sovereignty review → generalize → `RedactionReceipt` → demote to **T2** (reviewer-only) or **T1** (generalized public). No transform releases to **T0**. | Sovereignty review + `ReviewRecord` + `PolicyDecision` |
| Uncertain historic alignment (single-source, contested, low-precision) | **T2** | Reviewer-only until corroborating evidence or steward sign-off; generalization may later move to **T1**. | `ReviewRecord` + uncertainty label |
| `Movement Story Node` referencing a living-person account, oral-history participant, or culturally sensitive narrator | **T4** | De-identification + consent + `RedactionReceipt` → **T2**; aggregation may permit **T1**. Crosses into People / DNA / Land posture if living-person fields are present. | Consent + `ReviewRecord` + `PolicyDecision` `[DOM-PEOPLE]` |
| Modern freight-corridor cross-citation to a historic corridor | **T0–T1** | Freight footprint at parent-domain default; historic context carried as generalized cross-citation. | Per parent-domain release manifest |

### 7.2 Tier-transition motion (PROPOSED, per Atlas §24.5.3)

| From → To | Required artifact | Required reviewer | Reversibility |
|---|---|---|---|
| **T4 → T3** | `PolicyDecision` + `ReviewRecord` + named agreement | Steward + rights-holder where applicable | Reversible: agreement revocation returns to **T4** with `CorrectionNotice` |
| **T4 → T2** | `PolicyDecision` + `ReviewRecord` | Steward | Reversible: review revocation returns to **T4** |
| **T4 → T1** | `RedactionReceipt` + `ReviewRecord` | Steward | Reversible: redaction can be re-evaluated; a published **T1** can be demoted to **T4** by correction |
| **T2 → T1** | `RedactionReceipt` + `ReviewRecord` | Steward | Reversible |
| **T1 → T0** | `ReleaseManifest` + `ReviewRecord` | Steward + release authority | Reversible via `RollbackCard` |

> [!CAUTION]
> **Never publish exact archaeological coordinates that intersect a trade-route alignment.** Atlas Ch. 13 §F: historical corridor reconstructions are cited as context only; exact archaeological coordinates are denied. Archaeology owns the site, Roads / Rail cites the context, and the published corridor must be generalized enough that it does not become a forensic locator. `[DOM-ROADS]` `[DOM-ARCH]` `[ENCY]`

### 7.3 Tier transitions diagram (PROPOSED motion, ADR-S-05)

```mermaid
stateDiagram-v2
    [*] --> T4_Denied : Indigenous corridor / steward-flagged
    [*] --> T2_Reviewer : uncertain alignment, single source
    [*] --> T1_Generalized : public-attestation, generic historic trail
    T4_Denied --> T3_Restricted : PolicyDecision + ReviewRecord + named agreement
    T4_Denied --> T2_Reviewer : PolicyDecision + ReviewRecord
    T4_Denied --> T1_Generalized : RedactionReceipt + ReviewRecord
    T3_Restricted --> T2_Reviewer : PolicyDecision + ReviewRecord
    T2_Reviewer --> T1_Generalized : RedactionReceipt + ReviewRecord
    T1_Generalized --> T0_Open : ReleaseManifest + ReviewRecord (rare for trade routes)
    T0_Open --> T1_Generalized : Correction (demote)
    T1_Generalized --> T4_Denied : Correction (full deny)
    T2_Reviewer --> T4_Denied : Review revocation
```

### 7.4 Publication, correction, and rollback (merged from `trade_routes.md` §13)

CONFIRMED doctrine / PROPOSED implementation — publication requires `ReleaseManifest`, `EvidenceBundle`, validation / policy support, review state where required, correction path, stale-state rule, and rollback target. Atlas Appendix E governs supersession. `[ENCY Appendix E]` `[DOM-ROADS]`

| Lifecycle moment | Required artefact | Notes |
|---|---|---|
| Release of a `TradeRouteCorridor` polyline | `ReleaseManifest` + `EvidenceBundle` + `RedactionReceipt` + `ReviewRecord` | Indigenous-corridor cases additionally require a sovereignty `PolicyDecision`. |
| Correction of an alignment claim | `CorrectionNotice` (Atlas Appendix E) | Demotion to a more-restrictive tier is reversible per §24.5.3 (PROPOSED). |
| Stale historic source (e.g., superseded atlas edition) | Stale-state flag on the source descriptor | Published derivative continues to serve under a stale label until the next promotion cycle. |
| Rollback of a published corridor | `RollbackCard` referencing the prior `ReleaseManifest` | Graph projections derived from the rolled-back release roll back together (see §9 graph-rollback test). |

[↑ back to top](#trade-routes--historic-alignments-sublane--roads-rail-and-trade-routes-domain)

---

## 8. API, contract, and schema surfaces

PROPOSED governed surfaces from `[DOM-ROADS]` §J; exact routes, DTO field shapes, and schema slugs remain **UNKNOWN** until mounted-repo verification.

| Endpoint or artifact | DTO / schema | Finite outcomes | Status |
|---|---|---|---|
| Trade-routes feature / detail resolver — route `TBD` | `RoadsRailDecisionEnvelope` (parent-domain envelope; sublane partition TBD) | `ANSWER / ABSTAIN / DENY / ERROR` | PROPOSED; exact route UNKNOWN. `[DOM-ROADS]` |
| Historic-route claim layer manifest resolver | `LayerManifest` / domain layer descriptor (generalized geometry) | `ANSWER / DENY / ERROR` | PROPOSED; public-safe (generalized) release only. `[DOM-ROADS]` |
| Trade-routes Evidence Drawer payload | `EvidenceDrawerPayload` + `EvidenceBundle` projection | `ANSWER / ABSTAIN / DENY / ERROR` | PROPOSED; evidence + policy + sensitivity filtered. `[DOM-ROADS]` `[GAI]` |
| Trade-routes Focus Mode answer | `RuntimeResponseEnvelope` + `AIReceipt` | `ANSWER / ABSTAIN / DENY / ERROR` | PROPOSED; AI never root truth; DENY on unreviewed cultural detail. `[GAI]` |
| Schema responsibility root | `schemas/contracts/v1/...` per ADR-0001 | finite validator outcomes | PROPOSED; **slug variance** `domains/roads-rail-trade/` vs `transport/` — see §13. `[DIRRULES]` |
| Contracts (meaning) *(merged)* | `contracts/transport/` per the merged draft, vs `contracts/domains/roads-rail-trade/` where current drafts sit | n/a | PROPOSED; CONFLICTED — OPEN-TRADE-03 |
| Policy (admissibility) *(merged)* | `policy/domains/roads-rail-trade/` (PROPOSED per Directory Rules §12) | `ALLOW / DENY / RESTRICT / ABSTAIN` | PROPOSED |

<details>
<summary><strong>Illustrative TradeRouteCorridor response envelope (PROPOSED — not a contract; merged)</strong></summary>

```jsonc
// PROPOSED illustrative shape. Not a binding contract.
// Authoritative shape lives under schemas/contracts/v1/ (slug CONFLICTED — OPEN-TRADE-03).
{
  "outcome": "ANSWER",
  "claim": {
    "type": "TradeRouteCorridor",
    "name": "<canonical corridor name>",
    "alignment_evidence": [
      { "kind": "Historic RouteClaim", "evidence_ref": "kfm://evidence/..." }
    ],
    "temporal_scope": { "valid_from": "YYYY-MM-DD", "valid_to": "YYYY-MM-DD" },
    "geometry": {
      "type": "LineString",
      "generalization": { "method": "TODO", "cell_m": null }
    },
    "tier": "T1",
    "uncertainty": { "alignment": "TODO", "period": "TODO" }
  },
  "evidence_bundle": "kfm://evidence/bundle/...",
  "policy_decision": "kfm://policy/decision/...",
  "release_manifest": "kfm://release/manifest/...",
  "receipts": ["kfm://receipt/redaction/..."]
}
```

</details>

> [!NOTE]
> **Public clients use governed APIs, not canonical stores.** `[DIRRULES]` `[ENCY]` Map shells, dashboards, and AI surfaces consume `apps/governed-api/` responses; they do not read `data/processed/`, `data/catalog/`, or `data/published/` directly — and they receive **generalized** historic/cultural geometry, never the raw asserted line.

[↑ back to top](#trade-routes--historic-alignments-sublane--roads-rail-and-trade-routes-domain)

---

## 9. Validators, tests, fixtures

PROPOSED test obligations from `[DOM-ROADS]` §K, with sublane-relevant emphasis. None CONFIRMED present in a mounted repo this session; all tracked in §13.

| # | Test obligation | Sublane relevance | Status |
|---|---|---|---|
| 1 | Route membership and designation separation tests. | Medium — corridor / membership / claim kept distinct. | PROPOSED `[DOM-ROADS]` `[ENCY]` |
| 2 | Operator / status temporal tests. | Low — historic corridors rarely carry modern operator status. | PROPOSED `[DOM-ROADS]` `[ENCY]` |
| 3 | OSM / GNIS legal-status denial. | High — community / gazetteer sources cannot establish corridor legitimacy. | PROPOSED `[DOM-ROADS]` `[ENCY]` |
| 4 | **Historic overprecision denial.** | **Highest — the defining test of this sublane.** No false precision on historic/cultural alignments. | PROPOSED `[DOM-ROADS]` `[ENCY]` |
| 5 | Public generalization receipt tests. | **Highest — every public-safe geometry transform emits a `RedactionReceipt`.** | PROPOSED `[DOM-ROADS]` `[ENCY]` |
| 6 | Transport graph projection rollback tests. | Medium — derived projections roll back cleanly when a claim is corrected. | PROPOSED `[DOM-ROADS]` `[ENCY]` |
| 7 | **Steward-review-required denial (PROPOSED, sublane-specific).** | Cultural/Indigenous claims cannot reach PUBLISHED without a `[DOM-ARCH]` review record. | PROPOSED `[DOM-ARCH]` `[ENCY]` |

> [!TIP]
> **Fixture-first, no-network.** The first slice of test infrastructure is fixture-first and offline: source descriptors, deterministic identity, validators, deny policies, no-network fixtures, and proof-pack / promotion fixtures **before** any live source is activated. Negative fixtures (exact cultural geometry, unreviewed claim, missing sensitivity record) are required, not optional. `[UNIFIED]`

### 9.1 Test details (merged from `trade_routes.md` §11)

- **Route membership and designation separation.** A `RouteMembership` MUST NOT collapse a corridor's named designation with the underlying segment's administrative status. `[DOM-ROADS]`
- **Historic overprecision denial.** Released historic alignments MUST carry generalization metadata; alignments with precision tighter than the configured threshold are denied at the promotion gate. `[DOM-ROADS]`
- **OSM / GNIS legal-status denial.** Legal status (e.g., "national historic trail") MUST NOT be asserted from OSM tags or GNIS rows alone; an authority-role source is required. `[DOM-ROADS]`
- **Operator / status temporal tests.** Operator and status assertions MUST preserve source, observed, valid, retrieval, release, and correction times distinctly. `[DOM-ROADS]` `[ENCY]`
- **Public generalization receipt tests.** Every published corridor MUST resolve to a `RedactionReceipt` recording the generalization method, cell size or radius, and seed (if jittered). The seeded-jitter determinism rule's home is [`docs/standards/REDACTION_DETERMINISM.md`](../../../standards/REDACTION_DETERMINISM.md) (the merged draft called it "not yet authored"; the file now exists — content alignment NEEDS VERIFICATION).
- **Transport graph projection rollback.** A derived graph projection that loses its underlying corridor evidence MUST be rolled back, not patched in place. `[DOM-ROADS]`

> [!TIP]
> **Fixtures live close to the proof, not the schema.** Per Directory Rules §6.6 you MAY keep trade-route fixtures under `tests/fixtures/` or `fixtures/`, but you MUST NOT maintain two competing fixture homes for the same artefact. `[DIRRULES]`

[↑ back to top](#trade-routes--historic-alignments-sublane--roads-rail-and-trade-routes-domain)

---

## 10. Governed AI behavior

CONFIRMED doctrine / PROPOSED implementation. `[GAI]` `[DOM-ROADS]` `[ENCY]`

- AI **may** summarize released (generalized) trade-route / historic EvidenceBundles, compare evidence, explain limitations and uncertainty, and draft steward-review notes.
- AI **MUST `ABSTAIN`** when evidence is insufficient (missing EvidenceBundle, missing release state, conflicting claims without resolution).
- AI **MUST `DENY`** where policy, rights, sensitivity, or release state blocks the request — including **any request for exact historic/Indigenous/cultural-corridor geometry that lacks a `[DOM-ARCH]` review record**, or any request to locate sensitive cultural features precisely.
- AI **MUST NOT** answer from RAW / WORK / QUARANTINE stores, and MUST NOT treat a Historic RouteClaim as established fact. The trust-membrane rule from `[ENCY]` applies in full.
- Every Focus Mode answer carries an `AIReceipt`. `[GAI]`

### 10.1 Example requests and expected outcomes (merged from `trade_routes.md` §12)

| Trade-route AI request | Expected behaviour |
|---|---|
| "Summarize the published evidence for the corridor named X" | **ANSWER** with citations to the resolved `EvidenceBundle`; uncertainty surfaced. |
| "Where exactly does the Indigenous mobility corridor Y run?" | **DENY** when corridor Y is at a deny-default tier; **ABSTAIN** when published evidence is generalized and the question demands precision the published tier cannot supply. |
| "Was operator O assigned to corridor X in 1873?" | **ANSWER** if operator evidence supports it with distinct observed and valid times; otherwise **ABSTAIN**. |
| "Compose a story node connecting living-person account L to corridor X" | **DENY** unless consent + `ReviewRecord` + `PolicyDecision` satisfy the People / Land posture. `[DOM-PEOPLE]` |
| "Show me the underlying RAW source rows" | **DENY** — the AI surface never touches RAW / WORK. `[GAI]` |

[↑ back to top](#trade-routes--historic-alignments-sublane--roads-rail-and-trade-routes-domain)

---

## 11. Cross-lane and cross-sublane relations

### 11.1 Cross-lane edges this sublane participates in

CONFIRMED / PROPOSED (`[DOM-ROADS]` §F): every relation must preserve ownership, source role, sensitivity, and EvidenceBundle support.

| This sublane | Related lane | Relation | Constraint |
|---|---|---|---|
| Trade routes | `archaeology` / cultural heritage | Historic routes, Indigenous corridors, forts, missions. | **Cultural truth and sensitivity policy are owned by `[DOM-ARCH]`.** Default to generalized public geometry; exact site coords denied. |
| Trade routes | `settlements-infrastructure` | Forts, missions, townsites as place objects along a corridor. | Settlement / place identity stays with `settlements-infrastructure`; this sublane carries the corridor relation. |
| Trade routes | `hydrology` | Fords / river crossings on a historic corridor. | Water evidence stays with `hydrology`; this sublane owns the corridor-claim side. |
| Trade routes | `people-dna-land` | A corridor crossing private land or tied to land tenure. | Living-person, parcel, and ownership facts stay with `people-dna-land`. |
| Trade routes | `hazards` | Historic disaster/closure context on a corridor; closure, detour, flood / fire / smoke exposure along corridors. | Hazard truth stays with `hazards`; KFM is never an alert authority. `[DOM-HAZ]` |
| Trade routes *(merged)* | Frontier Matrix | Generalized access observations bound the access cells of the matrix. | Frontier Matrix is composition, not authority. `[DOM-ROADS]` `[UNIFIED]` |
| Trade routes *(merged)* | Planetary / 3D / Digital Twin | Corridor or fly-over scenes use the *same* `EvidenceBundle` / `DecisionEnvelope`. | 3D is an alternate renderer (`packages/maplibre-runtime/` + governed plugins), never an alternate truth path. `[DIRRULES §11]` |

Settlement-side context along corridors (merged detail): depots, stations, ferry-landings, and ghost-town anchors — identity is **settlement-owned**. `[DOM-SETTLE]`

### 11.2 Cross-sublane edges (PROPOSED, internal to `roads-rail-trade`)

| This sublane | Sibling sublane | Relation | Constraint |
|---|---|---|---|
| Trade routes | Roads | A modern Road Segment overlying a Historic RouteClaim or TradeRouteCorridor. | The historic claim **retains its sensitivity posture**; the modern segment does not absorb or override it. |
| Trade routes | Rail | A historic rail alignment interacting with a pre-rail trade corridor. | Two object families; uncertainty and sensitivity discipline preserved on both sides. |

[↑ back to top](#trade-routes--historic-alignments-sublane--roads-rail-and-trade-routes-domain)

---

## 12. Map and viewing products

PROPOSED viewing products from `[DOM-ROADS]` §G, narrowed to this sublane:

- Historic route claim view (with **uncertainty surface**, generalized geometry).
- Generalized trade-route corridor layer.
- Movement-story narrative view.
- Derived graph / connectivity view (historic-mode projection, clearly labeled derived).

CONFIRMED cross-cutting viewing products that apply to every released layer: **Evidence Drawer**, time-aware state, **trust badges**, **sensitivity-redacted view**, correction / stale-state view, and **governed Focus Mode**. `[MAP-MASTER]` `[GAI]`

### 12.1 Product tiers (PROPOSED, merged from `trade_routes.md` §9)

| Product | Role in this sublane | Tier / posture (PROPOSED) |
|---|---|---|
| Historic-route-claim view | Per-claim presentation of `Historic RouteClaim`, with EvidenceBundle resolution and uncertainty surface | T1 default (generalized); T2 for contested / single-source alignments |
| Generalized trade-route corridor | Public-safe `TradeRouteCorridor` polyline / band — generalization is governed, not stylistic | T1 default; T4 for Indigenous / steward-flagged corridors until review |
| Derived graph / connectivity view | Network projection across corridor membership; *labelled derived*, never canonical | T1; rollback test required (§9) |
| Evidence Drawer | Per-claim citation surface; stale / uncertainty badges; public-safe redaction visibility | Cross-cutting `[MAP-MASTER]` `[GAI]` |
| Focus Mode | Bounded-scope governed AI over released trade-route bundles only; ABSTAIN / DENY behaviour | Cross-cutting `[GAI]` |
| Movement Story Node renderer | Narrative anchor with abstain template when EvidenceBundle / spec_hash / redaction receipt is missing | T1–T2 depending on narrator status |

> [!NOTE]
> **MapLibre tile shape (illustrative).** The Master MapLibre catalog records `ML-G-046` (canonical historic-trail LineString shape), `ML-H-031` (historic-trail vector tile generation), and `ML-Y-077` (historic-trail overlay thin slice) as EXPANDED ideas — illustrative of how a corridor would be tiled (vector PMTiles per epoch, precision-gated), **not** a claim that such tiles exist in the repo. `[MAP-MASTER]`

> [!IMPORTANT]
> **The map renderer is not the truth path, and styling cannot imply precision.** Per `[MAP-MASTER]` / `[DIRRULES]` §11, the browser renderer consumes the same EvidenceBundle and DecisionEnvelope as any other client — it is an alternate renderer, not an alternate truth path. A historic-corridor layer whose styling implies a precise alignment that no reviewed EvidenceBundle supports is a trust-membrane bug, not a styling choice.

> [!NOTE]
> **Renderer note (v1.3).** `packages/maplibre-runtime/` is the **sole governed browser-side renderer adapter**; the v1.2 Cesium dual-renderer posture is **retired** (doctrine-target, pending the *MapLibre as Sole Browser-Side Renderer; Retire Cesium Dependency* ADR — Directory Rules §18.e OPEN-DR-10). The freeze rule is in effect: no new `cesium*` code, schemas, policies, or tests. `[DIRRULES]` `[MAP-MASTER]`

[↑ back to top](#trade-routes--historic-alignments-sublane--roads-rail-and-trade-routes-domain)

---

## 13. Open questions and verification backlog

Tracked here for triage; resolutions migrate to `docs/registers/VERIFICATION_BACKLOG.md`, `docs/registers/DRIFT_REGISTER.md`, or `docs/adr/` as appropriate.

### 13.1 Sublane-structure questions (ADR-class or per-root README class)

| ID | Question | Evidence that would settle it | Status |
|---|---|---|---|
| **OPEN-TRADE-01** | Is `docs/domains/<domain>/sublanes/` a recognized organizational pattern — and is "sublane" the right term, given it collides with the Focus Mode "sub-lane" (§6.7)? | Updated Directory Rules §6.1, parent dossier README, or a small ADR. | CONFLICTED — needs ADR or per-root README. `[DIRRULES]` |
| **OPEN-TRADE-02** | Is this file `trade-routes.md`, `historic-routes.md`, or `routes-historic.md`? | Parent dossier README and ADR alignment. | UNKNOWN — naming PROPOSED. |
| **OPEN-TRADE-03** | Schema-home slug: `schemas/contracts/v1/domains/roads-rail-trade/` (Directory Rules §12) vs. `schemas/contracts/v1/transport/` (Atlas §24.13)? | ADR aligning Atlas §24.13 and Directory Rules §12; `DRIFT_REGISTER.md` entry. | CONFLICTED — slug variance between two project docs. `[DIRRULES §12]` `[ENCY §24.13]` |

### 13.2 Source-and-policy questions (carried from `[DOM-ROADS]` §N, sensitivity-weighted)

| Item to verify | Evidence that would settle it | Status |
|---|---|---|
| **Indigenous / cultural corridor policy enforcement** (the central question for this sublane). | Mounted-repo `policy/sensitivity/` + `[DOM-ARCH]` review records; steward-review-required denial test. | NEEDS VERIFICATION |
| `RouteUncertaintyProfile` (or equivalent) for historic claims. | Mounted-repo schema, validator, emitted receipts. | NEEDS VERIFICATION |
| Generalization/redaction determinism for public corridor geometry. | Mounted-repo `RedactionReceipt` schema + generalization-receipt tests. | NEEDS VERIFICATION |
| Cultural-heritage / archival / oral-history source terms and rights-holder permissions. | Mounted-repo source descriptors + `[DOM-ARCH]` governance records. | NEEDS VERIFICATION |
| Transport graph projection and MapLibre integration (historic-mode). | Mounted-repo pipeline output, layer manifest, rollback drill receipts. | NEEDS VERIFICATION |

### 13.3 Implementation-maturity questions (this session is docs-only)

| Item | Status |
|---|---|
| Whether any of `contracts/domains/roads-rail-trade/`, `schemas/contracts/v1/domains/roads-rail-trade/` (or `…/transport/`), `policy/domains/roads-rail-trade/`, `tests/domains/roads-rail-trade/`, `pipelines/domains/roads-rail-trade/`, or `data/<phase>/roads-rail-trade/` exist in the mounted repo. | UNKNOWN — no mounted repo this session. |
| Exact route names, DTO field names, and validator commands. | UNKNOWN. |
| CI / workflow coverage of the §9 tests (esp. historic-overprecision and steward-review-required). | UNKNOWN. |

### 13.4 Questions merged from `trade_routes.md` (original IDs kept)

| ID | Item | What would settle it | Status |
|---|---|---|---|
| **OQ-TR-01** | `sublanes/` convention + "sublane" term — same as OPEN-TRADE-01. | ADR or amendment to `docs/doctrine/directory-rules.md` §6.1 | CONFLICTED (duplicate of OPEN-TRADE-01) |
| **OQ-TR-02** | Generalization profile (cell size, radius, jitter seed rule) for published corridors. | `docs/standards/REDACTION_DETERMINISM.md` per-profile entry | NEEDS VERIFICATION |
| **OQ-TR-03** | Schema home for `TradeRouteCorridor`, `Historic RouteClaim`, `RouteMembership`. | Repo evidence under the resolved schema slug + valid/invalid fixtures | UNKNOWN |
| **OQ-TR-04** | Indigenous-corridor steward-review workflow (sovereignty + rights-holder + reviewer roles). | `policy/domains/roads-rail-trade/` rules + workflow doc + signed `ReviewRecord` template | NEEDS VERIFICATION |
| **OQ-TR-05** | Historic-source rights and current terms for each §4 row. | `SourceDescriptor` entries with rights review | NEEDS VERIFICATION |
| **OQ-TR-06** | Anchor stability of `Movement Story Node` across Atlas v1.0 → v1.1. | Confirm against `docs/atlases/` and Appendix G | NEEDS VERIFICATION |
| **OQ-TR-07** | Filename: `trade-routes.md` vs `trade.md` (modern-freight sibling) vs legacy `trade_routes.md`. | Parent dossier README + ADR; `DRIFT_REGISTER.md` entry | PARTLY RESOLVED 2026-10-12 — `trade_routes.md` is now a redirect stub to this file; `trade.md` split (OPEN-TRADE-A1) still open |
| **OQ-TR-08** | Schema/contract slug `transport/` vs `domains/roads-rail-trade/` — same as OPEN-TRADE-03. | ADR aligning the two project docs | CONFLICTED (duplicate of OPEN-TRADE-03) |
| **OQ-TR-09** | Tier scheme T0–T4 adoption (§7.1–§7.3). | ADR-S-05 acceptance | NEEDS VERIFICATION |
| **OQ-TR-10** | Final repo placement of this document. | Repo inspection + OPEN-TRADE-01/02 resolution | NEEDS VERIFICATION |

> [!NOTE]
> **Merge conflict recorded (2026-10-12).** The two drafts differed on the schema/contract slug: this file treats `domains/roads-rail-trade/` vs `transport/` as an unresolved variance, while `trade_routes.md` (and the parent README's v1.1 correction note) leaned to `transport/` for schemas and contracts. Both are kept; OPEN-TRADE-03 remains CONFLICTED. The two drafts also used different policy labels (`public (sublane scaffold) …` here vs `public`); this file's more restrictive label is kept.

[↑ back to top](#trade-routes--historic-alignments-sublane--roads-rail-and-trade-routes-domain)

---

## 14. Related docs

- Parent dossier: [`docs/domains/roads-rail-trade/README.md`](../README.md) — `PROPOSED` link; verify on mount.
- Sublane index (PROPOSED): [`docs/domains/roads-rail-trade/sublanes/README.md`](./README.md)
- Sibling sublane: [`docs/domains/roads-rail-trade/sublanes/roads.md`](./roads.md)
- Sibling sublane: [`docs/domains/roads-rail-trade/sublanes/rail.md`](./rail.md)
- **Cultural authority:** [`docs/domains/archaeology/README.md`](../../archaeology/README.md) — owner of cultural / Indigenous corridor truth and sensitivity policy.
- [`docs/domains/people-dna-land/README.md`](../../people-dna-land/README.md) — land tenure / private-land authority.
- Doctrine: [`docs/doctrine/directory-rules.md`](../../../doctrine/directory-rules.md) — Domain Placement Law (§12), lifecycle invariant.
- Architecture: [`docs/architecture/governed-api/README.md`](../../../architecture/governed-api/README.md) — trust-membrane definition.
- ADR: [`docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md`](../../../adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) — schema-home rule.
- Registers: `docs/registers/VERIFICATION_BACKLOG.md`, `docs/registers/DRIFT_REGISTER.md` — destinations for §13 items, including the OPEN-TRADE-03 slug conflict.
- Atlas §24.13 — Responsibility-root crosswalk (source of the `transport` slug variance).
- Sibling sublane (modern freight): [`docs/domains/roads-rail-trade/sublanes/trade.md`](./trade.md) — see OQ-TR-07 / OPEN-TRADE-A1.
- Redirect stub: [`docs/domains/roads-rail-trade/sublanes/trade_routes.md`](./trade_routes.md) — former underscore twin, merged here 2026-10-12.
- [`docs/domains/settlements-infrastructure/README.md`](../../settlements-infrastructure/README.md) — facility / settlement identity.
- Doctrine: [`docs/doctrine/lifecycle-law.md`](../../../doctrine/lifecycle-law.md) — RAW → PUBLISHED lifecycle law; [`docs/doctrine/trust-membrane.md`](../../../doctrine/trust-membrane.md) — governed API boundary.
- Standards: [`docs/standards/PROV.md`](../../../standards/PROV.md) — provenance (W3C PROV-O mapping); [`docs/standards/REDACTION_DETERMINISM.md`](../../../standards/REDACTION_DETERMINISM.md) — redaction determinism; [`docs/standards/SENSITIVITY_RUBRIC.md`](../../../standards/SENSITIVITY_RUBRIC.md) — sensitivity rubric.

<sub>**Citation short-codes** — [DOM-ROADS] Roads, Rail, and Trade Routes dossier (Atlas v1.0 Ch. 13); [ENCY] KFM Encyclopedia; [DIRRULES] Directory Rules; [DOM-ARCH] Archaeology / Cultural Heritage dossier; [DOM-SETTLE] Settlements / Infrastructure dossier; [DOM-HYD] Hydrology dossier; [DOM-HAZ] Hazards dossier; [DOM-PEOPLE] People / Genealogy / DNA / Land dossier; [MAP-MASTER] Master MapLibre Components dossier; [GAI] Governed AI dossier; [UNIFIED] Unified Implementation Architecture Build Manual.</sub>

---

<sub><strong>Last updated:</strong> 2026-10-12 · <strong>Doc version:</strong> v0.2 (draft) · <strong>Status:</strong> standard doc; sublane structure PROPOSED · <strong>CONTRACT_VERSION:</strong> 3.0.0 · <strong>Owners:</strong> Roads/Rail/Trade Routes steward — `TBD`; cultural-heritage reviewer — `TBD` · [↑ back to top](#trade-routes--historic-alignments-sublane--roads-rail-and-trade-routes-domain)</sub>
