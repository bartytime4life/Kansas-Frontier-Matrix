import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { componentHarness, findNode, settle } from './component-harness.mjs';
const compile=async path=>`data:text/javascript;base64,${Buffer.from(ts.transpileModule(await readFile(new URL(path,import.meta.url),'utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64')}`;
const history=await import(await compile('../app/transport-history.ts'));
const sources=await import(await compile('../app/transport-history-sources.ts'));
const example=await readFile(new URL('../public/transport-construction-study-example.json',import.meta.url),'utf8');
const textOf=node=>typeof node==='string'||typeof node==='number'?String(node):!node||typeof node!=='object'?'':[node.props?.children].flat(Infinity).map(textOf).join(' ');
async function harness(reducedMotion=false, study=example){
 const timers=new Map();let timer=0;
 const h=await componentHarness(new URL('../app/transport-history-control.tsx',import.meta.url),{'./transport-history':history,'./transport-history-sources':sources},{window:{setInterval(fn){timers.set(++timer,fn);return timer;},clearInterval(id){timers.delete(id);}},document:{hidden:false}});
 const props={map:null,mapReady:false,date:'2024-01-06',reducedMotion,animate:true};
 const render=()=>h.render(h.exports.TransportHistoryControl,props);
 const button=(tree,name)=>findNode(tree,n=>n.type==='button'&&textOf(n)===name);
 const file=tree=>findNode(tree,n=>n.type==='input'&&n.props.type==='file');
 const load=async()=>{let tree=render();h.commit();await file(tree).props.onChange({target:{files:[{size:study.length,text:async()=>study}]}});await settle();tree=render();h.commit();return tree;};
 return {h,props,render,button,file,load,timers};
}
test('local load, source disclosure, day override and return to map time work without a renderer',async()=>{
 const a=await harness();let tree=await a.load();assert.match(textOf(tree),/SYNTHETIC/);assert.match(textOf(tree),/recorded closure/);assert.match(textOf(tree),/2024-01-06/);
 findNode(tree,n=>n.type==='input'&&n.props.type==='date').props.onChange({target:{value:'2024-01-11'}});tree=a.render();a.h.commit();assert.match(textOf(tree),/closure not established/);
 a.button(tree,'Follow map time').props.onClick();tree=a.render();a.h.commit();assert.match(textOf(tree),/recorded closure/);
 a.button(tree,'Clear study').props.onClick();tree=a.render();a.h.commit();assert.doesNotMatch(textOf(tree),/Format demonstration/);assert.equal(a.button(tree,'Play work history'),undefined);a.h.dispose();
});
test('oversized files are rejected before read and failed replacement retains the previous study',async()=>{
 const a=await harness();let tree=await a.load();let read=false;
 await a.file(tree).props.onChange({target:{files:[{size:2_000_001,text:async()=>{read=true;return '';}}]}});await settle();tree=a.render();a.h.commit();assert.equal(read,false);assert.match(textOf(tree),/2 MB/);assert.match(textOf(tree),/Format demonstration/);a.h.dispose();
});
test('clear fences a pending file read',async()=>{
 const a=await harness();let tree=await a.load();let resolve;
 const deferred=new Promise(r=>{resolve=r;});
 const pending=a.file(tree).props.onChange({target:{files:[{size:example.length,text:()=>deferred}]}});
 a.button(tree,'Clear study').props.onClick();resolve(example);await pending;await settle();tree=a.render();a.h.commit();assert.doesNotMatch(textOf(tree),/Format demonstration/);a.h.dispose();
});
test('reduced motion disables traversal; finite playback stops at last actual work date',async()=>{
 const reduced=await harness(true);let tree=await reduced.load();assert.equal(reduced.button(tree,'Play work history').props.disabled,true);assert.equal(reduced.timers.size,0);reduced.h.dispose();
 const a=await harness();tree=await a.load();a.button(tree,'Play work history').props.onClick();tree=a.render();a.h.commit();assert.equal(a.timers.size,1);
 for(let i=0;i<6;i++){for(const fn of [...a.timers.values()])fn();tree=a.render();a.h.commit();}
 assert.equal(a.timers.size,0);assert.equal(findNode(tree,n=>n.type==='input'&&n.props.type==='date').props.value,'2024-01-11');a.h.dispose();
});

test('milestone reports appear only as their report dates are reached and reverse seeking removes later reports',async()=>{
 const pilot=await readFile(new URL('../data/work/transport/junction-city-i70-2024.study.json',import.meta.url),'utf8');
 const a=await harness(false,pilot);a.props.date='2024-04-29';let tree=await a.load();
 assert.match(textOf(tree),/front, closure status and completion fraction unknown/);
 assert.match(textOf(tree),/construction progressing/);assert.doesNotMatch(textOf(tree),/Exact completion day is unknown/);
 const setDay=value=>{findNode(tree,n=>n.type==='input'&&n.props.type==='date').props.onChange({target:{value}});tree=a.render();a.h.commit();};
 setDay('2024-11-22');assert.match(textOf(tree),/Exact completion day is unknown/);assert.doesNotMatch(textOf(tree),/Interval average:/);
 setDay('2024-05-01');assert.doesNotMatch(textOf(tree),/Exact completion day is unknown/);assert.doesNotMatch(textOf(tree),/updated single-lane/);
 setDay('2024-04-28');assert.doesNotMatch(textOf(tree),/construction progressing/);
 a.button(tree,'Play work history').props.onClick();tree=a.render();a.h.commit();
 for(let i=0;i<200;i++){for(const fn of [...a.timers.values()])fn();tree=a.render();a.h.commit();}
 assert.equal(a.timers.size,0);assert.equal(findNode(tree,n=>n.type==='input'&&n.props.type==='date').props.value,'2024-11-22');
 a.h.dispose();
});
