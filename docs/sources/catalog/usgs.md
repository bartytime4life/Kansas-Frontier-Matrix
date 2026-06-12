<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/sources-catalog-usgs
title: U.S. Geological Survey Source Catalog Profile
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
tags: [kfm, sources, catalog, usgs, doi, federal, geospatial, national-map, nhd, wbd, 3dep, gnis, water-data, nwis, sciencebase, landsat, hazards, topography]
notes:
  - "v0.1 — Initial USGS source catalog profile for governed KFM ingestion, evidence use, and public-release boundaries."
  - "This profile describes source use. It does not authorize direct public-client reads from USGS systems."
] -->

# U.S. Geological Survey Source Catalog Profile

Path: `docs/sources/catalog/usgs.md`

## 1. Purpose

This document defines the Kansas Frontier Matrix (KFM) source-catalog profile for the **U.S. Geological Survey (USGS)**.

USGS sources are foundational to KFM for national base mapping, hydrography, elevation, geographic names, topographic maps, water observations, remote sensing, geology, hazards, and public scientific data releases. Within KFM, USGS data must be treated as governed upstream source material that enters the KFM lifecycle through source descriptors, ingestion receipts, validation, EvidenceBundles, catalog records, triplets, graph records, tile products, and released artifacts.

This profile prevents USGS material from becoming an ungoverned runtime dependency or a blanket substitute for local, state, tribal, county, or field-verified authority.

## 2. Source identity

| Field | Value |
|---|---|
| Source family | Federal earth-science, geospatial, hydrologic, topographic, and hazards source |
| Steward organization | U.S. Department of the Interior — U.S. Geological Survey |
| Common abbreviation | USGS |
| KFM source profile id | `source-profile:usgs` |
| Recommended source id prefix | `source:usgs:` |
| Primary KFM domains | `sources`, `catalog`, `map`, `hydrography`, `elevation`, `geology`, `names`, `hazards`, `remote-sensing`, `evidence` |
| Main access modes | The National Map, USGS data catalogs, USGS web services, ScienceBase, Water Data for the Nation, National Water Information System, EarthExplorer, GNIS, public downloads |
| Public-client access posture | Public clients may use only KFM released artifacts, governed APIs, tile services, and policy-safe runtime envelopes. They must not read USGS raw endpoints directly. |

## 3. KFM authority posture

USGS can be authoritative for records and datasets that USGS publishes, maintains, or designates as official for its own programs. USGS is not automatically authoritative for property ownership, legal access, road status, zoning, local emergency orders, county parcel boundaries, public-health guidance, tribal cultural-resource disclosure, or site-specific engineering decisions.

### 3.1 Use USGS as `primary` when

Use USGS as a primary source only for USGS-published records or datasets within USGS authority, such as:

- USGS topographic base-layer products from The National Map.
- USGS 3D Elevation Program elevation products and related lidar-derived products.
- USGS National Hydrography Dataset, Watershed Boundary Dataset, and related national hydrography products.
- USGS Geographic Names Information System records for federally recognized domestic geographic names.
- USGS Water Data for the Nation and National Water Information System site and observation records.
- USGS ScienceBase data releases when the release is the cited repository record.
- USGS Landsat archive records and USGS-provided Landsat products.
- USGS earthquake and natural-hazard event feeds when used within the stated event/product scope.
- USGS geologic maps, mineral-resource products, and public scientific data releases where USGS is the steward.

### 3.2 Use USGS as `corroborating` when

Use USGS as corroborating support when a KFM claim depends on another authority, including:

- County parcel ownership or tax records.
- County road status and maintenance responsibility.
- Local zoning, permitting, or land-use restrictions.
- FEMA flood-insurance or regulatory floodplain determinations.
- State water-rights, water-quality, or water-use regulation.
- State geology, environmental, wildlife, or conservation rules.
- Local emergency operations, road closures, evacuations, or hazard orders.
- Archaeological, burial, sacred, tribal, or cultural-resource claims.
- County Focus Mode claims involving access, ownership, or operational restrictions.

### 3.3 Use USGS as `context` when

Use USGS as contextual background when the record helps orient KFM but does not itself prove the final claim, including:

