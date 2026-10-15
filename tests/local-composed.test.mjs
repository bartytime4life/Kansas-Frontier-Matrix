import test from 'node:test';
import assert from 'node:assert/strict';
import {nativeApiPath,acceptedLocalRequest,apiOnlyEntry} from '../scripts/serve-local-composed.mjs';
test('composed entry preserves Node account operations and routes legacy data to the native boundary',()=>{
 for(const p of ['/api/pc-ai/status','/api/owner/sign-in','/api/ingestion/status','/','/assistant','/data/subsurface/manifest.json'])assert.equal(nativeApiPath(p),false,p);
 for(const p of ['/api/live-context','/api/earth-engine-context/active','/api/governed/v1/layers','/api/daily-archive','/api/land-records'])assert.equal(nativeApiPath(p),true,p);
});
test('local routing cannot inject owner identity or accept an alternate origin',()=>{
 const origin='http://127.0.0.1:4173';assert.equal(acceptedLocalRequest(new Request(origin+'/api/live-context'),origin),true);
 assert.equal(acceptedLocalRequest(new Request(origin+'/api/live-context',{headers:{'OAI-Authenticated-User':'owner'}}),origin),false);
 assert.equal(acceptedLocalRequest(new Request('http://evil.test/api/live-context'),origin),false);
});
test('the native backend is API-only and retains its pre-existing authority wrapper',()=>{
 const src='if (badAuthority) return new Response("Denied", {status:403}); return worker.fetch(request, env, ctx);';
 const output=apiOnlyEntry(src);assert.ok(output.startsWith('if (badAuthority)'));assert.match(output,/pathname\.startsWith\("\/api\/"\)/);assert.match(output,/status: 404/);assert.throws(()=>apiOnlyEntry('changed entry'),/NATIVE_ENTRY_DRIFT/);
});

test('current flowline detail uses the checked Node adapter without moving other hydrology APIs',()=>{
 assert.equal(nativeApiPath('/api/hydrology/flowlines'),false);
 for(const path of ['/api/hydrology/direction','/api/hydrology/flowlines/private','/api/hydrology','/api/live-context'])assert.equal(nativeApiPath(path),true);
});
