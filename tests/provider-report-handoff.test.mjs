import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';

// Execute the owning page's projection/renderers and actual drawer action.
// Fixtures contain invented provider records; no network or release operation.
const source = await readFile(new URL('../app/page.tsx', import.meta.url), 'utf8');
const tree = ts.createSourceFile('page.tsx', source, ts.ScriptTarget.ES2022, true, ts.ScriptKind.TSX);
function optionalDeclaration(name) {
  let result;
  function visit(node) {
    if (ts.isVariableDeclaration(node) && node.name.getText(tree) === name) result = node.initializer;
    ts.forEachChild(node, visit);
  }
  visit(tree);
  return result?.getText(tree);
}
function declaration(name) {
  const result = optionalDeclaration(name);
  assert.ok(result, `${name} is owned by the existing page`);
  return result;
}
function execute(name, scope = {}) {
  const js = ts.transpileModule(`return ${declaration(name)};`, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText;
  return new Function(...Object.keys(scope), js)(...Object.values(scope));
}
const provider = { id: 'census-counties', organization: 'U.S. Census Bureau', sourceUrl: 'https://www.census.gov/test', attribution: 'Census synthetic fixture', boundary: 'External context only; not KFM evidence.' };
const selection = { kind: 'basemap', featureId: 'official-context:county:20053', layerId: 'official-context-census-counties',
  layer: { title: 'Census counties' }, properties: { title: 'Ellsworth County', summary: '2020 Census population 6,376.', temporalScope: '2020 Census geography, population and housing baseline', year: 2026, evidenceState: 'MISSING_EVIDENCE', releaseState: 'GENERALIZED', uncertainty: 'Selected map snapshot.' }, geometry: { privateSentinel: 'NEVER_COPY_GEOMETRY' } };
const safeUrl = value => { try { const u = new URL(value); return u.protocol === 'https:' && !u.username && !u.password ? u.href : null; } catch { return null; } };
const project = () => execute('buildProviderReportSelection', { officialContextIdForSelection: item => item?.layerId === 'official-context-census-counties' && item.featureId.startsWith('official-context:') ? 'census-counties' : null, researchSourceUrl: safeUrl });
const input = overrides => ({ selected: selection, timeMismatch: false, locationPrivate: false, source: provider,
  attributes: [{ label: 'County GEOID', value: '20053' }, { label: 'Census edition', value: '2020' }, { label: 'Population count', value: '6,376' }],
  attributesCurrent: true, sourceState: 'ready', retrievedAt: '2026-10-28T12:00:00Z', providerUpdatedAt: '2026-10-27T00:00:00Z', observedAt: null, limitation: 'Synthetic fixture; no evidence admission.', ...overrides });
const providerSelectionValues = () => ({
  buildProviderReportSelection: project(), selectedOfficialConnection: { source: provider, state: 'ready', retrievedAt: '2026-10-28T12:00:00Z' },
  selectedOfficialPayload: { upstreamUpdatedAt: null, limitation: 'Fixture only' }, selectedRiverObservation: null,
  selectedArtifactAttributes: input().attributes, selectedAttributesCurrent: true,
});
const reportValues = () => ({
  reportDetail: 'STANDARD', reportRecords: [], scenePreset: 'flat', terrainState: 'IDLE', attachedTerrainProviderRef: { current: null }, terrainProvider: 'usgs-3dep', topographicOverlay: false,
  reportTitle: 'Ellsworth source context', reportScope: 'SELECTION', reportQuery: '', mapEvidenceFilter: 'ALL', reportEvidenceFilter: 'ALL', reportLayerIds: [], temporalQuery: { frame: 2026 }, temporalScopeLabel: '2026', temporalMode: 'snapshot', reportTemporalComparison: {},
  locationCameraRedacted: false, locationDerivedViewRef: { current: false }, researchLocationRedacted: false, subsurfacePrivate: false,
  view: { center: [-98, 38], zoom: 6, bearing: 0, pitch: 0 }, mapRepresentationLabel: '2D', verticalExaggeration: 1, lockedTerrainElevation: null, projection: 'mercator', basemap: 'vector', mapViewportBounds: null, analysisArea: null,
  measurementGeometryMode: null, selected: selection, selectedTimeMismatch: false, reportSections: { summary: true, findings: true, records: true, evidence: true, limitations: true }, reportLayerSummary: [], reportEvidenceCounts: {}, reportFindings: [],
  ...providerSelectionValues(),
});

test('county source context retains its own 2020 source axis and bounded attributes, never geometry or EvidenceRef', () => {
  const result = project()(input());
  assert.equal(result.status, 'AVAILABLE');
  assert.equal(result.role, 'EXTERNAL_CONTEXT_ONLY');
  assert.equal(result.evidenceBundle, null);
  assert.equal(result.context.title, 'Ellsworth County');
  assert.match(result.context.sourceTime, /^2020 Census/);
  assert.equal(result.context.retrievedAt, '2026-10-28T12:00:00Z');
  assert.equal(result.context.providerUpdatedAt, '2026-10-27T00:00:00Z');
  assert.deepEqual(result.context.attributes[2], { label: 'Population count', value: '6,376' });
  assert.ok(!JSON.stringify(result).includes('NEVER_COPY_GEOMETRY'));
  assert.equal(result.context.year, undefined, 'map year is not relabeled as provider year');
  assert.equal(result.evidenceReference, undefined);
});

test('stale context preserves original clocks with an explicit stale response state; incompatible and missing selections disclose no fields', () => {
  const build = project();
  const stale = build(input({ sourceState: 'error' }));
  assert.equal(stale.context.sourceState, 'error');
  assert.equal(stale.context.retrievedAt, '2026-10-28T12:00:00Z');
  assert.match(stale.context.fieldBasis, /snapshot|loaded/i);
  const incompatible = build(input({ timeMismatch: true }));
  assert.equal(incompatible.status, 'INCOMPATIBLE');
  assert.equal(incompatible.context, null);
  assert.equal(build(input({ selected: null })), null);
  assert.equal(build(input({ selected: { ...selection, kind: 'registry' } })), null);
});

test('location/private/local/unknown provider selection details are withheld before projection', () => {
  const build = project();
  for (const overrides of [ { locationPrivate: true }, { source: undefined }, { source: { ...provider, id: 'different' } },
    { selected: { ...selection, featureId: 'site-local:private', layerId: 'local-file' } },
    { selected: { ...selection, properties: { ...selection.properties, releaseState: 'RESTRICTED' } } },
    { selected: { ...selection, properties: { ...selection.properties, evidenceState: 'DENIED_BY_POLICY' } } } ]) {
    const result = build(input(overrides));
    assert.equal(result.status, 'WITHHELD'); assert.equal(result.context, null);
    assert.doesNotMatch(JSON.stringify(result), /Ellsworth|20053|6,376|census\.gov/);
  }
});

test('projection bounds text/rows, refuses unsafe source URLs, and HTML escapes all source content', () => {
  const build = project();
  const malicious = '<img src=x onerror="alert(1)"> & \' unsafe';
  const result = build(input({ selected: { ...selection, properties: { ...selection.properties, title: malicious, summary: 'x'.repeat(5000) } },
    source: { ...provider, sourceUrl: 'javascript:alert(1)', organization: malicious },
    attributes: Array.from({ length: 100 }, () => ({ label: malicious, value: malicious + 'x'.repeat(500) })) }));
  assert.equal(result.context.sourceUrl, null); assert.equal(result.context.summary.length, 2000);
  assert.equal(result.context.attributes.length, 32); assert.ok(result.context.attributes.every(row => row.value.length <= 240));
  const escapeReportHtml = execute('escapeReportHtml');
  const html = execute('providerReportHtml', { escapeReportHtml })(result);
  assert.match(html, /EXTERNAL_CONTEXT_ONLY/); assert.match(html, /No KFM EvidenceBundle/);
  assert.match(html, /&lt;img/); assert.doesNotMatch(html, /<img|javascript:|<script/);
  const ordinary = execute('providerReportHtml', { escapeReportHtml })(build(input()));
  assert.match(ordinary, /Ellsworth County/); assert.match(ordinary, /2020 Census/); assert.match(ordinary, /6,376/);
  assert.match(ordinary, /https:\/\/www\.census\.gov\/test/);
});

test('drawer Create report and Add to report share the provider handoff; registry action still opens its governed draft', () => {
  const calls = [];
  const scopes = { ...providerSelectionValues(), selected: selection, selectedTimeMismatch: false, locationCameraRedacted: false, locationDerivedViewRef: { current: false },
    researchLocationRedacted: false, subsurfacePrivate: false, researchContext: { oldNearbyPoint: true },
    setReportScope: value => calls.push(['scope', value]), setReportTitle: value => calls.push(['title', value]),
    setReportQuery: value => calls.push(['query', value]), setReportEvidenceFilter: value => calls.push(['filter', value]),
    openMapUtility: (...args) => calls.push(['utility', ...args]), openPrimaryWorkspace: (...args) => calls.push(['governed', ...args]) };
  let action;
  function visit(node) {
    if (ts.isJsxElement(node) && node.openingElement.tagName.getText(tree) === 'button'
      && node.children.some(child => ts.isJsxText(child) && child.text.trim() === 'Create report')) {
      action = node.openingElement.attributes.properties.find(attribute => attribute.name?.getText(tree) === 'onClick')?.initializer?.expression?.getText(tree);
    }
    ts.forEachChild(node, visit);
  }
  visit(tree); assert.ok(action, 'actual drawer Create report action exists');
  if (optionalDeclaration('openSelectedReport')) scopes.openSelectedReport = execute('openSelectedReport', scopes);
  const actionJs = ts.transpileModule(`return ${action};`, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText;
  new Function(...Object.keys(scopes), actionJs)(...Object.values(scopes))({ currentTarget: 'return-control' });
  assert.deepEqual(calls.find(call => call[0] === 'scope'), ['scope', 'SELECTION']);
  assert.deepEqual(calls.find(call => call[0] === 'utility'), ['utility', 'report', 'return-control']);
  assert.ok(calls.find(call => call[0] === 'title')[1].includes('Ellsworth'));
  assert.ok(!calls.some(call => call[0] === 'governed'));
  calls.length = 0; scopes.selected = { ...selection, kind: 'registry' };
  execute('openSelectedReport', scopes)();
  assert.deepEqual(calls, [['governed', 'reports', true, null, scopes.researchContext]]);
  assert.ok(/openSelectedReport\(event\.currentTarget\)\}>Create report/.test(source), 'Create report delegates to the provider-aware handoff');
  assert.ok(/openSelectedReport\(event\.currentTarget\)\}>Add to report/.test(source), 'Add to report shares the same handoff');
});

