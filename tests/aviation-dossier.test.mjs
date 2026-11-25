import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

// Modules with runtime imports of sibling app modules are compiled with those imports rewritten to data URLs.
const linked = new Map();
async function compileLinked(name) {
  if (linked.has(name)) return linked.get(name);
  const source = await readFile(new URL(`../app/${name}.ts`, import.meta.url), "utf8");
  let output = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 }, fileName: `${name}.ts` }).outputText;
  for (const match of [...output.matchAll(/from "\.\/([a-z0-9-]+)"/g)]) output = output.replace(match[0], `from "${await compileLinked(match[1])}"`);
  const url = `data:text/javascript;base64,${Buffer.from(output).toString("base64")}`;
  linked.set(name, url);
  return url;
}
const load = async name => import(await compileLinked(name));

const bounded = await load("bounded-json");
const dossier = await load("aviation-dossier");
const phase = await load("aviation-phase");
const types = await load("aircraft-types");
const weather = await load("aviation-weather");
const airspace = await load("aviation-airspace");
const traffic = await load("aviation-traffic");
const drone = await load("aviation-drone-data");
const chart = await load("aviation-chart");
const profile = await load("aviation-profile");
const research = await load("aviation-research");
const bytes = await readFile(new URL("../public/data/aviation/kansas-aviation-context.json", import.meta.url));
const context = airspace.parseAviationContext(JSON.parse(bytes.toString("utf8")));
const SLN = context.airports.find(airport => airport.faa_id === "SLN");
const NOW = Date.parse("2026-11-06T18:00:00Z");

// Synthetic observations around Salina: no real aircraft identifiers are fixtures.
const northOfField = { lat: SLN.lat + 5 / 60, lon: SLN.lon };
const plane = (changes = {}) => ({ hex: "a00001", callsign: "TEST1", registration: null, type: "C172", category: null, ...northOfField, onGround: false, altBaroFt: 2400, altGeomFt: 2500,
  groundSpeedKt: 90, trackDeg: 180, verticalRateFpm: -600, squawk: null, emergency: null, positionAgeS: 1, military: false, observedAt: new Date(NOW - 8000).toISOString(), ...changes });

test("the activity board keeps aircraft within 10 NM and 3,000 ft of the field and groups them by reported rate and track", () => {
  const board = dossier.activityBoard(SLN, [
    plane(),
    plane({ hex: "a00002", callsign: "TEST2", trackDeg: 355, verticalRateFpm: 900, altGeomFt: 2200, altBaroFt: 2100 }),
    plane({ hex: "a00003", callsign: "TEST3", lon: SLN.lon, lat: SLN.lat, onGround: true, altBaroFt: 0, altGeomFt: null, verticalRateFpm: null, trackDeg: null }),
    plane({ hex: "a00004", callsign: "TEST4", verticalRateFpm: 0, trackDeg: 90 }),
    plane({ hex: "a00005", callsign: "TEST5", verticalRateFpm: -900, trackDeg: 90 }),
    plane({ hex: "a00006", callsign: "HIGH", altGeomFt: 9000, altBaroFt: 8900 }),
    plane({ hex: "a00007", callsign: "FAR", lat: SLN.lat + 20 / 60 }),
    plane({ hex: "a00008", callsign: "NOALT", altGeomFt: null, altBaroFt: null }),
  ], NOW);
  assert.deepEqual(board.rows.map(row => row.label).sort(), ["TEST1", "TEST2", "TEST3", "TEST4", "TEST5"], "too high, too far and unknown height are left out");
  assert.deepEqual(board.groups["descending-toward"].map(row => row.label), ["TEST1"]);
  assert.deepEqual(board.groups["climbing-away"].map(row => row.label), ["TEST2"]);
  assert.deepEqual(board.groups["on-surface"].map(row => row.label), ["TEST3"]);
  assert.deepEqual(board.groups["other-low"].map(row => row.label).sort(), ["TEST4", "TEST5"], "level, and descending while crossing, are not 'toward'");
  const toward = board.groups["descending-toward"][0];
  assert.equal(toward.bearingToFieldDeg, 180);
  assert.ok(toward.aboveFieldFt > 1100 && toward.aboveFieldFt < 1300);
  assert.equal(toward.observationAgeS, 8);
  assert.match(toward.basis, /rate -600 ft\/min; track 180° vs bearing to field 180°; 1,21\d ft above field \(WGS84 geometric\)/);
  assert.equal(board.groups["on-surface"][0].aboveFieldFt, 0);
  assert.equal(board.groups["on-surface"][0].basis, "Reported surface flag.");
  assert.equal(board.truncated, false);
  assert.match(dossier.ACTIVITY_BASIS, /no arrival, departure or destination is known/);
  for (const title of Object.values(dossier.ACTIVITY_GROUP_TITLES)) assert.doesNotMatch(title, /arriv|depart|landing|takeoff/i);
  assert.equal(dossier.activityBoard(SLN, [], NOW).rows.length, 0);
  const many = Array.from({ length: 60 }, (_, index) => plane({ hex: (index + 1).toString(16).padStart(6, "0"), callsign: `T${index}` }));
  const capped = dossier.activityBoard(SLN, many, NOW);
  assert.equal(capped.rows.length, dossier.ACTIVITY_MAX_ROWS);
  assert.equal(capped.truncated, true);
});

