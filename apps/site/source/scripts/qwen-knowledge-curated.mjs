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
  ]),
  "Aquifers & groundwater": Object.freeze([
    "Relate High Plains aquifer saturated thickness to depth-to-water wells across western Kansas counties.",
    "Compare the alluvial aquifer footprint with Living Waters reaches to discuss surface-groundwater connection (as a question, not a finding).",
    "List which KGS groundwater layers are snapshots and what year each represents before comparing them.",
  ]),
  "Weather & hazards": Object.freeze([
    "Place FEMA declaration counties beside NWS alert history to separate administrative declarations from observed hazards.",
    "Compare long-term lightning climatology with a single storm night to discuss what is typical versus exceptional.",
    "Overlay FEMA flood zones on Living Waters reaches to frame where flood-risk mapping and observed flow meet.",
  ]),
  "Fire, smoke & hazards": Object.freeze([
    "Compare NASA FIRMS detections, NIFC reports, and HMS smoke polygons for one day to show how each sees fire differently.",
    "Use GOES GeoColor timing to discuss when smoke was visible versus when detections were recorded.",
    "Note which Flint Hills burn seasons appear and which detections may be agricultural burning.",
  ]),
  "Roads, rail & movement": Object.freeze([
    "Compare the 1918 KDOT road map with today's network to discuss which corridors persisted.",
    "Relate abandoned rail lines to historic towns and present roads as a settlement-history question.",
    "Contrast historic, old, and closed bridge records along one river crossing.",
  ]),
  "Land records & survey": Object.freeze([
    "Use PLSS townships and sections to explain how the survey grid organizes Kansas land description.",
    "Compare authorized and closed BLM mineral leases as context for subsurface resource history.",
  ]),
  "Geology & hazards": Object.freeze([
    "Compare USGS earthquake locations with Raspberry Shake station coverage to discuss detection limits.",
    "Ask how recent south-central Kansas seismicity is discussed in public sources, keeping causation as an open question.",
  ]),
  "Terrain & landforms": Object.freeze([
    "Use 3DEP hillshade and slope to identify landform regions (High Plains, Flint Hills, Smoky Hills, Red Hills) at overview scale.",
    "Pair slope with Living Waters reaches to discuss valley form without inferring flow values.",
  ]),
  Atmosphere: Object.freeze([
    "Compare forecast wind direction with HMS smoke drift on the same day as a qualitative question.",
  ]),
  "Reference boundaries & locators": Object.freeze([
    "Use county outlines to frame a question by county, then name which sources report at county versus point scale.",
  ]),
});

/** Cross-domain ideas for building KFM itself: gaps the Site could close next. */
export const QWEN_KNOWLEDGE_PROJECT_IDEAS = Object.freeze([
  "Admit a first reviewed EvidenceBundle for one Living Waters reach so the companion can give a cited ANSWER instead of an interpretation.",
  "Write per-source data dictionaries (fields, units, valid ranges) so questions about values can be checked instead of guessed.",
  "Record lineage for each snapshot layer (source vintage, transform, reviewer) so stale and superseded states are explainable.",
  "Add a Kansas place gazetteer at county and town level so questions can name places without precise coordinates.",
  "Collect user questions the companion abstained on, and turn the most common ones into evidence-admission priorities.",
]);
