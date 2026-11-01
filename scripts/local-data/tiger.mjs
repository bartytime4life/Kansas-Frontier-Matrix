// Census TIGER/Line 2025 features from the PC's Kansas GeoPackage: attributes, and a feature's
// shape on request. Small layers can be searched freely; the large per-county layers need an id,
// a county or a bounding box, each answered through an index or the layer's R-tree.
// Owner approval for public release: 2026-11-01.
import {only,text,oneOf,bbox,flag,int,fail} from './query.mjs';
import {gpkgToGeoJSON} from './gpkg.mjs';

// layer: [table, id column, name columns, county ('COLUMN' or {file:'suffix'}), large]
const LAYERS=Object.freeze({
 state:['us_state','GEOID',['NAME']],
 county:['us_county','GEOID',['NAME','NAMELSAD'],'COUNTYFP'],
 'county-subdivision':['ks_cousub','GEOID',['NAME','NAMELSAD'],'COUNTYFP'],
 place:['ks_place','GEOID',['NAME','NAMELSAD']],
 'consolidated-city':['ks_concity','GEOID',['NAME','NAMELSAD']],
 tract:['ks_tract','GEOID',['NAMELSAD'],'COUNTYFP'],
 'block-group':['ks_bg','GEOID',['NAMELSAD'],'COUNTYFP'],
 block:['ks_tabblock20','GEOID20',['NAME20'],'COUNTYFP20',true],
 'block-suffix':['ks_tabblocksufx','GEOID',['NAME'],'COUNTYFP',true],
 zcta:['us_zcta520','GEOID20',['ZCTA5CE20']],
 'school-district':['ks_unsd','GEOID',['NAME']],
 'state-house':['ks_sldl','GEOID',['NAMELSAD']],
 'state-senate':['ks_sldu','GEOID',['NAMELSAD']],
 'congressional-district':['ks_cd119','GEOID',['NAMELSAD']],
 puma:['ks_puma20','GEOID20',['NAMELSAD20']],
 'tribal-area':['us_aiannh','GEOID',['NAME','NAMELSAD']],
 'tribal-subdivision':['us_aitsn','GEOID',['NAME','NAMELSAD']],
 'tribal-tract':['us_ttract','GEOID',['NAME','NAMELSAD']],
 'tribal-block-group':['us_tbg','GEOID',['NAMELSAD']],
 cbsa:['us_cbsa','GEOID',['NAME','NAMELSAD']],
 csa:['us_csa','GEOID',['NAME','NAMELSAD']],
 'urban-area':['us_uac20','GEOID20',['NAME20','NAMELSAD20']],
 military:['us_mil','AREAID',['FULLNAME']],
 'area-landmark':['ks_arealm','AREAID',['FULLNAME']],
 'point-landmark':['ks_pointlm','POINTID',['FULLNAME']],
 'primary-roads':['us_primaryroads','LINEARID',['FULLNAME']],
 'primary-secondary-roads':['ks_prisecroads','LINEARID',['FULLNAME']],
 rails:['us_rails','LINEARID',['FULLNAME']],
 roads:['ks_roads','LINEARID',['FULLNAME'],{file:'roads'},true],
 'area-water':['ks_areawater','HYDROID',['FULLNAME'],{file:'areawater'},true],
 'linear-water':['ks_linearwater','LINEARID',['FULLNAME'],{file:'linearwater'},true],
 'address-ranges':['ks_addrfeat','TLID',['FULLNAME'],{file:'addrfeat'},true],
 edges:['ks_edges','TLID',['FULLNAME'],'COUNTYFP',true],
 faces:['ks_faces','TFID',[],'COUNTYFP',true],
});
export const TIGER_LAYERS=Object.freeze(Object.keys(LAYERS));
const INTEGER_IDS=new Set(['TLID','TFID']);

const indexes=[];
for(const [table,id,,county,large] of Object.values(LAYERS)){
 if(!large)continue;
 indexes.push({name:`kfm_${table}_id`,sql:`CREATE INDEX IF NOT EXISTS kfm_${table}_id ON "${table}"("${id}")`});
 const column=typeof county==='string'?county:'kfm_source_file';
 indexes.push({name:`kfm_${table}_county`,sql:`CREATE INDEX IF NOT EXISTS kfm_${table}_county ON "${table}"("${column}")`});
}

