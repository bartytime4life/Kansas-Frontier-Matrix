# Heat & Rain Lab

Open `/labs/heat-and-rain` from the Observatory source guide. Choose Dodge City,
Wichita or Topeka, a year from 2020–2025, and optionally one month. Read daily
maximum/minimum temperature and precipitation, count threshold events, and
download qualified daily CSV and an analysis JSON receipt. The three bundled
NOAA station snapshots work without an account, provider key or live NOAA
request. Only the selected approximately 195 KB station file is loaded.

These are provider-context display derivatives of public US station records.
They do not activate the governed weather pipeline, admit a KFM dataset, or
establish deployment. The monorepo source and standalone GoDaddy composition
remain distinct. This addition uses new isolated files; it does not replace
the standalone Labs or Research Discovery source.

## Measurements and calculations

Original GHCN-Daily `.dly` values are integers in tenths of °C for TMAX/TMIN
and tenths of mm for PRCP. Every source tuple retains the integer and NOAA
measurement, quality and source flags. The exact 2,192-day calendar is retained
for each station, including 2020 and 2024 leap days. Absent element records
become explicit missing fields, never zeros.

- Heat: reported TMAX greater than or equal to the selected °C threshold.
- Freezing threshold: reported TMIN at or below 0°C. The daily minimum alone
  does not establish the hour of the minimum or whether frost formed.
- Wet day: quantified PRCP greater than or equal to the positive mm threshold.
- Quantified precipitation sum: add only reported, quality-passing daily
  amounts. Separate denominators show valid versus expected days for every
  element; traces are unquantified and counted separately. An incomplete sum
  does not estimate precipitation on excluded dates. Quantified PRCP is
  liquid-equivalent precipitation and can include melted snow.

Nonblank quality flags are withheld. Presumed-zero missing (`P`), unresolved
precipitation (`H`), no precipitation report (`I`), unknown/inapplicable flags
and missing source flags are excluded. GHCN `.dly` measurement flags `A`,
`C` and `E` represent precipitation periods of 6, 18 and 12 hours. The
raw values remain available, with these partial periods excluded from daily
threshold counts and sums. Trace (`T`) at raw zero is retained as
an unquantified occurrence. For temperatures, hourly-derived (`H`) and lagged
(`L`) readings retain their measurement flags. A reported minimum exceeding
the reported maximum excludes both temperatures for that date.

Station observation-day conventions can differ; `.dly` contains no observation
time field. The coordinates are current inventory metadata, not a historical
station-location reconstruction. Do not use these observations as field,
county or gridded estimates. Six years do not establish a climate normal,
attributed trend, drought diagnosis or forecast. Daily precipitation is not
linked to a particular river or watershed by this tool.

For a winter example, inspect Topeka on January 5, 2025. The lab’s GHCN Daily
snapshot records 20.6 mm of liquid-equivalent precipitation. The separate
[NWS event summary](https://www.weather.gov/top/2025Blizzard) documents the
snowfall and other precipitation types during the January 4–5 storm.

CSV retains raw integers, every flag, accepted values in the selected units,
station/date, thresholds, source URL, capture time and original-source SHA256.
The JSON receipt adds the exact display-snapshot hash, support and method.
The original-source link reads NOAA's current file; NOAA may subsequently
revise that file. Local capture SHA256 records byte identity and is not a
provider-issued checksum.

## Reproduce and update

From `apps/site/source`, use a **new private directory outside Git**:

```bash
python3 scripts/prepare-daily-climate.py --capture-dir /absolute/private/new-capture
python3 scripts/prepare-daily-climate.py --source-dir /absolute/private/new-capture
node --test tests/heat-and-rain.test.mjs
```

The capture downloads six fixed official NOAA objects: station inventory,
version, format documentation and three `.dly` files. It limits each response
to 24 MiB and the capture to 64 MiB, uses a 30-second transport timeout and
keeps originals outside source/public assets. Its receipt binds original URLs,
capture times, sizes, Last-Modified and SHA256. Failed captures stay incomplete
and are not prepared implicitly. The offline preparation verifies every source
hash, station/date identity, record length and uniqueness before producing
content-hashed JSON files and a small manifest. Repeating offline preparation
from the same captured bytes produces the same derivatives.

The browser bounds snapshot reads to 1 MiB and 12 seconds, checks non-2xx and
exact bytes/SHA256, validates the complete calendar and binds results to the
selected station. Obsolete reads are cancelled; retry never presents another
station's values. The page does not depend on a new backend or database.

Preparation leaves old content-hashed assets in place. Review changes and
remove only explicitly superseded display files after verifying references.
Review provider revisions and retain provenance before any release. Rollback
reverts the bounded lab, links and successor mirror receipt; no database or
provider credential migration is involved.

## Sources

[NOAA GHCN-Daily documentation](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt)
defines units, record layout and flags. The
[official product page](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily)
describes processing, continuing revisions and the dataset citation
([DOI 10.7289/V5D21VHZ](https://doi.org/10.7289/V5D21VHZ)). The checked manifest
records the captured update version and precise provider URLs.
