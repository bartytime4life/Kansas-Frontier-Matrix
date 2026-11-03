// Public recovered records, authorized by the owner 2026-11-03. Identifiers come
// exclusively from a committed schema allowlist. No SQL, paths or arbitrary table
// names are accepted. Primary-key seek pagination never counts/scans whole tables.
import catalog from './recovered-catalog.json' with {type:'json'};
import {only,oneOf,int,fail} from './query.mjs';

const quote=s=>'"'+s+'"';
export const RECOVERED_COLLECTIONS=Object.freeze(catalog);
const source={provider:'Recovered public source records',url:'/data-library',
 coverage:'Archived editions; collection pages are not complete geographic coverage.',
 notes:'Original values, units, codes, flags and dates are retained. Import identity is not an observation date. Source links are attached to file-backed records. OpenStreetMap data © OpenStreetMap contributors, ODbL.'};
export function recoveredDataset(database){
 const collections=catalog.filter(c=>c.database===database), byId=new Map(collections.map(c=>[c.id,c]));
 return {id:'recovered-'+database,db:database,title:'Recovered '+database+' records',indexes:[],source,
  params:{collection:'allowlisted collection ID',after:'previous nextCursor, unchanged',limit:'1–50 (20)',record:'exact record identity for a long field',field:'allowlisted field name',start:'character offset for a long field'},
  parse(input){
   only(input,['collection','after','limit','record','field','start']);
   const collection=oneOf(input.collection,collections.map(c=>c.id),{required:true});
   let after=null;
   if(input.after!==undefined&&input.after!==null&&input.after!==''){
    if(typeof input.after!=='string'||input.after.length>2500)throw fail();
    try{after=JSON.parse(input.after);}catch{throw fail();}
    if(!Array.isArray(after)||after.length!==byId.get(collection).keys.length||after.some(v=>!(typeof v==='string'&&v.length<=512||typeof v==='number'&&Number.isSafeInteger(v))))throw fail();
   }
   let record=null,field=null,start=0;
   if(input.record!==undefined||input.field!==undefined||input.start!==undefined){
    if(after||typeof input.record!=='string'||input.record.length>2500)throw fail();
    try{record=JSON.parse(input.record);}catch{throw fail();}
    if(!Array.isArray(record)||record.length!==byId.get(collection).keys.length||record.some(v=>!(typeof v==='string'&&v.length<=512||typeof v==='number'&&Number.isSafeInteger(v))))throw fail();
    field=oneOf(input.field,byId.get(collection).columns,{required:true});
    start=int(input.start,{min:0,max:999999999,fallback:0});
   }
   return {collection,after,limit:int(input.limit,{min:1,max:50,fallback:20}),record,field,start};
  },
  run(db,q){
   const c=byId.get(q.collection);if(!c)throw fail();
   const keys=c.keys.map(quote), tuple=keys.length===1?keys[0]:'('+keys.join(',')+')';
   const parameters=keys.length===1?'?':'('+keys.map(()=>'?').join(',')+')';
   if(q.record){
    const field=quote(q.field),entry=db.prepare(`SELECT substr(${field},?,32768) AS value,length(${field}) AS characters FROM ${quote(c.table)} WHERE ${tuple} = ${parameters}`).get(q.start+1,...q.record);
    const nextStart=entry&&q.start+32768<entry.characters?q.start+32768:null;
    return {rows:entry?[{id:JSON.stringify(q.record),values:{[q.field]:entry.value}}]:[],total:null,collection:c.id,hasMore:false,nextCursor:null,fieldChunk:{field:q.field,start:q.start,nextStart,characters:entry?.characters??0}};
   }
   const sql=`SELECT ${c.columns.map(quote).join(',')} FROM ${quote(c.table)} ${q.after?`WHERE ${tuple} > ${parameters}`:''} ORDER BY ${keys.join(',')} LIMIT ?`;
   const page=db.prepare(sql).all(...(q.after??[]),q.limit+1), hasMore=page.length>q.limit;
   const rows=page.slice(0,q.limit).map(values=>({id:JSON.stringify(c.keys.map(k=>values[k])),values}));
   const sources=new Map();
   if(c.columns.includes('file_id')){
    const lookup=db.prepare('SELECT source_id, source_url, sha256 FROM kfm_sql_sources WHERE file_id=?');
    for(const row of rows){const id=row.values.file_id;if(!sources.has(id))sources.set(id,lookup.get(id)??null);row.provenance=sources.get(id);}
   }
   // An unusually large polygon/OCR cell must not make the whole collection
   // impossible to page. Mark each omitted cell explicitly; the exact text is
   // available in bounded character chunks through the same signed endpoint.
   for(const row of rows){
    if(Buffer.byteLength(JSON.stringify(row))<=650000)continue;
    const largest=Object.entries(row.values).filter(([,v])=>typeof v==='string').sort((a,b)=>b[1].length-a[1].length);
    for(const [field,value] of largest){
     row.values[field]={longField:true,preview:value.slice(0,256),message:'Open full field to read all text in parts.'};
     if(Buffer.byteLength(JSON.stringify(row))<=650000)break;
    }
   }
   return {rows,total:null,collection:c.id,hasMore,nextCursor:hasMore?rows.at(-1).id:null,
    columns:c.columns,coverage:'One record page, ordered by import identity; not a spatial search or full collection.',geometryField:c.geometry};
  },
 };
}
export const recoveredObservations=recoveredDataset('observations');
export const recoveredBulk=recoveredDataset('bulk');
