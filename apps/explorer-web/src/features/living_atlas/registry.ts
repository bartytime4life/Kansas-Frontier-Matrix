import type {
  AtlasView,
  EvidenceRecord,
  LayerRecord,
  MapSnapshot,
  PolicyDecision,
  SourceDescriptor,
  TemporalExtent,
} from "./types";

const camera = (
  longitude = -98.38,
  latitude = 38.48,
  zoom = 5.4,
  pitch = 0,
): AtlasView["camera"] =>
  Object.freeze({ longitude, latitude, zoom, bearing: 0, pitch });

const time = (
  id: string,
  label: string,
  startLabel: string,
  endLabel: string,
  precision: TemporalExtent["precision"],
  order: number,
  uncertainty: string | null = null,
): TemporalExtent =>
  Object.freeze({
    id,
    label,
    startLabel,
    endLabel,
    precision,
    kind: "INTERVAL",
    order,
    uncertainty,
  });

export const TEMPORAL_EXTENTS: readonly TemporalExtent[] = Object.freeze([
  time("time:hadean", "Hadean", "4.54 billion years ago", "4.0 billion years ago", "GEOLOGIC", 0, "Approximate geologic bounds"),
  time("time:archean", "Archean", "4.0 billion years ago", "2.5 billion years ago", "GEOLOGIC", 1),
  time("time:proterozoic", "Proterozoic", "2.5 billion years ago", "538.8 million years ago", "GEOLOGIC", 2),
  time("time:paleozoic", "Paleozoic", "538.8 million years ago", "251.9 million years ago", "ERA", 3),
  time("time:mesozoic", "Mesozoic", "251.9 million years ago", "66 million years ago", "ERA", 4),
  time("time:cenozoic", "Cenozoic", "66 million years ago", "present", "ERA", 5),
  time("time:quaternary", "Quaternary", "2.58 million years ago", "present", "PERIOD", 6),
  time("time:holocene", "Holocene", "11,700 years ago", "present", "PERIOD", 7),
  time("time:archaeological", "Archaeological periods", "interval-specific", "interval-specific", "UNKNOWN", 8, "Exact dates require admitted evidence"),
  time("time:1800s", "19th century", "1800", "1899", "CENTURY", 9),
  time("time:1900s", "20th century", "1900", "1999", "CENTURY", 10),
  time("time:modern", "Modern records", "2000", "present", "YEAR", 11),
  time("time:present", "Present operational window", "latest admitted release", "present", "DATE", 12, "No universal live state"),
  Object.freeze({ id: "time:timeless", label: "Timeless display context", startLabel: "not applicable", endLabel: "not applicable", precision: "UNKNOWN", kind: "TIMELESS", order: 13, uncertainty: null }),
  Object.freeze({ id: "time:unknown", label: "Unknown time", startLabel: "unknown", endLabel: "unknown", precision: "UNKNOWN", kind: "UNKNOWN", order: 14, uncertainty: "Temporal support is not available" }),
]);

const source = (
  id: string,
  title: string,
  organization: string,
  domain: string,
  officialUrl: string | null,
  value: string,
  cannotProve: string,
  nextGate: string,
  admissionState: SourceDescriptor["admissionState"] = "CANDIDATE",
  sourceRole: SourceDescriptor["sourceRole"] = "OFFICIAL",
): SourceDescriptor =>
  Object.freeze({
    id,
    title,
    organization,
    domain,
    admissionState,
    sourceRole,
    cadence: admissionState === "CONTEXT_ONLY" ? "site-local version" : "provider-defined",
    dataMode: admissionState === "CONTEXT_ONLY" ? "inline GeoJSON fixture" : "external official portal",
    value,
    cannotProve,
    nextGate,
    officialUrl,
    lastChecked: "2026-09-09",
    rights: admissionState === "CONTEXT_ONLY" ? "KFM-authored demonstration geometry" : "NEEDS VERIFICATION per exact asset",
    sensitivity: admissionState === "DENIED" ? "RESTRICTED" : "Public portal; item-level review required",
  });

