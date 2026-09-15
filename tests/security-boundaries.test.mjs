import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const compile = async (name, replacements = {}) => {
  let source = await readFile(new URL(`../app/${name}`, import.meta.url), "utf8");
  for (const [from, to] of Object.entries(replacements)) source = source.replaceAll(`"${from}"`, `"${to}"`);
  return `data:text/javascript;base64,${Buffer.from(ts.transpileModule(source, {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 }, fileName: name,
  }).outputText).toString("base64")}`;
};
const boundedUrl = await compile("bounded-json.ts");
const { readBoundedJson, JsonLimitError } = await import(boundedUrl);
const { POST } = await import(await compile("api/qwen/route.ts", {
  "../../bounded-json": boundedUrl,
  "../../qwen-context": await compile("qwen-context.ts"),
}));
const request = (body, headers = {}) => new Request("https://site.test/api/qwen", {
  method: "POST", headers: { "content-type": "application/json", ...headers }, body: JSON.stringify(body),
});

test("streaming JSON enforces actual bytes and cancels without reading to EOF", async () => {
  let canceled = false;
  let pulls = 0;
  const response = new Response(new ReadableStream({
    pull(controller) { pulls++; controller.enqueue(new TextEncoder().encode("x".repeat(40))); },
    cancel() { canceled = true; },
  }), { headers: { "content-length": "1" } });
  await assert.rejects(readBoundedJson(response, 64), JsonLimitError);
  assert.equal(canceled, true);
  assert.ok(pulls <= 3);
  assert.deepEqual(await readBoundedJson(new Response('{"x":"é"}'), 10), { x: "é" });
  await assert.rejects(readBoundedJson(new Response('{"x":"é"}'), 9), JsonLimitError);
  await assert.rejects(readBoundedJson(new Response(Uint8Array.of(0xff)), 8));
});

test("Qwen rejects malformed, oversized and cross-origin requests with zero upstream calls", async () => {
  const originalFetch = globalThis.fetch;
  let calls = 0;
  globalThis.fetch = async () => { calls++; throw new Error("NETWORK MUST NOT RUN"); };
  try {
    for (const body of [null, [], true, "x", {}, { question: "x", context: [] }, { question: "x", context: null }, { question: "x", endpoint: "https://other.test" }, { question: "x".repeat(1201) }]) {
      const response = await POST(request(body));
      assert.equal(response.status, 400, JSON.stringify(body));
      assert.equal(response.headers.get("cache-control"), "no-store");
    }
    assert.equal((await POST(request({ question: "x", context: { notes: "x".repeat(33 * 1024) } }))).status, 413);
    assert.equal((await POST(request({ question: "x" }, { origin: "https://other.test" }))).status, 403);
    assert.equal((await POST(request({ question: "x" }, { "content-type": "text/plain" }))).status, 415);
    assert.equal((await POST(new Request("https://site.test/api/qwen", { method: "POST", headers: { "content-type": "application/json" }, body: "{" }))).status, 400);
    assert.equal(calls, 0);
  } finally { globalThis.fetch = originalFetch; }
});

test("Qwen configuration, redirects, upstream errors and replies remain bounded", async () => {
  const keys = ["QWEN_ENDPOINT", "QWEN_OLLAMA_URL", "OLLAMA_BASE_URL", "QWEN_API_KEY", "QWEN_MODEL", "OLLAMA_MODEL"];
  const saved = Object.fromEntries(keys.map((key) => [key, process.env[key]]));
  const originalFetch = globalThis.fetch;
  let calls = 0;
  try {
    for (const key of keys) delete process.env[key];
    globalThis.fetch = async () => { calls++; throw new Error("unexpected"); };
    assert.equal((await POST(request({ question: "x" }))).status, 503);
    for (const endpoint of ["file:///etc/passwd", "http://remote.test", "https://user:secret@model.test", "https://model.test?url=elsewhere", "https://model.test/#secret"]) {
      process.env.QWEN_ENDPOINT = endpoint;
      assert.equal((await POST(request({ question: "x" }))).status, 503);
    }
    assert.equal(calls, 0);
    process.env.QWEN_ENDPOINT = "https://model.test";
    let captured;
    globalThis.fetch = async (url, options) => {
      captured = { url, options };
      return Response.json({ error: "PRIVATE_UPSTREAM_DETAIL" }, { status: 500 });
    };
    const failure = await POST(request({ question: "x", context: {} }));
    assert.equal(failure.status, 502);
    assert.doesNotMatch(await failure.text(), /PRIVATE_UPSTREAM_DETAIL/);
    assert.equal(captured.url, "https://model.test/api/chat");
    assert.equal(captured.options.redirect, "manual");
    assert.equal(captured.options.cache, "no-store");
    let redirects = 0;
    globalThis.fetch = async (_url, options) => {
      redirects++;
      assert.equal(options.redirect, "manual");
      return new Response(null, { status: 302, headers: { location: "https://unapproved.test" } });
    };
    assert.equal((await POST(request({ question: "x" }))).status, 502);
    assert.equal(redirects, 1);
    globalThis.fetch = async () => Response.json({ message: { content: "x".repeat(65 * 1024) } });
    assert.equal((await POST(request({ question: "x" }))).status, 502);
    globalThis.fetch = async () => Response.json({ message: { content: "Bounded fixture answer" } });
    const success = await POST(request({ question: "x" }));
    assert.equal(success.status, 200);
    assert.equal((await success.json()).answer, "Bounded fixture answer");
  } finally {
    globalThis.fetch = originalFetch;
    for (const key of keys) { if (saved[key] === undefined) delete process.env[key]; else process.env[key] = saved[key]; }
  }
});

test("the repository status route rejects oversized chunked responses", async () => {
  const { GET } = await import(await compile("api/repository-status/route.ts", { "../../bounded-json": boundedUrl }));
  const originalFetch = globalThis.fetch;
  let canceled = false;
  globalThis.fetch = async () => new Response(new ReadableStream({
    pull(controller) { controller.enqueue(new Uint8Array(256 * 1024)); },
    cancel() { canceled = true; },
  }));
  try {
    const response = await GET();
    assert.equal(response.status, 502);
    assert.equal(canceled, true);
    assert.equal((await response.json()).state, "error");
  } finally { globalThis.fetch = originalFetch; }
});
