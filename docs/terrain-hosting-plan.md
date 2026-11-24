# KFM terrain: GoDaddy delivery, dev processing, visitor workspace

For the wider website, archive, AI, media and browser design, see [KFM resource placement and loading](resource-placement.md).

Owner direction, 2026-11-24: optimize the actual Kansas Frontier Matrix website across the existing GoDaddy app `urdng3v1vk` and dev PC; use the approximately100GB of existing hosting storage they report, without new costs. The localhost preview is a verification surface, not the destination. Account remaining quota is not independently readable through the connected GoDaddy tools.

## Implemented candidate

| Item | Location and purpose | Bound |
|---|---|---|
| Standard statewide Ground overview | Shipped with the GoDaddy application, `public/data/terrain/kansas-ground-overview-v1.json` | 195,650bytes;96x96 output grid; exact version/hash; not statewide native1m detail |
| Prepared Ground receipts and native Surface/Canopy grids | GoDaddy `public/assets/kfm-terrain-cache-v1/`, compressed copies of schema-validated public outputs received through the signed dev relay |1GiB total,2048entries,1,004,096uncompressed bytes per entry,512MiB free-disk reserve |
| Frequently requested prepared data | Existing GoDaddy process memory | Existing64MiB/500entries, shared concurrent request coalescing |
| Raw source rasters, LAZ nodes, archive originals, queues and processing | Existing dev DATA14TB drive | Existing source/worker budgets retained; no move/deletion |
| Heavy math and raster/point processing | Existing dev workers and scientific Python environment | Existing CPU/RAM/queue limits retained; no paid calls |
| Temporary public working data | Visitor browser IndexedDB, shared within this site origin across tabs | 8 MiB conservative / 16 MiB capable-device serialized payload cap; 24 entries; 2 MiB per entry; five-minute reuse; automatically discarded on subsequent access after expiry |
| Landscape preparation | One dedicated terrain worker for the active viewport in each visible tab | Latest job only; cancel obsolete work; 15-second hard deadline; no synchronous heavy fallback |
| Map geometry and inspection | Visitor browser GPU | Same source cells and picking IDs; automatic or explicit lightweight framebuffer; separate visual scale/illumination |

Only the standard overview and public derived output copies go to the host. No token, private environment, SQL database, worker job, raw source archive or optional point chunk enters the disk cache. No new account/service/plan is needed. The current approximately526MB on dev is requested subsets and historical preparation, not all available Kansas raw LiDAR. Moving that small subtotal would not establish statewide installed coverage.

## Request behavior and freshness

1. Validate/canonicalize the visitor's fixed Kansas query. Use the existing bounded memory result if fresh.
2. Restore a host copy on process restart, checking gzip expansion size, HMAC under the existing relay key, exact query/schema, original cache time and parent receipt identity. Native grids are bound to the complete parent receipt. A different query is never silently substituted.
3. For the exact whole-Kansas overview query, a source-hash-pinned bundled overview is available even without dev. Keep provider retrieval/generated dates and coarse spacing. A historical bundled baseline remains usable with the stale label, rather than pretending it is a current survey.
4. For a new area, ask dev through the existing signed outbound relay. Dev prepares/cache-reuses the source, then the host saves the compact validated output for later visitors. First-ever detailed preparation still depends on dev and upstream public providers.
5. Prepared host copies are fresh for24hours; unavailable/processing state keeps its existing short lifetime and is never stored as a ready file. On dev failure, retain the stale label up to7days for expendable dynamic copies. Provider acquisition/retrieval dates are separate from host cache time.
6. GET responses negotiate lossless gzip with `Vary: Accept-Encoding` and an exact-byte weak ETag. Processing responses use max-age0; completed HTTP results use the existing60/300second bounds. All scientific numbers, source identifiers and no-data masks remain exact after compression.

The cache stops adding files when its capacity or free-disk reserve is reached and falls back to existing memory/relay behavior. It does not silently prune originals or existing host files. Runtime cache writes do not change the application source digest or the existing browser-asset retention limits. Copy formats/namespace must be advanced if an incompatible processing recipe is introduced.

## Measured verification, not live performance acceptance

2026-11-24: original dev KFM LiDAR data subtotal525,897,902bytes; Ground store6,748,425bytes; current native-v3 view store289,715,080bytes. These totals contain processing and older requested material.

