# `schemas/contracts/v1/domains/transport/` — Transport Schema Lane README

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-transport-readme
title: schemas/contracts/v1/domains/transport/ — Transport Schema Lane README
type: readme; schema-lane-readme; path-conflict-register
version: v0.1
status: draft; PATH-CONFLICTED; existing-empty-file-expanded; do-not-promote-until-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Roads / Rail / Trade domain steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; transport; roads-rail-trade; path-conflicted; source-role-aware; evidence-bound; lifecycle-aware; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, domains, transport, roads-rail-trade, road-segment, route, network-edge, bridge, crossing, restriction-event, status-event, evidence-bundle, decision-envelope, path-conflict]
related:
  - ../../../../README.md
  - ../../../../../contracts/domains/transport/road-segment.md
  - ../../../../../schemas/contracts/v1/domains/transport/road-segment.schema.json
  - ../../../../../docs/domains/roads-rail-trade/CANONICAL_PATHS.md
  - ../../../../../docs/domains/roads-rail-trade/ARCHITECTURE.md
  - ../../../../../docs/domains/roads-rail-trade/API_CONTRACTS.md
  - ../../../../../docs/domains/roads-rail-trade/DATA_LIFECYCLE.md
  - ../../../../../policy/domains/roads-rail-trade/
  - ../../../../../fixtures/domains/roads-rail-trade/
  - ../../../../../tests/domains/roads-rail-trade/
  - ../../../../../release/candidates/roads-rail-trade/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/domains/transport/README.md."
  - "This path is CONFIRMED present in the repository, but current Roads/Rail/Trade canonical-path doctrine says schemas/contracts/v1/domains/transport/ is a fabricated hybrid not produced by either doctrine source."
  - "This README exists to document the conflict, prevent silent promotion, and index any existing schema scaffold files until ADR resolution."
  - "Do not add new transport schema authority here unless an accepted ADR selects this path or explicitly authorizes a transitional/mirror lane."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![path](https://img.shields.io/badge/path-CONFLICTED-red)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-transport-blue)
![lane](https://img.shields.io/badge/lane-roads--rail--trade-slategray)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)
![promotion](https://img.shields.io/badge/promotion-blocked__until__ADR-orange)

> **Purpose.** This README documents the existing `schemas/contracts/v1/domains/transport/` schema lane as a **path-conflicted, draft, non-promoted** home for transport / Roads-Rail-Trade schema scaffolds.
>
> **One-line boundary.** This folder may index existing schema scaffolds, but it must not become canonical transport schema authority until the Roads/Rail/Trade slug and `domains/`-segment conflict is resolved by ADR.

---

## Quick jumps

[Status](#status) · [Path conflict](#path-conflict) · [Scope](#scope) · [Repo fit](#repo-fit) · [Current schema inventory](#current-schema-inventory) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Schema-lane rules](#schema-lane-rules) · [Transport object candidates](#transport-object-candidates) · [Support-type separation](#support-type-separation) · [Review checklist](#review-checklist) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/domains/transport/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Does this folder have at least one schema scaffold? | Yes: `road-segment.schema.json` exists. | **CONFIRMED** |
| Is `road-segment.schema.json` field-complete? | No evidence. Opened schema is a permissive `PROPOSED` scaffold with empty `properties` and `additionalProperties: true`. | **NEEDS VERIFICATION** |
| Is this path canonical? | Not yet. Current Roads/Rail/Trade path registry labels `schemas/contracts/v1/domains/transport/` as a fabricated hybrid that appears in neither doctrine source. | **PATH-CONFLICTED** |
| Should new schema authority be added here? | No, not until an accepted ADR selects this path, authorizes a mirror, or records a migration. | **DENY / ADR-required** |
| Does this README validate data or release a public layer? | No. It is documentation and conflict indexing only. | **CONFIRMED** |

> [!CAUTION]
> This README is intentionally not a promotion of the path. It is a guardrail around an already-present folder so the repo does not silently treat the hybrid path as settled authority.

---

## Path conflict

The current repository contains this README at:

```text
schemas/contracts/v1/domains/transport/README.md
```

The paired existing schema scaffold is:

```text
schemas/contracts/v1/domains/transport/road-segment.schema.json
```

However, the Roads / Rail / Trade canonical-path registry records a two-axis conflict:

1. **`domains/` segment conflict:** Directory Rules-style schema homes include `domains/`; Atlas-style schema homes omit it.
2. **Slug conflict:** Directory Rules-style lane naming uses `roads-rail-trade`; Atlas row 13 uses `transport`.

That produces two doctrine-supported diagonal forms and two hybrid forms:

| Pattern | Example | Status |
|---|---|---|
| Directory Rules-style form | `schemas/contracts/v1/domains/roads-rail-trade/` | **PROPOSED / real doctrine form** |
| Atlas-style form | `schemas/contracts/v1/transport/` | **PROPOSED / real doctrine form** |
| Hybrid with `domains/` + `transport` | `schemas/contracts/v1/domains/transport/` | **CONFIRMED present / PATH-CONFLICTED** |
| Hybrid without `domains/` + `roads-rail-trade` | `schemas/contracts/v1/roads-rail-trade/` | **Not selected / unsupported unless ADR says otherwise** |

> [!WARNING]
> Do not create a second road-segment schema in another home just to avoid this conflict. Resolve the conflict through ADR/migration, then move, mirror, or deprecate with a receipt and rollback plan.

---

## Scope

This README may document:

- existing schema scaffolds under this folder;
- the transport / Roads-Rail-Trade schema-home conflict;
- migration notes and ADR pointers;
- links to paired semantic contracts, fixtures, validators, policy, release, rollback, and docs;
- explicit `NEEDS VERIFICATION` status for schema maturity.

This README must not claim that any transport schema under this path is canonical, field-complete, validated, released, wired to CI, consumed by a public API, rendered by MapLibre, or safe for public publication unless separately proven by repo evidence.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        └── domains/
            └── transport/
                ├── README.md                         # this file; PATH-CONFLICTED guardrail
                └── road-segment.schema.json          # CONFIRMED scaffold; field maturity NEEDS VERIFICATION

contracts/
└── domains/
    └── transport/
        └── road-segment.md                           # paired semantic contract; also path-conflicted

docs/
└── domains/
    └── roads-rail-trade/
        ├── CANONICAL_PATHS.md                        # source of slug/path conflict warning
        ├── ARCHITECTURE.md
        ├── API_CONTRACTS.md
        └── DATA_LIFECYCLE.md

policy/
└── domains/
    └── roads-rail-trade/                             # policy lane; maturity NEEDS VERIFICATION

fixtures/
└── domains/
    └── roads-rail-trade/                             # examples and validator inputs; maturity NEEDS VERIFICATION

tests/
└── domains/
    └── roads-rail-trade/                             # proof lane; maturity NEEDS VERIFICATION

release/
└── candidates/
    └── roads-rail-trade/                             # release-candidate lane; maturity NEEDS VERIFICATION
```

The current repo therefore uses `transport` in at least one schema/contract path while the human-facing domain docs use `roads-rail-trade`. Keep both visible until ADR resolution.

---

## Current schema inventory

| Schema file | Primary role | Maturity note |
|---|---|---|
| `road-segment.schema.json` | Machine-shape scaffold for `RoadSegment`. | **CONFIRMED present / PROPOSED scaffold / NEEDS VERIFICATION** |

Opened evidence for `road-segment.schema.json` shows:

- JSON Schema draft `2020-12`;
- `$id: kfm://schemas/contracts/v1/domains/transport/road-segment.schema.json`;
- `title: "Road Segment"`;
- `type: object`;
- `properties: {}`;
- `additionalProperties: true`;
- `x-kfm.status: PROPOSED`;
- paired contract pointer to `contracts/domains/transport/road-segment.md`.

Because the schema currently has no declared fields, it should be treated as a scaffold, not a validation authority.

---

## What belongs here

Until an ADR resolves the path conflict, only the following should be added here:

- This README.
- Existing schema scaffolds that are already present and must be indexed to prevent silent drift.
- Migration notes that point to the ADR-selected future home.
- Deprecation notices if this path is later retired.
- Mirror notices if this path is later authorized as a temporary compatibility lane.
- Links to paired contracts, fixtures, validators, policy, source registry, release, correction, and rollback surfaces.

After ADR resolution, the accepted path may host machine-checkable transport / Roads-Rail-Trade JSON Schema files if that ADR selects or preserves this path.

---

## What does not belong here

- Semantic contract prose.
- Policy rules or sensitivity decisions.
- Validator implementation code.
- Runtime or routing code.
- Packages or pipeline implementation.
- Lifecycle data payloads.
- Source registry records or SourceDescriptor instances.
- Emitted receipts.
- Proof outputs or EvidenceBundles as data.
- Catalog records.
- Release records, release manifests, promotion decisions, correction notices, or rollback cards as records.
- Public tiles, route services, map/UI behavior, dashboards, screenshots, or generated summaries.
- Claims of current road access, closure, legal right-of-way, emergency detour, parcel boundary, operational restriction, or route membership unless evidence, time, policy, review, and release state are resolved.

---

## Schema-lane rules

| Rule | Requirement |
|---|---|
| Path conflict visibility | Every schema in this folder must remain `PATH-CONFLICTED` or `TRANSITIONAL` until ADR resolution. |
| Stable identity | Every schema must have a stable `$id`; if the path migrates, provide a migration note and do not silently break producers/consumers. |
| JSON Schema version | Use JSON Schema draft 2020-12 unless an ADR says otherwise. |
| Contract pairing | Link each schema to a semantic contract and mark any path conflict. |
| Source-role separation | Road geometry, route membership, graph edge, restriction event, status event, bridge/crossing record, and historic route claim must not collapse into one truth object. |
| Temporal explicitness | Preserve source time, observed time, valid time, retrieval time, release time, and correction time where material. |
| Evidence closure | Evidence-related fields must point to EvidenceRef / EvidenceBundle surfaces without storing proof objects in this schema lane. |
| Policy separation | Public exposure, redaction, access, sensitivity, rights, and release state are policy/release concerns. Schemas may define fields; they do not make decisions. |
| Release separation | ReleaseManifest, PromotionDecision, CorrectionNotice, and RollbackCard schemas may define shape, but authoritative records live under `release/`. |
| No parallel authority | Do not create duplicate RoadSegment schemas in multiple homes without an ADR-backed mirror/migration plan. |

---

## Transport object candidates

The existing `road-segment.schema.json` should not be treated as the whole transport schema model. Future schemas are candidates only after ADR and contract/schema review.

| Candidate schema | Role | Status |
|---|---|---|
| `road-segment.schema.json` | Atomic road-segment evidence shape. | **CONFIRMED scaffold** |
| `route-membership.schema.json` | Relation between road/rail/water segment and named route/corridor. | **PROPOSED / NEEDS VERIFICATION** |
| `transport-network-node.schema.json` | Node/intersection/crossing anchor. | **PROPOSED / NEEDS VERIFICATION** |
| `transport-network-edge.schema.json` | Derived graph edge; not canonical road truth. | **PROPOSED / NEEDS VERIFICATION** |
| `crossing.schema.json` | Road/rail/water crossing record. | **PROPOSED / NEEDS VERIFICATION** |
| `bridge.schema.json` | Bridge structure/context record. | **PROPOSED / NEEDS VERIFICATION** |
| `restriction-event.schema.json` | Time-scoped restriction, closure, or access event. | **PROPOSED / NEEDS VERIFICATION** |
| `status-event.schema.json` | Time-scoped condition/status record. | **PROPOSED / NEEDS VERIFICATION** |
| `historic-route-claim.schema.json` | Evidence-bound historical route assertion. | **PROPOSED / NEEDS VERIFICATION** |
| `trade-route-corridor.schema.json` | Generalized corridor interpretation. | **PROPOSED / NEEDS VERIFICATION** |
| `transport-layer-descriptor.schema.json` | Layer descriptor/profile; not release authority. | **PROPOSED / NEEDS VERIFICATION** |
| `transport-decision-envelope.schema.json` | Finite outcome envelope for transport API/UI responses. | **PROPOSED / NEEDS VERIFICATION** |

---

## Support-type separation

Transport schemas must preserve differences among evidence families.

| Support type | Examples | Schema warning |
|---|---|---|
| `modern_road_reference` | TIGER/Line, state/local roadway datasets, authoritative road inventories. | Not automatically current access, legal right-of-way, route membership, or safety condition. |
| `rail_reference` | Rail line, station, crossing, or corridor references. | Do not collapse rail and road geometry unless explicitly modeled as a crossing or multimodal relation. |
| `historic_route_claim` | Historical trail/road/trade-route interpretation. | Must keep evidence, source date, interpretation method, uncertainty, and generalization visible. |
| `operational_status_event` | Closure, detour, restriction, construction, incident, or status record. | Must be time-scoped and stale-aware; never replace base segment identity. |
| `graph_projection` | Derived nodes/edges, connectivity, shortest-path graph. | Downstream carrier only; must be reversible to segment/node evidence and release state. |
| `public_safe_layer` | PMTiles/GeoParquet/MapLibre layer projection. | Released artifact only; never canonical source truth. |

---

## Review checklist

- [ ] ADR/path decision is cited, or the schema is marked `PATH-CONFLICTED` / `TRANSITIONAL`.
- [ ] Schema has a stable `$id`.
- [ ] Schema uses JSON Schema draft 2020-12 unless an ADR says otherwise.
- [ ] Paired semantic contract is linked.
- [ ] Source-role semantics are explicit.
- [ ] Temporal fields preserve valid/source/observed/retrieval/release/correction distinctions where material.
- [ ] Geometry support, CRS, scale, generalization, and public-safe behavior are explicit where material.
- [ ] Route membership is separate from segment identity.
- [ ] Graph projection is separate from canonical evidence.
- [ ] Restrictions/status events are separate and stale-aware.
- [ ] Evidence references point to evidence surfaces without embedding proof instances in this schema lane.
- [ ] Policy and release fields reference decisions without making this schema lane the decision store.
- [ ] Valid fixtures are linked or marked **NEEDS VERIFICATION**.
- [ ] Invalid fixtures are linked or marked **NEEDS VERIFICATION**.
- [ ] Validator path is linked or marked **NEEDS VERIFICATION**.
- [ ] CI/schema-test support is linked or marked **NEEDS VERIFICATION**.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

---

## Validation

Recommended validation sequence:

```bash
# Inspect the current conflicted schema lane.
find schemas/contracts/v1/domains/transport -maxdepth 2 -type f | sort

# Inspect possible competing homes before adding new files.
find schemas/contracts/v1 -maxdepth 4 -type f \
  | grep -Ei 'transport|roads-rail-trade|road|route|rail|crossing|bridge|restriction|status' \
  | sort

# Validate JSON syntax for the known scaffold.
python -m json.tool schemas/contracts/v1/domains/transport/road-segment.schema.json >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/domains/roads-rail-trade tests/contract tests/schemas || true
```

Replace `|| true` with fail-closed CI behavior once the repository validator set and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/domains/transport/README.md`.

If this path is later retired by ADR:

1. Create or update the ADR naming the accepted schema home.
2. Move or mirror schemas according to the ADR.
3. Update `$id`, `$ref`, schema registry entries, fixtures, validators, producers, consumers, API payloads, and docs.
4. Add a migration note in this folder or remove it with an explicit drift/rollback record.
5. Update any release candidates that referenced the old path.
6. Keep correction and rollback targets visible for released or pre-release artifacts.

No migration should silently leave `RoadSegment` producers, validators, public API responses, MapLibre layer descriptors, Evidence Drawer payloads, or Focus Mode fixtures pointing at a withdrawn schema path.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should the accepted schema home be `schemas/contracts/v1/domains/roads-rail-trade/`, `schemas/contracts/v1/transport/`, or an ADR-approved compatibility pattern? | **ADR REQUIRED** | Schema steward + docs steward + Roads/Rail/Trade steward |
| Should existing `schemas/contracts/v1/domains/transport/road-segment.schema.json` be moved, mirrored, or deprecated? | **NEEDS VERIFICATION** | Schema steward |
| Should `contracts/domains/transport/road-segment.md` move with the schema, or remain as a transitional pointer? | **NEEDS VERIFICATION** | Contract steward |
| Which transport object families need schemas beyond `road-segment.schema.json`? | **NEEDS VERIFICATION** | Domain steward |
| Which fixtures prove valid/invalid route membership, graph edge separation, restriction-event staleness, geometry support, and public-safe layer behavior? | **NEEDS VERIFICATION** | Validation steward |
| Which public API and Evidence Drawer payloads currently consume the transport schema scaffold? | **NEEDS VERIFICATION** | API/UI steward |

---

## Maintainer notes

- Keep this README as a conflict-aware index, not a promotion of the path.
- Prefer ADR resolution before adding any new schema files here.
- Preserve cite-or-abstain: a transport schema can shape a claim, but evidence, source role, policy, review, release, correction lineage, and rollback support public truth.
- Preserve the trust membrane: public clients use governed APIs, released artifacts, catalog records, tile services, and EvidenceBundle resolution; they do not read RAW, WORK, QUARANTINE, unpublished candidates, internal stores, or model output directly.
