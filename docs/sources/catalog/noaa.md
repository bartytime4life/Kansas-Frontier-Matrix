<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/sources-catalog-noaa
title: National Oceanic and Atmospheric Administration Source Catalog Profile
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
tags: [kfm, sources, catalog, noaa, nws, ncei, weather, climate, radar, nexrad, storm-events, climate-normals, atlas-14, warnings, forecasts, nowcoast, digital-coast, hazards]
notes:
  - "v0.1 — Initial NOAA source catalog profile for governed KFM ingestion, evidence use, and public-release boundaries."
  - "This profile describes source use. It does not authorize direct public-client reads from NOAA, NWS, NCEI, nowCOAST, or other NOAA systems."
  - "Weather, warning, forecast, radar, and hazard feeds require strict time-awareness and stale-data suppression."
] -->

National Oceanic and Atmospheric Administration Source Catalog Profile

Path: docs/sources/catalog/noaa.md

1. Purpose

This document defines the Kansas Frontier Matrix (KFM) source-catalog profile for the National Oceanic and Atmospheric Administration (NOAA).

NOAA sources are foundational to KFM for weather, climate, severe storms, watches and warnings, radar, historical observations, climate normals, precipitation-frequency estimates, drought and climate context, coastal and ocean products, selected elevation/imagery/land-cover products, and environmental hazard records. Within KFM, NOAA data must be treated as governed upstream source material that enters the KFM lifecycle through source descriptors, ingestion receipts, validation, EvidenceBundles, catalog records, triplets, graph records, tile products, and released artifacts.

This profile prevents NOAA material from becoming an ungoverned runtime dependency, a stale public-safety signal, or a blanket substitute for local emergency management, county road authority, engineering design, insurance, legal, regulatory, or field-verified authority.

2. Source identity

Field	Value
Source family	Federal weather, climate, ocean, coastal, radar, hazard, and environmental data source
Steward organization	U.S. Department of Commerce — National Oceanic and Atmospheric Administration
Common abbreviation	NOAA
Major NOAA sub-sources	National Weather Service, National Centers for Environmental Information, National Ocean Service, Office for Coastal Management, National Environmental Satellite, Data, and Information Service, Storm Prediction Center, National Hurricane Center, Climate Prediction Center
Common abbreviations	NOAA, NWS, NCEI, NOS, OCM, NESDIS, SPC, NHC, CPC
KFM source profile id	source-profile:noaa
Recommended source id prefix	source:noaa:
Primary KFM domains	sources, catalog, map, weather, climate, hazards, radar, hydrology, drought, severe-storms, environmental-records, evidence
Main access modes	NWS API, weather.gov pages, NCEI data access, Climate Data Online, NEXRAD/radar archive, Storm Events Database, Climate Normals, NOAA Atlas 14 PFDS, nowCOAST, NOAA Digital Coast, NDFD, SPC/NHC/CPC products, public downloads and services
Public-client access posture	Public clients may use only KFM released artifacts, governed APIs, tile services, and policy-safe runtime envelopes. They must not read NOAA raw endpoints directly.

3. KFM authority posture

NOAA can be authoritative for records and datasets that NOAA publishes, maintains, or designates as official for its own programs. NOAA is not automatically authoritative for local road closures, property damage determination, insurance claims, legal floodplain status, emergency orders, parcel boundaries, land ownership, evacuation decisions, agricultural losses, infrastructure condition, or site-specific engineering design.

3.1 Use NOAA as primary when

Use NOAA as a primary source only for NOAA-published records or datasets within NOAA authority, such as:

* NWS watches, warnings, advisories, alerts, forecast discussions, forecast grids, and public forecast products within their issued time windows.
* NWS API responses for alerts, observations, forecast points, gridpoints, zones, offices, and stations when request and timestamp are receipted.
* NCEI climate records, Climate Data Online records, station observations, station metadata, climate normals, and historical weather datasets.
* NCEI radar archive records, including NEXRAD and related radar products, when used within product metadata and time scope.
* NOAA Storm Events Database records and severe-weather climatology products where NCEI is the source of record.
* NOAA Atlas 14 / Precipitation Frequency Data Server outputs where applicable.
* NOAA nowCOAST map services and products where the NOAA product metadata identifies the product and update status.
* NOAA Digital Coast hosted data products, including lidar, imagery, land cover, coastal hazards, and coastal/ocean datasets where NOAA is the steward or host.
* SPC, NHC, CPC, WPC, and other NOAA center products when used within the product’s stated scope, time period, and warning limitations.

3.2 Use NOAA as corroborating when

Use NOAA as corroborating support when a KFM claim depends on another authority, including:

* County road closures, barricades, detours, or maintenance responsibility.
* Local emergency management orders, evacuations, shelter status, curfews, or public-safety instructions.
* FEMA regulatory floodplain, flood insurance, NFIP, or flood-damage determinations.
* Insurance claims, crop-loss claims, disaster-aid eligibility, or legal proof of loss.
* County parcel, ownership, zoning, permitting, drainage, or tax records.
* State dam-safety, water-rights, water-quality, or environmental regulation.
* Engineering design, drainage design, stormwater design, or site-specific hydrology.
* Fire restrictions, burn bans, drought declarations, or agricultural emergency declarations issued by state/local authorities.
* County Focus Mode claims involving access, ownership, operational restrictions, or legal status.

3.3 Use NOAA as context when

Use NOAA as contextual background when the record helps orient or interpret KFM but does not itself prove the final claim, including:

