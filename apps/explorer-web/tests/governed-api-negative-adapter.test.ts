import { afterEach, describe, expect, it, vi } from "vitest";
import { parseEvidenceDrawerProjection } from "../src/adapters/GovernedClient";
import { fetchGovernedApiNegativeProjection } from "../src/adapters/governed_api_negative_adapter";

const encoder = new TextEncoder();
function envelope(changes: Record<string, unknown> = {}): Record<string, unknown> {
  return {
    id: "stub:evidence", spec_hash: `sha256:${"a".repeat(64)}`, version: "v1-stub",
    issued_at: "2026-09-15T18:00:00+00:00", outcome: "ABSTAIN", reason_code: "NOT_IMPLEMENTED",
    evidence_refs: [], policy_state: "baseline", freshness: "current", correction_state: "none",
    ...changes,
  };
}
function response(value: unknown = envelope(), status = 200, headers: Record<string, string> = {}): Response {
  return new Response(JSON.stringify(value), { status, headers: { "Content-Type": "application/json", ...headers } });
}
function install(value: Response): ReturnType<typeof vi.fn> {
  const fetch = vi.fn().mockResolvedValue(value);
  vi.stubGlobal("fetch", fetch);
  return fetch;
}
function safeProjection(value: unknown, outcome: string, reason: string): void {
  expect(parseEvidenceDrawerProjection(value).ok).toBe(true);
  expect(value).toMatchObject({ outcome, reason_code: reason, evidence_refs: [], citations: [], history: { negative_outcomes: [], corrections: [] } });
  expect(value).not.toHaveProperty("precision_actually_used");
  expect(JSON.stringify(value)).not.toContain("secret-canary");
}

afterEach(() => {
  vi.useRealTimers();
  vi.restoreAllMocks();
  vi.unstubAllGlobals();
});

