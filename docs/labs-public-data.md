# Labs with public data

The owner requested a functional, populated `/labs` on 2026-11-16. The page now
opens on two connected workspaces and nine instruments with bundled public source snapshots. The
question shortcuts, previews, controls, tables, record inspection and downloads
use these same bundles. Additional instruments and planned stories remain
accessible through **All research**.

## Guided investigations candidate, November 18, 2026

The Labs catalog and the Kansas Record on the map welcome link to these
dedicated investigations. Their publication is a separate release step.

| Investigation | Source scope |
| --- | --- |
| Water Chemistry, `/labs/water-chemistry` | 28 Water Quality Portal records at USGS 07144100 near Sedgwick. The 2019–2020 and 2021–2022 windows use the same dissolved nitrate analyte, units, analytical method, collection method and sampler. One non-detect retains its reporting limit and stays outside the numeric histogram. |
| Boom & Ghost Towns, `/labs/ghost-towns` | All 59 Douglas County rows matching the county fields in the original geocoded Blevins–Helbock file. The map includes 45 provider-matched locations, and the record view retains unlocated and undated records. County outlines are present-day context. |
| Newspaper Pulse, `/labs/newspaper-pulse` | All 20 Library of Congress digitized pages from two Abilene Weekly Reflector issues dated January 2, 1890 and January 4, 1900. Rates count pages containing each OCR token and use the matching issue's page inventory as the denominator. |
| 2012 Drought Replay, `/labs/drought-replay` | 17 Finney County U.S. Drought Monitor assessments and 119 approved daily means from USGS 07139000. Each map date keeps its validity interval and the selected week shows its seven dated gauge records. |

Each investigation exposes source records and a free export. Snapshot builders
capture the provider file or request and digest. A source-file receipt documents
the material used by the page. For historical dates, use the definitions and
coverage limits shown on the corresponding investigation.

## Finney County drought replay

