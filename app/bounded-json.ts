/** Read a JSON stream without first buffering an unbounded request or response. */
export class JsonLimitError extends Error {}

export async function readBoundedJson(message: Request | Response, maxBytes: number): Promise<unknown> {
  const declared = Number(message.headers.get("content-length"));
  if (Number.isFinite(declared) && declared > maxBytes) {
    void message.body?.cancel().catch(() => undefined);
    throw new JsonLimitError("JSON byte limit exceeded.");
  }
  if (!message.body) throw new SyntaxError("Missing JSON body.");
  const reader = message.body.getReader();
  const decoder = new TextDecoder("utf-8", { fatal: true });
  let bytes = 0;
  let text = "";
  try {
    while (true) {
      const chunk = await reader.read();
      if (chunk.done) break;
      bytes += chunk.value.byteLength;
      if (bytes > maxBytes) throw new JsonLimitError("JSON byte limit exceeded.");
      text += decoder.decode(chunk.value, { stream: true });
    }
    return JSON.parse(text + decoder.decode()) as unknown;
  } catch (error) {
    void reader.cancel().catch(() => undefined);
    throw error;
  } finally {
    reader.releaseLock();
  }
}
