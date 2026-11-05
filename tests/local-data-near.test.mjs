import test from 'node:test';
import assert from 'node:assert/strict';
import {DatabaseSync} from 'node:sqlite';
import {NEAR_COLLECTIONS,nearObservations,nearBulk,sidecarState,TOTAL_CAP} from '../scripts/local-data/near.mjs';
import {RECOVERED_COLLECTIONS} from '../scripts/local-data/recovered.mjs';
import {DATASETS} from '../scripts/local-data/datasets.mjs';
import {LOCAL_DATA_ROUTES} from '../scripts/local-data/protocol.mjs';

const c=NEAR_COLLECTIONS.find(c=>c.id==='observations-nrhp-locations');
const key=(file,row)=>(BigInt(file)<<32n)|BigInt(row);
const point=(lon,lat)=>JSON.stringify({type:'Point',coordinates:[lon,lat]});
// The pipeline's sidecar as tools/local_data/sql_spatial.py writes it: an R-tree keyed by file_id<<32|row_number
// and kfm_spatial_index recording the files it covers.
function fixture(t,{sidecar=true,state=true}={}){
 const db=new DatabaseSync(':memory:');t.after(()=>db.close());
 db.exec(`CREATE TABLE "${c.table}"(${c.columns.map(k=>`"${k}" ${c.keys.includes(k)?'INTEGER NOT NULL':'TEXT'}`).join(',')},PRIMARY KEY(${c.keys.join(',')}));
  CREATE TABLE kfm_sql_sources(file_id INTEGER PRIMARY KEY,source_id TEXT,source_url TEXT,sha256 TEXT,source_path TEXT);
  INSERT INTO kfm_sql_sources VALUES(1,'nps-nrhp','https://example.org/nrhp','hash','/private/path'),(2,'nps-nrhp','https://example.org/nrhp2','hash2','/private/path2');`);
 const insert=db.prepare(`INSERT INTO "${c.table}"(file_id,row_number,resname,city,geometry_geojson) VALUES(?,?,?,?,?)`);
 const rows=[[1,1,'Old Mill','Wichita',point(-97.33,37.69)],[1,2,'Union Station','Wichita',point(-97.34,37.68)],[1,3,'Court House','Topeka',point(-95.68,39.05)],
  [1,4,'Long Trail','Statewide',JSON.stringify({type:'LineString',coordinates:[[-101,37],[-95,39.5]]})],[1,5,'No place','Unknown',null],[2,1,'Fort','Leavenworth',point(-94.92,39.32)]];
 for(const r of rows)insert.run(...r);
 if(!sidecar)return db;
 db.exec(`CREATE VIRTUAL TABLE "${c.table}_rtree" USING rtree(id,min_lon,max_lon,min_lat,max_lat);`);
 const rt=db.prepare(`INSERT INTO "${c.table}_rtree" VALUES(?,?,?,?,?)`);
 rt.run(key(1,1),-97.33,-97.33,37.69,37.69);rt.run(key(1,2),-97.34,-97.34,37.68,37.68);rt.run(key(1,3),-95.68,-95.68,39.05,39.05);
 rt.run(key(1,4),-101,-95,37,39.5);rt.run(key(2,1),-94.92,-94.92,39.32,39.32);
 if(state)db.exec(`CREATE TABLE kfm_spatial_index(table_name TEXT PRIMARY KEY,file_ids_json TEXT NOT NULL,max_file_id INTEGER,entries INTEGER NOT NULL,updated_at TEXT NOT NULL) WITHOUT ROWID;
  INSERT INTO kfm_spatial_index VALUES('${c.table}','[1,2]',2,5,'2026-11-05T00:00:00Z');`);
 return db;
}
const run=(db,input)=>nearObservations.run(db,nearObservations.parse(input),{cache:new Map()});
const WICHITA='-97.5,37.5,-97.2,37.8';

test('every geometry collection is reachable, keyed by file and row, and most have a searchable name',()=>{
 assert.equal(NEAR_COLLECTIONS.length,RECOVERED_COLLECTIONS.filter(c=>c.geometry).length);
 assert.ok(NEAR_COLLECTIONS.every(c=>c.keys.join()==='file_id,row_number'));
 assert.ok(NEAR_COLLECTIONS.filter(c=>c.nameColumn).length>=NEAR_COLLECTIONS.length-6);
 assert.equal(c.nameColumn,'resname');
 assert.equal(NEAR_COLLECTIONS.find(c=>c.id==='bulk-osm-elements').nameColumn,'name');
 for(const id of ['near-observations','near-bulk']){assert.ok(DATASETS.has(id));assert.equal(LOCAL_DATA_ROUTES.get('/v1/data/'+id),'POST');}
});

