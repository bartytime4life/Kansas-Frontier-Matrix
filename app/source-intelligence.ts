export type CorpusSource = Readonly<{
  id: string;
  title: string;
  version: string;
  authority: "DOCTRINE" | "WORKING REFERENCE" | "PLANNING" | "PROPOSED";
  status: "CURRENT IN CORPUS" | "LINEAGE" | "NEEDS VERIFICATION";
  supports: readonly string[];
  limitation: string;
}>;

export type SourceCandidate = Readonly<{
  id: string;
  title: string;
  organization: string;
  domain: string;
  cadence: string;
  sourceRole: string;
  dataModes: readonly string[];
  value: string;
  cannotProve: string;
  nextGate: string;
  sourceUrl: string;
  checkedAt: string;
  layerId?: string;
  featureId?: string;
}>;

export type SourceAdmissionState = "candidate" | "context-only" | "admitted" | "held" | "quarantined" | "denied";

export const SOURCE_ADMISSION_STATES: readonly (SourceAdmissionState | "ALL")[] = Object.freeze([
  "ALL",
  "candidate",
  "context-only",
  "admitted",
  "held",
  "quarantined",
  "denied",
]);

export const SOURCE_ADMISSION_BY_ID: Readonly<Record<string, SourceAdmissionState>> = Object.freeze({
  "SRC-CAND-USGS-HYDRO": "candidate",
  "SRC-CAND-FEMA-NFHL": "context-only",
  "SRC-CAND-NOAA": "held",
  "SRC-CAND-CDL": "held",
  "SRC-CAND-SSURGO": "held",
  "SRC-CAND-KGS": "candidate",
  "SRC-CAND-KSMEM": "context-only",
  "SRC-CAND-USGS-TOPO": "context-only",
  "SRC-CAND-KS-GIS": "candidate",
  "SRC-CAND-MESONET": "held",
  "SRC-CAND-KDHE-WQ": "candidate",
  "SRC-CAND-AWS-TERRAIN": "context-only",
  "SRC-CAND-USGS-3DEP": "candidate",
  "SRC-CAND-NOAA-HMS-SMOKE": "context-only",
  "SRC-CAND-RASPBERRY-SHAKE": "candidate",
  "SRC-CAND-USGS-3DEP-LIDAR": "candidate",
});

export type SourceGap = Readonly<{
  id: string;
  priority: "P0" | "P1" | "P2" | "P3";
  title: string;
  disposition: "IMPLEMENTED" | "DEFER DATA" | "DEFER POLICY" | "DEFER DEPENDENCY" | "NEEDS DECISION";
  reason: string;
  unlock: string;
}>;

export const CORPUS_SNAPSHOT = Object.freeze({
  inspectedAt: "2026-09-08",
  sourceCount: 12,
  candidateCount: 16,
  gapCount: 10,
  rule: "Drive references inform doctrine and proposals; current repository and runtime evidence decide implementation claims.",
});

