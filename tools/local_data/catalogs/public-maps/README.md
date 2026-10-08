# Public map discovery inspection index

This folder preserves public bibliographic metadata and a discovery receipt for
review. It is a local-data tool input/evidence artifact, not a governed
`data/catalog/` projection, source admission, map-original archive, or publication.
The researched Site seed remains separate in
`apps/site/source/app/public-map-catalog.json`.

The 2026-10-08 capture reconciled all **2,270 unique NGMDB Kansas search IDs**
across 23 serial requests. The explicit publisher selection contains **944 USGS**
records (1892–2026) and **741 Kansas Geological Survey** records (1896–2026).
The remaining 585 records from other publishers are outside this index. The supplied search
URL contains `publisher_list=usgs`, but the live endpoint returned all publishers;
the adapter therefore checks each record's `published_by` field.

- `public-map-metadata-20261008.jsonl`: 1,685 records, one JSON object per line,
  sorted by source ID and catalog record ID. Each retains the provider's complete
  raw result object, metadata URL, stable ID, and rights status. No image, map,
  raster, vector payload, or full publication text is stored here.
- `discovery-20261008.json`: source URLs supplied by the owner, coverage counts,
  the 23 successful metadata-request SHA-256 receipts, index checksum/size, and
  checksum/size of the full external runtime snapshot. That snapshot contains
  1,695 display records including ten retained researched references.

The snapshot was subsequently augmented from the curated seed at
2026-10-08T18:09:04Z with verified regional and national archive choices, CNGM
service references, and explicit unknown CRS/spatial-accuracy defaults. A further
augmentation at 2026-10-08T18:29:28Z added the four ScienceBase provider MD5 checksums
for Limon/Lamar ZIPs as metadata. These checksums are not a claim that local
archive payloads were downloaded or verified. `seedAugmentation` records the
latest separate operation. The original discovery time,
coverage checks, response receipts, and 1,685 raw provider records are unchanged;
the receipt binds the augmented snapshot bytes. Archive sizes were checked from
response headers without downloading their payloads.

The NMMR source remains **unavailable**: its HTTPS certificate could not be
verified. Its one researched reference remains available without an invented
zero-record or complete-coverage claim. The OSMRE catalog and ArcGIS Experience
are interfaces to the same mine-map repository. Future point discovery is
explicitly scoped to a Kansas bounding rectangle, not exact state membership
or a complete inventory of mines or archival maps.

KGS rights remain **held**. NGMDB `online`, `gis`, and `formats` values are source
metadata flags; they do not establish file availability, georeferencing,
redistribution permission, data admission, or local download completion.
There were **zero map-original downloads** during this discovery.

## Reproduce or refresh

Run bounded discovery from the repository root. The output must be a new path
outside the Git tree. Fresh provider metadata may differ from this dated capture.

```sh
python tools/local_data/public_map_catalog.py --output /tmp/kfm-map-catalog-new.json
```

The complete protected runtime snapshot belongs at
`<KFM_DATA_ROOT>/data/work/public-map-downloads/catalog.json`, using the download
manager's atomic, permission-checked snapshot path. Do not substitute this compact
inspection index for the runtime catalog or overwrite the Site seed with it.

The deterministic review-bundle helper reproduces index/receipt bytes from an
unchanged snapshot. Verify the snapshot SHA-256 against the existing receipt
before claiming an exact replay. This example writes new files only:

```sh
python - /tmp/kfm-map-catalog-new.json /tmp/kfm-map-index-replay <<'PY'
from pathlib import Path
import sys
from tools.local_data.public_map_catalog import build_review_bundle

snapshot = Path(sys.argv[1]).read_bytes()
output = Path(sys.argv[2])
output.mkdir(mode=0o700)
for name, content in build_review_bundle(snapshot).items():
    with (output / name).open('xb') as stream:
        stream.write(content)
PY
```

The discovery receipt binds request-response bytes by checksum. The compact
index preserves provider result objects, not full response envelopes or debug
internals; those response envelopes are not claimed to be replayable offline.

Focused validation:

```sh
python -m pytest tests/local_data/test_public_map_catalog.py -q
```
