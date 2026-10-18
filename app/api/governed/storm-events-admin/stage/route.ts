import { publicStageAuthorization } from "../../../../public-release-server";
import { stageStormEventsPackage } from "../../../../governed-storm-events-admin";
import { WaterAdminError } from "../../../../governed-water-admin";
import { readBoundedText, waterAdminFailure, waterAdminHeaders, waterAdminStore, waterWorker } from "../../../../governed-water-admin-server";
import { STORM_EVENTS_PACKAGE_LIMIT } from "../../../../governed-storm-events";
export const dynamic = "force-dynamic";

// Stores a validated storm events package for owner review. Never activates. Accepts only the storm events profile.
export async function POST(request: Request) {
  try {
    waterWorker(request);
    if (!request.headers.get("content-type")?.startsWith("application/json")) throw new WaterAdminError("JSON_REQUIRED", 415);
    const text = await readBoundedText(request, STORM_EVENTS_PACKAGE_LIMIT);
    await publicStageAuthorization("storm-events", text, request);
    const result = await stageStormEventsPackage(waterAdminStore(), text, "staging-token", new Date().toISOString());
    return Response.json(result, { headers: waterAdminHeaders });
  } catch (error) { return waterAdminFailure(error); }
}
