# Kansas records (2026-11-23)

`/records` lists the extremes in four public datasets the site already ships: 22 entries in four
groups. It is linked from the county index and the guides index, and is in the sitemap.
The group links near the page title jump to each section. Each section also opens its
interactive data view in County Pulse, County Observatory, Built Kansas or Tornado Tracks.

| Group | Dataset | Examples |
|---|---|---|
| People | Census Bureau July 1 population estimates, 2020 and 2025 | Most and fewest people; largest gain and loss; fastest growth and steepest decline |
| Income, age, education and homes | American Community Survey 5-year estimates, 2020–2024 | Highest and lowest median household income; oldest and youngest median age |
| Bridges | KDOT bridge inventory | Oldest recorded built year; longest structure; most and fewest records in a county |
| Tornadoes | Storm Prediction Center tracks that started in Kansas, 1950–2025 | Longest and widest path; most reported deaths; year with the most |

## What a record here means

Each entry is the largest or smallest value **in one named dataset, for the years it covers**.
The page says so at the top, and each group ends with its source and a limit taken from the
dataset's own stated limits:

- Survey estimates carry their 90% margin of error, and the page says the county shown may not
  truly rank first where margins overlap.
- Bridge entries are inventory records, not always one physical bridge. The inventory's wording
  for a bridge is quoted as recorded ("I135 HWY SB" over "RR , 12CITY ST& STRM"), because tidying
  an abbreviation would be guessing. Unknown built years are left out.
- Tornado deaths are for the whole track, which can extend outside Kansas, and tracks that began
  in another state are not in the dataset. Counts by year are not presented as a trend.
- Earthquakes and river flow are left out: the earthquake bundle covers the border region as
  well as Kansas, and the river bundle holds three gauges.

A tie is reported as a tie ("Shared by 2 counties; the first alphabetically is shown").

## How it is built

Nothing is fetched when the page is read. `scripts/prepare-kansas-records.mjs` reads the four
bundles in `public/`, verifies their recorded sizes and SHA-256 checksums, and writes
`app/kansas-records.generated.json`. Each group's **Source data** disclosure links to the exact
JSON snapshot and shows its checksum. Run the generator after a bundle changes.

```bash
node scripts/prepare-kansas-records.mjs
```

`tests/kansas-records.test.mjs` regenerates the table and fails if the committed file differs,
recomputes several extremes straight from the bundles, and checks the tie and missing-value
handling.
