import {RECOVERED_COLLECTIONS,recoveredMapUrl,recoveredTopics} from './recovered-collections';

export type Collection = (typeof RECOVERED_COLLECTIONS)[number];
export type FieldRole = 'identity'|'time'|'location'|'unit'|'quality'|'value';
export function fieldRole(name:string, keys:readonly string[]=[]):FieldRole {
 if(keys.includes(name)||/(_number(?:_\d+)?|_no|_identifier)$/i.test(name)||/^(county|state|tract|block|site|station|block_group|variable|parameter|parameter_cd|element|measureid|characteristic_name)$/i.test(name)||/(^|_)(id|ids|code|fips|geoid|zip|row_number|file_id|site_no|station_id|objectid|lccn)($|_)/i.test(name))return 'identity';
 if(/(^|_)(date|time|year|month|day|start|end|begin|issued|valid|edition)($|_)/i.test(name))return 'time';
 if(/geometry|latitude|longitude|(^|_)(lat|lon|lng|coordinates)($|_)/i.test(name))return 'location';
 if(/(^|_)(units?|unit_name)($|_)/i.test(name))return 'unit';
 if(/flag|qualifier|quality|status|remark|censor|precision|uncertainty/i.test(name))return 'quality';
 return 'value';
}
export const fieldLabel = (name:string) => name.replaceAll('_',' ').replace(/\b\w/g,v=>v.toUpperCase());
const family = (id:string) => id.replace(/^(observations|bulk)-/,'').split('-')[0];
export const collectionUrl = (id:string) => `/data-library?collection=${encodeURIComponent(id)}`;
export const labUrl = (id:string) => `/data-lab?collection=${encodeURIComponent(id)}`;
export function collectionMetadata(c:Collection){
 const topics=[...recoveredTopics(c.id)];
 const fields=c.columns.map(name=>({name,label:fieldLabel(name),role:fieldRole(name,c.keys),definition:null,unit:null}));
 return {format:'kfm-collection-metadata-v1',id:c.id,title:c.title,
  description:`${c.title}: archived source records with ${fields.length} retained fields, including original identifiers and source values. ${c.geometry?'Stored geometry can be inspected on the map.':'Use the record table and lab; map geometry is not stored for this collection.'}`,
  topics,sourceFamily:family(c.id),recordIdentity:c.keys,
  access:{records:`/api/local-data/recovered-${c.database}?collection=${encodeURIComponent(c.id)}&limit=20`,library:collectionUrl(c.id),lab:labUrl(c.id),map:c.geometry?recoveredMapUrl([c.id]):null},
  spatial:{geometryField:c.geometry,coverage:null,crs:null,note:'A stored geometry field is a map option, not proof of complete geographic coverage.'},
  temporal:{candidateFields:fields.filter(f=>f.role==='time').map(f=>f.name),observationPeriod:null,edition:null,retrievedAt:null,note:'Source observation time, archive edition and retrieval time must be read separately.'},
  provenance:{provider:null,sourceUrls:[],digests:[],reviewCredit:null,note:'Source identity, links and file digests are supplied per record when available. This catalog does not establish an AI review or source approval.'},
  fields,unknowns:['Provider field definitions and units require source documentation.','Coverage, rights, edition and review are not inferred from collection names.'],
  uses:{map:!!c.geometry,recordBrowser:true,lab:true,storyBrief:true},
 };
}

