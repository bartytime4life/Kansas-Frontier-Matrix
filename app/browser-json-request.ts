import { readBoundedJson } from "./bounded-json";

type PublicReadRecovery = "census" | "river-network";
const recoveryPaths: Record<PublicReadRecovery, string> = {
  census: "/api/live-context?feed=census-counties",
  "river-network": "/api/hydrology/streamflow?mode=network&range=24h&encoding=columns-v1",
};
const transientStatuses = new Set([408, 500, 502, 503, 504]);

function retryAfter(response: Response): number | null {
  const value = response.headers.get("Retry-After")?.trim();
  if (!value) return null;
  const milliseconds = /^\d+$/.test(value) ? Number(value) * 1000 : Date.parse(value) - Date.now();
  return Number.isFinite(milliseconds) ? Math.max(0, milliseconds) : null;
}

function waitForRetry(milliseconds: number, signal: AbortSignal): Promise<void> {
  signal.throwIfAborted();
  return new Promise((resolve, reject) => {
    const abort = () => { clearTimeout(timer); signal.removeEventListener("abort", abort); reject(signal.reason); };
    const timer = setTimeout(() => { signal.removeEventListener("abort", abort); resolve(); }, milliseconds);
    signal.addEventListener("abort", abort, { once: true });
  });
}

/** Bound the complete request, including a stalled body; callers still validate their contract. */
export async function browserJsonRequest(
  url: string,
  options: RequestInit & { signal: AbortSignal; maxBytes: number; timeoutMs?: number; recovery?: PublicReadRecovery },
): Promise<{ response: Response; body: unknown }> {
  const { signal: caller, maxBytes, timeoutMs = 15_000, recovery, ...init } = options;
  // Explicitly opt in only these two public GETs. Private, archive and write
  // workflows retain their single-request behavior, even if misconfigured.
  if (recovery && (url !== recoveryPaths[recovery] || (init.method ?? "GET") !== "GET" || init.body != null)) {
    throw new Error("Recovery is limited to the selected public source GET.");
  }
  const budget = recovery === "river-network" ? 150_000 : recovery === "census" ? 65_000 : timeoutMs;
  const expires = Date.now() + budget;
  const deadline = new AbortController();
  const signal = AbortSignal.any([caller, deadline.signal]);
  const timer = setTimeout(() => deadline.abort(new DOMException("Request timed out", "TimeoutError")), budget);
  let failures = 0, busyResponses = 0;
  try {
    for (;;) {
      signal.throwIfAborted();
      const attempt = new AbortController();
      const attemptSignal = AbortSignal.any([signal, attempt.signal]);
      const attemptTimer = setTimeout(() => attempt.abort(new DOMException("Request timed out", "TimeoutError")), timeoutMs);
      let result: { response: Response; body: unknown } | undefined;
      let response: Response | undefined;
      let failure: unknown;
      try {
        response = await fetch(url, { ...init, signal: attemptSignal, cache: "no-store", credentials: "same-origin" });
        const body = await readBoundedJson(response, maxBytes, attemptSignal);
        attemptSignal.throwIfAborted();
        result = { response, body };
      } catch (error) {
        signal.throwIfAborted();
        // Successful malformed/oversized responses remain errors. A gateway's
        // non-JSON error page may be retried, but never accepted as source data.
        const temporary = attempt.signal.aborted || (!response && error instanceof TypeError)
          || (response && transientStatuses.has(response.status) && error instanceof SyntaxError);
        if (!recovery || !temporary) throw error;
        failure = error;
      } finally { clearTimeout(attemptTimer); }
      signal.throwIfAborted();
      if (!recovery || result?.response.ok) return result!;
      const code = result?.body && typeof result.body === "object" && "code" in result.body ? result.body.code : undefined;
      const busy = recovery === "river-network" && response?.status === 429 && code === "USGS_STREAMFLOW_NETWORK_BUSY";
      const minimum = response ? retryAfter(response) : null;
      const retryable = busy || (!result && failure !== undefined)
        || (response && transientStatuses.has(response.status) && code !== "USGS_STREAMFLOW_BUDGET_EXCEEDED")
        || (response?.status === 429 && minimum !== null);
      const exhausted = busy ? ++busyResponses > 10 : ++failures >= 3;
      const delay = Math.max(minimum ?? 0, busy ? Math.min(8_000, 2_000 * 2 ** (busyResponses - 1)) : 1_000 * 2 ** (failures - 1));
      // Never shorten a provider cooldown to fit the local recovery budget.
      if (!retryable || exhausted || delay >= expires - Date.now()) {
        if (result) return result;
        throw failure;
      }
      await waitForRetry(delay, signal);
    }
  } finally {
    clearTimeout(timer);
  }
}
