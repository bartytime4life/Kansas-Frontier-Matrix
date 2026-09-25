# Earth Engine processed context for Kansas

This is a Site-local, owner-only visual display path. It does not admit a KFM
source, supply claim evidence, or connect the Site to live Earth Engine. The
Google Cloud project ID, Earth Engine authentication, Google Drive exports,
source inventories and review records stay outside Git and the Site.

## Dataset and time contract

| Layer | Catalog source | Source period | Processing and display grid |
| --- | --- | --- | --- |
| Crop classes | [USDA CDL](https://developers.google.com/earth-engine/datasets/catalog/USDA_NASS_CDL) | 2024 harvest year | One categorical image, nearest-neighbor, EPSG:5070 at 30 m |
| Rainfall | [CHIRPS daily](https://developers.google.com/earth-engine/datasets/catalog/UCSB-CHG_CHIRPS_DAILY) | All 366 days of 2024 | Sum in mm; all daily pixels required; native 0.05° grid |
| Drought index | [TerraClimate](https://developers.google.com/earth-engine/datasets/catalog/IDAHO_EPSCOR_TERRACLIMATE) | All 12 months of 2024 | Mean PDSI × 0.01, unitless; all monthly pixels required; native 1/24° grid |
| Satellite composite | [Sentinel-2 SR harmonized](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED) | 2024 calendar year | SCL 4/5/6, B4/B3/B2 × 0.0001, median and retained-observation count; EPSG:5070 at 30 m |
| Elevation | [3DEP 10 m collection](https://developers.google.com/earth-engine/datasets/catalog/USGS_3DEP_10m_collection) | Mixed acquisition dates | Ordered elevation mosaic in meters; EPSG:5070 at 30 m; dates and vertical datum require separate review |

The study boundary is [TIGER/2018/States](https://developers.google.com/earth-engine/datasets/catalog/TIGER_2018_States), filtered to `STATEFP=20`. The 30 m display transform is `[30,0,-1200000,0,-30,2400000]`; it intentionally reduces the Sentinel-2 and 3DEP source resolution. The climate products retain their coarser source grids. The Site offers annual layers only while the map shows 2024. The terrain layer keeps its mixed-date label regardless of map year.

## Private processing and approval

1. Register and verify a noncommercial Earth Engine project through [Google's access workflow](https://developers.google.com/earth-engine/guides/access). Use the project only in the owner's Earth Engine session. Never place the ID, token or service-account credential in this repository, environment variables for the Site, or browser application code.
2. Download the small-area Drive recipe for each layer from the Site's Earth Engine workspace. Run it in the owner's Earth Engine Code Editor, review the count/time checks and task, then copy the completed GeoTIFF to `<private-data-root>/exports/<layer>/sample.tif`. Keep the original Drive file and task ID. The sample is the fixed rectangle `[-99.5,38.2,-99.3,38.4]` intersected with Kansas.
3. Capture the full source image ID inventory, not a truncated console list. Keep it as a private CSV or JSON beside the export. Save the `TIGER/2018/States` Kansas feature privately as `kansas_tiger2018.geojson`. A Google GeoJSON export may wrap a polygon and a tiny detached line in a GeometryCollection; preserve the original and normalize the polygon explicitly for raster coverage checks. Record both hashes.
4. Check the Google Drive free-space margin against a documented estimate before each statewide run. The high-resolution statewide recipes use 2048-pixel GeoTIFF shards so every file can be retrieved and checked independently. This changes file packaging, not area or pixel resolution. A quota or export failure holds the affected product; do not reduce its area or resolution to hide the failure. [Google's export guide](https://developers.google.com/earth-engine/guides/exporting_images) describes Drive export, CRS, affine transform and GeoTIFF options.
5. Save every statewide shard under `<private-data-root>/exports/<layer>/shards/`. For CDL, Sentinel-2 and 3DEP run `scripts/earth-engine/assemble_statewide.py --data-root <private-data-root> --layer <layer>`. It checks each shard's alignment, band layout and overlap, writes a BigTIFF with nodata in gaps, and records every shard hash in `assembly.json`. Climate exports are single `statewide.tif` files at native resolution.
6. Review each product independently: completed task ID, sample and statewide hashes, exact source IDs, time coverage, units, masks, source terms, resampling, nodata, grid, Kansas coverage and visible appearance. For 3DEP, inspect source acquisition dates and vertical datum. Keep the complete Earth Engine ID export as `exports/<layer>/source_ids.csv`. Write a private `exports/<layer>/review.json` only for a passing layer. Set `status` to `APPROVED_VISUAL_CONTEXT`, `samplePassed`, `statewidePassed`, `driveCapacityChecked` and `termsChecked` to true; include `sourceImageIds`, `sourceInventoryTaskId`, `sourceInventorySha256`, `sampleTaskId`, `statewideTaskId`, `sampleGeoTiffSha256`, `statewideGeoTiffSha256`, `boundarySha256`, `units`, `resampling`, `masks`, `terms`, `processingParameters`, `reviewer`, `approvedAt`, and `limits`. CDL also requires `paletteSha256`; 3DEP requires `acquisitionDateReview` and `verticalDatumReview`. The preparation script compares the reviewed IDs with the hashed CSV and validates the actual rasters. Never use a passing QA number alone as review approval.
7. Run `scripts/earth-engine/prepare_display_set.py --data-root <private-data-root>` with the isolated Python dependencies in `scripts/earth-engine/requirements.txt`. It checks hashes, grids, ranges and Kansas pixel coverage; holds failed products independently; generates immutable PNG tiles, per-zoom tile hashes, a manifest, and `active.json` under `display-sets/<set-id>/earth-engine-context/v1/`. Keep the entire output outside Git.

The minimum statewide coverage thresholds are 99.5% for CDL and 3DEP, 99% for CHIRPS and TerraClimate, and 95% for Sentinel-2, all evaluated inside the Kansas feature. A sample needs at least 95%. CHIRPS and TerraClimate also require per-pixel counts of 366 and 12, respectively. Sentinel-2 requires at least one retained clear observation per pixel. Each threshold is a review gate, not a claim of scientific accuracy.

## Site installation and rollback

The Site reuses its existing private `BUCKET` R2 binding under the separate `earth-engine-context/v1/` prefix. Configure `KFM_EARTH_ENGINE_OWNER_IDS` or `KFM_EARTH_ENGINE_OWNER_EMAILS` through Sites environment settings; it is an owner allowlist, not an Earth Engine credential. A missing allowlist or storage binding fails closed. Site access remains owner-only.

After code checks and independent raster review, deploy the owner-only Site version, then open `/earth-engine-context/install` as the owner. Choose the prepared display-set folder. The installer hashes every file, uploads only allowed immutable set paths through the owner-authenticated staging route, and requests readback. It can activate only after every manifest-listed tile exists. The only mutable R2 object is `active.json`; activation archives its previous bytes. The tile route checks owner identity, current set ID, manifest and index hashes, exact tile membership, PNG signature, and tile hash. A missing tile returns unavailable; it never falls through to another layer or public basemap.

Review the hosted owner-only display at desktop and mobile sizes in both 2D and Globe: controls, opacity, legend, source dates, attribution, 2024 gating, terrain's mixed-date label, missing-tile state and existing layers. If hosted review fails, roll back the Site to its prior version and restore the previous display-set pointer; there is no database migration. Keep the staged monorepo checkout and external data store untouched.

The installed map says “Processed snapshots available. Live Earth Engine remains disconnected.” The statement appears only when a valid active manifest is present. Pixel colors and clicks remain visual context, never KFM claim evidence.
