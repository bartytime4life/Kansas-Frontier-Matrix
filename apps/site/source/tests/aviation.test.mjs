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
const drone = await compileModule("aviation-drone-data");
const traffic = await compileModule("aviation-traffic");
const chart = await compileModule("aviation-chart");
const profile = await compileModule("aviation-profile");
const research = await compileModule("aviation-research");
const dossier = await compileModule("research-context");
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

test("private-use facilities are listed with a use flag, styled apart, and heliports never anchor ground", () => {
  const privateUse = context.airports.filter(airport => airport.use === "PRIVATE");
  assert.ok(privateUse.length > 300 && context.airports.every(airport => airport.use === "PUBLIC" || airport.use === "PRIVATE"));
  assert.ok(privateUse.some(airport => airport.facility_type === "HELIPORT"));
  const anchors = airspace.groundAnchors(context.airports);
  assert.ok(anchors.length < context.airports.length && anchors.every(airport => airport.facility_type !== "HELIPORT"));
  const { points } = airspace.airportFeatures({ airports: privateUse.slice(0, 1) });
  assert.equal(points.features[0].properties.private, true);
  assert.match(points.features[0].properties.label, / · PVT$/);
  const raw = JSON.parse(bytes.toString("utf8"));
  assert.throws(() => airspace.parseAviationContext({ ...raw, airports: [{ ...raw.airports[0], use: "MILITARY" }] }), /Invalid airport record/);
});

test("2D chart labels read ceiling/floor in hundreds of feet, as on a sectional", () => {
  const ict = context.volumes.filter(volume => volume.type === "CLASS_C" && volume.identifier === "ICT").map(airspace.chartLabel).sort();
  assert.deepEqual(ict, ["ICT 53/27", "ICT 53/SFC"]);
  assert.equal(airspace.chartLimit({ value_ft: 700, reference: "AGL" }), "7 AGL");
  assert.equal(airspace.chartLimit({ value_ft: 18000, reference: "MSL", inclusive: false }), "180");
  const features = airspace.airspaceFeatures(context, new Set(["controlled"]), 1).features;
  assert.ok(features.every(feature => typeof feature.properties.chart === "string" && Number.isFinite(feature.properties.groundFt)));
});

test("the altitude slice keeps what exists at one height, in 2D, from the same features as 3D", () => {
  const groundAt = () => 1333;
  const controlled = airspace.airspaceFeatures(context, new Set(["controlled"]), 3);
  const ictAt = (slice) => chart.sliceCollection(controlled, slice, 3, groundAt).features.filter(feature => feature.properties.chart.startsWith("ICT ")).map(feature => feature.properties.chart).sort();
  assert.deepEqual(ictAt({ kind: "msl", ft: 4000 }), ["ICT 53/27", "ICT 53/SFC"], "4,000 ft MSL is inside the core and the shelf");
  assert.deepEqual(ictAt({ kind: "msl", ft: 2000 }), ["ICT 53/SFC"], "below the 2,700 ft shelf floor only the core remains");
  assert.deepEqual(ictAt({ kind: "msl", ft: 6000 }), [], "above the 5,300 ft ceiling Class C is gone");
  assert.deepEqual(ictAt({ kind: "drone" }), ["ICT 53/SFC"], "the drone slice keeps volumes that start below 400 ft AGL");
  assert.equal(chart.sliceCollection(controlled, chart.ALL_ALTITUDES, 3, groundAt), controlled);
  // Thin point markers (aircraft) use a tolerance band instead of containment.
  const plane = traffic.trafficFeatures(traffic.parseTraffic({ ac: [aircraft()] }).records, groundAt, 1, () => "CLASS C · ICT");
  assert.equal(chart.sliceCollection(plane, { kind: "msl", ft: 4500 }, 1, groundAt, chart.SLICE_POINT_TOLERANCE_FT).features.length, 1);
  assert.equal(chart.sliceCollection(plane, { kind: "msl", ft: 6000 }, 1, groundAt, chart.SLICE_POINT_TOLERANCE_FT).features.length, 0);
  assert.equal(chart.sliceTitle({ kind: "msl", ft: 14500 }), "14,500 ft MSL");
});

test("picked-point ground uses loaded terrain only when it agrees with the nearest facility", () => {
  const anchors = airspace.groundAnchors(context.airports);
  const sln = anchors.find(airport => airport.faa_id === "SLN");
  const at = (terrainFt) => airspace.pointGroundReference(anchors, sln.lon, sln.lat, terrainFt);
  assert.deepEqual([at(sln.elevation_ft + 40).method, at(sln.elevation_ft + 40).ft], ["TERRAIN_DEM", sln.elevation_ft + 40]);
  const spike = at(sln.elevation_ft + 1500);
  assert.deepEqual([spike.method, spike.ft, spike.terrainRejected], ["NEAREST_FACILITY", sln.elevation_ft, true], "a DEM spike is reported, not used");
  assert.deepEqual([at(null).method, at(null).terrainRejected], ["NEAREST_FACILITY", false]);
  assert.equal(airspace.pointGroundReference([], -98, 38, 1800).method, "TERRAIN_DEM");
  assert.deepEqual(airspace.pointGroundReference([], -98, 38, null), { ft: 0, method: "NONE", facility: null, km: null, terrainRejected: false });
});

