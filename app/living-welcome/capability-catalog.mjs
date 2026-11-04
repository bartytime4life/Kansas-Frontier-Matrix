import { MAP_DEMOS } from './map-demos.mjs';
// Presentation references only; each reused capture keeps its original scope.
const selections = {
 weather: ['weather'], water: ['rivers'], groundwater: ['underground'],
 geology: [null, 'No verified earthquake footage is available. The live preview visits individual KGS well, core and mine records. Open Underground for source records and available intervals; no continuous geology is claimed.'],
 terrain: ['science'], ecology: ['farming', 'Aerial land-cover context; no species inventory.'],
 flora: [null, 'The preview draws NLCD 2021 land-cover classes. Open the map for annual plant-record hexagons and crop layers; no verified Flora recording is connected.'],
 fauna: [null, 'No verified wildlife capture is connected. The preview maps coarse GBIF Animalia records for 2025; exact occurrence sites stay withheld.'],
 'public-safety': [null, 'No crime, court or emergency-response capture is connected. The preview maps generalized community-reported ALPR areas, not incidents or a safety score.'],
 agriculture: ['farming'], history: ['history'], transport: ['transport'],
 engineering: ['transport', 'Bridge inventory and transport context; not engineering analysis.'],
 land: ['government', 'County and survey reference context; not ownership evidence.'],
 people: ['government', 'Aggregate county geography; not individual people.'], places: ['government'],
 science: [null, 'Preview the newest available dated NOAA satellite frame. No verified satellite capture is available yet.'], disaster: ['weather', 'Weather context only; not a hazard reconstruction or warning.'],
 aviation: [null, 'Preview only the pinned FAA airspace zones in 3D, a flat chart or an altitude slice. No verified aviation capture is available yet.'],
 government: ['government', 'County and city reference geography; not legal boundaries or office records.'],
 sky: [null, 'Use Sky tools for calculated daylight and solar geometry. No verified sky animation is available yet.'],
 evidence: [null, 'Open the source catalogue to inspect provenance, dates and limitations. No verified workflow animation is available yet.'],
};
export function capabilityPreviews(topic) {
 const [category, context] = selections[topic] || [];
 return (MAP_DEMOS[category] || []).map(demo => ({ ...demo,
  animation: demo.src.replace('/demos/', '/animations/').replace('.webm', '.webp'),
  context: context || null,
 }));
}
export function capabilityNote(topic) { return selections[topic]?.[1] || ''; }

