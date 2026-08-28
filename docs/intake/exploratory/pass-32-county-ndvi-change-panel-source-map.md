<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-county-ndvi-change-panel-source-map
title: Pass 32 county NDVI change panel - governed implementation source map
type: exploratory-intake-source-map
version: v1.0.0
status: proposed; implementation-mapped; fixture-only; non-authoritative
owners: OWNER_TBD - UI steward; agriculture steward; remote-sensing steward; evidence steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal
owning_root: docs/
responsibility: reconcile Pass 32 KFM-P32-FEAT-0005 and KFM-P32-IDEA-0011 with the deterministic NDVI computation and a bounded Explorer projection
truth_posture: CONFIRMED source statement and repository foundation / PROPOSED app-local implementation / UNKNOWN production integration and hosted exact-head proof
related: [../../../apps/explorer-web/src/features/county_ndvi_change_panel/README.md, ../../../contracts/domains/agriculture/ndvi_delta_computation.md, pass-32-ndvi-delta-computation-source-map.md]
[/KFM_META_BLOCK_V2] -->

# Pass 32 county NDVI change panel - governed implementation source map

## Source statement

`KFM-P32-FEAT-0005` in the supplied private Pass 32 source corpus proposes a county panel showing baseline and recent windows, a delta threshold, changed-area percentage, cluster count, and evidence state. `KFM-P32-IDEA-0011` requires county NDVI deltas to remain proposed indicators until source ETags, cloud masks, connected components, persistence, and steward validation support them. The rendered source pages and a separate private connected-Drive planning document corroborate the county-scale NDVI and deterministic-evidence lineage. Private source titles and identifiers are intentionally withheld from this public branch. These materials remain proposal evidence, not repository, scientific, source-admission, policy, or release authority.

## Current repository reconciliation

At initial inspection `main@7c69e025e2b274be4a19f49fa37e22401a2fe757`, the repository already contained the deterministic no-network `NdviDeltaComputation` profile, HLS NDVI materiality and readiness checks, and a separate vegetation connectivity gate. The NDVI computation explicitly leaves county aggregation, clustering, evidence closure, and public UI out of its authority. Contemporaneous duplicate, branch, and exact-path searches found no implementation of this card. Delivery was refreshed and revalidated against `main@ef1ba46a19e4de7c176e9d093c1285e73a0af75a`; intervening changes were path-disjoint.

The smallest dependency-closed gap is an unmounted Explorer projection that displays supplied synthetic aggregates while exposing that evidence is referenced but unresolved. No source connector, raster reader, county aggregator, cluster detector, EvidenceBundle producer, contract, schema, policy, route, workflow, or lifecycle writer is justified here.

## Implemented boundary

The adapter accepts exact fixture-only packets with one synthetic Kansas county scope, ordered non-overlapping windows, coherent integer-millionth NDVI arithmetic, a finite candidate classification, bounded changed-area basis points and cluster count, and two distinct digest-bound upstream references. It recomputes the delta and threshold classification and requires candidate area and clusters to agree. Negative outcomes carry no county, metric, or reference detail.

`REFERENCED_NOT_RESOLVED` is fixed and all network, source-activation, interpretation, promotion, release, publication, and public-use authority is false. The panel does not calculate NDVI, aggregate counties, detect connected components, resolve evidence, interpret environmental conditions, or author a claim.

## Directory Rules basis

Accepted ADR-0029 and Directory Rules route the user surface and app-local adapter to `apps/explorer-web/`, synthetic reusable display packets to `fixtures/ui/`, feature proof to the Explorer test harness, human source reconciliation to `docs/intake/exploratory/`, and authoring accountability to `data/receipts/generated/`. The county is a registered composition scope rather than a new domain or root. The existing calculation and connectivity authorities are referenced, not duplicated.

## Sources

- Consolidated atlas card `KFM-P32-FEAT-0005`, spec hash `sha256:1ac995f451999184cfac1057ccb48966ff9af464303ad225c56211cd1c5490ed`.
- Consolidated atlas card `KFM-P32-IDEA-0011`, spec hash `sha256:84a3d05450524471afc055265a1650ef10a615150efdebf8352280d6f63ec4b5`.
- Private connected-Drive corroboration was inspected; its title and identifier are omitted from the public branch.
- Repository foundations: `contracts/domains/agriculture/ndvi_delta_computation.md` and `contracts/domains/agriculture/vegetation_connectivity_gate.md`.

## Validation and rollback

Validation covers targeted and full Explorer unit suites, production build, isolated browser-fixture typechecking and discovery, the existing NDVI computation suite, metadata and link checks, and generated-receipt byte binding. Rollback is a focused revert of this additive packet; it creates no external, source, evidence, lifecycle, policy, promotion, release, deployment, publication, or public-use state.
