import test from 'node:test';
import assert from 'node:assert/strict';
import {recoveredObservations} from '../scripts/local-data/recovered.mjs';
import {nearObservations} from '../scripts/local-data/near.mjs';
import {modelUrl} from '../scripts/lib/typescript-model.mjs';
import {c,fixture} from './recovered-fixtures.mjs';
const ui=await import(await modelUrl('app/recovered-collections.ts'));
const data=await import(await modelUrl('app/archive-layer-data.ts'));
const layers=await import(await modelUrl('app/archive-layer-catalog.ts'));
test('map options use stored geometries, retain record identities and reject missing or invalid points',t=>{
 const db=fixture(t),a=recoveredObservations.run(db,recoveredObservations.parse({collection:c.id}));
 const layer=layers.archiveLayer(ui.recoveredMapId(c.id));assert.ok(layer);
 const result=data.archiveFeatures(layer,[...a.rows,{id:'bad',values:{geometry_geojson:'not-json'}}]);
 assert.equal(result.collection.features.length,3);assert.equal(result.unlocated,1);
 assert.equal(layer.dataset,'near-observations');
 const query=data.archiveQuery(layer,'-99,37,-97,39','', '');
 assert.deepEqual(query,{collection:c.id,bbox:'-99,37,-97,39',limit:'50'});
 const parsed=nearObservations.parse(query);
 assert.deepEqual(parsed.bbox,{west:-99,south:37,east:-97,north:39});assert.equal(parsed.limit,50);
 assert.throws(()=>nearObservations.parse(data.archiveQuery(layer,'','', '')),'map reads require an explicit area');
 assert.equal(new URL(ui.recoveredMapUrl([c.id,'observations-storm-event-fatalities']),'https://example.org').searchParams.get('archive'),ui.recoveredMapId(c.id));
});
test('client accepts truthful unknown totals only with a validated collection and pagination contract',async()=>{
 const body={format:'kfm-local-data-v1',dataset:'recovered-observations',collection:c.id,total:null,count:1,rows:[{id:'[1,1]',values:{}}],hasMore:true,nextCursor:'[1,1]',source:{provider:'Fixture'}};
 const get=b=>data.fetchArchive(body.dataset,{collection:c.id},new AbortController().signal,async()=>Response.json(b));
 assert.equal((await get(body)).total,null);
 for(const patch of [{collection:'wrong'},{total:10},{nextCursor:null},{hasMore:'true'}])await assert.rejects(get({...body,...patch}));
});
