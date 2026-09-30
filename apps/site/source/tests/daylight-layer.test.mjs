import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import ts from "typescript";
import { getSunrise, getTwilight } from "sunrise-sunset-js";

const modules = new Map();
const spaUrl = new URL("../node_modules/sunrise-sunset-js/dist/index.js", import.meta.url).href;
const clippingUrl = new URL("../node_modules/polygon-clipping/dist/polygon-clipping.esm.js", import.meta.url).href;
async function moduleUrl(file) {
  file = path.resolve(file);
  if (modules.has(file)) return modules.get(file);
  let javascript = ts.transpileModule(await readFile(file, "utf8"), {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  }).outputText
    .replaceAll('from "sunrise-sunset-js"', `from ${JSON.stringify(spaUrl)}`)
    .replaceAll('from "polygon-clipping"', `from ${JSON.stringify(clippingUrl)}`);
  for (const match of [...javascript.matchAll(/from ["'](\.[^"']+)["']/g)]) {
    javascript = javascript.replace(match[0], `from ${JSON.stringify(await moduleUrl(path.resolve(path.dirname(file), match[1]) + ".ts"))}`);
  }
  const url = `data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`;
  modules.set(file, url);
  return url;
}

const solar = await import(await moduleUrl("app/daylight-layer.ts"));
const runtime = await import(await moduleUrl("app/map-runtime.ts"));

const pointInRing = (point, ring) => {
  let inside = false;
  for (let index = 0, previous = ring.length - 1; index < ring.length; previous = index, index += 1) {
    const [x, y] = ring[index];
    const [previousX, previousY] = ring[previous];
    const crosses = (y > point[1]) !== (previousY > point[1])
      && point[0] < ((previousX - x) * (point[1] - y)) / (previousY - y) + x;
    if (crosses) inside = !inside;
  }
  return inside;
};

const pointInFeature = (point, feature) => feature.geometry.coordinates.some((polygon) =>
  pointInRing(point, polygon[0]) && !polygon.slice(1).some((hole) => pointInRing(point, hole)));

const bandAt = (geometry, point) => geometry.features.find((feature) => pointInFeature(point, feature))?.properties.band ?? "day";
const bandsAt = (geometry, point) => geometry.features.filter((feature) => pointInFeature(point, feature)).map((feature) => feature.properties.band);
const bandForElevation = (elevation) => elevation <= -18 ? "night"
  : elevation <= -12 ? "astronomical"
    : elevation <= -6 ? "nautical"
      : elevation <= -0.833 ? "civil" : "day";

const signedDegrees = (degrees) => ((degrees + 180) % 360 + 360) % 360 - 180;

const destinationPoint = (longitude, latitude, angularRadius, bearingDegrees) => {
  const radians = Math.PI / 180;
  const phi1 = latitude * radians;
  const lambda1 = longitude * radians;
  const delta = angularRadius * radians;
  const bearing = bearingDegrees * radians;
  const phi2 = Math.asin(Math.sin(phi1) * Math.cos(delta) + Math.cos(phi1) * Math.sin(delta) * Math.cos(bearing));
  const lambda2 = lambda1 + Math.atan2(
    Math.sin(bearing) * Math.sin(delta) * Math.cos(phi1),
    Math.cos(delta) - Math.sin(phi1) * Math.sin(phi2),
  );
  return [signedDegrees(lambda2 / radians), phi2 / radians];
};

const crossingForDeclination = (samples, target) => {
  for (let index = 1; index < samples.length; index += 1) {
    let left = samples[index - 1];
    let right = samples[index];
    if ((left.declination - target) * (right.declination - target) > 0) continue;
    for (let step = 0; step < 32; step += 1) {
      const middleMs = Math.floor((left.instant + right.instant) / 2);
      const middle = { instant: middleMs, declination: solar.solarPositionAt(middleMs).declinationDegrees };
      if ((left.declination - target) * (middle.declination - target) <= 0) right = middle;
      else left = middle;
    }
    return Math.floor((left.instant + right.instant) / 2);
  }
  assert.fail(`No 2026 solar-declination crossing found for ${target}°`);
};

test("SPA-backed solar position matches the published NREL Golden, Colorado example", () => {
  const result = solar.solarPositionAt(Date.parse("2003-10-17T19:30:30Z"), 39.742476, -105.1786, {
    elevation: 1830.14, pressure: 820, temperature: 11, deltaT: 67,
  });
  assert.ok(Math.abs(result.elevationDegrees - 39.88838) < 0.00001);
  assert.ok(Math.abs(result.azimuthDegrees - 194.34024) < 0.00001);
});

