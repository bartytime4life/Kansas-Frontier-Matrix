// Execute the production callbacks together, retaining their shared runtime-error
// closure. This deliberately does not reimplement the fallback or idle logic.
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';

const page = await readFile(process.env.KFM_PAGE_PATH ?? 'app/page.tsx', 'utf8');
const ast = ts.createSourceFile('page.tsx', page, ts.ScriptTarget.ES2022, true, ts.ScriptKind.TSX);
const callbacks = {}, declarations = {};
let detailEffect, fallbackEffect;
function visit(node) {
  if (ts.isVariableDeclaration(node) && ['chooseTerrainProvider', 'chooseTerrainProviderByHand', 'wantsTerrainDetail'].includes(node.name.getText(ast))) {
    declarations[node.name.getText(ast)] = `const ${node.getText(ast)};`;
  }
  if (ts.isCallExpression(node) && node.expression.getText(ast) === 'map.on' && ['error', 'sourcedata', 'idle'].includes(node.arguments[0]?.text)) {
    const body = node.arguments[1].getText(ast);
    if (body.includes('runtimeError') || body.includes('failedTerrainSourceRef')) callbacks[node.arguments[0].text] = body;
  }
  if (ts.isCallExpression(node) && node.expression.getText(ast) === 'useEffect') {
    const body = node.arguments[0]?.getText(ast) ?? '';
    if (body.includes('if (!wantsTerrainDetail')) detailEffect = body;
    if (body.includes('terrainDetailFallbackRef.current =')) fallbackEffect = body;
  }
  ts.forEachChild(node, visit);
}
visit(ast);
assert.ok(detailEffect && fallbackEffect && Object.keys(callbacks).length === 3);
const compile = source => ts.transpileModule(source, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText;

export function terrainHarness() {
  const h = { provider: 'mapzen', terrain: 'LOADING', runtime: { kind: 'loading' }, probe: {}, announcements: [], sources: new Map(), loaded: false, timers: new Map(), view: { center: [-98, 38.5], zoom: 10 }, scene: 'elevation-3d' };
  const ref = current => ({ current });
  const templates = { mapzen: 'https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png', 'usgs-3dep': '/api/3dep-dem-tile?v=2&z={z}&x={x}&y={y}' };
  const sourceFor = provider => ({ tileTemplate: templates[provider] });
  const terrainId = 'kfm-terrain-dem';
  const map = {
    getSource: id => h.sources.get(id), isSourceLoaded: () => h.loaded,
    getTerrain: () => ({ source: terrainId }),
    getLayer: () => undefined, refreshTiles: () => {},
  };
  const set = field => value => { h[field] = typeof value === 'function' ? value(h[field]) : value; };
  const scope = {
    map, mapRef: ref(map), terrainProviderRef: ref(h.provider), attachedTerrainProviderRef: ref(h.provider),
    terrainDetailRef: ref({ auto: false, failed: false, byHand: false }), terrainDetailFallbackRef: ref(null),
    failedTerrainSourceRef: ref(null), scenePresetRef: ref(h.scene), mapMutationErrorRef: ref(null),
    TERRAIN_SOURCE_ID: terrainId, TERRAIN_HILLSHADE_SOURCE_ID: 'kfm-terrain-hillshade-dem', TERRAIN_COLOR_SOURCE_ID: 'kfm-terrain-color-dem',
    terrainSourceFor: sourceFor, terrainPresentationSourceMatches: (_map, source) => h.sources.get(terrainId)?.serialize().tiles[0] === source.tileTemplate,
    setTerrainState: set('terrain'), setTerrainProvider: set('provider'), setRuntime: set('runtime'), setMaplibreProbe: set('probe'),
    setTerrainElevationReading: () => {}, setTerrainElevationUnavailable: () => {},
    announce: value => h.announcements.push(value), controlOwnsMapSourceErrors: () => false,
    mapRuntimeErrorCode: (_kind, id) => `MAP_SOURCE_ERROR:${id ?? 'runtime'}`, LAYER_REGISTRY: [{ id: 'catalog', sourceId: 'catalog-source' }],
    officialContextForMapSource: () => undefined, VECTOR_BASEMAPS: new Set(), basemapRef: ref('local'), BASEMAPS: { local: { style: { sources: {} } } },
    OFFICIAL_CONTEXT_BY_SOURCE_ID: {}, rasterRetryTimers: new Map(),
    syncTerrainRasterView: () => {}, runMapMutation: (_label, fn) => fn(), sameValues: (a, b) => JSON.stringify(a) === JSON.stringify(b),
    refreshMaplibreProbe: () => ({ styleLoaded: true, canvasReady: true, tilesLoaded: true, sourcesReady: 1, interactionsReady: true, failedChecks: [] }),
    setSourceStates: () => {}, version: '6.9.0', disposed: false, styleGenerationReadyRef: ref(true), document: { hidden: false },
    window: { setTimeout: (fn, delay) => { const id = ++h.nextTimer; h.timers.set(id, { fn, delay }); return id; }, clearTimeout: id => h.timers.delete(id) },
    TERRARIUM_RENDER_MAX_ZOOM: 11,
  };
  h.nextTimer = 0;
  const code = compile(`
    let runtimeError = null, degradedReason = null, styleFallbackAttempted = false, terrainRetryTimer = null, terrainRetryCount = 0;
    const failedSourceIds = new Set();
    ${declarations.chooseTerrainProvider}
    ${declarations.chooseTerrainProviderByHand}
    (${fallbackEffect})();
    return {
      error: ${callbacks.error}, sourceData: ${callbacks.sourcedata}, idle: ${callbacks.idle},
      manual: chooseTerrainProviderByHand,
      settled(scenePreset, terrainProvider, view) { ${declarations.wantsTerrainDetail} return (${detailEffect})(); },
      errors: () => ({ runtimeError, degradedReason, failedSourceIds: [...failedSourceIds] }),
    };
  `);
  Object.assign(h, new Function('scope', `with (scope) { ${code} }`)(scope));
  h.scope = scope;
  h.attach = (provider = h.provider) => {
    const source = { serialize: () => ({ type: 'raster-dem', tiles: [templates[provider]] }) };
    h.sources.set(terrainId, source); scope.attachedTerrainProviderRef.current = provider; h.loaded = false;
    return source.serialize();
  };
  h.flushSwitch = () => { for (const [id, timer] of h.timers) if (timer.delay === 0) { h.timers.delete(id); timer.fn(); } };
  h.settle = () => h.settled(h.scene, h.provider, h.view);
  h.complete = () => { h.loaded = true; h.sourceData({ sourceId: terrainId, isSourceLoaded: true }); h.idle(); };
  h.fail = (source = h.sources.get(terrainId)?.serialize(), sourceId = terrainId) => h.error({ sourceId, source });
  h.attach();
  return h;
}
