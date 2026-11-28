import test from 'node:test';
import assert from 'node:assert/strict';
import {DatabaseSync} from 'node:sqlite';
import {NEAR_COLLECTIONS,nearObservations,nearBulk,sidecarState,TOTAL_CAP} from '../scripts/local-data/near.mjs';
import {RECOVERED_COLLECTIONS} from '../scripts/local-data/recovered.mjs';
import {DATASETS} from '../scripts/local-data/datasets.mjs';
import {LOCAL_DATA_ROUTES} from '../scripts/local-data/protocol.mjs';
import {mkdtempSync,readFileSync,rmSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {createHash} from 'node:crypto';
import {createGateway} from '../scripts/local-data/gateway.mjs';
import {newSecret,signRequest,RESPONSE_SIGNATURE_HEADER} from '../scripts/home-inference/signature.mjs';
import {localDataConfig,createLocalDataService,LOCAL_DATA_CACHE} from '../server/local-data.mjs';

const c=NEAR_COLLECTIONS.find(c=>c.id==='observations-nrhp-locations');
const key=(file,row)=>(BigInt(file)<<32n)|BigInt(row);
const point=(lon,lat)=>JSON.stringify({type:'Point',coordinates:[lon,lat]});
// The pipeline's sidecar as tools/local_data/sql_spatial.py writes it: an R-tree keyed by file_id<<32|row_number
// and kfm_spatial_index recording the files it covers.
function fixture(t,{sidecar=true,state=true,path=':memory:'}={}){
 const db=new DatabaseSync(path);t.after(()=>db.close());
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

test('exact-cap and capped geographic pages retain their qualification through the read-only signed gateway and live, fresh and stale responses',async t=>{
 const directory=mkdtempSync(join(tmpdir(),'kfm-near-')),path=join(directory,'observations.sqlite');
 const db=fixture(t,{path});t.after(()=>rmSync(directory,{recursive:true,force:true}));
 const insert=db.prepare(`INSERT INTO "${c.table}"(file_id,row_number,resname,geometry_geojson) VALUES(1,?,?,?)`),rt=db.prepare(`INSERT INTO "${c.table}_rtree" VALUES(?,?,?,?,?)`);
 db.exec('BEGIN');
 for(let i=0;i<TOTAL_CAP-3;i++){insert.run(100+i,'Many '+i,point(-97.3,37.7));rt.run(key(1,100+i),-97.3,-97.3,37.7,37.7);}
 db.exec('COMMIT');
 const input={collection:c.id,bbox:WICHITA,limit:'50'};
 const exact=run(db,input);assert.equal(exact.total,TOTAL_CAP);assert.equal(exact.totalCapped,false);
 insert.run(20000,'One more',point(-97.3,37.7));rt.run(key(1,20000),-97.3,-97.3,37.7,37.7);
 const next=run(db,{...input,offset:'50'}),first=run(db,input);
 assert.equal(first.totalCapped,true);assert.equal(next.totalCapped,true);
 assert.equal(first.rows.length,50);assert.equal(next.rows.length,50);
 assert.equal(new Set([...first.rows,...next.rows].map(r=>r.id)).size,100);
 assert.equal(run(db,{...input,offset:'5000',limit:'200'}).rows.length,200);
 assert.equal(run(db,{...input,bbox:'-103,36.5,-102.5,37'}).totalCapped,false);
 const hash=()=>createHash('sha256').update(readFileSync(path)).digest('hex'),before=hash();
 let now=Date.now(),offline=false,calls=0;
 const origin='https://kansasfrontiermatrix.com',config=localDataConfig({KFM_LOCAL_DATA:'1',KFM_LOCAL_DATA_ORIGIN:origin,KFM_LOCAL_DATA_GATEWAY_KEY_ID:'gw',KFM_LOCAL_DATA_GATEWAY_SECRET:newSecret(),KFM_LOCAL_DATA_WORKER_KEY_ID:'wk',KFM_LOCAL_DATA_WORKER_SECRET:newSecret()});
 const gateway=createGateway({keyId:config.keyId,secret:config.secret,dbPath:path,clock:()=>now});
 const relay={lastSeen:now,handler:async()=>new Response(null,{status:204}),async submit({method,path,body}){
  calls++;if(offline)throw Error('Controlled outage');
  const requestHeaders=signRequest({keyId:config.keyId,secret:config.secret,method,path,body,now});
  const reply=gateway({method,path,body,headers:requestHeaders});
  assert.equal(reply.status,200);assert.equal(JSON.parse(reply.body).totalCapped,true);
  return {status:reply.status,bytes:reply.body,requestHeaders,headers:new Headers({'content-type':'application/json',[RESPONSE_SIGNATURE_HEADER]:reply.signature})};
 }};
 const service=createLocalDataService({config,relay,clock:()=>now});
 const query=()=>service.query(new Request(origin+'/api/local-data/near-observations?'+new URLSearchParams(input)),'near-observations');
 for(const state of ['live','fresh','stale']){
  if(state==='stale'){offline=true;now+=LOCAL_DATA_CACHE.freshMs;relay.lastSeen=now;}
  const response=await query();assert.equal(response.status,200);const value=await response.json();
  assert.equal(value.cache.state,state);assert.equal(value.total,10000);assert.equal(value.totalCapped,true);assert.equal(value.count,50);
  assert.deepEqual(value.rows[0].provenance,{...first.rows[0].provenance});assert.equal(value.collection,c.id);
 }
 assert.equal(calls,2);assert.equal(hash(),before,'read-only geographic queries leave database bytes unchanged');
});


test('wide payload projection is limited to returned page rows, including named searches and offsets',t=>{
 const db=fixture(t);let payloadReads=0;
 db.function('tracked_payload',value=>{payloadReads++;return value;});
 db.exec(`ALTER TABLE "${c.table}" RENAME TO raw_near_records;
  CREATE VIEW "${c.table}" AS SELECT ${c.columns.map(k=>k===c.geometry?`tracked_payload("${k}") AS "${k}"`:`"${k}"`).join(',')} FROM raw_near_records;`);
 for(const input of [{offset:'1',limit:'1'},{offset:'2',limit:'1'},{name:'I',offset:'1',limit:'1'},{offset:'3',limit:'1'}]){
  payloadReads=0;const answer=run(db,{collection:c.id,bbox:WICHITA,...input});
  assert.equal(payloadReads,answer.rows.length,JSON.stringify(input));
  assert.equal(answer.rows.length,input.offset==='3'?0:1);
  if(answer.rows.length)assert.deepEqual(JSON.parse(answer.rows[0].values.geometry_geojson).type,input.offset==='2'?'LineString':'Point');
 }
});

test('orphan sidecar identities do not consume paginated result slots',t=>{
 const db=fixture(t);
 db.prepare(`INSERT INTO "${c.table}_rtree" VALUES(?,?,?,?,?)`).run(key(1,0),-97.33,-97.33,37.69,37.69);
 const all=run(db,{collection:c.id,bbox:WICHITA,limit:'10'});
 assert.deepEqual(all.rows.map(r=>JSON.parse(r.id)),[[1,1],[1,2],[1,4]]);
 // The existing nameless total counts sidecar extents, including its orphan.
 assert.equal(all.total,4);
 const first=run(db,{collection:c.id,bbox:WICHITA,limit:'2'});
 assert.deepEqual(first.rows,all.rows.slice(0,2));
 const next=run(db,{collection:c.id,bbox:WICHITA,offset:'2',limit:'2'});
 assert.deepEqual(next.rows,all.rows.slice(2));
 const named=run(db,{collection:c.id,bbox:WICHITA,name:'I',limit:'2'});
 assert.deepEqual(named.rows,all.rows.slice(0,2));assert.equal(named.total,3);
});

test('packed spatial identities above the JavaScript safe-integer range stay inside SQLite',t=>{
 const db=fixture(t),file=2**22;
 db.prepare(`INSERT INTO "${c.table}"(file_id,row_number,resname,geometry_geojson) VALUES(?,?,?,?)`).run(file,1,'Large capture key',point(-97.33,37.69));
 db.prepare(`INSERT INTO "${c.table}_rtree" VALUES(?,?,?,?,?)`).run(key(file,1),-97.33,-97.33,37.69,37.69);
 db.prepare('UPDATE kfm_spatial_index SET max_file_id=? WHERE table_name=?').run(file,c.table);
 const answer=run(db,{collection:c.id,bbox:WICHITA,offset:'3',limit:'1'});
 assert.equal(answer.rows.length,1);assert.deepEqual(JSON.parse(answer.rows[0].id),[file,1]);
 assert.equal(answer.rows[0].values.resname,'Large capture key');
});

test('unnamed pages stop source identity lookups after the valid prefix, while orphan extents do not consume offsets',t=>{
 const db=fixture(t);
 const insert=db.prepare(`INSERT INTO "${c.table}"(file_id,row_number,resname,geometry_geojson) VALUES(1,?,?,?)`),rt=db.prepare(`INSERT INTO "${c.table}_rtree" VALUES(?,?,?,?,?)`);
 rt.run(key(1,0),-97.3,-97.3,37.7,37.7);
 for(let i=100;i<1100;i++){insert.run(i,'Later record '+i,point(-97.3,37.7));rt.run(key(1,i),-97.3,-97.3,37.7,37.7);}
 let identities=0,existenceLookups=0,payloadLookups=0;
 const tracked={prepare(sql){
  const statement=db.prepare(sql);
  return {all:(...args)=>statement.all(...args),get(...args){
   if(sql.includes(`FROM "${c.table}" WHERE file_id=?`))existenceLookups++;
   if(sql.includes(`FROM "${c.table}" t WHERE t.file_id=?`))payloadLookups++;
   return statement.get(...args);
  },*iterate(...args){for(const value of statement.iterate(...args)){identities++;yield value;}}};
 }};
 const answer=run(tracked,{collection:c.id,bbox:WICHITA,offset:'2',limit:'1'});
 assert.deepEqual(answer.rows.map(r=>r.id),['[1,4]']);
 assert.equal(answer.total,1004);assert.equal(identities,4);
 assert.equal(existenceLookups,3);assert.equal(payloadLookups,1);
 // Early iterator closure must allow the same connection to serve another page.
 assert.deepEqual(run(db,{collection:c.id,bbox:WICHITA,limit:'1'}).rows.map(r=>r.id),['[1,1]']);
});
