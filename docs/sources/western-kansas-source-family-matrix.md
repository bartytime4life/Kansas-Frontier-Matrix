<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/source-review/western-kansas-family-matrix
title: Western Kansas source-family review matrix
type: reference
version: v1.2
status: draft; repository-grounded; bounded source review; non-authoritative
owners: ["@bartytime4life — CODEOWNERS review route; accountable source/rights acceptance remains separate"]
created: 2026-11-27
updated: 2026-11-27
policy_label: repository-facing
owning_root: docs/
responsibility: Explain the seven drought/hydrology source families, their current scoped registry evidence, publisher documentation, distinct clocks, rights and correction gaps, and next review without admitting or activating a source.
truth_posture: "CONFIRMED repository declarations and retrieved publisher metadata; PARTIAL seven-family acceptance; UNKNOWN unreviewed terms, spatial support and operational consumer closure"
evidence_snapshot: "Matrix registry facts: main@9c7ab6014ed568dc51794b3e27c1cf18bf02f11d; inactive USDM candidate: main@490d61906ebb2760565858f41bc1bad436e65c32; unverified-rights shape refinement base: main@aec796b3521e7b3698d7f404a0f98f47f6b0e366; publisher documentation read 2026-11-27 local"
related:
  - docs/sources/README.md
  - contracts/domains/hydrology/western_kansas_observation_assessment.md
  - contracts/source/source_rights_currentness_assessment.md
  - fixtures/domains/hydrology/western_kansas_observation_assessment/multiclock/README.md
  - docs/adr/ADR-0044-owner-self-release-for-admitted-public-water-data.md
  - docs/adr/ADR-0045-owner-self-release-for-admitted-public-weather-data.md
  - docs/adr/ADR-0046-owner-self-release-for-admitted-public-soil-data.md
[/KFM_META_BLOCK_V2] -->

# Western Kansas source-family review matrix