export const SOURCE_DESCRIPTORS: readonly SourceDescriptor[] = Object.freeze([
  source("source:site-local-atlas", "KFM bounded Living Atlas fixture", "Kansas Frontier Matrix", "cross-domain", null, "Keeps the map functional while external source admission remains held.", "It does not establish Kansas facts, current conditions, legal boundaries, routes, hazards, measurements, or source admission.", "Replace each role with a versioned released public-safe artifact after evidence, rights, sensitivity, review, and release closure.", "CONTEXT_ONLY", "SITE_LOCAL_FIXTURE"),
  source("source:kgs", "Kansas Geological Survey data and maps", "Kansas Geological Survey", "geology", "https://kgs.ku.edu/data-and-maps", "Candidate geology and natural-resources source family.", "A portal link does not admit a dataset, prove coverage, or support a map claim.", "Verify exact asset, rights, edition, scale, fields, transformations, review, and release."),
  source("source:kdot", "Kansas maps and GIS resources", "Kansas Department of Transportation", "roads_rail_trade", "https://www.ksdot.gov/about/our-organization/divisions/planning-and-development/kansas-maps-and-gis-resources", "Candidate transportation context.", "It does not establish current closures, routing, schedules, safety, ownership, or access.", "Select and review exact dated assets and their permitted use."),
  source("source:fema-nfhl", "National Flood Hazard Layer", "Federal Emergency Management Agency", "hazards", "https://www.fema.gov/flood-maps/national-flood-hazard-layer", "Candidate regulatory flood-hazard context.", "A portal link or display does not determine parcel status, insurance, or emergency safety.", "Verify exact service, effective date, disclaimer, geometry, rights, and release binding."),
  source("source:nrcs-ssurgo", "Soil Survey Geographic Database (SSURGO)", "USDA Natural Resources Conservation Service", "soil", "https://www.nrcs.usda.gov/resources/data-and-reports/soil-survey-geographic-database-ssurgo", "Candidate survey-unit and soil-component source family.", "Mapped units do not prove field conditions, management, yield, or continuous subsurface structure.", "Pin survey area/version, preserve component and horizon identity, validate rights and fitness."),
  source("source:usgs-htmc", "Historical Topographic Map Collection", "U.S. Geological Survey", "historical_geography", "https://www.usgs.gov/programs/national-geospatial-program/historical-topographic-maps-preserving-past", "Candidate historical-map editions.", "A historical sheet does not prove present conditions or undocumented route chronology.", "Bind exact sheet edition, georeference quality, rights, and interpretation limits."),
  source("source:kansas-memory", "Kansas Memory", "Kansas Historical Society", "archaeology", "https://www.kansasmemory.org/", "Candidate documentary and historical context.", "Discovery metadata does not authorize redistribution or precise cultural-site disclosure.", "Complete item-level rights, cultural sensitivity, georeference, and release review."),
  source("source:kdhe-water", "Water Quality Information Resources", "Kansas Department of Health and Environment", "hydrology", "https://www.kdhe.ks.gov/1096/Water-Quality-Information-Resources", "Candidate water-quality context.", "A portal link does not prove current measurements or fitness for life-safety decisions.", "Verify exact record, method, qualifiers, cadence, spatial support, and release."),
  source("source:nws-api", "National Weather Service API documentation", "National Weather Service", "atmosphere", "https://www.weather.gov/documentation/services-web-api", "Candidate observations, forecasts, and alert-service documentation.", "Documentation is not an admitted feed, forecast guarantee, or emergency-warning substitute.", "Implement a bounded adapter with issue/valid time, failure, cache, rate, and attribution controls."),
  source("source:usda-cdl", "Cropland Data Layer", "USDA National Agricultural Statistics Service", "agriculture", "https://croplandcros.scinet.usda.gov/", "Candidate annual agricultural land-cover classification.", "A class pixel does not prove crop yield, ownership, management, or field-level behavior.", "Pin an edition and validate classification accuracy, nodata, rights, scale, and public-safe use."),
  source("source:kansas-mesonet", "Kansas Mesonet", "Kansas State University", "atmosphere", "https://mesonet.k-state.edu/", "Candidate station observations.", "A station reading does not represent a continuous statewide field or emergency guidance.", "Verify station metadata, quality flags, units, interval, terms, and adapter behavior."),
  source("source:usgs-nwis", "USGS Water Data for the Nation", "U.S. Geological Survey", "hydrology", "https://waterdata.usgs.gov/nwis", "Candidate water observations and station metadata.", "A gauge observation does not establish inundation, velocity, upstream causation, or current safety.", "Pin service/version semantics and retain qualifiers, units, site identity, time, and corrections."),
]);

