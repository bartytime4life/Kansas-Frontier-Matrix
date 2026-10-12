/**
 * Hand-curated half of the local Qwen knowledge pack.
 *
 * The other half (source metadata) is generated from the Site's own source
 * registries by scripts/build-qwen-knowledge-pack.mjs, so registry facts are
 * never retyped here. This file carries vocabulary, operating principles and
 * per-domain investigation ideas: metadata that tells the model what KFM terms
 * mean and which questions are worth asking, without supplying any evidence.
 */

export const QWEN_KNOWLEDGE_PRINCIPLES = Object.freeze([
  "KFM (Kansas Frontier Matrix) is an evidence-first map and archive of Kansas land, water, weather, hazards, infrastructure, and history.",
  "A map layer, tile, color, label, or model sentence is a context carrier, not evidence. Only a released, reviewed EvidenceBundle cited by an exact EvidenceRef supports a claim.",
  "Official external sources (USGS, NOAA, NASA, FEMA, BLM, KDOT, KGS, Census) are EXTERNAL_CONTEXT_ONLY in this Site: useful for orientation and comparison, never admitted KFM records.",
  "Every source has a boundary: what it is NOT. Respect it. A FEMA declaration is not a disaster footprint; a PLSS section is not ownership; streamflow is not flood guidance.",
  "Missing data is a gap, never a zero, an all-clear, or a negative finding.",
  "Keep observation (what the supplied context shows), inference (what it may suggest), and unknowns (what would be needed) visibly separate.",
  "Sensitive places (archaeology, rare species, living people, critical infrastructure detail) are generalized or withheld; never estimate or restore protected precision.",
  "Release, review, and publication state change only through governed review; model language cannot change them.",
]);

export const QWEN_KNOWLEDGE_GLOSSARY = Object.freeze({
  outcomes: Object.freeze({
    ANSWER: "Released, policy-safe, citation-valid support exists for the bounded question.",
    ABSTAIN: "Support is missing, stale, conflicted, unresolved, or outside scope; explain the limit instead of guessing.",
    DENY: "Rights, sensitivity, release state, or exposure risk blocks the request.",
    ERROR: "A resolver, validator, adapter, or runtime failed; never fall back to an unsupported answer.",
  }),
  evidenceStates: Object.freeze({
    ANSWER: "The feature resolves to supporting evidence.",
    CORRECTED: "Supported, with a first-class correction applied.",
    MISSING_EVIDENCE: "No EvidenceBundle supports the feature yet.",
    SOURCE_STALE: "The supporting source no longer meets freshness requirements.",
    GENERALIZED_GEOMETRY: "Geometry was deliberately coarsened for public safety.",
    RESTRICTED_ACCESS: "A bounded audience or obligation applies; details are withheld.",
    DENIED_BY_POLICY: "Policy blocks exposure; details are withheld.",
    SUPERSEDED: "A newer governed object or release replaces this one.",
    ERROR: "Evidence resolution failed.",
  }),
  releaseStates: Object.freeze({
    RELEASED: "Passed review and published for public use.",
    DEMONSTRATION: "Illustrative or synthetic fixture; never operational data.",
    GENERALIZED: "Public release with reduced precision.",
    RESTRICTED: "Not for public exposure.",
  }),
  publicStatus: Object.freeze({
    PUBLIC_SAFE: "Safe to show at its declared precision.",
    GENERALIZED: "Shown only after precision reduction.",
    RESTRICTED: "Not shown publicly.",
  }),
  evidenceRoles: Object.freeze({
    EXTERNAL_CONTEXT_ONLY: "Official provider data shown for context; not a KFM record, report claim, or export evidence.",
    DISPLAY_CONTEXT_ONLY: "Basemap or terrain carrier used for visual orientation and attribution only.",
    SITE_LOCAL_REDACTED_DIAGNOSTIC: "Browser health telemetry with locations and identifiers removed.",
  }),
  terms: Object.freeze({
    EvidenceBundle: "A content-addressed package of sources, transforms, and review that supports a claim.",
    EvidenceRef: "An exact kfm: identifier pointing to one EvidenceBundle; it must never be invented or transformed.",
    "Trust membrane": "The Governed API boundary; clients never read canonical or sensitive stores directly.",
    PLSS: "Public Land Survey System townships and sections; a survey reference grid, not parcels or ownership.",
    HUC: "USGS Hydrologic Unit Code watershed boundary at a stated level.",
    NWM: "NOAA National Water Model; modeled, not observed, streamflow.",
    "3DHP": "USGS 3D Hydrography Program flowlines with downstream topology.",
    "3DEP": "USGS 3D Elevation Program terrain products.",
    HMS: "NOAA Hazard Mapping System analyst smoke polygons.",
    FIRMS: "NASA Fire Information for Resource Management System satellite thermal detections.",
    "Visual transition": "A color blend between two exact image frames; it is not a numeric estimate.",
    Admission: "The reviewed step that turns a source record into a KFM record; display on the map is not admission.",
    Provenance: "Where a record came from and how it was transformed; KFM keeps it with the record.",
    Snapshot: "A layer captured at one date or vintage; it does not update with the live source.",
    "Operational feed": "A layer fetched from the provider on request; it reflects the provider's latest data and its delays.",
    Interpretation: "Companion model language attached to an ABSTAIN; never evidence, never citable.",
  }),
  sourceKinds: Object.freeze({
    SNAPSHOT_GEOJSON: "Vector features captured at a stated date or vintage.",
    OPERATIONAL_GEOJSON: "Vector features fetched from the provider on request.",
    OPERATIONAL_WMS: "Map images rendered by the provider's service; pixels, not features.",
    HISTORICAL_RASTER: "Archived image tiles for a past period.",
    MODEL_CANVAS: "Model output drawn as an image; modeled, not observed.",
    VECTOR_STYLE: "Basemap vector style used for orientation.",
    RASTER_BASEMAP: "Basemap image tiles used for orientation.",
    RASTER_DEM: "Elevation tiles used to shape 3D terrain.",
  }),
  connectionStates: Object.freeze({
    idle: "Not requested yet.",
    loading: "Request in progress.",
    ready: "Data returned and drawn.",
    empty: "The provider returned no features for this view or time; not a negative finding.",
    partial: "Some data returned; part is missing or capped.",
    error: "The request failed; nothing from this source is shown.",
  }),
  contextFields: Object.freeze({
    "camera.locationRedacted": "true when a device-location view was replaced with the Kansas overview.",
    "camera.representation": "How the map is drawn (2D, globe, 3D terrain).",
    "time.label": "The timeline frame or window the user selected.",
    "officialSources.selected": "The user switched the source on.",
    "officialSources.displayed": "The source is actually drawn at the current time frame; selected but not displayed means held.",
    "officialSources.featureCount": "Features returned for the current request, which may be capped.",
    "officialSources.retrievedAt": "When the Site fetched the data; not when the provider observed it.",
    "nearbyContext.distanceMiles": "Rounded distance from the selection; never a precise location.",
    telemetry: "Redacted browser health; it describes the Site, not the world.",
  }),
});

