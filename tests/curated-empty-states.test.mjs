import assert from 'node:assert/strict';
import test from 'node:test';
import { componentHarness, findNode, settle } from './component-harness.mjs';

const text = node => {
  if (typeof node === 'string' || typeof node === 'number') return String(node);
  if (!node || typeof node !== 'object') return '';
  return [node.props?.children].flat(Infinity).map(text).join('');
};
const empty = tree => findNode(tree, node => node.type === 'p' && node.props.role === 'status' && (
  /^(Checking for source records|Source records are withheld|Source records are unavailable|No approved snapshot|No records in this snapshot|This partial snapshot)/.test(text(node))
));
const product = (overrides = {}) => ({
  state: 'empty', sourceId: 'usgs-streamflow', evidenceRole: 'EXTERNAL_CONTEXT_ONLY',
  releaseId: 'a'.repeat(64), approvalExpiresAt: '2099-01-01T00:00:00Z',
  data: { type: 'FeatureCollection', features: [] }, ...overrides,
});

async function workspace() {
  const calls = [];
  let resolve, reject;
  const response = new Promise((yes, no) => { resolve = yes; reject = no; });
  const h = await componentHarness(new URL('../app/curated/workspace.tsx', import.meta.url), {
    'next/link': { default: 'a' },
    '../maplibre-seam': { loadMapLibre: async () => ({}) },
    '../kansas-orientation': { ORIENTATION_SOURCE_ID: 'orientation', orientationSource() {}, orientationLayers: () => [] },
    '../bounded-json': { readBoundedJson: async response => response.json() },
    './workspace.css': {},
  }, {
    queueMicrotask, setInterval: () => 1, clearInterval() {},
    document: { visibilityState: 'visible' },
    fetch: url => { calls.push(url); return url.endsWith('/history') ? Promise.resolve({ json: async () => ({ items: [] }) }) : response; },
  });
  const render = () => { const tree = h.render(h.exports.default); h.commit(); return tree; };
  render(); await settle();
  return {
    h, render, calls,
    async show(value) { resolve({ json: async () => value }); await settle(); return render(); },
    async fail() { reject(new Error('network unavailable')); await settle(); return render(); },
  };
}

test('records explain a pending read without claiming a zero result', async t => {
  const w = await workspace(); t.after(() => w.h.dispose());
  const tree = w.render();
  assert.equal(text(empty(tree)), 'Checking for source records…');
  assert.ok(findNode(tree, node => node.type === 'button' && node.props.disabled && text(node) === 'Checking…'));
  assert.ok(findNode(tree, node => node.type === 'div' && node.props['aria-label'] === 'Dated Kansas provider context map'));
  assert.ok(findNode(tree, node => node.type === 'a' && node.props.href === '/'));
});

const recordFixture = () => product({ state:'available', data:{type:'FeatureCollection',features:Array.from({length:63},(_,i)=>({
  type:'Feature',id:'record-'+(i+1),geometry:null,properties:{stationId:'SYNTHETIC-'+String(i+1).padStart(4,'0'),value:i,unit:'TEST UNIT',...(i===2?{headline:'Álert — river'}:{})},
}))}});
const allNodes=(tree,predicate)=>!tree||typeof tree!=='object'?[]:[...(predicate(tree)?[tree]:[]),...[tree.props?.children].flat(Infinity).flatMap(child=>allNodes(child,predicate))];
const recordRows=tree=>allNodes(findNode(tree,n=>n.type==='ul'&&n.props.className==='curated-records'),n=>n.type==='li');
const action=(tree,label)=>findNode(tree,n=>n.type==='button'&&text(n)===label);
const query=tree=>findNode(tree,n=>n.type==='input'&&n.props.type==='search');