const layer = (
  id: string,
  name: string,
  domain: string,
  geometryType: LayerRecord["geometryType"],
  temporalExtentId: string,
  color: string,
  warning: string,
  options: Partial<Pick<LayerRecord, "sourceId" | "trustState" | "availability" | "representation" | "scaleLimit" | "defaultVisible" | "defaultOpacity">> = {},
): LayerRecord =>
  Object.freeze({
    id,
    name,
    domain,
    sourceId: options.sourceId ?? "source:site-local-atlas",
    evidenceId: `evidence:${id.slice("layer:".length)}`,
    geometryType,
    temporalExtentId,
    trustState: options.trustState ?? "SYNTHETIC",
    availability: options.availability ?? "AVAILABLE",
    representation: options.representation ?? "MAPLIBRE_INLINE",
    scaleLimit: options.scaleLimit ?? "Statewide orientation only; not survey-grade",
    warning,
    defaultVisible: options.defaultVisible ?? false,
    defaultOpacity: options.defaultOpacity ?? 0.72,
    color,
  });

export const LAYER_RECORDS: readonly LayerRecord[] = Object.freeze([
  layer("layer:kansas-frame", "Generalized Kansas extent", "boundaries_places", "POLYGON", "time:timeless", "#d9c58d", "Generalized site-local frame; not a legal boundary.", { trustState: "GENERALIZED", defaultVisible: true, defaultOpacity: 0.22 }),
  layer("layer:county-locators", "County locator starter points", "boundaries_places", "POINT", "time:modern", "#f2d28b", "Synthetic locator samples; not county seats or boundaries.", { defaultVisible: true }),
  layer("layer:settlements", "Settlement and city context", "settlements_infrastructure", "POINT", "time:modern", "#f6e7bd", "Synthetic place-role markers; names and coordinates are intentionally omitted.", { defaultVisible: true }),
  layer("layer:river-context", "Generalized river context", "hydrology", "LINE", "time:timeless", "#55b9cf", "Synthetic linework; not hydrography, flow, navigation, or flood evidence.", { trustState: "GENERALIZED", defaultVisible: true }),
  layer("layer:watershed-storage", "Watershed and storage context", "hydrology", "POLYGON", "time:modern", "#3f95b7", "Catalog-only until a reviewed public-safe source and release are bound.", { sourceId: "source:usgs-nwis", trustState: "HELD", availability: "HELD", representation: "CATALOG_ONLY" }),
  layer("layer:prairie-regions", "Prairie and ecological-region context", "habitat", "POLYGON", "time:modern", "#7eaa72", "Synthetic generalized region; not a habitat determination.", { trustState: "GENERALIZED" }),
  layer("layer:habitat-connectivity", "Habitat-connectivity concept", "habitat", "LINE", "time:modern", "#71c174", "Synthetic corridor concept; not modeled or observed movement.", { defaultOpacity: 0.6 }),
  layer("layer:fauna-range", "Guild-level fauna range context", "fauna", "POLYGON", "time:modern", "#a4c686", "Generalized synthetic envelope; no species occurrence or protected location.", { trustState: "GENERALIZED" }),
  layer("layer:flora-communities", "Generalized flora communities", "flora", "POINT", "time:modern", "#93bd67", "Synthetic community markers; not specimen or survey observations."),
  layer("layer:physiography", "Physiography context", "geology", "POLYGON", "time:cenozoic", "#b08d72", "Synthetic zone; not a geologic map or site investigation.", { sourceId: "source:kgs", trustState: "SITE_LOCAL_DEMO" }),
  layer("layer:relative-elevation", "Relative-elevation concept", "geology", "POINT", "time:timeless", "#d7a96c", "Synthetic relative values; no DEM, datum, elevation, slope, or terrain evidence."),
  layer("layer:soil-survey-entry", "SSURGO survey entry", "soil", "POLYGON", "time:modern", "#9b815e", "Held: exact survey edition, component/horizon identity, rights, and release are not bound.", { sourceId: "source:nrcs-ssurgo", trustState: "HELD", availability: "HELD", representation: "CATALOG_ONLY" }),
  layer("layer:agriculture-context", "Generalized agricultural context", "agriculture", "POLYGON", "time:modern", "#c8ad55", "Synthetic land-cover concept; not crop, yield, ownership, or management evidence."),
  layer("layer:weather-window", "Year-specific weather observations", "atmosphere", "POINT", "time:present", "#7bb8d6", "Synthetic observations; not current conditions, forecasting, or life-safety guidance.", { sourceId: "source:nws-api" }),
  layer("layer:smoke-envelope", "Smoke-envelope demonstration", "atmosphere", "POLYGON", "time:present", "#a88b85", "Synthetic 2D envelope; not current smoke, concentration, transport, or plume height."),
  layer("layer:air-quality", "Air-quality state-machine points", "atmosphere", "POINT", "time:present", "#d49b70", "Synthetic finite states; not monitor data, AQI, concentration, or health advice.", { sourceId: "source:kansas-mesonet" }),
  layer("layer:hazard-context", "Multi-hazard context", "hazards", "POLYGON", "time:present", "#c87768", "Synthetic planning fixture; not an alert, forecast, regulatory determination, or emergency guide.", { sourceId: "source:fema-nfhl" }),
  layer("layer:road-corridors", "Generalized road corridors", "roads_rail_trade", "LINE", "time:modern", "#d8c7a5", "Synthetic linework; not routable and not closure, traffic, ownership, or safety evidence.", { sourceId: "source:kdot", trustState: "GENERALIZED" }),
  layer("layer:rail-study", "Rail-through-time study lines", "roads_rail_trade", "LINE", "time:1900s", "#a89b84", "Synthetic dated study geometry; not an undocumented historic route, active line, train, or schedule.", { sourceId: "source:kdot" }),
  layer("layer:historical-1885", "1885 study-line fixture", "historical_geography", "LINE", "time:1800s", "#d4a15f", "Synthetic edition-control fixture; not a historical route claim.", { sourceId: "source:usgs-htmc", defaultOpacity: 0.58 }),
  layer("layer:historical-1910", "1910 study-line fixture", "historical_geography", "LINE", "time:1900s", "#c18552", "Synthetic edition-control fixture; not a historical route claim.", { sourceId: "source:usgs-htmc", defaultOpacity: 0.58 }),
  layer("layer:protected-context", "Protected-context envelope", "archaeology", "POLYGON", "time:archaeological", "#b97070", "Denied: subject, coordinates, geometry, and reconstruction details are withheld.", { sourceId: "source:kansas-memory", trustState: "DENIED", availability: "DENIED", representation: "CATALOG_ONLY" }),
  layer("layer:people-policy", "Aggregate-only people policy zone", "people_dna_land", "POLYGON", "time:modern", "#b58bb6", "Held: contains no person-level, residence, parcel, tribal-affiliation, or genomic data.", { trustState: "RESTRICTED", availability: "HELD", representation: "CATALOG_ONLY" }),
  layer("layer:diagnostic-grid", "Tile-matrix diagnostic grid", "diagnostics", "GRID", "time:timeless", "#6a9e9a", "Synthetic renderer diagnostic; it makes no geographic or scientific claim.", { defaultOpacity: 0.25 }),
]);

