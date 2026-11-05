import test from 'node:test';
import assert from 'node:assert/strict';
import {DatabaseSync} from 'node:sqlite';
import {DATASETS} from '../scripts/local-data/datasets.mjs';
import {WARM_QUESTIONS,questionsFor,warm,summarize} from '../scripts/local-data/warm.mjs';

test('every published dataset has a warm question its own parse() accepts, and no question names an unpublished dataset',()=>{
 for(const dataset of DATASETS.values()){
  const questions=questionsFor(dataset.id);
  assert.ok(questions.length>=1,dataset.id+' has no warm question');
  for(const question of questions)assert.doesNotThrow(()=>dataset.parse(question),dataset.id+' refuses its warm question '+JSON.stringify(question));
 }
 for(const id of Object.keys(WARM_QUESTIONS))assert.ok(DATASETS.has(id),'warm question for unknown dataset '+id);
});

test('a warm pass reports every question, keeps going past failures, opens each database once and closes it',()=>{
 const opens=[],closed=[];
 const open=path=>{opens.push(path);const db=new DatabaseSync(':memory:');const close=db.close.bind(db);db.close=()=>{closed.push(path);close();};return db;};
 const clock=(()=>{let t=1000;return ()=>t+=7;})();
 const result=warm({databases:{observations:'obs.sqlite',bulk:'bulk.sqlite'},open,clock});
 // One entry per question, then one freshness entry per dataset (what the health route reads).
 const expected=[...DATASETS.values()].reduce((n,d)=>n+questionsFor(d.id).length,0);
 const questions=result.datasets.filter(e=>e.question!=='freshness'),freshness=result.datasets.filter(e=>e.question==='freshness');
 assert.equal(questions.length,expected);
 assert.equal(freshness.length,DATASETS.size);
 for(const entry of questions){
  assert.ok(DATASETS.has(entry.id));
  assert.ok(Number.isInteger(entry.question)&&entry.question>=0);
  assert.ok(entry.ms>0,'each question is timed');
 }
 // Empty databases have no tables: every question on them fails without stopping the pass.
 const byDb=id=>DATASETS.get(id).db;
 assert.ok(questions.filter(e=>byDb(e.id)==='observations').every(e=>e.status!=='ok'));
 assert.ok(questions.filter(e=>byDb(e.id)==='tiger'||byDb(e.id)==='nwm').every(e=>e.status==='DATABASE_NOT_CONFIGURED'));
 assert.ok(freshness.every(e=>typeof e.status==='string'&&e.ms>0));
 assert.equal(result.stormEvents,null);
 assert.deepEqual([...opens].sort(),['bulk.sqlite','obs.sqlite'],'each configured database is opened once');
 assert.deepEqual([...closed].sort(),['bulk.sqlite','obs.sqlite'],'and closed at the end');
 assert.ok(result.ms>0);
});

test('a dataset whose index is missing is reported DATASET_NOT_READY, and one with its tables answers ok',()=>{
 const open=()=>{
  const db=new DatabaseSync(':memory:');
  db.exec(`CREATE TABLE kfm_ghcnd_stations(station_id TEXT,name TEXT,latitude REAL,longitude REAL,elevation_m REAL,metadata_json TEXT);
   INSERT INTO kfm_ghcnd_stations VALUES('USW00003928','WICHITA',37.65,-97.43,407,'{}');
   CREATE TABLE kfm_ghcnd_daily(file_id INTEGER,row_number INTEGER,observation_day INTEGER,element TEXT,raw_value INTEGER,measurement_flag TEXT,quality_flag TEXT,source_flag TEXT,observation_time TEXT);
   CREATE TABLE kfm_sql_sources(file_id INTEGER, source_id TEXT, source_path TEXT, source_url TEXT);
   CREATE TABLE kfm_storm_event_details(event_id TEXT);`);
  return db;
 };
 const result=warm({databases:{observations:'obs.sqlite'},open,questions:{'ghcn-stations':{name:'WICHITA'},'ghcn-daily':{station:'USW00003928'}}});
 const status=Object.fromEntries(result.datasets.filter(e=>e.question!=='freshness').map(e=>[e.id,e.status]));
 // No bookkeeping tables in this fixture: freshness is a reason for every dataset, never a throw.
 assert.ok(result.datasets.filter(e=>e.question==='freshness').every(e=>['INDEX_MISSING','NO_FEED_STATE','NO_FILES','DATABASE_NOT_CONFIGURED','UNAVAILABLE'].includes(e.status)));
 assert.equal(status['ghcn-stations'],'ok');
 assert.equal(result.datasets.find(e=>e.id==='ghcn-stations').rows,1);
 assert.equal(status['ghcn-daily'],DATASETS.get('ghcn-daily').indexes.length?'DATASET_NOT_READY':'ok');
 assert.equal(result.stormEvents,0);
 const line=summarize(result,1);
 assert.equal(line.event,'warmed');
 assert.equal(line.pass,1);
 assert.equal(line.questions,2+DATASETS.size,'two questions and one freshness entry per dataset');
 assert.ok(line.slowest.length<=5&&line.slowest.every(s=>typeof s.ms==='number'));
 assert.ok(Array.isArray(line.failed));
 assert.ok(!JSON.stringify(line).includes('WICHITA'),'the journal line carries timings, never answers');
});

test('a database that cannot be opened is DATABASE_UNAVAILABLE for its datasets only',()=>{
 const open=path=>{if(path==='bad')throw new Error('nope');return new DatabaseSync(':memory:');};
 const result=warm({databases:{observations:'bad',bulk:'ok'},open,questions:{'storm-events':{},'recovered-bulk':{collection:'bulk-census-decennial-geographies'}}});
 const status=Object.fromEntries(result.datasets.map(e=>[e.id,e.status]));
 assert.equal(status['storm-events'],'DATABASE_UNAVAILABLE');
 assert.notEqual(status['recovered-bulk'],'DATABASE_UNAVAILABLE');
});
