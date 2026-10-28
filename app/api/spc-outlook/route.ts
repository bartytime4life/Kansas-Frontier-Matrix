import { boundedFetch } from "../event-atlas/upstream";
import { isOutlookProduct, outlookProducts, parseSpcOutlook, spcIntensityProviderUrl, spcOutlookProviderUrl, type OutlookDay, type SpcOutlook } from "../../spc-outlook";

export const dynamic = "force-dynamic";
const MAX_BYTES = 4 * 1024 * 1024;
const FRESH_MS = 10 * 60 * 1000;
const kept = new Map<string, { at: number; outlook: SpcOutlook }>();

/**
 * One SPC outlook: categorical for day 1, 2 or 3, or a tornado, wind or hail
 * probability outlook for day 1 or 2, read with its conditional-intensity
 * areas. Kept ten minutes; SPC reissues day 1 several times a day.
 */
export async function GET(request: Request) {
  const params = new URL(request.url).searchParams;
  const day = Number(params.get("day") ?? "1"), product = params.get("product") ?? "cat";
  const refuse = (message: string) => Response.json({ state: "error", message }, { status: 400, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  if (day !== 1 && day !== 2 && day !== 3) return refuse("Choose outlook day 1, 2 or 3.");
  if (!isOutlookProduct(product) || !outlookProducts(day as OutlookDay).includes(product)) return refuse("Choose the categorical outlook, or tornado, wind or hail for day 1 or 2.");
  const headers = { "Cache-Control": "public, max-age=300, s-maxage=600", "X-Content-Type-Options": "nosniff" };
  const id = `${day}-${product}`;
  const cached = kept.get(id);
  if (cached && Date.now() - cached.at < FRESH_MS) return Response.json(cached.outlook, { headers });
  const now = new Date();
  const source = spcOutlookProviderUrl(day, product);
  try {
    // The intensity areas are a second file; the probabilities still stand without them.
    const [response, intensity] = await Promise.all([
      boundedFetch(source, MAX_BYTES, { timeoutMs: 15_000 }),
      product === "cat" ? Promise.resolve(undefined)
        : boundedFetch(spcIntensityProviderUrl(day, product), MAX_BYTES, { timeoutMs: 15_000 }).then(r => JSON.parse(r.text()) as unknown).catch(() => undefined),
    ]);
    const outlook = parseSpcOutlook(JSON.parse(response.text()) as unknown, day, now.toISOString(), source, product, intensity);
    kept.set(id, { at: now.getTime(), outlook });
    return Response.json(outlook, { headers });
  } catch {
    return Response.json({ state: "unavailable", message: "The SPC outlook is unavailable. Try again, or open it at spc.noaa.gov." },
      { status: 502, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  }
}
