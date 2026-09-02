# `schemas/contracts/v1/facilities/` — Facilities Schema Family Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-facilities-readme
title: schemas/contracts/v1/facilities/ — Facilities Schema Family Index
type: readme; schema-family-index; facilities-governance-boundary
authority_class: schema-family-index
version: v0.1
status: draft; empty-family-index; proposed-schema-family; no-current-schema-files-found; cross-domain-boundary-sensitive; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Facilities steward
  - OWNER_TBD — Settlements/Infrastructure steward
  - OWNER_TBD — Roads/Rail/Trade steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; facilities; infrastructure; transport-facility; public-facility; asset-identity; source-role-aware; lifecycle-aware; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, facilities, infrastructure, settlements-infrastructure, roads-rail-trade, transport-facility, depot, station, yard, terminal, facility-role, public-facility, asset-identity, evidence, policy, release]
related:
  - ../README.md
  - ../domains/settlements-infrastructure/README.md
  - ../domains/roads-rail-trade/README.md
  - ../../../../contracts/domains/roads-rail-trade/transport_facility.md
  - ../../../../contracts/domains/roads-rail-trade/depot.md
  - ../../../../docs/domains/settlements-infrastructure/README.md
  - ../../../../docs/domains/settlements-infrastructure/sublanes/settlements.md
  - ../../../../docs/domains/settlements-infrastructure/EXPANSION_BACKLOG.md
  - ../../../../docs/domains/roads-rail-trade/README.md
  - ../../../../docs/domains/roads-rail-trade/CANONICAL_PATHS.md
  - ../../../../policy/domains/settlements-infrastructure/
  - ../../../../policy/domains/roads-rail-trade/
  - ../../../../fixtures/domains/settlements-infrastructure/
  - ../../../../fixtures/domains/roads-rail-trade/
  - ../../../../tests/domains/settlements-infrastructure/
  - ../../../../tests/domains/roads-rail-trade/
  - ../../../../release/candidates/settlements-infrastructure/
  - ../../../../release/candidates/roads-rail-trade/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/facilities/README.md."
  - "GitHub search did not surface existing schema files under schemas/contracts/v1/facilities/ beyond this README in the current check."
  - "Search did surface contracts/domains/roads-rail-trade/transport_facility.md, which states its paired schema was not found and distinguishes transport-facility role claims from canonical place/facility identity."
  - "Settlements/Infrastructure docs distinguish place/community identity from infrastructure assets, networks, facilities, service areas, operators, condition observations, and dependencies."
  - "This README is a proposed cross-domain schema-family index, not proof that facilities should be a top-level schema family rather than domain-specific schema lanes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-facilities-purple)
