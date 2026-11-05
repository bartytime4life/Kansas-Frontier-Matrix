import test from 'node:test';
import assert from 'node:assert/strict';
import {DatabaseSync} from 'node:sqlite';
import {mkdtemp,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {newSecret,signRequest} from '../scripts/home-inference/signature.mjs';
import {iso,fileLed,tableFreshness,sourcesFreshness,feedFreshness,geopackageFreshness,collectionsFreshness,datasetFreshness,SOURCES_INDEX} from '../scripts/local-data/freshness.mjs';
import {plannedIndexes} from '../scripts/local-data/indexes.mjs';
import {createGateway} from '../scripts/local-data/gateway.mjs';
import {DATASETS} from '../scripts/local-data/datasets.mjs';

const receipt=value=>JSON.stringify(value);
function bookkeeping(db,{index=true}={}){
 db.exec(`CREATE TABLE kfm_sql_sources(file_id INTEGER PRIMARY KEY, source_id TEXT NOT NULL, source_path TEXT NOT NULL, sha256 TEXT NOT NULL UNIQUE, source_bytes INTEGER NOT NULL, source_url TEXT NOT NULL, receipt_json TEXT NOT NULL, imported_rows INTEGER NOT NULL DEFAULT 0, state TEXT NOT NULL);
  CREATE TABLE kfm_feed_state(feed TEXT PRIMARY KEY, state_json TEXT NOT NULL, updated_at TEXT NOT NULL) WITHOUT ROWID;
  INSERT INTO kfm_feed_state VALUES('prism','{}','2026-11-04T06:00:00Z');`);
 const add=db.prepare('INSERT INTO kfm_sql_sources VALUES(?,?,?,?,?,?,?,?,?)');
 add.run(10,'noaa-ghcnd','a','s10',1,'u',receipt({retrieved_at:'2026-11-01T23:08:00Z',last_modified:'Thu, 29 Oct 2026 12:00:00 GMT'}),1,'complete');
 add.run(11,'noaa-ghcnd-diff','b','s11',1,'u',receipt({retrieved_at:'2026-11-05T18:03:00Z',last_modified:'Thu, 05 Nov 2026 04:01:12 GMT'}),1,'complete');
 add.run(12,'noaa-ghcndex-TXx','c','s12',1,'u',receipt({kansas_station_files:[]}),1,'complete');
 add.run(13,'nws-alerts','d','s13',1,'u',receipt({captureBucketAt:'2026-11-03T13:00:00.000Z',lastModified:'not a date'}),1,'complete');
 add.run(14,'noaa-storm-events-details','e','s14',1,'u',receipt({retrieved_at:'2026-11-01T23:30:00Z',last_modified:'Mon, 26 Oct 2026 16:57:18 GMT'}),1,'complete');
 if(index)db.exec(SOURCES_INDEX.sql);
}

test('dates from receipts are normalised to ISO instants or null',()=>{
 assert.equal(iso('Thu, 29 Oct 2026 12:00:00 GMT'),'2026-10-29T12:00:00.000Z');
 assert.equal(iso('2026-11-05T18:03:00Z'),'2026-11-05T18:03:00.000Z');
 for(const bad of [null,undefined,'','not a date',{}])assert.equal(iso(bad),null);
});

test('a table is file-led when file_id leads its primary key or an index; its newest file carries the receipt dates',()=>{
 const db=new DatabaseSync(':memory:');bookkeeping(db);
 db.exec(`CREATE TABLE led(file_id INTEGER, row_number INTEGER, v TEXT, PRIMARY KEY(file_id,row_number));
  CREATE TABLE indexed(id TEXT PRIMARY KEY, file_id INTEGER); CREATE INDEX indexed_file ON indexed(file_id, id);
  CREATE TABLE plain(id TEXT PRIMARY KEY, file_id INTEGER);
  CREATE TABLE nofile(id TEXT PRIMARY KEY);
  INSERT INTO led VALUES(10,1,'x'),(11,1,'y'); INSERT INTO indexed VALUES('a',13); INSERT INTO plain VALUES('a',14);`);
 const cache=new Map();
 assert.equal(fileLed(db,'led',cache),true);assert.equal(fileLed(db,'indexed',cache),true);
 assert.equal(fileLed(db,'plain',cache),false);assert.equal(fileLed(db,'nofile',cache),false);assert.equal(fileLed(db,'absent',cache),false);
 assert.deepEqual(tableFreshness(db,'led',{cache}),{file:11,sourceId:'noaa-ghcnd-diff',retrievedAt:'2026-11-05T18:03:00.000Z',modifiedAt:'2026-11-05T04:01:12.000Z'});
 assert.deepEqual(tableFreshness(db,'indexed',{cache}),{file:13,sourceId:'nws-alerts',retrievedAt:'2026-11-03T13:00:00.000Z',modifiedAt:null});
 // A table that is not file-led is never scanned for MAX(file_id).
 assert.equal(tableFreshness(db,'plain',{cache}),null);
 assert.equal(tableFreshness(db,'absent',{cache}),null);
 db.exec('CREATE TABLE empty(file_id INTEGER PRIMARY KEY)');
 assert.equal(tableFreshness(db,'empty',{cache}),null);
 // A file the sources table no longer describes still names its file.
 db.exec('CREATE TABLE orphan(file_id INTEGER PRIMARY KEY); INSERT INTO orphan VALUES(99)');
 assert.deepEqual(tableFreshness(db,'orphan',{cache}),{file:99,sourceId:null,retrievedAt:null,modifiedAt:null});
 assert.deepEqual(collectionsFreshness(db,[{id:'c-led',table:'led'},{id:'c-plain',table:'plain'},{id:'c-absent',table:'absent'}],{cache}),{'c-led':tableFreshness(db,'led',{cache})});
});

test('source families answer only through their index and respect the family boundary',()=>{
 const without=new DatabaseSync(':memory:');bookkeeping(without,{index:false});
 assert.deepEqual(sourcesFreshness(without,['noaa-ghcnd']),{reason:'INDEX_MISSING'});
 const db=new DatabaseSync(':memory:');bookkeeping(db);
 // noaa-ghcnd covers noaa-ghcnd and noaa-ghcnd-diff, not noaa-ghcndex-TXx.
 assert.deepEqual(sourcesFreshness(db,['noaa-ghcnd']),{file:11,sourceId:'noaa-ghcnd-diff',retrievedAt:'2026-11-05T18:03:00.000Z',modifiedAt:'2026-11-05T04:01:12.000Z'});
 assert.equal(sourcesFreshness(db,['noaa-ghcndex']).file,12);
 assert.deepEqual(sourcesFreshness(db,['noaa-ghcndex']),{file:12,sourceId:'noaa-ghcndex-TXx',retrievedAt:null,modifiedAt:null});
 assert.equal(sourcesFreshness(db,['nws-alerts','noaa-storm-events']).file,14,'the newest file across families');
 assert.deepEqual(sourcesFreshness(db,['nothing-here']),{reason:'NO_FILES'});
 assert.deepEqual(feedFreshness(db,'prism'),{file:null,sourceId:'prism',retrievedAt:'2026-11-04T06:00:00.000Z',modifiedAt:null});
 assert.deepEqual(feedFreshness(db,'absent'),{reason:'NO_FEED_STATE'});
 assert.deepEqual(feedFreshness(without,'prism').retrievedAt,'2026-11-04T06:00:00.000Z');
 const gpkg=new DatabaseSync(':memory:');
 assert.deepEqual(geopackageFreshness(gpkg),{reason:'NO_GEOPACKAGE'});
 gpkg.exec("CREATE TABLE gpkg_contents(table_name TEXT, last_change TEXT); INSERT INTO gpkg_contents VALUES('a','2026-11-01T18:46:10.604Z'),('b','2026-10-01T00:00:00Z')");
 assert.deepEqual(geopackageFreshness(gpkg),{file:null,sourceId:null,retrievedAt:null,modifiedAt:'2026-11-01T18:46:10.604Z'});
});

test('every published dataset declares a freshness basis and answers one, never throwing',()=>{
 const db=new DatabaseSync(':memory:');bookkeeping(db);
 db.exec('CREATE TABLE kfm_newspaper_pages(page_rowid INTEGER PRIMARY KEY, file_id INTEGER); CREATE INDEX kfm_newspaper_pages_file ON kfm_newspaper_pages(file_id); INSERT INTO kfm_newspaper_pages VALUES(1,14)');
 const kinds=new Set();
 for(const d of DATASETS.values()){
  assert.ok(d.freshness,d.id+' declares freshness');
  const answer=datasetFreshness(db,d,{cache:new Map()});
  assert.ok(typeof answer.basis==='string',d.id+' names its basis');
  assert.ok('reason' in answer||'retrievedAt' in answer,d.id);
  kinds.add(answer.basis);
 }
 assert.deepEqual([...kinds].sort(),['collections','feed','geopackage','sources','tables']);
 assert.deepEqual(datasetFreshness(db,{id:'x',freshness:{sources:['noaa-ghcnd']}}),{file:11,sourceId:'noaa-ghcnd-diff',retrievedAt:'2026-11-05T18:03:00.000Z',modifiedAt:'2026-11-05T04:01:12.000Z',basis:'sources'});
 assert.deepEqual(datasetFreshness(db,{id:'x',freshness:{tables:['kfm_newspaper_pages','absent']}}),{file:14,sourceId:'noaa-storm-events-details',retrievedAt:'2026-11-01T23:30:00.000Z',modifiedAt:'2026-10-26T16:57:18.000Z',basis:'tables'});
 assert.deepEqual(datasetFreshness(db,{id:'x',freshness:{collections:[{id:'c',table:'absent'}]}}),{reason:'NO_FILES',basis:'collections'});
 assert.deepEqual(datasetFreshness(db,{id:'x'}),{reason:'NOT_DECLARED'});
 const archive=DATASETS.get('archive-search');
 assert.equal(datasetFreshness(db,archive,{cache:new Map()}).file,14);
});

test('the sources index is planned for the pipeline but never required to answer a question',()=>{
 const planned=plannedIndexes();
 for(const database of ['observations','bulk']){
  const index=planned.get(database).get(SOURCES_INDEX.name);
  assert.ok(index,database+' plans the sources index');
  assert.deepEqual(index.datasets,['freshness']);
 }
 for(const d of DATASETS.values())assert.ok(!d.indexes.some(i=>i.name===SOURCES_INDEX.name));
});

test('health reports freshness per dataset and per recovered collection',async t=>{
 const dir=await mkdtemp(join(tmpdir(),'kfm-freshness-'));t.after(()=>rm(dir,{recursive:true,force:true}));
 const path=join(dir,'bulk.sqlite'),db=new DatabaseSync(path);bookkeeping(db);
 db.exec('CREATE TABLE kfm_newspaper_pages(page_rowid INTEGER PRIMARY KEY, file_id INTEGER); CREATE INDEX kfm_newspaper_pages_file ON kfm_newspaper_pages(file_id); INSERT INTO kfm_newspaper_pages VALUES(1,11)');
 db.exec('CREATE TABLE kfm_ia_texts(text_rowid INTEGER PRIMARY KEY, file_id INTEGER); CREATE INDEX kfm_ia_texts_file ON kfm_ia_texts(file_id); INSERT INTO kfm_ia_texts VALUES(1,10)');
 db.close();
 const secret=newSecret(),handle=createGateway({keyId:'k',secret,databases:{bulk:path}});
 const path_='/v1/health',headers=signRequest({keyId:'k',secret,method:'GET',path:path_,body:''});
 const answer=handle({method:'GET',path:path_,headers,body:''}),body=JSON.parse(answer.body.toString('utf8'));
 assert.equal(answer.status,503,'no observations database: not ok, but still reported');
 const search=body.datasets.find(d=>d.id==='archive-search');
 assert.deepEqual(search,{id:'archive-search',ready:true,freshness:{file:11,sourceId:'noaa-ghcnd-diff',retrievedAt:'2026-11-05T18:03:00.000Z',modifiedAt:'2026-11-05T04:01:12.000Z',basis:'tables'}});
 assert.deepEqual(body.collections['bulk-newspaper-pages'],{file:11,sourceId:'noaa-ghcnd-diff',retrievedAt:'2026-11-05T18:03:00.000Z',modifiedAt:'2026-11-05T04:01:12.000Z'});
 assert.equal('bulk-ia-texts' in body.collections,false,'only catalog collections are reported; the texts table is reached through archive-search');
 assert.equal('bulk-census-decennial-geographies' in body.collections,false,'an absent collection table is left out, not an error');
 assert.deepEqual(Object.keys(body.collections),['bulk-newspaper-pages']);
 assert.equal(body.datasets.find(d=>d.id==='storm-events').freshness.reason,'UNAVAILABLE');
});
