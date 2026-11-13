# Outdoor access and soil survey layers — November 13, 2026

This note records three public context layers that were added to the repository
Explorer (`apps/site/source`). They match the hosted composition's
`a0-hosted-ai-web-20261017` change of the same date. Every layer is off by
default and external display context (`EXTERNAL_CONTEXT_ONLY`). None creates a
KFM EvidenceBundle, source admission, review or release. This note does not
claim any hosted deployment, browser acceptance or public-website change.

## What a visitor can do now

| Layer | Provider | Kind | Topics | Clock |
|---|---|---|---|---|
| Wildlife areas · KDWP | Kansas Department of Wildlife and Parks | Clickable polygons (`feed=kdwp-wildlife-areas`) | Ecology, Land, Places | Current public layer |
| Walk-in hunting access | KDWP (the layer used by the public 2026–2027 WIHA map) | Clickable polygons (`feed=kdwp-wiha-access`) | Ecology, Land, Places | Current season layer |
| Soil survey · map units | USDA NRCS SSURGO (Soil Data Mart WMS) | Provider image, zoom 12 and closer | Agriculture, Land, Science | Current SSURGO edition |

A live check on November 13, 2026 returned:

- 266 wildlife-area polygons.
- 3,591 WIHA tracts, from two provider pages. After the provider simplified the
  geometry, the response was about 2 MB.

Counts change with the provider and are not a fixed inventory.

## Source and safety boundaries

- **KDWP outlines** are simplified display geometry. They are not legal
  boundaries, regulations or hunting permission. Seasons, refuges and closures
  change, so visitors should check KDWP before entering or hunting.
- **WIHA tracts** are private land. The public may hunt there only during the
  posted seasons and under program rules. The adapter never requests landowner
  contract identifiers (`CONTRACTID`) or the free-text `NOTES` field, which
  holds KDWP administrative text such as contract numbers, payment rates and
  conservation-contract expiries. A test checks both.
- **Links** are kept only when they point to `ksoutdoors.com` or
  `ksoutdoors.gov`. They are extracted from KDWP's HTML link field.
- **SSURGO outlines** are map units, which often contain several soil
  components. They are not site-specific soil tests or ratings of suitability
  for engineering, septic systems or buildings.

## Implementation

| Area | Files |
|---|---|
| Bounded server adapter (paged in 2,000s, 6,000 cap, provider-side simplification, Kansas bounds) | `app/api/live-context/route.ts`, `app/api/source-download/route.ts` |
| SSURGO image layer and legend | `app/kansas-discovery-layers.ts` |
| Registry, temporal support and MapLibre fill and line layers | `app/live-context.ts` |
| Topics, inspection fields and text | `app/layer-workspaces.ts`, `app/evidence-drawer-data.ts`, `app/page.tsx` |
| Feature, connection and download registries | `app/site-features.ts`, `app/site-connections.ts`, `app/source-downloads.ts` |
| Local companion cap (57 → 60) and knowledge pack | `scripts/qwen-local-contract.mjs`, `scripts/qwen-knowledge-pack.mjs` |
| Tests | `tests/kansas-discovery-layers.test.mjs` and registry-count updates |

The repository Explorer has no Fauna topic, so the KDWP layers are listed under
Ecology, Land and Places. Animal-occurrence layers are still not added. Tribal
context is still left to its jurisdiction and sensitivity review lane.

## Rollback

Revert the files above together. The change touches no database, storage
binding, dataset or deployment setting, so rollback needs no data migration.
