# County pages (2026-11-23)

Each of the 105 Kansas counties now has a plain page at `/counties/<name>` (for example
`/counties/sedgwick`), with an index at `/counties`. The guides index links to it.

## What a county page shows

Eight Census Bureau estimates for 2020–2024, each with its 90% margin of error: median
household income, median age, median home value, median gross rent, the share of adults 25 and
over with a bachelor's degree or higher, the share of people below the poverty line, the share
of occupied homes lived in by their owner, and housing units. Four also show their 2010–2014
estimate and margin of error. The County Observatory link selects the page's county.

A button opens the map centred on the county with county outlines on
(`/?ctx=census-counties&c=<lon>,<lat>&z=8.5`). The centre is the middle of the county's bounding
box, used only to aim the map.

## Population and bridges (added 2026-11-23, second pass)

- **Population.** The page opens with the Census Bureau's July 1 population estimate for the
  newest year (2025) beside its estimate for 2020, with the difference. A later release can
  revise earlier years, and the page gives the two estimates without saying why they differ.
- **Bridges.** A short section counts the county's records in the Kansas Department of
  Transportation bridge inventory: the total, how many are on state highways and on local
  roads, the oldest recorded built year, the longest structure, how many are recorded as closed
  to traffic, and how many local-road bridges are marked as on the National Register. A link
  opens the map on the county with both bridge layers on. The page says these are inventory
  records, not always one physical bridge each, and that a recorded status is not a safety
  assessment. The generator fails if any inventory record does not belong to one of the 105
  counties, so the 105 counts add up to the whole inventory (24,877 records as of 2026-11-16).

Both come from bundles the labs already ship (`public/labs-data/census-mosaic-*.json` and
`public/labs-data-bridges/built-kansas-*.json`), through the same generated table.

## Where the numbers come from

Nothing is fetched when a page is read. The pages read `app/county-facts.generated.json`, which
`scripts/prepare-county-pages.mjs` writes from the county bundle the County Conditions lab
already ships (`public/labs-data-observatory/county-conditions-*.json`: American Community
Survey 5-year estimates for all 105 counties, with source URLs and response hashes inside it).
After that bundle changes, run:

```bash
node scripts/prepare-county-pages.mjs
```

A test regenerates the table from the bundle and fails if the committed file differs.

## What the pages will not say

- **Dollars are not compared across periods.** The bundle keeps each period's own dollars,
  without an inflation adjustment, so income, home value and rent are shown for 2020–2024 only.
  The earlier dollar amounts are not carried into the generated table at all.
- **Change labels use both periods' margins of error.** For median age, education and poverty,
  the page uses the [Census Bureau comparison method](https://www2.census.gov/programs-surveys/acs/tech_docs/statistical_testing/2025_Instructions_for_Stat_Testing_ACS.pdf)
  at 90% confidence. The absolute difference must exceed the square root of the sum of the
  squared margins. The page says “Difference uncertain” when it falls within that threshold.
  Education and poverty use margins derived by the shipped County Conditions bundle.
- The page calls the figures survey estimates for a five-year period, not a count for a year,
  and says they are public context from the Census Bureau, not Kansas Frontier Matrix evidence.

## Routes and the sitemap

- `app/counties/[slug]/page.tsx` is the application's first dynamic page route. It lists its
  105 addresses with `generateStaticParams`; any other address answers 404.
- `/sitemap.xml` grows from 9 addresses to 129: `/counties`, the 105 county pages, and 14 public
  reading pages that were reachable from the site but never listed (`/topics`, `/civic`,
  `/curated`, `/data-library`, `/observatory`, `/observatory/sources`, `/labs` and five lab
  pages, and the two history pages). Pages `robots.txt` disallows, status pages and the
  Knowledge search (whose store is not provisioned) are left out.

## Checks

`tests/county-pages.test.mjs`: the generated table matches the bundle; 105 unique addresses with
centres inside Kansas, complete estimates and county handoff links; the two-margin comparison
and threshold; the source and dollar-period statements; the sitemap contents against
`robots.txt` and the page files.
In a browser at desktop and phone widths the county page and the index had no accessibility
violations (WCAG 2.2 A and AA rules) and no sideways scrolling.