The [county area statistics](https://usdmdataservices.unl.edu/api/CountyStatistics/GetDroughtSeverityStatisticsByAreaPercent?aoi=20055&startdate=6%2F5%2F2012&enddate=9%2F25%2F2012&statisticsType=1)
cover the Tuesday map dates June 5 through September 25, 2012. Format 1
percentages are cumulative by severity. The bars plot D3-only as D3 minus D4,
and D4 as reported. The source's validity end is inclusive. USDM releases its
weekly assessment on Thursday and uses Tuesday as the valid date.
[USDM methods](https://droughtmonitor.unl.edu/About/WhatistheUSDM.aspx)

The [USGS daily series](https://api.waterdata.usgs.gov/ogcapi/v0/collections/daily/items?monitoring_location_id=USGS-07139000&parameter_code=00060&statistic_id=00003&time=2012-06-05%2F2012-10-01&limit=150&f=json)
covers June 5 through October 1, 2012 and uses daily mean discharge `00060/00003`
in cubic feet per second. The 119 unique rows are approved, have no qualifiers,
and all report zero. The legacy USGS daily values response agreed for every
date. The two series align by calendar date for retrospective reading. The
gauge describes its own location, and the daily series supplies observation
dates only.

The report queries, capture timestamp, source record IDs, and raw SHA-256 values
travel with the download. To reproduce a capture, save the two provider
responses and run `python3 scripts/prepare-drought-replay.py COUNTY.csv DAILY.json CAPTURE_ISO app/labs/drought-replay/snapshot.json`.
USGS source records may be revised. The builder rejects unexpected grain, partial
coverage, mismatched station metadata and nonmonotone severity shares.

## Bundled instruments

| Lab | Shipped coverage | Records |
| --- | --- | ---: |
| Climate Stripes | January 1895–October 2026, Kansas and nine climate divisions | 132 years, 10 areas, 3 monthly measures |
| County Pulse | Vintage 2025, July 1 estimates for 2020–2025 | 630 county-year rows; 105 per selected year |
| River Memory | Three USGS gauges, January 2020–November 2026 | 7,526 daily observations |
| Tornado Tracks | SPC whole tornadoes starting in Kansas, 1950–2025 | 4,582 |
| Shaking Ground | USGS M≥1 events, Kansas and immediate border region, 2010–2026 | 6,762 |
| Built Kansas | Complete returned KDOT state and local bridge inventories, retrieved November 16, 2026; recorded built years 1870–2026 | 24,877 inventory records; 27 undated |
| Energy Shift | 26 selected EIA Kansas annual series, 1960–2024 | 1,690 annual observations |
| Air Quality | EPA monitored Kansas county annual AQI, 2000–2025 | 333 county-years; 17 counties historically, 12 in 2025 |
| County Conditions | ACS five-year periods 2010–2014, 2015–2019 and 2020–2024; nine measures with 90% margins of error | 315 county-period rows; all 105 counties per period |

These are dated source snapshots, not live observations. Source revision,
coverage, missingness, qualifiers and interpretation limits remain visible.
Population estimates are selected one year at a time. Tornado rows sharing an
SPC identifier retain separate date/time/state-sequence identities. An earthquake
query reaching its 10,000-row cap fails acquisition rather than claiming completeness.

### Source and rights basis for the nine bundled instruments

The importers for these nine instruments read only named public NOAA, Census, USGS, EIA, EPA and KDOT endpoints. Each bundle
records the exact URLs, retrieval times, raw byte counts and SHA-256 hashes.
The generated manifest binds each shipping filename, size and SHA-256. The
browser verifies the file before accepting its data. Build validation rejects
unexpected files in the four manifest data directories, invalid contracts and modified bytes.
The bridge instrument has an explicit 16 MB / 40,000-record bound; other instruments
retain the 3 MB / 10,000-record bound. No generic request can enlarge these limits.

- [NOAA nClimDiv downloads and format documentation](https://www.ncei.noaa.gov/pub/data/cirs/climdiv/)
- [Census public open-data policy](https://www.census.gov/topics/research/research-transparency-public-access/open-data.html)
- [USGS public-domain data and credit policy](https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits)
- [SPC source descriptions and actual-track downloads](https://www.spc.noaa.gov/wcm/)
- [USGS daily values service](https://waterservices.usgs.gov/docs/dv-service/)
- [USGS ComCat API documentation](https://earthquake.usgs.gov/fdsnws/event/1/)
- [KDOT state bridge inventory](https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Structures/State_Bridges/MapServer/0)
- [KDOT local bridge inventory](https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Structures/Non_State_Bridges/MapServer/0)
- [EIA SEDS](https://www.eia.gov/state/seds/) and [reuse policy](https://www.eia.gov/about/copyrights_reuse.php)
- [EPA AirData formats](https://aqs.epa.gov/aqsweb/airdata/FileFormats.html#_annual_aqi_by_county) and [data license](https://edg.epa.gov/EPA_Data_License.html)

Bridge acquisition enumerates every source OBJECTID before and after paged retrieval
and reconciles identifier multiplicities on every page. The state service returns
5,586 rows for 5,582 distinct OBJECTIDs, and different identifiers can also refer to
the same physical structure. All returned rows remain; counts mean inventory records.
Their identities bind the source network, OBJECTID and returned feature bytes.
Construction-year filtering describes present inventory with recorded years, not
historical construction rates or all structures that ever existed. KDOT attributes
are credited public service data, not a federal public-domain or safety certification.

Energy uses one source unit, billion Btu, and starts with Total consumption selected.
Fuel totals, sector totals and production overlap and must not be summed. Annual
series retain numeric years without invented observation dates. EPA selects one
county-year cohort at a time. Unmonitored counties remain absent. Coverage and
above-100 percentages use their declared calendar-day and monitored-day denominators;
AQI does not supply a health outcome or personal exposure measure.

## Connected investigations

`/labs/observatory` joins Census population and ACS conditions, KDOT inventory and
EPA annual AQI by exact county FIPS. KDOT county labels must match a normalized
Census county label; unmatched labels remain in diagnostics. The current snapshot
matches all 24,877 inventory records. Every metric retains its own source period;
these are not simultaneous measurements. The map, A/B profiles, county rankings,
cross-source scatter and exports share the selected measures. Missing county AQI
is unavailable, never zero. Inventory counts describe returned rows, not unique
physical bridges; score means are unweighted and age uses the inventory year.

ACS acquisition uses official summary-file downloads, with exact estimate and
90% margin-of-error inputs. The 2024 national table files use bounded byte-range
responses containing all 105 Kansas county rows; receipts identify the response
slice and Content-Range, and its hash does not claim to bind the whole national
file. All vintages require all 105 expected FIPS codes before replacement. Dollar
amounts use the vintage's dollars and are not inflation-adjusted across periods.
See the [Census ACS accuracy documentation](https://www2.census.gov/programs-surveys/acs/tech_docs/accuracy/MultiyearACSAccuracyofData2024.pdf).

`/labs/signals` offers 66 annual series across NOAA climate, EIA energy, three USGS
gauges, tornado records and earthquakes. Positive lag joins X(t) to Y(t + lag),
with both years inside the selected period. River annual means require a completed
calendar year and at least 90% of its 365/366 daily observations. Event counts
include zero years only within declared completed source coverage. Unknown
measurements remain missing. Annual climate requires all 12 monthly values.

Raw, separate linear detrending and consecutive-year differencing use complete
paired years. Differences never bridge a gap. Overlay z-scores use the transformed
paired mean and sample standard deviation; statistics use the transformed values.
The lag profile recalculates all 11 lags with the same rules. Neighboring years
can be autocorrelated, source series can overlap and shared trends can inflate
associations. Lag exploration supplies no significance or causal conclusion.

Both workspaces support bounded share/replay links, CSV and analysis-receipt
downloads, printing and a browser-local notebook of up to 12 investigations.
County CSV uploads accept exact Kansas FIPS plus up to 12 numeric measures and
512 KB. Uploads stay in the browser and never enter share links. Saving a county
investigation explicitly includes its private attachment in local storage;
downloading the notebook includes those attachments. Clearing browser storage
removes local copies. Source fingerprints distinguish saved from current data.

## Scientific tools and replay

Relationships use all complete pairs in the current selection, with Pearson r,
Spearman rho calculated as Pearson correlation of average tied ranks, and an optional
ordinary least-squares line with intercept and R². Fewer than three pairs or a constant
axis suppress the coefficients. Scatter marks use a disclosed deterministic sample
of at most 1,800 pairs; analytical counts and statistics use all pairs. Correlation is
descriptive and supplies no causal effect, p-value or independence assumption.

Quartiles interpolate at `(n - 1) p` (R type 7); sample standard deviation divides
the centered sum of squares by `n - 1`. Missingness, ranked observations and grouped
summaries follow the same filters and time selection as the table and CSV. See the
[R quantile specification](https://search.r-project.org/R/refmans/stats/help/quantile.html)
and [NIST rank-correlation formula](https://www.itl.nist.gov/div898/software/dataplot/refman2/ch2/rankcorr.pdf).
Climate trends fit only complete 12-month annual observations in the selected period,
using the source scale and sum/mean rules. Incomplete years are counted and excluded
from the fit and extremes. The trend is per decade, with descriptive R².

Share links encode only bounded, allowlisted control state, time, instrument ID and
the exact shipping SHA-256. A link for another revision or instrument is rejected.
It never supplies an arbitrary data URL or instructions to execute. Old links may
become stale after a source refresh; downloadable receipts retain their source binding.
Public record CSVs carry the shipping snapshot digest and its acquisition completion
time; individual raw-page hashes remain in the source snapshot and view receipt.

Climate baselines are monthly means calculated from the same downloaded series
for 1901–2000 and 1991–2020. They are explicitly distinguished from NOAA's
separately published normals. NOAA state code 014 is Kansas; the display's
state identifier is FIPS 20. Missing precipitation (-9.99), temperature (-99.90)
and PDSI (-99.99) are null, including unreported months in the final year.

The existing `stories` relay stays pending. No private local database or preview
was copied, and railroad, Newberry and fossil source gates were not lifted.
An instrument without a shipping bundle keeps its existing relay/preview path.
Public instruments always use their pinned shipping snapshot and never fall
through to the PC when loading fails. These source-context visualizations do
not grant governed KFM evidence admission.

## Refresh

Run from this standalone application's root:

```sh
python3 scripts/prepare-labs-data.py --through YYYY-MM-DD
python3 scripts/prepare-labs-science-data.py
python3 scripts/prepare-labs-bridges.py --through YYYY-MM-DD
python3 scripts/prepare-labs-county-data.py
node scripts/validate-labs-data.mjs
npm run build
node --test --test-concurrency=4 tests/*.test.mjs app/labs/atlas-model.test.mjs
```

Raw downloads stay under ignored work directories or `/tmp/kfm-labs-science-raw`; `--cache` can select another
local directory. `--offline` rebuilds from hash-verified raw responses. Raw
files, credentials and local databases are excluded from deployment. Acquisitions
finish before replacing the shipping snapshots and manifest. Review the changed
coverage and source counts, then deploy the application normally. The site has
no implicit automatic refresh or reliance on a running home PC for these labs.

## Delivery

Destination: existing GoDaddy app `urdng3v1vk`, hosted source branch
`a0-hosted-ai-web-20261017`, public route `/labs`. GoDaddy preview/build,
publication and public rendered verification are separate from local checks.
No DNS, provider secrets, private Site bindings or PC service changes are needed.