* Historic storm and climate context.
* County climate-normal summaries.
* Weather and severe-storm climatology.
* Radar imagery used for event interpretation.
* Drought, heat, precipitation, wind, hail, tornado, winter-weather, or flood-risk context.
* NOAA Atlas 14 precipitation-frequency context for planning narratives.
* nowCOAST or NOAA Digital Coast products used for map context.
* Forecast and warning products shown as time-bounded situational awareness.
* Climate trend and anomaly context.
* Remote-sensing or satellite-derived environmental context.

3.4 Use NOAA as restricted or fail closed when

Treat NOAA-derived material as restricted or fail closed when it includes or implies:

* Active watches, warnings, alerts, forecasts, radar, or hazard feeds without strict timestamp, expiration, and staleness gates.
* Emergency decisions that require local authority, field verification, or official incident command.
* Private damage, injury, fatality, insurance, property-loss, or farm-loss details not suitable for public display.
* Sensitive infrastructure vulnerability, critical-facility exposure, or public-safety weakness.
* Sensitive ecology, species, habitat, or protected-resource locations in coastal, marine, climate, or environmental datasets.
* Vessel, aircraft, or navigation-related operational information whose public reuse could be unsafe outside NOAA’s intended context.
* Unreleased, draft, provisional, restricted, embargoed, or partner-controlled NOAA datasets.
* Any record whose geometry, resolution, time step, uncertainty, or product status does not support the public claim being made.
* Any product with caveats indicating it is experimental, preliminary, advisory-only, or not for legal/regulatory use.

4. Kansas relevance

KFM is Kansas-centered. NOAA is highly relevant to Kansas Focus Mode and statewide build work.

NOAA is especially relevant to Kansas for:

* NWS watches, warnings, advisories, forecasts, alert areas, forecast zones, county warning areas, and weather office jurisdiction.
* Severe thunderstorm, tornado, hail, wind, lightning, winter storm, excessive heat, cold, flash flood, river flood, and fire-weather context.
* NCEI historical observations, station records, climate normals, climate summaries, and station metadata.
* Storm Events Database records for tornado, hail, wind, flood, winter, heat, drought, lightning, and other storm impacts.
* NEXRAD radar archive and near-real-time radar context from Kansas and surrounding WSR-88D sites.
* NOAA Atlas 14 precipitation-frequency estimates used as planning context.
* Climate Prediction Center outlooks and drought/climate context.
* Weather Prediction Center precipitation and excessive rainfall products.
* Storm Prediction Center convective outlooks, watches, mesoscale discussions, and severe-weather reports.
* Heat, drought, flood, and severe-storm history for county Focus Mode.
* NOAA Digital Coast products only where relevant to KFM datasets, national coverage, hazards, imagery, lidar, land cover, or cross-domain products.

NOAA should not be treated as a replacement for:

* Kansas county emergency management.
* Local law enforcement, road and bridge, or public works notices.
* Kansas Department of Transportation road conditions and closures.
* FEMA regulatory flood products.
* Kansas water-rights, water-quality, dam-safety, or emergency authorities.
* County parcel GIS and assessor records.
* Insurance, legal, engineering, or loss-determination authority.
* Local burn bans, emergency declarations, or agricultural disaster programs.
* Field verification.

For Kansas county Focus Mode, NOAA usually serves one of these roles:

1. Weather and hazard source for NWS warning, alert, forecast, and event products.
2. Climate source for NCEI station observations, climate normals, and historical climate context.
3. Storm-history source for Storm Events Database and severe-weather summaries.
4. Radar source for NEXRAD archive and radar-event interpretation.
5. Precipitation-frequency source for NOAA Atlas 14 / PFDS planning context.
6. Drought and outlook context source for CPC, NIDIS-linked NOAA context, and climate outlook products.
7. Public-safety context source that must remain time-bounded and locally corroborated.

5. Canonical access points

The following access points are recognized by this profile. Their availability, service structure, layer names, formats, metadata, and operating status must be verified during each source refresh.

Handle	Use	KFM treatment
noaa:nws-api	NWS API for alerts, forecasts, observations, gridpoints, zones, offices, and stations.	Use for receipt-backed weather products. Never expose raw live API dependency directly to public clients.
noaa:weather-gov	weather.gov public forecast, alert, office, radar, and product pages.	Use for human review, source discovery, and public product confirmation.
noaa:nws-alerts	NWS watches, warnings, advisories, and alert products.	Use only with issued, effective, onset, expiration, and update timestamps. Stale products must be suppressed or archived.
noaa:ndfd	National Digital Forecast Database products and services.	Use for forecast grids and forecast context with strict time-awareness.
noaa:ncei	NOAA National Centers for Environmental Information data access and archive.	Use for historical weather, climate, ocean, coastal, geophysical, and environmental data.
noaa:cdo	Climate Data Online and related climate-station data access.	Use for station observations, climate data, climate normals, and historical weather records.
noaa:climate-normals	NCEI U.S. Climate Normals products.	Use for 30-year climate-normal context and station summaries.
noaa:storm-events	NCEI Storm Events Database and related storm-event records.	Use for historical storm event evidence with caveats for reporting completeness and damage estimates.
noaa:nexrad	NCEI radar archive and NEXRAD data access.	Use for radar-event context, archive retrieval, and severe-weather evidence support.
noaa:radar-current	NOAA/NWS current radar products and viewers.	Use only for time-bounded situational awareness; do not publish as evergreen evidence.
noaa:atlas14-pfds	NOAA Atlas 14 Precipitation Frequency Data Server.	Use for precipitation-frequency estimates and planning context where applicable.
noaa:nowcoast	nowCOAST viewer and OGC/ArcGIS map services.	Use for near-real-time NOAA weather, ocean, hydrologic, and hazard map layers with strict staleness rules.
noaa:digital-coast	NOAA Digital Coast data and tools.	Use for hosted coastal, lidar, imagery, land cover, hazards, and related datasets where relevant and properly scoped.
noaa:data-access-viewer	NOAA Digital Coast Data Access Viewer.	Use for governed acquisition of imagery, lidar/elevation, and land-cover products when appropriate.
noaa:spc	Storm Prediction Center outlooks, watches, mesoscale discussions, and storm reports.	Use for severe-weather context with strict valid-time and product-status rules.
noaa:nhc	National Hurricane Center products.	Context source; generally low Kansas relevance except remnants and historical context.
noaa:cpc	Climate Prediction Center outlooks and climate products.	Use for climate outlook and drought/temperature/precipitation context with valid-period rules.
noaa:wpc	Weather Prediction Center precipitation, excessive rainfall, winter weather, and forecast products.	Use for national forecast context and event interpretation with valid-period rules.
noaa:ahps-nwm	NOAA/NWS river, flood, hydrologic, and National Water Model products where available.	Use with caution; corroborate with USGS streamgages and local emergency management for operational claims.
noaa:nesdis	NOAA satellite and environmental data products.	Use for satellite-derived environmental context with product-specific metadata and uncertainty.

