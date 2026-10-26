import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import vm from 'node:vm';
import ts from 'typescript';

// Views panel cards: "Open on map" applies the view's profile stack, then any source only that view adds.
const compiled=ts.transpileModule(await readFile('app/living-atlas.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText;
const mod={exports:{}};vm.runInNewContext(compiled,{module:mod,exports:mod.exports,require:dep=>{throw new Error(`unexpected import ${dep}`);},Object});
const {LIVING_ATLAS_VIEWS}=mod.exports;
const union=(await readFile('app/live-context.ts','utf8')).match(/export type OfficialContextId = ([^;]+);/)[1];
const officialIds=[...union.matchAll(/"([^"]+)"/g)].map(m=>m[1]);

const baseline=ts.transpileModule(await readFile('app/daily-baseline.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText;
const baselineModule={exports:{}};vm.runInNewContext(baseline,{module:baselineModule,exports:baselineModule.exports,Date});
const {BASELINE_STACKS}=baselineModule.exports;

test('views open on their own sources, and counties come with a view only where they are the subject',()=>{
 for(const [profile,stack] of Object.entries(BASELINE_STACKS))for(const source of stack)assert.ok(officialIds.includes(source),`${profile}: ${source} is an official context id`);
 assert.deepEqual([...BASELINE_STACKS.overview],[],'the overview is the Explorer\'s uncluttered start: no counties, water or fire');
 for(const [profile,stack] of Object.entries(BASELINE_STACKS))if(profile!=='people-movement')assert.ok(!stack.includes('census-counties'),`${profile}: counties are not a backdrop for every view`);
 const view=id=>LIVING_ATLAS_VIEWS.find(candidate=>candidate.id===id);
 assert.match(view('kansas-overview').sourcePosture,/base map only/i);assert.deepEqual([...view('kansas-overview').sources],[]);
 assert.equal(view('county-atlas').profileId,'overview');
 assert.deepEqual([...view('county-atlas').sources],['census-counties'],'County Atlas asks the visitor to click a county, so it adds them');
 // Every other card's named sources come from its profile's stack.
 assert.deepEqual([...BASELINE_STACKS.elevation],['usgs-3dep-hillshade']);
 assert.deepEqual([...BASELINE_STACKS.smoke],['noaa-hms-smoke','nws-radar']);
 assert.deepEqual([...BASELINE_STACKS.water],['usgs-streamflow','usgs-3dhp-hydrography','usgs-wbd-watersheds','noaa-nwps-gauges']);
 for(const v of LIVING_ATLAS_VIEWS)for(const source of v.sources)assert.ok(officialIds.includes(source),`${v.id}: ${source}`);
});

test('opening a view applies its profile stack, then the sources only that view adds',async()=>{
 const page=await readFile('app/page.tsx','utf8');
 assert.match(page,/if \(baselineSources\) for \(const source of OFFICIAL_CONTEXT_SOURCES\) setOfficialContextVisible\(source\.id, baselineSources\.includes\(source\.id\)\);/);
 assert.match(page,/if \(profile\) applyViewProfile\(profile\);[\s\S]{0,200}for \(const sourceId of atlasView\.sources\) setOfficialContextVisible\(sourceId, true\);/);
 assert.doesNotMatch(await readFile('app/living-atlas.ts','utf8'),/Opens on all 105 real county boundaries/);
});
