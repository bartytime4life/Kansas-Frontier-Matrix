# Sunlight & Sky Lab

`/labs/sunlight-and-sky` compares captured daily NASA POWER all-sky and clear-sky incoming shortwave energy on a horizontal surface. It adds a daily energy question to the existing astronomical daylight tools and monthly PRISM solar archive. `/science` provides the direct five-tool entry point.

## What the source supports

The three fixed query points are Dodge City area (37.7608, −99.9689), Wichita area (37.6544, −97.4431) and Topeka area (39.0725, −95.6261). These familiar place labels identify query coordinates, not ground stations, area averages or surveyed cell centers. All 2,192 calendar dates from 2020-01-01 through 2025-12-31 are retained for every point: 6,576 point-days and 13,152 parameter values.

The captured responses identify `POWER Daily API v2.10.5`, source `SYN1DEG`, and `kW-hr/m^2/day` for both `ALLSKY_SFC_SW_DWN` and `CLRSKY_SFC_SW_DWN`. Display notation is kWh/m²/day; a sum over daily values is kWh/m². This is energy per surface area, not a daylight duration or instantaneous power measurement.

[NASA's solar methodology](https://power.larc.nasa.gov/docs/methodology/data/sources_fluxes/) describes the primary CERES SYN1deg radiation grid as nominally 1° latitude by 1° longitude. Its current source table names Edition 4.2; these API responses report `SYN1DEG` without an edition identifier, so the capture does not independently pin that underlying edition. Solar fluxes are inferred through radiative-transfer models using satellite observations and atmospheric inputs. Returned point coordinates and elevation are preserved as provider metadata, without claiming an exact grid boundary or local site elevation.

Time is explicitly requested as NASA **Local Solar Time** (`time-standard=LST`), representing 15° longitude swaths with solar noon at each swath's center. This is different from local standard time in USCRN and from civil CST/CDT. See the [Daily API](https://power.larc.nasa.gov/docs/services/api/temporal/daily/) and [time FAQ](https://power.larc.nasa.gov/docs/faqs/other/).

## Arithmetic and interpretation

Each area’s all-sky mean and sum use its own valid modeled days. The comparison metric is **primary minus comparison**, computed only on dates with valid all-sky values for both areas. The primary all-sky versus clear-sky difference uses only dates with both primary values. Every metric includes its own denominator. Monthly summaries use the same rules; the month selector narrows the daily window, while the overview still describes the selected full year.

The provider missing sentinel `−999` remains in raw snapshot/export fields and becomes an unavailable reading for analysis. A real zero remains valid. Missing values are never filled or assigned zero, and missing dates break plot lines. All-sky estimates above a clear-sky reference are preserved without clipping. Clear-sky differences are model comparisons, not measured cloud effects or cloud percentages. The present capture has no missing, zero, or above-clear-sky values; those cases are explicitly synthetic regression fixtures.

For the default 2025 Dodge City–Topeka comparison, all 365 dates are paired. All-sky sums are 1,751.4821 and 1,570.5941 kWh/m²; means are about 4.7986 and 4.3030 kWh/m²/day. Their paired mean difference is about +0.4956 kWh/m²/day. These are historical model estimates for the selected query points, not a Kansas-wide gradient or a climate normal.

This tool does not estimate panel output, electricity, site design, crop response, photosynthetically active radiation or future conditions. Six years do not establish a trend or attribution. Sources can be revised. NASA publishes comparisons with surface radiation networks in its methodology; those global product statistics are not local uncertainty bounds for these query points. No local validation or numerical site error bar is claimed.

## Reproduction and containment

Use Python 3.11+ and an absolute, new capture directory outside every Git checkout:

```sh
python3 scripts/prepare-sunlight.py --capture-dir /var/tmp/kfm-sunlight-new-capture
python3 scripts/prepare-sunlight.py --source-dir /var/tmp/kfm-sunlight-new-capture
```

The fixed plan contains three API JSON responses and five provider documentation pages. Requests are sequential, allow no redirects, use a 20-second socket timeout and a 60-second per-object read budget. Limits are 1 MiB per object and 4 MiB aggregate. Original files and their receipt stay private outside Git; only three compact content-hashed display snapshots and the manifest enter the repository.

Offline preparation checks captured bytes and SHA-256, point identity, parameter names/units, API/product/clock identity, every calendar key, finite numeric bounds, and duplicate JSON keys. A schema or unit change fails preparation rather than silently changing arithmetic. It writes derived artifacts only after all three responses validate. Source request URLs are fixed; no browser key or live NASA query is required by the website.

The browser uses the shared bounded same-origin hash reader. Both point loads belong to the current pair selection; obsolete work is canceled and cannot supply later analysis. Snapshots and model analyses are frozen; exports accept only a current source-bound model result. CSV carries date keys, raw and interpreted values, states, query coordinates, source URL/hash/capture time, API/product and display-asset hashes. The analysis JSON records denominators, method, paired metrics, monthly summaries and limitations. Any inspected date or share link is labeled UI context; exports cover the selected full date window.

The three displayed assets total about 369 kB before transport compression. Original captures, dependencies and build output are excluded from scientific display assets.

## Credit, review and delivery

Credit NASA Langley Research Center's POWER project, funded by NASA Earth Science Division, with service name, API version and access date. Each source records these details. See [POWER referencing guidance](https://power.larc.nasa.gov/docs/referencing/) and [NASA science-data access](https://science.nasa.gov/learn/entry-points-to-nasa-data/). Downloads remain free. No NASA endorsement is implied.

Source/scientific review and KFM admission remain **PENDING**, dataset release **UNRELEASED**. Source hash checks, local rendering, repository CI and merges do not establish scientific acceptance or public hosting. The canonical mirror and standalone Node website retain their own navigation and preservation rules. No persisted data, original private Site audience/bindings, Earth Engine authority, workflow policy, dependencies or source-admission state changes.

## Validation and rollback

Validate parser regressions, model/schema/hash-reader tests, actual rendered controls and source exports, production build and TypeScript. Independent verification compares every display value and all 702 point-pair/year/month summaries to the original NASA JSON with separate Python arithmetic. Inspect actual desktop and phone production behavior; record deployment identity separately.

Rollback is a bounded source revert, preserving all earlier science tools, original capture files and immutable mirror receipt history. No storage migration is involved.
