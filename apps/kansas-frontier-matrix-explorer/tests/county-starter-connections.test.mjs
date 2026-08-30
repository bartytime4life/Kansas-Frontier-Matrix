import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const readJson = async (relativeUrl) => JSON.parse(await readFile(new URL(relativeUrl, import.meta.url), "utf8"));
const readText = async (relativeUrl) => readFile(new URL(relativeUrl, import.meta.url), "utf8");

test("county starter fixture covers all 105 Kansas counties exactly once", async () => {
  const fixture = await readJson("../app/county-starter-points.json");
  const counties = fixture.counties;

  assert.equal(fixture.schemaVersion, "kfm.county-starter-points.v1");
  assert.equal(fixture.source.publisher, "U.S. Census Bureau");
  assert.equal(fixture.source.year, 2025);
  assert.equal(counties.length, 105);

  const geoids = new Set(counties.map((county) => county.geoid));
  const names = new Set(counties.map((county) => county.name));
  const coordinates = new Set(counties.map((county) => `${county.longitude},${county.latitude}`));

  assert.equal(geoids.size, 105, "every county must have a unique Census GEOID");
  assert.equal(names.size, 105, "every county must have a unique name");
  assert.equal(coordinates.size, 105, "every county must have a unique representative point");

  for (const county of counties) {
    assert.match(county.geoid, /^20\d{3}$/);
    assert.match(county.name, / County$/);
    assert.ok(county.latitude >= 36.99 && county.latitude <= 40.01, `${county.name} latitude is outside the Kansas frame`);
    assert.ok(county.longitude >= -102.06 && county.longitude <= -94.75, `${county.name} longitude is outside the Kansas frame`);
  }

  assert.deepEqual(
    counties.find((county) => county.geoid === "20053"),
    { geoid: "20053", name: "Ellsworth County", latitude: 38.700845, longitude: -98.205355 },
  );
  assert.equal(counties.at(0).name, "Allen County");
  assert.equal(counties.at(-1).name, "Wyandotte County");
});

test("MapLibre plugin candidates are explicit, unique, and fail closed", async () => {
  const registry = await readJson("../app/maplibre-plugin-connections.json");
  const connections = registry.connections;
  const allowedStatuses = new Set(["READY_FOR_ADAPTER", "HOLD", "DEVELOPMENT_ONLY"]);

  assert.equal(registry.schemaVersion, "kfm.maplibre-plugin-connections.v1");
  assert.equal(registry.source.publisher, "MapLibre");
  assert.equal(connections.length, 9);
  assert.equal(new Set(connections.map((connection) => connection.id)).size, connections.length);

  for (const connection of connections) {
    assert.ok(allowedStatuses.has(connection.status), `${connection.id} has an unsupported status`);
    for (const field of ["title", "project", "connectionClass", "reason", "connection", "gate", "fallback"]) {
      assert.ok(typeof connection[field] === "string" && connection[field].trim().length > 0, `${connection.id}.${field} must be populated`);
    }
  }

  const byId = new Map(connections.map((connection) => [connection.id, connection]));
  assert.equal(byId.get("local-geocoder").status, "READY_FOR_ADAPTER");
  assert.equal(byId.get("pmtiles-protocol").status, "HOLD");
  assert.equal(byId.get("inspect-control").status, "DEVELOPMENT_ONLY");
});

test("county coverage and plugin candidates are wired into the existing Explorer registries", async () => {
  const [mapInterface, countyLayer, packageJson] = await Promise.all([
    readText("../app/map-interface.ts"),
    readText("../app/county-starter-slice.ts"),
    readJson("../package.json"),
  ]);

  assert.match(mapInterface, /registerCountyStarterSlice\(\);/);
  assert.match(mapInterface, /SEARCH_INDEX\.push\(\.\.\.countyStarterSearchItems\)/);
  assert.match(mapInterface, /MAPLIBRE_PLUGIN_CONNECTIONS\.map/);
  assert.match(mapInterface, /105 \/ 105/);
  assert.match(countyLayer, /defaultVisibility: true/);
  assert.match(countyLayer, /COUNTY_INTERNAL_POINT/);
  assert.equal(packageJson.scripts.test, "npm run build && node --test tests/*.test.mjs");
});
