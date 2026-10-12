# USGS earthquake pilot fixtures

Synthetic, deterministic stand-ins for the ComCat FDSN event query pages the
earthquake pilot capture fetches, one file per calendar month of 2025. They
follow the published GeoJSON layout but are not USGS solutions: event ids,
times, epicenters and magnitudes are invented, and every `place` says so. A
month with no file answers HTTP 204 with no body, as the service does with
`nodata=204`.

| File | Events | What it exercises |
|---|---|---|
| `2025-01.geojson` | `us7000p001`, `ok2025b002` | a reviewed event with an alias; `ok2025b002` at exactly 2025-02-01T00:00:00.000Z, which the inclusive January query also returns |
| `2025-02.geojson` | `ok2025b002`, `us7000p003` | February owns the boundary event; `us7000p003` is `deleted` and withheld as `STATUS_DELETED` |
| `2025-05.geojson` | `us7000p004`, `ok2025p005`, `us7000p006` | an automatic solution with no depth; an epicenter in the Oklahoma margin of the envelope (`CONTEXT_MARGIN`); an event with no magnitude and no place |
