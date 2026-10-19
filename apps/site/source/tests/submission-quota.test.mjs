import assert from "node:assert/strict";
import { readFile, readdir } from "node:fs/promises";
import { DatabaseSync } from "node:sqlite";
import test from "node:test";
import ts from "typescript";
import { landFixtures } from "./helpers/land-fixture.mjs";

const read = path => readFile(new URL(`../${path}`, import.meta.url), "utf8");
const url = source => `data:text/javascript;base64,${Buffer.from(ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText).toString("base64")}`;
const intakeUrl = url("const OFFICIAL_CONTEXT_SOURCES=[],SCIENCE_EVENTS=[],EARTH_ENGINE_DATASETS=[];\n" + (await read("app/data-intake.ts")).replace(/^import .*;\n/gm, ""));
const landUrl = url(await read("app/land-records.ts"));
const land = await import(landUrl);
const { fixture, bytes, rehash } = landFixtures(land);
const runtime = { env: {}, user: { id: "quota-user", email: "quota@example.test", displayName: "Quota tester" } };
globalThis.__quota = runtime;
const serverUrl = url((await read("app/data-intake-server.ts"))
  .replace('import { env } from "cloudflare:workers";', "const env=globalThis.__quota.env;")
  .replace('import { getRawDb } from "../db";', "const getRawDb=()=>globalThis.__quota.db;")
  .replace('import { getChatGPTUser } from "./chatgpt-auth";', "const getChatGPTUser=async()=>globalThis.__quota.user;")
  .replace('"./data-intake"', JSON.stringify(intakeUrl)));
const server = await import(serverUrl);
const api = {};
for (const route of ["data-submissions", "land-records"]) api[route] = await import(url((await read(`app/api/${route}/route.ts`))
  .replace('"../../data-intake-server"', JSON.stringify(serverUrl))
  .replace('"../../data-intake"', JSON.stringify(intakeUrl))
  .replace('"../../land-records"', JSON.stringify(landUrl))));

const insertSql = `INSERT INTO data_submissions (id,owner_key,owner_name,title,source_id,source_url,description,license,sensitivity,start_date,end_date,file_name,file_bytes,file_sha256,object_key,status,version,created_at,updated_at)
  VALUES (?,?,'Tester','Synthetic','general','','Synthetic control','Unknown','unknown','','','data.csv',1,?,?, 'submitted',1,?,?)`;