- Topographic basemap context.
- Elevation-derived terrain interpretation.
- Hydrographic context for watersheds, drainage, streams, and lakes.
- GNIS names used for search, labeling, or map orientation.
- Historic topographic-map comparison.
- Landsat-derived regional landscape context.
- Broad geologic, hydrologic, or hazard context.
- National-scale datasets clipped to Kansas counties for map background.

### 3.4 Use USGS as `restricted` or fail closed when

Treat USGS-derived material as restricted or fail closed when it includes or implies:

- Sensitive ecology, species, habitat, nesting, denning, cave, spring, or collection-site locations.
- Archaeological, burial, sacred, tribal, or cultural-resource locations.
- Vulnerable infrastructure, critical facilities, or operational public-safety details.
- Private well information, personally sensitive sampling context, or data that could reveal private household conditions.
- Unreleased, embargoed, provisional, draft, partner-restricted, or access-controlled ScienceBase items.
- Real-time or near-real-time hazard records that could be dangerous if stale.
- Any record marked with review, distribution, access, or use constraints that require KFM steward review.
- Any geometry too coarse, generalized, or uncertain for the public claim being made.

## 4. Kansas relevance

KFM is Kansas-centered. USGS is highly relevant to Kansas Focus Mode and statewide build work.

USGS is especially relevant to Kansas for:

- Streams, rivers, lakes, reservoirs, wetlands, watersheds, and drainage references.
- National Hydrography Dataset and Watershed Boundary Dataset layers.
- USGS streamgage, groundwater, spring, water-quality, and observation-site records.
- Elevation, slope, relief, lidar, DEMs, and terrain derivatives from 3DEP.
- USGS topographic maps and The National Map base layers.
- GNIS names for communities, physical features, hydrographic features, and named places.
- Landsat and remote-sensing context for land-cover, temporal change, and landscape interpretation.
- Geologic, mineral, earthquake, landslide, and natural-hazard context.
- Historic topographic maps for settlement, landscape, route, and hydrology comparison.

USGS should not be treated as a replacement for:

- Kansas county Register of Deeds records.
- County parcel GIS and assessor records.
- County road and bridge authorities.
- Kansas Department of Transportation road data where KDOT is the authority.
- Kansas water-rights, water-use, or regulatory records.
- FEMA regulatory flood products.
- Local emergency management notices.
- Tribal, cultural-resource, or protected-site authorities.
- Field verification.

For Kansas county Focus Mode, USGS usually serves one of these roles:

1. **Base-map and terrain source** for elevation, contours, topographic features, and map context.
2. **Hydrography source** for streams, lakes, watersheds, drainage, and named water features.
3. **Observation source** for USGS water monitoring sites and historical measurements.
4. **Name authority source** for federally recognized geographic names.
5. **Scientific context source** for geology, remote sensing, and natural hazards.
6. **Historic comparison source** for topographic maps and landform/watercourse interpretation.

## 5. Canonical access points

The following access points are recognized by this profile. Their availability, service structure, layer names, formats, and metadata must be verified during each source refresh.

| Handle | Use | KFM treatment |
|---|---|---|
| `usgs:the-national-map` | National base-layer GIS data, topographic maps, map viewing, and downloads. | Prefer for national base layers, topographic context, elevation access paths, and map products. |
| `usgs:tnm-downloader` | Search and download interface for The National Map data. | Use for governed acquisition of base-layer GIS, elevation, hydrography, boundaries, structures, transportation, and map products where applicable. |
| `usgs:tnm-services` | USGS National Map web services and service metadata. | Use for metadata and governed ingestion. Public clients must not directly depend on raw live services. |
| `usgs:3dep` | 3D Elevation Program lidar and DEM products. | Use for elevation, lidar, DEM, slope, relief, and terrain derivatives after QA and scale review. |
| `usgs:nhd` | National Hydrography Dataset. | Use for hydrographic features, stream reaches, lakes, reservoirs, and drainage network context. |
| `usgs:wbd` | Watershed Boundary Dataset. | Use for hydrologic unit boundaries and watershed context. |
| `usgs:nhdplus-hr` | NHDPlus High Resolution products. | Use for high-resolution hydrologic network context and analysis-ready derivatives when appropriate. |
| `usgs:gnis` | Geographic Names Information System. | Use for official domestic geographic-name records and map-label/name search support. |
| `usgs:waterdata` | Water Data for the Nation. | Use for current and historical USGS water observations and station records. |
| `usgs:nwis` | National Water Information System and NWIS Mapper. | Use for surface-water, groundwater, spring, atmospheric, site, measurement, and historical water data references. |
| `usgs:sciencebase` | ScienceBase data releases and repository records. | Use for public USGS scientific data releases, metadata, files, and citations. |
| `usgs:earthexplorer` | EarthExplorer and remote-sensing product access. | Use for Landsat, aerial photography, cartographic products, and remote-sensing discovery/acquisition. |
| `usgs:landsat` | Landsat archive and product access paths. | Use for USGS Landsat products and time-aware remote-sensing context. |
| `usgs:earthquake` | USGS earthquake maps, feeds, and hazard-event products. | Use for event context with strict staleness and warning rules. |
| `usgs:geologic-maps` | USGS geologic map products and related data. | Use for geology and mineral-resource context with scale and interpretation warnings. |

