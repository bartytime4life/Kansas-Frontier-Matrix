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
  layerId?: string;
  featureId?: string;
}>;

export type SourceGap = Readonly<{
  id: string;
  priority: "P0" | "P1" | "P2" | "P3";
  title: string;
  disposition: "IMPLEMENTED" | "DEFER DATA" | "DEFER POLICY" | "DEFER DEPENDENCY" | "NEEDS DECISION";
  reason: string;
  unlock: string;
}>;

export const CORPUS_SNAPSHOT = Object.freeze({
  inspectedAt: "2026-08-24",
  sourceCount: 12,
  candidateCount: 11,
  gapCount: 7,
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
  Object.freeze({ id: "SRC-CAND-USGS-HYDRO", title: "WBD / NWIS hydrology family", organization: "U.S. Geological Survey", domain: "Hydrology", cadence: "Versioned + continuous", sourceRole: "Governing context + observation", dataModes: ["Vector", "API", "Time series"], value: "Watersheds, stream context, gauges, and time-aware observations for a bounded proof lane.", cannotProve: "A rendered flowline is not current flow, flood risk, water quality, or a regulatory boundary.", nextGate: "Verify exact product versions, provisional-data rules, rights, identifiers, and geometry generalization.", layerId: "water-context", featureId: "water-smoky-hill" }),
  Object.freeze({ id: "SRC-CAND-FEMA-NFHL", title: "National Flood Hazard Layer", organization: "FEMA", domain: "Hazards", cadence: "Periodic", sourceRole: "Regulatory context", dataModes: ["Vector", "Services"], value: "Versioned flood-hazard context with explicit regulatory character.", cannotProve: "It is not a live flood observation, emergency warning, engineering determination, or property-specific advice.", nextGate: "Resolve service/version identity, effective dates, attribution, update cadence, and public carrier design." }),
  Object.freeze({ id: "SRC-CAND-NOAA", title: "Weather, climate, and alert source family", organization: "NOAA / National Weather Service", domain: "Atmosphere", cadence: "Event + continuous + periodic", sourceRole: "Operational + observational", dataModes: ["API", "Grid", "Time series"], value: "Freshness-aware observations and official-source routing for atmospheric context.", cannotProve: "KFM must not become an emergency alert service or reinterpret stale operational products as current guidance.", nextGate: "Separate observations, models, climate products, and official alerts; define expiry and life-safety boundaries.", layerId: "atmosphere-observations", featureId: "atmo-topeka-2026" }),
  Object.freeze({ id: "SRC-CAND-CDL", title: "Cropland Data Layer", organization: "USDA NASS", domain: "Agriculture", cadence: "Annual", sourceRole: "Modeled classification", dataModes: ["Raster", "API"], value: "Annual crop and land-cover context for versioned change analysis.", cannotProve: "A classified pixel is not parcel ownership, operator identity, exact crop truth, yield, or a material change by itself.", nextGate: "Verify year/version, accuracy metadata, rights, materiality thresholds, public scale, and change sidecars.", layerId: "agriculture-context", featureId: "ag-generalized-west" }),
  Object.freeze({ id: "SRC-CAND-SSURGO", title: "SSURGO / gSSURGO soil family", organization: "USDA NRCS", domain: "Soil", cadence: "Irregular revision", sourceRole: "Authoritative survey context", dataModes: ["Vector", "Database", "Raster"], value: "Soil map units, interpretations, and scale-aware land capability context.", cannotProve: "A map unit is not exact on-the-ground condition, current moisture, engineering suitability, or parcel truth.", nextGate: "Select carrier, preserve scale and interpretation caveats, record survey vintage, and design soil-specific evidence fields." }),
  Object.freeze({ id: "SRC-CAND-KGS", title: "Kansas geology and water data family", organization: "Kansas Geological Survey", domain: "Geology", cadence: "Dataset-specific", sourceRole: "Authoritative + observational", dataModes: ["Vector", "Raster", "Database", "Services"], value: "State geology, landforms, wells, and groundwater context from a Kansas specialist institution.", cannotProve: "A source family cannot collapse physical geology, resource estimates, permits, titles, well status, or current water condition.", nextGate: "Inventory datasets individually; assign source roles, versions, sensitivity, rights, and fitness before any layer admission.", layerId: "geology-context", featureId: "geology-smoky-hills" }),
  Object.freeze({ id: "SRC-CAND-KSMEM", title: "Kansas Memory digital archive", organization: "Kansas Historical Society", domain: "Historical geography", cadence: "Continuously expanded", sourceRole: "Primary-source archive", dataModes: ["Images", "Documents", "Metadata"], value: "Place- and time-linked primary sources for evidence-bounded historical interpretation.", cannotProve: "Archive metadata, OCR, geotags, or a single item cannot establish a broad historical route or event claim alone.", nextGate: "Resolve item-level rights, stable identifiers, metadata quality, citation format, OCR uncertainty, and public image rules.", layerId: "historical-context", featureId: "history-route-1885" }),
  Object.freeze({ id: "SRC-CAND-USGS-TOPO", title: "Historical Topographic Map Collection", organization: "U.S. Geological Survey", domain: "Historical geography", cadence: "Static archive", sourceRole: "Historical cartographic evidence", dataModes: ["GeoTIFF", "Map services"], value: "Versioned historical basemap evidence for change and place-context comparison.", cannotProve: "A historical map symbol is not present condition, surveyed boundary truth, or an unqualified historical claim.", nextGate: "Verify quadrangle identity, edition/date, georeferencing uncertainty, scale, attribution, and comparison accessibility." }),
  Object.freeze({ id: "SRC-CAND-KS-GIS", title: "State of Kansas government GIS family", organization: "Kansas agencies / KDOT", domain: "Roads & infrastructure", cadence: "Dataset-specific", sourceRole: "Governing + operational context", dataModes: ["Vector", "Services"], value: "State-maintained transportation and public-administration context.", cannotProve: "A service layer cannot establish ownership, legal status, operational condition, routing safety, or unrestricted infrastructure detail.", nextGate: "Inventory each service, resolve agency authority, terms, versioning, sensitivity, field meaning, and offline failure behavior.", layerId: "transport-context", featureId: "transport-i70-context" }),
  Object.freeze({ id: "SRC-CAND-MESONET", title: "Kansas Mesonet observations", organization: "Kansas State University", domain: "Atmosphere", cadence: "Near-real-time", sourceRole: "Observation", dataModes: ["API", "Time series"], value: "Kansas-specific station context for time-aware environmental observation patterns.", cannotProve: "A station value is not an official alert, statewide condition, forecast, or life-safety instruction.", nextGate: "Verify access terms, quality flags, station identity, latency, outage behavior, redistribution rights, and stale thresholds." }),
  Object.freeze({ id: "SRC-CAND-KDHE-WQ", title: "Kansas water-quality information family", organization: "Kansas Department of Health and Environment", domain: "Hydrology", cadence: "Program-specific", sourceRole: "Regulatory + observational context", dataModes: ["Reports", "Tables", "Services"], value: "State regulatory and monitoring context for water-quality evidence lanes.", cannotProve: "A program page or monitoring result cannot establish current safety for an unscoped location or use.", nextGate: "Separate regulatory designations, monitoring results, advisory products, dates, parameters, methods, and geographic scope." }),
]);

