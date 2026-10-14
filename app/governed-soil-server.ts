import { env } from "cloudflare:workers";
import { getRawDb } from "../db";
import { object, parseWaterJson } from "./governed-water";
import { parseSoilPackage, projectSoil, soilNegative, SOIL_PACKAGE_LIMIT, SOIL_STATIONS } from "./governed-soil";

type Bucket = { get(key: string): Promise<{ size: number; text(): Promise<string> } | null> };
export const SOIL_HEADERS = { "Cache-Control": "private, no-store", "X-Content-Type-Options": "nosniff", "Vary": "Cookie" };
export async function governedSoilRead(request: Request, view: string) {
  const now = new Date().toISOString(), correlation = crypto.randomUUID(), start = Date.now();
  let result, status = 200;
  try {
    // Hosted audience is enforced by Sites. This route only serves the active approved soil snapshot.
    const url = new URL(request.url), entries = [...url.searchParams.entries()];
    if (url.search.length > 256 || entries.length > 1 || entries.some(([key, value]) => key !== "station_id" || !SOIL_STATIONS.includes(value))) { status = 400; result = await soilNegative("INVALID_QUERY", now); }
    else {
      const active = await getRawDb().prepare("SELECT a.package_id, a.decision_json, p.state FROM soil_active a LEFT JOIN soil_packages p ON p.package_id = a.package_id WHERE a.singleton = 1").first<{ package_id: string; decision_json: string; state: string }>();
      if (!active || active.state !== "STAGED") result = await soilNegative("NO_APPROVED_SNAPSHOT", now);
      else {
        if (!/^sha256:[a-f0-9]{64}$/.test(active.package_id) || typeof active.decision_json !== "string" || active.decision_json.length > 8192) throw new Error("ACTIVE_METADATA_INVALID");
        const bucket = env.BUCKET as Bucket | undefined;
        if (!bucket) throw new Error("STORAGE_UNAVAILABLE");
        const stored = await bucket.get(`governed-soil/v1/objects/${active.package_id.slice(7)}.json`);
        if (!stored || !Number.isInteger(stored.size) || stored.size < 1 || stored.size > SOIL_PACKAGE_LIMIT) throw new Error("PACKAGE_UNAVAILABLE");
        const text = await stored.text();
        if (new TextEncoder().encode(text).length !== stored.size) throw new Error("PACKAGE_SIZE_MISMATCH");
        const pkg = await parseSoilPackage(text);
        if (pkg.manifest.package_id !== active.package_id) throw new Error("ACTIVE_BINDING_MISMATCH");
        // The gate is evaluated after the storage read, so an approval that lapses meanwhile is refused.
        result = await projectSoil(pkg, object(parseWaterJson(active.decision_json)), view, new Date().toISOString(), url.searchParams.get("station_id"));
      }
    }
  } catch { status = 503; result = await soilNegative("RELEASE_STORE_UNAVAILABLE", now, "ERROR"); }
  // Never log identity headers, query text, source content, or model inputs.
  console.info(JSON.stringify({ event: "governed_read", component: "site-soil", build: "kfm-soil-v1", correlation_id: correlation, source_id: "noaa-uscrn", outcome: result.envelope.outcome, reason_code: result.envelope.reason_code, duration_ms: Date.now() - start }));
  return Response.json(result, { status, headers: { ...SOIL_HEADERS, "X-KFM-Correlation-ID": correlation } });
}
