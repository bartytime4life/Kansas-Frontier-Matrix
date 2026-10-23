import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const compileModule = async (name) => {
  const source = await readFile(new URL(`../app/${name}.ts`, import.meta.url), "utf8");
  const output = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 }, fileName: `${name}.ts` }).outputText;
  return import(`data:text/javascript;base64,${Buffer.from(output).toString("base64")}`);
};

const airspace = await compileModule("aviation-airspace");
const weather = await compileModule("aviation-weather");
const bytes = await readFile(new URL("../public/data/aviation/kansas-aviation-context.json", import.meta.url));
const context = airspace.parseAviationContext(JSON.parse(bytes.toString("utf8")));
const SALINA = [-97.6522, 38.7906], RURAL = [-100.35, 39.35], FORT_RILEY_RANGE = [-96.85, 39.2];

test("pinned asset digest, product id and cycle match the bytes the Site serves", () => {
  assert.equal(createHash("sha256").update(bytes).digest("hex"), airspace.AVIATION_CONTEXT_ASSET.sha256);
  assert.equal(context.nasrCycle, "2026-10-29");
  assert.ok(bytes.length < airspace.AVIATION_CONTEXT_ASSET.maxBytes);
  assert.ok(context.volumes.length > 150 && context.airports.length > 150 && context.airways.length > 100);
  assert.throws(() => airspace.parseAviationContext({ ...JSON.parse(bytes.toString("utf8")), product_id: "sha256:" + "0".repeat(64) }), /pinned product contract/);
});

test("edition status never calls a preview or expired cycle current", () => {
  const status = (day) => airspace.aviationEditionStatus(context, Date.parse(`${day}T12:00:00Z`)).state;
  assert.equal(status("2026-10-22"), "PREVIEW");
  assert.equal(status("2026-10-29"), "CURRENT");
  assert.equal(status("2026-11-25"), "CURRENT");
  assert.equal(status("2026-11-26"), "EXPIRED");
});

test("chart-style limits and technical labels keep their references", () => {
  assert.equal(airspace.formatAltitudeBound({ value_ft: 0, reference: "SFC" }), "SFC");
  assert.equal(airspace.formatAltitudeBound({ value_ft: 3800, reference: "MSL" }), "3,800 MSL");
  assert.equal(airspace.formatAltitudeBound({ value_ft: 700, reference: "AGL" }), "700 AGL");
  assert.equal(airspace.formatAltitudeBound({ value_ft: 18000, reference: "MSL", inclusive: false }), "below FL180");
  assert.equal(airspace.formatAltitudeBound({ value_ft: 29000, reference: "MSL" }), "FL290");
  const icc = context.volumes.filter(v => v.type === "CLASS_C" && v.identifier === "ICT").map(airspace.airspaceLabel).sort();
  assert.deepEqual(icc, ["CLASS C · ICT · 2,700 MSL–5,300 MSL", "CLASS C · ICT · SFC–5,300 MSL"]);
  const r = context.volumes.find(v => v.identifier === "R3602A");
  assert.equal(airspace.airspaceLabel(r), "R-3602A MANHATTAN · SFC–FL290");
});

test("display heights convert only for drawing and use the stated ground reference", () => {
  const shelf = context.volumes.find(v => v.type === "CLASS_C" && v.floor.value_ft === 2700);
  const { base, top } = airspace.displayHeightsMeters(shelf);
  assert.equal(shelf.ground_reference.airport, "ICT");
  assert.ok(Math.abs(base - (2700 - 1333) * 0.3048) < 0.01 && Math.abs(top - (5300 - 1333) * 0.3048) < 0.01);
  assert.equal(airspace.feetAboveGround({ value_ft: 700, reference: "AGL" }, 9999), 700);
  assert.equal(airspace.feetAboveGround({ value_ft: 1000, reference: "MSL" }, 1500), 0, "MSL limits below ground clamp to the surface");
  assert.ok(airspace.displayHeightsMeters(shelf, 3).top > top * 2.9);
});