test('the question needs a collection and a bounded area; names and pages are bounded; other collections are refused',()=>{
 assert.deepEqual(nearObservations.parse({collection:c.id,bbox:WICHITA,name:'mill',limit:'10'}),{collection:c.id,bbox:{west:-97.5,south:37.5,east:-97.2,north:37.8},name:'MILL',limit:10,offset:0});
 for(const bad of [{collection:c.id},{bbox:WICHITA},{collection:c.id,bbox:'-100,37,-97,38'},{collection:c.id,bbox:WICHITA,limit:'201'},{collection:c.id,bbox:WICHITA,offset:'5001'},
  {collection:c.id,bbox:WICHITA,name:'a;b'},{collection:c.id,bbox:WICHITA,after:'[1,1]'},{collection:'observations-ahcb-changes',bbox:WICHITA},{collection:'bulk-osm-elements',bbox:WICHITA},{collection:c.table,bbox:WICHITA}])
  assert.throws(()=>nearObservations.parse(bad),{code:'QUERY_INVALID'},JSON.stringify(bad));
 assert.throws(()=>nearBulk.parse({collection:c.id,bbox:WICHITA}),{code:'QUERY_INVALID'});
 const noName=NEAR_COLLECTIONS.find(c=>!c.nameColumn);
 assert.throws(()=>nearObservations.parse({collection:noName.id,bbox:WICHITA,name:'x'}),{code:'QUERY_INVALID'});
 assert.doesNotThrow(()=>nearObservations.parse({collection:noName.id,bbox:WICHITA}));
});

test('records whose extent touches the area come back in record order with geometry, provenance and a bounded total',t=>{
 const db=fixture(t),a=run(db,{collection:c.id,bbox:WICHITA});
 assert.deepEqual(a.rows.map(r=>r.values.resname),['Old Mill','Union Station','Long Trail']);
 assert.deepEqual(a.rows.map(r=>r.id),['[1,1]','[1,2]','[1,4]']);
 assert.equal(a.total,3);assert.equal(a.totalCapped,false);assert.equal(a.collection,c.id);assert.equal(a.geometryField,'geometry_geojson');assert.equal(a.nameColumn,'resname');
 assert.equal(a.rows[0].provenance.source_url,'https://example.org/nrhp');assert.ok(!JSON.stringify(a).includes('/private/'));
 assert.deepEqual(JSON.parse(a.rows[0].values.geometry_geojson).coordinates,[-97.33,37.69]);
 assert.deepEqual(run(db,{collection:c.id,bbox:'-95,39,-94.5,39.5'}).rows.map(r=>r.values.resname),['Long Trail','Fort']);
 assert.deepEqual(run(db,{collection:c.id,bbox:WICHITA,name:'station'}).rows.map(r=>r.values.resname),['Union Station']);
 assert.deepEqual(run(db,{collection:c.id,bbox:WICHITA,limit:'1',offset:'1'}).rows.map(r=>r.values.resname),['Union Station']);
 assert.equal(run(db,{collection:c.id,bbox:'-103,36.5,-102.5,37'}).total,0);
});

test('a missing or stale sidecar refuses the collection instead of answering from the wrong rows',t=>{
 assert.throws(()=>run(fixture(t,{sidecar:false}),{collection:c.id,bbox:WICHITA}),{code:'DATASET_NOT_READY'});
 assert.throws(()=>run(fixture(t,{state:false}),{collection:c.id,bbox:WICHITA}),{code:'DATASET_NOT_READY'});
 const db=fixture(t);
 assert.equal(run(db,{collection:c.id,bbox:WICHITA}).total,3);
 // The feed replaced file 2 with file 3; until the pipeline refreshes the sidecar the collection waits.
 db.exec(`DELETE FROM "${c.table}" WHERE file_id=2;INSERT INTO "${c.table}"(file_id,row_number,resname,city,geometry_geojson) VALUES(3,1,'Fort again','Leavenworth','${point(-94.92,39.32)}');`);
 assert.throws(()=>run(db,{collection:c.id,bbox:WICHITA}),{code:'DATASET_NOT_READY'});
 assert.throws(()=>sidecarState(db,c.table),{code:'DATASET_NOT_READY'});
 db.exec(`UPDATE kfm_spatial_index SET file_ids_json='[1,3]',max_file_id=3 WHERE table_name='${c.table}'`);
 assert.equal(run(db,{collection:c.id,bbox:WICHITA}).total,3);
 assert.equal(sidecarState(db,'kfm_nothing'),null);
});

test('the count stops at the cap and the name is a bound value',t=>{
 const db=fixture(t);
 const insert=db.prepare(`INSERT INTO "${c.table}"(file_id,row_number,resname,city,geometry_geojson) VALUES(1,?,?,?,?)`),rt=db.prepare(`INSERT INTO "${c.table}_rtree" VALUES(?,?,?,?,?)`);
 for(let i=0;i<TOTAL_CAP+3;i++){insert.run(100+i,'Many '+i,'Wichita',point(-97.3,37.7));rt.run(key(1,100+i),-97.3,-97.3,37.7,37.7);}
 const a=run(db,{collection:c.id,bbox:WICHITA,limit:'200'});
 assert.equal(a.total,TOTAL_CAP);assert.equal(a.totalCapped,true);assert.equal(a.rows.length,200);
 assert.throws(()=>run(db,{collection:c.id,bbox:WICHITA,name:"MILL' OR 1=1 --"}),{code:'QUERY_INVALID'});
 assert.equal(run(db,{collection:c.id,bbox:WICHITA,name:"MILL' OR '"}).total,0);
 assert.throws(()=>run(db,{collection:c.id,bbox:WICHITA,name:"%"}),{code:'QUERY_INVALID'});
 assert.equal(db.prepare(`SELECT COUNT(*) n FROM "${c.table}"`).get().n,TOTAL_CAP+9);
});
