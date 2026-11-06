// Operator-only local candidate import. No provider I/O, public reads, activation,
// schema changes, or separate store: the existing shared archive owns persistence.
import { constants } from "node:fs";
import { lstat, open, opendir, realpath } from "node:fs/promises";
import { resolve, dirname, basename, parse, join } from "node:path";
import { createHash } from "node:crypto";
import { gunzipSync } from "node:zlib";
import { ingestionConfig, ARCHIVE_LIMIT_BYTES, RECEIPT_ALLOWANCE } from "./ingestion-config.mjs";
import { getIngestionStore } from "./ingestion-store.mjs";

export const SKY_ARTIFACT_LIMIT = 4 * 1024 * 1024;
const DAY_LIMIT = 2 * 1024 ** 3;
const MAX_FILES = 10_000;
const LICENSE_URL = "https://opendatacommons.org/licenses/odbl/1-0/";
const hash = value => createHash("sha256").update(value).digest("hex");
const object = value => value !== null && typeof value === "object" && !Array.isArray(value);
const integer = (value, min, max) => Number.isSafeInteger(value) && value >= min && value <= max;
const digest = value => typeof value === "string" && /^[a-f0-9]{64}$/.test(value);
const date = value => typeof value === "string" && Number.isFinite(Date.parse(value));
const hexPattern = "~?[a-f0-9]{6}";
const fail = code => { throw new Error(code); };
function json(bytes) { try { return JSON.parse(new TextDecoder("utf-8", { fatal: true }).decode(bytes)); } catch { fail("SKY_JSON_INVALID"); } }
function utcDay(day) {
  if (typeof day !== "string" || !/^\d{4}-\d{2}-\d{2}$/.test(day) || !date(day) || new Date(day).toISOString().slice(0, 10) !== day) fail("SKY_DAY_INVALID");
  return Date.parse(`${day}T00:00:00Z`);
}

