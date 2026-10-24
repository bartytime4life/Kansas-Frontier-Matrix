import { NextResponse } from "next/server";
import { fetchJson, UpstreamError } from "./aviation-weather-server";
import { TRAFFIC_PROVIDERS, parseTraffic } from "./aviation-traffic";

const HEADERS = { "X-Content-Type-Options": "nosniff" } as const;

/**
 * Live positions from the first public receiver network that answers, in a
 * fixed order. The response names the provider that supplied it, so the map
 * can carry that network's attribution and terms.
 */
export async function trafficResponse(): Promise<NextResponse> {
  let last: unknown = null;
  for (const provider of TRAFFIC_PROVIDERS) {
    try {
      const parsed = parseTraffic(await fetchJson(provider.url, 6 * 1024 * 1024, 10_000));
      return NextResponse.json({ retrievedAt: new Date().toISOString(), provider, evidenceRole: "EXTERNAL_CONTEXT_ONLY", records: parsed.records, dropped: parsed.dropped,
        limitation: "Positions reported by volunteer ADS-B/Mode S receivers within 60 seconds. Coverage depends on receivers: low-altitude and some aircraft are missing, and an empty area is not evidence of no traffic." },
      // Providers allow about one request per second per client; a 15-second shared cache keeps every viewer far below that.
      { status: 200, headers: { ...HEADERS, "Cache-Control": "public, max-age=15, stale-while-revalidate=15" } });
    } catch (error) {
      last = error;
    }
  }
  const timeout = last instanceof UpstreamError && last.timeout;
  return NextResponse.json({ state: "error", code: `AVIATION_TRAFFIC_${timeout ? "TIMEOUT" : "UNAVAILABLE"}`, evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    message: "Live aircraft positions are unavailable from every listed public receiver network. No cached or synthetic positions were substituted." },
  { status: timeout ? 504 : 502, headers: { ...HEADERS, "Cache-Control": "no-store" } });
}
