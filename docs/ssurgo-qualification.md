# SSURGO soil survey qualification

The pipeline catalog's wave 2 *Soil survey* lane (`app/pipeline-catalog.mjs`)
has this next gate: "Qualify one county, map units, units, rights and
validation". `SRC-CAND-SSURGO` stays `held` in `app/source-intelligence.ts`.

This record examines one survey area. It admits no source, writes nothing to the
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

To require the reviewed version (a mismatch holds; this does not request a
historical version from SDA):

```bash
node scripts/qualify-ssurgo.mjs KS169 --expected-version 23
```

The script reads one Kansas soil survey area (symbol `KS` plus three digits)
through USDA Soil Data Access, using five fixed, read-only query definitions
and a second survey read at the end:

| Query | Checks |
| --- | --- |
| `survey`, `surveyEnd` (`sacatalog`) | Exactly one matching area, name, positive integer version and readable save time; both identities must agree. An optional expected version must match both reads. The source timestamp is retained without inventing a timezone. |
| `mapunits` (`mapunit` via `legend`) | Map units exist and their keys are unique. Acres and kinds are recorded. |
| `components` (`component`) | Every map unit has a positive component count, distinct component keys within its group, no missing representative percentages, percentages within 0–100 totalling 100, and at least one major component. Duplicate or unexpected map-unit groups hold. |
| `polygons` (`mupolygon`) | Every map unit has a positive integer polygon count, with distinct polygon keys within its group. Duplicate groups, unmapped map units and polygon groups outside the tabular key set hold. |
| `units` (`sdvattribute`) | Each core column has published raw units. Every attribute is checked separately, including missing/blank/whitespace units. Unexpected units, aggregation or conflicting attribute identities hold. Unitless pH is intentional. AWC storage is recognized only as attribute 101, Available Water Storage, cm, Weighted Sum; raw AWC remains cm/cm. |

Anything missing or inconsistent is a **hold**, and the report's `state` is then
`held`. Facts a later product must handle are **findings**.

The v2 report keeps the exact SQL, its SHA-256, and the SHA-256 of each UTF-8
response text, without normalization. It always carries
`rights: "REVIEW_REQUIRED"`, `admitted: false`, `capture: false` and
`publication: false`. Required response headers, row shape and scalar cell
types are checked; errors cannot masquerade as empty tables. Each response
body is limited to 4 MiB while reading. The tests use a fake SDA offline.

These are qualification checks, not full source validation: no horizon values,
polygon coordinates, geometry validity/topology or global orphan components
are examined. Component queries join through the selected area's map units;
they cannot establish the absence of orphan rows elsewhere in USDA's database.
The polygon check is key coverage, not proof of geographic county coverage.

## Historical v1 record: Saline County (KS169), 2026-10-31

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

These digests identify the original queries at PR #5648 head
`a2a5207f3313a56e687cd64aa5e18ec6ab80bbcd`; they are not the new v2 query set.
Query changes require new digests. Response formatting or metadata changes
can also change a digest without changing the survey version.

## Technical review, 2026-10-31 (America/Chicago)

