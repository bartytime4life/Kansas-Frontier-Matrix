# SSURGO soil survey qualification

The pipeline catalog's wave 2 *Soil survey* lane (`app/pipeline-catalog.mjs`)
has this next gate: "Qualify one county, map units, units, rights and
validation". `SRC-CAND-SSURGO` stays `held` in `app/source-intelligence.ts`.

This record qualifies one county. It admits no source, writes nothing to the
pipeline store, publishes nothing, and decides no rights. The Field view's
point soil reading (`app/api/cropland/soil/route.ts`) is separate display
context and is unchanged.

## Method

To run it:

```bash
node scripts/qualify-ssurgo.mjs KS169
```

Or, to write the report to a new file:

```bash
node scripts/qualify-ssurgo.mjs KS169 --out /absolute/report.json
```

The script reads one Kansas soil survey area (symbol `KS` plus three digits)
through USDA Soil Data Access, using five fixed, read-only queries:

| Query | Checks |
| --- | --- |
| `survey` (`sacatalog`) | The survey area exists, and its published version and save time are recorded. |
| `mapunits` (`mapunit` via `legend`) | Map units exist and their keys are unique. Acres and kinds are recorded. |
| `components` (`component`) | Every map unit has components. Representative percentages total 100, and each map unit has a major component. |
| `polygons` (`mupolygon`) | Every map unit has polygons, and no polygon names a map unit outside the area. |
| `units` (`sdvattribute`) | SSURGO publishes each core horizon property: `awc_r`, `claytotal_r`, `dbthirdbar_r`, `ksat_r`, `om_r`, `ph1to1h2o_r` and `sandtotal_r`. Every property except pH, which has no unit, needs a non-empty published unit. A missing or empty unit is a hold. |

Anything missing or inconsistent is a **hold**, and the report's `state` is then
`held`. Facts a later product must handle are **findings**.

The report keeps a SHA-256 digest of every query and its response text. It
always carries `rights: "REVIEW_REQUIRED"`, `admitted: false` and
`publication: false`. `tests/ssurgo-qualification.test.mjs` covers the checks
with a fake Soil Data Access, offline.

## Saline County, Kansas (KS169), 2026-10-31

Run at `2026-10-31T19:55:47Z` against
`https://sdmdataaccess.sc.egov.usda.gov/Tabular/post.rest`.

| Item | Result |
| --- | --- |
| State | `ready-for-owner-review`, no holds |
| Survey | Saline County, Kansas, version 23, saved `8/27/2026 2:33:36 PM` (as SDA reports it, without a time zone) |
| Map units | 45 (40 consociations, 4 complexes, 1 undifferentiated group), 461,645 acres |
| Largest map units | Lancaster-Hedville complex, 3–20% slopes (92,370 ac) · Tobin silt loam, occasionally flooded (37,886 ac) · Crete-Wells complex, 3–7% slopes (26,989 ac) |
| Components | 213 across all 45 map units; every map unit totals 100%, and every map unit has a major component |
| Polygons | 4,772, covering all 45 map units; none unmapped or orphaned |
| Horizon units | `awc_r` cm/cm (per horizon) and cm (depth-summed storage) · `claytotal_r` percent · `sandtotal_r` percent · `om_r` percent · `dbthirdbar_r` g/cm3 · `ksat_r` um/s · `ph1to1h2o_r` no unit (pH) |

One finding: `UNIT_DEPENDS_ON_ATTRIBUTE`. The column `awc_r` is published as
*Available Water Capacity* in cm/cm and as *Available Water Storage* in cm, a
depth-integrated value computed from the same column. A soil product must tie
each value's unit to the attribute it shows, not to the column name.

Receipts (SHA-256):

| Query | Rows | Query digest | Response digest |
| --- | --- | --- | --- |
| survey | 1 | `3bcb75a20b589ee3766baf71227a11f71ae082b36706bfbd0e895007f0e0c40a` | `041ce6167a46e43241244420d56d763e82c6db7f5342c84c02cd813d84a2ec37` |
| mapunits | 45 | `f1b0e7409d772c5d4b682cd546c2d6777dc356047f6d6b191a3a8fb08ab3169b` | `ba633015af3beb81e85d3215a49aff7f1d2036e31516ec43b7a982a8227721d9` |
| components | 45 | `20b4881a9339115043728664886e81d51e25ad40e3a110088594f97159470b6a` | `8e72442d843ec1a628b0185f1780e134d97fe63716f958619fa23e8cc057d847` |
| polygons | 45 | `6363f19c8f665c98335477a2e49c90cee5ad8921920b2b1be5daa5e451f56c61` | `79682ccf44e6ceeefe639da1b6432ed36f66ec4fcff50680f6fe1b7f66370bc0` |
| units | 13 | `8b00906fdc99474beff663a2beebfd769f53c2cd27bb23eff7fe2be206b7551a` | `f46324b07d03eb1ddd4220c9ac0df58e439ca3e92d060119052c496c34caaea1` |

The query digests stay fixed for KS169. SSURGO is revised over time, so a later
run against a new survey version gives different response digests.

## Rights and what's left for the owner

NRCS recommends this citation: "Soil Survey Staff, Natural Resources
Conservation Service, United States Department of Agriculture. Web Soil Survey.
Available online at https://websoilsurvey.nrcs.usda.gov/. Accessed
[month/day/year]." SSURGO is a federal National Geospatial Data Asset, and U.S.
federal government works are generally not subject to copyright. That is
background, not a rights decision: the owner records rights and sensitivity
when reviewing the source.

Before any SSURGO product is admitted:

1. Owner review of rights and sensitivity for `SRC-CAND-SSURGO`.
2. Choose the product: which map-unit and component fields, which horizon
   attributes (each bound to its unit as above), and the geometry source and
   simplification.
3. Pin the survey version (KS169 version 23 here) and decide how a new version
   replaces an old one.
4. Only after that, add a bounded capture and review profile. The lane's cadence
   stays disabled until then.
