import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import vm from 'node:vm';
import ts from 'typescript';
import { componentHarness, findNode } from './component-harness.mjs';
const read = file => readFile(new URL('../'+file, import.meta.url),'utf8');
const compile = source => ts.transpileModule(source,{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText;
const starters={}; vm.runInNewContext(compile(await read('app/map-starters.ts')), {exports:starters});

test('the GitHub welcome keeps Staging release limits and routes Find without an AI request', async () => {
  let find=0,closed=0; const actions=[];
  const h=await componentHarness('app/explorer-guide.tsx',{'./map-starters':starters,'./public-profile':{IS_PUBLIC_COPY:true}});
  const tree=h.render(h.exports.ExplorerGuide,{open:true,onChoosePlace:()=>find++,onClose:()=>closed++,onAction:value=>actions.push(value)});
  const text=JSON.stringify(tree);
  assert.match(text,/Prairie Field Desk/);
  assert.match(text,/unapproved data withheld/);
  assert.match(text,/no map selection or draft is transferred/);
  assert.ok(findNode(tree,n=>n.type==='a'&&n.props.href==='/topics'));
  assert.equal(findNode(tree,n=>n.props?.className==='atlas-welcome-groups'),undefined,'no nonfunctional discussion prompt buttons');
  findNode(tree,n=>n.type==='button'&&n.props.children==='Find a place or layer').props.onClick();
  assert.equal(find,1);assert.equal(closed,1);assert.deepEqual(actions,[]);
  findNode(tree,n=>n.type==='button'&&n.props.children?.[0]?.props?.children==='Investigate change').props.onClick();
  assert.deepEqual(actions,['time']);
  h.dispose();
});

const page=ts.createSourceFile('page.tsx',await read('app/page.tsx'),ts.ScriptTarget.Latest,true,ts.ScriptKind.TSX);
const declarations=new Map();
function visit(n){if(ts.isVariableDeclaration(n)&&n.initializer)declarations.set(n.name.getText(page),n.initializer);ts.forEachChild(n,visit);}visit(page);
const evaluate=(node,scope)=>new Function(...Object.keys(scope),compile('return '+node.getText(page)))(...Object.values(scope));

test('the actual search memo suppresses stale rows while a new query settles',()=>{
  const memo=declarations.get('searchResults').arguments[0];
  const scope={SEARCH_INDEX:[{id:'a',title:'USGS rivers',subtitle:'source',kind:'feature'}],OFFICIAL_CONTEXT_SOURCES:[]};
  assert.equal(evaluate(memo,{...scope,globalQuery:'USGS',debouncedGlobalQuery:'USGS'})().length,1);
  assert.equal(evaluate(memo,{...scope,globalQuery:'NOAA',debouncedGlobalQuery:'USGS'})().length,0);
  assert.equal(evaluate(memo,{...scope,globalQuery:'',debouncedGlobalQuery:'USGS'})().length,0);
});

test('legacy and unavailable utility URL states resolve to current Appearance while comparison wins',()=>{
  const restored=declarations.get('nextMapUtilityView');
  for(const restoredMapUtilityView of ['navigate','unknown']) assert.equal(evaluate(restored,{restoredMapUtilityView,nextTemporalMode:'snapshot'}),'scene');
  assert.equal(evaluate(restored,{restoredMapUtilityView:'navigate',nextTemporalMode:'comparison'}),'compare');
});
