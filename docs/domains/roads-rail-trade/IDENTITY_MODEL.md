<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TBD
title: Roads / Rail / Trade — Identity Model
type: standard
version: v1
status: draft
owners: TBD
created: 2026-05-19
updated: 2026-05-19
policy_label: public
related:
  - docs/domains/roads-rail-trade/README.md
  - docs/standards/PROV.md
  - docs/standards/ISO-19115.md
  - schemas/contracts/v1/transport/  # PROPOSED home; see §24.13 crosswalk
  - control_plane/registers/DRIFT_REGISTER.md
tags: [kfm, domain, roads-rail-trade, identity, governance]
notes:
  - "Initial draft from KFM corpus (Atlas Ch. 13, §24.13; Directory Rules §§3, 12; Pass-10 C1-02)."
  - "No mounted repo, schemas, tests, or runtime were inspected; implementation claims are PROPOSED / NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

# Roads / Rail / Trade — Identity Model

> *How transport objects in KFM are distinguished, hashed, anchored to external authorities, and kept from collapsing into one another across source, time, and release state.*

[![status: draft](https://img.shields.io/badge/status-draft-orange)](#)
[![type: standard](https://img.shields.io/badge/type-standard-blue)](#)
[![domain: roads--rail--trade](https://img.shields.io/badge/domain-roads--rail--trade-9cf)](#)
[![doctrine: governed%20%26%20evidence--first](https://img.shields.io/badge/doctrine-governed%20%26%20evidence--first-success)](#)
[![implementation: PROPOSED](https://img.shields.io/badge/implementation-PROPOSED-lightgrey)](#)
[![last updated: 2026-05-19](https://img.shields.io/badge/updated-2026--05--19-informational)](#)

| Field | Value |
|---|---|
| Status | **draft** |
| Owners | **TBD** *(placeholder — no steward assigned in current session evidence)* |
| Last updated | 2026-05-19 |
| Doctrine basis | KFM Domains Atlas v1.1 Ch. 13 · Pass-10 Idea Index C1-02 · Directory Rules v1.1 §§3, 12 · DDD Reference (Entity / Value Object) |
| Implementation status | **PROPOSED** — repository not mounted this session; no schema, test, or runtime claim is asserted as present |

---

## Mini-TOC

1. [Purpose and scope](#1-purpose-and-scope)
2. [Doctrine basis and authority](#2-doctrine-basis-and-authority)
3. [Identity composition formula](#3-identity-composition-formula)
4. [The `spec_hash` convention](#4-the-spec_hash-convention)
5. [Object families and identity rules](#5-object-families-and-identity-rules)
6. [Temporal kinds and identity invariance](#6-temporal-kinds-and-identity-invariance)
7. [Source role and the anti-collapse rule](#7-source-role-and-the-anti-collapse-rule)
8. [External authority anchors (evidence, not identity)](#8-external-authority-anchors-evidence-not-identity)
9. [Cross-lane identity boundaries](#9-cross-lane-identity-boundaries)
10. [Validators and proof points](#10-validators-and-proof-points)
11. [Open questions and ADR backlog](#11-open-questions-and-adr-backlog)
12. [Related docs](#12-related-docs)
13. [Appendix — illustrative identity envelope](#appendix--illustrative-identity-envelope)

---

## 1. Purpose and scope

**CONFIRMED doctrine / PROPOSED implementation.** This document defines the **identity model** for the Roads / Rail / Trade domain in the Kansas Frontier Matrix (KFM): how every transport object family is distinguished as *the same thing* across evidence sources, time, and release state. It is the governance reference that downstream contracts, schemas, validators, EvidenceBundles, and graph projections in this lane MUST align to.

**In scope.** Identity composition for: `Road Segment`, `Rail Segment`, `CorridorRoute`, `RouteMembership`, `Network Node`, `Crossing`, `Bridge`, `Ferry`, `TransportFacility`, `RestrictionEvent`, `StatusEvent`, `OperatorAssignment`, `Historic RouteClaim`, `TradeRouteCorridor`, and the additional Roads/Rail object inventory of `Depot`, `Siding`, `Yard`, `River Crossing`, `Freight Corridor`, `Route Event`, `Operator Status`, `Access Restriction`, `Network Edge`, and `Movement Story Node`.

**Out of scope.** This document does NOT define rendering, tile production, policy decision flow, release-manifest shape, or correction/rollback mechanics — those live in their own standards. It also does not assign canonical identity for objects owned by adjacent lanes (Settlements, Hydrology, Archaeology, People/Land); see [§9](#9-cross-lane-identity-boundaries).

> [!IMPORTANT]
> "Roads/Rail" is summarized in the Atlas Crosswalk (§24.13) with the headline note **"Network identity governance."** That phrase is this document's reason to exist. Identity, not topology or styling, is the governing concern for this lane.

---

## 2. Doctrine basis and authority

The rules below are CONFIRMED **doctrine** drawn from attached KFM corpus material. Any **implementation** — schema files, validator code, CI workflows, runtime contracts — is PROPOSED until verified against a mounted repository.

| Source | Role in this document | Truth status |
|---|---|---|
| KFM Domains Atlas v1.1 Ch. 13 — Roads/Rail/Trade | Object families, identity rule pattern, temporal-kind doctrine, source-role anti-collapse | CONFIRMED doctrine |
| KFM Domains Atlas v1.1 §24.13 — Atlas↔Dossier↔Responsibility-Root Crosswalk | PROPOSED schema-home placement (`schemas/contracts/v1/transport/`) | CONFIRMED crosswalk note / PROPOSED placement |
| Pass-10 Idea Index C1-02 — Deterministic spec_hash via RFC 8785 JCS + SHA-256 | Hashing convention for the normalized identity envelope | CONFIRMED doctrine |
| Pass-10 Idea Index C1-01 — Universal Run Receipt | Receipt envelope that pins `spec_hash`, source URL, validators | CONFIRMED doctrine |
| Directory Rules v1.1 §§3, 12 — Domain Placement Law | This doc's own placement; domain-as-lane rule | CONFIRMED rule / PROPOSED repo presence |
| DDD Reference — Entity / Value Object | Identity-vs-attribute distinction; "the model must define what it means to be the same thing" | CONFIRMED (external authoritative reference, ingested into KFM doctrine) |
| KFM-P17-IDEA-0005 — Authority IDs and GLO anchors for identity resolution | Authority identifiers carried alongside KFM identity | CONFIRMED card / PROPOSED implementation |
| KFM-P24-IDEA-0004 — Permanent Identifier preference pattern (hydrography example) | Pattern for preferring stable external IDs as **evidence** anchors | CONFIRMED card / PROPOSED implementation |

> [!NOTE]
> The DDD Reference is treated as ingested doctrine (it is an attached project document), not as external research. No web search was performed for this document.

[Back to top](#mini-toc)

---

## 3. Identity composition formula

**CONFIRMED doctrine for the formula; PROPOSED for field-level realization.** Every object family in this lane MUST derive its identity from the same four-part composition, normalized and hashed deterministically:

```text
identity_envelope = ( source_id , object_role , temporal_scope , normalized_digest )
spec_hash         = "jcs:sha256:" + sha256( rfc8785_canonicalize( identity_envelope ) )
```

This is the same composition the Atlas asserts for every transport object family ([§5](#5-object-families-and-identity-rules)), and it is consistent with the identity rule used uniformly across every KFM domain in Atlas v1.1.

```mermaid
flowchart LR
  S["Source<br/>(TIGER, FHWA, KDOT, FRA,<br/>GNIS, OSM, KanDrive, ...)"] --> SD["SourceDescriptor<br/>(source_id + source_role)"]
  SD --> O["Object instance<br/>(Road Segment, Crossing,<br/>RouteMembership, ...)"]
  R["object_role<br/>(role within this family)"] --> O
  T["temporal_scope<br/>(observed / valid / retrieval window,<br/>kept distinct from release time)"] --> O
  O --> N["Normalize<br/>schema · geometry · time ·<br/>identity · evidence · rights · policy"]
  N --> C["RFC 8785 JCS<br/>canonicalize"]
  C --> H["SHA-256"]
  H --> SH["spec_hash<br/>jcs:sha256:<hex>"]
  A["External authority IDs<br/>(TIGER LinearID, FHWA route,<br/>FRA GCIS XingID, GNIS, OSM way,<br/>GLO anchors, ...)"] -. carried as evidence,<br/>NOT identity .-> O
```

**Why these four parts, and not fewer.**

- **`source_id`** disambiguates the same-looking object recorded by two different authorities (e.g., a KDOT segment and a TIGER/Line segment that overlap geometrically but were produced under different roles, vintages, and rights).
- **`object_role`** disambiguates the same source asserting the same thing in two different roles (e.g., the same FHWA layer cited once as an `authority` reference and once as an `aggregate` summary).
- **`temporal_scope`** disambiguates the same source/role across vintages without collapsing history (a Road Segment "as of 2010 TIGER" is not the same identity as the same alignment "as of 2024 TIGER", even if the geometry matches).
- **`normalized_digest`** locks the resolved bytes, so trivial reformatting does not silently mint a new identity — and so re-ingest of the same source at the same vintage produces the same hash.

> [!CAUTION]
> Identity MUST NOT be derived from raw geometry alone. Geometry is admissible **content** but not a sufficient identity, because: (a) two sources can publish the same alignment under different roles and rights; (b) precision and snapping differ across vintages; (c) historic and trade-route geometries are inherently uncertain. Use the four-part envelope, then verify geometry separately.

[Back to top](#mini-toc)

---

## 4. The `spec_hash` convention

**CONFIRMED doctrine.** KFM normalizes the identity envelope and any spec/contract/EvidenceBundle JSON via **RFC 8785 JSON Canonicalization Scheme (JCS)** and then applies **SHA-256**, recording the result as `jcs:sha256:<hex>`. The canonicalization step is what makes the hash deterministic; hashing developer-formatted JSON is explicitly not acceptable, because trivial whitespace or key-order changes would mint different hashes and break re-runs and audits.

**Why this matters for the transport lane specifically.**

- Route designations, restriction events, and operator status are revised frequently. Without canonical hashing, every cosmetic re-export of a KDOT or FHWA layer would invalidate downstream evidence bundles.
- Historic and trade-route claims are merged from multiple low-precision sources; the canonical hash is the only honest way to say "these two normalized envelopes are byte-equivalent."
- Promotion gates (`ValidationReport`, `EvidenceRef`, `PromotionDecision`) are idempotent only if the hash is reproducible.

```text
# CONFIRMED format, illustrative example only — not a sample of a real Roads/Rail object
spec_hash = "jcs:sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
```

> [!NOTE]
> The Pass-10 Index allows **URDNA2015 + SHA-256** as an alternative for graph-shaped JSON-LD content; the choice MUST be recorded in the run receipt. Most Roads/Rail identity envelopes will be plain JSON and use JCS; graph-projection layers may need URDNA2015. *(NEEDS VERIFICATION which projection layers, if any, require URDNA2015 in this lane.)*

[Back to top](#mini-toc)

---

## 5. Object families and identity rules

**CONFIRMED inventory** from Atlas Ch. 13 (Roads/Rail/Trade). The identity rule is the same four-part composition for every family; what varies is the natural object-role vocabulary and the typical authority anchor.

> [!NOTE]
> "Identity rule" below is the **PROPOSED deterministic basis** lifted verbatim from the Atlas: *source id + object role + temporal scope + normalized digest*. Field-name realization (`source_id`, `object_role`, etc.) is illustrative until verified against a mounted schema.

### 5.1 Network primitives

| Object family | Object role examples (illustrative) | Typical authority anchor *(evidence, not identity)* | Identity status |
|---|---|---|---|
| `Road Segment` | drivable_alignment, classified_segment | TIGER LinearID; KDOT segment ID; OSM way (low trust) | PROPOSED deterministic basis (formula §3) |
| `Rail Segment` | active_main, branch, abandoned, industrial_lead | FRA / HIFLD / NTAD rail-line ID | PROPOSED deterministic basis |
| `Network Node` | intersection, junction, terminus, grade_separation | derived; may anchor to TIGER node, OSM node, FRA GCIS where a crossing exists | PROPOSED deterministic basis |
| `Network Edge` | road_to_road, rail_to_rail, intermodal | derived from joined Road/Rail Segments | PROPOSED deterministic basis |

### 5.2 Designations and memberships

| Object family | Object role examples (illustrative) | Authority anchor *(evidence)* | Identity status |
|---|---|---|---|
| `CorridorRoute` | numbered_route, named_route, multi-segment_designation | FHWA route, NHFN corridor, KDOT route number | PROPOSED deterministic basis |
| `RouteMembership` | segment_in_route, time-bounded_membership | derived from a designation source | PROPOSED deterministic basis |
| `Freight Corridor` | NHFN segment, state freight plan corridor | FHWA NHFN | PROPOSED deterministic basis |

> [!IMPORTANT]
> **Designation is not segment, and segment is not designation.** A `Road Segment`'s identity MUST NOT depend on the routes it is a member of — designations change without the underlying alignment changing. `RouteMembership` is the explicit, separately-identified relation. The Atlas lists "Route membership and designation separation tests" as a PROPOSED validator for this lane.

### 5.3 Facilities, crossings, structures

| Object family | Object role examples (illustrative) | Authority anchor *(evidence)* | Identity status |
|---|---|---|---|
| `Crossing` | at-grade_rail_road, pedestrian, private | FRA GCIS Crossing ID | PROPOSED deterministic basis |
| `Bridge` | road_bridge, rail_bridge, pedestrian | NBI structure number; state inventory ID | PROPOSED deterministic basis |
| `Ferry` | vehicle_ferry, historic_ferry | GNIS; state/county records | PROPOSED deterministic basis |
| `River Crossing` | ford, ferry_site, historic_crossing | mixed (Hydrology evidence + transport evidence) | PROPOSED deterministic basis |
| `TransportFacility` | depot, siding, yard, intermodal_terminal | mixed | PROPOSED deterministic basis |
| `Depot` / `Siding` / `Yard` | typed facility | rail-operator records; historic maps | PROPOSED deterministic basis |

### 5.4 Time-bounded events

| Object family | Object role examples (illustrative) | Authority anchor *(evidence)* | Identity status |
|---|---|---|---|
| `RestrictionEvent` | closure, weight_limit, height_limit, hazmat_restriction | KanDrive, county records, WZDx | PROPOSED deterministic basis |
| `StatusEvent` | open, degraded, closed, advisory | KanDrive, WZDx | PROPOSED deterministic basis |
| `OperatorAssignment` | operator_assignment over time | regulatory filings; STB Class I where applicable | PROPOSED deterministic basis |
| `Operator Status` | active, in_receivership, abandoned | regulatory; historic | PROPOSED deterministic basis |
| `Access Restriction` | legal restriction; physical restriction | county/state records | PROPOSED deterministic basis |
| `Route Event` | grand_opening, decommissioning, realignment | historic maps; newspapers; archival | PROPOSED deterministic basis |

### 5.5 Historic and interpretive

| Object family | Object role examples (illustrative) | Authority anchor *(evidence)* | Identity status |
|---|---|---|---|
| `Historic Route` / `Historic RouteClaim` | named_trail, claimed_alignment, oral_corridor | historic maps; GLO; secondary scholarship; oral history *(steward-reviewed)* | PROPOSED deterministic basis |
| `TradeRouteCorridor` | generalized_corridor | mixed | PROPOSED deterministic basis |
| `Movement Story Node` | narrative-anchored point or segment along a route claim | curated | PROPOSED deterministic basis |

> [!WARNING]
> Historic and trade-route identities are especially sensitive. Indigenous trade and mobility corridors, oral history, treaty, cultural, and interpretive evidence default to **steward review and generalized public geometry** per the Atlas Roads/Rail §I. Identity envelopes for these families MUST NOT leak precise location through the digest — generalize the geometry **before** computing the normalized digest, and record the generalization in a `Redaction Receipt`.

[Back to top](#mini-toc)

---

## 6. Temporal kinds and identity invariance

**CONFIRMED doctrine.** The Atlas asserts uniformly for every Roads/Rail object: *"source, observed, valid, retrieval, release, and correction times stay distinct where material."* Identity composition uses only the **identity-relevant** temporal scope; event time and release time are properties of the object, not parts of the identity.

| Temporal kind | Definition | Role in identity? |
|---|---|---|
| `source_time` | When the source authored or published the record | **Part of `temporal_scope`** when the source dates the assertion |
| `observed_time` | When the real-world condition was observed (e.g., a crossing inspection, a closure start) | **Property of the object**, not its identity — a `StatusEvent` has `observed_at` |
| `valid_time` | The interval during which the assertion is asserted to be true | **Part of `temporal_scope`** where vintage matters (e.g., "TIGER 2024 segment") |
| `retrieval_time` | When KFM fetched the bytes | Carried in the run receipt; **not** in identity |
| `release_time` | When KFM published an artifact carrying this object | **Not** in identity — release is a separate state |
| `correction_time` | When a correction was issued | **Not** in identity — corrections produce new descriptors, not re-identified objects |

> [!IMPORTANT]
> Identity does **not** include `release_time` or `correction_time`. Two release manifests pointing at the same `spec_hash` are pointing at the same identity; a corrected object produces a **new** identity envelope and a `CorrectionNotice` linking the prior one. This preserves the corpus invariant that promotion is a governed state transition, not an in-place mutation.

[Back to top](#mini-toc)

---

## 7. Source role and the anti-collapse rule

**CONFIRMED doctrine.** Every source carries a `source_role` field on its `SourceDescriptor`. The Atlas §24.1.3 enumerates the canonical vocabulary; for Roads/Rail the seven roles apply as follows.

| `source_role` | Typical Roads/Rail example | Notes |
|---|---|---|
| `observed` | KanDrive incident; field bridge inspection | Direct observation evidence |
| `regulatory` | FHWA HPMS extract; NHFN designation | Authority assertion, not observation |
| `modeled` | Travel-time model; freight-flow estimate | Pin model run via `role_model_run_ref` |
| `aggregate` | County-level VMT; HUC-corridor summary | Pin `role_aggregation_unit` |
| `administrative` | Government compilation, e.g., a published "historic routes" booklet | Treat as compilation, NOT timeline of observed events |
| `candidate` | OSM way; crowdsourced trail | Default-deny public surface until promotion |
| `synthetic` | AI-generated narrative; reconstructed alignment | Reality Boundary Note required |

> [!CAUTION]
> **Anti-collapse rule for Roads/Rail (CONFIRMED doctrine).** Per the Atlas drift inventory, an "Administrative compilation cited as observation" → **DENY** publication of compilation as observed event timeline. In identity terms: an `administrative` source MUST NOT mint identities of role `observed`. The `source_role` is part of the identity envelope precisely to make this collapse impossible at the hash layer.

`source_role` is set at admission and never edited in place. Corrections produce a **new** SourceDescriptor and a `CorrectionNotice`; the prior identity is preserved for audit.

[Back to top](#mini-toc)

---

## 8. External authority anchors (evidence, not identity)

**CONFIRMED principle / PROPOSED field realization.** Stable external identifiers — TIGER LinearIDs, FHWA route designations, FRA GCIS crossing IDs, NBI structure numbers, GNIS feature IDs, OSM way IDs, GLO patent anchors — are carried on KFM objects as **evidence**, not as canonical identity. This mirrors the Pass-32 pattern asserted for hydrography (KFM-P24-IDEA-0004: prefer the NHDPlus HR Permanent Identifier over COMID, but carry both as evidence) and the broader Pass-23 pattern (KFM-P17-IDEA-0005: combine authority identifiers, GLO anchors, co-mentions, and negative evidence into a **deterministic confidence band**).

| External anchor | Source family | Typical KFM use |
|---|---|---|
| TIGER `LINEARID` / `MTFCC` | Census TIGER/Line | Roads, road class crosswalk |
| FHWA route number / NHFN ID | FHWA HPMS / NHFN | `CorridorRoute`, `Freight Corridor` |
| FRA GCIS Crossing ID | FRA GCIS | `Crossing` |
| NBI structure number | National Bridge Inventory *(NEEDS VERIFICATION as a named KFM source)* | `Bridge` |
| KDOT route / segment ID | KDOT / KanPlan / KanDrive | `Road Segment`, `RestrictionEvent`, `StatusEvent` |
| GNIS feature ID | GNIS | `Ferry`, named historic features |
| OSM way / node ID | OpenStreetMap | candidate-role evidence only |
| GLO patent anchor | GLO records *(via People/DNA/Land cross-citation)* | `Historic RouteClaim` co-anchor |

> [!NOTE]
> **Why external IDs are evidence, not identity.** External authorities can re-issue, retire, merge, or split their IDs without notifying KFM. If KFM identity were defined by an external ID, then an upstream renumbering would silently mint or destroy KFM identities. Treating the external ID as evidence carried inside the identity envelope (and surfaced via the `EvidenceBundle`) keeps KFM identity stable under upstream churn while preserving the ability to cite the upstream record.

[Back to top](#mini-toc)

---

## 9. Cross-lane identity boundaries

**CONFIRMED doctrine** from Atlas Ch. 13 §B and §F. Roads/Rail does not own identities that belong to adjacent lanes. Cross-lane evidence is carried, but identity authority stays with the owning domain.

| Roads/Rail object | Adjacent lane | Identity authority | Roads/Rail carries |
|---|---|---|---|
| `Crossing`, `Bridge`, `Ferry`, `River Crossing` | Hydrology | Hydrology owns water evidence (e.g., reach, HUC) | A reference to Hydrology identity; the **crossing/bridge identity itself stays in Roads/Rail** |
| `TransportFacility`, `Depot`, `Yard`, intermodal hubs | Settlements / Infrastructure | Settlements owns settlement and infrastructure canonical claims | A reference where the facility is also an infrastructure asset; Roads/Rail keeps the *transport-role* identity |
| `Historic RouteClaim`, `TradeRouteCorridor`, Indigenous corridors | Archaeology / Cultural Heritage | Archaeology retains sensitivity policy and steward review | Generalized geometry, steward-reviewed; ABSTAIN/DENY where review state is unresolved |
| `RestrictionEvent` driven by flood/fire/smoke | Hazards | Hazards owns the hazard event identity | A relation linking the closure to the hazard; not a re-identified hazard |
| Historic alignments crossing patented land | People / Genealogy / DNA / Land | People/Land owns LandInstrument and patent identity | An evidence-only co-citation through GLO anchors |

> [!IMPORTANT]
> When a transport object's identity-relevant evidence comes primarily from another lane (e.g., a `River Crossing` whose existence is asserted by a Hydrology source), the Roads/Rail identity envelope MUST still be a Roads/Rail envelope — `source_id` may point at a Hydrology source, but `object_role` and the family stay in this lane. Cross-lane evidence does not relocate identity ownership.

[Back to top](#mini-toc)

---

## 10. Validators and proof points

**PROPOSED.** The Atlas Roads/Rail §K names the following validator targets. None are asserted as implemented in a mounted repo this session.

- [ ] Route membership and designation separation tests
- [ ] Operator / status temporal tests
- [ ] OSM / GNIS legal-status denial *(deny promotion of crowdsourced sources past WORK without explicit policy)*
- [ ] Historic overprecision denial *(deny publication of historic alignments at higher precision than evidence supports)*
- [ ] Public generalization receipt tests
- [ ] Transport graph projection rollback tests

Identity-specific proof points this document implies (PROPOSED additions to the validator surface):

- [ ] **Canonical-hash reproducibility test.** Re-canonicalizing the same identity envelope on two implementations produces identical `jcs:sha256:<hex>`.
- [ ] **Role-anti-collapse test.** An `administrative` source cannot produce an identity envelope whose `object_role` is observed-only.
- [ ] **Vintage-distinction test.** The same alignment from two TIGER vintages produces two distinct `spec_hash` values.
- [ ] **External-anchor-as-evidence test.** Changing an upstream external ID (e.g., TIGER `LINEARID` renumbering) without changing the identity envelope does NOT mint a new KFM identity, but DOES emit a `CorrectionNotice` recording the upstream change.
- [ ] **Cross-lane non-leak test.** A Hydrology-owned identity cannot appear as a Roads/Rail canonical identity.

> [!NOTE]
> These tests are PROPOSED and their schema homes are PROPOSED. The Atlas §24.13 places the transport schema home at `schemas/contracts/v1/transport/`; Directory Rules §12 expresses the same lane pattern as `schemas/contracts/v1/domains/<domain>/`. See [§11](#11-open-questions-and-adr-backlog) for the unresolved naming conflict.

[Back to top](#mini-toc)

---

## 11. Open questions and ADR backlog

| # | Open question | Why it matters | Resolution path |
|---|---|---|---|
| OQ-01 | Schema-home naming: `schemas/contracts/v1/transport/` (Atlas §24.13) vs. `schemas/contracts/v1/domains/roads-rail-trade/` (Directory Rules §12 lane pattern). | Two doctrinal sources disagree on the literal segment name. NEEDS VERIFICATION against mounted repo + ADR. | Open ADR; record in `control_plane/registers/DRIFT_REGISTER.md` per Directory Rules §2.5 |
| OQ-02 | Canonical name of the run-receipt/provenance standard (`PROV.md` vs `PROVENANCE.md`). | Identity envelopes are recorded in run receipts; the file name is referenced by this doc. | Open ADR (already flagged in standards-docs corpus) |
| OQ-03 | Are URDNA2015 + SHA-256 hashes required for any Roads/Rail graph-projection layer, or is JCS sufficient throughout? | Affects validator implementation and reproducibility tests. | NEEDS VERIFICATION against the graph projection contract once mounted |
| OQ-04 | Field-name canonical form (`source_id`/`source_role`/`object_role`/`temporal_scope`/`normalized_digest` vs. existing or in-flight schema vocabulary). | Field names in this doc are illustrative; the canonical names live in the schema. | Cross-check against `schemas/contracts/v1/<...>/source-descriptor.json` (PROPOSED home) once mounted |
| OQ-05 | Treatment of OSM as a `candidate` source: is there a domain-specific promotion rule for OSM road segments that meet an evidence threshold? | The Atlas calls for "OSM/GNIS legal-status denial" as a validator; the threshold rule is not specified. | Open ADR scoped to the Roads/Rail policy lane |
| OQ-06 | Does `Movement Story Node` participate in the same identity formula or as a narrative-overlay value object without independent identity? | DDD distinction (entity vs. value object) matters for graph projections. | Document decision in this file once steward review confirms |
| OQ-07 | NBI structure number as a named KFM source family for `Bridge` identity. | Currently asserted in this doc only as illustrative; not in the Atlas Ch. 13 §D source-family list. | NEEDS VERIFICATION against source registry |

[Back to top](#mini-toc)

---

## 12. Related docs

> [!NOTE]
> Links below are PROPOSED targets; verify presence against a mounted repo before publication. Where a target may not yet exist, the link is a planning placeholder.

- [`docs/domains/roads-rail-trade/README.md`](./README.md) — *Roads/Rail/Trade lane landing page (PROPOSED)*
- [`docs/standards/PROV.md`](../../standards/PROV.md) — *Provenance standard profile; run-receipt vocabulary*
- [`docs/standards/ISO-19115.md`](../../standards/ISO-19115.md) — *Geospatial metadata crosswalk target*
- [`docs/standards/OAI-PMH.md`](../../standards/OAI-PMH.md) — *Harvest-side provenance interface*
- [`docs/standards/CANONICALIZATION.md`](../../standards/CANONICALIZATION.md) — *JCS vs URDNA2015 decision matrix (PROPOSED / NEEDS VERIFICATION)*
- [`control_plane/registers/DRIFT_REGISTER.md`](../../../control_plane/registers/DRIFT_REGISTER.md) — *Where to file the schema-home naming conflict (OQ-01)*
- [`schemas/contracts/v1/transport/`](../../../schemas/contracts/v1/transport/) — *PROPOSED schema home for transport contracts; NEEDS VERIFICATION*

---

## Appendix — illustrative identity envelope

> [!NOTE]
> The block below is **illustrative**. Field names are not drawn from a verified schema; they show the four-part composition this document specifies. Replace with canonical field names from `schemas/contracts/v1/.../source-descriptor.json` once that schema is mounted.

<details>
<summary><b>Illustrative `Road Segment` identity envelope (pseudo-JSON, not from a verified schema)</b></summary>

```json
{
  "object_family": "Road Segment",
  "source_id": "kfm:source:tiger-line:2024:ks",
  "source_role": "regulatory",
  "object_role": "drivable_alignment",
  "temporal_scope": {
    "source_time": "2024-01-01",
    "valid_time": { "start": "2024-01-01", "end": null }
  },
  "normalized_digest": {
    "method": "rfc8785-jcs+sha256",
    "value": "jcs:sha256:<computed-over-canonical-envelope>"
  },
  "evidence_anchors": {
    "tiger_linearid": "1104755123456",
    "kdot_segment_id": null,
    "fhwa_route": null,
    "osm_way": null
  },
  "spec_hash": "jcs:sha256:<computed-over-the-whole-envelope-minus-spec_hash>",
  "release_state": "not_released",
  "notes": "Illustrative only. Field names are PROPOSED; verify against mounted schema."
}
```

</details>

<details>
<summary><b>Illustrative `Crossing` (rail/road, FRA GCIS-anchored)</b></summary>

```json
{
  "object_family": "Crossing",
  "source_id": "kfm:source:fra-gcis:2025-snapshot",
  "source_role": "regulatory",
  "object_role": "at_grade_rail_road",
  "temporal_scope": {
    "source_time": "2025-Q1",
    "valid_time": { "start": "2025-01-01", "end": null }
  },
  "normalized_digest": {
    "method": "rfc8785-jcs+sha256",
    "value": "jcs:sha256:<computed>"
  },
  "evidence_anchors": {
    "fra_gcis_xing_id": "<XingID>",
    "tiger_linearid": null
  },
  "cross_lane_refs": {
    "hydrology": null
  },
  "spec_hash": "jcs:sha256:<computed>",
  "release_state": "not_released",
  "notes": "Illustrative only."
}
```

</details>

<details>
<summary><b>Illustrative `Historic RouteClaim` (steward-reviewed, generalized geometry)</b></summary>

```json
{
  "object_family": "Historic RouteClaim",
  "source_id": "kfm:source:glo-anchors+secondary-scholarship:bundle-001",
  "source_role": "administrative",
  "object_role": "claimed_alignment",
  "temporal_scope": {
    "source_time": "secondary-scholarship-1968",
    "valid_time": { "start": "1825", "end": "1872" }
  },
  "normalized_digest": {
    "method": "rfc8785-jcs+sha256",
    "value": "jcs:sha256:<computed-over-generalized-geometry>"
  },
  "evidence_anchors": {
    "glo_patent_refs": [ "<patent-id-1>", "<patent-id-2>" ],
    "secondary_scholarship_refs": [ "<citation>" ]
  },
  "sensitivity": {
    "steward_review_required": true,
    "generalization_applied": true,
    "redaction_receipt_ref": "<receipt-id>"
  },
  "spec_hash": "jcs:sha256:<computed>",
  "release_state": "review_required",
  "notes": "Illustrative only. Generalization MUST precede digest. Indigenous corridors and oral-history evidence default to DENY/HOLD."
}
```

</details>

---

**Doctrine status:** CONFIRMED. **Implementation status:** PROPOSED (repository not mounted this session).

### Related docs · Last updated · Back to top

- See [§12 Related docs](#12-related-docs).
- **Last updated:** 2026-05-19
- [Back to top](#roads--rail--trade--identity-model)