test("bearings and heading tolerance", () => {
  assert.ok(Math.abs(dossier.bearingDeg(-97.65, 38.8, -97.65, 38.7) - 180) < 0.01);
  assert.ok(Math.abs(dossier.bearingDeg(-97.65, 38.8, -97.5, 38.8) - 90) < 0.2);
  assert.equal(dossier.angleDiffDeg(350, 10), 20);
  assert.equal(dossier.angleDiffDeg(180, 0), 180);
});

const square = (lon, lat, size) => [[lon, lat], [lon + size, lat], [lon + size, lat + size], [lon, lat + size], [lon, lat]];
const shape = (ring, name = "AREA") => ({ notam: "6/1234", type: "HAZARDS", name, floor: { valueFt: 0, reference: "SFC" }, ceiling: { valueFt: 3000, reference: "MSL" }, effective: null, expires: null, ring,
  bbox: [Math.min(...ring.map(p => p[0])), Math.min(...ring.map(p => p[1])), Math.max(...ring.map(p => p[0])), Math.max(...ring.map(p => p[1]))] });

test("TFR areas touch an airport when they contain the field or a runway end, or come within 3 NM", () => {
  const over = shape(square(SLN.lon - 0.05, SLN.lat - 0.05, 0.1), "OVER");
  const runwayEnd = SLN.runways[0].ends[0];
  const endOnly = shape(square(runwayEnd.lon - 0.002, runwayEnd.lat - 0.002, 0.004), "END");
  const near = shape(square(SLN.lon + 0.03, SLN.lat + 0.03, 0.01), "NEAR");
  const far = shape(square(SLN.lon + 0.5, SLN.lat + 0.5, 0.1), "FAR");
  assert.deepEqual(dossier.tfrsTouchingAirport(SLN, [over, endOnly, near, far]).map(item => item.name), ["OVER", "END", "NEAR"]);
  assert.deepEqual(dossier.tfrsTouchingAirport(SLN, []), []);
});

test("runway and tower text come straight from NASR fields", () => {
  assert.deepEqual(SLN.runways.map(dossier.runwayLine), [
    "04/22 · 3,648 × 75 ft · asphalt", "12/30 · 6,510 × 100 ft · asphalt · medium lighting", "17/35 · 12,301 × 150 ft · asphalt/concrete · high lighting", "18/36 · 4,301 × 75 ft · asphalt",
  ].map((line, index) => line.replace(/ × \d+ ft/, SLN.runways[index].width_ft ? ` × ${SLN.runways[index].width_ft.toLocaleString("en-US")} ft` : " ft")));
  assert.equal(dossier.runwaySurfaceText("TURF-GRVL"), "turf/gravel");
  assert.equal(dossier.runwaySurfaceText(null), "surface not listed");
  assert.equal(dossier.towerText(SLN), "Towered (ATCT)");
  assert.equal(dossier.towerText({ tower: "NON-ATCT", ctaf_mhz: 122.8 }), "Non-towered, CTAF 122.800 MHz");
  assert.equal(dossier.towerText({ tower: null, ctaf_mhz: null }), "Non-towered, CTAF not listed");
});