function columns(db,table,cache){
 const key='tiger-columns:'+table;
 if(!cache.has(key))cache.set(key,db.prepare(`SELECT name FROM pragma_table_info(?)`).all(table).map(r=>r.name).filter(c=>!['fid','geom','kfm_source_file'].includes(c)));
 return cache.get(key);
}

export const tigerFeatures={
 id:'tiger-features',db:'tiger',title:'Census TIGER/Line 2025 features',indexes,
 source:Object.freeze({provider:'U.S. Census Bureau TIGER/Line Shapefiles 2025',url:'https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html',
  coverage:'Kansas: statewide layers, county-merged layers, and national layers clipped to the Kansas bounding box',
  notes:'Coordinates are NAD83 (EPSG:4269) longitude/latitude, rounded to 6 decimals. Attributes are the TIGER columns as delivered.'}),
 params:{layer:TIGER_LAYERS.join(', ')+' (required)',id:'exact id (GEOID, AREAID, LINEARID, TLID ...)',name:'part of the name',
  county:'county FIPS, e.g. 173 or 20173 (required with name, or alone, for large layers)',bbox:'west,south,east,north (2 degrees at most)',
  geometry:'1 to include each feature\'s shape (at most 20 features)',limit:'1-200 (50); 1-20 (5) with geometry',offset:'0-100000'},
 parse(input){
  only(input,['layer','id','name','county','bbox','geometry','limit','offset']);
  const layer=oneOf(input.layer,TIGER_LAYERS,{required:true}),[,idColumn,names,countyKey,large]=LAYERS[layer];
  const raw=text(input.county,/^(?:\d{1,3}|20\d{3})$/);
  const geometry=flag(input.geometry);
  const q={layer,id:text(input.id,INTEGER_IDS.has(idColumn)?/^\d{1,12}$/:/^[A-Z0-9]{1,22}$/),name:text(input.name,/^[A-Z0-9][A-Z0-9 .,'&/()#-]{1,39}$/),
   county:raw===null?null:raw.length===5?raw.slice(2):raw.padStart(3,'0'),bbox:bbox(input.bbox),geometry,
   limit:int(input.limit,{min:1,max:geometry?20:200,fallback:geometry?5:50}),offset:int(input.offset,{min:0,max:100000,fallback:0})};
  if(q.county&&!countyKey)throw fail();
  if(q.name&&!names.length)throw fail();
  // Large layers: never a scan of the whole state.
  if(large&&!q.id&&!q.county&&!q.bbox)throw fail();
  return q;
 },
 run(db,q,{cache}){
  const [table,idColumn,names,countyKey]=LAYERS[q.layer];
  const where=[],params=[];let from=`"${table}" t`;
  if(q.bbox){from+=` JOIN "rtree_${table}_geom" r ON r.id=t.fid`;where.push('r.maxx>=? AND r.minx<=? AND r.maxy>=? AND r.miny<=?');params.push(q.bbox.west,q.bbox.east,q.bbox.south,q.bbox.north);}
  if(q.id){where.push(`t."${idColumn}"=?`);params.push(INTEGER_IDS.has(idColumn)?+q.id:q.id);}
  if(q.county){
   if(typeof countyKey==='string'){where.push(`t."${countyKey}"=?`);params.push(q.county);}
   else{where.push('t.kfm_source_file=?');params.push(`tl_2025_20${q.county}_${countyKey.file}.shp`);}
  }
  if(q.name){where.push('('+names.map(c=>`upper(t."${c}") LIKE ?`).join(' OR ')+')');params.push(...names.map(()=>'%'+q.name+'%'));}
  const clause=' FROM '+from+(where.length?' WHERE '+where.join(' AND '):'');
  const total=db.prepare('SELECT COUNT(*) AS n'+clause).get(...params).n;
  const attrs=columns(db,table,cache);
  const select='SELECT '+attrs.map(c=>`t."${c}"`).join(',')+(q.geometry?',t.geom':'');
  const rows=db.prepare(select+clause+` ORDER BY t."${idColumn}" LIMIT ? OFFSET ?`).all(...params,q.limit,q.offset).map(r=>{
   const attributes=Object.fromEntries(attrs.map(c=>[c,r[c]===undefined?null:r[c]]));
   const name=names.map(c=>r[c]).find(v=>v!==null&&v!==undefined&&v!=='')??null;
   return {layer:q.layer,id:r[idColumn]===null?null:String(r[idColumn]),name,attributes,...(q.geometry?{geometry:gpkgToGeoJSON(r.geom)}:{})};
  });
  return {total,rows};
 },
};
