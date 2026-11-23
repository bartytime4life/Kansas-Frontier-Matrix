// Freshness: when the newest file behind a dataset, or behind one recovered collection, was
// retrieved by the pipeline and when its provider last changed it, so a visitor can tell "no
// match" from "not loaded yet". Every answer comes from the pipeline's own bookkeeping, never from
// a scan of a data table:
//  - a table whose primary key or an index leads with file_id: MAX(file_id) is one seek, and the
//    file's receipt in kfm_sql_sources (file_id is its primary key) carries the dates;
//  - a dataset read from several source families (storm events, captures, GHCN): the newest file
//    of those families through the (source_id, file_id) index declared below, which the pipeline
//    builds with `indexes.mjs apply`; until then the answer is INDEX_MISSING, never a scan;
//  - a dataset loaded outside kfm_sql_sources (PRISM): the feed's own kfm_feed_state row;
//  - a GeoPackage: gpkg_contents.last_change.
// No dependencies.
import {str} from './query.mjs';

export const SOURCES_INDEX=Object.freeze({name:'kfm_sql_sources_source_file',sql:'CREATE INDEX IF NOT EXISTS kfm_sql_sources_source_file ON kfm_sql_sources(source_id, file_id)'});
const STORM_FILE_INDEXES=['details','fatalities','locations'].map(kind=>{
 const table='kfm_storm_event_'+kind,name=table+'_file';
 return Object.freeze({name,sql:`CREATE INDEX IF NOT EXISTS ${name} ON ${table}(file_id)`,namedOnly:true});
});
/** Indexes freshness needs per database; `indexes.mjs` plans them, the gateway never requires them to answer a question. */
export const FRESHNESS_INDEXES=Object.freeze({observations:[SOURCES_INDEX,...STORM_FILE_INDEXES],bulk:[SOURCES_INDEX]});
// Receipt keys, in order of preference: feed receipts, hosted captures, older loaders.
const RETRIEVED=['retrieved_at','retrievedAt','captureBucketAt','downloaded_at_utc','created_at'];
const MODIFIED=['last_modified','lastModified','data_as_of'];

/** An ISO instant from any date string a receipt may carry (ISO, HTTP date), or null. */
export function iso(value){
 if(value===null||value===undefined||value==='')return null;
 const ms=Date.parse(String(value));
 return Number.isFinite(ms)?new Date(ms).toISOString():null;
}

