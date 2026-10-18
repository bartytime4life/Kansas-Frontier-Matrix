import { publicDeliveryStatus } from "../../../../public-release-admin-server";
export const dynamic = "force-dynamic";
export async function GET(request: Request) { return publicDeliveryStatus(request, "groundwater"); }
