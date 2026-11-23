# NEON terrain and vegetation pilot

The Explorer's Appearance controls and acquisition lab offer **Load Konza Prairie pilot**. Loading is explicit; **Show on map** and **Fit preview** remain separate actions. Local JSON import remains available. The pilot is historical provider context and is not admitted KFM evidence or a field-accuracy claim.

The selected footprint is one 1 km tile: `NEON_D06_KONZ_DP3_706000_4336000`, KONZ, catalog month September 2024, acquisition `2024_KONZ_10`, `RELEASE-2026`. DTM/DSM use `DP3.30024.001`; provider canopy uses `DP3.30015.001`. Three originals total 8,331,760 bytes. Their reported CRC32C checksums were verified on dev; local SHA-256 records preserve exact bytes. CRC32C is Castagnoli, not IEEE CRC32, and verifies transfer integrity rather than scientific accuracy.

## Data path and credentials

NEON account access, originals and NumPy/Rasterio processing stay on the dev workstation. The public Node app uses the existing signed, outbound-only [local data relay](local-data-relay.md):

```text
Explorer GET /api/neon/preview
  -> existing site's signed relay
  -> dev worker -> loopback gateway GET /v1/neon/preview
  -> one explicitly configured derived package
  -> signed reply -> site cache -> Explorer
```

This path does not use `NEON_TOKEN` on GoDaddy. Its existing private **Secrets** settings remain `KFM_LOCAL_DATA`, `KFM_LOCAL_DATA_ORIGIN`, and the gateway/worker key IDs and secrets described in the relay runbook. Do not replace those keys with the NEON token. The token is a different provider credential, saved outside Git on dev in a mode `0600` file inside an owner-only `0700` directory. Acquisition tools read it through `--token-file`; it never enters browser code, URLs, preview packages or logs.

The dev gateway additionally accepts these private local environment settings:

| Setting | Meaning |
| --- | --- |
| `KFM_NEON_PREVIEW_FILE` | Absolute path to the single reviewed derived `public.json` package on dev |
| `KFM_NEON_PREVIEW_SHA256` | Exact `sha256:<64 lowercase hex>` pin for that package |

The gateway refuses missing/unsafe files, symlink paths, shared permissions, hard links, oversized/changing files, a wrong hash, a different product/footprint or credential-like payload fields. The caller cannot supply a filesystem path. No directory or RAW file is served. The package must be at most 950,000 bytes; the complete signed/public response retains the existing 1,000,000-byte relay ceiling. No SQL database is opened for this route.

Install the reviewed gateway and worker modules on dev before a site that calls the new route. Use the existing release installer and preserve the prior release, settings and services for rollback. Configure only the explicit derived package, then verify its signature, hash, availability and cache labels. No database migration or new GoDaddy secret is required for this feature. Source and private local preparation alone do not establish installation, activation, publication or live delivery.

## Science and known limits

The native rasters share a 1000 by 1000 grid, 1 m spacing and aligned UTM zone 14 coordinates. A 100 by 100 preview displays the nearest native pixel to each 10 m cell center. It is neither a cell mean nor a maximum. NoData stays distinct from zero. The map transforms display-cell corners with Rasterio/PROJ offline and leaves heights unchanged.

The checksum-verified provider READMEs describe DTM/DSM values in metres above NAVD88, Geoid12A realization. The GeoTIFF band unit tags are absent. The rasters record a WGS84 UTM horizontal CRS, while the product descriptions name ITRF00 UTM. Epoch, frame equivalence and independent vertical/horizontal accuracy remain unresolved; the map uses the recorded raster CRS. No datum conversion or numeric accuracy is invented.

Provider canopy is calculated separately from the normalized point cloud using a pit-free algorithm. It is not `DSM - DTM`. Five native canopy cells exceed 50 m; the native maximum is 83.41000366210938 m. At that maximum, `DSM - DTM` is 11.28997802734375 m. These retained provider outliers need review and are not verified tree heights. The entire tile's maximum `DSM - DTM` is 32.5 m. A zero canopy value may reflect sensor-specific processing suppression; the acquisition sensor and applicable floor have not been verified. Canopy color saturates at 30 m while exact readouts retain the source value.

Flight QA reports have not been independently reviewed. Field accuracy, species, biomass, carbon and bare-ground classification are not established. The preview shows its historical acquisition, source hashes, pending review, cache time and any stale cache state. `cache.state: live` means a fresh relay exchange, not a current observation.

NEON account/data access and the local open-source processing path add no paid API, subscription, cloud account or billing integration. The feature uses the existing hosting and PC relay. Preserve provider attribution and the current [NEON data usage and citation policy](https://www.neonscience.org/usage-policies), and consult the [NEON LiDAR methods](https://www.neonscience.org/data-collection/lidar) for product and sensor context.

## Verification and rollout boundary

The candidate passed 31 NEON UI tests, 17 acquisition/terrain regressions, four signed-artifact tests, 11 existing relay tests, TypeScript, focused lint and a production build. All six existing SQL dataset cases passed on dev's Node 22.23.4 runtime; the workstation's older Node build lacks SQLite R-tree. All 27 scientific/capture/credential tests passed inside dev's pinned Python 3.12 / NumPy 2.2.6 / Rasterio 1.4.3 environment.

The actual derived package passed both the gateway and browser-client parsers, and the locally built production app returned it through an in-process signed test bridge. This is local HTTP evidence using dummy relay keys, not a live PC-to-GoDaddy exchange. Fresh Chrome desktop/mobile acceptance, current provider Published identity, dev-service activation and public deployment remain separate checks. Roll back application and PC module release together; retain original rasters and receipts.