export const EVIDENCE_RECORDS: readonly EvidenceRecord[] = Object.freeze(
  LAYER_RECORDS.map((record) =>
    Object.freeze({
      id: record.evidenceId,
      title: `${record.name} evidence posture`,
      layerId: record.id,
      sourceId: record.sourceId,
      trustState: record.trustState,
      confidence:
        record.availability === "AVAILABLE" ? "BOUNDED" : "NOT_ASSESSED",
      spatialScope: record.scaleLimit,
      temporalScope:
        TEMPORAL_EXTENTS.find((entry) => entry.id === record.temporalExtentId)
          ?.label ?? "Unknown time",
      supports:
        record.availability === "AVAILABLE"
          ? "Interaction, layer-state, temporal-compatibility, and evidence-interface demonstration only."
          : "The visible hold or denial state and its stated reason only.",
      cannotProve: record.warning,
      limitations: Object.freeze([
        record.warning,
        "Map pixels and rendered properties are not evidence authority.",
        "No external source is admitted or activated by this record.",
      ]),
      sensitivity:
        record.availability === "DENIED"
          ? "RESTRICTED; detail withheld"
          : "Public-safe synthetic or generalized fixture",
      policyStatus:
        record.availability === "DENIED"
          ? "DENY"
          : record.availability === "AVAILABLE"
            ? "ALLOW_DEMO"
            : "ABSTAIN",
      evidenceRefs:
        record.availability === "AVAILABLE"
          ? Object.freeze([`kfm:evidence:site-local:${record.id.slice("layer:".length)}`])
          : Object.freeze([]),
    }),
  ),
);

