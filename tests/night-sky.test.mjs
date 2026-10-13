import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const read = (path) => readFile(new URL(`../${path}`, import.meta.url), "utf8");
const toUrl = (javascript) => `data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`;
const transpile = (source) => ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const loadSky = async () => import(toUrl(transpile(await read("app/night-sky.ts"))));
const near = (actual, expected, tolerance, message) => assert.ok(Math.abs(actual - expected) <= tolerance, `${message}: ${actual} not within ${tolerance} of ${expected}`);
const angleNear = (actual, expected, tolerance, message) => near(((actual - expected + 540) % 360) - 180, 0, tolerance, message);
const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];

const J2000 = Date.UTC(2000, 0, 1, 12);
const KANSAS = [-98.38, 38.48];

test("sidereal time matches the J2000 epoch and advances one turn per sidereal day", async () => {
  const sky = await loadSky();
  near(sky.julianDate(J2000), 2_451_545, 1e-9, "J2000.0 Julian date");
  near(sky.greenwichSiderealDegrees(J2000), 280.46061837, 1e-6, "GMST at J2000.0");
  const siderealDayMs = 86_164_090.5;
  angleNear(sky.greenwichSiderealDegrees(J2000 + siderealDayMs), 280.46061837, 0.01, "one sidereal day later");
});

test("galactic coordinates put the pole at b = 90° and the centre in Sagittarius at l = 0°", async () => {
  const sky = await loadSky();
  near(sky.galacticPosition(192.85948, 27.12825).b, 90, 0.01, "north galactic pole");
  const centre = sky.galacticPosition(266.40510, -28.93617);
  angleNear(centre.l, 0, 0.05, "galactic centre longitude");
  near(centre.b, 0, 0.05, "galactic centre latitude");
});

test("Polaris stands at about the observer's latitude over Kansas at any hour", async () => {
  const sky = await loadSky();
  for (let hour = 0; hour < 24; hour += 3) {
    const { altitude, azimuth } = sky.horizontalPosition(37.95456, 89.26411, Date.UTC(2026, 9, 9, hour), ...KANSAS);
    near(altitude, KANSAS[1], 0.8, `Polaris altitude at ${hour}h`);
    angleNear(azimuth, 0, 1.2, `Polaris azimuth at ${hour}h`);
  }
});

test("a star on the local meridian transits due south at 90° minus its zenith distance", async () => {
  const sky = await loadSky();
  const instant = Date.UTC(2026, 9, 9, 4, 30);
  const localSidereal = sky.greenwichSiderealDegrees(instant) + KANSAS[0];
  const { altitude, azimuth } = sky.horizontalPosition(localSidereal, 20, instant, ...KANSAS);
  near(altitude, 90 - (KANSAS[1] - 20), 1e-6, "transit altitude");
  angleNear(azimuth, 180, 1e-6, "transit azimuth");
});

test("the Sun reaches the solstice declination in June and the equator in March", async () => {
  const sky = await loadSky();
  near(sky.sunEquatorial(Date.UTC(2026, 5, 21, 8, 24)).dec, 23.44, 0.02, "June solstice");
  near(sky.sunEquatorial(Date.UTC(2026, 2, 20, 14, 46)).dec, 0, 0.03, "March equinox");
  near(sky.sunEquatorial(Date.UTC(2026, 2, 20, 14, 46)).ra, 0, 0.1, "March equinox right ascension");
});

test("the globe frame puts each place's zenith where MapLibre draws that place on the sphere", async () => {
  const sky = await loadSky();
  const instant = Date.UTC(2026, 9, 9, 3);
  for (const [lng, lat] of [KANSAS, [0, 0], [139.7, 35.7], [-58.4, -34.6]]) {
    const zenith = sky.equatorialVector(sky.greenwichSiderealDegrees(instant) + lng, lat);
    const onGlobe = sky.transform3(sky.globeSkyFrame(instant).equatorialToView, zenith);
    const radians = Math.PI / 180;
    const expected = [Math.sin(lng * radians) * Math.cos(lat * radians), Math.sin(lat * radians), Math.cos(lng * radians) * Math.cos(lat * radians)];
    for (let axis = 0; axis < 3; axis += 1) near(onGlobe[axis], expected[axis], 1e-9, `globe axis ${axis} for ${lng},${lat}`);
  }
});