## 6. Example dataset families

USGS publishes many datasets and services. This profile does not whitelist every layer. It defines dataset families that can be considered by a KFM source steward.

| Dataset family | Example KFM use | Default source role | Risk posture |
|---|---|---:|---|
| The National Map base layers | Topographic context, public map base layers, national reference overlays | `primary` for USGS-published layer content; `context` for map orientation | Moderate; verify layer vintage and scale |
| 3DEP DEMs and lidar | Elevation, slope, contours, relief, drainage modeling, terrain context | `primary` for USGS elevation product; `context` for derived interpretation | Moderate to high; derivatives require QA |
| National Hydrography Dataset | Streams, rivers, lakes, canals, reaches, waterbody features | `primary` for USGS hydrography features; `corroborating` for legal/regulatory claims | High; water features change and may be scale-dependent |
| Watershed Boundary Dataset | HUC boundaries, watershed Focus Mode context | `primary` for USGS/partner WBD boundary dataset; `context` for local analysis | Moderate; explain HUC scale |
| NHDPlus HR | Hydrologic network analysis and value-added flowline context | `primary` for USGS product fields; `context` for interpretation | High; analysis assumptions must be recorded |
| GNIS | Official geographic names and label/search authority | `primary` for federally recognized name record | Moderate; GNIS is not parcel, ZIP Code, or road authority |
| Water Data / NWIS | Streamgage, groundwater, spring, water-quality, and monitoring-site observations | `primary` for USGS station/observation records | High; near-real-time data can become stale or preliminary |
| ScienceBase releases | USGS scientific datasets and data-release citations | `primary` for released USGS data product; `context` for interpretation | Moderate to high; release constraints vary |
| Landsat / EarthExplorer | Imagery discovery, remote-sensing change context, historical landscape comparison | `primary` for USGS product metadata; `context` for derived claims | High; classification/interpretation must be separate |
| Historic topographic maps | Historic route, settlement, hydrology, landform, and map comparison | `primary` for map existence/content; `context` for historical interpretation | Moderate; old maps are not current authority |
| Geologic maps | Bedrock, surficial geology, mineral-resource context | `primary` for USGS map/data content; `context` for local interpretation | High; scale and uncertainty matter |
| Earthquake and hazard feeds | Event context, recent seismic activity, hazard awareness | `primary` for USGS event/product record; `context` for operational decisions | Very high; stale or misinterpreted hazard data can be dangerous |
| Structures and transportation base layers | Map context where USGS provides base-layer data | `context` or `corroborating` | High; local/KDOT/county sources may outrank USGS |

## 7. KFM lifecycle requirements

USGS material must follow the KFM source lifecycle.

```text
RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET / GRAPH → PUBLISHED
```

### 7.1 RAW

RAW storage may contain downloaded files, service metadata snapshots, feature exports, DEM tiles, lidar point-cloud products, water-data responses, ScienceBase records, Landsat metadata, GNIS extracts, historic map files, or hazard-feed snapshots.

Requirements:

- Preserve original filenames, request URLs, timestamps, response headers when available, and checksums.
- Preserve service metadata separately from feature payloads.
- Record access date and source handle.
- Capture product date, publication date, data vintage, and update cadence where available.
- Preserve USGS citations, dataset landing pages, and repository identifiers.
- Capture license/public-domain posture as a claim to verify, not an assumption.
- Store full service descriptions, layer metadata, and product metadata where available.

### 7.2 WORK

WORK storage may contain normalized intermediate files, reprojections, county clips, mosaics, derived rasters, contour generation, hydrologic joins, schema mappings, QA outputs, and draft crosswalks.