6. Example dataset families

NOAA publishes many datasets, services, reports, feeds, products, warnings, outlooks, and map layers. This profile does not whitelist every product. It defines dataset families that can be considered by a KFM source steward.

Dataset family	Example KFM use	Default source role	Risk posture
NWS alerts	Tornado, severe thunderstorm, flash flood, winter storm, heat, wind, fire-weather alerts	primary for issued NWS alert record; context for public UI	Very high; expiration and stale suppression required
NWS forecasts and gridpoints	County Focus Mode weather context, forecast summaries, valid-time displays	primary for issued forecast product; context for planning	Very high; forecast validity windows required
NWS observations and stations	Recent observations, station metadata, temperature, wind, precipitation context	primary for NWS observation record	High; station placement and time validity matter
NCEI climate archive	Historical weather and climate records	primary for archived NOAA climate record	Moderate; station metadata and QC matter
Climate Data Online	Station observations, daily/monthly summaries, climate normals access	primary for CDO-returned records	Moderate; query receipt required
Climate Normals	30-year normals for temperature, precipitation, snowfall, etc.	primary for official normal product	Moderate; normal period must be labeled
Storm Events Database	Tornado, hail, wind, flood, winter, heat, drought event history	primary for NCEI storm-event record; context for interpretation	High; reporting and damage caveats
NEXRAD archive	Radar event reconstruction, hail/wind/tornado context	primary for archived radar product; context for interpretation	High; product level/time/site metadata required
Current radar	Situational awareness in public UI	context only	Very high; stale display can mislead
NOAA Atlas 14 / PFDS	Rainfall frequency, stormwater planning context	primary for NOAA PFDS estimate; corroborating for design/legal use	High; confidence intervals and station/location caveats
SPC outlooks/watches/reports	Severe-weather risk and event context	primary for issued SPC product; context for interpretation	Very high; valid-time and update rules
CPC outlooks	Climate outlook and seasonal climate context	primary for issued CPC product; context for local use	High; not a local forecast guarantee
WPC products	Excessive rainfall, QPF, winter weather, national forecast context	primary for issued WPC product; context for local use	High; valid-time rules
nowCOAST layers	Near-real-time weather, ocean, hydrologic, alert, forecast, and map services	primary for NOAA product layer; context for display	Very high; live-map staleness and service lineage
Digital Coast lidar/imagery/land cover	Elevation, imagery, land-cover, hazards and coastal products	primary for NOAA-hosted product where NOAA is steward; otherwise context	Moderate to high; coverage and coastal bias
Satellite products	Cloud, fire, vegetation, precipitation, environmental monitoring context	primary for product record; context for derived interpretation	High; algorithm and resolution caveats
NOAA marine/coastal products	Navigation, tide, current, coastal flood, shoreline, ocean datasets	primary within product scope; context for KFM inland work	High; Kansas relevance often limited
NOAA hazard outlooks	Drought, heat, excessive rainfall, severe storms, fire weather	context or corroborating unless product itself is the claim	High; local authority may outrank

7. KFM lifecycle requirements

NOAA material must follow the KFM source lifecycle.

RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET / GRAPH → PUBLISHED

7.1 RAW

RAW storage may contain NWS API responses, alert payloads, forecast grid responses, station observations, NCEI downloads, CDO queries, climate normals files, Storm Events records, radar metadata, radar files, NOAA Atlas 14 PFDS outputs, nowCOAST service metadata, Digital Coast downloads, outlook products, screenshots used for verification, or NOAA product text.

Requirements:

* Preserve original filenames, request URLs, API routes, timestamps, response headers when available, and checksums.
* Preserve request parameters, points, zones, stations, time ranges, product ids, event ids, radar station ids, and query filters.
* Preserve issued, effective, onset, valid, expiration, update, observation, product, archive, and access timestamps where available.
* Preserve NOAA office, center, station, radar, zone, county warning area, forecast office, or product lineage.
* Preserve climate-station metadata, quality-control flags, units, and normal periods.
* Preserve NOAA Atlas 14 location, duration, recurrence interval, estimate, confidence interval, and source volume/version where available.
* Preserve radar level, product type, radar site, scan time, and archive metadata.
* Capture license/public-domain posture as a claim to verify, not an assumption.
* Store full metadata, documentation, and source citations where available.

7.2 WORK

WORK storage may contain normalized intermediate files, reprojections, county clips, alert-zone overlays, time-series joins, radar mosaics, gridded forecast extracts, station joins, NCEI table extracts, storm-event geocoding, climate summaries, NOAA Atlas 14 point exports, QA outputs, and draft EvidenceBundle mappings.

Requirements:

* Do not publish WORK outputs.
* Mark all transformations clearly: clip, merge, dissolve, interpolate, reproject, aggregate, resample, rasterize, vectorize, geocode, summarize, normalize units, time-zone convert, or classify.
* Keep NOAA original identifiers alongside KFM local identifiers.
* Track lossy transformations, temporal aggregation, spatial interpolation, and derived products.
* Quarantine uncertain, stale, sensitive, private, public-safety, or unclear-authority records.

7.3 QUARANTINE

Quarantine NOAA-derived material when:

* Metadata is missing or contradictory.
* Product time, issue time, expiration time, valid period, observation time, or archive date is missing.
* A live or near-real-time product is stale or cannot be verified.
* A public display could mislead users during active severe weather, flooding, fire weather, heat, cold, winter weather, or other hazards.
* A record appears public but contains protected, sensitive, private, or review-required information.
* A record’s public display could expose sensitive infrastructure, emergency operations, or vulnerable sites.
* Storm damage, fatality, injury, or loss details require privacy or local corroboration review.
* Radar, satellite, outlook, or forecast interpretation has not been separated from source metadata and properly validated.
* NOAA product scope is being used for legal, insurance, engineering, regulatory, access, or parcel claims outside its scope.
* Dataset authority overlaps with county, state, tribal, municipal, FEMA, USGS, USDA, EPA, or private records.

7.4 PROCESSED

Processed NOAA-derived datasets must include:

* Normalized schema.
* KFM source descriptor.
* EvidenceBundle linkage.
* Policy classification.
* Transform receipt.
* QA report.
* Geometry, raster, time-series, or tabular validation report.
* Attribution statement.
* Update cadence.
* Staleness rule.
* Confidence and source-role labels.
* Valid-time, issue-time, expiration-time, and observation-time labels where applicable.
* Scale, resolution, uncertainty, and caveat notes.
* Derived-product lineage if KFM creates new rasters, vectors, event summaries, tiles, or interpretations.
* Query reproducibility receipts for API, CDO, PFDS, and archive-derived outputs.

7.5 CATALOG / TRIPLET / GRAPH

Only processed, validated, policy-labeled records may produce:

* Catalog records.
* Entity records.
* Spatial feature records.
* Alert records.
* Forecast records.
* Observation records.
* Time-series references.
* Climate-normal records.
* Storm-event records.
* Radar-product references.
* Hazard-product references.
* Triplets.
* Graph edges.
* Tile-build inputs.
* Public API payload candidates.

Triplets and graph records must never claim more authority than the NOAA source supports.

7.6 PUBLISHED

Publication is a governed state transition. A NOAA-derived artifact may be published only after:

* Source descriptor exists.
* EvidenceBundle exists.
* Policy label is assigned.
* Sensitive-data review is complete.
* Attribution is present.
* Update/staleness rule is defined.
* Valid-time and expiration logic exists for time-bounded products.
* Scale, uncertainty, interpretation, and public-safety warnings are attached where needed.
* Public API or tile envelope is generated from released KFM artifacts.
* Public-client runtime cannot bypass KFM and read RAW, WORK, QUARANTINE, canonical internal stores, or live NOAA endpoints directly.

8. Source descriptor baseline

Use this as the starting point for a source descriptor. Adjust fields to match the current source_descriptor schema.

id: source:noaa
title: National Oceanic and Atmospheric Administration
short_title: NOAA
source_profile: source-profile:noaa
agency:
  name: National Oceanic and Atmospheric Administration
  parent: U.S. Department of Commerce
source_type: federal_weather_climate_ocean_hazard_and_environmental_data_source
default_role: primary
role_guidance:
  primary:
    - NOAA-published records and datasets within NOAA authority.
    - NWS alerts, forecasts, observations, NCEI climate records, CDO data, climate normals, Storm Events, NEXRAD archive, NOAA Atlas 14 PFDS, nowCOAST, Digital Coast, SPC, CPC, WPC, NHC, and NESDIS products when used within stated scope and time window.
  corroborating:
    - Local emergency, road closure, flood insurance, regulatory, legal, engineering, damage, loss, parcel, access, and operational claims requiring another authority.
    - Kansas county Focus Mode claims where NOAA is not the final authority.
  context:
    - Weather, climate, hazard, radar, drought, precipitation-frequency, outlook, satellite, and storm-history context.
  restricted:
    - Stale active hazards, sensitive infrastructure, emergency operations, private damage/loss details, restricted/provisional products, and any product outside intended scope.
jurisdiction:
  country: US
  focus_region: Kansas and national NOAA coverage relevant to KFM
access:
  handles:
    - noaa:nws-api
    - noaa:weather-gov
    - noaa:nws-alerts
    - noaa:ndfd
    - noaa:ncei
    - noaa:cdo
    - noaa:climate-normals
    - noaa:storm-events
    - noaa:nexrad
    - noaa:radar-current
    - noaa:atlas14-pfds
    - noaa:nowcoast
    - noaa:digital-coast
    - noaa:data-access-viewer
    - noaa:spc
    - noaa:nhc
    - noaa:cpc
    - noaa:wpc
    - noaa:ahps-nwm
    - noaa:nesdis
policy:
  public_client_direct_read: false
  cite_or_abstain: true
  sensitive_topics_fail_closed: true
  active_hazard_stale_data_fail_closed: true
  public_safety_requires_local_corroboration: true
  publication_requires_evidence_bundle: true
  publication_requires_policy_review: true
refresh:
  default_cadence: quarterly_or_by_dataset
  high_volatility_cadence: hourly_daily_or_event_driven
  stale_after_days: 120
quality:
  require_metadata_snapshot: true
  require_checksum: true
  require_geometry_raster_time_series_or_tabular_validation: true
  require_schema_crosswalk: true
  require_attribution: true
  require_valid_time_for_forecasts_alerts_and_outlooks: true
  require_query_receipt_for_api_cdo_pfds_and_archive_outputs: true

