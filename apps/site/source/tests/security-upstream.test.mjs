import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import "./cloudflare-register.mjs";
import test from "node:test";
import ts from "typescript";

const noaaSource = await readFile(new URL("../app/api/hydrology/noaa/route.ts", import.meta.url), "utf8");
const shim = "data:text/javascript,export const NextResponse={json:(body,init)=>Response.json(body,init)}";
const noaaJavaScript = ts.transpileModule(noaaSource.replace('from "next/server"', `from "${shim}"`), {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
}).outputText;
const { GET: noaaGet } = await import(`data:text/javascript;base64,${Buffer.from(noaaJavaScript).toString("base64")}`);

test("NOAA hydrology refuses redirects and retains the Kansas network response", async () => {
  const originalFetch = globalThis.fetch;
  const calls = [];
  const request = { nextUrl: new URL("http://localhost/api/hydrology/noaa?mode=network") };
  try {
    globalThis.fetch = async (input, init) => {
      calls.push(String(input));
      assert.equal(init.redirect, "manual");
      return new Response(null, { status: 302, headers: { location: "http://127.0.0.1/private" } });
    };
    const rejected = await noaaGet(request);
    assert.equal(rejected.status, 502);
    assert.equal((await rejected.json()).error.code, "NOAA_UPSTREAM_STATUS");
    assert.equal(calls.length, 1);

    globalThis.fetch = async (input, init) => {
      calls.push(String(input));
      assert.equal(init.redirect, "manual");
      return Response.json({ gauges: [] });
    };
    const accepted = await noaaGet(request);
    assert.equal(accepted.status, 200);
    const payload = await accepted.json();
    assert.equal(payload.mode, "network");
    assert.deepEqual(payload.records, []);
    assert.equal(calls.length, 2);
  } finally { globalThis.fetch = originalFetch; }
});

test("malformed NASA fire dates cannot reach an upstream", async () => {
  const workerUrl = new URL("../dist/server/index.js", import.meta.url);
  workerUrl.searchParams.set("test", `gibs-security-${process.pid}-${Date.now()}`);
  const { default: worker } = await import(workerUrl.href);
  const originalFetch = globalThis.fetch;
  let calls = 0;
  try {
    globalThis.fetch = async () => { calls++; throw new Error("Unexpected upstream request"); };
    const response = await worker.fetch(new Request("http://localhost/api/live-context?feed=nasa-gibs-fire-points&day=2026-09-26%2F..%2Fprivate"), {}, { waitUntil() {}, passThroughOnException() {} });
    assert.equal(response.status, 400);
    assert.equal(calls, 0);
  } finally { globalThis.fetch = originalFetch; }
});
