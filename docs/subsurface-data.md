# Underground display data

This is a dated projection of official, publicly downloadable KGS records for
**external context** in the Underground workspace. It is not an evidence-store
import, an independently verified geological model, or a resource assessment.
The original archives remain outside the application tree. The existing
standalone application's `scripts/`, `public/`, `tests/`, and `docs/` own the
preparation code, display assets, checks, and behavior record respectively;
ADR-0029's Site mirror remains under `apps/site/source` in the main repository.

## Snapshot and coverage

Captured 2026-10-06. `public/data/subsurface/manifest.json` pins each original
archive by SHA-256 and its own retrieval time. Archive edition dates are distinct
from individual record dates. The well, lithology, and core inventories were
published September 11, 2026. The interpreted-log archive has an independent
March 27, 2025 last-modified date; that date is not an observation date.

| Included projection | Count |
| --- | ---: |
| Mapped WWC5 records | 314,844 |
| WWC5 records with valid logged intervals | 245,750 |
| Original logged intervals | 1,599,345 |
| Exact-matching standardized-code annotations | 953,599 |
| Mapped Kansas core-library identities | 6,598 |
| Valid core inventory ranges | 5,372 |
| Core identities with provider photo links | 406 |

The 257 adaptive spatial tiles start at half-degree cells and subdivide until
they are below 3 MB uncompressed. Tiles total 19,349,349 compressed bytes;
the statewide locator is another 3,550,680 bytes. The locator is loaded only
for statewide discovery. No images are downloaded, redistributed, or treated as
textures by this pipeline.

The complete source tables contain 315,254 well rows, 1,615,923 original log
rows, 964,516 interpreted rows, and 7,394 core rows (including other states).
The manifest separately counts exclusions: 410 unlocated or out-of-region well
rows; 382 Kansas core rows without eligible coordinates; 412 out-of-state core
rows; two malformed core rows; 15,739 invalid log intervals; 16 exactly duplicate
log intervals; and valid intervals whose well cannot be mapped. Invalid or
absent core ranges do not remove an otherwise valid core location. Missing
intervals stay missing; overlaps stay overlapping. No thinning by county or
interpretation availability occurs.

## Sources, references, and limitations