Requirements:

- Do not publish WORK outputs.
- Mark all transformations clearly: clip, merge, mosaic, resample, smooth, simplify, reproject, interpolate, derive slope/aspect/contours, burn streams, snap lines, join stations, or classify imagery.
- Keep USGS original identifiers alongside KFM local identifiers.
- Track lossy transformations, resampling, generalization, and derived products.
- Quarantine uncertain, sensitive, stale, or unclear-authority records.

### 7.3 QUARANTINE

Quarantine USGS-derived material when:

- Metadata is missing or contradictory.
- A ScienceBase item is access-controlled, draft, provisional, embargoed, or partner-restricted.
- A record appears public but contains protected, sensitive, or review-required information.
- A record’s public display could expose sensitive ecology, caves, archaeological, tribal, burial, sacred, or security information.
- Near-real-time water, earthquake, or hazard records are stale, preliminary, or operationally risky.
- Geometry is too coarse or generalized for the intended KFM claim.
- A topographic, hydrographic, or elevation layer is being used for legal, parcel, access, or regulatory claims outside its scope.
- Remote-sensing interpretation has not been separated from source metadata and properly validated.
- Dataset authority overlaps with county, state, tribal, municipal, or private records.

### 7.4 PROCESSED

Processed USGS-derived datasets must include:

- Normalized schema.
- KFM source descriptor.
- EvidenceBundle linkage.
- Policy classification.
- Transform receipt.
- QA report.
- Geometry or raster validity report.
- Attribution statement.
- Update cadence.
- Staleness rule.
- Confidence and source-role labels.
- Scale and uncertainty notes.
- Derived-product lineage if KFM creates new rasters, vectors, or classifications.

### 7.5 CATALOG / TRIPLET / GRAPH

Only processed, validated, policy-labeled records may produce:

- Catalog records.
- Entity records.
- Spatial feature records.
- Observation records.
- Time-series references.
- Triplets.
- Graph edges.
- Tile-build inputs.
- Public API payload candidates.

Triplets and graph records must never claim more authority than the USGS source supports.

### 7.6 PUBLISHED

Publication is a governed state transition. A USGS-derived artifact may be published only after:

- Source descriptor exists.
- EvidenceBundle exists.
- Policy label is assigned.
- Sensitive-data review is complete.
- Attribution is present.
- Update/staleness rule is defined.
- Public API or tile envelope is generated from released KFM artifacts.
- Public-client runtime cannot bypass KFM and read RAW, WORK, QUARANTINE, canonical internal stores, or live USGS endpoints directly.

## 8. Source descriptor baseline

Use this as the starting point for a source descriptor. Adjust fields to match the current `source_descriptor` schema.

```yaml
id: source:usgs
title: U.S. Geological Survey
short_title: USGS
source_profile: source-profile:usgs
agency:
  name: U.S. Geological Survey
  parent: U.S. Department of the Interior
source_type: federal_earth_science_geospatial_hydrologic_source
default_role: primary
role_guidance:
  primary:
    - USGS-published records and datasets within USGS authority.
    - The National Map, 3DEP, NHD, WBD, GNIS, NWIS, Water Data, ScienceBase releases, Landsat, and hazard-event records when used within stated scope.
  corroborating:
    - County parcel, access, road, zoning, regulatory, local emergency, or state-managed claims requiring another authority.
    - Kansas county Focus Mode claims where USGS is not the final authority.
  context:
    - Basemap, terrain, watershed, hydrographic, remote-sensing, geologic, and historical map context.
  restricted:
    - Sensitive ecology, cave, archaeology, tribal, burial, sacred, security, private well, embargoed, draft, or access-controlled data.
jurisdiction:
  country: US
  focus_region: Kansas and national USGS coverage relevant to KFM
access:
  handles:
    - usgs:the-national-map
    - usgs:tnm-downloader
    - usgs:tnm-services
    - usgs:3dep
    - usgs:nhd
    - usgs:wbd
    - usgs:nhdplus-hr
    - usgs:gnis
    - usgs:waterdata
    - usgs:nwis
    - usgs:sciencebase
    - usgs:earthexplorer
    - usgs:landsat
    - usgs:earthquake
    - usgs:geologic-maps
policy:
  public_client_direct_read: false
  cite_or_abstain: true
  sensitive_topics_fail_closed: true
  publication_requires_evidence_bundle: true
  publication_requires_policy_review: true
refresh:
  default_cadence: quarterly
  high_volatility_cadence: monthly_daily_or_event_driven
  stale_after_days: 120
quality:
  require_metadata_snapshot: true
  require_checksum: true
  require_geometry_or_raster_validation: true
  require_schema_crosswalk: true
  require_attribution: true
  require_scale_warning: true
```