export const SOURCE_GAPS: readonly SourceGap[] = Object.freeze([
  Object.freeze({ id: "GAP-P0-001", priority: "P0", title: "Focus outcome could be manually forced", disposition: "IMPLEMENTED", reason: "A prior scenario switch could display ANSWER for unsupported context.", unlock: "Selected evidence state now deterministically selects one of four finite outcomes." }),
  Object.freeze({ id: "GAP-P1-002", priority: "P1", title: "Share state omitted projection and draw order", disposition: "IMPLEMENTED", reason: "Shared views did not reproduce all supported visual context.", unlock: "Projection and validated full layer order now serialize and restore." }),
  Object.freeze({ id: "GAP-P1-008", priority: "P1", title: "No released PMTiles, MVT, COG, or governed API adapter", disposition: "DEFER DEPENDENCY", reason: "The Explorer currently uses bounded site-local GeoJSON fixtures.", unlock: "Admitted artifact, manifest, rights, exact-negative failures, correction propagation, and performance proof." }),
  Object.freeze({ id: "GAP-P2-009", priority: "P2", title: "County Focus Mode packages remain plans", disposition: "DEFER POLICY", reason: "No county-specific admitted data or release package is present.", unlock: "Source descriptors, review owners, policy, EvidenceBundles, generalized geometry, and release evidence." }),
  Object.freeze({ id: "GAP-P2-007", priority: "P2", title: "Swipe comparison has no compatible pair", disposition: "DEFER DATA", reason: "No aligned, rights-cleared, released or explicitly demonstrated comparison pair exists.", unlock: "Paired sources, temporal alignment, attribution/export rules, and keyboard/text alternative." }),
  Object.freeze({ id: "GAP-P3-006", priority: "P3", title: "Terrain and hillshade are data-gated", disposition: "DEFER DATA", reason: "No audited raster DEM or release-linked terrain manifest exists.", unlock: "Audited DEM, rights, attribution, performance budget, release linkage, and evidence-parity 2D fallback." }),
  Object.freeze({ id: "GAP-P1-011", priority: "P1", title: "Source discovery is not source admission", disposition: "NEEDS DECISION", reason: "Drive catalogs and external source lists can tempt the UI to imply live data readiness.", unlock: "A source-intake carrier, accountable disposition, rights and sensitivity review, stable version identity, and no-public-effect default." }),
]);

export const SOURCE_DOMAINS = Object.freeze(["ALL", ...Array.from(new Set(SOURCE_CANDIDATES.map((source) => source.domain))).sort()]);
