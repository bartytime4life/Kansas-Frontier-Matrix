import test from 'node:test';
import assert from 'node:assert/strict';
import ts from 'typescript';
import vm from 'node:vm';
import React from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { readFile } from 'node:fs/promises';

const source = await readFile(new URL('../app/county-search.ts', import.meta.url), 'utf8');
const county = await import('data:text/javascript;base64,' + Buffer.from(ts.transpileModule(source, {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
}).outputText).toString('base64'));
const page = await readFile(new URL('../app/page.tsx', import.meta.url), 'utf8');
const tree = ts.createSourceFile('page.tsx', page, ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
let resultsExpression, searchMarkup;
function visit(node) {
  if (ts.isVariableDeclaration(node) && node.name.getText(tree) === 'searchResults') resultsExpression = node.initializer.getText(tree);
  if (ts.isJsxElement(node) && node.openingElement.attributes.properties.some(attribute =>
    ts.isJsxAttribute(attribute) && attribute.name.getText(tree) === 'className' && attribute.initializer?.getText(tree) === '"global-search"')) searchMarkup = node.getText(tree);
  ts.forEachChild(node, visit);
}
visit(tree);
const feature = { type: 'Feature', properties: { name: 'Ellsworth', featureId: 'us-census-county-20053', vintage: '2020' } };
const payload = { feed: 'census-counties', data: { features: [feature] } };
const mapItem = { id: 'layer:water', kind: 'layer', title: 'Water observations', subtitle: 'Current layer catalog' };
const sourceItem = { id: 'source:water', kind: 'source', title: 'Water', subtitle: 'Official provider · Water' };

function actualResults(query, settledQuery, state) {
  return vm.runInNewContext(ts.transpileModule('(' + resultsExpression + ')', {
    compilerOptions: { target: ts.ScriptTarget.ES2022 },
  }).outputText, {
    useMemo: callback => callback(), globalQuery: query, debouncedGlobalQuery: settledQuery,
    SEARCH_INDEX: [mapItem], OFFICIAL_CONTEXT_SOURCES: [{ id: 'water', title: 'Water', shortTitle: 'Water', organization: 'Official provider', domain: 'Water', endpointLabel: 'Water records' }],
    officialPayloads: { 'census-counties': payload }, officialStates: { 'census-counties': state }, ...county,
  });
}

function actualMarkup(query, settledQuery, state, results) {
  const searchStatus = county.globalSearchStatus(query, settledQuery, state, results.length);
  const element = vm.runInNewContext(ts.transpileModule('(' + searchMarkup + ')', {
    compilerOptions: { jsx: ts.JsxEmit.React, target: ts.ScriptTarget.ES2022 },
  }).outputText, { React, searchStatus, searchResults: results, globalQuery: query, globalSearchInputRef: { current: null }, setGlobalQuery() {}, chooseSearchResult() {} });
  return renderToStaticMarkup(element);
}

test('blank queries remain quiet and changed queries report work while stale rows are withheld', () => {
  for (const state of ['idle', 'loading', 'error', 'empty', 'partial', 'ready']) {
    assert.deepEqual(county.globalSearchStatus('   ', 'Water', state, 2), { message: '', busy: false });
    assert.deepEqual(county.globalSearchStatus('Ellsworth', 'Water', state, 2), { message: 'Updating search…', busy: true });
    assert.equal(actualResults('Ellsworth', 'Water', state).length, 0);
  }
  assert.equal(actualResults('', 'Water', 'ready').length, 0);
  assert.equal(actualResults('  WATER  ', 'Water', 'ready').length, 2);
});

test('county pending, failed, empty and partial states never claim a completed no-match', () => {
  for (const resultCount of [0, 2]) {
    assert.deepEqual(county.globalSearchStatus('Ellsworth', 'Ellsworth', 'idle', resultCount), { message: 'County search is not ready. Available layers, features, and official sources can still be searched.', busy: false });
    assert.deepEqual(county.globalSearchStatus('Ellsworth', 'Ellsworth', 'loading', resultCount), { message: 'Loading county matches…', busy: true });
    assert.deepEqual(county.globalSearchStatus('Ellsworth', 'Ellsworth', 'error', resultCount), {
      message: resultCount ? 'County search is unavailable. Showing available matches.' : 'County search is unavailable. You can still search available layers, features, and official sources.', busy: false,
    });
    assert.deepEqual(county.globalSearchStatus('Ellsworth', 'Ellsworth', 'empty', resultCount), { message: 'No counties are available to search.', busy: false });
    assert.deepEqual(county.globalSearchStatus('Ellsworth', 'Ellsworth', 'partial', resultCount), { message: 'County search has limited coverage.', busy: false });
  }
});

test('a settled ready search alone may report no matches for the current query', () => {
  assert.deepEqual(county.globalSearchStatus('  Saline  ', 'Saline', 'ready', 0), {
    message: 'No matches for “Saline”. Try a county, layer, feature, or official source name.', busy: false,
  });
  assert.deepEqual(county.globalSearchStatus('Water', 'Water', 'ready', 2), { message: '', busy: false });
});

test('unexpected runtime states cannot establish complete county coverage', () => {
  for (const state of [undefined, null, 'held', 'unavailable']) {
    const status = county.globalSearchStatus('Saline', 'Saline', state, 0);
    assert.match(status.message, /^County search is unavailable\./);
    assert.doesNotMatch(status.message, /No matches/);
    assert.equal(status.busy, false);
  }
});

test('actual search keeps available layer and official-source matches when county data cannot be searched', () => {
  for (const state of ['idle', 'loading', 'error', 'empty', 'partial', 'ready']) {
    assert.deepEqual(Array.from(actualResults('Water', 'Water', state), item => item.id), [sourceItem.id, mapItem.id]);
  }
  assert.equal(actualResults('Ellsworth', 'Ellsworth', 'ready').length, 1);
  assert.equal(actualResults('Ellsworth', 'Ellsworth', 'partial').length, 1);
  for (const state of ['idle', 'loading', 'error', 'empty']) assert.equal(actualResults('Ellsworth', 'Ellsworth', state).length, 0);
});

test('actual result markup renders scoped, polite readiness feedback beside usable partial results', () => {
  for (const state of ['idle', 'loading', 'error', 'empty', 'partial', 'ready']) {
    const results = Array.from(actualResults('Water', 'Water', state));
    const html = actualMarkup('Water', 'Water', state, results);
    assert.equal((html.match(/<button /g) ?? []).length, 2);
    assert.match(html, /role="status"/);
    assert.match(html, /aria-live="polite"/);
    assert.match(html, /aria-atomic="true"/);
    assert.match(html, new RegExp('aria-busy="' + (state === 'loading') + '"'));
    assert.doesNotMatch(html, /No matches|No current place/);
    if (state === 'partial') assert.match(html, /County search has limited coverage\./);
    if (state === 'error') assert.match(html, /County search is unavailable\. Showing available matches\./);
  }
});

test('actual input clears its popup for blank queries and hides obsolete buttons during debounce', () => {
  for (const query of ['', '   ']) {
    const html = actualMarkup(query, 'Water', 'loading', Array.from(actualResults(query, 'Water', 'loading')));
    assert.doesNotMatch(html, /id="global-search-results"|role="status"|<button /);
    assert.match(html, /aria-busy="false"/);
  }
  const html = actualMarkup('Ellsworth', 'Water', 'ready', Array.from(actualResults('Ellsworth', 'Water', 'ready')));
  assert.match(html, /Updating search…/);
  assert.match(html, /aria-busy="true"/);
  assert.doesNotMatch(html, /<button |No matches/);
});

test('no-match query remains escaped text in the actual markup', () => {
  const html = actualMarkup('<img src=x onerror=alert(1)>', '<img src=x onerror=alert(1)>', 'ready', []);
  assert.match(html, /&lt;img src=x onerror=alert\(1\)&gt;/);
  assert.doesNotMatch(html, /<img|dangerouslySetInnerHTML/);
});
