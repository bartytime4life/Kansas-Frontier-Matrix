# `schemas/contracts/v1/domains/roads-rail-trade/` — Roads / Rail / Trade Domain Schema Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-roads-rail-trade-readme
title: schemas/contracts/v1/domains/roads-rail-trade/ — Roads / Rail / Trade Domain Schema Index
version: v1.1
status: draft; PROPOSED; slug-CONFLICTED; schema-index
policy_label: public
owners:
  - <schema-steward>
  - <roads-rail-trade-domain-steward>
  - <roads-steward>
  - <rail-steward>
  - <trade-routes-steward>
  - <validation-steward>
  - <docs-steward>
updated: 2026-08-03
tags: [kfm, schemas, contracts, v1, domains, roads-rail-trade, transport, routes, corridor-route, json-schema]
notes:
  - "v1.1 records the bounded CorridorRoute schema profile, validator, synthetic fixtures, and focused tests added from New Ideas 3-31-26.pdf."
  - "The profile is PROPOSED and fixture-only. It does not settle the roads-rail-trade versus transport slug conflict, activate sources, execute policy, approve review, release, publish, or provide routing authority."
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-roads--rail--trade-slategray)
![inventory](https://img.shields.io/badge/inventory-one__bounded__profile-orange)
![slug](https://img.shields.io/badge/slug-PROPOSED%20%2F%20CONFLICTED-red)
![truth](https://img.shields.io/badge/truth-evidence--first-blue)

## Purpose

This directory is the draft machine-shape lane for Roads / Rail / Trade domain contracts. It may contain JSON Schema files, schema-family indexes, compatibility notes, and links to paired contracts, fixtures, validators, tests, registry records, policy references, corrections, rollback records, and release records.

It must not contain semantic contract prose, policy rules, validator implementation, source registry records, lifecycle data, receipts, proofs, release decisions, public map/API artifacts, routing advice, legal-status advice, or emergency access instructions.

## Authority and placement

| Question | Controlling surface |
|---|---|
| What does a Roads / Rail / Trade object mean? | `contracts/domains/roads-rail-trade/` or an ADR-selected semantic-contract home |
| What fields and constraints exist? | This `schemas/` lane |
| May a candidate be used or exposed? | `policy/`, source/evidence/review state, and release governance |
| How is behavior proved? | `fixtures/`, `tests/`, and `tools/validators/` |
| Where are lifecycle objects stored? | Established `data/` lifecycle and accountability roots |
| What authorizes public release? | `release/` plus proof, review, correction, and rollback closure |

Directory Rules basis: schemas are machine-checkable shape artifacts under `schemas/`. The domain remains a segment inside that responsibility root. This index creates no new root and no parallel contract, policy, source, registry, proof, release, or publication authority.

## Path posture

The repository still carries an unresolved `roads-rail-trade` versus `transport` and domain-nested versus flat-path naming conflict. The bounded profile below uses the current domain-nested lane because it pairs directly with the existing semantic contract. That placement remains **PROPOSED** until the accepted ADR/Directory Rules projection settles the conflict.

## Current schema inventory

| Schema | Paired contract | Status | Validation surface | Authority limit |
|---|---|---|---|---|
| [`corridor_route.schema.json`](./corridor_route.schema.json) | [`contracts/domains/roads-rail-trade/corridor_route.md`](../../../../../contracts/domains/roads-rail-trade/corridor_route.md) | **DRAFT_SCHEMA / PROPOSED bounded profile** | [`validate_corridor_route.py`](../../../../../tools/validators/domains/roads-rail-trade/validate_corridor_route.py), [`fixtures/domains/roads-rail-trade/corridor_route/`](../../../../../fixtures/domains/roads-rail-trade/corridor_route/), [`tests/schemas/test_corridor_route_contract.py`](../../../../../tests/schemas/test_corridor_route_contract.py) | Fixture-only; no source admission, real-route truth, policy approval, review, release, publication, legal designation, or live routing authority. |

No other concrete Roads / Rail / Trade `.schema.json` file is claimed by this index without current repository evidence.

## CorridorRoute profile

The profile machine-requires the historical-route fields proposed by the source packet:

- stable route identity and name;
- `feature_class=route`;
- approximate dates and explicit date uncertainty;
- geometry accuracy;
- source URI and license;
- evidence references and evidence-resolution posture;
- bounded confidence;
- explicit authoritative-versus-derived representation;
- change state.

It also enforces KFM anti-collapse boundaries:

- route identity is not RoadSegment, RailSegment, RouteMembership, embedded geometry, or graph truth;
- bound evidence requires at least one EvidenceRef;
- unresolved source/evidence/geometry/rights cannot claim released posture;
- authoritative representation requires authority/official source role and cannot rely on derived geocoding;
- sensitive or rights-restricted geometry cannot be marked for generalized public use;
- released posture requires policy, review, release-manifest, and rollback references;
- live-routing, legal-designation, and publication-approval fields are forbidden.

## Candidate backlog

The names below remain **NEEDS VERIFICATION** and do not imply files exist:

| Candidate schema | Main boundary |
|---|---|
| `road_segment.schema.json` | Road alignment evidence; not route identity or live/legal routing status. |
| `rail_segment.schema.json` | Rail alignment and temporal/operator context; not service authority. |
| `route_membership.schema.json` | Source- and time-scoped segment-to-route relation. |
| `bridge.schema.json` / `river_crossing.schema.json` / `ferry.schema.json` | Transport-side crossing semantics without replacing Infrastructure or Hydrology truth. |
| `depot.schema.json` / `siding.schema.json` / `yard.schema.json` | Transport facilities with source role and temporal status. |
| `operator_assignment.schema.json` / `operator_status.schema.json` | Operator relationships and status without legal or operational authority. |
| `status_event.schema.json` / `restriction_event.schema.json` / `access_restriction.schema.json` | Time-bounded events and constraints; not live routing advice by default. |
| `network_edge.schema.json` | Derived graph projection; never canonical route/segment truth. |
| `public_safe_route_summary.schema.json` | Released derivative requiring evidence, policy, correction, and rollback references. |

## Status vocabulary

| Status | Meaning |
|---|---|
| `STUB` | File exists but is not field-complete. |
| `DRAFT_SCHEMA` | Meaningful shape exists with bounded fixtures/tests; admission remains pending. |
| `ACTIVE_SCHEMA` | Accepted contract pairing, registry record, fixtures, validator support, review, and CI are established. |
| `PATH_CONFLICT` | Placement is blocked by unresolved schema-home or slug authority. |
| `PROFILE` | Shape profiles a shared object or source without creating duplicate authority. |
| `MIRROR` | Compatibility mirror of an accepted canonical schema. |
| `TRANSITIONAL` | Awaiting governed migration. |
| `DEPRECATED` | Must not receive new consumers. |
| `NEEDS_VERIFICATION` | Required implementation or authority evidence has not been checked. |

## Review checklist

- [x] CorridorRoute schema has a stable `$id`.
- [x] CorridorRoute schema declares JSON Schema draft 2020-12.
- [x] Paired semantic contract is linked.
- [x] Synthetic valid, abstention, and exact-negative fixtures are linked.
- [x] No-network validator and focused schema tests are linked.
- [x] Route/segment/membership/geometry/live-routing/publication anti-collapse boundaries are tested.
- [ ] Resolve the `roads-rail-trade` versus `transport` and domain-nested versus flat-path conflict.
- [ ] Add or confirm the schema-registry entry.
- [ ] Bind admitted SourceDescriptor/source-role vocabulary.
- [ ] Confirm policy bundle and policy-test references.
- [ ] Confirm CODEOWNERS and steward review.
- [ ] Confirm broader CI integration and repository-wide regression status.
- [ ] Confirm release, correction, and rollback object-family integration before any public use.

## Validation

```bash
KFM_NO_NETWORK=1 PYTHONHASHSEED=0 TZ=UTC \
  python tools/validators/domains/roads-rail-trade/validate_corridor_route.py --fixtures

KFM_NO_NETWORK=1 PYTHONHASHSEED=0 TZ=UTC \
  python -m pytest -q tests/schemas/test_corridor_route_contract.py
```

`PASS` proves only the bounded schema, deterministic hash, temporal, source-role, and public-safety checks implemented by this profile. It does not grant truth, source admission, policy approval, review, release, publication, legal designation, or routing authority.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-08-03 |
| Review status | Draft index updated for the CorridorRoute bounded profile |
| Next trigger | ADR/path resolution, schema-registry admission, source onboarding, policy integration, CI wiring, release integration, correction/rollback drill, or another concrete Roads / Rail / Trade schema |
