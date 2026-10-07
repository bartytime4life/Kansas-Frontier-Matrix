<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/noaa-nexrad-local-capture
title: Bounded Kansas NEXRAD Level III storm-product capture
type: runbook
version: v1.0
status: implemented; private capture; review pending
owners: ["@bartytime4life"]
created: 2026-10-07
updated: 2026-10-07
policy_label: public-documentation
owning_root: docs/
responsibility: Explain product selection, storage limits, bounded acquisition, verification and the Event Observatory storm layer.
truth_posture: Implementation and capture evidence are separate from source admission and map release.
related:
  - docs/runbooks/noaa-ghcnd-local-capture.md
  - docs/sources/catalog/noaa.md
  - tools/local_data/noaa_nexrad.py
  - connectors/noaa/src/noaa/nexrad_level3.py
  - apps/site/source/app/nexrad-storms.ts
[/KFM_META_BLOCK_V2] -->

# Kansas NEXRAD storm tracks on the local PC

NCEI's [NEXRAD product page](https://www.ncei.noaa.gov/products/radar/next-generation-weather-radar)
describes the WSR-88D network, its Level II base data and Level III derived
products, and points public users to the NOAA Open Data Dissemination (NODD)
cloud copies of the archive. KFM reads the NODD Level III copy at
`https://unidata-nexrad-level3.s3.amazonaws.com/` (public, no account).

## What is captured, and why it is small

Only two text-bearing Level III products are read:

| Product | Code | What it says | Typical size |
|---|---|---|---|
| `NST` Storm Tracking Information | 58 | Each storm cell's ID, position, past positions, 15–60 min forecast positions, motion | 0.5–15 KB |
| `NMD` Mesocyclone Detection | 141 | Rotation detections: strength rank (1–25), low-level flag, base/depth, tornado-vortex-signature (TVS) flag | 0.1–7 KB |

The four Kansas radars are Wichita (`ICT`), Dodge City (`DDC`), Goodland
(`GLD`) and Topeka (`TWX`). Neighbors `EAX`, `UEX`, `VNX` and `INX` may be
selected with `--radars`. A complete busy storm day (2024-05-19, four radars,
24 hours) is **2,182 files / 7.98 MB** (13.5 MB on disk with block rounding).

Not captured: Level II volumes (each about 5–15 MB, roughly 3 GB per radar-day)
and Level III reflectivity images (100–270 KB each). Those would fill storage
quickly and are not needed for storm tracks. Archive depth for these products
in this bucket starts in 2020; earlier days return empty listings.

## Storage rules

- Hard cap: **64 MiB across all retained `noaa-nexrad-l3` runs** (`--cap-mib`,
  at most 1024), counting RAW, WORK and receipts with disk-block rounding.
- Minimum free-space reserve: **20 GiB**, plus 8 MiB report headroom.
- `prepare` lists the bucket and checks the cap **before any product bytes are
  downloaded**. It refuses more than 6,000 products per run.
- Receipts are written in batches of 50, not one file per product.
- `verify` keeps only its newest derived index per run; the index is
  reproducible from RAW.
- Four in-flight requests; no retries, cron, unattended refresh or eviction.

## Run and verify

```bash
python3 tools/local_data/noaa_nexrad.py prepare --root "$KFM_LOCAL_STORE" --run 20261007T180000Z --day 2024-05-19
python3 tools/local_data/noaa_nexrad.py capture --root "$KFM_LOCAL_STORE" --run 20261007T180000Z
python3 tools/local_data/noaa_nexrad.py verify  --root "$KFM_LOCAL_STORE" --run 20261007T180000Z
```

Narrow a run with `--start-hour 21 --hours 6` or `--radars ICT,DDC`. The store
must be the existing private, initialized local store (see
[the local-PC data store runbook](local-pc-data-store.md)).

Each product is checked before it is saved: the WMO/AWIPS envelope must name
the same product and radar as the key; the message length, product code,
radar latitude/longitude/height and volume time must agree with the key. On
busy volumes the NST text table can list fewer cells than the graphic block
(for example 34 of 38); both are merged and the declared cell count must match.
A failed product is reported, not saved, and a repeat `capture` fetches only
what is missing. `verify` re-hashes and re-parses every original and writes a
compact GeoJSON index (`storm-detections-<hash>.geojson`, coordinates rounded
to 0.001°).

Verified on 2026-10-07 for 2024-05-19 (four Kansas radars): 2,182 products,
12,861 storm-cell detections and 1,604 rotation detections, 28 carrying the
TVS flag (Wichita radar, 23:16–23:58 UTC, McPherson County area). Retained
disk: 25.6 MB of the 64 MiB cap.

## Meaning and limits

These are radar **algorithm detections**, not observations of tornadoes, hail
or damage, and not warnings. A storm may be missed far from a radar, under
beam blockage, or when it is small. The TVS flag is a velocity-pattern flag; it
must be shown with that wording. Every capture records `source_admitted`,
`reviewed`, `released` and `published` as false. Admission, corroboration with
NCEI Storm Events, and release are separate governed steps.

## Event Observatory layer

The Site's Event Observatory (`/observatory`) shows the same products as the
**Storm cells & rotation** layer, on by default, through
`/api/event-atlas/storms`. That route stores nothing; it keeps a small
in-memory cache of listings and parsed products. For each clock time it shows
each radar's latest scan at or before that time (at most 12 minutes earlier)
and never carries an older scan forward. A storm seen by two radars is drawn
once, from the closer radar. The **Storm tracks & rotation · May 19 2024**
preset opens a good example.
