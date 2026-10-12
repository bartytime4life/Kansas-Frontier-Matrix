import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { spawnSync } from "node:child_process";
import test from "node:test";
import { gunzipSync } from "node:zlib";

const root = path.resolve("public/data/subsurface");
const manifest = JSON.parse(await readFile(path.join(root, "manifest.json"), "utf8"));
const hash = bytes => createHash("sha256").update(bytes).digest("hex");
const permittedRecordKeys = new Set(["id", "sourceId", "kind", "name", "coordinates", "coordinateReference", "locationMethod", "sourceUrl", "sourceTime", "depthUnit", "depthReference", "totalDepth", "intervals", "photosUrl"]);
const permittedIntervalKeys = new Set(["top", "bottom", "description", "interpreted"]);
const recordInfo = new Map();

async function asset(entry) {
  assert.match(entry.url, /^\/data\/subsurface\/(?:tile-[\d-]+|locator)\.json\.gz$/);
  const compressed = await readFile(path.join(root, path.basename(entry.url)));
  assert.equal(hash(compressed), entry.sha256);
  assert.equal(compressed.length, entry.bytes);
  const bytes = gunzipSync(compressed);
  assert.equal(bytes.length, entry.uncompressedBytes);
  return JSON.parse(bytes);
}

test("pinned subsurface sources retain provider editions, datum transforms and limits", () => {
  assert.equal(manifest.version, 1);
  assert.equal(manifest.status, "EXTERNAL_CONTEXT_ONLY");
  assert.equal(manifest.sources.length, 4);
  assert.equal(manifest.totals.wwc5_wellsRows, 315254);
  assert.equal(manifest.totals.coreLibRows, 7394);
  assert.equal(manifest.totals.wwc5_lith_logRows, 1615923);
  for (const source of manifest.sources) {
    assert.match(source.url, /^https:\/\/www\.kgs\.ku\.edu\/PRS\/Ora_Archive\/[\w]+\.zip$/);
    assert.match(source.sha256, /^[a-f0-9]{64}$/);
    assert.ok(Number.isFinite(Date.parse(source.retrievedAt)));
    assert.ok(source.limitation.length > 50);
  }
  assert.match(manifest.horizontalTransform.nad83Operation, /EPSG:1188/);
  assert.equal(manifest.horizontalTransform.nad27GridSha256, "44611d823c48e5347500ee6afe40ff33d2b88cf817bf59f705ed4a4c3bd687d7");
  assert.ok(manifest.coverageLimits.some(text => text.includes("deviation")));
  assert.ok(manifest.privacy.excludedFields.includes("OWNER"));
  assert.ok(manifest.privacy.excludedFields.includes("DIRECTIONS"));
});

