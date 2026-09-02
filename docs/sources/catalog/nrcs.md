<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/sources-catalog-nrcs
title: Natural Resources Conservation Service Source Catalog Profile
type: source_catalog_profile
version: v0.1
status: draft
owners: <PLACEHOLDER — Source steward · Docs steward · Catalog profile owner>
created: 2026-06-12
updated: 2026-06-12
policy_label: public
related:
  - docs/sources/catalog/README.md
  - docs/sources/catalog/CROSSWALKS.md
  - docs/sources/catalog/IDENTITY.md
  - docs/sources/catalog/GLOSSARY.md
  - docs/sources/catalog/OPEN-QUESTIONS.md
  - docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/truth-posture.md
  - docs/governance/separation-of-duties.md
  - schemas/contracts/v1/source/
tags: [kfm, sources, catalog, nrcs, usda, soils, ssurgo, gssurgo, statsgo, web-soil-survey, soil-data-access, ecological-sites, scan, snotel, conservation, agriculture, hydrology]
notes:
  - "v0.1 — Initial NRCS source catalog profile for governed KFM ingestion, evidence use, and public-release boundaries."
  - "This profile describes source use. It does not authorize direct public-client reads from NRCS or USDA systems."
  - "The legacy NRCS Geospatial Data Gateway is treated as deprecated after its March 31, 2026 decommissioning notice."
] -->

# Natural Resources Conservation Service Source Catalog Profile

Path: `docs/sources/catalog/nrcs.md`

## 1. Purpose

This document defines the Kansas Frontier Matrix (KFM) source-catalog profile for the **USDA Natural Resources Conservation Service (NRCS)**.

NRCS sources are foundational to KFM for soils, soil survey interpretation, farmland and rangeland suitability context, conservation planning references, ecological site descriptions, soil climate monitoring, snow and water supply data, and selected public geospatial resources. Within KFM, NRCS data must be treated as governed upstream source material that enters the KFM lifecycle through source descriptors, ingestion receipts, validation, EvidenceBundles, catalog records, triplets, graph records, tile products, and released artifacts.

This profile prevents NRCS material from becoming an ungoverned runtime dependency, a substitute for private landowner records, or a blanket authority for legal, regulatory, access, ownership, conservation-compliance, or farm-program claims.

## 2. Source identity

| Field | Value |
|---|---|
| Source family | Federal soil, conservation, ecological-site, agricultural-resource, and natural-resource data source |
| Steward organization | U.S. Department of Agriculture — Natural Resources Conservation Service |
| Common abbreviation | NRCS |
| KFM source profile id | `source-profile:nrcs` |
| Recommended source id prefix | `source:nrcs:` |
| Primary KFM domains | `sources`, `catalog`, `map`, `soils`, `agriculture`, `conservation`, `ecology`, `hydrology`, `climate`, `evidence` |
| Main access modes | Web Soil Survey, SSURGO Portal, Soil Data Access, gSSURGO downloads, NRCS data/report pages, Ecological Site Description tools, National Water and Climate Center systems, SCAN, SNOTEL, direct USDA/NRCS download paths |
| Deprecated access modes | Legacy NRCS Geospatial Data Gateway order workflow after decommissioning notice |
| Public-client access posture | Public clients may use only KFM released artifacts, governed APIs, tile services, and policy-safe runtime envelopes. They must not read NRCS raw endpoints directly. |

## 3. KFM authority posture

NRCS can be authoritative for records and datasets that NRCS publishes, maintains, or designates as official for its own programs. NRCS is not automatically authoritative for parcel ownership, tax status, legal access, public-road status, zoning, building permits, flood-insurance determinations, water rights, current landowner participation in USDA programs, tribal cultural-resource disclosure, or private conservation-plan contents.

### 3.1 Use NRCS as `primary` when

Use NRCS as a primary source only for NRCS-published records or datasets within NRCS authority, such as:

- Web Soil Survey soil data and soil interpretations produced by the National Cooperative Soil Survey.
- SSURGO soil survey spatial and tabular data.
- gSSURGO products derived from official SSURGO data.
- STATSGO2 or national/general soil map products when used at their intended scale.
- Soil Data Access responses when the request, query, and returned attributes are captured by a KFM receipt.
- Official soil map unit attributes, component data, ecological site links, and interpretive ratings where NRCS is the steward.
- Public NRCS Ecological Site Descriptions and associated classification records.
- NRCS Soil Climate Analysis Network records.
- NRCS Snow Survey and Water Supply Forecasting records, including SNOTEL and snow-course data, where relevant.
- NRCS conservation practice standards and public technical documents when cited as the standard or guidance record.

### 3.2 Use NRCS as `corroborating` when

Use NRCS as corroborating support when a KFM claim depends on another authority, including:

- County parcel ownership, tax, legal-description, or assessor claims.
- County road status, maintenance responsibility, or public access.
- Kansas water-rights, water-use, dam-safety, or water-quality regulation.
- FEMA flood-insurance or regulatory floodplain determinations.
- Local zoning, construction, septic, drainage, or land-use permitting.
- Wetland, highly erodible land, conservation-compliance, easement, or USDA program-participation claims requiring case-specific authority.
- Agricultural operation, producer, tenant, or landowner identity.
- Tribal, cultural-resource, burial, sacred, or archaeological claims.
- County Focus Mode claims involving access, ownership, regulatory status, or operational restrictions.