async function directoryChain(path) {
  const chain = []; let current = path;
  while (true) { chain.push(current); const parent = dirname(current); if (parent === current) break; current = parent; }
  for (const item of chain.reverse()) {
    const stat = await lstat(item);
    if (stat.isSymbolicLink() || !stat.isDirectory()) fail("SKY_PATH_REJECTED");
  }
  if (await realpath(path) !== path) fail("SKY_PATH_REJECTED");
}
async function readBounded(root, relative, expected) {
  const path = join(root, relative);
  await directoryChain(dirname(path));
  let handle;
  try {
    handle = await open(path, constants.O_RDONLY | constants.O_NOFOLLOW);
    const before = await handle.stat();
    if (!before.isFile() || before.nlink !== 1 || !integer(before.size, 1, SKY_ARTIFACT_LIMIT)) fail("SKY_ARTIFACT_BOUND");
    const buffer = Buffer.alloc(before.size + 1); let count = 0;
    while (count < buffer.length) { const { bytesRead } = await handle.read(buffer, count, buffer.length - count, count); if (!bytesRead) break; count += bytesRead; }
    const after = await handle.stat(), named = await lstat(path);
    await directoryChain(dirname(path));
    if (named.isSymbolicLink() || named.dev !== before.dev || named.ino !== before.ino || after.size !== before.size || after.mtimeMs !== before.mtimeMs || count !== before.size) fail("SKY_ARTIFACT_CHANGED");
    const bytes = buffer.subarray(0, count), sha256 = hash(bytes);
    if (expected && (expected.bytes !== count || expected.sha256 !== sha256)) fail("SKY_ARTIFACT_INTEGRITY_FAILED");
    return { bytes, sha256 };
  } finally { await handle?.close(); }
}
function sourceIdentity(source, day) {
  const tag = `v${day.replaceAll("-", ".")}-planes-readsb-prod-0`;
  const releaseUrl = `https://api.github.com/repos/adsblol/globe_history_${day.slice(0, 4)}/releases/tags/${tag}`;
  if (!object(source) || source.day !== day || source.releaseUrl !== releaseUrl || !date(source.sourcePublishedAt)
    || source.provider !== "adsb.lol" || source.license !== "ODbL-1.0" || source.licenseUrl !== LICENSE_URL || source.maxCandidateBytes !== DAY_LIMIT
    || !object(source.region) || source.region.west !== -103.2 || source.region.east !== -93.6 || source.region.south !== 36.2 || source.region.north !== 40.9
    || !Array.isArray(source.assets) || !integer(source.assets.length, 1, 26)) fail("SKY_SOURCE_IDENTITY_INVALID");
  let total = 0;
  source.assets.forEach((asset, index) => {
    const name = `${tag}.tar.a${String.fromCharCode(97 + index)}`;
    const url = `https://github.com/adsblol/globe_history_${day.slice(0, 4)}/releases/download/${tag}/${name}`;
    if (!object(asset) || asset.name !== name || asset.url !== url || !digest(asset.sha256) || !integer(asset.bytes, 1, 6 * 1024 ** 3)) fail("SKY_ASSET_METADATA_INVALID");
    total += asset.bytes;
  });
  if (total > 6 * 1024 ** 3 || total !== source.downloadBytes) fail("SKY_ASSET_METADATA_INVALID");
  return { tag, sourceUrl: source.assets[0].url, sourceHash: hash(JSON.stringify(source)) };
}
function retainedManifest(receipt) {
  if (!object(receipt) || receipt.schemaVersion !== 1 || receipt.profile !== "kfm-sky-day-candidate/v1"
    || !["provider-day-processed", "partial-input"].includes(receipt.coverage) || receipt.lifecycle !== "WORK/QUARANTINE"
    || receipt.releaseState !== "unreleased" || receipt.evidenceRole !== "EXTERNAL_CONTEXT_ONLY" || !date(receipt.preparedAt)) fail("SKY_MANIFEST_INVALID");
  const dayStart = utcDay(receipt.day);
  if (dayStart + 86_400_000 > Date.now()) fail("SKY_DAY_NOT_FINISHED");
  const source = sourceIdentity(receipt.source, receipt.day);
  if (!integer(receipt.membersScanned, 0, 500_000) || !integer(receipt.aircraftCount, 0, MAX_FILES) || !integer(receipt.fileCount, 0, MAX_FILES)
    || !integer(receipt.pointCount, 0, MAX_FILES * 2500) || !Array.isArray(receipt.artifacts) || receipt.artifacts.length > MAX_FILES * 2 + 1) fail("SKY_MANIFEST_COUNTS_INVALID");
  const artifacts = new Map(); let total = 0;
  const rawPattern = new RegExp(`^raw/(${hexPattern})\\.json\\.gz$`);
  const replayPattern = new RegExp(`^replays/${receipt.day}-(?:nonicao-)?[a-f0-9]{6}-p[0-9]{4}\\.json$`);
  for (const item of receipt.artifacts) {
    if (!object(item) || typeof item.path !== "string" || !(item.path === "replays/index.json" || rawPattern.test(item.path) || replayPattern.test(item.path))
      || artifacts.has(item.path) || !digest(item.sha256) || !integer(item.bytes, 1, SKY_ARTIFACT_LIMIT)) fail("SKY_ARTIFACT_MANIFEST_INVALID");
    artifacts.set(item.path, { path: item.path, bytes: item.bytes, sha256: item.sha256 }); total += item.bytes;
  }
  if (!artifacts.has("replays/index.json") || total > DAY_LIMIT) fail("SKY_CANDIDATE_BOUND");
  return { dayStart, ...source, artifacts, total };
}
async function exactFiles(root, artifacts) {
  const allowed = new Set(["receipt.json", ...artifacts.keys()]); let found = 0;
  for await (const entry of await opendir(root)) {
    if (entry.isSymbolicLink()) fail("SKY_PATH_REJECTED");
    if (entry.isDirectory() && ["raw", "replays"].includes(entry.name)) {
      for await (const file of await opendir(join(root, entry.name))) {
        if (!file.isFile() || !allowed.has(`${entry.name}/${file.name}`)) fail("SKY_UNEXPECTED_ARTIFACT");
        found++; if (found > allowed.size) fail("SKY_UNEXPECTED_ARTIFACT");
      }
    } else if (entry.isFile() && entry.name === "receipt.json") found++;
    else fail("SKY_UNEXPECTED_ARTIFACT");
  }
  if (found !== allowed.size) fail("SKY_ARTIFACT_MISSING");
}
function rawTrace(bytes, hex) {
  let value;
  try { value = json(gunzipSync(bytes, { maxOutputLength: 16 * 1024 * 1024 })); } catch { fail("SKY_RAW_TRACE_INVALID"); }
  if (!object(value) || value.icao !== hex || !Array.isArray(value.trace) || !integer(value.trace.length, 1, 100_000)) fail("SKY_RAW_TRACE_INVALID");
}
function replayIdentity(value, flight, raw, receipt, sourceUrl, previousAt) {
  if (!object(value) || value.schemaVersion !== 1 || value.id !== flight.id || value.day !== receipt.day || value.provider !== "adsb.lol"
    || value.license !== "ODbL-1.0" || value.licenseUrl !== LICENSE_URL || value.sourceUrl !== sourceUrl || value.sourceSha256 !== raw.sha256
    || typeof value.sourceMember !== "string" || value.sourceMember.length > 300 || value.sourceMember.startsWith("/") || value.sourceMember.split("/").includes("..")
    || !new RegExp(`(?:^|/)traces/[a-f0-9]{2}/trace_full_${flight.hex}\\.json(?:\\.gz)?$`).test(value.sourceMember)
    || !Array.isArray(value.points) || !integer(value.points.length, 1, 2500) || value.points.length !== flight.pointCount) fail("SKY_REPLAY_IDENTITY_INVALID");
  let breaks = 0;
  for (const point of value.points) {
    if (!object(point) || point.hex !== flight.hex || point.providerId !== "adsb-lol" || point.timestampBasis !== "provider" || point.interpolated !== false
      || typeof point.breakBefore !== "boolean" || !Number.isFinite(point.observedAt) || point.observedAt <= previousAt || new Date(point.observedAt).toISOString().slice(0, 10) !== receipt.day
      || !Number.isFinite(point.lon) || point.lon < -103.2 || point.lon > -93.6 || !Number.isFinite(point.lat) || point.lat < 36.2 || point.lat > 40.9) fail("SKY_REPLAY_POINT_INVALID");
    previousAt = point.observedAt; if (point.breakBefore) breaks++;
  }
  if (new Date(value.points[0].observedAt).toISOString() !== flight.start || new Date(previousAt).toISOString() !== flight.end || breaks !== flight.segmentCount) fail("SKY_REPLAY_COUNTS_INVALID");
  return previousAt;
}

