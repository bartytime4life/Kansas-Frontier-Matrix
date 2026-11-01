// Every question the website may ask the pipeline PC, one entry per dataset. Each entry names its
// database, the indexes it relies on (the gateway refuses the dataset until they exist, so no
// question ever scans a large table), a shared parse() for the website and the gateway, and a
// gateway-only run(). Publication: Storm Events approved 2026-11-01 (fatalities table excluded);
// every other dataset here approved by the owner on 2026-11-01. No dependencies.
import {parseStormQuery,stormEventsSql,stormEvent,STORM_EVENTS_SOURCE} from './storm-events.mjs';
import {ghcnStations,ghcnDaily,ghcndexIndices,ghcndex,asosFiveMinute,windStations,windObservations,windDaily} from './weather.mjs';
import {prismCounty} from './prism.mjs';
import {tigerFeatures} from './tiger.mjs';
import {nwmReaches,nwmStreamflow,nwsAlerts,usgsEarthquakes,usgsStreamflowSites,usgsStreamflow} from './water.mjs';

const stormEvents={
 id:'storm-events',db:'observations',title:'NOAA Storm Events (Kansas)',indexes:[],source:STORM_EVENTS_SOURCE,
 // Phase 1 reply shape, kept for existing callers.
 format:'kfm-local-data-storm-events-v1',rowsKey:'events',
 params:{county:'county FIPS (counties only) or county/zone name',from:'YYYY-MM-DD',to:'YYYY-MM-DD',type:'NCEI event type, e.g. Tornado',limit:'1-200 (50)',offset:'0-50000'},
 parse:parseStormQuery,
 run(db,q){const sql=stormEventsSql(q);return {total:db.prepare(sql.count.sql).get(...sql.count.params).n,rows:db.prepare(sql.rows.sql).all(...sql.rows.params).map(stormEvent)};},
};

export const DATASETS=new Map([stormEvents,ghcnStations,ghcnDaily,ghcndexIndices,ghcndex,asosFiveMinute,windStations,windObservations,windDaily,
 prismCounty,tigerFeatures,nwmReaches,nwmStreamflow,nwsAlerts,usgsEarthquakes,usgsStreamflowSites,usgsStreamflow].map(d=>[d.id,d]));
export const DATABASES=Object.freeze(['observations','tiger','nwm']);

/** Public description of every dataset, for the website's catalog. */
export function datasetCatalog(){
 return [...DATASETS.values()].map(d=>({id:d.id,title:d.title,path:'/api/local-data/'+d.id,params:d.params,source:d.source}));
}
