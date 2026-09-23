import { afterEach, describe, expect, it, vi } from "vitest";
import {
  createLocalEvidenceSession,
  fetchLocalEvidenceProjection,
  localEvidenceSelection,
  type LocalEvidenceScenario,
} from "../src/adapters/local-http-evidence";
import { resolveMapFeatureEvidence } from "../src/features/map_runtime";
import { mapRuntimeSelectionToEvidenceRequest } from "../src/adapters/map_runtime_evidence_adapter";

const selected = (scenario: LocalEvidenceScenario = "current") => localEvidenceSelection("layer:kansas-frame", scenario)!;
const fixture = (scenario: LocalEvidenceScenario = "current") => {
  const ref = "kfm:evidence:site-local:kansas-frame";
  const outcome = scenario === "current" ? "ANSWER" : scenario === "denied" ? "DENY" : scenario === "error" ? "ERROR" : "ABSTAIN";
  return {
    profile: "kfm.explorer.evidence-drawer.public-safe.v1",
    id: `kfm:ui:evidence-drawer:local-http:kansas-frame:${scenario}`,
    outcome,
    reason_code: { current: "SUPPORTED", stale: "STALE_EVIDENCE", withdrawn: "WITHDRAWN_EVIDENCE", missing: "MISSING_EVIDENCE", denied: "POLICY_DENIED", error: "UPSTREAM_ERROR" }[scenario],
    title: "Synthetic local evidence",
    summary: "A synthetic fixture proves only the interface journey.",
    evidence_refs: ["current", "stale"].includes(scenario) ? [ref] : [],
    citations: scenario === "current" ? [{ label: "Synthetic fixture source", href: "https://example.invalid/fixture" }] : [],
    limitations: ["Synthetic only; no actual release or Kansas factual claim."],
    trust_state: {
      source_role: "context", policy: outcome === "ANSWER" ? "ALLOW" : outcome,
      review: scenario === "current" ? "REVIEWED" : "NOT_APPLICABLE",
      release: scenario === "current" ? "RELEASED" : scenario === "withdrawn" ? "WITHDRAWN" : "UNRELEASED",
      freshness: scenario === "current" ? "CURRENT" : scenario === "stale" ? "STALE" : "UNKNOWN",
      correction: "NONE",
    },
    history: {
      negative_outcomes: scenario === "withdrawn" ? [{ evidence_ref: ref, state: "WITHDRAWN", reason_code: "WITHDRAWN_EVIDENCE", recorded_at: "2026-09-01T00:00:00Z", visible_in_runtime: true, resolvable_as_current: false }] : [],
      corrections: [],
    },
  };
};
const response = (value: unknown = fixture(), status = 200) => new Response(JSON.stringify(value), {
  status, headers: { "Content-Type": "application/json; charset=utf-8", "X-KFM-Local-Fixture": "synthetic-only" },
});

afterEach(() => {
  vi.unstubAllGlobals();
  vi.useRealTimers();
});