test('large snapshots render bounded pages without additional source requests',async t=>{
 const w=await workspace();t.after(()=>w.h.dispose());let tree=await w.show(recordFixture());
 assert.equal(recordRows(tree).length,25);assert.equal(action(tree,'Previous records').props.disabled,true);assert.match(text(tree),/Showing 1–25 of 63 records/);
 let focused=0;findNode(tree,n=>n.props.id==='curated-records-heading').props.ref.current={focus:()=>focused++,scrollIntoView(){}};
 action(tree,'Next records').props.onClick();tree=w.render();assert.equal(recordRows(tree).length,25);assert.match(text(recordRows(tree)[0]),/SYNTHETIC-0026/);assert.equal(focused,1);
 action(tree,'Next records').props.onClick();tree=w.render();assert.equal(recordRows(tree).length,13);assert.equal(action(tree,'Next records').props.disabled,true);assert.match(text(tree),/Showing 51–63 of 63 records/);
 action(tree,'Previous records').props.onClick();tree=w.render();assert.match(text(recordRows(tree)[0]),/SYNTHETIC-0026/);
 assert.equal(w.calls.length,2,'paging does not fetch, download or alter the source');
});

test('record search matches words in any order across IDs and labels, ignoring case, accents and punctuation',async t=>{
 const w=await workspace();t.after(()=>w.h.dispose());let tree=await w.show(recordFixture());
 action(tree,'Next records').props.onClick();tree=w.render();
 for(const [value,label] of [['SYNTHETIC 0063','SYNTHETIC-0063'],['river alert','Álert — river'],['RECORD 42','SYNTHETIC-0042']]){
  query(tree).props.onChange({target:{value}});tree=w.render();assert.equal(recordRows(tree).length,1);assert.match(text(recordRows(tree)[0]),new RegExp(label));assert.match(text(tree),/Showing 1–1 of 1 matching records · 63 in this snapshot/);
 }
});

test('no-match recovery restores the first page and returns focus to search',async t=>{
 const w=await workspace();t.after(()=>w.h.dispose());let tree=await w.show(recordFixture());
 query(tree).props.onChange({target:{value:'no matching station'}});tree=w.render();
 assert.equal(recordRows(tree).length,0);assert.match(text(tree),/No records match “no matching station” in this snapshot/);assert.equal(empty(tree),undefined);
 let focused=0;query(tree).props.ref.current={focus:()=>focused++};action(tree,'Clear search').props.onClick();tree=w.render();
 assert.equal(focused,1);assert.equal(query(tree).props.value,'');assert.equal(recordRows(tree).length,25);assert.match(text(tree),/Showing 1–25 of 63 records/);
});

test('search and paging retain selection and the unfiltered provenance download',async t=>{
 const w=await workspace();t.after(()=>w.h.dispose());const data=recordFixture();let tree=await w.show(data);
 const download=findNode(tree,n=>n.type==='a'&&n.props.download).props.href;
 findNode(recordRows(tree)[0],n=>n.type==='button').props.onClick();tree=w.render();
 action(tree,'Next records').props.onClick();tree=w.render();query(tree).props.onChange({target:{value:'synthetic 0063'}});tree=w.render();
 assert.ok(findNode(tree,n=>n.props['aria-label']==='Selected source record'));assert.match(text(findNode(tree,n=>n.props['aria-label']==='Selected source record')),/SYNTHETIC-0001/);
 assert.equal(findNode(tree,n=>n.type==='a'&&n.props.download).props.href,download);assert.equal(data.data.features.length,63);assert.equal(w.calls.length,2);
});

test('an active query never turns pending, withheld or unavailable data into a completed no-match',async t=>{
 for(const result of [{state:'withheld',reason:'NO_APPROVED_RELEASE'},{state:'unavailable'}]){
  const w=await workspace();t.after(()=>w.h.dispose());let tree=w.render();query(tree).props.onChange({target:{value:'synthetic'}});tree=w.render();
  assert.equal(text(empty(tree)),'Checking for source records…');assert.doesNotMatch(text(tree),/No records match/);
  tree=await w.show(result);assert.ok(empty(tree));assert.doesNotMatch(text(tree),/No records match/);assert.equal(query(tree).props.value,'synthetic');
 }
});

