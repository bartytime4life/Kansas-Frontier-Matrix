<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TBD-settlements-infrastructure-sublane-settlements
title: Settlements / Infrastructure — Settlements Sublane Dossier
type: standard
version: v0.1
status: draft
owners: Settlements/Infrastructure domain stewards (TBD — placeholder)
created: 2026-05-19
updated: 2026-05-19
policy_label: public (sublane scaffold) — content tiers vary; Settlement / Municipality / GhostTown default T0, sovereignty-sensitive surfaces (ReservationCommunity, archaeology-adjacent townsites) escalate per per-source review
related:
  - docs/domains/settlements-infrastructure/README.md           # PROPOSED parent dossier
  - docs/domains/settlements-infrastructure/sublanes/infrastructure.md   # PROPOSED sibling sublane
  - docs/domains/roads-rail-trade/README.md                     # canonical owner of transport routes
  - docs/domains/roads-rail-trade/sublanes/rail.md              # rail-side depot identity discussion
  - docs/domains/hydrology/README.md                            # water / wastewater / floodplain context
  - docs/domains/hazards/README.md                              # exposure, resilience, disaster declarations
  - docs/domains/people-dna-land/README.md                      # residence, ownership, parcel, living-person privacy
  - docs/domains/archaeology/README.md                          # historic site / townsite cultural sensitivity
  - docs/domains/frontier-matrix/README.md                      # Settlement Status as matrix input
  - docs/doctrine/directory-rules.md                            # placement authority
tags: [kfm, domain, settlements-infrastructure, sublane, settlements]
notes:
  - "The 'sublanes/' organizational layer is a PROPOSED extension of docs/domains/<domain>/; not yet enumerated in Directory Rules §6.1. See OPEN-DR-SUBLANE-01."
  - "All path, route, schema, and tooling claims remain PROPOSED until a mounted repository is inspected."
  - "ReservationCommunity sensitivity defers to Indigenous-sovereignty review under [DOM-ARCH] / [DOM-PEOPLE] doctrine; this sublane does not author that policy."
[/KFM_META_BLOCK_V2] -->

# Settlements / Infrastructure — **Settlements Sublane Dossier**

> _Governance scaffold for Kansas community-and-place identity evidence — settlements, municipalities, census places, historic townsites, ghost towns, forts, missions, and reservation communities — within the Settlements/Infrastructure domain lane._

