import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
import { componentHarness, findNode, settle } from './component-harness.mjs';

async function compile(name, dependencies = {}) {
  const code = ts.transpileModule(await readFile(`app/${name}.ts`, 'utf8'), { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText;
  const module = { exports: {} };
  new Function('require', 'module', 'exports', code)(id => dependencies[id], module, module.exports);
  return module.exports;
}
const smoke = await compile('hms-smoke-playback', { './bounded-json': await compile('bounded-json') });
const page = await readFile('app/page.tsx', 'utf8');
const section = (start, end) => {
  const at = page.indexOf(`  const ${start} =`);
  return at < 0 ? '' : page.slice(at, page.indexOf(`  const ${end} =`, at));
};
const callbacks = ts.transpileModule([
  section('cancelSmokePlayback', 'layerJsonReadsRef'),
  section('commitTemporalFrame', 'stepTemporalSweep'),
  section('refreshOfficialContext', 'loadOfficialArchiveDay'),
  section('returnOfficialSourceToCurrent', 'seekCalendarFrame'),
].join('\n'), { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText;
const feed = 'noaa-hms-smoke', day = '2026-10-01';
const frame = (dated, id = dated ? 'archive' : 'current') => ({
  feed, state: 'ready', featureCount: 1, retrievedAt: dated ? '2026-10-02T12:00:00Z' : '2026-10-21T12:00:00Z',
  source: 'SYNTHETIC TEST ONLY', limitation: 'No evidence admission', upstreamUpdatedAt: null,
  smokeCoverage: { day: dated ? day : null, availableDays: [day], missingDays: [] },
  data: { type: 'FeatureCollection', features: [{ type: 'Feature', id }] },
});
const deferred = () => { let resolve; const promise = new Promise(r => { resolve = r; }); return { promise, resolve }; };
async function harness({ search = false, upload = false } = {}) {
  const ref = current => ({ current }), state = {}, writes = [], fetched = deferred(), response = deferred(), uploading = deferred(), uploaded = deferred();
  const transitions = new smoke.HmsFrameTransitions(), source = { type: 'geojson' }, current = frame(false), prior = frame(true, 'prior');
  const context = {
    useCallback: fn => fn, announce() {}, temporalMode: 'snapshot', OFFICIAL_CONTEXT_PRESENT_FRAME: 2026,
    CALENDAR_ARCHIVE_BOUNDS: { [feed]: '2005-08-05' }, OFFICIAL_CONTEXT_BY_ID: { [feed]: { apiPath: '/current', sourceId: 'smoke', shortTitle: 'HMS' } },
    calendarSeekGeneration: ref(0), calendarSweepRef: ref(search ? null : { day }), calendarArchiveLoads: ref(new Map()),
    officialArchiveDaysRef: ref(search ? {} : { [feed]: day }), officialArchivePayloadsRef: ref(search ? {} : { [feed]: prior }),
    officialPayloadsRef: ref({ [feed]: search ? current : prior, unrelated: { id: 'retained' } }),
    officialRequestsRef: ref(new Map()), officialVisibilityRef: ref({ [feed]: true }), officialOpacityRef: ref({ [feed]: .38 }),
    selectedRef: ref(search ? { id: 'unrelated-place' } : { feed }), officialContextIdForSelection: value => value?.feed ?? null,
    yearRef: ref(2026), buildYearCurrentRef: ref(true), temporalQueryRef: ref({ frame: 2026 }),
    mapRef: ref({ getSource: () => source }), styleGenerationReadyRef: ref(true),
    noaaRadarReadyRef: ref(false), noaaRadarFrameTimeRef: ref(null), smokeTransitionsRef: ref(transitions),
    runMapMutation: (_label, fn) => fn(), clearOfficialContextFeed: () => writes.push(undefined), updateSelectionSource() {},
    runtimeOfficialVisibility: v => v, applyOfficialContextState: (_map, _visibility, _opacity, values) => writes.push(values[feed]),
    resetHmsSmokeFade() {}, setHmsSmokeFade() {}, geoJSONHasData: () => true,
    hmsFade: async (_from, to, signal, paint) => { signal.throwIfAborted(); paint(to); },
    waitForGeoJSON: async (_source, signal) => { if (upload && signal) { uploading.resolve(); await uploaded.promise; } },
    validLayerPayload: () => true, layerJsonReadsRef: ref({ read: async () => ({ response: { ok: true }, body: current }) }),
  };
  for (const key of ['SmokePlaybackSignal', 'CalendarSweep', 'SweepRangeStart', 'SweepRangeEnd', 'Year', 'PreviewYear', 'CompareTimeB', 'OfficialArchiveDays', 'OfficialPayloads', 'OfficialStates', 'OfficialErrors', 'OfficialReadPhases', 'EarthquakeArchiveFrameIndex', 'SmokeArchiveFrameIndex', 'Selected', 'RightOpen'])
    context['set' + key] = value => { state[key] = typeof value === 'function' ? value(state[key] ?? {}) : value; };
  const parent = new Function(...Object.keys(context), callbacks + '\nreturn { commitTemporalFrame, reserveSmokePlayback, commitSmokePlayback, refreshOfficialContext, returnOfficialSourceToCurrent };')(...Object.values(context));
  const cache = new smoke.HmsFrameCache(async url => { fetched.resolve(); await response.promise; const value = frame(true); const requested = new URL(url, 'http://localhost').searchParams.get('day'); value.smokeCoverage.day = requested; value.smokeCoverage.availableDays = [requested]; return Response.json(value); });
  const h = await componentHarness(new URL('../app/hms-smoke-playback-control.tsx', import.meta.url), {
    './hms-smoke-playback': { ...smoke, hmsToday: () => '2026-10-21', HmsFrameCache: class { get(...args) { return cache.get(...args); } } },
  }, { setInterval: () => 1, clearInterval() {}, document: { hidden: false, addEventListener() {}, removeEventListener() {} } });
  const props = { enabled: true, reducedMotion: false, sessionSignal: transitions.signal ?? new AbortController().signal,
    onReserve: parent.reserveSmokePlayback, onFrame: parent.commitSmokePlayback, onCurrent: () => parent.returnOfficialSourceToCurrent(feed) };
  const render = () => { const tree = h.render(h.exports.HmsSmokePlayback, props); h.commit(); return tree; };
  let tree = render();
  findNode(tree, n => n.props?.['aria-label'] === 'HMS playback day').props.onChange({ target: { value: day } }); tree = render();
  const start = () => findNode(tree, n => n.type === 'button' && n.props.children === (search ? 'Find smoke in the last 7 days' : 'Check / retry day')).props.onClick();
  return { h, parent, context, state, writes, current, prior, fetched, response, uploading, uploaded, start, render, props, transitions };
}
for (const exit of ['Present', 'annual', 'current']) test(`held HMS request cannot restore history after ${exit}`, async t => {
  const r = await harness(); t.after(() => r.h.dispose());
  r.start(); await r.fetched.promise;
  assert.equal(r.context.officialArchiveDaysRef.current[feed], day);
  if (exit === 'current') r.parent.returnOfficialSourceToCurrent(feed);
  else r.parent.commitTemporalFrame(exit === 'annual' ? 2024 : 2026);
  if (exit !== 'annual') await r.parent.refreshOfficialContext(feed);
  const expected = r.context.officialPayloadsRef.current[feed];
  r.response.resolve(); await new Promise(resolve => setImmediate(resolve)); await settle();
  assert.equal(r.context.officialArchiveDaysRef.current[feed], undefined);
  assert.equal(r.context.officialArchivePayloadsRef.current[feed], undefined);
  assert.equal(r.context.officialPayloadsRef.current[feed], expected, 'late archive must not replace current hydration or a held annual frame');
  if (exit !== 'annual') assert.equal(expected, r.current);
  assert.equal(r.context.officialPayloadsRef.current.unrelated.id, 'retained');
  assert.equal(r.context.officialVisibilityRef.current[feed], true);
});
test('Present invalidates a pending recent-smoke search before it reserves any date', async t => {
  const r = await harness({ search: true }); t.after(() => r.h.dispose());
  r.start(); await r.fetched.promise; r.parent.commitTemporalFrame(2026);
  r.response.resolve(); await new Promise(resolve => setImmediate(resolve)); await settle();
  assert.equal(r.context.officialArchiveDaysRef.current[feed], undefined);
  assert.equal(r.context.officialPayloadsRef.current[feed], r.current);
  assert.equal(r.context.selectedRef.current.id, 'unrelated-place');
});
test('Present during an HMS map upload cannot restore a prior archive over current hydration', async t => {
  const r = await harness({ upload: true }); t.after(() => r.h.dispose());
  r.start(); await r.fetched.promise; r.response.resolve(); await r.uploading.promise;
  r.parent.commitTemporalFrame(2026); await r.parent.refreshOfficialContext(feed);
  r.uploaded.resolve(); await new Promise(resolve => setImmediate(resolve)); await settle();
  assert.equal(r.context.officialArchiveDaysRef.current[feed], undefined);
  assert.equal(r.context.officialArchivePayloadsRef.current[feed], undefined);
  assert.equal(r.context.officialPayloadsRef.current[feed], r.current);
  assert.equal(r.state.OfficialArchiveDays[feed], undefined);
  assert.equal(r.state.OfficialStates[feed], 'ready');
});