9. Dataset-level descriptor extension

Each NOAA dataset, API route family, service layer, archive product, warning product, forecast product, radar product, outlook product, station family, or map layer should receive its own dataset-level descriptor. Do not rely on this profile alone.

Recommended id pattern:

source:noaa:<program-or-theme>:<dataset-or-product-slug>

Examples:

source:noaa:nws:alerts
source:noaa:nws:forecast-gridpoints
source:noaa:nws:observations
source:noaa:nws:zones
source:noaa:ncei:climate-data-online
source:noaa:ncei:climate-normals
source:noaa:ncei:storm-events
source:noaa:radar:nexrad-level-2
source:noaa:radar:nexrad-level-3
source:noaa:precipitation:atlas14-pfds
source:noaa:nowcoast:alerts-and-hazards
source:noaa:digital-coast:data-access-viewer
source:noaa:spc:convective-outlooks
source:noaa:cpc:climate-outlooks
source:noaa:wpc:excessive-rainfall
source:noaa:nesdis:satellite-product

Minimum dataset-level fields:

id: source:noaa:<theme>:<dataset>
parent_profile: source-profile:noaa
title: <official dataset, service, route, product, archive, center product, or map layer title>
source_role: <primary|corroborating|context|restricted>
source_handle: <noaa:nws-api|noaa:ncei|noaa:cdo|...>
accessed_at: <ISO-8601 timestamp>
source_landing_page: <URL or registry pointer>
service_endpoint: <URL or registry pointer>
metadata_endpoint: <URL or registry pointer>
download_endpoint: <URL or registry pointer>
api_route: <API route or registry pointer when applicable>
product_id: <NOAA product id when applicable>
event_id: <storm/hazard/radar/event id when applicable>
office_id: <NWS office/center id when applicable>
zone_id: <NWS zone id when applicable>
station_id: <NOAA/NWS/NCEI station id when applicable>
radar_site: <NEXRAD/TDWR site id when applicable>
issued_at: <ISO-8601 timestamp or unknown>
effective_at: <ISO-8601 timestamp or unknown>
onset_at: <ISO-8601 timestamp or unknown>
expires_at: <ISO-8601 timestamp or unknown>
valid_period: <interval or unknown>
observation_time: <ISO-8601 timestamp or unknown>
archive_time: <ISO-8601 timestamp or unknown>
spatial_coverage: <national|state|county|zone|station|radar-site|grid|point|custom geometry>
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
public_safety_review:
  required: true
  status: pending
geometry_raster_time_series_or_tabular_policy:
  may_tile_publicly: false
  requires_simplification_review: true
  requires_scale_warning: true
  requires_valid_time_display: true
  requires_derivative_lineage: true
evidence:
  evidence_bundle_id: <KFM EvidenceBundle id>
  receipt_id: <KFM receipt id>

10. Identity and crosswalk policy

NOAA identifiers must be preserved. KFM identifiers must be deterministic and separate.

10.1 Preserve source identifiers

Preserve source fields such as:

* Dataset title.
* NOAA office, center, or program name.
* NWS office id.
* NWS zone id.
* County warning area.
* Alert id, product id, VTEC code, event id, or warning id where available.
* Forecast grid id, gridpoint, and geometry.
* Station id, network id, station name, and station metadata.
* Climate station id, GHCN id, COOP id, WBAN id, or other NCEI station identifiers where available.
* Storm Events episode id and event id.
* Radar site, product level, product id, volume scan time, and archive id.
* NOAA Atlas 14 point, coordinates, duration, recurrence interval, estimate, and confidence interval.
* nowCOAST layer id, service id, timestamp, product lineage, and update time.
* Digital Coast dataset id, product id, resolution, collection date, and metadata id.
* SPC/CPC/WPC/NHC product id, issue time, valid time, and product status.
* Product date, publication date, accessed timestamp, CRS, resolution, scale, uncertainty, and processing level.

10.2 Create KFM identifiers

KFM identifiers should be generated deterministically from source and geometry/record fields.

Recommended pattern:

kfm:feature:noaa:<theme>:<normalized-source-key>
kfm:record:noaa:<record-family>:<normalized-source-key>
kfm:alert:noaa:<office-or-zone>:<alert-or-event-key>
kfm:forecast:noaa:<grid-or-zone>:<issued-or-valid-key>
kfm:observation:noaa:<station-id>:<timestamp-or-record-key>
kfm:event:noaa:<event-family>:<event-id>
kfm:radar:noaa:<radar-site>:<product-time-or-volume-key>
kfm:evidence:noaa:<dataset>:<receipt-hash>

10.3 Crosswalk requirements

Create or update crosswalk records when NOAA data connects to:

* County Focus Mode areas.
* County warning areas and NWS zones.
* County road and emergency-management records.
* FEMA flood data.
* USGS streamgages, hydrography, terrain, and water observations.
* NRCS soils, hydric soils, erosion, climate, snow, and water-supply records.
* USDA NASS/FSA public aggregate datasets.
* Kansas state weather, water, agriculture, emergency, or transportation records.
* EPA environmental and air/water-quality records.
* KFM EvidenceBundle records.

Crosswalks must include directionality and authority posture.

Example:

crosswalk_id: crosswalk:noaa-nws-zone:kfm-county-focus:<hash>
from:
  source: source:noaa:nws:zones
  key: <NWS zone id>
to:
  source: kfm:county-focus:<county>
  key: <KFM county focus id>
relationship: overlaps_or_contains_warning_area
authority_posture: NOAA/NWS is weather warning and forecast authority; county/local emergency management may govern road closures, sheltering, evacuation, and local public-safety instructions.
confidence: <low|medium|high>
evidence_bundle_id: <EvidenceBundle id>