## 9. Dataset-level descriptor extension

Each USGS dataset, service layer, ScienceBase release, raster product, observation family, or map series should receive its own dataset-level descriptor. Do not rely on this profile alone.

Recommended id pattern:

```text
source:usgs:<program-or-theme>:<dataset-or-layer-slug>
```

Examples:

```text
source:usgs:tnm:national-map-base
source:usgs:elevation:3dep-dem-10m
source:usgs:elevation:3dep-lidar-point-cloud
source:usgs:hydrography:nhd
source:usgs:hydrography:wbd
source:usgs:hydrography:nhdplus-hr
source:usgs:names:gnis-domestic
source:usgs:water:nwis-sites
source:usgs:water:waterdata-instantaneous-values
source:usgs:repository:sciencebase-release
source:usgs:remote-sensing:landsat-collection
source:usgs:hazards:earthquake-feed
source:usgs:maps:historic-topographic-map
source:usgs:geology:geologic-map
```

Minimum dataset-level fields:

```yaml
id: source:usgs:<theme>:<dataset>
parent_profile: source-profile:usgs
title: <official dataset, service, release, or product title>
source_role: <primary|corroborating|context|restricted>
source_handle: <usgs:the-national-map|usgs:3dep|usgs:nhd|...>
accessed_at: <ISO-8601 timestamp>
source_landing_page: <URL or registry pointer>
service_endpoint: <URL or registry pointer>
metadata_endpoint: <URL or registry pointer>
download_endpoint: <URL or registry pointer>
repository_item_id: <ScienceBase or catalog id when applicable>
spatial_coverage: <national|state|county|custom geometry>
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
geometry_or_raster_policy:
  may_tile_publicly: false
  requires_simplification_review: true
  requires_scale_warning: true
  requires_raster_derivative_lineage: true
evidence:
  evidence_bundle_id: <KFM EvidenceBundle id>
  receipt_id: <KFM receipt id>
```

## 10. Identity and crosswalk policy

USGS identifiers must be preserved. KFM identifiers must be deterministic and separate.

### 10.1 Preserve source identifiers

Preserve source fields such as:

- Dataset title.
- USGS program name.
- Service name.
- Layer id.
- Layer name.
- Object id, feature id, reach code, COMID, site id, station id, event id, map id, scene id, product id, or repository id where applicable.
- GNIS Feature ID.
- NHD and WBD identifiers.
- NWIS site number and parameter code.
- ScienceBase item id.
- Landsat product identifier.
- Earthquake event id.
- DEM tile id or lidar project id.
- Product date, publication date, and accessed timestamp.
- CRS, resolution, scale, and processing level.

### 10.2 Create KFM identifiers

KFM identifiers should be generated deterministically from source and geometry/record fields.

Recommended pattern:

```text
kfm:feature:usgs:<theme>:<normalized-source-key>
kfm:record:usgs:<record-family>:<normalized-source-key>
kfm:observation:usgs:<station-or-event>:<timestamp-or-record-key>
kfm:raster:usgs:<product-family>:<tile-or-product-key>
kfm:evidence:usgs:<dataset>:<receipt-hash>
```

### 10.3 Crosswalk requirements

Create or update crosswalk records when USGS data connects to:

- County parcels.
- County road centerlines.
- Kansas state agency records.
- FEMA flood data.
- NOAA weather and climate data.
- USDA soils or land-cover datasets.
- EPA water-quality records.
- BLM PLSS and land-status data.
- Historic maps and archives.
- KFM Focus Mode county entities.
- KFM EvidenceBundle records.

Crosswalks must include directionality and authority posture.

Example:

```yaml
crosswalk_id: crosswalk:usgs-nhd:kfm-county-hydro:<hash>
from:
  source: source:usgs:hydrography:nhd
  key: <USGS NHD feature or reach key>
to:
  source: kfm:county-focus:<county>
  key: <KFM hydro feature id>
relationship: same_or_related_hydrographic_feature
authority_posture: USGS is hydrography reference; county, state, FEMA, or field records may govern legal, regulatory, flood, access, or operational claims.
confidence: <low|medium|high>
evidence_bundle_id: <EvidenceBundle id>
```

