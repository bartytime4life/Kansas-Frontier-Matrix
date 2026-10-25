import { cachedAviationRoute } from "../../../aviation-route-cache";
import { tfrResponse } from "../../../aviation-drone-server";

export const dynamic = "force-dynamic";

export async function GET() {
  return cachedAviationRoute("tfrs", 300_000, () => tfrResponse());
}
