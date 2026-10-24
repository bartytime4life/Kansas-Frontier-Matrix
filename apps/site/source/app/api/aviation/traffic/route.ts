import { trafficResponse } from "../../../aviation-traffic-server";

export const dynamic = "force-dynamic";

export async function GET() {
  return trafficResponse();
}