11. EvidenceBundle mapping

Every NOAA-derived public claim must point to an EvidenceBundle.

Minimum EvidenceBundle fields for NOAA material:

evidence_bundle_id: evidence:noaa:<dataset>:<hash>
claim:
  text: <precise claim supported by NOAA source>
  scope: <geometry|record|attribute|alert|forecast|observation|time-series|raster|event|relationship|context|outlook>
source:
  source_id: source:noaa:<theme>:<dataset>
  source_profile: source-profile:noaa
  source_role: <primary|corroborating|context|restricted>
  accessed_at: <ISO-8601 timestamp>
  source_title: <official source title>
  source_steward: National Oceanic and Atmospheric Administration
  source_handle: <handle>
lineage:
  raw_receipt_id: <receipt id>
  query_receipt_id: <receipt id if API/CDO/PFDS/archive query is used>
  transform_receipt_id: <receipt id>
  validation_receipt_id: <receipt id>
  derivative_receipt_id: <receipt id if KFM derived a new raster/vector/summary/interpretation>
policy:
  public_release: <allowed|denied|requires_review>
  sensitive_review: <passed|failed|pending>
  public_safety_review: <passed|failed|pending>
  local_authority_review: <not_applicable|passed|failed|pending>
  redaction: <none|generalized|suppressed|withheld>
quality:
  geometry_valid: <true|false|unknown|not_applicable>
  raster_valid: <true|false|unknown|not_applicable>
  time_series_valid: <true|false|unknown|not_applicable>
  tabular_valid: <true|false|unknown|not_applicable>
  metadata_complete: <true|false|unknown>
  source_date: <date or unknown>
  issued_at: <timestamp or unknown>
  effective_at: <timestamp or unknown>
  expires_at: <timestamp or unknown>
  valid_period: <interval or unknown>
  observation_time: <timestamp or unknown>
  stale_after: <date or rule>
  scale_or_resolution: <value or unknown>
  preliminary_or_provisional: <true|false|unknown>

12. Public API and tile policy

Public KFM clients may display NOAA-derived information only through KFM-governed outputs.

Allowed public surfaces:

* KFM public API records.
* KFM released vector tiles.
* KFM released raster tiles.
* KFM released static exports.
* KFM EvidenceDrawer payloads.
* KFM source-card summaries.
* KFM attribution and provenance panels.
* KFM time-series summaries derived from released KFM records.
* KFM weather/hazard summaries with clear timestamps, expiration state, and source role.
* KFM archived-event displays that cannot be mistaken for active warnings.
* KFM climate summaries derived from released historical records.

Prohibited public surfaces:

* Direct calls from the public UI to live NOAA, NWS, NCEI, nowCOAST, Digital Coast, SPC, CPC, WPC, NHC, or NESDIS raw endpoints.
* Direct calls from the public UI to live alert, forecast, radar, hazard, or warning feeds without KFM staleness and warning gates.
* Public display of active or near-real-time NOAA products without visible issue time, valid period, expiration state, and source.
* Direct exposure of RAW, WORK, QUARANTINE, or internal canonical stores.
* Direct display of unreleased candidate layers.
* Runtime AI claims derived from NOAA content without EvidenceBundle support.
* Public display of sensitive infrastructure, emergency operations, private damage/loss details, or protected resource data.

13. Ingestion checklist

Before acquiring a NOAA dataset:

* Identify the NOAA source handle.
* Confirm source page, service endpoint, API route, archive item, product page, station, radar site, alert product, or download endpoint.
* Confirm dataset title and steward.
* Confirm whether the dataset is public, reviewed public, provisional, experimental, restricted, private, or access controlled.
* Capture metadata and service/product description.
* Capture access timestamp.
* Capture checksums for downloaded files.
* Confirm geometry type, raster type, time-series schema, tabular schema, CRS, scale, resolution, and generalization.
* Confirm issue time, valid period, expiration time, observation time, archive date, product date, publication date, and update cadence or mark as unknown.
* Capture API request, CDO query, PFDS point query, archive search, or station/radar selection when applicable.
* Assign preliminary KFM source role.
* Assign preliminary policy label.
* Decide whether the data is suitable for county Focus Mode.
* Decide whether sensitive-data, privacy, local-authority, or public-safety review is required.
* Create or update dataset-level source descriptor.

During processing:

* Reproject to KFM standard CRS if required.
* Validate geometries, raster integrity, time-series continuity, and tabular joins.
* Normalize attributes and units.
* Preserve NOAA source identifiers.
* Generate deterministic KFM identifiers.
* Produce transform receipt.
* Produce QA report.
* Produce schema crosswalk.
* Produce EvidenceBundle candidates.
* Record all derived-product steps.
* Record query reproducibility for NWS API, CDO, NCEI, PFDS, radar, and archive outputs.
* Quarantine sensitive, public-safety, stale, preliminary, experimental, or ambiguous records.

Before publication:

* Confirm EvidenceBundle exists.
* Confirm source descriptor is current.
* Confirm policy review passed.
* Confirm sensitive-data review passed.
* Confirm public-safety review passed.
* Confirm local-authority review passed or is not applicable.
* Confirm attribution text exists.
* Confirm source-role label is visible.
* Confirm stale-after rule exists.
* Confirm issue time, valid time, expiration time, and observation time are visible where needed.
* Confirm scale/resolution/interpretation warning exists where needed.
* Confirm public output does not bypass KFM.
* Confirm public UI displays uncertainty, preliminary, valid-time, expiration, and staleness warnings where needed.
* Confirm no private damage, loss, emergency-operation, or sensitive infrastructure claim is exposed.

