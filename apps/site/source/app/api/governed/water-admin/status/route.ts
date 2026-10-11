import { waterAdminStatus } from "../../../../governed-water-admin";
import { waterAdminFailure, waterAdminHeaders, waterAdminStore, waterOwner, waterWorker } from "../../../../governed-water-admin-server";
export const dynamic = "force-dynamic";

// Owner or staging token. Reports only the active and previous package ids, so the
// release tool can bind a replacement's rollback target and the page can supply expected_active.
export async function GET(request: Request) {
  try {
    if (request.headers.has("authorization")) waterWorker(request);
    else await waterOwner();
    return Response.json(await waterAdminStatus(waterAdminStore()), { headers: waterAdminHeaders });
  } catch (error) { return waterAdminFailure(error); }
}
