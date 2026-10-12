# NOAA Storm Events pilot fixtures

Synthetic, deterministic stand-ins for the NCEI files the Storm Events pilot
capture fetches. They follow the published bulk CSV layout (the 51 details
columns) but are not NOAA records: event and episode IDs, counties, times and
coordinates are invented, and every narrative says so.

| File | Stands in for | What it exercises |
|---|---|---|
| `listing.html` | the `csvfiles/` directory listing | two 2025 details vintages (the newer, `c20251020`, is chosen), a 2024 file, and 2025 fatalities and locations files that are never fetched |
| `stormevents_details_d2025.csv` | `StormEvents_details-ftp_v1.0_d2025_c20251020.csv.gz` (the test fetcher gzips it) | the rows below |

| Event | Exercises |
|---|---|
| 9000101 | Tornado, EF1, `250.00K` damage, an injury, coordinates and narratives |
| 9000102 | Hail with blank damage (unreported, not zero) |
| 9000103 | Winter Storm on a forecast zone (`Z`), `MST-7`, no coordinates |
| 9000104 | Thunderstorm Wind with no episode ID |
| 9000105 | Flash Flood in `CDT` (no offset, so no UTC), `2.00M` / `10.00K` damage |
| 9000106 | `THUNDERSTORM WINDS/HAIL`, a label outside the directive list |
| 9000107 | unreadable damage `abc`: withheld as `DAMAGE_UNPARSEABLE` |
| 9000108 | end before begin: withheld as `END_BEFORE_BEGIN` |
| 9000109 | Nebraska: not selected |
