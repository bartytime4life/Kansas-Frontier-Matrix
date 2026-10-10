import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { componentHarness, findNode, settle } from './component-harness.mjs';

const moduleUrl = code => `data:text/javascript;base64,${Buffer.from(code).toString('base64')}`;
const transpile = async file => ts.transpileModule(await readFile(file, 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const boundedUrl = moduleUrl(await transpile('app/bounded-json.ts'));
const bounded = await import(boundedUrl);
const model = await import(moduleUrl((await transpile('app/history-research-model.ts')).replace('"./bounded-json"', JSON.stringify(boundedUrl))));
const css = new Proxy({}, { get: (_, key) => String(key) });
function nodes(tree, predicate) { const result = []; function visit(node) { if (!node || typeof node !== 'object') return; if (predicate(node)) result.push(node); for (const child of [node.props?.children].flat(Infinity)) visit(child); } visit(tree); return result; }
function content(node) { if (typeof node === 'string' || typeof node === 'number') return String(node); if (!node || typeof node !== 'object') return ''; return [node.props?.children].flat(Infinity).map(content).join(' ').replace(/\s+/g, ' '); }
const button = (tree, label) => findNode(tree, node => node.type === 'button' && content(node) === label);
const field = (tree, id) => findNode(tree, node => node.props?.id === id);
const entries = tree => nodes(findNode(tree, node => node.type === 'ul' && node.props['aria-label'] === 'Source research entries'), node => node.type === 'article');
const sourceRows = tree => nodes(findNode(tree, node => node.type === 'ul' && node.props['aria-label'] === 'Supplied research sources'), node => node.type === 'article');

function catalog() {
  const sources = Array.from({ length: 15 }, (_, index) => ({ id: `source-${index}`, title: `Kansas source ${index}`, publisher: `Publisher ${index}`, url: `https://history.org/source-${index}`, access: index === 0 ? 'readable' : index === 1 ? 'partial' : 'blocked', accessNote: index > 1 ? 'Provider page was inaccessible during this check.' : 'Read supplied page metadata.', coverage: 'Supplied page entries only.', rights: 'Metadata links; original publisher terms apply.', recordCount: index === 0 ? 35 : index === 1 ? 32 : 0, completeness: index > 1 ? 'Not acquired; completeness unknown.' : 'All supplied-page entries captured.', checkedAt: '2026-10-09' }));
  const records = Array.from({ length: 67 }, (_, index) => ({ id: `entry-${index}`, sourceId: index < 35 ? 'source-0' : 'source-1', kind: index % 2 ? 'event' : 'person', title: `Kansas entry ${index}`, category: 'History', date: index === 0 ? '1900 — collection date' : null, place: index === 0 ? 'Topeka — collection context' : null, relation: 'Listed by this supplied source in a Kansas collection.', sourceUrl: sources[index < 35 ? 0 : 1].url, targetUrl: `https://history.org/entry-${index}`, reviewNote: 'Candidate assertion; relation has not been independently resolved.', themes: ['Kansas', 'history'] }));
  return { schemaVersion: 1, checkedAt: '2026-10-09', scope: 'All supplied-page records; verify Kansas connections as needed.', attribution: 'Source authors retain rights in original works.', lifecycle: { sourceAdmission: 'NOT_ADMITTED', review: 'PENDING', mapActivation: 'NONE' }, sources, records };
}

async function harness(fetcher = async () => new Response(JSON.stringify(catalog()))) {
  const calls = [];
  const modelHarness = await componentHarness('app/history-research-model.ts', { './bounded-json': bounded }, { fetch: (...args) => { calls.push(args); return fetcher(...args); } });
  const h = await componentHarness('app/history/people-events/page.tsx', {
    '../../history-research-model': modelHarness.exports, '../../downloads/workspace.module.css': { default: css }, '../../history-research.module.css': { default: css },
  });
  return { calls, h, render: () => { const tree = h.render(h.exports.default, {}); h.commit(); return tree; }, dispose: () => { h.dispose(); modelHarness.dispose(); } };
}

test('catalogue preserves source assertions, nullable context and all 15 source states', () => {
  const input = catalog(); input.futureMetadata = true;
  const parsed = model.parseHistoryResearchCatalog(input);
  assert.equal(parsed.records.length, 67); assert.equal(parsed.sources.length, 15);
  assert.equal(parsed.records[0].date, '1900 — collection date'); assert.equal(parsed.records[0].place, 'Topeka — collection context');
  assert.equal(parsed.records[1].date, null); assert.equal(parsed.sources[2].access, 'blocked');
  assert.equal(model.filterHistoryResearch(parsed, 'Topeka collection', 'all', 'all').length, 1);
  assert.equal(model.filterHistoryResearch(parsed, '.*', 'all', 'all').length, 0, 'search treats punctuation literally');
  assert.equal(model.historyResearchKnowledgeLink('A & B?/' + 'x'.repeat(100)), `/knowledge?term=${encodeURIComponent(('A & B?/' + 'x'.repeat(100)).slice(0, 80))}`);
});

test('bundled research catalogue is valid, fits the byte budget and retains all supplied sources', async () => {
  const bytes = await readFile('public/history/people-events.json');
  assert.ok(bytes.length <= model.HISTORY_RESEARCH_MAX_BYTES);
  const parsed = await model.readHistoryResearchCatalog(new Response(bytes));
  assert.equal(parsed.sources.length, 15);
  assert.equal(parsed.sources.filter(source => source.access === 'blocked').length, 4);
  assert.equal(parsed.records.length, 1448);
  assert.equal(parsed.sources.reduce((total, source) => total + source.recordCount, 0), parsed.records.length);
});

test('invalid references, duplicate identifiers, inconsistent counts and malformed fields reject the complete catalogue', () => {
  const mutate = [
    value => { value.records[0].sourceId = 'missing'; },
    value => { value.records[1].id = value.records[0].id; },
    value => { value.sources[1].id = value.sources[0].id; },
    value => { value.sources[0].recordCount++; },
    value => { value.records[0].date = {}; },
    value => { value.records[0].kind = 'verified-person'; },
    value => { value.records[0].themes = [false]; },
    value => { value.sources[0].rights = ''; },
    value => { value.sources[0].access = 'admitted'; },
    value => { value.sources[0].access = ['readable']; },
    value => { value.lifecycle.sourceAdmission = 'ADMITTED'; },
    value => { value.lifecycle.review = 'APPROVED'; },
    value => { value.lifecycle.mapActivation = 'ACTIVE'; },
    value => { delete value.records[0].reviewNote; },
  ];
  for (const change of mutate) { const value = catalog(); change(value); assert.equal(model.parseHistoryResearchCatalog(value), null); }
  for (const value of [null, [], {}, 'catalogue', { ...catalog(), records: {} }]) assert.equal(model.parseHistoryResearchCatalog(value), null);
});

test('unsafe link schemes, credentials and local destinations never become source links', () => {
  for (const url of ['javascript:alert(1)', 'data:text/html,x', '//history.org', 'https://u:p@history.org/', 'https://127.0.0.1/', 'http://2130706433/', 'http://[::1]/', 'https://localhost/', 'https://service.local/', 'https://history.org:8080/', 'https://history.org\\@evil.org/', 'https://history.org/\npage']) {
    assert.equal(model.historyResearchUrl(url), false, url);
    for (const key of ['sourceUrl', 'targetUrl']) { const value = catalog(); value.records[0][key] = url; assert.equal(model.parseHistoryResearchCatalog(value), null); }
    const value = catalog(); value.sources[0].url = url; assert.equal(model.parseHistoryResearchCatalog(value), null);
  }
  assert.equal(model.historyResearchUrl('http://www.kansashistory.us/'), true);
  assert.equal(model.historyResearchUrl('https://en.wikipedia.org/wiki/List_of_people_from_Kansas'), true);
});

test('catalogue stream enforces 3 MiB before parse including missing or misleading lengths', async () => {
  assert.equal(model.HISTORY_RESEARCH_MAX_BYTES, 3145728);
  await assert.rejects(model.readHistoryResearchCatalog(new Response('[]', { headers: { 'content-length': '3145729' } })), /limit exceeded/);
  for (const headers of [{}, { 'content-length': '1' }]) {
    let cancelled = false;
    const body = new ReadableStream({ start(controller) { controller.enqueue(new Uint8Array(3145729)); }, cancel() { cancelled = true; } });
    await assert.rejects(model.readHistoryResearchCatalog(new Response(body, { headers })), /limit exceeded/);
    assert.equal(cancelled, true);
  }
  await assert.rejects(model.readHistoryResearchCatalog(new Response('{"unfinished":')), SyntaxError);
  await assert.rejects(model.readHistoryResearchCatalog(new Response(new Uint8Array([255]))), TypeError);
  await assert.rejects(model.readHistoryResearchCatalog(new Response('{}')), /could not be validated/);
  await assert.rejects(model.readHistoryResearchCatalog(new Response('No', { status: 503 })), /unavailable/);
  const abort = new AbortController(); abort.abort();
  await assert.rejects(model.readHistoryResearchCatalog(new Response(JSON.stringify(catalog())), abort.signal), { name: 'AbortError' });
});

test('real page loads one stable same-origin resource, paginates 30 entries and keeps source coverage visible', async () => {
  const p = await harness(); let tree = p.render(); assert.match(content(tree), /Loading research metadata/);
  assert.equal(p.calls.length, 1); assert.equal(p.calls[0][0], '/history/people-events.json');
  assert.equal(p.calls[0][1].mode, 'same-origin'); assert.equal(p.calls[0][1].credentials, 'same-origin'); assert.equal(p.calls[0][1].redirect, 'error');
  await settle(); tree = p.render();
  assert.equal(entries(tree).length, 30); assert.match(content(entries(tree)[0]), /Kansas entry 0/);
  assert.equal(sourceRows(tree).length, 15); assert.match(content(sourceRows(tree)[2]), /Blocked — not acquired.*0 curated entries.*completeness unknown/);
  assert.equal(button(tree, 'Previous entries').props.disabled, true);
  button(tree, 'Next entries').props.onClick(); tree = p.render(); assert.equal(entries(tree).length, 30); assert.match(content(entries(tree)[0]), /Kansas entry 30/);
  button(tree, 'Next entries').props.onClick(); tree = p.render(); assert.equal(entries(tree).length, 7); assert.match(content(entries(tree)[0]), /Kansas entry 60/); assert.equal(button(tree, 'Next entries').props.disabled, true);
  button(tree, 'Previous entries').props.onClick(); tree = p.render(); assert.match(content(entries(tree)[0]), /Kansas entry 30/);
  assert.equal(p.calls.length, 1, 'browsing never fetches provider pages');
  p.dispose(); assert.equal(p.calls[0][1].signal.aborted, true);
});

test('actual search, source, kind and clear callbacks each reset pagination; no results preserve blocked sources', async () => {
  const p = await harness(); p.render(); await settle(); let tree = p.render();
  button(tree, 'Next entries').props.onClick(); tree = p.render();
  field(tree, 'history-research-source').props.onChange({ target: { value: 'source-1' } }); tree = p.render();
  assert.equal(entries(tree).length, 30); assert.match(content(entries(tree)[0]), /Kansas entry 35/); assert.match(content(tree), /page 1 of 2/);
  button(tree, 'Next entries').props.onClick(); tree = p.render();
  field(tree, 'history-research-kind').props.onChange({ target: { value: 'event' } }); tree = p.render();
  assert.equal(entries(tree).length, 16); assert.match(content(entries(tree)[0]), /Kansas entry 35/); assert.equal(button(tree, 'Previous entries').props.disabled, true);
  button(tree, 'Clear filters').props.onClick(); tree = p.render(); button(tree, 'Next entries').props.onClick(); tree = p.render();
  field(tree, 'history-research-query').props.onChange({ target: { value: 'Kansas entry 6' } }); tree = p.render();
  assert.equal(entries(tree).length, 13); assert.match(content(entries(tree)[0]), /Kansas entry 6/); assert.equal(button(tree, 'Previous entries').props.disabled, true);
  field(tree, 'history-research-query').props.onChange({ target: { value: 'no-such-person' } }); tree = p.render();
  assert.equal(entries(tree).length, 0); assert.match(content(tree), /No entries match these filters/); assert.equal(sourceRows(tree).length, 15);
  button(tree, 'Clear filters').props.onClick(); tree = p.render();
  assert.equal(entries(tree).length, 30); assert.equal(field(tree, 'history-research-source').props.value, 'all'); assert.equal(field(tree, 'history-research-kind').props.value, 'all'); assert.equal(field(tree, 'history-research-query').props.value, '');
  field(tree, 'history-research-source').props.onChange({ target: { value: 'source-2' } }); tree = p.render(); assert.equal(entries(tree).length, 0); assert.equal(sourceRows(tree).length, 15);
  assert.equal(p.calls.length, 1); p.dispose();
});

test('entries expose source attribution and assertion context, safe external links and a separate reviewed knowledge search', async () => {
  const input = catalog(); input.records[0].title = '<script>A & B?</script>';
  const p = await harness(async () => new Response(JSON.stringify(input))); p.render(); await settle(); const tree = p.render(); const entry = entries(tree)[0];
  assert.match(content(entry), /Source: Kansas source 0.*Publisher 0/); assert.match(content(entry), /1900 — collection date/); assert.match(content(entry), /Topeka — collection context/);
  assert.match(content(entries(tree)[1]), /Not specified in this entry/); assert.match(content(tree), /matching released record may be absent/);
  assert.equal(nodes(tree, node => ['script', 'iframe', 'img'].includes(node.type) || node.props?.dangerouslySetInnerHTML).length, 0);
  const links = nodes(entry, node => node.type === 'a');
  assert.equal(links.find(link => content(link).startsWith('Search reviewed KFM')).props.href, `/knowledge?term=${encodeURIComponent(input.records[0].title)}`);
  for (const link of links.filter(link => link.props.href.startsWith('http'))) { assert.equal(link.props.target, '_blank'); assert.equal(link.props.rel, 'noopener noreferrer'); }
  assert.deepEqual(nodes(tree, node => node.type === 'a' && node.props.download).map(link => link.props.href), ['/history/people-events.json', '/history/people-events.csv']);
  assert.match(content(tree), /source admission: not admitted.*review: pending.*map activation: none/); p.dispose();
});

test('failed validation displays no partial entries and actual retry clears error while awaiting a new catalogue', async () => {
  const pending = [];
  const p = await harness(() => new Promise(resolve => pending.push(resolve))); p.render();
  const broken = catalog(); broken.records[0].sourceId = 'missing'; pending.shift()(new Response(JSON.stringify(broken))); await settle();
  let tree = p.render(); assert.ok(findNode(tree, node => node.props?.role === 'alert')); assert.equal(entries(tree).length, 0); assert.equal(sourceRows(tree).length, 0);
  button(tree, 'Retry loading').props.onClick(); tree = p.render(); assert.equal(p.calls.length, 2); assert.equal(p.calls[0][1].signal.aborted, true);
  assert.equal(findNode(tree, node => node.props?.role === 'alert'), undefined); assert.match(content(tree), /Loading research metadata/);
  pending.shift()(new Response(JSON.stringify(catalog()))); await settle(); tree = p.render(); assert.equal(entries(tree).length, 30); p.dispose();
});

test('unmounted page aborts its request and ignores a late response', async () => {
  let respond;
  const p = await harness(() => new Promise(resolve => { respond = resolve; })); p.render(); p.dispose();
  assert.equal(p.calls[0][1].signal.aborted, true);
  respond(new Response(JSON.stringify(catalog()))); await settle();
  assert.equal(entries(p.render()).length, 0);
});
