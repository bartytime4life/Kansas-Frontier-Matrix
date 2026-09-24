# Earth Engine discovery and recipes

Metadata checked: 2026-09-24. Scope: existing standalone Sites project
`appgprj_6aa0b1c41bc08191bfd86003920f1631`, opened at
`d31c6ca6bd32b9ed50a34679b936568f1585e489` (version 66).

The user selected discovery and recipes without an Earth Engine connection.
This adds Site functionality and source-discovery metadata only. It does not
admit Earth Engine pixels, authorize monorepo changes, or release KFM data.

## Source basis

Each entry links to Google's official catalog page and its terms/citations:

| Dataset | Recipe | Important boundary |
| --- | --- | --- |
| [USDA CDL](https://developers.google.com/earth-engine/datasets/catalog/USDA_NASS_CDL) | One annual cropland image | Harvest year; classification accuracy varies; recipes conservatively start in 2008 |
| [Dynamic World](https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_DYNAMICWORLD_V1) | Per-scene probability screen, then annual class mode | 0.6 threshold is an exploratory processing choice, not validated accuracy |
| [Landsat 8 C2 L2](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1_L2) | QA_PIXEL bits 0–5 and QA_RADSAT screening; RGB × 0.0000275 − 0.2; median | Annual composite, not one dated image |
| [Sentinel-2 SR harmonized](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED) | SCL classes 4, 5, 6; RGB × 0.0001; median | Excludes snow and unclassified pixels; avoids assuming QA60 continuity |
| [JRC GSW v1.4](https://developers.google.com/earth-engine/datasets/catalog/JRC_GSW1_4_GlobalSurfaceWater) | Historical occurrence percentage | Fixed 1984–2021 summary, no annual selection |
| [CHIRPS v2 daily](https://developers.google.com/earth-engine/datasets/catalog/UCSB-CHG_CHIRPS_DAILY) | Complete-year sum in mm | Expected day count, unique UTC days, per-pixel observation count; leap years supported |
| [TerraClimate](https://developers.google.com/earth-engine/datasets/catalog/IDAHO_EPSCOR_TERRACLIMATE) | Twelve-month mean PDSI × 0.01 | Modeled index; expected unique months and per-pixel completeness |
| [3DEP collection](https://developers.google.com/earth-engine/datasets/catalog/USGS_3DEP_10m_collection) | Elevation mosaic ordered by system:index | Replaces deprecated USGS/3DEP/10m; deterministic order is not chronological priority |

Recipes use [TIGER 2018 States](https://developers.google.com/earth-engine/datasets/catalog/TIGER_2018_States),
filtered to `STATEFP=20`. This is a dated study boundary, not present legal
boundary authority. Annual controls are bounded to complete years supported by
the metadata snapshot. The catalog's global coverage does not prove Kansas
pixel availability. The CHIRPS page summary lagged its availability table;
the record uses the table's observed 2026-08-31 endpoint and allows recipes only
through 2025. TerraClimate's last listed month is December 2024. Records are a
dated snapshot, not an automatic catalog refresh.

[Earth Engine access](https://developers.google.com/earth-engine/guides/access)
requires a registered Cloud project and appropriate authentication. No account,
billing configuration, secret, OAuth flow or network adapter is introduced.

## Placement and trust

The supplied sources directory does not contain `Directory Rules.pdf` in this
session. The checked repository's `docs/doctrine/directory-rules.md` and accepted
ADR-0029 supply the placement basis: authority follows responsibility; discovery
does not grant admission or release; deployable application concerns and human
documentation remain separate. The existing standalone Site README already
assigns its application, tests and documentation to `app/`, `tests/` and `docs/`.
This extension uses those homes. It creates no canonical contract, policy,
source descriptor, release record or parallel monorepo root.

`app/earth-engine-data.ts` is a Site-local discovery index and pure text recipe
generator. `app/earth-engine/` owns the UI. Existing source observatory and
contribution selectors consume the same records. New sources have candidate
status and no layer ID. Review JSON explicitly retains `NOT_RUN`, `NOT_ADMITTED`
and `NOT_RELEASED`; it is not an EvidenceBundle, source payload or approval.

Recipes print a bounded first 1000 asset-ID list and its full count. A truncated
list is not complete provenance. Before any downstream use, capture full source
identity, retrieval time, native projection, masks, resampling, transforms,
integrity, rights, sensitivity, validation and correction/rollback records.
The scripts preview data only when the user runs them outside KFM; they contain
no automatic export or write operation.

## Validation and rollback

Changed-area tests cover invalid and out-of-range requests, leap-year and missing
period behavior, empty/error results, duplicate periods, product-specific
processing, recipe syntax, and non-admitting review drafts. Worker-rendered route
checks follow a production build. These checks cannot prove authenticated Earth
Engine execution, image rendering, scientific fitness or data admission.

Session results: production build passed; all 140 existing and new tests passed;
TypeScript checking and changed-module lint passed. The built worker rendered
both the new route and its Explorer links, and the local preview returned HTTP
200. Interactive/visual browser QA remains unverified: the browser tool could not
verify its admin-enforced security policy and denied access. No alternate browser
path was used to bypass that check. Authenticated Earth Engine execution remains
unverified and is labeled in the UI and every generated draft.

Rollback: restore the prior Site version 66, or revert this bounded source change
and build a new version. No stored contribution, provider data, database schema,
access audience or monorepo source was migrated. Deployment rollback itself
requires normal same-Site authorization and verification.