This review advances [#2899](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/2899),
[#3390](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3390) and
[#3393](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3393).
It follows the [synthetic multi-clock rehearsal](../../fixtures/domains/hydrology/western_kansas_observation_assessment/multiclock/README.md).
Repository facts are pinned to `9c7ab6014ed568dc51794b3e27c1cf18bf02f11d`;
external documentation was read on **November 27, 2026**. No observation payload,
private well/ownership record, current drought condition or production state
was retrieved or assessed.

Scope is the governed drought/observation pilot registry. Separate local-data
SQL/archive feeds and their owner authorizations are not re-adjudicated here;
absence from this bounded registry review does not establish that those feeds
or records are absent. Their own rights/capture/release lineage is required
before using them in this governed proof.

The reviewed registry contains **three bounded approved pilot descriptors**:
USGS discharge, GHCN-Daily weather and USCRN soil. They do not admit every
product from those agencies. The central
[source-authority projection](../../control_plane/source_authority_register.yaml)
still has no entries; its incompleteness does not erase later source-specific
decisions in accepted ADRs. This is a bounded review of the seven families,
not an exhaustive active-source census.

## Repository disposition

| Family from the existing assessment | Registry evidence at the pin | What the existing scope supports | First unresolved step |
|---|---|---|---|
| USDM | No matching admitted descriptor found in the inspected `data/registry/sources/` identities; a [human product page](catalog/drought_monitor/drought-monitor.md) exists. | Synthetic proof and an inactive dated-ZIP review fixture; provider documentation and HTTP metadata are not KFM admission. | Review the [existing inactive candidate](../../fixtures/contracts/v1/source/source_descriptor/valid/valid_usdm_inactive.json), including attribution, polygon support, rights and source-correction questions. |
| USGS streamflow | [USGS descriptor](../../data/registry/sources/hydrology/usgs_nwis.yaml), approved/active, with [ADR-0044](../adr/ADR-0044-owner-self-release-for-admitted-public-water-data.md). | Provisional instantaneous discharge, parameter `00060`, at **USGS-06892518 and USGS-07156900**. | Reproduce one admitted package and its actual decision/readback; wider stations, groundwater and other variables need their own scope review. |
| KGS groundwater | No WIZARD-specific admitted descriptor found in the inspected registry identities. | Published database metadata provides discovery and review context. | Resolve current product/terms, per-well provenance, sensitivity and permitted precision before creating a candidate descriptor. |
| Precipitation / EDDI | [GHCN-Daily descriptor](../../data/registry/sources/atmosphere/noaa_ghcnd.yaml), approved/active, with [ADR-0045](../adr/ADR-0045-owner-self-release-for-admitted-public-weather-data.md); no reviewed EDDI descriptor found. | `PRCP`, `TMAX`, `TMIN` at **USW00003928, USW00013996, USW00013985 and USW00023065**. This is station weather, not EDDI authority. | Keep the admitted precipitation branch separate from a proposed, explicitly versioned CPC EDDI branch. |
| Soil moisture | [Soil USCRN descriptor](../../data/registry/sources/soil/noaa-uscrn.yaml), approved/active, with [ADR-0046](../adr/ADR-0046-owner-self-release-for-admitted-public-soil-data.md). The [agriculture USCRN file](../../data/registry/sources/agriculture/noaa-uscrn.yaml) and SMAP files remain proposals. | Daily moisture/temperature at **WBAN 53974 and 03067**, depths **5/10/20/50/100 cm**. | Verify station/depth-specific package closure; a modeled SMAP product needs a distinct descriptor and rights/method review. |
| Agriculture context | [Quick Stats](../../data/registry/sources/agriculture/nass_quickstats.yaml), [Crop Progress](../../data/registry/sources/agriculture/nass_crop_progress.yaml) and [USDA-NASS](../../data/registry/sources/agriculture/usda-nass.yaml) files are `PROPOSED` placeholders. | Existing synthetic aggregate/context checks do not admit a live NASS product or establish crop loss. | Choose one published aggregate product and resolve support, suppression, access and rights. |
| Water-management / watershed boundaries | Both [WBD proposal paths](../../data/registry/sources/hydrology/usgs_wbd.yaml) and [wbd.source.yaml](../../data/registry/sources/hydrology/wbd.source.yaml) remain placeholders. | Synthetic reference/join context only. | Resolve one descriptor identity, versioned geometry, CRS and permitted joins; retain both old paths until an explicit alias decision exists. |

Family names above are the existing assessment's labels. Role descriptions are
human explanations; they do not add strings to the SourceDescriptor schema or
normalize its vocabulary. Filename similarity does not make the three SMAP
proposals or the two WBD proposals aliases. Other registry locations and external
stores were not exhaustively inspected.

## Existing rights records

| Reviewed pilot | Descriptor declaration and recorded verification | Citation/release boundary |
|---|---|---|
| USGS discharge | `verified_open`; owner verification **2026-10-10**; USGS-authored public-domain data with provisional-data qualification. | Retain USGS attribution, station and retrieval identity, and provisional notice; ADR-0044's exact water gate/license scope. |
| GHCN-Daily | `verified_open`; owner verification **2026-10-11**; NOAA federal station data, preliminary and revisable. | Preserve the descriptor's GHCN-Daily Version 3/Menne citation, DOI and subset; ADR-0045's weather profile excludes unreviewed volunteer-network scope. |
| USCRN daily01 | `verified_open`; owner verification **2026-10-11**; NOAA federal station data subject to revision. | Retain NOAA NCEI/USCRN daily01 attribution and revision notice; ADR-0046's exact soil profile and admitted station/depth scope. |

These are declarations in the three linked descriptors, not new legal findings.
This pass does not change `last_verified_at`, the named reviewer or a release
license list. Reading a publisher page on November 27 does not renew an older
rights decision. Other products cannot inherit these license strings or the
scoped owner self-release exceptions.

## Publisher facts, rights and correction boundaries

### USDM: classification and required credit

The publisher describes a weekly retrospective classification, not a forecast.
Its production guide places the normal release on Thursday at 08:30 Eastern,
after the Tuesday data window. Keep a product's valid date and actual publication
separate; do not manufacture either from retrieval time or a nominal schedule.
[USDM explanation](https://droughtmonitor.unl.edu/About/WhatistheUSDM.aspx),
[production timeline](https://drought.unl.edu/Education/Tutorials/Usdm/Section-Six.aspx).

The permission page authorizes third-party commercial and noncommercial use of
the map and associated data with its required attribution. Use the publisher's
current credit format, which includes the NDMC/USDA/NOAA/NASA partnership and
NDMC attribution. This observed permission is review evidence, not an accepted
KFM license declaration. Exact distribution, transformations and citation text
still need the candidate review.
[Publisher permission](https://droughtmonitor.unl.edu/About/Permission.aspx).

Pin each classification release and digest. A later week's map is a successor,
not a silent rewrite of a prior briefing. Any exceptional correction must retain
the original capture and an attributable replacement link. A polygon/county
intersection cannot establish uniform conditions, groundwater state or a legal
drought declaration.

### USGS: preserve provisional observations and API identity

The migration guide distinguishes continuous, daily, field-measurement and
station-metadata collections. Continuous observation times, approval status,
qualifiers and units remain source fields; a response timestamp is not an
observation timestamp. Higher-volume access has an API-key boundary.
[Modern API migration](https://api.waterdata.usgs.gov/docs/ogcapi/migration/).

USGS explicitly warns that provisional records can change after review. Retain
both captured versions and qualifiers; missing values remain missing.
[Provisional-data statement](https://waterdata.usgs.gov/provisional-data-statement/).
The publisher currently schedules legacy WaterServices retirement for the first
quarter of 2027. That is a dated provider statement, not permission to re-enable
legacy endpoints or change a pinned KFM cutover rule.
[Retirement notice](https://waterdata.usgs.gov/blog/api-waterservices-decom/).

The existing descriptor records owner-verified open rights on October 10, 2026,
USGS attribution and a two-hour pilot staleness threshold. Those are scoped
repository declarations. This review does not renew the rights verification or
extend it to all USGS data, wells, variables or stations.

### KGS: mixed measurement cadence and historical terms

The WIZARD FGDC metadata describes mostly winter annual depth-to-water
measurements, with some more frequent series and incomplete records. It also
describes public access excluding private ownership, and warns about accuracy
and completeness. **Its metadata date is January 2, 2002**: treat it as historical
provider evidence, not a freshly verified redistribution/access decision.
[WIZARD metadata](https://geohydro.kgs.ku.edu/geohydro/wizard/wizardfgdc.html).

Require current terms and product identity, measurement date/method, datum,
units, native well support and quality flags. Preserve depth-to-water versus
water-level elevation distinctions. A recent database update cannot refresh an
old measurement. Ownership, exact-location exposure and reconstructive joins
remain review questions; this pass retrieved no well records. Corrections must
refer to the exact measurement/version, not replace an aquifer-wide condition.

### Precipitation and EDDI: two different products

GHCN-Daily documents station/element identity, units, quality/source flags and
dataset-version citation. Preserve those fields and the captured version; a
revised station file must not erase its predecessor. The four-station admission
does not include every volunteer network, EDDI, or regional interpolation.
[GHCN-Daily documentation](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt).

CPC now hosts an **experimental EDDI** product transitioned from PSL. Record the
selected producer, algorithm/version, aggregation window, native grid, reference
period and uncertainty from that exact product. Do not copy legacy PSL metadata
into a CPC descriptor or turn an evaporative-demand diagnostic into measured
soil moisture, crop loss or a forecast merely because it is an early-warning
tool. EDDI redistribution/access terms and KFM admission remain unresolved here.
[CPC EDDI](https://www.cpc.ncep.noaa.gov/products/Drought/eddi/).

### Soil: point measurements and modeled grids remain separate

NCEI's USCRN products distinguish daily station-year files from soil-anomaly
products and document corrections. Keep observation day, publication/capture,
depth, units, missing flags and source revision separate. The admitted daily01
scope is the two stations and five depths in the matrix; the descriptor's
three-day staleness threshold is a pilot rule.
[USCRN products](https://www.ncei.noaa.gov/access/crn/products.html),
[daily01 format and revision notes](https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/README.txt).

For comparison, the separately identified **SPL4SMGP Version 8** product provides
three-hourly, nominal 9 km surface/root-zone estimates from the L4 algorithm and
requires dataset citation. This is an explicitly identified research candidate,
not a claim that SMAP is admitted or interchangeable with USCRN probes. Product
version, modeled support, depth definition, access and terms need their own
review; nominal grid spacing is not field-level certainty.
[NASA NSIDC product and citation](https://nsidc.org/data/spl4smgp/versions/8).

### Agriculture: published aggregates and suppression

Quick Stats supports queries by commodity, location and period; its bulk exports
are updated after weekdays. That delivery cadence is different from a record's
reference year or observation period.
[NASS Quick Stats](https://www.nass.usda.gov/Quick_Stats/).
Crop Progress instead reports selected-state/U.S. progress and condition during
the growing season, normally on the first business day of the week. It is not
a county-wide observation merely because reporters cover counties.
[Crop Progress and Conditions](https://www.nass.usda.gov/surveys/guide-to-nass-surveys/crop-progress-and-condition).
Keep its reference week, source publication and retrieval as separate clocks.

Preserve suppression, missing, trace and rounding states. In particular, withheld
values are not zero and must not be reconstructed by subtraction or joined to
identify a farm/operator. NASS's confidentiality pledge is an explicit boundary
for identifiable respondent data.
[NASS confidentiality](https://www.nass.usda.gov/About_NASS/Confidentiality_Pledge/).
Exact public-product rights, citation, redistribution, API credentials/rate
limits and release support remain unaccepted in the placeholder descriptors.

### Boundaries: versioned reference geometry, not cause

WBD identifies nested drainage units, including HUC12, with optional finer
levels in some areas. A selected HUC12 is a versioned spatial reference, not
evidence of water condition, ownership, responsibility or causation.
[USGS hydrologic units](https://www.usgs.gov/faqs/how-can-i-find-huc-hydrologic-unit-code-a-stream-how-can-i-find-namelocation-a-stream-using).
The data dictionary defines unit IDs, geometry attributes and a load date; load
date is not the time of an environmental observation.
[WBD dictionary](https://www.usgs.gov/ngp-standards-and-specifications/watershed-boundary-dataset-wbd-data-dictionary).

USGS distinguishes monthly national downloads from HU2 packages regenerated
after edits. Pin the actual package, geometry digest, CRS, scale and identifier
crosswalk; never call the family universally monthly or silently replace a
basin boundary beneath an old join. Dataset-specific use constraints and KFM
admission still require review.
[Download products and cadence](https://www.usgs.gov/national-hydrography/access-national-hydrography-products).

## Review and next proof

### Inactive polygon candidate follow-through — November 27

The [existing USDM fixture](../../fixtures/contracts/v1/source/source_descriptor/valid/valid_usdm_inactive.json)
retains `src:usdm-weekly`, now narrowed to **USDM_20261124_M.zip**. It proposes
the existing `map_artifact` type and `derived_public_product` role for this
published classification; the mapping is review input, not an accepted decision.
No second identity or registry writer is created.

A metadata-only **HEAD** to the
[dated publisher ZIP](https://droughtmonitor.unl.edu/data/shapefiles_m/USDM_20261124_M.zip)
returned HTTP 200 at **2026-11-28T01:49:02.103102Z** (November 27 locally),
length 1,857,301 bytes, ZIP content type, an opaque ETag and Last-Modified.
These identify observed response metadata only. No ZIP body was read, no
content SHA-256 was computed, and neither actual validity nor publication time
was authenticated. Do not treat Last-Modified as publication or observation time.
Inspect the embedded metadata and actual CRS/support after authorization;
impacts, grids and statistics remain separate distributions.
[Publisher format notes](https://droughtmonitor.unl.edu/DmData/Metadata.aspx).
Existing connector response fixtures remain synthetic examples, not captures
of this dated ZIP.

Rights and permissions remain `unknown`, review is pending, the connector is
disabled and public release is false. The earlier v0.2 fixture used an explicit
synthetic sentinel because the shape required non-null verification values.
The proposed [bounded pre-review form](../../contracts/source/source_descriptor.md#verification-not-yet-performed)
now permits both required fields to be `null` with strict inactivity and
non-release constraints; v0.3 removes the date and verifier sentinels. Null means
no verification, not a fresh or approved rights decision. Existing non-null
records keep their prior constraints. Registry writer/placement, accountable
source-specific review and actual archive evidence remain unresolved.

The [offline negative tests](../../tests/schemas/test_usdm_source_descriptor_contracts.py)
exercise the existing schemas: unresolved rights block public release even
with approved review; pending review blocks live activation and release; the
human label `classification` cannot extend the role enum. These are schema
checks, not runtime policy or release proof.

### Required next decisions

The next proposed unadmitted product is **one USDM distribution/version**: its
classification role and published attribution terms are explicit, and it adds
context to the three existing pilots without pretending to measure groundwater
or agricultural loss. This is a prioritization recommendation, not admission.

1. Prepare a descriptor candidate with official identity, exact distribution,
   current credit/terms, native polygon support, source/valid/publication/capture
   clocks, correction/successor rules and public-safe precision. Keep unresolved
   fields explicit; do not fill a rights enum from provider reputation. Resolve
   the classification-to-descriptor role mapping and admissibility limits:
   `classification` is not an allowed `source_role` in the current
   [schema](../../schemas/contracts/v1/source/source_descriptor.schema.json).
2. Validate its shape and the source-role/currentness negative paths. The
   [rights/currentness profile](../../contracts/source/source_rights_currentness_assessment.md)
   remains fixture-only: a PASS cannot authenticate a steward decision.
3. Obtain the attributable source-specific decision before live acquisition.
   The current review route is `@bartytime4life`; wider stewardship is unknown.
   Existing self-release exceptions in ADR-0044/45/46 apply only to their exact
   gate/profile/license scopes and do not cover a new USDM package.
4. After that decision, prepare a separately authorized same-candidate capture,
   package and API/UI/AI readback, including missing/conflict/stale/abstain,
   correction, withdrawal, consumer invalidation and a retained rollback target.
   No real snapshot or serving acceptance is established by this matrix.

Do not combine sources into a consequential claim until rights/sensitivity,
native spatial-temporal support, uncertainty and tuple-level evidence close.
The separate [ForecastProduct contract](../../contracts/common/forecast_product.md)
preserves prediction roles and future validity; a later outlook cannot refresh
an old observation. No current forecast or current-condition claim was assessed.

## Validation and maintenance

The three approved descriptor files pass their existing Hydrology, Atmosphere
and Soil validator entrypoints at the pinned source revision. The source
rights/currentness fixtures and existing multi-clock/forecast checks are distinct
bounded evidence; no live rights acceptance follows. Final document/hash checks
are recorded in the contribution receipt.

Recheck this matrix when product identity, terms, access, algorithms, source
heads or governing decisions change. Preserve prior captures and decisions.
Suspect corrections stop reuse at the affected consumer; disable further
acquisition through the owning operational control, trace dependent claims,
and use the governed correction/withdrawal/rollback path before restoring
service. No disable, activation or release operation is performed here.

This human source-review document belongs under `docs/sources/` by accepted
Directory Rules/ADR-0029. It creates no machine register, descriptor, contract,
policy or alternate source authority. Rollback is a focused documentation revert
or dated forward correction preserving historical receipts and source records.