describe("opt-in local HTTP evidence transport", () => {
  it("sends only the fixed same-origin synthetic selection, without credentials or redirects", async () => {
    const fetch = vi.fn().mockResolvedValue(response());
    vi.stubGlobal("fetch", fetch);
    const value = await fetchLocalEvidenceProjection(selected(), new AbortController().signal);
    expect(value).toEqual(fixture());
    const [url, options] = fetch.mock.calls[0];
    expect(url).toBe("/__local__/evidence");
    expect(options).toMatchObject({ method: "POST", mode: "same-origin", credentials: "omit", redirect: "error", cache: "no-store", referrerPolicy: "no-referrer" });
    expect(JSON.parse(options.body)).toEqual(mapRuntimeSelectionToEvidenceRequest(selected()));
  });

  it.each(["current", "stale", "withdrawn", "missing", "denied", "error"] as const)("keeps %s finite through the existing selected-evidence bridge", async (scenario) => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue(response(fixture(scenario), scenario === "error" ? 503 : 200)));
    const result = await resolveMapFeatureEvidence(
      mapRuntimeSelectionToEvidenceRequest(selected(scenario)),
      (selection) => fetchLocalEvidenceProjection(selection, new AbortController().signal),
    );
    expect(result.drawer.outcome).toBe(fixture(scenario).outcome);
    expect(result.code).toBe(fixture(scenario).reason_code);
    if (scenario !== "current") expect(result.drawer.citations).toEqual([]);
    if (scenario === "withdrawn") expect(result.drawer.historyLabels.join(" ")).toContain("Withdrawn evidence");
  });

  it("rejects arbitrary request scope and already cancelled requests without networking", async () => {
    const fetch = vi.fn();
    vi.stubGlobal("fetch", fetch);
    expect(localEvidenceSelection("layer:protected-context", "current")).toBeNull();
    await expect(fetchLocalEvidenceProjection({ ...selected(), evidenceRefs: ["private:do-not-send"] }, new AbortController().signal)).rejects.toThrow();
    const controller = new AbortController();
    controller.abort();
    await expect(fetchLocalEvidenceProjection(selected(), controller.signal)).rejects.toThrow();
    expect(fetch).not.toHaveBeenCalled();
  });

  it.each([
    ["HTML", () => new Response("secret", { headers: { "Content-Type": "text/html", "X-KFM-Local-Fixture": "synthetic-only" } })],
    ["extra field", () => response({ ...fixture(), protected_detail: "secret" })],
    ["wrong selection identity", () => response({ ...fixture(), id: "kfm:ui:evidence-drawer:local-http:county-locators:current" })],
    ["oversized declared body", () => new Response("{}", { headers: { "Content-Type": "application/json", "Content-Length": "16385", "X-KFM-Local-Fixture": "synthetic-only" } })],
    ["oversized streamed body", () => new Response("x".repeat(16385), { headers: { "Content-Type": "application/json", "X-KFM-Local-Fixture": "synthetic-only" } })],
    ["wrong content length", () => new Response(JSON.stringify(fixture()), { headers: { "Content-Type": "application/json", "Content-Length": "1", "X-KFM-Local-Fixture": "synthetic-only" } })],
    ["positive error status", () => response(fixture(), 503)],
    ["redirect", () => Response.redirect("https://example.invalid/secret")],
    ["invalid UTF-8", () => new Response(new Uint8Array([0xff]), { headers: { "Content-Type": "application/json", "X-KFM-Local-Fixture": "synthetic-only" } })],
    ["missing synthetic marker", () => { const result = response(); result.headers.delete("X-KFM-Local-Fixture"); return result; }],
    ["wrong synthetic marker", () => { const result = response(); result.headers.set("X-KFM-Local-Fixture", "production"); return result; }],
    ["duplicate top-level key", () => new Response(JSON.stringify(fixture()).replace('"outcome":"ANSWER"', '"outcome":"DENY","outcome":"ANSWER"'), { headers: { "Content-Type": "application/json", "X-KFM-Local-Fixture": "synthetic-only" } })],
    ["duplicate nested key", () => new Response(JSON.stringify(fixture()).replace('"policy":"ALLOW"', '"policy":"DENY","policy":"ALLOW"'), { headers: { "Content-Type": "application/json", "X-KFM-Local-Fixture": "synthetic-only" } })],
  ])("fails closed on %s without displaying partial server content", async (_label, makeResponse) => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue((makeResponse as () => Response)()));
    const result = await resolveMapFeatureEvidence(
      mapRuntimeSelectionToEvidenceRequest(selected()),
      (selection) => fetchLocalEvidenceProjection(selection, new AbortController().signal),
    );
    expect(result.drawer.outcome).toBe("ERROR");
    expect(result.drawer.evidenceRefs).toEqual([]);
    expect(result.drawer.citations).toEqual([]);
    expect(JSON.stringify(result.drawer)).not.toContain("secret");
  });

  it("applies a total deadline even when fetch ignores abort", async () => {
    vi.useFakeTimers();
    vi.stubGlobal("fetch", vi.fn(() => new Promise(() => undefined)));
    const result = expect(fetchLocalEvidenceProjection(selected(), new AbortController().signal)).rejects.toThrow("stopped");
    await vi.advanceTimersByTimeAsync(5_001);
    await result;
  });

  it("applies the same deadline to a stalled body and does not await cancellation", async () => {
    vi.useFakeTimers();
    const body = new ReadableStream<Uint8Array>({ cancel: () => new Promise(() => undefined) });
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue(new Response(body, { headers: { "Content-Type": "application/json", "X-KFM-Local-Fixture": "synthetic-only" } })));
    const result = expect(fetchLocalEvidenceProjection(selected(), new AbortController().signal)).rejects.toThrow("stopped");
    await vi.advanceTimersByTimeAsync(5_001);
    await result;
  });

  it("cancels promptly while a transport ignores abort", async () => {
    const controller = new AbortController();
    vi.stubGlobal("fetch", vi.fn(() => new Promise(() => undefined)));
    const result = expect(fetchLocalEvidenceProjection(selected(), controller.signal)).rejects.toThrow("stopped");
    controller.abort();
    await result;
  });
});

describe("local evidence context cancellation", () => {
  it("keeps a late answer from replacing a newer withdrawal, even if resolver ignores abort", async () => {
    let completeFirst: (value: unknown) => void = () => undefined;
    const signals: AbortSignal[] = [];
    const consume = vi.fn();
    const session = createLocalEvidenceSession((_selection, signal) => {
      signals.push(signal);
      return signals.length === 1 ? new Promise((resolve) => { completeFirst = resolve; }) : Promise.resolve(fixture("withdrawn"));
    }, consume);
    const first = session.select(selected());
    await session.select(selected("withdrawn"));
    expect(signals[0].aborted).toBe(true);
    completeFirst(fixture());
    await first;
    expect(consume).toHaveBeenCalledTimes(1);
    expect(consume.mock.calls[0][0].drawer.code).toBe("WITHDRAWN_EVIDENCE");
  });

  it.each(["invalidate", "destroy"] as const)("suppresses pending evidence after %s and aborts its transport", async (action) => {
    let complete: (value: unknown) => void = () => undefined;
    let signal: AbortSignal | undefined;
    const consume = vi.fn();
    const session = createLocalEvidenceSession((_selection, currentSignal) => {
      signal = currentSignal;
      return new Promise((resolve) => { complete = resolve; });
    }, consume);
    const pending = session.select(selected());
    session[action]();
    expect(signal?.aborted).toBe(true);
    complete(fixture());
    await pending;
    expect(consume).not.toHaveBeenCalled();
  });
});