### 3.3 Use NRCS as `context` when

Use NRCS as contextual background when the record helps orient or interpret KFM but does not itself prove the final claim, including:

- Soil map context.
- Soil capability, limitation, suitability, productivity, and erosion context.
- Rangeland, pasture, forestland, ecological-site, and vegetation-state context.
- Watershed and conservation-planning context.
- Soil moisture, soil temperature, climate-station, snowpack, and water-supply context.
- Historic soil survey comparison.
- Broad conservation-practice or technical-standard background.
- Landscape interpretation in county Focus Mode.

### 3.4 Use NRCS as `restricted` or fail closed when

Treat NRCS-derived material as restricted or fail closed when it includes or implies:

- Private farm, ranch, producer, landowner, tenant, tract, or conservation-plan information.
- USDA program participation, eligibility, payment, compliance, contract, or application status.
- Farm-specific conservation practice locations that are not explicitly public.
- Wetland, highly erodible land, or compliance determinations tied to identifiable private property.
- Sensitive ecology, species, habitat, nesting, denning, cave, spring, rare plant, or collection-site locations.
- Archaeological, burial, sacred, tribal, or cultural-resource locations.
- Tribal SCAN or tribal-land monitoring context requiring extra review.
- Unreleased, draft, provisional, partner-restricted, or access-controlled records.
- Real-time or near-real-time climate, snow, or water records that could be dangerous if stale.
- Any geometry too coarse, generalized, or uncertain for the public claim being made.

## 4. Kansas relevance

KFM is Kansas-centered. NRCS is highly relevant to Kansas Focus Mode and statewide build work.

NRCS is especially relevant to Kansas for:

- County-level SSURGO soil survey packages.
- Soil map units, components, soil series, and interpretive soil properties.
- Prime farmland, farmland of statewide importance, land capability, hydric soils, drainage class, slope, erosion hazard, shrink-swell potential, pond/reservoir suitability, septic limitations, and agricultural suitability context.
- gSSURGO statewide soil products and map-unit summaries.
- Soil Data Access queries for AOI-specific spatial and tabular soil attributes.
- Ecological Site Descriptions for rangeland, grassland, pasture, and forestland interpretation.
- Soil climate and soil-moisture references where SCAN or related networks apply.
- Conservation practice standards and technical references.
- Historic and current soil survey interpretation for county Focus Mode.

NRCS should not be treated as a replacement for:

- Kansas county Register of Deeds records.
- County parcel GIS and assessor records.
- County road and bridge authorities.
- Kansas Department of Transportation road data where KDOT is the authority.
- Kansas Department of Agriculture regulatory records.
- Kansas water-rights, water-use, dam-safety, or drainage authorities.
- FEMA regulatory flood products.
- Local zoning, permitting, septic, drainage, or building officials.
- USDA Farm Service Agency program records.
- Private conservation plans or landowner records.
- Tribal, cultural-resource, or protected-site authorities.
- Field verification.

For Kansas county Focus Mode, NRCS usually serves one of these roles:

1. **Soils source** for SSURGO/gSSURGO map units, components, properties, interpretations, and farmland ratings.
2. **Ecological context source** for rangeland, pasture, forestland, and ecological site interpretation.
3. **Conservation-standard source** for public NRCS practice standards and technical references.
4. **Agricultural suitability context source** for soil limitations and land-use planning context.
5. **Hydrologic support source** for soil drainage, runoff, hydric soils, ponding, flooding-frequency, and watershed interpretation.
6. **Climate and monitoring context source** for SCAN, SNOTEL, snow survey, and water-supply data where applicable.

## 5. Canonical access points

The following access points are recognized by this profile. Their availability, service structure, layer names, formats, and metadata must be verified during each source refresh.

| Handle | Use | KFM treatment |
|---|---|---|
| `nrcs:web-soil-survey` | Web Soil Survey interface for official soil data, reports, maps, interpretations, and GIS downloads. | Prefer for human review, AOI definition, official citation, and governed SSURGO acquisition. |
| `nrcs:ssurgo` | Soil Survey Geographic Database products and documentation. | Use as primary source for detailed soil spatial and tabular data when within intended scale and coverage. |
| `nrcs:ssurgo-portal` | SSURGO Portal tooling for county packages and AOI-based SSURGO workflows. | Use for governed SSURGO preparation and package handling where appropriate. |
| `nrcs:gssurgo` | Gridded SSURGO statewide products derived from SSURGO. | Use for statewide and analysis-ready soil products; preserve derivative lineage and generalization notes. |
| `nrcs:statsgo2` | General Soil Map / STATSGO2 products. | Use for broad regional context only; do not substitute for SSURGO in county-scale claims. |
| `nrcs:soil-data-access` | Soil Data Access web services and applications. | Use for receipt-backed spatial/tabular queries. Public clients must not directly depend on raw live service calls. |
| `nrcs:ecological-site-descriptions` | NRCS Ecological Site Description pages, reports, and related tools. | Use for public ecological-site context and land-response interpretation with sensitive-data review. |
| `nrcs:edit` | Ecological Site Description access through EDIT-related tools where publicly available. | Use for ESD discovery and reference; capture access status and public availability. |
| `nrcs:national-ecological-site-handbook` | Standards and guidance for ESD development. | Use as public technical guidance, not as site-specific evidence unless linked to an ESD. |
| `nrcs:nwcc` | National Water and Climate Center systems. | Use for NRCS climate, snow, water, SCAN, SNOTEL, and forecasting records with staleness rules. |
| `nrcs:scan` | Soil Climate Analysis Network and Tribal SCAN references. | Use for station observations and soil-climate context; apply tribal/privacy/sensitivity review. |
| `nrcs:snotel` | Snow Telemetry and snow-course data. | Use for snowpack and water-supply context where relevant; enforce near-real-time staleness gates. |
| `nrcs:conservation-practice-standards` | Public conservation practice standards and technical documents. | Use as guidance/standard source; do not imply a private landowner has adopted a practice. |
| `nrcs:geospatial-data-gateway-legacy` | Legacy Geospatial Data Gateway discovery/order workflow. | Deprecated. Preserve in historical descriptors only; prefer current Web Soil Survey, Soil Data Access, SSURGO Portal, or replacement download paths. |

