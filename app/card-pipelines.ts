import { CATEGORY_MAPS } from './category-maps';
import type { CategoryMap } from './category-maps';
import { MAP_STARTERS } from './map-starters';
import { TOPIC_STRUCTURE, officialSourceTopics, SPECIALTY_LAYER_CATALOG, specialtyLayerTopics } from './layer-workspaces';
import { OFFICIAL_CONTEXT_SOURCES } from './live-context';
import { DOMAIN_PIPELINES, TOPIC_PIPELINES, PC_CAPTURE_IDS } from './pipeline-catalog.mjs';

export type CardPipelineBinding = Readonly<{
  id: string; kind: 'recipe' | 'topic'; title: string;
  required: readonly string[]; optional: readonly string[]; gaps: readonly string[]; demo: boolean;
}>;
export type PipelineDefinition = Readonly<{
  id: string; title: string; mode: 'pc-capture' | 'display' | 'candidate' | 'calculated' | 'index'; wave: number;
  owner: string; cadence: string; sourceRef: string; nextGate: string;
}>;
export type PipelineHealthSummary = Readonly<{
  sourceId: string; state: 'not-checked' | 'available' | 'partial' | 'empty' | 'stale' | 'held' | 'unavailable' | 'candidate';
  retrievedAt: string | null; observedFrom: string | null; observedThrough: string | null;
  releaseId: string | null; approvalExpiresAt: string | null;
}>;
const unique = (ids: readonly string[]) => Object.freeze([...new Set(ids)]);
const topicGaps = TOPIC_PIPELINES as Readonly<Record<string, readonly string[]>>;
const categoryMaps = CATEGORY_MAPS as Readonly<Record<string, CategoryMap>>;
const toolTitles: Readonly<Record<string, string>> = {
  landcover: 'NLCD land-cover classes', plants: 'Annual GBIF plant-record density', crops: 'USDA crop classes',
  radar: 'Dated radar frames', surface: 'Surface weather stations', outlook: 'SPC outlook', reports: 'Storm reports',
  rainfall: 'MRMS rainfall', tornadoes: 'Historical tornado records', reviewed: 'Approved source projections',
  fema: 'FEMA disaster declarations', flow: 'Terrain flow display', flood: 'NWS flood forecasts',
  aquifer: 'Aquifer display editions', wells: 'Measured well levels', underground: 'Recorded subsurface context',
  quakes: 'Historical earthquake records', transect: 'Display elevation profile', photoreal: 'Photoreal terrain',
  area: 'Calculated map area', soil: 'Modelled soil moisture', drought: 'Drought Monitor editions',
  daylight: 'Calculated daylight', sunyear: 'Annual solar and lunar geometry',
};
const calculatedTools = new Set(['flow', 'transect', 'area', 'daylight', 'sunyear']);
const categoryTools = unique(Object.values(categoryMaps).flatMap(map => map.tools ?? []));
export const CARD_PIPELINE_BINDINGS: readonly CardPipelineBinding[] = Object.freeze([
  ...MAP_STARTERS.map(recipe => Object.freeze({ id: `recipe:${recipe.id}`, kind: 'recipe' as const, title: recipe.title,
    required: unique(recipe.ids), optional: Object.freeze([]), gaps: Object.freeze([]), demo: false })),
  ...TOPIC_STRUCTURE.map(topic => Object.freeze({ id: `topic:${topic.id}`, kind: 'topic' as const, title: topic.title,
    required: Object.freeze([]), optional: unique([...(categoryMaps[topic.id]?.starters ?? []), ...(categoryMaps[topic.id]?.contextLayers ?? []).map(layer => layer.id),
      ...(categoryMaps[topic.id]?.tools ?? []).map(tool => `map-tool:${tool}`),
      ...OFFICIAL_CONTEXT_SOURCES.filter(source => officialSourceTopics(source.id).includes(topic.id)).map(source => source.id),
      ...SPECIALTY_LAYER_CATALOG.filter(layer => specialtyLayerTopics(layer.id).includes(topic.id)).map(layer => `specialty:${layer.id}`),
      ...(['evidence', 'history', 'people', 'land', 'places', 'science'].includes(topic.id) ? ['knowledge-index'] : [])]),
    gaps: unique(topicGaps[topic.id] ?? []), demo: false })),
]);
export const PIPELINE_DEFINITIONS: readonly PipelineDefinition[] = Object.freeze([
  ...OFFICIAL_CONTEXT_SOURCES.map(source => Object.freeze({ id: source.id, title: source.title,
    mode: PC_CAPTURE_IDS.includes(source.id) ? 'pc-capture' as const : 'display' as const, wave: 1,
    owner: PC_CAPTURE_IDS.includes(source.id) ? 'PC capture worker and Explorer adapter' : 'Explorer official-context adapter',
    cadence: PC_CAPTURE_IDS.includes(source.id) ? `Hourly PC capture; provider: ${source.cadence}` : source.cadence, sourceRef: `official-context:${source.id}`,
    nextGate: PC_CAPTURE_IDS.includes(source.id) ? 'Review a source-specific release profile before publishing PC captures' : 'Display adapter exists; qualify a bounded capture before scheduling on the PC' })),
  ...SPECIALTY_LAYER_CATALOG.map(layer => Object.freeze({ id: `specialty:${layer.id}`, title: layer.title,
    mode: layer.id === 'daylight' ? 'calculated' as const : 'display' as const, wave: 1,
    owner: 'Existing specialty-layer adapter', sourceRef: `specialty-layer:${layer.id}`,
    cadence: layer.id === 'daylight' ? 'Calculated for the selected location and time; not a provider observation' : 'Existing specialty control owns product dates, requests and serving checks',
    nextGate: 'Check the existing specialty control; a catalog entry does not establish source availability or release',
  })),
  Object.freeze({ id: 'knowledge-index', title: 'Released knowledge search index', mode: 'index' as const, wave: 1,
    owner: 'Existing knowledge serving and search adapters', sourceRef: 'app/knowledge-read.ts',
    cadence: 'Searches permitted indexed records; ingestion and source clocks remain separate',
    nextGate: 'Check indexed coverage and the existing knowledge serving policy before relying on a result',
  }),
  ...categoryTools.map(tool => Object.freeze({ id: `map-tool:${tool}`, title: toolTitles[tool] ?? tool,
    mode: calculatedTools.has(tool) ? 'calculated' as const : 'display' as const, wave: 1,
    owner: 'Existing category map control', sourceRef: `app/category-map-dock.tsx#${tool}`,
    cadence: calculatedTools.has(tool) ? 'Calculated from the selected display, location and time; not a provider observation'
      : 'The existing control checks its own product edition, request bounds, source clocks and availability',
    nextGate: 'Inspect this control and its source notes. No private PC capture or release is implied.',
  })),
  ...DOMAIN_PIPELINES,
]);
export function validateCardPipelines() {
  const ids = new Set(PIPELINE_DEFINITIONS.map(p => p.id));
  if (ids.size !== PIPELINE_DEFINITIONS.length || new Set(CARD_PIPELINE_BINDINGS.map(c => c.id)).size !== CARD_PIPELINE_BINDINGS.length) throw new Error('PIPELINE_ID_DUPLICATE');
  if (Object.keys(topicGaps).sort().join() !== TOPIC_STRUCTURE.map(t => t.id).sort().join()) throw new Error('CARD_BINDING_INCOMPLETE');
  for (const card of CARD_PIPELINE_BINDINGS) {
    const references = [...card.required, ...card.optional, ...card.gaps];
    if (new Set(references).size !== references.length || references.some(id => !ids.has(id))) throw new Error('CARD_DEPENDENCY_INVALID');
  }
  return true;
}
validateCardPipelines();