const view = (
  id: string,
  name: string,
  question: string,
  representation: AtlasView["representation"],
  layerIds: readonly string[],
  temporalExtentId: string,
  status: AtlasView["status"],
  statusReason: string,
  mapCamera: AtlasView["camera"] = camera(),
): AtlasView =>
  Object.freeze({
    id,
    name,
    question,
    representation,
    layerIds: Object.freeze([...layerIds]),
    temporalExtentId,
    status,
    statusReason,
    camera: mapCamera,
  });

export const ATLAS_VIEWS: readonly AtlasView[] = Object.freeze([
  view("view:kansas-overview", "Kansas Overview", "Where should this investigation begin?", "2D", ["layer:kansas-frame", "layer:county-locators", "layer:settlements", "layer:river-context", "layer:road-corridors", "layer:rail-study"], "time:modern", "SITE_LOCAL_DEMO", "Bounded site-local orientation; official layer admission remains held."),
  view("view:county-atlas", "County Atlas", "What is present, changing, or missing in a selected county?", "2D", ["layer:kansas-frame", "layer:county-locators", "layer:settlements", "layer:river-context"], "time:modern", "SITE_LOCAL_DEMO", "Synthetic locator exercise only; no county dossier or boundary claim."),
  view("view:terrain-landforms", "Terrain & Landforms", "How does the land rise, drain, and constrain a route?", "TERRAIN_3D", ["layer:physiography", "layer:relative-elevation"], "time:timeless", "DESIGN_DATA_HOLD", "No admitted DEM, vertical datum, terrain source, or numeric sampling path."),
  view("view:living-waters", "Living Waters", "What connects a river, reservoir, gauge, and watershed?", "2D", ["layer:kansas-frame", "layer:river-context", "layer:watershed-storage"], "time:present", "SITE_LOCAL_DEMO", "Generalized river interaction only; observations and watershed artifacts remain held."),
  view("view:weather-window", "Weather Window", "Which observations and forecasts apply to this place and time?", "2D", ["layer:weather-window"], "time:present", "DESIGN_DATA_HOLD", "No admitted observation, radar, alert, or forecast adapter."),
  view("view:smoke-transport", "Smoke Transport", "Where is smoke detected or modeled, and at what height?", "2D", ["layer:smoke-envelope"], "time:present", "DESIGN_DATA_HOLD", "No admitted smoke analysis, model field, wind field, or vertical concentration data."),
  view("view:air-quality", "Air Quality", "What do monitors and reporting areas support?", "2D", ["layer:air-quality"], "time:present", "DESIGN_DATA_HOLD", "No admitted monitor observations, averaging period, or AQI reporting-area artifact."),
  view("view:soil-moisture", "Soil & Moisture", "What soil is mapped here and what moisture is observed?", "2D", ["layer:soil-survey-entry", "layer:agriculture-context"], "time:modern", "DESIGN_DATA_HOLD", "SSURGO edition and observation adapters are not admitted."),
  view("view:rail-through-time", "Rail Through Time", "How did documented rail connections change?", "COMPARE", ["layer:rail-study", "layer:historical-1885", "layer:historical-1910"], "time:1900s", "SITE_LOCAL_DEMO", "Synthetic edition-control study lines only; no historic-route claim.", camera(-98.7, 38.5, 5.8)),
  view("view:roads-access", "Roads & Access", "How do roads connect places and what constraints are documented?", "2D", ["layer:road-corridors"], "time:modern", "DESIGN_DATA_HOLD", "No admitted dated centerline, closure, crossing, or routing graph."),
  view("view:cities-growth", "Cities & Growth", "How did a city's documented extent and built form change?", "COMPARE", ["layer:settlements"], "time:modern", "DESIGN_DATA_HOLD", "No admitted boundary, imagery edition, built-up extent, footprint, or height data."),
  view("view:archaeology", "Archaeology & Cultural Landscapes", "What can be responsibly explained about this landscape's past?", "2D", ["layer:protected-context"], "time:archaeological", "DESIGN_DATA_HOLD", "Protected detail fails closed; public-safe interpretation requires rights, cultural review, evidence, and release."),
  view("view:geology-resources", "Geology & Resources", "Which mapped geology and interpreted sections support an explanation?", "2D", ["layer:physiography", "layer:relative-elevation"], "time:paleozoic", "SITE_LOCAL_DEMO", "Synthetic interaction concepts only; no geologic unit, section, occurrence, reserve, or ownership claim."),
  view("view:agriculture-land-cover", "Agriculture & Land Cover", "How do documented land-cover patterns relate to soil and water?", "COMPARE", ["layer:agriculture-context", "layer:soil-survey-entry", "layer:river-context"], "time:modern", "DESIGN_DATA_HOLD", "No admitted annual classification, quality mask, soil edition, or public aggregate."),
  view("view:habitat-flora-fauna", "Habitat, Flora & Fauna", "What public-safe habitat and observation evidence is available?", "2D", ["layer:prairie-regions", "layer:habitat-connectivity", "layer:fauna-range", "layer:flora-communities"], "time:modern", "SITE_LOCAL_DEMO", "Generalized synthetic concepts only; no occurrence, absence, suitability, or movement claim."),
  view("view:hazards-resilience", "Hazards & Resilience", "Which official hazards, modeled risks, and public assets intersect?", "2D", ["layer:hazard-context"], "time:present", "DESIGN_DATA_HOLD", "No admitted alert, regulatory extent, observed event, model scenario, or public asset layer."),
  view("view:people-places", "People & Places", "What aggregate public evidence supports a place history?", "2D", ["layer:settlements", "layer:people-policy"], "time:modern", "DESIGN_DATA_HOLD", "No person-level, residence, parcel, tribal-affiliation, or genomic data; aggregate source admission remains held."),
  view("view:story-atlas", "Story Atlas", "How can released evidence become a guided, inspectable narrative?", "2D", ["layer:kansas-frame", "layer:river-context", "layer:protected-context"], "time:modern", "SITE_LOCAL_DEMO", "Draft-only four-scene trust demonstration; it grants no access and publishes nothing."),
]);