test("drone rules: surface controlled needs authorization, restricted needs agency permission, shelves are above 400 AGL", () => {
  const d = context.volumes.find(v => v.type === "CLASS_D" && v.identifier === "SLN");
  assert.equal(airspace.droneRule(d).code, "ATC_AUTHORIZATION_REQUIRED");
  assert.match(airspace.droneRule(d).cite, /107\.41/);
  assert.equal(airspace.droneRule(context.volumes.find(v => v.identifier === "R3602A")).code, "NO_FLY_WITHOUT_PERMISSION");
  assert.equal(airspace.droneRule(context.volumes.find(v => v.type === "CLASS_C" && v.floor.value_ft === 2700)).code, "ABOVE_DRONE_CEILING");
  assert.equal(airspace.droneRule(context.volumes.find(v => v.identifier === "MSMOKY")).code, "ABOVE_DRONE_CEILING", "500 AGL MOA floor sits above drones");
  assert.equal(airspace.droneVerdictAtPoint(context, ...SALINA).rule.code, "ATC_AUTHORIZATION_REQUIRED");
  assert.equal(airspace.droneVerdictAtPoint(context, ...FORT_RILEY_RANGE).rule.code, "NO_FLY_WITHOUT_PERMISSION");
  assert.equal(airspace.droneVerdictAtPoint(context, ...RURAL).rule.code, "ABOVE_DRONE_CEILING");
  assert.match(airspace.droneVerdictAtPoint(context, ...RURAL).rule.title, /Class G/);
});

test("airspace column stacks NASR volumes on the regulatory defaults, surface upward", () => {
  const salina = airspace.airspaceColumn(context, ...SALINA, 1288);
  assert.equal(salina[0].floorText, "SFC");
  assert.ok(salina.some(band => band.label === "CLASS D · SLN · SFC–3,800 MSL" && band.airspaceClass === "D"));
  assert.ok(!salina.some(band => band.airspaceClass === "G"), "controlled to the surface at Salina");
  assert.deepEqual(salina.slice(-2).map(band => band.key), ["class-a", "above-fl600"]);
  const rural = airspace.airspaceColumn(context, ...RURAL, 2700);
  assert.equal(rural[0].airspaceClass, "G");
  assert.match(rural[0].manned, /Uncontrolled/);
  for (let i = 1; i < rural.length; i++) assert.ok(rural[i].floorFtAgl >= rural[i - 1].floorFtAgl);
});

test("point-in-polygon honours holes and bbox prefilter", () => {
  const ring = [[0, 0], [10, 0], [10, 10], [0, 10], [0, 0]], hole = [[4, 4], [6, 4], [6, 6], [4, 6], [4, 4]];
  assert.equal(airspace.pointInRings(2, 2, [ring, hole]), true);
  assert.equal(airspace.pointInRings(5, 5, [ring, hole]), false);
  assert.equal(airspace.pointInRings(11, 5, [ring]), false);
});

test("nearest airport and airway proximity", () => {
  assert.equal(airspace.nearestAirport(context.airports, ...SALINA).airport.faa_id, "SLN");
  const near = airspace.airwaysNearPoint(context, ...SALINA);
  assert.ok(near.length > 0 && near.every(segment => ["VICTOR", "JET", "RNAV_T", "RNAV_Q"].includes(segment.type)));
});

test("map feature builders respect group toggles and carry extrusion heights", () => {
  const all = airspace.airspaceFeatures(context, new Set(["controlled"]), 1);
  assert.ok(all.features.length > 0 && all.features.every(f => ["CLASS_B", "CLASS_C", "CLASS_D"].includes(f.properties.type)));
  assert.ok(all.features.every(f => f.properties.top > f.properties.base));
  const drones = airspace.droneFeatures(context, 1);
  assert.ok(drones.features.every(f => Math.abs(f.properties.top - 400 * 0.3048) < 1e-9));
  assert.ok(!drones.features.some(f => f.properties.code === "ABOVE_DRONE_CEILING"));
  const { points, runways } = airspace.airportFeatures(context);
  assert.equal(points.features.length, context.airports.length);
  assert.ok(runways.features.every(f => f.geometry.coordinates.length === 2));
});

