import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';

const load=async path=>{const exports={};new Function('exports',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports);return exports;};
const prisms=await load('app/population-prisms.ts');
const county=(population,landSquareMiles)=>({properties:{population,landSquareMiles}});

test('counties fall in the Kansas density peer groups by people per square mile of land, lower bounds inclusive',()=>{
 const group=d=>prisms.kansasDensityGroup(d).label;
 assert.deepEqual([0,5.99,6,19.99,20,39.99,40,149.99,150,1288].map(group),['Frontier','Frontier','Rural','Rural','Densely-settled rural','Densely-settled rural','Semi-urban','Semi-urban','Urban','Urban']);
 assert.equal(prisms.peoplePerSquareMile(609863,473.4).toFixed(0),'1288','a metro county: count over land area');
 assert.equal(prisms.peoplePerSquareMile(1284,778.4).toFixed(2),'1.65','a frontier county');
 for(const [p,l] of [[null,10],[10,0],[10,null],[-1,10],['10',10]])assert.equal(prisms.peoplePerSquareMile(p,l),null,'missing or invalid counts give no density');
});

test('the legend counts counties per group and the state density from the counts themselves, not an average of ratios',()=>{
 const summary=prisms.densityGroupCounts([county(609863,473.4),county(1284,778.4),county(3000,300),county(null,500),county(900,0)]);
 assert.equal(summary.counties,3,'counties without both counts are left out');
 assert.deepEqual(summary.groups.map(g=>[g.label,g.count]),[['Frontier',1],['Rural',1],['Densely-settled rural',0],['Semi-urban',0],['Urban',1]]);
 assert.equal(summary.statewide.toFixed(1),((609863+1284+3000)/(473.4+778.4+300)).toFixed(1));
});

test('each prism rises linearly with density and takes its group colour; the layer reads the county source',()=>{
 const layer=prisms.populationPrismLayer('external-census-counties');
 assert.equal(layer.type,'fill-extrusion');assert.equal(layer.source,'external-census-counties');assert.equal(layer.id,prisms.POPULATION_PRISM_LAYER_ID);
 assert.ok(layer.id.startsWith('external-'),'composed with the other provider overlays');
 assert.deepEqual(layer.paint['fill-extrusion-height'],['*',['/',['to-number',['get','population']],['to-number',['get','landSquareMiles']]],100],'100 m per person per square mile, no log or exaggeration');
 const color=layer.paint['fill-extrusion-color'];
 assert.equal(color[0],'step');assert.deepEqual(color.slice(3).filter((_,i)=>i%2===0),[6,20,40,150],'breaks are the peer-group bounds');
 assert.deepEqual([color[2],...color.slice(4).filter((_,i)=>i%2===0)],prisms.KANSAS_DENSITY_GROUPS.map(g=>g.color));
 assert.match(JSON.stringify(layer.filter),/landSquareMiles.*>.*0|>.*landSquareMiles/,'no division by a missing or zero land area');
});

test('the context renderer draws prisms only where a map asks, with counties on and off the globe, in place of the outline',async()=>{
 const live=await readFile('app/live-context.ts','utf8');
 assert.match(live,/const prisms = Boolean\(visibility\["census-counties"\]\) && populationPrismsOn\(map\) && !globeView;/);
 assert.match(live,/if \(prisms && map\.getLayer\(county\.layerIds\[1\]\)\) setVisibleIfChanged\(map, county\.layerIds\[1\], false\);/);
 assert.match(live,/interactiveLayerIds: Object\.freeze\(\["external-census-counties-fill", POPULATION_PRISM_LAYER_ID\]\)/,'a prism can be selected for its county record');
 const baseline=await readFile('app/county-baseline.ts','utf8');
 assert.match(baseline,/peoplePerSquareMile: density === null \? null : Math\.round\(density \* 10\) \/ 10, densityGroup: density === null \? null : kansasDensityGroup\(density\)\.label/,'the record carries the same density the prism is drawn from');
 const page=await readFile('app/page.tsx','utf8');
 assert.match(page,/setPopulationPrismsShown\(Boolean\(look\.overlays\?\.includes\("population"\)\)\);/,'on with the People map, off with any other');
});

test('the People dock toggles the prisms and shows the density groups with their county counts and the height scale',async()=>{
 const maps=await load('app/category-maps.ts');
 const people=maps.CATEGORY_MAPS.people;
 assert.deepEqual([...people.overlays],['population']);assert.deepEqual([...people.tools],['population']);assert.equal(people.scene,'terrain');
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];
 const summary=prisms.densityGroupCounts([county(609863,473.4),county(1284,778.4)]);
 const base={look:people,mode:'terrain',depth:2.5,azimuth:315,sun:null,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},onPopulation:v=>calls.push(v)};
 let tree=h.render(h.exports.CategoryMapDock,{...base,population:{on:true,...summary,metresPerPerson:100}});
 const text=JSON.stringify(tree);
 assert.match(text,/Frontier.*under 6.*1 county.*Rural.*0 counties.*Urban.*150 and over.*1 county/);
 assert.match(text,/Height: .*100.* m per person per sq mi of land.*Kansas overall .*2020 Census/);
 findNode(tree,n=>n.type==='button'&&n.props.children==='Flatten the counties').props.onClick();
 tree=h.render(h.exports.CategoryMapDock,{...base,population:{on:false,...summary,metresPerPerson:100}});
 assert.doesNotMatch(JSON.stringify(tree),/Frontier/,'no legend while flat');
 findNode(tree,n=>n.type==='button'&&n.props.children==='Show population in 3D').props.onClick();
 assert.deepEqual(calls,[false,true]);
 h.dispose?.();
});