14. Validation rules

14.1 Metadata validation

Reject or quarantine if:

* No source title exists.
* No steward can be identified.
* No accessed timestamp exists.
* No source endpoint, landing page, API route, station id, radar site, product id, event id, service id, or archive id is recorded.
* No policy posture is assigned.
* No source-role label is assigned.
* No EvidenceBundle can be produced.
* Product vintage is unknown and the public claim depends on recency.
* Issue time, valid period, expiration time, observation time, or archive time is unknown for time-bounded products.
* Product resolution, scale, mapping level, uncertainty, or forecast period is unknown and the public claim depends on precision.
* NWS API, CDO, PFDS, NCEI archive, radar, nowCOAST, or Digital Coast query details are missing.

14.2 Geometry validation

Validate:

* CRS and reprojection.
* Geometry type.
* Null geometries.
* Invalid rings or self-intersections.
* Multipart handling.
* County, zone, radar, or grid clipping.
* Dissolve effects.
* Simplification effects.
* Gridpoint-to-county and zone-to-county overlap logic.
* Tile-scale visibility.
* Alignment against appropriate local, state, USGS, FEMA, or NOAA reference layers.
* Forecast zone and warning area boundaries where zone-level claims are shown.

Do not overstate geometry precision. Forecast zones, warning polygons, radar bins, satellite pixels, grids, and outlook polygons are product geometries, not property boundaries or local closure areas.

14.3 Raster validation

Validate:

* CRS and pixel resolution.
* NoData values.
* Data type.
* Tile boundaries.
* Radar projection and scan geometry.
* Mosaicking effects.
* Resampling method.
* Time step and valid time.
* Product lineage.
* Raster clipping and compression effects.
* Suitability for public tile display.

14.4 Time-series validation

Validate:

* Observation timestamps.
* Forecast issue and valid periods.
* Alert effective/onset/expiration timestamps.
* Time zone normalization.
* Sampling interval.
* Missing intervals.
* Station relocation or metadata changes.
* Quality-control flags.
* Preliminary or estimated values.
* Units.
* Derived aggregation windows.

14.5 Tabular validation

Validate:

* Required identifiers.
* Null or unknown values.
* Domain values.
* Station, event, radar, product, and zone joins.
* Weather event type.
* Magnitude, unit, and damage fields.
* Forecast period and valid-time fields.
* Preliminary/provisional/experimental indicators.
* Access or use constraints.
* Table-name-to-schema mapping.
* Product-level metadata and citation fields.

14.6 Authority validation

Ask:

* Is NOAA the authority for this claim?
* Is another federal, state, tribal, county, municipal, emergency-management, insurance, engineering, or private source more authoritative?
* Is the claim weather, climate, radar, forecast, warning, outlook, historical event, legal, regulatory, operational, insurance, engineering, or interpretive?
* Does the public display imply a road closure, evacuation, shelter instruction, or emergency order?
* Does the display imply legal floodplain, drainage, loss, crop damage, or insurance proof?
* Does the display create risk for sensitive infrastructure, emergency operations, or private property?
* Does the scale, geometry, forecast valid time, radar resolution, station location, or product caveat support the intended use?
* Is the data preliminary, experimental, near-real-time, stale, or tied to a private/sensitive record?
* Is KFM deriving an interpretation that must be labeled separately from the NOAA source?

15. Redaction and generalization rules

NOAA-derived records must follow KFM sensitive-topic, public-safety, and time-awareness rules.

Default redaction posture:

Topic	Default action
Active alerts without valid expiration state	Suppress or mark stale/unknown; do not present as current
Forecasts without valid time or issue time	Suppress
Radar without scan/product time	Suppress
Emergency operations or local response details	Withhold operational detail
Road closure or evacuation implication	Require local authority; do not infer from NOAA hazard
Private damage, injury, fatality, or loss detail	Generalize, suppress, or require steward review
Insurance/legal proof of loss	Do not assert; refer to source record scope only
Sensitive infrastructure exposure	Withhold or generalize
Archaeological, burial, sacred, tribal, or cultural-resource locations in environmental data	Withhold; tribal/legal review required
Sensitive species, habitat, marine, coastal, or environmental resource location	Generalize, aggregate, or withhold
Real-time or near-real-time hazard data	Publish only with KFM staleness and warning gates
Unverified access implication	Mark as unverified; do not route users
Generalized warning, outlook, radar, satellite, or climate geometry	Display with scale/time/uncertainty warning
Historic storm records	Display with event-date, source, and interpretation caveat

16. Attribution baseline

Public KFM products using NOAA-derived data must include attribution.

Recommended baseline:

Contains information derived from public National Oceanic and Atmospheric Administration (NOAA) datasets or records. KFM processing, normalization, filtering, generalization, derivation, and presentation are governed KFM outputs and should not be interpreted as direct NOAA publication.

For maps:

Source: National Oceanic and Atmospheric Administration (NOAA). Processed by Kansas Frontier Matrix. See EvidenceBundle for source, access date, issue/valid/expiration time where applicable, processing receipt, derivative lineage, and public-release policy.

For EvidenceDrawer:

NOAA source role: <primary|corroborating|context|restricted>. Authority scope: <scope>. Issued/valid/expires: <time values when applicable>. Accessed: <date>. KFM receipt: <receipt id>.

For public-safety displays:

Weather and hazard information is time-sensitive. Follow current instructions from the National Weather Service and local emergency management. KFM displays are governed summaries and may not be current emergency instructions.

17. Refresh and staleness policy

Default cadence:

