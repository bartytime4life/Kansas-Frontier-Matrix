import { cachedAviationRoute } from "../../../aviation-route-cache";
import { trafficResponse } from "../../../aviation-traffic-server";

export const dynamic = "force-dynamic";

export async function GET() {
  return cachedAviationRoute("traffic", 15_000, () => trafficResponse());
}