test("every spatial tile has verified hashes, bounded size and data-only field projection", async () => {
  let wells = 0, cores = 0, logged = 0, ranges = 0, interpreted = 0, photos = 0, gapCount = 0, overlapCount = 0;
  for (const entry of manifest.tiles) {
    const records = await asset(entry);
    assert.equal(records.length, entry.count);
    assert.ok(entry.uncompressedBytes <= 3_000_000);
    const [w, s, e, n] = entry.bounds;
    assert.ok(e > w && n > s);
    let tileWells = 0, tileCores = 0, previousId = "";
    for (const record of records) {
      assert.ok(record.id > previousId, "deterministic identity ordering"); previousId = record.id;
      assert.equal(recordInfo.has(record.id), false, "identities unique across tiles");
      assert.deepEqual(Object.keys(record).filter(key => !permittedRecordKeys.has(key)), []);
      assert.ok(record.kind === "core" || record.kind === "well");
      assert.match(record.name, record.kind === "core" ? /^Core KID \d+$/ : /^WWC5 \d+$/);
      assert.match(record.id, record.kind === "core" ? /^core-\d+$/ : /^wwc5-\d+$/);
      assert.equal(record.sourceId, record.kind === "core" ? "kgs-core" : "kgs-wwc5");
      assert.match(record.coordinateReference, /WGS84.*4 m/);
      assert.equal(record.depthUnit, "ft");
      const [x,y] = record.coordinates;
      assert.ok(Number.isFinite(x) && Number.isFinite(y) && x >= w && x <= e && y >= s && y <= n);
      recordInfo.set(record.id, { coordinates: record.coordinates, tile: entry.id });
      assert.match(record.sourceUrl, record.kind === "core" ? /^https:\/\/chasm\.kgs\.ku\.edu\/ords\/qualified\.well_page\.DisplayWell\?f_kid=\d+$/ : /^https:\/\/chasm\.kgs\.ku\.edu\/ords\/wwc5\.wwc5d2\.well_details\?well_id=\d+$/);
      assert.equal(record.depthReference, record.kind === "core" ? "drilled-depth" : "land-surface");
      if (record.kind === "core") { cores++; tileCores++; assert.equal(record.totalDepth, null); }
      else { wells++; tileWells++; }
      if (record.photosUrl) { assert.equal(record.kind, "core"); photos++; assert.match(record.photosUrl, /^https:\/\/chasm\.kgs\.ku\.edu\/ords\/qualified\.cimg2\.CoreImages\?f_well=\d+$/); }
      let previousTop = -1, previousBottom = null;
      for (const interval of record.intervals) {
        assert.deepEqual(Object.keys(interval).filter(key => !permittedIntervalKeys.has(key)), []);
        assert.ok(Number.isFinite(interval.top) && Number.isFinite(interval.bottom));
        assert.ok(interval.top >= 0 && interval.bottom > interval.top);
        assert.ok(interval.top >= previousTop); previousTop = interval.top;
        if (previousBottom !== null && record.kind === "well") { gapCount += interval.top > previousBottom; overlapCount += interval.top < previousBottom; }
        previousBottom = interval.bottom;
        assert.equal(typeof interval.description, "string");
        if (interval.interpreted) { interpreted++; assert.equal(record.kind, "well"); assert.match(interval.interpreted, /^[A-Za-z0-9/, .-]+$/); }
        if (record.kind === "well") logged++; else ranges++;
      }
    }
    assert.equal(tileWells, entry.wellCount); assert.equal(tileCores, entry.coreCount);
  }
  assert.equal(wells, manifest.totals.wellCount); assert.equal(cores, manifest.totals.coreCount);
  assert.equal(logged, manifest.totals.loggedIntervalCount); assert.equal(ranges, manifest.totals.coreRangeCount);
  assert.equal(interpreted, manifest.totals.matchedInterpretedIntervals); assert.equal(photos, manifest.totals.coresWithPhotoLinks);
  assert.ok(gapCount > 0 && overlapCount > 0, "recorded gaps and overlaps remain visible rather than interpolated or silently repaired");
  assert.equal(manifest.totals.wwc5_lith_logRows, logged + manifest.totals.invalidLoggedIntervals + manifest.totals.duplicateLoggedIntervals + manifest.totals.loggedIntervalsWithoutMappedWell);
});

test("statewide locator agrees with every tile and contains no ownership or descriptive fields", async () => {
  const locator = await asset(manifest.locator);
  assert.deepEqual(manifest.locator.columns, ["id", "county", "coordinates", "tileId"]);
  assert.equal(locator.length, manifest.locator.count);
  assert.equal(locator.length, manifest.totals.wellCount + manifest.totals.coreCount);
  let previous = "";
  for (const row of locator) {
    assert.equal(row.length, 4);
    const [id, county, coordinates, tile] = row;
    assert.ok(id > previous); previous = id;
    assert.ok(county === "" || /^[A-Za-z ]+$/.test(county));
    assert.deepEqual(recordInfo.get(id), { coordinates, tile });
  }
  assert.equal(manifest.counties.length, 105);
  assert.equal(manifest.counties.reduce((sum, county) => sum + county.count, 0), manifest.totals.wellCount);
});

test("asset preparer rejects invalid ranges and coordinates while preserving descriptions", () => {
  const python = `import importlib.util\ns=importlib.util.spec_from_file_location('subsurface','scripts/prepare-subsurface.py')\nm=importlib.util.module_from_spec(s);s.loader.exec_module(m)\nassert m.interval('0','10','original shale') == {'top':0.0,'bottom':10.0,'description':'original shale'}\nassert m.interval('10','5','bad') is None\nassert m.interval('nan','5','bad') is None\nassert m.interval('-1','5','bad') is None\nassert m.interval('0','0','bad') is None\nassert m.kansas_coordinates('',38) is None\nassert m.kansas_coordinates(-97,'nan') is None\nassert m.kansas_coordinates(-97,45) is None\nassert m.record_date('') == 'Unknown record date'\nassert m.record_date('10-Jul-1978') == '1978-07-10'\nassert m.normalize_description(' Clay,   Yellow ') == 'clay, yellow'\n`;
  const run = spawnSync("python3", ["-B", "-c", python], { encoding: "utf8" });
  assert.equal(run.status, 0, run.stderr);
});