**CONFIRMED:** [PR #5648](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5648)
merged its two commits, including `a2a5207f33`. The automated review was of
`2b5748cdbb`, not independent approval of the correction. The five original
tests passed in this review. GitHub reports the head's Public core repair
candidate workflow succeeded; that is separate from this session's checks.

The current application base examined here is
`9bdf1e972223964e16ff88f5c8c7a994b300579b` on
`a0-hosted-ai-web-20261017`. Its three qualification files were unchanged from
the merged PR head. No open PR matching SSURGO was found during the overlap
check; this is a bounded title/search check, not proof that no other work overlaps.

**CONFIRMED live replay:** the unmodified v1 tool ran at
`2026-11-01T03:23:11.363Z` (October 31 locally). All five query digests and
all five response digests exactly matched the historical table above. It
returned version 23, the same source save time, 45 map units/461,645 reported
acres, 213 components and 4,772 polygons, with no holds. No upstream response
payload or dataset archive was saved. The matched digests substantiate this
replay, but cannot reconstruct the responses after USDA changes them.

**Confirmed defects corrected in v2:**

- `a2a5207f33` catches wholly missing dimensional units, but a valid sibling
  attribute could mask a missing unit. Whitespace and contradictory nonempty
  units also passed. The old test fixture even used percent for density,
  conductivity and AWC. Tests now use scientific units and check every attribute.
- Zero counts, duplicate groups, missing survey version/save time and wrong
  response columns could pass. Keys, counts, schema and survey identity now
  fail closed. SQL aggregation now exposes distinct keys, missing component
  percentages and percentage extrema rather than hiding nulls inside SUM.
- Non-100 component totals and absent major components were findings despite
  the documented hold rule. They now hold. This is a conservative KFM candidate
  requirement, not a claim that every USDA survey must satisfy that product rule.
- Independent reads could straddle a survey revision. The catalog identity is
  now checked before and after, and `--expected-version` rejects a changed pin.

The report format changes from `kfm-ssurgo-qualification-v1` to `-v2`; readers
must dispatch on that field and retain old reports as historical evidence.
No application import or scheduler consumer of this script was found. The
source catalog still has `SRC-CAND-SSURGO: held`; the soil lane cadence stays
disabled. The separate point soil display is unchanged.

**CONFIRMED v2 live validation:** at `2026-11-01T03:32:09.549Z`, with expected
version 23, the strengthened tool returned `ready-for-owner-review`, no holds,
and the same counts/save time. Both catalog reads agreed. The sole finding was
`UNIT_DEPENDS_ON_ATTRIBUTE`; rights remained `REVIEW_REQUIRED`, and admission,
capture and publication were false. The survey and map-unit query/response
digests match v1 above; `surveyEnd` repeats the survey digest pair. New pairs:

| Query | Rows | Query SHA-256 | Response SHA-256 |
| --- | --- | --- | --- |
| components | 45 | `6ac0aa8282f5a207447c77eae41ebc418b94e253f0937c757645d0690166a7ce` | `cbec6d48246a125187f79a162819b0a09906f4269e1086b9591de0dc1d0194dd` |
| polygons | 45 | `d330c38e41f4529970f8c5081fb9dbd4de3c81230324c7e23d763ad9c3ef9d66` | `b27f60d5b90b2c1f25fb074cb8b3a9f8a982aeb49b514382fb09f8b03e8984cd` |
| units | 13 | `c7ab9ebfa8e414e1053ac7f91d77c7bcce29d4630707341888cd386b065b027a` | `4768e7c93ec98df4a6bd04b04e9866c15a5ce80fb32bfd40675bf364198d041c` |

### Scientific meaning and units

USDA's [current SDM Tables and Columns](https://sdmdataaccess.nrcs.usda.gov/documents/TablesAndColumnsReport.pdf)
(November 2025, pp. 6–7) gives the raw horizon units below. The `_r` suffix
means representative value, not an observation time. Live SDV metadata at
`2026-11-01T03:24:44.256Z` identified AWC capacity attribute 41 and Soil Health
capacity attribute 2755 in cm/cm with Weighted Average; storage attribute 101
uses cm and Weighted Sum. That second attribute describes an aggregation,
not an alternative unit for a raw `chorizon.awc_r` value.

| Raw horizon field | Label/unit for an initial product |
| --- | --- |
| `awc_r` | Available water capacity, cm water/cm soil (`cm/cm`) |
| `claytotal_r`, `sandtotal_r`, `om_r` | Clay, sand, organic matter, percent (`%`; source token `percent`) |
| `dbthirdbar_r` | Bulk density at one-third bar, `g/cm³` (source `g/cm3`) |
| `ksat_r` | Saturated hydraulic conductivity, `µm/s` (source `um/s`) |
| `ph1to1h2o_r` | pH in 1:1 water, dimensionless; no invented dimensional unit |
| `hzdept_r`, `hzdepb_r` (proposed addition) | Horizon top/bottom depth, cm |

The [SDV metadata definition](https://www.nrcs.usda.gov/sites/default/files/2022-08/SSURGO-Metadata-Tables-and-Columns-Report.pdf)
(pp. 83–85) separates attribute identity, units and horizon aggregation. A later
product must bind these plus depth interval, component aggregation, null policy
and algorithm version to every derived value. AWS is AWC multiplied by included
thickness, then summed; cm becomes mm only through an explicit factor of 10.
Do not label raw AWC as storage or as current water/moisture. Missing measurement
values remain null with a reason; never convert them to zero or silently
renormalize incomplete component coverage.

## Source rights and sensitivity review

**CONFIRMED source evidence; owner acceptance remains open.**

- USDA's [SSURGO catalog record](https://catalog.data.gov/dataset/soil-survey-geographic-database-ssurgo)
  identifies public access and the public-domain label for SSURGO and its SDA
  distribution, record `430-14-14`, modified 2026-07-02. The label redirects to
  government copyright guidance; do not relabel it as a CC-BY or CC0 grant.
  During browsing, the NRCS overview's data.gov link resolved to a STATSGO2
  record. This review used the directly verified, explicitly titled SSURGO
  record instead; the cross-link is not evidence for SSURGO rights.
- USDA's [digital rights and trademark policy](https://www.usda.gov/about-usda/policies-and-links)
  permits copying/distribution of its public-domain information, requests credit,
  and notes protected third-party exceptions. A USDA logo requires permission
  and cannot imply USDA endorsement. No separate authenticated API key or
  contractual license requirement was observed for these public SDA reads;
  that observation is not an approved automated collection profile.
- The live KS169 `sacatalog.fgdcmetadata` response reports no access constraints.
  Its use constraints request USDA NRCS acknowledgement, retain responsibility
  with the user, describe planning/reference use rather than primary regulatory
  decisions, warn against misleading enlargement, require site investigation
  for intensive uses, and tell users to obtain updated versions. Distribution
  liability text disclaims general fitness/warranty. These are county-specific
  metadata findings, not an assurance of fitness for an individual property.
- [NRCS recommends a Web Soil Survey citation](https://www.nrcs.usda.gov/resources/data-and-reports/soil-survey-geographic-database-ssurgo).
  Proposed product credit: Soil Survey Staff, USDA NRCS; SSURGO, Saline County,
  Kansas (KS169), version 23; source access date and URL, plus KFM processing
  version and a clear statement of modifications. Keep the full source
  citation and use limitations reachable from the product and exports.

The county metadata was inspected in memory at `2026-11-01T03:24:50.492Z`
using [SDA POST](https://sdmdataaccess.sc.egov.usda.gov/Tabular/post.rest),
`format: JSON+COLUMNNAME`, and this exact read-only SQL:

```sql
SELECT fgdcmetadata FROM sacatalog WHERE areasymbol = 'KS169'
```

Query SHA-256:
`4243218f3c436536328ffafd64cb1cb70e7379cde74dac3381d86fdbd9580701`.
Response SHA-256:
`d9f66e5040135d94dd625cdf4e6e24bbc97e962247fcaa78ac8a014c2ede7117`.
This digest is an inspection receipt, not a retained metadata archive or rights
approval. Before authorized capture, retain the chosen distribution's metadata
and rights evidence under the existing governed evidence lifecycle.

**PROPOSED sensitivity boundary:** a county soil map with ordinary soil
properties is a plausible public planning product, but public-domain status
does not clear every location or linkage. Initially exclude pedon/sample
locations, special feature points/lines, human-artifact records, landowner or
parcel identities, and joins revealing archaeology, rare species, sensitive
infrastructure or cultural/Tribal information. Do not infer that mapped soil
permits entry to private land. The owner must decide whether exact county
polygons and any intended overlays require redaction, generalization or
consultation; no sovereign/cultural clearance is established here.

## Bounded initial product recommendation — PROPOSED, not admitted

Start with one versioned **KS169 map-unit soil context** product for planning.
USDA describes map units as mixtures of components, with mapping scales that
vary by survey; the initial product must not locate a particular component
inside a polygon or assert parcel/site conditions. Survey area is the source
extent, not necessarily an administrative county boundary.

| Part | Proposed fields and treatment |
| --- | --- |
| Map unit | `areasymbol`, `mukey` as a string, `musym`, `muname`, `mukind`, `muacres` labelled USDA-reported acres; name/version/save time, source URL, access time and evidence reference. These describe the unit; acres are not a new polygon-area calculation. |
| Components | Keep every `cokey` and parent `mukey`, `compname`, `compkind`, `comppct_r` (%), `majcompflag`, `slope_r` (%), `drainagecl`, `hydgrp`, `hydricrating`. Preserve nullable categories and representative-value meaning. Show shares and all components; do not copy each component as if it fills the whole polygon. |
| Horizons | Keep `chkey`, parent `cokey`, `hzname`, `hzdept_r`, `hzdepb_r` and the seven raw measurements above. Report missingness and depth coverage. Validate foreign keys, depths, ranges and published units before admission. Preserve any supplied low/high values if later selected, with separate semantics. |
| Derivatives | Defer map-unit AWS and other rankings from the first product. If added, define depth clipping, missing-depth treatment, component weighting/cutoff, contributing share and calculation version explicitly. Do not sum overlapping or compound horizon records blindly. |
| Geometry | Prefer the official KS169 WSS polygon distribution with its matching tabular edition and metadata, or an independently version-matched SDA geometry export. Keep original bytes/CRS after capture is authorized; validate polygon keys, actual CRS, geometry validity, empties, bounds, overlaps/gaps and area tolerances. This review fetched no coordinates and does not select a verified CRS or simplification tolerance. |
| Display geometry | Generate a separate, labelled derivative with shared-boundary/topology-aware simplification and recorded error tolerance; preserve an unsimplified analysis source and all key joins. Never compute scientific areas from display tiles or imply added detail at high zoom. Generalize/redact if the sensitivity review requires it. |

The [USDA relationship report](https://sdmdataaccess.nrcs.usda.gov/documents/TableRelationshipsReport.pdf)
supports `legend.lkey -> mapunit.lkey`, `mapunit.mukey -> component.mukey`,
and `component.cokey -> chorizon.cokey`. Polygon linkage uses the area and
`mukey`, not symbol/name alone. The [column descriptions](https://sdmdataaccess.nrcs.usda.gov/documents/TableColumnDescriptionsReport.pdf)
explain representative ranges, polygon identifiers and compound horizons;
overlap in horizon depths can reflect compound records rather than corruption.
Full horizon validation and geometry qualification remain **NEEDS VERIFICATION**.

### Pinning, updates and owner decisions

USDA's [SDA Query Guide, pp. 37–38](https://sdmdataaccess.nrcs.usda.gov/documents/SoilDataAccessQueryGuide.pdf)
states that SDA holds the latest survey-area version; historical versions are
described as held in a separate warehouse. Neither a WHERE clause on the current
catalog nor `--expected-version` retrieves a historical snapshot. Bracketing
detects observed catalog drift, not a transactional snapshot across requests.
The archive retrieval path for KS169 v23 is **NEEDS VERIFICATION**.

Proposed immutable identity is the tuple of area symbol, catalog version and
source save time, plus the chosen spatial/tabular editions, metadata and exact
payload digests. Bind transformation/tool revision, queries, units, source
rights, sensitivity and EvidenceRef/EvidenceBundle links to that edition.
Do not invent a timezone for `8/27/2026 2:33:36 PM`. Keep access time separately
in UTC. Do not assume `spatialversion` equals catalog `saversion`.

After authorization, use manual version checks initially. A changed version,
save time, metadata or digest creates a new held candidate; a missing pinned
version must not fall back to latest. Review source changes, rights, units,
relationships, geometry and scientific effects before promotion. Retain the
previous released edition and its evidence; a governed alias change and
rollback receipt, not overwriting data, selects the successor. Cadence remains
disabled until an owner-approved profile defines bounds, retry/rate limits,
review triggers, retention, correction and rollback.

The owner must authorize independently:

1. Accept the source-specific public-domain evidence, attribution and use
   limitations for the chosen distribution; resolve any third-party exceptions.
2. Approve sensitivity/exposure and exact geometry/overlay boundaries, including
   any cultural consultation, generalization or denial.
3. Select fields, horizon/depth policy, geometry carrier and tolerances; approve
   scientific review and required validation evidence.
4. Approve a bounded capture/storage profile and reproducible version retention.
5. Separately authorize admission/promotion and any publication/release, with
   reviewer separation, correction and rollback. This PR provides no such decision.

### Validation, placement and rollback

On Node `v22.23.3`, 29 tests passed across the qualification, pipeline-domain,
crop-soil, subsurface-soil and soil-map-state suites. The qualification suite
contains 15 tests, including parameterized negative cases. Changed-file ESLint,
TypeScript (`--noEmit --incremental false -p .`) and `git diff --check` passed.
The full application suite and production build were not rerun: no served
application module, dependency or build configuration changes. These checks
are distinct from the original PR's reported test counts and GitHub workflow.

The focused suite covers all original missing-unit cases plus sibling masking,
whitespace, contradictory units, pH, AWC storage identity/aggregation, malformed
responses, null coercion, duplicate/count/key mismatches, partial percentages,
version drift/pins and invalid CLI options. Tests do not prove upstream rights,
geometry, horizon completeness, deployment or source admission.

Only the existing `scripts/qualify-ssurgo.mjs`,
`tests/ssurgo-qualification.test.mjs` and this document are changed. Placement
uses the standalone application's existing operator-script, executable-test
and explanatory-document homes. The checked project mirror's Directory Rules
v2 and accepted ADR-0029 establish responsibility/lifecycle separation;
`Directory Rules.pdf` was absent from this session's supplied source inventory.
No new registry, schema, policy, payload or release home is introduced. This
standalone script is not a replacement for canonical monorepo admission tools.

Rollback is a reviewed revert of the three source changes, retaining this review
as history. No database, dataset, schedule or release migration is involved.
Reverting also restores the old qualification weaknesses and v1 format; it
does not confer admission or publication authority.