Dataset type	Suggested refresh
NWS active alerts	Event-driven or every few minutes while displayed
NWS forecasts and gridpoints	Hourly or per product update cycle while displayed
NWS observations	Hourly or per station update cycle while displayed
NDFD products	Per product update cycle
Current radar	Every product update if displayed; suppress if stale
NCEI climate archive	On acquisition and before publication
Climate Data Online extracts	On query execution and before publication
Climate Normals	On release cycle and before publication
Storm Events Database	Quarterly or on NCEI update cycle
NEXRAD archive	On event acquisition and before publication
NOAA Atlas 14 / PFDS	On point query and before publication
nowCOAST layers	Per layer update cycle if displayed; suppress if stale
Digital Coast downloads	On acquisition and before publication
SPC outlooks/watches/reports	Event-driven; valid-time gate required
CPC outlooks	Per product update cycle; valid-period gate required
WPC products	Per product update cycle; valid-period gate required
Satellite products	Per product update cycle; valid-time and algorithm caveats required
Service metadata snapshots	Every acquisition and before publication

Default stale-after rule:

stale_after_days: 120

Override to much shorter windows for alerts, forecasts, radar, observations, nowCOAST layers, SPC/WPC/CPC products, hydrologic products, satellite products, and all public-safety-relevant data.

Recommended active-public-display stale rules:

active_alerts:
  suppress_after_expires: true
  require_expires_at: true
forecasts:
  require_valid_period: true
  suppress_when_valid_period_ended: true
observations:
  require_observation_time: true
  stale_after_hours: 3
radar:
  require_scan_time: true
  stale_after_minutes: 30
outlooks:
  require_valid_period: true
  suppress_when_valid_period_ended: true

18. Failure modes

Known NOAA-source failure modes for KFM:

Failure mode	KFM response
Active warning displayed after expiration	Suppress or mark archived/stale; do not present as current
Forecast displayed without valid time	Suppress until valid-time metadata exists
Radar image displayed without scan/product time	Suppress until time metadata exists
NOAA hazard used to infer road closure or evacuation	Require local emergency/road authority; do not infer
Storm Events damage estimate used as legal/insurance proof	Correct claim scope; require appropriate authority
Climate normal used without normal period	Quarantine until normal period is recorded
NOAA Atlas 14 estimate used for final engineering design without review	Label as planning context; require engineering authority
NEXRAD product used without radar site, level, and scan time	Quarantine until metadata is complete
Outlook polygon treated as site-specific prediction	Add uncertainty and scale warning or suppress
nowCOAST live layer used as evergreen evidence	Archive with timestamp or suppress stale display
Digital Coast product used outside coverage/scope	Correct source role or quarantine
NOAA product caveats ignored	Add caveat or suppress
Missing metadata	Quarantine until resolved
Conflicting NOAA and county/state records	Create conflict record; do not publish resolved claim without steward review
Runtime AI generates unsupported NOAA claim	Suppress or mark unsupported; cite-or-abstain

19. Open questions

* Which NOAA dataset families should be promoted to explicit KFM whitelisted dataset descriptors?
* Should KFM maintain a Kansas-focused NOAA mirror for NWS zones, offices, stations, CDO station metadata, climate normals, and Storm Events?
* Which Kansas county Focus Mode plans require NOAA storm-history, climate-normal, NEXRAD, and warning-zone extracts by default?
* What is the canonical KFM CRS for NOAA-derived vector, raster, radar, and grid processing?
* What public UI warning language should be required for active weather and hazard displays?
* Should NOAA active alerts be treated as runtime-only situational awareness, archived evidence, or both?
* Should KFM display NWS active alerts at all, or link out to weather.gov for live emergency decisions?
* How should KFM represent NWS forecast zones and warning polygons in relation to county Focus Mode boundaries?
* Should Storm Events records be linked to local newspaper, county emergency, insurance, or disaster-declaration records before publication?
* How should KFM store NEXRAD event bundles for severe-weather case studies?
* Should NOAA Atlas 14 PFDS query receipts be first-class KFM artifacts?
* How should KFM handle NOAA products that are official but experimental, preliminary, or not intended for legal use?

20. Steward review checklist

A source steward should review this file when:

* NOAA changes a relevant access point.
* NWS API behavior, product shape, or usage guidance changes.
* KFM adds a new NOAA dataset family.
* KFM updates the source descriptor schema.
* KFM changes public API or tile publication policy.
* A county Focus Mode plan depends on NOAA data.
* A public-safety, stale-data, sensitive-data, or privacy incident or near miss occurs.
* NOAA metadata conflicts with another authority.
* KFM adds weather, climate, alert, forecast, radar, storm-event, precipitation-frequency, drought, outlook, satellite, hydrologic, or Digital Coast features.
* KFM changes raster derivative, radar-processing, time-series, tabular aggregation, or tile-building rules.

21. Minimal publication rule

A NOAA-derived KFM record may be public only when this rule passes:

Public = released KFM artifact
       + EvidenceBundle
       + source descriptor
       + source role
       + policy label
       + sensitive review
       + public-safety review
       + local-authority review when applicable
       + attribution
       + staleness rule
       + issue/valid/expiration/observation/archive time when needed
       + scale/uncertainty/interpretation warning when needed
       + query receipt when API/CDO/PFDS/archive access is used
       + derivative lineage when KFM derived a product
       + no direct RAW/WORK/QUARANTINE/live-endpoint dependency
       + no stale active-hazard display
       + no inferred emergency instruction

If any term is missing, the record is not publishable.

22. Implementation note

This profile is intentionally conservative. It does not reduce the value of NOAA data. It protects KFM from making legal, regulatory, emergency, engineering, insurance, access, operational, ecological, cultural, private-loss, or public-safety claims that the source does not support.

NOAA data should enter KFM as evidence-bearing source material, not as sovereign runtime truth. KFM outputs must remain governed, cited, reviewable, time-aware, reversible, safety-gated, and policy-safe.