async function setup() {
  const sqlite = new DatabaseSync(":memory:");
  for (const file of (await readdir(new URL("../drizzle/", import.meta.url))).filter(p => p.endsWith(".sql")).sort()) {
    for (const statement of (await read(`drizzle/${file}`)).split("--> statement-breakpoint").filter(p => p.trim())) sqlite.exec(statement);
  }
  const state = { sqlite, objects: new Map(), reads: 0, puts: 0, failPut: false, failBatch: false, failDelete: false, lostCommit: false, failLookup: false };
  const prepare = sql => ({ sql, values: [], bind(...values) { return { ...this, values }; },
    async first() {
      if (state.failLookup && sql === "SELECT id FROM data_submissions WHERE id = ?") throw new Error("D1 read unavailable");
      return sqlite.prepare(sql).get(...this.values) ?? null;
    },
    async all() { return { results: sqlite.prepare(sql).all(...this.values) }; },
    async run() { return { meta: sqlite.prepare(sql).run(...this.values) }; },
  });
  runtime.db = { prepare, async batch(statements) {
    sqlite.exec("BEGIN"); let committed = false;
    try {
      if (state.failBatch) throw new Error("D1 unavailable");
      const results = statements.map(s => ({ meta: sqlite.prepare(s.sql).run(...s.values) }));
      sqlite.exec("COMMIT"); committed = true;
      if (state.lostCommit) throw new Error("D1 response lost after commit");
      return results;
    } catch (error) { if (!committed) sqlite.exec("ROLLBACK"); throw error; }
  } };
  runtime.env.BUCKET = {
    async put(key, value) { state.puts++; state.objects.set(key, value); if (state.failPut) throw new Error("R2 response failed"); },
    async delete(key) { if (state.failDelete) throw new Error("R2 delete unavailable"); state.objects.delete(key); },
  };
  state.owner = (await server.intakeUser()).key;
  state.rows = () => sqlite.prepare("SELECT * FROM data_submissions").all();
  state.pending = () => sqlite.prepare("SELECT * FROM data_submission_uploads").all();
  state.seed = (count, createdAt = new Date().toISOString(), owner = state.owner) => {
    for (let i = 0; i < count; i++) {
      const id = crypto.randomUUID(); sqlite.prepare(insertSql).run(id, owner, "seed", `quarantine/${owner}/${id}`, createdAt, createdAt);
    }
  };
  return state;
}
function upload(state, route, transfer) {
  const form = new FormData();
  const fields = route === "land-records" ? { title: "Synthetic land review", permission: "yes" } : {
    title: "Synthetic observations", sourceId: "general", sourceUrl: "https://example.test/data", description: "Synthetic quota test observations", license: "Unknown", sensitivity: "unknown", startDate: "", endDate: "", permission: "yes",
  };
  for (const [key, value] of Object.entries(fields)) form.set(key, value);
  form.set("file", new Blob([route === "land-records" ? bytes(transfer) : "x,y\n1,2\n"]), route === "land-records" ? "review.json" : "data.csv");
  const request = new Request(`https://kfm.test/api/${route}`, { method: "POST", headers: { Origin: "https://kfm.test" }, body: form });
  const originalReader = request.body.getReader.bind(request.body);
  request.body.getReader = (...args) => { state.reads++; return originalReader(...args); };
  return request;
}
const deferred = () => { let resolve; const promise = new Promise(r => { resolve = r; }); return { promise, resolve }; };

for (const firstRoute of ["data-submissions", "land-records"]) test(`concurrent cross-route uploads reserve the last shared slot before body reads or R2 writes (${firstRoute} first)`, async () => {
  const s = await setup(); s.seed(19);
  const transfers = await Promise.all(Array.from({ length: 12 }, async (_, i) => {
    const v = await fixture(); v.created_at = new Date(Date.parse(v.created_at) + i * 1000).toISOString().replace(".000Z", "Z");
    await rehash(v); await land.validateLandTransfer(bytes(v)); return v;
  }));
  const responses = await Promise.all(Array.from({ length: 12 }, (_, i) => {
    const route = i % 2 ? (firstRoute === "land-records" ? "data-submissions" : "land-records") : firstRoute;
    return api[route].POST(upload(s, route, transfers[i]));
  }));
  assert.equal(responses.filter(r => r.status === 201).length, 1);
  assert.equal(responses.filter(r => r.status === 429).length, 11);
  assert.equal(s.reads, 1); assert.equal(s.puts, 1); assert.equal(s.objects.size, 1);
  assert.equal(s.rows().length, 20); assert.equal(s.pending().length, 0);
  assert.equal((await api["land-records"].POST(upload(s, "land-records", transfers[1]))).status, 429);
  assert.equal(s.reads, 1); s.sqlite.close();
});

test("twenty in-flight uploads fill the quota even without committed rows and cannot age out", async () => {
  const s = await setup(), gate = deferred(), entered = deferred(); let n = 0;
  const active = Array.from({ length: 20 }, () => server.withSubmissionUpload(server.intakeStore(), s.owner, async () => { if (++n === 20) entered.resolve(); await gate.promise; }));
  await entered.promise;
  s.sqlite.prepare("UPDATE data_submission_uploads SET created_at = '2000-01-01T00:00:00.000Z'").run();
  await assert.rejects(server.withSubmissionUpload(server.intakeStore(), s.owner, async () => assert.fail("must not read body")), error => error.status === 429);
  assert.equal(s.pending().length, 20); assert.equal(s.rows().length, 0);
  gate.resolve(); await Promise.all(active); assert.equal(s.pending().length, 0); s.sqlite.close();
});

