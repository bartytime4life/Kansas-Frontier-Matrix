# GHCN-Daily pilot fixtures

Synthetic, deterministic stand-ins for the NCEI files the GHCN-Daily pilot
capture fetches. They follow the real layouts but are not NOAA observations:
values are generated and station coordinates are approximate.

| File | Stands in for | What it exercises |
|---|---|---|
| `ghcnd-stations-excerpt.txt` | `ghcnd-stations.txt` (fixed width) | the four pilot stations, an out-of-scope Kansas co-op station and a Missouri station |
| `usw00003928.csv` | `by_station/USW00003928.csv.gz` | a trace (M=T), a quality-flagged TMAX (Q=I) and a missing TMIN (-9999) |
| `usw00013985.csv` | `by_station/USW00013985.csv.gz` | a clean station |
| `usw00013996.csv` | `by_station/USW00013996.csv.gz` | M=P "presumed zero", which stays missing |
| `usw00023065.csv` | `by_station/USW00023065.csv.gz` | stops reporting five days before the window end, so it is STALE |

Each CSV has 31 days (2026-09-10 to 2026-10-10) and also carries SNOW and
TAVG, so the 30-day window and the PRCP/TMAX/TMIN selection are tested. Tests
gzip the CSVs with `mtime=0`, so the compressed bytes and digests are stable.