const NOW = Date.parse("2026-10-22T18:30:00Z");
const metar = (changes = {}) => ({ icaoId: "KSLN", name: "Salina Rgnl, KS, US", lat: 38.79, lon: -97.65, elev: 393, obsTime: Math.floor(Date.parse("2026-10-22T17:56:00Z") / 1000),
  rawOb: "METAR KSLN 221756Z 18012G20KT 10SM BKN025 OVC040 21/09 A2990", temp: 21, dewp: 9, wdir: 180, wspd: 12, wgst: 20, visib: "10+", altim: 1012.5,
  clouds: [{ cover: "BKN", base: 2500 }, { cover: "OVC", base: 4000 }], fltCat: "MVFR", ...changes });

test("METAR parsing: latest per station, ceilings, categories, density altitude, region and age bounds", () => {
  const older = metar({ obsTime: Math.floor(Date.parse("2026-10-22T17:20:00Z") / 1000), rawOb: "older" });
  const { records, dropped } = weather.parseMetars([older, metar(), metar({ icaoId: "KDEN", lat: 39.8, lon: -104.6 }), metar({ icaoId: "KOLD", obsTime: Math.floor(Date.parse("2026-10-22T15:00:00Z") / 1000) }), { junk: true }], NOW);
  assert.equal(records.length, 1);
  assert.equal(dropped, 3);
  const [r] = records;
  assert.equal(r.raw.startsWith("METAR KSLN"), true);
  assert.equal(r.ceilingFtAgl, 2500); assert.equal(r.ceilingCover, "BKN");
  assert.equal(r.flightCategory, "MVFR"); assert.equal(r.visibilitySm, 10); assert.equal(r.visibilityAtLeast, true);
  assert.equal(r.altimeterInHg, 29.9);
  assert.equal(r.elevationFt, 1289);
  assert.ok(r.densityAltitudeFt > 1289 + 1000, "warm day raises density altitude");
  assert.equal(weather.parseMetars([metar({ obsTime: "2026-10-22 17:56:00" })], NOW).records.length, 1, "ISO-like provider time accepted");
});

test("flight categories follow FAA thresholds", () => {
  assert.equal(weather.flightCategory(null, 10), "VFR");
  assert.equal(weather.flightCategory(3000, 10), "MVFR");
  assert.equal(weather.flightCategory(900, 10), "IFR");
  assert.equal(weather.flightCategory(400, 10), "LIFR");
  assert.equal(weather.flightCategory(5000, 0.5), "LIFR");
  assert.equal(weather.flightCategory(null, null), null);
  assert.deepEqual(weather.ceilingOf([{ cover: "SCT", baseFtAgl: 800 }, { cover: "OVC", baseFtAgl: 1500 }], 300), { ft: 300, cover: "VV" });
});

test("VFR check ties the nearest observation to the airspace class", () => {
  assert.equal(weather.basicVfrCheck("D", { station: "KSLN", ceilingFtAgl: 2500, visibilitySm: 10 }).meets, true);
  assert.equal(weather.basicVfrCheck("D", { station: "KSLN", ceilingFtAgl: 800, visibilitySm: 10 }).meets, false);
  assert.equal(weather.basicVfrCheck("G", { station: "KSLN", ceilingFtAgl: 800, visibilitySm: 2 }).meets, true);
  assert.equal(weather.basicVfrCheck("E", null).meets, null);
});

test("PIREPs keep reported altitude, intensities and urgency; climb/descent has no altitude", () => {
  const base = { obsTime: Math.floor(Date.parse("2026-10-22T17:00:00Z") / 1000), lat: 38.5, lon: -98.0, acType: "B737", rawOb: "ICT UA /OV ICT090020/TM 1700/FL110/TP B737/TB MOD", fltLvl: 110, tbInt1: "MOD", tbBas1: 100, tbTop1: 120 };
  const { records, dropped } = weather.parsePireps([base, { ...base, fltLvl: "DURD", pirepType: "Urgent PIREP", rawOb: "SLN UUA /OV SLN/TM 1710/FLDURD/TP C172/IC SEV" }, { ...base, lon: -110 }, { ...base, obsTime: Math.floor(Date.parse("2026-10-22T10:00:00Z") / 1000) }], NOW);
  assert.equal(dropped, 2);
  const cruise = records.find(r => !r.urgent), urgent = records.find(r => r.urgent);
  assert.equal(cruise.altitudeFtMsl, 11000);
  assert.equal(cruise.turbulence, "MOD 10000–12000 ft");
  assert.equal(urgent.altitudeFtMsl, null);
  const features = weather.pirepFeatures(records, () => 1500, 1);
  assert.ok(Math.abs(features.features.find(f => !f.properties.urgent).properties.base - (11000 - 1500) * 0.3048) < 1e-6);
});

