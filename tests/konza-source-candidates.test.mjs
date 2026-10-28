import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";
import { CAPTURE_SOURCES, captureRequest } from "../server/ingestion-sources.mjs";

const moduleUrls = new Map();
async function moduleUrl(name) {
  if (moduleUrls.has(name)) return moduleUrls.get(name);
  let js = ts.transpileModule(await readFile(new URL(`../app/${name}.ts`, import.meta.url), "utf8"), {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  }).outputText;
  for (const [, dependency] of [...js.matchAll(/from "\.\/([a-z-]+)"/g)]) {
    js = js.replaceAll(`from "./${dependency}"`, `from "${await moduleUrl(dependency)}"`);
  }
  const url = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`;
  moduleUrls.set(name, url);
  return url;
}

const catalog = await import(await moduleUrl("source-intelligence"));
const microbiomeId = "SRC-CAND-USDA-KNZ-SOIL-MICROBIOME-2020";
const riparianId = "SRC-CAND-KNZ-RIPARIAN-2014-C2015";
const candidate = id => {
  const found = catalog.SOURCE_CANDIDATES.find(source => source.id === id);
  assert.ok(found, `Missing research candidate ${id}`);
  return found;
};

test("Konza references stay unique, held and outside automatic capture and map activation", () => {
  const ids = catalog.SOURCE_CANDIDATES.map(source => source.id);
  assert.equal(new Set(ids).size, ids.length);
  assert.ok(catalog.SOURCE_DOMAINS.includes("Ecology"));
  for (const id of [microbiomeId, riparianId]) {
    const source = candidate(id);
    assert.equal(catalog.SOURCE_ADMISSION_BY_ID[id], "held");
    assert.match(source.sourceRole, /not connected or admitted/);
    assert.equal(source.checkedAt, "2026-10-28");
    assert.equal(source.layerId, undefined);
    assert.equal(source.featureId, undefined);
    assert.equal(source.discoveryPath, undefined);
    assert.equal(CAPTURE_SOURCES.some(capture => capture.id === id), false);
    assert.throws(() => captureRequest(id), /SOURCE_NOT_ALLOWED/);
    assert.match(source.nextGate, /immutable.*bytes.*hash/);
    assert.match(source.nextGate, /rights.*sensitivity/);
    assert.match(source.nextGate, /EvidenceBundle.*admission\/release/);
  }
});

test("soil microbiome discovery keeps seasonal observation scope separate from catalog review", () => {
  const source = candidate(microbiomeId);
  assert.equal(new URL(source.sourceUrl).host, "catalog.data.gov");
  assert.match(source.value, /10\.15482\/USDA\.ADC\/1528782/);
  assert.match(source.value, /PRJNA862140/);
  assert.match(source.value, /CC BY 4\.0/);
  assert.match(source.cadence, /2020-09-04.*2020-12-10/);
  assert.match(source.cannotProve, /not other ecosystems.*year-round/);
  assert.match(source.cannotProve, /No sequences or sampling locations are loaded/);
  assert.match(source.nextGate, /NCBI records remain unverified/);
});

test("riparian discovery binds original research to its corrected watershed population", () => {
  const source = candidate(riparianId);
  assert.equal(new URL(source.sourceUrl).searchParams.get("id"), "10.1371/journal.pone.0129409");
  assert.match(source.value, /10\.1371\/journal\.pone\.0106922/);
  assert.match(source.value, /10\.1371\/journal\.pone\.0129409/);
  assert.match(source.value, /20 of 54 watersheds/);
  assert.match(source.value, /no cattle-versus-native-grazer comparison/);
  assert.match(source.cannotProve, /uncorrected 22-watershed count/);
  assert.match(source.nextGate, /original publication and correction bound together/);
  assert.match(source.nextGate, /corrected watershed identities, dates and schema/);
});
