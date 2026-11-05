// "What is in this map area": the recovered geometry collections answered through the R-tree sidecars
// the pipeline keeps beside each geometry table (tools/local_data/sql_spatial.py: <table>_rtree keyed by
// file_id<<32|row_number, and kfm_spatial_index recording the files each sidecar covers). Identifiers
// come only from the committed catalog; a sidecar that is missing, or stale because the table holds a
// newer file than it was built from, refuses the collection rather than answer from the wrong rows.
// The same records remain readable one page at a time through recovered-*. No dependencies.
import catalog from './recovered-catalog.json' with {type:'json'};
import {only,text,oneOf,bbox,page,fail} from './query.mjs';

const quote=s=>'"'+s+'"';
// The first of these a collection has is its searchable name.
const NAME_COLUMNS=['name','primary_name','title','label','feature_name','facility_name','site_name','entity_name','dam_name','resname','sitename','map_name','unit_name','parkname',
 'current_mine_name','rrname','railroadname','col_name','ftr_name','rdname','trlname','poiname','bldgname','maplabel','arpt_id','structure_number_008','oas_number','registration_number',
 'crossingid','pointlab','survlab','frstdivlab','plssid','cessnum','tract_id','fclass','pgm_sys_id','station_id','registry_id','lccn','identifier'];
const NAME=/^[A-Z0-9][A-Z0-9 .,'&/()#-]{0,39}$/;
export const TOTAL_CAP=10000;
export const NEAR_COLLECTIONS=Object.freeze(catalog.filter(c=>c.geometry).map(c=>Object.freeze({...c,nameColumn:NAME_COLUMNS.find(n=>c.columns.includes(n))??null})));
const notReady=()=>Object.assign(new Error('DATASET_NOT_READY'),{code:'DATASET_NOT_READY'});
const source={provider:'Recovered public source records',url:'/data-library',
 coverage:'Every record whose bounding box touches the asked area, in record-identity order; a page is one slice of that set, never the whole state. The area is at most 2 degrees on a side.',
 notes:'Original values, units, codes, flags and dates are retained; geometry is the source\'s own. Bounding boxes come from the stored geometry, so a long line or large area can be returned for a small window it crosses. OpenStreetMap data © OpenStreetMap contributors, ODbL.'};

/** The sidecar's record for a table, or null; throws DATASET_NOT_READY when the table holds files the sidecar was not built from. */
export function sidecarState(db,table){
 if(!db.prepare("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?").get('kfm_spatial_index'))return null;
 const state=db.prepare('SELECT max_file_id,entries FROM kfm_spatial_index WHERE table_name=?').get(table);
 if(!state||!db.prepare("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?").get(table+'_rtree'))return null;
 const greatest=db.prepare(`SELECT MAX(file_id) AS m FROM ${quote(table)}`).get().m;
 if((greatest??null)!==(state.max_file_id??null))throw notReady();
 return state;
}

export function nearDataset(database){
 const collections=NEAR_COLLECTIONS.filter(c=>c.database===database),byId=new Map(collections.map(c=>[c.id,c]));
 return {id:'near-'+database,db:database,title:'Recovered '+database+' records in a map area',indexes:[],source,freshness:{collections},
  params:{collection:'allowlisted geometry collection ID',bbox:'west,south,east,north (required; at most 2 degrees a side)',name:'part of the record\'s name (collections that have one)',limit:'1–200 (50)',offset:'0–5000'},
  parse(input){
   only(input,['collection','bbox','name','limit','offset']);
   const collection=oneOf(input.collection,collections.map(c=>c.id),{required:true}),c=byId.get(collection);
   const box=bbox(input.bbox);if(!box)throw fail();
   const name=text(input.name,NAME);
   if(name&&!c.nameColumn)throw fail();
   return {collection,bbox:box,name,...page(input,{max:200,fallback:50,maxOffset:5000})};
  },
  run(db,q){
   const c=byId.get(q.collection);if(!c)throw fail();
   if(!sidecarState(db,c.table))throw notReady();
   const t=quote(c.table),r=quote(c.table+'_rtree');
   const where=['r.min_lon<=? AND r.max_lon>=? AND r.min_lat<=? AND r.max_lat>=?'],params=[q.bbox.east,q.bbox.west,q.bbox.north,q.bbox.south];
   const join=`FROM ${r} r JOIN ${t} t ON t.file_id = (r.id >> 32) AND t.row_number = (r.id & 4294967295)`;
   if(q.name){where.push(`upper(t.${quote(c.nameColumn)}) LIKE ?`);params.push('%'+q.name+'%');}
   const clause=`${join} WHERE ${where.join(' AND ')}`;
   // Without a name filter the count needs only the sidecar.
   const counted=db.prepare(`SELECT COUNT(*) AS n FROM (SELECT r.id ${q.name?clause:`FROM ${r} r WHERE ${where[0]}`} LIMIT ?)`).get(...params,TOTAL_CAP+1).n;
   const rows=db.prepare(`SELECT ${c.columns.map(k=>'t.'+quote(k)).join(',')} ${clause} ORDER BY r.id LIMIT ? OFFSET ?`).all(...params,q.limit,q.offset)
    .map(values=>({id:JSON.stringify(c.keys.map(k=>values[k])),values}));
   const sources=new Map();
   if(c.columns.includes('file_id')){
    const lookup=db.prepare('SELECT source_id, source_url, sha256 FROM kfm_sql_sources WHERE file_id=?');
    for(const row of rows){const id=row.values.file_id;if(!sources.has(id))sources.set(id,lookup.get(id)??null);row.provenance=sources.get(id);}
   }
   // As in recovered.mjs: one oversized cell must not block the page; its full text stays readable through recovered-*.
   for(const row of rows){
    if(Buffer.byteLength(JSON.stringify(row))<=650000)continue;
    const largest=Object.entries(row.values).filter(([,v])=>typeof v==='string').sort((a,b)=>b[1].length-a[1].length);
    for(const [field,value] of largest){
     row.values[field]={longField:true,preview:value.slice(0,256),message:'Open full field to read all text in parts.'};
     if(Buffer.byteLength(JSON.stringify(row))<=650000)break;
    }
   }
   return {rows,total:Math.min(counted,TOTAL_CAP),totalCapped:counted>TOTAL_CAP,collection:c.id,columns:c.columns,geometryField:c.geometry,nameColumn:c.nameColumn,
    coverage:'Records whose bounding box touches the asked area, in record-identity order.'};
  },
 };
}
export const nearObservations=nearDataset('observations');
export const nearBulk=nearDataset('bulk');
