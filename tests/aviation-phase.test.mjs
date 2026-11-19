import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const compileModule = async (name) => {
  const source = await readFile(new URL(`../app/${name}.ts`, import.meta.url), "utf8");
  const output = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 }, fileName: `${name}.ts` }).outputText;
  return import(`data:text/javascript;base64,${Buffer.from(output).toString("base64")}`);
};

const phase = await compileModule("aviation-phase");
const types = await compileModule("aircraft-types");
const traffic = await compileModule("aviation-traffic");
const airspace = await compileModule("aviation-airspace");
const context = airspace.parseAviationContext(JSON.parse(await readFile(new URL("../public/data/aviation/kansas-aviation-context.json", import.meta.url), "utf8")));
const facilities = airspace.groundAnchors(context.airports).filter(airport => airport.use === "PUBLIC");
const SLN = facilities.find(airport => airport.faa_id === "SLN");

// Synthetic observations: no real aircraft identifiers are fixtures.
const plane = (changes = {}) => ({ hex: "a00001", callsign: "TEST1", registration: null, type: "C172", category: null, lon: SLN.lon, lat: SLN.lat + 5 / 60,
  onGround: false, altBaroFt: 2400, altGeomFt: 2500, groundSpeedKt: 90, trackDeg: 180, verticalRateFpm: -600, squawk: null, emergency: null, positionAgeS: 1, military: false, ...changes });

test("observed phase is derived from the surface flag, vertical rate and height above the nearest public-use facility", () => {
  const low = phase.observedPhase(plane(), facilities);
  assert.equal(low.kind, "low-near");
  assert.equal(low.label, "low near KSLN, descending");
  assert.equal(low.facility, "KSLN");
  assert.equal(low.aboveFieldFt, Math.round(2500 - SLN.elevation_ft), "about 1,212 ft above the 1,288 ft field");
  assert.ok(Math.abs(low.distanceNm - 5) < 0.1);
  assert.match(low.basis, /WGS84 geometric height/);
  assert.match(low.basis, /Not an arrival or departure statement/);
  assert.equal(phase.observedPhase(plane({ onGround: true, altBaroFt: 0, altGeomFt: null }), facilities).label, "on surface");
  assert.match(phase.observedPhase(plane({ onGround: true, altBaroFt: 0, altGeomFt: null }), facilities).basis, /surface flag/);
  // High and fast: plain climbing / level / descending from the reported rate alone.
  assert.equal(phase.observedPhase(plane({ altGeomFt: 31000, altBaroFt: 30000, verticalRateFpm: 1200 }), facilities).label, "climbing");
  assert.equal(phase.observedPhase(plane({ altGeomFt: 31000, altBaroFt: 30000, verticalRateFpm: 64 }), facilities).label, "level");
  assert.equal(phase.observedPhase(plane({ altGeomFt: 31000, altBaroFt: 30000, verticalRateFpm: -1500 }), facilities).label, "descending");
  const level = phase.observedPhase(plane({ altGeomFt: 31000, altBaroFt: 30000, verticalRateFpm: 64 }), facilities);
  assert.match(level.basis, /within ±300 ft\/min/);
  // Just above the 3,000 ft envelope over the same field: plain "descending", with the height still stated.
  const above = phase.observedPhase(plane({ altGeomFt: Math.round(SLN.elevation_ft) + 3200, altBaroFt: Math.round(SLN.elevation_ft) + 3100 }), facilities);
  assert.equal(above.kind, "descending");
  assert.ok(above.aboveFieldFt >= 3199 && above.aboveFieldFt <= 3201);
  assert.match(above.basis, /above KSLN, 5 NM away/);
  // 12 NM out at 1,200 ft: low, but not within 10 NM of the only listed field.
  const far = phase.observedPhase(plane({ lat: SLN.lat + 12 / 60, altGeomFt: Math.round(SLN.elevation_ft) + 1200, altBaroFt: Math.round(SLN.elevation_ft) + 1100 }), [SLN]);
  assert.ok(far.distanceNm > 10, `${far.distanceNm} NM from ${far.facility}`);
  assert.equal(far.kind, "descending");
  // The same position against every public-use field finds the nearer one (45K, Salina area) and says so.
  const nearer = phase.observedPhase(plane({ lat: SLN.lat + 12 / 60, altGeomFt: Math.round(SLN.elevation_ft) + 1200, altBaroFt: Math.round(SLN.elevation_ft) + 1100 }), facilities);
  assert.notEqual(nearer.facility, "KSLN");
  assert.match(nearer.basis, new RegExp(`${nearer.facility}`));
});