test("the drone verdict judges MSL floors against the picked point's ground", () => {
  // Under the Wichita Class C shelf (floor 2,700 MSL): ~1,367 ft above 1,333 ft ground, but 250 ft above 2,450 ft ground.
  assert.equal(airspace.droneVerdictAtPoint(context, -97.6, 37.7, 1333).rule.code, "ABOVE_DRONE_CEILING");
  assert.equal(airspace.droneVerdictAtPoint(context, -97.6, 37.7, 2450).rule.code, "ATC_AUTHORIZATION_REQUIRED");
  assert.match(airspace.droneVerdictAtPoint(context, -100.35, 39.35).rule.detail, /TFRs still apply \(drawn when their FAA boundary can be read\)/);
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
  assert.match(server, /readBoundedText\(response, maxBytes/);
  const droneServer = await readFile(new URL("../app/aviation-drone-server.ts", import.meta.url), "utf8");
  assert.doesNotMatch(droneServer, /searchParams|nextUrl|NextRequest|headers\.get/, "drone routes never read caller input");
  assert.match(droneServer, /if \(!complete\) throw/, "an unfinished UASFM paging run fails instead of drawing a partial grid");
  const trafficServer = await readFile(new URL("../app/aviation-traffic-server.ts", import.meta.url), "utf8");
  assert.match(trafficServer, /for \(const provider of TRAFFIC_PROVIDERS\)/, "providers are tried in a fixed order");
  assert.doesNotMatch(trafficServer, /searchParams|nextUrl|NextRequest|headers\.get/, "the traffic route never reads caller input");
  for (const route of ["metar", "pireps", "traffic", "uas-grid", "tfrs"]) {
    const handler = await readFile(new URL(`../app/api/aviation/${route}/route.ts`, import.meta.url), "utf8");
    assert.match(handler, /export async function GET\(\)/, "handler takes no request input");
  }
});

const aircraft = (changes = {}) => ({ hex: "a1b2c3", flight: "SWA123  ", r: "N123SW", t: "B738", category: "A3", lat: 37.65, lon: -97.43, alt_baro: 4000, alt_geom: 4100,
  gs: 210.4, track: 15, baro_rate: -800, squawk: "4521", seen_pos: 2.1, seen: 0.4, ...changes });

test("traffic parsing keeps fresh in-region positions, decodes ground and emergencies, accepts both list keys", () => {
  const { records, dropped } = traffic.parseTraffic({ ac: [aircraft(), aircraft({ hex: "a1b2c4", seen_pos: 90 }), aircraft({ hex: "a1b2c5", lon: -120 }),
    aircraft({ hex: "A1B2C3" }), aircraft({ hex: "c0ffee", alt_baro: "ground", alt_geom: undefined, flight: "N5" }), aircraft({ hex: "beef01", squawk: "7700" }), { junk: 1 }] });
  assert.equal(dropped, 4, "stale, out-of-region, duplicate hex and malformed");
  const byHex = Object.fromEntries(records.map(record => [record.hex, record]));
  assert.equal(byHex.a1b2c3.callsign, "SWA123");
  assert.equal(traffic.aircraftAltitudeMsl(byHex.a1b2c3), 4100);
  assert.equal(byHex.c0ffee.onGround, true); assert.equal(traffic.aircraftAltitudeMsl(byHex.c0ffee), null);
  assert.equal(byHex.beef01.emergency, "general emergency");
  assert.equal(traffic.parseTraffic({ aircraft: [aircraft()] }).records.length, 1);
  assert.throws(() => traffic.parseTraffic({ msg: "no" }), /no aircraft list/);
  assert.deepEqual(traffic.TRAFFIC_PROVIDERS.map(provider => provider.id), ["adsb-lol", "adsb-fi"]);
  assert.ok(traffic.TRAFFIC_PROVIDERS.every(provider => provider.url.startsWith("https://") && provider.terms && provider.homepage.startsWith("https://")));
});

test("aircraft positions expire 60 s after observation, counting edge-cache age but not a wrong browser clock", () => {
  const records = traffic.parseTraffic({ ac: [aircraft({ seen_pos: 10 }), aircraft({ hex: "b00001", seen_pos: 50 })] }).records;
  const received = Date.parse("2026-10-24T22:00:00Z");
  const load = (retrievedAt, receivedAt = received) => ({ retrievedAt, receivedAt, records });
  const fresh = load("2026-10-24T22:00:00Z");
  assert.equal(traffic.freshAircraft(fresh, received), records, "nothing expired: same array, so the map is not redrawn");
  assert.deepEqual(traffic.freshAircraft(fresh, received + 15_000).map(record => record.hex), ["a1b2c3"]);
  assert.equal(traffic.freshAircraft(fresh, received + 20_000), traffic.freshAircraft(fresh, received + 15_000), "an unchanged subset keeps its identity across expiry ticks");
  assert.deepEqual(traffic.freshAircraft(fresh, received + 55_000), []);
  assert.equal(traffic.freshAircraft(fresh, received + 55_000), traffic.freshAircraft(null, received), "every empty result is one shared array");
  // Served 20 s after retrieval from the edge cache: the 50 s position is already too old.
  assert.deepEqual(traffic.freshAircraft(load("2026-10-24T21:59:40Z"), received).map(record => record.hex), ["a1b2c3"]);
  // A browser clock an hour fast or slow counts at most the 30 s cache window, never an hour.
  assert.equal(traffic.freshAircraft(load("2026-10-24T21:00:00Z"), received).length, 1);
  assert.equal(traffic.freshAircraft(load("2026-10-24T23:00:00Z"), received), records);
  assert.deepEqual(traffic.freshAircraft(load("not a time"), received), []);
  assert.deepEqual(traffic.freshAircraft(null, received), []);
});

test("aircraft are tagged with the airspace they occupy at their altitude", () => {
  // Over Wichita: 4,000 MSL is inside the Class C (ceiling 5,300 MSL); 12,000 MSL is above it.
  assert.match(airspace.occupiedAirspace(context, -97.433, 37.65, 4000, 1333), /CLASS C · ICT/);
  assert.doesNotMatch(airspace.occupiedAirspace(context, -97.433, 37.65, 12000, 1333), /CLASS C/);
  assert.match(airspace.occupiedAirspace(context, -98.35, 38.5, 35000, 1700), /CLASS A/);
  const [feature] = traffic.trafficFeatures(traffic.parseTraffic({ ac: [aircraft()] }).records, () => 1333, 1, () => "CLASS C · ICT").features;
  assert.ok(Math.abs(feature.properties.base - (4100 - 1333) * 0.3048) < 1e-6);
  assert.equal(feature.properties.airspace, "CLASS C · ICT");
  assert.match(feature.properties.label, /SWA123 B738 · 4,100 ft · 210 kt/);
  const [grounded] = traffic.trafficFeatures(traffic.parseTraffic({ ac: [aircraft({ alt_baro: "ground", alt_geom: undefined })] }).records, () => 1333, 3, () => "unused").features;
  assert.equal(grounded.properties.base, 0); assert.equal(grounded.properties.airspace, "surface");
});

const cell = (lon, lat, ceiling, size = 0.0083) => ({ type: "Feature", properties: { CEILING: ceiling, APT1_FAAID: "SLN", APT1_NAME: "SALINA RGNL" },
  geometry: { type: "Polygon", coordinates: [[[lon, lat], [lon + size, lat], [lon + size, lat + size], [lon, lat + size], [lon, lat]]] } });

test("UAS Facility Map pages parse strictly, report paging, and give the lowest ceiling at a point", () => {
  const page = drone.parseUasfmPage({ type: "FeatureCollection", features: [cell(-97.66, 38.78, 0), cell(-97.65, 38.78, 200)], properties: { exceededTransferLimit: true } });
  assert.equal(page.cells.length, 2); assert.equal(page.more, true);
  assert.equal(drone.uasCeilingAt(page.cells, -97.655, 38.784).ceilingFt, 0);
  assert.equal(drone.uasCeilingAt(page.cells, -97.645, 38.784).ceilingFt, 200);
  assert.equal(drone.uasCeilingAt(page.cells, -97.0, 38.0), null);
  assert.equal(drone.parseUasfmPage({ type: "FeatureCollection", features: [] }).more, false);
  assert.throws(() => drone.parseUasfmPage({ error: { code: 400 } }), /FeatureCollection/);
  assert.throws(() => drone.parseUasfmPage({ type: "FeatureCollection", features: [{ ...cell(0, 0, 0), properties: { CEILING: 500 } }] }), /CEILING/);
  const url = new URL(drone.uasfmPageUrl(2));
  assert.equal(url.searchParams.get("resultOffset"), "4000"); assert.equal(url.searchParams.get("f"), "geojson");
  assert.throws(() => drone.uasfmPageUrl(drone.UASFM_MAX_PAGES), /out of range/);
  const [extruded] = drone.uasFeatures(page.cells, 1).features;
  assert.equal(extruded.properties.label, "0 ft"); assert.equal(extruded.properties.color, drone.UAS_CEILING_COLORS[0][1]);
  assert.ok(Math.abs(drone.uasFeatures(page.cells, 1).features[1].properties.top - 200 * 0.3048) < 1e-9);
});

test("TFR list accepts known field spellings and keeps Kansas entries", () => {
  const list = [{ notam_id: "6/1234", type: "HAZARDS", state: "KS", description: "WICHITA, KS, Saturday ..." },
    { notamId: "6/5678", type: "VIP", state: "DC", description: "WASHINGTON, DC" },
    { NOTAM_ID: "6/9999", DESCRIPTION: "15NM NE MANHATTAN, KS FIRE FIGHTING" }, { nothing: true }];
  const parsed = drone.parseTfrList(list);
  assert.equal(parsed.total, 3);
  assert.deepEqual(parsed.kansas.map(entry => entry.notam), ["6/1234", "6/9999"]);
  assert.equal(drone.parseTfrList({ tfrs: list }).total, 3);
  assert.throws(() => drone.parseTfrList({}), /not an array/);
  const regional = drone.parseTfrList([...list, { notam_id: "6/2222", state: "OK", description: "PONCA CITY, OK" }, { notam_id: "6/3333", state: "TX", description: "AUSTIN, TX" }]).regional;
  assert.deepEqual(regional.map(entry => entry.notam), ["6/1234", "6/9999", "6/2222"], "Kansas first, then neighbouring states");
  const many = Array.from({ length: 50 }, (_, index) => ({ notam_id: `6/${1000 + index}`, state: "MO", description: "KANSAS CITY, MO" }));
  assert.equal(drone.parseTfrList(many).regional.length, drone.TFR_MAX_DETAILS, "detail reads stay within the subrequest budget");
});

// Synthetic XNOTAM shaped like the FAA detail files (paths as read by OpenSectional's parser).
const tfrArea = ({ name = "WICHITA &amp; AREA", lower = ["HEI", "0", "FT"], upper = ["ALT", "3000", "FT"], vertices, schedule = "" }) => `
  <TFRAreaGroup>
    <aseTFRArea><txtName>${name}</txtName>
      <codeDistVerUpper>${upper[0]}</codeDistVerUpper><valDistVerUpper>${upper[1]}</valDistVerUpper><uomDistVerUpper>${upper[2]}</uomDistVerUpper>
      <codeDistVerLower>${lower[0]}</codeDistVerLower><valDistVerLower>${lower[1]}</valDistVerLower><uomDistVerLower>${lower[2]}</uomDistVerLower>${schedule}
    </aseTFRArea>
    <aseShapes><Avx><geoLat>10.0N</geoLat><geoLong>010.0E</geoLong></Avx></aseShapes>
    <abdMergedArea>${vertices.map(([lon, lat]) => `<Avx><geoLat>${Math.abs(lat)}${lat < 0 ? "S" : "N"}</geoLat><geoLong>${String(Math.abs(lon)).padStart(3, "0")}${lon < 0 ? "W" : "E"}</geoLong></Avx>`).join("")}</abdMergedArea>
  </TFRAreaGroup>`;
const square = (lon, lat, size) => [[lon, lat], [lon + size, lat], [lon + size, lat + size], [lon, lat + size]];
const xnotam = areas => `<?xml version="1.0" encoding="UTF-8"?><XNOTAM-Update><Group><Add><Not>
  <NotUid><txtLocalName>6/1234</txtLocalName></NotUid><dateEffective>2026-10-24T18:00:00</dateEffective><dateExpire>2026-10-25T02:00:00</dateExpire>
  <TfrNot><codeType>HAZARDS</codeType>${areas.join("")}</TfrNot></Not></Add></Group></XNOTAM-Update>`;

test("TFR detail files give boundaries and altitude limits for areas reaching Kansas", () => {
  const xml = xnotam([
    tfrArea({ vertices: square(-97.5, 37.6, 0.1) }),
    tfrArea({ name: "HIGH", lower: ["ALT", "3000", "FT"], upper: ["STD", "180", "FL"], vertices: square(-97.5, 37.6, 0.1),
      schedule: "<ScheduleGroup><dateEffective>2026-10-24T20:00:00</dateEffective><dateExpire>2026-10-24T22:00:00</dateExpire></ScheduleGroup>" }),
    tfrArea({ name: "FLORIDA", vertices: square(-81, 28, 0.1) }),
    tfrArea({ name: "BAD VERTEX", vertices: [[-97.5, 37.6], [-97.4, 37.6], [-97.4, 37.7]].map(([lon, lat], index) => index === 1 ? [lon, Number.NaN] : [lon, lat]) }),
    tfrArea({ name: "BAD ALTITUDE", upper: ["ALT", "lots", "FT"], vertices: square(-97.5, 37.6, 0.1) }),
  ]);
  const { shapes, unreadable } = drone.parseTfrDetail(xml, "6/1234");
  assert.deepEqual(shapes.map(shape => shape.name), ["WICHITA & AREA", "HIGH"]);
  assert.equal(unreadable, 2, "the malformed vertex and altitude areas are counted; the out-of-region area is not");
  const [low, high] = shapes;
  assert.deepEqual([low.floor, low.ceiling], [{ valueFt: 0, reference: "SFC" }, { valueFt: 3000, reference: "MSL" }]);
  assert.deepEqual(high.ceiling, { valueFt: 18000, reference: "FL" });
  assert.equal(low.type, "HAZARDS");
  assert.deepEqual([low.effective, low.expires], ["2026-10-24T18:00:00", "2026-10-25T02:00:00"]);
  assert.deepEqual([high.effective, high.expires], ["2026-10-24T20:00:00", "2026-10-24T22:00:00"], "an area schedule overrides the NOTAM times");
  assert.equal(low.ring.length, 5, "the boundary is closed");
  assert.ok(low.ring.every(([lon, lat]) => lon < -97 && lat > 37), "only abdMergedArea vertices are used, with W/N signs applied");
  assert.equal(drone.formatTfrLimit(high.ceiling), "FL180");
  assert.equal(drone.formatTfrLimit({ valueFt: 99999, reference: "UNL" }), "UNL");
  assert.equal(drone.parseTfrDetail(xnotam([tfrArea({ upper: ["ALT", "99999", "FT"], vertices: square(-97.5, 37.6, 0.1) })]), "6/1234").shapes[0].ceiling.reference, "UNL");
  assert.equal(drone.parseTfrDetail(xnotam([tfrArea({ lower: ["HEI", "400", "FT"], vertices: square(-97.5, 37.6, 0.1) })]), "6/1234").shapes[0].floor.reference, "AGL");
  assert.deepEqual(drone.parseTfrDetail(xnotam([]), "6/1234"), { shapes: [], unreadable: 1 }, "a NOTAM with no area is reported, not treated as clear");
  // A 20,001-vertex circle around Wichita: rejected whole and counted, never shortened into a different polygon.
  const circle = Array.from({ length: 20_001 }, (_, index) => [-97.43 + 0.2 * Math.cos(index / 20_001 * 2 * Math.PI), 37.65 + 0.2 * Math.sin(index / 20_001 * 2 * Math.PI)]);
  assert.deepEqual(drone.parseTfrDetail(xnotam([tfrArea({ vertices: circle })]), "6/1234"), { shapes: [], unreadable: 1 });
  assert.throws(() => drone.parseTfrDetail("<html>maintenance</html>", "6/1234"), /Not an XNOTAM/);
});

test("TFR detail URLs come only from well-formed NOTAM ids", () => {
  assert.equal(drone.tfrDetailUrl("6/1234"), "https://tfr.faa.gov/download/detail_6_1234.xml");
  for (const bad of ["../6/1234", "6/1234?x=1", "6_1234", "", "6/123456"]) assert.throws(() => drone.tfrDetailUrl(bad), /Unexpected NOTAM id/);
});

test("TFR volumes rise from floor to ceiling and the inspector finds the areas covering a point", () => {
  const [low, high] = drone.parseTfrDetail(xnotam([
    tfrArea({ vertices: square(-97.5, 37.6, 0.1) }),
    tfrArea({ name: "HIGH", lower: ["ALT", "3000", "FT"], upper: ["STD", "180", "FL"], vertices: square(-97.5, 37.6, 0.1) }),
  ]), "6/1234").shapes;
  const features = drone.tfrFeatures([low, high], () => 1333, 1).features;
  assert.equal(features[0].properties.base, 0);
  assert.ok(Math.abs(features[0].properties.top - (3000 - 1333) * 0.3048) < 1e-6);
  assert.ok(Math.abs(features[1].properties.base - (3000 - 1333) * 0.3048) < 1e-6);
  assert.ok(Math.abs(features[1].properties.top - (18000 - 1333) * 0.3048) < 1e-6);
  assert.equal(features[0].properties.label, "TFR 6/1234 HAZARDS · SFC–3,000 MSL");
  assert.ok(Math.abs(drone.tfrLimitAboveGround({ valueFt: 99999, reference: "UNL" }, 1333) - (60000 - 1333)) < 1e-9);
  assert.equal(drone.tfrsAtPoint([low, high], -97.45, 37.65).length, 2);
  assert.equal(drone.tfrsAtPoint([low, high], -97.2, 37.65).length, 0);
});

test("the TFR route reads detail files only through the guarded URL builder, within a deadline", async () => {
  const server = await readFile(new URL("../app/aviation-drone-server.ts", import.meta.url), "utf8");
  assert.match(server, /fetchText\(tfrDetailUrl\(notam\), "xml"/);
  assert.match(server, /if \(Date\.now\(\) > deadline\) \{ failed\+\+; continue; \}/, "late details are counted as missing, not awaited");
  assert.match(server, /detailsFailed: details\.failed/);
  assert.match(server, /if \(detail\.unreadable > 0\) failed\+\+;/, "a file with any unreadable area counts as not fully read");
});

// Hashing and parsing the pinned product takes a variable time under load, so
// component tests wait (boundedly) for a rendered state instead of counting renders.
const renderUntil = async (cycle, ready, what) => {
  for (let attempt = 0; attempt < 400; attempt++) { const tree = await cycle(); if (ready(tree)) return tree; }
  assert.fail(`timed out waiting for ${what}`);
};

test("the UAS grid request survives its own loading-state re-render and reaches ready", { timeout: 10_000 }, async () => {
  const { componentHarness, findNode, settle } = await import("./component-harness.mjs");
  const control = await import("node:fs/promises").then(fs => fs.readFile(new URL("../app/aviation-control.tsx", import.meta.url), "utf8"));
  assert.doesNotMatch(control, /\[visible, showUas, uas\.state\]/, "loading state must not be a dependency of its own request");
  let release, gridSignal;
  const pendingGrid = new Promise(resolve => { release = resolve; });
  const fetch = async (path, init) => {
    if (path === drone.UASFM_API_PATH) { gridSignal = init.signal; await pendingGrid; return { ok: true, path }; }
    if (path === airspace.AVIATION_CONTEXT_ASSET.url) return { ok: true, path, arrayBuffer: async () => bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength) };
    return { ok: false, path };
  };
  const readBoundedJson = async (response, _max, signal) => {
    if (signal?.aborted) throw new Error("aborted");
    return response.path === drone.UASFM_API_PATH
      ? { evidenceRole: "EXTERNAL_CONTEXT_ONLY", retrievedAt: "2026-10-24T00:00:00Z", cells: [{ ceilingFt: 200, airport: "SLN", airportName: null, bbox: [0, 0, 1, 1], ring: [[0, 0], [1, 0], [1, 1], [0, 0]] }] }
      : {};
  };
  const h = await componentHarness("app/aviation-control.tsx", {
    "./bounded-json": { readBoundedJson }, "./aviation-airspace": airspace, "./aviation-weather": weather, "./aviation-drone-data": drone, "./aviation-traffic": traffic,
    "./aviation-chart": chart, "./aviation-profile": profile, "./aviation-research": research, "./map-runtime": { unexaggeratedTerrainElevation: () => null },
  }, { fetch, setInterval, clearInterval, crypto: globalThis.crypto, TextDecoder });
  const props = { mapRef: { current: null }, styleReady: false };
  const cycle = async () => { const tree = h.render(h.exports.AviationControl, props); h.commit(); await new Promise(resolve => setTimeout(resolve, 5)); await settle(); return tree; };
  try {
  let tree = await cycle();
  findNode(tree, node => node.type === "input" && node.props["aria-label"] === "Show airspace and aviation layers").props.onChange({ target: { checked: true } });
  await cycle();          // effect schedules the grid read
  tree = await cycle();   // re-render with state "loading": the old code aborted here
  assert.ok(gridSignal && !gridSignal.aborted, "the in-flight grid request was not cancelled by its own loading state");
  release(); await settle();
  const status = tree => JSON.stringify(findNode(tree, node => node.type === "small" && JSON.stringify(node.props.children ?? "").includes("UAS Facility Map:")) ?? null);
  tree = await renderUntil(cycle, tree => /1 grid cells/.test(status(tree)), "the grid to reach ready");
  assert.match(status(tree), /1 grid cells/);
  } finally { release(); h.dispose(); }
});

test("turning traffic off and on never redraws the previous positions as current", { timeout: 10_000 }, async () => {
  const { componentHarness, findNode, settle } = await import("./component-harness.mjs");
  let trafficReads = 0, release;
  const fetch = async (path) => {
    if (path === traffic.AVIATION_TRAFFIC_API_PATH) {
      trafficReads++;
      if (trafficReads > 1) await new Promise(resolve => { release = resolve; });
      return { ok: true, path };
    }
    if (path === airspace.AVIATION_CONTEXT_ASSET.url) return { ok: true, path, arrayBuffer: async () => bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength) };
    return { ok: false, path };
  };
  const readBoundedJson = async (response, _max, signal) => {
    if (signal?.aborted) throw new Error("aborted");
    return response.path === traffic.AVIATION_TRAFFIC_API_PATH
      ? { evidenceRole: "EXTERNAL_CONTEXT_ONLY", retrievedAt: new Date().toISOString(), provider: traffic.TRAFFIC_PROVIDERS[0], records: traffic.parseTraffic({ ac: [aircraft()] }).records, dropped: 0, limitation: "" }
      : {};
  };
  const h = await componentHarness("app/aviation-control.tsx", {
    "./bounded-json": { readBoundedJson }, "./aviation-airspace": airspace, "./aviation-weather": weather, "./aviation-drone-data": drone, "./aviation-traffic": traffic,
    "./aviation-chart": chart, "./aviation-profile": profile, "./aviation-research": research, "./map-runtime": { unexaggeratedTerrainElevation: () => null },
  }, { fetch, setInterval, clearInterval, crypto: globalThis.crypto, TextDecoder });
  const props = { mapRef: { current: null }, styleReady: false };
  const cycle = async () => { const tree = h.render(h.exports.AviationControl, props); h.commit(); await new Promise(resolve => setTimeout(resolve, 5)); await settle(); return tree; };
  const status = tree => JSON.stringify(findNode(tree, node => node.type === "small" && JSON.stringify(node.props.children ?? "").includes("Traffic:")) ?? null);
  const trafficToggle = tree => findNode(findNode(tree, node => node.type === "label" && JSON.stringify(node.props.children ?? "").includes("Live aircraft (ADS-B)")), node => node.type === "input");
  try {
    let tree = await cycle();
    findNode(tree, node => node.type === "input" && node.props["aria-label"] === "Show airspace and aviation layers").props.onChange({ target: { checked: true } });
    tree = await renderUntil(cycle, tree => /\[1," aircraft · retrieved /.test(status(tree)), "the first traffic response");
    trafficToggle(tree).props.onChange({ target: { checked: false } });
    tree = await cycle();
    trafficToggle(tree).props.onChange({ target: { checked: true } });
    tree = await renderUntil(cycle, () => trafficReads === 2, "the second traffic request");
    tree = await cycle();
    assert.doesNotMatch(status(tree), /aircraft ·/, "the previous response is not shown while the new one is pending");
    assert.match(status(tree), /Checking/);
  } finally { release?.(); h.dispose(); }
});

test("switching to the 2D chart redraws every 3D form flat, with chart labels and a top-down camera", { timeout: 15_000 }, async () => {
  const { componentHarness, findNode, settle } = await import("./component-harness.mjs");
  const layers = new Map(), sources = new Map(), cameras = [];
  const map = {
    getLayer: id => layers.get(id), removeLayer: id => { layers.delete(id); }, addLayer: layer => { layers.set(layer.id, layer); },
    getSource: id => sources.get(id), removeSource: id => { sources.delete(id); }, addSource: (id, source) => { sources.set(id, source); },
    on() {}, off() {}, once() {}, getCanvas: () => ({ style: {} }), getBearing: () => -18, easeTo: options => { cameras.push(options); },
  };
  const fetch = async (path) => path === airspace.AVIATION_CONTEXT_ASSET.url
    ? { ok: true, path, arrayBuffer: async () => bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength) } : { ok: false, path };
  const h = await componentHarness("app/aviation-control.tsx", {
    "./bounded-json": { readBoundedJson: async () => ({}) }, "./aviation-airspace": airspace, "./aviation-weather": weather, "./aviation-drone-data": drone,
    "./aviation-traffic": traffic, "./aviation-chart": chart, "./aviation-profile": profile, "./aviation-research": research, "./map-runtime": { unexaggeratedTerrainElevation: () => null },
  }, { fetch, setInterval, clearInterval, crypto: globalThis.crypto, TextDecoder });
  const props = { mapRef: { current: map }, styleReady: true };
  const cycle = async () => { const tree = h.render(h.exports.AviationControl, props); h.commit(); await new Promise(resolve => setTimeout(resolve, 5)); await settle(); return tree; };
  const formTypes = () => Object.fromEntries([...layers.values()].filter(layer => layer.id.endsWith("-3d")).map(layer => [layer.id.replace("kfm-aviation-", ""), layer.type]));
  try {
    let tree = await cycle();
    findNode(tree, node => node.type === "input" && node.props["aria-label"] === "Show airspace and aviation layers").props.onChange({ target: { checked: true } });
    tree = await renderUntil(cycle, () => layers.has("kfm-aviation-airspace-3d"), "the aviation layers");
    assert.ok(Object.values(formTypes()).every(type => type === "fill-extrusion"), "3D draws extruded volumes");
    const radio = label => findNode(findNode(tree, node => node.type === "label" && JSON.stringify(node.props.children ?? "").includes(label)), node => node.type === "input");
    radio("2D chart").props.onChange({ target: { checked: true } });
    tree = await renderUntil(cycle, () => layers.get("kfm-aviation-airspace-3d")?.type === "fill", "the 2D chart layers");
    const forms = formTypes();
    assert.deepEqual(Object.keys(forms).sort(), ["airspace-3d", "ceilings-3d", "drone-3d", "pireps-3d", "tfr-3d", "traffic-3d", "uas-3d"]);
    assert.ok(Object.values(forms).every(type => type === "fill"), "every 3D form has a flat twin in 2D");
    // Compared as JSON: the harness realm's arrays have their own prototype.
    assert.equal(JSON.stringify(layers.get("kfm-aviation-airspace-label").layout["text-field"]), JSON.stringify(["get", "chart"]));
    assert.equal(cameras.at(-1).pitch, 0, "2D looks straight down");
    // Slicing at 2,000 ft MSL drops the Wichita Class C shelf (floor 2,700 MSL) and keeps its surface core.
    const slicer = findNode(tree, node => node.type === "select" && JSON.stringify(node.props.children ?? "").includes("Drone altitudes"));
    slicer.props.onChange({ target: { value: "2000" } });
    await renderUntil(cycle, () => !sources.get("kfm-aviation-airspace").data.features.some(feature => feature.properties.chart === "ICT 53/27"), "the 2,000 ft slice");
    assert.ok(sources.get("kfm-aviation-airspace").data.features.some(feature => feature.properties.chart === "ICT 53/SFC"));
    radio("3D volumes").props.onChange({ target: { checked: true } });
    await renderUntil(cycle, () => layers.get("kfm-aviation-airspace-3d")?.type === "fill-extrusion", "the 3D layers again");
    assert.equal(cameras.at(-1).pitch, 62, "3D tilts back so floors and ceilings show");
    assert.ok(sources.get("kfm-aviation-airspace").data.features.some(feature => feature.properties.chart === "ICT 53/27"), "the slice applies to the 2D chart only");
  } finally { h.dispose(); }
});

const msl = (limit, ground) => limit.reference === "SFC" ? ground : limit.reference === "AGL" ? ground + limit.value_ft : limit.value_ft;
const profileVolumes = (types) => context.volumes.filter(volume => types.includes(volume.type)).map(volume => ({ key: volume.id, label: airspace.airspaceLabel(volume),
  color: "#000", kind: "airspace", bbox: volume.bbox, rings: volume.rings, lowFt: ground => msl(volume.floor, ground), highFt: ground => msl(volume.ceiling, ground) }));

test("a side view across Wichita shows the Class C core from the ground and the shelf from 2,700 ft", () => {
  const points = profile.profilePath({ lon: -97.9, lat: 37.65 }, { lon: -96.95, lat: 37.65 }).map(point => ({ ...point, groundFt: 1333 }));
  assert.equal(points.length, profile.PROFILE_SAMPLES);
  assert.ok(Math.abs(points.at(-1).distanceNm - 45.1) < 0.5);
  const bands = profile.profileBands(points, profileVolumes(["CLASS_C"]));
  const core = bands.find(band => band.label === "CLASS C · ICT · SFC–5,300 MSL"), shelf = bands.find(band => band.label === "CLASS C · ICT · 2,700 MSL–5,300 MSL");
  assert.equal(core.segments.length, 1);
  // NASR charts the shelf as the full 10 NM circle over the 5 NM core, so the line crosses it once, around the core.
  assert.equal(shelf.segments.length, 1);
  assert.ok(core.segments[0].low.every(value => value === 1333) && core.segments[0].high.every(value => value === 5300), "the core runs from the ground to 5,300 MSL");
  assert.ok(shelf.segments[0].low.every(value => value === 2700));
  assert.ok(shelf.segments[0].from < core.segments[0].from && core.segments[0].to < shelf.segments[0].to, "the shelf reaches farther out than the core on both sides");
  // A ring with a hole is crossed twice, on either side of the hole.
  const ring = [[-97.7, 37.5], [-97.2, 37.5], [-97.2, 37.8], [-97.7, 37.8], [-97.7, 37.5]], hole = [[-97.5, 37.6], [-97.4, 37.6], [-97.4, 37.7], [-97.5, 37.7], [-97.5, 37.6]];
  const [annulus] = profile.profileBands(points, [{ key: "a", label: "ANNULUS", color: "#000", kind: "airspace", bbox: [-97.7, 37.5, -97.2, 37.8], rings: [ring, hole], lowFt: () => 3000, highFt: () => 4000 }]);
  assert.equal(annulus.segments.length, 2);
  assert.equal(bands[0], core, "bands are ordered bottom-up");
  const summary = profile.profileSummary(points, bands);
  assert.ok(summary.some(line => /^CLASS C · ICT · SFC–5,300 MSL, \d+\.\d to \d+\.\d NM$/.test(line)));
  // A floor below the ground starts at the ground; an MSL ceiling below a high ground still never inverts.
  const [low] = profile.profileBands(points.map(point => ({ ...point, groundFt: 3000 })), profileVolumes(["CLASS_C"])).filter(band => band.label.includes("2,700"));
  assert.ok(low.segments[0].low.every(value => value === 3000));
});

test("side-view geometry: path limits and aircraft near the line", () => {
  assert.throws(() => profile.profilePath({ lon: -97, lat: 38 }, { lon: -97, lat: 38 }), /two distinct points/);
  assert.throws(() => profile.profilePath({ lon: -102, lat: 37 }, { lon: -94, lat: 40 }), /within 320 NM/);
  const a = { lon: -98, lat: 38 }, b = { lon: -97, lat: 38 };
  assert.ok(Math.abs(profile.alongTrackNm(a, b, -97.5, 38.01) - 23.7) < 0.3, "about halfway, 1 km off the line");
  assert.equal(profile.alongTrackNm(a, b, -97.5, 38.1), null, "11 km off the line");
  assert.equal(profile.alongTrackNm(a, b, -96.9, 38), null, "beyond B");
});

test("drawing a side view with two map clicks renders the cross-section and its text list", { timeout: 15_000 }, async () => {
  const { componentHarness, findNode, settle } = await import("./component-harness.mjs");
  const layers = new Map(), sources = new Map();
  let click = null;
  const map = {
    getLayer: id => layers.get(id), removeLayer: id => { layers.delete(id); }, addLayer: layer => { layers.set(layer.id, layer); },
    getSource: id => sources.get(id), removeSource: id => { sources.delete(id); }, addSource: (id, source) => { sources.set(id, source); },
    on() {}, off() { click = null; }, once: (type, handler) => { if (type === "click") click = handler; }, getCanvas: () => ({ style: {} }), getBearing: () => 0, easeTo() {},
  };
  const fetch = async (path) => path === airspace.AVIATION_CONTEXT_ASSET.url
    ? { ok: true, path, arrayBuffer: async () => bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength) } : { ok: false, path };
  const h = await componentHarness("app/aviation-control.tsx", {
    "./bounded-json": { readBoundedJson: async () => ({}) }, "./aviation-airspace": airspace, "./aviation-weather": weather, "./aviation-drone-data": drone,
    "./aviation-traffic": traffic, "./aviation-chart": chart, "./aviation-profile": profile, "./aviation-research": research, "./map-runtime": { unexaggeratedTerrainElevation: () => null },
  }, { fetch, setInterval, clearInterval, crypto: globalThis.crypto, TextDecoder });
  const props = { mapRef: { current: map }, styleReady: true };
  const cycle = async () => { const tree = h.render(h.exports.AviationControl, props); h.commit(); await new Promise(resolve => setTimeout(resolve, 5)); await settle(); return tree; };
  const button = (tree, text) => findNode(tree, node => node.type === "button" && JSON.stringify(node.props.children ?? "").includes(text));
  try {
    let tree = await cycle();
    findNode(tree, node => node.type === "input" && node.props["aria-label"] === "Show airspace and aviation layers").props.onChange({ target: { checked: true } });
    tree = await renderUntil(cycle, tree => Boolean(button(tree, "Draw a side view")), "the aviation panel");
    button(tree, "Draw a side view").props.onClick();
    tree = await renderUntil(cycle, () => typeof click === "function", "the first click handler");
    click({ lngLat: { lng: -97.9, lat: 37.65 } });
    tree = await renderUntil(cycle, tree => Boolean(button(tree, "Now click point B")) && typeof click === "function", "the second click handler");
    click({ lngLat: { lng: -96.95, lat: 37.65 } });
    tree = await renderUntil(cycle, tree => Boolean(findNode(tree, node => node.type === "figure")), "the side view");
    const figure = JSON.stringify(findNode(tree, node => node.type === "figure"));
    assert.match(figure, /Side view A→B/);
    assert.match(figure, /CLASS C · ICT · SFC–5,300 MSL, \d+\.\d to \d+\.\d NM/);
    assert.match(figure, /nearest facility['’]s elevation \(turn on 3D terrain/, "without loaded terrain the ground source is named");
    // The harness renders shallowly; the chart is a pure component, so render its element directly.
    const chartElement = findNode(tree, node => typeof node.type === "function" && node.type.name === "ProfileChart");
    const svg = findNode(chartElement.type(chartElement.props), node => node.type === "svg");
    assert.match(svg.props["aria-label"], /^Side view from A to B, \d+\.\d nautical miles, altitude in feet MSL$/);
    assert.match(JSON.stringify(svg), /drone ceiling 400 ft AGL/);
    assert.match(JSON.stringify(svg), /Class A from FL180/);
    await renderUntil(cycle, () => sources.get("kfm-aviation-profile")?.data.features.length === 3, "the A–B line on the map");
    button(tree, "Clear side view").props.onClick();
    tree = await renderUntil(cycle, tree => !findNode(tree, node => node.type === "figure"), "the cleared side view");
  } finally { h.dispose(); }
});

const metarAt = (station, lon, lat) => ({ station, name: "SALINA RGNL", lon, lat, observedAt: "2026-10-25T08:53:00.000Z", flightCategory: "VFR" });

test("aviation joins the Near-here dossier with public-use airports and weather stations only", () => {
  const records = research.aviationResearchPoints({ airports: context.airports, nasrCycle: context.nasrCycle, validFrom: context.validFrom, validToExclusive: context.validToExclusive,
    metars: [metarAt("KSLN", -97.65, 38.79)], metarRetrievedAt: "2026-10-25T09:00:00.000Z" });
  assert.ok(records.length > 150 && records.every(dossier.validResearchRecord), "every record passes the dossier's own validator");
  const airports = records.filter(record => record.sourceId === research.AVIATION_RESEARCH_SOURCE.airports);
  assert.equal(airports.length, context.airports.filter(airport => airport.use === "PUBLIC").length, "private-use strips stay out of the 50-record dossier");
  const anchor = { kind: "provider", sourceId: "test", featureId: "anchor", title: "Salina", coordinates: [-97.61, 38.84], sourceTitle: "Test", sourceUrl: null,
    sourceTime: "now", retrievedAt: null, evidenceLabel: "EXTERNAL_CONTEXT_ONLY", limitation: "Test anchor." };
  const near = dossier.nearbyResearch(anchor, records, 25).records.map(record => record.featureId);
  assert.ok(near.includes("airport:SLN") && near.includes("metar:KSLN"), "a Salina dossier lists the airport and its weather station");
  assert.match(records.find(record => record.featureId === "metar:KSLN").title, /KSLN SALINA RGNL weather station · VFR/);
  assert.match(records.find(record => record.featureId === "airport:SLN").title, /\(KSLN\) · public-use airport, towered · 1,288 ft$/);
});

test("the aviation layer offers dossier points while shown and withdraws them when hidden; the page feeds them to Near here", { timeout: 15_000 }, async () => {
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  assert.match(page, /<AviationControl [^>]*onResearchRecords=\{setAviationResearch\}/);
  assert.match(page, /if \(aviationResearch\) \{[\s\S]*?records\.push\(\.\.\.points\);[\s\S]*?sourceId: "aviation-context"/);
  assert.match(page, /\}, \[aviationResearch, mapEvidenceFilter,/);
  const { componentHarness, findNode, settle } = await import("./component-harness.mjs");
  const offered = [];
  const fetch = async (path) => path === airspace.AVIATION_CONTEXT_ASSET.url
    ? { ok: true, path, arrayBuffer: async () => bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength) } : { ok: false, path };
  const h = await componentHarness("app/aviation-control.tsx", {
    "./bounded-json": { readBoundedJson: async () => ({}) }, "./aviation-airspace": airspace, "./aviation-weather": weather, "./aviation-drone-data": drone,
    "./aviation-traffic": traffic, "./aviation-chart": chart, "./aviation-profile": profile, "./aviation-research": research, "./map-runtime": { unexaggeratedTerrainElevation: () => null },
  }, { fetch, setInterval, clearInterval, crypto: globalThis.crypto, TextDecoder });
  const props = { mapRef: { current: null }, styleReady: false, onResearchRecords: records => offered.push(records) };
  const cycle = async () => { const tree = h.render(h.exports.AviationControl, props); h.commit(); await new Promise(resolve => setTimeout(resolve, 5)); await settle(); return tree; };
  const toggle = tree => findNode(tree, node => node.type === "input" && /aviation layers$/.test(node.props["aria-label"] ?? ""));
  try {
    let tree = await cycle();
    assert.equal(offered.at(-1), null, "nothing is offered while hidden");
    toggle(tree).props.onChange({ target: { checked: true } });
    tree = await renderUntil(cycle, () => Array.isArray(offered.at(-1)) && offered.at(-1).length > 150, "the offered airports");
    assert.ok(offered.at(-1).every(dossier.validResearchRecord));
    toggle(tree).props.onChange({ target: { checked: false } });
    await renderUntil(cycle, () => offered.at(-1) === null, "the withdrawn records");
  } finally { h.dispose(); }
});
