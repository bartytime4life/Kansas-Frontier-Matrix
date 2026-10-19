import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
import {componentHarness,findNode} from './component-harness.mjs';

const compiled = ts.transpileModule(await readFile('app/earth-engine-data.ts', 'utf8'), {
 compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
}).outputText;
const data = await import(`data:text/javascript;base64,${Buffer.from(compiled).toString('base64')}`);
const dataset = id => data.EARTH_ENGINE_DATASETS.find(item => item.id === id);
const text = node => node == null || typeof node === 'boolean' ? '' : typeof node !== 'object' ? String(node)
 : Array.isArray(node) ? node.map(text).join('') : text(node.props?.children);
async function hostedPanel(t) {
 const h = await componentHarness('app/earth-engine-downloads.tsx', {
  'next/link': {default:'a'}, './earth-engine-data': data,
  './earth-engine/workspace.module.css': {default:new Proxy({}, {get:(_,key)=>key})},
 }, { fetch: () => assert.fail('Discovery must not start a network request'),
  window: {open: () => assert.fail('Discovery must not open an authentication window')} });
 t.after(() => h.dispose());
 return { render: props => {const tree=h.render(h.exports.default, props);h.commit();return tree;} };
}

test('hosted annual discovery preserves the provider, selected year, resolution and source limitations', async t => {
 const h = await hostedPanel(t), source = dataset('ee-cdl');
 const tree = h.render({dataset:source, year:2023, invalid:false});
 assert.equal(tree.props['aria-label'], 'Source files and reviewed captures');
 const paragraphs = tree.props.children.filter(node => node?.type === 'p');
 assert.equal(text(paragraphs[0]), `${source.provider} · 2023 · ${source.resolution}`);
 assert.equal(text(paragraphs[1]), source.limitation);
 assert.equal(text(findNode(tree, node => node.props?.role === 'status')),
  'Hosted capture is not configured for this source. Reviewed map layers remain separate from original provider files.');
 assert.equal(findNode(tree, node => ['button','form','input'].includes(node.type)), undefined);
});

test('invalid source periods explain the hold and do not expose a download or sign-in action', async t => {
 const h = await hostedPanel(t);
 const tree = h.render({dataset:dataset('ee-cdl'), year:1900, invalid:true});
 assert.equal(text(findNode(tree, node => node.props?.role === 'status')), 'Choose a valid source period above.');
 assert.equal(findNode(tree, node => node.type === 'form' || node.type === 'button' || node.props?.download), undefined);
 const catalog = findNode(tree, node => node.props?.target === '_blank');
 assert.equal(catalog.props.href, data.earthEngineUrl(dataset('ee-cdl')));
});

test('mixed-date terrain retains source-mosaic semantics without inventing a selected year', async t => {
 const h = await hostedPanel(t), source = dataset('ee-3dep');
 const tree = h.render({dataset:source, year:undefined, invalid:false});
 assert.ok(text(tree).includes(`${source.provider} · source mosaic · ${source.resolution}`));
 assert.ok(text(tree).includes(source.limitation));
 assert.doesNotMatch(text(tree), /undefined|NaN|2023/);
});

test('each registered dataset links to its own official provider catalog and the hosted source status', async t => {
 const h = await hostedPanel(t);
 for (const source of data.EARTH_ENGINE_DATASETS) {
  const tree = h.render({dataset:source, year:source.lastYear ?? undefined, invalid:false});
  const catalog = findNode(tree, node => node.props?.target === '_blank');
  const href = new URL(catalog.props.href);
  assert.equal(href.origin, 'https://developers.google.com');
  assert.equal(href.pathname, `/earth-engine/datasets/catalog/${source.catalogSlug}`);
  assert.equal(href.search, ''); assert.equal(href.hash, '');
  assert.equal(catalog.props.rel, 'noreferrer');
  assert.ok(findNode(tree, node => node.type === 'a' && node.props.href === '/?layers=sources'));
  assert.equal(findNode(tree, node => typeof node.props?.href === 'string' && /127\.0\.0\.1|localhost|auth\/start/.test(node.props.href)), undefined);
 }
});