## 6. Example dataset families

NRCS publishes many datasets, services, reports, and technical documents. This profile does not whitelist every layer. It defines dataset families that can be considered by a KFM source steward.

| Dataset family | Example KFM use | Default source role | Risk posture |
|---|---|---:|---|
| Web Soil Survey reports and AOIs | Soil maps, soil interpretations, AOI reports, county Focus Mode soil evidence | `primary` for NRCS soil survey report content | Moderate; validate AOI, date, and interpretation scope |
| SSURGO | Detailed county-scale soil spatial and tabular data | `primary` for NRCS soil map units and attributes | High; scale, map-unit complexity, and interpretation limits matter |
| gSSURGO | Statewide soil raster/vector products and ready-to-map attributes | `primary` for NRCS gSSURGO product fields; `context` for derived analysis | High; derived/generalized summaries require lineage |
| STATSGO2 | Regional or statewide soil context | `context` or `corroborating` | High; too coarse for parcel/county feature claims |
| Soil Data Access | Query-backed soil attributes and spatial/tabular extracts | `primary` when query and response are receipted | High; query must be reproducible |
| Hydric soils / farmland ratings | Planning and environmental context | `primary` for NRCS soil interpretation; `corroborating` for regulatory claim | Very high; not a standalone legal determination |
| Erosion, slope, drainage, runoff, ponding, flooding-frequency attributes | Agricultural, conservation, terrain, and hydrologic context | `primary` for attribute content; `context` for interpretation | High; not a substitute for engineering analysis |
| Ecological Site Descriptions | Rangeland, grassland, forestland, plant community, and disturbance-response context | `primary` for public ESD record; `context` for site interpretation | Very high; sensitive ecology review required |
| Conservation practice standards | Public technical standard or design context | `primary` for standard text; `context` for applied local interpretation | High; does not prove implementation on land |
| SCAN | Soil moisture, soil temperature, and climate-station records | `primary` for station observations | High; near-real-time and station-placement caveats |
| Tribal SCAN | Soil-climate monitoring on tribal lands | `restricted` by default until steward review | Very high; tribal context requires extra care |
| SNOTEL / snow survey | Snowpack, snow water equivalent, precipitation, and water-supply context | `primary` for station/product records | High; staleness and western-region relevance |
| Snow and water supply forecasts | Forecast context for water management | `context` unless final authority is explicitly NRCS product | Very high; stale forecast risk |
| Geospatial replacement downloads | USDA/NRCS-supported public geospatial data formerly served through GDG | `primary`, `corroborating`, or `context` by dataset | High; access-path changes require receipts |

## 7. KFM lifecycle requirements

NRCS material must follow the KFM source lifecycle.

```text
RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET / GRAPH → PUBLISHED
```

### 7.1 RAW

RAW storage may contain Web Soil Survey exports, SSURGO packages, gSSURGO geodatabases, STATSGO2 products, Soil Data Access request/response payloads, ecological site reports, conservation practice standards, SCAN/SNOTEL observations, NWCC reports, metadata snapshots, or direct-download packages.

Requirements:

- Preserve original filenames, request URLs, timestamps, response headers when available, and checksums.
- Preserve Web Soil Survey AOI parameters and report settings.
- Preserve Soil Data Access query text, SQL, spatial filters, Shape commands, response payloads, and timestamps.
- Preserve SSURGO survey area, package date, fiscal-year refresh date, and tabular/spatial schema versions.
- Preserve gSSURGO state extent, raster/vector products, Valu1 table details, and derivative status.
- Preserve conservation practice standard version, state/national scope, effective date, and publication source.
- Preserve station identifiers, observation timestamps, units, and provisional status for SCAN/SNOTEL/NWCC data.
- Capture license/public-domain posture as a claim to verify, not an assumption.
- Store full metadata, documentation, and source citations where available.

### 7.2 WORK

WORK storage may contain normalized intermediate files, reprojections, county clips, AOI extracts, tabular joins, map-unit/component summaries, raster conversions, soil interpretation outputs, ESD crosswalks, station joins, QA outputs, and draft EvidenceBundle mappings.

Requirements:

- Do not publish WORK outputs.
- Mark all transformations clearly: clip, merge, dissolve, rasterize, vectorize, reproject, aggregate, component-weight, join, summarize, interpolate, query, classify, or threshold.
- Keep NRCS original identifiers alongside KFM local identifiers.
- Track lossy transformations, map-unit aggregation, weighted averaging, generalization, and derived products.
- Quarantine uncertain, sensitive, stale, private, or unclear-authority records.

