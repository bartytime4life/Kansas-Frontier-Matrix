import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/bounded-json.ts", import.meta.url), "utf8");
const output = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const { readBoundedBytes, JsonLimitError, readBoundedText } = await import(`data:text/javascript;base64,${Buffer.from(output).toString("base64")}`);

test("bounded bytes preserve binary contents at the exact cap and release the reader", async () => {
  const bytes = new Uint8Array([0, 255, 128, 1, 2, 3]);
  const response = new Response(new ReadableStream({ start(controller) { controller.enqueue(bytes.slice(0, 2)); controller.enqueue(bytes.slice(2)); controller.close(); } }));
  assert.deepEqual(await readBoundedBytes(response, bytes.length), bytes);
  assert.equal(response.body.locked, false);
  assert.deepEqual(await readBoundedBytes(new Response(new Uint8Array()), 0), new Uint8Array());
});

test("declared and actual byte caps cancel without awaiting an uncooperative source", { timeout: 1000 }, async () => {
  for (const declared of ["9", undefined, "1"]) {
    let pulls = 0, cancellations = 0;
    const response = new Response(new ReadableStream({
      pull(controller) { pulls++; controller.enqueue(new Uint8Array(3)); },
      cancel() { cancellations++; return new Promise(() => {}); },
    }, { highWaterMark: 0 }), { headers: declared ? { "Content-Length": declared } : {} });
    await assert.rejects(readBoundedBytes(response, 8), JsonLimitError);
    assert.equal(pulls, declared === "9" ? 0 : 3);
    assert.equal(cancellations, 1);
    assert.equal(response.body.locked, false);
  }
});

test("a stalled byte read honors the exact caller abort reason and releases listeners and lock", { timeout: 1000 }, async t => {
  const controller = new AbortController(), reason = new DOMException("Fixture deadline", "TimeoutError");
  let started, cancelReason;
  const reading = new Promise(resolve => { started = resolve; });
  const response = new Response(new ReadableStream({ pull() { started(); }, cancel(value) { cancelReason = value; return new Promise(() => {}); } }, { highWaterMark: 0 }));
  const added = t.mock.method(controller.signal, "addEventListener"), removed = t.mock.method(controller.signal, "removeEventListener");
  const pending = readBoundedBytes(response, 8, controller.signal);
  await reading; controller.abort(reason);
  await assert.rejects(pending, error => error === reason);
  assert.equal(cancelReason, reason); assert.equal(response.body.locked, false);
  assert.equal(added.mock.callCount(), 1); assert.equal(removed.mock.callCount(), 1);
  assert.equal(removed.mock.calls[0].arguments[1], added.mock.calls[0].arguments[1]);
});

test("pre-aborted and broken byte responses are canceled or released without consuming more", async () => {
  const controller = new AbortController(), reason = new DOMException("Download closed", "AbortError");
  controller.abort(reason);
  let pulls = 0, canceled;
  const aborted = new Response(new ReadableStream({ pull() { pulls++; }, cancel(value) { canceled = value; } }, { highWaterMark: 0 }));
  await assert.rejects(readBoundedBytes(aborted, 8, controller.signal), error => error === reason);
  assert.equal(pulls, 0); assert.equal(canceled, reason); assert.equal(aborted.body.locked, false);
  const failure = new Error("Fixture stream failure");
  const broken = new Response(new ReadableStream({ pull(stream) { stream.error(failure); } }, { highWaterMark: 0 }));
  await assert.rejects(readBoundedBytes(broken, 8), error => error === failure);
  assert.equal(broken.body.locked, false);
  await assert.rejects(readBoundedBytes(new Response(null), 8), SyntaxError);
});

test("existing text reads still decode split UTF-8 and reject malformed text", async () => {
  const bytes = new TextEncoder().encode("A🌾é");
  const response = new Response(new ReadableStream({ start(controller) { for (const byte of bytes) controller.enqueue(new Uint8Array([byte])); controller.close(); } }));
  assert.equal(await readBoundedText(response, bytes.length), "A🌾é");
  await assert.rejects(readBoundedText(new Response(new Uint8Array([0xc3])), 1), TypeError);
});