export const CORPUS_SOURCES: readonly CorpusSource[] = Object.freeze([
  Object.freeze({
    id: "SRC-ATLAS-SEED",
    title: "KFM Full Atlas Seed Cards",
    version: "Drive document · inspected 24 Aug 2026",
    authority: "PROPOSED",
    status: "CURRENT IN CORPUS",
    supports: ["Claim-level trust fields", "Separate temporal axes", "Evidence-preserving exports", "Validation and runtime health states", "Receipts and proof objects"],
    limitation: "The cards are normalized proposals with placeholder identifiers. They do not prove repository adoption, stable contracts, live data, runtime behavior, or release authority.",
  }),
  Object.freeze({
    id: "SRC-UNIFIED-WORKSPACE",
    title: "KFM Unified Workspace — Complete User Interface Architecture",
    version: "v0.1.0 draft · 23 Aug 2026",
    authority: "PROPOSED",
    status: "CURRENT IN CORPUS",
    supports: ["Four public workspaces", "One context spine", "Role-bounded capability", "Progressive disclosure", "Federated surfaces"],
    limitation: "A repository-grounded architecture synthesis. Proposed routes and privileged workspaces are not current runtime, authorization, release, deployment, or publication evidence.",
  }),
  Object.freeze({
    id: "SRC-DELTA",
    title: "KFM Circled Sources — Distinctive Delta Synthesis",
    version: "Consolidation record · 23 Aug 2026",
    authority: "WORKING REFERENCE",
    status: "CURRENT IN CORPUS",
    supports: ["Authority and maturity as separate axes", "FRAME–TRACE–PROVE–SHOW–REHEARSE rhythm", "Five briefing lenses"],
    limitation: "Retains three non-authoritative reporting ideas only; it creates no state machine, policy result, workflow gate, roadmap commitment, or authority claim.",
  }),
  Object.freeze({
    id: "SRC-WHOLE",
    title: "KFM Authoritative Whole-System Reference",
    version: "Proposed-for-adoption edition · 15 Aug 2026",
    authority: "PROPOSED",
    status: "CURRENT IN CORPUS",
    supports: ["Inspectable claim unit", "Source intake", "Temporal axes", "Domain lanes", "MapContextEnvelope"],
    limitation: "A synthesis and source artifact; it does not supersede accepted ADRs, contracts, schemas, code, tests, manifests, or runtime evidence.",
  }),
  Object.freeze({
    id: "SRC-MAP-OPS",
    title: "KFM MapLibre Operating Architecture, Governed UI, and AI Interaction Manual",
    version: "Revised working edition · 26 Apr 2026",
    authority: "WORKING REFERENCE",
    status: "CURRENT IN CORPUS",
    supports: ["Persistent map shell", "Stable feature translation", "Evidence Drawer", "Bounded Focus Mode", "Runtime validation"],
    limitation: "Confirms design doctrine and proposed behavior, not repository depth, released data, or production runtime readiness.",
  }),
  Object.freeze({
    id: "SRC-MAP-MASTER",
    title: "Master MapLibre Components-Functions-Features",
    version: "v2.0 · 16 May 2026",
    authority: "WORKING REFERENCE",
    status: "CURRENT IN CORPUS",
    supports: ["Registry layers", "PMTiles diagnostics", "Comparison controls", "Accessibility", "Performance budgets"],
    limitation: "A cumulative idea atlas. Repetition, breadth, or inclusion does not prove adoption or data admission.",
  }),
  Object.freeze({
    id: "SRC-DOCTRINE",
    title: "KFM Unified Doctrine Synthesis",
    version: "v1.0 · reviewed 19 May 2026",
    authority: "DOCTRINE",
    status: "CURRENT IN CORPUS",
    supports: ["Evidence-first claims", "Finite outcomes", "Lifecycle", "Trust membrane", "Negative-state visibility"],
    limitation: "Repository paths and runtime claims must be verified against current main and executable evidence.",
  }),
  Object.freeze({
    id: "SRC-CONNECTED",
    title: "Kansas Frontier Matrix — Connected-Dots Architecture Brief",
    version: "v2.1 · 12 Jul 2026 copy",
    authority: "DOCTRINE",
    status: "CURRENT IN CORPUS",
    supports: ["Map-first surface", "Evidence-aware exports", "Finite Focus outcomes", "Governed public carriers"],
    limitation: "The authoring session did not itself inspect current repository state or operate a governed backend.",
  }),
  Object.freeze({
    id: "SRC-PIPE",
    title: "Kansas Frontier Matrix Pipeline Living Implementation Manual",
    version: "v0.3 · 30 Apr 2026",
    authority: "PLANNING",
    status: "CURRENT IN CORPUS",
    supports: ["Lifecycle loop", "Watcher limits", "No auto-publish", "Negative fixtures", "Receipts"],
    limitation: "Supersedes v0.2 for planning only; described code paths remain subordinate to repository evidence.",
  }),
  Object.freeze({
    id: "SRC-AI",
    title: "Kansas Frontier Matrix — AI Build Operating Contract",
    version: "v3.0 · 19 May 2026",
    authority: "DOCTRINE",
    status: "CURRENT IN CORPUS",
    supports: ["Evidence-subordinate AI", "Cite or abstain", "Finite envelopes", "Audit receipts", "No browser-to-model path"],
    limitation: "Proposed implementation placement and adapters are not proof of a live governed AI service.",
  }),
  Object.freeze({
    id: "SRC-OPEN-DATA",
    title: "Open Data Resources for Kansas — Comprehensive Catalog",
    version: "31 Jan 2026",
    authority: "WORKING REFERENCE",
    status: "NEEDS VERIFICATION",
    supports: ["Candidate sources", "Formats", "Cadence clues", "Agency discovery", "Historical archives"],
    limitation: "A discovery catalog, not a KFM source registry. Rights, current endpoints, versions, materiality, and fitness must be rechecked before admission.",
  }),
  Object.freeze({
    id: "SRC-FOCUS-NEMAHA",
    title: "Nemaha County Focus Mode Build Plan",
    version: "v0.1-proposed · 9 Jun 2026",
    authority: "PROPOSED",
    status: "NEEDS VERIFICATION",
    supports: ["County context", "Sensitive-lane defaults", "Finite outcomes", "Build-plan structure"],
    limitation: "Explicitly proves no implementation, admission, validation, review, release, or publication for the county lane.",
  }),
]);

