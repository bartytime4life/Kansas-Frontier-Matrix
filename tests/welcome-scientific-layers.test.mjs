import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';

async function compile(path, modules = {}) {
  const exports = {};
  new Function('exports', 'require', ts.transpileModule(await readFile(path, 'utf8'), {
    compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 },
  }).outputText)(exports, id => { if (id in modules) return modules[id]; throw new Error(`Unexpected module ${id}`); });
  return exports;
}
const land = await compile('app/land-cover.ts'), crops = await compile('app/cropland.ts');
let solarResult = true;
const solarCalls = [];
const { createWelcomeScientificLayers, ANIMAL_RECORDS_SOURCE_ID, ANIMAL_RECORDS_TILE_URL } = await compile('app/living-welcome/scientific-layers.ts', {
  '../land-cover': land, '../cropland': crops,
  '../map-runtime': { setDaylightMapLayer: (_map, on, instant) => { solarCalls.push({ on, instant }); return solarResult; } },
});
const plain = value => JSON.parse(JSON.stringify(value));
function setup() {
  const sources = new Map(), layers = new Map(), events = new Map();
  let changes = 0;
  const map = {
    on: (name, callback) => events.set(name, callback), off: name => events.delete(name),
    getSource: id => sources.get(id), addSource: (id, source) => sources.set(id, source), removeSource: id => sources.delete(id),
    getLayer: id => layers.get(id), addLayer: layer => layers.set(layer.id, layer), removeLayer: id => layers.delete(id),
    getStyle: () => ({ layers: [...layers.values()] }),
    setLayoutProperty: (id, key, value) => {const layer=layers.get(id); layer.layout={...layer.layout,[key]:value};},
  };
  const preview = createWelcomeScientificLayers(map, () => changes++);
  return { preview, sources, layers, events, changes: () => changes };
}

test('preview renderers use the existing classified rasters, keep editions and clean up on selection or comparison', () => {
  const { preview, sources, layers } = setup();
  assert.equal(sources.size, 0, 'no startup data requests');
  preview.sync(['land-cover'], true);
  assert.deepEqual(plain(sources.get(land.LAND_COVER_SOURCE_ID).tiles), [land.LAND_COVER_TILE_URL]);
  assert.equal(layers.get(land.LAND_COVER_LAYER_ID).paint['raster-resampling'], 'nearest');
  assert.match(preview.status()[0].label, /NLCD 2021.*30 m/);
  assert.equal(preview.status()[0].state, 'loading', 'installation does not claim successful provider tiles');
  preview.sync(['cropland'], true);
  assert.equal(sources.has(land.LAND_COVER_SOURCE_ID), false, 'land cover cannot linger over crop classes');
  assert.deepEqual(plain(sources.get(crops.CDL_SOURCE_ID).tiles), [crops.cdlTileTemplate(crops.CDL_LATEST_YEAR)]);
  assert.equal(layers.get(crops.CDL_LAYER_ID).minzoom, crops.CDL_MIN_ZOOM, 'the field-scale camera meets the renderer minimum');
  assert.match(preview.status()[0].label, new RegExp(`CDL ${crops.CDL_LATEST_YEAR}.*30 m`));
  preview.sync(['cropland'], false);
  assert.equal(sources.size, 0); assert.equal(layers.size, 0);
  assert.equal(preview.status()[0].state, 'hidden');
  preview.sync([], true);
  assert.deepEqual(plain(preview.status()), []);
});

