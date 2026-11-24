> This describes the retained fixed-capture example. Current Kansas-wide map layers use the viewport pipeline in [kansas-lidar-backend.md](kansas-lidar-backend.md) and [kansas-lidar-layers.md](kansas-lidar-layers.md).

# Native LiDAR points in Terrain & elevation

Terrain & elevation combines continuous ground context with selected, dated
source layers. Ground, surface and canopy rasters reuse the existing NEON
controller and [Terrain Science](neon-science-tools.md) samples. Native points
are original laser-return records, served separately from those raster samples.
No provider token is sent to a visitor or added to GoDaddy for point access.

## Data contract and reuse

`GET /api/lidar/points` returns a `kfm-lidar-points-manifest-v1` manifest.
`GET /api/lidar/points/{id}` returns its fixed numbered chunks. These use the
existing signed, outbound-only [dev data relay](local-data-relay.md), site cache,
and unchanged 1,000,000-byte reply ceiling. Requests accept no query, native
filename, filesystem path, provider URL, processing command or credential.

The manifest identifies capture, source assets, hashes, CRS, vertical-reference
limits, encoding, selected footprint, height range, exact chunk counts and pending
scientific review. Rows have eleven columns, in this order:

```text
x, y, z, intensity, classification, returnNumber, numberOfReturns,
classFlags, gpsTime, asset, record
```

XYZ are native EPSG:3857 coordinates and source elevation metres. `asset` indexes
the manifest's public source LAZ assets; `record` is its original zero-based EPT
LAZ record index. Distinct coincident returns retain distinct identities. Source
readings remain unchanged when display exaggeration, point size or color changes.

The pure model in `app/native-lidar.ts` and bounded client in
`app/native-lidar-client.ts` are reusable by other KFM science tools. Consumers
must retain source/review/cache metadata and withheld flags, verify the complete
manifest and every chunk, reject repeated source-record identities, and cancel
superseded work. Limits are 100,000 rows, 16 chunks, 16 MiB aggregate, two
concurrent chunk requests, 900,000 bytes per private chunk and 64,000 bytes per
private manifest. An unavailable capture has no inferred zero values.

Manifest chunk hashes describe exact private prepared artifact bytes. The dev
gateway verifies these before signing replies. HTTP responses add gateway/cache
metadata, so those private-artifact hashes are not advertised as HTTP-body hashes.
Native asset SHA-256 hashes record captured-byte/readback integrity; the provider
did not publish expected SHA-256 hashes for this capture.

## Actual initial native capture

The free public source is
[USGS KS_Statewide_B6A_2018 EPT](https://usgs-lidar-public.s3.amazonaws.com/KS_Statewide_B6A_2018/ept.json).
Its native EPT nodes `8-92-179-127.laz` and `9-185-358-254.laz` contain
30,058 and 63,514 records. The prepared capture selects their common finer-node
XY footprint and retains all selected Z values. It has 72,595 records in twelve
chunks, with native elevations 353.522–379.597 m. It is an additive-LOD subset
within a bounded footprint, not full-density or statewide native point coverage.
See the [EPT specification](https://entwine.io/en/latest/entwine-point-tile.html):
full resolution requires accumulated overlapping hierarchy levels.

There are 49,950 class-2 ground records, 22,517 class-1 unclassified records,
and 128 class-7 low-noise records. Class 1 is not a vegetation classification.
All 128 low-noise records carry the withheld flag; they remain in the data and
are excluded from default rendering. Native ClassFlags retain synthetic=1,
key point=2, withheld=4 and overlap=8. No RGB was supplied: colors encode the
selected measured attribute and are not aerial imagery.

Actual EPT node headers are LAS 1.2 / point format 1, including an extra-byte
ClassFlags dimension. Original source-file metadata describes LAS 1.4 / format 6;
these formats are not treated as identical. GPS values are retained as raw
numeric values; the node header identifies GPS week time but no GPS week,
adjusted-standard time or calendar flight time is inferred. The 2018 project
label and LAS creation date do not establish the flight interval.

Provider original-tile metadata describes NAVD88 / Geoid12B metres; EPT omits a
vertical code. Independent point accuracy and registration to the displayed DEM
remain unverified. Do not interpret point-minus-displayed-DEM as canopy height or
co-registration error. Millimetre coordinate encoding is not millimetre accuracy.
The renderer uses WebMercator's equatorial radius for XY and the installed
MapLibre altitude conversion's mean Earth radius for Z; these are distinct.

## Dev installation and rollback

Original LAZ files, capture receipts and prepared JSON stay outside Git on dev's
DATA14TB drive. The gateway needs only two additional private settings:

| Variable | Value |
| --- | --- |
| `KFM_LIDAR_POINTS_DIR` | Absolute owner-private prepared capture directory |
| `KFM_LIDAR_POINTS_MANIFEST_SHA256` | Exact `sha256:<64 lowercase hex>` manifest pin |

Directory mode is 0700 and artifact mode is 0600; files must be regular,
single-link, owner-owned, bounded, unchanged during read and hash-pinned.
Symlink paths and extra/unapproved public fields are refused. The gateway
exposes only a manifest and numbered chunks 0–15. No native file directory is
served and no database is opened for these routes.

Install a successor of the current gateway and worker together, preserving the
active NEON/water repairs, existing dataset files, credentials and previous
systemd drop-ins. Add the two point settings in a separate owner-private file.
Before activation, check source hashes and load every actual chunk. Afterward,
verify signed loopback HTTP for all chunks, unchanged NEON data, current readiness
of all 22 datasets and unchanged reply limits. Revert only the new source
drop-ins to restore the prior release; retain native originals and receipts.

The 2026-11-24 dev activation verified all 72,595 original record identities and
all exported attributes against native LAZ records. Reconstructed source integer
XYZ matched exactly. The signed loopback HTTP check delivered every chunk and
kept all 22 datasets ready; existing environment files and prior drop-ins were
byte-unchanged. This is dev-service and native-data evidence, not public GoDaddy
publication, Chrome/GPU acceptance, source admission or field-accuracy approval.

This path uses free public data, existing storage/hosting and local open-source
processing. It adds no paid API, cloud storage account or subscription.
