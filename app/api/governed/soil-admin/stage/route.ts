import { stageSoilPackage } from "../../../../governed-soil-admin";
import { WaterAdminError } from "../../../../governed-water-admin";
import { readBoundedText, waterAdminFailure, waterAdminHeaders, waterAdminStore, waterWorker } from "../../../../governed-water-admin-server";
import { SOIL_PACKAGE_LIMIT } from "../../../../governed-soil";
export const dynamic = "force-dynamic";

// Stores a validated soil package for owner review. Never activates. Accepts only the soil profile.
export async function POST(request: Request) {
  try {
    waterWorker(request);
    if (!request.headers.get("content-type")?.startsWith("application/json")) throw new WaterAdminError("JSON_REQUIRED", 415);
    const text = await readBoundedText(request, SOIL_PACKAGE_LIMIT);
    const result = await stageSoilPackage(waterAdminStore(), text, "staging-token", new Date().toISOString());
    return Response.json(result, { headers: waterAdminHeaders });
  } catch (error) { return waterAdminFailure(error); }
}
