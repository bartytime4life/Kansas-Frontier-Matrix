import { publicDeliveryWithdraw } from "../../../../public-release-admin-server";
export const dynamic = "force-dynamic";
export async function POST(request: Request) { return publicDeliveryWithdraw(request, "groundwater"); }