export function findTemporalExtent(id: string): TemporalExtent | null {
  return TEMPORAL_EXTENTS.find((entry) => entry.id === id) ?? null;
}

export function findLayerRecord(id: string): LayerRecord | null {
  return LAYER_RECORDS.find((entry) => entry.id === id) ?? null;
}

export function findEvidenceRecord(id: string): EvidenceRecord | null {
  return EVIDENCE_RECORDS.find((entry) => entry.id === id) ?? null;
}

export function findEvidenceForLayer(layerId: string): EvidenceRecord | null {
  return EVIDENCE_RECORDS.find((entry) => entry.layerId === layerId) ?? null;
}

export function findSourceDescriptor(id: string): SourceDescriptor | null {
  return SOURCE_DESCRIPTORS.find((entry) => entry.id === id) ?? null;
}

export function findAtlasView(id: string): AtlasView | null {
  return ATLAS_VIEWS.find((entry) => entry.id === id) ?? null;
}

export function createInitialSnapshot(now = new Date()): MapSnapshot {
  const defaultView = ATLAS_VIEWS[0]!;
  return Object.freeze({
    profile: "kfm.explorer.map-snapshot.v1",
    capturedAt: now.toISOString(),
    area: "Kansas statewide generalized fixture extent",
    representation: "2D",
    basemap: "SITE_LOCAL_ATLAS",
    camera: defaultView.camera,
    committedTimeId: defaultView.temporalExtentId,
    activeViewId: defaultView.id,
    layers: Object.freeze(
      LAYER_RECORDS.map((record) =>
        Object.freeze({
          id: record.id,
          visible: record.defaultVisible && record.availability === "AVAILABLE",
          opacity: record.defaultOpacity,
        }),
      ),
    ),
    selectedLayerId: null,
    evidenceRefs: Object.freeze([]),
    publicSafe: true,
    draftOnly: true,
  });
}

