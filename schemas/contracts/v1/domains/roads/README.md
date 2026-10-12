# `schemas/contracts/v1/domains/roads/`

## Purpose

Draft compatibility index for road-specific machine-shape work.

This path is not confirmed canonical. It is a short-segment compatibility surface under review. The broader current schema lane for this area is `schemas/contracts/v1/domains/roads-rail-trade/`.

This README is documentation only. It is not a schema file, contract, policy, validator, pipeline, lifecycle data, source registry record, proof, receipt, catalog record, release record, public API behavior, map behavior, or publication authority.

## Status

| Field | Value |
|---|---|
| Status | Draft |
| Owning root | `schemas/` |
| Path role | Compatibility index |
| Canonical posture | PROPOSED / CONFLICTED |
| Parent lane | `schemas/contracts/v1/domains/roads-rail-trade/` |
| Current schema inventory | NEEDS VERIFICATION |
| Last reviewed | 2026-07-03 |

## Placement basis

`schemas/` owns machine-checkable shape.

ADR-0001 places domain schemas under `schemas/contracts/v1/domains/<domain>/...`.

Directory Rules keep schemas, contracts, policy, data, registries, proofs, receipts, fixtures, tests, pipelines, and releases in separate responsibility roots.

`contracts/domains/roads/README.md` treats `roads/` as a compatibility or orientation slice under the broader Roads / Rail / Trade lane, not as a new canonical domain authority.

`schemas/contracts/v1/domains/roads-rail-trade/README.md` is the broader schema index and is itself PROPOSED / slug-CONFLICTED.

Current search found road-related semantic contracts and docs, but did not confirm concrete `.schema.json` files under this path.

## Related lanes

```text
schemas/contracts/v1/domains/roads/              # this compatibility index
schemas/contracts/v1/domains/roads-rail-trade/   # broader schema lane
contracts/domains/roads/                         # compatibility contract slice
contracts/domains/roads-rail-trade/              # broader semantic contract lane
docs/domains/roads-rail-trade/sublanes/roads.md  # roads doctrine, PROPOSED
```

## Candidate schema names

| Candidate | Status |
|---|---|
| `road_segment.schema.json` | NEEDS VERIFICATION |
| `corridor_route.schema.json` | NEEDS VERIFICATION |
| `route_membership.schema.json` | NEEDS VERIFICATION |
| `road_crossing.schema.json` | NEEDS VERIFICATION |
| `restriction_event.schema.json` | NEEDS VERIFICATION |
| `status_event.schema.json` | NEEDS VERIFICATION |
| `operator_assignment.schema.json` | NEEDS VERIFICATION |
| `transport_facility.schema.json` | NEEDS VERIFICATION |
| `network_node.schema.json` | NEEDS VERIFICATION |
| `network_edge.schema.json` | NEEDS VERIFICATION |
| `public_safe_road_summary.schema.json` | NEEDS VERIFICATION |

## What belongs here

- This README.
- Compatibility notes for the short `roads` schema segment.
- Migration notes after the accepted schema home is decided.
- Links to paired contracts, fixtures, validators, schema registry records, tests, policy references, release references, correction references, and rollback references.

## What does not belong here

- Contract prose beyond this boundary README.
- Policy rules.
- Validator code.
- Pipeline code.
- Lifecycle data.
- Source registry records.
- Proof or receipt records.
- Catalog records.
- Release records.
- Public map or API artifacts.
- Schema files until placement is resolved by steward decision, ADR, or migration note.

## Review checklist

- [ ] Confirm whether this compatibility path should exist, redirect, or be retired.
- [ ] Confirm whether accepted road schemas belong under `schemas/contracts/v1/domains/roads-rail-trade/`.
- [ ] Confirm paired contract paths.
- [ ] Confirm schema registry records.
- [ ] Confirm fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm policy, source-registry, release, correction, and rollback references.
