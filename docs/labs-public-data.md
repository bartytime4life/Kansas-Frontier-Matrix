# Labs with public data

The owner requested a functional, populated `/labs` on 2026-11-16. The page now
opens on five instruments with bundled public federal source snapshots. The
question shortcuts, previews, controls, tables, record inspection and downloads
use these same bundles. Additional instruments and planned stories remain
accessible through **All research**.

| Lab | Shipped coverage | Records |
| --- | --- | ---: |
| Climate Stripes | January 1895–October 2026, Kansas and nine climate divisions | 132 years, 10 areas, 3 monthly measures |
| County Pulse | Vintage 2025, July 1 estimates for 2020–2025 | 630 county-year rows; 105 per selected year |
| River Memory | Three USGS gauges, January 2020–November 2026 | 7,526 daily observations |
| Tornado Tracks | SPC whole tornadoes starting in Kansas, 1950–2025 | 4,582 |
| Shaking Ground | USGS M≥1 events, Kansas and immediate border region, 2010–2026 | 6,762 |

These are dated source snapshots, not live observations. Source revision,
coverage, missingness, qualifiers and interpretation limits remain visible.
Population estimates are selected one year at a time. Tornado rows sharing an
SPC identifier retain separate date/time/state-sequence identities. An earthquake
query reaching its 10,000-row cap fails acquisition rather than claiming completeness.

## Source and rights basis

The importer reads only public NOAA, Census and USGS endpoints. Each bundle
records the exact URLs, retrieval times, raw byte counts and SHA-256 hashes.
The generated manifest binds each shipping filename, size and SHA-256. The
browser verifies the file before accepting its data. Build validation rejects
unexpected files in `public/labs-data/`, invalid contracts and modified bytes.

- [NOAA nClimDiv downloads and format documentation](https://www.ncei.noaa.gov/pub/data/cirs/climdiv/)
- [Census public open-data policy](https://www.census.gov/topics/research/research-transparency-public-access/open-data.html)
- [USGS public-domain data and credit policy](https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits)
- [SPC source descriptions and actual-track downloads](https://www.spc.noaa.gov/wcm/)
- [USGS daily values service](https://waterservices.usgs.gov/docs/dv-service/)
- [USGS ComCat API documentation](https://earthquake.usgs.gov/fdsnws/event/1/)

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
node scripts/validate-labs-data.mjs
npm run build
node --test --test-concurrency=4 tests/*.test.mjs app/labs/atlas-model.test.mjs
```

Raw downloads stay under ignored `work/labs-raw/`; `--cache` can select another
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
