import { activateWaterPackage, WaterAdminError } from "../../../../governed-water-admin";
import { readBoundedText, waterAdminFailure, waterAdminHeaders, waterAdminStore, waterOwner, waterSameOrigin } from "../../../../governed-water-admin-server";
import { parseWaterJson } from "../../../../governed-water";
export const dynamic = "force-dynamic";

// Owner-only. Activates (or rolls back to) a staged package with a decision that passes the serving gate.
export async function POST(request: Request) {
  try {
    waterSameOrigin(request);
    await waterOwner();
    if (!request.headers.get("content-type")?.startsWith("application/json")) throw new WaterAdminError("JSON_REQUIRED", 415);
    let body: unknown;
    try { body = parseWaterJson(await readBoundedText(request, 16 * 1024)); } catch (error) { if (error instanceof WaterAdminError) throw error; throw new WaterAdminError("ACTIVATION_REQUEST_INVALID", 400); }
    return Response.json(await activateWaterPackage(waterAdminStore(), body, new Date().toISOString()), { headers: waterAdminHeaders });
  } catch (error) { return waterAdminFailure(error); }
}
