<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/reports/nexrad-kfm-opportunities-20261007
title: NEXRAD radar in KFM — delivered slice and next opportunities
type: report
version: v1.0
status: proposal; first slice implemented
owners: ["@bartytime4life"]
created: 2026-10-07
updated: 2026-10-07
policy_label: public-documentation
owning_root: docs/
responsibility: Record what was taken from NCEI's NEXRAD product page, what shipped, and ranked follow-up ideas with storage costs.
truth_posture: Delivered items are cited to repository paths; every other item is PROPOSED and unbuilt.
related:
  - docs/runbooks/noaa-nexrad-local-capture.md
  - docs/sources/catalog/noaa.md
[/KFM_META_BLOCK_V2] -->

# NEXRAD radar in KFM

Source: NCEI [Next Generation Weather Radar (NEXRAD)](https://www.ncei.noaa.gov/products/radar/next-generation-weather-radar).
The page describes 160 WSR-88D Doppler radars, Level II base data
(reflectivity, velocity, spectrum width and dual-polarization variables) and
Level III derived products, and points to the NOAA Open Data Dissemination
cloud copies for bulk access.

## Delivered in this change

| Piece | Where | What a user gets |
|---|---|---|
| Level III decoder (Python) | `connectors/noaa/src/noaa/nexrad_level3.py` | Storm cells, tracks, forecast paths, motion, rotation and TVS flags from `NST`/`NMD` files |
| Bounded local capture | `tools/local_data/noaa_nexrad.py` | One storm day for the four Kansas radars in ~8 MB, cap checked before download |
| Site decoder + route | `apps/site/source/app/nexrad-storms.ts`, `app/api/event-atlas/storms/route.ts` | In-memory only; ~66 KB JSON per replay frame |
| Event Observatory layer | `apps/site/source/app/observatory/` | **Storm cells & rotation**, on by default, with a plain-language map key, click-for-details cards and a timeline lane |

UI choices made to keep it simple:

- One dot per storm, even when two radars see it, colored by the strongest
  rotation found. Five colors, labeled in words rather than radar jargon.
- A solid tail for "where it has been" and a dashed line for "expected path,
  next hour", directly from the radar's own tracking product.
- A one-line headline ("64 storm cells · 14 rotating strongly · 2 tornado
  signatures*") so the state of the map can be read at a glance.
- Each storm card answers: which radar, how long before the clock, which
  direction and how fast (mph and compass), how strong the rotation is.
- Every tornado-signature mention says it is a radar algorithm flag, not a
  confirmed tornado.
- Storm scan times join the replay clock on five-minute slots, so playback
  steps smoothly even when no reflectivity mosaic is available.

## Next opportunities (proposed, ranked by value per byte)

1. **Storm reports next to radar detections.** Overlay NCEI Storm Events
   (`connectors/noaa-storm-events`) on the same clock, so a tornado-signature
   storm can be compared with what was reported on the ground. Tiny data;
   biggest gain in trust and understanding.
2. **"Which radar sees my place?" coverage view.** Draw the beam height above
   ground for each Kansas radar (computed from site height and range, no
   download). Explains why western and far-northern Kansas see low-level
   rotation less reliably.
3. **County storm-history summary.** From captured `NST`/`NMD` days, count
   storm and rotation detections per county per season. Kilobytes per year.
   Show it in Focus Mode as context, labeled as detections not events.
4. **Rainfall totals vs. rivers.** Level III `DAA` (one-hour) and `DTA`
   (storm-total) precipitation are 2–80 KB per scan. Pair storm-total rain with
   the existing USGS river-pulse layer to show rain-to-flood timing.
5. **Echo tops and VIL.** `EET` (echo tops, ~1.6 KB) and `DVL` (digital VIL,
   ~4 KB) give "how tall/strong was the storm" in plain words; they could size
   the storm dots.
6. **Bird and insect migration.** Night-time Level II reflectivity shows
   migrating birds over Kansas in spring and fall. Pairs naturally with the
   fauna and eBird lanes. Needs Level II; budget a few volumes per night,
   processed to a single small density value per radar.
7. **Smoke and dust plumes.** Prescribed-burn smoke in the Flint Hills is
   visible to the Topeka and Wichita radars; compare with the HMS smoke layer.
8. **Radar reflectivity from NOAA directly.** The Observatory's reflectivity
   currently comes from IEM mosaics. Level III `N0B` per-radar reflectivity is
   100–270 KB per scan; a renderer could replace it for 2020+ without storing
   anything, at a higher network cost per frame.
9. **Archive before 2020.** The Unidata bucket starts around 2020. Older
   storm-track products exist in NCEI's archive (and as NCEI SWDI summaries),
   reachable only from networks that allow `www.ncei.noaa.gov`. A bounded
   capture similar to this one could extend storm tracks back to the 1990s.

## Not recommended

- Bulk Level II downloads (about 3 GB per radar per day).
- Saving radar images server-side for the Site; the archive is already
  durable and public, so KFM should keep only small, derived, cited outputs.
