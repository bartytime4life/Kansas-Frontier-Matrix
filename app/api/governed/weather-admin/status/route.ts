import { publicAuthorizationStatus } from "../../../../public-release-server";
import { weatherAdminStatus } from "../../../../governed-weather-admin";
import { waterAdminFailure, waterAdminHeaders, waterAdminStore, waterOwner, waterWorker } from "../../../../governed-water-admin-server";
export const dynamic = "force-dynamic";

// Owner or staging token. Reports the active and previous weather package ids and the decision's expiry.
export async function GET(request: Request) {
  try {
    if (request.headers.has("authorization")) waterWorker(request);
    else await waterOwner();
    return Response.json({ ...await weatherAdminStatus(waterAdminStore()), ...await publicAuthorizationStatus("weather") }, { headers: waterAdminHeaders });
  } catch (error) { return waterAdminFailure(error); }
}
