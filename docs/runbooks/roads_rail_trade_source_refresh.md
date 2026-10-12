<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/roads-rail-trade-source-refresh
title: Roads Rail Trade source refresh review
type: runbook
version: v1.0
status: draft; repository-grounded; review-required
owners:
  - OWNER_TBD - Roads Rail Trade and source stewards
  - OWNER_TBD - Documentation steward
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: docs/
responsibility: Roads Rail Trade source refresh review; human guidance subordinate to owning contracts, schemas, policy, evidence, and release decisions
truth_posture: CONFIRMED inspected repository paths and bounded implementation; PROPOSED review procedure; UNKNOWN external source and operational acceptance
related:
  - docs/domains/roads-rail-trade/CANONICAL_PATHS.md
  - .github/workflows/domain-roads-rail-trade.yml
  - data/registry/sources/roads-rail-trade/README.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Roads Rail Trade Source Refresh

Use this procedure when transport source editions, segment identities, routes,
operators, restrictions or source roles change. It prepares a bounded source
review and does not fetch, activate, publish or provide route advice.

## Repository capability

The [domain workflow](../../.github/workflows/domain-roads-rail-trade.yml) runs
bounded synthetic CorridorRoute schema/validator tests with `PASS`, `ABSTAIN`
and `DENY` coverage. It explicitly holds broader semantic validation, proof and
release. Crossing, bridge/river-crossing, facility topology and facilities
validator roots are checked as documentation-only lanes at the pinned revision.

The [source-registry lane](../../data/registry/sources/roads-rail-trade/README.md)
and [candidate lane](../../release/candidates/roads-rail-trade/README.md) provide
boundaries, not evidence that a particular provider is active. Use the
[canonical-path guide](../domains/roads-rail-trade/CANONICAL_PATHS.md) to identify
existing owning surfaces before adding a descriptor or transform.

## Review inputs

Record provider and exact product/edition; source-native segment/facility/route
keys; geography and time validity; geometry/topology method; source role; rights
and redistribution constraints; precision/sensitivity; baseline and proposed
digests; intended consumers; and correction/rollback references.

Separate observed infrastructure, administrative designation, modeled network,
commercial service and operational restriction. A road line is not legal access;
a railway line is not proof of active service; an old restriction is not a live
closure status.

## Source-change procedure

1. Pin the baseline source identity and the proposed product or record set.
2. Establish bounded acquisition parameters separately if live access is needed:
   geography, date range, expected size, paging, licensing and cache behavior.
3. Compare stable IDs, geometry, topology, route membership, operator/source role,
   time validity and restrictions separately from packaging changes.
4. Preserve ambiguous joins and missing connections. Do not snap or merge nodes
   without a declared method and evidence.
5. Review crossings and bridges against their own evidence. Spatial intersection
   alone is not proof of a traversable connection or safe passage.
6. Build synthetic positive and negative examples for the changed contract.
7. Run the relevant bounded checks. Record semantic outcomes separately from CLI
   success and workflow readiness holds.
8. Route source, transport, rights, sensitivity and release questions to their
   accountable reviewer roles. Their named assignments remain unverified here.

## Available local checks

```bash
python -m pytest -q -p no:cacheprovider tests/schemas/test_corridor_route_contract.py
python tools/validators/domains/roads-rail-trade/validate_corridor_route.py --fixtures
python -m unittest discover --start-directory tests/domains/roads-rail-trade --pattern 'test_roads_rail_trade_smoke.py' --verbose
```

These commands do not establish actual route connectivity, current closures,
operator status, bridge condition, right of access, safe navigation, graph truth
or release approval. If new implementation appears in a held validator lane,
add its reviewed contract/fixtures/tests and deliberately wire the workflow.

## Troubleshooting and acceptance

| Finding | Required response |
|---|---|
| Segment key reused across editions | Preserve edition-specific lineage and investigate identity |
| Geometry changed with no method record | Hold derived connectivity and document the gap |
| Ambiguous intersection or route join | Retain ambiguity; do not choose a convenient edge |
| Restriction lacks effective time | Do not represent it as current operational guidance |
| Rights or infrastructure precision unclear | Restrict the candidate pending review |
| Green workflow with proof/release hold | Report fixture evidence and unresolved producer separately |

A completed refresh review records exact identities, change categories, impact
inventory, expected failures, local results, reviewer disposition and remaining
source/release gates. Rollback must restore an exact prior artifact and its
consumers, or an explicit unavailable state; this runbook supplies no execution
command or permission to republish a historical network.
