import { stageEarthquakePackage } from "../../../../governed-earthquakes-admin";
import { WaterAdminError } from "../../../../governed-water-admin";
import { readBoundedText, waterAdminFailure, waterAdminHeaders, waterAdminStore, waterWorker } from "../../../../governed-water-admin-server";
import { EARTHQUAKE_PACKAGE_LIMIT } from "../../../../governed-earthquakes";
export const dynamic = "force-dynamic";

// Stores a validated earthquake package for owner review. Never activates. Accepts only the earthquake profile.
export async function POST(request: Request) {
  try {
    waterWorker(request);
    if (!request.headers.get("content-type")?.startsWith("application/json")) throw new WaterAdminError("JSON_REQUIRED", 415);
    const text = await readBoundedText(request, EARTHQUAKE_PACKAGE_LIMIT);
    const result = await stageEarthquakePackage(waterAdminStore(), text, "staging-token", new Date().toISOString());
    return Response.json(result, { headers: waterAdminHeaders });
  } catch (error) { return waterAdminFailure(error); }
}
