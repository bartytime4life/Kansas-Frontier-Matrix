import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/science-events.ts", import.meta.url), "utf8");
const javascript = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const science = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);

test("science registry represents the requested phenomena with clocks, methods, measurements and source paths", () => {
  const required = ["tornadoes", "floods", "history", "erosion", "elevation", "cities", "roads", "trade-routes", "snow", "ice", "foliage", "fauna", "smoke", "water-levels", "earthquakes"];
  const ids = science.SCIENCE_EVENTS.map((event) => event.id);
  assert.equal(new Set(ids).size, ids.length);
  for (const id of required) assert.ok(ids.includes(id), `${id} is represented`);
  assert.ok(science.SCIENCE_EVENTS.length >= 18);
  const tracks = new Set(["radar", "smoke", "river", "geology", "flora", "fauna", "resources", "counties", "weather", "earthquakes", "shake"]);
  for (const event of science.SCIENCE_EVENTS) {
    assert.ok(event.clock.length > 10, `${event.id} has a time rule`);
    assert.ok(event.representation.length > 20, `${event.id} has a visual method`);
    assert.ok(event.measurement.length > 8, `${event.id} has a scientific measure`);
    assert.ok(event.limitation.length > 20, `${event.id} has a limitation`);
    assert.match(event.sourceUrl, /^https:\/\//);
    assert.ok(science.SCIENCE_SUPPORT_LABELS[event.support]);
    if (event.trackId) assert.ok(tracks.has(event.trackId), `${event.id} points to a real Observatory lane`);
  }
  assert.ok(science.SCIENCE_EVENTS.some((event) => event.support === "connected"));
  assert.ok(science.SCIENCE_EVENTS.some((event) => event.support === "download"));
  assert.ok(science.SCIENCE_EVENTS.some((event) => event.support === "derived"));
  assert.ok(science.SCIENCE_EVENTS.some((event) => event.support === "steward"));
});

test("two-point science probe returns a geodesic distance, bearing and honest map geometry", () => {
  const points = [[-98.5, 38.5], [-97.5, 38.5]];
  const measurement = science.scienceMeasurement(points);
  assert.ok(measurement.miles > 53 && measurement.miles < 55);
  assert.ok(measurement.kilometers > 85 && measurement.kilometers < 89);
  assert.ok(measurement.bearing > 89 && measurement.bearing < 91);
  assert.equal(science.scienceMeasurement(points.slice(0, 1)), null);
  const geojson = science.scienceProbeGeoJSON(points);
  assert.equal(geojson.type, "FeatureCollection");
  assert.equal(geojson.features.length, 3);
  assert.equal(geojson.features[0].geometry.type, "LineString");
  assert.deepEqual(geojson.features[0].geometry.coordinates, points);
  assert.deepEqual(geojson.features.slice(1).map((feature) => feature.properties.kind), ["vertex", "vertex"]);
});

test("Observatory exposes the responsive Science Lab, real tools and archive notices", async () => {
  const [workspace, css, toolbar, sources, intake] = await Promise.all([
    readFile(new URL("../app/observatory/workspace.tsx", import.meta.url), "utf8"),
    readFile(new URL("../app/globals.css", import.meta.url), "utf8"),
    readFile(new URL("../app/map-toolbar.tsx", import.meta.url), "utf8"),
    readFile(new URL("../app/observatory/sources/page.tsx", import.meta.url), "utf8"),
    readFile(new URL("../app/data-intake.ts", import.meta.url), "utf8"),
  ]);
  assert.match(workspace, /Science lab · \{SCIENCE_EVENTS\.length\}/);
  assert.match(workspace, /DISTANCE \/ BEARING/);
  assert.match(workspace, /Catalog origin-time ticks/);
  assert.match(workspace, /daily \/ annual \/ edition context/);
  assert.match(workspace, /scene=elevation-3d&mapui=open&maptab=scene/);
  assert.match(workspace, /Download-only, unqueried and unsupported time remain gaps/);
  assert.match(css, /\.event-science-lab \{/);
  assert.match(css, /\.event-science-probe-readout \{/);
  assert.match(css, /@media \(max-width: 760px\) \{[\s\S]*\.event-science-lab \{ top: 0/);
  assert.match(toolbar, /noaa-storm-events/);
  assert.match(toolbar, /Tornado, flood, snow & ice history/);
  assert.match(toolbar, /Historical map editions \/ shapefiles|Map editions \/ shapefiles/);
  assert.match(sources, /Science event visual grammar/);
  assert.match(intake, /SCIENCE_EVENTS\.map/);
});