/**
 * Technical terms per source domain. The bridge sends a domain's terms only
 * when that domain is relevant to the question or the map, like the ideas.
 */
export const QWEN_KNOWLEDGE_DOMAIN_TERMS = Object.freeze({
  "Living waters": Object.freeze({
    Discharge: "Volume of water passing a gauge per unit time, reported by USGS in cubic feet per second (cfs).",
    "Gage height": "Water-surface height at a gauge above that gauge's own datum; also called stage. It is not water depth and is not comparable between gauges.",
    "Provisional data": "Recent USGS values that have not been reviewed and may be revised or removed.",
    "Flood stage": "The NWS stage at a forecast point where flooding begins to affect nearby areas; set separately for each location.",
    Reach: "A stretch of stream between two points, such as between confluences.",
    "NWM analysis": "The National Water Model's estimate of current flow on each reach; modeled, not measured.",
    "NWM short-range forecast": "National Water Model flow forecast for the next 18 hours.",
  }),
  "Aquifers & groundwater": Object.freeze({
    Aquifer: "Rock or sediment that stores and yields usable groundwater.",
    "High Plains aquifer": "Regional aquifer beneath western and central Kansas; the Ogallala Formation is its main part.",
    "Saturated thickness": "Vertical thickness of the part of an aquifer filled with water.",
    "Depth to water": "Distance from the land surface down to the water level in a well.",
    "Water table": "The top of the saturated zone in an unconfined aquifer.",
    "Alluvial aquifer": "Water-bearing sand and gravel deposited along river valleys.",
    "Monitoring well": "A well measured on a schedule to track water levels; one well describes one point.",
  }),
  "Weather & hazards": Object.freeze({
    Warning: "NWS product: a hazard is occurring or imminent.",
    Watch: "NWS product: conditions are favorable for a hazard to develop.",
    Advisory: "NWS product: a less serious hazard that still needs caution.",
    Reflectivity: "Radar energy returned from precipitation, in dBZ; higher usually means heavier rain or hail. It is not a rainfall total.",
    "Lightning flash density": "Number of lightning flashes per area per period, such as per square kilometer per year.",
    "Disaster declaration": "A federal declaration for designated counties that enables FEMA assistance; it is not a map of damage.",
    "Special Flood Hazard Area": "FEMA zones (A, AE and similar) with a 1% or greater annual flood chance, the \"100-year\" floodplain.",
  }),
  "Fire, smoke & hazards": Object.freeze({
    "Active fire detection": "A satellite pixel markedly hotter than its surroundings; VIIRS pixels are about 375 m and MODIS about 1 km.",
    "Fire radiative power": "Heat energy released by a detected fire, in megawatts; it indicates intensity, not area burned.",
    "Smoke polygon": "HMS analyst-drawn smoke extent from satellite imagery, labeled light, medium or heavy; not ground-level air quality.",
    "Prescribed burn": "A planned, managed fire, common in Flint Hills grasslands in spring.",
    GeoColor: "GOES imagery that looks like true color by day and uses infrared at night.",
    Incident: "A reported wildland fire tracked by an agency, with its own name, size and dates.",
  }),
  "Roads, rail & movement": Object.freeze({
    KDOT: "Kansas Department of Transportation, publisher of the road, rail and bridge layers.",
    "Abandoned rail line": "A line where service ended and track was removed or left unused; some became trails.",
    "Active rail line": "A line currently in rail service.",
    "Bridge record": "An inventory entry describing a structure; it is not a current condition or load rating.",
    "1918 road map": "A historical state road map; its routes show that era, not today's network.",
  }),
  "Land records & survey": Object.freeze({
    Township: "A PLSS square about six miles on a side containing 36 sections, numbered north or south of a baseline.",
    Range: "A column of townships numbered east or west of a principal meridian.",
    Section: "A PLSS unit of about one square mile (640 acres).",
    "Sixth Principal Meridian": "The north-south survey line Kansas townships and ranges are counted from; its baseline is the Kansas-Nebraska border.",
    MLRS: "BLM Mineral and Land Records System, source of the lease layers.",
    "Federal mineral lease": "A BLM authorization to develop federally owned minerals; surface ownership may differ.",
  }),
  "Geology & hazards": Object.freeze({
    Magnitude: "Logarithmic measure of earthquake size; each whole step is about 32 times more energy.",
    Depth: "Estimated depth of the earthquake's origin below the surface.",
    ComCat: "USGS Comprehensive Earthquake Catalog, source of the earthquake layer.",
    "Raspberry Shake": "A network of low-cost seismographs run largely by volunteers.",
    "Felt report": "A public report that shaking was felt; different from an instrument detection.",
  }),
  "Terrain & landforms": Object.freeze({
    DEM: "Digital elevation model: a grid of ground heights.",
    Hillshade: "Shaded relief computed from a DEM for one chosen sun direction and angle.",
    Slope: "Steepness of the ground, in degrees or percent.",
    Lidar: "Laser surveying used for most 3DEP elevation data.",
    Escarpment: "A long, steep slope separating two flatter surfaces.",
  }),
  Atmosphere: Object.freeze({
    "Wind direction": "The direction the wind blows from; a south wind blows toward the north.",
    "Valid time": "The time a forecast applies to, distinct from when it was issued.",
    Gust: "A brief burst of wind above the sustained speed.",
    "Sustained wind": "Wind speed averaged over a short period.",
  }),
  "Reference boundaries & locators": Object.freeze({
    "FIPS code": "Federal numeric code for a state or county; Kansas is 20.",
    "Census vintage": "The year of the Census geography; county lines and names can change between vintages.",
    "County seat": "The town where county government sits.",
  }),
});

