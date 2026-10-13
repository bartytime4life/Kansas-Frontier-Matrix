import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFile } from "node:fs/promises";
import test from "node:test";

const asset = JSON.parse(await readFile(new URL("../public/data/subsurface/geophysics.json", import.meta.url), "utf8"));
const surveys = new Map(asset.surveys.map(survey => [survey.id, survey]));
const profiles = asset.surveys.flatMap(survey => survey.profiles);
const profile = id => profiles.find(item => item.id === id);

// Independent captures of the public workbook bytes. A source update requires
// requalification, rather than silently treating new bytes as the reviewed data.
const sourceReceipts = {
  "kgs-dpec-dg02": ["DG02%20EC%20Transect%20Data.xlsx", 1238778, "0fe30b96f9d826b4bcf4ec31678bfa60a90cacc6b4455dab6b18d636093f65e2"],
  "kgs-dpec-dg03": ["DG03%20EC%20Transect%20Data.xlsx", 767700, "c9b8ceac0fdfe7e49bf2c7fca78fce666167e0d6d1554182d0a00528ca08def7"],
  "kgs-dpec-jf01": ["JF01%20EC%20Transect%20Data.xlsx", 800826, "14090c05ffe586838f04bda7e0da35bee5379479c536c41c5040a761e6febf8a"],
  "kgs-dpec-rl01": ["RL01%20EC%20Transect%20Data.xlsx", 1024304, "cf30bfbdff5b35576fba492e3244a40bf0cc5fca573e2964121e07a55b254f64"],
  "kgs-dpec-wb01-pt02": ["WB01%20to%20PT02%20EC%20Transect%20Data.xlsx", 821239, "c0db284efd934bbed3d8b8ef9115a4a2a45e8bb3587d8f4f759465f9d46428d2"],
};

test("geophysical capture exposes versioned source metadata and separate geological model references", () => {
  assert.equal(asset.version, 1);
  assert.equal(asset.interpretationStatus, "external-context-only");
  assert.equal(surveys.size, asset.surveys.length, "survey identities must be unique");
  assert.equal(asset.surveys.length, 7);
  assert.ok(Number.isFinite(Date.parse(asset.retrievedAt)));
  for (const survey of asset.surveys) {
    assert.ok(["electrical", "electromagnetic", "gpr", "seismic"].includes(survey.method));
    assert.ok(["ready", "held", "reference-only"].includes(survey.status));
    assert.equal(new URL(survey.sourceUrl).protocol, "https:");
    assert.ok(survey.title && survey.sourceTime && survey.limitation);
    assert.equal(survey.retrievedAt, asset.retrievedAt);
    assert.ok(Array.isArray(survey.profiles));
    if (survey.status !== "ready") assert.deepEqual(survey.profiles, []);
  }
  assert.equal(asset.modelReferences.length, 1);
  const model = asset.modelReferences[0];
  assert.equal(model.recordKind, "published-model-reference");
  assert.equal(model.status, "held");
  assert.equal(model.method, undefined, "well-log models must not enter electrical survey filters");
  assert.deepEqual(model.profiles, []);
});

test("published DPEC source hashes, files, rights and capture notices remain attached", () => {
  const base = "https://www.kgs.ku.edu/Publications/OFR/2022/OFR2022-6/";
  for (const [id, [filename, bytes, hash]] of Object.entries(sourceReceipts)) {
    const survey = surveys.get(id);
    assert.equal(survey.sourceUrl, base + filename);
    assert.equal(survey.sourceBytes, bytes);
    assert.equal(survey.sourceSha256, hash);
    assert.equal(survey.method, "electrical");
    assert.equal(survey.publicationUrl, base + "index.html");
    assert.equal(survey.rightsUrl, "https://www.kgs.ku.edu/General/copyright.html");
    assert.equal(survey.attribution, asset.attribution);
    assert.match(survey.attribution, /All Rights Reserved\.$/);
    assert.match(survey.sourceTime, /Published 2022-07-11/);
  }
});

test("invalid PT01 longitude and ambiguous or duplicated source profiles stay held", () => {
  const wb = surveys.get("kgs-dpec-wb01-pt02");
  const pt01 = wb.heldProfiles.find(item => item.id === "PT01");
  assert.ok(pt01);
  assert.equal(Number(pt01.sourceLocation.west), 29.278079999999999);
  assert.match(pt01.reason, /outside Kansas/);
  assert.equal(profile("PT01"), undefined, "do not repair a bad longitude into an invented location");

  const jf = surveys.get("kgs-dpec-jf01");
  assert.deepEqual(jf.heldProfiles.map(item => item.id).sort(), ["JF01-EC1", "JF01-EC2"]);
  assert.ok(jf.heldProfiles.every(item => /same 1,073/.test(item.reason)));
  assert.equal(profile("JF01-EC1"), undefined);
  assert.equal(profile("JF01-EC2"), undefined);
  assert.ok(profile("JF01-well"), "the independent well log remains usable");

  const dg03 = surveys.get("kgs-dpec-dg03");
  assert.equal(dg03.status, "held");
  assert.equal(dg03.heldProfiles.length, 6);
  assert.deepEqual(dg03.profiles, []);
});