![Status](https://img.shields.io/badge/status-draft-yellow) ![Doc Type](https://img.shields.io/badge/type-sublane%20dossier-blue) ![Domain](https://img.shields.io/badge/domain-settlements--infrastructure-informational) ![Sublane](https://img.shields.io/badge/sublane-settlements-success) ![Lifecycle](https://img.shields.io/badge/lifecycle-RAW%20%E2%86%92%20PUBLISHED-lightgrey) ![Sensitivity](https://img.shields.io/badge/sensitivity-T0%20default%20%C2%B7%20escalate%20on%20cultural%2Fsacred-orange) ![Truth Labels](https://img.shields.io/badge/labels-CONFIRMED%20%7C%20PROPOSED%20%7C%20NEEDS%20VERIFICATION-blueviolet)

<sub><strong>Status:</strong> draft · <strong>Owners:</strong> Settlements/Infrastructure stewards (TBD placeholder) · <strong>Last updated:</strong> 2026-05-19 · <strong>Supersedes:</strong> n/a (first edition)</sub>

> [!IMPORTANT]
> **Scaffolding posture.** This file is a **doctrine surface**, not an implementation claim. It refines the `[DOM-SETTLE]` chapter (Atlas v1.0 Ch. 14) and the v1.1 Master Atlases (Atlas v1.1 Ch. 24) for the *place / community identity* half of the combined Settlements/Infrastructure lane. The sibling **infrastructure sublane** (assets, networks, facilities, service areas, operators, condition observations, dependencies) is **PROPOSED** and **NEEDS VERIFICATION** of authoring. Where the parent `[DOM-SETTLE]` chapter and this sublane disagree, **`[DOM-SETTLE]` governs** and the conflict is filed against `docs/registers/DRIFT_REGISTER.md` per Directory Rules §2.5.

> [!NOTE]
> **Truth-label convention.** Every claim that walks into implementation territory (routes, schemas, packages, tests, CI, deployment, runtime behavior) is **PROPOSED** or **NEEDS VERIFICATION** until checked against a mounted repository. Doctrine inherited from `[DOM-SETTLE]`, `[ENCY]`, `[DIRRULES]`, `[UNIFIED]`, `[MAP-MASTER]`, and `[GAI]` is **CONFIRMED** when faithful to source.

---

## Table of contents

- [A. Scope and one-line purpose](#a-scope-and-one-line-purpose)
- [B. Object families owned by this sublane](#b-object-families-owned-by-this-sublane)
- [C. Repo fit — parent dossier and responsibility roots](#c-repo-fit--parent-dossier-and-responsibility-roots)
- [D. Ubiquitous language (sublane-scoped)](#d-ubiquitous-language-sublane-scoped)
- [E. Key source families for the settlements sublane](#e-key-source-families-for-the-settlements-sublane)
- [F. Identity, deterministic basis, and temporal handling](#f-identity-deterministic-basis-and-temporal-handling)
- [G. Cross-lane and cross-sublane relations](#g-cross-lane-and-cross-sublane-relations)
- [H. Map and viewing products](#h-map-and-viewing-products)
- [I. Pipeline shape (RAW → PUBLISHED)](#i-pipeline-shape-raw--published)
- [J. Sensitivity, rights, and publication posture](#j-sensitivity-rights-and-publication-posture)
- [K. API, contract, and schema surfaces](#k-api-contract-and-schema-surfaces)
- [L. Validators, tests, fixtures](#l-validators-tests-fixtures)
- [M. Governed AI behavior for this sublane](#m-governed-ai-behavior-for-this-sublane)
- [N. Publication, correction, and rollback](#n-publication-correction-and-rollback)
- [O. Open questions and verification backlog](#o-open-questions-and-verification-backlog)
- [P. Related docs](#p-related-docs)

---

## A. Scope and one-line purpose

**CONFIRMED doctrine / PROPOSED sublane application.** The settlements sublane governs *place-and-community identity evidence* within the Settlements/Infrastructure domain (`[DOM-SETTLE]`): named settlements as legal, administrative, census, historic, military, religious, and reservation-community entities; their boundaries, status transitions, and public-safe representations; and their relations into the wider KFM graph. The sublane does **not** own infrastructure assets, networks, facilities, service areas, operators, condition observations, or dependencies — those remain with the sibling **infrastructure sublane** under the same domain root.

`[DOM-SETTLE]` `[ENCY]` `[DIRRULES]`

This sublane operates inside KFM's overall posture: **governed, evidence-first, map-first, time-aware**. Promotion to PUBLISHED is a **governed state transition, not a file move** (`[DIRRULES]` §0 lifecycle invariant). Public clients reach this content only through the **governed API** (trust-membrane rule, `[ENCY]` §24.9.2).

[↑ back to top](#settlements--infrastructure--settlements-sublane-dossier)

---

## B. Object families owned by this sublane

### B.1 Owned (CONFIRMED doctrine / PROPOSED field realization)

The parent chapter (`[DOM-SETTLE]` §B, Atlas Ch. 14, p. 90) names sixteen object families. The *settlements sublane* claims the place-/community-identity subset:

| Object family | Sublane role | Source |
|---|---|---|
| **Settlement** | Generic place-of-occupation identity (umbrella for legal/historic/census variants when none of the more specific classes is admissible). | `[DOM-SETTLE]` `[ENCY]` |
| **Municipality** | Legal incorporated entity (city, town, township, village) with charter, boundary, governance, status events. | `[DOM-SETTLE]` `[ENCY]` |
| **CensusPlace** | Census-defined place (CDP, incorporated place as enumerated by the census authority) — a *statistical* identity distinct from legal municipality. | `[DOM-SETTLE]` `[ENCY]` |
| **Townsite** | Platted town site (legal plat record, historic founding act) — an *origin* claim, not necessarily a continuing settlement. | `[DOM-SETTLE]` `[ENCY]` |
| **GhostTown** | A settlement whose population has dropped to zero or near-zero and whose evidentiary trail has shifted from active records to historical / archaeological sources. | `[DOM-SETTLE]` `[ENCY]` |
| **Fort** | Military post — built, garrisoned, decommissioned; historic-era authority for many settlement origins. | `[DOM-SETTLE]` `[ENCY]` |
| **Mission** | Religious mission station — founding, operation, abandonment; cultural-heritage adjacency. | `[DOM-SETTLE]` `[ENCY]` |
| **ReservationCommunity** | Community on an Indigenous reservation or trust land. Sovereignty review and `[DOM-ARCH]` / `[DOM-PEOPLE]` cultural-sensitivity policy govern downstream publication. | `[DOM-SETTLE]` `[ENCY]` `[DOM-ARCH]` `[DOM-PEOPLE]` |

> [!NOTE]
> **One umbrella, several specialisations.** A given Kansas place may carry multiple co-existing identities at the same `valid_time` — e.g., a Settlement + Municipality + CensusPlace + (historically) Fort. KFM does **not** collapse them into one object; identity stays plural and source-roled, with cross-references through the catalog. Identity rule below (§F).

### B.2 Explicit non-ownership

The settlements sublane explicitly does **not** own the following. Authoring or publishing those claims here is a doctrine violation:

| Concern | Owning lane / sublane | Why this matters |
|---|---|---|
| Infrastructure Asset, Network Node, Network Segment, Facility, Service Area, Operator, Condition Observation, Dependency | **Infrastructure sublane** (sibling, same parent `[DOM-SETTLE]`) | A depot, water tower, substation, hospital, or school building is an *asset* in its own object family. The settlements sublane only consumes the *place* relation, not the asset detail. |
| Road / rail / trail / trade-route alignments and corridor identity | **Roads / Rail / Trade Routes** (`[DOM-ROADS]`) | Transport route truth is owned upstream; this sublane consumes routes as *context* (e.g., "settled along the Smoky Hill Trail"). |
| Hydrologic feature evidence | **Hydrology** (`[DOM-HYD]`) | Rivers, gauges, NFHL zones live in hydrology; the settlements sublane only carries spatial-adjacency joins. |
| Hazard events, warnings, disaster declarations | **Hazards** (`[DOM-HAZ]`) | KFM is **never** an emergency-alert authority (`[DOM-HAZ]` retained boundary; Atlas v1.1 §24.5.2). The settlements sublane cites hazard exposure but does not author it. |
| Person assertions, living-person fields, DNA, residence / migration events, parcel ownership | **People / DNA / Land** (`[DOM-PEOPLE]`) | Living-person and DNA fields default **T4** (deny). This sublane never publishes joins that pierce that policy. |
| Archaeological sites, sacred sites, cultural-heritage chronology | **Archaeology / Cultural Heritage** (`[DOM-ARCH]`) | Site coordinates default **T4**; historic-townsite adjacency uses generalized geometry only after steward review. |
| Frontier Definition, GeographyVersion, County-Year Panel, Settlement Status (matrix-level) | **Frontier Matrix** | `[DOM-SETTLE]` owns *legal and infrastructure status of a settlement*; the matrix owns *Settlement Status as a panel cell* in a county-year analytic. The two are related but not identical. |
| LandParcel, Land Office Record, Public Land Record | **People / Land** and **Frontier Matrix** | The parcel and land-office surfaces are owned upstream. The settlements sublane consumes them as *context*, never as authority. |

`[DOM-SETTLE]` `[DOM-ROADS]` `[DOM-HYD]` `[DOM-HAZ]` `[DOM-PEOPLE]` `[DOM-ARCH]` `[ENCY]` `[UNIFIED]`

[↑ back to top](#settlements--infrastructure--settlements-sublane-dossier)

---

## C. Repo fit — parent dossier and responsibility roots

### C.1 PROPOSED tree (this sublane in its dossier context)

> [!CAUTION]
> The tree below is **PROPOSED** and **NEEDS VERIFICATION** against a mounted repository. The `settlements-infrastructure/` subfolder under `docs/domains/` is **CONFIRMED in `docs/doctrine/directory-rules.md` §6.1** as one of the listed domain-dossier subfolders. The `sublanes/` layer beneath it is **not yet enumerated** there. Treat the structure as a working scaffold pending **OPEN-DR-SUBLANE-01** (§ O).

```text
docs/
└── domains/
    └── settlements-infrastructure/                    # CONFIRMED in directory-rules.md §6.1 listing
        ├── README.md                                  # PROPOSED parent dossier README (NEEDS VERIFICATION)
        ├── ARCHITECTURE.md                            # PROPOSED — parallel to peer dossiers
        ├── PRESERVATION_MATRIX.md                     # PROPOSED — parallel to peer dossiers
        ├── VERIFICATION_BACKLOG.md                    # PROPOSED
        └── sublanes/                                  # PROPOSED organizational layer — see OPEN-DR-SUBLANE-01
            ├── README.md                              # PROPOSED — sublane index
            ├── settlements.md                         # THIS FILE
            └── infrastructure.md                      # PROPOSED sibling sublane
```

### C.2 Canonical responsibility roots this dossier defers to

The settlements sublane is a **doctrine surface**, not an authority root. Every implementation artifact derived from this sublane lands in a **canonical responsibility root** elsewhere in the repo (`[DIRRULES]` §5 / §12 / Domain Placement Law). The sublane explicitly **does not** create parallel homes for schemas, contracts, policy, sources, registries, releases, proofs, or receipts (`[DIRRULES]` §13).

| Surface | Canonical responsibility root (PROPOSED) | Authority |
|---|---|---|
| Object meaning (Markdown contracts) | `contracts/domains/settlements-infrastructure/` | `[DIRRULES]` §6.3 |
| Machine schemas (JSON Schema, JSON-LD context) | `schemas/contracts/v1/settlement/` (per `[ENCY]` §5.1 and Atlas v1.1 §24.13) | ADR-0001 schema-home |
| Policy bundles (allow / deny / restrict / abstain) | `policy/domains/settlements-infrastructure/` and `policy/sensitivity/infrastructure/` (the infrastructure-side sensitivity register applies even to settlements joins that *cross* it) | `[DIRRULES]` §6.5; `[ENCY]` §5.1 |
| Tests | `tests/domains/settlements-infrastructure/` | `[DIRRULES]` §6 |
| Fixtures | `fixtures/domains/settlements-infrastructure/` | `[DIRRULES]` §6 |
| Pipelines / specs | `pipelines/domains/settlements-infrastructure/`, `pipeline_specs/settlements-infrastructure/` | `[DIRRULES]` §6 |
| Data lifecycle | `data/{raw,work,quarantine,processed,catalog,published,registry,receipts,proofs,rollback}/settlements-infrastructure/` | `[DIRRULES]` §6.10 |
| Release decisions | `release/candidates/settlements-infrastructure/` | `[DIRRULES]` §6.11 |
| Public surface | `apps/governed-api/` (trust-membrane rule) | `[DIRRULES]` §6 / `[ENCY]` §24.9.2 |

> [!IMPORTANT]
> **Sublane scope discipline.** Because the canonical responsibility roots are keyed to the **parent domain** (`settlements-infrastructure`) and not to the sublane, this file is **organizational, not authoritative** with respect to where artifacts live. The split between the settlements sublane and the infrastructure sublane is a **doctrine-level boundary**, not a directory-level one. ADR-S-SUBLANE-02 (PROPOSED, see §O) tracks whether `<domain>/sublanes/` should ever propagate into non-`docs/` roots — current default: **no**.

[↑ back to top](#settlements--infrastructure--settlements-sublane-dossier)

---

## D. Ubiquitous language (sublane-scoped)

> All terms inherit Settlements/Infrastructure lane semantics from `[DOM-SETTLE]` and `[ENCY]` and are constrained by **source role, evidence, time, and release state**. Casing follows project convention exactly.

| Term | Sublane-scoped working definition | Source |
|---|---|---|
| **Settlement** | Generic, source-roled identity for a place of human occupation in Kansas at a given `valid_time`. Used when a more specific class (Municipality, CensusPlace, Townsite, etc.) is not directly admissible. | `[DOM-SETTLE]` `[ENCY]` |
| **Municipality** | Legally incorporated entity (city of the first/second/third class, township, village) recognized by Kansas statute or county record. Carries charter and status events; legal-source role required. | `[DOM-SETTLE]` `[ENCY]` |
| **CensusPlace** | A place enumerated by the census authority (incorporated place or census-designated place) at a specific census vintage. *Statistical*, not legal. | `[DOM-SETTLE]` `[ENCY]` |
| **Townsite** | A platted or proclaimed town site — the *founding* claim. May or may not still correspond to a continuing settlement; downstream evidence determines that. | `[DOM-SETTLE]` `[ENCY]` |
| **GhostTown** | A place once meeting Settlement criteria whose evidentiary trail has shifted from active legal/census records to historical and (sometimes) archaeological sources. Marked as such only with cite-or-abstain support. | `[DOM-SETTLE]` `[ENCY]` |
| **Fort** | Military post — a place identified by garrisoning record (federal, territorial, state, or tribal). Founding, garrison period, and decommissioning carried as status events. | `[DOM-SETTLE]` `[ENCY]` |
| **Mission** | Religious mission station identified by founding-organization record; carries operation and abandonment events; cultural-heritage adjacency to `[DOM-ARCH]`. | `[DOM-SETTLE]` `[ENCY]` |
| **ReservationCommunity** | A community located on Indigenous reservation or trust land. Sovereignty review and `[DOM-ARCH]` / `[DOM-PEOPLE]` cultural-sensitivity policy govern downstream publication of detail. | `[DOM-SETTLE]` `[ENCY]` `[DOM-ARCH]` `[DOM-PEOPLE]` |
| **StatusEvent** *(consumed)* | A dated change in legal, census, or operational status (incorporation, disincorporation, name change, annexation, abandonment, decommissioning). Sourced from legal records, census vintages, or historical authority. | `[DOM-SETTLE]` `[UNIFIED]` |
| **PlaceNameAssertion** *(consumed)* | An assertion that a given identifier (e.g., a GNIS feature, a historical gazetteer entry) refers to a Settlement object at a given time. Multiple competing assertions are allowed and cite-or-abstain-resolved. | `[DOM-SETTLE]` `[ENCY]` |
| **SettlementStatus** *(referenced; matrix-owned)* | A *Frontier Matrix*–owned object that records settlement-related state at a county-year panel level. The settlements sublane feeds it but does not author it. | `[ENCY]` `[UNIFIED]` |

[↑ back to top](#settlements--infrastructure--settlements-sublane-dossier)

---

## E. Key source families for the settlements sublane

Adapted from `[DOM-SETTLE]` §D (Atlas v1.0 p. 91). Sources whose primary value is *infrastructure-asset detail* (KDOT bridge condition, FEMA resilience inventory, operator-side utility data) move to the **infrastructure sublane** and are referenced from there.

| Source family | Role (admission-time) | Rights / sensitivity | Freshness | Status |
|---|---|---|---|---|
| **Census TIGER / census place geography** | Authority for `CensusPlace`; observation for boundary; context for Settlement / Municipality | Open per current census authority terms — **NEEDS VERIFICATION** per release vintage; sensitive joins fail closed | Source-vintage specific (decennial + ACS revisions) | `[DOM-SETTLE]` `[ENCY]` |
| **GNIS and gazetteers** | Authority for canonical place-name records (federal); context for cross-source identity reconciliation | Public; current terms **NEEDS VERIFICATION**; sensitive joins (e.g., archaeology-adjacent feature names) fail closed | Cadence per upstream service | `[DOM-SETTLE]` `[ENCY]` |
| **State / local GIS — Kansas Geoportal-style sources** | Authority for state/local administrative boundaries; observation for current settlements | Rights and current terms **NEEDS VERIFICATION**; sensitive joins fail closed | Source-vintage / cadence specific | `[DOM-SETTLE]` `[ENCY]` |
| **Municipal and local legal records** | Authority for **Municipality** charter, incorporation, annexation, dissolution events | Public-record terms — **NEEDS VERIFICATION** per jurisdiction; sensitive joins (living-person officials) fail closed | Event-driven | `[DOM-SETTLE]` `[ENCY]` |
| **Historical gazetteers and maps** | Authority for **Townsite**, **GhostTown**, **Fort**, **Mission** historical existence claims; context for legal-municipality predecessors | Source-by-source; rights **NEEDS VERIFICATION**; cultural-heritage joins escalate to `[DOM-ARCH]` review | Snapshot (one vintage per source) | `[DOM-SETTLE]` `[ENCY]` |
| **Tribal-nation public registries and treaty-record context** | Authority for **ReservationCommunity** identification at a specified level of detail; sovereignty-governed | Tribal-data sovereignty governs — **NEEDS VERIFICATION** per nation and per record; fail closed by default | Event-driven | `[DOM-SETTLE]` `[DOM-PEOPLE]` `[DOM-ARCH]` `[ENCY]` |
| **Academic and historical-society publications (settlement histories)** | Context / model (interpretive); secondary attribution only | Copyright varies; **NEEDS VERIFICATION** per work | Snapshot | `[DOM-SETTLE]` `[ENCY]` |

> [!WARNING]
> **Source-role anti-collapse (Atlas v1.1 §24.1).** A census enumeration is **not** a legal-incorporation record; a historical gazetteer entry is **not** a federal-authority place name; a settlement-history monograph is **not** a primary legal source. Source role is **fixed at admission** and is **never silently upgraded** by promotion (`[ENCY]` `[UNIFIED]`).

[↑ back to top](#settlements--infrastructure--settlements-sublane-dossier)

---

## F. Identity, deterministic basis, and temporal handling

CONFIRMED from `[DOM-SETTLE]` §E (Atlas v1.0 pp. 92–93):

- **Deterministic identity basis (PROPOSED across object families):** `source id + object role + temporal scope + normalized digest`.
- **Temporal handling (CONFIRMED):** source, observed, valid, retrieval, release, and correction times **stay distinct where material**.

In this sublane that means:

| Object | Identity rule (PROPOSED) | Notes on temporal handling |
|---|---|---|
| Settlement | Source id + role `place` + temporal scope (`valid_from` / `valid_to` where known) + normalized digest of canonical fields. | A single physical location may carry multiple Settlement records across time (origin claim → renamed → reorganized as Municipality). |
| Municipality | Source id + role `legal-place` + charter/jurisdiction key + temporal scope + digest. | StatusEvents (incorporation, dissolution, annexation, name change) emitted as separate records, each with own `observed_at` and `valid_time`. |
| CensusPlace | Source id + role `census-place` + census vintage + GEOID + digest. | Each census vintage is its **own** record. Vintages are **not** silently merged. |
| Townsite | Source id + role `townsite-founding` + plat/proclamation reference + digest. | A Townsite is an *event* in time; continuing settlement, if any, is a separate Settlement / Municipality object. |
| GhostTown | Source id + role `historic-place` + predecessor settlement reference + digest. | Status as GhostTown is **derived** from evidence trail, never asserted without cite-or-abstain support. |
| Fort | Source id + role `military-post` + garrisoning-authority reference + temporal scope + digest. | Garrison and decommissioning carried as StatusEvents. |
| Mission | Source id + role `mission-station` + founding-organization reference + temporal scope + digest. | Cultural-heritage adjacency may escalate to `[DOM-ARCH]` review for detail. |
| ReservationCommunity | Source id + role `reservation-community` + nation/authority reference + temporal scope + digest. | Detail level is governed by sovereignty review; default public exposure is **generalized**. |

> [!NOTE]
> **Temporal honesty.** A 19th-century Townsite proclamation, a 1900 census place enumeration, a 1950 municipal annexation, and a 2025 GIS boundary refresh are **four** facts at **four** times. The sublane preserves all four; downstream views compose them but never collapse them silently.

[↑ back to top](#settlements--infrastructure--settlements-sublane-dossier)

---

## G. Cross-lane and cross-sublane relations

### G.1 Cross-lane edges this sublane participates in

CONFIRMED / PROPOSED (`[DOM-SETTLE]` §F): every relation must preserve **ownership**, **source role**, **sensitivity**, and **EvidenceBundle support**.

| This sublane | Related lane | Relation | Constraint |
|---|---|---|---|
| Settlements | `roads-rail-trade` | A Settlement along, founded on, or adjacent to a CorridorRoute / RouteMembership; depot location *as a place* (the asset side is infrastructure-sublane). | Transport route identity stays with `[DOM-ROADS]`; this sublane consumes the route as context, not authority. |
| Settlements | `hydrology` | Settlement-on-river, NFHL exposure adjacency, public-water-supply *placement* (asset detail is infrastructure-sublane). | Water evidence stays with `[DOM-HYD]`; we cite, we do not author. |
| Settlements | `hazards` | Disaster declaration *touching* a Settlement; resilience context. | Hazard truth stays with `[DOM-HAZ]`; **KFM is never an alert authority** (`[DOM-HAZ]` retained boundary). |
| Settlements | `people-dna-land` | Residence event referencing a Settlement; ownership / parcel context. **Living-person and DNA fields are denied at the membrane.** | `[DOM-PEOPLE]` governs; aggregate joins only; default T1/T2 with redaction receipt. |
| Settlements | `archaeology` | Historic Townsite, GhostTown, Fort, or Mission whose footprint overlaps a known archaeological context. | `[DOM-ARCH]` cultural-sensitivity policy governs; site-coordinate detail defaults **T4**; settlement public layer uses generalized geometry only. |
| Settlements | `frontier-matrix` | Feeds **Settlement Status** as a county-year panel cell. | Matrix Release rules govern the matrix output; this sublane provides the underlying evidence, never the panel. |
| Settlements | `infrastructure` *(sibling)* | A Settlement-as-place hosts Facility / Infrastructure Asset / Network Node objects. | Place identity here; asset identity in the sibling sublane. Cross-references through the catalog, not by collapsing object families. |
| Settlements | `spatial-foundation` | All settlement boundaries carry a CoordinateReferenceProfile + GeographyVersion. | Reference geometry, not authority over place truth. |

### G.2 Cross-sublane edges (PROPOSED, internal to `settlements-infrastructure`)

| This sublane | Sibling sublane | Relation | Constraint |
|---|---|---|---|
| Settlements | Infrastructure | A Municipality operates a Facility; a Fort houses Infrastructure Assets; a CensusPlace contains Network Nodes. | The structural identity of a *place* lives here; the asset identity lives in the sibling sublane. Cross-references resolve via the catalog. Operator legal-entity facts are people/land-owned. |
| Settlements | Infrastructure | A ServiceArea (operator-side) covers one or more Settlements. | Aggregation direction is *settlements ← serviceArea*; the join is allowed only when the serviceArea is on a public-safe tier (T0 / T1 generalized). |

[↑ back to top](#settlements--infrastructure--settlements-sublane-dossier)

---

## H. Map and viewing products

PROPOSED viewing products narrowed from `[DOM-SETTLE]` §G to the settlements sublane:

- **Current settlement view** — Municipality + CensusPlace, time-aware, governed Focus Mode.
- **Historic townsite view** — Townsite + GhostTown + Fort + Mission, with `valid_time` filter.
- **Legal-status-event view** — StatusEvent timeline per Municipality (incorporations, annexations, dissolutions, name changes).
- **Census-place comparison view** — multiple census vintages, *not collapsed*, with attribution per vintage.
- **Reservation-community context view** — generalized geometry; detail escalates to sovereignty review.

CONFIRMED cross-cutting viewing products (apply to every released settlement layer, `[MAP-MASTER]` `[GAI]`): **Evidence Drawer**, **time-aware state**, **trust badges**, sensitivity-redacted view, correction / stale-state view, and **governed Focus Mode**.

> [!TIP]
> **Public-safe asset view** and **service-area aggregate view** from `[DOM-SETTLE]` §G belong to the **infrastructure sublane**, not this one. This sublane carries the *place* under which those views are *anchored* in the UI.

[↑ back to top](#settlements--infrastructure--settlements-sublane-dossier)

---

## I. Pipeline shape (RAW → PUBLISHED)

CONFIRMED doctrine / PROPOSED sublane application (`[DIRRULES]` §0 lifecycle invariant; `[DOM-SETTLE]` §H; Atlas v1.1 §24.6):

```mermaid
flowchart LR
  A["RAW<br/>SourceDescriptor<br/>+ hash"] --> B["WORK / QUARANTINE<br/>TransformReceipt + ValidationReport<br/>+ PolicyDecision"]
  B -->|"pass"| C["PROCESSED<br/>EvidenceRef + ValidationReport<br/>+ digest closure"]
  B -->|"fail"| Q["QUARANTINE<br/>(reason recorded)"]
  C --> D["CATALOG / TRIPLET<br/>EvidenceBundle + CatalogMatrix<br/>+ graph projection"]
  D --> E["PUBLISHED<br/>ReleaseManifest + rollback target<br/>+ correction path + ReviewRecord"]
  E -.->|"defect or new evidence"| F["CorrectionNotice<br/>(PUBLISHED → PUBLISHED')"]
  E -.->|"policy / rights revocation"| R["Tier downgrade → T4<br/>(CorrectionNotice)"]
```

> [!NOTE]
> The diagram reflects the **doctrinal** lifecycle. Per-stage **gate artifacts** are CONFIRMED in Atlas v1.1 §24.6.1 (Pipeline Gate Reference); concrete *file paths and schema IDs* for this sublane remain PROPOSED until the canonical responsibility roots are inspected.

| Stage | Handling | Gate | Status |
|---|---|---|---|
| **RAW** | Capture immutable source payload (or stable reference) with source role, rights, sensitivity, citation, time, and content hash. | `SourceDescriptor` exists. | PROPOSED |
| **WORK / QUARANTINE** | Normalize schema, geometry, time, identity, evidence, rights, and policy. Hold failures. | Validation + policy gates pass, **or** quarantine reason is recorded. Never silently promotes. | PROPOSED |
| **PROCESSED** | Emit validated normalized Settlement / Municipality / CensusPlace / Townsite / GhostTown / Fort / Mission / ReservationCommunity objects, receipts, and public-safe candidates. | `EvidenceRef`, `ValidationReport`, and digest closure exist. | PROPOSED |
| **CATALOG / TRIPLET** | Emit catalog records, `EvidenceBundle`s, graph/triplet projections, and release candidates. | Catalog / proof closure passes. | PROPOSED |
| **PUBLISHED** | Serve released public-safe artifacts through the **governed API** and `ReleaseManifest`. | `ReleaseManifest`, rollback target, correction path, and review/policy state exist; release authority distinct from author at materiality. | PROPOSED |

`[DIRRULES]` `[DOM-SETTLE]` `[ENCY]`

[↑ back to top](#settlements--infrastructure--settlements-sublane-dossier)

---

## J. Sensitivity, rights, and publication posture

CONFIRMED doctrine (`[ENCY]` §5.1; Atlas v1.1 §24.5): Settlement / Municipality / GhostTown default **T0** (Open). The escalation rules below are **PROPOSED** sublane application of the master tier matrix.

| Object class (this sublane) | Default tier | Allowed transforms (PROPOSED) | Required gates |
|---|---|---|---|
| Settlement, Municipality, CensusPlace | **T0** | None required for public-safe attribution; minor field redaction where municipal records expose living-person detail. | Standard `ReleaseManifest` + `ReviewRecord`. |
| Townsite, GhostTown | **T0** | Generalized footprint when overlapping a known archaeological context (escalate to `[DOM-ARCH]`). | `RedactionReceipt` only if archaeology-overlap transform applied. |
| Fort, Mission | **T0** (modern interpretive) / **T1** (sensitive-period or cultural-context detail) | Generalization; cultural-context callouts; steward review. | `RedactionReceipt` + `ReviewRecord` where applicable. |
| ReservationCommunity | **T1 by default in this sublane** (generalization to community-level, never household / parcel detail) | Sovereignty review + generalization → public layer; **never** join private person-parcel fields. | `RedactionReceipt` + `ReviewRecord` + sovereignty review per `[DOM-ARCH]` / `[DOM-PEOPLE]`. |
| StatusEvent involving living-person officials (e.g., named mayor in current term) | **T1** | Redact name; carry role + event. | `RedactionReceipt` + `ReviewRecord` (per `[DOM-PEOPLE]`). |

> [!WARNING]
> **Tier upgrade is two-key, tier downgrade is one-key.** Promoting toward more-public requires a **transform receipt** *and* a **review record**. Demoting toward less-public needs only a **CorrectionNotice** with `ReviewRecord` (Atlas v1.1 §24.5.3). The asymmetry is deliberate.

> [!CAUTION]
> **Hard boundaries that hold for this sublane regardless of any settlements-side framing:**
> - The sublane **never** publishes living-person fields or DNA-derived joins (`[DOM-PEOPLE]` denies).
> - The sublane **never** publishes archaeological site coordinates as authority (`[DOM-ARCH]` denies T4).
> - The sublane **never** authors hazard alerts or emergency advisories — KFM is not an alert authority (`[DOM-HAZ]`).
> - The sublane **never** promotes a settlement claim past WORK without `EvidenceBundle` support (cite-or-abstain).

[↑ back to top](#settlements--infrastructure--settlements-sublane-dossier)

---

## K. API, contract, and schema surfaces

PROPOSED governed-API surfaces (`[DOM-SETTLE]` §J; `[ENCY]` §5.1; ADR-0001 schema home). Exact route names are **UNKNOWN** in a docs-only session.

| Endpoint or artifact | DTO / schema | Outcomes | Status |
|---|---|---|---|
| Settlement / Municipality / CensusPlace feature & detail resolver (sublane scope) | `SettlementsInfrastructureDecisionEnvelope` (sublane discriminator: `settlements`) | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED governed-API surface; exact route UNKNOWN. |
| Historic townsite / GhostTown / Fort / Mission detail resolver | Same envelope, sublane discriminator + `historic=true` | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED; public-safe release only. |
| ReservationCommunity context resolver | Same envelope, sublane discriminator + sovereignty-review filter | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` (defaults to `ABSTAIN` outside reviewer scope) | PROPOSED; default-deny on detail; T1 generalized layer for public. |
| Settlements layer-manifest resolver | `LayerManifest` / sublane layer descriptor | `ANSWER` / `DENY` / `ERROR` | PROPOSED; public-safe release only. |
| Settlements Evidence Drawer payload | `EvidenceDrawerPayload` + `EvidenceBundle` projection | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED; evidence and policy filtered at the membrane. |
| Settlements Focus Mode answer | Runtime Response Envelope + `AIReceipt` | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED; AI is **never** root truth (`[GAI]`). |
| Schema responsibility root | `schemas/contracts/v1/settlement/` | finite validator outcomes | PROPOSED per `[ENCY]` §5.1 and Atlas v1.1 §24.13; verify with Directory Rules and ADR-0001. |

> [!NOTE]
> **Finite outcomes everywhere.** Every governed-API result is one of `ANSWER` / `ABSTAIN` / `DENY` / `ERROR`. Soft / fuzzy outcomes are not permitted; the trust membrane depends on this discipline (`[ENCY]` §24.9.2).

[↑ back to top](#settlements--infrastructure--settlements-sublane-dossier)

---

## L. Validators, tests, fixtures

PROPOSED (`[DOM-SETTLE]` §K; `[DIRRULES]` §6 / §13). Sublane-scoped:

- **Legal-municipality evidence test** — every Municipality record carries a legal-source citation and an admissible role; assertion without legal source ⇒ ABSTAIN.
- **Census-vs-municipality distinction test** — a `CensusPlace` record never silently coerces into a `Municipality`; cross-references are explicit, vintaged, and reversible.
- **Settlement / Townsite / GhostTown coherence test** — a Townsite founding without continuing settlement evidence is **not** silently promoted to Settlement; a GhostTown classification requires cite-or-abstain support.
- **ReservationCommunity sovereignty-review fixture** — every published ReservationCommunity record has a sovereignty-review record in its `EvidenceBundle`; absent that, DENY at the membrane.
- **Archaeology-overlap no-leak test** — a settlements public layer must not expose archaeological site coordinates; the cross-lane edge uses generalized geometry only.
- **Living-person redaction test** — fields that would name a living-person official (current mayor, current councilmember) are redacted in the public tier; the redaction transform is reviewable.
- **Catalog / proof / release closure test** — every PUBLISHED settlements record resolves through `EvidenceBundle` to a `ReleaseManifest` with a working rollback target.
- **Time-distinct fields test** — `source_time`, `observed_at`, `valid_from` / `valid_to`, `retrieval_time`, `release_time`, `correction_time` are preserved as distinct fields where material.
- **Negative-state coverage** — validators exercise DENY / ABSTAIN / ERROR paths, not only ANSWER (tools-README contract).

Fixtures live under `fixtures/domains/settlements-infrastructure/` (PROPOSED). Golden / valid / invalid sample data follow the same lifecycle invariant as production data (`[DIRRULES]` §6).

[↑ back to top](#settlements--infrastructure--settlements-sublane-dossier)

---

## M. Governed AI behavior for this sublane

CONFIRMED doctrine / PROPOSED implementation (`[GAI]`; `[DOM-SETTLE]` §L; `[ENCY]` §24.9.2):

- AI **MAY** summarize **released** Settlements `EvidenceBundle`s, compare competing source claims (e.g., divergent founding dates between a gazetteer and a county history), explain limitations, and draft steward-review notes.
- AI **MUST `ABSTAIN`** when evidence is insufficient — e.g., a "founding date" without admissible source, a "ghost town" classification without supporting trail, a "current population" claim from a stale census vintage.
- AI **MUST `DENY`** where policy, rights, sensitivity, or release state blocks the request — e.g., a ReservationCommunity detail outside sovereignty-review scope, a living-person municipal-official identification, a query that would join a private person-parcel record, an archaeology-coordinate request via a settlement-context framing.
- AI **MUST NOT** answer settlements questions from RAW / WORK / QUARANTINE stores. Trust-membrane rule from `[ENCY]` §24.9.2 applies in full.
- Every Focus Mode answer carries an `AIReceipt`. `[GAI]`

> [!IMPORTANT]
> **EvidenceBundle outranks generated language.** Where the model would synthesize a fluent narrative that drifts from the bundle, the bundle wins and the narrative is narrowed or abstained.

[↑ back to top](#settlements--infrastructure--settlements-sublane-dossier)

---

## N. Publication, correction, and rollback

CONFIRMED doctrine / PROPOSED implementation (`[ENCY]` Appendix E; `[DOM-SETTLE]` §M; `[DIRRULES]` §6.11):

- **Publication requires:** `ReleaseManifest`, `EvidenceBundle`, validation / policy support, `ReviewRecord` where required, correction path, stale-state rule, and rollback target.
- **Release authority** is distinct from the original author when materiality applies (Atlas v1.1 §24.7 — Reviewer Role and Separation-of-Duties Matrix).
- **Correction** is `CorrectionNotice` + `ReviewRecord`; downstream derivatives are identified and either re-derived or invalidated.
- **Rollback** is always available; the manifest pins to spec-hashed contents (`KFM-P7-PROG-0003`, ReleaseManifest as publishable artifact).
- **Stale-state rule** (Atlas v1.1 §24.8): a settlements record whose underlying source has been superseded carries a stale badge until refreshed or demoted.

[↑ back to top](#settlements--infrastructure--settlements-sublane-dossier)

---

## O. Open questions and verification backlog

| ID | Question | Evidence that would settle it | Status |
|---|---|---|---|
| **OPEN-DR-SUBLANE-01** | Should `docs/domains/<combined-domain>/sublanes/` be enumerated in Directory Rules §6.1 (or §12) as a recognized organizational layer? Should it propagate to non-`docs/` roots? | ADR + mounted-repo inspection; precedent from `roads-rail-trade/sublanes/` and (PROPOSED) `habitat/sublanes/` work. | NEEDS VERIFICATION |
| **OPEN-DR-SUBLANE-02** | What is the boundary contract between this settlements sublane and the sibling infrastructure sublane when a single source (e.g., a county GIS layer) carries *both* place identity and asset detail in one feature class? | Mounted-repo schema fixtures; pipeline split rule; ADR-S-SUBLANE-02 candidate. | NEEDS VERIFICATION |
| **OPEN-DR-SUBLANE-03** | Is the schema-home `schemas/contracts/v1/settlement/` (singular) per `[ENCY]` §5.1, or `schemas/contracts/v1/settlements-infrastructure/` (combined-domain) per the §12 Domain Placement Law pattern in `directory-rules.md`? | Mounted-repo schema layout; ADR-0001 follow-up. | NEEDS VERIFICATION |
| **OPEN-SETTLE-01** | Verify source rights and **municipal legal-source roles** (statutory authority per jurisdiction). | Mounted-repo source registry + policy bundles + tests. | NEEDS VERIFICATION *(carried from `[DOM-SETTLE]` §N)* |
| **OPEN-SETTLE-02** | Verify **sovereignty-review** workflow for ReservationCommunity records and the named-party-agreement path for any detail beyond T1. | Mounted-repo policy bundles + ReviewRecord workflow; `[DOM-PEOPLE]` / `[DOM-ARCH]` coordination. | NEEDS VERIFICATION |
| **OPEN-SETTLE-03** | Verify **public-safe layer registry** for settlements (current, historic, generalized variants). | Mounted-repo `data/published/layers/settlements-infrastructure/` registry + `LayerManifest` schema. | NEEDS VERIFICATION *(carried from `[DOM-SETTLE]` §N)* |
| **OPEN-SETTLE-04** | Verify **API and Focus Mode** auth/policy behavior for settlement / municipality / reservation-community resolvers. | Mounted-repo `apps/governed-api/` routes + policy tests + AIReceipt fixtures. | NEEDS VERIFICATION *(carried from `[DOM-SETTLE]` §N)* |
| **OPEN-SETTLE-05** | Verify the *Settlement Status* hand-off between this sublane and the Frontier Matrix (who emits, who consumes, what the matrix-cell receipt looks like). | Mounted-repo matrix contracts + cross-references; `[ENCY]` `[UNIFIED]` reconciliation. | NEEDS VERIFICATION |
| **OPEN-SETTLE-06** | Verify the **historical-gazetteer** source-role taxonomy — when is a gazetteer entry *authority* for a Townsite vs. only *context*? | Mounted-repo source descriptors + ADR. | NEEDS VERIFICATION |

<details>
<summary><strong>Carried verification items from <code>[DOM-SETTLE]</code> §N — full text</strong></summary>

| Item to verify | Evidence that would settle it | Status |
|---|---|---|
| Verify source rights and municipal legal-source roles. | mounted repo files, schemas, registry entries, tests, logs, emitted artifacts, review records, or release manifests | NEEDS VERIFICATION |
| Verify critical infrastructure policy. | mounted repo files, schemas, registry entries, tests, logs, emitted artifacts, review records, or release manifests | NEEDS VERIFICATION *(applies primarily to the infrastructure sublane)* |
| Verify public-safe layer registry. | mounted repo files, schemas, registry entries, tests, logs, emitted artifacts, review records, or release manifests | NEEDS VERIFICATION |
| Verify API and Focus Mode auth/policy behavior. | mounted repo files, schemas, registry entries, tests, logs, emitted artifacts, review records, or release manifests | NEEDS VERIFICATION |

Source: `[DOM-SETTLE]` §N (Atlas v1.0 p. 96).
</details>

[↑ back to top](#settlements--infrastructure--settlements-sublane-dossier)

---

## P. Related docs

- Parent dossier: [`docs/domains/settlements-infrastructure/README.md`](../README.md) — `TODO` link target, **NEEDS VERIFICATION**.
- Sibling sublane: [`docs/domains/settlements-infrastructure/sublanes/infrastructure.md`](./infrastructure.md) — **PROPOSED**, not yet authored.
- Atlas chapter: `[DOM-SETTLE]` — Settlements / Infrastructure, Atlas v1.0 Ch. 14 (pp. 90–96); Atlas v1.1 Master Atlases (Ch. 24).
- Encyclopedia: `[ENCY]` §5.1 (Settlements / Infrastructure row); `[ENCY]` §24.9.2 (trust-membrane rule).
- Implementation architecture: `[UNIFIED]` §6.9 (Settlements / Infrastructure lane).
- Roads/Rail/Trade Routes domain: [`docs/domains/roads-rail-trade/README.md`](../../roads-rail-trade/README.md) — depot / transport facility identity boundary.
- Hydrology: [`docs/domains/hydrology/README.md`](../../hydrology/README.md) — water / wastewater / floodplain context.
- Hazards: [`docs/domains/hazards/README.md`](../../hazards/README.md) — exposure / resilience / declarations.
- People / DNA / Land: [`docs/domains/people-dna-land/README.md`](../../people-dna-land/README.md) — residence, parcel, living-person policy.
- Archaeology: [`docs/domains/archaeology/README.md`](../../archaeology/README.md) — historic-townsite cultural sensitivity.
- Frontier Matrix: [`docs/domains/frontier-matrix/README.md`](../../frontier-matrix/README.md) — Settlement Status hand-off — `TODO`, **NEEDS VERIFICATION**.
- Doctrine: [`docs/doctrine/directory-rules.md`](../../../doctrine/directory-rules.md) — Domain Placement Law (§12).
- Architecture: [`docs/architecture/governed-api.md`](../../../architecture/governed-api.md) — trust-membrane definition.
- ADR: [`docs/adr/ADR-0001-schema-home.md`](../../../adr/ADR-0001-schema-home.md) — schema-home rule.
- Registers: `docs/registers/VERIFICATION_BACKLOG.md`, `docs/registers/DRIFT_REGISTER.md` — destinations for §O items. (`TODO` link targets — verify on mount.)

---

<sub>**Last updated:** 2026-05-19 · **Doc version:** v0.1 (draft) · **Status:** standard doc; sublane structure PROPOSED · **Owners:** Settlements/Infrastructure stewards — `TBD` · [↑ back to top](#settlements--infrastructure--settlements-sublane-dossier)</sub>