export const SOURCE_CANDIDATES: readonly SourceCandidate[] = Object.freeze([
  Object.freeze({ id: "SRC-CAND-USGS-HYDRO", title: "WBD / NWIS hydrology family", organization: "U.S. Geological Survey", domain: "Hydrology", cadence: "Versioned + continuous", sourceRole: "Governing context + observation", dataModes: ["Vector", "API", "Time series"], value: "Watersheds, stream context, gauges, and time-aware observations for a bounded proof lane.", cannotProve: "A rendered flowline is not current flow, flood risk, water quality, or a regulatory boundary.", nextGate: "Verify exact product versions, provisional-data rules, rights, identifiers, and geometry generalization.", sourceUrl: "https://waterdata.usgs.gov/nwis", checkedAt: "2026-09-08", layerId: "water-context", featureId: "water-smoky-hill" }),
  Object.freeze({ id: "SRC-CAND-FEMA-NFHL", title: "National Flood Hazard Layer", organization: "FEMA", domain: "Hazards", cadence: "Periodic", sourceRole: "Regulatory context", dataModes: ["Vector", "Services"], value: "Versioned flood-hazard context with explicit regulatory character.", cannotProve: "It is not a live flood observation, emergency warning, engineering determination, or property-specific advice.", nextGate: "Resolve service/version identity, effective dates, attribution, update cadence, and public carrier design.", sourceUrl: "https://www.fema.gov/flood-maps/national-flood-hazard-layer", checkedAt: "2026-09-08" }),
  Object.freeze({ id: "SRC-CAND-NOAA", title: "Weather, climate, and alert source family", organization: "NOAA / National Weather Service", domain: "Atmosphere", cadence: "Event + continuous + periodic", sourceRole: "Operational + observational", dataModes: ["API", "Grid", "Time series"], value: "Freshness-aware observations and official-source routing for atmospheric context.", cannotProve: "KFM must not become an emergency alert service or reinterpret stale operational products as current guidance.", nextGate: "Separate observations, models, climate products, and official alerts; define expiry and life-safety boundaries.", sourceUrl: "https://www.weather.gov/documentation/services-web-api", checkedAt: "2026-09-08", layerId: "atmosphere-observations", featureId: "atmo-topeka-2026" }),
  Object.freeze({ id: "SRC-CAND-CDL", title: "Cropland Data Layer", organization: "USDA NASS", domain: "Agriculture", cadence: "Annual", sourceRole: "Modeled classification", dataModes: ["Raster", "API"], value: "Annual crop and land-cover context for versioned change analysis.", cannotProve: "A classified pixel is not parcel ownership, operator identity, exact crop truth, yield, or a material change by itself.", nextGate: "Verify year/version, accuracy metadata, rights, materiality thresholds, public scale, and change sidecars.", sourceUrl: "https://croplandcros.scinet.usda.gov/", checkedAt: "2026-09-08", layerId: "agriculture-context", featureId: "ag-generalized-west" }),
  Object.freeze({ id: "SRC-CAND-SSURGO", title: "SSURGO / gSSURGO soil family", organization: "USDA NRCS", domain: "Soil", cadence: "Irregular revision", sourceRole: "Authoritative survey context", dataModes: ["Vector", "Database", "Raster"], value: "Soil map units, interpretations, and scale-aware land capability context.", cannotProve: "A map unit is not exact on-the-ground condition, current moisture, engineering suitability, or parcel truth.", nextGate: "Select carrier, preserve scale and interpretation caveats, record survey vintage, and design soil-specific evidence fields.", sourceUrl: "https://www.nrcs.usda.gov/resources/data-and-reports/soil-survey-geographic-database-ssurgo", checkedAt: "2026-09-08" }),
  Object.freeze({ id: "SRC-CAND-KGS", title: "Kansas geology and water data family", organization: "Kansas Geological Survey", domain: "Geology", cadence: "Dataset-specific", sourceRole: "Authoritative + observational", dataModes: ["Vector", "Raster", "Database", "Services"], value: "State geology, landforms, wells, and groundwater context from a Kansas specialist institution.", cannotProve: "A source family cannot collapse physical geology, resource estimates, permits, titles, well status, or current water condition.", nextGate: "Inventory datasets individually; assign source roles, versions, sensitivity, rights, and fitness before any layer admission.", sourceUrl: "https://kgs.ku.edu/data-and-maps", checkedAt: "2026-09-08", layerId: "geology-context", featureId: "geology-smoky-hills" }),
  Object.freeze({ id: "SRC-CAND-KSMEM", title: "Kansas Memory digital archive", organization: "Kansas Historical Society", domain: "Historical geography", cadence: "Continuously expanded", sourceRole: "Primary-source archive", dataModes: ["Images", "Documents", "Metadata"], value: "Place- and time-linked primary sources for evidence-bounded historical interpretation.", cannotProve: "Archive metadata, OCR, geotags, or a single item cannot establish a broad historical route or event claim alone.", nextGate: "Resolve item-level rights, stable identifiers, metadata quality, citation format, OCR uncertainty, and public image rules.", sourceUrl: "https://www.kansasmemory.org/", checkedAt: "2026-09-08", layerId: "historical-context", featureId: "history-route-1885" }),
  Object.freeze({ id: "SRC-CAND-USGS-TOPO", title: "Historical Topographic Map Collection", organization: "U.S. Geological Survey", domain: "Historical geography", cadence: "Static archive", sourceRole: "Historical cartographic evidence", dataModes: ["GeoTIFF", "Map services"], value: "Versioned historical basemap evidence for change and place-context comparison.", cannotProve: "A historical map symbol is not present condition, surveyed boundary truth, or an unqualified historical claim.", nextGate: "Verify quadrangle identity, edition/date, georeferencing uncertainty, scale, attribution, and comparison accessibility.", sourceUrl: "https://www.usgs.gov/programs/national-geospatial-program/historical-topographic-maps-preserving-past", checkedAt: "2026-09-08" }),
  Object.freeze({ id: "SRC-CAND-KS-GIS", title: "State of Kansas government GIS family", organization: "Kansas agencies / KDOT", domain: "Roads & infrastructure", cadence: "Dataset-specific", sourceRole: "Governing + operational context", dataModes: ["Vector", "Services"], value: "State-maintained transportation and public-administration context.", cannotProve: "A service layer cannot establish ownership, legal status, operational condition, routing safety, or unrestricted infrastructure detail.", nextGate: "Inventory each service, resolve agency authority, terms, versioning, sensitivity, field meaning, and offline failure behavior.", sourceUrl: "https://www.ksdot.gov/about/our-organization/divisions/planning-and-development/kansas-maps-and-gis-resources", checkedAt: "2026-09-08", layerId: "transport-context", featureId: "transport-i70-context" }),
  Object.freeze({ id: "SRC-CAND-MESONET", title: "Kansas Mesonet observations", organization: "Kansas State University", domain: "Atmosphere", cadence: "Near-real-time", sourceRole: "Observation", dataModes: ["API", "Time series"], value: "Kansas-specific station context for time-aware environmental observation patterns.", cannotProve: "A station value is not an official alert, statewide condition, forecast, or life-safety instruction.", nextGate: "Verify access terms, quality flags, station identity, latency, outage behavior, redistribution rights, and stale thresholds.", sourceUrl: "https://mesonet.k-state.edu/", checkedAt: "2026-09-08" }),
  Object.freeze({ id: "SRC-CAND-KDHE-WQ", title: "Kansas water-quality information family", organization: "Kansas Department of Health and Environment", domain: "Hydrology", cadence: "Program-specific", sourceRole: "Regulatory + observational context", dataModes: ["Reports", "Tables", "Services"], value: "State regulatory and monitoring context for water-quality evidence lanes.", cannotProve: "A program page or monitoring result cannot establish current safety for an unscoped location or use.", nextGate: "Separate regulatory designations, monitoring results, advisory products, dates, parameters, methods, and geographic scope.", sourceUrl: "https://www.kdhe.ks.gov/1096/Water-Quality-Information-Resources", checkedAt: "2026-09-08" }),
  Object.freeze({ id: "SRC-CAND-AWS-TERRAIN", title: "Terrain Tiles · Terrarium", organization: "AWS Open Data / Mapzen", domain: "Terrain / Elevation", cadence: "Community-maintained mosaic", sourceRole: "External display carrier", dataModes: ["Raster DEM", "Terrarium tiles"], value: "Key-free RGB elevation tiles that MapLibre can decode directly for reversible 3D terrain and hillshade.", cannotProve: "A successfully rendered surface is not an admitted KFM elevation value, survey result, USGS product identity, accuracy statement, or release.", nextGate: "Keep it context-only; monitor availability and attribution, retain 2D parity, and never export sampled values as evidence.", sourceUrl: "https://registry.opendata.aws/terrain-tiles/", checkedAt: "2026-09-09" }),
  Object.freeze({ id: "SRC-CAND-USGS-3DEP", title: "3DEP 1/3 arc-second Digital Elevation Model", organization: "U.S. Geological Survey", domain: "Terrain / Elevation", cadence: "Continuously maintained seamless product", sourceRole: "Authoritative elevation candidate", dataModes: ["COG", "WCS", "Image service"], value: "Approximately 10 m national seamless bare-earth elevation suitable for a Kansas terrain artifact after a governed, reproducible transform.", cannotProve: "A catalog page or raw DEM cannot by itself prove the exact source tile, vertical datum, transform, renderer compatibility, accuracy for a selected point, or KFM release.", nextGate: "Pin product/version and Kansas coverage, record datum and lineage, transform to a MapLibre-compatible DEM carrier, validate performance and 2D parity, then complete admission and release review.", sourceUrl: "https://data.usgs.gov/datacatalog/data/USGS%3A3a81321b-c153-416f-98b7-cc8e5f0e17c3", checkedAt: "2026-09-09" }),
  Object.freeze({ id: "SRC-CAND-NOAA-HMS-SMOKE", title: "NOAA HMS satellite-analyzed smoke polygons", organization: "NOAA Hazard Mapping System", domain: "Atmosphere / Fire", cadence: "Daily analyst publication", sourceRole: "External operational context", dataModes: ["KML", "Polygons", "Time intervals"], value: "Dated qualitative smoke footprints with provider Start/End intervals for a bounded Kansas situational-context layer.", cannotProve: "A smoke footprint is not surface PM2.5, plume altitude, measured transport, a fire perimeter, exposure, a health advisory, a warning, or an all-clear.", nextGate: "Keep the fixed bounded adapter context-only; if any future source admission is proposed, pin product meaning, interval semantics, rights, QA, correction behavior, and a separate surface-concentration/transport source.", sourceUrl: "https://www.ospo.noaa.gov/products/land/hms.html", checkedAt: "2026-09-10", layerId: "external-noaa-hms-smoke" }),
  Object.freeze({ id: "SRC-CAND-RASPBERRY-SHAKE", title: "Raspberry Shake AM FDSN network", organization: "Raspberry Shake", domain: "Geology / Hazards", cadence: "Station metadata on demand; archived waveform delay", sourceRole: "Citizen-seismology station context", dataModes: ["FDSN StationXML/text", "miniSEED", "StationView"], value: "Public station locations and metadata can connect seismic context to a Kansas map, with provider StationView as the realtime inspection surface.", cannotProve: "FDSN station metadata is not a realtime waveform stream, event catalog, calibrated ground-motion value, alert, or evidence of absence; raw counts need response metadata and waveform quality checks.", nextGate: "Keep the station layer context-only; separately scope a rate-limited waveform adapter, response conversion, station privacy/rights review, failure states, and a non-alert product contract before loading samples.", sourceUrl: "https://manual.raspberryshake.org/fdsn.html", checkedAt: "2026-09-10", layerId: "external-raspberry-shake-stations" }),
  Object.freeze({ id: "SRC-CAND-USGS-3DEP-LIDAR", title: "USGS 3DEP LiDAR point clouds and work-unit metadata", organization: "U.S. Geological Survey", domain: "Terrain / Elevation", cadence: "Work-unit and product dependent", sourceRole: "Authoritative terrain source candidate", dataModes: ["LiDAR point cloud", "DEM", "XML/GeoPackage metadata", "Image/WCS services"], value: "LiDAR-derived terrain, slope, hillshade, and provenance metadata for a future governed Kansas terrain lane.", cannotProve: "A dynamic visualization does not prove the selected work unit, nominal pulse spacing, vertical accuracy, datum, acquisition interval, point classification, or a claim-bearing elevation at a cursor.", nextGate: "Select exact Kansas work units/products, preserve XML and spatial metadata, validate CRS/datum/nodata and derived parameters, produce a reproducible bounded artifact, and complete performance, rights, review, and release gates.", sourceUrl: "https://www.usgs.gov/3d-elevation-program/about-3dep-products-services", checkedAt: "2026-09-10", layerId: "external-usgs-3dep-slope" }),
]);

