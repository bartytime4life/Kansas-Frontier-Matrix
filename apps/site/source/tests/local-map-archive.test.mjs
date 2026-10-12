import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { createHash, webcrypto } from "node:crypto";
import { spawnSync } from "node:child_process";
import test from "node:test";
import ts from "typescript";
const source = await readFile("app/local-map-archive.ts", "utf8");
const js = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const archiveModuleUrl = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`;
const { filterLocalMaps, LocalPdfSession, MAX_LOCAL_PDF_BYTES } = await import(archiveModuleUrl);
const inventory = JSON.parse(await readFile("app/local-map-archive-inventory.json", "utf8"));
const all = { collection: "all", text: "", year: "all", issuesOnly: false };
const bytes = new TextEncoder().encode("%PDF-1.7 synthetic unit-test bytes only\n").buffer;
const sha256 = createHash("sha256").update(new Uint8Array(bytes)).digest("hex");
const sheet = { id: "test", fileName: "test.pdf", sizeBytes: bytes.byteLength, sha256 };
const file = overrides => ({ name: "test.pdf", size: bytes.byteLength, arrayBuffer: async () => bytes, ...overrides });
function session(digest = data => webcrypto.subtle.digest("SHA-256", data)) {
  const created = [], revoked = [];
  return { created, revoked, checker: new LocalPdfSession({ digest, createUrl: blob => { created.push(blob); return `blob:test-${created.length}`; }, revokeUrl: url => revoked.push(url) }) };
}
test("all six preserved collections and source flags remain discoverable without year promotion", () => {
  assert.equal(inventory.records.length, 596);
  assert.equal(new Set(inventory.records.map(row => row.id)).size, 596);
  assert.deepEqual(inventory.collections.map(collection => filterLocalMaps(inventory.records, { ...all, collection }).length), [105, 55, 105, 100, 191, 40]);
  assert.equal(inventory.records.filter(row => row.alignment === "embedded-control-unreviewed").length, 185);
  assert.equal(filterLocalMaps(inventory.records, { ...all, issuesOnly: true }).length, 4);
  for (const row of inventory.records) { assert.match(row.sha256, /^[a-f0-9]{64}$/); assert.ok(row.sizeBytes > 0 && row.sizeBytes <= MAX_LOCAL_PDF_BYTES); }
  const conflicts = inventory.records.filter(row => row.flags.includes("conflicting-filenames"));
  assert.equal(conflicts.length, 2); assert.equal(conflicts[0].sha256, conflicts[1].sha256);
  for (const row of conflicts) { assert.equal(row.startYear, null); assert.equal(row.placeHint, null); assert.equal(row.editionBasis, "identity-conflict"); }
  assert.equal(filterLocalMaps(conflicts, { ...all, year: "1972" }).length, 0);
  assert.equal(filterLocalMaps(conflicts, { ...all, year: "unknown", text: "1972" }).length, 1);
  assert.equal(filterLocalMaps(inventory.records, { ...all, collection: "KFM Historic County Township Maps", text: "Allen", year: "1976" }).length, 1);
  assert.equal(filterLocalMaps(inventory.records, { ...all, text: "invented nonexistent" }).length, 0);
  assert.equal(filterLocalMaps(inventory.records, { ...all, collection: "Kansas Road Maps", year: "2024" }).some(row => row.editionLabel === "2023–2024"), true);
});
test("only exact selected PDF bytes create a local object URL, which clear revokes", async () => {
  const s = session(); const result = await s.checker.check(file(), sheet);
  assert.equal(result.state, "matched"); assert.equal(result.sheetId, "test"); assert.equal(s.created.length, 1);
  assert.equal(s.created[0].type, "application/pdf"); assert.equal(s.created[0].size, bytes.byteLength);
  s.checker.clear(); assert.deepEqual(s.revoked, [result.url]); s.checker.clear(); assert.equal(s.revoked.length, 1);
});
test("wrong name/size, oversized files, non-PDF bodies and hash mismatches stay closed", async () => {
  for (const bad of [file({ name: "different.pdf" }), file({ size: 1 }), file({ size: MAX_LOCAL_PDF_BYTES + 1 })]) {
    bad.arrayBuffer = () => assert.fail("metadata rejection read bytes");
    const s = session(); assert.equal((await s.checker.check(bad, sheet)).state, "blocked"); assert.equal(s.created.length, 0);
  }
  for (const data of [new ArrayBuffer(bytes.byteLength), new TextEncoder().encode("%PDF-1.7 altered contents".padEnd(bytes.byteLength, " ")).buffer]) {
    const s = session(); assert.equal((await s.checker.check(file({ arrayBuffer: async () => data }), sheet)).state, "blocked"); assert.equal(s.created.length, 0);
  }
  const s = session(); assert.equal((await s.checker.check(file({ arrayBuffer: async () => { throw new Error("device unavailable"); } }), sheet)).state, "blocked");
  assert.equal(s.created.length, 0);
});
test("cancelled file reads and replaced sheets never create a stale preview", async () => {
  let finishRead; const s = session();
  const pending = s.checker.check(file({ arrayBuffer: () => new Promise(resolve => { finishRead = resolve; }) }), sheet);
  s.checker.clear(); finishRead(bytes);
  assert.equal((await pending).state, "cancelled"); assert.equal(s.created.length, 0);
  let finishDigest; const digest = session(() => new Promise(resolve => { finishDigest = resolve; }));
  const checking = digest.checker.check(file(), sheet);
  await new Promise(resolve => setImmediate(resolve));
  digest.checker.clear();
  const other = session(); assert.equal((await other.checker.check(file({ arrayBuffer: () => assert.fail("parallel digest read") }), sheet)).state, "blocked");
  finishDigest(await webcrypto.subtle.digest("SHA-256", bytes));
  assert.equal((await checking).state, "cancelled"); assert.equal(digest.created.length, 0);
  assert.equal((await other.checker.check(file(), sheet)).state, "matched"); other.checker.clear();
});
test("inventory projection is deterministic and rejects stale provenance and unsafe identities", () => {
  const script = `
