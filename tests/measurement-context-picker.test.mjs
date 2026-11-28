import test from 'node:test';
import assert from 'node:assert/strict';
import {modelUrl} from '../scripts/lib/typescript-model.mjs';
import {componentHarness,findNode} from './component-harness.mjs';

const metadata=await import(await modelUrl('app/collection-metadata.ts'));
const dictionary=await import(await modelUrl('app/collection-field-dictionary.ts'));
const lab=await import(await modelUrl('app/collection-lab.ts'));
const bundle=await import(await modelUrl('app/data-lab/lab-bundle.ts'));
const {recoveredCollection}=await import(await modelUrl('app/recovered-collections.ts'));
const collection=recoveredCollection('observations-usgs-daily-values');
const rows=Array.from({length:20},(_,index)=>({
 id:String(index+1),values:{file_id:1,row_number:index+1,value:String(index),
  parameter_code:'synthetic-'+index,unit_of_measure:'m',approval_status:'A'},
 provenance:{source_id:'synthetic-context-picker'},
}));
const snapshot={rows,pages:1,hasMore:true,answers:[{generatedAt:'2026-11-28T00:00:00Z'}]};
const fields=lab.profileCollection(collection,snapshot).fields.filter(field=>field.groups.length);

async function picker(t,patch={}){
 const harness=await componentHarness('app/data-lab/measurement-explorer.tsx',{
  '../collection-metadata':metadata,'../collection-field-dictionary':dictionary,
  '../collection-lab':lab,'./lab-bundle':bundle,'./lab.module.css':{default:{}},
 });
 t.after(()=>harness.dispose());
 const changes=[],props={collection,snapshot,fields,busy:false,save(){},view:null,
  onViewChange(view){changes.push(view);props.view=view;},...patch};
 const draw=()=>harness.render(harness.exports.default,props);
 const contexts=tree=>findNode(tree,node=>node.type==='select'&&node.props['aria-describedby']==='measurement-context-matches');
 const search=tree=>findNode(tree,node=>node.type==='input'&&node.props.type==='search');
 return {draw,contexts,search,props,changes};
}

test('context picker exposes and selects contexts beyond the twelve-group overview',async t=>{
 const {draw,contexts,props}=await picker(t);
 let tree=draw();
 assert.equal(fields[0].groups.length,12);
 assert.equal(contexts(tree).props.children.length,20);
 const last=contexts(tree).props.children.at(-1);
 contexts(tree).props.onChange({target:{value:last.props.value}});
 tree=draw();
 assert.equal(props.view.context,last.props.value);assert.equal(props.view.range,null);
 const bin=findNode(tree,node=>node.type==='button'&&node.props['aria-controls']==='measurement-range-records');
 assert.equal(bin.props['aria-label'],'Exactly 19: 1 record');
 bin.props.onClick();tree=draw();
 assert.deepEqual({...props.view.range},{lower:19,upper:19,includeUpper:true});
 assert.equal(findNode(tree,node=>node.type==='code'&&node.props.children==='20').props.children,'20');
});

test('context search retains the active chart and range with no matches, then a selection clears the range',async t=>{
 const {draw,contexts,search,props,changes}=await picker(t);
 let tree=draw();
 findNode(tree,node=>node.type==='button'&&node.props['aria-controls']==='measurement-range-records').props.onClick();
 const before=JSON.stringify(props.view),changeCount=changes.length;
 search(tree).props.onChange({target:{value:'NO MATCH'}});tree=draw();
 assert.equal(contexts(tree).props.children.length,1);
 assert.equal(contexts(tree).props.value,props.view.context);
 assert.equal(JSON.stringify(props.view),before);assert.equal(changes.length,changeCount);
 assert.match(JSON.stringify(findNode(tree,node=>node.props?.id==='measurement-context-matches')),/0 of 20 contexts match.*Current selection retained/);
 search(tree).props.onChange({target:{value:' SYNTHETIC-19 '}});tree=draw();
 assert.equal(contexts(tree).props.children.length,2,'matching context plus retained selection');
 const last=contexts(tree).props.children.at(-1);
 contexts(tree).props.onChange({target:{value:last.props.value}});tree=draw();
 assert.equal(props.view.context,last.props.value);assert.equal(props.view.range,null);
 assert.equal(contexts(tree).props.children.length,1);
 search(tree).props.onChange({target:{value:''}});tree=draw();
 assert.equal(contexts(tree).props.children.length,20);assert.equal(contexts(tree).props.value,last.props.value);
});

test('a measurement field switch clears search and range without carrying another field context',async t=>{
 const c={...collection,columns:[...collection.columns,'other_measurement']};
 const s={...snapshot,rows:rows.map(row=>({...row,values:{...row.values,other_measurement:2}}))};
 const {draw,search,contexts,props}=await picker(t,{collection:c,snapshot:s,
  fields:lab.profileCollection(c,s).fields.filter(field=>field.groups.length)});
 let tree=draw();
 search(tree).props.onChange({target:{value:'synthetic-19'}});tree=draw();
 findNode(tree,node=>node.type==='select'&&!node.props['aria-describedby']).props.onChange({target:{value:'other_measurement'}});
 tree=draw();
 assert.equal(search(tree).props.value,'');assert.equal(props.view.field,'other_measurement');
 assert.equal(props.view.range,null);assert.equal(contexts(tree).props.children.length,1);
 assert.equal(contexts(tree).props.value,props.view.context);
});