Four actual validated Ground regions,36,864F32 values: prepared relay42–90ms, warm memory0.66–2.25ms, restarted-host disk3.02–5.50ms;4saved host copies159,018bytes in total. Gzip response reductions69–85%. The bundled statewide overview served without dev in3.47ms. These measurements are the local website service through an SSH-forwarded signed QA gateway, not the GoDaddy WAN, first-time source preparation, or browser frame time. Public deployment and live response measurements remain separate. A fresh public read of the already-published predecessor returned Brotli-encoded API data; the local gzip reduction is therefore not a measured improvement over GoDaddy's existing compression. The primary hosting refinement is durable reuse without another dev trip, not a claimed public compression speedup.

The frontend revision removes duplicate coplanar internal cell walls and frames the acquired landscape with supported-gradient lighting, while preserving source heights and cell IDs. Report its final geometry counts and actual browser/owner proof independently.

## Publication and follow-through

Run complete regressions, focused GPU/browser CI and independent source/design review on the exact candidate, then integrate into owner-confirmed `a0-hosted-ai-web-20261017`. Publish through the existing GoDaddy app and verify `/api/build`, the same terrain APIs, compressed delivery and a warm/restart host read. Do not create another app or change DNS, secrets, billing, SQL, or the preserved Sites deployment. The current Chrome policy error and connector's lack of Node-hosting actions do not establish a successful publication.

Future refinements require measured need: cache hit-rate and first-detail timing; standard multiresolution geographic tiles to share nearby pans; optional prewarming within the existing1GiB budget; source-aware datum/registration checks before changes or differences. No promise of uniformly complete statewide Surface/Canopy, metre-scale detail at regional zoom, or independent surveyed accuracy follows from a rendering/cache improvement.

Source: GoDaddy documents `public/assets` persistence between deployments: https://www.godaddy.com/help/deploy-my-cursor-or-claude-app-with-nodejs-hosting-42908 . Official existing-app update workflow: https://developer.godaddy.com/en/docs/api-users/hosting/workflows/deploy-nodejs-app .


## Visitor working set

The visitor browser processes only the public terrain currently being explored. It does not prepare work for other visitors, download an archive, access a local companion service, or retain a background worker after the view is hidden or disposed. This is a bounded addition to the existing map; the full browser's RAM, GPU usage and frame rate cannot be reserved or guaranteed by a website.

Public ready/partial Ground receipts and complete native Surface/Canopy receipt-grid pairs can be reused by the same browser origin for at most five minutes. Exact canonical query, schema, source identity, original cache timestamps, source values and NoData support are revalidated on every hit. Originally stale data is not added; original 24-hour host freshness is never extended. A cache hit never renews its own expiry. Refresh explicitly bypasses the browser copy. Raw point chunks, private records, credentials and worker geometry are excluded from this disk cache.

The default is conservative when browser hints are absent, RAM is at most 4 GB, logical cores at most four, or Save-Data is enabled. Logical serialized cache limits are 8 MiB (conservative) or 16 MiB (capable), 24 entries, and 2 MiB per record. IndexedDB bookkeeping and browser-managed storage overhead are outside those payload numbers. Writes use a shared readwrite transaction to enforce an aggregate origin budget across tabs and remove oldest replaceable entries first. Quota estimates reduce writes when space is tight, with a 50 MiB reported-origin reserve. Storage denial, timeout or quota failure falls back to normal website delivery. No persistent-storage permission is requested.

Temporary copies are removed on later cache access after expiry, with an additional one-hour absolute retention guard. A closed browser cannot run deletion code: its own eviction policy controls physical removal while closed. “Clear temporary data” and disabling storage remove these copies immediately when browser storage is available, and invalidate in-flight writers across tabs. These actions do not delete Places, investigations, user files, map assets or owner-PC archives.

A dedicated module worker prepares the same gradient analysis and packed solid geometry, then transfers its bounded vertex buffer. GPU rendering/picking remains with the map. Mode, extent, scale and color are bound to each result so a late response cannot replace the current view. Opacity and selection reuse prepared geometry. One job runs at a time; hidden pages abort terrain fetches and preparation and resume their current selection on return. Slow preparation selects a lower display framebuffer budget; this changes display work, not source grid resolution or scientific values. Unsupported workers retain continuous terrain and source readings with an explicit status.

The Terrain panel's collapsed “This device” section exposes Automatic/Lightweight, temporary-data use and Clear. Browser/device hints are local and are not uploaded. No new hosting, compute subscription, paid API, or dev worker changes are required.

Platform references: [Web Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers), [browser storage and eviction](https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria), and [approximate device-memory hints](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/deviceMemory). Actual public publication, measured visitor-device performance and owner visual acceptance remain separate from source tests.
