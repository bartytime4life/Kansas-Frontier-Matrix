# Flora map: plants and vegetation

The starting page's **Flora & vegetation** card opens **Plants & vegetation**.
It starts the existing USGS NLCD 2021 land-cover raster over the prairie base.
The legend identifies forest, grassland, shrub, wetland and cultivated classes;
clicking the map asks the existing MRLC point endpoint for the classified cell.
This is a dated land-cover classification, not a species inventory.

## Data and features

| Layer | Initial state | Time and resolution | Controls and limits |
|---|---|---|---|
| USGS / MRLC NLCD | On | 2021, 30 m | Class legend and point lookup; mapped classes can be wrong. This is the existing legacy 2021 product, not the latest Annual NLCD. |
| GBIF Plantae records | Off | One event year, coarse hexagons; source zoom capped at 6 | Select 1995–2025, opacity, hide/show and retry. Default 2021 matches the cover reference year, not observation dates within that year. |
| USDA Cropland Data Layer | Off | Existing independently selected annual editions | Existing crop legend, year selection and point inspection. A crop class is not a botanical occurrence or proof of current activity. |

Area measurement is available for outlining an investigation. The small welcome
preview remains basemap context and explicitly directs visitors to open the map
for these data layers. There is no fabricated Flora recording.

GBIF uses the existing `/api/event-atlas/tile` proxy with fixed `kind=flora`,
Plantae taxon 6, US records, a single event year, `bin=hex`, `hexPerTile=20` and
provider `green.poly` rendering. Only raster images reach the client. The client
limits tile bounds to Kansas and a small margin; cells crossing the state border
can include neighboring US records, so this is not a Kansas-only count. Zooming
in overzooms the coarse images; it never requests precise coordinates. The year
selector is a supported request range, not a coverage guarantee. The main map
calendar does not change these explicitly dated tool layers.

Source IDs include year and retry generation. Changing year removes the prior
image before loading the replacement. A tile error hides the whole plant layer
until retry or a new year; late events cannot mark another generation loaded.
A source-confirmed empty image stays transparent. Neither empty nor unavailable
imagery establishes absence. The status reports tile requests settling, not a
complete inventory or evidence validation. Record-density colors retain GBIF's
provider scale and are not a numeric abundance legend or effort-adjusted trend.

Sources and interpretation:

- [USGS legacy NLCD](https://www.usgs.gov/centers/eros/science/national-land-cover-database)
- [GBIF Maps API](https://techdocs.gbif.org/en/openapi/v2/maps)
- [GBIF data user agreement](https://www.gbif.org/terms/data-user)
- [GBIF sensitive-species guidance](https://docs.gbif.org/sensitive-species-best-practices/master/en/)
- Existing application source notes: `/observatory/sources#ecology`.

The map retains GBIF contributor attribution. Dataset-specific rights and
citation requirements still apply to downstream use. No occurrence downloads,
species drill-down, exact plant sites, conservation-status assertions or
reviewed Flora EvidenceBundles are introduced. Existing main-lane Flora
admission and release controls are unchanged; displaying external context is
not data promotion or authorization to publish a governed Flora product.

## Placement, validation and rollback

This hosted composition keeps UI/runtime code in its existing `app/` root,
checks in `tests/`, and behavior documentation in `docs/`. This follows the
responsibility-first rule of accepted ADR-0029 / Directory Rules §4–§7 and the
hosted branch's preservation instructions. There is no new schema, registry,
policy or data authority root and no copy from private source stores.

The read-only local seed-card Flora pattern informed separation of specimens,
occurrences, classifications and sensitive locations. The existing domain's
thin-slice plan describes later governed evidence work; this change does not
claim to complete that pipeline.

`tests/flora-context.test.mjs` exercises layer lifecycle, opacity, year bounds,
style replacement, failures, retries, stale events, controls and taxonomy.
`tests/event-atlas.test.mjs` retains the adapter's precise-zoom and arbitrary-query
refusal. Existing NLCD, crop, category and welcome checks cover their reused
paths. Browser and live-provider results are recorded separately in the PR.

Rollback is a source revert. There are no persistent data writes or migrations.
