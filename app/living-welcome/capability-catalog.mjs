import { MAP_DEMOS } from './map-demos.mjs';
// Presentation references only; each reused capture keeps its original scope.
const selections = {
 weather: ['weather'], water: ['rivers'], groundwater: ['underground'],
 geology: ['underground', 'Regional groundwater context; not a continuous rock model.'],
 terrain: ['science'], ecology: ['farming', 'Aerial land-cover context; no species inventory.'],
 agriculture: ['farming'], history: ['history'], transport: ['transport'],
 engineering: ['transport', 'Bridge inventory and transport context; not engineering analysis.'],
 land: ['government', 'County and survey reference context; not ownership evidence.'],
 people: ['government', 'Aggregate county geography; not individual people.'], places: ['government'],
 science: ['science'], disaster: ['weather', 'Weather context only; not a hazard reconstruction or warning.'],
 aviation: [null, 'Open the aviation chart for runways, airport identifiers and terrain relief. No verified aviation capture is available yet.'],
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
