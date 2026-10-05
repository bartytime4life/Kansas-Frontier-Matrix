import assert from "node:assert/strict";
import { chmodSync, mkdirSync, mkdtempSync, readFileSync, rmSync, symlinkSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import test from "node:test";
import { spawn } from "node:child_process";
import { request as httpRequest } from "node:http";
import { createServer } from "node:net";
import { fileURLToPath } from "node:url";
import { readUsgsApiKey, assertNoLocalSecretFiles, checkedPath, collectModules, localEntry, parseArguments, prepareWorker, validateConfiguration } from "../scripts/serve-local-worker.mjs";

const config = JSON.parse(readFileSync(new URL("../dist/server/wrangler.json", import.meta.url)));
const hosting = JSON.parse(readFileSync(new URL("../.openai/hosting.json", import.meta.url)));

test("local launcher requires explicit existing storage and constrains the imagery exception", () => {
  assert.throws(() => parseArguments([]), /EXISTING_STATE_REQUIRED/);
  assert.throws(() => parseArguments(["--state", "--port", "4173"]), /INVALID_ARGUMENT/);
  for (const value of ["0", "80", "65536", "4173junk", "-1"]) assert.throws(() => parseArguments(["--state", "/tmp/state", "--port", value]));
  assert.throws(() => parseArguments(["--state", "/tmp/state", "--host", "0.0.0.0"]), /INVALID_ARGUMENT/);
  assert.throws(() => parseArguments(["--state", "/tmp/state", "--state", "/tmp/other"]), /DUPLICATE_ARGUMENT/);
  assert.throws(() => parseArguments(["--state", "/tmp/state", "--port", "4175", "--local-reviewed-imagery"]), /IMAGERY_ORIGIN/);
  assert.equal(parseArguments(["--state", "/tmp/state"]).localReviewedImagery, false);
  assert.equal(parseArguments(["--state", "/tmp/state", "--local-reviewed-imagery"]).port, 4173);
});

test("built Site configuration is recognized without changing its storage identities", () => {
  const before = JSON.stringify(config);
  validateConfiguration(config, hosting);
  assert.equal(JSON.stringify(config), before);
  assert.throws(() => validateConfiguration(config, { project_id: "another-site" }), /WRONG_SITE/);
  for (const edit of [
    (c) => { c.r2_buckets[0].bucket_name = "new-empty-store"; },
    (c) => { c.d1_databases[0].database_id = "another-database"; },
    (c) => { c.d1_databases[0].remote = true; },
    (c) => { c.assets.directory = "../.."; },
    (c) => { c.rules.push({ type: "CommonJS", globs: ["**/*"] }); },
    (c) => { c.vars.OWNER = "true"; },
  ]) {
    const changed = structuredClone(config); edit(changed);
    assert.throws(() => validateConfiguration(changed, hosting));
  }
});

function withDirectory(fn) {
  const directory = mkdtempSync(path.join(tmpdir(), "kfm-runtime-test-"));
  try { fn(directory); } finally { rmSync(directory, { recursive: true, force: true }); }
}

test("direct runtime refuses dotenv and dev-vars configuration without reading secrets", () => withDirectory((directory) => {
  writeFileSync(path.join(directory, "environment-notes.md"), "ordinary documentation");
  assert.doesNotThrow(() => assertNoLocalSecretFiles(directory));
  for (const name of [".env", ".env.local", ".env.production", ".dev.vars", ".dev.vars.local"]) {
    const file = path.join(directory, name);
    writeFileSync(file, "PRIVATE_TEST_VALUE=do-not-read", { mode: 0o000 });
    assert.throws(() => assertNoLocalSecretFiles(directory), /^Error: LOCAL_SECRET_CONFIGURATION_REQUIRES_REVIEW$/);
    rmSync(file);
  }
}));

test("state paths reject missing, symlinked, and publicly writable directories", () => withDirectory((directory) => {
  checkedPath(directory, true);
  assert.throws(() => checkedPath(path.join(directory, "missing"), true));
  symlinkSync(directory, path.join(directory, "alias"));
  assert.throws(() => checkedPath(path.join(directory, "alias"), true), /SYMLINK/);
  chmodSync(directory, 0o777);
  assert.throws(() => checkedPath(directory, true), /UNSAFE_PATH/);
}));

test("module discovery keeps the entry first and cannot escape or exceed its bounds", () => withDirectory((directory) => {
  mkdirSync(path.join(directory, "chunks"));
  writeFileSync(path.join(directory, "index.js"), "import './chunks/a.mjs'");
  writeFileSync(path.join(directory, "chunks/a.mjs"), "export const a = 1");
  writeFileSync(path.join(directory, "schema.sql"), "select 1");
  const modules = collectModules(directory);
  assert.equal(modules[0].path, path.join(directory, "index.js"));
  assert.ok(modules.some((m) => m.type === "Text"));
  assert.throws(() => collectModules(directory, 1), /ENTRY_LIMIT/);
  assert.throws(() => collectModules(directory, 10, 1), /BYTE_LIMIT/);
  symlinkSync(path.join(directory, "index.js"), path.join(directory, "chunks/outside.js"));
  assert.throws(() => collectModules(directory), /SYMLINK/);
}));

const translated = () => ({
  main: "/build/server/index.js", externalWorkers: [], define: {},
  workerOptions: {
    modulesRules: [], assets: { directory: "/build/client" }, bindings: {},
    r2Buckets: { BUCKET: { id: "site-creator-r2" } },
    d1Databases: { DB: { id: "00000000-0000-4000-8000-000000000000" } },
  },
});

test("configuration translation refuses additional workers, remote bindings, or authority variables", () => {
  for (const edit of [
    (t) => t.externalWorkers.push({ name: "extra" }),
    (t) => { t.workerOptions.serviceBindings = { OWNER: "admin" }; },
    (t) => { t.workerOptions.bindings = { KFM_LOCAL_REVIEWED_IMAGERY_ORIGIN: "https://evil.example" }; },
    (t) => { t.workerOptions.r2Buckets.BUCKET.remoteProxyConnectionString = "remote"; },
  ]) {
    const changed = translated(); edit(changed);
    assert.throws(() => prepareWorker(changed, "/build/server", "/build/client", [], false));
  }
  const ordinary = prepareWorker(translated(), "/build/server", "/build/client", [], false);
  assert.deepEqual(ordinary.bindings, {});
  const local = prepareWorker(translated(), "/build/server", "/build/client", [], true);
  assert.deepEqual(local.bindings, { KFM_LOCAL_REVIEWED_IMAGERY_ORIGIN: "http://127.0.0.1:4173" });
  assert.deepEqual(local.d1Databases, ordinary.d1Databases);
  assert.deepEqual(local.r2Buckets, ordinary.r2Buckets);
});

test("local entry rejects forged edge identity and a rebound Host before invoking the application", async () => {
  const application = `export const marker = 'preserved'; export default { fetch: async (request) => Response.json({ body: await request.text(), method: request.method }), scheduled: () => 'preserved' }`;
  const url = `data:text/javascript;base64,${Buffer.from(application).toString("base64")}`;
  const entryModule = await import(`data:text/javascript;base64,${Buffer.from(localEntry(4173).replaceAll('"./index.js"', JSON.stringify(url))).toString("base64")}`);
  assert.equal(entryModule.marker, "preserved");
  assert.equal(entryModule.default.scheduled(), "preserved");
  for (const request of [
    new Request("http://attacker.example:4173/api/governed/v1/knowledge"),
    new Request("http://127.0.0.1:4173/", { headers: { "OAI-Authenticated-User-Email": "owner@example.com" } }),
    new Request("http://127.0.0.1:4173/", { headers: { "oai-authenticated-user-id": "owner" } }),
  ]) assert.equal((await entryModule.default.fetch(request)).status, 403);
  const response = await entryModule.default.fetch(new Request("http://127.0.0.1:4173/api/historical-topo/activate", { method: "POST", body: "bounded control" }));
  assert.deepEqual(await response.json(), { method: "POST", body: "bounded control" });
});

test("built local runtime survives abandoned denials and rejects forged authority over HTTP", { timeout: 30000 }, async () => {
  const directory = mkdtempSync(path.join(tmpdir(), "kfm-runtime-http-"));
  // Explicitly empty, disposable test stores; never the operator's data.
  mkdirSync(path.join(directory, "v3/d1"), { recursive: true });
  mkdirSync(path.join(directory, "v3/r2"), { recursive: true });
  const reservation = createServer();
  await new Promise((resolve, reject) => { reservation.once("error", reject); reservation.listen(0, "127.0.0.1", resolve); });
  const port = reservation.address().port;
  await new Promise((resolve) => reservation.close(resolve));
  const child = spawn(process.execPath, [fileURLToPath(new URL("../scripts/serve-local-worker.mjs", import.meta.url)), "--state", directory, "--port", String(port)], { stdio: ["ignore", "pipe", "pipe"] });
  const exited = new Promise((resolve) => child.once("exit", (code) => resolve(code)));
  const origin = `http://127.0.0.1:${port}`;
  const probe = (pathname, method = "GET", headers = {}, abandon = false) => new Promise((resolve, reject) => {
    const req = httpRequest(origin + pathname, { method, agent: false, headers: { Origin: origin, "Content-Type": "application/json", ...headers } }, (response) => {
      const status = response.statusCode;
      if (abandon) { response.destroy(); resolve(status); return; }
      response.resume(); response.once("end", () => resolve(status)); response.once("error", reject);
    });
    req.setTimeout(3000, () => req.destroy(new Error("HTTP_TEST_TIMEOUT")));
    req.once("error", reject);
    req.end(method === "POST" ? "{}" : undefined);
  });
  try {
    await new Promise((resolve, reject) => {
      const timer = setTimeout(() => reject(new Error("RUNTIME_START_TIMEOUT")), 10000);
      let output = "";
      child.stdout.on("data", (chunk) => {
        output = (output + chunk.toString()).slice(-4096);
        if (output.includes('"event":"local_runtime_ready"')) { clearTimeout(timer); resolve(); }
      });
      child.stderr.resume();
      child.once("error", (error) => { clearTimeout(timer); reject(error); });
      child.once("exit", (code) => { clearTimeout(timer); reject(new Error(`RUNTIME_EARLY_EXIT_${code}`)); });
    });
    for (let i = 0; i < 5; i++) {
      assert.equal(await probe("/api/earth-engine-context/activate", "POST", {}, true), 401);
      assert.equal(await probe("/api/historical-topo/activate", "POST"), 401);
      assert.equal(await probe("/api/historical-topo/review?scan=122705"), 401);
    }
    assert.equal(await probe("/api/earth-engine-context/catalog", "GET", { "oai-authenticated-user-email": "owner@example.com" }), 403);
    assert.equal(await probe("/api/earth-engine-context/catalog", "GET", { Host: "attacker.invalid" }), 403);
    assert.equal(await probe("/api/earth-engine-context/catalog"), 401);
    assert.equal(await probe("/maplibre/maplibre-gl-worker.mjs"), 200);
  } finally {
    child.kill("SIGTERM");
    const timer = setTimeout(() => child.kill("SIGKILL"), 5000);
    try { assert.equal(await exited, 0); } finally { clearTimeout(timer); rmSync(directory, { recursive: true, force: true }); }
  }
});


test("USGS key file is optional, private, bounded and never follows symlinks", () => {
  const root=mkdtempSync(path.join(tmpdir(),"kfm-usgs-key-"));
  const file=path.join(root,"key");
  try {
    assert.equal(readUsgsApiKey(file),null);
    writeFileSync(file,"test-key-only-not-a-real-key",{mode:0o600});
    assert.equal(readUsgsApiKey(file),"test-key-only-not-a-real-key");
    chmodSync(file,0o644);assert.throws(()=>readUsgsApiKey(file),/USGS_KEY_FILE_UNSAFE/);
    chmodSync(file,0o600);symlinkSync(file,path.join(root,"link"));assert.throws(()=>readUsgsApiKey(path.join(root,"link")),/USGS_KEY_FILE_UNSAFE/);
    writeFileSync(file,"x".repeat(257));assert.throws(()=>readUsgsApiKey(file),/USGS_KEY_FILE_UNSAFE/);
    writeFileSync(file,"bad\nheader");assert.throws(()=>readUsgsApiKey(file),/USGS_KEY_FILE_INVALID/);
  } finally { rmSync(root,{recursive:true,force:true}); }
});