test('changing dataset and year replaces displayed provenance and catalog without retaining the prior selection', async t => {
 const h = await hostedPanel(t), first = dataset('ee-cdl'), next = dataset('ee-landsat8');
 h.render({dataset:first, year:2023, invalid:false});
 const tree = h.render({dataset:next, year:2019, invalid:false});
 assert.ok(text(tree).includes(`${next.provider} · 2019 · ${next.resolution}`));
 assert.ok(text(tree).includes(next.limitation));
 assert.ok(!text(tree).includes(first.limitation));
 assert.equal(findNode(tree, node => node.props?.target === '_blank').props.href, data.earthEngineUrl(next));
});

test('legacy connected-operator props cannot turn hosted discovery into a PC control surface', async t => {
 const h = await hostedPanel(t);
 const forbidden = new Proxy({}, {get:() => assert.fail('Hosted discovery must not access an operator session')});
 const props = {dataset:dataset('ee-cdl'), year:2023, invalid:false};
 const plain = h.render(props);
 const compatibility = h.render({...props, downloads:forbidden, compact:true, blockedByOtherDownload:false,
  onViewActivity:() => assert.fail('Hosted discovery must not open local activity')});
 assert.deepEqual(compatibility, plain);
});

test('recipe navigation focuses the newly selected heading after render and respects reduced motion',async()=>{
 const datasets=[{id:'ee-cdl',title:'CDL',topic:'Crops',temporalMode:'annual',firstYear:2000,lastYear:2023},{id:'ee-water',title:'Water',topic:'Water',temporalMode:'annual',firstYear:2000,lastYear:2024}];
 const transitions=[];let reduced=true,renderedTitle='';
 const h=await componentHarness('app/earth-engine/workspace.tsx',{
  'next/link':{default:'a'},'../earth-engine-data':{EARTH_ENGINE_DATASETS:datasets,findEarthEngineDatasets:()=>datasets,buildEarthEngineRecipe:()=>'',earthEngineUrl:()=>'',earthEngineReviewPacket:()=>({})},
  '../earth-engine-context':{EARTH_ENGINE_CONTEXT_LAYERS:[],EARTH_ENGINE_SOURCE_YEARS:{}},'../earth-engine-context-client':{useEarthEngineContext:()=>({loading:false,manifests:[],error:null})},
  '../earth-engine-export':{buildEarthEngineExportRecipe:()=>''},'../source-history':{SourceHistory:'source-history'},'../earth-engine-downloads':{default:'downloads'},'./workspace.module.css':{default:new Proxy({},{get:(_,key)=>key})},
 },{URLSearchParams,window:{location:{search:''},matchMedia:query=>{assert.equal(query,'(prefers-reduced-motion: reduce)');return {matches:reduced};}},document:{getElementById:id=>{assert.equal(id,'recipe-workspace');return {scrollIntoView:options=>transitions.push({kind:'scroll',behavior:options.behavior})};}}});
 const render=()=>{const tree=h.render(h.exports.default);const heading=findNode(tree,n=>n.props?.id==='recipe-title');renderedTitle=heading.props.children;assert.equal(heading.props.tabIndex,-1);heading.props.ref.current={focus:options=>transitions.push({kind:'focus',title:renderedTitle,preventScroll:options.preventScroll})};h.commit();return tree;};
 let tree=render();assert.equal(transitions.length,0);
 const water=findNode(tree,n=>n.type==='article'&&findNode(n,c=>c.type==='button'&&c.props.children==='Water'));
 findNode(water,n=>n.type==='button'&&n.props.children==='Download / view years').props.onClick();assert.equal(transitions.length,0,'wait until the selected content is rendered');tree=render();
 assert.deepEqual(transitions,[{kind:'focus',title:'Water',preventScroll:true},{kind:'scroll',behavior:'instant'}]);
 reduced=false;const selected=findNode(tree,n=>n.type==='article'&&findNode(n,c=>c.type==='button'&&c.props.children==='Water'));findNode(selected,n=>n.type==='button'&&n.props.children==='Download / view years').props.onClick();render();
 assert.deepEqual(transitions.slice(2),[{kind:'focus',title:'Water',preventScroll:true},{kind:'scroll',behavior:'smooth'}]);h.dispose();
});