test("apparent sunrise and all twilight boundaries use their conventional solar altitudes", () => {
  const latitude = 38.5;
  const longitude = -98.2;
  const day = new Date("2026-06-21T12:00:00Z");
  const options = { timezoneId: solar.KANSAS_DAYLIGHT_TIME_ZONE };
  const times = [
    [getSunrise(latitude, longitude, day, options), -0.833],
    [getTwilight(latitude, longitude, day, options).civilDawn, -6],
    [getTwilight(latitude, longitude, day, options).nauticalDawn, -12],
    [getTwilight(latitude, longitude, day, options).astronomicalDawn, -18],
  ];
  for (const [instant, expectedAltitude] of times) {
    assert.ok(instant instanceof Date);
    const actualAltitude = solar.solarPositionAt(instant, latitude, longitude).elevationDegrees;
    assert.ok(Math.abs(actualAltitude - expectedAltitude) < 0.03, `${actualAltitude}° should be near ${expectedAltitude}°`);
  }
});

test("Kansas Central dates convert across standard time and 23/25-hour DST days", () => {
  const winter = solar.kansasLocalDayInterval("2026-01-15");
  assert.equal(new Date(winter.startMs).toISOString(), "2026-01-15T06:00:00.000Z");
  assert.equal(solar.formatKansasSolarTime(Date.parse("2026-01-15T18:34:56Z")).central.includes("12:34:56 PM CST"), true);
  assert.equal(solar.formatKansasSolarTime(Date.parse("2026-01-15T18:34:56Z")).utc.includes("18:34:56 UTC"), true);
  assert.equal(solar.kansasLocalDayInterval("2026-03-08").durationMs, 23 * 3_600_000);
  assert.equal(solar.kansasLocalDayInterval("2026-11-01").durationMs, 25 * 3_600_000);
  assert.equal(solar.instantAtDayFraction("2026-03-08", 0.5), winter.startMs + (solar.kansasLocalDayInterval("2026-03-08").startMs - winter.startMs) + 11.5 * 3_600_000);
  assert.equal(solar.isInstantInKansasDay(solar.kansasLocalDayInterval("2026-11-01").endMs, "2026-11-01"), false);
});

test("loop, date-change, scrub, and URL-restore state stay bounded and paused when restored", () => {
  assert.equal(solar.daylightLoopFraction(0, 30_000), 0.5);
  assert.equal(solar.daylightLoopFraction(0.75, 30_000), 0.25);
  assert.equal(solar.daylightLoopFraction(0.25, 60_000), 0.25);
  assert.equal(solar.daylightShouldAutoplay(false, false), true);
  assert.equal(solar.daylightShouldAutoplay(true, false), false);
  assert.equal(solar.daylightShouldAutoplay(false, true), false);
  assert.equal(solar.instantAtDayFraction("2026-03-08", 0.5), solar.kansasLocalDayInterval("2026-03-08").startMs + 11.5 * 3_600_000);
  const restored = solar.restoreDaylightView("2026-11-01", "2026-11-01T17:00:00.000Z", true, "2026-09-29");
  assert.deepEqual(restored, { day: "2026-11-01", instantMs: Date.parse("2026-11-01T17:00:00Z"), enabled: true, playing: false });
  const outOfDay = solar.restoreDaylightView("2026-11-01", "2026-11-02T12:00:00.000Z", false, "2026-09-29");
  assert.equal(outOfDay.instantMs, solar.kansasLocalDayInterval("2026-11-01").startMs);
  assert.equal(outOfDay.playing, false);
});

test("equinox, solstice, and polar day/night geometry remain bounded", () => {
  const equinox = solar.solarPositionAt(Date.parse("2026-03-20T14:46:00Z"), 0, 0);
  const summer = solar.solarPositionAt(Date.parse("2026-06-21T12:00:00Z"), 0, 0);
  const winter = solar.solarPositionAt(Date.parse("2026-12-21T12:00:00Z"), 0, 0);
  assert.ok(Math.abs(equinox.declinationDegrees) < 0.2);
  assert.ok(summer.declinationDegrees > 23 && summer.declinationDegrees < 24);
  assert.ok(winter.declinationDegrees < -23 && winter.declinationDegrees > -24);
  assert.ok(solar.solarPositionAt(Date.parse("2026-06-21T12:00:00Z"), 89, 0).elevationDegrees > 0);
  assert.ok(solar.solarPositionAt(Date.parse("2026-12-21T12:00:00Z"), 89, 0).elevationDegrees < 0);

  const geometry = solar.buildDaylightGeometry(Date.parse("2026-06-21T12:00:00Z"));
  assert.equal(geometry.features.length, 4);
  assert.ok(geometry.features.some((feature) => feature.properties.band === "astronomical"));
  assert.ok(geometry.features.some((feature) => feature.properties.band === "nautical"));
  assert.ok(geometry.features.some((feature) => feature.properties.band === "civil"));
  for (const feature of geometry.features) {
    assert.equal(feature.geometry.type, "MultiPolygon");
    for (const polygon of feature.geometry.coordinates) for (const ring of polygon) {
      assert.deepEqual(ring[0], ring.at(-1));
      assert.ok(ring.length >= 4);
      assert.ok(ring.every(([longitude, latitude]) => longitude >= -180 && longitude <= 180 && latitude >= -90 && latitude <= 90));
      for (let index = 1; index < ring.length; index += 1) {
        const longitudeSpan = Math.abs(ring[index][0] - ring[index - 1][0]);
        assert.ok(longitudeSpan <= 180 || Math.abs(Math.abs(ring[index][1]) - 90) < 1e-8, "no polygon edge jumps across the antimeridian");
      }
    }
  }
});