export const SOURCE_GAPS: readonly SourceGap[] = Object.freeze([
  Object.freeze({ id: "GAP-P0-001", priority: "P0", title: "Focus outcome could be manually forced", disposition: "IMPLEMENTED", reason: "A prior scenario switch could display ANSWER for unsupported context.", unlock: "Selected evidence state now deterministically selects one of four finite outcomes." }),
  Object.freeze({ id: "GAP-P1-002", priority: "P1", title: "Share state omitted projection and draw order", disposition: "IMPLEMENTED", reason: "Shared views did not reproduce all supported visual context.", unlock: "Projection and validated full layer order now serialize and restore." }),
  Object.freeze({ id: "GAP-P1-008", priority: "P1", title: "No released PMTiles, MVT, COG, or governed API adapter", disposition: "DEFER DEPENDENCY", reason: "The Explorer currently uses bounded site-local GeoJSON fixtures.", unlock: "Admitted artifact, manifest, rights, exact-negative failures, correction propagation, and performance proof." }),
  Object.freeze({ id: "GAP-P2-009", priority: "P2", title: "County Focus Mode packages remain plans", disposition: "DEFER POLICY", reason: "No county-specific admitted data or release package is present.", unlock: "Source descriptors, review owners, policy, EvidenceBundles, generalized geometry, and release evidence." }),
  Object.freeze({ id: "GAP-P2-007", priority: "P2", title: "Swipe comparison has no compatible pair", disposition: "DEFER DATA", reason: "No aligned, rights-cleared, released or explicitly demonstrated comparison pair exists.", unlock: "Paired sources, temporal alignment, attribution/export rules, and keyboard/text alternative." }),
  Object.freeze({ id: "GAP-P3-006", priority: "P3", title: "Terrain display carrier is active; evidence admission remains gated", disposition: "IMPLEMENTED", reason: "An attributed Terrarium carrier now supports opt-in 3D display with a 2D fallback, while USGS 3DEP remains a separately identified candidate.", unlock: "For evidence use: pin a 3DEP product/version, preserve datum and transform lineage, validate a MapLibre-compatible derivative, close rights and performance review, and attach release evidence." }),
  Object.freeze({ id: "GAP-P1-011", priority: "P1", title: "Source discovery is not source admission", disposition: "NEEDS DECISION", reason: "Drive catalogs and external source lists can tempt the UI to imply live data readiness.", unlock: "A source-intake carrier, accountable disposition, rights and sensitivity review, stable version identity, and no-public-effect default." }),
  Object.freeze({ id: "GAP-P1-012", priority: "P1", title: "External display endpoints lacked one runtime disclosure registry", disposition: "IMPLEMENTED", reason: "Basemap and terrain URLs, activation rules, attribution, fallbacks, and evidence exclusions were spread across renderer modules and interface copy.", unlock: "One typed registry now drives external renderer configuration and the visible Sources disclosure without admitting any carrier as KFM evidence." }),
  Object.freeze({ id: "GAP-P1-013", priority: "P1", title: "Smoke and hazard context needed a source-separated live surface", disposition: "IMPLEMENTED", reason: "The Site now binds NOAA HMS dated smoke polygons, NWS alert areas, NOAA radar, USGS earthquakes, NWM guidance, and hydrology as separately labeled operational context instead of one composite hazard layer.", unlock: "For any claim-bearing hazard workflow, add release-pinned source contracts, QA/correction receipts, model-vs-observation separation, rights/sensitivity review, and emergency-boundary policy." }),
  Object.freeze({ id: "GAP-P2-014", priority: "P2", title: "Raspberry Shake station context lacks a governed waveform bridge", disposition: "DEFER DEPENDENCY", reason: "Station metadata and StationView are connected, while archived waveform retrieval, response conversion, realtime streaming, and event interpretation remain deliberately out of the browser path.", unlock: "Define bounded FDSN waveform queries, T−30-minute freshness, response/units conversion, station quality and outage states, rate limits, privacy/rights, and an explicit non-alert product contract." }),
]);

export const SOURCE_DOMAINS = Object.freeze(["ALL", ...Array.from(new Set(SOURCE_CANDIDATES.map((source) => source.domain))).sort()]);
