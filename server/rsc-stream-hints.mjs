// Flight 19.2.9 length-framed rows: text, ArrayBuffer and typed-array views.
// Payloads have no newline delimiter and may contain arbitrary bytes or rows.
const LENGTH_TAGS = new Set('TAOoUSsLlGgMmV');
const MAX_HEADER_BYTES = 64;
const MAX_HINT_BYTES = 64 * 1024;
const encoder = new TextEncoder();
const decoder = new TextDecoder('utf-8', {fatal: true});

function hex(byte) {
  if (byte >= 48 && byte <= 57) return byte - 48;
  if (byte >= 97 && byte <= 102) return byte - 87;
  return -1;
}

function join(parts, length) {
  const bytes = new Uint8Array(length);
  let offset = 0;
  for (const part of parts) { bytes.set(part, offset); offset += part.length; }
  return bytes;
}

function normalizeHint(bytes) {
  try {
    const line = decoder.decode(bytes);
    const colon = line.indexOf(':');
    if (line.slice(colon + 1, colon + 4) !== 'HL[') return bytes;
    const payload = JSON.parse(line.slice(colon + 3, -1));
    if (!Array.isArray(payload) || typeof payload[0] !== 'string' || payload[1] !== 'stylesheet') return bytes;
    // Only the second array item changes. Escaped URLs, options and other text
    // retain their original representation; never replace inside a JSON string.
    return encoder.encode(line.replace(
      /^([0-9a-f]*:HL\[\s*"(?:[^"\\]|\\.)*"\s*,\s*)"stylesheet"(?=\s*[,\]])/,
      '$1"style"',
    ));
  } catch {
    // Invalid UTF-8 or JSON belongs to the downstream codec, unchanged.
    return bytes;
  }
}

/** Normalize CSS preload hints without decoding or buffering binary/model rows. */
export function normalizeReactFlightPreloadHints(stream) {
  let state = 'id', header = [], length = 0, lengthDigits = 0;
  let hintParts = [], hintBytes = 0;

  return stream.pipeThrough(new TransformStream({
    transform(chunk, controller) {
      let offset = 0;
      const emitHeader = () => { controller.enqueue(Uint8Array.from(header)); header = []; };
      const emitHint = () => {
        for (const part of hintParts) controller.enqueue(part);
        hintParts = []; hintBytes = 0;
      };
      while (offset < chunk.length) {
        if (state === 'opaque') { controller.enqueue(chunk.subarray(offset)); return; }
        if (state === 'binary') {
          const end = offset + Math.min(length, chunk.length - offset);
          controller.enqueue(chunk.subarray(offset, end));
          length -= end - offset; offset = end;
          if (length === 0) state = 'id';
          continue;
        }
        if (state === 'line' || state === 'hint') {
          const newline = chunk.indexOf(10, offset);
          const end = newline === -1 ? chunk.length : newline + 1;
          const part = chunk.subarray(offset, end);
          if (state === 'line') controller.enqueue(part);
          else {
            hintParts.push(part); hintBytes += part.length;
            if (hintBytes > MAX_HINT_BYTES) { emitHint(); state = 'line'; }
            else if (newline !== -1) {
              controller.enqueue(normalizeHint(join(hintParts, hintBytes)));
              hintParts = []; hintBytes = 0;
            }
          }
          offset = end;
          if (newline !== -1) state = 'id';
          continue;
        }

        const byte = chunk[offset++];
        header.push(byte);
        if (header.length > MAX_HEADER_BYTES) { emitHeader(); state = 'opaque'; continue; }
        if (state === 'id') {
          if (byte === 58) state = 'tag';
          else if (hex(byte) === -1) { emitHeader(); state = 'opaque'; }
        } else if (state === 'tag') {
          if (LENGTH_TAGS.has(String.fromCharCode(byte))) { length = 0; lengthDigits = 0; state = 'length'; }
          else if (byte === 72) {
            hintParts = [Uint8Array.from(header)]; hintBytes = header.length; header = []; state = 'hint';
          } else { emitHeader(); state = byte === 10 ? 'id' : 'line'; }
        } else if (state === 'length') {
          if (byte === 44) { emitHeader(); state = lengthDigits === 0 ? 'opaque' : length === 0 ? 'id' : 'binary'; }
          else {
            const digit = hex(byte);
            lengthDigits++;
            length = length * 16 + digit;
            // An unknown/malformed framing cannot be safely resynchronized.
            // Forward the remainder verbatim rather than guessing row boundaries.
            if (digit === -1 || !Number.isSafeInteger(length)) { emitHeader(); state = 'opaque'; }
          }
        }
      }
    },
    flush(controller) {
      if (header.length) controller.enqueue(Uint8Array.from(header));
      for (const part of hintParts) controller.enqueue(part);
    },
  }));
}

export function createRscRenderer(render) {
  return (model, options) => normalizeReactFlightPreloadHints(render(model, options));
}
