// What the public record holds for each welcome topic: the recovered collections under it, a
// newspaper search that fits it, and where each leads. Links only; the welcome admits no data.
import catalog from '../../scripts/local-data/recovered-catalog.json' with {type:'json'};
import {recoveredTitle,recoveredTopics,recoveredLibraryUrl,recoveredMapUrl} from '../recovered-topics.mjs';

export const RECORD_COLLECTIONS=catalog.map(c=>({id:c.id,title:recoveredTitle(c.title),geometry:Boolean(c.geometry),database:c.database,topics:recoveredTopics(c.id)}));
export const RECORD_COUNTS=Object.freeze({collections:RECORD_COLLECTIONS.length,mapped:RECORD_COLLECTIONS.filter(c=>c.geometry).length});
// A search a reader of the period's newspapers might start with; the words, not the answer.
export const NEWSPAPER_TERMS=Object.freeze({
 engineering:['bridge','waterworks'],transport:['railroad','depot'],aviation:['aeroplane','balloon'],
 weather:['tornado','blizzard'],disaster:['cyclone','flood'],water:['river','flood'],groundwater:['artesian','well'],
 geology:['oil','coal'],terrain:['prairie','bluff'],ecology:['grasshopper','prairie'],agriculture:['wheat','harvest'],
 flora:['grass','orchard'],fauna:['buffalo','prairie chicken'],history:['territory','homestead'],land:['homestead','land office'],
 people:['census','colony'],government:['legislature','election'],places:['post office','town site'],'public-safety':['sheriff','fire'],
 science:['eclipse','telegraph'],sky:['comet','meteor'],evidence:['survey','deed'],
});
export const newspaperSearchUrl=(q,source='newspapers')=>`/data-library?q=${encodeURIComponent(q)}&source=${source}`;
export const librarySearchUrl=find=>`/data-library?find=${encodeURIComponent(find)}`;
const PREFER=/storm-event-details|ghcnd-stations|wind-stations|usdm-county|usgs-sites|nrhp-locations|gnis|post-office|nbi-bridges|nid-dams|nasr-airports|kgs-wells|census-acs-geographies|osm-places|pbdb|nass|frs-facilities|climdiv-monthly|prism-county|wqp-stations|neotoma-sites|msha-mines/;
const family=id=>id.replace(/^(?:observations|bulk)-/,'').split('-')[0];
/** Up to `limit` collections for a topic: mapped ones and the better-known tables first, one per source family before a
 *  second from any family, each with its library link and, when it has geometry, its map link. */
export function recordLinksFor(topic,limit=4){
 const under=RECORD_COLLECTIONS.filter(c=>c.topics.includes(topic));
 const ranked=[...under].sort((a,b)=>Number(b.geometry)-Number(a.geometry)||Number(PREFER.test(b.id))-Number(PREFER.test(a.id))||a.title.localeCompare(b.title));
 const chosen=[],families=new Set();
 for(const c of ranked)if(!families.has(family(c.id))){families.add(family(c.id));chosen.push(c);if(chosen.length===limit)break;}
 for(const c of ranked)if(chosen.length<limit&&!chosen.includes(c))chosen.push(c);
 return {
  total:under.length,mapped:under.filter(c=>c.geometry).length,
  collections:chosen.map(c=>({id:c.id,title:c.title,geometry:c.geometry,url:recoveredLibraryUrl(c.id),mapUrl:c.geometry?recoveredMapUrl([c.id],()=>true):null})),
  terms:(NEWSPAPER_TERMS[topic]??['kansas']).map(term=>({term,url:newspaperSearchUrl(term)})),
  libraryUrl:'/data-library',
 };
}
