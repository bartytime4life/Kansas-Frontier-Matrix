import { boundedFetch } from "../event-atlas/upstream";
import { isChamber, legislatureProviderUrl, parseLegislature, type Chamber, type LegislatureDistricts } from "../../state-legislature";

export const dynamic = "force-dynamic";
const MAX_BYTES = 8 * 1024 * 1024;
const FRESH_MS = 24 * 60 * 60 * 1000;
const kept = new Map<Chamber, { at: number; districts: LegislatureDistricts }>();

/** Kansas Senate or House districts from TIGERweb, the complete edition or none; kept a day, since the plan changes after a census. */
export async function GET(request: Request) {
  const chamber = new URL(request.url).searchParams.get("chamber");
  const noStore = { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" };
  if (!isChamber(chamber)) return Response.json({ state: "error", message: "Choose the senate or the house." }, { status: 400, headers: noStore });
  const headers = { "Cache-Control": "public, max-age=3600, s-maxage=86400", "X-Content-Type-Options": "nosniff" };
  const cached = kept.get(chamber);
  if (cached && Date.now() - cached.at < FRESH_MS) return Response.json(cached.districts, { headers });
  try {
    const response = await boundedFetch(legislatureProviderUrl(chamber), MAX_BYTES, { timeoutMs: 25_000 });
    const districts = parseLegislature(JSON.parse(response.text()) as unknown, chamber, new Date().toISOString());
    kept.set(chamber, { at: Date.now(), districts });
    return Response.json(districts, { headers });
  } catch {
    return Response.json({ state: "unavailable", message: "The Census legislative districts are unavailable; nothing is drawn from part of a plan." }, { status: 502, headers: noStore });
  }
}