test("missing measurements stay unknown instead of becoming a phase", () => {
  const noRate = phase.observedPhase(plane({ verticalRateFpm: null, altGeomFt: 31000, altBaroFt: 30000 }), facilities);
  assert.equal(noRate.kind, "unknown");
  assert.equal(noRate.label, "phase not derivable");
  assert.match(noRate.basis, /vertical rate not reported/);
  const noHeight = phase.observedPhase(plane({ altGeomFt: null, altBaroFt: null, verticalRateFpm: -600 }), facilities);
  assert.equal(noHeight.kind, "descending", "a rate without a height is still a rate");
  assert.equal(noHeight.aboveFieldFt, null);
  assert.match(noHeight.basis, /no altitude reported/);
  const noFacilities = phase.observedPhase(plane(), []);
  assert.equal(noFacilities.kind, "descending");
  assert.equal(noFacilities.facility, null);
  assert.equal(phase.verticalTrend(null), null);
  assert.equal(phase.verticalTrend(299), "level");
  assert.equal(phase.verticalTrend(-300), "descending");
});

test("the map label and feature carry the observed phase, introduced as such", () => {
  const raw = { hex: "a00001", flight: "TEST1", t: "C172", lat: SLN.lat + 5 / 60, lon: SLN.lon, alt_baro: 2400, alt_geom: 2500, gs: 90, track: 180, baro_rate: -600, seen_pos: 1 };
  const { records } = traffic.parseTraffic({ ac: [raw] });
  const [feature] = traffic.trafficFeatures(records, () => SLN.elevation_ft, 1, () => "", aircraft => phase.observedPhase(aircraft, facilities).label).features;
  assert.match(feature.properties.label, /TEST1 C172 · 2,500 ft WGS84 · 90 kt · observed phase: low near KSLN, descending$/);
  assert.equal(feature.properties.phase, "low near KSLN, descending");
  assert.doesNotMatch(feature.properties.label, /landing|arriving|en route|destination/i);
  const [plain] = traffic.trafficFeatures(records, () => SLN.elevation_ft, 1, () => "").features;
  assert.doesNotMatch(plain.properties.label, /observed phase/, "without a phase function the label is unchanged");
  assert.equal(plain.properties.phase, "");
});

test("the static ICAO type table decodes common designators and leaves unknown codes raw", () => {
  assert.ok(types.AIRCRAFT_TYPES.size >= 120, `${types.AIRCRAFT_TYPES.size} designators`);
  assert.deepEqual(types.decodeAircraftType("B738"), { code: "B738", manufacturer: "Boeing", model: "737-800", engine: "jet", wake: "M" });
  assert.equal(types.decodeAircraftType("c172").model, "172 Skyhawk", "lookup is case-insensitive");
  assert.equal(types.decodeAircraftType("A388").wake, "J");
  assert.equal(types.decodeAircraftType("R44").engine, "piston helicopter");
  assert.equal(types.decodeAircraftType("ZZZZ"), null);
  assert.equal(types.decodeAircraftType(null), null);
  assert.equal(types.aircraftTypeLine("B738"), "B738 · Boeing 737-800 · jet · medium wake (static table)");
  assert.equal(types.aircraftTypeLine("ZZZZ"), "ZZZZ · designator not in the static table");
  assert.equal(types.aircraftTypeLine(null), "Aircraft type not reported");
  for (const [code, info] of types.AIRCRAFT_TYPES) {
    assert.equal(code, info.code);
    assert.match(code, /^[A-Z0-9]{2,4}$/, code);
    assert.ok(["L", "M", "H", "J"].includes(info.wake), code);
    assert.ok(info.manufacturer && info.model, code);
  }
  assert.match(types.AIRCRAFT_TYPE_SOURCE, /Doc 8643/);
});
