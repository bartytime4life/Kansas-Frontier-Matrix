import { NextResponse } from "next/server";
import { readBoundedText } from "./bounded-json";
import { AWC_API_BASE, AWC_KANSAS_BBOX, AWC_SOURCE_TITLE, AWC_SOURCE_URL, parseMetars, parsePireps } from "./aviation-weather";

const USER_AGENT = "KansasFrontierMatrixExplorer/1.0 (https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site)";
const MAX_BYTES = 2 * 1024 * 1024;
const TIMEOUT_MS = 12_000;

// Fixed upstream URLs: no caller-controlled query reaches the provider.
const PRODUCTS = {
  metar: { url: `${AWC_API_BASE}/metar?bbox=${AWC_KANSAS_BBOX}&format=json&hours=2`, code: "AVIATION_METAR",
    limitation: "Latest ASOS/AWOS observation per station within 90 minutes. Observations describe the station site only, may be missing or amended, and are not forecasts or flight briefings." },
  pirep: { url: `${AWC_API_BASE}/pirep?bbox=${AWC_KANSAS_BBOX}&format=json&age=3`, code: "AVIATION_PIREP",
    limitation: "Voluntary pilot reports from the last 3 hours. Few reports does not mean little traffic or smooth air; locations and altitudes are as reported." },
} as const;

export class UpstreamError extends Error {
  constructor(message: string, readonly timeout = false) { super(message); }
}

/** Fixed-URL JSON read: no redirects, bounded time and bytes. Shared by every aviation route. */
export async function fetchJson(url: string, maxBytes = MAX_BYTES, timeoutMs = TIMEOUT_MS): Promise<unknown> {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  try {
    const response = await fetch(url, { cache: "no-store", redirect: "manual", signal: controller.signal,
      headers: { Accept: "application/json", "User-Agent": USER_AGENT } });
    // AWC answers 204 when nothing matches: that is an empty list, not an error.
    if (response.status === 204) return [];
    if (!response.ok) throw new UpstreamError(`Upstream returned HTTP ${response.status}.`);
    if (!(response.headers.get("content-type") ?? "").toLowerCase().includes("json")) throw new UpstreamError("Unexpected media type.");
    return JSON.parse(await readBoundedText(response, maxBytes, controller.signal)) as unknown;
  } catch (error) {
    if (error instanceof UpstreamError) throw error;
    if (error instanceof Error && error.name === "AbortError") throw new UpstreamError("Request timed out.", true);
    throw new UpstreamError("Request failed.");
  } finally {
    clearTimeout(timer);
  }
}

export async function aviationWeatherResponse(kind: keyof typeof PRODUCTS): Promise<NextResponse> {
  const product = PRODUCTS[kind];
  try {
    const payload = await fetchJson(product.url);
    const now = Date.now();
    const parsed = kind === "metar" ? parseMetars(payload, now) : parsePireps(payload, now);
    return NextResponse.json({ retrievedAt: new Date(now).toISOString(), sourceTitle: AWC_SOURCE_TITLE, sourceUrl: AWC_SOURCE_URL,
      evidenceRole: "EXTERNAL_CONTEXT_ONLY", records: parsed.records, dropped: parsed.dropped, limitation: product.limitation }, {
      status: 200,
      // AWC asks clients not to poll faster than about once a minute; the edge cache absorbs repeat viewers.
      headers: { "Cache-Control": "public, max-age=120, stale-while-revalidate=60", "X-Content-Type-Options": "nosniff" },
    });
  } catch (error) {
    const timeout = error instanceof UpstreamError && error.timeout;
    return NextResponse.json({ state: "error", code: `${product.code}_${timeout ? "TIMEOUT" : "UNAVAILABLE"}`,
      message: "Aviation weather is temporarily unavailable. No cached or synthetic observations were substituted.", evidenceRole: "EXTERNAL_CONTEXT_ONLY" },
    { status: timeout ? 504 : 502, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  }
}