/** Reads only local bytes; returned plan is not a storage or collection receipt. */
export async function verifyKansasSkyDay(directory) {
  if (typeof directory !== "string" || !directory) fail("SKY_DIRECTORY_REQUIRED");
  const root = resolve(directory); if (root === parse(root).root) fail("SKY_PATH_REJECTED");
  await directoryChain(root);
  const manifest = await readBounded(root, "receipt.json"), receipt = json(manifest.bytes);
  const checked = retainedManifest(receipt);
  if (checked.total + manifest.bytes.length > DAY_LIMIT) fail("SKY_CANDIDATE_BOUND");
  await exactFiles(root, checked.artifacts);
  const catalog = json((await readBounded(root, "replays/index.json", checked.artifacts.get("replays/index.json"))).bytes);
  if (!object(catalog) || catalog.schemaVersion !== 1 || !Array.isArray(catalog.flights) || catalog.flights.length !== receipt.fileCount) fail("SKY_CATALOG_INVALID");
  const raw = new Map();
  for (const item of checked.artifacts.values()) if (item.path.startsWith("raw/")) {
    const hex = basename(item.path).slice(0, -8);
    rawTrace((await readBounded(root, item.path, item)).bytes, hex); raw.set(hex, item);
  }
  if (raw.size !== receipt.aircraftCount) fail("SKY_CATALOG_COUNTS_INVALID");
  const grouped = new Map(), paths = new Set(); let points = 0;
  for (const flight of catalog.flights) {
    if (!object(flight) || typeof flight.hex !== "string" || !new RegExp(`^${hexPattern}$`).test(flight.hex) || !raw.has(flight.hex)
      || flight.day !== receipt.day || flight.coverage !== receipt.coverage || flight.provider !== "adsb.lol" || flight.license !== "ODbL-1.0" || flight.sourceUrl !== checked.sourceUrl
      || !integer(flight.part, 1, 9999) || !integer(flight.partCount, 1, 9999) || flight.id !== `${receipt.day}-${flight.hex.replace("~", "nonicao-")}-p${String(flight.part).padStart(4, "0")}`
      || flight.url !== `/data/aviation/replays/days/${receipt.day}/${flight.id}.json` || !digest(flight.sha256)
      || !integer(flight.pointCount, 1, 2500) || !integer(flight.segmentCount, 0, flight.pointCount) || !date(flight.start) || !date(flight.end)) fail("SKY_CATALOG_ENTRY_INVALID");
    const path = `replays/${flight.id}.json`, artifact = checked.artifacts.get(path);
    if (!artifact || artifact.sha256 !== flight.sha256 || paths.has(path)) fail("SKY_CATALOG_INTEGRITY_FAILED");
    paths.add(path); const group = grouped.get(flight.hex) ?? []; group.push(flight); grouped.set(flight.hex, group); points += flight.pointCount;
  }
  if (grouped.size !== raw.size || paths.size + raw.size + 1 !== checked.artifacts.size || points !== receipt.pointCount) fail("SKY_CATALOG_COUNTS_INVALID");
  for (const [hex, flights] of grouped) {
    flights.sort((a, b) => a.part - b.part); let previousAt = -Infinity;
    for (const [index, flight] of flights.entries()) {
      if (flight.part !== index + 1 || flight.partCount !== flights.length) fail("SKY_REPLAY_PARTS_INVALID");
      const path = `replays/${flight.id}.json`;
      previousAt = replayIdentity(json((await readBounded(root, path, checked.artifacts.get(path))).bytes), flight, raw.get(hex), receipt, checked.sourceUrl, previousAt);
    }
  }
  const artifacts = [...checked.artifacts.values(), { path: "receipt.json", bytes: manifest.bytes.length, sha256: manifest.sha256 }];
  return { root, receipt, artifacts, sourceHash: checked.sourceHash, manifestSha256: manifest.sha256,
    plan: { state: "verified-plan", collectionActive: false, day: receipt.day, coverage: receipt.coverage, releaseState: "unreleased", aircraftCount: receipt.aircraftCount,
      pointCount: receipt.pointCount, artifacts: artifacts.length, payloadBytes: checked.total + manifest.bytes.length,
      maximumAccountedBytes: checked.total + manifest.bytes.length + artifacts.length * RECEIPT_ALLOWANCE, sharedCapacityBytes: ARCHIVE_LIMIT_BYTES, manifestSha256: manifest.sha256 } };
}
function captureFor(candidate, artifact, bytes) {
  const { receipt, sourceHash } = candidate;
  const id = hash(`kfm-sky-import-v1\n${receipt.day}\n${sourceHash}\n${artifact.path}\n${artifact.sha256}`);
  const sourceId = artifact.path === "receipt.json" ? "adsb-lol-kansas-day-manifest" : "adsb-lol-kansas-day-artifact";
  const request = { id, sourceId, slot: utcDay(receipt.day), limitBytes: artifact.bytes };
  return { request, capture: { bytes, receipt: { format: "kfm-hosted-capture-receipt-v1", captureId: id, sourceId,
    sourceUrl: receipt.source.releaseUrl, sourcePlanSha256: sourceHash, sourceDay: receipt.day, candidatePath: artifact.path,
    candidateManifestSha256: artifact.path === "receipt.json" ? candidate.manifestSha256 : null,
    sha256: artifact.sha256, byteLength: artifact.bytes, retrievedAt: new Date().toISOString(), preparedAt: receipt.preparedAt,
    adapterVersion: "kfm-sky-import-v1", validation: "structure-valid", lifecycle: "WORK/QUARANTINE", evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    rightsReview: "pending", sensitivityReview: "pending", releaseState: "unreleased", license: "ODbL-1.0", rightsUrl: LICENSE_URL,
    coverage: receipt.coverage, capturedBy: "sky-archive-operator", transforms: ["Imported prepared local artifact unchanged; preparation manifest retains source assets and transformations."],
    limitation: "Chosen provider observations within Kansas and nearby bounds; missing aircraft and source gaps remain. Private retention is not source admission or publication." } } };
}
function verifyStored(stored, expected) {
  const record = stored?.receipt, wanted = expected.capture.receipt;
  if (!Buffer.isBuffer(stored?.bytes) || stored.bytes.length !== expected.request.limitBytes || hash(stored.bytes) !== wanted.sha256
    || !object(record) || record.captureId !== expected.request.id || record.sha256 !== wanted.sha256 || record.sourcePlanSha256 !== wanted.sourcePlanSha256
    || record.candidatePath !== wanted.candidatePath || record.sourceDay !== wanted.sourceDay || record.lifecycle !== "WORK/QUARANTINE"
    || record.candidateManifestSha256 !== wanted.candidateManifestSha256 || record.evidenceRole !== "EXTERNAL_CONTEXT_ONLY"
    || record.releaseState !== "unreleased" || record.rightsReview !== "pending" || record.sensitivityReview !== "pending") fail("SKY_STORED_INTEGRITY_FAILED");
}