### 7.3 QUARANTINE

Quarantine NRCS-derived material when:

- Metadata is missing or contradictory.
- SSURGO package date, annual refresh status, or AOI parameters are unknown.
- Soil Data Access query text or spatial filter is not receipted.
- A record appears public but contains protected, private, or review-required information.
- A record’s public display could reveal sensitive ecology, caves, archaeological, tribal, burial, sacred, or security information.
- A record implies private USDA program participation, conservation-plan location, compliance status, payment, or application status.
- Near-real-time climate, snow, or water records are stale, preliminary, or operationally risky.
- Geometry or raster resolution is too coarse or generalized for the intended KFM claim.
- STATSGO2 is being used for parcel/county-scale conclusions.
- Soil interpretations are being treated as legal determinations without corroborating authority.
- Dataset authority overlaps with county, state, tribal, municipal, or private records.

### 7.4 PROCESSED

Processed NRCS-derived datasets must include:

- Normalized schema.
- KFM source descriptor.
- EvidenceBundle linkage.
- Policy classification.
- Transform receipt.
- QA report.
- Geometry, raster, or tabular validation report.
- Attribution statement.
- Update cadence.
- Staleness rule.
- Confidence and source-role labels.
- Scale, interpretation, and uncertainty notes.
- Derived-product lineage if KFM creates new rasters, vectors, ratings, or summaries.
- AOI/query reproducibility receipts for WSS/SDA-derived outputs.

### 7.5 CATALOG / TRIPLET / GRAPH

Only processed, validated, policy-labeled records may produce:

- Catalog records.
- Entity records.
- Spatial feature records.
- Soil map-unit records.
- Soil component records.
- Soil interpretation records.
- Ecological-site records.
- Station observation references.
- Time-series references.
- Conservation-standard references.
- Triplets.
- Graph edges.
- Tile-build inputs.
- Public API payload candidates.

Triplets and graph records must never claim more authority than the NRCS source supports.

### 7.6 PUBLISHED

Publication is a governed state transition. An NRCS-derived artifact may be published only after:

- Source descriptor exists.
- EvidenceBundle exists.
- Policy label is assigned.
- Sensitive-data review is complete.
- Attribution is present.
- Update/staleness rule is defined.
- Scale and interpretation warnings are attached where needed.
- Public API or tile envelope is generated from released KFM artifacts.
- Public-client runtime cannot bypass KFM and read RAW, WORK, QUARANTINE, canonical internal stores, or live NRCS endpoints directly.

## 8. Source descriptor baseline

Use this as the starting point for a source descriptor. Adjust fields to match the current `source_descriptor` schema.

```yaml
id: source:nrcs
title: Natural Resources Conservation Service
short_title: NRCS
source_profile: source-profile:nrcs
agency:
  name: Natural Resources Conservation Service
  parent: U.S. Department of Agriculture
source_type: federal_soils_conservation_ecological_and_agricultural_resource_source
default_role: primary
role_guidance:
  primary:
    - NRCS-published records and datasets within NRCS authority.
    - Web Soil Survey, SSURGO, gSSURGO, Soil Data Access, public Ecological Site Descriptions, SCAN, SNOTEL, and public conservation practice standards when used within stated scope.
  corroborating:
    - Parcel, road, zoning, regulatory, floodplain, water-rights, conservation-compliance, program-participation, or private-land claims requiring another authority.
    - Kansas county Focus Mode claims where NRCS is not the final authority.
  context:
    - Soil capability, agricultural suitability, ecological site, conservation, hydrologic soil, soil climate, snow, and water-supply context.
  restricted:
    - Private farm, ranch, producer, tract, conservation-plan, USDA program, compliance, sensitive ecology, tribal, burial, sacred, archaeology, security, embargoed, draft, or access-controlled data.
jurisdiction:
  country: US
  focus_region: Kansas and national NRCS coverage relevant to KFM
access:
  handles:
    - nrcs:web-soil-survey
    - nrcs:ssurgo
    - nrcs:ssurgo-portal
    - nrcs:gssurgo
    - nrcs:statsgo2
    - nrcs:soil-data-access
    - nrcs:ecological-site-descriptions
    - nrcs:edit
    - nrcs:national-ecological-site-handbook
    - nrcs:nwcc
    - nrcs:scan
    - nrcs:snotel
    - nrcs:conservation-practice-standards
    - nrcs:geospatial-data-gateway-legacy
policy:
  public_client_direct_read: false
  cite_or_abstain: true
  sensitive_topics_fail_closed: true
  private_landowner_data_fail_closed: true
  tribal_context_extra_review: true
  publication_requires_evidence_bundle: true
  publication_requires_policy_review: true
refresh:
  default_cadence: annually_or_quarterly_by_dataset
  high_volatility_cadence: monthly_daily_hourly_or_event_driven
  stale_after_days: 120
quality:
  require_metadata_snapshot: true
  require_checksum: true
  require_geometry_raster_or_tabular_validation: true
  require_schema_crosswalk: true
  require_attribution: true
  require_scale_warning: true
  require_query_receipt_for_soil_data_access: true
```

## 9. Dataset-level descriptor extension

Each NRCS dataset, service, report family, station network, practice standard, ecological site record, or soil survey extract should receive its own dataset-level descriptor. Do not rely on this profile alone.

Recommended id pattern:

```text
source:nrcs:<program-or-theme>:<dataset-or-layer-slug>
```

