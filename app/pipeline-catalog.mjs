/** Orchestration metadata only. These bindings grant no acquisition or release authority. */
const lane = (id, title, wave, sourceRef, nextGate) => Object.freeze({
  id, title, wave, sourceRef, nextGate, mode: 'candidate', owner: 'Source and domain review',
  cadence: 'Disabled until a bounded product and review profile are qualified',
});
export const DOMAIN_PIPELINES = Object.freeze([
  lane('soil-survey', 'Soil survey', 2, 'connectors/nrcs-ssurgo', 'Qualify one county, map units, units, rights and validation'),
  lane('crop-editions', 'Crop editions', 2, 'connectors/usda-nass', 'Qualify one dated crop product and comparable editions'),
  lane('station-soil', 'Soil station observations', 2, 'connectors/kansas_mesonet', 'Review access, rate limits, depths, units and source clocks'),
  lane('geology-resources', 'Geology and resources', 2, 'connectors/kgs', 'Pin the exact geology or well product, scale and rights'),
  lane('fauna-occurrences', 'Public-safe wildlife occurrences', 3, 'connectors/fauna', 'Validate dataset rights, taxonomy and sensitive-location generalization'),
  lane('flora-occurrences', 'Public-safe plant occurrences', 3, 'connectors/flora', 'Validate dataset rights, taxonomy and sensitive-location generalization'),
  lane('land-cover', 'Dated land cover', 3, 'connectors/nlcd', 'Qualify product, classification, resolution and edition'),
  lane('outdoor-access', 'Outdoor access references', 3, 'connectors/kdwp', 'Review official access references and regulation editions'),
  lane('historical-archives', 'Historical maps and archives', 4, 'connectors/kansas_memory', 'Bind exact archival editions, dates, attribution and reuse rights'),
  lane('archaeology-context', 'Public-safe archaeological context', 4, 'connectors/archaeology', 'Review sensitivity; exclude protected site locations'),
  lane('tribal-context', 'Authoritative public tribal context', 4, 'docs/domains/people-dna-land', 'Select authoritative public records and review jurisdiction and sensitivity'),
  lane('aviation-reference', 'Airport reference', 5, 'connectors/faa', 'Review the pinned FAA airport edition and normalize; live tracking stays disabled'),
  lane('utility-reference', 'Public utility reference', 5, 'connectors/settlements-infrastructure', 'Qualify public service-area records and infrastructure sensitivity'),
  lane('public-projects', 'Public project records', 5, 'connectors/manual_curation', 'Bind dated agency records and proposal, approval or completion status'),
  lane('economic-editions', 'Aggregate economic statistics', 6, 'connectors/census', 'Review geography, edition, definitions and uncertainty'),
  lane('public-updates', 'Dated public updates', 6, 'connectors/manual_curation', 'Select official records and distinguish publication date from event date'),
  lane('cultural-records', 'Cultural events and stories', 6, 'connectors/manual_curation', 'Review attribution, event dates, expiry and reuse rights'),
]);
export const TOPIC_PIPELINES = Object.freeze({
  engineering: ['utility-reference', 'public-projects'], transport: ['aviation-reference'], weather: [], disaster: [], water: [],
  groundwater: ['geology-resources'], geology: ['geology-resources'], terrain: [], ecology: ['flora-occurrences', 'fauna-occurrences', 'land-cover', 'outdoor-access'],
  agriculture: ['soil-survey', 'crop-editions', 'station-soil'], history: ['historical-archives', 'archaeology-context'],
  land: ['soil-survey', 'land-cover'], people: ['economic-editions', 'tribal-context', 'cultural-records', 'public-updates'], aviation: ['aviation-reference'], flora: ['flora-occurrences', 'land-cover'], fauna: ['fauna-occurrences', 'outdoor-access'],
  government: ['public-projects', 'economic-editions'], 'public-safety': ['public-updates'], places: [], science: [], sky: [], evidence: [],
});
// Scheduling remains source/product based, never one job per card.
export const PC_CAPTURE_IDS = Object.freeze(['usgs-streamflow', 'nws-alerts', 'usgs-earthquakes']);
for (const map of [TOPIC_PIPELINES]) for (const value of Object.values(map)) Object.freeze(value);
