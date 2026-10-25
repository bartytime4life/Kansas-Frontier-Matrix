import { cachedAviationRoute } from "../../../aviation-route-cache";
import { aviationWeatherResponse } from "../../../aviation-weather-server";

export const dynamic = "force-dynamic";

export async function GET() {
  return cachedAviationRoute("metar", 120_000, () => aviationWeatherResponse("metar"));
}
