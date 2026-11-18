import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";
import { componentHarness } from "./component-harness.mjs";

// Owner release console: an unreadable successful reply must report an unknown state,
// never "no package active" with the Activate button enabled.
const cjs = async path => {
  const loaded = { exports: {} };
  const code = ts.transpileModule(await readFile(path, "utf8"), { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText;
  new Function("exports", "module", "require", code)(loaded.exports, loaded, () => ({}));
  return loaded.exports;
};
const bounded = await cjs("app/bounded-json.ts");
const expiry = await cjs("app/water-release-expiry.ts");

async function consoleWith(reply) {
  const calls = [];
  const fetch = async (url, init) => { calls.push({ url: String(url), init }); return reply(); };
  const h = await componentHarness("app/water-release-console.tsx", { "./bounded-json": bounded, "./water-release-expiry": expiry },
    { fetch, Response, ReadableStream, TextDecoder, TextEncoder, Uint8Array, JSON, setInterval, clearInterval },
    "\nexports.__fetchStatus = fetchStatus;\nexports.__readAdminBody = readAdminBody;");
  return { h, calls };
}

test("an unreadable successful status reply is unavailable, not an empty active state", async () => {
  for (const reply of [
    () => new Response("<html>gateway</html>", { status: 200 }),
    () => new Response(JSON.stringify(["not", "an", "object"]), { status: 200 }),
    () => new Response("x".repeat(300 * 1024), { status: 200 }),
    () => new Response(new ReadableStream({ start(controller) { controller.enqueue(new TextEncoder().encode('{"active_package_id":')); controller.error(new Error("connection reset")); } }), { status: 200 }),
  ]) {
    const { h } = await consoleWith(reply);
    const result = await h.exports.__fetchStatus("water");
    assert.equal(result.status, null, "no status object means Activate stays disabled");
    assert.match(result.message, /Status is unavailable right now/);
    h.dispose();
  }
});

test("refused replies keep their reason text even when the body is unreadable, and valid replies still load", async () => {
  let { h } = await consoleWith(() => new Response("upstream error page", { status: 503 }));
  let result = await h.exports.__fetchStatus("water");
  assert.equal(result.status, null);
  assert.equal(result.message, "Status unavailable (NO_REASON_SUPPLIED).");
  h.dispose();

  ({ h } = await consoleWith(() => Response.json({ reason_code: "AUTHENTICATION_REQUIRED" }, { status: 401 })));
  result = await h.exports.__fetchStatus("water");
  assert.equal(result.status, null);
  assert.match(result.message, /AUTHENTICATION_REQUIRED|Sign in/);
  h.dispose();

  ({ h } = await consoleWith(() => Response.json({ active_package_id: "pkg-1", previous_package_id: null, revision: 3 })));
  result = await h.exports.__fetchStatus("water");
  assert.equal(result.status.active_package_id, "pkg-1");
  assert.equal(result.message, "A water package is active.");
  h.dispose();
});

test("actions report an unconfirmed result when a successful reply cannot be read", async () => {
  const source = await readFile("app/water-release-console.tsx", "utf8");
  // send() reads through readAdminBody inside the try whose catch reports the unconfirmed outcome.
  assert.match(source, /const result = await readAdminBody\(response, signal\) as Result;[\s\S]*?\} catch \{\s*setMessage\("The request did not complete, so nothing is confirmed\./);
  const { h } = await consoleWith(() => new Response("not json", { status: 200 }));
  await assert.rejects(h.exports.__readAdminBody(new Response("not json", { status: 200 }), new AbortController().signal));
  // The body object comes from the harness realm, so compare its serialized value.
  assert.equal(JSON.stringify(await h.exports.__readAdminBody(new Response("not json", { status: 409 }), new AbortController().signal)), "{}");
  h.dispose();
});