Examples:

```text
source:nrcs:soils:web-soil-survey-aoi
source:nrcs:soils:ssurgo-county-package
source:nrcs:soils:gssurgo-kansas
source:nrcs:soils:statsgo2
source:nrcs:soils:soil-data-access-query
source:nrcs:ecology:ecological-site-description
source:nrcs:ecology:edit-report
source:nrcs:climate:scan-stations
source:nrcs:climate:tribal-scan
source:nrcs:snow:snotel-stations
source:nrcs:water:nwcc-forecast
source:nrcs:standards:conservation-practice-standard
```

Minimum dataset-level fields:

```yaml
id: source:nrcs:<theme>:<dataset>
parent_profile: source-profile:nrcs
title: <official dataset, report, service, standard, network, or product title>
source_role: <primary|corroborating|context|restricted>
source_handle: <nrcs:web-soil-survey|nrcs:ssurgo|nrcs:soil-data-access|...>
accessed_at: <ISO-8601 timestamp>
source_landing_page: <URL or registry pointer>
service_endpoint: <URL or registry pointer>
metadata_endpoint: <URL or registry pointer>
download_endpoint: <URL or registry pointer>
survey_area_symbol: <SSURGO survey area symbol when applicable>
fiscal_year_or_refresh_date: <date or unknown>
aoi_id: <KFM AOI id when applicable>
query_receipt_id: <KFM query receipt id when applicable>
station_id: <SCAN/SNOTEL/NWCC station id when applicable>
practice_code: <NRCS practice code when applicable>
standard_scope: <national|state|local|unknown>
spatial_coverage: <national|state|county|survey-area|aoi|station|custom geometry>
temporal_coverage: <as stated by source>
product_date: <date or unknown>
publication_date: <date or unknown>
update_frequency: <as stated by source or unknown>
license_or_use_statement: <as stated by source>
public_release_review:
  required: true
  status: pending
sensitive_data_review:
  required: true
  status: pending
privacy_review:
  required: true
  status: pending
geometry_raster_or_tabular_policy:
  may_tile_publicly: false
  requires_simplification_review: true
  requires_scale_warning: true
  requires_derivative_lineage: true
evidence:
  evidence_bundle_id: <KFM EvidenceBundle id>
  receipt_id: <KFM receipt id>
```

## 10. Identity and crosswalk policy

NRCS identifiers must be preserved. KFM identifiers must be deterministic and separate.

### 10.1 Preserve source identifiers

Preserve source fields such as:

- Dataset title.
- NRCS program name.
- Web Soil Survey AOI identifier or KFM-generated AOI receipt.
- SSURGO survey area symbol.
- Soil map unit key, symbol, and name.
- Soil component key and component name.
- Soil series name.
- Horizon identifiers where applicable.
- Interpretation rating class, rating value, rule name, and report name.
- Soil Data Access query text, schema, selected tables, fields, spatial filters, and response id.
- gSSURGO product, state, refresh year, Valu1 fields, raster layer name, and map-unit key.
- Ecological site id, ecological site name, MLRA, LRU, state, and publication/status fields.
- Conservation practice code, name, standard date, state/national scope, and document version.
- SCAN, Tribal SCAN, SNOTEL, snow course, or NWCC station id.
- Observation timestamp, unit, parameter code/name, and provisional/status fields.
- Product date, publication date, accessed timestamp, CRS, resolution, scale, and processing level.

### 10.2 Create KFM identifiers

KFM identifiers should be generated deterministically from source and geometry/record fields.

Recommended pattern:

```text
kfm:feature:nrcs:<theme>:<normalized-source-key>
kfm:record:nrcs:<record-family>:<normalized-source-key>
kfm:soil:nrcs:<survey-area>:<mapunit-or-component-key>
kfm:ecosite:nrcs:<ecological-site-id>
kfm:standard:nrcs:<practice-code>:<version-or-date>
kfm:observation:nrcs:<station-id>:<timestamp-or-record-key>
kfm:evidence:nrcs:<dataset>:<receipt-hash>
```

### 10.3 Crosswalk requirements

Create or update crosswalk records when NRCS data connects to:

- County parcels.
- County road centerlines.
- Kansas state agency records.
- Kansas water-rights, dam-safety, environmental, or conservation records.
- FEMA flood data.
- USGS hydrography, elevation, and water observation records.
- USDA FSA public aggregate datasets.
- USDA NASS agricultural statistics.
- EPA water-quality records.
- BLM PLSS and land-status data.
- Ecological, habitat, or conservation layers.
- KFM Focus Mode county entities.
- KFM EvidenceBundle records.

Crosswalks must include directionality and authority posture.

Example:

```yaml
crosswalk_id: crosswalk:nrcs-ssurgo:kfm-county-soils:<hash>
from:
  source: source:nrcs:soils:ssurgo-county-package
  key: <SSURGO survey area symbol + map unit key>
to:
  source: kfm:county-focus:<county>
  key: <KFM county soil feature id>
relationship: same_or_related_soil_map_unit_area
authority_posture: NRCS is soil survey reference; county, state, FEMA, water-rights, or field records may govern legal, regulatory, access, or operational claims.
confidence: <low|medium|high>
evidence_bundle_id: <EvidenceBundle id>
```

## 11. EvidenceBundle mapping

Every NRCS-derived public claim must point to an EvidenceBundle.

Minimum EvidenceBundle fields for NRCS material:

```yaml
evidence_bundle_id: evidence:nrcs:<dataset>:<hash>
claim:
  text: <precise claim supported by NRCS source>
  scope: <geometry|record|attribute|interpretation|observation|time-series|raster|relationship|context|standard>
source:
  source_id: source:nrcs:<theme>:<dataset>
  source_profile: source-profile:nrcs
  source_role: <primary|corroborating|context|restricted>
  accessed_at: <ISO-8601 timestamp>
  source_title: <official source title>
  source_steward: Natural Resources Conservation Service
  source_handle: <handle>
lineage:
  raw_receipt_id: <receipt id>
  query_receipt_id: <receipt id if WSS/SDA query or AOI is used>
  transform_receipt_id: <receipt id>
  validation_receipt_id: <receipt id>
  derivative_receipt_id: <receipt id if KFM derived a new raster/vector/rating/summary>
policy:
  public_release: <allowed|denied|requires_review>
  sensitive_review: <passed|failed|pending>
  privacy_review: <passed|failed|pending>
  tribal_review: <not_applicable|passed|failed|pending>
  redaction: <none|generalized|suppressed|withheld>
quality:
  geometry_valid: <true|false|unknown|not_applicable>
  raster_valid: <true|false|unknown|not_applicable>
  tabular_valid: <true|false|unknown|not_applicable>
  metadata_complete: <true|false|unknown>
  source_date: <date or unknown>
  stale_after: <date or rule>
  scale_or_resolution: <value or unknown>
  interpretation_scope: <soil_map_unit|component|horizon|site|station|standard|unknown>
  preliminary_or_provisional: <true|false|unknown>
```

## 12. Public API and tile policy

Public KFM clients may display NRCS-derived information only through KFM-governed outputs.

Allowed public surfaces:

- KFM public API records.
- KFM released vector tiles.
- KFM released raster tiles.
- KFM released static exports.
- KFM EvidenceDrawer payloads.
- KFM source-card summaries.
- KFM attribution and provenance panels.
- KFM soil interpretation summaries derived from released KFM records.
- KFM ecological-site summaries derived from public, reviewed records.
- KFM station/time-series summaries derived from released KFM records.

Prohibited public surfaces:

- Direct calls from the public UI to live NRCS or USDA raw endpoints.
- Direct calls from the public UI to Web Soil Survey, Soil Data Access, SSURGO Portal, NWCC, SCAN, SNOTEL, or legacy GDG endpoints.
- Direct calls from the public UI to live near-real-time station or forecast endpoints without KFM staleness and warning gates.
- Direct exposure of RAW, WORK, QUARANTINE, or internal canonical stores.
- Direct display of unreleased candidate layers.
- Runtime AI claims derived from NRCS content without EvidenceBundle support.
- Public display of sensitive site locations, private conservation-plan details, farm-program participation, or protected resource data.

## 13. Ingestion checklist

Before acquiring an NRCS dataset:

- [ ] Identify the NRCS source handle.
- [ ] Confirm source page, service endpoint, repository item, report, standard, station, or download endpoint.
- [ ] Confirm dataset title and steward.
- [ ] Confirm whether the dataset is public, reviewed public, provisional, restricted, private, or access controlled.
- [ ] Capture metadata and service/report description.
- [ ] Capture access timestamp.
- [ ] Capture checksums for downloaded files.
- [ ] Confirm geometry type, raster type, tabular schema, CRS, scale, resolution, and generalization.
- [ ] Confirm product date, publication date, annual refresh date, and update cadence or mark as unknown.
- [ ] Capture AOI definition or Soil Data Access query when applicable.
- [ ] Assign preliminary KFM source role.
- [ ] Assign preliminary policy label.
- [ ] Decide whether the data is suitable for county Focus Mode.
- [ ] Decide whether sensitive-data, privacy, or tribal review is required.
- [ ] Create or update dataset-level source descriptor.

During processing:

- [ ] Reproject to KFM standard CRS if required.
- [ ] Validate geometries, raster integrity, and tabular joins.
- [ ] Normalize attributes.
- [ ] Preserve NRCS source identifiers.
- [ ] Generate deterministic KFM identifiers.
- [ ] Produce transform receipt.
- [ ] Produce QA report.
- [ ] Produce schema crosswalk.
- [ ] Produce EvidenceBundle candidates.
- [ ] Record all derived-product steps.
- [ ] Record query reproducibility for Web Soil Survey and Soil Data Access outputs.
- [ ] Quarantine sensitive, private, stale, preliminary, or ambiguous records.

Before publication:

- [ ] Confirm EvidenceBundle exists.
- [ ] Confirm source descriptor is current.
- [ ] Confirm policy review passed.
- [ ] Confirm sensitive-data review passed.
- [ ] Confirm privacy review passed.
- [ ] Confirm tribal review passed or is not applicable.
- [ ] Confirm attribution text exists.
- [ ] Confirm source-role label is visible.
- [ ] Confirm stale-after rule exists.
- [ ] Confirm scale/resolution/interpretation warning exists where needed.
- [ ] Confirm public output does not bypass KFM.
- [ ] Confirm public UI displays uncertainty, preliminary, and staleness warnings where needed.
- [ ] Confirm no private conservation, farm, ranch, tract, producer, or program-participation claim is exposed.

## 14. Validation rules

### 14.1 Metadata validation

Reject or quarantine if:

- No source title exists.
- No steward can be identified.
- No accessed timestamp exists.
- No source endpoint, landing page, report id, standard id, station id, service id, or product id is recorded.
- No policy posture is assigned.
- No source-role label is assigned.
- No EvidenceBundle can be produced.
- Dataset vintage is unknown and the public claim depends on recency.
- Product resolution, scale, mapping level, or interpretation scope is unknown and the public claim depends on precision.
- Soil Data Access query text, AOI geometry, selected fields, or response payload is missing.
- SSURGO package date or annual refresh status is missing.

### 14.2 Geometry validation

Validate:

- CRS and reprojection.
- Geometry type.
- Null geometries.
- Invalid rings or self-intersections.
- Multipart handling.
- Slivers after clipping.
- Dissolve effects.
- Simplification effects.
- Soil map-unit topology.
- County-boundary clipping.
- Tile-scale visibility.
- Alignment against appropriate local, state, USGS, or USDA reference layers.
- Station placement where station-level claims are shown.

Do not overstate geometry precision. Soil map units are interpretive mapping units, not parcel boundaries, site surveys, or engineering drawings.

### 14.3 Raster validation

Validate:

- CRS and pixel resolution.
- NoData values.
- Data type.
- Tile boundaries.
- Rasterization method.
- Mosaicking effects.
- Resampling method.
- Map-unit key linkage.
- Value table linkage.
- gSSURGO Valu1 field mapping.
- Source product and derivative lineage.
- Raster clipping and compression effects.
- Suitability for public tile display.

### 14.4 Tabular validation

Validate:

- Required identifiers.
- Null or unknown values.
- Domain values.
- Map-unit/component/horizon joins.
- Interpretation rating classes and units.
- Aggregation rules and component weighting.
- Date and timestamp fields.
- Station parameters and units.
- Preliminary/provisional indicators.
- Access or use constraints.
- Table-name-to-schema mapping.
- Product-level metadata and citation fields.

### 14.5 Authority validation

Ask:

- Is NRCS the authority for this claim?
- Is another federal, state, tribal, county, municipal, conservation-district, or private source more authoritative?
- Is the claim soil survey, ecological, conservation technical guidance, hydrologic context, legal, regulatory, operational, historical, or interpretive?
- Does the public display imply a right of access?
- Does the display imply ownership, USDA program participation, compliance status, or conservation-plan contents?
- Does the display imply legal wetland, floodplain, or highly erodible land determination?
- Does the display create risk for sensitive resources or private property?
- Does the scale, map-unit concept, or interpretation rating support the intended use?
- Is the data preliminary, provisional, near-real-time, stale, or tied to a private record?
- Is KFM deriving an interpretation that must be labeled separately from the NRCS source?

## 15. Redaction and generalization rules

NRCS-derived records must follow KFM sensitive-topic and private-land rules.

Default redaction posture:

| Topic | Default action |
|---|---|
| Private farm, ranch, tract, producer, tenant, or landowner information | Withhold |
| Conservation-plan or practice-location details tied to private land | Withhold unless explicitly public and reviewed |
| USDA program participation, eligibility, payment, contract, or compliance status | Withhold |
| Wetland or highly erodible land determinations tied to identifiable private property | Withhold or require steward/legal review |
| Archaeological sites | Withhold or aggregate; do not publish precise locations |
| Burial or sacred sites | Withhold; tribal and legal review required |
| Tribal cultural resources | Withhold unless explicit public-release authority exists |
| Tribal SCAN or tribal-land monitoring context | Require tribal/privacy review |
| Sensitive species, habitat, nest, den, cave, spring, rare plant, or collection site | Generalize, aggregate, or withhold |
| Private wells or household-sensitive sampling context | Generalize, suppress, or require steward review |
| Law enforcement or emergency operations | Withhold operational detail |
| Infrastructure vulnerability | Withhold or generalize |
| Real-time snow, climate, water, or forecast data | Publish only with KFM staleness and warning gates |
| Unverified access implication | Mark as unverified; do not route users |
| Generalized soil, ecological-site, or conservation boundary | Display with scale or interpretation warning |
| Historic soil surveys | Display with date and interpretation warning |

## 16. Attribution baseline

Public KFM products using NRCS-derived data must include attribution.

Recommended baseline:

```text
Contains information derived from public Natural Resources Conservation Service (NRCS), U.S. Department of Agriculture, datasets or records. KFM processing, normalization, filtering, generalization, derivation, and presentation are governed KFM outputs and should not be interpreted as direct NRCS publication.
```

For maps:

```text
Source: USDA Natural Resources Conservation Service (NRCS). Processed by Kansas Frontier Matrix. See EvidenceBundle for source, access date, processing receipt, query/AOI receipt, derivative lineage, and public-release policy.
```

For EvidenceDrawer:

```text
NRCS source role: <primary|corroborating|context|restricted>. Authority scope: <scope>. Accessed: <date>. KFM receipt: <receipt id>.
```

For soil survey citations, use the official NRCS/Web Soil Survey citation pattern where required by the dataset descriptor.

## 17. Refresh and staleness policy

Default cadence:

| Dataset type | Suggested refresh |
|---|---:|
| Web Soil Survey AOI reports | On generation and before publication |
| SSURGO county packages | Annually after NRCS refresh, and before publication |
| gSSURGO statewide products | Annually after NRCS refresh, and before publication |
| STATSGO2 | Annual or on release cycle |
| Soil Data Access queries | On query execution and before publication |
| Ecological Site Descriptions | Quarterly or before publication |
| Conservation practice standards | Quarterly or before use in a build plan |
| SCAN station metadata | Monthly or on source update |
| SCAN observations | Daily, hourly, or event-driven if publicly displayed |
| Tribal SCAN | Manual steward review before any public use |
| SNOTEL station metadata | Monthly or on source update |
| SNOTEL and snow-course observations | Daily, hourly, or event-driven if publicly displayed |
| Snow and water supply forecasts | Event-driven; strict stale warning required |
| Legacy Geospatial Data Gateway references | Do not refresh as active source; migrate descriptors |
| Service metadata snapshots | Every acquisition and before publication |

Default stale-after rule:

```yaml
stale_after_days: 120
```

Override to shorter windows for station observations, snowpack, forecasts, climate records, water-supply products, public safety, and operationally sensitive data.

For SSURGO and gSSURGO, prefer an annual refresh rule tied to NRCS annual soils refresh rather than a generic stale-after value.

## 18. Failure modes

Known NRCS-source failure modes for KFM:

| Failure mode | KFM response |
|---|---|
| Legacy Geospatial Data Gateway endpoint is used as active source after decommissioning | Migrate descriptor to current access path; preserve legacy handle only for historical lineage |
| Web Soil Survey AOI is missing or not reproducible | Quarantine until AOI receipt exists |
| Soil Data Access query is not captured | Quarantine until query receipt exists |
| SSURGO map unit treated as parcel boundary | Correct source role; require parcel/local authority |
| SSURGO interpretation treated as legal wetland, HEL, or regulatory determination | Correct claim scope; require official determination authority |
| STATSGO2 used for county-scale or parcel-scale decision | Quarantine or relabel as broad context |
| gSSURGO Valu1 summary used without explaining generalization | Add derivative/generalization warning or quarantine |
| Soil property used for engineering design without site investigation | Add limitation warning; require engineering authority |
| Conservation practice standard used to imply a practice exists on private land | Suppress implementation claim unless independently evidenced and public |
| Farm/program/compliance/private plan data appears in source material | Withhold and quarantine |
| Ecological site data exposes sensitive habitat/species | Generalize, aggregate, or withhold |
| Tribal SCAN data used without extra review | Quarantine pending tribal/privacy review |
| Near-real-time climate/snow/water data becomes stale | Suppress or mark stale; do not present as current |
| Missing metadata | Quarantine until resolved |
| Conflicting NRCS and county/state records | Create conflict record; do not publish resolved claim without steward review |
| Runtime AI generates unsupported NRCS claim | Suppress or mark unsupported; cite-or-abstain |

## 19. Open questions

- Which NRCS dataset families should be promoted to explicit KFM whitelisted dataset descriptors?
- Should KFM maintain a statewide Kansas SSURGO/gSSURGO mirror, or acquire per Focus Mode build?
- Which Kansas county Focus Mode plans require SSURGO, gSSURGO, ecological-site, and conservation-practice extracts by default?
- What is the canonical KFM CRS for all NRCS-derived vector and raster processing?
- What scale or map-unit warning should be required before public display of NRCS soil boundaries?
- Which NRCS data families require automatic sensitive-resource quarantine?
- How should KFM distinguish NRCS source interpretations from KFM-derived summaries?
- Should Soil Data Access query receipts be stored as first-class KFM artifacts?
- Should NRCS annual soils refresh become a scheduled KFM source-steward task?
- How should KFM represent conservation practice standards without implying private-land implementation?
- What redaction threshold should apply to Tribal SCAN and tribal-land ecological context?
- How should KFM migrate any existing GDG descriptors after GDG decommissioning?

## 20. Steward review checklist

A source steward should review this file when:

- NRCS changes a relevant access point.
- KFM adds a new NRCS dataset family.
- KFM updates the source descriptor schema.
- KFM changes public API or tile publication policy.
- A county Focus Mode plan depends on NRCS data.
- A sensitive-data, privacy, or tribal-data incident or near miss occurs.
- NRCS metadata conflicts with another authority.
- KFM adds soil, ecological-site, conservation, SCAN, SNOTEL, snow, water-supply, or agricultural suitability features.
- KFM changes raster derivative, soil interpretation, tabular aggregation, or tile-building rules.
- NRCS announces annual soils refresh or new access-path modernization.

## 21. Minimal publication rule

An NRCS-derived KFM record may be public only when this rule passes:

```text
Public = released KFM artifact
       + EvidenceBundle
       + source descriptor
       + source role
       + policy label
       + sensitive review
       + privacy review
       + tribal review when applicable
       + attribution
       + staleness rule
       + scale/interpretation warning when needed
       + AOI/query receipt when WSS/SDA is used
       + derivative lineage when KFM derived a product
       + no direct RAW/WORK/QUARANTINE/live-endpoint dependency
       + no private conservation/farm/program/compliance disclosure
```

If any term is missing, the record is not publishable.

## 22. Implementation note

This profile is intentionally conservative. It does not reduce the value of NRCS data. It protects KFM from making legal, regulatory, ownership, access, conservation-compliance, ecological, cultural, private-land, or operational claims that the source does not support.

NRCS data should enter KFM as evidence-bearing source material, not as sovereign runtime truth. KFM outputs must remain governed, cited, reviewable, time-aware, reversible, private-land-safe, and policy-safe.