/**
 * Per-domain prompts for exploration. They are questions, not findings: each
 * names the sources to compare and the gate that would have to pass before
 * the comparison could become a KFM claim.
 */
export const QWEN_KNOWLEDGE_DOMAIN_IDEAS = Object.freeze({
  "Living waters": Object.freeze([
    "Compare observed USGS River Pulse gauges with NOAA National Water Model analysis on the same reach to see where modeled and observed flow disagree.",
    "Trace a selected reach downstream through USGS 3DHP flowlines and list which gauges and HUC watersheds it crosses.",
    "Ask which watersheds have no active gauge, so gaps are explicit before any statewide reading.",
    "Contrast NWPS forecast stage locations with gauges that report only discharge.",
    "Compare upstream and downstream Arkansas River gauges to ask where flow is lost along the reach, leaving the cause as an open question.",
    "Set the NWM short-range forecast beside the latest observed River Pulse frame and name which one is a model and which an observation.",
  ]),
  "Aquifers & groundwater": Object.freeze([
    "Relate High Plains aquifer saturated thickness to depth-to-water wells across western Kansas counties.",
    "Compare the alluvial aquifer footprint with Living Waters reaches to discuss surface-groundwater connection (as a question, not a finding).",
    "List which KGS groundwater layers are snapshots and what year each represents before comparing them.",
    "Find where thin saturated thickness and deep water levels coincide, and ask what a later snapshot would need to show before calling it a trend.",
    "Name which counties sit over more than one aquifer system, such as the Dakota beneath the High Plains, to frame layered-groundwater questions.",
    "Check how evenly KGS monitoring wells cover each aquifer before reading any regional pattern from them.",
  ]),
  "Weather & hazards": Object.freeze([
    "Place FEMA declaration counties beside NWS alert history to separate administrative declarations from observed hazards.",
    "Compare long-term lightning climatology with a single storm night to discuss what is typical versus exceptional.",
    "Overlay FEMA flood zones on Living Waters reaches to frame where flood-risk mapping and observed flow meet.",
    "Compare lightning density in western and eastern Kansas and ask what the climatology period does and does not cover.",
    "Note where FEMA flood-zone mapping is absent, and say plainly that unmapped does not mean no flood risk.",
    "Use NWS radar frame times beside alert issue times to discuss timing as a question, not a verification of any warning.",
  ]),
  "Fire, smoke & hazards": Object.freeze([
    "Compare NASA FIRMS detections, NIFC reports, and HMS smoke polygons for one day to show how each sees fire differently.",
    "Use GOES GeoColor timing to discuss when smoke was visible versus when detections were recorded.",
    "Note which Flint Hills burn seasons appear and which detections may be agricultural burning.",
    "Compare spring Flint Hills detections with HMS smoke reaching eastern Kansas cities, keeping air quality outside what these sources measure.",
    "Ask how cloud cover or satellite overpass timing could hide fires on a given day before reading an empty map as no fire.",
    "Count detections that have no matching NIFC incident report, and explain why a thermal detection is not necessarily a wildfire.",
  ]),
  "Roads, rail & movement": Object.freeze([
    "Compare the 1918 KDOT road map with today's network to discuss which corridors persisted.",
    "Relate abandoned rail lines to historic towns and present roads as a settlement-history question.",
    "Contrast historic, old, and closed bridge records along one river crossing.",
    "Trace a 1918 road beside an abandoned rail line to ask how towns connected before the interstate era.",
    "Compare active rail density in western and eastern Kansas and ask what agriculture and settlement history might explain, as questions.",
    "List closed bridges on local roads and ask what crossing gaps they leave, without asserting current detours.",
  ]),
  "Land records & survey": Object.freeze([
    "Use PLSS townships and sections to explain how the survey grid organizes Kansas land description.",
    "Compare authorized and closed BLM mineral leases as context for subsurface resource history.",
    "Explain how Kansas township and range numbers count from the Sixth Principal Meridian and its baseline.",
    "Ask why BLM lease records are sparse in Kansas, where most land and minerals are privately held, before reading the map as complete.",
    "Use section-scale PLSS references to describe where non-sensitive layers sit without giving coordinates.",
    "Compare lease activity periods with today's authorized leases to discuss how mineral interest shifted over time.",
  ]),
  "Geology & hazards": Object.freeze([
    "Compare USGS earthquake locations with Raspberry Shake station coverage to discuss detection limits.",
    "Ask how recent south-central Kansas seismicity is discussed in public sources, keeping causation as an open question.",
    "Compare reported depths and magnitudes to discuss which small events are likely to be felt and which are only instrument-recorded.",
    "Look for Raspberry Shake coverage gaps in western Kansas and ask what magnitude might go unrecorded there.",
    "Place Kansas events beside nearby activity across the Oklahoma border as regional context, not a shared cause.",
    "Separate catalog events from felt reports: ask which source each map mark comes from.",
  ]),
  "Terrain & landforms": Object.freeze([
    "Use 3DEP hillshade and slope to identify landform regions (High Plains, Flint Hills, Smoky Hills, Red Hills) at overview scale.",
    "Pair slope with Living Waters reaches to discuss valley form without inferring flow values.",
    "Find the Flint Hills and Smoky Hills edges on the slope layer and ask how they compare with the flatter High Plains surface.",
    "Compare valley width on hillshade between the Kansas River and the upper Arkansas River.",
    "Look for steep slopes beside river reaches to frame erosion or sediment questions, not hazard findings.",
    "Ask where hillshade sun angle could make a landform look sharper or flatter than it is.",
  ]),
  Atmosphere: Object.freeze([
    "Compare forecast wind direction with HMS smoke drift on the same day as a qualitative question.",
    "Compare forecast wind speed across Kansas on a windy spring day, keeping forecast frames separate from observations.",
    "Ask how the forecast time and the selected map time differ before reading wind arrows as current conditions.",
    "Set forecast wind beside NIFC fire reports to discuss wind as context while never inferring fire spread.",
    "Compare wind patterns in western and eastern Kansas across several forecast frames as an orientation exercise.",
    "Pair forecast wind with lightning climatology to discuss storm-season context, not a storm forecast.",
  ]),
  "Reference boundaries & locators": Object.freeze([
    "Use county outlines to frame a question by county, then name which sources report at county versus point scale.",
    "Compare county population with the count of FEMA declarations as context, not a risk statistic.",
    "Group counties into western, central, and eastern Kansas to frame regional comparisons across other layers.",
    "Count which sources report by county and which by point or polygon before combining them.",
    "Note that county outlines are 2020 Census geography and ask how boundaries differed for historical questions.",
    "Use a county as the unit for a follow-up question when a point location would be too precise.",
  ]),
});