export function evaluateFocusSelection(
  layerId: string | null,
  simulateAdapterError = false,
  activeViewId: string | null = null,
): PolicyDecision {
  if (simulateAdapterError) {
    return Object.freeze({ profile: "kfm.explorer.policy-decision.v1", outcome: "ERROR", reasonCode: "DEMO_ADAPTER_ERROR", summary: "The deterministic demonstration adapter failed. No factual fallback was produced.", evidenceRefs: Object.freeze([]), proposedActions: Object.freeze(["Retry the bounded demonstration or inspect diagnostics."]), generated: false });
  }
  if (layerId === null) {
    return Object.freeze({ profile: "kfm.explorer.policy-decision.v1", outcome: "ABSTAIN", reasonCode: "NO_SELECTED_EVIDENCE", summary: "Select an inspectable layer before requesting a bounded interpretation.", evidenceRefs: Object.freeze([]), proposedActions: Object.freeze(["Select an available site-local demonstration layer."]), generated: false });
  }
  const evidence = findEvidenceForLayer(layerId);
  if (evidence === null) {
    return Object.freeze({ profile: "kfm.explorer.policy-decision.v1", outcome: "ERROR", reasonCode: "EVIDENCE_RECORD_NOT_FOUND", summary: "The selected layer has no registered evidence record. No factual fallback was produced.", evidenceRefs: Object.freeze([]), proposedActions: Object.freeze(["Inspect the registry and correct the missing binding."]), generated: false });
  }
  if (evidence.policyStatus === "DENY") {
    return Object.freeze({ profile: "kfm.explorer.policy-decision.v1", outcome: "DENY", reasonCode: "PROTECTED_SPATIAL_DETAIL", summary: "Policy blocks disclosure of the selected detail.", evidenceRefs: Object.freeze([]), proposedActions: Object.freeze(["Use the public-safe generalized context or request authorized review outside this public surface."]), generated: false });
  }
  const activeView = activeViewId === null ? null : findAtlasView(activeViewId);
  if (activeView?.status === "DESIGN_DATA_HOLD") {
    return Object.freeze({ profile: "kfm.explorer.policy-decision.v1", outcome: "ABSTAIN", reasonCode: "VIEW_DATA_HELD", summary: `${activeView.name} remains held: ${activeView.statusReason}`, evidenceRefs: Object.freeze([]), proposedActions: Object.freeze(["Complete the view's source, evidence, review, and release gates before requesting interpretation."]), generated: false });
  }
  if (evidence.policyStatus === "ABSTAIN" || evidence.evidenceRefs.length === 0) {
    return Object.freeze({ profile: "kfm.explorer.policy-decision.v1", outcome: "ABSTAIN", reasonCode: "SOURCE_OR_RELEASE_HELD", summary: "The selected layer is held or lacks evidence eligible for this demonstration.", evidenceRefs: Object.freeze([]), proposedActions: Object.freeze(["Complete the next admission gate shown in Source Observatory."]), generated: false });
  }
  return Object.freeze({ profile: "kfm.explorer.policy-decision.v1", outcome: "ANSWER", reasonCode: "SITE_LOCAL_DEMO_SUPPORTED", summary: "The selected fixture supports interface behavior only. It does not support a Kansas factual claim.", evidenceRefs: evidence.evidenceRefs, proposedActions: Object.freeze(["Add the bounded evidence reference to a draft report or story."]), generated: false });
}
