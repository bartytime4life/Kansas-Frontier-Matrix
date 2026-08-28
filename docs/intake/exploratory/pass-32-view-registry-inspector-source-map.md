<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://docs/intake/exploratory/pass-32-view-registry-inspector-source-map
title: Pass 32 View Registry Inspector Source Map
type: exploratory-source-map
version: v0.1.0
status: proposed; implementation-bounded; non-authoritative
owners: [kfm-maintainers]
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; public-safe-projection
owning_root: docs/
responsibility: source-to-repository reconciliation for the bounded View Registry inspector adaptation
truth_posture: CONFIRMED source and repository reconciliation; PROPOSED fixture-backed implementation
source_ideas: [KFM-P32-IDEA-0008, KFM-P32-FEAT-0004]
related:
  - ../../../contracts/ui/view_registry_profile.md
  - ../../../schemas/contracts/v1/ui/view_registry_profile.schema.json
  - ../../../apps/explorer-web/src/adapters/ViewRegistryInspectorProjection.ts
  - ../../../apps/explorer-web/src/features/view_registry_inspector/README.md
  - ../../../fixtures/ui/view_registry_inspector_projection/README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Pass 32 View Registry Inspector Source Map

## Source candidate

| Candidate | Source statement | Source spec hash |
|---|---|---|
| KFM-P32-IDEA-0008 | Keep the route-to-layer registry explicit so UI publication remains reviewable. | sha256:eef8ba04e47f439aa679211785993bdbf358b0684ac8e12af5338790ea80b31d |
| KFM-P32-FEAT-0004 | Maintainers should be able to inspect route-to-layer registry entries, rendering hints, budgets, and policy labels before UI publication. | sha256:93a77dbdccc5468ebddd264671ae749d7adba7ec3be94ad5a1dc353b78478784 |

The source review used the supplied consolidated Pass 23–32 domain atlas and the connected Drive atlas index. Private Drive locators are intentionally excluded from this repository document.

## Repository reconciliation

The current main branch already contains the View Registry profile contract, schema, validator, fixtures, tests, and source map. That source map explicitly leaves a maintainer UI inspector outside the foundation packet. Repository and pull-request review found no implementation of the bounded inspector on the reconciled base.

This packet consumes only a closed, prevalidated public-safe projection. It does not replace the View Registry validator, resolve contract or catalog references, read a registry store, or establish a route.

## Bounded adaptation

The implementation provides:

- an exact-field adapter for one public-safe inspection projection;
- deterministic identity binding between registry_id and spec_hash;
- finite available, abstain, deny, and error outcomes;
- a read-only table of route, delivery, catalog, layer, rendering, budget, access, sensitivity, Evidence Drawer, and release references;
- explicit PROPOSED_INACTIVE activation state for every displayed entry;
- fixture-backed unit and browser coverage for positive and negative paths.

The inspector has no transport, registry lookup, route binding, layer activation, policy evaluation, approval, release, or publication seam.

## Source pressure and response

| Source pressure | Bounded repository response |
|---|---|
| Inspect route-to-layer entries | Display only entries supplied by the closed projection. |
| Inspect rendering hints | Display finite renderer, protocol, style, and layer-manifest references. |
| Inspect budgets | Display precomputed budget references; do not calculate or alter budgets. |
| Inspect policy labels | Display opaque access and sensitivity labels; do not evaluate policy. |
| Review before publication | Keep every activation state PROPOSED_INACTIVE and all authority flags false. |

## Directory Rules basis

The adapter and feature remain under apps/explorer-web; synthetic packets remain under fixtures/ui; executable tests remain with the Explorer application; source reconciliation remains under docs/intake/exploratory; and the generated receipt remains under data/receipts/generated. This follows DIR-PLACE-002, DIR-PLACE-005, DIR-EXEC-001, and DIR-DEP-002 without creating a new root or bypassing the governed API boundary.

## Explicit non-effects

This packet does not bind a route, activate a layer, resolve a source, read RAW or WORK data, evaluate access, approve a candidate, change lifecycle state, release, deploy, or publish. Displayed references remain opaque. Missing, malformed, contradictory, or direct-store-shaped input fails closed without reflecting unknown fields.

## Rollback

Close the draft or revert the additive adapter, feature, fixtures, tests, source map, and receipt. No registry, route, release, deployment, or publication state is changed.
