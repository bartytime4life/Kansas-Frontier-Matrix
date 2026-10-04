/** Read a JSON stream without first buffering an unbounded request or response. */
export class JsonLimitError extends Error {}

export async function readBoundedText(message: Request | Response, maxBytes: number, signal?: AbortSignal): Promise<string> {
  signal?.throwIfAborted();
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