describe("governed API negative transport", () => {
  it("requests only the literal evidence endpoint and reports the actual scaffold limitation", async () => {
    const fetch = install(response());
    const result = await fetchGovernedApiNegativeProjection();
    safeProjection(result, "ABSTAIN", "MISSING_EVIDENCE");
    expect(result.summary).toContain("does not yet resolve selected evidence");
    expect(fetch).toHaveBeenCalledExactlyOnceWith("/evidence", expect.objectContaining({
      method: "GET", mode: "same-origin", credentials: "omit", redirect: "error",
      cache: "no-store", referrerPolicy: "no-referrer", headers: { Accept: "application/json" },
      signal: expect.any(AbortSignal),
    }));
    expect(fetch.mock.calls[0][1]).not.toHaveProperty("body");
    expect(Object.isFrozen(result)).toBe(true);
    expect(Object.isFrozen(result.history)).toBe(true);
  });

  it.each([
    [200, "ABSTAIN", "UNSUPPORTED_SCOPE", "ABSTAIN", "MISSING_EVIDENCE"],
    [200, "ABSTAIN", "MISSING_EVIDENCE", "ABSTAIN", "MISSING_EVIDENCE"],
    [200, "ABSTAIN", "SOURCE_STALE", "ABSTAIN", "STALE_EVIDENCE"],
    [200, "ABSTAIN", "REQUEST_CANCELLED", "ABSTAIN", "MISSING_EVIDENCE"],
    [500, "ABSTAIN", "REQUEST_CANCELLED", "ABSTAIN", "MISSING_EVIDENCE"],
    [200, "DENY", "POLICY_DENIED", "DENY", "POLICY_DENIED"],
    [404, "ERROR", "SAFE_RUNTIME_ERROR", "ERROR", "UPSTREAM_ERROR"],
    [405, "ERROR", "SAFE_RUNTIME_ERROR", "ERROR", "UPSTREAM_ERROR"],
    [500, "ERROR", "SAFE_RUNTIME_ERROR", "ERROR", "UPSTREAM_ERROR"],
    [500, "ERROR", "INVALID_REQUEST", "ERROR", "UPSTREAM_ERROR"],
    [500, "ERROR", "DEPENDENCY_UNAVAILABLE", "ERROR", "UPSTREAM_ERROR"],
    [500, "ERROR", "REQUEST_TIMEOUT", "ERROR", "UPSTREAM_ERROR"],
    [500, "ERROR", "INVALID_RESPONSE", "ERROR", "UPSTREAM_ERROR"],
  ])("projects documented status %s and %s/%s without copying server identifiers or state", async (status, outcome, reason, drawerOutcome, drawerReason) => {
    install(response(envelope({ outcome, reason_code: reason, id: "secret-canary", policy_state: "secret-canary", freshness: "secret-canary", correction_state: "secret-canary" }), Number(status)));
    safeProjection(await fetchGovernedApiNegativeProjection(), String(drawerOutcome), String(drawerReason));
  });

  it.each([
    [200, "ERROR", "SAFE_RUNTIME_ERROR"],
    [404, "ABSTAIN", "NOT_IMPLEMENTED"],
    [405, "DENY", "POLICY_DENIED"],
    [500, "ABSTAIN", "SOURCE_STALE"],
    [404, "ERROR", "REQUEST_TIMEOUT"],
    [500, "DENY", "POLICY_DENIED"],
    [200, "ABSTAIN", "POLICY_DENIED"],
    [200, "DENY", "NOT_IMPLEMENTED"],
    [200, "ABSTAIN", "secret-canary"],
  ])("fails closed on status/outcome/reason mismatch %s/%s/%s", async (status, outcome, reason) => {
    install(response(envelope({ outcome, reason_code: reason }), Number(status)));
    safeProjection(await fetchGovernedApiNegativeProjection(), "ERROR", "UPSTREAM_ERROR");
  });

  it.each([
    { outcome: "ANSWER", reason_code: "SUPPORTED", precision_actually_used: { secret: "secret-canary" } },
    { evidence_refs: [{ ref: "secret-canary" }] },
    { extra: "secret-canary" },
    { policy_state: { secret: "secret-canary" } },
    { spec_hash: "sha256:wrong" },
    { id: "https://secret-canary.invalid" },
    { version: "x".repeat(65) },
    { freshness: "current uppercase" },
  ])("rejects positive, nonempty, extended and malformed envelope fields %j", async (changes) => {
    install(response(envelope(changes)));
    safeProjection(await fetchGovernedApiNegativeProjection(), "ERROR", "UPSTREAM_ERROR");
  });

  it.each([
    "2026-02-29T00:00:00Z", "2024-02-30T00:00:00Z", "0000-01-01T00:00:00Z",
    "2026-13-01T00:00:00Z", "2026-00-01T00:00:00Z", "2026-01-00T00:00:00Z",
    "2026-01-01T24:00:00Z", "2026-01-01T00:60:00Z", "2026-01-01T00:00:60Z",
    "2026-01-01T00:00:00", "2026-01-01T00:00:00+24:00", "2026-01-01T00:00:00+00:60",
  ])("rejects malformed or normalized calendar timestamp %s", async (issued_at) => {
    install(response(envelope({ issued_at })));
    safeProjection(await fetchGovernedApiNegativeProjection(), "ERROR", "UPSTREAM_ERROR");
  });

  it("accepts bounded fractional seconds and a valid leap date without deriving freshness from the timestamp", async () => {
    install(response(envelope({ issued_at: "2024-02-29T23:59:59.123456-05:30" })));
    const result = await fetchGovernedApiNegativeProjection();
    safeProjection(result, "ABSTAIN", "MISSING_EVIDENCE");
    expect(result.trust_state).toMatchObject({ freshness: "UNKNOWN" });
  });

  it.each([
    (text: string) => text.replace('{"id":', '{"id":"secret-canary","id":'),
    (text: string) => text.replace('{"id":', '{"\\u0069d":"secret-canary","id":'),
    (text: string) => `${text}{"secret":"secret-canary"}`,
    (text: string) => text.replace('"evidence_refs":[]', '"evidence_refs":[[]]'),
    (text: string) => text.replace('"correction_state":"none"', '"correction_state":null'),
    (text: string) => text.replace(',"correction_state":"none"', ''),
  ])("rejects ambiguous, nested, missing or concatenated JSON", async (change) => {
    install(new Response(change(JSON.stringify(envelope())), { headers: { "Content-Type": "application/json" } }));
    safeProjection(await fetchGovernedApiNegativeProjection(), "ERROR", "UPSTREAM_ERROR");
  });

  it.each([201, 204, 301, 401, 403, 429, 503])("rejects unsupported HTTP status %s", async (status) => {
    install(new Response(status === 204 ? null : JSON.stringify(envelope()), { status, headers: { "Content-Type": "application/json" } }));
    safeProjection(await fetchGovernedApiNegativeProjection(), "ERROR", "UPSTREAM_ERROR");
  });

  it.each(["text/html", "application/jsonp", "application/json; charset=iso-8859-1", ""]) ("rejects unsupported media type %s", async (mediaType) => {
    install(response(envelope(), 200, { "Content-Type": mediaType }));
    safeProjection(await fetchGovernedApiNegativeProjection(), "ERROR", "UPSTREAM_ERROR");
  });

  it("rejects redirected, opaque, and unexpected-origin responses", async () => {
    for (const fields of [{ redirected: true }, { type: "opaque" }, { url: "https://secret-canary.invalid/evidence" }]) {
      const value = response();
      for (const [key, data] of Object.entries(fields)) Object.defineProperty(value, key, { value: data });
      install(value);
      safeProjection(await fetchGovernedApiNegativeProjection(), "ERROR", "UPSTREAM_ERROR");
    }
  });

  it("accepts only the exact same-origin response URL", async () => {
    vi.stubGlobal("location", { href: "https://example.invalid/tests/browser/map.html" });
    const value = response();
    Object.defineProperty(value, "url", { value: "https://example.invalid/evidence" });
    install(value);
    safeProjection(await fetchGovernedApiNegativeProjection(), "ABSTAIN", "MISSING_EVIDENCE");
  });

  it("accepts split UTF-8 JSON with truthful Content-Length", async () => {
    const bytes = encoder.encode(JSON.stringify(envelope()));
    const body = new ReadableStream<Uint8Array>({ start(controller) {
      controller.enqueue(bytes.slice(0, 23)); controller.enqueue(bytes.slice(23)); controller.close();
    } });
    install(new Response(body, { headers: { "Content-Type": "application/json; charset=utf-8", "Content-Length": String(bytes.length) } }));
    safeProjection(await fetchGovernedApiNegativeProjection(), "ABSTAIN", "MISSING_EVIDENCE");
  });

  it.each(["1", "0", "16385", "99999999999999999", "-1", "1e3", "1.5", "500"]) ("rejects dishonest or invalid Content-Length %s", async (length) => {
    install(response(envelope(), 200, { "Content-Length": length }));
    safeProjection(await fetchGovernedApiNegativeProjection(), "ERROR", "UPSTREAM_ERROR");
  });

  it("enforces streamed byte bounds when Content-Length lies and stops the reader", async () => {
    const cancel = vi.fn();
    const body = new ReadableStream<Uint8Array>({ start(controller) { controller.enqueue(new Uint8Array(16_385)); }, cancel });
    install(new Response(body, { headers: { "Content-Type": "application/json", "Content-Length": "1" } }));
    safeProjection(await fetchGovernedApiNegativeProjection(), "ERROR", "UPSTREAM_ERROR");
    expect(cancel).toHaveBeenCalledOnce();
  });

  it("rejects missing length oversized streams and invalid UTF-8", async () => {
    for (const body of [new Uint8Array(16_385), new Uint8Array([0xff, 0xfe])]) {
      install(new Response(body, { headers: { "Content-Type": "application/json" } }));
      safeProjection(await fetchGovernedApiNegativeProjection(), "ERROR", "UPSTREAM_ERROR");
    }
  });

  it("bounds zero-byte chunk floods independently of timers", async () => {
    const cancel = vi.fn();
    let pulls = 0;
    const body = new ReadableStream<Uint8Array>({ pull(controller) { pulls += 1; controller.enqueue(new Uint8Array()); }, cancel });
    install(new Response(body, { headers: { "Content-Type": "application/json" } }));
    safeProjection(await fetchGovernedApiNegativeProjection(), "ERROR", "UPSTREAM_ERROR");
    expect(pulls).toBeLessThan(260);
    expect(cancel).toHaveBeenCalledOnce();
  });

  it("bounds stalled fetch even when it ignores abort and never retries", async () => {
    vi.useFakeTimers();
    const fetch = vi.fn((_input: RequestInfo | URL, _init?: RequestInit) => new Promise<Response>(() => undefined));
    vi.stubGlobal("fetch", fetch);
    const pending = fetchGovernedApiNegativeProjection();
    await vi.advanceTimersByTimeAsync(5_000);
    safeProjection(await pending, "ERROR", "UPSTREAM_ERROR");
    expect(fetch).toHaveBeenCalledOnce();
    expect(fetch.mock.calls[0]?.[1]?.signal?.aborted).toBe(true);
    expect(vi.getTimerCount()).toBe(0);
  });

  it("bounds a stalled body and stalled cancel without waiting for either", async () => {
    vi.useFakeTimers();
    const cancel = vi.fn(() => new Promise<void>(() => undefined));
    const body = new ReadableStream<Uint8Array>({ cancel });
    install(new Response(body, { headers: { "Content-Type": "application/json", "Content-Length": "10" } }));
    const pending = fetchGovernedApiNegativeProjection();
    await vi.advanceTimersByTimeAsync(5_000);
    safeProjection(await pending, "ERROR", "UPSTREAM_ERROR");
    expect(cancel).toHaveBeenCalledOnce();
    expect(vi.getTimerCount()).toBe(0);
  });

  it("does not fetch an already-cancelled request", async () => {
    const fetch = install(response());
    const controller = new AbortController(); controller.abort("secret-canary");
    safeProjection(await fetchGovernedApiNegativeProjection({ signal: controller.signal }), "ABSTAIN", "MISSING_EVIDENCE");
    expect(fetch).not.toHaveBeenCalled();
  });

  it("cancels a stalled request independently of transport and removes listeners", async () => {
    const controller = new AbortController();
    const remove = vi.spyOn(controller.signal, "removeEventListener");
    vi.stubGlobal("fetch", vi.fn(() => new Promise<Response>(() => undefined)));
    const pending = fetchGovernedApiNegativeProjection({ signal: controller.signal });
    controller.abort("secret-canary");
    const result = await pending;
    safeProjection(result, "ABSTAIN", "MISSING_EVIDENCE");
    expect(result.summary).toContain("cancelled");
    expect(remove).toHaveBeenCalledWith("abort", expect.any(Function));
  });

  it("does not consume a late response after timeout", async () => {
    vi.useFakeTimers();
    let deliver: (value: Response) => void = () => undefined;
    vi.stubGlobal("fetch", vi.fn(() => new Promise<Response>((resolve) => { deliver = resolve; })));
    const pending = fetchGovernedApiNegativeProjection();
    await vi.advanceTimersByTimeAsync(5_000);
    safeProjection(await pending, "ERROR", "UPSTREAM_ERROR");
    const value = response();
    const reader = vi.spyOn(value.body!, "getReader");
    deliver(value);
    await Promise.resolve(); await Promise.resolve();
    expect(reader).not.toHaveBeenCalled();
  });

  it("does not reflect network errors or fall back to fixture evidence", async () => {
    const fetch = vi.fn().mockRejectedValue(new Error("secret-canary credential or internal location"));
    vi.stubGlobal("fetch", fetch);
    safeProjection(await fetchGovernedApiNegativeProjection(), "ERROR", "UPSTREAM_ERROR");
    expect(fetch).toHaveBeenCalledOnce();
  });
});
