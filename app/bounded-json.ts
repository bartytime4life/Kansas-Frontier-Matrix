/** Read a JSON stream without first buffering an unbounded request or response. */
export class JsonLimitError extends Error {}

/** Preserve exact bytes for integrity checks while bounding the stream before allocation. */
export async function readBoundedBytes(message: Response, maxBytes: number, signal?: AbortSignal): Promise<Uint8Array<ArrayBuffer>> {
  if (signal?.aborted) {
    void message.body?.cancel(signal.reason).catch(() => undefined);
    signal.throwIfAborted();
  }
  const declared = Number(message.headers.get("content-length"));
  if (Number.isFinite(declared) && declared > maxBytes) {
    void message.body?.cancel().catch(() => undefined);
    throw new JsonLimitError("Response byte limit exceeded.");
  }
  if (!message.body) throw new SyntaxError("Missing response body.");
  const reader = message.body.getReader();
  const cancel = () => { void reader.cancel(signal?.reason).catch(() => undefined); };
  signal?.addEventListener("abort", cancel, { once: true });
  const chunks: Uint8Array[] = [];
  let bytes = 0;
  try {
    for (;;) {
      signal?.throwIfAborted();
      const chunk = await reader.read();
      signal?.throwIfAborted();
      if (chunk.done) break;
      bytes += chunk.value.byteLength;
      if (bytes > maxBytes) throw new JsonLimitError("Response byte limit exceeded.");
      chunks.push(chunk.value);
    }
    const result = new Uint8Array(bytes);
    let offset = 0;
    for (const chunk of chunks) { result.set(chunk, offset); offset += chunk.byteLength; }
    return result;
  } catch (error) {
    void reader.cancel().catch(() => undefined);
    throw error;
  } finally {
    signal?.removeEventListener("abort", cancel);
    reader.releaseLock();
  }
}

export async function readBoundedText(message: Request | Response, maxBytes: number, signal?: AbortSignal): Promise<string> {
  if (signal?.aborted) {
    void message.body?.cancel(signal.reason).catch(() => undefined);
    signal.throwIfAborted();
  }
  const declared = Number(message.headers.get("content-length"));
  if (Number.isFinite(declared) && declared > maxBytes) {
    void message.body?.cancel().catch(() => undefined);
    throw new JsonLimitError("JSON byte limit exceeded.");
  }
  if (!message.body) throw new SyntaxError("Missing JSON body.");
  const reader = message.body.getReader();
  const cancel = () => { void reader.cancel(signal?.reason).catch(() => undefined); };
  signal?.addEventListener("abort", cancel, { once: true });
  const decoder = new TextDecoder("utf-8", { fatal: true });
  let bytes = 0;
  let text = "";
  try {
    while (true) {
      signal?.throwIfAborted();
      const chunk = await reader.read();
      signal?.throwIfAborted();
      if (chunk.done) break;
      bytes += chunk.value.byteLength;
      if (bytes > maxBytes) throw new JsonLimitError("JSON byte limit exceeded.");
      text += decoder.decode(chunk.value, { stream: true });
    }
    return text + decoder.decode();
  } catch (error) {
    void reader.cancel().catch(() => undefined);
    throw error;
  } finally {
    signal?.removeEventListener("abort", cancel);
    reader.releaseLock();
  }
}

export async function readBoundedJson(message: Request | Response, maxBytes: number, signal?: AbortSignal): Promise<unknown> {
  return JSON.parse(await readBoundedText(message, maxBytes, signal)) as unknown;
}

/** A released-looking body cannot turn a failed HTTP response into a successful read. */
export async function readSuccessfulJson(response: Response, maxBytes: number, signal?: AbortSignal): Promise<unknown> {
  if (!response.ok) {
    void response.body?.cancel().catch(() => undefined);
    throw new Error("Response request failed.");
  }
  return readBoundedJson(response, maxBytes, signal);
}
