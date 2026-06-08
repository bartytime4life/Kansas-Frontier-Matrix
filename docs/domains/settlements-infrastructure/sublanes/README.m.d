<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/settlements-infrastructure-object-families
title: Settlements & Infrastructure — Object Families
type: standard
version: v1
status: draft
owners: PLACEHOLDER-settlements-infrastructure-domain-steward, PLACEHOLDER-docs-steward
created: 2026-06-07
updated: 2026-06-07
policy_label: public
related: [ai-build-operating-contract.md, directory-rules.md, docs/domains/settlements-infrastructure/README.md, docs/domains/settlements-infrastructure/PATHS.md, contracts/domains/settlements-infrastructure/, schemas/contracts/v1/domains/settlements-infrastructure/]
tags: [kfm, settlements-infrastructure, object-families, ddd, grouping]
notes: [Doctrine-adjacent; CONTRACT_VERSION = "3.0.0" pinned. Authored via Option A in place of a requested sublanes/ folder. "Sublane" is NOT an established KFM unit; the doctrinal subdivision of a domain is by OBJECT FAMILY. This doc groups the compound domain's families settlements-side vs infrastructure-side without minting a new structural unit. Families are CONFIRMED (Atlas ch.14 §B/§E, §24.14); field realization and all paths are PROPOSED.]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🏘️ Settlements & Infrastructure — Object Families

> The object families this compound domain owns, grouped by its two natural halves — settlements-side and infrastructure-side — using the doctrinal subdivision unit (object family), not an invented "sublane."

![status](https://img.shields.io/badge/status-draft-orange)
![doc](https://img.shields.io/badge/doc-object_families-blue)
![domain](https://img.shields.io/badge/domain-settlements--infrastructure-1f6feb)
![subdivision](https://img.shields.io/badge/subdivision-by_object_family-blueviolet)
![contract](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-informational)
<!-- TODO: replace with real CI / contract-coverage endpoint once available -->
![families](https://img.shields.io/badge/field_realization-PROPOSED-lightgrey)

**Status:** `draft` · **Owners:** Settlements/Infrastructure domain steward + docs steward _(placeholders — verify)_ · **Updated:** 2026-06-07
**Pinned:** `CONTRACT_VERSION = "3.0.0"` (`ai-build-operating-contract.md`)

> [!IMPORTANT]
> **The doctrinal way to subdivide a domain is by object family, not by "sublane."** KFM has no "sublane" unit; domains split into object families, and cross-cutting files route to the lowest common responsibility root. This doc groups the compound domain's families into a **settlements-side** and an **infrastructure-side** view for navigation only — both halves remain one bounded context under one lane. *(CONFIRMED — `[DIRRULES §12] [ENCY §24.14] [DDD]`)*

---

## Quick navigation

- [1. Why this grouping](#1-why-this-grouping)
- [2. Settlements-side families](#2-settlements-side-families)
- [3. Infrastructure-side families](#3-infrastructure-side-families)
- [4. Shared / boundary families](#4-shared--boundary-families)
- [5. Family map (diagram)](#5-family-map-diagram)
- [6. Sensitivity by family group](#6-sensitivity-by-family-group)
- [7. What this grouping is NOT](#7-what-this-grouping-is-not)
- [Open questions register](#open-questions-register)
- [Open verification backlog](#open-verification-backlog)
- [Changelog](#changelog-v0--v1)
- [Definition of done](#definition-of-done)
- [Related docs](#related-docs)

---

## 1. Why this grouping

"Settlements **and** Infrastructure" is one bounded context with two recognizable halves. Rather than introduce a `sublanes/` folder — a structural unit KFM does not define — this doc uses the unit doctrine **does** define: the **object family**. Each family below is a CONFIRMED member of the domain's owned set (Atlas ch.14 §B / object-family spine); the **fields** that realize each family are PROPOSED until verified against `schemas/contracts/v1/domains/settlements-infrastructure/`. `[DOM-SETTLE §B, §E] [ENCY §24.14]`

> [!NOTE]
> Definitions live in the lane glossary (a `UBIQUITOUS_LANGUAGE.md` neighbor, PROPOSED); shape lives in `schemas/`; meaning in `contracts/`. This doc only **groups and routes**.

[↑ Back to top](#top)

---

## 2. Settlements-side families

The human-settlement half: places, their legal-status history, and historic/cultural sites. `[DOM-SETTLE §B, §E]`

| Family | One-line role (this context) | Status |
|---|---|---|
| **Settlement** | A populated place as an evidence-bearing object or released derivative. | CONFIRMED term / PROPOSED field |
| **Municipality** | An incorporated governing place; legal-status events kept distinct from geometry. | CONFIRMED term / PROPOSED field |
| **CensusPlace** | A census-defined place (for comparison and aggregation), `administrative`/`aggregate` in role. | CONFIRMED term / PROPOSED field |
| **Townsite** | A platted or historic townsite. | CONFIRMED term / PROPOSED field |
| **GhostTown** | A depopulated/abandoned settlement, often `candidate`/historic. | CONFIRMED term / PROPOSED field |
| **Fort** | A military post as a settlement-adjacent site (cites Archaeology for cultural truth). | CONFIRMED term / PROPOSED field |
| **Mission** | A mission site (cites Archaeology for cultural truth). | CONFIRMED term / PROPOSED field |
| **ReservationCommunity** | A reservation community; sovereignty/cultural sensitivity applies. | CONFIRMED term / PROPOSED field |

[↑ Back to top](#top)

---

## 3. Infrastructure-side families

The built-infrastructure half: assets, networks, facilities, and the operations/conditions around them. `[DOM-SETTLE §B, §E]`

| Family | One-line role (this context) | Status |
|---|---|---|
| **Infrastructure Asset** | A built asset (utility, public works, etc.); **critical detail defaults to T4**. | CONFIRMED term / PROPOSED field |
| **Network Node** | A node in an infrastructure network (vertex). | CONFIRMED term / PROPOSED field |
| **Network Segment** | A segment/edge of an infrastructure network. | CONFIRMED term / PROPOSED field |
| **Facility** | A facility serving the network (cites Roads/Rail for transport facilities). | CONFIRMED term / PROPOSED field |
| **Service Area** | The area an asset/facility serves; often `aggregate`. | CONFIRMED term / PROPOSED field |
| **Operator** | The entity operating an asset/facility/service. | CONFIRMED term / PROPOSED field |
| **Condition Observation** | A time-scoped condition reading; `observed`; condition detail may be T2/T4. | CONFIRMED term / PROPOSED field |
| **Dependency** | A dependency relation between assets/facilities; suppressed in public for critical assets. | CONFIRMED term / PROPOSED field |

> [!CAUTION]
> `Infrastructure Asset` (critical detail), `Condition Observation` (vulnerability), and `Dependency` (for critical assets) carry the **critical-asset deny lane**: precise detail defaults to **T4**, generalized footprint to T1 only after steward review, condition/vulnerability to T3 named-authorities-only. Governed under `policy/sensitivity/infrastructure/`. `[DOM-SETTLE §I] [ENCY §24.5.2]`

[↑ Back to top](#top)

---

## 4. Shared / boundary families

Some families sit on the boundary or are shared with other lanes; ownership and citation direction matter.

| Family | Note |
|---|---|
| **Network Node / Network Segment** | Also appear in Roads/Rail (transport network). Here they are *infrastructure* networks; Roads/Rail owns *transport* networks. Keep the two uses distinct — same English term, different bounded context. |
| **Facility** | Transport facilities (depot, yard) are Roads/Rail's `TransportFacility`; this lane's `Facility` is the infrastructure/service facility. Cross-reference, don't redefine. |
| **Fort / Mission / ReservationCommunity** | Cultural truth and sensitivity are Archaeology's / People-Land's; this lane holds the settlement view and cites theirs. |

*(CONFIRMED non-ownership + cross-lane relations — `[DOM-SETTLE §B, §F]`)*

[↑ Back to top](#top)

---

## 5. Family map (diagram)

```mermaid
flowchart TD
  DOM["Settlements / Infrastructure<br/>(one bounded context)"]
  subgraph settle["Settlements-side"]
    S["Settlement"]
    M["Municipality"]
    CP["CensusPlace"]
    TS["Townsite"]
    GT["GhostTown"]
    FT["Fort"]
    MI["Mission"]
    RC["ReservationCommunity"]
  end
  subgraph infra["Infrastructure-side"]
    IA["Infrastructure Asset<br/>(T4 critical detail)"]
    NN["Network Node"]
    NS["Network Segment"]
    FAC["Facility"]
    SA["Service Area"]
    OP["Operator"]
    CO["Condition Observation"]
    DEP["Dependency"]
  end
  DOM --> settle
  DOM --> infra
  FT -.->|"cultural truth cites"| ARCH["Archaeology"]
  FAC -.->|"transport facility cites"| ROADS["Roads / Rail"]
  IA -.->|"hazard exposure cites"| HAZ["Hazards"]
```

<sub>CONFIRMED family set (Atlas ch.14 §B/§E); group split and cross-lane edges are an INFERRED navigation aid, PROPOSED until contract-verified.</sub>

[↑ Back to top](#top)

---

## 6. Sensitivity by family group

| Group | Default posture | Gate |
|---|---|---|
| Settlements-side (Settlement, Municipality, CensusPlace, Townsite, GhostTown) | T0 | standard gates |
| Cultural-adjacent (Fort, Mission, ReservationCommunity) | steward review; defer to Archaeology / People-Land sensitivity | `ReviewRecord` + rights-holder where applicable |
| Infrastructure-side — general | T0/T1 | standard gates; generalize where needed |
| Infrastructure-side — critical detail / condition / dependency | **T4** | steward review + `RedactionReceipt`; T3 named-authorities-only |

*(Tiers PROPOSED per `[ENCY §24.5.2]`; critical-asset deny lane `[DOM-SETTLE §I]`)*

[↑ Back to top](#top)

---

## 7. What this grouping is NOT

> [!WARNING]
> This settlements-side / infrastructure-side split is a **navigation aid, not a structural subdivision.** It does **not**:
> - create a `sublanes/` folder or any new directory unit (no doctrinal basis);
> - split the bounded context into two contexts (it remains one lane, one ubiquitous language);
> - change placement — all files still live in the single `settlements-infrastructure` lane segments per Directory Rules §12;
> - override `contracts/` or `schemas/`, which remain the authority for meaning and shape.
>
> If a genuine split into two domains is ever proposed, that is an **ADR-class** decision (it would add a domain), not a doc-level grouping. `[DIRRULES §2.4]`

[↑ Back to top](#top)

---

## Open questions register

| ID | Question | Owner role | Resolution path |
|---|---|---|---|
| OQ-SI-OF-01 | Is the settlements/infrastructure split ever intended to become two domains, or does it stay one compound lane? | Domain steward | ADR (adding a domain is §2.4-class) |
| OQ-SI-OF-02 | Singular `settlement/` schema slug vs full `settlements-infrastructure/` lane name. | Docs steward | Shared with PATHS.md OQ-SI-PATH-01; ADR/drift |
| OQ-SI-OF-03 | Do `Network Node` / `Network Segment` / `Facility` need disambiguation from the Roads/Rail same-named terms in the glossary? | Domain steward | `UBIQUITOUS_LANGUAGE.md` cross-reference |

## Open verification backlog

These remain `NEEDS VERIFICATION` before promotion from `draft` to `published`:

1. Field realization of every family against `schemas/contracts/v1/domains/settlements-infrastructure/`.
2. Semantic definitions against `contracts/domains/settlements-infrastructure/` (this doc mirrors, not invents).
3. Confirmation that no `sublanes/` (or similar) folder exists or is planned.
4. Critical-asset tier defaults against `policy/sensitivity/infrastructure/`.

## Changelog v0 → v1

| Change | Type (per contract §37) | Reason |
|---|---|---|
| Created as object-families grouping (Option A) | new | Requested `sublanes/README.m.d` reframed: "sublane" has no doctrinal basis; domains subdivide by object family `[DIRRULES §12] [ENCY §24.14]` |
| Settlements-side / infrastructure-side grouping of CONFIRMED families | clarification | Serve the organizing intent without minting a structural unit |
| Critical-asset deny-lane caution by family group | clarification | Sensitivity must travel with the families |

> **Backward compatibility.** New file `OBJECT_FAMILIES.md` (not the requested `sublanes/README.m.d`; `.m.d` was a malformed extension, and `sublanes/` an undefined unit). No prior anchors.

## Definition of done

This document is done enough to enter the repository when:

- it is placed at `docs/domains/settlements-infrastructure/OBJECT_FAMILIES.md` per Directory Rules §12;
- a domain steward **and** docs steward review it;
- it mirrors (does not contradict) `contracts/domains/settlements-infrastructure/`;
- it is linked from the lane `README.md` and the glossary;
- no `sublanes/`-style folder is introduced absent an accepted ADR;
- the `GENERATED_RECEIPT.json` planned in Notes is wired into CI;
- future changes follow the operating contract's §37 lifecycle.

---

## Related docs

- [`docs/domains/settlements-infrastructure/README.md`](./README.md) — lane landing page
- [`docs/domains/settlements-infrastructure/PATHS.md`](./PATHS.md) — lane path crosswalk
- `docs/domains/settlements-infrastructure/UBIQUITOUS_LANGUAGE.md` — glossary *(PROPOSED — TODO)*
- [`directory-rules.md`](../../../directory-rules.md) — Domain Placement Law §12; §2.4 ADR triggers
- [`ai-build-operating-contract.md`](../../../ai-build-operating-contract.md) — operating law; `CONTRACT_VERSION = "3.0.0"`
- Atlas ch.14 §B/§E (object families) and §24.14 (object-family × domain matrix) — dossier
- `contracts/domains/settlements-infrastructure/` · `schemas/contracts/v1/domains/settlements-infrastructure/` *(PROPOSED)*

---

*Last updated: 2026-06-07 · Doc version: v1 (draft) · `CONTRACT_VERSION = "3.0.0"`*

[↑ Back to top](#top)