/** --apply is an explicit operator action; config/paused gates are never changed. */
export async function importKansasSkyDay(directory, { apply = false, config = ingestionConfig(), store, storeFactory = getIngestionStore } = {}) {
  const candidate = await verifyKansasSkyDay(directory);
  if (!apply) return candidate.plan;
  const common = { ...candidate.plan, state: "held", imported: 0, existing: 0, complete: false };
  if (candidate.receipt.coverage !== "provider-day-processed") return { ...common, reason: "SKY_PARTIAL_INPUT_HELD" };
  if (!config.ready) return { ...common, reason: "STORAGE_CONFIGURATION_REQUIRED" };
  store ??= await storeFactory();
  let imported = 0, existing = 0;
  for (const artifact of candidate.artifacts) {
    // Verify bytes again immediately before a bounded per-artifact lease.
    const { bytes } = await readBounded(candidate.root, artifact.path, artifact);
    const expected = captureFor(candidate, artifact, bytes);
    const token = await store.claim(Date.now(), "sky-archive-operator");
    if (!token) return { ...common, imported, existing, reason: "PIPELINE_PAUSED_OR_BUSY" };
    let reservation = 0;
    try {
      if (!await store.due(expected.request, token)) {
        let stored;
        try { stored = await store.read(expected.request.id); } catch (error) { if (error.message === "CAPTURE_NOT_FOUND") fail("SKY_RETRY_HELD"); throw error; }
        verifyStored(stored, expected); existing++;
      } else {
        reservation = await store.reserve(expected.request, token);
        await store.save(expected.request, expected.capture, token, reservation); reservation = 0;
        verifyStored(await store.read(expected.request.id), expected); imported++;
      }
    } catch (error) {
      const reason = ["ARCHIVE_LIMIT_REACHED", "LEASE_LOST", "PIPELINE_PAUSED", "SKY_RETRY_HELD", "SKY_STORED_INTEGRITY_FAILED", "CAPTURE_INTEGRITY_FAILED"].includes(error.message) ? error.message : "SKY_STORAGE_UNAVAILABLE";
      try { await store.failure(expected.request, token, reason, reservation); } catch { /* The existing fencing rejects expired workers; reservations remain owned by the store. */ }
      return { ...common, imported, existing, reason };
    } finally { await store.release(token); }
  }
  return { ...common, state: "retained-private", imported, existing, complete: true, collectionActive: false };
}