import runpy
p=runpy.run_path('scripts/project-local-map-archive.py')['project']
h='a'*64
r={'createdAt':'2026-10-03T00:00:00Z','files':[{'path':'Kansas Road Maps/1950-1951 Kansas.pdf','bytes':100,'sha256':h}]}
x=p(r,{'rows':[]},[],[]);assert x==p(r,{'rows':[]},[],[])
assert x['records'][0]['startYear']==1950 and x['records'][0]['endYear']==1951
for path in ['../../private.pdf','/Kansas Road Maps/a.pdf','Kansas Road Maps/../a.pdf']:
 try:p({'createdAt':'x','files':[{'path':path,'bytes':100,'sha256':h}]},{'rows':[]},[],[]);raise AssertionError('unsafe path passed')
 except ValueError:pass
try:p(r,{'rows':[]},[{'source_path':r['files'][0]['path'],'sha256':'b'*64}],[]);raise AssertionError('stale metadata passed')
except ValueError:pass
try:p(r,{'rows':[]},[{'source_path':'same'},{'source_path':'same'}],[]);raise AssertionError('duplicate metadata passed')
except ValueError:pass
`;
  const result = spawnSync("python3", ["-c", script], { encoding: "utf8" }); assert.equal(result.status, 0, result.stderr);
});
test("archive component renders bounded keyboard controls without loading any original", async () => {
  const { createElement } = await import("react");
  const { renderToStaticMarkup } = await import("react-dom/server");
  const inventoryUrl = `data:text/javascript;base64,${Buffer.from(`export default ${JSON.stringify(inventory)}`).toString("base64")}`;
  let browser = ts.transpileModule(await readFile("app/local-map-archive-browser.tsx", "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.ReactJSX } }).outputText;
  for (const [from, to] of [["react", import.meta.resolve("react")], ["react/jsx-runtime", import.meta.resolve("react/jsx-runtime")], ["./local-map-archive", archiveModuleUrl], ["./local-map-archive-inventory.json", inventoryUrl]]) browser = browser.replaceAll(`from "${from}"`, `from "${to}"`);
  const { default: Browser } = await import(`data:text/javascript;base64,${Buffer.from(browser).toString("base64")}`);
  const html = renderToStaticMarkup(createElement(Browser));
  assert.match(html, /596 PDF records/); assert.match(html, /Unknown or withheld/); assert.match(html, /Flagged sources only/);
  assert.equal((html.match(/aria-pressed="false"/g) ?? []).length, 20);
  assert.match(html, /Page 1 of 30/); assert.doesNotMatch(html, /<iframe|<object|<embed|blob:|type="file"/);
});