test("the flat-map frame round-trips view rays and reports the same altitude as the horizon math", async () => {
  const sky = await loadSky();
  const instant = Date.UTC(2026, 9, 9, 4);
  const frame = sky.flatSkyFrame(instant, ...KANSAS, 7.5);
  const sirius = sky.equatorialVector(101.287, -16.716);
  const back = sky.transform3(frame.viewToEquatorial, sky.transform3(frame.equatorialToView, sirius));
  for (let axis = 0; axis < 3; axis += 1) near(back[axis], sirius[axis], 1e-9, `round trip axis ${axis}`);
  const altitude = Math.asin(dot(sirius, frame.zenith)) * 180 / Math.PI;
  near(altitude, sky.horizontalPosition(101.287, -16.716, instant, ...KANSAS).altitude, 1e-9, "zenith altitude");
  // North on the map is −y in Mercator world pixels.
  const northHorizon = sky.transform3(frame.viewToEquatorial, [0, -1, 0]);
  near(sky.transform3(frame.equatorialToView, northHorizon)[1], -1, 1e-9, "north maps to −y");
});

test("the 4×4 inverse recovers the identity", async () => {
  const sky = await loadSky();
  const m = [2, 0.1, 0, 0.3, -0.4, 1.5, 0.2, 0, 0.7, -0.2, 0.9, 0.05, 12, -7, 3, 1];
  const inverse = sky.invert4(m);
  for (let row = 0; row < 4; row += 1) for (let column = 0; column < 4; column += 1) {
    let sum = 0;
    for (let k = 0; k < 4; k += 1) sum += m[k * 4 + row] * inverse[column * 4 + k];
    near(sum, row === column ? 1 : 0, 1e-5, `identity ${row},${column}`);
  }
  assert.equal(sky.invert4(new Array(16).fill(0)), null);
});

test("star colours run from blue-white to orange and brightness falls with magnitude", async () => {
  const sky = await loadSky();
  const hot = sky.starColor(-0.3), cool = sky.starColor(1.6), unknown = sky.starColor(null);
  assert.ok(hot[2] > hot[0], "hot stars lean blue");
  assert.ok(cool[0] > cool[2], "cool stars lean red");
  assert.ok(unknown.every((channel) => channel > 0.9), "unknown colour draws near-white");
  for (const channel of [...hot, ...cool]) assert.ok(channel >= 0.45 && channel <= 1);
  const sirius = sky.starAppearance(-1.44), faint = sky.starAppearance(5.5);
  assert.ok(sirius.size > faint.size && sirius.brightness > faint.brightness);
  assert.ok(faint.size >= 2 && sirius.size <= 14);
});

test("the sky shows from orbit always, on tilted maps only under a dark sky, and never in Battery saver", async () => {
  const sky = await loadSky();
  assert.equal(sky.nightSkyShouldShow(true, false, "globe", 0, 0), true, "space is dark by day too");
  assert.equal(sky.nightSkyShouldShow(true, false, "mercator", 70, sky.SKY_DARKNESS.night), true);
  assert.equal(sky.nightSkyShouldShow(true, false, "mercator", 70, sky.SKY_DARKNESS.dusk), true);
  assert.equal(sky.nightSkyShouldShow(true, false, "mercator", 70, sky.SKY_DARKNESS.clear), false, "no stars in a blue sky");
  assert.equal(sky.nightSkyShouldShow(true, false, "mercator", sky.NIGHT_SKY_MIN_PITCH - 1, 1), false, "too flat for any horizon");
  // The renderer draws only once the horizon is in frame for the live field of view.
  assert.equal(sky.horizonInView(66), true, "default field of view");
  assert.equal(sky.horizonInView(64), false, "horizon just below the frame");
  assert.equal(sky.horizonInView(60, 50), true, "a wider field of view brings the horizon in");
  assert.equal(sky.nightSkyShouldShow(true, true, "globe", 60, 1), false, "Battery saver");
  assert.equal(sky.nightSkyShouldShow(false, false, "globe", 60, 1), false, "switched off");
});