test("admitted conductivity logs preserve ft depth versus mS/m values without fabricated elevation", () => {
  assert.equal(profiles.length, 21);
  assert.equal(profiles.reduce((count, item) => count + item.samples.length, 0), 25479);
  assert.equal(new Set(profiles.map(item => item.id)).size, profiles.length);
  for (const item of profiles) {
    assert.equal(item.depthUnit, "ft");
    assert.equal(item.valueUnit, "mS/m");
    assert.equal(item.depthReference, "land-surface");
    assert.match(item.coordinateReference, /approximate Google Earth/);
    assert.match(item.coordinateReference, /EPSG unspecified/);
    assert.match(item.limitation, /not registered to a geodetic datum/);
    assert.equal(item.coordinates.length, 2, "no unsupported sea-level z coordinate");
    assert.ok(item.coordinates.every(Number.isFinite));
    assert.ok(item.coordinates[0] >= -102.1 && item.coordinates[0] <= -94.5);
    assert.ok(item.coordinates[1] >= 36.9 && item.coordinates[1] <= 40.1);
    assert.equal(item.elevation, undefined);
    assert.equal(item.elevationM, undefined);
    assert.equal(item.lithology, undefined, "conductivity must not silently become a rock classification");
  }
});

test("every admitted sample is finite with a strictly increasing original depth sequence", () => {
  for (const item of profiles) {
    assert.ok(item.samples.length > 1, item.id);
    for (let index = 0; index < item.samples.length; index++) {
      const sample = item.samples[index];
      assert.ok(Number.isFinite(sample.depth) && sample.depth >= 0, `${item.id} depth ${index}`);
      assert.ok(Number.isFinite(sample.value), `${item.id} value ${index}`);
      if (index) assert.ok(sample.depth > item.samples[index - 1].depth, `${item.id} duplicate/reversed depth`);
    }
  }
  const signatures = profiles.map(item => createHash("sha256").update(JSON.stringify(item.samples)).digest("hex"));
  assert.equal(new Set(signatures).size, signatures.length, "identical full source series cannot map to separate admitted locations");
});

test("independently reread workbook samples retain their source values and bounds", () => {
  // Checked from the XLSX XML in a separate source read. RL01 EC is column C;
  // its column B is metres and must never be mistaken for conductivity.
  const observed = [
    ["DG02-EC1", 1508, [0, 0.88], [5, 28.39], [75.35, 21.69], [0.88, 129.18]],
    ["JF01-well", 937, [0, 0.01], [5, 7.87], [46.8, 33.21], [0, 208.48]],
    ["RL01-EC1-Well", 1007, [0, 0.03], [5, 14.05], [50.3, 2.06], [0, 33.86]],
    ["PT-EC4", 722, [0, 0.36], [5, 121.28], [36.05, 32.89], [0.23, 123.42]],
  ];
  const pair = sample => [sample.depth, sample.value];
  for (const [id, count, first, hundredth, last, bounds] of observed) {
    const samples = profile(id).samples;
    assert.equal(samples.length, count, id);
    assert.deepEqual(pair(samples[0]), first, id);
    assert.deepEqual(pair(samples[100]), hundredth, id);
    assert.deepEqual(pair(samples.at(-1)), last, id);
    assert.deepEqual([Math.min(...samples.map(item => item.value)), Math.max(...samples.map(item => item.value))], bounds, id);
  }
});

test("GPR remains a time-uncertain report reference without invented depth traces", () => {
  const radar = surveys.get("kgs-gems-gpr-1998");
  assert.equal(radar.method, "gpr");
  assert.equal(radar.status, "reference-only");
  assert.equal(radar.sourceTime, "1998-10-07 and 1998-10-12");
  assert.deepEqual(radar.profiles, []);
  assert.match(radar.limitation, /time-zero is uncertain/);
  assert.match(radar.limitation, /casing/);
  assert.match(radar.limitation, /no numerical velocity conversion/);
  assert.equal(radar.velocityModel, undefined);
  assert.equal(radar.depthUnit, undefined);
});

test("tTEM resistivity and missing native-grid coverage are not promoted to continuous geology", () => {
  const ttem = surveys.get("kraa-ttem");
  assert.equal(ttem.method, "electromagnetic");
  assert.equal(ttem.status, "reference-only");
  assert.deepEqual(ttem.profiles, []);
  assert.match(ttem.limitation, /depth-of-investigation/);
  assert.match(ttem.limitation, /cannot be treated as unique rock identity/);
  assert.ok(asset.surveys.filter(item => item.status === "ready").every(item => item.method === "electrical"));
  assert.match(asset.modelReferences[0].limitation, /not reconstructed/);
});
