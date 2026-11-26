import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import postcss from 'postcss';

const css=postcss.parse(await readFile('app/category-map-dock.css','utf8'));
// Bounded cascade evaluation of the actual dock rules: include media conditions,
// :has()/attribute specificity and final custom-property substitution. This is
// source/layout-math coverage; the normal browser journey checks real geometry.
function dockStyle(context){
 const declarations=new Map();let order=0;
 css.walkRules(rule=>{
  const relevant=rule.nodes.filter(node=>node.type==='decl'&&['max-height','bottom','display','--category-dock-height-ceiling'].includes(node.prop));
  if(!relevant.length)return;
  for(let parent=rule.parent;parent&&parent.type!=='root';parent=parent.parent){
   if(parent.type==='atrule'&&parent.name==='media'){
    const width=parent.params.match(/^\(max-width:\s*(\d+)px\)$/);assert.ok(width,`unsupported media condition: ${parent.params}`);
    if(context.width>Number(width[1]))return;
   }
  }
  for(const selector of rule.selectors){
   if(!/(?:^|\s)\.category-map-dock(?::has\(\[aria-label="Kansas LiDAR layers"\]\))?(?::not\(\[data-topic=terrain\]\))?$/.test(selector))continue;
   if(selector.includes('Kansas LiDAR layers')&&!context.native)continue;
   if(selector.includes(':not([data-topic=terrain])')&&context.topic==='terrain')continue;
   if(selector.includes('.measurement-readout')&&!context.measurement)continue;
   if(selector.includes('[data-live-dock="true"]')&&!context.live)continue;
   if(selector.includes('.hydrology-observatory')&&!context.hydrology)continue;
   if(selector.includes('.glm-flash-studio')&&!context.glm)continue;
   // All matching selectors use classes/attributes; :has itself contributes no
   // specificity, while its argument does. Fail on an unsupported selector.
   assert.match(selector,/^(?:\.map-stage(?:\[data-live-dock="true"\])?(?::has\(\.[\w-]+\))? )?\.category-map-dock(?::has\(\[aria-label="Kansas LiDAR layers"\]\))?(?::not\(\[data-topic=terrain\]\))?$/);
   const specificity=(selector.match(/\.[\w-]+|\[[^\]]+\]/g)??[]).length;
   relevant.forEach(decl=>{
    const weight=[Number(Boolean(decl.important)),specificity,++order],old=declarations.get(decl.prop);
    if(!old||weight.some((value,i)=>value!==old.weight[i]&&weight.slice(0,i).every((v,j)=>v===old.weight[j])&&value>old.weight[i]))declarations.set(decl.prop,{value:decl.value,weight});
   });
  }
 });
 return Object.fromEntries([...declarations].map(([key,decl])=>[key,decl.value]));
}
function splitTop(value,separator){
 let depth=0,start=0;const parts=[];
 for(let i=0;i<value.length;i++){
  if(value[i]==='(')depth++;else if(value[i]===')')depth--;
  else if(depth===0&&separator(value[i],i)){parts.push(value.slice(start,i));start=i+1;}
 }
 parts.push(value.slice(start));return parts;
}
function pixels(expression,style,context){
 const value=expression.trim(),literal=value.match(/^(-?\d+(?:\.\d+)?)(px|%)$/);
 if(literal)return Number(literal[1])*(literal[2]==='%'?context.height/100:1);
 const fn=value.match(/^([a-z]+)\((.*)\)$/);assert.ok(fn,`unsupported length: ${value}`);
 const [,name,body]=fn;
 if(name==='var'){
  const [key,fallback]=splitTop(body,c=>c===',');
  const resolved=style[key.trim()]??(key.trim()==='--live-dock-clearance'?`${context.clearance}px`:fallback);
  assert.notEqual(resolved,undefined,`missing custom property: ${key}`);return pixels(resolved,style,context);
 }
 if(name==='env'){assert.equal(body.split(',')[0],'safe-area-inset-bottom');return context.inset;}
 if(name==='min'||name==='max')return Math[name](...splitTop(body,c=>c===',').map(part=>pixels(part,style,context)));
 assert.equal(name,'calc');
 let depth=0,start=0,sign=1,total=0;
 for(let i=0;i<=body.length;i++){
  const c=body[i];if(c==='(')depth++;else if(c===')')depth--;
  if(i===body.length||(depth===0&&(c==='+'||c==='-'))){total+=sign*pixels(body.slice(start,i),style,context);sign=c==='-'?-1:1;start=i+1;}
 }
 return total;
}
const base={width:1280,height:900,inset:0,clearance:200,native:false,measurement:false,live:false};
const existingLimit=c=>c.live?c.height-c.clearance-(c.measurement?80:20):c.measurement?c.height-90-c.inset:c.width<=760?c.height-152-c.inset:c.height-28;
const existingBottom=c=>c.live?c.clearance+(c.measurement?66:6):c.measurement?76+c.inset:c.width<=760?80+c.inset:14+c.inset;

test('native dock ceiling survives measurement/live specificity while retaining every stricter clearance',()=>{
 for(const height of [420,900])for(const clearance of [200,320])for(const inset of [0,24])for(const measurement of [false,true])for(const live of [false,true]){
  const c={...base,height,clearance,inset,measurement,live,native:true},style=dockStyle(c);
  const ceiling=Math.min(height*.6,Math.max(100,height-200));
  assert.equal(pixels(style['max-height'],style,c),Math.min(ceiling,existingLimit(c)),JSON.stringify(c));
  assert.equal(pixels(style.bottom,style,c),existingBottom(c),'bottom clearance is independent of the native cap');
 }
});

test('other topic docks preserve their existing desktop/mobile height and bottom clearances',()=>{
 for(const width of [390,1280])for(const measurement of [false,true])for(const live of [false,true]){
  const c={...base,width,measurement,live,inset:24},style=dockStyle(c);
  assert.equal(pixels(style['max-height'],style,c),existingLimit(c));
  assert.equal(pixels(style.bottom,style,c),existingBottom(c));
 }
});

test('other topic docks still yield to phone measurements and taller live instruments',()=>{
 for(const native of [false,true]){
  const normal={...base,width:390,native},style=dockStyle(normal);
  assert.notEqual(style.display,'none');assert.equal(pixels(style['max-height'],style,normal),native?540:748);
  for(const flags of [{width:390,measurement:true},{width:390,live:true},{live:true,hydrology:true},{live:true,glm:true}])assert.equal(dockStyle({...base,native,...flags}).display,'none');
 }
});

test('a phone terrain cross-section remains visible while other topic measurement docks still step aside',()=>{const c={...base,width:375,height:667,measurement:true,topic:'terrain'};assert.notEqual(dockStyle(c).display,'none');assert.equal(dockStyle({...c,topic:'land'}).display,'none');assert.equal(dockStyle({...c,live:true}).display,'none','a live instrument retains its existing priority');});
