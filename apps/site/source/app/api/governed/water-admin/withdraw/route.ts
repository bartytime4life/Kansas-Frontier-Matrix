import { withdrawWaterPackage, WaterAdminError } from "../../../../governed-water-admin";
import { readBoundedText, waterAdminFailure, waterAdminHeaders, waterAdminStore, waterOwner, waterSameOrigin } from "../../../../governed-water-admin-server";
import { parseWaterJson } from "../../../../governed-water";
export const dynamic = "force-dynamic";

// Owner-only. A withdrawn package stops serving at once, even while it is the active pointer.
export async function POST(request: Request) {
  try {
    waterSameOrigin(request);
    await waterOwner();
    if (!request.headers.get("content-type")?.startsWith("application/json")) throw new WaterAdminError("JSON_REQUIRED", 415);
    let body: unknown;
    try { body = parseWaterJson(await readBoundedText(request, 1024)); } catch (error) { if (error instanceof WaterAdminError) throw error; throw new WaterAdminError("WITHDRAW_REQUEST_INVALID", 400); }
    return Response.json(await withdrawWaterPackage(waterAdminStore(), body, new Date().toISOString()), { headers: waterAdminHeaders });
  } catch (error) { return waterAdminFailure(error); }
}