test('changing source resets record filters and never reuses the previous source rows',async t=>{
 const w=await workspace();t.after(()=>w.h.dispose());let tree=await w.show(recordFixture());
 query(tree).props.onChange({target:{value:'synthetic 0063'}});tree=w.render();
 findNode(tree,n=>n.type==='select'&&n.props.value==='usgs-streamflow').props.onChange({target:{value:'nws-alerts'}});tree=w.render();
 assert.equal(query(tree).props.value,'');assert.equal(recordRows(tree).length,0);assert.doesNotMatch(text(tree),/SYNTHETIC-0063|No records match/);
});

test('withheld and missing approvals explain why records are not listed and retain the source reason', async t => {
  for (const [reason, message, sourceReason] of [
    ['PIPELINE_NOT_CONFIGURED', 'Source records are withheld. See the publication reason above.', 'Published snapshots are not configured yet.'],
    ['APPROVAL_REVOKED', 'Source records are withheld. See the publication reason above.', 'This snapshot has been withheld following review.'],
    ['NO_APPROVED_RELEASE', 'No approved snapshot is available to list records.', 'No approved snapshot is available.'],
  ]) {
    const w = await workspace(); t.after(() => w.h.dispose());
    const tree = await w.show({ state: 'withheld', reason });
    assert.equal(text(empty(tree)), message);
    assert.ok(findNode(tree, node => node.type === 'p' && text(node) === sourceReason));
    assert.ok(findNode(tree, node => node.type === 'button' && text(node) === 'Refresh'));
    assert.doesNotMatch(text(tree), /No records in this snapshot/);
  }
});

test('failed reads and incomplete responses are unavailable, not successful empty snapshots', async t => {
  const failed = await workspace(); t.after(() => failed.h.dispose());
  assert.equal(text(empty(await failed.fail())), 'Source records are unavailable. Refresh to check again.');
  for (const value of [
    { state: 'unavailable' }, { state: 'empty' },
    product({ sourceId: 'nws-alerts' }), product({ evidenceRole: 'EVIDENCE' }),
    product({ data: { type: 'FeatureCollection', features: null } }),
    product({ state: 'withheld', reason: 'APPROVAL_REVOKED' }),
  ]) {
    const w = await workspace(); t.after(() => w.h.dispose());
    const tree = await w.show(value);
    assert.doesNotMatch(text(tree), /No records in this snapshot/);
    assert.ok(empty(tree), 'an empty records section still explains its state');
  }
});

test('only a compatible successful zero-record collection is described as an empty snapshot', async t => {
  for (const state of ['empty', 'available']) {
    const w = await workspace(); t.after(() => w.h.dispose());
    const tree = await w.show(product({ state }));
    assert.equal(text(empty(tree)), 'No records in this snapshot.');
    assert.equal(findNode(tree, node => node.type === 'ul' && node.props.className === 'curated-records'), undefined);
  }
});

test('a partial zero-record publication preserves the incomplete-coverage distinction', async t => {
  const w = await workspace(); t.after(() => w.h.dispose());
  const tree = await w.show(product({ state: 'partial' }));
  assert.equal(text(empty(tree)), 'This partial snapshot supplies no records; coverage may be incomplete.');
  assert.doesNotMatch(text(tree), /No records in this snapshot/);
});

test('a populated snapshot retains its record list and free provenance download without an empty message', async t => {
  const w = await workspace(); t.after(() => w.h.dispose());
  const tree = await w.show(product({ state: 'available', data: { type: 'FeatureCollection', features: [
    { type: 'Feature', id: 'gauge-1', geometry: null, properties: { stationId: 'USGS-test-gauge', value: 12, unit: 'ft³/s' } },
  ] } }));
  assert.equal(empty(tree), undefined);
  const list = findNode(tree, node => node.type === 'ul' && node.props.className === 'curated-records');
  assert.match(text(list), /USGS-test-gauge/);
  assert.ok(findNode(tree, node => node.type === 'a' && node.props.download === 'usgs-streamflow-' + 'a'.repeat(64) + '.json'));
  assert.match(text(tree), /not admitted evidence or an emergency notification service/);
});
