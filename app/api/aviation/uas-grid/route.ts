import { cachedAviationRoute } from "../../../aviation-route-cache";
import { uasGridResponse } from "../../../aviation-drone-server";

export const dynamic = "force-dynamic";

export async function GET() {
  return cachedAviationRoute("uas-grid", 86_400_000, () => uasGridResponse());
}
