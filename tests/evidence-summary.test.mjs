import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';

const compile=async path=>ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const url=js=>`data:text/javascript;base64,${Buffer.from(js).toString('base64')}`;
const workspaces=url(await compile('app/layer-workspaces.ts'));
const summary=await import(url((await compile('app/evidence-summary.ts')).replace('from "./layer-workspaces"',`from "${workspaces}"`)));
const base={kind:'registry',officialId:null,layerDomain:'Hydrology',title:'Gauge',summary:'  A dated   station anchor. ',sourceOrganization:'USGS',spatialScope:'Kansas River at DeSoto',temporalScope:'2026-10-25',lastUpdate:'2026-10-24',evidenceState:'ANSWER',generalizationNote:'Display anchor.',uncertainty:'Location ±30 m.',focusLng:-94.96,focusLat:38.98};

test('every selection answers the same three questions from its own fields',()=>{
 const s=summary.evidenceSummary(base);
 assert.equal(s.what,'A dated station anchor.','whitespace is normalized, not reworded');
 assert.equal(s.where,'Kansas River at DeSoto · display anchor 38.980° N, 94.960° W');
 assert.equal(s.when,'2026-10-25 · source updated 2026-10-24');
 assert.equal(s.source,'USGS');assert.equal(s.status,'ANSWER');
 assert.equal(s.limits,'Display anchor. Location ±30 m.');
 assert.deepEqual([...s.topics],['water'],'registry membership uses the catalogue rule');
});

test('a live observation time leads, and missing fields are said plainly rather than invented',()=>{
 const observed=summary.evidenceSummary({...base,observedAt:'2026-10-25T18:00Z',lastUpdate:'2026-10-25T18:00Z'});
 assert.equal(observed.when,'2026-10-25T18:00Z','no duplicate update clause');
 const sparse=summary.evidenceSummary({...base,summary:'',spatialScope:'',temporalScope:'',lastUpdate:'',sourceOrganization:'',evidenceState:'',generalizationNote:'',uncertainty:'',focusLng:NaN,focusLat:NaN});
 assert.equal(sparse.what,'Gauge');assert.equal(sparse.where,'No location recorded');assert.equal(sparse.when,'No time recorded');
 assert.equal(sparse.source,'Source not recorded');assert.equal(sparse.status,'Evidence state not recorded');
 assert.match(sparse.limits,/does not mean there is none/);
});

test('provider basemap records stay external context and official sources keep their catalogue categories',()=>{
 const basemap=summary.evidenceSummary({...base,kind:'basemap',evidenceState:'ANSWER'});
 assert.equal(basemap.status,'External context only · no KFM EvidenceBundle','a basemap record never borrows an evidence state');
 assert.match(basemap.what,/provider/);assert.deepEqual([...basemap.topics],[]);
 assert.deepEqual([...summary.evidenceSummary({...base,officialId:'census-counties'}).topics].sort(),['government','history','people','places']);
 assert.equal(summary.selectionTopics('registry',null,'Roads and rail')[0],'transport');
});

test('the drawer renders the summary and offers the category map only when it is not already on',async()=>{
 const page=await readFile('app/page.tsx','utf8');
 assert.match(page,/const selectedSummary = useMemo\(\(\) => selected \? evidenceSummary\(\{ \.\.\.selected\.properties, kind: selected\.kind, officialId: selectedOfficialContextId,/);
 const drawer=page.slice(page.indexOf('<section className={researchStyles.summary} aria-label="Selection summary">'),page.indexOf('<div className={researchStyles.actions}>'));
 for(const label of ['What it is','Where &amp; when','Source &amp; limits'])assert.ok(drawer.includes(`<dt>${label}</dt>`),label);
 assert.match(drawer,/const lookOn = look && look\.basemap === basemap && officialWorkspace === primary;/);
 assert.match(drawer,/\{look && !lookOn && <button type="button" onClick=\{\(\) => openCategoryMap\(primary\)\}>Open the \{look\.name\.toLowerCase\(\)\}<\/button>\}/);
 assert.ok(drawer.indexOf('drawer-category')<drawer.indexOf('data-selection-summary'),'the category heads the record');
 assert.doesNotMatch(drawer,/evidenceState\s*=|ANSWER/,'the drawer never writes or upgrades an evidence state');
});
