import { publicStageAuthorization } from "../../../../public-release-server";
import { stageWeatherPackage } from "../../../../governed-weather-admin";
import { WaterAdminError } from "../../../../governed-water-admin";
import { readBoundedText, waterAdminFailure, waterAdminHeaders, waterAdminStore, waterWorker } from "../../../../governed-water-admin-server";
import { WEATHER_PACKAGE_LIMIT } from "../../../../governed-weather";
export const dynamic = "force-dynamic";

// Stores a validated weather package for owner review. Never activates. Accepts only the weather profile.
export async function POST(request: Request) {
  try {
    waterWorker(request);
    if (!request.headers.get("content-type")?.startsWith("application/json")) throw new WaterAdminError("JSON_REQUIRED", 415);
    const text = await readBoundedText(request, WEATHER_PACKAGE_LIMIT);
    await publicStageAuthorization("weather", text, request);
    const result = await stageWeatherPackage(waterAdminStore(), text, "staging-token", new Date().toISOString());
    return Response.json(result, { headers: waterAdminHeaders });
  } catch (error) { return waterAdminFailure(error); }
}
