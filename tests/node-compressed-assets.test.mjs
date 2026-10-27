import assert from "node:assert/strict";
import { test } from "node:test";
import { mkdtemp, writeFile, mkdir, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { createServer } from "node:http";
import { gzipSync, gunzipSync, brotliCompressSync } from "node:zlib";
import { createHash } from "node:crypto";
const runtime = new URL(import.meta.resolve("vinext/server/prod-server"));
const { StaticFileCache } = await import(new URL("./static-file-cache.js", runtime));
const { tryServeStatic } = await import(runtime);

async function serverFor(t, files) {
  const dir = await mkdtemp(join(tmpdir(), "kfm-compressed-asset-test-"));
  for (const [name, bytes] of Object.entries(files)) {
    await mkdir(join(dir, name, ".."), { recursive: true });
    await writeFile(join(dir, name), bytes);
  }
  const cache = await StaticFileCache.create(dir);
  const server = createServer(async (req, res) => {
    const pathname = new URL(req.url, "http://localhost").pathname;
    if (!(await tryServeStatic(req, res, dir, pathname, true, cache))) {
      res.writeHead(404); res.end("Not Found");
    }
  });
  await new Promise(resolve => server.listen(0, "127.0.0.1", resolve));
  t.after(async () => {
    await new Promise(resolve => server.close(resolve));
    await rm(dir, { recursive: true, force: true });
  });
  return { cache, origin: `http://127.0.0.1:${server.address().port}` };
}

test("standalone gzip datasets return the original hashed bytes, without transport decoding", async t => {
  const bytes = gzipSync(JSON.stringify([{ fixture: "synthetic", value: 12.5, unit: "ft" }]));
  const { cache, origin } = await serverFor(t, { "data/fixture.json.gz": bytes });
  assert.ok(cache.lookup("/data/fixture.json.gz"));
  const response = await fetch(`${origin}/data/fixture.json.gz`, { headers: { "Accept-Encoding": "gzip, br" } });
  assert.equal(response.status, 200);
  assert.equal(response.headers.get("content-type"), "application/gzip");
  assert.equal(response.headers.get("content-encoding"), null);
  const served = Buffer.from(await response.arrayBuffer());
  assert.deepEqual(served, bytes);
  assert.equal(createHash("sha256").update(served).digest("hex"), createHash("sha256").update(bytes).digest("hex"));
  assert.deepEqual(JSON.parse(gunzipSync(served)), [{ fixture: "synthetic", value: 12.5, unit: "ft" }]);
});

test("real transport variants keep negotiation and do not acquire a separate public URL", async t => {
  const script = "window.fixture = 7;", compressed = gzipSync(script);
  const { cache, origin } = await serverFor(t, { "assets/example.js": script, "assets/example.js.gz": compressed });
  assert.equal(cache.lookup("/assets/example.js.gz"), undefined);
  assert.deepEqual(await (await fetch(`${origin}/assets/example.js`, { headers: { "Accept-Encoding": "gzip" } })).text(), script);
  const response = await fetch(`${origin}/assets/example.js`, { headers: { "Accept-Encoding": "gzip" } });
  assert.equal(response.headers.get("content-encoding"), "gzip");
  assert.equal((await fetch(`${origin}/assets/example.js.gz`)).status, 404);
});

test("built JS and CSS negotiate Brotli ahead of gzip with exact decoded content and Vary", async t => {
  const script = 'export const fixture="Kansas";\n'.repeat(200), css = '.atlas{color:#123456}\n'.repeat(200);
  const files = {};
  for (const [name, value] of Object.entries({ "assets/example.js": script, "assets/example.css": css })) {
    files[name] = value; files[name + ".gz"] = gzipSync(value); files[name + ".br"] = brotliCompressSync(value);
  }
  const { origin } = await serverFor(t, files);
  for (const [name, value] of [["example.js", script], ["example.css", css]]) {
    const response = await fetch(`${origin}/assets/${name}`, { headers: { "Accept-Encoding": "br, gzip" } });
    assert.equal(response.headers.get("content-encoding"), "br");
    assert.match(response.headers.get("vary"), /Accept-Encoding/i);
    assert.equal(await response.text(), value);
    const head = await fetch(`${origin}/assets/${name}`, { method: "HEAD", headers: { "Accept-Encoding": "gzip" } });
    assert.equal(head.headers.get("content-encoding"), "gzip"); assert.equal(await head.text(), "");
    assert.equal((await fetch(`${origin}/assets/${name}.br`)).status, 404);
    const plain = await fetch(`${origin}/assets/${name}`, { headers: { "Accept-Encoding": "identity" } });
    assert.equal(plain.headers.get("content-encoding"), null); assert.equal(await plain.text(), value);
  }
});

test("gzip HEAD and conditional reads work; an absent uncompressed sibling stays absent", async t => {
  const { origin } = await serverFor(t, {
    "data/fixture.json.gz": gzipSync("[]"),
    ".vite/private.json.gz": gzipSync('{"fixture":"synthetic private metadata"}')
  });
  const head = await fetch(`${origin}/data/fixture.json.gz`, { method: "HEAD" });
  assert.equal(head.status, 200); assert.equal(await head.text(), "");
  const conditional = await fetch(`${origin}/data/fixture.json.gz`, { headers: { "If-None-Match": head.headers.get("etag") } });
  assert.equal(conditional.status, 304);
  assert.equal((await fetch(`${origin}/data/fixture.json`)).status, 404);
  assert.equal((await fetch(`${origin}/.vite/private.json.gz`)).status, 404);
  assert.equal((await fetch(`${origin}/%2evite/private.json.gz`)).status, 404);
  assert.equal((await fetch(`${origin}/data/%2e%2e%2f.vite/private.json.gz`)).status, 404);
  assert.equal((await fetch(`${origin}/data/%2e%2e%2fprivate.json.gz`)).status, 404);
});
