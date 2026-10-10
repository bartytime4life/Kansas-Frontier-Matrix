import { stageWaterPackage, WaterAdminError } from "../../../../governed-water-admin";
import { readBoundedText, waterAdminFailure, waterAdminHeaders, waterAdminStore, waterWorker } from "../../../../governed-water-admin-server";
import { WATER_PACKAGE_LIMIT } from "../../../../governed-water";
export const dynamic = "force-dynamic";

// Stores a validated package for owner review. Never activates.
export async function POST(request: Request) {
  try {
    waterWorker(request);
    if (!request.headers.get("content-type")?.startsWith("application/json")) throw new WaterAdminError("JSON_REQUIRED", 415);
    const text = await readBoundedText(request, WATER_PACKAGE_LIMIT);
    const result = await stageWaterPackage(waterAdminStore(), text, "staging-token", new Date().toISOString());
    return Response.json(result, { headers: waterAdminHeaders });
  } catch (error) { return waterAdminFailure(error); }
}
