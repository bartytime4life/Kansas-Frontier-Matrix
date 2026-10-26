import { boundedFetch } from "../event-atlas/upstream";
import { parseSpcOutlook, spcOutlookProviderUrl, type OutlookDay, type SpcOutlook } from "../../spc-outlook";

export const dynamic = "force-dynamic";
const MAX_BYTES = 4 * 1024 * 1024;
const FRESH_MS = 10 * 60 * 1000;
const kept = new Map<OutlookDay, { at: number; outlook: SpcOutlook }>();

/** One SPC categorical outlook (day 1, 2 or 3), kept ten minutes; SPC reissues day 1 several times a day. */
export async function GET(request: Request) {
  const day = Number(new URL(request.url).searchParams.get("day") ?? "1");
  if (day !== 1 && day !== 2 && day !== 3) return Response.json({ state: "error", message: "Choose outlook day 1, 2 or 3." }, { status: 400, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  const headers = { "Cache-Control": "public, max-age=300, s-maxage=600", "X-Content-Type-Options": "nosniff" };
  const cached = kept.get(day);
  if (cached && Date.now() - cached.at < FRESH_MS) return Response.json(cached.outlook, { headers });
  const now = new Date();
  const source = spcOutlookProviderUrl(day);
  try {
    const response = await boundedFetch(source, MAX_BYTES, { timeoutMs: 15_000 });
    const outlook = parseSpcOutlook(JSON.parse(response.text()) as unknown, day, now.toISOString(), source);
    kept.set(day, { at: now.getTime(), outlook });
    return Response.json(outlook, { headers });
  } catch {
    return Response.json({ state: "unavailable", message: "The SPC outlook is unavailable. Try again, or open it at spc.noaa.gov." },
      { status: 502, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  }
}
