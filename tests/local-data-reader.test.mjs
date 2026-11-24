import test from 'node:test';
import assert from 'node:assert/strict';
import {DatabaseSync} from 'node:sqlite';
import {createDatabaseReader} from '../scripts/local-data/database-reader.mjs';
import {USGS_CAPTURE_INDEX} from '../scripts/local-data/water.mjs';
import {usgsStreamflow} from '../scripts/local-data/water.mjs';

test('health opens each configured database once, closes it, and reports unavailable datasets honestly',()=>{
 const opened=[],closed=[];
 const read=createDatabaseReader({databases:{observations:'obs',bulk:'bulk'},open:path=>{
  opened.push(path);const db=new DatabaseSync(':memory:');
  db.exec('CREATE TABLE kfm_storm_event_details(event_id TEXT)');
  const close=db.close.bind(db);db.close=()=>{closed.push(path);close();};return db;
 }});
 const h=read({kind:'health'});
 assert.equal(h.ok,true);assert.equal(h.stormEvents,0);assert.equal(h.datasets.length,22);
 assert.deepEqual(opened.sort(),['bulk','obs']);assert.deepEqual(closed.sort(),['bulk','obs']);
 assert.equal(h.datasets.find(d=>d.id==='nwm-reaches').ready,false);
});

test('the USGS expression index searches a site and minute range without changing minute boundaries',t=>{
 const db=new DatabaseSync(':memory:');t.after(()=>db.close());
 db.exec('CREATE TABLE kfm_environmental_features(source_id TEXT,feature_json TEXT)');
 const add=db.prepare('INSERT INTO kfm_environmental_features VALUES(?,?)');
 for(const [source,time,parameter] of [['usgs-streamflow','2026-11-01T12:00:59Z','00060'],['usgs-streamflow','2026-11-01T12:01:00Z','00060'],['usgs-streamflow','2026-11-01T12:00:30Z','00065'],['other','2026-11-01T12:00:00Z','00060']])
  add.run(source,JSON.stringify({type:'Feature',properties:{monitoring_location_id:'USGS-06864500',time,parameter_code:parameter,value:1}}));
 db.exec(USGS_CAPTURE_INDEX.sql);
 const statements=[],wrapped={prepare:sql=>{statements.push(sql);return db.prepare(sql);}};
 const result=usgsStreamflow.run(wrapped,usgsStreamflow.parse({site:'USGS-06864500',from:'2026-11-01T12:00',to:'2026-11-01T12:00',parameter:'00060'}));
 assert.equal(result.total,1);assert.equal(result.rows[0].time,'2026-11-01T12:00:59Z');
 const plan=db.prepare('EXPLAIN QUERY PLAN '+statements[0]).all('USGS-06864500','2026-11-01T12:00','2026-11-01T12:00','00060').map(x=>x.detail).join(' ');
 assert.match(plan,/SEARCH.*kfm_environmental_usgs_site_minute_cover/);
});

test('an index dropped after a successful query is detected before the next read',t=>{
 const db=new DatabaseSync(':memory:');t.after(()=>db.close());
 db.exec('CREATE TABLE kfm_environmental_features(source_id TEXT,feature_json TEXT)');
 db.exec(USGS_CAPTURE_INDEX.sql);
 const read=createDatabaseReader({databases:{observations:'fixture'},open:()=>({prepare:sql=>db.prepare(sql),close(){}})});
 const ask={kind:'dataset',id:'usgs-streamflow',input:{site:'USGS-06864500'}};
 assert.equal(read(ask).result.total,0);
 db.exec('DROP INDEX '+USGS_CAPTURE_INDEX.name);
 assert.throws(()=>read(ask),{code:'DATASET_NOT_READY'});
});
