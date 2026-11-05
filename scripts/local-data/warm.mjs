#!/usr/bin/env node
// KFM local-data warm-up: asks every published dataset one real question through the same code the
// gateway runs, so the pipeline PC's spinning data disk has the index pages, catalogs and FTS
// segments a visitor's first question needs already in the page cache. The gateway's SQLite calls
// are synchronous, so a cold read that takes 40 s would stall every other visitor; this runs in its
// own process (a user timer on the PC, at start and every 15 minutes) and leaves the gateway alone.
// It reads only, through the datasets' own parse() and run(), and never prints an answer: one
// JSON line per pass with the time each question took. No dependencies.
//
//   KFM_LOCAL_DATA_DB=... [KFM_LOCAL_DATA_TIGER_DB=...] [KFM_LOCAL_DATA_NWM_DB=...] [KFM_LOCAL_DATA_BULK_DB=...] node warm.mjs [--repeat N]
import {pathToFileURL} from 'node:url';
import {DatabaseSync} from 'node:sqlite';
import {DATASETS} from './datasets.mjs';
import {missingIndexes,databasesFromEnv} from './gateway.mjs';
import {TIGER_LAYERS} from './tiger.mjs';
import {NEAR_COLLECTIONS} from './near.mjs';

const fail=code=>Object.assign(new Error(code),{code});
// Wichita and its county: the busiest corner of most collections, and the area the map opens on.
const WICHITA_BOX='-97.6,37.5,-97.2,37.8';
const near=database=>(NEAR_COLLECTIONS.find(c=>c.database===database&&c.id.includes('nrhp'))??NEAR_COLLECTIONS.find(c=>c.database===database))?.id;

/**
 * One question per dataset (a list for datasets with more than one cold path). Each must be a
 * question the dataset's parse() accepts; the test checks that and that no dataset is left out.
 * Identifiers are real records (Wichita's airport station, the Arkansas River gauge, an NWM reach)
 * but a missing one still warms the index the question seeks through.
 */
export const WARM_QUESTIONS=Object.freeze({
 'storm-events':{county:'Sedgwick',type:'Tornado',limit:5},
 'ghcn-stations':{name:'WICHITA',limit:5},
 'ghcn-daily':{station:'USW00003928',from:'2024-01-01',to:'2024-01-31',limit:50},
 'ghcndex-indices':{},
 'ghcndex':{station:'USW00003928',index:'TXx',limit:50},
 'asos-5min':{station:'KICT',limit:50},
 'wind-stations':{name:'Wichita',limit:5},
 'wind-observations':{station:'ICT',limit:50},
 'wind-daily':{station:'ICT',limit:50},
 'prism-county':{variable:'ppt',county:'173'},
 'tiger-features':{layer:TIGER_LAYERS[0],name:'Wichita',limit:5},
 'nwm-reaches':{feature:744181},
 'nwm-streamflow':{feature:744181,limit:50},
 'nws-alerts':{limit:5},
 'usgs-earthquakes':{limit:5},
 'usgs-streamflow-sites':{limit:5},
 'usgs-streamflow':{site:'USGS-07144100',parameter:'00060',limit:50},
 'recovered-observations':{collection:'observations-ahcb-changes',limit:5},
 'recovered-bulk':{collection:'bulk-census-decennial-geographies',limit:5},
 'archive-search':[{q:'tornado',source:'newspapers',facets:1,limit:5},{q:'kansas',source:'texts',facets:1,limit:5}],
 'near-observations':{collection:near('observations'),bbox:WICHITA_BOX,limit:5},
 'near-bulk':{collection:near('bulk'),bbox:WICHITA_BOX,limit:5},
});

/** The questions for one dataset, always as a list. */
export const questionsFor=(id,questions=WARM_QUESTIONS)=>[].concat(questions[id]??[]);

/**
 * One warm pass: every dataset's questions in catalog order, each database opened read-only once.
 * Returns {ms, stormEvents, datasets:[{id, question, status, ms, rows}]}; status is 'ok' or the
 * gateway's own code (DATASET_NOT_READY, DATABASE_NOT_CONFIGURED, DATABASE_UNAVAILABLE) or FAILED.
 * Never throws for a dataset: a question that fails is reported and the pass goes on.
 */
export function warm({databases,questions=WARM_QUESTIONS,open=path=>new DatabaseSync(path,{readOnly:true}),clock=Date.now}){
 const started=clock(),opened=new Map(),caches=new Map(),report=[];
 const database=name=>{
  const path=databases[name];if(!path)throw fail('DATABASE_NOT_CONFIGURED');
  if(!opened.has(name)){let db;try{db=open(path);}catch{throw fail('DATABASE_UNAVAILABLE');}opened.set(name,db);caches.set(name,new Map());}
  return {db:opened.get(name),cache:caches.get(name)};
 };
 try{
  for(const dataset of DATASETS.values()){
   questionsFor(dataset.id,questions).forEach((question,index)=>{
    const at=clock();let status='ok',rows=null;
    try{
     const {db,cache}=database(dataset.db);
     if(missingIndexes(db,dataset).length)throw fail('DATASET_NOT_READY');
     const answer=dataset.run(db,dataset.parse(question),{cache});
     rows=(answer[dataset.rowsKey??'rows']??[]).length;
    }catch(error){status=typeof error?.code==='string'?error.code:'FAILED';}
    report.push({id:dataset.id,question:index,status,ms:clock()-at,rows});
   });
  }
  // The health route's one aggregate, which is a full index walk when cold.
  let stormEvents=null;
  try{stormEvents=database('observations').db.prepare('SELECT COUNT(*) AS n FROM kfm_storm_event_details').get().n;}catch{}
  return {ms:clock()-started,stormEvents,datasets:report};
 }finally{
  for(const db of opened.values()){try{db.close();}catch{}}
 }
}

/** The journal line for one pass: totals and the slowest questions, never an answer. */
export function summarize(result,pass){
 const slowest=[...result.datasets].sort((a,b)=>b.ms-a.ms).slice(0,5).map(d=>({id:d.id,question:d.question,ms:d.ms,status:d.status}));
 const failed=result.datasets.filter(d=>d.status!=='ok').map(d=>({id:d.id,question:d.question,status:d.status}));
 return {at:new Date().toISOString(),event:'warmed',pass,ms:result.ms,questions:result.datasets.length,failed,slowest,stormEvents:result.stormEvents,datasets:result.datasets};
}

async function main(argv){
 const repeatAt=argv.indexOf('--repeat'),repeat=repeatAt>=0?Number(argv[repeatAt+1]):1;
 if(!Number.isInteger(repeat)||repeat<1||repeat>10){console.error(JSON.stringify({event:'config_refused',code:'REPEAT_INVALID'}));return 1;}
 let databases;
 try{databases=databasesFromEnv();}
 catch(error){console.error(JSON.stringify({event:'config_refused',code:error.code??'CONFIG_INVALID'}));return 1;}
 for(let pass=1;pass<=repeat;pass++)console.log(JSON.stringify(summarize(warm({databases}),pass)));
 return 0;
}

if(import.meta.url===pathToFileURL(process.argv[1]??'').href)main(process.argv.slice(2)).then(code=>{process.exitCode=code;});