- [KGS WWC5 downloads](https://www.kgs.ku.edu/Magellan/WaterWell/) provide the
  well and original-log archives. The
  [provider metadata](https://www.kgs.ku.edu/Magellan/WaterWell/wwc5_fgdc.html)
  describes public access and provider accuracy/completeness disclaimers. These
  data include submitted records that have not had general accuracy review.
- [KGS OFR 2020-13](https://www.kgs.ku.edu/Publications/OFR/2020/OFR2020-13.pdf)
  explains the separate, subjective standardized lithology codes. Its logged
  depth examples are in feet; it documents NAD83 coordinate columns and the
  need for ground elevation to relate interval depths to elevation. Codes are
  attached only when well identity, top, bottom, and normalized description all
  match the current original interval, with exactly one distinct code result.
  Older interpretations never replace original descriptions, create missing
  intervals, or become measured permeability.
- The [KDHE WWC5 form](https://www.kdhe.ks.gov/DocumentCenter/View/2215/WWC-5-Water-Well-Record-PDF)
  records completed depth in feet. `COMPLE_DATE` can represent construction,
  reconstruction, or plugging; it is displayed as the record date, not the
  current well state or necessarily the lithology observation date.
- [KGS Core Library](https://www.kgs.ku.edu/Magellan/CoreLibrary/) provides
  inventory ranges. The associated
  [well-header metadata](https://www.kgs.ku.edu/Magellan/Qualified/ogwell_fgdc.html)
  documents NAD27 positions and feet-based drilling depths, which may be
  referenced to the Kelly Bushing. The projection therefore marks these ranges
  `drilled-depth`, leaves total well depth null, and does not register them as
  true vertical depth below terrain. Inventory start/end is an envelope and
  does not prove continuous recovery or lithology. Detailed box intervals
  remain available in the source record.
- [KGS core photographs](https://www.kgs.ku.edu/Magellan/CoreLibrary/image.html)
  are linked only when the snapshot's `PHOTOS` value is exactly `YES`. The
  dated photograph flag does not guarantee the provider is available today.

This projection asserts neither a Creative Commons license nor source admission
into KFM evidence. It retains attribution and limitations from the official
public-download sources. The original owner, operator, lease, private-direction,
water-right, contractor, and other identifying fields are excluded. Generic
provider record identifiers label the map. Original geological log text remains
in the projection; source pages may independently expose additional fields.

### Horizontal and depth reference

WWC5 uses explicit `NAD83_LONGITUDE` and `NAD83_LATITUDE`, never the older NAD27
columns. Display conversion uses EPSG:1188, NAD83 to WGS84 (1), a documented
zero-offset approximation with 4-metre stated operation accuracy. This is not
an estimate of well-location accuracy: most locations are derived from PLSS
legal descriptions and may be much less precise.

Core NAD27 coordinates first undergo the NOAA CONUS NADCON grid shift to NAD83
using [the PROJ distribution of the NOAA grid](https://cdn.proj.org/us_noaa_conus.tif),
pinned by hash in the manifest; the same WGS84 approximation then applies. For
example, transformed core KID 1025687266 is `[-95.287550, 39.872788]`, matching
the provider's NAD83 coordinates at displayed precision. Six decimal places
are display precision, not a claim of surveyed accuracy.

No usable vertical datum or surveyed borehole trajectory is provided by these
archives. Reported WWC5 depths are local logged depth below land surface;
rendering them as schematic columns must not imply measured vertical geometry.
Core ranges remain in their original drilling-depth reference. No numerical
surface elevation is imported or synthesized. Raster colors, interpreted log
codes, and nearby observations are never converted into continuous strata.

The Kansas bounds `[-102.1,36.9,-94.5,40.1]` are a regional eligibility check,
not an exact state polygon. Core rows also require `STATE_CODE=Kansas`.
County navigation coordinates are arithmetic means of included WWC5 positions,
not authoritative county centroids. Core inventory does not supply county names;
its locator county field remains empty rather than being guessed.

## Asset contract

`manifest.json` has version 1, captured time, four source entries, tile entries,
count totals, 105 county navigation entries, locator metadata, transformation
provenance, field exclusions, and coverage/use limits. Each tile entry has
`id`, `[west,south,east,north]` bounds, URL, record/well/core counts, SHA-256 of
the compressed bytes, and compressed/uncompressed sizes.

Each `.json.gz` tile is a JSON array of records:

```text
{id, sourceId, kind, name, coordinates:[longitude,latitude],
 coordinateReference, locationMethod, sourceUrl, sourceTime,
 depthUnit:'ft', depthReference:'land-surface'|'drilled-depth',
 totalDepth:number|null,
 intervals:[{top,bottom,description,interpreted?}], photosUrl?}
```

`sourceId` is `kgs-wwc5` or `kgs-core`. `interpreted` is the provider's literal
lithology-code list, kept distinct from `description`. No new category is
invented. IDs are `wwc5-WELL_ID` or `core-WELL_KID`. Duplicate core identities
merge distinct inventory ranges; conflicting coordinates fail preparation.
All source and photo links use fixed HTTPS KGS endpoints and numeric IDs.

`locator.json.gz` is a compact JSON array with rows:

```text
[id, countyOrEmptyString, [longitude,latitude], tileId]
```

The manifest's `locator.columns` declares that order. Record identity and
coordinates are sufficient to navigate, after which the matching spatial tile
supplies the original logs. Both index and tiles are deterministically sorted
by identity. The worker must check tile coverage and honor missing-data states;
the manifest describes the available archive, not complete subsurface knowledge.

## Reproduction and checks

Use Python 3.10+ and a disposable environment with `pyproj==3.7.1`. Do not add
this preparation-only dependency to the deployed application's package list.
Run:

```sh
python scripts/prepare-subsurface.py --input-dir /absolute/path/outside/site/kgs-cache
node --test tests/subsurface-assets.test.mjs
```

The preparer downloads only the four pinned archives and the pinned NOAA grid.
It rejects changed hashes and corrupt/malformed archive layouts. Original files
are cached outside the source tree, and temporary joining tables are removed
when preparation finishes. Deterministic gzip output has a zero timestamp.
To qualify a future source edition, review its metadata and differences before
updating pinned hashes and capture details; do not treat archive currentness as
observation currentness. Projection does not call backend APIs, migrate a
schema, or modify DB/R2 bindings.

Checks cover all tile hashes and counts, bounded decompressed sizes, field
allowlists, deterministic unique identities, original/interpretation separation,
recorded gaps and overlaps, missing/invalid ranges, locator consistency, 105
county entries, allowlisted links, and the exact source-row accounting.