// Synthetic provider records: no live observations or aircraft identifiers are fixtures.
const pirep = (changes = {}) => ({ obsTime: NOW / 1000 - 1800, lat: 38.5, lon: -98,
  rawOb: "SYNTHETIC PIREP FOR PARSER TEST", acType: "TEST", fltLvl: "230", fltLvlType: "CRUISE", ...changes });

test("PIREP string and numeric flight levels reach the map at reported feet MSL", () => {
  for (const [fltLvl, feet] of [["230", 23000], [230, 23000], ["095", 9500], [" 230 ", 23000], ["600", 60000], ["000", 0], [0, 0]]) {
    const { records, dropped } = weather.parsePireps([pirep({ fltLvl })], NOW);
    assert.equal(dropped, 0);
    assert.equal(records[0].altitudeFtMsl, feet, String(fltLvl));
    assert.equal(records[0].flightLevelType, "CRUISE");
    for (const exaggeration of [1, 3, 6]) {
      const feature = weather.pirepFeatures(records, () => 1500, exaggeration).features[0];
      assert.ok(Math.abs(feature.properties.base - Math.max(0, feet - 1500) * 0.3048 * exaggeration) < 1e-8);
      assert.equal(feature.properties.altitude_ft_msl, feet);
      assert.equal(feature.properties.flight_level_type, "CRUISE");
      assert.match(feature.properties.label, /ft MSL/);
      assert.doesNotMatch(feature.properties.label, /climb|descent|unavailable/);
    }
  }
});

test("PIREP climb and descent phases have distinct labels and no fabricated fixed altitude", () => {
  for (const [fltLvlType, label] of [["DURC", /climb/], ["DURD", /descent/]]) {
    for (const fltLvl of ["230", 230, "DURC", "DURD", null, undefined]) {
      const { records } = weather.parsePireps([pirep({ fltLvlType, fltLvl })], NOW);
      assert.equal(records[0].flightLevelType, fltLvlType);
      assert.equal(records[0].altitudeFtMsl, null);
      assert.deepEqual(weather.pirepFeatures(records, () => { throw new Error("No fixed altitude to project"); }, 3).features, []);
      assert.match(weather.pirepAltitudeLabel(records[0]), label);
      assert.match(weather.pirepAltitudeLabel(records[0]), /altitude varies/);
      assert.doesNotMatch(weather.pirepAltitudeLabel(records[0]), /ft MSL/);
    }
  }
});

test("PIREP malformed and missing flight levels stay unavailable rather than becoming zero or a phase", () => {
  for (const fltLvl of [undefined, null, "", " ", "UNKN", "DURC", "DURD", "230junk", "FL230", "230.5", "2.3e2", "0xe6", "-1", "601", true, false, [], {}, NaN, Infinity, -1, 601, 230.5]) {
    const { records } = weather.parsePireps([pirep({ fltLvl })], NOW);
    assert.equal(records.length, 1, "a missing altitude does not erase the reported location");
    assert.equal(records[0].altitudeFtMsl, null, String(fltLvl));
    assert.deepEqual(weather.pirepFeatures(records, () => 1500, 1).features, []);
    assert.match(weather.pirepAltitudeLabel(records[0]), /altitude unavailable/);
    assert.doesNotMatch(weather.pirepAltitudeLabel(records[0]), /climb|descent|ft MSL/);
  }
  for (const fltLvlType of ["GRND", "OTHER", "UNKN", undefined, null, "", "invalid", 0, {}]) {
    const { records } = weather.parsePireps([pirep({ fltLvlType })], NOW);
    assert.equal(records[0].altitudeFtMsl, 23000, "valid altitude is retained independently of an absent/unknown phase");
    assert.equal(records[0].flightLevelType, ["GRND", "OTHER", "UNKN"].includes(fltLvlType) ? fltLvlType : null);
  }
});

