import test from 'node:test';
import assert from 'node:assert/strict';
import {DatabaseSync} from 'node:sqlite';
import {mkdtemp,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {newSecret,decodeSecret,signRequest,RESPONSE_SIGNATURE_HEADER} from '../scripts/home-inference/signature.mjs';
import {createGateway} from '../scripts/local-data/gateway.mjs';
import {SOURCES_INDEX} from '../scripts/local-data/freshness.mjs';
import {createLocalDataService,LOCAL_DATA_CACHE} from '../server/local-data.mjs';

const SITE='https://kansasfrontiermatrix.com',gatewaySecret=newSecret(),workerSecret=newSecret();
const config={origin:SITE,keyId:'data-gw-1',secret:decodeSecret(gatewaySecret),worker:{keyId:'data-worker-1',secret:decodeSecret(workerSecret)}};

async function fixture(t){
 const dir=await mkdtemp(join(tmpdir(),'kfm-catalog-'));t.after(()=>rm(dir,{recursive:true,force:true}));
 const path=join(dir,'observations.sqlite'),db=new DatabaseSync(path);
 db.exec(`CREATE TABLE kfm_storm_event_details(event_id TEXT, file_id INTEGER);
  CREATE TABLE kfm_sql_sources(file_id INTEGER PRIMARY KEY, source_id TEXT NOT NULL, source_path TEXT NOT NULL, sha256 TEXT NOT NULL UNIQUE, source_bytes INTEGER NOT NULL, source_url TEXT NOT NULL, receipt_json TEXT NOT NULL, imported_rows INTEGER NOT NULL DEFAULT 0, state TEXT NOT NULL);
  INSERT INTO kfm_sql_sources VALUES(14,'noaa-storm-events-details','e','s14',1,'u','{"retrieved_at":"2026-11-01T23:30:00Z","last_modified":"Mon, 26 Oct 2026 16:57:18 GMT"}',1,'complete');
  CREATE TABLE kfm_ahcb_changes(file_id INTEGER, row_number INTEGER, PRIMARY KEY(file_id,row_number)); INSERT INTO kfm_ahcb_changes VALUES(14,1);
  ${SOURCES_INDEX.sql};`);
 db.close();
 return path;
}

/** A relay that answers from an in-process gateway, as the PC's worker would, with the real signatures. */
function fakeRelay(handle,clock){
 let lastSeen=clock(),calls=0,down=false;
 return {
  get lastSeen(){return lastSeen;},set lastSeen(v){lastSeen=v;},get calls(){return calls;},set down(v){down=v;},
  handler:()=>new Response(null,{status:404}),
  submit:async({method,path,body=''})=>{
   calls++;if(down)throw Object.assign(new Error('LOCAL_DATA_UNAVAILABLE'),{code:'LOCAL_DATA_UNAVAILABLE'});
   const requestHeaders={...signRequest({keyId:'data-gw-1',secret:gatewaySecret,method,path,body,now:clock()}),...(body?{'content-type':'application/json'}:{})};
   const answer=handle({method,path,headers:requestHeaders,body});
   return {status:answer.status,bytes:answer.body,requestHeaders,headers:new Headers({'content-type':'application/json',[RESPONSE_SIGNATURE_HEADER]:answer.signature})};
  },
 };
}

test('the catalog carries readiness and freshness from one cached health trip, and stays useful when the PC is away',async t=>{
 let now=1_700_000_000_000;const clock=()=>now;
 const handle=createGateway({keyId:'data-gw-1',secret:gatewaySecret,dbPath:await fixture(t),clock});
 const relay=fakeRelay(handle,clock),service=createLocalDataService({config,relay,clock});
 const get=async()=>{const r=await service.catalog(new Request(SITE+'/api/local-data'));return {status:r.status,body:await r.json(),cache:r.headers.get('cache-control')};};

 let {status,body,cache}=await get();
 assert.equal(status,200);assert.equal(cache,'public, max-age=60');assert.equal(body.online,true);
 assert.equal(relay.calls,1,'one health trip');
 const storm=body.datasets.find(d=>d.id==='storm-events');
 assert.equal(storm.ready,true);
 assert.deepEqual(storm.freshness,{file:14,sourceId:'noaa-storm-events-details',retrievedAt:'2026-11-01T23:30:00.000Z',modifiedAt:'2026-10-26T16:57:18.000Z',basis:'sources'});
 assert.deepEqual(body.datasets.find(d=>d.id==='tiger-features').freshness,{reason:'UNAVAILABLE'});
 assert.equal(body.status.state,'live');
 assert.deepEqual(body.status.collections['observations-ahcb-changes'],{file:14,sourceId:'noaa-storm-events-details',retrievedAt:'2026-11-01T23:30:00.000Z',modifiedAt:'2026-10-26T16:57:18.000Z'});
 assert.equal('observations-ahcb-chronology' in body.status.collections,false,'a collection without a loaded file is left out');
 assert.ok(!('gateway' in body.status));

 // Within freshMs the cached health answers; no second trip.
 now+=60_000;({body}=await get());
 assert.equal(relay.calls,1);assert.equal(body.status.state,'fresh');

 // The PC goes away: the cached health is served stale, marked, and the catalog is still complete.
 now+=LOCAL_DATA_CACHE.freshMs;relay.down=true;relay.lastSeen=now-LOCAL_DATA_CACHE.workerSeenMs-1;
 ({body}=await get());
 assert.equal(body.online,false);assert.equal(body.status.state,'stale');assert.equal(body.datasets.length,22);
 assert.equal(body.datasets.find(d=>d.id==='storm-events').freshness.file,14);

 // Beyond staleMs nothing is left to serve: the catalog without status, as before.
 now+=LOCAL_DATA_CACHE.staleMs;
 ({body}=await get());
 assert.equal('status' in body,false);
 assert.equal('freshness' in body.datasets.find(d=>d.id==='storm-events'),false);
 assert.equal((await service.catalog(new Request(SITE+'/api/local-data',{method:'POST'}))).status,405);
});

test('a catalog asked while the PC has never answered has no status and takes no trip',async t=>{
 let now=1_700_000_000_000;const clock=()=>now;
 const handle=createGateway({keyId:'data-gw-1',secret:gatewaySecret,dbPath:await fixture(t),clock});
 const relay=fakeRelay(handle,clock);relay.lastSeen=0;
 const service=createLocalDataService({config,relay,clock});
 const body=await (await service.catalog(new Request(SITE+'/api/local-data'))).json();
 assert.equal(body.online,false);assert.equal('status' in body,false);assert.equal(relay.calls,0);
 assert.equal(body.datasets.length,22);
});
