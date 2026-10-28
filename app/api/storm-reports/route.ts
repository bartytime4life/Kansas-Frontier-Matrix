import { boundedFetch } from "../event-atlas/upstream";
import { parseStormReports, stormReportsProviderUrl, type ReportDay, type StormReports } from "../../storm-reports";

export const dynamic = "force-dynamic";
const MAX_BYTES = 2 * 1024 * 1024;
/** Today's reports arrive through the day; yesterday's settle once its convective day ends. */
const FRESH_MS: Readonly<Record<ReportDay, number>> = { today: 5 * 60 * 1000, yesterday: 30 * 60 * 1000 };
const kept = new Map<ReportDay, { at: number; reports: StormReports }>();

/** SPC's filtered preliminary storm reports for the current ("today") or previous ("yesterday") convective day. */
export async function GET(request: Request) {
  const day = new URL(request.url).searchParams.get("day") ?? "today";
  if (day !== "today" && day !== "yesterday") return Response.json({ state: "error", message: "Choose today's or yesterday's reports." }, { status: 400, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  const headers = { "Cache-Control": `public, max-age=120, s-maxage=${FRESH_MS[day] / 1000}`, "X-Content-Type-Options": "nosniff" };
  const cached = kept.get(day);
  if (cached && Date.now() - cached.at < FRESH_MS[day]) return Response.json(cached.reports, { headers });
  const now = new Date();
  const source = stormReportsProviderUrl(day);
  try {
    const response = await boundedFetch(source, MAX_BYTES, { timeoutMs: 15_000 });
    const reports = parseStormReports(response.text(), day, now, source);
    kept.set(day, { at: now.getTime(), reports });
    return Response.json(reports, { headers });
  } catch {
    return Response.json({ state: "unavailable", message: "The SPC storm reports are unavailable. Try again, or open them at spc.noaa.gov." },
      { status: 502, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  }
}
