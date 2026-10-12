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
 * bridge offers one when every named domain is among the relevant sources.
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
