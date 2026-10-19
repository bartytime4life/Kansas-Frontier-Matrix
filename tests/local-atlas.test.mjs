import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
const url = value => `data:text/javascript;base64,${Buffer.from(value).toString('base64')}`;
const compile = async path => ts.transpileModule(await readFile(path, 'utf8'), {compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const bounded = url(await compile('app/bounded-json.ts'));
const intake = url((await compile('app/intake-desk-client.ts')).replace('"./bounded-json"', JSON.stringify(bounded)));
const client = await import(url((await compile('app/local-atlas-client.ts')).replace('"./bounded-json"', JSON.stringify(bounded)).replace('"./intake-desk-client"', JSON.stringify(intake))));
const renderer = await import(url(await compile('app/local-atlas-map.ts')));
const feature = (value, name='A') => ({type:'Feature',properties:{name,value},geometry:{type:'Polygon',coordinates:[[[-100,38],[-99,38],[-99,39],[-100,38]]]}});
const preview = (patch={}) => ({schema:'kfm-local-atlas-preview/v1',id:'fixture',kind:'vector',title:'Synthetic fixture',source:{role:'test only',attribution:'fixture',sourceUrl:null,sha256:null},time:{kind:'test',label:'test',start:null,end:null,processedAt:null},units:'mm',bounds:[-100,38,-99,39],limitations:[],displayedCount:3,totalCount:3,truncated:false,authority:{admission:false,evidence:false,release:false},numericFields:['value'],valueField:'value',data:{type:'FeatureCollection',features:[feature(-2),feature(4,'B'),feature(null,'C')]},...patch});
test('preview validation preserves source semantics and rejects malformed or authoritative payloads', () => {
 const p=client.parseAtlasPreview(preview());assert.equal(p.units,'mm');assert.equal(p.data.features[2].properties.value,null);
 for(const patch of [{schema:'other'},{bounds:[-200,0,0,10]},{displayedCount:1},{authority:{admission:true,evidence:false,release:false}},{time:{label:'bad'}},{data:{type:'FeatureCollection',features:[{...feature(3),geometry:{type:'Point',coordinates:[0,NaN]}}]}}]) assert.equal(client.parseAtlasPreview(preview(patch)),null);
 assert.equal(client.atlasCollection({type:'FeatureCollection',features:Array(5001).fill(feature(1))}),false);
});
test('raster previews allow only bounded embedded PNGs and retain original categorical palettes', () => {
 const raster = {imageDataUrl:'data:image/png;base64,aGVsbG8=',coordinates:[[-100,39],[-99,39],[-99,38],[-100,38]],width:32,height:32,min:1,max:5,band:1,nodata:null,paletteType:'categorical',colorMap:[{value:1,color:'#abcdef'}],colors:['#dcf6ef','#115582']};
 const p=client.parseAtlasPreview(preview({kind:'raster',data:raster}));assert.deepEqual(p.data.colorMap,raster.colorMap);
 for(const patch of [{imageDataUrl:'https://evil.test/tile.png'},{width:100000},{paletteType:'random'},{colorMap:[{value:1,color:'url(x)'}]}]) assert.equal(client.parseAtlasPreview(preview({kind:'raster',data:{...raster,...patch}})),null);
});
test('difference scales are symmetric and keep missing counties separate from zero', () => {
 const scale=renderer.atlasScale(preview(),'value',true);assert.deepEqual(scale,{min:-4,max:4,count:2,difference:true});
 const color=renderer.atlasColor('value',scale);assert.equal(color.at(-1),renderer.ATLAS_COLORS.missing);assert.equal(color[2][5],0);
 assert.equal(renderer.atlasScale(preview({data:{type:'FeatureCollection',features:[feature(null)]}}),'value'),null);
 const constant=renderer.atlasColor('value',{min:3,max:3,count:1,difference:false});assert.equal(constant[2],renderer.ATLAS_COLORS.mid);
});
test('clear and a newer selection reject late responses even if transport ignores abort', () => {
 const gate=new client.AtlasRequestGate(), old=gate.begin(), current=gate.begin();assert.equal(old.signal.aborted,true);assert.equal(old.current(),false);assert.equal(current.current(),true);
 gate.clear();assert.equal(current.current(),false);assert.equal(current.signal.aborted,true);
});
test('requests use fixed loopback origin, session header, omit credentials, and surface errors', async () => {
 const original=globalThis.fetch;let seen;
 globalThis.fetch=async (input,init)=>{seen={input,init};return new Response(JSON.stringify(preview()),{headers:{'content-type':'application/json'}})};
 try {
 const p=await client.atlasRequest('/api/atlas/preview',new AbortController().signal,client.parseAtlasPreview,{kind:'prism',id:'B',compareId:'A'},'session');assert.equal(p.id,'fixture');
 assert.equal(seen.input,'http://127.0.0.1:8771/api/atlas/preview');assert.deepEqual([seen.init.credentials,seen.init.cache,seen.init.redirect],['omit','no-store','error']);assert.equal(seen.init.headers['X-KFM-Session'],'session');assert.equal(JSON.parse(seen.init.body).compareId,'A');
 globalThis.fetch=async()=>new Response(JSON.stringify({error:'ATLAS_DIFFERENCE_INCOMPATIBLE'}),{status:400});await assert.rejects(client.atlasRequest('/api/atlas/preview',new AbortController().signal,client.parseAtlasPreview,{},'session'),/INCOMPATIBLE/);
 } finally{globalThis.fetch=original;}
});
function harness(){
 const sources=new Map(),layers=new Map(),listeners=new Map(),events=[];let state,inspected;
 const map={pitch:0,projection:'mercator',terrain:null,getPitch(){return this.pitch},getProjection(){return {type:this.projection}},getTerrain(){return this.terrain},getSource:n=>sources.get(n),getLayer:n=>layers.get(n),
 addSource:(id,s)=>{sources.set(id,s);events.push('source+')},addLayer:l=>layers.set(l.id,structuredClone(l)),removeLayer:id=>{events.push('layer-');layers.delete(id)},removeSource:id=>{assert.equal(layers.size,0);events.push('source-');sources.delete(id)},
 on:(type,fn)=>listeners.set(type,fn),off:(type,fn)=>{if(listeners.get(type)===fn)listeners.delete(type)},setLayoutProperty:(id,k,v)=>{(layers.get(id).layout??={})[k]=v},queryRenderedFeatures:()=>[{properties:{name:'clicked',value:4}}]};
 const start=(p=preview(),patch={})=>renderer.attachAtlasPreview(map,p,{field:'value',difference:true,density:false,opacity:.6,flatMap:true,...patch},p=>{inspected=p},s=>{state=s});
 return {map,sources,layers,listeners,events,start,state:()=>state,inspected:()=>inspected};
}
test('map overlays own inspection and remove listeners/layers before sources on disposal',()=>{
 const h=harness(),control=h.start();assert.equal(h.sources.size,1);assert.equal(h.state(),'visible');assert.equal(renderer.localAtlasHit(h.map,{x:0,y:0}),true);
 h.listeners.get('click')({point:{x:1,y:1}});assert.equal(h.inspected().name,'clicked');control.dispose();control.dispose();assert.equal(h.layers.size,0);assert.equal(h.sources.size,0);assert.equal(h.listeners.size,0);assert.equal(h.events.at(-1),'source-');
});
test('raster is withheld on globe, pitch, or terrain and resumes only on a flat Mercator map',()=>{
 const p=preview({kind:'raster',data:{imageDataUrl:'data:image/png;base64,aGVsbG8=',coordinates:[[-100,39],[-99,39],[-99,38],[-100,38]]}}),h=harness();h.map.projection='globe';const c=h.start(p);assert.equal(h.state(),'flat-map-required');
 assert.equal(h.layers.get('kfm-local-atlas-raster').paint['raster-resampling'],'nearest');h.map.projection='mercator';h.map.pitch=25;h.listeners.get('move')();assert.equal(h.state(),'flat-map-required');h.map.pitch=0;h.listeners.get('move')();assert.equal(h.state(),'visible');c.dispose();
});
test('a failed owned source clears the partial display without marking other sources failed',()=>{
 const h=harness(),c=h.start();h.listeners.get('error')({sourceId:'unrelated'});assert.equal(h.state(),'visible');h.listeners.get('error')({sourceId:'kfm-local-atlas-source'});assert.equal(h.state(),'unavailable');assert.equal(h.sources.size,0);assert.equal(h.layers.size,0);c.dispose();assert.equal(h.listeners.size,0);
});
test('hosted map mounts source status without mounting or importing the local-PC atlas control', async () => {
 const page=await readFile('app/page.tsx','utf8');
 const ast=ts.createSourceFile('page.tsx',page,ts.ScriptTarget.ES2022,true,ts.ScriptKind.TSX);
 const imports=[],mounts=[];
 function visit(node,ancestors=[]){
  if(ts.isImportDeclaration(node))imports.push(node.moduleSpecifier.text);
  if(ts.isJsxSelfClosingElement(node))mounts.push({name:node.tagName.getText(ast),ancestors});
  ts.forEachChild(node,child=>visit(child,[...ancestors,node]));
 }
 visit(ast);
 assert.equal(imports.some(name=>name.startsWith('./local-atlas')),false);
 assert.equal(mounts.some(node=>node.name==='LocalAtlasControl'),false);
 const sourceStatus=mounts.filter(node=>node.name==='HostedSourceStatus');assert.equal(sourceStatus.length,1);
 assert.ok(sourceStatus[0].ancestors.some(node=>ts.isBinaryExpression(node)&&node.operatorToken.kind===ts.SyntaxKind.AmpersandAmpersandToken
  &&node.left.getText(ast)==='sourceStatusOpen && (leftPanelMode === "layers" || leftPanelMode === "live")'), 'hosted status is only mounted in its open Layers view');
});

test('legacy local Atlas bookmarks reveal hosted source status without opening a PC utility', async () => {
 const page=await readFile('app/page.tsx','utf8');
 const ast=ts.createSourceFile('page.tsx',page,ts.ScriptTarget.ES2022,true,ts.ScriptKind.TSX),declarations=new Map();let reveal;
 function visit(node){
  if(ts.isVariableDeclaration(node)&&node.initializer)declarations.set(node.name.getText(ast),node.initializer.getText(ast));
  if(ts.isIfStatement(node)&&node.expression.getText(ast)==='restoredSourceStatus')reveal=node.getText(ast);
  ts.forEachChild(node,visit);
 }
 visit(ast);assert.ok(reveal);
 const code=['restoredMapUtilityView','restoredSourceStatus','nextMapUtilityView','restoredMapUtilityOpen']
  .map(name=>{assert.ok(declarations.has(name));return `const ${name} = ${declarations.get(name)};`;}).join('\n');
 const javascript=ts.transpileModule(`${code}\n${reveal}\nreturn {view:nextMapUtilityView,open:restoredMapUtilityOpen};`,{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText;
 for(const query of ['maptab=localAtlas&mapui=open','maptab=localAtlas','layers=sources','layers=sources&maptab=compare&mapui=open'])for(const mode of ['snapshot','comparison']){
  const params=new URLSearchParams(query+'&ctx=census-counties&time=1909'),original=params.toString(),actions=[];
  const result=new Function('params','nextTemporalMode','setLeftPanelMode','setLeftOpen','setSourceStatusOpen',javascript)(params,mode,
   value=>actions.push(['mode',value]),value=>actions.push(['left',value]),value=>actions.push(['sources',value]));
  assert.deepEqual(actions,[['mode','layers'],['left',true],['sources',true]]);
  assert.equal(result.open,false);assert.notEqual(result.view,'localAtlas');assert.equal(params.toString(),original);
 }
});

test('hosted global click selection filters hidden official layers and yields to Underground before querying', async () => {
 const page=await readFile('app/page.tsx','utf8');
 const ast=ts.createSourceFile('page.tsx',page,ts.ScriptTarget.ES2022,true,ts.ScriptKind.TSX);let callback;
 function visit(node){
  if(ts.isCallExpression(node)&&node.expression.getText(ast)==='map.on'&&node.arguments[0]?.getText(ast)==='"click"')callback=node.arguments[1];
  ts.forEachChild(node,visit);
 }
 visit(ast);assert.ok(callback);
 const statements=[];
 for(const statement of callback.body.statements){
  if(ts.isVariableStatement(statement)&&statement.declarationList.declarations.some(node=>node.name.getText(ast)==='availableLayers'))break;
  statements.push(statement.getText(ast));
 }
 const javascript=ts.transpileModule(statements.join('\n')+'\nreturn renderedHits;',{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText;
 const hidden={source:'hidden-source',layer:{id:'hidden'}},visible={source:'visible-source',layer:{id:'visible'}},registry={source:'registry',layer:{id:'registry'}},proof={source:'synthetic-proof',layer:{id:'proof'}};
 let queries=0;
 const scope={map:{queryRenderedFeatures:()=>{queries++;return [hidden,visible,registry,proof];}},event:{point:{x:1,y:2}},undergroundOpenRef:{current:false},measureModeRef:{current:null},
  OFFICIAL_CONTEXT_BY_SOURCE_ID:{'hidden-source':{id:'hidden'},'visible-source':{id:'visible'}},officialOpacityRef:{current:{hidden:0,visible:.5}},
  findLayerByRenderer:id=>id==='registry'?{id:'registry',defaultOpacity:1}:null,opacityRef:{current:{registry:0}}};
 const handler=()=>new Function(...Object.keys(scope),javascript)(...Object.values(scope));
 assert.deepEqual(handler(),[visible,proof]);assert.equal(queries,1);
 scope.undergroundOpenRef.current=true;assert.equal(handler(),undefined);assert.equal(queries,1);
});
test('raster image bounds own only visible local clicks without claiming pixel values', () => {
 const h=harness(),p=preview({kind:'raster',data:{imageDataUrl:'data:image/png;base64,aGVsbG8=',coordinates:[[-100,39],[-99,39],[-99,38],[-100,38]]}}),c=h.start(p);
 h.map.queryRenderedFeatures=()=>[];h.map.getStyle=()=>({sources:Object.fromEntries(h.sources)});
 h.map.getLayoutProperty=(id,key)=>h.layers.get(id).layout[key];h.map.getPaintProperty=(id,key)=>h.layers.get(id).paint[key];
 h.map.unproject=()=>({lng:-99.5,lat:38.5});assert.equal(renderer.localAtlasHit(h.map,{x:0,y:0}),true);
 h.map.unproject=()=>({lng:-98,lat:38.5});assert.equal(renderer.localAtlasHit(h.map,{x:0,y:0}),false);
 h.map.unproject=()=>({lng:-99.5,lat:38.5});h.map.projection='globe';h.listeners.get('move')();assert.equal(renderer.localAtlasHit(h.map,{x:0,y:0}),false);
 h.map.projection='mercator';h.listeners.get('move')();h.layers.get('kfm-local-atlas-raster').paint['raster-opacity']=0;assert.equal(renderer.localAtlasHit(h.map,{x:0,y:0}),false);c.dispose();
});
test('an absent projection is not treated as proof of a flat Mercator raster view', () => {
 const h=harness(),p=preview({kind:'raster',data:{imageDataUrl:'data:image/png;base64,aGVsbG8=',coordinates:[[-100,39],[-99,39],[-99,38],[-100,38]]}});h.map.getProjection=()=>undefined;
 const c=h.start(p);assert.equal(h.state(),'flat-map-required');c.dispose();
});

test('expected preparation errors give actionable guidance without exposing backend codes', () => {
 const cases = [
  ['ATLAS_CSV_COORDINATES_REQUIRED', /latitude and longitude/],
  ['ATLAS_SPATIAL_RUNTIME_UNAVAILABLE', /spatial reader is unavailable/],
  ['ATLAS_GEOJSON_CRS_UNSUPPORTED', /WGS84/],
  ['ATLAS_FORMAT_NEEDS_SPATIAL_DERIVATIVE', /prepared spatial copy/],
  ['ATLAS_ARCHIVE_SELECT_SINGLE_RASTER', /exactly one supported GeoTIFF/],
  ['ATLAS_ARCHIVE_SELECT_SINGLE_VECTOR', /exactly one supported shapefile/],
  ['ATLAS_SOURCE_CHANGED_REANALYZE', /Run analysis in Intake Desk/],
  ['ATLAS_BAND_INVALID', /band 1/],
  ['ATLAS_PREVIEW_TIMEOUT', /took too long/],
  ['ATLAS_PREVIEW_BUSY', /Wait for it to finish/],
  ['ATLAS_RASTER_OUTSIDE_KANSAS', /does not overlap/],
  ['ATLAS_RESPONSE_LIMIT', /smaller spatial subset/],
  ['ATLAS_VERTEX_LIMIT', /simplified/],
  ['ATLAS_NO_DISPLAYABLE_FEATURES', /coordinate columns/],
  ['ATLAS_PRISM_NOT_AVAILABLE', /explore Local files/],
  ['ATLAS_DIFFERENCE_INCOMPATIBLE', /same climate collection/],
  ['ATLAS_ARCHIVE_MEMBER_LIMIT', /smaller single-layer/],
 ];
 for(const [code, guidance] of cases){const result=client.atlasErrorMessage(new Error(code));assert.match(result,guidance);assert.doesNotMatch(result,/ATLAS_/);}
 assert.match(client.atlasErrorMessage(new Error('ATLAS_FUTURE_CODE: secret technical detail')),/Review the source/);
 assert.doesNotMatch(client.atlasErrorMessage(new Error('ATLAS_FUTURE_CODE: secret technical detail')),/FUTURE|secret/);
 assert.match(client.atlasErrorMessage(new TypeError('Failed to fetch')),/Start it on this PC/);
 assert.match(client.atlasErrorMessage(new DOMException('deadline','TimeoutError')),/took too long/);
});

const presentation = await import(url(await compile('app/local-atlas-presentation.ts')));
test('climate labels explain source variables and the A/B meaning of each statistic', () => {
 const label=presentation.atlasCollectionLabel({variable:'ppt',period:'annual',resolution:'4km'});
 assert.equal(label,'Precipitation · annual · 4 km');
 assert.equal(presentation.atlasInspectorLabel('value',true,true),'Difference (B − A)');
 assert.equal(presentation.atlasInspectorLabel('minimum',true,true),'Period B minimum');
 assert.equal(presentation.atlasInspectorLabel('valid_pixels_A',true,true),'Period A valid grid cells');
 assert.equal(presentation.atlasInspectorLabel('valueA',true,true),'Period A value');
 assert.equal(presentation.atlasInspectorLabel('valueB',true,true),'Period B value');
 assert.equal(presentation.atlasInspectorLabel('mean',true,false),'County mean');
 assert.equal(presentation.atlasInspectorLabel('minimum',false,true),'minimum');
});
test('mobile fitting reserves only the displayed bottom sheet and keeps an exposed map rectangle', () => {
 assert.deepEqual(presentation.atlasMobilePadding(86,784,585),{top:32,left:24,right:24,bottom:215});
 const p=presentation.atlasMobilePadding(86,784,650);assert.ok(p.bottom<200);assert.ok(784-86-p.top-p.bottom>450);
 const tiny=presentation.atlasMobilePadding(0,160,0);assert.ok(tiny.bottom<=60);
});

test('a supplied vector hit stack avoids another query without losing local ownership',()=>{
 const h=harness(),c=h.start();h.map.queryRenderedFeatures=()=>{throw new Error('duplicate query');};
 const id=[...h.layers.keys()].find(id=>id.includes('point'));
 assert.equal(renderer.localAtlasHit(h.map,{x:0,y:0},[{layer:{id}}]),true);
 assert.equal(renderer.localAtlasHit(h.map,{x:0,y:0},[]),false);c.dispose();
});