test('tile readiness, errors, style replacement and late events retain truthful layer status', () => {
  const { preview, sources, layers, events, changes } = setup();
  preview.sync(['land-cover'], true);
  events.get('sourcedata')({ sourceId: land.LAND_COVER_SOURCE_ID, sourceDataType: 'metadata', isSourceLoaded: true });
  assert.equal(preview.status()[0].state, 'loading', 'metadata alone is not a rendered classification');
  events.get('sourcedata')({ sourceId: land.LAND_COVER_SOURCE_ID, sourceDataType: 'content', isSourceLoaded: false });
  assert.equal(preview.status()[0].state, 'loading', 'one content tile is not the complete view');
  events.get('sourcedata')({ sourceId: land.LAND_COVER_SOURCE_ID, sourceDataType: 'idle', isSourceLoaded: true });
  assert.equal(preview.status()[0].state, 'map-layer'); assert.equal(changes(), 1);
  events.get('error')({ sourceId: land.LAND_COVER_SOURCE_ID, error: new Error('private provider detail') });
  assert.equal(preview.status()[0].state, 'unavailable');
  events.get('sourcedata')({ sourceId: land.LAND_COVER_SOURCE_ID, sourceDataType: 'content', isSourceLoaded: true });
  assert.equal(preview.status()[0].state, 'unavailable', 'other successful tiles cannot mask a failed tile');
  assert.doesNotMatch(JSON.stringify(preview.status()), /private provider/);
  sources.clear(); layers.clear(); preview.sync(['land-cover'], true);
  assert.equal(preview.status()[0].state, 'loading', 'a fresh style retries its new source');
  preview.sync(['cropland'], true);
  const before = changes();
  events.get('error')({ sourceId: land.LAND_COVER_SOURCE_ID });
  assert.equal(changes(), before, 'a retired source cannot affect the selected category');
  preview.dispose(); assert.equal(events.size, 0, 'no listeners after the welcome closes');
});

test('the Sky preview calculates the actual current instant and comparison hides it', () => {
  const { preview } = setup();
  solarResult = true;
  const before = Date.now(); preview.sync(['daylight'], true);
  const state = preview.status()[0], instant = Date.parse(state.observedAt);
  assert.ok(instant >= before && instant <= Date.now());
  assert.equal(state.product, 'calculated'); assert.equal(state.state, 'calculated');
  assert.equal(solarCalls.at(-1).on, true); assert.equal(solarCalls.at(-1).instant, instant);
  solarResult = false; preview.sync(['daylight'], true);
  assert.equal(preview.status()[0].state, 'unavailable', 'a failed shader/fallback is disclosed');
  preview.sync(['daylight'], false);
  assert.equal(solarCalls.at(-1).on, false); assert.equal(preview.status()[0].state, 'hidden');
  preview.sync([], true); assert.equal(solarCalls.at(-1).on, false);
  solarResult = true;
});


test('animal records retain the exact annual coarse carrier, disclose failure and never linger on another topic', () => {
  const { preview, sources, layers, events } = setup();
  preview.sync(['animal-records'], true);
  const source=sources.get(ANIMAL_RECORDS_SOURCE_ID);
  assert.deepEqual(plain(source.tiles), [ANIMAL_RECORDS_TILE_URL]);
  assert.match(source.tiles[0], /kind=fauna&date=2025-01-01/);
  assert.equal(source.maxzoom,6,'no exact occurrence sites or fine source tiles');
  assert.match(preview.status()[0].label,/GBIF Animalia.*2025/);
  assert.equal(preview.status()[0].state,'loading');
  events.get('sourcedata')({sourceId:ANIMAL_RECORDS_SOURCE_ID,sourceDataType:'content',isSourceLoaded:true});
  assert.equal(preview.status()[0].state,'map-layer');
  assert.equal(preview.status()[0].product,'occurrence-records');
  events.get('error')({sourceId:ANIMAL_RECORDS_SOURCE_ID,error:new Error('outage')});
  assert.equal(preview.status()[0].state,'unavailable');
  assert.equal(layers.get(ANIMAL_RECORDS_SOURCE_ID).layout.visibility,'none','partial aggregate pixels cannot imply complete coverage');
  preview.sync(['animal-records'],true);
  assert.equal(layers.get(ANIMAL_RECORDS_SOURCE_ID).layout.visibility,'none','redraw cannot silently mask failure');
  preview.sync(['animal-records'],false);
  assert.equal(preview.status()[0].state,'hidden');assert.equal(sources.size,0);
  preview.sync(['animal-records'],true);
  assert.equal(preview.status()[0].state,'loading','deliberate restore retries a new source');
  preview.sync(['land-cover'],true);
  assert.equal(sources.has(ANIMAL_RECORDS_SOURCE_ID),false);
  assert.equal(layers.has(ANIMAL_RECORDS_SOURCE_ID),false);
  events.get('error')({sourceId:ANIMAL_RECORDS_SOURCE_ID});
  assert.equal(preview.status()[0].state,'loading','a late animal tile cannot affect vegetation');
});
