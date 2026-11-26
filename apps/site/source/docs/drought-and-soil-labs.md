# County Drought and Soil Profile Labs

The science entry at `/science` connects three populated, browser-based analyses:
Heat & Rain, County Drought and Soil Profile. The map's topic links, agriculture,
weather, water and science subjects, Observatory source guide and sitemap lead
to them. No login, paid API or live provider request is needed to analyse the
bundled history. The existing standalone Labs hub and 2012 Drought Replay are
separate compositions and were not replaced.

## Source scope

**County Drought** (`/labs/county-drought`) uses official U.S. Drought Monitor
county-area statistics, `statisticsType=1`, for all 105 Kansas counties. The six
annual CSV captures contain 32,865 county/Tuesday records: 313 assessment weeks
in 2020–2025. The API supports `aoi=KS` for all Kansas counties. Requests begin on
each year's first Tuesday because the service selects overlapping validity
intervals; January 1 can otherwise return the previous year's final assessment.

Sources and reuse:

- [Official REST service](https://droughtmonitor.unl.edu/DmData/DataDownload/WebServiceInfo.aspx)
- [Traditional and categorical statistics](https://droughtmonitor.unl.edu/About/AbouttheData/StatisticsExplanation.aspx)
- [Classification](https://droughtmonitor.unl.edu/About/AbouttheData/DroughtClassification.aspx)
- [Reuse and required attribution](https://droughtmonitor.unl.edu/About/Permission.aspx)

The app and exports retain the provider's attribution. Traditional percentages
are cumulative: D0 ≥ D1 ≥ D2 ≥ D3 ≥ D4. Exclusive stacked categories are computed
from adjacent differences; cumulative shares must not be stacked. None + D0
can differ from 100 by source rounding. D0 is abnormally dry; drought begins at
D1. The Drought Severity and Coverage Index is the sum of the five cumulative
shares, 0–500 index points.

The same severity, area threshold and year range apply to comparison, ranking
and export. The threshold spans 0.01–100% in 0.01% steps, matching the source's
reported precision. A count means **assessment weeks**, not exact physical drought days.
Missing weeks break runs. An observed run touching the selection or a missing
assessment has a censored boundary. These percentages describe county area,
not population, field conditions or plant water availability. Six selected
years do not establish a climate normal or trend.

**Soil Profile** (`/labs/soil-profile`) uses NOAA NCEI USCRN daily01 files for
Manhattan 6 SSW (WBAN 53974) and Oakley 19 SSW (03067), 2020–2025. The twelve
station/year captures contain 4,384 calendar station-days. Each reports separate
moisture and temperature tokens at 5, 10, 20, 50 and 100 cm; these record counts
do not mean every reading is valid. Five point measurements do not constitute
a depth-integrated root-zone mean.

Sources and citations:

- [Daily01 format and quality semantics](https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/README.txt)
- [Current field headers](https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/headers.txt)
- [NOAA products and requested citations](https://www.ncei.noaa.gov/access/crn/products.html)
- Diamond et al. (2013), [U.S. Climate Reference Network after one decade of operations](https://doi.org/10.1175/BAMS-D-12-00170.1).
- Bell et al. (2013), [U.S. Climate Reference Network soil moisture and temperature observations](https://doi.org/10.1175/JHM-D-12-0146.1).

Moisture is volumetric water content (m³/m³), not percent saturation or
plant-available water. Soil temperature is °C. Daily means use the local
standard day (UTC−6 at these stations), without daylight-saving shifts. The
daily product has no individual quality flags; NOAA does not calculate derived
values from erroneous raw inputs. `-99.000` moisture and `-9999.0` temperature
remain missing. No reason is invented for an individual missing reading.
Moisture may be suppressed near freezing, but daily mean temperature cannot
recover hourly freezing history. The cold-day count means daily mean soil
temperature ≤0°C, using its own reported-temperature denominator.

The display withholds additional out-of-range tokens outside 0–1 m³/m³ or
−50–60°C and preserves their original text. Datalogger version is text,
including NOAA's `-9.000` missing-version token. Medians, minima and maxima use
only reported values at the chosen depth, variable and calendar window. There
is no interpolation, cross-depth averaging or causal rainfall interpretation.

## Reproduce the display

The preparation script uses only the Python standard library. Its fixed plan
has 20 official objects: six county CSVs, twelve soil station/year files, the
daily README and field headers. No custom URLs, redirects or credentials are
accepted. Transport reads have object, aggregate-size, timeout and deadline
bounds. Original source captures must remain outside the repository and public
directory. A new capture directory is required; existing captures are preserved.

```sh
python3 scripts/prepare-drought-and-soil.py --capture-dir /absolute/private/new-capture
python3 scripts/prepare-drought-and-soil.py --source-dir /absolute/private/new-capture
```

Preparation verifies source URL, byte count and SHA-256; checks the exact
28-column NOAA header; enforces station IDs, coordinates, real dates, unique
identities, complete calendars, all county FIPS, format, validity intervals,
percent bounds and cumulative ordering. Both families are validated before
display files are written. The original captures and their transport receipt
remain private; selected values and source metadata become content-hashed app
assets. These hashes are computed by KFM, not provider-issued signatures.

Browser readers enforce exact display length and SHA-256 before validating the
full schema. Reads time out even if a transport ignores cancellation. A station
switch clears old soil results, cancels obsolete work and disables stale export.
CSV retains source tokens/qualification and settings; JSON retains provenance,
coverage and methods. The inspection date is recorded separately from the
analysis window when added by the UI.

## Evidence boundaries

These are provider-context display overlays, with review/source admission
PENDING and release UNRELEASED. They do not activate the fixed-30-day governed
USCRN pipeline, admit new evidence, change map carriers or imply hosted
publication. The monorepo source, standalone application, preserved Site and
production host remain separate identities. A local build or preview is local
evidence only. Preserve the source mirror's immutable receipt lineage when
updating any app file.

Meaningful verification covers scientific denominators, weekly run boundaries,
exclusive categories, schema identity, raw-token preservation, source integrity,
stalled/failed reads, stale UI completion, exports and responsive browser use.