## 11. EvidenceBundle mapping

Every USGS-derived public claim must point to an EvidenceBundle.

Minimum EvidenceBundle fields for USGS material:

```yaml
evidence_bundle_id: evidence:usgs:<dataset>:<hash>
claim:
  text: <precise claim supported by USGS source>
  scope: <geometry|record|attribute|observation|time-series|raster|relationship|context>
source:
  source_id: source:usgs:<theme>:<dataset>
  source_profile: source-profile:usgs
  source_role: <primary|corroborating|context|restricted>
  accessed_at: <ISO-8601 timestamp>
  source_title: <official source title>
  source_steward: U.S. Geological Survey
  source_handle: <handle>
lineage:
  raw_receipt_id: <receipt id>
  transform_receipt_id: <receipt id>
  validation_receipt_id: <receipt id>
  derivative_receipt_id: <receipt id if KFM derived a new raster/vector/classification>
policy:
  public_release: <allowed|denied|requires_review>
  sensitive_review: <passed|failed|pending>
  redaction: <none|generalized|suppressed|withheld>
quality:
  geometry_valid: <true|false|unknown|not_applicable>
  raster_valid: <true|false|unknown|not_applicable>
  metadata_complete: <true|false|unknown>
  source_date: <date or unknown>
  stale_after: <date or rule>
  scale_or_resolution: <value or unknown>
  preliminary_or_provisional: <true|false|unknown>
```

## 12. Public API and tile policy

Public KFM clients may display USGS-derived information only through KFM-governed outputs.

Allowed public surfaces:

- KFM public API records.
- KFM released vector tiles.
- KFM released raster tiles.
- KFM released static exports.
- KFM EvidenceDrawer payloads.
- KFM source-card summaries.
- KFM attribution and provenance panels.
- KFM time-series summaries derived from released KFM records.
- KFM map labels derived from released name records.

Prohibited public surfaces:

- Direct calls from the public UI to live USGS service endpoints.
- Direct calls from the public UI to USGS raw download URLs.
- Direct calls from the public UI to live near-real-time hazard or water endpoints without KFM staleness and warning gates.
- Direct exposure of RAW, WORK, QUARANTINE, or internal canonical stores.
- Direct display of unreleased candidate layers.
- Runtime AI claims derived from USGS content without EvidenceBundle support.
- Public display of sensitive site locations or unreleased protected resource data.

## 13. Ingestion checklist

Before acquiring a USGS dataset:

- [ ] Identify the USGS source handle.
- [ ] Confirm source page, service endpoint, repository item, or download endpoint.
- [ ] Confirm dataset title and steward.
- [ ] Confirm whether the dataset is public, reviewed public, provisional, restricted, or access controlled.
- [ ] Capture metadata and service description.
- [ ] Capture access timestamp.
- [ ] Capture checksums for downloaded files.
- [ ] Confirm geometry type, raster type, CRS, scale, resolution, and generalization.
- [ ] Confirm product date, publication date, and update cadence or mark as unknown.
- [ ] Assign preliminary KFM source role.
- [ ] Assign preliminary policy label.
- [ ] Decide whether the data is suitable for county Focus Mode.
- [ ] Decide whether sensitive-data review is required.
- [ ] Create or update dataset-level source descriptor.

During processing:

- [ ] Reproject to KFM standard CRS if required.
- [ ] Validate geometries or raster integrity.
- [ ] Normalize attributes.
- [ ] Preserve USGS source identifiers.
- [ ] Generate deterministic KFM identifiers.
- [ ] Produce transform receipt.
- [ ] Produce QA report.
- [ ] Produce schema crosswalk.
- [ ] Produce EvidenceBundle candidates.
- [ ] Record all derived-product steps.
- [ ] Quarantine sensitive, stale, preliminary, or ambiguous records.

Before publication:

- [ ] Confirm EvidenceBundle exists.
- [ ] Confirm source descriptor is current.
- [ ] Confirm policy review passed.
- [ ] Confirm sensitive-data review passed.
- [ ] Confirm attribution text exists.
- [ ] Confirm source-role label is visible.
- [ ] Confirm stale-after rule exists.
- [ ] Confirm scale/resolution warning exists where needed.
- [ ] Confirm public output does not bypass KFM.
- [ ] Confirm public UI displays uncertainty, preliminary, and staleness warnings where needed.

## 14. Validation rules

### 14.1 Metadata validation

Reject or quarantine if:

- No source title exists.
- No steward can be identified.
- No accessed timestamp exists.
- No source endpoint, landing page, repository item, service id, or product id is recorded.
- No policy posture is assigned.
- No source-role label is assigned.
- No EvidenceBundle can be produced.
- Dataset vintage is unknown and the public claim depends on recency.
- Product resolution, scale, or processing level is unknown and the public claim depends on precision.

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
- County-boundary clipping.
- Tile-scale visibility.
- Alignment against appropriate local or state reference layers.
- Hydrographic connectivity where network use is claimed.
- Point-station placement where station-level claims are shown.

Do not overstate geometry precision. If a USGS layer is generalized, scale-dependent, or optimized for display, KFM must carry that warning forward.

### 14.3 Raster validation

Validate:

- CRS and pixel resolution.
- NoData values.
- Data type.
- Tile boundaries.
- Mosaicking effects.
- Resampling method.
- Vertical datum and units for elevation.
- Slope, contour, hillshade, or derivative settings.
- Source product and derivative lineage.
- Raster clipping and compression effects.
- Suitability for public tile display.

### 14.4 Attribute validation

Validate:

- Required identifiers.
- Null or unknown values.
- Domain values.
- Date and timestamp fields.
- Program/category fields.
- Observation parameter codes.
- Unit fields.
- Preliminary/provisional indicators.
- Access or use constraints.
- Layer-name-to-schema mapping.
- Product-level metadata and citation fields.

### 14.5 Authority validation

Ask:

- Is USGS the authority for this claim?
- Is another federal, state, tribal, county, municipal, or private source more authoritative?
- Is the claim geospatial, hydrologic, observational, scientific, legal, operational, historical, or interpretive?
- Does the public display imply a right of access?
- Does the display imply legal flood status or regulatory authority?
- Does the display create risk for sensitive resources or private property?
- Does the scale or resolution support the intended use?
- Is the data preliminary, provisional, near-real-time, or stale?
- Is KFM deriving an interpretation that must be labeled separately from the USGS source?

## 15. Redaction and generalization rules

USGS-derived records must follow KFM sensitive-topic rules.

Default redaction posture:

| Topic | Default action |
|---|---|
| Archaeological sites | Withhold or aggregate; do not publish precise locations |
| Burial or sacred sites | Withhold; tribal and legal review required |
| Tribal cultural resources | Withhold unless explicit public-release authority exists |
| Sensitive species, habitat, nest, den, cave, or collection site | Generalize, aggregate, or withhold |
| Private wells or household-sensitive sampling context | Generalize, suppress, or require steward review |
| Law enforcement or emergency operations | Withhold operational detail |
| Infrastructure vulnerability | Withhold or generalize |
| Real-time hazard data | Publish only with KFM staleness and warning gates |
| Unverified access implication | Mark as unverified; do not route users |
| Generalized topographic, hydrographic, geologic, or elevation boundary | Display with scale or resolution warning |
| Historic maps | Display with date and interpretation warning |

## 16. Attribution baseline

Public KFM products using USGS-derived data must include attribution.

Recommended baseline:

```text
Contains information derived from public U.S. Geological Survey (USGS) datasets or records. KFM processing, normalization, filtering, generalization, derivation, and presentation are governed KFM outputs and should not be interpreted as direct USGS publication.
```

For maps:

```text
Source: U.S. Geological Survey (USGS). Processed by Kansas Frontier Matrix. See EvidenceBundle for source, access date, processing receipt, derivative lineage, and public-release policy.
```

For EvidenceDrawer:

```text
USGS source role: <primary|corroborating|context|restricted>. Authority scope: <scope>. Accessed: <date>. KFM receipt: <receipt id>.
```

## 17. Refresh and staleness policy

Default cadence:

