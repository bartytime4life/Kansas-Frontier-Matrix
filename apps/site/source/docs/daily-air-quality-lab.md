# Daily Air Quality Lab

`/labs/daily-air-quality` makes daily timing and source records inspectable,
alongside the existing annual Air Quality story and County Observatory. It uses
EPA's supplied county daily AQI, category, defining pollutant, defining site and
reporting-site count. It does not recompute AQI from concentrations.

## Captured observations

Six official AirData `daily_aqi_by_county_YEAR.zip` files cover 2020–2025.
The Kansas cut has 22,458 reported county-days in 12 counties appearing at least
once: Chase, Douglas, Ford, Johnson, Leavenworth, Neosho, Sedgwick, Shawnee,
Sherman, Sumner, Trego and Wyandotte. Eleven counties report in each year
2020–2024, and twelve in 2025. Kansas has 105 counties; the remainder are not
represented as clean air or filled from a neighboring county.

The derivative retains 2,192 calendar dates for each reporting county. A null
cell means there was no county-day row in this captured source. The reason is
not inferred. Seasonal, changing or incomplete monitoring can affect coverage.
An actual AQI zero is a reported value. Reporting-site counts belong to the
individual source date, not to a fixed monitor inventory or population coverage.

The default Sedgwick County 2023 selection reports 365/365 dates and five dates
with AQI ≥101. Its maximum is 157 on September 6, defined by PM2.5 at site
`20-173-0010`, original national CSV row 103181 (header is row 1). This identifies
the source's defining pollutant, not an established cause or smoke attribution.

Source references:

- [Official pre-generated files](https://aqs.epa.gov/aqsweb/airdata/download_files.html)
- [AirData report definitions](https://www.epa.gov/outdoor-air-quality-data/about-airdata-reports)
- [AQI categories](https://www.epa.gov/outdoor-air-quality-data/airdata-basic-information)
- [County defining AQI](https://aqs.epa.gov/aqsweb/documents/aqi/aqi_data.html)
- [Download format documentation](https://aqs.epa.gov/aqsweb/airdata/FileFormats.html)
- [EPA public-domain data license and limitations](https://edg.epa.gov/EPA_Data_License.html)

EPA selects the highest reported qualifying monitor AQI within a county for
that date. It is not a county average, personal exposure, indoor measurement or
measured health outcome. The file does not identify an event cause, all measured
pollutants, concentrations, a regulatory violation or a live alert. For current
air-quality information use [AirNow](https://www.airnow.gov/).

EPA categories are retained exactly: Good 0–50, Moderate 51–100, Unhealthy for
Sensitive Groups 101–150, Unhealthy 151–200, Very Unhealthy 201–300 and Hazardous
301+. Category validation is a consistency check; the index is not recalculated.
Historical AQS files can be revised, including breakpoint treatment. This
capture preserves the published values and records provider file creation dates,
HTTP last-modified fields and capture identities separately.

## Analysis and export

County, calendar year, month/all-year and inclusive integer AQI threshold define
one selection. Threshold-day percentage is `100 × thresholdDays / reportedDays`,
not a fraction of all calendar days; it is null when there are no reports.
Coverage is reported/calendar dates. Median is computed only from reported
daily county values, using the midpoint of the central pair for even counts.
Peak and longest-run ties select the earliest date/run.

A run comprises consecutive calendar dates meeting the threshold. Missing dates
break it. A run touching a selected-window boundary or a missing neighboring
date has that boundary marked censored; the tool does not infer when the
underlying event began or ended. Defining-pollutant counts count only the days
that pollutant set the county AQI. Monitor/pollutant support can differ across
dates and counties; six years do not establish a climate normal or causal trend.

CSV includes missing calendar rows, original AQI/site-count text, exact source
category, defining pollutant/site text, original CSV row, selection and ZIP
provenance. The JSON analysis receipt includes the selected inspection date,
summary/coverage/methods and exact content-hashed display identity. Neither is
a provider signature, review approval or dataset admission receipt.

## Reproduce without a live dependency

The preparation script uses the Python standard library and a fixed plan of
eight objects: six annual ZIPs, EPA's file index and format documentation.
Original national objects and their receipt stay in a new private directory
outside Git; no provider key, custom URL or redirect is accepted.

```sh
python3 scripts/prepare-daily-air-quality.py --capture-dir /absolute/private/new-capture
python3 scripts/prepare-daily-air-quality.py --source-dir /absolute/private/new-capture
```

The offline command verifies URL, size and SHA-256, exact source plan, file-index
row counts and creation dates. ZIP/member/CSV/field sizes are bounded. Only the
one expected CSV member is read, without filesystem extraction. Kansas state,
FIPS/date/year, raw integer fields, category consistency and unique county/date
identities are validated. Source byte/hash failure, duplicate rows, changed
schema or an incomplete national CSV fail preparation before either derivative
is written. UTF-8 and Latin-1 handling is explicit in source metadata.

Only the bounded Kansas derivative and manifest enter application source.
The same-origin browser reader bounds decoded size, verifies exact length and
SHA-256, then validates the complete calendar/schema/coverage before analysis.
Gzip/Brotli delivery retains decoded-byte integrity checks. Loading or failed
reads do not leave old results exportable. All exports remain free.

## Delivery boundary

This is captured public provider context. Scientific review and source admission
remain `PENDING`; dataset release remains `UNRELEASED`. The lab does not change
the existing EPA ingestion pipeline, SQL stores, map-source counts, public story
snapshot allowlist, private Site bindings or Earth Engine state. Source tests,
GitHub CI, public UI publication and scientific acceptance remain separate.