const quote=name=>'"'+String(name).replace(/"/g,'""')+'"';
const exists=(db,type,name)=>!!db.prepare('SELECT 1 FROM sqlite_master WHERE type=? AND name=?').get(type,name);
const remembered=(cache,key,compute)=>{if(cache&&cache.has(key))return cache.get(key);const value=compute();if(cache)cache.set(key,value);return value;};

function fromReceipt(row){
 let receipt={};try{receipt=JSON.parse(row.receipt_json)??{};}catch{}
 const pick=keys=>{for(const key of keys){const value=iso(receipt[key]);if(value)return value;}return null;};
 return {file:row.file_id,sourceId:str(row.source_id),retrievedAt:pick(RETRIEVED),modifiedAt:pick(MODIFIED)};
}

function fileKeyCache(db,cache){
 if(!cache)return new Map();
 const version=db.prepare('PRAGMA schema_version').get().schema_version;
 let snapshot=cache.get('file-keys');
 if(!snapshot||snapshot.version!==version){
  snapshot={version,keys:new Map()};
  cache.set('file-keys',snapshot);
 }
 return snapshot.keys;
}

/** The schema requirement for a bounded MAX(file_id) lookup. */
function fileKeyState(db,table,keys){
 return remembered(keys,table,()=>{
  if(!exists(db,'table',table))return 'TABLE_ABSENT';
  const columns=db.prepare('SELECT name,pk FROM pragma_table_info(?)').all(table);
  const column=columns.find(c=>c.name==='file_id');
  if(!column)return 'COLLECTION_FILE_KEY_MISSING';
  if(column.pk===1)return 'INDEXED';
  const indexed=db.prepare('SELECT name,partial FROM pragma_index_list(?)').all(table)
   .some(i=>!i.partial&&db.prepare('SELECT name FROM pragma_index_info(?) WHERE seqno=0').get(i.name)?.name==='file_id');
  return indexed?'INDEXED':'INDEX_MISSING';
 });
}

export function fileLed(db,table,cache){
 return fileKeyState(db,table,fileKeyCache(db,cache))==='INDEXED';
}

function indexedTableFreshness(db,table){
 const newest=db.prepare(`SELECT MAX(file_id) AS m FROM ${quote(table)}`).get().m;
 if(newest===null||newest===undefined)return null;
 const row=db.prepare('SELECT file_id,source_id,receipt_json FROM kfm_sql_sources WHERE file_id=?').get(newest);
 return row?fromReceipt(row):{file:newest,sourceId:null,retrievedAt:null,modifiedAt:null};
}

/** The newest file behind one table, or null when its bounded lookup is unavailable or empty. */
export function tableFreshness(db,table,{cache}={}){
 return fileLed(db,table,cache)?indexedTableFreshness(db,table):null;
}

/**
 * The newest file of the given source families: a family name matches source_id exactly or as
 * `family-…`, so 'noaa-ghcnd' covers noaa-ghcnd and noaa-ghcnd-diff but not noaa-ghcndex.
 * Needs SOURCES_INDEX; without it the answer is {reason:'INDEX_MISSING'}.
 */
export function sourcesFreshness(db,families,{cache}={}){
 if(!remembered(cache,'index:'+SOURCES_INDEX.name,()=>exists(db,'index',SOURCES_INDEX.name)))return {reason:'INDEX_MISSING'};
 const exact=db.prepare('SELECT file_id,source_id,receipt_json FROM kfm_sql_sources WHERE source_id=? ORDER BY file_id DESC LIMIT 1');
 const under=db.prepare("SELECT file_id,source_id,receipt_json FROM kfm_sql_sources WHERE source_id>=? AND source_id<? ORDER BY file_id DESC LIMIT 1");
 let best=null;
 for(const family of families){
  for(const row of [exact.get(family),under.get(family+'-',family+'-\u007f')]){
   if(row&&(!best||row.file_id>best.file_id))best=row;
  }
 }
 return best?fromReceipt(best):{reason:'NO_FILES'};
}

/** When a feed last wrote this database, from its own state row. */
export function feedFreshness(db,feed){
 if(!exists(db,'table','kfm_feed_state'))return {reason:'NO_FEED_STATE'};
 const row=db.prepare('SELECT updated_at FROM kfm_feed_state WHERE feed=?').get(feed);
 return row?{file:null,sourceId:str(feed),retrievedAt:iso(row.updated_at),modifiedAt:null}:{reason:'NO_FEED_STATE'};
}

/** A GeoPackage's newest layer change. */
export function geopackageFreshness(db){
 if(!exists(db,'table','gpkg_contents'))return {reason:'NO_GEOPACKAGE'};
 const row=db.prepare('SELECT MAX(last_change) AS m FROM gpkg_contents').get();
 return row?.m?{file:null,sourceId:null,retrievedAt:null,modifiedAt:iso(row.m)}:{reason:'NO_FILES'};
}

/** Registered collections may report an exact file receipt or the reason the lookup is unavailable. */
export function collectionsFreshness(db,collections,{cache}={}){
 const out={},keys=fileKeyCache(db,cache);
 for(const c of collections){
  try{
   const state=fileKeyState(db,c.table,keys);
   if(state==='TABLE_ABSENT')continue;
   const value=state==='INDEXED'?indexedTableFreshness(db,c.table):{reason:state};
   if(value)out[c.id]=value;
  }catch{/* A collection's unavailable receipt must not hide its peers. */}
 }
 return out;
}

const newer=(a,b)=>!a?b:!b?a:(b.retrievedAt??'')>(a.retrievedAt??'')||(!a.retrievedAt&&!b.retrievedAt&&(b.file??0)>(a.file??0))?b:a;

/**
 * One dataset's freshness from its declaration: {tables:[…]}, {sources:[…]}, {feed:'…'},
 * {geopackage:true} or {collections:[…]}. Returns {file, sourceId, retrievedAt, modifiedAt,
 * basis} or {reason}. Never throws for a dataset: a missing table or index is a reason.
 */
export function datasetFreshness(db,dataset,{cache}={}){
 const spec=dataset.freshness;
 if(!spec)return {reason:'NOT_DECLARED'};
 try{
  if(spec.geopackage)return {...geopackageFreshness(db),basis:'geopackage'};
  if(spec.feed)return {...feedFreshness(db,spec.feed),basis:'feed'};
  if(spec.sources)return {...sourcesFreshness(db,spec.sources,{cache}),basis:'sources'};
  const tables=spec.tables??(spec.collections??[]).map(c=>c.table);
  let best=null,seen=0;
  const keys=fileKeyCache(db,cache);
  for(const table of tables){
   if(fileKeyState(db,table,keys)!=='INDEXED')continue;
   const f=indexedTableFreshness(db,table);if(f){seen++;best=newer(best,f);}
  }
  return best?{...best,basis:spec.tables?'tables':'collections'}:{reason:seen?'NO_DATES':'NO_FILES',basis:spec.tables?'tables':'collections'};
 }catch{return {reason:'UNAVAILABLE',basis:spec.geopackage?'geopackage':spec.feed?'feed':spec.sources?'sources':'tables'};}
}
