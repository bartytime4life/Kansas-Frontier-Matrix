import { waterAdminStatus } from "../../../../governed-water-admin";
import { waterAdminFailure, waterAdminHeaders, waterAdminStore, waterOwner } from "../../../../governed-water-admin-server";
export const dynamic = "force-dynamic";

// Owner-only. Reports the active pointer so a release tool can supply expected_active.
export async function GET() {
  try {
    await waterOwner();
    return Response.json(await waterAdminStatus(waterAdminStore()), { headers: waterAdminHeaders });
  } catch (error) { return waterAdminFailure(error); }
}