test('actual JSON builder recomputes immediate-ref privacy and carries the same provider projection, separately from active map time', () => {
  const values = reportValues();
  const build = () => execute('buildCustomReportPayload', values)('2026-10-28T14:00:00Z');
  const result = build();
  assert.equal(result.activeTime.value, 2026); assert.match(result.selection.context.sourceTime, /^2020 Census/);
  assert.equal(result.selection.role, 'EXTERNAL_CONTEXT_ONLY'); assert.deepEqual(result.records, []);
  for (const gate of ['state', 'immediate-ref', 'research-private', 'subsurface-private']) {
    values.locationCameraRedacted = gate === 'state'; values.locationDerivedViewRef.current = gate === 'immediate-ref';
    values.researchLocationRedacted = gate === 'research-private'; values.subsurfacePrivate = gate === 'subsurface-private';
    const privateReport = build(); assert.equal(privateReport.selection.status, 'WITHHELD');
    assert.doesNotMatch(JSON.stringify(privateReport), /Ellsworth|20053|6,376|census\.gov/);
  }
  assert.match(source, /providerReportHtml\(report\.selection/);
  assert.match(source, /aria-label="Selected provider source context"/);
});

test('unknown/local/restricted/incompatible and immediate-private handoffs never retain a secret title after selection clears or changes', () => {
  const secret = 'SECRET_PROVIDER_LABEL';
  const secretSelection = { ...selection, properties: { ...selection.properties, title: secret } };
  const cases = [
    { selectedOfficialConnection: undefined },
    { selected: { ...secretSelection, featureId: 'site-local:private', layerId: 'local-file' } },
    { selected: { ...secretSelection, properties: { ...secretSelection.properties, releaseState: 'RESTRICTED' } } },
    { selectedTimeMismatch: true },
    { locationDerivedViewRef: { current: true } },
  ];
  for (const overrides of cases) {
    const values = { ...reportValues(), selected: secretSelection, ...overrides };
    execute('openSelectedReport', { ...values, researchContext: null,
      setReportScope: value => { values.reportScope = value; }, setReportTitle: value => { values.reportTitle = value; },
      setReportQuery() {}, setReportEvidenceFilter() {}, openMapUtility() {}, openPrimaryWorkspace() {},
    })();
    assert.match(values.reportTitle, /^(Withheld|Incompatible) source-context report$/);
    for (const nextSelection of [null, { ...selection, properties: { ...selection.properties, title: 'Public county' } }]) {
      const next = { ...values, selected: nextSelection, selectedTimeMismatch: false, locationDerivedViewRef: { current: false }, ...providerSelectionValues() };
      const report = execute('buildCustomReportPayload', next)('2026-10-28T14:00:00Z');
      assert.ok(!JSON.stringify(report).includes(secret), 'a cleared/replaced selection cannot reveal a retained private label');
    }
  }
});

test('ordinary report download serializes the same context in JSON and escaped HTML without converting it into an evidence record', async () => {
  const blobs = [], links = [];
  const selection = project()(input());
  const report = { title: 'County source context', scope: 'SELECTION', activeTime: { label: '2026' }, selection,
    mapContext: { terrain: { heightOverlay: { enabled: false, lockedReading: null } } }, summary: null, records: [], findings: [], limitations: [], attribution: [],
    temporalComparison: { timeA: 2025, timeB: 2026, timeARecordCount: 0, timeBRecordCount: 0, recordDelta: 0, changedLayerCount: 0 } };
  const escapeReportHtml = execute('escapeReportHtml');
  const download = execute('downloadCustomReport', {
    buildCustomReportPayload: () => report, setReportGeneratedAt() {}, reportRecords: [], escapeReportHtml,
    providerReportHtml: execute('providerReportHtml', { escapeReportHtml }), formatTimelineStep: String,
    Blob, URL: { createObjectURL(blob) { blobs.push(blob); return 'blob:synthetic'; }, revokeObjectURL() {} },
    document: { createElement() { const link = { click() {}, remove() {} }; links.push(link); return link; }, body: { append() {} } }, window: { setTimeout() {} }, announce() {},
  });
  download('json'); download('html');
  assert.deepEqual(JSON.parse(await blobs[0].text()).selection, selection);
  const html = await blobs[1].text();
  for (const value of ['Ellsworth County', '2020 Census', '6,376', 'EXTERNAL_CONTEXT_ONLY', 'No KFM EvidenceBundle']) assert.ok(html.includes(value), `actual HTML download keeps ${value}`);
  assert.ok(html.includes('active time 2026')); assert.doesNotMatch(html, /<h2>Included records/);
  assert.equal(links[0].download, 'county-source-context.json'); assert.equal(links[1].download, 'county-source-context.html');
});

test('actual HTML download preserves replacement tokens once without expanding them into document fragments', async () => {
  const blobs = [];
  const selected = { ...selection, properties: { ...selection.properties, title: 'TITLE[$&]', summary: 'SUMMARY[$`]' } };
  const providerSelection = project()(input({ selected, attributes: [{ label: 'Literal token', value: "FIELD[$']" }] }));
  const report = { title: 'Literal token report', scope: 'SELECTION', activeTime: { label: '2026' }, selection: providerSelection,
    mapContext: { terrain: { heightOverlay: { enabled: false, lockedReading: null } } }, summary: null, records: [], findings: [], limitations: [], attribution: [],
    temporalComparison: { timeA: 2025, timeB: 2026, timeARecordCount: 0, timeBRecordCount: 0, recordDelta: 0, changedLayerCount: 0 } };
  const escapeReportHtml = execute('escapeReportHtml');
  execute('downloadCustomReport', {
    buildCustomReportPayload: () => report, setReportGeneratedAt() {}, reportRecords: [], escapeReportHtml,
    providerReportHtml: execute('providerReportHtml', { escapeReportHtml }), formatTimelineStep: String,
    Blob, URL: { createObjectURL(blob) { blobs.push(blob); return 'blob:synthetic'; }, revokeObjectURL() {} },
    document: { createElement: () => ({ click() {}, remove() {} }), body: { append() {} } }, window: { setTimeout() {} }, announce() {},
  })('html');
  const html = await blobs[0].text();
  for (const literal of ['TITLE[$&amp;]', 'SUMMARY[$`]', 'FIELD[$&#039;]']) assert.equal(html.split(literal).length - 1, 1, `${literal} survives exactly once`);
  for (const fragment of ['<!doctype html>', '<body>', '</header>', '</body>']) assert.equal(html.split(fragment).length - 1, 1, `${fragment} is not duplicated`);
});
