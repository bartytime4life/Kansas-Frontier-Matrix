import { stormEventsAdminStatus } from "../../../../governed-storm-events-admin";
import { waterAdminFailure, waterAdminHeaders, waterAdminStore, waterOwner, waterWorker } from "../../../../governed-water-admin-server";
export const dynamic = "force-dynamic";

// Owner or staging token. Reports the active and previous storm events package ids and the decision's expiry.
export async function GET(request: Request) {
  try {
    if (request.headers.has("authorization")) waterWorker(request);
    else await waterOwner();
    return Response.json(await stormEventsAdminStatus(waterAdminStore()), { headers: waterAdminHeaders });
  } catch (error) { return waterAdminFailure(error); }
}
