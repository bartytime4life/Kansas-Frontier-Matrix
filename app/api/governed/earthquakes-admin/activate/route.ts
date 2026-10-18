import { publicDecisionForActivation } from "../../../../public-release-server";
import { activateEarthquakePackage } from "../../../../governed-earthquakes-admin";
import { WaterAdminError } from "../../../../governed-water-admin";
import { readBoundedText, waterAdminFailure, waterAdminHeaders, waterAdminStore, waterOwner, waterSameOrigin } from "../../../../governed-water-admin-server";
import { parseWaterJson } from "../../../../governed-water";
export const dynamic = "force-dynamic";

// Owner-only. Activates (or rolls back to) a staged earthquake package with a decision that passes the earthquake gate.
export async function POST(request: Request) {
  try {
    waterSameOrigin(request);
    await waterOwner();
    if (!request.headers.get("content-type")?.startsWith("application/json")) throw new WaterAdminError("JSON_REQUIRED", 415);
    let body: unknown;
    try { body = parseWaterJson(await readBoundedText(request, 16 * 1024)); } catch (error) { if (error instanceof WaterAdminError) throw error; throw new WaterAdminError("ACTIVATION_REQUEST_INVALID", 400); }
    if (!body || typeof body !== "object" || Array.isArray(body)) throw new WaterAdminError("ACTIVATION_REQUEST_INVALID", 400);
    const publicRequest = body as Record<string, unknown>;
    if (Object.keys(publicRequest).some(key => !["package_id", "expected_active", "rollback"].includes(key)) || typeof publicRequest.package_id !== "string") throw new WaterAdminError("PUBLIC_ACTIVATION_INVALID", 400);
    body = { ...publicRequest, decision: await publicDecisionForActivation("earthquakes", publicRequest.package_id, request) };
    return Response.json(await activateEarthquakePackage(waterAdminStore(), body, new Date().toISOString()), { headers: waterAdminHeaders });
  } catch (error) { return waterAdminFailure(error); }
}