export const RESEARCH_PACKS = [
 {id:'built-places',title:'Places and the built landscape',question:'How do mapped buildings, place names, administrative areas and points of interest describe the landscape?',match:/osm-|gnis|census-.*geographies|nps|nces|frs-facilities/,note:'Map tags and administrative geometries need their source edition and local context; a mapped feature is not a current occupancy or legal boundary determination.'},
 {id:'water-land',title:'Water, wells and working land',question:'How can water measurements, wells, dams and agricultural records inform a place investigation?',match:/wqp|usgs-(sites|daily|field|peaks|samples|series)|nwm|nid|wwc5|prism|usdm|nass/,note:'Match station identity, measurement units and observation dates before comparing water records.'},
 {id:'weather-risk',title:'Weather, exposure and recovery',question:'Which dated weather observations and disaster records help explain a local event?',match:/storm|spc|iem|asos|wind|ghcn|climdiv|aqs|fema|prism|usdm/,note:'Weather, climate, disaster declarations and losses describe different things; overlap alone does not establish cause.'},
 {id:'roads-aviation',title:'Moving across Kansas',question:'Where do bridges, railways, airports and obstacles connect to the built environment?',match:/nbi|narn|fra|faa|nasr|asr|osm-(roads|railways|traffic|transport)/,note:'Archived infrastructure records are context; use current official notices for navigation or safety decisions.'},
 {id:'land-history',title:'Changing places and boundaries',question:'How do changing counties, surveys, place names and historical records describe the same place?',match:/ahcb|atack|blevins|blm|gnis|nrhp|newspaper|usfs|htmc|wikidata/,note:'Keep historical boundary versions and source editions distinct; modern coordinates are not historical jurisdiction proof.'},
 {id:'living-land',title:'Life, habitats and deep time',question:'What can occurrence records, protected lands, fossils and dated samples contribute to a landscape story?',match:/idigbio|neotoma|pbdb|p3k|nps|osm-(natural|protected|water|landuse)/,note:'Occurrences, fossils and age models have different sampling and uncertainty; absence of a record does not establish absence.'},
 {id:'geology-energy',title:'Geology, resources and energy',question:'How can wells, lithology, geological units, mines and energy statistics be investigated together?',match:/kgs|macrostrat|mrds|msha|usmin|eia|usgs-earthquakes/,note:'Depth, age, production and energy units require provider definitions; nearby records are not a geological correlation.'},
 {id:'communities',title:'Communities and public services',question:'How do population tables, schools, libraries, health and civic records describe a community?',match:/census|cdc|nces|ipeds|imls|congress|irs|fdic/,note:'Match geographic identifiers and reference years; survey estimates, margins of error and reporting universes differ.'},
 {id:'environment',title:'Environmental context',question:'Which facility, air, water and land records support a grounded environmental investigation?',match:/frs|aqs|wqp|usgs-samples|nass|osm-(water|landuse|natural)/,note:'A listed facility or environmental interest is not proof of a release, violation, exposure or health effect.'},
 {id:'prepared',title:'Prepared observations',question:'What source records and preparation context are available for this derived collection?',match:/prepared|environmental-(capture-)?features/,note:'Inspect preparation lineage and original source references before interpreting derived observations.'},
] as const;
export function packCollections(id:string){const pack=RESEARCH_PACKS.find(p=>p.id===id);return pack?RECOVERED_COLLECTIONS.filter(c=>pack.match.test(c.id)):[];}
export const collectionPacks = (id:string) => RESEARCH_PACKS.filter(p=>p.match.test(id));
export function relatedCollections(c:Collection){
 const topics=recoveredTopics(c.id),packs=collectionPacks(c.id);
 return RECOVERED_COLLECTIONS.filter(other=>other.id!==c.id).map(other=>{
  const sharedTopics=recoveredTopics(other.id).filter(t=>topics.includes(t));
  const sharedPacks=packs.filter(p=>p.match.test(other.id));
  const sameFamily=family(c.id)===family(other.id);
  return {collection:other,score:sharedTopics.length+sharedPacks.length*3+(sameFamily?2:0),reason:sharedPacks[0]?.title??(sharedTopics.length?sharedTopics.join(', '):`Shared ${family(c.id)} source family; verify definitions`),
   joinCandidates:sameFamily?c.columns.filter(k=>other.columns.includes(k)&&fieldRole(k,c.keys)==='identity'&&!c.keys.includes(k)&&!other.keys.includes(k)):[]};
 }).filter(v=>v.score>0).sort((a,b)=>b.score-a.score||a.collection.id.localeCompare(b.collection.id)).slice(0,6);
}
