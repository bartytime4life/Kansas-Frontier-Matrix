# Basemaps on this PC

The owner selected a **10,000,000,000-byte (10 GB)** cap with automatic removal
of least recently used cache entries. No originals, admissions, receipts,
Earth Engine snapshots, radar frames, thermal observations, or report data are
stored or evicted by this service.

## Location and operation

The existing initialized external KFM data root on this PC is
`/home/bartytime/Projects/KFM-data`. The disposable namespace is
`data/work/basemap-cache/` beneath that root. It contains hashed provider bytes
and an SQLite index with original URL, retrieval/expiry times, SHA-256, size,
ETag and provider Last-Modified. Retrieval time is never an observation time.
Provider imagery dates, attribution, unknown coverage and source resolution
remain unchanged. Expired tiles require a successful provider refresh; failed
refreshes are not represented as current imagery or clear conditions.

Run with Python 3.11 or newer (standard library only):

```sh
# From the KFM monorepo root:
python3 tools/local_data/basemap_cache.py --root /absolute/path/to/KFM-data
```

The server listens only on `127.0.0.1:8770`. It requires the exact owner-private
Site origin (or local preview ports 4173/4194), the loopback Host header, and a
per-process session token for tile requests and download controls. Redirects,
arbitrary URLs and symlink roots are rejected. No credentials are forwarded to
providers. The browser may require permission to access the local network.

**Layers → Tune this view → Basemaps on this PC** shows destination, usage,
tile count, session disk hits and download progress. It offers reconnect, a
local-use checkbox, **Save Kansas overview**, and **Stop download**. The main
map, detached surface, 3D detail renderer and saved-view preview share the
transport. Source styles and URLs remain untouched. Provider network fallback
keeps maps usable when the service is stopped. The checkbox disables local
reads/writes for subsequent browser map requests; it does not cancel a running
overview job (use Stop download).

For startup at sign-in, install a reviewed copy of the script under an
owner-private stable directory, then create a user systemd unit:

```ini
[Unit]
Description=KFM bounded local basemap cache
After=network-online.target
[Service]
Type=simple
UMask=0077
ExecStart=/usr/bin/python3 /absolute/path/to/KFM/tools/local_data/basemap_cache.py --root /absolute/path/to/KFM-data
Restart=on-failure
RestartSec=5
NoNewPrivileges=true
[Install]
WantedBy=default.target
```

Enable/start it with `systemctl --user enable --now kfm-basemap-cache.service`.
Stop/disable with `systemctl --user disable --now kfm-basemap-cache.service`.
This does not affect the separate Earth Engine operator. To reclaim space,
stop the service first and remove only its dedicated `data/work/basemap-cache`
directory. The UI deliberately has no broad delete-data operation.

## Bounds and source policy

- 10 GB total budget, including 64 MiB reserved for bounded in-flight files and
  SQLite overhead. Objects count allocated 4 KiB blocks. SQLite is capped at
  16 MiB, with at most 100,000 indexed objects. Two provider downloads at a time;
  each resource is limited to 8 MiB. No full-planet or high-resolution statewide
  download is attempted. Originals and other KFM lanes are never eviction targets.
- A Kansas overview saves Kansas aerial and USGS topo tiles at zooms 4–9. Each manual run
  stops before exceeding 512 MiB. Detail tiles are saved as viewed, preserving
  their original provider bytes and zoom level. This partial cache does not
  provide a fully offline app, styles/fonts, or guaranteed coverage.
- **Kansas NG911 2024:** on-demand 512-pixel images from the exact existing
  image service, refreshed within 30 days or sooner if provider cache headers
  require it. The service advertises `allowCopy: true`. Kansas DOT's
  [FFY2025 program](https://www.ksdot.gov/home/showpublisheddocument/12262/638941468941030000)
  describes public-domain publication of statewide NG911 orthoimagery.
  The source remains February–April 2024, approximately 1 foot; exact local
  flight date is unresolved and independent of map time.
- **OpenFreeMap:** vector tile URLs retain their provider edition; maximum
  cache age one day because the provider can substitute the latest edition for
  expired version URLs. Natural Earth tiles use at most 30 days. The
  [official project](https://github.com/hyperknot/openfreemap) provides reusable
  downloads and describes version behavior. Attribution remains visible.
- **USGS topo:** at most seven days, respecting shorter provider cache headers.
  [USGS terms](https://www.usgs.gov/faqs/what-are-terms-uselicensing-map-services-and-data-national-map)
  permit copying map services; provider attribution remains on the map.
- `no-store`, `private`, and `no-cache` responses are not persisted. No stale
  offline fallback is used. Refresh intervals describe cached delivery, not
  the age of imagery or surveys.
- **Esri imagery and OSM raster** are not routed through this service. OSM's
  [tile policy](https://operations.osmfoundation.org/policies/tiles/) forbids
  offline prefetch on its standard public raster endpoint.

All bytes are **display context, not KFM evidence**. No source-admission,
activation, source-time, DB/R2 binding, or audience change is made.

## Verification

`node --test tests/basemap-cache.test.mjs` includes client transport/fallback,
source exclusions, rendered GUI actions and Python filesystem/HTTP tests.
From the KFM repository root, `python3 tests/local_data/test_basemap_cache.py`
runs the companion tests directly.
Tests use a temporary initialized root, fake provider bytes and in-memory
HTTP requests; they never alter the installed cache or fetch live providers.
Browser local-network access, actual provider availability and visual acceptance
are separate from these checks and from private Site deployment.
