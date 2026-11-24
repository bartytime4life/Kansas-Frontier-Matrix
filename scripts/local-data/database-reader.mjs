// Fixed dataset operations only. This module never receives relay credentials.
import {DatabaseSync} from 'node:sqlite';
import {DATASETS} from './datasets.mjs';
import {datasetFreshness,collectionsFreshness} from './freshness.mjs';

const fail=code=>Object.assign(new Error(code),{code});
export function missingIndexes(db,dataset){
 if(!dataset.indexes.length)return [];
 const present=new Set(db.prepare(`SELECT name FROM sqlite_master WHERE type='index' AND name IN (${dataset.indexes.map(()=>'?').join(',')})`).all(...dataset.indexes.map(i=>i.name)).map(r=>r.name));
 return dataset.indexes.map(i=>i.name).filter(n=>!present.has(n));
}

export function createDatabaseReader({databases,open=path=>new DatabaseSync(path,{readOnly:true}),clock=Date.now}){
 const caches=new Map(),cacheFor=path=>{if(!caches.has(path))caches.set(path,new Map());return caches.get(path);};
 const ready=(db,path,dataset)=>{
  const cache=cacheFor(path),version=db.prepare('PRAGMA schema_version').get().schema_version,key='ready:'+dataset.id;
  if(cache.get(key)===version)return [];
  const missing=missingIndexes(db,dataset);if(!missing.length)cache.set(key,version);return missing;
 };
 const database=(name,opened)=>{
  const path=databases[name];if(!path)throw fail('DATABASE_NOT_CONFIGURED');
  if(!opened.has(name)){
   let db;try{db=open(path);}catch{throw fail('DATABASE_UNAVAILABLE');}
   opened.set(name,db);
  }
  return {db:opened.get(name),path};
 };
 return operation=>{
  const opened=new Map();
  try{
   if(operation.kind==='health'){
    const collections={},datasets=[...DATASETS.values()].map(d=>{
     try{
      const {db,path}=database(d.db,opened),cache=cacheFor(path),missing=ready(db,path,d);
      const entry=missing.length?{id:d.id,ready:false,reason:'INDEX_MISSING'}:{id:d.id,ready:true};
      entry.freshness=datasetFreshness(db,d,{cache});
      if(d.freshness?.collections)Object.assign(collections,collectionsFreshness(db,d.freshness.collections,{cache}));
      return entry;
     }catch(e){return {id:d.id,ready:false,reason:e.code==='DATABASE_NOT_CONFIGURED'?'DATABASE_NOT_CONFIGURED':'DATABASE_UNAVAILABLE',freshness:{reason:'UNAVAILABLE'}};}
    });
    let stormEvents=null;
    try{stormEvents=database('observations',opened).db.prepare('SELECT COUNT(*) AS n FROM kfm_storm_event_details').get().n;}catch{}
    return {ok:stormEvents!==null,datasets,collections,stormEvents,generatedAt:new Date(clock()).toISOString()};
   }
   if(operation.kind!=='dataset')throw fail('QUERY_INVALID');
   const dataset=DATASETS.get(operation.id);if(!dataset)throw fail('QUERY_INVALID');
   const query=dataset.parse(operation.input),{db,path}=database(dataset.db,opened);
   if(ready(db,path,dataset).length)throw fail('DATASET_NOT_READY');
   const result=dataset.run(db,query,{cache:cacheFor(path)});
   return {query,result};
  }finally{for(const db of opened.values()){try{db.close();}catch{}}}
 };
}