test("the bundled catalog carries its provenance and real star positions", async () => {
  const catalog = JSON.parse(await read("app/night-sky-catalog.json"));
  assert.equal(catalog.schema, "kfm-night-sky-catalog/v1");
  assert.equal(catalog.role, "display");
  assert.equal(catalog.source.license, "BSD-3-Clause");
  assert.match(catalog.source.catalog, /XHIP/);
  assert.match(catalog.source.sha256, /^[0-9a-f]{64}$/);
  assert.deepEqual(catalog.fields, ["ra", "dec", "mag", "bv"]);
  assert.equal(catalog.stars.length, catalog.count * 4);
  assert.ok(catalog.count > 2000, "naked-eye sky");
  let previous = Infinity;
  for (let index = 0; index < catalog.count; index += 1) {
    const [ra, dec, mag] = catalog.stars.slice(index * 4, index * 4 + 3);
    assert.ok(ra >= 0 && ra < 360 && dec >= -90 && dec <= 90 && mag <= catalog.magnitudeLimit);
    assert.ok(mag <= previous, "faintest first so the brightest draw on top");
    previous = mag;
  }
  // Sirius, the brightest star, is drawn last.
  assert.deepEqual(catalog.stars.slice(-4, -1), [101.287, -16.716, -1.44]);
});

test("packed stars are unit directions with a colour, a look and a stable twinkle phase", async () => {
  const sky = await loadSky();
  const data = sky.packStars({ count: 2, stars: [101.287, -16.716, -1.44, 0.01, 37.955, 89.264, 1.97, null] });
  assert.equal(data.length, 18);
  for (const offset of [0, 9]) {
    near(Math.hypot(data[offset], data[offset + 1], data[offset + 2]), 1, 1e-6, "unit direction");
    assert.ok(data[offset + 8] >= 0 && data[offset + 8] < 1, "phase in [0, 1)");
  }
  assert.ok(data[6] > data[15], "Sirius draws larger than Polaris");
});

test("the layer is a 2D custom layer that never draws before the map is attached", async () => {
  const sky = await loadSky();
  const layer = sky.createNightSkyLayer({ id: "sky", catalog: () => null, darkness: () => 1, clock: () => null });
  assert.equal(layer.type, "custom");
  assert.equal(layer.renderingMode, "2d");
  assert.equal(layer.id, "sky");
  assert.doesNotThrow(() => layer.render({}, {}), "render before onAdd is a no-op");
});

test("the camera sits at the near-plane centre the inverse matrix reports", async () => {
  const sky = await loadSky();
  // A perspective camera at z = +5 looking down −z (column-major view and projection).
  const zNear = 0.1, zFar = 100, f = 1 / Math.tan(Math.PI / 8);
  const projection = [f, 0, 0, 0, 0, f, 0, 0, 0, 0, (zFar + zNear) / (zNear - zFar), -1, 0, 0, (2 * zFar * zNear) / (zNear - zFar), 0];
  const view = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, -5, 1];
  const matrix = new Array(16).fill(0);
  for (let column = 0; column < 4; column += 1) for (let row = 0; row < 4; row += 1) {
    for (let k = 0; k < 4; k += 1) matrix[column * 4 + row] += projection[k * 4 + row] * view[column * 4 + k];
  }
  const camera = sky.cameraPosition(sky.invert4(matrix));
  near(camera[0], 0, 1e-5, "x");
  near(camera[1], 0, 1e-5, "y");
  near(camera[2], 5 - zNear, 1e-3, "z sits on the near plane in front of the eye");
});