test("PIREP cloud bases are bounded integer feet, with low/high and zero observations preserved", () => {
  for (const base of [0, 500, 5000, 11000, 60000]) {
    const { records } = weather.parsePireps([pirep({ clouds: [{ cover: "BKN", base }] })], NOW);
    assert.equal(records[0].skyCondition, `BKN ${base} ft`);
    assert.equal(records[0].altitudeFtMsl, 23000, "cloud height is never the aircraft altitude");
  }
  const { records } = weather.parsePireps([pirep({ clouds: [{ cover: "SCT", base: 500 }, { cover: "BKN", base: 5000 }] })], NOW);
  assert.equal(records[0].skyCondition, "SCT 500 ft, BKN 5000 ft");
});

test("PIREP malformed or absent cloud heights never fabricate a height or observation", () => {
  for (const base of [undefined, null, "500", "", "UNKN", -1, 60001, 500.5, NaN, Infinity, false, [], {}]) {
    const { records } = weather.parsePireps([pirep({ clouds: [{ cover: "BKN", base }] })], NOW);
    assert.equal(records[0].skyCondition, "BKN", String(base));
  }
  for (const clouds of [undefined, null, [], {}, "BKN005", [null, 42, {}, { base: null }]]) {
    const { records } = weather.parsePireps([pirep({ clouds })], NOW);
    assert.equal(records[0].skyCondition, null);
  }
});

test("PIREP missing/invalid observations are empty or dropped, never synthesized", () => {
  assert.deepEqual(weather.parsePireps([], NOW), { records: [], dropped: 0 });
  assert.deepEqual(weather.pirepFeatures([], () => 1500, 1).features, []);
  for (const payload of [null, undefined, {}, ""]) assert.throws(() => weather.parsePireps(payload, NOW), /not a list/);
  const invalid = [null, {}, pirep({ obsTime: undefined }), pirep({ obsTime: "invalid" }), pirep({ obsTime: NOW / 1000 - 4 * 3600 }),
    pirep({ obsTime: NOW / 1000 + 3600 }), pirep({ rawOb: undefined }), pirep({ lon: undefined }), pirep({ lat: undefined }), pirep({ lon: -110 })];
  assert.deepEqual(weather.parsePireps(invalid, NOW), { records: [], dropped: invalid.length });
  const { records } = weather.parsePireps([pirep({ fltLvl: undefined, fltLvlType: undefined, acType: undefined, clouds: undefined })], NOW);
  assert.equal(records[0].altitudeFtMsl, null);
  assert.equal(records[0].flightLevelType, null);
  assert.equal(records[0].aircraftType, null);
  assert.equal(records[0].skyCondition, null);
});

test("metar features draw ceilings as discs at reported height", () => {
  const { records } = weather.parseMetars([metar()], NOW);
  const { stations, ceilings } = weather.metarFeatures(records, 2);
  assert.equal(stations.features[0].properties.color, weather.FLIGHT_CATEGORY_COLORS.MVFR);
  assert.ok(Math.abs(ceilings.features[0].properties.base - 2500 * 0.3048 * 2) < 1e-6);
  assert.match(stations.features[0].properties.label, /KSLN MVFR · 180@12G20kt/);
});

test("weather route uses fixed upstream URLs and never forwards caller input", async () => {
  const server = await readFile(new URL("../app/aviation-weather-server.ts", import.meta.url), "utf8");
  assert.match(server, /redirect: "manual"/);
  assert.match(server, /readBoundedText\(response, MAX_BYTES/);
  for (const route of ["metar", "pireps"]) {
    const handler = await readFile(new URL(`../app/api/aviation/${route}/route.ts`, import.meta.url), "utf8");
    assert.match(handler, /export async function GET\(\)/, "handler takes no request input");
  }
});
