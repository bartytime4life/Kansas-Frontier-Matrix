# Captured IEM verification inputs

Public airport weather observations and catalog metadata retrieved on 2026-10-30.
`provenance.json` records each unmodified response's URL, retrieval timestamp,
status, byte size and SHA-256. These are bounded test fixtures, not released KFM
data, a canonical source registry, or a guarantee that IEM will return identical
historical bytes later. No source value was invented to populate these files.

- `ks-asos.geojson`: the 69-feature Kansas station catalog, including closed sites.
- `sln-2024.csv`: actual default-column daily CSV, April 1–October 31, Salina.
- `gld-2024.csv`: actual selected-column CSV with `na=M`, same season, Goodland.
- `closed-1k1-2024.csv`: three actual all-missing rows from a retired station.

The independent reference is `python3 tests/iem_reference_totals.py`.
The Node regression suite distinguishes fixture replays from live acquisition.
See `docs/iem-field-verification-2026-10-30.md` for source semantics and limits.