// Shaped like the live AWC `taf` JSON (read 2026-11-06): times are Unix seconds, visib may be "6+".
const unix = ms => Math.floor(ms / 1000);
const taf = (changes = {}) => ({ icaoId: "KSLN", issueTime: "2026-11-06T17:23:00.000Z", validTimeFrom: unix(NOW - 3600000), validTimeTo: unix(NOW + 23 * 3600000),
  rawTAF: "TAF KSLN 061723Z 0618/0718 01006KT P6SM BKN025 FM070700 15004KT 2SM BR OVC005", lat: SLN.lat, lon: SLN.lon, elev: 393, name: "Salina Rgnl", mostRecent: 1,
  fcsts: [
    { timeFrom: unix(NOW - 3600000), timeTo: unix(NOW + 13 * 3600000), fcstChange: null, probability: null, wdir: 10, wspd: 6, wgst: null, visib: "6+", clouds: [{ cover: "BKN", base: 2500 }] },
    { timeFrom: unix(NOW + 2 * 3600000), timeTo: unix(NOW + 4 * 3600000), fcstChange: "TEMPO", probability: null, wdir: null, wspd: null, visib: 4, clouds: [{ cover: "OVC", base: 1500 }] },
    { timeFrom: unix(NOW + 13 * 3600000), timeTo: unix(NOW + 23 * 3600000), fcstChange: "FM", probability: null, wdir: 150, wspd: 4, visib: 2, wxString: "BR", clouds: [{ cover: "OVC", base: 500 }] },
  ], ...changes });

test("TAF parsing keeps the latest current forecast per station with a flight category per period", () => {
  const { records, dropped } = weather.parseTafs([taf(), taf({ issueTime: "2026-11-06T11:20:00.000Z", rawTAF: "older" }), taf({ icaoId: "KDEN", lat: 39.8, lon: -104.6 }),
    taf({ validTimeTo: unix(NOW - 60000) }), taf({ issueTime: "2026-11-04T17:23:00.000Z" }), taf({ fcsts: [] }), { junk: true }], NOW);
  assert.equal(records.length, 1);
  assert.equal(dropped, 5, "out of region, expired, issued over 30 h ago, no periods, malformed");
  const [record] = records;
  assert.equal(record.station, "KSLN");
  assert.match(record.raw, /^TAF KSLN/);
  assert.equal(record.periods.length, 3);
  assert.deepEqual(record.periods.map(period => [period.change, period.flightCategory]), [[null, "MVFR"], ["TEMPO", "MVFR"], ["FM", "IFR"]], "a 500 ft ceiling is IFR; LIFR starts below 500 ft");
  assert.deepEqual([record.periods[0].visibilitySm, record.periods[0].visibilityAtLeast], [6, true]);
  assert.equal(record.periods[2].weather, "BR");
  assert.equal(record.periods[2].ceilingFtAgl, 500);
  const outlook = weather.tafOutlook(record, NOW, 12);
  assert.deepEqual(outlook.map(entry => [entry.period.change, entry.current]), [[null, true], ["TEMPO", false]], "the FM period 13 h out is beyond the 12 h window");
  assert.deepEqual(weather.tafOutlook(record, NOW + 3 * 3600000, 12).map(entry => entry.current), [true, true, false], "a TEMPO overlays the base period");
  assert.equal(weather.tafTimeText("2026-11-07T07:00:00.000Z"), "07/07Z");
  assert.throws(() => weather.parseTafs({}, NOW), /not a list/);
  assert.equal(weather.AVIATION_TAF_API_PATH, "/api/aviation/taf");
});

