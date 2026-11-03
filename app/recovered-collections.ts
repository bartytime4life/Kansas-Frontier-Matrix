import catalog from '../scripts/local-data/recovered-catalog.json' with {type:'json'};
import type { TopicId } from './layer-workspaces';

export const RECOVERED_COLLECTIONS = catalog.map(collection => ({...collection,
  title: collection.title.split(' ').map(word => /^(?:aqs|asr|blm|cdc|eia|faa|fdic|fema|fra|frs|ghcnd|ghcndex|gnis|imls|ipeds|irs|kgs|mrds|msha|narn|nasr|nass|nbi|nces|nid|nps|nrhp|nwm|osm|pbdb|prism|spc|usdm|usfs|usgs|usmin|wqp)$/.test(word) ? word.toUpperCase() : word[0].toUpperCase()+word.slice(1)).join(' '),
}));
export const recoveredCollection = (id: string) => RECOVERED_COLLECTIONS.find(c=>c.id===id);
export function recoveredTopics(id: string): readonly TopicId[] {
  if(/osm/.test(id))return ['places','land','transport','evidence'];
  if(/aqs|climdiv|ghcn|storm|wind|prism|spc|usdm|vtec|asos/.test(id))return ['weather','science','disaster'];
  if(/kgs|macrostrat|mrds|msha|usmin/.test(id))return ['geology','science','engineering'];
  if(/wqp|usgs-(sites|daily|series|samples|field|peaks)|nwm/.test(id))return ['water','science'];
  if(/faa|nasr/.test(id))return ['aviation','transport','engineering'];
  if(/nbi|narn|fra|nid|asr/.test(id))return ['transport','engineering'];
  if(/census|cdc|eia|fdic|imls|ipeds|irs|nces/.test(id))return ['people','government','places'];
  if(/idigbio|neotoma|pbdb|p3k/.test(id))return ['ecology','geology','science','history'];
  if(/frs/.test(id))return ['ecology','engineering','places'];
  if(/nass/.test(id))return ['agriculture','land'];
  return ['history','places','evidence'];
}
export const recoveredMapId = (id: string) => `archive-records-${id}`;
export const recoveredMapUrl = (ids: readonly string[]) => `/?archive=${encodeURIComponent(ids.filter(id=>recoveredCollection(id)?.geometry).map(recoveredMapId).join(','))}&layerView=selected&panel=layers`;