![shape](https://img.shields.io/badge/authority-machine--shape-informational)
![maturity](https://img.shields.io/badge/maturity-empty__family__index-orange)
![boundary](https://img.shields.io/badge/boundary-cross--domain-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/facilities/` is a proposed schema-family home for machine-checkable shapes that describe facility-like assets, sites, service points, terminals, depots, stations, yards, public facilities, and facility-role relations when those shapes are cross-domain and do not belong more specifically under a domain schema lane.
>
> **One-line boundary.** This folder may define facility object **shape**. It does not certify canonical place identity, property title, structural condition, legal access, active service, operational authority, map truth, publication approval, or public-safe exposure.

---

## Quick jumps

[Status](#status) · [Authority and placement](#authority-and-placement) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Candidate schemas](#candidate-schemas) · [Cross-domain boundaries](#cross-domain-boundaries) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Schema-family rules](#schema-family-rules) · [Promotion checklist](#promotion-checklist) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/facilities/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are facilities schema files currently present in this folder? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Is `facilities/` already proven as a first-class schema family? | Not proven. Treat as proposed until ADR/schema-steward review. | **PROPOSED / NEEDS VERIFICATION** |
| Is there related facility doctrine elsewhere? | Yes. Search surfaced Roads/Rail/Trade `transport_facility` contract and Settlements/Infrastructure docs discussing facilities/assets boundaries. | **CONFIRMED related evidence** |
| Can this folder decide canonical facility identity or publication status? | No. It can only define machine-checkable shape if accepted. | **CONFIRMED boundary** |
| Should new schemas be added here without review? | No. Facilities cut across domains, so schema placement must be reviewed before adding authority. | **PROPOSED discipline** |

> [!IMPORTANT]
> Facilities are cross-domain and boundary-sensitive. A depot, school, hospital, station, yard, rest area, water tower, substation, terminal, bridge-adjacent site, or public-service asset may carry different meanings in different lanes. Do not collapse role claims, canonical asset identity, operator status, public access, condition, property title, and publication authority into one object.

---

## Authority and placement

This folder is under the schema responsibility root:

```text
schemas/contracts/v1/facilities/
```

That means it may only own machine-checkable shape. Adjacent authority is split:

- `contracts/` owns human-readable facility meaning.
- `docs/domains/settlements-infrastructure/` owns settlements/infrastructure doctrine and facility/asset context.
- `docs/domains/roads-rail-trade/` owns transport-route and transport-facility-role context.
- `schemas/contracts/v1/domains/<domain>/` owns domain-specific facility shapes when the primary responsibility is a domain lane.
- `policy/` owns sensitivity, access, rights, and exposure decisions.
- `fixtures/` and `tests/` prove valid/invalid behavior.
- `data/` owns lifecycle payloads, registries, receipts, proofs, catalog, triplets, and published artifacts.
- `release/` owns promotion, release manifests, correction, withdrawal, and rollback decisions.

This README does not amend ADR-0001, Directory Rules, domain canonical-path decisions, or any future facility-family ADR.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── domains/
        │   ├── settlements-infrastructure/             # domain-specific infrastructure/settlement shapes
        │   └── roads-rail-trade/                       # domain-specific transport role shapes
        └── facilities/
            └── README.md                               # this file; proposed empty-family index

contracts/
└── domains/
    └── roads-rail-trade/
        ├── transport_facility.md                       # related role contract; schema noted missing
        └── depot.md                                    # related transport facility type

docs/
├── domains/
│   ├── settlements-infrastructure/                     # facilities/assets/service-area domain context
│   └── roads-rail-trade/                               # transport facility-role context
policy/
fixtures/
tests/
release/
```

---

## Current inventory

Current check:

| Path | Status | Note |
|---|---|---|
| `schemas/contracts/v1/facilities/README.md` | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/facilities/*.schema.json` | **Not found in current search** | Treat family as proposed/empty until a mounted checkout or schema registry proves otherwise. |

Related surfaced files outside this folder:

| Related path | Why it matters |
|---|---|
| `contracts/domains/roads-rail-trade/transport_facility.md` | Defines a transport-facility role claim and explicitly notes its paired schema was not found in that task. |
| `contracts/domains/roads-rail-trade/depot.md` | Related transport facility subtype. |
| `docs/domains/settlements-infrastructure/sublanes/settlements.md` | Distinguishes settlement/place identity from infrastructure assets, networks, facilities, service areas, operators, condition observations, and dependencies. |
| `data/registry/settlements-infrastructure/README.md` | Related registry lane surfaced by search; maturity not inspected here. |
| `docs/domains/settlements-infrastructure/EXPANSION_BACKLOG.md` | Related backlog surfaced by search; maturity not inspected here. |

---

## Candidate schemas

The following are candidates only. Do not add them without paired contracts, fixture plan, validator plan, and steward review.

| Candidate schema | Purpose | Likely ownership question | Status |
|---|---|---|---|
| `facility_identity.schema.json` | Canonical cross-domain facility identity envelope. | Does it belong here or under `domains/settlements-infrastructure/`? | **PROPOSED / NEEDS VERIFICATION** |
| `facility_role.schema.json` | Role assertion that a facility functioned as depot, station, terminal, yard, rest area, port-of-entry, etc. | Could belong under Roads/Rail/Trade if transport-specific. | **PROPOSED / NEEDS VERIFICATION** |
| `transport_facility.schema.json` | Shape paired to Roads/Rail/Trade `transport_facility` semantic contract. | Likely domain lane: `schemas/contracts/v1/domains/roads-rail-trade/`. | **PROPOSED / placement-sensitive** |
| `public_facility.schema.json` | Public-service facility shape for school, hospital, civic building, office, emergency/service site, etc. | May require sensitivity/access review. | **PROPOSED / NEEDS VERIFICATION** |
| `facility_status_event.schema.json` | Time-scoped open/closed/active/inactive/abandoned/damaged/service status. | Avoid claiming live service authority. | **PROPOSED / NEEDS VERIFICATION** |
| `facility_operator_assignment.schema.json` | Time-scoped operator or managing organization relation. | Must not certify legal authority unless source supports it. | **PROPOSED / NEEDS VERIFICATION** |
| `facility_condition_observation.schema.json` | Evidence-scoped condition observation for a facility or asset. | May belong in infrastructure domain lane; condition-sensitive. | **PROPOSED / NEEDS VERIFICATION** |
| `facility_access_restriction.schema.json` | Time-scoped public/private/restricted/unknown access relation. | Policy/access/law-sensitive; fail closed. | **PROPOSED / NEEDS VERIFICATION** |
| `facility_layer_descriptor.schema.json` | Public-safe layer descriptor for facility map presentation. | Must reference release, evidence, and policy. | **PROPOSED / NEEDS VERIFICATION** |

> [!CAUTION]
> The presence of a candidate here does not mean it belongs here. If the object is domain-specific, place it under the domain schema lane. Use `facilities/` only when the primary responsibility is a reusable cross-domain facility shape.

---

## Cross-domain boundaries

| Boundary | Rule |
|---|---|
| Settlement/place identity | A facility can be related to a settlement, municipality, townsite, fort, mission, or reservation community, but should not overwrite place/community identity. |
| Infrastructure asset identity | Canonical asset/facility identity likely belongs with Settlements/Infrastructure unless a cross-family ADR says otherwise. |
| Transport role | Depot, station, yard, terminal, rest area, weigh station, port-of-entry, and interchange roles may belong to Roads/Rail/Trade when the claim is route/network-role-specific. |
| Property/title | Facility schema shape must not certify property ownership, title, parcel boundary, legal access, or right-of-way. |
| Live operation | Facility schema shape must not certify live service status, emergency status, inspection status, or operational authority without time-scoped source evidence and policy/release review. |
| Sensitive infrastructure | Critical infrastructure, emergency facilities, utilities, shelters, restricted facilities, archaeology-adjacent facilities, and precise sensitive locations require policy review and may require redaction/generalization/denial. |
| Public map display | A facility layer is a released projection, not canonical facility truth. |

---

## What belongs here

- This README.
- Cross-domain facility-family JSON Schema files after contract/schema review.
- Machine-readable shapes for generic facility identity, facility role, facility status event, facility operator assignment, facility access restriction, and facility layer descriptors when they do not belong more specifically under a domain lane.
- Migration notes, mirror notices, and deprecation notes for facility schema placement.
- Links to paired contracts, fixtures, validators, policy profiles, source registry records, EvidenceBundle references, release references, correction/withdrawal records, rollback cards, and tests.

---

## What does not belong here

- Semantic contract prose.
- Domain-specific facility schemas that should live under `schemas/contracts/v1/domains/<domain>/`.
- Policy rules, access-control logic, sensitivity decisions, redaction decisions, or exposure decisions.
- Source payloads, SourceDescriptor records, registry records, receipts, proofs, catalog records, triplets, or lifecycle data as emitted data.
- Release approvals, release manifests, correction notices, withdrawal notices, or rollback cards as records.
- Runtime/API implementation code.
- Map tiles, public exports, dashboards, screenshots, or generated summaries.
- Claims of canonical identity, structural condition, legal access, active service, property title, operating authority, public safety status, or publication approval merely because an object validates against a schema.

---

## Schema-family rules

| Rule | Requirement |
|---|---|
| Cross-domain placement | Use this folder only for reusable facility shapes. Use domain lanes for domain-specific facility meanings. |
| Role separation | Facility role claims must remain separate from canonical facility identity. |
| Time scoping | Status, operator, service, access, condition, and role claims must be time-scoped where material. |
| Source-role preservation | A source claim, interpretation, derived layer, and released public artifact must not collapse into one object. |
| Evidence dependency | Facility claims should reference EvidenceRef/EvidenceBundle where they support public claims or released artifacts. |
| Policy dependency | Sensitive facility locations, restricted facilities, critical infrastructure, emergency/public-safety facilities, and living-person-adjacent facilities require policy and sensitivity review. |
| Release dependency | Public facility layers require release manifests, correction path, and rollback targets. |
| No live-authority claim | KFM facility schemas must not imply live emergency, safety, service, access, or inspection authority without explicit bounded source and policy/release posture. |
| No parallel authority | Do not duplicate transport, settlements-infrastructure, release, policy, or evidence schemas here without ADR/migration notes. |

---

## Promotion checklist

A facility schema should not advance beyond `PROPOSED` unless:

- [ ] Primary responsibility is cross-domain facility shape, not a domain-specific object family.
- [ ] Paired semantic contract exists or is explicitly marked **NEEDS VERIFICATION**.
- [ ] `$id` and filename are stable.
- [ ] JSON Schema dialect is pinned.
- [ ] Valid fixtures exist.
- [ ] Invalid fixtures exist.
- [ ] Validator implementation exists.
- [ ] CI/schema-test support exists.
- [ ] Source-role, temporal, evidence, policy, release, correction, and rollback fields are explicit where material.
- [ ] Sensitive facility cases are tested for denial, restriction, generalization, or redaction.
- [ ] Transport-facility role vs canonical facility identity is tested.
- [ ] Public-facing layer/API consumers are version-aware if they use the schema.

---

## Validation

Recommended local validation sequence:

```bash
# Inspect current facilities schema family.
find schemas/contracts/v1/facilities -maxdepth 2 -type f | sort

# Look for possible duplicate facility authority elsewhere.
find schemas/contracts/v1 contracts docs/domains policy fixtures tests -maxdepth 6 -type f \
  | grep -Ei 'facility|facilities|depot|station|yard|terminal|infrastructure|operator|condition|access_restriction' \
  | sort

# Validate JSON syntax once schemas exist.
find schemas/contracts/v1/facilities -name '*.schema.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/domains tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/facilities/README.md`.

Rollback for future facility schemas requires checking every downstream reference:

1. Revert or migrate the schema file.
2. Revert or update paired semantic contracts.
3. Revert or update fixtures and validators.
4. Revert or update schema registry entries.
5. Revert or update domain schemas that reference facility shapes.
6. Revert or update governed API payloads, public UI payloads, MapLibre layer descriptors, Evidence Drawer payloads, and public export manifests.
7. Preserve correction/withdrawal/rollback records for any public facility surface affected by schema changes.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should `facilities/` be a first-class schema family, or should all facility shapes live under domain schema lanes? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + domain stewards |
| Should `transport_facility.schema.json` live here or under `schemas/contracts/v1/domains/roads-rail-trade/`? | **NEEDS VERIFICATION** | Roads/Rail/Trade steward + schema steward |
| What is the accepted schema home for infrastructure-owned facility identity? | **NEEDS VERIFICATION** | Settlements/Infrastructure steward |
| Which facility types are sensitive enough to require redaction/generalization or denial by default? | **NEEDS VERIFICATION** | Policy steward + security steward |
| Which fixtures prove role-vs-identity separation? | **NEEDS VERIFICATION** | Validation steward |
| Which public API, MapLibre, Evidence Drawer, or Focus Mode payloads need facility schemas? | **NEEDS VERIFICATION** | API/UI steward |
| Which release and rollback records should facility layers reference? | **NEEDS VERIFICATION** | Release steward |

---

## Maintainer notes

- Keep this folder empty except for this README until the facility family is accepted or a specific schema is reviewed.
- Do not use this folder to bypass domain lane ownership.
- Preserve facility-role vs facility-identity separation.
- Public facility display requires evidence, policy, sensitivity review, release state, correction path, and rollback target; schema validity alone is never enough.
