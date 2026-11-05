// How a recovered collection relates to the Explorer's topics, and how it is named and reached.
// Plain ESM so the welcome page and its tests can use it beside the TypeScript catalog module.

const ACRONYM=/^(?:aqs|asr|blm|cdc|eia|faa|fdic|fema|fra|frs|ghcnd|ghcndex|gnis|imls|ipeds|irs|kgs|mrds|msha|narn|nasr|nass|nbi|nces|nid|nps|nrhp|nwm|osm|pbdb|prism|spc|usdm|usfs|usgs|usmin|wqp)$/;
/** "ahcb changes" -> "AHCB Changes": source acronyms upper-cased, other words capitalised. */
export const recoveredTitle=title=>title.split(' ').map(word=>ACRONYM.test(word)?word.toUpperCase():word[0].toUpperCase()+word.slice(1)).join(' ');

/** The Explorer topics a collection belongs under, from its source family. */
export function recoveredTopics(id){
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
export const recoveredMapId=id=>`archive-records-${id}`;
/** The map URL that opens the given collections' archive layers; collections without geometry are left out. */
export const recoveredMapUrl=(ids,hasGeometry)=>`/?archive=${encodeURIComponent(ids.filter(hasGeometry).map(recoveredMapId).join(','))}&layerView=selected&panel=layers`;
export const recoveredLibraryUrl=id=>`/data-library?collection=${encodeURIComponent(id)}`;