test("daylight polygons preserve the physical band on both sides of the antimeridian", () => {
  const instants = [
    Date.parse("2026-03-20T00:00:00Z"),
    Date.parse("2026-05-01T00:00:00Z"),
    Date.parse("2026-06-21T00:00:00Z"),
    Date.parse("2026-09-22T00:00:00Z"),
    Date.parse("2026-11-01T00:00:00Z"),
    Date.parse("2026-12-21T00:00:00Z"),
  ];
  for (const instant of instants) {
    const geometry = solar.buildDaylightGeometry(instant);
    for (const latitude of [-80, -55, -25, 0, 25, 55, 80]) {
      const east = [179.999, latitude];
      const west = [-179.999, latitude];
      const eastBand = bandAt(geometry, east);
      const westBand = bandAt(geometry, west);
      assert.equal(eastBand, westBand, `adjacent positions at ${latitude}° share a band at ${new Date(instant).toISOString()}`);
      const expected = solar.solarPositionAt(instant, latitude, 179.999).elevationDegrees;
      const expectedBand = expected <= -18 ? "night" : expected <= -12 ? "astronomical" : expected <= -6 ? "nautical" : expected <= -0.833 ? "civil" : "day";
      const nearBoundary = [-18, -12, -6, -0.833].some((boundary) => Math.abs(expected - boundary) < 0.4);
      if (!nearBoundary) assert.equal(eastBand, expectedBand, `band at ${latitude}° agrees with SPA at ${new Date(instant).toISOString()}`);
    }
  }
});

test("polar twilight subtraction stays correct across every pole-enclosure threshold and the seam", () => {
  const samples = [];
  const yearStart = Date.parse("2026-01-01T00:00:00Z");
  for (let instant = yearStart; instant <= Date.parse("2027-01-01T00:00:00Z"); instant += 12 * 60 * 60 * 1000) {
    samples.push({ instant, declination: solar.solarPositionAt(instant).declinationDegrees });
  }
  const thresholds = [0.833, 6, 12, 18];
  for (const threshold of thresholds) for (const declinationThreshold of [-threshold, threshold]) {
    const crossing = crossingForDeclination(samples, declinationThreshold);
    for (const instant of [crossing - 15 * 60_000, crossing + 15 * 60_000]) {
      const sun = solar.solarPositionAt(instant);
      const antiLongitude = signedDegrees(sun.subsolarLongitudeDegrees + 180);
      const geometry = solar.buildDaylightGeometry(instant);
      const innerRadii = { astronomical: 72, nautical: 78, civil: 84 };
      for (const feature of geometry.features.filter(({ properties }) => properties.band !== "night")) {
        const innerRadius = innerRadii[feature.properties.band];
        for (const radius of [30, 60, innerRadius - 1]) for (let bearing = 0; bearing < 360; bearing += 30) {
          const point = destinationPoint(antiLongitude, -sun.declinationDegrees, radius, bearing);
          if (Math.abs(signedDegrees(point[0] - antiLongitude)) < 0.01) continue; // avoid the artificial branch-cut edge itself
          assert.equal(
            bandsAt(geometry, point).includes(feature.properties.band),
            false,
            `${feature.properties.band} does not overlap its inner disk at declination ${sun.declinationDegrees.toFixed(3)}°, radius ${radius}°, bearing ${bearing}°`,
          );
        }
      }
      const polewardSign = -Math.sign(sun.declinationDegrees);
      const latitudes = [70, 80, 85, 88, 89.5, 89.9].map((latitude) => polewardSign * latitude);
      const longitudes = [antiLongitude, 179.999, -179.999, signedDegrees(antiLongitude + 90), signedDegrees(antiLongitude - 90)];
      for (const latitude of latitudes) for (const longitude of longitudes) {
        const point = [longitude, latitude];
        const actual = solar.solarPositionAt(instant, latitude, longitude).elevationDegrees;
        if ([-18, -12, -6, -0.833].some((boundary) => Math.abs(actual - boundary) < 0.6)) continue;
        assert.equal(
          bandAt(geometry, point),
          bandForElevation(actual),
          `twilight band matches SPA at declination ${sun.declinationDegrees.toFixed(3)}°, point ${longitude.toFixed(3)}°, ${latitude.toFixed(3)}°`,
        );
      }
    }
  }
});