test("rolling cutoff is inclusive, counts all review states and sources, and isolates owners", async () => {
  const s = await setup(), now = Date.parse("2026-10-19T12:00:00Z"), original = Date.now;
  s.seed(19, new Date(now - 86_400_000).toISOString());
  s.seed(5, new Date(now - 86_400_001).toISOString()); s.seed(25, new Date(now).toISOString(), "other-owner");
  s.sqlite.exec("UPDATE data_submissions SET status='rejected',source_id='land-records'");
  Date.now = () => now;
  try {
    await server.withSubmissionUpload(server.intakeStore(), s.owner, async () => {
      await assert.rejects(server.withSubmissionUpload(server.intakeStore(), s.owner, async () => {}), error => error.status === 429);
    });
    Date.now = () => now + 1;
    let entered = 0;
    await server.withSubmissionUpload(server.intakeStore(), s.owner, async () => {
      await server.withSubmissionUpload(server.intakeStore(), s.owner, async () => { entered++; });
    });
    assert.equal(entered, 1);
  } finally { Date.now = original; s.sqlite.close(); }
});

test("invalid bodies release capacity and valid sequential uploads and land replay retain contracts", async () => {
  const s = await setup(), transfer = await fixture();
  const invalid = upload(s, "data-submissions"); invalid.headers.set("content-type", "text/plain");
  assert.equal((await api["data-submissions"].POST(invalid)).status, 413);
  assert.equal(s.pending().length, 0); assert.equal(s.puts, 0);
  const general = await api["data-submissions"].POST(upload(s, "data-submissions"));
  assert.equal(general.status, 201); assert.equal((await general.json()).status, "submitted");
  assert.equal(general.headers.get("cache-control"), "private, no-store");
  const first = await api["land-records"].POST(upload(s, "land-records", transfer));
  assert.equal(first.status, 201); const receipt = await first.json(); assert.equal(receipt.releaseState, "UNRELEASED");
  const replay = await api["land-records"].POST(upload(s, "land-records", transfer));
  assert.equal(replay.status, 200); assert.equal((await replay.json()).id, receipt.id);
  assert.equal(s.puts, 2); assert.equal(s.rows().length, 2); assert.equal(s.pending().length, 0); s.sqlite.close();
});

for (const failure of ["failPut", "failBatch"]) test(`${failure} cleans the request object before releasing its reservation`, async () => {
  const s = await setup(); s[failure] = true;
  assert.equal((await api["data-submissions"].POST(upload(s, "data-submissions"))).status, 503);
  assert.equal(s.objects.size, 0); assert.equal(s.pending().length, 0); assert.equal(s.rows().length, 0);
  s[failure] = false;
  assert.equal((await api["data-submissions"].POST(upload(s, "data-submissions"))).status, 201); s.sqlite.close();
});

for (const uncertain of ["failDelete", "failLookup"]) test(`${uncertain} retains the reservation and blocks excess storage`, async () => {
  const s = await setup(); s.seed(19); s.failBatch = true; s[uncertain] = true;
  assert.equal((await api["data-submissions"].POST(upload(s, "data-submissions"))).status, 503);
  assert.equal(s.objects.size, 1); assert.equal(s.pending().length, 1);
  const reads = s.reads;
  assert.equal((await api["data-submissions"].POST(upload(s, "data-submissions"))).status, 429);
  assert.equal(s.reads, reads); assert.equal(s.puts, 1); s.sqlite.close();
});

test("a lost response after D1 commit preserves the completed object's bytes and quota", async () => {
  const s = await setup(); s.seed(19); s.lostCommit = true;
  assert.equal((await api["data-submissions"].POST(upload(s, "data-submissions"))).status, 503);
  assert.equal(s.rows().length, 20); assert.equal(s.pending().length, 0); assert.equal(s.objects.size, 1);
  assert.equal((await api["data-submissions"].POST(upload(s, "data-submissions"))).status, 429); s.sqlite.close();
});
