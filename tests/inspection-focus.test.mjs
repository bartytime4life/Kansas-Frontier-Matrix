import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';

const page=await readFile(new URL('../app/page.tsx',import.meta.url),'utf8');
const ast=ts.createSourceFile('page.tsx',page,ts.ScriptTarget.ES2022,true,ts.ScriptKind.TSX);
const effects=[];
function visit(node){
 if(ts.isCallExpression(node)&&node.expression.getText(ast)==='useEffect'){
  const callback=node.arguments[0]?.getText(ast);
  if(callback?.includes('assistantEvidenceReturnRef.current')&&callback.includes('rightPanelRef.current'))effects.push(callback);
 }
 ts.forEachChild(node,visit);
}
visit(ast);

function enter({rightOpen=true,isCompact=false,fromAssistant=true,hasSummary=true}={}){
 const body={},summary={},focus=[];
 const document={activeElement:body};
 const context={rightOpen,isCompact,assistantEvidenceReturnRef:{current:fromAssistant?{}:null},
  rightPanelRef:{current:{querySelector(selector){
   assert.equal(selector,'[data-selection-summary]');
   return hasSummary?{focus(options){focus.push(options);document.activeElement=summary;}}:null;
  }}},document};
 // Run the page's committed entry effects against the newly visible drawer.
 for(const effect of effects){
  const code=ts.transpileModule(`return (${effect})();`,{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText;
  new Function(...Object.keys(context),code)(...Object.values(context));
 }
 return {body,summary,document,focus};
}

test('desktop discovery hands keyboard focus to the selected record after the drawer mounts',()=>{
 const h=enter();
 assert.equal(h.document.activeElement,h.summary,'focus must leave the hidden search result and enter its evidence summary');
 assert.deepEqual(h.focus,[{preventScroll:true}]);
});

test('closed drawers, map hover and compact modal entry keep their existing focus owner',()=>{
 for(const state of [{rightOpen:false},{fromAssistant:false},{isCompact:true},{hasSummary:false}]){
  const h=enter(state);
  assert.equal(h.document.activeElement,h.body);
  assert.deepEqual(h.focus,[]);
 }
});