| Dataset type | Suggested refresh |
|---|---:|
| The National Map base layers | Quarterly or on release cycle |
| 3DEP DEMs and lidar | Quarterly or on release cycle |
| NHD / WBD / NHDPlus HR | Quarterly or on release cycle |
| GNIS | Bi-monthly or on release cycle |
| Water Data / NWIS station metadata | Monthly or on source update |
| Water observations / near-real-time values | Daily, hourly, or event-driven if publicly displayed |
| ScienceBase releases | On ingestion and before publication |
| Landsat metadata and products | On scene/product acquisition |
| Historic topographic maps | Annual or on-demand |
| Geologic maps | Annual or on-demand |
| Earthquake and hazard feeds | Event-driven; strict stale warning required |
| Service metadata snapshots | Every acquisition and before publication |

Default stale-after rule:

```yaml
stale_after_days: 120
```

Override to shorter windows for water observations, earthquakes, hazards, near-real-time feeds, public safety, and operationally sensitive data.

## 18. Failure modes

Known USGS-source failure modes for KFM:

| Failure mode | KFM response |
|---|---|
| Service endpoint changes | Refresh source descriptor; do not silently repoint without receipt |
| Layer id changes | Rebuild dataset descriptor and crosswalk |
| Display-optimized layer used as legal boundary | Quarantine or label with scale warning |
| NHD feature treated as legal water boundary | Correct source role; require regulatory/local authority |
| WBD HUC boundary treated as parcel or jurisdiction boundary | Correct source role; display watershed scale warning |
| GNIS name treated as road, parcel, ZIP Code, or municipal authority | Correct claim scope; require appropriate authority |
| Water observation displayed without timestamp or provisional warning | Suppress or add KFM warning gate |
| Near-real-time hazard feed becomes stale | Suppress or mark stale; do not present as current |
| DEM derivative shown without resolution/datum/lineage | Quarantine until derivative receipt exists |
| Landsat imagery interpreted as land-use fact without method | Separate source product from KFM interpretation |
| ScienceBase item has access or release constraints | Quarantine until steward review |
| Missing metadata | Quarantine until resolved |
| Conflicting USGS and county/state records | Create conflict record; do not publish resolved claim without steward review |
| Runtime AI generates unsupported USGS claim | Suppress or mark unsupported; cite-or-abstain |

## 19. Open questions

- Which USGS dataset families should be promoted to explicit KFM whitelisted dataset descriptors?
- Should KFM maintain a statewide Kansas USGS base mirror for NHD, WBD, 3DEP, GNIS, and selected National Map layers?
- Which Kansas county Focus Mode plans require USGS hydrography, elevation, GNIS, and water-site extracts by default?
- What is the canonical KFM CRS for all USGS-derived vector and raster processing?
- What scale or resolution threshold should be required before public display of USGS-derived boundaries or terrain products?
- Which USGS data families require automatic sensitive-resource quarantine?
- How should KFM distinguish USGS source observations from KFM-derived interpretations?
- Should near-real-time water and hazard displays require an explicit freshness badge in the public UI?
- Should USGS historic topographic maps be cataloged by county, quadrangle, year, or map series?
- How should USGS ScienceBase citations be represented in EvidenceBundle records?

## 20. Steward review checklist

A source steward should review this file when:

- USGS changes a relevant access point.
- KFM adds a new USGS dataset family.
- KFM updates the source descriptor schema.
- KFM changes public API or tile publication policy.
- A county Focus Mode plan depends on USGS data.
- A sensitive-data incident or near miss occurs.
- USGS metadata conflicts with another authority.
- KFM adds hydrography, elevation, GNIS, water-observation, geology, remote-sensing, or hazard features.
- KFM changes raster derivative, tile-building, or terrain-processing rules.

## 21. Minimal publication rule

A USGS-derived KFM record may be public only when this rule passes:

```text
Public = released KFM artifact
       + EvidenceBundle
       + source descriptor
       + source role
       + policy label
       + sensitive review
       + attribution
       + staleness rule
       + scale/resolution warning when needed
       + derivative lineage when KFM derived a product
       + no direct RAW/WORK/QUARANTINE/live-endpoint dependency
```

If any term is missing, the record is not publishable.

## 22. Implementation note

This profile is intentionally conservative. It does not reduce the value of USGS data. It protects KFM from making legal, regulatory, access, emergency, ecological, cultural, or operational claims that the source does not support.

USGS data should enter KFM as evidence-bearing source material, not as sovereign runtime truth. KFM outputs must remain governed, cited, reviewable, time-aware, reversible, and policy-safe.