/**
 * Ideas that only make sense when two domains are in view together. The
 * bridge offers one only when the map is displaying a source from each named
 * domain; a question that merely mentions a domain does not qualify.
 */
export const QWEN_KNOWLEDGE_CROSS_DOMAIN_IDEAS = Object.freeze([
  Object.freeze({ domains: Object.freeze(["Living waters", "Aquifers & groundwater"]), idea: "Compare gauged reaches with the alluvial and High Plains aquifer extents to ask where rivers and groundwater may interact, leaving the connection unproven." }),
  Object.freeze({ domains: Object.freeze(["Living waters", "Roads, rail & movement"]), idea: "List bridges that cross gauged reaches and ask which crossings have river observations nearby." }),
  Object.freeze({ domains: Object.freeze(["Living waters", "Weather & hazards"]), idea: "Set NWS alert timing beside River Pulse observations on the same reach to discuss rainfall and river response as a question." }),
  Object.freeze({ domains: Object.freeze(["Living waters", "Terrain & landforms"]), idea: "Follow a 3DHP flowline across the slope layer to describe the valley it runs through without estimating flow." }),
  Object.freeze({ domains: Object.freeze(["Fire, smoke & hazards", "Atmosphere"]), idea: "Compare HMS smoke direction with forecast wind on the same day, keeping smoke observation and wind forecast separate." }),
  Object.freeze({ domains: Object.freeze(["Roads, rail & movement", "Weather & hazards"]), idea: "Find closed or old bridges inside FEMA flood zones and ask what the records say about their history, not their condition." }),
  Object.freeze({ domains: Object.freeze(["Land records & survey", "Aquifers & groundwater"]), idea: "Compare BLM mineral lease areas with aquifer extents to frame subsurface-resource questions without implying impact." }),
  Object.freeze({ domains: Object.freeze(["Geology & hazards", "Reference boundaries & locators"]), idea: "Count earthquakes per county as orientation, then name the station-coverage limits that shape those counts." }),
  Object.freeze({ domains: Object.freeze(["Roads, rail & movement", "Terrain & landforms"]), idea: "Compare where 1918 roads and rail lines follow valleys or ridges on hillshade, as a route-history question." }),
]);

/** Cross-domain ideas for building KFM itself: gaps the Site could close next. */
export const QWEN_KNOWLEDGE_PROJECT_IDEAS = Object.freeze([
  "Admit a first reviewed EvidenceBundle for one Living Waters reach so the companion can give a cited ANSWER instead of an interpretation.",
  "Write per-source data dictionaries (fields, units, valid ranges) so questions about values can be checked instead of guessed.",
  "Record lineage for each snapshot layer (source vintage, transform, reviewer) so stale and superseded states are explainable.",
  "Add a Kansas place gazetteer at county and town level so questions can name places without precise coordinates.",
  "Collect user questions the companion abstained on, and turn the most common ones into evidence-admission priorities.",
  "Build a small benchmark of map questions with expected outcomes to measure the companion after model or prompt changes.",
  "Record license and reuse terms per source so exports and reports can state them without guessing.",
  "Add historical county boundaries so time-aware questions use the geography of their own year.",
  "Summarize companion receipts by reason code to see which evidence gaps users hit most often.",
]);
