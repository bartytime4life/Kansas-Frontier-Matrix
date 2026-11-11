import assert from 'node:assert/strict';
import test from 'node:test';
import {normalizeReactFlightPreloadHints} from '../server/rsc-stream-hints.mjs';

const bytes = text => new TextEncoder().encode(text);
const hint = ':HL["/theme.css","stylesheet",{"title":"stylesheet"}]\n';
const fixedHint = hint.replace(',"stylesheet",', ',"style",');
const concat = parts => Buffer.concat(parts);
async function normalize(chunks) {
  const source = new ReadableStream({start(controller) {
    for (const chunk of chunks) controller.enqueue(chunk);
    controller.close();
  }});
  return Buffer.from(await new Response(normalizeReactFlightPreloadHints(source)).arrayBuffer());
}

for (const tag of 'TAOoUSsLlGgMmV') {
  test(`Flight ${tag} payload stays byte-exact at every two-chunk split`, async () => {
    const payload = concat([Uint8Array.of(255, 128, 0, 10), bytes(hint), bytes('🦕\n')]);
    const row = concat([bytes(`a:${tag}${payload.length.toString(16)},`), payload]);
    const empty = bytes(`b:${tag}0,`);
    const wire = concat([bytes(hint), row, empty, bytes(hint)]);
    const expected = concat([bytes(fixedHint), row, empty, bytes(fixedHint)]);
    for (let split = 0; split <= wire.length; split++) {
      assert.deepEqual(await normalize([wire.subarray(0, split), new Uint8Array(), wire.subarray(split)]), expected, `split ${split}`);
    }
    assert.deepEqual(await normalize(Array.from(wire, byte => Uint8Array.of(byte))), expected, 'one byte per chunk');
  });
}

test('only valid preload rows with stylesheet as the second item change', async () => {
  const unchanged = [
    '0:{"label":":HL[\\"/x.css\\",\\"stylesheet\\"]","unicode":"🦕"}\n',
    ':HD["/x.css","stylesheet"]\n', ':HL["/x.woff","font"]\n',
    ':HL["stylesheet","image",{"title":"stylesheet"}]\n',
    ':HL["/x.css",{"as":"stylesheet"}]\n', ':HL["/x.css","stylesheet",invalid]\n',
    ':HL["/x.css","stylesheet"]trailing\n',
  ].join('');
  const escaped = 'abc:HL["/with\\\"quote\\\\slash-🦕.css", "stylesheet",{"title":"stylesheet"}]\n';
  const wire = bytes(unchanged + escaped + hint);
  assert.deepEqual(await normalize(Array.from(wire, byte => Uint8Array.of(byte))),
    Buffer.from(unchanged + escaped.replace(', "stylesheet",', ', "style",') + fixedHint));
});

test('malformed UTF-8 in hints and ordinary model rows passes through unchanged', async () => {
  const wire = concat([bytes(':HL["/'), Uint8Array.of(255), bytes('.css","stylesheet"]\n0:{"v":"'), Uint8Array.of(128), bytes('"}\n')]);
  assert.deepEqual(await normalize([wire]), wire);
});

test('truncated headers, hints and length payloads pass through without repair', async () => {
  for (const text of ['a', 'a:', 'a:o', 'a:o12', ':HL["/x.css","stylesheet"]', 'a:T100,\n' + hint]) {
    assert.deepEqual(await normalize([bytes(text)]), Buffer.from(text));
  }
});

test('unknown or unsafe framing stays opaque instead of interpreting embedded hints', async () => {
  for (const prefix of ['bad!:', 'a:o,', 'a:o1z,', 'a:o20000000000000,', 'a'.repeat(65) + ':']) {
    const wire = bytes(prefix + '\n' + hint);
    assert.deepEqual(await normalize([wire]), Buffer.from(wire));
  }
});

test('oversized hint rows pass through and the next real row still normalizes', async () => {
  const large = ':HL["/' + 'a'.repeat(70 * 1024) + '.css","stylesheet"]\n';
  const wire = bytes(large + hint);
  const chunks = [];
  for (let i = 0; i < wire.length; i += 1024) chunks.push(wire.subarray(i, i + 1024));
  assert.deepEqual(await normalize(chunks), Buffer.from(large + fixedHint));
});

test('binary and ordinary model bytes flow before the rest of a row arrives', {timeout: 3000}, async () => {
  for (const prefix of ['1:o100000,', '0:{']) {
    let source;
    const reader = normalizeReactFlightPreloadHints(new ReadableStream({start(controller) { source = controller; }})).getReader();
    source.enqueue(bytes(prefix));
    const first = await reader.read();
    assert.equal(Buffer.from(first.value).toString(), prefix);
    const next = reader.read();
    source.enqueue(Uint8Array.of(255, 128));
    assert.deepEqual((await next).value, Uint8Array.of(255, 128));
    await reader.cancel();
  }
});

test('upstream errors propagate and downstream cancellation reaches the source', {timeout: 3000}, async () => {
  const failure = new Error('upstream render failed');
  const stream = new ReadableStream({start(controller) { controller.error(failure); }});
  await assert.rejects(new Response(normalizeReactFlightPreloadHints(stream)).arrayBuffer(), error => error === failure);
  const reason = new Error('navigation ended');
  let cancelled;
  const cancellation = new Promise(resolve => { cancelled = resolve; });
  const source = new ReadableStream({cancel(value) { cancelled(value); }});
  await normalizeReactFlightPreloadHints(source).cancel(reason);
  assert.equal(await cancellation, reason);
});
