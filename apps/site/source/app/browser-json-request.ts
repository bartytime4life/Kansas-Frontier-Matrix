import { readBoundedJson } from "./bounded-json";

/** Bound the complete request, including a stalled body; callers still validate their contract. */
export async function browserJsonRequest(
  url: string,
  options: RequestInit & { signal: AbortSignal; maxBytes: number; timeoutMs?: number },
): Promise<{ response: Response; body: unknown }> {
  const { signal: caller, maxBytes, timeoutMs = 15_000, ...init } = options;
  const deadline = new AbortController();
  const signal = AbortSignal.any([caller, deadline.signal]);
  const timer = setTimeout(() => deadline.abort(new DOMException("Request timed out", "TimeoutError")), timeoutMs);
  try {
    signal.throwIfAborted();
    const response = await fetch(url, { ...init, signal, cache: "no-store", credentials: "same-origin" });
    const body = await readBoundedJson(response, maxBytes, signal);
    signal.throwIfAborted();
    return { response, body };
  } finally {
    clearTimeout(timer);
  }
}
