import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import * as jsxRuntime from 'react/jsx-runtime';
import { renderToStaticMarkup } from 'react-dom/server';

// Execute actual page projections and JSX with synthetic records; no provider or release calls.
async function compile(path, dependencies = {}) {
  const exports = {};
  const js = ts.transpileModule(await readFile(path, 'utf8'), { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText;
  new Function('exports', 'require', js)(exports, name => {
    assert.ok(name in dependencies, `Unexpected dependency ${name}`); return dependencies[name];
  });
  return exports;
}
const civic = await compile('app/civic-districts.ts');
const history = await compile('app/civic-history.ts', { './civic-districts': civic });
const temporal = await compile('app/temporal-sweep.ts');
const source = await readFile('app/page.tsx', 'utf8');
const tree = ts.createSourceFile('page.tsx', source, ts.ScriptTarget.ES2022, true, ts.ScriptKind.TSX);
const declarations = new Map();
let sourceCard, timeWarning;
function visit(node) {
  if (ts.isVariableDeclaration(node)) declarations.set(node.name.getText(tree), node.initializer?.getText(tree));
  if (ts.isJsxElement(node) && node.openingElement.attributes.properties.some(attribute =>
    attribute.name?.getText(tree) === 'aria-label' && attribute.initializer?.text === 'Selected external source and telemetry')) sourceCard = node.getText(tree);
  if (ts.isJsxExpression(node) && node.expression?.getText(tree).startsWith('selectedTimeMismatch &&')) timeWarning = node.expression.getText(tree);
  ts.forEachChild(node, visit);
}
visit(tree);
function evaluate(expression, scope) {
  const js = ts.transpileModule(`return (${expression});`, { fileName: 'test.tsx', compilerOptions: {
    module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.ReactJSX,
  } }).outputText;
  return new Function('exports', 'require', ...Object.keys(scope), js)({}, () => jsxRuntime, ...Object.values(scope));
}
const pageValue = (name, scope = {}) => {
  assert.ok(declarations.has(name), `Missing page declaration ${name}`);
  return evaluate(declarations.get(name), scope);
};
const str = (properties, key) => typeof properties[key] === 'string' ? properties[key] : null;
const ids = pageValue('officialContextIdForSelection', { OFFICIAL_CONTEXT_SOURCES: [civic.CIVIC_SOURCE, { id: 'nws-alerts' }] });
const held = pageValue('officialSelectionIsHeld', { ...civic, ...history, officialContextIdForSelection: ids, OFFICIAL_CONTEXT_PRESENT_FRAME: 2026 });
const carrierVisible = pageValue('selectionCarrierIsVisible', { officialContextIdForSelection: ids });
const contextTime = pageValue('officialContextTime', { CIVIC_ID: civic.CIVIC_ID, stringContextProperty: str });
const contextSummary = pageValue('officialContextSummary', { ...civic, ...history, stringContextProperty: str });
const select = pageValue('buildBasemapContext', {
  ...civic, ...history, OFFICIAL_CONTEXT_BY_SOURCE_ID: { [civic.CIVIC_SOURCE.sourceId]: civic.CIVIC_SOURCE },
  BASEMAP_CONTEXT_LAYER: {}, officialContextTime: contextTime, officialContextSummary: contextSummary,
  stringContextProperty: str, drawerArtifactAttributes: () => [],
});
const polygon = { type: 'Polygon', coordinates: [[[-99,38],[-98,38],[-98,39],[-99,39],[-99,38]]] };
function record(day = '1861-01-29') {
  const congress = history.civicCongressForDay(day), plan = history.civicHistoryPlan(congress);
  return { type: 'Feature', id: 'synthetic-plan-id', geometry: polygon, properties: {
    featureId: 'synthetic-plan-id', name: 'Synthetic at-large constituency', sourceDay: day,
    congressNumber: congress, congress: history.civicCongressLabel(congress),
    termStart: history.civicTermStart(congress), termEndExclusive: history.civicTermStart(congress + 1),
    sourceRevision: plan.commit,
  } };
}
const selection = feature => select({ ...feature, source: civic.CIVIC_SOURCE.sourceId }, -99, 38);
function flags(selected, day = '1861-01-29', visible = true, buildYearCurrent = true) {
  const scope = { ...civic, ...history, ...temporal, selected, selectedOfficialContextId: ids(selected), civicFrameDay: day,
    temporalQuery: { mode: 'snapshot', frame: Number(day?.slice(0,4) ?? 1860) }, OFFICIAL_CONTEXT_PRESENT_FRAME: 2026,
    buildYearCurrent, officialSelectionIsHeld: held, selectionCarrierIsVisible: carrierVisible, visibility: { 'synthetic-registry': visible },
    effectiveOfficialVisibility: { [civic.CIVIC_ID]: visible, 'nws-alerts': visible }, selectedEvidenceFiltered: false };
  for (const name of ['selectedIsHeldOfficialContext', 'selectedTimeMismatch', 'selectedLayerHidden', 'selectionVisible']) scope[name] = pageValue(name, scope);
  return scope;
}

test('the selected historical record carries its exact day and Congress into time, visibility and halo gates', () => {
  const picked = selection(record());
  assert.deepEqual(picked.civicRecord, { sourceDay: '1861-01-29', congressNumber: 36, termStart: '1861-01-29', termEndExclusive: '1861-03-04' });
  const valid = flags(picked);
  assert.equal(valid.selectedTimeMismatch, false);
  assert.equal(valid.selectedLayerHidden, false);
  assert.equal(valid.selectionVisible, true);
  const hidden = flags(picked, '1861-01-29', false);
  assert.equal(hidden.selectedTimeMismatch, false, 'Hiding the layer does not change source time');
  assert.equal(hidden.selectedLayerHidden, true);
  assert.equal(hidden.selectionVisible, false);
});

test('same-year changes, shared plan IDs, unsupported dates, missing metadata and stale builds stay withheld', () => {
  const picked = selection(record());
  for (const day of ['1861-01-30', '1861-03-04', '2026-10-29', null]) {
    assert.equal(flags(picked, day).selectedTimeMismatch, true, String(day));
    assert.equal(flags(picked, day).selectionVisible, false, String(day));
  }
  assert.equal(flags(picked, '1861-01-29', true, false).selectedTimeMismatch, true);
  assert.equal(flags({ ...picked, civicRecord: undefined }).selectedTimeMismatch, true);
  assert.equal(history.civicRecordMatchesDay({ sourceDay: '1861-01-29', congressNumber: '36' }, '1861-01-29'), false);
  assert.equal(history.civicRecordMatchesDay({ sourceDay: '1900-02-29', congressNumber: 56 }, '1900-02-29'), false);
  assert.equal(history.civicRecordMatchesDay({ sourceDay: '1861-01-29', congressNumber: 37 }, '1861-01-29'), false);
});

test('the existing undated Census edition remains usable only within its declared 119th term', () => {
  const raw = { type: 'FeatureCollection', features: [1,2,3,4].map(district => ({ type: 'Feature', geometry: polygon,
    properties: { GEOID: `200${district}`, STATE: '20', CDSESSN: '119' } })) };
  const payload = civic.parseCivicDistricts(raw, new Date('2026-10-29T00:00:00Z'));
  const picked = selection(payload.data.features[0]);
  for (const day of ['2025-01-03', '2026-10-29', '2027-01-02']) assert.equal(flags(picked, day).selectedTimeMismatch, false);
  for (const day of ['2025-01-02', '2027-01-03']) assert.equal(flags(picked, day).selectedTimeMismatch, true);
  assert.equal(history.civicRecordMatchesDay({ congressNumber: 119 }, '2026-10-29'), false);
  assert.equal(history.civicRecordMatchesDay({ ...picked.civicRecord, termEndExclusive: '2028-01-03' }, '2026-10-29'), false);
  assert.equal(history.civicRecordMatchesDay({ ...picked.civicRecord, sourceDay: '2025-01-03' }, '2026-10-29'), false);
  for (const sourceDay of [undefined, '2025-01-03', '2025-01-04']) {
    const found = pageValue('selectedOfficialFeature', { ...history, ...civic, selected: picked,
      selectedOfficialContextId: civic.CIVIC_ID, civicFrameDay: '2025-01-03', selectedOfficialPayload: { ...payload, sourceDay } });
    assert.equal(found, sourceDay === '2025-01-04' ? undefined : payload.data.features[0]);
  }
});

test('a reused feature ID cannot replace captured historical attributes with another day or Congress', () => {
  const first = record(), picked = selection(first);
  const loaded = (feature, sourceDay = '1861-01-29') => pageValue('selectedOfficialFeature', {
    ...history, ...civic, selected: picked, selectedOfficialContextId: civic.CIVIC_ID, civicFrameDay: '1861-01-29',
    selectedOfficialPayload: { sourceDay, data: { features: [feature] } },
  });
  assert.equal(loaded(first), first);
  assert.equal(loaded(record('1861-01-30')), undefined);
  assert.equal(loaded(record('1861-03-04')), undefined);
  assert.equal(loaded(first, '1861-01-30'), undefined);
  assert.equal(loaded({ ...first, properties: { ...first.properties, featureId: 'other' } }), undefined);
});

test('registry, basemap and present-only provider selection behavior remains bounded', () => {
  const registry = { kind: 'registry', featureId: 'fixture', layerId: 'synthetic-registry',
    layer: { temporal: { mode: 'exact' } }, properties: { year: 1861 } };
  assert.equal(flags(registry).selectionVisible, true);
  assert.equal(flags(registry, '1862-01-01').selectionVisible, false);
  assert.equal(flags(registry, '1861-01-29', false).selectedLayerHidden, true);
  const basemap = { kind: 'basemap', featureId: 'basemap:fixture', layerId: 'basemap', layer: {}, properties: { year: 2026 } };
  assert.equal(flags(basemap).selectionVisible, true);
  const alert = { ...basemap, featureId: 'official-context:alert:fixture', layerId: 'official-context-nws-alerts' };
  assert.equal(flags(alert).selectedTimeMismatch, true);
  assert.equal(flags(alert, '2026-10-29').selectedTimeMismatch, false);
  assert.equal(flags(alert, '2026-10-29', false).selectedLayerHidden, true);
});

test('the actual source card uses neutral context language and keeps scholarly credit and immutable links', () => {
  assert.ok(sourceCard);
  const sourceRecord = history.civicSourceForRecord(record().properties);
  const html = renderToStaticMarkup(evaluate(sourceCard, {
    selectedOfficialConnection: { source: sourceRecord, state: 'ready', featureCount: 1, retrievedAt: '2026-10-29T00:00:00Z' },
    selectedRiverObservation: null, drawerTimestamp: value => value,
  }));
  assert.match(html, /SOURCE CONTEXT/);
  assert.match(html, /Jeffrey B. Lewis/);
  assert.ok(html.includes(sourceRecord.sourceUrl));
  assert.match(html, /Open source/);
  assert.doesNotMatch(html, /OFFICIAL SOURCE|Open official source/);
});

test('the actual time warning is absent for a matching historical record and explains an incompatible exact day', () => {
  assert.ok(timeWarning);
  const picked = selection(record());
  const render = day => renderToStaticMarkup(evaluate(timeWarning, { ...flags(picked, day), formatTimelineStep: String, temporalScopeLabel: day }));
  assert.equal(render('1861-01-29'), '');
  const html = render('1861-03-04');
  assert.match(html, /1861-01-29/);
  assert.match(html, /1861-03-04/);
  assert.doesNotMatch(html, /Current official context|outside 2026/);
});

test('style initialization and recovery use the same qualified historical selection gates', () => {
  const start = source.indexOf('styleStep = "SELECTION";');
  const end = source.indexOf('styleStep = "MEASUREMENT";', start);
  assert.ok(start >= 0 && end > start);
  const initialize = source.slice(start, end);
  for (const [day, visible, buildCurrent, expected] of [
    ['1861-01-29', true, true, true], ['1861-03-04', true, true, false],
    ['1861-01-29', false, true, false], ['1861-01-29', true, false, false],
  ]) {
    const picked = selection(record()), shown = [];
    const scope = { ...civic, ...history, ...temporal, currentSelection: picked, selectedRef: { current: picked },
      temporalQueryRef: { current: { mode: 'snapshot', frame: Number(day.slice(0,4)) } },
      buildYearCurrentRef: { current: buildCurrent }, calendarSweepRef: { current: { day } }, calendarFrameDay: frame => frame.day,
      OFFICIAL_CONTEXT_PRESENT_FRAME: 2026, currentUtcDay: () => '2026-10-29',
      officialSelectionIsHeld: held, selectionCarrierIsVisible: carrierVisible,
      visibilityRef: { current: {} }, officialVisibilityRef: { current: { [civic.CIVIC_ID]: true } },
      noaaRadarReadyRef: { current: false }, noaaRadarFrameTimeRef: { current: null },
      runtimeOfficialVisibility: () => ({ [civic.CIVIC_ID]: visible }),
      selectionPassesEvidenceFilter: () => true, mapEvidenceFilterRef: { current: 'ALL' },
      updateSelectionSource: (_map, geometry) => shown.push(geometry), map: {},
    };
    const js = ts.transpileModule(`let styleStep; ${initialize}`, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText;
    new Function(...Object.keys(scope).filter(key => key !== 'currentSelection'), js)(...Object.entries(scope).filter(([key]) => key !== 'currentSelection').map(([,value]) => value));
    assert.equal(Boolean(shown[0]), expected, `style initialization ${day}/${visible}/${buildCurrent}`);
    assert.equal(Boolean(pageValue('selectionAvailable', scope)), expected, `style recovery ${day}/${visible}/${buildCurrent}`);
  }
});
