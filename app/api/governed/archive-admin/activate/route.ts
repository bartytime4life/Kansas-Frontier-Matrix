import { publicDeliveryActivate } from "../../../../public-release-admin-server";
export const dynamic = "force-dynamic";
export async function POST(request: Request) { return publicDeliveryActivate(request, "archive"); }
