# Historical topographic display transformation

`historical_topo_tiles.py` verifies the saved USGS GeoTIFF against its capture
receipt, reads its actual CRS and affine transform, and reprojects its pixels
into transparent EPSG:3857 map tiles. The output contains one immutable
manifest with source identity, original digest, geographic bounds, native
detail zoom and every tile digest. It is a candidate display carrier, not
historical-feature evidence or a release decision.

Use Python 3.12 with the adjacent hash-locked requirements, then run the
preparer against external directories. The maintainer entry point is
`tools/historical_topo_worker.py --site <owner-private-origin> --raw
<external-raw-dir> --packages <external-package-dir>`. Set
`KFM_HISTORICAL_WORKER_TOKEN` and, if private dispatch requires it,
`KFM_SITES_BYPASS_TOKEN` in the worker environment. `--request <queue.json>
--dry-run` performs an offline preparation rehearsal without staging. The
worker uploads tiles and a manifest idempotently; an owner still reviews and
activates the candidate in the Explorer. Rerunning from the same captured
bytes produces the same tile hashes and manifest bytes.

Preparation rejects missing georeferencing and packages over 5,000 tiles or
500 MB. The source's georeferencing supports display alignment but cannot
erase positional error in a historical printed map. The scan's printed scale
is distinct from screen zoom.
