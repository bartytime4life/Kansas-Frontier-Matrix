import test from 'node:test';
import assert from 'node:assert/strict';
import {readdir,readFile} from 'node:fs/promises';
import {join} from 'node:path';
import ts from 'typescript';

const retired=new Set(['/data','/stewards','/source-operations','/daily-archive','/governed/water-release','/governed/weather-release','/earth-engine-context/install']);
async function files(directory){
 const entries=await readdir(directory,{withFileTypes:true});
 return (await Promise.all(entries.map(item=>item.isDirectory()?files(join(directory,item.name)):[join(directory,item.name)]))).flat();
}
test('application navigation and topology do not advertise retired account destinations',async()=>{
 const sourceFiles=await files('app');
 for(const path of retired)assert.ok(!sourceFiles.includes('app'+path+'/page.tsx'),path);
 for(const path of sourceFiles.filter(path=>/\.(?:tsx?|mjs)$/.test(path))){
  const source=ts.createSourceFile(path,await readFile(path,'utf8'),ts.ScriptTarget.Latest,true,path.endsWith('.tsx')?ts.ScriptKind.TSX:ts.ScriptKind.TS);
  function visit(node){
   if(ts.isJsxAttribute(node)&&node.name.text==='href'&&node.initializer){
    const value=ts.isJsxExpression(node.initializer)?node.initializer.expression:node.initializer;
    const prefix=value&&(ts.isStringLiteral(value)||ts.isNoSubstitutionTemplateLiteral(value)?value.text:ts.isTemplateExpression(value)?value.head.text:null);
    if(prefix?.startsWith('/'))assert.ok(!retired.has(new URL(prefix,'https://app.test').pathname),`${path}: ${prefix}`);
   }
   ts.forEachChild(node,visit);
  }
  visit(source);
 }
});
