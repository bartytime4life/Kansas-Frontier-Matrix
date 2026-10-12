<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/soil/map-ui-contracts
title: Soil map and user interface guide
type: domain-guide
version: v1.0
status: draft; repository-grounded; review-required
owners:
  - OWNER_TBD - Soil domain steward
  - OWNER_TBD - Documentation steward
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: docs/
responsibility: Soil map and user interface guide; human guidance subordinate to owning contracts, schemas, policy, evidence, and release decisions
truth_posture: CONFIRMED inspected repository paths and bounded implementation; PROPOSED review procedure; UNKNOWN external source and operational acceptance
related:
  - docs/domains/soil/API_CONTRACTS.md
  - apps/site/source/app/soil-moisture.ts
  - apps/site/source/tests/soil-map-state.test.mjs
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# soil — MAP_UI_CONTRACTS.md

This guide separates the governed Soil domain's intended delivery contract from
Soil-related visual context implemented in the Site. A rendered overlay does not
establish admission, catalog closure or a released Soil product.

## Inspected Site behavior

At the evidence snapshot, [soil-moisture.ts](../../../apps/site/source/app/soil-moisture.ts)
defines four NASA GIBS views: surface moisture, root-zone moisture, surface
uncertainty and root-zone uncertainty. The code labels depths as 0–5 cm and
0–100 cm, and explicitly identifies the images as visual context rather than
pixel readings. These are configured product labels, not a live provider audit.

Visibility, selected view, UTC calendar day and opacity form one saved map state.
The default is hidden, surface view, no selected day and opacity 0.65. Invalid
share values fall back safely; valid opacity is clamped to 0–1. Hide all preserves
selection settings while switching visibility off. See the
[state tests](../../../apps/site/source/tests/soil-map-state.test.mjs).

The [subsurface soil endpoint](../../../apps/site/source/app/api/subsurface/soil/route.ts)
and its [tests](../../../apps/site/source/tests/subsurface-soil.test.mjs) preserve
USDA response components separately, centimetre depths, retrieval time and a
partial-result indicator. Invalid coordinates are rejected before a request.
Malformed and oversized responses become unavailable; they are not interpreted
as an empty soil profile.

## Display requirements for review

| Display element | Required interpretation |
|---|---|
| Source and edition | Identify the product being shown, not just the provider brand |
| Support | Distinguish survey polygon, raster/model grid, station, profile and interpretation |
| Depth | Keep surface and root zone explicit; never imply a borehole interval |
| Time | Keep source observation/vintage, display frame and retrieval time distinct |
| Legend and units | Attach the relevant legend and units to the selected view |
| Uncertainty | Show QA, limitations, missing coverage and partial responses |
| Interaction | Preserve source roles when selecting, sharing, hiding or exporting |
| Evidence | A governed product must resolve its evidence through the appropriate carrier |

Soil survey components are not continuous geological strata. A moisture image
cannot establish field-specific water content, crop advice, groundwater depth,
excavation safety or ownership. Adjacent [cross-lane context](CROSS_LANES.md)
retains its own authority and scale.

## Review procedure

1. Pin Site source version and test revision separately from hosted deployment.
2. Check each view's label, legend, depth and time semantics against the code and
   product reference. Record whether provider behavior was actually checked.
3. Exercise visible/hidden state, shared-state restoration, invalid dates and
   opacity bounds. Confirm uncertainty views cannot be mistaken for moisture.
4. Exercise unavailable, empty, partial and malformed source responses separately.
5. Check privacy suppression before precise location or exports enter a public
   route. Verify keyboard, touch and screen-reader behavior in a browser.
6. Record code tests, browser observations and hosted acceptance independently.

## Focused local checks

From `apps/site/source/`, after installing its pinned dependencies:

```bash
node --test tests/soil-map-state.test.mjs tests/soil-moisture.test.mjs tests/subsurface-soil.test.mjs
```

These mocked/local tests do not prove current NASA/USDA availability or hosted
rendering. Browser acceptance remains a separate observation. If a layer renders
without metadata, retain an unavailable/limited state and investigate source
mapping; do not manufacture a numeric reading from image color.

## Governed Soil handoff

A future released Soil carrier still needs source, evidence, rights, sensitivity,
policy, review, correction and rollback closure described in
[API contracts](API_CONTRACTS.md) and [catalog closure](CATALOG_CLOSURE.md).
Use the Site's existing owning implementation path for UI work; the retired
Explorer Web lane is historical context, not a destination for new components.
