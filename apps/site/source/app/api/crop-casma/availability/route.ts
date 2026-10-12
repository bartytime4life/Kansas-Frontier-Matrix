import { cropCasmaRead } from "../../../crop-casma-server";
export const dynamic = "force-dynamic";
export async function GET(request: Request) { return cropCasmaRead(request, "availability"); }
