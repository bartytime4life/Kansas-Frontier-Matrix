import { publicFamilyAuthorization } from "./public-release-server";
import { PublicReleaseError } from "./public-release";
import { env } from "cloudflare:workers";
import { getRawDb } from "../db";
import { object, parseWaterJson } from "./governed-water";
import { parseStormEventsPackage, projectStormEvents, stormEventsNegative, STORM_EVENTS_PACKAGE_LIMIT } from "./governed-storm-events";

type Bucket = { get(key: string): Promise<{ size: number; text(): Promise<string> } | null> };
export const STORM_EVENTS_HEADERS = { "Cache-Control": "private, no-store", "X-Content-Type-Options": "nosniff", "Vary": "Cookie" };
// Only the exact tokens 1..12, as governed_api/storm_events.py MONTHS: no leading zeros, signs or spaces.
const MONTHS: Record<string, number> = Object.fromEntries(Array.from({ length: 12 }, (_, i) => [String(i + 1), i + 1]));
export async function governedStormEventsRead(request: Request, view: string) {
  const now = new Date().toISOString(), correlation = crypto.randomUUID(), start = Date.now();
  let result, status = 200;
  try {
    // Hosted audience is enforced by Sites. This route only serves the active approved storm events snapshot.
    const url = new URL(request.url), entries = [...url.searchParams.entries()];
    if (url.search.length > 256 || entries.length > 1 || entries.some(([key, value]) => key !== "month" || !Object.hasOwn(MONTHS, value))) { status = 400; result = await stormEventsNegative("INVALID_QUERY", now); }
    else {
      const active = await getRawDb().prepare("SELECT a.package_id, a.decision_json, p.state FROM storm_events_active a LEFT JOIN storm_events_packages p ON p.package_id = a.package_id WHERE a.singleton = 1").first<{ package_id: string; decision_json: string; state: string }>();
      if (!active || active.state !== "STAGED") result = await stormEventsNegative("NO_APPROVED_SNAPSHOT", now);
      else {
        if (!/^sha256:[a-f0-9]{64}$/.test(active.package_id) || typeof active.decision_json !== "string" || active.decision_json.length > 8192) throw new Error("ACTIVE_METADATA_INVALID");
        const bucket = env.BUCKET as Bucket | undefined;
        if (!bucket) throw new Error("STORAGE_UNAVAILABLE");
        const stored = await bucket.get(`governed-storm-events/v1/objects/${active.package_id.slice(7)}.json`);
        if (!stored || !Number.isInteger(stored.size) || stored.size < 1 || stored.size > STORM_EVENTS_PACKAGE_LIMIT) throw new Error("PACKAGE_UNAVAILABLE");
        const text = await stored.text();
        if (new TextEncoder().encode(text).length !== stored.size) throw new Error("PACKAGE_SIZE_MISMATCH");
        const pkg = await parseStormEventsPackage(text);
        if (pkg.manifest.package_id !== active.package_id) throw new Error("ACTIVE_BINDING_MISMATCH");
        // The gate is evaluated after the storage read, so an approval that lapses meanwhile is refused.
        const month = url.searchParams.get("month");
        await publicFamilyAuthorization("storm-events", active.package_id, text, object(parseWaterJson(active.decision_json)), request);
        result = await projectStormEvents(pkg, object(parseWaterJson(active.decision_json)), view, new Date().toISOString(), month === null ? null : MONTHS[month]);
      }
    }
  } catch (error) { status = error instanceof PublicReleaseError ? 200 : 503; result = await stormEventsNegative(error instanceof PublicReleaseError ? "NO_APPROVED_SNAPSHOT" : "RELEASE_STORE_UNAVAILABLE", now, error instanceof PublicReleaseError ? "ABSTAIN" : "ERROR"); }
  // Never log identity headers, query text, source content, or model inputs.
  console.info(JSON.stringify({ event: "governed_read", component: "site-storm-events", build: "kfm-storm-events-v1", correlation_id: correlation, source_id: "noaa-storm-events", outcome: result.envelope.outcome, reason_code: result.envelope.reason_code, duration_ms: Date.now() - start }));
  return Response.json(result, { status, headers: { ...STORM_EVENTS_HEADERS, "X-KFM-Correlation-ID": correlation } });
}
