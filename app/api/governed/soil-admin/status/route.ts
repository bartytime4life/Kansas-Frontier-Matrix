import { publicAuthorizationStatus } from "../../../../public-release-server";
import { soilAdminStatus } from "../../../../governed-soil-admin";
import { waterAdminFailure, waterAdminHeaders, waterAdminStore, waterOwner, waterWorker } from "../../../../governed-water-admin-server";
export const dynamic = "force-dynamic";

// Owner or staging token. Reports the active and previous soil package ids and the decision's expiry.
export async function GET(request: Request) {
  try {
    if (request.headers.has("authorization")) waterWorker(request);
    else await waterOwner();
    return Response.json({ ...await soilAdminStatus(waterAdminStore()), ...await publicAuthorizationStatus("soil") }, { headers: waterAdminHeaders });
  } catch (error) { return waterAdminFailure(error); }
}