test("the TAF route follows the METAR pattern: fixed AWC URL, no caller input, two-minute cache", async () => {
  const server = await readFile(new URL("../app/aviation-weather-server.ts", import.meta.url), "utf8");
  assert.match(server, /taf: \{ url: `\$\{AWC_API_BASE\}\/taf\?bbox=\$\{AWC_KANSAS_BBOX\}&format=json`/);
  assert.match(server, /kind === "taf" \? parseTafs\(payload, now\)/);
  const handler = await readFile(new URL("../app/api/aviation/taf/route.ts", import.meta.url), "utf8");
  assert.match(handler, /export async function GET\(\)/);
  assert.match(handler, /cachedAviationRoute\("taf", 120_000/);
  assert.doesNotMatch(handler, /searchParams|nextUrl|NextRequest/);
});

const renderUntil = async (cycle, ready, what) => {
  for (let attempt = 0; attempt < 400; attempt++) { const tree = await cycle(); if (ready(tree)) return tree; }
  assert.fail(`timed out waiting for ${what}`);
};
const text = node => typeof node === "object" && node ? [node.props?.children].flat(Infinity).map(text).join("") : String(node ?? "");

test("choosing a public-use airport opens a dossier with runways, weather, forecast, TFRs and the observed activity board", { timeout: 20_000 }, async () => {
  const { componentHarness, findNode, settle } = await import("./component-harness.mjs");
  const now = Date.now();
  const liveTaf = taf({ validTimeFrom: unix(now - 3600000), validTimeTo: unix(now + 23 * 3600000), issueTime: new Date(now - 3600000).toISOString(), fcsts: [
    { timeFrom: unix(now - 3600000), timeTo: unix(now + 5 * 3600000), fcstChange: null, wdir: 10, wspd: 6, visib: "6+", clouds: [{ cover: "BKN", base: 2500 }] },
    { timeFrom: unix(now + 5 * 3600000), timeTo: unix(now + 23 * 3600000), fcstChange: "FM", wdir: 150, wspd: 4, visib: 2, wxString: "BR", clouds: [{ cover: "OVC", base: 500 }] }] });
  const metar = { icaoId: "KSLN", name: "Salina Rgnl", lat: SLN.lat, lon: SLN.lon, elev: 393, obsTime: unix(now - 600000), rawOb: "METAR KSLN SYNTHETIC 18012KT 10SM BKN025 21/09 A2990", temp: 21, dewp: 9, wdir: 180, wspd: 12, visib: "10+", altim: 1012.5, clouds: [{ cover: "BKN", base: 2500 }] };
  const ac = [
    { hex: "a00001", flight: "TEST1", t: "C172", ...northOfField, alt_baro: 2400, alt_geom: 2500, gs: 90, track: 180, baro_rate: -600, seen_pos: 1 },
    { hex: "a00002", flight: "TEST2", t: "B738", lat: SLN.lat, lon: SLN.lon, alt_baro: "ground", gs: 5, track: 170, seen_pos: 1 },
  ];
  const tfrShape = shape(square(SLN.lon - 0.05, SLN.lat - 0.05, 0.1), "SALINA AREA");
  const envelope = records => ({ evidenceRole: "EXTERNAL_CONTEXT_ONLY", retrievedAt: new Date().toISOString(), sourceTitle: "test", sourceUrl: "https://example.invalid/", records, dropped: 0, limitation: "" });
  const fetch = async path => path === airspace.AVIATION_CONTEXT_ASSET.url
    ? new Response(bytes) : { ok: true, path };
  const readBoundedJson = async (response, _max, signal) => {
    if (signal?.aborted) throw new Error("aborted");
    switch (response.path) {
      case weather.AVIATION_METAR_API_PATH: return envelope(weather.parseMetars([metar], Date.now()).records);
      case weather.AVIATION_TAF_API_PATH: return envelope(weather.parseTafs([liveTaf], Date.now()).records);
      case weather.AVIATION_PIREP_API_PATH: return envelope([]);
      case traffic.AVIATION_TRAFFIC_API_PATH: return { ...envelope(traffic.parseTraffic({ ac }).records), provider: traffic.TRAFFIC_PROVIDERS[0] };
      case drone.TFR_API_PATH: return { evidenceRole: "EXTERNAL_CONTEXT_ONLY", retrievedAt: new Date().toISOString(), kansas: [{ notam: "6/1234", type: "HAZARDS", state: "KS", facility: null, description: "SALINA, KS", created: null }], total: 1, shapes: [tfrShape], detailsChecked: 1, detailsFailed: 0 };
      default: return {};
    }
  };
  const h = await componentHarness("app/aviation-layer-control.tsx", {
    "./bounded-json": { ...bounded, readBoundedJson }, "./aviation-airspace": airspace, "./aviation-weather": weather, "./aviation-drone-data": drone, "./aviation-traffic": traffic,
    "./kansas-sky-control": { KansasSkyControl: () => null }, "./aviation-chart": chart, "./aviation-profile": profile, "./aviation-research": research, "./map-runtime": { unexaggeratedTerrainElevation: () => null },
    "./aviation-phase": phase, "./aircraft-types": types, "./aviation-dossier": dossier,
  }, { fetch, setInterval, clearInterval, crypto: globalThis.crypto, TextDecoder });
  const props = { mapRef: { current: null }, styleReady: false };
  const cycle = async () => { const tree = h.render(h.exports.AviationLayerControl, props); h.commit(); await new Promise(resolve => setTimeout(resolve, 5)); await settle(); return tree; };
  const panel = tree => findNode(tree, node => node.type === "div" && node.props["data-aviation-dossier"] !== undefined);
  try {
    let tree = await cycle();
    findNode(tree, node => node.type === "input" && node.props["aria-label"] === "Show airspace and aviation layers").props.onChange({ target: { checked: true } });
    tree = await renderUntil(cycle, tree => Boolean(findNode(tree, node => node.type === "select" && node.props["aria-label"] === "Airport dossier")), "the airport list");
    assert.equal(panel(tree), undefined, "no dossier until an airport is chosen");
    findNode(tree, node => node.type === "select" && node.props["aria-label"] === "Airport dossier").props.onChange({ target: { value: "SLN" } });
    tree = await renderUntil(cycle, tree => { const node = panel(tree); return Boolean(node) && /TEST1/.test(text(node)) && /Issued/.test(text(node)) && /METAR KSLN SYNTHETIC/.test(text(node)) && /SALINA AREA/.test(text(node)); }, "the filled dossier");
    const body = text(panel(tree));
    assert.match(body, /SALINA RGNL \(KSLN\) · SALINA, SALINE County · public-use airport/);
    assert.match(body, /Towered \(ATCT\)/);
    assert.match(body, /1,288 ft MSL \(NASR\)/);
    assert.match(body, /17\/35 · 12,301 × 150 ft · asphalt\/concrete · high lighting/);
    assert.match(body, /METAR KSLN SYNTHETIC.*station KSLN at this airport/);
    assert.match(body, /MVFR · base .*\(in force now\) · ceiling 2,500 ft BKN · ≥6 SM/);
    assert.match(body, /IFR · FM .* · ceiling 500 ft OVC · 2 SM · wind 150@4 kt · BR/);
    assert.match(body, /6\/1234 HAZARDS · SALINA AREA: SFC to 3,000 MSL/);
    assert.match(body, /Descending, track toward the field/);
    assert.match(body, /TEST1 · C172 Cessna 172 Skyhawk · 1,21\d ft above field · 5 NM · observed \d+ s ago/);
    assert.match(body, /On the surface \(reported\)/);
    assert.match(body, /TEST2 · B738 Boeing 737-800 · on surface/);
    assert.match(body, /no arrival, departure or destination is known/);
    assert.doesNotMatch(body, /\b(arrivals|departures|scheduled|landing|departing)\b/i, "the board is observation, not a FIDS");
    findNode(panel(tree), node => node.type === "button" && /Close dossier/.test(text(node))).props.onClick();
    tree = await renderUntil(cycle, tree => !panel(tree), "the closed dossier");
  } finally { h.dispose(); }
});
