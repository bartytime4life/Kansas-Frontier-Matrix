import { publicDeliveryStage } from "../../../../public-release-admin-server";
export const dynamic = "force-dynamic";
export async function POST(request: Request) { return publicDeliveryStage(request, "groundwater"); }
