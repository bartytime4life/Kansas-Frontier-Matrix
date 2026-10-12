# USCRN daily soil pilot fixtures

Synthetic, deterministic stand-ins for the NCEI USCRN daily01 files the soil
pilot capture fetches. They follow the published daily01 (CRND0103) layout,
28 whitespace-separated fields, but are not NOAA observations: values are
generated and station coordinates are approximate.

| File | Stands in for | What it exercises |
|---|---|---|
| `headers.txt` | `daily01/headers.txt` | the field numbers and names the capture requires to match its pinned profile |
| `crnd0103-2026-ks_manhattan_6_ssw.txt` | `daily01/2026/CRND0103-2026-KS_Manhattan_6_SSW.txt` | a missing 5 cm moisture (`-99.000`), a missing 100 cm temperature (`-9999.0`) and an impossible 20 cm moisture (`1.234`, withheld as OUT_OF_RANGE) |
| `crnd0103-2026-ks_oakley_19_ssw.txt` | `daily01/2026/CRND0103-2026-KS_Oakley_19_SSW.txt` | soil moisture stops reporting after 2026-10-05, so the station is STALE |

Each station file has 40 days (2026-09-01 to 2026-10-10), so the 30-day
window ending 2026-10-10 is selected from a longer year file.