test("daylight tints basemap and imagery, then yields to observation overlays and labels", () => {
  const sources = new Map();
  const layers = [
    { id: "basemap-labels", type: "symbol" },
    { id: "external-goes-geocolor", type: "raster" },
    { id: "external-hydrology", type: "line" },
    { id: "external-streamflow-observations", type: "circle" },
  ];
  const map = {
    getStyle: () => ({ layers: [...layers] }),
    getSource: (id) => sources.get(id),
    addSource: (id, source) => sources.set(id, { ...source, setData(data) { this.data = data; } }),
    getLayer: (id) => layers.find((layer) => layer.id === id),
    addLayer: (layer, beforeId) => {
      const index = beforeId ? layers.findIndex((candidate) => candidate.id === beforeId) : layers.length;
      layers.splice(index < 0 ? layers.length : index, 0, layer);
    },
    moveLayer: (id) => {
      const index = layers.findIndex((layer) => layer.id === id);
      if (index < 0) return;
      layers.push(layers.splice(index, 1)[0]);
    },
    setLayoutProperty: (id, name, value) => { map.getLayer(id).layout[name] = value; },
  };
  assert.equal(runtime.setDaylightMapLayer(map, true, Date.parse("2026-06-21T12:00:00Z")), true);
  const ids = layers.map(({ id }) => id);
  assert.ok(ids.indexOf("basemap-labels") < ids.indexOf(runtime.DAYLIGHT_FILL_LAYER_ID));
  assert.ok(ids.indexOf("external-goes-geocolor") < ids.indexOf(runtime.DAYLIGHT_FILL_LAYER_ID));
  assert.ok(ids.indexOf(runtime.DAYLIGHT_FILL_LAYER_ID) < ids.indexOf("external-hydrology"));
  assert.ok(ids.indexOf(runtime.DAYLIGHT_FILL_LAYER_ID) < ids.indexOf("external-streamflow-observations"));
  assert.equal(sources.get(runtime.DAYLIGHT_GEOJSON_SOURCE_ID).data.features.length, 4);
  assert.equal(sources.get(runtime.DAYLIGHT_GEOJSON_SOURCE_ID).data.features[0].geometry.type, "MultiPolygon");
  assert.equal(runtime.setDaylightMapLayer(map, false, 0), true);
  assert.equal(map.getLayer(runtime.DAYLIGHT_FILL_LAYER_ID).layout.visibility, "none");
});

test("page persists selected solar cursor and restores the layer paused with reduced-motion safeguards", async () => {
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const requiredStateContracts = [
    ['params.set("sunDay", daylightDay)', "day is saved in shared map state"],
    ['params.set("sunAt", new Date(daylightInstant).toISOString())', "cursor is saved in shared map state"],
    ['restoreDaylightView(params.get("sunDay"), params.get("sunAt"), params.get("sun") === "on")', "URL restore uses the validated paused state helper"],
    [/daylightPlayingRef\.current = false;\s+setDaylightDay\(restoredSolar\.day\)/, "URL restore pauses playback"],
    ["daylightShouldAutoplay(reducedMotion, document.hidden)", "date selection honors reduced motion and hidden tabs"],
    ["if (!enabled || document.hidden) setDaylightPlayback(false)", "hiding the layer pauses its invisible loop"],
    ["now - lastMapUpdate >= 100", "map geometry updates at a bounded 10 Hz"],
    ["now - lastClockUpdate >= 250", "clock display rerenders at a bounded 4 Hz"],
    ["if (!document.hidden) return", "tab visibility change pauses playback"],
    ['daylightPlaying ? "Pause" : "Resume"', "control toggles pause and resume"],
    [/seekDaylight\(Number\(event\.target\.value\) \/ 10_000\)/, "scrubber seeks within the selected day"],
  ];
  for (const [contract, description] of requiredStateContracts) {
    assert.ok(typeof contract === "string" ? page.includes(contract) : contract.test(page), description);
  }
});
