import { MAP_DEMOS } from './map-demos.mjs';
// Presentation references only; each reused capture keeps its original scope.
const selections = {
 weather: ['weather'], water: ['rivers'], groundwater: ['underground'],
 geology: [null, 'Lift a symbolic surface plate to read one original KGS well log. The full map retains earthquake context and Underground tools; no earthquake footage or continuous geology is claimed.'],
 terrain: ['science'], ecology: ['farming', 'Aerial land-cover context; no species inventory.'],
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
 engineering: ['Crossings in the landscape', 'Bridge inventory points sit against real river valleys and terrain.', 'Look for crossings near the Big Blue and Kansas rivers.', 'Open the map to inspect a bridge record or draw a terrain profile.'],
 transport: ['Follow roads and rail', 'KDOT highway and active-rail layers meet around Wichita.', 'Compare the road and railway lines as the map settles.', 'Reference networks do not show live vehicles, closures or access.'],
 aviation: ['Explore the airspace zones', 'See the FAA airspace zones around Wichita, without the extra airport and airway overlays.', 'Compare the stacked zones with the flat chart and an altitude slice.', 'Open the aviation map for point inspection, side views, weather, traffic and separately dated drone/TFR context. Display only; not for navigation.'],
 weather: ['A scan, not a moving illustration', 'Current NOAA radar and NWS alert areas share a dark map.', 'Read the scan time; an unavailable or stale scan stays absent.', 'Open the map for the dated radar loop and individual alert records.'],
 disaster: ['Separate the hazard clocks', 'Alert areas, satellite fire detections and incident reports keep their own sources.', 'Compare the symbols without treating nearby records as the same event.', 'An empty or unavailable feed is not an all-clear; this is not emergency guidance.'],
 water: ['Trace the river network', 'Waterways and lakes stand out on the hydrographic base.', 'Follow a river, then watch a recorded Explorer tour below.', 'Live gauge samples and River Pulse load in the opened map, not on a category hover.'],
 groundwater: ['See aquifer thickness', 'KGS regional saturated-thickness classes appear over western Kansas.', 'Compare the mapped colour classes across the High Plains.', '2022–2024 estimates are regional context, not a present-day well or parcel measurement.'],
 geology: ['Lift the map. Read one real log.', 'A surface-reference plate opens onto one recorded KGS well column, from soil through clay to shale.', 'Lift or return the surface; open Underground to inspect original intervals and other recorded wells.', 'One 2024 log, 0–60 ft below local land surface. Width is illustrative; unknown between observations. Earthquakes and terrain remain separate context in the opened map.'],
 terrain: ['Read light across the land', 'A real elevation model reveals slopes and valleys as the view turns.', 'Look at the western Kansas relief rather than decorative mountains.', 'Welcome terrain is displayed at 1.5× vertical scale; open a profile for unexaggerated display elevations.'],
 ecology: ['Landscape and drainage', 'Satellite imagery supplies landscape context; watershed boundaries appear at closer scales.', 'Look for vegetation, fields and water corridors by eye.', 'Imagery is not a classified habitat map or a species inventory.'],
 agriculture: ['Fields at aerial scale', 'Kansas 2024 aerial imagery reveals actual field and pivot patterns.', 'Look at field geometry, then open the map to outline an area.', 'NASA soil moisture is a separate 9 km model layer, not a measurement of the pictured field.'],
 history: ['Two dates in one view', 'KDOT 1918 road references and abandoned rail sit over a modern atlas base.', 'Compare the dated routes with present-day towns and geography.', 'The basemap does not reconstruct the landscape of 1918 or establish public access.'],
 land: ['Find the survey pattern', 'BLM PLSS township references reveal the survey grid.', 'Read the township pattern near the Sixth Principal Meridian.', 'Survey references are not ownership, exact parcel boundaries or access rights.'],
 people: ['County population in relief', 'County columns encode 2020 Census people per square mile of land.', 'Compare aggregate density rather than interpreting height as terrain.', 'The column heights are a thematic display; the 2020 baseline is not a current population estimate.'],
 government: ['Four districts. One Kansas.', 'See the Census’s four Kansas U.S. House districts for the 119th Congress (2025–2027), with distinct colors and district labels.', 'Compare the present shapes here; open the map to explore congressional plans back to Kansas statehood in 1861.', 'January 1, 2025 generalized boundaries. Colors are not parties; this does not determine your ballot, officeholder or polling place.'],
 places: ['Counties meet watersheds', 'County boundaries and closer-scale drainage units provide two ways to locate a question.', 'Start with a county; zoom in to compare the watershed reference.', 'These separate boundary systems do not establish a causal relationship.'],
 science: ['A dated view from orbit', 'The newest current NOAA GOES catalog frame is previewed when available.', 'Look for its scan time and product label, including a visible-band fallback.', 'Cloud appearance is visual context, not a surface measurement or a forecast.'],
 sky: ['Kansas on the globe', 'The same real vector map becomes a globe view.', 'See the projection change, then open the map for calculated daylight.', 'Daylight and twilight are calculated in the Sky tools; no live cloud or star observation is claimed here.'],
 evidence: ['Follow the source trail', 'A quiet reference base leaves room for inspecting source, time and limitations.', 'Open the map and select a mapped feature to inspect its source context.', 'Provider context and recorded tours are separate from released KFM evidence.'],
};
export function categoryGlimpse(topic) {
 const entry = Object.hasOwn(glimpses, topic) ? glimpses[topic] : null;
 return entry ? { title: entry[0], summary: entry[1], try: entry[2], limit: entry[3] } : null;
}
