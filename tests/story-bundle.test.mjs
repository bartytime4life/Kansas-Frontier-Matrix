import test from 'node:test';
import assert from 'node:assert/strict';
import { validStoryBundle, boundedStoryText, STORY_BUNDLE_BYTES } from '../app/living-welcome/stories/story-bundle.mjs';
const sample = () => ({ format:'kfm-story-bundle-v1',story:'shaking-ground',version:1,observed:{from:2020,to:2021},
  sources:[{name:'Synthetic contract test',url:'https://example.org/data',license:'Test only',citation:'Test only'}],
  data:{kind:'records',columns:[{key:'year',label:'Year',type:'number'},{key:'value',label:'Magnitude',type:'number'}],
    yearField:'year',valueField:'value',coverage:'Synthetic test only',limits:['Not observed data'],records:[{id:'a',year:2020,value:0,longitude:-98,latitude:38}]}});
test('valid zero and null measurements survive; mismatched and malformed payloads fail closed', () => {
  const b=sample(); assert.ok(validStoryBundle(b,b.story)); b.data.records[0].value=null; assert.ok(validStoryBundle(b,b.story));
  assert.equal(validStoryBundle(b,'census-mosaic'),false);
  for (const mutate of [b=>b.sources=[],b=>b.sources[0].url='javascript:alert(1)',b=>b.data.records.push({...b.data.records[0]}),
    b=>b.data.records[0].value='3',b=>b.data.records[0].value=NaN,b=>b.data.records[0].latitude=100,b=>b.data.valueField='missing',
    b=>b.data.columns.push({...b.data.columns[0]}),b=>b.data.limits=[]]) {
    const bad=sample();mutate(bad);assert.equal(validStoryBundle(bad,bad.story),false);
  }
  assert.equal(validStoryBundle({...sample(),story:'iron-horse'},'iron-horse'),false,'the rail renderer cannot consume generic records');
});
test('chunked and declared oversize responses are rejected before parsing',async()=>{
  assert.equal(await boundedStoryText(new Response('hello')),'hello');
  await assert.rejects(boundedStoryText(new Response('{}',{headers:{'content-length':String(STORY_BUNDLE_BYTES+1)}})),/limit/);
  let canceled=false;
  const body=new ReadableStream({start(c){c.enqueue(new Uint8Array(STORY_BUNDLE_BYTES));c.enqueue(new Uint8Array(1));},cancel(){canceled=true;}});
  await assert.rejects(boundedStoryText(new Response(body)),/limit/);assert.equal(canceled,true);
});

test('climate requires complete baseline normals so absolute values cannot become false anomalies', () => {
  const climate = () => ({ ...sample(), story: 'climate-stripes', data: {
    years: [2020], areas: [{id:'20',name:'Kansas'}], baselines:['1901-2000'], latest:{year:2020,month:12}, limits:['Synthetic test only'],
    elements: Object.fromEntries(['tmpc','pcpn','pdsi'].map(key => [key,{label:key,unit:key,scale:10,annual:key==='pcpn'?'sum':'mean'}])),
    values: Object.fromEntries(['tmpc','pcpn','pdsi'].map(key => [key,{'20':Array(12).fill(10)}])),
    normals:{'1901-2000':{tmpc:{'20':Array(12).fill(5)},pcpn:{'20':Array(12).fill(5)}}},
  }});
  assert.ok(validStoryBundle(climate(),'climate-stripes'));
  for (const mutate of [b=>b.data.normals['1901-2000']={},b=>b.data.normals['1901-2000'].tmpc['20'][1]=null,
    b=>delete b.data.latest,b=>delete b.data.elements.tmpc.label,b=>b.data.latest.month=13,
    b=>b.data.normals['1901-2000'].pcpn['20'].pop()]) {
    const bad=climate();mutate(bad);assert.equal(validStoryBundle(bad,'climate-stripes'),false);
  }
});

test('malformed geometry is rejected before reaching canvas traversal', () => {
  for (const value of [{type:'Point',coordinates:[0,100]}, {type:'Polygon',coordinates:[]},
    {type:'Polygon',coordinates:[[[0,0],[1,0],[1,1],[0,1]]]}, {type:'LineString',coordinates:[[0,0]]},
    {type:'MultiPolygon',coordinates:[[[['bad',0],[1,0],[1,1],['bad',0]]]]}]) {
    const b=sample();b.data.records[0].geometry=value;assert.equal(validStoryBundle(b,b.story),false);
  }
});