// Welcome presentation only. The category map and its source controls still own
// layer selection, source clocks and availability; these descriptions admit nothing.
const glimpses = {
 flora: ['Read plants at two scales', 'NLCD 2021 land-cover classes at 30 m show forests, grassland, crops and wetlands across real Flint Hills aerial imagery and terrain.', 'Open the map, inspect a land-cover cell, then compare annual GBIF plant-record hexagons.', 'Cover classes do not identify species. Record density is not abundance or absence; exact plant sites are withheld.'],
 fauna: ['Map real animal records', 'GBIF Animalia occurrence records from 2025 appear as coarse density hexagons over a labelled Kansas map.', 'Read the geographic pattern, then use the Observatory to compare other annual aggregates.', 'Records include observations and specimens. Density is not abundance, absence, migration or habitat. Source zoom is capped at six; exact sites stay withheld.'],
 'public-safety': ['Locate reported ALPR areas', 'Generalized DeFlock / OpenStreetMap report cells appear over Wichita, with mapped report counts.', 'Compare the cells with roads and towns; exact locations remain withheld.', 'Cells are 0.05° areas, not camera coverage. Reports do not verify devices or current operation. No crime, court or emergency feed; blank areas do not establish safety.'],
 engineering: ['Crossings in the landscape', 'Bridge inventory points sit against real river valleys and terrain.', 'Look for crossings near the Big Blue and Kansas rivers.', 'Open the map to inspect a bridge record or draw a terrain profile.'],
 transport: ['Follow roads and rail', 'KDOT highway and active-rail layers meet around Wichita.', 'Compare the road and railway lines as the map settles.', 'Reference networks do not show live vehicles, closures or access.'],
 aviation: ['Explore the airspace zones', 'See the FAA airspace zones around Wichita, without the extra airport and airway overlays.', 'Compare the stacked zones with the flat chart and an altitude slice.', 'Open the aviation map for point inspection, side views, weather, traffic and separately dated drone/TFR context. Display only; not for navigation.'],
 weather: ['A scan, not a moving illustration', 'Current NOAA radar and NWS alert areas share a dark map.', 'Read the scan time; an unavailable or stale scan stays absent.', 'Open the map for the dated radar loop and individual alert records.'],
 disaster: ['Separate the hazard clocks', 'Alert areas, satellite fire detections and incident reports keep their own sources.', 'Compare the symbols without treating nearby records as the same event.', 'An empty or unavailable feed is not an all-clear; this is not emergency guidance.'],
 water: ['Trace the river network', 'Published USGS/NRCS watershed boundaries appear over the river and lake network.', 'Compare drainage boundaries, then open River Pulse for separately dated gauge samples.', 'WBD is legacy reference geography. Live gauge samples and River Pulse load in the opened map, not on a category hover.'],
 groundwater: ['See aquifer thickness', 'KGS regional saturated-thickness classes appear over western Kansas.', 'Compare the mapped colour classes across the High Plains.', '2022–2024 estimates are regional context, not a present-day well or parcel measurement.'],
 geology: ['Explore recorded subsurface sites', 'Recorded wells, cores and mines connect individual source records with their locations.', 'Follow a recorded site, then open Underground to inspect its original records and available intervals.', 'Individual observations do not form a continuous underground model. Display widths are illustrative; conditions between records are unknown. Earthquakes and terrain are separate context.'],
 terrain: ['Read light across the land', 'A real elevation model reveals slopes and valleys as the view turns.', 'Look at the western Kansas relief rather than decorative mountains.', 'Welcome terrain is displayed at 1.5× vertical scale; open a profile for unexaggerated display elevations.'],
 ecology: ['Landscape and drainage', 'NLCD 2021 land-cover classes and published watershed boundaries follow the Big Blue River landscape on imagery and terrain.', 'Compare classified forest, grassland, crops and water corridors.', 'Land-cover classification is not a habitat model or a species inventory. Watershed boundaries are legacy reference geography.'],
 agriculture: ['Fields at aerial scale', 'The dated USDA NASS Cropland Data Layer draws classified crop cells over Kansas aerial imagery.', 'Compare the crop classes at field scale, then open the map to inspect a cell or outline an area.', 'Crop classes are dated satellite classifications. NASA soil moisture is a separate 9 km model layer, not a measurement of the pictured field.'],
 history: ['Two dates in one view', 'KDOT 1918 road references and abandoned rail sit over a modern atlas base.', 'Compare the dated routes with present-day towns and geography.', 'The basemap does not reconstruct the landscape of 1918 or establish public access.'],
 land: ['Find the survey pattern', 'BLM PLSS township and section references reveal the survey grid over Kansas 2024 aerial imagery.', 'Read the township pattern near the Sixth Principal Meridian.', 'Survey references are not ownership, exact parcel boundaries or access rights.'],
 people: ['County population in relief', 'County columns encode 2020 Census people per square mile of land.', 'Compare aggregate density rather than interpreting height as terrain.', 'The column heights are a thematic display; the 2020 baseline is not a current population estimate.'],
 government: ['Four districts. One Kansas.', 'See the Census’s four Kansas U.S. House districts for the 119th Congress (2025–2027), with distinct colors and district labels.', 'Compare the present shapes here; open the map to explore congressional plans back to Kansas statehood in 1861.', 'January 1, 2025 generalized boundaries. Colors are not parties; this does not determine your ballot, officeholder or polling place.'],
 places: ['Counties meet watersheds', 'County boundaries and closer-scale drainage units provide two ways to locate a question.', 'Start with a county; zoom in to compare the watershed reference.', 'These separate boundary systems do not establish a causal relationship.'],
 science: ['A dated view from orbit', 'The newest current NOAA GOES catalog frame is previewed when available.', 'Look for its scan time and product label, including a visible-band fallback.', 'Cloud appearance is visual context, not a surface measurement or a forecast.'],
 sky: ['Kansas on the globe', 'Calculated current daylight and twilight bands follow the existing globe view.', 'Read the calculation time, then open the Sky tools to explore solar geometry through time.', 'Solar geometry is calculated; no live cloud or star observation is claimed here.'],
 evidence: ['Follow the source trail', '2020 Census county source geography supplies a real reference layer for inspecting source, time and limitations.', 'Open the map and select a mapped feature to inspect its source context.', 'Provider context and recorded tours are separate from released KFM evidence.'],
};
export function categoryGlimpse(topic) {
 const entry = Object.hasOwn(glimpses, topic) ? glimpses[topic] : null;
 return entry ? { title: entry[0], summary: entry[1], try: entry[2], limit: entry[3] } : null;
}
