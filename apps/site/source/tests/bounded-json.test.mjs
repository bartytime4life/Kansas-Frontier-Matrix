import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = ts.transpileModule(await readFile(new URL("../app/bounded-json.ts", import.meta.url), "utf8"), {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
}).outputText;
const { JsonLimitError, readBoundedBytes } = await import(`data:text/javascript;base64,${Buffer.from(source).toString("base64")}`);

// A chunked body: no Content-Length header, so only the streamed byte count can enforce the limit.
function chunked(chunks) {
  let pulled = 0, cancelled = false;
  const body = new ReadableStream({
    pull(controller) { if (pulled < chunks.length) controller.enqueue(new Uint8Array(chunks[pulled++])); else controller.close(); },
    cancel() { cancelled = true; },
  });
  return { response: new Response(body), pulled: () => pulled, cancelled: () => cancelled };
}

test("binary reads return exact bytes across chunks within the limit", async () => {
  const { response } = chunked([[1, 2, 3], [4], [5, 6]]);
  assert.deepEqual([...await readBoundedBytes(response, 6)], [1, 2, 3, 4, 5, 6]);
  assert.equal((await readBoundedBytes(new Response(null), 6)).byteLength, 0);
});

test("a chunked body without Content-Length stops at the limit instead of buffering the rest", async () => {
  const stream = chunked([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]);
  await assert.rejects(readBoundedBytes(stream.response, 5), JsonLimitError);
  assert.ok(stream.pulled() < 4, "the body is not read to its end");
  assert.ok(stream.cancelled(), "the upstream body is cancelled");
});

test("a declared oversize body is refused before it is read", async () => {
  const stream = chunked([[1, 2, 3]]);
  const response = new Response(stream.response.body, { headers: { "Content-Length": "999" } });
  await assert.rejects(readBoundedBytes(response, 5), JsonLimitError);
  assert.equal(stream.pulled(), 0);
});
