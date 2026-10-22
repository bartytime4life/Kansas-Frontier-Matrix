import { aviationWeatherResponse } from "../../../aviation-weather-server";

export const dynamic = "force-dynamic";

export async function GET() {
  return aviationWeatherResponse("metar");
}
