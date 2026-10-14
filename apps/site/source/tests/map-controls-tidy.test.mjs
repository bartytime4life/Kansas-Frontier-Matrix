import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
const text=await readFile('app/page.tsx','utf8');
const ast=ts.createSourceFile('page.tsx',text,ts.ScriptTarget.ES2022,true,ts.ScriptKind.TSX);
const callbacks=new Map();let undergroundAction;
function scan(node){
 if(ts.isVariableDeclaration(node)&&node.initializer&&ts.isArrowFunction(node.initializer)) callbacks.set(node.name.getText(ast),node.initializer.getText(ast));
 if(ts.isJsxOpeningElement(node)&&node.tagName.getText(ast)==='button'){
  const attrs=node.attributes.properties;
  if(attrs.some(a=>a.name?.getText(ast)==='aria-label'&&a.initializer?.text==='Underground recorded layers')) undergroundAction=attrs.find(a=>a.name?.getText(ast)==='onClick').initializer.expression.getText(ast);
 }
 ts.forEachChild(node,scan);
}scan(ast);
function run(code,scope){assert.ok(code);const js=ts.transpileModule('return '+code+';',{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText;return new Function(...Object.keys(scope),js)(...Object.values(scope));}
test('Appearance enters the existing Underground transition with public-location privacy and dedicated focus preserved',()=>{
 for(const privateLocation of [false,true]){
  const changes=[],state={open:false,request:0,private:false,utility:true};
  const scope={primaryWorkspace:'map',undergroundOpen:false,locationCameraRedacted:privateLocation,locationDerivedViewRef:{current:false},
   activateMapRepresentation:value=>changes.push(value),setUndergroundOpen:value=>state.open=value,setPlaying:value=>changes.push(['playing',value]),
   setSubsurfacePrivate:fn=>state.private=fn(state.private),setTimelineOpen:()=>{},setLeftOpen:()=>{},setRightOpen:()=>{},setMapUtilityOpen:value=>state.utility=value};
  const toggle=run(callbacks.get('toggleUnderground'),scope);
  run(undergroundAction,{toggleUnderground:toggle,setUndergroundFocusRequest:fn=>state.request=fn(state.request)})();
  assert.equal(state.open,true);assert.equal(state.utility,false);assert.equal(state.request,1);assert.equal(state.private,privateLocation);
  assert.equal(changes[0],'2d');assert.deepEqual(changes[1],['playing',false]);
 }
});
test('phone measurement choices reveal and focus the live map; desktop keeps the pane',()=>{
 for(const isCompact of [false,true])for(const mode of ['point','distance','area']){
  const calls=[],frames=[];
  const action=run(callbacks.get('beginMapMeasurement'),{isCompact,toggleMeasure:value=>calls.push(['measure',value]),dismissMapUtilityWithoutFocus:()=>calls.push(['dismiss']),window:{requestAnimationFrame:fn=>frames.push(fn)},mapContainerRef:{current:{focus:options=>calls.push(['focus',options])}}});
  action(mode);assert.deepEqual(calls[0],['measure',mode]);assert.equal(frames.length,isCompact?1:0);
  if(isCompact){assert.deepEqual(calls[1],['dismiss']);frames[0]();assert.deepEqual(calls[2],['focus',{preventScroll:true}]);}else assert.equal(calls.length,1);
 }
});
