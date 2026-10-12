import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";
const source = await readFile("app/water-path-analysis.ts", "utf8");
const js = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const water = await import(`data:text/javascript;base64,${Buffer.from(js).toString("base64")}`);
const reach = (id, sequence, downstream, coordinates) => ({ id, sequence, downstream, coordinates, levelpath: 1, name: "Test river" });
const a = reach("A", 30, 20, [[-98, 38], [-97.99, 38]]);
const b = reach("B", 20, 10, [[-97.99, 38], [-97.98, 38]]);
const c = reach("C", 10, null, [[-97.98, 38], [-97.97, 38]]);

test("route snaps to the gauge vicinity and follows network identifiers, not nearby unrelated rivers", () => {
  const unrelated = reach("X", 99, null, [[-97.99, 38], [-97.99, 38.01]]);
  const seed = water.nearestWaterReach([a, b], [-97.995, 38.0001]);
  const route = water.traceWaterPath(seed, [unrelated, c, a, b]);
  assert.equal(route.segments, 3); assert.equal(route.path.coordinates[0][0], -97.995);
  assert.deepEqual(route.path.coordinates.at(-1), [-97.97, 38]);
  assert.ok(route.lengthM > 2000 && route.lengthM < 2300); assert.ok(route.gaugeOffsetM < 12);
  assert.equal(water.nearestWaterReach([a], [-99, 39]), null);
});

test("gaps, ambiguous network identities and cycles stop instead of inventing connections", () => {
  const seed = water.nearestWaterReach([a], [-97.995, 38]);
  assert.match(water.traceWaterPath(seed, [a, { ...b, coordinates: [[-97.9, 38], [-97.8, 38]] }]).stopReason, /gap/);
  assert.match(water.traceWaterPath(seed, [a, b, { ...b, id: "D" }]).stopReason, /Ambiguous/);
  assert.match(water.traceWaterPath(seed, [a, { ...b, downstream: 30 }]).stopReason, /Repeated/);
  assert.equal(water.traceWaterPath(seed, [a]).segments, 1);
});

test("long river geometries survive the former 300-vertex cutoff and remain bounded", () => {
  const coordinates = Array.from({ length: 1000 }, (_, i) => [-98 + i / 2000, 38]);
  const parsed = water.parseWaterReaches({ features: [{ properties: { id3dhp: "A", flowdirection: 1, featuretype: 1, hydrosequence: 30 }, geometry: { type: "LineString", coordinates } }] });
  assert.equal(parsed[0].coordinates.length, 1000);
  const route = water.traceWaterPath(water.nearestWaterReach(parsed, [-98, 38]), parsed);
  assert.equal(route.lengthM, 40000); assert.match(route.stopReason, /40 km/);
  assert.ok(route.path.coordinates.at(-1)[0] < coordinates.at(-1)[0]);
  assert.throws(() => water.parseWaterReaches({ features: Array(401).fill({}) }));
});

test("terrain samples use along-path distance and require matched endpoint datums for slope", () => {
  const samples = water.sampleWaterPath([[-98, 38], [-97.99, 38], [-97.99, 37.99]]);
  assert.equal(samples.length, 25); assert.deepEqual(samples[0].coordinate, [-98, 38]);
  assert.deepEqual(samples.at(-1).coordinate, [-97.99, 37.99]);
  const payload = { samples: samples.map((s, index) => ({ locationId: index, location: { x: s.coordinate[0], y: s.coordinate[1], spatialReference: { wkid: 4326 } }, value: String(500 - index), resolution: 1, attributes: { VerticalDatum: "NAVD88" } })) };
  const result = water.parseWaterElevations(payload, samples);
  assert.equal(result.state, "ready"); assert.equal(result.dropM, 24);
  assert.equal(result.slopePercent, 24 / samples.at(-1).distanceM * 100);
  payload.samples[12].value = "NoData";
  assert.equal(water.parseWaterElevations(payload, samples).state, "partial");
  payload.samples.at(-1).attributes.VerticalDatum = "unknown";
  assert.equal(water.parseWaterElevations(payload, samples).dropM, null);
  payload.samples[0].value = null;
  assert.equal(water.parseWaterElevations(payload, samples).samples[0].elevationM, null);
  payload.samples[0].location.x = -97;
  assert.throws(() => water.parseWaterElevations(payload, samples), /location/);
});


test("corridor extends before and after gauge while all arrows retain downstream order", () => {
  const seed=water.nearestWaterReach([b],[-97.985,38]);
  const corridor=water.traceWaterCorridor(seed,[a,b,c]);
  assert.deepEqual(corridor.path.coordinates[0],a.coordinates[0]);
  assert.deepEqual(corridor.path.coordinates.at(-1),c.coordinates.at(-1));
  assert.ok(corridor.upstreamM>1000 && corridor.downstreamM>1000);
  assert.equal(corridor.lengthM,corridor.upstreamM+corridor.downstreamM);
  assert.equal(corridor.segments,3);
  assert.ok(corridor.path.coordinates.every((p,i,all)=>i===0||p[0]>=all[i-1][0]));
});
test("upstream mainstem requires reciprocal topology and never guesses a tributary", () => {
  const tributary={...a,id:"D",sequence:40,coordinates:[[-97.99,38.01],[-97.99,38]]};
  const seed=water.nearestWaterReach([b],[-97.985,38]);
  const ambiguous=water.traceWaterCorridor(seed,[a,tributary,b,c]);
  assert.deepEqual(ambiguous.path.coordinates[0],b.coordinates[0]);
  assert.match(ambiguous.upstreamStop,/ambiguous/);
  const explicit={...b,upstream:30};
  assert.deepEqual(water.traceWaterCorridor({...seed,reach:explicit},[a,tributary,explicit,c]).path.coordinates[0],a.coordinates[0]);
  const wrong={...b,upstream:999};
  assert.deepEqual(water.traceWaterCorridor({...seed,reach:wrong},[a,wrong,c]).path.coordinates[0],b.coordinates[0]);
});
test("long corridors stop at 100 km each way and preserve mapped geometry", () => {
  const river=reach("LONG",1,null,[[-100,38],[-98,38],[-96,38]]);
  const corridor=water.traceWaterCorridor(water.nearestWaterReach([river],[-98,38]),[river]);
  assert.equal(corridor.upstreamM,100000);assert.equal(corridor.downstreamM,100000);
  assert.equal(corridor.lengthM,200000);
  assert.ok(corridor.path.coordinates.every(p=>p[1]===38));
});
