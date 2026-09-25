import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const compile = async (path, replacements = {}) => {
  let source = await readFile(new URL(`../app/${path}`, import.meta.url), "utf8");
  for (const [from, to] of Object.entries(replacements)) source = source.replaceAll(`"${from}"`, `"${to}"`);
  return `data:text/javascript;base64,${Buffer.from(ts.transpileModule(source, {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 }, fileName: path,
  }).outputText).toString("base64")}`;
};
const observationModule = await compile("repository-status.ts");
const { parseRepositoryObservation, REPOSITORY_STATUS_TTL_MS } = await import(observationModule);
const now = Date.parse("2026-09-24T23:00:00Z");
const snapshot = {
  state: "ready", repository: "bartytime4life/Kansas-Frontier-Matrix", ref: "main",
  mode: "READ_ONLY_PUBLIC_METADATA", synchronization: "SITE_SOURCE_SEPARATE",
  commit: "A".repeat(40), shortCommit: "incorrect", observedAt: new Date(now).toISOString(),
};

test("currentness expires from observation time and derives its short identity", () => {
  assert.equal(parseRepositoryObservation(snapshot, now).shortCommit, "aaaaaaa");
  assert.equal(parseRepositoryObservation(snapshot, now + REPOSITORY_STATUS_TTL_MS - 1).state, "ready");
  assert.equal(parseRepositoryObservation(snapshot, now + REPOSITORY_STATUS_TTL_MS).state, "stale");
  for (const patch of [{ observedAt: undefined }, { observedAt: "invalid" },
    { observedAt: new Date(now + 1).toISOString() }, { repository: "another/repo" },
    { ref: "other" }, { mode: "MUTATION" }, { synchronization: "SYNCED" }, { commit: "bad" }]) {
    assert.throws(() => parseRepositoryObservation({ ...snapshot, ...patch }, now));
  }
});

test("cached GitHub observations retain their age, expire, and never become stale HTTP success", async () => {
  const { GET } = await import(await compile("api/repository-status/route.ts", {
    "../../bounded-json": await compile("bounded-json.ts"), "../../repository-status": observationModule,
  }));
  const originalFetch = globalThis.fetch;
  const originalNow = Date.now;
  let clock = originalNow();
  let calls = 0;
  let reject = false;
  let canceled = false;
  Date.now = () => clock;
  globalThis.fetch = async () => {
    calls++;
    return reject ? new Response(new ReadableStream({ cancel() { canceled = true; } }), { status: 302 })
      : Response.json({ commit: { sha: "b".repeat(40), commit: { message: "Inspected metadata" } } });
  };
  try {
    const first = await GET();
    assert.equal(first.headers.get("cache-control"), "no-store");
    const value = await first.json();
    clock = Date.parse(value.observedAt) + 59_000;
    const cached = await GET();
    assert.equal(cached.headers.get("cache-control"), "no-store");
    assert.deepEqual(await cached.json(), value);
    assert.equal(calls, 1);
    clock = Date.parse(value.observedAt) + REPOSITORY_STATUS_TTL_MS;
    reject = true;
    const expired = await GET();
    assert.equal(expired.status, 502);
    assert.equal((await expired.json()).state, "error");
    assert.equal(calls, 2);
    assert.equal(canceled, true);
  } finally { globalThis.fetch = originalFetch; Date.now = originalNow; }
});
