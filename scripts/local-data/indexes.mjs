#!/usr/bin/env node
// Lists or adds the indexes the local-data datasets need. Indexes are additive: no row changes.
// `apply` writes to the pipeline's databases, so run it under the pipeline lock, e.g.
//   flock --exclusive run/pipeline.lock node indexes.mjs apply [INDEX_NAME]
// with the same KFM_LOCAL_DATA_*DB variables as the gateway. With INDEX_NAME only that index is
// built, so a caller can take the lock once per index. Prints one JSON line per index.
import {pathToFileURL} from 'node:url';
import {DatabaseSync} from 'node:sqlite';
import {DATASETS} from './datasets.mjs';
import {databasesFromEnv,missingIndexes} from './gateway.mjs';

export function plannedIndexes(){
 const byDatabase=new Map();
 for(const d of DATASETS.values())for(const index of d.indexes){
  if(!byDatabase.has(d.db))byDatabase.set(d.db,new Map());
  byDatabase.get(d.db).set(index.name,{...index,datasets:[...(byDatabase.get(d.db).get(index.name)?.datasets??[]),d.id]});
 }
 return byDatabase;
}

async function main(mode,only){
 if(mode!=='check'&&mode!=='apply'){console.error('Use: indexes.mjs check|apply [INDEX_NAME]');return 2;}
 const databases=databasesFromEnv(),planned=plannedIndexes();
 if(only&&![...planned.values()].some(m=>m.has(only))){console.error('Unknown index '+only);return 2;}
 let missingTotal=0;
 for(const [name,indexes] of planned){
  const chosen=[...indexes.values()].filter(i=>!only||i.name===only);
  if(!chosen.length)continue;
  const path=databases[name];
  if(!path){console.log(JSON.stringify({database:name,state:'not-configured'}));continue;}
  const db=new DatabaseSync(path,{readOnly:mode==='check'});
  try{
   for(const index of chosen){
    const missing=missingIndexes(db,{indexes:[index]}).length>0;
    if(!missing){console.log(JSON.stringify({database:name,index:index.name,state:'present'}));continue;}
    if(mode==='check'){missingTotal++;console.log(JSON.stringify({database:name,index:index.name,state:'missing',datasets:index.datasets}));continue;}
    const started=Date.now();
    db.exec(index.sql);
    console.log(JSON.stringify({database:name,index:index.name,state:'created',seconds:Math.round((Date.now()-started)/100)/10}));
   }
  }finally{db.close();}
 }
 return mode==='check'&&missingTotal?1:0;
}

if(import.meta.url===pathToFileURL(process.argv[1]??'').href)main(process.argv[2],process.argv[3]).then(code=>{process.exitCode=code;});
